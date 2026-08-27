# Minta blokknyugták

Három előre generált blokknyugta fájl ellenőrzéshez a notebook futtatása nélkül.

| Fájl | Mit tartalmaz |
|---|---|
| `01_valid_receipt.json` | Egy érvényes, aláírt blokknyugta egy `lookup_flights` eszköz híváshoz. Az ellenőrzés True értéket ad vissza. |
| `02_tampered_receipt.json` | Ugyanaz a blokknyugta, amelyben egy mező módosítva lett az aláírás után. Az ellenőrzés False értéket ad vissza. |
| `03_chain_three_receipts.json` | Három érvényes blokknyugta láncolata (keresés, foglalás, lefoglalás) `previous_receipt_hash` mezővel, amely összekapcsolja őket egymással. |

A minták a terhelés kanonikus JCS byte-jait közvetlenül az Ed25519-gyel írják alá.
A SHA-256 továbbra is a tartalomösszefoglalókhoz és a blokknyugtalánc linkekhez használatos, nem pedig
külön előfeldolgozásként az aláírás előtt.

## A minták ellenőrzése

A notebook négy részben halad az ellenőrzésen keresztül. Ezeknek a mintáknak 
az ellenőrzéséhez közvetlenül, a notebook narratíva futtatása nélkül:

```python
import json
from pathlib import Path

# Feltételezi, hogy befejezted az importokat és a segédfunkciókat
# az 18-signed-receipts.ipynb 1-es és 2-es szakaszából.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Igaz

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Hamis

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Hogyan készültek ezek

A minták ugyanazt a kódfolyamatot használják, mint a notebook, egy fix aláíró kulccsal
és fix időbélyegekkel a byte-reprodukálhatóság érdekében. Újrageneráláshoz:

```bash
python3 generate_fixtures.py
```

(A szkript a `generate_fixtures.py` fájlban található ebben a könyvtárban.)

## Mit tanulnak a hallgatók a nyers JSON megtekintéséből

A nyers blokknyugta formátum olvasása olyan intuíciót épít, amit a notebook cellák nem
mindig nyújtanak. A hallgatók, akik átlapozzák a JSON-t, gyakran észreveszik:

1. Az aláírás egy átlátszatlan base64url karakterlánc, de minden más mező egyszerű,
   olvasható JSON. Az aláírás nem titkosítja a tartalmat; annak hitelesítésére szolgál.
2. A `public_key` beágyazva van a blokknyugtában. Egy ellenőrnek nincs szüksége másra
   az ellenőrzéshez (feltéve, hogy bízik abban, hogy a kulcs valóban a kijelölt
   kibocsátóhoz tartozik; lásd a tananyag README fájlját az identitás infrastruktúráról).
3. Bármely mező egyetlen karakterének megváltoztatása, majd ennek a fájlnak az összehasonlítása az
   `02_tampered_receipt.json` fájllal konkrétan bemutatja a byte-szintű mechanizmust.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->