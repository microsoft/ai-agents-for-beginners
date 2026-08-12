# Чит-лист по Responses API (Python + Azure OpenAI)

> Все примеры ниже подразумевают `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` и что `client` уже инициализирован (см. настройку клиента).

## Базовый запрос
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Настройка клиента — EntraID (рекомендуется)
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

## Настройка клиента — API ключ
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Асинхронная настройка клиента — EntraID
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

## Асинхронная настройка клиента — EntraID с явным указанием арендатора (мультиарендность)

Когда ресурс Azure OpenAI находится в **другом арендаторе**, чем по умолчанию, передавайте `tenant_id` явно в креденшелы. Это часто встречается в сценариях разработки/тестирования, где домашний арендатор разработчика отличается от арендатора ресурса.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential для продакшена (Azure Container Apps, App Service и т.д.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # управляемая идентификация, назначенная пользователем
)
# AzureDeveloperCliCredential для локальной разработки — критически важен явный tenant_id
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Цепочка: сначала попытаться использовать управляемую идентификацию, затем перейти к azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Миграция асинхронного клиента — до/после

Ранее (устарело):
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

После:
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

## Полная синхронная миграция — до/после

Ранее (наследие — Azure OpenAI Chat Completions):
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

После (Responses API — конечная точка Azure OpenAI v1):
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

## Потоковая передача данных (синхронно)
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
        print()  # новая строка в конце
```

## Потоковая передача данных (асинхронно)
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

## Веб-приложение с потоковой передачей — формат между бэкендом и фронтендом

При миграции веб-приложения, которое транслирует SSE/JSONL на фронтенд, **формат сериализации на бэкенде** изменяется. Спроектируйте новый вывод бэкенда так, чтобы сохранить существующие паттерны доступа фронтенда, чтобы никакие изменения во фронтенде не потребовались.

**Ранее** — бэкенд Chat Completions обычно сериализовал `choices[0]` словаря каждого чанка:
```python
# Старое: сериализованный полный словарь выбора по каждому чанку
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Фронтенд читает: `response.delta.content` (глубокий путь в объект выбора).

**После** — бэкенд Responses API выпускает минимальную структуру, сохраняющую тот же путь доступа на фронтенде:
```python
# Новое: испускать только то, что нужно фронтенду
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Фронтенд по-прежнему читает `response.delta.content` — **изменения на фронтенде не нужны**.

> **Ключевой вывод**: Формат потоковой передачи Responses API (`event.type` + `event.delta`) принципиально отличается от Chat Completions (`chunk.choices[0].delta.content`). Но контракт между бэкендом и фронтендом вы задаёте сами. Формируйте вывод бэкенда так, чтобы он соответствовал тому, что фронтенд уже ожидает.

## Последовательность событий потоковой передачи

При `stream: true` API выдаёт события в этом порядке:
1. `response.created` – объект ответа инициализирован
2. `response.in_progress` – генерация началась
3. `response.output_item.added` – создан элемент вывода
4. `response.content_part.added` – начата часть контента
5. `response.output_text.delta` – текстовые чанки (несколько, каждый с `delta: string`)
6. `response.output_text.done` – генерация текста завершена
7. `response.content_part.done` – часть контента завершена
8. `response.output_item.done` – элемент вывода завершён
9. `response.completed` – полный ответ завершён

Для базовой потоковой передачи текста обрабатывайте только `response.output_text.delta` (текстовые чанки) и `response.completed` (завершение).

## Обработка ошибок потоковой передачи в веб-приложениях

При потоковой передаче в веб-приложении оборачивайте асинхронную итерацию в `try/except` и отдавайте ошибки в JSON, чтобы фронтенд мог корректно их отображать (например, лимиты скорости, временные сбои):

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

> **Зачем это нужно**: Azure OpenAI возвращает `429 Too Many Requests` при превышении лимитов. Без `try/except` потоковый ответ тихо завершается. С ним фронтенд получает `{"error": "Too Many Requests"}` и может показать предложение повторить запрос.

## Типы событий потоковой передачи (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Формат разговора
```python
# API ответов поддерживает формат разговора через массив ввода
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

