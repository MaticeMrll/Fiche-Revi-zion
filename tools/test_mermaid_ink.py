import zlib, base64, urllib.request

code = 'graph TD;A-->B;'

def enc(zdata: bytes) -> str:
    return base64.urlsafe_b64encode(zdata).decode('ascii').rstrip('=')

# zlib wrapped
enc1 = enc(zlib.compress(code.encode('utf-8')))
url1 = f'https://mermaid.ink/svg/{enc1}'

# raw deflate
co = zlib.compressobj(level=9, wbits=-15)
comp2 = co.compress(code.encode('utf-8')) + co.flush()
enc2 = enc(comp2)
url2 = f'https://mermaid.ink/svg/{enc2}'

for url in (url1, url2):
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            data = r.read()
            print('OK', url, len(data), r.status)
    except Exception as e:
        print('ERR', url, e)

