# عينات الإيصالات

ثلاثة ملفات إيصالات مولدة مسبقًا للفحص بدون تشغيل الدفتر.

| الملف | ما هو |
|---|---|
| `01_valid_receipt.json` | إيصال صالح موقع لمكالمة أداة `lookup_flights`. التحقق يرجع True. |
| `02_tampered_receipt.json` | نفس الإيصال مع تعديل حقل واحد بعد التوقيع. التحقق يرجع False. |
| `03_chain_three_receipts.json` | سلسلة من ثلاثة إيصالات صالحة (بحث، احتجاز، حجز) مع `previous_receipt_hash` تربط كل منها بالسابق. |

تقوم العينات بالتوقيع مباشرة على بايتات JCS القانونية للحمل باستخدام Ed25519.
تبقى SHA-256 مستخدمة لهضم المحتوى وروابط سلسلة الإيصالات، وليس كـ
هضم مسبق إضافي قبل التوقيع.

## التحقق من العينات

في `18-signed-receipts.ipynb`، قم بتشغيل الإعداد والأقسام من 1 إلى 3 أولاً.
القسم 3 يعرف `verify_chain`؛ الأقسام 1 و2 وحدهما غير كافيين.
ثم شغّل الكتلة التالية في خلية جديدة، مع ضبط دليل العمل للدفتر
إلى `18-securing-ai-agents/code_samples`. مسارات العينات أدناه نسبية
لذلك الدليل.

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

### التحقق من المثال بدون Jupyter

من جذر المستودع، قم بتثبيت اعتماديات الدرس وتشغيل:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

تنفذ هذه الاختبارات أمثلة بايثون للدفتر وكتلة README الدقيقة
أعلاه. كما تتحقق من رفض التلاعب والمفاتيح غير المثبتة من قبل
المدققين. تتخطى الاختبارات خلية الإعداد `%pip` الخاصة بالدفتر لأن الاعتماديات
مثبتة بشكل منفصل. لا تغير الدفاتر أو العينات.

## كيف تم توليد هذه العينات

تستخدم العينات نفس مسار الكود كالدفتر، مع مفتاح توقيع ثابت
وطوابع زمنية ثابتة لإعادة إنتاجية البايت. لإعادة التوليد:

```bash
python3 generate_fixtures.py
```

(السكربت موجود في `generate_fixtures.py` ضمن هذا الدليل.)

## ما يتعلمه الطلاب من فحص JSON الخام

قراءة صيغة الإيصال الخام تبني حدسًا لا توفره الخلايا في الدفتر دائمًا.
غالبًا ما يلاحظ الطلاب الذين يتصفحون JSON:

1. التوقيع هو سلسلة مشفرة بالقاعدة64url غامضة، لكن كل حقل آخر هو JSON
   واضح للقراءة. التوقيع لا يشفر المحتوى؛ بل يشهد عليه.
2. `public_key` مضمن في الإيصال، وهذا كافٍ لفحص
   الاتساق الذاتي لكن ليس الثقة بإصدار الإيصال. يجب على المدقق مقارنته بمفتاح
   مثبت خارج الإيصال أو يتم حله عبر سجل موثوق.
3. تعديل حرف واحد في أي حقل، ثم إعادة مقارنة هذا الملف مع
   `02_tampered_receipt.json` يجعل آلية مستوى البايت ملموسة.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->