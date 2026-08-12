# Responses API চিট শীট (পাইথন + আজুর ওপেনএআই)

> নিচের সব স্নিপেট ধরে নেয় যে `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` এবং `client` ইতোমধ্যেই ইনিশিয়ালাইজড (দেখুন ক্লায়েন্ট সেটআপ)।

## বেসিক রিকোয়েস্ট
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## ক্লায়েন্ট সেটআপ — EntraID (প্রস্তাবিত)
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

## ক্লায়েন্ট সেটআপ — API কী
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## অ্যাসিঙ্ক ক্লায়েন্ট সেটআপ — EntraID
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

## অ্যাসিঙ্ক ক্লায়েন্ট সেটআপ — EntraID স্পষ্ট টেন্যান্ট সহ (মাল্টি-টেন্যান্ট)

যখন আজুর ওপেনএআই রিসোর্সটি ডিফল্ট থেকে **অন্য টেন্যান্টে** থাকে, তখন ক্রেডেনশিয়ালে `tenant_id` স্পষ্টভাবে পাস করুন। এটি ডেভ/টেস্ট পরিস্থিতিতে সাধারণ যেখানে ডেভেলপার এর হোম টেন্যান্ট রিসোর্স টেন্যান্ট থেকে আলাদা।

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# প্রোডাকশনের জন্য ManagedIdentityCredential (Azure Container Apps, App Service, ইত্যাদি)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # ব্যবহারকারী-নিযুক্ত পরিচালিত পরিচয়
)
# লোকাল ডেভের জন্য AzureDeveloperCliCredential — স্পষ্ট tenant_id অত্যন্ত গুরুত্বপূর্ণ
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# চেইন: প্রথমে managed identity চেষ্টা করুন, ব্যর্থ হলে azd CLI ব্যবহার করুন
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## অ্যাসিঙ্ক ক্লায়েন্ট মাইগ্রেশন — আগে/পরে

আগে (ডিপ্রিকেটেড):
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

পরে:
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

## ফুল সিনক মাইগ্রেশন — আগে/পরে

আগে (লিগ্যাসি — আজুর ওপেনএআই চ্যাট কমপ্লিশনস):
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

পরে (Responses API — আজুর ওপেনএআই v1 এন্ডপয়েন্ট):
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

## স্ট্রিমিং (সিনক)
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
        print()  # শেষ লাইনে নতুন লাইন
```

## স্ট্রিমিং (অ্যাসিঙ্ক)
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

## ওয়েব অ্যাপ স্ট্রিমিং — ব্যাকএন্ড-টু-ফ্রন্টএন্ড শেপ

যখন আপনি SSE/JSONL স্ট্রিম করে এমন একটি ওয়েব অ্যাপকে ফ্রন্টএন্ডে মাইগ্রেট করেন, তখন **ব্যাকএন্ড সিরিয়ালাইজেশন ফরম্যাট** পরিবর্তিত হয়। নতুন ব্যাকএন্ড আউটপুট এমনভাবে ডিজাইন করুন যাতে ফ্রন্টএন্ডের বিদ্যমান অ্যাক্সেস প্যাটার্নগুলি রক্ষা পাওয়া যায়, ফলে ফ্রন্টএন্ডে কোন পরিবর্তনের প্রয়োজন হয় না।

**আগে** — চ্যাট কমপ্লিশনস ব্যাকএন্ড সাধারণত প্রতিটি চাঙ্কের `choices[0]` ডিক্ট সিরিয়ালাইজ করত:
```python
# পুরানো: প্রতি চাঙ্কে সিরিয়ালাইজড পূর্ণ পছন্দ ডিক্ট
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend পড়ে: `response.delta.content` (চয়েস অবজেক্টে গভীর পথ)।

