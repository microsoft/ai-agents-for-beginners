# AGENTS.md

## نمای کلی پروژه

این مخزن شامل "عوامل هوش مصنوعی برای مبتدیان" است - یک دوره آموزشی جامع که همه چیز مورد نیاز برای ساخت عوامل هوش مصنوعی را آموزش می‌دهد. این دوره شامل بیش از 15 درس است که اصول اولیه، الگوهای طراحی، چارچوب‌ها و استقرار عوامل هوش مصنوعی در محیط تولید را پوشش می‌دهد.

**فناوری‌های کلیدی:**
- Python 3.12+
- Jupyter Notebooks برای یادگیری تعاملی
- چارچوب‌های هوش مصنوعی: Semantic Kernel، AutoGen، Microsoft Agent Framework (MAF)
- خدمات Azure AI: Azure AI Foundry، Azure AI Agent Service
- بازار مدل‌های GitHub (نسخه رایگان موجود)

**معماری:**
- ساختار مبتنی بر درس (پوشه‌های 00-15+)
- هر درس شامل: مستندات README، نمونه‌های کد (دفترچه‌های Jupyter) و تصاویر
- پشتیبانی چندزبانه از طریق سیستم ترجمه خودکار
- گزینه‌های متعدد چارچوب برای هر درس (Semantic Kernel، AutoGen، Azure AI Agent Service)

## دستورات راه‌اندازی

### پیش‌نیازها
- Python 3.12 یا بالاتر
- حساب GitHub (برای مدل‌های GitHub - نسخه رایگان)
- اشتراک Azure (اختیاری، برای خدمات Azure AI)

### راه‌اندازی اولیه

1. **کلون یا فورک کردن مخزن:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **ایجاد و فعال‌سازی محیط مجازی Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **نصب وابستگی‌ها:**
   ```bash
   pip install -r requirements.txt
   ```

4. **تنظیم متغیرهای محیطی:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### متغیرهای محیطی مورد نیاز

برای **مدل‌های GitHub (رایگان):**
- `GITHUB_TOKEN` - توکن دسترسی شخصی از GitHub

برای **خدمات Azure AI** (اختیاری):
- `PROJECT_ENDPOINT` - نقطه پایانی پروژه Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - کلید API Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL نقطه پایانی Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - نام استقرار برای مدل چت
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - نام استقرار برای تعبیه‌ها
- تنظیمات اضافی Azure همانطور که در `.env.example` نشان داده شده است

## جریان کاری توسعه

### اجرای دفترچه‌های Jupyter

هر درس شامل چندین دفترچه Jupyter برای چارچوب‌های مختلف است:

1. **شروع Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **به یک پوشه درس بروید** (مثلاً `01-intro-to-ai-agents/code_samples/`)

3. **دفترچه‌ها را باز و اجرا کنید:**
   - `*-semantic-kernel.ipynb` - استفاده از چارچوب Semantic Kernel
   - `*-autogen.ipynb` - استفاده از چارچوب AutoGen
   - `*-python-agent-framework.ipynb` - استفاده از Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - استفاده از Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - استفاده از Azure AI Agent Service

### کار با چارچوب‌های مختلف

**Semantic Kernel + مدل‌های GitHub:**
- نسخه رایگان با حساب GitHub موجود است
- مناسب برای یادگیری و آزمایش
- الگوی فایل: `*-semantic-kernel*.ipynb`

**AutoGen + مدل‌های GitHub:**
- نسخه رایگان با حساب GitHub موجود است
- قابلیت‌های هماهنگی چندعامل
- الگوی فایل: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- جدیدترین چارچوب از Microsoft
- موجود در Python و .NET
- الگوی فایل: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- نیاز به اشتراک Azure دارد
- ویژگی‌های آماده تولید
- الگوی فایل: `*-azureaiagent.ipynb`

## دستورالعمل‌های تست

این مخزن آموزشی شامل کد نمونه است و کد تولیدی با تست‌های خودکار نیست. برای بررسی تنظیمات و تغییرات خود:

### تست دستی

1. **تست محیط Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **تست اجرای دفترچه‌ها:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **بررسی متغیرهای محیطی:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### اجرای دفترچه‌های جداگانه

دفترچه‌ها را در Jupyter باز کنید و سلول‌ها را به ترتیب اجرا کنید. هر دفترچه مستقل است و شامل موارد زیر می‌شود:
- دستورات وارد کردن
- بارگذاری تنظیمات
- پیاده‌سازی‌های نمونه عامل
- خروجی‌های مورد انتظار در سلول‌های markdown

