# AGENTS.md

## প্রকল্পের পর্যালোচনা

এই রিপোজিটরিটি "শিক্ষানবিসদের জন্য AI এজেন্ট" ধারণ করে - একটি ব্যাপক শিক্ষামূলক কোর্স যা AI এজেন্ট তৈরি করতে প্রয়োজনীয় সবকিছু শেখায়। এই কোর্সে ১৮টি পাঠ (সংখ্যাঙ্ক ০০-১৮) রয়েছে যা মৌলিক বিষয়, ডিজাইন প্যাটার্ন, ফ্রেমওয়ার্ক, প্রোডাকশন ডিপ্লয়মেন্ট, লোকাল/ডিভাইস ভিত্তিক এজেন্ট, এবং AI এজেন্টের সিকিউরিটি কভার করে।

**মূল প্রযুক্তিসমূহ:**
- Python 3.12+
- ইন্টারেক্টিভ শিক্ষার জন্য Jupyter নোটবুক
- AI ফ্রেমওয়ার্ক: Microsoft Agent Framework (MAF)
- Azure AI সেবাসমূহ: Microsoft Foundry, Microsoft Foundry Agent Service V2

**বিন্যাস:**
- পাঠ-ভিত্তিক স্থাপত্য (০০-১৮ নির্দেশিকা)
- প্রতিটি পাঠে থাকে: README ডকুমেন্টেশন, কোড নমুনা (Jupyter নোটবুক), এবং ছবি
- স্বয়ংক্রিয় অনুবাদ ব্যবস্থার মাধ্যমে বহুভাষী সমর্থন
- প্রতি পাঠে একক Python নোটবুক যা Microsoft Agent Framework ব্যবহার করে

## সেটআপ কমান্ড

### প্রাকশর্তসমূহ
- Python 3.12 বা তার উপরের সংস্করণ
- Azure সাবস্ক্রিপশন (Microsoft Foundry এর জন্য)
- Azure CLI ইনস্টল করা এবং প্রমাণীকৃত (`az login`)

### প্রাথমিক সেটআপ

১. **রিপোজিটরি ক্লোন বা ফর্ক করুন:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

২. **Python ভার্চুয়াল এনভায়রনমেন্ট তৈরি এবং সক্রিয় করুন:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

৩. **ডিপেন্ডেন্সি ইন্সটল করুন:**
   ```bash
   pip install -r requirements.txt
   ```

৪. **পরিবেশ পরিবর্তনশীল সেটআপ করুন:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### প্রয়োজনীয় পরিবেশ পরিবর্তনশীল

**Microsoft Foundry** (প্রয়োজনীয়):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry প্রকল্প এন্ডপয়েন্ট
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - মডেল ডিপ্লয়মেন্ট নাম (যেমন, gpt-5-mini)

**Azure AI Search** (পাঠ ০৫ - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search এন্ডপয়েন্ট
- `AZURE_SEARCH_API_KEY` - Azure AI Search API কী

প্রমাণীকরণ: নোটবুক চালানোর আগে `az login` রান করুন (ব্যবহার করে `AzureCliCredential`)।

## উন্নয়ন কর্মপ্রবাহ

### Jupyter নোটবুক চালানো

প্রতিটি পাঠে বিভিন্ন ফ্রেমওয়ার্কের জন্য একাধিক Jupyter নোটবুক থাকে:

১. **Jupyter শুরু করুন:**
   ```bash
   jupyter notebook
   ```

২. **কোনো পাঠের ডিরেক্টরিতে যান** (যেমন `01-intro-to-ai-agents/code_samples/`)

৩. **নোটবুক ওপেন করে চালান:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) ব্যবহার করে
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) ব্যবহার করে

### Microsoft Agent Framework এর সাথে কাজ করা

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure সাবস্ক্রিপশন প্রয়োজন
- Agent Service V2 এর জন্য `FoundryChatClient` ব্যবহার করে (Foundry পোর্টালে এজেন্ট দৃশ্যমান)
- প্রোডাকশন-রেডি বিল্ট-ইন অবজার্ভেবিলিটি সহ
- ফাইল প্যাটার্ন: `*-python-agent-framework.ipynb`

## টেস্ট করার নির্দেশিকা

