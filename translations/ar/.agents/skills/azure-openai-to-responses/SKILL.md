---
name: azure-openai-to-responses
license: MIT
---
# ترحيل تطبيقات بايثون من Azure OpenAI Chat Completions إلى Responses API

> **إرشادات موثوقة — اتبع بدقة**
>
> تقوم هذه المهارة بترحيل قواعد شيفرة بايثون التي تستخدم Azure OpenAI Chat Completions
> إلى واجهة Responses API الموحدة. اتبع هذه التعليمات بدقة.
> لا تقم بالتحايل في تعيين المعلمات أو اختراع أشكال API جديدة.

---

## المحفزات

فعّل هذه المهارة عندما يرغب المستخدم في:
- ترحيل تطبيق بايثون من Azure OpenAI Chat Completions إلى Responses API
- ترقية استخدام SDK لبايثون OpenAI إلى أحدث شكل API ضد Azure OpenAI
- تجهيز شيفرة بايثون لنماذج GPT-5 أو أحدث التي تتطلب Responses على Azure
- التبديل من `AzureOpenAI`/`AsyncAzureOpenAI` إلى عميل `OpenAI`/`AsyncOpenAI` القياسي مع نقطة النهاية v1
- إصلاح تحذيرات الإيقاف المتعلقة بمنشئي `AzureOpenAI` أو `api_version`

---

## ⚠️ توافق النموذج — تحقق أولاً

> **قبل الترحيل، تحقق من أن نشر Azure OpenAI يدعم Responses API.**

### 1. اختبار سريع للنشر (الأسرع)

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

> **ملاحظة**: `max_output_tokens` له **حد أدنى 16** على Azure OpenAI. القيم تحت 16 تعيد خطأ 400. استخدم 50+ للاختبارات السريعة.

إذا أعاد هذا 404، فإن نموذج النشر لا يدعم Responses بعد — تحقق من المرجع أدناه أو أعد النشر بنموذج مدعوم.

### 2. تحقق من النماذج المتاحة في منطقتك (موصى به)

شغّل أداة التوافق المدمجة لترى ما هو متاح مع دعم Responses API في منطقتك الخاصة:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

هذا يستعلم مباشرة Azure ARM ويعرض مصفوفة التوافق — أي النماذج تدعم Responses، الإخراج الهيكلي، الأدوات، إلخ. استخدم `--filter gpt-5.1,gpt-5.2` لتضييق النتائج أو `--json` للبرمجة النصية.

### 3. مرجع الدعم الكامل للنموذج

