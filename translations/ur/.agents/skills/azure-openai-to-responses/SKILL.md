---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI Chat Completions سے Responses API کی طرف Python ایپس کی مائیگریشن

> **مستند رہنمائی — عین مطابق کریں**
>
> یہ سکل Python کوڈ بیسز کو Azure OpenAI Chat Completions سے
> Responses API کی متحدہ شکل پر منتقل کرتا ہے۔ ان ہدایات کو بالکل صحیح طریقے سے فالو کریں۔
> پیرامیٹر میپنگز میں خود ساختہ تبدیلی نہ کریں یا API کی شکل بنائیں۔

---

## ٹرگرز

جب صارف چاہتا ہو تو اس قابلیت کو فعال کریں:
- Azure OpenAI Chat Completions سے Responses API کی طرف Python ایپ کی مائیگریشن
- Azure OpenAI کے خلاف Python OpenAI SDK کے استعمال کو جدید API شکل میں اپ گریڈ کریں
- GPT-5 یا نئے ماڈلز کے لیے Python کوڈ تیار کریں جو Azure پر Responses کی ضرورت رکھتے ہوں
- `AzureOpenAI`/`AsyncAzureOpenAI` سے معیار `OpenAI`/`AsyncOpenAI` کلائنٹ کی طرف v1 اینڈپوائنٹ کے ساتھ منتقل ہوں
- `AzureOpenAI` کنسٹرکٹرز یا `api_version` سے متعلق ڈیپریکیشن وارننگز کو ٹھیک کریں

---

## ⚠️ ماڈل مطابقت — پہلے چیک کریں

> **مائیگریٹ کرنے سے پہلے، یقین دہانی کریں کہ آپ کے Azure OpenAI تعیناتی Responses API کو سپورٹ کرتی ہے۔**

### 1. اپنی تعیناتی کا فوری ٹیسٹ کریں (تیز ترین)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **نوٹ**: Azure OpenAI پر `max_output_tokens` کی **کم از کم حد 16** ہوتی ہے۔ 16 سے کم ویلیوز 400 ایرر دیتی ہیں۔ smoke tests کے لیے 50+ استعمال کریں۔

اگر یہ 404 واپس کرے، تو تعیناتی کا ماڈل ابھی Responses سپورٹ نہیں کرتا — نیچے دی گئی حوالہ دیکھیں یا سپورٹڈ ماڈل کے ساتھ دوبارہ تعینات کریں۔

### 2. اپنے ریجن میں دستیاب ماڈلز چیک کریں (تجویز کردہ)

بلٹ اِن ماڈل مطابقتی ٹول چلائیں تاکہ معلوم ہو سکے کہ آپ کے مخصوص ریجن میں Responses API سپورٹ کے ساتھ کون سے ماڈلز دستیاب ہیں:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

یہ Azure ARM لائیو سے پوچھتا ہے اور ایک مطابقت میٹرکس دکھاتا ہے — کون سے ماڈلز Responses، سٹرکچرڈ آؤٹ پٹ، ٹولز وغیرہ سپورٹ کرتے ہیں۔ نتائج کو محدود کرنے کے لیے `--filter gpt-5.1,gpt-5.2` یا اسکرپٹنگ کے لیے `--json` استعمال کریں۔

### 3. مکمل ماڈل سپورٹ ریفرنس

