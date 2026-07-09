# Ръководство за Responses API (Python + Azure OpenAI)

> Всички фрагменти по-долу приемат, че `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` и че `client` вече е инициализиран (виж настройка на клиента).

## Основна заявка
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Настройка на клиента — EntraID (препоръчително)
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

## Настройка на клиента — API ключ
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Асинхронна настройка на клиента — EntraID
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

## Асинхронна настройка на клиента — EntraID с експлицитен tenant (мулти-tenant)

Когато ресурсът Azure OpenAI е в **различен tenant** от подразбиращия се, предайте `tenant_id` явно в креденциала. Това е често срещано в сценарии за разработка/тестване, където home tenant на разработчика е различен от този на ресурса.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential за продукция (Azure Container Apps, App Service и др.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # управлявана идентичност, зададена от потребител
)
# AzureDeveloperCliCredential за локална разработка — изричното tenant_id е критично
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Верига: първо опитай управлявана идентичност, при неуспех премини към azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Миграция на асинхронен клиент — преди/след

Преди (преходно):
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

След:
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

## Пълна синхронна миграция — преди/след

Преди (legacy — Azure OpenAI Chat Completions):
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

След (Responses API — Azure OpenAI v1 крайна точка):
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

## Потоково предаване (sync)
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
        print()  # нов ред в края
```

## Потоково предаване (async)
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

## Потоково предаване на уеб приложение — форма backend-to-frontend

При миграция на уеб приложение, което стриймва SSE/JSONL към фронтенд, **форматът на сериализация в бекенда** се променя. Проектирайте новия бекенд изход така, че да запази съществуващите модели на достъп на фронтенда, за да не са необходими промени там.

**Преди** — бекендът на Chat Completions обикновено сериализираше речника `choices[0]` на всеки chunk:
```python
# Старо: сериализиран пълен речник на избора за всеки сегмент
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Фронтенд четене: `response.delta.content` (дълбок път до изборния обект).

**След** — бекендът на Responses API излиза с минимална форма, запазваща същия фронтенд път за достъп:
```python
# Ново: изпращайте само това, от което се нуждае потребителският интерфейс
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Фронтендът все още чете `response.delta.content` — **не са нужни промени във фронтенда**.

> **Основна идея**: Форматът за потоково предаване на Responses API (`event.type` + `event.delta`) е съществено различен от Chat Completions (`chunk.choices[0].delta.content`). Но вашият контракт backend-to-frontend е по ваша преценка. Оформете бекенд изхода така, че да съвпада с онова, което фронтендът вече очаква.

## Последователност на събитията за потоково предаване

Когато `stream: true`, API-то излъчва събития в този ред:
1. `response.created` – инициализиран обект отговор
2. `response.in_progress` – стартирано генериране
3. `response.output_item.added` – създаден изходен елемент
4. `response.content_part.added` – започнал се е част от съдържанието
5. `response.output_text.delta` – текстови кусове (множество, всеки има `delta: string`)
6. `response.output_text.done` – генерирането на текста приключи
7. `response.content_part.done` – частта от съдържанието приключи
8. `response.output_item.done` – изходният елемент приключи
9. `response.completed` – пълен отговор завършен

За основно потоково предаване на текст обработвайте само `response.output_text.delta` (за текстови кусове) и `response.completed` (за завършване).

## Обработка на грешки при потоково предаване в уеб приложения

Когато стриймвате в уеб приложение, обградете асинхронната итерация в `try/except` и предавайте грешките като JSON, така че фронтендът да може да ги показва красиво (напр. ограничения на честотата, временни грешки):

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

> **Защо това е важно**: Azure OpenAI връща `429 Too Many Requests` при ограничаване на честотата. Без `try/except`, потоковият отговор умира безшумно. С него фронтендът получава `{"error": "Too Many Requests"}` и може да покаже подкана за повторен опит.

## Типове събития за потоково предаване (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Формат на разговора
```python
# API за отговори поддържа формат на разговор чрез масив входни данни
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

