---
name: jupyter-notebook
description: Use dis one wen di user dey ask make you create, scaffold, or edit Jupyter
  notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer di bundled
  templates and run di helper script `new_notebook.py` make e generate a clean starting
  notebook.
---
# Jupyter Notebook Skill

Make clean, reproducible Jupyter notebooks for two main modes:

- Experiments and exploratory analysis
- Tutorials and teaching-oriented walkthroughs

Dey prefer di bundled templates and di helper script for consistent structure and to reduce JSON mistakes.

## When to use
- Make new `.ipynb` notebook from scratch.
- Turn rough notes or scripts into one structured notebook.
- Refactor an existing notebook make am more reproducible and easy to skim.
- Build experiments or tutorials wey other people go read or run again.

## Decision tree
- If di request na exploratory, analytical, or hypothesis-driven, choose `experiment`.
- If di request na instructional, step-by-step, or audience-specific, choose `tutorial`.
- If you dey edit existing notebook, treat am as refactor: preserve intent and improve structure.

## Skill path (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills dey install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Workflow
1. Lock the intent.
Identify di notebook kind: `experiment` or `tutorial`.
Capture di objective, audience, and wetin "done" suppose look like.

2. Scaffold from the template.
Use di helper script so you no go hand-author raw notebook JSON.

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
Make each code cell focus on one step.
Add short markdown cells wey explain di purpose and wetin dem suppose expect.
Avoid big, noisy outputs if small summary fit do.

4. Apply the right pattern.
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. Edit safely when working with existing notebooks.
Preserve di notebook structure; no dey reorder cells unless e go improve di top-to-bottom story.
Prefer targeted edits rather than full rewrites.
If you must edit raw JSON, check `references/notebook-structure.md` first.

6. Validate the result.
Run the notebook top-to-bottom when environment allow.
If execution no possible, talk am clear and explain how to validate locally.
Use di final pass checklist in `references/quality-checklist.md`.

## Templates and helper script
- Templates dey for `assets/experiment-template.ipynb` and `assets/tutorial-template.ipynb`.
- Di helper script go load a template, update di title cell, and write di notebook.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp and output conventions
- Use `tmp/jupyter-notebook/` for intermediate files; delete when done.
- Write final artifacts under `output/jupyter-notebook/` when you dey work for this repo.
- Use stable, descriptive filenames (for example, `ablation-temperature.ipynb`).

## Dependencies (install only when needed)
Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

Di bundled scaffold script dey use only di Python standard library and no need extra dependencies.

## Environment
No required environment variables.

## Reference map
- `references/experiment-patterns.md`: experiment structure and heuristics.
- `references/tutorial-patterns.md`: tutorial structure and teaching flow.
- `references/notebook-structure.md`: notebook JSON shape and safe editing rules.
- `references/quality-checklist.md`: final validation checklist.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis dokument don translate wit AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automatic translations fit get errors or mistakes. The original dokument for im own language na the correct/official source. For important information, na professional human translator we dey recommend. We no dey responsible for any wrong understanding or misinterpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->