# কোর্স সেটআপ

## পরিচিতি

এই পাঠে এই কোর্সের কোড নমুনাগুলি কীভাবে চালাতে হয় তা বোঝানো হবে।

## অন্যান্য শিক্ষার্থীদের সাথে যোগ দিন এবং সহায়তা পান

আপনার রিপো ক্লোন করা শুরু করার আগে, সেটআপে কোনও সহায়তা, কোর্স সম্পর্কিত কোনও প্রশ্ন বা অন্যান্য শিক্ষার্থীদের সাথে সংযোগ করার জন্য [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) এ যোগ দিন।

## এই রিপো ক্লোন অথবা ফর্ক করুন

শুরু করার জন্য, দয়া করে GitHub রিপোজিটরি ক্লোন অথবা ফর্ক করুন। এটি আপনাকে কোর্স উপকরণের নিজের সংস্করণ তৈরি করতে সাহায্য করবে যাতে আপনি কোড চালাতে, পরীক্ষা করতে এবং পরিবর্তন করতে পারেন!

এটি করতে <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">রিপো ফর্ক করার জন্য</a> লিঙ্কে ক্লিক করুন

এখন আপনার নিজের এই কোর্সের ফর্ক করা সংস্করণ নিম্নলিখিত লিঙ্কে থাকা উচিত:

![Forked Repo](../../../translated_images/bn/forked-repo.33f27ca1901baa6a.webp)

### শ্যালো ক্লোন (ওয়ার্কশপ / Codespaces-এর জন্য সুপারিশকৃত)

  >পূর্ণ ইতিহাস এবং সব ফাইল ডাউনলোড করলে পুরো রিপোজিটরি অনেক বড় হতে পারে (~৩ জিবি)। আপনি যদি শুধু ওয়ার্কশপে অংশগ্রহণ করেন বা কেবল কয়েকটি পাঠ ফোল্ডারের প্রয়োজন হয়, তাহলে একটি শ্যালো ক্লোন (বা sparse ক্লোন) অনেক কম ডাউনলোড করে।

#### দ্রুত শ্যালো ক্লোন — সর্বনিম্ন ইতিহাস, সব ফাইল

নিচের কমান্ডগুলিতে `<your-username>` আপনার ফর্ক URL (অথবা প্রযোজ্য upstream URL) দিয়ে প্রতিস্থাপন করুন।

শুধুমাত্র সর্বশেষ commit ইতিহাস ক্লোন করতে (ছোট ডাউনলোড):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

নির্দিষ্ট একটি শাখা ক্লোন করতে:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### আংশিক (sparse) ক্লোন — সর্বনিম্ন ব্লব ও শুধুমাত্র নির্বাচিত ফোল্ডারগুলি

এটি আংশিক ক্লোন এবং sparse-checkout ব্যবহার করে (যার জন্য Git 2.25+ এবং আংশিক ক্লোন সমর্থন সহ আধুনিক Git প্রয়োজন):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

রিপো ফোল্ডারে প্রবেশ করুন:

```bash
cd ai-agents-for-beginners
```

তারপর আপনি কোন ফোল্ডারগুলি চান তা নির্দিষ্ট করুন (নিচে উদাহরণে দুটি ফোল্ডার দেখানো হয়েছে):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

ক্লোন এবং ফাইলগুলো যাচাই করার পর, আপনি যদি শুধুমাত্র ফাইল প্রয়োজন এবং স্থান মুক্ত করতে চান (কোনও Git ইতিহাস নয়), তাহলে রিপোজিটরি মেটাডাটা মুছে ফেলুন (💀অপ্রত্যাবর্তনীয় — এতে আপনার সব Git কার্যকারিতা হারাবে):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# পাওয়ারশেল
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ব্যবহারের (স্থানীয় বড় ডাউনলোড এড়াতে সুপারিশকৃত)

