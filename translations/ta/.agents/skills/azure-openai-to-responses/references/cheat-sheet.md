# பதில்கள் API சீட் (Python + Azure OpenAI)

> கீழே உள்ள அனைத்து குறியீட்டு துண்டுகளும் `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` என நினைத்து செயல்படுகின்றன மற்றும் `client` ஏற்கனவே ஆரம்பிக்கப்பட்டுள்ளது (client அமைப்பைப் பார்க்கவும்).

## அடிப்படை கோரிக்கை
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## கிளையண்ட் அமைப்பு — EntraID (சிபாரிசு)
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

## கிளையண்ட் அமைப்பு — API விசை
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## அசிங்க் கிளையண்ட் அமைப்பு — EntraID
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

## அசிங்க் கிளையண்ட் அமைப்பு — தெளிவான வாடிக்கையாளர் உடன் EntraID (பல வாடிக்கையாளர்)

Azure OpenAI வளம் **வேறொரு வாடிக்கையாளரில்** இருந்தால் இயல்புநிலை வாடிக்கையாளரை விட, அங்குள்ள சரிபத்திரிகைக்கு தெளிவான `tenant_id` வழங்கவும். இது மேம்பாடு/சோதனை சூழல்களில் சாதாரணம், இதில் மேம்படுத்தியவரின் வீட்டுவாடிக்கையாளர் வள வாடிக்கையாளருக்கு மாறுபடுகிறது.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# தயாரிப்புக்கான ManagedIdentityCredential (Azure Container செயலிகள், செயலி சேவை, மற்றும் பிற)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # பயனரால் ஒதுக்கிய நிர்வகிக்கப்பட்ட அடையாளம்
)
# உள்ளூர் dev க்கான AzureDeveloperCliCredential — தெளிவான tenant_id மிக முக்கியம்
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# சங்கிலி: முதலில் நிர்வகிக்கப்பட்ட அடையாளத்தை முயற்சி செய்க, பின்னர் azd CLI க்கு மாறு
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## அசிங்க் கிளையண்ட் மாற்றம் — முன்/பிறகு

முன்பு (பழையது):
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

பிறகு:
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

## முழு ஒத்திசைவு மாற்றம் — முன்/பிறகு

முன்பு (பழையது — Azure OpenAI உரையாடல் முடிவுகள்):
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

பிறகு (பதில்கள் API — Azure OpenAI v1 நுணுக்கம்):
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

## ஸ்ட்ரீமிங் (ஒத்திசைவு)
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
        print()  # கடைசியில் புதிய வரி
```

## ஸ்ட்ரீமிங் (அசிங்க்)
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

## இணையத் தொடுப்புத் தளம் ஸ்ட்ரீமிங் — பின்புலம் முதல் முன்னணி வரை வடிவமைப்பு

SSE/JSONL ஸ்ட்ரீம் செய்யும் இணையத் தொடுப்புத்தள்ளத்தை முன்னணிக்கு மாற்றும்போது, **பின்புல வரிசைப்படுத்தல் வடிவம்** மாற்றப்படும். புதிய பின்புல வெளியீடு முன்பணி அணுகல் முறைமைகளை பராமரிக்க வடிவமைக்கவேண்டும்; பின்னணி மாற்றங்கள் தேவையில்லை.

**முன்பு** — Chat Completions பின்புலம் பொதுவாக ஒவ்வொரு துண்டின் `choices[0]` அகராதியை வரிசைப்படுத்தியது:
```python
# பழையவு: ஒவ்வொரு துண்டிலும் முறையீட்ட செய்யப்பட்ட முழு தேர்வுத் தமிழியல்
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend வாசிப்பு: `response.delta.content` (தேர்வின் உள்ளடக்கத்தில் ஆழமான பாதை).

