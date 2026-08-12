# Responses API ਚੀਟ ਸ਼ੀਟ (Python + Azure OpenAI)

> ਹੇਠਾਂ ਦਿੱਤੇ ਸਾਰੇ ਸਨਿੱਪੇਟ فرض کرتے ہیں کہ `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ਅਤੇ `client` ਪਹਿਲਾਂ ਹੀ ਸ਼ੁਰੂ ਕੀਤਾ ਗਿਆ ਹੈ ( ਵੇਖੋ client ਸੈਟਅਪ ).

## ਮੁੱਢਲਾ ਬੇਨਤੀ
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## ਕਲਾਇੰਟ ਸੈਟਅਪ — ਐਂਟਰਾID (ਸਿਫਾਰਸ਼ੀ)
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

## ਕਲਾਇੰਟ ਸੈਟਅਪ — API ਕੁੰਜੀ
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## ਐਸਿੰਕ ਕਲਾਇੰਟ ਸੈਟਅਪ — ਐਂਟਰਾID
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

## ਐਸਿੰਕ ਕਲਾਇੰਟ ਸੈਟਅਪ — ਸਪਸ਼ਟ ਟੇਨੈਂਟ ਨਾਲ ਐਂਟਰਾID (ਮਲਟੀ-ਟੇਨੈਂਟ)

ਜਦੋਂ Azure OpenAI ਸਰੋਤ ਮੂਲ ਟੇਨੈਂਟ ਤੋਂ **ਵੱਖਰਾ ਟੇਨੈਂਟ** ਵਿੱਚ ਹੁੰਦਾ ਹੈ, ਤਾਂ `tenant_id` ਨੂੰ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ ਕਰੈਡੈਂਸ਼ੀਅਲ ਨੂੰ ਪਾਸ ਕਰੋ। ਇਹ ਆਮ ਤੌਰ 'ਤੇ ਵਿਕਾਸ/ਟੈਸਟ ਸਥਿਤੀਆਂ ਵਿੱਚ ਹੁੰਦਾ ਹੈ ਜਿੱਥੇ ਡਿਵੈਲਪਰ ਦਾ ਹੌਮ ਟੇਨੈਂਟ ਸਰੋਤ ਟੇਨੈਂਟ ਤੋਂ ਵੱਖਰਾ ਹੁੰਦਾ ਹੈ।

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ਉਤਪਾਦਨ ਲਈ ManagedIdentityCredential (Azure Container Apps, App Service, ਆਦਿ)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # ਯੂਜ਼ਰ-ਅਸਾਈਨਡ ਮੈਨੇਜਡ ਆਈਡੈਂਟਿਟੀ
)
# ਸਥਾਨਕ ਵਿਕਾਸ ਲਈ AzureDeveloperCliCredential — ਸਪਸ਼ਟ tenant_id ਜ਼ਰੂਰੀ ਹੈ
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# ਚੇਨ: ਪਹਿਲਾਂ managed identity ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ, ਫਿਰ azd CLI 'ਤੇ ਵਾਪਸੀ ਕਰੋ
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## ਐਸਿੰਕ ਕਲਾਇੰਟ ਮਾਈਗ੍ਰੇਸ਼ਨ — ਪਹਿਲਾਂ/ਬਾਅਦ

ਪਹਿਲਾਂ (ਪੁਰਾਣਾ):
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

ਬਾਅਦ:
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

## ਪੂਰੀ ਸਿੰਕ ਮਾਈਗ੍ਰੇਸ਼ਨ — ਪਹਿਲਾਂ/ਬਾਅਦ

ਪਹਿਲਾਂ (ਪੁਰਾਣਾ — Azure OpenAI ਚੈਟ ਪੂਰੀਆਂ):
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

ਬਾਅਦ (Responses API — Azure OpenAI v1 ਐਂਡਪੋਇੰਟ):
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

## ਸਟ੍ਰੀਮਿੰਗ (ਸਿੰਕ)
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
        print()  # ਅੰਤ ਵਿੱਚ ਨਵਾਂ ਲਾਈਨ
```

## ਸਟ੍ਰੀਮਿੰਗ (ਐਸਿੰਕ)
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

## ਵੈੱਬ ਐਪ ਸਟ੍ਰੀਮਿੰਗ — ਬੈਕੈਂਡ ਤੋਂ ਫਰੰਟਏਂਡ ਸ਼ੇਪ

