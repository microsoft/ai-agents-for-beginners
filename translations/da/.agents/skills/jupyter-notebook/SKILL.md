---
name: jupyter-notebook
description: Bruges når brugeren beder om at oprette, opsætte eller redigere Jupyter-notebooks
  (`.ipynb`) til eksperimenter, udforskninger eller vejledninger; foretræk de medfølgende
  skabeloner og kør hjælpeskriptet `new_notebook.py` for at generere en ren start-notebook.
---
# Jupyter Notebook-færdighed

Opret rene, reproducerbare Jupyter-notebooks til to primære tilstande:

- Eksperimenter og eksplorativ analyse
- Vejledninger og undervisningsorienterede gennemgange

Brug helst de medfølgende skabeloner og hjælpeprogrammet for konsistent struktur og færre JSON-fejl.

## Hvornår man skal bruge det
- Opret en ny `.ipynb`-notebook fra bunden.
- Konverter grove noter eller scripts til en struktureret notebook.
- Refaktorér en eksisterende notebook for at gøre den mere reproducerbar og let at overskue.
- Byg eksperimenter eller vejledninger, der vil blive læst eller genkørt af andre.

## Beslutningstræ
- Hvis anmodningen er eksplorativ, analytisk eller hypotesedrevet, vælg `experiment`.
- Hvis anmodningen er instruktionsbaseret, trin-for-trin eller målgruppe-specifik, vælg `tutorial`.
- Hvis du redigerer en eksisterende notebook, behandl det som en refaktorering: bevar hensigten og forbedr strukturen.

## Færdighedsvej (opsæt én gang)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Arbejdsgang
1. Fastlæg intentionen.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. Scaffold fra skabelonen.
Use the helper script to avoid hand-authoring raw notebook JSON.

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

3. Fyld notebooken med små, kørbare trin.
Hold hver kodecelle fokuseret på ét trin.
Tilføj korte markdown-celler, der forklarer formålet og forventet resultat.
Undgå store, støjende outputs når et kort sammendrag er tilstrækkeligt.

4. Anvend det rigtige mønster.
For eksperimenter, følg `references/experiment-patterns.md`.
For vejledninger, følg `references/tutorial-patterns.md`.

5. Rediger forsigtigt når du arbejder med eksisterende notebooks.
Bevar notebook-strukturen; undgå at omarrangere celler medmindre det forbedrer fortællingen fra top til bund.
Foretræk målrettede rettelser frem for fulde omskrivninger.
Hvis du er nødt til at redigere rå JSON, gennemgå `references/notebook-structure.md` først.

6. Valider resultatet.
Kør notebooken fra top til bund når miljøet tillader det.
Hvis kørsel ikke er muligt, sig det eksplicit og beskriv hvordan man validerer lokalt.
Brug den endelige tjekliste i `references/quality-checklist.md`.

## Skabeloner og hjælpe-script
- Skabeloner ligger i `assets/experiment-template.ipynb` og `assets/tutorial-template.ipynb`.
- Hjælpe-scriptet indlæser en skabelon, opdaterer titelcellen og skriver en notebook.

Scriptsti:
- `$JUPYTER_NOTEBOOK_CLI` (installeret som standard: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Midlertidige filer og outputkonventioner
- Brug `tmp/jupyter-notebook/` til midlertidige filer; slet når du er færdig.
- Skriv endelige artefakter under `output/jupyter-notebook/` når du arbejder i dette repo.
- Brug stabile, beskrivende filnavne (for eksempel, `ablation-temperature.ipynb`).

## Afhængigheder (installer kun når nødvendigt)
Foretræk `uv` til afhængighedsstyring.

Valgfrie Python-pakker til lokal notebook-udførelse:

```bash
uv pip install jupyterlab ipykernel
```

Det medfølgende scaffold-script bruger kun Python-standardbiblioteket og kræver ikke ekstra afhængigheder.

## Miljø
Ingen krævede miljøvariabler.

## Referencemappe
- `references/experiment-patterns.md`: struktur for eksperimenter og heuristikker.
- `references/tutorial-patterns.md`: vejledningsstruktur og undervisningsforløb.
- `references/notebook-structure.md`: notebookens JSON-form og regler for sikker redigering.
- `references/quality-checklist.md`: endelig tjekliste for validering.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget bør anses for den autoritative kilde. For kritisk information anbefales en professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->