---
name: azure-openai-to-responses
license: MIT
---
# مهاجرت برنامه‌های پایتون از Azure OpenAI Chat Completions به Responses API

> **راهنمایی معتبر — دقیقا دنبال کنید**
>
> این قابلیت، پایگاه‌های کد پایتون که از Azure OpenAI Chat Completions استفاده می‌کنند را
> به API یکپارچه Responses مهاجرت می‌دهد. این دستورالعمل‌ها را دقیقاً دنبال کنید.
> پارامترهای نگاشت را اختراع نکنید و شکل‌های API را خودسرانه تغییر ندهید.

---

## محرک‌ها

این قابلیت زمانی فعال می‌شود که کاربر بخواهد:
- مهاجرت برنامه پایتون از Azure OpenAI Chat Completions به Responses API
- ارتقا استفاده از SDK پایتون OpenAI به شکل جدید API در برابر Azure OpenAI
- آماده‌سازی کد پایتون برای مدل‌های GPT-5 یا جدیدتر که نیاز به Responses در Azure دارند
- تغییر از `AzureOpenAI`/`AsyncAzureOpenAI` به کلاینت استاندارد `OpenAI`/`AsyncOpenAI` با نقطه پایانی v1
- رفع هشدارهای منسوخ شدن مربوط به سازندگان `AzureOpenAI` یا `api_version`

---

## ⚠️ سازگاری مدل — ابتدا بررسی کنید

> **قبل از مهاجرت، اطمینان حاصل کنید که استقرار Azure OpenAI شما از Responses API پشتیبانی می‌کند.**

### 1. تست سریع استقرار (سریع‌ترین)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **توجه**: `max_output_tokens` حداقل ۱۶ در Azure OpenAI دارد. مقادیر کمتر از ۱۶ باعث خطای ۴۰۰ می‌شود. برای تست‌های سریع از ۵۰+ استفاده کنید.

اگر این پاسخ ۴۰۴ برگرداند، مدل استقرار هنوز از Responses پشتیبانی نمی‌کند — مرجع زیر را بررسی کنید یا با مدلی پشتیبانی‌شده دوباره استقرار دهید.

### 2. بررسی مدل‌های موجود در منطقه خود (توصیه‌شده)

ابزار سازگاری مدل داخلی را اجرا کنید تا ببینید چه مدل‌هایی در منطقه خاص شما با پشتیبانی Responses API موجود است:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

این به صورت زنده Azure ARM را پرس‌وجو می‌کند و ماتریس سازگاری را نشان می‌دهد — کدام مدل‌ها Responses، خروجی ساختاریافته، ابزارها و غیره را پشتیبانی می‌کنند. از `--filter gpt-5.1,gpt-5.2` برای محدود کردن نتایج یا از `--json` برای اسکریپت استفاده کنید.

### 3. مرجع کامل پشتیبانی مدل

