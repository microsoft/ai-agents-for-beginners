---
name: microsoft-docs
---
# مائیکروسافٹ ڈاکس

مائیکروسافٹ ٹیکنالوجی ایکو سسٹم کے لیے تحقیقی مہارت۔ learn.microsoft.com اور اس سے باہر کی دستاویزات کو کور کرتا ہے (VS Code، GitHub، Aspire، Agent Framework ریپوز)۔

---

## ڈیفالٹ: مائیکروسافٹ لرن MCP

**learn.microsoft.com** پر ہر چیز کے لیے یہ ٹولز استعمال کریں — Azure، .NET، M365، Power Platform، Agent Framework، Semantic Kernel، ونڈوز، اور مزید۔ یہ زیادہ تر مائیکروسافٹ دستاویزات کی تلاش کے لیے بنیادی ٹول ہے۔

| ٹول | مقصد |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com پر تلاش کریں — تصورات، گائیڈز، ٹیوٹوریلز، کنفیگریشن |
| `microsoft_code_sample_search` | لرن ڈاکس سے کام کرنے والے کوڈ سنپٹس تلاش کریں۔ بہترین نتائج کے لیے `language` (`python`, `csharp`، وغیرہ) پاس کریں |
| `microsoft_docs_fetch` | مخصوص URL سے مکمل صفحہ کا مواد حاصل کریں (جب سرچ اقتباسات کافی نہ ہوں) |

جب آپ کو مکمل ٹیوٹوریلز، تمام کنفیگریشن آپشنز کی ضرورت ہو یا سرچ اقتباسات کٹ چکے ہوں تو تلاش کے بعد `microsoft_docs_fetch` استعمال کریں۔

---

## مستثنیات: کب دیگر ٹولز استعمال کریں

درج ذیل زمرے **learn.microsoft.com** سے **باہر** ہیں۔ ان کے بجائے مخصوص ٹول استعمال کریں۔

### Aspire — Aspire MCP سرور (ترجیحی) یا Context7 استعمال کریں

Aspire ڈاکس **aspire.dev** پر ہیں، نہ کہ لرن پر۔ بہترین ٹول آپ کے Aspire CLI ورژن پر منحصر ہے:

**CLI 13.2+** (تجویز کردہ) — Aspire MCP سرور میں اندرونی ڈاکس تلاش کے ٹولز شامل ہیں:

| MCP ٹول | وضاحت |
|----------|-------------|
| `list_docs` | aspire.dev سے تمام دستیاب دستاویزات کی فہرست بناتا ہے |
| `search_docs` | aspire.dev مواد پر وزنی لغوی تلاش |
| `get_doc` | خاص دستاویز کو سلاج کے ذریعے حاصل کرتا ہے |

یہ Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)) میں شامل ہیں۔ اپڈیٹ کرنے کے لیے: `aspire update --self --channel daily`۔

**CLI 13.1** — MCP سرور انضمام کی تلاش فراہم کرتا ہے (`list_integrations`, `get_integration_docs`) لیکن **دочных تلاش نہیں**۔ Context7 استعمال کریں:

| لائبریری ID | استعمال کے لیے |
|---|---|
| `/microsoft/aspire.dev` | بنیادی — گائیڈز، انٹیگریشنز، CLI ریفرنس، تعیناتی |
| `/microsoft/aspire` | رن ٹائم سورس — API اندرونی، نفاذ کی تفصیلات |
| `/communitytoolkit/aspire` | کمیونٹی انٹیگریشنز — Go، Java، Node.js، Ollama |

### VS Code — Context7 استعمال کریں

VS Code ڈاکس **code.visualstudio.com** پر ہیں، نہ کہ لرن پر۔

| لائبریری ID | استعمال کے لیے |
|---|---|
| `/websites/code_visualstudio` | صارف ڈاکس — سیٹنگز، فیچرز، ڈیبگنگ، ریموٹ ڈیولپمنٹ |
| `/websites/code_visualstudio_api` | ایکسٹینشن API — ویب ویوز، TreeViews، کمانڈز، کنٹری بیوشن پوائنٹس |

### GitHub — Context7 استعمال کریں

GitHub ڈاکس **docs.github.com** اور **cli.github.com** پر ہیں۔

| لائبریری ID | استعمال کے لیے |
|---|---|
| `/websites/github_en` | ایکشنز، API، ریپوز، سیکیورٹی، ایڈمن، کوپائلٹ |
| `/websites/cli_github` | GitHub CLI (`gh`) کمانڈز اور فلیگز |

### Agent Framework — Learn MCP + Context7 استعمال کریں

Agent Framework ٹیوٹوریلز learn.microsoft.com پر ہیں (`microsoft_docs_search` استعمال کریں)، لیکن **GitHub ریپو** میں API سطح کی تفصیل ہوتی ہے جو اکثر شائع شدہ ڈاکس سے آگے ہوتی ہے — خاص طور پر DevUI REST API ریفرنس، CLI آپشنز، اور .NET انٹیگریشن۔

| لائبریری ID | استعمال کے لیے |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ٹیوٹوریلز — DevUI گائیڈز، ٹریسنگ، ورک فلو آرکسٹریشن |
| `/microsoft/agent-framework` | API تفصیل — DevUI REST اینڈ پوائنٹس، CLI فلیگز، تصدیق، .NET `AddDevUI`/`MapDevUI` |

**DevUI ٹپ:** لرن ویب سائٹ سورس سے ہاؤ ٹو گائیڈز تلاش کریں، پھر API سطح کی تفصیلات (اینڈ پوائنٹ اسکیمز، پراکسی کنفیگ، آتھ ٹوکنز) کے لیے ریپو سورس دیکھیں۔

---

## Context7 سیٹ اپ

کسی بھی Context7 سوال کے لیے پہلے لائبریری ID حل کریں (ہر سیشن میں ایک بار):

1. ٹیکنالوجی کا نام لے کر `mcp_context7_resolve-library-id` کال کریں
2. واپس ملنے والی لائبریری ID اور مخصوص سوال کے ساتھ `mcp_context7_query-docs` کال کریں

---

## موثر سوالات لکھنا

واضح رہیں — ورژن، مقصد، اور زبان شامل کریں:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

سیاق و سباق شامل کریں:
- جب متعلقہ ہو **ورژن** (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **ٹاسک کا مقصد** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- کثیراللسانی ڈاکس کے لیے **زبان** (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->