ਜਦੋਂ ਵੈੱਬ ਐਪ ਜੋ SSE/JSONL ਸਟ੍ਰੀਮ ਕਰਦਾ ਹੈ ਨੂੰ ਫਰੰਟਏਂਡ ਵੱਲ ਮਾਈਗ੍ਰੇਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਤਾਂ **ਬੈਕੈਂਡ ਸੀਰੀਅਲਾਈਜ਼ੇਸ਼ਨ ਫਾਰਮੈਟ** ਬਦਲ ਜਾਂਦਾ ਹੈ। ਨਵੇਂ ਬੈਕੈਂਡ ਆਉਟਪੁੱਟ ਨੂੰ ਡਿਜ਼ਾਈਨ ਕਰੋ ਤਾਂ ਕਿ ਫਰੰਟਏਂਡ ਦੇ ਮੌਜੂਦਾ ਐਕਸੈਸ ਪੈਟਰਨਾਂ ਨੂੰ ਬਚਾਇਆ ਜਾ ਸਕੇ ਤਾਂ ਜੋ ਫਰੰਟਏਂਡ ਵਿੱਚ ਕੋਈ ਬਦਲਾਵ ਦੀ ਲੋੜ ਨਾ ਪਏ।

**ਪਹਿਲਾਂ** — ਚੈਟ ਪੂਰੀਆਂ ਬੈਕੈਂਡ ਆਮ ਤੌਰ 'ਤੇ ਹਰ ਚੰਕ ਦਾ `choices[0]` ਡਿਕਸ਼ਨਰੀ ਸੀਰੀਅਲਾਈਜ਼ ਕਰਦਾ ਸੀ:
```python
# ਪੁਰਾਣਾ: ਹਰ ਚੰਕ ਲਈ ਸੀਰੀਅਲਾਈਜ਼ਡ ਪੂਰਾ ਚੋਣ ਡਿਕਸ਼ਨਰੀ
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
ਫਰੰਟਏਂਡ ਪੜ੍ਹਦਾ ਹੈ: `response.delta.content` (ਚੋਣ ਆਬਜ਼ੈਕਟ ਦੀ ਗਹਿਰੀ ਰਾਹ).

**ਬਾਅਦ** — Responses API ਬੈਕੈਂਡ ਇਕ ਘੱਟੋ-ਘੱਟ ਸ਼ੇਪ ਜਾਰੀ ਕਰਦਾ ਹੈ ਜੋ ਉਹੀ ਫਰੰਟਏਂਡ ਐਕਸੈਸ ਰਾਹ ਬਚਾਉਂਦਾ ਹੈ:
```python
# ਨਵਾਂ: ਕੇਵਲ ਉਹੀ ਚੀਜ਼ ਭੇਜੋ ਜੋ ਫਰੰਟਐਂਡ ਨੂੰ ਲੋੜੀਂਦੀ ਹੈ
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
ਫਰੰਟਏਂਡ ਅਜੇ ਵੀ `response.delta.content` ਪੜ੍ਹਦਾ ਹੈ — **ਕੋਈ ਫਰੰਟਏਂਡ ਬਦਲਾਅ ਦੀ ਲੋੜ ਨਹੀ ਹੈ**.

> **ਮੁੱਖ ਸੂਝ**: Responses API ਸਟ੍ਰੀਮਿੰਗ ਸ਼ੇਪ (`event.type` + `event.delta`) ਬੁਨਿਆਦੀ ਤੌਰ 'ਤੇ ਚੈਟ ਪੂਰੀਆਂ (`chunk.choices[0].delta.content`) ਤੋਂ ਵੱਖਰਾ ਹੈ। ਪਰ ਤੁਹਾਡਾ ਬੈਕੈਂਡ-ਫਰੰਟਏਂਡ ਕੰਟ੍ਰੈਕਟ ਤੁਹਾਡੇ ਅਨੁਸਾਰ ਹੈ। ਬੈਕੈਂਡ ਆਉਟਪੁੱਟ ਨੂੰ ਉਸੇ ਅਨੁਸਾਰ ਗਠਿਤ ਕਰੋ ਜੋ ਫਰੰਟਏਂਡ ਪਹਿਲਾਂ ਤੋਂ ਉਮੀਦ ਕਰਦਾ ਹੈ।

## ਸਟ੍ਰੀਮਿੰਗ ਇਵੈਂਟ ਕ੍ਰਮ