- এই রিপোর জন্য [GitHub UI](https://github.com/codespaces) এর মাধ্যমে একটি নতুন Codespace তৈরি করুন।  

- নতুন তৈরি হওয়া Codespace এর টার্মিনালে, উপরের শ্যালো/স্পার্স ক্লোন কমান্ডগুলির একটি চালিয়ে প্রয়োজনীয় পাঠ ফোল্ডারগুলোকে Codespace কর্মস্থলে আনা হবে।
- ঐচ্ছিক: Codespaces এর ভিতরে ক্লোন করার পর, অতিরিক্ত স্থান মুক্ত করার জন্য .git ফোল্ডার মুছে দিন (উপরে মুছে ফেলা কমান্ড দেখুন)।
- লক্ষ্য করুন: যদি আপনি রিপো সরাসরি Codespaces এ খুলতে চান (অতিরিক্ত ক্লোন ছাড়াই), তাহলে সচেতন থাকুন Codespaces ডেভকন্টেনার পরিবেশ গঠন করবে এবং প্রয়োজনে আরো কিছু প্রস্তুতি দিতে পারে।

#### টিপস

- যদি আপনি সম্পাদনা/কমিট করতে চান তাহলে সর্বদা ক্লোন URL আপনার ফর্ক দিয়ে প্রতিস্থাপন করুন।
- পরে যদি আরো ইতিহাস বা ফাইল প্রয়োজন হয়, তবে আপনি সেগুলো fetch করতে পারেন বা sparse-checkout সমন্বয় করে অতিরিক্ত ফোল্ডার অন্তর্ভুক্ত করতে পারেন।

## কোড চালানো

এই কোর্সটি একটি সিরিজ জুপিটার নোটবুক প্রদান করে যা দিয়ে আপনি AI এজেন্ট তৈরি করার হাতে কলম অভিজ্ঞতা পেতে পারেন।

কোড নমুনায় **Microsoft Agent Framework (MAF)** ব্যবহার করা হয়েছে `FoundryChatClient` এর সাথে, যা **Microsoft Foundry** মাধ্যমে **Microsoft Foundry Agent Service V2** (Responses API) এর সাথে সংযুক্ত।

সব পাইথন নোটবুকের নামের শেষে থাকে `*-python-agent-framework.ipynb`।

## প্রয়োজনীয়তা

- Python 3.12+
  - **নোট**: যদি আপনার কাছে Python3.12 ইনস্টল না থাকে, নিশ্চিত করুন এটি ইনস্টল করেছেন। তারপর python3.12 ব্যবহার করে venv তৈরি করুন যাতে requirements.txt ফাইল থেকে সঠিক সংস্করণগুলো ইনস্টল হয়।
  
    >উদাহরণ

    পাইথন venv ডিরেক্টরি তৈরি করুন:

    ```bash
    python -m venv venv
    ```

    তারপর venv পরিবেশ সক্রিয় করুন:

    ```bash
    # জেডএসএইচ/ব্যাশ
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET নমুনাগুলোর জন্য, নিশ্চিত করুন আপনি [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) বা তার পরবর্তী সংস্করণ ইনস্টল করেছেন। তারপর আপনার .NET SDK সংস্করণ পরীক্ষা করুন:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — প্রমাণীকরণের জন্য প্রয়োজন। এটি [aka.ms/installazurecli](https://aka.ms/installazurecli) থেকে ইনস্টল করুন।
- **Azure সাবস্ক্রিপশন** — Microsoft Foundry এবং Microsoft Foundry Agent Service প্রবেশাধিকার জন্য।
- **Microsoft Foundry প্রকল্প** — ডিপ্লয় করা একটি মডেল সহ একটি প্রকল্প (উদাহরণস্বরূপ, `gpt-5-mini`)। দেখুন [Step 1](#ধাপ-১-একটি-microsoft-foundry-প্রকল্প-তৈরি-করুন) নিচে।

এই রিপোজিটরির মূল ফোল্ডারে একটি `requirements.txt` ফাইল রয়েছে যা কোড নমুনা চালাতে সব প্রয়োজনীয় পাইথন প্যাকেজ অন্তর্ভুক্ত করে।

আপনি এগুলো ইনস্টল করতে পারেন নিম্নলিখিত কমান্ড টার্মিনালে রান করে:

```bash
pip install -r requirements.txt
```

আমরা সুপারিশ করি আপনি পাইথন ভার্চুয়াল পরিবেশ তৈরি করুন যাতে কোনো দ্বন্দ্ব বা সমস্যা না হয়।

## VSCode সেটআপ

নিশ্চিত করুন আপনি VSCode এ সঠিক পাইথন সংস্করণ ব্যবহার করছেন।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry এবং Microsoft Foundry Agent Service সেটআপ

### ধাপ ১: একটি Microsoft Foundry প্রকল্প তৈরি করুন

নোটবুকগুলি চালাতে আপনাকে একটি Microsoft Foundry **হাব** এবং **প্রকল্প** প্রয়োজন যার মডেল ডিপ্লয় করা আছে।

১. [ai.azure.com](https://ai.azure.com) এ যান এবং আপনার Azure একাউন্ট দিয়ে সাইন ইন করুন।
২. একটি **হাব** তৈরি করুন (অথবা বিদ্যমান একটি ব্যবহার করুন)। দেখুন: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)।
৩. হাবের ভিতরে একটি **প্রকল্প** তৈরি করুন।
৪. **Models + Endpoints** থেকে একটি মডেল ডিপ্লয় করুন (যেমন, `gpt-5-mini`)।

### ধাপ ২: আপনার প্রকল্পের endpoint এবং মডেল ডিপ্লয়মেন্ট নাম সংগ্রহ করুন

Microsoft Foundry পোর্টালের আপনার প্রকল্প থেকে:

- **Project Endpoint** — **Overview** পেজে যান এবং endpoint URL কপি করুন।

![Project Connection String](../../../translated_images/bn/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** এ যান, আপনার ডিপ্লয় করা মডেল নির্বাচন করুন এবং **Deployment name** (যেমন, `gpt-5-mini`) নোট করুন।

### ধাপ ৩: `az login` দিয়ে Azure এ সাইন ইন করুন

অধিকাংশ নোটবুক আপনার **Azure CLI সাইন ইন** এর মাধ্যমে প্রমাণীকরণ করে — `azure-identity` প্যাকেজ থেকে `AzureCliCredential` বা `DefaultAzureCredential` (যা আপনার `az login` সেশনকে ধরে নেয়) ব্যবহার করে — তাই API কী প্রয়োজন হয় না। কিছু পাঠ এবং ঐচ্ছিক ইন্টিগ্রেশন API কী ব্যবহার করে; অতিরিক্ত পরিবেশ ভেরিয়েবল জন্য প্রতিটি পাঠের পূর্বশর্ত পরীক্ষা করুন। এর জন্য Azure CLI দিয়ে সাইন ইন থাকা আবশ্যক।

১. **Azure CLI ইনস্টল করুন** যদি আগে করা না থাকে: [aka.ms/installazurecli](https://aka.ms/installazurecli)

২. **সাইন ইন করুন** নীচের কমান্ড চালিয়ে:

    ```bash
    az login
    ```

    অথবা আপনি যদি ব্রাউজার ছাড়া দূরবর্তী/Codespace পরিবেশে থাকেন:

    ```bash
    az login --use-device-code
    ```

৩. **আপনার সাবস্ক্রিপশন নির্বাচন করুন** যদি প্রম্পট আসে — আপনার Foundry প্রকল্পের অন্তর্গত সাবস্ক্রিপশন বেছে নিন।

৪. **সাইন ইন নিশ্চিত করুন**:

    ```bash
    az account show
    ```

> **কেন `az login`?** নোটবুকগুলি `azure-identity` প্যাকেজ থেকে `AzureCliCredential` (অথবা `DefaultAzureCredential`, যা আপনার Azure CLI সাইন ইনও নেয়) ব্যবহার করে প্রমাণীকরণ করে। এর মানে আপনার Azure CLI সেশন হল ক্রেডেনশিয়ালস — আপনার `.env` ফাইলে কোনও API কী বা সিক্রেট প্রয়োজন হয় না। এটি একটি [সুরক্ষা সেরা অনুশীলন](https://learn.microsoft.com/azure/developer/ai/keyless-connections)।

### ধাপ ৪: আপনার `.env` ফাইল তৈরি করুন

উদাহরণ ফাইলটি কপি করুন:

```bash
# জেডএসএইচ/বাশ
cp .env.example .env
```

```powershell
# পাওয়ারশেল
Copy-Item .env.example .env
```

`.env` ফাইল খুলুন এবং নিচের দুটো মান পূরণ করুন:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| ভেরিয়েবল | কোথায় পাবেন |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry পোর্টাল → আপনার প্রকল্প → **Overview** পাতা |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry পোর্টাল → **Models + Endpoints** → আপনার ডিপ্লয়কৃত মডেলের নাম |

অধিকাংশ পাঠের জন্য এটুকুই যথেষ্ট! নোটবুকগুলি স্বয়ংক্রিয়ভাবে আপনার `az login` সেশন দিয়ে প্রমাণীকরণ করবে।

### ধাপ ৫: পাইথন নির্ভরতা ইনস্টল করুন

```bash
pip install -r requirements.txt
```

আমরা সুপারিশ করি এটি আপনি পূর্বে তৈরি ভার্চুয়াল পরিবেশের ভিতরে চালান।

## ঐচ্ছিক সেটআপ: Azure AI Search (পাঠ ৫ এবং ১৬)

পাঠ ৫ (Agentic RAG) এবং পাঠ ১৬ নোটবুকগুলি ইন-মেমোরি নলেজ বেস দিয়ে স্বয়ংক্রিয়ভাবে চলে — অতিরিক্ত Azure রিসোর্স প্রয়োজন হয় না। আপনি যদি এগুলোকে একটি বাস্তব **Azure AI Search** ইনডেক্স দিয়ে বেক করতে চান, বুঝে নিন যে **পাঠ ১৬ নোটবুক বর্তমানে কী-ভিত্তিক প্রমাণীকরণ ব্যবহার করে**: এটি ইন-মেমোরি সার্চ থেকে Azure AI Search এ পরিবর্তিত হয় শুধুমাত্র যখন **উভয়** `AZURE_SEARCH_SERVICE_ENDPOINT` **এবং** `AZURE_SEARCH_API_KEY` সেট থাকে, অন্যথায় এটি ইন-মেমোরি সার্চ চালিয়ে যায় — তাই একটি বাস্তব ইনডেক্সের জন্য আপনাকে অ্যাডমিন কীও সেট করতে হবে। মাইক্রোসফট এন্ত্রা ID (RBAC) ব্যবহার করে কীলেস প্রমাণীকরণ আপনার নিজস্ব প্রোডাকশন কোডের জন্য সুপারিশকৃত পন্থা, যা এই কোর্সের অন্যত্র ব্যবহৃত `az login` ফ্লোর সাথে সামঞ্জস্যপূর্ণ।

নিচের RBAC ধাপগুলি গাইড নমুনাগুলোর এবং আপনার নিজস্ব কোডের জন্য প্রযোজ্য। এগুলো পাঠ ১৬ নোটবুকে কীলেস প্রমাণীকরণ সক্রিয় করে না; পাঠ ১৬ এখনও Azure AI Search ব্যবহারের জন্য উভয় endpoint এবং অ্যাডমিন কী প্রয়োজন।

১. আপনার সার্চ সার্ভিসে **রোল-বেইজড এক্সেস** সক্ষম করুন:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

২. নিজের জন্য প্রয়োজনীয় রোলগুলি বরাদ্দ করুন (ইনডেক্স তৈরি/লোড এবং কোয়েরি):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

৩. `.env` ফাইলে endpoint যোগ করুন:

| ভেরিয়েবল | কোথায় পাবেন |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure পোর্টাল → আপনার **Azure AI Search** রিসোর্স → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | প্রয়োজন (endpoint এর সাথে) পাঠ ১৬ নোটবুকে Azure AI Search চালানোর জন্য, যা কী-ভিত্তিক প্রমাণীকরণ ব্যবহার করে। Azure পোর্টাল → **Settings** → **Keys** → প্রাথমিক অ্যাডমিন কী |

> **কেন কীলেস?** অ্যাডমিন কী আপনাকে সম্পূর্ণ লিখনাধিকার দেয় এবং `.env` ফাইলে ফাঁস হতে পারে। RBAC এর মাধ্যমে আপনার `az login` পরিচয় ব্যবহার হয় — কোর্স নোটবুকগুলিও এই কীলেস এন্ত্রা ID প্যাটার্ন ব্যবহার করে (`AzureCliCredential` / `DefaultAzureCredential` ব্যবহার করে)। দেখুন [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

পূর্ণ ইনডেক্স-তৈরি নমুনার জন্য [Azure AI Search সেটআপ গাইড](./AzureSearch.md) দেখুন পাইথন এবং .NET এ।

## অতিরিক্ত সেটআপ যা সরাসরি Azure OpenAI কল করে (পাঠ ৬ এবং ৮)

পাঠ ৬ এবং ৮ এর কিছু নোটবুকে সরাসরি **Azure OpenAI** কল করা হয় (Response API ব্যবহার করে) Microsoft Foundry প্রকল্পের মাধ্যমে না গিয়ে। এই নমুনাগুলো আগে GitHub Models ব্যবহার করতো, যা অবলুপ্ত এবং Response API সমর্থন করে না। আপনার `.env` ফাইলে এই ভেরিয়েবলগুলো যোগ করুন:

| ভেরিয়েবল | কোথায় পাবেন |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure পোর্টাল → আপনার **Azure OpenAI** রিসোর্স → **Keys and Endpoint** → Endpoint (যেমন `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | আপনার ডিপ্লয় করা মডেলের নাম (যেমন `gpt-5-mini`) যা Response API সমর্থন করে |
| `AZURE_OPENAI_API_KEY` | ঐচ্ছিক — শুধুমাত্র যদি আপনি কী-ভিত্তিক প্রমাণীকরণ ব্যবহার করেন `az login` / এন্ত্রা ID পরিবর্তে |

> Response API স্থিতিশীল `/openai/v1/` endpoint ব্যবহার করে, তাই `api-version` প্রয়োজন নেই। কীলেস এন্ত্রা ID প্রমাণীকরণের জন্য `az login` ব্যবহার করে সাইন ইন করুন।

## বিকল্প প্রদানকারী: MiniMax (OpenAI-Compatible)

[MiniMax](https://platform.minimaxi.com/) বড় প্রসঙ্গ মডেল প্রদান করে (২০৪কে টোকেন পর্যন্ত) OpenAI-অনুকূল API দিয়ে। Microsoft Agent Framework এর `OpenAIChatClient` যেকোন OpenAI-অনুকূল endpoint এর সাথে কাজ করে, তাই আপনি MiniMax ব্যবহার করতে পারেন `OpenAIChatClient` ব্যবহার করে পাঠগুলোর জন্য একটি বিকল্প হিসেবে।

আপনার `.env` ফাইলে এই ভেরিয়েবলগুলো যোগ করুন:

| ভেরিয়েবল | কোথায় পাবেন |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API কী |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` ব্যবহার করুন (ডিফল্ট মান) |
| `MINIMAX_MODEL_ID` | ব্যবহার করার মডেলের নাম (যেমন, `MiniMax-M3`) |

**উদাহরণ মডেল**: `MiniMax-M3` (সুপারিশকৃত), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (দ্রুত রেসপন্স)। মডেলের নাম এবং উপলভ্যতা সময়ে সময়ে পরিবর্তিত হতে পারে, এবং একটি মডেলের অ্যাক্সেস আপনার অ্যাকাউন্টের ওপর নির্ভর করে।

`OpenAIChatClient` ব্যবহার করে কোড নমুনাগুলি (যেমন পাঠ ১৪ হোটেল বুকিং ওয়ার্কফ্লো) স্বয়ংক্রিয়ভাবে আপনার MiniMax কনফিগারেশন সনাক্ত করবে যখন `MINIMAX_API_KEY` সেট থাকে।


## বিকল্প প্রদানকারী: Novita AI (OpenAI-সাপোর্টেড)

[Novita AI](https://novita.ai/llm-api) ওপেন-সোর্স এবং ফ্রন্টিয়ার LLMs (DeepSeek, Llama, Qwen, এবং আরও অনেক কিছু) এর জন্য OpenAI-সাপোর্টেড API প্রদান করে। যেহেতু Microsoft Agent Framework এর `OpenAIChatClient` যেকোন OpenAI-সাপোর্টেড endpoint এর সাথে কাজ করে, আপনি Novita AI কে Azure OpenAI বা OpenAI এর বিকল্প হিসেবে ব্যবহার করতে পারেন।

আপনার `.env` ফাইলে নিম্নলিখিত ভেরিয়েবলগুলো যোগ করুন:

| ভেরিয়েবল | কোথায় পাবেন |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | `https://api.novita.ai/openai/v1` ব্যবহার করুন (ডিফল্ট মান) |
| `NOVITA_MODEL_ID` | ব্যবহারের জন্য মডেল নাম (যেমন, `moonshotai/kimi-k3`) |

**উদাহরণ মডেল**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`। Novita AI আরও অনেক ওপেন-সোর্স মডেল পরিবার (Llama, Qwen, GLM, এবং আরও) হোস্ট করে — বর্তমান উপলব্ধ মডেল এবং তাদের মডেল আইডি দেখতে [Novita AI মডেল লাইব্রেরি](https://novita.ai/llm-api) দেখুন।

বর্তমান স্যাম্পলগুলো স্বয়ংক্রিয়ভাবে `NOVITA_*` ভেরিয়েবলগুলো ব্যবহার করে না। Novita AI ব্যবহার করতে, আপনি চালানো স্যাম্পলে `OpenAIChatClient` তৈরি করার সময় এই মানগুলো স্পষ্টভাবে দিন।

## বিকল্প প্রদানকারী: Foundry Local (ডিভাইসে মডেল চালান)

[Foundry Local](https://foundrylocal.ai) হল একটি হালকা রানটাইম যা OpenAI-সাপোর্টেড API এর মাধ্যমে সম্পূর্ণরূপে **আপনার নিজস্ব মেশিনে** ভাষার মডেলগুলো ডাউনলোড, ম্যানেজ এবং সার্ভ করে — কোনো ক্লাউডের প্রয়োজন নেই।

যেহেতু Microsoft Agent Framework এর `OpenAIChatClient` যেকোন OpenAI-সাপোর্টেড endpoint এর সাথে কাজ করে, Foundry Local হল Azure OpenAI এর একটি লোকাল বিকল্প।

**1. Foundry Local ইনস্টল করুন**

```bash
# উইন্ডোজ
winget install Microsoft.FoundryLocal

# ম্যাকওএস
brew install foundrylocal
```

**2. একটি মডেল ডাউনলোড এবং চালান** (এটি লোকাল সার্ভিসও শুরু করবে):

```bash
foundry model list          # উপলব্ধ মডেলগুলি দেখুন
foundry model run phi-4-mini
```

**3. স্থানীয় endpoint আবিষ্কার করতে ব্যবহৃত Python SDK ইনস্টল করুন:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework কে আপনার লোকাল মডেলের দিকে নির্দেশ করুন:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# মডেলটি স্থানীয়ভাবে ডাউনলোড (প্রয়োজনে) এবং পরিবেশন করে, তারপর এন্ডপয়েন্ট/পোর্ট খুঁজে বের করে।
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # যেমন http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local এর জন্য সবসময় "not-required"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **টীপ:** Foundry Local একটি OpenAI-সাপোর্টেড **Chat Completions** endpoint এক্সপোজ করে। লোকাল ডেভেলপমেন্ট এবং অফলাইন কাজে এটি ব্যবহার করুন। পূর্ণ **Responses API** ফিচার সেটের জন্য (স্টেটফুল কথোপকথন ইত্যাদি), Azure OpenAI অথবা Microsoft Foundry প্রজেক্ট ব্যবহার করুন।

## পাঠ ৮ এর জন্য অতিরিক্ত সেটআপ (Bing Grounding Workflow)

পাঠ ৮ এর শর্তাধীন workflow নোটবুক Microsoft Foundry এর মাধ্যমে **Bing grounding** ব্যবহার করে। আপনি যদি ওই স্যাম্পল চালানোর পরিকল্পনা করেন, আপনার `.env` ফাইলে এই ভেরিয়েবলটি যোগ করুন:

| ভেরিয়েবল | কোথায় পাবেন |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry পোর্টাল → আপনার প্রজেক্ট → **Management** → **Connected resources** → আপনার Bing সংযোগ → সংযোগ আইডি কপি করুন |

## সমস্যা সমাধান

### macOS-এ SSL সার্টিফিকেট যাচাইকরণ ত্রুটি

আপনি যদি macOS তে নিম্নরূপ ত্রুটি পান:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

এটি macOS এ Python এর একটি পরিচিত সমস্যা যেখানে সিস্টেম SSL সার্টিফিকেট স্বয়ংক্রিয়ভাবে বিশ্বাসযোগ্য হয় না। নিম্নলিখিত সমাধানগুলো ক্রমান্বয়ে চেষ্টা করুন:

**অপশন ১: Python এর Install Certificates স্ক্রিপ্ট চালান (প্রস্তাবিত)**

```bash
# আপনার ইনস্টল করা পাইথন সংস্করণ দিয়ে 3.XX প্রতিস্থাপন করুন (যেমন, 3.12 অথবা 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**অপশন ২: আপনার নোটবুকে `connection_verify=False` ব্যবহার করুন (শুধুমাত্র GitHub Models নোটবুকগুলোর জন্য)**

পাঠ ৬ এর নোটবুকে (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) একটি কমেন্ট করা workaround ইতিমধ্যে আছে। সার্টিফিকেট ত্রুটি পেলে `connection_verify=False` আনকমেন্ট করুন:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # যদি আপনি সার্টিফিকেট ত্রুটি সম্মুখীন হন তবে SSL যাচাইকরণ অক্ষম করুন
)
```

> **⚠️ সতর্কতা:** SSL যাচাইকরণ নিষ্ক্রিয় করা (`connection_verify=False`) নিরাপত্তা হ্রাস করে কারণ এটি সার্টিফিকেট যাচাইকরণ এড়িয়ে চলে। এটি শুধুমাত্র ডেভেলপমেন্ট পরিবেশে অস্থায়ী সমাধান হিসেবে ব্যবহার করুন। প্রোডাকশনে কখনোই ব্যবহার করবেন না।

**অপশন ৩: `truststore` ইনস্টল করে ব্যবহার করুন**

```bash
pip install truststore
```

তারপর নেটওয়ার্ক কল করার আগে আপনার নোটবুক অথবা স্ক্রিপ্টের সর্বোচ্চ অংশে নিম্নলিখিত কোড যোগ করুন:

```python
import truststore
truststore.inject_into_ssl()
```

## কোথাও আটকে গেছেন?

যদি এই সেটআপ চালাতে কোনো সমস্যা হয়, আমাদের <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI কমিউনিটি ডিসকর্ড</a> এ প্রবেশ করুন অথবা <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ইস্যু তৈরি করুন</a>।

## পরবর্তী পাঠ

আপনি এখন এই পাঠ্যক্রমের কোড চালানোর জন্য প্রস্তুত। AI এজেন্টের দুনিয়া সম্পর্কে আরও শেখার জন্য শুভ কামনা!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->