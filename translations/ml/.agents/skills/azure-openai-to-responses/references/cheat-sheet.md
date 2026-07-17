# Responses API ചീറ്റ്ഷീറ്റ് (Python + Azure OpenAI)

> താഴെ എല്ലാ സ്നിപ്പെറ്റുകളും `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ആണെന്ന് ধরেകൊള്ളുന്നുണ്ട്, കൂടാതെ `client` ഇതിനകം സജ്ജമാക്കിയതാണ് (ക്ലയന്റ് സെറ്റപ്പിന് കാണുക).

## അടിസ്ഥാന അഭ്യർത്ഥന
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## ക്ലയന്റ് സെറ്റപ്പ് — EntraID (ശിപാർശ ചെയ്യുന്നു)
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

## ക്ലയന്റ് സെറ്റപ്പ് — API കീ
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## അസിങ്ക് ക്ലയന്റ് സെറ്റപ്പ് — EntraID
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

## അസിങ്ക് ക്ലയന്റ് സെറ്റപ്പ് — EntraID വ്യക്തമായ ടെന്നന്റ് ഉപയോഗിച്ച് (മൾട്ടി-ടെന്നന്റ്)

Azure OpenAI റിസോഴ്സ് **വ്യത്യസ്ത ടെന്നന്റിലാണെങ്കിൽ** ഡീഫോൾട്ടിൽ തന്നേക്കാൾ, ക്രെഡൻഷ്യലിന് `tenant_id` തെളിവായി നൽകുക. ഇത് ഡെവലപ്പർ ഹോം ടെന്നന്റ് റിസോഴ്‌സ് ടെന്നന്റിനേക്കാൾ വ്യത്യസ്തമായിരിക്കുന്ന ഡെവ്/ടെസ്റ്റ് സാഹചര്യങ്ങളിൽ സാധാരണമാണ്.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# പ്രൊഡക്ഷനായി ManagedIdentityCredential (Azure Container Apps, App Service മുതലായവ)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # ഉപയോക്താവ് നിർധാരിച്ച മാനേജ്ഡ് ഐഡൻറ്റിറ്റി
)
# ലൊക്കൽ ഡെവലപ്മെന്റിന് AzureDeveloperCliCredential — വ്യക്തമായ tenant_id അനിവാര്യമാണ്
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# ചൈൻ: ആദ്യം മാനേജ്ഡ് ഐഡൻറ്റിറ്റി ശ്രമിക്കുക, പരാജയപ്പെട്ടാൽ azd CLI ഉപയോഗിക്കുക
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## അസിങ്ക് ക്ലയന്റ് മൈഗ്രേഷൻ — മുമ്പും/ശേഷവും

മുമ്പ് (ഡീപ്രിക്കേറ്റഡ്):
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

ശേഷം:
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

## പൂർണ്ണ സിങ്ക് മൈഗ്രേഷൻ — മുമ്പും/ശേഷവും

മുമ്പ് (ലേഗസി — Azure OpenAI ചാറ്റ് കോംപ്ലീഷനുകൾ):
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

ശേഷം (Responses API — Azure OpenAI v1 എൻഡ്പോയിന്റ്):
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

## സ്ട്രീമിംഗ് (സിങ്ക്)
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
        print()  # അവസാനത്തില്‍ ന്യൂലൈന്‍
```

## സ്ട്രീമിംഗ് (അസിങ്ക്)
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

## വെബ് ആപ്പ് സ്ട്രീമിംഗ് — ബാക്ക്‌എൻഡിൽ നിന്നുള്ള ഫ്രീണ്ട്എൻ‌ഡ് രൂപം

SSE/JSONL സ്ട്രീം ചെയ്യുന്ന ഒരു വെബ് ആപ്പ് front-end-ലേക്ക് മൈഗ്രേറ്റ് ചെയ്യുമ്പോൾ, **ബാക്ക്‌എൻഡ് സെറിയലൈസേഷൻ ഫോർമാറ്റ്** മാറുന്നു. പുതിയ ബാക്ക്‌എൻഡ് ഔട്ട്പുട്ട് നിലവിലുള്ള ഫ്രന്റ്എൻഡിന്റെ ആക്സസ് പാറ്റേണുകൾ സൂക്ഷിക്കാനായി രൂപകല്പന ചെയ്യുക, അതായത് ഫ്രന്റ്എൻഡിൽ മാറ്റങ്ങൾ ആവശ്യമില്ല.