ਜਦੋਂ `stream: true` ਹੁੰਦਾ ਹੈ, API ਇਨ੍ਹਾਂ ਕ੍ਰਮਾਂ ਵਿੱਚ ਇਵੈਂਟ ਜਾਰੀ ਕਰਦਾ ਹੈ:
1. `response.created` – ਜਵਾਬ ਵਸਤੂ ਸ਼ੁਰੂ ਹੋਈ
2. `response.in_progress` – ਜਨਰੇਸ਼ਨ ਸ਼ੁਰੂ ਹੋਇਆ
3. `response.output_item.added` – ਆਉਟਪੁੱਟ ਵਸਤੂ ਬਣਾਈ ਗਈ
4. `response.content_part.added` – ਸਮੱਗਰੀ ਹਿੱਸਾ ਸ਼ੁਰੂ ਹੋਇਆ
5. `response.output_text.delta` – ਲਿਖਾਈ ਚੰਕ (ਕਈ, ਹਰੇਕ ਦਾ `delta: string`)
6. `response.output_text.done` – ਲਿਖਾਈ ਜਨਰੇਸ਼ਨ ਖਤਮ ਹੋਇਆ
7. `response.content_part.done` – ਸਮੱਗਰੀ ਹਿੱਸਾ ਖਤਮ ਹੋਇਆ
8. `response.output_item.done` – ਆਉਟਪੁੱਟ ਵਸਤੂ ਖਤਮ ਹੋਈ
9. `response.completed` – ਪੂਰਾ ਜਵਾਬ ਪੂਰਾ

ਆਧਾਰਭੂਤ ਲਿਖਾਈ ਸਟ੍ਰੀਮਿੰਗ ਲਈ, ਸਿਰਫ `response.output_text.delta` (ਲਿਖਾਈ ਚੰਕ ਲਈ) ਅਤੇ `response.completed` (ਖਤਮ ਲਈ) ਨੂੰ ਹੈਂਡਲ ਕਰੋ।

## ਵੈੱਬ ਐਪ ਵਿੱਚ ਸਟ੍ਰੀਮਿੰਗ ਤਰੁੱਟੀ ਸੰਭਾਲ

ਵੈੱਬ ਐਪ ਵਿੱਚ ਸਟ੍ਰੀਮਿੰਗ ਦੌਰਾਨ, ਐਸਿੰਕ ਇਟਰੇਸ਼ਨ ਨੂੰ `try/except` ਵਿੱਚ ਲਪੇਟੋ ਅਤੇ ਤਰੁੱਟੀਆਂ ਨੂੰ JSON ਵਜੋਂ ਜਾਰੀ ਕਰੋ ਤਾਂ ਕਿ ਫਰੰਟਏਂਡ ਉਨ੍ਹਾਂ ਨੂੰ ਸੁੰਦਰਤਾ ਨਾਲ ਦਿਖਾ ਸਕੇ (ਜਿਵੇਂ ਕਿ ਰੇਟ ਸੀਮਾਵਾਂ, ਅਸਥਾਈ ਅਸਫਲਤਾਵਾਂ):

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

> **ਇਹ ਕਿਉਂ ਜ਼ਰੂਰੀ ਹੈ**: Azure OpenAI ਰੇਟ ਲਿਮਟਿੰਗ ਦੌਰਾਨ `429 Too Many Requests` ਵਾਪਸ ਕਰਦਾ ਹੈ। ਬਿਨਾਂ `try/except` ਦੇ, ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬ ਸੁਣੈਹੀ ਮੌਤ ਨੂੰ ਪਹੁੰਚਦਾ ਹੈ। ਇਸ ਦੇ ਨਾਲ, ਫਰੰਟਏਂਡ ਨੂੰ `{"error": "Too Many Requests"}` ਮਿਲਦਾ ਹੈ ਅਤੇ ਉਹ ਰੀਟ੍ਰਾਈ ਪ੍ਰਾਂਪਟ ਦਿਖਾ ਸਕਦਾ ਹੈ।

