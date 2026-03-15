# কোর্স সেটআপ

## ভূমিকা

এই পাঠে কিভাবে এই কোর্সের কোড নমুনাগুলো চালাতে হয় তা আলোচনা করা হবে।

## অন্যান্য শিক্ষার্থীদের সাথে যোগ দিন এবং সহায়তা পান

আপনি আপনার রিপো ক্লোন করা শুরু করার আগে, সেটআপে কোনো সহায়তা, কোর্স সম্পর্কে কোনো প্রশ্ন বা অন্যান্য শিক্ষার্থীদের সাথে সংযুক্ত হতে [AI Agents For Beginners Discord চ্যানেল](https://aka.ms/ai-agents/discord) এ যোগ দিন।

## এই রিপো ক্লোন বা ফর্ক করুন

শুরু করতে, অনুগ্রহ করে GitHub রেপোসিটরি ক্লোন বা ফর্ক করুন। এটি আপনার নিজের সংস্করণ করবে কোর্সের উপকরণগুলির যাতে আপনি কোড চালাতে, পরীক্ষা করতে এবং সামান্য পরিবর্তন করতে পারেন!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">রিপো ফর্ক করুন</a>

You should now have your own forked version of this course in the following link:

![ফর্ক করা রিপো](../../../translated_images/bn/forked-repo.33f27ca1901baa6a.webp)

### শ্যালো ক্লোন (ওয়ার্কশপ / Codespaces-এর জন্য সুপারিশকৃত)

  > পূর্ণ রেপোজিটরি সম্পূর্ণ ইতিহাস এবং সব ফাইল ডাউনলোড করলে বেশ বড় হতে পারে (~3 GB)। যদি আপনি কেবল ওয়ার্কশপে অংশ নিচ্ছেন বা কেবল কয়েকটি লেসন ফোল্ডার দরকার, তাহলে একটি শ্যালো ক্লোন (অথবা একটি sparse ক্লোন) ইতিহাস সংক্ষিপ্ত করে এবং/অথবা ব্লব স্কিপ করে সেই ডাউনলোডের অনেকটাই এড়ায়।

#### দ্রুত শ্যালো ক্লোন — ন্যূনতম ইতিহাস, সব ফাইল

Replace `<your-username>` in the below commands with your fork URL (or the upstream URL if you prefer).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### আংশিক (sparse) ক্লোন — ন্যূনতম ব্লব + শুধুমাত্র নির্বাচিত ফোল্ডার

This uses partial clone and sparse-checkout (requires Git 2.25+ and recommended modern Git with partial clone support):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Traverse into the repo folder:

```bash|powershell
cd ai-agents-for-beginners
```

Then specify which folders you want (example below shows two folders):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

After cloning and verifying the files, if you only need files and want to free space (no git history), please delete the repository metadata (💀irreversible — you will lose all Git functionality: no commits, pulls, pushes, or history access).

```bash
# জেডএসএইচ/বাশ
rm -rf .git
```

```powershell
# পাওয়ারশেল
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ব্যবহার (লোকাল বড় ডাউনলোড এড়াতে সুপারিশকৃত)

- এই রিপো-এর জন্য [GitHub UI](https://github.com/codespaces) ব্যবহার করে একটি নতুন Codespace তৈরি করুন।  

- নবনির্মিত codespace-এর টার্মিনালে, উপরের শ্যালো/স্পার্স ক্লোন কমান্ডগুলোর মধ্যে একটি চালান যাতে শুধু আপনার দরকারি লেসন ফোল্ডারগুলোই Codespace ওয়ার্কস্পেসে আসে।
- ঐচ্ছিক: Codespaces-এ ক্লোন করার পরে অতিরিক্ত স্থান পুনরুদ্ধার করতে .git সরান (উপরে থাকা রিমুভাল কমান্ডগুলো দেখুন)।
- নোট: যদি আপনি রিপোটি সরাসরি Codespaces-এ খুলতে চান (অতিরিক্ত ক্লোন ছাড়াই), জানবেন Codespaces devcontainer পরিবেশ তৈরি করবে এবং সম্ভবত আপনার চাওয়ার তুলনায় আরও কিছু প্রোভিশন করতে পারে। নতুন Codespace-এর ভিতরে একটি শ্যালো কপি ক্লোন করলে ডিস্ক ব্যবহারে আপনার নিয়ন্ত্রণ বেড়ে যায়।

#### টিপস

- যদি আপনি সম্পাদনা/কমিট করতে চান, সবসময় ক্লোন URL আপনার ফর্ক দিয়ে প্রতিস্থাপন করুন।
- পরে যদি আপনার আরও ইতিহাস বা ফাইল দরকার হয়, আপনি সেগুলো fetch করতে পারেন বা sparse-checkout সামঞ্জস্য করে অতিরিক্ত ফোল্ডার অন্তর্ভুক্ত করতে পারবেন।

## কোড চালানো

এই কোর্সটি হাতে কলমে AI এজেন্ট তৈরির অভিজ্ঞতা অর্জনের জন্য একটি সিরিজ Jupyter নোটবুক সরবরাহ করে যেগুলো আপনি চালাতে পারবেন।

The code samples use **Microsoft Agent Framework (MAF)** with the `AzureAIProjectAgentProvider`, which connects to **Azure AI Agent Service V2** (the Responses API) through **Microsoft Foundry**.

All Python notebooks are labelled `*-python-agent-framework.ipynb`.

## প্রয়োজনীয়তা

- Python 3.12+
  - **নোট**: যদি আপনার কাছে Python3.12 ইনস্টল না থাকে, নিশ্চিত করুন যে আপনি এটি ইনস্টল করুন। তারপর requirements.txt ফাইল থেকে সঠিক ভার্সনগুলো ইনস্টল করার জন্য python3.12 ব্যবহার করে আপনার venv তৈরি করুন।
  
    > উদাহরণ

    Create Python venv directory:

    ```bash|powershell
    python -m venv venv
    ```

    Then activate venv environment for:

    ```bash
    # জেডএসএইচ/বাশ
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For the sample codes using .NET, ensure you install [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or later. Then, check your installed .NET SDK version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — প্রমাণীকরণের জন্য প্রয়োজন। [aka.ms/installazurecli](https://aka.ms/installazurecli) থেকে ইনস্টল করুন।
- **Azure Subscription** — Microsoft Foundry এবং Azure AI Agent Service-এ অ্যাক্সেসের জন্য।
- **Microsoft Foundry Project** — চালনার জন্য একটি ডিপ্লয় করা মডেল সহ একটি প্রকল্প (যেমন `gpt-4o`)। নিচে [Step 1](../../../00-course-setup) দেখুন।

রিপোজিটরির রুটে একটি `requirements.txt` ফাইল অন্তর্ভুক্ত করা আছে যা কোড নমুনাগুলো চালাতে প্রয়োজনীয় সব পাইথন প্যাকেজ রয়েছে।

আপনি রিপোজিটরির রুটে টার্মিনাল থেকে নিচের কমান্ডটি চালিয়ে সেগুলো ইনস্টল করতে পারেন:

```bash|powershell
pip install -r requirements.txt
```

আমরা সুপারিশ করি কোনো কনফ্লিক্ট এবং সমস্যাসমূহ এড়াতে একটি পাইথন ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন।

## VSCode সেটআপ

VSCode-এ নিশ্চিত করুন আপনি সঠিক সংস্করণের পাইথন ব্যবহার করছেন।

![ছবি](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry এবং Azure AI Agent Service সেটআপ

### ধাপ 1: একটি Microsoft Foundry প্রকল্প তৈরি করুন

নোটবুকগুলো চালানোর জন্য আপনার একটি Azure AI Foundry **hub** এবং **project** প্রয়োজন যাদের কাছে একটি ডিপ্লয় করা মডেল আছে।

1. আপনার Azure অ্যাকাউন্ট দিয়ে সাইন ইন করতে [ai.azure.com](https://ai.azure.com) এ যান।
2. একটি **hub** তৈরি করুন (অথবা বিদ্যমান একটি ব্যবহার করুন)। দেখুন: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)।
3. হাবের ভিতরে একটি **project** তৈরি করুন।
4. **Models + Endpoints** → **Deploy model** থেকে একটি মডেল ডিপ্লয় করুন (উদাহরণ: `gpt-4o`)।

### ধাপ 2: আপনার প্রকল্পের এন্ডপয়েন্ট এবং মডেল ডিপ্লয়মেন্ট নাম সংগ্রহ করুন

Microsoft Foundry পোর্টালের আপনার প্রকল্প থেকে:

- **Project Endpoint** — **Overview** পৃষ্ঠায় যান এবং endpoint URL কপি করুন।

![প্রকল্প সংযোগ স্ট্রিং](../../../translated_images/bn/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** এ যান, আপনার ডিপ্লয় করা মডেল নির্বাচন করুন এবং **Deployment name** নোট করুন (উদাহরণ: `gpt-4o`)।

### ধাপ 3: `az login` দিয়ে Azure-এ সাইন ইন করুন

সমস্ত নোটবুক প্রমাণীকরণের জন্য **`AzureCliCredential`** ব্যবহার করে — কোনো API কী ম্যানেজ করার প্রয়োজন নেই। এর জন্য আপনাকে Azure CLI দিয়ে সাইন ইন করতে হবে।

1. **Azure CLI ইনস্টল করুন** যদি না করে থাকেন: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Sign in** করতে নিচের কমান্ডটি চালান:

    ```bash|powershell
    az login
    ```

    Or if you're in a remote/Codespace environment without a browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **আপনার সাবস্ক্রিপশন নির্বাচন করুন** যদি প্রম্পট আসে — আপনার Foundry প্রকল্পটি যে সাবস্ক্রিপশনে আছে সেটি নির্বাচন করুন।

4. **যাচাই করুন** যে আপনি সাইন ইন করেছেন:

    ```bash|powershell
    az account show
    ```

> **কেন `az login`?** নোটবুকগুলো `azure-identity` প্যাকেজ থেকে `AzureCliCredential` ব্যবহার করে প্রমাণীকরণ করে। এর মানে আপনার Azure CLI সেশনই ক্রেডেনশিয়াল প্রদান করে — আপনার `.env` ফাইলে কোনো API কী বা সিক্রেট নেই। এটি একটি [সুরক্ষা শ্রেষ্ঠ অনুশীলন](https://learn.microsoft.com/azure/developer/ai/keyless-connections)।

### ধাপ 4: আপনার `.env` ফাইল তৈরি করুন

উদাহরণ ফাইল কপি করুন:

```bash
# zsh/বাশ
cp .env.example .env
```

```powershell
# পাওয়ারশেল
Copy-Item .env.example .env
```

`.env` খুলুন এবং এই দুটি ভ্যালু পূরণ করুন:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → আপনার প্রকল্প → **Overview** পৃষ্ঠা |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → আপনার ডিপ্লয় করা মডেলের নাম |

এটাই বেশিরভাগ পাঠের জন্য যথেষ্ট! নোটবুকগুলো আপনার `az login` সেশনের মাধ্যমে স্বয়ংক্রিয়ভাবে প্রমাণীকরণ করবে।

### ধাপ 5: পাইথন নির্ভরতা ইনস্টল করুন

```bash|powershell
pip install -r requirements.txt
```

আমরা সুপারিশ করি আপনি এটি আগে তৈরিকৃত ভার্চুয়াল এনভায়রনমেন্টের ভিতর থেকে চালান।

## পাঠ ৫ (Agentic RAG)-এর জন্য অতিরিক্ত সেটআপ

পাঠ 5-এ retrieval-augmented generation এর জন্য **Azure AI Search** ব্যবহার করা হয়। যদি আপনি সেই পাঠটি চালাতে চান, তবে আপনার `.env` ফাইলে এই ভেরিয়েবলগুলো যোগ করুন:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → আপনার **Azure AI Search** রিসোর্স → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → আপনার **Azure AI Search** রিসোর্স → **Settings** → **Keys** → primary admin key |

## পাঠ ৬ ও পাঠ ৮ (GitHub Models)-এর জন্য অতিরিক্ত সেটআপ

কিছুকটি নোটবুক পাঠ 6 এবং 8-এ Azure AI Foundry-এর বদলে **GitHub Models** ব্যবহার করে। যদি আপনি সেই নমুনাগুলো চালাতে চান, আপনার `.env` ফাইলে এই ভেরিয়েবলগুলো যোগ করুন:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | ব্যবহার করুন `https://models.inference.ai.azure.com` (ডিফল্ট মান) |
| `GITHUB_MODEL_ID` | ব্যবহারের জন্য মডেলের নাম (উদাহরণ: `gpt-4o-mini`) |

## পাঠ ৮ (Bing Grounding Workflow)-এর জন্য অতিরিক্ত সেটআপ

পাঠ 8-এর conditional workflow নোটবুকটি Azure AI Foundry-এর মাধ্যমে **Bing grounding** ব্যবহার করে। যদি আপনি সেই নমুনা চালাতে চান, আপনার `.env` ফাইলে এই ভেরিয়েবলটি যোগ করুন:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry পোর্টাল → আপনার প্রকল্প → **Management** → **Connected resources** → আপনার Bing connection → connection ID কপি করুন |

## সমস্যা সমাধান

### macOS-এ SSL সার্টিফিকেট যাচাইকরণ ত্রুটি

যদি আপনি macOS-এ থাকেন এবং নিম্নরকম একটি ত্রুটি পান:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

এটি Python-এর macOS সংস্করণে একটি পরিচিত সমস্যা যেখানে সিস্টেম SSL সার্টিফিকেটগুলি স্বয়ংক্রিয়ভাবে ট্রাস্ট করা হয় না। নিম্নলিখিত সমাধানগুলো ক্রমান্বয়ে চেষ্টা করুন:

**অপশন 1: Python-এর Install Certificates স্ক্রিপ্ট চালান (সুপারিশকৃত)**

```bash
# আপনার ইনস্টল করা পাইথন সংস্করণ দিয়ে 3.XX প্রতিস্থাপন করুন (যেমন, 3.12 বা 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**অপশন 2: আপনার নোটবুকে `connection_verify=False` ব্যবহার করুন (শুধুমাত্র GitHub Models নোটবুকগুলোর জন্য)**

Lesson 6 নোটবুকে (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) একটি মন্তব্য করা ওয়ার্কঅ্যারাউন্ড ইতোমধ্যেই অন্তর্ভুক্ত আছে। ক্লায়েন্ট তৈরি করার সময় `connection_verify=False` আনকমেন্ট করুন:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # যদি সার্টিফিকেট ত্রুটি দেখা দেয়, তাহলে SSL যাচাইকরণ নিষ্ক্রিয় করুন
)
```

> **⚠️ সতর্কতা:** SSL যাচাই অক্ষম করা (`connection_verify=False`) সার্টিফিকেট যাচাইকরণ এড়িয়ে নিরাপত্তা হ্রাস করে। এটি শুধুমাত্র ডেভেলপমেন্ট পরিবেশে অস্থায়ী ওয়ার্কঅ্যারাউন্ড হিসেবে ব্যবহার করুন, প্রোডাকশনে কখনই ব্যবহার করা উচিত নয়।

**অপশন 3: `truststore` ইনস্টল করে ব্যবহার করুন**

```bash
pip install truststore
```

এরপর নেটওয়ার্ক কল করার আগে আপনার নোটবুক বা স্ক্রিপ্টের শীর্ষে নিম্নলিখিত যোগ করুন:

```python
import truststore
truststore.inject_into_ssl()
```

## কোথাও আটকে গেছেন?

যদি এই সেটআপ চালাতে কোনো সমস্যা হয়, আমাদের <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> এ যোগ দিন অথবা <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">একটি ইস্যু তৈরি করুন</a>।

## পরবর্তী পাঠ

আপনি এখন এই কোর্সের কোড চালানোর জন্য প্রস্তুত। AI এজেন্টদের দুনিয়া সম্পর্কে আরও জানতে শুভ শেখা!

[AI এজেন্টদের পরিচিতি এবং এজেন্ট ব্যবহারের কেসসমূহ](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
দায়মুক্তি:
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা সঠিকতার জন্য যতেষ্ট চেষ্টা করি, তবুও দয়া করে জানুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকেই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের ক্ষেত্রে পেশাদার মানব অনুবাদ পরামর্শযোগ্য। এই অনুবাদ ব্যবহারের ফলে যে কোনো ভুল বোঝাবুঝি বা অপ্রাসঙ্গিক ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->