- **پرس‌وجوی زنده**: `python migrate.py models` (بالا — خاص منطقه، همیشه به‌روز)
- **مرور قابلیت‌ها**: [جدول خلاصه مدل‌ها و دسترسی منطقه‌ای](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **شروع سریع و راهنمایی**: **https://aka.ms/openai/start**

### ⚠️ محدودیت‌های مدل‌های قدیمی‌تر

> **هشدار**: مدل‌های قدیمی‌تر (قبل از `gpt-4.1`) ممکن است تمام ویژگی‌های Responses API را کاملاً پشتیبانی نکنند.
>
> محدودیت‌های شناخته‌شده با مدل‌های قدیمی‌تر:
> - **پارامتر `reasoning`**: در بسیاری از مدل‌های بدون reasoning پشتیبانی نمی‌شود. فقط در صورت وجود قبلی `reasoning` را مهاجرت دهید.
> - **پارامتر `seed`**: اصلا در Responses API پشتیبانی نمی‌شود — از همه درخواست‌ها حذف شود.
> - **خروجی ساختاریافته با `text.format`**: مدل‌های قدیمی‌تر ممکن است شماتیک‌های JSON `strict: true` را به صورت قابل اعتماد اعمال نکنند.
> - **هماهنگی ابزارها**: GPT-5+ هماهنگی تماس با ابزارها را به عنوان بخشی از reasoning داخلی انجام می‌دهد. مدل‌های قدیمی‌تر در Responses هنوز کار می‌کنند اما این ارتباط عمیق را ندارند.
> - **محدودیت دما**: هنگام مهاجرت به `gpt-5` دما باید حذف شود یا روی `1` تنظیم شود. مدل‌های قدیمی‌تر چنین محدودیتی ندارند.

### مدل‌های reasoning سری O (o1, o3-mini, o3, o4-mini)

مدل‌های سری O محدودیت‌های پارامتری خاصی دارند. هنگام مهاجرت برنامه‌هایی که هدف مدل‌های سری O هستند:

- **`temperature`**: باید `1` باشد (یا حذف شود). مدل‌های سری O مقادیر دیگر را قبول ندارند.
- **`max_completion_tokens` → `max_output_tokens`**: برنامه‌هایی که از `max_completion_tokens` مخصوص Azure استفاده می‌کنند باید به `max_output_tokens` تغییر دهند. مقادیر بالا (۴۰۹۶+) تنظیم کنید زیرا توکن‌های reasoning به حد نهایی اضافه می‌شوند.
- **`reasoning_effort`**: اگر برنامه `reasoning_effort` (کم/متوسط/زیاد) را استفاده می‌کند، نگه دارید — Responses API این پارامتر را برای مدل‌های سری O پشتیبانی می‌کند.
- **رفتار استریمینگ**: مدل‌های سری O ممکن است خروجی را تا اتمام reasoning بافر کنند قبل از ارسال رویدادهای تغییر متن. استریمینگ هنوز کار می‌کند، اما اولین `response.output_text.delta` ممکن است با تأخیر بیشتری نسبت به مدل‌های GPT دریافت شود.
- **`top_p`**: در سری O پشتیبانی نمی‌شود — اگر هست حذف کنید.
- **استفاده از ابزار**: مدل‌های سری O از ابزارها از طریق Responses API مانند مدل‌های GPT پشتیبانی می‌کنند، اما کیفیت هماهنگی تماس ابزار بر اساس مدل متفاوت است.

**عمل — مشاوره پیشگیرانه مدل**: در مرحله اسکن بررسی کنید برنامه به کدام مدل هدف دارد (نام‌های استقرار، متغیرهای محیطی، تنظیمات). اگر مدل قبل از `gpt-4.1` است (نه `gpt-4.1` به بعد)، به صورت پیشگیرانه به کاربر بگویید:
- مهاجرت برای متن پایه، چت، استریمینگ و ابزارها روی مدل فعلی‌شان کار می‌کند.
- مدل‌های جدیدتر (`gpt-5.1`، `gpt-5.2`) هماهنگی بهتر ابزار، اعمال دقیق‌تر ساختار خروجی، reasoning و دسترسی بین‌منطقه‌ای بهتری دارند.
- آنها باید هنگام آماده بودن ارتقا دهند — این موضوع مانعی برای مهاجرت نیست.

مهاجرت را به دلیل نسخه مدل مسدود یا رد نکنید. این مشاوره صرفاً اطلاع‌رسانی است.

### مدل‌های GitHub پشتیبانی Responses API را ندارند

> **مدل‌های GitHub (`models.github.ai`, `models.inference.ai.azure.com`) از Responses API پشتیبانی نمی‌کنند.**

اگر پایگاه کد شما مسیر کد مدل‌های GitHub دارد (دنبال `base_url` به `models.github.ai` یا `models.inference.ai.azure.com` بگردید)، **در هنگام مهاجرت آن را کاملا حذف کنید**. Responses API به Azure OpenAI، OpenAI یا نقطه پایانی محلی سازگار (مثل Ollama با پشتیبانی Responses) نیاز دارد.

اقدام در زمان اسکن:
- مسیرهای کد مدل‌های GitHub را برای حذف علامت‌گذاری کنید.

---

## مهاجرت چارچوب‌ها

بسیاری از برنامه‌ها از چارچوب‌های سطح بالاتر روی OpenAI استفاده می‌کنند. هنگام مهاجرت اینها، تغییرات API چارچوب نیز باید اعمال شود — نه فقط فراخوان‌های پایه OpenAI.

### چارچوب Microsoft Agent Framework (MAF)

**ابتدا نسخه MAF خود را بررسی کنید** — مهاجرت بستگی دارد که شما روی MAF 1.0.0+ هستید یا نسخه بتا/rc قبل از 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **هم‌اکنون از Responses API استفاده می‌کند** — نیازی به مهاجرت نیست. اگر پایگاه کد از `OpenAIChatCompletionClient` قدیمی استفاده می‌کند (که `chat.completions.create` را صدا می‌زند)، آن را با `OpenAIChatClient` جایگزین کنید.

| قبل | بعد |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

برای بررسی نسخه: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### نسخه‌های قبل از 1.0.0 MAF (انتشارهای بتا/rc)

در MAF قبل از 1.0.0، `OpenAIChatClient` از Chat Completions استفاده می‌کرد. به `agent-framework-openai>=1.0.0` ارتقا دهید که در آن `OpenAIChatClient` به طور پیش‌فرض از Responses API استفاده می‌کند.

هیچ تغییر دیگری لازم نیست — API های `Agent` و ابزارها همانند قبل هستند.

### LangChain (`langchain-openai`)

پارامتر `use_responses_api=True` را به `ChatOpenAI()` اضافه کنید. همچنین دسترسی به پاسخ را از `.content` به `.text` تغییر دهید.

| قبل | بعد |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

برای مثال‌های کامل کد قبل و بعد، به [cheat-sheet.md](./references/cheat-sheet.md) مراجعه کنید.

---

## راهنمایی مهاجرت فرانت‌اند

> **Responses API مسئله سرور است.** بک‌اند پایتون خود را مهاجرت دهید؛ قرارداد HTTP فرانت‌اند نباید تغییر کند مگر اینکه بک‌اند شما صرفاً یک لایه عبوری نازک باشد — در این صورت به کارگیری شکل درخواست Responses را برای حذف لایه ترجمه در نظر بگیرید. اگر فرانت‌اند مستقیماً با کلید سمت کلاینت OpenAI را صدا می‌زند، ابتدا آن تماس‌ها را به بک‌اند منتقل کنید.

### حذف پکیج `@microsoft/ai-chat-protocol`

پکیج npm `@microsoft/ai-chat-protocol` منسوخ شده و باید با [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) جایگزین شود. اگر در فرانت‌اند با آن مواجه شدید:

1. تگ اسکریپت CDN را جایگزین کنید:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. نمونه‌سازی `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`) را حذف کنید.
3. `client.getStreamedCompletion(messages)` را با فراخوانی مستقیم `fetch()` به نقطه پایانی استریم بک‌اند جایگزین کنید.
4. `for await (const response of result)` را با `for await (const chunk of readNDJSONStream(response.body))` جایگزین کنید.
5. دسترسی به ویژگی‌ها را از `response.delta.content` / `response.error` به `chunk.delta.content` / `chunk.error` به‌روزرسانی کنید.

