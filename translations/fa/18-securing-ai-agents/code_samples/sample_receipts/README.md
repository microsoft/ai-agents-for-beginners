# نمونه فایل‌های رسید

چهار فایل رسید از پیش تولید شده برای بررسی بدون اجرای نوت‌بوک.

| فایل | محتوا |
|---|---|
| `01_valid_receipt.json` | یک رسید معتبر امضا شده برای فراخوانی ابزار `lookup_flights`. تأیید صحت مقدار True بازمی‌گرداند. |
| `02_tampered_receipt.json` | همان رسید با یک فیلد تغییر یافته پس از امضا. تأیید صحت مقدار False بازمی‌گرداند. |
| `03_chain_three_receipts.json` | زنجیره‌ای از سه رسید معتبر (جستجو، نگه‌داشت، رزرو) با `previous_receipt_hash` که هر کدام را به قبلی پیوند می‌دهد. |
| `04_resigned_receipt.json` | همان رسید دستکاری شده و سپس توسط مهاجم دوباره امضا شده، با کلید عمومی خود مهاجم جاسازی شده. نسبت به کلید داخل آن تأیید می‌شود. نسبت به کلید صادرکننده رد می‌شود. |

این فایل‌ها، بایت‌های استاندارد JCS محتوای اصلی را مستقیماً با Ed25519 امضا می‌کنند.
SHA-256 همچنان برای خلاصه‌های محتوا و پیوندهای زنجیره رسید استفاده می‌شود، نه به عنوان
پیش‌تکمیلی پیش از امضا.

## تأیید نمونه‌ها

در `18-signed-receipts.ipynb`، ابتدا Setup و بخش‌های 1 تا 3 را اجرا کنید.
بخش 3 تعریف می‌کند `verify_chain`؛ فقط بخش‌های 1 و 2 کافی نیستند.
سپس بلوک زیر را در یک سل جدید اجرا کنید، با دایرکتوری کاری نوت‌بوک
تنظیم شده به `18-securing-ai-agents/code_samples`. مسیرهای فایل‌ها در پایین به این دایرکتوری نسبت داده شده‌اند.


```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### بررسی مثال بدون Jupyter

از ریشه مخزن، وابستگی‌های درس را نصب کرده و اجرا کنید:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

این تست‌ها نمونه‌های پایتونی نوت‌بوک و بلوک دقیق README را اجرا می‌کنند
بالا. آنها همچنین بررسی می‌کنند که دستکاری‌ها و کلیدهای غیرسنجاق‌خورده توسط 
تاییدکنندگان رد می‌شوند. تست‌ها سلول راه‌اندازی `%pip` دفترچه یادداشت را رد می‌کنند زیرا وابستگی‌ها 
جداگانه نصب شده‌اند. آنها دفترچه یا ابزارهای آزمایشی را تغییر نمی‌دهند.

## چگونه اینها تولید شدند

ابزارهای آزمایشی از همان مسیر کد دفترچه استفاده می‌کنند، با یک کلید امضای ثابت 
و زمان‌های ثابت برای بازتولید بایت. برای تولید مجدد:

```bash
python3 generate_fixtures.py
```

(اسکریپت در `generate_fixtures.py` در این دایرکتوری قرار دارد.)

`../test_signed_receipts.py` به‌صورت خودکار همه این‌ها را بررسی می‌کند: این اجرا می‌کند
کد دفترچه یادداشت، این چهار ابزار آزمایشی را با دفترچه یادداشت
`verify_receipt` و `verify_chain` بررسی می‌کند و تأیید می‌کند که تولید مجدد
ابزار آزمایشی، بایت‌های یکسانی را به‌دست می‌دهد. از `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## آنچه دانش‌آموزان از بررسی JSON خام یاد می‌گیرند

خواندن فرمت خام رسید شهودی را ایجاد می‌کند که سلول‌های دفترچه
همیشه فراهم نمی‌کنند. دانش‌آموزانی که JSON را به‌سرعت نگاه می‌کنند اغلب متوجه می‌شوند:

1. امضا رشته‌ای رمزگذاری شده‌ی base64url غیرشفاف است، اما هر فیلد دیگر به صورت JSON قابل خواندن ساده است.
   امضا محتوا را رمزنگاری نمی‌کند؛ بلکه بر آن صحه می‌گذارد.
2. `public_key` در رسید جای‌گذاری شده است که باعث می‌شود فایل
   خودکفا است اما چیزی نیست که یک حسابرس بر اساس آن تأیید کند. مقایسه کنید
   `02_tampered_receipt.json` با `04_resigned_receipt.json`: هر دو پس از امضا تغییر کرده‌اند،
   اما دومی با کلید خود حمل‌کننده که به‌دست مهاجم است دوباره امضا شده،
   بنابراین در مقابل کلیدی که دارد تأیید می‌شود. کلید جاسازی‌شده
   به شما می‌گوید فایل از درون سازگار است. تنها کلیدی که از جای دیگری به‌دست آمده
   به شما می‌گوید که چه کسی آن را صادر کرده است.
3. تغییر یک کاراکتر واحد در هر فیلدی خارج از `signature`، سپس
   دوباره مقایسه این فایل با `02_tampered_receipt.json`، مکانیزم سطح بایت را عینی می‌کند.
 

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->