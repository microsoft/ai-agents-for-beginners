# Jegyzetfüzet szerkezete

A Jupyter jegyzetfüzetek JSON-dokumentumok, amelyek a következő magas szintű felépítéssel rendelkeznek:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (a markdown és kód cellák listája)

When editing `.ipynb` files programmatically:

- Tartsd meg a sablonból származó `nbformat` és `nbformat_minor` értékeket.
- Tartsd a `cells`-t rendezett listaként; ne rendezd át, kivéve ha szándékos.
- Kód cellák esetén állítsd az `execution_count` értékét `null`-ra, ha ismeretlen.
- Kód cellák esetén állítsd az `outputs` értékét üres listára, amikor kezdeti vázat készítesz.
- Markdown cellák esetén hagyd meg a `cell_type="markdown"` és `metadata={}` értékeket.

Preferáljuk a csomagolt sablonokból vagy a `new_notebook.py` (például `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) használatával történő vázkészítést a nyers notebook JSON kézi létrehozása helyett.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősségkizárás**:
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelven tekintendő hiteles forrásnak. Kritikus jelentőségű információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő bármilyen félreértésért vagy téves értelmezésért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->