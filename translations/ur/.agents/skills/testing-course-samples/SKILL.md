---
name: testing-course-samples
---
# کورس کے نمونوں کی جانچ

اس بات کی تصدیق کریں کہ سبق کے نوٹ بکس اور کوڈ کے نمونے کسی زندہ
Microsoft Foundry / Azure OpenAI سیٹ اپ کے خلاف چلتے ہیں۔ ریپو میں ایک رنر شامل ہے
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) جو
ہر پائتھن نوٹ بک کو بغیر ہیڈ کے چلتا ہے اور PASS/FAIL میٹرکس پرنٹ کرتا ہے۔

## کب استعمال کریں
- "اپنی Azure سبسکرپشن کے خلاف تمام نوٹ بکس / نمونوں کی تصدیق کریں۔"
- "پیکجز کو اپ گریڈ کرنے یا ماڈلز کو تبدیل کرنے کے بعد کورس کا سمُوک ٹیسٹ کریں۔"
- "کون سے سبق ابھی زندہ چلتے ہوئے پاس یا فیل ہو رہے ہیں؟"

اسے AI Smoke Test GitHub ایکشن کے لیے **استعمال نہ کریں** (جو *تعینات* کردہ
ہوسٹ کیے ہوئے ایجنٹس کی تصدیق کرتا ہے — ملاحظہ کریں [`tests/README.md`](../../../tests/README.md))۔ یہ اسکل
نوٹ بکس کو مقامی طور پر چلاتا ہے۔

## لازمی تقاضے (پہلے چیک کریں)
1. **Python 3.12+** کورس کی dependencies کے ساتھ: `python -m pip install -r requirements.txt`
   اور ایکزیکیوٹر: `python -m pip install nbconvert ipykernel`.
2. **ریپو کی جڑ میں `.env`** (ناک کاپی سے [`.env.example`](../../../../../.env.example)) کم از کم درج ذیل کے ساتھ:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry پروجیکٹ اینڈپوائنٹ
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — ایک غیر منسوخ ڈپلائمنٹ (مثلاً `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) اور `AZURE_OPENAI_DEPLOYMENT`
     ان اسباق کے لیے جو Azure OpenAI کو براہِ راست کال کرتے ہیں (سبق 06، 02-azure-openai، 14 ہینڈ آف/ہیومن لوپ)۔
3. **`az login`** مکمل کیا ہوا — نمونے `AzureCliCredential` کے ساتھ مستند ہوتے ہیں (Entra ID، کی لیس)۔
4. ماڈل ڈپلائمنٹ کی موجودگی کی تصدیق کریں:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## تصدیق چلانا
```powershell
# تمام پائتھن نوٹ بکس (.NET، .venv، site-packages، ترجمے، مہارت اثاثے چھوڑ دیے گئے ہیں)
pwsh scripts/validate-notebooks.ps1

# ایک واحد سبق، ہر سیل کے لیے زیادہ طویل وقت معطلی کے ساتھ
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# صرف دکھائیں کہ کیا چلایا جائے گا (کوئی عمل درآمد نہیں)
pwsh scripts/validate-notebooks.ps1 -List

# واضح مترجم (اگر `python` PATH میں نہیں ہے، مثلاً ونڈوز اسٹور عرفی نام)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
سکرپٹ چلائی ہوئی کاپیاں، فی نوٹ بک کی لاگ فائلیں، اور `results.json` میں لکھتا ہے
`$env:TEMP\aiab-nbval` پر اور ناکامیوں کی تعداد کے ساتھ خارج ہو جاتا ہے۔

عارضی ناکامیاں (مشترکہ سبسکرپشن HTTP 429 ریٹ لمٹس، کبھی کبھار
`AzureCliCredential` ٹوکن میں خرابی، یا ٹائم آؤٹ) خود بخود دوبارہ کوشش کی جاتی ہیں
(`-Retries`، ڈیفالٹ 2، `-RetryDelaySeconds` تاخیر کے ساتھ، ڈیفالٹ 20)۔ اگر
ماڈل ڈپلائمنٹ باقاعدگی سے 429 دکھا رہی ہو، تو سبسکرپشن کے GlobalStandard
TPM کوٹا چیک کریں (`az cognitiveservices usage list -l <region>`) — ایک واحد
ڈپلائمنٹ کی صلاحیت بڑھانا اس وقت مدد نہیں کرتا جب *سبسکرپشن* کوٹا ختم ہو چکا ہو۔

## نتائج کی تشریح
- `PASS` — نوٹ بک بغیر کسی سیل کی خرابی کے مکمل طور پر چل گئی۔
- `FAIL` — پہلی `*Error` / `*Exception` لائن دکھائی گئی؛ مکمل ٹریس بیک کے لیے
  متعلقہ `log_*.txt` کو آؤٹ پٹ ڈائرکٹری میں کھولیں۔
- ایک نوٹ بک کی ناکامی `-Timeout` (فی سیل) سے محدود ہوتی ہے، اس لیے اگر
  ہیومن-ان-دی-لوپ سیل ہینگ ہو جائے تو وہ `StdinNotImplementedError` کے طور پر ظاہر ہوتا ہے بجائے اس کے کہ ہینگ ہو۔

## ایسے اسباق جنہیں اضافی وسائل کی ضرورت ہوتی ہے (ان کے بغیر ناکام ہونے کی توقع)
| سبق | اضافی ضرورت |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, کی) — ایک ان میموری بیک اپ راستہ بھی موجود ہے |
| 11 MCP / GitHub | GitHub MCP سرور + PAT |
| 13 memory (cognee) | `cognee` ایک ماڈل فراہم کنندہ کے ساتھ ترتیب دیا گیا ہے |
| 15 browser-use | Playwright براؤزر انسٹال کیے گئے (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry لوکل رن ٹائم + ایک ڈاؤن لوڈ شدہ Qwen ماڈل (ڈیوائس پر، کوئی کلاؤڈ نہیں) |
| `*-dotnet-*` نوٹ بکس | .NET Interactive کرنل (ڈیفالٹ میں مستثنیٰ؛ استعمال کریں `-IncludeDotnet`) |

## رپورٹنگ واپس
سبق کے حساب سے گروپ کی گئی PASS/FAIL ٹیبل کے طور پر خلاصہ کریں۔ حقیقی ریگریشنز
(کوڈ/کنفیگریشن کی خرابیوں کی اصلاح کے لیے) ماحول کے خلاؤں (مفقود سرچ/Foundry لوکل/PAT)
سے الگ کریں، اور ہر حقیقی ناکامی کے لیے `log_*.txt` کو حوالہ دیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->