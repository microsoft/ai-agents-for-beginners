# AGENTS.md

## סקירת הפרויקט

מאגר זה מכיל "סוכני AI למתחילים" - קורס חינוכי מקיף המלמד את כל הדרוש לבניית סוכני AI. הקורס מורכב מ-18 שיעורים (מספרים 00-18) שמכסים יסודות, דפוסי עיצוב, מסגרות, פריסה לייצור, סוכנים מקומיים/מכשיריים, ובטיחות של סוכני AI.

**טכנולוגיות מפתח:**
- Python 3.12+
- יומני Jupyter ללמידה אינטראקטיבית
- מסגרות AI: Microsoft Agent Framework (MAF)
- שירותי Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**ארכיטקטורה:**
- מבנה מבוסס שיעורים (ספריות 00-18)
- כל שיעור מכיל: תיעוד README, דוגמאות קוד (יומני Jupyter), ותמונות
- תמיכה רב-לשונית באמצעות מערכת תרגום אוטומטית
- יומן Python אחד לכל שיעור באמצעות Microsoft Agent Framework

## פקודות התקנה

### דרישות מוקדמות
- Python 3.12 ומעלה
- מנוי Azure (ל-Microsoft Foundry)
- Azure CLI מותקן ומאומת (`az login`)

### התקנה ראשונית

1. **שכפל או צרף למאגר:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **צור והפעל סביבה וירטואלית של Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **התקן תלותים:**
   ```bash
   pip install -r requirements.txt
   ```

4. **הגדר משתני סביבה:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### משתני סביבה דרושים

עבור **Microsoft Foundry** (חובה):
- `AZURE_AI_PROJECT_ENDPOINT` - נקודת קצה לפרויקט Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - שם פריסת מודל (למשל, gpt-5-mini)

