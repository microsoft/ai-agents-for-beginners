# Minta nyugta minták

Három előre generált nyugtafájl megtekintéshez anélkül, hogy futtatnánk a jegyzetfüzetet.

| Fájl | Leírás |
|---|---|
| `01_valid_receipt.json` | Egy érvényes, aláírt nyugta egy `lookup_flights` eszközhíváshoz. Az ellenőrzés True értéket ad. |
| `02_tampered_receipt.json` | Ugyanaz a nyugta, egy mező módosításával az aláírás után. Az ellenőrzés False értéket ad. |
| `03_chain_three_receipts.json` | Három érvényes nyugta láncolata (keresés, tartás, foglalás), ahol `previous_receipt_hash` az előzőhöz köti mindegyiket. |

A minták az adatköteg kanonikus JCS byte-jait közvetlenül Ed25519-gyel írják alá.
A SHA-256 továbbra is használatban marad tartalmi összefoglalókhoz és nyugta-lánc kapcsolatokhoz, nem pedig
előzetes hash-ként az aláírás előtt.

## A minták ellenőrzése

A `18-signed-receipts.ipynb` futtatásakor először a Setupot és az 1–3. szakaszokat futtasd le.
A 3. szakasz definiálja a `verify_chain`-t; az 1. és 2. szakasz önmagában nem elégséges.
Ezután futtass egy új cellában a következő blokkot, a jegyzetfüzet munkakönyvtárát
beállítva `18-securing-ai-agents/code_samples`-re. Az alábbi minták elérési útjai relatívak
ehhez a könyvtárhoz.

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

### A példa ellenőrzése Jupyter nélkül

A tároló gyökeréből telepítsd a tananyag függőségeit és futtasd:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ezek a tesztek lefuttatják a jegyzetfüzet Python példáit és a pontos README blokkot
fent. Ellenőrzik azt is, hogy a hamisítás és a nem rögzített kulcsok visszautasításra kerülnek
az ellenőrzők által. A tesztek kihagyják a jegyzetfüzet `%pip` beállító celláját, mivel a függőségek
külön telepítve vannak. Nem változtatják meg a jegyzetfüzetet vagy a mintákat.

## Hogyan készültek ezek

A minták ugyanazt a kódfutatást használják, mint a jegyzetfüzet, egy rögzített aláíró kulccsal
és rögzített időbélyegekkel a byte-reprodukálhatóság érdekében. Az újrageneráláshoz:

```bash
python3 generate_fixtures.py
```

(A szkript a `generate_fixtures.py` alatt található ebben a könyvtárban.)

## Mit tanulnak a hallgatók a nyers JSON megtekintéséből

A nyers nyugta formátum olvasása olyan intuíciót épít, amit a jegyzetfüzet cellái
nem mindig nyújtanak. A JSON-ben böngésző hallgatók gyakran észreveszik:

1. Az aláírás egy átlátszatlan base64url karakterlánc, de minden más mező egyszerű,
   olvasható JSON. Az aláírás nem titkosítja a tartalmat; igazolja azt.
2. A `public_key` be van ágyazva a nyugtába, amely elegendő
   önkonzisztencia ellenőrzésére, de nem az kibocsátói bizalomra. Egy ellenőrnek össze kell hasonlítania azt
   egy a nyugtán kívül rögzített kulccsal vagy egy megbízható nyilvántartáson keresztül feloldott kulccsal.
3. Egyetlen mező egyetlen karakterének módosítása, majd ennek a fájlnak
   az újra összehasonlítása `02_tampered_receipt.json`-vel, kézzelfoghatóvá teszi a byte-szintű mechanizmust.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->