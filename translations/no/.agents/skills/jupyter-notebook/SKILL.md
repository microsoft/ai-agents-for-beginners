---
name: jupyter-notebook
description: Bruk når brukeren ber om å opprette, sette opp eller redigere Jupyter-notatbøker
  (`.ipynb`) for eksperimenter, utforskninger eller veiledninger; foretrekk de medfølgende
  malene og kjør hjelpeskriptet `new_notebook.py` for å generere en ren startnotatbok.
---
# Jupyter Notebook-ferdighet

Lag rene, reproduserbare Jupyter-notatbøker for to hovedmoduser:

- Eksperimenter og utforskende analyse
- Veiledninger og undervisningsorienterte gjennomganger

Foretrekk de inkluderte malene og hjelpeskriptet for konsistent struktur og færre JSON-feil.

## Når du skal bruke
- Opprett en ny `.ipynb`-notatbok fra bunnen av.
- Konverter uferdige notater eller skript til en strukturert notatbok.
- Refaktorer en eksisterende notatbok for å bli mer reproduserbar og lett å skumme.
- Bygg eksperimenter eller veiledninger som skal leses eller kjøres av andre.

## Beslutningstre
- Hvis forespørselen er utforskende, analytisk eller hypotesedrevet, velg `experiment`.
- Hvis forespørselen er instruksjonell, steg-for-steg eller målgruppe-spesifikk, velg `tutorial`.
- Hvis du redigerer en eksisterende notatbok, behandl det som en refaktorering: bevar intensjonen og forbedre strukturen.

## Kompetansesti (settes én gang)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Brukerspesifikke ferdigheter installeres under `$CODEX_HOME/skills` (standard: `~/.codex/skills`).

## Arbeidsflyt
1. Lås intensjonen.
Identifiser notatboktypen: `experiment` eller `tutorial`.
Fang målet, målgruppen, og hva "done" ser ut som.

2. Bygg skjelett fra malen.
Bruk hjelpeskriptet for å unngå manuell redigering av rå notebook JSON.

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

3. Fyll notatboken med små, kjørbare steg.
Hold hver kodecelle fokusert på ett steg.
Legg til korte markdown-celler som forklarer formålet og forventet resultat.
Unngå store, støyende utdata når en kort oppsummering fungerer.

4. Bruk riktig mønster.
For eksperimenter, følg `references/experiment-patterns.md`.
For veiledninger, følg `references/tutorial-patterns.md`.

5. Rediger trygt når du arbeider med eksisterende notatbøker.
Bevar notatbokens struktur; unngå å omorganisere celler med mindre det forbedrer historien ovenfra og ned.
Foretrekk målrettede endringer framfor fullstendige omskrivinger.
Hvis du må redigere rå JSON, gå gjennom `references/notebook-structure.md` først.

6. Valider resultatet.
Kjør notatboken ovenfra og ned når miljøet tillater det.
Hvis kjøring ikke er mulig, si det eksplisitt og forklar hvordan man kan validere lokalt.
Bruk sjekklisten i siste gjennomgang i `references/quality-checklist.md`.

## Malene og hjelpeskriptet
- Malene ligger i `assets/experiment-template.ipynb` og `assets/tutorial-template.ipynb`.
- Hjelpeskriptet laster en mal, oppdaterer tittelen i cellen, og skriver en notatbok.

Scriptbane:
- `$JUPYTER_NOTEBOOK_CLI` (installert som standard: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Midlertidige filer og utdata-konvensjoner
- Bruk `tmp/jupyter-notebook/` for mellomliggende filer; slett når du er ferdig.
- Skriv endelige artefakter under `output/jupyter-notebook/` når du arbeider i dette repoet.
- Bruk stabile, beskrivende filnavn (for eksempel, `ablation-temperature.ipynb`).

## Avhengigheter (installer kun når nødvendig)
Foretrekk `uv` for avhengighetsstyring.

Valgfrie Python-pakker for lokal notatbokkjøring:

```bash
uv pip install jupyterlab ipykernel
```

Det medfølgende skjelettskriptet bruker bare Pythons standardbibliotek og krever ingen ekstra avhengigheter.

## Miljø
Ingen påkrevde miljøvariabler.

## Referansekart
- `references/experiment-patterns.md`: struktur og heuristikker for eksperimenter.
- `references/tutorial-patterns.md`: struktur for veiledninger og undervisningsflyt.
- `references/notebook-structure.md`: notatbok-JSON-form og regler for sikker redigering.
- `references/quality-checklist.md`: sluttvaliderings-sjekkliste.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell, menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->