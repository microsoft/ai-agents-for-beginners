# Responses API ചീറ്റ് ഷീറ്റ് (Python + Azure OpenAI)

> താഴെ എല്ലാ സ്നിപ്പറ്റുകളും `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` എന്നത് അനുമാനിച്ചാണ് പ്രവർത്തിക്കുന്നത്, കൂടാതെ `client` ഇതിനകം ഇൻഷ്യലൈസ് ചെയ്തിട്ടുണ്ട് (ക്ലയന്റ് സെറ്റപ്പ് കാണുക).

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

## അസിങ്ക് ക്ലയന്റ് സെറ്റപ്പ് — വ്യക്തമായ ടെന്നന്റ് റെഫറൻസ് നൽകിയുള്ള EntraID (മൾട്ടി-ടെന്നന്റ്)

Azure OpenAI റിസോഴ്‌സ് **വിവത്യസ്ത ടെന്നന്റിൽ** ആയിരിക്കുമ്പോൾ, ക്രെഡൻഷ്യലിൽ `tenant_id` വ്യക്തമായി നൽകുക. ഡെവലപ്പറുടെ ഹോം ടെന്നന്റ് റിസോഴ്‌സ് ടെന്നന്റിൽ നിന്നുള്ള വ്യത്യാസം ഉണ്ടായിരിക്കുന്ന വികസന/ടെസ്റ്റ് സാഹചര്യങ്ങളിൽ ഇത് സാധാരണമാണ്.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# പ്രൊഡക്ഷന് വേണ്ടി ManagedIdentityCredential (ആസ്യൂർ കണ്ടെയ്‌നർ ആപ്പുകൾ, ആപ്പി സര്‍വീസ്, തുടങ്ങിയവ)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # ഉപയോക്തൃ-നിമിത്തം മാനേജിംഗ് ഐഡന്റിറ്റി
)
# ലൊക്കൽ ഡെവലപ്പ്മെന്റ് വേണ്ടി AzureDeveloperCliCredential — വ്യക്തമായ tenant_id അത്യന്താപേക്ഷിതമാണ്
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# ചെയിൻ: ആദ്യം മാനേജിംഗ് ഐഡന്റിറ്റി പരീക്ഷിക്കുക, അതെല്ലാതെ azd CLI-ക്കായി fallback ചെയ്യുക
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## അസിങ്ക് ക്ലയന്റ് മൈഗ്രേഷൻ — മുമ്പും/പിന്നിലും

മുമ്പ് (ഡിപ്രിക്കേറ്റഡ്):
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

## പൂർണ്ണ സിങ്ക് മൈഗ്രേഷൻ — മുമ്പും/പിന്നിലും

മുമ്പ് (പാരമ്പര്യമുള്ളത് — Azure OpenAI ചാറ്റ് പൂർത്തീകരണങ്ങൾ):
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

ശേഷം (Responses API — Azure OpenAI v1 എണ്ഡ്പോയിന്റ്):
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
        print()  # അവസാനത്തിൽ പുതിയ വരി
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

## വെബ് ആപ്പ് സ്ട്രീമിംഗ് — ബാക്ക്എൻഡ്-ടു-ഫ്രണ്ട്‌എൻഡ് രൂപം

SSE/JSONL സ്ട്രീമിംഗ് ചെയ്യുന്ന വെബ് ആപ്പ് antaŭാരണടിപ്പിച്ചു ശേഷം, **ബാക്ക്‌എൻഡ് സീരിയലൈസേഷൻ ഫോർമാറ്റ്** മാറുന്നു. ബാക്ക്‌എൻഡ് ഔട്ട്പുട്ട് ഡിസൈൻ ചെയ്യുക മുൻനിര ഫ്രണ്ട്‌എൻഡിന്റെ നിലവിലുള്ള ആക്സസ് പാറ്റേണുകൾ സംരക്ഷിക്കുന്ന രീതിയിൽ, ആകെ ഫ്രണ്ട്‌എൻഡിൽ മാറ്റങ്ങൾ ആവശ്യമില്ലാത്തത് ഉറപ്പാക്കാൻ.

