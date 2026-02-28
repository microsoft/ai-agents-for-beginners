# AGENTS.md

## مروری بر پروژه

این مخزن شامل «عامل‌های هوش مصنوعی برای مبتدیان» است – یک دوره آموزشی جامع که همه چیزهای لازم برای ساخت عامل‌های هوش مصنوعی را آموزش می‌دهد. این دوره شامل بیش از ۱۵ درس است که اصول پایه، الگوهای طراحی، چارچوب‌ها و استقرار در محیط تولید عامل‌های هوش مصنوعی را پوشش می‌دهد.

**فناوری‌های کلیدی:**
- پایتون ۳.۱۲ به بالا
- Jupyter Notebooks برای یادگیری تعاملی
- چارچوب‌های هوش مصنوعی: Microsoft Agent Framework (MAF)
- خدمات هوش مصنوعی Azure: Microsoft Foundry، Azure AI Foundry Agent Service V2

**معماری:**
- ساختار مبتنی بر درس (دایرکتوری‌های ۰۰-۱۵+)
- هر درس شامل: مستندات README، نمونه‌کدها (دفترچه‌های Jupyter)، و تصاویر
- پشتیبانی چند زبانه از طریق سیستم ترجمه خودکار
- یک دفترچه پایتون برای هر درس با استفاده از Microsoft Agent Framework

## فرمان‌های راه‌اندازی

### پیش‌نیازها
- پایتون ۳.۱۲ یا بالاتر
- اشتراک Azure (برای Azure AI Foundry)
- نصب و ورود به Azure CLI (`az login`)

### راه‌اندازی اولیه

