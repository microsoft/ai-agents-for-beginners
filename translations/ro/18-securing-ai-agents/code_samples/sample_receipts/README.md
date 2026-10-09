# Exemple de chitanțe

Trei fişiere de chitanțe pre-generate pentru inspecție fără a rula notebook-ul.

| Fișier | Ce este |
|---|---|
| `01_valid_receipt.json` | O chitanță validă semnată pentru un apel al instrumentului `lookup_flights`. Verificarea returnează True. |
| `02_tampered_receipt.json` | Aceeași chitanță cu un câmp modificat după semnare. Verificarea returnează False. |
| `03_chain_three_receipts.json` | Un lanț de trei chitanțe valide (căutare, rezervare temporară, rezervare finală) cu `previous_receipt_hash` care le leagă pe fiecare de cea anterioară. |

Exemplele semnează direct octeții canonici JCS ai conținutului cu Ed25519.
SHA-256 rămâne folosit pentru digesturile de conținut și legăturile lanțului de chitanțe, nu ca un
pre-hash suplimentar înainte de semnare.

## Verificarea exemplelor

Notebook-ul parcurge verificarea în patru secțiuni. Pentru a verifica aceste exemple
direct, fără a parcurge explicația din notebook:

```python
import json
from pathlib import Path

# Presupune că ați finalizat importurile și funcțiile auxiliare
# din secțiunile 1 și 2 ale fișierului 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Adevărat

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Fals

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Cum au fost generate

Exemplele folosesc aceeași cale de cod ca notebook-ul, cu o cheie de semnare fixă
și timpi fixați pentru a avea reproducibilitate byte cu byte. Pentru a regenera:

```bash
python3 generate_fixtures.py
```

(Scriptul este în `generate_fixtures.py` în acest director.)

## Ce învață studenții din inspectarea JSON-ului brut

Citirea formatului brut al chitanței construiește o intuiție pe care celulele din notebook
nu o oferă întotdeauna. Studenții care parcurg rapid JSON-ul observă adesea:

1. Semnătura este un șir opac base64url, dar fiecare alt câmp este JSON simplu
   lizibil. Semnătura nu criptează conținutul; îl atestă.
2. `public_key` este încorporată în chitanță. Un auditor nu are nevoie de altceva
   pentru a verifica (sub rezerva de a avea încredere că cheia aparține efectiv emitentului
   declarat; vezi README-ul lecției despre infrastructura de identitate).
3. Modificarea unui singur caracter în orice câmp și apoi compararea cu
   `02_tampered_receipt.json` face mecanismul la nivel de octeți concret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->