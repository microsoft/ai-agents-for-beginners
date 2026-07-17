# Водич за Responses API (Python + Azure OpenAI)

> Сви примери у наставку претпостављају `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` и да је `client` већ иницијализован (погледајте подешавање клијента).

## Основни захтев
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Подешавање клијента — EntraID (препоручено)
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

## Подешавање клијента — API кључ
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Асинхроно подешавање клијента — EntraID
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

## Асинхроно подешавање клијента — EntraID са изричитим tenant-ом (више-tenant)

Када је Azure OpenAI ресурс у **другом tenant-у** у односу на подразумевани, проследите `tenant_id` изричито у credential. Ово је уобичајено у развојним/тест сценаријима где се кућни tenant програмера разликује од tenant-а ресурса.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential за продукцију (Azure Container Apps, App Service, итд.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # кориснички додељени управљани идентитет
)
# AzureDeveloperCliCredential за локални развој — експлицитан tenant_id је кључан
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Ланац: прво покушај управљани идентитет, у супротном азд CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Асинхрона миграција клијента — пре/после

Пре (застарело):
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

## Потпуна синхрона миграција — пре/после

Пре (легоци — Azure OpenAI Chat Completions):
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

После (Responses API — Azure OpenAI v1 крајња тачка):
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

## Стреаминг (синхрони)
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
        print()  # нови ред на крају
```

## Стреаминг (асинхрони)
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

## Веб апликација стреаминг — облик са позадине ка фронтенду

Код миграције веб апликације која стримује SSE/JSONL ка фронтенду, **формат серријализације позадине** се мења. Дизајнирајте нови излаз са позадине тако да сачува постојеће приступне обрасце фронтенда како фронтенд не би требало да мења ништа.

**Пре** — Chat Completions позадина типично серијализује `choices[0]` речник сваког дела:
```python
# Старо: серијализован цео речник избора по делићу
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Фронтенд чита: `response.delta.content` (дубок пут у објекту choice).

**После** — Responses API позадина емитује минималан облик који задржава исти приступ фронтенда:
```python
# Нова функција: емитуј само оно што је потребно за фронтенд
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Фронтенд и даље чита `response.delta.content` — **није потребна промена фронтенда**.

> **Кључна поента**: Streaming облик Responses API (`event.type` + `event.delta`) је суштински другачији од Chat Completions (`chunk.choices[0].delta.content`). Али уговор између позадине и фронтенда је на вама да дефинишете. Облик излаза позадине прилагодите ономе што фронтенд већ очекује.

## Предмет редоследа стриминг догађаја

Када је `stream: true`, API емитује догађаје овим редоследом:
1. `response.created` – иницијализован објекат одговора
2. `response.in_progress` – започето генерисање
3. `response.output_item.added` – креиран излазни елемент
4. `response.content_part.added` – започео део садржаја
5. `response.output_text.delta` – текстуални делови (више, сваки има `delta: string`)
6. `response.output_text.done` – завршено генерисање текста
7. `response.content_part.done` – завршен део садржаја
8. `response.output_item.done` – завршен излазни елемент
9. `response.completed` – цео одговор комплетан

За основни текстуални стриминг обрадите само `response.output_text.delta` (за делове текста) и `response.completed` (за завршетак).

## Обрада грешака током стриминга у веб апликацијама

При стримовању у веб апликацији умотајте асинхроно понављање у `try/except` и емитујте грешке као JSON како би фронтенд могао пријатно да их прикаже (нпр. rate limits, транзијентни неуспеси):

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

> **Зашто је ово важно**: Azure OpenAI враћа `429 Too Many Requests` током rate лимита. Без `try/except`, стриминг одговор тихо нестане. Са њим, фронтенд добија `{"error": "Too Many Requests"}` и може приказати позив на поновни покушај.

## Типови стриминг догађаја (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Формат разговора
```python
# API за одговоре подржава формат разговора путем низа улаза
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

## Обрада грешака content filter-а

Срхт тела грешке је промењен са Chat Completions на Responses API.

Пре (Chat Completions):
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

