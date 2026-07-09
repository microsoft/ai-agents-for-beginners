# Шпаргалка по Responses API (Python + Azure OpenAI)

> Усі наведені нижче приклади передбачають, що `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` та `client` уже ініціалізований (див. налаштування клієнта).

## Основний запит
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Налаштування клієнта — EntraID (рекомендовано)
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Налаштування клієнта — API ключ
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Асинхронне налаштування клієнта — EntraID
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Асинхронне налаштування клієнта — EntraID з явним tenant (багатокористувацький)

Якщо ресурс Azure OpenAI знаходиться в **іншому tenant**, ніж за замовчуванням, передайте `tenant_id` явно в облікові дані. Це часто трапляється в сценаріях розробки/тестування, де домашній tenant розробника відрізняється від tenant ресурсу.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential для продакшну (Azure Container Apps, App Service тощо)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # користувацька призначена керована ідентичність
)
# AzureDeveloperCliCredential для локальної розробки — явний tenant_id є критичним
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Ланцюжок: спочатку спробуйте керовану ідентичність, у разі невдачі використовуйте azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Міграція асинхронного клієнта — до/після

Раніше (застаріло):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

Після:
```python
from openai import AsyncOpenAI

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)

resp = await client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Повна синхронна міграція — до/після

Раніше (легасі — Azure OpenAI Chat Completions):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

Після (Responses API — кінцева точка Azure OpenAI v1):
```python
from openai import OpenAI
import os

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Стримінг (синхронний)
```python
stream = client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()  # новий рядок у кінці
```

## Стримінг (асинхронний)
```python
stream = await client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## Стримінг веб-додатку — структура backend-to-frontend

Під час міграції веб-додатку, який стримить SSE/JSONL на фронтенд, **формат серіалізації бекенду** змінюється. Спроєктуйте новий вихід бекенду так, щоб зберегти існуючі патерни доступу фронтенду, аби фронтенд не потребував змін.

**Раніше** — бекенд Chat Completions зазвичай серіалізував словник `choices[0]` кожного чанку:
```python
# Старий: серіалізований повний словник вибору на кожен блок
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Фронтенд читає: `response.delta.content` (глибокий шлях у обʼєкті choice).

**Після** — бекенд Responses API видає мінімальну структуру, що зберігає той самий шлях доступу фронтенду:
```python
# Нове: надсилати лише те, що потрібне фронтенду
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Фронтенд все ще читає `response.delta.content` — **зміни у фронтенді не потрібні**.

> **Головне:** Структура стримінгу Responses API (`event.type` + `event.delta`) фундаментально відрізняється від Chat Completions (`chunk.choices[0].delta.content`). Але контракт між бекендом і фронтендом — це ваша власна справа. Повертайте у бекенді вихідні дані у форматі, який вже очікує фронтенд.

## Послідовність подій стримінгу

При `stream: true`, API видає події у такому порядку:
1. `response.created` – обʼєкт відповіді ініціалізовано
2. `response.in_progress` – генерація почалася
3. `response.output_item.added` – створено вихідний елемент
4. `response.content_part.added` – початок частини контенту
5. `response.output_text.delta` – текстові чанки (кілька, кожен має `delta: string`)
6. `response.output_text.done` – генерація тексту завершена
7. `response.content_part.done` – частина контенту завершена
8. `response.output_item.done` – вихідний елемент завершено
9. `response.completed` – повна відповідь завершена

Для базового текстового стримінгу обробляйте лише `response.output_text.delta` (текстові чанки) та `response.completed` (для сигналу завершення).

## Обробка помилок стримінгу у веб-додатках

Під час стримінгу у веб-додатку, обгорніть асинхронну ітерацію в `try/except` та повертайте помилки у вигляді JSON, щоб фронтенд міг коректно їх відобразити (наприклад, обмеження за кількістю запитів, тимчасові відмови):

```python
@stream_with_context
async def response_stream():
    chat_coroutine = client.responses.create(
        model=deployment,
        input=all_messages,
        max_output_tokens=1000,
        stream=True,
        store=False,
    )
    try:
        async for event in await chat_coroutine:
            if event.type == "response.output_text.delta":
                yield json.dumps({"delta": {"content": event.delta}}) + "\n"
            elif event.type == "response.completed":
                yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
    except Exception as e:
        current_app.logger.error(e)
        yield json.dumps({"error": str(e)}) + "\n"