**മുമ്പ്** — ചാറ്റ് കോംപ്ലീഷൻസ് ബാക്ക്‌എൻഡ് സാധാരണയായി ഓരോ chunk-ഉം `choices[0]` dict സീരിയലൈസ് ചെയ്തു:
```python
# പഴയത്: ചങ്ക്‌പ്രതി സീരിയലൈസ്ഡ് പൂർണ്ണ തിരഞ്ഞെടുപ്പ് നിഘണ്ടു
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend വായിക്കുന്നത്: `response.delta.content` (choice ഒബ്ജക്റ്റിലേക്ക് ആഴമുള്ള പാത).

**ശേഷം** — Responses API ബാക്ക്‌എൻഡ് അതേ ഫ്രന്റ്എൻഡ് ആക്സസ് പാത്ത് സംരക്ഷിക്കുന്ന മിനിമൽ രൂപം പുറപ്പെടുവിക്കുന്നു:
```python
# പുതിയത്: ഫ്രണ്ട്എൻഡ് ആവശ്യമായതെല്ലാം മാത്രമേ പുറപ്പെടുവിക്കുകയുള്ളു
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend ഇപ്പോഴും `response.delta.content` വായിക്കുന്നു — **ഫ്രന്റ്എൻഡിൽ മാറ്റങ്ങൾ ആവശ്യമില്ല**.

> **പ്രധാന മനസിലാക്കേണ്ടത്**: Responses API സ്ട്രീമിംഗ് രൂപം (`event.type` + `event.delta`) ചാറ്റ് കോംപ്ലീഷൻസ് (`chunk.choices[0].delta.content`) നേക്കാൾ അടിസ്ഥാനപരമായും വ്യത്യസ്തമാണ്. എന്നാൽ നിങ്ങളുടെ ബാക്ക്‌എൻഡ്-ഫ്രന്റ്എൻഡ് കരാർ നിങ്ങൾ നിർവചിക്കേണ്ടതാണ്. ബാക്ക്‌എൻഡ് ഔട്ട്പുട്ട് ഫ്രന്റ്എൻഡ് ഇതിനകം പ്രതീക്ഷിക്കുന്നതിൽ പൊരുത്തപ്പെടുന്ന രൂപത്തിലാക്കുക.

## സ്ട്രീമിംഗ് ഇവന്റ് ക്രമം

`stream: true` ആണെങ്കിൽ, API ഇവന്റ് ഈ ക്രമത്തിൽ പുറപ്പെടുവിക്കുന്നു:
1. `response.created` – പ്രതികരണ ഒബ്ജക്റ്റ് ആരംഭിച്ചു
2. `response.in_progress` – ജനറേഷൻ ആരംഭിച്ചു
3. `response.output_item.added` – ഔട്ട്പുട്ട് ഐറ്റം സൃഷ്ടി
4. `response.content_part.added` – ഉള്ളടക്ക ഭാഗം ആരംഭിച്ചു
5. `response.output_text.delta` – ടെക്സ്റ്റ് ചങ്കുകൾ (അനേകം, ഓരോതിലും `delta: string`)
6. `response.output_text.done` – ടെക്സ്റ്റ് ജനറേഷൻ പൂർത്തിയായി
7. `response.content_part.done` – ഉള്ളടക്ക ഭാഗം പൂർത്തിയായി
8. `response.output_item.done` – ഔട്ട്പുട്ട് ഐറ്റം പൂർത്തിയായി
9. `response.completed` – മുഴുവൻ പ്രതികരണവും പൂർത്തിയായി

അടിസ്ഥാന ടെക്സ്റ്റ് സ്ട്രീമിംഗിനായി, `response.output_text.delta` (ടെക്സ്റ്റ് ചങ്കുകൾക്ക്) മാത്രവും `response.completed` (പൂർത്തീകരണത്തിന്) മാത്രം കൈകാര്യം ചെയ്യുക.

## വെബ് ആപ്പുകളിൽ സ്ട്രീമിംഗ് പിശക് കൈകാര്യം ചെയ്യൽ

വെബ് ആപ്പിൽ സ്ട്രീമിംഗ് ചെയ്യുമ്പോൾ, അസിങ്ക് ഇറ്ററേഷൻ `try/except` ൽ പാക്ക് ചെയ്ത് പിശകുകൾ JSON ആയി പുറത്തിറക്കുക, ώστε ഫ്രന്റ്എൻഡ് അവ സൌകര്യത്തോടെ പ്രദർശിപ്പിക്കാൻ (ഉദാ: റേറ്റ് ലിമിറ്റുകൾ, താൽക്കാലിക പരാജയങ്ങൾ):

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


