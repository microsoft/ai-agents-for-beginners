# Responses API Cheat Sheet (Python + Azure OpenAI)

> Lahat ng mga snippet sa ibaba ay ina-assume ang `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` at ang `client` ay naka-initialize na (tingnan ang client setup).

## Pangunahing request
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Pag-setup ng client — EntraID (inirerekomenda)
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

## Pag-setup ng client — API key
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async na pag-setup ng client — EntraID
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

## Async na pag-setup ng client — EntraID na may explicit na tenant (multi-tenant)

Kapag ang Azure OpenAI resource ay nasa **ibang tenant** kaysa sa default, ipasa ang `tenant_id` nang tahasan sa credential. Karaniwan ito sa mga dev/test na scenario kung saan ang home tenant ng developer ay naiiba sa resource tenant.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential para sa produksyon (Azure Container Apps, App Service, atbp.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # user-assigned managed identity
)
# AzureDeveloperCliCredential para sa lokal na dev — mahalaga ang explicit tenant_id
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Chain: subukan muna ang managed identity, pagkatapos ay bumalik sa azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async na migration ng client — bago/after

Bago (deprecated):
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

Pagkatapos:
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

## Buong sync migration — bago/after

Bago (legacy — Azure OpenAI Chat Completions):
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

Pagkatapos (Responses API — Azure OpenAI v1 endpoint):
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

## Streaming (sync)
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
        print()  # bagong linya sa dulo
```

## Streaming (async)
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

## Web app streaming — backend-to-frontend na anyo

Kapag nagmi-migrate ng web app na nag-i-stream ng SSE/JSONL papunta sa frontend, nagbabago ang **backend serialization format**. Disenyuhin ang bagong backend output upang mapanatili ang umiiral na access patterns ng frontend upang walang kailangang baguhin sa frontend.

**Bago** — Karaniwang sine-serialize ng Chat Completions backend ang bawat chunk na `choices[0]` dict:
```python
# Lumang: naka-serialize na buong diksyunaryo ng pagpipilian bawat chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Binabasa ng frontend: `response.delta.content` (malalim na path sa choice object).

**Pagkatapos** — Nagbubuga ang Responses API backend ng minimal na anyo na pinapanatili ang parehong access path ng frontend:
```python
# Bago: i-emit lamang ang kailangan ng frontend
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Binabasa pa rin ng frontend ang `response.delta.content` — **walang kailangang pagbabago sa frontend**.

> **Pangunahing pananaw**: Ang streaming shape ng Responses API (`event.type` + `event.delta`) ay radikal na iba sa Chat Completions (`chunk.choices[0].delta.content`). Ngunit ang kontrata ng backend-to-frontend ay nasa inyo para idefine. I-ayos ang backend output para tumugma sa inaasahan ng frontend.

## Sekwensya ng streaming event

Kapag `stream: true`, nagpapadala ang API ng mga event sa ganitong ayos:
1. `response.created` – na-initialize ang response object
2. `response.in_progress` – nagsimula ang generation
3. `response.output_item.added` – nilikha ang output item
4. `response.content_part.added` – nagsimula ang content part
5. `response.output_text.delta` – mga text chunk (marami, bawat isa ay may `delta: string`)
6. `response.output_text.done` – natapos ang text generation
7. `response.content_part.done` – natapos ang content part
8. `response.output_item.done` – natapos ang output item
9. `response.completed` – kumpleto na ang buong response

Para sa basic na text streaming, i-handle lamang ang `response.output_text.delta` (para sa mga text chunk) at `response.completed` (para sa pagtapos).

## Pag-handle ng streaming error sa mga web app

Kapag nagst-stream sa web app, i-wrap ang async iteration sa `try/except` at i-yield ang mga error bilang JSON upang maipakita ng frontend ng maayos (hal., rate limits, pansamantalang mga failure):

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

> **Bakit ito mahalaga**: Nagbabalik ang Azure OpenAI ng `429 Too Many Requests` kapag rate limiting. Kung walang `try/except`, tahimik na titigil ang streaming response. Kung meron, makakatanggap ang frontend ng `{"error": "Too Many Requests"}` at maaaring ipakita ang retry prompt.

## Mga uri ng streaming event (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Format ng pag-uusap
```python
# Sinusuportahan ng Responses API ang format ng pag-uusap sa pamamagitan ng input array
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

## Pag-handle ng content filter error

