# Minta nyugta rögzítő fájlok

Négy előre generált nyugtafájl ellenőrzéshez a jegyzetfüzet futtatása nélkül.

| Fájl | Mi ez? |
|---|---|
| `01_valid_receipt.json` | Érvényes aláírt nyugta egy `lookup_flights` eszközhívásról. Az ellenőrzés True értéket ad vissza. |
| `02_tampered_receipt.json` | Ugyanez a nyugta egy beállítás módosítása után az aláírás után. Az ellenőrzés False értéket ad vissza. |
| `03_chain_three_receipts.json` | Három érvényes átvétel (keresés, tartás, foglalás) lánca, ahol `previous_receipt_hash` összekapcsolja mindet az előzővel. |
| `04_resigned_receipt.json` | Ugyanaz az átvétel módosítva, majd egy támadó által újból aláírva, a támadó saját nyilvános kulcsával beágyazva. A benne lévő kulcs ellenőrizve van. Sikertelen a kibocsátó kulcsával szemben. |

A fixtures közvetlenül az Ed25519-gyel írják alá a terhelés kanonikus JCS bájtjait.
A SHA-256 továbbra is a tartalom digestként és az átvétel-lánc linkekhez használatos, nem egy
extra előhash aláírás előtt.

## A minták ellenőrzése

A `18-signed-receipts.ipynb`-ban először futtasd le a Setup-ot és az 1–3. szakaszokat.
A 3. szakasz definiálja a `verify_chain`-t; az 1. és 2. szakasz önmagában nem elég.
Ezután futtasd az alábbi blokkot egy új cellában, miközben a jegyzetfüzet munkakönyvtára
`18-securing-ai-agents/code_samples`-ra van állítva. Az alábbi fixtures elérési utak ehhez a könyvtárhoz viszonyítottak.


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

### Az példa Jupyter nélküli ellenőrzése

A tárhely gyökeréből telepítsd a leckefüggőségeket, majd futtasd:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ezek a tesztek lefuttatják a jegyzetfüzet Python példáit és a pontos README blokkot
fentebb. Ellenőrzik továbbá, hogy a módosításokat és a nem rögzített kulcsokat a
ellenőrzők elutasítják. A tesztek kihagyják a jegyzetfüzet `%pip` beállító celláját, mert a függőségek
külön telepítve vannak. Nem módosítják a jegyzetfüzetet vagy a fixtures-eket.

## Hogyan lettek generálva ezek

A fixtures ugyanazt a kódutat használja, mint a jegyzetfüzet, egy rögzített aláíró kulccsal
és rögzített időbélyegekkel a bájtszintű reprodukálhatóság érdekében. Újrageneráláshoz:

```bash
python3 generate_fixtures.py
```

(A script a `generate_fixtures.py` alatt található ebben a könyvtárban.)

`../test_signed_receipts.py` mindezt automatikusan ellenőrzi: lefuttatja a
jegyzetfüzet kódját, ellenőrzi ezt a négy fixture-t a jegyzetfüzet
`verify_receipt` és `verify_chain` segítségével, és megerősíti, hogy a fixtures-ek újragenerálása
azonos bájtokat eredményez. A `code_samples` szerint:

```bash
python -m unittest test_signed_receipts
```

## Amit a hallgatók megtanulnak a nyers JSON megtekintésével

A nyers átvételi formátum olvasása olyan intuíciót épít, amit a jegyzetfüzet cellái
nem mindig nyújtanak. Azok a hallgatók, akik rápillantanak a JSON-re, gyakran észreveszik:

1. Az aláírás egy átlátszatlan base64url karakterlánc, de minden más mező egyszerű,
   olvasható JSON. Az aláírás nem titkosítja a tartalmat; igazolja azt.
2. Az `public_key` be van ágyazva az átvételbe, ami önállóvá teszi a fájlt,
   de nem az, amit egy ellenőr igazol. Hasonlítsd össze
   `02_tampered_receipt.json`-t `04_resigned_receipt.json`-tel: mindkettő
   aláírás után módosítva lett, de a másodikat a támadó
   saját kulcsával újra aláírták, így az az átvételben található kulccsal hitelesíthető.
   A beágyazott kulcs belső konzisztenciát jelez. Csak egy külsőleg
   megszerzett kulcs árulja el, ki bocsátotta ki.
3. Egyetlen karakter módosítása a `signature`-on kívüli bármely mezőben, majd
   ennek a fájlnak az újrakomparálása `02_tampered_receipt.json`-vel a
   bájtszintű mechanizmust konkréttá teszi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->