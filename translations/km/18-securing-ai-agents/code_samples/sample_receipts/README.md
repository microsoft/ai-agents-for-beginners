# Sample Receipt Fixtures

Three pre-generated receipt files for inspection without running the notebook.

| File | What it is |
|---|---|
| `01_valid_receipt.json` | វា​ជា​វិទ្យាសាស្ត្រ​ដែល​បាន​ចុះ​ហត្ថលេខា​ត្រឹមត្រូវ​សម្រាប់​ការ​ស៊ើបអង្កេត​ហោះហើរ `lookup_flights` ។ ការ​ផ្ទៀងផ្ទាត់​បាន​ទទួល​ប្រសិទ្ធភាព។ |
| `02_tampered_receipt.json` | វា​ជា​វិទ្យាសាស្ត្រ​ដូចគ្នា​ដែល​មាន​វាល​មួយ​បាន​ផ្លាស់ប្តូរ​បន្ទាប់​ពី​បាន​ចុះ​ហត្ថលេខា។ ការ​ផ្ទៀងផ្ទាត់​បាន​ស្ទួន។ |
| `03_chain_three_receipts.json` | ច្រវាក់​នៃ​វិទ្យាសាស្ត្រ​ត្រឹមត្រូវ​បី​រក្សា (ស្វែងរក ការកាន់ ការកក់) ជាមួយ `previous_receipt_hash` តភ្ជាប់​មួយ​នីមួយៗ​ទៅ​នឹង​មុន។ |

## Verifying the samples

The notebook walks through verification in four sections. To verify these fixtures
directly without running through the notebook narrative:

```python
import json
from pathlib import Path

# សន្មត់ថាអ្នកបានបញ្ចប់ការនាំចូលនិងមុខងារជួយរួចរាល់ហើយ
# ពីផ្នែក 1 និង 2 នៃ 18-signed-receipts.ipynb។

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # ពិត

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # មិនពិត

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## How these were generated

The fixtures use the same code path as the notebook, with one fixed signing key
and fixed timestamps for byte-reproducibility. To regenerate:

```bash
python3 generate_fixtures.py
```

(Script is at `generate_fixtures.py` in this directory.)

## What students learn from inspecting raw JSON

Reading the raw receipt format builds intuition that the cells in the notebook
do not always provide. Students who skim the JSON often notice:

1. ប្រស្នា​ជា​សញ្ញា​មូលដ្ឋាន64url ដែលមិនច្បាស់លាស់ ប៉ុន្តែ​វាល​ទាំងអស់​ផ្សេង​ទៀត​ជា JSON ដែលអាន​ងាយ។ សញ្ញា​មិន​បញ្ជូន​កូដ មិន​អ៊ិនគ្រីបមាតិកា​ទេ វាធានា​អំពីវា។
2. `public_key` ត្រូវបាន​បញ្ចូលក្នុង​វិទ្យាសាស្ត្រ។ អ្នកត្រួតពិនិត្យមិន​ត្រូវការអ្វី​បន្ថែម​ដើម្បីផ្ទៀងផ្ទាត់ (ដោយមានលក្ខខណ្ឌ​ថា​ជំនឿថា​កូនសោ​នេះ​សព្វថ្ងៃ​យល់ព្រម​ឲ្យ​ដោយ​អ្នកចេញផ្សាយ​ផ្ទាល់ខ្លួន; មាន​ពុម្ព​បទ README ស្ដីអំពី​រោងចក្រ​អត្តសញ្ញាណ)។
3. ការផ្លាស់ប្តូរតួអក្សរ​តែមួយ​ក្នុង​វាលណាមួយ បន្ទាប់ពី​ប្រៀបធៀប​ឯកសារ​នេះ​ជាមួយ `02_tampered_receipt.json` ធ្វើឲ្យ​គ្រប់ប្រព័ន្ធ​ប្លែក​ផ្ទាល់ច្បាស់លាស់។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->