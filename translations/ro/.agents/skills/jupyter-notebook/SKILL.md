---
name: jupyter-notebook
description: Se folosește atunci când utilizatorul solicită crearea, structurarea
  sau editarea notebook-urilor Jupyter (`.ipynb`) pentru experimente, explorări sau
  tutoriale; se recomandă utilizarea șabloanelor incluse și rularea scriptului de
  asistență `new_notebook.py` pentru a genera un notebook de pornire curat.
---
# Competență Jupyter Notebook

Creează notebook-uri Jupyter curate și reproductibile pentru două moduri principale:

- Experimente și analiză exploratorie
- Tutoriale și ghiduri orientate spre predare

Folosește șabloanele incluse și scriptul de asistență pentru o structură consecventă și mai puține erori JSON.

## Când să folosești
- Creează un nou notebook `.ipynb` de la zero.
- Convertește notițe sau scripturi schițate într-un notebook structurat.
- Refactorizează un notebook existent pentru a fi mai reproductibil și mai ușor de parcurs.
- Creează experimente sau tutoriale care vor fi citite sau rulate din nou de alte persoane.

## Arbore decizional
- Dacă solicitarea este exploratorie, analitică sau bazată pe ipoteze, alege `experiment`.
- Dacă solicitarea este instructivă, pas cu pas sau specifică unui public, alege `tutorial`.
- Dacă editezi un notebook existent, tratează-l ca pe o refactorizare: păstrează intenția și îmbunătățește structura.

## Parcurs de competență (se setează o singură dată)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Flux de lucru
1. Fixează intenția.
Identifică tipul de notebook: `experiment` sau `tutorial`.
Stabilește obiectivul, publicul și cum arată "done".

2. Pornește de la un șablon.
Folosește scriptul ajutător pentru a evita scrierea manuală a JSON-ului brut al notebook-ului.

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

3. Completează notebook-ul cu pași mici, executabili.
Păstrează fiecare celulă de cod concentrată pe un singur pas.
Adaugă celule scurte markdown care explică scopul și rezultatul așteptat.
Evită output-uri mari și zgomotoase atunci când un scurt rezumat este suficient.

4. Aplică tiparul potrivit.
Pentru experimente, urmează `references/experiment-patterns.md`.
Pentru tutoriale, urmează `references/tutorial-patterns.md`.

5. Editează în siguranță atunci când lucrezi cu notebook-uri existente.
Păstrează structura notebook-ului; evită reordonarea celulelor decât dacă îmbunătățește fluxul de sus în jos al narațiunii.
Preferă editările țintite în locul rescrierilor complete.
Dacă trebuie să editezi JSON brut, consultă mai întâi `references/notebook-structure.md`.

6. Validează rezultatul.
Rulează notebook-ul de sus în jos când mediul permite.
Dacă execuția nu este posibilă, menționează explicit acest lucru și explică cum se poate valida local.
Folosește lista de verificare finală din `references/quality-checklist.md`.

## Șabloane și scriptul de asistență
- Șabloanele se află în `assets/experiment-template.ipynb` și `assets/tutorial-template.ipynb`.
- Scriptul de asistență încarcă un șablon, actualizează celula de titlu și scrie un notebook.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (instalat implicit: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Convenții pentru fișiere temporare și de ieșire
- Folosește `tmp/jupyter-notebook/` pentru fișiere intermediare; șterge-le la final.
- Scrie artefactele finale în `output/jupyter-notebook/` când lucrezi în acest repo.
- Folosește nume de fișiere stabile și descriptive (de exemplu, `ablation-temperature.ipynb`).

## Dependențe (instalează numai când este necesar)
Preferă `uv` pentru gestionarea dependențelor.

Pachete Python opționale pentru executarea locală a notebook-urilor:

```bash
uv pip install jupyterlab ipykernel
```

Scriptul de schelă inclus folosește doar biblioteca standard Python și nu necesită dependențe suplimentare.

## Mediu
Nu sunt variabile de mediu obligatorii.

## Harta de referință
- `references/experiment-patterns.md`: structură și euristici pentru experimente.
- `references/tutorial-patterns.md`: structură a tutorialelor și fluxul de predare.
- `references/notebook-structure.md`: forma JSON a notebook-ului și reguli pentru editare în siguranță.
- `references/quality-checklist.md`: lista de verificare pentru validarea finală.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Declinare de responsabilitate:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă o traducere profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->