---

## اهداف

- فهرست همه مکان‌های فراخوانی پایتون که از Chat Completions یا Completions قدیمی در برابر Azure OpenAI استفاده می‌کنند.
- پیشنهاد برنامه و توالی مهاجرت برای پایگاه کد پایتون.
- اعمال ویرایش‌های ایمن و کمینه برای تغییر به Responses API.
- به‌روزرسانی فراخوان‌ها برای استفاده از شماتیک خروجی Responses؛ بدون لفافه‌های سازگاری عقبگرد.
- اجرای تست‌ها/لینت‌ها؛ رفع شکست‌های جزئی ناشی از مهاجرت.
- آماده‌سازی مجموعه‌های تغییر کوچک و قابل بازبینی و ارائه خلاصه نهایی همراه با تفاوت‌ها (بدون کامیت).

---

## محدودیت‌ها

- فقط فایل‌های داخل فضای کاری گیت را تغییر دهید. هرگز بیرون ننویسید.
- شیم‌های سازگاری عقبگرد را نگه ندارید؛ کد را به شکل API جدید مهاجرت دهید.
- نظر یادداشت‌های مربوط به انتقال یا فایل‌های پشتیبان باقی نگذارید.
- معنای استریمینگ را اگر قبلا استفاده شده حفظ کنید؛ در غیر این صورت غیر استریمینگ استفاده کنید.
- اگر در حالت تأیید هستید، قبل از اجرای دستورات یا تماس‌های شبکه‌ای اجازه بگیرید.
- `git add`/`git commit`/`git push` اجرا نکنید؛ فقط تغییرات کاری در شاخه کاری تولید کنید.

