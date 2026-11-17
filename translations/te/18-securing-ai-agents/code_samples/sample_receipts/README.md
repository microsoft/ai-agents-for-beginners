# నమూనా రసీదు ఫిక్చర్లు

నోట్‌బుక్ నడిపించకుండా పరిశీలన కోసం నాలుగు ప్రీ-జనరేటెడ్ రసీదు ఫైల్స్.

| ఫైల్ | ఇది ఏమిటి |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` టూల్ కాల్ కోసం చెల్లుబాటు అయ్యే సంతకం చేసిన రసీదు. ధృవీకరణ ఫలితం True వస్తుంది. |
| `02_tampered_receipt.json` | సంతకం చేసిన తరువాత ఒక ఫీల్డ్ మార్చబడిన అదే రసీదు. ధృవీకరణ ఫలితం False వస్తుంది. |
| `03_chain_three_receipts.json` | మూడు చెల్లుబాటు అయ్యే రసీదుల గొలుసు (search, hold, book), ప్రతి ఒక్కటి మునుపటి వాటితో `previous_receipt_hash` ద్వారా అనుసంధానం చేయబడి ఉంటుంది. |
| `04_resigned_receipt.json` | అదే రసీదు దోపిడి చేయబడిన తరువాత దోపిడి చేస్తున్న వ్యక్తి సంతకం చేసినప్పటికీ, దోపిడి చేస్తున్న వ్యక్తి యొక్క స్వంత పబ్లిక్ కీతో నింపబడింది. దీని వైపు కీతో ధృవీకరిస్తుంది. ఆపై జారీదారు కీతో విఫలమవుతుంది. |

ఫిక్చర్లు Ed25519 తో ప్యaload యొక్క క్యానానికల్ JCS బైట్స్‌ను నేరుగా సంతకం చేస్తాయి.
కంటెంట్ డైజెస్ట్‌లు మరియు రసీదు-గొలుసు లింక్స్ కోసం SHA-256 ఇంకా ఉపయోగిస్తారు, సంతకం చేసేముందు అదనపు ప్రీ-హ్యాష్ విధానం కాదు.


## నమూనాలను ధృవీకరించడం

`18-signed-receipts.ipynb`లో, మొదట సెటప్ మరియు సెక్షన్లు 1 నుండి 3 వరకు నడపండి.
సెక్షన్ 3 లో `verify_chain` నిర్వచించబడింది; సెక్షన్లు 1 మరియు 2 మాత్రమే సరిపోవు.
ఆ తర్వాత క్రింది బ్లాక్ ను కొత్త సెల్ లో నడపండి, మరియు నోట్‌బుక్ యొక్క వర్కింగ్ డైరెక్టరీ
`18-securing-ai-agents/code_samples`గా సెట్ చేయండి. కింద ఇచ్చిన ఫిక్చర్ మార్గాలు ఆ డైరెక్టరీకి సంబంధించి ఉన్నాయి.


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

### జ్యూయిపిటర్ లేకుండా ఉదాహరణ తనిఖీ చేయడం

రిపాజిటరీ రూట్ నుండి, పాఠం డిపెండెన్సీలను ఇన్‌స్టాల్ చేసి, నడపండి:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ఈ పరీక్షలు నోట్‌బుక్ లోని పట్లాన్ ఉదాహరణలను మరియు పై EXACT README బ్లాక్ ను నడిపిస్తాయి.
అవి కూడా దోపిడి మరియు అన్‌పిన్న్డ్ కీలు వేరీఫైయర్ల ద్వారా తిరస్కరించబడ్డాయో లేదో తనిఖీ చేస్తాయి.
పరీక్షలు నోట్‌బుక్ లోని `%pip` సెటప్ సెల్ ని దాటిచెప్పుతాయి ఎందుకంటే డిపెండెన్సీలు వేరుగా ఇన్‌స్టాల్ అయ్యాయి.
అవి నోట్‌బుక్ లేదా ఫిక్చర్లు మార్చవు.

## ఇవి ఎలా రూపొందించబడ్డాయి

ఫిక్చర్లు నోట్‌బుక్ లో ఉపయోగించిన అదే కోడ్ మార్గం ఉపయోగిస్తాయి, ఒక నిర్ధారిత సంతకం కీ మరియు బైట్ పునరుత్పత్తి కోసం నిర్ధారిత టైమ్‌స్టాంప్‌లు ఉన్నాయి.
మళ్లీ తయారు చేయడానికి:

```bash
python3 generate_fixtures.py
```

(స్క్రిప్ట్ ఈ డైరెక్టరీలోని `generate_fixtures.py` వద్ద ఉంది.)

`../test_signed_receipts.py` దీనిని స్వయంచాలకంగా తనిఖీ చేస్తుంది: ఇది నడిపిస్తుంది
నోట్‌బుక్ కోడ్, ఈ నాలుగు ఫిక్స్చర్లను నోట్‌బుక్ యొక్క
`verify_receipt` మరియు `verify_chain` తో ధృవీకరిస్తుంది, మరియు పునఃసృష్టించడం
ఫిక్స్చర్లు ఒకే బైట్స్ ఇస్తాయని నిర్ధారిస్తుంది. `code_samples` నుండి:

```bash
python -m unittest test_signed_receipts
```

## ద 학생లు raw JSON ని పరిశీలించి ఏం నేర్చుకుంటారు

రా రసీదుల ఫార్మాట్ ని చదవడం, నోట్‌బుక్‌లో సెల్స్ ఎల్లప్పుడూ అందించని అనుభూతిని
నిర్మిస్తుంది. JSON ని త్వరగా చదివే విద్యార్థులు సాధారణంగా గమనిస్తారు:

1. సంతకం ఒక అజ్ఞాత base64url స్ట్రింగ్, కానీ మిగిలిన ప్రతి ఫీల్డ్ సరళమైన
   చదవగల JSON. సంతకం కంటెంట్ ను గోప్యంగా మార్చదు; అది దానికి ధృవాన్ని ఇస్తుంది.
2. `public_key` రసీదు లో జోడించబడింది, ఇది ఫైల్ ని
   స్వీయ-క్ంటైన్డ్ గా చేస్తుంది కానీ ఆడిట్ చేయు వ్యక్తి వేరిఫై చేయేది కాదు. పోల్చండి
   `02_tampered_receipt.json` ను `04_resigned_receipt.json` తో: రెండింటినీ
   సంతకం చేసిన తర్వాత మార్చింది, కానీ రెండవది ఆగ్రహించే వారి తమ
   కీతో మళ్లీ సంతకం చేయబడింది, కాబట్టి ఇది దాన్ని కొనసాగించే కీతో ధృవీకరించబడుతుంది. జోడించిన కీ
   మీరు ఫైల్ అంతర్గతంగా సక్రమమని చెపుతుంది. మీరు పొందిన కీ మాత్రమే
   ఎవరు జారీ చేశారో మీకు తెలియజేస్తుంది.
3. `signature` కి బయితిరుగు ఏదైనా ఫీల్డ్ లో ఒక అక్షరాన్ని మార్చివేయడం,
   ఆ ఫైల్ ని `02_tampered_receipt.json` తో మళ్ళీ సరిపోల్చడం,
   బైట్ స్థాయి మెకానిజాన్ని స్పష్టంగా చూపిస్తుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->