## ਸਟ੍ਰੀਮਿੰਗ ਇਵੈਂਟ ਕਿਸਮਾਂ (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## ਗੱਲਬਾਤ ਫਾਰਮੈਟ
```python
# Responses API ਇਨਪੁਟ ਐਰੇ ਰਾਹੀਂ ਗੱਲਬਾਤ ਫਾਰਮੈਟ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦੀ ਹੈ
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

## ਸਮੱਗਰੀ ਛਾਣਬੀਣ ਤਰੁੱਟੀ ਸੰਭਾਲ

ਤਰੁੱਟੀ ਬਾਡੀ ਦੀ ਬਣਤਰ ਚੈਟ ਪੂਰੀਆਂ ਤੋਂ Responses API ਵਿੱਚ ਬਦਲੀ ਹੈ।

ਪਹਿਲਾਂ (ਚੈਟ ਪੂਰੀਆਂ):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ਬਾਅਦ (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ਮੁੱਖ ਅੰਤਰ:
- `innererror` ਰੈਪਰ **ਹਟ ਗਿਆ** — ਸਮੱਗਰੀ ਛਾਣਬੀਣ ਵੇਰਵੇ ਹੁਣ `error.body` ਦੇ ਉੱਚ-ਸਤਹ ਤੇ ਹਨ।
- `content_filter_result` (ਇਕਵਚਨ) → `content_filters` (ਬਹੁਵਚਨ ਏਰੇ) ਜਿਸ ਵਿੱਚ ਹਰ ਐਂਟਰੀ ਵਿੱਚ `content_filter_results` (ਬਹੁਵਚਨ) ਸ਼ਾਮਲ ਹਨ।
- ਹਰ ਐਂਟਰੀ `content_filters` ਵਿੱਚ `blocked`, `source_type`, ਅਤੇ `content_filter_results` ਹਨ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਪ੍ਰਤੀ-ਸ਼੍ਰੇਣੀ ਵੇਰਵੇ ਹਨ (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`)।

ਪੂਰੀ Responses API ਸਮੱਗਰੀ ਛਾਣਬੀਣ ਤਰੁੱਟੀ ਬਾਡੀ ਦੀ ਬਣਤਰ:
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

## ਕੱਚਾ HTTP ਮਾਈਗ੍ਰੇਸ਼ਨ (requests/httpx)

ਜੇ ਐਪ ਸਿੱਧਾ Azure OpenAI REST ਨੂੰ ਬਿਨਾਂ SDK ਵਰਤੇ ਕਾਲ ਕਰਦੀ ਹੈ:

ਪਹਿਲਾਂ (ਚੈਟ ਪੂਰੀਆਂ):
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

ਬਾਅਦ (Responses API):
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

> **ਟਿੱਪਣੀ**: `output_text` ਪਾਇਥਨ SDK ਦੇ `Response` ਆਬਜ਼ੈਕਟ ਤੇ ਇੱਕ ਸੁਵਿਧਾ ਗੁਣ ਹੈ। ਕੱਚਾ REST JSON ਜਵਾਬ ਕੋਲ ਉੱਚ-ਸਤਹ ਦੀ `output_text` ਫੀਲਡ ਨਹੀਂ ਹੁੰਦੀ — ਲਿਖਾਈ `output[0].content[0].text` 'ਤੇ ਹੁੰਦੀ ਹੈ।

## ਮਲਟੀ-ਟਰਨ ਗੱਲਬਾਤ
```python
# Responses API ਨਾਲ ਗੱਲਬਾਤ ਬਣਾਓ
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# ਸਹਾਇਕ ਦੀ ਜਵਾਬ ਗੱਲਬਾਤ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ
messages.append({"role": "assistant", "content": response.output_text})

# ਗੱਲਬਾਤ ਜਾਰੀ ਰੱਖੋ
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

ਸਮੱਗਰੀ-ਅਧਾਰਿਤ ਮਲਟੀ-ਟਰਨ (ਸਪਸ਼ਟ `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### ਮਲਟੀ-ਟਰਨ `previous_response_id` ਰਾਹੀਂ (ਵਿਕਲਪਿਕ)

ਗੱਲਬਾਤ ਐਰੇ ਨੂੰ ਆਪਣੇ ਆਪ ਸੰਭਾਲਣ ਦੀ ਥਾਂ, ਤੁਸੀਂ ਸਰਵਰ-ਸਾਈਡ 'ਤੇ `previous_response_id` ਵਰਤ ਕੇ ਜਵਾਬਾਂ ਨੂੰ ਸੰਗ੍ਰਹਿਤ ਕਰ ਸਕਦੇ ਹੋ।
API ਹਰ ਜਵਾਬ ਨੂੰ ਸਟੋਰ ਕਰਦਾ ਹੈ ਅਤੇ ਆਪਣੇ ਆਪ ਪਹਿਲਾਂ ਦੀਆਂ ਵਾਰੀਕਾਂ ਜੋੜਦਾ ਹੈ।


