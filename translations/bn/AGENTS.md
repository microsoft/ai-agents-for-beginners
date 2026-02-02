# AGENTS.md

## প্রকল্পের সংক্ষিপ্ত বিবরণ

এই রিপোজিটরিতে "AI Agents for Beginners" অন্তর্ভুক্ত রয়েছে - একটি ব্যাপক শিক্ষামূলক কোর্স যা AI এজেন্ট তৈরি করার জন্য প্রয়োজনীয় সবকিছু শেখায়। কোর্সটি ১৫+ পাঠ নিয়ে গঠিত, যেখানে মৌলিক বিষয়, ডিজাইন প্যাটার্ন, ফ্রেমওয়ার্ক এবং AI এজেন্টের প্রোডাকশন ডিপ্লয়মেন্ট কভার করা হয়েছে।

**মূল প্রযুক্তি:**
- Python 3.12+
- ইন্টারঅ্যাকটিভ লার্নিংয়ের জন্য Jupyter Notebooks
- AI ফ্রেমওয়ার্ক: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI Services: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (ফ্রি টিয়ার উপলব্ধ)

**আর্কিটেকচার:**
- পাঠ-ভিত্তিক কাঠামো (00-15+ ডিরেক্টরি)
- প্রতিটি পাঠে রয়েছে: README ডকুমেন্টেশন, কোড নমুনা (Jupyter notebooks), এবং ছবি
- স্বয়ংক্রিয় অনুবাদ ব্যবস্থার মাধ্যমে বহু-ভাষার সমর্থন
- প্রতিটি পাঠে একাধিক ফ্রেমওয়ার্ক অপশন (Semantic Kernel, AutoGen, Azure AI Agent Service)

## সেটআপ কমান্ড

### প্রয়োজনীয়তা
- Python 3.12 বা তার বেশি
- GitHub অ্যাকাউন্ট (GitHub Models - ফ্রি টিয়ার)
- Azure সাবস্ক্রিপশন (ঐচ্ছিক, Azure AI পরিষেবার জন্য)

### প্রাথমিক সেটআপ

1. **রিপোজিটরি ক্লোন বা ফর্ক করুন:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python ভার্চুয়াল এনভায়রনমেন্ট তৈরি এবং সক্রিয় করুন:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **ডিপেনডেন্সি ইনস্টল করুন:**
   ```bash
   pip install -r requirements.txt
   ```

4. **এনভায়রনমেন্ট ভেরিয়েবল সেট করুন:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### প্রয়োজনীয় এনভায়রনমেন্ট ভেরিয়েবল

**GitHub Models (ফ্রি)** এর জন্য:
- `GITHUB_TOKEN` - GitHub থেকে পার্সোনাল অ্যাক্সেস টোকেন

**Azure AI Services** (ঐচ্ছিক) এর জন্য:
- `PROJECT_ENDPOINT` - Azure AI Foundry প্রকল্পের এন্ডপয়েন্ট
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API কী
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI এন্ডপয়েন্ট URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - চ্যাট মডেলের জন্য ডিপ্লয়মেন্ট নাম
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - এমবেডিংয়ের জন্য ডিপ্লয়মেন্ট নাম
- `.env.example` এ দেখানো অতিরিক্ত Azure কনফিগারেশন

## ডেভেলপমেন্ট ওয়ার্কফ্লো

### Jupyter Notebooks চালানো

প্রতিটি পাঠে বিভিন্ন ফ্রেমওয়ার্কের জন্য একাধিক Jupyter notebook রয়েছে:

1. **Jupyter শুরু করুন:**
   ```bash
   jupyter notebook
   ```

2. **একটি পাঠের ডিরেক্টরিতে যান** (যেমন, `01-intro-to-ai-agents/code_samples/`)

3. **নোটবুক খুলুন এবং চালান:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel ফ্রেমওয়ার্ক ব্যবহার করে
   - `*-autogen.ipynb` - AutoGen ফ্রেমওয়ার্ক ব্যবহার করে
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) ব্যবহার করে
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) ব্যবহার করে
   - `*-azureaiagent.ipynb` - Azure AI Agent Service ব্যবহার করে

### বিভিন্ন ফ্রেমওয়ার্ক নিয়ে কাজ করা

