---
name: azure-openai-to-responses
license: MIT
---
# Мигриране на Python приложения от Azure OpenAI Chat Completions към Responses API

> **АВТОРИТЕТНО РЪКОВОДСТВО — СПАЗВАЙТЕ ТОЧНО**
>
> Тази функция мигрира Python кодови бази, използващи Azure OpenAI Chat Completions
> към унифицирания Responses API. Следвайте тези инструкции прецизно.
> Не импровизирайте с параметрични съпоставяния или измисляйте форми на API.

---

## Тригери

Активирайте тази функция, когато потребителят иска да:
- Мигрира Python приложение от Azure OpenAI Chat Completions към Responses API
- Обнови употребата на Python OpenAI SDK до последната форма на API спрямо Azure OpenAI
- Подготви Python код за модели GPT-5 или по-нови, които изискват Responses на Azure
- Превключи от `AzureOpenAI`/`AsyncAzureOpenAI` към стандартния `OpenAI`/`AsyncOpenAI` клиент с v1 endpoint
- Поправи предупреждения за оттегляне, свързани с конструкторите на `AzureOpenAI` или `api_version`

---

## ⚠️ Съвместимост на моделите — ПРОВЕРЕТЕ ПЪРВО

> **Преди миграцията, уверете се, че вашето разгръщане на Azure OpenAI поддържа Responses API.**

### 1. Бърз тест на разгръщането (най-бърз)

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

> **Бележка**: `max_output_tokens` има **минимум 16** в Azure OpenAI. Стойности под 16 връщат грешка 400. Използвайте 50+ за бързи тестове.

Ако това връща 404, моделът на разгръщането все още не поддържа Responses — проверете референцията по-долу или преинсталирайте с поддържан модел.

### 2. Проверете наличните модели във вашия регион (препоръчително)

Стартирайте вградения инструмент за съвместимост на модели, за да видите какво е налично с поддръжка на Responses API във вашия конкретен регион:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Това заявява директно към Azure ARM и показва матрица на съвместимост — кои модели поддържат Responses, структурирани изходи, инструменти и др. Използвайте `--filter gpt-5.1,gpt-5.2` за филтриране или `--json` за скриптиране.

### 3. Пълна референция за поддръжка на модели

