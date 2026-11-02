---
name: microsoft-docs
---
# Microsoft Docs

Навички дослідження для екосистеми технологій Microsoft. Охоплює learn.microsoft.com та документацію, що знаходиться за його межами (VS Code, GitHub, Aspire, Agent Framework репозиторії).

---

## За замовчуванням: Microsoft Learn MCP

Використовуйте ці інструменти для **всього на learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows та інше. Це основний інструмент для більшості запитів до документації Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Пошук learn.microsoft.com — концепції, керівництва, навчальні посібники, конфігурація |
| `microsoft_code_sample_search` | Пошук робочих фрагментів коду з документації Learn. Використовуйте `language` (`python`, `csharp` та ін.) для кращих результатів |
| `microsoft_docs_fetch` | Отримання повного вмісту сторінки за конкретним URL (коли витяги з пошуку недостатні) |

Використовуйте `microsoft_docs_fetch` після пошуку, коли потрібні повні навчальні посібники, усі параметри конфігурації або коли витяги пошуку скорочені.

---

## Винятки: Коли використовувати інші інструменти

Наступні категорії розташовані **поза межами** learn.microsoft.com. Натомість використовуйте вказаний інструмент.

### Aspire — Використовуйте Aspire MCP Server (бажано) або Context7

Документація Aspire розміщена на **aspire.dev**, а не в Learn. Найкращий інструмент залежить від вашої версії Aspire CLI:

**CLI 13.2+** (рекомендовано) — сервер Aspire MCP включає вбудовані інструменти пошуку документації:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Перелічує всю доступну документацію з aspire.dev |
| `search_docs` | Вагомий лексичний пошук по контенту aspire.dev |
| `get_doc` | Отримує конкретний документ за слагом |

Ці інструменти з'явилися в Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Для оновлення: `aspire update --self --channel daily`.

**CLI 13.1** — Сервер MCP забезпечує пошук інтеграцій (`list_integrations`, `get_integration_docs`), але **не** пошук документації. Використовуйте Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Основний — керівництва, інтеграції, довідка CLI, розгортання |
| `/microsoft/aspire` | Джерело часу виконання — внутрішній API, деталі реалізації |
| `/communitytoolkit/aspire` | Спільнотні інтеграції — Go, Java, Node.js, Ollama |

### VS Code — Використовуйте Context7

Документація VS Code знаходиться на **code.visualstudio.com**, а не на Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Документація користувача — налаштування, функції, налагодження, віддалена розробка |
| `/websites/code_visualstudio_api` | API розширень — вебперегляди, TreeViews, команди, пункти внеску |

### GitHub — Використовуйте Context7

Документація GitHub знаходиться на **docs.github.com** та **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, репозиторії, безпека, адміністрування, Copilot |
| `/websites/cli_github` | Команди та прапорці GitHub CLI (`gh`) |

### Agent Framework — Використовуйте Learn MCP + Context7

Навчальні посібники Agent Framework розміщені на learn.microsoft.com (використовуйте `microsoft_docs_search`), але **репозиторій GitHub** містить деталі API, які часто оновлюються раніше за опубліковану документацію — особливо довідник DevUI REST API, параметри CLI та інтеграції .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Навчальні посібники — керівництва DevUI, трасування, оркестрація робочих процесів |
| `/microsoft/agent-framework` | Деталі API — кінцеві точки DevUI REST, прапорці CLI, автентифікація, .NET `AddDevUI`/`MapDevUI` |

**Порада для DevUI:** Спершу зверніться до джерела сайту Learn для керівництв по використанню, а потім — до джерела репозиторію для деталей API (схеми кінцевих точок, конфігурація проксі, маркери автентифікації).

---

## Налаштування Context7

Щоб здійснити будь-який запит у Context7, спершу отримайте library ID (одноразово за сесію):

1. Викличте `mcp_context7_resolve-library-id` з назвою технології
2. Викличте `mcp_context7_query-docs` з отриманим library ID та конкретним запитом

---

## Написання ефективних запитів

Будьте конкретними — вказуйте версію, мету та мову:

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

Включайте контекст:
- **Версія** коли це доречно (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Мета завдання** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Мова** для полілінгвальних документів (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->