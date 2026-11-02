# Responses API چیٹ شیٹ (Python + Azure OpenAI)

> ذیل میں تمام کوڈ کے ٹکڑے فرض کرتے ہیں کہ `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ہے اور `client` پہلے ہی initialize ہو چکا ہے (دیکھیں کلائنٹ سیٹ اپ)۔

## بنیادی درخواست
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## کلائنٹ سیٹ اپ — EntraID (تجویز کردہ)
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

## کلائنٹ سیٹ اپ — API کی
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## غیر ہم وقت کلائنٹ سیٹ اپ — EntraID
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

## غیر ہم وقت کلائنٹ سیٹ اپ — واضح ٹیننٹ کے ساتھ EntraID (کثیر ٹیننٹ)

جب Azure OpenAI ریسورس **مختلف ٹیننٹ** میں ہو بہ نسبت ڈیفالٹ کے، تو `tenant_id` کو بطور کریڈینشل واضح طور پر دیں۔ یہ عام طور پر ڈویلپمنٹ/ٹیسٹ منظرناموں میں ہوتا ہے جہاں ڈویلپر کا ہوم ٹیننٹ ریسورس ٹیننٹ سے مختلف ہوتا ہے۔

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# پروڈکشن کے لیے ManagedIdentityCredential (Azure Container Apps، App Service، وغیرہ)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # صارف کی طرف سے تفویض کردہ مینیجڈ شناخت
)
# مقامی ترقی کے لیے AzureDeveloperCliCredential — واضح tenant_id بہت اہم ہے
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# چین: پہلے منیجڈ شناخت آزماییں، پھر azd CLI کی طرف رجوع کریں
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## غیر ہم وقت کلائنٹ مائیگریشن — پہلے/بعد

پہلے (پرانی):
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

بعد:
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

## مکمل ہم وقت مائیگریشن — پہلے/بعد

پہلے (پرانا — Azure OpenAI Chat Completions):
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

بعد (Responses API — Azure OpenAI v1 endpoint):
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

## اسٹریمنگ (ہم وقت)
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
        print()  # آخر میں نیا لائن
```

## اسٹریمنگ (غیر ہم وقت)
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

## ویب ایپ اسٹریمنگ — بیک اینڈ سے فرنٹ اینڈ کی صورت

جب ایک ویب ایپ کو مائیگریٹ کریں جو SSE/JSONL اسٹریمنگ فرنٹ اینڈ کو کرتی ہے، **بیک اینڈ سیریلائزیشن فارمیٹ** تبدیل ہوتا ہے۔ نئے بیک اینڈ آؤٹ پٹ کو فرنٹ اینڈ کے موجودہ طریقوں کو برقرار رکھنے کے لیے ڈیزائن کریں تاکہ فرنٹ اینڈ میں کوئی تبدیلی نہ کرنی پڑے۔

**پہلے** — Chat Completions بیک اینڈ عام طور پر ہر چنک کے `choices[0]` ڈکشنری کو سیریلائز کرتا تھا:
```python
# پرانا: ہر چنک کے لیے مکمل انتخابی ڈکشنری کی ترتیب دی گئی شکل
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
فرنٹ اینڈ پڑھتا ہے: `response.delta.content` (choice آبجیکٹ کا گہرا راستہ)۔

**بعد** — Responses API بیک اینڈ ایک حد سے کم شکل فراہم کرتا ہے جو فرنٹ اینڈ رسائی کے راستے کو برقرار رکھتا ہے:
```python
# نیا: صرف وہی خارج کریں جس کی فرنٹ اینڈ کو ضرورت ہو
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
فرنٹ اینڈ اب بھی `response.delta.content` پڑھتا ہے — **فرنٹ اینڈ میں کوئی تبدیلی نہیں چاہیے**۔

> **اہم بات**: Responses API اسٹریمنگ شکل (`event.type` + `event.delta`) بنیادی طور پر Chat Completions (`chunk.choices[0].delta.content`) سے مختلف ہے۔ لیکن آپ کا بیک اینڈ سے فرنٹ اینڈ تک کا معاہدہ آپ خود طے کرتے ہیں۔ بیک اینڈ آؤٹ پٹ کو فرنٹ اینڈ کی توقعات کے مطابق شکل دیں۔

## اسٹریمنگ ایونٹ کی ترتیب

