<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:29:39+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ar"
}
-->
# إعداد الدورة

## المقدمة

ستتناول هذه الدرس كيفية تشغيل نماذج الكود الخاصة بهذه الدورة.

## انضم إلى المتعلمين الآخرين واحصل على المساعدة

قبل أن تبدأ في استنساخ المستودع الخاص بك، انضم إلى [قناة Discord الخاصة بـ AI Agents للمبتدئين](https://aka.ms/ai-agents/discord) للحصول على أي مساعدة في الإعداد، أو للإجابة على أي أسئلة حول الدورة، أو للتواصل مع المتعلمين الآخرين.

## استنساخ أو نسخ هذا المستودع

للبدء، يرجى استنساخ أو نسخ مستودع GitHub. سيتيح لك ذلك إنشاء نسخة خاصة بك من مواد الدورة لتتمكن من تشغيل واختبار وتعديل الكود!

يمكنك القيام بذلك بالنقر على الرابط <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">لنسخ المستودع</a>

يجب أن يكون لديك الآن نسخة مخصصة من هذه الدورة في الرابط التالي:

![المستودع المنسوخ](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.ar.png)

### استنساخ سطحي (موصى به للورش / Codespaces)

  > يمكن أن يكون المستودع الكامل كبيرًا (~3 جيجابايت) عند تنزيل التاريخ الكامل وجميع الملفات. إذا كنت تحضر ورشة عمل فقط أو تحتاج فقط إلى بعض مجلدات الدروس، فإن الاستنساخ السطحي (أو الاستنساخ الجزئي) يتجنب معظم هذا التنزيل عن طريق تقليص التاريخ و/أو تخطي الكتل.

#### استنساخ سطحي سريع — تاريخ محدود، جميع الملفات

استبدل `<your-username>` في الأوامر أدناه بعنوان URL الخاص بنسختك (أو عنوان URL الأصلي إذا كنت تفضل ذلك).

للاستنساخ مع تاريخ آخر التزام فقط (تنزيل صغير):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

للاستنساخ فرع معين:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### استنساخ جزئي (Sparse) — كتل بيانات محدودة + مجلدات مختارة فقط

يستخدم الاستنساخ الجزئي والتفريغ الانتقائي (يتطلب Git 2.25+ ويوصى باستخدام Git الحديث مع دعم الاستنساخ الجزئي):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

انتقل إلى مجلد المستودع:

لـ bash:

```bash
cd ai-agents-for-beginners
```

لـ Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

ثم حدد المجلدات التي تريدها (المثال أدناه يظهر مجلدين):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

بعد الاستنساخ والتحقق من الملفات، إذا كنت بحاجة فقط إلى الملفات وترغب في توفير مساحة (بدون تاريخ Git)، يرجى حذف بيانات المستودع (💀 لا يمكن التراجع عنها — ستفقد جميع وظائف Git: لا توجد التزامات، سحب، دفع، أو الوصول إلى التاريخ).

لـ Linux/macOS:

```bash
rm -rf .git
```

لـ Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### استخدام GitHub Codespaces (موصى به لتجنب التنزيلات المحلية الكبيرة)

- قم بإنشاء Codespace جديد لهذا المستودع عبر [واجهة GitHub](https://github.com/codespaces).  

- في نافذة الأوامر الخاصة بـ Codespace الذي تم إنشاؤه حديثًا، قم بتشغيل أحد أوامر الاستنساخ السطحي/الجزئي المذكورة أعلاه لجلب فقط مجلدات الدروس التي تحتاجها إلى مساحة عمل Codespace.
- اختياري: بعد الاستنساخ داخل Codespaces، قم بإزالة .git لاستعادة مساحة إضافية (راجع أوامر الإزالة أعلاه).
- ملاحظة: إذا كنت تفضل فتح المستودع مباشرة في Codespaces (دون استنساخ إضافي)، كن على علم بأن Codespaces ستقوم بإنشاء بيئة devcontainer وقد توفر أكثر مما تحتاج. يتيح لك استنساخ نسخة سطحية داخل Codespace جديد التحكم بشكل أكبر في استخدام القرص.

#### نصائح

- استبدل دائمًا عنوان URL للاستنساخ بنسختك إذا كنت تريد التعديل/الالتزام.
- إذا كنت بحاجة لاحقًا إلى المزيد من التاريخ أو الملفات، يمكنك جلبها أو تعديل التفريغ الانتقائي لتضمين مجلدات إضافية.

## تشغيل الكود

تقدم هذه الدورة سلسلة من دفاتر Jupyter التي يمكنك تشغيلها للحصول على تجربة عملية في بناء وكلاء الذكاء الاصطناعي.

تستخدم نماذج الكود إما:

**يتطلب حساب GitHub - مجاني**:

1) إطار عمل Semantic Kernel Agent + سوق النماذج في GitHub. مُسمى بـ (semantic-kernel.ipynb)
2) إطار عمل AutoGen + سوق النماذج في GitHub. مُسمى بـ (autogen.ipynb)