```

> **Чому це важливо:** Azure OpenAI повертає `429 Too Many Requests` при обмеженні частоти запитів. Без `try/except` стримінг відповіді тихо припиняється. З `try/except` фронтенд отримує `{"error": "Too Many Requests"}` і може показати пропозицію повторити спробу.

## Типи подій стримінгу (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Формат розмови
```python
# API відповідей підтримує формат розмови через вхідний масив
response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are an Azure cloud architect."},
        {"role": "user", "content": "Design a scalable web application architecture."},
    ],
    max_output_tokens=1000,
)
print(response.output_text)
```

## Обробка помилок фільтру контенту

Структура тіла помилки змінилася від Chat Completions до Responses API.

Раніше (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Після (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Ключові відмінності:
- обгортка `innererror` **зникла** — деталі фільтрації контенту тепер на верхньому рівні `error.body`.
- з `content_filter_result` (однина) стало `content_filters` (множина масив), що містить `content_filter_results` (множина) всередині кожного запису.
- Кожен запис у `content_filters` включає `blocked`, `source_type` та `content_filter_results` із деталями по категоріях (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Повна структура тіла помилки фільтру контенту в Responses API:
```json
{
  "message": "The response was filtered...",
  "type": "invalid_request_error",
  "param": "prompt",
  "code": "content_filter",
  "content_filters": [
    {
      "blocked": true,
      "source_type": "prompt",
      "content_filter_results": {
        "jailbreak": { "detected": true, "filtered": true },
        "hate": { "filtered": false, "severity": "safe" },
        "sexual": { "filtered": false, "severity": "safe" },
        "violence": { "filtered": false, "severity": "safe" },
        "self_harm": { "filtered": false, "severity": "safe" }
      }
    }
  ]
}
```

## Міграція raw HTTP (requests/httpx)

Якщо застосунок викликає Azure OpenAI REST напряму, а не через SDK:

Раніше (Chat Completions):
```python
endpoint = f"{azure_endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-03-01-preview"
data = {
    "messages": [{"role": "user", "content": query}],
    "model": model_name,
    "temperature": 0,
}
response = requests.post(endpoint, headers=headers, json=data)
message = response.json()["choices"][0]["message"]["content"]
```

Після (Responses API):
```python
endpoint = f"{azure_endpoint}/openai/v1/responses"
data = {
    "model": deployment,
    "input": [{"role": "user", "content": query}],
    "temperature": 0,
    "max_output_tokens": 1000,
    "store": False,
}
response = requests.post(endpoint, headers=headers, json=data)
output_text = response.json()["output"][0]["content"][0]["text"]
```

> **Примітка:** `output_text` — це зручна властивість у Python SDK обʼєкта `Response`. Сирий JSON REST-відповіді немає на верхньому рівні поля `output_text` — текст знаходиться в `output[0].content[0].text`.

## Багатокрокова розмова
```python
# Побудуйте розмову за допомогою API відповідей
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Додайте відповідь помічника до розмови
messages.append({"role": "assistant", "content": response.output_text})

