# Struktura bilježnice

Jupyter bilježnice su JSON dokumenti s ovakvom visokom razinom strukture:

- `nbformat` i `nbformat_minor`
- `metadata`
- `cells` (popis markdown i ćelija s kodom)

Prilikom programskog uređivanja `.ipynb` datoteka:

- Sačuvajte `nbformat` i `nbformat_minor` iz predloška.
- Zadržite `cells` kao poredani popis; ne mijenjajte redoslijed osim ako nije namjerno.
- Za ćelije s kodom, postavite `execution_count` na `null` kada nije poznato.
- Za ćelije s kodom, prilikom izrade kostura postavite `outputs` na prazan popis.
- Za markdown ćelije, zadržite `cell_type="markdown"` i `metadata={}`.

Preferirajte korištenje kostura iz priloženih predložaka ili `new_notebook.py` (na primjer, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) umjesto ručnog pisanja sirovog JSON-a bilježnice.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Odricanje odgovornosti:
Ovaj je dokument preveden pomoću AI usluge prevođenja Co-op Translator (https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz upotrebe ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->