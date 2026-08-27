# Primjeri računa

Tri unaprijed generirane datoteke računa za pregled bez pokretanja bilježnice.

| Datoteka | Što je to |
|---|---|
| `01_valid_receipt.json` | Važeći potpisani račun za poziv alata `lookup_flights`. Verifikacija vraća True. |
| `02_tampered_receipt.json` | Isti račun s modificiranim jednim poljem nakon potpisivanja. Verifikacija vraća False. |
| `03_chain_three_receipts.json` | Lanac od tri valjana računa (pretraživanje, zadržavanje, rezervacija) s `previous_receipt_hash` povezujući svaki s prethodnim. |

Primjeri potpisuju kanonične JCS bajtove sadržaja izravno pomoću Ed25519.
SHA-256 se i dalje koristi za sažetke sadržaja i poveznice lanaca računa, ne kao
dodatni pred-sažetak prije potpisivanja.

## Verifikacija primjera

Bilježnica objašnjava verifikaciju u četiri dijela. Za direktnu verifikaciju ovih primjera
bez pokretanja bilježnice:

```python
import json
from pathlib import Path

# Pretpostavlja se da ste dovršili uvoze i pomoćne funkcije
# iz odjela 1 i 2 datoteke 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Točno

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Netočno

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kako su generirani

Primjeri koriste isti kôd kao bilježnica, s jednim fiksnim potpisnim ključem
i fiksnim vremenskim oznakama radi reproducibilnosti bajtova. Za ponovnu generaciju:

```bash
python3 generate_fixtures.py
```

(Skript se nalazi u `generate_fixtures.py` u ovom direktoriju.)

## Što studenti uče pregledavajući sirovi JSON

Čitanje sirovog formata računa gradi intuiciju koju ćelije u bilježnici
ne daju uvijek. Studenti koji pregledavaju JSON često primijete:

1. Potpis je neproziran base64url niz, ali svako drugo polje je običan
   čitljiv JSON. Potpis ne šifrira sadržaj; potvrđuje ga.
2. `public_key` je ugrađen u račun. Revizor ne treba ništa drugo
   za verifikaciju (osim uvjerenja da ključ zapravo pripada navedenom
   izdavaču; vidi README lekcije o infrastrukturi identiteta).
3. Modifikacija jednog znaka bilo kojeg polja, pa ponovno uspoređivanje ove datoteke s
   `02_tampered_receipt.json`, konkretizira mehanizam na razini bajtova.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->