- **لائیو کوئری**: `python migrate.py models` (اوپر دیکھیں — ریجن مخصوص، ہمیشہ اپ ٹو ڈیٹ)
- **دستیابی ملاحظہ کریں**: [ماڈل سمری ٹیبل اور ریجن دستیابی](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **کریئر اسٹارٹ اور رہنمائی**: **https://aka.ms/openai/start**

### ⚠️ پرانے ماڈلز کی حدود

> **خبردار**: پرانے ماڈلز (`gpt-4.1` سے پہلے کے) ممکن ہے کہ Responses API کی تمام خصوصیات کو مکمل طور پر سپورٹ نہ کریں۔
>
> پرانے ماڈلز کے ساتھ جانی پہچانی حدود:
> - **`reasoning` پیرامیٹر**: بہت سے غیر reasoning ماڈلز میں سپورٹ نہیں۔ صرف وہیں `reasoning` مائیگریٹ کریں جہاں یہ اصل کوڈ میں موجود ہو۔
> - **`seed` پیرامیٹر**: Responses API میں بالکل سپورٹ نہیں — تمام درخواستوں سے ہٹا دیں۔
> - **`text.format` کے ذریعہ سٹرکچرڈ آؤٹ پٹ**: پرانے ماڈلز `strict: true` JSON اسکیموں کو معتبر طریقے سے نافذ نہیں کر سکتے۔
> - **ٹول آرکسٹریشن**: GPT-5+ ٹول کالز کو اندرونی reasoning کے طور پر منظم کرتا ہے۔ Responses پر پرانے ماڈلز کام کرتے ہیں لیکن یہ گہری انٹیگریشن نہیں رکھتے۔
> - **درجہ حرارت کی پابندیاں**: `gpt-5` میں مائیگریشن کرتے وقت temperature کو چھوڑنا ہوگا یا 1 پر سیٹ کرنا ہوگا۔ پرانے ماڈلز میں ایسی پابندی نہیں ہے۔

### O-سیریز reasoning ماڈلز (o1, o3-mini, o3, o4-mini)

O-سیریز ماڈلز کے لئے منفرد پیرامیٹر پابندیاں ہیں۔ جب o-سیریز ماڈلز کے لیے ایپس کو مائیگریٹ کریں:

- **`temperature`**: 1 ہونا چاہیے (یا چھوڑا جائے)۔ O-سیریز ماڈلز دیگر ویلیوز قبول نہیں کرتے۔
- **`max_completion_tokens` → `max_output_tokens`**: Azure مخصوص `max_completion_tokens` استعمال کرنے والی ایپس کو `max_output_tokens` پر سوئچ کرنا چاہیے۔ reasoning ٹوکنز کو دھیان میں رکھتے ہوئے زیادہ قدر (4096+) مقرر کریں۔
- **`reasoning_effort`**: اگر ایپ `reasoning_effort` (low/medium/high) استعمال کرتی ہے، اسے رکھیں — Responses API اس پیرامیٹر کو o-سیریز ماڈلز کے لیے سپورٹ کرتا ہے۔
- **اسٹریمنگ کی طبیعت**: O-سیریز ماڈلز متن کے ڈیلٹا ایونٹس کے اجراء سے پہلے reasoning مکمل ہونے تک آؤٹ پٹ بفر کر سکتے ہیں۔ اسٹریمنگ کام کرتی ہے، مگر پہلی `response.output_text.delta` عمرانی GPT ماڈلز کے مقابلے میں زیادہ تاخیر سے آ سکتی ہے۔
- **`top_p`**: O-سیریز پر سپورٹ نہیں — اگر موجود ہو تو ہٹا دیں۔
- **ٹول استعمال**: O-سیریز ماڈلز Responses API کے ذریعے ٹولز کو GPT ماڈلز کی طرح سپورٹ کرتے ہیں، مگر ٹول کال آرکسٹریشن کا معیار ماڈل کے لحاظ سے مختلف ہوتا ہے۔

**عمل — پیشگی ماڈل مشورہ**: اسکین کے دوران چیک کریں کہ ایپ کس ماڈل کو ہدف بناتی ہے (ڈیپلائمنٹ کے نام، env vars، config)۔ اگر ماڈل `gpt-4.1` سے پہلے کا ہے (یعنی gpt-4.1+ نہیں)، صارف کو پیشگی اطلاع دیں:
- مائیگریشن ان کے موجودہ ماڈل پر بنیادی متن، چیٹ، اسٹریمنگ، اور ٹولز کے لیے کام کرے گی۔
- نئے ماڈلز (`gpt-5.1`, `gpt-5.2`) بہتر ٹول آرکسٹریشن، سٹرکچرڈ آؤٹ پٹ نفاذ، reasoning، اور کراس ریجن دستیابی فراہم کرتے ہیں۔
- جب تیار ہوں، اپنی تعیناتی کو اپ گریڈ کرنے پر غور کریں — یہ مائیگریشن میں رکاوٹ نہیں ہے۔

ماڈل ورژن کی بنیاد پر مائیگریشن کو بلاک یا انکار نہ کریں۔ یہ مشورہ معلوماتی ہے۔

### GitHub ماڈلز Responses API کو سپورٹ نہیں کرتے

> **GitHub ماڈلز (`models.github.ai`, `models.inference.ai.azure.com`) Responses API کو سپورٹ نہیں کرتے۔**

اگر کوڈ بیس میں GitHub ماڈلز کا کوڈ راستہ ہو (دیکھیں `base_url` جو `models.github.ai` یا `models.inference.ai.azure.com` کی طرف اشارہ کرتا ہو)، تو مائیگریشن کے دوران اسے **مکمل طور پر ہٹا دیں**۔ Responses API کے لیے Azure OpenAI، OpenAI، یا ہم آہنگ لوکل اینڈپوائنٹ (مثلاً Ollama جس میں Responses سپورٹ ہو) ضروری ہے۔

اسکین کے دوران عمل:
- GitHub ماڈلز کوڈ راستے کو ہٹانے کے لیے نشان زد کریں۔

---

## فریم ورک مائیگریشن

بہت سی ایپس اوپر سے OpenAI کے اعلیٰ سطحی فریم ورک استعمال کرتی ہیں۔ جب انہیں منتقل کریں تو فریم ورک کی اپنی API میں تبدیلی ہوتی ہے — صرف بنیادی OpenAI کالز نہیں۔

### Microsoft Agent Framework (MAF)

**سب سے پہلے اپنی MAF ورژن چیک کریں** — مائیگریشن اس بات پر منحصر ہے کہ آپ MAF 1.0.0+ پر ہیں یا pre-1.0.0 beta/rc پر۔

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **پہلے سے ہی Responses API استعمال کرتا ہے** — مائیگریشن کی ضرورت نہیں۔ اگر کوڈ بیس پرانا `OpenAIChatCompletionClient` استعمال کرتا ہے (جو `chat.completions.create` استعمال کرتا ہے)، اسے `OpenAIChatClient` سے بدلیں۔

| پہلے | بعد |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

اپنی ورژن جاننے کے لیے: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc ریلیز)

