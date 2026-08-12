# Struttura del notebook

I notebook Jupyter sono documenti JSON con questa struttura ad alto livello:

- `nbformat` e `nbformat_minor`
- `metadata`
- `cells` (una lista di celle markdown e di codice)

Quando si modificano i file `.ipynb` programmaticamente:

- Conservare `nbformat` e `nbformat_minor` dal modello.
- Tenere `cells` come elenco ordinato; non riordinare a meno che non sia intenzionale.
- Per le celle di codice, impostare `execution_count` su `null` quando non è noto.
- Per le celle di codice, impostare `outputs` su una lista vuota quando si crea lo scheletro.
- Per le celle markdown, mantenere `cell_type="markdown"` e `metadata={}`.

È preferibile utilizzare gli scheletri forniti dai modelli inclusi o `new_notebook.py` (ad esempio, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) invece di scrivere manualmente il JSON grezzo del notebook.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica basato su IA [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua d'origine deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->