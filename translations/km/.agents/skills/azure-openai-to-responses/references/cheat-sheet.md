# ព័ត៌មានជំនួយ Responses API (Python + Azure OpenAI)

> ទិន្នន័យគំរូទាំងអស់ខាងក្រោមសន្មត់ថា `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ហើយ `client` ត្រូវបាន initialized រួចហើយ (មើលការតំឡើង client)។

## សំណើមូលដ្ធាន
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## ការតំឡើង client — EntraID (ដែលបានណែនាំ)
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

## ការតំឡើង client — កូនសោ API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## ការតំឡើង client អស៊ីង — EntraID
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

## ការតំឡើង client អស៊ីង — EntraID ជាមួយ tenant ឯកះ (multi-tenant)

នៅពេលដែលធនធាន Azure OpenAI មាននៅក្នុង **tenant ខុសពី** ថ្មី, ប្រើ `tenant_id` ដោយច្បាស់ទៅកាន់ credential។ វាជារឿងធម្មតានៅក្នុងស្ថានការណ៍ dev/test ដែល tenant មុខផ្ទះអ្នកអភិវឌ្ឍខុសពី tenant ធនធាន។

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential សម្រាប់ផលិតកម្ម (កម្មវិធីកុងតឺន័រអាស៊ួរ, សេវាកម្មកម្មវិធី, ល។)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # អត្តសញ្ញាណគ្រប់គ្រងដែលបានផ្ដល់ដោយអ្នកប្រើ
)
# AzureDeveloperCliCredential សម្រាប់ការអភិវឌ្ឍជាផ្ទាល់ — tenant_id ពិចារណាជាក់លាក់គឺសំខាន់
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# ច្រង់: សាកល្បងអត្តសញ្ញាណគ្រប់គ្រងជាមុនសិន, បញ្ចេញទៅ azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## ការផ្លាស់ទី client អស៊ីង — មុន/ក្រោយ

មុន (មិនបានគាំទ្រ):
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

បន្ទាប់:
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

## ការផ្លាស់ទី sync ពេញលេញ — មុន/ក្រោយ

មុន (ចាស់— Azure OpenAI Chat Completions):
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

បន្ទាប់ (Responses API — Azure OpenAI v1 endpoint):
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

## ប្រព័ន្ធផ្សព្វផ្សាយ (sync)
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
        print()  # បន្ទាត់ថ្មីនៅចុងក្រោយ
```

## ប្រព័ន្ធផ្សព្វផ្សាយ (async)
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

## ប្រព័ន្ធផ្សព្វផ្សាយកម្មវិធីបណ្ដាញ — រូបរាងពីបណ្ដាញហេដ្ឋារចនាសម្ព័ន្ធទៅផ្ទាំងមុខ

ពេលផ្លាស់ប្តូរកម្មវិធីបណ្ដាញដែលផ្ទុក SSE/JSONL ទៅផ្ទាំងមុខ, រូបរាង **ការតម្រៀបបណ្ដាញផ្ទាល់ខ្លួន** ផ្លាស់ប្តូរ។ រចនាផលចេញថ្មីពីបណ្ដាញដើម្បីរក្សាចំនុចចូលដំណើរការដដែលជាមួយផ្ទាំងមុខ ដូច្នេះផ្ទាំងមុខមិនត្រូវការផ្លាស់ប្តូរទេ។

**មុន** — បណ្ដាញ Chat Completions ជាទូទៅតម្រៀប dict `choices[0]` នៃលំនួននីមួយៗ៖
```python
# ចាស់: បានបញ្ចូល dict ជម្រើសពេញលេញលម្អិតក្នុងមួយប្លុក
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend អាន៖ `response.delta.content` (ផ្លូវជ្រៅចូលទៅក្នុងវត្ថុជម្រើស)។

**បន្ទាប់** — Responses API បណ្ដាញបញ្ចេញរូបរាងតិចតួចរក្សារផ្លូវចូលដំណើរការដដែលទៅផ្ទាំងមុខ៖
```python
# ថ្មី: បញ្ចេញតែអ្វីដែលផ្នែកមុខត្រូវការតែប៉ុណ្ណោះ
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend នៅតែអាន `response.delta.content` — **មិនត្រូវការផ្លាស់ប្តូរផ្ទាំងមុខ**។