جب `stream: true` ہو، API یہ ایونٹس درج ذیل ترتیب میں بھیجتا ہے:
1. `response.created` – جواب آبجیکٹ initialized ہوا
2. `response.in_progress` – جنریشن شروع ہوا
3. `response.output_item.added` – آؤٹ پٹ آئٹم بنایا گیا
4. `response.content_part.added` – مواد کا حصہ شروع ہوا
5. `response.output_text.delta` – متن کے ٹکڑے (کئی، ہر ایک کے ساتھ `delta: string`)
6. `response.output_text.done` – متن کی تیاری ختم ہوئی
7. `response.content_part.done` – مواد کا حصہ مکمل ہوا
8. `response.output_item.done` – آؤٹ پٹ آئٹم مکمل ہوا
9. `response.completed` – مکمل جواب مکمل ہوا

بنیادی متن کی اسٹریمنگ کے لیے، صرف `response.output_text.delta` (متن کے ٹکڑے) اور `response.completed` (ختم) کو ہینڈل کریں۔

## ویب ایپس میں اسٹریمنگ ایرر ہینڈلنگ

جب ویب ایپ میں اسٹریمنگ ہو رہی ہو، غیر ہم وقت تکرار کو `try/except` میں لپیٹیں اور ایررز کو JSON کے طور پر جاری کریں تاکہ فرنٹ اینڈ انہیں مناسب طریقے سے دکھا سکے (مثلاً ریٹ لیمٹس، عبوری ناکامیاں):

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

> **کیوں اہم ہے**: Azure OpenAI ریٹ لیمٹ ہونے پر `429 Too Many Requests` واپس کرتا ہے۔ بغیر `try/except` کے، اسٹریمنگ جواب خاموشی سے ختم ہو جاتا ہے۔ `try/except` کے ساتھ، فرنٹ اینڈ کو `{"error": "Too Many Requests"}` ملتا ہے اور وہ ریٹری پرامپٹ دکھا سکتا ہے۔

## اسٹریمنگ ایونٹ کی اقسام (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## گفتگو کا فارمیٹ
```python
# Responses API ان پٹ ارے کے ذریعے مکالمے کا فارمیٹ سپورٹ کرتا ہے
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

## مواد فلٹر ایرر ہینڈلنگ

ایرر باڈی کی ساخت Chat Completions سے Responses API میں بدل گئی ہے۔

پہلے (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

بعد (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

اہم اختلافات:
- `innererror` لفافہ **غائب** ہے — مواد فلٹر کی تفصیلات اب `error.body` کی سب سے اوپر سطح پر ہیں۔
- `content_filter_result` (واحد) سے → `content_filters` (جمع آرے) جو ہر اندراج میں `content_filter_results` (جمع) رکھتا ہے۔
- `content_filters` کے ہر اندراج میں `blocked`, `source_type`, اور `content_filter_results` شامل ہوتے ہیں جن میں ہر قسم کی تفصیلات (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) ہوتی ہیں۔

Responses API کا مکمل مواد فلٹر ایرر باڈی کا خاکہ:
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

## را HTTP مائیگریشن (requests/httpx)

اگر ایپ Azure OpenAI REST کو براہ راست کال کرتی ہے بجائے SDK کے:

پہلے (Chat Completions):
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

بعد (Responses API):
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

> **نوٹ**: `output_text` Python SDK کے `Response` آبجیکٹ کی سہولت کی پراپرٹی ہے۔ RAW REST JSON جواب میں `output_text` کی سطح پر فیلڈ نہیں ہوتی — متن `output[0].content[0].text` پر ہوتا ہے۔

## کثیر مرحلہ (Multi-turn) گفتگو
```python
# گفتگو Responses API کے ساتھ بنائیں
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# گفتگو میں معاون کا جواب شامل کریں
messages.append({"role": "assistant", "content": response.output_text})

# گفتگو جاری رکھیں
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

