# नमूना रसिद फिक्स्चरहरू

नोटबुक चलाउनु बिना निरीक्षणका लागि चार पूर्व-निर्मित रसिद फाइलहरू।

| फाइल | के हो |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` उपकरण कलको लागि मान्य हस्ताक्षर गरिएको रसिद। प्रमाणीकरणले True फर्काउँछ। |
| `02_tampered_receipt.json` | हस्ताक्षर पछि एउटा क्षेत्र परिमार्जन गरिएको उस्तै रसिद। प्रमाणीकरणले False फर्काउँछ। |
| `03_chain_three_receipts.json` | तीन मान्य रसिदहरूको शृंखला (खोज, होल्ड, बुक) जसले `previous_receipt_hash` प्रयोग गरेर हरेकलाई अघिल्लोमा जोड्छ। |
| `04_resigned_receipt.json` | उस्तै रसिदमा आक्रमणकारीले फेरि हस्ताक्षर गरी आक्रमण गरेको, आक्रमणकारीको आफ्नै सार्वजनिक कुञ्जी समावेश गरिएको। यसमा रहेको कुञ्जीको विरुद्ध प्रमाणित हुन्छ। जारीकर्ताको कुञ्जीको विरुद्ध असफल हुन्छ। |

फिक्स्चरहरूले Ed25519 सँग पेलोडको canonical JCS बाइटहरू सिधै हस्ताक्षर गर्छन्।
SHA-256 सामग्री डाइजेस्ट र रसिद-श्रृंखला लिंकहरूका लागि प्रयोगमा रहन्छ, हस्ताक्षर अघि अतिरिक्त प्रि-ह्यासको रूपमा होइन।


## नमूनाहरू प्रमाणीकरण गरिँदै

`18-signed-receipts.ipynb` मा, सर्वप्रथम Setup र १ देखि ३ सम्मको खण्डहरू चलाउनुहोस्।
खण्ड ३ ले `verify_chain` परिभाषित गर्दछ; केवल खण्ड १ र २ पर्याप्त छैनन्।
त्यसपछि नयाँ सेलमा निम्न ब्लक चलाउनुहोस्, नोटबुकको कार्य निर्देशिका
`18-securing-ai-agents/code_samples` मा सेट गरिएको। तलका फिक्स्चर पथहरू उक्त निर्देशिकासँग सापेक्षिक छन्।


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

### Jupyter बिना उदाहरण जाँच्दै

रिपोजिटरीको मूलबाट, पाठ्यक्रम निर्भरता स्थापना गरी चलाउनुहोस्:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

यी परीक्षणहरूले नोटबुकका पाइथन उदाहरणहरू र माथिको ठीक README ब्लक चलाउँछन्।
तिनीहरूले आक्रमण र अनपिन गरिएको कुञ्जीहरू प्रमाणीकरणकर्ताद्वारा अस्वीकृत हुने पनि जाँच गर्छन्।
परीक्षणहरूले नोटबुकको `%pip` सेटअप सेल छोड्छन् किनभने निर्भरताहरू अलग्गै स्थापना गरिएको हुन्छ।
तिनीहरूले नोटबुक वा फिक्स्चरहरू परिवर्तन गर्दैनन्।

## यी कसरी उत्पन्न गरियो

फिक्स्चरहरूले नोटबुकसँग उस्तै कोड पथ प्रयोग गर्दछन्, एक स्थिर हस्ताक्षर कुञ्जी
र बाइट पुनरुत्पादनको लागि स्थिर टाइमस्ट्याम्पहरूसँग। पुनः उत्पन्न गर्न:

```bash
python3 generate_fixtures.py
```

(स्क्रिप्ट यस निर्देशिकामा `generate_fixtures.py` मा छ।)

`../test_signed_receipts.py` यस सबैलाई स्वचालित रूपमा जाँच्छ: यसले
नोटबुकको कोड चलाउँछ, यी चार फिक्स्चरहरू नोटबुकको
`verify_receipt` र `verify_chain` सँग प्रमाणीकरण गर्छ, र फिक्स्चरहरू पुनः उत्पन्न गर्दा
ठ्याक्कै उही बाइट आउँछ भनी पुष्टि गर्छ। `code_samples` बाट:

```bash
python -m unittest test_signed_receipts
```

## कच्चा JSON निरीक्षण गर्दा विद्यार्थीहरूले के सिक्छन्

कच्चा रसिद ढाँचा पढ्दा नोटबुकका कोषहरूले सधैं दिन नसक्ने नैतिक ज्ञान विकास हुन्छ।
JSON छिटो हेरिरहेका विद्यार्थीहरूले प्रायः ध्यान दिन्छन्:

1. हस्ताक्षर धूसर base64url स्ट्रिङ हो, तर अन्य सबै क्षेत्रहरू सामान्य
   पढ्नयोग्य JSON छन्। हस्ताक्षर सामग्रीलाई इन्क्रिप्ट गर्दैन; यसले प्रमाणित गर्दछ।
2. `public_key` रसिदमा समावेश गरिएको हुन्छ, जसले फाइललाई
   स्व-सम्पूर्ण बनाउँछ तर अडिट गर्नेले यस विरुद्ध प्रमाणीकरण गर्दैन। तुलना
   `02_tampered_receipt.json` र `04_resigned_receipt.json` लाई: दुवैलाई
   हस्ताक्षर पछि परिवर्तन गरिएको थियो, तर दोस्रो आक्रमणकारीले पुनः हस्ताक्षर गरेको
   आफ्नो कुञ्जीसँग, त्यसैले यसले आफ्नो कुञ्जीसँग प्रमाणीकरण गर्छ। समावेश कुन्जीले
   फाइललाई आन्तरिक रूपमा सुसंगत बनाउँछ। बाहिरबाट प्राप्त कुञ्जी मात्र
   जारीकर्ताको परिचय दिन्छ।
3. `signature` बाहेक कुनै पनि फिल्डको एक अक्षर परिवर्तन गरी,
   यो फाइललाई `02_tampered_receipt.json` सँग फेरि तुलना गर्दा,
   बाइट-स्तर मेकानिज्म स्पष्ट हुन्छ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->