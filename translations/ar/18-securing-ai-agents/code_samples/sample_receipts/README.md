# أمثلة على الإيصالات النموذجية

ثلاثة ملفات إيصالات مولدة مسبقًا للفحص دون الحاجة لتشغيل الدفتر.

| الملف | ما هو |
|---|---|
| `01_valid_receipt.json` | إيصال موقع صالح لاستدعاء أداة `lookup_flights`. التحقق يرجع True. |
| `02_tampered_receipt.json` | نفس الإيصال مع تعديل حقل واحد بعد التوقيع. التحقق يرجع False. |
| `03_chain_three_receipts.json` | سلسلة من ثلاث إيصالات صالحة (بحث، تعليق، حجز) مع `previous_receipt_hash` تربط كل منها بالسابق. |

تقوم الأمثلة بتوقيع بايتات JCS الموحدة للعبء مباشرة بواسطة Ed25519.
تبقى SHA-256 مستخدمة لهضم المحتوى ورابط سلسلة الإيصالات، وليست
كهاش مسبق إضافي قبل التوقيع.

## التحقق من العينات

يشرح الدفتر عملية التحقق في أربعة أقسام. للتحقق من هذه الأمثلة
مباشرة دون المرور بسرد الدفتر:

```python
import json
from pathlib import Path

# Assumes you have completed the imports and helper functions
# from sections 1 and 2 of 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # True

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # False

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## كيف تم توليد هذه

تستخدم الأمثلة نفس مسار الكود الخاص بالدفتر، مع مفتاح توقيع ثابت
وطوابع زمنية ثابتة لضمان استنساخ البايتات. لإعادة التوليد:

```bash
python3 generate_fixtures.py
```

(السكريبت موجود في `generate_fixtures.py` في هذا الدليل.)

## ما يتعلمه الطلاب من فحص JSON الخام

قراءة تنسيق الإيصال الخام تبني الحدس الذي لا توفره دائمًا الخلايا في الدفتر.
غالبًا ما يلاحظ الطلاب الذين يتصفحون JSON بسرعة:

1. التوقيع هو سلسلة base64url غامضة، لكن كل الحقول الأخرى JSON عادي
   قابل للقراءة. التوقيع لا يشفر المحتوى؛ بل يشهد عليه.
2. `public_key` مضمّن في الإيصال. لا يحتاج المدقق إلى أي شيء آخر
   للتحقق (بشرط الثقة في أن المفتاح ينتمي فعلاً للجهة المصدرّة المدعاة؛
   راجع README الدرس حول بنية الهوية).
3. تعديل حرف واحد في أي حقل، ثم إعادة مقارنة هذا الملف مع
   `02_tampered_receipt.json`، يجعل آلية مستوى البايت واضحة.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->