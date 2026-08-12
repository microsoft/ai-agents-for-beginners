# ورقة غش لواجهة برمجة التطبيقات للاستجابات (Python + Azure OpenAI)

> جميع المقاطع أدناه تفترض `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` وأن العميل `client` مُهيأ بالفعل (انظر إعداد العميل).

## الطلب الأساسي
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## إعداد العميل — EntraID (موصى به)
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

## إعداد العميل — مفتاح API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## إعداد العميل غير المتزامن — EntraID
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

## إعداد العميل غير المتزامن — EntraID مع معرّف المستأجر صريح (متعدد المستأجرين)

عندما يكون مورد Azure OpenAI في **مستأجر مختلف** عن الافتراضي، قم بتمرير `tenant_id` صراحةً إلى بيانات الاعتماد. هذا شائع في سيناريوهات التطوير/الاختبار حيث يختلف مستأجر المطور الرئيسي عن مستأجر المورد.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential للإنتاج (تطبيقات حاوية أزور، خدمة التطبيقات، إلخ)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # هوية مُدارة مخصّصة للمستخدم
)
# AzureDeveloperCliCredential للتطوير المحلي — معرف المستأجر (tenant_id) الصريح أمر حاسم
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# السلسلة: جرب الهوية المُدارة أولاً، ثم العودة إلى azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## ترحيل العميل غير المتزامن — قبل/بعد

قبل (مهمل):
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

## ترحيل التزامن الكامل — قبل/بعد

قبل (قديم — إكمالات الدردشة لـ Azure OpenAI):
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

بعد (API الاستجابات — نقطة نهاية Azure OpenAI v1):
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

## البث (متزامن)
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
        print()  # سطر جديد في النهاية
```

## البث (غير متزامن)
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

## بث تطبيق الويب — شكل الواجهة الخلفية إلى الواجهة الأمامية

عند ترحيل تطبيق ويب يقوم ببث SSE/JSONL إلى الواجهة الأمامية، يتغير **تنسيق التسلسل في الواجهة الخلفية**. صمم مخرجات الواجهة الخلفية الجديدة للحفاظ على أنماط الوصول الموجودة في الواجهة الأمامية بحيث لا تحتاج الواجهة الأمامية إلى تغييرات.

**قبل** — عادةً ما كانت الواجهة الخلفية لإكمالات الدردشة تسلسل قاموس `choices[0]` لكل جزء:
```python
# قديم: قاموس اختيار كامل مسلسل لكل جزء
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
قراءة الواجهة الأمامية: `response.delta.content` (مسار عميق داخل كائن الخيار).

**بعد** — ترسل الواجهة الخلفية لواجهة برمجة التطبيقات للاستجابات شكلاً بسيطًا يحافظ على نفس مسار الوصول في الواجهة الأمامية:
```python
# جديد: إصدار فقط ما يحتاجه الواجهة الأمامية
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
لا تزال الواجهة الأمامية تقرأ `response.delta.content` — **لا تحتاج إلى أي تغييرات في الواجهة الأمامية**.

> **رؤية رئيسية**: شكل البث في API الاستجابات (`event.type` + `event.delta`) يختلف جوهريًا عن إكمالات الدردشة (`chunk.choices[0].delta.content`). لكن عقدتك بين الواجهة الخلفية والأمامية لك لتحددها. شكّل ناتج الواجهة الخلفية ليطابق ما تتوقعه الواجهة الأمامية بالفعل.

## تسلسل أحداث البث

عند `stream: true`، تصدر API الأحداث بهذا الترتيب:
1. `response.created` – تم تهيئة كائن الاستجابة
2. `response.in_progress` – بدأ التوليد
3. `response.output_item.added` – تم إنشاء عنصر المخرجات
4. `response.content_part.added` – بدأ جزء المحتوى
5. `response.output_text.delta` – كتل نصية (عدة، كل واحدة تحتوي على `delta: string`)
6. `response.output_text.done` – انتهى توليد النص
7. `response.content_part.done` – انتهى جزء المحتوى
8. `response.output_item.done` – انتهى عنصر المخرجات
9. `response.completed` – اكتملت الاستجابة بالكامل

للبث النصي الأساسي، تعامل فقط مع `response.output_text.delta` (للكتل النصية) و`response.completed` (للانتهاء).

## معالجة أخطاء البث في تطبيقات الويب

عند البث في تطبيق ويب، غلف التكرار غير المتزامن في `try/except` ومرّر الأخطاء كـ JSON حتى يمكن للواجهة الأمامية عرضها بلطف (مثلاً، حدود المعدل، الإخفاقات المؤقتة):

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

> **لماذا هذا مهم**: يعيد Azure OpenAI `429 Too Many Requests` أثناء تحديد المعدل. بدون `try/except`، يموت التدفق البثي بصمت. مع ذلك، تستقبل الواجهة الأمامية `{"error": "Too Many Requests"}` ويمكنها عرض مطالبة لإعادة المحاولة.

## أنواع أحداث البث (SDK بايثون)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## تنسيق المحادثة
```python
# تدعم واجهة برمجة تطبيقات الردود تنسيق المحادثة عبر مصفوفة الإدخال
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

