# பதில்கள் API கூட்டு பட்டியல் (Python + Azure OpenAI)

> கீழ்காணும் அனைத்து உதாரணங்களும் `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` மற்றும் `client` முன்னதாகவே தொடங்கப்பட்டிருப்பதாக கருதுகின்றன (client அமைப்பு பார்க்கவும்).

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

## Client அமைப்பு — EntraID (பரிந்துரைக்கப்பட்டது)
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

## Client அமைப்பு — API விசை
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async client அமைப்பு — EntraID
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

## Async client அமைப்பு — தெளிவான tenant உடன் EntraID (பன்மை-வாடிக்கை)

Azure OpenAI ஆதாரம் **வேறுபட்ட tenant** இல் இருந்தால், விடுவிக்கப்பட்ட tenant இல்லை என்றால், `tenant_id`-ஐ தெளிவாக கடவுச் சான்று அளிக்கும் போது அனுப்பவும். இது வளர்ச்சி/சோதனை சூழல்களில் பொதுவாக, உருவாக்குனரின் முகப்பு tenant ஆதாரம் tenant-இல் வேறுபடும்போது உண்டு.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# தயாரிப்பிற்கான ManagedIdentityCredential (Azure Container Apps, App Service, மற்றும் பிற)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # பயனர்-ஒதுக்கப்பட்ட மேலாண்மை அடையாளம்
)
# உள்ளூர் டெவலப்பிற்கான AzureDeveloperCliCredential — தெளிவான tenant_id முக்கியம்
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# சங்கிலி: முதலில் மேலாண்மை அடையாளத்தை முயற்சிக்கவும், பின்னர் azd CLI-க்கு மறு முயற்சி செய்யவும்
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async client மாற்றம் — முன்/பின்

முன்பு (பழையது):
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

பின்னர்:
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

## முழு முரணான மாற்றம் — முன்னும்/பின்னும்

முன்பு (பழையது — Azure OpenAI உரையாடல் கூடுதல்):
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

பின்னர் (பதில்கள் API — Azure OpenAI v1 முகவரி):
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

## ஒளிபரப்பல் (சுமூகமானSynchronuous)
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

## ஒளிபரப்பல் (அசிங்க்Asynchronous)
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

## இணைய பயன்பாடு ஒளிபரப்பு — பின்புறம்-முன்புறம் வடிவம்

SSE/JSONL ஒளிபரப்பை முன்புறத்துக்கு மாற்றும்போது, **பின்புற தொடர் வடிவம்** மாறுகிறது. புதிய பின்புற வெளியீட்டை உருவாக்கி முன்னிலை முன்புற அணுகல் வழிகளை காக்கவும், இதனால் முன்புறத்தில் மாற்றங்கள் தேவையில்லை.

**முன்பாக** — உரையாடல் கூடுதல் பின்புறம் பொதுவாக ஒவ்வொரு துண்டின் `choices[0]` அகராதியை தொடர் வடிவில் சேமித்தது:
```python
# பழையது: பகுதி ஒன்றுக்கு பொருந்தும் முழு தேர்வு dict சீரமைக்கப்பட்டது
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
முன்புற வாசிப்பு: `response.delta.content` (ஆழமான பாதை).

**பின்னர்** — பதில்கள் API பின்புறம் அதே முன்புற அணுகல் பாதையை பாதுகாத்த சுருக்கமான வடிவத்தை அளிக்கிறது:
```python
# புதியது: முன் முனையில் தேவையானவை மட்டுமே வெளியிடவும்
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
முன்புறம் இன்னும் `response.delta.content`-ஐ வாசிக்கிறது — **எந்த முன்புற மாற்றமும் தேவையில்லை**.

