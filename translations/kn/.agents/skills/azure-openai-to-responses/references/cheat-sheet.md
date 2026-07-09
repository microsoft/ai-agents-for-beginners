# ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಚೀಟ್ ಶೀಟ್ (Python + Azure OpenAI)

> ಕೆಳಗಿನ ಎಲ್ಲ ಸ್ಲೈಸ್‌ಗಳು `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ಮತ್ತು `client` 이미 ಆರಂಭಿಸಲಾಗಿದೆ ಎಂದು ಊಹಿಸುತ್ತವೆ (ಕ್ಲೈಂಟ್ ಸೆಟಪ್ ನೋಡಿ).

## ಮೂಲ ವಿನಂತಿ
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## ಕ್ಲೈಂಟ್ ಸೆಟಪ್ — EntraID ( ಶಿವೇಷಿಸಲಾಗಿದೆ )
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

## ಕ್ಲೈಂಟ್ ಸೆಟಪ್ — API ಕೀ
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## ಅಸಿಂಕ್ ಕ್ಲೈಂಟ್ ಸೆಟಪ್ — EntraID
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

## ಅಸಿಂಕ್ ಕ್ಲೈಂಟ್ ಸೆಟಪ್ — ಖಾಸಗಿ ಭಾನುವಾರದೊಂದಿಗೆ EntraID (ಬಹು-ಟೆನಂಟ್)

Azure OpenAI ಸಂಪನ್ಮೂಲವು **ಬೇರೆಯುವ ಟೆನಂಟ್** ಆಗಿದ್ದರೆ ಡೀಫಾಲ್ಟ್‌ಗಿಂತ ಭಿನ್ನ, `tenant_id` ಅನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಕ್ರೆಡೆನ್ಶಿಯಲ್ ಗೆ ಪಾಸ್ಸ್ ಮಾಡಿ. ಇದು ಅಭಿವೃದ್ಧಿ/ಪರೀಕ್ಷೆ ಸಂದರ್ಭಗಳಲ್ಲಿ ಸಾಮಾನ್ಯ, ಅಲ್ಲಿ ಡೆವಲಪರ್‌ನ ಹೊಂಗೆ ಟೆನಂಟ್ ಸಂಪನ್ಮೂಲ ಟೆನಂಟ್‌ನಿಂದ ಭಿನ್ನವಾಗಿರುತ್ತದೆ.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ಉತ್ಪಾದನೆಗಾಗಿ ManagedIdentityCredential (Azure ಕಂಟೇನರ್ ಅಪ್ಸ್, ಅಪ್ಲಿಕೇಶನ್ ಸರ್ವೀಸ್, ಇತ್ಯಾದಿ)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # ಬಳಕೆದಾರ-ನಿರ್ಧಾರಿತ ನಿರ್ವಹಿತ ಗುರುತಿನೀಡಿ
)
# ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಗಾಗಿ AzureDeveloperCliCredential — ಸ್ಪಷ್ಟ tenant_id ಅತ್ಯಂತ ಮುಖ್ಯ
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# ಸರಪಳಿ: ಮೊದಲು ನಿರ್ವಹಿತ ಗುರುತಿನೀಡಿಯನ್ನು ಪ್ರಯತ್ನಿಸಿ, ವಿಫಲವಾದರೆ azd CLI ಗೆ ಹಿಂತಿರುಗಿ
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## ಅಸಿಂಕ್ ಕ್ಲೈಂಟ್ ಮೈಗ್ರೇಶನ್ — ಮುನ್ನ/ನಂತರ

ಮುನ್ನ (ಹಳೆ):
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

ನಂತರ:
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

## ಪೂರ್ಣ ಸಿಂಕ್ ಮೈಗ್ರೇಶನ್ — ಮುನ್ನ/ನಂತರ

ಮುನ್ನ (ಪಾರಂಪರಿಕ — Azure OpenAI ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ):
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

ನಂತರ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API — Azure OpenAI v1 ಎಂಡ್ಪಾಯಿಂಟ್):
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

## ಸ್ಟ್ರೀಮಿಂಗ್ (ಸಿಂಕ್)
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
        print()  # ಕೊನೆಯಲ್ಲಿ ಹೊಸ ಸಾಲು
```

## ಸ್ಟ್ರೀಮಿಂಗ್ (ಅಸಿಂಕ್)
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

