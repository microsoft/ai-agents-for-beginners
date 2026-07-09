---
name: azure-openai-to-responses
license: MIT
---
# Мигриране на Python приложения от Azure OpenAI Chat Completions към Responses API

> **АВТОРИТАТИВНИ НАСТРОЙКИ — СПАЗВАЙТЕ ТОЧНО**
>
> Този модул мигрира Python кодови бази, използващи Azure OpenAI Chat Completions
> към унифицирания Responses API. Следвайте тези инструкции точно.
> Не измисляйте съпоставяне на параметри или форми на API.

---

## Активатори

Активирайте този модул, когато потребителят иска да:
- Мигрира Python приложение от Azure OpenAI Chat Completions към Responses API
- Надгради използването на Python OpenAI SDK до последната форма на API към Azure OpenAI
- Подготви Python код за GPT-5 или по-нови модели, изискващи Responses на Azure
- Превключи от `AzureOpenAI`/`AsyncAzureOpenAI` към стандартния клиент `OpenAI`/`AsyncOpenAI` с v1 endpoint
- Поправи предупреждения за излизане от употреба, свързани с конструкторите на `AzureOpenAI` или `api_version`

---

## ⚠️ Съвместимост на моделите — ПРОВЕРЕТЕ ПРЕДИ

> **Преди миграцията, уверете се, че вашето Azure OpenAI разполагане поддържа Responses API.**

### 1. Бърз тест на разполагането (най-бърз)

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

> **Забележка**: `max_output_tokens` има **минимум 16** в Azure OpenAI. Стойности под 16 връщат грешка 400. За бързи тестове използвайте 50+.

Ако върне 404, моделът на разполагането все още не поддържа Responses — проверете референцията по-долу или препоставете с поддържан модел.

### 2. Проверете наличните модели във вашия регион (препоръчително)

Стартирайте вградения инструмент за съвместимост на модели, за да видите какво е налично с поддръжка на Responses API във вашия регион:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Това заявява на живо Azure ARM и показва матрица на съвместимост — кои модели поддържат Responses, структурирани изходи, инструменти и др. Използвайте `--filter gpt-5.1,gpt-5.2` за филтриране или `--json` за скриптове.

### 3. Пълна справка на поддръжката на модели

