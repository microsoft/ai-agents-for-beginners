---
name: microsoft-docs
description: Търсене в официалната документация на Microsoft за намиране на концепции,
  уроци и примери с код по теми като Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub и други. Използва Microsoft Learn MCP като стандарт, с Context7 и Aspire
  MCP за съдържание, което се намира извън learn.microsoft.com.
---
# Microsoft Docs

Умение за търсене в екосистемата на технологиите на Microsoft. Обхваща learn.microsoft.com и документация, която се намира извън него (VS Code, GitHub, Aspire, Agent Framework хранилища).

---

## По подразбиране: Microsoft Learn MCP

Използвайте тези инструменти за **всичко в learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows и други. Това е основният инструмент за огромното мнозинство от запитванията по документация на Microsoft.

| Инструмент | Предназначение |
|------|---------|
| `microsoft_docs_search` | Търсене в learn.microsoft.com — концепции, ръководства, уроци, конфигурация |
| `microsoft_code_sample_search` | Намиране на работещи кодови примери от документация на Learn. Подайте `language` (`python`, `csharp` и др.) за най-добри резултати |
| `microsoft_docs_fetch` | Вземане на цялото съдържание на страница от конкретен URL (когато откъсите от търсенето не са достатъчни) |

Използвайте `microsoft_docs_fetch` след търсене, когато имате нужда от пълни уроци, всички опции за конфигурация или когато откъсите от търсенето са съкратени.

---

## Изключения: Кога да използвате други инструменти

Следните категории са **извън** learn.microsoft.com. Вместо това използвайте посочения инструмент.

### Aspire — Използвайте Aspire MCP Server (предпочитано) или Context7

Документацията за Aspire е на **aspire.dev**, не в Learn. Най-добрият инструмент зависи от версията на Aspire CLI:

**CLI 13.2+** (препоръчително) — Aspire MCP сървърът включва вградени инструменти за търсене в документация:

| MCP Инструмент | Описание |
|----------|-------------|
| `list_docs` | Изброява цялата налична документация от aspire.dev |
| `search_docs` | Теглено лексикално търсене в съдържанието на aspire.dev |
| `get_doc` | Извлича конкретен документ по идентификатор |

Тези инструменти са налични в Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). За актуализация: `aspire update --self --channel daily`.

**CLI 13.1** — MCP сървърът осигурява търсене за интеграции (`list_integrations`, `get_integration_docs`), но **не** предоставя търсене в документация. Върнете се към Context7:

| Идентификатор на библиотека | Използва се за |
|---|---|
| `/microsoft/aspire.dev` | Основно — ръководства, интеграции, CLI справочник, разгръщане |
| `/microsoft/aspire` | Източник на време за изпълнение — API детайли, подробности за реализация |
| `/communitytoolkit/aspire` | Общностни интеграции — Go, Java, Node.js, Ollama |

### VS Code — Използвайте Context7

Документацията за VS Code е на **code.visualstudio.com**, не в Learn.

| Идентификатор на библиотека | Използва се за |
|---|---|
| `/websites/code_visualstudio` | Потребителска документация — настройки, функции, отстраняване на грешки, отдалечена разработка |
| `/websites/code_visualstudio_api` | Extension API — уеб изгледи, TreeViews, команди, точки на принос |

### GitHub — Използвайте Context7

Документацията за GitHub е на **docs.github.com** и **cli.github.com**.

| Идентификатор на библиотека | Използва се за |
|---|---|
| `/websites/github_en` | Actions, API, хранилища, сигурност, администриране, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) команди и флагове |

### Agent Framework — Използвайте Learn MCP + Context7

Уроците за Agent Framework са в learn.microsoft.com (използвайте `microsoft_docs_search`), но **GitHub хранилището** има детайли на ниво API, които често изпреварват публикуваната документация — особено справочник за DevUI REST API, CLI опции и .NET интеграция.

| Идентификатор на библиотека | Използва се за |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Уроци — ръководства за DevUI, трасировка, управление на работния поток |
| `/microsoft/agent-framework` | Детайли за API — крайни точки на DevUI REST, CLI флагове, удостоверяване, .NET `AddDevUI`/`MapDevUI` |

**Съвет за DevUI:** Първо използвайте източника на уебсайта Learn за указания как да направите, после източника на хранилището за подробности на ниво API (схеми на крайни точки, прокси конфигурации, токени за удостоверяване).

---

## Настройка на Context7

За всеки въпрос към Context7, първо разрешете идентификатора на библиотеката (веднъж за сесията):

1. Извикайте `mcp_context7_resolve-library-id` с името на технологията
2. Извикайте `mcp_context7_query-docs` с върнатия идентификатор на библиотеката и конкретен въпрос

---

## Създаване на ефективни запитвания

Бъдете конкретни — включете версия, цел и език:

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

Включете контекст:
- **Версия** когато е приложимо (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Цел на задачата** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Език** за полиглотска документация (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->