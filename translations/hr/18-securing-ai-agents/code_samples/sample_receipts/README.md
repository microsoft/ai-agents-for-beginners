# Uzorci priznatnica

Tri unaprijed generirane datoteke priznatnica za pregled bez pokretanja bilježnice.

| Datoteka | Što je to |
|---|---|
| `01_valid_receipt.json` | Valjana potpisana priznatnica za poziv alata `lookup_flights`. Verifikacija vraća True. |
| `02_tampered_receipt.json` | Ista priznatnica s jednim poljem izmijenjenim nakon potpisivanja. Verifikacija vraća False. |
| `03_chain_three_receipts.json` | Lanac od tri valjane priznatnice (pretraživanje, zadržavanje, rezervacija) s `previous_receipt_hash` koji povezuje svaki s prethodnim. |

## Verifikacija uzoraka

Bilježnica prolazi kroz verifikaciju u četiri dijela. Za izravnu verifikaciju ovih uzoraka
bez prolaska kroz naraciju bilježnice:

```python
import json
from pathlib import Path

# Pretpostavlja se da ste završili uvoze i pomoćne funkcije
# iz odjeljaka 1 i 2 datoteke 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Istina

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Netočno

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kako su ove priznatnice generirane

Uzorci koriste isti kodni put kao bilježnica, s jednim fiksnim ključem za potpisivanje
i fiksnim vremenskim oznakama za reproducibilnost u bajtovima. Za ponovnu generaciju:

```bash
python3 generate_fixtures.py
```

(Skripta je u `generate_fixtures.py` u ovom direktoriju.)

## Što studenti uče pregledavanjem sirovog JSON-a

Čitanje sirovog formata priznatnica gradi intuiciju koju ćelije u bilježnici
ne uvijek pružaju. Studenti koji površno pregledavaju JSON često primijete:

1. Potpis je neproziran base64url niz, ali svaki drugi podatak je običan,
   čitljiv JSON. Potpis ne šifrira sadržaj; on ga potvrđuje.
2. `public_key` je ugrađen u priznatnicu. Revizor ne treba ništa drugo
   za verifikaciju (uz pretpostavku da je ključ stvarno u vlasništvu navedenog
   izdavatelja; vidi README lekcije o infrastrukturi identiteta).
3. Izmjena jednog znaka u bilo kojem polju, a zatim usporedba ove datoteke s
   `02_tampered_receipt.json`, čini mehanizam na razini bajtova konkretnim.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->