# إعداد الدورة

## مقدمة

ستغطي هذه الدرس كيفية تشغيل عينات الشيفرة لهذه الدورة.

## انضم إلى المتعلمين الآخرين واحصل على المساعدة

قبل أن تبدأ في استنساخ مستودعك، انضم إلى قناة [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) للحصول على أي مساعدة في الإعداد، أو لأي أسئلة حول الدورة، أو للتواصل مع متعلمين آخرين.

## استنساخ أو عمل Fork لهذا المستودع

لبدء، يرجى استنساخ أو عمل fork لمستودع GitHub. سيجعل هذا نسختك الخاصة من مواد الدورة حتى تتمكن من تشغيل، اختبار، وتعديل الشيفرة!

يمكن تنفيذ ذلك من خلال النقر على الرابط إلى <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">استنساخ المستودع</a>

يجب أن يكون لديك الآن نسختك المنسوخة من هذه الدورة في الرابط التالي:

![Forked Repo](../../../translated_images/ar/forked-repo.33f27ca1901baa6a.webp)

### استنساخ سطحي (موصى به للورشة / Codespaces)

  >المستودع الكامل يمكن أن يكون كبيرًا (~3 GB) عند تنزيل السجل الكامل وجميع الملفات. إذا كنت تحضر الورشة فقط أو تحتاج فقط إلى بعض مجلدات الدروس، فإن الاستنساخ السطحي (أو الاستنساخ الجزئي) يتجنب معظم هذا التنزيل عن طريق تقصير التاريخ و/أو تخطي البلوكات.

#### استنساخ سطحي سريع — تاريخ محدود، جميع الملفات

استبدل `<your-username>` في الأوامر أدناه بعنوان URL الخاص بفوركك (أو عنوان URL upstream إذا فضلت).

للاستنساخ فقط سجل الالتزامات الأخير (تنزيل صغير):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

لاستنساخ فرع محدد:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### استنساخ جزئي (sparse) — بلوكات قليلة + مجلدات محددة فقط

هذا يستخدم الاستنساخ الجزئي وsparse-checkout (يتطلب Git 2.25+ ويُنصح باستخدام Git حديث بدعم الاستنساخ الجزئي):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

انتقل إلى مجلد المستودع:

```bash|powershell
cd ai-agents-for-beginners
```

ثم حدد المجلدات التي تريدها (المثال أدناه يظهر مجلدين):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

بعد الاستنساخ والتحقق من الملفات، إذا كنت تحتاج فقط إلى الملفات وتريد تحرير مساحة (بدون سجل git)، يرجى حذف بيانات تعريف المستودع (💀غير قابل للعكس — ستفقد كل وظائف Git: لا امتدادات، لا سحب، لا دفع، ولا وصول للسجل).

```bash
# زي إس إتش/باش
rm -rf .git
```

```powershell
# باورشيل
Remove-Item -Recurse -Force .git
```

#### استخدام GitHub Codespaces (موصى به لتجنب التنزيلات الكبيرة محليًا)

