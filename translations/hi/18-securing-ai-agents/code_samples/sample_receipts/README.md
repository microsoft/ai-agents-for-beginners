# नमूना रसीद फ़िक्सचर्स

बिना नोटबुक चलाए निरीक्षण के लिए तीन पूर्व-निर्मित रसीद फ़ाइलें।

| फ़ाइल | यह क्या है |
|---|---|
| `01_valid_receipt.json` | एक वैध हस्ताक्षरित रसीद `lookup_flights` टूल कॉल के लिए। सत्यापन True लौटाता है। |
| `02_tampered_receipt.json` | उसी रसीद में हस्ताक्षर के बाद एक फ़ील्ड संशोधित किया गया। सत्यापन False लौटाता है। |
| `03_chain_three_receipts.json` | तीन वैध रसीदों की श्रृंखला (search, hold, book) जिसमें `previous_receipt_hash` प्रत्येक को पिछले से जोड़ता है। |

फिटिंग्स सीधे Ed25519 के साथ पेलोड के कैनॉनिकल JCS बाइट्स पर हस्ताक्षर करते हैं।
SHA-256 कंटेंट डाइजेस्ट और रसीद-चेन लिंक के लिए उपयोग में रहता है, इसे हस्ताक्षर करने से पहले अतिरिक्त प्री-हैश के रूप में नहीं।


## नमूनों का सत्यापन करना

`18-signed-receipts.ipynb` में, पहले Setup और Sections 1 से 3 चलाएँ।
Section 3 `verify_chain` को परिभाषित करता है; केवल Sections 1 और 2 पर्याप्त नहीं हैं।
फिर निम्नलिखित ब्लॉक को एक नए सेल में चलाएँ, नोटबुक के कार्यशील निर्देशिका
को `18-securing-ai-agents/code_samples` पर सेट करें। नीचे दिए गए फिक्स्चर पथ उस निर्देशिका के सापेक्ष हैं।


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

### Jupyter के बिना उदाहरण की जांच करना

रिपॉजिटरी रूट से, पाठ के निर्भरता स्थापित करें और चलाएं:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ये परीक्षण नोटबुक के Python उदाहरणों और ऊपर दिए गए ठीक README ब्लॉक को चलाते हैं। 
ये यह भी जांचते हैं कि छेड़छाड़ और बिना पिन किए गए कुंजी सत्यापकों द्वारा अस्वीकृत हैं। 
परीक्षण नोटबुक के `%pip` सेटअप सेल को छोड़ देते हैं क्योंकि निर्भरताएं अलग से स्थापित होती हैं। 
वे नोटबुक या फिक्स्चर को बदलते नहीं हैं।

## इन्हें कैसे बनाया गया

फिक्स्चर वही कोड पथ उपयोग करते हैं जो नोटबुक उपयोग करता है, एक फिक्स्ड साइनिंग कुंजी
और बाइट-प्रोड्यूसिबिलिटी के लिए फिक्स्ड टाइमस्टैम्प के साथ। पुनः उत्पन्न करने के लिए:

```bash
python3 generate_fixtures.py
```

(स्क्रिप्ट इस निर्देशिका में `generate_fixtures.py` पर है।)

## कच्चे JSON का निरीक्षण करके छात्र क्या सीखते हैं

कच्चे रसीद फ़ॉर्मेट को पढ़ने से वह अंतर्दृष्टि बनती है जो नोटबुक की कोशिकाएं
हमेशा प्रदान नहीं करतीं। जो छात्र JSON को जल्दी से देखते हैं, वे अक्सर नोटिस करते हैं:

1. सिग्नेचर एक अस्पष्ट बेस64url स्ट्रिंग है, लेकिन हर अन्य फ़ील्ड साधारण है
   पठनीय JSON। हस्ताक्षर सामग्री को एन्क्रिप्ट नहीं करता है; यह इसकी पुष्टि करता है।
2. `public_key` रसीद में एम्बेड किया गया है, जो आत्म-संगति जांचने के लिए पर्याप्त है
   लेकिन जारीकर्ता विश्वास के लिए नहीं। एक ऑडिटर को इसे एक कुंजी के साथ तुलना करनी चाहिए
   रिसिप्ट के बाहर पिन किया गया या एक विश्वसनीय रजिस्ट्री के माध्यम से हल किया गया।
3. किसी भी फ़ील्ड के एकल वर्ण को संशोधित करना, फिर इस फ़ाइल की पुनः तुलना
   `02_tampered_receipt.json` से करना, बाइट-स्तरीय तंत्र को ठोस बनाता है।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->