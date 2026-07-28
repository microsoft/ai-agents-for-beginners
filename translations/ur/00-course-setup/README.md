# کورس کی ترتیب

## تعارف

یہ سبق اس بات کا احاطہ کرے گا کہ اس کورس کے کوڈ نمونے کیسے چلائے جائیں۔

## دوسرے سیکھنے والوں سے جڑیں اور مدد حاصل کریں

اپنی ریپو کو کلون کرنے سے پہلے، کسی بھی سیٹ اپ میں مدد، کورس کے بارے میں کسی بھی سوال کے لیے، یا دوسرے سیکھنے والوں سے جڑنے کے لیے [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) میں شامل ہوں۔

## اس ریپو کو کلون یا فورک کریں

شروع کرنے کے لیے، براہ کرم گٹ ہب ریپوزیٹری کو کلون یا فورک کریں۔ اس سے آپ کے پاس کورس کے مواد کا اپنا ورژن بن جائے گا تاکہ آپ کوڈ کو چلا سکیں، ٹیسٹ کریں، اور تبدیل کریں!

یہ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ریفو کو فورک کرنے</a> کے لنک پر کلک کر کے کیا جا سکتا ہے

اب آپ کے پاس اس کورس کا اپنا فورک شدہ ورژن درج ذیل لنک میں ہونا چاہیے:

![Forked Repo](../../../translated_images/ur/forked-repo.33f27ca1901baa6a.webp)

### شالو کلون (ورکشاپ / کوڈ سپیسز کے لیے تجویز کردہ)

  > پورا ریپوزیٹری بڑا ہو سکتا ہے (~3 جی بی) جب آپ مکمل ہسٹری اور تمام فائلیں ڈاؤن لوڈ کرتے ہیں۔ اگر آپ صرف ورکشاپ میں حصہ لے رہے ہیں یا صرف کچھ اسباق کے فولڈرز کی ضرورت ہے، تو شالو کلون (یا اسپارس کلون) ہسٹری کو کاٹ کر اور/یا بلوبس کو چھوڑ کر زیادہ تر ڈاؤن لوڈ سے بچاتا ہے۔

#### فوری شالو کلون — کم سے کم ہسٹری، تمام فائلیں

نیچے دیے گئے کمانڈز میں `<your-username>` کو اپنے فورک URL (یا اگر ترجیح ہو تو اپ اسٹریم URL) سے تبدیل کریں۔

صرف تازہ ترین کمیٹ ہسٹری کلون کرنے کے لیے (چھوٹا ڈاؤن لوڈ):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

کسی مخصوص برانچ کو کلون کرنے کے لیے:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### جزوی (اسپارس) کلون — کم سے کم بلوبس + صرف منتخب شدہ فولڈرز

یہ جزوی کلون اور اسپارس چیک آؤٹ استعمال کرتا ہے (Git 2.25+ درکار ہے اور اسپارس کلون سپورٹ کے ساتھ جدید Git کی سفارش کی جاتی ہے):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ریپو فولڈر میں جائیں:

```bash|powershell
cd ai-agents-for-beginners
```

پھر ان فولڈرز کی وضاحت کریں جن کی آپ کو ضرورت ہے (نیچے مثال میں دو فولڈرز دکھائے گئے ہیں):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

کلون کرنے اور فائلز کی تصدیق کے بعد، اگر آپ کو صرف فائلز کی ضرورت ہے اور آپ جگہ خالی کرنا چاہتے ہیں (کوئی گٹ ہسٹری نہیں)، تو براہ کرم ریپوزیٹری میٹا ڈیٹا کو حذف کریں (💀 غیر واپسی — آپ تمام گٹ فنکشنلٹی کھو دیں گے: نہ کمیٹس، نہ پل، نہ پش، اور نہ ہی ہسٹری تک رسائی)۔

```bash
# زی ایس ایچ / بی اے ایس ایچ
rm -rf .git
```

