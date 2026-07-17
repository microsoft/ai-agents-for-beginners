# استكشاف الأخطاء، جدول المخاطر والمشكلات الشائعة

## استكشاف أخطاء 400

| الخطأ | الحل |
|-------|-----|
| `missing_required_parameter: tools[0].name` | تعريف الأداة يستخدم تنسيق التعشيش القديم لـ Chat Completions | تغيير الهيكلة من `{"type": "function", "function": {"name": ...}}` إلى `{"type": "function", "name": ..., "parameters": ...}` — حيث توضع name، description، parameters في المستوى الأعلى |
| `unknown_parameter: input[N].tool_calls` | نتائج الأدوات متعددة الأدوار تستخدم تنسيق Chat Completions القديم | استبدال `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` بعناصر `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | أداة `strict: true` تفتقد مصفوفة `required` | عند استخدام `strict: true`، يجب إدراج جميع الخصائص في `required` ويجب تعيين `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | أداة `strict: true` تفتقد `additionalProperties: false` | إضافة `"additionalProperties": false` إلى كائن المعلمات |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | معرف function_call قليل الأمثلة لديه بادئة خاطئة | يجب أن تبدأ معرّفات الاتصال بالدالة بـ `fc_` (مثلاً `fc_example1`)، وليس بـ `call_` |
| `missing_required_parameter: text.format.name` | أضف مفتاح `"name"` إلى قاموس التنسيق (مثلاً `"name": "Output"`) |
| `invalid_type: text.format` | تأكد أن `text.format` قاموس يحتوي على المفاتيح `type`, `name`, `strict`, `schema` — لا يكون نصًا |
| `invalid input content type` | استخدم أنواع المحتوى `input_text`/`output_text` بدلًا من Chat `text` |
| `invalid input content type` (صورة) | محتوى الصورة لا يزال يستخدم `"type": "image_url"` | غيّرها إلى `"type": "input_image"` |
| `Expected object, got string` في `image_url` | `image_url` لا يزال كائنًا متداخلًا `{"url": "..."}` | ساوِه إلى نص عادي: `"image_url": "https://..."` أو `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` لـ `max_output_tokens` | الحد الأدنى هو **16** في Azure OpenAI. استخدم 50+ للاختبارات، 1000+ للإنتاج. |
| `429 Too Many Requests` أثناء البث | تم الحد من المعدل. غلّف البث في `try/except`، وأرسل خطأ JSON للواجهة الأمامية، وطبق تأخير/إعادة المحاولة. |
| `KeyError: 'innererror'` في خطأ فلتر المحتوى | تغير بنية جسم خطأ فلتر المحتوى في Responses API | استخدم `error.body["content_filters"][0]["content_filter_results"]` بدلاً من `error.body["innererror"]["content_filter_result"]` (الجمع وبداخل مصفوفة). أعد كتابة جميع الولوجات إلى `innererror`. |

---

## جدول مخاطر الهجرة

