# Notebook Structure

Jupyter notebooks na JSON documents wey get dis high-level shape:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (one list of markdown and code cells)

When you dey edit `.ipynb` files programmatically:

- Make you preserve `nbformat` and `nbformat_minor` from the template.
- Make you keep `cells` as ordered list; no reorder unless na intentional.
- For code cells, set `execution_count` to `null` when e no clear.
- For code cells, set `outputs` to empty list when you dey scaffold.
- For markdown cells, keep `cell_type="markdown"` and `metadata={}`.

Better make you scaffold from the bundled templates or `new_notebook.py` (for example, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) instead of to dey hand-author raw notebook JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document na translat use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translations fit get errors or mistakes. Di original document wey dey di original language be di correct one. For important info, make person wey sabi human translation do am. We no go responsible for any wahala or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->