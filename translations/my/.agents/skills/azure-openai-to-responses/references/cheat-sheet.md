# Responses API Cheat Sheet (Python + Azure OpenAI)

> အောက်ပါ စနစ်လုတ်အားလုံးသည် `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` နှင့် `client` ကို မူရင်းသတ်မှတ်ပြီးဖြစ်သည်ဟု သတ်မှတ်ထားသည် (client တပ်ဆင်ခြင်းကိုကြည့်ပါ)။

## အခြေခံတောင်းဆိုမှု
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Client တပ်ဆင်ခြင်း — EntraID (အကြံပြု)
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

## Client တပ်ဆင်ခြင်း — API key
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async client တပ်ဆင်ခြင်း — EntraID
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

## Async client တပ်ဆင်ခြင်း — EntraID နှင့် ထူးခြား tenant (အဆင့်မြင့်စနစ်)

Azure OpenAI အရင်းအမြစ်သည် **ကောင်းမကွဲခြားသော tenant** တွင်ရှိသည်ဆိုပါက `tenant_id` ကို credential သို့ ထပ်မံပေးပို့ရန်လိုသည်။ ဒါဟာ developer ၏ မူလ tenant နှင့် ရင်းနှီးမှု tenant မတူသော dev/test အခြေအနေများတွင် မကြာခဏ တွေ့ရှိသည်။

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ထုတ်လုပ်မှုအတွက် ManagedIdentityCredential (Azure Container Apps, App Service, စသည်များ)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # အသုံးပြုသူပေးအပ်ထားသော managed identity
)
# ဒေတာပိုင်းဆိုင်ရာဖွံ့ဖြိုးတိုးတက်မှုအတွက် AzureDeveloperCliCredential — tenant_id ကိုရှင်းလင်းထုတ်ဖော်မှုသည် အရေးကြီးသည်
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Chain: ပထမဦးဆုံး managed identity ကိုကြိုးစားပါ၊ မအောင်မြင်လျှင် azd CLI ကိုအသုံးပြုပါ
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async client ပြောင်းရွှေ့မှု — မတိုင်မီ/ပြီးနောက်

မတိုင်မီ (အသုံးမပြုတော့သော):
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

ပြီးနောက်:
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

## ပြည့်စုံစနစ်ပြောင်းရွှေ့မှု — မတိုင်မီ/ပြီးနောက်

မတိုင်မီ (အတိတ်ကာလ — Azure OpenAI Chat Completions):
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

ပြီးနောက် (Responses API — Azure OpenAI v1 endpoint):
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

## စီးဆင်းမှု (sync)
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
        print()  # အဆုံးတွင် တန်းသစ်ထည့်ပြီး
```

## စီးဆင်းမှု (async)
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

## ဝက်ဘ်အက်ပ် စီးဆင်းမှု — backend မှ frontend ပုံစံ

SSE/JSONL ကို frontend သို့ စီးဆင်းမှု stream ပြောင်းရွှေ့သော ဝက်ဘ်အက်ပ်တစ်ခုကို ပြောင်းရွှေ့သောအခါမှာ **backend serialization ပုံစံ** ပြောင်းလဲသည်။ Backend ထုတ်လုပ်မှုအသစ်ကို ရှိပြီးသား frontend ၏ ရယူမှု နမူနာများကို မပြောင်းလဲစေဘဲ ဒီဇိုင်းဆွဲပါ။

**မတိုင်မီ** — Chat Completions backend သည် အကြိမ်များစွာ `choices[0]` dict ကို serialized လုပ်ပေးသည့်ပုံစံဖြစ်သည်။
```python
# ဟောင်း: ချန်ခ််တစ်ခုစီအတွက် စစ်ဆေးပြီး စုစည်းထားသော အပြည့်အဝ ရွေးချယ်မှု dict
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend အတွက် ရှာဖွေဖတ်ခြင်း: `response.delta.content` (choice object ၏ နက်ရှိုင်းသောလမ်းကြောင်း)။