| العَرَض | الخطأ المحتمل | الحل |
|---------|---------------|-----|
| `output_text` فارغة / استجابة مقتصة | `max_output_tokens` منخفض جدًا لنماذج الاستدلال | اضبط `max_output_tokens=1000` أو أعلى — حيث أن رموز الاستدلال تُحتسب مقابل الحد |
| `400 invalid_type: text.format` | تم تمرير سلسلة `response_format` بدلاً من قاموس `text.format` | استخدم `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` على `/openai/v1/responses` | `base_url` خاطئ — مفقود لاحقة `/openai/v1/` | تأكد من `base_url=f"{endpoint}/openai/v1/"` (مع الشرط المائل الأخير) |
| `401 Unauthorized` بعد التبديل إلى `OpenAI()` | `api_key` غير مضبوط أو مزود الرمز لم يُمرّر بشكل صحيح | لـ EntraID: `api_key=token_provider` (دالة قابلة للاستدعاء). لمفتاح API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| النموذج يُرجع `deployment not found` | تُعريف `model` لا يطابق اسم النشر في Azure | استخدم `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — هذا هو اسم النشر لا اسم النموذج |
| `json.loads(resp.output_text)` يرمي `JSONDecodeError` | المخطط غير مفروض أو النموذج لا يدعم JSON الصارم | ضمن `"strict": True` في المخطط، وتحقق أن النموذج يدعم الناتج المهيكل |
| البث لم يُرجع أحداث `delta` | فحص نوع الحدث خاطئ | صفِّ على `event.type == "response.output_text.delta"`، وليس `chat.completion.chunk` الخاص بـ Chat |
| خطأ 400 على إدخال صورة بعد الهجرة | نوع محتوى الصورة غير محدث | غيّر `"type": "image_url"` إلى `"type": "input_image"` وبسط `"image_url": {"url": "..."}` إلى `"image_url": "..."` (نص عادي) |
| نداءات الأدوات تدور إلى ما لا نهاية | نتيجة الأداة مفقودة في `input` الاستدلالي | بعد تنفيذ أداة، ألحق عنصر `{"type": "function_call_output", "call_id": ..., "output": ...}` إلى `input` في الطلب التالي |
| خطأ `temperature` مع GPT-5 أو سلسلة o | قيمة `temperature` صريحة مختلفة عن 1 | أزل `temperature` أو اضبط على `1` لنماذج GPT-5 وسلسلة o (o1, o3-mini, o3, o4-mini) |
| خطأ `top_p` مع سلسلة o | `top_p` غير مدعوم | أزل `top_p` عند استهداف نماذج سلسلة o |
| `max_completion_tokens` غير معترف بها | استخدام معلمة خاصة بـ Azure | استبدل `max_completion_tokens` بـ `max_output_tokens`. واضبطه على 4096+ لسلسلة o (رموز الاستدلال تُحتسب مقابل الحد). |
| خرج فارغ / مقتص من سلسلة o | `max_output_tokens` منخفض جدًا | سلسلة o تستخدم رموز استدلال داخليًا. اضبط `max_output_tokens=4096` أو أعلى — لا تستخدم 500-1000. |
| `400 integer_below_min_value` لـ `max_output_tokens` | القيمة أقل من 16 | Azure OpenAI يفرض `max_output_tokens >= 16`. استخدم 50+ للاختبارات السريعة، 1000+ للإنتاج. |
| `429 Too Many Requests` في منتصف البث | تم الحد من المعدل بواسطة Azure OpenAI | البث ينقطع بصمت بدون معالجة خطأ. غلّف دائمًا `async for event in await coroutine:` بـ `try/except` وأرسل `{"error": str(e)}` للواجهة الأمامية. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | المستأجر خاطئ أو لم يتم تسجيل الدخول | مرر `tenant_id=os.getenv("AZURE_TENANT_ID")` صراحة. شغّل `azd auth login --tenant <tenant-id>` محليًا. |
| `404 Not Found` عند استخدام نماذج GitHub (`models.github.ai`) | نماذج GitHub لا تدعم Responses API | أزل مسار كود نماذج GitHub بالكامل. استخدم Azure OpenAI، OpenAI، أو نقطة نهاية محلية متوافقة (مثلاً Ollama مع دعم Responses). |
| حزمة MAF `OpenAIChatCompletionClient` لا تزال تستخدم Chat Completions | استخدام عميل MAF القديم في 1.0.0+ | في MAF 1.0.0+، يستخدم `OpenAIChatClient` Responses API افتراضيًا. استبدل `OpenAIChatCompletionClient` بـ `OpenAIChatClient`. للتحديث من الإصدارات قبل 1.0.0، قم بالترقية إلى `agent-framework-openai>=1.0.0`. |
| وكيل LangChain يرجع خاليًا أو يفشل مع نداءات الأدوات | `ChatOpenAI` لا يستخدم Responses API | أضف `use_responses_api=True` إلى `ChatOpenAI(...)`. وغيّر `.content` إلى `.text` في رسائل الرد. |
| `KeyError: 'innererror'` في معالج خطأ فلتر المحتوى | بنية جسم الخطأ تغيرت في Responses API | أعد كتابة `error.body["innererror"]["content_filter_result"]["jailbreak"]` إلى `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. لم يعد هناك غلاف `innererror`؛ تفاصيل فلتر المحتوى الآن في مصفوفة عليا `content_filters` مع `content_filter_results` (جمع) داخل كل عنصر. |
| استدعاء HTTP الخام لـ `/openai/deployments/.../chat/completions` يُرجع 404 | نقطة نهاية REST القديمة لـ Chat Completions | أعد كتابة URL إلى `/openai/v1/responses`. غيّر جسم الطلب: `messages` إلى `input`، أضف `max_output_tokens` و `store: false`، واحذف معلمة استعلام `api-version`. غيّر تحليل الرد: `choices[0].message.content` إلى `output[0].content[0].text` (تنبيه: `output_text` خاصية في SDK للتسهيل، غير موجود في JSON الخام لـ REST). |

---

## المشكلات الشائعة

