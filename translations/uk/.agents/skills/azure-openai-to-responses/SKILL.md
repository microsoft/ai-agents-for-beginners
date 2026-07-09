---
name: azure-openai-to-responses
license: MIT
---
# Міграція Python-додатків з Azure OpenAI Chat Completions на Responses API

> **АВТОРИТЕТНІ ВКАЗІВКИ — ДОТРИМУЙТЕСЯ ДОКЛАДНО**
>
> Цей навик мігрує Python-код із використання Azure OpenAI Chat Completions
> до уніфікованого Responses API. Дотримуйтесь цих інструкцій точно.
> Не імпровізуйте відображення параметрів і не вигадуйте структури API.

---

## Тригери

Активуйте цей навик, коли користувач хоче:
- Мігрувати Python-додаток з Azure OpenAI Chat Completions на Responses API
- Оновити використання Python OpenAI SDK до останньої версії API для Azure OpenAI
- Підготувати Python-код для GPT-5 або новіших моделей, які потребують Responses на Azure
- Перейти з `AzureOpenAI`/`AsyncAzureOpenAI` на стандартний клієнт `OpenAI`/`AsyncOpenAI` з вендпоінтом v1
- Виправити попередження про застарілість, пов’язані з конструкторами `AzureOpenAI` чи `api_version`

---

## ⚠️ Сумісність моделі — ПЕРЕВІРТЕ ПЕРШЕ

> **Перед міграцією перевірте, що ваша розгортка Azure OpenAI підтримує Responses API.**

### 1. Швидкий тест розгортки (найшвидший)

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

> **Примітка**: `max_output_tokens` має **мінімум 16** в Azure OpenAI. Значення менше за 16 повернуть помилку 400. Для швидких тестів використовуйте 50 і більше.

Якщо повертає 404, модель розгортки ще не підтримує Responses — перевірте довідку нижче або повторно розгорніть із підтримуваною моделлю.

### 2. Перевірка доступних моделей у вашому регіоні (рекомендовано)

Запустіть вбудований інструмент перевірки сумісності моделей, щоб побачити, що доступно з підтримкою Responses API у вашому регіоні:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Цей запит до Azure ARM у режимі реального часу показує матрицю сумісності — які моделі підтримують Responses, структурований вивід, інструменти тощо. Використовуйте `--filter gpt-5.1,gpt-5.2` для звуження результатів або `--json` для скриптування.

### 3. Повний довідник по підтримці моделей

