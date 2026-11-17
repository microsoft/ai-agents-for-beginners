# नमुना प्राप्ती सुसज्जा

नोटबुक चालवण्याशिवाय तपासणीसाठी चार पूर्वनिर्मित प्राप्ती फाइल्स.

| फाइल | ती काय आहे |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` टूल कॉलसाठी वैध स्वाक्षरी केलेली प्राप्ती. पडताळणी True परत करते. |
| `02_tampered_receipt.json` | स्वाक्षरी केल्यानंतर एका फील्डमध्ये बदल केलेली समान प्राप्ती. पडताळणी False परत करते. |
| `03_chain_three_receipts.json` | तीन वैध प्राप्तींची साखळी (शोधा, धरणे, बुक करा) ज्यामध्ये प्रत्येक मागील प्राप्तीशी `previous_receipt_hash` द्वारे जोडलेले आहे. |
| `04_resigned_receipt.json` | ह्या प्राप्तीला छेडछाड करून हल्लेखोराने पुन्हा स्वाक्षरी केली आहे, ज्यात हल्लेखोराची स्वतःची सार्वजनिक की समाविष्ट आहे. त्यातील कीवर तो पडताळणी होतो. जारीकर्त्याच्या कीवर पडताळणी अपयशी ठरते. |

सुसज्जा Ed25519 सह थेट पे-लोडच्या canonical JCS बाइट्सवर स्वाक्षरी करतात.
SHA-256 अजूनही सामग्रीचा संक्षेप आणि प्राप्ती-साखळी लिंकसाठी वापरला जातो, 
स्वाक्षरीपूर्वी अतिरिक्त प्रि-हॅश म्हणून नाही.

## नमुन्यांची पडताळणी करणे

`18-signed-receipts.ipynb` मध्ये, प्रथम Setup आणि विभाग 1 ते 3 चालवा.
विभाग 3 मध्ये `verify_chain` परिभाषित आहे; फक्त विभाग 1 आणि 2 पुरेसे नाहीत.
त्यानंतर, नवीन सेलमध्ये खालील ब्लॉक चालवा, नोटबुकच्या कार्यरत निर्देशिकेला
`18-securing-ai-agents/code_samples` सेट करा. खालील सुसज्जा मार्ग त्या निर्देशिकेच्या सापेक्ष आहेत.


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

### Jupyter शिवाय उदाहरण तपासणी

रेपॉजिटरी मुळ स्थानावरून, धड्याच्या अवलंबित्वे इंस्टॉल करा आणि चालवा:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

हे चाचणी नोटबुकच्या Python उदाहरणे आणि अचूक README ब्लॉक
वर चालवतात. ते तसेच तपासतात की छेडछाड केलेल्या आणि अनपिन केलेल्या कीजना
सत्यापन करणाऱ्यांकडून नाकारले जाते. चाचण्या नोटबुकचा `%pip` सेटअप सेल वगळतात कारण अवलंबित्व
स्वतंत्रपणे स्थापित केले जातात. त्या नोटबुक किंवा फिक्स्चरमध्ये बदल करत नाहीत.

## हे कसे तयार केले गेले

फिक्स्चर नोटबुकसारखाच कोड मार्ग वापरतात, ज्यात एक निश्चित सही की
आणि बाइट-पुनरुत्पादकतेसाठी निश्चित टाईमस्टॅम्प आहेत. पुनःनिर्माण करण्यासाठी:

```bash
python3 generate_fixtures.py
```

(स्क्रिप्ट या संचिकेमध्ये `generate_fixtures.py` मध्ये आहे.)

`../test_signed_receipts.py` हे सर्व स्वयंचलितपणे तपासते: ते चालवते
नोटबुकच्या कोडने, नोटबुकच्या या चार फिक्स्चर्सची पडताळणी करते
`verify_receipt` आणि `verify_chain` सोबत, आणि पुष्टी करते की फिक्स्चर्सचे पुनर्जन्म
बाइट्समध्ये समान आहे. `code_samples` मधून:

```bash
python -m unittest test_signed_receipts
```

## विद्यार्थ्यांना कच्च्या JSON तपासल्यावर काय शिकायला मिळते

कच्च्या रिसीप्ट स्वरुपाचे वाचन हे निरीक्षण तयार करते की नोटबुकमधील सेल्स नेहमीच उपलब्ध करीत नाहीत. JSON ची झटपट पाहणी करणारे विद्यार्थी सहसा लक्षात घेतात:


1. सही ही एक अस्पष्ट base64url स्ट्रिंग आहे, पण प्रत्येक इतर क्षेत्र साधे वाचनीय JSON आहे.
   सही सामग्री एन्क्रिप्ट करत नाही; ती त्यावर प्रमाणित करते.
2. `public_key` पावतीमध्ये एम्बेड केलेले आहे, ज्यामुळे फाईल
   स्वयंपूर्ण होते पण हेच काही ऑडिटर पडताळणी करत नाही. तुलना करा
   `02_tampered_receipt.json` आणि `04_resigned_receipt.json`: दोन्ही मध्ये बदल
   सही केल्यानंतर झाले होते, पण दुसऱ्या पुन्हा
   हल्लेखोराच्या स्वतःच्या कीने सही केले होते, त्यामुळे ती त्याच्या कीशी पडताळणी होते. एम्बेड केलेली की
   तुम्हाला फाईल अंतर्गत सुसंगत आहे हे सांगते. केवळ इतरत्रून मिळालेली की
   तुम्हाला सांगते की कोणतीसंही ती जारी केली आहे.
३. `signature` च्या बाहेरील कोणत्याही फील्डच्या एका अक्षरात बदल करून,
   नंतर हा फाइल `02_tampered_receipt.json` शी पुन्हा तपासल्यास,
   बाईट-स्तरीय यंत्रणा ठोस होते.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->