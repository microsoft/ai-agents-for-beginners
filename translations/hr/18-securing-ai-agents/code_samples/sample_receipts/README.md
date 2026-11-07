# Primjeri računa (Receipt Fixtures)

Četiri unaprijed generirane datoteke računa za pregled bez pokretanja bilježnice.

| Datoteka | Što je to |
|---|---|
| `01_valid_receipt.json` | Valjani potpisani račun za poziv alata `lookup_flights`. Verifikacija vraća True. |
| `02_tampered_receipt.json` | Isti račun s jednim izmijenjenim poljem nakon potpisivanja. Verifikacija vraća False. |
| `03_chain_three_receipts.json` | Lanac od tri valjana računa (search, hold, book) s `previous_receipt_hash` koji povezuje svaki s prethodnim. |
| `04_resigned_receipt.json` | Isti račun izmijenjen, a zatim ponovo potpisan od strane napadača, s javnim ključem napadača ugrađenim u njega. Verificira se prema ključu unutar njega. Ne uspijeva prema ključu izdavatelja. |

Primjeri direktno potpisuju kanonske JCS bajtove sadržaja s Ed25519.
SHA-256 ostaje u upotrebi za sažetke sadržaja i veze lanaca računa, ne kao
dodatni predsažetak prije potpisivanja.

## Verifikacija primjera

U `18-signed-receipts.ipynb` najprije pokrenite Setup i Sekcije 1 do 3.
Sekcija 3 definira `verify_chain`; samotne Sekcije 1 i 2 nisu dovoljne.
Zatim pokrenite sljedeći blok u novoj ćeliji, s radnim direktorijem bilježnice
postavljenim na `18-securing-ai-agents/code_samples`. Putanje primjera u nastavku su relativne
prema tom direktoriju.

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

### Provjera primjera bez Jupyter-a

Iz korijena repozitorija instalirajte ovisnosti lekcije i pokrenite:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ovi testovi izvršavaju Python primjere iz bilježnice i točan README blok
gore. Također provjeravaju da se izmjene i nepotpisani ključevi odbacuju od strane
verifikatora. Testovi preskaču ćeliju za postavljanje `%pip` jer se ovisnosti
instaliraju zasebno. Ne mijenjaju bilježnicu ni primjere.

## Kako su generirani

Primjeri koriste isti kod kao i bilježnica, s jednim fiksnim potpisnim ključem
i fiksnim vremenskim oznakama radi višekratne reproducibilnosti bajtova. Za ponovnu generaciju:

```bash
python3 generate_fixtures.py
```

(Skripta se nalazi na `generate_fixtures.py` u ovom direktoriju.)

`../test_signed_receipts.py` automatski provjerava sve ovo: izvršava
kod bilježnice, verificira ove četiri primjere s bilježničkim
`verify_receipt` i `verify_chain`, i potvrđuje da ponovna generacija
primjera daje identične bajtove. Iz `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Što studenti nauče pregledom sirovog JSON-a

Čitanje sirovog formata računa razvija intuiciju koju ćelije u bilježnici
ne pružaju uvijek. Studenti koji pregledaju JSON često primijete:

1. Potpis je neproziran base64url niz, ali svako drugo polje je čitljiv
   običan JSON. Potpis ne šifrira sadržaj; potvrđuje ga.
2. `public_key` je ugrađen u račun, što čini datoteku
   samodostatnom, ali nije ono što revizor verificira. Usporedite
   `02_tampered_receipt.json` s `04_resigned_receipt.json`: oba su
   izmijenjena nakon potpisivanja, ali drugi je ponovno potpisan s napadačevim
   vlastitim ključem, pa se verificira prema ključeu koji sadrži. Ugrađeni ključ
   govori vam da je datoteka interna dosljedna. Samo ključ dobiven
   negdje drugdje govori tko ju je izdao.
3. Izmjena jednog znaka bilo kojeg polja izvan `signature`, zatim
   usporedba ove datoteke s `02_tampered_receipt.json`, konkretizira
   mehanizam na razini bajtova.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->