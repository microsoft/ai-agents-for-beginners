# عیب‌یابی، جدول ریسک و نکات مهم  

## عیب‌یابی خطاهای ۴۰۰  

| خطا | رفع |  
|-------|-----|  
| `missing_required_parameter: tools[0].name` | تعریف ابزار از فرمت قدیمی تو در توی Chat Completions استفاده می‌کند | تبدیل از `{"type": "function", "function": {"name": ...}}` به `{"type": "function", "name": ..., "parameters": ...}` — نام، توضیح و پارامترها در سطح بالاتر قرار می‌گیرند |  
| `unknown_parameter: input[N].tool_calls` | نتایج ابزار چندمرحله‌ای از فرمت قدیمی Chat Completions استفاده می‌کنند | جایگزینی `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` با آیتم‌های `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |  
| `invalid_function_parameters: 'required' is required` | ابزار با `strict: true` آرایه `required` ندارد | هنگام تنظیم `strict: true`، تمام خصوصیات باید در `required` لیست شده و `additionalProperties: false` تنظیم شود |  
| `invalid_function_parameters: 'additionalProperties' is required` | ابزار با `strict: true` مقدار `additionalProperties: false` را ندارد | افزودن `"additionalProperties": false` به شیء پارامترها |  
| `invalid input[N].id: Expected an ID that begins with 'fc'` | شناسه function_call چندمرحله‌ای دارای پیشوند اشتباه است | شناسه‌های تماس تابع باید با `fc_` شروع شوند (مثلاً `fc_example1`)، نه `call_` |  
| `missing_required_parameter: text.format.name` | افزودن کلید `"name"` به دیکشنری فرمت (مثلاً `"name": "Output"`) |  
| `invalid_type: text.format` | اطمینان از اینکه `text.format` یک دیکشنری با کلیدهای `type`، `name`، `strict` و `schema` است — نه رشته |  
| `invalid input content type` | استفاده از نوع محتوای `input_text`/`output_text` به جای Chat `text` |  
| `invalid input content type` (تصویر) | نوع محتوای تصویر هنوز `"type": "image_url"` است | تغییر به `"type": "input_image"` |  
| `Expected object, got string` در `image_url` | `image_url` هنوز یک شیء تو در تو به شکل `{"url": "..."}` است | تبدیل به رشته ساده: `"image_url": "https://..."` یا `"image_url": "data:image/...;base64,..."` |  
| `integer below minimum value` برای `max_output_tokens` | حداقل روی Azure OpenAI برابر با **16** است. برای آزمایش‌ها بیش از ۵۰، برای تولید بیش از ۱۰۰۰ استفاده کنید. |  
| `429 Too Many Requests` هنگام استریم | محدودیت نرخ اعمال شده است. استریم را داخل `try/except` پیچیده و خطای JSON را به فرانت‌اند ارسال کنید، پیاده‌سازی استراحت/تلاش مجدد را انجام دهید. |  
| `KeyError: 'innererror'` در خطای فیلتر محتوا | ساختار بدنه خطای فیلتر محتوا در API Responses تغییر کرده است | Chat Completions از `error.body["innererror"]["content_filter_result"]` استفاده می‌کرد؛ Responses API از `error.body["content_filters"][0]["content_filter_results"]` (جمع و داخل آرایه) استفاده می‌کند. تمام دسترسی‌های `innererror` را بازنویسی کنید. |  

---  

## جدول ریسک مهاجرت  

| نشانه | اشتباه احتمالی | رفع |  
|---------|---------------|-----|  
| خروجی `output_text` خالی یا بریده شده | `max_output_tokens` برای مدل‌های استنتاجی خیلی کم است | مقدار `max_output_tokens=1000` یا بیشتر تنظیم شود — توکن‌های استنتاجی جزو محدودیت هستند |  
| `400 invalid_type: text.format` | رشته `response_format` به جای دیکشنری `text.format` پاس داده شده | استفاده از `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |  
| خطای `404 Not Found` روی `/openai/v1/responses` | `base_url` اشتباه است — پسوند `/openai/v1/` فراموش شده | اطمینان از `base_url=f"{endpoint}/openai/v1/"` (با اسلش در انتها) |  
| خطای `401 Unauthorized` پس از تغییر به `OpenAI()` | کلید api تنظیم نشده یا ارائه‌دهنده توکن به درستی منتقل نشده | برای EntraID: `api_key=token_provider` (تابع فراخوانی‌پذیر). برای کلید API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |  
| مدل خطای `deployment not found` برمی‌گرداند | پارامتر `model` با نام استقرار Azure شما مطابقت ندارد | استفاده از `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — این نام استقرار است، نه نام مدل |  
| `json.loads(resp.output_text)` خطای `JSONDecodeError` دارد | شِما اعمال نشده یا مدل پشتیبانی خروجی JSON سخت‌گیرانه ندارد | اطمینان از تنظیم `"strict": True` در شِما و بررسی پشتیبانی مدل از خروجی ساختارمند |  
| استریم هیچ رویداد `delta` تولید نمی‌کند | بررسی نوع رویداد اشتباه است | فیلتر کردن روی `event.type == "response.output_text.delta"`، نه `chat.completion.chunk` در Chat |  
| خطای ۴۰۰ روی ورودی تصویر پس از مهاجرت | نوع محتوای تصویر به‌روزرسانی نشده است | تغییر `"type": "image_url"` به `"type": "input_image"` و تبدیل `"image_url": {"url": "..."}` به `"image_url": "..."` (رشته ساده) |  
| حلقه بی‌نهایت تماس ابزار | نتیجه ابزار در `input` درخواست بعدی موجود نیست | پس از اجرای ابزار، یک آیتم `{"type": "function_call_output", "call_id": ..., "output": ...}` به `input` درخواست بعدی اضافه کنید |  
| خطای `temperature` با GPT-5 یا سری o | مقدار صریح `temperature` غیر از ۱ | حذف `temperature` یا تنظیم آن به `1` برای GPT-5 و مدل‌های سری o (o1, o3-mini, o3, o4-mini) |  
| خطای `top_p` با سری o | پشتیبانی از `top_p` وجود ندارد | هنگام هدف قرار دادن مدل‌های سری o، `top_p` را حذف کنید |  
| شناسایی نشدن `max_completion_tokens` | استفاده از پارامتر مختص Azure | جایگزینی `max_completion_tokens` با `max_output_tokens`. برای سری o مقدار ۴۰۹۶+ تنظیم شود (توکن‌های استنتاجی در محدودیت حساب می‌شوند). |  
| خروجی خالی یا بریده شده در سری o | مقدار `max_output_tokens` خیلی پایین است | سری o از توکن‌های استنتاجی استفاده می‌کند. `max_output_tokens=4096` یا بیشتر تنظیم شود — نه ۵۰۰-۱۰۰۰. |  
| `400 integer_below_min_value` برای `max_output_tokens` | مقدار کمتر از ۱۶ | Azure OpenAI مقدار `max_output_tokens >= 16` را الزامی کرده است. برای تست‌های سریع بیش از ۵۰، برای تولید بیش از ۱۰۰۰ استفاده کنید. |  
| `429 Too Many Requests` در وسط استریم | محدودیت نرخ توسط Azure OpenAI اعمال شده | استریم بدون نمایش خطا قطع می‌شود. همیشه حلقه استریم `async for event in await coroutine:` را در `try/except` بپیچید و خطای `{"error": str(e)}` را به فرانت‌اند ارسال کنید. |  
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | مستاجر اشتباه یا عدم ورود | به صورت صریح `tenant_id=os.getenv("AZURE_TENANT_ID")` را پاس دهید. محلی دستور `azd auth login --tenant <tenant-id>` را اجرا کنید. |  
| `404 Not Found` هنگام استفاده از GitHub Models (`models.github.ai`) | GitHub Models از Responses API پشتیبانی نمی‌کند | مسیر کد GitHub Models را به طور کامل حذف کنید. از Azure OpenAI، OpenAI یا نقطه پایان محلی سازگار (مثلاً Ollama با پشتیبانی Responses) استفاده کنید. |  
| MAF `OpenAIChatCompletionClient` هنوز از Chat Completions استفاده می‌کند | استفاده از کلاینت قدیمی MAF در 1.0.0+ | در MAF 1.0.0+، `OpenAIChatClient` به طور پیش‌فرض از Responses API استفاده می‌کند. جایگزین کردن `OpenAIChatCompletionClient` با `OpenAIChatClient`. برای نسخه‌های قبل از 1.0.0، به `agent-framework-openai>=1.0.0` ارتقا دهید. |  
| عامل LangChain خروجی خالی برمی‌گرداند یا در تماس‌های ابزار شکست می‌خورد | `ChatOpenAI` از Responses API استفاده نمی‌کند | افزودن `use_responses_api=True` به `ChatOpenAI(...)`. همچنین تغییر `.content` به `.text` در پیام‌های پاسخ. |  
| `KeyError: 'innererror'` در هندلر خطای فیلتر محتوا | ساختار بدنه خطا در Responses API تغییر کرده است | بازنویسی `error.body["innererror"]["content_filter_result"]["jailbreak"]` به `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. بخش `innererror` حذف شده است؛ جزئیات فیلتر محتوا اکنون در آرایه سطح بالای `content_filters` با `content_filter_results` (جمع) داخل هر ورودی قرار دارد. |  
| فراخوانی HTTP خام به `/openai/deployments/.../chat/completions` کد 404 برمی‌گرداند | نقطه پایان قدیمی Chat Completions REST | بازنویسی URL به `/openai/v1/responses`. تغییر بدنه درخواست: `messages` → `input`، اضافه کردن `max_output_tokens` + `store: false`، حذف پارامتر کوئری `api-version`. تغییر پارس پاسخ: `choices[0].message.content` → `output[0].content[0].text` (توجه: `output_text` یک ویژگی راحتی SDK است، در JSON خام REST نیست). |  

