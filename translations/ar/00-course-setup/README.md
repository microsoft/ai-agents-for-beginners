# إعداد الدورة

## مقدمة

ستغطي هذه الدرس كيفية تشغيل عينات الكود الخاصة بهذه الدورة.

## انضم إلى المتعلمين الآخرين واحصل على المساعدة

قبل البدء باستنساخ المستودع الخاص بك، انضم إلى [قناة Discord لوكلاء الذكاء الاصطناعي للمبتدئين](https://aka.ms/ai-agents/discord) للحصول على أي مساعدة في الإعداد، أو أي أسئلة حول الدورة، أو للتواصل مع متعلمين آخرين.

## استنساخ أو فورك هذا المستودع

للبدء، يرجى استنساخ أو فورك مستودع GitHub. هذا سيجعل لديك نسختك الخاصة من مواد الدورة حتى تتمكن من تشغيل واختبار وتعديل الكود!

يمكن القيام بذلك عن طريق النقر على الرابط لـ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">فورك المستودع</a>

يجب أن يكون لديك الآن نسختك الخاصة المفروكة من هذه الدورة في الرابط التالي:

![Forked Repo](../../../translated_images/ar/forked-repo.33f27ca1901baa6a.webp)

### استنساخ سطحي (موصى به للورش / Codespaces)

  >يمكن أن يكون المستودع الكامل كبيرًا (~3 جيجابايت) عند تنزيل التاريخ الكامل وجميع الملفات. إذا كنت تحضر الورشة فقط أو تحتاج فقط إلى بعض مجلدات الدرس، فإن الاستنساخ السطحي (أو الاستنساخ الجزئي) يتجنب معظم هذا التنزيل عن طريق تقليص التاريخ و/أو تخطي ملفات كبيرة.

#### استنساخ سطحي سريع — تاريخ ضئيل، جميع الملفات

استبدل `<your-username>` في الأوامر أدناه بعنوان URL الخاص بفوركك (أو عنوان URL الأصلي إذا فضلت).

لاستنساخ تاريخ الكوميت الأخير فقط (تنزيل صغير):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

لاستنساخ فرع محدد:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### استنساخ جزئي (متفرق) — ملفات ضئيلة + مجلدات محددة فقط

هذا يستخدم الاستنساخ الجزئي والفحص المتفرق (يتطلب Git 2.25+ وموصى باستخدام Git حديث يدعم الاستنساخ الجزئي):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ادخل إلى مجلد المستودع:

```bash|powershell
cd ai-agents-for-beginners
```

ثم حدد المجلدات التي تريدها (يظهر المثال أدناه مجلدين):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

بعد الاستنساخ والتحقق من الملفات، إذا كنت تحتاج فقط للملفات وتريد تحرير مساحة (بدون تاريخ git)، يرجى حذف بيانات تعريف المستودع (💀لا يمكن التراجع — ستفقد كل وظائف Git: لا الكوميتات، لا السحب، لا الدفع، ولا الوصول للتاريخ).

```bash
# زي شيل / باش
rm -rf .git
```

```powershell
# باورشيل
Remove-Item -Recurse -Force .git
```

#### استخدام GitHub Codespaces (موصى به لتجنب التنزيلات الكبيرة المحلية)

- أنشئ مساحة رموز جديدة لهذا المستودع عبر [واجهة GitHub](https://github.com/codespaces).  

- في الطرفية لمساحة الرموز المنشأة حديثًا، شغّل أحد أوامر الاستنساخ السطحي/المتفرق أعلاه لجلب مجلدات الدروس التي تحتاجها فقط إلى مساحة عمل Codespace.
- اختياري: بعد الاستنساخ داخل Codespaces، احذف .git لاستعادة مساحة إضافية (انظر أوامر الحذف أعلاه).
- ملاحظة: إذا فضلت فتح المستودع مباشرة في Codespaces (بدون استنساخ إضافي)، كن على علم أن Codespaces سيقوم بإنشاء بيئة devcontainer وقد يزود أكثر مما تحتاج. استنساخ نسخة سطحية داخل Codespace جديد يتيح لك التحكم أكثر في استخدام القرص.

#### نصائح

- دائمًا استبدل رابط الاستنساخ برابط الفورك الخاص بك إذا كنت تريد التعديل/الكوميت.
- إذا كنت بحاجة لاحقًا إلى المزيد من التاريخ أو الملفات، يمكنك جلبها أو تعديل إعدادات الفحص المتفرق لتضمين مجلدات إضافية.

## تشغيل الكود

تقدم هذه الدورة سلسلة من دفاتر Jupyter التي يمكنك تشغيلها للحصول على تجربة عملية في بناء وكلاء الذكاء الاصطناعي.

تستخدم عينات الكود **إطار عمل وكلاء Microsoft (MAF)** مع `FoundryChatClient`، الذي يتصل بخدمة **Microsoft Foundry Agent Service V2** (واجهة برمجة التطبيقات للردود) عبر **Microsoft Foundry**.

جميع دفاتر Python معنونة بـ `*-python-agent-framework.ipynb`.

## المتطلبات

- Python 3.12+
  - **ملاحظة**: إذا لم تقم بتثبيت Python3.12، تأكد من تثبيته. ثم أنشئ بيئة venv باستخدام python3.12 لضمان تثبيت الإصدارات الصحيحة من ملف requirements.txt.
  
    >مثال

    أنشئ مجلد بيئة Python الافتراضية:

    ```bash|powershell
    python -m venv venv
    ```

    ثم فعّل بيئة venv لـ:

    ```bash
    # زد ش أو باش
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: للأكواد النموذجية التي تستخدم .NET، تأكد من تثبيت [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) أو أحدث. ثم تحقق من إصدار SDK المثبت لديك:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — مطلوب للمصادقة. قم بالتثبيت من [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **اشتراك Azure** — للوصول إلى Microsoft Foundry وخدمة Microsoft Foundry Agent.
- **مشروع Microsoft Foundry** — مشروع يحتوي على نموذج منشور (مثلاً، `gpt-4.1-mini`). انظر [الخطوة 1](#الخطوة-1-إنشاء-مشروع-microsoft-foundry) أدناه.

لقد أدرجنا ملف `requirements.txt` في جذر هذا المستودع يحتوي على جميع حزم Python المطلوبة لتشغيل عينات الكود.

يمكنك تثبيتها عن طريق تشغيل الأمر التالي في الطرفية لديك عند جذر المستودع:

```bash|powershell
pip install -r requirements.txt
```

نوصي بإنشاء بيئة افتراضية لـ Python لتجنب أي تعارضات ومشاكل.

## إعداد VSCode

تأكد من أنك تستخدم الإصدار الصحيح من Python في VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## إعداد Microsoft Foundry وخدمة Microsoft Foundry Agent

### الخطوة 1: إنشاء مشروع Microsoft Foundry

تحتاج إلى **مركز** و**مشروع** في Microsoft Foundry مع نموذج منشور لتشغيل دفاتر Jupyter.

1. توجه إلى [ai.azure.com](https://ai.azure.com) وسجل الدخول بحساب Azure الخاص بك.
2. أنشئ **مركز** (أو استخدم واحدًا موجودًا). انظر: [نظرة عامة على موارد المركز](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. داخل المركز، أنشئ **مشروع**.
4. انشر نموذجًا (مثلاً، `gpt-4.1-mini`) من **النماذج + نقاط النهاية** → **نشر نموذج**.

### الخطوة 2: استرجع نقطة نهاية مشروعك واسم نشر النموذج

من مشروعك في بوابة Microsoft Foundry:

- **نقطة نهاية المشروع** — اذهب إلى صفحة **نظرة عامة** وانسخ عنوان URL للنقطة النهاية.

![Project Connection String](../../../translated_images/ar/project-endpoint.8cf04c9975bbfbf1.webp)

- **اسم نشر النموذج** — اذهب إلى **النماذج + نقاط النهاية**، اختر نموذجك المنشور، وسجل **اسم النشر** (مثلاً، `gpt-4.1-mini`).

### الخطوة 3: تسجيل الدخول إلى Azure باستخدام `az login`

تستخدم كل دفاتر Jupyter مصادقة **`AzureCliCredential`** — لا حاجة لإدارة مفاتيح API. يتطلب هذا تسجيل دخولك عبر Azure CLI.

1. **ثبت Azure CLI** إذا لم تفعل ذلك بعد: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **سجل الدخول** بتشغيل:

    ```bash|powershell
    az login
    ```

    أو إذا كنت في بيئة بعيدة/Codepace بدون متصفح:

    ```bash|powershell
    az login --use-device-code
    ```

3. **اختر اشتراكك** إذا طُلب منك — اختر الاشتراك الذي يحتوي على مشروع Foundry الخاص بك.

4. **تحقق** من أنك مسجل الدخول:

    ```bash|powershell
    az account show
    ```

> **لماذا `az login`؟** تستخدم دفاتر Jupyter المصادقة عبر `AzureCliCredential` من حزمة `azure-identity`. وهذا يعني أن جلسة Azure CLI الخاصة بك توفر بيانات الاعتماد — لا مفاتيح API أو أسرار في ملف `.env`. هذه [أفضل ممارسة أمان](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### الخطوة 4: إنشاء ملف `.env` الخاص بك

انسخ ملف المثال:

```bash
# زش/باش
cp .env.example .env
```

```powershell
# باورشيل
Copy-Item .env.example .env
```

افتح ملف `.env` واملأ هذين القيمتين:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | بوابة Foundry → مشروعك → صفحة **نظرة عامة** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | بوابة Foundry → **النماذج + نقاط النهاية** → اسم نموذجك المنشور |

هذا كل شيء لمعظم الدروس! ستتم المصادقة في الدفاتر تلقائيًا عبر جلسة `az login` الخاصة بك.

### الخطوة 5: تثبيت تبعيات Python

```bash|powershell
pip install -r requirements.txt
```

نوصي بتشغيل هذا داخل البيئة الافتراضية التي أنشأتها سابقًا.

## إعداد إضافي للدرس 5 (الوكلاء المستخدمون لاسترجاع المعلومات - Agentic RAG)

يستخدم الدرس 5 **بحث Azure AI** لتوليد معزز باسترجاع المعلومات. إذا كنت تخطط لتشغيل ذلك الدرس، أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | بوابة Azure → مورد **Azure AI Search** الخاص بك → **نظرة عامة** → عنوان URL |
| `AZURE_SEARCH_API_KEY` | بوابة Azure → مورد **Azure AI Search** الخاص بك → **الإعدادات** → **المفاتيح** → مفتاح المسؤول الأساسي |

## إعداد إضافي للدروس التي تستدعي Azure OpenAI مباشرة (الدروس 6 و 8)

بعض دفاتر الدروس 6 و 8 تستدعي **Azure OpenAI** مباشرة (باستخدام **واجهة ردود الفعل API**) بدلاً من المرور بمشروع Microsoft Foundry. هذه العينات كانت تستخدم سابقًا نماذج GitHub، التي تم إيقاف دعمها رسميًا (تتوقف في يوليو 2026) ولا تدعم API الردود. إذا كنت تخطط لتشغيل تلك العينات، أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | بوابة Azure → مورد **Azure OpenAI** الخاص بك → **المفاتيح ونقطة النهاية** → نقطة النهاية (مثلاً `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | اسم النموذج المنشور الخاص بك (مثلاً `gpt-4.1-mini`) الذي يدعم واجهة ردود الفعل API |
| `AZURE_OPENAI_API_KEY` | اختياري — فقط إذا تستخدم المصادقة بمفتاح بدلاً من `az login` / Entra ID |

> تستخدم واجهة ردود الفعل API نقطة النهاية الثابتة `/openai/v1/`، لذا لا حاجة لإضافة `api-version`. سجل دخول باستخدام `az login` لاستخدام المصادقة بدون مفاتيح مع Entra ID.

## مزود بديل: MiniMax (متوافق مع OpenAI)

يوفر [MiniMax](https://platform.minimaxi.com/) نماذج بسياقات كبيرة (حتى 204 ألف توكن) عبر واجهة برمجة تطبيقات متوافقة مع OpenAI. بما أن `OpenAIChatClient` في إطار عمل وكلاء Microsoft يعمل مع أي نقطة نهاية متوافقة مع OpenAI، يمكنك استخدام MiniMax كبديل جاهز لـ Azure OpenAI أو OpenAI.

أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `MINIMAX_API_KEY` | [منصة MiniMax](https://platform.minimaxi.com/) → مفاتيح API |
| `MINIMAX_BASE_URL` | استخدم `https://api.minimax.io/v1` (القيمة الافتراضية) |
| `MINIMAX_MODEL_ID` | اسم النموذج المستخدم (مثلاً، `MiniMax-M3`) |

**نماذج مثال**: `MiniMax-M3` (موصى به)، `MiniMax-M2.7`، `MiniMax-M2.7-highspeed` (ردود أسرع). أسماء النماذج وتوفرها قد تتغير مع الوقت، والوصول إلى نموذج معين قد يعتمد على حسابك أو منطقتك — راجع [منصة MiniMax](https://platform.minimaxi.com/) للقائمة الحالية. إذا لم يكن `MiniMax-M3` متاحًا لحسابك، اضبط `MINIMAX_MODEL_ID` إلى نموذج يمكنك الوصول إليه (مثلاً `MiniMax-M2.7`).

ستكتشف عينات الكود التي تستخدم `OpenAIChatClient` (مثلاً، سير حجز الفنادق في الدرس 14) تلقائيًا إعداد MiniMax الخاص بك عندما يتم تعيين `MINIMAX_API_KEY`.

## مزود بديل: Foundry Local (تشغيل النماذج على الجهاز)

[Foundry Local](https://foundrylocal.ai) هو بيئة تشغيل خفيفة الوزن تقوم بتنزيل وإدارة وتقديم نماذج اللغة **كليًا على جهازك** عبر واجهة متوافقة مع OpenAI — بدون سحابة، بدون اشتراك Azure، وبدون مفاتيح API. إنه خيار ممتاز للتطوير في وضع عدم الاتصال، والتجريب دون تكبد تكاليف السحابة، أو الاحتفاظ بالبيانات على الجهاز.

بما أن `OpenAIChatClient` في إطار عمل وكلاء Microsoft يعمل مع أي نقطة نهاية متوافقة مع OpenAI، فإن Foundry Local هو بديل محلي جاهز لـ Azure OpenAI.

**1. تثبيت Foundry Local**

```bash
# ويندوز
winget install Microsoft.FoundryLocal

# ماك أو إس
brew install foundrylocal
```

**2. تنزيل وتشغيل نموذج** (هذا يبدأ أيضًا الخدمة المحلية):

```bash
foundry model list          # عرض النماذج المتاحة
foundry model run phi-4-mini
```

**3. تثبيت SDK لـ Python** المستخدم لاكتشاف نقطة النهاية المحلية:

```bash
pip install foundry-local-sdk
```

**4. وجه إطار عمل وكلاء Microsoft إلى نموذجك المحلي:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# يقوم بتنزيل النموذج محليًا (إذا لزم الأمر) وتشغيله ثم يكتشف نقطة النهاية/المنفذ.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # مثلاً http://localhost:<port>/v1
    api_key=manager.api_key,        # دائماً "غير مطلوب" لـ Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **ملاحظة:** تعرض Foundry Local نقطة نهاية متوافقة مع OpenAI لخدمات **تكملة المحادثة**. استخدمها للتطوير المحلي والسيناريوهات دون اتصال. للحصول على مجموعة كاملة من ميزات **واجهة ردود الفعل API** (محادثات حالة متقدمة، تنظيم أدوات عميق، وتطوير نمطي للوكيل)، استهدف **Azure OpenAI** أو مشروع **Microsoft Foundry** كما هو موضح في الدروس. انظر [توثيق Foundry Local](https://foundrylocal.ai) لكاتالوج النماذج الحالي ودعم المنصة.


## إعداد إضافي للدرس 8 (سير عمل Bing Grounding)

يستخدم دفتر سير العمل الشرطي في الدرس 8 **Bing grounding** عبر Microsoft Foundry. إذا كنت تخطط لتشغيل هذا المثال، أضف هذا المتغير إلى ملف `.env` الخاص بك:

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `BING_CONNECTION_ID` | بوابة Microsoft Foundry → مشروعك → **الإدارة** → **الموارد المتصلة** → اتصال Bing الخاص بك → نسخ معرف الاتصال |

## استكشاف الأخطاء وإصلاحها

### أخطاء التحقق من شهادة SSL على macOS

إذا كنت تستخدم macOS وواجهت خطأ مثل:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

هذه مشكلة معروفة مع Python على macOS حيث لا يتم تلقائيًا الثقة بشهادات SSL للنظام. جرب الحلول التالية بالترتيب:

**الخيار 1: تشغيل سكربت تثبيت شهادات Python (موصى به)**

```bash
# استبدل 3.XX بإصدار بايثون المثبت لديك (مثلاً، 3.12 أو 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**الخيار 2: استخدام `connection_verify=False` في دفتر الملاحظات الخاص بك (لدفاتر ملاحظات GitHub Models فقط)**

في دفتر ملاحظات الدرس 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)، يوجد حل بديل معلّق مسبقًا. قم بإلغاء تعليق `connection_verify=False` عند إنشاء العميل:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # قم بتعطيل التحقق من SSL إذا واجهت أخطاء في الشهادة
)
```

> **⚠️ تحذير:** تعطيل التحقق من SSL (`connection_verify=False`) يقلل الأمان بتخطي التحقق من الشهادة. استخدم هذا فقط كحل مؤقت في بيئات التطوير، وليس في الإنتاج.

**الخيار 3: تثبيت واستخدام `truststore`**

```bash
pip install truststore
```

ثم أضف التالي في أعلى دفتر الملاحظات أو السكربت قبل إجراء أي مكالمات شبكة:

```python
import truststore
truststore.inject_into_ssl()
```

## هل علقت في مكان ما؟

إذا واجهت أي مشاكل في تشغيل هذا الإعداد، انضم إلى <a href="https://discord.gg/kzRShWzttr" target="_blank">ديسكورد مجتمع Azure AI</a> أو <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">قم بإنشاء مشكلة</a>.

## الدرس التالي

أنت الآن جاهز لتشغيل كود هذه الدورة. نتمنى لك تعلمًا موفقًا حول عالم وكلاء الذكاء الاصطناعي! 

[مقدمة إلى وكلاء الذكاء الاصطناعي وحالات استخدام الوكلاء](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->