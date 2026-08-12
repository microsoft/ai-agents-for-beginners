# Шпаргалка Responses API (Python + Azure OpenAI)

> Усі наведені нижче фрагменти коду припускають `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` і що `client` вже ініціалізований (див. налаштування клієнта).

## Базовий запит
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Налаштування клієнта — EntraID (рекомендується)
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

## Асинхронне налаштування клієнта — EntraID з явним зазначенням орендаря (багатоорендне середовище)

Коли ресурс Azure OpenAI знаходиться в **іншому орендарі**, ніж за замовчуванням, передайте `tenant_id` явно в облікові дані. Це поширено в сценаріях розробки/тестування, де домашній орендар розробника відрізняється від орендаря ресурсу.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential для продуктивного використання (Azure Container Apps, App Service тощо)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # керована ідентичність, призначена користувачем
)
# AzureDeveloperCliCredential для локальної розробки — явне tenant_id є критичним
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Ланцюг: спочатку спробуйте керовану ідентичність, у разі невдачі — azd CLI
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

До (застаріло):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4.1",
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

До (легасі — Azure OpenAI Chat Completions):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4.1",
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

## Потокова передача (синхронна)
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
        print()  # новий рядок в кінці
```

## Потокова передача (асинхронна)
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

## Потокова передача в вебзастосунку — форма backend-to-frontend

Під час міграції вебзастосунку, який передає SSE/JSONL на фронтенд, **формат серіалізації на бекенді** змінюється. Спроєктуйте новий бекенд-формат так, щоб зберегти існуючі патерни доступу фронтенда, щоб він не потребував змін.

**Раніше** — бекенд Chat Completions зазвичай серіалізував словник `choices[0]` кожного чанку:
```python
# Старий: серіалізований повний словник вибору для кожного чанку
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Фронтенд читає: `response.delta.content` (глибокий шлях у об’єкті вибору).

**Потім** — бекенд Responses API надсилає мінімальну форму, яка зберігає той самий шлях доступу з фронтенда:
```python
# Нове: надсилати лише те, що потрібно фронтенду
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Фронтенд досі читає `response.delta.content` — **без потреби в змінах фронтенда**.

> **Головна ідея**: Потоковий формат Responses API (`event.type` + `event.delta`) суттєво відрізняється від Chat Completions (`chunk.choices[0].delta.content`). Але ваш контракт бекенд-фронтенд — це ваша відповідальність. Спроєктуйте бекенд-вивід під те, що фронтенд уже очікує.

## Послідовність потокових подій

Коли `stream: true`, API надсилає події в такому порядку:
1. `response.created` – ініціалізація об’єкта відповіді
2. `response.in_progress` – початок генерації
3. `response.output_item.added` – створено елемент виводу
4. `response.content_part.added` – початок частини контенту
5. `response.output_text.delta` – текстові чанки (кілька, кожен має `delta: string`)
6. `response.output_text.done` – генерація тексту завершена
7. `response.content_part.done` – частина контенту завершена
8. `response.output_item.done` – елемент виводу завершено
9. `response.completed` – повна відповідь завершена

Для базового потокового тексту обробляйте лише `response.output_text.delta` (текстові частини) і `response.completed` (завершення).

## Обробка помилок потокової передачі у вебзастосунках

При потоковій передачі у вебзастосунку обгорніть асинхронну ітерацію в `try/except` та передавайте помилки у вигляді JSON, щоб фронтенд міг їх коректно показувати (наприклад, ліміти швидкості, тимчасові збої):

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

> **Чому це важливо**: Azure OpenAI повертає `429 Too Many Requests` при лімітуванні. Без `try/except` потокова відповідь тихо завершується. З ним фронтенд отримує `{"error": "Too Many Requests"}` і може показати запит на повтор.

## Типи потокових подій (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Формат розмови
```python
# API Відповідей підтримує формат бесіди через масив введення
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

## Обробка помилок фільтрації контенту

Структура тіла помилки змінилася з Chat Completions на Responses API.

До (Chat Completions):
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

