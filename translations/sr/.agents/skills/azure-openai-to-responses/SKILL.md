---
name: azure-openai-to-responses
license: MIT
---
# Мигрирање Python апликација са Azure OpenAI Chat Completions на Responses API

> **АУТОРИТЕТСКА УПУТСТВА — ПРЕПОРУЧУЈЕ СЕ ПРЕЦИЗНО ПОСЛЕДОВАЊЕ**
>
> Ова вештина мигрира Python код који користи Azure OpenAI Chat Completions
> на уједињени Responses API. Пратите ова упутства тачно.
> Немојте импровизовати мапирање параметара или измишљати облике API-ја.

---

## Триггери

Активирајте ову вештину када корисник жели да:
- Мигрира Python апликацију са Azure OpenAI Chat Completions на Responses API
- Надогради коришћење Python OpenAI SDK на најновији облик API-ја за Azure OpenAI
- Припреми Python код за GPT-5 или новије моделе који захтевају Responses на Azure
- Прелазак са `AzureOpenAI`/`AsyncAzureOpenAI` на стандардни `OpenAI`/`AsyncOpenAI` клијент са v1 endpoint-ом
- Поправи упозорења о кварању због `AzureOpenAI` конструкторе или `api_version`

---

## ⚠️ Компатибилност модела — ПРОВЕРИТЕ ПРВО

> **Пре миграције, проверите да ли ваша Azure OpenAI имплементација подржава Responses API.**

### 1. Брзи тест имплементације (најбрже)

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

> **Напомена**: `max_output_tokens` има **минимум 16** на Azure OpenAI. Вредности испод 16 враћају грешку 400. За брзе тестове користите 50+.

Ако ово врати 404, модел на имплементацији још не подржава Responses — погледајте референце испод или поново поставите подржани модел.

### 2. Проверите доступне моделе у вашој регији (препоручено)

Покрените уграђени алат за проверу компатибилности модела да бисте видели шта је доступно са подршком за Responses API у вашој регији:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Ово упитује Azure ARM уживо и приказује матрицу компатибилности — који модели подржавају Responses, структуриран излаз, алате итд. Користите `--filter gpt-5.1,gpt-5.2` за сужење резултата или `--json` за скриптовање.

### 3. Пуна референца подршке модела

