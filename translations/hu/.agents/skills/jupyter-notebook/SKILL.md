---
name: jupyter-notebook
description: Használható, amikor a felhasználó Jupyter notebookok (`.ipynb`) létrehozását,
  felépítését vagy szerkesztését kéri kísérletekhez, felfedezésekhez vagy oktatóanyagokhoz;
  részesítse előnyben a csomagolt sablonokat, és futtassa a segédprogramot `new_notebook.py`,
  hogy egy tiszta kezdő notebookot generáljon.
---
# Jupyter Notebook készség

Hozzon létre tiszta, reprodukálható Jupyter notebookokat két fő módra:

- Kísérletek és feltáró elemzés
- Oktató és tanítás-centrikus bemutatók

Használja előnyben a beépített sablonokat és a segédscriptet az egységes felépítéshez és kevesebb JSON-hiba érdekében.

## Mikor használjuk
- Hozzon létre egy új `.ipynb` jegyzetfüzetet a semmiből.
- Konvertáljon durva jegyzeteket vagy szkripteket strukturált jegyzetfüzetté.
- Refaktoráljon egy meglévő jegyzetfüzetet, hogy reprodukálhatóbb és könnyebben átfutható legyen.
- Építsen kísérleteket vagy oktatóanyagokat, amelyeket mások el fognak olvasni vagy újra futtatni.

## Döntési fa
- Ha a kérés feltáró, elemző vagy hipotézis-vezérelt, válassza a `experiment` módot.
- Ha a kérés oktató jellegű, lépésről-lépésre vagy konkrét közönségre szabott, válassza a `tutorial` módot.
- Ha meglévő jegyzetfüzetet szerkeszt, kezelje refaktorálásként: tartsa meg a szándékot és javítsa a szerkezetet.

## Készségút (egyszer beállítandó)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Munkafolyamat
1. Zárja le a szándékot.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. Készítse el a vázlatot a sablonból.
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

3. Töltse fel a jegyzetfüzetet kis, futtatható lépésekkel.
Keep each code cell focused on one step.
Add short markdown cells that explain the purpose and expected result.
Avoid large, noisy outputs when a short summary works.

4. Alkalmazza a megfelelő mintát.
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. Szerkesszen óvatosan, amikor meglévő jegyzetfüzetekkel dolgozik.
Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story.
Prefer targeted edits over full rewrites.
If you must edit raw JSON, review `references/notebook-structure.md` first.

6. Érvényesítse az eredményt.
Run the notebook top-to-bottom when the environment allows.
If execution is not possible, say so explicitly and call out how to validate locally.
Use the final pass checklist in `references/quality-checklist.md`.

## Sablonok és segédscript
- Templates live in `assets/experiment-template.ipynb` and `assets/tutorial-template.ipynb`.
- A segédscript betölt egy sablont, frissíti a cím cellát, és kiír egy jegyzetfüzetet.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Ideiglenes és kimeneti konvenciók
- Use `tmp/jupyter-notebook/` for intermediate files; delete when done.
- Write final artifacts under `output/jupyter-notebook/` when working in this repo.
- Use stable, descriptive filenames (for example, `ablation-temperature.ipynb`).

## Függőségek (telepítse csak ha szükséges)
Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

A csomagolt vázoló script csak a Python standard könyvtárát használja, és nem igényel további függőségeket.

## Környezet
Nincsenek kötelező környezeti változók.

## Referencia térkép
- `references/experiment-patterns.md`: kísérleti szerkezet és heurisztikák.
- `references/tutorial-patterns.md`: oktatóanyag szerkezete és tanítási folyamat.
- `references/notebook-structure.md`: a jegyzetfüzet JSON alakja és a biztonságos szerkesztési szabályok.
- `references/quality-checklist.md`: végső érvényesítési ellenőrzőlista.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Felelősségkizárás:
Ezt a dokumentumot a Co-op Translator mesterséges intelligencia alapú fordítószolgáltatás (https://github.com/Azure/co-op-translator) segítségével fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvi dokumentum tekintendő a hiteles forrásnak. Fontos információk esetén javasolt hivatásos, emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->