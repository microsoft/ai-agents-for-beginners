---
name: azure-openai-to-responses
license: MIT
---
# Міграція Python-додатків із Azure OpenAI Chat Completions на Responses API

> **АВТОРИТЕТНА ІНСТРУКЦІЯ — ВИКОНУВАТИ ТОЧНО**
>
> Ця навичка переносить Python-код, що використовує Azure OpenAI Chat Completions,
> на уніфікований Responses API. Дотримуйтесь цих інструкцій точно.
> Не імпровізуйте параметри або не вигадуйте форми API.

---

## Тригери

Активуйте цю навичку, коли користувач хоче:
- Перенести Python-додаток з Azure OpenAI Chat Completions на Responses API
- Оновити використання Python OpenAI SDK до нової форми API для Azure OpenAI
- Підготувати Python-код для GPT-5 або новіших моделей, які потребують Responses на Azure
- Перейти від `AzureOpenAI`/`AsyncAzureOpenAI` до стандартного клієнта `OpenAI`/`AsyncOpenAI` з кінцевою точкою v1
- Виправити попередження про застарілість, пов’язані з конструкторами `AzureOpenAI` або параметром `api_version`

---

## ⚠️ Сумісність моделей — ПЕРЕВІРТЕ СПЕРЕДУ

> **Перед міграцією переконайтесь, що ваше розгортання Azure OpenAI підтримує Responses API.**

### 1. Швидкий тест розгортання (найшвидший)

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

> **Примітка**: `max_output_tokens` має **мінімум 16** в Azure OpenAI. Значення нижче 16 повертає помилку 400. Використовуйте 50+ для швидких тестів.

Якщо повертає 404, модель розгортання ще не підтримує Responses — перевірте посилання нижче або переналаштуйте з підтримуваною моделлю.

### 2. Перевірте доступні моделі у вашому регіоні (рекомендовано)

Запустіть вбудований інструмент перевірки сумісності моделей, щоб дізнатись, які моделі з підтримкою Responses API доступні у вашому регіоні:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Запитує Azure ARM у живому режимі та показує матрицю сумісності — які моделі підтримують Responses, структурований вивід, інструменти тощо. Використовуйте `--filter gpt-5.1,gpt-5.2` для фільтрації або `--json` для скриптування.

### 3. Повний довідник підтримки моделей