> **முக்கிய தகவல்**: பதில்கள் API ஒளிபரப்பு வடிவம் (`event.type` + `event.delta`) உரையாடல் கூடுதலுடன் (`chunk.choices[0].delta.content`) அடிப்படையாகவே வேறுபட்டவை. ஆனால் உங்கள் பின்புறம்-முன்புற ஒப்பந்தம் உங்கள் விருப்பப்படி உருவாக்கலாம். பின்புற வெளியீட்டை முன்புறம் எதிர்பார்க்கும் வடிவத்திற்கு அமைக்கவும்.

## ஒளிபரப்பு நிகழ்ச்சி தொடர்வு

`stream: true` என இருந்தால், API நிகழ்வுகளை கீழ்காணும் முறையில் அனுப்பும்:
1. `response.created` – பதில் பொருள் துவக்கம்
2. `response.in_progress` – உருவாக்கம் தொடக்கம்
3. `response.output_item.added` – வெளியீடு பொருள் உருவாக்கம்
4. `response.content_part.added` – உள்ளடக்க பகுதி தொடக்கம்
5. `response.output_text.delta` – உரை துண்டுகள் (பல, ஒவ்வொன்றும் `delta: string` கொண்டது)
6. `response.output_text.done` – உரை உருவாக்கம் முடிந்தது
7. `response.content_part.done` – உள்ளடக்க பகுதி முடிந்தது
8. `response.output_item.done` – வெளியீடு பொருள் முடிந்தது
9. `response.completed` – முழுமையான பதில் முடிந்தது

அடிப்படை உரை ஒளிபரப்புக்கு, `response.output_text.delta` (உரை துண்டுகளுக்காக) மற்றும் `response.completed` (முடிவுக்கு) மட்டுமே கையாளவும்.

## இணைய பயன்பாடுகளில் ஒளிபரப்பு பிழை கையாளல்

இணைய பயன்பாட்டில் ஒளிபரப்பில் `try/except` மூலம் அசிங்க் இடைமுகத்தை சுற்றவும் மற்றும் பிழைகளை JSON வடிவில் வெளியிடவும், இதனால் முன்புறம் அவற்றை சுட்டிக்காட்டியுடன் காட்டலாம் (உதாரணத்திற்கு, வரம்பு மீறல்கள், தற்காலிக தோல்விகள்):

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

> **ஏன் இது முக்கியம்?**: Azure OpenAI வரம்பு மீறும்போது `429 Too Many Requests` தெரிவிக்கிறது. `try/except` இல்லாமல் ஒளிபரப்பு பதில் மௌனமாக முடிவடைகிறது. இதன் மூலம் முன்புறம் `{"error": "Too Many Requests"}` பெறுவதால் மீண்டும் முயற்சிக்கவும் கூறலாம்.

## ஒளிபரப்பு நிகழ்ச்சித் வகைகள் (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## உரையாடல் வடிவம்
```python
# பதில்கள் API உள்ளீட்டு வரிசையின் மூலம் உரையாடல் வடிவமைப்பை ஆதரிக்கிறது
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

## உள்ளடக்க வடிகட்டி பிழை கையாளல்

பிழை உடல் வடிவமைப்பு உரையாடல் கூடுதல் என் பதில்கள் API இடையே மாறியது.

முன் (உரையாடல் கூடுதல்):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

பின்னர் (பதில்கள் API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

முக்கிய வேறுபாடுகள்:
- `innererror` பொருத்தி **இன்று இல்லை** — உள்ளடக்க வடிகட்டு விவரங்கள் தற்போது `error.body`-ன் மேல்நிலை பகுதியில் உள்ளன.
- `content_filter_result` (ஒற்றை) → `content_filters` (பலவகை வரிசை) உட்பட `content_filter_results` (பலவகை) உள்ளன.
- `content_filters`-ல் ஒவ்வொரு நுழைவுக்கும் `blocked`, `source_type`, மற்றும் `content_filter_results` உள்ளன, ஒவ்வொன்றும் பிரிவு விவரங்கள் கொண்டவை (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

முழு பதில்கள் API உள்ளடக்க வடிகட்டி பிழை உடல் வடிவம்:
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

## Raw HTTP மாற்றம் (requests/httpx)

பயன்பாடு Azure OpenAI REST நேரடியாக அழைத்தால் SDK பயன்படுத்தாமலும்:

முன் (உரையாடல் கூடுதல்):
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

பின்னர் (பதில்கள் API):
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

> **குறிப்பு**: `output_text` என்பது Python SDK இன் `Response` பொருளில் வசதிக்கான பண்பு ஆகும். மூல REST JSON பதிலில் மேல்நிலை `output_text` களம் இல்லை — உரை `output[0].content[0].text` இல் உள்ளது.

## பன்முறை உரையாடல்
```python
# பதில்கள் API உடன் உரையாடலை கட்டிக்கொள்ளுங்கள்
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# உதவியாளரின் பதிலை உரையாட்டில் சேர்க்கவும்
messages.append({"role": "assistant", "content": response.output_text})

