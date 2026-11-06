# Δείγματα Αποδείξεων

Τέσσερα προγεννημένα αρχεία απόδειξης για επιθεώρηση χωρίς να τρέξετε το σημειωματάριο.

| Αρχείο | Τι είναι |
|---|---|
| `01_valid_receipt.json` | Μια έγκυρη υπογεγραμμένη απόδειξη για κλήση εργαλείου `lookup_flights`. Η επαλήθευση επιστρέφει True. |
| `02_tampered_receipt.json` | Η ίδια απόδειξη με ένα πεδίο τροποποιημένο μετά την υπογραφή. Η επαλήθευση επιστρέφει False. |
| `03_chain_three_receipts.json` | Μια αλυσίδα τριών έγκυρων αποδείξεων (αναζήτηση, κράτηση, κράτηση) με `previous_receipt_hash` που συνδέει κάθε μια με την προηγούμενη. |
| `04_resigned_receipt.json` | Η ίδια απόδειξη παραποιημένη και έπειτα υπογεγραμμένη ξανά από έναν επιτιθέμενο, με το δικό του δημόσιο κλειδί ενσωματωμένο. Επαληθεύεται έναντι του κλειδιού μέσα σε αυτήν. Αποτυγχάνει έναντι του κλειδιού του εκδότη. |

Οι αποδείξεις υπογράφουν τα κανονικοποιημένα bytes JCS του φορτίου απευθείας με Ed25519.
Το SHA-256 παραμένει σε χρήση για ψηφιακές υπογραφές περιεχομένου και συνδέσμους αλυσίδας απόδειξης, όχι ως
επιπλέον προ-κατακερματισμός πριν από την υπογραφή.

## Επαλήθευση των δειγμάτων

Στο `18-signed-receipts.ipynb`, τρέξτε πρώτα τη Ρύθμιση και τις Ενότητες 1 έως 3.
Η Ενότητα 3 ορίζει το `verify_chain`· οι Ενότητες 1 και 2 μόνες τους δεν αρκούν.
Μετά τρέξτε τον ακόλουθο κώδικα σε νέο κελί, με τον τρέχοντα κατάλογο εργασίας του σημειωματαρίου
ρυθμισμένο σε `18-securing-ai-agents/code_samples`. Οι διαδρομές των δειγμάτων παρακάτω είναι σχετικές
προς αυτόν τον κατάλογο.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### Έλεγχος του παραδείγματος χωρίς Jupyter

Από τη ρίζα του αποθετηρίου, εγκαταστήστε τις εξαρτήσεις του μαθήματος και τρέξτε:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Αυτά τα τεστ εκτελούν τα παραδείγματα Python του σημειωματαρίου και το ακριβές κομμάτι README
παραπάνω. Επίσης ελέγχουν ότι η παραποίηση και τα μη καρφωμένα κλειδιά απορρίπτονται από τους
επαληθευτές. Τα τεστ παραλείπουν το κελί ρύθμισης `%pip` του σημειωματαρίου επειδή οι εξαρτήσεις
εγκαθίστανται ξεχωριστά. Δεν αλλάζουν το σημειωματάριο ή τα δείγματα.

## Πώς δημιουργήθηκαν αυτά

Τα δείγματα χρησιμοποιούν την ίδια διαδρομή κώδικα με το σημειωματάριο, με ένα σταθερό κλειδί υπογραφής
και σταθερές χρονικές σφραγίδες για αναπαραγωγιμότητα byte. Για να τα ξαναδημιουργήσετε:

```bash
python3 generate_fixtures.py
```

(Το σενάριο βρίσκεται στο `generate_fixtures.py` σε αυτόν τον κατάλογο.)

Το `../test_signed_receipts.py` ελέγχει όλα αυτά αυτόματα: εκτελεί τον
κώδικα του σημειωματαρίου, επαληθεύει αυτά τα τέσσερα δείγματα με το
`verify_receipt` και `verify_chain` του σημειωματαρίου, και επιβεβαιώνει ότι η επαναδημιουργία των
δειγμάτων δίνει ταυτόσημα bytes. Από το `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Τι μαθαίνουν οι μαθητές από την επιθεώρηση ακατέργαστου JSON

Η ανάγνωση της μορφής ακατέργαστης απόδειξης χτίζει διαίσθηση που τα κελιά του σημειωματαρίου
δεν παρέχουν πάντα. Οι μαθητές που παρατηρούν το JSON συχνά διαπιστώνουν:

1. Η υπογραφή είναι μια αδιαφανής συμβολοσειρά base64url, αλλά κάθε άλλο πεδίο είναι απλό
   αναγνώσιμο JSON. Η υπογραφή δεν κρυπτογραφεί το περιεχόμενο· το βεβαιώνει.
2. Το `public_key` είναι ενσωματωμένο στην απόδειξη, κάτι που κάνει το αρχείο
   αυτόνομο αλλά δεν είναι αυτό που ελέγχει ο ελεγκτής. Συγκρίνετε
   `02_tampered_receipt.json` με `04_resigned_receipt.json`: και τα δύο
   τροποποιήθηκαν μετά την υπογραφή, αλλά το δεύτερο υπογράφτηκε ξανά με το δικό
   κλειδί του επιτιθέμενου, άρα επαληθεύεται έναντι του κλειδιού που φέρει. Το ενσωματωμένο κλειδί
   σας λέει ότι το αρχείο είναι εσωτερικά συνεπές. Μόνο κλειδί που αποκτήθηκε
   αλλού σας λέει ποιος το εξέδωσε.
3. Η τροποποίηση ενός απλού χαρακτήρα σε οποιοδήποτε πεδίο εκτός από `signature`, και
   στη συνέχεια η επανασύγκριση αυτού του αρχείου με το `02_tampered_receipt.json`, κάνει
   τον μηχανισμό σε επίπεδο byte απτό.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->