pre-1.0.0 MAF میں، `OpenAIChatClient` Chat Completions استعمال کرتا تھا۔ `agent-framework-openai>=1.0.0` میں اپ گریڈ کریں جہاں `OpenAIChatClient` ڈیفالٹ کے طور پر Responses API استعمال کرتا ہے۔

دیگر کوئی تبدیلیاں درکار نہیں — `Agent` اور ٹول APIs ویسے ہی رہیں گے۔

### LangChain (`langchain-openai`)

`ChatOpenAI()` میں `use_responses_api=True` شامل کریں۔ نیز ردعمل تک رسائی `.content` کی بجائے `.text` سے اپ ڈیٹ کریں۔

| پہلے | بعد |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

مکمل پہلے/بعد کے کوڈ کی مثالوں کے لیے دیکھیں [cheat-sheet.md](./references/cheat-sheet.md)۔

---

## فرنٹ اینڈ مائیگریشن رہنمائی

> **Responses API سرور-سائیڈ کا معاملہ ہے۔** اپنے Python بیک اینڈ کو منتقل کریں؛ فرنٹ اینڈ کا HTTP معاہدہ تب تک تبدیل نہ کریں جب تک کہ آپ کا بیک اینڈ صرف ایک پتلا پاس تھرو نہ ہو — ایسی صورت میں، ترجمہ کی تہہ ختم کرنے کے لیے Responses ریکویسٹ شکل اپنانے پر غور کریں۔ اگر فرنٹ اینڈ کلائنٹ-سائیڈ کلید کے ساتھ براہ راست OpenAI کو کال کرتا ہے، تو پہلے وہ کالز بیک اینڈ پر منتقل کریں۔

### `@microsoft/ai-chat-protocol` کا ڈیپریکیشن

