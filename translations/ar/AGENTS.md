# AGENTS.md

## نظرة عامة على المشروع

يحتوي هذا المستودع على "وكلاء الذكاء الاصطناعي للمبتدئين" - دورة تعليمية شاملة تعلم كل ما تحتاجه لبناء وكلاء الذكاء الاصطناعي. تتكون الدورة من أكثر من 15 درسًا تغطي الأساسيات، أنماط التصميم، الأطر، ونشر الوكلاء في بيئة الإنتاج.

**التقنيات الرئيسية:**
- Python 3.12+
- دفاتر Jupyter للتعلم التفاعلي
- أطر الذكاء الاصطناعي: Semantic Kernel، AutoGen، Microsoft Agent Framework (MAF)
- خدمات Azure AI: Azure AI Foundry، Azure AI Agent Service
- سوق نماذج GitHub (متوفر مستوى مجاني)

**الهيكلية:**
- هيكلية تعتمد على الدروس (00-15+ مجلدات)
- يحتوي كل درس على: وثائق README، أمثلة على الأكواد (دفاتر Jupyter)، وصور
- دعم متعدد اللغات عبر نظام ترجمة تلقائي
- خيارات متعددة للأطر لكل درس (Semantic Kernel، AutoGen، Azure AI Agent Service)

## أوامر الإعداد

### المتطلبات الأساسية
- Python 3.12 أو أعلى
- حساب GitHub (لنماذج GitHub - المستوى المجاني)
- اشتراك Azure (اختياري، لخدمات Azure AI)

### الإعداد الأولي

1. **نسخ أو تفريع المستودع:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **إنشاء وتفعيل بيئة Python الافتراضية:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **تثبيت التبعيات:**
   ```bash
   pip install -r requirements.txt
   ```

4. **إعداد متغيرات البيئة:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### متغيرات البيئة المطلوبة

بالنسبة لـ **نماذج GitHub (مجانية)**:
- `GITHUB_TOKEN` - رمز الوصول الشخصي من GitHub

بالنسبة لـ **خدمات Azure AI** (اختياري):
- `PROJECT_ENDPOINT` - نقطة نهاية مشروع Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - مفتاح API لـ Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - عنوان URL لنقطة نهاية Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - اسم النشر لنموذج الدردشة
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - اسم النشر للتضمينات
- إعدادات إضافية لـ Azure كما هو موضح في `.env.example`

## سير العمل التطويري

### تشغيل دفاتر Jupyter

يحتوي كل درس على عدة دفاتر Jupyter لأطر مختلفة:

1. **تشغيل Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **انتقل إلى مجلد الدرس** (على سبيل المثال، `01-intro-to-ai-agents/code_samples/`)

3. **افتح وشغل الدفاتر:**
   - `*-semantic-kernel.ipynb` - باستخدام إطار Semantic Kernel
   - `*-autogen.ipynb` - باستخدام إطار AutoGen
   - `*-python-agent-framework.ipynb` - باستخدام إطار Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - باستخدام إطار Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - باستخدام خدمة Azure AI Agent

### العمل مع الأطر المختلفة

**Semantic Kernel + نماذج GitHub:**
- المستوى المجاني متوفر مع حساب GitHub
- جيد للتعلم والتجربة
- نمط الملف: `*-semantic-kernel*.ipynb`

**AutoGen + نماذج GitHub:**
- المستوى المجاني متوفر مع حساب GitHub
- قدرات تنسيق متعددة الوكلاء
- نمط الملف: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- أحدث إطار من Microsoft
- متوفر بـ Python و .NET
- نمط الملف: `*-agent-framework.ipynb`

**خدمة Azure AI Agent:**
- يتطلب اشتراك Azure
- ميزات جاهزة للإنتاج
- نمط الملف: `*-azureaiagent.ipynb`

## تعليمات الاختبار

هذا مستودع تعليمي يحتوي على أمثلة أكواد بدلاً من أكواد إنتاجية مع اختبارات تلقائية. للتحقق من إعدادك وتغييراتك:

### الاختبار اليدوي

1. **اختبر بيئة Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **اختبر تشغيل الدفاتر:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **تحقق من متغيرات البيئة:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### تشغيل الدفاتر الفردية