## معالجة أخطاء تصفية المحتوى

تغير هيكل جسم الخطأ من إكمالات الدردشة إلى API الاستجابات.

قبل (إكمالات الدردشة):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

بعد (API الاستجابات):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

الفروقات الرئيسية:
- ملف لف `innererror` **مفقود** — تفاصيل تصفية المحتوى أصبحت الآن في المستوى الأعلى لجسم `error.body`.
- `content_filter_result` (مفرد) → `content_filters` (مصفوفة جمع) تحتوي على `content_filter_results` (جمع) داخل كل مدخل.
- كل مدخل في `content_filters` يتضمن `blocked`, `source_type`, و`content_filter_results` مع تفاصيل لكل فئة (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

شكل جسم الخطأ الخاص بتصفية المحتوى الكامل في API الاستجابات:
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

## ترحيل بروتوكول HTTP الخام (requests/httpx)

إذا كان التطبيق ينادي Azure OpenAI REST مباشرة بدلاً من استخدام SDK:

قبل (إكمالات الدردشة):
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

بعد (API الاستجابات):
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

> **ملاحظة**: `output_text` خاصية توفرها كائن `Response` في SDK بايثون. استجابة JSON الخام لـ REST لا تحتوي على حقل `output_text` في المستوى الأعلى — النص موجود في `output[0].content[0].text`.

## محادثة متعددة الأدوار
```python
# بناء محادثة باستخدام واجهة برمجة تطبيقات الردود
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# إضافة رد المساعد إلى المحادثة
messages.append({"role": "assistant", "content": response.output_text})

# متابعة المحادثة
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

متعدد الأدوار حسب نوع المحتوى (صريح `input_text` / `output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### متعدد الأدوار عبر `previous_response_id` (بديل)

بدلاً من إدارة مصفوفة المحادثة بنفسك، يمكنك ربط الاستجابات
على جهة الخادم باستخدام `previous_response_id`. يحتفظ API بكل استجابة
ويضيف الأدوار السابقة تلقائيًا.

```python
# الدور الأول
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# الأدوار التالية — فقط مرر رسالة المستخدم الجديدة + معرف الرد السابق
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**متى تستخدم أيهما:**

| النهج | الإيجابيات | السلبيات |
|---|---|---|
| مصفوفة `input` (يدوي) | تحكم كامل بالتاريخ؛ يمكن تقليص/تلخيص؛ لا حاجة لتخزين على الخادم (`store=False`) | مزيد من الكود؛ أنت تدير المصفوفة |
| `previous_response_id` | كود أبسط؛ ربط تلقائي | يتطلب `store=True` (افتراضي); المحادثة مخزنة على الخادم؛ لا يمكن تعديل التاريخ بين الأدوار |

> **ملاحظة ترحيل:** معظم تطبيقات إكمال الدردشة تدير مصفوفة رسائلها بالفعل، لذا يعتبر التحويل إلى مصفوفة `input` ترجمة مباشرة 1:1. استخدم `previous_response_id` للكود الجديد أو عندما لا تحتاج إلى التلاعب بتاريخ المحادثة.

## نماذج التفكير من سلسلة O (o1, o3-mini, o3, o4-mini)

لنماذج سلسلة O قيود معلمات فريدة عند الترحيل إلى API الاستجابات.

### تعيين المعلمات لسلسلة o

| إكمالات الدردشة (سلسلة o) | API الاستجابات | ملاحظات |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | ضبط مرتفع (4096+) — رموز التفكير تحتسب ضمن الحد |
| `reasoning_effort` | `reasoning.effort` | اتركها كما هي إذا كانت موجودة (منخفض/متوسط/مرتفع) |
| `temperature` | أزلها أو ضبطها على `1` | سلسلة o تقبل فقط `1` |
| `top_p` | أزلها | غير مدعومة على سلسلة o |
| `seed` | أزلها | غير مدعومة في API الاستجابات |

### سلسلة o قبل/بعد

قبل (إكمالات دردشة مع سلسلة o):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

بعد (API الاستجابات):
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

> **ملاحظة**: قد تحتفظ نماذج سلسلة o بالإخراج مؤقتًا أثناء التفكير قبل إصدار تغييرات النص. البث لا يزال يعمل لكن أول حدث `response.output_text.delta` قد يصل بعد تأخير أطول مقارنة بنماذج GPT.

## الوصول إلى رموز التفكير
```python
# تستخدم نماذج الاستدلال الاستدلال الداخلي — يمكنك رؤية عدد رموز الاستدلال التي تم استخدامها
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

> **مهم**: استخدم `max_output_tokens=1000` (وليس 50–200) لأخذ عملية التفكير الداخلية لنماذج التفكير في الحسبان. يستخدم النموذج رموز التفكير داخليًا قبل توليد المخرجات النهائية.

## الإخراج المهيكل — مخطط JSON
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

## استخدام الأدوات

- عرّف الدوال في `tools` باستخدام **تنسيق API الاستجابات المسطح** — `name`، `description`، و`parameters` على المستوى الأعلى (ليس متداخلاً تحت `function`).
- عندما يطلب النموذج استخدام أداة، قم بتنفيذها في تطبيقك وضمن نتيجة الأداة في الطلب التالي كعنصر `function_call_output` داخل `input`.
- احتفظ بالمخططات بسيطة؛ قم بمصادقة المدخلات قبل التنفيذ.
- عند استخدام `strict: true`، يجب سرد جميع الخصائص في `required` ويجب أن يكون `additionalProperties: false` إلزامياً.

> **⚠️ `pydantic_function_tool()` غير متوافق**: المساعد `openai.pydantic_function_tool()` لا يزال ينتج تنسيق إكمالات الدردشة القديم المتداخل (`{"type": "function", "function": {"name": ...}}`). لا تستخدمه مع `responses.create()`. عرّف مخططات الأدوات يدويًا أو اكتب غلافًا لتسطيح المخرجات.

### تنسيق تعريف الأداة

يستخدم API الاستجابات تنسيق أداة **مسطح** — المفاتيح `name`، `description`، `parameters` هي في المستوى الأعلى (ليست متداخلة تحت `function`).

**قبل (إكمالات الدردشة — متداخل):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**بعد (API الاستجابات — مسطح):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

مثال كامل:
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

مع `strict: true` (فرض المخطط):
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
            "required": ["city_name"],       # يجب سرد جميع الخصائص
            "additionalProperties": False,   # مطلوب للوضع الصارم
        },
    }
]
```

### دورة استدعاء الأداة (تنفيذ وإرجاع النتائج)

عندما يطلب النموذج استدعاء أداة، استخدم عناصر `response.output` + `function_call_output` — **وليس** نمط إكمالات الدردشة `role: assistant` + `role: tool`.

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
    # أضف عناصر function_call الخاصة بالنموذج إلى المحادثة
    messages.extend(response.output)

    # نفذ كل أداة وأضف النتائج
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # احصل على الرد النهائي مع نتائج الأداة
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### أمثلة استدعاء أدوات بقليل من اللقطات

عند تقديم أمثلة قليلة لاستدعاءات الأدوات في `input`, استخدم عناصر `function_call` و`function_call_output`. يجب أن تبدأ المعرفات بـ `fc_`.

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
# مثال البحث على الويب المدمج
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## إدخال الصور

يتغير نوع عناصر محتوى الصورة من `image_url` إلى `input_image`، ويتغير عنوان URL من كائن متداخل إلى سلسلة مسطحة.

### إدخال الصور — قبل (إكمالات الدردشة)
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

### إدخال الصور — بعد (API الاستجابات، URL)
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

### إدخال الصور — بعد (API الاستجابات، base64)
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

> **التغييرات الرئيسية**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (كائن متداخل) → `"image_url": "..."` (سلسلة مسطحة — إما HTTPS URL أو URI بيانات `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## ترحيل إطار عمل Microsoft Agent (MAF)

