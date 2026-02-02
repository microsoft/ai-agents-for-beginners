# AGENTS.md

## پروجیکٹ کا جائزہ

یہ ریپوزیٹری "AI Agents for Beginners" پر مشتمل ہے - ایک جامع تعلیمی کورس جو AI ایجنٹس بنانے کے لیے ضروری تمام معلومات فراہم کرتا ہے۔ کورس میں 15+ اسباق شامل ہیں جو بنیادی اصول، ڈیزائن پیٹرنز، فریم ورک، اور AI ایجنٹس کی پروڈکشن ڈیپلائمنٹ کا احاطہ کرتے ہیں۔

**اہم ٹیکنالوجیز:**
- Python 3.12+
- انٹرایکٹو لرننگ کے لیے Jupyter Notebooks
- AI فریم ورک: Semantic Kernel، AutoGen، Microsoft Agent Framework (MAF)
- Azure AI سروسز: Azure AI Foundry، Azure AI Agent Service
- GitHub Models Marketplace (مفت ٹائر دستیاب)

**آرکیٹیکچر:**
- سبق پر مبنی ساخت (00-15+ ڈائریکٹریز)
- ہر سبق میں شامل ہیں: README دستاویزات، کوڈ کے نمونے (Jupyter notebooks)، اور تصاویر
- خودکار ترجمہ نظام کے ذریعے کثیر زبان کی حمایت
- ہر سبق کے لیے متعدد فریم ورک کے اختیارات (Semantic Kernel، AutoGen، Azure AI Agent Service)

## سیٹ اپ کمانڈز

### ضروریات
- Python 3.12 یا اس سے زیادہ
- GitHub اکاؤنٹ (GitHub Models کے لیے - مفت ٹائر)
- Azure سبسکرپشن (اختیاری، Azure AI سروسز کے لیے)

### ابتدائی سیٹ اپ

1. **ریپوزیٹری کو کلون یا فورک کریں:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python ورچوئل ماحول بنائیں اور فعال کریں:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **ضروریات انسٹال کریں:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ماحول کے متغیرات سیٹ کریں:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### ضروری ماحول کے متغیرات

**GitHub Models (مفت)** کے لیے:
- `GITHUB_TOKEN` - GitHub سے پرسنل ایکسیس ٹوکن

**Azure AI سروسز** (اختیاری) کے لیے:
- `PROJECT_ENDPOINT` - Azure AI Foundry پروجیکٹ اینڈ پوائنٹ
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API کی
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI اینڈ پوائنٹ URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - چیٹ ماڈل کے لیے ڈیپلائمنٹ کا نام
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - ایمبیڈنگ کے لیے ڈیپلائمنٹ کا نام
- اضافی Azure کنفیگریشن جیسا کہ `.env.example` میں دکھایا گیا ہے

## ترقیاتی ورک فلو

### Jupyter Notebooks چلانا

ہر سبق میں مختلف فریم ورک کے لیے متعدد Jupyter notebooks شامل ہیں:

1. **Jupyter شروع کریں:**
   ```bash
   jupyter notebook
   ```

2. **سبق کی ڈائریکٹری پر جائیں** (مثال کے طور پر، `01-intro-to-ai-agents/code_samples/`)

3. **نوٹ بکس کھولیں اور چلائیں:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel فریم ورک استعمال کرتے ہوئے
   - `*-autogen.ipynb` - AutoGen فریم ورک استعمال کرتے ہوئے
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) استعمال کرتے ہوئے
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) استعمال کرتے ہوئے
   - `*-azureaiagent.ipynb` - Azure AI Agent Service استعمال کرتے ہوئے

### مختلف فریم ورک کے ساتھ کام کرنا

**Semantic Kernel + GitHub Models:**
- GitHub اکاؤنٹ کے ساتھ مفت ٹائر دستیاب
- سیکھنے اور تجربہ کرنے کے لیے بہترین
- فائل پیٹرن: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- GitHub اکاؤنٹ کے ساتھ مفت ٹائر دستیاب
- ملٹی ایجنٹ آرکیسٹریشن کی صلاحیتیں
- فائل پیٹرن: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoft کا جدید ترین فریم ورک
- Python اور .NET میں دستیاب
- فائل پیٹرن: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azure سبسکرپشن کی ضرورت ہے
- پروڈکشن کے لیے تیار خصوصیات
- فائل پیٹرن: `*-azureaiagent.ipynb`

## ٹیسٹنگ کی ہدایات

یہ ایک تعلیمی ریپوزیٹری ہے جس میں مثال کے کوڈ شامل ہیں، پروڈکشن کوڈ کے بجائے خودکار ٹیسٹ کے ساتھ۔ اپنی سیٹ اپ اور تبدیلیوں کی تصدیق کے لیے:

### دستی ٹیسٹنگ

1. **Python ماحول کی جانچ کریں:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **نوٹ بک کی عملدرآمد کی جانچ کریں:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ماحول کے متغیرات کی تصدیق کریں:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### انفرادی نوٹ بکس چلانا