- **Живий запит**: `python migrate.py models` (див. вище — регіонально специфічно, завжди актуально)
- **Переглянути доступність**: [Таблиця моделей та доступність по регіонах](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Швидкий старт та керівництво**: **https://aka.ms/openai/start**

### ⚠️ Обмеження старіших моделей

> **УВАГА**: Старіші моделі (наприклад, `gpt-4o`, `gpt-4`) можуть не повністю підтримувати всі функції Responses API.
>
> Відомі обмеження старих моделей:
> - **Параметр `reasoning`**: не підтримується у `gpt-4o-mini`, `gpt-4o` та багатьох моделях без reasoning. Мігруйте `reasoning` лише якщо він був у вихідному коді.
> - **Параметр `seed`**: не підтримується в Responses API взагалі — видаліть з усіх запитів.
> - **Структурований вивід через `text.format`**: Старі моделі можуть ненадійно застосовувати схеми JSON з `strict: true`.
> - **Оркестрація інструментів**: GPT-5+ оркеструє виклики інструментів як частину внутрішнього reasoning. Старі моделі у Responses працюють, але без глибокої інтеграції.
> - **Обмеження температури**: При міграції на `gpt-5` температуру потрібно пропустити або встановити у `1`. Старі моделі таких обмежень не мають.

### Reasoning-моделі серії O (o1, o3-mini, o3, o4-mini)

Моделі серії O мають унікальні обмеження параметрів. При міграції додатків, орієнтованих на O-серію:

- **`temperature`**: має бути `1` (або пропущено). Моделі O-серії не приймають інших значень.
- **`max_completion_tokens` → `max_output_tokens`**: Додатки, що використовують специфічний для Azure `max_completion_tokens`, повинні перейти на `max_output_tokens`. Встановіть високі значення (4096+), бо токени reasoning входять у ліміт.
- **`reasoning_effort`**: Якщо додаток використовує `reasoning_effort` (low/medium/high), залиште цей параметр — Responses API підтримує його для моделей O-серії.
- **Поведінка стрімінгу**: Моделі O-серії можуть накопичувати вивід до завершення reasoning перед відправкою текстових дельта-подій. Стрімінг працює, але перший `response.output_text.delta` може надходити із більшою затримкою, ніж у GPT-моделей.
- **`top_p`**: Не підтримується в O-серії — видаліть, якщо він є.
- **Використання інструментів**: Моделі O-серії підтримують інструменти через Responses API так само, як GPT-моделі, але якість оркестрації викликів залежить від моделі.

**Дія — проактивне консультування щодо моделі**: Під час сканування перевірте, на яку модель орієнтований додаток (назви розгорток, змінні оточення, конфігурації). Якщо модель — `gpt-4o` або старіша (не gpt-4.1+), попередьте користувача:
- Міграція працюватиме для базового тексту, чату, стрімінгу та інструментів на їхній поточній моделі.
- Новіші моделі (`gpt-5.1`, `gpt-5.2`) пропонують кращу оркестрацію інструментів, застосування структурованого виводу, reasoning і крос-регіональну доступність.
- Вони мають розглянути оновлення розгортки, коли будуть готові — це не блокує міграцію.

Не блокуйте і не відмовляйтеся від міграції через версію моделі. Це інформаційне повідомлення.

### GitHub Models не підтримують Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) не підтримують Responses API.**

Якщо в базі коду є шлях для GitHub Models (перевірте `base_url`, що вказує на `models.github.ai` або `models.inference.ai.azure.com`), **повністю видаліть його** під час міграції. Responses API потребує Azure OpenAI, OpenAI або сумісний локальний вендпоінт (наприклад, Ollama з підтримкою Responses).

Дія під час сканування:
- Позначте всі GitHub Models шляхи для видалення.

---

## Міграція фреймворку

Багато додатків використовують вищі за рівнем фреймворки поверх OpenAI. При міграції таких слід змінити API самого фреймворку — а не лише базові виклики OpenAI.

### Microsoft Agent Framework (MAF)

**Спочатку перевірте версію MAF** — міграція залежить від того, чи у вас MAF 1.0.0+ чи передрелізні версії beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **вже використовує Responses API** — міграція не потрібна. Якщо код використовує застарілий `OpenAIChatCompletionClient` (що викликає `chat.completions.create`), замініть його на `OpenAIChatClient`.

| До       | Після          |
|---------|----------------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Щоб перевірити версію: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"` 

#### MAF до 1.0.0 (beta/rc релізи)

У MAF до 1.0.0 `OpenAIChatClient` використовував Chat Completions. Оновіться до `agent-framework-openai>=1.0.0`, де `OpenAIChatClient` за замовчуванням використовує Responses API.

Інші зміни не потрібні — API `Agent` та інструментів залишаються незмінними.

### LangChain (`langchain-openai`)

Додайте `use_responses_api=True` до `ChatOpenAI()`. Також оновіть доступ до відповіді з `.content` на `.text`.

| До                                                  | Після                                                     |
|-----------------------------------------------------|-----------------------------------------------------------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)`   | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content`                      | `result['messages'][-1].text`                              |

Для повних прикладів до/після див. у [cheat-sheet.md](./references/cheat-sheet.md).

---

## Керівництво з міграції фронтенду

> **Responses API — це серверна справа.** Міграція вашого Python-бекенду; HTTP-Контракт фронтенду має залишатися без змін, якщо тільки бекенд не є тонким транзитним шаром — в такому разі розгляньте можливість прийняття форми запитів Responses для усунення шару трансляції. Якщо фронтенд викликає OpenAI напряму з ключем з клієнта, перемістіть ці виклики на бекенд.

### Застарілість `@microsoft/ai-chat-protocol`

