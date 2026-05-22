# Mostre de chitanțe

Trei fișiere de chitanțe pre-generate pentru inspectare fără a rula notebook-ul.

| Fișier | Ce este |
|---|---|
| `01_valid_receipt.json` | O chitanță validă semnată pentru un apel la instrumentul `lookup_flights`. Verificarea returnează True. |
| `02_tampered_receipt.json` | Aceeași chitanță cu un câmp modificat după semnare. Verificarea returnează False. |
| `03_chain_three_receipts.json` | Un lanț de trei chitanțe valide (căutare, rezervare temporară, rezervare finală) cu `previous_receipt_hash` care leagă fiecare de precedentă. |

## Verificarea mostrelor

Notebook-ul parcurge verificarea în patru secțiuni. Pentru a verifica aceste mostre direct fără a parcurge narațiunea notebook-ului:

```python
import json
from pathlib import Path

# Presupuneți că ați finalizat importurile și funcțiile ajutătoare
# din secțiunile 1 și 2 ale fișierului 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Adevărat

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Fals

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Cum au fost generate acestea

Mostrele folosesc aceeași cale de cod ca și notebook-ul, cu o cheie de semnare fixă
și timpi fixați pentru reproducibilitate la nivel de octeți. Pentru a regenera:

```bash
python3 generate_fixtures.py
```

(Scriptul este în `generate_fixtures.py` în acest director.)

## Ce învață studenții din inspectarea JSON-ului brut

Citind formatul brut al chitanței se construiește o intuiție pe care celulele din notebook
nu o oferă întotdeauna. Studenții care parcurg JSON-ul observă adesea:

1. Semnătura este un șir opac în base64url, dar toate celelalte câmpuri sunt în JSON simplu
   lizibil. Semnătura nu criptează conținutul; aceasta îl atestă.
2. `public_key` este inclusă în chitanță. Un auditor nu are nevoie de altceva
   pentru a verifica (sub rezerva încrederii că cheia aparține într-adevăr emitentului reclamat; vezi README-ul lecției despre infrastructura de identitate).
3. Modificarea unui singur caracter din orice câmp, apoi compararea din nou a acestui fișier cu
   `02_tampered_receipt.json`, face mecanismul la nivel de octeți concret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->