## Обработка на грешки при content filter

Структурата на тялото на грешката се промени от Chat Completions към Responses API.

Преди (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

След (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Основни разлики:
- обвивката `innererror` е **премахната** — детайлите на content filter сега са на върховото ниво в `error.body`.
- `content_filter_result` (единствено) → `content_filters` (множествен масив) съдържащ `content_filter_results` (множествено) във всяка записа.
- Всяка записа в `content_filters` включва `blocked`, `source_type` и `content_filter_results` с детайли по категории (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Пълна форма на тялото на грешка за content filter на Responses API:
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

## Миграция на Raw HTTP (requests/httpx)

Ако приложението извиква Azure OpenAI REST директно вместо да използва SDK:

Преди (Chat Completions):
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

След (Responses API):
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

> **Забележка**: `output_text` е удобен property на Python SDK обекта `Response`. Суровият JSON от REST няма поле `output_text` на върховото ниво — текстът е в `output[0].content[0].text`.

## Многоходов разговор
```python
# Изградете разговор с Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Добавете отговор на асистента към разговора
messages.append({"role": "assistant", "content": response.output_text})

# Продължете разговора
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Многоходов с тип съдържание (експлицитен `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Многоходов чрез `previous_response_id` (алтернатива)

Вместо да управлявате масива с разговори ръчно, можете да вържете отговорите от сървърната страна, използвайки `previous_response_id`. API-то съхранява всеки отговор и
автоматично предшества предишните ходове.


```python
# Първи ход
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Следващи ходове — просто предайте новото съобщение от потребителя + ID на предишния отговор
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Кога да ползвате кое:**

| Подход | Предимства | Недостатъци |
|---|---|---|
| Массив `input` (ръчен) | Пълен контрол върху историята; може да се монтира/резюмира; не е нужна сървърна памет (`store=False`) | Повече код; вие управлявате масива |
| `previous_response_id` | По-лесен код; автоматично свързване | Изисква `store=True` (по подразбиране); разговорът се съхранява на сървъра; не може да се редактира историята между ходовете |

> **Бележка за миграция:** Повечето Chat Completions приложения вече управляват собствения си масив с съобщения, така че преминаването към масив `input` е по-пряк 1:1 преход. Използвайте `previous_response_id` за нов код или когато не ви трябва манипулиране на историята на разговора.

## Модели за разсъждение от серия O (o1, o3-mini, o3, o4-mini)

Моделите от серия O имат специфични параметрични ограничения при миграция към Responses API.

### Съответствие на параметрите за серия O

| Chat Completions (серия O) | Responses API | Бележки |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Поставете високо (4096+) — токените за разсъждение се броят към лимита |
| `reasoning_effort` | `reasoning.effort` | Оставете същото, ако е налично (low/medium/high) |
| `temperature` | Премахнете или задайте на `1` | Серия О приема само `1` |
| `top_p` | Премахнете | Не се поддържа на серия О |
| `seed` | Премахнете | Не се поддържа в Responses API |

### Серия O преди/след

Преди (Chat Completions със серия О):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

След (Responses API):
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

> **Забележка**: Моделите серия O може да буферират изхода по време на разсъждение преди да излъчат текстови делти. Потоковото предаване все още работи, но първото събитие `response.output_text.delta` може да пристигне с по-дълго забавяне в сравнение с GPT моделите.

## Достъп до токени за разсъждение
```python
# Моделите за разсъждение използват вътрешно разсъждение — можете да видите колко токена за разсъждение са били използвани
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

> **Важно**: Използвайте `max_output_tokens=1000` (не 50–200), за да отчетете вътрешния процес на разсъждение на моделите за разсъждение. Моделът използва токени за разсъждение вътрешно преди да генерира крайния изход.

## Структуриран изход — JSON Schema
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

## Използване на инструменти

- Дефинирайте функции в `tools` с **плосък формат Responses API** — `name`, `description` и `parameters` на върховото ниво (не вложени под `function`).
- Когато моделът поиска да извика инструмент, изпълнете го в приложението си и включете резултата от инструмента в следващата заявка като елемент `function_call_output` в `input`.
- Поддържайте схемите минимални; валидирайте входовете преди изпълнение.
- При използване на `strict: true` всички свойства трябва да са изброени в `required` и `additionalProperties: false` е задължително.

> **⚠️ `pydantic_function_tool()` е несъвместим**: помощната функция `openai.pydantic_function_tool()` все още генерира стария вложен формат на Chat Completions (`{"type": "function", "function": {"name": ...}}`). Не я използвайте с `responses.create()`. Дефинирайте схемите на инструмента ръчно или напишете обвивка, която да ги направи плоски.

### Формат за дефиниране на инструмент

Responses API използва **плосък** формат на инструмента — `name`, `description`, `parameters` са ключове на върховото ниво (не вложени под `function`).

**Преди (Chat Completions — вложен):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**След (Responses API — плосък):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Пълен пример:
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

С `strict: true` (налагане на схема):
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
            "required": ["city_name"],       # Всички свойства ТРЯБВА да бъдат изброени
            "additionalProperties": False,   # Задължително за строг режим
        },
    }
]
```

### Кръг на повикване на инструмент (изпълнение и връщане на резултати)

Когато моделът поиска повикване на инструмент, използвайте елементи `response.output` + `function_call_output` — **не** шаблона на Chat Completions с `role: assistant` + `role: tool`.

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
    # Добавете елементите function_call на модела към разговора
    messages.extend(response.output)

    # Изпълнете всеки инструмент и добавете резултатите
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Вземете окончателния отговор с резултатите от инструментите
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Примери за few-shot повиквания на инструменти

При предоставяне на few-shot примери за повиквания на инструменти в `input`, използвайте елементи `function_call` и `function_call_output`. ID-тата трябва да започват с `fc_`.

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
# Вграден пример за уеб търсене
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Входна картинна информация

Елементите със съдържание тип изображение сменят типа си от `image_url` на `input_image`, а URL адресът се променя от вложен обект в плосък низ.

### Входна картинна информация — преди (Chat Completions)
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

### Входна картинна информация — след (Responses API, URL)
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

### Входна картинна информация — след (Responses API, base64)
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

> **Ключови промени**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (вложен обект) → `"image_url": "..."` (плосък низ — HTTPS URL или `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Миграция на Microsoft Agent Framework (MAF)

