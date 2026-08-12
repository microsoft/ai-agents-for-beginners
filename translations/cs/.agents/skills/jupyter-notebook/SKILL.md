---
name: jupyter-notebook
description: Použijte, když uživatel požádá o vytvoření, inicializaci nebo úpravu
  Jupyter notebooků (`.ipynb`) pro experimenty, průzkumy nebo návody; upřednostněte
  zabudované šablony a spusťte pomocný skript `new_notebook.py`, abyste vygenerovali
  čistý výchozí notebook.
---
# Dovednost Jupyter Notebook

Vytvářejte čisté, reprodukovatelné Jupyter notebooky pro dva hlavní režimy:

- Experimenty a průzkumné analýzy
- Tutoriály a výukové průvodce

Upřednostněte dodané šablony a pomocný skript pro konzistentní strukturu a méně chyb v JSONu.

## Kdy použít
- Vytvořte nový `.ipynb` notebook od začátku.
- Převeďte hrubé poznámky nebo skripty do strukturovaného notebooku.
- Přepracujte existující notebook tak, aby byl více reprodukovatelný a přehledný.
- Vytvářejte experimenty nebo tutoriály, které budou čteny nebo znovu spouštěny jinými lidmi.

## Rozhodovací strom
- Pokud je požadavek průzkumný, analytický nebo založený na hypotéze, zvolte `experiment`.
- Pokud je požadavek instruktážní, krok za krokem nebo zaměřený na konkrétní publikum, zvolte `tutorial`.
- Při úpravě existujícího notebooku jej považujte za refaktorizaci: zachovejte záměr a vylepšete strukturu.

## Cesta dovednosti (nastavit jednou)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Pracovní postup
1. Lock the intent.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. Scaffold from the template.
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

3. Fill the notebook with small, runnable steps.
Keep each code cell focused on one step.
Add short markdown cells that explain the purpose and expected result.
Avoid large, noisy outputs when a short summary works.

4. Apply the right pattern.
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. Edit safely when working with existing notebooks.
Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story.
Prefer targeted edits over full rewrites.
If you must edit raw JSON, review `references/notebook-structure.md` first.

6. Validate the result.
Run the notebook top-to-bottom when the environment allows.
If execution is not possible, say so explicitly and call out how to validate locally.
Use the final pass checklist in `references/quality-checklist.md`.

## Šablony a pomocný skript
- Šablony se nacházejí v `assets/experiment-template.ipynb` a `assets/tutorial-template.ipynb`.
- Pomocný skript načte šablonu, aktualizuje titulní buňku a zapíše notebook.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Konvence pro dočasné a výstupní soubory
- Používejte `tmp/jupyter-notebook/` pro mezisoubory; smažte je po dokončení.
- Zapisujte finální artefakty do `output/jupyter-notebook/` při práci v tomto repozitáři.
- Používejte stabilní, popisné názvy souborů (například `ablation-temperature.ipynb`).

## Závislosti (instalovat pouze pokud je potřeba)
Preferujte `uv` pro správu závislostí.

Volitelné Python balíčky pro lokální spuštění notebooku:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## Prostředí
Žádné povinné proměnné prostředí.

## Referenční mapa
- `references/experiment-patterns.md`: struktura experimentu a heuristiky.
- `references/tutorial-patterns.md`: struktura tutoriálu a průběh výuky.
- `references/notebook-structure.md`: tvar JSONu notebooku a pravidla bezpečných úprav.
- `references/quality-checklist.md`: finální kontrolní seznam pro ověření.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Prohlášení o vyloučení odpovědnosti:
Tento dokument byl přeložen pomocí AI překladatelské služby Co-op Translator (https://github.com/Azure/co-op-translator). I když usilujeme o co nejvyšší přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za rozhodující zdroj. Pro zásadní informace doporučujeme využít profesionální lidský překlad. Nejsme odpovědní za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->