# AGENTS.md

## پروجیکٹ کا جائزہ

یہ ریپوزیٹری "AI Agents for Beginners" پر مشتمل ہے - ایک جامع تعلیمی کورس جو AI ایجنٹس بنانے کے لیے درکار ہر چیز سکھاتا ہے۔ کورس میں 15+ اسباق شامل ہیں جو بنیادیات، ڈیزائن پیٹرنز، فریم ورک، اور AI ایجنٹس کی پروڈکشن تعیناتی کا احاطہ کرتے ہیں۔

**اہم ٹیکنالوجیز:**
- Python 3.12+
- تعاملی تعلیم کے لیے Jupyter Notebooks
- AI فریم ورکس: Microsoft Agent Framework (MAF)
- Azure AI سروسز: Microsoft Foundry, Azure AI Foundry Agent Service V2

**معماری:**
- سبق بنیاد پر ساخت (00-15+ ڈائریکٹریز)
- ہر سبق میں شامل ہیں: README دستاویزات، کوڈ نمونے (Jupyter نوٹ بکس)، اور تصاویر
- خودکار ترجمہ نظام کے ذریعے کثیر لسانی معاونت
- ہر سبق کے لیے ایک Python نوٹ بک جو Microsoft Agent Framework استعمال کرتی ہے

## سیٹ اپ کمانڈز

### قبل از شرط
- Python 3.12 یا اس سے اوپر
- Azure سبسکرپشن (Azure AI Foundry کے لیے)
- Azure CLI انسٹال اور مستند (`az login`)

### ابتدائی سیٹ اپ