Кључне разлике:
- `innererror` омотач је **уклоњен** — детаљи content filter-а су сада на врху у `error.body`.
- `content_filter_result` (јединачно) → `content_filters` (множествени низ) који садржи `content_filter_results` (множествени) у сваком уносу.
- Сваки унос у `content_filters` укључује `blocked`, `source_type`, и `content_filter_results` са појединачним детаљима категорија (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Потпуни облик тела грешке content filter-а у Responses API:
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

## Сирови HTTP миграција (requests/httpx)

Ако апликација позива Azure OpenAI REST директно уместо коришћења SDK:

Пре (Chat Completions):
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

> **Напомена**: `output_text` је погодна особина на Python SDK објекту `Response`. Сирови REST JSON одговор нема пољe `output_text` на врху — текст је у `output[0].content[0].text`.

## Вишесмерни разговор
```python
# Наконите разговор са Responses API-јем
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Додајте одговор асистента у разговор
messages.append({"role": "assistant", "content": response.output_text})

# Наставите разговор
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Мултитурни са типом садржаја (експлицитни `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Мултитурни преко `previous_response_id` (алтернатива)

Уместо да сами управљате низом разговора, можете повезивати одговоре
на серверској страни користећи `previous_response_id`. API чува сваки одговор и
аутоматски додаје претходне кругове.

```python
# Први потез
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Накнадни потези — само пошаљите нову поруку корисника + ИД претходног одговора
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Када користити који приступ:**

| Приступ | Предности | Манe |
|---|---|---|
| `input` низ (мануално) | Потпуна контрола историје; може се скратити/сажети; није потребно чување на серверу (`store=False`) | Више кода; ви управљате низом |
| `previous_response_id` | Једноставнији код; аутоматско повезивање | Захтева `store=True` (подразумевано); разговор се чува серверски; не може се мењати историја у току разговора |

> **Напомена о миграцији:** Већина Chat Completions апликација већ управља властитим низом порука, тако да је конверзија у `input` низ директнија миграција 1:1. Користите `previous_response_id` за нови код или кад не треба да мењате историју разговора.

## O-series модели за резоновање (o1, o3-mini, o3, o4-mini)

O-series модели имају јединствена ограничења параметара при миграцији на Responses API.

### Мапирање параметара за o-series

| Chat Completions (o-series) | Responses API | Напомене |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Поставите велико (4096+) — резоновање броји према лимиту |
| `reasoning_effort` | `reasoning.effort` | Оставите као јесте ако је присутно (low/medium/high) |
| `temperature` | Уклоните или поставите на `1` | O-series прихвата само `1` |
| `top_p` | Уклоните | Није подржано на o-series |
| `seed` | Уклоните | Није подржано у Responses API |

### O-series пре/после

Пре (Chat Completions са o-series):
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

> **Напомена**: O-series модели могу да кеширају излаз током резоновања пре емитовања текстуалних делта. Стреаминг и даље функционише, али први `response.output_text.delta` догађај може доћи са дужим кашњењем него код GPT модела.

## Приступ резоновајућим токенима
```python
# Модели расуђивања користе унутрашње расуђивање — можете видети колико је токена расуђивања коришћено
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

> **Важно**: Користите `max_output_tokens=1000` (не 50–200) да бисте узели у обзир унутрашњи процес резоновања модела. Модел користи резоновајуће токене унутар машине пре генерације коначног излаза.

## Структурирани излаз — JSON Schema
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

## Користење алата

- Дефинишите функције у `tools` помоћу **плoског формата Responses API** — кључеви `name`, `description`, и `parameters` су на врху (нису угнеждени под `function`).
- Када модел затражи позив алата, извршите га у вашој апликацији и укључите резултат алата у следећи захтев као `function_call_output` ставку унутар `input`.
- Чувајте шеме минималним; валидирајте уносе пре извршења.
- Када користите `strict: true`, све особине морају бити наведене у `required` и `additionalProperties: false` је обавезно.

> **⚠️ `pydantic_function_tool()` није компатибилан**: Помоћна функција `openai.pydantic_function_tool()` још увек генерише стари угнежђени формат Chat Completions (`{"type": "function", "function": {"name": ...}}`). Немојте је користити са `responses.create()`. Дефинишите шеме алата ручно или напишите омотач за плишавање излаза.

### Формат дефиниције алата

Responses API користи **плоски** формат алата — `name`, `description`, `parameters` су кључеви на врхунском нивоу (нису угнеждени испод `function`).

**Пре (Chat Completions — угнежђени):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**После (Responses API — плоски):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Потпуни пример:
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

Са `strict: true` (присила шеме):
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
            "required": ["city_name"],       # Сва својства МОРАЈУ бити наведена
            "additionalProperties": False,   # Захтевано за строги режим
        },
    }
]
```

### Путања позива алата (изврши и врати резултате)

Када модел тражи позив алата, користите `response.output` ставке + `function_call_output` — **не** користите Chat Completions `role: assistant` + `role: tool` образац.

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
    # Додајте функцију модела _function_call_ у разговор
    messages.extend(response.output)

    # Извршите сваки алат и додајте резултате
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Добити коначни одговор са резултатима алата
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Пример позива алата са неколико примера

Када дајете неколико примера позива алата у `input`, користите `function_call` и `function_call_output` ставке. ID-ови морају почети са `fc_`.

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
# Примера уграђене претраге на мрежи
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Унос слике

Ставке садржаја слике мењају тип са `image_url` на `input_image`, а URL се мења са угнежђеног објекта на плоски низ.

### Унос слике — пре (Chat Completions)
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

### Унос слике — после (Responses API, URL)
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

### Унос слике — после (Responses API, base64)
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

> **Кључне измене**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (угнежђени објекат) → `"image_url": "..."` (плоски низ — било HTTPS URL или `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Миграција Microsoft Agent Framework (MAF)

**Прво проверите вашу верзију MAF-а** — миграција зависи од тога да ли сте на MAF 1.0.0+ или на претходној 1.0.0 бета/rc.

Да проверите: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

У MAF 1.0.0+, `OpenAIChatClient` **већ користи Responses API** — није потребна миграција.

Ако код користи наследни `OpenAIChatCompletionClient` (који користи `chat.completions.create`), замените га са `OpenAIChatClient`:

Пре:
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

### MAF пре 1.0.0 (бета/rc издања)

У MAF претходном 1.0.0, `OpenAIChatClient` је користио Chat Completions. Надоградите на `agent-framework-openai>=1.0.0` где `OpenAIChatClient` користи Responses API подразумевано.

> **Напомена**: API-ји `Agent`, `MCPStreamableHTTPTool` и други у MAF-у остају непромењени — мењају се само увоз и инстанцирање класе клијента.

## LangChain (`langchain-openai`) миграција

Додајте `use_responses_api=True` у `ChatOpenAI()`. Такође ажурирајте приступ порукама са `.content` на `.text`.

Пре:
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

# ... позив агента ...
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

# ... позив агента ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Кључне измене**: (1) `use_responses_api=True` у конструктору, (2) `.content` → `.text` на одговорним порукама.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->