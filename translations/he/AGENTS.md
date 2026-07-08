# AGENTS.md

## סקירת הפרויקט

מאגר זה מכיל "סוכני בינה מלאכותית למתחילים" - קורס חינוכי מקיף המלמד הכל הדרוש לבניית סוכני בינה מלאכותית. הקורס מורכב מ-18 שיעורים המכסים יסודות, תבניות עיצוב, מסגרות עבודה ופריסת סוכנים בסביבת ייצור.

**טכנולוגיות מרכזיות:**
- Python 3.12 ומעלה
- מחברות Jupyter ללמידה אינטראקטיבית
- מסגרות AI: Microsoft Agent Framework (MAF)
- שירותי Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**ארכיטקטורה:**
- מבנה מבוסס שיעורים (ספריות 00-15+)
- כל שיעור כולל: תיעוד README, דוגמאות קוד (מחברות Jupyter), ותמונות
- תמיכה בריבוי שפות באמצעות מערכת תרגום אוטומטית
- מחברת Python אחת לכל שיעור המשתמשת ב-Microsoft Agent Framework

## פקודות הגדרה

### דרישות מוקדמות
- Python 3.12 או גבוה יותר
- מנוי Azure (עבור Microsoft Foundry)
- התקנת Azure CLI ואימות (`az login`)

### הגדרה ראשונית