1. **ریپوزیٹری کلون یا فورک کریں:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # یا
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python ورچوئل ماحول بنائیں اور فعال کریں:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # ونڈوز پر: venv\Scripts\activate
   ```

3. **Dependencies انسٹال کریں:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ماحول کے متغیرات ترتیب دیں:**
   ```bash
   cp .env.example .env
   # اپنی API کیز اور اینڈ پوائنٹس کے ساتھ .env کو ترمیم کریں
   ```

### مطلوبہ ماحول کے متغیرات

برائے **Azure AI Foundry** (ضروری):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry پروجیکٹ اینڈپوائنٹ
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ماڈل ڈیپلائمنٹ کا نام (مثلاً gpt-4o)

برائے **Azure AI Search** (سبق 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search اینڈپوائنٹ
- `AZURE_SEARCH_API_KEY` - Azure AI Search API کلید

تصدیق: نوٹ بکس چلانے سے پہلے `az login` چلائیں (استعمال کرتا ہے `AzureCliCredential`)۔

## ڈویلپمنٹ ورک فلو

### Jupyter نوٹ بکس چلانا

ہر سبق میں مختلف فریم ورکس کے لیے متعدد Jupyter نوٹ بکس شامل ہیں:

1. **Jupyter شروع کریں:**
   ```bash
   jupyter notebook
   ```

2. **سبق ڈائریکٹری میں جائیں** (مثلاً `01-intro-to-ai-agents/code_samples/`)

3. **نوٹ بکس کھولیں اور چلائیں:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) استعمال کرتے ہوئے
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) استعمال کرتے ہوئے

### Microsoft Agent Framework کے ساتھ کام کرنا

**Microsoft Agent Framework + Azure AI Foundry:**
- Azure سبسکرپشن درکار ہے
- Agent Service V2 کے لیے `AzureAIProjectAgentProvider` استعمال کرتا ہے (ایجنٹس Foundry پورٹل میں دکھائی دیتے ہیں)
- پیداواری استعمال کے قابل، اندرونی مشاہداتی صلاحیت کے ساتھ
- فائل پیٹرن: `*-python-agent-framework.ipynb`

## ٹیسٹنگ ہدایات

یہ ایک تعلیمی ریپوزیٹری ہے جس میں نمونہ کوڈ ہے، نہ کہ خودکار ٹیسٹس کے ساتھ پروڈکشن کوڈ۔ اپنے سیٹ اپ اور تبدیلیوں کی تصدیق کے لیے:

### دستی ٹیسٹنگ

1. **Python ماحول کی جانچ کریں:**
   ```bash
   python --version  # 3.12 یا اس سے زیادہ ہونا چاہیے
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **نوٹ بک کے نفاذ کی جانچ کریں:**
   ```bash
   # نوٹ بک کو اسکرپٹ میں تبدیل کریں اور چلائیں (درآمدات کی جانچ)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ماحول کے متغیرات کی توثیق کریں:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### انفرادی نوٹ بکس چلانا

Jupyter میں نوٹ بکس کھولیں اور خلیوں کو تسلسل سے چلائیں۔ ہر نوٹ بک خود مختار ہے اور شامل کرتی ہے:
- امپورٹ اسٹیٹمنٹس
- کنفیگریشن لوڈ کرنا
- مثال ایجنٹ امپلیمنٹیشنز
- مارک ڈاؤن خلیات میں متوقع آؤٹ پٹس

## کوڈ اسٹائل

### Python کنونشنز

- **Python ورژن**: 3.12+
- **کوڈ اسٹائل**: معیاری Python PEP 8 کنونشنز کی پیروی کریں
- **نوٹ بکس**: تصورات کی وضاحت کے لیے واضح مارک ڈاؤن خلیات استعمال کریں
- **Imports**: اسٹینڈرڈ لائبریری، تھرڈ پارٹی، لوکل امپورٹس کے حساب سے گروپ کریں

### Jupyter نوٹ بک کنونشنز

- کوڈ خلیات سے پہلے وضاحتی مارک ڈاؤن خلیات شامل کریں
- حوالہ کے لیے نوٹ بکس میں آؤٹ پٹ مثالیں شامل کریں
- سبق کے تصورات سے میل کھانے والے واضح ویریبل نام استعمال کریں
- نوٹ بک کے نفاذ کا سلسلہ خطی رکھیں (خانہ 1 → 2 → 3...)

### فائل آرگنائزیشن

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## بلڈ اور ڈیپلائمنٹ

### دستاویزات بنانا

یہ ریپوزیٹری دستاویزات کے لیے Markdown استعمال کرتی ہے:
- ہر سبق کے فولڈر میں README.md فائلیں
- ریپوزیٹری کے روٹ پر مرکزی README.md
- خودکار ترجمہ نظام GitHub Actions کے ذریعے

### CI/CD پائپ لائن

واقع ہے `.github/workflows/` میں:

1. **co-op-translator.yml** - 50+ زبانوں میں خودکار ترجمہ
2. **welcome-issue.yml** - نئے ایشو بنانے والوں کو خوش آمدید کہتا ہے
3. **welcome-pr.yml** - نئے پل ریکویسٹ کنٹریبیوٹرز کو خوش آمدید کہتا ہے

### تعیناتی

یہ ایک تعلیمی ریپوزیٹری ہے - کوئی تعیناتی عمل نہیں۔ صارفین:
1. ریپوزیٹری فورک یا کلون کریں
2. نوٹ بکس لوکل یا GitHub Codespaces میں چلائیں
3. مثالوں میں ترمیم اور تجربہ کر کے سیکھیں

## پل ریکویسٹ رہنما اصول

### جمع کروانے سے پہلے

1. **اپنی تبدیلیوں کا ٹیسٹ کریں:**
   - متاثرہ نوٹ بکس کو مکمل طور پر چلائیں
   - تصدیق کریں کہ تمام خانے بغیر غلطی کے چلتے ہیں
   - چیک کریں کہ آؤٹ پٹس مناسب ہیں

2. **دستاویزات کی اپ ڈیٹس:**
   - اگر نئے تصورات شامل کر رہے ہیں تو README.md اپ ڈیٹ کریں
   - پیچیدہ کوڈ کے لیے نوٹ بکس میں کمنٹس شامل کریں
   - یقینی بنائیں کہ مارک ڈاؤن خلیات مقصد کی وضاحت کرتے ہیں

3. **فائل تبدیلیاں:**
   - `.env` فائلز جمع نہ کریں (استعمال کریں `.env.example`)
   - `venv/` یا `__pycache__/` ڈائریکٹریز جمع نہ کریں
   - جب نوٹ بکس تصورات ظاہر کریں تو ان کے آؤٹ پٹس رکھیں
   - عارضی فائلیں اور بیک اپ نوٹ بکس (`*-backup.ipynb`) ہٹا دیں

### PR عنوان فارمٹ

وضاحتی عنوانات استعمال کریں:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### درکار چیکس

- نوٹ بکس بغیر غلطی کے چلنے چاہئیں
- README فائلیں واضح اور درست ہونی چاہئیں
- ریپوزیٹری میں موجودہ کوڈ پیٹرنز کی پیروی کریں
- دیگر اسباق کے ساتھ مطابقت برقرار رکھیں

## اضافی نوٹس

### عام مسائل

1. **Python ورژن کا عدم مطابقت:**
   - یقینی بنائیں کہ Python 3.12+ استعمال ہو رہا ہے
   - کچھ پیکیجز پرانے ورژنز کے ساتھ کام نہیں کریں گے
   - مخصوص Python ورژن بتانے کے لیے `python3 -m venv` استعمال کریں

2. **ماحول کے متغیرات:**
   - ہمیشہ `.env.example` سے `.env` بنائیں
   - `.env` فائل کو کمیٹ نہ کریں (یہ `.gitignore` میں ہے)
   - GitHub ٹوکن کو مناسب اجازتیں درکار ہیں

3. **پیکیج تنازعات:**
   - تازہ ورچوئل ماحول استعمال کریں
   - انفرادی پیکیجز کی بجائے `requirements.txt` سے انسٹال کریں
   - کچھ نوٹ بکس کو اضافی پیکیجز درکار ہو سکتے ہیں جو ان کے مارک ڈاؤن خلیات میں ذکر ہیں

4. **Azure سروسز:**
   - Azure AI سروسز کے لیے فعال سبسکرپشن درکار ہے
   - کچھ فیچرز مخصوص علاقوں تک محدود ہوتے ہیں
   - GitHub Models کے لیے فری ٹئیر حدود لاگو ہو سکتی ہیں

### سیکھنے کا راستہ

سبقوں کے ذریعے تجویز کردہ ترتیب:
1. **00-course-setup** - ماحول سیٹ اپ کے لیے یہاں شروع کریں
2. **01-intro-to-ai-agents** - AI ایجنٹ کی بنیادی باتیں سمجھیں
3. **02-explore-agentic-frameworks** - مختلف فریم ورکس کے بارے میں جانیں
4. **03-agentic-design-patterns** - بنیادی ڈیزائن پیٹرنز
5. متواتر طور پر نمبر والے اسباق سے آگے بڑھتے رہیں

### فریم ورک کا انتخاب

اپنے مقاصد کی بنیاد پر فریم ورک منتخب کریں:
- **تمام اسباق**: Microsoft Agent Framework (MAF) اور `AzureAIProjectAgentProvider`
- **ایجنٹس سرور-سائیڈ رجسٹر ہوتے ہیں** Azure AI Foundry Agent Service V2 میں اور Foundry پورٹل میں دکھائی دیتے ہیں

### مدد حاصل کرنا

- شامل ہوں [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- مخصوص رہنمائی کے لیے سبق README فائلیں دیکھیں
- کورس کا جائزہ کرنے کے لیے مرکزی [README.md](./README.md) چیک کریں
- تفصیلی سیٹ اپ ہدایات کے لیے [Course Setup](./00-course-setup/README.md) دیکھیں

### تعاون

یہ ایک اوپن تعلیمی پراجیکٹ ہے۔ تعاون خوش آئند ہے:
- کوڈ مثالوں کو بہتر بنائیں
- ٹائپوز یا غلطیوں کو درست کریں
- وضاحتی کمنٹس شامل کریں
- نئے سبق کے موضوعات تجویز کریں
- مزید زبانوں میں ترجمہ کریں

موجودہ ضروریات کے لیے دیکھیں [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues)۔

## پراجیکٹ مخصوص پس منظر

### کثیر لسانی معاونت

یہ ریپوزیٹری خودکار ترجمہ نظام استعمال کرتی ہے:
- 50+ زبانیں معاونت یافتہ
- ترجمے `/translations/<lang-code>/` ڈائریکٹریز میں
- GitHub Actions ورک فلو ترجمہ اپڈیٹس کو ہینڈل کرتا ہے
- ماخذ فائلیں انگریزی میں ریپوزیٹری روٹ پر دستیاب ہیں

### سبق کی ساخت

ہر سبق ایک مستقل پیٹرن کی پیروی کرتا ہے:
1. ویڈیو تھمبنل کے ساتھ لنک
2. تحریری سبق کا مواد (README.md)
3. متعدد فریم ورکس میں کوڈ نمونے
4. سیکھنے کے مقاصد اور قبل از شرطات
5. اضافی تعلیمی وسائل کے لنکس

### کوڈ سیمپل کا نام رکھنے کا انداز

فارمیٹ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - سبق 1، MAF Python
- `14-sequential.ipynb` - سبق 14، MAF اعلیٰ درجے کے پیٹرنز

### خاص ڈائریکٹریز

- `translated_images/` - ترجمہ شدہ تصاویر کے لیے مقامی فولڈر
- `images/` - انگریزی مواد کے لیے اصل تصاویر
- `.devcontainer/` - VS Code ڈویلپمنٹ کنٹینر کنفیگریشن
- `.github/` - GitHub Actions ورک فلو اور ٹیمپلیٹس

### Dependencies

`requirements.txt` سے اہم پیکیجز:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent پروٹوکول سپورٹ
- `azure-ai-inference`, `azure-ai-projects` - Azure AI سروسز
- `azure-identity` - Azure تصدیق (AzureCliCredential)
- `azure-search-documents` - Azure AI Search انضمام
- `mcp[cli]` - Model Context Protocol سپورٹ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
دستبرداری:
اس دستاویز کا ترجمہ AI ترجمہ سروس Co-op Translator (https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہِ کرم نوٹ کریں کہ خودکار تراجم میں غلطیاں یا عدم مطابقت ہو سکتی ہیں۔ اصل دستاویز، اپنی مادری زبان میں، مستند ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمے کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کے لیے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->