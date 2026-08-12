---
name: jupyter-notebook
description: Använd när användaren ber om att skapa, strukturera eller redigera Jupyter-notebooks
  (`.ipynb`) för experiment, utforskningar eller handledningar; använd helst de medföljande
  mallarna och kör hjälpskriptet `new_notebook.py` för att generera en ren startanteckningsbok.
---
# Jupyter Notebook-färdighet

Skapa rena, reproducerbara Jupyter-notebookar för två huvudsakliga lägen:

- Experiment och utforskande analys
- Handledningar och undervisningsinriktade genomgångar

Använd helst de medföljande mallarna och hjälpskriptet för en konsekvent struktur och färre JSON-fel.

## När man ska använda
- Skapa en ny `.ipynb`-notebook från början.
- Konvertera grova anteckningar eller skript till en strukturerad notebook.
- Refaktorera en befintlig notebook för att göra den mer reproducerbar och lättöverskådlig.
- Skapa experiment eller handledningar som kommer att läsas eller köras om av andra.

## Beslutsträd
- Om förfrågan är explorativ, analytisk eller hypotesdriven, välj `experiment`.
- Om förfrågan är instruktiv, steg-för-steg eller målgruppsspecifik, välj `tutorial`.
- Om du redigerar en befintlig notebook, behandla det som en refaktorering: bevara avsikten och förbättra strukturen.

## Färdighetsväg (anges en gång)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Färdigheter som är användarspecifika installeras under `$CODEX_HOME/skills` (standard: `~/.codex/skills`).

## Arbetsflöde
1. Fastställ avsikten.
Identifiera notebook-typen: `experiment` eller `tutorial`.
Formulera målet, målgruppen och hur 'klart' ser ut.

2. Skapa stommen från mallen.
Använd hjälpskriptet för att undvika att manuellt skapa rå notebook-JSON.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. Fyll notebooken med små, körbara steg.
Håll varje kodcell inriktad på ett steg.
Lägg till korta markdown-celler som förklarar syftet och väntat resultat.
Undvik stora, stökiga utskrifter när en kort sammanfattning fungerar.

4. Använd rätt mönster.
För experiment, följ `references/experiment-patterns.md`.
För handledningar, följ `references/tutorial-patterns.md`.

5. Redigera säkert när du arbetar med befintliga notebooks.
Bevara notebook-strukturen; undvik att omordna celler om det inte förbättrar berättelsen från topp till botten.
Föredra riktade ändringar framför fullständiga omskrivningar.
Om du måste redigera rå JSON, granska först `references/notebook-structure.md`.

6. Validera resultatet.
Kör notebooken från början till slut när miljön tillåter.
Om körning inte är möjlig, ange det uttryckligen och beskriv hur man validerar lokalt.
Använd slutkontrollistan i `references/quality-checklist.md`.

## Mallar och hjälpskript
- Mallarna finns i `assets/experiment-template.ipynb` och `assets/tutorial-template.ipynb`.
- Hjälpskriptet laddar en mall, uppdaterar titelcellen och skriver en notebook.

Skriptväg:
- `$JUPYTER_NOTEBOOK_CLI` (installerat som standard: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temporära och utdatakonventioner
- Använd `tmp/jupyter-notebook/` för mellanfiler; radera när du är klar.
- Skriv slutliga artefakter under `output/jupyter-notebook/` när du arbetar i detta repo.
- Använd stabila, beskrivande filnamn (till exempel `ablation-temperature.ipynb`).

## Beroenden (installera endast vid behov)
Föredra `uv` för beroendehantering.

Valfria Python-paket för lokal notebookkörning:

```bash
uv pip install jupyterlab ipykernel
```

Det medföljande scaffold-skriptet använder endast Python-standardbiblioteket och kräver inga ytterligare beroenden.

## Miljö
Inga obligatoriska miljövariabler.

## Referenskarta
- `references/experiment-patterns.md`: struktur och heuristiker för experiment.
- `references/tutorial-patterns.md`: struktur för handledningar och undervisningsflöde.
- `references/notebook-structure.md`: notebook-JSON:s form och regler för säker redigering.
- `references/quality-checklist.md`: slutgiltig valideringschecklista.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfriskrivning:
Detta dokument har översatts med hjälp av AI-översättningstjänsten Co-op Translator (https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet i dess ursprungliga språk ska betraktas som den auktoritativa källan. För viktig information rekommenderas professionell, mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->