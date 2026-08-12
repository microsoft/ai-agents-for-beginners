# Responses API Cheat Sheet (Python + Azure OpenAI)

> အောက်ပါ code snippet များသည် `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ကို သတ်မှတ်ပြီး `client` ကို ရှိပြီးသား initialized လုပ်ထားသည်ဟု သတ်မှတ်ထားသည် (client setup ကို ကြည့်ပါ)။

## မူလတောင်းဆိုမှု
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Client setup — EntraID (အကြံပြု)
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

## Async client setup — EntraID with explicit tenant (multi-tenant)

Azure OpenAI resource သည် သတ်မှတ်ထားသော default tenant ကွဲနေသော **tenant မတူညီမှု** ဖြစ်ပါက `tenant_id` ကို credential ထဲသို့ စာတိကျစွာ ပေးပို့ရန် လိုအပ်သည်။ ၎င်းသည် developer ၏ မူလ tenant နှင့် resource tenant မတူသော dev/test အခြေအနေများတွင် ဖြစ်ပေါ်တတ်သည်။

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ထုတ်လုပ်မှုအတွက် ManagedIdentityCredential (Azure Container Apps, App Service၊ စသည်)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # အသုံးပြုသူသတ်မှတ် Managed Identity
)
# ဒေသိယ ဖွံ့ဖြိုးရေးအတွက် AzureDeveloperCliCredential — ဖော်ပြထားသော tenant_id အရေးကြီးသည်
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# ချိန်း: managed identity ကို پہلےစမ်းကြည့်ပြီး၊ မရနိုင်လျှင် azd CLI ကို သုံးပါ။
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async client ပုံစံ ပြောင်းရွှေ့ခြင်း — မတိုင်ခင်/မပြီးစီးခင်

မတိုင်ခင် (deprecated):
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

မပြီးစီးခင်:
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

## Full sync ပုံစံ ပြောင်းရွှေ့ခြင်း — မတိုင်ခင်/မပြီးစီးခิน

မတိုင်ခင် (အဟောင်း — Azure OpenAI Chat Completions):
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

မပြီးစီးခင် (Responses API — Azure OpenAI v1 endpoint):
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

## စတိုင်းမင်းခြင်း (sync)
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
        print()  # အဆုံးတွင် new line ရှိသည်
```

## စတိုင်းမင်းခြင်း (async)
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

## Web app စတိုင်းမင်းခြင်း — backend မှ frontend ပုံစံ

SSE/JSONL ကို frontend သို့ စတိုင်းမင်း လုပ်နေသော web app တစ်ခုကို ပြောင်းရွှေ့ရာတွင်၊ **backend serialization format** ပြောင်းလဲ ရတယ်။ မူရင်း frontend က အသုံးပြုနေသော access ပုံစံကို ထိန်းသိမ်းပြီး frontend တွင် မပြောင်းလဲရန် နေရာသတ် မပေးပဲ အသစ် backend output ကို ဒီဇိုင်း ဆွဲပါ။

**မတိုင်ခင်** — Chat Completions backend သည် လူကြိုက်များစွာနှင့် ရိုးရှင်းစွာ `choices[0]` dict ကို serialize လုပ်သည်။
```python
# အဟောင်း: ခွဲစိတ်တိုင်းအတွက် စီးရီးလိုက်ထားသော အပြည့်အစုံရွေးချယ်မှတ်တမ်း
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend သည် `response.delta.content` ကို ဖတ်တတ်သည် (choice object ၏နက်ရှိုင်းထဲ)။

**မပြီးစီးခင်** — Responses API backend သည် frontend လက်ရှိ access လမ်းကြောင်းကို ထိန်းသိမ်းထားသော အနည်းဆုံး ပုံစံ ထုတ်လွှင့်သည်။
```python
# အသစ်: frontend မှ လိုအပ်သည့်အရာများကိုသာ ထုတ်ပြန်ပေးသည်
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend သည် ထိုအတိုင်း `response.delta.content` ကို ဖတ်သုံးသည် — **frontend တွင် မပြောင်းလဲရန် မလိုပါ**။

