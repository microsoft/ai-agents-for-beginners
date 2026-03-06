# إعداد الدورة

## مقدمة

ستغطي هذه الدرس كيفية تشغيل أمثلة الشيفرة الخاصة بهذه الدورة.

## انضم إلى متعلّمين آخرين واحصل على المساعدة

قبل أن تبدأ في استنساخ المستودع الخاص بك، انضم إلى قناة [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) للحصول على أي مساعدة في الإعداد، أو لأي أسئلة حول الدورة، أو للتواصل مع متعلّمين آخرين.

## استنساخ أو تفريع (Fork) هذا المستودع

لبدء العمل، يرجى استنساخ أو تفريع مستودع GitHub. سيمنحك ذلك نسخة خاصة بك من مواد الدورة حتى تتمكن من تشغيل الشيفرة واختبارها وتعديلها!

يمكنك القيام بذلك بالنقر على الرابط إلى <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">تفريع المستودع</a>

يجب أن يكون لديك الآن نسختك المفروعة من هذه الدورة في الرابط التالي:

![مستودع مُنسخ](../../../translated_images/ar/forked-repo.33f27ca1901baa6a.webp)

### استنساخ سطحي (مُوصى به للعملية / Codespaces)

  >المستودع الكامل قد يكون كبيرًا (~3 جيجابايت) عند تنزيل كامل التاريخ وكل الملفات. إذا كنت تحضر الورشة فقط أو تحتاج إلى بعض مجلدات الدروس فقط، فإن الاستنساخ السطحي (أو الاستنساخ المتناثر) يتجنّب معظم هذا التنزيل عن طريق تقصير التاريخ و/أو تجاوز الكتل.

#### استنساخ سطحي سريع — تاريخ أدنى، كل الملفات

استبدل `<your-username>` في الأوامر أدناه بعنوان URL الخاص بتفريع المستودع لديك (أو عنوان upstream إذا فضّلت).

لاستنساخ تاريخ الالتزامات الأخير فقط (تنزيل صغير):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

لاستنساخ فرع محدد:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### استنساخ جزئي (sparse) — كتل أقل + المجلدات المُختارة فقط

