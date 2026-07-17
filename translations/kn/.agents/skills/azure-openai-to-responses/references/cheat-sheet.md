# ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಚೀಟ್ ಶೀಟ್ (Python + Azure OpenAI)

> ಕೆಳಗಿನ ಎಲ್ಲಾ ಸ్నಿಪೆಟ್‌ಗಳು `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ಮತ್ತು `client` ಈಗಾಗಲೇ ನಿರ್ನಾಯಕೃತವಾಗಿದೆ ಎಂದು ಅನುumAssume ಮಾಡುತ್ತದೆ (ಕ್ಲೈಂಟ್ ಸೆಟಪ್ ನೋಡಿ).

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

## ಕ್ಲೈಂಟ್ ಸೆಟಪ್ — EntraID (ಶಿಫಾರಸು ಮಾಡಿದ)
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

## ಅಸಿಂಕ್ ಕ್ಲೈಂಟ್ ಸೆಟಪ್ — ಸ್ಪಷ್ಟ ಟಿನಂಟ್ (ಬಹು-ಟಿನಂಟ್) ಸಹಿತ EntraID

Azure OpenAI ಸಂಪನ್ಮೂಲವು **ಭಿನ್ನ ಟಿನಂಟ್**ನಲ್ಲಿದ್ದರೆ, ಕ್ರೆಡೆಂಶಿಯಲ್‌ಗೆ ಸ್ಪಷ್ಟವಾಗಿ `tenant_id` ಅನ್ನು ಪಾಸು ಮಾಡಬೇಕು. ಇದು ಸಾಮಾನ್ಯವಾಗಿ ಡೆವ್/ಟೆಸ್ಟ್ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ, ಬಳಕೆದಾರರ ಮನೆ ಟಿನಂಟ್ ಸಂಪನ್ಮೂಲ ಟಿನಂಟನಿಗಿಂತ ವಿಭಿನ್ನವಾಗಿರುತ್ತದೆ.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ಉತ್ಪಾದನೆಗಾಗಿ ManagedIdentityCredential (ಅ್ಯಜೂರ್ ಕಂಟೇನರ್ ಅಪ್ಲಿಕೇಶನ್ಗಳು, ಅಪ್ಲಿಕೇಶನ್ ಸರ್ವೀಸ್, ಇತ್ಯಾದಿ)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # ಬಳಕೆದಾರ-ನಿಯುಕ್ತಿತ ನಿರ್ವಹಿತ ಗುರುತು
)
# ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಗಾಗಿ AzureDeveloperCliCredential — ಸ್ಪಷ್ಟ tenant_id ಅವಶ್ಯಕವಾಗಿದೆ
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# ಸರಪಳಿ: ಮೊದಲಿಗೆ ನಿರ್ವಹಿತ ಗುರುತನ್ನು ಪ್ರಯತ್ನಿಸಿ, ನಂತರ azd CLIಗೆ ಬಿಟ್ಟುಕೊಡು
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## ಅಸಿಂಕ್ ಕ್ಲೈಂಟ್ ಮೈಗ್ರೇಷನ್ — ಮುಂಚೆ/ನಂತರ

ಮುಂಚೆ (ಪರಿಹರಿಸಲಾಗಿದೆ):
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

## ಸಂಪೂರ್ಣ ಸಿಂಕೇ ಮಾಯಗ್ರೇಷನ್ — ಮುಂಚೆ/ನಂತರ

ಮುಂಚೆ (ಪಾರಂಪರಿಕ — Azure OpenAI ಚಾಟ್ ಪೂರ್ಣತೆಗಳು):
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

## ವೆಬ್ ಅಪ್ಲಿಕೇಶನ್ ಸ್ಟ್ರೀಮಿಂಗ್ — ಹಿನ್ನೆಲೆ-ಫ್ರಂಟ್‌ಎಂಡ್ ರೂಪ

SSE/JSONL ಅನ್ನು ಫ್ರಂಟ್‌ಎಂಡ್‌ಗೆ ಸ್ಟ್ರೀಮ್ ಮಾಡುವ ವೆಬ್ ಅಪ್ ಅನ್ನು ಮೈಗ್ರೇಟ್ ಮಾಡುವಾಗ, **ಹಿನ್ನೆಲೆ ಸರಣೀಕರಣ ಸ್ವರೂಪ** ಬದಲಾಗುತ್ತದೆ. ಹೊಸ ಹಿನ್ನೆಲೆ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಫ್ರಂಟ್‌ಎಂಡ್‌ನ ಇತ್ತೀಚಿನ ಪ್ರವೇಶ ಮಾದರಿಗಳನ್ನು ಉಳಿಸುವಂತೆ ವಿನ್ಯಾಸಗೊಳ್ಳಿಸಿ, ಆದ್ದರಿಂದ ಫ್ರಂಟ್‌ಎಂಡ್‌ಗೆ ಯಾವುದೇ ಬದಲಾವಣೆಗಳ ಅಗತ್ಯವಿಲ್ಲ.

**ಮುಂಚೆ** — ಚಾಟ್ ಪೂರ್ಣತೆಗಳು ಹಿನ್ನೆಲೆ ಸಾಮಾನ್ಯವಾಗಿ ಪ್ರತಿಯೊಂದು ಚಂಕ್‌ನ `choices[0]` ಡಿಕ್ಷನರಿಯನ್ನು ಸರಣೀಕರಿಸಿತು:
```python
# ಹಳೆಯದು: ಪ್ರತಿ ತುಣುಕುಗೆ ಸರಣೀಕೃತ ಪೂರ್ಣ ಆಯ್ಕೆ ಪದಕ
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
ಫ್ರಂಟ್‌ಎಂಡ್ ಓದು: `response.delta.content` (ಆಬ್ಜೆಕ್ಟಿನ ಆಳಗಿನ ಮಾರ್ಗ).

