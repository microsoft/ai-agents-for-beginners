# سجل التغييرات

تم توثيق جميع التغييرات الجديرة بالذكر في دورة **الوكلاء الذكاء الاصطناعي للمبتدئين** في هذا الملف.

## [تم الإصدار] — 2026-07-13

يضيف هذا الإصدار درسين جديدين يكملا قوس النشر — توسيع الوكلاء باستخدام Microsoft Foundry وتقليصهم إلى محطة عمل واحدة — بالإضافة إلى سير عمل اختبار دخان، وتجديد التنقل في الدورة، ومهارات جديدة للمتعلمين، وتحديث العلامة التجارية.

### تمت الإضافة

- **الدرس 16 — نشر وكلاء قابلين للتوسع باستخدام Microsoft Foundry.** درس جديد [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ودفتر تفاعلي قابل للتشغيل [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) يبني وكيل دعم العملاء الإنتاجي (الأدوات، RAG، الذاكرة، توجيه النموذج، تخزين الاستجابة مؤقتًا، الموافقة البشرية، بوابة التقييم، وتتبع OpenTelemetry)، مع مخططات Mermaid للتطوير / النشر / وقت التشغيل، تحقق من المعرفة، مهمة، وتحدي.
- **الدرس 17 — إنشاء وكلاء ذكاء اصطناعي محليين باستخدام Foundry Local و Qwen.** درس جديد [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ودفتر تفاعلي [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) يبني مساعد هندسي يعمل بالكامل على الجهاز (استدعاء الوظيفة Qwen عبر Foundry Local، أدوات ملفات في بيئة محمية، RAG محلي مع Chroma، MCP محلي اختياري)، مع مخططات محلية فقط / RAG محلي / استدعاء الأدوات، تحقق من المعرفة، مهمة، وتحدي.
- **سير عمل اختبار الدخان.** سير عمل جديد [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) بالإضافة إلى فهارس لكل درس تحت [tests/](./tests/README.md) للوكلاء القابلين للنشر في الدروس 01، 04، 05، و16، مع ملف README فهرسي يربط كل فهرس بدروسه واسم الوكيل المستضاف. يضيف الدرس 16 قسم "التحقق من وكيل منشور باختبارات الدخان"؛ وتضيف الدروس 01/04/05 مؤشر اختبار دخان اختياري.
- **مهارات المتعلم.** مهارات وكلاء جديدة تحت `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md)، [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (تجميع إرشادات الدرس 16 و 17)، و [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (كيفية التحقق من صحة عينات الدفاتر مقابل إعداد Microsoft Foundry / Azure OpenAI مباشر).
- **مشغل التحقق من الدفاتر التفاعلية.** ملف جديد [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) ينفذ كل دفتر Python تلقائيًا باستخدام `nbconvert` ويطبع مصفوفة نجاح / فشل (بالإضافة إلى `results.json`). يكتشف تلقائيًا جذر المستودع وبيئة Python، يستثني دفاتر غير الدورة (`.venv`، `site-packages`، `translations`، أصول قالب المهارة) ودفاتر `.NET` بشكل افتراضي، ويدعم `-Filter`، `-Timeout`، `-List`، `-IncludeDotnet`، و `-Python`.
- **تنقل الدورة.** تمت إضافة روابط الدرس السابق / التالي للدروس 11–15 (كانت مفقودة سابقًا) بحيث تربط الدورة بأكملها من 00 إلى 18 في كلا الاتجاهين.
- **مصغرات جديدة.** صور مصغرة للدروس 16 و 17، بالإضافة إلى صورة اجتماعية محدثة للمستودع [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (تعلن الآن عن الدرسين الجديدين ورابط `aka.ms/ai-agents-beginners`).
- **التبعيات** ([requirements.txt](../../requirements.txt)): أضيفت `foundry-local-sdk` و `chromadb` للدرس 17.

### تم التغيير

- **جدول الدروس الرئيسي في [README.md](./README.md)**: الآن يربط الدروس 16 و 17 بمحتواها (كان "قريبًا" سابقًا)؛ وتم تحديث صورة المستودع إلى `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: أضيفت الدروس 16 و 17 إلى دليل الدروس ومسارات التعلم، وقسم "التحقق من الوكلاء المنشورين باختبارات الدخان".
- **[AGENTS.md](./AGENTS.md)**: تم تحديث عدد الدروس / وصفها (00–18)، إضافة قسم تحقق اختبار الدخان، وأمثلة تسمية عينات الدروس 16 و 17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "الدرس السابق" الآن يشير إلى الدرس 17 (كان الدرس 15)، مكتمل سلسلة الدروس.
- **توحد مراجع النماذج على النماذج غير المتقادمة.** استبدلت جميع مراجع `gpt-4o` / `gpt-4o-mini` في الدورة (الوثائق، `.env.example`، دفاتر وعينات Python/.NET) بـ `gpt-4.1-mini` — حيث سيتم إيقاف `gpt-4o` (جميع الإصدارات) في 2026. يحافظ مثال توجيه النموذج في الدرس 16 على التباين الصغير/الكبير باستخدام `gpt-4.1-mini` (صغير) و `gpt-4.1` (كبير). تختار دفاتر Python الآن النموذج من متغيرات البيئة (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) بدلاً من تحديد اسم النموذج مباشرةً.

### ملاحظات وقيود معروفة

- **لم تُنفذ ضد Azure مباشر.** دفاتر الدروس الجديدة هي عينات تعليمية؛ شغّلها وحقق من صحتها باستخدام إعداد Microsoft Foundry / Foundry Local الخاص بك. يتطلب سير عمل اختبار الدخان نشر وكيل الدرس وتكوين أسرار Azure OIDC (`AZURE_CLIENT_ID`، `AZURE_TENANT_ID`، `AZURE_SUBSCRIPTION_ID`) بدور **Azure AI User** على نطاق مشروع Foundry.
- **الدرس 17 محلي فقط.** لا يحتوي على نقطة نهاية Foundry Responses، لذا لا ينطبق إجراء اختبار الدخان؛ تحقق منه بتشغيل الدفتر على محطة العمل الخاصة بك.

## [تم الإصدار] — 2026-07-06

ينقل هذا الإصدار الدورة إلى **واجهة برمجة تطبيقات استجابات Azure OpenAI**، يوحّد تسمية المنتج على **Microsoft Foundry** و **إطار عمل الوكلاء من مايكروسوفت (MAF)**، يتوقف عن استخدام نماذج GitHub، يحدث إصدارات SDK، ويضيف محتوى جديد عن النماذج المحلية واستضافة أطر عمل أخرى على Foundry.

### تمت الإضافة

- **مهارة الهجرة** — تم تثبيت مهارة الوكيل [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (من [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) تحت `.agents/skills/`، بما في ذلك مراجعها وسكريبت الفحص.
- **Foundry Local (تشغيل النماذج على الجهاز)** — قسم جديد "مزود بديل: Foundry Local" في [00-course-setup/README.md](./00-course-setup/README.md) يغطي التثبيت (`winget` / `brew`)، `foundry model run`، `foundry-local-sdk`، وربط `FoundryLocalManager` بإطار عمل الوكلاء من مايكروسوفت عبر `OpenAIChatClient`.
- **استضافة وكلاء LangChain / LangGraph على Microsoft Foundry** — قسم جديد في [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) بالإضافة إلى عينة قابلة للتشغيل [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) باستخدام `langchain-azure-ai[hosting]` و `ResponsesHostServer` (بروتوكول `/responses`)، بناءً على [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **مشروع Opal من مايكروسوفت** — قسم جديد "مثال من العالم الحقيقي: مشروع Opal من مايكروسوفت" في [15-browser-use/README.md](./15-browser-use/README.md) يصور Opal كوagent استخدام حاسوب مؤسسي ويربطه بمفاهيم الدورة (البشر في الحلقة، الثقة / الأمان، التخطيط، المهارات).
- **عينة ثانية لدرس 02 بلغة Python** — أضيف [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (انظر "تم التغيير" — تم النقل من دفتر Semantic Kernel السابق) وربطها في README الدرس.
- تم إضافة قسم النماذج والمزودين إلى [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### تم التغيير

- **إكمالات الدردشة → واجهة برمجة استجابات (Python).** تم نقل العينات التي استدعت النموذج مباشرة من إكمالات الدردشة إلى واجهة برمجة استجابات (`client.responses.create(input=..., store=False)`, `resp.output_text`)، باستخدام العميل `OpenAI` ضد نقطة نهاية Azure OpenAI المستقرة `/openai/v1/` (بدون `api_version`). تشمل العينات المتأثرة:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — شرح كامل لاستدعاء الدالة (مخطط الأداة مسطح إلى تنسيق Responses، نتائج الأداة معادة كـ `function_call_output`, `max_output_tokens`، إلخ).
- **نماذج GitHub → Azure OpenAI.** تم إيقاف نماذج GitHub (تتوقف في **يوليو 2026**) ولا تدعم واجهة برمجة استجابات API. تم تحويل جميع مسارات كود نماذج GitHub إلى Azure OpenAI / Microsoft Foundry عبر عينات Python و .NET:
  - بايثون: دفاتر سير العمل الدرس 08 (`01`–`03`)، الدرس 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`، `07`، `08` ملفات `*-dotnet-agent-framework.cs` + الوثائق المصاحبة `.md`، ودفاتر سير عمل الدرس 08 dotNET / `.md` (`01`–`03`) تستخدم الآن `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` مع `AzureCliCredential`.
- **Semantic Kernel → إطار عمل الوكلاء من مايكروسوفت.** تم إعادة كتابة الدفتر `02-semantic-kernel.ipynb` لاستخدام إطار عمل الوكلاء من مايكروسوفت مع Azure OpenAI (واجهات استجابة API) وتم إعادة تسميته إلى `02-python-agent-framework-azure-openai.ipynb`.
- **موحد على `FoundryChatClient` + `as_agent`.** README وكود الدفاتر التي كانت تشير إلى `AzureAIProjectAgentProvider` تم توحيدها على النمط الرسمي المستخدم في الدرس 01 والعينات الخاصة بالإطار: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` مع `provider.as_agent(...)`. تم تحديثها عبر README و دفاتر الدروس 02–14 (مثلاً، ذاكرة الدرس 13، جميع دفاتر الدرس 14، `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **تسمية المنتج.** تم إعادة التسمية عبر محتوى اللغة الإنجليزية:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **خدمة وكلاء Microsoft Foundry**
  - (ثابتة: "Azure OpenAI"، "Azure AI Search"، "Azure AI Inference"، وأسماء متغيرات البيئة.)
- **التبعيات** ([requirements.txt](../../requirements.txt)):
  - تم تثبيت `agent-framework>=1.10.0`، `agent-framework-foundry>=1.10.0`، `agent-framework-openai>=1.10.0`.
  - تم تثبيت `openai>=1.108.1` (الحد الأدنى لواجهة برمجة استجابات API).
  - أزيل `azure-ai-inference` (كان يُستخدم فقط في عينات نماذج GitHub المُحول).
- **تكوين البيئة** ([.env.example](../../.env.example)): أزيلت متغيرات نماذج GitHub (`GITHUB_TOKEN`، `GITHUB_ENDPOINT`، `GITHUB_MODEL_ID`); أضيفت `AZURE_OPENAI_ENDPOINT`، `AZURE_OPENAI_DEPLOYMENT`، ومفتاح API اختياري `AZURE_OPENAI_API_KEY`; وتم تحديث التسمية إلى Microsoft Foundry.
- **الوثائق** — تم تحديث [00-course-setup/README.md](./00-course-setup/README.md)، [AGENTS.md](./AGENTS.md)، [README.md](./README.md)، و [STUDY_GUIDE.md](./STUDY_GUIDE.md) للمواضيع السابقة (تثبيت متغيرات البيئة، مقتطف التحقق، توجيه المزود، التسميات).

### تمت الإزالة

- خطوات بدء استخدام نماذج GitHub ومتغيرات البيئة من وثائق الإعداد (تم استبدالها بـ Azure OpenAI / Microsoft Foundry).

### الأمان / الخصوصية (تنظيف المشاركة العامة)

- تم مسح مخرجات تنفيذ دفاتر Jupyter التي كشفت عن **معرف اشتراك Azure** الحقيقي، أسماء مجموعات الموارد / الموارد، ومعرف اتصال Bing، بالإضافة إلى **مسارات ملفات المستخدمين المحليين وأسماء المستخدمين** في:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- تم التحقق من عدم وجود مفاتيح API أو رموز أو معرفات اشتراك أو مسارات شخصية في المحتوى الإنجليزي المتعقّب (المرجع لـ `GITHUB_TOKEN` المتبقي هو رمز إجراءات GitHub في سير العمل وPAT الخاص بخادم MCP لـ GitHub في إعداد الدرس 11 — كلاهما شرعي وغير مرتبط بنماذج GitHub).

### ملاحظات وقيود معروفة

- **لم تُنفّذ / تُجمّع.** هذه عينات تعليمية محدثة للدقة في أسماء وواجهة برمجة التطبيقات؛ لم تُشغّل على موارد Azure حية، ولم تُجمع عينات .NET في هذه البيئة. تحقق من صحتها مقابل نشر Microsoft Foundry / Azure OpenAI الخاص بك.
- **يجب أن تدعم نشر النموذج واجهة برمجة تطبيقات Responses.** استخدم نشرًا مثل `gpt-4.1-mini`، `gpt-4.1`، أو نموذج `gpt-5.x`. النماذج الأقدم تدعم الوظائف الأساسية لـ Responses ولكن ليس كل الميزات.
- **إصدار إطار العمل الوكيل.** تستهدف العينات أحدث إصدار من MAF (`>=1.10.0`). تستدعي الطريقة النموذجية لإنشاء وكيل `client.as_agent(...)`; تم التحقق من APIs مقابل الوثائق المنشورة للإطار وبناء مثبت. إذا أرفقت إصدارًا مختلفًا، تحقق من توفر الطريقة (`as_agent` مقابل `create_agent`).
- **دفتر عمل سير العمل الدرس 08 رقم 04** يحتفظ عمدًا بـ `AzureAIAgentClient` (من `agent-framework-azure-ai`) لأنه يستخدم أدوات خدمة وكيل Microsoft Foundry المستضافة (تعزيز Bing، مفسر الكود)؛ وهو قائم بالفعل على Responses.
- **نشر .NET الافتراضي.** عينتان لسير عمل dotNET في الدرس 08 كانا يحددان نموذجًا معينًا بشكل صارم؛ أصبحا الآن يستندان افتراضيًا إلى `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). إذا اعتمدت عينة على إدخال متعدد الأوضاع / الرؤية، عيّن `AZURE_OPENAI_DEPLOYMENT` إلى نموذج مناسب.
- **Foundry Local** يعرض نقطة نهاية **استكمالات الدردشة** متوافقة مع OpenAI وهو مخصص للتطوير المحلي؛ استخدم Azure OpenAI / Microsoft Foundry لمجموعة ميزات واجهة برمجة تطبيقات Responses الكاملة.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->