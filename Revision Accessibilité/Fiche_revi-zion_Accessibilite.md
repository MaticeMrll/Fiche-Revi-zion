# Fiche de révision – Accessibilité des systèmes interactifs

## 1. Principes clés
- **Accessibilité numérique** : rendre contenus et services compréhensibles, utilisables et contributifs par toute personne, quelles que soient ses capacités (W3C, DINUM).
- **Principe “Web for All”** : ambition de Tim Berners-Lee de garantir l’accès au web indépendamment du matériel, de la langue, de la culture ou des aptitudes.
- **Accessibilité = facteur d’inclusion** : bénéfices pour les personnes handicapées, les situations de handicap temporaires, les seniors, mais aussi pour l’ensemble des utilisateurs (ergonomie, SEO, RSE).
- **Accessibilité ≠ accessibilité “à part”** : éviter les versions alternatives pauvres ; viser des expériences unifiées.
- **Situationally Induced Impairments and Disabilities (SIID)** : l’environnement peut créer des limitations temporaires ; concevoir pour ces situations améliore la robustesse globale.

## 2. Cadre légal et réglementaire
- **International**
  - *ADA (USA)* : interdit la discrimination et impose l’accessibilité des TIC fédérales (Section 508 → WCAG 2.0 niveau A).
  - *European Accessibility Act (2019/882)* : harmonise l’accessibilité des produits et services clés (transport, e-commerce, éducation, emploi).
- **France**
  - *Loi handicap 2005* (article 47) : obligation d’accessibilité des services publics.
  - *RGAA* : référentiel national, révisé en 2019 (v4) → alignement WCAG 2.1 + EN 301 549.
  - *Ordonnance 2023* : renforce sanctions (20 000 € pour services publics, 50 000 € pour récidive).
  - *Directive 2025* : obligation d’accessibilité pour secteurs public et entreprises >10 salariés et CA >2 M€ (web, intranet, appli, mobiliers numériques).
  - *Commerce en ligne* : nouveaux services accessibles dès 2025, existants avant 2030 (directive 2019/882).
- **Obligations déclaratives**
  - Afficher le **niveau de conformité** (pleinement, partiellement, non conforme).
  - Publier une **déclaration d’accessibilité** à jour.
  - Mettre en place un **schéma pluriannuel (≤3 ans)** + plan d’action annuel détaillé.
  - Fournir un **mécanisme de contact** et un recours (défenseur des droits).

## 3. Types de handicaps & besoins associés

| Handicap | Exemples de difficultés | Leviers d’accessibilité |
| --- | --- | --- |
| **Visuel** (cécité, DMLA, daltonisme, glaucome…) | Perte d’acuité, de couleurs, de champ visuel | Texte alternatif descriptif, contraste ≥ 4.5:1 (AA), taille adaptable, structure sémantique, audiodescription, navigation clavier, éviter “cliquez ici” |
| **Auditif** (surdité perception/transmission) | Compréhension orale limitée, acquisition langage | Sous-titres synchronisés, transcription, langue des signes, visuel fort, lexique clair |
| **Moteur** (IMC, quadriplégie, tremblements…) | Viser / cliquer, maintenir, saisir | Commande clavier complète, zones cliquables suffisantes, délais ajustables, support des aides (switch, eye-tracking, commandes vocales) |
| **Cognitif / mental** (TSA, TDAH, dys, Alzheimer…) | Charge cognitive, compréhension, mémoire | Information simplifiée (FALC), hiérarchie claire, animations limitées, instructions explicites, feedbacks prévisibles |
| **Situations temporaires / contextuelles** | Marche, stress, bruit, luminosité | Principes d’universal design, réactivité des interfaces, tolérance aux erreurs |

## 4. Concepts avancés
- **Modèles du handicap**
  - Biomédical (centré déficience) vs social (centré environnement & droits).
  - OMS (CIH 1980 → CIF 2001) : déficience / incapacité / handicap.
- **Accessibilité normative vs effective**
  - *Normative* : conformité (efficacité).
  - *Effective* : efficacité + efficience + satisfaction (expérience réelle).
- **Ability-Based Design (Wobbrock et al.)**
  - Partir des capacités réelles de l’utilisateur et adapter l’interface (ex. WalkType, SwitchBack).
  - Prise en compte des SIID, adaptation contextuelle.
- **Universal Design (Mace, 1991)**
  - Sept principes : usage équitable, flexible, simple, information perceptible, tolérance à l’erreur, effort réduit, dimensions adéquates.
  - Application large (interfaces, mobilier urbain, packaging).

## 5. Normes et référentiels
- **WCAG 2.1** – 4 principes P.O.U.R. :
  - *Perceptible* : alternatives textuelles, médias temporels, adaptabilité, contrastes.
  - *Utilisable* : navigation clavier, délais suffisants, éviter flashs, focus visible.
  - *Compréhensible* : langage clair, comportements prévisibles, aide à la saisie.
  - *Robuste* : compatibilité outils d’assistance, HTML valide.
- **Niveaux de conformité** : A (minimum), AA (référence légale UE), AAA (avancé).
- **RGAA 4.1** : 13 thématiques, 106 critères couvrant images, cadres, couleurs, multimédia, tableaux, liens, scripts, éléments obligatoires, structuration, présentation, formulaires, navigation, consultation.
- **ARIA (Accessible Rich Internet Applications)**
  - Utilisation parcimonieuse pour compléter la sémantique native.
  - `role`, `aria-label`, `aria-describedby`, `aria-expanded`, etc.
  - Attention au rôle `presentation` qui supprime la sémantique.

