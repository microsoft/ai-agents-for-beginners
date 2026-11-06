# নমুনা রসিদ ফিকচার

নোটবুক চালানো ছাড়াই পরিদর্শনের জন্য তিনটি পূর্ব-উত্পন্ন রসিদ ফাইল।

| ফাইল | এটি কী |
|---|---|
| `01_valid_receipt.json` | একটি বৈধ স্বাক্ষরযুক্ত রসিদ একটি `lookup_flights` টুল কলের জন্য। যাচাই সত্য ফেরত দেয়। |
| `02_tampered_receipt.json` | স্বাক্ষর করার পরে একটি ক্ষেত্র পরিবর্তিত হওয়া একই রসিদ। যাচাই মিথ্যা ফেরত দেয়। |
| `03_chain_three_receipts.json` | তিনটি বৈধ রসিদের একটি চেইন (search, hold, book) যেখানে `previous_receipt_hash` প্রতিটি আগেরটির সাথে সংযুক্ত করছে। |

ফিক্সচারগুলি সরাসরি Ed25519 দিয়ে পে-লোডের canonical JCS বাইটগুলিতে স্বাক্ষর করে।
SHA-256 কন্টেন্ট ডাইজেস্ট এবং রসিদ-চেইন লিঙ্কের জন্য ব্যবহৃত হয়, স্বাক্ষরের আগে অতিরিক্ত pre-hash হিসাবে নয়।
অতিরিক্ত pre-hash স্বাক্ষরের আগে ব্যবহৃত হয় না।

## নমুনাগুলো যাচাই করা

`18-signed-receipts.ipynb` তে, প্রথমে Setup এবং Section 1 থেকে 3 চালান।
Section 3 এ `verify_chain` সংজ্ঞায়িত করা হয়েছে; কেবল Section 1 এবং 2 যথেষ্ট নয়।
তারপর একটি নতুন সেলে নিচের ব্লকটি চালান, যেখানে নোটবুকের কাজের ডিরেক্টরি
সেট করা হয়েছে `18-securing-ai-agents/code_samples` এ। নিচের ফিক্সচারের পথগুলি সেই ডিরেক্টরির আপেক্ষিক।


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

### জুপিটার ছাড়া উদাহরণ পরীক্ষা করা

রিপোজিটোরি রুট থেকে, লেসনের ডিপেন্ডেন্সিগুলি ইনস্টল করুন এবং চালান:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

এই টেস্টগুলি নোটবুকের পাইথন উদাহরণসমূহ এবং ঠিক উপরের README ব্লকটি চালায়।  
সেগুলিও যাচাই করে যে তাম্পারিং এবং আনপিন করা কীগুলি ভেরিফায়ার দ্বারা প্রত্যাখ্যাত হচ্ছে।  
টেস্টগুলি নোটবুকের `%pip` সেটআপ সেল এড়িয়ে যায় কারণ ডিপেন্ডেন্সিগুলি আলাদাভাবে ইনস্টল করা হয়।  
এগুলি নোটবুক বা ফিক্সচারে কোনো পরিবর্তন আনে না।  

## এগুলি কীভাবে তৈরি করা হয়েছে

ফিক্সচারগুলি একই কোড পাথ ব্যবহার করে যেমন নোটবুক, একটি নির্দিষ্ট সাইনিং কী সহ
এবং বাইট-রিপ্রোডিউসিবিলিটির জন্য নির্দিষ্ট টাইমস্ট্যাম্প সহ। পুনরায় তৈরি করতে:

```bash
python3 generate_fixtures.py
```

(স্ক্রিপ্টটি এই ডিরেক্টরির `generate_fixtures.py` এ রয়েছে।)

## ছাত্ররা কাঁচা JSON পরিদর্শন থেকে কী শেখে

কাঁচা রসিদ ফরম্যাট পড়া এমন বোধ গড়ে তোলে যা নোটবুকের সেল সবসময় দেয় না। 
JSON স্কিম করা শিক্ষার্থীরা প্রায়ই লক্ষ্য করে:

1. সাক্ষরটি একটি অপ্যাক বেস64url স্ট্রিং, কিন্তু বাকী সব ক্ষেত্র সোজাসুজি
   পড়ার উপযোগী JSON। সাক্ষরটি বিষয়বস্তু এনক্রিপ্ট করে না; এটি তার প্রমাণ দেয়।
2. `public_key` রসিদে অন্তর্ভুক্ত থাকে, যা স্ব-সঙ্গতি যাচাই করার জন্য যথেষ্ট,
   কিন্তু ইস্যুকারককে বিশ্বাস করার জন্য নয়। একজন নিরীক্ষককে এটি একটি কীয়ের সঙ্গে তুলনা করতে হবে
   যা রসিদের বাইরে পিন করা আছে বা একটি বিশ্বাসযোগ্য রেজিস্ট্রির মাধ্যমে সমাধান করা হয়েছে।
৩. যেকোনো ক্ষেত্রের একক অক্ষর পরিবর্তন করা, তারপর এই ফাইলটিকে পুনরায় তুলনা করা  
   `02_tampered_receipt.json`, বাইট-স্তরের পদ্ধতিটিকে বাস্তব রূপ দেয়।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->