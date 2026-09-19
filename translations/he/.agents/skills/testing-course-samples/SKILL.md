---
name: testing-course-samples
---
# בדיקת דוגמאות הקורס

אמת שהמחברות של השיעור ודוגמאות הקוד רצות מול התקנה חיה של
Microsoft Foundry / Azure OpenAI. המאגר כולל ראנר ב
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) שמריץ
כל מחברת פייתון בצורה אוטונומית ומדפיס מטריצת PASS/FAIL.

## מתי להשתמש
- "אמת את כל המחברות / הדוגמאות מול המנוי שלי ב-Azure."
- "הרץ בדיקת סמוק לקורס לאחר שדרוג חבילות או שינוי מודלים."
- "אילו שיעורים עדיין עוברים / נכשלים בלייב?"

אל תשתמש ב**זאת** עבור פעולת ה-GitHub AI Smoke Test (שמאמתת *סוכנים מתפרסים*
— ראה [`tests/README.md`](../../../tests/README.md)). מיומנות זו
מריצה את המחברות באופן מקומי.

## דרישות קדם (בדוק קודם)
1. **Python 3.12+** עם התלויות של הקורס: `python -m pip install -r requirements.txt`
   בנוסף למריץ: `python -m pip install nbconvert ipykernel`.
2. **`.env` בשורש המאגר** (העתק מקובץ [`.env.example`](../../../../../.env.example)) עם לפחות:
   - `AZURE_AI_PROJECT_ENDPOINT` — נקודת קצה של פרויקט Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — פריסה שאינה מיושנת (למשל `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) ו-`AZURE_OPENAI_DEPLOYMENT`
     עבור שיעורים שקוראים ל-Azure OpenAI ישירות (שיעור 06, 02-azure-openai, 14 handoff/human-loop).
3. סיום **`az login`** — הדוגמאות מאימותות עם `AzureCliCredential` (Entra ID, ללא מפתח).
4. אמת שקיימת פריסת מודל:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## הרצת האימות
```powershell
# כל פנקסי הפייתון (דלג על .NET, .venv, site-packages, תרגומים, נכסי מיומנות)
pwsh scripts/validate-notebooks.ps1

# שיעור אחד, עם זמן המתנה ארוך יותר לכל תא
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# רק רשום מה ירוץ (ללא ביצוע)
pwsh scripts/validate-notebooks.ps1 -List

# מפרש מפורש (אם `python` לא נמצא ב-PATH, למשל כינוי מ-Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
התסריט כותב עותקים מבוצעים, לוגים לכל מחברת, ו-`results.json` ל-
`$env:TEMP\aiab-nbval` ויוצא עם מספר הכשלונות.

כשלונות חולפים (הגבלות HTTP בקצב לשיתוף מנוי, תקלה זמנית ב-token של
`AzureCliCredential`, או תזמון שעבר) ייתבטאו בניסיון חוזר אוטומטי
(`-Retries`, ברירת מחדל 2, עם `-RetryDelaySeconds` להשהיה, ברירת מחדל 20). אם
פריסת מודל דומה מראה 429 לעיתים קרובות, בדוק את מכסת TPM ברמת GlobalStandard למנוי
(`az cognitiveservices usage list -l <region>`) — הגדלת קיבולת פריסה בודדת לא מסייעת כאשר
המכסה של *המנוי* נוצלה עד תום.

## פירוש התוצאות
- `PASS` — המחברת רצה מתחילתו ועד סופו ללא שגיאת תא.
- `FAIL` — מוצגת שורת ה`*Error` / `*Exception` הראשונה; פתח את
  הקובץ `log_*.txt` המתאים בספריית הפלט כדי לראות את המעקב המלא.
- כשלון במחברת יחידה מוגבל לפי `-Timeout` (לכל תא), כך שתא עם תלות בבני אדם
  יופיע כ`StdinNotImplementedError` במקום להיתקע.

## שיעורים שדורשים משאבים נוספים (צפויים לכשלון בלעדיהם)
| שיעור | דרישה נוספת |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — כולל מסלול מילוט בזיכרון פנימי |
| 11 MCP / GitHub | שרת MCP של GitHub + PAT |
| 13 memory (cognee) | `cognee` מוגדר עם ספק מודלים |
| 15 browser-use | דפדפנים של Playwright מותקנים (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + מודל Qwen שהורד (על המכשיר, ללא ענן) |
| מחברות `*-dotnet-*` | ליבת .NET Interactive (מוסתרות כברירת מחדל; השתמש ב`-IncludeDotnet`) |

## דיווח חזרה
סכם בטבלה של PASS/FAIL מקובצת לפי שיעור. הפרד רגרסיות אמיתיות
(באגי קוד/קונפיג לתיקון) מפערי סביבה (חסרונות ב-Search/Foundry Local/PAT),
וציין את קובצי ה-`log_*.txt` שנכשלו עבור כל כשלון אמיתי.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->