**পরে** — Responses API ব্যাকএন্ড একটি মিনিমাল শেপ প্রেরণ করে যা একই ফ্রন্টএন্ড অ্যাক্সেস পাথ সংরক্ষণ করে:
```python
# নতুন: শুধুমাত্র যা ফ্রন্টেন্ড প্রয়োজন তা প্রকাশ করুন
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend এখনও `response.delta.content` পড়ে — **কোনো ফ্রন্টএন্ড পরিবর্তনের প্রয়োজন নেই**।

> **মূল অন্তর্দৃষ্টি**: Responses API স্ট্রিমিং শেপ (`event.type` + `event.delta`) মূলত চ্যাট কমপ্লিশনস (`chunk.choices[0].delta.content`) থেকে ভিন্ন। কিন্তু আপনার ব্যাকএন্ড-টু-ফ্রন্টএন্ড চুক্তি আপনি নির্ধারণ করবেন। ব্যাকএন্ড আউটপুটকে ফ্রন্টএন্ডের প্রত্যাশিত আকারে গঠন করুন।

## স্ট্রিমিং ইভেন্ট সিকেনস

যখন `stream: true` থাকে, API এই ক্রমানুসারে ইভেন্ট প্রেরণ করে:
1. `response.created` – রেসপন্স অবজেক্ট initialized হচ্ছে
2. `response.in_progress` – জেনারেশন শুরু হয়েছে
3. `response.output_item.added` – আউটপুট আইটেম তৈরি হয়েছে
4. `response.content_part.added` – কন্টেন্ট পার্ট শুরু হয়েছে
5. `response.output_text.delta` – টেক্সট চাঙ্ক (বহু, প্রত্যেকের `delta: string` থাকে)
6. `response.output_text.done` – টেক্সট জেনারেশন শেষ হয়েছে
7. `response.content_part.done` – কন্টেন্ট পার্ট শেষ হয়েছে
8. `response.output_item.done` – আউটপুট আইটেম শেষ হয়েছে
9. `response.completed` – সম্পূর্ণ রেসপন্স সম্পন্ন

বেসিক টেক্সট স্ট্রিমিং এর জন্য, শুধু `response.output_text.delta` (টেক্সট চাঙ্কের জন্য) এবং `response.completed` (শেষের জন্য) হ্যান্ডেল করুন।

## ওয়েব অ্যাপে স্ট্রিমিং ত্রুটি হ্যান্ডলিং

ওয়েব অ্যাপে স্ট্রিমিং করার সময়, অ্যাসিঙ্ক ইটারেশনে `try/except` র‍্যাপ করুন এবং ত্রুটিগুলো JSON হিসেবে প্রদান করুন যাতে ফ্রন্টএন্ড সেগুলো সুশৃঙ্খলভাবে প্রদর্শন করতে পারে (যেমন, রেট লিমিট, স্থানচ্যুত ব্যর্থতা):

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


> **এই বিষয়টি গুরুত্বপূর্ণ কেন**: Azure OpenAI রেট সীমাবদ্ধতার সময় `429 Too Many Requests` ফেরত দেয়। `try/except` ছাড়া স্ট্রিমিং প্রতিক্রিয়া চুপচাপ মৃত্যু ঘটে। এটি থাকলে, ফ্রন্টএন্ড `{"error": "Too Many Requests"}` পায় এবং একটি পুনরায় চেষ্টা করার প্রম্পট দেখাতে পারে।

## স্ট্রিমিং ইভেন্ট প্রকার (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## কথোপকথনের ফরম্যাট
```python
# Responses API ইনপুট অ্যারের মাধ্যমে কথোপকথন ফর্ম্যাট সমর্থন করে
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

## কনটেন্ট ফিল্টার ত্রুটি পরিচালনা

ত্রুটি বডির কাঠামো Chat Completions থেকে Responses API তে পরিবর্তিত হয়েছে।

