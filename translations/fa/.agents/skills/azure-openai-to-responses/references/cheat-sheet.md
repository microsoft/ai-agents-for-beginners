# راهنمای سریع API پاسخ‌ها (پایتون + آژور OpenAI)

> همه کدهای نمونه زیر فرض می‌کنند `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` است و `client` قبلاً مقداردهی اولیه شده (به تنظیمات کلاینت مراجعه کنید).

## درخواست پایه
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## تنظیم کلاینت — EntraID (توصیه‌شده)
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

## تنظیم کلاینت — کلید API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## تنظیم کلاینت غیرهمزمان — EntraID
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

## تنظیم کلاینت غیرهمزمان — EntraID با مستأجر صریح (چند مستأجری)

هنگامی که منبع Azure OpenAI در **مستأجر متفاوتی** نسبت به پیش‌فرض قرار دارد، `tenant_id` را به‌صورت صریح به مدرک (credential) ارسال کنید. این در سناریوهای توسعه/آزمایش که مستأجر خانگی توسعه‌دهنده با مستأجر منبع متفاوت است، رایج است.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential برای محیط تولید (Azure Container Apps، App Service و غیره)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # شناسه مدیریت شده اختصاص یافته به کاربر
)
# AzureDeveloperCliCredential برای توسعه محلی — شناسه tenant_id صریح بسیار مهم است
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# زنجیره: ابتدا تلاش برای استفاده از شناسه مدیریت شده، در صورت عدم موفقیت به azd CLI بازگردد
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## مهاجرت کلاینت غیرهمزمان — قبل/بعد

قبل (منسوخ شده):
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

## مهاجرت کامل همزمان — قبل/بعد

قبل (قدیمی — تکمیل‌های گفتگویی Azure OpenAI):
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

بعد (API پاسخ‌ها — نقطه انتهایی Azure OpenAI v1):
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

## پخش زنده (همزمان)
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
        print()  # خط جدید در پایان
```

## پخش زنده (غیرهمزمان)
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

## پخش زنده برنامه وب — شکل بک‌اند به فرانت‌اند

هنگام مهاجرت برنامه وبی که SSE/JSONL را به فرانت‌اند پخش می‌کند، **فرمت سریالی‌سازی بک‌اند** تغییر می‌کند. خروجی جدید بک‌اند را به‌گونه‌ای طراحی کنید که الگوهای دسترسی فرانت‌اند را حفظ کند تا نیازی به تغییر در فرانت‌اند نباشد.

**قبل** — بک‌اند تکمیل‌های گفتگویی معمولاً دیکشنری `choices[0]` هر بخش را سریالی‌سازی می‌کرد:
```python
# قدیمی: دیکشنری کامل انتخاب سریالی شده برای هر قطعه
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
 خواندن فرانت‌اند: `response.delta.content` (مسیر عمیق به داخل شیء انتخاب).

