# Fiche de Révision — Conception de Systèmes Interactifs (CEIHM)



## Sommaire
- S1 — Introduction (Usability, UX, UCD)
- S2 — Utilisateurs (groupes, rôles, personae, questionnaires)
- S3 — Prototypage (fidélité, typologies, annotations)
- S4 — Modèles de tâches (CTT, GOMS/KLM, HAMSTERS)
- S5 — Design Rationale (QOC, Norman, task–artifact)
- S6 — Inspection (Heuristics, Walkthrough, GOMS/KLM)

---

## S1 — Introduction (l’essentiel visuel)

### À retenir
- Usability (ISO 9241): efficacité, efficience, satisfaction.
- UX (ISO 9241‑210): expérience avant/pendant/après l’usage (dimensions hédoniques).
- Principes clés: predictability, consistency, observability, recoverability, responsiveness.
- Accessibilité: concevoir pour tous (sensoriel, moteur, cognitif, contexte technique).
- UCD: comprendre contexte → fixer exigences → concevoir → évaluer → itérer.



### Définitions rapides
- Usability: aptitude d’un système à être utilisé avec efficacité/efficience/satisfaction.
- UX: perceptions et réponses de l’utilisateur face à l’usage (temps court/long).
- Accessibilité: accès équitable aux fonctionnalités malgré limitations ou contextes.

---

## S2 — Utilisateurs

### À retenir
- Identifier les groupes (primaire/secondaire/représentant/acheteur) et leur variabilité.
- Rôles vs Personae: rôles = responsabilités/tâches ; personae = archétypes riches.
- Méthodes: entretiens, observations, focus groups, tri de cartes, questionnaires.

### Modèle — Matrice utilisateur × tâche
| Utilisateurs           | Tâche A | Tâche B | Tâche C | Fréquence |
|------------------------|:------:|:------:|:------:|:---------:|
| Novice clinicien       |   X    |   X    |        |  Régulier |
| Expert clinicien       |   X    |   X    |   X    |  Fréquent |
| Patient / famille      |   X    |        |   X    | Occasionnel|

### Modèle — Template de Persona
| Champ         | Exemple |
|---------------|---------|
| Nom / Rôle    | Alice, Assistante médicale |
| Objectifs     | Gagner du temps à l’accueil |
| Pain points   | Erreurs de saisie, files d’attente |
| Contexte      | Bruit, pics d’affluence |
| Compétences   | Intermédiaire informatique |



---

## S3 — Prototypage

### À retenir
- Pourquoi: communiquer, explorer, tester tôt, documenter alternatives, décider.
- Fidélité: Low‑fi (papier) pour explorer; Hi‑fi pour tester look&feel/flux réalistes.
- Typologies (Mackay/Beaudouin‑Lafon): représentation, précision, interactivité, évolution.
- Annotations: clarifier, questionner, valider, planifier (outils: Balsamiq, Uxpin…)



### Récap — Stratégies
- Étendre l’espace de conception: générer options (horizontal/vertical, tâches/scénarios).
- Contracter: sélectionner, raffiner, itérer (tracer les choix et le pourquoi).

---

## S4 — Modèles de tâches

### À retenir
- Objectif: comprendre le travail réel, structurer, analyser et réutiliser.
- Notations: HTA, GOMS/KLM, UAN, CTT, HAMSTERS.
- CTT: hiérarchie + opérateurs temporels (>>, [>, |>, [ ], *, |||, |=|, [T]).



### Opérateurs CTT (exemples)
```text
T1 >> T2      : T2 après T1 (enabling)
T1 [> T2      : T2 interrompu par fin de T1 (disabling)
T1 |> T2      : T2 peut interrompre T1 (interruption)
T1 [ ] T2     : choix exclusif
T1*           : itération
T1 ||| T2     : concurrence libre
T1 |=| T2     : concurrence avec synchronisation de fin
[T]           : tâche optionnelle
```

### GOMS/KLM — Feuille rapide
| Opérateur | Signification         | Temps typ. |
|-----------|-----------------------|------------|
| K         | Keypress / click      | 0,2 s      |
| P         | Pointage (souris)     | 1,1 s      |
| H         | Homing (main clavier/souris) | 0,4 s |
| M         | Préparation mentale   | ~1,2 s     |

---

## S5 — Design Rationale

### À retenir
- Rationale: expliciter issues → options → critères → décisions (traçabilité).
- S’appuyer sur théories (Norman) et scénarios/claims (bénéfices/risques).



### QOC — Grille
| Question | Options | Critères | Décision | Pourquoi |
|----------|---------|---------|----------|----------|
| Ex: Choix navigation | Menu latéral / Onglets | Temps, erreurs, apprentissage | Onglets | +Rapide, -erreurs |



---

## S6 — Inspection

### Panorama
- Inspection (experts): Heuristic Evaluation, Cognitive Walkthrough, revues normes.
- Tests utilisateurs, enquêtes/questionnaires, analyses par modèles (GOMS/KLM).

### 10 Heuristiques (Nielsen & Molich)
| # | Intitulé (rappel)                     | Résumé actionnable |
|---|--------------------------------------|--------------------|
| 1 | Dialogues simples et naturels        | Centrés tâches, info pertinente uniquement |
| 2 | Langage de l’utilisateur             | Termes familiers, pas de jargon technique |
| 3 | Charge cognitive minimale            | Favoriser reconnaissance, formats explicites |
| 4 | Cohérence                            | Mêmes actions → mêmes effets |
| 5 | Feedback                             | Statuts clairs, temps de réponse adaptés |
| 6 | Sorties explicites / annulation      | Undo, annuler, interrompre |
| 7 | Raccourcis                           | Accélérateurs pour experts |
| 8 | Messages d’erreur utiles             | Clairs, cause + solution |
| 9 | Concevoir pour les erreurs           | Prévenir slips/mistakes, protections |
|10 | Aide et documentation                | Recherche, compréhension, application |



### GOMS/KLM — Utilisation
- Estimer temps/erreurs pour comparer 2 designs.
- Spécifique à tâches séquentielles (limites pour collaboratif/interruptions).

---

## Mini‑checklists (imprimables)

### Avant test utilisateur
- [ ] Personae/segments validés
- [ ] Scénarios réalistes (pré/post‑conditions)
- [ ] Hypothèses/mesures (succès, erreurs, temps, SUS/NASA‑TLX)
- [ ] Consentement, matériel, script, débrief

### Revue heuristique rapide
- [ ] Jargon remplacé par termes métier
- [ ] États/feedback visibles et utiles
- [ ] Actions critiques annulables
- [ ] Chemins experts disponibles
- [ ] Messages d’erreur actionnables

---

## Définitions flash
- Usability: efficacité/efficience/satisfaction en contexte d’usage.
- UX: perceptions/réactions avant‑pendant‑après usage.
- Persona: archétype utilisateur fondé sur données.
- Rôle: ensemble responsabilités/tâches (indépendant préférences).
- Prototype: représentation concrète (low‑fi/hi‑fi) pour explorer/valider.
- CTT: modèle hiérarchique de tâches + opérateurs temporels.
- GOMS/KLM: modèle analytique de performance (opérateurs chronométrés).
- Walkthrough: simulation guidée de première utilisation pour détecter obstacles.