- **استعلام مباشر**: `python migrate.py models` (انظر أعلاه — خاص بالمنطقة، دائمًا محدث)
- **تصفح التوفر**: [جدول ملخص النماذج وتوفر المناطق](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **بدء سريع وإرشادات**: **https://aka.ms/openai/start**

### ⚠️ قيود النماذج الأقدم

> **تحذير**: النماذج القديمة (قبل `gpt-4.1`) قد لا تدعم جميع ميزات Responses API بالكامل.
>
> قيود معروفة مع النماذج القديمة:
> - **معلمة `reasoning`**: غير مدعومة في الكثير من النماذج غير القائمة على الاستدلال. ترحيل `reasoning` فقط إذا كانت موجودة أصلاً في الشيفرة الأصلية.
> - **معلمة `seed`**: غير مدعومة إطلاقًا في Responses API — قم بإزالتها من كل الطلبات.
> - **الإخراج الهيكلي عبر `text.format`**: قد لا تفرض النماذج القديمة بشكل موثوق مخططات JSON بـ `strict: true`.
> - **تنسيق استخدام الأدوات**: GPT-5+ ينظم استدعاءات الأدوات كجزء من الاستدلال الداخلي. النماذج القديمة على Responses ما تزال تعمل لكنها تفتقر لهذا التكامل العميق.
> - **قيود درجة الحرارة**: عند الترحيل إلى `gpt-5`، يجب حذف درجة الحرارة أو تعيينها إلى `1`. النماذج القديمة لا تمتلك هذا القيد.

### نماذج سلسلة O (o1, o3-mini, o3, o4-mini)

لنماذج سلسلة O قيود معلمات فريدة. عند ترحيل التطبيقات التي تستهدف نماذج سلسلة O:

- **`temperature`**: يجب أن تكون `1` (أو محذوفة). نماذج سلسلة O لا تقبل قيم أخرى.
- **`max_completion_tokens` → `max_output_tokens`**: التطبيقات التي تستخدم `max_completion_tokens` الخاصة بـ Azure يجب أن تنتقل إلى `max_output_tokens`. عيّن قيمًا عالية (4096+) لأن رموز الاستدلال تُحسب ضمن الحد.
- **`reasoning_effort`**: إذا استخدم التطبيق `reasoning_effort` (منخفض/متوسط/مرتفع)، احتفظ به — Responses API تدعمه لنماذج سلسلة O.
- **سلوك التدفق**: قد تقوم نماذج سلسلة O بتجميع الإخراج حتى انتهاء الاستدلال قبل إصدار أحداث تغيير النص. التدفق لا يزال يعمل، لكن أول `response.output_text.delta` قد يصل بتأخير أطول مقارنة بنماذج GPT.
- **`top_p`**: غير مدعوم في سلسلة O — قم بإزالته إذا كان موجودًا.
- **استخدام الأدوات**: نماذج سلسلة O تدعم الأدوات عبر Responses API كما في نماذج GPT، لكن جودة تنسيق استدعاء الأدوات تختلف حسب النموذج.

**إجراء — نصيحة استباقية للنموذج**: أثناء مرحلة الفحص، تحقق من النموذج المستهدف للتطبيق (أسماء النشر، متغيرات البيئة، الإعدادات). إذا كان النموذج أقدم من `gpt-4.1` (ليس gpt-4.1+)، أخبر المستخدم استباقيًا:
- الترحيل سيعمل للنص الأساسي، الدردشة، التدفق، والأدوات على النموذج الحالي.
- النماذج الأحدث (`gpt-5.1`، `gpt-5.2`) تقدم تنظيم أدوات أفضل، فرض إخراج منظم، استدلال، وتوفر عبر المناطق.
- يجب عليهم التفكير في ترقية نشرهم عند الاستعداد — ليس عائقًا أمام الترحيل.

لا تمنع أو ترفض الترحيل بناءً على إصدار النموذج. النصيحة للعلم فقط.

### نماذج GitHub لا تدعم Responses API

> **نماذج GitHub (`models.github.ai`، `models.inference.ai.azure.com`) لا تدعم Responses API.**

إذا احتوى قاعدة الشيفرة مسار شيفرة لنماذج GitHub (ابحث عن `base_url` يشير إلى `models.github.ai` أو `models.inference.ai.azure.com`)، **قم بإزالته بالكامل** أثناء الترحيل. Responses API تتطلب Azure OpenAI أو OpenAI أو نقطة نهاية محلية متوافقة (مثل Ollama مع دعم Responses).

إجراء أثناء الفحص:
- علّم أي مسارات شيفرة لنماذج GitHub لإزالتها.

---

## ترحيل الإطار

العديد من التطبيقات تستخدم أُطُرًا عليا فوق OpenAI. عند ترحيلها، يتغير API الخاص بالإطار ذاته — وليس فقط استدعاءات OpenAI الأساسية.

### إطار Microsoft Agent Framework (MAF)

**تحقق من إصدار MAF أولًا** — الترحيل يعتمد على ما إذا كنت على MAF 1.0.0+ أو إصدار بيتا/rc قبل 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **يستخدم Responses API بالفعل** — لا حاجة للترحيل. إذا كانت الشيفرة تستخدم العميل القديم `OpenAIChatCompletionClient` (الذي يستخدم `chat.completions.create`)، استبدله بـ `OpenAIChatClient`.

| قبل | بعد |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

للتحقق من الإصدار: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF قبل 1.0.0 (إصدارات بيتا/rc)

في MAF قبل 1.0.0، يستخدم `OpenAIChatClient` Chat Completions. قم بالترقية إلى `agent-framework-openai>=1.0.0` حيث يستخدم `OpenAIChatClient` Responses API بشكل افتراضي.

لا تغييرات أخرى مطلوبة — تبقى APIs الخاصة بالعميل والأدوات كما هي.

### LangChain (`langchain-openai`)

أضف `use_responses_api=True` إلى `ChatOpenAI()`. كذلك حدّث الوصول إلى الاستجابة من `.content` إلى `.text`.

| قبل | بعد |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

لأمثلة كاملة عن الشيفرة قبل/بعد، راجع [cheat-sheet.md](./references/cheat-sheet.md).

---

## إرشادات ترحيل الواجهة الأمامية

> **Responses API أمر خاص بالجهة الخادمية.** رَحِّل الباك إند الخاص ببايثون؛ يجب أن يبقى عقد HTTP في الواجهة الأمامية دون تغيير إلا إذا كان الباك إند مجرد تمرير خفيف — في هذه الحالة، فكّر في اعتماد شكل طلب Responses لإزالة طبقة الترجمة. إذا كانت الواجهة الأمامية تستدعي OpenAI مباشرةً بمفتاح من جهة العميل، حرّك تلك الاستدعاءات إلى باك إند أولًا.

### إيقاف `@microsoft/ai-chat-protocol`

حزمة npm `@microsoft/ai-chat-protocol` ملغاة ويجب استبدالها بـ [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). إذا وجدتها في الواجهة الأمامية:

1. استبدل وسم سكربت CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. أزل تهيئة `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. استبدل `client.getStreamedCompletion(messages)` باستدعاء `fetch()` مباشر إلى نقطة تدفق الخادم.
4. استبدل `for await (const response of result)` بـ `for await (const chunk of readNDJSONStream(response.body))`.
5. حدّث وصول الخاصية من `response.delta.content` / `response.error` إلى `chunk.delta.content` / `chunk.error`.

---

## الأهداف

- حصر كل مواقع استدعاء بايثون التي تستخدم Chat Completions أو Completions القديمة ضد Azure OpenAI.
- اقتراح خطة ترحيل وتسلسل لقواعد الشيفرة بايثون.
- تطبيق تعديلات آمنة وتصحيحات طفيفة للانتقال إلى Responses API.
- تحديث المستدعين لاستهلاك مخطط إخراج Responses؛ بدون أغلفة توافق خلفي.
- تشغيل اختبارات/تّنقيحات؛ إصلاح الأعطال الطفيفة الناتجة عن الترحيل.
- تجهيز مجموعات تغييرات صغيرة قابلة للمراجعة وتقديم ملخص نهائي مع الفروقات (لا تلتزم بالتغييرات).

---

## الضوابط

- عدّل الملفات فقط داخل مساحة عمل git. لا تكتب خارجها أبدًا.
- لا تحافظ على أغلفة التوافق الخلفي؛ رحّل الشيفرة إلى شكل API الجديد.
- لا تترك تعليقات انتقال أو ملفات نسخ احتياطي.
- احتفظ بسيميantics التدفق إذا استُخدمت سابقًا؛ وإلا استعمل غير تدفقية.
- اطلب موافقة قبل تشغيل الأوامر أو استدعاءات الشبكة إذا كنت في وضع الموافقة.
- لا تشغّل `git add` / `git commit` / `git push`; قم فقط بإنتاج تعديلات في شجرة العمل.

---

## الخطوة 0: ترحيل عميل Azure OpenAI (المتطلب الأولي)

إذا كانت قاعدة الشيفرة تستخدم منشئي `AzureOpenAI` أو `AsyncAzureOpenAI`، رحّل أولًا إلى منشئي `OpenAI` / `AsyncOpenAI` القياسيين. منشئو Azure المحددون مهجورون في `openai>=1.108.1`.

### لماذا مسار API v1؟

تستخدم نقطة النهاية الجديدة `/openai/v1` عميل `OpenAI()` القياسي بدلًا من `AzureOpenAI()`، ولا تتطلب معلمة `api_version`، وتعمل بشكل متطابق عبر OpenAI وAzure OpenAI. شيفرة العميل نفسها مؤمنة للمستقبل — لا حاجة لإدارة الإصدار.

### التغييرات المفتاحية

| قبل | بعد |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | إزالة تامة |

### قائمة تنظيف

- أزل وسيط `api_version` من إنشاء العميل.
- أزل متغيرات البيئة `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` من `.env`، إعدادات التطبيق، وملفات Bicep/البنية التحتية.
- أعد تسمية `AZURE_OPENAI_CLIENT_ID` إلى `AZURE_CLIENT_ID` في `.env`، إعدادات التطبيق، Bicep/البنية التحتية، وfixtures الاختبارية (وفقًا لاتفاقية SDK القياسية لـ Azure Identity).
- تأكد من أن `openai>=1.108.1` موجود في `requirements.txt` أو `pyproject.toml`.

### ترحيل متغيرات البيئة

| متغير البيئة القديم | الإجراء | الملاحظات |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **إزالة** | لا حاجة لـ `api_version` مع نقطة النهاية v1 |
| `AZURE_OPENAI_API_VERSION` | **إزالة** | كما أعلاه |
| `AZURE_OPENAI_CLIENT_ID` | **إعادة تسمية** → `AZURE_CLIENT_ID` | اتفاقية SDK القياسية لـ Azure Identity لـ `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **الاحتفاظ** | لا يزال مطلوبًا لإنشاء `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **الاحتفاظ** | يستخدم كمعلمة `model` في `responses.create` |
| `AZURE_OPENAI_API_KEY` | **الاحتفاظ** | يستخدم كمفتاح `api_key` للمصادقة المعتمدة على المفتاح |

لمثال على إعداد العميل (تزامني، غير متزامن، EntraID، مفتاح API، المستأجر المتعدد)، راجع [cheat-sheet.md](./references/cheat-sheet.md).

---

## الخطوة 1: كشف مواقع الاستدعاء القديمة

شغّل السكريبت [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) لإيجاد كل مواقع الاستدعاء التي تحتاج ترحيل:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

أو شغّل هذه البحثات يدويًا — كل تطابق هدف ترحيل:

```bash
# استدعاءات API القديمة (يجب إعادة كتابة)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# منشئو عملاء أزور المهجورين (يجب الاستبدال)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# أنماط الوصول لشكل الاستجابة (يجب التحديث)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# تعريفات الأدوات بتنسيق متداخل قديم (يجب التسوية)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# نتائج الأدوات بالتنسيق القديم (يجب التحويل إلى function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# المعلمات المهجورة (يجب الإزالة أو إعادة التسمية)
rg "response_format"
rg "max_tokens\b"        # إعادة التسمية إلى max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# متغيرات البيئة المهجورة (تنظيف)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # يجب أن تكون AZURE_CLIENT_ID

# نقاط نهاية نماذج GitHub (يجب الإزالة — واجهة استجابات API غير مدعومة)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# أنماط قديمة على مستوى الإطار (يجب التحديث)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: الاستبدال بـ OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: يحتاج إلى use_responses_api=True

# بنية الاختبار التحتية (يجب التحديث)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# الوصول إلى جسم خطأ مرشح المحتوى (يجب التحديث — تم تغيير الهيكل)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # صيغة مفردة قديمة — الآن content_filter_results (جمعة) داخل مصفوفة content_filters

# استدعاءات HTTP الخام لنقطة نهاية Chat Completions (يجب تحديث URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### قواعد تقريبية (كشف وإعادة كتابة)

- **عميل Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **مُنشئو عملاء Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **الأدوات**: حوّل تعريفات أدوات استدعاء الدوال من الشكل المتداخل (`{"type": "function", "function": {"name": ...}}`) إلى صيغة Responses المسطحة (`{"type": "function", "name": ...}`)؛ استخدم `tool_choice`؛ أرجع نتائج الأدوات كعناصر `{"type": "function_call_output", "call_id": ..., "output": ...}` (وليس `{"role": "tool", ...}`).
- **جولات الأدوات**: عندما يعيد النموذج استدعاءات دوال، أضف عناصر `response.output` إلى المحادثة (وليس قاموس يدوي `{"role": "assistant", "tool_calls": [...]}`)، ثم أضف عناصر `function_call_output` لكل نتيجة.
- **أمثلة الأدوات قليلة الطلقات**: إذا تضمن الحوار أمثلة استدعاء أدواة مشفرة يدويًا، حوّلها إلى عناصر `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. يجب أن تبدأ المعرفات بـ `fc_`.
- **`pydantic_function_tool()`**: هذه الدالة المساعدة لا تزال تولد التنسيق المتداخل القديم وهي **غير متوافقة** مع `responses.create()`. استبدلها بتعريفات أدوات يدوية أو غلاف تسطيح.
- **دورات متعددة**: احتفظ بتاريخ المحادثة في التطبيق؛ مرّر اللفات السابقة عبر عناصر `input`.
- **التنسيق**: استبدل مستوى Chat الأعلى `response_format` بـ `text.format` في Responses. الشكل القانوني: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **عناصر المحتوى**: استبدل Chat `content[].type: "text"` بـ Responses `content[].type: "input_text"` للدوران المستخدم/النظام.
- **عناصر محتوى الصور**: استبدل Chat `content[].type: "image_url"` بـ Responses `content[].type: "input_image"`. يتغير حقل `image_url` من كائن متداخل `{"url": "..."}` إلى سلسلة مسطحة. راجع ورقة الغش لأمثلة قبل/بعد.
- **جهد الاستدلال**: **انقل `reasoning` فقط إذا كان موجودًا بالفعل في الكود الأصلي**.
- **معالجة خطأ فلترة المحتوى**: تغير هيكل جسم الخطأ. استخدمت Chat Completions `error.body["innererror"]["content_filter_result"]` (مفرد)؛ يستخدم Responses API `error.body["content_filters"][0]["content_filter_results"]` (جمع، داخل مصفوفة). الكود الذي يصل إلى `innererror` سيرمي `KeyError`. أعد كتابة المسار لاستخدام المسار الجديد.
- **مكالمات HTTP الخام**: إذا استدعى التطبيق REST API الخاص بـ Azure OpenAI مباشرة (عبر `requests`، `httpx`، إلخ) باستخدام `/openai/deployments/{name}/chat/completions?api-version=...`، أعد الكتابة إلى `/openai/v1/responses`. يتغير جسم الطلب: `messages` → `input`, أضف `max_output_tokens` و `store: false`, احذف باراميتر الاستعلام `api-version`. يتغير جسم الاستجابة: `choices[0].message.content` → `output[0].content[0].text` (ملاحظة: `output_text` خاصية مساعدة في SDK غير موجودة في JSON الخام).

---

## الخطوة 2: تطبيق الترحيل

### ملاحظات الترحيل (Chat Completions → Responses)

- **لماذا نرحل**: Responses هو API الموحد للنصوص والأدوات والبث؛ Chat Completions هو قديم. مع GPT-5، Responses مطلوب لأفضل أداء.
- **HTTP**: نقطة نهاية Azure تتحول من `/openai/deployments/{name}/chat/completions` إلى `/openai/v1/responses`.
- **الحقول**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` تبقى كما هي.
- **التنسيق**: `response_format` → `text.format` مع كائن مناسب.
- **عناصر المحتوى**: استبدل Chat `content[].type: "text"` بـ Responses `content[].type: "input_text"` للدوران النظام/المستخدم.
- **عناصر محتوى الصور**: استبدل Chat `content[].type: "image_url"` بـ Responses `content[].type: "input_image"`، مسطحًا الحقل `image_url` من `{"image_url": {"url": "..."}}` إلى `{"image_url": "..."}` (سلسلة نصية عادية — إما عنوان HTTPS أو URI بيانات `data:image/...;base64,...`).

### مرجع تعيين المعلمات

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (مصفوفة عناصر) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (كائن) |
| `temperature` | `temperature` (لم يتغير) |
| `stop` | `stop` (لم يتغير) |
| `frequency_penalty` | `frequency_penalty` (لم يتغير) |
| `presence_penalty` | `presence_penalty` (لم يتغير) |
| `tools` / استدعاء الدوال | `tools` (لم يتغير) |
| `seed` | **احذف** (غير مدعوم) |
| `store` | `store` (تعيين إلى `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (نص مسطح) |

للأمثلة الكاملة على الكود قبل/بعد، راجع [cheat-sheet.md](./references/cheat-sheet.md).

لترحيل البنية التحتية للاختبار (القيود، اللقطات، التأكيدات)، راجع [test-migration.md](./references/test-migration.md).

لاستكشاف الأخطاء وإصلاحها، راجع [troubleshooting.md](./references/troubleshooting.md).

---

## الاحتفاظ بالبيانات والحالة

- عيّن `store: false` في جميع طلبات Responses.
- لا تعتمد على معرّفات الرسائل السابقة أو السياق المخزن في الخادم؛ احتفظ بالحالة التي يديرها العميل وقلل البيانات الوصفية.

---

## معايير القبول

### بوابات على مستوى الكود (يجب أن تمر جميعها)

- [ ] لا توجد نتائج مطابقة لـ `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` في الملفات المهاجرة.
- [ ] لا توجد نتائج مطابقة لـ `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — جميع المنشئين يستخدمون `OpenAI`/`AsyncOpenAI` مع نقطة نهاية v1.
- [ ] لا توجد نتائج مطابقة لـ `rg "models\.github\.ai|models\.inference\.ai\.azure"` — تم إزالة مسارات كود نماذج GitHub.
- [ ] لا توجد نتائج مطابقة لـ `rg "OpenAIChatCompletionClient"` — يستخدم كود MAF 1.0.0+ `OpenAIChatClient` (الذي يستخدم Responses API). في ما قبل 1.0.0، قم بالترقية إلى `agent-framework-openai>=1.0.0`.
- [ ] جميع نداءات `ChatOpenAI(...)` تتضمن `use_responses_api=True`.
- [ ] لا توجد نتائج مطابقة لـ `rg "choices\[0\]"` — جميع وصولات الاستجابة تستخدم `resp.output_text` أو مخطط إخراج Responses.
- [ ] لا يوجد `response_format` في المستوى الأعلى؛ جميع الإخراجات المهيكلة تستخدم `text={"format": {...}}`.
- [ ] `openai>=1.108.1` و `azure-identity` موجودان في `requirements.txt` أو `pyproject.toml`; تم إعادة تثبيت التبعيات.
- [ ] `store=False` محدد في كل نداء `responses.create`.
- [ ] لا يوجد `api_version` في إنشاء العميل؛ تمت إزالة `AZURE_OPENAI_API_VERSION` من ملفات البيئة والبنية التحتية.

### بوابات بنية تحتية للاختبار (يجب أن تمر جميعها)

- [ ] لا توجد نتائج مطابقة لـ `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] لا توجد نتائج مطابقة لـ `rg "_azure_ad_token_provider" tests/` — تم تحديث التأكيدات للتحقق من `isinstance(client, AsyncOpenAI)` أو `base_url`.
- [ ] لا توجد نتائج مطابقة لـ `rg "prompt_filter_results|content_filter_results" tests/` — تمت إزالة فلترات Azure المزوّرة.
- [ ] استخدام تجهييزات المزيف بـ `kwargs.get("input")` بدلًا من `kwargs.get("messages")`.
- [ ] تحديث لقطات الملفات / المفاتيح الذهبية لشكل بث Responses (بدون `choices[0]`، `function_call`، `logprobs`، إلخ).
- [ ] اجتياز `pytest` بدون أخطاء بعد جميع تحديثات الاختبار.

### بوابات سلوكية (تحقق يدويًا أو عبر حزمة الاختبار)

- [ ] **الإتمام الأساسي**: `responses.create` غير المتدفقة تعيد `output_text` غير فارغ.
- [ ] **تكافؤ البث**: إذا كان الكود الأصلي يستخدم البث، فالكود المهاجر يبث ويرجع أحداث `response.output_text.delta` ذات التغييرات غير الفارغة.
- [ ] **الإخراج المهيكل**: إذا كان يستخدم `text.format` مع `json_schema`، تكتمل `json.loads(resp.output_text)` بنجاح وتتطابق مع المخطط.
- [ ] **دورة استدعاء الأدوات**: إذا استخدمت الأدوات، يصدر النموذج استدعاءات أدوات، ينفذها التطبيق، ويعيد الطلب التالي `output_text` نهائيًا (لا حلقة لانهائية).
- [ ] **تكافؤ غير متزامن**: إذا كان يستخدم `AsyncAzureOpenAI`، فإن ما يعادله في `AsyncOpenAI` يعمل مع `await`.
- [ ] **معدل الخطأ**: لا أخطاء جديدة 400/401/404 مقارنة بالخط الأساسي قبل الترحيل.

### المسلّمات

- الملخص يتضمن الملفات المعدلة، عدد مواقع الاتصال القديمة قبل/بعد، والخطوات التالية.
- التغييرات هي تعديلات على شجرة العمل فقط (بدون التزامات).

---

## متطلبات إصدار SDK

| الحزمة | الإصدار الأدنى |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | الأحدث (لمصادقة EntraID) |

---

## المراجع

- [ورقة الغش - كل مقتطفات الكود](./references/cheat-sheet.md)
- [ترحيل الاختبار - المزيفات، اللقطات، التأكيدات](./references/test-migration.md)
- [استكشاف الأخطاء وإصلاحها - الأخطاء، جدول المخاطر، الفخاخ](./references/troubleshooting.md)
- [detect_legacy.py - الماسح الآلي](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [عدة بدء Azure OpenAI](https://aka.ms/openai/start)
- [توثيق API Azure OpenAI Responses](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [دورة حياة إصدار API لـ Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [مرجع API OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->