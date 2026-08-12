---
name: jupyter-notebook
description: Χρησιμοποιήστε όταν ο χρήστης ζητά να δημιουργήσει, να δομήσει ή να επεξεργαστεί
  σημειωματάρια Jupyter (`.ipynb`) για πειράματα, εξερευνήσεις ή σεμινάρια; προτιμήστε
  τα συνημμένα πρότυπα και εκτελέστε το βοηθητικό σκριπτ `new_notebook.py` για να
  δημιουργήσετε ένα καθαρό αρχικό σημειωματάριο.
---
# Δεξιότητα Jupyter Notebook

Δημιουργήστε καθαρά, αναπαραγώγιμα Jupyter notebooks για δύο κύριες λειτουργίες:

- Πειράματα και διερευνητική ανάλυση
- Σεμινάρια και οδηγοί προσανατολισμένοι στη διδασκαλία

Προτιμήστε τα ενσωματωμένα πρότυπα και το βοηθητικό script για συνεπή δομή και λιγότερα σφάλματα JSON.

## Πότε να το χρησιμοποιήσετε
- Δημιουργήστε ένα νέο `.ipynb` σημειωματάριο από το μηδέν.
- Μετατρέψτε πρόχειρες σημειώσεις ή σενάρια σε ένα δομημένο σημειωματάριο.
- Αναδιαρθρώστε ένα υπάρχον σημειωματάριο ώστε να είναι πιο αναπαραγώγιμο και εύκολο στο γρήγορο διάβασμα.
- Δημιουργήστε πειράματα ή σεμινάρια που θα διαβαστούν ή θα επανεκτελεστούν από άλλους.

## Δέντρο αποφάσεων
- Εάν το αίτημα είναι διερευνητικό, αναλυτικό ή καθοδηγούμενο από υπόθεση, επιλέξτε `experiment`.
- Εάν το αίτημα είναι εκπαιδευτικό, βήμα-προς-βήμα ή προσαρμοσμένο σε συγκεκριμένο κοινό, επιλέξτε `tutorial`.
- Αν επεξεργάζεστε ένα υπάρχον σημειωματάριο, αντιμετωπίστε το ως αναδιάρθρωση: διατηρήστε την πρόθεση και βελτιώστε τη δομή.

## Διαδρομή δεξιότητας (ορίζεται μία φορά)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Ροή εργασίας
1. Κλειδώστε την πρόθεση.
Identify the notebook kind: `experiment` or `tutorial`.
Καταγράψτε τον στόχο, το κοινό, και τι σημαίνει "ολοκληρωμένο".

2. Δημιουργήστε τη δομή από το πρότυπο.
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

3. Συμπληρώστε το σημειωματάριο με μικρά, εκτελέσιμα βήματα.
Διατηρήστε κάθε κελί κώδικα εστιασμένο σε ένα βήμα.
Προσθέστε σύντομα κελιά markdown που εξηγούν τον σκοπό και το αναμενόμενο αποτέλεσμα.
Αποφύγετε μεγάλα, θορυβώδη outputs όταν μια σύντομη περίληψη είναι επαρκής.

4. Εφαρμόστε το σωστό πρότυπο.
Για πειράματα, ακολουθήστε `references/experiment-patterns.md`.
Για tutorials, ακολουθήστε `references/tutorial-patterns.md`.

5. Επεξεργαστείτε με ασφάλεια όταν εργάζεστε με υπάρχοντα σημειωματάρια.
Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story.
Προτιμήστε στοχευμένες επεξεργασίες αντί πλήρων επαναγραφών.
Εάν πρέπει να επεξεργαστείτε ακατέργαστο JSON, αναθεωρήστε πρώτα `references/notebook-structure.md`.

6. Επικυρώστε το αποτέλεσμα.
Run the notebook top-to-bottom when the environment allows.
Εάν η εκτέλεση δεν είναι δυνατή, αναφέρετέ το ρητά και εξηγείστε πώς να επικυρωθεί τοπικά.
Use the final pass checklist in `references/quality-checklist.md`.

## Πρότυπα και βοηθητικό script
- Τα πρότυπα βρίσκονται στο `assets/experiment-template.ipynb` και `assets/tutorial-template.ipynb`.
- Το βοηθητικό script φορτώνει ένα πρότυπο, ενημερώνει το κελί τίτλου και γράφει ένα σημειωματάριο.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (προεπιλεγμένο εγκατάστασης: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Συμβάσεις προσωρινών αρχείων και εξόδου
- Χρησιμοποιήστε `tmp/jupyter-notebook/` για ενδιάμεσα αρχεία· διαγράψτε όταν τελειώσετε.
- Αποθηκεύστε τα τελικά αρχεία κάτω από `output/jupyter-notebook/` όταν εργάζεστε σε αυτό το αποθετήριο.
- Χρησιμοποιήστε σταθερά, περιγραφικά ονόματα αρχείων (για παράδειγμα, `ablation-temperature.ipynb`).

## Εξαρτήσεις (εγκατάσταση μόνο όταν χρειάζεται)
Προτιμήστε `uv` για τη διαχείριση εξαρτήσεων.

Προαιρετικά πακέτα Python για τοπική εκτέλεση σημειωματάριου:

```bash
uv pip install jupyterlab ipykernel
```

Το ενσωματωμένο script υποδομής χρησιμοποιεί μόνο τη βασική βιβλιοθήκη της Python και δεν απαιτεί επιπλέον εξαρτήσεις.

## Περιβάλλον
Δεν απαιτούνται μεταβλητές περιβάλλοντος.

## Χάρτης αναφορών
- `references/experiment-patterns.md`: δομή πειράματος και ευρετικές.
- `references/tutorial-patterns.md`: δομή οδηγιών και ροή διδασκαλίας.
- `references/notebook-structure.md`: σχήμα JSON του σημειωματαρίου και κανόνες ασφαλούς επεξεργασίας.
- `references/quality-checklist.md`: τελική λίστα ελέγχου επικύρωσης.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Αποποίηση ευθύνης:
Αυτό το έγγραφο έχει μεταφραστεί με τη χρήση της υπηρεσίας μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, σημειώστε ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύψουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->