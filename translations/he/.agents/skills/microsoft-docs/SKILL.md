---
name: microsoft-docs
description: שאילתה בתיעוד הרשמי של Microsoft למציאת מושגים, מדריכים ודוגמאות קוד
  ב-Azure, .NET, Agent Framework, Aspire, VS Code, GitHub ועוד. משתמש ב-Microsoft
  Learn MCP כברירת מחדל, עם Context7 ו-Aspire MCP עבור תוכן שנמצא מחוץ ל-learn.microsoft.com.
---
# Microsoft Docs

מיומנות מחקר לאקו-סיסטמה הטכנולוגית של Microsoft. כולל את learn.microsoft.com ואת התיעוד הקיים מחוצה לו (VS Code, GitHub, Aspire, מאגרי Agent Framework).

---

## Default: Microsoft Learn MCP

Use these tools for **everything on learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, and more. This is the primary tool for the vast majority of Microsoft documentation queries.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | חפש ב-learn.microsoft.com — מושגים, מדריכים, הדרכות, הגדרות |
| `microsoft_code_sample_search` | מצא קטעי קוד פועלים מתוך מסמכי Learn. העבר `language` (`python`, `csharp`, וכו') לתוצאות הטובות ביותר |
| `microsoft_docs_fetch` | השג תוכן עמוד מלא מ-URL ספציפי (כשקטעי החיפוש לא מספיקים) |

Use `microsoft_docs_fetch` after search when you need complete tutorials, all config options, or when search excerpts are truncated.

---

## Exceptions: When to Use Other Tools

The following categories live **outside** learn.microsoft.com. Use the specified tool instead.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire docs live on **aspire.dev**, not Learn. The best tool depends on your Aspire CLI version:

**CLI 13.2+** (recommended) — The Aspire MCP server includes built-in docs search tools:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | מציג את כל התיעוד הזמין מ-aspire.dev |
| `search_docs` | חיפוש לקסיקלי משוקלל בתכני aspire.dev |
| `get_doc` | משיג מסמך ספציפי על-ידי slug |

These ship in Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). To update: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — The MCP server provides integration lookup (`list_integrations`, `get_integration_docs`) but **not** docs search. Fall back to Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primary — guides, integrations, CLI reference, deployment |
| `/dotnet/aspire` | Runtime source — API internals, implementation details |
| `/communitytoolkit/aspire` | Community integrations — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code docs live on **code.visualstudio.com**, not Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | תיעוד למשתמש — הגדרות, תכונות, ניפוי שגיאות, פיתוח מרחוק |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, commands, contribution points |

### GitHub — Use Context7

GitHub docs live on **docs.github.com** and **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, מאגרים, אבטחה, ניהול, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) commands and flags |

### Agent Framework — Use Learn MCP + Context7

Agent Framework tutorials are on learn.microsoft.com (use `microsoft_docs_search`), but the **GitHub repo** has API-level detail that is often ahead of published docs — particularly DevUI REST API reference, CLI options, and .NET integration.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI guides, tracing, workflow orchestration |
| `/microsoft/agent-framework` | API detail — DevUI REST endpoints, CLI flags, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** שאול את מקור אתר Learn עבור מדריכים מעשיים, ואז את מקור המאגר עבור פרטים ברמת ה-API (סכמות נקודות קצה, תצורת פרוקסי, אסימוני אימות).

---

## Context7 Setup

For any Context7 query, resolve the library ID first (one-time per session):

1. הרץ את `mcp_context7_resolve-library-id` עם שם הטכנולוגיה
2. הרץ את `mcp_context7_query-docs` עם מזהה הספרייה שהוחזר ושאילתה ספציפית

---

## Writing Effective Queries

Be specific — include version, intent, and language:

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

Include context:
- **גרסה** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **כוונת המשימה** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **שפה** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
הצהרת אי-אחריות:
המסמך הזה תורגם באמצעות שירות תרגום בבינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לשים לב כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי שבשפה המקורית כמקור הסמכות. למידע קריטי מומלץ להיעזר בתרגום מקצועי על ידי מתרגם אנושי. איננו נושאים באחריות לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->