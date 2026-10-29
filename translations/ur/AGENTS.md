# AGENTS.md

## پراجیکٹ کا جائزہ

یہ ذخیرہ "نئے شروع کرنے والوں کے لیے AI ایجنٹس" پر مشتمل ہے - ایک جامع تعلیمی کورس جو AI ایجنٹس بنانے کے لیے درکار تمام چیزوں کی تعلیم دیتا ہے۔ کورس میں 18 اسباق (نمبر 00-18) شامل ہیں جن میں بنیادی باتیں، ڈیزائن پیٹرن، فریم ورکس، پروڈکشن تعیناتی، لوکل/ڈیوائس ایجنٹس، اور AI ایجنٹس کی سیکیورٹی شامل ہیں۔

**اہم ٹیکنالوجیز:**
- پائتھن 3.12+
- متعامل سیکھنے کے لیے Jupyter نوٹ بکس
- AI فریم ورکس: مائیکروسافٹ ایجنٹ فریم ورک (MAF)
- Azure AI سروسز: مائیکروسافٹ فاؤنڈری، مائیکروسافٹ فاؤنڈری ایجنٹ سروس V2

**معماری:**
- سبق کی بنیاد پر ساخت (00-18 ڈائریکٹریز)
- ہر سبق میں شامل ہے: README دستاویزات، کوڈ مثالیں (Jupyter نوٹ بکس)، اور تصاویر
- خودکار ترجمہ نظام کے ذریعے کثیر لسانی حمایت
- ہر سبق کے لیے ایک Python نوٹ بک جو Microsoft Agent Framework استعمال کرتی ہے

## سیٹ اپ کمانڈز

### ضروریات
- پائتھن 3.12 یا اس سے زیادہ
- Azure سبسکرپشن (مائیکروسافٹ فاؤنڈری کے لیے)
- Azure CLI انسٹال اور مستند شدہ (`az login`)

### ابتدائی سیٹ اپ

1. **ذخیرہ کلون یا فورک کریں:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python ورچوئل ماحول بنائیں اور چالو کریں:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **انحصار نصب کریں:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ماحول کے متغیرات سیٹ کریں:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### ضروری ماحول کے متغیرات

**Microsoft Foundry** کے لیے (ضروری):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry پروجیکٹ اینڈ پوائنٹ
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ماڈل تعیناتی کا نام (مثلاً gpt-5-mini)

**Azure AI Search** کے لیے (سبق 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search اینڈ پوائنٹ
- `AZURE_SEARCH_API_KEY` - Azure AI Search API کلید

مستند کاری: Jupyter نوٹ بکس چلانے سے پہلے `az login` چلائیں (یہ `AzureCliCredential` استعمال کرتا ہے)۔

## ترقیاتی ورک فلو

### Jupyter نوٹ بکس چلانا

ہر سبق میں مختلف فریم ورکس کے لیے متعدد Jupyter نوٹ بکس ہوتے ہیں:

1. **Jupyter شروع کریں:**
   ```bash
   jupyter notebook
   ```

2. **سبق کی ڈائریکٹری میں جائیں** (مثلاً `01-intro-to-ai-agents/code_samples/`)

3. **نوٹ بکس کھولیں اور چلائیں:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) استعمال کرتے ہوئے
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) استعمال کرتے ہوئے

### Microsoft Agent Framework کے ساتھ کام کرنا

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure سبسکرپشن ضروری ہے
- ایجنٹ سروس V2 کے لیے `FoundryChatClient` استعمال کرتا ہے (ایجنٹس Foundry پورٹل میں نظر آتے ہیں)
- بلٹ ان آبزروربیلٹی کے ساتھ پروڈکشن کے قابل
- فائل پیٹرن: `*-python-agent-framework.ipynb`

## جانچ کے ہدایات

یہ تعلیمی ذخیرہ ہے جس میں مثال کوڈ ہے، پروڈکشن کوڈ یا خودکار ٹیسٹس نہیں۔ اپنا سیٹ اپ اور تبدیلیوں کی تصدیق کے لیے:

### دستی جانچ

1. **پائتھن ماحول کی جانچ کریں:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **نوٹ بک کی کارروائی کی جانچ کریں:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ماحول کے متغیرات کی تصدیق کریں:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### انفرادی نوٹ بکس چلانا

Jupyter میں نوٹ بکس کھولیں اور سیلز کو ترتیب سے چلائیں۔ ہر نوٹ بک خود مشتمل ہوتا ہے اور شامل کرتا ہے:
- امپورٹ بیان
- کنفیگریشن لوڈنگ
- ایجنٹ کی مثالیں
- مارک ڈاؤن سیلز میں متوقع نتائج

### تعینات ایجنٹس کی اسموک ٹیسٹنگ