> **ចំណុចសំខាន់**: រូបរាងប្រព័ន្ធផ្សព្វផ្សាយ Responses API (`event.type` + `event.delta`) ខុសគ្នាដោយសំខាន់ពី Chat Completions (`chunk.choices[0].delta.content`)។ ប៉ុន្តែសន្ធិសញ្ញាផ្ទាល់ខ្លួនរវាងបណ្ដាញទៅផ្ទាំងមុខគឺជារបស់អ្នកសម្រាប់កំណត់។ រចនាបញ្ចេញពីបណ្ដាញឲ្យផ្គូផ្គងនឹងអ្វីដែលផ្ទាំងមុខរង់ចាំរួច។

## ជួរតួន事件ផ្សព្វផ្សាយ

នៅពេល `stream: true`, API បញ្ចេញការព្រឹត្តិការណ៍លំដាប់ដូចខាងក្រោម៖
1. `response.created` – វត្ថុចាប់ផ្តើមបង្កើតបាន
2. `response.in_progress` – ការបង្កើតបានចริ่ม
3. `response.output_item.added` – វត្ថុចេញបានបង្កើត
4. `response.content_part.added` – ផ្នែកមាតិកាបានចាប់ផ្តើម
5. `response.output_text.delta` – ខ្នាតអក្សរពហុ (ច្រើន, ធាតុទាំងអស់មាន `delta: string`)
6. `response.output_text.done` – ការបង្កើតអក្សរបញ្ចប់
7. `response.content_part.done` – ផ្នែកមាតិកាបញ្ចប់
8. `response.output_item.done` – វត្ថុចេញបញ្ចប់
9. `response.completed` – ការឆ្លើយតបពេញលេញបានបញ្ចប់

សម្រាប់ប្រព័ន្ធផ្សព្វផ្សាយអក្សរមូលដ្ឋាន គ្រាន់តែគ្រប់គ្រង `response.output_text.delta` (សម្រាប់ខ្នាតអក្សរ) និង `response.completed` (សម្រាប់បញ្ចប់)។

## ការគ្រប់គ្រងកំហុសប្រព័ន្ធផ្សព្វផ្សាយនៅក្នុងកម្មវិធីបណ្ដាញ

នៅពេលប្រព័ន្ធផ្សព្វផ្សាយនៅក្នុងកម្មវិធីបណ្ដាញ, កំណត់ async iteration ក្នុង `try/except` ហើយធ្វើបញ្ចេញកំហុសជា JSON ដូច្នេះផ្ទាំងមុខអាចបង្ហាញបានយ៉ាងអំណត់ (ឧ. កំណត់អត្រា, ការបរាជ័យបណ្តោះអាសន្ន):

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

> **ហេតុអ្វីបានជា វាមានសារៈសំខាន់**: Azure OpenAI បញ្ចេញ `429 Too Many Requests` ពេលកំណត់អត្រា។ បើគ្មាន `try/except`, ប្រតិកម្មបណ្ដាញនឹងបញ្ឈប់ដោយស្ងាត់។ ជាមួយវា, ផ្ទាំងមុខទទួលបាន `{"error": "Too Many Requests"}` ហើយអាចបង្ហាញការចូលសំណើម្តងទៀត។

## ប្រភេទព្រឹត្តិការណ៍ប្រព័ន្ធផ្សព្វផ្សាយ (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## ទ្រង់ទ្រាយសន្ទនា
```python
# API នៃការឆ្លើយតបគាំទ្រទ្រង់ទ្រាយការសន្ទនាតាមរយៈអារេអ៊ីនបញ្ចូល
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

## ការគ្រប់គ្រងកំហុសត្រង់តម្រងមាតិកា

រចនាសម្ព័ន្ធខ្លួនកំហុសផ្លាស់ប្ដូរពី Chat Completions ទៅ Responses API។

មុន (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

បន្ទាប់ (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ចំណុចខុសគ្នាសំខាន់ៗ៖
- ឧបករណ៍ `innererror` ត្រូវបាន **ដកចេញ** — ព័ត៌មានលម្អិតត្រង់តម្រងមាតិកានៅលើកម្រិតខ្លួនកំហុស `error.body`។
- `content_filter_result` (តែមួយ) → `content_filters` (ជាអារេពហុ) ដែលមាន `content_filter_results` (ពហុ) នៅក្នុងប្រភេទនីមួយៗ។
- លើក្រឡាចត្រង្គក្នុង `content_filters` រួមបញ្ចូល `blocked`, `source_type`, និង `content_filter_results` ជាមួយព័ត៌មានលម្អិតតាមប្រភេទ (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`)។

