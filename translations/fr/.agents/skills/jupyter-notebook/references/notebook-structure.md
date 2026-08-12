# Structure du notebook

Les notebooks Jupyter sont des documents JSON avec cette structure générale:

- `nbformat` et `nbformat_minor`
- `metadata`
- `cells` (une liste de cellules Markdown et de cellules de code)

When editing `.ipynb` files programmatically:

- Conserver `nbformat` et `nbformat_minor` depuis le modèle.
- Conserver `cells` en tant que liste ordonnée; ne pas réordonner sauf intentionnellement.
- Pour les cellules de code, mettre `execution_count` à `null` lorsqu'il est inconnu.
- Pour les cellules de code, mettre `outputs` sur une liste vide lors de la création du gabarit.
- Pour les cellules markdown, conserver `cell_type="markdown"` et `metadata={}`.

Privilégiez la génération depuis les modèles fournis ou `new_notebook.py` (for example, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) instead of hand-authoring raw notebook JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Clause de non-responsabilité :
Ce document a été traduit à l'aide du service de traduction par IA Co‑op Translator (https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un traducteur humain. Nous déclinons toute responsabilité pour tout malentendu ou mauvaise interprétation résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->