আগে (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

পরে (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

প্রধান পার্থক্য:
- `innererror` র‌্যাপার **অদৃশ্য** — কনটেন্ট ফিল্টার বিস্তারিত এখন `error.body` এর শীর্ষ স্তরে।
- `content_filter_result` (একবচন) → `content_filters` (বহুবচন অ্যারে) যার মধ্যে প্রত্যেক এন্ট্রিতে `content_filter_results` (বহুবচন) রয়েছে।
- `content_filters` এর প্রত্যেক এন্ট্রিতে `blocked`, `source_type` এবং ক্যাটাগরি অনুসারে বিস্তারিত `content_filter_results` (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) থাকে।

পূর্ণ Responses API কনটেন্ট ফিল্টার ত্রুটি বডির কাঠামো:
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

## র গুলো HTTP মাইগ্রেশন (requests/httpx)

যদি অ্যাপ সরাসরি Azure OpenAI REST কল করে SDK ব্যবহার না করে:

আগে (Chat Completions):
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

পরে (Responses API):
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

> **নোট**: `output_text` হল Python SDK এর `Response` অবজেক্টের একটি সুবিধাজনক প্রোপার্টি। কাঁচা REST JSON প্রতিক্রিয়াতে শীর্ষ স্তরে `output_text` ফিল্ড থাকে না — টেক্সট আছে `output[0].content[0].text` এ।

## মাল্টি-টার্ন কথোপকথন
```python
# Responses API দিয়ে একটি কথোপকথন তৈরি করুন
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# কথোপকথনে সহকারী এর উত্তর যোগ করুন
messages.append({"role": "assistant", "content": response.output_text})

# কথোপকথন চালিয়ে যান
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

বিষয়বস্তু-ভিত্তিক মাল্টি-টার্ন (স্পষ্ট `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` দিয়ে মাল্টি-টার্ন (বিকল্প)

কথোপকথনের অ্যারে নিজে পরিচালনা করার পরিবর্তে, আপনি সার্ভার-সাইডে `previous_response_id` ব্যবহার করে প্রতিক্রিয়া চেইন করতে পারেন। API প্রতিটি প্রতিক্রিয়া সংরক্ষণ করে এবং স্বয়ংক্রিয়ভাবে পূর্ববর্তী টার্নগুলো যোগ করে।



```python
# প্রথম পালা
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# পরবর্তী পালা — শুধুমাত্র নতুন ব্যবহারকারীর বার্তা + পূর্ববর্তী সাড়া আইডি পাঠান
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**কখন কোনটি ব্যবহার করবেন:**

| পদ্ধতি | সুবিধা | অসুবিধা |
|---|---|---|
| `input` অ্যারে (ম্যানুয়াল) | ইতিহাসের উপর পূর্ণ নিয়ন্ত্রণ; ট্রিম বা সংক্ষিপ্তকরণ সম্ভব; সার্ভার-সাইডে সংরক্ষণ প্রয়োজন নেই (`store=False`) | বেশি কোড; অ্যারে আপনি নিজেই পরিচালনা করবেন |
| `previous_response_id` | সহজ কোড; স্বয়ংক্রিয় চেইনিং | `store=True` (ডিফল্ট) প্রয়োজন; কথোপকথন সার্ভার-সাইডে সংরক্ষিত; টার্নের মাঝে ইতিহাস পরিবর্তন করা যায় না |

> **মাইগ্রেশন নোট:** অধিকাংশ Chat Completions অ্যাপ ইতিমধ্যে তাদের নিজস্ব মেসেজ অ্যারে পরিচালনা করে, তাই `input` অ্যারে ব্যবহার করে সরাসরি 1:1 মাইগ্রেশন করা সহজ। নতুন কোডে বা কথোপকথন ইতিহাস পরিবর্তন না করলে `previous_response_id` ব্যবহার করুন।

## O-সিরিজ রিজনিং মডেলস (o1, o3-mini, o3, o4-mini)

O-সিরিজ মডেলগুলির Responses API তে মাইগ্রেট করার সময় কিছু বিশেষ প্যারামিটার সীমাবদ্ধতা থাকে।

### o-সিরিজের জন্য প্যারামিটার ম্যাপিং

| Chat Completions (o-সিরিজ) | Responses API | মন্তব্য |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | উচ্চ সেট করুন (4096+) — যুক্তি টোকেন সীমার বিরুদ্ধে গণনা করে |
| `reasoning_effort` | `reasoning.effort` | উপস্থিত থাকলে যেমন আছে রাখুন (কম/মধ্যম/উচ্চ) |
| `temperature` | মুছে ফেলুন বা `1` এ সেট করুন | ও-সিরিজ শুধুমাত্র `1` গ্রহণ করে |
| `top_p` | মুছে ফেলুন | ও-সিরিজে সমর্থিত নয় |
| `seed` | মুছে ফেলুন | Responses API তে সমর্থিত নয় |

### ও-সিরিজ আগে/পরপর

আগে (চ্যাট কমপ্লিশনস ও-সিরিজের সাথে):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

পরে (Responses API):
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

> **নোট**: ও-সিরিজ মডেলগ্রী যুক্তির সময় আউটপুট বাফার করতে পারে লেখা ডেল্টা বের করার আগে। স্ট্রীমিং এখনও কাজ করে কিন্তু প্রথম `response.output_text.delta` ইভেন্টটি GPT মডেলগুলির তুলনায় দীর্ঘ বিলম্বে আসতে পারে।

## যুক্তি টোকেনে অ্যাক্সেস
```python
# যুক্তির মডেলগুলি অভ্যন্তরীণ যুক্তি ব্যবহার করে — আপনি দেখতে পারবেন কতগুলো যুক্তি টোকেন ব্যবহার করা হয়েছে
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

> **গুরুত্বপূর্ণ**: যুক্তি মডেলদের অভ্যন্তরীণ যুক্তি প্রক্রিয়াকে বিবেচনায় এনে `max_output_tokens=1000` (50–200 নয়) ব্যবহার করুন। মডেল চূড়ান্ত আউটপুট তৈরি করার আগে যুক্তি টোকেন অভ্যন্তরীন ভাবে ব্যবহার করে।

## গঠনমূলক আউটপুট — JSON Schema
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

## টুল ব্যবহার

- `tools` এ ফাংশনগুলো সংজ্ঞায়িত করুন **ফ্ল্যাট Responses API ফরম্যাট** অনুযায়ী — `name`, `description`, এবং `parameters` টপ-লেভেলে থাকতে হবে (যা `function` এর নিচে নয়)।
- যখন মডেল একটি টুল কল করতে বলে, তখন এটি আপনার অ্যাপে সম্পাদন করুন এবং পরবর্তী অনুরোধে `input` এর মধ্যে `function_call_output` আইটেম হিসেবে টুল ফলাফল অন্তর্ভুক্ত করুন।
- স্কিমা গুলো সংক্ষিপ্ত রাখুন; কার্যকর করার আগে ইনপুটগুলো যাচাই করুন।
- `strict: true` ব্যবহার করলে, সমস্ত প্রোপার্টি অবশ্যই `required` এ তালিকাভুক্ত থাকতে হবে এবং `additionalProperties: false` বাধ্যতামূলক।

> **⚠️ `pydantic_function_tool()` সহযোগী অমেলযোগ্য**: `openai.pydantic_function_tool()` সহযোগী এখনও পুরানো চ্যাট কমপ্লিশনস নেস্টেড ফরম্যাট (`{"type": "function", "function": {"name": ...}}`) তৈরি করে। এটি `responses.create()` সঙ্গে ব্যবহার করবেন না। নিজে হাতে টুল স্কিমা সংজ্ঞায়িত করুন বা আউটপুট ফ্ল্যাট করতে একটি র‍্যাপার লিখুন।

### টুল সংজ্ঞা ফরম্যাট

Responses API একটি **ফ্ল্যাট** টুল ফরম্যাট ব্যবহার করে — `name`, `description`, `parameters` হচ্ছে টপ-লেভেল কী (যা `function` এর নিচে নয়)।

**আগে (চ্যাট কমপ্লিশনস — নেস্টেড):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**পরে (Responses API — ফ্ল্যাট):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

সম্পূর্ণ উদাহরণ:
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

`strict: true` (স্কিমা কার্যকরকরণ) নিয়ে:
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
            "required": ["city_name"],       # সমস্ত বৈশিষ্ট্যগুলি তালিকাভুক্ত করা আবশ্যক
            "additionalProperties": False,   # কঠোর মোডের জন্য প্রয়োজনীয়
        },
    }
]
```

### টুল কল রাউন্ড-ট্রিপ (এক্সিকিউট এবং ফলাফল ফিরিয়ে দিন)

মডেল যখন একটি টুল কলের অনুরোধ করে, `response.output` আইটেম + `function_call_output` ব্যবহার করুন — **চ্যাট কমপ্লিশনসের** `role: assistant` + `role: tool` প্যাটার্ন নয়।

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
    # মডেলের function_call আইটেমগুলি কথোপকথনে যোগ করুন
    messages.extend(response.output)

    # প্রতিটি টুল চালান এবং ফলাফল যোগ করুন
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # টুলের ফলাফল নিয়ে চূড়ান্ত উত্তর পান
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### কয়েকটি-শট টুল কল উদাহরণ

যখন `input` এ কয়েকটি-শট টুল কলের উদাহরণ দেন, `function_call` এবং `function_call_output` আইটেম ব্যবহার করুন। আইডিগুলো অবশ্যই `fc_` দিয়ে শুরু হতে হবে।

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
# বিল্ট-ইন ওয়েব সার্চ উদাহরণ
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## ইমেজ ইনপুট

ইমেজ কনটেন্ট আইটেমের টাইপ `image_url` থেকে `input_image` এ পরিবর্তিত হয়েছে, এবং URL nested অবজেক্ট থেকে ফ্ল্যাট স্ট্রিং এ এসেছে।

### ইমেজ ইনপুট — আগে (চ্যাট কমপ্লিশনস)
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

### ইমেজ ইনপুট — পরে (Responses API, URL)
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

### ইমেজ ইনপুট — পরে (Responses API, base64)
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

> **মূল পরিবর্তন**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (nested অবজেক্ট) → `"image_url": "..."` (ফ্ল্যাট স্ট্রিং — HTTPS URL বা `data:image/...;base64,...` ডাটা URI হতে পারে), (3) `"type": "text"` → `"type": "input_text"`.

## মাইক্রোসফট এজেন্ট ফ্রেমওয়ার্ক (MAF) মাইগ্রেশন

**আপনার MAF ভার্সন প্রথমে নিশ্চিত করুন** — মাইগ্রেশন নির্ভর করে আপনি MAF 1.0.0+ এ আছেন কিনা অথবা পূর্ব-1.0.0 বেটা/আরসি তে।

যাচাই করতে: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ তে, `OpenAIChatClient` **আগেই Responses API ব্যবহার করে** — কোনো মাইগ্রেশন দরকার নেই।

যদি কোডবেস পুরাতন `OpenAIChatCompletionClient` (যে `chat.completions.create` ব্যবহার করে) ব্যবহার করে, তাহলে এটি `OpenAIChatClient` দিয়ে প্রতিস্থাপন করুন:

আগে:
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

পরে:
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

### MAF পূর্ব-1.0.0 (বেটা/আরসি রিলিজ)

পূর্ব-1.0.0 MAF তে `OpenAIChatClient` চ্যাট কমপ্লিশনস ব্যবহার করত। `agent-framework-openai>=1.0.0` আপগ্রেড করুন যেখানে `OpenAIChatClient` ডিফল্টরূপে Responses API ব্যবহার করে।

> **নোট**: `Agent`, `MCPStreamableHTTPTool`, এবং অন্যান্য MAF API অপরিবর্তিত থাকে — কেবল ক্লায়েন্ট ক্লাস ইম্পোর্ট এবং ইনস্ট্যান্সিয়েশন পরিবর্তিত হয়।

## LangChain (`langchain-openai`) মাইগ্রেশন

`ChatOpenAI()` তে `use_responses_api=True` যোগ করুন। এছাড়াও মেসেজ কনটেন্ট অ্যাক্সেস `.content` থেকে `.text` এ আপডেট করুন।

আগে:
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

# ... এজেন্ট আহ্বান ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

পরে:
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

# ... এজেন্ট আহ্বান ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **মূল পরিবর্তন**: (1) কনস্ট্রাক্টরে `use_responses_api=True`, (2) রেসপন্স মেসেজে `.content` → `.text`।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->