1. إذا كنت تستخدم سابقًا Chat Completions لحفظ حالة المحادثة، فقم بإدارة حالتك الخاصة صراحةً باستخدام Responses.
2. فضّل `max_output_tokens` على `max_tokens` القديم.
3. عند الترحيل إلى `gpt-5`، تأكد من عدم تحديد `temperature` أو تعيينها إلى `1`.
4. استبدل Chat نوع `content[].type: "text"` بنوع Responses `content[].type: "input_text"` للمدخلات من المستخدم/النظام.
5. بالنسبة لـ `text.format`، قدّم قاموسًا صحيحًا (مثلاً `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`)، وليس نصًا عاديًا.
6. معلمة `seed` غير مدعومة في Responses؛ احذفها من الطلبات.
7. **الاستدلال**: ضمّن فقط `reasoning` إذا كان الكود الأصلي يستخدمه بالفعل. لا تضف `reasoning` إلى نداءات API التي لم تكن تحتوي عليه — العديد من النماذج غير المعتمدة على الاستدلال لا تدعم هذه المعلمة.
8. **حجم `max_output_tokens`**: لنماذج الاستدلال (GPT-5-mini، GPT-5، سلسلة o)، استخدم `max_output_tokens=4096` أو أعلى — لا تستخدم 50-1000. النموذج يستخدم رموز الاستدلال داخليًا قبل إنتاج الناتج المرئي؛ الحدود المنخفضة جدًا تسبب استجابات مقتصة أو فارغة.
9. **`max_completion_tokens` لسلسلة o**: إذا كان الكود الأصلي يستخدم `max_completion_tokens` (خاص بـ Azure لسلسلة o)، استبدله بـ `max_output_tokens`. Responses API لا تقبل `max_completion_tokens`.
10. **`reasoning_effort` لسلسلة o**: إذا كان الكود الأصلي يستخدم `reasoning_effort` (منخفض / متوسط / مرتفع)، انقله إلى `reasoning={"effort": "<value>"}` في نداء Responses API.
11. **تأخير البث لسلسلة o**: نماذج سلسلة o تقوم بالاستدلال داخليًا قبل توليد الناتج. عند البث، توقع تأخيرًا أطول قبل حدوث أول حدث `response.output_text.delta`. هذا طبيعي — النموذج يستدل، وليس معلقًا.
9. **`_azure_ad_token_provider` اختفى**: `AsyncOpenAI` / `OpenAI` لا يحتويان على الخاصية `_azure_ad_token_provider`. الاختبارات أو الكود الذي يصل لهذه الخاصية سيفشل بـ `AttributeError`. يتم تمرير مزود الرمز كـ `api_key` ولا يمكن فحصه من كائن العميل.
10. **ملفات Snapshot / الذهبية**: إذا كان مجموعة الاختبار تستخدم اختبار Snapshot، يجب تحديث **جميع** ملفات Snapshot التي تحتوي على أشكال بث Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, ... ) إلى شكل Responses الجديد. هذا سهل التفويت ويسبب فشل تحقق Snapshot.
11. **مسار mock monkeypatch**: يتغير هدف monkeypatch من `openai.resources.chat.AsyncCompletions.create` إلى `openai.resources.responses.AsyncResponses.create` (أو `Responses.create` للتزامن). استخدام المسار القديم لا يفعل شيئًا بصمت — لن يلتقط mock، وستستخدم الاختبارات API الحقيقية أو تفشل.
12. **`input` وليس `messages`**: يجب أن تقرأ دوال mock `kwargs.get("input")` وليس `kwargs.get("messages")`. Responses API تستخدم `input` لسجل المحادثة.
13. **تسمية المتغير البيئي**: Azure Identity SDK يستخدم `AZURE_CLIENT_ID` (وليس `AZURE_OPENAI_CLIENT_ID`) لـ `ManagedIdentityCredential(client_id=...)`. عدّل في الاختبارات، ملفات `.env`، إعدادات التطبيق، وBicep/البنية التحتية.
14. **الحد الأدنى لـ `max_output_tokens` هو 16**: Azure OpenAI يرفض القيم أقل من 16 بخطأ `400 integer_below_min_value`. استخدم 50 للاختبارات السريعة، 1000+ للإنتاج. الـ `max_tokens` القديم لم يكن له حد أدنى كهذا.
15. **`tenant_id` لـ `AzureDeveloperCliCredential`**: عند وجود مورد Azure OpenAI في مستأجر مختلف، **يجب** تمرير `tenant_id` صراحةً — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. بدونه، يستخدم الاعتماد المستأجر الخطأ بصمت ويُرجع 401.
16. **قيود المعدل تظهر بشكل مختلف في البث**: مع Chat Completions، كان 429 يمنع بدء البث عادةً. مع بث Responses API، قد يحدث 429 **منتصف البث** — يرفع المكرر اللامتزامن استثناءً. غلّف دائمًا حلقة البث بـ `try/except` وأرسل سطر JSON للخطأ لكي يتمكن الواجهة الأمامية من التعامل معه بسلاسة.

