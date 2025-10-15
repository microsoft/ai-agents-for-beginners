<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:37:58+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fa"
}
-->
# تنظیم دوره

## مقدمه

در این درس، نحوه اجرای نمونه کدهای این دوره را بررسی خواهیم کرد.

## پیوستن به سایر فراگیران و دریافت کمک

قبل از اینکه مخزن خود را کلون کنید، به [کانال دیسکورد AI Agents For Beginners](https://aka.ms/ai-agents/discord) بپیوندید تا در مورد تنظیمات، سوالات مربوط به دوره یا ارتباط با سایر فراگیران کمک بگیرید.

## کلون یا فورک کردن این مخزن

برای شروع، لطفاً مخزن GitHub را کلون یا فورک کنید. این کار نسخه‌ای از مطالب دوره را برای شما ایجاد می‌کند تا بتوانید کدها را اجرا، آزمایش و تغییر دهید!

این کار را می‌توانید با کلیک بر روی لینک <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">فورک کردن مخزن</a> انجام دهید.

اکنون باید نسخه فورک شده خود از این دوره را در لینک زیر داشته باشید:

![مخزن فورک شده](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.fa.png)

### کلون سطحی (توصیه شده برای کارگاه / Codespaces)

  > کل مخزن ممکن است بزرگ باشد (~3 گیگابایت) زمانی که تاریخچه کامل و همه فایل‌ها را دانلود کنید. اگر فقط در کارگاه شرکت می‌کنید یا فقط به چند پوشه درس نیاز دارید، کلون سطحی (یا کلون پراکنده) بیشتر این دانلود را با کوتاه کردن تاریخچه و/یا حذف بلوک‌ها اجتناب می‌کند.

#### کلون سطحی سریع — تاریخچه حداقلی، همه فایل‌ها

در دستورات زیر `<your-username>` را با URL فورک خود (یا URL اصلی اگر ترجیح می‌دهید) جایگزین کنید.

برای کلون کردن فقط تاریخچه آخرین کامیت (دانلود کوچک):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

برای کلون کردن یک شاخه خاص:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### کلون جزئی (پراکنده) — بلوک‌های حداقلی + فقط پوشه‌های انتخاب شده

این روش از کلون جزئی و بررسی پراکنده استفاده می‌کند (نیاز به Git 2.25+ دارد و Git مدرن با پشتیبانی از کلون جزئی توصیه می‌شود):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

وارد پوشه مخزن شوید:

برای bash:

```bash
cd ai-agents-for-beginners
```

برای Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

سپس مشخص کنید کدام پوشه‌ها را می‌خواهید (مثال زیر دو پوشه را نشان می‌دهد):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

پس از کلون کردن و بررسی فایل‌ها، اگر فقط به فایل‌ها نیاز دارید و می‌خواهید فضای بیشتری آزاد کنید (بدون تاریخچه گیت)، لطفاً متادیتای مخزن را حذف کنید (💀غیرقابل بازگشت — تمام قابلیت‌های گیت را از دست خواهید داد: بدون کامیت، پول، پوش و دسترسی به تاریخچه).

برای لینوکس/macOS:

```bash
rm -rf .git
```

برای ویندوز:

```powershell
Remove-Item -Recurse -Force .git
```

#### استفاده از GitHub Codespaces (توصیه شده برای جلوگیری از دانلودهای بزرگ محلی)

- یک Codespace جدید برای این مخزن از طریق [رابط کاربری GitHub](https://github.com/codespaces) ایجاد کنید.  

- در ترمینال Codespace تازه ایجاد شده، یکی از دستورات کلون سطحی/پراکنده بالا را اجرا کنید تا فقط پوشه‌های درس مورد نیاز را به فضای کاری Codespace بیاورید.
- اختیاری: پس از کلون کردن داخل Codespaces، .git را حذف کنید تا فضای اضافی آزاد شود (دستورات حذف بالا را ببینید).
- توجه: اگر ترجیح می‌دهید مخزن را مستقیماً در Codespaces باز کنید (بدون کلون اضافی)، توجه داشته باشید که Codespaces محیط devcontainer را ایجاد می‌کند و ممکن است همچنان بیش از نیاز شما فراهم کند. کلون کردن یک نسخه سطحی داخل یک Codespace تازه به شما کنترل بیشتری بر استفاده از دیسک می‌دهد.

#### نکات

- همیشه URL کلون را با فورک خود جایگزین کنید اگر می‌خواهید ویرایش/کامیت کنید.
- اگر بعداً به تاریخچه یا فایل‌های بیشتری نیاز داشتید، می‌توانید آن‌ها را دریافت کنید یا بررسی پراکنده را تنظیم کنید تا پوشه‌های اضافی را شامل شود.

## اجرای کد

این دوره مجموعه‌ای از نوت‌بوک‌های Jupyter را ارائه می‌دهد که می‌توانید با آن‌ها تجربه عملی ساخت عوامل هوش مصنوعی را کسب کنید.

نمونه کدها از موارد زیر استفاده می‌کنند:

**نیازمند حساب GitHub - رایگان**:

1) چارچوب Semantic Kernel Agent + بازار مدل‌های GitHub. با برچسب (semantic-kernel.ipynb)
2) چارچوب AutoGen + بازار مدل‌های GitHub. با برچسب (autogen.ipynb)

