---
name: jupyter-notebook
description: వినియోగదారు ప్రయోగాలు, అన్వేషణలు లేదా పాఠ్యాల కోసం Jupyter నోట్‌బుక్స్
  (`.ipynb`) సృష్టించమని, ఆధార నిర్మాణం (scaffold) చేయమని లేదా సవరిచమని అడిగినప్పుడు
  ఉపయోగించండి; బండిల్ చేయబడ్డ టెంప్లేట్లను ప్రాధాన్యంగా ఉపయోగించి సహాయక స్క్రిప్ట్
  `new_notebook.py` ని నడపండి ఒక శుభ్రమైన ప్రారంభ నోట్‌బుక్ రూపొందించడానికి.
---
# Jupyter Notebook నైపుణ్యం

రెండు ప్రధాన మోడ్‌ల కోసం శుభ్రంగా, పునఃరుత్పాదకంగా ఉండే Jupyter నోట్‌బుక్స్ సృష్టించండి:

- ప్రయోగాలు మరియు అన్వेषణాత్మక విశ్లేషణ
- ట్యుటోరియల్స్ మరియు చెప్పుకునేందుకు ఉద్దేశించిన వాక్థ్రూస్

సంయుక్తంగా ఉన్న టెంప్లేట్లు మరియు సహాయ స్క్రిప్ట్‌ను ప్రాధాన్యతగా ఉపయోగించండి, తద్వారా ఒకరూపమైన నిర్మాణం మరియు తక్కువ JSON తప్పులను పొందవచ్చు.

## When to use
- కొత్తగా ఒక `.ipynb` నోట్‌బుక్‌ను క్రొత్తగా సృష్టించండి.
- ముడి గమనికలు లేదా స్క్రిప్టులను ఒక నిర్మిత నోట్‌బుక్‌గా మార్పిడీ చేయండి.
- ఇప్పటికే ఉన్న నోట్‌బుక్‌ను మరింత పునఃరుత్పాదకంగా మరియు సులభంగా సమీక్షించదగినదిగా పునఃరూపకల్పన చేయండి.
- ఇతరులు చదవబోయే లేదా మళ్ళీ నడిపే ప్రయోగాలు లేదా ట్యుటోరియల్స్ నిర్మించండి.

## Decision tree
- అభ్యర్థన అన్వేషణాత్మక, విశ్లేషణాత్మక లేదా తాత్త్విక-ఒప్పందంతో ఉంటే, `experiment` ను ఎంచుకోండి.
- అభ్యర్థన బోధనాత్మక, దశ-బై-దశ లేదా ఇతర ప్రేక్షకులకు ఉద్దేశించబడినదై ఉంటే, `tutorial` ను ఎంచుకోండి.
- ఒకటి ఉన్న నోట్‌బుక్‌ను సవరించేటప్పుడు, దానిని రిఫ్యాక్టర్‌గా తీసుకోండి: ఉద్దేశ్యాన్ని నిలుపుకోండి మరియు నిర్మాణాన్ని మెరుగుపరచండి.

## Skill path (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Workflow
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

## Templates and helper script
- Templates live in `assets/experiment-template.ipynb` and `assets/tutorial-template.ipynb`.
- The helper script loads a template, updates the title cell, and writes a notebook.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp and output conventions
- Use `tmp/jupyter-notebook/` for intermediate files; delete when done.
- Write final artifacts under `output/jupyter-notebook/` when working in this repo.
- Use stable, descriptive filenames (for example, `ablation-temperature.ipynb`).

## Dependencies (install only when needed)
Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## Environment
No required environment variables.

## Reference map
- `references/experiment-patterns.md`: experiment structure and heuristics.
- `references/tutorial-patterns.md`: tutorial structure and teaching flow.
- `references/notebook-structure.md`: notebook JSON shape and safe editing rules.
- `references/quality-checklist.md`: final validation checklist.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి యత్నిస్తామొక్క, కాని స్వయంచాలక అనువాదాలలో పొరపాట్లు లేదా తప్పులు ఉండే అవకాశం ఉందని దయచేసి గమనించండి. మూల భాషలోని అసలైన పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదాన్ని సిఫార్సు చేయబడుతుంది. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పైన అనువయానాల కోసం మేము బాధ్యులం కము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->