**يتطلب اشتراك Azure**:
3) Azure AI Foundry + خدمة Azure AI Agent. مُسمى بـ (azureaiagent.ipynb)

نشجعك على تجربة جميع أنواع الأمثلة الثلاثة لمعرفة أيها يناسبك بشكل أفضل.

أيًا كان الخيار الذي تختاره، فإنه سيحدد خطوات الإعداد التي تحتاج إلى اتباعها أدناه:

## المتطلبات

- Python 3.12+
  - **ملاحظة**: إذا لم يكن لديك Python3.12 مثبتًا، تأكد من تثبيته. ثم قم بإنشاء بيئة venv باستخدام python3.12 لضمان تثبيت الإصدارات الصحيحة من ملف requirements.txt.
  
    >مثال

    إنشاء دليل بيئة Python venv:

    ``` bash
    python3 -m venv venv
    ```

    ثم قم بتنشيط بيئة venv لـ:

    macOS و Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- حساب GitHub - للوصول إلى سوق النماذج في GitHub
- اشتراك Azure - للوصول إلى Azure AI Foundry
- حساب Azure AI Foundry - للوصول إلى خدمة Azure AI Agent

لقد قمنا بتضمين ملف `requirements.txt` في جذر هذا المستودع يحتوي على جميع حزم Python المطلوبة لتشغيل نماذج الكود.

يمكنك تثبيتها عن طريق تشغيل الأمر التالي في نافذة الأوامر في جذر المستودع:

```bash
pip install -r requirements.txt
```

نوصي بإنشاء بيئة Python افتراضية لتجنب أي تعارضات أو مشاكل.

## إعداد VSCode
تأكد من أنك تستخدم الإصدار الصحيح من Python في VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## إعداد النماذج باستخدام سوق GitHub 

### الخطوة 1: استرجاع رمز الوصول الشخصي الخاص بـ GitHub (PAT)

تستخدم هذه الدورة سوق النماذج في GitHub، مما يوفر وصولًا مجانيًا إلى نماذج اللغة الكبيرة (LLMs) التي ستستخدمها لبناء وكلاء الذكاء الاصطناعي.

لاستخدام نماذج GitHub، ستحتاج إلى إنشاء [رمز الوصول الشخصي لـ GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

يمكنك القيام بذلك عن طريق الذهاب إلى <a href="https://github.com/settings/personal-access-tokens" target="_blank">إعدادات رموز الوصول الشخصي</a> في حساب GitHub الخاص بك.

يرجى اتباع [مبدأ أقل امتياز](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) عند إنشاء الرمز. هذا يعني أنه يجب عليك فقط منح الرمز الأذونات التي يحتاجها لتشغيل نماذج الكود في هذه الدورة.

1. اختر خيار `Fine-grained tokens` على الجانب الأيسر من الشاشة بالانتقال إلى **إعدادات المطور**
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.ar.png)

    ثم اختر `Generate new token`.

    ![إنشاء رمز](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.ar.png)