- **Уживо упит**: `python migrate.py models` (погледајте горе — специфично за регију, увек ажурирано)
- **Преглед доступности**: [Табела резимеа модела и доступност по регионима](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Брзо покретање и упутства**: **https://aka.ms/openai/start**

### ⚠️ Ограничења старијих модела

> **УПОЗОРЕЊЕ**: Старији модели (пре `gpt-4.1`) можда не подржавају све функције Responses API у потпуности.
>
> Позната ограничења са старијим моделима:
> - **параметар `reasoning`**: Неподржан на многим моделима без rasuđivanja. Мигрирајте `reasoning` само ако је већ био присутан у оригиналном коду.
> - **параметар `seed`**: Уопште није подржан у Responses API — уклоните из свих захтева.
> - **Структурирани излаз преко `text.format`**: Старији модели можда не примењују поуздано `strict: true` JSON шеме.
> - **Оркестрација алата**: GPT-5+ оркестрира позиве алата као део интерног расуђивања. Старији модели на Responses раде али без ове дубоке интеграције.
> - **Ограничења температуре**: При миграцији на `gpt-5`, температура мора бити изостављена или постављена на `1`. Старији модели немају овакво ограничење.

### O-серија модела за расуђивање (o1, o3-mini, o3, o4-mini)

O-серија модели имају јединствена ограничења параметара. При миграцији апликација које циљају o-серију:

- **`temperature`**: Мора бити `1` (или изостављен). O-серија модели не прихватају друге вредности.
- **`max_completion_tokens` → `max_output_tokens`**: Апликације које користе Azure-специфични `max_completion_tokens` морају прелазити на `max_output_tokens`. Подесите високе вредности (4096+) јер tokeni за rasuđivanje улазe у лимит.
- **`reasoning_effort`**: Ако апликација користи `reasoning_effort` (low/medium/high), задржите га — Responses API подржава овај параметар за o-серију модела.
- **Понашање стримовања**: O-серија модели можда кеширају излаз док се rasuđivanje не заврши пре емитовања текстуалних delta догађаја. Стримовање и даље ради, али први `response.output_text.delta` може стићи са дужим закашњењем него код GPT модела.
- **`top_p`**: Неподржан на o-серији — уклоните ако је присутан.
- **Коришћење алата**: O-серија модели подржавају алате преко Responses API исто као GPT модели, али квалитет оркестрације позива алата варира по моделу.

**Акција — проактивни савет о моделу**: Током фазе скенирања провјерите који модел апликација користи (називи имплементација, окружене променљиве, конфигурација). Ако је модел старији од `gpt-4.1` (не gpt-4.1+), проактивно обавестите корисника:
- Миграција ће радити за основни текст, ћаскање, стримовање и алате са њиховим тренутним моделом.
- Новији модели (`gpt-5.1`, `gpt-5.2`) нуде бољу оркестрацију алата, примену структурираног излаза, расуђивање и доступност преко региона.
- Требало би да размотре надоградњу имплементације кад буду спремни — то не блокира миграцију.

Не блокирајте и не одбијајте миграцију због верзије модела. Савет је информативан.

### GitHub модели НЕ подржавају Responses API

> **GitHub модели (`models.github.ai`, `models.inference.ai.azure.com`) не подржавају Responses API.**

Ако кодна база има кодни пут за GitHub моделе (потражите `base_url` који указује на `models.github.ai` или `models.inference.ai.azure.com`), **уклоните га у потпуности** током миграције. Responses API захтева Azure OpenAI, OpenAI или компатибилан локални endpoint (нпр. Ollama са Responses подршком).

Акција током скенирања:
- Обележите све кодне путеве GitHub модела за уклањање.

---

## Миграција оквира (framework-a)

Многе апликације користе вишем нивоу оквире изнад OpenAI. При миграцији ових, мења се сопствени API оквира — не само основни OpenAI позиви.

### Microsoft Agent Framework (MAF)

**Прво проверите вашу верзију MAF-а** — миграција зависи од тога да ли сте на MAF 1.0.0+ или пре-1.0.0 бета/rc верзијама.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **већ користи Responses API** — није потребна миграција. Ако кодна база користи застарели `OpenAIChatCompletionClient` (који користи `chat.completions.create`), замените га са `OpenAIChatClient`.

| Пре | После |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Да проверите верзију: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF пре-1.0.0 (бета/rc издања)

У пре-1.0.0 MAF, `OpenAIChatClient` је користио Chat Completions. Надоградите на `agent-framework-openai>=1.0.0` где `OpenAIChatClient` по дефаулту користи Responses API.

Друге промене нису потребне — API-ји `Agent` и алата остају исти.

### LangChain (`langchain-openai`)

Додајте `use_responses_api=True` у `ChatOpenAI()`. Такође ажурирајте приступ одговору са `.content` на `.text`.

| Пре | После |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

За комплетне примере кода пре/после гледајте [cheat-sheet.md](./references/cheat-sheet.md).

---

## Упутства за миграцију фронтенда

> **Responses API је ствар серверске стране.** Мигрирајте Python backend; HTTP ugovor фронтенда треба остати непромењен осим ако ваш backend није само танак пролаз — у том случају размотрите прилагођавање облика Responses захтева да елиминишете слој превођења. Ако фронтенд директно позива OpenAI са клијентским кључем, прво преместите те позиве на backend.

### `@microsoft/ai-chat-protocol` депрецатион

npm пакет `@microsoft/ai-chat-protocol` је депрецатион и треба га заменити са [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Ако га пронађете у фронтенду:

1. Замените CDN script tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Уклони инстанцирање `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Замените `client.getStreamedCompletion(messages)` директним `fetch()` позивом на backend стриминг endpoint.
4. Замените `for await (const response of result)` са `for await (const chunk of readNDJSONStream(response.body))`.
5. Ажурирајте приступ својствима са `response.delta.content` / `response.error` на `chunk.delta.content` / `chunk.error`.

---

## Циљеви

- Пописати све Python позиве који користе Chat Completions или Legacy Completions са Azure OpenAI.
- Предложити план миграције и редослед за Python код.
- Примени безбедне, минималне измене за прелазак на Responses API.
- Ажурирати позиваче за коришћење Responses output шеме; без штићених замотача.
- Покренути тестове/лінтове; поправити тривијалне грешке настале миграцијом.
- Припремити мале, прегледне скупове промена и пружити коначни резиме са дифовима (не комитујте).

---

## Ограничења (Guardrails)

- Мењати само фајлове унутар git workspace-а. Никада не писати изван.
- Не чувати шиме за назадну компатибилност; мигрирајте код на нови облик API.
- Не остављати коментаре за транзицију или бекуп фајлове.
- Очувати семантику стримовања ако је раније коришћена; иначе користити нестреминг.
- Тражити одобрење пре покретања команди или мрежних позива у режиму одобрења.
- Не покретати `git add`/`git commit`/`git push`; радити само измене у радном простору.

---

## Корак 0: Миграција Azure OpenAI клијента (претпоставка)

Ако код користи конструкторе `AzureOpenAI` или `AsyncAzureOpenAI`, прво мигрирајте на стандардне конструкторе `OpenAI` / `AsyncOpenAI`. Azure специфични конструктори су депрецатирани у `openai>=1.108.1`.

### Зашто v1 API пут?

Нови `/openai/v1` endpoint користи стандардни `OpenAI()` клијент уместо `AzureOpenAI()`, не захтева параметар `api_version`, и ради идентично на OpenAI и Azure OpenAI. Исти клиентски код је отпоран на будућност — нема потребе за управљањем верзијама.

### Кључне промене

| Пре | После |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Уклонити у потпуности |

### Контролна листа за чишћење

- Уклонити аргумент `api_version` из конструктора клијента.
- Уклонити окружења `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` из `.env`, подешавања апликације и Bicep/infra фајлова.
- Преименовати `AZURE_OPENAI_CLIENT_ID` у `AZURE_CLIENT_ID` у `.env`, подешавањима апликације, Bicep/infra и тест фиxtures (стандардна Azure Identity SDK конвенција).
- Осигурати `openai>=1.108.1` у `requirements.txt` или `pyproject.toml`.

### Миграција окружења

| Стари env var | Акција | Напомене |
|-------------|--------|----------|
| `AZURE_OPENAI_VERSION` | **Уклони** | Није потребно са v1 endpoint-ом |
| `AZURE_OPENAI_API_VERSION` | **Уклони** | Исто као горе |
| `AZURE_OPENAI_CLIENT_ID` | **Преимenuј** → `AZURE_CLIENT_ID` | Стандартна Azure Identity SDK конвенција за `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Задржи** | Још увек је потребан за конструкцију `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Задржи** | Користи се као `model` параметар у `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Задржи** | Користи се као `api_key` за аутентикацију кључем |

За примере подешавања клијента (синхрони, асинхрони, EntraID, API кључ, мултитенант), видети [cheat-sheet.md](./references/cheat-sheet.md).

---

## Корак 1: Препознавање застарелих позива

Покрените скрипту [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) да пронађете све позиције позива које треба мигрирати:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Или покрените ове претраге ручно — сваки поклапајући случај је мета миграције:

```bash
# Легендарни API позиви (морају се преписати)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Застарели конструктори Azure клијента (морају се заменити)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Обрасци приступа облику одговора (морају се ажурирати)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Дефиниције алата у старом унутрашњем формату (морају се поравнати)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Резултати алата у старом формату (морају се конвертовати у function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Застарели параметри (морају се уклонити или преименовати)
rg "response_format"
rg "max_tokens\b"        # преименовати у max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Застареле променљиве окружења (очистити)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # требало би да буде AZURE_CLIENT_ID

# GitHub Models крајње тачке (морају се уклонити — Responses API није подржан)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Легендарни обрасци на нивоу фрејмворка (морају се ажурирати)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: заменити са OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: потребно use_responses_api=True

# Тест инфраструктура (мора се ажурирати)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Приступ телу грешке филтера садржаја (мора се ажурирати — структура је промењена)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # стари једниначки облик — сад content_filter_results (множествени) унутар content_filters низа

# Сирови HTTP позиви ка Chat Completions крајњој тачки (мора се ажурирати URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Хеуристике (препознавање и преписивање)

- **Chat Completions клијент**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure клијент конструктори**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Алати**: претвори дефиниције алата за позив функција из уметнутог формата (`{"type": "function", "function": {"name": ...}}`) у раван Responses формат (`{"type": "function", "name": ...}`); користи `tool_choice`; врати резултате алата као ставке `{"type": "function_call_output", "call_id": ..., "output": ...}` (не `{"role": "tool", ...}`).
- **Повратак алата**: када модел враћа позиве функција, додај ставке `response.output` у разговор (не ручни речник `{"role": "assistant", "tool_calls": [...]}`), затим додај ставке `function_call_output` за сваки резултат.
- **Примери за неколико позива алата**: ако разговор укључује примерима позива алата у коду, претвори их у `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` ставке. ИД-ови морају почети од `fc_`.
- **`pydantic_function_tool()`**: овај помоћни алат још увек генерише стари уметнути формат и **није компатибилан** са `responses.create()`. Замени ручним дефиницијама алата или омотачем за раван формат.
- **Више корака**: одржавај историју разговора у апликацији; претходне кораке прослеђуј кроз ставке `input`.
- **Форматирање**: замени горњи `response_format` из Чата са `text.format` у Responses. Канонски облик: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Ставке садржаја**: замени Chat `content[].type: "text"` са Responses `content[].type: "input_text"` за корисничке/системске кораке.
- **Ставке слике у садржају**: замени Chat `content[].type: "image_url"` са Responses `content[].type: "input_image"`. Поље `image_url` се мења из уметнутог објекта `{"url": "..."}` у равни низ. Погледај у листу примера пре/после.
- **Напор размишљања**: **мигрирај `reasoning` само ако већ постоји у оригиналном коду**.
- **Руковање грешкама филтера садржаја**: структура тела грешке се променила. Chat Completions је користио `error.body["innererror"]["content_filter_result"]` (једнина); Responses API користи `error.body["content_filters"][0]["content_filter_results"]` (множеина, унутар низа). Код који приступа `innererror` ће изазвати `KeyError`. Препиши да користи нови пут.
- **Сирови HTTP позиви**: ако апликација директно позива Azure OpenAI REST API (путем `requests`, `httpx`, итд.) користећи `/openai/deployments/{name}/chat/completions?api-version=...`, препиши на `/openai/v1/responses`. Тело захтева се мења: `messages` → `input`, додај `max_output_tokens` и `store: false`, уклони `api-version` query параметар. Тело одговора се мења: `choices[0].message.content` → `output[0].content[0].text` (напр: `output_text` је SDK погодност својство које није присутно у сировом REST JSON-у).

---

## Корак 2: Примени миграцију

### Напомене о миграцији (Chat Completions → Responses)

- **Зашто мигрирати**: Responses је јединствени API за текст, алате и стриминг; Chat Completions је наслеђе. Са GPT-5, Responses је обавезан за најбоље перформансе.
- **HTTP**: Azure крајња тачка се мења са `/openai/deployments/{name}/chat/completions` на `/openai/v1/responses`.
- **Поља**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` остаје иста.
- **Форматирање**: `response_format` → `text.format` са одговарајућим објектом.
- **Ставке садржаја**: замени Chat `content[].type: "text"` са Responses `content[].type: "input_text"` за системске/корисничке кораке.
- **Ставке слике у садржају**: замени Chat `content[].type: "image_url"` са Responses `content[].type: "input_image"`. Поједностави поље `image_url` из `{"image_url": {"url": "..."}}` у `{"image_url": "..."}` (обичан низ — или HTTPS URL или `data:image/...;base64,...` data URI).

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
| `tools` / function-calling | `tools` (непромењено) |
| `seed` | **Уклони** (није подржано) |
| `store` | `store` (постављено на `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (равни низ) |

За потпуне примере кода пре/после, види [cheat-sheet.md](./references/cheat-sheet.md).

За миграцију тест инфраструктуре (мокови, снимци, асертиције), види [test-migration.md](./references/test-migration.md).

За решавање грешака и проблематика, види [troubleshooting.md](./references/troubleshooting.md).

---

## Чување података и стање

- Постави `store: false` на све захтеве Responses.
- Не ослањај се на претходне ИД-ове порука или контекст чuvan на серверу; одржавај стање под управом клијента и минимизирај метаподатке.

---

## Критеријуми прихватања

### Провере на нивоу кода (све морају проћи)

- [ ] Ниједно поклапање за `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` у мигрираним фајловима.
- [ ] Ниједно поклапање за `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — сви конструктори користе `OpenAI`/`AsyncOpenAI` са v1 крајњом тачком.
- [ ] Ниједно поклапање за `rg "models\.github\.ai|models\.inference\.ai\.azure"` — уклоњени код путеви за GitHub Models.
- [ ] Ниједно поклапање за `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ код користи `OpenAIChatClient` (који користи Responses API). У верзијама пре 1.0.0, ажурирај на `agent-framework-openai>=1.0.0`.
- [ ] Сви позиви `ChatOpenAI(...)` укључују `use_responses_api=True`.
- [ ] Ниједно поклапање за `rg "choices\[0\]"` — сав приступ одговорима користи `resp.output_text` или Responses output шему.
- [ ] Нема `response_format` на горњем нивоу; сваки структуирани излаз користи `text={"format": {...}}`.
- [ ] `openai>=1.108.1` и `azure-identity` у `requirements.txt` или `pyproject.toml`; зависности поново инсталиране.
- [ ] `store=False` подешено на сваком `responses.create` позиву.
- [ ] Нема `api_version` у конструкцији клијента; `AZURE_OPENAI_API_VERSION` уклоњен из env фајлова и инфраструктуре.

### Провере тест инфраструктуре (све морају проћи)

- [ ] Ниједно поклапање за `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Ниједно поклапање за `rg "_azure_ad_token_provider" tests/` — асертиције ажуриране да провере `isinstance(client, AsyncOpenAI)` или `base_url`.
- [ ] Ниједно поклапање за `rg "prompt_filter_results|content_filter_results" tests/` — уклоњени Azure-специфични филтер мокови.
- [ ] Мок фикстуре користе `kwargs.get("input")` а не `kwargs.get("messages")`.
- [ ] Снимци/голд файлови ажурирани на Responses стриминг облик (нема `choices[0]`, `function_call`, `logprobs`, итд.).
- [ ] `pytest` пролази са нула грешака након свих ажурирања тестова.

### Понашајне провере (верификација ручно или путем тест хрна)

- [ ] **Основни излаз**: нестриминг `responses.create` враћа непразан `output_text`.
- [ ] **Потпуна сличност стриминга**: ако је оригинални код користио стриминг, мигрирани код стримује и враћа `response.output_text.delta` догађаје са непразним делтама.
- [ ] **Структурирани излаз**: ако се користи `text.format` са `json_schema`, `json.loads(resp.output_text)` успева и одговара шеми.
- [ ] **Петља позива алата**: ако се користе алати, модел шаље позиве алатима, апликација их извршава, а следећи захтев враћа коначан `output_text` (нема бесконачне петље).
- [ ] **Async сличност**: ако је коришћен `AsyncAzureOpenAI`, еквивалент `AsyncOpenAI` ради са `await`.
- [ ] **Стопа грешака**: нема нових 400/401/404 грешака у односу на довољену верзију пре миграције.

### Испоруке

- Резиме укључује измењене фајлове, број позива Legacy пре/после и следеће кораке.
- Промене су само радне копије (без комита).

---

## Захтеви за верзију SDK-а

| Пакет | Минимална верзија |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Најновија (за EntraID аутентификацију) |

---

## Референце

- [Листа варалица — сви примери кода](./references/cheat-sheet.md)
- [Миграција теста — мокови, снимци, асертиције](./references/test-migration.md)
- [Решавање проблема — грешке, табела ризика, замке](./references/troubleshooting.md)
- [detect_legacy.py — аутоматизовани скенер](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI скуп за почетнике](https://aka.ms/openai/start)
- [Azure OpenAI Responses API документација](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Животни циклус Azure OpenAI API верзије](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API референца](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->