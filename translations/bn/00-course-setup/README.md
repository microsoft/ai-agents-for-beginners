# কোর্স সেটআপ

## পরিচিতি

এই পাঠে কিভাবে এই কোর্সের কোড নমুনাগুলো চালাতে হয় তা আচ্ছাদন করা হবে।

## অন্যান্য শিক্ষার্থীদের সঙ্গে যুক্ত হন এবং সাহায্য নিন

আপনার রিপো ক্লোন করা শুরু করার আগে, সেটআপে সাহায্য, কোর্স সম্পর্কে যেকোন প্রশ্ন বা অন্যান্য শিক্ষার্থীদের সাথে যুক্ত হওয়ার জন্য [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) এ যোগ দিন।

## এই রিপো ক্লোন বা ফর্ক করুন

শুরু করার জন্য, অনুগ্রহ করে GitHub রিপোজিটরিটি ক্লোন বা ফর্ক করুন। এটি আপনাকে কোর্সের সামগ্রীর নিজস্ব একটি সংস্করণ তৈরি করতে সাহায্য করবে যাতে আপনি কোড চালাতে, পরীক্ষা করতে এবং বদলাতে পারেন!

এটি করা যাবে <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">রিপো ফর্ক করতে</a> লিঙ্কে ক্লিক করে

এখন আপনার নিজের ফর্ক করা সংস্করণ নিম্নলিখিত লিঙ্কে থাকা উচিত:

![Forked Repo](../../../translated_images/bn/forked-repo.33f27ca1901baa6a.webp)

### শ্যালো ক্লোন (ওয়ার্কশপ / কোডস্পেসের জন্য সুপারিশকৃত)

  >পুরো রিপোজিটোরি যখন পুরো ইতিহাস এবং সব ফাইল ডাউনলোড করবেন তখন বড় হতে পারে (~৩ জিবি)। যদি আপনি শুধু ওয়ার্কশপে অংশগ্রহণ করেন বা কিছু নির্দিষ্ট লেসনের ফোল্ডার প্রয়োজন হয়, তবে শ্যালো ক্লোন (বা একটি স্পার্স ক্লোন) ইতিহাস সংক্ষিপ্ত করে ও/অথবা ব্লব বাদ দিয়ে অধিকাংশ ডাউনলোড এড়ায়।

#### দ্রুত শ্যালো ক্লোন — ন্যূনতম ইতিহাস, সব ফাইল

নিচের কমান্ডগুলিতে `<your-username>` আপনার ফর্ক URL (অথবা যদি চান আপস্ট্রীম URL) দিয়ে প্রতিস্থাপন করুন।

শুধুমাত্র সাম্প্রতিক কমিট ইতিহাস ক্লোন করতে (ছোট ডাউনলোড):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

একটি নির্দিষ্ট ব্রাঞ্চ ক্লোন করতে:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### আংশিক (স্পার্স) ক্লোন — ন্যূনতম ব্লব + শুধুমাত্র নির্বাচিত ফোল্ডারসমূহ

এটি আংশিক ক্লোন এবং স্পার্স-চেকআউট ব্যবহার করে (Git 2.25+ প্রয়োজন এবং আংশিক ক্লোন সমর্থন সহ আধুনিক Git সুপারিশকৃত):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

রিপো ফোল্ডারে প্রবেশ করুন:

```bash|powershell
cd ai-agents-for-beginners
```

তারপর আপনি যে ফোল্ডারগুলো চান তা নির্দিষ্ট করুন (নিচের উদাহরণে দুটি ফোল্ডার দেখানো হয়েছে):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

ক্লোন ও ফাইলগুলি যাচাই করার পর, যদি আপনি শুধুমাত্র ফাইলগুলোই প্রয়োজন এবং স্থান মুক্ত করতে চান (কোন গিট ইতিহাস নয়), তবে রিপোজিটোরি মেটাডেটা মুছে ফেলুন (💀প্রত্যাবর্তনীয় নয় — সব Git ফাংশনালিটি হারাবেন: কোনো কমিট, পুল, পুশ বা ইতিহাস অ্যাক্সেস সম্ভব হবে না)।

```bash
# zsh/bash
rm -rf .git
```

