---
name: microsoft-docs
description: Запитуйте офіційну документацію Microsoft, щоб знаходити концепції, навчальні
  посібники та приклади коду щодо Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  та іншого. Використовує Microsoft Learn MCP за замовчуванням, а для вмісту, що знаходиться
  поза learn.microsoft.com, — Context7 та Aspire MCP.
---
# Microsoft Docs

Навичка дослідження для екосистеми технологій Microsoft. Охоплює learn.microsoft.com та документацію, що розміщується поза нею (репозиторії VS Code, GitHub, Aspire, Agent Framework).

---

## Default: Microsoft Learn MCP

Використовуйте ці інструменти для **всього на learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows та інше. Це основний інструмент для більшості запитів по документації Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Пошук по learn.microsoft.com — концепції, керівництва, підручники, конфігурація |
| `microsoft_code_sample_search` | Знайти робочі фрагменти коду з документації Learn. Передайте `language` (`python`, `csharp`, тощо) для кращих результатів |
| `microsoft_docs_fetch` | Отримати повний вміст сторінки з конкретного URL (коли уривків пошуку недостатньо) |

Використовуйте `microsoft_docs_fetch` після пошуку, коли вам потрібні повні підручники, всі параметри конфігурації або коли уривки пошуку обрізані.

---

## Exceptions: When to Use Other Tools

Наступні категорії розміщуються **поза** learn.microsoft.com. Замість цього використовуйте вказаний інструмент.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Документація Aspire розміщена на **aspire.dev**, а не в Learn. Найкращий інструмент залежить від вашої версії Aspire CLI:

**CLI 13.2+** (рекомендовано) — Aspire MCP server включає вбудовані інструменти пошуку документації:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Перелічує всю доступну документацію з aspire.dev |
| `search_docs` | Зважений лексичний пошук по контенту aspire.dev |
| `get_doc` | Отримує конкретний документ за slug |

Вони доступні в Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Щоб оновити: `aspire update --self --channel daily`. Див.: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP server забезпечує пошук інтеграцій (`list_integrations`, `get_integration_docs`), але **не** пошук документації. У такому випадку поверніться до Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Основне — керівництва, інтеграції, довідник CLI, розгортання |
| `/dotnet/aspire` | Джерело рантайму — внутрішні API, деталі реалізації |
| `/communitytoolkit/aspire` | Інтеграції спільноти — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

Документація VS Code розміщена на **code.visualstudio.com**, а не в Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Документи для користувачів — налаштування, функції, налагодження, віддалена розробка |
| `/websites/code_visualstudio_api` | API розширень — webviews, TreeViews, команди, точки внеску |

### GitHub — Use Context7

Документація GitHub розміщена на **docs.github.com** та **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, репозиторії, безпека, адміністрування, Copilot |
| `/websites/cli_github` | Команди та прапорці GitHub CLI (`gh`) |

### Agent Framework — Use Learn MCP + Context7

Підручники Agent Framework знаходяться на learn.microsoft.com (використовуйте `microsoft_docs_search`), але **репозиторій на GitHub** містить API-рівневі деталі, які часто випереджають опубліковану документацію — особливо довідник DevUI REST API, опції CLI та інтеграція з .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Підручники — керівництва DevUI, трасування, оркестрація робочих процесів |
| `/microsoft/agent-framework` | Деталі API — кінцеві точки DevUI REST, прапорці CLI, автентифікація, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Запитуйте джерело сайту Learn за керівництвами «як зробити», а потім джерело репозиторію для API-рівневих специфікацій (схеми кінцевих точок, налаштування проксі, токени автентифікації).

---

## Context7 Setup

Для будь-якого запиту до Context7 спочатку визначте library ID (одноразово за сесію):

1. Викличте `mcp_context7_resolve-library-id` з назвою технології  
2. Викличте `mcp_context7_query-docs` з отриманим library ID та конкретним запитом

---

## Writing Effective Queries

Будьте конкретні — вказуйте версію, мету та мову:

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
- **Version** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Застереження:
Цей документ було перекладено за допомогою сервісу машинного перекладу на основі ШІ Co-op Translator (https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, зверніть увагу, що автоматизовані переклади можуть містити помилки чи неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звернутися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->