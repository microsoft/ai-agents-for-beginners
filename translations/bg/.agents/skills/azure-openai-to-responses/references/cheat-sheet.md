# Резюме за Responses API (Python + Azure OpenAI)

> Всички примери по-долу приемат `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` и че `client` вече е инициализиран (виж настройка на клиента).

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

## Асинхронна настройка на клиента — EntraID с изрично зададен тенант (мулти-тенант)

Когато ресурсът Azure OpenAI е в **различен тенант** от подразбиращия се, подайте `tenant_id` изрично в креденциала. Това е често срещано в развитие/тестови сценарии, където домашният тенант на разработчика е различен от този на ресурса.

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
    client_id=os.getenv("AZURE_CLIENT_ID")  # потребителско зададена управлявана идентичност
)
# AzureDeveloperCliCredential за локална разработка — изричното tenant_id е критично
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Верига: първо опитай управляваната идентичност, при неуспех използвай azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Асимхронна миграция на клиента — преди/след

Преди (непрепоръчително):
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

Преди (старата версия — Azure OpenAI Chat Completions):
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

## Стрийминг (синхронен)
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

## Стрийминг (асинхронен)
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

## Стрийминг на уеб приложение — форма от бекенд към фронтенд

При миграция на уеб приложение, което стриймва SSE/JSONL към фронтенд, **форматът за сериализация в бекенда** се променя. Проектирайте новия изход на бекенда така, че да съответства на съществуващите модели за достъп на фронтенда, за да не се налагат промени във фронтенда.

**Преди** — бекендът на Chat Completions обикновено сериализира речника `choices[0]` на всеки фрагмент:
```python
# Старо: сериализиран пълен речник на изборите за всяка част
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Фронтенд чете: `response.delta.content` (дълбок път в обекта choice).

**След** — бекендът на Responses API издава минимална форма, запазваща същия достъп на фронтенда:
```python
# Ново: излъчвайте само това, от което имате нужда във фронтенда
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Фронтендът все още чете `response.delta.content` — **не са нужни промени във фронтенда**.

> **Ключово прозрение**: Формата за стрийминг на Responses API (`event.type` + `event.delta`) е фундаментално различна от Chat Completions (`chunk.choices[0].delta.content`). Но договорът от бекенд към фронтенд е ваше решение. Оформете изхода от бекенда така, че да отговаря на очакванията на фронтенда.

## Ред на събитията при стрийминг

Когато `stream: true`, API издава събития в този ред:
1. `response.created` – инициализиране на response обекта
2. `response.in_progress` – започнато генериране
3. `response.output_item.added` – създаден изходен артикул
4. `response.content_part.added` – започната част от съдържанието
5. `response.output_text.delta` – текстови фрагменти (няколко, всеки с `delta: string`)
6. `response.output_text.done` – приключено генериране на текст
7. `response.content_part.done` – приключена част от съдържанието
8. `response.output_item.done` – приключен изходен артикул
9. `response.completed` – пълен отговор готов

За основен текстов стрийминг се обработват само `response.output_text.delta` (за текстови фрагменти) и `response.completed` (за финал).

## Обработка на грешки при стрийминг в уеб приложения

При стрийминг в уеб приложение оградете асинхронната итерация в `try/except` и връщайте грешките като JSON, за да може фронтендът да ги показва елегантно (напр. ограничения на честотата, временни грешки):

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

> **Защо е важно това**: Azure OpenAI връща `429 Too Many Requests` при ограничение на трафика. Без `try/except` стриймингът спира тихо. С `try/except` фронтендът получава `{"error": "Too Many Requests"}` и може да покаже подкана за повтаряне.

## Типове събития при стрийминг (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Формат на разговора
```python
# API-то за отговори поддържа формат на разговор чрез масив от входни данни
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

## Обработка на грешки при филтър за съдържание

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

Ключови разлики:
- Обвивката `innererror` е **премахната** — детайлите за филтъра за съдържание са вече на най-високо ниво в `error.body`.
- `content_filter_result` (единствено) → `content_filters` (множествен масив), съдържащ `content_filter_results` (множествено) във всеки запис.
- Всеки запис в `content_filters` включва `blocked`, `source_type` и `content_filter_results` с детайли за категории (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Пълна структура на тялото на грешка за филтър за съдържание в Responses API:
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

## Миграция при Raw HTTP (requests/httpx)

Ако приложението извиква Azure OpenAI REST директно, а не SDK:

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

> **Забележка**: `output_text` е удобство в Python SDK `Response` обекта. Суровият JSON от REST няма поле `output_text` на най-високо ниво — текстът е в `output[0].content[0].text`.

## Мултиходов разговор
```python
# Създайте разговор с Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Добавете отговора на асистента към разговора
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