`@microsoft/ai-chat-protocol` npm پیکج اب استعمال میں نہیں ہے اور اس کی جگہ [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) لینا چاہیے۔ اگر فرنٹ اینڈ میں ملے:

1. CDN سکرپٹ ٹیگ تبدیل کریں:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` کی انسٹینشی ایشن (`new ChatProtocol.AIChatProtocolClient("/chat")`) ہٹا دیں۔
3. `client.getStreamedCompletion(messages)` کو براہ راست بیک اینڈ اسٹریمنگ اینڈپوائنٹ پر `fetch()` کال سے بدلیں۔
4. `for await (const response of result)` کو `for await (const chunk of readNDJSONStream(response.body))` سے بدلیں۔
5. پراپرٹی ایکسیس کو `response.delta.content` / `response.error` سے `chunk.delta.content` / `chunk.error` میں تبدیل کریں۔

---

## مقاصد

- Azure OpenAI کے خلاف Chat Completions یا پرانے Completions استعمال کرنے والی تمام Python کال سائٹس کی گنتی کریں۔
- Python کوڈ بیس کے لیے مائیگریشن منصوبہ اور ترتیب کی تجویز دیں۔
- Responses API پر منتقل کرنے کے لیے محفوظ اور کم سے کم ترمیمات کریں۔
- Responses آؤٹ پٹ اسکیمہ کو استعمال کرنے کے لیے کالرز کو اپ ڈیٹ کریں؛ بیکورڈیپٹی رپرز نہیں۔
- ٹیسٹ/لِنٹس چلائیں؛ مائیگریشن سے پیدا ہونے والی معمولی خرابیوں کو درست کریں۔
- چھوٹے، قابل جائزہ تبدیلی سیٹ تیار کریں اور حتمی خلاصہ بیانات (diffs) فراہم کریں (commit نہ کریں)۔

---

## گارڈ ریلز

- صرف git ورک اسپیس کے اندر فائلیں تبدیل کریں۔ کبھی باہر نہ لکھیں۔
- پچھلی مطابقت کے لیے shim نہ رکھیں؛ کوڈ کو نئی API شکل میں منتقل کریں۔
- ٹمب اسٹون/ٹرانزیشن تبصرے یا بیک اپ فائلیں نہ چھوڑیں۔
- اگر پہلے اسٹریمنگ استعمال ہو رہی تھی تو اسٹریمنگ کی اصطلاحات برقرار رکھیں؛ ورنہ غیر اسٹریمنگ استعمال کریں۔
- اپروول موڈ میں ہوں تو کمانڈ یا نیٹ ورک کالز چلانے سے پہلے اجازت لیں۔
- `git add`/`git commit`/`git push` نہ چلائیں؛ صرف ورکنگ ٹری ایڈیٹس تیار کریں۔

---

## قدم 0: Azure OpenAI کلائنٹ مائیگریشن (ضروری شرط)

اگر کوڈ بیس `AzureOpenAI` یا `AsyncAzureOpenAI` کنسٹرکٹرز استعمال کرتا ہے، پہلے معیار `OpenAI` / `AsyncOpenAI` کنسٹرکٹرز کی طرف منتقل کریں۔ Azure مخصوص کنسٹرکٹرز `openai>=1.108.1` میں ڈیپریکٹڈ ہیں۔

### v1 API راستہ کیوں؟

نیا `/openai/v1` اینڈپوائنٹ معیار `OpenAI()` کلائنٹ استعمال کرتا ہے بجائے `AzureOpenAI()`، اس میں `api_version` پیرامیٹر کی ضرورت نہیں، اور OpenAI اور Azure OpenAI دونوں پر بالکل ایک جیسا کام کرتا ہے۔ یہی کلائنٹ کوڈ مستقبل میں قابل استعمال ہے — ورژن منیجمنٹ کی ضرورت نہیں۔

### کلیدی تبدیلیاں

| پہلے | بعد |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | مکمل ہٹا دیں |

### صفائی کی چیک لسٹ

- کلائنٹ تعمیر سے `api_version` دلیل نکالیں۔
- `.env`, ایپ سیٹنگز، اور Bicep/انفراسٹرکچر فائلوں سے `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` ماحول متغیرات ہٹائیں۔
- `.env`, ایپ سیٹنگز، Bicep/انفراسٹرکچر، اور ٹیسٹ فکسچرز میں `AZURE_OPENAI_CLIENT_ID` کو `AZURE_CLIENT_ID` میں تبدیل کریں (معیاری Azure شناخت SDK کنونشن)۔
- `requirements.txt` یا `pyproject.toml` میں `openai>=1.108.1` کو یقینی بنائیں۔

### ماحول متغیرات کی مائیگریشن

| پرانا env var | عمل | نوٹس |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **ہٹائیں** | v1 اینڈپوائنٹ کے ساتھ `api_version` کی ضرورت نہیں |
| `AZURE_OPENAI_API_VERSION` | **ہٹائیں** | اوپر جیسا |
| `AZURE_OPENAI_CLIENT_ID` | **نام تبدیل کریں** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` کے لیے معیاری Azure شناخت SDK کنونشن |
| `AZURE_OPENAI_ENDPOINT` | **رکھیں** | ابھی بھی `base_url` تعمیر کے لیے ضروری ہے |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **رکھیں** | `responses.create` میں `model` پیرامیٹر کے طور پر استعمال ہوتا ہے |
| `AZURE_OPENAI_API_KEY` | **رکھیں** | کی بنیاد پر تصدیق کے لیے `api_key` کے طور پر استعمال ہوتا ہے |