# உரையாட்டை தொடரவும்
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

உள்ளடக்க வகை பெற்ற பன்முறை (தெளிவான `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### பன்முறை `previous_response_id` மூலம் (மாற்று வழி)

உரையாடல் வரிசையை நீங்களே நிர்வகிப்பதற்குப் பதிலாக, பதில்களை
சேவையகப் பக்கம் `previous_response_id` கொண்டு சங்கிலி செய்யலாம். API ஒவ்வொரு பதிலையும் சேமித்து
முன்பு உள்ள முறுகலை தானாக முன்னிட்டு சேர்க்கிறது.

```python
# முதல் சுழற்சி
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# அடுத்த சுழற்சிகள் — புதிய பயனர் செய்தியையும் முந்தைய பதில் ஐடியையும் அனுப்பவும்
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**ஏதேனும் எப்போது பயன்படுத்துவது:**

| அணுகல் | நன்மைகள் | குறைபாடுகள் |
|---|---|---|
| `input` வரிசை (கையால்) | வரலாறில் முழு கட்டுப்பாடு; சுருக்கம்/சுருக்கம் செய்யலாம்; சேவையக பக்க சேமிப்பு தேவை இல்லை (`store=False`) | அதிகக் குறியீடு; வரிசையை நீங்கள் நிர்வகிக்க வேண்டும் |
| `previous_response_id` | குறைந்த குறியீடு; தானாக சங்கிலி | `store=True` தேவை (இயல்பானது); உரையாடலை சேவையகத்தில் வைத்திருக்கும்; முறுகலை மாற்ற முடியாது |

> **மாற்று குறிப்பு:** பெரும்பாலான உரையாடல் கூடுதல் பயன்பாடுகள் தங்களது சொந்த செய்தி வரிசையை முகாமை செய்கின்றன, ஆகவே `input` வரிசைக்குப் பரிமாற்றம் நேரடியான 1:1 மாற்றம். புதிய குறியீடு அல்லது உரையாடல் வரலாறை மாற்ற வேண்டாமெனில் `previous_response_id` பயன்படுத்தவும்.

## O-வரிசை கோட்பாடுகள் (o1, o3-mini, o3, o4-mini)

O-வரிசை மாதிரிகள் பதில்கள் APIக்கு மாற்றும் போது தனித்துவமான அளவுரு கட்டுப்பாடுகள் கொண்டவை.

### o-வரிசைக்கான அளவுரு மேப்பிங்

| உரையாடல் கூடுதல் (o-வரிசை) | பதில்கள் API | குறிப்புக்கள் |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | உயர்ந்த அளவு (4096+)-க்கு அமைக்கவும் — கொள்கை குறியடிகள் வரம்புக்கு பிணைக்கப்படுகின்றன |
| `reasoning_effort` | `reasoning.effort` | உள்ளது என்றால் அதன் போலவே வைக்கவும் (குறைந்த/நடுத்தர/உயர்ந்த) |
| `temperature` | நீக்கவும் அல்லது `1` ஆக அமைக்கவும் | O-வரிசை மட்டும் `1` ஐ ஏற்கிறது |
| `top_p` | நீக்கவும் | O-வரிசைக்கு ஆதரவு இல்லை |
| `seed` | நீக்கவும் | பதில்கள் APIக்கு ஆதரவு இல்லை |

### O-வரிசை முன்/பின்

முன் (உரையாடல் கூடுதல் உடன் o-வரிசை):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

பின்னர் (பதில்கள் API):
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

> **குறிப்பு**: O-வரிசை மாதிரிகள் காரணமாய் உரையை வெளிப்படுத்தும் முன் வெளியீட்டை துப்புரவு செய்யலாம். ஒளிபரப்பு இன்னும் செயல்படும், ஆனால் முதலாவது `response.output_text.delta` நிகழ்வு GPT மாதிரிகளைவிட அதிக நேரம் எடுக்கலாம்.

## காரணமிடும் குறியடிகள் அணுகல்
```python
# கருதுக் கூறும் மாதிரிகள் அடிப்படைக் காரணிப்பை பயன்படுத்துகின்றன — எத்தனை காரணிப்பு குறிச்சொற்கள் பயன்படுத்தப்பட்டன என்பதை நீங்கள் பார்க்க முடியும்
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

> **முக்கியம்**: காரணமிடும் மாதிரிகளின் உள்ளக நிகழ்வுகளை கணக்கில் கொள்வதற்கு `max_output_tokens=1000` (50–200 அல்ல) பயன்படுத்தவும். மாதிரி காரணமிடும் குறியடிகள் உள்ளகமாகப் பயன்படுத்தி இறுதி வெளியீட்டை உருவாக்குகிறது.

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

- `tools` இல் செயல்பாடுகளை flat பதில்கள் API வடிவில் வரையறுக்கவும் — `name`, `description`, மற்றும் `parameters` மேல்நிலை விசைகளாக (function-இல் இல்லை).
- மாதிரி கருவியை அழைக்கும்போது உங்கள் பயன்பாட்டில் அதைச் செயல்படுத்தவும் மற்றும் அடுத்த கோரிக்கையில் `function_call_output` உருப்படியை இணைக்கவும்.
- ஸ்கீமாவை மிகக் குறைவாக வைக்கவும்; செயல்படுத்தும் முன் உள்ளீடுகளை சரிபார்க்கவும்.
- `strict: true` பயன்படுத்தும்போது, அனைத்து பண்புகளும் வழமையாக `required`-ல் பட்டியலிடப்பட்டிருக்க வேண்டும், மற்றும் `additionalProperties: false` கட்டாயம்.

> **⚠️ `pydantic_function_tool()` பொருந்தாது**: `openai.pydantic_function_tool()` உதவியாளர் இன்னும் பழைய உரையாடல் கூடுதல் அடுக்கான வடிவத்தை உருவாக்குகிறது (`{"type": "function", "function": {"name": ...}}`). `responses.create()` உடன் இதைப் பயன்படுத்த வேண்டாம். கருவி ஸ்கீமாவை கையால் வரையறுக்கவும் அல்லது வெளியீட்டை சுருக்க ஒரு மூடியை எழுதவும்.

### கருவி வரையறை வடிவம்

பதில்கள் API **flat** கருவி வடிவத்தை பயன்படுத்துகிறது — `name`, `description`, `parameters` மேல்நிலை விசைகளாக (function-இல் இல்லை).

**முன்பு (உரையாடல் கூடுதல் — அடுக்குகள்):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**பின்னர் (பதில்கள் API — flat):**
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

`strict: true` உடன் (ஸ்கீமா கட்டாயம்):
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
            "required": ["city_name"],       # அனைத்து பண்புகளும் பட்டியலிடப்பட வேண்டும்
            "additionalProperties": False,   # கடுமையான முறைக்கு அவசியம்
        },
    }
]
```

### கருவி அழைப்பு சுற்று பயணம் (செயல்படுத்தி முடிவுகளை திருப்பி அனுப்புதல்)

மாதிரி கருவி அழைப்பை கோரும்போது, `response.output` உருப்படிகள் + `function_call_output` பயன்படுத்தவும் — உரையாடல் கூடுதல் `role: assistant` + `role: tool` படிவம் **இல்லை**.

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
    # மொடல் function_call உருப்படிகளை உரையாடலில் சேர்க்கவும்
    messages.extend(response.output)

    # ஒவ்வொரு கருவியையும் இயக்கு மற்றும் முடிவுகளை சேர்க்கவும்
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # கருவி முடிவுகளுடன் இறுதி பதிலைப் பெற வேண்டும்
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### சில-தாள்கள் கருவி அழைப்புச் சான்றுகள்

`input` இல் கருவி அழைப்புகளின் சில-தாள்கள் எடுத்துக்காட்டுகளை அளிக்கும் போது `function_call` மற்றும் `function_call_output` உருப்படிகளைப் பயன்படுத்தவும். அடையாளங்கள் `fc_`-ஆல் தொடங்க வேண்டும்.

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
# உள்ளமைவான வலைத் தேடல் உதாரணம்
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## படம் உள்ளீடு

பட உள்ளடக்க உருப்படிகள் வகை `image_url` இருந்து `input_image` ஆக மாறுகிறது, மற்றும் URL அட்டவணை அடுக்கில் இருந்து நேரடியான சரமாக மாறுகிறது.

### படம் உள்ளீடு — முன்பு (உரையாடல் கூடுதல்)
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

### படம் உள்ளீடு — பின்னர் (பதில்கள் API, URL)
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

### படம் உள்ளீடு — பின்னர் (பதில்கள் API, base64)
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

> **முக்கிய மாற்றங்கள்**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (அடுக்கு பொருள்) → `"image_url": "..."` (நேரடியான சரம் — HTTPS URL அல்லது `data:image/...;base64,...` URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) மாற்றம்

**முதலில் உங்கள் MAF பதிப்பைக் காண்க** — மாற்றம் MAF 1.0.0+ அல்லது 1.0.0க்கு முன் beta/rc ஆக இருக்கின்றதா என்பதை சார்ந்தது.

சரிபார்க்க: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ இல், `OpenAIChatClient` **இப்போது பதில்கள் API-ஐப் பயன்படுத்துகிறது** — மாற்றம் தேவையில்லை.

பழைய `OpenAIChatCompletionClient` (`chat.completions.create` பயன்படுத்தும்) பயன்பாட்டில் இருந்தால், இதை `OpenAIChatClient` ஆக மாற்றவும்:

முன்பு:
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

பின்னர்:
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

### MAF 1.0.0க்கு முன் (beta/rc வெளியீடுகள்)

MAF 1.0.0க்கு முன், `OpenAIChatClient` உரையாடல் கூடுதலை பயன்படுத்தியது. `agent-framework-openai>=1.0.0`க்கு மேம்படுத்தவும், இப்போது `OpenAIChatClient` இயல்பாக பதில்கள் API-ஐ பயன்படுத்தும்.

> **குறிப்பு**: `Agent`, `MCPStreamableHTTPTool`, மற்றும் மற்ற MAF API-கள் மாற்றமற்றவை — சா்லண்டையை தவிர க்ளையண்ட் வகுப்பு இறக்கம் மற்றும் உருவாக்கம் மட்டுமே மாறுகிறது.

## LangChain (`langchain-openai`) மாற்றம்

`ChatOpenAI()` க்கு `use_responses_api=True` சேர்க்கவும். மேலும் செய்தி உள்ளடக்க அணுகலை `.content` இருந்து `.text` ஆக மாற்றவும்.

முன்பு:
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

பின்னர்:
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

> **முக்கிய மாற்றங்கள்**: (1) கட்டுமானத்தில் `use_responses_api=True`, (2) பதில் செய்திகள் `.content` → `.text`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->