17. **التعامل مع أخطاء البث أمر ضروري لتطبيقات الويب**: النمط `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` هو أمر حاسم. بدونه، يتوقف تدفق SSE/JSONL بصمت عند حدوث أي خطأ على جانب الخادم ويتوقف الواجهة الأمامية عن الاستجابة.
18. **يجب أن تستخدم تعريفات الأدوات تنسيقًا مسطحًا**: يتوقع API الردود التنسيق `{"type": "function", "name": ..., "parameters": ...}` — وليس التنسيق المتداخل الخاص بإكمالات الدردشة `{"type": "function", "function": {"name": ..., "parameters": ...}}`. هذه هي أكثر أخطاء الترحيل شيوعًا في شفرة استدعاء الوظائف.
19. **`pydantic_function_tool()` غير متوافق**: لا يزال المساعد `openai.pydantic_function_tool()` ينتج التنسيق القديم المتداخل. لا تستخدمه مع `responses.create()`. عرّف مخططات الأدوات يدويًا أو قم بتسطيح الناتج.
20. **نتائج الأدوات تستخدم `function_call_output` وليس `role: tool`**: بعد تنفيذ أداة، قم بإضافة `{"type": "function_call_output", "call_id": ..., "output": ...}` — وليس `{"role": "tool", "tool_call_id": ..., "content": ...}`. لطلب الأداة من المساعد، استخدم `messages.extend(response.output)` — وليس قاموسًا يدويًا من نوع `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` يتطلب `required` + `additionalProperties: false`**: عند استخدام `strict: true` على أداة، يجب إدراج كل خاصية في مصفوفة `required` ويجب أن يكون `additionalProperties` مساويًا لـ `false`. إغفال أيٍ منهما يتسبب في خطأ 400.
22. **لمعرفات استدعاء الوظائف بادئات محددة**: عند توفير عناصر `function_call` متعددة في `input`، يجب أن يبدأ الحقل `id` بـ `fc_` ويبدأ الحقل `call_id` بـ `call_` (مثال: `"id": "fc_example1", "call_id": "call_example1"`). استخدام بادئة `call_` القديمة الخاصة بـ Chat Completions للحقل `id` مرفوض.
23. **نماذج GitHub لا تدعم Responses API**: إذا كان للتطبيق مسار كود نماذج GitHub (`base_url` يشير إلى `models.github.ai` أو `models.inference.ai.azure.com`)، فقم بحذفه تمامًا. لا يوجد مسار ترحيل — انتقل إلى Azure OpenAI أو OpenAI أو نقطة نهاية محلية متوافقة.
24. **تغير هيكل جسم خطأ فلتر المحتوى**: كانت أخطاء إكمالات الدردشة تستخدم `error.body["innererror"]["content_filter_result"]` (مفرد). أما أخطاء Responses API فتستخدم `error.body["content_filters"][0]["content_filter_results"]` (جمع، داخل مصفوفة). مفتاح `innererror` لم يعد موجودًا. الكود الذي يصل مباشرةً إلى `innererror` سيرمي `KeyError` أثناء التشغيل — وهو أمر سهل أن يُفقد أثناء الترحيل لأنه يظهر فقط عند تحفيز فلتر المحتوى فعليًا. ابحث دائمًا عن `innererror` أثناء الترحيل.
25. **مكالمات HTTP الخام تحتاج إلى إعادة كتابة URL + الجسم**: يجب على التطبيقات التي تستدعي REST الخاص بـ Azure OpenAI مباشرة (عبر `requests`، `httpx`، `aiohttp`) باستخدام `/openai/deployments/{name}/chat/completions?api-version=...` أن تتبدل إلى `/openai/v1/responses`. يستخدم جسم الطلب `input` بدلاً من `messages`، ويتطلب `max_output_tokens` و `store`، ويتم حذف معامل الاستعلام `api-version`. نص جسم الاستجابة موجود في `output[0].content[0].text` — **وليس** `output_text`، وهي خاصية راحة في SDK غير موجودة في JSON الخام لخدمة REST.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->