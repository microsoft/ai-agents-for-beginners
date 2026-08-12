---
name: jupyter-notebook
description: Tumia wakati mtumiaji anapoomba kuunda, kupanga muundo (scaffold), au
  kuhariri daftari za Jupyter (`.ipynb`) kwa majaribio, uchunguzi, au mafunzo; pendelea
  violezo vinavyokuja pamoja na uendeshe skripti ya msaidizi `new_notebook.py` ili
  kuunda daftari safi la kuanzia.
---
# Ujuzi wa Jupyter Notebook

Unda daftari za Jupyter zilizopangwa vizuri, zinazoweza kurudiwa kwa njia mbili kuu:

- Maajaribio na uchambuzi wa uchunguzi
- Mafunzo na mwongozo wa kufundisha

Tumia kiolezo kilichopo pamoja na skripti ya msaada kwa muundo thabiti na makosa machache ya JSON.

## Wakati wa kutumia
- Unda daftari jipya la `.ipynb` kutoka mwanzo.
- Badilisha noti za awali au skripti kuwa daftari lililopangwa.
- Boresha daftari lililopo ili liweze kurudiwa na kusomwa kwa haraka.
- Jenga majaribio au mafunzo yatakayosomwa au kutekelezwa tena na watu wengine.

## Mti wa maamuzi
- Ikiwa ombi ni la uchunguzi, la uchambuzi, au linaloongozwa na nadharia, chagua `experiment`.
- Ikiwa ombi ni la mafunzo, hatua kwa hatua, au linalolenga hadhira maalum, chagua `tutorial`.
- Unapohariri daftari lililopo, lishughulikie kama marekebisho: hifadhi nia na boresha muundo.

## Njia ya ujuzi (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Mtiririko wa kazi
1. Weka nia.
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
- Violezo viko katika `assets/experiment-template.ipynb` na `assets/tutorial-template.ipynb`.
- Skripti ya msaada inabeba kiolezo, inasasisha seli ya kichwa, na inaandika daftari.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Temp and output conventions
- Tumia `tmp/jupyter-notebook/` kwa mafaili ya kati; futa wakati umemaliza.
- Andika makala za mwisho chini ya `output/jupyter-notebook/` unapoifanya kazi katika repo hii.
- Tumia majina ya mafaili thabiti na yaliyoeleweka (kwa mfano, `ablation-temperature.ipynb`).

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
- `references/experiment-patterns.md`: muundo wa majaribio na mbinu za heuristiki.
- `references/tutorial-patterns.md`: muundo wa mafunzo na mtiririko wa kufundisha.
- `references/notebook-structure.md`: muundo wa JSON wa daftari na kanuni za kuhariri kwa usalama.
- `references/quality-checklist.md`: orodha ya ukaguzi wa mwisho.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tamko**:
Dokumenti hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au ukosefu wa usahihi. Nakala ya awali ya dokumenti katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, inapendekezwa kutumia tafsiri ya kitaalamu iliyofanywa na mtafsiri wa binadamu. Hatuwajibiki kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->