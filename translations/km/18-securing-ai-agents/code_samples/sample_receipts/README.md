# គំរូឯកសារទទួល

ឯកសារទទួលចំនួនបួនដែលបានបង្កើតជាមុនសម្រាប់ពិនិត្យដោយមិនចាំបាច់រត់សឺរីនូតប៊ុក។

| ឯកសារ | តើវាជាអ្វី |
|---|---|
| `01_valid_receipt.json` | ឯកសារទទួលដែលបានចុះហត្ថលេខាត្រឹមត្រូវសម្រាប់ការហៅឧបករណ៍ `lookup_flights` មួយ។ ការបញ្ចាក់ប្រត្តិបត្តិជាសុំណាច់ជាក់។ |
| `02_tampered_receipt.json` | ដូចគ្នានឹងឯកសារទទួលមានវាលមួយដែលបានកែប្រែនៅបន្ទាប់ពីចុះហត្ថលេខា។ ការបញ្ចាក់ប្រត្តិបត្តិជាមិនជាភាពជាក់។ |
| `03_chain_three_receipts.json` | សំណុំឯកសារទទួលត្រឹមត្រូវបីសន្លឹក (ស្វែងរក, កាន់, កក់) ដែលមាន `previous_receipt_hash` ចងខ្សែរភ្ជាប់នីមួយទៅមួយមុន។ |
| `04_resigned_receipt.json` | ដូចគ្នាក្នុងឯកសារទទួលដែលត្រូវបានរំខានហើយបន្ទាប់មកបានចុះហត្ថលេខាឡើងវិញដោយអ្នកវាយប្រហារ ជាមួយកូនសោសាធារណៈរបស់អ្នកវាយប្រហារដែលបានបញ្ចូល។ វាបញ្ជាក់ផ្ទៀងផ្ទាត់ចំពោះកូនសោក្នុងវា។ មិនបានជាប់ជាមួយកូនសោរបស់អ្នកចេញផ្សាយ។ |

គំរូទទួលភ្ជាប់ចុះហត្ថលេខាដោយផ្ទាល់លើបៃ JCS ផ្លូវការរបស់ផ្ទុកទិន្នន័យដោយប្រើ Ed25519។
SHA-256 ត្រូវបានប្រើនៅសម្រាប់សង្ខេបមាតិកានិងតំណភ្ជាប់ខ្សែឯកសារទទួល មិនមែនជាការផ្ដល់ចំនួនគម្រប៊ូជាមុនសម្រាប់ចុះហត្ថលេខា។
​

## ការបញ្ជាក់ទ្ញើរគំរូទទួល

នៅក្នុង `18-signed-receipts.ipynb`, រត់ Setup និងផ្នែកទី 1 រហូតដល់ 3 ជាមុន។
ផ្នែកទី 3 កំណត់ `verify_chain`; ផ្នែកទី 1 និង 2 ប៉ុណ្ណោះមិនគ្រប់គ្រាន់ទេ។
បន្ទាប់មករត់ប្លុកខាងក្រោមនៅក្នុងកោសិកាថ្មី មួយដោយមានថតការងាររបស់សៀវភៅកំណត់ត្រា
ត្រូវបានកំណត់ទៅ `18-securing-ai-agents/code_samples`។ ផ្លូវជា fixture ខាងក្រោមគឺជាផ្លូវទាក់ទង
ទៅកាន់ថតនោះ។

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

### ការត្រួតពិនិត្យឧទាហរណ៍ដោយគ្មាន Jupyter

ចាប់ផ្តើមពីធ្វើទីតាំងមូលដ្ឋាននៃឃ្លាំង សូមដំឡើងការពឹងផ្អែកនៃមេរៀន ហើយរត់:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ការប្រឡងទាំងនេះអនុវត្តឧទាហរណ៍ Python របស់សៀវភៅកំណត់ត្រា និងប្លុក README ត្រង់
ខាងលើ។ ពួកវាក៏ពិនិត្យមើលថាការបំភាន់ និងកូនសោមិនត្រូវបានចុះបញ្ជីត្រូវបានបដិសេធដោយ
អ្នកផ្ទៀងផ្ទាត់ផងដែរ។ ការប្រឡងមិនចូលរួមជាសាធារណៈក្នុងកោសិកា `%pip` របស់សៀវភៅកំណត់ត្រា
ព្រោះកាតព្វកិច្ចត្រូវបានដំឡើងផ្សេងពីគ្នា។ ពួកវាមិនប្ដូរសៀវភៅកំណត់ត្រាឬឧបករណ៍ភូតទេ។