**பிறகு** — Responses API பின்புலம் மிகச் சிறிய வடிவத்தை வெளியிடுகிறது, அதே முன்னணி அணுகல் பாதையை பராமரிக்கிறது:
```python
# புதியது: முன் நான்கு தேவையானதையே வெளியிடுங்கள்
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend இன்னமும் `response.delta.content` வாசிக்கிறது — **பின்னணி மாற்றங்கள் தேவையில்லை**.

> **முக்கிய கவனிக்கை**: Responses API ஸ்ட்ரீமிங் வடிவம் (`event.type` + `event.delta`) Chat Completions (`chunk.choices[0].delta.content`) உடனான அடிப்படையில் வேறுபாடானது. ஆனால் உங்கள் பின்னணி முதல் முன்னணி ஒப்பந்தம் உங்கள் எண்ணத்திற்கு உட்பட்டது. முன்னணி ஏற்கனவே எதிர்பார்க்கும் வடிவிற்கு பின்புல வெளியீட்டை வடிவமைக்கவும்.

## ஸ்ட்ரீமிங் நிகழ்வு தொடர்

`stream: true` என்றபோது, API இந்த வரிசையில் நிகழ்வுகளை வெளியிடும்:
1. `response.created` – பதில் பொருள் ஆரம்பிக்கப்பட்டது
2. `response.in_progress` – உருவாக்கம் தொடங்கியது
3. `response.output_item.added` – வெளியீட்டு பொருள் உருவாக்கப்பட்டது
4. `response.content_part.added` – உள்ளடக்க பகுதி தொடங்கப்பட்டது
5. `response.output_text.delta` – எழுத்து துண்டுகள் (பல, ஒவ்வொன்றும் `delta: string`)
6. `response.output_text.done` – எழுத்து உருவாக்கம் முடிந்தது
7. `response.content_part.done` – உள்ளடக்க பகுதி முடிந்தது
8. `response.output_item.done` – வெளியீட்டு பொருள் முடிந்தது
9. `response.completed` – முழு பதில் நிறைவு

அடிப்படை எழுத்து ஸ்ட்ரீமிங்குக்கு, `response.output_text.delta` (எழுத்து துண்டுகளுக்கு) மற்றும் `response.completed` (முடிவுக்கு) மட்டும் கையாளவும்.

## இணையத் தொடுப்புகளில் ஸ்ட்ரீமிங் பிழை கையாளுதல்

இணையத் தொடுப்பில் ஸ்ட்ரீமிங் செய்யும்போது, அசிங்க் திரைவரிசையை `try/except` உடன் இழுப்பாற்றவும் மற்றும் பிழைகள் JSON ஆக வெளியிடவும், இதனால் முன்னணி அவற்றை நன்றாக காட்ட முடியும் (எ.கா., வீதக் கட்டுப்பாடுகள், தற்காலிக தோல்விகள்):

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

> **இது ஏன் முக்கியம்**: Azure OpenAI வீதக் கட்டுப்பாட்டின் போது `429 Too Many Requests` ஐ வழங்குகிறது. `try/except` இல்லாமல் ஸ்ட்ரீமிங் பதில் மௌனமாக முடிவடைகிறது. அதுடன், முன்னணி `{"error": "Too Many Requests"}` பெறுகிறது மற்றும் மீண்டும் முயற்சிக்க அறிவுறுத்தலை காட்ட முடியும்.

## ஸ்ட்ரீமிங் நிகழ்வு வகைகள் (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## உரையாடல் வடிவம்
```python
# பதில்கள் API உள்ளீட்டு வரிசை மூலம் உரையாடல் வடிவத்தை ஆதரிக்கிறது
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

## உள்ளடக்கம் வடிகட்டி பிழை கையாளுதல்

பிழை உடல் அமைப்பு Chat Completions இருந்து Responses API க்கு மாறியது.

