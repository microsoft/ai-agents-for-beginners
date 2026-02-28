---
name: jupyter-notebook
description: వినియోగదారు ప్రయోగాలు, అన్వేషణలు లేదా ట్యుటోరియల్స్ కోసం Jupyter నోటుబుక్స్
  (`.ipynb`) ని సృష్టించమని, మౌలిక నిర్మాణం సిద్ధం చేయమని లేదా సవరించమని అడిగినప్పుడు
  ఉపయోగించండి; బండిల్ చేయబడిన టెంప్లేట్లను ప్రాధాన్యంగా ఉపయోగించి శుభ్రమైన ప్రారంభ
  నోట్‌బుక్‌ను ఉత్పత్తి చేయడానికి సహాయక స్క్రిప్ట్ `new_notebook.py` ని నడపండి.
---
# Jupyter Notebook నైపుణ్యం

Create clean, reproducible Jupyter notebooks for two primary modes:

- ప్రయోగాలు మరియు అన్వేషణాత్మక విశ్లేషణ
- ట్యుటోరియల్స్ మరియు బోధన-కేంద్రీకృత దశల వారీ మార్గదర్శకాలు

Prefer the bundled templates and the helper script for consistent structure and fewer JSON mistakes.

## ఉపయోగించాల్సిన సందర్భాలు
- Create a new `.ipynb` notebook from scratch.
- అసంపూర్ణ గమనికలు లేదా స్క్రిప్ట్‌లను నిర్మాణాత్మక నోట్‌బుక్‌లుగా మార్చండి.
- ఒక ప్రస్తుత నోట్‌బుకును మరింత పునరుత్పాదకంగా మరియు తేలికగా చదవదగినదిగా రిఫ్యాక్టర్ చేయండి.
- ఇతరులు చదవగలిగే లేదా మళ్లీ అమలు చేయగలిగే ప్రయోగాలు లేదా ట్యుటోరియల్స్‌ను రూపొందించండి.

## నిర్ణయ వృక్షం
- వినతీ అన్వೇಷణాత్మకంగా, విశ్లేషణాత్మకంగా లేదా హైపోథీసిస్-ఆధారంగా ఉంటే, `experiment` ని ఎంచుకోండి.
- వినతీ బోధనాత్మకంగా, దశల వారీగా లేదా ప్రేక్షక-నిర్దేశితంగా ఉంటే, `tutorial` ని ఎంచుకోండి.
- ఒక ప్రస్తుత నోట్‌బుక్‌ను సవరిస్తుంటే, దాన్ని రిఫ్యాక్టర్‌లాగా పరిగణించండి: ఉద్దేశ్యాన్ని నిలిపి పెట్టండి మరియు నిర్మాణాన్ని మెరుగుపరుచండి.

## నైపుణ్య మార్గం (ఒకసారి సెటప్ చేయాలి)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## వర్క్‌ఫ్లో
1. ఉద్దేశాన్ని నిర్ధారించండి.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. టెంప్లేట్ నుండి స్కాఫోల్డ్ చేయండి.
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

3. నోట్‌బుక్‌ను చిన్న, అమలుచేయగల స్టెప్పులతో నింపండి.
Keep each code cell focused on one step.
Add short markdown cells that explain the purpose and expected result.
Avoid large, noisy outputs when a short summary works.

4. సరైన ప్యాటర్న్‌ను వర్తింపజేయండి.
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. ఇప్పటికే ఉన్న నోట్‌బుక్స్‌పై పనిచేస్తున్నప్పుడు సురక్షితంగా సవరించండి.
Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story.
Prefer targeted edits over full rewrites.
If you must edit raw JSON, review `references/notebook-structure.md` first.

6. ఫలితాన్ని ధృవీకరించండి.
Run the notebook top-to-bottom when the environment allows.
If execution is not possible, say so explicitly and call out how to validate locally.
Use the final pass checklist in `references/quality-checklist.md`.

## టెంప్లేట్లు మరియు సహాయక స్క్రిప్ట్
- టెంప్లేట్లు `assets/experiment-template.ipynb` మరియు `assets/tutorial-template.ipynb` లో ఉంటాయి.
- సహాయక స్క్రిప్ట్ ఒక టెంప్లేట్‌ను లోడ్ చేసి, టైటిల్ సెల్‌ని నవీకరించి, నోట్‌బుక్‌ను రాస్తుంది.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (స్థాపించబడిన డిఫాల్ట్: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## తాత్కాలిక మరియు అవుట్‌పుట్ నియమాలు
- మధ్యంతర ఫైళ్ల కోసం `tmp/jupyter-notebook/` ను ఉపయోగించండి; పూర్తయిన తర్వాత తొలగించండి.
- ఈ రేపోలో పనిచేస్తున్నప్పుడు ముగింపు ఆర్టిఫాక్ట్స్‌ను `output/jupyter-notebook/` కింద రాయండి.
- స్థిరమైన, వివరణాత్మక ఫైల్ పేర్లను ఉపయోగించండి (ఉదాహరణకు, `ablation-temperature.ipynb`).

## Dependencies (అవసరం ఉన్నప్పుడు మాత్రమే ఇన్‌స్టాల్ చేయండి)
Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## పర్యావరణం
అవసరమైన పర్యావరణ వేరియబుల్‌లు లేవు.

## సూచన మ్యాప్
- `references/experiment-patterns.md`: ప్రయోగ నిర్మాణం మరియు సాధనాత్మక నియమాలు.
- `references/tutorial-patterns.md`: ట్యుటోరియల్ నిర్మాణం మరియు బోధనా ప్రవాహం.
- `references/notebook-structure.md`: నోట్‌బుక్ JSON ఆకృతి మరియు సురక్షిత ఎడిటింగ్ నియమాలు.
- `references/quality-checklist.md`: ఫైనల్ ధృవీకరణ చెక్లిస్ట్.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
బాధ్యతా మినహాయింపు:
ఈ దస్తావేజును AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా లోపాలు ఉండవచ్చును అని దయచేసి గమనించండి. మూల దస్తావేజును దాని స్వదేశీ భాషలో ఉన్న వర్షన్‌ను అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదాన్ని సూచిస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడంపై మేము బాధ్యులు కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->