**Semantic Kernel + GitHub Models:**
- GitHub অ্যাকাউন্টের সাথে ফ্রি টিয়ার উপলব্ধ
- শেখা এবং পরীক্ষার জন্য ভালো
- ফাইল প্যাটার্ন: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- GitHub অ্যাকাউন্টের সাথে ফ্রি টিয়ার উপলব্ধ
- মাল্টি-এজেন্ট অর্কেস্ট্রেশন ক্ষমতা
- ফাইল প্যাটার্ন: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoft-এর সর্বশেষ ফ্রেমওয়ার্ক
- Python এবং .NET-এ উপলব্ধ
- ফাইল প্যাটার্ন: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azure সাবস্ক্রিপশন প্রয়োজন
- প্রোডাকশন-রেডি বৈশিষ্ট্য
- ফাইল প্যাটার্ন: `*-azureaiagent.ipynb`

## টেস্টিং নির্দেশনা

এটি একটি শিক্ষামূলক রিপোজিটরি, যেখানে উদাহরণ কোড রয়েছে, প্রোডাকশন কোড নয়। স্বয়ংক্রিয় টেস্টের পরিবর্তে সেটআপ এবং পরিবর্তন যাচাই করতে:

### ম্যানুয়াল টেস্টিং

1. **Python এনভায়রনমেন্ট পরীক্ষা করুন:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **নোটবুক এক্সিকিউশন পরীক্ষা করুন:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **এনভায়রনমেন্ট ভেরিয়েবল যাচাই করুন:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### পৃথক নোটবুক চালানো

Jupyter-এ নোটবুক খুলুন এবং সেলগুলো ধারাবাহিকভাবে চালান। প্রতিটি নোটবুক স্বয়ংসম্পূর্ণ এবং অন্তর্ভুক্ত করে:
- ইমপোর্ট স্টেটমেন্ট
- কনফিগারেশন লোডিং
- এজেন্টের উদাহরণ বাস্তবায়ন
- Markdown সেলে প্রত্যাশিত আউটপুট

## কোড স্টাইল

### Python কনভেনশন

- **Python ভার্সন**: 3.12+
- **কোড স্টাইল**: স্ট্যান্ডার্ড Python PEP 8 কনভেনশন অনুসরণ করুন
- **নোটবুক**: ধারণা ব্যাখ্যা করার জন্য পরিষ্কার Markdown সেল ব্যবহার করুন
- **ইমপোর্ট**: স্ট্যান্ডার্ড লাইব্রেরি, থার্ড-পার্টি, এবং লোকাল ইমপোর্ট দ্বারা গ্রুপ করুন

### Jupyter Notebook কনভেনশন

- কোড সেলের আগে বর্ণনামূলক Markdown সেল অন্তর্ভুক্ত করুন
- রেফারেন্সের জন্য নোটবুকে আউটপুট উদাহরণ যোগ করুন
- পাঠের ধারণার সাথে মিল রেখে পরিষ্কার ভেরিয়েবল নাম ব্যবহার করুন
- নোটবুক এক্সিকিউশন অর্ডার লিনিয়ার রাখুন (সেল ১ → ২ → ৩...)

### ফাইল সংগঠন

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## বিল্ড এবং ডিপ্লয়মেন্ট

### ডকুমেন্টেশন তৈরি

এই রিপোজিটরি Markdown ব্যবহার করে ডকুমেন্টেশন তৈরি করে:
- প্রতিটি পাঠের ফোল্ডারে README.md ফাইল
- রিপোজিটরির মূল README.md
- GitHub Actions এর মাধ্যমে স্বয়ংক্রিয় অনুবাদ ব্যবস্থা

### CI/CD পাইপলাইন

`.github/workflows/` এ অবস্থিত:

1. **co-op-translator.yml** - ৫০+ ভাষায় স্বয়ংক্রিয় অনুবাদ
2. **welcome-issue.yml** - নতুন ইস্যু ক্রিয়েটরদের স্বাগত জানায়
3. **welcome-pr.yml** - নতুন পুল রিকোয়েস্ট কন্ট্রিবিউটরদের স্বাগত জানায়

### ডিপ্লয়মেন্ট