```powershell
# পাওয়ারশেল
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ব্যবহার (লোকাল বড় ডাউনলোড এড়াতে সুপারিশকৃত)

- এই রিপোর জন্য [GitHub UI](https://github.com/codespaces) থেকে একটি নতুন Codespace তৈরি করুন।  

- নবনির্মিত কোডস্পেসের টার্মিনালে, উপরের শ্যালো/স্পার্স ক্লোন কমান্ডগুলোর একটি চালান যাতে কোডস্পেস ওয়ার্কস্পেসে শুধুমাত্র প্রয়োজনীয় লেসন ফোল্ডারগুলি নিয়ে আসা যায়।
- ঐচ্ছিক: কোডস্পেসের ভিতরে ক্লোন করার পর, অতিরিক্ত স্থান পুনরুদ্ধারের জন্য .git মুছে ফেলুন (উপরের মুছে ফেলার কমান্ড দেখুন)।
- নোট: আপনি যদি সরাসরি কোডস্পেসে রিপো খুলতে চান (অতিরিক্ত ক্লোন ছাড়া), জানবেন কোডস্পেস ডেভকনটেইনার পরিবেশ তৈরি করবে এবং প্রয়োজনের থেকেও বেশি কনফিগারেশন করতে পারে। নতুন কোডস্পেসের ভিতরে শ্যালো কপি ক্লোন করলে ডিস্ক ব্যবহারের আরও নিয়ন্ত্রণ থাকে।

#### টিপস

- আপনি যদি কোড সম্পাদনা/কমিট করতে চান তবে সর্বদা ক্লোন URL আপনার ফর্ক দিয়ে প্রতিস্থাপন করুন।
- পরবর্তীতে যদি আরও ইতিহাস বা ফাইল দরকার হয়, অনায়াসে fetch চালাতে পারেন বা স্পার্স-চেকআউট সামঞ্জস্য করে অতিরিক্ত ফোল্ডার অন্তর্ভুক্ত করতে পারেন।

## কোড চালানো

এই কোর্সে একটি ধারাবাহিক জুপিটার নোটবুক রয়েছে যা চালিয়ে আপনি AI এজেন্ট তৈরি করার হাতে-কলমে অভিজ্ঞতা লাভ করতে পারেন।

কোড নমুনাগুলি **Microsoft Agent Framework (MAF)** ব্যবহার করে `FoundryChatClient` সাথে, যা **Microsoft Foundry Agent Service V2** (Responses API) এর সাথে **Microsoft Foundry** এর মাধ্যমে সংযুক্ত।

সমস্ত পাইথন নোটবুকগুলো `*-python-agent-framework.ipynb` নামে লেবেল করা হয়েছে।

## প্রয়োজনীয়তা

- পাইথন ৩.১২+
  - **বিঃদ্রঃ**: যদি পাইথন৩.১২ ইন্সটল না থাকে, নিশ্চিত করুন এটি ইন্সটল করেছেন। তারপরে requirements.txt থেকে সঠিক সংস্করণ পেতে python3.12 ব্যবহার করে venv তৈরি করুন।
  
    > উদাহরণ

    পাইথন venv ডিরেক্টরি তৈরি করুন:

    ```bash|powershell
    python -m venv venv
    ```

    তারপর venv এনভায়রনমেন্ট সক্রিয় করুন:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET ১০+: .NET ব্যবহার করে নমুনা কোডের জন্য, [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) বা তার পরবর্তী সংস্করণ ইন্সটল করুন। তারপর আপনার ডাউনলোড করা .NET SDK সংস্করণ যাচাই করুন:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — প্রমাণীকরণের জন্য প্রয়োজন। ইন্সটল করুন [aka.ms/installazurecli](https://aka.ms/installazurecli) থেকে।
- **Azure Subscription** — Microsoft Foundry ও Microsoft Foundry Agent Service অ্যাক্সেসের জন্য।
- **Microsoft Foundry Project** — একটি প্রকল্প যার একটি ডিপ্লোয়েড মডেল আছে (যেমন, `gpt-5-mini`)। দেখুন [Step 1](#ধাপ-১-একটি-microsoft-foundry-প্রকল্প-তৈরি-করুন) নিচে।

আমরা এই রিপোজিটরির মূল অংশে একটি `requirements.txt` ফাইল অন্তর্ভুক্ত করেছি যা কোড নমুনাগুলো চালাতে প্রয়োজনীয় সব পাইথন প্যাকেজের তালিকা দেয়।

আপনি এটি আপনার টার্মিনালে পরবর্তী কমান্ড চালিয়ে ইন্সটল করতে পারেন:

```bash|powershell
pip install -r requirements.txt
```

আমরা একটি পাইথন ভার্চুয়াল এনভায়রনমেন্ট তৈরি করতে পরামর্শ দিই যাতে কোনো সংঘাত বা সমস্যা এড়ানো যায়।

## VSCode সেটআপ

নিশ্চিত করুন যে আপনি VSCode-এ সঠিক পাইথন সংস্করণ ব্যবহার করছেন।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry এবং Microsoft Foundry Agent Service সেটআপ

### ধাপ ১: একটি Microsoft Foundry প্রকল্প তৈরি করুন

আপনার একটি Microsoft Foundry **হাব** এবং একটি ডিপ্লোয়েড মডেলসহ **প্রকল্প** প্রয়োজন নোটবুক চালানোর জন্য।

১। যান [ai.azure.com](https://ai.azure.com) এবং আপনার Azure একাউন্ট দিয়ে সাইন ইন করুন।
২। একটি **হাব** তৈরি করুন (অথবা বিদ্যমান ব্যবহার করুন)। দেখুন: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)।
৩। হাবের ভিতরে একটি **প্রকল্প** তৈরি করুন।
৪। **Models + Endpoints** → **Deploy model** থেকে একটি মডেল (যেমন `gpt-5-mini`) ডিপ্লয় করুন।

### ধাপ ২: আপনার প্রকল্পের এন্ডপয়েন্ট ও মডেল ডিপ্লয়মেন্ট নাম সংগ্রহ করুন

Microsoft Foundry পোর্টালে আপনার প্রকল্প থেকে:

- **প্রকল্প এন্ডপয়েন্ট** — **Overview** পেজে যান ও এন্ডপয়েন্ট URL কপি করুন।

![Project Connection String](../../../translated_images/bn/project-endpoint.8cf04c9975bbfbf1.webp)

- **মডেল ডিপ্লয়মেন্ট নাম** — **Models + Endpoints** এ যান, আপনার ডিপ্লয় করা মডেলটি নির্বাচন করুন এবং **Deployment name** নোট করুন (যেমন, `gpt-5-mini`)।

### ধাপ ৩: `az login` দিয়ে Azure-তে সাইন ইন করুন

সমস্ত নোটবুক **`AzureCliCredential`** ব্যবহার করে প্রমাণীকরণ করে — কোনো API কী ম্যানেজ করতে হয় না। এর জন্য আপনাকে Azure CLI ব্যবহারের মাধ্যমে সাইন ইন থাকতে হবে।

১। যদি আগে না করে থাকেন **Azure CLI** ইন্সটল করুন: [aka.ms/installazurecli](https://aka.ms/installazurecli)

২। চালান:

    ```bash|powershell
    az login
    ```

    অথবা আপনি যদি কোনো ব্রাউজার ছাড়া রিমোট/কোডস্পেসে থাকেন:

    ```bash|powershell
    az login --use-device-code
    ```

৩। অনুরোধ করলে আপনার সাবস্ক্রিপশন নির্বাচন করুন — আপনার Foundry প্রকল্পের অন্তর্গতটি বেছে নিন।

৪। নিশ্চিত করুন আপনি সাইন ইন করেছেন:

    ```bash|powershell
    az account show
    ```

> **কেন `az login`?** নোটবুকগুলো `azure-identity` প্যাকেজ থেকে `AzureCliCredential` ব্যবহার করে প্রমাণীকরণ করে। অর্থাৎ আপনার Azure CLI সেশনই ক্রেডেনশিয়াল সরবরাহ করে — `.env` ফাইলে কোনো API কী বা সিক্রেট নেই। এটাই [নিরাপত্তার সর্বোত্তম প্র্যাকটিস](https://learn.microsoft.com/azure/developer/ai/keyless-connections)।

### ধাপ ৪: আপনার `.env` ফাইল তৈরি করুন

উদাহরণ ফাইল কপি করুন:

```bash
# জেডএসএইচ/বাশ
cp .env.example .env
```

```powershell
# পাওয়ারশেল
Copy-Item .env.example .env
```

`.env` খুলে এই দুই মান পূরণ করুন:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| পরিবর্তনশীল | কোথায় পাবেন |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry পোর্টাল → আপনার প্রকল্প → **Overview** পেজ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry পোর্টাল → **Models + Endpoints** → আপনার ডিপ্লয় করা মডেলের নাম |

বেশিরভাগ লেসনের জন্য এতটুকুই! নোটবুকগুলো স্বয়ংক্রিয়ভাবে আপনার `az login` সেশনের মাধ্যমে প্রমাণীকরণ করবে।

### ধাপ ৫: পাইথন নির্ভরতাসমূহ ইন্সটল করুন

```bash|powershell
pip install -r requirements.txt
```

আমরা সুপারিশ করছি এটি আপনি আগেই তৈরি করা ভার্চুয়াল এনভায়রনমেন্টে চালাবেন।

## লেসন ৫ এর জন্য অতিরিক্ত সেটআপ (Agentic RAG)

লেসন ৫ **Azure AI Search** ব্যবহার করে রিট্রিভাল-অগমেন্টেড জেনারেশন এর জন্য। আপনি যদি ওই লেসন চালাতে চান, তবে `.env` ফাইলে এই পরিবর্তনশীলগুলো যোগ করুন:

| পরিবর্তনশীল | কোথায় পাবেন |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure পোর্টাল → আপনার **Azure AI Search** রিসোর্স → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure পোর্টাল → আপনার **Azure AI Search** রিসোর্স → **Settings** → **Keys** → প্রাইমারি অ্যাডমিন কী |

## লেসনগুলো যা সরাসরি Azure OpenAI কল করে (লেসন ৬ এবং ৮) এর জন্য অতিরিক্ত সেটআপ

লেসন ৬ ও ৮ এর কিছু নোটবুকে সরাসরি **Azure OpenAI** কল করা হয় (**Responses API** ব্যবহার করে) Microsoft Foundry প্রকল্প না দিয়ে। এই নমুনাগুলো আগে GitHub Models ব্যবহার করত, যা নিষ্ক্রিয় (২০২৬ জুলাই অবধি) এবং Responses API সমর্থন করে না। ওই নমুনাগুলো চালানোর পরিকল্পনা থাকলে `.env` ফাইলে এই পরিবর্তনশীলগুলো যোগ করুন:

| পরিবর্তনশীল | কোথায় পাবেন |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure পোর্টাল → আপনার **Azure OpenAI** রিসোর্স → **Keys and Endpoint** → Endpoint (যেমন `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | আপনার ডিপ্লয় করা মডেলের নাম (যেমন `gpt-5-mini`) যা Responses API সমর্থন করে |
| `AZURE_OPENAI_API_KEY` | ঐচ্ছিক — কিইভিত্তিক প্রমাণীকরণ ব্যবহারের জন্য যদি `az login` / Entra ID ব্যবহার না করেন |

