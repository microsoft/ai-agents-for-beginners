---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI চ্যাট সম্পূর্ণতা থেকে Responses API তে পাইথন অ্যাপসগুলো মাইগ্রেট করুন

> **অধিকারিক নির্দেশনা — সঠিকভাবে অনুসরণ করুন**
>
> এই স্কিলটি Azure OpenAI চ্যাট সম্পূর্ণতা ব্যবহৃত পাইথন কোডবেসগুলোকে
> একীভূত Responses API তে মাইগ্রেট করে। এই নির্দেশনাগুলো যথাযথভাবে অনুসরণ করুন।
> প্যারামিটার ম্যাপিংস ইম্প্রোভাইজ করবেন না বা API আকৃতি উদ্ভাবন করবেন না।

---

## ট্রিগারসমূহ

যখন ব্যবহারকারী চান, এই স্কিল সক্রিয় করুন:
- Azure OpenAI চ্যাট সম্পূর্ণতা থেকে Responses API তে একটি পাইথন অ্যাপ মাইগ্রেট করতে
- Azure OpenAI এর বিরুদ্ধে সর্বশেষ API আকৃতির জন্য পাইথন OpenAI SDK ব্যবহার আপগ্রেড করতে
- Azure এ Responses প্রয়োজন এমন GPT-5 বা নতুন মডেলের জন্য পাইথন কোড প্রস্তুত করতে
- `AzureOpenAI`/`AsyncAzureOpenAI` থেকে ভি১ এন্ডপয়েন্ট সহ স্ট্যান্ডার্ড `OpenAI`/`AsyncOpenAI` ক্লায়েন্টে স্যুইচ করতে
- `AzureOpenAI` কনস্ট্রাক্টর বা `api_version` সম্পর্কিত অব্যবহিত সতর্কতা ঠিক করতে

---

## ⚠️ মডেল সামঞ্জস্যতা — প্রথমে পরীক্ষা করুন

> **মাইগ্রেশনের আগে, নিশ্চিত করুন যে আপনার Azure OpenAI ডিপ্লয়মেন্ট Responses API সমর্থন করে।**

### ১। আপনার ডিপ্লয়মেন্ট দ্রুত পরীক্ষা করুন (সবচেয়ে দ্রুত)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **নোট**: Azure OpenAI এ `max_output_tokens` এর **সর্বনিন্ম ১৬** আছে। ১৬ এর নিচের মান ৪০০ এরর দেয়। স্মোক টেস্টের জন্য ৫০+ ব্যবহার করুন।

যদি এটি ৪০৪ রিটার্ন করে, তাহলে ডিপ্লয়মেন্টের মডেল এখনো Responses সমর্থন করে না — নিচের রেফারেন্স দেখুন অথবা সমর্থিত মডেল দিয়ে পুনরায় ডিপ্লয় করুন।

### ২। আপনার অঞ্চলের উপলব্ধ মডেল পরীক্ষা করুন (প্রস্তাবিত)

বিল্ট-ইন মডেল সামঞ্জস্যতা টুল চালান যা দেখাবে আপনার নির্দিষ্ট অঞ্চলে Responses API সমর্থনসহ কী কী মডেল পাওয়া যায়:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

এটি Azure ARM লাইভ কুয়েরি করে এবং একটি সামঞ্জস্যতা ম্যাট্রিক্স দেখায় — কোন মডেল Responses, স্ট্রাকচার্ড আউটপুট, টুলস ইত্যাদি সাপোর্ট করে। ফলাফল সঙ্কুচিত করতে `--filter gpt-5.1,gpt-5.2` ব্যবহার করুন অথবা স্ক্রিপ্টিং এর জন্য `--json`।

### ৩। পূর্ণ মডেল সমর্থন রেফারেন্স