**മുമ്പ്** — ചാറ്റ് പൂർത്തീകരണങ്ങൾ ബാക്ക്‌എൻഡ് സാധാരണയായി ഓരോ ചങ്കിന്റെ `choices[0]` ഡിക്ഷണറിയെ സീരിയലൈസ് ചെയ്തു:
```python
# പഴയത്: ഓരോ ചങ്കിനും സീരിയലൈസ്ഡ് ഫുൾ ചോയ്സ് ഡിക്ഷണറി
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend വായിക്കുക: `response.delta.content` (ഓബ്‌ജെക്ടിന് ആഴത്തിൽ).

**ശേഷം** — Responses API ബാക്ക്‌എൻഡ് ഏറ്റവും കുറഞ്ഞ രൂപം പുറപ്പെടുവിക്കുന്നു ഫ്രണ്ട്‌എൻഡിന്റെ ആക്സസ് പാത്ത് സംരക്ഷിക്കുന്ന ഒരേ രൂപം:
```python
# പുതിയത്: മുന്നൊരുക്കം ആവശ്യമായതിനെ മാത്രമേ പുറപ്പെടുവിക്കൂ
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend ഇപ്പോഴും വായിക്കുന്നു `response.delta.content` — **ഫ്രണ്ട്‌എൻഡിന്റെ മാറ്റങ്ങൾ ആവശ്യമില്ല**.

> **പ്രധാന洞**: Responses API സ്ട്രീമിംഗ് രൂപം (`event.type` + `event.delta`) ചാറ്റ് പൂർത്തീകരണങ്ങളുമായി (`chunk.choices[0].delta.content`) അടിസ്ഥാനപരമായി വ്യത്യസ്തമാണ്. എന്നാൽ, നിങ്ങളുടെ ബാക്ക്‌എൻഡ്-ടു-ഫ്രണ്ട്‌എൻഡ് കരാർ നിങ്ങളുടെ തയാറാക്കലാണ്. ബാക്ക്‌എൻഡ് ഔട്ട്‌പുട്ട് രൂപമാക്കുക ഫ്രണ്ട്‌എൻഡ് പ്രതീക്ഷിക്കുന്ന രീതിയിലേക്ക്.

## സ്ട്രീമിംഗ് ഇവന്റ് പരമ്പര

`stream: true` ആയിരിക്കുമ്പോൾ, API ഈ ഓർഡറിൽ ഇവന്റുകൾ പുറപ്പെടുവിക്കുന്നു:
1. `response.created` – പ്രതികരണ ഓബ്‌ജെക്ട് ആരംഭിച്ചു
2. `response.in_progress` – ഉൽപാദനം ആരംഭിച്ചു
3. `response.output_item.added` – ഔട്ട്പുട്ട് ഇനം സൃഷ്ടിച്ചു
4. `response.content_part.added` – ഉള്ളടക്ക ഭാഗം ആരംഭിച്ചു
5. `response.output_text.delta` – ടെക്സ്റ്റ് ചങ്കുകൾ (പലത്, ഓരോന്നിലും `delta: string` ഉണ്ട്)
6. `response.output_text.done` – ടെക്സ്റ്റ് ജനനമു് പൂർത്തിയായി
7. `response.content_part.done` – ഉള്ളടക്ക ഭാഗം പൂർത്തിയായി
8. `response.output_item.done` – ഔട്ട്പുട്ട് ഇനം പൂർത്തിയായി
9. `response.completed` – മുഴുവൻ പ്രതികരണവും പൂർത്തിയായി

അടിസ്ഥാന ടെക്സ്റ്റ് സ്ട്രീമിംഗിനു്, `response.output_text.delta` (ടെക്സ്റ്റ് ചങ്കുകൾക്കായി) ഉം `response.completed` (അവസാനത്തിനായി) മാത്രമേ കൈകാര്യം ചെയ്യേണ്ടതുള്ളൂ.

## വെബ് ആപ്പുകളിൽ സ്ട്രീമിംഗ് പിശക് കൈതുടക്കം

വെബ് ആപ്പിൽ സ്ട്രീമിംഗ് ചെയ്യുമ്പോൾ, അസിങ്ക് റിപീട്ടറേഷൻ `try/except` ൽ മൂടി, പിശകുകൾ JSON ആയി ഉളവാക്കി ഫറണ്ട്‌എൻഡിന് സുന്ദരമായി കാണിക്കാൻ അനുവദിക്കുക (ഉദാ: നിരക്ക് പരിധികൾ, താൽക്കാലിക പരാജയങ്ങൾ):

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


