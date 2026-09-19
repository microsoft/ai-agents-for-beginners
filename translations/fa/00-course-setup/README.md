# راه‌اندازی دوره

## مقدمه

این درس نحوه اجرای نمونه‌کدهای این دوره را پوشش می‌دهد.

## به دیگر یادگیرندگان بپیوندید و کمک بگیرید

قبل از شروع کلون کردن مخزن خود، به [کانال دیسکورد AI Agents For Beginners](https://aka.ms/ai-agents/discord) بپیوندید تا برای راه‌اندازی، پرسش‌ها درباره دوره و ارتباط با دیگر یادگیرندگان کمک بگیرید.

## کلون یا فورک این مخزن

برای شروع، لطفاً مخزن GitHub را کلون یا فورک کنید. این کار نسخه‌ی خودتان از محتوای دوره را ایجاد می‌کند تا بتوانید کدها را اجرا، تست و تغییر دهید!

این کار با کلیک روی لینک <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">فورک کردن مخزن</a> انجام می‌شود.

اکنون باید نسخه فورک شده‌ی خودتان از این دوره را در لینک زیر داشته باشید:

![Forked Repo](../../../translated_images/fa/forked-repo.33f27ca1901baa6a.webp)

### کلون سطحی (توصیه شده برای کارگاه / Codespaces)

  > کل مخزن می‌تواند بزرگ باشد (~۳ گیگابایت) وقتی کل تاریخچه و همه فایل‌ها را دانلود می‌کنید. اگر فقط در کارگاه شرکت می‌کنید یا فقط به چند پوشه درس نیاز دارید، کلون سطحی (یا کلون پراکنده) بسیار کمتر دانلود می‌کند.

#### کلون سریع سطحی — حداقل تاریخچه، همه فایل‌ها

`<your-username>` را در فرمان‌های زیر با URL فورک خود (یا URL اصلی اگر ترجیح می‌دهید) جایگزین کنید.

برای کلون کردن فقط آخرین تاریخچه کامیت (دانلود کم):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

برای کلون کردن یک شاخه خاص:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### کلون جزئی (پراکنده) — بلاک‌های حداقلی + فقط پوشه‌های انتخابی

این روش از کلون جزئی و sparse-checkout استفاده می‌کند (نیازمند گیت نسخه 2.25+ و توصیه می‌شود گیت مدرن با پشتیبانی کلون جزئی):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

وارد پوشه مخزن شوید:

```bash
cd ai-agents-for-beginners
```

سپس مشخص کنید کدام پوشه‌ها را می‌خواهید (مثال زیر دو پوشه را نشان می‌دهد):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

پس از کلون و بررسی فایل‌ها، اگر فقط به فایل‌ها نیاز دارید و می‌خواهید فضا آزاد کنید (بدون تاریخچه گیت)، لطفاً متادیتای مخزن را حذف کنید (💀غیرقابل بازگشت — همه قابلیت‌های گیت را از دست خواهید داد):

```bash
# زد شل/باش
rm -rf .git
```

```powershell
# پاورشل
Remove-Item -Recurse -Force .git
```

#### استفاده از GitHub Codespaces (توصیه شده برای اجتناب از دانلودهای بزرگ محلی)

- یک Codespace جدید برای این مخزن از طریق [رابط کاربری GitHub](https://github.com/codespaces) بسازید.

- در ترمینال Codespace تازه ساخته شده، یکی از دستورهای کلون سطحی/پراکنده بالا را اجرا کنید تا فقط پوشه‌های درس مورد نیاز به فضای کاری Codespace آورده شوند.
- اختیاری: بعد از کلون داخل Codespaces، برای آزاد کردن فضای اضافه، دایرکتوری .git را حذف کنید (دستورات حذف را بالا ببینید).
- نکته: اگر ترجیح می‌دهید مستقیماً مخزن را در Codespaces باز کنید (بدون کلون اضافی)، توجه داشته باشید Codespaces محیط devcontainer را می‌سازد و ممکن است هنوز بیشتر از نیازتان منابع فراهم کند.

#### نکات

- همیشه URL کلون را با فورک خود جایگزین کنید اگر قصد ویرایش/کامیت دارید.
- اگر بعداً به تاریخچه یا فایل‌های بیشتری نیاز داشتید، می‌توانید آن‌ها را دریافت کنید یا sparse-checkout را تنظیم کنید تا پوشه‌های بیشتری اضافه شود.

## اجرای کد

این دوره مجموعه‌ای از دفترچه‌های Jupyter را ارائه می‌دهد که می‌توانید برای کسب تجربه عملی در ساخت عامل‌های هوش مصنوعی اجرا کنید.

نمونه‌های کد از **چارچوب عامل مایکروسافت (MAF)** با `FoundryChatClient` استفاده می‌کنند که به خدمت **Microsoft Foundry Agent Service V2** (API پاسخ‌ها) از طریق **Microsoft Foundry** متصل می‌شود.

همه دفترچه‌های پایتون با نام `*-python-agent-framework.ipynb` مشخص شده‌اند.

## ملزومات

- پایتون 3.12+
  - **توجه**: اگر پایتون 3.12 نصب ندارید، مطمئن شوید آن را نصب کنید. سپس با استفاده از python3.12 محیط مجازی خود را بسازید تا نسخه‌های درست از فایل requirements.txt نصب شود.
  
    >مثال

    ساخت دایرکتوری محیط مجازی پایتون:

    ```bash
    python -m venv venv
    ```

    سپس محیط مجازی را فعال کنید برای:

    ```bash
    # زد-اچ/باش
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- دات‌نت 10+: برای نمونه‌های کدی که از دات‌نت استفاده می‌کنند، مطمئن شوید [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا نسخه جدیدتر نصب شده باشد. سپس نسخه نصب شده SDK دات‌نت را چک کنید:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — برای احراز هویت لازم است. از [aka.ms/installazurecli](https://aka.ms/installazurecli) نصب کنید.
- **اشتراک Azure** — برای دسترسی به Microsoft Foundry و Microsoft Foundry Agent Service.
- **پروژه Microsoft Foundry** — یک پروژه با مدل مستقر شده (مثلاً `gpt-5-mini`). به [مرحله 1](#مرحله-1-ساخت-پروژه-microsoft-foundry) زیر مراجعه کنید.

ما فایلی به نام `requirements.txt` در ریشه این مخزن قرار داده‌ایم که شامل تمام بسته‌های پایتون مورد نیاز برای اجرای نمونه‌کدها است.

شما می‌توانید آن‌ها را با اجرای دستور زیر در ترمینال خود در ریشه مخزن نصب کنید:

```bash
pip install -r requirements.txt
```

توصیه می‌کنیم یک محیط مجازی پایتون ایجاد کنید تا از تداخل‌ها و مشکلات جلوگیری شود.

## راه‌اندازی VSCode

مطمئن شوید که در VSCode از نسخه صحیح پایتون استفاده می‌کنید.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## راه‌اندازی Microsoft Foundry و Microsoft Foundry Agent Service

### مرحله 1: ساخت پروژه Microsoft Foundry

برای اجرای دفترچه‌ها به یک **هاب** و **پروژه** در Microsoft Foundry نیاز دارید که دارای مدلی مستقر شده باشد.

1. به [ai.azure.com](https://ai.azure.com) بروید و با حساب Azure خود وارد شوید.
2. یک **هاب** بسازید (یا از هاب موجود استفاده کنید). ببینید: [مرور منابع هاب](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. درون هاب، یک **پروژه** بسازید.
4. از بخش **Models + Endpoints** → **Deploy model** یک مدل مستقر کنید (مثلاً `gpt-5-mini`).

### مرحله 2: دریافت آدرس پایان پروژه و نام استقرار مدل

از پروژه خود در پرتال Microsoft Foundry:

- **آدرس پایان پروژه** — به صفحه **Overview** بروید و URL پایان را کپی کنید.

![Project Connection String](../../../translated_images/fa/project-endpoint.8cf04c9975bbfbf1.webp)

- **نام استقرار مدل** — به **Models + Endpoints** بروید، مدل مستقر شده خود را انتخاب کنید و نام **Deployment** را یادداشت کنید (مثلاً `gpt-5-mini`).

### مرحله 3: ورود به Azure با دستور `az login`

بیشتر دفترچه‌ها از طریق **ورود به Azure CLI** شما احراز هویت می‌شوند — با استفاده از `AzureCliCredential` یا `DefaultAzureCredential` (که جلسۀ `az login` شما را می‌گیرد) از بسته `azure-identity` — پس نیازی به کلیدهای API ندارند. چند درس و ادغام‌های اختیاری از کلید API استفاده می‌کنند؛ برای متغیرهای محیطی اضافی، پیش‌نیازهای هر درس را بررسی کنید. برای این کار باید از طریق Azure CLI وارد شده باشید.

1. **اگر Azure CLI نصب ندارید، نصب کنید:** [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **ورود** با اجرای:

    ```bash
    az login
    ```

    اگر در محیط ریموت/Codespace بدون مرورگر هستید:

    ```bash
    az login --use-device-code
    ```

3. **انتخاب اشتراک** اگر درخواست شد — اشتراکی را انتخاب کنید که پروژه Foundry شما در آن است.

4. **بررسی** اینکه وارد شده‌اید:

    ```bash
    az account show
    ```

> **چرا `az login`؟** دفترچه‌ها با استفاده از `AzureCliCredential` (یا `DefaultAzureCredential` که ورود Azure CLI شما را نیز می‌گیرد) از بسته `azure-identity` احراز هویت می‌شوند. بنابراین جلسه Azure CLI شما اعتبارها را فراهم می‌کند — نیازی به کلیدهای API یا رازها در فایل `.env` نیست. این [یک بهترین روش امنیتی](https://learn.microsoft.com/azure/developer/ai/keyless-connections) است.

### مرحله 4: ایجاد فایل `.env` خود

فایل نمونه را کپی کنید:

```bash
# زد شل/باش
cp .env.example .env
```

```powershell
# پاورشل
Copy-Item .env.example .env
```

فایل `.env` را باز کنید و دو مقدار زیر را پر کنید:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| متغیر | محل یافتن |
|---------|-----------|
| `AZURE_AI_PROJECT_ENDPOINT` | پرتال Foundry → پروژه شما → صفحه **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | پرتال Foundry → **Models + Endpoints** → نام مدل مستقر شما |

این برای بیشتر درس‌ها کافی است! دفترچه‌ها به‌طور خودکار از طریق جلسه `az login` شما احراز هویت می‌کنند.

### مرحله 5: نصب وابستگی‌های پایتون

```bash
pip install -r requirements.txt
```

توصیه می‌شود این دستور را در داخل محیط مجازی که قبلاً ساختید اجرا کنید.

## راه‌اندازی اختیاری: جستجوی Azure AI (درس‌های ۵ و ۱۶)

دفاتر درس ۵ (Agentic RAG) و ۱۶ به صورت پیش‌فرض با یک **پایگاه دانش در حافظه** اجرا می‌شوند — نیازی به منابع اضافه Azure نیست. اگر می‌خواهید آن‌ها را به یک شاخص واقعی **Azure AI Search** متصل کنید، توجه داشته باشید که **دفترچه درس ۱۶ در حال حاضر از احراز هویت با کلید استفاده می‌کند**: وقتی **هر دو مقدار** `AZURE_SEARCH_SERVICE_ENDPOINT` و `AZURE_SEARCH_API_KEY` تنظیم شده باشند، جستجو از حافظه به Azure AI Search تغییر می‌کند — پس برای استفاده از آن در مقابل یک شاخص واقعی باید کلید ادمین را هم تنظیم کنید. احراز هویت بدون کلید با Microsoft Entra ID (RBAC) رویکرد توصیه‌شده برای کدهای تولیدی شماست که مطابق با جریان `az login` در کل دوره است.

مراحل RBAC زیر برای نمونه‌های راهنمای راه‌اندازی و کد خود شما است. این موارد احراز هویت بدون کلید را در دفترچه درس ۱۶ فعال نمی‌کند؛ درس ۱۶ هنوز به هر دو مقدار پایان و کلید ادمین برای استفاده از Azure AI Search نیاز دارد.

۱. **فعال کردن دسترسی مبتنی بر نقش** روی سرویس جستجوی خود:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

۲. **اختصاص نقش‌های لازم به خودتان** (ساخت/بارگذاری شاخص‌ها و پرس و جو):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

۳. **اضافه کردن آدرس پایان به فایل `.env` خود:**

| متغیر | محل یافتن |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | پرتال Azure → منبع **Azure AI Search** شما → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | لازم (همراه با آدرس پایان) برای فعال‌سازی Azure AI Search در دفترچه درس ۱۶ که از احراز هویت کلید استفاده می‌کند. پرتال Azure → **Settings** → **Keys** → کلید ادمین اصلی |

> **چرا بدون کلید؟** کلیدهای ادمین دسترسی کامل نوشتن روی سرویس جستجوی شما می‌دهند و ممکن است از فایل‌های `.env` نشت کنند. با RBAC، هویت `az login` شما به جای آن استفاده می‌شود — همان الگوی بدون کلیدی Entra ID که دفترچه‌های دوره به صورت پیش‌فرض استفاده می‌کنند (از طریق `AzureCliCredential` / `DefaultAzureCredential`). نگاه کنید به [اتصال به Azure AI Search با استفاده از نقش‌ها](https://learn.microsoft.com/azure/search/search-security-rbac).

برای نمونه‌های کامل ایجاد شاخص در پایتون و دات‌نت، به [راهنمای راه‌اندازی Azure AI Search](./AzureSearch.md) مراجعه کنید.

## راه‌اندازی اضافی برای درس‌هایی که مستقیماً از Azure OpenAI استفاده می‌کنند (درس‌های ۶ و ۸)

برخی دفترچه‌ها در درس‌های ۶ و ۸ مستقیماً از **Azure OpenAI** با استفاده از **API پاسخ‌ها** فراخوانی می‌کنند، نه از طریق پروژه Microsoft Foundry. این نمونه‌ها قبلاً از مدل‌های GitHub استفاده می‌کردند که منسوخ شده و API پاسخ‌ها را پشتیبانی نمی‌کند. این متغیرها را به فایل `.env` خود اضافه کنید:

| متغیر | محل یافتن |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | پرتال Azure → منبع **Azure OpenAI** شما → **Keys and Endpoint** → Endpoint (مثلاً `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | نام مدل مستقر شده شما (مثلاً `gpt-5-mini`) که API پاسخ‌ها را پشتیبانی می‌کند |
| `AZURE_OPENAI_API_KEY` | اختیاری — فقط اگر از احراز هویت کلیدی به جای ورود `az login` / Entra ID استفاده می‌کنید |

> API پاسخ‌ها از آدرس ثابت `/openai/v1/` استفاده می‌کند، بنابراین نیازی به `api-version` نیست. برای استفاده از احراز هویت بدون کلید Entra ID، با `az login` وارد شوید.

## ارائه‌دهنده جایگزین: MiniMax (سازگار با OpenAI)

[MiniMax](https://platform.minimaxi.com/) مدل‌های با زمینه بزرگ (تا ۲۰۴ هزار توکن) را از طریق API سازگار با OpenAI فراهم می‌کند. از آنجایی که `OpenAIChatClient` در چارچوب عامل مایکروسافت با هر نقطه پایانی سازگار با OpenAI کار می‌کند، می‌توانید MiniMax را به عنوان جایگزین مستقیم برای درس‌هایی که از `OpenAIChatClient` استفاده می‌کنند به کار ببرید.

این متغیرها را به فایل `.env` خود اضافه کنید:

| متغیر | محل یافتن |
|----------|-----------------|
| `MINIMAX_API_KEY` | [پلتفرم MiniMax](https://platform.minimaxi.com/) → کلیدهای API |
| `MINIMAX_BASE_URL` | از `https://api.minimax.io/v1` استفاده کنید (مقدار پیش‌فرض) |
| `MINIMAX_MODEL_ID` | نام مدلی که می‌خواهید استفاده کنید (مثلاً، `MiniMax-M3`) |

**مدل‌های نمونه**: `MiniMax-M3` (توصیه شده)، `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (پاسخ‌های سریع‌تر). نام و در دسترس بودن مدل‌ها ممکن است در طول زمان تغییر کند و دسترسی به مدل خاصی ممکن است وابسته به حساب شما باشد.

نمونه‌های کدی که از `OpenAIChatClient` استفاده می‌کنند (مثلاً جریان رزرو هتل در درس ۱۴) وقتی `MINIMAX_API_KEY` تنظیم شده باشد، به‌طور خودکار تنظیمات MiniMax شما را تشخیص داده و استفاده می‌کنند.


## ارائه‌دهنده جایگزین: Novita AI (سازگار با OpenAI)

[Novita AI](https://novita.ai/llm-api) یک API سازگار با OpenAI برای مدل‌های زبان منبع‌باز و پیشرفته (DeepSeek، Llama، Qwen و غیره) ارائه می‌دهد. از آنجا که `OpenAIChatClient` چارچوب Microsoft Agent با هر نقطه انتهایی سازگار با OpenAI کار می‌کند، می‌توانید از Novita AI به عنوان جایگزینی مستقیم برای Azure OpenAI یا OpenAI استفاده کنید.

این متغیرها را به فایل `.env` خود اضافه کنید:

| متغیر | محل یافتن |
|----------|-----------------|
| `NOVITA_API_KEY` | [داشبورد Novita AI](https://novita.ai/settings/key-management) → کلیدهای API |
| `NOVITA_BASE_URL` | از `https://api.novita.ai/openai/v1` استفاده کنید (مقدار پیش‌فرض) |
| `NOVITA_MODEL_ID` | نام مدلی برای استفاده (مثلاً `moonshotai/kimi-k3`) |

**مدل‌های نمونه**: `moonshotai/kimi-k3`، `zai-org/glm-5.2`، `deepseek/deepseek-v4-flash-0731`. Novita AI همچنین میزبان بسیاری از خانواده‌های مدل‌های منبع‌باز دیگر (Llama، Qwen، GLM و غیره) است — برای فهرست فعلی مدل‌های در دسترس و شناسه مدل‌هایشان به [کتابخانه مدل Novita AI](https://novita.ai/llm-api) مراجعه کنید.

نمونه‌های فعلی به صورت خودکار متغیرهای `NOVITA_*` را مصرف نمی‌کنند. برای استفاده از Novita AI، این مقادیر را به طور صریح هنگام ساختن `OpenAIChatClient` در نمونه‌ای که اجرا می‌کنید، ارسال کنید.

## ارائه‌دهنده جایگزین: Foundry Local (اجرای مدل‌ها روی دستگاه)

[Foundry Local](https://foundrylocal.ai) یک محیط اجرایی سبک است که مدل‌های زبان را **به صورت کامل روی دستگاه خودتان** دانلود، مدیریت و ارائه می‌دهد با استفاده از یک API سازگار با OpenAI — بدون نیاز به فضای ابری.

از آنجا که `OpenAIChatClient` چارچوب Microsoft Agent با هر نقطه انتهایی سازگار با OpenAI کار می‌کند، Foundry Local جایگزینی محلی و دونقطه‌ای برای Azure OpenAI است.

**1. نصب Foundry Local**

```bash
# ویندوز
winget install Microsoft.FoundryLocal

# مک‌او‌اس
brew install foundrylocal
```

**2. دانلود و اجرای یک مدل** (این کار همچنین سرویس محلی را راه‌اندازی می‌کند):

```bash
foundry model list          # مشاهده مدل‌های موجود
foundry model run phi-4-mini
```

**3. نصب SDK پایتون** که برای کشف نقطه انتهایی محلی استفاده می‌شود:

```bash
pip install foundry-local-sdk
```

**4. اشاره دادن چارچوب Microsoft Agent به مدل محلی شما:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# مدل را در صورت نیاز دانلود کرده و به صورت محلی ارائه می‌دهد، سپس نقطه پایانی/پورت را شناسایی می‌کند.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # به عنوان مثال http://localhost:<port>/v1
    api_key=manager.api_key,        # همیشه برای Foundry Local "غيرضروري" است
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **نکته:** Foundry Local یک نقطه انتهایی **Chat Completions** سازگار با OpenAI ارائه می‌دهد. برای توسعه محلی و سناریوهای آفلاین استفاده کنید. برای استفاده کامل از امکانات **Responses API** (گفتگوهای دارای حالت و غیره)، از Azure OpenAI یا پروژه Microsoft Foundry استفاده کنید.

## تنظیمات اضافی برای درس ۸ (فرایند اتصال به بینگ)

نوت‌بوک جریان کاری شرطی در درس ۸ از طریق Microsoft Foundry از **اتصال بینگ** استفاده می‌کند. اگر قصد اجرای آن نمونه را دارید، این متغیر را به فایل `.env` خود اضافه کنید:

| متغیر | محل یافتن |
|----------|-----------------|
| `BING_CONNECTION_ID` | پورتال Microsoft Foundry → پروژه شما → **مدیریت** → **منابع متصل** → اتصال بینگ شما → کپی شناسه اتصال |

## عیب‌یابی

### خطاهای تأیید گواهی SSL روی macOS

اگر روی macOS هستید و با خطایی مانند زیر مواجه می‌شوید:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

این یک مشکل شناخته‌شده در پایتون روی macOS است که گواهی‌های SSL سیستم به‌طور خودکار اعتماد نمی‌شوند. راه‌حل‌های زیر را به ترتیب امتحان کنید:

**گزینه ۱: اجرای اسکریپت نصب گواهی‌های پایتون (توصیه می‌شود)**

```bash
# نسخه پایتون نصب شده‌ی خود را به جای 3.XX وارد کنید (برای مثال، 3.12 یا 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**گزینه ۲: استفاده از `connection_verify=False` در نوت‌بوک خود (فقط برای نوت‌بوک‌های GitHub Models)**

در نوت‌بوک درس ۶ (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) یک راه‌حل موقت کامنت‌شده‌شده از پیش آمده است. وقتی به خطاهای گواهی برخوردید `connection_verify=False` را از حالت کامنت خارج کنید:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # در صورت مواجهه با خطاهای گواهی‌نامه، اعتبارسنجی SSL را غیرفعال کنید
)
```

> **⚠️ هشدار:** غیر فعال کردن تأیید SSL (`connection_verify=False`) امنیت را کاهش می‌دهد چون اعتبارسنجی گواهی را دور می‌زند. این را فقط به عنوان راه‌حل موقتی در محیط‌های توسعه استفاده کنید و هرگز در محیط‌های تولید به کار نگیرید.

**گزینه ۳: نصب و استفاده از `truststore`**

```bash
pip install truststore
```

سپس قبل از هر فراخوانی شبکه‌ای، موارد زیر را در بالای نوت‌بوک یا اسکریپت خود اضافه کنید:

```python
import truststore
truststore.inject_into_ssl()
```

## گیر کرده‌اید؟

اگر در اجرای این تنظیمات با مشکلی روبرو شدید، به <a href="https://discord.gg/kzRShWzttr" target="_blank">دیسکورد انجمن Azure AI</a> بپیوندید یا <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">یک مسئله ایجاد کنید</a>.

## درس بعدی

اکنون آماده‌اید کدهای این دوره را اجرا کنید. یادگیری خوش بگذرد درباره دنیای عوامل هوش مصنوعی!

[مقدمه‌ای بر عوامل هوش مصنوعی و کاربردهای آن‌ها](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->