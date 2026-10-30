# నమూనా రశీదు ఫిక్చర్లు

నోట్‌బుక్ నడపకుండా పరిశీలించడానికి మూడు ముందుగానే సృష్టించిన రశీదు ఫైళ్లు.

| ఫైల్ | ఇది ఏమిటి |
|---|---|
| `01_valid_receipt.json` | ఒక `lookup_flights` టూల్ కాల్ కోసం చెలామణీైన సంతకం చేసిన రసీదు. నిర్ధారణ ఫలితం True. |
| `02_tampered_receipt.json` | సంతకం చేసిన తర్వాత ఒక రంగంలో మార్పు చేసిన సలువైన అదే రసీదు. నిర్ధారణ ఫలితం False. |
| `03_chain_three_receipts.json` | మూడు చెలామణీైన రసీదుల శ్రేణి (search, hold, book) వాటిని వరుసగా లింక్ చేసే `previous_receipt_hash` తో. |

ఫిక్చర్లు లోడును యొక్క కేనానికల్ JCS బైట్లను ప్రత్యక్షంగా Ed25519 తో సంతకం చేస్తాయి.
SHA-256 అనేది కంటెంట్ డైజెస్ట్‌లు మరియు రసీది-చైన్ లింకులకు ఉపయోగంలో ఉంటుంది, సంతకం కోర్ ముందు అదనపు ప్రీ-హ్యాష్‌గా కాదు.


## నమూనాలను ధృవీకరించడం

`18-signed-receipts.ipynb` లో, ముందుగా Setup మరియు సెక్షన్స్ 1 నుండి 3 నడిపించండి.
సెక్షన్ 3 `verify_chain` ని నిర్వచిస్తుంది; సెక్షన్లు 1 మరియు 2 మాత్రమే చాలవు.
తరువాత కింది బ్లాక్‌ను కొత్త సెల్‌లో, నోట్‌బుక్ పని డైరెక్టరీగా
`18-securing-ai-agents/code_samples` ను సెట్ చేసి అమర్చండి. దిగువ ఫిక్స్చర్ మార్గాలు ఆ డైరెక్టరీకు
నిష్ప్రభమైనవి.

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

### జూపైటర్ లేకుండా ఉదాహరణను తనిఖీ చేయడం

రిపాజిటరీ రూట్ నుండి, పాఠం ఆధారాలు ఇన్‌స్టాల్ చేసి, రన్ చేయండి:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ఈ పరీక్షలు నోట్‌బుక్ యొక్క పైథన్ ఉదాహరణలను మరియు అద్దిపట్టిన README బ్లాక్‌ను నడపడం జరుగుతాయి
పైన. అవి కూడా తెరవుని మార్పిడి మరియు అన్‌పిన్న్ కీలు వాలిడేటర్ల ద్వారా తిరస్కరించబడేలా పరీక్షిస్తాయి.
ఈ పరీక్షలు నోట్‌బుక్ యొక్క `%pip` సెటప్ సెల్‌ని వదలిపోతాయి ఎందుకంటే ఆధారాలు వేరుగా ఇన్స్టాల్ చేయబడతాయి.
అవి నోట్‌బుక్ లేదా ఫిక్స్చర్లను మార్చవు.

## ఇవి ఎలా రూపొందించబడ్డాయి

ఫిక్స్చర్లు నోట్‌బుక్‌తోనే అదే కోడ్ పాథ్‌ని ఉపయోగిస్తాయి, ఒక నిర్ధారిత సంతకం కీ మరియు పిక్స్ చేయబడిన టైమ్‌స్టాంప్లతో
బైట్-రిప్రొడ్యూసిబిలిటీ కోసం. తిరిగి రూపొందించడానికి:

```bash
python3 generate_fixtures.py
```

(స్క్రిప్ట్ ఈ డైరెక్టరీలో `generate_fixtures.py` వద్ద ఉంది.)

## విద్యార్థులు రా JSON‌ని పరిశీలించడం ద్వారా ఏమి నేర్పుకుంటారు

రా రసీదులోని ఫార్మాట్ చదవడం, నోట్‌బుక్‌లోని సెల్స్ ఎప్పుడూ అందించని అవగాహనను ఏర్పరుస్తుంది.
JSON‌ను తేలికగా చదివే విద్యార్థులు తరచుగా గమనిస్తారు:

1. సంతకం ఒక అత్యంత గోప్యమైన base64url స్ట్రింగ్, కానీ అన్ని ఇతర ఫీల్డులు సాధారణమైనవి
   చదవగల JSON. సంతకం విషయం గుప్తీకరించదు; అది దానికి ధృవీకరించడమే.
2. `public_key` రశీదులో జత చేయబడింది, ఇది స్వ-సామరస్యాన్ని పరిశీలించడానికి సరిపోతుంది కానీ జారీదారుని విశ్వాసం కోసం కాదు.
   ఒక ఆడిటర్ అది రశీదుకు బయట ఉన్న ఒక కీతో పోల్చాలి లేదా నమ్మదగిన రిజిస్ట్రీ ద్వారా పరిష్కరించాలి.
   చక్రవర్తి కావాలి.
3. ఏదైనా ఫీల్డ్ యొక్క ఒక్క అక్షరాన్ని మార్చి, ఆ తర్వాత ఈ ఫైల్‌ను
   `02_tampered_receipt.json` తో మళ్లీ సరిపోల్చడం ద్వారా, బైట్-స్థాయి మెకానిజం స్పష్టంగా అవుతుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->