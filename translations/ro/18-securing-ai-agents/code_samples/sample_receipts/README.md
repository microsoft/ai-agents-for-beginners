# Fișe de chitanțe de exemplu

Trei fișiere de chitanțe pre-generate pentru inspectare fără a rula caietul.

| Fișier | Ce este |
|---|---|
| `01_valid_receipt.json` | O chitanță semnată validă pentru un apel `lookup_flights` al uneltei. Verificarea returnează True. |
| `02_tampered_receipt.json` | Aceeași chitanță cu un câmp modificat după semnare. Verificarea returnează False. |
| `03_chain_three_receipts.json` | Un lanț de trei chitanțe valide (search, hold, book) cu `previous_receipt_hash` care leagă fiecare de precedentă. |

Fixture-urile semnează direct bytes JCS canonice ale payload-ului cu Ed25519.
SHA-256 rămâne folosit pentru digesturile conținutului și linkurile lanțului de chitanțe, nu ca un
pre-hash suplimentar înainte de semnare.

## Verificarea exemplarelor

În `18-signed-receipts.ipynb`, rulează mai întâi Setup și Secțiunile 1 până la 3.
Secțiunea 3 definește `verify_chain`; doar Secțiunile 1 și 2 nu sunt suficiente.
Apoi rulează blocul următor într-o celulă nouă, cu directorul de lucru al caietului
setat la `18-securing-ai-agents/code_samples`. Căile fișierelor fixture de mai jos sunt relative
la acest director.

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

### Verificarea exemplului fără Jupyter

Din rădăcina depozitului, instalează dependențele lecției și rulează:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Aceste teste execută exemplele Python din caiet și același bloc exact din README-ul
de mai sus. De asemenea, verifică că modificările neautorizate și cheile nefixate sunt respinse de
verificatori. Testele sar peste celula setup `%pip` a caietului deoarece dependențele
sunt instalate separat. Nu modifică caietul sau fixture-urile.

## Cum au fost generate acestea

Fixture-urile folosesc aceeași cale de cod ca și caietul, cu o cheie fixă de semnare
și timpi fixați pentru reproducibilitatea la nivel de bytes. Pentru a regenera:

```bash
python3 generate_fixtures.py
```

(Scriptul este la `generate_fixtures.py` în acest director.)

## Ce învață studenții din inspectarea JSON-ului brut

Citirea formatului brut al chitanței dezvoltă intuiția pe care celulele din caiet
nu o oferă întotdeauna. Studenții care parcurg rapid JSON-ul observă adesea:

1. Semnătura este un șir opac base64url, dar fiecare alt câmp este JSON simplu și
   citibil. Semnătura nu criptează conținutul; o atestă.
2. `public_key` este încorporat în chitanță, ceea ce este suficient pentru verificarea
   auto-consistenței, dar nu și pentru încrederea în emitent. Un auditor trebuie să îl compare cu o cheie
   fixată în afara chitanței sau rezolvată printr-un registru de încredere.
3. Modificarea unui singur caracter din orice câmp, apoi re-compararea acestui fișier cu
   `02_tampered_receipt.json` face mecanismul la nivel de bytes concret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->