រចនាសម្ព័ន្ធខ្លួនកំហុសត្រង់តម្រងមាតិកា Responses API ពេញលេញ៖
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

## ការផ្លាស់ទី HTTP ស្ងាត់ (requests/httpx)

ប្រសិនបើកម្មវិធីហៅ Azure OpenAI REST ដោយផ្ទាល់ជំនួស SDK:

មុន (Chat Completions):
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

បន្ទាប់ (Responses API):
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

> **ចំណាំ**: `output_text` ជាលក្ខណៈងាយស្រួលលើវត្ថុ Python SDK របស់ `Response`។ ប្រតិកម្ម JSON REST ដើមគឺមិនមានវាល `output_text` នៅកម្រិតខ្លួន — អក្សរនៅក្នុង `output[0].content[0].text`។

## សន្ទនាប្រវត្តិជាច្រើនជំហាន
```python
# សាងសង់ការសន្ទនាជាមួយ Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# បន្ថែមចម្លើយរបស់ជំនួយការទៅកាន់ការសន្ទនា
messages.append({"role": "assistant", "content": response.output_text})

# បន្តការសន្ទនា
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

ថ្នាក់ខ្នាតមាតិកាច្រើនជំហាន (មាន `input_text`/`output_text` យ៉ាងច្បាស់):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### ជំហានច្រើនតាមរយៈ `previous_response_id` (ជម្រើសបន្ថែម)

ជំនួសនឹងគ្រប់គ្រងអារេសន្ទនាដោយខ្លួនឯង អ្នកអាចភ្ជាប់ចម្លើយ
ពីបណ្ដាញដោយប្រើ `previous_response_id`។ API រក្សាទុកចម្លើយនីមួយៗ ហើយ
មានការផ្ដល់មុនហត្ថដល់ជំហានមុនៗដោយស្វ័យប្រវត្តិ។

```python
# បង្វិលដំបូង
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# បង្វិលបន្ទាប់ — គ្រាន់តែផ្ញើសារអ្នកប្រើថ្មី + អត្តសញ្ញាណការឆ្លើយតបមុន
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**ពេលណាដើម្បីប្រើប្រភេទណា៖**

| វិធីសាស្រ្ត | ល្អ | ខ្សោយ |
|---|---|---|
| អារេ `input` (ដៃគូរ) | រក្សាការគ្រប់គ្រងប្រវត្តិពេញលេញ; អាចកាត់បន្ថយ/សង្ខេប; មិនចាំបាច់រក្សាទុកនៅបណ្ដាញ (`store=False`) | មានកូដច្រើន; អ្នកគ្រប់គ្រងអារេដោយផ្ទាល់ |
| `previous_response_id` | កូដសាមញ្ញ; ភ្ជាប់ដោយស្វ័យប្រវត្តិ | តម្រូវ `store=True` (លំនាំដើម); រក្សាទុកសន្ទនានៅបណ្ដាញ; មិនអាចកែប្រែប្រវត្តិរវាងជំហានបាន |

> **ចំណាំផ្លាស់ទី:** កម្មវិធី Chat Completions ភាគច្រើនបានគ្រប់គ្រងអារេសារ្យដោយខ្លួនឯងរួចហើយ, ដូច្នេះការបម្លែងទៅកាន់អារេ `input` គឺជាការផ្លាស់ទីតាមផ្លូវត្រង់មួយទៅមួយ។ ប្រើ `previous_response_id` សម្រាប់កូដថ្មី ឬពេលដែលអ្នកមិនចាំបាច់កែប្រែប្រវត្តិសន្ទនា។

## ម៉ូដែលចិត្តវិភាគ O-series (o1, o3-mini, o3, o4-mini)

ម៉ូដែល O-series មានការចំរាញ់លំដាប់ប៉ារ៉ាម៉ែត្រពិសេសពេលផ្លាស់ទៅ Responses API។

### ការផ្គូផ្គងប៉ារ៉ាម៉ែត្រសម្រាប់ o-series