```python
# ਪਹਿਲਾ ਮੋੜ
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# ਅਗਲੇ ਮੋਰ — ਸਿਰਫ ਨਵਾਂ ਉਪਭੋਗਤਾ ਸੁਨੇਹਾ + ਪਹਿਲੀ ਜਵਾਬ ID ਪਾਸ ਕਰੋ
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**ਕਦੋਂ ਕਿਹੜੀ ਵਰਤੋਂ ਕਰਨੀ ਹੈ:**

| ਢੰਗ | ਫਾਇਦੇ | ਨੁਕਸਾਨ |
|---|---|---|
| `input` ਐਰੇ (ਮੈਨੂਅਲ) | ਇਤਿਹਾਸ 'ਤੇ ਪੂਰੀ ਕਾਬੂ; ਕਟਾਈ/ਸੰਖੇਪ ਕਰ ਸਕਦੇ ਹੋ; ਸਰਵਰ-ਸਾਈਡ ਸਟੋਰੇਜ ਨਹੀਂ ਚਾਹੀਦਾ (`store=False`) | ਵਧੀਕ ਕੋਡ; ਤੁਸੀਂ ਐਰੇ ਸੰਭਾਲਦੇ ਹੋ |
| `previous_response_id` | ਸਧਾਰਣ ਕੋਡ; ਆਪੋਆਪ ਕੜੀਬੰਦੀ | `store=True` ਦੀ ਲੋੜ (ਡਿਫੌਲਟ); ਗੱਲਬਾਤ ਸਰਵਰ-ਸਾਈਡ ਸਟੋਰ; ਵਾਰੀ ਵਾਰੀ ਇਤਿਹਾਸ ਵਿੱਚ ਸੋਧ ਨਹੀਂ ਕਰ ਸਕਦੇ |

> **ਮਾਈਗ੍ਰੇਸ਼ਨ ਨੋਟ:** ਜ਼ਿਆਦਾਤਰ ਚੈਟ ਪੂਰੀਆਂ ਐਪਸ ਆਪਣੇ ਸੁਨੇਹੇ ਐਰੇ ਨੂੰ ਮੈਨੇਜ ਕਰਦੀਆਂ ਹਨ, ਇਸ ਲਈ `input` ਐਰੇ ਨੂੰ ਬਦਲਣਾ ਸਿੱਧਾ 1:1 ਮਾਈਗ੍ਰੇਸ਼ਨ ਹੈ। ਨਵੇਂ ਕੋਡ ਜਾਂ ਜਦੋਂ ਤੁਹਾਨੂੰ ਗੱਲਬਾਤ ਇਤਿਹਾਸ ਵਿੱਚ ਸੋਧ ਦੀ ਲੋੜ ਨਾ ਹੋਵੇ ਤਾਂ `previous_response_id` ਵਰਤੋਂ।

## O-ਸਿਰੀਜ਼ ਕਾਰਨ ਮਾਡਲ (o1, o3-mini, o3, o4-mini)

O-ਸਿਰੀਜ਼ ਮਾਡਲਾਂ ਨੂੰ Responses API ਨੂੰ ਮਾਈਗ੍ਰੇਟ ਕਰਨ ਵੇਲੇ ਵਿਲੱਖਣ ਪੈਰਾਮੀਟਰ ਸੀਮਾਵਾਂ ਹੁੰਦੀਆਂ ਹਨ।

### O-ਸਿਰੀਜ਼ ਲਈ ਪੈਰਾਮੀਟਰ ਨਕਸ਼ਾ

| ਚੈਟ ਪੂਰੀਆਂ (o-ਸਿਰੀਜ਼) | Responses API | ਨੋਟਸ |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | ਵਧੀਆ ਤੌਰ 'ਤੇ ਉੱਚਾ ਕਰੋ (4096+) — ਕਾਰਨ ਟੋਕਨ ਹੱਦ ਵਿੱਚ ਸ਼ਾਮਲ |
| `reasoning_effort` | `reasoning.effort` | ਮੌਜੂਦ ਹੈ ਤਾਂ ਆਉਸੇ ਹੀ ਰੱਖੋ (ਘੱਟ/ਦਰਮਿਆਨਾ/ਵੱਧ) |
| `temperature` | ਹਟਾਓ ਜਾਂ `1` ਤੇ ਸੈੱਟ ਕਰੋ | O-ਸਿਰੀਜ਼ ਸਿਰਫ `1` ਸਵੀਕਾਰ ਕਰਦਾ ਹੈ |
| `top_p` | ਹਟਾਓ | O-ਸਿਰੀਜ਼ ਸਪੋਰਟ ਨਹੀਂ ਕਰਦਾ |
| `seed` | ਹਟਾਓ | Responses API ਵਿੱਚ ਸਪੋਰਟ ਨਹੀਂ |

### O-ਸਿਰੀਜ਼ ਪਹਿਲਾਂ/ਬਾਅਦ

ਪਹਿਲਾਂ (ਚੈਟ ਪੂਰੀਆਂ ਨਾਲ o-ਸਿਰੀਜ਼):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

ਬਾਅਦ (Responses API):
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

> **ਨੋਟ**: O-ਸਿਰੀਜ਼ ਮਾਡਲ ਕਾਰਨ ਦੇ ਦੌਰਾਨ ਟੈਕਸਟ ਡੈਲਟਾ ਜਾਰੀ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਆਉਟਪੁੱਟ ਨੂੰ ਬਫਰ ਕਰ ਸਕਦੇ ਹਨ। ਸਟ੍ਰੀਮਿੰਗ ਫਿਰ ਵੀ ਕੰਮ ਕਰਦੀ ਹੈ ਪਰ ਪਹਿਲਾ `response.output_text.delta` ਇਵੈਂਟ GPT ਮਾਡਲਾਂ ਨਾਲੋਂ ਦੇਰ ਨਾਲ ਆ ਸਕਦਾ ਹੈ।

## ਕਾਰਨ ਟੋਕਨਾਂ ਨੂੰ ਐਕਸੈਸ ਕਰਨਾ
```python
# ਦਲੀਲ ਦੇ ਮਾਡਲ ਅੰਦਰੂਨੀ ਦਲੀਲ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ — ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ ਕਿ ਕਿੰਨੇ ਦਲੀਲ ਟੋਕਨ ਵਰਤੇ ਗਏ ਸਨ
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

