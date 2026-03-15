# کورس سیٹ اپ

## تعارف

یہ سبق کورس کے کوڈ نمونوں کو چلانے کا طریقہ کار سکھائے گا۔

## دیگر سیکھنے والوں میں شامل ہوں اور مدد حاصل کریں

اپنا ریپو کلون کرنے سے پہلے، سیٹ اپ میں مدد، کورس کے بارے میں سوالات، یا دیگر سیکھنے والوں سے رابطہ کے لیے [AI Agents For Beginners Discord چینل](https://aka.ms/ai-agents/discord) میں شامل ہوں۔

## اس ریپو کو کلون یا فورک کریں

شروع کرنے کے لیے، براہ کرم GitHub ریپوزیٹری کو کلون یا فورک کریں۔ اس سے آپ کے پاس کورس کے مواد کا اپنا ورژن ہوگا تاکہ آپ کوڈ کو چلا سکیں، ٹیسٹ کر سکیں، اور اس میں ترمیم کر سکیں!

یہ کام <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ریپو کو فورک کرنے</a> کے لنک پر کلک کر کے کیا جا سکتا ہے۔

اب آپ کے پاس اس کورس کا اپنے فورک شدہ ورژن درج ذیل لنک میں موجود ہونا چاہیے:

![Forked Repo](../../../translated_images/ur/forked-repo.33f27ca1901baa6a.webp)

### شالو کلون (ورکشاپ / Codespaces کے لیے تجویز کردہ)

  > جب آپ مکمل ہسٹری اور تمام فائلز ڈاؤن لوڈ کرتے ہیں تو مکمل ریپوزیٹری بڑی ہو سکتی ہے (~3 GB)۔ اگر آپ صرف ورکشاپ میں شرکت کر رہے ہیں یا صرف چند سبق کے فولڈر درکار ہیں، تو شالو کلون (یا اسپارس کلون) زیادہ تر ڈاؤن لوڈ کو روک کر ہسٹری کو کتر دیتا ہے اور/یا بلاگز کو اسکپ کر دیتا ہے۔

#### جلدی شالو کلون — کم سے کم ہسٹری، تمام فائلز

نیچے دیے گئے کمانڈز میں `<your-username>` کو اپنے فورک URL (یا اگر پسند ہو تو اپ اسٹریم URL) سے بدل دیں۔

صرف تازہ ترین کمیٹ ہسٹری کلون کرنے کے لیے (چھوٹا ڈاؤن لوڈ):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

کسی خاص برانچ کو کلون کرنے کے لیے:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### جزوی (اسپارس) کلون — کم سے کم بلاگز + صرف منتخب فولڈرز

اس میں جزوی کلون اور اسپارس چیک آؤٹ استعمال ہوتے ہیں (Git 2.25+ ضروری اور جزوی کلون سپورٹ کے ساتھ جدید Git تجویز کیا جاتا ہے):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ریپو فولڈر میں جائیں:

```bash|powershell
cd ai-agents-for-beginners
```

پھر وہ فولڈرز منتخب کریں جو آپ چاہتے ہیں (نیچے دیے گئے مثال میں دو فولڈرز دکھائے گئے ہیں):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

کلون اور فائلوں کی تصدیق کے بعد، اگر آپ کو صرف فائلیں چاہیے اور آپ جگہ خالی کرنا چاہتے ہیں (کوئی گٹ ہسٹری نہیں)، تو براہ کرم ریپوزیٹری میٹا ڈیٹا حذف کریں (💀 ناقابل واپسی — آپ تمام گٹ فنکشنلٹیز کھو دیں گے: کوئی کمیٹس، پل، پوش یا ہسٹری تک رسائی نہیں)۔

```bash
# زی ش/باش
rm -rf .git
```

```powershell
# پاور شیل
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces کا استعمال (مقامی بڑے ڈاؤن لوڈز سے بچنے کے لیے تجویز کردہ)

- اس ریپو کے لیے [GitHub UI](https://github.com/codespaces) کے ذریعے نیا Codespace بنائیں۔

- نئے بنائے گئے Codespace کے ٹرمینل میں اوپر دیے گئے شالو/اسپارس کلون کمانڈز میں سے کوئی ایک چلائیں تاکہ صرف وہی سبق کے فولڈر Codespace ورک اسپیس میں آئیں جو آپ کو چاہیے۔
- اختیاری: Codespaces میں کلون کرنے کے بعد، فالتو جگہ کی بحالی کے لیے .git حذف کریں (ہٹانے کے کمانڈز اوپر دیکھیں)۔
- نوٹ: اگر آپ ریپو کو براہ راست Codespaces میں کھولنا پسند کرتے ہیں (اضافی کلون کے بغیر)، تو جان لیں کہ Codespaces ڈیولپمنٹ کنٹینر ماحول بنائے گا اور ہو سکتا ہے آپ کو زیادہ وسائل دے۔ تازہ Codespace میں شالو کلون کرنے سے آپ کو ڈسک کے استعمال پر زیادہ کنٹرول ملتا ہے۔

#### تجاویز

- اگر آپ ترمیم/کمیٹ کرنا چاہتے ہیں تو ہمیشہ کلون URL کو اپنے فورک سے بدلیں۔
- اگر آپ کو بعد میں مزید ہسٹری یا فائلز چاہیے، تو آپ انہیں فیچ کر سکتے ہیں یا اسپارس چیک آؤٹ کو ایڈجسٹ کر کے اضافی فولڈرز شامل کر سکتے ہیں۔

## کوڈ چلانا

یہ کورس Jupyter Notebooks کی ایک سیریز پیش کرتا ہے جسے آپ AI ایجنٹس کی ہینڈز آن تجربہ حاصل کرنے کے لیے چلا سکتے ہیں۔

کوڈ نمونے **Microsoft Agent Framework (MAF)** استعمال کرتے ہیں جس میں `AzureAIProjectAgentProvider` شامل ہے، جو **Microsoft Foundry** کے ذریعے **Azure AI Agent Service V2** (Responses API) سے جڑتا ہے۔

تمام Python نوٹ بکس پر `*-python-agent-framework.ipynb` کا لیبل لگا ہوتا ہے۔

## ضروریات

- Python 3.12+
  - **نوٹ**: اگر آپ کے پاس Python3.12 انسٹال نہیں ہے، تو یقینی بنائیں کہ اسے انسٹال کریں۔ پھر `python3.12` استعمال کرتے ہوئے اپنا venv بنائیں تاکہ requirements.txt سے صحیح ورژنز انسٹال ہوں۔

    >مثال

    Python venv ڈائریکٹری بنائیں:

    ```bash|powershell
    python -m venv venv
    ```

    پھر venv ماحول کو فعال کریں:

    ```bash
    # زی شیل/باش
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET استعمال کرنے والے نمونہ کوڈز کے لیے، [dotnet 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا اس کے بعد والا ورژن انسٹال کریں۔ پھر انسٹال شدہ .NET SDK ورژن چیک کریں:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — توثیق کے لیے ضروری۔ [aka.ms/installazurecli](https://aka.ms/installazurecli) سے انسٹال کریں۔
- **Azure Subscription** — Microsoft Foundry اور Azure AI Agent Service تک رسائی کے لیے۔
- **Microsoft Foundry Project** — ایک پرائمشنڈ ماڈل کے ساتھ پروجیکٹ (مثلاً `gpt-4o`)۔ نیچے [Step 1](../../../00-course-setup) میں دیکھیں۔

ہم نے اس ریپوزیٹری کی روٹ میں `requirements.txt` فائل شامل کی ہے جس میں کوڈ نمونے چلانے کے لیے تمام مطلوبہ Python پیکجز موجود ہیں۔

آپ انہیں ریپوزیٹری کے روٹ میں اپنے ٹرمینل میں درج ذیل کمانڈ چلانے سے انسٹال کر سکتے ہیں:

```bash|powershell
pip install -r requirements.txt
```

ہم تجویز کرتے ہیں کہ آپ کسی Python ورچوئل ماحول میں یہ انسٹال کریں تاکہ کسی قسم کے تصادم اور مسائل سے بچا جا سکے۔

## VSCode سیٹ اپ کریں

یقینی بنائیں کہ آپ VSCode میں صحیح Python ورژن استعمال کر رہے ہیں۔

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry اور Azure AI Agent Service سیٹ اپ کریں

### مرحلہ 1: Microsoft Foundry پروجیکٹ بنائیں

نوٹ بکس چلانے کے لیے آپ کو Azure AI Foundry کا **ہب** اور **پروجیکٹ** درکار ہے جس میں ایک ماڈل تعینات ہو۔

1. [ai.azure.com](https://ai.azure.com) پر جائیں اور اپنے Azure اکاؤنٹ سے سائن ان کریں۔
2. ایک **ہب** بنائیں (یا موجودہ استعمال کریں)۔ دیکھیں: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)۔
3. ہب کے اندر ایک **پروجیکٹ** بنائیں۔
4. **Models + Endpoints** → **Deploy model** سے کوئی ماڈل تعینات کریں (مثلاً `gpt-4o`)۔

### مرحلہ 2: اپنے پروجیکٹ اینڈ پوائنٹ اور ماڈل تعیناتی کا نام حاصل کریں

Microsoft Foundry پورٹل میں اپنے پروجیکٹ سے:

- **Project Endpoint** — **Overview** صفحہ پر جائیں اور اینڈ پوائنٹ URL کاپی کریں۔

![Project Connection String](../../../translated_images/ur/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** پر جائیں، اپنا تعینات ماڈل منتخب کریں، اور **Deployment name** نوٹ کریں (مثلاً `gpt-4o`)۔

### مرحلہ 3: Azure میں `az login` کے ذریعے سائن ان کریں

تمام نوٹ بکس توثیق کے لیے **`AzureCliCredential`** استعمال کرتے ہیں — کوئی API کیز مینیج کرنے کی ضرورت نہیں۔ اس کے لیے آپ کو Azure CLI کے ذریعے لاگ ان ہونا ضروری ہے۔

1. اگر آپ کے پاس Azure CLI انسٹال نہیں ہے تو انسٹال کریں: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. درج ذیل کمانڈ چلائیں:

    ```bash|powershell
    az login
    ```

    یا اگر آپ ریموٹ/Codespace ماحول میں ہیں جہاں براؤزر نہیں ہے:

    ```bash|powershell
    az login --use-device-code
    ```

3. اگر پوچھا جائے تو اپنی سبسکرپشن منتخب کریں — وہ جس میں آپ کا Foundry پروجیکٹ ہو۔

4. تصدیق کریں کہ آپ سائن ان ہیں:

    ```bash|powershell
    az account show
    ```

> **`az login` کیوں؟** نوٹ بکس `azure-identity` پیکج سے `AzureCliCredential` استعمال کرتے ہوئے توثیق کرتے ہیں۔ اس کا مطلب ہے کہ آپ کے Azure CLI سیشن کی اسناد فراہم کرتا ہے — آپ کی `.env` فائل میں کوئی API کیز یا سیکریٹس نہیں ہوتے۔ یہ ایک [بہترین سیکورٹی طریقہ کار](https://learn.microsoft.com/azure/developer/ai/keyless-connections) ہے۔

### مرحلہ 4: اپنی `.env` فائل بنائیں

مثال فائل کو کاپی کریں:

```bash
# زی شیل/بش
cp .env.example .env
```

```powershell
# پاور شیل
Copy-Item .env.example .env
```

`.env` کھولیں اور ان دو اقدار کو پُر کریں:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| ویری ایبل | کہاں سے حاصل کریں |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry پورٹل → آپ کا پروجیکٹ → **Overview** صفحہ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry پورٹل → **Models + Endpoints** → آپ کے تعینات ماڈل کا نام |

زیادہ تر اسباق کے لیے بس یہی کافی ہے! نوٹ بکس خود بخود آپ کے `az login` سیشن کے ذریعہ توثیق کریں گے۔

### مرحلہ 5: Python Dependencies انسٹال کریں

```bash|powershell
pip install -r requirements.txt
```

ہم تجویز کرتے ہیں کہ آپ اسے اسی ورچوئل ماحول میں چلائیں جو آپ نے پہلے بنایا تھا۔

## اسباق 5 (Agentic RAG) کے لیے اضافی سیٹ اپ

سبق 5 retrieval-augmented generation کے لیے **Azure AI Search** استعمال کرتا ہے۔ اگر آپ اس سبق کو چلانے کا ارادہ رکھتے ہیں، تو اپنی `.env` فائل میں یہ ویری ایبلز شامل کریں:

| ویری ایبل | کہاں سے حاصل کریں |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure پورٹل → آپ کا **Azure AI Search** ریسورس → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure پورٹل → آپ کا **Azure AI Search** ریسورس → **Settings** → **Keys** → پرائمری ایڈمن کی |

## اسباق 6 اور 8 (GitHub Models) کے لیے اضافی سیٹ اپ

سبق 6 اور 8 کے کچھ نوٹ بکس **GitHub Models** استعمال کرتے ہیں بجائے Azure AI Foundry کے۔ اگر آپ ان نمونوں کو چلانے کا ارادہ رکھتے ہیں، تو اپنی `.env` فائل میں یہ ویری ایبلز شامل کریں:

| ویری ایبل | کہاں سے حاصل کریں |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | `https://models.inference.ai.azure.com` استعمال کریں (ڈیفالٹ ویلو) |
| `GITHUB_MODEL_ID` | ماڈل کا نام جو استعمال کرنا ہے (مثلاً `gpt-4o-mini`) |

## سبق 8 (Bing Grounding ورک فلو) کے لیے اضافی سیٹ اپ

سبق 8 کا conditional ورک فلو نوٹ بک **Bing grounding** Azure AI Foundry کے ذریعے استعمال کرتا ہے۔ اگر آپ اس نمونے کو چلانے کا ارادہ رکھتے ہیں، تو اپنی `.env` فائل میں یہ ویری ایبل شامل کریں:

| ویری ایبل | کہاں سے حاصل کریں |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry پورٹل → آپ کا پروجیکٹ → **Management** → **Connected resources** → آپ کا Bing کنکشن → کنکشن ID کاپی کریں |

## مسئلہ حل کرنا

### macOS پر SSL سرٹیفکیٹ ویریفیکیشن کی غلطیاں

اگر آپ macOS استعمال کر رہے ہیں اور آپ کو درج ذیل قسم کی غلطی آتی ہے:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

یہ Python کا macOS پر ایک معروف مسئلہ ہے جہاں سسٹم کے SSL سرٹیفکیٹس خود بخود قابل اعتماد نہیں ہوتے۔ درج ذیل حل بالترتیب آزمائیں:

**اختیار 1: Python کا Install Certificates اسکرپٹ چلائیں (تجویز کردہ)**

```bash
# اپنے نصب شدہ پائتھن ورژن کے ساتھ 3.XX کو تبدیل کریں (جیسے، 3.12 یا 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**اختیار 2: `connection_verify=False` استعمال کریں (صرف GitHub Models نوٹ بکس کے لیے)**

سبق 6 کے نوٹ بک (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) میں ایک تبصرہ شدہ متبادل حل پہلے سے شامل ہے۔ کلائنٹ بناتے وقت `connection_verify=False` کو انکمنٹ کریں:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # اگر آپ سرٹیفیکیٹ کی غلطیوں کا سامنا کرتے ہیں تو SSL کی تصدیق کو غیر فعال کریں
)
```

> **⚠️ خبردار:** SSL ویریفیکیشن کو غیر فعال کرنا (`connection_verify=False`) سیکیورٹی کم کر دیتا ہے کیونکہ سرٹیفکیٹ کی تصدیق چھوڑ دی جاتی ہے۔ اسے صرف ترقیاتی ماحول میں وقتی جائزے کے طور پر استعمال کریں، پیداواری ماحول میں کبھی نہ کریں۔

**اختیار 3: `truststore` انسٹال کریں اور استعمال کریں**

```bash
pip install truststore
```

پھر کسی نیٹ ورک کال سے پہلے اپنی نوٹ بک یا اسکرپٹ کے اوپر یہ شامل کریں:

```python
import truststore
truststore.inject_into_ssl()
```

## کہیں پھنس گئے ہیں؟

اگر آپ کو اس سیٹ اپ کو چلانے میں کوئی مسئلہ ہو، تو ہماری <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> میں شامل ہوں یا <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">مسئلہ رپورٹ کریں</a>۔

## اگلا سبق

آپ اب اس کورس کے لیے کوڈ چلانے کے لیے تیار ہیں۔ AI ایجنٹس کی دنیا کے بارے میں مزید سیکھنے کے لیے خوش رہیں!

[AI Agents اور ایجنٹس کے استعمال کی صورتوں کا تعارف](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**انتباہ:**  
اس دستاویز کا ترجمہ AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجموں میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی مستند ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا بدفہمی کے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->