# Anteckningsboksstruktur

Jupyter-notebooks är JSON-dokument med den här övergripande strukturen:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (en lista med markdown- och kodceller)

När du redigerar `.ipynb`-filer programmässigt:

- Behåll `nbformat` och `nbformat_minor` från mallen.
- Behåll `cells` som en ordnad lista; ändra inte ordningen om det inte är avsiktligt.
- För kodceller, sätt `execution_count` till `null` när den är okänd.
- För kodceller, sätt `outputs` till en tom lista när du förbereder grundstrukturen.
- För markdownceller, behåll `cell_type="markdown"` och `metadata={}`.

Föredra att skapa stommen från de medföljande mallarna eller `new_notebook.py` (till exempel `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) istället för att författa rå notebook-JSON för hand.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfriskrivning:
Detta dokument har översatts med hjälp av AI-översättningstjänsten Co-op Translator (https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet i dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->