## سبک کدنویسی

### قراردادهای Python

- **نسخه Python**: 3.12+
- **سبک کدنویسی**: پیروی از استانداردهای PEP 8 Python
- **دفترچه‌ها**: استفاده از سلول‌های markdown واضح برای توضیح مفاهیم
- **وارد کردن‌ها**: گروه‌بندی بر اساس کتابخانه استاندارد، کتابخانه‌های شخص ثالث، وارد کردن‌های محلی

### قراردادهای دفترچه Jupyter

- شامل سلول‌های markdown توصیفی قبل از سلول‌های کد
- افزودن نمونه‌های خروجی در دفترچه‌ها برای مرجع
- استفاده از نام‌های متغیر واضح که با مفاهیم درس مطابقت دارند
- حفظ ترتیب اجرای دفترچه‌ها به صورت خطی (سلول 1 → 2 → 3...)

### سازماندهی فایل‌ها

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## ساخت و استقرار

### ساخت مستندات

این مخزن از Markdown برای مستندات استفاده می‌کند:
- فایل‌های README.md در هر پوشه درس
- README.md اصلی در ریشه مخزن
- سیستم ترجمه خودکار از طریق GitHub Actions

### خط لوله CI/CD

در `.github/workflows/` قرار دارد:

1. **co-op-translator.yml** - ترجمه خودکار به بیش از 50 زبان
2. **welcome-issue.yml** - خوش‌آمدگویی به ایجادکنندگان مسائل جدید
3. **welcome-pr.yml** - خوش‌آمدگویی به مشارکت‌کنندگان درخواست‌های کشش جدید

### استقرار

این یک مخزن آموزشی است - فرآیند استقرار ندارد. کاربران:
1. مخزن را فورک یا کلون کنند
2. دفترچه‌ها را به صورت محلی یا در GitHub Codespaces اجرا کنند
3. با تغییر و آزمایش مثال‌ها یاد بگیرند

## دستورالعمل‌های درخواست کشش

### قبل از ارسال

1. **تست تغییرات خود:**
   - دفترچه‌های تحت تأثیر را به طور کامل اجرا کنید
   - بررسی کنید که همه سلول‌ها بدون خطا اجرا شوند
   - خروجی‌ها را مناسب بررسی کنید

2. **به‌روزرسانی مستندات:**
   - README.md را به‌روزرسانی کنید اگر مفاهیم جدیدی اضافه می‌کنید
   - برای کد پیچیده در دفترچه‌ها توضیحات اضافه کنید
   - اطمینان حاصل کنید که سلول‌های markdown هدف را توضیح می‌دهند

3. **تغییرات فایل:**
   - از تعهد فایل‌های `.env` خودداری کنید (از `.env.example` استفاده کنید)
   - پوشه‌های `venv/` یا `__pycache__/` را تعهد نکنید
   - خروجی‌های دفترچه‌ها را حفظ کنید وقتی که مفاهیم را نشان می‌دهند
   - فایل‌های موقت و دفترچه‌های پشتیبان (`*-backup.ipynb`) را حذف کنید

### قالب عنوان PR

از عناوین توصیفی استفاده کنید:
- `[Lesson-XX] افزودن مثال جدید برای <مفهوم>`
- `[Fix] اصلاح اشتباه تایپی در README درس-XX`
- `[Update] بهبود نمونه کد در درس-XX`
- `[Docs] به‌روزرسانی دستورالعمل‌های راه‌اندازی`

### بررسی‌های مورد نیاز

- دفترچه‌ها باید بدون خطا اجرا شوند
- فایل‌های README باید واضح و دقیق باشند
- پیروی از الگوهای کد موجود در مخزن
- حفظ سازگاری با سایر درس‌ها

## یادداشت‌های اضافی

### مشکلات رایج

1. **عدم تطابق نسخه Python:**
   - اطمینان حاصل کنید که از Python 3.12+ استفاده می‌کنید
   - برخی بسته‌ها ممکن است با نسخه‌های قدیمی‌تر کار نکنند
   - از `python3 -m venv` برای مشخص کردن نسخه Python به طور صریح استفاده کنید

2. **متغیرهای محیطی:**
   - همیشه `.env` را از `.env.example` ایجاد کنید
   - فایل `.env` را تعهد نکنید (در `.gitignore` است)
   - توکن GitHub نیاز به مجوزهای مناسب دارد

