# سجل التغييرات

يتم توثيق جميع التغييرات المهمة في دورة **وكلاء الذكاء الاصطناعي للمبتدئين** في هذا الملف.

## [تم الإصدار] — 2026-07-14

ينقل هذا الإصدار الدورة من نموذجين تم إيقافهما حديثًا، وينقل دفاتر الدروس المتبقية إلى واجهة برمجة تطبيقات إطار عمل الوكيل المستقر من مايكروسوفت، ويصادق على دفاتر بايثون مقابل نشر حي لـ Microsoft Foundry.

### تم التغيير

- **الانتقال بعيدًا عن النماذج المتوقفة (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** تم الآن إيقاف كل من `gpt-4.1` و `gpt-4.1-mini` (تاريخ التقاعد المنشور **14 أكتوبر 2026**). تم استبدال كل مرجع في الدورة (الوثائق، `.env.example`، دفاتر بايثون/.NET والعينات) بـ `gpt-5-mini` غير المتوقفة. يحتفظ مثال توجيه النماذج في الدرس 16 بالتباين الصغير/الكبير باستخدام `gpt-5-nano` (صغير) و `gpt-5-mini` (كبير). الملفات التابعة لجهات خارجية المحتفظ بها ([15-browser-use/llms.txt](../../15-browser-use/llms.txt))، نص نماذج GitHub التاريخي، وملاحظات قدرة مهارة `azure-openai-to-responses` تُركت دون تغيير عمدًا.
- **تم نقل دفتر تسليم الدرس 14 إلى الواجهة البرمجية المستقرة.** يستخدم الآن [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) `agent_framework.orchestrations.HandoffBuilder` مع `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, تدفق مبني على `event.type`، و `FoundryChatClient` (بديلًا عن الرموز المحذوفة قبل النسخة 1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **تم نقل دفتر الحلقة البشرية في الدرس 14 إلى الواجهة البرمجية المستقرة.** يتوقف الآن عبر `ctx.request_info(...)` + `@response_handler` (بديلًا عن `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` المحذوفة)، يبني باستخدام `WorkflowBuilder(start_executor=..., output_executors=[...])`, يدير المخرجات المنظمة من خلال `default_options={"response_format": ...}`, ويستخدم إجابة مبرمجة لكي يعمل الدفتر بدون إشراف (بدون حظر `input()`).
- **تكوين البيئة** ([.env.example](../../.env.example)): تم تغيير أسماء نشر النماذج إلى `gpt-5-mini`; أُضيفت `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (توجيه الدرس 16) و `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` المفقودة سابقًا (استخدام المتصفح في الدرس 15).
- **التبعيات** ([requirements.txt](../../requirements.txt)): تثبيت الإصدار `~=1.10.0` لـ `agent-framework`, `agent-framework-foundry`, و `agent-framework-openai` لمجموعة متماسكة ومصادق عليها ذاتيًا (الإصدار 1.11.0 يطرح تغييرات كسرية تجريبية على الأسطح التي تستخدمها هذه الدروس).

### ملاحظات وقيود معروفة

- **تم التصديق على دفاتر بايثون في نشر حي لـ Microsoft Foundry.** تم تشغيل دفاتر بايثون بدون رأس باستخدام `nbconvert` على مشروع Microsoft Foundry باستخدام `gpt-5-mini` (و `gpt-5-nano` لتوجيه الدرس 16). قم بنشر نماذج معادلة غير متوقفة في مشروعك الخاص؛ تقرأ الدفاتر اسم النشر من `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **ما زالت بعض الدروس تتطلب موارد إضافية.** يحتاج الدرس 05 إلى Azure AI Search؛ ويتطلب سير عمل التأسيس من Bing في الدرس 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) اتصال Bing وأدوات خدمة وكيل Microsoft Foundry المستضافة؛ يحتاج الدرس 13 (Cognee) والدرس 17 (Foundry Local) إلى بيئات تشغيل خاصة بهما.

## [تم الإصدار] — 2026-07-13

يضيف هذا الإصدار درسين جديدين يُكملان مسار النشر — توسعة الوكلاء حتى Microsoft Foundry وتخفيضهم إلى محطة عمل واحدة — بالإضافة إلى خط أنابيب اختبار الدخان، تنقل محدث للدورة، مهارات جديدة للمتعلمين، وتحديث العلامة التجارية.

### أضيف

- **الدرس 16 — نشر وكلاء قابلين للتوسع باستخدام Microsoft Foundry.** درس جديد [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ودفتر قابل للتشغيل [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) يبني وكيل دعم العملاء للإنتاج (الأدوات، RAG، الذاكرة، توجيه النموذج، تخزين الرد، الموافقة البشرية، بوابة التقييم، وتتبع OpenTelemetry)، مع مخططات Mermaid للتطوير/النشر/التشغيل، اختبار معرفة، واجب، وتحدي.
- **الدرس 17 — إنشاء وكلاء ذكاء اصطناعي محليين باستخدام Foundry Local و Qwen.** درس جديد [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ودفتر [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) يبني مساعد هندسي كامل على الجهاز (استدعاء دالة Qwen عبر Foundry Local، أدوات ملفات معزولة، RAG محلي مع Chroma، MCP محلي اختياري)، مع مخططات خاصّة محلي/محلي-RAG/استدعاء أدوات، اختبار معرفة، واجب، وتحدي.
- **خط أنابيب اختبار الدخان.** تدفق عمل جديد [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) في [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) مع فهارس دروس تحت [tests/](./tests/README.md) للوكلاء القابلين للنشر في الدروس 01، 04، 05، و16، مع README لفهرس يربط كل فهرس بدروسه واسم الوكيل المستضاف. يكتسب الدرس 16 قسم "التحقق من وكيل نشر عبر اختبارات الدخان"؛ تكتسب الدروس 01/04/05 مؤشر اختبار دخان اختياري.
- **مهارات المتعلم.** مهارات وكلاء جديدة تحت `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (تغليف توجيهات الدرس 16 و17)، و [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (كيفية التحقق من صحة عينات الدفاتر مقابل إعداد حي لـ Microsoft Foundry / Azure OpenAI).
- **مشغل التحقق من الدفاتر.** جديد [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) ينفذ كل دفتر Python بدون رأس باستخدام `nbconvert` ويطبع مصفوفة نجاح/فشل (بالإضافة إلى `results.json`). يكتشف جذر المستودع وبايثون تلقائيًا، يستثني دفاتر غير الدورة (`.venv`، `site-packages`، `translations`، أصول قالب المهارة) ودفاتر `.NET` افتراضيًا، ويدعم `-Filter`، `-Timeout`، `-List`، `-IncludeDotnet`، و `-Python`.
- **تصفح الدورة.** أضيفت روابط درس سابق/التالي للدروس 11–15 (مفقودة سابقًا) بحيث تشكل كامل الدورة سلسلة من 00 → 18 في كلا الاتجاهين.
- **صور مصغرة جديدة.** صور مصغرة للدروس 16 و17، بالإضافة إلى صورة اجتماعية محدثة للمستودع [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (تُعلن الآن عن الدرسين الجديدين ورابط `aka.ms/ai-agents-beginners`).
- **التبعيات** ([requirements.txt](../../requirements.txt)): أضيف `foundry-local-sdk` و `chromadb` للدرس 17.

### تم التغيير

- **الجدول الرئيسي في [README.md](./README.md):** الدروس 16 و17 ترتبط بمحتواها الآن (كانت "قريبًا")؛ رفع صورة المستودع إلى `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** أضيفت الدروس 16 و17 إلى دليل الدرس تلو الآخر ومسارات التعلم، وقسم "تحقق من وكلاء نشرو باستخدام اختبارات الدخان".
- **[AGENTS.md](./AGENTS.md):** تم تحديث عدد الدروس/الوصف (00–18)، أضيف قسم تحقق اختبار الدخان، وأضيفت أمثلة تسمية عينات الدروس 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** "الدرس السابق" يشير الآن إلى الدرس 17 (كان الدرس 15)، مما يغلق السلسلة.
- **توحيد مراجع النماذج على النماذج غير المتوقفة.** تم استبدال جميع مراجع `gpt-4o` / `gpt-4o-mini` في الدورة (الوثائق، `.env.example`, دفاتر Python/.NET والعينات) بـ `gpt-4.1-mini` — إذ سيُوقف `gpt-4o` (جميع النسخ) في 2026. يحتفظ مثال توجيه النموذج في الدرس 16 بتباين صغير/كبير باستخدام `gpt-4.1-mini` (صغير) و `gpt-4.1` (كبير). تختار دفاتر بايثون الآن النموذج من متغيرات البيئة (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) بدلًا من ترميز اسم النموذج مباشرةً.

### ملاحظات وقيود معروفة

- **لم تُنفذ على Azure الحي.** دفاتر الدروس الجديدة تُعد عينات تعليمية؛ شغّلها وتحقق منها مقابل إعداد Microsoft Foundry / Foundry Local الخاص بك. يتطلب تدفق عمل اختبار الدخان نشر وكيل الدرس وتكوين أسرار Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) بدور **Azure AI User** على نطاق مشروع Foundry.
- **الدرس 17 محلي فقط.** لا يحتوي على نقطة استجابة Foundry، لذلك لا ينطبق إجراء اختبار الدخان؛ تحقق منه بتشغيل الدفتر على محطة العمل الخاصة بك.

## [تم الإصدار] — 2026-07-06

ينقل هذا الإصدار الدورة إلى **واجهة برمجة تطبيقات استجابات Azure OpenAI**، ويوحد تسميات المنتجات على **Microsoft Foundry** و **Microsoft Agent Framework (MAF)**، ويوقف نماذج GitHub، ويحدث إصدارات SDK، ويضيف محتوى جديدًا عن النماذج المحلية واستضافة أُطر عمل أخرى على Foundry.

### أضيف

- **مهارة الهجرة** — تم تثبيت مهارة وكيل [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (من [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) تحت `.agents/skills/`، بما في ذلك مراجعها ونص الماسح الضوئي.
- **Foundry Local (تشغيل النماذج على الجهاز)** — قسم جديد "مزود بديل: Foundry Local" في [00-course-setup/README.md](./00-course-setup/README.md) يغطي التثبيت (`winget` / `brew`)، `foundry model run`، الـ `foundry-local-sdk`, وربط `FoundryLocalManager` بإطار وكيل مايكروسوفت عبر `OpenAIChatClient`.
- **استضافة وكلاء LangChain / LangGraph على Microsoft Foundry** — قسم جديد في [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) مع عينة قابلة للتشغيل [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) تستخدم `langchain-azure-ai[hosting]` و `ResponsesHostServer` (بروتوكول `/responses`)، استنادًا إلى [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **مشروع مايكروسوفت أوبال** — قسم جديد "مثال واقعي: مشروع مايكروسوفت أوبال" في [15-browser-use/README.md](./15-browser-use/README.md) يؤطر أوبال كوكيل لاستخدام حاسوب المؤسسة ويربطه بمفاهيم الدورة (حلقة الإنسان، الثقة/الأمان، التخطيط، المهارات).
- **عينة بايثون ثانية للدرس 02** — إضافة [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (انظر "تم التغيير" — نُقلت من دفتر Semantic Kernel السابق) وربطها في README الدرس.
- **تم إضافة قسم النماذج والمزودين** إلى [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### تم التغيير

- **تحويل Chat Completions إلى Responses API (بايثون).** تم نقل العينات التي كانت تستدعي النموذج مباشرة إلى Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), باستخدام عميل `OpenAI` باتجاه نقطة النهاية المستقرة Azure OpenAI `/openai/v1/` (بدون `api_version`). العينات المتأثرة تشمل:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — شرح استدعاء الوظيفة الكامل (مخطط الأداة مسطح إلى تنسيق Responses، النتائج المعادة كـ `function_call_output`, `max_output_tokens`، إلخ).

- **نماذج GitHub → Azure OpenAI.** تم إيقاف نماذج GitHub (التقاعد في **يوليو 2026**) ولا تدعم API الاستجابات. تم تحويل جميع مسارات كود نماذج GitHub إلى Azure OpenAI / Microsoft Foundry عبر عينات Python و .NET:
  - بايثون: دفاتر عمل الدرس 08 (`01`–`03`)، الدرس 14 (`14-handoff`، `14-human-loop`، `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`، `07`، `08` `*-dotnet-agent-framework.cs` + وثائق مرافق `.md`، ودفاتر عمل مشروع الدرس 08 dotNET/`.md` (`01`–`03`) تستخدم الآن `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` مع `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** تم إعادة كتابة الملف السابق `02-semantic-kernel.ipynb` لاستخدام Microsoft Agent Framework مع Azure OpenAI (Responses API) وتمت إعادة تسميته إلى `02-python-agent-framework-azure-openai.ipynb`.
- **التوحيد على `FoundryChatClient` + `as_agent`.** README وكود الدفتر الذي أشار إلى `AzureAIProjectAgentProvider` تم توحيده بالأسلوب القياسي المستخدم في الدرس 01 وعينات الإطار نفسها: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` مع `provider.as_agent(...)`. تم التحديث عبر README ودفاتر العمل من الدرس 02 إلى 14 (مثلًا، ذاكرة الدرس 13، جميع دفاتر عمل الدرس 14، `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **تسمية المنتج.** تم إعادة تسميتها في المحتوى الإنجليزي:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (لم يتغير: "Azure OpenAI"، "Azure AI Search"، "Azure AI Inference"، وأسماء متغيرات البيئة.)
- **التبعيات** ([requirements.txt](../../requirements.txt)):
  - تثبيت `agent-framework>=1.10.0`، `agent-framework-foundry>=1.10.0`، `agent-framework-openai>=1.10.0`.
  - تثبيت `openai>=1.108.1` (الحد الأدنى لـ Responses API).
  - إزالة `azure-ai-inference` (تم استخدامه فقط في عينات نماذج GitHub التي تم نقلها).
- **تكوين البيئة** ([.env.example](../../.env.example)): تمت إزالة متغيرات نماذج GitHub (`GITHUB_TOKEN`، `GITHUB_ENDPOINT`، `GITHUB_MODEL_ID`); أُضيف `AZURE_OPENAI_ENDPOINT`، `AZURE_OPENAI_DEPLOYMENT`، ومفتاح API اختياري `AZURE_OPENAI_API_KEY`; تم تحديث التسمية إلى Microsoft Foundry.
- **الوثائق** — تم تحديث [00-course-setup/README.md](./00-course-setup/README.md)، [AGENTS.md](./AGENTS.md)، [README.md](./README.md)، و [STUDY_GUIDE.md](./STUDY_GUIDE.md) لما سبق (تكوين متغيرات البيئة، مقتطف التحقق، إرشادات المزود، التسمية).

### تم الإزالة

- خطوات الإعداد لموديلات GitHub ومتغيرات البيئة من وثائق الإعداد (تم استبدالها بـ Azure OpenAI / Microsoft Foundry).

### الأمان / الخصوصية (تنظيف المشاركة العامة)

- تم مسح مخرجات تنفيذ دفاتر جوبتر التي كشفت عن معرف اشتراك حقيقي **Azure**، أسماء مجموعات الموارد / الموارد، معرف اتصال Bing، بالإضافة إلى مسارات ملفات وأسماء مستخدمين محلية للمطورين، في:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- تم التأكد من عدم وجود مفاتيح API، رموز، معرفات اشتراك، أو مسارات شخصية في المحتوى الإنجليزي المتعقب (مراجع `GITHUB_TOKEN` المتبقية هي لمفتاح GitHub Actions في سير العمل ومفتاح PAT لخادم GitHub MCP في إعداد الدرس 11 — كلاهما شرعي وغير مرتبط بنماذج GitHub).

### ملاحظات وقيود معروفة

- **لم يتم التنفيذ/الترجمة.** هذه عينات تعليمية تم تحديثها لتصحيح API والتسمية؛ لم تُشغل ضد موارد Azure الحية، ولم تُترجم عينات .NET في هذا البيئة. يرجى التحقق مقابل نشر Microsoft Foundry / Azure OpenAI الخاص بك.
- **يجب أن يدعم نشر النموذج Responses API.** استخدم نشرًا مثل `gpt-4.1-mini`، `gpt-4.1`، أو نموذج `gpt-5.x`. النماذج الأقدم تدعم وظائف أساسية للاستجابات ولكن ليس كل الميزات.
- **نسخة إطار العمل الخاص بالوكيل.** العينات تستهدف أحدث MAF (`>=1.10.0`). نداء الإنشاء القياسي للوكيل هو `client.as_agent(...)`; تم التحقق من API مقابل وثائق الإطار المنشورة وبناء مثبت. إذا قمت بتثبيت نسخة مختلفة، تحقق من توفر الطريقة (`as_agent` مقابل `create_agent`).
- **دفتر عمل تدفق الدرس 08 رقم 04** يحتفظ عمدًا بـ `AzureAIAgentClient` (من `agent-framework-azure-ai`) لأنه يستخدم أدوات مستضافة من خدمة Microsoft Foundry Agent (تأسيس Bing، مفسر الكود)؛ وهو قائم على Responses API بالفعل.
- **نشر .NET الافتراضي.** عينتا عمل الدرس 08 dotNET كانتا مبرمجتين سابقًا بنموذج معين؛ الآن الافتراضي هو `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). إذا كان العينة تعتمد على إدخال متعدد الوسائط/رؤية، اضبط `AZURE_OPENAI_DEPLOYMENT` على نموذج مناسب.
- **Foundry Local** يعرض نقطة نهاية مكالمات دردشة متوافقة مع OpenAI وهو مخصص للتطوير المحلي؛ استخدم Azure OpenAI / Microsoft Foundry لمجموعة ميزات Responses API الكاملة.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->