ان اسباق کے لیے جہاں ایجنٹ Microsoft Foundry میزبان ایجنٹ کے طور پر تعینات ہوتا ہے (01, 04, 05, 16)، ریپو اسموک ٹیسٹ کیٹلاگز `tests/` کے تحت فراہم کرتا ہے جو `.github/workflows/smoke-test.yml` ورک فلو ذریعے [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) ایکشن کے ذریعہ چلائے جاتے ہیں۔ یہ ایک ہلکا پوسٹ-تعیناتی گارنٹی ہے (کیا ایجنٹ قابل رسائی ہے اور بنیادی پرامپٹ توقعات پر عمل کر رہا ہے؟)، جو اسباق 10 اور 16 میں جانچ پائپ لائن کو مکمل کرتا ہے۔ کیٹلاگ سے سبق اور ایجنٹ کے ملاپ کے لیے [tests/README.md](./tests/README.md) دیکھیں۔ سبق 17 لوکل Foundry Local کے ساتھ چلتا ہے اور اس کا کوئی میزبان اینڈپوائنٹ نہیں ہے، لہذا اس کی توثیق اس کے نوٹ بک کو براہ راست چلا کر کی جاتی ہے۔

## کوڈ اسٹائل

### Python کی روایات

- **Python ورژن**: 3.12+
- **کوڈ اسٹائل**: معیاری Python PEP 8 روایات کی پیروی کریں
- **نوٹ بکس**: تصورات کی وضاحت کے لیے واضح مارک ڈاؤن سیلز استعمال کریں
- **امپورٹس**: معیاری لائبریری، تیسری پارٹی، لوکل امپورٹس کی ترتیب دیں

### Jupyter نوٹ بک کی روایات

- کوڈ سیلز سے پہلے وضاحتی مارک ڈاؤن سیلز شامل کریں
- حوالہ کے لیے نوٹ بکس میں آؤٹ پٹ کی مثالیں دیں
- سبق کے تصورات کے مطابق واضح متغیر نام استعمال کریں
- نوٹ بک چلانے کا تسلسل خطی رکھیں (سیل 1 → 2 → 3...)

### فائل کی تنظیم

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## تعمیر اور تعیناتی

### دستاویزات کی تعمیر

یہ ذخیرہ دستاویزات کے لیے مارک ڈاؤن استعمال کرتا ہے:
- ہر سبق کے فولڈر میں README.md فائلیں
- ذخیرہ کی جڑ میں مرکزی README.md فائل
- GitHub Actions کے ذریعے خودکار ترجمہ نظام

### CI/CD پائپ لائن

`.github/workflows/` میں واقع:

1. **co-op-translator.yml** - 50+ زبانوں میں خودکار ترجمہ
2. **welcome-issue.yml** - نئے ایشو بنانے والوں کو خوش آمدید کہتا ہے
3. **welcome-pr.yml** - نئے پل ریکویسٹ تعاون کرنے والوں کو خوش آمدید کہتا ہے

### تعیناتی

یہ تعلیمی ذخیرہ ہے - کوئی تعیناتی کا عمل نہیں۔ صارفین:
1. ذخیرہ فورک یا کلون کریں
2. لوکل یا GitHub Codespaces میں نوٹ بکس چلائیں
3. مثالوں میں ترمیم اور تجربہ کر کے سیکھیں

## پل ریکویسٹ کے ہدایات

### جمع کروانے سے پہلے

1. **اپنی تبدیلیوں کا ٹیسٹ کریں:**
   - متاثرہ نوٹ بکس مکمل طور پر چلائیں
   - یقینی بنائیں کہ تمام سیلز بغیر غلطی کے چلتی ہیں
   - چیک کریں کہ نتائج مناسب ہیں

2. **دستاویزات کی تازہ کاری:**
   - اگر نئے تصورات شامل کر رہے ہیں تو README.md اپ ڈیٹ کریں
   - پیچیدہ کوڈ کے لیے نوٹ بکس میں تبصرے شامل کریں
   - یقینی بنائیں کہ مارک ڈاؤن سیلز مقصد کی وضاحت کرتے ہیں

3. **فائل چینجز:**
   - `.env` فائلیں جمع نہ کروائیں (استعمال کریں `.env.example`)
   - `venv/` یا `__pycache__/` ڈائریکٹریز جمع نہ کروائیں
   - جب نوٹ بک آؤٹ پٹ تصورات کی وضاحت کرتی ہے اسے رکھیں
   - عارضی فائلیں اور بیک اپ نوٹ بکس ہٹا دیں (`*-backup.ipynb`)

### PR عنوان کا فارمیٹ

وضاحتی عنوانات استعمال کریں:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### درکار چیکس

- نوٹ بکس بغیر غلطی کے چلنی چاہئیں
- README فائلیں واضح اور درست ہونی چاہئیں
- ذخیرہ میں موجودہ کوڈ پیٹرنز کی پیروی کریں
- دیگر اسباق کے ساتھ مطابقت برقرار رکھیں

## اضافی نوٹس

### عام مسائل

1. **Python ورژن میں فرق:**
   - یقینی بنائیں کہ Python 3.12+ استعمال ہو رہا ہے
   - بعض پیکجز پرانے ورژنز کے ساتھ کام نہیں کرتے
   - Python ورژن صراحت سے مقرر کرنے کے لیے `python3 -m venv` استعمال کریں