کلائنٹ سیٹ اپ کوڈ مثالوں کے لیے (سِنک، ایسِنک، EntraID، API کی، ملٹی ٹیننٹ) دیکھیں [cheat-sheet.md](./references/cheat-sheet.md)۔

---

## قدم 1: پرانے کال سائٹس کا پتہ لگائیں

تمام کال سائٹس کو تلاش کرنے کے لیے [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) اسکرپٹ چلائیں جنہیں مائیگریٹ کرنا ہے:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

یا یہ سرچز دستی طور پر چلائیں — ہر میچ مائیگریشن کا ہدف ہوتا ہے:

```bash
# پرانے API کالز (ضروری دوبارہ لکھیں)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# غیر مستعمل Azure کلائنٹ کنسٹرکٹرز (ضروری تبدیلی کریں)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# ریسپانس شیپ تک رسائی کے طریقے (ضروری اپ ڈیٹ کریں)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# ٹول کی تعریفیں پرانے گھنے انداز میں (ضروری سیدھی کریں)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# ٹول کے نتائج پرانے انداز میں (ضروری function_call_output میں تبدیل کریں)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# غیر مستعمل پیرامیٹرز (ضروری حذف یا نام تبدیل کریں)
rg "response_format"
rg "max_tokens\b"        # زیادہ سے زیادہ آؤٹ پٹ ٹوکنز کے لیے نام تبدیل کریں
rg "['\"]seed['\"]"      # remove entirely

# غیر مستعمل ماحول کی متغیرات (صفائی کریں)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID ہونا چاہیے

# GitHub ماڈلز اینڈپوائنٹس (ضروری حذف کریں — Responses API معاونت یافتہ نہیں)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# فریم ورک سطح کے پرانے انداز (ضروری اپ ڈیٹ کریں)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient سے تبدیلی کریں
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: ضرورت ہے use_responses_api=True

# ٹیسٹ کا ڈھانچہ (ضروری اپ ڈیٹ کریں)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# مواد فلٹر غلطی باڈی تک رسائی (ضروری اپ ڈیٹ — ڈھانچہ تبدیل ہو گیا)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # پرانی واحد شکل — اب content_filter_results (جمع) مواد فلٹرز صف میں

# Chat Completions اینڈپوائنٹ کے لیے خام HTTP کالز (ضروری URL اپ ڈیٹ کریں)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### طریقہ کار (پہچانیں اور دوبارہ لکھیں)

- **Chat Completions کلائنٹ**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure کلائنٹ کنسٹرکٹرز**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **ٹولز**: nested format کے فنکشن کالنگ ٹول ڈیفینیشنز کو (`{"type": "function", "function": {"name": ...}}`) سے flat Responses format میں تبدیل کریں (`{"type": "function", "name": ...}`)؛ `tool_choice` استعمال کریں؛ ٹول کے نتائج کو `{"type": "function_call_output", "call_id": ..., "output": ...}` آئٹمز کے طور پر واپس کریں (نہ کہ `{"role": "tool", ...}`).
- **ٹول راؤنڈ-ٹریپس**: جب ماڈل فنکشن کالز واپس کرے، تو `response.output` آئٹمز کو مکالمے میں شامل کریں (دستی `{"role": "assistant", "tool_calls": [...]}` ڈکشنری نہیں)، پھر ہر نتیجے کے لیے `function_call_output` آئٹمز شامل کریں۔
- **چند-نمونہ ٹول مثالیں**: اگر مکالمے میں ہارڈ کوڈڈ ٹول کال مثالیں شامل ہیں، تو انہیں `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` آئٹمز میں تبدیل کریں۔ IDs لازمی طور پر `fc_` سے شروع ہونی چاہئیں۔
- **`pydantic_function_tool()`**: یہ ہیلپر اب بھی پرانا nested format پیدا کرتا ہے اور `responses.create()` کے ساتھ **مطابقت نہیں رکھتا**۔ دستی ٹول ڈیفینیشنز یا flattening ریپر استعمال کریں۔
- **کئی چکر**: ایپ میں مکالمے کی تاریخ رکھیں؛ پچھلے چکر `input` آئٹمز کے ذریعے پاس کریں۔
- **فارمیٹنگ**: Chat کے top-level `response_format` کو Responses میں `text.format` سے بدلیں۔ canonical شکل: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`۔
- **مواد کے آئٹمز**: Chat `content[].type: "text"` کو Responses کے لیے `content[].type: "input_text"` سے بدلیں جو یوزر/سسٹم کی طرف سے ہو۔
- **تصویری مواد کے آئٹمز**: Chat `content[].type: "image_url"` کو Responses میں `content[].type: "input_image"` سے بدلیں۔ `image_url` فیلڈ nested آبجیکٹ `{"url": "..."}` سے flat سٹرنگ میں تبدیل ہو جاتا ہے۔ پہلے/بعد کی مثالوں کے لیے cheat sheet دیکھیں۔
- **وجہ بتانے کی کوشش**: **صرف اس صورت میں `reasoning` کو منتقل کریں اگر اصل کوڈ میں پہلے سے موجود ہو**۔
- **مواد فلٹر ایرر ہینڈلنگ**: ایرر باڈی کی ساخت بدل گئی ہے۔ Chat Completions `error.body["innererror"]["content_filter_result"]` (واحد) استعمال کرتا تھا؛ Responses API اب `error.body["content_filters"][0]["content_filter_results"]` (جمع، ایک ارے کے اندر) استعمال کرتا ہے۔ جو کوڈ `innererror` تک رسائی کرتا ہے، وہ `KeyError` پھینکے گا۔ اسے نئے راستے کے مطابق دوبارہ تحریر کریں۔
- **خام HTTP کالز**: اگر ایپ Azure OpenAI REST API کو براہ راست (requests، httpx وغیرہ کے ذریعے) `/openai/deployments/{name}/chat/completions?api-version=...` استعمال کرتے ہوئے کال کرتی ہے، تو اسے `/openai/v1/responses` میں تبدیل کریں۔ درخواست باڈی میں تبدیلی: `messages` → `input`، `max_output_tokens` اور `store: false` شامل کریں، `api-version` کوئری پیرامیٹر ہٹا دیں۔ جواب کی باڈی میں تبدیلی: `choices[0].message.content` → `output[0].content[0].text` (نوٹ: `output_text` ایک SDK آسانی اثاثہ ہے جو خام REST JSON میں موجود نہیں)۔

