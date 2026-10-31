# Esempi di Ricevute

Tre file di ricevute pre-generati per l'ispezione senza eseguire il notebook.

| File | Cosa è |
|---|---|
| `01_valid_receipt.json` | Una ricevuta valida firmata per una chiamata allo strumento `lookup_flights`. La verifica restituisce True. |
| `02_tampered_receipt.json` | La stessa ricevuta con un campo modificato dopo la firma. La verifica restituisce False. |
| `03_chain_three_receipts.json` | Una catena di tre ricevute valide (search, hold, book) con `previous_receipt_hash` che collega ciascuna alla precedente. |

Gli esempi firmano direttamente i byte canonici JCS del payload con Ed25519.
SHA-256 rimane in uso per i digest del contenuto e i collegamenti della catena di ricevute, non come
pre-hash extra prima della firma.

## Verifica degli esempi

In `18-signed-receipts.ipynb`, esegui prima Setup e le Sezioni da 1 a 3.
La Sezione 3 definisce `verify_chain`; da sole le Sezioni 1 e 2 non bastano.
Poi esegui il blocco seguente in una nuova cella, con la directory di lavoro del notebook impostata
su `18-securing-ai-agents/code_samples`. I percorsi degli esempi sotto sono relativi
a quella directory.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# This fixture key is pinned by the verifier, outside the receipt under test.
FIXTURE_ISSUER_PUBLIC_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"
fixture_trusted_public_keys = {FIXTURE_ISSUER_PUBLIC_KEY}

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text())
print(
    f"Valid receipt: {verify_receipt(valid, fixture_trusted_public_keys)}"
)  # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text())
print(
    f"Tampered receipt: {verify_receipt(tampered, fixture_trusted_public_keys)}"
)  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text())
for r in verify_chain(chain, fixture_trusted_public_keys):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

### Controllare l'esempio senza Jupyter

Dalla radice del repository, installa le dipendenze della lezione ed esegui:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Questi test eseguono gli esempi Python del notebook e il blocco esatto nel README
sopra. Controllano anche che la manomissione e le chiavi non fissate siano respinte dai
verificatori. I test saltano la cella di setup `%pip` del notebook perché le dipendenze
vengono installate separatamente. Non modificano il notebook o gli esempi.

## Come sono stati generati

Gli esempi usano lo stesso percorso di codice del notebook, con una chiave di firma fissa
e timestamp fissi per la riproducibilità a livello di byte. Per rigenerare:

```bash
python3 generate_fixtures.py
```

(Lo script si trova in `generate_fixtures.py` in questa directory.)

## Cosa imparano gli studenti ispezionando il JSON grezzo

Leggere il formato grezzo della ricevuta sviluppa un’intuizione che le celle nel notebook
non sempre forniscono. Gli studenti che scorrono il JSON spesso notano:

1. La firma è una stringa opaca base64url, ma ogni altro campo è JSON leggibile
   in chiaro. La firma non cripta il contenuto; ne attesta l’autenticità.
2. `public_key` è incorporato nella ricevuta, il che è sufficiente per controllare
   l'auto-consistenza ma non la fiducia nell’issuer. Un revisore deve confrontarlo con una chiave
   fissata al di fuori della ricevuta o risolta tramite un registro di fiducia.
3. Modificare anche un solo carattere di qualsiasi campo e poi riconfrontare questo file con
   `02_tampered_receipt.json` rende concreto il meccanismo a livello di byte.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->