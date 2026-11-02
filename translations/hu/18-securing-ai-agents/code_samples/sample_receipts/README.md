# Minta Nyugta Fixture-ök

Három előre legenerált nyugta fájl ellenőrzéshez anélkül, hogy a jegyzetfüzetet futtatnánk.

| Fájl | Mi ez |
|---|---|
| `01_valid_receipt.json` | Egy érvényes, aláírt nyugta egy `lookup_flights` eszközhíváshoz. Az ellenőrzés True értéket ad vissza. |
| `02_tampered_receipt.json` | Ugyanaz a nyugta, egy mező módosítva az aláírás után. Az ellenőrzés False értéket ad vissza. |
| `03_chain_three_receipts.json` | Három érvényes nyugta láncolata (keresés, foglalás, könyvelés), ahol a `previous_receipt_hash` mindegyiket az előzőhöz köti. |

A fixture-ök közvetlenül az Ed25519-gyel írják alá a teherként használt kanonikus JCS bájtokat.
A SHA-256 továbbra is a tartalom hash-éhez és a nyugta lánc hivatkozásokhoz használatos, nem
pedig előkezelő hash-ként az aláírás előtt.

## Minták ellenőrzése

A jegyzetfüzet négy szekcióban vezeti végig az ellenőrzést. Ezeket a fixture-öket közvetlenül,
a jegyzetfüzet futtatása nélkül is ellenőrizhetjük:

```python
import json
from pathlib import Path

# Feltételezi, hogy befejezted az importokat és segédfunkciókat
# az 18-signed-receipts.ipynb 1. és 2. szakaszából.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Igaz

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Hamis

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Hogyan készültek ezek

A fixture-ök ugyanazt a kódutat használják, mint a jegyzetfüzet, egy fix aláíró kulccsal
és fix időbélyegekkel a bájt szintű reprodukálhatóság érdekében. Újrageneráláshoz:

```bash
python3 generate_fixtures.py
```

(A szkript a `generate_fixtures.py` fájlban található ebben a könyvtárban.)

## Mit tanulnak a hallgatók a nyers JSON átvizsgálásából

A nyers nyugta formátum olvasása olyan intuíciót épít, amit a jegyzetfüzet cellái nem mindig nyújtanak.
A JSON-t csak átfutó hallgatók gyakran észreveszik:

1. Az aláírás egy átlátszatlan base64url karakterlánc, de minden más mező egyszerű,
   olvasható JSON. Az aláírás nem titkosítja a tartalmat; hanem tanúsítja azt.
2. A `public_key` be vannak ágyazva a nyugtába. Egy ellenőrzőnek semmi mást nem kell tudnia
   az ellenőrzéshez (feltéve, hogy bízik abban, hogy a kulcs valóban a
   megnevezett kibocsátóé; lásd a lecke README-jét az identitás infrastruktúráról).
3. Bármely mező egyetlen karakterének módosítása, majd ennek az állománynak az
   összehasonlítása a `02_tampered_receipt.json`-el szemléletesen mutatja a bájt szintű mechanizmust.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->