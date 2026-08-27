# Campioni di Ricevute

Tre file di ricevute pre-generate per l'ispezione senza eseguire il notebook.

| File | Che cos'è |
|---|---|
| `01_valid_receipt.json` | Una ricevuta firmata valida per una chiamata allo strumento `lookup_flights`. La verifica restituisce True. |
| `02_tampered_receipt.json` | La stessa ricevuta con un campo modificato dopo la firma. La verifica restituisce False. |
| `03_chain_three_receipts.json` | Una catena di tre ricevute valide (ricerca, prenotazione temporanea, prenotazione) con `previous_receipt_hash` che collega ciascuna alla precedente. |

I fixtures firmano direttamente i byte canonici JCS del payload con Ed25519.
SHA-256 rimane in uso per i digest del contenuto e i collegamenti della catena di ricevute, non come
un pre-hash extra prima della firma.

## Verifica dei campioni

Il notebook spiega la verifica in quattro sezioni. Per verificare questi fixtures
direttamente senza passare dalla narrazione del notebook:

```python
import json
from pathlib import Path

# Presuppone che tu abbia completato le importazioni e le funzioni di supporto
# dalle sezioni 1 e 2 di 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Vero

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Falso

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Come sono stati generati

I fixtures utilizzano lo stesso percorso di codice del notebook, con una chiave di firma fissa
e timestamp fissi per la riproducibilità dei byte. Per rigenerarli:

```bash
python3 generate_fixtures.py
```

(Lo script si trova in `generate_fixtures.py` in questa directory.)

## Cosa imparano gli studenti ispezionando il JSON grezzo

Leggere il formato grezzo della ricevuta costruisce un'intuizione che le celle nel notebook
non sempre forniscono. Gli studenti che sfogliano il JSON spesso notano:

1. La firma è una stringa opaca base64url, ma tutti gli altri campi sono JSON
   leggibile in chiaro. La firma non cifra il contenuto; lo attesta.
2. La `public_key` è incorporata nella ricevuta. Un revisore non ha bisogno di altro
   per verificare (a patto di fidarsi che la chiave appartenga effettivamente all'emittente dichiarato;
   vedi il README della lezione sull'infrastruttura di identità).
3. Modificare un solo carattere di qualsiasi campo e poi riconsiderare questo file con
   `02_tampered_receipt.json` rende concreto il meccanismo a livello di byte.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->