**نیازمند اشتراک Azure**:
3) Azure AI Foundry + سرویس عامل هوش مصنوعی Azure. با برچسب (azureaiagent.ipynb)

ما شما را تشویق می‌کنیم که هر سه نوع مثال را امتحان کنید تا ببینید کدام یک برای شما بهتر عمل می‌کند.

هر گزینه‌ای که انتخاب کنید، تعیین می‌کند که کدام مراحل تنظیم را باید در زیر دنبال کنید:

## الزامات

- Python 3.12+
  - **NOTE**: اگر Python3.12 نصب نشده است، مطمئن شوید که آن را نصب کنید. سپس با استفاده از python3.12 دایرکتوری venv خود را ایجاد کنید تا نسخه‌های صحیح از فایل requirements.txt نصب شوند.
  
    > مثال

    ایجاد دایرکتوری محیط مجازی Python:

    ``` bash
    python3 -m venv venv
    ```

    سپس محیط venv را فعال کنید برای:

    macOS و لینوکس

    ```bash
    source venv/bin/activate
    ```
  
    ویندوز

    ```bash
    venv\Scripts\activate
    ```

- حساب GitHub - برای دسترسی به بازار مدل‌های GitHub
- اشتراک Azure - برای دسترسی به Azure AI Foundry
- حساب Azure AI Foundry - برای دسترسی به سرویس عامل هوش مصنوعی Azure

ما یک فایل `requirements.txt` در ریشه این مخزن قرار داده‌ایم که شامل تمام بسته‌های مورد نیاز Python برای اجرای نمونه کدها است.

می‌توانید آن‌ها را با اجرای دستور زیر در ترمینال در ریشه مخزن نصب کنید:

```bash
pip install -r requirements.txt
```

ما توصیه می‌کنیم یک محیط مجازی Python ایجاد کنید تا از هرگونه تضاد و مشکل جلوگیری شود.

## تنظیم VSCode
اطمینان حاصل کنید که از نسخه صحیح Python در VSCode استفاده می‌کنید.

![تصویر](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## تنظیم برای نمونه‌ها با استفاده از مدل‌های GitHub 

### مرحله 1: دریافت توکن دسترسی شخصی GitHub (PAT)

این دوره از بازار مدل‌های GitHub استفاده می‌کند که دسترسی رایگان به مدل‌های زبان بزرگ (LLM) را فراهم می‌کند که شما برای ساخت عوامل هوش مصنوعی استفاده خواهید کرد.

برای استفاده از مدل‌های GitHub، باید یک [توکن دسترسی شخصی GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) ایجاد کنید.

این کار را می‌توانید با رفتن به <a href="https://github.com/settings/personal-access-tokens" target="_blank">تنظیمات توکن دسترسی شخصی</a> در حساب GitHub خود انجام دهید.

لطفاً هنگام ایجاد توکن، [اصل حداقل امتیاز](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) را دنبال کنید. این بدان معناست که باید فقط مجوزهایی را که برای اجرای نمونه کدهای این دوره نیاز دارید به توکن بدهید.

1. گزینه `توکن‌های دقیق` را در سمت چپ صفحه خود انتخاب کنید و به **تنظیمات توسعه‌دهنده** بروید.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.fa.png)

    سپس گزینه `ایجاد توکن جدید` را انتخاب کنید.

    ![ایجاد توکن](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.fa.png)

