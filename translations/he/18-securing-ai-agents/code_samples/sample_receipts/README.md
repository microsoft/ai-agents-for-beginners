# אביזרי דוגמת קבלה

שלושה קבצי קבלות שנוצרו מראש לבדיקה ללא הפעלת המחברת.

| קובץ | מה זה |
|---|---|
| `01_valid_receipt.json` | קבלה חתומה תקינה עבור קריאה לכלי `lookup_flights`. אימות מחזיר True. |
| `02_tampered_receipt.json` | אותה קבלה עם שדה אחד ששונה לאחר החתימה. אימות מחזיר False. |
| `03_chain_three_receipts.json` | שרשרת של שלוש קבלות תקינות (חיפוש, השהייה, הזמנה) עם `previous_receipt_hash` שמקשר כל אחת לקודמתה. |

## אימות הדוגמאות

המחברת ממקדת את האימות בארבעה חלקים. כדי לאמת את האביזרים האלה
ישירות ללא הרצת הסיפור במחברת:

```python
import json
from pathlib import Path

# מניח שסיימת את הייבוא והפונקציות המסייעות
# מחלקים 1 ו-2 של 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # נכון

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # לא נכון

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## כיצד הן נוצרו

האביזרים משתמשים באותו מסלול קוד כמו במחברת, עם מפתח חתימה קבוע
וטיימסטמפים קבועים לשחזור סיביות זהה. ליצירה מחדש:

```bash
python3 generate_fixtures.py
```

(התסריט נמצא ב- `generate_fixtures.py` בתיקיה זו.)

## מה התלמידים לומדים מסקירת JSON גולמי

קריאת פורמט הקבלה הגולמי בונה אינטואיציה שהתאים במחברת
לא תמיד מספקים. תלמידים שמחליקים על ה-JSON לעיתים שמים לב ל:

1. החתימה היא מחרוזת בסיס64url אטומה, אך כל שאר השדות הם JSON קריא פשוט.
   החתימה אינה מצפינה את התוכן; היא מאשרת אותו.
2. ה-`public_key` מוטמע בקבלה. מבקר לא צריך דבר נוסף
   כדי לאמת (בתנאי לסמוך שהמפתח שייך באמת למנפיק הטעון;
   ראו את קובץ ה-README של השיעור על תשתית זהות).
3. שינוי תו יחיד בכל שדה, ואז השוואת הקובץ הזה עם
   `02_tampered_receipt.json`, מבהיר את המנגנון ברמת הסיביות.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->