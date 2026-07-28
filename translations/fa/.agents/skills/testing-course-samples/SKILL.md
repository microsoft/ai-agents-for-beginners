---
name: testing-course-samples
---
# آزمایش نمونه‌های دوره

اعتبارسنجی کنید که دفترچه‌های درس و نمونه‌های کد در برابر یک تنظیم زنده
Microsoft Foundry / Azure OpenAI اجرا می‌شوند. این مخزن یک اجراکننده را در
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) ارائه می‌دهد که
هر دفترچه پایتون را بدون رابط کاربری گرافیکی اجرا کرده و ماتریس قبول/رد را چاپ می‌کند.

## زمان استفاده
- "اعتبارسنجی تمام دفترچه‌ها / نمونه‌ها در برابر اشتراک Azure من."
- "آزمون سریع دوره پس از به‌روزرسانی بسته‌ها یا تغییر مدل‌ها."
- "کدام درس‌ها هنوز زنده قبول یا رد می‌شوند؟"

این را برای اقدام AI Smoke Test GitHub که عامل‌های مستقر شده را اعتبارسنجی می‌کند **استفاده نکنید**
(عامل‌های میزبانی شده — به [`tests/README.md`](../../../tests/README.md) مراجعه کنید). این مهارت
دفترچه‌ها را به صورت محلی اجرا می‌کند.

## پیش‌نیازها (ابتدا بررسی کنید)
1. **Python 3.12+** به همراه وابستگی‌های دوره: `python -m pip install -r requirements.txt`
   به علاوه اجراکننده: `python -m pip install nbconvert ipykernel`.
2. **`.env` در ریشه مخزن** (کپی از [`.env.example`](../../../../../.env.example)) حداقل شامل:
   - `AZURE_AI_PROJECT_ENDPOINT` — نقطه انتهایی پروژه Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — یک استقرار غیر منسوخ (مثلاً `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) و `AZURE_OPENAI_DEPLOYMENT`
     برای درس‌هایی که مستقیماً به Azure OpenAI فراخوانی می‌کنند (درس 06، 02-azure-openai، 14 handoff/human-loop).
3. **تکمیل شده `az login`** — نمونه‌ها با `AzureCliCredential` (Entra ID، بدون کلید) احراز هویت می‌شوند.
4. تأیید کنید که استقرار مدل وجود دارد:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## اجرای اعتبارسنجی
```powershell
# همه دفترچه‌های پایتون (صرف‌نظر از .NET، .venv، site-packages، ترجمه‌ها، دارایی‌های مهارتی)
pwsh scripts/validate-notebooks.ps1

# یک درس واحد، با تایم‌اوت طولانی‌تر برای هر سلول
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# فقط لیست آنچه اجرا خواهد شد (بدون اجرا)
pwsh scripts/validate-notebooks.ps1 -List

# مفسر صریح (اگر `python` در PATH نیست، مثلاً نام مستعار فروشگاه ویندوز)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
اسکریپت نسخه‌های اجرا شده، گزارش‌های هر دفترچه، و `results.json` را به
`$env:TEMP\aiab-nbval` می‌نویسد و با تعداد شکست‌ها خارج می‌شود.

## تفسیر نتایج
- `PASS` — دفترچه بدون خطا در سلول از ابتدا تا انتها اجرا شد.
- `FAIL` — اولین خط `*Error` / `*Exception` نمایش داده می‌شود؛ برای مشاهده دنبال‌نام خطا، `log_*.txt`
  متناظر در دایرکتوری خروجی را باز کنید.
- شکست یک دفترچه تنها توسط `-Timeout` (برای هر سلول) محدود شده است، بنابراین یک سلول معلق با تعامل انسان به صورت `StdinNotImplementedError`
  به جای معلق ماندن ظاهر می‌شود.

## درس‌هایی که منابع اضافی نیاز دارند (انتظار شکست بدون آن‌ها می‌رود)
| درس | نیاز اضافی |
|--------|-------------------|
| 05 Agentic RAG | جستجوی Azure AI (`AZURE_SEARCH_SERVICE_ENDPOINT`، کلید) — مسیر پشتیبان حافظه داخلی دارد |
| 11 MCP / GitHub | سرور MCP GitHub + PAT |
| 13 حافظه (cognee) | `cognee` پیکربندی شده با ارائه‌دهنده مدل |
| 15 استفاده از مرورگر | مرورگرهای Playwright نصب شده (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 عامل محلی | زمان‌اجرای محلی Foundry + یک مدل Qwen دانلود شده (روی دستگاه، بدون کلود) |
| دفترچه‌های `*-dotnet-*` | کرنل تعاملی .NET (به صورت پیش‌فرض حذف شده؛ از `-IncludeDotnet` استفاده کنید) |

## گزارش‌دهی بازگشت
خلاصه‌ای به صورت جدول قبول/رد گروه‌بندی شده بر اساس درس ارائه دهید. افت‌های واقعی
(باگ‌های کد/پیکربندی برای رفع) را از کمبودهای محیطی (کمبود جستجو/اجرا محلی Foundry/PAT)
تفکیک کنید و برای هر شکست واقعی، فایل `log_*.txt` مربوطه را ذکر کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->