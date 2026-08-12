---
name: jupyter-notebook
description: ਜਦੋਂ ਉਪਭੋਗਤਾ ਤਜਰਬਿਆਂ, ਖੋਜਾਂ, ਜਾਂ ਟਿਊਟੋਰੀਅਲਾਂ ਲਈ Jupyter ਨੋਟਬੁੱਕ (`.ipynb`)
  ਬਣਾਉਣ, ਸਕੈਫੋਲਡ ਕਰਨ, ਜਾਂ ਸੋਧ ਕਰਨ ਨੂੰ ਕਹੇ, ਇਸਦਾ ਉਪਯੋਗ ਕਰੋ; ਬੰਡਲ ਕੀਤੇ ਟੈਮਪਲੇਟਾਂ ਨੂੰ
  ਤਰਜੀਹ ਦਿਓ ਅਤੇ ਇੱਕ ਸਾਫ਼ ਸ਼ੁਰੂਆਤੀ ਨੋਟਬੁੱਕ ਤਿਆਰ ਕਰਨ ਲਈ ਸਹਾਇਕ ਸਕ੍ਰਿਪਟ `new_notebook.py`
  ਚਲਾਓ.
---
# Jupyter Notebook Skill

ਦੋ ਪ੍ਰਮੁੱਖ ਮੋਡਾਂ ਲਈ ਸਾਫ਼, ਦੁਹਰਾਏ ਜਾਣ ਯੋਗ Jupyter ਨੋਟਬੁੱਕ ਬਣਾਓ:

- ਪ੍ਰਯੋਗ ਅਤੇ ਖੋਜਾਤਮਕ ਵਿਸ਼ਲੇਸ਼ਣ
- ਟਿਊਟੋਰੀਅਲ ਅਤੇ ਸਿੱਖਣ-ਕੇਂਦਰਿਤ ਵਾਕਥਰੂ

ਸੰਰਚਨਾ ਵਿੱਚ ਇਕਸਾਰਤਾ ਅਤੇ ਘੱਟ JSON ਗਲਤੀਆਂ ਲਈ ਬੰਡਲ ਕੀਤੀਆਂ ਟੈਂਪਲੇਟ ਅਤੇ ਹੈਲਪਰ ਸਕ੍ਰਿਪਟ ਦੀ ਪਸੰਦ ਕਰੋ।

## When to use
- ਇਕ ਨਵਾਂ `.ipynb` ਨੋਟਬੁੱਕ ਖਾਲੀ ਤੋਂ ਬਣਾਓ।
- ਅਣਗਢੇ ਨੋਟਸ ਜਾਂ ਸਕ੍ਰਿਪਟਾਂ ਨੂੰ ਸੰਗਠਿਤ ਨੋਟਬੁੱਕ ਵਿੱਚ ਬਦਲੋ।
- ਮੌਜੂਦਾ ਨੋਟਬੁੱਕ ਨੂੰ ਵਧੇਰੇ ਦੁਹਰਾਏ ਜਾਣਯੋਗ ਅਤੇ ਸਕਿਮेबल ਬਣਾਉਣ ਲਈ ਰਿਫੈਕਟਰ ਕਰੋ।
- ਐਸੇ ਪ੍ਰਯੋਗ ਜਾਂ ਟਿਊਟੋਰੀਅਲ ਬਣਾਓ ਜੋ ਹੋਰ ਲੋਕ ਪੜ੍ਹਨ ਜਾਂ ਦੁਬਾਰਾ ਚਲਾਉਣਗੇ।

## Decision tree
- ਜੇ ਬੇਨਤੀ ਖੋਜਾਤਮਕ, ਵਿਸ਼ਲੇਸ਼ਣਾਤਮਕ, ਜਾਂ ਕਾਰਨ-ਪ੍ਰਸਤਾਵਕ ਹੈ ਤਾਂ `experiment` ਚੁਣੋ।
- ਜੇ ਬੇਨਤੀ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ਕ, ਕਦਮ-ਦਰ-কਦਮ, ਜਾਂ ਦਰਸ਼ਕ-ਨਿਰਧਾਰਿਤ ਹੈ ਤਾਂ `tutorial` ਚੁਣੋ।
- ਜੇ ਮੌਜੂਦਾ ਨੋਟਬੁੱਕ ਨੂੰ ਸੋਧ ਰਹੇ ਹੋ, ਤਾਂ ਇਸਨੂੰ ਰਿਫੈਕਟਰ ਵਜੋਂ ਸਮਝੋ: ਮਕਸਦ ਬਰਕਰਾਰ ਰੱਖੋ ਅਤੇ ਸੰਰਚਨਾ ਸੁਧਾਰੋ।