**ನಂತರ** — ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಹಿನ್ನೆಲೆ ಕನಿಷ್ಠ ರೂಪವನ್ನು ಹೊರಬಿಡುತ್ತದೆ ಮತ್ತು ಅದೇ ಫ್ರಂಟ್‌ಎಂಡ್ ಪ್ರವೇಶ ಮಾರ್ಗವನ್ನು ಉಳಿಸುತ್ತದೆ:
```python
# ಹೊಸದು: ಫ್ರಂಟ್‌ಎಂಡ್‌ಗೆ ಬೇಕಾದವುಗಳನ್ನೇ ಮಾತ್ರ ಪ್ರಸಾರ ಮಾಡು
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
ಫ್ರಂಟ್‌ಎಂಡ್ ಇನ್ನೂ `response.delta.content` ಅನ್ನು ಓದುತ್ತದೆ — **ಯಾವುದೇ ಫ್ರಂಟ್‌ಎಂಡ್ ಬದಲಾವಣೆ ಅಗತ್ಯವಿಲ್ಲ**.

> **ಪ್ರಮುಖ ಅರ್ಥ**: ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಸ್ಟ್ರೀಮಿಂಗ್ ರೂಪ (`event.type` + `event.delta`) ಚಾಟ್ ಪೂರ್ಣತೆಗಳ (`chunk.choices[0].delta.content`)ಅಗತ್ಯವಾಗಿರುವುದರಿಂದ ಮೂಲತಃ ವಿಭಿನ್ನವಾಗಿದೆ. ಆದರೆ ನಿಮ್ಮ ಹಿನ್ನೆಲೆ-ಫ್ರಂಟ್‌ಎಂಡ್ ಒಪ್ಪಂದವನ್ನು ನೀವು ನಿರ್ಧರಿಸಬಹುದು. ಹಿನ್ನೆಲೆ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಫ್ರಂಟ್‌ಎಂಡ್ ಈಗಾಗಲೇ ನಿರೀಕ್ಷಿಸುವಂತೆ ರೂಪಿಸಿ.

## ಸ್ಟ್ರೀಮಿಂಗ್ ಘಟನೆ ಸರಣೀಕರಣ

`stream: true` ಇರುವಾಗ, API ಕೆಳಗಿನ ಕ್ರಮದಲ್ಲಿ ಘಟನೆಗಳನ್ನು ಹೊರಡಿಸುತ್ತದೆ:
1. `response.created` – ಪ್ರತಿಕ್ರಿಯೆ ವಸ್ತು ಆರಂಭಗೊಂಡಿದೆ
2. `response.in_progress` – ಉತ್ಪಾದನೆ ಪ್ರಾರಂಭವಾಗಿದೆ
3. `response.output_item.added` – ಔಟ್‌ಪುಟ್ ಐಟಂ ಸೃಷ್ಟಿಸಲಾಗಿದೆ
4. `response.content_part.added` – ವಿಷಯ ಭಾಗ ಆರಂಭವಾಗಿದೆ
5. `response.output_text.delta` – ಪಠ್ಯ ಚಂಕ್‌ಗಳು (ಬಹುಮಾನ, ಪ್ರತಿ ಒಂದು `delta: string` ಹೊಂದಿದೆ)
6. `response.output_text.done` – ಪಠ್ಯ ಉತ್ಪಾದನೆ ಮುಗಿಯಿತು
7. `response.content_part.done` – ವಿಷಯ ಭಾಗ ಮುಗಿಯಿತು
8. `response.output_item.done` – ಔಟ್‌ಪುಟ್ ಐಟಂ ಮುಗಿಯಿತು
9. `response.completed` – ಸಂಪೂರ್ಣ ಪ್ರತಿಕ್ರಿಯೆ ಪೂರ್ಣವಾಗಿದೆ

ಮೂಲ ಪಠ್ಯ ಸ್ಟ್ರೀಮಿಂಗ್‌ಗೆ, `response.output_text.delta` (ಪಠ್ಯ ಚಂಕ್ಗೆ) ಮತ್ತು `response.completed` (ಮೊತ್ತ ಮಿತಿಗೆ) ಮಾತ್ರ ಕೈಗಾರಿಕೆಮಾಡಿ.

## ವೆಬ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಸ್ಟ್ರೀಮಿಂಗ್ ದೋಷ ನಿರ್ವಹಣೆ

ವೆಬ್ ಅಪ್ಲಿಕೇಶನಿನಲ್ಲಿ ಸ್ಟ್ರೀಮಿಂಗ್ ಮಾಡುವಾಗ, ಅಸಿಂಕ್ ಪುನರಾವರ್ತನೆಗೆ `try/except` ಅನ್ನು ಬಳಸಿ ಮತ್ತು ದೋಷಗಳನ್ನು JSON ರೂಪದಲ್ಲಿ ಹಿಂತೆಗೆ ಮಾಡಿ, ಇದರಿಂದ ಫ್ರಂಟ್‌ಎಂಡ್Gracefully ತೋರಿಸಬಲ್ಲದು (ಉದಾ: ದರ ನಿಯಂತ್ರಣ, ತಾತ್ಕಾಲಿಕ ವೈಫಲ್ಯಗಳು):

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

> **ಈದರಿಂದ ಪ್ರಮುಖ ಇಷ್ಟ**: ಅವಧಿಯಲ್ಲಿ दರ ನಿಬಂಧನೆ ಎಲ್ಲ Azure OpenAI  `429 Too Many Requests` ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. `try/except` ಇಲ್ಲದಿದ್ದರೆ, ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆ ಮೌನವಾಗಿ ನಿಂತದು. ಇದಿದ್ದರೆ, ಫ್ರಂಟ್‌ಎಂಡ್‌ಗೆ `{"error": "Too Many Requests"}` ಸಿಗುತ್ತದೆ ಮತ್ತು ಮತ್ತೆ ಪ್ರಯತ್ನಿಸುವ ಸೂಚನೆಗಳನ್ನು ತೋರಿಸಬಹುದು.

## ಸ್ಟ್ರೀಮಿಂಗ್ ಘಟನೆಯ ಪ್ರಕಾರಗಳು (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## ಸಂಭಾಷಣೆ ಸ್ವರೂಪ
```python
# ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಇನ್‌ಪುಟ್ ಅರೆ ಮೂಲಕ ಸಂಭಾಷಣಾ ಸ್ವರೂಪವನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ
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