نوٹ بکس کو Jupyter میں کھولیں اور سیلز کو ترتیب وار چلائیں۔ ہر نوٹ بک خود مختار ہے اور شامل کرتی ہے:
- امپورٹ اسٹیٹمنٹس
- کنفیگریشن لوڈنگ
- ایجنٹ کے نفاذ کی مثالیں
- متوقع نتائج مارک ڈاؤن سیلز میں

## کوڈ اسٹائل

### Python کنونشنز

- **Python ورژن**: 3.12+
- **کوڈ اسٹائل**: معیاری Python PEP 8 کنونشنز پر عمل کریں
- **نوٹ بکس**: تصورات کو واضح کرنے کے لیے مارک ڈاؤن سیلز استعمال کریں
- **امپورٹس**: معیاری لائبریری، تھرڈ پارٹی، اور لوکل امپورٹس کے لحاظ سے گروپ کریں

### Jupyter Notebook کنونشنز

- کوڈ سیلز سے پہلے وضاحتی مارک ڈاؤن سیلز شامل کریں
- حوالہ کے لیے نوٹ بکس میں آؤٹ پٹ کی مثالیں شامل کریں
- سبق کے تصورات سے مطابقت رکھنے والے واضح ویریبل نام استعمال کریں
- نوٹ بک کے عملدرآمد کا ترتیب لکیری رکھیں (سیل 1 → 2 → 3...)

### فائل آرگنائزیشن

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


## بلڈ اور ڈیپلائمنٹ

### دستاویزات بنانا

یہ ریپوزیٹری دستاویزات کے لیے مارک ڈاؤن استعمال کرتی ہے:
- ہر سبق فولڈر میں README.md فائلز
- ریپوزیٹری روٹ پر مرکزی README.md
- GitHub Actions کے ذریعے خودکار ترجمہ نظام

### CI/CD پائپ لائن

`.github/workflows/` میں موجود:

1. **co-op-translator.yml** - 50+ زبانوں میں خودکار ترجمہ
2. **welcome-issue.yml** - نئے مسئلے کے تخلیق کاروں کو خوش آمدید کہتا ہے
3. **welcome-pr.yml** - نئے پل ریکویسٹ کے تعاون کرنے والوں کو خوش آمدید کہتا ہے

### ڈیپلائمنٹ

یہ ایک تعلیمی ریپوزیٹری ہے - کوئی ڈیپلائمنٹ عمل نہیں۔ صارفین:
1. ریپوزیٹری کو فورک یا کلون کریں
2. نوٹ بکس کو مقامی طور پر یا GitHub Codespaces میں چلائیں
3. مثالوں میں ترمیم اور تجربہ کرکے سیکھیں

## پل ریکویسٹ گائیڈ لائنز

### جمع کرانے سے پہلے

1. **اپنی تبدیلیوں کی جانچ کریں:**
   - متاثرہ نوٹ بکس کو مکمل طور پر چلائیں
   - تصدیق کریں کہ تمام سیلز بغیر کسی غلطی کے چلتے ہیں
   - چیک کریں کہ آؤٹ پٹ مناسب ہیں

2. **دستاویزات کی اپ ڈیٹس:**
   - اگر نئے تصورات شامل کر رہے ہیں تو README.md کو اپ ڈیٹ کریں
   - پیچیدہ کوڈ کے لیے نوٹ بکس میں تبصرے شامل کریں
   - یقینی بنائیں کہ مارک ڈاؤن سیلز مقصد کی وضاحت کرتے ہیں

3. **فائل تبدیلیاں:**
   - `.env` فائلز کو کمیٹ کرنے سے گریز کریں (`.env.example` استعمال کریں)
   - `venv/` یا `__pycache__/` ڈائریکٹریز کو کمیٹ نہ کریں
   - جب وہ تصورات کو ظاہر کرتے ہیں تو نوٹ بک آؤٹ پٹ کو برقرار رکھیں
   - عارضی فائلز اور بیک اپ نوٹ بکس (`*-backup.ipynb`) کو ہٹا دیں

### PR عنوان کا فارمیٹ

وضاحتی عنوانات استعمال کریں:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### ضروری چیکس

- نوٹ بکس کو بغیر کسی غلطی کے چلنا چاہیے
- README فائلز واضح اور درست ہونی چاہئیں
- ریپوزیٹری میں موجودہ کوڈ پیٹرنز کی پیروی کریں
- دیگر اسباق کے ساتھ مطابقت برقرار رکھیں

## اضافی نوٹس

### عام مسائل

1. **Python ورژن کا عدم مطابقت:**
   - یقینی بنائیں کہ Python 3.12+ استعمال ہو رہا ہے
   - کچھ پیکجز پرانے ورژنز کے ساتھ کام نہیں کریں گے
   - Python ورژن کو واضح طور پر بتانے کے لیے `python3 -m venv` استعمال کریں

2. **ماحول کے متغیرات:**
   - ہمیشہ `.env.example` سے `.env` بنائیں
   - `.env` فائل کو کمیٹ نہ کریں (یہ `.gitignore` میں ہے)
   - GitHub ٹوکن کو مناسب اجازتوں کی ضرورت ہے

