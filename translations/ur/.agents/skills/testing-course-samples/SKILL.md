---
name: testing-course-samples
---
# کورس کے نمونوں کی جانچ

تصدیق کریں کہ اسباق کے نوٹ بکس اور کوڈ کے نمونے ایک فعال
Microsoft Foundry / Azure OpenAI سیٹ اپ کے خلاف چل رہے ہیں۔ ریپو میں ایک رنر شامل ہے
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) جو
ہر پائتھن نوٹ بک کو ہیڈلیس طریقے سے چلاتا ہے اور PASS/FAIL ماتریس پرنٹ کرتا ہے۔

## کب استعمال کریں
- "اپنی Azure سبسکرپشن کے خلاف تمام نوٹ بکس / نمونوں کی تصدیق کریں۔"
- "پیکجز کو اپ گریڈ کرنے یا ماڈلز میں تبدیلی کے بعد کورس کا سمورک ٹیسٹ کریں۔"
- "کون سے سبق اب بھی زندہ چل رہے ہیں یا ناکام ہو رہے ہیں؟"

AI Smoke Test GitHub ایکشن کے لئے اسے **استعمال نہ کریں** (جو *تعینات شدہ*
ہوسٹ کیے گئے ایجنٹس کی تصدیق کرتا ہے — دیکھیں [`tests/README.md`](../../../tests/README.md))۔ یہ مہارت
نوٹ بکس کو مقامی طور پر چلاتی ہے۔

## ضروریات (پہلے چیک کریں)
1. **Python 3.12+** کورس کی dependencies کے ساتھ: `python -m pip install -r requirements.txt`
   اور ایگزیکیوٹر کے لئے: `python -m pip install nbconvert ipykernel`۔
2. رپو کے روٹ پر **`.env`** فائل (نقل کریں [`.env.example`](../../../../../.env.example) سے) جس میں کم از کم شامل ہوں:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry پروجیکٹ اینڈ پوائنٹ
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — ایک غیر متروک تعیناتی (مثلاً `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) اور `AZURE_OPENAI_DEPLOYMENT`
     ان اسباق کے لئے جو براہ راست Azure OpenAI کو کال کرتے ہیں (سبق 06, 02-azure-openai, 14 handoff/human-loop)۔
3. **`az login`** مکمل ہو چکا ہو — نمونے `AzureCliCredential` (Entra ID, keyless) کے ساتھ تصدیق کرتے ہیں۔
4. ماڈل کی تعیناتی موجود ہے یہ تصدیق کریں:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`۔

## تصدیق چلانا
```powershell
# تمام پائتھن نوٹ بکس (.NET، .venv، site-packages، translations، skill assets کو چھوڑ کر)
pwsh scripts/validate-notebooks.ps1

# ایک واحد سبق، ہر سیل کے لیے زیادہ طویل ٹائم آؤٹ کے ساتھ
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# صرف فہرست بنائیں کہ کیا چلے گا (کوئی عملدرآمد نہیں)
pwsh scripts/validate-notebooks.ps1 -List

# واضح مفسر (اگر `python` PATH پر نہیں ہے، مثلاً Windows Store الیاس)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
اسکرپٹ چلائی گئی کاپیاں، فی نوٹ بک لاگز، اور `results.json` کو لکھتا ہے
`$env:TEMP\aiab-nbval` میں اور نقصانات کی تعداد کے ساتھ باہر نکلتا ہے۔

## نتائج کی تشریح
- `PASS` — نوٹ بک بغیر کسی سیل کی غلطی کے مکمل چل گئی۔
- `FAIL` — پہلی `*Error` / `*Exception` لائن دکھائی جاتی ہے؛ مکمل ٹریس بیک کے لیے
  آؤٹ پٹ ڈائریکٹری میں مطابقت رکھنے والا `log_*.txt` کھولیں۔
- ایک نوٹ بک کی ناکامی `-Timeout` (فی سیل) سے محدود ہوتی ہے، لہٰذا رکا ہوا
  human-in-the-loop سیل `StdinNotImplementedError` کے طور پر ظاہر ہوتا ہے بجائے رکے رہنے کے۔

## اسباق جن کو اضافی وسائل کی ضرورت ہے (ان کے بغیر ناکام ہونے کی توقع ہے)
| سبق | اضافی ضرورت |
|--------|-------------------|
| 05 Agentic RAG | Azure AI سرچ (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — ایک ان میموری بیک اپ راستہ موجود ہے |
| 11 MCP / GitHub | GitHub MCP سرور + PAT |
| 13 میموری (cognee) | `cognee` ماڈل فراہم کنندہ کے ساتھ ترتیب دیا گیا |
| 15 browser-use | Playwright براؤزرز انسٹال کیے گئے (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local رن ٹائم + ڈاؤن لوڈ شدہ Qwen ماڈل (آلے پر، بغیر کلاؤڈ) |
| `*-dotnet-*` نوٹ بکس | .NET Interactive کرنل (ڈیفالٹ میں شامل نہیں؛ استعمال کریں `-IncludeDotnet`) |

## رپورٹنگ
سبق کے مطابق گروپ بندی کی گئی PASS/FAIL ٹیبل کے طور پر خلاصہ کریں۔ حقیقی ریگریشنز
(کوڈ/کنفیگریشن کی خرابیوں کی درستگی) کو ماحول کے خلا (مثلاً Search/Foundry Local/PAT کی کمی) سے الگ کریں،
اور ہر حقیقی ناکامی کے لیے ناکام `log_*.txt` کا حوالہ دیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->