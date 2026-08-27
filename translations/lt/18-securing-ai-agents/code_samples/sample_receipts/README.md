# Pavyzdinės kvito bylos

Trys iš anksto sugeneruotos kvito bylos patikrinimui be būtinybės vykdyti užrašų knygelę.

| Failas | Kas tai yra |
|---|---|
| `01_valid_receipt.json` | Galiojantis pasirašytas kvitas `lookup_flights` įrankio kvietimui. Patikrinimas grąžina True. |
| `02_tampered_receipt.json` | Tas pats kvitas, kuriame vienas laukas pakeistas po pasirašymo. Patikrinimas grąžina False. |
| `03_chain_three_receipts.json` | Trys galiojantys kvitai grandinėje (paieška, rezervavimas, užsakymas), kuriuos sujungia `previous_receipt_hash`. |

Šios bylos pasirašo JCS baitų kanoninį krūvį tiesiogiai su Ed25519.
SHA-256 naudojamas toliau turinio santraukoms ir kvito grandinės nuorodoms, o ne kaip
papildoma priešpasirašymo santrauka.

## Pavyzdžių tikrinimas

Užrašų knygelėje tikrinimas aptariamas keturiose dalyse. Norint patikrinti šias bylas
tiesiogiai, neperbėginėjant per užrašų knygelės naratyvą:

```python
import json
from pathlib import Path

# Daroma prielaida, kad importai ir pagalbinės funkcijos jau yra užbaigtos
# iš 1 ir 2 skyrių 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Teisinga

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Neteisinga

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kaip jos buvo sugeneruotos

Šios bylos naudoja tą pačią kodo seką kaip ir užrašų knygelė, su vienu fiksuotu pasirašymo raktu
ir fiksuotais laiko ženklais, kad būtų atkuriami tie patys baitai. Norint sugeneruoti iš naujo:

```bash
python3 generate_fixtures.py
```

(Scenarijus yra `generate_fixtures.py` šiame kataloge.)

## Ką studentai sužino nagrinėdami neapdorotą JSON

Skaitymas neapdoroto kvito formato suteikia intuiciją, kurios kartais trūksta ląstelėse užrašų knygelėje.
Studentai, greitai peržiūrintys JSON, dažnai pastebi:

1. Parašas yra nepermatomas base64url eilutė, o visi kiti laukai yra atviro
   skaitomo JSON formato. Parašas nešifruoja turinio; jis jį patvirtina.
2. `public_key` yra įterptas į kvitą. Auditorius nieko daugiau nereikia
   patikrinimui (tik reikalaujant pasitikėjimo, kad raktas tikrai priklauso nurodytam
   leidėjui; žr. pamokos README apie atpažinimo infrastruktūrą).
3. Vieno simbolio bet kuriame lauke pakeitimas ir to failo palyginimas su
   `02_tampered_receipt.json` leidžia suprasti baitų lygio mechanizmą.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->