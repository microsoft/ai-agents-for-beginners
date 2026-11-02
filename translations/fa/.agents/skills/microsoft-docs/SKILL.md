---
name: microsoft-docs
---
# مستندات مایکروسافت

مهارت تحقیق در اکوسیستم فناوری مایکروسافت. شامل learn.microsoft.com و مستنداتی که خارج از آن زندگی می‌کنند (VS Code، GitHub، Aspire، مخازن Agent Framework).

---

## پیش‌فرض: Microsoft Learn MCP

از این ابزارها برای **همه چیز در learn.microsoft.com** استفاده کنید — Azure، .NET، M365، Power Platform، Agent Framework، Semantic Kernel، ویندوز و موارد بیشتر. این ابزار اصلی برای بیشتر پرس‌وجوهای مستندات مایکروسافت است.

| ابزار | هدف |
|------|---------|
| `microsoft_docs_search` | جستجوی learn.microsoft.com — مفاهیم، راهنماها، آموزش‌ها، پیکربندی |
| `microsoft_code_sample_search` | یافتن قطعات کد کاری از مستندات Learn. بهترین نتیجه با ارسال `language` (`python`، `csharp`، و غیره) |
| `microsoft_docs_fetch` | دریافت محتوای کامل صفحه از یک URL خاص (وقتی که گزیده‌های جستجو کافی نیست) |

پس از جستجو از `microsoft_docs_fetch` استفاده کنید وقتی نیاز به آموزش‌های کامل، همه گزینه‌های پیکربندی، یا وقتی گزیده‌های جستجو کوتاه شده‌اند دارید.

---

## استثناها: چه زمانی از ابزارهای دیگر استفاده کنیم

دسته‌های زیر **خارج از** learn.microsoft.com قرار دارند. به جای آن از ابزار مشخص شده استفاده کنید.

### Aspire — استفاده از Aspire MCP Server (ترجیحی) یا Context7

مستندات Aspire در **aspire.dev** است، نه Learn. بهترین ابزار به نسخه Aspire CLI شما بستگی دارد:

**CLI 13.2 به بالا** (توصیه شده) — سرور Aspire MCP شامل ابزارهای جستجوی مستندات داخلی است:

| ابزار MCP | توضیحات |
|----------|-------------|
| `list_docs` | فهرست تمام مستندات موجود در aspire.dev |
| `search_docs` | جستجوی وزنی لغوی در محتوای aspire.dev |
| `get_doc` | بازیابی سند خاص توسط slug |

این‌ها در Aspire CLI 13.2 عرضه شده‌اند ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). برای به‌روزرسانی: `aspire update --self --channel daily`.

**CLI 13.1** — سرور MCP جستجوی مستندات ندارد اما جستجوی ادغام (`list_integrations`، `get_integration_docs`) را ارائه می‌دهد. در این صورت به Context7 رجوع کنید:

| شناسه کتابخانه | استفاده برای |
|---|---|
| `/microsoft/aspire.dev` | اصلی — راهنماها، ادغام‌ها، مرجع CLI، استقرار |
| `/microsoft/aspire` | منبع زمان اجرا — جزئیات API، پیاده‌سازی |
| `/communitytoolkit/aspire` | ادغام‌های جامعه — Go، Java، Node.js، Ollama |

### VS Code — استفاده از Context7

مستندات VS Code در **code.visualstudio.com** است، نه Learn.

| شناسه کتابخانه | استفاده برای |
|---|---|
| `/websites/code_visualstudio` | مستندات کاربر — تنظیمات، ویژگی‌ها، اشکال زدایی، توسعه از راه دور |
| `/websites/code_visualstudio_api` | Extension API — وب‌ویوها، TreeViews، دستورات، نقاط مشارکت |

### GitHub — استفاده از Context7

مستندات GitHub در **docs.github.com** و **cli.github.com** قرار دارند.

| شناسه کتابخانه | استفاده برای |
|---|---|
| `/websites/github_en` | اکشن‌ها، API، مخازن، امنیت، مدیریت، Copilot |
| `/websites/cli_github` | دستورات و گزینه‌های GitHub CLI (`gh`) |

### Agent Framework — استفاده از Learn MCP + Context7

آموزش‌های Agent Framework در learn.microsoft.com هستند (از `microsoft_docs_search` استفاده کنید)، اما **مخزن GitHub** شامل جزئیات سطح API است که معمولاً جلوتر از مستندات منتشر شده است — به ویژه مرجع REST API در DevUI، گزینه‌های CLI، و ادغام .NET.

| شناسه کتابخانه | استفاده برای |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | آموزش‌ها — راهنماهای DevUI، ردیابی، ارکستراسیون گردش کار |
| `/microsoft/agent-framework` | جزئیات API — نقاط پایانی REST در DevUI، گزینه‌های CLI، احراز هویت، .NET `AddDevUI`/`MapDevUI` |

**نکته DevUI:** ابتدا منبع وب‌سایت Learn را برای راهنماهای چگونگی استفاده جستجو کنید، سپس منبع مخزن را برای جزئیات سطح API (شماره‌گذاری نقاط پایانی، پیکربندی پروکسی، توکن‌های احراز هویت) بررسی کنید.

---

## راه‌اندازی Context7

برای هر پرس‌وجوی Context7، ابتدا شناسه کتابخانه را تعیین کنید (یک بار در هر جلسه):

1. فراخوانی `mcp_context7_resolve-library-id` با نام فناوری
2. فراخوانی `mcp_context7_query-docs` با شناسه کتابخانه بازگشتی و یک پرس‌وجوی خاص

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

زمینه را شامل کنید:
- **نسخه** در صورت مرتبط بودن (`.NET 8`، `Aspire 13`، `VS Code 1.96`)
- **هدف کار** (`quickstart`، `tutorial`، `overview`، `limits`، `API reference`)
- **زبان** برای مستندات چندزبانه (`Python`، `TypeScript`، `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->