> **ഇത് എന്തുകൊണ്ട് പ്രധാനമാണ്**: Azure OpenAI rate limiting സമയത്ത് `429 Too Many Requests` തിരികെ നൽകുന്നു. `try/except` ഇല്ലാതെ, സ്ട്രീമിംഗ് പ്രതികരണങ്ങൾ നിശബ്ദമായി മരിക്കും. അതോടെ, фрон്‌എൻഡ് `{"error": "Too Many Requests"}` സ്വീകരിക്കുകയും ഒരു retry പ്രോംപ്റ്റ് കാണിക്കുകയും ചെയ്യാം.

## സ്ട്രീമിംഗ് ഇവന്റ് തരങ്ങൾ (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## സംഭാഷണ ഫോർമാറ്റ്
```python
# പ്രതികരണങ്ങൾ API ആമുഖ അറേവിലൂടെ സംഭാഷണ ഫോർമാറ്റ് പിന്തുണയ്ക്കുന്നു
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

## ഉള്ളടക്കം ഫിൽട്ടർ പിശക് കൈകാര്യം ചെയ്യൽ

പിശക് ബോഡി ഘടന Chat Completions-ലോ Responses API-ലോ മാറിയിട്ടുണ്ട്.

മുൻപ് (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

പിന്നീട് (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

പ്രധാന വ്യത്യാസങ്ങൾ:
- `innererror` കവറേജ് **അകന്നു പോയി** — ഉള്ളടക്കം ഫിൽട്ടർ വിശദാംശങ്ങൾ ഇപ്പോൾ `error.body`ന്റെ മുകളിൽ ആണ്.
- `content_filter_result` (ഏകവചനം) → `content_filters` (ബഹുവചന ഫലകം) ഉള്ളിൽ `content_filter_results` (ബഹുവചനം) ഉള്ള ഫലകങ്ങൾ.
- `content_filters`ലെ ഓരോ എൻട്രിയിലും `blocked`, `source_type`, കൂടാതെ ഓരോ വിഭാഗം വിശദാംശങ്ങളായ `content_filter_results` (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) ഉൾക്കൂടുന്നു.

Responses API-ലെ പൂർണ്ണ ഉള്ളടക്കം ഫിൽട്ടർ പിശക് ബോഡി ശൈലി:
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

## റോ ഹ്റ്റ്‌റ്റിപി മാറ്റം (requests/httpx)

SDK ഉപയോഗിക്കാതെ Azure OpenAI REST നേരിട്ട് കേൾക്കുമ്പോൾ:

മുൻപ് (Chat Completions):
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

പിന്നീട് (Responses API):
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

> **കുറിപ്പ്**: Python SDKയിലെ `Response` объектаയിൽ `output_text` ഒരു സൗകര്യപ്രദമായ қасиതയാണ്. വീഥി REST JSON പ്രതികരണം മേൽനിരയിലുള്ള `output_text` ഫീൽഡ് ഇല്ല — ടെക്സ്‌റ്റ് `output[0].content[0].text`ൽ ആണ്.

## ബഹുതവണ സംവാദം
```python
# Responses API ഉപയോഗിച്ച് സംവാദം നിർമ്മിക്കുക
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# അടിസ്ഥിതാവിന്റെ പ്രതികരണം സംവാദത്തിലേക്ക് ചേർക്കുക
messages.append({"role": "assistant", "content": response.output_text})

# സംവാദം തുടരുക
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

