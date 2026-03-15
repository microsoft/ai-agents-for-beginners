# AGENTS.md

## Project Overview

מאגר זה מכיל "AI Agents for Beginners" - קורס חינוכי מקיף המלמד הכל שצריך לבנות סוכני AI. הקורס מורכב מ-15+ שיעורים המכסים יסודות, תבניות עיצוב, מסגרות, ופריסה לפרודקשן של סוכני AI.

**טכנולוגיות מרכזיות:**
- Python 3.12+
- Jupyter Notebooks ללמידה אינטראקטיבית
- מסגרות AI: Microsoft Agent Framework (MAF)
- שירותי Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**ארכיטקטורה:**
- מבנה מבוסס שיעורים (תיקיות 00-15+)
- כל שיעור מכיל: תיעוד README, דוגמאות קוד (מחברות Jupyter), ותמונות
- תמיכה ברב-שפות באמצעות מערכת תרגום אוטומטית
- מחברת Python אחת לכל שיעור המשתמשת ב-Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 או גרסה גבוהה יותר
- מנוי Azure (עבור Azure AI Foundry)
- Azure CLI מותקן ומאומת (`az login`)

### Initial Setup

1. **Clone or fork the repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # או
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Create and activate Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # ב־Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # ערוך את קובץ .env עם מפתחות ה-API ונקודות הקצה שלך
   ```

### Required Environment Variables

For **Azure AI Foundry** (Required):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-4o)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

אימות: הרץ את `az login` לפני הרצת המחברות (משתמש ב-`AzureCliCredential`).

## Development Workflow

### Running Jupyter Notebooks

כל שיעור מכיל מספר מחברות Jupyter עבור מסגרות שונות:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate to a lesson directory** (e.g., `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - Using Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Using Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- דורש מנוי Azure
- משתמש ב-`AzureAIProjectAgentProvider` עבור Agent Service V2 (סוכנים נראים בפורטל Foundry)
- מוכן לסביבת ייצור עם יכולות תצפית מובנות
- דפוס קבצים: `*-python-agent-framework.ipynb`

## Testing Instructions

זהו מאגר חינוכי עם קוד לדוגמה במקום קוד פרודקשן עם בדיקות אוטומטיות. כדי לאמת את ההתקנה והשינויים שלך:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # צריך להיות 3.12 ומעלה
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # המר מחברת לסקריפט והרץ (ייבוא עבור הבדיקות)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Running Individual Notebooks

פתח מחברות ב-Jupyter והריץ תאים ברצף. כל מחברת עצמאית וכוללת:
- הוראות import
- טעינת תצורה
- מימושי דוגמה של סוכנים
- תוצאות צפויות בתאי Markdown

## Code Style

### Python Conventions

- **גרסת Python**: 3.12+
- **סגנון קוד**: פעל לפי קונבנציות PEP 8 של Python
- **מחברות**: השתמש בתאי Markdown ברורים כדי להסביר מושגים
- **ייבוא**: קבץ לפי ספרייה סטנדרטית, חבילות צד-שלישי, וייבוא מקומי

### Jupyter Notebook Conventions

- כלול תאי Markdown תיאוריים לפני תאי קוד
- הוסף דוגמאות פלט במחברות כהפניה
- השתמש בשמות משתנים ברורים התואמים למושאי השיעור
- שמור על סדר הרצת המחברת לינארי (תא 1 → 2 → 3...)

### File Organization

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Build and Deployment

### Building Documentation

מאגר זה משתמש ב-Markdown לתיעוד:
- קבצי README.md בכל תיקיית שיעור
- README.md הראשי בשורש המאגר
- מערכת תרגום אוטומטית באמצעות GitHub Actions

### CI/CD Pipeline

ממוקם ב-`.github/workflows/`:

1. **co-op-translator.yml** - תרגום אוטומטי ל-50+ שפות
2. **welcome-issue.yml** - מקבל בברכה יוצרים של איסיוז חדשים
3. **welcome-pr.yml** - מקבל בברכה תורמי Pull Request חדשים

### Deployment

זהו מאגר חינוכי - אין תהליך פריסה. משתמשים:
1. Fork או שכפל את המאגר
2. הרץ מחברות באופן מקומי או ב-GitHub Codespaces
3. למד על ידי שינוי וניסוי בדוגמאות

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - הרץ את המחברות המושפעות באופן מלא
   - וודא שכל התאים יורצו ללא שגיאות
   - בדוק שהתפוקות מתאימות

2. **Documentation updates:**
   - עדכן README.md אם מוסיפים מושגים חדשים
   - הוסף הערות במחברות עבור קוד מורכב
   - ודא שתאי Markdown מסבירים את המטרה

3. **File changes:**
   - הימנע מלהעלות קבצי `.env` (השתמש ב-`.env.example`)
   - אל תעלה את התיקיות `venv/` או `__pycache__/`
   - השאר פלטי מחברות כאשר הם מדגימים מושגים
   - הסר קבצי זמניים ומחברות גיבוי (`*-backup.ipynb`)

