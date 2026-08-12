# តារាង Cheat Sheet សម្រាប់ Responses API (Python + Azure OpenAI)

> ខ្សែស្រឡាយទាំងអស់ខាងក្រោម គិតថា `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` និង `client` បាន初始化រួចហើយ (សូមមើលការតំឡើង client)។

## សំណើមូលដ្ឋាន
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## ការតំឡើង Client — EntraID (ណែនាំ)
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

## ការតំឡើង Client — API key
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## ការតំឡើង Async Client — EntraID
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

## ការតំឡើង Async Client — EntraID ជាមួយ tenant ច្បាស់លាស់ (multi-tenant)

នៅពេលធនធាន Azure OpenAI នៅក្នុង **tenant ប្លែក** ពី default tenant​ អ្នកត្រូវផ្ទេរទៅ `tenant_id` ដោយច្បាស់ដល់ credential។ នេះគឺជារឿងធម្មតាក្នុងសេណារីយ៉ូ dev/test ដែល tenant ផ្ទះរបស់អ្នកអភិវឌ្ឍន៍ខុសពី tenant របស់ធនធាន។

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential សម្រាប់ផលិតកម្ម (Azure Container Apps, App Service, ល។)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # គោលសម្គាល់គ្រប់គ្រងដែលបានផ្ដល់ឱ្យអ្នកប្រើប្រាស់
)
# AzureDeveloperCliCredential សម្រាប់ dev ក្នុងតំបន់មូលដ្ឋាន — tenant_id ដែលច្បាស់លាស់គឺសំខាន់
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# ស៊េរី: ព្យាយាម managed identity មុនសឹង, បន្តទៅ azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## ការផ្លាស់ប្តូរ Async client — មុន/ក្រោយ

មុន (ចាស់ទាស់):
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

## ការផ្លាស់ប្តូរ sync ពេញលេញ — មុន/ក្រោយ

មុន (ចាស់ — Azure OpenAI Chat Completions):
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

បន្ទាប់ (Responses API — ចំណុចចុង Azure OpenAI v1):
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

## ការចាក់បញ្ចាំង (sync)
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
        print()  # បន្ទាត់ថ្មីនៅចប់
```

## ការចាក់បញ្ចាំង (async)
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

## ការចាក់បញ្ចាំងកម្មវិធីបណ្តាញ — រូបរាងពី backend ទៅ frontend

នៅពេលផ្លាស់ប្តូរកម្មវិធីបណ្ដាញដែលចាក់បញ្ចាំង SSE/JSONL ទៅផ្នែកមុខ (frontend), **ទ្រង់ទ្រាយ serialization backend** នឹងផ្លាស់ប្តូរ។ គូសការបញ្ចេញរបស់ backend ថ្មីដើម្បីរក្សាបែបផែនចូលប្រើរបស់ frontend ដូចដដែល ដូច្នេះ frontend មិនត្រូវការផ្លាស់ប្តូរទេ។

**មុន** — បណ្តាញ Chat Completions backend មានទំនង serialize ជាធម្មតាច្រក `choices[0]` របស់ `chunk` កាលណាលេខ:
```python
# ចាស់: បញ្ជីជម្រើសពេញលេញដែលបានសម្គាល់ជារបារៀងលំដាប់ដោយប្លង់នីមួយៗ
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend អាន: `response.delta.content` (ផ្លូវជ្រៅក្នុងវត្ថុ choice)។