> **ഇതിന്റെ പ്രാധാന്യം**: Azure OpenAI റേറ്റ് ലിമിറ്റിങ്ങിനിടയിൽ `429 Too Many Requests` തിരികെ നൽകുന്നു. `try/except` ഇല്ലാതെ, സ്ട്രീമിംഗ് പ്രതികരണം ഒളിഞ്ഞുപോകും. അതോടൊപ്പം, ഫ്രണ്ട്‌എൻഡ് `{"error": "Too Many Requests"}` ലഭിച്ച് വീണ്ടും ശ്രമിക്കാൻ പ്രോംപ്റ്റ് കാണിക്കാമാകും.

## സ്ട്രീമിംഗ് ഇവന്റ് തരം (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## സംഭാഷണ ഫോർമാറ്റ്
```python
# റെസ്പോൺസസ് API ഇൻപുട്ട് അറേ വഴി സംഭാഷണ ഫോർമാറ്റ് പിന്തുണയ്ക്കുന്നു
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

## കണ്ടന്റ് ഫിൽറ്റർ പിഴവു കൈമാറ്റം

പിഴവ് ബോഡി ഘടന Chat Completions-ൽ നിന്ന് Responses API-ലേക്ക് മാറിയിട്ടുണ്ട്.

മുൻപ് (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ശേഷിച്ചു (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

പ്രധാന വ്യത്യാസങ്ങൾ:
- `innererror` റാപ്പർ **മറ്റുമില്ല** — കണ്ടന്റ് ഫിൽട്ടർ വിശദാംശങ്ങൾ ഇപ്പോൾ `error.body`-ന്റെ മുകളിലത്തെ നിരയിൽ.
- `content_filter_result` (എകതലം) → `content_filters` (ബഹുവചന ശൃംഖല) ഓഫ each entry ഉള്ളിൽ `content_filter_results` (ബഹുവചന) ഉൾക്കൊള്ളുന്നു.
- `content_filters`-ൽ ഓരോ എന്റ്രിയിലും `blocked`, `source_type`, `content_filter_results` ഉണ്ട്, ഓരോ വിഭാഗത്തിന്റെയും വിശദാംശങ്ങളോടുകൂടെ (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Responses API പൂർണ്ണ കണ്ടന്റ് ഫിൽട്ടർ പിഴവു ബോഡി ഘടന:
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

## റോ HTTP മൈഗ്രേഷൻ (requests/httpx)

ആപ്പ് SDK ഉപയോഗിക്കുന്നതിന് പകരം Azure OpenAI REST നേരിട്ട് വിളിക്കുന്നുവെങ്കിൽ:

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

ശേഷിച്ചു (Responses API):
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

> **ഗുരുതര കുറിപ്പ്**: Python SDK-യിലെ `Response` ഒബ്ജക്റ്റിലെ `output_text` ഒരു സൗകര്യപ്രദമായ പ്രോപ്പർട്ടി ആണ്. റോ REST JSON പ്രതികരണത്തിന് മുകളിലത്തെ `output_text` ഫീൽഡ് ഇല്ല — ടെക്സ്റ്റ് `output[0].content[0].text`-ൽ കാണാം.

## ബഹു-ടേൺ സംഭാഷണം
```python
# Responses API ഉപയോഗിച്ച് ഒരു സംവാദം നിർമ്മിക്കുക
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# സഹായി പ്രതികരണം സംവാദത്തിലേക്ക് ചേർക്കുക
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