## ವೆಬ್ ಆಪ್ ಸ್ಟ್ರೀಮಿಂಗ್ — ಬ್ಯಾಕ್ಎಂಡ್-ದಿಂದ-ಫ್ರಂಟ್‌ಎಂಡ್ ರೂಪ

SSE/JSONL ಅನ್ನು ಸ್ಟ್ರೀಮ್ ಮಾಡುವ ವೆಬ್ ಆಪ್ ಅನ್ನು ಮುigrateಗಿಸುವಾಗ, **ಬ್ಯಾಕ್ಎಂಡ್ ಸೀರಿಯಲೈಜೆಷನ್ ಫಾರ್ಮ್ಯಾಟ್** ಬದಲಾಗುತ್ತದೆ. ಫ್ರಂಟ್‌ಎಂಡ್ ಕೊಡಲಿದ್ದ ಪ್ರವೇಶ ಮಾದರಿಗಳನ್ನು ಉಳಿಸಲು ಹೊಸ ಬ್ಯಾಕ್ಎಂಡ್ ಔಟ್‌ಪುಟ್ ಅನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ, ಹಾಗಾಗಿ ಫ್ರಂಟ್‌ಎಂಡ್ ಅನ್ನು ಬದಲಿಸುವ ಅಗತ್ಯವಿಲ್ಲ.

**ಮುನ್ನ** — ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ ಬ್ಯಾಕ್ಎಂಡ್ ಪ್ರತಿ ಚಂಕ್‌ನ `choices[0]` ನಿಥಿ ಸಾಮಾನ್ಯವಾಗಿ ಸೀರಿಯಲೈಜ್ ಮಾಡುತ್ತಿತ್ತು:
```python
# ಹಳೆ: ಪ್ರತಿ ಚಂಕ್‌ಗೆ ಸರಣೀಕೃತ ಪೂರ್ಣ ಆಯ್ಕೆ ನಿಘಂಟು
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
ಫ್ರಂಟ್‌ಎಂಡ್ ಓದುತ್ತದೆ: `response.delta.content` (ಆಬ್ಜೆಕ್ಟ್‌ನ ಆಯ್ಕೆ ವಿಭಾಗದ ಆಳನೆ).

**ನಂತರ** — ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಬ್ಯಾಕ್ಎಂಡ್ ಒಂದು ಕನಿಷ್ಠ ರೂಪವನ್ನು ಹಿಗ್ಗಿಸುತ್ತದೆ, ಇದೇ ಫ್ರಂಟ್‌ಎಂಡ್ ಪ್ರವೇಶ ಮಾರ್ಗವನ್ನು ಉಳಿಸುವುದು:
```python
# ಹೊಸದು: ಮುಂಭಾಗವು ಅವಶ್ಯಕವಿರುವುದನ್ನು ಮಾತ್ರ ಹೊರಹಾಕಿ
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
ಫ್ರಂಟ್‌ಎಂಡ್ ಇನ್ನೂ ಓದುತ್ತದೆ `response.delta.content` — **ಯಾವುದೇ ಫ್ರಂಟ್‌ಎಂಡ್ ಬದಲಾವಣೆ ಅಗತ್ಯವಿಲ್ಲ**.

> **ಪ್ರಮುಖ ಅರ್ಥ**: ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಸ್ಟ್ರೀಮಿಂಗ್ ರೂಪ (`event.type` + `event.delta`) ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳಿಂದ ಮೂಲತಃ ವಿಭಿನ್ನವಾಗಿದೆ (`chunk.choices[0].delta.content`). ಆದರೆ ನಿಮ್ಮ ಬ್ಯಾಕ್ಎಂಡ್-ದಿಂದ-ಫ್ರಂಟ್‌ಎಂಡ್ ಒಪ್ಪಂದ ನೀವು ನಿರ್ಧರಿಸಬಹುದು. ಫ್ರಂಟ್‌ಎಂಡ್ ಮುಂಚಿತವಾಗಿಯೇ ನಿರೀಕ್ಷಿಸುವಂತೆ ಬ್ಯಾಕ್ಎಂಡ್ ಔಟ್‌ಪುಟ್ ಅನ್ನು ರೂಪಗೊಳಿಸಿ.

## ಸ್ಟ್ರೀಮಿಂಗ್ ಘಟನೆ ಕ್ರಮ

