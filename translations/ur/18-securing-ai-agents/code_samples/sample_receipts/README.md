# نمونہ رسید فکسچر

نوٹ بک چلائے بغیر معائنہ کے لیے چار پہلے سے تیار شدہ رسید فائلیں۔

| فائل | یہ کیا ہے |
|---|---|
| `01_valid_receipt.json` | ایک درست دستخط شدہ رسید برائے `lookup_flights` ٹول کال۔ توثیق True واپس کرتی ہے۔ |
| `02_tampered_receipt.json` | یہی رسید جس کا ایک فیلڈ دستخط کے بعد تبدیل کر دیا گیا ہے۔ توثیق False واپس کرتی ہے۔ |
| `03_chain_three_receipts.json` | تین درست رسیدوں کی زنجیر (search, hold, book)، جس میں `previous_receipt_hash` ہر ایک کو پچھلی والے سے منسلک کرتا ہے۔ |
| `04_resigned_receipt.json` | یہی رسید جو حملہ آور نے چھیڑی اور پھر دوبارہ دستخط کی، جس میں حملہ آور کی اپنی پبلک کی ایمبیڈ کی گئی ہے۔ یہ اُس میں موجود کلید کے خلاف توثیق ہوتی ہے۔ اجرا کنندہ کی کلید کے خلاف ناکام ہو جاتی ہے۔ |

فکسچر پے لوڈ کے معیاری JCS بائٹس کو براہِ راست Ed25519 سے دستخط کرتے ہیں۔
SHA-256 مواد کے ڈائجسٹ اور رسید چین لنکس کے لیے استعمال ہوتا رہتا ہے، بطور
اضافی pre-hash دستخط سے پہلے نہیں۔

## نمونوں کی تصدیق

`18-signed-receipts.ipynb` میں پہلے Setup اور سیکشن 1 تا 3 چلائیں۔
سیکشن 3 `verify_chain` کی تعریف کرتا ہے؛ صرف سیکشنز 1 اور 2 کافی نہیں ہیں۔
پھر نئی سیل میں مندرجہ ذیل بلاک چلائیں، نوٹ بک کی ورکنگ ڈائریکٹری
کو `18-securing-ai-agents/code_samples` پر سیٹ کریں۔ نیچے دیے گئے فکسچر راستے نسبتاً
اسی ڈائریکٹری کے ہیں۔

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

### Jupyter کے بغیر مثال کی جانچ

ریپوزٹری کے روٹ سے، سبق کے انحصارات انسٹال کریں اور چلائیں:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

یہ ٹیسٹ نوٹ بک کی Python مثالوں اور اوپر اسی README بلاک کو چلائیں گے۔
یہ یہ بھی چیک کرتے ہیں کہ چھیڑ چھاڑ اور غیر پن کی گئی کلیدیں توثیق کنندگان کے ذریعہ مسترد ہوں۔
یہ ٹیسٹ نوٹ بک کے `%pip` سیٹ اپ سیل کو اس لیے اسکِپ کرتے ہیں کیونکہ انحصارات
الگ سے انسٹال کیے جاتے ہیں۔ وہ نوٹ بک یا فکسچرز میں تبدیلی نہیں کرتے۔

## یہ کیسے بنائے گئے تھے

فکسچر نوٹ بک کے اسی کوڈ راستے کو استعمال کرتے ہیں، ایک مقررہ دستخطی کلید کے ساتھ
اور بائٹ-تکرارپذیری کے لیے مقررہ ٹائم اسٹیمپس۔ دوبارہ بنانے کے لیے:

```bash
python3 generate_fixtures.py
```

(اس اسکرپٹ کا مقام اس ڈائریکٹری میں `generate_fixtures.py` ہے۔)

`../test_signed_receipts.py` خودکار طور پر یہ سب چیک کرتا ہے: یہ
نوٹ بک کا کوڈ چلاتا ہے، ان چار فکسچرز کو نوٹ بک کے
`verify_receipt` اور `verify_chain` کے ساتھ تصدیق کرتا ہے، اور اس کی تصدیق کرتا ہے کہ فکسچر کو دوبارہ جنریٹ کرنے سے
وہی بائٹس ملتی ہیں۔ `code_samples` سے:

```bash
python -m unittest test_signed_receipts
```

## خام JSON کا معائنہ کر کے طلباء کیا سیکھتے ہیں

خام رسید فارمیٹ پڑھنے سے وہ سمجھ بوجھ بنتی ہے جو نوٹ بک کے سیلز ہمیشہ فراہم نہیں کرتے۔
وہ طلباء جو JSON کو جھَلک میں دیکھتے ہیں اکثر نوٹس کرتے ہیں:

1. دستخط ایک مبہم base64url سٹرنگ ہے، لیکن ہر دوسرا فیلڈ سیدھا
   قابلِ مطالعہ JSON ہوتا ہے۔ دستخط مواد کو خفیہ نہیں کرتا؛ یہ اس کی تصدیق کرتا ہے۔
2. `public_key` رسید میں ایمبیڈ ہوتا ہے، جو فائل کو
   خودمختار بناتا ہے مگر یہ وہ چیز نہیں ہے جس کے خلاف آڈیٹر توثیق کرتا ہے۔ مقابلہ کریں
   `02_tampered_receipt.json` کو `04_resigned_receipt.json` کے ساتھ: دونوں کو
   دستخط کے بعد تبدیل کیا گیا تھا، لیکن دوسرے پر حملہ آور نے دوبارہ دستخط کیے
   اپنی کلید کے ساتھ، لہٰذا یہ اس کلید کے خلاف توثیق ہوتا ہے جو یہ اپنے اندر رکھتا ہے۔ ایمبیڈ کی گئی کلید
   اپکو بتاتی ہے کہ فائل داخلی طور پر مطابقت رکھتی ہے۔ صرف وہ کلید جو کہیں اور حاصل کی گئی ہو
   آپ کو بتاتی ہے کہ اسے کس نے جاری کیا تھا۔
3. `signature` کے باہر کسی بھی فیلڈ کے ایک حرف میں ترمیم کرنا، پھر
اس فائل کا دوبارہ موازنہ `02_tampered_receipt.json` کے ساتھ،
بائٹ سطح کے میکانزم کو واضح کرتا ہے۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->