> **အဓိက သိရှိရန်**: Responses API streaming ပုံစံသည် (`event.type` + `event.delta`) သည် Chat Completions ၏ (`chunk.choices[0].delta.content`) သဟဇာတ မဟုတ်ပါ။ သင့် backend နှင့် frontend အကြား အွန်ရှီ contract သည် သင့်ပိုင်ဖြစ်သည်။ ဝန်ဆောင်မှုလမ်းကြောင်း အတိုင်း backend output ကို ဖန်တီးပါ။

## Streaming event စဉ်

`stream: true` ဖြစ်သောအခါ API သည် အောက်ပါ event များကို အစဉ်လိုက် ထုတ်ပေးသည်။
1. `response.created` – response object စတင် initialize ဖြစ်
2. `response.in_progress` – စတင်သွားခြင်း
3. `response.output_item.added` – output item ဖန်တီးခြင်း
4. `response.content_part.added` – content part စတင်ခြင်း
5. `response.output_text.delta` – စာသားပိုင်းများ (အတော်များများ, တစ်ခုချင်းစီတွင် `delta: string` ပါသည်)
6. `response.output_text.done` – စာသားထုတ်လုပ်မှု ပြီးဆုံးခြင်း
7. `response.content_part.done` – content part ပြီးဆုံးခြင်း
8. `response.output_item.done` – output item ပြီးဆုံးခြင်း
9. `response.completed` – ပြည့်စုံသော response ဖြစ်ခြင်း

မူလ စာသားစတိုင်းမင်းလုပ်ရာတွင် `response.output_text.delta` (စာသား chunk များအတွက်) နှင့် `response.completed` (ပြီးစီးခြင်းအတွက်) ကိုသာ ကိုင်တွယ်ပါ။

## Web app များတွင် စတိုင်းမင်းခြင်း error ကိုင်တွယ်မှု

Web app မှာ စတိုင်းမင်းလုပ်စဉ်၊ async iteration ကို `try/except` ဖြင့် ဝတ်ပြီး error များကို JSON အဖြစ် ပေးပို့ပါက frontend သည် သေချာစွာ ပြသနိုင်သည် (ဥပမာ၊ rate limit, အချိန်ကာလတုန်းစွဲမှားယွင်းမှုများ)။

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

> **ဘာကြောင့် အရေးကြီးသလဲ**: Azure OpenAI မှ rate limit ဖြစ်သောအခါ `429 Too Many Requests` ပြန်ပေးသည်။ `try/except` မပါမဖြစ်လျှင် streaming response သည် တစ်ချက်တည်း သေဆုံးသွားတတ်သည်။ ပါလျှင် frontend သည် `{"error": "Too Many Requests"}` ကိုရရှိပြီး retry prompt ကို ပြသနိုင်သည်။

## Streaming event အမျိုးအစားများ (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## စကားပြောပုံစံ
```python
# တုံ့ပြန်မှုများ API သည် အလယ်ခံအရေအတွက်မှတဆင့် စကားဝိုင်းပုံစံကို ထောက်ပံ့သည်။
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

## Content filter error ကိုင်တွယ်မှု

Error body ၏ ဖွဲ့စည်းမှုသည် Chat Completions မှ Responses API သို့ ပြောင်းလဲသွားသည်။

မတိုင်ခင် (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

မပြီးစီးခင် (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

အဓိကကွာခြားချက်များ
- `innererror` wrapper သည် **ပျောက်သွားပြီး** — content filter အသေးစိတ်များကို error.body ၏ ထိပ်ဆုံးတွင် ပါရှိသည်။
- `content_filter_result` (တစ်ခု) မှ `content_filters` (အရေအတွက် များ) အဖြစ်ပြောင်းလဲပြီး၊ ထည့်သွင်းထားသော `content_filter_results` များပါရှိသည်။
- `content_filters` ၏ entry တစ်ခုစီတွင် `blocked`, `source_type`, နှင့် category အလိုက် အသေးစိတ်များဖြစ်သည့် (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) ပါဝင်သည်။

Responses API content filter error body ၏ ပြည့်စုံပုံစံ:
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

## Raw HTTP ပြောင်းရွှေ့ခြင်း (requests/httpx)

SDK အသုံးမပြုဘဲ Azure OpenAI REST ကိုတိုက်ရိုက် ခေါ်ယူရာတွင် -

မတိုင်ခင် (Chat Completions):
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

မပြီးစီးခင် (Responses API):
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

> **မှတ်ချက်**: Python SDK ၏ Response object တွင် `output_text` သည် အဆင်ပြေခြင်းအတွက် property ဖြစ်သည်။ raw REST JSON response တွင် `output_text` ထိပ်တန်းကွင်းမရှိပါ — စာသားသည် `output[0].content[0].text` တွင်ရှိသည်။

## မြောက်ထပ် စကားပြောခြင်း
```python
# Responses API နဲ့ စကားပြောပွဲ တည်ဆောက်ပါ
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# အကူအညီပေးသူရဲ့ တုံ့ပြန်ချက်ကို စကားပြောပွဲထဲ ထည့်ပါ
messages.append({"role": "assistant", "content": response.output_text})