ದೋಷ ದೇಹದ ರಚನೆ ಚಾಟ್ ಪೂರ್ಣತೆಗಳಿಂದ ಪ್ರತಿಕ್ರಿಯೆಗಳು APIಗೆ ಬದಲಾಗಿದೆ.

ಮುಂಚೆ (ಚಾಟ್ ಪೂರ್ಣತೆಗಳು):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ನಂತರ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳು:
- `innererror` ಕವರ್ **ಲೀಹಾಗಿದೆ** — ವಿಷಯ ಫಿಲ್ಟರ್ ವಿವರಗಳು ಈಗ `error.body` ಟಾಪ್ ಮಟ್ಟದಲ್ಲಿವೆ.
- `content_filter_result` (ಏಕವಚನ) → `content_filters` (ಬಹುವಚನ ಸರಣಿ) ಮತ್ತು ಅವರೊಳಗೆ ಬಹುವಚನ `content_filter_results` ಇದ್ದವೆ.
- ಪ್ರತಿಯೊಂದು ಎಂಟ್ರಿಯಲ್ಲಿ `content_filters` ನಲ್ಲಿ `blocked`, `source_type` ಮತ್ತು ತನಿಖೇಕ್ಕೆ `content_filter_results` (ಪ್ರತಿ ವರ್ಗದ ವಿವರಗಳೊಂದಿಗೆ) ಸೇರಿವೆ (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

ಸಂಪೂರ್ಣ ಪ್ರತಿಕ್ರಿಯೆಗಳು API ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷ ದೇಹ ರೂಪ:
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

## ರಾ HTTP ಮೈಗ್ರೇಷನ್ (requests/httpx)

ਐಪ್ ನೇರವಾಗಿ SDK ಬಳಸದೆ Azure OpenAI REST ಅನ್ನು ಕರೆಯಿಸಿದರೆ:

ಮುಂಚೆ (ಚಾಟ್ ಪೂರ್ಣತೆಗಳು):
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

ನಂತರ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API):
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