---

## مرحلہ 2: مائیگریشن لاگو کریں

### مائیگریشن کے نوٹس (Chat Completions → Responses)

- **کیوں منتقل کریں**: Responses متن، ٹولز، اور سٹریمِنگ کے لیے متحد API ہے؛ Chat Completions پرانا ہے۔ GPT-5 کے ساتھ، بہترین کارکردگی کے لیے Responses ضروری ہے۔
- **HTTP**: Azure اینڈ پوائنٹ `/openai/deployments/{name}/chat/completions` سے `/openai/v1/responses` میں بدل گیا ہے۔
- **فیلڈز**: `messages` → `input`، `max_tokens` → `max_output_tokens`۔ `temperature` ویسا ہی ہے۔
- **فارمیٹنگ**: `response_format` → ایک مناسب آبجیکٹ کے ساتھ `text.format`۔
- **مواد کے آئٹمز**: Chat `content[].type: "text"` کو Responses میں سسٹم/یوزر کی طرف سے `content[].type: "input_text"` سے بدلیں۔
- **تصویری مواد کے آئٹمز**: Chat `content[].type: "image_url"` کو Responses میں `content[].type: "input_image"` سے بدلیں۔ `image_url` فیلڈ کو `{"image_url": {"url": "..."}}` سے `{"image_url": "..."}` (ایک سادہ سٹرنگ — چاہے HTTPS URL ہو یا `data:image/...;base64,...` ڈیٹا URI) میں فلیٹ کریں۔