**ပြီးနောက်** — Responses API backend သည် frontend ၏ ရှိပြီးသား လမ်းကြောင်းကို ထိန်းသိမ်းထားသော အနည်းငယ်ပုံစံ ထုတ်ပေးသည်။
```python
# အသစ်: ရှေ့နောက်ပိုင်းလိုအပ်သမျှသာ ထုတ်ပေးပါ
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend သည် `response.delta.content` ကို ဆက်လက်ဖတ်သည် — **frontend အတွက် ပြောင်းလဲမှု မလိုအပ်ပါ**။

> **အဓိက ကျွမ်းကျင်မှု**: Responses API စီးဆင်းမှုပုံစံ (`event.type` + `event.delta`) သည် Chat Completions (`chunk.choices[0].delta.content`) နှင့် မတူညီသည်။ သို့သော် သင်၏ backend မှ frontend သို့ သဘောတူညီချက်ကို သင့်နည်းလမ်းဖြင့် သတ်မှတ်နိုင်သည်။ Backend ထုတ်လွှတ်မှုကို frontend ၏ မျှော်လင့်ချက်နှင့် ကိုက်ညီအောင် ဖန်တီးပါ။

## စီးဆင်းမှု event အစဉ်လိုက်

`stream: true` ဖြစ်သောအခါ API သည် အောက်ပါ အစဉ်လိုက်ဖြင့် event များ ထုတ်ပေးသည်။
1. `response.created` – response object စတင်တည်ဆောက်ခြင်း
2. `response.in_progress` – ဖန်တီးမှု စတင်ခြင်း
3. `response.output_item.added` – အထွက်ပစ္စည်း တည်ဆောက်ခြင်း
4. `response.content_part.added` – အကြောင်းအရာ အစိတ်အပိုင်း စတင်ခြင်း
5. `response.output_text.delta` – စာသား အပိုင်းအစများ (အများအပြား၊ တစ်ခုချင်းစီတွင် `delta: string`)
6. `response.output_text.done` – စာသားဖန်တီးမှု ပြီးဆုံးခြင်း
7. `response.content_part.done` – အကြောင်းအရာ အစိတ်အပိုင်း ပြီးဆုံး
8. `response.output_item.done` – အထွက်ပစ္စည်း ပြီးဆုံးခြင်း
9. `response.completed` – ပြည့်စုံသော response ပြီးဆုံးမှု

အခြေခံ စာသားစီးဆင်းမှုအတွက် `response.output_text.delta` (စာသား အပိုင်းအစများအတွက်) နှင့် `response.completed` (ပြီးဆုံးခြင်းအတွက်) ကိုသာ ကိုင်တွယ်ပါ။

## ဝက်ဘ်အက်ပ်များတွင် စီးဆင်းမှုအမှား မျက်နှာချင်းဆိုင်ဆောင်ရွက်ခြင်း

ဝက်ဘ်အက်ပ်အတွင်း စီးဆင်းမှုကို async iteration ကို `try/except` ဖြင့် ထူထောင်ပြီး အမှားများကို JSON အဖြစ် ထုတ်ပေးပါ၊ ထိုကဲ့သို့ frontend သည် အဆင်ပြေစွာ ပြသနိုင်ပါသည် (ဥပမာ-rate limit, ပျက်ကွက်မှုများ)။

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

> **ဘာကြောင့် အရေးကြီးသနည်း**: Azure OpenAI သည် rate limiting အတွင်း `429 Too Many Requests` ပြန်ပေးပါသည်။ `try/except` မပါဘဲဆို streaming response သည် silently မဖြစ်ပါဘူး။ ပါရှိရင် frontend သည် `{"error": "Too Many Requests"}`ကို လက်ခံပြီး ထပ်မံကြိုးစားရန် ဖော်ပြနိုင်ပါသည်။

## Streaming event အမျိုးအစားများ (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## စကားပြောစနစ်ပုံစံ
```python
# Responses API သည် input အနေဖြင့် array ကို အသုံးပြု၍ စကားဝိုင်းဖော်မတ်ကို ပံ့ပိုးသည်။
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

## အကြောင်းအရာ စစ်တမ်းအမှား ကိုင်တွယ်ခြင်း

အမှား အုပ်စုဖွဲ့ခြင်းသည် Chat Completions မှ Responses API သို့ ပြောင်းလဲခဲ့သည်။