- **Живий запит**: `python migrate.py models` (див. вище — специфічно для регіону, завжди оновлено)
- **Перегляд доступності**: [Таблиця моделей і доступність за регіонами](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Швидкий старт і настанови**: **https://aka.ms/openai/start**

### ⚠️ Обмеження старіших моделей

> **УВАГА**: Старіші моделі (які передують `gpt-4.1`) можуть не повністю підтримувати всі функції Responses API.
>
> Відомі обмеження старіших моделей:
> - **Параметр `reasoning`**: Не підтримується багатьма не-розумовими моделями. Мігрируйте `reasoning` лише якщо він уже був у початковому коді.
> - **Параметр `seed`**: В Responses API взагалі не підтримується — видаліть з усіх запитів.
> - **Структурований вихід через `text.format`**: Старіші моделі можуть ненадійно підтримувати `strict: true` JSON-схеми.
> - **Оркестрація інструментів**: GPT-5+ керує викликами інструментів у ході внутрішнього логічного процесу. Старіші моделі у Responses працюють, але без глибокої інтеграції.
> - **Обмеження температури**: При переході до `gpt-5` температуру треба пропускати або ставити `1`. Старіші моделі такого обмеження не мають.

### Моделі серії O (o1, o3-mini, o3, o4-mini)

Моделі серії O мають унікальні обмеження параметрів. Під час міграції додатків, що цільовані на серію O:

- **`temperature`**: Має бути `1` (або пропущено). Моделі серії O не приймають інших значень.
- **`max_completion_tokens` → `max_output_tokens`**: Додатки, що використовують специфічний для Azure параметр `max_completion_tokens`, мають перейти на `max_output_tokens`. Встановіть великі значення (4096+), оскільки токени reasoning зараховуються у ліміт.
- **`reasoning_effort`**: Якщо у додатку використовується `reasoning_effort` (low/medium/high), залишайте його — Responses API підтримує цей параметр для моделей серії O.
- **Повідінка стрімінгу**: Моделі серії O можуть накопичувати вихід, доки reasoning не завершиться, перш ніж видавати текстові дельти. Стрімінг працює, але перша `response.output_text.delta` може прийти з більшою затримкою, ніж у GPT-моделей.
- **`top_p`**: Не підтримується на серії O — видаліть якщо є.
- **Використання інструментів**: Моделі серії O підтримують інструменти через Responses API так само, як і GPT, але якість оркестрації викликів інструментів залежить від моделі.

**Дія — проактивна порада щодо моделей**: Під час сканування перевірте, яка модель цільована у додатку (імена розгортань, змінні оточення, конфіг). Якщо модель передує `gpt-4.1` (не gpt-4.1+), проінформуйте користувача:
- Міграція працюватиме для основного тексту, чату, стрімінгу та інструментів на їхній поточній моделі.
- Новіші моделі (`gpt-5.1`, `gpt-5.2`) пропонують кращу оркестрацію інструментів, жорсткіші правила для структурованого виводу, reasoning і доступність у різних регіонах.
- Варто розглянути оновлення розгортання, коли буде готовність — це не блокуватиме міграцію.

Не блокувати і не відмовляти в міграції через версію моделі. Порада лише інформаційна.

### Моделі GitHub НЕ підтримують Responses API

> **Моделі GitHub (`models.github.ai`, `models.inference.ai.azure.com`) не підтримують Responses API.**

Якщо у коді є шлях для моделей GitHub (шукайте `base_url` із посиланням на `models.github.ai` або `models.inference.ai.azure.com`), **видаліть його повністю** під час міграції. Responses API вимагає Azure OpenAI, OpenAI або сумісну локальну точку (наприклад, Ollama з підтримкою Responses).

Дія під час сканування:
- Позначати всі шляхи моделей GitHub для видалення.

---

## Міграція фреймворку

Багато додатків використовують високорівневі фреймворки поверх OpenAI. При міграції їх змінюється API самого фреймворку, не лише виклики OpenAI.

### Microsoft Agent Framework (MAF)

**Спочатку перевірте вашу версію MAF** — міграція залежить від того, чи у вас MAF 1.0.0+ або попередня бета/rc версія.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **вже використовує Responses API** — міграція не потрібна. Якщо код використовує застарілий `OpenAIChatCompletionClient` (який викликає `chat.completions.create`), замініть його на `OpenAIChatClient`.

| До | Після |
|----|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Щоб перевірити версію: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF до 1.0.0 (бета/rc релізи)

У MAF до 1.0.0 `OpenAIChatClient` використовував Chat Completions. Оновіться до `agent-framework-openai>=1.0.0`, де `OpenAIChatClient` за замовчуванням використовує Responses API.

Інших змін не потрібно — API `Agent` та інструментів залишаються без змін.

### LangChain (`langchain-openai`)

Додайте `use_responses_api=True` у `ChatOpenAI()`. Також оновіть доступ до відповіді з `.content` на `.text`.

| До | Після |
|----|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Для повних прикладів до/після дивіться [cheat-sheet.md](./references/cheat-sheet.md).

---

## Настанови з міграції фронтенду

> **Responses API — це питання серверного боку.** Міґруйте ваш бекенд на Python; HTTP контракти фронтенду повинні залишатися незмінними, якщо бекенд не є тонким посередником — у такому випадку розгляньте впровадження форми запиту Responses для усунення проміжного шару. Якщо фронтенд викликає OpenAI безпосередньо із клієнтським ключем, перемістіть ці виклики на бекенд.

### Відмова від `@microsoft/ai-chat-protocol`

Пакунок npm `@microsoft/ai-chat-protocol` застарілий і його слід замінити на [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Якщо зустрічаєте у фронтенді:

1. Замініть CDN-скрипт тег:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Видаліть інстанцію `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Замініть `client.getStreamedCompletion(messages)` на прямий виклик `fetch()` до стрімінгової кінцевої точки бекенду.
4. Замініть `for await (const response of result)` на `for await (const chunk of readNDJSONStream(response.body))`.
5. Оновіть доступ до властивостей з `response.delta.content` / `response.error` на `chunk.delta.content` / `chunk.error`.

---

## Цілі

- Перелік усіх Python-викликів Chat Completions або застарілих Completions проти Azure OpenAI.
- Запропонувати план міграції та послідовність змін для Python-коду.
- Застосувати безпечні, мінімальні правки для переходу на Responses API.
- Оновити викликачів для роботи із схемою виводу Responses; без оболонок з підтримкою зворотної сумісності.
- Запустити тести/лінти; виправити незначні збої, викликані міграцією.
- Підготувати невеликі, зручні для перегляду набори змін і надати фінальне резюме з різницями (не комітити).

---

## Обмеження

- Модифікувати лише файли у git-репозиторії. Ніколи не писати поза ним.
- Не зберігати шими для сумісності; мігрувати код до нової форми API.
- Не залишати коментарів переходу або резервних копій файлів.
- Зберегти семантику стрімінгу, якщо вона була; інакше використовувати без стрімінгу.
- Запитувати підтвердження перед запуском команд або мережевих викликів, якщо увімкнено режим затвердження.
- Не виконувати `git add`/`git commit`/`git push`; лише змінювати робоче дерево.

---

## Крок 0: Міграція клієнта Azure OpenAI (передумова)

Якщо код використовує конструктори `AzureOpenAI` або `AsyncAzureOpenAI`, спочатку мігруйте їх на стандартні конструктори `OpenAI` / `AsyncOpenAI`. Специфічні конструктори Azure застаріли в `openai>=1.108.1`.

### Чому шлях v1 API?

Нова кінцева точка `/openai/v1` використовує стандартний клієнт `OpenAI()`, а не `AzureOpenAI()`, не вимагає параметра `api_version` і працює однаково на OpenAI та Azure OpenAI. Той самий клієнт використовується надалі — без потреби в управлінні версіями.

### Основні зміни

| До | Після |
|----|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Видалити повністю |

### Контрольний список очищення

- Видалити аргумент `api_version` з конструктора клієнта.
- Видалити змінні оточення `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` з `.env`, налаштувань додатка і Bicep/інфра файлів.
- Перейменувати `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` у `.env`, налаштуваннях додатка, Bicep/інфра та тестових фікстурах (стандартна конвенція Azure Identity SDK).
- Переконатися, що `openai>=1.108.1` у `requirements.txt` або `pyproject.toml`.

### Міграція змінних оточення

| Стара змінна | Дія | Примітки |
|------------|------|----------|
| `AZURE_OPENAI_VERSION` | **Видалити** | `api_version` не потрібен з v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Видалити** | Те саме, що і вище |
| `AZURE_OPENAI_CLIENT_ID` | **Перейменувати** → `AZURE_CLIENT_ID` | Стандартна конвенція Azure Identity SDK для `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Залишити** | Все ще потрібен для конструювання `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Залишити** | Використовується як параметр `model` у `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Залишити** | Використовується як `api_key` для аутентифікації по ключу |

Для прикладів налаштування клієнта (синхронний, асинхронний, EntraID, API-ключ, мультиоренне) див. [cheat-sheet.md](./references/cheat-sheet.md).

---

## Крок 1: Виявити застарілі виклики

Запустіть скрипт [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py), щоб знайти всі виклики, які потребують міграції:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Або виконайте пошуки вручну — кожне співпадіння є об’єктом міграції:

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

# Точки доступу моделей GitHub (потрібно видалити — Responses API не підтримується)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Успадковані шаблони на рівні фреймворку (потрібно оновити)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: замінити на OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: потрібен use_responses_api=True

# Тестова інфраструктура (потрібно оновити)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Доступ до тіла помилки фільтра вмісту (потрібно оновити — структура змінилася)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # старий однина форма — тепер content_filter_results (множина) всередині масиву content_filters

# Сурові HTTP виклики до кінцевої точки Chat Completions (потрібно оновити URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Евристика (виявлення та переписування)

- **Клієнт Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Конструктори клієнтів Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Інструменти**: перетворюйте визначення інструментів для виклику функцій з вкладеного формату (`{"type": "function", "function": {"name": ...}}`) у плоский формат Responses (`{"type": "function", "name": ...}`); використовуйте `tool_choice`; повертайте результати інструментів як елементи `{"type": "function_call_output", "call_id": ..., "output": ...}` (не `{"role": "tool", ...}`).
- **Повторні обходи інструментів**: коли модель повертає виклики функцій, додавайте елементи `response.output` до розмови (а не вручну `{"role": "assistant", "tool_calls": [...]}` словник), потім додавайте елементи `function_call_output` для кожного результату.
- **Приклади використання інструментів з декількома запитами**: якщо у розмові є захардкоджені приклади виклику інструментів, конвертуйте їх у елементи `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Ідентифікатори мають починатися з `fc_`.
- **`pydantic_function_tool()`**: цей помічник досі генерує старий вкладений формат і **не сумісний** з `responses.create()`. Замініть на ручні визначення інструментів або обгортку для сплощення.
- **Багатоходовість**: підтримуйте історію розмови в додатку; передавайте попередні ходи через елементи `input`.
- **Форматування**: замініть верхньорівневий `response_format` в Chat на `text.format` в Responses. Канонічна форма: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Елементи контенту**: замініть у Chat `content[].type: "text"` на Response `content[].type: "input_text"` для ходів користувача/системи.
- **Елементи контенту зображень**: замініть у Chat `content[].type: "image_url"` на Response `content[].type: "input_image"`. Поле `image_url` змінюється з вкладеного об’єкта `{"url": "..."}` на плоский рядок. Див. шпаргалку для прикладів до/після.
- **Зусилля з міркувань**: **мігруйте `reasoning` лише якщо воно вже існує у вихідному коді**.
- **Обробка помилок фільтрації контенту**: змінилася структура тіла помилки. Chat Completions використовував `error.body["innererror"]["content_filter_result"]` (однина); Responses API використовує `error.body["content_filters"][0]["content_filter_results"]` (множина, у масиві). Код, що звертається до `innererror`, викликатиме `KeyError`. Перепишіть на новий шлях.
- **Прямі HTTP виклики**: якщо додаток викликає безпосередньо REST API Azure OpenAI (через `requests`, `httpx` тощо) використовуючи `/openai/deployments/{name}/chat/completions?api-version=...`, перепишіть на `/openai/v1/responses`. Тіло запиту змінюється: `messages` → `input`, додаються `max_output_tokens` і `store: false`, видаляється параметр запиту `api-version`. Тіло відповіді змінюється: `choices[0].message.content` → `output[0].content[0].text` (зверніть увагу: `output_text` — це властивість SDK для зручності, відсутня у сирому REST JSON).

---

## Крок 2: Застосування міграції

### Нотатки про міграцію (Chat Completions → Responses)

- **Чому мігрувати**: Responses — це уніфікований API для тексту, інструментів та стрімінгу; Chat Completions — застарілий. З GPT-5 Responses потрібен для найкращої продуктивності.
- **HTTP**: точка доступу Azure змінюється з `/openai/deployments/{name}/chat/completions` на `/openai/v1/responses`.
- **Поля**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` без змін.
- **Форматування**: `response_format` → `text.format` з відповідним об’єктом.
- **Елементи контенту**: замініть у Chat `content[].type: "text"` на Responses `content[].type: "input_text"` для ходів системи/користувача.
- **Елементи контенту зображень**: замініть у Chat `content[].type: "image_url"` на Responses `content[].type: "input_image"`. Сплющіть поле `image_url` з `{"image_url": {"url": "..."}}` у `{"image_url": "..."}` (простий рядок — або HTTPS URL, або URI даних `data:image/...;base64,...`).

### Посилання для відображення параметрів

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
| `tools` / виклик функцій | `tools` (без змін) |
| `seed` | **Видалити** (не підтримується) |
| `store` | `store` (встановлено у `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (плоский рядок) |

Для повних прикладів коду до/після див. [cheat-sheet.md](./references/cheat-sheet.md).

Для міграції тестової інфраструктури (моки, снапшоти, твердження) див. [test-migration.md](./references/test-migration.md).

Для усунення неполадок та ще рад див. [troubleshooting.md](./references/troubleshooting.md).

---

## Збереження даних та стану

- Встановіть `store: false` у всіх запитах Responses.
- Не покладайтеся на попередні ID повідомлень або контекст на сервері; зберігайте стан на клієнті та мінімізуйте метадані.

---

## Критерії прийняття

### Вимоги на рівні коду (усі мають бути виконані)

- [ ] Нуль збігів для `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` у мігрованих файлах.
- [ ] Нуль збігів для `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — всі конструктори використовують `OpenAI`/`AsyncOpenAI` з кінцевою точкою v1.
- [ ] Нуль збігів для `rg "models\.github\.ai|models\.inference\.ai\.azure"` — кодові шляхи GitHub Models вилучені.
- [ ] Нуль збігів для `rg "OpenAIChatCompletionClient"` — код MAF 1.0.0+ використовує `OpenAIChatClient` (який використовує Responses API). У версії до 1.0.0 оновіть до `agent-framework-openai>=1.0.0`.
- [ ] Всі виклики `ChatOpenAI(...)` містять `use_responses_api=True`.
- [ ] Нуль збігів для `rg "choices\[0\]"` — весь доступ до відповіді здійснюється через `resp.output_text` або схему Responses.
- [ ] Відсутній `response_format` на верхньому рівні; весь структурований вивід використовує `text={"format": {...}}`.
- [ ] `openai>=1.108.1` та `azure-identity` у `requirements.txt` або `pyproject.toml`; залежності перевстановлені.
- [ ] `store=False` встановлено для кожного виклику `responses.create`.
- [ ] Відсутній `api_version` у конструкторі клієнта; `AZURE_OPENAI_API_VERSION` вилучено з файлів оточення та інфраструктури.

### Вимоги до тестової інфраструктури (усі мають бути виконані)

- [ ] Нуль збігів для `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Нуль збігів для `rg "_azure_ad_token_provider" tests/` — твердження оновлені для перевірки `isinstance(client, AsyncOpenAI)` або `base_url`.
- [ ] Нуль збігів для `rg "prompt_filter_results|content_filter_results" tests/` — мокі Azure-специфічного фільтра вилучені.
- [ ] Мок-фікстури використовують `kwargs.get("input")` а не `kwargs.get("messages")`.
- [ ] Снапшоти / golden файли оновлені під структуру стрімінгу Responses (без `choices[0]`, `function_call`, `logprobs` тощо).
- [ ] `pytest` проходить без помилок після оновлення всіх тестів.

### Поведінкові вимоги (перевірка вручну або через тестований механізм)

- [ ] **Базове завершення**: нестрімінговий `responses.create` повертає непорожній `output_text`.
- [ ] **Паритет стріму**: якщо у вихідному коді використовувався стрімінг, мігрований код також стрімить і видає події `response.output_text.delta` з непорожніми дельтами.
- [ ] **Структурований вивід**: якщо використовується `text.format` з `json_schema`, `json.loads(resp.output_text)` виконується успішно і відповідає схемі.
- [ ] **Цикл виклику інструментів**: якщо використовуються інструменти, модель здійснює виклики інструментів, додаток їх виконує, а подальший запит повертає фінальний `output_text` (без нескінченного циклу).
- [ ] **Асинхронний паритет**: якщо використовувався `AsyncAzureOpenAI`, еквівалент `AsyncOpenAI` працює з `await`.
- [ ] **Рівень помилок**: відсутність нових помилок 400/401/404 у порівнянні з базовою лінією до міграції.

### Результати

- Звіт включає відредаговані файли, до/після кількість застарілих викликів, наступні кроки.
- Зміни внесені тільки у робоче дерево (без комітів).

---

## Вимоги до версій SDK

| Пакет | Мінімальна версія |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Остання (для аутентифікації EntraID) |

---

## Посилання

- [Шпаргалка — всі фрагменти коду](./references/cheat-sheet.md)
- [Міграція тестів — моки, снапшоти, твердження](./references/test-migration.md)
- [Усунення неполадок — помилки, таблиця ризиків, підводні камені](./references/troubleshooting.md)
- [detect_legacy.py — автоматизований сканер](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Документація Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Життєвий цикл версій Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Довідник OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->