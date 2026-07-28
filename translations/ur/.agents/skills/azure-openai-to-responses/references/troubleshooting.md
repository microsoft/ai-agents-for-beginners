# مسئلہ حل کرنا، خطرے کی میز اور احتیاطی تدابیر

## 400 کی خرابیوں کا حل

| خرابی | حل |
|-------|-----|
| `missing_required_parameter: tools[0].name` | ٹول کی تعریف پرانا چیٹ کمپلیشنز نیسٹڈ فارمیٹ استعمال کرتی ہے | `{"type": "function", "function": {"name": ...}}` سے `{"type": "function", "name": ..., "parameters": ...}` کی طرف فلیٹ کریں — نام، وضاحت، اور پیرامیٹرز ٹاپ لیول پر جائیں |
| `unknown_parameter: input[N].tool_calls` | ملٹی ٹرن ٹول کے نتائج پرانا چیٹ کمپلیشنز فارمیٹ استعمال کرتے ہیں | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` کو `response.output` آئٹمز + `{"type": "function_call_output", "call_id": ..., "output": ...}` کے ساتھ تبدیل کریں |
| `invalid_function_parameters: 'required' is required` | `strict: true` ٹول میں `required` ارے نہیں ہے | جب `strict: true` ہو، تو تمام خصوصیات کو `required` میں شامل کیا جانا چاہیے اور `additionalProperties: false` سیٹ کرنا پڑے گا |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` ٹول میں `additionalProperties: false` نہیں ہے | پیرامیٹرز آبجیکٹ میں `"additionalProperties": false` شامل کریں |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | فیو-شاٹ function_call ID کی پرکس غلط ہے | فنکشن کال IDs کو `fc_` سے شروع ہونا چاہیے (مثلاً `fc_example1`)، `call_` سے نہیں |
| `missing_required_parameter: text.format.name` | فارمیٹ ڈکشنری میں `"name"` کلید شامل کریں (مثلاً `"name": "Output"`) |
| `invalid_type: text.format` | یقینی بنائیں کہ `text.format` ایک ڈکشنری ہے جس میں `type`, `name`, `strict`, `schema` کیز ہوں — سادہ سٹرنگ نہ ہو |
| `invalid input content type` | چیٹ کے `text` کے بجائے `input_text`/`output_text` کنٹینٹ ٹائپ استعمال کریں |
| `invalid input content type` (تصویر) | تصویری مواد اب بھی `"type": "image_url"` استعمال کر رہا ہے | اسے `"type": "input_image"` میں تبدیل کریں |
| `Expected object, got string` on `image_url` | `image_url` اب بھی نیسٹڈ آبجیکٹ `{"url": "..."}` ہے | اسے سیدھی سٹرنگ میں تبدیل کریں: `"image_url": "https://..."` یا `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI پر کم از کم **16** ہے۔ ٹیسٹ کے لیے 50+ اور پروڈکشن کے لیے 1000+ استعمال کریں۔ |
| `429 Too Many Requests` during streaming | ریٹ لمیٹ ہو گئی ہے۔ سٹریمنگ کو `try/except` میں لپیٹیں، ایرر JSON فرنٹ اینڈ کو دیں، بیک آف/ریٹری نافذ کریں۔ |
| `KeyError: 'innererror'` on content filter error | Responses API میں کانٹینٹ فلٹر ایرر باڈی سٹرکچر تبدیل ہو گیا ہے | چیٹ کمپلیشنز میں `error.body["innererror"]["content_filter_result"]` استعمال ہوتا تھا؛ Responses API میں `error.body["content_filters"][0]["content_filter_results"]` (جمع اور آرے کے اندر)۔ تمام `innererror` رسائی کو دوبارہ لکھیں۔ |

---

## مائیگریشن رسک ٹیبل

| علامت | ممکنہ غلطی | حل |
|---------|---------------|-----|
| خالی `output_text` / مختصر جواب | ریئزننگ ماڈلز کے لیے `max_output_tokens` بہت کم ہے | `max_output_tokens=1000` یا اس سے زیادہ سیٹ کریں — ریئزننگ ٹوکنز حد میں شامل ہوتے ہیں |
| `400 invalid_type: text.format` | `text.format` ڈکشنری کے بجائے `response_format` سٹرنگ دی گئی | استعمال کریں `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `/openai/v1/responses` پر `404 Not Found` | غلط `base_url` — `/openai/v1/` سرفکس غائب ہے | یقینی بنائیں `base_url=f"{endpoint}/openai/v1/"` (ٹریلنگ سلیش کے ساتھ) |
| `OpenAI()` پر سوئچ کرنے کے بعد `401 Unauthorized` | `api_key` سیٹ نہیں ہے یا ٹوکن پرووائیڈر درست طریقے سے نہیں دیا گیا | EntraID کے لیے: `api_key=token_provider` (کال ایبل) ۔ API کلید کے لیے: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| ماڈل `deployment not found` دیتا ہے | `model` پیرا میٹر آپ کے Azure ڈیپلائمنٹ نام سے میل نہیں کھاتا | استعمال کریں `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — یہ ڈیپلائمنٹ نام ہے، ماڈل نام نہیں |
| `json.loads(resp.output_text)` پر `JSONDecodeError` آتا ہے | اسکیمہ نافذ نہیں یا ماڈل سخت JSON سپورٹ نہیں کرتا | اسکیمہ میں `"strict": True` یقینی بنائیں، اور چیک کریں ماڈل ساختی آؤٹ پٹ کو سپورٹ کرتا ہے |
| سٹریمنگ میں کوئی `delta` ایونٹ نہیں آتا | غلط ایونٹ ٹائپ چیک کرنا | فلٹر کریں `event.type == "response.output_text.delta"` پر، نہ کہ چیٹ کے `chat.completion.chunk` پر |
| مائیگریشن کے بعد تصویر کی انپٹ پر `400` ایرر | تصویر کا کونٹینٹ ٹائپ اپڈیٹ نہیں ہوا | `"type": "image_url"` کو `"type": "input_image"` میں تبدیل کریں اور `"image_url": {"url": "..."}` کو `"image_url": "..."` (سادہ سٹرنگ) کر دیں |
| ٹول کالز لا متناہی لوپ میں پھنس جاتی ہیں | فالو اپ `input` میں ٹول کا نتیجہ نہیں ہے | ٹول چلانے کے بعد، اگلی درخواست کے `input` میں `{"type": "function_call_output", "call_id": ..., "output": ...}` آئٹم شامل کریں |
| GPT-5 یا o-سیریز کے ساتھ `temperature` ایرر | 1 کے علاوہ صریح `temperature` کی قدر | GPT-5 اور o-سیریز ماڈلز (o1, o3-mini, o3, o4-mini) کے لیے `temperature` ہٹا دیں یا اس کی قدر `1` پر سیٹ کریں |
| o-سیریز کے ساتھ `top_p` ایرر | `top_p` سپورٹ نہیں کرتا | o-سیریز ماڈلز کے لیے `top_p` ہٹا دیں |
| `max_completion_tokens` تسلیم نہیں کیا جاتا | Azure مخصوص پیرا میٹر استعمال کر رہے ہیں | `max_completion_tokens` کی جگہ `max_output_tokens` استعمال کریں۔ o-سیریز کے لیے 4096+ سیٹ کریں (ریئزننگ ٹوکنز حد میں شامل ہوتے ہیں)۔ |
| o-سیریز سے خالی یا مختصر آؤٹ پٹ آنا | `max_output_tokens` بہت کم ہے | o-سیریز اندرونی طور پر ریئزننگ ٹوکن استعمال کرتی ہے۔ `max_output_tokens=4096` یا اس سے زیادہ سیٹ کریں — 500–1000 نہیں۔ |
| `400 integer_below_min_value` برائے `max_output_tokens` | قدر 16 سے کم ہے | Azure OpenAI میں `max_output_tokens >= 16` لازمی ہے۔ سموک ٹیسٹ کے لیے 50+، پروڈکشن کے لیے 1000+ استعمال کریں۔ |
| سٹریمنگ کے دوران `429 Too Many Requests` | Azure OpenAI کے ذریعہ ریٹ لمیٹ | اسٹریم خاموشی سے ٹوٹ جاتا ہے بغیر ایرر ہینڈلنگ کے۔ ہمیشہ `async for event in await coroutine:` کو `try/except` میں لپیٹیں اور فرنٹ اینڈ کو `{"error": str(e)}` دیں۔ |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | غلط ٹیننٹ یا لاگ ان نہیں | واضح طور پر `tenant_id=os.getenv("AZURE_TENANT_ID")` پاس کریں۔ مقامی طور پر `azd auth login --tenant <tenant-id>` چلائیں۔ |
| GitHub ماڈلز (`models.github.ai`) استعمال کرتے ہوئے `404 Not Found` | GitHub ماڈلز Responses API سپورٹ نہیں کرتے | GitHub ماڈلز کا کوڈ ہٹائیں۔ Azure OpenAI، OpenAI یا موزوں لوکل اینڈپوائنٹ (جیسے Ollama جو Responses سپورٹ کرتا ہے) استعمال کریں۔ |
| MAF `OpenAIChatCompletionClient` اب بھی پرانا چیٹ کمپلیشنز استعمال کر رہا ہے | MAF 1.0.0+ میں لیگیسی کلائنٹ استعمال کر رہے ہیں | MAF 1.0.0+ میں `OpenAIChatClient` ڈیفالٹ طور پر Responses API استعمال کرتا ہے۔ `OpenAIChatCompletionClient` کو `OpenAIChatClient` سے بدلیں۔ پری-1.0.0 کے لیے `agent-framework-openai>=1.0.0` میں اپ گریڈ کریں۔ |
| LangChain ایجنٹ ٹول کالز کے ساتھ خالی جواب دیتا ہے یا فیل ہو جاتا ہے | `ChatOpenAI` Responses API استعمال نہیں کر رہا | `ChatOpenAI(...)` میں `use_responses_api=True` شامل کریں۔ جواب کے پیغامات میں `.content` کو `.text` میں تبدیل کریں۔ |
| کانٹینٹ فلٹر ایرر ہینڈلر میں `KeyError: 'innererror'` | Responses API میں ایرر باڈی سٹرکچر تبدیل ہو گیا ہے | `error.body["innererror"]["content_filter_result"]["jailbreak"]` کو `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` میں تبدیل کریں۔ `innererror` ریپر ختم ہو گیا ہے؛ کانٹینٹ فلٹر ڈیٹیلز اب ایک ٹاپ لیول `content_filters` آرے میں ہیں جس میں ہر اندراج کے اندر `content_filter_results` (جمع) موجود ہے۔ |
| `/openai/deployments/.../chat/completions` پر را HTTP کال 404 ریٹرن کرتی ہے | پرانا چیٹ کمپلیشنز REST اینڈپوائنٹ | URL کو `/openai/v1/responses` پر دوبارہ لکھیں۔ درخواست کے باڈی میں `messages` کو `input` میں تبدیل کریں، `max_output_tokens` + `store: false` شامل کریں، `api-version` کو حذف کریں۔ جواب کی پارسنگ میں `choices[0].message.content` کو `output[0].content[0].text` سے بدلیں (نوٹ: `output_text` SDK کی سہولت ہے، اصل REST JSON میں نہیں)۔ |

---

## احتیاطی تدابیر

1. اگر آپ پہلے چیٹ کمپلیشنز کو مکالمے کی حالت کے لیے استعمال کرتے تھے، تو اب Responses کے ساتھ اپنی خود کی حالت واضح طور پر مینج کریں۔
2. روایتی `max_tokens` کے بجائے `max_output_tokens` کو ترجیح دیں۔
3. `gpt-5` پر مائیگریٹ کرتے وقت، یقینی بنائیں کہ `temperature` مقرر نہ ہو یا اس کی قیمت `1` ہو۔
4. چیٹ کے `content[].type: "text"` کو Responses کے `content[].type: "input_text"` سے تبدیل کریں، خاص طور پر یوزر/سسٹم انپٹس کے لیے۔
5. `text.format` کے لیے ایک مناسب ڈکشنری فراہم کریں (مثلاً `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`)، سادہ سٹرنگ نہ دیں۔
6. Responses میں `seed` پیرامیٹر سپورٹ نہیں ہے؛ اس کو درخواستوں سے ہٹا دیں۔
7. **ریئزننگ**: صرف اسی صورت میں `reasoning` شامل کریں اگر اصل کوڈ پہلے ہی اسے استعمال کرتا تھا۔ ان API کالز میں `reasoning` نہ ڈالیں جو اسے استعمال نہیں کرتیں — کئی غیر ریئزننگ ماڈلز اس پیرامیٹر کو سپورٹ نہیں کرتے۔
8. **`max_output_tokens` کا سائز**: ریئزننگ ماڈلز (GPT-5-mini, GPT-5, o-سیریز) کے لیے، `max_output_tokens=4096` یا اس سے زیادہ رکھیں — 50–1000 نہیں۔ ماڈل آؤٹ پٹ بنانے سے پہلے اندرونی طور پر ریئزننگ ٹوکنز استعمال کرتا ہے؛ بہت کم حدیں مختصر یا خالی جوابات کا سبب بنتی ہیں۔
9. **O-سیریز `max_completion_tokens`**: اگر اصل کوڈ میں `max_completion_tokens` (o-سیریز کے لیے Azure مخصوص) استعمال ہو رہا ہے، تو اسے `max_output_tokens` کے ساتھ تبدیل کریں۔ Responses API `max_completion_tokens` قبول نہیں کرتا۔
10. **O-سیریز `reasoning_effort`**: اگر اصل کوڈ `reasoning_effort` (low/medium/high) استعمال کرتا ہے، تو اسے Responses API کال میں `reasoning={"effort": "<value>"}` میں مائیگریٹ کریں۔
11. **O-سیریز سٹریمنگ کی تاخیر**: o-سیریز ماڈلز مشمول تخلیق سے پہلے اندرونی طور پر ریئزننگ کرتے ہیں۔ سٹریمنگ کے دوران، پہلے `response.output_text.delta` ایونٹ میں دیر متوقع ہے۔ یہ عام ہے — ماڈل ریئزن کر رہا ہے، پھنس نہیں گیا۔
9. **`_azure_ad_token_provider` ختم ہو گیا**: `AsyncOpenAI` / `OpenAI` میں `_azure_ad_token_provider` ایٹریبیوٹ نہیں ہے۔ ایسا کوڈ یا ٹیسٹ جو اس پر انحصار کرتے ہیں، `AttributeError` دیں گے۔ ٹوکن پرووائیڈر `api_key` کے طور پر پاس ہوتا ہے اور کلائنٹ آبجیکٹ میں قابل معائنہ نہیں ہے۔
10. **Snapshot / golden فائلز**: اگر ٹیسٹ سوئٹ snapshot testing استعمال کرتی ہے، تو **تمام** snapshot فائلیں جن میں چیٹ کمپلیشنز سٹریمنگ شیپس (`choices[0]`, `content_filter_results`, `function_call` وغیرہ) شامل ہیں، انہیں نئے Responses شیپ کے مطابق اپ ڈیٹ کرنا لازم ہے۔ یہ آسانی سے نظر انداز ہو جاتا ہے اور snapshot کے اسرسنٹ فالئرز کا سبب بنتا ہے۔
11. **Mock monkeypatch کا راستہ**: مونکی پیچ کا ٹارگٹ `openai.resources.chat.AsyncCompletions.create` سے بدل کر `openai.resources.responses.AsyncResponses.create` (یا سنک کے لیے `Responses.create`) ہو گیا ہے۔ پرانا راستہ کچھ نہیں کرے گا — موک اثرانداز نہیں ہوگا، اور ٹیسٹ حقیقی API کو کال کریں گے یا فیل ہو جائیں گے۔
12. **`input`، `messages` نہیں**: موک فنکشنز کو `kwargs.get("input")` پڑھنا چاہیے، نہ کہ `kwargs.get("messages")`۔ Responses API مکالمے کی تاریخ کے لیے `input` استعمال کرتا ہے۔
13. **Env var کا نام**: Azure Identity SDK `AZURE_CLIENT_ID` (نہ کہ `AZURE_OPENAI_CLIENT_ID`) استعمال کرتا ہے `ManagedIdentityCredential(client_id=...)` کے لیے۔ ٹیسٹ، `.env` فائلز، ایپ سیٹنگز، اور Bicep/انفرا میں نام تبدیل کریں۔
14. **`max_output_tokens` کی کم از کم حد 16 ہے**: Azure OpenAI 16 سے کم قدروں کو `400 integer_below_min_value` ایرر دیتا ہے۔ سموک ٹیسٹ کے لیے 50، پروڈکشن کے لیے 1000+ استعمال کریں۔ پرانا `max_tokens` ایسی حد نہیں رکھتا تھا۔
15. **`AzureDeveloperCliCredential` کے لیے `tenant_id`**: جب Azure OpenAI ریسورس مختلف ٹیننٹ میں ہو، تو **ضروری** ہے کہ `tenant_id` واضح طور پر پاس کریں — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`۔ بغیر اس کے، کرڈینشل غلط ٹیننٹ استعمال کرے گا اور `401` واپس کرے گا۔
16. **ریٹ لمٹس سٹریمنگ میں مختلف ظاہر ہوتے ہیں**: چیٹ کمپلیشنز میں 429 عام طور پر اسٹریم شروع ہونے سے روک دیتا تھا۔ Responses API سٹریمنگ میں، 429 **درمیان-اسٹریم** ہو سکتا ہے — اسینک ایٹریٹر ایک استثناء دیتا ہے۔ ہمیشہ سٹریمنگ لوپ کو `try/except` میں لپیٹیں اور ایک ایرر JSON لائن ییلڈ کریں تاکہ فرنٹ اینڈ اسے آسانی سے ہینڈل کر سکے۔

