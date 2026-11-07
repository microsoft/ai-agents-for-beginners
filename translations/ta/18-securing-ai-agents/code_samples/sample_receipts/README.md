# மாதிரி ரசீது பொருட்கள்

நோட்புக் பயன்படுத்தாமலேயே பரிசோதனைக்கான நான்கு முன் உற்பத்தி செய்யப்பட்ட ரசீது கோப்புகள்.

| கோப்பு | அது என்ன |
|---|---|
| `01_valid_receipt.json` | ஒரு `lookup_flights` கருவி அழைப்புக்கு செல்லுபடியான கையெழுத்தான ரசீது. சரிபார்ப்பு உண்மையைக் காட்டுகிறது. |
| `02_tampered_receipt.json` | கையெழுத்திடப்பட்ட பிறகு ஒரு புலம் மாற்றப்பட்ட அதே ரசீது. சரிபார்ப்பு முடியாது என்று காட்டுகிறது. |
| `03_chain_three_receipts.json` | மூன்று செல்லுபடியான ரசீதுகளின் தொடர் (search, hold, book), ஒவ்வொன்றும் `previous_receipt_hash` மூலம் முன் ஒன்றுடன் இணைக்கப்பட்டுள்ளன. |
| `04_resigned_receipt.json` | அதே ரசீது மோசடியுடன் மாற்றப்பட்டு பிறகு தாக்குதல் நடத்துபவரால் மீண்டும் கையெழுத்திடப்பட்டது, அதில் தாக்குதல் ந kovar படம் உள்ளது. அதினுள் உள்ள திறவுகோலுக்கு எதிராக சரிபார்க்கிறது. வழங்குபவரின் திறவுகோலுக்கு எதிராக தோல்வி அடைகிறது. |

இந்த டெஸ்டுகள் பளிச் பதிவின் canonical JCS பைட்டுகளை நேரடியாக Ed25519 கொண்டு கையெழுத்திடுகின்றன.
SHA-256 உள்ளடக்க குறியீடுகள் மற்றும் ரசீது தொடர் இணைப்புகளுக்கு பயன்படுத்தப்படுகிறது, கூடுதல் முன்கூட்டிய முன்னோடியைப் பயன்படுத்துவது இல்லை.
கையெழுத்திடுவதற்கு முன்.

## மாதிரிகளை சரிபார்த்தல்

`18-signed-receipts.ipynb` இல், முதலில் Setup மற்றும் பிரிவு 1 முதல் 3 வரை இயக்கவும்.
பிரிவு 3 இல் `verify_chain` வரையறுக்கப்பட்டுள்ளது; பிரிவு 1 மற்றும் 2 மட்டும் போதாது.
பின்னர், புது செலில்தான் கீழ்க்கண்ட தொகுதியை இயக்கவும், குறிப்பேட்டின் வேலைதிடமாக
`18-securing-ai-agents/code_samples` அமைக்கப்பட்டுள்ளது. கீழுள்ள நிர்மாண பாதைகள் அந்த திடத்துக்கே
சார்ந்தவை.

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

### Jupyter இன்றி எடுத்துக்காட்டை சரிபார்க்கும்

இருப்புப்பெட்டியின் மூலத்திலிருந்து, பாடப் பொருளின் சார்புகளை நிறுவி இயக்கவும்:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

இவை குறிப்பேட்டின் Python எடுத்துக்காட்டுகளைப் பரிசோதித்து மேலுள்ள README தொகுதியையும்
சோதிக்கின்றன. மேலும், கையாளப்படாத மற்றும் பிடிக்கப்படாத விசைகள் சரிபார்ப்பாளர்களால்
மறுக்கப்படுவதைவும் பரிசோதிக்கின்றன. சார்புகள் காரணமாக குறிப்பேட்டின் `%pip`
தனித்தனியாக நிறுவப்படுகின்றன. இவை நோட்புக் அல்லது பொருத்துகளைக் மாற்றாது.

## இவை எப்படி உருவாக்கப்பட்டன

பொருத்துக்கள் நோட்புக்கின் சமமான குறியீடு பாதையைப் பயன்படுத்துகின்றன, ஒரு நிலையான கையொப்ப விசை மற்றும் நிலையான நேர முத்திரைகள் மூலம் பைட்டின் மீண்டும் தயாரிப்பைப் பெற.
மீண்டும் உருவாக்க:

```bash
python3 generate_fixtures.py
```

(ஸ்கிரிப்ட் இந்த அடைவு உள்ள `generate_fixtures.py` இல் உள்ளது.)

`../test_signed_receipts.py` இதனை எல்லாவற்றையும் தானாகச் சரிபார்க்கின்றது: இது
நோட்புக்கின் குறியீட்டை இயக்கி, இந்த நான்கு பொருத்துக்களையும் நோட்புக்கின்
`verify_receipt` மற்றும் `verify_chain` உடன் உறுதிப்படுத்தி, பொருத்துக்களை மீண்டும் உருவாக்கும் போது 
அதே பைடுகளை தருவதாக உறுதிசெய்கிறது. `code_samples` இற்கிருந்தது:

```bash
python -m unittest test_signed_receipts
```

## மாணவர்கள் மூல JSON ஐ பரிசீலித்து என்ன கற்றுக்கொள்கிறார்கள்

மூல ரசீது வடிவைப் படிப்பது நோட்பூக்கில் உள்ள செல்களை பின்வாங்கும் பகுத்தறிவை உருவாக்குகிறது.
JSON ஐ விரைவாக பார்ப்பவர்கள் அடிக்கடி கவனிக்கிறார்கள்:

1. கையொப்பம் ஒரு மறைபிடித்த base64url உரையாகும், ஆனாலும் மற்ற எல்லா புலங்களும் பொதுவான வாசிக்கக்கூடிய JSON.
   கையொப்பம் உள்ளடக்கத்தை குறியாக்கமில்லை; அதனை சான்றளிக்கிறது.
2. `public_key` ரசீதுக்குள் இணைக்கப்பட்டுள்ளது, இதனால் கோப்பு
   சுயமாக உள்ளது ஆனால் ஒரு நிருபன் எதிர் பார்த்துப் பார்ப்பதற்கு இது அல்ல.
   `02_tampered_receipt.json` மற்றும் `04_resigned_receipt.json` ஐ ஒப்பிடுக்க: இரண்டும் கையொப்பம் போன பிறகு மாற்றப்பட்டன,
   ஆனால் இரண்டாவது தாக்குவனுடைய சொந்த விசையுடன் மீண்டும் கையொப்பமிடப்பட்டது, எனவே அது தன்னிடம் உள்ள விசைக்கெதிராக உறுதிப்படுத்துகிறது.
   இணைக்கப்பட்ட விசை கோப்பு உள் பொருந்தியுள்ளது என்று கூறுகிறது.
   வேறு எங்கிருந்தோ கிடைத்த விசை உங்களுக்கு யார் வழங்கினார்கள் என்பதைச் சொல்கிறது.

3. `signature` வெளியே உள்ள எந்தவொரு புலத்தின் ஒரு எழுத்தை மாற்றி,
   பின்னர் இந்த கோப்பை `02_tampered_receipt.json` உடன் மீண்டும் ஒப்பிட்டு பார்த்தல்,
   பைட் நிலை இயந்திரத்தை தெளிவாக்குகிறது.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->