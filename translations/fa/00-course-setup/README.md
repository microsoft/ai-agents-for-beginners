# تنظیم دوره

## معرفی

این درس نحوه اجرای نمونه‌های کد این دوره را پوشش خواهد داد.

## پیوستن به سایر یادگیرندگان و دریافت کمک

قبل از اینکه مخزن خود را کلون کنید، به [کانال Discord مربوط به AI Agents For Beginners](https://aka.ms/ai-agents/discord) بپیوندید تا در صورت نیاز به کمک در راه‌اندازی، پرسش در مورد دوره، یا ارتباط با سایر یادگیرندگان، کمک دریافت کنید.

## کلون یا فورک کردن این مخزن

برای شروع، لطفاً مخزن GitHub را کلون یا فورک کنید. این کار نسخهٔ خودتان از مطالب دوره را ایجاد می‌کند تا بتوانید کد را اجرا، آزمایش و تغییر دهید!

این کار را می‌توانید با کلیک روی لینک <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a> انجام دهید

شما اکنون باید نسخهٔ فورک‌شدهٔ این دوره را در لینک زیر داشته باشید:

![مخزن فورک‌شده](../../../translated_images/fa/forked-repo.33f27ca1901baa6a.webp)

### کلون سطحی (توصیه‌شده برای کارگاه / Codespaces)

  >مخزن کامل می‌تواند بزرگ باشد (~3 GB) زمانی که تاریخچهٔ کامل و همهٔ فایل‌ها را دانلود می‌کنید. اگر فقط در کارگاه شرکت می‌کنید یا فقط به چند پوشهٔ درس نیاز دارید، یک کلون سطحی (یا کلون پراکنده) بیشتر آن دانلود را با کوتاه‌سازی تاریخچه و/یا جا‌انداختن blobها اجتناب می‌کند.

#### کلون سطحی سریع — تاریخچهٔ حداقلی، همهٔ فایل‌ها

مقدار `<your-username>` در دستورات زیر را با URL فورک خود (یا URL upstream در صورت ترجیح) جایگزین کنید.

برای کلون کردن فقط تاریخچهٔ آخرین کامیت (دانلود کوچک):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

برای کلون یک شاخهٔ خاص:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### کلون جزئی (پراکنده) — blobهای حداقلی + فقط پوشه‌های انتخاب‌شده

این روش از کلون جزئی و sparse-checkout استفاده می‌کند (نیاز به Git 2.25+ و توصیه می‌شود از Git مدرن با پشتیبانی از کلون جزئی استفاده کنید):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

وارد پوشهٔ مخزن شوید:

```bash|powershell
cd ai-agents-for-beginners
```

سپس مشخص کنید کدام پوشه‌ها را می‌خواهید (نمونهٔ زیر دو پوشه را نشان می‌دهد):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

بعد از کلون و بررسی فایل‌ها، اگر فقط به فایل‌ها نیاز دارید و می‌خواهید فضا آزاد کنید (بدون تاریخچهٔ git)، لطفاً متادیتای مخزن را حذف کنید (💀غیرقابل بازگشت — تمام عملکردهای Git را از دست خواهید داد: هیچ commit، pull، push یا دسترسی به تاریخچه).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# پاورشل
Remove-Item -Recurse -Force .git
```

#### استفاده از GitHub Codespaces (توصیه‌شده برای جلوگیری از دانلودهای بزرگ محلی)

- یک Codespace جدید برای این مخزن از طریق [GitHub UI](https://github.com/codespaces) ایجاد کنید.  

- در ترمینال Codespace تازه ایجادشده، یکی از دستورات کلون سطحی/پراکندهٔ بالا را اجرا کنید تا فقط پوشه‌های درسی که نیاز دارید وارد فضای کاری Codespace شوند.
- اختیاری: پس از کلون در داخل Codespaces، برای بازپس‌گیری فضای اضافی، .git را حذف کنید (دستورات حذف را در بالا ببینید).
- توجه: اگر ترجیح می‌دهید مخزن را مستقیماً در Codespaces باز کنید (بدون کلون اضافی)، توجه داشته باشید که Codespaces محیط devcontainer را می‌سازد و ممکن است هنوز بیش از نیاز شما منابع فراهم کند. کلون یک نسخهٔ سطحی داخل یک Codespace تازه به شما کنترل بیشتری روی استفاده دیسک می‌دهد.

#### نکات

- همیشه URL کلون را با فورک خود جایگزین کنید اگر می‌خواهید ویرایش/commit انجام دهید.
- اگر بعداً به تاریخچه یا فایل‌های بیشتری نیاز داشتید، می‌توانید آن‌ها را fetch کنید یا sparse-checkout را تنظیم کنید تا پوشه‌های اضافی را شامل شود.

## اجرای کد

این دوره مجموعه‌ای از نوت‌بوک‌های Jupyter را ارائه می‌دهد که می‌توانید برای کسب تجربهٔ عملی در ساخت AI Agents اجرا کنید.

نمونه‌های کد از **Microsoft Agent Framework (MAF)** با `AzureAIProjectAgentProvider` استفاده می‌کنند، که از طریق **Microsoft Foundry** به **Azure AI Agent Service V2** (Responses API) متصل می‌شود.

تمام نوت‌بوک‌های پایتون با برچسب `*-python-agent-framework.ipynb` علامت‌گذاری شده‌اند.

## پیش‌نیازها

- Python 3.12+
  - **توجه**: اگر Python3.12 را نصب ندارید، آن را نصب کنید. سپس venv خود را با استفاده از python3.12 ایجاد کنید تا نسخه‌های صحیح از فایل requirements.txt نصب شوند.
  
    >مثال

    ایجاد دایرکتوری venv پایتون:

    ```bash|powershell
    python -m venv venv
    ```

    سپس محیط venv را برای فعال کنید:

    ```bash
    # زد‌اِش/باش
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: برای نمونه‌های کد که از .NET استفاده می‌کنند، مطمئن شوید [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا نسخهٔ جدیدتر را نصب کرده‌اید. سپس نسخهٔ SDK نصب‌شدهٔ .NET خود را بررسی کنید:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — برای احراز هویت لازم است. از [aka.ms/installazurecli](https://aka.ms/installazurecli) نصب کنید.
- **اشتراک Azure** — برای دسترسی به Microsoft Foundry و Azure AI Agent Service.
- **پروژهٔ Microsoft Foundry** — یک پروژه با مدل مستقر شده (مثلاً `gpt-4o`). ببینید [مرحلهٔ 1](../../../00-course-setup) در زیر.

ما یک فایل `requirements.txt` را در ریشهٔ این مخزن گنجانده‌ایم که شامل همهٔ بسته‌های پایتون مورد نیاز برای اجرای نمونه‌های کد است.

می‌توانید آن‌ها را با اجرای دستور زیر در ترمینال خود در ریشهٔ مخزن نصب کنید:

```bash|powershell
pip install -r requirements.txt
```

توصیه می‌کنیم برای جلوگیری از هرگونه تداخل و مشکلات، یک محیط مجازی پایتون ایجاد کنید.

## تنظیم VSCode

اطمینان حاصل کنید که در VSCode از نسخهٔ صحیح پایتون استفاده می‌کنید.

![تصویر](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## راه‌اندازی Microsoft Foundry و Azure AI Agent Service

### مرحلهٔ 1: ایجاد یک پروژهٔ Microsoft Foundry

شما به یک **hub** و یک **project** در Azure AI Foundry با یک مدل مستقر نیاز دارید تا نوت‌بوک‌ها را اجرا کنید.

1. به [ai.azure.com](https://ai.azure.com) بروید و با حساب Azure خود وارد شوید.
2. یک **hub** ایجاد کنید (یا از یک hub موجود استفاده کنید). ببینید: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. درون hub، یک **project** ایجاد کنید.
4. یک مدل مستقر کنید (مثلاً `gpt-4o`) از **Models + Endpoints** → **Deploy model**.

### مرحلهٔ 2: بازیابی Endpoint پروژه و نام استقرار مدل

از پروژهٔ خود در پرتال Microsoft Foundry:

- **Project Endpoint** — به صفحهٔ **Overview** بروید و URL endpoint را کپی کنید.

![رشتهٔ اتصال پروژه](../../../translated_images/fa/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — به **Models + Endpoints** بروید، مدل مستقرشدهٔ خود را انتخاب کنید و **Deployment name** را یادداشت کنید (مثلاً `gpt-4o`).

### مرحلهٔ 3: ورود به Azure با `az login`

تمام نوت‌بوک‌ها برای احراز هویت از **`AzureCliCredential`** استفاده می‌کنند — نیازی به مدیریت کلیدهای API نیست. این مستلزم این است که از طریق Azure CLI وارد شده باشید.

1. **Azure CLI را نصب کنید** اگر قبلاً نصب نکرده‌اید: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **وارد شوید** با اجرای دستور:

    ```bash|powershell
    az login
    ```

    یا اگر در یک محیط راه دور/Codespace بدون مرورگر هستید:

    ```bash|powershell
    az login --use-device-code
    ```

3. **اشتراک خود را انتخاب کنید** در صورت درخواست — همان اشتراکی را انتخاب کنید که پروژهٔ Foundry شما در آن قرار دارد.

4. **تأیید کنید** که وارد شده‌اید:

    ```bash|powershell
    az account show
    ```

> **چرا از `az login` استفاده می‌کنیم؟** نوت‌بوک‌ها از `AzureCliCredential` در بستهٔ `azure-identity` برای احراز هویت استفاده می‌کنند. این بدان معناست که نشست Azure CLI شما مدارک لازم را فراهم می‌کند — هیچ کلید API یا راز در فایل `.env` شما ذخیره نمی‌شود. این یک [روش امن برای اتصال بدون کلید](https://learn.microsoft.com/azure/developer/ai/keyless-connections) است.

### مرحلهٔ 4: ایجاد فایل `.env` خود

فایل نمونه را کپی کنید:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# پاورشل
Copy-Item .env.example .env
```

فایل `.env` را باز کنید و این دو مقدار را پر کنید:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

همین برای بیشتر درس‌ها کافی است! نوت‌بوک‌ها به‌طور خودکار از طریق نشست `az login` شما احراز هویت می‌کنند.

### مرحلهٔ 5: نصب وابستگی‌های پایتون

```bash|powershell
pip install -r requirements.txt
```

توصیه می‌کنیم این را داخل محیط مجازی که قبلاً ایجاد کردید اجرا کنید.

## تنظیمات اضافی برای درس 5 (Agentic RAG)

درس 5 از **Azure AI Search** برای تولید تکمیلی بازیابی‌شده استفاده می‌کند. اگر قصد اجرای آن درس را دارید، این متغیرها را به فایل `.env` خود اضافه کنید:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## تنظیمات اضافی برای درس 6 و درس 8 (GitHub Models)

برخی نوت‌بوک‌ها در درس‌های 6 و 8 از **GitHub Models** به‌جای Azure AI Foundry استفاده می‌کنند. اگر قصد اجرای آن نمونه‌ها را دارید، این متغیرها را به فایل `.env` خود اضافه کنید:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## تنظیمات اضافی برای درس 8 (Bing Grounding Workflow)

نوت‌بوک جریان کاری شرطی در درس 8 از **Bing grounding** از طریق Azure AI Foundry استفاده می‌کند. اگر قصد اجرای آن نمونه را دارید، این متغیر را به فایل `.env` خود اضافه کنید:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## رفع اشکال

### خطاهای تأیید گواهی SSL در macOS

اگر در macOS با خطایی مانند زیر مواجه شدید:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

این یک مشکل شناخته‌شده با پایتون روی macOS است که در آن گواهی‌های SSL سیستم به‌طور خودکار مورد اعتماد قرار نمی‌گیرند. راه‌حل‌های زیر را به ترتیب امتحان کنید:

**گزینهٔ 1: اجرای اسکریپت Install Certificates پایتون (توصیه‌شده)**

```bash
# 3.XX را با نسخه پایتون نصب‌شدهٔ خود جایگزین کنید (مثلاً 3.12 یا 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**گزینهٔ 2: استفاده از `connection_verify=False` در نوت‌بوک شما (فقط برای نوت‌بوک‌های GitHub Models)**

در نوت‌بوک درس 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)، یک راه‌حل موقت به‌صورت کامنت‌شده قبلاً قرار داده شده است. هنگام ایجاد کلاینت، `connection_verify=False` را از کامنت خارج کنید:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # در صورت مواجهه با خطاهای گواهی‌نامه، اعتبارسنجی SSL را غیرفعال کنید
)
```

> **⚠️ هشدار:** غیرفعال کردن تأیید SSL (`connection_verify=False`) با رد اعتبارسنجی گواهی‌ها امنیت را کاهش می‌دهد. از این فقط به‌عنوان راه‌حل موقت در محیط‌های توسعه استفاده کنید، هرگز در تولید.

**گزینهٔ 3: نصب و استفاده از `truststore`**

```bash
pip install truststore
```

سپس موارد زیر را در بالای نوت‌بوک یا اسکریپت خود قبل از انجام هر تماس شبکه‌ای اضافه کنید:

```python
import truststore
truststore.inject_into_ssl()
```

## در جایی گیر کرده‌اید؟

اگر در اجرای این تنظیمات با هر مشکلی مواجه شدید، وارد <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> شوید یا <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">یک issue ایجاد کنید</a>.

## درس بعدی

شما اکنون آماده اجرای کد این دوره هستید. از یادگیری بیشتر دربارهٔ دنیای AI Agents لذت ببرید!

[مقدمه‌ای بر AI Agents و موارد استفاده از عامل‌ها](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
سلب‌مسئولیت:
این سند با استفاده از سرویس ترجمه ماشینی Co-op Translator (https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است دارای خطا یا نادرستی باشند. سند اصلی به زبان مبدأ خود باید به‌عنوان مرجع معتبر در نظر گرفته شود. برای اطلاعات حساس یا حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->