# إعداد الدورة

## مقدمة

ستغطي هذه الدرس كيفية تشغيل عينات الكود لهذه الدورة.

## انضم إلى المتعلمين الآخرين واحصل على المساعدة

قبل أن تبدأ في استنساخ المستودع الخاص بك، انضم إلى [قناة Discord لوكلاء الذكاء الاصطناعي للمبتدئين](https://aka.ms/ai-agents/discord) للحصول على أي مساعدة في الإعداد، أو أي أسئلة حول الدورة، أو للتواصل مع متعلمين آخرين.

## استنساخ أو عمل فورك لهذا المستودع

للبدء، يرجى استنساخ أو عمل فورك لمستودع GitHub. سيجعل هذا نسختك الخاصة من مواد الدورة لتتمكن من تشغيلها، اختبارها، وتعديل الكود!

يمكن القيام بذلك بالنقر على الرابط لـ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">عمل فورك للمستودع</a>

يجب أن يكون لديك الآن نسختك الخاصة المفروكة من هذه الدورة في الرابط التالي:

![Forked Repo](../../../translated_images/ar/forked-repo.33f27ca1901baa6a.webp)

### استنساخ سطحي (موصى به للورشة / بيئات Codespaces)

  >المستودع الكامل يمكن أن يكون كبيرًا (~3 جيجابايت) عند تحميل التاريخ الكامل وجميع الملفات. إذا كنت تحضر الورشة فقط أو تحتاج فقط إلى بعض مجلدات الدروس، فإن الاستنساخ السطحي (أو الاستنساخ الجزئي) يتجنب معظم هذا التحميل عن طريق تقصير التاريخ و/أو تخطي البيانات الكبيرة.

#### استنساخ سطحي سريع — تاريخ محدود، جميع الملفات

استبدل `<your-username>` في الأوامر أدناه بعنوان URL لفورك الخاص بك (أو عنوان URL الأصلي إذا فضلت).

لاستنساخ تاريخ الالتزام الأخير فقط (تحميل صغير):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

لاستنساخ فرع محدد:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### استنساخ جزئي (متفرق) — حزم صغيرة + مجلدات مختارة فقط

هذا يستخدم الاستنساخ الجزئي و sparse-checkout (يتطلب Git 2.25+ ويفضل استخدام Git حديث مع دعم للاستنساخ الجزئي):

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

بعد الاستنساخ والتحقق من الملفات، إذا كنت تحتاج فقط للملفات وترغب في تحرير مساحة (بدون تاريخ Git)، يرجى حذف بيانات المستودع (💀 لا يمكن التراجع — ستفقد كل وظائف Git: لا التزامات، لا سحب، لا دفعات، ولا وصول للتاريخ).

```bash
# زش/باش
rm -rf .git
```

```powershell
# باورشيل
Remove-Item -Recurse -Force .git
```

#### استخدام GitHub Codespaces (موصى به لتجنب التحميلات الكبيرة محليًا)

- أنشئ فضاء تعليمات برمجية جديد لهذا المستودع عبر [واجهة GitHub](https://github.com/codespaces).  

- في الطرفية داخل فضاء التعليمات البرمجية الجديد، نفذ أحد أوامر الاستنساخ السطحي/المتفرق أعلاه لجلب مجلدات الدروس التي تحتاجها فقط إلى مساحة عمل فضاء التعليمات البرمجية.
- اختياري: بعد الاستنساخ داخل Codespaces، قم بإزالة .git لاسترجاع مساحة إضافية (انظر أوامر الحذف أعلاه).
- ملاحظة: إذا فضلت فتح المستودع مباشرة في Codespaces (بدون استنساخ إضافي)، كن على علم أن Codespaces سيبني بيئة devcontainer وقد يزود أكثر مما تحتاج. استنساخ نسخة سطحية داخل Codespace جديد يمنحك تحكمًا أكبر في استخدام القرص.

#### نصائح

- استبدل دائمًا عنوان URL للاستنساخ بفورك الخاص بك إذا أردت التعديل/الالتزام.
- إذا احتجت لاحقًا إلى مزيد من التاريخ أو الملفات، يمكنك جلبها أو ضبط sparse-checkout لتضمين مجلدات إضافية.

## تشغيل الكود

تقدم هذه الدورة سلسلة من دفاتر Jupyter التي يمكنك تشغيلها للحصول على تجربة عملية في بناء وكلاء الذكاء الاصطناعي.

تستخدم عينات الكود **إطار عمل الوكيل من مايكروسوفت (MAF)** مع `FoundryChatClient`، الذي يتصل بـ **خدمة وكلاء Microsoft Foundry V2** (واجهة برمجة تطبيقات الاستجابات) من خلال **Microsoft Foundry**.

جميع دفاتر بايثون معنونة بـ `*-python-agent-framework.ipynb`.

## المتطلبات

- بايثون 3.12+
  - **ملاحظة**: إذا لم يكن لديك بايثون 3.12 مثبتًا، تأكد من تثبيته. ثم أنشئ بيئة افتراضية باستخدام python3.12 لضمان تثبيت الإصدارات الصحيحة من ملف requirements.txt.
  
    >مثال

    أنشئ دليل البيئة الافتراضية لبايثون:

    ```bash|powershell
    python -m venv venv
    ```

    ثم فعّل بيئة venv لـ:

    ```bash
    # زد شل/باش
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: بالنسبة لأكواد الأمثلة التي تستخدم .NET، تأكد من تثبيت [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) أو أحدث. ثم تحقق من إصدار SDK المثبت لديك:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — مطلوب للمصادقة. قم بالتثبيت من [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **اشتراك Azure** — للوصول إلى Microsoft Foundry وخدمة وكلاء Microsoft Foundry.
- **مشروع Microsoft Foundry** — مشروع به نموذج نشر (مثل `gpt-5-mini`). راجع [الخطوة 1](#الخطوة-1-إنشاء-مشروع-microsoft-foundry) أدناه.

لقد أدرجنا ملف `requirements.txt` في جذر هذا المستودع يحتوي على جميع الحزم المطلوبة لبايثون لتشغيل عينات الكود.

يمكنك تثبيتها بتنفيذ الأمر التالي في الطرفية في جذر المستودع:

```bash|powershell
pip install -r requirements.txt
```

نوصي بإنشاء بيئة بايثون افتراضية لتجنب أي تعارضات ومشاكل.

## إعداد VSCode

تأكد من أنك تستخدم الإصدار الصحيح من بايثون في VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## إعداد Microsoft Foundry وخدمة وكلاء Microsoft Foundry

### الخطوة 1: إنشاء مشروع Microsoft Foundry

تحتاج إلى **مركز** ومشروع في Microsoft Foundry مع نموذج منشور لتشغيل دفاتر Jupyter.

1. اذهب إلى [ai.azure.com](https://ai.azure.com) وقم بتسجيل الدخول بحساب Azure الخاص بك.
2. أنشئ **مركزًا** (أو استخدم مركزًا موجودًا). انظر: [نظرة عامة على موارد المركز](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. داخل المركز، أنشئ **مشروعًا**.
4. انشر نموذجًا (مثل `gpt-5-mini`) من **النماذج + النقاط النهائية** → **نشر نموذج**.

### الخطوة 2: استرجاع نقطة نهاية المشروع واسم نشر النموذج

من مشروعك في بوابة Microsoft Foundry:

- **نقطة نهاية المشروع** — اذهب إلى صفحة **نظرة عامة** ونسخ عنوان URL لنقطة النهاية.

![Project Connection String](../../../translated_images/ar/project-endpoint.8cf04c9975bbfbf1.webp)

- **اسم نشر النموذج** — اذهب إلى **النماذج + النقاط النهائية**، اختر النموذج المنشور، ودوّن **اسم النشر** (مثل `gpt-5-mini`).

### الخطوة 3: تسجيل الدخول إلى Azure باستخدام `az login`

تستخدم جميع دفاتر Jupyter مصادقة **`AzureCliCredential`** — لا حاجة لإدارة مفاتيح API. يتطلب هذا تسجيل الدخول عبر Azure CLI.

1. **ثبت Azure CLI** إذا لم يكن مثبتًا: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **قم بتسجيل الدخول** بتنفيذ:

    ```bash|powershell
    az login
    ```

    أو إذا كنت في بيئة بعيدة/ Codespace بدون متصفح:

    ```bash|powershell
    az login --use-device-code
    ```

3. **اختر اشتراكك** إذا طُلب منك — اختر الذي يحتوي على مشروع Foundry الخاص بك.

4. **تحقق** من أنك مسجل الدخول:

    ```bash|powershell
    az account show
    ```

> **لماذا `az login`؟** دفاتر Jupyter تستخدم `AzureCliCredential` من حزمة `azure-identity` للمصادقة. هذا يعني أن جلسة Azure CLI تزود بيانات الاعتماد — لا مفاتيح API أو أسرار في ملف `.env` الخاص بك. هذه هي [أفضل ممارسات الأمان](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### الخطوة 4: إنشاء ملف `.env` الخاص بك

انسخ ملف المثال:

```bash
# زد شيل/باش
cp .env.example .env
```

```powershell
# باورشيل
Copy-Item .env.example .env
```

افتح `.env` واملأ هذين المتغيرين:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| متغير | مكان إيجاده |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | بوابة Foundry → مشروعك → صفحة **نظرة عامة** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | بوابة Foundry → **النماذج + النقاط النهائية** → اسم النموذج المنشور الخاص بك |

هذا كل شيء لمعظم الدروس! ستتم المصادقة تلقائيًا عبر جلسة `az login` الخاصة بك.

### الخطوة 5: تثبيت تبعيات بايثون

```bash|powershell
pip install -r requirements.txt
```

نوصي بتشغيل هذا داخل البيئة الافتراضية التي أنشأتها سابقًا.

## إعداد إضافي للدرس 5 (Agentic RAG)

يستخدم الدرس 5 **Azure AI Search** للتوليد المعزز بالاسترجاع. إذا كنت تخطط لتشغيل هذا الدرس، أضف هذه المتغيرات إلى ملف `.env`:

| متغير | مكان إيجاده |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | بوابة Azure → مورد **Azure AI Search** الخاص بك → **نظرة عامة** → URL |
| `AZURE_SEARCH_API_KEY` | بوابة Azure → مورد **Azure AI Search** → **الإعدادات** → **المفاتيح** → المفتاح الإداري الأساسي |

## إعداد إضافي للدروس التي تستدعي Azure OpenAI مباشرة (الدروس 6 و 8)

بعض دفاتر Jupyter في الدروس 6 و 8 تستدعي **Azure OpenAI** مباشرة (باستخدام **واجهة Responses API**) بدلاً من الذهاب عبر مشروع Microsoft Foundry. كانت هذه العينات تستخدم سابقًا نماذج GitHub، والتي تم إيقاف دعمها (تُوقف بحلول يوليو 2026) ولا تدعم Responses API. إذا كنت تخطط لتشغيل تلك العينات، أضف هذه المتغيرات إلى ملف `.env`:

| متغير | مكان إيجاده |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | بوابة Azure → مورد **Azure OpenAI** الخاص بك → **المفاتيح ونقطة النهاية** → نقطة النهاية (مثلاً `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | اسم النموذج المنشور الخاص بك (مثلاً `gpt-5-mini`) الذي يدعم Responses API |
| `AZURE_OPENAI_API_KEY` | اختياري — فقط إذا كنت تستخدم المصادقة بمفتاح بدلاً من `az login` / Entra ID |

> تستخدم Responses API نقطة النهاية المستقرة `/openai/v1/`، لذلك لا يلزم `api-version`. سجّل الدخول باستخدام `az login` لاستخدام مصادقة Entra ID بدون مفتاح.

## موفر بديل: MiniMax (متوافق مع OpenAI)

يوفر [MiniMax](https://platform.minimaxi.com/) نماذج سياق كبير (حتى 204K رمز) من خلال API متوافق مع OpenAI. بما أن `OpenAIChatClient` في إطار Microsoft Agent Framework يعمل مع أي نقطة نهاية متوافقة مع OpenAI، يمكنك استخدام MiniMax كبديل جاهز لـ Azure OpenAI أو OpenAI.

أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| متغير | مكان إيجاده |
|----------|-----------------|
| `MINIMAX_API_KEY` | منصة [MiniMax](https://platform.minimaxi.com/) → مفاتيح API |
| `MINIMAX_BASE_URL` | استخدم `https://api.minimax.io/v1` (القيمة الافتراضية) |
| `MINIMAX_MODEL_ID` | اسم النموذج لاستخدامه (مثلاً `MiniMax-M3`) |

**نماذج مثال**: `MiniMax-M3` (موصى به)، `MiniMax-M2.7`، `MiniMax-M2.7-highspeed` (استجابات أسرع). قد تتغير أسماء النماذج وتوفرها مع الزمن، وقد يعتمد الوصول إلى نموذج معين على حسابك أو منطقتك — تحقق من منصة [MiniMax](https://platform.minimaxi.com/) للقائمة الحالية. إذا لم يكن `MiniMax-M3` متاحًا لحسابك، قم بضبط `MINIMAX_MODEL_ID` إلى نموذج لديك صلاحية الوصول إليه (مثلًا `MiniMax-M2.7`).

ستكتشف عينات الكود التي تستخدم `OpenAIChatClient` (مثل سير عمل حجز الفندق في الدرس 14) تلقائيًا وتستخدم تكوين MiniMax عند تعيين `MINIMAX_API_KEY`.

## موفر بديل: Foundry Local (تشغيل النماذج على الجهاز)

[Foundry Local](https://foundrylocal.ai) هو وقت تشغيل خفيف الوزن يقوم بتنزيل، إدارة، وخدمة نماذج اللغة **كليًا على جهازك الخاص** من خلال واجهة برمجة التطبيقات المتوافقة مع OpenAI — بدون سحابة، بدون اشتراك في Azure، وبدون مفاتيح API. إنه خيار رائع للتطوير دون اتصال، والتجربة دون تكبد تكاليف السحابة، أو الحفاظ على البيانات على الجهاز.

ونظرًا لأن `OpenAIChatClient` في إطار Microsoft Agent Framework يعمل مع أي نهاية متوافقة مع OpenAI، فإن Foundry Local هو بديل محلي جاهز لـ Azure OpenAI.

**1. تثبيت Foundry Local**

```bash
# ويندوز
winget install Microsoft.FoundryLocal

# ماك أو إس
brew install foundrylocal
```

**2. تنزيل وتشغيل نموذج** (هذا يبدأ الخدمة المحلية أيضًا):

```bash
foundry model list          # عرض النماذج المتاحة
foundry model run phi-4-mini
```

**3. تثبيت SDK لبايثون** المستخدم لاكتشاف نقطة النهاية المحلية:

```bash
pip install foundry-local-sdk
```

**4. وجه إطار Microsoft Agent Framework إلى نموذجك المحلي:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# يقوم بتنزيل النموذج (إذا لزم الأمر) ويخدمه محليًا، ثم يكتشف نقطة النهاية/المنفذ.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # على سبيل المثال http://localhost:<port>/v1
    api_key=manager.api_key,        # دائمًا "غير مطلوب" لـ Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **ملاحظة:** تعرض Foundry Local نقطة نهاية **إكمال المحادثة** متوافقة مع OpenAI. استخدمها للتطوير المحلي والسيناريوهات بدون اتصال. للحصول على كامل ميزات **Responses API** (المحادثات ذات الحالة، تنظيم الأدوات العميق، والتطوير بأسلوب الوكيل)، وجه إلى **Azure OpenAI** أو مشروع **Microsoft Foundry** كما هو موضح في الدروس. راجع [وثائق Foundry Local](https://foundrylocal.ai) لكاتالوج النماذج الحالي ودعم المنصة.

## إعداد إضافي للدرس 8 (سير عمل تعزيز Bing)


يستخدم دفتر سير العمل الشرطي في الدرس 8 **تكامل Bing** عبر Microsoft Foundry. إذا كنت تخطط لتشغيل هذا النموذج، أضف هذا المتغير إلى ملف `.env` الخاص بك:

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `BING_CONNECTION_ID` | بوابة Microsoft Foundry → مشروعك → **الإدارة** → **الموارد المتصلة** → اتصال Bing الخاص بك → انسخ معرف الاتصال |

## استكشاف الأخطاء وإصلاحها

### أخطاء التحقق من شهادة SSL على macOS

إذا كنت تستخدم macOS وواجهت خطأ مثل:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

هذه مشكلة معروفة في Python على macOS حيث لا يتم الوثوق تلقائيًا بشهادات SSL للنظام. جرّب الحلول التالية بالترتيب:

**الخيار 1: تشغيل سكريبت تثبيت شهادات Python (مستحسن)**

```bash
# استبدل 3.XX بإصدار بايثون المثبت لديك (مثلاً، 3.12 أو 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**الخيار 2: استخدام `connection_verify=False` في دفتر ملاحظاتك (لفهارس GitHub Models فقط)**

في دفتر الملاحظات الخاص بالدرس 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)، تم تضمين حل بديل معلق بالفعل. قم بإلغاء تعليق `connection_verify=False` عند إنشاء العميل:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # تعطيل التحقق من SSL إذا واجهت أخطاء في الشهادة
)
```

> **⚠️ تحذير:** تعطيل التحقق من SSL (`connection_verify=False`) يقلل من الأمان بتخطي التحقق من الشهادة. استخدم هذا كحل مؤقت فقط في بيئات التطوير، وليس في الإنتاج.

**الخيار 3: تثبيت واستخدام `truststore`**

```bash
pip install truststore
```

ثم أضف ما يلي في أعلى دفتر ملاحظاتك أو سكريبتك قبل إجراء أي اتصالات شبكية:

```python
import truststore
truststore.inject_into_ssl()
```

## عالق في مكان ما؟

إذا واجهت أي مشاكل في تشغيل هذا الإعداد، انضم إلى <a href="https://discord.gg/kzRShWzttr" target="_blank">ديسكورد مجتمع Azure AI</a> أو <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">أنشئ تقرير مشكلة</a>.

## الدرس التالي

أنت الآن جاهز لتشغيل كود هذا الدورة. نتمنى لك تعلمًا سعيدًا وأكثر عن عالم وكلاء الذكاء الاصطناعي! 

[مقدمة إلى وكلاء الذكاء الاصطناعي وحالات استخدام الوكلاء](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->