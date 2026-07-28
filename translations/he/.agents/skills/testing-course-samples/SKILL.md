---
name: testing-course-samples
description: השתמש כאשר מתבקשים לבדוק תוקף, לבצע בדיקת פונקציונליות בסיסית, או להריץ
  את המחברת ודוגמאות הקוד של הקורס נגד תצורת Microsoft Foundry / Azure OpenAI חיה.
  כולל הגדרת סביבה (.env, az login, חבילות), הרצת הסקריפט scripts/validate-notebooks.ps1,
  פירוש תוצאות PASS/FAIL, ואילו שיעורים דורשים משאבים נוספים (Azure AI Search, GitHub
  MCP, Foundry Local, Playwright).
---
# בדיקת דוגמאות הקורס

אמתו שהמחברות והדוגמאות של השיעור רצות נגד הגדרת
Microsoft Foundry / Azure OpenAI חיה. המאגר כולל ראנר ב-
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) שמבצע
הפעלה שקטה של כל מחברת פייתון ומדפיס מטריצת PASS/FAIL.

## מתי להשתמש
- "אמת את כל המחברות / הדוגמאות מול מנוי Azure שלי."
- "בצע בדיקת תפקוד ראשונית בקורס לאחר שדרוג חבילות או שינוי דגמים."
- "אילו שיעורים עדיין עוברים / נכשלים בזמן אמת?"

אל תשתמשו בזה עבור GitHub Action של AI Smoke Test (שמאמת סוכנים *מופעלים* —
ראו [`tests/README.md`](../../../tests/README.md)). מיומנות זו
מריצה את המחברות באופן מקומי.

## דרישות מוקדמות (בדקו קודם)
1. **Python 3.12+** עם התלויות של הקורס: `python -m pip install -r requirements.txt`
   בנוסף המפעיל: `python -m pip install nbconvert ipykernel`.
2. **`.env` בשורש המאגר** (העתק מ-[`.env.example`](../../../../../.env.example)) עם לפחות:
   - `AZURE_AI_PROJECT_ENDPOINT` — נקודת קצה של פרויקט Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — פריסת מודל שאינה מיושנת (למשל `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) ו- `AZURE_OPENAI_DEPLOYMENT`
     לשיעורים שקוראים ישירות ל-Azure OpenAI (שיעור 06, 02-azure-openai, 14 handoff/human-loop).
3. **התחברות `az login`** הושלמה — דוגמאות מאמתות עם `AzureCliCredential` (Entra ID, ללא מפתח).
4. אמתו שקיים פריסת המודל:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## הרצת האימות
```powershell
# כל פנקסי הפייתון (מדלג על .NET, .venv, site-packages, תרגומים, נכסי מיומנות)
pwsh scripts/validate-notebooks.ps1

# שיעור יחיד, עם זמן קצוב ארוך יותר לכל תא
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# רק לרשום מה ירוץ (ללא ביצוע)
pwsh scripts/validate-notebooks.ps1 -List

# מפרש מוצהר (אם `python` לא נמצא ב-PATH, לדוגמה קיצור חנות ווינדוס)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
הסקריפט כותב עותקים מוקצים, לוגים לכל מחברת ו- `results.json` אל
`$env:TEMP\aiab-nbval` ויוצא עם מספר הכשלים.

## פירוש התוצאות
- `PASS` — המחברת רצה מקצה לקצה ללא שגיאת תא.
- `FAIL` — מוצגת שורת השגיאה/חריגה הראשונה `*Error` / `*Exception`; פתח את הקובץ המתאים
  `log_*.txt` בתיקיית הפלט לקבלת המעקב המלא.
- כישלון של מחברת אחת מוגבל על ידי הגבלה של `-Timeout` (לכל תא), כך שתא תלוי
  עם התערבות אדם יופיע כ- `StdinNotImplementedError` במקום להיתקע.

## שיעורים שדורשים משאבים נוספים (צפויים להיכשל בלעדיהם)
| שיעור | דרישה נוספת |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, מפתח) — כולל דרך תחזית בזיכרון |
| 11 MCP / GitHub | שרת MCP של GitHub + PAT |
| 13 memory (cognee) | `cognee` מוגדר עם ספק מודל |
| 15 browser-use | דפדפני Playwright מותקנים (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + מודל Qwen שהורד (במכשיר, ללא ענן) |
| מחברות `*-dotnet-*` | ליבת .NET Interactive (מוחרג כברירת מחדל; השתמש ב- `-IncludeDotnet`) |

## דיווח חזרה
סכם בטבלת PASS/FAIL מקובצת לפי שיעור. הפרד בין נסיגות אמתיות
(באגים בקוד/הגדרות לתיקון) לבין פערי סביבה (חסר חיפוש / Foundry Local / PAT),
וציין את ה- `log_*.txt` הכושלים עבור כל כשל אמיתי.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->