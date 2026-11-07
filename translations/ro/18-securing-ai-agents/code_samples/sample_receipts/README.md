# Fișe de chitanțe de probă

Patru fișiere de chitanțe pre-generate pentru inspectare fără a rula caietul.

| Fișier | Ce este |
|---|---|
| `01_valid_receipt.json` | O chitanță validă semnată pentru un apel de instrument `lookup_flights`. Verificarea returnează True. |
| `02_tampered_receipt.json` | Aceeași chitanță cu un câmp modificat după semnare. Verificarea returnează False. |
| `03_chain_three_receipts.json` | Un lanț de trei chitanțe valide (search, hold, book) cu `previous_receipt_hash` care leagă fiecare de precedentă. |
| `04_resigned_receipt.json` | Aceeași chitanță manipulat și apoi re-semnată de un atacator, cu cheia publică a atacatorului inclusă. Verifică în raport cu cheia din ea. Eșuează față de cheia emițătorului. |

Fișele semnează direct octeții canonici JCS ai încărcăturii folosind Ed25519.
SHA-256 rămâne în uz pentru digesturi de conținut și linkuri în lanțul chitanțelor, nu ca un
pre-hash suplimentar înainte de semnare.

## Verificarea exemplelor

În `18-signed-receipts.ipynb`, rulează mai întâi Setup și Secțiunile 1 până la 3.
Secțiunea 3 definește `verify_chain`; doar Secțiunile 1 și 2 nu sunt suficiente.
Apoi rulează blocul următor într-o celulă nouă, cu directorul de lucru al caietului
setat la `18-securing-ai-agents/code_samples`. Căile fișierelor din fixture de mai jos sunt relative
la acel director.

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

### Verificarea exemplului fără Jupyter

Din rădăcina depozitului, instalează dependențele lecției și rulează:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Aceste teste execută exemplele Python din caiet și exact blocul README
de mai sus. De asemenea, verifică ca manipularea și cheile nefixate să fie respinse de
verificatori. Testele sar peste celula de setup `%pip` a caietului deoarece dependențele
sunt instalate separat. Nu modifică caietul sau fixture-urile.

## Cum au fost generate acestea

Fixture-urile folosesc aceeași cale de cod ca și caietul, cu o cheie fixă de semnare
și timestamp-uri fixe pentru reproducibilitate la nivel de octeți. Pentru a regenera:

```bash
python3 generate_fixtures.py
```

(Scriptul este la `generate_fixtures.py` în acest director.)

`../test_signed_receipts.py` verifică toată aceasta automat: rulează
codul caietului, verifică aceste patru fixture-uri cu
`verify_receipt` și `verify_chain` ale caietului, și confirmă că regenerarea
fixture-urilor produce exact aceiași octeți. Din `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Ce învață studenții din inspectarea JSON-ului brut

Citirea formatului brut al chitanței dezvoltă intuiția pe care celulele din caiet
nu o oferă întotdeauna. Studenții care răsfoiesc JSON-ul observă adesea:

1. Semnătura este un șir opac base64url, dar fiecare alt câmp este JSON simplu
   lizibil. Semnătura nu criptează conținutul; îl atestă.
2. `public_key` este încorporat în chitanță, ceea ce face fișierul
   auto-conținut, dar nu este ceea ce un auditor verifică. Compară
   `02_tampered_receipt.json` cu `04_resigned_receipt.json`: ambele au fost
   modificate după semnare, dar al doilea a fost re-semnate cu cheia
   atacatorului, deci verifică în raport cu cheia pe care o conține. Cheia
   încorporată arată că fișierul este intern consistent. Numai o cheie obținută
   din altă parte îți spune cine l-a emis.
3. Modificarea unui singur caracter din orice câmp în afara `signature`, apoi
   re-compararea acestui fișier cu `02_tampered_receipt.json`, face mecanismul
   la nivel de octeți concret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->