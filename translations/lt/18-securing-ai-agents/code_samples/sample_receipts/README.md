# Pavyzdinės kvitų fixtūros

Trys iš anksto sugeneruoti kvitų failai peržiūrai be užrašų knygelės vykdymo.

| Failas | Kas tai yra |
|---|---|
| `01_valid_receipt.json` | Galiojantis pasirašytas kvitas `lookup_flights` įrankio skambučiui. Patikrinimas grąžina True. |
| `02_tampered_receipt.json` | Tas pats kvitas su vienu lauku pakeistu po pasirašymo. Patikrinimas grąžina False. |
| `03_chain_three_receipts.json` | Trys galiojantys kvitai grandinėje (paieška, rezervavimas, užsakymas) su `previous_receipt_hash`, susiedami kiekvieną su ankstesniu. |

Fixtūros pasirašo apkrovos kanoniniais JCS baitais tiesiogiai su Ed25519.
SHA-256 vis dar naudojamas turinio santrumpoms ir kvitų grandinės nuorodoms, o ne kaip
papildomas išankstinis maišas prieš pasirašymą.

## Pavyzdžių patikra

Užrašų knyga peržiūri patikrą keturiose dalyse. Norint patikrinti šias fixtūras
tiesiogiai be užrašų knygos vykdymo:

```python
import json
from pathlib import Path

# Tarkime, kad jūs užbaigėte importavimus ir pagalbines funkcijas
# iš 1 ir 2 skirsnių failo 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Tiesa

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Melas

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kaip šios buvo sugeneruotos

Fixtūros naudoja tą pačią kodo eilutę kaip užrašų knyga, su viena fiksuota pasirašymo raktą
ir fiksuotais laiko ženklais baitų atkuriamumui. Norint sugeneruoti iš naujo:

```bash
python3 generate_fixtures.py
```

(Scenarijus yra `generate_fixtures.py` šiame kataloge.)

## Ką studentai sužino nagrinėdami neapdorotą JSON

Skaitant neapdorotą kvito formatą vystosi intuicija, kurios ląstelės užrašų knygoje
ne visada pateikia. Studentai, kurie greitai peržiūri JSON, dažnai pastebi:

1. Parašas yra neaiškus base64url eilutė, bet kiekvienas kitas laukas yra paprastas
   skaitomas JSON. Parašas nekoduoja turinio; jis liudija jo tikrumą.
2. `public_key` yra įterptas į kvitą. Auditorius nieko daugiau
   nereikia patikrinti (tik jei tiki, kad raktas iš tiesų priklauso tvirtinamu
   leidėju; žr. pamokos README apie tapatybės infrastruktūrą).
3. Vieno simbolio bet kuriame lauke pakeitimas, o paskui failo palyginimas su
   `02_tampered_receipt.json`, paverčia baitų lygio mechanizmą akivaizdžiu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->