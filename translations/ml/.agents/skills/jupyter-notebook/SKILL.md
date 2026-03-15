---
name: jupyter-notebook
description: ഉപയോക്താവ് പരീക്ഷണങ്ങൾ, അന്വേഷണങ്ങൾ, അല്ലെങ്കിൽ ട്യൂട്ടോറിയലുകൾക്കുള്ള
  Jupyter നോട്ട്ബുക്കുകൾ (`.ipynb`) സൃഷ്ടിക്കാൻ, സ്‌കാഫോൾഡ് ചെയ്യാൻ, അല്ലെങ്കിൽ തിരുത്താൻ
  ആവശ്യപ്പെടുമ്പോൾ ഉപയോഗിക്കുക; ബണ്ടിൽ ചെയ്ത ടെംപ്ലേറ്റുകൾ പ്രാഥമ്യം നൽകുക, കൂടാതെ
  ശുദ്ധമായ ആരംഭ നോട്ട്ബുക്ക് സൃഷ്ടിക്കാൻ സഹായി സ്ക്രിപ്റ്റ് `new_notebook.py` ഓടിക്കുക.
---
# Jupyter Notebook കഴിവ്

രണ്ട് പ്രധാന രീതികൾക്കായി ശുദ്ധവും പുനരുത്പാദനയോഗ്യവുമായ Jupyter നോട്ട്‌ബുക്കുകൾ സൃഷ്ടിക്കുക:

- പരീക്ഷണങ്ങളും പര്യവേക്ഷണ വിശകലനവും
- ട്യൂട്ടോറിയലുകളും അധ്യയനമാധ്യമമായ വഴി-നടപടികളും

സ്ഥിരമായ ഘടനക്കും JSON പിശകുകൾ കുറയ്ക്കുന്നതിനും ബണ്ടിൽ ചെയ്ത ടെംപ്ലേറ്റുകളും സഹായകരമായ സ്ക്രിപ്റ്റും മുൻഗണന നൽകുക.

## ഉപയോഗിക്കേണ്ടപ്പോൾ
- നിലംതുറന്നുതന്നെ ഒരു പുതിയ `.ipynb` നോട്ട്‌ബുക്ക് സൃഷ്ടിക്കുക.
- സൂക്ഷ്മമല്ലാത്ത കുറിപ്പുകൾ അല്ലെങ്കിൽ സ്ക്രിപ്റ്റുകൾ ഘടനയുള്ള നോട്ട്‌ബുക്കായി പരിവർത്തനം ചെയ്യുക.
- നിലവിലുള്ള നോട്ട്‌ബുക്ക് പുനർരൂപപ്പെടുത്തുകയും അത് കൂടുതൽ പുനരുത്പാദനയോഗ്യവും സരളമായി പരിശോധിക്കാവുന്നതുമായതും ചെയ്യുക.
- മറ്റുള്ളവർ വായിക്കുകയോ വീണ്ടും പ്രവർത്തിപ്പിക്കുകയോ ചെയ്യാൻ ഉദ്ദേശിച്ച പരീക്ഷണങ്ങൾ അല്ലെങ്കിൽ ട്യൂട്ടോറിയലുകൾ നിർമിക്കുക.

## തീരുമാനം വൃക്ഷം
- അഭ്യർത്ഥന പര്യവേക്ഷണാത്മകമോ വിശകലനപരമോ ഹൈപ്പോത്തസിസ്-ചാലിതമോ ആയാൽ, `experiment` തിരഞ്ഞെടുക്കുക.
- അഭ്യർത്ഥന നിർദ്ദേശപരമോ ഘട്ടം-വഴികാട്ടിയോ അല്ലെങ്കിൽ പ്രത്യേക പ്രേക്ഷകരെ ലക്ഷ്യമാക്കിയതായെങ്കിൽ, `tutorial` തിരഞ്ഞെടുക്കുക.
- നിലവിലുള്ള നോട്ട്‌ബുക്ക് എഡിറ്റ് ചെയ്യുകയാണെങ്കിൽ, അത് റിഫാക്ടർ ആയി കാണുക: ഉദ്ദേശം നിലനിർത്തുകയും ഘടന മെച്ചപ്പെടുത്തുകയും ചെയ്യുക.

## സ്കിൽ പാത്ത് (ഒരു പ്രാവശ്യം ക്രമീകരിക്കുക)

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
- `$JUPYTER_NOTEBOOK_CLI` (ഇൻസ്റ്റാൾ ചെയ്ത ഡീഫോൾട്ട്: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

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
- `references/experiment-patterns.md`: പരീക്ഷണ ഘടനയും നയങ്ങളും.
- `references/tutorial-patterns.md`: ട്യൂട്ടോറിയൽ ഘടനയും പഠന പ്രവാഹവും.
- `references/notebook-structure.md`: നോട്ട്‌ബുക്ക് JSON ശൈലിയും സുരക്ഷിത എഡിറ്റിംഗ് നിയമങ്ങളും.
- `references/quality-checklist.md`: അവസാന പരിശോധനം നടത്താനുളള ചെക്ലിസ്റ്റ്.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഉത്തരവാദിത്വ മോചനം:
ഈ പ്രമാണം AI പരിഭാഷാ സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. നാം കൃത്യതയിലേക്ക് ശ്രമിച്ചിരിക്കുകയും ചെയ്തതായിരുന്നാലും, യന്ത്രപരിഭാഷകളിൽ പിശകുകൾക്കും അസത്യതകൾക്കും വഴിവെക്കാനുള്ള സാധ്യതയുണ്ടെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അടിസ്ഥാന ഭാഷയിലുള്ള മൂല പ്രമാണം പ്രാമാണികമായ ഉറവിടമായാണ് കണക്കാക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനവ പരിഭാഷおすすめ (സുചിപ്പിക്കുന്നു). ഈ പരിഭാഷ ഉപയോഗിച്ചതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകളോ തെറ്റായ വ്യാഖ്യാനങ്ങളോ സംബന്ധിച്ചുള്ള ഉത്തരവാദിത്തം ഞങ്ങളിലില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->