**Проверете първо версията на MAF** — миграцията зависи дали използвате MAF 1.0.0+ или преди 1.0.0 бета/rc.

За проверка: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

В MAF 1.0.0+, `OpenAIChatClient` **вече използва Responses API** — не е нужна миграция.

Ако кодовата база използва наследения `OpenAIChatCompletionClient` (който използва `chat.completions.create`), заменете го с `OpenAIChatClient`:

Преди:
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

След:
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

### MAF преди 1.0.0 (бета/rc версии)

В предишния MAF под 1.0.0, `OpenAIChatClient` използваше Chat Completions. Ъпгрейднете до `agent-framework-openai>=1.0.0`, където `OpenAIChatClient` използва Responses API по подразбиране.

> **Забележка**: API-тата на `Agent`, `MCPStreamableHTTPTool` и други в MAF остават непроменени — само импортирането и инстанцирането на клиентската клас са различни.

## Миграция на LangChain (`langchain-openai`)

Добавете `use_responses_api=True` към `ChatOpenAI()`. Също така обновете достъпа до съдържанието на съобщенията от `.content` на `.text`.

Преди:
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

# ... извикване на агент ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

След:
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

# ... извикване на агент ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Ключови промени**: (1) `use_responses_api=True` в конструктора, (2) `.content` → `.text` в съобщенията с отговор.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->