# စကားပြောပွဲကို ဆက်လက်လုပ်ဆောင်ပါ
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

အကြောင်းအရာအမျိုးအစားမြောက်ထပ် (explicit `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` အသုံးပြုပြီး မြောက်ထပ်စကားပြောခြင်း (နည်းလမ်းအခြား)

ဤနည်းလမ်းဖြင့် conversation array ကို ကိုင်တွယ်မလုပ်ဘဲ၊ `previous_response_id` ဖြင့် server-side တွင် responses များကို ချိတ်ဆက်နိုင်သည်။
API သည် နောက်ပြန်ဖြတ်ထားသော turn များကို အလိုအလျောက် ထည့်သွင်းသည်။


```python
# ပထမအကြိမ်လှည့်ခြင်း
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# နောက်ထပ်အကြိမ်များ - အသုံးပြုသူ၏သစ်သည့်စာစောင်နှင့် အရင်ဆုံးဖြေကြားချက်အိုင်ဒီကိုပို့ရန်သာဖြစ်သည်။
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**ဘယ်အချိန် ဘယ်အတိုင် အသုံးပြုမလဲ**

| နည်းလမ်း | အားသာချက် | ဆိုးကျိုး |
|---|---|---|
| `input` array (လက်ဖြင့်) | မှတ်တမ်း အပြည့်အစုံ ထိန်းချုပ်နိုင်သည်၊ trim/summarize လုပ်နိုင်၊ server-side တွင် သိမ်းဆည်းရန် မလို (`store=False`) | code များသည် ကျယ်၊ array ကို ကိုင်တွယ်ရသည် |
| `previous_response_id` | code လျော့နည်း၊ ချိတ်ဆက်မှုကို အလိုအလျောက်လုပ်ဖြစ် | `store=True` ကတိ၊ conversation server-side တွင် သိမ်းဆည်းပြီးဖြစ်သည်၊ turns အကြား သမိုင်းကို မပြင်ဆင်နိုင် |

> **ပြောင်းရွှေ့ရေးမှတ်ချက်**: Chat Completions အများစုသည် messaging array ကိုကိုင်တွယ်ပြီးသားဖြစ်သောကြောင့် `input` array သို့ ပြောင်းရွှေ့ခြင်းမှာ ပိုမို တိုရပ်တိုင်းတိ ဖြစ်သလောက်ဖြစ်သည်။ မူလစာသားများကို မပြင်လိုလျှင် `previous_response_id` ကို အသုံးပြုပါ။

## O-series reasoning မော်ဒယ်များ (o1, o3-mini, o3, o4-mini)

O-series မော်ဒယ်များမှာ Responses API သို့ ပြောင်းရွှေ့စဉ် parameter ကန့်သတ်ချက်များ ထူးခြားသည်။

### O-series အတွက် parameter mapping

| Chat Completions (o-series) | Responses API | မှတ်ချက်များ |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | မြင့်ထားရန် (4096+), reasoning token များသည် ကန့်သတ်ချက်ကို ထိခိုက်သည် |
| `reasoning_effort` | `reasoning.effort` | ရှိလျှင် မပြောင်းလဲ အသုံးပြုရန် (low/medium/high) |
| `temperature` | ဖယ်ရှားရန် သို့မဟုတ် `1` သတ်မှတ်ရန် | O-series သည် `1` ဖြင့်သာ လက်ခံသည် |
| `top_p` | ဖယ်ရှားရန် | O-series တွင် မပံ့ပိုးပါ |
| `seed` | ဖယ်ရှားရန် | Responses API တွင် မပံ့ပိုးပါ |

### O-series မတိုင်ခင်/မပြီးစီးခင်

မတိုင်ခင် (Chat Completions နှင့် o-series):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

မပြီးစီးခင် (Responses API):
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

> **မှတ်ချက်**: O-series မော်ဒယ်များသည် reasoning လုပ်စဉ်တွင် စာသား delta များ ထုတ်ပြန်ရန်မတိုင်မှီ buffered output များ ဖြစ်စေတတ်သည်။ Streaming သည် အဆက်မပြတ် လည်ပတ်သည့် အခြေအနေဖြစ်သော်လည်း GPT မော်ဒယ်များထက် ပထမဆုံး `response.output_text.delta` event သည် နှောင့်နှေးစွာ ရောက်ရှိနိုင်သည်။

## Reasoning tokens ကို ပြန်လည်ရယူခြင်း
```python
# အတွင်းအကြောင်းအရာတွေကိုသုံးပြီး အကြောင်းတရားထုတ်လုပ်ခြင်းမော်ဒယ်တွေ သုံးတယ် — ဘယ်လောက်ရှင်းလင်းချက်များအသုံးပြုထားကြောင်းကိုတွေ့နိုင်ပါတယ်
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

> **အရေးကြီးချက်**: Reasoning မော်ဒယ်များ၏ အတွင်းရေး Reasoning လုပ်ငန်းစဉ်အတွက် တွက်ချက်မှုဖြစ်သောကြောင့် `max_output_tokens=1000` (50–200 မဟုတ်) ကို အသုံးပြုပါ။ မော်ဒယ်သည် အတွင်းရေး Reasoning tokens များကို အသုံးပြု၍ နောက်ဆုံး output ကို ထုတ်ပေးသည်။

## ဖွဲ့စည်းတည်ဆောက် output — JSON Schema
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

## ကိရိယာအသုံးပြုခြင်း

- `tools` မှာ functions ကို **flat Responses API ပုံစံ** ဖြင့် သတ်မှတ်ပါ — top level တွင် `name`, `description`, နှင့် `parameters` ပါ (function အောက်တွင် မဟုတ်)။
- မော်ဒယ်က tool ခေါ်ဆိုအခါ app ထဲတွင် ပြုလုပ်ပြီး နောက်တောင်းဆိုမှုတွင် tool ရလဒ်ကို `function_call_output` item အဖြစ် `input` ကြား ထည့်သွင်းပါ။
- schema များကို သက်သာေရမယ့် ပုံစံနည်းနည်းထားပြီး input များကို တိုးတက်စွာ စစ်ဆေးပါ။
- `strict: true` သုံးသည့်အခါ property အားလုံးကို `required` ထဲသို့ ရေးထည့်ရမည့်အပြင် `additionalProperties: false` အကျဉ်းချုပ် ပြုလုပ်ရမည်။

> **⚠️ `pydantic_function_tool()` သည် မလိုက်ဖက်ပါ**: `openai.pydantic_function_tool()` helper သည် ယခင် Chat Completions nested ပုံစံ (`{"type": "function", "function": {"name": ...}}`) ကို မရစ်ပြန်တက်သေးပါ။ `responses.create()` နဲ့ မသုံးစွဲရ။ Tool schemas ကို ကိုယ်တိုင် သတ်မှတ်ပါ သို့မဟုတ် wrapper တစ်ခုရေးပြီး output ကို flat ပြုပြင်ပါ။

### ကိရိယာသတ်မှတ်ပုံစံ

Responses API သည် **flat** tool ပုံစံတစ်ခုကို အသုံးပြုသည် — `name`, `description`, `parameters` သည် top-level key များဖြစ်သည် (function အောက်မှာ မဟုတ်)။

**မတိုင်ခင် (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**မပြီးစီးခင် (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

ပြည့်စုံတဲ့ နမူနာ -
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

`strict: true` ဖြင့် (schema လိုက်နာမှု):
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
            "required": ["city_name"],       # အတွက်ပိုင်ဆိုင်မှုအားလုံးကို လက်မှတ်စာရင်းထဲတွင် ပါဝင်ရမည်
            "additionalProperties": False,   # တင်းကြပ်သော mode အတွက် လိုအပ်သည်
        },
    }
]
```

### ကိရိယာခေါ်ဆိုခြင်း round-trip (လုပ်ဆောင်ပြီး ရလဒ် ပြန်လည်ပို့ခြင်း)

မော်ဒယ်က tool call တောင်းဆိုရင် `response.output` item များနှင့် `function_call_output` ကို အသုံးပြုပါ — Chat Completions ၏ `role: assistant` + `role: tool` ပုံစံမဟုတ်ပါ။

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
    # မော်ဒယ်၏ function_call ပစ္စည်းများကို စကားပြောပွဲထဲ ထည့်ရန်
    messages.extend(response.output)

    # ကိရိယာတစ်ခုစီ ကို ဖျော်ဖြေပြီး ရလဒ်များ ထည့်ရန်
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # ကိရိယာရလဒ်များနှင့်အတူ နောက်ဆုံးတုံ့ပြန်ချက်ရယူရန်
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### ကိရိယာခေါ်ဆိုခြင်းနမူနာ အနည်းငယ်

`input` တွင် tool call နမူနာတွေ တွဲမီးသွင်းရာ `function_call` နှင့် `function_call_output` item များကို အသုံးပြုပါ။ ID များမှာ `fc_` နဲ့ စတင်ရမည်။

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
# တပ်ဆင်ထားသော ဝဘ်ရှာဖွေမှု နမူနာ
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Image input

ပုံအကြောင်းအရာ item များသည် `image_url` မှ `input_image` သို့ ပြောင်းလဲပြီး URL သည် nested object မှ flat string သို့ ပြောင်းသည်။

### Image input — မတိုင်ခင် (Chat Completions)
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

### Image input — မပြီးစီးခင် (Responses API, URL)
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

### Image input — မပြီးစီးခင် (Responses API, base64)
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

> **အဓိကပြောင်းလဲမှုများ**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (nested object မှ) → `"image_url": "..."` (flat string — HTTPS URL သို့မဟုတ် `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"` ဖြစ်သည်။

