# Notatbokstruktur

Jupyter-notatbøker er JSON-dokumenter med denne overordnede strukturen:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (en liste over markdown- og kodeceller)

Når du redigerer `.ipynb`-filer programmatisk:

- Bevar `nbformat` og `nbformat_minor` fra malen.
- Behold `cells` som en ordnet liste; ikke endre rekkefølgen med mindre det er tilsiktet.
- For kodeceller, sett `execution_count` til `null` når den er ukjent.
- For kodeceller, sett `outputs` til en tom liste når du lager skjelettet.
- For markdown-celler, behold `cell_type="markdown"` og `metadata={}`.

Foretrekk å generere skjelettet fra de medfølgende malene eller `new_notebook.py` (for eksempel, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) i stedet for å håndskrive rå notebook JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Originaldokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->