**تحقق من إصدار MAF الخاص بك أولاً** — يعتمد الترحيل على ما إذا كنت على MAF 1.0.0+ أو إصدار بيتا/RC قبل 1.0.0.

للتحقق: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

في MAF 1.0.0+، يستخدم `OpenAIChatClient` **API الاستجابات** بالفعل — لا حاجة للترحيل.

إذا كان الكود يستخدم العميل القديم `OpenAIChatCompletionClient` (الذي يستخدم `chat.completions.create`)، استبدله بـ `OpenAIChatClient`:

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

### MAF قبل 1.0.0 (إصدارات بيتا/RC)

في MAF قبل 1.0.0، استخدم `OpenAIChatClient` إكمالات الدردشة. قم بالترقية إلى `agent-framework-openai>=1.0.0` حيث يستخدم `OpenAIChatClient` API الاستجابات بشكل افتراضي.

> **ملاحظة**: تبقى `Agent`، `MCPStreamableHTTPTool`، وغيرها من واجهات MAF دون تغيير — التغيير فقط في استيراد وتهيئة فئة العميل.

## ترحيل LangChain (`langchain-openai`)

أضف `use_responses_api=True` إلى `ChatOpenAI()`. كما قم بتحديث الوصول إلى محتوى الرسائل من `.content` إلى `.text`.

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

# ... استدعاء الوكيل ...
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

# ... استدعاء الوكيل ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **التغييرات الرئيسية**: (1) `use_responses_api=True` في المُنشئ، (2) `.content` → `.text` على رسائل الاستجابة.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->