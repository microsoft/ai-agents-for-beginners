# AGENTS.md

## نمای کلی پروژه

این مخزن شامل "عامل‌های هوش مصنوعی برای مبتدیان" است - یک دوره آموزشی جامع که همه چیز لازم برای ساخت عامل‌های هوش مصنوعی را آموزش می‌دهد. این دوره شامل ۱۸ درس (شماره‌گذاری شده ۰۰-۱۸) است که مبانی، الگوهای طراحی، فریمورک‌ها، استقرار در تولید، عامل‌های محلی/روی دستگاه و امنیت عامل‌های هوش مصنوعی را پوشش می‌دهد.

**فناوری‌های کلیدی:**
- پایتون ۳.۱۲ و بالاتر
- دفترچه‌های Jupyter برای یادگیری تعاملی
- فریمورک‌های هوش مصنوعی: Microsoft Agent Framework (MAF)
- خدمات هوش مصنوعی Azure: Microsoft Foundry، سرویس Agent Microsoft Foundry V2

**معماری:**
- ساختار مبتنی بر درس (دایرکتوری‌های ۰۰-۱۸)
- هر درس شامل: مستندات README، نمونه‌های کد (دفترچه‌های Jupyter) و تصاویر
- پشتیبانی چندزبانه از طریق سیستم ترجمه خودکار
- یک دفترچه پایتون برای هر درس با استفاده از Microsoft Agent Framework

## دستورات نصب

### پیش‌نیازها
- پایتون ۳.۱۲ یا بالاتر
- اشتراک Azure (برای Microsoft Foundry)
- نصب و احراز هویت Azure CLI (`az login`)

### راه‌اندازی اولیه

۱. **مخزن را کلون یا فورک کنید:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

۲. **ایجاد و فعال کردن محیط مجازی پایتون:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

۳. **نصب وابستگی‌ها:**
   ```bash
   pip install -r requirements.txt
   ```

۴. **تنظیم متغیرهای محیطی:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### متغیرهای محیطی موردنیاز

برای **Microsoft Foundry** (الزامی):
- `AZURE_AI_PROJECT_ENDPOINT` - نقطه انتهایی پروژه Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - نام استقرار مدل (مثلاً gpt-5-mini)

