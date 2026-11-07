# Esempi di Ricevute

Quattro file di ricevute pre-generati per l'ispezione senza eseguire il notebook.

| File | Cos'è |
|---|---|
| `01_valid_receipt.json` | Una ricevuta valida firmata per una chiamata allo strumento `lookup_flights`. La verifica restituisce True. |
| `02_tampered_receipt.json` | La stessa ricevuta con un campo modificato dopo la firma. La verifica restituisce False. |
| `03_chain_three_receipts.json` | Una catena di tre ricevute valide (search, hold, book) con `previous_receipt_hash` che collega ciascuna alla precedente. |
| `04_resigned_receipt.json` | La stessa ricevuta manomessa e poi rifirmata da un attaccante, con la chiave pubblica dell'attaccante incorporata. Verifica con la chiave interna. Fallisce con la chiave dell'emittente. |

Le fixture firmano direttamente i byte canonici JCS del payload con Ed25519.
SHA-256 rimane in uso per i digest del contenuto e i collegamenti della catena di ricevute, non come un
pre-hash extra prima della firma.

## Verifica degli esempi

In `18-signed-receipts.ipynb`, esegui prima Setup e le Sezioni da 1 a 3.
La Sezione 3 definisce `verify_chain`; solo le Sezioni 1 e 2 non sono sufficienti.
Quindi esegui il blocco seguente in una nuova cella, con la directory di lavoro del notebook
impostata su `18-securing-ai-agents/code_samples`. I percorsi delle fixture sottostanti sono relativi
a quella directory.

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

### Controllo dell'esempio senza Jupyter

Dalla radice del repository, installa le dipendenze della lezione ed esegui:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Questi test eseguono gli esempi Python del notebook e lo stesso blocco README
sopra. Controllano anche che la manomissione e le chiavi non fissate vengano respinte dai
verificatori. I test saltano la cella di setup `%pip` del notebook perché le dipendenze
sono installate separatamente. Non modificano il notebook o le fixture.

## Come sono stati generati

Le fixture utilizzano lo stesso percorso di codice del notebook, con una chiave di firma fissa
e timestamp fissi per la riproducibilità dei byte. Per rigenerare:

```bash
python3 generate_fixtures.py
```

(Lo script si trova in `generate_fixtures.py` in questa directory.)

`../test_signed_receipts.py` controlla tutto questo automaticamente: esegue il
codice del notebook, verifica queste quattro fixture con il
`verify_receipt` e `verify_chain` del notebook, e conferma che rigenerare le
fixture produce byte identici. Da `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Cosa imparano gli studenti ispezionando il JSON grezzo

La lettura del formato grezzo della ricevuta costruisce un'intuizione che le celle nel notebook
a volte non forniscono. Gli studenti che scorrono il JSON spesso notano:

1. La firma è una stringa opaca base64url, ma ogni altro campo è JSON leggibile
   normale. La firma non cifra il contenuto; lo attesta.
2. `public_key` è incorporato nella ricevuta, il che rende il file
   autonomo ma non è ciò contro cui un revisore verifica. Confronta
   `02_tampered_receipt.json` con `04_resigned_receipt.json`: entrambi sono stati
   alterati dopo la firma, ma il secondo è stato rifirmato con la chiave
   dell'attaccante, quindi verifica contro la chiave che porta. La chiave incorporata
   indica che il file è internamente coerente. Solo una chiave ottenuta
   altrove indica chi lo ha emesso.
3. Modificare un singolo carattere di qualsiasi campo fuori da `signature`, quindi
   ricontrollare questo file con `02_tampered_receipt.json`, rende il
   meccanismo a livello di byte concreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->