2. **ماحول کے متغیرات:**
   - ہمیشہ `.env` سے `.env.example` بنائیں
   - `.env` فائل جمع نہ کروائیں (یہ `.gitignore` میں ہے)
   - کلید کے بغیر Entra ID مستند کاری کے لیے `az login` کے ساتھ سائن ان کریں

3. **پیکج تنازعات:**
   - نیا ورچوئل ماحول استعمال کریں
   - ہر پیکج کی بجائے `requirements.txt` سے انسٹال کریں
   - بعض نوٹ بکس میں اضافی پیکجز کی ضرورت ہوتی ہے جو ان کے مارک ڈاؤن سیلز میں دیے گئے ہیں

4. **Azure سروسز:**
   - Azure AI سروسز کے لیے فعال سبسکرپشن ضروری ہے
   - بعض خصوصیات علاقائی نوعیت کی ہیں
   - یقین کریں کہ آپ کی Azure OpenAI ماڈل تعیناتی Responses API کی حمایت کرتی ہے

### سیکھنے کا راستہ

سفارش کردہ اسباق کی ترتیب:
1. **00-course-setup** - ماحول کی تیاری کے لیے یہاں شروع کریں
2. **01-intro-to-ai-agents** - AI ایجنٹس کے بنیادی اصول سمجھیں
3. **02-explore-agentic-frameworks** - مختلف فریم ورکس کے بارے میں جانیں
4. **03-agentic-design-patterns** - بنیادی ڈیزائن پیٹرنز
5. نمبر والے اسباق کو ترتیب وار جاری رکھیں

### فریم ورک کا انتخاب

اپنے مقاصد کی بنیاد پر فریم ورک کا انتخاب کریں:
- **تمام اسباق**: Microsoft Agent Framework (MAF) کے ساتھ `FoundryChatClient`
- **ایجنٹس سرور-جانب Microsoft Foundry Agent Service V2 میں رجسٹر ہوتے ہیں اور Foundry پورٹل میں نظر آتے ہیں**

### مدد حاصل کرنا

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں
- مخصوص رہنمائی کے لیے سبق کے README فائلز دیکھیں
- کورس کا جائزہ لینے کے لیے مرکزی [README.md](./README.md) دیکھیں
- تفصیلی سیٹ اپ ہدایات کے لیے [Course Setup](./00-course-setup/README.md) ملاحظہ کریں

### تعاون کرنا

یہ ایک کھلا تعلیمی پروجیکٹ ہے۔ تعاون خوش آمدید:
- کوڈ کی مثالوں کو بہتر کریں
- ٹائپوز یا غلطیوں کو درست کریں
- وضاحتی تبصرے شامل کریں
- نئے سبق کے موضوعات تجویز کریں
- مزید زبانوں میں ترجمہ کریں

موجودہ ضروریات کے لیے [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) دیکھیں۔

## پروجیکٹ مخصوص سیاق و سباق

### کثیر لسانی حمایت

یہ ذخیرہ خودکار ترجمہ نظام استعمال کرتا ہے:
- 50+ زبانوں کی حمایت
- ترجمے `/translations/<lang-code>/` ڈائریکٹریز میں
- ترجمہ کی تازہ کاریوں کے لیے GitHub Actions ورک فلو
- ماخذ فائلیں انگریزی میں ذخیرہ کی جڑ میں

### سبق کی ساخت

ہر سبق یکساں پیٹرن پر عمل کرتا ہے:
1. لنک کے ساتھ ویڈیو تھمب نیل
2. تحریری سبق کا مواد (README.md)
3. متعدد فریم ورکس میں کوڈ کی مثالیں
4. سیکھنے کے مقاصد اور ضروریات
5. اضافی سیکھنے کے وسائل کے لنکس

### کوڈ سمپل کے نام

فارمیٹ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - سبق 1، MAF Python
- `14-sequential.ipynb` - سبق 14، MAF اعلیٰ درجے کے پیٹرنز
- `16-python-agent-framework.ipynb` - سبق 16، پروڈکشن کسٹمر سپورٹ ایجنٹ
- `17-local-agent-foundry-local.ipynb` - سبق 17، لوکل ایجنٹ Foundry Local + Qwen کے ساتھ

### خاص ڈائریکٹریز

- `translated_images/` - ترجموں کے لیے مقامی تصاویر
- `images/` - انگریزی مواد کے لیے اصل تصاویر
- `.devcontainer/` - VS Code ڈیولپمنٹ کنٹینر کی ترتیب
- `.github/` - GitHub Actions ورک فلو اور ٹیمپلیٹس

### انحصارات

اہم پیکجز `requirements.txt` سے:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent پروٹوکول سپورٹ
- `azure-ai-inference`, `azure-ai-projects` - Azure AI سروسز
- `azure-identity` - Azure توثیق (AzureCliCredential)
- `azure-search-documents` - Azure AI سرچ انضمام
- `mcp[cli]` - ماڈل کانٹیکسٹ پروٹوکول سپورٹ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->