**បន្ទាប់** — Responses API backend បញ្ចេញរូបរាងតិចតួចរក្សាប្រភេទផ្លូវចូលដូចគ្នានៅ frontend:
```python
# ថ្មី: ផ្ទុកតែអ្វីដែលផ្នែកមុខតែប៉ុណ្ណោះ
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend កំពុងអាន `response.delta.content` ដូចមុន — **មិនចាំបាច់មានការផ្លាស់ប្តូរផ្នែកមុខ**។

> **ដំណឹងសំខាន់**: ទំរង់ការចាក់បញ្ចាំង Responses API (`event.type` + `event.delta`) ខុសពី Chat Completions (`chunk.choices[0].delta.content`) ជាលក្ខណៈមូលដ្ឋាន។ ប៉ុន្តែកិច្ចព្រមព្រៀងពី backend ទៅ frontend គឺជារបស់អ្នកត្រូវកំណត់។ គូសកែទ្រង់ទ្រាយ backend ដើម្បីផ្គូផ្គងនឹងចំណាំដែល frontend ចង់បានរួច។

## ដំណើរការកម្មវិធីចាក់បញ្ចាំង

នៅពេល `stream: true`, API នឹងបញ្ចេញព្រឹត្តិការណ៍តាមលំដាប់ដូចខាងក្រោម៖
1. `response.created` – វត្ថុ response ត្រូវបាន初始化
2. `response.in_progress` – ការបង្កើតបានចាប់ផ្តើម
3. `response.output_item.added` – ទំនិញចេញបានបង្កើត
4. `response.content_part.added` – ផ្នែកមាតិកា បានចាប់ផ្តើម
5. `response.output_text.delta` – តួអក្សរច្រើន (ច្រើន, មួយៗមាន `delta: string`)
6. `response.output_text.done` – ការបញ្ចូលអក្សរបញ្ចប់
7. `response.content_part.done` – ផ្នែកមាតិកាបញ្ចប់
8. `response.output_item.done` – ទំនិញចេញបានបញ្ចប់
9. `response.completed` – ការឆ្លើយតបពេញលេញបានបញ្ចប់

សម្រាប់ការចាក់បញ្ចាំងអក្សរជាមូលដ្ឋាន, គ្រាន់តែដោះស្រាយ `response.output_text.delta` (សម្រាប់តួអក្សរ) និង `response.completed` (សម្រាប់បញ្ចប់) เท่านั้น។

## ការដោះស្រាយកំហុសចាក់បញ្ចាំងក្នុងកម្មវិធីបណ្តាញ

នៅពេលចាក់បញ្ចាំងក្នុងកម្មវិធីបណ្ដាញ, អ្នកគួរច្របាច់ iteration async ក្នុង `try/except` ហើយបញ្ចេញកំហុសជាចំណុច JSON ដើម្បីបញ្ជាក់អោយ frontend បង្ហាញបានយ៉ាងរលូន (ឧ. របាំងកំណត់ល្បឿន, បរាជ័យផ្តាច់ពេល):

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

> **ហេតុអ្វីនេះគឺសំខាន់**: Azure OpenAI ឆ្លើយតប `429 Too Many Requests` នៅពេលរបាំងល្បឿន។ បើគ្មាន `try/except`, ការឆ្លើយតបចាក់បញ្ចាំងនឹងស្ងាត់ស្ងៀមបាត់បង់។ មានវា frontend នឹងទទួលបាន `{"error": "Too Many Requests"}` ហើយអាចបង្ហាញស្នើសុំ retry បាន។

## ប្រភេទព្រឹត្តិការណ៍ចាក់បញ្ចាំង (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## ទ្រង់ទ្រាយសន្ទនារ
```python
# អេភ៊ីអាយឆ្លើយតបទ្រទ្រង់ទន់នៃការប្រាស្រ័យទាក់ទងតាមរយៈអារេធ្វើចូល
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

## ការដោះស្រាយកំហុសជាមួយ content filter

រចនាសម្ព័ន្ធ error body ផ្លាស់ប្តូរពី Chat Completions ទៅ Responses API។

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