17. **ویب ایپس کے لیے اسٹریمنگ ایرر ہینڈلنگ لازمی ہے**: پیٹرن `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` بہت اہم ہے۔ اس کے بغیر، SSE/JSONL اسٹریم کسی بھی سرور سائیڈ ایرر پر خاموشی سے ختم ہو جاتی ہے اور فرنٹ اینڈ ہینگ ہو جاتا ہے۔
18. **ٹول تعریفات کو فلیٹ فارمیٹ استعمال کرنا چاہیے**: ریسپانسز API کو `{"type": "function", "name": ..., "parameters": ...}` درکار ہے — نہ کہ چیٹ کمپلیشنز کے nested `{"type": "function", "function": {"name": ..., "parameters": ...}}`۔ یہ فنکشن کالنگ کوڈ کے لیے سب سے عام مائیگریشن ایرر ہے۔
19. **`pydantic_function_tool()` غیر مطابقت رکھتا ہے**: `openai.pydantic_function_tool()` ہیلپر اب بھی پرانا nested فارمیٹ تیار کرتا ہے۔ اسے `responses.create()` کے ساتھ استعمال نہ کریں۔ ٹول اسکیماز کو دستی طور پر تعریف کریں یا آؤٹ پٹ کو فلیٹ کریں۔
20. **ٹول کے نتائج میں `function_call_output` استعمال کریں، نہ کہ `role: tool`**: ٹول کے چلنے کے بعد `{"type": "function_call_output", "call_id": ..., "output": ...}` شامل کریں — نہ کہ `{"role": "tool", "tool_call_id": ..., "content": ...}`۔ اسسٹنٹ کی ٹول درخواست کے لیے، `messages.extend(response.output)` استعمال کریں — نہ کہ دستی `{"role": "assistant", "tool_calls": [...]}` ڈکشنری۔
21. **`strict: true` کے لیے `required` + `additionalProperties: false` ضروری ہے**: جب ٹول پر `strict: true` استعمال ہو، تو ہر پراپرٹی `required` ارے میں شامل ہونی چاہیے اور `additionalProperties` کا ویلیو `false` ہونا چاہیے۔ ان میں سے کوئی بھی چیز غائب ہو تو 400 ایرر آئے گا۔
22. **فنکشن کال آئی ڈیز مخصوص سابقے رکھتے ہیں**: جب few-shot `function_call` آئٹمز `input` میں دیں، تو `id` فیلڈ کا آغاز `fc_` سے ہونا چاہیے اور `call_id` فیلڈ کا آغاز `call_` سے ہونا چاہیے (مثلاً `"id": "fc_example1", "call_id": "call_example1"`). پرانے چیٹ کمپلیشنز کے `call_` سابقے والے `id` کو رد کیا جاتا ہے۔
23. **GitHub ماڈلز ریسپانسز API کو سپورٹ نہیں کرتے**: اگر ایپ میں GitHub ماڈلز کوڈ راستہ (`base_url` جو `models.github.ai` یا `models.inference.ai.azure.com` کی طرف اشارہ کرتا ہو) موجود ہو، تو اسے مکمل طور پر ہٹا دیں۔ اس کے لیے کوئی مائیگریشن راستہ نہیں ہے — Azure OpenAI، OpenAI، یا کوئی موافق لوکل اینڈپوائنٹ استعمال کریں۔
24. **کانٹینٹ فلٹر ایرر باڈی کا ڈھانچہ بدل گیا ہے**: چیٹ کمپلیشنز کے ایررز میں `error.body["innererror"]["content_filter_result"]` (واحد) استعمال ہوتا تھا۔ ریسپانسز API کے ایررز میں `error.body["content_filters"][0]["content_filter_results"]` (جمع، ایک آرے کے اندر) استعمال ہوتا ہے۔ `innererror` کلید اب موجود نہیں ہے۔ کوڈ جو براہ راست `innererror` تک رسائی کرتا ہے، رن ٹائم پر `KeyError` دے گا — یہ مائیگریشن میں آسانی سے چھپ جاتا ہے کیونکہ یہ صرف تب ظاہر ہوتا ہے جب کانٹینٹ فلٹر واقعی ٹرگر ہو۔ مائیگریشن کے دوران ہمیشہ `innererror` کے لیے گرپ کریں۔
25. **راؤ ایچ ٹی ٹی پی کالز کو URL + باڈی ری رائٹ کی ضرورت ہے**: Azure OpenAI REST کو براہ راست کال کرنے والی ایپس (جیسا کہ `requests`, `httpx`, `aiohttp`) جو `/openai/deployments/{name}/chat/completions?api-version=...` استعمال کرتی ہیں، انہیں `/openai/v1/responses` پر منتقل ہونا چاہیے۔ درخواست کی باڈی میں `messages` کی جگہ `input` استعمال ہوتی ہے، `max_output_tokens` اور `store` درکار ہیں، اور `api-version` کوئری پیرامیٹر کو ہٹا دیا گیا ہے۔ جواب کی باڈی کا ٹیکسٹ `output[0].content[0].text` پر ہوتا ہے — **نہ کہ** `output_text` پر، جو کہ ایک SDK سہولت پراپرٹی ہے اور راؤ REST JSON میں موجود نہیں ہے۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->