မတိုင်မီ (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ပြီးနောက် (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

အဓိက ကွာခြားချက်များ-
- `innererror` wrapper သည် **ပျောက်ဆုံးပြီး** — content filter အသေးစိတ်အချက်အလက်များသည် `error.body` ၏ အထက်ဆုံးအဆင်း၌ ရှိသည်။
- `content_filter_result` (တစ်ခု) မှ `content_filters` (စနစ်စု များ) သို့ ပြောင်းလဲပြီး ၎င်းတွင် `content_filter_results` များ ပါရှိသည်။
- `content_filters` အတွင်း  အသီးအသီးတွင် `blocked`, `source_type`, နှင့်  category လိုက် အသေးစိတ်ပါဝင်သော `content_filter_results` (ဥပမာ- `jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) ပါရှိသည်။

Responses API ၏ အပြည့်အစုံ content filter အမှား တည်ဆောက်ပုံ-
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

## Raw HTTP ပြောင်းရွွေ့မှု (requests/httpx)

အက်ပ်သည် SDK မှလွဲ၍ Azure OpenAI REST ကို တိုက်ရိုက်ခေါ်ဆိုပါက-

မတိုင်မီ (Chat Completions):
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

ပြီးနောက် (Responses API):
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

> **မှတ်ချက်** - `output_text` သည် Python SDK ၏ `Response` အရာဝတ္ထုတွင် အသုံးပြုရ လွယ်ကူသော အချက်အလက် ဖြစ်သည်။ Raw REST JSON တုံ့ပြန်မှုတွင် ထိပ်ဆုံး `output_text` နယ်ပယ် မရှိပါ — စာသားကို `output[0].content[0].text` တွင် တွေ့ရသည်။

## Multi-turn စကားပြောခြင်း
```python
# Responses API နှင့် ကုသမှုတစ်ခုတည်ဆောက်ပါ
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# အကူအညီပေးသူ၏ ဖြေကြားချက်ကို စကားပြောပွဲထဲထည့်ပါ
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

အကြောင်းအရာအမျိုးအစား ဝင်ရောက်မှုနဲ့ multi-turn (သိသာသော `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` ဖြင့် multi-turn (နည်းလမ်းပြောင်း)

သင်၏ စကားပြောကြားမှု စနစ်ကို ကိုယ်တိုင် စီမံခန့်ခွဲရန် အစား server လက်တွဲဖြင့် `previous_response_id` ကို အသုံးပြုနိုင်သည်။ API သည် တုံ့ပြန်ချက်အားလုံးကို သိမ်းဆည်းပြီး အလိုအလျောက် ယခင် တုန့်ပြန်ချက်များကို ဆက်စပ်ထည့်သည်။



**ဘယ်အခါ ဘယ်ဟာသုံးရမလဲ။**


|---|---|---|
| `input` စာရင်း (လက်ရှိ) | သမိုင်းကြောင်းကို ထိန်းချုပ်မှု ပြည့်ဝ; ဖြတ်တောက်/ အနှစ်ချုပ် ပြုလုပ်နိုင်; server storage မလိုအပ် (`store=False`) | ကုဒ်ပို; စာရင်းကို ကိုယ်တိုင် စီမံရမည် |
| `previous_response_id` | ကုဒ်သိပ်ရိုးရှင်း; အလိုအလျောက်ဆက်သွယ်မှု | `store=True` (ပုံမှန်) လိုအပ်; စကားပြောဆက်အောင် server တွင် သိမ်းဆည်း; သမိုင်းကြောင်းကို turn များကြား ပြင်ဆင်လို့မရ |




## O-series reasoning မော်ဒယ်များ (o1, o3-mini, o3, o4-mini)

O-series မော်ဒယ်များသည် Responses API သို့ ပြောင်းရွှေ့သောအခါ ထူးခြားသော parameter ကန့်သတ်ချက်များရှိသည်။

### o-series များအတွက် parameter mapping

| Chat Completions (o-series) | Responses API | မှတ်ချက်များ |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | ၄၉၀၆+ အထက် သတ်မှတ်ပါ — နည်းချက် tokens များသည် ကန့်သတ်ချက်အတွက် ရေတွက်ပါသည် |
| `reasoning_effort` | `reasoning.effort` | ရှိလျှင် မပြောင်းဘဲထားပါ (နိမ့်/အလတ်/မြင့်) |
| `temperature` | ဖယ်ရှားပါ သို့မဟုတ် `1` သို့ သတ်မှတ်ပါ | O-series သာ `1` ကို လက်ခံသည် |
| `top_p` | ဖယ်ရှားပါ | o-series တွင် မထောက်ခံပါ |
| `seed` | ဖယ်ရှားပါ | Responses API တွင် မထောက်ခံပါ |

### O-series မတိုင်မီ/ပြီးနောက်

မတိုင်မီ (o-series ဖြင့် Chat Completions):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

ပြီးနောက် (Responses API):
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

> **မှတ်ချက်**: O-series မော်ဒယ်များသည် စဉ်းစားမှုအတွင်း ထွက်ရှိမှုများကို မိမိထွက်ရှိမှုများပေးမီ ဘာဖာဖြစ်နိုင်သည်။ Streaming သည် အလုပ်လုပ်သေးသည်၊ သို့သော် ပထမ `response.output_text.delta` ပြုလုပ်မှုသည် GPT မော်ဒယ်များနှင့်နှိုင်းယှဉ်လျှင် ပိုကြာမြင့်နိုင်သည်။

## စဉ်းစားမှု tokens များသုံးလမ်း
```python
# ရှင်းလင်းတင်ပြမှု မော်ဒယ်များသည် အတွင်းပိုင်း ရှင်းလင်းတင်ပြမှုကို အသုံးပြုသည် — ဘယ်နှစ်ခုပြန်လည်ရှင်းလင်းမှု token တွေကို အသုံးပြုခဲ့သည်ကို မြင်နိုင်သည်
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

> **အရေးကြီးသည်**: reasoning မော်ဒယ်များ၏ အတွင်းစဉ်းစားမှုလမ်းညွှန်မှုကို သတိထားရန် `max_output_tokens=1000` (50–200 မဟုတ်) ကို အသုံးပြုပါ။ မော်ဒယ်သည် နောက်ဆုံးထွက်ရှိမှုထုတ်မပေးမီ အတွင်းရေးအတွက် reasoning tokens များကို အသုံးပြုသည်။

## ဖော်ပြထားသော ထွက်ရှိမှု — JSON စနစ်
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

## ကိရိယာ အသုံးပြုမှု

- `tools` တွင် ဖန်တီးချက်များကို **flat Responses API ပုံစံ** ဖြင့် သတ်မှတ်ပါ — အပေါ်ဆုံး `name`၊ `description` နှင့် `parameters` (function အောက်တွင် မထည့်ပါနှင့်)။
- မော်ဒယ်သည် ကိရိယာခေါ်ရန် မေးပါက၊ သင့် app တွင် ပြုလုပ်ပြီး နောက်တန်းအဖြစ် `input` ထဲရှိ `function_call_output` ပစ္စည်းအဖြစ် ထည့်ပါ။
- schemas များကို အနည်းဆုံးထားပြီး အကောင်အထည်ဖော်မပြုမီ အချက်အလက်မှန်ကန်မှုကို စစ်ဆေးပါ။
- `strict: true` ကို အသုံးပြုသည့်အခါ၊ အားလုံးသော property များကို `required` ထဲတွင်စာရင်းပြုထားရမည်၊ `additionalProperties: false` သည် လိုအပ်သည်။

> **⚠️ `pydantic_function_tool()` သည် မလိုက်ဖက်ပါ**: `openai.pydantic_function_tool()` helper သည် ယခင် Chat Completions nested ပုံစံ (`{"type": "function", "function": {"name": ...}}`) ကို မကြာသေးမီ generate လုပ်ဆောင်သေးပါသည်။ `responses.create()` နှင့် မသုံးပါနှင့်။ ကိရိယာ schemas များကို ကိုယ်တိုင်သတ်မှတ်ပါ သို့မဟုတ် ထွက်ရှိမှုကို flat ဖို့ wrapper တစ်ခုရေးပါ။

### ကိရိယာသတ်မှတ်ပုံစံ

Responses API သည် **flat** ကိရိယာ ပုံစံကို သုံးသည် — `name`၊ `description` နှင့် `parameters` မည်သည်တို့သည် function အောက်မရှိပါ။

**မတိုင်မီ (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**ပြီးနောက် (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

နမူနာပြည့်စုံ:
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

`strict: true` (schema ထိန်းသိမ်းမှု) ဖြင့်:
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
            "required": ["city_name"],       # အမျိုးအစားအားလုံးကို ထည့်သွင်းဖော်ပြရန် မဖြစ်မနေလိုအပ်သည်
            "additionalProperties": False,   # တင်းကြပ်သော mode အတွက် လိုအပ်ပါသည်
        },
    }
]
```

### ကိရိယာခေါ်ဆောင်မှု လည်ပတ်မှု (ကိုင်တွယ်ဆောင်ရွက်ပြီး ရလဒ်ပြန်ပေးခြင်း)

မော်ဒယ်သည် ကိရိယာခေါ်ရန် တောင်းဆိုပါက၊ `response.output` ပစ္စည်းများနဲ့ `function_call_output` ကို သုံးပါ — Chat Completions ၏ `role: assistant` နှင့် `role: tool` ပုံစံ မသုံးပါနှင့်။

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
    # မော်ဒယ်ရဲ့ function_call အချက်အလက်တွေကို စကားပြောဆက်သွယ်မှုထဲထည့်ပါ
    messages.extend(response.output)

    # တစ်ခုချင်းစီသော တူးလ်ကို ထည့်သွင်းအသုံးပြုပြီး ရလဒ်တွေထည့်ပါ
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # တူးလ်ရလဒ်တွေနဲ့ အဆုံးသတ်တုံ့ပြန်ချက်ကို ရယူပါ
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### few-shot ကိရိယာခေါ်သော နမူနာများ

`input` တွင် few-shot ကိရိယာခေါ်မှု နမူနာများပေးသောအခါ `function_call` နှင့် `function_call_output` ပစ္စည်းများကိုအသုံးပြုပါ။ ID များသည် `fc_` ဖြင့် စတင်ရမည်။

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
# တပ်ဆင်ပြီးသား ဝက်ဘ်ရှာဖွေမှု ဥပမာ
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## ပုံရိပ် ထည့်သွင်းခြင်း

ပုံရိပ်အကြောင်းအရာ အမျိုးအစားသည် `image_url` မှ `input_image` သို့ ပြောင်းလဲပြီး URL သည် nested object မှ flat string သို့ ပြောင်းလဲသည်။

### ပုံရိပ်ထည့်သွင်းခြင်း — မတိုင်မီ (Chat Completions)
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

### ပုံရိပ်ထည့်သွင်းခြင်း — ပြီးနောက် (Responses API, URL)
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

### ပုံရိပ်ထည့်သွင်းခြင်း — ပြီးနောက် (Responses API, base64)
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

> **အဓိကပြောင်းလဲချက်များ**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (nested object) → `"image_url": "..."` (flat string — HTTPS URL သို့မဟုတ် `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) ရှေ့ပြောင်းမှု

**MAF ဗားရှင်းကို ပထမဦးစွာစစ်ဆေးပါ** — ရှေ့ပြောင်းမှုသည် MAF 1.0.0+ သို့မဟုတ် pre-1.0.0 beta/rc ပေါ်မူတည်သည်။

စစ်ဆေးရန်: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ တွင် `OpenAIChatClient` သည် **ပြီးစီးပြီး Responses API ကို အသုံးပြုသည်** — ရှေ့ပြောင်းရန် မလိုပါ။

legacy `OpenAIChatCompletionClient` (`chat.completions.create` သုံးသော) ကို `OpenAIChatClient` ဖြင့် အစားထိုးပါ။

မတိုင်မီ:
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

ပြီးနောက်:
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

### MAF pre-1.0.0 (beta/rc ထုတ်ပြန်မှုများ)

pre-1.0.0 MAF တွင် `OpenAIChatClient` သည် Chat Completions ကို သုံးသည်။ `agent-framework-openai>=1.0.0` သို့ အဆင့်မြှင့်လိုက်ပါ၊ အဆိုပါ `OpenAIChatClient` သည် Responses API ကို မူရင်းအနေဖြင့် အသုံးပြုသည်။

> **မှတ်ချက်**: `Agent`၊ `MCPStreamableHTTPTool` နှင့် အခြား MAF API များသည် မပြောင်းလဲသေးပါ — client class import နှင့် သတ်မှတ်ခြင်းများသာ ပြောင်းပါသည်။

## LangChain (`langchain-openai`) ရှေ့ပြောင်းမှု

`ChatOpenAI()` တွင် `use_responses_api=True` ဖြည့်ပါ။ စာတမ်းရောင်းမက်ဆေ့ခ်ျများမှ `.content` ကို `.text` သို့ပြောင်းပါ။

မတိုင်မီ:
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

# ... ကိုယ်စားလှယ် ခေါ်ယူမှု ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

ပြီးနောက်:
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

# ... အေးဂျင့် ဖုန်းခေါ်ခြင်း ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **အဓိကပြောင်းလဲချက်များ**: (1) constructor တွင် `use_responses_api=True`, (2) မက်ဆေ့ချ်များတွင် `.content` → `.text` ပြောင်းမှု။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->