افتح الدفاتر في Jupyter ونفذ الخلايا بالتسلسل. كل دفتر مكتفٍ ذاتيًا ويشمل:
- عبارات الاستيراد
- تحميل الإعدادات
- تنفيذ أمثلة للوكلاء
- النتائج المتوقعة في خلايا Markdown

## أسلوب كتابة الأكواد

### اتفاقيات Python

- **إصدار Python**: 3.12+
- **أسلوب كتابة الأكواد**: اتباع معايير Python PEP 8
- **الدفاتر**: استخدام خلايا Markdown واضحة لشرح المفاهيم
- **الاستيرادات**: ترتيب حسب المكتبة القياسية، الطرف الثالث، الاستيرادات المحلية

### اتفاقيات دفاتر Jupyter

- تضمين خلايا Markdown وصفية قبل خلايا الأكواد
- إضافة أمثلة للنتائج في الدفاتر كمرجع
- استخدام أسماء متغيرات واضحة تتماشى مع مفاهيم الدرس
- الحفاظ على ترتيب تنفيذ الدفاتر خطيًا (خلية 1 → 2 → 3...)

### تنظيم الملفات

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## البناء والنشر

### بناء الوثائق

يستخدم هذا المستودع Markdown للوثائق:
- ملفات README.md في كل مجلد درس
- README.md الرئيسي في جذر المستودع
- نظام ترجمة تلقائي عبر GitHub Actions

### خط أنابيب CI/CD

موجود في `.github/workflows/`:

1. **co-op-translator.yml** - ترجمة تلقائية إلى أكثر من 50 لغة
2. **welcome-issue.yml** - الترحيب بمبدعي القضايا الجديدة
3. **welcome-pr.yml** - الترحيب بمساهمي طلبات السحب الجديدة

### النشر

هذا مستودع تعليمي - لا توجد عملية نشر. المستخدمون:
1. تفريع أو نسخ المستودع
2. تشغيل الدفاتر محليًا أو في GitHub Codespaces
3. التعلم من خلال تعديل وتجربة الأمثلة

## إرشادات طلب السحب

### قبل التقديم

1. **اختبر تغييراتك:**
   - شغل الدفاتر المتأثرة بالكامل
   - تحقق من أن جميع الخلايا تعمل بدون أخطاء
   - تأكد من أن النتائج مناسبة

2. **تحديث الوثائق:**
   - تحديث README.md إذا تمت إضافة مفاهيم جديدة
   - إضافة تعليقات في الدفاتر للأكواد المعقدة
   - ضمان أن خلايا Markdown تشرح الغرض

3. **تغييرات الملفات:**
   - تجنب الالتزام بملفات `.env` (استخدم `.env.example`)
   - لا تلتزم بمجلدات `venv/` أو `__pycache__/`
   - احتفظ بنتائج الدفاتر عندما توضح المفاهيم
   - إزالة الملفات المؤقتة ودفاتر النسخ الاحتياطي (`*-backup.ipynb`)

### تنسيق عنوان طلب السحب

استخدم عناوين وصفية:
- `[Lesson-XX] إضافة مثال جديد لـ <المفهوم>`
- `[Fix] تصحيح خطأ في README الدرس-XX`
- `[Update] تحسين مثال الكود في الدرس-XX`
- `[Docs] تحديث تعليمات الإعداد`

### الفحوصات المطلوبة

- يجب أن تعمل الدفاتر بدون أخطاء
- يجب أن تكون ملفات README واضحة ودقيقة
- اتباع أنماط الأكواد الموجودة في المستودع
- الحفاظ على التناسق مع الدروس الأخرى

## ملاحظات إضافية

### الأخطاء الشائعة

1. **عدم توافق إصدار Python:**
   - تأكد من استخدام Python 3.12+
   - قد لا تعمل بعض الحزم مع الإصدارات القديمة
   - استخدم `python3 -m venv` لتحديد إصدار Python بشكل صريح

2. **متغيرات البيئة:**
   - قم دائمًا بإنشاء `.env` من `.env.example`
   - لا تلتزم بملف `.env` (موجود في `.gitignore`)
   - يحتاج رمز GitHub إلى أذونات مناسبة

