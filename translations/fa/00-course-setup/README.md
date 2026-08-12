# راه‌اندازی دوره

## مقدمه

این درس نحوه اجرای نمونه کدهای این دوره را پوشش می‌دهد.

## پیوستن به سایر یادگیرندگان و دریافت کمک

قبل از اینکه شروع به کلون کردن مخزن خود کنید، به [کانال Discord عامل‌های هوش مصنوعی برای مبتدیان](https://aka.ms/ai-agents/discord) بپیوندید تا هرگونه کمک در راه‌اندازی، هرگونه سؤال درباره دوره، یا برای ارتباط با سایر یادگیرندگان دریافت کنید.

## کلون یا فورک این مخزن

برای شروع، لطفاً مخزن گیت‌هاب را کلون یا فورک کنید. این کار نسخه خودتان از مطالب دوره را ایجاد می‌کند تا بتوانید کد را اجرا، تست و تنظیم کنید!

این کار را می‌توانید با کلیک روی لینک <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">فورک کردن مخزن</a> انجام دهید

اکنون باید نسخه فورک شده خود از این دوره را در لینک زیر داشته باشید:

![Forked Repo](../../../translated_images/fa/forked-repo.33f27ca1901baa6a.webp)

### کلون سطحی (توصیه‌شده برای کارگاه / Codespaces)

  >کل مخزن ممکن است بزرگ باشد (~3 گیگابایت) وقتی تاریخچه کامل و همه فایل‌ها را دانلود می‌کنید. اگر فقط در کارگاه شرکت می‌کنید یا فقط به چند پوشه درس نیاز دارید، کلون سطحی (یا کلون پراکنده) با کوتاه کردن تاریخچه و/یا رد کردن blobها از بیشتر این دانلود جلوگیری می‌کند.

#### کلون سریع سطحی — تاریخچه حداقلی، همه فایل‌ها

`<your-username>` را در دستورات زیر با آدرس فورک خود (یا آدرس بالادستی اگر ترجیح می‌دهید) جایگزین کنید.

برای کلون کردن فقط تاریخچه آخرین کامیت (دانلود کوچک):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

برای کلون کردن یک شاخه خاص:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### کلون جزئی (پراکنده) — blobهای حداقل + تنها پوشه‌های انتخاب شده

این از کلون جزئی و sparse-checkout استفاده می‌کند (نیاز به Git نسخه 2.25+ و توصیه‌شده گیت مدرن با پشتیبانی کلون جزئی):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

وارد پوشه مخزن شوید:

```bash|powershell
cd ai-agents-for-beginners
```

سپس مشخص کنید که کدام پوشه‌ها را می‌خواهید (نمونه زیر دو پوشه را نشان می‌دهد):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

پس از کلون کردن و تأیید فایل‌ها، اگر فقط به فایل‌ها نیاز دارید و می‌خواهید فضا آزاد کنید (بدون تاریخچه گیت)، لطفاً متادیتای مخزن را حذف کنید (💀 غیرقابل بازگشت — تمام عملکردهای گیت را از دست خواهید داد: بدون کامیت، پول، پوش یا دسترسی به تاریخچه).

```bash
# زش/بش
rm -rf .git
```

```powershell
# پاورشل
Remove-Item -Recurse -Force .git
```

#### استفاده از GitHub Codespaces (توصیه‌شده برای جلوگیری از دانلودهای بزرگ محلی)

- ایجاد یک Codespace جدید برای این مخزن از طریق [رابط کاربری GitHub](https://github.com/codespaces).  

- در ترمینال Codespace تازه ایجاد شده، یکی از دستورات کلون سطحی/پراکنده بالا را اجرا کنید تا فقط پوشه‌های درس مورد نیاز را به فضای کاری Codespace بیاورید.
- اختیاری: پس از کلون در Codespaces، برای بازیابی فضای اضافی .git را حذف کنید (دستورات حذف را در بالا ببینید).
- نکته: اگر ترجیح می‌دهید مخزن را مستقیماً در Codespaces باز کنید (بدون کلون اضافی)، توجه داشته باشید که Codespaces محیط devcontainer را ایجاد می‌کند و ممکن است بیشتر از نیاز شما برپا شود. کلون یک نسخه سطحی در یک Codespace تازه کنترل بیشتری روی استفاده از دیسک به شما می‌دهد.

#### نکات

- همیشه آدرس کلون را با فورک خود جایگزین کنید اگر می‌خواهید ویرایش یا کامیت انجام دهید.
- اگر بعداً به تاریخچه یا فایل‌های بیشتری نیاز داشتید، می‌توانید آن‌ها را دریافت کنید یا sparse-checkout را تنظیم کنید تا پوشه‌های اضافی را شامل شود.

## اجرای کد

این دوره مجموعه‌ای از دفترچه‌های Jupyter ارائه می‌دهد که می‌توانید برای کسب تجربه عملی در ساخت عامل‌های هوش مصنوعی اجرا کنید.

نمونه‌های کد از **Microsoft Agent Framework (MAF)** با `FoundryChatClient` استفاده می‌کنند، که از طریق **Microsoft Foundry** به **Microsoft Foundry Agent Service V2** (رابط API پاسخ‌ها) متصل می‌شود.

همه دفترچه‌های پایتون با نام `*-python-agent-framework.ipynb` برچسب‌گذاری شده‌اند.

## پیش‌نیازها

- Python 3.12+
  - **توجه**: اگر Python 3.12 نصب ندارید، حتماً آن را نصب کنید. سپس محیط مجازی خود را با استفاده از python3.12 بسازید تا نسخه‌های صحیح از فایل requirements.txt نصب شود.
  
    >مثال

    ساخت دایرکتوری محیط مجازی Python:

    ```bash|powershell
    python -m venv venv
    ```

    سپس محیط مجازی را فعال کنید برای:

    ```bash
    # زد شل/باش
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: برای نمونه کدهای استفاده‌شده در .NET، مطمئن شوید [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا بالاتر نصب باشد. سپس نسخه SDK نصب شده‌ی خود را بررسی کنید:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — برای احراز هویت لازم است. از [aka.ms/installazurecli](https://aka.ms/installazurecli) نصب کنید.
- **اشتراک Azure** — برای دسترسی به Microsoft Foundry و Microsoft Foundry Agent Service.
- **پروژه Microsoft Foundry** — پروژه‌ای با مدل استقرار یافته (مثلاً `gpt-5-mini`). مرحله 1 را ببینید.

ما یک فایل `requirements.txt` در ریشه این مخزن قرار داده‌ایم که شامل همه بسته‌های مورد نیاز پایتون برای اجرای نمونه کدهاست.

می‌توانید آن‌ها را با اجرای دستور زیر در ترمینال خود در ریشه مخزن نصب کنید:

```bash|powershell
pip install -r requirements.txt
```

توصیه می‌کنیم یک محیط مجازی پایتون بسازید تا از بروز هرگونه تعارض و مشکل جلوگیری شود.

## تنظیم VSCode

مطمئن شوید در VSCode از نسخه درست پایتون استفاده می‌کنید.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## راه‌اندازی Microsoft Foundry و Microsoft Foundry Agent Service

### مرحله 1: ایجاد پروژه Microsoft Foundry

برای اجرای دفترچه‌ها به یک **هاب** و **پروژه** Microsoft Foundry با مدل مستقر نیاز دارید.

1. به [ai.azure.com](https://ai.azure.com) بروید و با حساب Azure خود وارد شوید.
2. یک **هاب** ایجاد کنید (یا از یکی موجود استفاده کنید). ببینید: [مرور منابع هاب](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. داخل هاب، یک **پروژه** بسازید.
4. یک مدل استقرار دهید (مثلاً `gpt-5-mini`) از بخش **Models + Endpoints** → **Deploy model**.

### مرحله 2: دریافت آدرس نقطه انتهایی پروژه و نام استقرار مدل

از پروژه خود در پرتال Microsoft Foundry:

- **نقطه انتهایی پروژه** — به صفحه **Overview** رفته و URL نقطه انتهایی را کپی کنید.

![Project Connection String](../../../translated_images/fa/project-endpoint.8cf04c9975bbfbf1.webp)

- **نام استقرار مدل** — به قسمت **Models + Endpoints** بروید، مدل مستقر خود را انتخاب کنید و نام **Deployment** را یادداشت کنید (مثلاً `gpt-5-mini`).

### مرحله 3: ورود به Azure با `az login`

همه دفترچه‌ها برای احراز هویت از **`AzureCliCredential`** استفاده می‌کنند — نیازی به مدیریت کلیدهای API نیست. این نیاز دارد که از طریق CLI آژور وارد شوید.

1. **Azure CLI را نصب کنید** اگر هنوز نصب نکرده‌اید: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **وارد شوید** با اجرای:

    ```bash|powershell
    az login
    ```

    یا اگر در محیط ریموت/Codespace بدون مرورگر هستید:

    ```bash|powershell
    az login --use-device-code
    ```

3. **اشتراک خود را انتخاب کنید** اگر خواسته شد — اشتراکی که پروژه Foundry شما را شامل میشود انتخاب کنید.

4. **تأیید کنید** که وارد شده‌اید:

    ```bash|powershell
    az account show
    ```

> **چرا `az login`؟** دفترچه‌ها برای احراز هویت از `AzureCliCredential` در بسته `azure-identity` استفاده می‌کنند. این به این معنی است که نشست Azure CLI شما مجوزها را فراهم می‌کند — نیاز به کلید API یا اسرار در فایل `.env` نیست. این یک [بهترین روش امنیتی](https://learn.microsoft.com/azure/developer/ai/keyless-connections) است.

### مرحله 4: ایجاد فایل `.env`

فایل نمونه را کپی کنید:

```bash
# زِش/باش
cp .env.example .env
```

```powershell
# پاورشل
Copy-Item .env.example .env
```

فایل `.env` را باز کنید و این دو مقدار را پر کنید:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| متغیر | محل یافتن |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | پرتال Foundry → پروژه شما → صفحه **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | پرتال Foundry → **Models + Endpoints** → نام مدل مستقر شما |

این برای بیشتر درس‌ها کافی است! دفترچه‌ها به طور خودکار از طریق نشست `az login` شما احراز هویت می‌کنند.

### مرحله 5: نصب وابستگی‌های پایتون

```bash|powershell
pip install -r requirements.txt
```

توصیه می‌کنیم این کار را داخل محیط مجازی که قبلاً ساختید اجرا کنید.

## راه‌اندازی اضافی برای درس ۵ (Agentic RAG)

درس ۵ از **Azure AI Search** برای تولید با بازیابی پشتیبانی شده استفاده می‌کند. اگر قصد اجرای آن درس را دارید، این متغیرها را به فایل `.env` خود اضافه کنید:

| متغیر | محل یافتن |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | پرتال Azure → منبع **Azure AI Search** شما → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | پرتال Azure → منبع **Azure AI Search** شما → **Settings** → **Keys** → کلید اصلی مدیریت |

## راه‌اندازی اضافی برای درس‌هایی که مستقیماً Azure OpenAI را فرا می‌خوانند (درس ۶ و ۸)

برخی دفترچه‌ها در درس‌های ۶ و ۸ مستقیماً از **Azure OpenAI** استفاده می‌کنند (با استفاده از **Responses API**) به جای رفتن از طریق پروژه Microsoft Foundry. این نمونه‌ها قبلاً از مدل‌های GitHub استفاده می‌کردند که منسوخ شده‌اند (تا جولای ۲۰۲۶ بازنشسته می‌شود) و از Responses API پشتیبانی نمی‌کنند. اگر قصد اجرای آن‌ها را دارید، این متغیرها را به فایل `.env` خود اضافه کنید:

| متغیر | محل یافتن |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | پرتال Azure → منبع **Azure OpenAI** شما → **Keys and Endpoint** → نقطه انتهایی (مثلاً `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | نام مدل مستقر شما (مثلاً `gpt-5-mini`) که از Responses API پشتیبانی می‌کند |
| `AZURE_OPENAI_API_KEY` | اختیاری — فقط اگر از احراز هویت مبتنی بر کلید به جای `az login` / Entra ID استفاده می‌کنید |

> Responses API از نقطه پایانی پایدار `/openai/v1/` استفاده می‌کند، بنابراین نیازی به `api-version` نیست. برای استفاده از احراز هویت بدون کلید Entra ID با `az login` وارد شوید.

## ارائه‌دهنده جایگزین: MiniMax (سازگار با OpenAI)

[MiniMax](https://platform.minimaxi.com/) مدل‌های دارای بافت بزرگ (تا ۲۰۴ هزار توکن) را از طریق API سازگار با OpenAI ارائه می‌دهد. از آنجا که `OpenAIChatClient` در Microsoft Agent Framework با هر نقطه پایانی سازگار با OpenAI کار می‌کند، می‌توانید MiniMax را به عنوان جایگزینی برای Azure OpenAI یا OpenAI استفاده کنید.

این متغیرها را به فایل `.env` خود اضافه کنید:

| متغیر | محل یافتن |
|----------|-----------------|
| `MINIMAX_API_KEY` | [پلتفرم MiniMax](https://platform.minimaxi.com/) → کلیدهای API |
| `MINIMAX_BASE_URL` | استفاده کنید از `https://api.minimax.io/v1` (مقدار پیش‌فرض) |
| `MINIMAX_MODEL_ID` | نام مدل برای استفاده (مثلاً `MiniMax-M3`) |

**نمونه مدل‌ها**: `MiniMax-M3` (توصیه‌شده)، `MiniMax-M2.7`، `MiniMax-M2.7-highspeed` (پاسخ‌های سریع‌تر). نام مدل‌ها و دسترسی ممکن است در طول زمان تغییر کند و دسترسی به مدل خاص ممکن است به حساب یا منطقه شما بستگی داشته باشد — فهرست فعلی را در [پلتفرم MiniMax](https://platform.minimaxi.com/) بررسی کنید. اگر `MiniMax-M3` برای حساب شما در دسترس نیست، `MINIMAX_MODEL_ID` را به مدلی که به آن دسترسی دارید تنظیم کنید (مثلاً `MiniMax-M2.7`).

نمونه کدهایی که از `OpenAIChatClient` استفاده می‌کنند (مثلاً جریان کاری رزرو هتل درس ۱۴) به طور خودکار پیکربندی MiniMax شما را وقتی `MINIMAX_API_KEY` تنظیم شده باشد، تشخیص داده و استفاده می‌کنند.

## ارائه‌دهنده جایگزین: Foundry Local (اجرای مدل‌ها روی دستگاه)

[Foundry Local](https://foundrylocal.ai) یک محیط اجرای سبک است که مدل‌های زبانی را **کاملاً روی دستگاه خودتان** از طریق API سازگار با OpenAI دانلود، مدیریت و ارائه می‌دهد — هیچ ابر، هیچ اشتراک Azure و هیچ کلید API لازم نیست. این گزینه عالی برای توسعه آفلاین، آزمایش بدون هزینه‌های ابری یا نگهداری داده‌ها روی دستگاه است.

از آنجا که `OpenAIChatClient` در Microsoft Agent Framework با هر نقطه پایانی سازگار با OpenAI کار می‌کند، Foundry Local یک جایگزین محلی برای Azure OpenAI است.

**۱. نصب Foundry Local**

```bash
# ویندوز
winget install Microsoft.FoundryLocal

# مک‌اواس
brew install foundrylocal
```

**۲. دانلود و اجرای یک مدل** (این همچنین سرویس محلی را راه‌اندازی می‌کند):

```bash
foundry model list          # مشاهده مدل‌های موجود
foundry model run phi-4-mini
```

**۳. نصب SDK پایتون** برای کشف نقطه انتهایی محلی:

```bash
pip install foundry-local-sdk
```

**۴. اشاره دادن Microsoft Agent Framework به مدل محلی خود:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# مدل را به‌صورت محلی دانلود می‌کند (در صورت نیاز) و سرو می‌کند، سپس نقطه پایانی/پورت را کشف می‌کند.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # برای مثال http://localhost:<port>/v1
    api_key=manager.api_key,        # همیشه برای Foundry Local "نیاز نیست" است
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **توجه:** Foundry Local یک نقطه پایانی سازگار با OpenAI برای **Chat Completions** فراهم می‌کند. از آن برای توسعه محلی و سناریوهای آفلاین استفاده کنید. برای مجموعه کامل ویژگی‌های **Responses API** (گفتگوهای حالت‌دار، سازماندهی عمیق ابزارها و توسعه سبک عامل)، به **Azure OpenAI** یا پروژه **Microsoft Foundry** مراجعه کنید همانطور که در درس‌ها نمایش داده شده است. مستندات [Foundry Local](https://foundrylocal.ai) را برای فهرست مدل‌های فعلی و پشتیبانی پلتفرم ببینید.

## راه‌اندازی اضافی برای درس ۸ (جریان کاری پایه‌گذاری Bing)


دفترچه کاری شرطی در درس ۸ از **بنیان‌بخشی بینگ** از طریق Microsoft Foundry استفاده می‌کند. اگر قصد دارید آن نمونه را اجرا کنید، این متغیر را به فایل `.env` خود اضافه کنید:

| متغیر | محل یافتن |
|----------|-----------------|
| `BING_CONNECTION_ID` | پرتال Microsoft Foundry → پروژه شما → **مدیریت** → **منابع متصل** → اتصال بینگ شما → کپی شناسه اتصال |

## رفع اشکال

### خطاهای تأیید گواهی SSL در macOS

اگر در macOS با خطایی مانند روبه‌رو شدید:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

این یک مشکل شناخته‌شده در پایتون در macOS است که گواهی‌های SSL سیستم به‌طور خودکار مورد اعتماد قرار نمی‌گیرند. راه‌حل‌های زیر را به ترتیب امتحان کنید:

**گزینه ۱: اجرای اسکریپت نصب گواهی‌نامه‌های پایتون (توصیه‌شده)**

```bash
# نسخه‌ی پایتون نصب شده خود را جایگزین 3.XX کنید (مثلاً 3.12 یا 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**گزینه ۲: استفاده از `connection_verify=False` در دفترچه یادداشت خود (فقط برای دفترهای GitHub Models)**

در دفترچه یادداشت درس ۶ (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)، یک راه‌حل کامنت شده قبلاً درج شده است. هنگام ایجاد کلاینت، `connection_verify=False` را از حالت کامنت خارج کنید:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # در صورت مواجهه با خطاهای گواهی، تأیید SSL را غیرفعال کنید
)
```

> **⚠️ هشدار:** غیرفعال کردن تأیید SSL (`connection_verify=False`) با رد شدن از اعتبارسنجی گواهی‌نامه، امنیت را کاهش می‌دهد. این کار را فقط به عنوان یک راه‌حل موقت در محیط‌های توسعه استفاده کنید و هرگز در تولید.

**گزینه ۳: نصب و استفاده از `truststore`**

```bash
pip install truststore
```

سپس موارد زیر را در بالای دفترچه یا اسکریپت خود قبل از هر فراخوانی شبکه‌ای اضافه کنید:

```python
import truststore
truststore.inject_into_ssl()
```

## گیر کرده‌اید؟

اگر در اجرای این تنظیمات با مشکلی مواجه شدید، به <a href="https://discord.gg/kzRShWzttr" target="_blank">دیـسکورد جامعه هوش مصنوعی آزور</a> بپیوندید یا <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">یک مشکل گزارش کنید</a>.

## درس بعدی

اکنون آماده‌اید کد این دوره را اجرا کنید. از یادگیری بیشتر درباره دنیای عوامل هوش مصنوعی لذت ببرید!

[مقدمه‌ای بر عوامل هوش مصنوعی و موارد استفاده آنها](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->