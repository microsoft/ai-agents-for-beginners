# דוגמאות קבלות

ארבע קבצי קבלות שנוצרו מראש לבדיקה ללא הרצת המחברת.

| קובץ | מה זה |
|---|---|
| `01_valid_receipt.json` | קבלה תקפה וחתומה עבור קריאת כלי `lookup_flights`. האימות מחזיר True. |
| `02_tampered_receipt.json` | אותה קבלה עם שדה אחד ששונה לאחר החתימה. האימות מחזיר False. |
| `03_chain_three_receipts.json` | שרשרת של שלוש קבלות תקפות (חיפוש, החזקה, הזמנה) עם `previous_receipt_hash` שמקשר כל אחת לזו הקודמת. |
| `04_resigned_receipt.json` | אותה קבלה שעוותה ואז נחתמה מחדש על ידי תוקף, כאשר המפתח הציבורי של התוקף מוטמע בתוכה. מאמת נגד המפתח שבתוכה, נכשל נגד מפתח המנפיק. |

הדוגמאות חותמות את בתים של ה-JCS הקנוני של המטען ישירות עם Ed25519.
SHA-256 נשאר בשימוש עבור דיגסטים של תוכן וקישורים בשרשרת הקבלות, לא בתור
קדם-האשטה נוספת לפני החתימה.

## אימות הדוגמאות

ב-`18-signed-receipts.ipynb`, הרץ קודם כל את ההגדרות ואת הסעיפים 1 עד 3.
סעיף 3 מגדיר את `verify_chain`; סעיפים 1 ו-2 לבד אינם מספיקים.
לאחר מכן הרץ את הבלוק הבא בתא חדש, כאשר תיקיית העבודה של המחברת
מוגדרת ל־`18-securing-ai-agents/code_samples`. הנתיבים לדוגמאות מטה יחסיים
לתיקייה זו.

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

### בדיקת הדוגמא ללא Jupyter

מהשורש של המאגר, התקן את התלויות של השיעור והריץ:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

בדיקות אלה מריצות את דוגמאות הפייתון במחברת ואת בלוק ה-README המדויק
למעלה. הן גם בודקות ששינויי התוכן ומפתחות לא נעולים נדחים על ידי
המאמתים. הבדיקות מדלגות על תא ההגדרה `%pip` של המחברת מפני שהתלויות
מותקנות בנפרד. הן אינן משנות את המחברת או את הדוגמאות.

## כיצד נוצרו אלה

הדוגמאות משתמשות באותו נתיב קוד כמו המחברת, עם מפתח חתימה קבוע
וחותמות זמן קבועות לשחזור בייטים מדויק. לשחזור מחדש:

```bash
python3 generate_fixtures.py
```

(התסריט נמצא ב־`generate_fixtures.py` בתיקייה זו.)

`../test_signed_receipts.py` בודק את כל זה אוטומטית: הוא מריץ את
הקוד של המחברת, מאמת את ארבעת האביזרים האלה עם המחברת
`verify_receipt` ו-`verify_chain`, ומאשר ששחזור האביזרים
מניב בתים זהים. מתוך `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## מה שהתלמידים לומדים מבדיקת JSON גולמי

קריאת פורמט הקבלה הגולמי בונה אינטואיציה שהתאים במחברת
לא תמיד מספקים. תלמידים שמגלים את ה-JSON לעיתים שמים לב ל:

1. החתימה היא מחרוזת לא שקופה ב-base64url, אבל כל שדה אחר הוא JSON קריא
   פשוט. החתימה אינה מצפינה את התוכן; היא מאשרת אותו.
2. `public_key` מוטמע בקבלה, מה שהופך את הקובץ
   לעצמאי אך אינו מה שמבקר מאמת מולו. השווה
   `02_tampered_receipt.json` עם `04_resigned_receipt.json`: שניהם
   שונו לאחר החתימה, אבל השנייה נחתמה מחדש עם מפתחו של התוקף,
   כך שהיא מאומתת מול המפתח שהיא נושאת. המפתח המוטמע
   אומר לך שהקובץ עקבי פנימית. רק מפתח שנרכש
   במקום אחר אומר לך מי הוציא אותו.
3. שינוי תו אחד בכל שדה מחוץ ל-`signature`, ואז
   השוואה מחדש של קובץ זה עם `02_tampered_receipt.json`, מייחדת
   את המנגנון ברמת הבייטים.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->