முன்பு (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

பிறகு (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

முக்கிய மாற்றங்கள்:
- `innererror` மூடியானது **நீக்கப்பட்டது** — உள்ளடக்கம் வடிகட்டி விவரங்கள் இப்போது `error.body` உள்நிலை நிலைமையில் உள்ளன.
- `content_filter_result` (ஒற்றை) → `content_filters` (பல தொகுப்பு) மற்றும் அவற்றுக்குள் ஒவ்வொரு உள்ளீடிலும் `content_filter_results` (பல).
- உள்ளீடுகளில் ஒவ்வொன்றும் `blocked`, `source_type`, மற்றும் பிரிவு விபரங்களுடன் `content_filter_results` (பிரிவுகள்: `jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) உள்ளன.

முழு Responses API உள்ளடக்கம் வடிகட்டி பிழை உடல் வடிவம்:
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

## நேரடி HTTP மாற்றம் (requests/httpx)

பயன்பாடு Azure OpenAI REST ஐ நேரடியாக அழைப்பதால் SDK பயன்படுத்தப்படாவிட்டால்:

முன்பு (Chat Completions):
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

பிறகு (Responses API):
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

> **குறிப்பு**: `output_text` என்பது Python SDK இன் `Response` பொருளில் வசதிகரமான சொத்து. முதன்மை REST JSON பதில் மேல் நிலையாக `output_text` இல்லை — உரை `output[0].content[0].text` இல் உள்ளது.

## பலதரப்பு உரையாடல்
```python
# பதில்கள் API உடன் ஒரு உரையாடலை உருவாக்கவும்
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# உதவியாளரின் பதிலை உரையாடலில் சேர்க்கவும்
messages.append({"role": "assistant", "content": response.output_text})

# உரையாடலை தொடரவும்
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

உள்ளடக்கம் வகைப்படுத்தப்பட்ட பலதரப்பு (தெளிவான `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` மூலம் பலதரப்பு (மாற்று வழி)

உரையாடல் தொகுப்பை நீங்கள் நேரடியாக நிர்வகிப்பதற்கு பதிலாக, நீங்கள் பதில்களை
சேவையகம் இடத்தில் `previous_response_id` மூலம் சங்கிலி செய்யலாம். API ஒவ்வொரு பதிலையும் சேமித்து
முந்தைய சுற்றுக்களை தானாக முன்பிரித்து வைக்கும்.

```python
# முதல் முறை
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# அடுத்த முறை — புதிய பயனர் செய்தி + முந்தைய பதிலின் ID ஐ மட்டுமே அனுப்பு
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**எப்போது எதை பயன்படுத்துவது:**

| முறையுணர்வு | நன்மைகள் | অসুবিধைகள் |
|---|---|---|
| `input` தொகுப்பு (கையேடு) | வரலாறு மீது முழு கட்டுப்பாடு; குறைப்பது/சுருக்கல் செய்யலாம்; சேவையகத்தில் சேமிப்பதில்லை (`store=False`) | அதிக குறியீடு; நீங்கள் தொகுப்பை நிர்வகிக்க வேண்டும் |
| `previous_response_id` | எளிதான குறியீடு; தானாக சங்கிலி | `store=True` தேவை (இயல்புநிலை); உரையாடல் சேவையகத்தில் சேமிக்கப்படுகிறது; சுற்றுகளுக்கிடையில் வரலாற்றை மாற்ற முடியாது |

> **மாற்ற கவனிப்பு:** பெரும்பாலான Chat Completions பயன்பாடுகள் சொந்தச் செய்தி தொகுப்பை ஏற்கனவே நிர்வகிப்பதால், `input` தொகுப்பிற்கு மாற்றுதல் நேரடி 1:1 மாற்றமாகும். புதிய குறியீடு அல்லது உரையாடல் வரலாற்றை மாற்ற தேவையில்லாத போது `previous_response_id` பயன்படுத்தவும்.

## ஓ-சீரிஸ் காரண விளக்க மாதிரிகள் (o1, o3-mini, o3, o4-mini)

ஓ-சீரிஸ் மாதிரிகளுக்கு Responses API க்கு மாற்றியபோது தனித்துவமான அளவுரு கட்டுப்பாடுகள் உள்ளன.

### ஓ-சீரிஸ் அளவுரு வரைபடம்

| Chat Completions (ஓ-சீரிஸ்) | Responses API | குறிப்பு |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | அதிகமாக அமைக்கவும் (4096+) — காரண токன்கள் வரம்புக்கு எதிராக கணக்கிடப்படும் |
| `reasoning_effort` | `reasoning.effort` | இருந்தால் அதேபோல் வைக்கவும் (குறைந்த/இடைநிலை/அதிகம்) |
| `temperature` | அகற்று அல்லது `1` ஆக அமைக்கவும் | O-தொடர் மட்டுமே `1` ஏற்றுக்கொள்கிறது |
| `top_p` | அகற்று | o-தொடரில் ஆதரவு இல்லை |
| `seed` | அகற்று | Responses API யில் ஆதரவு இல்லை |

### O-தொடர் முன்/பிறகு

முன் (o-தொடர் உடன் Chat Completions):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

பிறகு (Responses API):
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

> **குறிப்பு**: O-தொடர் மாதிரிகள் காரணம் சொல்லும் போது வெளியீட்டு முன் டெல்டாக்களை தற்காலிகமாக சேமிக்கலாம். ஸ்ட்ரீமிங் செயல்படும், ஆனால் முதல் `response.output_text.delta` ஈவென்ட் GPT மாதிரிகளுடன் ஒப்பிடுகையில் சற்று தாமதமாக வரும்.

## காரணம் சொல்வதற்கான டோக்கன்களுக்கான அணுகல்
```python
# காரணியின் மாதிரிகள் உள்நிலை காரணத்தைப் பயன்படுத்துகின்றன — எத்தனை காரண டோக்கன்கள் பயன்படுத்தப்பட்டன என்பதை நீங்கள் பார்க்கலாம்
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

> **முக்கியம்**: காரண மாதிரிகளின் உள்ளக காரண செயல்முறையை கருத்தில் கொண்டு `max_output_tokens=1000` (50–200 அல்ல) பயன்படுத்தவும். மாதிரி இறுதி வெளியீட்டை உருவாக்குவதற்கு முன் காரண டோக்கன்களை பயன்படுத்துகிறது.

## கட்டமைக்கப்பட்ட வெளியீடு — JSON ஸ்கீமா
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

## கருவி பயன்பாடு

- கருவிகளுக்கு `tools` இல் **flat Responses API வடிவம்** உடன் செய்முறைகளை வரையறுக்கவும் — மேல் மட்டத்தில் `name`, `description`, மற்றும் `parameters` ( `function` கீழ் இல்லை).
- மாதிரி கருவி அழைக்கும்போது, உங்கள் செயலியில் அதை இயக்கு மற்றும் அடுத்த கோரிக்கையில் `input` உட்பட `function_call_output` உருப்படியை சேர்க்கவும்.
- ஸ்கீமாக்களை குறைந்தபட்சமாக வைக்கவும்; செயல்படுத்துவதற்கு முன் உள்ளீடுகளை சரிபார்க்கவும்.
- `strict: true` பயன்படுத்தும் போது, அனைத்து பண்புகளும் `required` இல் பட்டியலிடப்பட வேண்டும் மற்றும் `additionalProperties: false` அவசியம்.

> **⚠️ `pydantic_function_tool()` பொருந்தாது**: `openai.pydantic_function_tool()` உதவிக்கூறு பழைய Chat Completions உட்பட வடிவத்தை ( `{"type": "function", "function": {"name": ...}}`) இன்னும் உருவாக்குகிறது. `responses.create()` உடன் பயன்படுத்த வேண்டாம். கருவி ஸ்கீமாக்களை கைமுறையாக வரையறுக்கவும் அல்லது வெளியீட்டை தோண்டும் ஒரு கவரப்பை எழுதவும்.

### கருவி வரையறை வடிவம்

Responses API **flat** கருவி வடிவம் பயன்படுத்துகிறது — `name`, `description`, `parameters` மேல்நிலை சாவிகள் ( `function` கீழ் இல்லை).

**முன் (Chat Completions — உட்பட்ட):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**பிறகு (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

முழு எடுத்துக்காட்டு:
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

`strict: true` (ஸ்கீமா கட்டாயம்):
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
            "required": ["city_name"],       # அனைத்து சொத்துகளும் பட்டியலிடப்பட வேண்டும்
            "additionalProperties": False,   # கடும்பாணிக்கு தேவையானது
        },
    }
]
```

### கருவி அழைப்பை சுற்றி பயணம் (இயக்கு மற்றும் முடிவுகளை திருப்பி அனுப்பு)

மாதிரி கருவி அழைப்பு கோரும்போது, Chat Completions உள்ள `role: assistant` + `role: tool` வடிவத்தை பயன்படுத்தாமல் `response.output` உருப்படிகள் + `function_call_output` பயன்படுத்தவும்.

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
    # உரையாடலுக்கு மாடலின் function_call பொருட்களைச் சேர்க்கவும்
    messages.extend(response.output)

    # ஒவ்வொரு கருவியையும் செயல்படுத்தி முடிவுகளைச் சேர்க்கவும்
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # கருவி முடிவுகளுடன் இறுதி பதிலைப் பெறவும்
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### சில எடுத்துக்காட்டு கருவி அழைப்புகள்

`input` இல் சில எடுத்துக்காட்டுக் கருவி அழைப்புகளை வழங்கும்போது `function_call` மற்றும் `function_call_output` உருப்படிகள் பயன்படுத்து. அடையாளங்களும் `fc_` இல் தொடங்க வேண்டும்.

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
# உள்ளமைக்கப்பட்ட வலைத் தேடல் உதாரணம்
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## பட உள்ளீடு

படம் உள்ளடக்க உருப்படிகள் வகை `image_url` இருந்து `input_image` ஆக மாறியும் URL கீழ் உள்ள ஆப்ஜெக்டு நிலையில் இருந்தது ஒரு நேரடி சரமாக மாற்றப்பட்டுள்ளது.

### படம் உள்ளீடு — முன் (Chat Completions)
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

### படம் உள்ளீடு — பிறகு (Responses API, URL)
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

### படம் உள்ளீடு — பிறகு (Responses API, base64)
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

> **முக்கிய மாற்றங்கள்**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (உட்பட்ட ஆப்ஜெக்டு) → `"image_url": "..."` (நேரடி சரம் — HTTPS URL அல்லது `data:image/...;base64,...` தரவு URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft முகவர் கட்டமைப்பு (MAF) இடமாற்றம்

**உங்கள் MAF பதிப்பை முதலில் சரிபார்க்கவும்** — இடமாற்றம் நீங்கள் MAF 1.0.0+ அல்லது 1.0.0 முன் பீட்டா/ரிலீஸ் ஆக இருக்கிறீர்கள் என்பதைக் குறிக்கிறது.

சரிபார்க்க: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ இல், `OpenAIChatClient` **தயாரிப்புகளை Responses API உடன்** பயன்படுத்துகிறது — இடமாற்றம் தேவையில்லை.

பழைய `OpenAIChatCompletionClient` ( `chat.completions.create` பயன்படுத்துவது) பயன்படுத்தியிருந்தால், அதனை `OpenAIChatClient` ஆக மாற்றவும்:

முன்:
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

பிறகு:
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

### MAF 1.0.0 முன் (பீட்டா/RC வெளியீடுகள்)

MAF 1.0.0 முன், `OpenAIChatClient` Chat Completions பயன்படுத்தியது. `agent-framework-openai>=1.0.0` க்கு மேம்படுத்தவும், அங்கே `OpenAIChatClient` Responses API ஐ இயல்பாகப் பயன்படுத்தும்.

> **குறிப்பு**: `Agent`, `MCPStreamableHTTPTool` மற்றும் மற்ற MAF APIs மாற்றமில்லை — எந்தவொரு மாற்றமும் கேண்ணின் கிளைண்ட் வகுப்பின் இறக்குமதி மற்றும் உருவாக்கத்தில் மட்டுமே இருக்கிறது.

## LangChain (`langchain-openai`) இடமாற்றம்

`ChatOpenAI()`க்கு `use_responses_api=True` சேர்க்கவும். மேலும் செய்திகள் உள்ளடக்கம் அணுகலை `.content` இருந்து `.text` ஆக மாற்றவும்.

முன்:
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

# ... முகவர் அழைப்பு ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

பிறகு:
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

# ... முகவர் அழைப்பு ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **முக்கிய மாற்றங்கள்**: (1) கட்டமைтвщியில் `use_responses_api=True`, (2) பதிலில் `.content` → `.text`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->