2. یک نام توصیفی برای توکن خود وارد کنید که هدف آن را نشان دهد و شناسایی آن را در آینده آسان کند.


    🔐 توصیه برای مدت زمان توکن

    مدت زمان توصیه شده: 30 روز
    برای امنیت بیشتر، می‌توانید مدت زمان کوتاه‌تری مانند 7 روز 🛡️ انتخاب کنید.
    این یک روش عالی برای تعیین هدف شخصی و تکمیل دوره در حالی است که انگیزه یادگیری شما بالا است 🚀.

    ![نام و تاریخ انقضای توکن](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.fa.png)

3. دامنه توکن را به فورک این مخزن محدود کنید.

    ![محدود کردن دامنه به مخزن فورک شده](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.fa.png)

4. مجوزهای توکن را محدود کنید: در زیر **Permissions**، بر روی تب **Account** کلیک کنید و دکمه "+ Add permissions" را فشار دهید. یک منوی کشویی ظاهر خواهد شد. لطفاً به دنبال **Models** بگردید و کادر مربوط به آن را علامت بزنید.
    ![افزودن مجوز مدل‌ها](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.fa.png)

5. قبل از ایجاد توکن، مجوزهای مورد نیاز را بررسی کنید. ![بررسی مجوزها](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.fa.png)

6. قبل از ایجاد توکن، مطمئن شوید که آماده ذخیره توکن در مکانی امن مانند یک گاوصندوق مدیریت رمز عبور هستید، زیرا پس از ایجاد آن دیگر نمایش داده نمی‌شود. ![ذخیره امن توکن](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.fa.png)

توکن جدیدی که ایجاد کرده‌اید را کپی کنید. اکنون باید این توکن را به فایل `.env` که در این دوره گنجانده شده است اضافه کنید.


### مرحله 2: ایجاد فایل `.env`

برای ایجاد فایل `.env` دستور زیر را در ترمینال خود اجرا کنید.

```bash
cp .env.example .env
```

این دستور فایل نمونه را کپی کرده و یک فایل `.env` در دایرکتوری شما ایجاد می‌کند که در آن مقادیر متغیرهای محیطی را پر می‌کنید.

با کپی کردن توکن خود، فایل `.env` را در ویرایشگر متن مورد علاقه خود باز کنید و توکن خود را در قسمت `GITHUB_TOKEN` قرار دهید.
![قسمت توکن GitHub](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.fa.png)


اکنون باید بتوانید نمونه کدهای این دوره را اجرا کنید.

## تنظیم برای نمونه‌ها با استفاده از Azure AI Foundry و سرویس عامل هوش مصنوعی Azure

### مرحله 1: دریافت نقطه پایانی پروژه Azure خود