> Responses API স্থিতিশীল `/openai/v1/` এন্ডপয়েন্ট ব্যবহার করে, তাই `api-version` প্রয়োজন হয় না। keyless Entra ID প্রমাণীকরণের জন্য `az login` সাইন ইন করুন।

## বিকল্প প্রদানকারী: MiniMax (OpenAI-সঙ্গতিপূর্ণ)

[MiniMax](https://platform.minimaxi.com/) বৃহৎ প্রসঙ্গ মডেল (সর্বোচ্চ 204K টোকেন) OpenAI-সঙ্গতিপূর্ণ API মাধ্যমে প্রদান করে। Microsoft Agent Framework এর `OpenAIChatClient` যেকোনো OpenAI-সঙ্গতিপূর্ণ এন্ডপয়েন্টের সঙ্গে কাজ করে, তাই MiniMax ব্যবহার করতে পারেন Azure OpenAI বা OpenAI এর বিকল্প হিসাবে।

`.env` ফাইলে এই পরিবর্তনশীলগুলো যোগ করুন:

| পরিবর্তনশীল | কোথায় পাবেন |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | ব্যবহার করুন `https://api.minimax.io/v1` (ডিফল্ট মান) |
| `MINIMAX_MODEL_ID` | ব্যবহারের মডেলের নাম (যেমন, `MiniMax-M3`) |

**উদাহরণ মডেলসমূহ**: `MiniMax-M3` (সুপারিশকৃত), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (দ্রুত প্রতিক্রিয়া)। মডেল নাম ও উপলভ্যতা সময়ের সাথে পরিবর্তিত হতে পারে, এবং নির্দিষ্ট মডেলের অ্যাক্সেস আপনার অ্যাকাউন্ট বা অঞ্চলের উপর নির্ভরশীল — বর্তমান তালিকার জন্য [MiniMax Platform](https://platform.minimaxi.com/) দেখুন। যদি `MiniMax-M3` আপনার অ্যাকাউন্টে না থাকে, তবে `MINIMAX_MODEL_ID` এমন কোনো মডেল দিন যা আপনার অ্যাকাউন্টে আছে (যেমন `MiniMax-M2.7`)।

`OpenAIChatClient` ব্যবহার করা কোড নমুনাগুলো (যেমন, লেসন ১৪ হোটেল বুকিং ওয়ার্কফ্লো) স্বয়ংক্রিয়ভাবে আপনার MiniMax কনফিগারেশন চিহ্নিত করে ব্যবহার করবে যখন `MINIMAX_API_KEY` সেট করা থাকবে।

## বিকল্প প্রদানকারী: Foundry Local (স্থানীয়ভাবে মডেল চালান)

[Foundry Local](https://foundrylocal.ai) একটি হালকা রানটাইম যা ভাষা মডেলগুলি সম্পূর্ণরূপে আপনার নিজের মেশিনে ডাউনলোড, পরিচালনা ও পরিবেশন করে OpenAI-সঙ্গতিপূর্ণ API মাধ্যমে — কোন ক্লাউড, কোন Azure সাবস্ক্রিপশন, এবং কোন API কী নয়। এটি অফলাইন ডেভেলপমেন্ট, ক্লাউড খরচ ছাড়া পরীক্ষা-নিরীক্ষা, বা ডেটা ডিভাইসে রাখার জন্য একটি চমৎকার বিকল্প।

Microsoft Agent Framework এর `OpenAIChatClient` যেকোন OpenAI-সঙ্গতিপূর্ণ এন্ডপয়েন্টের সাথে কাজ করে, তাই Foundry Local Azure OpenAI-এর একটি স্থানীয় বিকল্প।

**১। Foundry Local ইন্সটল করুন**

```bash
# উইন্ডোজ
winget install Microsoft.FoundryLocal

# ম্যাকওএস
brew install foundrylocal
```

**২। একটি মডেল ডাউনলোড ও চালান** (এটি স্থানীয় সার্ভিস শুরু করবে):

```bash
foundry model list          # উপলব্ধ মডেলগুলি দেখুন
foundry model run phi-4-mini
```

**৩। স্থানীয় এন্ডপয়েন্ট আবিষ্কারের জন্য পাইথন SDK ইন্সটল করুন:**

```bash
pip install foundry-local-sdk
```

**৪। Microsoft Agent Framework কে আপনার স্থানীয় মডেল নির্দেশ করুন:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# ডাউনলোড করে (যদি প্রয়োজন হয়) এবং মডেলটি স্থানীয়ভাবে সার্ভ করে, তারপর এন্ডপয়েন্ট/পোর্ট আবিষ্কার করে।
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # উদাহরণস্বরূপ http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local এর জন্য সবসময় "প্রয়োজন নেই"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **নোট:** Foundry Local OpenAI-সঙ্গতিপূর্ণ **Chat Completions** এন্ডপয়েন্ট সরবরাহ করে। এটি স্থানীয় ডেভেলপমেন্ট ও অফলাইন পরিস্থিতির জন্য। সম্পূর্ণ **Responses API** বৈশিষ্ট্যের জন্য (রাষ্ট্রপূর্ণ কথোপকথন, গভীর টুল অর্চেস্ট্রেশন, এবং এজেন্ট-স্টাইল ডেভেলপমেন্ট), পাঠ্যে দেখানো মত **Azure OpenAI** বা **Microsoft Foundry** প্রকল্প ব্যবহার করুন। বর্তমান মডেল ক্যাটালগ ও প্ল্যাটফর্ম সাপোর্টের জন্য [Foundry Local ডকুমেন্টেশন](https://foundrylocal.ai) দেখুন।

## লেসন ৮ এর অতিরিক্ত সেটআপ (Bing Grounding ওয়ার্কফ্লো)


পাঠ ৮ এর শর্তাধীন ওয়ার্কফ্লো নোটবুক মাইক্রোসফট ফাউন্ড্রির মাধ্যমে **বিং গ্রাউন্ডিং** ব্যবহার করে। আপনি যদি সেই নমুনাটি চালানোর পরিকল্পনা করেন, তবে আপনার `.env` ফাইলে এই ভ্যারিয়েবলটি যোগ করুন:

| ভ্যারিয়েবল | কোথায় খুঁজে পাবেন |
|----------|-----------------|
| `BING_CONNECTION_ID` | মাইক্রোসফট ফাউন্ড্রি পোর্টাল → আপনার প্রকল্প → **Management** → **Connected resources** → আপনার Bing সংযোগ → সংযোগ আইডি কপি করুন |

## সমস্যা সমাধান

### macOS-এ SSL সার্টিফিকেট যাচাইকরণ ত্রুটি

আপনি যদি macOS-এ থাকেন এবং নিচের মতো ত্রুটি পান:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

এটি macOS-এ পাইথনের একটি পরিচিত সমস্যা যেখানে সিস্টেমের SSL সার্টিফিকেট স্বয়ংক্রিয়ভাবে বিশ্বাসযোগ্য হয় না। নিম্নলিখিত সমাধানগুলি ধাপে ধাপে চেষ্টা করুন:

**বিকল্প ১: পাইথনের ইনস্টল সার্টিফিকেট স্ক্রিপ্ট চালান (প্রস্তাবিত)**

```bash
# আপনার ইন্সটল করা পাইথন সংস্করণটি (যেমন, 3.12 বা 3.13) দিয়ে 3.XX প্রতিস্থাপন করুন:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**বিকল্প ২: আপনার নোটবুকে `connection_verify=False` ব্যবহার করুন (শুধুমাত্র GitHub মডেল নোটবুকের জন্য)**

পাঠ ৬ নোটবুকে (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) একটি মন্তব্য করা ওয়ার্কারাউন্ড ইতিমধ্যে অন্তর্ভুক্ত আছে। ক্লায়েন্ট তৈরি করার সময় `connection_verify=False` আনমেন্ট করুন:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # সার্টিফিকেট ত্রুটি পরিলক্ষিত হলে SSL যাচাইকরণ নিষ্ক্রিয় করুন
)
```

> **⚠️ সতর্কতা:** SSL যাচাইকরণ বন্ধ করা (`connection_verify=False`) সার্টিফিকেট যাচাইকরণ এড়ানোর মাধ্যমে নিরাপত্তা হ্রাস করে। এটি শুধুমাত্র ডেভেলপমেন্ট পরিবেশে অস্থায়ী সমাধান হিসেবে ব্যবহার করুন, প্রোডাকশনে কখনও করবেন না।

**বিকল্প ৩: `truststore` ইনস্টল ও ব্যবহার করুন**

```bash
pip install truststore
```

তারপর যেকোন নেটওয়ার্ক কল করার আগে আপনার নোটবুক বা স্ক্রিপ্টের শীর্ষে নিচেরটি যোগ করুন:

```python
import truststore
truststore.inject_into_ssl()
```

## কোথাও আটকে গেলেন?

এই সেটআপ চালানোর সময় যদি কোনো সমস্যা হয়, তবে আমাদের <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> এ যোগ দিন অথবা <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">এখানে একটি সমস্যা তৈরি করুন</a>।

## পরবর্তী পাঠ

এখন আপনি এই কোর্সের কোড চালানোর জন্য প্রস্তুত। AI এজেন্টসের বিশ্ব সম্পর্কে আরও জানার জন্য শুভ শিক্ষালাভ!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->