## 6. Bonnes pratiques de conception & développement
- **Structure HTML**
  - Un seul `<h1>` par page, progression hiérarchique logique (`<h2>`, `<h3>`, …).
  - Balises structurelles : `<header>`, `<nav>`, `<main>` (unique), `<footer>`.
  - Citations via `<q>` (inline) ou `<blockquote>` + attribut `cite`.
- **Images**
  - Attribut `alt` pertinent si image informative, vide si purement décorative.
  - Légendes via `<figure>` + `<figcaption>`.
- **Couleurs & contrastes**
  - Information jamais transmise par la couleur seule.
  - Ratio ≥ 4.5:1 (AA texte normal) / 3:1 (large ou focus personnalisé).
- **Multimédia**
  - Sous-titres, transcription, audiodescription, contrôle de lecture.
  - Sons automatiques désactivables.
- **Liens & boutons**
  - Intitulé explicite (“Télécharger le rapport PDF”, “Aller au formulaire”).
  - Liens d’évitement (“Aller au contenu principal”) en premier élément focusable.
  - Boutons pour actions (`<button>`), liens pour navigation (`<a href>`).
- **Formulaires**
  - Association `label for` ↔ `id`, mention explicite des champs obligatoires.
  - Messages d’erreur clairs + suggestion de correction.
  - `autocomplete` normalisé, éviter d’utiliser `placeholder` comme étiquette.
- **Tableaux**
  - `<caption>` pour le titre, `<th scope="col/row">`, résumés pour structures complexes.
- **Navigation**
  - Parcours clavier complet, ordre de tabulation cohérent, focus visible.
  - Au moins deux systèmes : menu, plan du site, moteur de recherche.
- **Langues**
  - `lang` sur `<html>`, `lang` local pour changements ponctuels.
- **Scripts**
  - Compatibles AT (éviter navigation uniquement via `onclick`).
  - Interactions accessibles via clavier et dispositifs de pointage.
- **Animations & contenus dynamiques**
  - Contrôle par l’utilisateur (pause, stop), éviter flashes dangereux (>3 Hz).
- **Tests utilisateurs**
  - Intégrer des testeurs handicapés pour valider l’accessibilité effective.
- **Surcouches “magiques”**
  - Ne garantissent ni conformité ni accessibilité réelle (cf. RGAA).

## 7. Méthodologie d’audit & conformité
1. **Sélection des pages** : accueil, contact, mentions légales, accessibilité, plan du site, aide, authentification + pages à formulaires ou médias.
2. **Échantillonnage & tests** :
   - Vérifier chaque critère RGAA → statut conforme / non conforme / non applicable / non testé.
   - Un seul échec rend le critère globalement non conforme.
3. **Rapport d’audit** :
   - Liste des écarts, gravité, recommandations correctives.
   - Proposition d’un plan de mise en conformité (priorisation, chiffrage).
4. **Suivi** :
   - Mesurer le **taux de conformité** (0–49 % non conforme ; 50–99 % partiellement conforme ; 100 % conforme).
   - Mettre à jour la déclaration, le schéma pluriannuel et le plan annuel.

## 8. Technologies d’assistance & outils
- **Lecteurs d’écran** : NVDA, JAWS, VoiceOver (navigation flèches, tabulation, listes de liens via Inser + F7, etc.).
- **Plages braille**, **synthèses vocales**, commandes vocales, switches, eye-tracking.
- **Outils d’évaluation** :
  - Assistant RGAA (Firefox), Accessibility Insights, axe DevTools, HeadingsMap, WCAG Contrast Checker, W3C HTML Validator.
- **Ressources** :
  - https://accessibilite.numerique.gouv.fr/, https://www.w3.org/WAI/, blogs Idéance & Stephanie Walter, checklist design-accessible.fr.

## 9. Projet pédagogique (DH x Polytech Nice)
- Audit basé sur 20 critères RGAA (HTML sémantique, navigation clavier, contrastes, médias).
- Développement de trois pages accessibles (accueil, contact, blog) :
  - Code structuré (HTML5, ARIA limitée).
  - Contenus testés par des utilisateurs handicapés (moteur, visuel, auditif, cognitif).
  - Livrables : prototype fonctionnel, rapport d’audit, présentation (personas, recommandations).
- Évaluation (20 pts) :
  - 11 pts accessibility (RGAA, code accessible, personas, recommandations).
  - 7 pts école (distinction handicaps permanents/temp., enjeux du code, recherche de ressources).
  - Bonus présentation claire + réponses aux questions.

## 10. Chiffres clés & sensibilisation
- 1 milliard de personnes handicapées dans le monde (~15 %).
- 18 % de la population française concernée, 80 % des handicaps sont invisibles.
- ~3 % des sites web seraient pleinement accessibles (source CNCPH).
- 8 % des hommes (0,5 % des femmes) daltoniens → ne pas communiquer l’information par la couleur seule.
- Statistiques SIID : marcher, téléphoner, stress… chacun peut expérimenter des limitations.

## 11. Messages à retenir
- L’accessibilité est un **droit fondamental** et un **enjeu d’équité**.
- Conformité réglementaire nécessaire mais **insuffisante sans tests réels**.
- **Conception universelle** et **ability-based design** permettent d’anticiper les SIID.
- L’accessibilité doit être pensée **dès le départ** : plus économique, meilleure UX, meilleure image.
- Travailler en **équipe pluridisciplinaire** (développeurs, designers, juristes, communication, testeurs).
- **Pas d’accessibilité sans personnes handicapées** impliquées dans l’évaluation.