### PR Title Format

השתמש בכותרות מתארות:
- `[Lesson-XX] הוסף דוגמה חדשה עבור <concept>`
- `[Fix] תקן טעות הקלדה ב-lesson-XX README`
- `[Update] שפר דוגמת קוד ב-lesson-XX`
- `[Docs] עדכן הוראות התקנה`

### Required Checks

- מחברות צריכות להתבצע ללא שגיאות
- קבצי README צריכים להיות ברורים ומדויקים
- עקוב אחרי דפוסי קוד קיימים במאגר
- שמור על עקביות עם שאר השיעורים

## Additional Notes

### Common Gotchas

1. **אי התאמה בגרסת Python:**
   - הקפד להשתמש ב-Python 3.12+
   - חבילות מסוימות עלולות לא לעבוד עם גרסאות ישנות יותר
   - השתמש ב-`python3 -m venv` כדי לציין את גרסת ה-Python במפורש

2. **משתני סביבה:**
   - תמיד צור את `.env` מתוך `.env.example`
   - אל תעלה את קובץ `.env` (הוא נמצא ב-`.gitignore`)
   - ל-Token של GitHub צריך הרשאות מתאימות

3. **קונפליקטים של חבילות:**
   - השתמש בסביבת וירטואלית חדשה
   - התקן מ-`requirements.txt` במקום חבילות בודדות
   - חלק מהמחברות עשויות לדרוש חבילות נוספות המוזכרות בתאי Markdown שלהן

4. **שירותי Azure:**
   - שירותי Azure AI דורשים מנוי פעיל
   - חלק מהתכונות תלויות באזור
   - מגבלות השכבה החינמית חלות על GitHub Models

### Learning Path

המלצה על סדר הלמידה דרך השיעורים:
1. **00-course-setup** - התחל כאן להגדרת הסביבה
2. **01-intro-to-ai-agents** - הבן את היסודות של סוכני AI
3. **02-explore-agentic-frameworks** - למד על מסגרות שונות
4. **03-agentic-design-patterns** - דפוסי עיצוב מרכזיים
5. המשך בסדר המספרי של השיעורים

### Framework Selection

בחר מסגרת בהתאם למטרותיך:
- **כל השיעורים**: Microsoft Agent Framework (MAF) עם `AzureAIProjectAgentProvider`
- **סוכנים נרשמים בצד השרת** ב-Azure AI Foundry Agent Service V2 ונראים בפורטל Foundry

### Getting Help

- הצטרף ל-[קהילת Microsoft Foundry ב-Discord](https://aka.ms/ai-agents/discord)
- עיין בקבצי README של השיעורים להנחיות ספציפיות
- עיין ב-[README.md](./README.md) הראשי לקבלת סקירת הקורס
- עיין ב-[הגדרת הקורס](./00-course-setup/README.md) להוראות הגדרה מפורטות

### Contributing

זהו פרויקט חינוכי פתוח. תרומות מתקבלות בברכה:
- שפר דוגמאות קוד
- תקן שגיאות הקלדה או טעויות
- הוסף הערות מבהירות
- הצע נושאים חדשים לשיעורים
- תרגם לשפות נוספות

עיין ב-[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) לצרכים הנוכחיים.

## Project-Specific Context

### Multi-Language Support

מאגר זה משתמש במערכת תרגום אוטומטית:
- תמיכה ב-50+ שפות
- תרגומים בתיקיות `/translations/<lang-code>/`
- workflow של GitHub Actions מטפל בעדכוני תרגום
- קבצי המקור באנגלית נמצאים בשורש המאגר

### Lesson Structure

כל שיעור עוקב אחרי תבנית קבועה:
1. תמונת ממוזערת של וידאו עם קישור
2. תוכן שיעור כתוב (README.md)
3. דוגמאות קוד במסגרות מרובות
4. מטרות למידה ודרישות מוקדמות
5. משאבי למידה נוספים מקושרים

### Code Sample Naming

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - שיעור 1, MAF Python
- `14-sequential.ipynb` - שיעור 14, דפוסי MAF מתקדמים

### Special Directories

- `translated_images/` - תמונות מתורגמות מקומית
- `images/` - תמונות מקוריות לתוכן באנגלית
- `.devcontainer/` - קביעת תצורת מכולת פיתוח VS Code
- `.github/` - GitHub Actions workflows ותבניות

### Dependencies

חבילות מרכזיות מתוך `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - תמיכה בפרוטוקול Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - שירותי Azure AI
- `azure-identity` - אימות Azure (AzureCliCredential)
- `azure-search-documents` - אינטגרציה עם Azure AI Search
- `mcp[cli]` - תמיכה בפרוטוקול Model Context

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
הצהרת אחריות:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לשים לב כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש לראות את המסמך המקורי בשפתו כמקור הסמכותי. עבור מידע קריטי מומלץ תרגום מקצועי על ידי מתרגם אנושי. איננו נושאים באחריות לכל אי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->