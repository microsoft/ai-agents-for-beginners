# דוגמאות קבלות לדוגמה

שלושה קבצי קבלה שנוצרו מראש לבדיקה מבלי להריץ את המחברת.

| קובץ | מה זה |
|---|---|
| `01_valid_receipt.json` | קבלה חתומה תקפה עבור קריאת הכלי `lookup_flights`. אימות מחזיר True. |
| `02_tampered_receipt.json` | אותה קבלה כאשר שונה שדה אחד לאחר החתימה. אימות מחזיר False. |
| `03_chain_three_receipts.json` | שרשרת של שלוש קבלות תקפות (חיפוש, החזקה, הזמנה) עם `previous_receipt_hash` שמקשר כל אחת לקודמתה. |

הדוגמאות חותמות את הביטים הקנוניים של JCS בפיילוד ישירות עם Ed25519.
SHA-256 ממשיך לשמש לעיכול תוכן ולקישורים בשרשרת הקבלות, לא
כמקרי-קדם נוסף לפני החתימה.

## אימות הדוגמאות

המחברת עוסקת באימות בארבעה חלקים. לאימות הדוגמאות האלו
ישירות מבלי לעבור על הסיפור במחברת:

```python
import json
from pathlib import Path

# מניח שסיימת את הייבוא והפונקציות העוזרות
# מחלקות 1 ו-2 של 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # נכון

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # לא נכון

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## כיצד נוצרו הדוגמאות

הדוגמאות משתמשות באותו מסלול קוד כמו המחברת, עם מפתח חתימה אחד קבוע
וטיימסטמפ קבוע לשחזור ביטים מדויק. ליצירה מחדש:

```bash
python3 generate_fixtures.py
```

(הסקריפט נמצא ב- `generate_fixtures.py` בתיקייה זו.)

## מה הסטודנטים לומדים מבדיקת JSON גולמי

קריאת פורמט הקבלה הגולמית מפתחת אינטואיציה שהמחברת לא תמיד מספקת. סטודנטים
שסוקרים את ה-JSON בדרך כלל שמים לב לכך:

1. החתימה היא מחרוזת base64url אטומה, אבל כל שדה אחר הוא JSON לקריאה
   פשוטה. החתימה אינה מצפינה את התוכן; היא מאשרת אותו.
2. `public_key` מוטמע בקבלה. מבקר אינו זקוק לשום דבר נוסף
   לאימות (בתנאי שהוא סומך שהמפתח אכן שייך לגורם
   שהוכרז; ראו את קובץ ה-README של השיעור על תשתית זהות).
3. שינוי תו אחד בכל שדה, ואז השוואה מחודשת של קובץ זה עם
   `02_tampered_receipt.json`, מבהירה את מנגנון רמת הבייטים.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->