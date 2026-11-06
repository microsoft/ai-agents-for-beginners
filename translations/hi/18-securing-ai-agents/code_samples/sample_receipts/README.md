# नमूना रसीद फिक्स्चर

नोटबुक चलाए बिना निरीक्षण के लिए चार पूर्व-जनरेट की गई रसीद फ़ाइलें।

| फ़ाइल | क्या है यह |
|---|---|
| `01_valid_receipt.json` | एक वैध हस्ताक्षरित रसीद `lookup_flights` टूल कॉल के लिए। सत्यापन True लौटाता है। |
| `02_tampered_receipt.json` | हस्ताक्षर के बाद एक क्षेत्र में संशोधन के साथ वही रसीद। सत्यापन False लौटाता है। |
| `03_chain_three_receipts.json` | तीन वैध रसीदों की श्रृंखला (search, hold, book) जिसके साथ `previous_receipt_hash` प्रत्येक को पिछले से जोड़ता है। |
| `04_resigned_receipt.json` | वही रसीद जिसे छेड़छाड़ की गई और फिर हमलावर द्वारा पुनः हस्ताक्षरित किया गया, जिसमें हमलावर की अपनी सार्वजनिक कुंजी सम्मिलित है। अंदर की कुंजी के खिलाफ सत्यापित करता है। जारीकर्ता की कुंजी के खिलाफ विफल रहता है। |

फिक्स्चर पेलोड के कैनोनिकल JCS बाइट्स को सीधे Ed25519 के साथ साइन करते हैं।
सामग्री डाइजेस्ट और रसीद-चेन लिंक के लिए SHA-256 का उपयोग जारी रहता है, न कि
साइनिंग से पहले किसी अतिरिक्त प्री-हैश के रूप में।

## नमूनों का सत्यापन

`18-signed-receipts.ipynb` में, पहले Setup और अनुभाग 1 से 3 तक चलाएं।
अनुभाग 3 में `verify_chain` परिभाषित किया गया है; केवल अनुभाग 1 और 2 पर्याप्त नहीं हैं।
फिर नीचे दिए गए ब्लॉक को एक नए सेल में चलाएँ, नोटबुक की वर्किंग डायरेक्टरी
को `18-securing-ai-agents/code_samples` पर सेट करें। नीचे दिए गए फिक्सचर पथ उस डायरेक्टरी के सापेक्ष हैं।


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

### Jupyter के बिना उदाहरण की जाँच करना

रिपॉजिटरी रूट से, लेसन निर्भरताएं इंस्टॉल करें और चलाएँ:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ये परीक्षण नोटबुक के Python उदाहरण और ऊपर दिए गए सटीक README ब्लॉक को निष्पादित करते हैं।
वे यह भी जांचते हैं कि छेड़छाड़ और अनुचित चाबियां सत्यापनकर्ताओं द्वारा अस्वीकृत की गई हैं।
परीक्षण नोटबुक की `%pip` सेटअप सेल को छोड़ देते हैं क्योंकि निर्भरताएं
वे अलग से इंस्टॉल किए जाते हैं। वे नोटबुक या फिटिंग्स को नहीं बदलते हैं।

## ये कैसे उत्पन्न किए गए थे

फिटिंग्स उसी कोड पथ का उपयोग करते हैं जो नोटबुक करता है, एक निश्चित साइनिंग कुंजी के साथ
और बाइट-प्रजनन क्षमता के लिए निश्चित टाइमस्टैम्प के साथ। पुनः उत्पन्न करने के लिए:

```bash
python3 generate_fixtures.py
```

(स्क्रिप्ट इस निर्देशिका में `generate_fixtures.py` पर है।)

`../test_signed_receipts.py` इसे स्वचालित रूप से जांचता है: यह
नोटबुक के कोड को चलाता है, नोटबुक के साथ इन चार फिटिंग्स को प्रमाणित करता है
`verify_receipt` और `verify_chain`, और पुष्टि करता है कि फिटिंग्स का पुनः उत्पादन
बिल्कुल एक जैसे बाइट्स देता है। `code_samples` से:

```bash
python -m unittest test_signed_receipts
```

## कच्चे JSON का निरीक्षण करने से छात्र क्या सीखते हैं

कच्चे रसीद प्रारूप को पढ़ने से उन अंतर्दृष्टियों का निर्माण होता है जो नोटबुक में
कोशिकाएँ हमेशा प्रदान नहीं कर पाती। जो छात्र JSON को संक्षेप में देखते हैं, वे अक्सर ध्यान देते हैं:

1. हस्ताक्षर एक अस्पष्ट बेस64url स्ट्रिंग है, लेकिन हर अन्य फ़ील्ड स्पष्ट
   पठनीय JSON है। हस्ताक्षर सामग्री को एन्क्रिप्ट नहीं करता; यह उसकी पुष्टि करता है।
2. `public_key` रसीद में एम्बेड है, जो फाइल को
   स्वयं में पूर्ण बनाता है लेकिन यह वह नहीं है जिसकी एक ऑडिटर जांच करता है। तुलना करें
   `02_tampered_receipt.json` को `04_resigned_receipt.json` से: दोनों को
   साइनिंग के बाद बदला गया था, लेकिन दूसरे को हमलावर की
   अपनी कुंजी से फिर से साइन किया गया, इसलिए यह उस कुंजी के खिलाफ प्रमाणित होता है जो इसमें है। एम्बेडेड कुंजी
   बताती है कि फाइल आंतरिक रूप से सुसंगत है। केवल कहीं और प्राप्त कुंजी आपको बताती है कि इसे किसने जारी किया है।
   अन्यत्र आपको बताया जाता है कि इसे किसने जारी किया था।
3. `signature` के बाहर किसी भी फील्ड के एकल अक्षर को संशोधित करना, फिर
   इस फ़ाइल की तुलना `02_tampered_receipt.json` से पुनः करना,
   बाइट-स्तरीय तंत्र को ठोस बनाता है।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->