---

## گام ۰: مهاجرت کلاینت Azure OpenAI (پیش‌نیاز)

اگر پایگاه کد از سازندگان `AzureOpenAI` یا `AsyncAzureOpenAI` استفاده می‌کند، ابتدا به سازندگان استاندارد `OpenAI` / `AsyncOpenAI` مهاجرت کنید. سازندگان مخصوص Azure در `openai>=1.108.1` منسوخ شده‌اند.

### چرا مسیر API نسخه v1؟

نقطه پایانی جدید `/openai/v1` از کلاینت استاندارد `OpenAI()` به جای `AzureOpenAI()` استفاده می‌کند، پارامتر `api_version` نیاز ندارد و روی OpenAI و Azure OpenAI به همان صورت کار می‌کند. کد کلاینت آینده‌نگر است — مدیریت نسخه لازم نیست.

### تغییرات کلیدی

| قبل | بعد |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | کامل حذف شود |

### فهرست پاک‌سازی

- آرگومان `api_version` را از ساخت کلاینت حذف کنید.
- متغیرهای محیطی `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` را از `.env`، تنظیمات برنامه و فایل‌های Bicep/زیرساخت حذف کنید.
- `AZURE_OPENAI_CLIENT_ID` را به `AZURE_CLIENT_ID` در `.env`، تنظیمات برنامه، Bicep/زیرساخت و تست‌های مصنوعی (رسم استاندارد Azure Identity SDK) تغییر نام دهید.
- اطمینان حاصل کنید `openai>=1.108.1` در `requirements.txt` یا `pyproject.toml` است.

### مهاجرت متغیرهای محیطی

| متغیر محیطی قدیمی | اقدام | توضیحات |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **حذف** | با نقطه پایانی v1 نیازی به `api_version` نیست |
| `AZURE_OPENAI_API_VERSION` | **حذف** | مانند بالا |
| `AZURE_OPENAI_CLIENT_ID` | **تغییر نام** → `AZURE_CLIENT_ID` | رسم استاندارد Azure Identity SDK برای `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **نگه دارید** | هنوز برای ساخت `base_url` لازم است |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **نگه دارید** | به عنوان پارامتر `model` در `responses.create` استفاده می‌شود |
| `AZURE_OPENAI_API_KEY` | **نگه دارید** | به عنوان کلید API برای اعتبارسنجی مبتنی بر کلید استفاده می‌شود |

برای مثال‌های کد راه‌اندازی کلاینت (همگام، غیرهمگام، EntraID، کلید API، چند مستاجری) به [cheat-sheet.md](./references/cheat-sheet.md) مراجعه کنید.

---

## گام ۱: شناسایی محل‌های فراخوانی قدیمی

اسکریپت [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) را اجرا کنید تا همه محل‌های فراخوانی که نیاز به مهاجرت دارند پیدا شوند:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

یا این جستجوها را دستی انجام دهید — هر تطابق یک هدف مهاجرت است:

```bash
# تماس‌های API قدیمی (باید بازنویسی شود)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# سازندگان کلاینت Azure منسوخ‌شده (باید جایگزین شوند)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# الگوهای دسترسی به شکل پاسخ (باید به‌روزرسانی شود)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# تعاریف ابزار در قالب تو در تو قدیمی (باید صاف شود)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# نتایج ابزار در قالب قدیمی (باید به function_call_output تبدیل شود)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# پارامترهای منسوخ‌شده (باید حذف یا تغییر نام یابند)
rg "response_format"
rg "max_tokens\b"        # تغییر نام به max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# متغیرهای محیطی منسوخ‌شده (باید پاک‌سازی شوند)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # باید AZURE_CLIENT_ID باشد