`stream: true` ಆಗಿರುವಾಗ, API ಈ ಕ್ರಮದಲ್ಲಿ ಘಟನೆಗಳನ್ನು ಹೊರಡಿಸುತ್ತದೆ:
1. `response.created` – ಪ್ರತಿಕ್ರಿಯೆ ವಸ್ತು ಆರಂಭವಾಯಿತು
2. `response.in_progress` – ಉತ್ಪತ್ತಿ ಪ್ರಾರಂಭವಾಯಿತು
3. `response.output_item.added` – ಔಟ್‌ಪುಟ್ ವಸ್ತು ಸೃಷ್ಟಿಸಲಾಗಿದೆ
4. `response.content_part.added` – ವಿಷಯ ಭಾಗ ಪ್ರಾರಂಭವಾಯಿತು
5. `response.output_text.delta` – ಪಠ್ಯ ತುಂಡುಗಳು (ಬಹು, ಪ್ರತಿಯೊಂದಕ್ಕೂ `delta: string` ಇದೆ)
6. `response.output_text.done` – ಪಠ್ಯ ಉತ್ಪಾದನೆ ಮುಗಿಸಿಕೊಂಡಿತು
7. `response.content_part.done` – ವಿಷಯ ಭಾಗ ಮುಗಿಯಿತು
8. `response.output_item.done` – ಔಟ್‌ಪುಟ್ ವಸ್ತು ಮುಗಿದಿದೆ
9. `response.completed` – ಪೂರ್ಣ ಪ್ರತಿಕ್ರಿಯೆ ಮುಗಿದಿದೆ

ಮೂಲ ಪಠ್ಯ ಸ್ಟ್ರೀಮಿಂಗಿಗಾಗಿ, ಕೇವಲ `response.output_text.delta` (ಪಠ್ಯ ತುಂಡುಗಳಿಗೆ) ಮತ್ತು `response.completed` (ಮುಗಿದಂತೆ) ಹ್ಯಾಂಡಲ್ ಮಾಡುವುದು.

## ವೆಬ್ ಆಪ್‌ಗಳಲ್ಲಿ ಸ್ಟ್ರೀಮಿಂಗ್ ದೋಷ ನಿರ್ವಹಣೆ

ವೆಬ್ ಆಪ್‌ನಲ್ಲಿ ಸ್ಟ್ರೀಮಿಂಗ್ ಮಾಡುವಾಗ, ಅಸಿಂಕ್ ಇಟರೇಶನ್ ಅನ್ನು `try/except` ನಲ್ಲಿ ರಾಪ್ ಮಾಡಿ ಮತ್ತು ದೋಷಗಳನ್ನು JSON ಆಗಿ ನಮೂದಿಸಿ, ಆದ್ದರಿಂದ ಫ್ರಂಟ್‌ಎಂಡ್ ಅವುಗಳನ್ನು ಸುಲಭವಾಗಿ ಪ್ರದರ್ಶಿಸಬಹುದು (ಉದಾಹರಣೆಗೆ, ದರ ಮಿತಿ, ತಾತ್ಕಾಲಿಕ ವೈಫಲ್ಯಗಳು):

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


> **ಏಕೆ ಇದು ಮುಖ್ಯ**: ಅಜೂರ್ ಓಪನ್‌ಎಐ ದರ ಮಿತಿ ಅಪಘಾತದ ಸಂದರ್ಭದಲ್ಲಿ `429 Too Many Requests` ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. `try/except` ಇಲ್ಲದೆ ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆ ಶಾಂತವಾಗಿ ಸಾಯುತ್ತದೆ. ಇದೊಂದಿಗೆ, ಫ್ರಂಟ್‌ಎಂಡ್‌ಗೆ `{"error": "Too Many Requests"}` ಸಿಗುತ್ತದೆ ಮತ್ತು ಮರುಪ್ರಯತ್ನ ಪ್ರಾಂಪ್ಟ್ ತೋರಿಸಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ.

