# নমুনা রসিদ ফিক্সচার

নোটবুক চালানো ছাড়াই পরিদর্শনের জন্য চারটি পূর্ব-তৈরি রসিদ ফাইল।

| ফাইল | এটি কী |
|---|---|
| `01_valid_receipt.json` | একটি বৈধ স্বাক্ষরিত রসিদ একটি `lookup_flights` টুল কলের জন্য। যাচাইকরণ সত্য ফিরিয়ে দেয়। |
| `02_tampered_receipt.json` | স্বাক্ষরের পরে একটি ক্ষেত্র পরিবর্তিত একই রসিদ। যাচাইকরণ মিথ্যা ফিরিয়ে দেয়। |
| `03_chain_three_receipts.json` | তিনটি বৈধ রসিদের শৃঙ্খল (search, hold, book) যেখানে `previous_receipt_hash` প্রতিটি পূর্ববর্তীটির সাথে যুক্ত করে। |
| `04_resigned_receipt.json` | একই রসিদে আক্রমণকারী দ্বারা টেম্পার করা হয়েছে এবং পুনরায় স্বাক্ষর করা হয়েছে, আক্রমণকারীর নিজস্ব পাবলিক কী এম্বেড করা হয়েছে। এর ভেতরের কী বিরুদ্ধে যাচাই করে। ইস্যুকারীর কী বিরুদ্ধে ব্যর্থ হয়। |

ফিক্সচারগুলি সরাসরি Ed25519 দিয়ে পে'লডের ক্যানোনিক্যাল JCS বাইটগুলো স্বাক্ষর করে।
SHA-256 কন্টেন্ট ডাইজেস্ট এবং রসিদ-শৃঙ্খল লিঙ্কের জন্য ব্যবহৃত হয়, স্বাক্ষরের আগে অতিরিক্ত প্রি-হ্যাশ হিসাবে নয়।


## নমুনাগুলো যাচাই

`18-signed-receipts.ipynb`, এ প্রথমে Setup এবং সেকশন 1 থেকে 3 চালান।
সেকশন 3 এ `verify_chain` সংজ্ঞায়িত; সেকশন 1 এবং 2 একলা যথেষ্ট নয়।
তারপর নিম্নলিখিত ব্লকটি একটি নতুন সেলে চালান, নোটবুকের কাজের ডিরেক্টরি
`18-securing-ai-agents/code_samples` হিসাবে সেট করা হয়েছে। নিচের ফিক্সচার পাথগুলো সেই ডিরেক্টরির আপেক্ষিক।


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

### জুপিটার ছাড়া উদাহরণ যাচাই

রিপোজিটরির মূল থেকে, পাঠের নির্ভরশীলতা ইনস্টল করুন এবং চালান:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

এই পরীক্ষা গুলো নোটবুকের পাইথন উদাহরণ এবং সঠিক README ব্লক চালায়
উপরে। এগুলো যাচাই করে যে ছিনতাইকৃত এবং আনপিন করা কী গুলো যাচাইকারীগণের দ্বারা প্রত্যাখ্যাত হয়েছে কি না।
পরীক্ষা গুলো নোটবুকের `%pip` সেটআপ সেলটি এড়িয়ে চলে কারণ নির্ভরশীলতা আলাদাভাবে ইনস্টল করা হয়।
এগুলো নোটবুক বা ফিক্সচার গুলো পরিবর্তন করে না।

## এগুলো কীভাবে তৈরি হয়েছে

ফিক্সচার গুলো একই কোড পথ ব্যবহার করে যেমন নোটবুক, একটি ফিক্সড সাইনিং কী সহ
এবং বিট-প্রজননযোগ্যতার জন্য স্থির টাইমস্ট্যাম্প সহ। পুনরায় তৈরি করতে:

```bash
python3 generate_fixtures.py
```

(স্ক্রিপ্টটি এই ডিরেক্টরির `generate_fixtures.py` এ রয়েছে।)

`../test_signed_receipts.py` স্বয়ংক্রিয়ভাবে এটি সব পরীক্ষা করে: এটি চালায়
নোটবুকের কোড, এই চারটি ফিক্সচার নোটবুকের
`verify_receipt` এবং `verify_chain` দিয়ে যাচাই করে, এবং নিশ্চিত করে যে পুনরায় তৈরি করা
ফিক্সচারগুলি অভিন্ন বাইট দেয়। `code_samples` থেকে:

```bash
python -m unittest test_signed_receipts
```

## শিক্ষার্থীরা কি শেখে কাঁচা JSON পরীক্ষা করে

কাঁচা রসিদ ফরম্যাট পড়া সেই অন্তর্দৃষ্টি গড়ে তোলে যা নোটবুকের
কোষগুলি সবসময় প্রদান করে না। JSON দ্রুত লক্ষ করা শিক্ষার্থীরা প্রায়ই লক্ষ্য করে:

1. স্বাক্ষর একটি অস্পষ্ট base64url স্ট্রিং, কিন্তু প্রতিটি অন্য ক্ষেত্র সাধারণ
   পাঠযোগ্য JSON। স্বাক্ষর সামগ্রীটি এনক্রিপ্ট করে না; এটি তার প্রতি সনদ দেয়।
2. `public_key` রসিদে এম্বেড করা আছে, যা ফাইলটিকে
   স্ব-সম্পূর্ণ করে তোলে কিন্তু এটি নয় যা নিরীক্ষক যাচাই করে। তুলনা করুন
   `02_tampered_receipt.json` এর সাথে `04_resigned_receipt.json`: উভয়ই
   সই করার পরে পরিবর্তিত হয়েছিল, কিন্তু দ্বিতীয়টি আক্রমণকারীর
   নিজস্ব কী দিয়ে পুনঃসই করা হয়েছিল, সুতরাং এটি তার বহনকৃত কী এর বিরুদ্ধে যাচাই করে। এম্বেড করা কীটি
   বলে দেয় যে ফাইলটি অভ্যন্তরীণভাবে সামঞ্জস্যপূর্ণ। শুধুমাত্র বাহ্যিক উৎস থেকে প্রাপ্ত কী
   বলে দেয় এটি কে ইস্যু করেছে।
3. `signature` এর বাইরে যেকোনো ক্ষেত্রের একটি মাত্র অক্ষর পরিবর্তন করা, তারপরে
   এই ফাইলটি `02_tampered_receipt.json` এর সাথে পুনরায় তুলনা করা,
   বাইট-স্তরের ব্যবস্থাটি স্পষ্ট করে তোলে।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->