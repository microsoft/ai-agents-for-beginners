# नमुना रसीद फिटचर्स

नोटबुक न चालवता तपासणीसाठी तीन पूर्वनिर्मित रसीद फायली.

| फायली | काय आहे |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` टूल कॉलसाठी वैध स्वाक्षरी केलेली रसीद. सत्यापन True दर्शवते. |
| `02_tampered_receipt.json` | स्वाक्षरीनंतर एका फील्डमध्ये बदल केलेली तीच रसीद. सत्यापन False दर्शवते. |
| `03_chain_three_receipts.json` | तीन वैध रसीदांच्या साखळीची (search, hold, book) रसीद, ज्यात `previous_receipt_hash` प्रत्येकाला मागील रसीदशी जोडते. |

फिटचर्स थेट पेलोडच्या कॅनोनिकल JCS बाइट्सवर Ed25519 सह स्वाक्षरी करतात.
SHA-256 अजूनही सामग्री डाइजेस्ट आणि रसीद-साखळी लिंकसाठी वापरले जाते,  
स्वाक्षरी करण्यापूर्वी अतिरिक्‍त प्री-हॅश म्हणून नाही.

## नमुने सत्यापित करणे

`18-signed-receipts.ipynb` मध्ये, प्रथम सेटअप आणि विभाग 1 ते 3 चालवा.
विभाग 3 मध्ये `verify_chain` परिभाषित केले आहे; केवळ विभाग 1 आणि 2 पुरेसे नाहीत.
नंतर खालील ब्लॉक नवीन सेलमध्ये चालवा, नोटबुकची कार्यरत निर्देशिका
`18-securing-ai-agents/code_samples` वर सेट केलेली असावी. खालील फिक्स्चर मार्ग
त्या निर्देशिकेच्या सापेक्ष आहेत.

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

### Jupyter शिवाय उदाहरण तपासणे

रिपॉझिटरीच्या मूळ निर्देशिकेतून, धड्याच्या अवलंबित्वे स्थापित करा आणि चालवा:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

हे चाचण्या नोटबुकमधील Python उदाहरणे आणि README मधील नेमका ब्लॉक चालवतात.
वर दिलेले. ते हे देखील तपासतात की छेडछाड आणि अनपिन केलेल्या कींना परीक्षकांकडून
नाकारल्या जातात. चाचण्या नोटबुकचा `%pip` सेटअप सेल वगळतात कारण अवलंबित्वे
स्वतंत्रपणे स्थापित केली जातात. त्या नोटबुक किंवा फिक्स्चर्स बदलत नाहीत.

## हे कसे तयार करण्यात आले

फिटचर्स नोटबुकसाठी वापरल्या जाणाऱ्या कोडमार्गाचा वापर करतात, एका निश्चित स्वाक्षरी कीसह  
आणि पुन्हा तयार करण्यासाठी निश्चित वेळा वापरून. पुन्हा तयार करण्यासाठी:

```bash
python3 generate_fixtures.py
```

(स्क्रिप्ट `generate_fixtures.py` या फोल्डरमध्ये आहे.)

## विद्यार्थ्यांना रॉ JSON तपासून काय शिकायला मिळते

रॉ रसीद फॉरमॅट वाचणे त्या जाणिवेस प्रवृत्त करते जी नोटबुकमधील  
सेल्स नेहमी देत नाहीत. JSON पटकन पाहणाऱ्या विद्यार्थ्यांकडे सहसा लक्ष वेधले जाते:

1. स्वाक्षरी ही एक अस्पष्ट base64url स्ट्रिंग आहे, पण इतर प्रत्येक फील्ड प्लेन  
   वाचनीय JSON मध्ये आहे. स्वाक्षरी सामग्रीला एन्क्रिप्ट करत नाही, ती त्याचे प्रमाणपत्र देते.
2. `public_key` रसीदेमध्ये अंतर्भूत आहे. एक ऑडिटरला काहीही वेगळे  
   आवश्यक नाही सत्यापनासाठी (जर की सत्य मूळधारकाचा असल्याचा विश्वास ठेवला तर; ओळख यंत्रणा विषयी README पाहा).
3. कोणत्याही फील्डचा एकही अक्षर बदलणे, नंतर `02_tampered_receipt.json` या फाईलशी  
   पुन्हा तुलना करणे, बाइट-स्तरीय यंत्रणा स्पष्ट करते.


---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
