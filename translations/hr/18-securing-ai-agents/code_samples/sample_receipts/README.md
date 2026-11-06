# Primjer datoteka računa

Tri unaprijed generirane datoteke računa za pregled bez pokretanja bilježnice.

| Datoteka | Što je to |
|---|---|
| `01_valid_receipt.json` | Važeći potpisani račun za poziv alata `lookup_flights`. Verifikacija vraća True. |
| `02_tampered_receipt.json` | Isti račun s jednim poljem izmijenjenim nakon potpisivanja. Verifikacija vraća False. |
| `03_chain_three_receipts.json` | Lanac od tri važeća računa (search, hold, book) s `previous_receipt_hash` koji povezuje svaki s prethodnim. |

Datoteke izravno potpisuju kanonske JCS bajtove sadržaja s Ed25519.
SHA-256 ostaje u uporabi za sažetke sadržaja i veze u lancu računa, ne kao
dodatni pre-hash prije potpisivanja.

## Verifikacija primjera

U `18-signed-receipts.ipynb` prvo pokrenite Setup i Sekcije 1 do 3.
Sekcija 3 definira `verify_chain`; same Sekcije 1 i 2 nisu dovoljne.
Zatim pokrenite sljedeći blok u novoj ćeliji, s radnim direktorijem bilježnice
postavljenim na `18-securing-ai-agents/code_samples`. Donje staze do datoteka su relativne
na taj direktorij.

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

### Provjera primjera bez Jupyter-a

Iz korijena spremišta instalirajte ovisnosti lekcije i pokrenite:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ovi testovi izvršavaju Python primjere iz bilježnice i točan README blok
iznad. Također provjeravaju da verifikatori odbijaju manipulacije i neprikvačene ključeve.
Testovi zaobilaze setup ćeliju `%pip` bilježnice jer su ovisnosti
instalirane zasebno. Oni ne mijenjaju bilježnicu ni datoteke.

## Kako su ove datoteke generirane

Datoteke koriste isti kod kao bilježnica, s jednim fiksnim ključem za potpisivanje
i fiksnim vremenskim oznakama radi reproduktivnosti bajtova. Za regeneraciju:

```bash
python3 generate_fixtures.py
```

(Skript se nalazi u `generate_fixtures.py` u ovom direktoriju.)

## Što studenti uče pregledom sirovog JSON-a

Čitanje sirovog formata računa gradi intuiciju koju ćelije u bilježnici
ne pružaju uvijek. Studenti koji prelete JSON često primijete:

1. Potpis je neprozirni base64url niz, ali svako drugo polje je čisti
   čitljivi JSON. Potpis ne šifrira sadržaj; on potvrđuje.
2. `public_key` je ugrađen u račun, što je dovoljno za provjeru
   samodosljednosti, ali ne i povjerenja izdavatelja. Revizor mora usporediti s ključem
   pričvršćenim izvan računa ili riješenim putem pouzdanog registra.
3. Izmjena jednoga znaka bilo kojeg polja, pa ponovno uspoređivanje ove datoteke s
   `02_tampered_receipt.json`, konkretizira mehanizam na razini bajtova.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->