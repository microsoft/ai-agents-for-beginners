---
name: microsoft-docs
description: Консултујте званичну Microsoft документацију да пронађете концепте, туторијале
  и примере кода за Azure, .NET, Agent Framework, Aspire, VS Code, GitHub и још много
  тога. Користи Microsoft Learn MCP као подразумевани извор, са Context7 и Aspire
  MCP за садржаје који се налазе ван learn.microsoft.com.
---
# Microsoft Docs

Вештина истраживања за Microsoft технолошки екосистем. Обухвата learn.microsoft.com и документацију која се налази ван ње (VS Code, GitHub, Aspire, Agent Framework репозиторијуми).

---

## Подразумевано: Microsoft Learn MCP

Користите ове алате за **све на learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows и други. Ово је основни алат за већину упита у вези са Microsoft документацијом.

| Алат | Сврха |
|------|---------|
| `microsoft_docs_search` | Претражује learn.microsoft.com — концепте, водиче, туторијале, конфигурацију |
| `microsoft_code_sample_search` | Пронађе радне исечке кода из Learn документације. Проследите `language` (`python`, `csharp` и др.) за најбоље резултате |
| `microsoft_docs_fetch` | Добите цео садржај странице са одређеног URL-а (када исечци из претраге нису довољни) |

Користите `microsoft_docs_fetch` након претраге када су вам потребни комплетни туторијали, све опције конфигурације или када су исечци из претраге скраћени.

---

## Изузеци: Када користити друге алате

Следеће категорије се налазе **ван** learn.microsoft.com. Уместо тога користите назначени алат.

### Aspire — Користите Aspire MCP Server (преферирано) или Context7

Aspire документација се налази на **aspire.dev**, не на Learn. Најбољи алат зависи од ваше Aspire CLI верзије:

**CLI 13.2+** (препоручено) — Aspire MCP сервер укључује уграђене алате за претрагу документације:

| MCP алат | Опис |
|----------|-------------|
| `list_docs` | Листи сву доступну документацију са aspire.dev |
| `search_docs` | Тежинска лексичка претрага кроз aspire.dev садржај |
| `get_doc` | Враћа одређени документ по слугу |

Ови алати долазе у Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). За ажурирање: `aspire update --self --channel daily`.

**CLI 13.1** — MCP сервер пружа претрагу интеграција (`list_integrations`, `get_integration_docs`) али **не** претрагу документације. У том случају користите Context7:

| ИД библиотеке | Користи се за |
|---|---|
| `/microsoft/aspire.dev` | Основно — водичи, интеграције, CLI референца, деплојмент |
| `/microsoft/aspire` | Извор извршавања — API унутрашњости, детаљи имплементације |
| `/communitytoolkit/aspire` | Заједница интеграција — Go, Java, Node.js, Ollama |

### VS Code — Користите Context7

VS Code документација се налази на **code.visualstudio.com**, не на Learn.

| ИД библиотеке | Користи се за |
|---|---|
| `/websites/code_visualstudio` | Корисничка документација — подешавања, функције, дебаговање, удаљени развој |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, команде, поене учешћа |

### GitHub — Користите Context7

GitHub документација се налази на **docs.github.com** и **cli.github.com**.

| ИД библиотеке | Користи се за |
|---|---|
| `/websites/github_en` | Actions, API, репозиторијуми, безбедност, администрација, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) команде и опције |

### Agent Framework — Користите Learn MCP + Context7

Agent Framework туторијали су на learn.microsoft.com (користите `microsoft_docs_search`), али **GitHub репо** има детаље на нивоу API-ја који често претичу објављену документацију — посебно DevUI REST API референцу, CLI опције и .NET интеграцију.

| ИД библиотеке | Користи се за |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Туторијали — DevUI водичи, праћење, оркестрација токова рада |
| `/microsoft/agent-framework` | Детаљи API-ја — DevUI REST крајње тачке, CLI опције, аутентификација, .NET `AddDevUI`/`MapDevUI` |

**DevUI савет:** Прво претражите Learn сајт за упутства како се ради, а затим репо за детаље на нивоу API-ја (шеме крајњих тачака, прокси конфигурација, аутентификациони токени).

---

## Подешавање Context7

За било који Context7 упит, прво решите ИД библиотеке (једнократно по сесији):

1. Позовите `mcp_context7_resolve-library-id` са именом технологије
2. Позовите `mcp_context7_query-docs` са добијеним ИД-ом библиотеке и конкретним упитом

---

## Писање ефективних упита

Будите конкретни — укључите верзију, намеру и језик:

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

Укључите контекст:
- **Верзију** када је релевантно (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Намера задатка** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Језик** за полиглот документацију (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->