ഉള്ളടക്കം-ടൈപ്പ് ചെയ്ത ബഹുതവണ (സ്പഷ്ട `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` വഴി ബഹുതവണ (മറുവിധി)

സംഭാഷണ അറേ നിങ്ങൾ സ്വയം കൈകാര്യം ചെയ്യുന്നത് പകരം, `previous_response_id` ഉപയോഗിച്ച് സെർവർ-സൈഡിൽ 
പ്രതികരണങ്ങൾ ചെയിൻ ചെയ്യാം. API ഓരോ പ്രതികരണവും സൂക്ഷിച്ച് മുന് തവണകൾ സ്വയം മുൻപേ ചേര്ക്കുന്നു.


```python
# ആദ്യമായുള്ള തിരിയല്
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# തുടർന്നുള്ള തിരികൾ — പുതിയ ഉപയോക്തൃ സന്ദേശവും മുൻത്തെ പ്രതികരണ ഐഡിയും മാത്രമേ പാസ്സാക്കൂ
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**എപ്പോൾ ഏതു ഉപയോഗിക്കും:**

| സമീപനം | ഗുണങ്ങൾ | ദോഷങ്ങൾ |
|---|---|---|
| `input` അറേ (അനുയായി) | ചരിത്രം പൂർണ്ണ നിയന്ത്രണം; ട്രീമോ സംഗ്രഹണo ചെയ്യാം; സെർവർ-സൈഡ് സംഭരണം ആവശ്യമില്ല (`store=False`) | കൂടുതൽ കോഡ്; നിങ്ങൾ അറേ കൈകാര്യം ചെയ്യും |
| `previous_response_id` | ലളിതമായ കോഡ്; സ്വയം ചെയിൻ ചെയ്യൽ | `store=True` (ഡീഫോൾട്ട്) ആവശ്യമുണ്ട്; സെർവർ-സൈഡ് സംഭരണം; തവണകളിലിടയിൽ ചരിത്രം മാറ്റാനാകില്ല |

> **മാറ്റം കുറിപ്പ്:** കൂടുതലായും Chat Completions ആപ്പുകൾ അവർയുടെ സന്ദേശ അറേ നേരത്തേ കൈകാര്യം ചെയ്യുന്നു, അതിനാൽ `input` അറേ ആയി മാറ്റുന്നത് നേരിട്ടുള്ള 1:1 മാറ്റമാണ്. പുതിയ കോഡിന് `previous_response_id` ഉപയോഗിക്കുക അല്ലെങ്കിൽ സംവാദ ചരിത്രം കൈകാര്യം ചെയ്യേണ്ടത് ഇല്ലെങ്കിൽ.

## ഒ-ശ്രേണി റീജണിംഗ് മോഡലുകൾ (o1, o3-mini, o3, o4-mini)

Responses API ലേക്കുള്ള മാറ്റത്തിൽ ഒ-ശ്രേണി മോഡലുകൾക്ക് പ്രത്യേക പാരാമീറ്റർ നിയന്ത്രണങ്ങൾ ഉണ്ട്.

### ഒ-ശ്രേണിക്കുള്ള പാരാമീറ്റർ മാപ്പിംഗ്

| Chat Completions (o-ശ്രേണി) | Responses API | കുറിപ്പുകൾ |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | ഉയർന്നതായി (4096+) സജീകരിക്കുക — ചിന്തന ടോക്കണുകൾ പരിധിയോടൊപ്പം എണ്ണപ്പെടുന്നു |
| `reasoning_effort` | `reasoning.effort` | ഉണ്ടെങ്കിൽ അതുപോലെ വയ്ക്കുക (കുറഞ്ഞ/ഇടത്തരം/ഉയരം) |
| `temperature` | ഒഴിവാക്കുക അല്ലെങ്കിൽ `1` ആയി സജീകരിക്കുക | O-സീരീസ് ൽ മാത്രം `1` സ്വീകരിക്കുന്നു |
| `top_p` | ഒഴിവാക്കുക | O-സീരീസിൽ പിന്തുണയില്ല |
| `seed` | ഒഴിവാക്കുക | Responses API ൽ പിന്തുണയില്ല |

### O-സീരീസ് മുമ്പ്/പിന്നീട്

മുമ്പ് (o-സീരീസുമായി ചേർത്ത് പൂരിപ്പിക്കൽ):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

പിന്നീട് (Responses API):
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

> **കുറിപ്പ്**: ഓ-സീരീസ് മോഡലുകൾ നിർദ്ദേശം നടത്തുമ്പോൾ ടെക്‌സ്‌റ്റ് ഡെൽറ്റ വിഹിതീകരിക്കുന്നതിന് മുമ്പ് ഉത്പാദനം ബഫർ ചെയ്യാം. സ്റ്റ്രീമിംഗ്‌ പ്രവർത്തിക്കുന്നു, പക്ഷേ ആദ്യത്തെ `response.output_text.delta` ഇവന്റ് GPT മോഡലുകളേക്കാൾ ദീർഘമായി വൈകി എത്താം.

## ചിന്തന ടോക്കണുകളിലേക്ക് ആക്‌സസ്
```python
# വിശകലന മോഡലുകൾ അഭ്യന്തര വിശകലനം ഉപയോഗിക്കുന്നു — എത്ര വിശകലന ടോക്കണുകൾ ഉപയോഗിച്ചു എന്ന് നിങ്ങൾക്ക് കാണാം
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

> **പ്രധാനமானത്**: ചിന്തന മോഡലുകളുടെ ആന്തരിക ചിന്തന പ്രക്രിയയെ കണക്കിലെടുത്ത് `max_output_tokens=1000` (50–200 അല്ല) ഉപയോഗിക്കുക. മോഡൽ അന്തർഗതമായി ചിന്തന ടോക്കണുകൾ ഉപയോഗിച്ച് അന്തിമ ഔട്ട്‌പുട്ട് സൃഷ്ടിക്കുന്നു.

## ഘടനയിട്ട ഔട്ട്‌പുട്ട് — JSON Schema
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

## ടൂൾ ഉപയോഗം

- `tools` ൽ ഫങ്ക്ഷനുകൾ ഡിഫൈൻ ചെയ്യുക **flat Responses API ഫോർമാറ്റിൽ** — `name`, `description`, `parameters` ടോപ്പ് ലെവലിൽ ( `function` ഉള്ളിൽ അടങ്ങിയിട്ടില്ല).
- മോഡൽ ടൂൾ വിളിക്കാൻ ആവശ്യപ്പെടുമ്പോൾ, നിങ്ങളുടെ ആപ്പിൽ ടൂൾ എക്സിക്യൂട്ട് ചെയ്ത് `input` ൽ `function_call_output` ഇനം ആയി ടൂൾ ഫലം അടുത്ത റിക്വസ്റ്റിൽ ഉൾപ്പെടുത്തുക.
- സ്കീമകളെ മിനിമയിൽ ഇട്ടു; എക്സിക്യൂഷനിന് മുമ്പ് ഇൻപുട്ടുകൾ സാധുത പരിശോധിക്കുക.
- `strict: true` ഉപയോഗിക്കുമ്പോൾ, എല്ലാ പ്രോപ്പർട്ടികളും `required` ല്‍ പട്ടികപ്പെടുത്തിയിരിക്കണം, കൂടാതെ `additionalProperties: false` നിർബന്ധമാണ്.

> **⚠️ `pydantic_function_tool()` പൊരുത്തക്കേടല്ല**: `openai.pydantic_function_tool()` ഹെൽപ്പർ പഴയ Chat Completions nested ഫോർമാറ്റ് (`{"type": "function", "function": {"name": ...}}`) ഉണ്ടാക്കുന്നു. അതു `responses.create()` ഉപയോഗിക്കരുത്. ടൂൾ സ്കീമകൾ കൈമാറ manually നിർവ്വചിക്കുക അല്ലെങ്കിൽ ഔട്ട്‌പുട്ട് flatten ചെയ്യുന്ന റാപ്പർ എഴുതുക.

### ടൂൾ നിർവ്വചന ഫോർമാറ്റ്

Responses API ഒരു **flat** ടൂൾ ഫോർമാറ്റ് ഓർക്കുന്നു — `name`, `description`, `parameters` ടോപ്പ് ലെവൽ കീകൾ ( `function` ഉള്ളിൽ അടങ്ങിയിട്ടില്ല).

**മുൻപ് (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**പിന്നീട് (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

പൂർണ്ണ ഉദാഹരണം:
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

`strict: true` (സ്കീമ എൻഫോഴ്സ്മെന്റ്) ഉപയോഗിച്ച്:
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
            "required": ["city_name"],       # എല്ലാ പ്രോപർട്ടികളും പട്ടികപ്പെടുത്തണം
            "additionalProperties": False,   # കർശന മോദിനായി ആവശ്യമാണ്
        },
    }
]
```

### ടൂൾ കോളിന്റെ റൗണ്ട്-ടിപ്പ് (എക്സിക്യൂട്ട് ചെയ്ത് ഫലമടക്കം തിരിച്ചയക്കുക)

മോഡൽ ടൂൾ കോളിന്റെ അഭ്യർത്ഥന അറിയുമ്പോൾ, Chat Completions `role: assistant` + `role: tool` പാറ്റേൺ **വരാതെ** `response.output` ഇനങ്ങളും `function_call_output` ഉപയോഗിക്കുക.

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
    # മോഡലിന്റെ function_call ഇനങ്ങൾ സംഭാഷണത്തിലേക്ക് ചേർക്കുക
    messages.extend(response.output)

    # ഓരോ ടൂളിനെയും പ്രവർത്തിപ്പിച്ച് ഫലങ്ങൾ ചേർക്കുക
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # ടൂൾ ഫലങ്ങളോടെ അന്തിമ മറുപടി നേടുക
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Few-shot ടൂൾ കോളിന്റെ ഉദാഹരണങ്ങൾ

`input` ൽ കുറച്ച് ഉദാഹരണങ്ങൾ നൽകുമ്പോൾ `function_call` and `function_call_output` ഇനങ്ങൾ ഉപയോഗിക്കുക. ഐഡികൾ `fc_` കൊണ്ട് തുടങ്ങണം.

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
# ഇൻബിൽറ്റ് വെബ് സേർച്ചിന്റെ ഉദാഹരണം
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## ഇമേജ് ഇൻപുട്ട്

ഇമേജ് ഉള്ളടക്കം ഇനങ്ങൾ `image_url` മുതൽ `input_image` ആയി മാറുന്നു, URL ഒരു nested object നിന്ന് flat string ആയി മാറുന്നു.

### ഇമേജ് ഇൻപുട്ട് — മുമ്പ് (Chat Completions)
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

### ഇമേജ് ഇൻപുട്ട് — ശേഷം (Responses API, URL)
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

### ഇമേജ് ഇൻപുട്ട് — പിന്നീട് (Responses API, base64)
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

> **പ്രധാന മാറ്റങ്ങൾ**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (nested	object) → `"image_url": "..."` (flat string — HTTPS URL അല്ലെങ്കിൽ `data:image/...;base64,...` ഡേറ്റാ URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft ഏജന്റ് ഫ്രെയിംവർക്ക് (MAF) മൈഗ്രേഷൻ

**മുതൽ നീങ്ങുന്നതിന് നിങ്ങളുടെ MAF വേഴ്ഷൻ പരിശോധിക്കുക** — മൈഗ്രേഷൻ MAF 1.0.0+ ആണോ അതോ പ്രീ-1.0.0 ബീറ്റ/ആർസി ആണോ എന്നതിനെ ആശ്രയിച്ചിരിക്കുന്നു.

പരിശോധിക്കാൻ: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ ൽ, `OpenAIChatClient` **ഇപ്പൊഴേ Responses API ഉപയോഗിക്കുന്നു** — മൈഗ്രേഷൻ ആവശ്യമില്ല.

ലെഗസി `OpenAIChatCompletionClient` ( `chat.completions.create` ഉപയോഗിക്കുന്നു) ഉപയോഗിക്കുന്ന കോഡ്ബേസ് ഉണ്ടെങ്കിൽ, അത് `OpenAIChatClient` കൊണ്ട് മാറ്റുക:

മുമ്പ്:
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

ശേഷം:
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

### MAF പ്രീ-1.0.0 (ബീറ്റ/ആർസി റിലീസുകൾ)

പ്രീ-1.0.0 MAF ൽ `OpenAIChatClient` Chat Completions ഉപയോഗിച്ചിരുന്നു. `agent-framework-openai>=1.0.0` അപ്ഗ്രേഡ് ചെയ്യുക, ഇത് ഡിഫോൾട്ട് Responses API ഉപയോഗിക്കുന്നത് `OpenAIChatClient` ആണ്.

> **കുറിപ്പ്**: `Agent`, `MCPStreamableHTTPTool`, മറ്റ് MAF APIകൾ മാറ്റമില്ല — ക്ലയന്റ് ക്ലാസ് ഇറക്കുമതി മാറ്റവും ഇൻസ്റ്റാൻഷിയേഷനും മാത്രമാണ്.

## LangChain (`langchain-openai`) മൈഗ്രേഷൻ

`ChatOpenAI()` ൽ `use_responses_api=True` ചേർക്കുക. കൂടാതെ മെസേജ് ഉള്ളടക്കം `.content` ന്റേതിൽ നിന്ന് `.text` ആയി അപ്ഡേറ്റ് ചെയ്യുക.

മുമ്പ്:
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

# ... ഏജന്റ് വിളിപ്പ് ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

ശേഷം:
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

# ... ഏജന്റ് വിളിക്കല്‍ ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **പ്രധാന മാറ്റങ്ങൾ**: (1) കൺസ്ട്രക്റ്ററിൽ `use_responses_api=True`, (2) പ്രതികരണ പ്രസംഗങ്ങളിൽ `.content` → `.text`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->