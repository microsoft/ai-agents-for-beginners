# Notebook Structure

Jupyter notebooks are JSON documents with this high-level shape:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (a list of markdown and code cells)

When editing `.ipynb` files programmatically:

- Preserve `nbformat` and `nbformat_minor` from the template.
- Keep `cells` as an ordered list; do not reorder unless intentional.
- For code cells, set `execution_count` to `null` when unknown.
- For code cells, set `outputs` to an empty list when scaffolding.
- For markdown cells, keep `cell_type="markdown"` and `metadata={}`.

Prefer scaffolding from the bundled templates or `new_notebook.py` (for example, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) instead of hand-authoring raw notebook JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
This document was translated using the AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). While we strive for accuracy, automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->