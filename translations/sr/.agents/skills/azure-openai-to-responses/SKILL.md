---
name: azure-openai-to-responses
license: MIT
---
# Миграција Python апликација са Azure OpenAI Chat Completions на Responses API

> **АУТОРИТАТИВНА УПУТСТВА — ПРАТИ ТАЧНО**
>
> Ова вештина мигрира Python кодне базе које користе Azure OpenAI Chat Completions
> на уједињени Responses API. Пратите ове инструкције прецизно.
> Не импровизујте мапирање параметара нити не измишљајте форме API-ја.

---

## Тригери

Активирајте ову вештину када корисник жели да:
- Мигрира Python апликацију са Azure OpenAI Chat Completions на Responses API
- Надогради употребу Python OpenAI SDK на најновији облик API-ја за Azure OpenAI
- Припреми Python код за GPT-5 или новије моделе који захтевају Responses на Azure
- Пребаци са `AzureOpenAI`/`AsyncAzureOpenAI` на стандардни `OpenAI`/`AsyncOpenAI` клијент са v1 endpoint-ом
- Исправи упозорења о укидању везана за `AzureOpenAI` конструкторе или `api_version`

---

## ⚠️ Компатибилност модела — ПРВО ПРОВЕРИТЕ

> **Пре миграције, проверите да ли ваша Azure OpenAI инсталација подржава Responses API.**

### 1. Бренд-тестирање инсталације (најбржа метода)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Напомена**: `max_output_tokens` има **минимум од 16** на Azure OpenAI. Вредности испод 16 враћају 400 грешку. Користите 50+ за бренд тестове.

Ако ово врати 404, модел инсталације још не подржава Responses — проверите референцу испод или поново распоредите са подржаним моделом.

### 2. Проверите доступне моделе у вашој регији (препоручено)

Покрените уграђени алат за проверу компатибилности модела да видите шта је доступно са подршком за Responses API у вашој регији:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Ово упитује Azure ARM уживо и приказује матрицу компатибилности — који модели подржавају Responses, структурирани излаз, алате итд. Користите `--filter gpt-5.1,gpt-5.2` да сужите резултате или `--json` за скриптовање.

### 3. Потпуна референца подршке модела