## Обработка ошибок фильтра контента

Структура тела ошибки изменилась с Chat Completions на Responses API.

Ранее (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

После (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Ключевые отличия:
- Обёртка `innererror` **удалена** — детали фильтра контента теперь на верхнем уровне `error.body`.
- `content_filter_result` (единственное) → `content_filters` (множественный массив), содержащий `content_filter_results` (множественные) внутри каждой записи.
- Каждая запись в `content_filters` включает `blocked`, `source_type` и `content_filter_results` с деталями по категориям (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Полная форма тела ошибки фильтра контента Responses API:
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

## Миграция на уровень HTTP (requests/httpx)

Если приложение вызывает Azure OpenAI REST напрямую, а не через SDK:

Ранее (Chat Completions):
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

После (Responses API):
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

> **Примечание**: `output_text` — это удобное свойство объекта `Response` в Python SDK. Сырой JSON-ответ REST не содержит верхнего поля `output_text` — текст находится в `output[0].content[0].text`.

## Многошаговый разговор
```python
# Постройте разговор с помощью API Ответов
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Добавьте ответ ассистента в разговор
messages.append({"role": "assistant", "content": response.output_text})

# Продолжить разговор
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Многошаговый с типизированным содержимым (явные `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Многошаговый с помощью `previous_response_id` (альтернативный)

Вместо самостоятельного управления массивом сообщений можете цеплять ответы
на сервере с помощью `previous_response_id`. API хранит каждый ответ и
автоматически подставляет предыдущие шаги.

```python
# Первый ход
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Последующие ходы — просто передайте новое сообщение пользователя + ID предыдущего ответа
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Когда что использовать:**

| Метод | Преимущества | Недостатки |
|---|---|---|
| Массив `input` (ручной) | Полный контроль над историей; можно укорачивать/резюмировать; не нужен серверный сторедж (`store=False`) | Больше кода; сами управляете массивом |
| `previous_response_id` | Проще код; автоматическое сцепление | Требует `store=True` (по умолчанию); беседа хранится серверно; нельзя изменять историю между ходами |

> **Примечание миграции:** Большинство приложений Chat Completions уже управляют собственным массивом сообщений, поэтому конвертация в массив `input` — более прямой 1:1 переход. Используйте `previous_response_id` для нового кода или если не нужно изменять историю диалога.

## Reasoning модели серии O (o1, o3-mini, o3, o4-mini)

Модели серии O имеют уникальные ограничения параметров при миграции на Responses API.

### Соответствие параметров для серии O

| Chat Completions (серия O) | Responses API | Примечания |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Устанавливайте высоко (4096+) — токены рассуждения учитываются в лимите |
| `reasoning_effort` | `reasoning.effort` | Оставьте как есть, если есть (low/medium/high) |
| `temperature` | Уберите или установите в `1` | Серия O принимает только `1` |
| `top_p` | Уберите | Не поддерживается в серии O |
| `seed` | Уберите | Не поддерживается в Responses API |

### Серия O до/после

Ранее (Chat Completions с серией O):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

После (Responses API):
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

> **Примечание**: Модели серии O могут буферизовать вывод во время рассуждений перед выпуском текстовых дельт. Потоковая передача работает, но первое событие `response.output_text.delta` может появиться позже, чем у моделей GPT.

## Доступ к токенам рассуждений
```python
# Модели рассуждений используют внутреннее рассуждение — вы можете увидеть, сколько токенов рассуждения было использовано
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

> **Важно**: Используйте `max_output_tokens=1000` (не 50-200), чтобы учесть внутренний процесс рассуждений моделей. Модель использует токены рассуждений внутри перед генерацией итогового вывода.

## Структурированный вывод — JSON Schema
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

## Использование инструментов

- Определяйте функции в `tools` с **плоским форматом Responses API** — `name`, `description` и `parameters` находятся на верхнем уровне (не вложены в `function`).
- Когда модель просит вызвать инструмент, выполняйте его в приложении и включайте результат вызова в следующий запрос как элемент `function_call_output` внутри `input`.
- Держите схемы минимальными; валидируйте входные данные перед выполнением.
- При использовании `strict: true` все свойства должны быть указаны в `required`, а `additionalProperties: false` обязательно.

> **⚠️ `pydantic_function_tool()` несовместим**: Хелпер `openai.pydantic_function_tool()` всё ещё генерирует старый вложенный формат Chat Completions (`{"type": "function", "function": {"name": ...}}`). Не используйте его с `responses.create()`. Определяйте схемы инструментов вручную или пишите обёртку для выравнивания вывода.

### Формат определения инструмента

Responses API использует **плоский** формат инструмента — `name`, `description`, `parameters` — верхнеуровневые ключи (не вложены в `function`).

**Ранее (Chat Completions — вложенный):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**После (Responses API — плоский):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Полный пример:
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

С `strict: true` (жёсткое соблюдение схемы):
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
            "required": ["city_name"],       # Все свойства ДОЛЖНЫ быть перечислены
            "additionalProperties": False,   # Обязательно для строгого режима
        },
    }
]
```

### Круг вызова инструмента (выполнить и вернуть результаты)

Когда модель запрашивает вызов инструмента, используйте элементы `response.output` + `function_call_output` — **не** паттерн Chat Completions с `role: assistant` + `role: tool`.

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
    # Добавьте элементы function_call модели в беседу
    messages.extend(response.output)

    # Выполните каждый инструмент и добавьте результаты
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Получите окончательный ответ с результатами инструментов
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Примеры вызова инструментов с few-shot

При предоставлении примеров вызова инструментов в `input` используйте элементы `function_call` и `function_call_output`. ID должны начинаться с `fc_`.

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
# Пример встроенного веб-поиска
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Ввод изображения

Элементы контента изображения меняют тип с `image_url` на `input_image`, а URL меняется с вложенного объекта на плоскую строку.

### Ввод изображения — ранее (Chat Completions)
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

### Ввод изображения — после (Responses API, URL)
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

### Ввод изображения — после (Responses API, base64)
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

> **Ключевые изменения**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (вложенный объект) → `"image_url": "..."` (плоская строка — либо HTTPS URL, либо data URI вида `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Миграция Microsoft Agent Framework (MAF)

