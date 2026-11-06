# គំរូឯកសារទទួល

ឯកសារទទួលបានបង្កើតជាមុនចំនួនបីសម្រាប់ពិនិត្យដោយមិនចាំបាច់រត់ notebook។

| ឯកសារ | វាជាអ្វី |
|---|---|
| `01_valid_receipt.json` | ឯកសារទទួលបានចុះហត្ថលេខាត្រឹមត្រូវសម្រាប់ការហៅឧបករណ៍ `lookup_flights`។ ការផ្ទៀងផ្ទាត់បង្ហាញថា True។ |
| `02_tampered_receipt.json` | ឯកសារទទួលដដែលដែលបានកែប្រែវាលមួយបន្ទាប់ពីចុះហត្ថលេខា។ ការផ្ទៀងផ្ទាត់បង្ហាញថា False។ |
| `03_chain_three_receipts.json` | ខ្សែតំណរបស់ឯកសារទទួលត្រឹមត្រូវបី (ស្វែងរក, មៀង, កក់) ដែលមាន `previous_receipt_hash` ភ្ជាប់ក្នងនីមួយៗទៅនឹងមួយមុន។ |

គំរូទទួលចុះហត្ថលេខាលើបៃ JCS canonical នៃ payload ដោយផ្ទាល់ជាមួយ Ed25519។
SHA-256 បន្តត្រូវបានប្រើសម្រាប់ digest មាតិការនិងតំណខ្សែឯកសារទទួលមិនមែនជាមុន hash បន្ថែមមុនចុះហត្ថលេខា។


## ការផ្ទៀងផ្ទាត់គំរូ

ក្នុង `18-signed-receipts.ipynb`, ប្រតិបត្តិ Setup និងផ្នែក 1 រហូតដល់ 3 ជាមុន។
ផ្នែក 3 កំណត់ `verify_chain`; ផ្នែក 1 និង 2 តែម្ដងមិនគ្រប់គ្រាន់ឡើយ។
បន្ទាប់មករត់ប្លុកខាងក្រោមក្នុងសែលថ្មីមួយ ដោយឲ្យថតធ្វើការ
របស់សៀវភៅកំណត់ជា `18-securing-ai-agents/code_samples`។ ផ្លូវឆែកខាងក្រោម
គឺប្រៀបទៅតាមថតនោះ។

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

### ការត្រួតពិនិត្យឧទាហរណ៍ដោយគ្មាន Jupyter

ពីឫសរ៉េប៉ូស៊ីតូរី សូមដំឡើងអាស្រ័យការពីមេរៀនហើយរត់៖

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ការប្រឡងទាំងនេះដំណើរការឧទាហរណ៍ Python ក្នុងសៀវភៅកំណត់ និងប្លុក README ពិតប្រាកដ
ខាងលើ។ ពួកវាក៏ពិនិត្យផងដែរថាការប្រែក្លាយនិងក្តារចុចដែលមិនបានតំរូវក៏ត្រូវបានបដិសេធដោយ
អ្នកផ្ទៀងផ្ទាត់។ ការធ្វើតេស្តជៀសវាងកោសិការដំឡើង `%pip` នៃកំណត់ត្រា ព្រោះការពឹងផ្អែក
ត្រូវបានដំឡើងដោយឡែក។ ពួកវាមិនបម្លែងកំណត់ត្រា ឬឧបករណ៍នានាទេ។

## របៀបដែលវាត្រូវបានបង្កើត

ឧបករណ៍ប្រើពណ៌ណនារបៀបកូដដូចគ្នានឹងកំណត់ត្រា ជាមួយគន្លឹះចុះហត្ថលេខាមួយដែលបានកំណត់រួច
ហើយមានកាលបរិច្ឆេទថេរសម្រាប់សំណាក់ត្រឹមត្រូវឲ្យអាចបង្កប់ឡើងវិញបែបបាយប៊ែរទេខេ។ ដើម្បីបង្កប់ឡើងវិញ៖

```bash
python3 generate_fixtures.py
```

(ស្គ្រីបនៅក្នុង `generate_fixtures.py` នៅក្នុងថតនេះ។)

## អ្វីដែលសិស្សរៀនពីការត្រួតពិនិត្យ JSON កំប្លែង

ការអានទម្រង់បញ្ចូលសំរឹទ្ធដើមធ្វើឱ្យមានការយល់ដឹងដែលប្រអប់នៅក្នុងកំណត់ត្រា
មិនបានផ្តល់ជានិច្ច។ សិស្សដែលអានជុល JSON ជាញឹកញាប់គឺសង្កត់សម្គាល់ថា៖

1. ហត្ថលេខាគឺជាសម្មញ្ញា base64url ដែលមិនច្បាស់លាស់, ប៉ុន្តែពេលវេលាផ្សេងទៀតគឺឯកសារសាមញ្ញ
   JSON ដែលអាចអានបាន។ လက္សញ្ញា​មិន​បាន​ស៊ុម​ខ្សែរ​អត្ថបទ​នោះទេ; វា​បញ្ជាក់​អំពី​វា។
2. `public_key` ត្រូវបាន​បញ្ចូល​នៅ​ក្នុង​អត្រា ដែលគប់គ្រប់គ្រាន់សម្រាប់ត្រួតពិនិត្យ
   ភាពដើមទ្រូងមិនខ្វះខាត ប៉ុន្ដែមិនមែនជាវិជ្ជមាននឿយហត្ថី។ អ្នកត្រួតពិនិត្យត្រូវតែប្រៀបធៀបទៅនឹងកូនសោមួយ
   ដែលត្រូវបានចងខ្សែក្រវាត់ពីក្រៅអត្រា ឬក៏ត្រូវបានដោះស្រាយតាមរយៈកំណត់ត្រាទំនុកចិត្ត។
3. ការផ្លាស់ប្តូរអក្សរតែមួយក្នុងក្រងបទណាមួយ បន្ទាប់មកប្រៀបធៀបឯកសារនេះម្ដងទៀតជាមួយ
   `02_tampered_receipt.json` ធ្វើឲ្យដំណើរការដោយកម្រិតបៃនេះក្លាយជាការពិត។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->