| Chat Completions (o-series) | Responses API | សំគាល់ |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | កំណត់ខ្ពស់ (4096+) — បរិមាណទូរសារតំណល់គិតចំពោះដែនកំណត់ |
| `reasoning_effort` | `reasoning.effort` | ទុកដូចមាន ប្រសិនបើមាន (ទាប/មធ្យម/ខ្ពស់) |
| `temperature` | លុប ឬកំណត់ជាមូល `1` | O-series ទទួលយកតែ `1` ផ្ទាល់ |
| `top_p` | លុប | មិនគាំទ្រ​លើ o-series |
| `seed` | លុប | មិនគាំទ្រ​នៅក្នុង Responses API |

### O-series មុន/ក្រោយ

មុន (Chat Completions ជាមួយ o-series):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

ក្រោយ (Responses API):
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

> **សម្គាល់**: ម៉ូឌែល O-series អាចបង្កុកលទ្ធផលផ្សាយក្នុងដំណើរការជំនិត មុននឹងបញ្ចេញអក្សរបង្ហាញ។ ការផ្សាយបន្ត​ភ្លាមៗនៅតែដំណើរការ ប៉ុន្តែព្រឹត្តិការណ៍ `response.output_text.delta` ដំបូងអាចមកយឺតជាងម៉ូឌែល GPT ។

## ការចូលដំណើរការត្រូវលោកហ្មត់ចត់ (reasoning tokens)
```python
# ម៉ូដែលហេតុផលប្រើហេតុផលផ្ទៃក្នុង — អ្នកអាចមើលឃើញពីចំនួនសញ្ញាហេតុផលដែលបានប្រើ
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

> **សំខាន់**: ប្រើ `max_output_tokens=1000` (មិនមែន 50–200) ដើម្បីគិតគូរលទ្ធផលម៉ូឌែល reasoning លើកមុនក្នុងការ​បង្កើតលទ្ធផលចុងក្រោយ។

## លទ្ធផលលំអិត — JSON Schema
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

## ការប្រើឧបករណ៍

- កំណត់មុខងារជា `tools` ជាទម្រង់ Responses API ល្អមួយ — `name`, `description`, និង `parameters` នៅកម្រិតខ្ពស់ (មិនបានសម្រាប់នៅក្រោម `function`)។
- ពេលម៉ូឌែលស្នើហៅឧបករណ៍ ចាប់អនុវត្តនៅកម្មវិធីរបស់អ្នក ហើយបញ្ចូលលទ្ធផលឧបករណ៍ជាឥតទទួលខុសត្រូវ `function_call_output` ជាធាតុក្នុង `input`។
- រក្សាទុក schemas ឲ្យតិចតួច; ធ្វើការត្រួតពិនិត្យការបញ្ចូលមុនពេលអនុវត្ត។
- បើប្រើ `strict: true` គ្រប់គ្រងលក្ខណៈគ្រប់យ៉ាងត្រូវតែនៅក្នុង `required` ហើយ `additionalProperties: false` គឺបាច់បាច់។

> **⚠️ `pydantic_function_tool()` មិនសមស្រប**៖ ផ្នែកជំនួយ `openai.pydantic_function_tool()` នៅតែបង្កើតទម្រង់ nested ចាស់ Chat Completions (`{"type": "function", "function": {"name": ...}}`)។ មិនត្រូវប្រើជាមួយ `responses.create()` ទេ។ សូមកំណត់ schemas ឧបករណ៍ដោយដៃ ឬសរសេរលំដាប់បញ្ចូលដើម្បីធ្វើ flat output។

### ទម្រង់កំណត់ឧបករណ៍

Responses API ប្រើទម្រង់ឧបករណ៍ **flat** — `name`, `description`, `parameters` ជា keys កំពូល (មិនស្តិតនៅក្រោម `function`)។

**មុន (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**ក្រោយ (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

ឧទាហរណ៍ពេញលេញ:
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

ជាមួយ `strict: true` (ការបង្ហាញ schema):
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
            "required": ["city_name"],       # គ្រប់លក្ខណៈអចលនទ្រព្យត្រូវតែចុះបញ្ជី
            "additionalProperties": False,   # ត្រូវការសម្រាប់របៀបតឹងរឹង
        },
    }
]
```