- **লাইভ কুয়েরি**: `python migrate.py models` (উপর দেখুন — অঞ্চল-নির্দিষ্ট, সর্বদা হালনাগাদ)
- **উপলব্ধতা ব্রাউজ করুন**: [মডেল সারাংশ টেবিল এবং অঞ্চল উপলব্ধতা](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **দ্রুত শুরু ও নির্দেশনা**: **https://aka.ms/openai/start**

### ⚠️ পুরানো মডেল সীমাবদ্ধতা

> **সতর্কতা**: পুরানো মডেল (য например `gpt-4.1` পূর্ববর্তী) Responses API এর সব ফিচার সম্পূর্ণরূপে সাপোর্ট নাও করতে পারে।
>
> পুরানো মডেলের পরিচিত সীমাবদ্ধতা:
> - **`reasoning` প্যারামিটার**: অনেক নন-রিজনিং মডেলে সাপোর্ট করে না। কেবলমাত্র মূল কোডে আগে থেকেই `reasoning` থাকলে তা মাইগ্রেট করুন।
> - **`seed` প্যারামিটার**: Responses API তে একেবারেই সাপোর্ট করে না — সব অনুরোধ থেকে এটি সরান।
> - **`text.format` এর মাধ্যমে স্ট্রাকচার্ড আউটপুট**: পুরানো মডেলগুলো হয়তো `strict: true` JSON স্কিমা নির্ভরযোগ্যভাবে প্রয়োগ করতে পারে না।
> - **টুল অর্কেস্ট্রেশন**: GPT-5+ টুল কলগুলো অভ্যন্তরীণ রিজনিং অংশ হিসেবে অর্কেস্ট্রেট করে। Responses এর পুরানো মডেলগুলো কাজ করে তবে গভীর ইন্টিগ্রেশন নেই।
> - **তাপমাত্রার সীমাবদ্ধতা**: `gpt-5` তে মাইগ্রেট করার সময় তাপমাত্রা বাদ দিতে হবে অথবা ১ এ সেট করতে হবে। পুরানো মডেলে এমন সীমাবদ্ধতা নেই।

### ও-সিরিজ রিজনিং মডেলস (o1, o3-mini, o3, o4-mini)

ও-সিরিজ মডেলগুলোর বিশেষ প্যারামিটার সীমাবদ্ধতা আছে। যারা এই মডেলগুলো টার্গেট করে এমন অ্যাপ মাইগ্রেট করবেন:

- **`temperature`**: অবশ্যই `1` হতে হবে (অথবা বাদ দিন)। ও-সিরিজ মডেল অন্য মান গ্রহণ করে না।
- **`max_completion_tokens` → `max_output_tokens`**: Azure-নির্দিষ্ট `max_completion_tokens` ব্যবহার করলে `max_output_tokens` এ স্যুইচ করুন। উচ্চ মান (৪০৯৬+) দিন কারণ রিজনিং টোকেন লিমিটের বিরুদ্ধে গুণিত হয়।
- **`reasoning_effort`**: অ্যাপ যদি `reasoning_effort` (low/medium/high) ব্যবহার করে, রাখুন — Responses API ও-সিরিজ মডেলের জন্য এই প্যারামিটার সমর্থন করে।
- **স্ট্রিমিং আচরণ**: ও-সিরিজ মডেল রিজনিং শেষ না হওয়া পর্যন্ত আউটপুট বাফার করতে পারে পূর্বে পাঠানোর পরিবর্তে। স্ট্রিমিং কাজ করবে, তবে প্রথম `response.output_text.delta` GPT মডেলগুলোর চেয়ে বেশি দেরিতে আসতে পারে।
- **`top_p`**: ও-সিরিজে সাপোর্ট করে না — থাকলে সরান।
- **টুল ব্যবহার**: ও-সিরিজ মডেল Responses API মাধ্যমে GPT মডেলের মতোই টুল সাপোর্ট করে, তবে মডেল ভেদে টুল কল অর্কেস্ট্রেশনের মান ভিন্ন হতে পারে।

**কর্ম — প্রঅ্যাকটিভ মডেল পরামর্শ**: স্ক্যান পর্যায়ে দেখুন অ্যাপ কোন মডেল টার্গেট করে (ডিপ্লয়মেন্ট নাম, env vars, কনফিগ)। যদি মডেল `gpt-4.1` পূর্ববর্তী হয় (gpt-4.1+ না), প্র ব্যবহারকারীকে বলুন:
- মাইগ্রেশন তাদের বর্তমান মডেলে বেসিক টেক্সট, চ্যাট, স্ট্রিমিং, এবং টুলসের জন্য কাজ করবে।
- নতুন মডেলগুলো (`gpt-5.1`, `gpt-5.2`) ভালো টুল অর্কেস্ট্রেশন, স্ট্রাকচার্ড আউটপুট জোরদারকরণ, রিজনিং এবং অঞ্চল পারাপার উপলব্ধতা দেয়।
- তারা আপগ্রেড করার সময় বিবেচনা করতে পারে — এটা মাইগ্রেশন ব্লক করে না।

মডেল ভার্সন ভিত্তিক মাইগ্রেশন ব্লক বা প্রত্যাখ্যান করবেন না। পরামর্শ শুধুমাত্র তথ্যবহুল।

### GitHub মডেলস Responses API সাপোর্ট করে না

> **GitHub মডেলস (`models.github.ai`, `models.inference.ai.azure.com`) Responses API সাপোর্ট করে না।**

যদি কোডবেসে GitHub মডেলস কোডপাথ থাকে (`base_url` `models.github.ai` বা `models.inference.ai.azure.com` এ নির্দেশ করে), মাইগ্রেশনের সময় **সম্পূর্ণরূপে সরিয়ে ফেলুন**। Responses API এর জন্য Azure OpenAI, OpenAI বা সামঞ্জস্যপূর্ণ লোকাল এন্ডপয়েন্ট (যেমন Ollama Responses সাপোর্টসহ) প্রয়োজন।

স্ক্যানের সময় করনীয়:
- GitHub মডেলস কোডপাথ সরানোর জন্য চিহ্নিত করুন।

---

## ফ্রেমওয়ার্ক মাইগ্রেশন

অনেক অ্যাপ OpenAI উপরে উচ্চ-স্তরের ফ্রেমওয়ার্ক ব্যবহার করে। এগুলো মাইগ্রেট করার সময়, শুধুমাত্র OpenAI কল নয়, ফ্রেমওয়ার্কের নিজস্ব API পরিবর্তন দরকার।

### Microsoft Agent Framework (MAF)

**আপনার MAF ভার্সন প্রথমে পরীক্ষা করুন** — মাইগ্রেশন নির্ভর করে আপনি MAF 1.0.0+ এ আছেন কি না বা 1.0.0 পূর্ববর্তী বিটা/RC তে আছেন।

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ইতিমধ্যে Responses API ব্যবহার করে** — মাইগ্রেশন দরকার নেই। যদি কোডবেস লিগ্যাসি `OpenAIChatCompletionClient` (যা `chat.completions.create` ব্যবহার করে) থাকে, সেটি `OpenAIChatClient` দিয়ে প্রতিস্থাপন করুন।

| পূর্বে | পরে |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

আপনার ভার্সন দেখার জন্য: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF প্রি-1.0.0 (বিটা/আরসি রিলিজ)

প্রি-1.0.0 MAF এ, `OpenAIChatClient` চ্যাট সম্পূর্ণতা ব্যবহার করত। `agent-framework-openai>=1.0.0` এ আপগ্রেড করুন যেখানে `OpenAIChatClient` ডিফল্টভাবে Responses API ব্যবহার করে।

অন্য কোন পরিবর্তন দরকার নেই — `Agent` এবং টুল API একই রকম থাকে।

### LangChain (`langchain-openai`)

`ChatOpenAI()` এ `use_responses_api=True` যোগ করুন। এছাড়াও `.content` থেকে `.text` এ রেসপন্স অ্যাক্সেস আপডেট করুন।

| পূর্বে | পরে |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

পূর্ণ পূর্ব-পরবর্তী কোড উদাহরণ জন্য দেখুন [cheat-sheet.md](./references/cheat-sheet.md)।

---

## ফ্রন্টএন্ড মাইগ্রেশন নির্দেশিকা

> **Responses API সার্ভার-সাইড বিষয়।** আপনার পাইথন ব্যাকএন্ড মাইগ্রেট করুন; ফ্রন্টএন্ডের HTTP চুক্তি অপরিবর্তিত থাকা উচিত যদি না আপনার ব্যাকএন্ড একটি পাতলা পাস-থ্রু হয় — সেই ক্ষেত্রে, অনুবাদ স্তর কমানোর জন্য Responses অনুরোধ আকৃতি গ্রহণ বিবেচনা করুন। যদি ফ্রন্টএন্ড সরাসরি ক্লায়েন্ট-সাইড কী দিয়ে OpenAI কল করে, তবে প্রথমে কলগুলো ব্যাকএন্ডে সরান।

### `@microsoft/ai-chat-protocol` অব্যবহৃতকরণ

`@microsoft/ai-chat-protocol` এনপিএম প্যাকেজটি অব্যবহৃত এবং [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) দিয়ে প্রতিস্থাপন করতে হবে। ফ্রন্টএন্ডে এটি পেলে:

১. CDN স্ক্রিপ্ট ট্যাগ প্রতিস্থাপন করুন:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
২. `AIChatProtocolClient` ইনস্ট্যান্সিয়েশন (`new ChatProtocol.AIChatProtocolClient("/chat")`) সরান।
৩. `client.getStreamedCompletion(messages)` এর পরিবর্তে সরাসরি ব্যাকএন্ড স্ট্রিমিং এন্ডপয়েন্টে `fetch()` কল দিন।
৪. `for await (const response of result)` এর পরিবর্তে `for await (const chunk of readNDJSONStream(response.body))` ব্যবহার করুন।
৫. প্রপার্টি অ্যাক্সেস আপডেট করুন `response.delta.content` / `response.error` থেকে `chunk.delta.content` / `chunk.error` এ।

---

## লক্ষ্যসমূহ

- Azure OpenAI বিরুদ্ধে চ্যাট সম্পূর্ণতা বা লিগ্যাসি সম্পূর্ণতা ব্যবহারকারী সব পাইথন কলসাইট তালিকাভুক্ত করুন।
- পাইথন কোডবেসের জন্য একটি মাইগ্রেশন পরিকল্পনা ও ক্রমানুসার প্রস্তাব করুন।
- Responses API তে স্যুইচ করার জন্য নিরাপদ, সর্বনিম্ন সম্পাদনাগুলো প্রয়োগ করুন।
- কলারদের Responses আউটপুট স্কিমা গ্রহণের জন্য আপডেট করুন; কোন ব্যাককম্প্যাট শিম নয়।
- টেস্ট/লিন্ট চালান; মাইগ্রেশন দ্বারা সৃষ্ট সামান্য ভাঙ্গন ঠিক করুন।
- ছোট, রিভিউযোগ্য পরিবর্তন সেট তৈরি করুন এবং ডিফ সহ একটি চূড়ান্ত সারাংশ দিন (কমিট করবেন না)।

---

## গার্ডরেইলস

- শুধুমাত্র গিট ওয়ার্কস্পেসের ভিতরের ফাইলগুলো সংশোধন করুন। বাইরে কোনও লেখা করবেন না।
- ব্যাকওয়ার্ড-কম্প্যাটিবিলিটি শিম সংরক্ষণ করবেন না; কোড নতুন API আকৃতিতে মাইগ্রেট করুন।
- টুম্বস্টোন/ট্রানজিশন কমেন্ট বা ব্যাকআপ ফাইল রাখবেন না।
- পূর্বে স্ট্রিমিং ব্যবহার করলেই স্ট্রিমিং বজায় রাখুন; অন্যথায় নন-স্ট্রিমিং ব্যবহার করুন।
- অনুমোদন মোডে থাকলে কমান্ড বা নেটওয়ার্ক কল চালানোর আগে অনুমতি নিন।
- `git add`/`git commit`/`git push` চালাবেন না; শুধুমাত্র ওয়ার্কিং-ট্রি সম্পাদনা দিন।

---

## ধাপ ০: Azure OpenAI ক্লায়েন্ট মাইগ্রেশন (প্রয়োজনীয় শর্ত)

যদি কোডবেস `AzureOpenAI` বা `AsyncAzureOpenAI` কনস্ট্রাক্টর ব্যবহার করে, প্রথমে স্ট্যান্ডার্ড `OpenAI` / `AsyncOpenAI` কনস্ট্রাক্টরে মাইগ্রেট করুন। Azure-নির্দিষ্ট কনস্ট্রাক্টরগুলি `openai>=1.108.1` এ অব্যবহৃত।

### কেন v1 API পাথ?

নতুন `/openai/v1` এন্ডপয়েন্ট স্ট্যান্ডার্ড `OpenAI()` ক্লায়েন্ট ব্যবহার করে `AzureOpenAI()` এর পরিবর্তে, `api_version` প্যারামিটার লাগে না, এবং OpenAI ও Azure OpenAI তে একই রকম কাজ করে। একই ক্লায়েন্ট কোড ভবিষ্যত-প্রমাণ — কোন ভার্সন ম্যানেজমেন্ট দরকার নেই।

### মূল পরিবর্তনসমূহ

| পূর্বে | পরে |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | সম্পূর্ণরূপে সরান |

### পরিষ্কারের চেকলিস্ট

- ক্লায়েন্ট নির্মাণ থেকে `api_version` আর্গুমেন্ট সরান।
- `.env`, অ্যাপ সেটিংস, Bicep/ইনফ্রা ফাইল থেকে `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` পরিবেশ ভেরিয়েবল সরান।
- `.env`, অ্যাপ সেটিংস, Bicep/ইনফ্রা ও টেস্ট ফিক্সচারে `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` পুনঃনামকরণ করুন (স্ট্যান্ডার্ড Azure Identity SDK রীতি)।
- `requirements.txt` বা `pyproject.toml` এ `openai>=1.108.1` নিশ্চিত করুন।

### পরিবেশ ভেরিয়েবল মাইগ্রেশন

| পুরাতন env var | পদক্ষেপ | টীকা |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **সরান** | v1 এন্ডপয়েন্টে `api_version` দরকার নেই |
| `AZURE_OPENAI_API_VERSION` | **সরান** | আগের মত একই |
| `AZURE_OPENAI_CLIENT_ID` | **পুনঃনামকরণ** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` এর জন্য স্ট্যান্ডার্ড Azure Identity SDK রীতি |
| `AZURE_OPENAI_ENDPOINT` | **রাখুন** | এখনও `base_url` নির্মাণে দরকার |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **রাখুন** | `responses.create` তে `model` প্যারামিটার হিসাবে ব্যবহৃত |
| `AZURE_OPENAI_API_KEY` | **রাখুন** | কী-ভিত্তিক অনুমোদনের জন্য `api_key` হিসেবে ব্যবহৃত |

ক্লায়েন্ট সেটআপ কোড উদাহরণ (সিঙ্ক, অ্যাসিঙ্ক, EntraID, API কী, মাল্টি-টেন্যান্ট) জন্য দেখুন [cheat-sheet.md](./references/cheat-sheet.md)।

---

## ধাপ ১: লিগ্যাসি কল সাইট শনাক্তকরণ

মাইগ্রেশন দরকার এমন সব কল সাইট খুঁজে পেতে [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) স্ক্রিপ্ট চালান:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

অথবা ম্যানুয়ালি নিচের অনুসন্ধানগুলো চালান — প্রতিটি ম্যাচ মাইগ্রেশন লক্ষ্য:

```bash
# লিগেসি API কলসমূহ (আবশ্যক পুনঃলিখন)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# অব্যবহৃত Azure ক্লায়েন্ট নির্মাতা (আবশ্যক প্রতিস্থাপন)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# প্রতিক্রিয়া আকৃতি প্রবেশাধিকার প্যাটার্নসমূহ (আবশ্যক আপডেট)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# পুরনো নেস্টেড ফরম্যাটে টুল ডেফিনিশনসমূহ (আবশ্যক ফ্ল্যাটেন)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# পুরনো ফরম্যাটে টুল ফলাফল (আবশ্যক function_call_output এ রূপান্তর)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# অব্যবহৃত প্যারামিটারসমূহ (আবশ্যক সরানো বা নাম পরিবর্তন)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens নামে পুনঃনামকরণ করুন
rg "['\"]seed['\"]"      # remove entirely

# অব্যবহৃত env ভেরিয়েবলসমূহ (পরিষ্কার করুন)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # এটি AZURE_CLIENT_ID হওয়া উচিত

# GitHub মডেল এন্ডপয়েন্টসমূহ (আবশ্যক সরান — প্রতিক্রিয়া API সমর্থিত নয়)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# ফ্রেমওয়ার্ক-স্তরের লিগেসি প্যাটার্নস (আবশ্যক আপডেট)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient দিয়ে প্রতিস্থাপন করুন
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True প্রয়োজন

# টেস্ট অবকাঠামো (আবশ্যক আপডেট)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# কন্টেন্ট ফিল্টার ত্রুটি বডি প্রবেশাধিকার (আবশ্যক আপডেট — কাঠামো পরিবর্তিত)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # পুরনো একবচন ফরম — এখন content_filter_results (বহুবচন) content_filters অ্যারের ভিতরে

# Chat Completions এন্ডপয়েন্টে র ল HTTP কলসমূহ (আবশ্যক URL আপডেট)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### হিউরিস্টিকস (সনাক্তকরণ ও পুনঃলিখন)

- **চ্যাট সম্পূর্ণতা ক্লায়েন্ট**: `client.chat.completions.create` → `client.responses.create(...)`।

- **Azure ক্লায়েন্ট কনস্ট্রাক্টর**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`।
- **টুলস**: ফাংশন-কলে টুল সংজ্ঞাগুলো nested ফরম্যাট থেকে (`{"type": "function", "function": {"name": ...}}`) ফ্ল্যাট Responses ফরম্যাটে কনভার্ট করুন (`{"type": "function", "name": ...}`); `tool_choice` ব্যবহার করুন; টুল রেজাল্ট `{"type": "function_call_output", "call_id": ..., "output": ...}` আইটেম হিসেবে রিটার্ন করুন (না যে `{"role": "tool", ...}`)।
- **টুল রাউন্ড-ট্রিপস**: যখন মডেল ফাংশন কল রিটার্ন করে, তখন `response.output` আইটেমগুলো কনভারসেশনে অ্যাপেন্ড করুন (ম্যানুয়াল `{"role": "assistant", "tool_calls": [...]}` ডিক্ট নয়), তারপর প্রতিটি রেজাল্টের জন্য `function_call_output` আইটেম অ্যাপেন্ড করুন।
- **ফিউ শট টুল উদাহরণ**: যদি কনভারসেশনে হার্ডকোডেড টুল কল উদাহরণ থাকে, সেগুলো `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` আইটেমে রূপান্তর করুন। আইডিগুলো অবশ্যই `fc_` দিয়ে শুরু হতে হবে।
- **`pydantic_function_tool()`**: এই হেল্পার এখনও পুরানো nested ফরম্যাট তৈরি করে এবং এটি `responses.create()` এর সাথে **অসঙ্গত**। ম্যানুয়াল টুল সংজ্ঞা বা ফ্ল্যাটেনিং র‍্যাপার দিয়ে বদলান।
- **মাল্টি-টার্ন**: অ্যাপে কনভারসেশন হিস্ট্রি বজায় রাখুন; পূর্বের টার্নগুলো `input` আইটেমের মাধ্যমে পাঠান।
- **ফরম্যাটিং**: Chat এর টপ-লেভেল `response_format` কে Responses এর `text.format` দিয়ে বদলান। canonical শেপ: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`।
- **কন্টেন্ট আইটেমস**: User/System টার্নের জন্য Chat এর `content[].type: "text"` কে Responses এর `content[].type: "input_text"` দিয়ে প্রতিস্থাপন করুন।
- **ইমেজ কন্টেন্ট আইটেমস**: Chat এর `content[].type: "image_url"` কে Responses এর `content[].type: "input_image"` দিয়ে প্রতিস্থাপন করুন। `image_url` ফিল্ড nested অবজেক্ট থেকে `{"url": "..."}` ফ্ল্যাট স্ট্রিং এ পরিবর্তিত হয়েছে। আগে/পরে উদাহরণের জন্য চিট শীট দেখুন।
- **রিজনিং প্রয়াস**: **শুধুমাত্র তখনই `reasoning` মাইগ্রেট করুন যখন মূল কোডে এটি ইতিমধ্যে বিদ্যমান থাকে**।
- **কন্টেন্ট ফিল্টার এরর হ্যান্ডলিং**: এরর বডির স্ট্রাকচার পরিবর্তিত হয়েছে। Chat Completions ব্যবহার করত `error.body["innererror"]["content_filter_result"]` (একবچন); Responses API ব্যবহার করে `error.body["content_filters"][0]["content_filter_results"]` (বহুবচন, একটি অ্যারের ভিতরে)। `innererror` অ্যাক্সেস করলে `KeyError` উঠবে। নতুন পথ ব্যবহার করে পুনর্লিখন করুন।
- **র’ ড HTTP কল**: যদি অ্যাপ সরাসরি Azure OpenAI REST API কল করে (যেমন `requests`, `httpx` ইত্যাদি দিয়ে) `/openai/deployments/{name}/chat/completions?api-version=...` ব্যবহার করে, তবে এটি `/openai/v1/responses` এ রিরাইট করুন। রিকোয়েস্ট বডি পরিবর্তিত হয়েছে: `messages` → `input`, `max_output_tokens` এবং `store: false` যোগ করুন, `api-version` কোয়েরি প্যারাম রিমুভ করুন। রেসপন্স বডি পরিবর্তিত হয়েছে: `choices[0].message.content` → `output[0].content[0].text` (জরিপ: `output_text` একটি SDK সুবিধাজনক প্রপার্টি, কাঁচা REST JSON-এ নেই)।

---

## ধাপ ২: মাইগ্রেশন প্রয়োগ করুন

### মাইগ্রেশন নোটস (Chat Completions → Responses)

- **কেন মাইগ্রেট করবেন**: Responses API হলো texts, tools, এবং streaming এর জন্য একীভূত API; Chat Completions হলো পুরনো Legacy। GPT-5 এর সাথে Responses সেরা পারফরম্যান্সের জন্য প্রয়োজন।
- **HTTP**: Azure endpoint পরিবর্তিত হয়েছে `/openai/deployments/{name}/chat/completions` থেকে `/openai/v1/responses`।
- **ফিল্ডস**: `messages` → `input`, `max_tokens` → `max_output_tokens`; `temperature` অপরিবর্তিত।
- **ফরম্যাটিং**: `response_format` → `text.format` (সঠিক অবজেক্ট সহ)।
- **কন্টেন্ট আইটেমস**: সিস্টেম/ইউজার টার্নের জন্য Chat এর `content[].type: "text"` কে Responses এর `content[].type: "input_text"` দিয়ে বদলান।
- **ইমেজ কন্টেন্ট আইটেমস**: Chat এর `content[].type: "image_url"` কে Responses এর `content[].type: "input_image"` দিয়ে বদলান। `image_url` ফিল্ড `{"image_url": {"url": "..."}}` থেকে ফ্ল্যাট `{"image_url": "..."}` (সরাসরি স্ট্রিং - HTTPS URL অথবা `data:image/...;base64,...` ডাটা URI) এ রূপান্তর করুন।

### প্যারামিটার ম্যাপিং রেফারেন্স

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (আইটেম অ্যারের মধ্যে) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (অবজেক্ট) |
| `temperature` | `temperature` (অপরিবর্তিত) |
| `stop` | `stop` (অপরিবর্তিত) |
| `frequency_penalty` | `frequency_penalty` (অপরিবর্তিত) |
| `presence_penalty` | `presence_penalty` (অপরিবর্তিত) |
| `tools` / function-calling | `tools` (অপরিবর্তিত) |
| `seed` | **অপসারণ করুন** (সমর্থিত নয়) |
| `store` | `store` (সেট করুন `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ফ্ল্যাট স্ট্রিং) |

সম্পূর্ণ আগে/পরে কোড উদাহরণগুলোর জন্য [cheat-sheet.md](./references/cheat-sheet.md) দেখুন।

টেস্ট ইনফ্রাস্ট্রাকচার মাইগ্রেশন (মক্স, স্ন্যাপশট, অ্যাসারশন) এর জন্য [test-migration.md](./references/test-migration.md) দেখুন।

সমস্যা সমাধান জন্য, এরর ও gotchas দেখতে [troubleshooting.md](./references/troubleshooting.md) দেখুন।

---

## ডাটা রিটেনশন ও স্টেট

- সব Responses রিকোয়েস্টে `store: false` সেট করুন।
- পূর্বের মেসেজ আইডি বা সার্ভার-স্টোরড কনটেক্সটের উপর নির্ভর করবেন না; স্টেট ক্লায়েন্ট-ব্যবস্থাপিত রাখুন এবং মেটাডেটা কমিয়ে আনুন।

---

## গ্রহণযোগ্যতার মানদণ্ড

### কোড-লেভেল গেটসমূহ (সব পাস করতে হবে)

- [ ] মাইগ্রেট করা ফাইলগুলিতে `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` জন্য ০টি ম্যাচ।
- [ ] সব কনস্ট্রাক্টর `AzureOpenAI\(|AsyncAzureOpenAI\(` খুঁজে পাওয়া যাবে না — সব কনস্ট্রাক্টর v1 endpoint সহ `OpenAI`/`AsyncOpenAI` ব্যবহার করে।
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` এর জন্য ০টি ম্যাচ — GitHub Models কোডপাথ মুছে ফেলা হয়েছে।
- [ ] `rg "OpenAIChatCompletionClient"` এর জন্য ০টি ম্যাচ — MAF 1.0.0+ কোডে `OpenAIChatClient` ব্যবহার হয় (যা Responses API ব্যবহার করে)। pre-1.0.0 এ `agent-framework-openai>=1.0.0` এ আপগ্রেড করুন।
- [ ] সব `ChatOpenAI(...)` কল `use_responses_api=True` অন্তর্ভুক্ত করে।
- [ ] `rg "choices\[0\]"` এর জন্য ০টি ম্যাচ — সব রেসপন্স অ্যাক্সেস `resp.output_text` অথবা Responses আউটপুট স্কিমা ব্যবহার করে।
- [ ] টপ-লেভেলে কোনো `response_format` নেই; সব স্ট্রাকচার্ড আউটপুট `text={"format": {...}}` ব্যবহার করে।
- [ ] `requirements.txt` বা `pyproject.toml` এ `openai>=1.108.1` এবং `azure-identity` আছে; ডিপেন্ডেন্সি পুনরায় ইনস্টল করা হয়েছে।
- [ ] সব `responses.create` কল এ `store=False` সেট করা হয়েছে।
- [ ] ক্লায়েন্ট নির্মাণে কোনো `api_version` নেই; env ফাইল ও ইনফ্রা থেকে `AZURE_OPENAI_API_VERSION` সরানো হয়েছে।

### টেস্ট ইনফ্রাস্ট্রাকচার গেট (সব পাস করতে হবে)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` এর জন্য ০টি ম্যাচ।
- [ ] `rg "_azure_ad_token_provider" tests/` এর জন্য ০টি ম্যাচ — অ্যাসারশনগুলো আপডেট হয়েছে `isinstance(client, AsyncOpenAI)` অথবা `base_url` চেক করার জন্য।
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` এর জন্য ০টি ম্যাচ — অ্যাজুর-স্পেসিফিক ফিল্টার মকস রিমুভ করা হয়েছে।
- [ ] মক ফিক্সচারগুলো `kwargs.get("input")` ব্যবহার করে, `kwargs.get("messages")` নয়।
- [ ] স্ন্যাপশট / গোল্ডেন ফাইলগুলো Responses স্ট্রিমিং শেপ অনুসারে আপডেট হয়েছে (কোনো `choices[0]`, `function_call`, `logprobs` ইত্যাদি নেই)।
- [ ] সব টেস্ট `pytest` দিয়ে জিরো ফেইলিউরে পাস হয়েছে।

### আচরণগত গেট (ম্যানুয়ালি বা টেস্ট হারনেস দিয়ে যাচাই করুন)

- [ ] **মৌলিক কমপ্লিশন**: নন-স্ট্রিমিং `responses.create` নন-এম্পটি `output_text` রিটার্ন করে।
- [ ] **স্ট্রিম প্যারিটি**: যদি পূর্বের কোড স্ট্রিমিং ব্যবহার করে, মাইগ্রেটেড কোড স্ট্রিম করে এবং নন-এম্পটি ডেল্টাস সহ `response.output_text.delta` ইভেন্ট তৈরি করে।
- [ ] **স্ট্রাকচার্ড আউটপুট**: `text.format` (json_schema সহ) ব্যবহৃত হলে, `json.loads(resp.output_text)` সফল হয় এবং স্কিমার সাথে মেলে।
- [ ] **টুল-কল লুপ**: যদি টুল ব্যবহৃত হয়, মডেল টুল কল ইস্যু করে, অ্যাপ এগুলো এক্সিকিউট করে, এবং পরবর্তী রিকোয়েস্ট একটি চূড়ান্ত `output_text` রিটার্ন করে (অসীম লুপ নয়)।
- [ ] **অ্যাসিঙ্ক প্যারিটি**: যদি `AsyncAzureOpenAI` ব্যবহার করা হয়, `AsyncOpenAI` এর সমতুল্য `await` সহ কাজ করে।
- [ ] **এরর রেট**: প্রি-মাইগ্রেশন বেসলাইন থেকে কোনো নতুন 400/401/404 এরর নেই।

### ডেলিভারেবলস

- সারসংক্ষেপে এডিট করা ফাইল, আগে/পরে লেগ্যাসি কল সাইট গণনা, এবং পরবর্তী ধাপ যুক্ত থাকতে হবে।
- পরিবর্তন গুলো ওয়ার্কিং-ট্রি এডিট শুধু (কমিট নয়)।

---

## SDK সংস্করণ প্রয়োজনীয়তা

| প্যাকেজ | সর্বনিম্ন সংস্করণ |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | সর্বশেষ (EntraID অথেন্টিকেশনের জন্য) |

---

## রেফারেন্সসমূহ

- [চিট শীট — সব কোড স্নিপেট](./references/cheat-sheet.md)
- [টেস্ট মাইগ্রেশন — মক, স্ন্যাপশট, অ্যাসারশন](./references/test-migration.md)
- [ট্রাবলশুটিং — এরর, ঝুঁকির তালিকা, গটচাস](./references/troubleshooting.md)
- [detect_legacy.py — অটোমেটেড স্ক্যানার](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API ডকুমেন্টেশন](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API সংস্করণের জীবনচক্র](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API রেফারেন্স](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->