---
name: jupyter-notebook
description: ഉപയോക്താവ് പരീക്ഷണങ്ങൾ, കണ്ടെത്തലുകൾ, അല്ലെങ്കിൽ ട്യൂട്ടോറിയലുകൾക്കായി
  Jupyter നോട്ട്ബുക്കുകൾ (`.ipynb`) സൃഷ്ടിക്കാൻ, സ്കാഫോൾഡ് ചെയ്യാൻ, അല്ലെങ്കിൽ തിരുത്താൻ
  അഭ്യർത്ഥിച്ചാൽ ഉപയോഗിക്കുക; ബണ്ടിലോടിച്ച ടെംപ്ലേറ്റുകൾക്ക് മുൻഗണന നൽകുകയും ശുചിയായ
  ആരംഭ നോട്ട്ബുക്ക് സൃഷ്ടിക്കാൻ ഹെൽപ്പർ സ്ക്രിപ്റ്റ് `new_notebook.py` ഓടിക്കുകയും
  ചെയ്യുക.
---
# Jupyter Notebook നൈപുണ്യം

രണ്ട് പ്രാഥമിക രീതികൾക്കായി ശുദ്ധമാകുന്ന, പുനരുത്പാദിപ്പിക്കാവുന്ന Jupyter നോട്ട്ബുക്കുകൾ സൃഷ്ടിക്കുക:

- പരീക്ഷണങ്ങളും അന്വേഷനാത്മക വിശകലനവും
- ട്യൂട്ടോറിയലുകളും അധ്യാപനമേഖലയിലേക്കുള്ള കൈവഴികാട്ടലുകളും

സുസ്ഥിര ഘടനക്കും JSON പിഴവുകൾ കുറയ്ക്കുന്നതിനും ബണ്ടിൽ ചെയ്ത ടെംപ്ലേറ്റുകളും സഹായക സ്ക്രിപ്റ്റും ഉപയോഗിക്കുന്നത് മുൻഗണന നൽകുക.

## When to use
- Create a new `.ipynb` notebook from scratch.
- Convert rough notes or scripts into a structured notebook.
- Refactor an existing notebook to be more reproducible and skimmable.
- Build experiments or tutorials that will be read or re-run by other people.

## Decision tree
- If the request is exploratory, analytical, or hypothesis-driven, choose `experiment`.
- If the request is instructional, step-by-step, or audience-specific, choose `tutorial`.
- If editing an existing notebook, treat it as a refactor: preserve intent and improve structure.

## Skill path (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Workflow
1. Lock the intent.
ഉദ്ദേശ്യം നിശ്ചയിക്കുക: നോട്ട്‌ബുക്ക് തരമറിയിക്കുക — `experiment` അല്ലെങ്കിൽ `tutorial`.
ലക്ഷ്യം, പ്രേക്ഷകർ, ഒപ്പം "done" എങ്ങനെ കാണപ്പെടുമെന്ന് രേഖപ്പെടുത്തുക.

2. Scaffold from the template.
ടെംപ്ലേറ്റ് ഉപയോഗിച്ച് അടിസ്ഥാന ഘടനം സോഫ്റ്റ്-സ്‌കാഫോൾഡ് ചെയ്യുക.
Raw notebook JSON കൈയെഴുതുന്നത് ഒഴിവാക്കാൻ ഹെൽപ്പർ സ്ക്രിപ്റ്റ് ഉപയോഗിക്കുക.

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
ഓരോ കോഡ് സെൽും ഒരു ഘട്ടത്തിൽ ശ്രദ്ധ കേന്ദ്രീകരിച്ചിരിക്കണം.
ഉദ്ദേശ്യവും പ്രതീക്ഷിക്കാവുന്ന ഫലവും വിശദീകരിക്കുന്ന ചെറിയ മാർക്ക് ഡൗൺ സെല്ലുകൾ ചേർക്കുക.
വലിയ ശബ്ദമുള്ള ഔട്ട്പുട്ടുകൾ ഒഴിവാക്കി, ചെറിയ സംഗ്രഹം पर्याप्तമാകുമ്പോൾ അതുകൊണ്ടുതീരിക്കുക.

4. Apply the right pattern.
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. Edit safely when working with existing notebooks.
നോട്ട്ബുക്ക് ഘടന സംരക്ഷിക്കുക; സെല്ലുകൾ വീണ്ടും ക്രമീകരിക്കുന്നത് ടോപ്പ്-ടു-ബോട്ടം കഥ മെച്ചപ്പെടുത്താതിരുന്നാൽ ഒഴിവാക്കുക.
പൂർണ റിറൈറ്റുകൾക്കേക്കാൾ ലക്ഷ്യമിട്ട എഡിറ്റുകൾക്ക് മുൻഗണന നൽകുക.
Raw JSON എഡിറ്റുചെയ്യേണ്ടിവരുന്നുവെങ്കിൽ, ആദ്യം `references/notebook-structure.md` പരിശോധിക്കുക.

6. Validate the result.
പരിസ്ഥിതി അനുവദിക്കുന്ന പക്ഷം നോട്ട്‌ബുക്ക് മുകളിലുനിന്ന് താഴെത്തോളം റൺ ചെയ്യുക.
എക്‌സിക്യൂഷൻ സാധ്യമല്ലെങ്കിൽ അതിനെ വ്യക്തമാക്കുകയും ലോക്കൽ ആയി എങ്ങനെ സാധൂകരിക്കാമെന്ന് വിളിപ്പിക്കയും ചെയ്യുക.
അവസാന പരിശോധനയ്ക്കായി `references/quality-checklist.md` ഉപയോഗിക്കുക.

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
- `references/experiment-patterns.md`: പരീക്ഷണങ്ങളുടെ ഘടനയും നയങ്ങളും.
- `references/tutorial-patterns.md`: ട്യൂട്ടോറിയലുകളുടെ ഘടനയും അധ്യാപന പ്രവാഹവും.
- `references/notebook-structure.md`: നോട്ട്‌ബുക്ക് JSON രൂപവും സുരക്ഷിത എഡിറ്റിംഗ് നിയമങ്ങളും.
- `references/quality-checklist.md`: അന്തിമ സ്ഥിരീകരണ ചെക്ക്ലിസ്റ്റ്.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഉത്തരവാദിത്വ നിഷേധം:
ഈ രേഖ AI തർജ്ജമാ സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് തർജ്ജമ ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് പരിശ്രമിച്ചിരിക്കുകയാണെങ്കിലും, ഓട്ടോമേറ്റഡ് തർജ്ജമകളിൽ പിശകുകൾ կամ അശുദ്ധതകൾ ഉണ്ടാകാമെന്നു ദയവായി ശ്രദ്ധിക്കുക. അസൽ ഭാഷയിലെ (മൂല) രേഖയെ പ്രാമാണികമായ ഉറവിടമായി കരുതുക. നിർണ്ണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനവ തർജ്ജമ ശുപാർശ ചെയ്യുന്നു. ഈ തർജ്ജമ ഉപയോഗിച്ചതിന്റെ ഫലമായി ഉണ്ടായ ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->