مراحل ایجاد یک هاب و پروژه در Azure AI Foundry را دنبال کنید که در اینجا آمده است: [بررسی اجمالی منابع هاب](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


پس از ایجاد پروژه خود، باید رشته اتصال پروژه خود را دریافت کنید.

این کار را می‌توانید با رفتن به صفحه **Overview** پروژه خود در پورتال Azure AI Foundry انجام دهید.

![رشته اتصال پروژه](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.fa.png)

### مرحله 2: ایجاد فایل `.env`

برای ایجاد فایل `.env` دستور زیر را در ترمینال خود اجرا کنید.

```bash
cp .env.example .env
```

این دستور فایل نمونه را کپی کرده و یک فایل `.env` در دایرکتوری شما ایجاد می‌کند که در آن مقادیر متغیرهای محیطی را پر می‌کنید.

با کپی کردن توکن خود، فایل `.env` را در ویرایشگر متن مورد علاقه خود باز کنید و توکن خود را در قسمت `PROJECT_ENDPOINT` قرار دهید.

### مرحله 3: ورود به Azure

به عنوان یک بهترین روش امنیتی، از [احراز هویت بدون کلید](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) برای احراز هویت به Azure OpenAI با Microsoft Entra ID استفاده خواهیم کرد. 

سپس، یک ترمینال باز کنید و دستور `az login --use-device-code` را اجرا کنید تا وارد حساب Azure خود شوید.

پس از ورود، اشتراک خود را در ترمینال انتخاب کنید.


## متغیرهای محیطی اضافی - جستجوی Azure و Azure OpenAI 

برای درس Agentic RAG - درس 5 - نمونه‌هایی وجود دارد که از جستجوی Azure و Azure OpenAI استفاده می‌کنند.

اگر می‌خواهید این نمونه‌ها را اجرا کنید، باید متغیرهای محیطی زیر را به فایل `.env` خود اضافه کنید:

### صفحه Overview (پروژه)

- `AZURE_SUBSCRIPTION_ID` - جزئیات **پروژه** را در صفحه **Overview** پروژه خود بررسی کنید.

- `AZURE_AI_PROJECT_NAME` - در بالای صفحه **Overview** پروژه خود نگاه کنید.

- `AZURE_OPENAI_SERVICE` - این مورد را در تب **Included capabilities** برای **سرویس Azure OpenAI** در صفحه **Overview** پیدا کنید.

### مرکز مدیریت

- `AZURE_OPENAI_RESOURCE_GROUP` - به **Project properties** در صفحه **Overview** مرکز مدیریت بروید.

- `GLOBAL_LLM_SERVICE` - در زیر **Connected resources**، نام اتصال **Azure AI Services** را پیدا کنید. اگر لیست نشده است، در **پورتال Azure** زیر گروه منابع خود برای نام منبع AI Services بررسی کنید.

### صفحه مدل‌ها + نقاط پایانی

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - مدل جاسازی خود را انتخاب کنید (مثلاً `text-embedding-ada-002`) و نام **Deployment name** را از جزئیات مدل یادداشت کنید.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - مدل چت خود را انتخاب کنید (مثلاً `gpt-4o-mini`) و نام **Deployment name** را از جزئیات مدل یادداشت کنید.

### پورتال Azure

- `AZURE_OPENAI_ENDPOINT` - به دنبال **سرویس‌های Azure AI** بگردید، روی آن کلیک کنید، سپس به **Resource Management**، **Keys and Endpoint** بروید، به پایین صفحه "نقاط پایانی Azure OpenAI" بروید و یکی از نقاط پایانی "Language APIs" را کپی کنید.

- `AZURE_OPENAI_API_KEY` - از همان صفحه، کلید KEY 1 یا KEY 2 را کپی کنید.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - منبع **جستجوی Azure AI** خود را پیدا کنید، روی آن کلیک کنید و صفحه **Overview** را مشاهده کنید.

- `AZURE_SEARCH_API_KEY` - سپس به **Settings** و سپس **Keys** بروید تا کلید اصلی یا کلید فرعی مدیر را کپی کنید.

### صفحه وب خارجی

- `AZURE_OPENAI_API_VERSION` - به صفحه [چرخه عمر نسخه API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) در زیر **آخرین نسخه GA API** مراجعه کنید.

### تنظیم احراز هویت بدون کلید

به جای کدنویسی ثابت اعتبارنامه‌های خود، از اتصال بدون کلید با Azure OpenAI استفاده خواهیم کرد. برای این کار، `DefaultAzureCredential` را وارد کرده و بعداً تابع `DefaultAzureCredential` را برای دریافت اعتبارنامه فراخوانی خواهیم کرد.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## جایی گیر کرده‌اید؟
اگر در اجرای این تنظیمات مشکلی دارید، به <a href="https://discord.gg/kzRShWzttr" target="_blank">دیسکورد انجمن Azure AI</a> ما بپیوندید یا یک <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">مشکل جدید ایجاد کنید</a>.

## درس بعدی

اکنون آماده‌اید تا کد این دوره را اجرا کنید. از یادگیری بیشتر درباره دنیای عوامل هوش مصنوعی لذت ببرید!

[مقدمه‌ای بر عوامل هوش مصنوعی و موارد استفاده از عوامل](../01-intro-to-ai-agents/README.md)

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.