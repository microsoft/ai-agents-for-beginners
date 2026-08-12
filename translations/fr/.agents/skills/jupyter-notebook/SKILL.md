---
name: jupyter-notebook
description: À utiliser lorsque l'utilisateur demande de créer, structurer ou modifier
  des notebooks Jupyter (`.ipynb`) pour des expériences, explorations ou tutoriels
  ; privilégiez les modèles fournis et exécutez le script d'aide `new_notebook.py`
  pour générer un notebook de départ propre.
---
# Compétence Jupyter Notebook

Créez des notebooks Jupyter propres et reproductibles pour deux modes principaux :

- Expériences et analyse exploratoire
- Tutoriels et parcours guidés à visée pédagogique

Privilégiez les modèles fournis et le script d'assistance pour une structure cohérente et moins d'erreurs JSON.

## Quand l'utiliser
- Créez un nouveau notebook `.ipynb` à partir de zéro.
- Convertissez des notes ou des scripts bruts en un notebook structuré.
- Refactorez un notebook existant pour le rendre plus reproductible et plus facile à parcourir.
- Réalisez des expériences ou des tutoriels destinés à être lus ou réexécutés par d'autres personnes.

## Arbre décisionnel
- Si la demande est exploratoire, analytique ou guidée par des hypothèses, choisissez `experiment`.
- Si la demande est didactique, étape par étape ou ciblée sur un public spécifique, choisissez `tutorial`.
- Si vous modifiez un notebook existant, considérez cela comme une refonte : préservez l'intention et améliorez la structure.

## Chemin de compétence (à définir une fois)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Les skills au niveau utilisateur s'installent sous `$CODEX_HOME/skills` (par défaut : `~/.codex/skills`).

## Flux de travail
1. Verrouillez l'intention.
Identifiez le type de notebook : `experiment` ou `tutorial`.
Consignez l'objectif, le public et à quoi ressemble "terminé".

2. Générez la structure à partir du modèle.
Utilisez le script d'aide pour éviter d'éditer manuellement le JSON brut du notebook.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. Remplissez le notebook avec de petites étapes exécutables.
Veillez à ce que chaque cellule de code soit axée sur une seule étape.
Ajoutez de courtes cellules Markdown qui expliquent l'objectif et le résultat attendu.
Évitez les sorties volumineuses et bruyantes lorsqu'un bref résumé suffit.

4. Appliquez le bon modèle.
Pour les expériences, suivez `references/experiment-patterns.md`.
Pour les tutoriels, suivez `references/tutorial-patterns.md`.

5. Modifiez en toute sécurité lorsque vous travaillez sur des notebooks existants.
Préservez la structure du notebook ; évitez de réordonner les cellules sauf si cela améliore la progression de haut en bas.
Privilégiez les modifications ciblées plutôt que les réécritures complètes.
Si vous devez modifier le JSON brut, consultez d'abord `references/notebook-structure.md`.

6. Validez le résultat.
Exécutez le notebook de haut en bas lorsque l'environnement le permet.
Si l'exécution n'est pas possible, indiquez-le explicitement et précisez comment valider localement.
Utilisez la liste de contrôle finale dans `references/quality-checklist.md`.

## Modèles et script d'assistance
- Les modèles se trouvent dans `assets/experiment-template.ipynb` et `assets/tutorial-template.ipynb`.
- Le script d'assistance charge un modèle, met à jour la cellule de titre et écrit un notebook.

Chemin du script:
- `$JUPYTER_NOTEBOOK_CLI` (installé par défaut : `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Conventions pour les fichiers temporaires et de sortie
- Utilisez `tmp/jupyter-notebook/` pour les fichiers intermédiaires ; supprimez-les une fois terminé.
- Placez les artefacts finaux sous `output/jupyter-notebook/` lorsque vous travaillez dans ce dépôt.
- Utilisez des noms de fichiers stables et descriptifs (par exemple, `ablation-temperature.ipynb`).

## Dépendances (installer uniquement si nécessaire)
Privilégiez `uv` pour la gestion des dépendances.

Packages Python optionnels pour l'exécution locale du notebook:

```bash
uv pip install jupyterlab ipykernel
```

Le script d'échafaudage inclus n'utilise que la bibliothèque standard Python et ne nécessite pas de dépendances supplémentaires.

## Environnement
Aucune variable d'environnement requise.

## Carte de référence
- `references/experiment-patterns.md`: structure et heuristiques pour les expériences.
- `references/tutorial-patterns.md`: structure des tutoriels et déroulement pédagogique.
- `references/notebook-structure.md`: forme du JSON du notebook et règles d'édition sécurisées.
- `references/quality-checklist.md`: liste de contrôle finale de validation.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avis de non-responsabilité** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->