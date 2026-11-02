# नमूना रसिद फिक्स्चर्स

नोटबुक नचलाइकन निरीक्षणका लागि तीनवटा पूर्व-उत्पन्न रसिद फाइलहरू।

| फाइल | के हो |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` उपकरण कलको लागि मान्य हस्ताक्षरित रसिद। प्रमाणीकरणले सत्य फर्काउँछ। |
| `02_tampered_receipt.json` | हस्ताक्षर गरेपछि एक क्षेत्र परिमार्जन गरिएको उही रसिद। प्रमाणीकरणले असत्य फर्काउँछ। |
| `03_chain_three_receipts.json` | तीन वटा मान्य रसिदहरूको श्रृंखला (खोज, राख्नुहोस्, बुक) जसमा `previous_receipt_hash` ले प्रत्येकलाई अघिल्लो रसिदसँग जोड्छ। |

यी फिक्स्चर्सले पेलोडको मानक JCS बाइटहरू Ed25519 सँग सिधै हस्ताक्षर गर्छन्।
SHA-256 अझै पनि सामग्री डाइजेस्ट र रसिद-श्रृंखला लिंकहरूका लागि प्रयोग हुन्छ, हस्ताक्षरअघि
अतिरिक्त प्रि-ह्यासको रूपमा होइन।

## नमूनाहरूको जाँच

`18-signed-receipts.ipynb` मा, पहिले सेटअप र सेक्सन 1 देखि 3 चलाउनुहोस्।
सेक्सन 3 ले `verify_chain` परिभाषित गर्छ; मात्र सेक्सन 1 र 2 पर्याप्त छैनन्।
त्यसपछि नयाँ सेलमा तलको ब्लक चलाउनुहोस्, नोटबुकको कार्य निर्देशिका
लाई `18-securing-ai-agents/code_samples` मा सेट गरिएको। तलका फिक्स्चर पथहरू सापेक्ष
त्यस निर्देशिकासँग।

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

### Jupyter बिना उदाहरण जाँच

रिपोजिटरी रुटबाट पाठका निर्भरताहरू स्थापना गरी चलाउनुहोस्:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

यी परीक्षणहरूले नोटबुकका Python उदाहरणहरू र ठ्याक्कै README ब्लक चलाउँछन्
माथि। तिनीहरूले साथै छेडछाड र अनपिन गरिएका कुञ्जीहरू प्रमाणकहरूले
अस्वीकृत गर्छन्। परीक्षणहरूले नोटबुकको `%pip` सेटअप सेल स्किप गर्छन् किनभने निर्भरता
अलग रूपमा स्थापना गरिएका छन्। तिनीहरूले नोटबुक वा फिक्स्चरहरू परिवर्तन गर्दैनन्।

## कसरी यी उत्पादन गरियो

फिक्स्चर्सले नोटबुक जस्तै कोड पथ प्रयोग गर्छ, एकै निश्चित हस्ताक्षर कुञ्जी
र निश्चित टाइमस्ट्याम्पहरू बाइट पुनरुत्पादनका लागि। पुनःउत्पादन गर्न:

```bash
python3 generate_fixtures.py
```

(स्क्रिप्ट यस डिरेक्ट्रीमा `generate_fixtures.py` मा छ।)

## विद्यार्थीहरूले कच्चा JSON निरीक्षण गरेर के सिक्छन्

कच्चा रसिद ढाँचा पढ्दा नोटबुकका सेलहरूले जहिले पनि नदिने अन्तर्दृष्टि निर्माण हुन्छ।
JSON छरपस्टरी हेरिरहेका विद्यार्थीहरूले प्रायः देख्छन्:

1. हस्ताक्षर एक अस्पष्ट base64url स्ट्रिङ हो, तर बाँकि सबै क्षेत्र स्पष्ट
   पढ्न मिल्ने JSON हो। हस्ताक्षरले सामग्रीलाई एन्क्रिप्ट गर्दैन; यसले त्यसलाई प्रमाणित गर्छ।
2. `public_key` रसिदमा एम्बेड गरिएको छ। एक अडिटरलाई प्रमाणीकरण गर्न
   अरु केही आवश्यक छैन (के उक्त कुञ्जी साँच्चिकै दाबी गरिएका जारीकर्ताको हो भन्नेमा भरोसा गर्ने सन्दर्भमा;
   पहिचान पूर्वाधार सम्बन्धी पाठ README हेर्नुहोस्)।
3. कुनै क्षेत्रको एक अक्षर मात्र परिमार्जन गरी `02_tampered_receipt.json` सँग पुनः तुलना गर्दा,
   बाइट-स्तर मेकानिज्म स्पष्ट हुन्छ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