---  

## نکات مهم  

1. اگر قبلاً از Chat Completions برای وضعیت مکالمه استفاده می‌کردید، وضعیت خود را به صورت صریح با Responses مدیریت کنید.  
2. استفاده از `max_output_tokens` را به جای `max_tokens` قدیمی ترجیح دهید.  
3. هنگام مهاجرت به `gpt-5` مطمئن شوید که `temperature` مشخص نشده یا برابر با `1` باشد.  
4. جایگزین کردن Chat `content[].type: "text"` با Responses `content[].type: "input_text"` برای ورودی‌های کاربر/سیستم.  
5. برای `text.format` دیکشنری مناسب ارائه دهید (مثلاً `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`)، نه رشته ساده.  
6. پارامتر `seed` در Responses پشتیبانی نمی‌شود؛ آن را از درخواست‌ها حذف کنید.  
7. **استنتاج:** تنها در صورتی `reasoning` را اضافه کنید که کد اصلی آن را استفاده کرده باشد. `reasoning` را به تماس‌های API که قبلاً نداشتند اضافه نکنید ـ بسیاری از مدل‌های غیر استنتاجی این پارامتر را پشتیبانی نمی‌کنند.  
8. **اندازه‌گیری `max_output_tokens`:** برای مدل‌های استنتاجی (GPT-5-mini, GPT-5, سری o)، مقدار `max_output_tokens=4096` یا بیشتر تنظیم شود — نه ۵۰–۱۰۰۰. مدل ابتدا از توکن‌های استنتاجی داخلی استفاده می‌کند قبل از تولید خروجی قابل مشاهده؛ محدودیت‌های پایین باعث پاسخ بریده یا خالی می‌شوند.  
9. **سری o و `max_completion_tokens`:** اگر کد اصلی از `max_completion_tokens` (مختص Azure برای سری o) استفاده کرده، جایگزین آن با `max_output_tokens` شود. Responses API آن پارامتر را قبول نمی‌کند.  
10. **سری o و `reasoning_effort`:** اگر کد اصلی از `reasoning_effort` (کم/متوسط/زیاد) استفاده می‌کند، آن را به `reasoning={"effort": "<value>"}` در تماس Responses API منتقل کنید.  
11. **تاخیر استریم سری o:** مدل‌های سری o استنتاج داخلی انجام می‌دهند قبل از تولید خروجی. هنگام استریم، انتظار تاخیر طولانی‌تر قبل از اولین رویداد `response.output_text.delta` را داشته باشید. این طبیعی است — مدل در حال استنتاج است، متوقف نشده است.  
9. **`_azure_ad_token_provider` حذف شده است:** `AsyncOpenAI` / `OpenAI` دیگر ویژگی `_azure_ad_token_provider` ندارند. آزمون‌ها یا کدی که به این ویژگی دسترسی دارند با `AttributeError` مواجه می‌شوند. ارائه‌دهنده توکن به عنوان `api_key` ارسال شده و در شیء کلاینت قابل بررسی نیست.  
10. **فایل‌های Snapshot / طلایی:** اگر مجموعه تست از تست‌های snapshot استفاده می‌کند، **همه** فایل‌های snapshot حاوی شکل‌های استریم Chat Completions (`choices[0]`, `content_filter_results`, `function_call` و غیره) باید به شکل جدید Responses به‌روزرسانی شوند. این موضوع آسان است که فراموش شود و باعث شکست‌های مقایسه snapshot گردد.  
11. **مسیر mock monkeypatch:** هدف monkeypatch از `openai.resources.chat.AsyncCompletions.create` به `openai.resources.responses.AsyncResponses.create` (یا `Responses.create` برای حالت همگام) تغییر یافته است. استفاده از مسیر قدیمی به صورت بی‌صدا بی‌تاثیر است — mock دریافت نمی‌شود و تست‌ها به API واقعی برخورد می‌کنند یا شکست می‌خورند.  
12. **`input` به جای `messages`:** توابع mock باید مقدار `kwargs.get("input")` را بخوانند نه `kwargs.get("messages")`. API Responses از `input` برای سابقه مکالمه استفاده می‌کند.  
13. **نامگذاری متغیر محیطی:** Azure Identity SDK از `AZURE_CLIENT_ID` (نه `AZURE_OPENAI_CLIENT_ID`) برای `ManagedIdentityCredential(client_id=...)` استفاده می‌کند. در تست‌ها، فایل‌های `.env`، تنظیمات برنامه و Bicep/زیرساخت تغییر نام دهید.  
14. **حداقل `max_output_tokens` برابر ۱۶ است:** Azure OpenAI مقادیر کمتر از ۱۶ را با خطای `400 integer_below_min_value` رد می‌کند. برای تست سریع مقدار ۵۰، برای تولید بیش از ۱۰۰۰ استفاده کنید. حداقل‌بندی در `max_tokens` قدیمی وجود نداشت.  
15. **`tenant_id` برای `AzureDeveloperCliCredential`:** وقتی منبع Azure OpenAI در مستاجر متفاوت است، باید `tenant_id` را صراحتاً ارسال کنید — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. بدون آن، اعتبارنامه به صورت خاموش مستاجر اشتباه را استفاده کرده و `401` بازمی‌گرداند.  
16. **محدودیت‌های نرخ در استریم به شکل متفاوت ظاهر می‌شوند:** با Chat Completions، خطای 429 معمولاً مانع شروع جریان می‌شد. در استریم API Responses، خطای 429 می‌تواند **میان جریان** رخ دهد — تکرارگر ناهمگام استثنا پرتاب می‌کند. همیشه حلقه استریم را در `try/except` بپیچید و خطای JSON خط به خط ارسال کنید تا فرانت‌اند بتواند آن را به خوبی مدیریت کند.  