3. **تعارض الحزم:**
   - استخدم بيئة افتراضية جديدة
   - قم بالتثبيت من `requirements.txt` بدلاً من الحزم الفردية
   - قد تتطلب بعض الدفاتر حزم إضافية مذكورة في خلايا Markdown الخاصة بها

4. **خدمات Azure:**
   - تتطلب خدمات Azure AI اشتراكًا نشطًا
   - بعض الميزات خاصة بالمناطق
   - تنطبق قيود المستوى المجاني على نماذج GitHub

### مسار التعلم

التقدم الموصى به عبر الدروس:
1. **00-course-setup** - ابدأ هنا لإعداد البيئة
2. **01-intro-to-ai-agents** - فهم أساسيات وكلاء الذكاء الاصطناعي
3. **02-explore-agentic-frameworks** - تعلم حول الأطر المختلفة
4. **03-agentic-design-patterns** - أنماط التصميم الأساسية
5. استمر عبر الدروس المرقمة بالتسلسل

### اختيار الإطار

اختر الإطار بناءً على أهدافك:
- **التعلم/النمذجة**: Semantic Kernel + نماذج GitHub (مجانية)
- **أنظمة متعددة الوكلاء**: AutoGen
- **أحدث الميزات**: Microsoft Agent Framework (MAF)
- **نشر الإنتاج**: Azure AI Agent Service

### الحصول على المساعدة

- انضم إلى [مجتمع Azure AI Foundry على Discord](https://aka.ms/ai-agents/discord)
- راجع ملفات README الخاصة بالدروس للحصول على إرشادات محددة
- تحقق من [README.md الرئيسي](./README.md) للحصول على نظرة عامة على الدورة
- راجع [إعداد الدورة](./00-course-setup/README.md) للحصول على تعليمات إعداد مفصلة

### المساهمة

هذا مشروع تعليمي مفتوح. مرحب بالمساهمات:
- تحسين أمثلة الأكواد
- تصحيح الأخطاء أو الأخطاء المطبعية
- إضافة تعليقات توضيحية
- اقتراح مواضيع دروس جديدة
- الترجمة إلى لغات إضافية

راجع [قضايا GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) للاحتياجات الحالية.

## سياق خاص بالمشروع

### دعم متعدد اللغات

يستخدم هذا المستودع نظام ترجمة تلقائي:
- دعم لأكثر من 50 لغة
- الترجمات في مجلدات `/translations/<lang-code>/`
- يقوم GitHub Actions بتحديث الترجمات
- الملفات المصدرية باللغة الإنجليزية في جذر المستودع

### هيكلية الدروس

يتبع كل درس نمطًا ثابتًا:
1. صورة مصغرة للفيديو مع رابط
2. محتوى الدرس المكتوب (README.md)
3. أمثلة الأكواد في أطر متعددة
4. أهداف التعلم والمتطلبات الأساسية
5. موارد تعلم إضافية مرتبطة

### تسمية أمثلة الأكواد

النمط: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - الدرس 4، Semantic Kernel
- `07-autogen.ipynb` - الدرس 7، AutoGen
- `14-python-agent-framework.ipynb` - الدرس 14، MAF Python
- `14-dotnet-agent-framework.ipynb` - الدرس 14، MAF .NET

### المجلدات الخاصة

- `translated_images/` - صور مترجمة للترجمات
- `images/` - الصور الأصلية للمحتوى الإنجليزي
- `.devcontainer/` - إعدادات حاوية التطوير لـ VS Code
- `.github/` - قوالب وإجراءات GitHub Actions

### التبعيات

الحزم الرئيسية من `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - إطار AutoGen
- `semantic-kernel` - إطار Semantic Kernel
- `agent-framework` - إطار Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - خدمات Azure AI
- `azure-search-documents` - تكامل بحث Azure AI
- `chromadb` - قاعدة بيانات متجهة لأمثلة RAG
- `chainlit` - إطار واجهة المستخدم للدردشة
- `browser_use` - أتمتة المتصفح للوكلاء
- `mcp[cli]` - دعم بروتوكول سياق النموذج
- `mem0ai` - إدارة الذاكرة للوكلاء

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.