## របៀបដែលវាត្រូវបានបង្កើត

ឧបករណ៍ភូតប្រើផ្លូវកូដដូចសៀវភៅកំណត់ត្រា ជាមួយកូនសោចុះហត្ថលេខាមួយជាប់ខ្ទើយ
និងពេលវេលាដែលដាក់ជាក់លាក់ទៅសម្រាប់ការចំណារវិញតាមបែបបៃតង។ ដើម្បីបង្កើតឡើងវិញៈ

```bash
python3 generate_fixtures.py
```

(កូដស្គ្រីបត្រូវមាននៅក្នុង `generate_fixtures.py` ក្នុងផ្ទាំងនេះ។)

`../test_signed_receipts.py` ពិនិត្យឲ្យឃើញទាំងនេះដោយស្វ័យប្រវត្តិ៖ វាអនុវត្ត
កូដសៀវភៅកំណត់ត្រា ពិនិត្យឧបករណ៍ភូតទាំងបួនទាំងនេះជាមួយនឹង
`verify_receipt` និង `verify_chain` របស់សៀវភៅកំណត់ត្រា ហើយបញ្ជាក់ថាការបង្កើត
ឧបករណ៍ភូតឡើងវិញឲ្យបានប្រាប់ជាបៃតមុខស្មើគ្នា។ ពី `code_samples`៖

```bash
python -m unittest test_signed_receipts
```

## អ្វីដែលសិស្សរៀនពីការត្រួតពិនិត្យ JSON ដើម

ការអានទ្រង់ទ្រាយប័ន្ទដើមបង្កើតការយល់ដឹងថាកោសិកានៅក្នុងសៀវភៅកំណត់ត្រា
មិនអាចផ្តល់បានជានិច្ចទេ។ សិស្សដែលប្រហែលមើល JSON ជាញឹកញាប់គឺនឹងចាប់អារម្មណ៍ថា៖

1. ហត្ថលេខាជាសរសេរបែប base64url មិនអាចយល់បាន ប៉ុន្តាលើវាលផ្សេងទាំងអស់មាន JSON ដែលអាចអានបានជាធម្មតា។
   ហត្ថលេខាមិនបានបង្ហាញខ្លួនក្នុងការអ៊ិនគ្រីបមាតិកា ទេ វាបញ្ជាក់ទៅលើវា។
2. `public_key` ត្រូវបានបញ្ចូលនៅក្នុងប័ន្ទ ដែលធ្វើឲ្យឯកសារទាំងមូលគ្នា
   ប៉ុន្តែមិនមែនជាអ្វីដែលអ្នកត្រួតពិនិត្យបញ្ជាក់ទេ។ ប្រៀបធៀបទៅ
   `02_tampered_receipt.json` ជាមួយ `04_resigned_receipt.json`៖ ទាំងពីរបាន
   ត្រូវបានកែប្រែក្រោយការចុះហត្ថលេខា ប៉ុន្តែទីពីរត្រូវបានចុះហត្ថលេខាទៀតដោយកូនសោរបស់អ្នកវាយប្រហារ
   ដូច្នេះវាស្ថិតនៅក្រោមការផ្ទៀងផ្ទាត់ទៅលើកូនសោដែលវាអាចផ្ដល់បាន។ កូនសោដែលបញ្ចូល
   ថ្ងៃនេះនិយាយឲ្យអ្នកដឹងថា ឯកសារនេះមានភាពសមហេតុផលពីខាងក្នុង។ គ្រាន់តែបានកូនសោ
   មកពីកន្លែងផ្សេងទៀតបង្ហាញថាអ្នកណាជាអ្នកចេញផ្សាយវា។
3. ការផ្លាស់ប្ដូរអក្សរតែមួយលើវាលណាមួយក្រៅពី `signature` បន្ទាប់មក
   ប្រៀបធៀបឯកសារនេះជាមួយ `02_tampered_receipt.json` ធ្វើឲ្យ
   ឧបករណ៍តម្រុយតាមកម្រិតបៃតមកកាន់ភាពច្បាស់លាស់។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->