ផ្ទាំងខុសគ្នា៖
- `innererror` wrapper បាន **ផុតទៅហើយ** — ព័ត៌មានលម្អិតនៃ content filter មាននៅកំពូល `error.body`។
- `content_filter_result` (ឯកតា) → `content_filters` (ជាអារេ plural) មាន `content_filter_results` (plural) ក្នុងចំណោមមួយមួយ entry។
- Entry នីមួយៗក្នុង `content_filters` រួមបញ្ចូល `blocked`, `source_type`, និង `content_filter_results` ដែលមានព័ត៌មានច្បាស់លាស់តាមប្រភេទ (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`)។

ទ្រង់ទ្រាយ error body content filter ពេញលេញ Responses API៖
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

## ការផ្លាស់ប្តូរប្រើ HTTP ទន្លេ (requests/httpx)

ប្រសិនបើកម្មវិធីហៅ Azure OpenAI REST ដោយផ្ទាល់ មិនប្រើ SDK:

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

> **ចំណាំ**: `output_text` គឺជាគុណលក្ខណៈងាយស្រួលមួយនៅលើ Python SDK របស់ `Response` ។ JSON REST ប្រាក់{raw} មិនមានវាល `output_text` លើកំពូលទេ — អក្សរនៅក្នុង `output[0].content[0].text`។

## សន្ទនា multi-turn
```python
# បង្កើតការសន្ទនាមួយជាមួយ Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# បន្ថែមចម្លើយរបស់ជំនួយករទៅក្នុងការសន្ទនា
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

ទ្រង់ទ្រាយ multi-turn ប្រភេទ content (ច្បាស់លាស់ `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turn តាមរយៈ `previous_response_id` (ជាជម្រើស)

ជំនួសមិនបានគ្រប់គ្រង arrays សន្ទនារបស់អ្នកដោយផ្ទាល់, អ្នកអាចភ្ជាប់ responses ជាសំណុំផ្នែក
server-side ដោយប្រើ `previous_response_id`។ API នឹងរក្សារាល់ response ហើយ
ដាក់បញ្ចូលជាមុនរាល់ពន្លឺពីមុន។

```python
# មុខងារដំបូង
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# មុខងារបន្ត — គ្រាន់តែផ្ញើសារ​​អ្នកប្រើថ្មី + លេខសម្គាល់ចម្លើយមុន
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**ពេលណាគួរប្រើលក្ខណៈណា:**

| វិធីសាស្រ្ត | អត្ថប្រយោជន៍ | គុណវិបត្តិ |
|---|---|---|
| `input` array (ដៃគូរ) | គ្រប់គ្រងពេញលេញលើប្រវត្តិ; អាចកាត់ចំណុច/សង្ខេប; មិនចាំបាច់រក្សាទុក server-side (`store=False`) | មានកូដច្រើន; អ្នកគ្រប់គ្រង array ដោយផ្ទាល់ |
| `previous_response_id` | កូដសាមញ្ញ; ភ្ជាប់ស្វ័យប្រវត្តិ | ត្រូវការ `store=True` (លំនាំដើម); សន្ទនាត្រូវបានរក្សា server-side; មិនអាចផ្លាស់ប្តូរប្រវត្តិរវាងពន្លឺបាន |

> **កំណត់សម្គាល់ការផ្លាស់ប្តូរ:** កម្មវិធី Chat Completions ប្រេីសហា្រាប់ដំបូងគ្រប់គ្រងសំណុំសារ ដូចនេះការបំលែងទៅ `input` array ជារបៀបផ្ទាល់ខ្លួន 1:1 ។ ប្រើ `previous_response_id` សម្រាប់កូដថ្មីឬពេលអ្នកមិនចាំបាច់កែប្រែប្រវត្តិសន្ទនា។

## ម៉ូដែល reasoning របស់ O-series (o1, o3-mini, o3, o4-mini)

ម៉ូដែល O-series មានការ​កំណត់​តម្លៃ​ប៉ារ៉ាម៉ែត្រ​វិសេស​នៅពេល​ផ្លាស់ប្តូរ​ទៅ Responses API។

### ការតភ្ជាប់ប៉ារ៉ាម៉ែត្រ​សម្រាប់ o-series

| Chat Completions (o-series) | Responses API | កំណត់សម្គាល់ |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | កំណត់ខ្ពស់ (4096+) — reasoning tokens គិតរួមក្នុងដែនកំណត់ |
| `reasoning_effort` | `reasoning.effort` | រក្សាទុកដូចផ្ទាល់ ប្រសិនបើមាន (ទាប/មធ្យម/ខ្ពស់) |
| `temperature` | លុបចោល ឬកំណត់ជា `1` | O-series ទទួលយកតែ `1` តែប៉ុណ្ណោះ |
| `top_p` | លុបចោល | មិនគាំទ្រ o-series |
| `seed` | លុបចោល | មិនគាំទ្រ Responses API |

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

បន្ទាប់ (Responses API):
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

> **ចំណាំ**: ម៉ូដែល O-series អាចបិទបាំងទ្រង់ទ្រាយចេញនូវ output ខណៈពេល reasoning មុននឹងបញ្ចេញ text deltas។ ការចាក់បញ្ចាំងនៅតែដំណើរការបន្តតែព្រឹត្តិការណ៍ `response.output_text.delta` ពីលើកទីមួយអាចមកយឺតជាងម៉ូដែល GPT។

## ការចូលប្រើ reasoning tokens
```python
# ម៉ូឌែលហេតុផលប្រើហេតុផលខាងក្នុង — អ្នកអាចមើលឃើញចំនួនតួអក្សរហេតុផលដែលបានប្រើ
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

> **សំខាន់**: ប្រើ `max_output_tokens=1000` (មិនមែន 50–200) ដើម្បីគិតទៅលើដំណើរការហ្នឹង reasoning សម្រាប់ម៉ូដែល reasoning។ ម៉ូដែលប្រើ tokens reasoning ខ្នាតខាងក្នុង មុនបង្កើត output ចុងក្រោយ។

## ចេញផ្សាយរចនាសម្ព័ន្ធ — JSON Schema
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

## ការប្រើប្រាស់ឧបករណ៍

- កំណត់មុខងារ​នៅក្នុង `tools` ជាទ្រង់ទ្រាយ Responses API **ស្រួលៗ** — `name`, `description`, និង `parameters` នៅកំពូល (មិនបន្ទាប់ក្រោម `function`)។
- ប្រសិនបើម៉ូដែលស្នើសុំហៅឧបករណ៍ អនុវត្តន៍នៅក្នុងកម្មវិធីរបស់អ្នក ហើយបញ្ចូលលទ្ធផលឧបករណ៍នៅក្នុងសំណើបន្ទាប់ជារបស់ `function_call_output` នៅក្នុង `input`។
- រក្សាទុក schema តិចតួចតែប៉ុណ្ណោះ និងធ្វើ validate inputs មុនការអនុវត្ត។
- នៅពេលប្រើ `strict: true`, គ្រប់លក្ខណៈត្រូវរាយបញ្ជីក្នុង `required` ហើយ `additionalProperties: false` ត្រូវបានកំណត់ជាវេទិកា។

> **⚠️ `pydantic_function_tool()` មិនសមớm**: ជំនួយ `openai.pydantic_function_tool()` នៅតែបង្កើតរចនាសម្ព័ន្ធ nested ចាស់ Chat Completions (`{"type": "function", "function": {"name": ...}}`) មិនត្រូវប្រើជាមួយ `responses.create()`។ សរសេររចនាសម្ព័ន្ធឧបករណ៍ដោយដៃ ឬធ្វើ wrapper ដើម្បីសម្រួល output។

### ទ្រង់ទ្រាយកំណត់ឧបករណ៍

Responses API ប្រើទ្រង់ទ្រាយឧបករណ៍ **ស្រួលៗ** — `name`, `description`, `parameters` ជាគ្រាប់ចម្បង (មិនបន្ទាប់ក្រោម `function`)។

**មុន (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**បន្ទាប់ (Responses API — ស្រួលៗ):**
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

ជាមួយ `strict: true` (គ្រប់គ្រង schema):
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
            "required": ["city_name"],       # គ្រប់លក្ខណៈត្រូវតែបញ្ជាក់
            "additionalProperties": False,   # ត្រូវការសម្រាប់របៀបតឹងរ៉ឹង
        },
    }
]
```

### វិធីហៅឧបករណ៍ round-trip (អនុវត្តន៍ និងត្រឡប់លទ្ធផល)

នៅពេលម៉ូដែលស្នើសុំហៅឧបករណ៍ ប្រើ `response.output` items + `function_call_output` — **មិន** ប្រើរចនាសម្ព័ន្ធ Chat Completions `role: assistant` + `role: tool`។

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
    # បន្ថែមធាតុ function_call របស់ម៉ូដែលទៅក្នុងការសន្ទនា
    messages.extend(response.output)

    # ប្រតិបត្តិមុខងារ ឧបករណ៍មួយៗ ហើយបន្ថែមលទ្ធផល
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # ទទួលបានចម្លើយចុងក្រោយជាមួយនឹងលទ្ធផលឧបករណ៍
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### ឧទាហរណ៍ហៅឧបករណ៍ few-shot

នៅពេលផ្តល់ឧទាហរណ៍ few-shot នៃការហៅឧបករណ៍ក្នុង `input`, ប្រើ `function_call` និង `function_call_output` items។ ម៉ាស៊ីនត្រូវចាប់ផ្តើមជាមួយ `fc_`។

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
# ឧទាហរណ៍ស្វែងរកវេបសាយដែលបង្កើតជាមូលដ្ឋាន
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## ការបញ្ចូលរូបភាព

ធាតុខ្លឹមសាររូបភាពផ្លាស់ប្តូរប្រភេទពី `image_url` ទៅជា `input_image`, ហើយ URL ផ្លាស់ពីវត្ថុ nested ទៅខ្សែអក្សរស្រួល។

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

### ការបញ្ចូលរូបភាព — បន្ទាប់ (Responses API, URL)
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

### ការបញ្ចូលរូបភាព — បន្ទាប់ (Responses API, base64)
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

> **ការផ្លាស់ប្តូរសំខាន់ៗ**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (វត្ថុ nested) → `"image_url": "..."` (ខ្សែអក្សរស្រួលស្រួលៗ — អាចជារៀង HTTPS URL ឬ `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`។

## ការផ្លាស់ប្តូរ Microsoft Agent Framework (MAF)

**ពិនិត្យកំណែ MAF របស់អ្នកជាមុន** — ការផ្លាស់ប្តូរនេះអាស្រ័យលើថាតើអ្នកកំពុងប្រើ MAF 1.0.0+ ឬកំណត់ត្រាបា/កំណែសម្រួលមុន1.0.0។

ដើម្បីពិនិត្យ៖ `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

នៅក្នុង MAF 1.0.0+ `OpenAIChatClient` **បានប្រើ Responses API រួចហើយ** — មិនចាំបាច់ផ្លាស់ប្តូរ។

ប្រសិនបើកូដប្រើ `OpenAIChatCompletionClient` ចាស់ (ដែលប្រើ `chat.completions.create`) ប្តូរជា `OpenAIChatClient`:

មុន៖
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

បន្ទាប់៖
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

### MAF មុន1.0.0 (កំណត់ត្រាបា/rc)

នៅក្នុង MAF មុន1.0.0, `OpenAIChatClient` ប្រើ Chat Completions។ ធ្វើឲ្យថ្មីជា `agent-framework-openai>=1.0.0` ដែល `OpenAIChatClient` ប្រើ Responses API ដោយលំនាំដើម។

> **ចំណាំ**: `Agent`, `MCPStreamableHTTPTool`, និង API MAF ផ្សេងទៀត មិនបានផ្លាស់ប្តូរ — មានតែការនាំចូល class និងការបង្កើត client ទេ។

## ការផ្លាស់ប្តូរ LangChain (`langchain-openai`)

បន្ថែម `use_responses_api=True` ទៅ `ChatOpenAI()`។ ផ្លាស់ប្តូរផ្លូវចូលមាតិកាសារពី `.content` ទៅ `.text` ផងដែរ។

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

# ... ការហៅភ្នាក់ងារ ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

បន្ទាប់:
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

# ... ការអញ្ជើញភ្នាក់ងារ ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **ការផ្លាស់ប្តូរសំខាន់ៗ**: (1) `use_responses_api=True` ក្នុង constructor, (2) `.content` → `.text` លើសារឆ្លើយតប។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->