**Сначала проверьте версию MAF** — миграция зависит от того, используете ли вы MAF 1.0.0+ или предрелизные версии до 1.0.0.

Для проверки: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

В MAF 1.0.0+ `OpenAIChatClient` **уже использует Responses API** — миграция не требуется.

Если в кодовой базе используется устаревший `OpenAIChatCompletionClient` (который вызывает `chat.completions.create`), замените его на `OpenAIChatClient`:

Ранее:
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

После:
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

### MAF до 1.0.0 (бета/rc релизы)

В MAF до 1.0.0 `OpenAIChatClient` использовал Chat Completions. Обновитесь до `agent-framework-openai>=1.0.0`, где `OpenAIChatClient` по умолчанию использует Responses API.

> **Примечание**: API `Agent`, `MCPStreamableHTTPTool` и другие MAF остаются без изменений — меняются только импорт и создание экземпляра клиентского класса.

## Миграция LangChain (`langchain-openai`)

Добавьте `use_responses_api=True` в `ChatOpenAI()`. Также обновите доступ к содержимому сообщений с `.content` на `.text`.

Ранее:
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

# ... вызов агента ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

После:
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

# ... вызов агента ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Ключевые изменения**: (1) `use_responses_api=True` в конструкторе, (2) `.content` → `.text` в сообщениях ответа.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->