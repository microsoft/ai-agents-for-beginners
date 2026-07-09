# Responses API Cheat Sheet (Python + Azure OpenAI)

> All snippets wey dey below assume say `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` and say `client` don already initialize (make you see client setup).

## Basic request
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Client setup — EntraID (dem recommend am)
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

## Client setup — API key
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async client setup — EntraID
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

## Async client setup — EntraID wit explicit tenant (multi-tenant)

When Azure OpenAI resource dey for **different tenant** than the default one, you go pass `tenant_id` clear to the credential. Na common tin for dev/test wey developer home tenant no resemble resource tenant.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential for production (Azure Container Apps, App Service, etc.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # user-assigned managed identity
)
# AzureDeveloperCliCredential for local dev — explicit tenant_id dey very important
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Chain: try managed identity first, if e no work, use azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async client migration — before/after

Before (no dey use again):
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

After:
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

## Full sync migration — before/after

Before (old one — Azure OpenAI Chat Completions):
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

After (Responses API — Azure OpenAI v1 endpoint):
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
        print()  # new line for end
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

## Web app streaming — backend-to-frontend shape

When you dey migrate web app wey dey stream SSE/JSONL go frontend, the **backend serialization format** go change. Di new backend output make e preserve frontend access path so frontend no go need change anything.

**Before** — Chat Completions backend dey usually serialize each chunk `choices[0]` dict:
```python
# Old: di entire choice dict wey dem serialized per chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend go read: `response.delta.content` (deep path inside di choice object).

**After** — Responses API backend dey emit minimal shape wey still preserve di frontend access path same way:
```python
# New: make e emit only wetin di frontend need
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend still dey read `response.delta.content` — **no need change frontend**.

> **Key insight**: Di Responses API streaming shape (`event.type` + `event.delta`) different well-well from Chat Completions (`chunk.choices[0].delta.content`). But na your own backend-to-frontend contract you fit define. Shape your backend output make e match wetin frontend dey expect already.

## Streaming event sequence

When `stream: true`, the API dey emit events in dis order:
1. `response.created` – response object don initialize
2. `response.in_progress` – generation don start
3. `response.output_item.added` – output item don create
4. `response.content_part.added` – content part don start
5. `response.output_text.delta` – text chunks (plenty, each get `delta: string`)
6. `response.output_text.done` – text generation done
7. `response.content_part.done` – content part finish
8. `response.output_item.done` – output item finish
9. `response.completed` – full response complete

For simple text streaming, make you handle only `response.output_text.delta` (text chunks) and `response.completed` (finish).

## Streaming error handling for web apps

When you dey stream for web app, make you wrap async iteration for `try/except` then yield errors as JSON so frontend fit show am well (like rate limits, transient wahala):

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

> **Why dis matter**: Azure OpenAI go return `429 Too Many Requests` when e dey limit rate don choke. If no get `try/except`, di streaming response go just stop without any info. But with am, frontend go get `{"error": "Too Many Requests"}` and fit show retry prompt.

## Streaming event types (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Conversation format
```python
# Di Responses API dey support conversation format wit input array
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

## Content filter error handling

Di error body structure don change from Chat Completions go Responses API.

Before (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

After (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Key differences:
- `innererror` wrapper don **disappear** — content filter details dey top level for `error.body`.
- `content_filter_result` (singular) don turn `content_filters` (plural array) wey get `content_filter_results` (plural) inside each entry.
- Every entry for `content_filters` get `blocked`, `source_type`, and `content_filter_results` with details for each category (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Full Responses API content filter error body shape:
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

If your app dey call Azure OpenAI REST directly without SDK:

Before (Chat Completions):
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

After (Responses API):
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

> **Note**: `output_text` na convenience property for the Python SDK `Response` object. The raw REST JSON response no get `output_text` top-level field — text dey for `output[0].content[0].text`.

## Multi-turn conversation
```python
# Build wan tin wea go be like conversation wit Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Add di assistant answer come inside di conversation
messages.append({"role": "assistant", "content": response.output_text})