# نقاط پایانی مدل‌های GitHub (باید حذف شوند — API پاسخ‌ها پشتیبانی نمی‌شود)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# الگوهای قدیمی در سطح چارچوب (باید به‌روزرسانی شود)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: جایگزینی با OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: نیاز به use_responses_api=True دارد

# زیرساخت تست (باید به‌روزرسانی شود)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# دسترسی به بدنه خطای فیلتر محتوا (باید به‌روزرسانی شود — ساختار تغییر کرده است)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # فرم مفرد قدیمی — اکنون content_filter_results (جمع) داخل آرایه content_filters

# تماس‌های HTTP خام به نقطه پایانی Chat Completions (باید URL به‌روزرسانی شود)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### قواعد سرانگشتی (شناسایی و بازنویسی)

- **کلاینت Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **سازه‌های کلاینت آژور**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **ابزارها**: تبدیل تعاریف ابزارهای تابع‌فراخوانی شده از فرمت تو در تو (`{"type": "function", "function": {"name": ...}}`) به فرمت مسطح Responses (`{"type": "function", "name": ...}`); استفاده از `tool_choice`; نتایج ابزار را به صورت آیتم‌های `{"type": "function_call_output", "call_id": ..., "output": ...}` برگردانید (نه `{"role": "tool", ...}`).
- **رفت و برگشت ابزار**: وقتی مدل فراخوانی‌های تابع را برمی‌گرداند، آیتم‌های `response.output` را به مکالمه اضافه کنید (نه دیکشنری دستی `{"role": "assistant", "tool_calls": [...]}`)، سپس آیتم‌های `function_call_output` را برای هر نتیجه ضمیمه کنید.
- **مثال‌های ابزار چند-شات**: اگر مکالمه شامل مثال‌های سخت‌کد شده برای فراخوانی ابزار باشد، آنها را به آیتم‌های `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` تبدیل کنید. شناسه‌ها باید با `fc_` شروع شوند.
- **`pydantic_function_tool()`**: این کمکی هنوز فرمت تو در تو قدیمی را تولید می‌کند و **با `responses.create()` سازگار نیست**. به جای آن از تعاریف ابزار دستی یا یک لایه مسطح‌کننده استفاده کنید.
- **چند نوبتی**: سابقه مکالمه را در برنامه نگه دارید؛ نوبت‌های قبلی را با آیتم‌های `input` ارسال کنید.
- **قالب‌بندی**: `response_format` سطح بالای Chat را با `text.format` در Responses جایگزین کنید. شکل متعارف: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **آیتم‌های محتوا**: `content[].type: "text"` در Chat را با `content[].type: "input_text"` در Responses برای نوبت‌های کاربر/سیستم جایگزین کنید.
- **آیتم‌های محتوای تصویر**: `content[].type: "image_url"` در Chat را با `content[].type: "input_image"` در Responses جایگزین کنید. فیلد `image_url` از شیء تو در تو `{"url": "..."}` به رشته مسطح تغییر می‌کند. برای نمونه‌های قبل و بعد به برگه راهنما مراجعه کنید.
- **تلاش استدلال**: **فقط در صورتی `reasoning` را مهاجرت دهید که در کد اصلی وجود داشته باشد**.
- **مدیریت خطای فیلتر محتوا**: ساختار بدنه خطا تغییر کرده است. Chat Completions از `error.body["innererror"]["content_filter_result"]` (مفرد) استفاده می‌کرد؛ Responses API از `error.body["content_filters"][0]["content_filter_results"]` (جمع، داخل آرایه) استفاده می‌کند. کدی که به `innererror` دسترسی دارد `KeyError` ایجاد می‌کند. مسیر جدید را استفاده کنید.
- **فراخوانی‌های HTTP خام**: اگر برنامه مستقیماً از API REST آژور OpenAI (از طریق `requests`, `httpx` و غیره) با آدرس `/openai/deployments/{name}/chat/completions?api-version=...` استفاده می‌کند، آن را به `/openai/v1/responses` بازنویسی کنید. بدنه درخواست تغییر می‌کند: `messages` → `input`, افزودن `max_output_tokens` و `store: false`, حذف پارامتر کوئری `api-version`. بدنه پاسخ تغییر می‌کند: `choices[0].message.content` → `output[0].content[0].text` (توجه: `output_text` یک ویژگی راحت SDK است که در JSON خام REST نیست).