> **ਮਹੱਤਵਪੂਰਨ**: ਕਾਰਨ ਮਾਡਲਾਂ ਦੀ ਅੰਦਰੂਨੀ ਕਾਰਨ ਪ੍ਰਕਿਰਿਆ ਲਈ `max_output_tokens=1000` (50–200 ਨਹੀਂ) ਵਰਤੋਂ। ਮਾਡਲ ਅੰਤਿਮ ਨਤੀਜੇ ਤਿਆਰ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਅੰਦਰੂਨੀ ਕਾਰਨ ਟੋਕਨ ਵਰਤਦਾ ਹੈ।

## ਸੰਰਚਿਤ ਆਉਟਪੁੱਟ — JSON ਸਕੀਮਾ
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

## ਟੂਲ ਵਰਤੋਂ

- `tools` ਵਿੱਚ ਫੰਕਸ਼ਨ.define ਕਰੋ **ਸਧਾਰਣ Responses API ਫਾਰਮੈਟ** — ਉੱਪਰਲੇ ਪੱਧਰ ਤੇ `name`, `description`, ਅਤੇ `parameters` ( ਨਾ ਕਿ `function` ਦੇ ਹੇਠਾਂ )।
- ਜਦੋਂ ਮਾਡਲ ਟੂਲ ਕਾਲ ਕਰਨ ਲਈ ਆਖਦਾ ਹੈ, ਤਾਂ ਇਹ ਤੁਹਾਡੇ ਐਪ ਵਿੱਚ ਚਲਾਓ ਅਤੇ ਅਗਲੀ ਬੇਨਤੀ ਵਿੱਚ `function_call_output` ਵਸਤੂ ਵਜੋਂ ਸ਼ਾਮਲ ਕਰੋ।
- ਸਕੀਮਾਂ ਨੂੰ ਘੱਟੋ-ਘੱਟ ਰੱਖੋ; ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇਨਪੁੱਟ ਦੀ ਜਾਂਚ ਕਰੋ।
- ਜਦੋਂ `strict: true` ਵਰਤਦੇ ਹੋ, ਸਾਰੀਆਂ ਪ੍ਰਾਪਰਟੀਜ਼ `required` ਵਿੱਚ ਦਰਜ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ ਅਤੇ `additionalProperties: false` ਲਾਜ਼ਮੀ ਹੈ।

