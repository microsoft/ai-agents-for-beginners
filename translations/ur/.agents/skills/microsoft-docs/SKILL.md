---
name: microsoft-docs
description: سرکاری Microsoft دستاویزات میں استفسار کریں تاکہ Azure، .NET، Agent Framework،
  Aspire، VS Code، GitHub، اور دیگر میں موجود تصورات، ٹیوٹوریلز، اور کوڈ کی مثالیں
  تلاش کی جا سکیں۔ ڈیفالٹ کے طور پر Microsoft Learn MCP استعمال کیا جاتا ہے، جبکہ
  learn.microsoft.com کے باہر موجود مواد کے لیے Context7 اور Aspire MCP استعمال ہوتے
  ہیں۔
---
# Microsoft Docs

مائیکروسوفٹ ٹیکنالوجی ایکوسسٹم کے لیے تحقیقاتی مہارت۔ learn.microsoft.com اور وہ دستاویزات جو اس کے باہر موجود ہیں (VS Code، GitHub، Aspire، Agent Framework ریپوز) کو شامل کرتا ہے۔

---

## Default: Microsoft Learn MCP

ان ٹولز کو **learn.microsoft.com پر موجود سب کچھ** کے لیے استعمال کریں — Azure، .NET، M365، Power Platform، Agent Framework، Semantic Kernel، Windows، اور مزید۔ یہ مائیکروسوفٹ دستاویزات کے وسیع اکثریتی سوالات کے لیے بنیادی ٹول ہے۔

| ٹول | مقصد |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com میں تلاش کریں — تصورات، رہنما، ٹیوٹوریلز، ترتیب |
| `microsoft_code_sample_search` | Learn دستاویزات سے کام کرنے والے کوڈ نمونے تلاش کریں۔ بہترین نتائج کے لیے `language` (`python`, `csharp`, وغیرہ) فراہم کریں |
| `microsoft_docs_fetch` | کسی مخصوص URL سے مکمل صفحے کا مواد حاصل کریں (جب تلاش کے اقتباسات کافی نہ ہوں) |

جب آپ کو مکمل ٹیوٹوریلز، تمام ترتیب کے اختیارات، یا جب تلاش کے اقتباسات مختصر ہوں تو تلاش کے بعد `microsoft_docs_fetch` استعمال کریں۔

---

## Exceptions: When to Use Other Tools

مندرجہ ذیل زمرے learn.microsoft.com کے باہر موجود ہیں۔ اس کی بجائے مخصوص ٹول استعمال کریں۔

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire کی دستاویزات **aspire.dev** پر ہیں، Learn پر نہیں۔ بہترین ٹول آپ کے Aspire CLI ورژن پر منحصر ہے:

**CLI 13.2+** (recommended) — The Aspire MCP server includes built-in docs search tools:

| MCP ٹول | تفصیل |
|----------|-------------|
| `list_docs` | aspire.dev سے دستیاب تمام دستاویزات کی فہرست بناتا ہے |
| `search_docs` | aspire.dev مواد میں وزن شدہ لِیگزیکل تلاش |
| `get_doc` | slug کے ذریعے مخصوص دستاویز حاصل کرتا ہے |

یہ Aspire CLI 13.2 میں شامل ہیں ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). اپڈیٹ کرنے کے لیے: `aspire update --self --channel daily`. حوالہ: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP سرور انٹیگریشن تلاش فراہم کرتا ہے (`list_integrations`, `get_integration_docs`) مگر ڈاکس سرچ فراہم نہیں کرتا۔ Context7 پر واپس جائیں:

| لائبریری ID | استعمال کے لیے |
|---|---|
| `/microsoft/aspire.dev` | پرائمری — رہنما، انٹیگریشنز، CLI حوالہ، ڈیپلائمنٹ |
| `/dotnet/aspire` | رن ٹائم ماخذ — API اندرونی اجزا، نفاذ کی تفصیلات |
| `/communitytoolkit/aspire` | کمیونٹی انٹیگریشنز — Go، Java، Node.js، Ollama |

### VS Code — Use Context7

VS Code کی دستاویزات **code.visualstudio.com** پر ہیں، Learn پر نہیں۔

| لائبریری ID | استعمال کے لیے |
|---|---|
| `/websites/code_visualstudio` | یوزر دستاویزات — سیٹنگز، خصوصیات، ڈیبگنگ، ریموٹ ڈیولپمنٹ |
| `/websites/code_visualstudio_api` | ایکسٹینشن API — webviews، TreeViews، کمانڈز، کنٹریبیوشن پوائنٹس |

### GitHub — Use Context7

GitHub کی دستاویزات **docs.github.com** اور **cli.github.com** پر ہیں۔

| لائبریری ID | استعمال کے لیے |
|---|---|
| `/websites/github_en` | Actions، API، ریپوز، سیکیورٹی، ایڈمن، Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) کمانڈز اور فلیگز |

### Agent Framework — Use Learn MCP + Context7

Agent Framework کے ٹیوٹوریلز learn.microsoft.com پر ہیں (استعمال کریں `microsoft_docs_search`)، مگر **GitHub repo** میں اکثر شائع شدہ ڈاکس سے آگے API سطح کی تفصیل ہوتی ہے — خاص طور پر DevUI REST API حوالہ، CLI اختیارات، اور .NET انٹیگریشن۔

| لائبریری ID | استعمال کے لیے |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ٹیوٹوریلز — DevUI رہنما، ٹریسنگ، ورک فلو آرکسٹراشن |
| `/microsoft/agent-framework` | API تفصیل — DevUI REST اینڈ پوائنٹس، CLI فلیگز، auth، .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** How-to گائیڈز کے لیے Learn ویب سائٹ سورس کو کوئری کریں، پھر API سطح کی مخصوصیات (endpoint اسکیمیں، proxy ترتیب، auth ٹوکنز) کے لیے repo سورس دیکھیں۔

---

## Context7 Setup

کسی بھی Context7 سوال کے لیے، پہلے لائبریری ID کو حل کریں (سیشن میں ایک بار):

1. ٹیکنالوجی کے نام کے ساتھ `mcp_context7_resolve-library-id` کال کریں
2. واپسی کردہ لائبریری ID اور مخصوص سوال کے ساتھ `mcp_context7_query-docs` کال کریں

---

## Writing Effective Queries

مخصوص رہیں — ورژن، مقصد، اور زبان شامل کریں:

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
- **ورژن** جب متعلقہ ہو (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **کام کا مقصد** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **زبان** کثیر لسانی ڈاکس کے لیے (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
استثنیٰ:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لئے کوشاں ہیں، براہِ کرم نوٹ کریں کہ خودکار تراجم میں غلطیاں یا عدمِ درستگی ہو سکتی ہے۔ اصل دستاویز کو اس کی مادری زبان میں معتبر ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کے لیے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->