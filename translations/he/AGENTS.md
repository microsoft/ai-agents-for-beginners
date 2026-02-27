# AGENTS.md

## Project Overview

מאגר זה מכיל "AI Agents for Beginners" - קורס חינוכי מקיף המלמד הכל הנדרש לבניית סוכני AI. הקורס מורכב מ-15+ שיעורים המכסים יסודות, תבניות עיצוב, מסגרות ועבודה בפרודקשן של סוכני AI.

**Key Technologies:**
- Python 3.12+
- Jupyter Notebooks ללמידה אינטראקטיבית
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architecture:**
- מבנה מבוסס שיעורים (00-15+ directories)
- כל שיעור מכיל: תיעוד README, דוגמאות קוד (Jupyter notebooks), ותמונות
- תמיכה ברב-שפות דרך מערכת תרגום אוטומטית
- מחברת Python אחת לכל שיעור המשתמשת ב-Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 or higher
- Azure subscription (for Azure AI Foundry)
- Azure CLI installed and authenticated (`az login`)

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
   source venv/bin/activate  # ב-Windows: venv\Scripts\activate
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
- `AZURE_AI_PROJECT_ENDPOINT` - נקודת הקצה של פרויקט Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - שם פריסת המודל (e.g., gpt-4o)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - נקודת הקצה של Azure AI Search
- `AZURE_SEARCH_API_KEY` - מפתח ה-API של Azure AI Search

Authentication: הרץ `az login` לפני הרצת המחברות (משתמש ב-`AzureCliCredential`).

## Development Workflow

### Running Jupyter Notebooks

