# AGENTS.md

## نظرة عامة على المشروع

يحتوي هذا المستودع على "وكلاء الذكاء الاصطناعي للمبتدئين" - دورة تعليمية شاملة تعلم كل ما يلزم لبناء وكلاء الذكاء الاصطناعي. تتكون الدورة من 18 درساً (مرقمة 00-18) تغطي الأساسيات، وأنماط التصميم، وأُطُر العمل، ونشر الإنتاج، والوكلاء المحليين / على الجهاز، وأمن وكلاء الذكاء الاصطناعي.

**التقنيات الرئيسية:**
- بايثون 3.12+
- دفاتر جوبتر للتعلم التفاعلي
- أُطُر الذكاء الاصطناعي: Microsoft Agent Framework (MAF)
- خدمات Azure AI: Microsoft Foundry، Microsoft Foundry Agent Service V2

**الهيكلية:**
- هيكلية تعتمد على الدروس (00-15+ مجلدات)
- يحتوي كل درس على: توثيق README، أمثلة برمجية (دفاتر جوبتر)، وصور
- دعم متعدد اللغات عبر نظام ترجمة آلي
- دفتر بايثون واحد لكل درس باستخدام Microsoft Agent Framework

## أوامر الإعداد

### المتطلبات الأساسية
- بايثون 3.12 أو أعلى
- اشتراك Azure (لـ Microsoft Foundry)
- مثبت ومصادق Azure CLI (`az login`)

### الإعداد الأولي