مواد کی نوعیت کے ساتھ کثیر مرحلہ (واضح `input_text` / `output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` کے ذریعے کثیر مرحلہ (متبادل)

بجائے خود بات چیت کی فہرست کو سنبھالنے کے، آپ سرور سائڈ پر `previous_response_id` کا استعمال کرتے ہوئے جوابات کا سلسلہ بنا سکتے ہیں۔ API ہر جواب کو محفوظ کرتا ہے اور خودکار طور پر پچھلے ٹرنز کو پہلے شامل کرتا ہے۔



```python
# پہلا موڑ
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# اگلے موڑ — بس نیا صارف پیغام + پچھلے جواب کا شناختی نمبر بھیجیں
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**کب کونسا استعمال کریں:**

| طریقہ کار | فائدے | نقصانات |
|---|---|---|
| `input` آرے (دستی) | تاریخ پر مکمل کنٹرول؛ تراشنے/خلاصہ کرنے کی صلاحیت؛ سرور سائڈ اسٹوریج کی ضرورت نہیں (`store=False`) | مزید کوڈ؛ آپ آرے کو سنبھالتے ہیں |
| `previous_response_id` | آسان کوڈ؛ خودکار سلسلہ بندی | `store=True` درکار ہے (ڈیفالٹ)؛ گفتگو سرور سائڈ محفوظ ہوتی ہے؛ ٹرنز کے درمیان تاریخ تبدیل نہیں کی جا سکتی |

> **مائیگریشن کی اطلاع:** زیادہ تر Chat Completions ایپس پہلے ہی اپنی میسج آرے کو خود سنبھالتے ہیں، تو `input` آرے میں تبدیل ہونا زیادہ براہ راست 1:1 مائیگریشن ہے۔ نیا کوڈ یا جب آپ کو گفتگو کی تاریخ کو تبدیل کرنے کی ضرورت نہ ہو، تب `previous_response_id` استعمال کریں۔

## O-سیریز استدلال ماڈلز (o1, o3-mini, o3, o4-mini)

O-سیریز ماڈلز کے پاس Responses API کی طرف مائیگریٹ کرتے وقت منفرد پیرا میٹر پابندیاں ہوتی ہیں۔

### O-سیریز کے لیے پیرا میٹر میپنگ

| Chat Completions (o-سیریز) | Responses API | نوٹس |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | زیادہ مقرر کریں (4096+) — استدلال ٹوکنز حد میں شمار ہوتے ہیں |
| `reasoning_effort` | `reasoning.effort` | موجود ہو تو ویسا ہی رکھیں (low/medium/high) |
| `temperature` | ہٹا دیں یا `1` پر سیٹ کریں | O-سیریز صرف `1` قبول کرتا ہے |
| `top_p` | ہٹا دیں | O-سیریز میں سپورٹ نہیں ہے |
| `seed` | ہٹا دیں | Responses API میں سپورٹ نہیں ہے |

### O-سیریز پہلے/بعد

پہلے (Chat Completions کے ساتھ o-سیریز):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

بعد (Responses API):
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

> **نوٹ**: O-سیریز ماڈلز استدلال کے دوران متن ڈیلٹاز جاری کرنے سے پہلے آؤٹ پٹ بفر کر سکتے ہیں۔ اسٹریمنگ کام کرتی رہتی ہے مگر پہلی `response.output_text.delta` ایونٹ GPT ماڈلز کے مقابلے میں دیر سے آ سکتی ہے۔

## استدلال ٹوکنز تک رسائی
```python
# منطق کے ماڈلز داخلی منطق استعمال کرتے ہیں — آپ دیکھ سکتے ہیں کہ کتنے منطق کے ٹوکن استعمال ہوئے
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

> **اہم**: استدلال ماڈلز کے اندرونی استدلال کے عمل کو مدنظر رکھتے ہوئے `max_output_tokens=1000` (نہ کہ 50–200) استعمال کریں۔ ماڈل آخری آؤٹ پٹ بنانے سے پہلے داخلی طور پر استدلال ٹوکنز استعمال کرتا ہے۔

## منظم آؤٹ پٹ — JSON اسکیمہ
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

## ٹول کا استعمال

- `tools` میں فنکشنز کو **فلیٹ Responses API فارمیٹ** میں تعریف کریں — `name`, `description`, اور `parameters` سب ٹاپ لیول پر ہوں (نہ کہ `function` کے اندر)۔
- جب ماڈل ٹول کال کرنے کو کہے، اسے اپنی ایپ میں execute کریں اور اگلی درخواست میں ٹول کے نتیجے کو `function_call_output` آئٹم کے طور پر `input` کے اندر شامل کریں۔
- اسکیمے مختصر رکھیں؛ execution سے پہلے انپٹس کی تصدیق کریں۔
- `strict: true` استعمال کرتے وقت، تمام پراپرٹیز `required` میں شامل ہونی چاہئیں اور `additionalProperties: false` لازمی ہے۔

> **⚠️ `pydantic_function_tool()` مطابقت نہیں رکھتا**: `openai.pydantic_function_tool()` ابھی بھی پرانا Chat Completions نیسٹڈ فارمیٹ جنریٹ کرتا ہے (`{"type": "function", "function": {"name": ...}}`)۔ اسے `responses.create()` کے ساتھ استعمال نہ کریں۔ ٹول اسکیمے خود دستی طور پر تعریف کریں یا آؤٹ پٹ کو فلیٹ کرنے کے لیے ریپر لکھیں۔

### ٹول تعریف کا فارمیٹ

Responses API ایک **فلیٹ** ٹول فارمیٹ استعمال کرتا ہے — `name`, `description`, `parameters` ٹاپ لیول کیز ہیں (نہ کہ `function` کے اندر)۔

**پہلے (Chat Completions — نیسٹڈ):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**بعد (Responses API — فلیٹ):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

مکمل مثال:
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

`strict: true` (اسکیمہ نفاذ) کے ساتھ:
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
            "required": ["city_name"],       # تمام خصوصیات کو فہرست میں شامل کرنا ضروری ہے
            "additionalProperties": False,   # سخت موڈ کے لیے ضروری ہے
        },
    }
]
```

### ٹول کال راؤنڈ ٹرپ (عمل درآمد اور نتائج واپس کرنا)

جب ماڈل ٹول کال کی درخواست کرے، `response.output` آئٹمز + `function_call_output` استعمال کریں — **نہ کہ** Chat Completions کے `role: assistant` + `role: tool` پیٹرن۔

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
    # ماڈل کے function_call آئٹمز کو گفتگو میں شامل کریں
    messages.extend(response.output)

    # ہر ٹول کو چلائیں اور نتائج شامل کریں
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # ٹول کے نتائج کے ساتھ آخری جواب حاصل کریں
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### چند مثالیں ٹول کال کی

جب `input` میں ٹول کالز کی چند مثالیں دیں، `function_call` اور `function_call_output` آئٹمز استعمال کریں۔ IDs کو `fc_` سے شروع ہونا چاہیے۔

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
# سرکردہ ویب تلاش کی مثال
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## تصویر انپٹ

تصویر کی مواد کی اشیاء کی قسم `image_url` سے بدل کر `input_image` ہو گئی ہے، اور URL nested object سے فلیٹ سٹرنگ میں تبدیل ہو گیا ہے۔

### تصویر انپٹ — پہلے (Chat Completions)
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

### تصویر انپٹ — بعد (Responses API، URL)
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

### تصویر انپٹ — بعد (Responses API، base64)
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

> **اہم تبدیلیاں**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (nested object) → `"image_url": "..."` (فلیٹ سٹرنگ — HTTPS URL یا `data:image/...;base64,...` ڈیٹا URI), (3) `"type": "text"` → `"type": "input_text"`۔

## Microsoft Agent Framework (MAF) مائیگریشن

**پہلے اپنی MAF ورژن چیک کریں** — مائیگریشن اس بات پر منحصر ہے کہ آپ MAF 1.0.0+ پر ہیں یا pre-1.0.0 بیٹا/RC پر۔

چیک کرنے کے لیے: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ میں، `OpenAIChatClient` **پہلے ہی Responses API استعمال کرتا ہے** — مائیگریشن کی ضرورت نہیں۔

اگر کوڈبیس پرانا `OpenAIChatCompletionClient` استعمال کرتا ہے (جو `chat.completions.create` استعمال کرتا ہے)، اسے `OpenAIChatClient` سے بدلیں:

پہلے:
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

بعد:
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

### MAF pre-1.0.0 (بیٹا/RC ریلیزز)

pre-1.0.0 MAF میں، `OpenAIChatClient` Chat Completions استعمال کرتا تھا۔ `agent-framework-openai>=1.0.0` پر اپ گریڈ کریں جہاں `OpenAIChatClient` ڈیفالٹ کے طور پر Responses API استعمال کرتا ہے۔

> **نوٹ**: `Agent`, `MCPStreamableHTTPTool`, اور دیگر MAF APIs ویسے ہی رہتے ہیں — صرف کلائنٹ کلاس امپورٹ اور انسٹینشی ایشن بدلتی ہے۔

## LangChain (`langchain-openai`) مائیگریشن

`ChatOpenAI()` میں `use_responses_api=True` شامل کریں۔ نیز میسج کنٹینٹ رسائی `.content` سے `.text` میں تبدیل کریں۔

پہلے:
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

# ... ایجنٹ کی کال ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

بعد:
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

# ... ایجنٹ کی کال ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **اہم تبدیلیاں**: (1) کنسٹرکٹر میں `use_responses_api=True`، (2) میسج ریسپانسز میں `.content` → `.text`۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->