1. **שכפל או פורק את המאגר:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # או
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **צור והפעל סביבת פיתוח וירטואלית לפייתון:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # ב-Windows: venv\Scripts\activate
   ```

3. **התקן תלותיות:**
   ```bash
   pip install -r requirements.txt
   ```

4. **הגדר משתני סביבה:**
   ```bash
   cp .env.example .env
   # ערוך את קובץ .env עם מפתחות ה-API והנקודות הקצה שלך
   ```

### משתני סביבה דרושים

עבור **Microsoft Foundry** (נדרש):
- `AZURE_AI_PROJECT_ENDPOINT` - נקודת הקצה של פרויקט ב-Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - שם פריסת המודל (למשל, gpt-4o)

עבור **Azure AI Search** (שיעור 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - נקודת הקצה של Azure AI Search
- `AZURE_SEARCH_API_KEY` - מפתח ה-API של Azure AI Search

אימות: להריץ `az login` לפני הרצת המחברות (משתמש ב-`AzureCliCredential`).

## זרימת עבודה לפיתוח

### הרצת מחברות Jupyter

כל שיעור כולל מספר מחברות Jupyter למסגרות עבודה שונות:

1. **הפעל Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **נווט לתיקיית השיעור** (למשל, `01-intro-to-ai-agents/code_samples/`)

3. **פתח והרץ מחברות:**
   - `*-python-agent-framework.ipynb` - שימוש ב-Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - שימוש ב-Microsoft Agent Framework (.NET)

### עבודה עם Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- דורש מנוי Azure
- משתמש ב-`FoundryChatClient` עבור Agent Service V2 (סוכנים נראים בפורטל Foundry)
- מוכן לייצור עם יכולות ניתוח מובנות
- תבנית קבצים: `*-python-agent-framework.ipynb`

## הוראות בדיקה

זהו מאגר חינוכי עם קוד לדוגמא במקום קוד ייצור עם בדיקות אוטומטיות. להבטיח שתצורתך ושינויים תקינים:

### בדיקה ידנית

1. **בדוק את סביבת הפייתון:**
   ```bash
   python --version  # צריך להיות 3.12 ומעלה
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **בדוק את הרצת המחברת:**
   ```bash
   # המרה של פנקס לריצה כסקריפט (בודק ייבוא בדיקות)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ודא משתני סביבה:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### הרצת מחברות בודדות

פתח מחברות ב-Jupyter והרץ את התאים לפי הסדר. כל מחברת עצמאית וכוללת:
- משפטי ייבוא
- טעינת תצורה
- יישום דוגמאות סוכנים
- פלטים צפויים בתאי markdown

## סגנון קוד

### מתכונות פייתון

- **גרסת פייתון**: 3.12 ומעלה
- **סגנון קוד**: עקוב אחר קווי הנחיה סטנדרטיים של PEP 8 בפייתון
- **מחברות**: השתמש בתאי markdown ברורים להסבר מושגים
- **ייבוא**: קיבוץ לפי ספריה סטנדרטית, צד שלישי, ומקומי

### מתכונות מחברת Jupyter

- כלול תאי markdown תיאוריים לפני תאי הקוד
- הוסף דוגמאות פלט במחברות כהפניה
- השתמש בשמות משתנים ברורים התואמים למושגי השיעור
- שמור על סדר הרצת מחברת ליניארי (תא 1 → 2 → 3...)

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
- מערכת תרגום אוטומטית באמצעות GitHub Actions

### צינור CI/CD

ממוקם ב-`.github/workflows/`:

1. **co-op-translator.yml** - תרגום אוטומטי ל-50+ שפות
2. **welcome-issue.yml** - מקבל יוצרי נושאים חדשים
3. **welcome-pr.yml** - מקבל תורמים של Pull Requests חדשים

### פריסה

זהו מאגר חינוכי - אין תהליך פריסה. משתמשים:
1. פורקים או משכפלים את המאגר
2. מריצים מחברות באופן מקומי או ב-GitHub Codespaces
3. לומדים על ידי שינוי וניסוי בדוגמאות

## הנחיות ל-Pull Request

### לפני ההגשה

1. **בדוק את השינויים שלך:**
   - הרץ מחברות מושפעות במלואן
   - וודא שכל התאים רצים ללא שגיאות
   - בדוק שהפלט מתאים

2. **עדכוני תיעוד:**
   - עדכן README.md אם נוסף מושג חדש
   - הוסף הערות במחברות לקוד מורכב
   - ודא שתאי markdown מסבירים את המטרה

3. **שינויים בקבצים:**
   - הימנע מדחיפת קבצי `.env` (השתמש ב-`.env.example`)
   - אל תדחוף תיקיות `venv/` או `__pycache__/`
   - שמור פלטים במחברות כאשר הם מדגימים מושגים
   - הסר קבצים זמניים ומחברות גיבוי (`*-backup.ipynb`)

### פורמט כותרת PR

השתמש בכותרות תיאוריות:
- `[Lesson-XX] הוסף דוגמה חדשה עבור <concept>`
- `[Fix] תיקון טעות כתיב ב-README של lesson-XX`
- `[Update] שפר דוגמת קוד ב-lesson-XX`
- `[Docs] עדכן הוראות התקנה`

### בדיקות נדרשות

- יש להריץ מחברות ללא שגיאות
- קבצי README צריכים להיות ברורים ומדויקים
- עקוב אחרי תבניות קוד קיימות במאגר
- שמור על עקביות עם שיעורים אחרים

## הערות נוספות

### טעויות נפוצות

1. **אי התאמת גרסת פייתון:**
   - ודא שימוש ב-Python 3.12 ומעלה
   - חלק מהחבילות עלולות לא לעבוד בגרסאות ישנות יותר
   - השתמש ב-`python3 -m venv` לציון גרסת פייתון במפורש

2. **משתני סביבה:**
   - תמיד צור `.env` מתוך `.env.example`
   - אל תדחוף קובץ `.env` (נמצא ב-.gitignore)
   - התחבר עם `az login` לאימות Entra ID ללא מפתח

3. **קונפליקטים בחבילות:**
   - השתמש בסביבת וירטואלית חדשה
   - התקן דרך `requirements.txt` במקום חבילות בודדות
   - חלק מהמחברות דורשות חבילות נוספות שמוזכרות בתאי markdown שלהם

4. **שירותי Azure:**
   - שירותי Azure AI דורשים מנוי פעיל
   - חלק מהפיצ'רים ספציפיים לאזורים גאוגרפיים
   - ודא שפריסת מודל Azure OpenAI שלך תומכת ב-Responses API

### מסלול למידה

מומלץ להתקדם לפי הסדר הבא בשיעורים:
1. **00-course-setup** - התחל כאן עם הגדרת הסביבה
2. **01-intro-to-ai-agents** - הבן יסודות סוכני AI
3. **02-explore-agentic-frameworks** - למד על מסגרות עבודה שונות
4. **03-agentic-design-patterns** - תבניות עיצוב מרכזיות
5. המשך בשיעורים ממוספרים לפי סדר

### בחירת מסגרת עבודה

בחר מסגרת עבודה לפי המטרות שלך:
- **כל השיעורים**: Microsoft Agent Framework (MAF) עם `FoundryChatClient`
- **הרשמת סוכנים בצד השרת** ב-Microsoft Foundry Agent Service V2 והם נראים בפורטל Foundry

### קבלת עזרה

- הצטרף ל-[Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- בדוק את קבצי README של השיעורים להכוונה ספציפית
- עיין בקובץ [README.md](./README.md) הראשי לסיכום הקורס
- ראה את [Course Setup](./00-course-setup/README.md) להוראות מפורטות להגדרה

### תרומה

זהו פרויקט חינוכי פתוח. תרומות מתקבלות בברכה:
- שפר דוגמאות קוד
- תקן טעויות כתיב או שגיאות
- הוסף הערות להבהרה
- הצע נושאים חדשים לשיעורים
- תרגם לשפות נוספות

ראה ב-[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) לצרכים הנוכחיים.

## הקשר ספציפי לפרויקט

### תמיכה בריבוי שפות

מאגר זה משתמש במערכת תרגום אוטומטית:
- 50+ שפות נתמכות
- תרגומים בספריות `/translations/<lang-code>/`
- צינור GitHub Actions מטפל בעדכוני תרגום
- קבצי מקור באנגלית בשורש המאגר

### מבנה שיעור

כל שיעור עוקב אחרי דפוס עקבי:
1. תמונת ממוזערת וידאו עם קישור
2. תוכן השיעור כתוב (README.md)
3. דוגמאות קוד במסגרות עבודה שונות
4. מטרות למידה ודרישות מוקדמות
5. משאבי למידה נוספים מקושרים

### שם דוגמאות קוד

פורמט: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - שיעור 1, MAF Python
- `14-sequential.ipynb` - שיעור 14, תבניות מתקדמות ב-MAF

### ספריות מיוחדות

- `translated_images/` - תמונות מתורגמות מקומיות
- `images/` - תמונות מקור לתוכן באנגלית
- `.devcontainer/` - קונפיגורציית מיכל פיתוח ל-VS Code
- `.github/` - צינורות וテンプレייטים של GitHub Actions

### תלותיות

חבילות מפתח מתוך `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - תמיכה בפרוטוקול Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - שירותי Azure AI
- `azure-identity` - אימות Azure (AzureCliCredential)
- `azure-search-documents` - אינטגרציה עם Azure AI Search
- `mcp[cli]` - תמיכה ב-Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->