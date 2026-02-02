# AGENTS.md

## סקירת הפרויקט

מאגר זה מכיל את "סוכני AI למתחילים" - קורס חינוכי מקיף המלמד כל מה שצריך כדי לבנות סוכני AI. הקורס כולל מעל 15 שיעורים המכסים יסודות, תבניות עיצוב, מסגרות עבודה ופריסת סוכני AI בסביבת ייצור.

**טכנולוגיות מרכזיות:**
- Python 3.12+
- Jupyter Notebooks ללמידה אינטראקטיבית
- מסגרות AI: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- שירותי Azure AI: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (זמין ברמת חינם)

**ארכיטקטורה:**
- מבנה מבוסס שיעורים (תיקיות 00-15+)
- כל שיעור מכיל: תיעוד README, דוגמאות קוד (Jupyter notebooks) ותמונות
- תמיכה רב-לשונית באמצעות מערכת תרגום אוטומטית
- אפשרויות מסגרת עבודה מרובות לכל שיעור (Semantic Kernel, AutoGen, Azure AI Agent Service)

## פקודות התקנה

### דרישות מוקדמות
- Python 3.12 או גרסה גבוהה יותר
- חשבון GitHub (ל-GitHub Models - רמת חינם)
- מנוי Azure (אופציונלי, עבור שירותי Azure AI)

### התקנה ראשונית

1. **שכפול או יצירת fork למאגר:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **יצירה והפעלה של סביבת Python וירטואלית:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **התקנת תלות:**
   ```bash
   pip install -r requirements.txt
   ```

4. **הגדרת משתני סביבה:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### משתני סביבה נדרשים

עבור **GitHub Models (חינם)**:
- `GITHUB_TOKEN` - אסימון גישה אישי מ-GitHub

עבור **שירותי Azure AI** (אופציונלי):
- `PROJECT_ENDPOINT` - נקודת קצה של פרויקט Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - מפתח API של Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - כתובת URL של נקודת קצה של Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - שם פריסה עבור מודל צ'אט
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - שם פריסה עבור הטמעות
- תצורת Azure נוספת כפי שמוצג ב-`.env.example`

## זרימת עבודה לפיתוח

### הפעלת Jupyter Notebooks

כל שיעור מכיל מספר Jupyter notebooks עבור מסגרות עבודה שונות:

1. **הפעלת Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **ניווט לתיקיית שיעור** (לדוגמה, `01-intro-to-ai-agents/code_samples/`)

3. **פתיחה והפעלת notebooks:**
   - `*-semantic-kernel.ipynb` - שימוש במסגרת Semantic Kernel
   - `*-autogen.ipynb` - שימוש במסגרת AutoGen
   - `*-python-agent-framework.ipynb` - שימוש במסגרת Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - שימוש במסגרת Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - שימוש בשירות Azure AI Agent

### עבודה עם מסגרות עבודה שונות

**Semantic Kernel + GitHub Models:**
- רמת חינם זמינה עם חשבון GitHub
- מתאים ללמידה וניסויים
- תבנית קובץ: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- רמת חינם זמינה עם חשבון GitHub
- יכולות תזמור רב-סוכנים
- תבנית קובץ: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- מסגרת העבודה העדכנית ביותר של Microsoft
- זמינה ב-Python וב-.NET
- תבנית קובץ: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- דורש מנוי Azure
- תכונות מוכנות לייצור
- תבנית קובץ: `*-azureaiagent.ipynb`

## הוראות בדיקה

זהו מאגר חינוכי עם קוד לדוגמה ולא קוד ייצור עם בדיקות אוטומטיות. כדי לוודא את ההתקנה והשינויים שלך:

### בדיקה ידנית

1. **בדיקת סביבת Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **בדיקת הפעלת notebooks:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **אימות משתני סביבה:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### הפעלת notebooks בודדים

פתח notebooks ב-Jupyter והפעל תאים באופן רציף. כל notebook הוא עצמאי וכולל:
- פקודות ייבוא
- טעינת תצורה
- יישומי סוכנים לדוגמה
- תוצאות צפויות בתאי markdown

## סגנון קוד

### מוסכמות Python

- **גרסת Python**: 3.12+
- **סגנון קוד**: עקוב אחר מוסכמות PEP 8 של Python
- **Notebooks**: השתמש בתאי markdown ברורים להסבר מושגים
- **ייבוא**: קבץ לפי ספרייה סטנדרטית, צד שלישי, ייבוא מקומי

### מוסכמות Jupyter Notebook

- כלול תאי markdown תיאוריים לפני תאי קוד
- הוסף דוגמאות פלט ב-notebooks לצורך התייחסות
- השתמש בשמות משתנים ברורים התואמים למושגי השיעור
- שמור על סדר הפעלת notebook ליניארי (תא 1 → 2 → 3...)

### ארגון קבצים

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
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
2. **welcome-issue.yml** - ברכה ליוצרי בעיות חדשים
3. **welcome-pr.yml** - ברכה לתורמי pull request חדשים

### פריסה

זהו מאגר חינוכי - אין תהליך פריסה. משתמשים:
1. מבצעים fork או משכפלים את המאגר
2. מפעילים notebooks באופן מקומי או ב-GitHub Codespaces
3. לומדים על ידי שינוי וניסוי בדוגמאות

## הנחיות Pull Request

### לפני הגשה

1. **בדוק את השינויים שלך:**
   - הפעל לחלוטין את ה-notebooks המושפעים
   - ודא שכל התאים פועלים ללא שגיאות
   - בדוק שהתוצאות מתאימות

