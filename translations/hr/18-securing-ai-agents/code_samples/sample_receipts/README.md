# Primjeri računa

Tri unaprijed generirane datoteke računa za pregled bez pokretanja bilježnice.

| Datoteka | Što je to |
|---|---|
| `01_valid_receipt.json` | Važeći potpisani račun za poziv alata `lookup_flights`. Verifikacija vraća True. |
| `02_tampered_receipt.json` | Isti račun s jednom izmijenjenom stavkom nakon potpisivanja. Verifikacija vraća False. |
| `03_chain_three_receipts.json` | Lanac od tri važeća računa (pretraživanje, rezervacija, potvrda) s `previous_receipt_hash` koji povezuje svaki s prethodnim. |

Primjeri izravno potpisuju kanonske JCS bajtove tereta s Ed25519.
SHA-256 se i dalje koristi za sažetke sadržaja i veze lanca računa, ne kao
dodatni pred-hash prije potpisivanja.

## Verifikacija primjera

Bilježnica prolazi kroz verifikaciju u četiri dijela. Za izravnu provjeru ovih primjera
bez prolaska kroz narativ bilježnice:

```python
import json
from pathlib import Path

# Pretpostavlja se da ste završili uvoze i pomoćne funkcije
# iz odjeljaka 1 i 2 datoteke 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Točno

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Netočno

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kako su generirani

Primjeri koriste isti kodni put kao bilježnica, s jednim fiksnim ključem za potpis
i fiksnim vremenskim oznakama radi ponovljivosti bajtova. Za ponovnu generaciju:

```bash
python3 generate_fixtures.py
```

(Skripta se nalazi u `generate_fixtures.py` u ovom direktoriju.)

## Što studenti nauče pregledom sirovog JSON-a

Čitanje sirovog formata računa gradi intuitivno razumijevanje koje stanice u bilježnici
ne uvijek pružaju. Studenti koji brzo pregledaju JSON često primijete:

1. Potpis je neprozirni base64url niz, ali svaki drugi element je običan
   čitljiv JSON. Potpis ne šifrira sadržaj; on ga potvrđuje.
2. `public_key` je ugrađen u račun. Revizor ne treba ništa drugo
   za verifikaciju (pod uvjetom da vjeruje da ključ stvarno pripada navedenom
   izdavaču; vidi README lekcije o infrastrukturi identiteta).
3. Promjena jednog znaka bilo kojeg polja, a zatim usporedba s
   `02_tampered_receipt.json`, čini mehanizam na razini bajtova opipljivim.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->