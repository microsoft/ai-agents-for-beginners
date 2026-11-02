# דוגמאות קבלות לדוגמה

שלושה קבצים של קבלות שנוצרו מראש לצורך בדיקה ללא הרצת המחברת.

| קובץ | מה זה |
|---|---|
| `01_valid_receipt.json` | קבלה תקפה וחתומה לשימוש בכלי `lookup_flights`. אימות מחזיר True. |
| `02_tampered_receipt.json` | אותה קבלה עם שדה אחד ששונָה אחרי החתימה. אימות מחזיר False. |
| `03_chain_three_receipts.json` | שרשרת של שלוש קבלות תקפות (חיפוש, החזקה, הזמנה) עם `previous_receipt_hash` שמקשר כל אחת לזו הקודמת. |

הדוגמאות חותמות את הבייטים הקאנוניים של JCS בפיילוד ישירות בעזרת Ed25519.
SHA-256 נשאר בשימוש לעיכול תוכן ולקישורי שרשרת הקבלות, לא כ-
חישוב מקדים נוסף לפני החתימה.

## אימות הדוגמאות

המחברת מציגה את תהליך האימות בארבעה חלקים. לאימות הדוגמאות האלה
ישירות ללא הרצה של הסיפור במחברת:

```python
import json
from pathlib import Path

# מניח שסיימת את הייבוא והפונקציות העזר
# מהחלקים 1 ו-2 של 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # נכון

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # לא נכון

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## איך הן נוצרו

הדוגמאות משתמשות באותו מסלול קוד כמו המחברת, עם מפתח חתימה אחד קבוע
וחותמות זמן קבועות לשחזור בתים. ליצירה מחדש:

```bash
python3 generate_fixtures.py
```

(הסקריפט נמצא ב-`generate_fixtures.py` בתיקייה זו.)

## מה הסטודנטים לומדים בבדיקת JSON גולמי

קריאת פורמט הקבלה הגולמי מפתחת אינטואיציה שלפעמים התאים במחברת
אינם מספקים. סטודנטים הסורקים את ה-JSON לעיתים מבחינים ב:

1. החתימה היא מחרוזת base64url לא שקופה, אך כל שדה אחר הוא JSON קריא
   פשוט. החתימה אינה מצפינה את התוכן; היא מאשרת אותו.
2. `public_key` מוטמע בקבלה. מבקר לא צריך דבר נוסף
   לאימות (בתנאי שמהימנים שהמפתח שייך למנפיק המוצהר;
   ראה את הדרכת ה-README בנושא תשתיות זהות).
3. שינוי תו יחיד בכל שדה, ואז השוואה מחודשת עם
   `02_tampered_receipt.json`, עושה את המנגנון ברמת הבייטים למוחשי.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->