# Продовжуйте розмову
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Багатокрокова з typed content (явні `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Багатокрокова через `previous_response_id` (альтернатива)

Замість того, щоб керувати масивом розмови самостійно, ви можете ланцюжити відповіді
на сервері, використовуючи `previous_response_id`. API зберігає кожну відповідь і
автоматично додає попередні ходи.

```python
# Перший хід
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Наступні ходи — просто передайте нове повідомлення користувача + ID попередньої відповіді
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Коли що використовувати:**

| Підхід | Переваги | Недоліки |
|---|---|---|
| Масив `input` (ручний) | Повний контроль над історією; можна обрізати/резюмувати; не потрібне серверне зберігання (`store=False`) | Більше коду; ви керуєте масивом |
| `previous_response_id` | Простий код; автоматичне ланцюження | Потрібен `store=True` (за замовчуванням); розмова зберігається на сервері; не можна змінювати історію між ходами |

> **Примітка міграції:** Більшість застосунків Chat Completions вже самі керують масивом повідомлень, тому перехід на масив `input` є більш прямим 1:1 переходом. Використовуйте `previous_response_id` для нового коду або якщо не потрібно змінювати історію розмови.

## Моделі серії O (o1, o3-mini, o3, o4-mini)

Моделі серії O мають унікальні обмеження параметрів при міграції в Responses API.

### Відповідність параметрів для серії o

| Chat Completions (серія o) | Responses API | Примітки |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Встановлюйте високо (4096+) — токени логіки враховуються у ліміт |
| `reasoning_effort` | `reasoning.effort` | Залишайте як є, якщо присутній (low/medium/high) |
| `temperature` | Видаліть або встановіть `1` | Серія o приймає тільки `1` |
| `top_p` | Видаліть | Не підтримується на серії o |
| `seed` | Видаліть | Не підтримується в Responses API |

### Серія o — до/після

Раніше (Chat Completions з серією o):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Після (Responses API):
```python
resp = client.responses.create(
    model=deployment,
    input="Solve this step by step: 2x + 5 = 13",
    max_output_tokens=4096,
    reasoning={"effort": "medium"},
    store=False,
)
print(resp.output_text)
```

> **Примітка:** Моделі серії O можуть кешувати вивід під час логічного виводу, перш ніж надсилати текстові дельти. Стримінг все одно працює, але перша подія `response.output_text.delta` може надійти із тривалішою затримкою ніж у моделей GPT.

## Доступ до токенів логіки
```python
# Моделі міркування використовують внутрішнє міркування — ви можете побачити, скільки токенів міркування було використано
response = client.responses.create(
    model=deployment,
    input="Explain quantum computing in simple terms",
    max_output_tokens=1000,
)
print(response.output_text)
print(f"Status: {response.status}")
print(f"Reasoning tokens: {response.usage.output_tokens_details.reasoning_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

> **Важливо:** Використовуйте `max_output_tokens=1000` (не 50–200), щоб врахувати внутрішній процес логічного виводу моделей. Модель спочатку використовує токени логіки, перш ніж генерувати фінальний вихід.

## Структурований вихід — JSON Schema
```python
resp = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
    max_output_tokens=500,
    text={
        "format": {
            "type": "json_schema",
            "name": "Output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"answer": {"type": "string"}},
                "required": ["answer"],
                "additionalProperties": False,
            },
        }
    },
    store=False,
)
import json
data = json.loads(resp.output_text)
print(data["answer"])
```

## Використання інструментів

- Визначайте функції в `tools` у **плоскому форматі Responses API** — `name`, `description` та `parameters` на верхньому рівні (не вкладені під `function`).
- Коли модель просить викликати інструмент, виконуйте його у вашому застосунку і включайте результат інструмента у наступний запит як елемент `function_call_output` всередині `input`.
- Тримайте схеми мінімальними; перевіряйте вхідні дані перед виконанням.
- При використанні `strict: true` усі властивості повинні бути перелічені в `required` і `additionalProperties: false` є обовʼязковим.

> **⚠️ `pydantic_function_tool()` несумісний**: Хелпер `openai.pydantic_function_tool()` досі генерує старий вкладений формат Chat Completions (`{"type": "function", "function": {"name": ...}}`). Не використовувати його з `responses.create()`. Визначайте схеми інструментів вручну або напишіть обгортку для плоского формату.

### Формат визначення інструмента

Responses API використовує **плоский** формат інструментів — `name`, `description`, `parameters` є ключами верхнього рівня (не вкладені під `function`).

**Раніше (Chat Completions — вкладений):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Після (Responses API — плоский):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Повний приклад:
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are a weather chatbot."},
        {"role": "user", "content": "What's the weather in Berkeley?"},
    ],
    tools=tools,
    tool_choice="auto",
    store=False,
)
```

