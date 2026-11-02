---
name: microsoft-docs
description: שאילתה לתיעוד הרשמי של מיקרוסופט למציאת מושגים, מדריכים, ודוגמאות קוד
  ב-Azure, .NET, Agent Framework, Aspire, VS Code, GitHub, ועוד. משתמש ב-Microsoft
  Learn MCP כברירת מחדל, עם Context7 ו-Aspire MCP עבור תוכן שנמצא מחוץ ל-learn.microsoft.com.
---
# Microsoft Docs

מיומנות מחקר לאקוסיסטם הטכנולוגיה של מיקרוסופט. כולל את learn.microsoft.com ותיעוד שמתארח מחוצה לו (VS Code, GitHub, Aspire, Agent Framework repos).

---

## ברירת מחדל: Microsoft Learn MCP

השתמש בכלים האלו עבור **כל דבר ב-learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, ועוד. זהו הכלי הראשי עבור רוב השאלות בנושא תיעוד של מיקרוסופט.

| כלי | מטרה |
|------|---------|
| `microsoft_docs_search` | חיפוש ב-learn.microsoft.com — מושגים, מדריכים, הדרכות, קונפיגורציה |
| `microsoft_code_sample_search` | מציאת קטעי קוד עובדים מתיעוד Learn. העבר `language` (`python`, `csharp`, וכו') לתוצאות מיטביות |
| `microsoft_docs_fetch` | קבלת תוכן עמוד מלא מכתובת URL ספציפית (כאשר קטעי החיפוש אינם מספקים) |

השתמש ב-`microsoft_docs_fetch` לאחר החיפוש כאשר אתה צריך הדרכות מלאות, את כל אפשרויות הקונפיגורציה, או כאשר קטעי החיפוש קצרים מדי.

---

## יוצאים מן הכלל: מתי להשתמש בכלים אחרים

הקטגוריות הבאות מתארחות **מחוץ** ל-learn.microsoft.com. השתמש בכלי המתאים במקום זאת.

### Aspire — השתמש ב-Aspire MCP Server (מומלץ) או ב-Context7

תיעודי Aspire מתארחים ב-**aspire.dev**, לא ב-Learn. הכלי הטוב ביותר תלוי בגרסת Aspire CLI שלך:

**CLI 13.2+** (מומלץ) — שרת Aspire MCP כולל כלים מובנים לחיפוש תיעוד:

| כלי MCP | תיאור |
|----------|-------------|
| `list_docs` | מציג את כל התיעוד הזמין מ-aspire.dev |
| `search_docs` | חיפוש לקסיקלי מושקל ברחבי תוכן aspire.dev |
| `get_doc` | משחזר מסמך ספציפי לפי סלג |

כלים אלו נשלחו ב-Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). לעדכון: `aspire update --self --channel daily`.

**CLI 13.1** — שרת MCP מספק חיפוש אינטגרציה (`list_integrations`, `get_integration_docs`) אך **לא** חיפוש תיעוד. חזור ל-Context7:

| מזהה ספריה | שימוש עבור |
|---|---|
| `/microsoft/aspire.dev` | ראשי — מדריכים, אינטגרציות, הפניה ל-CLI, פריסה |
| `/microsoft/aspire` | מקור בזמן ריצה — פרטי API פנימיים, פרטים ליישום |
| `/communitytoolkit/aspire` | אינטגרציות קהילתיות — Go, Java, Node.js, Ollama |

### VS Code — השתמש ב-Context7

תיעוד VS Code מתארח ב-**code.visualstudio.com**, לא ב-Learn.

| מזהה ספריה | שימוש עבור |
|---|---|
| `/websites/code_visualstudio` | תיעוד משתמש — הגדרות, תכונות, דיבוג, פיתוח מרחוק |
| `/websites/code_visualstudio_api` | API של הרחבות — webviews, TreeViews, פקודות, נקודות תרומה |

### GitHub — השתמש ב-Context7

תיעוד GitHub מתארח ב-**docs.github.com** ו-**cli.github.com**.

| מזהה ספריה | שימוש עבור |
|---|---|
| `/websites/github_en` | Actions, API, ריפוזיטוריות, אבטחה, ניהול, Copilot |
| `/websites/cli_github` | פקודות ודגלים של GitHub CLI (`gh`) |

### Agent Framework — השתמש ב-Learn MCP + Context7

הדרכות Agent Framework נמצאות ב-learn.microsoft.com (השתמש ב-`microsoft_docs_search`), אך **הריפוזיטורי של GitHub** מכיל פרטי API ברמת עומק שלעתים מקדימים את התיעוד המשתחרר — בפרט הפנייה ל-DevUI REST API, אפשרויות CLI, ואינטגרציה עם .NET.

| מזהה ספריה | שימוש עבור |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | הדרכות — מדריכי DevUI, ניתור, תזמון זרימות עבודה |
| `/microsoft/agent-framework` | פרטי API — נקודות קצה של DevUI REST, דגלי CLI, אימות, .NET `AddDevUI`/`MapDevUI` |

**עצה ל-DevUI:** חפש באתר Learn מדריכים מעשיים, ואז בדוק בריפוזיטורי לפרטים ברמת API (סכימות נקודות קצה, קונפיגורציית פרוקסי, אסימוני אימות).

---

## הגדרת Context7

לכל שאילתה ב-Context7, פענח את מזהה הספריה תחילה (פעם אחת לכל סשן):

1. תקרא ל-`mcp_context7_resolve-library-id` עם שם הטכנולוגיה
2. תקרא ל-`mcp_context7_query-docs` עם מזהה הספריה שהוחזר ושאילתה ספציפית

---

## כתיבת שאילתות אפקטיביות

תהיה ספציפי — כלול גרסה, כוונה, ושפה:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

כלול הקשר:
- **גרסה** כשהוא רלוונטי (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **כוונת המשימה** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **שפה** עבור תיעוד רב-לשוני (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->