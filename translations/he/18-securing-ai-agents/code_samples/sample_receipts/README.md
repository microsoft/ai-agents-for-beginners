# דוגמאות קבלות

שלושה קבצי קבלה שנוצרו מראש לבדיקה ללא צורך בהרצת המחברת.

| קובץ | מה הוא |
|---|---|
| `01_valid_receipt.json` | קבלה תקפה וחתומה עבור קריאה לכלי `lookup_flights`. אימות מחזיר True. |
| `02_tampered_receipt.json` | אותה קבלה עם שדה אחד ששונה לאחר החתימה. אימות מחזיר False. |
| `03_chain_three_receipts.json` | שרשרת של שלוש קבלות תקפות (חיפוש, החזקה, הזמנה) עם `previous_receipt_hash` שמקשר כל אחת לקודמתה. |

הדוגמאות חותמות את בתים הקנוניים של המידע בפורמט JCS ישירות עם Ed25519.
SHA-256 נשאר בשימוש לעיכול תוכן ולקישורים בשרשרת הקבלות, לא כ-
מקדים נוסף לפני החתימה.

## אימות הדוגמאות

ב-`18-signed-receipts.ipynb`, הרץ תחילה את ההגדרות ואת הסעיפים 1 עד 3.
סעיף 3 מגדיר את `verify_chain`; הסעיפים 1 ו-2 לבדם אינם מספיקים.
לאחר מכן הרץ את הבלוק הבא בתא חדש, כאשר ספריית העבודה של המחברת
מוגדרת ל-`18-securing-ai-agents/code_samples`. הנתיבים לדוגמאות למטה יחסיים
לספריה זו.

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

### בדיקת הדוגמה ללא Jupyter

משורש המאגר, התקן את התלויות של השיעור והרץ:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

בדיקות אלו מריצות את הדוגמאות בפייתון במחברת ואת בלוק ה-README המדויק
למעלה. הן גם בודקות כי שינוי והוספת מפתחות לא מקובעים נדחים על ידי
המאמתים. הבדיקות מדלגות על תא ההגדרות `%pip` במחברת מכיוון שהתלויות
מותקנות בנפרד. הן אינן משנות את המחברת או הדוגמאות.

## איך נוצרו אלו

הדוגמאות משתמשות באותו מסלול קוד כמו המחברת, עם מפתח חתימה קבוע
וטיימסטמפ קבועים לשחזור בתים מדויק. ליצירה מחדש:

```bash
python3 generate_fixtures.py
```

(הסקריפט נמצא ב-`generate_fixtures.py` בספריה זו.)

## מה לומדים התלמידים מבדיקת JSON גולמי

קריאת פורמט הקבלה הגולמית בונה אינטואיציה שהתאים במחברת
לא תמיד מספקים. תלמידים הסורקים את ה-JSON לעיתים מבחינים ב:

1. החתימה היא מחרוזת בסיס64url אטומה, אך כל שדה אחר הוא JSON קריא
   פשוט. החתימה אינה מוצפנת את התוכן; היא מאשרת אותו.
2. ה-`public_key` מוטמע בקבלה, וזה מספיק לבדוק
   עקביות עצמית אך לא אמון במנפיק. מבקר חייב להשוות זאת עם מפתח
   מקובע מחוץ לקבלה או שנפתר דרך רישום מהימן.
3. שינוי תו אחד בלבד בכל שדה, ואז השוואת הקובץ מחדש עם
   `02_tampered_receipt.json`, ממחיש את המנגנון ברמת ה-בתים.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->