2. أدخل اسمًا وصفيًا للرمز يعكس الغرض منه، مما يسهل التعرف عليه لاحقًا.


    🔐 توصية مدة صلاحية الرمز

    المدة الموصى بها: 30 يومًا
    للحصول على وضع أمني أكثر أمانًا، يمكنك اختيار فترة أقصر — مثل 7 أيام 🛡️
    إنها طريقة رائعة لتحديد هدف شخصي وإكمال الدورة بينما تكون في ذروة حماسك للتعلم 🚀.

    ![اسم الرمز وتاريخ انتهاء الصلاحية](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.ar.png)

3. قم بتحديد نطاق الرمز ليشمل نسختك من هذا المستودع فقط.

    ![تحديد النطاق لنسخة المستودع](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.ar.png)

4. قم بتقييد أذونات الرمز: ضمن علامة التبويب **Permissions**، انقر فوق زر "+ Add permissions". ستظهر قائمة منسدلة. يرجى البحث عن **Models** وتحديد المربع الخاص بها.
    ![إضافة إذن النماذج](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.ar.png)

5. تحقق من الأذونات المطلوبة قبل إنشاء الرمز. ![التحقق من الأذونات](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.ar.png)

6. قبل إنشاء الرمز، تأكد من أنك مستعد لتخزين الرمز في مكان آمن مثل خزنة مدير كلمات المرور، حيث لن يتم عرضه مرة أخرى بعد إنشائه. ![تخزين الرمز بأمان](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.ar.png)

انسخ الرمز الجديد الذي قمت بإنشائه للتو. ستقوم الآن بإضافته إلى ملف `.env` المضمن في هذه الدورة.


### الخطوة 2: إنشاء ملف `.env` الخاص بك

لإنشاء ملف `.env`، قم بتشغيل الأمر التالي في نافذة الأوامر.

```bash
cp .env.example .env
```

سيقوم هذا بنسخ ملف المثال وإنشاء ملف `.env` في دليلك حيث يمكنك ملء القيم للمتغيرات البيئية.

بعد نسخ الرمز، افتح ملف `.env` في محرر النصوص المفضل لديك والصق الرمز في حقل `GITHUB_TOKEN`.
![حقل رمز GitHub](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.ar.png)


يجب أن تكون الآن قادرًا على تشغيل نماذج الكود الخاصة بهذه الدورة.

## إعداد النماذج باستخدام Azure AI Foundry وخدمة Azure AI Agent

### الخطوة 1: استرجاع نقطة نهاية مشروع Azure الخاص بك