1. **استنساخ أو تفريع المستودع:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # أو
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **إنشاء وتفعيل بيئة بايثون الافتراضية:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # على ويندوز: venv\Scripts\activate
   ```

3. **تثبيت التبعيات:**
   ```bash
   pip install -r requirements.txt
   ```

4. **إعداد متغيرات البيئة:**
   ```bash
   cp .env.example .env
   # حرر ملف .env باستخدام مفاتيح API ونقاط النهاية الخاصة بك
   ```

### متغيرات البيئة المطلوبة

لـ **Microsoft Foundry** (مطلوب):
- `AZURE_AI_PROJECT_ENDPOINT` - نقطة نهاية مشروع Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - اسم نشر النموذج (مثلاً: gpt-4.1-mini)

لـ **Azure AI Search** (الدرس 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - نقطة نهاية Azure AI Search
- `AZURE_SEARCH_API_KEY` - مفتاح API لـ Azure AI Search

المصادقة: نفذ `az login` قبل تشغيل دفاتر جوبتر (يستخدم `AzureCliCredential`).

## سير العمل للتطوير

### تشغيل دفاتر جوبتر

يحتوي كل درس على دفاتر جوبتر متعددة لأُطُر مختلفة:

1. **ابدأ Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **انتقل إلى مجلد درس** (مثلاً: `01-intro-to-ai-agents/code_samples/`)

3. **افتح وشغّل الدفاتر:**
   - `*-python-agent-framework.ipynb` - باستخدام Microsoft Agent Framework (بايثون)
   - `*-dotnet-agent-framework.ipynb` - باستخدام Microsoft Agent Framework (.NET)

### العمل مع Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- يتطلب اشتراك Azure
- يستخدم `FoundryChatClient` لخدمة Agent Service V2 (الوكلاء ظاهرون في بوابة Foundry)
- جاهز للإنتاج مع مفعّل الرصد المدمج
- نمط الملف: `*-python-agent-framework.ipynb`

## تعليمات الاختبار

هذا مستودع تعليمي يحتوي على أمثلة برمجية وليس شفرة إنتاج مع اختبارات آلية. للتحقق من الإعداد والتغييرات:

### الاختبار اليدوي

1. **اختبر بيئة بايثون:**
   ```bash
   python --version  # يجب أن يكون 3.12 أو أعلى
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **اختبر تنفيذ دفتر جوبتر:**
   ```bash
   # تحويل الدفتر إلى سكريبت وتشغيله (اختبار الاستيرادات)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **تحقق من متغيرات البيئة:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### تشغيل دفاتر فردية

افتح الدفاتر في Jupyter ونفذ الخلايا بالتسلسل. كل دفتر مستقل ويشمل:
- عبارات الاستيراد
- تحميل الإعدادات
- تطبيقات مثال لوكيل
- المخرجات المتوقعة في خلايا ماركداون

### اختبار أولي للوكلاء المنشورين

في الدروس التي يُنشر فيها الوكيل كوكيل مستضاف من Microsoft Foundry (01، 04، 05، 16)، يحتوي المستودع على كتالوجات اختبار أولي تحت مجلد `tests/` التي يديرها سير العمل `.github/workflows/smoke-test.yml` عبر إجراء [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). هذه بوابة خفيفة بعد النشر (هل الوكيل قابل للوصول ويتبع توقعات المطالبات الأساسية؟)، تكمل مسار التقييم في الدروس 10 و16. راجع [tests/README.md](./tests/README.md) لخريطة الكتالوج إلى الدرس إلى الوكيل. الدرس 17 يعمل محلياً مع Foundry Local ولا يمتلك نقطة نهاية مستضافة، لذا يتم التحقق منه بتشغيل دفتريه مباشرة.

## نمط البرمجة

### قواعد بايثون

- **إصدار بايثون**: 3.12+
- **نمط الشفرة**: اتبع قواعد PEP 8 القياسية في بايثون
- **دفاتر جوبتر**: استخدم خلايا ماركداون واضحة لشرح المفاهيم
- **الاستيرادات**: اجمع حسب مكتبة قياسية، طرف ثالث، ومحلية

### قواعد دفاتر جوبتر

- إدراج خلايا وصفية ماركداون قبل خلايا الكود
- أضف أمثلة نواتج في الدفاتر كمرجع
- استخدم أسماء متغيرات واضحة توافق مفاهيم الدرس
- حافظ على ترتيب تنفيذ الدفتر خطي (خلية 1 → 2 → 3 ...)

### تنظيم الملفات

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## البناء والنشر

### بناء التوثيق

يستخدم هذا المستودع Markdown للتوثيق:
- ملفات README.md في كل مجلد درس
- README.md الرئيسي في جذر المستودع
- نظام ترجمة آلي عبر GitHub Actions

### خط أنابيب CI/CD

يقع في `.github/workflows/`:

1. **co-op-translator.yml** - الترجمة الآلية إلى أكثر من 50 لغة
2. **welcome-issue.yml** - يرحب بمنشئي القضايا الجديدة
3. **welcome-pr.yml** - يرحب بالمساهمين في طلبات السحب الجديدة

### النشر

هذا مستودع تعليمي - لا توجد عملية نشر. المستخدمون:
1. يفّرعون أو يستنسخون المستودع
2. يشغلون الدفاتر محلياً أو في GitHub Codespaces
3. يتعلمون من خلال تعديل وتجارِب الأمثلة

## إرشادات طلب السحب

### قبل الإرسال

1. **اختبر تغييراتك:**
   - شغّل الدفاتر المتأثرة بالكامل
   - تحقق من تنفيذ جميع الخلايا بدون أخطاء
   - افحص أن المخرجات مناسبة

2. **تحديث التوثيق:**
   - حدث README.md إذا أضفت مفاهيم جديدة
   - أضف تعليقات في الدفاتر للكود المعقد
   - تأكد أن خلايا الماركداون تشرح الغرض

3. **تغييرات الملفات:**
   - تجنب الالتزام بملفات `.env` (استخدم `.env.example`)
   - لا تلتزم بمجلدات `venv/` أو `__pycache__/`
   - احتفظ بمخرجات الدفاتر عندما توضح المفاهيم
   - احذف الملفات المؤقتة ونسخ النسخ الاحتياطية للدفاتر (`*-backup.ipynb`)

### صيغة عنوان طلب السحب

استخدم عناوين وصفية:
- `[Lesson-XX] أضف مثال جديد لـ <concept>`
- `[Fix] صحح خطأ مطبعي في README الخاص بالدرس-XX`
- `[Update] حسن مثال الشفرة في الدرس-XX`
- `[Docs] حدث تعليمات الإعداد`

### الفحوصات المطلوبة

- الدفاتر يجب أن تنفذ بدون أخطاء
- ملفات README يجب أن تكون واضحة ودقيقة
- اتبع أنماط الشفرة الموجودة في المستودع
- حافظ على التناسق مع الدروس الأخرى

## ملاحظات إضافية

### مشكلات شائعة

1. **تعارض إصدار بايثون:**
   - تأكد من استخدام بايثون 3.12+
   - قد لا تعمل بعض الحزم مع الإصدارات الأقدم
   - استخدم `python3 -m venv` لتحديد إصدار بايثون صراحة

2. **متغيرات البيئة:**
   - دائماً أنشئ ملف `.env` انطلاقاً من `.env.example`
   - لا تلتزم بملف `.env` (موجود في `.gitignore`)
   - سجّل الدخول باستخدام `az login` للمصادقة بدون مفاتيح عبر Entra ID

3. **تعارض الحزم:**
   - استخدم بيئة افتراضية جديدة
   - ثبّت من `requirements.txt` بدلاً من الحزم الفردية
   - قد تحتاج بعض الدفاتر إلى حزم إضافية مذكورة في خلايا الماركداون الخاصة بها

4. **خدمات Azure:**
   - خدمات Azure AI تتطلب اشتراكاً فعالاً
   - بعض الميزات خاصة بمناطق جغرافية معينة
   - تأكد من أن نشر نموذج Azure OpenAI يدعم واجهة برمجة التطبيقات Responses API

### مسار التعلم

التدرج الموصى به عبر الدروس:
1. **00-course-setup** - ابدأ هنا لإعداد البيئة
2. **01-intro-to-ai-agents** - افهم أساسيات وكلاء الذكاء الاصطناعي
3. **02-explore-agentic-frameworks** - تعرّف على أُطُر العمل المختلفة
4. **03-agentic-design-patterns** - أنماط التصميم الأساسية
5. استمر في الدروس المرقمة بالتسلسل

### اختيار الأُطُر

اختر الإطار بناءً على أهدافك:
- **جميع الدروس**: Microsoft Agent Framework (MAF) مع `FoundryChatClient`
- **يتم تسجيل الوكلاء على الخادم** في Microsoft Foundry Agent Service V2 وهم ظاهرون في بوابة Foundry

### الحصول على المساعدة

- انضم إلى [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- راجع ملفات README الخاصة بالدروس للتوجيه المحدد
- تحقق من [README.md](./README.md) الرئيسي لنظرة عامة على الدورة
- ارجع إلى [Course Setup](./00-course-setup/README.md) للحصول على تعليمات الإعداد التفصيلية

### المساهمة

هذا مشروع تعليمي مفتوح. المساهمات مرحب بها:
- تحسين أمثلة الشفرة
- تصحيح الأخطاء أو الطباعة
- إضافة تعليقات توضيحية
- اقتراح مواضيع دروس جديدة
- الترجمة إلى لغات إضافية

راجع [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) للاحتياجات الحالية.

## سياق خاص بالمشروع

### دعم متعدد اللغات

يستخدم هذا المستودع نظام ترجمة آلي:
- يدعم أكثر من 50 لغة
- الترجمات في مجلدات `/translations/<lang-code>/`
- سير عمل GitHub Actions يدير تحديثات الترجمة
- ملفات المصدر بالإنجليزية في جذر المستودع

### هيكلية الدرس

يتبع كل درس نمطاً متسقاً:
1. صورة مصغرة للفيديو مع رابط
2. محتوى الدرس المكتوب (README.md)
3. أمثلة البرمجة في أُطُر متعددة
4. أهداف التعلم والمتطلبات المسبقة
5. موارد إضافية للتعلم مرتبطة

### تسمية أمثلة الشفرة

الصيغة: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - الدرس 1، MAF بايثون
- `14-sequential.ipynb` - الدرس 14، أنماط متقدمة في MAF
- `16-python-agent-framework.ipynb` - الدرس 16، وكيل دعم العملاء في الإنتاج
- `17-local-agent-foundry-local.ipynb` - الدرس 17، وكيل محلي مع Foundry Local + Qwen

### مجلدات خاصة

- `translated_images/` - صور مترجمة
- `images/` - صور أصلية للمحتوى الإنجليزي
- `.devcontainer/` - إعداد حاوية تطوير VS Code
- `.github/` - سير عمل وقوالب GitHub Actions

### التبعيات

الحزم الرئيسية من `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - دعم بروتوكول Agent-to-Agent
- `azure-ai-inference`، `azure-ai-projects` - خدمات Azure AI
- `azure-identity` - مصادقة Azure (AzureCliCredential)
- `azure-search-documents` - تكامل Azure AI Search
- `mcp[cli]` - دعم Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->