- **Жива заявка**: `python migrate.py models` (виж горе — специфично за регион, винаги актуално)
- **Преглед на наличност**: [Таблица с обобщение на моделите и регионална наличност](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Бърз старт и указания**: **https://aka.ms/openai/start**

### ⚠️ Ограничения на по-старите модели

> **ПРЕДУПРЕЖДЕНИЕ**: По-старите модели (напр. `gpt-4o`, `gpt-4`) може да не поддържат всички функции на Responses API изцяло.
>
> Познати ограничения при по-старите модели:
> - **`reasoning` параметър**: Не се поддържа при `gpt-4o-mini`, `gpt-4o` и много модели без reasoning. Мигрирайте `reasoning` само ако вече е бил наличен в оригиналния код.
> - **`seed` параметър**: Изобщо не се поддържа в Responses API — премахнете го от всички заявки.
> - **Структуриран изход чрез `text.format`**: По-старите модели може да не прилагат надеждно JSON схеми с `strict: true`.
> - **Оркестрация на инструменти**: GPT-5+ оркестрира повиквания на инструменти като част от вътрешния reasoning. По-старите модели в Responses все още работят, но липсва дълбока интеграция.
> - **Ограничения на температурата**: При миграция към `gpt-5`, температурата трябва да се пропусне или зададе на `1`. По-старите модели нямат това изискване.

### O-серия модели за reasoning (o1, o3-mini, o3, o4-mini)

Моделите от серията O имат специфични ограничения на параметрите. При миграция на приложения към o-серия:

- **`temperature`**: Трябва да е `1` (или да се пропусне). O-серията не приема други стойности.
- **`max_completion_tokens` → `max_output_tokens`**: Приложения, използващи Azure-специфичния `max_completion_tokens` трябва да преминат към `max_output_tokens`. Задайте високи стойности (4096+), тъй като reasoning токените влизат в лимита.
- **`reasoning_effort`**: Ако приложението използва `reasoning_effort` (ниско/средно/високо), запазете го — Responses API го поддържа за o-серия модели.
- **Поведение при стрийминг**: Моделите o-серия могат да буферират изхода до приключване на reasoning, преди да излъчват delta текстови събития. Стриймингът все още работи, но първият `response.output_text.delta` може да дойде с по-дълго забавяне в сравнение с GPT моделите.
- **`top_p`**: Не се поддържа при o-серия — премахнете, ако е наличен.
- **Използване на инструменти**: Моделите o-серия поддържат инструменти чрез Responses API както GPT моделите, но качеството на оркестрацията варира.

**Действие — проактивен съвет към модела**: По време на сканирането, проверете кой модел използва приложението (име на разполагане, променливи на околната среда, конфигурация). Ако моделът е `gpt-4o` или по-стар (не `gpt-4.1+`), съобщете на потребителя:
- Миграцията ще работи за основен текст, чат, стрийминг и инструменти на текущия модел.
- По-новите модели (`gpt-5.1`, `gpt-5.2`) предлагат по-добра оркестрация на инструменти, прилагане на структурирания изход, reasoning и междурегионална наличност.
- Трябва да обмислят надграждане на разполагането си, когато са готови — не блокира миграцията.

Не блокирайте или отказвайте миграция базирано на версията на модела. Съветът е информационен.

### GitHub Models НЕ поддържа Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) не поддържа Responses API.**

Ако кодовата база има път за GitHub Models (проверете за `base_url`, сочещ към `models.github.ai` или `models.inference.ai.azure.com`), **премахнете го изцяло** при миграция. Responses API изисква Azure OpenAI, OpenAI или локален съвместим endpoint (напр. Ollama с Responses поддръжка).

Действия по време на сканирането:
- Пометете всички кодови пътища за GitHub Models за премахване.

---

## Миграция на Framework

Много приложения използват по-високо ниво рамки над OpenAI. При тях мигрирайте API-то на рамката, не само вътрешните OpenAI повиквания.

### Microsoft Agent Framework (MAF)

**Проверете първо версията на MAF** — миграцията зависи дали ползвате MAF 1.0.0+ или преди 1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **вече използва Responses API** — не е нужна миграция. Ако кодовата база използва стария `OpenAIChatCompletionClient` (който използва `chat.completions.create`), заменете го с `OpenAIChatClient`.

| Преди | След |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

За да проверите версията: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF преди 1.0.0 (beta/rc издания)

В преди 1.0.0 MAF, `OpenAIChatClient` използва Chat Completions. Надградете до `agent-framework-openai>=1.0.0`, където `OpenAIChatClient` използва Responses API по подразбиране.

Други промени не са нужни — API на `Agent` и инструментите остават същите.

### LangChain (`langchain-openai`)

Добавете `use_responses_api=True` към `ChatOpenAI()`. Също така актуализирайте достъпа до отговора от `.content` на `.text`.

| Преди | След |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

За пълни примери преди/след, вижте [cheat-sheet.md](./references/cheat-sheet.md).

---

## Насоки за миграция на фронтенда

> **Responses API е въпрос на сървърна страна.** Мигрирайте Python бекенд; HTTP договора на фронтенда трябва да остане същият, освен ако бекендът не е тънък пропуск — в този случай обмислете прилагане на Responses заявките, за да премахнете преводачния слой. Ако фронтендът извършва обаждания към OpenAI директно с клиентски ключ, преместете тези повиквания първо в бекенд.

### Отписване на `@microsoft/ai-chat-protocol`

npm пакета `@microsoft/ai-chat-protocol` е остарял и трябва да се замени с [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Ако го срещнете във фронтенд:

1. Заменете CDN скрипт таг:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Премахнете инстанцирането на `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Заменете `client.getStreamedCompletion(messages)` с директно `fetch()` повикване към backend endpoint за стрийминг.
4. Заменете `for await (const response of result)` с `for await (const chunk of readNDJSONStream(response.body))`.
5. Актуализирайте достъпа до свойства от `response.delta.content` / `response.error` към `chunk.delta.content` / `chunk.error`.

---

## Цели

- Избройте всички места за повикване в Python, използващи Chat Completions или наследени Completions в Azure OpenAI.
- Предложете план и последователност на миграция за Python кодовата база.
- Направете безопасни, минимални редакции за превключване към Responses API.
- Актуализирайте повикващите за използване на схемата на Responses; без обвивки за обратно съвместимост.
- Стартирайте тестове и линове; оправете дребни счупвания от миграцията.
- Подгответе малки, прегледни комплекти с промени и дайте финално резюме с разлики (без да правите commit).

---

## Защитни мерки

- Модифицирайте само файлове в git работната област. Никога извън нея.
- Не запазвайте backward-совместими обвивки; мигрирайте към новата форма на API.
- Не оставяйте коментари за преход или резервни файлове.
- Запазете семантиката на стрийминг, ако е използвана; иначе използвайте безстрийминг.
- Изисквайте одобрение преди изпълнение на команди или мрежови повиквания при одобрителен режим.
- Не изпълнявайте `git add`/`git commit`/`git push`; правете само редакции в работната директория.

---

## Стъпка 0: Миграция на Azure OpenAI Клиент (Предварително изискване)

Ако кодовата база използва конструктори `AzureOpenAI` или `AsyncAzureOpenAI`, мигрирайте първо към стандартните `OpenAI` / `AsyncOpenAI` конструктори. Azure-специфичните конструктори са остарели в `openai>=1.108.1`.

### Защо v1 API път?

Новият `/openai/v1` endpoint използва стандартния клиент `OpenAI()` вместо `AzureOpenAI()`, не изисква параметър `api_version`, и работи еднакво в OpenAI и Azure OpenAI. Същият клиент код е защитен за бъдещето — без нужда от управление на версии.

### Ключови промени

| Преди | След |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Премахнете изцяло |

### Контролен списък за почистване

- Премахнете аргумента `api_version` от конструирането на клиента.
- Премахнете променливите на среда `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` от `.env`, настройки на приложението и Bicep/infra файлове.
- Преименувайте `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` в `.env`, настройки, Bicep/infra и тестови фикстури (стандартна конвенция на Azure Identity SDK).
- Осигурете `openai>=1.108.1` в `requirements.txt` или `pyproject.toml`.

### Миграция на променливи на средата

| Стара променлива | Действие | Бележки |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Премахнете** | Не трябва `api_version` с v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Премахнете** | Същото като горното |
| `AZURE_OPENAI_CLIENT_ID` | **Преименувайте** → `AZURE_CLIENT_ID` | Стандартна конвенция Azure Identity SDK за `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Запазете** | Все още е нужен за създаване на `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Запазете** | Използва се като параметър `model` в `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Запазете** | Използва се като `api_key` за ключова автентикация |

За примери на настройка на клиента (синхронни, асинхронни, EntraID, API ключ, мулти-тенант), вижте [cheat-sheet.md](./references/cheat-sheet.md).

---

## Стъпка 1: Откриване на наследени места за повикване

Стартирайте скрипта [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py), за да откриете всички места за повикване, нуждаещи се от миграция:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Или изпълнете тези търсения ръчно — всяко съвпадение е цел за миграция:

```bash
# Наследени извиквания на API (трябва пренаписване)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Остарели конструктори на Azure клиент (трябва замяна)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Шаблони за достъп до формата на отговорите (трябва актуализация)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Дефиниции на инструменти в стар вложен формат (трябва изравняване)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Резултати от инструменти в стар формат (трябва преобразуване към function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Остарели параметри (трябва премахване или преименуване)
rg "response_format"
rg "max_tokens\b"        # преименуване на max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Остарели променливи на средата (почистване)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # трябва да бъде AZURE_CLIENT_ID

# Крайни точки на GitHub Models (трябва премахване — Responses API не се поддържа)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Наследени шаблони на ниво фреймуърк (трябва актуализация)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: замяна с OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: изисква use_responses_api=True

# Тестова инфраструктура (трябва актуализация)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Достъп до тяло на грешка на филтър на съдържание (трябва актуализация — структурата е променена)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # стар единствен брой — сега content_filter_results (множествено число) в масива content_filters

# Сурови HTTP извиквания към Chat Completions крайна точка (трябва актуализация на URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Евристики (откриване и пре-писване)

- **Chat Completions клиент**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Конструктори на Azure клиент**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Инструменти**: конвертирайте определенията за повикване на функции от вложен формат (`{"type": "function", "function": {"name": ...}}`) към плосък формат Responses (`{"type": "function", "name": ...}`); използвайте `tool_choice`; връщайте резултатите от инструмента като елементи `{"type": "function_call_output", "call_id": ..., "output": ...}` (не като `{"role": "tool", ...}`).
- **Кръгови повиквания на инструменти**: когато моделът връща повиквания на функции, добавете елементи `response.output` към разговора (не ръчно речник `{"role": "assistant", "tool_calls": [...]}`), след това добавете елементи `function_call_output` за всеки резултат.
- **Примери за няколко повиквания на инструменти**: ако разговорът съдържа предварително зададени примери за повикване на инструменти, конвертирайте ги в елементи `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Идентификаторите трябва да започват с `fc_`.
- **`pydantic_function_tool()`**: този помощник все още генерира стария вложен формат и НЕ Е съвместим с `responses.create()`. Заменете го с ръчни дефиниции на инструменти или обвивка за оплескване.
- **Многоходови взаимодействия**: запазвайте историята на разговора в приложението; подавайте предишните ходове чрез `input` елементи.
- **Форматиране**: заменете на високо ниво `response_format` на Chat с `text.format` в Responses. Канонична форма: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Елементи за съдържание**: заменете Chat `content[].type: "text"` с Responses `content[].type: "input_text"` за ходове на потребителя/системата.
- **Елементи за изображение**: заменете Chat `content[].type: "image_url"` с Responses `content[].type: "input_image"`. Полето `image_url` се променя от вложен обект `{"url": "..."}` в плосък низ. Вижте листа с бързи справки за примери преди и след.
- **Усилия за разсъждения**: **мигрирайте `reasoning` само ако вече съществува в оригиналния код**.
- **Обработка на грешки при филтър за съдържание**: структурата на тялото на грешката се промени. Chat Completions използваше `error.body["innererror"]["content_filter_result"]` (единствено число); Responses API използва `error.body["content_filters"][0]["content_filter_results"]` (множествено число, в масив). Кодът, който достъпва `innererror`, ще предизвика `KeyError`. Пренапишете, за да използва новия път.
- **Сурови HTTP повиквания**: ако приложението директно извиква Azure OpenAI REST API (чрез `requests`, `httpx` и т.н.) с `/openai/deployments/{name}/chat/completions?api-version=...`, пренапишете го на `/openai/v1/responses`. Тялото на заявката се променя: `messages` → `input`, добавете `max_output_tokens` и `store: false`, премахнете query параметъра `api-version`. Тялото на отговора се променя: `choices[0].message.content` → `output[0].content[0].text` (забележка: `output_text` е удобна собственост на SDK, която не съществува в суровия REST JSON).

---

## Стъпка 2: Приложете миграцията

### Бележки за миграцията (Chat Completions → Responses)

- **Защо да мигрираме**: Responses е унифицирано API за текст, инструменти и стрийминг; Chat Completions е остарял. С GPT-5 Responses е задължително за оптимална производителност.
- **HTTP**: Azure крайна точка се променя от `/openai/deployments/{name}/chat/completions` към `/openai/v1/responses`.
- **Поля**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` остава същото.
- **Форматиране**: `response_format` → `text.format` с правилен обект.
- **Елементи за съдържание**: Заменете Chat `content[].type: "text"` с Responses `content[].type: "input_text"` за ходове на системата/потребителя.
- **Елементи за изображение**: Заменете Chat `content[].type: "image_url"` с Responses `content[].type: "input_image"`. Превърнете полето `image_url` от `{"image_url": {"url": "..."}}` в `{"image_url": "..."}` (обикновен низ — HTTPS URL или `data:image/...;base64,...` data URI).

### Референция за съответствие на параметрите

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
| `tools` / повикване на функции | `tools` (непроменено) |
| `seed` | **Премахнете** (неподдържано) |
| `store` | `store` (зададено на `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (плосък низ) |

За пълни примери преди/след, вижте [cheat-sheet.md](./references/cheat-sheet.md).

За миграция на тестова инфраструктура (мокове, снимки, проверки), вижте [test-migration.md](./references/test-migration.md).

За отстраняване на грешки и проблеми, вижте [troubleshooting.md](./references/troubleshooting.md).

---

## Запазване на данни и състояние

- Задайте `store: false` на всички заявки към Responses.
- Не разчитайте на предишни ID на съобщения или контекст, запазен на сървъра; поддържайте състоянието управлявано от клиента и минимизирайте метаданните.

---

## Критерии за приемане

### Gate-ове на ниво код (всички трябва да преминат)

- [ ] Няма съвпадения за `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` в мигрираните файлове.
- [ ] Няма съвпадения за `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — всички конструктори използват `OpenAI`/`AsyncOpenAI` с v1 endpoint.
- [ ] Няма съвпадения за `rg "models\.github\.ai|models\.inference\.ai\.azure"` — премахнати са пътища за GitHub модели.
- [ ] Няма съвпадения за `rg "OpenAIChatCompletionClient"` — кодът в MAF 1.0.0+ използва `OpenAIChatClient` (който използва Responses API). В версии преди 1.0.0 обновете до `agent-framework-openai>=1.0.0`.
- [ ] Всички повиквания `ChatOpenAI(...)` съдържат параметър `use_responses_api=True`.
- [ ] Няма съвпадения за `rg "choices\[0\]"` — достъп до отговорите се извършва чрез `resp.output_text` или Responses изходната схема.
- [ ] Няма `response_format` на най-високо ниво; цялата структурирана продукция използва `text={"format": {...}}`.
- [ ] В `requirements.txt` или `pyproject.toml` са зададени `openai>=1.108.1` и `azure-identity`; зависимостите са преинсталирани.
- [ ] На всяко повикване `responses.create` е зададен `store=False`.
- [ ] Няма `api_version` при конструиране на клиента; `AZURE_OPENAI_API_VERSION` е премахнат от файлове с променливи на средата и инфраструктура.

### Gate-ове за тестова инфраструктура (всички трябва да преминат)

- [ ] Няма съвпадения за `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Няма съвпадения за `rg "_azure_ad_token_provider" tests/` — проверките са обновени да проверяват `isinstance(client, AsyncOpenAI)` или `base_url`.
- [ ] Няма съвпадения за `rg "prompt_filter_results|content_filter_results" tests/` — премахнати са мокове, специфични за Azure филтри.
- [ ] Мок фикстурите използват `kwargs.get("input")` вместо `kwargs.get("messages")`.
- [ ] Снимковите файлове / златните файлове са обновени към стрийминг формата на Responses (няма `choices[0]`, `function_call`, `logprobs` и др.).
- [ ] `pytest` успешно преминава без грешки след всички обновления по тестовете.

### Поведенчески gate-ове (проверяват се ръчно или чрез тестови рамки)

- [ ] **Основно завършване**: нестрийминг `responses.create` връща непразен `output_text`.
- [ ] **Паралелност на стрийминга**: ако оригиналният код е използвал стрийминг, мигрираният код стриймва и произвежда събития `response.output_text.delta` с непразни делти.
- [ ] **Структуриран изход**: ако се използва `text.format` с `json_schema`, `json.loads(resp.output_text)` е успешен и съвпада със схемата.
- [ ] **Цикъл на повикване на инструменти**: ако се използват инструменти, моделът извършва повиквания, приложението ги изпълнява, а последващата заявка връща финален `output_text` (няма безкраен цикъл).
- [ ] **Паралелност при асинхронност**: ако е използван `AsyncAzureOpenAI`, съответният `AsyncOpenAI` работи с „await“.
- [ ] **Процент грешки**: няма нови грешки 400/401/404 в сравнение с базовото състояние преди миграцията.

### Резултати

- Обобщение включва редактирани файлове, брой повиквания преди и след миграцията и следващи стъпки.
- Промените са само в работната директория (без комити).

---

## Изисквания към версиите на SDK

| Пакет | Минимална версия |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Най-нова (за EntraID автентикация) |

---

## Препратки

- [Лист с примери — всички кодови откъси](./references/cheat-sheet.md)
- [Миграция на тестове — мокове, снимки, проверки](./references/test-migration.md)
- [Отстраняване на грешки — грешки, таблица на рисковете, проблеми](./references/troubleshooting.md)
- [detect_legacy.py — автоматизиран скенер](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Стартов комплект](https://aka.ms/openai/start)
- [Документация за Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Живот на версията на Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Референция за OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->