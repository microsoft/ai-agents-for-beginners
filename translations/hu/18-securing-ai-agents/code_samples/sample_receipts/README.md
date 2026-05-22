# Minta blokkok nyugtákhoz

Három előre legenerált nyugta fájl ellenőrzéshez a jegyzetfüzet futtatása nélkül.

| Fájl | Mi ez? |
|---|---|
| `01_valid_receipt.json` | Egy érvényes aláírt nyugta a `lookup_flights` eszköz híváshoz. Az ellenőrzés True értéket ad vissza. |
| `02_tampered_receipt.json` | Ugyanaz a nyugta, egy mező módosítása után aláíráskor. Az ellenőrzés False-t ad vissza. |
| `03_chain_three_receipts.json` | Három érvényes nyugta láncolata (keresés, foglalás, könyvelés), melyek `previous_receipt_hash`-szal egymáshoz vannak kötve. |

## A minták ellenőrzése

A jegyzetfüzet négy részben vezeti végig az ellenőrzést. Ha azokat a blokkokat közvetlenül szeretnénk ellenőrizni a jegyzetfüzet magyarázatának futtatása nélkül:

```python
import json
from pathlib import Path

# Feltételezi, hogy befejezte az importokat és segédfunkciókat
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

A minták ugyanazon a kódúton haladnak, mint a jegyzetfüzet, egy fix aláírási kulccsal
és fix időbélyegekkel a bájt-reprodukálhatóságért. A regeneráláshoz:

```bash
python3 generate_fixtures.py
```

(A szkript a `generate_fixtures.py` ebben a könyvtárban.)

## Mit tanulnak a diákok az alap JSON átnézéséből

Az alap nyugta formátum olvasása segíti az intuíció kiépítését, amit a jegyzetfüzet cellái nem mindig adnak meg. A JSON-t átnéző diákok gyakran észreveszik:

1. Az aláírás egy átlátszatlan base64url karakterlánc, de a többi mező sima, olvasható JSON. Az aláírás nem titkosítja a tartalmat; csak igazolja azt.
2. A `public_key` be van ágyazva a nyugtába. Egy ellenőrnek nincs szüksége másra az ellenőrzéshez (feltéve, hogy megbízik abban, hogy a kulcs valóban a kijelölt kibocsátóhoz tartozik; lásd a tananyag README-jét az identitás-infrastruktúráról).
3. Egyetlen karakter módosítása bármelyik mezőben, majd a fájl újraösszehasonlítása a `02_tampered_receipt.json`-nel, kézzelfoghatóvá teszi a bájtszintű mechanizmust.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->