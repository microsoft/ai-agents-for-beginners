# Structura notebook-ului

Jupyter notebooks sunt documente JSON cu această structură generală:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (o listă de celule markdown și celule de cod)

Când editați fișierele `.ipynb` programatic:

- Păstrați `nbformat` și `nbformat_minor` din șablon.
- Păstrați `cells` ca o listă ordonată; nu reordonați decât dacă este intenționat.
- Pentru celulele de cod, setați `execution_count` la `null` când este necunoscut.
- Pentru celulele de cod, setați `outputs` la o listă goală când creați scheletul.
- Pentru celulele markdown, păstrați `cell_type="markdown"` și `metadata={}`.

Preferați crearea scheletului folosind șabloanele incluse sau `new_notebook.py` (de exemplu, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) în loc să scrieți manual JSON brut al notebook-ului.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă o traducere profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări eronate care ar putea rezulta din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->