برای **Azure AI Search** (درس ۰۵ - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - نقطه انتهایی جستجوی Azure AI
- `AZURE_SEARCH_API_KEY` - کلید API جستجوی Azure AI

احراز هویت: قبل از اجرای دفترچه‌ها `az login` را اجرا کنید (از `AzureCliCredential` استفاده می‌کند).

## جریان کاری توسعه

### اجرای دفترچه‌های Jupyter

هر درس شامل چندین دفترچه Jupyter برای فریمورک‌های مختلف است:

۱. **شروع Jupyter:**
   ```bash
   jupyter notebook
   ```

۲. **رفتن به دایرکتوری درس** (مثلاً `01-intro-to-ai-agents/code_samples/`)

۳. **باز کردن و اجرای دفترچه‌ها:**
   - `*-python-agent-framework.ipynb` - با استفاده از Microsoft Agent Framework (پایتون)
   - `*-dotnet-agent-framework.ipynb` - با استفاده از Microsoft Agent Framework (.NET)

### کار با Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- نیازمند اشتراک Azure
- استفاده از `FoundryChatClient` برای Agent Service V2 (عامل‌ها در پورتال Foundry قابل مشاهده‌اند)
- آماده تولید با قابلیت رصد داخلی
- الگوی فایل: `*-python-agent-framework.ipynb`

## دستورالعمل‌های تست

این یک مخزن آموزشی با کد نمونه است نه کد تولیدی با تست‌های خودکار. برای تایید راه‌اندازی و تغییرات خود:

### تست دستی

۱. **تست محیط پایتون:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

۲. **تست اجرای دفترچه:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

۳. **بررسی متغیرهای محیطی:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### اجرای دفترچه‌های جداگانه

دفترچه‌ها را در Jupyter باز کرده و سلول‌ها را به ترتیب اجرا کنید. هر دفترچه مستقل است و شامل:
- دستورات ایمپورت
- بارگذاری پیکربندی
- پیاده‌سازی نمونه عامل‌ها
- خروجی‌های مورد انتظار در سلول‌های markdown

### تست سریع عامل‌های مستقر شده

برای درس‌هایی که عامل به عنوان عامل میزبانی‌شده Microsoft Foundry مستقر شده است (۰۱، ۰۴، ۰۵، ۱۶)، مخزن کاتالوگ‌های آزمون سریع را تحت `tests/` ارائه می‌کند که توسط جریان کاری `.github/workflows/smoke-test.yml` از طریق اکشن [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) اجرا می‌شوند. این‌ها یک دروازه سبک پس از استقرار هستند (آیا عامل در دسترس است و دستورالعمل‌های پایه را دنبال می‌کند؟) که مکمل خط لوله ارزیابی در درس‌های ۱۰ و ۱۶ است. برای نقشه‌برداری کاتالوگ به درس به عامل، به [tests/README.md](./tests/README.md) مراجعه کنید. درس ۱۷ محلی با Foundry Local اجرا می‌شود و نقطه انتهایی میزبانی‌شده ندارد، بنابراین با اجرای مستقیم دفترچه خود تایید می‌شود.

## سبک کدنویسی

### قراردادهای پایتون

- **نسخه پایتون**: ۳.۱۲ و بالاتر
- **سبک کد**: پیروی از قراردادهای استاندارد Python PEP 8
- **دفترچه‌ها**: استفاده از سلول‌های markdown واضح برای توضیح مفاهیم
- **ایمپورت‌ها**: گروه‌بندی بر اساس کتابخانه استاندارد، شخص ثالث، محلی

### قراردادهای دفترچه Jupyter

- استفاده از سلول‌های markdown توصیفی قبل از سلول‌های کد
- افزودن مثال‌های خروجی در دفترچه‌ها برای مرجع
- استفاده از نام‌های متغیر واضح که با مفاهیم درس مطابقت دارند
- حفظ ترتیب اجرای خطی دفترچه (سلول ۱ → ۲ → ۳…)

### سازماندهی فایل‌ها

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## ساخت و استقرار

### ساخت مستندات

این مخزن از Markdown برای مستندسازی استفاده می‌کند:
- فایل‌های README.md در هر پوشه درس
- README.md اصلی در ریشه مخزن
- سیستم ترجمه خودکار از طریق GitHub Actions

### خط لوله CI/CD

در `.github/workflows/` واقع شده است:

۱. **co-op-translator.yml** - ترجمه خودکار به بیش از ۵۰ زبان
۲. **welcome-issue.yml** - خوش‌آمدگویی به سازندگان مسائل جدید
۳. **welcome-pr.yml** - خوش‌آمدگویی به مشارکت‌کنندگان درخواست کشش جدید

### استقرار

این یک مخزن آموزشی است - فرایند استقرار ندارد. کاربران:
۱. مخزن را فورک یا کلون کنند
۲. دفترچه‌ها را به صورت محلی یا در GitHub Codespaces اجرا کنند
۳. از طریق تغییر و آزمایش نمونه‌ها یاد بگیرند

## دستورالعمل‌های درخواست کشش

### قبل از ارسال

۱. **تغییرات خود را تست کنید:**
   - اجرای کامل دفترچه‌های متاثر
   - اطمینان از اجرای بدون خطا تمام سلول‌ها
   - بررسی مناسب بودن خروجی‌ها

۲. **به‌روزرسانی مستندات:**
   - به‌روزرسانی README.md اگر مفاهیم جدید اضافه شود
   - افزودن کامنت در دفترچه‌ها برای کد پیچیده
   - اطمینان از توضیح هدف در سلول‌های markdown

۳. **تغییرات فایل‌ها:**
   - اجتناب از کامیت فایل‌های `.env` (استفاده از `.env.example`)
   - کامیت نکردن دایرکتوری‌های `venv/` یا `__pycache__/`
   - حفظ خروجی دفترچه‌ها وقتی مفاهیم را نشان می‌دهند
   - حذف فایل‌های موقت و نسخه‌های پشتیبان دفترچه (`*-backup.ipynb`)

### فرمت عنوان PR

استفاده از عناوین توصیفی:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### بررسی‌های مورد نیاز

- دفترچه‌ها باید بدون خطا اجرا شوند
- فایل‌های README باید واضح و دقیق باشند
- پیروی از الگوهای کد موجود در مخزن
- حفظ هماهنگی با سایر دروس

## یادداشت‌های اضافی

### نکات متداول

۱. **ناسازگاری نسخه پایتون:**
   - اطمینان از استفاده پایتون ۳.۱۲ و بالاتر
   - برخی پکیج‌ها ممکن است با نسخه‌های قدیمی کار نکنند
   - استفاده از `python3 -m venv` برای تعیین صریح نسخه پایتون

۲. **متغیرهای محیطی:**
   - همیشه ایجاد `.env` از `.env.example`
   - کامیت نکردن فایل `.env` (در `.gitignore` است)
   - ورود با `az login` برای احراز هویت بدون کلید Entra ID

۳. **تداخل‌های پکیج:**
   - استفاده از محیط مجازی تازه
   - نصب از `requirements.txt` به جای پکیج‌های جداگانه
   - برخی دفترچه‌ها ممکن است به پکیج‌های اضافی که در سلول‌های markdownشان ذکر شده نیاز داشته باشند

۴. **خدمات Azure:**
   - خدمات هوش مصنوعی Azure نیازمند اشتراک فعال است
   - برخی ویژگی‌ها منطقه‌ای هستند
   - اطمینان از اینکه استقرار مدل Azure OpenAI شما از API پاسخ‌ها پشتیبانی می‌کند

### مسیر یادگیری

پیشرفت پیشنهادی از طریق دروس:
۱. **۰۰-course-setup** - شروع برای راه‌اندازی محیط
۲. **۰۱-intro-to-ai-agents** - درک مبانی عامل‌های هوش مصنوعی
۳. **۰۲-explore-agentic-frameworks** - آشنایی با فریمورک‌های مختلف
۴. **۰۳-agentic-design-patterns** - الگوهای طراحی اصلی
۵. ادامه دروس شماره‌گذاری شده به ترتیب

### انتخاب فریمورک

فریمورک را بر اساس اهداف خود انتخاب کنید:
- **تمام دروس**: Microsoft Agent Framework (MAF) با `FoundryChatClient`
- **عامل‌ها سمت سرور ثبت می‌شوند** در Microsoft Foundry Agent Service V2 و در پورتال Foundry قابل مشاهده‌اند

### دریافت کمک

- به [جامعه Discord Microsoft Foundry](https://aka.ms/ai-agents/discord) بپیوندید
- فایل‌های README دروس را برای راهنمایی‌های خاص بررسی کنید
- فایل اصلی [README.md](./README.md) را برای نمای کلی دوره بررسی کنید
- به [Course Setup](./00-course-setup/README.md) برای دستورالعمل‌های دقیق راه‌اندازی مراجعه کنید

### مشارکت

این یک پروژه آموزشی باز است. مشارکت‌ها خوش‌آمد گفته می‌شوند:
- بهبود نمونه کدها
- رفع اشتباهات تایپی یا خطاها
- افزودن کامنت‌های روشن‌کننده
- پیشنهاد موضوعات جدید برای درس‌ها
- ترجمه به زبان‌های دیگر

برای نیازهای کنونی به [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) مراجعه کنید.

## زمینه خاص پروژه

### پشتیبانی چندزبانه

این مخزن از یک سیستم ترجمه خودکار استفاده می‌کند:
- پشتیبانی از بیش از ۵۰ زبان
- ترجمه‌ها در دایرکتوری‌های `/translations/<lang-code>/`
- جریان کاری GitHub Actions مسئول به‌روزرسانی ترجمه‌ها
- فایل‌های منبع به زبان انگلیسی در ریشه مخزن هستند

### ساختار درس

هر درس از الگوی ثابتی پیروی می‌کند:
۱. تصویر بندانگشتی ویدئو با لینک
۲. محتوای نوشتاری درس (README.md)
۳. نمونه‌های کد در فریمورک‌های مختلف
۴. اهداف یادگیری و پیش‌نیازها
۵. منابع یادگیری اضافی لینک‌شده

### نام‌گذاری نمونه‌های کد

قالب: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - درس ۱، MAF پایتون
- `14-sequential.ipynb` - درس ۱۴، الگوهای پیشرفته MAF
- `16-python-agent-framework.ipynb` - درس ۱۶، عامل پشتیبانی مشتری تولیدی
- `17-local-agent-foundry-local.ipynb` - درس ۱۷، عامل محلی با Foundry Local + Qwen

### دایرکتوری‌های خاص

- `translated_images/` - تصاویر محلی‌شده برای ترجمه‌ها
- `images/` - تصاویر اصلی برای محتوای انگلیسی
- `.devcontainer/` - پیکربندی کانتینر توسعه VS Code
- `.github/` - جریان کاری و قالب‌های GitHub Actions

### وابستگی‌ها

بسته‌های کلیدی از `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - پشتیبانی پروتکل Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - خدمات هوش مصنوعی Azure
- `azure-identity` - احراز هویت Azure (AzureCliCredential)
- `azure-search-documents` - ادغام جستجوی Azure AI
- `mcp[cli]` - پشتیبانی پروتکل Model Context

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->