Основні відмінності:
- Обгортка `innererror` **відсутня** — деталі фільтрації контенту тепер на верхньому рівні `error.body`.
- `content_filter_result` (однина) → `content_filters` (множина масив), що містить `content_filter_results` (множина) в кожному записі.
- Кожен запис у `content_filters` містить `blocked`, `source_type` і `content_filter_results` з деталями по категоріях (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Повна форма тіла помилки фільтрації контенту Responses API:
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

Якщо застосунок викликає Azure OpenAI REST напряму замість використання SDK:

До (Chat Completions):
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

> **Примітка**: `output_text` — це зручність на об’єкті Python SDK `Response`. Сировинна JSON-відповідь REST не має верхньорівневого поля `output_text` — текст знаходиться у `output[0].content[0].text`.

## Багатократна розмова
```python
# Побудувати розмову за допомогою Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Додати відповідь асистента до розмови
messages.append({"role": "assistant", "content": response.output_text})

# Продовжити розмову
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Багатократний контент-тип (явно `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Багатократний через `previous_response_id` (альтернатива)

Замість того, щоб керувати масивом розмови самостійно, ви можете ланцюжити відповіді
на сервері, використовуючи `previous_response_id`. API зберігає кожну відповідь і
автоматично додає попередні кроки.

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
| Масив `input` (ручний) | Повний контроль над історією; можна обрізати/сумаризувати; не потрібне серверне зберігання (`store=False`) | Більше коду; ви керуєте масивом |
| `previous_response_id` | Простий код; автоматичне ланцюжіння | Треба `store=True` (за замовчуванням); історія зберігається на сервері; не можна змінювати історію між ходами |

> **Примітка міграції:** Більшість застосунків Chat Completions уже керують своїм масивом повідомлень, тому перехід на масив `input` є більш прямим 1:1. Використовуйте `previous_response_id` для нового коду або коли не потрібно змінювати історію розмови.

## Моделі серії O (o1, o3-mini, o3, o4-mini)

Моделі серії O мають унікальні обмеження параметрів при міграції до Responses API.

### Відповідність параметрів для серії o

| Chat Completions (серія o) | Responses API | Примітки |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Встановіть високо (4096+) — токени міркувань враховуються у ліміті |
| `reasoning_effort` | `reasoning.effort` | Залиште як є, якщо присутній (low/medium/high) |
| `temperature` | Видаліть або встановіть `1` | Серія o приймає лише `1` |
| `top_p` | Видаліть | Не підтримується на серії o |
| `seed` | Видаліть | Не підтримується в Responses API |

### Серія o до/після

До (Chat Completions із серією o):
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

> **Примітка**: Моделі серії o можуть буферизувати вивід під час міркувань перед надсиланням текстових дельт. Потокова передача працює, але перша подія `response.output_text.delta` може прийти із більшою затримкою, ніж у GPT-моделей.

## Доступ до токенів міркувань
```python
# Моделі логічного мислення використовують внутрішнє міркування — ви можете побачити, скільки токенів міркування було використано
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

> **Важливо**: Використовуйте `max_output_tokens=1000` (не 50–200), щоб врахувати внутрішній процес міркувань моделей. Модель використовує токени міркувань внутрішньо перед генерацією фінального виводу.

## Структурований вивід — JSON Schema
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

- Визначайте функції в `tools` з **плоским форматом Responses API** — ключі `name`, `description` і `parameters` на верхньому рівні (не вкладені під `function`).
- Коли модель запитує виклик інструменту, виконуйте його у вашому застосунку і включайте результат інструменту в наступний запит як елемент `function_call_output`, що знаходиться в `input`.
- Тримайте схеми мінімальними; перевіряйте вхідні дані перед виконанням.
- При використанні `strict: true` всі властивості мають бути вказані в `required`, а `additionalProperties: false` обов’язковий.

> **⚠️ `pydantic_function_tool()` несумісний**: Помічник `openai.pydantic_function_tool()` досі генерує старий вкладений формат Chat Completions (`{"type": "function", "function": {"name": ...}}`). Не використовуйте його з `responses.create()`. Визначайте схеми інструментів вручну або пишіть обгортку для плоского формату виходу.

### Формат визначення інструменту

Responses API використовує **плоский** формат для інструментів — ключі `name`, `description`, `parameters` знаходяться на верхньому рівні (не вкладені під `function`).

**До (Chat Completions — вкладений):**
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

З `strict: true` (примусова перевірка схеми):
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
            "required": ["city_name"],       # Всі властивості МАЮТЬ бути перелічені
            "additionalProperties": False,   # Обов'язково для суворого режиму
        },
    }
]
```

### Круговий виклик інструменту (виконати і повернути результат)

Коли модель запитує виклик інструменту, використовуйте елементи `response.output` + `function_call_output` — **а не** патерн Chat Completions `role: assistant` + `role: tool`.

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

    # Отримати остаточну відповідь з результатами інструментів
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Приклади викликів інструменту з кількома прикладами (few-shot)

При наданні прикладів виклику інструментів у `input`, використовуйте елементи `function_call` і `function_call_output`. Ідентифікатори повинні починатися з `fc_`.

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

## Вхідні зображення

Типи зображень змінюються з `image_url` на `input_image`, а URL переходить із вкладеного об’єкта у плоский рядок.

### Вхідні зображення — до (Chat Completions)
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

### Вхідні зображення — після (Responses API, URL)
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

### Вхідні зображення — після (Responses API, base64)
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

> **Ключові зміни**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (вкладений об’єкт) → `"image_url": "..."` (плоский рядок — або HTTPS URL, або URI даних `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Міграція Microsoft Agent Framework (MAF)

**Спершу перевірте версію MAF** — міграція залежить від того, чи використовуєте ви MAF 1.0.0+ чи попередню бета/риб리즈 версію.

Щоб перевірити: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

У MAF 1.0.0+ `OpenAIChatClient` **вже використовує Responses API** — міграція не потрібна.

Якщо код використовує легасі `OpenAIChatCompletionClient` (який використовує `chat.completions.create`), замініть його на `OpenAIChatClient`:

До:
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

У MAF до 1.0.0 `OpenAIChatClient` використовував Chat Completions. Оновіться до `agent-framework-openai>=1.0.0`, де `OpenAIChatClient` за замовчуванням використовує Responses API.

> **Примітка**: API `Agent`, `MCPStreamableHTTPTool` та інші в MAF не змінюються — лише імпорт і створення клієнтського класу.

## Міграція LangChain (`langchain-openai`)

Додайте `use_responses_api=True` до `ChatOpenAI()`. Також оновіть доступ до вмісту повідомлень з `.content` на `.text`.

До:
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

> **Ключові зміни**: (1) `use_responses_api=True` у конструкторі, (2) `.content` → `.text` у повідомленнях відповіді.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->