> **⚠️ `pydantic_function_tool()` ਅਣਕੰਪੈਟੀਬਲ ਹੈ**: `openai.pydantic_function_tool()` ਹੇਲਪਰ ਪੁਰਾਣੇ ਚੈਟ ਪੂਰੀਆਂ ਨੇਸਟਫਾਰਮੈਟ ( `{"type": "function", "function": {"name": ...}}` ) ਅਜੇ ਵੀ ਜਨਰੇਟ ਕਰਦਾ ਹੈ। ਇਸਨੂੰ `responses.create()` ਨਾਲ ਨਾ ਵਰਤੋਂ। ਟੂਲ ਸਕੀਮਾਂ ਮੈਨੁਅਲੀ ਡਿਫਾਈਨ ਕਰੋ ਜਾਂ ਆਉਟਪੁੱਟ ਨੂੰ ਫਲੈਟ ਕਰਨ ਲਈ ਰੈਪਪਰ ਲਿਖੋ।

### ਟੂਲ ਪਰਿਭਾਸ਼ਾ ਫਾਰਮੈਟ

Responses API ਇੱਕ **ਸਧਾਰਣ** ਟੂਲ ਫਾਰਮੈਟ ਵਰਤਦਾ ਹੈ — `name`, `description`, `parameters` ਸਿੱਧੇ ਉੱਪਰਲੇ ਪੱਧਰ ਦੀਆਂ ਕੁੰਜੀਆਂ ਹਨ ( ਨਾ ਕਿ `function` ਦੇ ਅੰਦਰ )।

**ਪਹਿਲਾਂ (ਚੈਟ ਪੂਰੀਆਂ — ਨੇਸਟ):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**ਬਾਅਦ (Responses API — ਸਧਾਰਣ):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

ਪੂਰਾ ਉਦਾਹਰਨ:
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