Мултиходов с типизирано съдържание (изрично `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Мултиходов чрез `previous_response_id` (алтернативен метод)

Вместо сами да управлявате масива от разговори, можете да свържете отговори
от страна на сървъра със `previous_response_id`. API записва всеки отговор и
автоматично добавя предшестващите ходове.

```python
# Първи ход
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Последващи ходове — просто предайте новото съобщение от потребителя + предишния ID на отговора
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Кога да използвате кой подход:**

| Подход | Предимства | Недостатъци |
|---|---|---|
| Массив `input` (ръчен) | Пълен контрол върху историята; може да се изрязва/обобщава; не е нужна сървърна памет (`store=False`) | Повече код; вие управлявате масива |
| `previous_response_id` | По-прост код; автоматично свързване | Изисква `store=True` (по подразбиране); разговора се съхранява сървърно; не може да се модифицира историята между ходовете |

> **Забележка при миграция:** Повечето приложения Chat Completions вече управляват собствен масив с послания, затова конвертирането към масива `input` е по-пряка миграция 1:1. Използвайте `previous_response_id` за нов код или когато не трябва да променяте историята на разговора.

## Модели за разсъждение серия O (o1, o3-mini, o3, o4-mini)

Моделите от серия O имат уникални ограничения на параметрите при миграция към Responses API.

### Съответствие на параметрите за серия O

| Chat Completions (серия O) | Responses API | Бележки |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Задайте високо (4096+) — токени за разсъждение се броят към лимита |
| `reasoning_effort` | `reasoning.effort` | Оставете както е, ако е зададено (нисък/среден/висок) |
| `temperature` | Премахнете или задайте на `1` | Серия O приема само `1` |
| `top_p` | Премахнете | Не се поддържа на серия O |
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

> **Забележка**: Моделите серия O може да буферират изхода по време на разсъждение преди да изведат текстовите делти. Стриймингът работи, но първото събитие `response.output_text.delta` може да се появи след по-дълго забавяне в сравнение с GPT моделите.

## Достъп до токените за разсъждение
```python
# Моделите за разсъждение използват вътрешно разсъждение — можете да видите колко токена за разсъждение са използвани
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

> **Важно**: Използвайте `max_output_tokens=1000` (не 50–200) заради вътрешния процес на разсъждение на моделите за разсъждение. Моделът използва токени за разсъждение вътрешно преди да генерира окончателния изход.

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

- Дефинирайте функции в `tools` с **плосък формат на Responses API** — `name`, `description` и `parameters` са ключове на най-високо ниво (не вложени под `function`).
- Когато моделът поиска извикване на инструмент, изпълнете го в приложението си и включете резултата от инструмента в следващата заявка като елемент `function_call_output` в `input`.
- Поддържайте схемите минимални; валидирайте входните данни преди изпълнение.
- При `strict: true` всички свойства трябва да са в `required` и `additionalProperties: false` е задължително.

> **⚠️ `pydantic_function_tool()` е несъвместим**: Помощната функция `openai.pydantic_function_tool()` още генерира стария вложен формат на Chat Completions (`{"type": "function", "function": {"name": ...}}`). Не го използвайте с `responses.create()`. Дефинирайте схемите на инструментите ръчно или напишете обвивка за изравняване на изхода.

### Формат на дефиниция на инструмент

Responses API използва **плосък** формат на инструмента — `name`, `description`, `parameters` са ключове на най-горно ниво (не вложени под `function`).

**Преди (Chat Completions — вложено):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**След (Responses API — плоско):**
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

С `strict: true` (прилагане на схемата):
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

### Обратна връзка при повикване на инструмент (изпълнение и връщане на резултати)

Когато моделът изисква повикване на инструмент, използвайте `response.output` елементи + `function_call_output` — **не** шаблона на Chat Completions с `role: assistant` + `role: tool`.

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

    # Получете крайния отговор с резултатите от инструментите
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Примери за few-shot повиквания на инструменти

При подаване на few-shot примери за повиквания на инструменти в `input` използвайте `function_call` и `function_call_output` елементи. ID-тата трябва да започват с `fc_`.

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
# Пример за вградена уеб търсачка
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Вход с изображение

Обектите със съдържание на изображение сменят типа от `image_url` на `input_image`, а URL адресът се променя от вложен обект на плосък стринг.

### Вход с изображение — преди (Chat Completions)
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

### Вход с изображение — след (Responses API, URL)
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

### Вход с изображение — след (Responses API, base64)
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

> **Ключови промени**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (вложен обект) → `"image_url": "..."` (плосък стринг — или HTTPS URL или данни URI `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Миграция на Microsoft Agent Framework (MAF)

**Проверете версията на MAF първо** — миграцията зависи от дали използвате MAF 1.0.0+ или предварителна версия beta/rc.

За проверка: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

В MAF 1.0.0+ `OpenAIChatClient` **вече използва Responses API** — не е нужна миграция.

Ако кодът използва наследения `OpenAIChatCompletionClient` (който използва `chat.completions.create`), заменете го с `OpenAIChatClient`:

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

### MAF преди 1.0.0 (beta/rc версии)

В предишни версии на MAF `OpenAIChatClient` използваше Chat Completions. Обновете до `agent-framework-openai>=1.0.0`, където `OpenAIChatClient` по подразбиране използва Responses API.

> **Бележка**: `Agent`, `MCPStreamableHTTPTool` и останалите API от MAF остават без промяна — променя се само импортът и инстанцирането на клиентския клас.

## Миграция LangChain (`langchain-openai`)

Добавете `use_responses_api=True` към `ChatOpenAI()`. Също така актуализирайте достъпа до съдържанието на съобщенията от `.content` на `.text`.

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

# ... повикване на агент ...
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

> **Ключови промени**: (1) `use_responses_api=True` в конструктора, (2) `.content` → `.text` при съобщенията на отговора.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->