اتبع الخطوات لإنشاء مركز ومشروع في Azure AI Foundry الموجودة هنا: [نظرة عامة على موارد المركز](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

بمجرد إنشاء مشروعك، ستحتاج إلى استرجاع سلسلة الاتصال الخاصة بمشروعك.

يمكن القيام بذلك عن طريق الذهاب إلى صفحة **نظرة عامة** لمشروعك في بوابة Azure AI Foundry.

![سلسلة اتصال المشروع](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.ar.png)

### الخطوة 2: إنشاء ملف `.env` الخاص بك

لإنشاء ملف `.env`، قم بتشغيل الأمر التالي في نافذة الأوامر.

```bash
cp .env.example .env
```

سيقوم هذا بنسخ ملف المثال وإنشاء ملف `.env` في دليلك حيث يمكنك ملء القيم للمتغيرات البيئية.

بعد نسخ الرمز، افتح ملف `.env` في محرر النصوص المفضل لديك والصق الرمز في حقل `PROJECT_ENDPOINT`.

### الخطوة 3: تسجيل الدخول إلى Azure

كأفضل ممارسة أمان، سنستخدم [المصادقة بدون مفتاح](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) للمصادقة على Azure OpenAI باستخدام Microsoft Entra ID.

بعد ذلك، افتح نافذة الأوامر وقم بتشغيل `az login --use-device-code` لتسجيل الدخول إلى حساب Azure الخاص بك.

بمجرد تسجيل الدخول، اختر اشتراكك في نافذة الأوامر.


## متغيرات البيئة الإضافية - Azure Search و Azure OpenAI 

بالنسبة لدرس Agentic RAG - الدرس الخامس - هناك نماذج تستخدم Azure Search و Azure OpenAI.

إذا كنت ترغب في تشغيل هذه النماذج، ستحتاج إلى إضافة المتغيرات البيئية التالية إلى ملف `.env` الخاص بك:

### صفحة النظرة العامة (المشروع)

- `AZURE_SUBSCRIPTION_ID` - تحقق من **تفاصيل المشروع** في صفحة **النظرة العامة** لمشروعك.

- `AZURE_AI_PROJECT_NAME` - انظر أعلى صفحة **النظرة العامة** لمشروعك.

- `AZURE_OPENAI_SERVICE` - ابحث عن هذا في علامة التبويب **القدرات المضمنة** لخدمة **Azure OpenAI** في صفحة **النظرة العامة**.

### مركز الإدارة

- `AZURE_OPENAI_RESOURCE_GROUP` - انتقل إلى **خصائص المشروع** في صفحة **النظرة العامة** لمركز الإدارة.

- `GLOBAL_LLM_SERVICE` - ضمن **الموارد المتصلة**، ابحث عن اسم اتصال **خدمات Azure AI**. إذا لم يكن مدرجًا، تحقق من **بوابة Azure** ضمن مجموعة الموارد الخاصة بك للحصول على اسم مورد خدمات الذكاء الاصطناعي.

### صفحة النماذج + نقاط النهاية

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - اختر نموذج التضمين الخاص بك (مثل `text-embedding-ada-002`) ولاحظ **اسم النشر** من تفاصيل النموذج.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - اختر نموذج الدردشة الخاص بك (مثل `gpt-4o-mini`) ولاحظ **اسم النشر** من تفاصيل النموذج.

### بوابة Azure

- `AZURE_OPENAI_ENDPOINT` - ابحث عن **خدمات Azure AI**، انقر عليها، ثم انتقل إلى **إدارة الموارد**، **المفاتيح ونقطة النهاية**، وانتقل لأسفل إلى "نقاط نهاية Azure OpenAI"، ونسخ النقطة التي تقول "واجهات برمجة التطبيقات اللغوية".

- `AZURE_OPENAI_API_KEY` - من نفس الشاشة، انسخ المفتاح 1 أو المفتاح 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - ابحث عن مورد **Azure AI Search** الخاص بك، انقر عليه، وشاهد **النظرة العامة**.

- `AZURE_SEARCH_API_KEY` - ثم انتقل إلى **الإعدادات** ثم **المفاتيح** لنسخ المفتاح الإداري الأساسي أو الثانوي.

### صفحة ويب خارجية

- `AZURE_OPENAI_API_VERSION` - قم بزيارة صفحة [دورة حياة إصدار API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) ضمن **الإصدار الأخير من API GA**.

### إعداد المصادقة بدون مفتاح

بدلاً من كتابة بيانات الاعتماد الخاصة بك، سنستخدم اتصالًا بدون مفتاح مع Azure OpenAI. للقيام بذلك، سنقوم باستيراد `DefaultAzureCredential` ثم استدعاء وظيفة `DefaultAzureCredential` للحصول على بيانات الاعتماد.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## هل واجهت مشكلة؟
إذا واجهت أي مشاكل أثناء تشغيل هذا الإعداد، انضم إلى <a href="https://discord.gg/kzRShWzttr" target="_blank">مجتمع Azure AI على Discord</a> أو <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">قم بإنشاء مشكلة</a>.

## الدرس التالي

أنت الآن جاهز لتشغيل الكود الخاص بهذه الدورة. نتمنى لك تعلمًا ممتعًا عن عالم وكلاء الذكاء الاصطناعي!

[مقدمة عن وكلاء الذكاء الاصطناعي وحالات استخدامهم](../01-intro-to-ai-agents/README.md)

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.