> **ಗಮನಿಸಿ**: `output_text` ಪೈಠಾನ್ SDKಯ `Response` ವಸ್ತುವಿನ ಒಂದು ಅನುಕೂಲಿತ ಪ್ರಾಪರ್ಟಿ. ರಾ REST JSON ಪ್ರತಿಕ್ರಿಯೆಗೆ ಮೇಲ್ಮಟ್ಟ `output_text` ಕ್ಷೇತ್ರವಿಲ್ಲ — ಪಠ್ಯ `output[0].content[0].text` ನಲ್ಲಿ ಇದೆ.

## ಬಹು-ತಿರುವು ಸಂಭಾಷಣೆ
```python
# Responses API ನೊಂದಿಗೆ ಸಂಭಾಷಣೆ ನಿರ್ಮಿಸಿ
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# ಸಹಾಯಕನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಸಂಭಾಷಣೆಗೆ ಸೇರಿಸಿ
messages.append({"role": "assistant", "content": response.output_text})

# ಸಂಭಾಷಣೆಯನ್ನು ಮುಂದುವರೆಸಿ
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

ವಿಷಯ ಟೈಪ್ ಮಾಡಿದ ಬಹು-ತಿರುವು (`input_text`/`output_text` ಸ್ಪಷ್ಟವಾದ):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` ಮೂಲಕ ಬಹು-ತಿರುವು (ವikleೂಪ)

ನೀವು ಸಂಭಾಷಣೆ ಸರಣಿಯನ್ನು ಸ್ವತಃ ನಿರ್ವಹಿಸುವ ಬದಲು, ನೀವು ಸೃಷ್ಟಿಸಿದ ಪ್ರತಿಕ್ರಿಯೆಗಳು
ಸರ್ವರ್-ಬದಿಯಲ್ಲಿ `previous_response_id` ಬಳಸಿ ತಂತಿಯಾಗಿ ಸರಪಳಿಯಿಡಬಹುದು. API ಪ್ರತಿ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಸಂಗ್ರಹಿಸುತ್ತದೆ ಮತ್ತು
ಹಿಂದಿನ ತಿರುವುಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸೇರಿಸುತ್ತದೆ.