এটি একটি শিক্ষামূলক রিপোজিটরি - কোনো ডিপ্লয়মেন্ট প্রক্রিয়া নেই। ব্যবহারকারীরা:
1. রিপোজিটরি ফর্ক বা ক্লোন করুন
2. নোটবুক স্থানীয়ভাবে বা GitHub Codespaces-এ চালান
3. উদাহরণ পরিবর্তন এবং পরীক্ষা করে শিখুন

## পুল রিকোয়েস্ট নির্দেশিকা

### জমা দেওয়ার আগে

1. **আপনার পরিবর্তন পরীক্ষা করুন:**
   - প্রভাবিত নোটবুক সম্পূর্ণ চালান
   - নিশ্চিত করুন যে সব সেল কোনো ত্রুটি ছাড়াই এক্সিকিউট হয়
   - আউটপুট যথাযথ কিনা যাচাই করুন

2. **ডকুমেন্টেশন আপডেট:**
   - নতুন ধারণা যোগ করলে README.md আপডেট করুন
   - জটিল কোডের জন্য নোটবুকে মন্তব্য যোগ করুন
   - Markdown সেলে উদ্দেশ্য ব্যাখ্যা নিশ্চিত করুন

3. **ফাইল পরিবর্তন:**
   - `.env` ফাইল কমিট করবেন না (`.env.example` ব্যবহার করুন)
   - `venv/` বা `__pycache__/` ডিরেক্টরি কমিট করবেন না
   - ধারণা প্রদর্শনের জন্য নোটবুক আউটপুট রাখুন
   - অস্থায়ী ফাইল এবং ব্যাকআপ নোটবুক (`*-backup.ipynb`) সরিয়ে ফেলুন

### PR শিরোনামের ফরম্যাট

বর্ণনামূলক শিরোনাম ব্যবহার করুন:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### প্রয়োজনীয় চেক

- নোটবুক ত্রুটি ছাড়াই এক্সিকিউট হওয়া উচিত
- README ফাইলগুলো পরিষ্কার এবং সঠিক হওয়া উচিত
- রিপোজিটরির বিদ্যমান কোড প্যাটার্ন অনুসরণ করুন
- অন্যান্য পাঠের সাথে সামঞ্জস্য বজায় রাখুন

## অতিরিক্ত নোট

### সাধারণ সমস্যাগুলো

1. **Python ভার্সন মিসম্যাচ:**
   - Python 3.12+ ব্যবহার নিশ্চিত করুন
   - কিছু প্যাকেজ পুরোনো ভার্সনে কাজ নাও করতে পারে
   - `python3 -m venv` ব্যবহার করে Python ভার্সন স্পষ্টভাবে নির্দিষ্ট করুন

2. **এনভায়রনমেন্ট ভেরিয়েবল:**
   - সর্বদা `.env.example` থেকে `.env` তৈরি করুন
   - `.env` ফাইল কমিট করবেন না (এটি `.gitignore`-এ রয়েছে)
   - GitHub টোকেনের যথাযথ অনুমতি প্রয়োজন

3. **প্যাকেজ কনফ্লিক্ট:**
   - একটি নতুন ভার্চুয়াল এনভায়রনমেন্ট ব্যবহার করুন
   - পৃথক প্যাকেজের পরিবর্তে `requirements.txt` থেকে ইনস্টল করুন
   - কিছু নোটবুকে তাদের Markdown সেলে উল্লেখিত অতিরিক্ত প্যাকেজ প্রয়োজন হতে পারে

4. **Azure পরিষেবা:**
   - Azure AI পরিষেবার জন্য সক্রিয় সাবস্ক্রিপশন প্রয়োজন
   - কিছু বৈশিষ্ট্য অঞ্চল-নির্দিষ্ট
   - GitHub Models-এর ফ্রি টিয়ার সীমাবদ্ধতা প্রযোজ্য

### শেখার পথ

পাঠক্রমের প্রস্তাবিত অগ্রগতি:
1. **00-course-setup** - পরিবেশ সেটআপের জন্য এখানে শুরু করুন
2. **01-intro-to-ai-agents** - AI এজেন্টের মৌলিক বিষয় বুঝুন
3. **02-explore-agentic-frameworks** - বিভিন্ন ফ্রেমওয়ার্ক সম্পর্কে জানুন
4. **03-agentic-design-patterns** - মূল ডিজাইন প্যাটার্ন
5. ক্রমানুসারে নম্বরযুক্ত পাঠগুলো চালিয়ে যান