## Skill path (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Workflow
1. Lock the intent.
ਨੋਟਬੁੱਕ ਕਿਸਮ ਦੀ ਪਛਾਣ ਕਰੋ: `experiment` ਜਾਂ `tutorial`।
ਉਦੇਸ਼, ਦਰਸ਼ਕ, ਅਤੇ "ਮੁਕੰਮਲ" ਹੋਣ ਦਾ ਮਾਪ ਕੀ ਹੈ ਇਹ ਦਰਜ ਕਰੋ।

2. Scaffold from the template.
ਹੱਥੋਂ ਹਥਿਆਰਬੰਦ কੱਚਾ ਨੋਟਬੁੱਕ JSON ਲਿਖਣ ਤੋਂ ਬਚਣ ਲਈ ਹੈਲਪਰ ਸਕ੍ਰਿਪਟ ਦੀ ਵਰਤੋਂ ਕਰੋ।

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
ਹਰ ਕੋਡ ਸੈੱਲ ਨੂੰ ਇੱਕ ਕਦਮ 'ਤੇ ਕੇਂਦ੍ਰਿਤ ਰੱਖੋ।
ਛੋਟੇ ਮਾਰਕਡਾਉਨ ਸੈੱਲ ਜੋ ਉਦੇਸ਼ ਅਤੇ ਉਮੀਦ ਕੀਤੀ ਨਤੀਜੇ ਨੂੰ ਸਮਝਾਉਂਦੇ ਹੋ ਸ਼ਾਮਲ ਕਰੋ।
ਜਦੋਂ ਛੋਟਾ ਸਾਰ ਕੰਮ ਕਰਦਾ ਹੈ ਤਾਂ ਵੱਡੇ, ਸ਼ੋਰ ਵਾਲੇ ਆਉਟਪੁੱਟੋਂ ਤੋਂ ਬਚੋ।

4. Apply the right pattern.
ਪ੍ਰਯੋਗਾਂ ਲਈ, `references/experiment-patterns.md` ਦੀ ਪਾਲਣਾ ਕਰੋ।
ਟਿਊਟੋਰੀਅਲਾਂ ਲਈ, `references/tutorial-patterns.md` ਦੀ ਪਾਲਣਾ ਕਰੋ।

5. Edit safely when working with existing notebooks.
ਨੋਟਬੁੱਕ ਦੀ ਸੰਰਚਨਾ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖੋ; ਸੈੱਲਾਂ ਨੂੰ ਦੁਬਾਰਾ ਕ੍ਰਮਬੱਧ ਕਰਨ ਤੋਂ ਬਚੋ ਜਦ ਤੱਕ ਕਿ ਇਹ ਉਪਰ ਤੋਂ ਹੇਠਾਂ ਦੀ ਕਹਾਣੀ ਨੂੰ ਸੁਧਾਰ ਨਾ ਦੇਵੇ।
ਪੂਰੇ ਰੀਰਾਈਟਸ ਦੇ ਬਦਲੇ ਟਰਗੇਟ ਕੀਤੀਆਂ ਸੋਧਾਂ ਨੂੰ ਤਰਜੀਹ ਦਿਓ।
ਜੇ ਤੁਹਾਨੂੰ ਕੱਚਾ JSON ਸੋਧਣਾ ਪੈਂਦਾ ਹੈ, ਤਾਂ ਪਹਿਲਾਂ `references/notebook-structure.md` ਦੀ ਸਮੀਖਿਆ ਕਰੋ।