```python
# ಮೊದಲ ಬಾರಿಗೆ ತಿರುಗು
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# ಮುಂದಿನ ತಿರುಗುಗಳು — ಹೊಸ ಬಳಕೆದಾರ ಸಂದೇಶ + ಹಿಂದಿನ ಪ್ರತಿಕ್ರಿಯೆ ID ಅನ್ನು ಕೇವಲ ಪಾಸು ಮಾಡಿ
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**ಯಾವುದನ್ನು ಯಾವಾಗ ಉಪಯೋಗಿಸುವುದು:**

| ವಿಧಾನ | ಲಾಭಗಳು | ತೊಂದರೆಗಳು |
|---|---|---|
| `input` ಸರಣಿ (ಹಸ್ತಚಾಲಿತ) | ಇತಿಹಾಸದ ಮೇಲೆ ಸಂಪೂರ್ಣ ನಿಯಂತ್ರಣ; ಕಡಿಮೆ/ಸಾರಾಂಶ ಮಾಡಬಹುದು; ಸರ್ವರ್-ಬದಿ ಸಂಗ್ರಹಣೆ ಅಗತ್ಯವಿಲ್ಲ (`store=False`) | ಹೆಚ್ಚು ಕೋಡ್; ನೀವು ಸರಣಿಯನ್ನು ನಿರ್ವಹಿಸಬೇಕಾಗುತ್ತದೆ |
| `previous_response_id` | ಸರಳ ಕೋಡ್; ಸ್ವಯಂಚಾಲಿತ ತಂತಿ | `store=True` (ಡೀಫಾಲ್ಟ್) ಅಗತ್ಯ; ಸಂಭಾಷಣೆ ಸರ್ವರ್-ಬದಿ ಸಂಗ್ರಹಿತ; ತಿರುವುಗಳ ನಡುವೆ ಇತಿಹಾಸ ಬದಲಾಯಿಸಲಾಗದು |

> **ಮೈಗ್ರೇಷನ್ ಸೂಚನೆ:** ಹೆಚ್ಚಿನ ಚಾಟ್ ಪೂರ್ಣತೆ ಅಪ್ಲಿಕೇಶನ್ಗಳು ಈಗಾಗಲೆ ತಮ್ಮ ಸ್ವಂತ ಸಂದೇಶ ಸರಣಿಯನ್ನು ನಿರ್ವಹಿಸುತ್ತವೆ, ಆದ್ದರಿಂದ `input` ಸರಣಿಗೆ ಪರಿವಾರ್ತನೆ ಹೆಚ್ಚು ನೇರ 1:1 ಮೈಗ್ರೇಷನ್ ಆಗಿದೆ. ಹೊಸ ಕೋಡ್‌ಗಾಗಿ ಅಥವಾ ಸಂಭಾಷಣೆ ಇತಿಹಾಸವನ್ನು ತಿದ್ದುಪಡಿಸುವ ಅಗತ್ಯವಿಲ್ಲದಿದ್ದರೆ `previous_response_id` ಉಪಯೋಗಿಸಿ.

## o-ಸೀರೀಸ್ ಯುಕ್ತಿ ಮಾದರಿ (o1, o3-mini, o3, o4-mini)

o-ಸೀರೀಸ್ ಮಾದರಿಗಳಿಗೆ ಪ್ರತಿಕ್ರಿಯೆಗಳು APIಗೆ ಮೈಗ್ರೇಟ್ ಮಾಡುವಾಗ ವಿಶೇಷ ಪ್ಯಾರಾಮೀಟರ್ ನಿಯಮಾವಳಿಗಳು ಇವೆ.

### o-ಸೀರೀಸ್ ಪ್ಯಾರಾಮೀಟರ್ మ్యಾಪಿಂಗ್

| ಚಾಟ್ ಪೂರ್ಣತೆಗಳು (o-ಸೀರೀಸ್) | ಪ್ರತಿಕ್ರಿಯೆಗಳು API | ಟಿಪ್ಪಣಿಗಳು |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | ಹೆಚ್ಚಿನ ಸಂಖ್ಯೆಗೆ ಹೊಂದಿಸಿ (4096+) — ಯುಕ್ತಿಯ ಟೋಕನ್‌ಗಳು ಮಿತಿಗೆ ಸೇರಿವೆ |
| `reasoning_effort` | `reasoning.effort` | ಇದ್ದರೆ ಇರುತ್ತದೆ (ತಗ್ಗು/ಮಧ್ಯ/ಹೆಚ್ಚು) |
| `temperature` | ತೆಗೆದುಹಾಕಿ ಅಥವಾ `1` ರಹಿತ ಮಾಡಿರಿ | o-ಸೀರೀಸ್ ಗೆ ಮಾತ್ರ `1` ಗುರುತಿಸಲಾಗಿದೆ |
| `top_p` | ತೆಗೆದುಹಾಕಿ | o-ಸೀರೀಸ್ ನಲ್ಲಿ ಬೆಂಬಲವಿಲ್ಲ |
| `seed` | ತೆಗೆದುಹಾಕಿ | ಪ್ರತಿಕ್ರಿಯೆಗಳು APIನಲ್ಲಿ ಬೆಂಬಲವಿಲ್ಲ |

### o-ಸೀರೀಸ್ ಮುಂಚೆ/ನಂತರ

ಮುಂಚೆ (o-ಸೀರೀಸ್ ಸಹಿತ ಚಾಟ್ ಪೂರ್ಣತೆಗಳು):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

ನಂತರ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API):
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

> **ಗಮನಿಸಿ**: ಯುಕ್ತಿ ಇರುತ್ತಿರುವಾಗ o-ಸೀರೀಸ್ ಮಾದರಿಗಳು ಪಠ್ಯ ಡೆಲ್ಟಾಗಳನ್ನು ಹೊಡೆದ ಮೊದಲು ಔಟ್‌ಪುಟ್ ಸಂಗ್ರಹಿಸಬಹುದು. ಸ್ಟ್ರೀಮಿಂಗ್ ಇನ್ನೂ ಕೆಲಸಮಾಡುತ್ತದೆ ಆದರೆ ಮೊದಲ `response.output_text.delta` ಘಟನೆ ಹೆಚ್ಚಿನ ವಿಳಂಬದ ನಂತರ ಬರುವ ಸಾಧ್ಯತೆ ಇದೆ, GPT ಮಾದರಿಗಳಿಗಿಂತ.

## ಯುಕ್ತಿ ಟೋಕನ್‌ಗಳನ್ನು ಪ್ರವೇಶಿಸುವುದು
```python
# ತರ್ಕ ಮಾದರಿಗಳು ಆಂತರಿಕ ತರ್ಕಾವಳಿಯನ್ನು ಬಳಸುತ್ತವೆ — ನೀವು ಎಷ್ಟು ತರ್ಕ ಟೋಕನ್ಗಳು ಬಳಸಲ್ಪಟ್ಟಿವೆ ಎಂದು ನೋಡಬಹುದು
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