**بعد** — بک‌اند API پاسخ‌ها شکل مینیمالی تولید می‌کند که مسیر دسترسی فرانت‌اند را حفظ می‌کند:
```python
# جدید: تنها آنچه که رابط کاربری نیاز دارد را ارسال کنید
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
 فرانت‌اند هنوز `response.delta.content` را می‌خواند — **نیازی به تغییر در فرانت‌اند نیست**.

> **نکته کلیدی**: شکل پخش زنده API پاسخ‌ها (`event.type` + `event.delta`) بنیاداً متفاوت با تکمیل‌های گفتگویی (`chunk.choices[0].delta.content`) است. اما قرارداد بک‌اند به فرانت‌اند بر عهده شماست. خروجی بک‌اند را به‌گونه‌ای شکل دهید که با انتظار فرانت‌اند مطابقت داشته باشد.

## توالی رویدادهای پخش زنده

وقتی `stream: true` است، API رویدادها را به این ترتیب ارسال می‌کند:
1. `response.created` – شیء پاسخ مقداردهی اولیه شد
2. `response.in_progress` – تولید آغاز شد
3. `response.output_item.added` – آیتم خروجی ایجاد شد
4. `response.content_part.added` – بخش محتوا شروع شد
5. `response.output_text.delta` – بخش‌های متنی (چندگانه، هر کدام شامل `delta: string`)
6. `response.output_text.done` – تولید متن تمام شد
7. `response.content_part.done` – بخش محتوا تمام شد
8. `response.output_item.done` – آیتم خروجی تمام شد
9. `response.completed` – پاسخ کامل شد

برای پخش متن پایه، فقط `response.output_text.delta` (بخش‌های متن) و `response.completed` (برای پایان) را پردازش کنید.

## مدیریت خطا در پخش زنده برنامه‌های وب

هنگام پخش غیرهمزمان در برنامه وب، حلقه غیرهمزمان را در `try/except` قرار دهید و خطاها را به‌صورت JSON برگردانید تا فرانت‌اند بتواند آن‌ها را به‌خوبی نمایش دهد (مثلاً محدودیت نرخ، خطاهای موقتی):

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

> **چرا این مهم است**: Azure OpenAI هنگام محدودیت نرخ، `429 Too Many Requests` را برمی‌گرداند. بدون `try/except` پاسخ پخش زنده به‌صورت خاموش خاتمه می‌یابد. با آن، فرانت‌اند `{"error": "Too Many Requests"}` را دریافت می‌کند و می‌تواند پیام تلاش مجدد نشان دهد.

## نوع‌های رویداد پخش زنده (کتابخانه پایتون)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`، `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`، `response: Response`

## فرمت گفت‌وگو
```python
# API پاسخ‌ها از قالب مکالمه از طریق آرایه ورودی پشتیبانی می‌کند
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

## مدیریت خطا فیلتر محتوا

ساختار بدنه خطا از تکمیل‌های گفتگویی به API پاسخ‌ها تغییر کرده است.

قبل (تکمیل‌های گفتگویی):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

بعد (API پاسخ‌ها):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

تفاوت‌های کلیدی:
- بسته‌بندی `innererror` **حذف شده** — جزئیات فیلتر محتوا اکنون در سطح بالای `error.body` هستند.
- `content_filter_result` (مفرد) → `content_filters` (آرایه جمع) شامل `content_filter_results` (جمع) در هر ورودی.
- هر ورودی در `content_filters` شامل `blocked`، `source_type`، و `content_filter_results` با جزئیات دسته‌ای (`jailbreak`، `hate`، `sexual`، `violence`، `self_harm`) است.

شکل کامل بدنه خطای فیلتر محتوای API پاسخ‌ها:
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

## مهاجرت HTTP خام (requests/httpx)

اگر برنامه به‌طور مستقیم به REST آژور OpenAI به‌جای استفاده از SDK فراخوانی می‌کند:

قبل (تکمیل‌های گفتگویی):
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

بعد (API پاسخ‌ها):
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

> **توجه**: `output_text` یک خصوصیت راحت در شیء `Response` کتابخانه پایتون است. پاسخ JSON خام REST فیلد سطح بالای `output_text` ندارد — متن در `output[0].content[0].text` قرار دارد.

## گفت‌وگوی چند دور
```python
# ساخت یک گفتگو با استفاده از Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# افزودن پاسخ دستیار به گفتگو
messages.append({"role": "assistant", "content": response.output_text})

# ادامه دادن گفتگو
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