এটি একটি শিক্ষামূলক রিপোজিটরি যা স্বয়ংক্রিয় পরীক্ষাসমূহ সহ প্রোডাকশন কোড নয়। আপনার সেটআপ ও পরিবর্তন যাচাই করতে:

### ম্যানুয়াল টেস্টিং

১. **Python এনভায়রনমেন্ট টেস্ট করুন:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

২. **নোটবুক কার্যকরীতা টেস্ট করুন:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

৩. **পরিবেশ পরিবর্তনশীল যাচাই করুন:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### পৃথক নোটবুক চালানো

Jupyter এ নোটবুকগুলো খুলে সেল সিকোয়েন্সিয়ালি চালান। প্রতিটি নোটবুক স্ব-বিষয়বস্তু এবং অন্তর্ভুক্ত:
- ইম্পোর্ট বিবৃতি
- কনফিগারেশন লোড
- উদাহরণ স্বরূপ এজেন্ট বাস্তবায়ন
- মার্কডাউন সেলে প্রত্যাশিত আউটপুট

### ডিপ্লয় হওয়া এজেন্টের স্মোক-টেস্টিং

যেসব পাঠে Microsoft Foundry হোস্টেড এজেন্ট হিসেবে এজেন্ট ডিপ্লয় করা হয়েছে (০১, ০৪, ০৫, ১৬), সেখানে রিপোতে পরিবেশন করা হয় স্মোক-টেস্ট ক্যাটালগস `tests/` এ যা `.github/workflows/smoke-test.yml` ওয়ার্কফ্লো মাধ্যমে [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) অ্যাকশনে চালানো হয়। এগুলো একটি হালকা ওজনের পোস্ট-ডিপ্লয় গেট (এজেন্ট কি পৌঁছনীয় এবং বেসিক প্রম্পট প্রত্যাশা মেনে চলছে?), যা পাঠ ১০ এবং ১৬ এর মূল্যায়ন পাইপলাইনের পরিপূরক। ক্যাটালগ-থেকে-পাঠ-থেকে-এজেন্ট ম্যাপিং সম্পর্কে জানতে [tests/README.md](./tests/README.md) দেখুন। পাঠ ১৭ লোকালিতে Foundry Local দিয়ে চলে এবং হোস্টেড এন্ডপয়েন্ট নেই, তাই তার নোটবুক সরাসরি চালিয়ে যাচাই করা হয়।

## কোড স্টাইল

### পাইথন রীতিনীতি

- **Python সংস্করণ**: 3.12+
- **কোড স্টাইল**: স্ট্যান্ডার্ড Python PEP 8 নিয়ম অনুসরণ করুন
- **নোটবুক**: ধারণাসমূহ ব্যাখ্যা করতে পরিষ্কার মার্কডাউন সেল ব্যবহার করুন
- **ইম্পোর্ট**: স্ট্যান্ডার্ড লাইব্রেরি, তৃতীয় পক্ষ, লোকাল ইম্পোর্ট আলাদা করে গ্রুপ করুন

### Jupyter নোটবুক রীতিনীতি

- কোড সেলের আগে বর্ণনামূলক মার্কডাউন সেল অন্তর্ভুক্ত করুন
- রেফারেন্সের জন্য আউটপুট উদাহরণ যোগ করুন
- পাঠের ধারণার সাথে ম্যাচ করা পরিষ্কার ভেরিয়েবল নাম ব্যবহার করুন
- নোটবুক কার্যকরীতা লিনিয়ার রাখুন (সেল ১ → ২ → ৩...)

### ফাইল সংগঠন

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## নির্মাণ ও ডিপ্লয়মেন্ট

### ডকুমেন্টেশন তৈরি

এই রিপোজিটরিতে ডকুমেন্টেশনের জন্য Markdown ব্যবহার করা হয়:
- প্রতিটি পাঠ ফোল্ডারে README.md ফাইল
- মূল README.md রিপোজিটরি রুটে
- GitHub Actions এর মাধ্যমে স্বয়ংক্রিয় অনুবাদ ব্যবস্থা

### CI/CD পাইপলাইন

`.github/workflows/` এ অবস্থিত:

১. **co-op-translator.yml** - ৫০+ ভাষায় স্বয়ংক্রিয় অনুবাদ
২. **welcome-issue.yml** - নতুন ইস্যু নির্মাতাদের স্বাগত
৩. **welcome-pr.yml** - নতুন পুল রিকুয়েস্ট অবদানকারীদের স্বাগত

