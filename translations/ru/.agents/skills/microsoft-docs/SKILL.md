---
name: microsoft-docs
---
# Microsoft Docs

Навык поиска информации для экосистемы технологий Microsoft. Охватывает learn.microsoft.com и документацию, которая располагается вне его (VS Code, GitHub, Aspire, репозитории Agent Framework).

---

## По умолчанию: Microsoft Learn MCP

Используйте эти инструменты для **всего на learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows и не только. Это основной инструмент для подавляющего большинства запросов по документации Microsoft.

| Tool | Назначение |
|------|---------|
| `microsoft_docs_search` | Поиск по learn.microsoft.com — концепции, руководства, учебники, настройки |
| `microsoft_code_sample_search` | Поиск работающих примеров кода из документов Learn. Передайте `language` (`python`, `csharp` и др.) для лучших результатов |
| `microsoft_docs_fetch` | Получить полный контент по конкретному URL (когда отрывков поиска недостаточно) |

Используйте `microsoft_docs_fetch` после поиска, когда нужны полные учебники, все опции конфигурации или когда отрывки поиска обрезаны.

---

## Исключения: Когда использовать другие инструменты

Следующие категории расположены **вне** learn.microsoft.com. Используйте указанный инструмент.

### Aspire — Используйте Aspire MCP Server (предпочтительно) или Context7

Документы Aspire находятся на **aspire.dev**, а не в Learn. Лучший инструмент зависит от версии Aspire CLI:

**CLI 13.2+** (рекомендуется) — Aspire MCP сервер включает встроенные инструменты поиска документации:

| MCP Tool | Описание |
|----------|-------------|
| `list_docs` | Перечисляет всю доступную документацию с aspire.dev |
| `search_docs` | Взвешенный лексический поиск по содержимому aspire.dev |
| `get_doc` | Получает конкретный документ по slug |

Эти функции доступны в Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Для обновления: `aspire update --self --channel daily`.

**CLI 13.1** — MCP сервер предоставляет поиск интеграций (`list_integrations`, `get_integration_docs`), но **не** поиск по документации. Воспользуйтесь Context7:

| Library ID | Используется для |
|---|---|
| `/microsoft/aspire.dev` | Основное — руководства, интеграции, справочник CLI, развертывание |
| `/microsoft/aspire` | Исходники среды выполнения — детали API, реализация |
| `/communitytoolkit/aspire` | Интеграции сообщества — Go, Java, Node.js, Ollama |

### VS Code — Используйте Context7

Документация VS Code располагается на **code.visualstudio.com**, а не в Learn.

| Library ID | Используется для |
|---|---|
| `/websites/code_visualstudio` | Пользовательская документация — настройки, функции, отладка, удалённая разработка |
| `/websites/code_visualstudio_api` | API расширений — веб-вью, TreeViews, команды, точки расширения |

### GitHub — Используйте Context7

Документация GitHub есть на **docs.github.com** и **cli.github.com**.

| Library ID | Используется для |
|---|---|
| `/websites/github_en` | Actions, API, репозитории, безопасность, администрирование, Copilot |
| `/websites/cli_github` | Команды и параметры GitHub CLI (`gh`) |

### Agent Framework — Используйте Learn MCP + Context7

Учебные материалы по Agent Framework находятся на learn.microsoft.com (используйте `microsoft_docs_search`), но **репозиторий GitHub** содержит детали уровня API, которые часто опережают опубликованные документы — особенно справочник DevUI REST API, параметры CLI и интеграции .NET.

| Library ID | Используется для |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Учебники — руководства DevUI, трассировка, оркестровка рабочих процессов |
| `/microsoft/agent-framework` | Детали API — конечные точки DevUI REST, флаги CLI, аутентификация, .NET `AddDevUI`/`MapDevUI` |

**Совет DevUI:** Задавайте запросы к сайту Learn для руководств по выполнению задач, затем к исходникам репозитория для деталей уровня API (схемы конечных точек, прокси-конфигурация, токены аутентификации).

---

## Настройка Context7

Для любого запроса Context7 сначала определите library ID (один раз за сессию):

1. Вызовите `mcp_context7_resolve-library-id` с названием технологии
2. Вызовите `mcp_context7_query-docs` с возвращённым library ID и конкретным запросом

---

## Как писать эффективные запросы

Будьте конкретны — указывайте версию, цель и язык:

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

Добавьте контекст:
- **Версия**, если актуально (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Цель задачи** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Язык** для многоязычной документации (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->