6. Validate the result.
ਜਦੋਂ ਵਾਤਾਵਰਣ ਦੀ ਆਗਿਆ ਹੋਵੇ ਤਾਂ ਨੋਟਬੁੱਕ ਨੂੰ ਉਪਰ ਤੋਂ ਹੇਠਾਂ ਚਲਾਓ।
ਜੇ ਐਕਜ਼ਿਕਿਊਸ਼ਨ ਸੰਭਵ ਨਹੀਂ ਹੈ, ਤਾਂ ਇਸ ਨੂੰ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਦੱਸੋ ਅਤੇ ਲੋਕਲ ਰੂਪ ਵਿੱਚ ਕਿਵੇਂ ਵੈਰੀਫਾਈ ਕਰਨਾ ਹੈ ਇਹ ਦਰਜ ਕਰੋ।
`references/quality-checklist.md` ਵਿੱਚ ਦਿੱਤੇ ਆਖਰੀ ਪਾਸ ਚੈਕਲਿਸਟ ਦੀ ਵਰਤੋਂ ਕਰੋ।

## Templates and helper script
- ਟੈਂਪਲੇਟ `assets/experiment-template.ipynb` ਅਤੇ `assets/tutorial-template.ipynb` ਵਿੱਚ ਰਹਿੰਦੇ ਹਨ।
- ਹੈਲਪਰ ਸਕ੍ਰਿਪਟ ਇੱਕ ਟੈਂਪਲੇਟ ਲੋਡ ਕਰਦਾ ਹੈ, ਟਾਈਟਲ ਸੈੱਲ ਨੂੰ ਅੱਪਡੇਟ ਕਰਦਾ ਹੈ, ਅਤੇ ਨੋਟਬੁੱਕ ਲਿਖਦਾ ਹੈ।

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp and output conventions
- ਦਰਮਿਆਨੀ ਫਾਈਲਾਂ ਲਈ `tmp/jupyter-notebook/` ਦੀ ਵਰਤੋਂ ਕਰੋ; ਕੰਮ ਮੁੱਕਣ 'ਤੇ ਹਟਾ ਦਿਓ।
- ਇਸ ਰੈਪੋ ਵਿੱਚ ਕੰਮ ਕਰਦਿਆਂ ਅਖੀਰੀ ਨਤੀਜੇ `output/jupyter-notebook/` ਹੇਠਾਂ ਲਿਖੋ।
- ਸਥਿਰ, ਵੇਰਣਾਤਮਕ ਫਾਈਲ ਨਾਂ ਵਰਤੋਂ (ਉਦਾਹਰਨ ਲਈ, `ablation-temperature.ipynb`)।

## Dependencies (install only when needed)
ਡਿਪੈਂਡੈਂਸੀ ਮੈਨੇਜਮੈਂਟ ਲਈ `uv` ਨੂੰ ਤਰਜੀਹ ਦਿਓ।

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## Environment
ਕੋਈ ਲਾਜ਼ਮੀ ਐਨਵਾਇਰਨਮੈਂਟ ਵੇਰੀਏਬਲ ਨਹੀਂ ਹਨ।

## Reference map
- `references/experiment-patterns.md`: ਪ੍ਰਯੋਗ ਦੀ ਸੰਰਚਨਾ ਅਤੇheuristics.
- `references/tutorial-patterns.md`: ਟਿਊਟੋਰੀਅਲ ਦੀ ਸੰਰਚਨਾ ਅਤੇ ਸਿੱਖਣ ਦੀ ਪ੍ਰਵਾਹ।
- `references/notebook-structure.md`: ਨੋਟਬੁੱਕ JSON ਰੂਪ ਅਤੇ ਸੁਰੱਖਿਅਤ ਸੋਧ ਨਿਯਮ।
- `references/quality-checklist.md`: ਆਖਰੀ ਵੈਧਤਾ ਜਾਂਚ-ਪੱਤਰ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ਡਿਸਕਲੇਮਰ:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ AI ਅਨੁਵਾਦ ਸੇਵਾ Co-op Translator (https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਿਵੇਂ ਕਿ ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਥਿਰਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ, ਉਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ, ਅਧਿਕਾਰਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਅਹਿਮ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਾਰਨ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->