## ಸ್ಟ್ರೀಮಿಂಗ್ ಈವೆಂಟ್ ಪ್ರಕಾರಗಳು (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## ಸಂವಾದ格式
```python
# ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಸಂದರ್ಶನ ಮಾದರಿಯನ್ನು ಇನ್ಪುಟ್ ಅರೆ ಮೂಲಕ ಬೆಂಬಲಿಸುತ್ತದೆ
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

## ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷ ನಿರ್ವಹಣೆ

ದೋಷ ಶರೀರ ರಚನೆ ಚಾಟ್ ಮುಗింపు‌ಗಳಿಂದ Responses API ಗೆ ಬದಲಾಗಿದೆ.

ಮೊದಲು (ಚಾಟ್ ಮುಗింపುಗಳು):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ನಂತರ (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ಪ್ರಮುಖ ಭೇದಗಳು:
- `innererror` ಲೇಪನವು **ಹೋಗಿದೆ** — ವಿಷಯ ಫಿಲ್ಟರ್ ವಿವರಗಳು ಈಗ `error.body` ನ ಮೇಲ್ಮಟ್ಟದಲ್ಲಿವೆ.
- `content_filter_result` (ಒಂದು) → `content_filters` (ಬಹುವಚನ ಸರಣಿಗಳು) ಪ್ರತಿಯೊಂದರ ಒಳಗೆ `content_filter_results` (ಬಹುವಚನ) ಹೊಂದಿವೆ.
- ಪ್ರತಿ `content_filters` ಎಂಟ್ರಿಯಲ್ಲಿ `blocked`, `source_type`, ಮತ್ತು ಪ್ರತಿ ವರ್ಗದ ವಿವರಗಳೊಂದಿಗೆ `content_filter_results` (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) ಇರುತ್ತದೆ.

ಸಂಪೂರ್ಣ Responses API ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷ ಶರೀರ ರಚನೆ:
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

## ಹನಿಯಾದ HTTP ಜಾಗೃತಿ (requests/httpx)

ಆಪ್ SDK ಬಳಕೆ ಬದಲಾಗಿ ನೇರವಾಗಿ ಅಜೂರ್ ಓಪನ್‌ಎಐ REST ಅನ್ನು ಕರೆಸಿದಾಗ:

ಮೊದಲು (ಚಾಟ್ ಮುಗింపುಗಳು):
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

ನಂತರ (Responses API):
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

> **ಗಮನಿಸಿ**: `output_text` ಪೈಥಾನ್ SDK ನ `Response` ಆಬ್ಜೆಕ್ಟಿನಲ್ಲಿನ ಅನುಕೂಲಾತ್ಮಕ ಪ್ರಾಪರ್ಟಿ. ಕಚ್ಚಾ REST JSON ಪ್ರತಿಕ್ರಿಯೆಯು ಮೇಲ್ಮಟ್ಟದ `output_text` ಕ್ಷೇತ್ರವಿಲ್ಲ — ಪಠ್ಯವು `output[0].content[0].text` ನಲ್ಲಿ ಇರುತ್ತದೆ.

## ಬಹು-ಬಾರ ಸಂವಾದ
```python
# ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಸಹಿತ ಸಂವಾದವನ್ನು ನಿರ್ಮಿಸಿ
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# ಸಹಾಯಕನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಸಂವಾದಕ್ಕೆ ಸೇರಿಸಿ
messages.append({"role": "assistant", "content": response.output_text})

# ಸಂವಾದವನ್ನು جاري ठेवಿರಿ
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

