# Pavyzdinės kvitų bylos

Trys iš anksto sugeneruoti kvito failai patikrinimui be užrašų knygelės paleidimo.

| Failas | Kas tai yra |
|---|---|
| `01_valid_receipt.json` | Teisingas pasirašytas kvitas `lookup_flights` įrankio kvietimui. Patikrinimas grąžina True. |
| `02_tampered_receipt.json` | Tas pats kvitas, kuriame po pasirašymo pakeistas vienas laukas. Patikrinimas grąžina False. |
| `03_chain_three_receipts.json` | Trijų galiojančių kvitų grandinė (paieška, rezervacija, užsakymas) su `previous_receipt_hash`, jungiančiu kiekvieną su ankstesniu. |

## Pavyzdžių tikrinimas

Užrašų knyga žingsnis po žingsnio paaiškina tikrinimą keturiose dalyse. Norint tiesiogiai patikrinti šiuos pavyzdžius be užrašų knygos pasakojimo:

```python
import json
from pathlib import Path

# Daroma prielaida, kad importai ir pagalbinės funkcijos jau atliktos
# iš 18-signed-receipts.ipynb 1 ir 2 skyrių.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Tiesa

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Klaidinga

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kaip jie buvo sugeneruoti

Šie pavyzdžiai naudoja tą pačią kodo eigą kaip užrašų knyga, tik su viena fiksuota pasirašymo raktu
ir fiksuotais laiko žymėmis, užtikrinant baitų atkuriamumą. Norint sugeneruoti iš naujo:

```bash
python3 generate_fixtures.py
```

(Skriptas yra `generate_fixtures.py` šiame kataloge.)

## Ko studentai išmoksta nagrinėdami neapdorotą JSON

Skaitant neapdorotą kvito formatą, kyla intuicija, kurios užrašų knygos ląstelės ne visada suteikia. Studentai, kurie peržiūri JSON, dažnai pastebi:

1. Parašas yra nepralaidus base64url eilutė, tačiau visi kiti laukai yra aiškiai skaitomas JSON. Parašas nešifruoja turinio; jis patvirtina turinį.
2. `public_key` yra įterptas kvite. Auditorius nieko kito nereikia patikrinimui (atsižvelgiant į pasitikėjimą, kad raktas iš tikrųjų priklauso tvirtinamajam leidėjui; žr. pamokos README apie tapatybės infrastruktūrą).
3. Pakeitus vieną simbolį bet kuriame lauke ir palyginus šį failą su `02_tampered_receipt.json`, baitų lygio mechanizmas tampa aiškus ir konkrečiai suvokiamas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->