npm-пакет `@microsoft/ai-chat-protocol` застарілий і має бути замінений на [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Якщо він трапляється у фронтенді:

1. Замініть тег сценарію CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Видаліть ініціалізацію `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Замініть `client.getStreamedCompletion(messages)` на прямий виклик `fetch()` до бекендового streaming endpoint.
4. Замініть `for await (const response of result)` на `for await (const chunk of readNDJSONStream(response.body))`.
5. Оновіть доступ до властивостей з `response.delta.content` / `response.error` на `chunk.delta.content` / `chunk.error`.

---

## Цілі

- Перерахувати всі виклики Python, що використовують Chat Completions або застарілі Completions проти Azure OpenAI.
- Запропонувати план міграції і послідовність для Python-коду.
- Застосувати безпечні, мінімальні зміни для переходу на Responses API.
- Оновити виклики для роботи з Responses шемою виводу; без обгорток з підтримкою сумісності.
- Запустити тести/лінти; виправити тривіальні порушення, що з’явилися після міграції.
- Підготувати малі набори змін, придатні для рев’ю, і надати остаточне резюме з дельтами (не комітити).

---

## Обмеження

- Модифікуйте лише файли в git-репозиторії. Не записуйте поза його межами.
- Не зберігайте shim-и з сумісністю назад; мігруйте код на нову форму API.
- Не залишайте коментарі транзиту чи резервні копії файлів.
- Зберігайте семантику стрімінгу, якщо раніше використовувалась; інакше використовуй нестрімінговий режим.
- У схвалювальному режимі запитуйте дозвіл перед виконанням команд чи мережевих викликів.
- Не виконувати `git add`/`git commit`/`git push`; лише редагування робочої області.

---

## Крок 0: Міграція Azure OpenAI Клиєнта (попередня умова)

Якщо код використовує конструктори `AzureOpenAI` або `AsyncAzureOpenAI`, спочатку мігруйте на стандартні конструктори `OpenAI` / `AsyncOpenAI`. Специфічні для Azure конструктори застаріли у `openai>=1.108.1`.

### Чому шлях API v1?

Новий endpoint `/openai/v1` використовує стандартний клієнт `OpenAI()`, замість `AzureOpenAI()`, не потребує параметра `api_version` і працює однаково для OpenAI та Azure OpenAI. Той самий код клієнта є майбутньо-орієнтованим — не потрібно керувати версіями.

### Основні зміни

| До            | Після        |
|---------------|--------------|
| `AzureOpenAI`  | `OpenAI`     |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url`    |
| `azure_ad_token_provider` | `api_key`   |
| `api_version=...` | Видалити повністю |

### Чеклист очищення

- Видаліть аргумент `api_version` з конструктора клієнта.
- Видаліть змінні оточення `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` з `.env`, налаштувань додатку, Bicep/інфраструктурних файлів.
- Перейменуйте `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` у `.env`, налаштуваннях додатку, Bicep/інфраструктурних файлах і тестових фікстурах (стандартна конвенція Azure Identity SDK).
- Забезпечте `openai>=1.108.1` у `requirements.txt` або `pyproject.toml`.

### Міграція змінних оточення

| Старий env var           | Дія              | Примітки |
|-------------------------|------------------|----------|
| `AZURE_OPENAI_VERSION`   | **Видалити**     | Не потрібен `api_version` з v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Видалити**   | Те саме, що вище |
| `AZURE_OPENAI_CLIENT_ID` | **Перейменувати** → `AZURE_CLIENT_ID` | Стандартна конвенція Azure Identity SDK для `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT`  | **Залишити**     | Потрібен для побудови `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Залишити** | Використовується як параметр `model` в `responses.create` |
| `AZURE_OPENAI_API_KEY`   | **Залишити**     | Використовується як `api_key` для автентифікації за ключем |

Приклади коду налаштування клієнта (синхронний, асинхронний, EntraID, ключ API, мульти-орендність) див. у [cheat-sheet.md](./references/cheat-sheet.md).

---

## Крок 1: Виявлення Застарілих Викликів

Запустіть скрипт [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py), щоб знайти всі виклики, які потребують міграції:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Або виконайте такі пошуки вручну — кожен збіг є метою міграції:

```bash
# Успадковані виклики API (потрібно переписати)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Застарілі конструктори клієнтів Azure (потрібно замінити)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Шаблони доступу до форми відповіді (потрібно оновити)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Визначення інструментів у старому вкладеному форматі (потрібно спростити)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Результати інструментів у старому форматі (потрібно конвертувати у function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Застарілі параметри (потрібно видалити або перейменувати)
rg "response_format"
rg "max_tokens\b"        # перейменувати на max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Застарілі змінні середовища (потрібно очистити)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # має бути AZURE_CLIENT_ID

# Кінцеві точки моделей GitHub (потрібно видалити — API відповідей не підтримується)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Успадковані шаблони рівня фреймворку (потрібно оновити)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: замінити на OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: потрібно use_responses_api=True

# Тестова інфраструктура (потрібно оновити)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Доступ до тіла помилки фільтра вмісту (потрібно оновити — структура змінилася)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # старий одниний формат — тепер content_filter_results (множина) у масиві content_filters

# Сирі HTTP виклики до кінцевої точки Chat Completions (потрібно оновити URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Гевристики (виявлення і переписування)

- **Клієнт Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Конструктори клієнта Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Інструменти**: конвертуйте визначення функціональних інструментів із вкладеного формату (`{"type": "function", "function": {"name": ...}}`) у плоский формат Responses (`{"type": "function", "name": ...}`); використовуйте `tool_choice`; повертайте результати роботи інструментів як елементи `{"type": "function_call_output", "call_id": ..., "output": ...}` (не `{"role": "tool", ...}`).
- **Обробка викликів інструментів**: коли модель повертає виклики функцій, додайте елементи `response.output` до розмови (не вручну словник `{"role": "assistant", "tool_calls": [...]}`), потім додайте елементи `function_call_output` для кожного результату.
- **Приклади викликів інструментів з кількома прикладами**: якщо в розмові є жорстко задані приклади викликів інструментів, перетворіть їх в елементи `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Ідентифікатори повинні починатися з `fc_`.
- **`pydantic_function_tool()`**: цей помічник досі генерує старий вкладений формат і **несумісний** з `responses.create()`. Замініть на ручні визначення інструментів або обгортку для випрямлення.
- **Багатоетапне спілкування**: підтримуйте історію розмови в додатку; передавайте попередні повідомлення через `input` елементи.
- **Форматування**: замініть верхньорівневий `response_format` у Chat на `text.format` у Responses. Канонічна структура: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Елементи вмісту**: замініть у Chat `content[].type: "text"` на `content[].type: "input_text"` у Responses для ходів користувача/системи.
- **Елементи зображень у вмісті**: замініть у Chat `content[].type: "image_url"` на `content[].type: "input_image"` у Responses. Поле `image_url` змінюється з вкладеного об'єкта `{"url": "..."}` на плоский рядок. Див. шпаргалку для прикладів до/після.
- **Зусилля на логіку**: **мігруйте `reasoning` лише якщо воно є в оригінальному коді**.
- **Обробка помилок фільтрації вмісту**: змінилася структура тіла помилки. Chat Completions використовував `error.body["innererror"]["content_filter_result"]` (однина); Responses API використовує `error.body["content_filters"][0]["content_filter_results"]` (множина, всередині масиву). Код, який звертається до `innererror`, викличе `KeyError`. Перепишіть, щоб використовувати новий шлях.
- **Прямі HTTP виклики**: якщо додаток безпосередньо викликає Azure OpenAI REST API (через `requests`, `httpx` тощо) з `/openai/deployments/{name}/chat/completions?api-version=...`, перепишіть на `/openai/v1/responses`. Зміни у тілі запиту: `messages` → `input`, додаються `max_output_tokens` і `store: false`, видаляється параметр `api-version` у запиті. Зміни у відповіді: `choices[0].message.content` → `output[0].content[0].text` (увага: `output_text` — це зручна властивість SDK, якої немає у сирому REST JSON).

---

## Крок 2: Застосування міграції

### Примітки щодо міграції (Chat Completions → Responses)

- **Чому мігрувати**: Responses — це єдиний API для тексту, інструментів і стрімінгу; Chat Completions — застарілий. З GPT-5 Responses потрібен для найкращої продуктивності.
- **HTTP**: Azure перейшов від `/openai/deployments/{name}/chat/completions` до `/openai/v1/responses`.
- **Поля**: `messages` → `input`, `max_tokens` → `max_output_tokens`. Параметр `temperature` залишився без змін.
- **Форматування**: `response_format` → `text.format` з об’єктом.
- **Елементи вмісту**: замініть у Chat `content[].type: "text"` на Responses `content[].type: "input_text"` для ходів системи/користувача.
- **Елементи зображень у вмісті**: замініть у Chat `content[].type: "image_url"` на Responses `content[].type: "input_image"`. Сплющіть поле `image_url` із `{"image_url": {"url": "..."}}` у `{"image_url": "..."}` (звичайний рядок — HTTPS URL або data URI у форматі `data:image/...;base64,...`).

### Довідник відображення параметрів

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (масив елементів) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (об’єкт) |
| `temperature` | `temperature` (без змін) |
| `stop` | `stop` (без змін) |
| `frequency_penalty` | `frequency_penalty` (без змін) |
| `presence_penalty` | `presence_penalty` (без змін) |
| `tools` / виклики функцій | `tools` (без змін) |
| `seed` | **Видалити** (не підтримується) |
| `store` | `store` (встановити у `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (плоский рядок) |

Для повних прикладів коду до/після див. [cheat-sheet.md](./references/cheat-sheet.md).

Для міграції тестової інфраструктури (моки, снепшоти, асерти) див. [test-migration.md](./references/test-migration.md).

Для усунення помилок і частої проблематики див. [troubleshooting.md](./references/troubleshooting.md).

---

## Збереження даних та стану

- Встановіть `store: false` у всіх запитах Responses.
- Не покладайтеся на ідентифікатори попередніх повідомлень або контекст, збережений на сервері; тримайте стан під керуванням клієнта та мінімізуйте метадані.

---

## Критерії приймання

### Контрольні точки на рівні коду (усі повинні бути виконані)

- [ ] Немає збігів для `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` у мігрованих файлах.
- [ ] Немає збігів для `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — всі конструктори використовують `OpenAI`/`AsyncOpenAI` з версією v1 endpoint.
- [ ] Немає збігів для `rg "models\.github\.ai|models\.inference\.ai\.azure"` — видалено шляхи коду GitHub Models.
- [ ] Немає збігів для `rg "OpenAIChatCompletionClient"` — код MAF 1.0.0+ використовує `OpenAIChatClient` (який використовує Responses API). Для версій до 1.0.0 оновіть до `agent-framework-openai>=1.0.0`.
- [ ] Всі виклики `ChatOpenAI(...)` включають `use_responses_api=True`.
- [ ] Немає збігів для `rg "choices\[0\]"` — увесь доступ до відповідей використовує `resp.output_text` або схему виходу Responses.
- [ ] Відсутній `response_format` на верхньому рівні; увесь структурований вихід використовує `text={"format": {...}}`.
- [ ] У `requirements.txt` або `pyproject.toml` є `openai>=1.108.1` і `azure-identity`; залежності перевстановлені.
- [ ] На кожному виклику `responses.create` встановлено `store=False`.
- [ ] Відсутній `api_version` у конструкції клієнта; змінна середовища `AZURE_OPENAI_API_VERSION` видалена з файлів і інфраструктури.

### Контрольні точки тестової інфраструктури (усі повинні бути виконані)

- [ ] Немає збігів для `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Немає збігів для `rg "_azure_ad_token_provider" tests/` — асерти оновлено для перевірки `isinstance(client, AsyncOpenAI)` або `base_url`.
- [ ] Немає збігів для `rg "prompt_filter_results|content_filter_results" tests/` — видалено Azure-специфічні мокі фільтру.
- [ ] Мок-фикстури використовують `kwargs.get("input")`, а не `kwargs.get("messages")`.
- [ ] Снепшоти / golden файли оновлено до формату Responses для стрімінгу (без `choices[0]`, `function_call`, `logprobs` і т. д.).
- [ ] `pytest` проходить без помилок після оновлення тестів.

### Поведінкові критерії (перевірити вручну або через тестовий стенд)

- [ ] **Базове завершення**: нешвидкісний виклик `responses.create` повертає непорожній `output_text`.
- [ ] **Паритет стрімінгу**: якщо в оригінальному коді використовувався стрімінг, мігрований код стрімить і видає події `response.output_text.delta` з непорожніми дельтами.
- [ ] **Структурований вихід**: при використанні `text.format` з `json_schema`, `json.loads(resp.output_text)` успішний і відповідає схемі.
- [ ] **Цикл виклику інструментів**: якщо використовують інструменти, модель видає виклики інструментів, додаток їх виконує, а наступний запит повертає остаточний `output_text` (без нескінченного циклу).
- [ ] **Паритет асинхронності**: якщо використовувався `AsyncAzureOpenAI`, еквівалент `AsyncOpenAI` працює з `await`.
- [ ] **Рівень помилок**: відсутність нових помилок 400/401/404 порівняно з базовою лінією перед міграцією.

### Остаточні результати

- Резюме містить відредаговані файли, кількість викликів застарілого API до/після, та наступні кроки.
- Зміни залишаються у робочому каталозі (без комітів).

---

## Вимоги до версій SDK

| Пакет | Мінімальна версія |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Остання (для аутентифікації EntraID) |

---

## Посилання

- [Шпаргалка — усі приклади коду](./references/cheat-sheet.md)
- [Міграція тестів — моки, снепшоти, асерти](./references/test-migration.md)
- [Вирішення проблем — помилки, таблиця ризиків, хитрощі](./references/troubleshooting.md)
- [detect_legacy.py — автоматизований сканер](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Starter Kit для Azure OpenAI](https://aka.ms/openai/start)
- [Документація Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Життєвий цикл версії Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->