עבור **Azure AI Search** (שיעור 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - נקודת קצה של Azure AI Search
- `AZURE_SEARCH_API_KEY` - מפתח API ל-Azure AI Search

אימות: הרץ `az login` לפני הפעלת היומנים (משתמש ב-`AzureCliCredential`).

## תהליך פיתוח

### הרצת יומני Jupyter

כל שיעור מכיל מספר יומני Jupyter עבור מסגרות שונות:

1. **הפעל את Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **נווט לספריה של שיעור** (למשל, `01-intro-to-ai-agents/code_samples/`)

3. **פתח והרץ יומנים:**
   - `*-python-agent-framework.ipynb` - שימוש ב-Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - שימוש ב-Microsoft Agent Framework (.NET)

### עבודה עם Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- דרוש מנוי Azure
- משתמש ב-`FoundryChatClient` עבור Agent Service V2 (סוכנים נראים בפורטל Foundry)
- מוכן לייצור עם יכולת ניטור מובנית
- תבנית קבצים: `*-python-agent-framework.ipynb`

## הוראות בדיקה

זהו מאגר חינוכי עם קוד דוגמה ולא קוד ייצור עם בדיקות אוטומטיות. לאמת את ההתקנה והשינויים:

### בדיקה ידנית

1. **בדוק את סביבת ה-Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **בדוק הרצת היומן:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **אמת את משתני הסביבה:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### הרצת יומנים בודדים

פתח יומנים ב-Jupyter והרץ תאים ברצף. כל יומן הוא עצמאי וכולל:
- הצהרות ייבוא
- טעינת הגדרות
- יישומי סוכן לדוגמה
- פלטים צפויים בתאי markdown

### בדיקת עשן לסוכנים שפועלים

עבור שיעורים בהם סוכן מפורסם כסוכן Microsoft Foundry (01, 04, 05, 16), המאגר כולל קטלוגי בדיקה בעזרת עשן תחת `tests/` שמופעלים על ידי תהליך `.github/workflows/smoke-test.yml` באמצעות הפעולה [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). אלו שער קל משקל לאחר פריסה (האם הסוכן נגיש ועומד בציפיות הנחיה בסיסיות?), המשלימים את קו הערכה בשיעורים 10 ו-16. ראה [tests/README.md](./tests/README.md) למיפוי קטלוג-לשיעור-לסוכן. שיעור 17 רץ מקומית עם Foundry Local ואין לו נקודת קצה משודרת, לכן הוא מאומת בהרצת היומן שלו ישירות.

## סגנון קוד

### נורמות Python

- **גרסת Python**: 3.12+
- **סגנון קוד**: עקוב אחרי הנורמות הסטנדרטיות PEP 8 של Python
- **יומנים**: השתמש בתאי markdown ברורים להסבר מושגים
- **ייבוא**: קבץ לפי ספריית סטנדרט, צד שלישי, מקומי

### נורמות יומני Jupyter

- כלול תאי markdown מתארים לפני תאי קוד
- הוסף דוגמאות פלט ביומנים כהפניה
- השתמש בשמות משתנים ברורים התואמים למושגי השיעור
- שמור על סדר הרצת היומן ליניארי (תא 1 → 2 → 3...)

### ארגון קבצים

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## בנייה ופריסה

### בניית תיעוד

מאגר זה משתמש ב-Markdown לתיעוד:
- קבצי README.md בכל תיקיית שיעור
- README.md ראשי בשורש המאגר
- מערכת תרגום אוטומטית דרך GitHub Actions

### צינור CI/CD

ממוקם ב-`.github/workflows/`:

1. **co-op-translator.yml** - תרגום אוטומטי ליותר מ-50 שפות
2. **welcome-issue.yml** - מקבל יוצרים חדשים של נושאים
3. **welcome-pr.yml** - מקבל משתתפי pull request חדשים

### פריסה

זהו מאגר חינוכי - אין תהליך פריסה. המשתמשים:
1. מצורפים או משכפלים את המאגר
2. מריצים יומנים מקומית או ב-GitHub Codespaces
3. לומדים על ידי שינוי וניסוי בדוגמאות

## קווים מנחים לבקשות משיכה

### לפני ההגשה

1. **בדוק את השינויים שלך:**
   - הרץ את כל היומנים המושפעים במלואם
   - אמת שכל התאים מורצים ללא שגיאות
   - בדוק שהפלטים מתאימים

2. **עדכוני תיעוד:**
   - עדכן README.md אם מוסיף מושגים חדשים
   - הוסף הערות ביומנים לקוד מורכב
   - וודא שתאי markdown מסבירים את המטרה

3. **שינויים בקבצים:**
   - הימנע מהתחייבות של קבצי `.env` (השתמש ב-`.env.example`)
   - אל תתחייב בספריות `venv/` או `__pycache__/`
   - שמור על פלטי היומנים כשהם מראים מושגים
   - הסר קבצים זמניים וגיבויים של יומנים (`*-backup.ipynb`)

### פורמט כותרת PR

השתמש בכותרות מתארות:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### בדיקות דרושות

- היומנים צריכים לרוץ ללא שגיאות
- קבצי README צריכים להיות ברורים ותקינים
- עקוב אחרי דפוסי קוד קיימים במאגר
- שמור עקביות עם שיעורים אחרים

## הערות נוספות

### בעיות נפוצות

1. **אי התאמת גרסת Python:**
   - ודא שמשתמשים ב-Python 3.12+
   - ייתכן שחלק מהחבילות לא יעבדו עם גרסאות ישנות יותר
   - השתמש ב-`python3 -m venv` כדי לציין במפורש את גרסת Python

2. **משתני סביבה:**
   - תמיד צור `.env` מ-`.env.example`
   - אל תתחייב בקובץ `.env` (הוא ב-`.gitignore`)
   - התחבר באמצעות `az login` לאימות Entra ID ללא מפתח

3. **קונפליקטים בחבילות:**
   - השתמש בסביבה וירטואלית חדשה
   - התקן מ-`requirements.txt` במקום חבילות בודדות
   - ייתכן שיומנים מסוימים ידרשו חבילות נוספות שמצוינות בתאי markdown שלהם

4. **שירותי Azure:**
   - שירותי Azure AI דורשים מנוי פעיל
   - חלק מהפיצ'רים הם ספציפיים לאזור
   - וודא שפריסת מודל Azure OpenAI שלך תומכת ב-Responses API

### מסלול הלמידה

התקדמות מומלצת בין השיעורים:
1. **00-course-setup** - התחל כאן להגדרת סביבה
2. **01-intro-to-ai-agents** - הבן את יסודות סוכני AI
3. **02-explore-agentic-frameworks** - למד על מסגרות שונות
4. **03-agentic-design-patterns** - דפוסי עיצוב מרכזיים
5. המשך בשיעורים ממוספרים ברצף

### בחירת מסגרת עבודה

בחר מסגרת על פי המטרות שלך:
- **כל השיעורים**: Microsoft Agent Framework (MAF) עם `FoundryChatClient`
- **רישום סוכנים בצד השרת** ב-Microsoft Foundry Agent Service V2 וסוכנים נראים בפורטל Foundry

### קבלת עזרה

- הצטרף ל-[Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- עיין בקבצי README של השיעורים להדרכה ספציפית
- בדוק את ה-[README.md](./README.md) הראשי לקבלת סקירת הקורס
- התייחס ל-[Course Setup](./00-course-setup/README.md) להוראות התקנה מפורטות

### תרומה

זהו פרויקט חינוכי פתוח. תרומות מתקבלות בברכה:
- שפר דוגמאות קוד
- תקן שגיאות כתיב או טעויות
- הוסף הערות להסברים
- הצע נושאים חדשים לשיעורים
- תרגום לשפות נוספות

ראה [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) לצרכים העדכניים.

## הקשר ספציפי לפרויקט

### תמיכה רב-לשונית

מאגר זה משתמש במערכת תרגום אוטומטית:
- תמיכה בלמעלה מ-50 שפות
- תרגומים בתיקיות `/translations/<lang-code>/`
- תהליך GitHub Actions מטפל בעדכוני תרגום
- קבצי מקור באנגלית בשורש המאגר

### מבנה השיעור

כל שיעור עוקב אחרי דפוס אחיד:
1. תמונת טמפון עם קישור לסרטון
2. תוכן השיעור כתוב (README.md)
3. דוגמאות קוד במסגרות שונות
4. מטרות למידה ודרישות מוקדמות
5. קישורים למשאבים חינוכיים נוספים

### שם דוגמת קוד

פורמט: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - שיעור 1, MAF Python
- `14-sequential.ipynb` - שיעור 14, דפוסים MAF מתקדמים
- `16-python-agent-framework.ipynb` - שיעור 16, סוכן תמיכה ללקוח לייצור
- `17-local-agent-foundry-local.ipynb` - שיעור 17, סוכן מקומי עם Foundry Local + Qwen

### תיקיות מיוחדות

- `translated_images/` - תמונות מותאמות לתרגומים
- `images/` - תמונות מקור לתוכן באנגלית
- `.devcontainer/` - תצורת מכולת פיתוח VS Code
- `.github/` - תהליכי עבודה ותבניות GitHub Actions

### תלותים

חבילות מפתח מ-`requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - תמיכה בפרוטוקול בין סוכנים
- `azure-ai-inference`, `azure-ai-projects` - שירותי Azure AI
- `azure-identity` - אימות Azure (AzureCliCredential)
- `azure-search-documents` - אינטגרציה עם Azure AI Search
- `mcp[cli]` - תמיכה בפרוטוקול Model Context

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->