---

## گام ۲: اعمال مهاجرت

### نکات مهاجرت (Chat Completions → Responses)

- **چرایی مهاجرت**: Responses API یکپارچه برای متن، ابزارها و پخش است؛ Chat Completions قدیمی است. همراه با GPT-5، استفاده از Responses برای بهترین عملکرد ضروری است.
- **HTTP**: نقطه انتهایی آژور از `/openai/deployments/{name}/chat/completions` به `/openai/v1/responses` تغییر می‌یابد.
- **فیلدها**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` بدون تغییر می‌ماند.
- **قالب‌بندی**: `response_format` → `text.format` با یک شیء مناسب.
- **آیتم‌های محتوا**: `content[].type: "text"` از Chat را با `content[].type: "input_text"` در Responses برای نوبت‌های سیستم/کاربر جایگزین کنید.
- **آیتم‌های محتوای تصویر**: `content[].type: "image_url"` از Chat را با `content[].type: "input_image"` در Responses جایگزین کنید. فیلد `image_url` را از `{"image_url": {"url": "..."}}` به `{"image_url": "..."}` (رشته ساده — یا URL HTTPS یا URI داده `data:image/...;base64,...`) مسطح کنید.

### مرجع نگاشت پارامترها

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (آرایه‌ای از آیتم‌ها) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (شیء) |
| `temperature` | `temperature` (بدون تغییر) |
| `stop` | `stop` (بدون تغییر) |
| `frequency_penalty` | `frequency_penalty` (بدون تغییر) |
| `presence_penalty` | `presence_penalty` (بدون تغییر) |
| `tools` / فراخوانی تابع | `tools` (بدون تغییر) |
| `seed` | **حذف شود** (پشتیبانی نمی‌شود) |
| `store` | `store` (تنظیم بر `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (رشته مسطح) |

برای نمونه کامل کد قبل/بعد، به [cheat-sheet.md](./references/cheat-sheet.md) مراجعه کنید.

برای مهاجرت زیرساخت تست (ماک‌ها، اسنپ‌شات‌ها، assertions) به [test-migration.md](./references/test-migration.md) مراجعه کنید.

برای عیب‌یابی خطاها و نکات مهم، به [troubleshooting.md](./references/troubleshooting.md) مراجعه کنید.

---

## نگهداری داده و وضعیت

- مقدار `store: false` را در همه درخواست‌های Responses تنظیم کنید.
- به شناسه پیام‌های قبلی یا زمینه ذخیره شده سرور تکیه نکنید؛ وضعیت را در کلاینت مدیریت کنید و متادیتا را به حداقل برسانید.

---

## معیارهای پذیرش

### گیت‌های سطح کد (همه باید پاس شوند)

- [ ] هیچ نتیجه‌ای برای جستجوی `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` در فایل‌های مهاجرت شده نباشد.
- [ ] هیچ نتیجه‌ای برای `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` نباشد — همه سازندگان از `OpenAI`/`AsyncOpenAI` با نقطه انتهایی v1 استفاده کنند.
- [ ] هیچ نتیجه‌ای برای `rg "models\.github\.ai|models\.inference\.ai\.azure"` نباشد — مسیرهای کد GitHub Models حذف شده‌اند.
- [ ] هیچ نتیجه‌ای برای `rg "OpenAIChatCompletionClient"` نباشد — کد MAF 1.0.0+ از `OpenAIChatClient` (که از Responses API استفاده می‌کند) بهره می‌برد. در نسخه‌های قبل از 1.0.0، به `agent-framework-openai>=1.0.0` آپگرید کنید.
- [ ] همه فراخوانی‌های `ChatOpenAI(...)` شامل `use_responses_api=True` باشند.
- [ ] هیچ نتیجه‌ای برای `rg "choices\[0\]"` نباشد — همه دسترسی‌های پاسخ با `resp.output_text` یا اسکیمای خروجی Responses انجام شود.
- [ ] هیچ `response_format` ای در سطح بالا نباشد؛ همه خروجی ساختاریافته از `text={"format": {...}}` استفاده کنند.
- [ ] در `requirements.txt` یا `pyproject.toml`، `openai>=1.108.1` و `azure-identity` باشند؛ وابستگی‌ها دوباره نصب شده باشند.
- [ ] مقدار `store=False` در همه فراخوانی‌های `responses.create` تنظیم شده باشد.
- [ ] در ساخت کلاینت هیچ `api_version` وجود نداشته باشد؛ `AZURE_OPENAI_API_VERSION` از فایل‌های محیط و زیرساخت حذف شده باشد.

