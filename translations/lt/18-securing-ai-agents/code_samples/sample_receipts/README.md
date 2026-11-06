# Pavyzdiniai kvito šablonai

Trys iš anksto sugeneruoti kvito failai, skirti peržiūrai be užrašų vykdymo.

| Failas | Kas tai yra |
|---|---|
| `01_valid_receipt.json` | Galiojantis pasirašytas kvitas už `lookup_flights` įrankio kvietimą. Patvirtinimas grąžina True. |
| `02_tampered_receipt.json` | Tas pats kvitas, kurio vienas laukas pakeistas po pasirašymo. Patvirtinimas grąžina False. |
| `03_chain_three_receipts.json` | Trijų galiojančių kvitų grandinė (paieška, rezervavimas, užsakymas), su `previous_receipt_hash` siejančiomis kiekvieną su ankstesniu. |

Šablonai tiesiogiai pasirašo duomenų užkrauto kanoninį JCS baitų vaizdą naudodami Ed25519.
SHA-256 lieka naudojamas turinio santraukų ir kvitų grandinės nuorodų atvaizdavimui, ne kaip
papildomas priešpasirašymo maišos žingsnis.

## Pavyzdžių patikrinimas

Naudojant `18-signed-receipts.ipynb`, pirmiausia paleiskite Setup ir 1–3 skyrius.
3 skyrius apibrėžia `verify_chain`; tik 1 ir 2 skyrius nepakanka.
Tada paleiskite žemiau esančią bloką naujame lange, nustatydami užrašų darbinį katalogą
kaip `18-securing-ai-agents/code_samples`. Šablonų keliai žemiau yra santykiniai šiam katalogui.


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

### Pavyzdžio tikrinimas be Jupyter

Iš saugyklos šaknies įdiekite pamokos priklausomybes ir paleiskite:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Šie testai įvykdo užrašų Python pavyzdžius ir tikslią README sekciją
aukščiau. Jie taip pat tikrina, ar manipuliavimas ir neįpirkti raktai atmetami
tikrinimo metu. Testai praleidžia užrašų `%pip` inicijavimo ląstelę, nes priklausomybės
įdiegiamos atskirai. Jie nekeičia užrašų ar šablonų.

## Kaip jie buvo sugeneruoti

Šablonai naudoja tą pačią kodo kelią kaip ir užrašai, su vienu fiksuotu pasirašymo raktu
ir fiksuotais laiko žymekliais dėl baitų atkuriamumo. Norint iš naujo sugeneruoti:

```bash
python3 generate_fixtures.py
```

(Scenarijus yra `generate_fixtures.py` šiame kataloge.)

## Ko studentai išmoksta nagrinėdami neapdorotą JSON

Skaitant žalią kvito formatą, suformuojama intuicija, kurios kartais neužrašų ląstelės
nepateikia. Studentai, greitai perbėgdami JSON, dažnai pastebi:

1. Parašas yra nepermatomas base64url eilutė, tačiau visi kiti laukai yra aiškūs
   skaitomi JSON formatu. Parašas nešifruoja turinio; jis patvirtina turinį.
2. `public_key` yra įterptas kvite, kas pakanka savarankiškam
   patikrinimui, bet ne leidėjo pasitikėjimui. Auditorius turi palyginti jį su raktu,
   kuris pritvirtintas už kvito ribų arba gaunamas iš patikimos registracijos.
3. Pakeitus vieną simbolį bet kuriame lauke ir vėl palyginus šį failą su
   `02_tampered_receipt.json`, baitų lygmens mechanizmas tampa aiškus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->