### ডিপ্লয়মেন্ট

এটি একটি শিক্ষামূলক রিপোজিটরি - কোন ডিপ্লয়মেন্ট প্রক্রিয়া নেই। ব্যবহারকারীরা:
১. রিপোজিটরি ফর্ক বা ক্লোন করুন
২. নোটবুক लोकালি বা GitHub Codespaces এ চালান
৩. উদাহরণ পরিবর্তন ও পরীক্ষা করে শিখুন

## পুল রিকুয়েস্ট নির্দেশিকা

### জমা দেওয়ার আগে

১. **আপনার পরিবর্তন পরীক্ষা করুন:**
   - সংশ্লিষ্ট নোটবুক সম্পূর্ণ চালান
   - সকল সেল ত্রুটিমুক্ত চালানো যাচাই করুন
   - আউটপুট উপযুক্ত কিনা পরীক্ষা করুন

২. **ডকুমেন্টেশন হালনাগাদ:**
   - নতুন ধারণা থাকলে README.md আপডেট করুন
   - জটিল কোডের জন্য নোটবুকে মন্তব্য যোগ করুন
   - মার্কডাউন সেলে উদ্দেশ্য ব্যাখ্যা নিশ্চিত করুন

৩. **ফাইল পরিবর্তন:**
   - `.env` ফাইল কমিট এড়ান (`.env.example` ব্যবহার করুন)
   - `venv/` বা `__pycache__/` ডিরেক্টরি কমিট করবেন না
   - ধারণা ব্যাখ্যা করলে নোটবুক আউটপুট রাখুন
   - সাময়িক ফাইল ও ব্যাকআপ নোটবুক সরান (`*-backup.ipynb`)

### পিআর শিরোনাম ফরম্যাট

বর্ণনামূলক শিরোনাম ব্যবহার করুন:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### প্রয়োজনীয় চেক

- নোটবুক ত্রুটিমুক্ত চালানো উচিত
- README ফাইল পরিষ্কার ও সঠিক হওয়া উচিত
- রিপোজিটরির বিদ্যমান কোড প্যাটার্ন অনুসরণ করুন
- অন্যান্য পাঠের সাথে সামঞ্জস্য বজায় রাখুন

## অতিরিক্ত নোট

### সাধারণ সমস্যাসমূহ

১. **Python সংস্করণ অসামঞ্জস্যতা:**
   - Python 3.12+ ব্যবহার নিশ্চিত করুন
   - কিছু প্যাকেজ পুরনো সংস্করণে কাজ নাও করতে পারে
   - Python সংস্করণ স্পষ্ট করতে `python3 -m venv` ব্যবহার করুন

২. **পরিবেশ পরিবর্তনশীল:**
   - সর্বদা `.env` থেকে `.env.example` তৈরি করুন
   - `.env` ফাইল কমিট করবেন না (এটি `.gitignore` তে রয়েছে)
   - কীবিহীন Entra ID প্রমাণীকরণের জন্য `az login` দিয়ে সাইন ইন করুন

৩. **প্যাকেজ দ্বন্দ্ব:**
   - একটি নতুন ভার্চুয়াল এনভায়রনমেন্ট ব্যবহার করুন
   - পৃথক প্যাকেজের বদলে `requirements.txt` থেকে ইন্সটল করুন
   - কিছু নোটবুকে অতিরিক্ত প্যাকেজ থাকতে পারে যা তাদের মার্কডাউন সেলে উল্লেখ আছে

৪. **Azure সেবা:**
   - Azure AI সেবার জন্য সক্রিয় সাবস্ক্রিপশন প্রয়োজন
   - কিছু বৈশিষ্ট্য অঞ্চল-নির্দিষ্ট হতে পারে
   - আপনার Azure OpenAI মডেল ডিপ্লয়মেন্টকে Responses API সাপোর্ট করতে হবে

### শেখার পথে

পাঠক্রমের প্রস্তাবিত অগ্রগতি:
১. **০০-course-setup** - এনভায়রনমেন্ট সেটআপ শুরু করুন
২. **০১-intro-to-ai-agents** - AI এজেন্টের মৌলিক বিষয়গুলো বুঝুন
৩. **০২-explore-agentic-frameworks** - বিভিন্ন ফ্রেমওয়ার্ক সম্পর্কে জানুন
৪. **০৩-agentic-design-patterns** - মূল ডিজাইন প্যাটার্ন শেখা
৫. ধারাবাহিকভাবে সংখ্যাঙ্কিত পাঠগুলি অনুসরণ করুন

