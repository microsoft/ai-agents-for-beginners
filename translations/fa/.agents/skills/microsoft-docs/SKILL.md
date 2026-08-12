---
name: microsoft-docs
description: پرس‌وجو در مستندات رسمی مایکروسافت برای یافتن مفاهیم، آموزش‌ها و مثال‌های
  کد در حوزه‌های Azure، .NET، Agent Framework، Aspire، VS Code، GitHub و موارد دیگر.
  از Microsoft Learn MCP به‌عنوان پیش‌فرض استفاده می‌کند، و برای محتوایی که خارج از
  learn.microsoft.com قرار دارد از Context7 و Aspire MCP استفاده می‌کند.
---
# مستندات مایکروسافت

مهارت تحقیق برای اکوسیستم فناوری مایکروسافت. پوشش‌دهنده learn.microsoft.com و مستنداتی که خارج از آن قرار دارند (VS Code، GitHub، Aspire، مخازن Agent Framework).

---

## پیش‌فرض: Microsoft Learn MCP

از این ابزارها برای **همه چیز روی learn.microsoft.com** استفاده کنید — Azure، .NET، M365، Power Platform، Agent Framework، Semantic Kernel، Windows و غیره. این ابزار اصلی برای اکثریت قریب به اتفاق پرسش‌های مربوط به مستندات مایکروسافت است.

| ابزار | هدف |
|------|---------|
| `microsoft_docs_search` | جستجو در learn.microsoft.com — مفاهیم، راهنماها، آموزش‌ها، پیکربندی |
| `microsoft_code_sample_search` | پیدا کردن قطعات کد عملی از مستندات Learn. برای بهترین نتیجه مقدار `language` (`python`, `csharp`, و غیره) را مشخص کنید |
| `microsoft_docs_fetch` | دریافت محتوای کامل صفحه از یک URL مشخص (وقتی که قطعات نتیجه جستجو کافی نیستند) |

پس از جستجو از `microsoft_docs_fetch` استفاده کنید وقتی به آموزش‌های کامل، تمام گزینه‌های پیکربندی، یا وقتی که قطعات نتیجه جستجو کوتاه شده‌اند نیاز دارید.

---

## استثنائات: چه زمانی از ابزارهای دیگر استفاده کنیم

دسته‌های زیر در **خارج از** learn.microsoft.com قرار دارند. به‌جای آن از ابزار مشخص‌شده استفاده کنید.

### .NET Aspire — از Aspire MCP Server (ترجیحی) یا Context7 استفاده کنید

مستندات Aspire در **aspire.dev** قرار دارند، نه Learn. بهترین ابزار به نسخه Aspire CLI شما بستگی دارد:

**CLI 13.2+** (توصیه‌شده) — سرور Aspire MCP شامل ابزارهای جستجوی مستندات داخلی است:

| ابزار MCP | توضیحات |
|----------|-------------|
| `list_docs` | فهرست تمام مستندات موجود از aspire.dev |
| `search_docs` | جستجوی واژگانی وزن‌دار در میان محتوای aspire.dev |
| `get_doc` | بازیابی یک سند مشخص با slug |

این‌ها در Aspire CLI 13.2 عرضه می‌شوند ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). برای به‌روزرسانی: `aspire update --self --channel daily`. مرجع: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — سرور MCP جستجوی یکپارچه‌سازی را فراهم می‌کند (`list_integrations`, `get_integration_docs`) اما **جستجوی مستندات** را فراهم نمی‌کند. به Context7 بازگردید:

| Library ID | استفاده برای |
|---|---|
| `/microsoft/aspire.dev` | اصلی — راهنماها، یکپارچگی‌ها، مرجع CLI، استقرار |
| `/dotnet/aspire` | منبع زمان اجرا — اجزای داخلی API، جزئیات پیاده‌سازی |
| `/communitytoolkit/aspire` | یکپارچگی‌های جامعه — Go، Java، Node.js، Ollama |

### VS Code — از Context7 استفاده کنید

مستندات VS Code در **code.visualstudio.com** قرار دارند، نه Learn.

| Library ID | استفاده برای |
|---|---|
| `/websites/code_visualstudio` | مستندات کاربری — تنظیمات، قابلیت‌ها، اشکال‌زدایی، توسعه راه دور |
| `/websites/code_visualstudio_api` | Extension API — webviews، TreeViews، دستورات، نقاط مشارکت |

### GitHub — از Context7 استفاده کنید

مستندات GitHub در **docs.github.com** و **cli.github.com** قرار دارند.

| Library ID | استفاده برای |
|---|---|
| `/websites/github_en` | Actions، API، مخازن، امنیت، مدیریت، Copilot |
| `/websites/cli_github` | دستورات و فلگ‌های GitHub CLI (`gh`) |

### Agent Framework — از Learn MCP + Context7 استفاده کنید

آموزش‌های Agent Framework در learn.microsoft.com قرار دارند (از `microsoft_docs_search` استفاده کنید)، اما **مخزن GitHub** دارای جزئیات سطح API است که اغلب جلوتر از مستندات منتشرشده است — به‌ویژه مرجع REST API DevUI، گزینه‌های CLI و یکپارچگی .NET.

| Library ID | استفاده برای |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | آموزش‌ها — راهنماهای DevUI، ردیابی، ارکستراسیون جریان کاری |
| `/microsoft/agent-framework` | جزئیات API — نقاط پایانی REST DevUI، فلگ‌های CLI، احراز هویت، .NET `AddDevUI`/`MapDevUI` |

**نکته DevUI:** ابتدا منبع سایت Learn را برای راهنماهای نحوه انجام کار بررسی کنید، سپس منبع مخزن را برای جزئیات سطح API (شِماهای نقاط پایانی، پیکربندی پروکسی، توکن‌های احراز هویت) بررسی کنید.

---

## راه‌اندازی Context7

برای هر پرس‌وجوی Context7، ابتدا شناسه کتابخانه را حل کنید (یک‌بار در هر جلسه):

1. فراخوانی `mcp_context7_resolve-library-id` با نام فناوری
2. فراخوانی `mcp_context7_query-docs` با شناسه کتابخانه بازگردانده‌شده و یک پرس‌وجوی خاص

---

## نوشتن پرس‌وجوهای مؤثر

مشخص باشید — نسخه، هدف و زبان را وارد کنید:

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

زمینه را وارد کنید:
- **نسخه** زمانی که مرتبط است (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **هدف کار** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **زبان** برای مستندات چندزبانه (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
سلب مسئولیت:
این سند با استفاده از سرویس ترجمهٔ هوش مصنوعی Co‑op Translator (https://github.com/Azure/co-op-translator) ترجمه شده است. اگرچه ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نادرستی‌هایی باشند. نسخهٔ اصلی سند به زبان اصلی آن باید به‌عنوان مرجع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمهٔ انسانی حرفه‌ای توصیه می‌شود. ما در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->