۱۷. **مدیریت خطای جریان الزامی برای برنامه‌های وب است**: الگوی `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` حیاتی است. بدون آن، جریان SSE/JSONL به‌صورت خاموش هنگام هر خطای سروری می‌میرد و فرانت‌اند هنگ می‌کند.
۱۸. **تعاریف ابزار باید از فرمت تخت استفاده کنند**: API پاسخ‌ها انتظار دارد `{"type": "function", "name": ..., "parameters": ...}` — نه فرمت تو در توی Chat Completions که به صورت `{"type": "function", "function": {"name": ..., "parameters": ...}}` است. این رایج‌ترین خطای مهاجرت برای کد فراخوانی تابع است.
۱۹. **`pydantic_function_tool()` ناسازگار است**: کمک‌کتابخانه `openai.pydantic_function_tool()` هنوز فرمت قدیمی تو در تو را تولید می‌کند. از آن با `responses.create()` استفاده نکنید. اسکیمای ابزار را دستی تعریف کنید یا خروجی را تخت کنید.
۲۰. **نتایج ابزار از `function_call_output` استفاده می‌کنند، نه `role: tool`**: بعد از اجرای ابزار، باید `{"type": "function_call_output", "call_id": ..., "output": ...}` اضافه شود — نه `{"role": "tool", "tool_call_id": ..., "content": ...}`. برای درخواست ابزار دستیار، از `messages.extend(response.output)` استفاده کنید — نه دیکشنری دستی `{"role": "assistant", "tool_calls": [...]}`.
۲۱. **`strict: true` به `required` + `additionalProperties: false` نیاز دارد**: هنگام استفاده از `strict: true` روی ابزار، هر ویژگی باید در آرایه `required` باشد و `additionalProperties` باید `false` باشد. عدم وجود هر کدام باعث خطای ۴۰۰ می‌شود.
۲۲. **شناسه‌های فراخوانی تابع پیشوندهای خاصی دارند**: هنگام ارائه آیتم‌های `function_call` کم‌شات در `input`، فیلد `id` باید با `fc_` شروع شود و فیلد `call_id` باید با `call_` شروع شود (مثلاً `"id": "fc_example1", "call_id": "call_example1"`). استفاده از پیشوند قدیمی Chat Completions `call_` برای `id` رد می‌شود.
۲۳. **GitHub Models از API پاسخ‌ها پشتیبانی نمی‌کند**: اگر برنامه دارای مسیر کد GitHub Models است (که `base_url` به `models.github.ai` یا `models.inference.ai.azure.com` اشاره دارد)، باید کامل حذف شود. هیچ مسیر مهاجرتی وجود ندارد — به Azure OpenAI، OpenAI، یا نقطه پایانی محلی سازگار منتقل شوید.
۲۴. **ساختار بدنه خطای فیلتر محتوا تغییر کرده است**: خطاهای Chat Completions از `error.body["innererror"]["content_filter_result"]` (مفرد) استفاده می‌کردند. خطاهای API پاسخ‌ها از `error.body["content_filters"][0]["content_filter_results"]` (جمع و داخل آرایه) استفاده می‌کنند. کلید `innererror` دیگر وجود ندارد. کدی که مستقیم به `innererror` دسترسی داشته باشد در زمان اجرا `KeyError` می‌دهد — این به‌راحتی در مهاجرت قابل چشم‌پوشی است چون فقط وقتی فیلتر محتوا واقعاً فعال شود ظاهر می‌شود. هنگام مهاجرت همیشه روی `innererror` جستجو کنید.
۲۵. **فراخوانی‌های HTTP خام نیاز به بازنویسی URL + بدنه دارند**: برنامه‌هایی که مستقیماً از طریق `requests`، `httpx`، `aiohttp` به Azure OpenAI REST با مسیر `/openai/deployments/{name}/chat/completions?api-version=...` فراخوانی می‌کنند، باید به `/openai/v1/responses` تغییر دهند. بدنه درخواست به جای `messages` از `input` استفاده می‌کند، به `max_output_tokens` و `store` نیاز دارد، و پارامتر کوئری `api-version` حذف شده است. متن بدنه پاسخ در `output[0].content[0].text` است — **نه** `output_text` که یک ویژگی راحتی SDK است و در JSON خام REST وجود ندارد.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->