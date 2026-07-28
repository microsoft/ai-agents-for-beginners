---
name: testing-course-samples
---
# কোর্স নমুনাগুলির পরীক্ষা

নিশ্চিত করুন যে পাঠের নোটবুক এবং কোড নমুনাগুলি লাইভ
Microsoft Foundry / Azure OpenAI সেটআপের বিরুদ্ধে চালানো হয়। রিপোতে একটি রানার রয়েছে
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) যা
প্রতিটি পাইথন নোটবুককে হেডলেসলি চালিয়ে পাস/ফেইল ম্যাট্রিক্স প্রিন্ট করে।

## কখন ব্যবহার করবেন
- "আমার Azure সাবস্ক্রিপশনের বিরুদ্ধে সব নোটবুক / নমুনা যাচাই করুন।"
- "প্যাকেজ আপগ্রেড বা মডেল পরিবর্তনের পর কোর্সের সংক্ষেপে পরীক্ষা করুন।"
- "কোন কোন পাঠ এখনও লাইভে পাস / ফেইল হচ্ছে?"

AI স্মোক টেস্ট GitHub Action এর জন্য এটি **ব্যবহার করবেন না** (যা *ডিপ্লয়ড*
হোস্টেড এজেন্ট যাচাই করে — দেখুন [`tests/README.md`](../../../tests/README.md))। এই স্কিল
নোটবুকগুলি লোকালি চালায়।

## পূর্বশর্ত (প্রথমে চেক করুন)
1. **Python 3.12+** কোর্স ডিপস সহ: `python -m pip install -r requirements.txt`
   অ্যাক্সিকিউটরের জন্য: `python -m pip install nbconvert ipykernel`.
2. **রিপো রুটে `.env`** (কপি করুন [`.env.example`](../../../../../.env.example)) অন্তত:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry প্রকল্পের এন্ডপয়েন্ট
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — একটি অপ্রচলিত নয় এমন ডিপ্লয়মেন্ট (যেমন `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) এবং `AZURE_OPENAI_DEPLOYMENT`
     এমন পাঠের জন্য যা সরাসরি Azure OpenAI কল করে (পাঠ ০৬, ০২-azure-openai, ১৪ হ্যান্ডঅফ/হিউম্যান-লুপ)।
3. **`az login`** সম্পন্ন — নমুনাগুলি `AzureCliCredential` দিয়ে প্রমাণীকরণ করে (Entra ID, কীবিহীন)।
4. মডেল ডিপ্লয়মেন্ট আছে কিনা যাচাই করুন:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`।

## যাচাই চালানো
```powershell
# সমস্ত পাইথন নোটবুক (এড়ানো হয় .NET, .venv, site-packages, অনুবাদ, দক্ষতা সম্পদ)
pwsh scripts/validate-notebooks.ps1

# একটি একক পাঠ, প্রতিটি সেলের জন্য দীর্ঘতর টাইমআউট সহ
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# শুধু তালিকা করুন যা চালানো হবে (কোনও কার্যকর করা হবে না)
pwsh scripts/validate-notebooks.ps1 -List

# স্পষ্ট দোভাষী (যদি `python` PATH-এ না থাকে, যেমন Windows Store আলিয়াস)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
স্ক্রিপ্টটি চালানো কপি, প্রতি-নোটবুক লগ এবং `results.json` লেখে
`$env:TEMP\aiab-nbval` এ এবং ব্যর্থতার সংখ্যাসহ বেরিয়ে আসে।

অস্থায়ী ব্যর্থতা (শেয়ার্ড-সাবস্ক্রিপশন HTTP 429 রেট লিমিট, মাঝে মাঝে
`AzureCliCredential` টোকেন সমস্যার ঘটনা, অথবা টাইমআউট) স্বয়ংক্রিয়ভাবে
পুনরায় চেষ্টা করা হয় (`-Retries`, ডিফল্ট ২, `-RetryDelaySeconds` ব্যাকঅফ সহ, ডিফল্ট ২০)। যদি একটি
মডেল ডিপ্লয়মেন্ট নিয়মিত 429 দেখায়, সাবস্ক্রিপশনের GlobalStandard
TPM কোটা যাচাই করুন (`az cognitiveservices usage list -l <region>`) — একটি
একক ডিপ্লয়মেন্টের ক্ষমতা বাড়ানো *সাবস্ক্রিপশনের* কোটা শেষ হলে সাহায্য করে না।

## ফলাফল ব্যাখ্যা করা
- `PASS` — নোটবুকটি কোনো সেল ত্রুটি ছাড়াই সম্পূর্ণ চালানো হয়েছে।
- `FAIL` — প্রথম `*Error` / `*Exception` লাইন দেখানো হয়; আউটপুট ডিরেক্টরিতে মিল থাকা
  `log_*.txt` খুলে সম্পূর্ণ ট্রেসব্যাক দেখুন।
- একটি নোটবুকের ব্যর্থতা `-Timeout` (প্রতি সেল) দ্বারা সীমাবদ্ধ, তাই একটি আটকে থাকা
  হিউম্যান-ইন-দ্য-লুপ সেল `StdinNotImplementedError` হিসেবে সরাসরি প্রদর্শিত হয়, হ্যাং হওয়ার পরিবর্তে।

## অতিরিক্ত সম্পদ প্রয়োজন এমন পাঠসমূহ (তারা না থাকলে ব্যর্থ হওয়ার প্রত্যাশা)
| পাঠ | অতিরিক্ত প্রয়োজনীয়তা |
|--------|-------------------|
| 05 Agentic RAG | Azure AI খোঁজ (`AZURE_SEARCH_SERVICE_ENDPOINT`, কী) — একটি ইন-মেমোরি ব্যাকআপ পথ আছে |
| 11 MCP / GitHub | GitHub MCP সার্ভার + PAT |
| 13 memory (cognee) | `cognee` একটি মডেল প্রদানকারী সহ কনফিগার করা |
| 15 browser-use | প্লেওরাইট ব্রাউজার ইনস্টল করা (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry লোকাল রানটাইম + একটি ডাউনলোড করা Qwen মডেল (অন্যদিকে, কোন ক্লাউড নয়) |
| `*-dotnet-*` নোটবুক | .NET ইন্টারেক্টিভ কার্নেল (ডিফল্টে বাদ দেওয়া হয়েছে; `-IncludeDotnet` ব্যবহার করুন) |

## রিপোর্টিং
পাঠভিত্তিক একটি PASS/FAIL টেবিল সংক্ষিপ্ত করুন। প্রকৃত রিগ্রেশন
(কোড/কনফিগ ত্রুটি) পরিবেশগত ফাঁক (মিসিং সার্চ/Foundry লোকাল/PAT) থেকে পৃথক করুন,
এবং প্রতিটি প্রকৃত ব্যর্থতার জন্য `log_*.txt` উল্লেখ করুন।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->