يستخدم هذا الاستنساخ الجزئي وميزة sparse-checkout (يتطلب Git 2.25+ ويُوصى باستخدام Git حديث بدعم partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ادخل إلى مجلد المستودع:

```bash|powershell
cd ai-agents-for-beginners
```

ثم حدد المجلدات التي تريدها (المثال أدناه يظهر مجلدين):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

بعد الاستنساخ والتحقق من الملفات، إذا كنت تحتاج فقط إلى الملفات وتريد تحرير المساحة (بدون تاريخ git)، يرجى حذف بيانات تعريف المستودع (💀غير قابل للعكس — ستفقد كل وظائف Git: لا التزامات، ولا سحب، ولا دفع، ولا الوصول إلى التاريخ).

```bash
# zsh/باش
rm -rf .git
```

```powershell
# باورشيل
Remove-Item -Recurse -Force .git
```

#### استخدام GitHub Codespaces (مُوصى به لتجنّب التنزيلات الكبيرة محليًا)

- أنشئ Codespace جديدًا لهذا المستودع عبر [GitHub UI](https://github.com/codespaces).  

- في الطرفية (terminal) الخاصة بالـ Codespace الذي أنشأته مؤخرًا، نفّذ أحد أوامر الاستنساخ السطحي/المتناثر أعلاه لإحضار مجلدات الدروس التي تحتاجها فقط إلى مساحة عمل الـ Codespace.
- اختياري: بعد الاستنساخ داخل Codespaces، احذف .git لاستعادة مساحة إضافية (انظر أوامر الإزالة أعلاه).
- ملاحظة: إذا فضّلت فتح المستودع مباشرة في Codespaces (دون استنساخ إضافي)، فاعلم أن Codespaces سيبني بيئة devcontainer وقد يزود المزيد مما تحتاجه. استنساخ نسخة سطحية داخل Codespace جديد يمنحك مزيدًا من التحكم في استخدام القرص.

#### نصائح

- استبدل دائمًا عنوان URL الخاص بالاستنساخ بعنوان fork الخاص بك إذا أردت التعديل/الالتزام.
- إذا احتجت لاحقًا إلى مزيد من التاريخ أو الملفات، يمكنك جلبها أو ضبط sparse-checkout لتضمين مجلدات إضافية.

## تشغيل الشيفرة

تقدّم هذه الدورة سلسلة من دفاتر Jupyter (Jupyter Notebooks) التي يمكنك تشغيلها للحصول على تجربة عملية في بناء وكلاء الذكاء الاصطناعي.

تستخدم أمثلة الشيفرة **Microsoft Agent Framework (MAF)** مع الـ `AzureAIProjectAgentProvider`، الذي يتصل بـ **Azure AI Agent Service V2** (واجهة Responses API) عبر **Microsoft Foundry**.

كل دفاتر Python معنونة بـ `*-python-agent-framework.ipynb`.

## المتطلبات

- Python 3.12+
  - **ملاحظة**: إذا لم تكن قد ثبّتت Python 3.12، تأكد من تثبيتها. ثم أنشئ بيئة افتراضية (venv) باستخدام python3.12 لضمان تثبيت الإصدارات الصحيحة من ملف requirements.txt.
  
    >مثال

    أنشئ مجلد بيئة Python الافتراضية:

    ```bash|powershell
    python -m venv venv
    ```

    ثم فعّل البيئة الافتراضية لـ:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: لأمثلة الشيفرة التي تستخدم .NET، تأكد من تثبيت [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) أو أحدث. ثم تحقق من إصدار .NET SDK المثبت لديك:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — مطلوب للمصادقة. ثبّت من [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **اشتراك Azure** — للوصول إلى Microsoft Foundry وخدمة Azure AI Agent.
- **مشروع Microsoft Foundry** — مشروع يحتوي على نموذج منشور (مثلاً `gpt-4o`). انظر [الخطوة 1](../../../00-course-setup) أدناه.

قمنا بتضمين ملف `requirements.txt` في جذر هذا المستودع يحتوي على جميع حزم Python المطلوبة لتشغيل أمثلة الشيفرة.

يمكنك تثبيتها بتشغيل الأمر التالي في الطرفية في جذر المستودع:

```bash|powershell
pip install -r requirements.txt
```

نوصي بإنشاء بيئة افتراضية Python لتجنّب أي تعارضات أو مشاكل.

## إعداد VSCode

تأكد من أنك تستخدم إصدار Python الصحيح في VSCode.

![صورة](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## إعداد Microsoft Foundry وخدمة Azure AI Agent

### الخطوة 1: إنشاء مشروع Microsoft Foundry

تحتاج إلى **hub** و**project** في Azure AI Foundry مع نموذج منشور لتشغيل دفاتر الملاحظات.

1. انتقل إلى [ai.azure.com](https://ai.azure.com) وسجّل الدخول باستخدام حساب Azure الخاص بك.
2. أنشئ **hub** (أو استخدم واحدًا موجودًا). انظر: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. داخل الـ hub، أنشئ **project**.
4. انشر نموذجًا (مثلاً `gpt-4o`) من **Models + Endpoints** → **Deploy model**.

### الخطوة 2: استرجاع نقطة نهاية المشروع واسم نشر النموذج

من مشروعك في بوابة Microsoft Foundry:

- **Project Endpoint** — اذهب إلى صفحة **Overview** وانسخ عنوان URL الخاص بالنقطة النهائية.

![Project Connection String](../../../translated_images/ar/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — اذهب إلى **Models + Endpoints**، اختر النموذج المنشور لديك، ولاحظ **Deployment name** (مثلاً `gpt-4o`).

### الخطوة 3: تسجيل الدخول إلى Azure باستخدام `az login`

تستخدم كل دفاتر الملاحظات **`AzureCliCredential`** للمصادقة — لا توجد مفاتيح API لإدارتها. هذا يتطلب أن تكون مسجّلًا عبر Azure CLI.

1. **ثبّت Azure CLI** إذا لم تكن قد فعلت ذلك بالفعل: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **سجّل الدخول** بتشغيل:

    ```bash|powershell
    az login
    ```

    أو إذا كنت في بيئة بعيدة/Codespace بدون متصفح:

    ```bash|powershell
    az login --use-device-code
    ```

3. **اختر اشتراكك** إذا طُلب — اختر الاشتراك الذي يحتوي مشروع Foundry الخاص بك.

4. **تحقق** من أنك مسجّل الدخول:

    ```bash|powershell
    az account show
    ```

> **لماذا `az login`؟** دفاتر الملاحظات تقوم بالمصادقة باستخدام `AzureCliCredential` من حزمة `azure-identity`. هذا يعني أن جلسة Azure CLI الخاصة بك توفّر بيانات الاعتماد — لا مفاتيح API أو أسرار في ملف `.env` الخاص بك. هذه [أفضل ممارسة أمنية](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### الخطوة 4: أنشئ ملف `.env` الخاص بك

انسخ ملف المثال:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# باور شيل
Copy-Item .env.example .env
```

افتح `.env` واملأ هاتين القيمتين:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | بوابة Foundry → مشروعك → صفحة **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | بوابة Foundry → **Models + Endpoints** → اسم النموذج المنشور لديك |

هذا كل شيء لمعظم الدروس! ستقوم دفاتر الملاحظات بالمصادقة تلقائيًا عبر جلستك في `az login`.

### الخطوة 5: تثبيت تبعيات Python

```bash|powershell
pip install -r requirements.txt
```

نوصي بتشغيل هذا داخل البيئة الافتراضية التي أنشأتها سابقًا.

## إعداد إضافي للدرس 5 (Agentic RAG)

يستخدم الدرس 5 **Azure AI Search** للتوليد المدعوم بالاسترجاع. إذا خططت لتشغيل ذلك الدرس، أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | بوابة Azure → مورد **Azure AI Search** الخاص بك → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | بوابة Azure → مورد **Azure AI Search** الخاص بك → **Settings** → **Keys** → المفتاح الإداري الأساسي |

## إعداد إضافي للدرس 6 والدرس 8 (نماذج GitHub)

بعض دفاتر الملاحظات في الدرسين 6 و 8 تستخدم **GitHub Models** بدلًا من Azure AI Foundry. إذا خططت لتشغيل تلك الأمثلة، أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | استخدم `https://models.inference.ai.azure.com` (القيمة الافتراضية) |
| `GITHUB_MODEL_ID` | اسم النموذج المستخدم (مثلاً `gpt-4o-mini`) |

## إعداد إضافي للدرس 8 (تدفق عمل Bing Grounding)

دفتر العمل الشرطي في الدرس 8 يستخدم **Bing grounding** عبر Azure AI Foundry. إذا خططت لتشغيل ذلك المثال، أضف هذا المتغير إلى ملف `.env` الخاص بك:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | بوابة Azure AI Foundry → مشروعك → **Management** → **Connected resources** → اتصال Bing الخاص بك → انسخ معرف الاتصال |

## استكشاف الأخطاء وإصلاحها

### أخطاء التحقق من شهادة SSL على macOS

إذا كنت تستخدم macOS وواجهت خطأ مثل:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

هذه مشكلة معروفة مع Python على macOS حيث أن شهادات SSL الخاصة بالنظام لا تُوثّق تلقائيًا. جرّب الحلول التالية بالترتيب:

**الخيار 1: شغّل سكربت تثبيت الشهادات الخاص بـ Python (مُستحسن)**

```bash
# استبدل 3.XX بإصدار بايثون المثبت لديك (مثل 3.12 أو 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**الخيار 2: استخدم `connection_verify=False` في دفتر الملاحظات الخاص بك (لدفاتر ملاحظات نماذج GitHub فقط)**

في دفتر الملاحظات للدرس 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)، يوجد حل بديل معلق بالفعل. قم بإلغاء تعليق `connection_verify=False` عند إنشاء العميل:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # عطّل التحقق من SSL إذا واجهت أخطاء في الشهادة
)
```

> **⚠️ تحذير:** تعطيل التحقق من SSL (`connection_verify=False`) يقلل من الأمان بتجاوز التحقق من الشهادات. استخدم هذا كحل مؤقت فقط في بيئات التطوير، وليس في الإنتاج.

**الخيار 3: تثبيت واستخدام `truststore`**

```bash
pip install truststore
```

ثم أضف ما يلي في أعلى دفتر الملاحظات أو الشيفرة قبل إجراء أي اتصالات شبكية:

```python
import truststore
truststore.inject_into_ssl()
```

## علقت في مكان ما؟

إذا واجهت أي مشاكل في تشغيل هذا الإعداد، انضم إلى <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> أو <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">أنشئ مشكلة (issue)</a>.

## الدرس التالي

أنت الآن جاهز لتشغيل شيفرة هذه الدورة. نتمنى لك تعلمًا ممتعًا أكثر عن عالم وكلاء الذكاء الاصطناعي! 

[مقدمة إلى وكلاء الذكاء الاصطناعي وحالات استخدام الوكلاء](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية:**
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الحرجة، يُنصح بالاستعانة بترجمة بشرية احترافية. لسنا مسؤولين عن أي سوء فهم أو تفسير ينشأ عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->