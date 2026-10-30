# نمونہ رسید کے فکسچرز

تین پیشگی تیار شدہ رسید فائلیں بغیر نوٹ بک چلائے معائنہ کے لیے۔

| فائل | یہ کیا ہے |
|---|---|
| `01_valid_receipt.json` | ایک صحیح دستخط شدہ رسید `lookup_flights` ٹول کال کے لیے۔ تصدیق True لوٹاتی ہے۔ |
| `02_tampered_receipt.json` | دستخط کے بعد ایک فیلڈ تبدیل کی گئی اسی رسید۔ تصدیق False لوٹاتی ہے۔ |
| `03_chain_three_receipts.json` | تین درست رسیدوں کی زنجیر (search, hold, book) جن میں `previous_receipt_hash` ہر ایک کو پچھلی سے جوڑتا ہے۔ |

فکسچرز لوڈ کی جے سی ایس کے کینونیکل بائٹس کو براہ راست Ed25519 سے دستخط کرتے ہیں۔
SHA-256 مواد کے خلاصوں اور رسید زنجیر کے روابط کے لیے استعمال ہوتا رہتا ہے، دستخط سے پہلے اضافی پری ہیش کے طور پر نہیں۔


## نمونوں کی تصدیق

`18-signed-receipts.ipynb` میں، پہلے Setup اور سیکشن 1 سے 3 چلائیں۔
سیکشن 3 میں `verify_chain` کی تعریف کی گئی ہے؛ صرف سیکشن 1 اور 2 کافی نہیں ہیں۔
پھر نیچے والا بلاک ایک نئے سیل میں چلائیں، اور نوٹ بک کے ورکنگ ڈائریکٹری کو
`18-securing-ai-agents/code_samples` پر سیٹ کریں۔ نیچے فکسچر راستے اس ڈائریکٹری کے مطابق ہیں۔


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

### جیوپیٹر کے بغیر مثال کی جانچ

ریپوزیٹری کے روٹ سے، سبق کی انحصاریوں کو انسٹال کریں اور چلائیں:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

یہ ٹیسٹ نوٹ بک کے پائتھن مثالیں اور بالکل اوپر README بلاک کو اجرا کرتے ہیں۔
یہ یہ بھی چیک کرتے ہیں کہ چھیڑ چھاڑ اور ان پن کیے ہوئے کیز کو جانچنے والے مسترد کردیتے ہیں۔
ٹیسٹ نوٹ بک کے `%pip` سیٹ اپ سیل کو چھوڑ دیتے ہیں کیونکہ انحصار الگ سے انسٹال ہوتے ہیں۔
یہ نوٹ بک یا فکسچرز کو تبدیل نہیں کرتے۔

## یہ کس طرح تیار کیے گئے تھے

فکسچرز نوٹ بک کی وہی کوڈ راہ استعمال کرتے ہیں، ایک مقررہ دستخطی کلید
اور بائٹ کی بازپیدائش کے لیے مقررہ وقت کے ساتھ۔ دوبارہ تیار کرنے کے لیے:

```bash
python3 generate_fixtures.py
```

(اسکرپٹ اس ڈائریکٹری میں `generate_fixtures.py` پر ہے۔)

## طالب علم خام JSON کا معائنہ کرکے کیا سیکھتے ہیں

خام رسیدی فارمیٹ پڑھنا وہ سمجھ بوجھ پیدا کرتا ہے جو نوٹ بک میں موجود سیلز ہمیشہ فراہم نہیں کرتے۔
طلباء جو JSON کو تیزی سے دیکھتے ہیں اکثر نوٹس کرتے ہیں:

1۔ دستخط ایک مبہم base64url سٹرنگ ہے، لیکن ہر اور فیلڈ سادہ پڑھنے کے قابل JSON ہے۔
   دستخط مواد کو خفیہ نہیں کرتا؛ یہ اس کی تصدیق کرتا ہے۔
2۔ `public_key` رسید میں شامل ہے، جو خود-مطابقت کی جانچ کے لیے کافی ہے لیکن اجرا کنندہ پر اعتماد کے لیے نہیں۔
   ایک آڈیٹر کو اسے رسید کے باہر پن کی گئی کلید کے ساتھ موازنہ کرنا ہوگا
   یا معتبر رجسٹری کے ذریعے حل شدہ کلید کے ساتھ۔
3. کسی بھی فیلڈ کے ایک کردار میں ترمیم کرنا، پھر اس فائل کا دوبارہ موازنہ کرنا
   `02_tampered_receipt.json`، بائٹ-لیول میکانزم کو واضح کرتا ہے۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->