כל שיעור מכיל מספר מחברות Jupyter עבור מסגרות שונות:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate to a lesson directory** (e.g., `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - שימוש ב-Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - שימוש ב-Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- דורש מנוי Azure
- משתמש ב-`AzureAIProjectAgentProvider` עבור Agent Service V2 (agents visible in Foundry portal)
- מוכן לייצור עם תצפית מובנית
- תבנית קבצים: `*-python-agent-framework.ipynb`

## Testing Instructions

זהו מאגר חינוכי עם קוד לדוגמה ולא קוד ייצור עם בדיקות אוטומטיות. כדי לאמת את ההתקנה והשינויים שלך:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # צריך להיות 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # המר את המחברת לסקריפט והרץ (יבוא בדיקות)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Running Individual Notebooks

פתח מחברות ב-Jupyter והרץ תאים לפי הסדר. כל מחברת עצמאית וכוללת:
- Import statements
- טעינת תצורה
- מימושי סוכן לדוגמה
- פלטים צפויים בתאי markdown

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: עקוב אחרי הנחיות PEP 8 של Python
- **Notebooks**: השתמש בתאי markdown ברורים כדי להסביר רעיונות
- **Imports**: קבץ לפי ספריית הסטנדרט, צד שלישי, וייבוא מקומי

### Jupyter Notebook Conventions

- כלול תאי markdown תיאוריים לפני תאי קוד
- הוסף דוגמאות פלט במחברות כהפניה
- השתמש בשמות משתנים ברורים התואמים למושגי השיעור
- שמור על סדר הרצת המחברת ליניארי (cell 1 → 2 → 3...)

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
2. **welcome-issue.yml** - מקבל בברכה יוצרי ה-issue החדשים
3. **welcome-pr.yml** - מקבל בברכה תורמי ה-pull request החדשים

### Deployment

זהו מאגר חינוכי - אין תהליך פריסה. משתמשים:
1. Fork or clone the repository
2. הרץ מחברות מקומית או ב-GitHub Codespaces
3. למד על ידי שינוי וניסוי בדוגמאות

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - הרץ את המחברות המושפעות במלואן
   - וודא שכל התאים מבוצעים ללא שגיאות
   - בדוק שהתוצאות מתאימות

2. **Documentation updates:**
   - עדכן README.md אם מוסיפים מושגים חדשים
   - הוסף הערות במחברות עבור קוד מורכב
   - וודא שתאי ה-markdown מסבירים את המטרה

3. **File changes:**
   - הימנע מלהתחייב לקבצי `.env` (השתמש ב-`.env.example`)
   - אל תתחייב לתיקיות `venv/` או `__pycache__/`
   - שמור על פלטי מחברות כשהם ממחישים מושגים
   - הסר קבצים זמניים ומחברות גיבוי (`*-backup.ipynb`)

### PR Title Format

השתמש בכותרות תיאוריות:
- `[Lesson-XX] הוסף דוגמה חדשה ל-<concept>`
- `[Fix] תקן שגיאת הקלדה ב-lesson-XX README`
- `[Update] שפר דוגמת קוד ב-lesson-XX`
- `[Docs] עדכן הוראות התקנה`

### Required Checks

- יש להבטיח שהמחברות ירוצו ללא שגיאות
- קבצי README צריכים להיות ברורים ומדויקים
- עקוב אחרי דפוסי הקוד הקיימים במאגר
- שמור על עקביות עם שיעורים אחרים

## Additional Notes

### Common Gotchas

1. **Python version mismatch:**
   - ודא שמשתמשים ב-Python 3.12+
   - חבילות מסוימות עשויות לא לעבוד עם גרסאות ישנות יותר
   - השתמש ב-`python3 -m venv` כדי לציין במפורש את גרסת ה-Python

2. **Environment variables:**
   - תמיד צור את `.env` מתוך `.env.example`
   - אל תתחייב לקובץ `.env` (הוא נמצא ב-`.gitignore`)
   - ל-Token של GitHub דרושות ההרשאות המתאימות

3. **Package conflicts:**
   - השתמש בסביבת וירטואלית חדשה
   - התקן מתוך `requirements.txt` במקום חבילות בודדות
   - ייתכן שחלק מהמחברות ידרשו חבילות נוספות שמצוינות בתאי ה-markdown שלהן

4. **Azure services:**
   - שירותי Azure AI דורשים מנוי פעיל
   - חלק מהתכונות תלויות באזור גיאוגרפי
   - הגבלות השכבה החינמית חלות על GitHub Models

### Learning Path

התקדמות מומלצת דרך השיעורים:
1. **00-course-setup** - התחל כאן להגדרת הסביבה
2. **01-intro-to-ai-agents** - הבן את יסודות סוכני ה-AI
3. **02-explore-agentic-frameworks** - למד על מסגרות שונות
4. **03-agentic-design-patterns** - דפוסי עיצוב מרכזיים
5. המשך דרך השיעורים המספריים בסדר

### Framework Selection

בחר מסגרת בהתאם למטרותיך:
- **All lessons**: Microsoft Agent Framework (MAF) עם `AzureAIProjectAgentProvider`
- **Agents register server-side** in Azure AI Foundry Agent Service V2 and are visible in the Foundry portal

### Getting Help

- הצטרף ל-[Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- עיין בקבצי README של השיעורים להנחיות ספציפיות
- בדוק את ה-[README.md](./README.md) הראשי לקבלת סקירת הקורס
- עיין ב-[הגדרת הקורס](./00-course-setup/README.md) להוראות הגדרה מפורטות

### Contributing

זהו פרויקט חינוכי פתוח. תרומות מתקבלות בברכה:
- שפר דוגמאות קוד
- תקן שגיאות הקלדה או שגיאות
- הוסף הערות מבהירות
- הצע נושאים לשיעורים חדשים
- תרגם לשפות נוספות

ראה את [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) לצרכים נוכחיים.

## Project-Specific Context

### Multi-Language Support

מאגר זה משתמש במערכת תרגום אוטומטית:
- תמיכה בלמעלה מ-50 שפות
- תרגומים בתיקיות `/translations/<lang-code>/`
- צנרת GitHub Actions מטפלת בעדכוני תרגום
- קבצי המקור באנגלית בשורש המאגר

### Lesson Structure

כל שיעור עוקב אחרי דפוס קבוע:
1. תמונת ממוזערת של וידאו עם קישור
2. תוכן שיעור כתוב (README.md)
3. דוגמאות קוד במסגרות שונות
4. מטרות למידה ודרישות מוקדמות
5. משאבי למידה נוספים מקושרים

### Code Sample Naming

פורמט: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - שיעור 1, MAF Python
- `14-sequential.ipynb` - שיעור 14, דפוסים מתקדמים של MAF

### Special Directories

- `translated_images/` - תמונות מותאמות לשפות עבור תרגומים
- `images/` - תמונות מקור עבור תוכן באנגלית
- `.devcontainer/` - קונפיגורציית מיכל פיתוח ל-VS Code
- `.github/` - צנרות ותבניות של GitHub Actions

### Dependencies

חבילות מפתח מתוך `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - תמיכה בפרוטוקול Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - שירותי Azure AI
- `azure-identity` - אימות Azure (AzureCliCredential)
- `azure-search-documents` - אינטגרציה עם Azure AI Search
- `mcp[cli]` - תמיכה ב-Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
הצהרת אחריות:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית Co-op Translator (https://github.com/Azure/co-op-translator). אמנם אנו שואפים לדיוק, אך יש להשים לב שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להסתמך על המסמך המקורי בשפתו כמקור הסמכות. לפרטים קריטיים מומלץ להיעזר בתרגום מקצועי על ידי מתרגם אנושי. איננו אחראים לכל אי-הבנה או פירוש שגוי שעלול לנבוע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->