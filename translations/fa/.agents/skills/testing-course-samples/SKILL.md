---
name: testing-course-samples
---
# آزمایش نمونه‌های دوره

اطمینان حاصل کنید که دفترچه‌های درسی و نمونه‌های کد با یک تنظیم زنده
Microsoft Foundry / Azure OpenAI اجرا می‌شوند. مخزن یک اجراکننده در
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) دارد که
هر دفترچه پایتون را بدون واسط گرافیکی اجرا کرده و ماتریس PASS/FAIL چاپ می‌کند.

## زمان استفاده
- "اعتبارسنجی همه دفترچه‌ها / نمونه‌ها در مقابل اشتراک Azure من."
- "آزمایش سریع دوره پس از بروزرسانی بسته‌ها یا تغییر مدل‌ها."
- "کدام درس‌ها هنوز به طور زنده موفق / ناموفق هستند؟"

این را **استفاده نکنید** برای عملیات AI Smoke Test GitHub Action (که *عاملان مستقر‌شده*
را اعتبارسنجی می‌کند — به [`tests/README.md`](../../../tests/README.md) مراجعه کنید). این مهارت
دفترچه‌ها را به صورت محلی اجرا می‌کند.

## پیش‌نیازها (ابتدا بررسی کنید)
1. **Python 3.12+** همراه با وابستگی‌های دوره: `python -m pip install -r requirements.txt`
   به علاوه اجراکننده: `python -m pip install nbconvert ipykernel`.
2. **`.env` در ریشه مخزن** (کپی از [`.env.example`](../../../../../.env.example)) با حداقل:
   - `AZURE_AI_PROJECT_ENDPOINT` — نقطه انتهایی پروژه Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — استقرار غیرمنسوخ شده (مثلاً `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) و `AZURE_OPENAI_DEPLOYMENT`
     برای درس‌هایی که مستقیماً Azure OpenAI را فراخوانی می‌کنند (درس 06، 02-azure-openai، 14 handoff/human-loop).
3. **`az login`** تکمیل شده — نمونه‌ها با `AzureCliCredential` احراز هویت می‌کنند (Entra ID، بدون کلید).
4. اطمینان از وجود استقرار مدل:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## اجرای اعتبارسنجی
```powershell
# All Python notebooks (skips .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# A single lesson, with a longer per-cell timeout
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Just list what would run (no execution)
pwsh scripts/validate-notebooks.ps1 -List

# Explicit interpreter (if `python` is not on PATH, e.g. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
اسکریپت کپی‌های اجرا شده، گزارش‌های هر دفترچه و `results.json` را در
`$env:TEMP\aiab-nbval` می‌نویسد و با تعداد شکست‌ها خارج می‌شود.

شکست‌های موقتی (محدودیت‌های نرخ HTTP 429 اشتراک مشترک، ایجاد اشکال گاه‌به‌گاه توکن `AzureCliCredential`، یا تایم‌اوت)
به صورت خودکار تلاش مجدد می‌شوند
(`-Retries`، مقدار پیش‌فرض 2، با پس‌نشینی `-RetryDelaySeconds`، پیش‌فرض 20). اگر یک
استقرار مدل مکرراً با 429 مواجه شود، سهمیه TPM استاندارد جهانی اشتراک را بررسی کنید (`az cognitiveservices usage list -l <region>`) — افزایش ظرفیت
یک استقرار منفرد زمانی که سهمیه اشتراک *تمام* شده باشد، کمکی نمی‌کند.


## تفسیر نتایج
- `PASS` — دفترچه به طور کامل بدون خطای سلولی اجرا شده است.
- `FAIL` — اولین خط `*Error` / `*Exception` نمایش داده شده است؛
  برای مشاهده ردگیری کامل، `log_*.txt` متناظر در دایرکتوری خروجی را باز کنید.
- شکست یک دفترچه تنها محدود به `-Timeout` (به ازای هر سلول) است، پس یک سلول انسان-در-حلقه که گیر کرده
  به صورت `StdinNotImplementedError` ظاهر می‌شود به جای اینکه آویزان شود.

## درس‌هایی که به منابع اضافی نیاز دارند (انتظار می‌رود بدون آن‌ها شکست بخورند)
| درس | نیازمندی اضافی |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`، کلید) — مسیر جایگزین حافظه داخلی دارد |
| 11 MCP / GitHub | سرور MCP گیت‌هاب + PAT |
| 13 حافظه (cognee) | `cognee` با یک ارائه‌دهنده مدل پیکربندی شده است |
| 15 استفاده مرورگر | مرورگرهای Playwright نصب شده (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 عامل محلی | زمان اجرای محلی Foundry + مدلی Qwen دانلود شده (روی دستگاه، بدون ابر) |
| دفترچه‌های `*-dotnet-*` | هسته .NET Interactive (به طور پیش‌فرض مستثنی شده؛ استفاده از `-IncludeDotnet`) |

## گزارش‌دهی برگشتی
خلاصه‌ای به صورت جدول PASS/FAIL گروه‌بندی شده بر اساس درس تهیه کنید. افت واقعی را
(اشکالات کد/پیکربندی که باید رفع شوند) از کمبودهای محیطی (جستجو/Foundry Local/PAT ناقص) جدا کنید،
و برای هر شکست واقعی `log_*.txt` را ذکر کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->