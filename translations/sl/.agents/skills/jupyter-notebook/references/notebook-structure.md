# Struktura zvezka

Jupyter zvezki so JSON-dokumenti s to splošno strukturo:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (seznam markdown in celic s kodo)

Pri programskem urejanju datotek `.ipynb`:

- Ohranite `nbformat` in `nbformat_minor` iz predloge.
- Ohranite `cells` kot urejen seznam; ne spreminjajte vrstnega reda, razen če je to namerno.
- Za celice s kodo nastavite `execution_count` na `null`, kadar ni znano.
- Za celice s kodo nastavite `outputs` na prazen seznam pri ustvarjanju osnutka.
- Za markdown celice ohranite `cell_type="markdown"` in `metadata={}`.

Raje uporabljajte ogrodja iz priloženih predlog ali `new_notebook.py` (na primer, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) namesto ročnega pisanja surovega JSON-a zvezka.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Izjava o omejitvi odgovornosti:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->