- أنشئ Codespace جديد لهذا المستودع عبر [GitHub UI](https://github.com/codespaces).  

- في طرفية الـ Codespace المنشأ حديثًا، نفذ أحد أوامر الاستنساخ السطحي/الجزئي أعلاه لجلب مجلدات الدروس التي تحتاجها فقط إلى مساحة عمل الـ Codespace.
- اختياري: بعد الاستنساخ داخل Codespaces، احذف .git لاسترداد مساحة إضافية (انظر أوامر الحذف أعلاه).
- ملاحظة: إذا فضلت فتح المستودع مباشرة في Codespaces (بدون استنساخ إضافي)، فكن على علم أن Codespaces سيبني بيئة devcontainer وقد يوفر موارد أكثر مما تحتاج. استنساخ نسخة سطحية داخل Codespace جديد يمنحك تحكمًا أفضل في استخدام القرص.

#### نصائح

- استبدل دائمًا عنوان URL للاستنساخ بفوركك إذا أردت التحرير/الالتزام.
- إذا احتجت لاحقًا إلى مزيد من التاريخ أو الملفات، يمكنك جلبها أو ضبط sparse-checkout لتضمين مجلدات إضافية.

## تشغيل الشيفرة

تقدم هذه الدورة سلسلة من دفاتر Jupyter التي يمكنك تشغيلها للحصول على تجربة عملية في بناء وكلاء الذكاء الاصطناعي.

تستخدم عينات الشيفرة **Microsoft Agent Framework (MAF)** مع `AzureAIProjectAgentProvider`، الذي يتصل بـ **Azure AI Agent Service V2** (واجهة Responses API) عبر **Microsoft Foundry**.

كل دفاتر Python تحمل التصنيف `*-python-agent-framework.ipynb`.

## المتطلبات

- Python 3.12+
  - **ملاحظة**: إذا لم تكن مثبتًا Python3.12، تأكد من تثبيته. ثم أنشئ بيئة venv باستخدام python3.12 لضمان تثبيت الإصدارات الصحيحة من ملف requirements.txt.
  
    >مثال

    أنشئ دليل Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    ثم فعّل بيئة venv لـ:

    ```bash
    # zsh/باش
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: بالنسبة لأمثلة الشيفرة التي تستخدم .NET، تأكد من تثبيت [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) أو أحدث. ثم تحقق من إصدار .NET SDK المثبت:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — مطلوب للمصادقة. ثبّت من [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **اشتراك Azure** — للوصول إلى Microsoft Foundry وAzure AI Agent Service.
- **مشروع Microsoft Foundry** — مشروع يحتوي على نموذج منشور (مثلاً `gpt-4o`). انظر [الخطوة 1](../../../00-course-setup) أدناه.

لقد أدرجنا ملف `requirements.txt` في جذر هذا المستودع والذي يحتوي على جميع حزم Python المطلوبة لتشغيل عينات الشيفرة.

يمكنك تثبيتها بتشغيل الأمر التالي في الطرفية في جذر المستودع:

```bash|powershell
pip install -r requirements.txt
```

نوصي بإنشاء بيئة افتراضية Python لتجنب أي تعارضات ومشكلات.

## إعداد VSCode

تأكد من أنك تستخدم إصدار Python الصحيح في VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## إعداد Microsoft Foundry وAzure AI Agent Service

### الخطوة 1: إنشاء مشروع Microsoft Foundry

تحتاج إلى **hub** و**مشروع** في Azure AI Foundry مع نموذج منشور لتشغيل دفاتر الملاحظات.

1. انتقل إلى [ai.azure.com](https://ai.azure.com) وقم بتسجيل الدخول بحساب Azure الخاص بك.
2. أنشئ **hub** (أو استخدم واحدًا قائمًا). راجع: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. داخل الـ hub، أنشئ **مشروعًا**.
4. انشر نموذجًا (مثلاً `gpt-4o`) من **Models + Endpoints** → **Deploy model**.

### الخطوة 2: استرداد نقطة نهاية مشروعك واسم نشر النموذج

من مشروعك في بوابة Microsoft Foundry:

- **Project Endpoint** — انتقل إلى صفحة **Overview** ونسخ عنوان URL لنقطة النهاية.

![Project Connection String](../../../translated_images/ar/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — انتقل إلى **Models + Endpoints**، اختر النموذج المنشور، ودوّن **Deployment name** (مثلاً `gpt-4o`).

### الخطوة 3: تسجيل الدخول إلى Azure باستخدام `az login`

تستخدم جميع دفاتر الملاحظات **`AzureCliCredential`** للمصادقة — لا مفاتيح API لإدارتها. هذا يتطلب أن تكون مسجلاً عبر Azure CLI.

1. **ثبّت Azure CLI** إذا لم تكن قد فعلت ذلك بالفعل: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **سجّل الدخول** بتشغيل:

    ```bash|powershell
    az login
    ```

    أو إذا كنت في بيئة بعيدة/Codepace بدون متصفح:

    ```bash|powershell
    az login --use-device-code
    ```

3. **اختر اشتراكك** إذا طُلب — اختر الاشتراك الذي يحتوي على مشروع Foundry الخاص بك.

4. **تحقق** من أنك مسجّل الدخول:

    ```bash|powershell
    az account show
    ```

> **لماذا `az login`؟** تقوم دفاتر الملاحظات بالمصادقة باستخدام `AzureCliCredential` من حزمة `azure-identity`. هذا يعني أن جلسة Azure CLI الخاصة بك توفر بيانات الاعتماد — لا مفاتيح API أو أسرار في ملف `.env` الخاص بك. هذه [أفضل ممارسة أمنية](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### الخطوة 4: إنشاء ملف `.env` الخاص بك

انسخ ملف المثال:

```bash
# زي إس إتش/باش
cp .env.example .env
```

```powershell
# باورشل
Copy-Item .env.example .env
```

افتح `.env` واملأ هاتين القيمتين:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

هذا كل شيء بالنسبة لمعظم الدروس! ستقوم دفاتر الملاحظات بالمصادقة تلقائيًا عبر جلسة `az login` الخاصة بك.

### الخطوة 5: تثبيت تبعيات Python

```bash|powershell
pip install -r requirements.txt
```

نوصي بتشغيل هذا داخل البيئة الافتراضية التي أنشأتها سابقًا.

## إعداد إضافي للدرس 5 (Agentic RAG)

يستخدم الدرس 5 **Azure AI Search** للتوليد المعزز بالاستخراج. إذا كنت تخطط لتشغيل ذلك الدرس، أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## إعداد إضافي للدرس 6 والدرس 8 (نماذج GitHub)

بعض دفاتر الملاحظات في الدرسين 6 و8 تستخدم **GitHub Models** بدلاً من Azure AI Foundry. إذا كنت تخطط لتشغيل هذه العينات، أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## إعداد إضافي للدرس 8 (Bing Grounding Workflow)

دفتر العمل ذو سير العمل الشرطي في الدرس 8 يستخدم **Bing grounding** عبر Azure AI Foundry. إذا كنت تخطط لتشغيل هذا المثال، أضف هذا المتغير إلى ملف `.env` الخاص بك:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## استكشاف الأخطاء وإصلاحها

### أخطاء التحقق من شهادة SSL على macOS

إذا كنت على macOS وصادفت خطأ مثل:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

هذه مشكلة معروفة مع Python على macOS حيث لا يتم الوثوق بشهادات SSL للنظام تلقائيًا. جرّب الحلول التالية بالترتيب:

**الخيار 1: تشغيل سكريبت تثبيت الشهادات في Python (موصى به)**

```bash
# استبدل 3.XX بإصدار بايثون المثبت لديك (مثلًا 3.12 أو 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**الخيار 2: استخدم `connection_verify=False` في دفتر الملاحظات الخاص بك (لدفاتر نماذج GitHub فقط)**

في دفتر الملاحظات للدرس 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)، تم تضمين حل بديل معلق بالفعل. قم بإلغاء تعليق `connection_verify=False` عند إنشاء العميل:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # عطّل التحقق من SSL إذا واجهت أخطاء في الشهادة
)
```

> **⚠️ تحذير:** تعطيل التحقق من SSL (`connection_verify=False`) يقلل من الأمان عن طريق تخطي التحقق من الشهادات. استخدم هذا كحل مؤقت فقط في بيئات التطوير، ولا تستخدمه في الإنتاج.

**الخيار 3: تثبيت واستخدام `truststore`**

```bash
pip install truststore
```

ثم أضف ما يلي في أعلى دفتر الملاحظات أو السكربت قبل إجراء أي مكالمات شبكة:

```python
import truststore
truststore.inject_into_ssl()
```

## عالق في مكان ما؟

إذا واجهت أي مشكلات في تشغيل هذا الإعداد، انضم إلى <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> أو <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">أنشئ مشكلة</a>.

## الدرس التالي

أنت الآن جاهز لتشغيل الشيفرة لهذه الدورة. تعلم سعيد أكثر عن عالم وكلاء الذكاء الاصطناعي!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
إخلاء المسؤولية:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). وعلى الرغم من سعينا للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. بالنسبة للمعلومات الحرجة، يُنصح باللجوء إلى ترجمة بشرية مهنية. لا نتحمل أي مسؤولية عن أي سوء فهم أو تفسير خاطئ ينجم عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->