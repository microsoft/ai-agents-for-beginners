# عينات إيصالات جاهزة

ثلاثة ملفات إيصالات مولدة مسبقًا للفحص دون تشغيل الدفتر.

| الملف | ما هو |
|---|---|
| `01_valid_receipt.json` | إيصال صالح موقع لاستدعاء أداة `lookup_flights`. تُرجع عملية التحقق True. |
| `02_tampered_receipt.json` | نفس الإيصال مع تعديل حقل واحد بعد التوقيع. تُرجع عملية التحقق False. |
| `03_chain_three_receipts.json` | سلسلة من ثلاثة إيصالات صالحة (بحث، احتجاز، حجز) مع `previous_receipt_hash` تربط كل منها بالتي قبلها. |

## التحقق من العينات

ينتقل الدفتر عبر التحقق في أربعة أقسام. للتحقق من هذه العينات
مباشرة دون المرور من خلال سير الدفتر:

```python
import json
from pathlib import Path

# يفترض أنك أكملت الاستيراد والدوال المساعدة
# من القسم 1 و 2 من ملف 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # صحيح

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # خطأ

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## كيف تم توليد هذه العينات

تستخدم العينات نفس مسار الكود في الدفتر، مع مفتاح توقيع واحد ثابت
وطوابع زمنية ثابتة لإعادة إنتاج الحروف البايتية. لإعادة التوليد:

```bash
python3 generate_fixtures.py
```

(السكريبت في `generate_fixtures.py` في هذا الدليل.)

## ما يتعلمه الطلاب من فحص JSON الخام

قراءة تنسيق الإيصال الخام تبني حدسًا لا توفره خلايا الدفتر دائمًا. الطلاب الذين يتصفحون JSON غالبًا ما يلاحظون:

1. التوقيع هو سلسلة معتمة بصيغة base64url، ولكن كل الحقول الأخرى هي JSON نصي
   قابل للقراءة. التوقيع لا يشفر المحتوى؛ بل يشهد عليه.
2. مفتاح `public_key` مضمّن في الإيصال. المدقق لا يحتاج إلى شيء آخر
   للتحقق (رهناً بالثقة بأن المفتاح ينتمي فعلاً للجهة المصدرة المزعومة؛ راجع README الدرس حول بنية الهوية).
3. تعديل حرف واحد فقط في أي حقل، ثم إعادة مقارنة هذا الملف مع
   `02_tampered_receipt.json`، يجعل الآلية على مستوى البايت واضحة وملموسة.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->