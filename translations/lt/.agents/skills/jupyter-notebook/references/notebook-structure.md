# Užrašo struktūra

Jupyter užrašai yra JSON dokumentai su tokia bendrąja struktūra:

- `nbformat` ir `nbformat_minor`
- `metadata`
- `cells` (sąrašas markdown ir kodo ląstelių)

Redaguojant `.ipynb` failus programuotiniu būdu:

- Išsaugokite `nbformat` ir `nbformat_minor`, kaip nurodyta šablone.
- Laikykite `cells` kaip išdėstytą sąrašą; nekeiskite eiliškumo, nebent tai darote tyčia.
- Kodo ląstelėms nustatykite `execution_count` į `null`, kai nežinoma.
- Kodo ląstelėms nustatykite `outputs` į tuščią sąrašą, kai kuriate karkasą.
- Markdown ląstelėms išlaikykite `cell_type="markdown"` ir `metadata={}`.

Teikite pirmenybę karkaso kūrimui naudojant pridėtus šablonus arba `new_notebook.py` (pavyzdžiui, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) vietoje rankinio neapdoroto notebook JSON rašymo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Atsakomybės apribojimas:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą Co‑op Translator (https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turi būti laikomas pagrindiniu (autoritative) šaltiniu. Kritinei informacijai rekomenduojamas profesionalus, žmogaus atliktas vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->