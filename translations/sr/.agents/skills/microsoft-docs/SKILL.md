---
name: microsoft-docs
description: Претражите званичну Microsoft документацију да бисте пронашли концепте,
  туторијале и примере кода за Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  и још. Користи Microsoft Learn MCP као подразумевани, а за садржај који се налази
  ван learn.microsoft.com користи Context7 и Aspire MCP.
---
# Microsoft Docs

Вештина истраживања за Microsoft технолошки екосистем. Обухвата learn.microsoft.com и документацију која се налази ван ње (VS Code, GitHub, Aspire, Agent Framework репозиторијуми).

---

## Default: Microsoft Learn MCP

Користите ове алате за **све на learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows и још много тога. Ово је примарни алат за огромну већину упита везаних за Microsoft документацију.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Претражује learn.microsoft.com — концепти, водичи, туторијали, конфигурација |
| `microsoft_code_sample_search` | Пронађите радне примере кода из Learn докумената. Проследите `language` (`python`, `csharp`, итд.) за најбоље резултате |
| `microsoft_docs_fetch` | Добијте цео садржај странице са одређеног URL-а (кada исечци са претраге нису довољни) |

Користите `microsoft_docs_fetch` након претраге када су вам потребни комплетни туторијали, све опције конфигурације или када су исечци претраге скраћени.

---

## Exceptions: When to Use Other Tools

Следеће категорије се налазе **ван** learn.microsoft.com. Уместо тога користите назначени алат.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire документација живи на **aspire.dev**, не на Learn. Најбољи алат зависи од ваше Aspire CLI верзије:

**CLI 13.2+** (препоручено) — Aspire MCP сервер укључује уграђене алате за претрагу документације:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Наводи сву доступну документацију са aspire.dev |
| `search_docs` | Тежинско лексичко претраживање садржаја aspire.dev |
| `get_doc` | Преузима одређени документ по slug-у |

Ово је доступно у Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). За ажурирање: `aspire update --self --channel daily`. Реф: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP сервер пружа претрагу интеграција (`list_integrations`, `get_integration_docs`) али **не** претрагу документacije. Вратите се на Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Примарно — водичи, интеграције, CLI референца, деплојмент |
| `/dotnet/aspire` | Извор окружења за извршавање — унутрашњости API-ја, детаљи имплементације |
| `/communitytoolkit/aspire` | Заједничке интеграције — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code документација живи на **code.visualstudio.com**, не на Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Корисничка документација — подешавања, функције, дебаговање, remote dev |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, команде, тачке за допринос |

### GitHub — Use Context7

GitHub документација живи на **docs.github.com** и **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, репозиторијуми, безбедност, администрација, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) команде и флагови |

### Agent Framework — Use Learn MCP + Context7

Agent Framework туторијали су на learn.microsoft.com (користите `microsoft_docs_search`), али **GitHub репо** садржи детаље на нивоу API-ја који често претходе објављеним документима — посебно DevUI REST API референцу, CLI опције и .NET интеграцију.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Туторијали — DevUI водичи, трасирање, оркестрација радних токова |
| `/microsoft/agent-framework` | Детаљи API-ја — DevUI REST endpoint-и, CLI флагови, ауторизација, .NET `AddDevUI`/`MapDevUI` |

**DevUI савет:** Прво упитајте извор Learn веб-сајта за how-to водиче, а затим извор из репозиторијума за API-специфике (шеме endpoint-а, proxy конфигурација, auth токени).

---

## Context7 Setup

За било који Context7 упит, прво решите library ID (једнократно по сесији):

1. Позовите `mcp_context7_resolve-library-id` са именом технологије
2. Позовите `mcp_context7_query-docs` са враћеним library ID и конкретним упитом

---

## Writing Effective Queries

Будите специфични — укључите верзију, намеру и језик:

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
Изјава о одрицању одговорности:
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења проистекла из употребе овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->