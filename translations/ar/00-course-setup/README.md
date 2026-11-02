# إعداد الدورة

## مقدمة

ستغطي هذه الدرس كيفية تشغيل عينات الأكواد لهذه الدورة.

## انضم إلى المتعلمين الآخرين واحصل على المساعدة

قبل أن تبدأ في استنساخ المستودع الخاص بك، انضم إلى [قناة Discord لوكلاء الذكاء الاصطناعي للمبتدئين](https://aka.ms/ai-agents/discord) للحصول على أي مساعدة في الإعداد، أو لأي أسئلة حول الدورة، أو للتواصل مع متعلمين آخرين.

## استنسخ أو افرد هذا المستودع

للبدء، يرجى استنساخ أو تفريع مستودع GitHub. سيتيح لك هذا إنشاء نسختك الخاصة من مواد الدورة لتتمكن من تشغيل الأكواد واختبارها وتعديلها!

يمكن القيام بذلك بالنقر على الرابط لـ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">تفريع المستودع</a>

يجب أن يكون لديك الآن نسختك المفروعة الخاصة من هذه الدورة في الرابط التالي:

![Forked Repo](../../../translated_images/ar/forked-repo.33f27ca1901baa6a.webp)

### استنساخ سطحي (موصى به للورشة / مساحات الأكواد)

  >يمكن أن يكون المستودع الكامل كبيرًا (~3 جيجابايت) عند تنزيل التاريخ الكامل وجميع الملفات. إذا كنت تحضر الورشة فقط أو تحتاج فقط إلى بعض مجلدات الدروس، فإن الاستنساخ السطحي (أو الاستنساخ الجزئي) ينزل حجمًا أقل بكثير.

#### استنساخ سطحي سريع — أدنى تاريخ، جميع الملفات

استبدل `<your-username>` في الأوامر أدناه برابط التفريع الخاص بك (أو بالرابط الأصلي upstream إذا فضلت).

لاستنساخ تاريخ الالتزام الأخير فقط (تنزيل صغير):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

لاستنساخ فرع محدد:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### استنساخ جزئي (مشتت) — أقل حجم بيانات + فقط المجلدات المحددة

يستخدم هذا الاستنساخ الجزئي وتقنية sparse-checkout (يتطلب Git 2.25+ ويوصى باستخدام Git حديث يدعم الاستنساخ الجزئي):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

انتقل إلى مجلد المستودع:

```bash
cd ai-agents-for-beginners
```

ثم حدد أي المجلدات تريدها (المثال أدناه يظهر مجلدين):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

بعد الاستنساخ والتحقق من الملفات، إذا كنت بحاجة فقط للملفات وترغب في تحرير مساحة (بدون تاريخ Git)، يرجى حذف بيانات تعريف المستودع (💀 لا يمكن التراجع عنه — ستفقد جميع وظائف Git):

```bash
# زش/باش
rm -rf .git
```

```powershell
# باورشيل
Remove-Item -Recurse -Force .git
```

#### استخدام GitHub Codespaces (موصى به لتجنب التنزيلات المحلية الكبيرة)

- قم بإنشاء مساحة أكواد جديدة لهذا المستودع عبر [واجهة GitHub](https://github.com/codespaces).  

- في الطرفية لمساحة الأكواد الجديدة، نفذ أحد أوامر الاستنساخ السطحي/الجزئي أعلاه لجلب مجلدات الدروس التي تحتاجها فقط إلى مساحة العمل في Codespaces.
- اختياري: بعد الاستنساخ داخل Codespaces، يمكن إزالة .git لاستعادة مساحة إضافية (انظر أوامر الإزالة أعلاه).
- ملاحظة: إذا فضلت فتح المستودع مباشرة في Codespaces (بدون استنساخ إضافي)، كن على علم بأن Codespaces سيقوم بإنشاء بيئة devcontainer وقد يوفر أكثر مما تحتاج.

#### نصائح

- استبدل دائمًا رابط الاستنساخ برابط التفريع الخاص بك إذا أردت التحرير/الإضافة.
- إذا احتجت لاحقًا إلى المزيد من التاريخ أو الملفات، يمكنك جلبها أو تعديل sparse-checkout لتضمين مجلدات إضافية.

## تشغيل الكود

تقدم هذه الدورة سلسلة من دفاتر Jupyter التي يمكنك تشغيلها للحصول على خبرة عملية في بناء وكلاء الذكاء الاصطناعي.

تستخدم عينات الكود **إطار عمل Microsoft Agent Framework (MAF)** مع `FoundryChatClient`، الذي يتصل بـ **خدمة Microsoft Foundry Agent V2** (واجهة API للردود) عبر **Microsoft Foundry**.

جميع دفاتر Python معنونة بـ `*-python-agent-framework.ipynb`.

## المتطلبات

- Python 3.12+
  - **ملاحظة**: إذا لم يكن لديك Python3.12 مثبتًا، تأكد من تثبيته. ثم أنشئ بيئة venv باستخدام python3.12 لضمان تثبيت الإصدارات الصحيحة من ملف requirements.txt.
  
    >مثال

    أنشئ مجلد بيئة Python الافتراضية:

    ```bash
    python -m venv venv
    ```

    ثم فعّل بيئة venv لـ:

    ```bash
    # زد شيل / باش
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: بالنسبة لأكواد الأمثلة التي تستخدم .NET، تأكد من تثبيت [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) أو أحدث. ثم تحقق من إصدار .NET SDK المثبت:

    ```bash
    dotnet --list-sdks
    ```

- **واجهة Azure CLI** — مطلوبة للمصادقة. قم بالتثبيت من [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **اشتراك Azure** — للوصول إلى Microsoft Foundry وخدمة Microsoft Foundry Agent.
- **مشروع Microsoft Foundry** — مشروع يحتوي على نموذج منشور (مثل `gpt-5-mini`). انظر [الخطوة 1](#الخطوة-1-إنشاء-مشروع-microsoft-foundry) أدناه.

قمنا بتضمين ملف `requirements.txt` في جذر هذا المستودع يحتوي على جميع حزم Python المطلوبة لتشغيل عينات الأكواد.

يمكنك تثبيتها عن طريق تشغيل الأمر التالي في الطرفية في جذر المستودع:

```bash
pip install -r requirements.txt
```

نوصي بإنشاء بيئة افتراضية Python لتجنب أي تعارضات ومشاكل.

## إعداد VSCode

تأكد من أنك تستخدم الإصدار الصحيح من Python في VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## إعداد Microsoft Foundry وخدمة Microsoft Foundry Agent

### الخطوة 1: إنشاء مشروع Microsoft Foundry

تحتاج إلى **Hub** و**مشروع** في Microsoft Foundry مع نموذج منشور لتشغيل دفاتر Jupyter.

1. اذهب إلى [ai.azure.com](https://ai.azure.com) وقم بتسجيل الدخول بحساب Azure الخاص بك.
2. أنشئ **Hub** (أو استخدم واحدًا موجودًا). انظر: [نظرة عامة على موارد Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. داخل الـ Hub، أنشئ **مشروعًا**.
4. انشر نموذجًا (مثل `gpt-5-mini`) من **Models + Endpoints** → **Deploy model**.

### الخطوة 2: استرجاع نقطة نهاية المشروع واسم نشر النموذج

من مشروعك في بوابة Microsoft Foundry:

- **نقطة نهاية المشروع** — اذهب إلى صفحة **نظرة عامة** وانسخ رابط نقطة النهاية.

![Project Connection String](../../../translated_images/ar/project-endpoint.8cf04c9975bbfbf1.webp)

- **اسم نشر النموذج** — اذهب إلى **Models + Endpoints**، اختر النموذج المنشور، ودوّن **اسم النشر** (مثلاً `gpt-5-mini`).

### الخطوة 3: تسجيل الدخول إلى Azure باستخدام `az login`

معظم دفاتر Jupyter تقوم بالمصادقة عبر **تسجيل الدخول إلى Azure CLI** — باستخدام `AzureCliCredential` أو `DefaultAzureCredential` (كلاهما يأخذ جلسة `az login` الخاصة بك) من حزمة `azure-identity` — لذا لا تحتاج إلى مفاتيح API. تستخدم بعض الدروس والدمجات الاختيارية مفاتيح API؛ تحقق من متطلبات كل درس لأي متغيرات بيئية إضافية. يتطلب هذا أن تكون مسجلاً الدخول عبر Azure CLI.

1. **ثبت Azure CLI** إذا لم تكن قد فعلت ذلك: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **سجل الدخول** بتشغيل:

    ```bash
    az login
    ```

    أو إذا كنت في بيئة بعيدة/مساحة أكواد بدون متصفح:

    ```bash
    az login --use-device-code
    ```

3. **اختر اشتراكك** إذا طُلب منك — اختر الاشتراك الذي يحتوي على مشروع Foundry الخاص بك.

4. **تحقق** من تسجيل دخولك:

    ```bash
    az account show
    ```

> **لماذا `az login`؟** تستخدم دفاتر Jupyter المصادقة باستخدام `AzureCliCredential` (أو `DefaultAzureCredential`، التي تلتقط أيضًا تسجيل دخول Azure CLI الخاص بك) من حزمة `azure-identity`. هذا يعني أن جلسة Azure CLI الخاصة بك توفر بيانات الاعتماد — لا مفاتيح أو أسرار API في ملف `.env`. هذه [أفضل ممارسة أمانية](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### الخطوة 4: إنشاء ملف `.env` الخاص بك

انسخ ملف المثال:

```bash
# زي شل/باش
cp .env.example .env
```

```powershell
# باورشيل
Copy-Item .env.example .env
```

افتح `.env` واملأ هذين القيمتين:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | بوابة Foundry → مشروعك → صفحة **نظرة عامة** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | بوابة Foundry → **Models + Endpoints** → اسم النموذج المنشور |

هذا كل شيء لمعظم الدروس! ستقوم دفاتر Jupyter بالمصادقة تلقائيًا عبر جلسة `az login` الخاصة بك.

### الخطوة 5: تثبيت تبعيات Python

```bash
pip install -r requirements.txt
```

نوصي بتشغيل هذا داخل البيئة الافتراضية التي أنشأتها سابقًا.

## إعداد اختياري: بحث Azure AI (الدروس 5 و16)

يعمل دفتر Lesson 5 (Agentic RAG) ودفتر Lesson 16 بشكل افتراضي مع **قاعدة معرفة في الذاكرة** — لا حاجة لموارد Azure إضافية. إذا كنت ترغب في دعمهما بفهرس حقيقي لـ **Azure AI Search**، لاحظ أن دفتر Lesson 16 يستخدم حاليًا المصادقة بالمفتاح: يتحول من بحث الذاكرة إلى Azure AI Search فقط عندما يتم تعيين **كل من** `AZURE_SEARCH_SERVICE_ENDPOINT` **و** `AZURE_SEARCH_API_KEY`، وإلا يبقى على البحث في الذاكرة — لذا لتشغيله ضد فهرس حقيقي يجب تعيين مفتاح المسؤول أيضًا. المصادقة بدون مفتاح باستخدام Microsoft Entra ID (RBAC) هي الطريقة الموصى بها لكود الإنتاج الخاص بك، متوافقة مع تدفق `az login` المستخدم في كل مكان آخر في هذه الدورة.

تنطبق خطوات RBAC التالية على عينات دليل الإعداد والشفرة الخاصة بك. لا تمكّن المصادقة بدون مفتاح في دفتر Lesson 16؛ يحتاج Lesson 16 إلى كل من نقطة النهاية ومفتاح المسؤول لاستخدام Azure AI Search.

1. **فعّل الوصول المستند إلى الدور** على خدمة البحث الخاصة بك:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **قم بتعيين الأدوار المطلوبة لنفسك** (إنشاء/تحميل الفهارس والاستعلام):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **أضف نقطة النهاية** إلى ملف `.env` الخاص بك:

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | بوابة Azure → مورد **Azure AI Search** الخاص بك → **نظرة عامة** → URL |
| `AZURE_SEARCH_API_KEY` | مطلوب (مع نقطة النهاية) لتمكين Azure AI Search في دفتر Lesson 16، الذي يستخدم المصادقة بالمفتاح. بوابة Azure → **الإعدادات** → **المفاتيح** → مفتاح المسؤول الأساسي |

> **لماذا بدون مفتاح؟** تمنح مفاتيح المسؤول حق الكتابة الكامل على خدمة البحث وقد تتسرب عبر ملفات `.env`. باستخدام RBAC، يتم استخدام هوية `az login` الخاصة بك بدلاً من ذلك — نفس نمط Entra ID بدون مفتاح الذي تستخدمه دفاتر الدورة (عبر `AzureCliCredential` / `DefaultAzureCredential`). انظر [الاتصال بـ Azure AI Search باستخدام الأدوار](https://learn.microsoft.com/azure/search/search-security-rbac).

راجع [دليل إعداد Azure AI Search](./AzureSearch.md) لنماذج كاملة لإنشاء الفهارس بـ Python و .NET.

## إعداد إضافي للدروس التي تستدعي Azure OpenAI مباشرة (الدروس 6 و8)

تستدعي بعض دفاتر الدروس 6 و8 **Azure OpenAI** مباشرة (باستخدام **واجهة Responses API**) بدلاً من المرور عبر مشروع Microsoft Foundry. كانت هذه العينات تستخدم سابقًا نماذج GitHub، التي تم إيقافها ولا تدعم Responses API. أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | بوابة Azure → مورد **Azure OpenAI** الخاص بك → **المفاتيح ونقطة النهاية** → نقطة النهاية (مثال `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | اسم النموذج المنشور (مثلاً `gpt-5-mini`) الذي يدعم Responses API |
| `AZURE_OPENAI_API_KEY` | اختياري — فقط إذا كنت تستخدم المصادقة بالمفتاح بدلاً من `az login` / Entra ID |

> تستخدم Responses API نقطة نهاية `/openai/v1/` المستقرة، لذلك لا توجد حاجة لـ `api-version`. قم بتسجيل الدخول باستخدام `az login` لاستخدام مصادقة Entra ID بدون مفتاح.

## موفر بديل: MiniMax (متوافق مع OpenAI)

توفر [MiniMax](https://platform.minimaxi.com/) نماذج ذات سياق كبير (حتى 204K توكن) من خلال API متوافق مع OpenAI. نظرًا لأن `OpenAIChatClient` في Microsoft Agent Framework يعمل مع أي نقطة نهاية متوافقة مع OpenAI، يمكنك استخدام MiniMax كبديل مباشر للدروس التي تستخدم `OpenAIChatClient`.

أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `MINIMAX_API_KEY` | منصة [MiniMax](https://platform.minimaxi.com/) → مفاتيح API |
| `MINIMAX_BASE_URL` | استخدم `https://api.minimax.io/v1` (القيمة الافتراضية) |
| `MINIMAX_MODEL_ID` | اسم النموذج لاستخدامه (مثلاً `MiniMax-M3`) |

**نماذج مثال**: `MiniMax-M3` (موصى به)، `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (استجابات أسرع). أسماء النماذج والتوفر يمكن أن تتغير مع الوقت، وقد يعتمد الوصول إلى نموذج معين على حسابك.

ستكتشف عينات الكود التي تستخدم `OpenAIChatClient` (مثل سير عمل حجز الفنادق في الدرس 14) تلقائيًا وتستخدم إعداد MiniMax الخاص بك عند تعيين `MINIMAX_API_KEY`.


## مزود بديل: Novita AI (متوافق مع OpenAI)

يوفر [Novita AI](https://novita.ai/llm-api) واجهة برمجة تطبيقات متوافقة مع OpenAI للنماذج اللغوية الكبيرة مفتوحة المصدر والحديثة (DeepSeek، Llama، Qwen، والمزيد). نظرًا لأن `OpenAIChatClient` في Microsoft Agent Framework يعمل مع أي نقطة نهاية متوافقة مع OpenAI، يمكنك استخدام Novita AI كبديل مباشر لـ Azure OpenAI أو OpenAI.

أضف هذه المتغيرات إلى ملف `.env` الخاص بك:

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `NOVITA_API_KEY` | [لوحة تحكم Novita AI](https://novita.ai/settings/key-management) → مفاتيح API |
| `NOVITA_BASE_URL` | استخدم `https://api.novita.ai/openai/v1` (القيمة الافتراضية) |
| `NOVITA_MODEL_ID` | اسم النموذج الذي تريد استخدامه (مثل `moonshotai/kimi-k3`) |

**نماذج أمثلة**: `moonshotai/kimi-k3`، `zai-org/glm-5.2`، `deepseek/deepseek-v4-flash-0731`. يستضيف Novita AI أيضًا العديد من عائلات النماذج مفتوحة المصدر الأخرى (Llama, Qwen, GLM، والمزيد) — تحقق من [مكتبة نماذج Novita AI](https://novita.ai/llm-api) للاطلاع على القائمة الحالية للنماذج المتاحة ومعرفات النماذج الخاصة بها.

العينات الحالية لا تستخدم متغيرات `NOVITA_*` تلقائيًا. لاستخدام Novita AI، مرر هذه القيم صراحة عند إنشاء `OpenAIChatClient` في العينة التي تستديرها.

## مزود بديل: Foundry Local (تشغيل النماذج على الجهاز)

[Foundry Local](https://foundrylocal.ai) هو بيئة تشغيل خفيفة تقوم بتنزيل وإدارة وتقديم نماذج اللغة **كليًا على جهازك الخاص** عبر واجهة برمجة تطبيقات متوافقة مع OpenAI — بدون الحاجة للسحابة.

نظرًا لأن `OpenAIChatClient` في Microsoft Agent Framework يعمل مع أي نقطة نهاية متوافقة مع OpenAI، فإن Foundry Local هو بديل محلي مباشر لـ Azure OpenAI.

**1. قم بتثبيت Foundry Local**

```bash
# ويندوز
winget install Microsoft.FoundryLocal

# ماك أو إس
brew install foundrylocal
```

**2. قم بتنزيل وتشغيل نموذج** (سيتم أيضًا بدء الخدمة المحلية):

```bash
foundry model list          # عرض النماذج المتاحة
foundry model run phi-4-mini
```

**3. قم بتثبيت SDK لبايثون** المستخدم لاكتشاف نقطة النهاية المحلية:

```bash
pip install foundry-local-sdk
```

**4. وجه Microsoft Agent Framework إلى النموذج المحلي الخاص بك:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# يقوم بتنزيل النموذج (إذا لزم الأمر) وتشغيله محليًا، ثم يكتشف نقطة النهاية/المنفذ.
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

> **ملاحظة:** يقوم Foundry Local بالكشف عن نقطة نهاية **مكالمات الدردشة** المتوافقة مع OpenAI. استخدمها للتطوير المحلي والسيناريوهات دون اتصال. للحصول على مجموعة ميزات **API الردود** الكاملة (المحادثات ذات الحالة، إلخ)، استخدم Azure OpenAI أو مشروع Microsoft Foundry.

## إعداد إضافي للدرس 8 (تدفق عمل ربط بينغ)

يستخدم دفتر التدفق المشروط في الدرس 8 **ربط بينغ** عبر Microsoft Foundry. إذا كنت تخطط لتشغيل تلك العينة، أضف هذا المتغير إلى ملف `.env` الخاص بك:

| المتغير | مكان العثور عليه |
|----------|-----------------|
| `BING_CONNECTION_ID` | بوابة Microsoft Foundry → مشروعك → **الإدارة** → **الموارد المتصلة** → اتصال بينغ الخاص بك → انسخ معرف الاتصال |

## استكشاف المشكلات وإصلاحها

### أخطاء تحقق شهادة SSL على macOS

إذا كنت تستخدم macOS وواجهت خطأ مثل:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

هذه مشكلة معروفة في بايثون على macOS حيث لا تُعتمد شهادات SSL للنظام تلقائيًا. جرب الحلول التالية وفقًا للترتيب:

**الخيار 1: تشغيل سكريبت تثبيت الشهادات الخاص ببايثون (موصى به)**

```bash
# استبدل 3.XX بإصدار بايثون المثبت لديك (مثلاً، 3.12 أو 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**الخيار 2: استخدم `connection_verify=False` في دفتر الملاحظات (لدفاتر ملاحظات GitHub Models فقط)**

في دفتر ملاحظات الدرس 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)، هناك حل بديل معلق مسبقًا. قم بإزالة التعليق عن `connection_verify=False` عند حدوث أخطاء في الشهادة:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # تعطيل التحقق من SSL إذا واجهت أخطاء في الشهادة
)
```

> **⚠️ تحذير:** تعطيل التحقق من SSL (`connection_verify=False`) يقلل من الأمان بتخطي التحقق من الشهادة. استخدم هذا فقط كحل مؤقت في بيئات التطوير. لا تستخدمه أبدًا في الإنتاج.

**الخيار 3: تثبيت واستخدام `truststore`**

```bash
pip install truststore
```

ثم أضف التالي إلى أعلى دفتر الملاحظات أو السكريبت قبل إجراء أي طلبات شبكة:

```python
import truststore
truststore.inject_into_ssl()
```

## عالق في مكان ما؟

إذا واجهت أي مشكلات في تشغيل هذا الإعداد، انضم إلى <a href="https://discord.gg/kzRShWzttr" target="_blank">خادم Discord لمجتمع Azure AI</a> أو <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">أنشئ مشكلة (issue)</a>.

## الدرس التالي

أنت الآن جاهز لتشغيل الشيفرة الخاصة بهذا المساق. استمتع بالتعلم عن عالم وكلاء الذكاء الاصطناعي! 

[مقدمة في وكلاء الذكاء الاصطناعي وحالات استخدامها](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->