- **Живо запитване**: `python migrate.py models` (вижте по-горе — специфично за регион, винаги актуално)
- **Преглед на наличности**: [Таблица с обобщение на модели и регионална наличност](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Бърз старт и ръководство**: **https://aka.ms/openai/start**

### ⚠️ Ограничения на по-старите модели

> **ВНИМАНИЕ**: По-старите модели (тези преди `gpt-4.1`) може да не поддържат всички функции на Responses API пълноценно.
>
> Известни ограничения с по-старите модели:
> - **Параметър `reasoning`**: Не се поддържа при много модели без reasoning. Мигрирайте `reasoning` само ако вече присъства в оригиналния код.
> - **Параметър `seed`**: Не се поддържа изобщо в Responses API — премахнете го от всички заявки.
> - **Структуриран изход чрез `text.format`**: При по-старите модели `strict: true` JSON схеми може да не се налагат надеждно.
> - **Оркестрация на инструменти**: GPT-5+ обработва извиквания на инструменти като част от вътрешния reasoning. По-старите модели на Responses работят, но им липсва тази дълбока интеграция.
> - **Ограничения на температурата**: При мигриране към `gpt-5`, температурата трябва да се пропусне или зададе на `1`. По-старите модели нямат такова ограничение.

### O-серия reasoning модели (o1, o3-mini, o3, o4-mini)

Моделите от серия O имат уникални параметрични ограничения. При мигриране на приложения, които целят тези модели:

- **`temperature`**: Трябва да бъде `1` (или пропуснат). O-серия моделите не приемат други стойности.
- **`max_completion_tokens` → `max_output_tokens`**: Приложения, използващи Azure-специфичния `max_completion_tokens`, трябва да преминат към `max_output_tokens`. Задайте високи стойности (4096+) тъй като токените за reasoning се броят към лимита.
- **`reasoning_effort`**: Ако приложението използва `reasoning_effort` (ниско/средно/високо), запазете това — Responses API поддържа този параметър за o-серия модели.
- **Поведение на стрийминг**: O-серия моделите може да буферират изхода до приключване на reasoning преди да изпратят събития с текстови дялове. Стриймингът все още работи, но първият `response.output_text.delta` може да пристигне с по-голямо изчакване спрямо GPT моделите.
- **`top_p`**: Не се поддържа на o-серия — премахнете го, ако е наличен.
- **Употреба на инструменти**: O-серия моделите поддържат инструменти чрез Responses API както GPT моделите, но качеството на оркестрация на извикванията варира по модели.

**Действие — проактивна информационна препоръка**: По време на сканиране проверявайте към кой модел таргетира приложението (имена на разгръщания, системни променливи, конфигурация). Ако моделът е преди `gpt-4.1` (не е gpt-4.1+), проактивно уведомете потребителя:
- Миграцията ще работи за базов текст, чат, стрийминг и инструменти на текущия му модел.
- По-новите модели (`gpt-5.1`, `gpt-5.2`) предлагат по-добра оркестрация на инструменти, прилагане на структурирани изходи, reasoning и крос-регионална наличност.
- Те трябва да обмислят ъпгрейд на разгръщането си когато са готови — това не блокира миграцията.

Не блокирайте или отказвайте миграция според версията на модела. Информацията е само препоръчителна.

### GitHub моделите НЕ поддържат Responses API

> **GitHub моделите (`models.github.ai`, `models.inference.ai.azure.com`) не поддържат Responses API.**

Ако кодовата база съдържа път за GitHub модели (потърсете `base_url`, сочещ към `models.github.ai` или `models.inference.ai.azure.com`), **премахнете го изцяло** при миграцията. Responses API изисква Azure OpenAI, OpenAI, или съвместим локален endpoint (например Ollama с Responses поддръжка).

Действия по време на сканиране:
- Отбележете всеки кодов път с GitHub модели за премахване.

---

## Миграция на рамката (Framework)

Много приложения използват по-високо ниво рамки върху OpenAI. При миграция на тези, промените са в самия API на рамката — не само основните OpenAI извиквания.

### Microsoft Agent Framework (MAF)

**Проверете първо версията на MAF** — миграцията зависи дали сте на MAF 1.0.0+ или на пред-1.0.0 бета/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **вече използва Responses API** — няма нужда от миграция. Ако кодовата база използва остарялото `OpenAIChatCompletionClient` (който ползва `chat.completions.create`), заменете го с `OpenAIChatClient`.

| Преди | След |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

За да проверите версията: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF преди 1.0.0 (бета/rc версии)

В пред-1.0.0 MAF, `OpenAIChatClient` използва Chat Completions. Ъпгрейднете до `agent-framework-openai>=1.0.0`, където `OpenAIChatClient` по подразбиране използва Responses API.

Други промени не са необходими — `Agent` и инструменталните API остават същите.

### LangChain (`langchain-openai`)

Добавете `use_responses_api=True` на `ChatOpenAI()`. Също така обновете достъпа до отговорите от `.content` към `.text`.

| Преди | След |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

За пълни пример кодове преди/след, вижте [cheat-sheet.md](./references/cheat-sheet.md).

---

## Ръководство за миграция на фронтенд

> **Responses API е грижа на сървърната страна.** Мигрирайте backend на Python; HTTP контракта на фронтенда трябва да остане непроменен, освен ако backend не е тънък пропускателен слой — в такъв случай обмислете да приемете формата на Responses заявки, за да елиминирате слой превод. Ако фронтенд извиква OpenAI директно с ключ на клиентската страна, преместете тези извиквания първо в backend.

### Оттегляне на `@microsoft/ai-chat-protocol`

Пакетът npm `@microsoft/ai-chat-protocol` е оттеглен и трябва да бъде заменен с [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Ако го срещнете във фронтенд:

1. Заменете CDN скрипт тага:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Премахнете инстанцията `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Заменете `client.getStreamedCompletion(messages)` с директно `fetch()` извикване към backend стрийминг endpoint.
4. Заменете `for await (const response of result)` с `for await (const chunk of readNDJSONStream(response.body))`.
5. Обновете достъпа до свойства от `response.delta.content` / `response.error` към `chunk.delta.content` / `chunk.error`.

---

## Цели

- Изброяване на всички Python извиквания, използващи Chat Completions или остарели Completions срещу Azure OpenAI.
- Предложете план и последователност за миграция на Python кодовата база.
- Прилагане на сигурни, минимални редакции за превключване към Responses API.
- Актуализиране на извикващите, за да консумират схемата за изход на Responses; няма нужда от обвивни backward-compatibility решения.
- Изпълнете тестове/линт проверки; поправете дребни счупвания, въведени при миграцията.
- Подгответе малки, лесно рецензируеми набори промени и предоставете финално резюме с дифове (не комитвайте).

---

## Граници

- Променяйте само файлове в git workspace. Никога не пишете извън него.
- Не запазвайте backward-compatibility шими; мигрирайте кода към новата форма на API.
- Не оставяйте преходни коментари или резервни копия на файлове.
- Запазвайте семантиката на стрийминг ако преди сте я използвали; иначе използвайте не-стрийминг.
- Поискайте одобрение преди изпълнение на команди или мрежови извиквания, ако сте в режим на одобрение.
- Не изпълнявайте `git add`/`git commit`/`git push`; правете само редакции на работното дърво.

---

## Стъпка 0: Миграция на Azure OpenAI клиент (предварително условие)

Ако кодовата база използва конструктори `AzureOpenAI` или `AsyncAzureOpenAI`, първо мигрирайте към стандартните конструктори `OpenAI` / `AsyncOpenAI`. Специфичните конструктори за Azure са оттеглени в `openai>=1.108.1`.

### Защо API пътя v1?

Новият endpoint `/openai/v1` използва стандартния клиент `OpenAI()` вместо `AzureOpenAI()`, не изисква параметър `api_version` и работи еднакво както с OpenAI, така и с Azure OpenAI. Същият клиент код е бъдещо устойчива — няма нужда от управление на версии.

### Основни промени

| Преди | След |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Премахнете напълно |

### Контролен списък за почистване

- Премахнете аргумента `api_version` от конструктора на клиента.
- Премахнете променливите на средата `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` от `.env`, настройки на приложение и Bicep/infra файлове.
- Преименувайте `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` в `.env`, настройки на приложение, Bicep/infra и тестови фикстури (стандартна конвенция на Azure Identity SDK).
- Уверете се, че `openai>=1.108.1` е в `requirements.txt` или `pyproject.toml`.

### Миграция на променливи на средата

| Стара променлива | Действие | Забележки |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Премахнете** | Не е нужна `api_version` с v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Премахнете** | Същото като по-горе |
| `AZURE_OPENAI_CLIENT_ID` | **Преименувайте** → `AZURE_CLIENT_ID` | Стандартна конвенция на Azure Identity SDK за `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Запазете** | Все още се използва за конструкция на `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Запазете** | Използва се като параметър `model` в `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Запазете** | Използва се като `api_key` за автентикация с ключ |

За примери за настройка на клиент (синхронен, асинхронен, EntraID, API ключ, мулти-клиентски), вижте [cheat-sheet.md](./references/cheat-sheet.md).

---

## Стъпка 1: Откриване на остарели извиквания

Стартирайте скрипта [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) за намиране на всички извиквания, които трябва да бъдат мигрирани:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Или изпълнете тези търсения ръчно — всяко съвпадение е цел за миграция:

```bash
# Обаждания към остарял API (трябва преписване)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Остарели конструктори на Azure клиент (трябва замяна)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Модели за достъп до формата на отговорите (трябва обновяване)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Определения на инструменти в стар вложен формат (трябва изглаждане)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Резултати от инструменти в стар формат (трябва конвертиране във function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Остарели параметри (трябва премахване или преименуване)
rg "response_format"
rg "max_tokens\b"        # преименувай на max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Остарели променливи на средата (почистване)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # трябва да е AZURE_CLIENT_ID

# Крайни точки на GitHub Models (трябва премахване — Responses API не се поддържа)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Наследствени модели на ниво фреймуърк (трябва обновяване)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: замени с OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: изисква use_responses_api=True

# Тестова инфраструктура (трябва обновяване)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Достъп до тялото на грешката при филтър за съдържание (трябва обновяване — структурата се е променила)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # старо единствено число — сега content_filter_results (множествено) вътре в масива content_filters

# Сурови HTTP повиквания към крайна точка Chat Completions (трябва обновяване на URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Евристики (откриване и преписване)

- **Chat Completions клиент**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Конструктори на Azure клиент**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Инструменти**: конвертирайте дефинициите на инструментите за извикване на функции от вложен формат (`{"type": "function", "function": {"name": ...}}`) във формат на Responses (`{"type": "function", "name": ...}`); използвайте `tool_choice`; връщайте резултатите от инструмента като елементи `{"type": "function_call_output", "call_id": ..., "output": ...}` (не като `{"role": "tool", ...}`).
- **Обратни трансформации на инструментите**: когато моделът връща извиквания на функции, добавяйте елементите `response.output` към разговора (не ръчно речник `{"role": "assistant", "tool_calls": [...]}`), след което добавяйте елементите `function_call_output` за всеки резултат.
- **Примери с малък брой удари за инструменти**: ако в разговора има твърдо кодирани примери за извикване на инструменти, конвертирайте ги в елементи `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Идентификаторите трябва да започват с `fc_`.
- **`pydantic_function_tool()`**: този помощник все още генерира стария вложен формат и **не е съвместим** с `responses.create()`. Заменете с ръчно дефинирани инструменти или обвивка за изравняване.
- **Многостъпков режим**: поддържайте история на разговора в приложението; предавайте предишни ходове чрез елементи `input`.
- **Форматиране**: заменете главното ниво `response_format` на Chat с `text.format` в Responses. Канонична форма: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Елементи съдържание**: заменете `content[].type: "text"` в Chat с `content[].type: "input_text"` в Responses за ходове на потребител/система.
- **Елементи съдържание с изображения**: заменете `content[].type: "image_url"` в Chat с `content[].type: "input_image"` в Responses. Полето `image_url` се променя от вложен обект `{"url": "..."}` на плосък низ. Вижте листа с препоръки за примери преди/след.
- **Усилие за логическо обяснение**: **мигрирайте `reasoning` само ако вече съществува в оригиналния код**.
- **Обработка на грешки от филтъра на съдържание**: структурата на тялото на грешката се промени. Chat Completions използваше `error.body["innererror"]["content_filter_result"]` (в единствено число); Responses API използва `error.body["content_filters"][0]["content_filter_results"]` (в множествено число вътре в масив). Код, който достъпва `innererror`, ще вдигне `KeyError`. Пренапишете, за да използвате новия път.
- **Сурови HTTP повиквания**: ако приложението директно извиква Azure OpenAI REST API (чрез `requests`, `httpx` и др.) с `/openai/deployments/{name}/chat/completions?api-version=...`, пренапишете към `/openai/v1/responses`. Тялото на заявката се променя: `messages` → `input`, добавя се `max_output_tokens` и `store: false`, премахва се заявният параметър `api-version`. Тялото на отговора се променя: `choices[0].message.content` → `output[0].content[0].text` (забележка: `output_text` е удобство в SDK, което липсва в суровия REST JSON).

---

## Стъпка 2: Приложете миграцията

### Бележки по миграцията (Chat Completions → Responses)

- **Защо да мигрираме**: Responses е унифицирано API за текст, инструменти и стрийминг; Chat Completions е наследен. С GPT-5 Responses се изисква за най-добра производителност.
- **HTTP**: Azure ендпойнт преминава от `/openai/deployments/{name}/chat/completions` към `/openai/v1/responses`.
- **Полетата**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` остава.
- **Форматиране**: `response_format` → `text.format` с правилен обект.
- **Елементи съдържание**: Заменете `content[].type: "text"` в Chat с `content[].type: "input_text"` в Responses за системни и потребителски ходове.
- **Елементи съдържание с изображения**: Заменете `content[].type: "image_url"` в Chat с `content[].type: "input_image"` в Responses. Изравнете полето `image_url` от `{"image_url": {"url": "..."}}` в `{"image_url": "..."}` (обикновен низ — HTTPS URL или data URI от тип `data:image/...;base64,...`).

### Справка със съпоставяне на параметри

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (масив от елементи) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (обект) |
| `temperature` | `temperature` (непроменено) |
| `stop` | `stop` (непроменено) |
| `frequency_penalty` | `frequency_penalty` (непроменено) |
| `presence_penalty` | `presence_penalty` (непроменено) |
| `tools` / извикване на функции | `tools` (непроменено) |
| `seed` | **Премахнете** (не се поддържа) |
| `store` | `store` (зададено на `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (плосък низ) |

За пълни примери с код преди и след, вижте [cheat-sheet.md](./references/cheat-sheet.md).

За миграция на тестова инфраструктура (мокове, снимки, проверки), вижте [test-migration.md](./references/test-migration.md).

За отстраняване на грешки и често срещани проблеми, вижте [troubleshooting.md](./references/troubleshooting.md).

---

## Съхранение на данни и състояние

- Задайте `store: false` на всички заявки към Responses.
- Не се доверявайте на предишни идентификатори на съобщения или контекст, съхраняван на сървъра; управлявайте състоянието от клиента и минимизирайте метаданните.

---

## Критерии за приемане

### Кодови проверки (всички трябва да преминат)

- [ ] Нулев брой съвпадения за `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` в мигрираните файлове.
- [ ] Нулев брой съвпадения за `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — всички конструктори използват `OpenAI`/`AsyncOpenAI` с v1 ендпойнт.
- [ ] Нулев брой съвпадения за `rg "models\.github\.ai|models\.inference\.ai\.azure"` — премахнати са пътища в кода за модели на GitHub.
- [ ] Нулев брой съвпадения за `rg "OpenAIChatCompletionClient"` — кодът от MAF 1.0.0+ използва `OpenAIChatClient` (който използва Responses API). В преди 1.0.0 ъпгрейднете до `agent-framework-openai>=1.0.0`.
- [ ] Всички повиквания `ChatOpenAI(...)` включват `use_responses_api=True`.
- [ ] Нулев брой съвпадения за `rg "choices\[0\]"` — целият достъп до отговори използва `resp.output_text` или схемата за отговори на Responses.
- [ ] Няма `response_format` на главно ниво; цялата структурирана продукция използва `text={"format": {...}}`.
- [ ] `openai>=1.108.1` и `azure-identity` в `requirements.txt` или `pyproject.toml`; зависимости преинсталирани.
- [ ] `store=False` зададено във всяко извикване на `responses.create`.
- [ ] Няма `api_version` в конструкцията на клиента; `AZURE_OPENAI_API_VERSION` премахнат от файловете с околна среда и инфраструктурата.

### Тестови инфраструктурни проверки (всички трябва да преминат)

- [ ] Нулев брой съвпадения за `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Нулев брой съвпадения за `rg "_azure_ad_token_provider" tests/` — проверки актуализирани да проверяват `isinstance(client, AsyncOpenAI)` или `base_url`.
- [ ] Нулев брой съвпадения за `rg "prompt_filter_results|content_filter_results" tests/` — премахнати са мокове, специфични за Azure филтри.
- [ ] Моковете използват `kwargs.get("input")`, не `kwargs.get("messages")`.
- [ ] Файловете със снимки / златни файлове са актуализирани към формата на Responses за стрийминг (няма `choices[0]`, `function_call`, `logprobs` и т.н.).
- [ ] `pytest` минава без грешки след всички тестови актуализации.

### Поведенчески проверки (проверяват се ръчно или с тестови инструменти)

- [ ] **Основно завършване**: нестрийминг `responses.create` връща непразен `output_text`.
- [ ] **Паритет на стрийминг**: ако оригиналният код използваше стрийминг, мигрираният код стриймва и излъчва събития `response.output_text.delta` с непразни делти.
- [ ] **Структуриран изход**: ако се използва `text.format` с `json_schema`, `json.loads(resp.output_text)` е успешна и съвпада със схемата.
- [ ] **Цикъл за извикване на инструменти**: ако се използват инструменти, моделът издава извиквания на инструменти, приложението ги изпълнява, а следващата заявка връща финален `output_text` (няма безкраен цикъл).
- [ ] **Паритет на асинхронност**: ако е използван `AsyncAzureOpenAI`, равностойният `AsyncOpenAI` работи с `await`.
- [ ] **Ниво на грешки**: няма нови грешки 400/401/404 в сравнение с базовата линия преди миграцията.

### Доставки

- Резюмето включва редактирани файлове, брой повиквания на наследен код преди/след и следващи стъпки.
- Промените са само като редакции в работното дърво (без комити).

---

## Изисквания за версия на SDK

| Пакет | Минимална версия |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Най-нова (за EntraID автентикация) |

---

## Препратки

- [Cheat Sheet — всички кодови фрагменти](./references/cheat-sheet.md)
- [Test Migration — мокове, снимки, проверки](./references/test-migration.md)
- [Troubleshooting — грешки, таблица с рискове, често срещани проблеми](./references/troubleshooting.md)
- [detect_legacy.py — автоматизиран скенер](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API docs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->