`strict: true` ਨਾਲ (ਸਕੀਮਾ ਲਾਗੂ ਕਰਨ):
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
            "required": ["city_name"],       # ਸਾਰੀਆਂ ਸੰਪੱਤੀਆਂ ਦੀ ਸੂਚੀ ਦਿੰਨੀ ਜ਼ਰੂਰੀ ਹੈ
            "additionalProperties": False,   # ਸਖ਼ਤ ਮੋਡ ਲਈ ਲਾਜ਼ਮੀ ਹੈ
        },
    }
]
```

### ਟੂਲ ਕਾਲ ਰਾਊਂਡ-ਟਰਿਪ (ਚਲਾਉਣਾ ਅਤੇ ਨਤੀਜੇ ਵਾਪਸ ਕਰਨਾ)

ਜਦੋਂ ਮਾਡਲ ਟੂਲ ਕਾਲ ਦੀ ਬੇਨਤੀ ਕਰਦਾ ਹੈ, `response.output` ਵਸਤੂਆਂ + `function_call_output` ਵਰਤੋਂ — **ਨਹੀਂ** ਚੈਟ ਪੂਰੀਆਂ `role: assistant` + `role: tool` ਪੈਟਰਨ।

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
    # ਮਾਡਲ ਦੇ function_call ਆਈਟਮਾਂ ਨੂੰ ਗੱਲਬਾਤ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ
    messages.extend(response.output)

    # ਹਰ ਇੱਕ ਟੂਲ ਨੂੰ ਚਲਾਓ ਅਤੇ ਨਤੀਜੇ ਸ਼ਾਮਲ ਕਰੋ
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # ਟੂਲ ਦੇ ਨਤੀਜਿਆਂ ਨਾਲ ਅਖੀਰਲਾ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰੋ
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### ਕੁਝ ਉਦਾਹਰਨਾਂ ਟੂਲ ਕਾਲ ਦੀਆਂ (few-shot)

ਜਦੋਂ `input` ਵਿੱਚ ਕੁਝ ਉਦਾਹਰਨਾਂ ਦੇਂਦਿਆਂ ਟੂਲ ਕਾਲ ਦੀਆਂ, `function_call` ਅਤੇ `function_call_output` ਵਸਤੂਆਂ ਵਰਤੋਂ। IDਆਂ ਦੀ ਸ਼ੁਰੂਆਤ `fc_` ਨਾਲ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।

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
# ਬਿਲਟ-ਇਨ ਵੈੱਬ ਖੋਜ ਉਦਾਹਰਨ
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## ਚਿੱਤਰ ਇਨਪੁੱਟ

ਚਿੱਤਰ ਸਮੱਗਰੀ ਵਸਤੂਆਂ ਦੀ ਕਿਸਮ `image_url` ਤੋਂ `input_image` ਹੋ ਗਈ ਹੈ, ਅਤੇ URL ਲਕੀਰ ਬਸਤੂ ਤੋਂ ਸਧੀ ਸਤਰਗੀ ਸਟ੍ਰਿੰਗ ਵਿੱਚ ਬਦਲ ਗਈ ਹੈ।

### ਚਿੱਤਰ ਇਨਪੁੱਟ — ਪਹਿਲਾਂ (ਚੈਟ ਪੂਰੀਆਂ)
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

### ਚਿੱਤਰ ਇਨਪੁੱਟ — ਬਾਅਦ (Responses API, URL)
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

### ਚਿੱਤਰ ਇਨਪੁੱਟ — ਬਾਅਦ (Responses API, base64)
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

> **ਮੁੱਖ ਬਦਲਾਅ**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (ਨੇਸਟ ਆਬਜੈਕਟ) → `"image_url": "..."` (ਸਧਾਰਣ ਸਤਰਗੀ — HTTPS URL ਜਾਂ `data:image/...;base64,...` ਡੇਟਾ URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft ਏਜੰਟ ਫਰੇਮਵਰਕ (MAF) ਮਾਈਗ੍ਰੇਸ਼ਨ

**ਪਹਿਲਾਂ ਆਪਣੀ MAF ਵਰਜ਼ਨ ਜਾਂਚੋ** — ਮਾਈਗ੍ਰੇਸ਼ਨ ਇਸ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ ਕਿ ਤੁਸੀਂ MAF 1.0.0+ ਜਾਂ ਪਹਿਲਾਂ ਦਾ pre-1.0.0 ਬੇਟਾ/ਕੈਪੀਆਰ ਉਪਯੋਗ ਕਰ ਰਹੇ ਹੋ।

ਜਾਂਚ ਕਰਨ ਲਈ: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ ਵਿੱਚ, `OpenAIChatClient` ਪਹਿਲਾਂ ਹੀ Responses API ਵਰਤਦਾ ਹੈ — ਕੋਈ ਮਾਈਗ੍ਰੇਸ਼ਨ ਦੀ ਲੋੜ ਨਹੀਂ।

ਜੇ ਕੋਡਬੇਸ ਲੈਗੇਸੀ `OpenAIChatCompletionClient` (ਜੋ `chat.completions.create` ਵਰਤਦਾ ਹੈ) ਵਰਤਦਾ ਹੈ, ਤਾਂ ਇਸਦੀ ਥਾਂ `OpenAIChatClient` ਵਰਤੋਂ:

ਪਹਿਲਾਂ:
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

ਬਾਅਦ:
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

### MAF pre-1.0.0 (ਬੇਟਾ/ਕੈਪੀਆਰ ਰਿਲੀਜ਼)

pre-1.0.0 MAF ਵਿੱਚ, `OpenAIChatClient` ਚੈਟ ਪੂਰੀਆਂ ਵਰਤਦਾ ਸੀ। ਅੱਪਗ੍ਰੇਡ ਕਰੋ `agent-framework-openai>=1.0.0` ਤੇ ਜਿੱਥੇ `OpenAIChatClient` ਮੂਲ ਰੂਪ ਵਿੱਚ Responses API ਵਰਤਦਾ ਹੈ।

> **ਨੋਟ**: `Agent`, `MCPStreamableHTTPTool`, ਅਤੇ ਹੋਰ MAF API ਬਦਲੇ ਨਹੀਂ — ਸਿਰਫ ਕਲਾਇੰਟ ਕਲਾਸ ਦੀ ਆਯਾਤ ਅਤੇ ਨਿਰਮਾਣ ਬਦਲਦਾ ਹੈ।

## LangChain (`langchain-openai`) ਮਾਈਗ੍ਰੇਸ਼ਨ

`ChatOpenAI()` ਵਿੱਚ `use_responses_api=True` ਸ਼ਾਮਲ ਕਰੋ। ਨਾਲ ਹੀ ਸੁਨੇਹੇ ਸਮੱਗਰੀ ਐਕਸੈਸ `.content` ਤੋਂ `.text` 'ਤੇ ਬਦਲੋ।

ਪਹਿਲਾਂ:
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

# ... ਏਜੰਟ ਕਾਲ ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

ਬਾਅਦ:
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

# ... ਏਜੰਟ ਸੱਦਾ ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **ਮੁੱਖ ਬਦਲਾਅ**: (1) ਕਨਸਟਰਕਟਰ ਵਿੱਚ `use_responses_api=True`, (2) ਜਵਾਬ ਸੁਨੇਹਿਆਂ ਤੇ `.content` → `.text`।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->