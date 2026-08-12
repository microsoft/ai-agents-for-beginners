# AGENTS.md

## סקירת הפרויקט

מאגר זה מכיל "סוכני בינה מלאכותית למתחילים" - קורס חינוכי מקיף המלמד כל מה שצריך כדי לבנות סוכני בינה מלאכותית. הקורס מורכב מ-18 שיעורים (מספרים 00-18) העוסקים ביסודות, תבניות עיצוב, מסגרות עבודה, פריסה בפרודקשן, סוכנים מקומיים/מכשיריים, ואבטחת סוכנים.

**טכנולוגיות מרכזיות:**
- Python 3.12+
- מחברות Jupyter ללימוד אינטראקטיבי
- מסגרות בינה מלאכותית: Microsoft Agent Framework (MAF)
- שירותי Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**ארכיטקטורה:**
- מבנה מבוסס שיעורים (תיקיות 00-15+)
- כל שיעור כולל: תיעוד README, דוגמאות קוד (מחברות Jupyter), ותמונות
- תמיכה רב-שפתית באמצעות מערכת תרגום אוטומטי
- מחברת Python אחת לכל שיעור המשתמשת ב-Microsoft Agent Framework

## פקודות התקנה

### דרישות מוקדמות
- Python 3.12 ומעלה
- מנוי Azure (עבור Microsoft Foundry)
- Azure CLI מותקן ומאומת (פקודת `az login`)

### התקנה ראשונית