Nagbago ang istruktura ng error body mula Chat Completions papuntang Responses API.

Bago (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Pagkatapos (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Mga pangunahing pagkakaiba:
- Wala na ang `innererror` wrapper — ngayon nasa top level ng `error.body` ang detalye ng content filter.
- `content_filter_result` (isahan) → `content_filters` (maramihang array) na naglalaman ng `content_filter_results` (maramihan) sa bawat entry.
- Bawat entry sa `content_filters` ay may kasamang `blocked`, `source_type`, at `content_filter_results` na may detalye para sa bawat kategorya (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Buong istruktura ng content filter error body ng Responses API:
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

## Raw HTTP migration (requests/httpx)

Kung ang app ay tumatawag nang direkta sa Azure OpenAI REST imbes na gumamit ng SDK:

Bago (Chat Completions):
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

Pagkatapos (Responses API):
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

> **Tandaan**: Ang `output_text` ay convenience property sa Python SDK na `Response` object. Ang raw REST JSON response ay walang top-level na `output_text` field — ang teksto ay nasa `output[0].content[0].text`.

## Multi-turn na pag-uusap
```python
# Bumuo ng isang pag-uusap gamit ang Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Idagdag ang tugon ng katulong sa pag-uusap
messages.append({"role": "assistant", "content": response.output_text})

# Ipagpatuloy ang pag-uusap
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Content-typed multi-turn (tahasan na `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turn gamit ang `previous_response_id` (alternatibo)

Sa halip na ikaw ang mag-manage ng conversation array, maaari mong i-chain ang mga response
server-side gamit ang `previous_response_id`. Ini-store ng API ang bawat response at
awtomatikong dinadagdag ang mga naunang turn.

```python
# Unang liko
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Mga sumunod na liko — ipasa lamang ang bagong mensahe ng user + nakaraang ID ng tugon
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kailan gagamitin ang alin:**

| Paraan | Pros | Cons |
|---|---|---|
| `input` array (manu-manong) | Buong kontrol sa history; pwedeng mag-trim/summarize; walang server-side storage na kailangan (`store=False`) | Mas maraming code; ikaw ang nag-manage ng array |
| `previous_response_id` | Mas simpleng code; awtomatikong chaining | Nangangailangan ng `store=True` (default); naka-store ang conversation server-side; hindi pwedeng baguhin ang history sa pagitan ng mga turn |

> **Tandaan sa migration:** Karamihan sa mga Chat Completions app ay nagma-manage na ng sarili nilang message array, kaya ang pag-convert sa `input` array ay mas direct na 1:1 migration. Gamitin ang `previous_response_id` para sa bagong code o kapag hindi mo kailangan i-manipula ang history ng conversation.

## O-series na reasoning models (o1, o3-mini, o3, o4-mini)

May mga natatanging parameter constraints ang O-series models kapag nagmi-migrate papunta sa Responses API.

### Pagtutugma ng parameter para sa o-series

| Chat Completions (o-series) | Responses API | Mga Tala |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | I-set ng mataas (4096+) — binibilang ng reasoning tokens ang limit |
| `reasoning_effort` | `reasoning.effort` | Panatilihin kung meron (low/medium/high) |
| `temperature` | Alisin o i-set sa `1` | Tinatanggap lang ng o-series ang `1` |
| `top_p` | Alisin | Hindi supported sa o-series |
| `seed` | Alisin | Hindi supported sa Responses API |

### O-series bago/after

Bago (Chat Completions gamit ang o-series):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Pagkatapos (Responses API):
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

> **Tandaan**: Posibleng mag-buffer ng output ang O-series models habang nage-effort sa reasoning bago maglabas ng text deltas. Gumagana pa rin ang streaming pero maaaring dumating nang mas matagal ang unang `response.output_text.delta` event kumpara sa GPT models.

## Pag-access sa reasoning tokens
```python
# Ang mga reasoning model ay gumagamit ng panloob na pangangatwiran — makikita mo kung gaano karaming reasoning tokens ang nagamit
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

> **Mahalaga**: Gumamit ng `max_output_tokens=1000` (hindi 50–200) para isaisip ang internal na proseso ng reasoning ng models. Gumagamit ang model ng reasoning tokens nang internal bago bumuo ng huling output.

## Structured output — JSON Schema
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

## Paggamit ng tool

- Magdefine ng mga function sa `tools` gamit ang **flat Responses API format** — `name`, `description`, at `parameters` ay nasa top level (hindi nakapaloob sa `function`).
- Kapag ang model ay humiling ng tool call, isagawa ito sa iyong app at isama ang resulta ng tool sa susunod na request bilang `function_call_output` item sa loob ng `input`.
- Panatilihing minimal ang mga schema; i-validate muna ang inputs bago i-execute.
- Kapag gumagamit ng `strict: true`, lahat ng properties ay kailangang nakalista sa `required` at mandatory ang `additionalProperties: false`.

> **⚠️ Hindi compatible ang `pydantic_function_tool()`**: Ang `openai.pydantic_function_tool()` helper ay gumagawa pa rin ng lumang Chat Completions nested format (`{"type": "function", "function": {"name": ...}}`). Huwag gamitin ito sa `responses.create()`. Mag-define ng tool schemas nang mano-mano o gumawa ng wrapper para gawing flat ang output.

### Format ng tool definition

Ginagamit ng Responses API ang **flat** na format para sa mga tool — ang `name`, `description`, `parameters` ay mga top-level key (hindi nasa loob ng `function`).

**Bago (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Pagkatapos (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Buong halimbawa:
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

Kapag `strict: true` (pagpapatupad ng schema):
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
            "required": ["city_name"],       # Lahat ng mga ari-arian AY DAPAT na nakalista
            "additionalProperties": False,   # Kailangan para sa mahigpit na mode
        },
    }
]
```

### Round-trip ng tool call (ipatupad at ibalik ang mga resulta)

Kapag humiling ang model ng tool call, gamitin ang `response.output` items + `function_call_output` — **hindi** ang Chat Completions `role: assistant` + `role: tool` pattern.

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
    # Idagdag ang mga item ng function_call ng modelo sa pag-uusap
    messages.extend(response.output)

    # Isagawa ang bawat tool at idagdag ang mga resulta
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Kunin ang huling tugon kasama ang mga resulta ng tool
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Mga halimbawa ng few-shot tool call

Kapag nagbibigay ng few-shot na halimbawa ng tool calls sa `input`, gamitin ang `function_call` at `function_call_output` items. Dapat magsimula ang mga ID sa `fc_`.

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
# Halimbawa ng naka-built-in na paghahanap sa web
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Pag-input ng imahe

Nagbabago ang mga image content item mula sa `image_url` patungong `input_image`, at ang URL ay nagiging flat string mula sa nested object.

### Pag-input ng imahe — bago (Chat Completions)
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

### Pag-input ng imahe — pagkatapos (Responses API, URL)
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

### Pag-input ng imahe — pagkatapos (Responses API, base64)
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

> **Pangunahing pagbabago**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (nested object) → `"image_url": "..."` (flat string — maaaring HTTPS URL o `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migration

**Suriin muna ang bersyon ng MAF** — nakadepende ang migration kung ikaw ay nasa MAF 1.0.0+ o pre-1.0.0 beta/rc.

Para suriin: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Sa MAF 1.0.0+, ang `OpenAIChatClient` **ay gumagamit na ng Responses API** — walang migration na kailangan.

Kung ang codebase ay gumagamit ng legacy na `OpenAIChatCompletionClient` (na gumagamit ng `chat.completions.create`), palitan ito ng `OpenAIChatClient`:

Bago:
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

Pagkatapos:
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

### MAF pre-1.0.0 (beta/rc releases)

Sa pre-1.0.0 na MAF, ang `OpenAIChatClient` ay gumagamit pa ng Chat Completions. I-upgrade sa `agent-framework-openai>=1.0.0` kung saan ang `OpenAIChatClient` ay default na gumagamit ng Responses API.

> **Tandaan**: Ang `Agent`, `MCPStreamableHTTPTool`, at iba pang MAF API ay nananatiling hindi nagbabago — ang import at pag-instantiate lamang ng client class ang nagbabago.

## LangChain (`langchain-openai`) migration

Magdagdag ng `use_responses_api=True` sa `ChatOpenAI()`. I-update rin ang pag-access ng message content mula `.content` patungong `.text`.

Bago:
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

# ... pagtawag ng ahente ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Pagkatapos:
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

# ... pagtawag ng ahente ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Pangunahing pagbabago**: (1) `use_responses_api=True` sa constructor, (2) `.content` → `.text` sa response messages.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->