## Microsoft Agent Framework (MAF) ပြောင်းရွှေ့ခြင်း

**MAF version ကို ပထမဦးစွာ စစ်ဆေးပါ** — ပြောင်းတမ်းသည် MAF 1.0.0+ သို့မဟုတ် pre-1.0.0 beta/rc မဟုတ်ခြင်းပေါ်တွင် အခြေခံသည်။

စစ်ဆေးရန်: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ တွင် `OpenAIChatClient` သည် **Response API ကို အသုံးပြုပြီးဖြစ်** — ပြောင်းရွှေ့ရန် မလိုပါ။

legacy `OpenAIChatCompletionClient` (chat.completions.create သုံးသည်) ကို သုံးနေပါက `OpenAIChatClient` သို့ ပြောင်းပါ။

မတိုင်ခင်:
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

မပြီးစီးခင်:
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

### MAF pre-1.0.0 (beta/rc များ)

pre-1.0.0 MAF တွင် `OpenAIChatClient` သည် Chat Completions ကို သုံးသည်။ `agent-framework-openai>=1.0.0` သို့ အဆင့်မြှင့်ပါ၊ ဤသို့ရင် `OpenAIChatClient` သည် Responses API ကို ပုံမှန်အသုံးပြုပါသည်။

> **မှတ်ချက်**: `Agent`, `MCPStreamableHTTPTool` နှင့် အခြား MAF API များ မပြောင်းလဲသေးပါ — client class import နှင့် instantiation သာ ပြောင်းလဲသည်။

## LangChain (`langchain-openai`) ပြောင်းရွှေ့ခြင်း

`ChatOpenAI()` သို့ `use_responses_api=True` ကို ထည့်ပါ။ message content မှ `.content` ကို `.text` သို့ပြောင်းလဲပါ။

မတိုင်ခင်:
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

# ... ကိုယ်စားလှယ်ခေါ်ယူမှု ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

မပြီးစီးခင်:
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

# ... အေးဂျင့်ခေါ်ယူမှု ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **အဓိကပြောင်းလဲမှုများ**: (1) constructor တွင် `use_responses_api=True` ဖြစ်ခြင်း, (2) response messages တွင် `.content` မှ `.text` သို့ ပြောင်းလဲခြင်း။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->