- **Уживо упит**: `python migrate.py models` (погледајте горе — специфично за регију, увек ажурирано)
- **Преглед доступности**: [Табела резимеа модела и доступности по регијама](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Брзи почетак & упутства**: **https://aka.ms/openai/start**

### ⚠️ Ограничења старијих модела

> **УПОЗОРЕЊЕ**: Старији модели (нпр. `gpt-4o`, `gpt-4`) можда не подржавају све функције Responses API у пуном опсегу.
>
> Позната ограничења са старијим моделима:
> - **`reasoning` параметар**: Није подржан на `gpt-4o-mini`, `gpt-4o` и многим моделима без рeасонинга. Мигрирајте `reasoning` само ако је већ био присутан у оригиналном коду.
> - **`seed` параметар**: Није уопште подржан у Responses API — уклоните га из свих захтева.
> - **Структурирани излаз преко `text.format`**: Старији модели можда не примењују поуздано `strict: true` JSON шеме.
> - **Оркестрација алата**: GPT-5+ оркестрира позиве алата као део интерног размишљања. Старији модели преко Responses и даље раде, али немају ову дубоку интеграцију.
> - **Ограничења температуре**: При миграцији на `gpt-5`, температура мора бити изостављена или постављена на `1`. Старији модели немају таква ограничења.

### O-series модели за размишљање (o1, o3-mini, o3, o4-mini)

O-series модели имају јединствена ограничења параметара. При миграцији апликација које циљају ове моделе:

- **`temperature`**: Мора бити `1` (или изостављено). O-series модели не прихватају друге вредности.
- **`max_completion_tokens` → `max_output_tokens`**: Апликације које користе Azure-специфични `max_completion_tokens` морају прећи на `max_output_tokens`. Поставите високе вредности (4096+) јер се токени за размишљање рачунају у лимит.
- **`reasoning_effort`**: Ако апликација користи `reasoning_effort` (low/medium/high), задржите га — Responses API подржава овај параметар за o-series моделе.
- **Понашање стримовања**: O-series модели могу буферирати излаз док се процес размишљања не заврши пре него што издају текстуалне детаље догађаја. Стримовање и даље функционише, али први `response.output_text.delta` може стићи са већим кашњењем него код GPT модела.
- **`top_p`**: Није подржан на o-series моделима — уклоните ако постоји.
- **Употреба алата**: O-series модели подржавају алате преко Responses API исто као GPT модели, али квалитет оркестрације позива алата варира по моделу.

**Акција — проактивни моделски савет**: Током фазе скенирања проверите који модел апликација користи (име распоређивања, окружне променљиве, конфигурација). Ако је модел `gpt-4o` или старији (није gpt-4.1+), проактивно обавестите корисника:
- Миграција ће радити за основни текст, чет, стриминг и алате на тренутном моделу.
- Новији модели (`gpt-5.1`, `gpt-5.2`) нуде бољу оркестрацију алата, примену структурираних излаза, размишљање и доступност преко региона.
- Треба да размисле о надоградњи инсталације када буду спремни — то не спречава миграцију.

Не блокирајте нити одбијајте миграцију на основу верзије модела. Савет је информативан.

### GitHub Models НЕ подржава Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) не подржава Responses API.**

Ако кодна база има GitHub Models кодни пут (тражите `base_url` ка `models.github.ai` или `models.inference.ai.azure.com`), **уклоните га у потпуности** током миграције. Responses API захтева Azure OpenAI, OpenAI или компатибилни локални endpoint (нпр. Ollama са подршком за Responses).

Акција током скенирања:
- Означите све GitHub Models кодне путеве за уклањање.

---

## Миграција оквира рада (framework)

Многе апликације користе виши ниво оквира на врху OpenAI. При миграцији ових, мења се свој API оквира — не само основни OpenAI позиви.

### Microsoft Agent Framework (MAF)

**Прво проверите вашу MAF верзију** — миграција зависи да ли користите MAF 1.0.0+ или пре-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **већ користи Responses API** — није потребна миграција. Ако кодна база користи стару `OpenAIChatCompletionClient` (која користи `chat.completions.create`), замените је са `OpenAIChatClient`.

| Пре | После |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Да проверите верзију: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)" `

#### MAF пре-1.0.0 (beta/rc издања)

У пре-1.0.0 MAF, `OpenAIChatClient` је користио Chat Completions. Надоградите на `agent-framework-openai>=1.0.0` где `OpenAIChatClient` по дифолту користи Responses API.

Нема других потребних измена — API-и `Agent`-а и алата остају исти.

### LangChain (`langchain-openai`)

Додајте `use_responses_api=True` у `ChatOpenAI()`. Такође ажурирајте приступ резултату са `.content` на `.text`.

| Пре | После |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

За комплетне пре/после примере кода, погледајте [cheat-sheet.md](./references/cheat-sheet.md).

---

## Упутство за миграцију фронтенда

> **Responses API је брiga на страни сервера.** Мигрирајте ваш Python backend; HTTP уговор фронтенда треба остати непромењен осим ако ваш backend није танки пролаз — у том случају размислите о усвајању Responses формата захтева да елиминишете слој превођења. Ако фронтенд директно позива OpenAI са клиентском кључем, преместите те позиве прво на backend.

### Депрецатион `@microsoft/ai-chat-protocol`