> **ಮುಖ್ಯವಾಗಿದೆ**: ಯುಕ್ತಿ ಮಾದರಿಗಳ ಅಂತರಂಗ ಯುಕ್ತಿ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಕುರಿತು ಗಮನಿಸಿದರೆ `max_output_tokens=1000` ಉಪಯೋಗಿಸಿ (50-200 ಅಲ್ಲ). ಮಾದರಿ ಅಂತರ್ಗತವಾಗಿ ಯುಕ್ತಿ ಟೋಕನ್‌ಗಳನ್ನು ಉಪಯೋಗಿಸಿ ಬಳಿಕ ಅಂತಿಮ ಔಟ್‌ಪುಟ್ ಅನ್ನು ರಚಿಸುತ್ತದೆ.

## ಸಂರಚಿತ ಔಟ್‌ಪುಟ್ — JSON Schema
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

- `tools` ನಲ್ಲಿ ಕಾರ್ಯಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ **ಫ್ಲ್ಯಾಟ್ ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಸ್ವರೂಪ** ಜೊತೆ — `name`, `description`, ಮತ್ತು `parameters` ಮುಖ್ಯ ಮಟ್ಟದಲ್ಲಿ (ನಿರ್ವಹಣೆ `function` ಅಡಿಯಲ್ಲಿ ಇಲ್ಲ).
- ಮಾದರಿ ಉಪಕರಣವನ್ನು ಕರೆಸಲು ಕೇಳಿದಾಗ, ಅದನ್ನು ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ನಡೆಸಿ ಮತ್ತು ಮುಂದಿನ ವಿನಂತಿಯಲ್ಲಿ ಉಪಕರಣ ಫಲಿತಾಂಶವನ್ನು `function_call_output` ಐಟಂ ಆಗಿ `input` ಒಳಗೆ ಸೇರಿಸಿ.
- schemas ಅನ್ನು ಕನಿಷ್ಠವನ್ನಾಗಿರಿ; ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಮೊದಲು ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.
- `strict: true` ಬಳಸಿದಾಗ ಎಲ್ಲ ಗುಣಲಕ್ಷಣಗಳನ್ನು `required`ದಲ್ಲಿ ಪಟ್ಟಿ ಮಾಡಬೇಕು ಮತ್ತು `additionalProperties: false` ಅನಿವಾರ್ಯವಾಗಿದೆ.

> **⚠️ `pydantic_function_tool()` ಅಸಂಗತವಾಗಿದೆ**: `openai.pydantic_function_tool()` ಸಹಾಯಕವು ಹಳೆಯ ಚಾಟ್ ಪೂರ್ಣತೆಗಳ ಗೂಢ ಸಂರಚನೆಯ ಸ್ವರೂಪ ({"type": "function", "function": {"name": ...}}) ಇನ್ನೂ ಉತ್ಪಾದಿಸುತ್ತದೆ. `responses.create()` ಜೊತೆಗೆ ಇದನ್ನು ಬಳಸಬೇಡಿ. ಉಪಕರಣ schemas ಲಿಖಿತವಾಗಿವಾಗಿಪ್ಪವಾಗಿ ವ್ಯಾಖ್ಯಾನಿಸಿ ಅಥವಾ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಫ್ಲ್ಯಾಟ್ ಮಾಡಲು ವ್ಯಾಖ್ಯಾನಕರ್ತನನ್ನು ಬರೆಯಿರಿ.

