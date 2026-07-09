# Историја измена

Све значајне измене за курс **AI агенти за почетнике** су документоване у овом фајлу.

## [Непубликовано] — 2026-07-06

Ово издање мигрира курс на **Azure OpenAI Responses API**, стандардизује именовање производа на **Microsoft Foundry** и **Microsoft Agent Framework (MAF)**, пензионише GitHub моделе, ажурира верзије SDK-а и додаје нови садржај о локалним моделима и хостовању других оквира на Foundry.

### Додато

- **Вештина миграције** — Инсталирана [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Агент Вештина (из [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) унутар `.agents/skills/`, укључујући њене референце и скенер скрипту.
- **Foundry Local (покретање модела на уређају)** — Нова секција "Алтернативни провајдер: Foundry Local" у [00-course-setup/README.md](./00-course-setup/README.md) која покрива инсталацију (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, и повезивање `FoundryLocalManager` са Microsoft Agent Framework путем `OpenAIChatClient`.
- **Хостовање LangChain / LangGraph агената на Microsoft Foundry** — Нова секција у [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) плус извршни пример [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) користећи `langchain-azure-ai[hosting]` и `ResponsesHostServer` (протокол `/responses`), базирано на [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Нова секција "Пример из реалног света: Microsoft Project Opal" у [15-browser-use/README.md](./15-browser-use/README.md) која приказује Opal као агент за коришћење рачунара у предузећу и мапира је на концепте курса (човек у петљи, поверење/безбедност, планирање, Вештине).
- **Други пример из Лекције 02 Python** — Додат [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (погледај "Промењено" — мигрирано из претходног Semantic Kernel нотебука) и повезан у README лекције.
- Додат одељак **Модели и Провајдери** у [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Промењено

- **Chat Completions → Responses API (Python).** Примери који су директно позивали модел су мигрирани са Chat Completions на Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), користећи `OpenAI` клијента против стабилног Azure OpenAI `/openai/v1/` ендпоинта (без `api_version`). Погођени примери укључују:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — цео преглед позива функција (структура алата је поравната у Responses формат, резултати алата враћени као `function_call_output`, `max_output_tokens`, итд.).
- **GitHub Models → Azure OpenAI.** GitHub Models је пензионисан (истиче **јул 2026**) и не подржава Responses API. Сви код путањи за GitHub Models су пређени на Azure OpenAI / Microsoft Foundry у Python и .NET примерима:
  - Python: Лекција 08 workflow нотебуци (`01`–`03`), Лекција 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + пратећа `.md` документација, и Лекција 08 dotNET workflow нотебуци/`.md` (`01`–`03`) сада користе `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` са `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Претходни `02-semantic-kernel.ipynb` је преписан да користи Microsoft Agent Framework са Azure OpenAI (Responses API) и преименован у `02-python-agent-framework-azure-openai.ipynb`.
- **Стандаризовано на `FoundryChatClient` + `as_agent`.** README и код у нотебуцима који је реферисао `AzureAIProjectAgentProvider` је стандарнизован на канонски образац који користи Лекција 01 и оквирни примери: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` са `provider.as_agent(...)`. Ажурирано у README-има и нотебуцима Лекција 02–14 (нпр. меморија у Лекцији 13, сви нотебуци у Лекцији 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Именовање производа.** Преименовано у целокупном енглеском садржају:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Неизмењено: "Azure OpenAI", "Azure AI Search", "Azure AI Inference" и имена променљивих окружења.)
- **Зависности** ([requirements.txt](../../requirements.txt)):
  - Закључане верзије `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Закључана верзија `openai>=1.108.1` (минимум за Responses API).
  - Уклоњен `azure-ai-inference` (коришћен само од мигрираних GitHub Models примера).
- **Конфигурација окружења** ([.env.example](../../.env.example)): уклоњене променљиве за GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); додате `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` и опционални `AZURE_OPENAI_API_KEY`; ажурирана имена на Microsoft Foundry.
- **Документација** — Ажурирани [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), и [STUDY_GUIDE.md](./STUDY_GUIDE.md) за горе наведено (постављање env var, верификациони исечак, упутства за провајдере, именовање).

### Уклоњено

- GitHub Models кориснички кораци и променљиве окружења из документације за подешавање (замењени Azure OpenAI / Microsoft Foundry).

### Безбедност / Приватност (чишћење јавно дељених података)

- Обрисани излази извршавања Jupyter нотебука који су процурили прави **Azure subscription ID**, имена ресурса и група ресурса, Bing ID везе, као и локалне путање датотека и корисничка имена програмера, у:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Потврђено да нема API кључева, токена, ID претплата или личних путања у праћеном енглеском садржају (референце `GITHUB_TOKEN` који остају су GitHub Actions токен у workflow-има и GitHub MCP сервер PAT у подешавању Лекције 11 — оба легитимна и нерелевантна за GitHub Models).

### Белешке и позната ограничења

- **Није извршавано/компиловано.** Ово су едукативни примери ажурирани за исправност API-ја/именовања; нису покретани против живих Azure ресурса, нити су .NET примери компиловани у овом окружењу. Потврдите са сопственом Microsoft Foundry / Azure OpenAI имплементацијом.
- **Деплојмент модела мора подржавати Responses API.** Користите деплојмент као што је `gpt-4o-mini`, `gpt-4.1` или модел `gpt-5.x`. Старији модели подржавају основну функционалност Responses али не све функције.
- **Верзија agent-framework-а.** Примери циљају на новији MAF (`>=1.10.0`). Канонски позив за креирање агента је `client.as_agent(...)`; API-ји су верификовани према објављеним документацијама и инсталираној верзији. Ако користите другу верзију, проверите доступност метода (`as_agent` против `create_agent`).
- **Лекција 08 workflow нотебук 04** намерно задржава `AzureAIAgentClient` (из `agent-framework-azure-ai`) јер користи Microsoft Foundry Agent Service хостоване алате (Bing grounding, тумач кода); већ је заснован на Responses.
- **.NET подразумевани деплојмент.** Два Лекција 08 dotNET workflow примера раније су тврдокодирала `gpt-4o`; сада подразумевано користе `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Ако пример захтева мултимодални/види модалитет улаза, подесите `AZURE_OPENAI_DEPLOYMENT` на одговарајући модел.
- **Foundry Local** пружа OpenAI компатибилни **Chat Completions** ендпоинт и намењен је за локални развој; за пуну функционалност Responses API користите Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->