3. **پیکج تنازعات:**
   - ایک نیا ورچوئل ماحول استعمال کریں
   - انفرادی پیکجز کے بجائے `requirements.txt` سے انسٹال کریں
   - کچھ نوٹ بکس کو اضافی پیکجز کی ضرورت ہو سکتی ہے جو ان کے مارک ڈاؤن سیلز میں ذکر کیے گئے ہیں

4. **Azure سروسز:**
   - Azure AI سروسز کو فعال سبسکرپشن کی ضرورت ہے
   - کچھ خصوصیات علاقہ مخصوص ہیں
   - GitHub Models پر مفت ٹائر کی حدود لاگو ہوتی ہیں

### سیکھنے کا راستہ

سبق کے ذریعے تجویز کردہ ترقی:
1. **00-course-setup** - ماحول کی سیٹ اپ کے لیے یہاں سے شروع کریں
2. **01-intro-to-ai-agents** - AI ایجنٹ کے بنیادی اصول سمجھیں
3. **02-explore-agentic-frameworks** - مختلف فریم ورک کے بارے میں سیکھیں
4. **03-agentic-design-patterns** - بنیادی ڈیزائن پیٹرنز
5. نمبر شدہ اسباق کو ترتیب وار جاری رکھیں

### فریم ورک کا انتخاب

اپنے اہداف کی بنیاد پر فریم ورک منتخب کریں:
- **سیکھنا/پروٹوٹائپنگ**: Semantic Kernel + GitHub Models (مفت)
- **ملٹی ایجنٹ سسٹمز**: AutoGen
- **جدید خصوصیات**: Microsoft Agent Framework (MAF)
- **پروڈکشن ڈیپلائمنٹ**: Azure AI Agent Service

### مدد حاصل کرنا

- [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord) میں شامل ہوں
- مخصوص رہنمائی کے لیے سبق README فائلز کا جائزہ لیں
- کورس کے جائزے کے لیے مرکزی [README.md](./README.md) چیک کریں
- تفصیلی سیٹ اپ ہدایات کے لیے [Course Setup](./00-course-setup/README.md) کا حوالہ دیں

### تعاون کرنا

یہ ایک کھلا تعلیمی پروجیکٹ ہے۔ تعاون کا خیر مقدم:
- کوڈ کی مثالوں کو بہتر بنائیں
- ٹائپوز یا غلطیوں کو درست کریں
- وضاحتی تبصرے شامل کریں
- نئے سبق کے موضوعات تجویز کریں
- اضافی زبانوں میں ترجمہ کریں

موجودہ ضروریات کے لیے [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) دیکھیں۔

## پروجیکٹ کے مخصوص سیاق و سباق

### کثیر زبان کی حمایت

یہ ریپوزیٹری خودکار ترجمہ نظام استعمال کرتی ہے:
- 50+ زبانوں کی حمایت
- ترجمے `/translations/<lang-code>/` ڈائریکٹریز میں
- GitHub Actions ورک فلو ترجمہ اپ ڈیٹس کو ہینڈل کرتا ہے
- سورس فائلز ریپوزیٹری روٹ پر انگریزی میں ہیں

### سبق کی ساخت

ہر سبق ایک مستقل پیٹرن کی پیروی کرتا ہے:
1. ویڈیو تھمب نیل کے ساتھ لنک
2. تحریری سبق مواد (README.md)
3. متعدد فریم ورک میں کوڈ کے نمونے
4. سیکھنے کے مقاصد اور ضروریات
5. اضافی سیکھنے کے وسائل کے لنکس

### کوڈ نمونے کے نام

فارمیٹ: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - سبق 4، Semantic Kernel
- `07-autogen.ipynb` - سبق 7، AutoGen
- `14-python-agent-framework.ipynb` - سبق 14، MAF Python
- `14-dotnet-agent-framework.ipynb` - سبق 14، MAF .NET

### خاص ڈائریکٹریز

- `translated_images/` - ترجمہ شدہ تصاویر کے لیے
- `images/` - انگریزی مواد کے لیے اصل تصاویر
- `.devcontainer/` - VS Code ترقیاتی کنٹینر کنفیگریشن
- `.github/` - GitHub Actions ورک فلو اور ٹیمپلیٹس

### ضروریات

`requirements.txt` سے کلیدی پیکجز:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen فریم ورک
- `semantic-kernel` - Semantic Kernel فریم ورک
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI سروسز
- `azure-search-documents` - Azure AI Search انٹیگریشن
- `chromadb` - RAG مثالوں کے لیے ویکٹر ڈیٹا بیس
- `chainlit` - چیٹ UI فریم ورک
- `browser_use` - ایجنٹس کے لیے براؤزر آٹومیشن
- `mcp[cli]` - ماڈل کانٹیکسٹ پروٹوکول سپورٹ
- `mem0ai` - ایجنٹس کے لیے میموری مینجمنٹ

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