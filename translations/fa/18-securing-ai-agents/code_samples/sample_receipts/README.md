# نمونه فایل‌های رسید آماده

سه فایل رسید از پیش ساخته شده برای بررسی بدون اجرای نوت‌بوک.

| فایل | توضیحات |
|---|---|
| `01_valid_receipt.json` | یک رسید معتبر امضا شده برای فراخوانی ابزار `lookup_flights`. تأیید اعتبار نتیجه True می‌دهد. |
| `02_tampered_receipt.json` | همان رسید با یک فیلد تغییر یافته بعد از امضا. تأیید اعتبار نتیجه False می‌دهد. |
| `03_chain_three_receipts.json` | یک زنجیره از سه رسید معتبر (جستجو، نگه‌داشت، رزرو) که هرکدام با `previous_receipt_hash` به قبلی متصل شده‌اند. |

فایل‌ها مستقیم بایت‌های canonical JCS داده را با Ed25519 امضا می‌کنند.
SHA-256 برای هضم محتوا و لینک‌های زنجیره رسید استفاده می‌شود، نه به عنوان
پیش‌هشد اضافی قبل از امضا.

## تأیید نمونه‌ها

در `18-signed-receipts.ipynb` ابتدا بخش Setup و بخش‌های ۱ تا ۳ را اجرا کنید.
بخش ۳ تعریف کننده `verify_chain` است؛ فقط بخش‌های ۱ و ۲ کافی نیستند.
سپس بلوک زیر را در یک سل جدید اجرا کنید، با دایرکتوری کاری نوت‌بوک
تنظیم شده به `18-securing-ai-agents/code_samples`. مسیرهای فایل زیر نسبت به آن دایرکتوری هستند.


```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# This fixture key is pinned by the verifier, outside the receipt under test.
FIXTURE_ISSUER_PUBLIC_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"
fixture_trusted_public_keys = {FIXTURE_ISSUER_PUBLIC_KEY}

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text())
print(
    f"Valid receipt: {verify_receipt(valid, fixture_trusted_public_keys)}"
)  # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text())
print(
    f"Tampered receipt: {verify_receipt(tampered, fixture_trusted_public_keys)}"
)  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text())
for r in verify_chain(chain, fixture_trusted_public_keys):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

### بررسی نمونه بدون Jupyter

از ریشه مخزن، وابستگی‌های درس را نصب و اجرا کنید:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

این آزمون‌ها نمونه‌های پایتون نوت‌بوک و همان بلوک README را اجرا می‌کنند.
همچنین بررسی می‌کنند که تغییرات غیرمجاز و کلیدهای بدون پین‌شدن توسط
تأییدکننده‌ها رد شوند. این آزمون‌ها سل Setup در نوت‌بوک با نام `%pip` را رد می‌کنند زیرا وابستگی‌ها جداگانه نصب شده‌اند.
آن‌ها نوت‌بوک یا فایل‌ها را تغییر نمی‌دهند.

## روند تولید این فایل‌ها

فایل‌ها از همان مسیر کد نوت‌بوک استفاده می‌کنند، با یک کلید امضای ثابت
و زمان‌های ثابت برای تکرارپذیری بایتی. برای بازتولید:

```bash
python3 generate_fixtures.py
```

(اسکریپت در `generate_fixtures.py` در این دایرکتوری است.)

## آنچه دانش‌آموزان از بررسی JSON خام یاد می‌گیرند

خواندن فرمت خام رسید شهودی را می‌سازد که سل‌های نوت‌بوک همیشه ارائه نمی‌دهند.
دانش‌آموزانی که JSON را مرور می‌کنند اغلب متوجه موارد زیر می‌شوند:

1. امضا یک رشته base64url مبهم است، اما هر فیلد دیگر JSON خوانا و ساده است.
   امضا محتوا را رمزنگاری نمی‌کند؛ بلکه به آن گواهی می‌دهد.
2. `public_key` در رسید جاسازی شده است که برای بررسی
   خود انسجام کافی است اما اعتماد به صادرکننده را تضمین نمی‌کند. یک حسابرس باید آن را با کلیدی
   که خارج از رسید پین شده یا از طریق یک رجیستری مورد اعتماد حل شده، مقایسه کند.
3. تغییر حتی یک کاراکتر در هر فیلد و سپس مقایسه مجدد این فایل با
   `02_tampered_receipt.json`، مکانیزم سطح بایت را ملموس می‌کند.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->