گفت‌وگوی چند دور با نوع محتوا (صریح `input_text` / `output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### گفت‌وگوی چند دور از طریق `previous_response_id` (جایگزین)

به جای مدیریت آرایه گفت‌وگو به‌صورت دستی، می‌توانید پاسخ‌ها را
سمت سرور با استفاده از `previous_response_id` زنجیره کنید. API هر پاسخ را ذخیره کرده و
به‌طور خودکار دورهای قبلی را پیش‌فرض می‌کند.

```python
# گردش اول
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# گردش‌های بعدی — فقط پیام جدید کاربر + شناسه پاسخ قبلی را ارسال کنید
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**چه زمانی کدام را استفاده کنیم:**

| رویکرد | مزایا | معایب |
|---|---|---|
| آرایه `input` (دستی) | کنترل کامل روی تاریخچه؛ امکان اصلاح/خلاصه‌سازی؛ نیازی به ذخیره سمت سرور نیست (`store=False`) | کد بیشتر؛ مدیریت آرایه با شماست |
| `previous_response_id` | کد ساده‌تر؛ زنجیره خودکار | نیازمند `store=True` (پیش‌فرض)؛ گفت‌وگو سمت سرور ذخیره می‌شود؛ نمی‌توان بین دورها تاریخچه را تغییر داد |

> **یادداشت مهاجرت:** بیشتر برنامه‌های تکمیل گفتگویی آرایه پیام خود را مدیریت می‌کنند، بنابراین تبدیل به آرایه `input` مهاجرت مستقیم 1:1 است. از `previous_response_id` برای کد جدید یا زمانی که نیازی به دستکاری تاریخچه گفت‌وگو ندارید استفاده کنید.

## مدل‌های استدلال سری O (o1، o3-mini، o3، o4-mini)

مدل‌های سری O هنگام مهاجرت به API پاسخ‌ها محدودیت‌های پارامتری منحصر به فردی دارند.

### نگاشت پارامتر برای سری O

| تکمیل‌های گفتگویی (سری O) | API پاسخ‌ها | یادداشت‌ها |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | تنظیم مقدار بالا (۴۰۹۶+) — توکن‌های استدلالی بر محدودیت شمارش می‌شوند |
| `reasoning_effort` | `reasoning.effort` | اگر وجود دارد بدون تغییر نگه دارید (کم/متوسط/زیاد) |
| `temperature` | حذف یا مقدار `1` را قرار دهید | سری O تنها `1` را می‌پذیرد |
| `top_p` | حذف | در سری o پشتیبانی نمی‌شود |
| `seed` | حذف | در API پاسخ‌ها پشتیبانی نمی‌شود |

### سری O قبل/بعد

قبل (Chat Completions با سری o):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

بعد (API پاسخ‌ها):
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

> **توجه**: مدل‌های سری O ممکن است خروجی را در حین استدلال بافر کنند پیش از آنکه دلتاهای متنی را ارسال کنند. پخش جریان هنوز کار می‌کند اما اولین رویداد `response.output_text.delta` ممکن است با تأخیر بیشتری نسبت به مدل‌های GPT برسد.

## دسترسی به توکن‌های استدلالی
```python
# مدل‌های استدلال از استدلال داخلی استفاده می‌کنند — شما می‌توانید ببینید چه تعداد توکن استدلال استفاده شده است
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

> **مهم**: از `max_output_tokens=1000` استفاده کنید (نه ۵۰–۲۰۰) تا فرایند استدلال داخلی مدل‌های reasoning لحاظ شود. مدل قبل از تولید خروجی نهایی از توکن‌های استدلالی به‌صورت داخلی استفاده می‌کند.

## خروجی ساختاریافته — طرح JSON
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

## استفاده از ابزار

- توابع را در `tools` با فرمت **مسطح API پاسخ‌ها** تعریف کنید — کلیدهای `name`، `description`، و `parameters` در سطح بالا باشند (نه به صورت تو در تو در زیر `function`).
- وقتی مدل درخواست استفاده از یک ابزار می‌کند، آن را در اپ خود اجرا و نتیجه ابزار را در درخواست بعدی به صورت آیتم `function_call_output` درون `input` درج کنید.
- طرح‌ها را حداقلی نگه دارید؛ ورودی‌ها را قبل از اجرا اعتبارسنجی کنید.
- وقتی از `strict: true` استفاده می‌کنید، همه ویژگی‌ها باید در `required` ذکر شده و `additionalProperties: false` الزامی است.

> **⚠️ `pydantic_function_tool()` ناسازگار است**: کمکی `openai.pydantic_function_tool()` هنوز فرمت تو در توی قدیمی Chat Completions را تولید می‌کند (`{"type": "function", "function": {"name": ...}}`). آن را با `responses.create()` استفاده نکنید. طرح‌های ابزاری را دستی تعریف کنید یا یک لفاف برای مسطح‌سازی خروجی بنویسید.

### فرمت تعریف ابزار

API پاسخ‌ها از فرمت ابزاری **مسطح** استفاده می‌کند — کلیدهای `name`، `description`، `parameters` در سطح بالا هستند (نه به صورت تو در تو زیر `function`).

**قبل (Chat Completions — تو در تو):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**بعد (API پاسخ‌ها — مسطح):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

مثال کامل:
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

با `strict: true` (اجباری‌سازی طرح):
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
            "required": ["city_name"],       # تمام ویژگی‌ها باید فهرست شوند
            "additionalProperties": False,   # مورد نیاز برای حالت سخت‌گیرانه
        },
    }
]
```

### گردش تماس ابزار (اجرا و بازگرداندن نتایج)

وقتی مدل درخواست تماس ابزاری می‌دهد، از آیتم‌های `response.output` به همراه `function_call_output` استفاده کنید — **نه** الگوی نقش در Chat Completions با `role: assistant` و `role: tool`.

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
    # افزودن آیتم‌های function_call مدل به مکالمه
    messages.extend(response.output)

    # اجرای هر ابزار و اضافه کردن نتایج
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # دریافت پاسخ نهایی با نتایج ابزارها
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### چند مثال تماس ابزار با نمونه‌های محدود

هنگام ارائه نمونه‌های کم‌شات تماس ابزار در `input`، از آیتم‌های `function_call` و `function_call_output` استفاده کنید. شناسه‌ها باید با `fc_` شروع شوند.

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
# نمونه جستجوی وب داخلی
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## ورودی تصویر

آیتم‌های محتوای تصویر نوع خود را از `image_url` به `input_image` تغییر می‌دهند، و URL از یک شیء تو در تو به رشته مسطح تبدیل می‌شود.

### ورودی تصویر — قبل (Chat Completions)
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

### ورودی تصویر — بعد (API پاسخ‌ها، URL)
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

### ورودی تصویر — بعد (API پاسخ‌ها، base64)
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

> **تغییرات کلیدی**: (1) `"type": "image_url"` → `"type": "input_image"`، (۲) `"image_url": {"url": "..."}` (شیء تو در تو) → `"image_url": "..."` (رشته مسطح — یا URL HTTPS یا URI داده `data:image/...;base64,...`)، (۳) `"type": "text"` → `"type": "input_text"`.

## مهاجرت چارچوب عامل مایکروسافت (MAF)

**ابتدا نسخه MAF خود را بررسی کنید** — مهاجرت بستگی دارد که آیا از MAF 1.0.0+ استفاده می‌کنید یا نسخه بتا/RC پیشین.

برای بررسی: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

در MAF 1.0.0+، `OpenAIChatClient` **در حال حاضر از API پاسخ‌ها استفاده می‌کند** — نیازی به مهاجرت نیست.

اگر کد شما از `OpenAIChatCompletionClient` قدیمی (که `chat.completions.create` استفاده می‌کند) بهره می‌برد، آن را با `OpenAIChatClient` جایگزین کنید:

قبل:
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

### MAF قبل از ۱.۰.۰ (نسخه‌های بتا/RC)

در MAF پیش از ۱.۰.۰، `OpenAIChatClient` از Chat Completions استفاده می‌کرد. به `agent-framework-openai>=1.0.0` ارتقا دهید که به صورت پیشفرض از API پاسخ‌ها استفاده می‌کند.

> **توجه**: کلاس‌های API `Agent`، `MCPStreamableHTTPTool` و سایر موارد MAF تغییری نکرده‌اند — تنها وارد کردن و نمونه‌سازی کلاس کلاینت تغییر می‌کند.

## مهاجرت LangChain (`langchain-openai`)

به `ChatOpenAI()` پارامتر `use_responses_api=True` اضافه کنید. همچنین دسترسی به محتوای پیام‌ها را از `.content` به `.text` به‌روزرسانی کنید.

قبل:
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

# ... فراخوانی عامل ...
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

# ... فراخوانی عامل ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **تغییرات کلیدی**: (1) `use_responses_api=True` در سازنده، (2) `.content` → `.text` در پیام‌های پاسخ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->