### گیت‌های زیرساخت تست (همه باید پاس شوند)

- [ ] هیچ نتیجه‌ای برای `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` نباشد.
- [ ] هیچ نتیجه‌ای برای `rg "_azure_ad_token_provider" tests/` نباشد — assertions به‌روزرسانی شده‌اند تا `isinstance(client, AsyncOpenAI)` یا `base_url` را بررسی کنند.
- [ ] هیچ نتیجه‌ای برای `rg "prompt_filter_results|content_filter_results" tests/` نباشد — ماک‌های فیلتر خاص آژور حذف شده‌اند.
- [ ] در ماک‌ها از `kwargs.get("input")` به جای `kwargs.get("messages")` استفاده شود.
- [ ] فایل‌های اسنپ‌شات / طلایی به شکل پخش Responses به‌روزرسانی شده‌اند (بدون `choices[0]`, `function_call`, `logprobs` و غیره).
- [ ] پس از همه به‌روزرسانی‌های تست، `pytest` بدون خطا اجرا شود.

### گیت‌های رفتاری (تصدیق دستی یا از طریق ابزار تست)

- [ ] **تکمیل پایه**: `responses.create` غیرجریانی، `output_text` غیرخالی برمی‌گرداند.
- [ ] **همترازی پخش**: اگر کد اصلی از پخش استفاده می‌کرد، کد مهاجرت‌شده پخش کرده و رویدادهای `response.output_text.delta` با دلتاهای غیرخالی تولید کند.
- [ ] **خروجی ساخت‌یافته**: اگر از `text.format` با `json_schema` استفاده می‌شود، `json.loads(resp.output_text)` موفق بوده و با اسکیمای تعریف شده مطابقت داشته باشد.
- [ ] **حلقه فراخوانی ابزار**: اگر ابزارها استفاده می‌شوند، مدل فراخوانی ابزار انجام دهد، برنامه این‌ها را اجرا کند و درخواست پیگیری خروجی نهایی `output_text` را برگرداند (حلقه بی‌نهایت نباشد).
- [ ] **تطابق غیرهمزمان**: اگر `AsyncAzureOpenAI` استفاده شده بود، معادل `AsyncOpenAI` با `await` کار کند.
- [ ] **نرخ خطا**: نسبت به خط پایه پیش از مهاجرت، خطای ۴۰۰/۴۰۱/۴۰۴ جدیدی ایجاد نشود.

### تحویل‌ها

- خلاصه شامل فایل‌های ویرایش شده، شمارش قبل/بعد سایت‌های کال قدیمی، و مراحل بعدی باشد.
- تغییرات تنها ویرایش در درخت کاری باشند (بدون کامیت).

---

## الزامات نسخه SDK

| پکیج | حداقل نسخه |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | آخرین نسخه (برای احراز هویت EntraID) |

---

## مراجع

- [برگه تقلب — همه قطعه‌کدها](./references/cheat-sheet.md)
- [مهاجرت تست — ماک‌ها، اسنپشات‌ها، assertions](./references/test-migration.md)
- [عیب‌یابی — خطاها، جدول ریسک، نکات](./references/troubleshooting.md)
- [detect_legacy.py — اسکنر خودکار](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [مجموعه شروع آژور OpenAI](https://aka.ms/openai/start)
- [مستندات Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [چرخه عمر نسخه API آژور OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [مرجع API OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->