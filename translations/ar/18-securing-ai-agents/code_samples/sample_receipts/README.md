# عينات إيصال نموذجية

أربعة ملفات إيصال مُعدة مسبقًا لمراجعتها بدون تشغيل دفتر الملاحظات.

| الملف | ما هو |
|---|---|
| `01_valid_receipt.json` | إيصال صالح موقع لاستدعاء أداة `lookup_flights`. التحقق يُرجع صحيح. |
| `02_tampered_receipt.json` | نفس الإيصال مع تعديل حقل واحد بعد التوقيع. التحقق يُرجع خطأ. |
| `03_chain_three_receipts.json` | سلسلة من ثلاث إيصالات صالحة (بحث، حجز مؤقت، حجز) مع `previous_receipt_hash` تربط كل منها بالسابقة. |
| `04_resigned_receipt.json` | نفس الإيصال تم التلاعب به ثم إعادة توقيعه بواسطة مهاجم، مع تضمين المفتاح العام الخاص بالمهاجم. يتحقق مقابل المفتاح داخل الإيصال. يفشل مقابل مفتاح المُصدر. |

العينات توقع بايتات JCS الكنسي للحمولة مباشرة باستخدام Ed25519.
SHA-256 يُستخدم للبصمات المحتوى وروابط سلسلة الإيصالات، وليس كـ
هاش مسبق إضافي قبل التوقيع.

## التحقق من العينات

في `18-signed-receipts.ipynb`، شغل قسم الإعداد والأقسام من 1 إلى 3 أولًا.
يعرّف القسم 3 `verify_chain`؛ الأقسام 1 و 2 فقط غير كافية.
ثم شغل الكتلة التالية في خلية جديدة، مع تعيين دليل العمل لدفتر الملاحظات
إلى `18-securing-ai-agents/code_samples`. مسارات العينات أدناه نسبية
لذلك الدليل.

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

### التحقق من المثال بدون Jupyter

من جذر المستودع، ثبّت تبعيات الدرس وشغل:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

تنفذ هذه الاختبارات أمثلة بايثون من دفتر الملاحظات والكتلة الدقيقة من README
أعلاه. كما تتحقق من أن التلاعب والمفاتيح غير المثبتة يتم رفضها من قِبل
المحققات. تتخطى الاختبارات خلية إعداد `%pip` في دفتر الملاحظات لأن التبعيات
مُثبتة بشكل منفصل. ولا تغير دفتر الملاحظات أو العينات.

## كيف تم توليد هذه العينات

تستخدم العينات نفس مسار الكود في دفتر الملاحظات، مع مفتاح توقيع ثابت
وطوابع زمنية ثابتة لإعادة إنتاج بايتات متطابقة. لإعادة التوليد:

```bash
python3 generate_fixtures.py
```

(النص البرمجي في `generate_fixtures.py` في هذا الدليل.)

`../test_signed_receipts.py` يتحقق من كل هذا تلقائيًا: يشغل
كود دفتر الملاحظات، يتحقق من هذه الأربع عينات مع دفتر الملاحظات
`verify_receipt` و `verify_chain`، ويؤكد أن إعادة توليد
العينات تعطي بايتات متطابقة. من `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## ما يتعلمه الطلاب من فحص JSON الخام

قراءة شكل الإيصال الخام تبني حدسًا لا توفره خلايا دفتر الملاحظات دائمًا.
غالبًا ما يلاحظ الطلاب الذين يتصفحون JSON:

1. التوقيع هو سلسلة شفافة Base64url، لكن كل حقل آخر JSON قابل
   للقراءة بشكل واضح. التوقيع لا يشفر المحتوى؛ بل يشهد عليه.
2. `public_key` مضمن في الإيصال، مما يجعل الملف
   مكتفيًا ذاتيًا لكنه ليس ما يتحقق منه المدقق. قارن
   `02_tampered_receipt.json` مع `04_resigned_receipt.json`: كلاهما
   تم تعديله بعد التوقيع، لكن الثاني أعيد توقيعه بمفتاح
   المهاجم الخاص، لذا يتحقق مقابل المفتاح الموجود بداخله. المفتاح المضمن
   يخبرك أن الملف متناسق داخليًا. فقط مفتاح تم الحصول عليه
   من مكان آخر يخبرك بمن أصدره.
3. تعديل حرف واحد فقط من أي حقل خارج `signature`، ثم
   إعادة مقارنة هذا الملف مع `02_tampered_receipt.json`، يجعل الآلية
   على مستوى البايتات ملموسة.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->