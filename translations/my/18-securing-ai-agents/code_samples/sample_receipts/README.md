# နမူနာရရှိမှု ဖိုင်များ

notebook မပြည့်စုံစွာ လည်ပတ်ခြင်းမရှိဘဲ စစ်ဆေးနိုင်ရန် ကြိုတင်ပြင်ဆင်ထားသော ရရှိမှုဖိုင်လေးခု။

| ဖိုင် | အရာဟာဘာလဲ |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` ကိရိယာခေါ်စဉ်အတွက် မှန်ကန်စီလျော်ပြီး လက်မှတ်ရေးထိုးထားသော ရရှိမှုတစ်ခု။ စစ်ဆေးမှုက True ပြန်လာသည်။ |
| `02_tampered_receipt.json` | လက်မှတ်ရေးထိုးပြီးနောက် အကွက်တစ်ခုပြောင်းလဲထားသော အတူတူ ရရှိမှု။ စစ်ဆေးမှုက False ပြန်လာသည်။ |
| `03_chain_three_receipts.json` | အတည်ပြုထားသော ရရှိမှုသုံးခုစီးကြောင်း (ရှာဖွေမှု၊ ကိုင်တွယ်မှု၊ ဝယ်ယူမှု) နှင့် `previous_receipt_hash` သည် ပြီးခဲ့သော အရာနှင့် ချိတ်ဆက်ထားသည်။ |
| `04_resigned_receipt.json` | တိုက်ခိုက်သူတစ်ဦးမှ ကစားနေပြီး ပြန်လည်လက်မှတ်ရေးထိုးထားသော ရရှိမှုတူသည်။ တိုက်ခိုက်သူ၏ ကိုယ့်သူ ပုဂ္ဂိုလ်အသီးသီးသော ကျွတ်သော Key ဖြင့်ထည့်သွင်းထားသည်။ ရှေ့မှာရှိသော Key ဖြင့် စစ်ဆေးလျှင် မပြီး။ |

ဤ fixtures များသည် payload ၏ canonical JCS bytes ကိုတိုက်ရိုက် Ed25519 ဖြင့် လက်မှတ်ရေးထိုးသည်။
SHA-256 ကို အကြောင်းအရာ digest များနှင့် ရရှိမှုချိတ်ဆက်မှုများအတွက်သာ အသုံးပြုထားကာ,
လက်မှတ်ရေးထိုးမှုမတိုင်မီ အပို pre-hash အဖြစ်မသုံးပါ။

## နမူနာများကို စစ်ဆေးခြင်း

`18-signed-receipts.ipynb` တွင် Setup နှင့် ပုဒ်မ ၁ မှ ၃ အထိကို စဉ်လိုက် လုပ်ဆောင်ပါ။
ပုဒ်မ ၃ သည် `verify_chain` ကို သတ်မှတ်ထားပြီး ပုဒ်မ ၁ နှင့် ၂ သာဖြင့် မလုံလောက်ပါ။
ပြီးရင် နေရာသစ်ကွက်တစ်ခုမှာ အောက်ပါ ကိုဒ်အပိုင်းကို နှိပ်၍ ကားချက်ပတ်ဝန်းကျင်၏ လည်ပတ်နေသော ဖိုင်လမ်းကြောင်းကို 
`18-securing-ai-agents/code_samples` အဖြစ် သတ်မှတ်ပါ။ အောက်ပါ လမ်းကြောင်းများသည် ဤဖိုင်လမ်းကြောင်းနှင့် ဆက်စပ်သည်။


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

### Jupyter မပါဘဲ ဥပမာကို စစ်ဆေးခြင်း

သိုလှောင်တင်ရာမူလနေရာမှ သင်ခန်းစာပေါ်မူတည်ချက်များကို 설치ပြီး အောက်ပါကိရိယာကို 실행ပါ။

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ဒီစမ်းသပ်မှုများသည် notebook ရဲ့ Python ဥပမာများနှင့် အထက်ဖော်ပြပါ README ဗလာကို တိတိကျကျ အလုပ်လုပ်စေပါသည်။
၎င်းအပြင် တမန့်မှုနှင့် unpinned key များကို verification အဖွဲ့ဝင်များက ပိတ်ပင်ဆန့်ကျင်ကြောင်းလဲ စစ်ဆေးသည်။
စမ်းသပ်မှုများသည် notebook ရဲ့ `%pip` စတင်မှုဆဲလ်ကို ပြေးလို့ မရှိပါ၊ အကြောင်းမှာ မူတည်ချက်များကို မတူညီအနေဖြင့် 설치လိုက်ခြင်း ဖြစ်သည်။
၎င်းသည် notebook သို့ fixture များကို မပြောင်းလဲပါ။

## ဒါတွေ ဘယ်လိုဖန်တီးခဲ့တာလဲ

ထို fixtures များသည် notebook နှင့် မတူညီသော စာရေးနည်းလမ်းတစ်ခုကို အသုံးပြုပေမယ့်
ဘိုက်ထုန်မှတည်ငြိမ်မှုရှိစေရန် အတည်ပြုချက်မှတ်တမ်းအားတစ်ခုနှင့် အချိန်တုရိုးတစ်ခုကို သတ်မှတ်ထားသည်။ ပြန်လည်ဖန်တီးရန်။

```bash
python3 generate_fixtures.py
```

(script သည် ဒီ directory တွင် `generate_fixtures.py` တွင်ရှိသည်။)

`../test_signed_receipts.py` သည် အလိုအလျောက် ဤအရာအားလုံးကို စစ်ဆေးသည်။ ၎င်းသည်
notebook ၏ ကုဒ်ကို ရှာဖွေပြေးဆွဲပြီး fixtures ၄ ခုဖြင့် notebook ၏
`verify_receipt` နှင့် `verify_chain` ကို အတည်ပြုသည်၊ ပြန်လည်ဖန်တီးခြင်းသည်
fixtures များနှင့် တူညီသော ဘိုက်တစ်များရှိကြောင်း သေချာစေသည်။ `code_samples` မှ။

```bash
python -m unittest test_signed_receipts
```

## ကျောင်းသားများ ရှင်းလင်းကြည့်ရှုခြင်းမှ ရယူသော အရာများ

ကြည့်ရှုစစ်ဆေးသော receipt အမျိုးအစားသည် notebook ၏ ကုလားထိုင်များ စဉ်ဆက်မပြတ်ဖြေရှင်းပုံကို မပေးနိုင်သော အတွင်းစိတ်ကိုတည်ဆောက်ပေးသည်။
JSON ကို ပေါ်တင်ကြည့်ရှုသော ကျောင်းသားများသည် အထူးသဖြင့် သတိပြုမိကြသည်။

1. အတည်ပြုချက်သည် opaque base64url စာကြောင်းတစ်ခု ဖြစ်သော်လည်း အခြား field များအားလုံးသည် ပျော်ရွှင်စရာJSON ဖြစ်သည်။
   အတည်ပြုချက်သည် အကြောင်းအရာကို စာတည်းဖွင့်ခြင်းမဟုတ်ပဲ ၎င်းကို အတည်ပြုသည်။
၂။ `public_key` သည် စာရင်းပေါ်တွင် ထည့်သွင်းထားပြီး၊ ၎င်းသည် ဖိုင်ကို ပြုလုပ်ပေးသည်
   တစ်ကိုယ်တော်ဖြစ်သော်လည်း စစ်ဆေးသူတစ်ဦးက စစ်ဆေးတာမဟုတ်ပါ။ နှိုင်းယှဉ်ကြည့်ပါ
   `02_tampered_receipt.json` ကို `04_resigned_receipt.json` နှင့် - နှစ်ခုစလုံးကို
   လက်မှတ်ရေးထိုးပြီးနောက် ပြောင်းလဲခဲ့သော်လည်း ဒုတိယဟာ ဝင်ရောက်တိုက်ခိုက်သူ၏
   မိမိသော key ဖြင့် ပြန်လက်မှတ်ရေးထိုးခဲ့သောကြောင့် သယ်ဆောင်ထားသော key နှင့် စစ်ဆေးသည်။
   ထည့်သွင်းထားသော key သည် ဖိုင်သည် အတွင်းပိုင်းသဟဇာတရှိသည်ကို ပြောပြသည်။ ဘယ်နေရာမှ ရရှိသော key
   တစ်ခုသာ သင်ကို ထုတ်ပေးသူကို ပြောပြသည်။
3. `signature` ပြင်ပရှိ အကွက်တစ်ခုလုံး၌ တစ်လုံးတည်းကရာတာကို ပြင်ဆင်ပြီး
   ထို့နောက် ဖိုင်ကို `02_tampered_receipt.json` နှင့် ပြန်လည်နှိုင်းယှဉ်ခြင်းသည်
   byte အဆင့်စစ်ဆေးမှုပုံစံကို ထိတွေ့ခံနိုင်စေသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->