### پیرامیٹر میپنگ حوالہ

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (آئٹمز کی ارے) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (آبجیکٹ) |
| `temperature` | `temperature` (بدلاؤ نہیں) |
| `stop` | `stop` (بدلاؤ نہیں) |
| `frequency_penalty` | `frequency_penalty` (بدلاؤ نہیں) |
| `presence_penalty` | `presence_penalty` (بدلاؤ نہیں) |
| `tools` / فنکشن کالنگ | `tools` (بدلاؤ نہیں) |
| `seed` | **ہٹائیں** (معاون نہیں) |
| `store` | `store` (سیٹ کریں `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (فلیٹ سٹرنگ) |

مکمل پہلے/بعد کوڈ کے نمونے کے لیے، [cheat-sheet.md](./references/cheat-sheet.md) دیکھیں۔

ٹیسٹ انفراسٹرکچر کی مائیگریشن (mocks, snapshots, assertions) کے لیے، [test-migration.md](./references/test-migration.md) دیکھیں۔

خرابیوں اور پیچیدگیوں کے حل کے لیے، [troubleshooting.md](./references/troubleshooting.md) دیکھیں۔

---

## ڈیٹا ریٹینشن اور حالت

- تمام Responses درخواستوں پر `store: false` سیٹ کریں۔
- پچھلے میسج IDs یا سرور پر ذخیرہ شدہ سیاق و سباق پر انحصار نہ کریں؛ حالت کو کلائنٹ کے زیر انتظام رکھیں اور میٹا ڈیٹا کو کم سے کم کریں۔

---

## قبولیت کے معیار

### کوڈ-لیول گیٹس (سب کو پاس ہونا ضروری ہے)

- [ ] مائیگریٹڈ فائلوں میں `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` کے لیے صفر میچز۔
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` کے لیے صفر میچز — تمام کنسٹرکٹرز `OpenAI`/`AsyncOpenAI` کے v1 اینڈ پوائنٹ استعمال کرتے ہیں۔
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` کے لیے صفر میچز — GitHub Models کا کوڈ ہٹایا گیا۔
- [ ] `rg "OpenAIChatCompletionClient"` کے لیے صفر میچز — MAF 1.0.0+ کوڈ `OpenAIChatClient` (جو Responses API استعمال کرتا ہے) استعمال کرتا ہے۔ پری 1.0.0 میں، اپ گریڈ کریں `agent-framework-openai>=1.0.0` تک۔
- [ ] تمام `ChatOpenAI(...)` کالز میں `use_responses_api=True` شامل ہے۔
- [ ] `rg "choices\[0\]"` کے لیے صفر میچز — تمام جوابات کی رسائی `resp.output_text` یا Responses کی آؤٹ پٹ اسکیمہ کے ذریعے کی جاتی ہے۔
- [ ] اوپر کی سطح پر `response_format` نہیں؛ تمام ساختہ آؤٹ پٹ `text={"format": {...}}` استعمال کرتا ہے۔
- [ ] `openai>=1.108.1` اور `azure-identity` `requirements.txt` یا `pyproject.toml` میں؛ انحصار کو دوبارہ انسٹال کیا گیا۔
- [ ] ہر `responses.create` کال پر `store=False` سیٹ ہے۔
- [ ] کلائنٹ کنسٹرکشن میں کوئی `api_version` نہیں؛ `AZURE_OPENAI_API_VERSION` کو env فائلز اور انفراسٹرکچر سے ہٹا دیا گیا۔

### ٹیسٹ انفراسٹرکچر کے گیٹس (سب کو پاس ہونا ضروری ہے)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` کے لیے صفر میچز۔
- [ ] `rg "_azure_ad_token_provider" tests/` کے لیے صفر میچز — اسٹیٹمنٹس اپ ڈیٹ ہو چکے ہیں تاکہ `isinstance(client, AsyncOpenAI)` یا `base_url` چیک کریں۔
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` کے لیے صفر میچز — Azure مخصوص فلٹر mocks ہٹا دیے گئے۔
- [ ] mock fixtures میں `kwargs.get("input")` استعمال ہوتا ہے، `kwargs.get("messages")` نہیں۔
- [ ] snapshot / golden فائلیں Responses کے سٹریمینگ شیپ کے مطابق اپ ڈیٹ کی گئی ہیں (کوئی `choices[0]`, `function_call`, `logprobs` وغیرہ نہیں)۔
- [ ] تمام ٹیسٹ اپ ڈیٹس کے بعد `pytest` بغیر کسی ناکامی کے پاس ہو جاتا ہے۔

### برتاؤ کے گیٹس (دستی یا ٹیسٹ ہارنس کے ذریعے تصدیق کریں)

- [ ] **بنیادی تکمیل**: non-streaming `responses.create` غیر خالی `output_text` دیتا ہے۔
- [ ] **سٹریم مماثلت**: اگر اصل کوڈ سٹریم کرتا تھا، تو مائیگریٹڈ کوڈ بھی سٹریم کرتا ہے اور `response.output_text.delta` ایونٹس غیر خالی ڈیلیٹاز کے ساتھ پیدا کرتا ہے۔
- [ ] **ساختہ آؤٹ پٹ**: اگر `text.format` اور `json_schema` استعمال ہو رہا ہے، تو `json.loads(resp.output_text)` کامیاب ہوتا ہے اور اسکیمہ سے میل کھاتا ہے۔
- [ ] **ٹول-کال لوپ**: اگر ٹولز استعمال کیے جائیں، تو ماڈل ٹول کالز جاری کرے، ایپ انہیں چلائے، اور بعد کی درخواست فائنل `output_text` واپس کرے (کوئی لامتناہی لوپ نہیں)۔
- [ ] **Async مماثلت**: اگر `AsyncAzureOpenAI` استعمال ہوا ہو تو، اس کا ہم منصب `AsyncOpenAI` `await` کے ساتھ کام کرے۔
- [ ] **غلطی کی شرح**: مائیگریشن سے پہلے کے بیس لائن کے مقابلے میں کوئی نیا 400/401/404 ایرر نہیں ہے۔

### ڈیلیوریبلز

- خلاصہ میں ترمیم شدہ فائلیں، پرانے/نئے کال سائٹس کی تعداد، اور اگلے اقدامات شامل ہوں۔
- تبدیلیاں صرف ورکنگ ٹری ایڈیٹس ہیں (کوئی کمٹ نہیں)۔

---

## SDK ورژن کی ضروریات

| پیکیج | کم از کم ورژن |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | تازہ ترین (EntraID آتھن کے لیے) |

---

## حوالہ جات

- [Cheat Sheet — تمام کوڈ اسنیپٹس](./references/cheat-sheet.md)
- [Test Migration — mocks, snapshots, assertions](./references/test-migration.md)
- [Troubleshooting — ایررز، رسک ٹیبل، مشکلات](./references/troubleshooting.md)
- [detect_legacy.py — خودکار اسکینر](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API دستاویزات](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API ورژن لائف سائیکل](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API حوالہ](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->