3. **تعارض بسته‌ها:**
   - از یک محیط مجازی تازه استفاده کنید
   - از `requirements.txt` نصب کنید به جای بسته‌های جداگانه
   - برخی دفترچه‌ها ممکن است نیاز به بسته‌های اضافی ذکر شده در سلول‌های markdown خود داشته باشند

4. **خدمات Azure:**
   - خدمات Azure AI نیاز به اشتراک فعال دارند
   - برخی ویژگی‌ها منطقه‌ای هستند
   - محدودیت‌های نسخه رایگان برای مدل‌های GitHub اعمال می‌شود

### مسیر یادگیری

پیشرفت پیشنهادی از طریق درس‌ها:
1. **00-course-setup** - از اینجا برای تنظیم محیط شروع کنید
2. **01-intro-to-ai-agents** - اصول اولیه عوامل هوش مصنوعی را درک کنید
3. **02-explore-agentic-frameworks** - درباره چارچوب‌های مختلف بیاموزید
4. **03-agentic-design-patterns** - الگوهای طراحی اصلی
5. ادامه دهید از طریق درس‌های شماره‌گذاری شده به ترتیب

### انتخاب چارچوب

چارچوب را بر اساس اهداف خود انتخاب کنید:
- **یادگیری/نمونه‌سازی اولیه**: Semantic Kernel + مدل‌های GitHub (رایگان)
- **سیستم‌های چندعاملی**: AutoGen
- **ویژگی‌های جدید**: Microsoft Agent Framework (MAF)
- **استقرار تولید**: Azure AI Agent Service

### دریافت کمک

- به [جامعه Discord Azure AI Foundry](https://aka.ms/ai-agents/discord) بپیوندید
- فایل‌های README درس را برای راهنمایی خاص مرور کنید
- README.md اصلی [README.md](./README.md) را برای نمای کلی دوره بررسی کنید
- به [Course Setup](./00-course-setup/README.md) برای دستورالعمل‌های تنظیم دقیق مراجعه کنید

### مشارکت

این یک پروژه آموزشی باز است. مشارکت‌ها خوش‌آمدند:
- بهبود مثال‌های کد
- اصلاح اشتباهات تایپی یا خطاها
- افزودن توضیحات روشن‌کننده
- پیشنهاد موضوعات جدید درس
- ترجمه به زبان‌های اضافی

به [مسائل GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) برای نیازهای فعلی مراجعه کنید.

## زمینه خاص پروژه

### پشتیبانی چندزبانه

این مخزن از یک سیستم ترجمه خودکار استفاده می‌کند:
- پشتیبانی از بیش از 50 زبان
- ترجمه‌ها در پوشه‌های `/translations/<lang-code>/` قرار دارند
- گردش کار GitHub Actions ترجمه‌ها را به‌روزرسانی می‌کند
- فایل‌های منبع به زبان انگلیسی در ریشه مخزن هستند

### ساختار درس

هر درس از یک الگوی ثابت پیروی می‌کند:
1. تصویر بندانگشتی ویدیو با لینک
2. محتوای درس نوشته شده (README.md)
3. نمونه‌های کد در چارچوب‌های مختلف
4. اهداف یادگیری و پیش‌نیازها
5. منابع یادگیری اضافی لینک شده

### نام‌گذاری نمونه‌های کد

فرمت: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - درس 4، Semantic Kernel
- `07-autogen.ipynb` - درس 7، AutoGen
- `14-python-agent-framework.ipynb` - درس 14، MAF Python
- `14-dotnet-agent-framework.ipynb` - درس 14، MAF .NET

### پوشه‌های ویژه

- `translated_images/` - تصاویر محلی‌سازی شده برای ترجمه‌ها
- `images/` - تصاویر اصلی برای محتوای انگلیسی
- `.devcontainer/` - پیکربندی کانتینر توسعه VS Code
- `.github/` - گردش کار و قالب‌های GitHub Actions

### وابستگی‌ها

بسته‌های کلیدی از `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - چارچوب AutoGen
- `semantic-kernel` - چارچوب Semantic Kernel
- `agent-framework` - چارچوب Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - خدمات Azure AI
- `azure-search-documents` - یکپارچه‌سازی جستجوی Azure AI
- `chromadb` - پایگاه داده برداری برای مثال‌های RAG
- `chainlit` - چارچوب رابط کاربری چت
- `browser_use` - اتوماسیون مرورگر برای عوامل
- `mcp[cli]` - پشتیبانی از پروتکل زمینه مدل
- `mem0ai` - مدیریت حافظه برای عوامل

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.