കണ്ടന്റ്-ടൈപ്പ്ഡ് ബഹു-ടേൺ (സ്പഷ്ടമായ `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` ഉപയോഗിച്ച് ബഹു-ടേൺ (വൈകല്യം)

സംഭാഷണ ലിസ്റ്റ് നന്നായി നിയന്ത്രിക്കുന്നതിന് പകരം, റിസ്പോൺസുകൾ സേർവർ-സൈഡിൽ `previous_response_id` ഉപയോഗിച്ച് ബന്ധിപ്പിക്കാൻ കഴിയും.
API ഓരോ പ്രതികരണവും സൂക്ഷിക്കുകയും മുൻ ടേൺസ് സ്വയം ചേർക്കുകയും ചെയ്യുന്നു.


```python
# ആദ്യമായി തിരിയുക
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# തുടര്‍ന്ന് തിരിയായാല്‍ — പുതിയ ഉപയോക്തൃ സന്ദേശവും മുന്‍ പ്രതികരണ ഐഡിയയും മാത്രം പാസ്സ് ചെയ്യുക
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**വെറുതെ ഉപയോഗിക്കേണ്ടത്:**

| സമീപനം | ഗുണങ്ങൾ | ദോഷങ്ങൾ |
|---|---|---|
| `input` അറേ (മാനുവൽ) | ചരിത്രത്തെ പൂർണ നിയന്ത്രണം; ക്രമസമയിപ്പിക്കൽ/ചുരുക്കൽ കഴിയും; സേർവർ-സൈഡ് സംഭരണം ആവശ്യമില്ല (`store=False`) | കൂടുതൽ കോഡ്; നിങ്ങൾ അറേ കൈകാര്യം ചെയ്യണം |
| `previous_response_id` | എളുപ്പമുള്ള കോഡ്; സ്വയം ബന്ധിപ്പിക്കൽ | `store=True` (ഡിഫോൾട്ട്) ആവശ്യം; സംഭാഷണം സേർവർ-സൈഡിൽ സൂക്ഷിച്ചിരിക്കുന്നു; ടേണുകൾ നുഴഞ്ഞുനോക്കാൻ അനുമതി ഇല്ല |

> **മൈഗ്രേഷൻ കുറിപ്പ്:** കൂടുതൽ Chat Completions ആപ്ലിക്കേഷനുകൾ ഇതിനകം തന്നെ അവരുടെ മെസേജ് അറേ മാനേജു ചെയ്യുന്നു, അതിനാൽ `input` അറേയിലേക്ക് മാറ്റുന്നത് സാരമായി 1:1 മൈഗ്രേഷൻ ആണ്. പുതിയ കോഡിന് അല്ലെങ്കിൽ സംഭാഷണ ചരിത്രം നിയന്ത്രിക്കേണ്ടതില്ലെങ്കിൽ `previous_response_id` ഉപയോഗിക്കുക.

## O-സീരീസ് റീസ്‌നിങ്ങ് മോഡലുകൾ (o1, o3-mini, o3, o4-mini)

O-സീരീസ് മോഡലുകൾ Responses API-യിലേക്ക് മൈഗ്രേറ്റ് ചെയ്യുമ്പോൾ പ്രത്യേക പാരാമീറ്റർ നിയന്ത്രണങ്ങൾ ഉണ്ട്.

### O-സീരീസ് പാരാമീറ്റർ మ్యാപിംഗ്

| Chat Completions (o-സീരീസ്) | Responses API | കുറിപ്പുകൾ |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | ഉയർന്ന നിരക്കില്‍ (4096+) സജ്ജമാക്കുക — വ്യാഖ്യാന ടോകണ്‍‌കള്‍ സ лимിഗ്‌റിന് നല്‍കുന്നു |
| `reasoning_effort` | `reasoning.effort` | ഉണ്ടെങ്കില്‍ 그대로 വെക്കുക (കുറഞ്ഞത്/മധ്യം/ഉയര്‍ന്നത്) |
| `temperature` | നീക്കം ചെയ്യുക അല്ലെങ്കില്‍ `1` ആക്കുക | ഒ-സീരിസ് വെറും `1` സ്വീകരിക്കുന്നു |
| `top_p` | നീക്കം ചെയ്യുക | ഒ-സീരിസില്‍ പിന്തുണയില്ല |
| `seed` | നീക്കം ചെയ്യുക | Responses API ൽ പിന്തുണയില്ല |

### ഒ-സീരിസ് മുന്‍പ്/പിന്നീട്

മുന്‍പ് (ഒ-സീരിസുമായി ചാറ്റ് പൂരിപ്പുകള്‍):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

ശേഷം (Responses API):
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

> **കുറിപ്പ്**: ഒ-സീരിസ് മാതൃകകള്‍ വ്യാഖ്യാനത്തിനിടയില്‍ ഔട്ട്പുട്ട് ബഫര്‍ ചെയ്യാം, പിന്നീട് ടെക്സ്റ്റ് ഡെല്‍റ്റകള്‍ പ്രസിദ്ധീകരിക്കും. സ്ട്രീമിംഗ് ഇപ്പോഴും പ്രവര്‍ത്തിക്കുന്നു, പക്ഷേ ആദ്യത്തെ `response.output_text.delta` ഇവന്റ് GPT മാതൃകകളെക്കാള്‍ ദീര്‍ഘ വൈകിയെത്താം.

## reasoning ടോകണ്‍സിലേക്ക് ആക്സസ്
```python
# വിവേക മാതൃകകൾ ആഭ്യന്തര വിവേകം ഉപയോഗിക്കുന്നു — എത്ര വിവേക ടോക്കണുകൾ ഉപയോഗിച്ചതെന്ന് നിങ്ങൾക്ക് കാണാം
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

> **പ്രധാനാംഗ്**: reasoning മാതൃകകളുടെ ആഭ്യന്തര reasoning പ്രക്രിയ കണക്കിലെടുക്കാന്‍ `max_output_tokens=1000` (50–200 അല്ല) ഉപയോഗിക്കുക. മാതൃക അവസാന ഔട്ട്പുട്ട് സൃഷ്ടിക്കുന്നതിന് മുമ്പ് reasoning ടോകണ്‍സിന്റെ വരിച്ചുപയോഗിക്കുന്നു.

## ഘടനയുള്ള ഔട്ട്പുട്ട് — JSON സ്കീമ
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

## ടൂള്‍ ഉപയോഗം

- `tools`-ലും ഫ്ലാറ്റ് Responses API ഫോർമാറ്റിൽ — `name`, `description`, `parameters` മുകളിലെ ലെവലിൽ നിര്‍വചിക്കുക (function-ന്റെ അടിയില്‍ അല്ല).
- മാതൃക ടൂള്‍ വിളിക്കണമെന്ന് ആവശ്യപ്പെടുമ്പോൾ, നിങ്ങളുടെ ആപ്പിൽ അത് നടത്തി ടൂള്‍ ഫലം അടുത്ത അഭ്യര്‍ത്ഥനയിലേക്ക് `function_call_output` ഇനമായി `input`-ല്‍ ഉള്‍പ്പെടുത്തുക.
- സ്കീമകൾ ലഘുക്കരിക്കുക; സാധനങ്ങള്‍ ചെയ്യുന്നതിന് മുമ്പ് ഇന്‍പുട്ടുകള്‍ ശരിയാണെന്ന് പരിശോദിക്കുക.
- `strict: true` ഉപയോഗിക്കുമ്പോൾ എല്ലാ പ്രോപ്പർട്ടികളും `required`-ലും ഉൾപ്പെടുത്തണം, കൂടാതെ `additionalProperties: false` നിർബന്ധമാണ്.

> **⚠️ `pydantic_function_tool()` പൊരുത്തപ്പെടുന്നില്ല**: പഴയ Chat Completions നെസ്റ്റഡ് ഫോർമാറ്റ് (`{"type": "function", "function": {"name": ...}}`) ഇപ്പോഴും `openai.pydantic_function_tool()` സഹായിക്കുന്നുണ്ടെങ്കിലും `responses.create()`-നൊപ്പം ഉപയോഗിക്കരുത്. ടൂളുകൾ മാനുവലായി നിർവചിക്കുക അല്ലെങ്കിൽ ഔട്ട്പുട്ട് ഫ്ലാറ്റ് ആക്കാൻ ഒരു റാപ്പർ എഴുതുക.

### ടൂൾ നിർവചന ഫോർമാറ്റ്

Responses API ഫ്ലാറ്റ് ടൂൾ ഫോർമാറ്റ് ഉപയോഗിക്കുന്നു — `name`, `description`, `parameters` മുകളിലെ കീകൾ ആണു (function-ന്റെ അടിക്കല്ല).

**മുൻപ് (Chat Completions — നെസ്റ്റ് ചെയ്തിരിക്കുന്നത്):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**ശേഷം (Responses API — ഫ്ലാറ്റ്):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

പൂര്‍ണ്ണ ഉദാഹരണം:
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

`strict: true` (സ്കീമ നിർവഹണം) ഉപയോഗിച്ച്:
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
            "required": ["city_name"],       # എല്ലാ പ്രോപ്പർടീസും ആവശ്യമാണ് പട്ടികപ്പെടുത്തുന്നത്
            "additionalProperties": False,   # കഠിന മോട്ടം (strict mode) നായി ആവശ്യമാണ്
        },
    }
]
```

### ടൂൾ വിളി റൗണ്ട്-ട്രിപ്പ് (നിലവില്‍ പ്രവര്‍ത്തിപ്പിച്ച് ഫലം മടക്കയച്ചു)

മാതൃക ടൂൾ വിളിക്കണമെന്ന് ആവശ്യപ്പെടുമ്പോൾ, `response.output` ഇനങ്ങളെയും `function_call_output`-ഉം ഉപയോഗിക്കുക — **chat completions**-ന്റെ `role: assistant` + `role: tool` മാതൃകയല്ല.

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
    # മോഡലിന്റെ function_call ഇനങ്ങൾ സംഭാഷണത്തിൽ ചേർക്കുക
    messages.extend(response.output)

    # ഓരോ ടൂളും നടപ്പാക്കുക ഫലങ്ങൾ ചേർക്കുക
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # ടൂൾ ഫലങ്ങളുമായി അവസാന പ്രതികരണം ലഭിക്കുക
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### കുറച്ച്-ശോട്ട് ടൂൾ വിളി ഉദാഹരണങ്ങൾ

`input`-ല്‍ കുറച്ച്-ശോട്ട് ടൂൾ വിളികളുടെ ഉദാഹരണങ്ങൾ കൊടുക്കുമ്പോൾ, `function_call`യും `function_call_output` ഇനങ്ങളും ഉപയോഗിക്കുക. ഐ.ഡി `fc_`-നാലാണ് ആരംഭിക്കേണ്ടത്.

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
# ബിൽറ്റ്-ഇൻ വെബ് സെർച്ച് ഉദാഹരണം
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## ചിത്ര ഇൻപുട്ട്

ചിത്ര മുന്പെയും இனിയും വേർതിരിക്കുന്നു: `image_url`-ൽനിന്നും `"input_image"` ആയി മാറ്റാനും URL-നെ നസ്റ്റഡ് объъക്റ്റിൽനിന്ന് ഫ്ലാറ്റ് സ്റ്റ്രിങ്ങിലേക്ക് മാറ്റാനും.

### ചിത്ര ഇൻപുട്ട് — മുൻപ് (Chat Completions)
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

### ചിത്ര ഇൻപുട്ട് — ശേഷം (Responses API, URL)
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

### ചിത്ര ഇൻപുട്ട് — ശേഷം (Responses API, base64)
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

> **പ്രധാന മാറ്റങ്ങൾ**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (നസ്റ്റഡ് объъക്റ്റ്) → `"image_url": "..."` (ഫ്ലാറ്റ് സ്ട്രിംഗ് — HTTPS URL അല്ലെങ്കിൽ `data:image/...;base64,...` ഡാറ്റാ URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) മൈഗ്രേഷൻ

**നിങ്ങളുടെ MAF പതിപ്പ് ആദ്യം പരിശോധിക്കുക** — മൈഗ്രേഷൻ MAF 1.0.0+ ആണോ അതല്ലയോ എന്നതിൽ ആശ്രയിക്കുന്നു.

പരിശോധിക്കാന്‍: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ യില്‍, `OpenAIChatClient` **ഇപ്പോഴAlready Responses API ഉപയോഗിക്കുന്നു** — മൈഗ്രേഷൻ ആവശ്യമില്ല.

കോഡ് ബേസ് പഴയ `OpenAIChatCompletionClient` (ഇത് `chat.completions.create` ഉപയോഗിക്കുന്നു) ഉപയോഗിക്കുന്നുണ്ടെങ്കിൽ, അത് `OpenAIChatClient`-അായി മാറ്റുക:

മുന്‍പ്:
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

### MAF 1.0.0-മുന്‍പ് (ബീറ്റ/ആർ.സി. റിലീസുകൾ)

MAF 1.0.0-മുന്‍പ് `OpenAIChatClient` Chat Completions ഉപയോഗിച്ചിരുന്നു. `agent-framework-openai>=1.0.0`-ലേക്ക് അപ്ഗ്രേഡ് ചെയ്യുക, അതിൽ `OpenAIChatClient` Responses API സ്വാഭാവികമായി ഉപയോഗിക്കുന്നു.

> **കുറിപ്പ്**: `Agent`, `MCPStreamableHTTPTool`, മറ്റു MAF APIകൾ മാറ്റമില്ല — വെറും ക്ലയന്റ് ക്ലാസ് ഇംപോർട്ട് സൃഷ്ടിയും മാറുന്നു.

## LangChain (`langchain-openai`) മൈഗ്രേഷൻ

`ChatOpenAI()`-യിലേക്ക് `use_responses_api=True` ചേർക്കുക. സാന്റകസ് മെസേജ് കോൺടന്റ് `.content`-ലിൽ നിന്നു `.text` ആക്കുക.

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

# ... ഏജന്റ് കോളിംഗ് ...
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

# ... ഏജന്റ് ക്ഷണിക്കല്‍ ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **പ്രധാന മാറ്റങ്ങൾ**: (1) കൺസ്ട്രക്ടറിൽ `use_responses_api=True`, (2) `.content` → `.text` മറുപടിയിലെ സന്ദേശങ്ങളിൽ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->