# Notebookstructuur

Jupyter-notebooks zijn JSON-documenten met deze hoog-niveau structuur:

- `nbformat` en `nbformat_minor`
- `metadata`
- `cells` (een lijst met markdown- en codecellen)

Wanneer je `.ipynb`-bestanden programmatisch bewerkt:

- Behoud `nbformat` en `nbformat_minor` van het sjabloon.
- Houd `cells` als een geordende lijst; herschik deze niet tenzij dat opzettelijk is.
- Voor codecellen, zet `execution_count` op `null` wanneer onbekend.
- Voor codecellen, zet `outputs` op een lege lijst bij het opzetten.
- Voor markdowncellen, behoud `cell_type="markdown"` en `metadata={}`.

Geef de voorkeur aan het gebruiken van de meegeleverde sjablonen of `new_notebook.py` (bijvoorbeeld `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) in plaats van het handmatig schrijven van ruwe notebook-JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we naar nauwkeurigheid streven, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->