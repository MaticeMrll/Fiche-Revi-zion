import os
import re
import hashlib
import urllib.request
import urllib.error
import zlib
import base64
from pathlib import Path


KROKI_ENDPOINT = os.environ.get("KROKI_ENDPOINT", "https://kroki.io")
DIAGRAM_FORMAT = os.environ.get("DIAGRAM_FORMAT", "svg")  # svg or png
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "mermaid-images")


def find_markdown_files(root: Path):
    for p in root.rglob("*.md"):
        yield p


def iter_mermaid_blocks(text: str):
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        # Triple backticks fence
        if line.strip().lower().startswith("```mermaid"):
            start = i
            i += 1
            block_lines = []
            while i < len(lines) and lines[i].strip() != "```":
                block_lines.append(lines[i])
                i += 1
            end = i  # line with closing ``` or EOF
            code = "\n".join(block_lines)
            yield (start, end, code, "triple")
        # Single backtick fence as observed in the repo
        elif line.strip().lower().startswith("`mermaid"):
            start = i
            i += 1
            block_lines = []
            while i < len(lines) and lines[i].strip() != "`":
                block_lines.append(lines[i])
                i += 1
            end = i  # line with closing ` or EOF
            code = "\n".join(block_lines)
            yield (start, end, code, "single")
        else:
            i += 1


def _deflate_base64url(data: bytes) -> str:
    co = zlib.compressobj(level=9, wbits=-15)
    comp = co.compress(data) + co.flush()
    return base64.urlsafe_b64encode(comp).decode("ascii").rstrip("=")


def render_mermaid(code: str, out_path: Path) -> None:
    # Render via mermaid.ink (stateless). Supports svg/png.
    fmt = DIAGRAM_FORMAT.lower()
    if fmt not in ("svg", "png"):
        fmt = "svg"
    encoded = _deflate_base64url(code.encode("utf-8"))
    url = f"https://mermaid.ink/{fmt}/{encoded}"
    req = urllib.request.Request(url, method="GET")
    req.add_header("User-Agent", "codex-cli-mermaid-renderer/1.0")
    req.add_header("Accept", "image/svg+xml" if fmt == "svg" else "image/png")
    import time
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                content = resp.read()
                out_path.parent.mkdir(parents=True, exist_ok=True)
                with open(out_path, "wb") as f:
                    f.write(content)
                return
        except Exception as e:
            last_err = e
            time.sleep(1.0 * (attempt + 1))
    raise RuntimeError(f"mermaid.ink render failed: {last_err}")


def replace_blocks(md_path: Path, root: Path, out_root: Path) -> int:
    original = md_path.read_text(encoding="utf-8", errors="replace")
    lines = original.splitlines()
    # Collect blocks first (indices can shift on in-place edits)
    blocks = list(iter_mermaid_blocks(original))
    if not blocks:
        return 0

    # Process from the end to preserve indices
    count = 0
    for start, end, code, fence in reversed(blocks):
        if not code.strip():
            continue
        sha = hashlib.sha1(code.encode("utf-8")).hexdigest()[:10]
        base = md_path.stem
        img_name = f"{base}-mermaid-{sha}.{DIAGRAM_FORMAT}"
        out_path = out_root / img_name
        if not out_path.exists():
            render_mermaid(code, out_path)
        # Compute relative path from markdown file directory
        rel = os.path.relpath(out_path, start=md_path.parent)

        # Build replacement: image with HTML comment containing original code
        alt = f"Diagramme Mermaid ({base})"
        image_md = f"![{alt}]({rel.replace(os.sep, '/')})"
        comment_start = "<!-- Mermaid source replaced by image:\n"
        comment_body = code.replace("-->", "--&gt;")  # avoid breaking comments
        comment_end = "\n-->"
        replacement = [image_md, comment_start + comment_body + comment_end]

        # Determine closing marker line index (inclusive)
        close_idx = end
        if fence == "triple":
            # Skip closing ``` line if present
            if close_idx < len(lines) and lines[close_idx].strip() == "```":
                pass  # will drop it by replacing the whole slice
        elif fence == "single":
            if close_idx < len(lines) and lines[close_idx].strip() == "`":
                pass

        # Replace slice [start, close_idx] inclusive with replacement lines
        # Python slice end is exclusive, so use close_idx+1
        lines[start:close_idx + 1] = replacement
        count += 1

    new_text = "\n".join(lines) + ("\n" if original.endswith("\n") else "")
    md_path.write_text(new_text, encoding="utf-8")
    return count


def main():
    repo_root = Path.cwd()
    out_root = repo_root / OUTPUT_DIR
    total = 0
    changed_files = 0
    for md in find_markdown_files(repo_root):
        n = replace_blocks(md, repo_root, out_root)
        if n:
            changed_files += 1
            total += n
            print(f"Updated {md} ({n} diagram(s))")
    print(f"Done. {changed_files} file(s) updated, {total} diagram(s) rendered.")


if __name__ == "__main__":
    main()