2. **עדכוני תיעוד:**
   - עדכן README.md אם מוסיפים מושגים חדשים
   - הוסף הערות ב-notebooks עבור קוד מורכב
   - ודא שתאי markdown מסבירים את המטרה

3. **שינויים בקבצים:**
   - הימנע מהתחייבות קבצי `.env` (השתמש ב-`.env.example`)
   - אל תתחייב תיקיות `venv/` או `__pycache__/`
   - שמור על פלט notebook כאשר הוא מדגים מושגים
   - הסר קבצים זמניים ו-notebooks גיבוי (`*-backup.ipynb`)

### פורמט כותרת PR

השתמש בכותרות תיאוריות:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### בדיקות נדרשות

- notebooks צריכים לפעול ללא שגיאות
- קבצי README צריכים להיות ברורים ומדויקים
- עקוב אחר תבניות קוד קיימות במאגר
- שמור על עקביות עם שיעורים אחרים

## הערות נוספות

### בעיות נפוצות

1. **אי התאמה בגרסת Python:**
   - ודא שמשתמשים ב-Python 3.12+
   - חבילות מסוימות עשויות לא לעבוד עם גרסאות ישנות יותר
   - השתמש ב-`python3 -m venv` כדי לציין גרסת Python במפורש

2. **משתני סביבה:**
   - תמיד צור `.env` מ-`.env.example`
   - אל תתחייב קובץ `.env` (הוא ב-`.gitignore`)
   - אסימון GitHub צריך הרשאות מתאימות

3. **קונפליקטים בחבילות:**
   - השתמש בסביבת וירטואלית חדשה
   - התקן מ-`requirements.txt` במקום חבילות בודדות
   - ייתכן ש-notebooks מסוימים ידרשו חבילות נוספות המוזכרות בתאי markdown שלהם

4. **שירותי Azure:**
   - שירותי Azure AI דורשים מנוי פעיל
   - תכונות מסוימות הן ספציפיות לאזור
   - מגבלות רמת חינם חלות על GitHub Models

### מסלול למידה

התקדמות מומלצת דרך השיעורים:
1. **00-course-setup** - התחל כאן להגדרת הסביבה
2. **01-intro-to-ai-agents** - הבן את יסודות סוכני AI
3. **02-explore-agentic-frameworks** - למד על מסגרות עבודה שונות
4. **03-agentic-design-patterns** - תבניות עיצוב מרכזיות
5. המשך דרך שיעורים ממוספרים באופן רציף

### בחירת מסגרת עבודה

בחר מסגרת עבודה בהתאם למטרות שלך:
- **למידה/פרוטוטיפ**: Semantic Kernel + GitHub Models (חינם)
- **מערכות רב-סוכנים**: AutoGen
- **תכונות עדכניות**: Microsoft Agent Framework (MAF)
- **פריסה בייצור**: Azure AI Agent Service

### קבלת עזרה

- הצטרף ל-[Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- עיין בקבצי README של שיעורים להנחיות ספציפיות
- בדוק את [README.md](./README.md) הראשי לסקירת הקורס
- עיין ב-[Course Setup](./00-course-setup/README.md) להוראות התקנה מפורטות

### תרומה

זהו פרויקט חינוכי פתוח. תרומות מתקבלות בברכה:
- שיפור דוגמאות קוד
- תיקון שגיאות או טעויות
- הוספת הערות מבהירות
- הצעת נושאי שיעור חדשים
- תרגום לשפות נוספות

ראה [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) לצרכים נוכחיים.

## הקשר ספציפי לפרויקט

### תמיכה רב-לשונית

מאגר זה משתמש במערכת תרגום אוטומטית:
- תמיכה ב-50+ שפות
- תרגומים בתיקיות `/translations/<lang-code>/`
- תהליך עדכון תרגומים מנוהל על ידי GitHub Actions
- קבצי מקור באנגלית בשורש המאגר

### מבנה שיעור

כל שיעור עוקב אחר תבנית עקבית:
1. תמונת וידאו עם קישור
2. תוכן שיעור כתוב (README.md)
3. דוגמאות קוד במסגרות עבודה שונות
4. מטרות למידה ודרישות מוקדמות
5. משאבי למידה נוספים מקושרים

### תבנית שמות דוגמאות קוד

פורמט: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - שיעור 4, Semantic Kernel
- `07-autogen.ipynb` - שיעור 7, AutoGen
- `14-python-agent-framework.ipynb` - שיעור 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - שיעור 14, MAF .NET

### תיקיות מיוחדות

- `translated_images/` - תמונות מתורגמות עבור תרגומים
- `images/` - תמונות מקור עבור תוכן באנגלית
- `.devcontainer/` - תצורת מכולת פיתוח של VS Code
- `.github/` - תהליכי עבודה ותבניות של GitHub Actions

### תלות

חבילות מרכזיות מ-`requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - מסגרת AutoGen
- `semantic-kernel` - מסגרת Semantic Kernel
- `agent-framework` - מסגרת Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - שירותי Azure AI
- `azure-search-documents` - אינטגרציה של חיפוש Azure AI
- `chromadb` - מסד נתונים וקטורי לדוגמאות RAG
- `chainlit` - מסגרת UI לצ'אט
- `browser_use` - אוטומציה של דפדפן עבור סוכנים
- `mcp[cli]` - תמיכה בפרוטוקול הקשר מודל
- `mem0ai` - ניהול זיכרון עבור סוכנים

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.