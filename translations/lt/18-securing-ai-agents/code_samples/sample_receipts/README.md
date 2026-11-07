# Pavyzdinės kvitų konfigūracijos

Keturi iš anksto sugeneruoti kvitų failai peržiūrai be užrašų vykdymo.

| Failas | Kas tai yra |
|---|---|
| `01_valid_receipt.json` | Galiojantis pasirašytas kvitas už `lookup_flights` įrankio kvietimą. Tikrinimas grąžina True. |
| `02_tampered_receipt.json` | Tas pats kvitas, kurio vienas laukas pakeistas po pasirašymo. Tikrinimas grąžina False. |
| `03_chain_three_receipts.json` | Trys galiojančių kvitų grandinė (paieška, rezervacija, užsakymas) su `previous_receipt_hash`, jungiančiu kiekvieną su ankstesniu. |
| `04_resigned_receipt.json` | Tas pats kvitas, suklastotas ir vėl pasirašytas atakotojo, kuriame įterptas atakotojo viešasis raktas. Tikrina su raktu faile. Nepavyksta su išdavimo rakto tikrinimu. |

Konfigūracijos pasirašo krautojo kanoninį JCS baitų vaizdą tiesiogiai su Ed25519.
SHA-256 vis dar naudojamas turinio santraukoms ir kvitų grandinės nuorodoms, ne kaip
papildomas priešpasirašymo maišos žingsnis.

## Pavyzdžių tikrinimas

Užrašinyje `18-signed-receipts.ipynb` pirmiausia vykdykite Setup ir skirsnius 1 iki 3.
Skyrius 3 apibrėžia `verify_chain`; vien tik skyriai 1 ir 2 nepakankami.
Tada vykdykite žemiau esantį bloką naujame langelyje, užrašinio darbinę direktoriją
nustatykite į `18-securing-ai-agents/code_samples`. Konfigūracijų keliai yra santykiniai
šiame kataloge.

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

### Pavyzdžio tikrinimas be Jupyter

Iš saugyklos šakninio katalogo įdiekite pamokos priklausomybes ir paleiskite:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Šie testai vykdo užrašo Python pavyzdžius ir tiksliai aukščiau esančią README dalį.
Jie taip pat tikrina, kad klastojimas ir nevaržomi raktai būtų atmetami
tikrinimo metu. Testai praleidžia užrašo `%pip` setup langelį, nes priklausomybės
įdiegtos atskirai. Jie nekeičia užrašo ar konfigūracijų.

## Kaip tai buvo sugeneruota

Konfigūracijos naudoja tą patį kodo kelią kaip ir užrašas, su fiksuotu pasirašymo raktu
ir fiksuotais laiko žymenimis baitų atkuriamumui. Norint iš naujo sugeneruoti:

```bash
python3 generate_fixtures.py
```

(Skriptas yra `generate_fixtures.py` šiame kataloge.)

`../test_signed_receipts.py` automatiškai patikrina visa tai: vykdo
užrašo kodą, patikrina šias keturias konfigūracijas su užrašo
`verify_receipt` ir `verify_chain`, ir patvirtina, kad iš naujo generuotos
konfigūracijos turi identiškus baitus. Iš `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Ko studentai išmoksta nagrinėdami neapdorotą JSON

Skaitant neapdorotą kvito formatą atsiranda intuicija, kurios langeliai užraše
ne visada suteikia. Studentai, greitai peržvelgę JSON, dažnai pastebi:

1. Parašas yra neaiški base64url eilutė, bet visi kiti laukai yra paprastas
   skaitomas JSON. Parašas neslepia turinio; jis jį liudija.
2. `public_key` yra įterptas kvite, kas daro failą
   savarankišką, bet ne tai, ką auditorius tikrina. Palyginkite
   `02_tampered_receipt.json` su `04_resigned_receipt.json`: abu buvo
   pakeisti po pasirašymo, bet antrąjį vėl pasirašė atakotojas
   savo raktu, todėl jis tikrinamas su savo raktu. Įterptas raktas
   nurodo, kad failas yra viduje nuoseklus. Tik raktas,
   paimtas iš kitos vietos, nurodo, kas jį išdavė.
3. Pakoregavus vieną simbolį bet kuriame lauke, išskyrus `signature`,
   ir po to vėl palyginus šį failą su `02_tampered_receipt.json`,
   baitų lygmens mechanizmas tampa aiškus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->