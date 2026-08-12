---
name: microsoft-docs
description: Запрашивайте официальную документацию Microsoft, чтобы находить концепции,
  учебники и примеры кода по Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  и другим. Используется Microsoft Learn MCP по умолчанию, а для контента, размещённого
  вне learn.microsoft.com, — Context7 и Aspire MCP.
---
# Microsoft Docs

Навык исследования для экосистемы технологий Microsoft. Охватывает learn.microsoft.com и документацию, которая размещена вне него (VS Code, GitHub, Aspire, репозитории Agent Framework).

---

## Default: Microsoft Learn MCP

Используйте эти инструменты для **всего на learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows и прочее. Это основной инструмент для подавляющего большинства запросов по документации Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Поиск по learn.microsoft.com — концепции, руководства, туториалы, конфигурация |
| `microsoft_code_sample_search` | Поиск работающих фрагментов кода из документации Learn. Укажите `language` (`python`, `csharp` и т. д.) для лучших результатов |
| `microsoft_docs_fetch` | Получить полный контент страницы по конкретному URL (когда фрагментов поиска недостаточно) |

Используйте `microsoft_docs_fetch` после поиска, когда вам нужны полные руководства, все параметры конфигурации или когда фрагменты поиска обрезаны.

---

## Exceptions: When to Use Other Tools

Следующие категории размещены **вне** learn.microsoft.com. Используйте указанный инструмент вместо этого.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Документация Aspire размещена на **aspire.dev**, а не в Learn. Лучший инструмент зависит от версии Aspire CLI:

**CLI 13.2+** (рекомендуется) — Сервер Aspire MCP включает встроенные инструменты поиска по документации:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Перечисляет всю доступную документацию с aspire.dev |
| `search_docs` | Взвешенный лексический поиск по содержимому aspire.dev |
| `get_doc` | Получает конкретный документ по slug |

Они включены в Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Чтобы обновить: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP сервер предоставляет поиск интеграций (`list_integrations`, `get_integration_docs`), но **не** поиск по документации. В этом случае используйте Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Основное — руководства, интеграции, справочник CLI, деплоймент |
| `/dotnet/aspire` | Исходники рантайма — внутренняя реализация API, детали реализации |
| `/communitytoolkit/aspire` | Интеграции сообщества — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

Документация VS Code размещена на **code.visualstudio.com**, а не в Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Документация для пользователей — настройки, функции, отладка, удаленная разработка |
| `/websites/code_visualstudio_api` | API расширений — webviews, TreeViews, команды, точки расширения |

### GitHub — Use Context7

Документация GitHub размещена на **docs.github.com** и **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, репозитории, безопасность, администрирование, Copilot |
| `/websites/cli_github` | Команды и флаги GitHub CLI (`gh`) |

### Agent Framework — Use Learn MCP + Context7

Учебные материалы по Agent Framework находятся на learn.microsoft.com (используйте `microsoft_docs_search`), но **репозиторий на GitHub** содержит детали уровня API, которые часто опережают опубликованную документацию — в частности справочник DevUI REST API, параметры CLI и интеграция с .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Учебники — руководства по DevUI, трассировка, оркестрация рабочих процессов |
| `/microsoft/agent-framework` | Детали API — конечные точки DevUI REST, флаги CLI, аутентификация, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Сначала запрашивайте на сайте Learn руководства по практическому использованию, затем обращайтесь к исходникам репозитория для деталей уровня API (схемы конечных точек, конфиг прокси, токены аутентификации).

---

## Context7 Setup

Для любого запроса в Context7 сначала разрешите идентификатор библиотеки (один раз за сессию):

1. Вызовите `mcp_context7_resolve-library-id` с названием технологии
2. Вызовите `mcp_context7_query-docs` с возвращенным идентификатором библиотеки и конкретным запросом

---

## Writing Effective Queries

Будьте конкретны — указывайте версию, намерение и язык:

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
**Отказ от ответственности**:
Этот документ был переведён с использованием сервиса автоматического перевода на базе ИИ [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или неверные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->