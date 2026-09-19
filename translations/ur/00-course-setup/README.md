# کورس کی تیاری

## تعارف

یہ سبق آپ کو اس کورس کے کوڈ نمونوں کو چلانے کا طریقہ بتائے گا۔

## دوسرے سیکھنے والوں سے شامل ہوں اور مدد حاصل کریں

اپنے ذخیرہ کو کلون کرنے سے پہلے، [AI Agents For Beginners Discord چینل](https://aka.ms/ai-agents/discord) میں شامل ہوں تاکہ سیٹ اپ میں مدد، کورس کے بارے میں کوئی سوالات، یا دوسرے سیکھنے والوں سے رابطہ حاصل کر سکیں۔

## اس ریپو کو کلون کریں یا فورک کریں

شروع کرنے کے لیے، براہ کرم GitHub ریپوزیٹری کو کلون یا فورک کریں۔ اس سے آپ کو اپنی ایک ورژن ملے گی تاکہ آپ کوڈ کو چلا سکیں، ٹیسٹ کر سکیں اور اس میں ترمیم کر سکیں!

یہ کام <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ریپو کی فورک کرنے</a> کے لنک پر کلک کرکے کیا جا سکتا ہے۔

اب آپ کے پاس اس کورس کی اپنی فورک کی ہوئی ورژن مندرجہ ذیل لنک پر ہے:

![Forked Repo](../../../translated_images/ur/forked-repo.33f27ca1901baa6a.webp)

### شالو کلون (ورکشاپ / کوڈ اسپیسز کے لیے تجویز کردہ)

  >جب آپ پورا تاریخچہ اور تمام فائلیں ڈاؤن لوڈ کرتے ہیں تو مکمل ذخیرہ بڑا (~3 جی بی) ہو سکتا ہے۔ اگر آپ صرف ورکشاپ میں شامل ہو رہے ہیں یا صرف کچھ اسباق کے فولڈرز درکار ہیں، تو شالو کلون (یا سپارس کلون) بہت کم ڈاؤن لوڈ کرتا ہے۔

#### جلدی شالو کلون — کم تاریخچہ، تمام فائلیں

نیچے دی گئی کمانڈز میں `<your-username>` کو اپنی فورک URL (یا اگر پسند کریں تو اپ اسٹریم URL) سے بدلیں۔

صرف تازہ ترین کمیٹ تاریخچہ کلون کرنے کے لیے (چھوٹا ڈاؤن لوڈ):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

مخصوص برانچ کلون کرنے کے لیے:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### جزوی (سپارس) کلون — کم بلیبز + صرف منتخب فولڈرز

یہ جزوی کلون اور سپارس چیک آؤٹ استعمال کرتا ہے (Git 2.25+ اور جدید Git جو جزوی کلون سپورٹ کرتا ہے تجویز کیا جاتا ہے):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ریپو فولڈر میں جائیں:

```bash
cd ai-agents-for-beginners
```

پھر بیان کریں کہ آپ کون سے فولڈرز چاہتے ہیں (نیچے کی مثال میں دو فولڈرز دکھائے گئے ہیں):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

کلون کرنے اور فائلز کی تصدیق کے بعد، اگر آپ کو صرف فائلز کی ضرورت ہے اور آپ جگہ خالی کرنا چاہتے ہیں (کوئی git تاریخچہ نہیں)، تو براہ کرم ریپو میٹا ڈیٹا حذف کریں (💀 ناقابل واپسی — آپ تمام Git فنکشنالٹی کھو دیں گے):

```bash
# زی ایس ایچ/بی اے ایس ایچ
rm -rf .git
```

```powershell
# پاور شیل
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces کا استعمال (مقامی بڑے ڈاؤن لوڈ سے بچنے کے لیے تجویز کردہ)

- اس ریپو کے لیے [GitHub UI](https://github.com/codespaces) کے ذریعے نیا Codespace بنائیں۔  

- نئے بنائے گئے codespace کے ٹرمینل میں، اوپر دی گئی شالو/سپارس کلون کمانڈز میں سے کوئی ایک چلائیں تاکہ آپ کو صرف ضروری اسباق کے فولڈرز Codespace ورک اسپیس میں لے آئیں۔
- اختیاری: Codespaces کے اندر کلون کرنے کے بعد، اضافی جگہ خالی کرنے کے لیے .git کو حذف کر دیں (نیچے ہٹانے کی کمانڈز دیکھیں)۔
- نوٹ: اگر آپ ریپو کو سیدھا Codespaces میں کھولنا چاہتے ہیں (بغیر اضافی کلون کے)، تو ذہن میں رکھیں کہ Codespaces ڈیوسنٹینر ماحول تیار کرے گا اور ممکن ہے آپ کو درکار سے زیادہ فراہم کرے۔

#### مشورے

- ہمیشہ کلون URL کو اپنی فورک سے بدلیں اگر آپ ایڈیٹ/کمیٹ کرنا چاہتے ہیں۔
- اگر بعد میں آپ کو مزید تاریخچہ یا فائلز کی ضرورت ہو، تو آپ انہیں حاصل کر سکتے ہیں یا سپارس چیک آؤٹ کو اضافی فولڈرز شامل کرنے کے لیے ایڈجسٹ کر سکتے ہیں۔

## کوڈ چلانا

یہ کورس آپ کو Jupyter نوٹ بکس کی ایک سیریز پیش کرتا ہے جنہیں آپ چلانے کے ذریعے AI ایجنٹس بنانے کا عملی تجربہ حاصل کر سکتے ہیں۔

کوڈ نمونے **Microsoft Agent Framework (MAF)** استعمال کرتے ہیں جس میں `FoundryChatClient` ہے، جو **Microsoft Foundry Agent Service V2** (Responses API) کے ذریعے **Microsoft Foundry** سے جڑتا ہے۔

تمام Python نوٹ بکس `*-python-agent-framework.ipynb` کے لیبل کے ساتھ ہیں۔

## ضروریات

- Python 3.12+
  - **نوٹ**: اگر آپ کے پاس Python3.12 انسٹال نہیں ہے تو اسے انسٹال کریں۔ پھر اپنی venv بنائیں python3.12 کے ذریعے تاکہ requirements.txt سے درست ورژنز انسٹال ہوں۔
  
    >مثال

    Python venv ڈائریکٹری بنائیں:

    ```bash
    python -m venv venv
    ```

    پھر venv ماحول کو فعال کریں:

    ```bash
    # زی ایس ایچ/بش
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET استعمال کرنے والے نمونوں کے لیے، یقینی بنائیں کہ آپ نے [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا بعد کا ورژن انسٹال کیا ہے۔ پھر، انسٹال شدہ .NET SDK ورژن چیک کریں:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — تصدیق کے لیے لازمی۔ اسے یہاں سے انسٹال کریں: [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure سبسکرپشن** — Microsoft Foundry اور Microsoft Foundry Agent Service تک رسائی کے لیے۔
- **Microsoft Foundry پروجیکٹ** — ایک پروجیکٹ جس میں ایک تعین شدہ ماڈل ہے (مثلاً `gpt-5-mini`)۔ دیکھیں: [Step 1](#مرحلہ-1-microsoft-foundry-پروجیکٹ-بنائیں) نیچے۔

ہم نے اس ریپو کی جڑ میں `requirements.txt` فائل شامل کی ہے جس میں کوڈ نمونوں کو چلانے کے لیے تمام ضروری Python پیکجز شامل ہیں۔

آپ انہیں درج ذیل کمانڈ چلا کر انسٹال کر سکتے ہیں:

```bash
pip install -r requirements.txt
```

ہم تجویز کرتے ہیں کہ Python ورچوئل ماحول بنائیں تاکہ کسی قسم کے تصادم اور مسائل سے بچا جا سکے۔

## VSCode سیٹ اپ کریں

یقینی بنائیں کہ آپ VSCode میں صحیح Python ورژن استعمال کر رہے ہیں۔

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry اور Microsoft Foundry Agent Service ترتیب دیں

### مرحلہ 1: Microsoft Foundry پروجیکٹ بنائیں

آپ کو Microsoft Foundry کا **ہب** اور **پروجیکٹ** چاہیے جس میں ایک تعین شدہ ماڈل موجود ہو تاکہ نوٹ بکس چلائیں۔

1. [ai.azure.com](https://ai.azure.com) جائیں اور اپنے Azure اکاؤنٹ سے سائن ان کریں۔
2. ایک **ہب** بنائیں (یا موجودہ ہب استعمال کریں)۔ دیکھیں: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)۔
3. ہب کے اندر ایک **پروجیکٹ** بنائیں۔
4. **Models + Endpoints** → **Deploy model** سے ایک ماڈل (مثلاً `gpt-5-mini`) تعینات کریں۔

### مرحلہ 2: اپنے پروجیکٹ کا اینڈ پوائنٹ اور ماڈل تعیناتی نام حاصل کریں

Microsoft Foundry پورٹل میں اپنے پروجیکٹ سے:

- **Project Endpoint** — **Overview** صفحے پر جائیں اور اینڈ پوائنٹ URL کاپی کریں۔

![Project Connection String](../../../translated_images/ur/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** میں جائیں، اپنے تعین شدہ ماڈل کو منتخب کریں، اور **Deployment name** نوٹ کریں (مثلاً `gpt-5-mini`)۔

### مرحلہ 3: `az login` کے ذریعے Azure میں سائن ان کریں

زیادہ تر نوٹ بکس آپ کے **Azure CLI سائن ان** کے ذریعے محفوظ طریقے سے تصدیق کرتے ہیں — `AzureCliCredential` یا `DefaultAzureCredential` استعمال کرتے ہوئے (دونوں آپ کے `az login` سیشن کو پکڑتے ہیں) جو `azure-identity` پیکیج سے آتا ہے — اس لئے انہیں API کیز کی ضرورت نہیں ہوتی۔ چند اسباق اور اختیاری انٹیگریشنز میں API کیز استعمال ہوتی ہیں؛ ہر سبق کی شرائط میں چیک کریں۔ اس کے لیے آپ کو Azure CLI سے لاگ ان ہونا ضروری ہے۔

1. اگر پہلے انسٹال نہیں کیا تو **Azure CLI انسٹال کریں**: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **سائن ان کریں** چلانے سے:

    ```bash
    az login
    ```

    یا اگر آپ ریموٹ/کوڈسپیس ماحول میں ہیں جہاں براؤزر نہیں ہے:

    ```bash
    az login --use-device-code
    ```

3. اگر پوچھا جائے تو **اپنی سبسکرپشن منتخب کریں** — وہ سبسکرپشن منتخب کریں جس میں آپ کا Foundry پروجیکٹ ہے۔

4. تصدیق کریں کہ آپ سائن ان ہیں:

    ```bash
    az account show
    ```

> **کیوں `az login`؟** نوٹ بکس `AzureCliCredential` (یا `DefaultAzureCredential`) کے ذریعے تصدیق کرتے ہیں جو Azure CLI کے سائن ان سیشن کو استعمال کرتا ہے، اس لیے آپ کی `.env` فائل میں کوئی API کیز یا سیکریٹس نہیں ہوتے۔ یہ ایک [محفوظ ترین طریقہ کار](https://learn.microsoft.com/azure/developer/ai/keyless-connections) ہے۔

### مرحلہ 4: اپنی `.env` فائل بنائیں

مثال کی فائل کو کاپی کریں:

```bash
# زی ش / باش
cp .env.example .env
```

```powershell
# پاور شیل
Copy-Item .env.example .env
```

`.env` کھولیں اور یہ دو اقدار پر کریں:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| متغیر | کہاں سے حاصل کریں |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry پورٹل → اپنا پروجیکٹ → **Overview** صفحہ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry پورٹل → **Models + Endpoints** → اپنے تعین شدہ ماڈل کا نام |

زیادہ تر اسباق کے لیے بس اتنا کافی ہے! نوٹ بکس خود بخود آپ کے `az login` سیشن کے ذریعے تصدیق کریں گے۔

### مرحلہ 5: Python انحصارات انسٹال کریں

```bash
pip install -r requirements.txt
```

ہم تجویز کرتے ہیں کہ یہ کمانڈ اس ورچوئل ماحول کے اندر چلائیں جو آپ نے پہلے بنایا تھا۔

## اختیاری سیٹ اپ: Azure AI Search (سبق 5 اور 16)

سبق 5 (Agentic RAG) اور سبق 16 کی نوٹ بکس باہمی میموری علم کی بنیاد کے ساتھ چلتیں ہیں — اضافی Azure وسائل کی ضرورت نہیں۔ اگر آپ انہیں حقیقی **Azure AI Search** انڈیکس کے ساتھ پشت پناہی دینا چاہتے ہیں، تو نوٹ کریں کہ **سبق 16 کی نوٹ بک اس وقت صرف کلیدی تصدیق استعمال کرتی ہے**: جب **دونوں** `AZURE_SEARCH_SERVICE_ENDPOINT` اور `AZURE_SEARCH_API_KEY` سیٹ ہوں، تب ہی یہ حقیقی انڈیکس پر شفٹ کرتی ہے ورنہ میموری سرچ پر رہتی ہے — لہذا اسے حقیقی انڈیکس کے ساتھ چلانے کے لیے ایڈمن کلید بھی سیٹ کرنا ضروری ہے۔ Microsoft Entra ID (RBAC) کی کلید سے پاک تصدیق آپ کے پروڈکشن کوڈ کے لیے تجویز کردہ طریقہ ہے، جو اس کورس میں کہیں بھی استعمال ہونے والے `az login` فلو کے مطابق ہے۔

ذیل کے RBAC اقدامات سیٹ اپ گائیڈ نمونوں اور آپ کے اپنے کوڈ پر لاگو ہوتے ہیں۔ یہ سبق 16 کی نوٹ بک میں کلید سے پاک تصدیق کو فعال نہیں کرتے؛ سبق 16 اب بھی Azure AI Search کے لیے اینڈ پوائنٹ اور ایڈمن کلید دونوں کی ضرورت ہے۔

1. اپنے سرچ سروس پر **رول پر مبنی رسائی** فعال کریں:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. اپنے آپ کو مطلوبہ رولز سونپیں (انڈیکسز بنانا/لوڈ کرنا اور سوالات کرنا):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. اپنے `.env` فائل میں اینڈ پوائنٹ شامل کریں:

| متغیر | کہاں سے حاصل کریں |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure پورٹل → آپ کے **Azure AI Search** وسائل → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | سبق 16 کی نوٹ بک میں Azure AI Search کو فعال کرنے کے لیے ضروری (اینڈ پوائنٹ کے ساتھ)، جو کلید پر مبنی تصدیق استعمال کرتا ہے۔ Azure پورٹل → **Settings** → **Keys** → بنیادی ایڈمن کلید |

> **کیوں بغیر کلید؟** ایڈمن کیز آپ کے سرچ سروس کو مکمل لکھنے کی اجازت دیتی ہیں اور `.env` فائلز کے ذریعے لیک ہو سکتی ہیں۔ RBAC کے ساتھ، آپ کی `az login` شناخت استعمال ہوتی ہے — وہی کلید سے پاک Entra ID پیٹرن جو کورس نوٹ بکس استعمال کرتے ہیں (مزید تفصیلات کے لیے دیکھیں: [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac))۔

مکمل انڈیکس بنانے کے نمونوں کے لیے [Azure AI Search سیٹ اپ گائیڈ](./AzureSearch.md) دیکھیں (Python اور .NET)۔

## مزید سیٹ اپ ان اسباق کے لیے جو براہ راست Azure OpenAI کو کال کرتے ہیں (سبق 6 اور 8)

سبق 6 اور 8 کی کچھ نوٹ بکس براہ راست **Azure OpenAI** کو کال کرتی ہیں (جو **Responses API** استعمال کرتی ہے) بجائے Microsoft Foundry پروجیکٹ کے۔ یہ نمونے پہلے GitHub Models استعمال کرتے تھے، جو اب مسترد ہو چکا ہے اور Responses API کی حمایت نہیں کرتا۔ اپنے `.env` فائل میں یہ متغیرات شامل کریں:

| متغیر | کہاں سے حاصل کریں |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure پورٹل → آپ کا **Azure OpenAI** وسائل → **Keys and Endpoint** → اینڈ پوائنٹ (مثلاً `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | آپ کے تعین شدہ ماڈل کا نام (مثلاً `gpt-5-mini`) جو Responses API کو سپورٹ کرتا ہو |
| `AZURE_OPENAI_API_KEY` | اختیاری — صرف اگر آپ کلید کی بنیاد پر تصدیق استعمال کر رہے ہیں `az login` / Entra ID کی بجائے |

> Responses API مستحکم `/openai/v1/` اینڈ پوائنٹ استعمال کرتا ہے، اس لیے `api-version` کی ضرورت نہیں۔ کلید سے پاک Entra ID تصدیق کے لیے `az login` کے ذریعے سائن ان کریں۔

## متبادل فراہم کنندہ: MiniMax (OpenAI-مطابق)

[MiniMax](https://platform.minimaxi.com/) بڑے کانٹیکسٹ ماڈلز (204K ٹوکن تک) OpenAI-مطابق API کے ذریعے فراہم کرتا ہے۔ چونکہ Microsoft Agent Framework کا `OpenAIChatClient` کسی بھی OpenAI-مطابق اینڈ پوائنٹ کے ساتھ کام کرتا ہے، آپ MiniMax کو ان اسباق کے لیے بآسانی متبادل کے طور پر استعمال کر سکتے ہیں جو `OpenAIChatClient` استعمال کرتے ہیں۔

اپنے `.env` فائل میں یہ متغیرات شامل کریں:

| متغیر | کہاں سے حاصل کریں |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | استعمال کریں `https://api.minimax.io/v1` (ڈیفالٹ ویلیو) |
| `MINIMAX_MODEL_ID` | ماڈل نام استعمال کرنے کے لیے (مثلاً `MiniMax-M3`) |

**مثال ماڈلز**: `MiniMax-M3` (تجویز کردہ), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (تیز رفتار جوابات)۔ ماڈل نام اور دستیابی وقت کے ساتھ تبدیل ہو سکتی ہے، اور کسی خاص ماڈل تک رسائی آپ کے اکاؤنٹ پر منحصر ہو سکتی ہے۔

جو کوڈ نمونے `OpenAIChatClient` استعمال کرتے ہیں (مثلاً سبق 14 ہوٹل بکنگ ورک فلو) وہ خود بخود آپ کی MiniMax کنفیگریشن کو پہچان کر استعمال کریں گے جب `MINIMAX_API_KEY` سیٹ ہو۔


## متبادل فراہم کنندہ: Novita AI (OpenAI-مطابقت رکھنے والا)

[Novita AI](https://novita.ai/llm-api) اوپن سورس اور جدید LLMs (DeepSeek, Llama, Qwen، اور مزید) کے لیے ایک OpenAI-مطابقت رکھنے والا API فراہم کرتا ہے۔ چونکہ Microsoft Agent Framework کا `OpenAIChatClient` کسی بھی OpenAI-مطابقت رکھنے والے اینڈپوائنٹ کے ساتھ کام کرتا ہے، آپ Novita AI کو Azure OpenAI یا OpenAI کے متبادل کے طور پر استعمال کر سکتے ہیں۔

اپنے `.env` فائل میں یہ متغیرات شامل کریں:

| متغیر | کہاں سے حاصل کریں |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | `https://api.novita.ai/openai/v1` استعمال کریں (معمول کے مطابق) |
| `NOVITA_MODEL_ID` | استعمال کرنے کے لیے ماڈل کا نام (مثلاً `moonshotai/kimi-k3`) |

**مثال کے طور پر ماڈلز**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`۔ Novita AI متعدد دیگر اوپن سورس ماڈل فیملیز (Llama, Qwen, GLM، اور دیگر) بھی ہوسٹ کرتا ہے — تازہ ترین دستیاب ماڈلز اور ان کے ماڈل IDs کے لیے [Novita AI ماڈل لائبریری](https://novita.ai/llm-api) دیکھیں۔

موجودہ نمونے خودکار طریقے سے `NOVITA_*` متغیرات کا استعمال نہیں کرتے۔ Novita AI استعمال کرنے کے لیے، ان قدروں کو واضح طور پر `OpenAIChatClient` بنانے کے وقت پاس کریں جس نمونہ کو آپ چلا رہے ہیں۔

## متبادل فراہم کنندہ: Foundry Local (ماڈلز کو ڈیوائس پر چلائیں)

[Foundry Local](https://foundrylocal.ai) ایک ہلکا پھلکا رن ٹائم ہے جو زبان کے ماڈلز کو مکمل طور پر **آپ کے اپنے کمپیوٹر پر** ڈاؤن لوڈ، منظم، اور OpenAI-مطابقت رکھنے والے API کے ذریعے فراہم کرتا ہے — کوئی کلاؤڈ کی ضرورت نہیں۔

چونکہ Microsoft Agent Framework کا `OpenAIChatClient` کسی بھی OpenAI-مطابقت رکھنے والے اینڈپوائنٹ کے ساتھ کام کرتا ہے، Foundry Local Azure OpenAI کا ایک مقامی اور آسانی سے قابل استعمال متبادل ہے۔

**1. Foundry Local انسٹال کریں**

```bash
# ونڈوز
winget install Microsoft.FoundryLocal

# میک او ایس
brew install foundrylocal
```

**2. ایک ماڈل ڈاؤن لوڈ کریں اور چلائیں** (اس سے لوکل سروس بھی شروع ہو جائے گی):

```bash
foundry model list          # دستیاب ماڈلز دیکھیں
foundry model run phi-4-mini
```

**3. Python SDK انسٹال کریں** جو لوکل اینڈپوائنٹ تلاش کرنے کے لیے استعمال ہوتا ہے:

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework کو اپنے لوکل ماڈل پر پوائنٹ کریں:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# ماڈل کو لوکل طور پر ڈاؤن لوڈ کرتا ہے (اگر ضرورت ہو) اور جاری رکھتا ہے، پھر اینڈ پوائنٹ/پورٹ دریافت کرتا ہے۔
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # مثلاً http://localhost:<port>/v1
    api_key=manager.api_key,        # ہمیشہ Foundry Local کے لیے "not-required" ہوتا ہے
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **نوٹ:** Foundry Local ایک OpenAI-مطابقت رکھنے والا **Chat Completions** اینڈپوائنٹ فراہم کرتا ہے۔ اسے لوکل ڈویلپمنٹ اور آف لائن حالات کے لیے استعمال کریں۔ مکمل **Responses API** فیچر سیٹ (ریاستی مکالمے وغیرہ) کے لیے Azure OpenAI یا Microsoft Foundry پروجیکٹ استعمال کریں۔

## سبق 8 کے لیے اضافی سیٹ اپ (Bing Grounding ورک فلو)

سبق 8 میں کنڈیشنل ورک فلو نوٹ بک Microsoft Foundry کے ذریعے **Bing grounding** استعمال کرتی ہے۔ اگر آپ اس نمونے کو چلانے کا ارادہ رکھتے ہیں تو اپنے `.env` فائل میں یہ متغیر شامل کریں:

| متغیر | کہاں سے حاصل کریں |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry پورٹل → آپ کا پروجیکٹ → **Management** → **Connected resources** → آپ کا Bing کنکشن → کنکشن ID کو کاپی کریں |

## مسائل کا حل

### macOS پر SSL سرٹیفکیٹ کی تصدیق کی غلطیاں

اگر آپ macOS پر ہیں اور درج ذیل جیسی غلطی آتی ہے:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

یہ macOS پر Python کا معروف مسئلہ ہے جہاں سسٹم SSL سرٹیفکیٹس خودکار طریقے سے قابل اعتماد نہیں ہوتے۔ درج ذیل حلوں کی ترتیب وار کوشش کریں:

**آپشن 1: Python کا Install Certificates اسکرپٹ چلائیں (تجویز کردہ)**

```bash
# اپنے نصب شدہ پائتھن ورژن (مثلاً، 3.12 یا 3.13) کے ساتھ 3.XX کو تبدیل کریں:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**آپشن 2: اپنے نوٹ بک میں `connection_verify=False` استعمال کریں (صرف GitHub Models نوٹ بکس کے لیے)**

سبق 6 کی نوٹ بک (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) میں پہلے سے ایک تبصرہ شدہ حل شامل ہے۔ سرٹیفکیٹ کی غلطیاں آئیں تو `connection_verify=False` کا تبصرہ ہٹا دیں:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # اگر آپ کو سرٹیفکیٹ کی خرابیوں کا سامنا ہو تو SSL تصدیق کو غیر فعال کریں
)
```

> **⚠️ انتباہ:** SSL تصدیق کو غیر فعال کرنا (`connection_verify=False`) سیکیورٹی کو کم کر دیتا ہے کیونکہ یہ سرٹیفکیٹ کی توثیق کو چھوڑ دیتا ہے۔ اسے صرف عارضی حل کے طور پر ترقیاتی ماحول میں استعمال کریں۔ کبھی بھی پیداوار (production) میں استعمال نہ کریں۔

**آپشن 3: `truststore` انسٹال کریں اور استعمال کریں**

```bash
pip install truststore
```

اس کے بعد اپنے نوٹ بک یا اسکرپٹ کے شروع میں نیٹ ورک کالز کرنے سے پہلے درج ذیل شامل کریں:

```python
import truststore
truststore.inject_into_ssl()
```

## کہیں پھنس گئے ہیں؟

اگر آپ کو اس سیٹ اپ کو چلانے میں کوئی مسئلہ ہو، تو ہمارے <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> میں شامل ہوں یا <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ایک مسئلہ رپورٹ کریں</a>۔

## اگلا سبق

اب آپ اس کورس کے کوڈ کو چلانے کے لیے تیار ہیں۔ AI ایجنٹس کی دنیا کے بارے میں مزید جاننے کے لیے خوش رہیں!

[AI ایجنٹس اور ایجنٹ کے استعمال کے کیسز کا تعارف](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->