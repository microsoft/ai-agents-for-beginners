# Notebook-struktur

Jupyter-notebooks er JSON-dokumenter med denne overordnede struktur:

- `nbformat` og `nbformat_minor`
- `metadata`
- `cells` (en liste af markdown- og kodeceller)

Når du redigerer `.ipynb` filer programmatisk:

- Bevar `nbformat` og `nbformat_minor` fra skabelonen.
- Behold `cells` som en ordnet liste; omrokér ikke medmindre det er tilsigtet.
- For kodeceller, sæt `execution_count` til `null` når det er ukendt.
- For kodeceller, sæt `outputs` til en tom liste ved opbygning.
- For markdown-celler, behold `cell_type="markdown"` og `metadata={}`.

Foretræk at basere opbygningen på de medfølgende skabeloner eller `new_notebook.py` (for eksempel, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) i stedet for at skrive rå notebook-JSON manuelt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales en professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->