1. **שכפל או ספר את המאגר:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # או
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **צור והפעל סביבת Python וירטואלית:**
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
   # ערוך את קובץ .env עם מפתחות ה-API והנקודות קצה שלך
   ```

### משתני סביבה נדרשים

עבור **Microsoft Foundry** (נדרש):
- `AZURE_AI_PROJECT_ENDPOINT` - נקודת הקצה של פרויקט Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - שם פריסת המודל (למשל, gpt-5-mini)

עבור **Azure AI Search** (שיעור 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - נקודת הקצה של Azure AI Search
- `AZURE_SEARCH_API_KEY` - מפתח API של Azure AI Search

אימות: הרץ `az login` לפני הפעלת המחברות (משתמש ב-`AzureCliCredential`).

## תהליך פיתוח

### הפעלת מחברות Jupyter

כל שיעור מכיל מספר מחברות Jupyter עבור מסגרות שונות:

1. **הפעל את Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **נווט לתיקיית השיעור** (למשל, `01-intro-to-ai-agents/code_samples/`)

3. **פתח והפעל מחברות:**
   - `*-python-agent-framework.ipynb` - שימוש ב-Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - שימוש ב-Microsoft Agent Framework (.NET)

### עבודה עם Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- דורש מנוי Azure
- משתמש ב-`FoundryChatClient` לשירות סוכן V2 (סוכנים נראים בפורטל Foundry)
- מוכן לפרודקשן עם נראות מובנית
- תבנית קבצים: `*-python-agent-framework.ipynb`

## הוראות בדיקה

מאגר זה חינוכי עם קוד לדוגמא ולא קוד לפרודקשן עם בדיקות אוטומטיות. כדי לאמת את ההתקנה והשינויים:

### בדיקה ידנית

1. **בדוק את סביבת Python:**
   ```bash
   python --version  # צריך להיות 3.12 ומעלה
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **בדוק הרצת מחברת:**
   ```bash
   # המר את המחברת לתסריט והפעל (מייבא בדיקות)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **אמת משתני סביבה:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### הפעלת מחברות יחידות

פתח מחברות ב-Jupyter והרץ תאים ברצף. כל מחברת היא עצמאית וכוללת:
- הצהרות ייבוא
- טעינת קונפיגורציה
- מימושים לדוגמא של סוכן
- פלט צפוי בתאי markdown

### בדיקה ראשונית של סוכנים פרוסים

עבור שיעורים שבהם סוכן משוחרר כסוכן Microsoft Foundry (01, 04, 05, 16), המאגר כולל קטלוגי בדיקות ראשוניות תחת `tests/` שמופעלות ע"י תהליך `.github/workflows/smoke-test.yml` דרך הפעולה [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). אלו שערי בדיקה קלים לאחר פריסה (האם הסוכן נגיש ועוקב אחרי דרישות הפקודות הבסיסיות?), כמילוי תהליך ההערכה בשיעורים 10 ו-16. ראה [tests/README.md](./tests/README.md) למיפוי בין קטלוג לשיעור ולסוכן. שיעור 17 רץ מקומית עם Foundry Local ואין לו נקודת קצה מתארחת, לכן הוא נבדק על ידי הרצת מחברתו ישירות.

## סגנון קוד

### קונבנציות Python

- **גרסת Python**: 3.12 ומעלה
- **סגנון קוד**: עקוב אחרי קונבנציות PEP 8 סטנדרטיות של Python
- **מחברות**: השתמש בתאי markdown ברורים כדי להסביר מושגים
- **ייבוא**: קבץ לפי ספרייה סטנדרטית, צד שלישי ומוכר מקומי

### קונבנציות מחברות Jupyter

- כלול תאי markdown תיאוריים לפני תאי הקוד
- הוסף דוגמאות פלט במחברות כהפניה
- השתמש בשמות משתנים ברורים התואמים למושגי השיעור
- שמור על סדר הרצת המחברת ליניארי (תא 1 → 2 → 3...)

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

מאגר זה משתמש Markdown לתיעוד:
- קבצי README.md בכל תיקיית שיעור
- README.md ראשי בשורש המאגר
- מערכת תרגום אוטומטית דרך GitHub Actions

### תהליך CI/CD

ממוקם ב-`.github/workflows/`:

1. **co-op-translator.yml** - תרגום אוטומטי ל-50+ שפות
2. **welcome-issue.yml** - מקבל ברוכים הבאים ליוצרי נושאים חדשים
3. **welcome-pr.yml** - מקבל ברוכים הבאים לתורמי בקשות משיכה חדשות

### פריסה

זהו מאגר חינוכי - ללא תהליך פריסה. משתמשים:
1. עושים Fork או שכפול של המאגר
2. מריצים את המחברות מקומית או ב-GitHub Codespaces
3. לומדים על ידי שינוי וניסוי בדוגמאות

## הנחיות לבקשות משיכה

### לפני הגשה

1. **בדוק את השינויים שלך:**
   - הרץ את המחברות המושפעות במלואן
   - אמת שכל התאים רצים ללא שגיאות
   - בדוק שהפלטים מתאימים

2. **עדכוני תיעוד:**
   - עדכן README.md אם מוסיפים מושגים חדשים
   - הוסף הערות במחברות לקוד מורכב
   - ודא שתאי markdown מסבירים את המטרה

3. **שינויים בקבצים:**
   - הימנע מהתחייבות של קבצי `.env` (השתמש ב-`.env.example`)
   - אל תתחייב בתיקיות `venv/` או `__pycache__/`
   - שמור פלטי מחברות כשהם ממחישים מושגים
   - הסר קבצים זמניים ומחברות גיבוי (`*-backup.ipynb`)

### פורמט כותרת PR

השתמש בכותרות מתארות:
- `[Lesson-XX] הוסף דוגמה חדשה עבור <concept>`
- `[Fix] תקן שגיאת כתיב ב-README של lesson-XX`
- `[Update] שפר דוגמת קוד ב-lesson-XX`
- `[Docs] עדכן הוראות התקנה`

### בדיקות נדרשות

- יש להפעיל מחברות ללא שגיאות
- קבצי README צריכים להיות ברורים ומדויקים
- עקוב אחרי דפוסי קוד קיימים במאגר
- שמור על עקביות עם שיעורים אחרים

## הערות נוספות

### טעויות נפוצות

1. **אי התאמת גרסת Python:**
   - ודא שמשתמשים ב-Python 3.12 ומעלה
   - ייתכן שחבילות מסוימות לא יעבדו עם גרסאות ישנות יותר
   - השתמש בפקודה `python3 -m venv` כדי לציין במפורש גרסת Python

2. **משתני סביבה:**
   - תמיד צור קובץ `.env` מתוך `.env.example`
   - אל תתחייב את קובץ `.env` (הוא ב-`.gitignore`)
   - התחבר עם `az login` לאימות Entra ID ללא מפתח

3. **קונפליקטים בחבילות:**
   - השתמש בסביבה וירטואלית חדשה
   - התקן מתוך `requirements.txt` במקום חבילות בודדות
   - ייתכן שמחברות מסוימות דורשות חבילות נוספות המוזכרות בתאי markdown

4. **שירותי Azure:**
   - שירותי Azure AI דורשים מנוי פעיל
   - חלק מהפיצ'רים ספציפיים לאזור גאוגרפי
   - ודא שפריסת Azure OpenAI שלך תומכת ב-API התגובות

### מסלול לימוד

מומלץ להתקדם בשיעורים לפי הסדר:
1. **00-course-setup** - התחלה להגדרת הסביבה
2. **01-intro-to-ai-agents** - הבנת יסודות סוכני AI
3. **02-explore-agentic-frameworks** - למידה על מסגרות עבודה שונות
4. **03-agentic-design-patterns** - תבניות עיצוב מרכזיות
5. המשך בשיעורים המסומנים לפי הסדר

### בחירת מסגרת עבודה

בחר מסגרת על פי המטרות שלך:
- **כל השיעורים**: Microsoft Agent Framework (MAF) עם `FoundryChatClient`
- **רישום סוכנים בצד השרת** ב-Microsoft Foundry Agent Service V2 והם גלויים בפורטל Foundry

### קבלת עזרה

- הצטרף ל-[Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- בדוק את קבצי README של השיעורים להנחיות ספציפיות
- עיין ב-[README.md](./README.md) הראשי לקבלת סקירת הקורס
- התייחס ל-[Course Setup](./00-course-setup/README.md) להוראות התקנה מפורטות

### תרומה

זהו פרויקט חינוכי פתוח. תרומות מתקבלות בברכה:
- שפר דוגמות קוד
- תקן שגיאות כתיב או טעויות
- הוסף הערות להבהרה
- הצע נושאי שיעור חדשים
- תרגם לשפות נוספות

עיין ב-[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) לצרכים נוכחיים.

## הקשר ספציפי לפרויקט

### תמיכה ברב-שפות

מאגר זה משתמש במערכת תרגום אוטומטית:
- תומך ב-50+ שפות
- תרגומים בתיקיות `/translations/<lang-code>/`
- תהליך GitHub Actions מטפל בעדכוני התרגום
- קבצי מקור באנגלית בשורש המאגר

### מבנה השיעור

כל שיעור עוקב אחרי דפוס אחיד:
1. תמונת תצוגה מקדימה עם קישור לסרטון
2. תוכן השיעור הכתוב (README.md)
3. דוגמאות קוד במספר מסגרות עבודה
4. מטרות למידה ודרישות מוקדמות
5. משאבי לימוד נוספים בקישורים

### שם דוגמאות קוד

פורמט: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - שיעור 1, MAF Python
- `14-sequential.ipynb` - שיעור 14, תבניות מתקדמות ב-MAF
- `16-python-agent-framework.ipynb` - שיעור 16, סוכן תמיכה בלקוח בפרודקשן
- `17-local-agent-foundry-local.ipynb` - שיעור 17, סוכן מקומי עם Foundry Local + Qwen

### תיקיות מיוחדות

- `translated_images/` - תמונות מתורגמות
- `images/` - תמונות מקור באנגלית
- `.devcontainer/` - קונפיגורציית מכולת פיתוח ל-VS Code
- `.github/` - תהליכי עבודה ותבניות GitHub Actions

### תלותיות

חבילות מרכזיות מתוך `requirements.txt`:
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