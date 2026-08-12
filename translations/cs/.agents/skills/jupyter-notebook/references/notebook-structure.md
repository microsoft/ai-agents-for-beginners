# Struktura notebooku

Jupyter notebooky jsou JSON dokumenty s touto obecnou strukturou:

- `nbformat` a `nbformat_minor`
- `metadata`
- `cells` (seznam markdown a kódových buněk)

Při programové úpravě souborů `.ipynb`:

- Zachovejte `nbformat` a `nbformat_minor` ze šablony.
- Udržujte `cells` jako seřazený seznam; nepřeskupujte jej, pokud to není záměrné.
- U kódových buněk nastavte `execution_count` na `null`, pokud není znám.
- U kódových buněk nastavte `outputs` na prázdný seznam při vytváření kostry.
- U markdownových buněk ponechte `cell_type="markdown"` a `metadata={}`.

Upřednostněte vytváření kostry z dodávaných šablon nebo `new_notebook.py` (například `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) namísto ručního vytváření surového JSONu notebooku.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vyloučení odpovědnosti:
Tento dokument byl přeložen pomocí služby pro automatický překlad Co-op Translator (https://github.com/Azure/co-op-translator). Ačkoliv usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro zásadní informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za žádná nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->