### ការហៅឧបករណ៍ទ្វេដង (អនុវត្តន៍ និងត្រឡប់លទ្ធផល)

ពេលម៉ូឌែលស្នើហៅឧបករណ៍ ប្រើ `response.output` + `function_call_output` — **មិន** ប្រើតួជា `role: assistant` + `role: tool` នៅ Chat Completions ។

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
    # បន្ថែមធាតុ function_call របស់គំរូទៅកាន់ការសន្ទនា
    messages.extend(response.output)

    # ប្រតិបត្តិការប្រើប្រាស់ឧបករណ៍នីមួយៗ ហើយបន្ថែមលទ្ធផល
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # បានលទ្ធផលចុងក្រោយជាមួយលទ្ធផលឧបករណ៍
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### ឧទាហរណ៍ហៅឧបករណ៍ពី few-shot

ពេលផ្ដល់ឧទាហរណ៍ few-shot ហៅឧបករណ៍ ក្នុង `input` ប្រើធាតុ `function_call` និង `function_call_output` ។ រឺបត្តិមួយគួរចាប់ផ្តើមជាមួយ `fc_`។

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
# ឧទាហរណ៍ស្វែងរកបណ្ដាញក្នុងសរយៈដែលមានរួចមកហើយ
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## ការបញ្ចូលរូបភាព

ធាតុកម្រិតរូបភាពផ្លាស់ប្តូរពី `image_url` ទៅជា `input_image` ហើយ URL ផ្លាស់ពីអOBJECT nested ទៅខ្សែអក្សរលាត (flat)។

### ការបញ្ចូលរូបភាព — មុន (Chat Completions)
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

### ការបញ្ចូលរូបភាព — ក្រោយ (Responses API, URL)
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

### ការបញ្ចូលរូបភាព — ក្រោយ (Responses API, base64)
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

> **ការផ្លាស់ប្តូរចម្បង**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (អOBJECT nested) → `"image_url": "..."` (ខ្សែអក្សរលាត — អាចជា HTTPS URL ឬ `data:image/...;base64,...` URI ទិន្នន័យ), (3) `"type": "text"` → `"type": "input_text"`។

## ការផ្លាស់ប្តូរ Microsoft Agent Framework (MAF)

**ពិនិត្យមើល MAF version របស់អ្នកជាមុន** — ការផ្លាស់ប្តូរប្រហែលជាមានអាស្រ័យលើថាតើអ្នកមាន MAF 1.0.0 លើកមួយ ឬ beta/rc មុន 1.0.0។

ដើម្បីពិនិត្យ: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

នៅ MAF 1.0.0+, `OpenAIChatClient` **បានប្រើ Responses API រួចហើយ** — មិនចាំបាច់ផ្លាស់ប្តូរ។

បើ codebase ប្រើ legacy `OpenAIChatCompletionClient` (ប្រើ `chat.completions.create`), ជំនួសដោយ `OpenAIChatClient`:

មុន:
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

ក្រោយ:
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

### មុន MAF 1.0.0 (release beta/rc)

នៅ pre-1.0.0 MAF, `OpenAIChatClient` ប្រើ Chat Completions។ អាប់ដេតទៅ `agent-framework-openai>=1.0.0` ដែល `OpenAIChatClient` ប្រើ Responses API ជាលំនាំដើម។

> **សម្គាល់**: `Agent`, `MCPStreamableHTTPTool` និង API មျគ័ MAF ផ្សេងទៀតនៅតែទៀងទាត់ — មានតែ class client នាំចូល និង បង្កើត instance តែប៉ុណ្ណោះផ្លាស់ប្តូរ។

## ការផ្លាស់ប្តូរ LangChain (`langchain-openai`)

បន្ថែម `use_responses_api=True` ទៅក្នុង `ChatOpenAI()`។ ក៏បំលែងការចូលដំណើរការ message ពី `.content` ទៅ `.text` ផងដែរ។

មុន:
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

# ... ការអញ្ជើញភ្នាក់ងារ ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

ក្រោយ:
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

# ... ការហៅភ្នាក់ងារ ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **ការផ្លាស់ប្តូរចម្បង**: (1) `use_responses_api=True` ក្នុង constructor, (2) `.content` → `.text` លើសារ​ឆ្លើយតប។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->