З `strict: true` (примусове дотримання схеми):
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],       # Всі властивості ПОВИННІ бути зазначені
            "additionalProperties": False,   # Обов’язково для суворого режиму
        },
    }
]
```

### Круговий виклик інструмента (виконання і повернення результатів)

Коли модель запитує виклик інструмента, використовуйте елементи `response.output` + `function_call_output` — **не** патерн Chat Completions з `role: assistant` + `role: tool`.

```python
import json

messages = [
    {"role": "system", "content": "You are a weather chatbot."},
    {"role": "user", "content": "Is it sunny in Berkeley?"},
]

response = client.responses.create(
    model=deployment, input=messages, tools=tools, store=False,
)

tool_calls = [item for item in response.output if item.type == "function_call"]
if tool_calls:
    # Додати елементи function_call моделі до розмови
    messages.extend(response.output)

    # Виконати кожен інструмент і додати результати
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Отримати кінцеву відповідь з результатами інструментів
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Приклади кількох викликів інструментів

При подачі кількох прикладів викликів в `input`, використовуйте елементи `function_call` і `function_call_output`. Ідентифікатори мають починатися з `fc_`.

```python
messages = [
    {"role": "system", "content": "You are a product search assistant."},
    {"role": "user", "content": "Find climbing gear for outdoors"},
    {
        "type": "function_call",
        "id": "fc_example1",
        "call_id": "call_example1",
        "name": "search_database",
        "arguments": '{"search_query": "climbing gear outdoor"}',
    },
    {
        "type": "function_call_output",
        "call_id": "call_example1",
        "output": "Results: ...",
    },
    {"role": "user", "content": "Now find shoes under $50"},
]
```

```python
# Приклад вбудованого веб-пошуку
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Вхідне зображення

Елементи контенту зображення змінили тип з `image_url` на `input_image`, а URL змінився з вкладеного обʼєкта на плоский рядок.

### Вхідне зображення — раніше (Chat Completions)
```python
resp = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

### Вхідне зображення — після (Responses API, URL)
```python
resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

### Вхідне зображення — після (Responses API, base64)
```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("path_to_your_image.jpg")

resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

> **Ключові зміни:** (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (вкладений обʼєкт) → `"image_url": "..."` (плоский рядок — чи то HTTPS URL, чи data URI у форматі `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Міграція Microsoft Agent Framework (MAF)

**Спершу перевірте версію MAF** — міграція залежить від того, чи у вас MAF 1.0.0+ чи бета/rc перед 1.0.0.

Для перевірки: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

В MAF 1.0.0+ `OpenAIChatClient` **вже використовує Responses API** — міграція не потрібна.

Якщо кодова база використовує спадковий `OpenAIChatCompletionClient` (що викликає `chat.completions.create`), замініть його на `OpenAIChatClient`:

Раніше:
```python
from agent_framework.openai import OpenAIChatCompletionClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatCompletionClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

Після:
```python
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

### MAF до 1.0.0 (бета/rc релізи)

У бета-версіях MAF до 1.0.0 `OpenAIChatClient` використовував Chat Completions. Оновіться до `agent-framework-openai>=1.0.0`, де `OpenAIChatClient` за замовчуванням використовує Responses API.

> **Примітка:** API `Agent`, `MCPStreamableHTTPTool` та інших залишаються без змін — змінюються лише імпорт та інстанціювання класу клієнта.

## Міграція LangChain (`langchain-openai`)

Додайте `use_responses_api=True` у `ChatOpenAI()`. Також оновіть доступ до вмісту повідомлень з `.content` на `.text`.

Раніше:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
)

# ... виклик агента ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Після:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
    use_responses_api=True,
)

# ... виклик агента ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Ключові зміни:** (1) `use_responses_api=True` у конструкторі, (2) `.content` → `.text` у повідомленнях відповіді.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->