# Make di conversation still dey go
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Content-typed multi-turn (explicit `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turn with `previous_response_id` (alternative)

Instead of you manage the conversation array yourself, you fit chain responses
for server side with `previous_response_id`. API go store each response and
automatically add prior turns front.

```python
# Fes turn
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Next turns — jus pass di new user message + dia last response ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**When you go use which one:**

| Approach | Pros | Cons |
|---|---|---|
| `input` array (manual) | Full control for history; you fit trim/summarize; no need store for server side (`store=False`) | More code; you dey manage di array |
| `previous_response_id` | Simpler code; automatic chaining | Need `store=True` (default); conversation dey store server-side; no fit change history between turns |

> **Migration note:** Most Chat Completions apps don dey manage dia own message array, so to convert to `input` array na more direct 1:1 migration. Use `previous_response_id` for new code or if you no need manipulate conversation history.

## O-series reasoning models (o1, o3-mini, o3, o4-mini)

O-series models get unique rules for parameters when you dey migrate go Responses API.

### Parameter mapping for o-series

| Chat Completions (o-series) | Responses API | Notes |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Set am high (4096+) — reasoning tokens dey count against limit |
| `reasoning_effort` | `reasoning.effort` | Keep as e be if e dey (low/medium/high) |
| `temperature` | Remove or set to `1` | O-series only accept `1` |
| `top_p` | Remove | Dem no support o-series |
| `seed` | Remove | No support for Responses API |

### O-series before/after

Before (Chat Completions wit o-series):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

After (Responses API):
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

> **Note**: O-series models fit buffer output during reasoning before dem start to emit text deltas. Streaming still dey work but di first `response.output_text.delta` event fit come after longer delay compared to GPT models.

## Accessing reasoning tokens
```python
# Reasoning models de use internal reasoning — you fit see how many reasoning tokens dem use
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

> **Important**: Use `max_output_tokens=1000` (no be 50–200) to cover di internal reasoning process of reasoning models. Di model dey use reasoning tokens inside before e generate final output.

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

## Tool use

- Define functions for `tools` wit di **flat Responses API format** — `name`, `description`, and `parameters` dey top level (no nest under `function`).
- When di model ask make you call tool, you go run am for your app and include di tool result for next request as `function_call_output` item inside `input`.
- Make sure schemas no too big; validate inputs before you run am.
- When you dey use `strict: true`, all properties must dey inside `required` and you must get `additionalProperties: false`.

> **⚠️ `pydantic_function_tool()` no gree**: Di `openai.pydantic_function_tool()` helper still dey generate old Chat Completions nested format (`{"type": "function", "function": {"name": ...}}`). No use am with `responses.create()`. Define your own tool schemas or write wrapper to flatten am.

### Tool definition format

Responses API dey use **flat** tool format — `name`, `description`, `parameters` dey top-level keys (no nest under `function`).

**Before (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**After (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Full example:
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

Wit `strict: true` (schema enforcement):
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
            "required": ["city_name"],       # All properties na MUST to list
            "additionalProperties": False,   # Na wetin dem require for strict mode
        },
    }
]
```

### Tool call round-trip (execute and return results)

When di model ask make you call tool, use `response.output` items + `function_call_output` — **no be** Chat Completions `role: assistant` + `role: tool` pattern.

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
    # Add di model function_call tins go conversation
    messages.extend(response.output)

    # Run each tool and add di results
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Comot final response with tool results
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Few-shot tool call examples

When you dey provide few-shot examples of tool calls inside `input`, use `function_call` and `function_call_output` items. IDs suppose begin wit `fc_`.

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
# Di built-in web search example
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Image input

Image content items change from `image_url` to `input_image`, and di URL change from one nested object to flat string.

### Image input — before (Chat Completions)
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

### Image input — after (Responses API, URL)
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

### Image input — after (Responses API, base64)
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

> **Key changes**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (nested object) → `"image_url": "..."` (flat string — fit be HTTPS URL or `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migration

**Check your MAF version first** — di migration depend on whether you dey MAF 1.0.0+ or na pre-1.0.0 beta/rc.

To check: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

For MAF 1.0.0+ `OpenAIChatClient` **don dey use Responses API** — no need migrate again.

If your codebase dey use old `OpenAIChatCompletionClient` (wey dey use `chat.completions.create`), replace am wit `OpenAIChatClient`:

Before:
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

After:
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

For pre-1.0.0 MAF, `OpenAIChatClient` dey use Chat Completions. Upgrade to `agent-framework-openai>=1.0.0` where `OpenAIChatClient` use Responses API by default.

> **Note**: `Agent`, `MCPStreamableHTTPTool`, plus other MAF APIs still remain same — only di client class import and how you instantiate e dey change.

## LangChain (`langchain-openai`) migration

Add `use_responses_api=True` inside `ChatOpenAI()`. Also update message content access from `.content` to `.text`.

Before:
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

# ... agent tok ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

After:
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

# ... agent tok am ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Key changes**: (1) `use_responses_api=True` dey for constructor, (2) `.content` change to `.text` on response messages.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->