1. **کلون یا فورک کردن مخزن:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # یا
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **ساخت و فعال‌سازی محیط مجازی پایتون:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # روی ویندوز: venv\Scripts\activate
   ```

3. **نصب وابستگی‌ها:**
   ```bash
   pip install -r requirements.txt
   ```

4. **تنظیم متغیرهای محیطی:**
   ```bash
   cp .env.example .env
   # فایل .env را با کلیدهای API و نقاط پایانی خود ویرایش کنید
   ```

### متغیرهای محیطی مورد نیاز

برای **Azure AI Foundry** (الزامی):
- `AZURE_AI_PROJECT_ENDPOINT` - نقطه انتهایی پروژه Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - نام استقرار مدل (مثلاً gpt-4o)

برای **Azure AI Search** (درس ۰۵ - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - نقطه انتهایی Azure AI Search
- `AZURE_SEARCH_API_KEY` - کلید API Azure AI Search

احراز هویت: قبل از اجرای دفترچه‌ها، دستور `az login` را اجرا کنید (از `AzureCliCredential` استفاده می‌شود).

## روند توسعه

### اجرای Jupyter Notebooks

هر درس چندین دفترچه Jupyter برای چارچوب‌های مختلف دارد:

1. **شروع Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **رفتن به دایرکتوری یک درس** (مثلاً `01-intro-to-ai-agents/code_samples/`)

3. **باز کردن و اجرای دفترچه‌ها:**
   - `*-python-agent-framework.ipynb` - استفاده از Microsoft Agent Framework (پایتون)
   - `*-dotnet-agent-framework.ipynb` - استفاده از Microsoft Agent Framework (.NET)

### کار با Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- نیاز به اشتراک Azure دارد
- از `AzureAIProjectAgentProvider` برای Agent Service V2 استفاده می‌کند (عامل‌ها در پرتال Foundry قابل مشاهده‌اند)
- آماده تولید با قابلیت مشاهده داخلی
- الگوی نامگذاری فایل: `*-python-agent-framework.ipynb`

## دستورالعمل‌های تست

این یک مخزن آموزشی با کد نمونه است نه کد تولیدی با تست‌های خودکار. برای تایید راه‌اندازی و تغییرات خود:

### تست دستی

1. **تست محیط پایتون:**
   ```bash
   python --version  # باید ۳.۱۲ یا بالاتر باشد
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **تست اجرای دفترچه:**
   ```bash
   # تبدیل دفترچه یادداشت به اسکریپت و اجرا (واردات آزمون‌ها)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **بررسی متغیرهای محیطی:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### اجرای دفترچه‌های جداگانه

دفترچه‌ها را در Jupyter باز کرده و سلول‌ها را به ترتیب اجرا کنید. هر دفترچه خودکفا است و شامل موارد زیر است:
- دستورات import
- بارگذاری پیکربندی
- پیاده‌سازی نمونه عامل
- خروجی‌های مورد انتظار در سلول‌های markdown

## سبک کدنویسی

### قراردادهای پایتون

- **نسخه پایتون**: ۳.۱۲ به بالا
- **سبک کد**: پیروی از قراردادهای استاندارد PEP 8 پایتون
- **دفترچه‌ها**: استفاده از سلول‌های markdown شفاف برای توضیح مفاهیم
- **import ها**: گروه‌بندی بر اساس کتابخانه استاندارد، شخص ثالث، و محلی

### قراردادهای دفترچه Jupyter

- اضافه کردن سلول‌های توضیحی markdown قبل از سلول‌های کد
- افزودن نمونه خروجی‌ها در دفترچه‌ها برای مرجع
- استفاده از نام‌های متغیر شفاف که با مفاهیم درس تطابق دارد
- حفظ ترتیب اجرای خطی دفترچه (سلول ۱ → ۲ → ۳...)

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
- سیستم ترجمه خودکار با GitHub Actions

### خط لوله CI/CD

در `.github/workflows/` قرار دارد:

1. **co-op-translator.yml** - ترجمه خودکار به بیش از ۵۰ زبان
2. **welcome-issue.yml** - خوش‌آمد گویی به ایجادکنندگان issue جدید
3. **welcome-pr.yml** - خوش‌آمد گویی به مشارکت‌کنندگان pull request جدید

### استقرار

این یک مخزن آموزشی است - فرایند استقرار ندارد. کاربران:
1. مخزن را فورک یا کلون کنند
2. دفترچه‌ها را به صورت محلی یا در GitHub Codespaces اجرا کنند
3. از طریق تغییر و آزمایش نمونه‌ها یاد بگیرند

## دستورالعمل‌های Pull Request

### پیش از ارسال

1. **تست تغییرات:**
   - اجرای کامل دفترچه‌های تحت تاثیر
   - اطمینان از اجرای بدون خطای تمام سلول‌ها
   - بررسی خروجی‌های مناسب

2. **به‌روزرسانی مستندات:**
   - به‌روزرسانی README.md اگر مفاهیم جدید اضافه شده
   - افزودن کامنت در دفترچه‌ها برای کدهای پیچیده
   - اطمینان از توضیح در سلول‌های markdown درباره هدف

3. **تغییرات فایل:**
   - از کامیت کردن فایل‌های `.env` خودداری کنید (از `.env.example` استفاده شود)
   - کامیت نکردن دایرکتوری‌های `venv/` یا `__pycache__/`
   - نگه داشتن خروجی دفترچه‌ها در صورت نشان دادن مفاهیم
   - حذف فایل‌های موقتی و نسخه پشتیبان دفترچه‌ها (`*-backup.ipynb`)

### فرمت عنوان PR

از عناوین توصیفی استفاده کنید:
- `[Lesson-XX] افزودن مثال جدید برای <concept>`
- `[Fix] اصلاح تایپو در README درس XX`
- `[Update] بهبود نمونه کد در درس XX`
- `[Docs] به‌روزرسانی دستورالعمل‌های راه‌اندازی`

### بررسی‌های لازم

- دفترچه‌ها باید بدون خطا اجرا شوند
- فایل‌های README واضح و دقیق باشند
- پیروی از الگوهای کد موجود در مخزن
- حفظ سازگاری با سایر دروس

## نکات اضافی

### اشتباهات رایج

1. **عدم تطابق نسخه پایتون:**
   - اطمینان از استفاده از پایتون ۳.۱۲ به بالا
   - برخی بسته‌ها ممکن است با نسخه‌های قدیمی کار نکنند
   - استفاده از `python3 -m venv` برای تعیین نسخه پایتون به صورت صریح

2. **متغیرهای محیطی:**
   - همیشه `.env` را از `.env.example` بسازید
   - فایل `.env` را commit نکنید (در `.gitignore` است)
   - توکن GitHub نیاز به مجوزهای مناسب دارد

3. **تداخل بسته‌ها:**
   - استفاده از محیط مجازی تازه
   - نصب از طریق `requirements.txt` به جای بسته‌های تکی
   - برخی دفترچه‌ها ممکن است نیاز به بسته‌های اضافی داشته باشند که در سلول‌های markdown ذکر شده‌ است

4. **خدمات Azure:**
   - خدمات AI Azure به اشتراک فعال نیاز دارند
   - برخی ویژگی‌ها منطقه‌ای هستند
   - محدودیت‌های لایه رایگان برای GitHub Models اعمال می‌شود

### مسیر یادگیری

ترتیب پیشنهادی انجام دروس:
1. **00-course-setup** - شروع راه‌اندازی محیط
2. **01-intro-to-ai-agents** - درک اصول عامل‌های هوش مصنوعی
3. **02-explore-agentic-frameworks** - آشنایی با چارچوب‌های مختلف
4. **03-agentic-design-patterns** - الگوهای طراحی اصلی
5. ادامه بر اساس شماره درس‌ها به ترتیب

### انتخاب چارچوب

چارچوب براساس اهداف شما انتخاب می‌شود:
- **همه دروس**: Microsoft Agent Framework (MAF) با `AzureAIProjectAgentProvider`
- **عامل‌ها سمت سرور ثبت می‌شوند** در Azure AI Foundry Agent Service V2 و در پرتال Foundry قابل مشاهده‌اند

### دریافت کمک

- به [انجمن Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) بپیوندید
- فایل‌های README درس برای راهنمایی خاص را بررسی کنید
- مروری بر [README.md اصلی](./README.md) برای دید کلی دوره
- مراجعه به [Course Setup](./00-course-setup/README.md) برای دستورالعمل‌های جزئی راه‌اندازی

### مشارکت

این پروژه آموزشی باز است. مشارکت‌ها خوش‌آمدیده:
- بهبود نمونه‌های کد
- اصلاح تایپوها یا خطاها
- افزودن کامنت‌های توضیحی
- پیشنهاد موضوعات جدید برای درس‌ها
- ترجمه به زبان‌های اضافی

نیازهای فعلی را در [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) مشاهده کنید.

## زمینه مخصوص پروژه

### پشتیبانی چند زبانه

این مخزن از سیستم ترجمه خودکار استفاده می‌کند:
- پشتیبانی از بیش از ۵۰ زبان
- ترجمه‌ها در دایرکتوری‌های `/translations/<lang-code>/`
- جریان کاری GitHub Actions به‌روزرسانی ترجمه‌ها را مدیریت می‌کند
- فایل‌های منبع به زبان انگلیسی در ریشه مخزن قرار دارند

### ساختار درس‌ها

هر درس الگوی ثابتی دارد:
1. تصویر بندانگشتی ویدئو با لینک
2. محتوای نوشتاری درس (README.md)
3. نمونه‌کدها در چارچوب‌های مختلف
4. اهداف یادگیری و پیش‌نیازها
5. منابع آموزشی اضافی پیوند داده شده

### نام‌گذاری نمونه‌کد

قالب: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - درس ۱، MAF پایتون
- `14-sequential.ipynb` - درس ۱۴، الگوهای پیشرفته MAF

### دایرکتوری‌های خاص

- `translated_images/` - تصاویر محلی‌سازی‌شده برای ترجمه‌ها
- `images/` - تصاویر اصل برای محتوای انگلیسی
- `.devcontainer/` - پیکربندی کانتینر توسعه VS Code
- `.github/` - جریان‌های کاری و قالب‌های GitHub Actions

### وابستگی‌ها

بسته‌های کلیدی از `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - پشتیبانی از پروتکل Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - خدمات هوش مصنوعی Azure
- `azure-identity` - احراز هویت Azure (AzureCliCredential)
- `azure-search-documents` - ادغام Azure AI Search
- `mcp[cli]` - پشتیبانی از Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده شود. ما مسئول هیچ‌گونه سوءتفاهم یا تفسیر نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->