`@microsoft/ai-chat-protocol` npm пакет је депрецириран и треба га заменити са [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Ако га пронађете у фронтенду:

1. Замените CDN скрипту:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Уклоните иницијализацију `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Замените `client.getStreamedCompletion(messages)` директним `fetch()` позивом на backend стриминг ентпоинт.
4. Замените `for await (const response of result)` са `for await (const chunk of readNDJSONStream(response.body))`.
5. Ажурирајте приступ својствима са `response.delta.content` / `response.error` на `chunk.delta.content` / `chunk.error`.

---

## Циљеви

- Набројати све Python позиве који користе Chat Completions или legacy Completions према Azure OpenAI.
- Предложити план и редослед миграције за Python кодну базу.
- Применити безбедне, минималне измене да се пређе на Responses API.
- Ажурирати позиваоце да користе Responses шему излаза; без backcompat омотача.
- Покренути тестове/линтове; поправити тривијалне грешке настале миграцијом.
- Припремити мале, лако прегледне измене и обезбедити коначни резиме са diff-овима (не комитовати).

---

## Заштитне мере (Guardrails)

- Мењајте само фајлове у git workspace-у. Никад не пишите ван њега.
- Не задржавајте шиме за уназадну компатибилност; мигрирајте код на нови облик API-ја.
- Не остављајте коментаре за транзицију или бекуп фајлове.
- Задржите семантику стримовања ако је раније коришћена; иначе користите не-стриминг.
- Тражите одобрење пре извршавања команди или мрежних позива у режиму одобравања.
- Не покрећите `git add`/`git commit`/`git push`; правите само измене у радном дрвету.

---

## Корак 0: Миграција Azure OpenAI Client-а (претпоставка)

Ако кодна база користи `AzureOpenAI` или `AsyncAzureOpenAI` конструкторе, прво мигрирајте на стандардне `OpenAI` / `AsyncOpenAI` конструкторе. Azure-специфични конструктори су депрецирани у `openai>=1.108.1`.

### Зашто v1 API пут?

Нови `/openai/v1` endpoint користи стандардни `OpenAI()` клијент уместо `AzureOpenAI()`, не захтева `api_version` параметар и ради идентично на OpenAI и Azure OpenAI. Исти клијентски код је будућнo без потребе управљања верзијом.

### Кључне промене

| Пре | После |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Потпуно уклонити |

### Контролна листа чишћења

- Уклоните `api_version` аргумент из конструисања клијента.
- Уклоните `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` окружне променљиве из `.env`, подешавања апликације и Bicep/infra фајлова.
- Преименујте `AZURE_OPENAI_CLIENT_ID` у `AZURE_CLIENT_ID` у `.env`, подешавањима апликације, Bicep/infra и тест фиxtures (стандардна конвенција Azure Identity SDK).
- Обезбедите `openai>=1.108.1` у `requirements.txt` или `pyproject.toml`.

### Миграција окружних променљивих

| Стари env var | Акција | Напомене |
|-------------|--------|---------|
| `AZURE_OPENAI_VERSION` | **Уклонити** | Нема потребе за `api_version` са v1 endpoint-ом |
| `AZURE_OPENAI_API_VERSION` | **Уклонити** | Исто као горе |
| `AZURE_OPENAI_CLIENT_ID` | **Преименуј** → `AZURE_CLIENT_ID` | Стандардна конвенција Azure Identity SDK за `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Задржати** | И даље потребно за конструкцију `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Задржати** | Користи се као `model` параметар у `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Задржати** | Користи се као `api_key` за кључ аутентификацију |

За примере подешавања клијента (синхрони, асинхрони, EntraID, API кључ, мулти-тенант), погледајте [cheat-sheet.md](./references/cheat-sheet.md).

---

## Корак 1: Детекција Legacy позива

Покрените [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) скрипту да пронађете све позиве које треба мигрирати:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Или ручно претражујте — сваки подудар је циљ миграције:

```bash
# Наслеђени API позиви (мора да се препише)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Застарели Azure клиент конструктори (морају да се заменe)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Обрасци приступа облику одговора (морају да се ажурирају)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Дефиниције алата у старом угнежђеном формату (морају да се исправе)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Резултати алата у старом формату (морају да се конвертују у function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Застарели параметри (морају да се уклоне или преименују)
rg "response_format"
rg "max_tokens\b"        # преименуј у max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Застареле еколошке променљиве (очистити)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # треба да буде AZURE_CLIENT_ID

# GitHub Models крајње тачке (морају да се уклоне — Responses API није подржан)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Наслеђени обрасци на нивоу фрејмворка (морају да се ажурирају)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: замени са OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: потребно use_responses_api=True

# Тест инфраструктура (мора да се ажурира)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Приступ телу грешке филтера садржаја (мора да се ажурира — структура је промењена)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # стари јединствени облик — сада content_filter_results (множина) унутар content_filters низа

# Сирови HTTP позиви ка Chat Completions крајњој тачки (морају да се ажурирају URL-ови)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Хеуристике (детекција и преписивање)

- **Chat Completions клијент**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure конструктори клијената**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Алатке**: конвертовати дефиниције алатки за позивање функција из угнежђеног формата (`{"type": "function", "function": {"name": ...}}`) у равни Responses формат (`{"type": "function", "name": ...}`); користити `tool_choice`; враћати резултате алатке као ставке `{"type": "function_call_output", "call_id": ..., "output": ...}` (не као `{"role": "tool", ...}`).
- **Рундтрип алатки**: када модел врати позиве функција, додати `response.output` ставке у разговор (не ручни речник `{"role": "assistant", "tool_calls": [...]}`), затим додати `function_call_output` ставке за сваки резултат.
- **Примери алатки са неколико снимака**: ако разговор укључује тврдо кодиране примере позива алатки, конвертовати их у `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` ставке. ИД морају почети са `fc_`.
- **`pydantic_function_tool()`**: овај помоћни алат и даље генерише стари угнежђени формат и **није компатибилан** са `responses.create()`. Заменити ручним дефиницијама алатки или омотачем за раван формат.
- **Вишеокретна комуникација**: одржавати историју разговора у апликацији; прослеђивати претходне окрете преко `input` ставки.
- **Форматовање**: заменити Chat-ов горњи нивоу `response_format` са `text.format` у Responses. Канонски облик: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Ставке садржаја**: заменити Chat `content[].type: "text"` са Responses `content[].type: "input_text"` за корисничке/системске окрете.
- **Ставке садржаја слике**: заменити Chat `content[].type: "image_url"` са Responses `content[].type: "input_image"`. Поље `image_url` се мења из угнежђеног објекта `{"url": "..."}` у раван низ. Погледати кратак преглед за примере пре/после.
- **Труд разумевања**: **мигрирати само `reasoning` ако већ постоји у оригиналном коду**.
- **Руководјење грешкама филтера садржаја**: структура тела грешке се променила. Chat Completions користи `error.body["innererror"]["content_filter_result"]` (једнина); Responses API користи `error.body["content_filters"][0]["content_filter_results"]` (мн. број, у низу). Код који приступа `innererror` ће изазвати `KeyError`. Преписати да користи нову путању.
- **Сирови HTTP позиви**: ако апликација директно позива Azure OpenAI REST API (кроз `requests`, `httpx` итд.) користећи `/openai/deployments/{name}/chat/completions?api-version=...`, преписати у `/openai/v1/responses`. Тело захтева се мења: `messages` → `input`, додати `max_output_tokens` и `store: false`, уклонити `api-version` query параметар. Тело одговора се мења: `choices[0].message.content` → `output[0].content[0].text` (напомена: `output_text` је својство СДК-а за погодност, није присутно у сировом REST JSON-у).

---

## Корак 2: Примени миграцију

### Напомене о миграцији (Chat Completions → Responses)

- **Зашто мигрирати**: Responses је уједињени API за текст, алатке и стримовање; Chat Completions је застарео. Са GPT-5, Responses је потребан за најбоље перформансе.
- **HTTP**: Azure крајња тачка се мења са `/openai/deployments/{name}/chat/completions` на `/openai/v1/responses`.
- **Поља**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` остаје.
- **Форматовање**: `response_format` → `text.format` са исправним објектом.
- **Ставке садржаја**: Замена Chat `content[].type: "text"` са Responses `content[].type: "input_text"` за системске/корисничке окрете.
- **Ставке садржаја слике**: Замена Chat `content[].type: "image_url"` са Responses `content[].type: "input_image"`. Развити `image_url` из `{"image_url": {"url": "..."}}` у `{"image_url": "..."}` (обичан низ — HTTPS URL или `data:image/...;base64,...` data URI).

### Референца мапирања параметара

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (низ ставки) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (објекат) |
| `temperature` | `temperature` (непромењено) |
| `stop` | `stop` (непромењено) |
| `frequency_penalty` | `frequency_penalty` (непромењено) |
| `presence_penalty` | `presence_penalty` (непромењено) |
| `tools` / позив функција | `tools` (непромењено) |
| `seed` | **Уклонити** (није подржано) |
| `store` | `store` (постављено на `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (раван низ) |

За комплетне примере кода пре/после, видети [cheat-sheet.md](./references/cheat-sheet.md).

За миграцију тест инфраструктуре (мокови, снимци, тврдње), видети [test-migration.md](./references/test-migration.md).

За решавање грешака и замки, видети [troubleshooting.md](./references/troubleshooting.md).

---

## Чување података и стање

- Поставити `store: false` на свим захтевима Responses.
- Не ослањати се на претходне ИД порука или контекст чuvan на серверу; држати стање под контролом клијента и минимизирати метаподатке.

---

## Критеријуми прихватања

### Врата на нивоу кода (сви морају бити прошли)

- [ ] Нула поклапања за `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` у мигрираним фајловима.
- [ ] Нула поклапања за `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — сви конструктори користе `OpenAI`/`AsyncOpenAI` са v1 крајњом тачком.
- [ ] Нула поклапања за `rg "models\.github\.ai|models\.inference\.ai\.azure"` — уклоњени код путање GitHub Модела.
- [ ] Нула поклапања за `rg "OpenAIChatCompletionClient"` — МAF 1.0.0+ код користи `OpenAIChatClient` (који користи Responses API). У верзијама пре 1.0.0, надоградити на `agent-framework-openai>=1.0.0`.
- [ ] Сви позиви `ChatOpenAI(...)` укључују `use_responses_api=True`.
- [ ] Нула поклапања за `rg "choices\[0\]"` — сваки приступ одговору користи `resp.output_text` или Responses шему излаза.
- [ ] Није присутан `response_format` на врхунском нивоу; сваки структурисани излаз користи `text={"format": {...}}`.
- [ ] `openai>=1.108.1` и `azure-identity` у `requirements.txt` или `pyproject.toml`; зависности поново инсталиране.
- [ ] `store=False` постављено на сваки позив `responses.create`.
- [ ] Нема `api_version` у конструисању клијента; `AZURE_OPENAI_API_VERSION` уклоњен из env фајлова и инфраструктуре.

### Врата за тест инфраструктуру (сви морају бити прошли)

- [ ] Нула поклапања за `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Нула поклапања за `rg "_azure_ad_token_provider" tests/` — тврдње ажуриране да провере `isinstance(client, AsyncOpenAI)` или `base_url`.
- [ ] Нула поклапања за `rg "prompt_filter_results|content_filter_results" tests/` — уклоњени Azure-специфични филтер мокови.
- [ ] Мок фикстуре користе `kwargs.get("input")` не `kwargs.get("messages")`.
- [ ] Snapshot / golden фајлови ажурирани на Responses стриминг облик (нема `choices[0]`, `function_call`, `logprobs` итд.).
- [ ] `pytest` пролази без грешака након свих ажурирања тестова.

### Врата понашања (потврдити ручно или преко тест хардвера)

- [ ] **Основно комплетирање**: нестриминг `responses.create` враћа непразан `output_text`.
- [ ] **Паритет стримовања**: ако је оригинални код користио стримовање, мигрирани код стримује и емитује `response.output_text.delta` догађаје са непразним делтама.
- [ ] **Структурисани излаз**: ако користи `text.format` са `json_schema`, `json.loads(resp.output_text)` успехује и поклапа се са схемом.
- [ ] **Лупа позива алатки**: ако се користе алатке, модел издaје позиве алаткама, апликација их извршава, а следећи захтев враћа коначни `output_text` (нема бесконачне петље).
- [ ] **Async паритет**: ако је коришћен `AsyncAzureOpenAI`, еквивалентни `AsyncOpenAI` ради са `await`.
- [ ] **Стопа грешака**: нема нових 400/401/404 грешака у поређењу са базом пре миграције.

### Испоруке

- Резиме укључује уређене фајлове, бројеве пре/после локација позива застарелог кода и наредне кораке.
- Промене су само радне копије (без комита).

---

## Захтеви верзије СДК-а

| Пакет | Минимална верзија |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Најновија (за EntraID аутентификацију) |

---

## Референце

- [Кратак преглед — сви исечци кода](./references/cheat-sheet.md)
- [Миграција теста — мокови, снимци, тврдње](./references/test-migration.md)
- [Отстрањавање проблема — грешке, табела ризика, замке](./references/troubleshooting.md)
- [detect_legacy.py — аутоматизовани скенер](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI почетни пакет](https://aka.ms/openai/start)
- [Azure OpenAI Responses API документација](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Животни циклус Azure OpenAI API верзије](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API референца](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->