```powershell
# پاور شیل
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces کا استعمال (بڑی مقامی ڈاؤن لوڈز سے بچنے کے لیے تجویز کردہ)

- اس ریپو کے لیے [GitHub UI](https://github.com/codespaces) کے ذریعے نیا Codespace بنائیں۔  

- نئے بنائے گئے Codespace کے ٹرمینل میں، اوپر دیے گئے شالو/اسپارس کلون کمانڈز میں سے ایک چلائیں تاکہ صرف آپ کو ضرورت والے لیکچر فولڈرز کو Codespace ورک اسپیس میں لایا جا سکے۔
- اختیاری: Codespaces کے اندر کلون کرنے کے بعد، اضافی جگہ واپس لینے کے لیے .git کو ہٹا دیں (اوپر دیے گئے ہٹانے کے کمانڈز دیکھیں)۔
- نوٹ: اگر آپ ریپو کو براہ راست Codespaces میں (اضافی کلون کے بغیر) کھولنا چاہتے ہیں، تو خیال رکھیں کہ Codespaces ڈیونٹینر ماحول بنائے گا اور شاید آپ کی ضرورت سے زیادہ فراہم کرے گا۔ ایک نیا Codespace میں شالو کلون کرنے سے آپ کو ڈسک کے استعمال پر زیادہ کنٹرول ملتا ہے۔

#### مشورے

- اگر آپ ایڈیٹ یا کمیٹ کرنا چاہتے ہیں تو ہمیشہ کلون URL کو اپنے فورک سے تبدیل کریں۔
- اگر آپ کو بعد میں مزید ہسٹری یا فائلز کی ضرورت ہو، تو آپ انہیں فچ کرسکتے ہیں یا اسپارس چیک آؤٹ کو ایڈجسٹ کر کے اضافی فولڈرز شامل کرسکتے ہیں۔

## کوڈ چلانا

یہ کورس جیوپائٹر نوٹ بکس کی ایک سیریز پیش کرتا ہے جنہیں آپ چلانے کے ذریعے AI ایجنٹس بنانے کا عملی تجربہ حاصل کر سکتے ہیں۔

کوڈ نمونے **Microsoft Agent Framework (MAF)** استعمال کرتے ہیں جس میں `FoundryChatClient` شامل ہے، جو **Microsoft Foundry Agent Service V2** (Responses API) کے ذریعے **Microsoft Foundry** سے جڑتا ہے۔

تمام پائتھن نوٹ بکس کو `*-python-agent-framework.ipynb` کے لیبل سے نشان زد کیا گیا ہے۔

## ضروریات

- پائتھون 3.12+
  - **نوٹ**: اگر آپ کے پاس Python3.12 انسٹال نہیں ہے، تو اسے انسٹال کریں۔ پھر اپنا وینv python3.12 کے ساتھ بنائیں تاکہ requirements.txt فائل سے درست ورژنز انسٹال ہوں۔
  
    >مثال

    پائتھون وینv ڈائریکٹری بنائیں:

    ```bash|powershell
    python -m venv venv
    ```

    پھر وینv ماحول کو فعال کریں:

    ```bash
    # زیش/باش
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET استعمال کرنے والے نمونہ کوڈز کے لیے، یقینی بنائیں کہ آپ نے [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا بعد کا ورژن انسٹال کیا ہوا ہے۔ پھر اپنے انسٹال شدہ .NET SDK کے ورژن کی جانچ کریں:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — توثیق کے لیے ضروری۔ اسے [aka.ms/installazurecli](https://aka.ms/installazurecli) سے انسٹال کریں۔
- **Azure Subscription** — Microsoft Foundry اور Microsoft Foundry Agent Service تک رسائی کے لیے۔
- **Microsoft Foundry Project** — ایک پروجیکٹ جس میں مودل تعینات ہو چکا ہو (مثلاً `gpt-5-mini`)۔ نیچے [Step 1](#قدم-1-microsoft-foundry-پروجیکٹ-بنائیں) دیکھیں۔

ہم نے اس ریپوزیٹری کی روٹ میں `requirements.txt` فائل شامل کی ہے جس میں کوڈ نمونے چلانے کے لیے تمام ضروری پائتھن پیکیجز ہیں۔

آپ انہیں ریپوزیٹری کی روٹ میں اپنے ٹرمینل میں درج ذیل کمانڈ چلانے سے انسٹال کر سکتے ہیں:

```bash|powershell
pip install -r requirements.txt
```

ہم مشورہ دیتے ہیں کہ کسی پائتھن ورچوئل ماحول کو بنائیں تاکہ کسی تصادم اور مسائل سے بچا جا سکے۔

## VSCode کی سیٹ اپ کریں

یقینی بنائیں کہ آپ VSCode میں صحیح پائتھن ورژن استعمال کر رہے ہیں۔

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry اور Microsoft Foundry Agent Service کی ترتیب

### قدم 1: Microsoft Foundry پروجیکٹ بنائیں

نوٹ بکس چلانے کے لیے آپ کو Microsoft Foundry **ہب** اور **پروجیکٹ** کی ضرورت ہے جس میں ایک تعینات شدہ ماڈل ہو۔

1. [ai.azure.com](https://ai.azure.com) پر جائیں اور اپنے Azure اکاؤنٹ سے سائن ان کریں۔
2. ایک **ہب** بنائیں (یا موجودہ ہب استعمال کریں)۔ دیکھیں: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)۔
3. ہب کے اندر ایک **پروجیکٹ** بنائیں۔
4. **Models + Endpoints** → **Deploy model** سے ایک ماڈل تعینات کریں (مثلاً `gpt-5-mini`)۔

### قدم 2: اپنے پروجیکٹ کا اینڈ پوائنٹ اور ماڈل تعیناتی کا نام حاصل کریں

Microsoft Foundry پورٹل میں اپنے پروجیکٹ سے:

- **Project Endpoint** — **Overview** صفحے پر جائیں اور اینڈ پوائنٹ URL کو کاپی کریں۔

![Project Connection String](../../../translated_images/ur/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** میں جائیں، اپنے تعینات شدہ ماڈل کو منتخب کریں اور **Deployment name** نوٹ کریں (مثلاً `gpt-5-mini`)۔

### قدم 3: Azure میں `az login` کے ذریعے سائن ان کریں

تمام نوٹ بکس توثیق کے لیے **`AzureCliCredential`** کا استعمال کرتے ہیں — کوئی API کیز منیج کرنے کی ضرورت نہیں۔ اس کے لیے آپ کا Azure CLI کے ذریعے سائن ان ہونا ضروری ہے۔

1. **Azure CLI انسٹال کریں** اگر آپ نے پہلے نہیں کیا: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **سائن ان** کمانڈ چلائیں:

    ```bash|powershell
    az login
    ```

    یا اگر آپ ریموٹ/Codespace ماحول میں ہیں جہاں براؤزر نہیں ہے:

    ```bash|powershell
    az login --use-device-code
    ```

3. اگر پوچھا جائے تو **اپنا سبسکرپشن منتخب کریں** — وہ جس میں آپ کا Foundry پروجیکٹ ہے۔

4. تصدیق کریں کہ آپ سائن ان ہیں:

    ```bash|powershell
    az account show
    ```

> **کیوں `az login`؟** نوٹ بکس توثیق کے لیے `azure-identity` پیکیج سے `AzureCliCredential` استعمال کرتے ہیں۔ اس کا مطلب ہے کہ آپ کا Azure CLI سیشن آپ کو اسناد فراہم کرتا ہے — آپ کے `.env` فائل میں کوئی API کیز یا سیکریٹس نہیں ہیں۔ یہ ایک [سیکورٹی کی بہترین پریکٹس](https://learn.microsoft.com/azure/developer/ai/keyless-connections) ہے۔

### قدم 4: اپنی `.env` فائل بنائیں

مثال کی فائل کو کاپی کریں:

```bash
# زی ش/باش
cp .env.example .env
```

```powershell
# پاور شیل
Copy-Item .env.example .env
```

`.env` کھولیں اور ان دو اقدار کو پُر کریں:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| متغیر | کہاں ملے گا |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry پورٹل → آپ کا پروجیکٹ → **Overview** صفحہ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry پورٹل → **Models + Endpoints** → آپ کے تعینات شدہ ماڈل کا نام |

زیادہ تر اسباق کے لیے بس اتنا ہے! نوٹ بکس آپ کے `az login` سیشن کے ذریعے خود بخود توثیق کریں گے۔

### قدم 5: پائتھن انحصارات انسٹال کریں

```bash|powershell
pip install -r requirements.txt
```

ہم مشورہ دیتے ہیں کہ یہ آپ نے جو ورچوئل ماحول بنایا ہے اس کے اندر چلائیں۔

## سبق 5 (Agentic RAG) کے لیے اضافی سیٹ اپ

سبق 5 کے لیے **Azure AI Search** استعمال ہوتا ہے جو ریٹریول-آگمینٹڈ جنریشن کے لیے ہے۔ اگر آپ اس سبق کو چلانے کا ارادہ رکھتے ہیں تو اپنی `.env` فائل میں یہ متغیرات شامل کریں:

| متغیر | کہاں ملے گا |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure پورٹل → آپ کا **Azure AI Search** ریسورس → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure پورٹل → آپ کا **Azure AI Search** ریسورس → **Settings** → **Keys** → پرائمری ایڈمن کی |

## اسباق کے لیے اضافی سیٹ اپ جو Azure OpenAI کو براہ راست کال کرتے ہیں (سبق 6 اور 8)

سبق 6 اور 8 کے کچھ نوٹ بکس **Azure OpenAI** کو براہ راست (Responses API) کے ذریعے کال کرتے ہیں بجائے Microsoft Foundry پروجیکٹ کے۔ یہ نمونے پہلے GitHub Models استعمال کرتے تھے، جو ختم ہو چکا ہے (جولائی 2026 کو ریٹائر ہو جائے گا) اور Responses API سپورٹ نہیں کرتا۔ اگر آپ یہ نمونے چلانے کا ارادہ رکھتے ہیں، تو اپنی `.env` فائل میں یہ متغیرات شامل کریں:

| متغیر | کہاں ملے گا |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure پورٹل → آپ کا **Azure OpenAI** ریسورس → **Keys and Endpoint** → اینڈ پوائنٹ (مثلاً `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | آپ کے تعینات شدہ ماڈل کا نام (مثلاً `gpt-5-mini`) جو Responses API کو سپورٹ کرتا ہو |
| `AZURE_OPENAI_API_KEY` | اختیاری — صرف اگر آپ کی-بیسڈ توثیق `az login` / Entra ID کے بجائے استعمال کرتے ہیں |

> Responses API مستحکم `/openai/v1/` اینڈ پوائنٹ استعمال کرتا ہے، اس لیے `api-version` کی ضرورت نہیں۔ کی لیس Entra ID توثیق استعمال کرنے کے لیے `az login` سے سائن ان ہوں۔

## متبادل فراہم کنندہ: MiniMax (OpenAI-مطابق)

[MiniMax](https://platform.minimaxi.com/) بڑے کانٹیکسٹ ماڈلز (تا 204K ٹوکنز) OpenAI-مطابق API کے ذریعے فراہم کرتا ہے۔ چونکہ Microsoft Agent Framework کا `OpenAIChatClient` کسی بھی OpenAI-مطابق اینڈ پوائنٹ کے ساتھ کام کرتا ہے، آپ MiniMax کو Azure OpenAI یا OpenAI کی جگہ استعمال کر سکتے ہیں۔

اپنی `.env` فائل میں یہ متغیرات شامل کریں:

| متغیر | کہاں ملے گا |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → APIkeys |
| `MINIMAX_BASE_URL` | استعمال کریں `https://api.minimax.io/v1` (ڈیفالٹ ویلیو) |
| `MINIMAX_MODEL_ID` | استعمال کرنے کے لیے ماڈل کا نام (مثلاً `MiniMax-M3`) |

**مثال ماڈلز**: `MiniMax-M3` (تجویز کردہ)، `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (تیز تر جوابات)۔ ماڈل کے نام اور دستیابی وقت کے ساتھ تبدیل ہو سکتے ہیں، اور کسی ماڈل تک رسائی آپ کے اکاؤنٹ یا علاقے پر منحصر ہو سکتی ہے — موجودہ فہرست کے لیے [MiniMax Platform](https://platform.minimaxi.com/) دیکھیں۔ اگر آپ کے اکاؤنٹ کو `MiniMax-M3` دستیاب نہیں، تو `MINIMAX_MODEL_ID` کو ایسے ماڈل پر سیٹ کریں جس کی آپ کو رسائی ہو (مثلاً `MiniMax-M2.7`)۔

وہ کوڈ نمونے جو `OpenAIChatClient` استعمال کرتے ہیں (مثلاً سبق 14 ہوٹل بکنگ ورک فلو) خود بخود آپ کی MiniMax کنفیگریشن کو پہچان کر استعمال کریں گے جب `MINIMAX_API_KEY` سیٹ ہو۔

## متبادل فراہم کنندہ: Foundry Local (ماڈلز کو ڈیوائس پر چلائیں)

[Foundry Local](https://foundrylocal.ai) ایک ہلکا پھلکا رن ٹائم ہے جو زبان کے ماڈلز کو مکمل طور پر آپ کے اپنے کمپیوٹر پر ڈاؤن لوڈ، منیج، اور سروس دیتا ہے، OpenAI-مطابق API کے ذریعے — نہ کلاؤڈ، نہ Azure سبسکرپشن، اور نہ API کیز۔ یہ آف لائن ڈیولپمنٹ، بغیر کلاؤڈ لاگت کے تجربہ کرنے، یا ڈیٹا کو اپنے ڈیوائس پر رکھنے کے لیے بہت اچھا آپشن ہے۔

چونکہ Microsoft Agent Framework کا `OpenAIChatClient` کسی بھی OpenAI-مطابق اینڈ پوائنٹ کے ساتھ کام کرتا ہے، Foundry Local Azure OpenAI کا ایک مقامی متبادل ہے۔

**1. Foundry Local انسٹال کریں**

```bash
# ونڈوز
winget install Microsoft.FoundryLocal

# میک او ایس
brew install foundrylocal
```

**2. ماڈل ڈاؤن لوڈ کریں اور چلائیں** (اس سے مقامی سروس بھی شروع ہو جاتی ہے):

```bash
foundry model list          # دستیاب ماڈلز دیکھیں
foundry model run phi-4-mini
```

**3. Python SDK انسٹال کریں** جو مقامی اینڈ پوائنٹ کو دریافت کرنے کے لیے استعمال ہوتی ہے:

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework کو اپنے مقامی ماڈل کی طرف اشارہ کریں:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# ماڈل کو مقامی طور پر ڈاؤن لوڈ کرتا ہے (اگر ضرورت ہو) اور سرو کرتا ہے، پھر اینڈپوائنٹ/پورٹ دریافت کرتا ہے۔
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # مثلاً http://localhost:<port>/v1
    api_key=manager.api_key,        # فاؤنڈری لوکل کے لئے ہمیشہ "ضرورت نہیں"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **نوٹ:** Foundry Local OpenAI-مطابق **Chat Completions** اینڈ پوائنٹ فراہم کرتا ہے۔ اسے مقامی ڈیولپمنٹ اور آف لائن حالات کے لیے استعمال کریں۔ مکمل **Responses API** فیچر سیٹ (ریاستی گفتگو، گہری ٹول آرکسٹریشن، اور ایجنٹ طرز کی ترقی) کے لیے، سبقوں میں دکھائے گئے Azure OpenAI یا Microsoft Foundry پروجیکٹ کو ہدف بنائیں۔ موجودہ ماڈل کیٹلاگ اور پلیٹ فارم سپورٹ کے لیے [Foundry Local documentation](https://foundrylocal.ai) دیکھیں۔

## سبق 8 (Bing Grounding Workflow) کے لیے اضافی سیٹ اپ


سبق 8 میں مشروط ورک فلو نوٹ بک Microsoft Foundry کے ذریعے **Bing grounding** استعمال کرتی ہے۔ اگر آپ اس نمونے کو چلانے کا منصوبہ بنا رہے ہیں، تو اسے آپ کی `.env` فائل میں شامل کریں:

| متغیر | کہاں سے حاصل کریں |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry پورٹل → آپ کا پروجیکٹ → **Management** → **Connected resources** → آپ کا Bing کنکشن → کنکشن ID کی کاپی کریں |

## مسائل کا حل

### macOS پر SSL سرٹیفکیٹ کی تصدیق کی خرابی

اگر آپ macOS پر ہیں اور اس قسم کی خرابی کا سامنا کرتے ہیں:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

یہ macOS پر Python کے ساتھ ایک معروف مسئلہ ہے جہاں سسٹم SSL سرٹیفکیٹس خود بخود قابل اعتماد نہیں سمجھے جاتے۔ درج ذیل حل کو ترتیب سے آزمائیں:

**اختیار 1: Python کی Install Certificates اسکرپٹ چلائیں (تجویز کردہ)**

```bash
# اپنے نصب کردہ پائتھون ورژن کے ساتھ 3.XX کو تبدیل کریں (مثلاً، 3.12 یا 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**اختیار 2: نوٹ بک میں `connection_verify=False` استعمال کریں (صرف GitHub Models نوٹ بکس کے لیے)**

سبق 6 کی نوٹ بک (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) میں ایک تبصرہ شدہ حل پہلے سے شامل ہے۔ کلائنٹ بناتے وقت `connection_verify=False` کا تبصرہ ہٹائیں:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # اگر آپ کو سرٹیفیکیٹ کی غلطیاں پیش آئیں تو SSL تصدیق کو غیر فعال کریں
)
```

> **⚠️ انتباہ:** SSL کی تصدیق کو غیر فعال کرنا (`connection_verify=False`) سرٹیفکیٹ کی تصدیق کو نظر انداز کرکے سکیورٹی کو کم کرتا ہے۔ اسے صرف ترقیاتی ماحول میں عارضی حل کے طور پر استعمال کریں، کبھی پروڈکشن میں نہیں۔

**اختیار 3: `truststore` انسٹال کریں اور استعمال کریں**

```bash
pip install truststore
```

پھر نیٹ ورک کالز کرنے سے پہلے اپنی نوٹ بک یا اسکرپٹ کے اوپر یہ شامل کریں:

```python
import truststore
truststore.inject_into_ssl()
```

## کہیں پھنس گئے ہیں؟

اگر آپ کو اس سیٹ اپ کو چلانے میں کوئی مسئلہ ہو تو ہمارے <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> میں شامل ہوں یا <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">مسئلہ رجسٹر کریں</a>۔

## اگلا سبق

آپ اب اس کورس کے کوڈ کو چلانے کے لیے تیار ہیں۔ AI ایجنٹس کی دنیا کے بارے میں مزید سیکھنے کا مزہ لیں!

[AI ایجنٹس کا تعارف اور ایجنٹ استعمال کی مثالیں](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->