### ফ্রেমওয়ার্ক নির্বাচনের নির্দেশিকা

আপনার লক্ষ্য অনুযায়ী ফ্রেমওয়ার্ক নির্বাচন করুন:
- **সমস্ত পাঠের জন্য**: Microsoft Agent Framework (MAF) এর সাথে `FoundryChatClient`
- **এজেন্ট সার্ভার-সাইডে রেজিস্টার হয়** Microsoft Foundry Agent Service V2 তে এবং Foundry পোর্টালে দৃশ্যমান

### সাহায্য নেওয়া

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)-এ যোগ দিন
- নির্দিষ্ট নির্দেশনার জন্য পাঠের README ফাইল দেখুন
- কোর্স পর্যালোচনার জন্য প্রধান [README.md](./README.md) দেখুন
- বিস্তারিত সেটআপ নির্দেশনার জন্য [Course Setup](./00-course-setup/README.md) দেখুন

### অবদান রাখা

এটি একটি উন্মুক্ত শিক্ষামূলক প্রকল্প। অবদান গ্রহণযোগ্য:
- কোড উদাহরণ উন্নত করা
- টাইপোস বা ত্রুটি সংশোধন করা
- ব্যাখ্যামূলক মন্তব্য যোগ করা
- নতুন পাঠ বিষয় প্রস্তাব করা
- অতিরিক্ত ভাষায় অনুবাদ করা

বর্তমান চাহিদার জন্য [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) দেখুন।

## প্রকল্প-নির্দিষ্ট প্রেক্ষাপট

### বহুভাষী সমর্থন

এই রিপোজিটরিতে একটি স্বয়ংক্রিয় অনুবাদ ব্যবস্থা ব্যবহার হয়:
- ৫০+ ভাষা সমর্থিত
- অনুবাদসমূহ `/translations/<lang-code>/` ডিরেক্টরিতে
- অনুবাদ আপডেটের জন্য GitHub Actions ওয়ার্কফ্লো
- উৎস ফাইলগুলি ইংরেজিতে রিপোজিটরি রুটে

### পাঠের গঠন

প্রতিটি পাঠ নির্দিষ্ট প্যাটার্ন অনুসরণ করে:
১. লিঙ্ক সহ ভিডিও থাম্বনেইল
২. লিখিত পাঠ সামগ্রী (README.md)
৩. বিভিন্ন ফ্রেমওয়ার্কের কোড নমুনা
৪. শেখার উদ্দেশ্য এবং প্রাকশর্তসমূহ
৫. অতিরিক্ত শেখার সম্পদ লিঙ্ককৃত

### কোড নমুনার নামকরণ

ফরম্যাট: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - পাঠ ১, MAF Python
- `14-sequential.ipynb` - পাঠ ১৪, MAF উন্নত প্যাটার্ন
- `16-python-agent-framework.ipynb` - পাঠ ১৬, প্রোডাকশন কাস্টমার-সাপোর্ট এজেন্ট
- `17-local-agent-foundry-local.ipynb` - পাঠ ১৭, লোকাল এজেন্ট with Foundry Local + Qwen

### বিশেষ ডিরেক্টরি

- `translated_images/` - অনুবাদের জন্য লোকালাইজড ছবি
- `images/` - ইংরেজি সামগ্রীর জন্য মূল ছবি
- `.devcontainer/` - VS Code ডেভেলপমেন্ট কনটেইনার কনফিগারেশন
- `.github/` - GitHub Actions ওয়ার্কফ্লো এবং টেমপ্লেট

### ডিপেন্ডেন্সি

মূল প্যাকেজসমূহ `requirements.txt` থেকে:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent প্রোটোকল সমর্থন
- `azure-ai-inference`, `azure-ai-projects` - Azure AI সেবা
- `azure-identity` - Azure প্রমাণীকরণ (AzureCliCredential)
- `azure-search-documents` - Azure AI Search ইন্টিগ্রেশন
- `mcp[cli]` - Model Context Protocol সমর্থন

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->