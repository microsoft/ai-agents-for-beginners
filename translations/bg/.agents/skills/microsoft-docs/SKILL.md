---
name: microsoft-docs
description: Запитвайте официалната документация на Microsoft, за да намерите концепции,
  уроци и примери за код за Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  и други. Използва Microsoft Learn MCP като по подразбиране, като за съдържание,
  което се намира извън learn.microsoft.com, използва Context7 и Aspire MCP.
---
# Microsoft Docs

Умение за проучване на екосистемата на технологиите на Microsoft. Обхваща learn.microsoft.com и документацията, която се намира извън нея (репозиториите на VS Code, GitHub, Aspire, Agent Framework).

---

## По подразбиране: Microsoft Learn MCP

Използвайте тези инструменти за **всичко в learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows и други. Това е основният инструмент за голямата част от заявките за документация на Microsoft.

| Инструмент | Предназначение |
|------|---------|
| `microsoft_docs_search` | Търси в learn.microsoft.com — концепции, ръководства, уроци, конфигурация |
| `microsoft_code_sample_search` | Намира работещи кодови фрагменти от документацията в Learn. Подайте `language` (`python`, `csharp`, и т.н.) за най-добри резултати |
| `microsoft_docs_fetch` | Връща пълното съдържание на страница от конкретен URL (когато откъсите от търсенето не са достатъчни) |

Използвайте `microsoft_docs_fetch` след търсене, когато имате нужда от пълни уроци, всички опции за конфигурация или когато откъсите от търсенето са съкратени.

---

## Изключения: Кога да използвате други инструменти

Следните категории се намират **извън** learn.microsoft.com. Използвайте посочения инструмент вместо това.

### .NET Aspire — Използвайте Aspire MCP Server (предпочитан) или Context7

Aspire документацията се намира на **aspire.dev**, не в Learn. Най-подходящият инструмент зависи от версията на Aspire CLI:

**CLI 13.2+** (препоръчително) — Aspire MCP сървърът включва вградени инструменти за търсене в документацията:

| MCP Tool | Описание |
|----------|-------------|
| `list_docs` | Изброява цялата налична документация от aspire.dev |
| `search_docs` | Претеглено лексикално търсене сред съдържанието на aspire.dev |
| `get_doc` | Извлича конкретен документ по slug |

Тези функции се доставят в Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). За ъпдейт: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP сървърът предоставя интеграционни търсения (`list_integrations`, `get_integration_docs`), но **не** търсене в документацията. Върнете се към Context7:

| ID на библиотеката | Използва се за |
|---|---|
| `/microsoft/aspire.dev` | Основен — ръководства, интеграции, CLI референция, разгръщане |
| `/dotnet/aspire` | Изходен код на runtime — вътрешности на API, детайли за имплементацията |
| `/communitytoolkit/aspire` | Интеграции от общността — Go, Java, Node.js, Ollama |

### VS Code — Използвайте Context7

VS Code документацията се намира на **code.visualstudio.com**, не в Learn.

| ID на библиотеката | Използва се за |
|---|---|
| `/websites/code_visualstudio` | Потребителска документация — настройки, функционалности, отстраняване на грешки, отдалечено разработване |
| `/websites/code_visualstudio_api` | API за разширения — webviews, TreeViews, команди, точки за принос |

### GitHub — Използвайте Context7

GitHub документацията се намира на **docs.github.com** и **cli.github.com**.

| ID на библиотеката | Използва се за |
|---|---|
| `/websites/github_en` | Actions, API, репозитории, сигурност, администриране, Copilot |
| `/websites/cli_github` | Команди и флагове на GitHub CLI (`gh`) |

### Agent Framework — Използвайте Learn MCP + Context7

Уроците за Agent Framework са на learn.microsoft.com (използвайте `microsoft_docs_search`), но **GitHub репото** съдържа детайли на ниво API, които често предхождат публикуваната документация — особено референцията на DevUI REST API, опции на CLI и .NET интеграцията.

| ID на библиотеката | Използва се за |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Уроци — ръководства за DevUI, трасиране, оркестрация на работни потоци |
| `/microsoft/agent-framework` | Детайли по API — REST endpoint-и на DevUI, CLI флагове, автентикация, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Потърсете източника на уебсайта Learn за ръководства „как да“, след това репозиторния източник за специфики на ниво API (схеми на endpoint-и, proxy конфигурация, токени за автентикация).

---

## Настройка на Context7

За всяка заявка към Context7, разрешете library ID първо (еднократно за сесията):

1. Извикайте `mcp_context7_resolve-library-id` с името на технологията
2. Извикайте `mcp_context7_query-docs` с върнатия library ID и конкретна заявка

---

## Писане на ефективни заявки

Бъдете конкретни — включете версия, намерение и език:

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
- **Версия** когато е релевантно (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Намерение на задачата** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Език** за полиглотна документация (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на оригиналния език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод, извършен от човек. Не носим отговорност за каквито и да е недоразумения или погрешни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->