### ফ্রেমওয়ার্ক নির্বাচন

আপনার লক্ষ্য অনুযায়ী ফ্রেমওয়ার্ক নির্বাচন করুন:
- **শেখা/প্রোটোটাইপিং**: Semantic Kernel + GitHub Models (ফ্রি)
- **মাল্টি-এজেন্ট সিস্টেম**: AutoGen
- **সর্বশেষ বৈশিষ্ট্য**: Microsoft Agent Framework (MAF)
- **প্রোডাকশন ডিপ্লয়মেন্ট**: Azure AI Agent Service

### সাহায্য পাওয়া

- [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)-এ যোগ দিন
- নির্দিষ্ট নির্দেশনার জন্য পাঠের README ফাইলগুলো পর্যালোচনা করুন
- কোর্সের সংক্ষিপ্ত বিবরণের জন্য মূল [README.md](./README.md) দেখুন
- বিস্তারিত সেটআপ নির্দেশনার জন্য [Course Setup](./00-course-setup/README.md) দেখুন

### অবদান রাখা

এটি একটি ওপেন শিক্ষামূলক প্রকল্প। অবদান স্বাগত:
- কোড উদাহরণ উন্নত করুন
- টাইপো বা ত্রুটি সংশোধন করুন
- স্পষ্টতামূলক মন্তব্য যোগ করুন
- নতুন পাঠ বিষয়ের প্রস্তাব দিন
- অতিরিক্ত ভাষায় অনুবাদ করুন

বর্তমান প্রয়োজনের জন্য [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) দেখুন।

## প্রকল্প-নির্দিষ্ট প্রসঙ্গ

### বহু-ভাষার সমর্থন

এই রিপোজিটরি একটি স্বয়ংক্রিয় অনুবাদ ব্যবস্থা ব্যবহার করে:
- ৫০+ ভাষা সমর্থিত
- `/translations/<lang-code>/` ডিরেক্টরিতে অনুবাদ
- GitHub Actions ওয়ার্কফ্লো অনুবাদ আপডেট পরিচালনা করে
- মূল ফাইলগুলো ইংরেজিতে রিপোজিটরির মূল অংশে রয়েছে

### পাঠের কাঠামো

প্রতিটি পাঠ একটি ধারাবাহিক প্যাটার্ন অনুসরণ করে:
1. ভিডিও থাম্বনেইল লিঙ্ক সহ
2. লিখিত পাঠের বিষয়বস্তু (README.md)
3. একাধিক ফ্রেমওয়ার্কে কোড নমুনা
4. শেখার লক্ষ্য এবং প্রয়োজনীয়তা
5. অতিরিক্ত শেখার সংস্থান লিঙ্ক

### কোড নমুনার নামকরণ

ফরম্যাট: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - পাঠ ৪, Semantic Kernel
- `07-autogen.ipynb` - পাঠ ৭, AutoGen
- `14-python-agent-framework.ipynb` - পাঠ ১৪, MAF Python
- `14-dotnet-agent-framework.ipynb` - পাঠ ১৪, MAF .NET

### বিশেষ ডিরেক্টরি

- `translated_images/` - অনুবাদের জন্য স্থানীয়কৃত ছবি
- `images/` - ইংরেজি বিষয়বস্তুর মূল ছবি
- `.devcontainer/` - VS Code ডেভেলপমেন্ট কন্টেইনার কনফিগারেশন
- `.github/` - GitHub Actions ওয়ার্কফ্লো এবং টেমপ্লেট

### ডিপেনডেন্সি

`requirements.txt` থেকে মূল প্যাকেজ:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen ফ্রেমওয়ার্ক
- `semantic-kernel` - Semantic Kernel ফ্রেমওয়ার্ক
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI পরিষেবা
- `azure-search-documents` - Azure AI Search ইন্টিগ্রেশন
- `chromadb` - RAG উদাহরণের জন্য ভেক্টর ডাটাবেস
- `chainlit` - চ্যাট UI ফ্রেমওয়ার্ক
- `browser_use` - এজেন্টের জন্য ব্রাউজার অটোমেশন
- `mcp[cli]` - Model Context Protocol সমর্থন
- `mem0ai` - এজেন্টের জন্য মেমরি ব্যবস্থাপনা

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। এর মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।