ವಿಷಯ-ಪ್ರಕಾರಿತ ಬಹು-ಬಾರ (ಸ್ಪಷ್ಟ `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` ಮೂಲಕ ಬಹು-ಬಾರ (ಪರ್ಯಾಯ)

ನೀವು ಸ್ವಲ್ಪವಾಗಿ ಸಂವಾದ ಸರಣಿಯನ್ನು ನಿರ್ವಹಿಸುವ ಬದಲು, ನೀವು ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು
ಸರ್ವರ್-ಬದಿಗೆ `previous_response_id` ಬಳಸಿ ಸರಪಳಿ ಮಾಡಬಹುದು. API ಪ್ರತಿಯೊಂದು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು محفوظ ಮಾಡುತ್ತದೆ ಮತ್ತು
ತಾನಾಗಿ ಹಿಂದಿನ ತಿರುವುಗಳನ್ನು ಮುಂಚೆ ಸೇರಿಸುತ್ತದೆ.

```python
# ಮೊದಲ ತಿರುವು
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# ಮುಂದಿನ ತಿರುವುಗಳು — ಹೊಸ ಬಳಕೆದಾರ ಸಂದೇಶ + ಹಿಂದಿನ ಪ್ರತಿಕ್ರಿಯೆಯ ID ಅನ್ನು ಕಳುಹಿಸಿ ಮಾತ್ರ
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**ಯಾವನ್ನು ಯಾವಾಗ ಬಳಸಬೇಕು:**

| ವಿಧಾನ | ಪ್ರಯೋಜನಗಳು | ಹಾನಿಗಳು |
|---|---|---|
| `input` ಸರಣಿ (ಹಸ್ತಚಾಲಿತ) | ಇತಿಹಾಸದ ಮೇಲೆ ಸಂಪೂರ್ಣ ನಿಯಂತ್ರಣ; ಕಡಿಮೆ/ಸಾರಾಂಶ ಮಾಡಬಹುದು; ಸರ್ವರ್-ಬದಿಗೆ ಸಂಗ್ರಹಣೆ ಅಗತ್ಯವಿಲ್ಲ (`store=False`) | ಹೆಚ್ಚು ಕೋಡ್; ನೀವು ಸರಣಿಯನ್ನು ನಿರ್ವಹಿಸುತ್ತೀರಿ |
| `previous_response_id` | ಸರಳ ಕೋಡ್; ಸ್ವಯಂಚಾಲಿತ ಸರಪಳಿ | `store=True` ಅಗತ್ಯ (ಡಿಫಾಲ್ಟ್); ಸಂವಾದ ಸರ್ವರ್-ಬದಿಗೆ ಸಂಗ್ರಹಿತ; ತಿರುವುಗಳ ನಡುವಿನ ಇತಿಹಾಸವನ್ನು ತಿದ್ದುಪಡಿ ಮಾಡಲಾಗುವುದಿಲ್ಲ |

> **ಸ್ಥಳಾಂತರ ಟಿಪ್ಪಣಿ:** ಹೆಚ್ಚಿನ ಚಾಟ್ ಮುಗింపು ಆ್ಯಪ್‌ಗಳು ಈಗಾಗಲೇ ತಮ್ಮದೇ ಸಂದೇಶ ಸರಣಿಯನ್ನು ನಿರ್ವಹಿಸುತ್ತವೆ, ಆದಾಗ್ಯೂ `input` ಸರಣಿಗೆ ಪರಿವರ್ತನೆ 1:1 ಸ್ಥಳಾಂತರವಾಗುತ್ತದೆ. ಹೊಸ ಕೋಡ್‌ಗೆ ಅಥವಾ ಸಂವಾದ ಇತಿಹಾಸವನ್ನು ಮಿತಿ ಮಾಡದಿದ್ದಾಗ `previous_response_id` ಬಳಸಿ.

## O-ಸೀರಿ ತರ್ಕ ಸೂತ್ರಗಳು (o1, o3-mini, o3, o4-mini)

O-ಸೀರಿ ಮಾದರಿಗಳು Responses API ಗೆ ಸ್ಥಳಾಂತರವಾಗುವಾಗ ವಿಶಿಷ್ಟ ಪರಿಮಾಣ ನಿರ್ಬಂಧಗಳನ್ನು ಹೊಂದಿವೆ.

### o-ಸೀರಿ ಪರಿಮಾಣ మ్యಾಪಿಂಗ್

| ಚಾಟ್ ಮುಗింపు (o-ಸೀರಿ) | Responses API | ಟಿಪ್ಪಣಿಗಳು |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | ಎತ್ತರಕ್ಕೆ ಸೆಟ್ ಮಾಡಿ (4096+) — ಯುಕ್ತಿವಾದ ಟೋಕನ್‌ಗಳು ಮೀರಿಕೊಳ್ತಾರೆ |
| `reasoning_effort` | `reasoning.effort` | ಇದ್ದರೆ ಹಾಗೆಯೇ ಇಡಿ (ಕಡಿಮೆ/ಮಧ್ಯಮ/ಹೆಚ್ಚು) |
| `temperature` | ತೆಗೆದುಹಾಕಿ ಅಥವಾ `1` ಆಗಿ ಸೆಟ್ ಮಾಡಿ | O-ಸಿರಿಯಸ್‌ಗೆ ಮಾತ್ರ `1` ಸರಿ |
| `top_p` | ತೆಗೆದುಹಾಕಿ | O-ಸಿರಿಯಸ್‌ನಲ್ಲಿ ಬೆಂಬಲವಿಲ್ಲ |
| `seed` | ತೆಗೆದುಹಾಕಿ | Responses API ಯಲ್ಲಿ ಬೆಂಬಲವಿಲ್ಲ |

### O-ಸಿರಿಯಸ್ ಮೊದಲು/ನಂತರ

ಮೊದಲು (ಒ-ಸಿರಿಯಸ್‌ನೊಂದಿಗೆ ಚಾಟ್ ಪೂರ್ಣತೆಗಳು):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

ನಂತರ (Responses API):
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

> **ಗಮನಿಸಿ**: O-ಸಿರಿಯಸ್ ಮಾದರಿಗಳು ಯುಕ್ತಿವಾದದ ವೇಳೆ ಪಠ್ಯ ಡೆಲ್ಟಾಗಳನ್ನು ಬಿಡುಗಡೆಮಾಡುವ ಮೊದಲು ಔಟ್ಪುಟ್ ಬಿಡರ್ ಮಾಡಬಹುದು. ಸ್ಟ್ರೀಮಿಂಗ್ ಇನ್ನೂ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಆದರೆ ಮೊದಲ `response.output_text.delta` ಇವೆಂಟ್ GPT ಮಾದರಿಗಳಿಗಿಂತಲೂ ಹೆಚ್ಚಿನ ವಿಳಂಬದ ನಂತರ ಬರಬಹುದು.

## ಯುಕ್ತಿವಾದ ಟೋಕನ್‌ಗಳನ್ನು ಪ್ರಾಪ್ತಿಪಡಿಸುವುದು
```python
# ಯಾಕ್‌ನೀಡಿನ ಮಾದರಿಗಳು ಅನವನ್ನು ಒಳಗೊಂಡವು — ನೀವು ಎಷ್ಟೊಂದು ಯಾಕೀ ಟೋಕನ್‌ಗಳನ್ನು ಉಪಯೋಗಿಸಲಾಯಿತು ಎಂಬುದನ್ನು ನೋಡಬಹುದು
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

> **ಮುಖ್ಯ**: ಯುಕ್ತಿವಾದ ಮಾದರಿಗಳ ಆಂತರಿಕ ಯುಕ್ತಿವಾದ ಪ್ರಕ್ರಿಯೆಗಾಗಿ `max_output_tokens=1000` (50–200 ಅಲ್ಲ) ಬಳಸಿರಿ. ಮಾದರಿ ಅಂತಿಮ ಔಟ್ಪುಟ್ ನಿರ್ಮಿಸುವ ಮೊದಲು ಆಂತರಿಕವಾಗಿ ಯುಕ್ತಿವಾದ ಟೋಕನ್‌ಗಳನ್ನು ಬಳಸುತ್ತದೆ.

## ರಚನಾತ್ಮಕ ಔಟ್ಪುಟ್ — JSON ಸ್ಕೀಮಾ
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

## ಉಪಕರಣ ಬಳಕೆ

- `tools` ನಲ್ಲಿ ಫ್ಲಾಟ್ Responses API ಫಾರ್ಮ್ಯಾಟ್‌ನೊಂದಿಗೆ ಕಾರ್ಯಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ — `name`, `description`, ಮತ್ತು `parameters` ಮೇಲೆ (ನಸ್ಟ್ ಆಗದಂತೆ) ಇರಬೇಕು.
- ಮಾದರಿ ಉಪಕರಣವನ್ನು ಕರೆದರೆ, ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಅದನ್ನು ನಡಿಸಿ ಮತ್ತು ಮುಂದಿನ ವಿನಂತಿಯಲ್ಲಿ `function_call_output` ಐಟಂ ಅನ್ನು `input` ಒಳಗೆ ಸೇರಿಸಿ.
- ಸ್ಕೀಮಾಗಳನ್ನು ಕನಿಷ್ಠವಾಗಿಯೇ ಇಡಿ; ಕಾರ್ಯ ನಿರ್ವಹಿಸುವ ಮೊದಲು ಇನ್ಪುಟ್‌ಗಳ ಪರಿಶೀಲನೆ ಮಾಡಿ.
- `strict: true` ಯನ್ನು ಬಳಸಿದಾಗ ಎಲ್ಲ ಗುಣಲಕ್ಷಣಗಳೂ `required` ನಲ್ಲಿ ಮತ್ತು `additionalProperties: false` ಅಗತ್ಯವಿದೆ.

> **⚠️ `pydantic_function_tool()` ಅನ್ವಯಿಸುವುದಿಲ್ಲ**: `openai.pydantic_function_tool()` ಸಹಾಯಕರಿಂದ ಇನ್ನೂ ಹಳೆಯ ಚಾಟ್ ಪೂರ್ಣತೆಗಳ ನಸ್ಟ್‌ ಆಗಿರುವ ಫಾರ್ಮ್ಯಾಟ್ (`{"type": "function", "function": {"name": ...}}`) ಸೃಷ್ಟಿಸಲಾಗುತ್ತದೆ. ಇದನ್ನು `responses.create()` ಜೊತೆ ಬಳಸಬೇಡಿ. ಉಪಕರಣ ಸ್ಕೀಮಾಗಳನ್ನು ಕೈಯಿಂದ ವ್ಯಾಖ್ಯಾನಿಸಿ ಅಥವಾ ಔಟ್ಪುಟ್ ಅನ್ನು ಫ್ಲಾಟ್ ಮಾಡಲು ಒಂದು ರಾಪರ್ ಬರೆಯಿರಿ.

### ಉಪಕರಣ ವ್ಯಾಖ್ಯಾನದ ಫಾರ್ಮ್ಯಾಟ್

Responses API ಫ್ಲಾಟ್ ಉಪಕರಣ ಫಾರ್ಮ್ಯಾಟ್ ಅನ್ನು ಉಪಯೋಗಿಸುತ್ತದೆ — `name`, `description`, `parameters` ಮೇಲ್ಮಟ್ಟ ಕೀಗಳಾಗಿವೆ (ನಸ್ಟ್ ಆಗದೆ).

**ಮೊದಲು (ಚಾಟ್ ಪೂರ್ಣತೆಗಳು — ನಸ್ಟ್ ಆಗಿದ್ದವು):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**ನಂತರ (Responses API — ಫ್ಲಾಟ್):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

ಸಂಪೂರ್ಣ ಉದಾಹರಣೆ:
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

`strict: true` ಇದ್ದಾಗ (ಸ್ಕೀಮಾ ವಿಧೇಯತೆ):
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
            "required": ["city_name"],       # ಎಲ್ಲಾ ಗುಣಲಕ್ಷಣಗಳನ್ನು ಪಟ್ಟಿಮಾಡಬೇಕು
            "additionalProperties": False,   # ಕಠಿಣ ಮODESಕಾಗಿ ಅವಶ್ಯಕವಾಗಿದೆ
        },
    }
]
```

### ಉಪಕರಣ ಕರೆ ರೌಂಡ್-ಟ್ರಿಪ್ (ನಡಿಸಿ ಫಲಿತಾಂಶವನ್ನು ಹಿಂತಿರುಗಿಸಿ)

ಮಾದರಿ ಉಪಕರಣ ಕರೆ ಕೇಳಿದಾಗ, `response.output` ಐಟಂ ಮತ್ತು `function_call_output` ಬಳಸಿ — ಚಾಟ್ ಪೂರ್ಣತೆಗಳ `role: assistant` + `role: tool` ಪ್ಯಾಟರ್ನ್ ಅಲ್ಲ.

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
    # ಸಂಭಾಷಣೆಗೆ ಮಾದರಿಯ function_call ಅಂಶಗಳನ್ನು ಸೇರಿಸಿ
    messages.extend(response.output)

    # ಪ್ರತಿಯೊಂದು ಉಪಕರಣವನ್ನು ನಿರ್ವಹಿಸಿ ಮತ್ತು ಫಲಿತಾಂಶಗಳನ್ನು ಸೇರಿಸಿ
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # ಉಪಕರಣದ ಫಲಿತಾಂಶಗಳೊಂದಿಗೆ ಅಂತಿಮ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯಿರಿ
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### ಕೆಲವು-ಶಾಟ್ ಉಪಕರಣ ಕರೆ ಉದಾಹರಣೆಗಳು

`input` ನಲ್ಲಿ ಕೆಲವು-ಶಾಟ್ ಉಪಕರಣ ಕರೆ ಉದಾಹರಣೆಗಳನ್ನು ನೀಡಿದಾಗ, `function_call` ಮತ್ತು `function_call_output` ಐಟಂಗಳನ್ನು ಬಳಸಿ. ID ಗಳು `fc_` ಮೂಲಕ ಪ್ರಾರಂಭವಾಗಬೇಕು.

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
# ಒಳಗೆಯ ವೆಬ್ ಹುಡುಕಾಟ ಉದಾಹರಣೆ
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## ಚಿತ್ರ ಇನ್ಪುಟ್

ಚಿತ್ರ ವಿಷಯ ಐಟಂಗಳು ಪ್ರಕಾರ `image_url` ಇಂದ `input_image`ಗೆ ಬದಲಾಗಿದೆ, URL ಕೂಡ ನಸ್ಟ್ ಆದ ಹವೆಯಿಂದ ಫ್ಲಾಟ್ ಸ್ಟ್ರಿಂಗ್‌ಗೆ ಬದಲಾಗಿದೆ.

### ಚಿತ್ರ ಇನ್ಪುಟ್ — ಮೊದಲು (ಚಾಟ್ ಪೂರ್ಣತೆಗಳು)
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

### ಚಿತ್ರ ಇನ್ಪುಟ್ — ನಂತರ (Responses API, URL)
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

### ಚಿತ್ರ ಇನ್ಪುಟ್ — ನಂತರ (Responses API, base64)
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

> **ಮುಖ್ಯ ಬದಲಾವಣೆಗಳು**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (ನಸ್ಟ್ ಆದ ಹವೆಯ объект್) → `"image_url": "..."` (ಫ್ಲಾಟ್ ಸ್ಟ್ರಿಂಗ್ — HTTPS URL ಅಥವಾ `data:image/...;base64,...` ಡೇಟಾ ಯುಸುಆರ್‌ಐ), (3) `"type": "text"` → `"type": "input_text"`.

## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ (MAF) ಸ್ಥಳಾಂತರ

**ನಿಮ್ಮ MAF ಆವೃತ್ತಿಯನ್ನು ಮೊದಲು ಪರಿಶೀಲಿಸಿ** — ಸ್ಥಳಾಂತರವು ನೀವು MAF 1.0.0+ ಮೇಲಿರುವಿರಿ ಅಥವಾ 1.0.0 ಮೊದಲುದ ಬ್ಯೇಟಾ/ಆರ್‌ಸಿ ಆವೃತ್ತಿಯಲ್ಲಿದ್ದೀರಾ ಅವಲಂಬಿಸುತ್ತದೆ.

ಪರಿಶೀಲಿಸಲು: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ ನಲ್ಲಿ, `OpenAIChatClient` **ಈಗಾಗಲೇ Responses API ಅನ್ನು ಬಳಸುತ್ತದೆ** — ಯಾವುದೇ ಸ್ಥಳಾಂತರ ಅಗತ್ಯವಿಲ್ಲ.

ಕೋಡ್‌ಬೇಸ್ ಹಳೆಯ `OpenAIChatCompletionClient` (ಹಾಗೂ `chat.completions.create` ಬಳಸುವ) ಇದ್ದರೆ, ಅದನ್ನು `OpenAIChatClient` ಮೂಲಕ ಬದಲಿಸಿ:

ಮೊದಲು:
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

ನಂತರ:
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

### MAF 1.0.0 ಮೊದಲು (ಬೇಟಾ/ಆರ್‌ಸಿ ಬಿಡುಗಡೆಗಳು)

MAF 1.0.0 ಮೊದಲು, `OpenAIChatClient` ಚಾಟ್ ಪೂರ್ಣತೆಗಳನ್ನು ಬಳಸಿತ್ತು. `agent-framework-openai>=1.0.0` ಗೆ ಸುಧಾರಿಸಿ ಅಲ್ಲಿ `OpenAIChatClient` Responses API ಅನ್ನು ಡಿಫಾಲ್ಟ್ ಆಗಿ ಬಳಸುತ್ತದೆ.

> **ಗಮನಿಸಿ**: `Agent`, `MCPStreamableHTTPTool` ಮತ್ತು ಇತರೆ MAF APIs ಬದಲಾಗಿಲ್ಲ — ಕೇವಲ ಕ್ಲೈಂಟ್ ಕ್ಲಾಸ್ ಆಮದು ಮತ್ತು ನಿರ್ಮಾಣ ಬದಲಾಗಿದೆ.

## ಲ್ಯಾಂಗ್‌ಚೈನ್ (`langchain-openai`) ಸ್ಥಳಾಂತರ

`ChatOpenAI()` ಗೆ `use_responses_api=True` ಅನ್ನು ಸೇರಿಸಿ. ಜೊತೆಗೆ ಮೆಸೇಜ್ ವಿಷಯ ಪಡೆಯುವುದನ್ನು `.content` ಇಂದ `.text` ಗೆ ನವೀಕರಿಸಿ.

ಮೊದಲು:
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

# ... ಏಜೆಂಟ್ ಕರೆಯುವಿಕೆ ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

ನಂತರ:
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

# ... ಏಜೆಂಟ್ ಕರೆಯುವಿಕೆ ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **ಮುಖ್ಯ ಬದಲಾವಣೆಗಳು**: (1) ನಿರ್ಮಾಪಕದಲ್ಲಿ `use_responses_api=True`, (2) ಪ್ರತಿಕ್ರಿಯೆಯ ಮೆಸೇಜ್‌ಗಳಲ್ಲಿ `.content` → `.text`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->