### ಉಪಕರಣ ವ್ಯಾಖ್ಯಾನ ಸ್ವರೂಪ

ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಫ್ಲ್ಯಾಟ್ ಉಪಕರಣ ಸ್ವರೂಪ ಬಳಸುತ್ತದೆ — `name`, `description`, `parameters` ಮುಖ್ಯಮುಖದ ಕೀಲಿಗಳು (ನಿರ್ವಹಣೆ `function` ಅಡಿಯಲ್ಲಿ ಇಲ್ಲ).

**ಮುಂಚೆ (ಚಾಟ್ ಪೂರ್ಣತೆಗಳು — ಗುಡಿಪು):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**ನಂತರ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API — ಫ್ಲ್ಯಾಟ್):**
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

`strict: true` (schema ಜೋರಣೆಯೊಂದಿಗೆ):
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
            "required": ["city_name"],       # ಎಲ್ಲಾ ಗುಣಲಕ್ಷಣಗಳನ್ನು ನಮೂದಿಸಬೇಕು
            "additionalProperties": False,   # ಕಠಿಣ ಮೌಡ್ಗಾಗಿ ಅಗತ್ಯವಿದೆ
        },
    }
]
```

### ಉಪಕರಣ ಕರೆ ಮರುಪಂಕ್ತಿ (ನಡೆ ಸೇರಿದಂತೆ ಫಲಿತಾಂಶ ಪ್ರತಿಕ್ರಿಯಿಸಿ)

ಮಾದರಿ ಉಪಕರಣ ಕರೆ ಕೇಳಿದಾಗ, `response.output` ಐಟಂಗಳೊಂದಿಗೆ + `function_call_output` ಅನ್ನು ಉಪಯೋಗಿಸಿ — **ಚಾಟ್ ಪೂರ್ಣತೆಗಳ** `role: assistant` + `role: tool` ಮಾದರಿಯ ಬದಲು.

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
    # ಮಾದರಿಯ function_call ಐಟಂಗಳನ್ನು ಸಂವಾದಕ್ಕೆ ಸೇರಿಸಿ
    messages.extend(response.output)

    # ಪ್ರತಿ ಸಾಧನವನ್ನು ನಿರ್ವಹಿಸಿ ಮತ್ತು ಫಲಿತಾಂಶಗಳನ್ನು ಸೇರಿಸಿ
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # ಸಾಧನ ಫಲಿತಾಂಶಗಳೊಂದಿಗೆ ಅಂತಿಮ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯಿರಿ
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### ಸ್ವಲ್ಪ-ಶಾಟ್ ಉಪಕರಣ ಕರೆ ಉದಾಹರಣೆಗಳು

`input` ನಲ್ಲಿ ಸ್ವಲ್ಪ-ಶಾಟ್ ಉಪಕರಣ ಕರೆ ಉದಾಹರಣೆಗಳನ್ನು ನೀಡುವಾಗ `function_call` ಮತ್ತು `function_call_output` ಐಟಂಗಳನ್ನು ಬಳಸಿ. IDs `fc_` ಇಂದ ಪ್ರಾರಂಭವಾಗಬೇಕು.

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
# ನಿರ್ಮಿತ ವೆಬ್ ಹುಡುಕಾಟ ಉದಾಹರಣೆ
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## ಚಿತ್ರ ಇನ್‌ಪುಟ್

ಚಿತ್ರ ವಿಷಯ ಐಟಂಗಳ ಪ್ರಕಾರವು `image_url` ಇಂದ `input_image` ಗೆ ಬದಲಾಗಿದೆ, ಮತ್ತು URL ನು ಗುಡಿಪು ಆಬ್ಜೆಕ್ಟ್‌ನಿಂದ ಫ್ಲ್ಯಾಟ್ ಸ್ಟ್ರಿಂಗ್‌ಗೆ ಬದಲಾಗಿದೆ.

### ಚಿತ್ರ ಇನ್‌ಪುಟ್ — ಮುಂಚೆ (ಚಾಟ್ ಪೂರ್ಣತೆಗಳು)
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

### ಚಿತ್ರ ಇನ್‌ಪುಟ್ — ನಂತರ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API, URL)
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

### ಚಿತ್ರ ಇನ್‌ಪುಟ್ — ನಂತರ (ಪ್ರತಿಕ್ರಿಯೆಗಳು API, base64)
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

> **ಪ್ರಮುಖ ಬದಲಾವಣೆಗಳು**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (ಗುಡಿಪು ಆಬ್ಜೆಕ್ಟ್) → `"image_url": "..."` (ಫ್ಲ್ಯಾಟ್ ಸ್ಟ್ರಿಂಗ್ — HTTPS URL ಅಥವಾ `data:image/...;base64,...` ಡೇಟಾ URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ (MAF) ಮೈಗ್ರೇಷನ್

**ನಿಮ್ಮ MAF ಆವೃತ್ತಿಯನ್ನು ಮೊದಲು ಪರಿಶೀಲಿಸಿ** — ಮೈಗ್ರೇಷನ್ MAF 1.0.0+ ಅಥವಾ ಪೂರ್ವ 1.0.0 ಬೀಟಾ/ಆರ್‌ಸಿ ಆವೃತ್ತಿಯ ಮೇಲೆ ಅವಲಂಭಿಸುತ್ತದೆ.

ಪರಿಶೀಲಿಸಲು: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ ನಲ್ಲಿ, `OpenAIChatClient` **ಈಗಾಗಲೇ ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಬಳಸುತ್ತದೆ** — ಯಾವುದೇ ಮೈಗ್ರೇಷನ್ ಅಗತ್ಯವಿಲ್ಲ.

ಕೋಡ್ ಬೇಸ್ ಹಳೆಯ `OpenAIChatCompletionClient` (ಅದು `chat.completions.create` ಬಳಕೆಮಾಡುತ್ತದೆ) ಅನ್ನು ಉಪಯೋಗಿಸುತ್ತಿದ್ದರೆ, ಅದನ್ನು `OpenAIChatClient` વડಗೆ ಬದಲಾಯಿಸಿ:

ಮುಂಚೆ:
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

### MAF ಪೂರ್ವ 1.0.0 (ಬೀಟಾ/ಆರ್‌ಸಿ ಬಿಡುಗಡೆಗಳು)

ಪೂರ್ವ 1.0.0 MAF ನಲ್ಲಿ `OpenAIChatClient` ಚಾಟ್ ಪೂರ್ಣತೆಗಳು ಬಳಸುತ್ತಿತ್ತು. `agent-framework-openai>=1.0.0` ಕ್ಕೆ ಅತ್ಯುತ್ತಮೀಕರಿಸಿ, ಅಲ್ಲಿ `OpenAIChatClient` ನೇರವಾಗಿ ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಅನ್ನು ಬಳಕೆಯಲ್ಲಿರುತ್ತದೆ.

> **ಗಮನಿಸಿ**: `Agent`, `MCPStreamableHTTPTool`, ಮತ್ತು ಇತರ MAF APIಗಳು ಬದಲಾವಣೆಗೊಳ್ಳಲಿಲ್ಲ — ಮಾತ್ರ ಕ್ಲೈಂಟ್ ಕ್ಲಾಸ್ ಆಮದು ಮತ್ತು ನಿರ್ಮಾಣ ಬದಲಾಯಿತು.

## LangChain (`langchain-openai`) ಮೈಗ್ರೇಷನ್

`ChatOpenAI()` ಗೆ `use_responses_api=True` ಸೇರಿಸಿ. ಜೊತೆಗೆ ಸಂದೇಶ ವಿಷಯವನ್ನು `.content` ರಿಂದ `.text` ಗೆ ಅಪ್ಡೇಟ್ ಮಾಡಿ.

ಮುಂಚೆ:
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

# ... ಏಜೆಂಟ್ ಆಹ್ವಾನ ...
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

# ... ಏಜೆಂಟ್ ಕರೆಯುವುದು ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **ಪ್ರಮುಖ ಬದಲಾವಣೆಗಳು**: (1) ಕಾನ್ಸ್ಟ್ರಕ್‌ಟರ್‌ನಲ್ಲಿ `use_responses_api=True`, (2) ಪ್ರತಿಕ್ರಿಯೆಗಳು ಸಂದೇಶದ ಮೇಲೆ `.content` → `.text`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->