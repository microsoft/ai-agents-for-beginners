# Štruktúra notebooku

Jupyter notebooks sú JSON dokumenty s týmto všeobecným tvarom:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (zoznam markdownových a kódových buniek)

Pri úprave súborov `.ipynb` programaticky:

- Zachovajte `nbformat` a `nbformat_minor` z šablóny.
- Udržujte `cells` ako usporiadaný zoznam; nepreusporiadajte ich, pokiaľ to nie je zámerné.
- Pre kódové bunky nastavte `execution_count` na `null`, ak nie je známe.
- Pre kódové bunky nastavte `outputs` na prázdny zoznam pri vytváraní kostry.
- Pre markdown bunky zachovajte `cell_type="markdown"` a `metadata={}`.

Uprednostňujte vytváranie kostry z dodaných šablón alebo `new_notebook.py` (napríklad `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) namiesto ručného písania surového notebookového JSONu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vyhlásenie o zodpovednosti:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa usilujeme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho originálnom jazyku by mal byť považovaný za rozhodujúci zdroj. Pre kritické informácie odporúčame profesionálny ľudský preklad. Za žiadne nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu nenesieme zodpovednosť.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->