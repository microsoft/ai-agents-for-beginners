# পরিবর্তনলিপি

**AI Agents for Beginners** কোর্সের সমস্ত উল্লেখযোগ্য পরিবর্তন এই ফাইলে নথিভুক্ত করা হয়েছে।

## [রিলিজড] — ২০২৬-০৭-১৪

এই রিলিজটি কোর্সটিকে দুটি নতুন-অবসুন্ন ভাবে ঘোষিত মডেল থেকে সরিয়ে নিয়ে যায়, বাকি লেসনের নোটবুকগুলোকে স্থিতিশীল Microsoft Agent Framework API তে মাইগ্রেট করে, এবং Python নোটবুকগুলোকে একটি লাইভ Microsoft Foundry ডিপ্লয়মেন্টের বিরুদ্ধে যাচাই করে।

### পরিবর্তিত

- **অবসুন্ন মডেল থেকে সরানো হয়েছে (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`)।** `gpt-4.1` এবং `gpt-4.1-mini` এখন অবসুন্ন (প্রকাশিত অবসর তারিখ **১৪ অক্টোবর ২০২৬**)। প্রতিটি কোর্স রেফারেন্স (ডকুমেন্ট, `.env.example`, Python/.NET নোটবুক এবং স্যাম্পল) অবসুন্ন নয় এমন `gpt-5-mini` দিয়ে প্রতিস্থাপন করা হয়েছে। লেসন ১৬ এর মডেল-রাউটিং উদাহরণে `gpt-5-nano` (ছোট) এবং `gpt-5-mini` (বড়) ব্যবহার করে একটি ছোট/বড় পার্থক্য রক্ষা করা হয়েছে। তৃতীয় পক্ষের ফাইলগুলো ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), ঐতিহাসিক GitHub Models টেক্সট, এবং `azure-openai-to-responses` স্কিলের সক্ষমতা নোট স্বেচ্ছায় অপরিবর্তিত রাখা হয়েছে।
- **লেসন ১৪ হ্যান্ডঅফ নোটবুক স্থিতিশীল API তে মাইগ্রেট করা হয়েছে।** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) এখন `agent_framework.orchestrations.HandoffBuilder` ব্যবহার করে `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type`-ভিত্তিক স্ট্রিমিং, এবং `FoundryChatClient` (পূর্বে ব্যবহৃত pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` প্রতীকগুলি পরিবর্তে)।
- **লেসন ১৪ মানব-ইন-দ্য-লুপ নোটবুক স্থিতিশীল API তে মাইগ্রেট করা হয়েছে।** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) এখন `ctx.request_info(...)` + `@response_handler` (পুরানো `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` এর পরিবর্তে), `WorkflowBuilder(start_executor=..., output_executors=[...])` দিয়ে বিল্ড করে, `default_options={"response_format": ...}` এর মাধ্যমে কাঠামোগত আউটপুট প্রদান করে এবং একটি স্ক্রিপ্টেড উত্তর ব্যবহার করে যাতে নোটবুকটি অবরুদ্ধ `input()` ছাড়াই নির্বিঘ্নে চলে।
- **পরিবেশ কনফিগারেশন** ([.env.example](../../.env.example)): মডেল ডিপ্লয়মেন্ট নামগুলো `gpt-5-mini` তে পরিবর্তিত হয়েছে; যুক্ত করা হয়েছে `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (লেসন ১৬ রাউটিং) এবং পূর্বে অনুপস্থিত `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (লেসন ১৫ ব্রাউজার-ব্যবহার)।
- **নির্ভরশীলতা** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry`, এবং `agent-framework-openai` কে `~=1.10.0` এ পিন করা হয়েছে একটি স্বকীয় এবং যাচাই করা সেটের জন্য (1.11.0 আসছে এই লেসনগুলোর ব্যবহৃত সারফেসে পরীক্ষামূলক পরিবর্তন সহ)।

### নোটস এবং পরিচিত সীমাবদ্ধতাসমূহ

- **লাইভ Microsoft Foundry এর বিরুদ্ধে যাচাই করা হয়েছে।** Python নোটবুকগুলো `nbconvert` দিয়ে হেডলেস চালানো হয়েছে Microsoft Foundry প্রজেক্টের বিরুদ্ধে `gpt-5-mini` (এবং লেসন ১৬ রাউটিং এর জন্য `gpt-5-nano`) ব্যবহার করে। আপনার নিজের প্রজেক্টে সমতুল্য অবসুন্ন নয় এমন মডেলগুলো ডিপ্লয় করুন; নোটবুকগুলো `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` থেকে ডিপ্লয়মেন্ট নাম পড়ে।
- **কিছু লেসনের জন্য অতিরিক্ত রিসোর্স এখনো প্রয়োজন।** লেসন ০৫ এর জন্য Azure AI Search প্রয়োজন; লেসন ০৮ Bing-গ্রাউন্ডিং ওয়ার্কফ্লো (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) এর জন্য Bing সংযোগ এবং Microsoft Foundry Agent Service হোস্টেড টুলস আবশ্যক; লেসন ১৩ (Cognee) এবং লেসন ১৭ (Foundry Local) তাদের নিজস্ব রানটাইম প্রয়োজন।

## [রিলিজড] — ২০২৬-০৭-১৩

এই রিলিজে দুটি নতুন লেসন যোগ করা হয়েছে যা ডিপ্লয়মেন্ট আর্ক সম্পূর্ণ করে—এজেন্টগুলো Microsoft Foundry পর্যন্ত স্কেল করা এবং একটি সিঙ্গেল ওয়ার্কস্টেশনে ডাউন করা—সাথে একটি স্মোক-টেস্ট পাইপলাইন, নতুন কোর্স নেভিগেশন, নতুন শেখার দক্ষতা এবং হালনাগাদ ব্র্যান্ডিং।

### যোগ করা হয়েছে

- **লেসন ১৬ — Microsoft Foundry দিয়ে স্কেলযোগ্য এজেন্ট ডিপ্লয়মেন্ট।** নতুন লেসন [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) এবং রানযোগ্য নোটবুক [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) একটি প্রোডাকশন কাস্টমার-সাপোর্ট এজেন্ট তৈরি করে (টুলস, RAG, মেমোরি, মডেল রাউটিং, রেসপন্স ক্যাশিং, মানব অনুমোদন, একটি মূল্যায়ন গেট, এবং OpenTelemetry ট্রেসিং), ডেভেলপমেন্ট/ডিপ্লয়মেন্ট/রানটাইম মেরমেইড ডায়াগ্রাম, জ্ঞান যাচাইকরণ, অ্যাসাইনমেন্ট এবং চ্যালেঞ্জ সহ।
- **লেসন ১৭ — Foundry Local এবং Qwen দিয়ে স্থানীয় AI এজেন্ট তৈরি।** নতুন লেসন [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) এবং নোটবুক [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) সম্পূর্ণ অন-ডিভাইস ইঞ্জিনিয়ারিং অ্যাসিস্ট্যান্ট তৈরি করে (Foundry Local এর মাধ্যমে Qwen ফাংশন কলিং, স্যান্ডবক্সড ফাইল টুলস, লোকাল RAG চরমা সহ, ঐচ্ছিক লোকাল MCP), লোকাল-অনুভূত / লোকাল-RAG / টুল কলিং ডায়াগ্রাম, জ্ঞান যাচাইকরণ, অ্যাসাইনমেন্ট এবং চ্যালেঞ্জ সহ।
- **স্মোক-টেস্ট পাইপলাইন।** নতুন [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) ওয়ার্কফ্লো [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) প্লাস লেসন ০১, ০৪, ০৫, এবং ১৬ এর ডিপ্লয়েবল এজেন্টগুলোর জন্য [tests/](./tests/README.md) এর অধীনে পার-লেসন ক্যাটালগ, প্রতিটি ক্যাটালগ তার লেসন এবং হোস্টেড-এজেন্ট নামের সাথে যুক্ত একটি ইনডেক্স README সহ। লেসন ১৬ একটি "স্মোক টেস্টসহ ডিপ্লয়ড এজেন্ট যাচাই" বিভাগ পেয়েছে; লেসন ০১/০৪/০৫ একটি ঐচ্ছিক স্মোক-টেস্ট পয়েন্টার পেয়েছে।
- **শিক্ষার্থী দক্ষতা।** নতুন Agent Skills `.agents/skills/` এর মধ্যে: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (লেসন ১৬ এবং ১৭ এর নির্দেশনা প্যাকেজিং), এবং [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (কিভাবে নোটবুক স্যাম্পলগুলো লাইভ Microsoft Foundry / Azure OpenAI সেটআপের বিরুদ্ধে যাচাই করবেন)।
- **নোটবুক যাচাইকরণ চালক।** নতুন [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) যা প্রতিটি Python নোটবুক `nbconvert` দিয়ে হেডলেস এক্সিকিউট করে এবং PASS/FAIL ম্যাট্রিক্স (সাথে `results.json`) প্রিন্ট করে। এটি স্বয়ংক্রিয়ভাবে রিপো রুট এবং Python সনাক্ত করে, ডিফল্টরূপে কোর্স নয় এমন নোটবুক(excludes `.venv`, `site-packages`, `translations`, স্কিল টেমপ্লেট অ্যাসেটস) এবং `.NET` নোটবুকগুলো বাদ দেয়, এবং `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, এবং `-Python` সমর্থন করে।
- **কোর্স নেভিগেশন।** লেসন ১১–১৫ এ পূর্বের/পরবর্তী লেসন লিঙ্ক যোগ করা হয়েছে (আগে অনুপস্থিত ছিল) যাতে পুরো কোর্স ০০ থেকে ১৮ উভয় দিকে যুক্ত থাকে।
- **নতুন থাম্বনেইল।** লেসন ১৬ এবং ১৭ এর থাম্বনেইল, প্লাস রিফ্রেশড রিপোজিটরি সোশাল ইমেজ [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (এখন দুই নতুন লেসন এবং `aka.ms/ai-agents-beginners` URL প্রচার করছে)।
- **নির্ভরশীলতা** ([requirements.txt](../../requirements.txt)): লেসন ১৭ এর জন্য `foundry-local-sdk` এবং `chromadb` যোগ করা হয়েছে।

### পরিবর্তিত

- **মুল [README.md](./README.md)** লেসন টেবিল: লেসন ১৬ এবং ১৭ এখন তাদের কন্টেন্টের লিঙ্ক ধরে (আগে "শীঘ্রই আসছে" ছিল); রিপোজিটরি ইমেজ `repo-thumbnailv3.png`-এ আপডেট করা হয়েছে।
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: লেসন বাই লেসন গাইড এবং লার্নিং পাথ এ লেসন ১৬ এবং ১৭ যোগ করা হয়েছে, এবং একটি "স্মোক টেস্ট দিয়ে ডিপ্লয়ড এজেন্ট যাচাই" সেকশন।
- **[AGENTS.md](./AGENTS.md)**: লেসনের সংখ্যা / বর্ণনা (০০–১৮) আপডেট করা হয়েছে, স্মোক-টেস্টিং যাচাইকরণ সেকশন যোগ করা হয়েছে, এবং লেসন ১৬/১৭ এর স্যাম্পল নামকরণের উদাহরণ যোগ করা হয়েছে।
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "পূর্বের লেসন" এখন লেসন ১৭-এ নির্দেশ করে (আগে লেসন ১৫ ছিল), চেইন বন্ধ করেছে।
- **অবসুন্ন নয় এমন মডেলে স্ট্যান্ডার্ডাইজড রেফারেন্স।** পুরো কোর্সে (`gpt-4o` / `gpt-4o-mini` রেফারেন্স, ডকস, `.env.example`, Python/.NET নোটবুক এবং স্যাম্পল) `gpt-4.1-mini` দিয়ে প্রতিস্থাপন করা হয়েছে— `gpt-4o` (সকল সংস্করণ) ২০২৬ সালে অবসর নিচ্ছে। লেসন ১৬ এর মডেল রাউটিং উদাহরণে `gpt-4.1-mini` (ছোট) এবং `gpt-4.1` (বড়) ব্যবহার করে একটি ছোট/বড় পার্থক্য রাখা হয়েছে। Python নোটবুকগুলো এখন মডেল নাম হার্ড-কোড করার পরিবর্তে পরিবেশ ভেরিয়েবল থেকে (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) মডেল নির্বাচন করে।

### নোটস এবং পরিচিত সীমাবদ্ধতাসমূহ

- **লাইভ Azure এর বিরুদ্ধে চালানো হয়নি।** নতুন লেসনের নোটবুকগুলো শিক্ষামূলক স্যাম্পল; এগুলো আপনার নিজস্ব Microsoft Foundry / Foundry Local সেটআপে চালিয়ে যাচাই করুন। স্মোক-টেস্ট ওয়ার্কফ্লো চলতে লেসনের এজেন্ট ডিপ্লয় করে Azure OIDC গোপন (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) Foundry প্রজেক্ট স্কোপে **Azure AI User** ভূমিকা দিয়ে কনফিগার করা আবশ্যক।
- **লেসন ১৭ একমাত্র লোকাল।** এটি কোনো Foundry Responses এন্ডপয়েন্ট নেই, তাই স্মোক-টেস্ট অ্যাকশন প্রযোজ্য নয়; এটি যাচাই করতে আপনার ওয়ার্কস্টেশনে নোটবুকটি চালান।

## [রিলিজড] — ২০২৬-০৭-০৬

এই রিলিজটি কোর্সটিকে **Azure OpenAI Responses API** এ মাইগ্রেট করে, পণ্যের নামকরণ স্ট্যান্ডার্ডাইজ করে **Microsoft Foundry** এবং **Microsoft Agent Framework (MAF)** উপর, GitHub Models অবসান ঘটায়, SDK সংস্করণ আপডেট করে, এবং স্থানীয় মডেল ও Foundry তে অন্যান্য ফ্রেমওয়ার্ক হোস্টিং নিয়ে নতুন বিষয়বস্তু যোগ করে।

### যোগ করা হয়েছে

- **মাইগ্রেশন স্কিল** — [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill ইনস্টল করা হয়েছে `.agents/skills/` এ, এর রেফারেন্স এবং স্ক্যানার স্ক্রিপ্টসহ (উৎস: [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses))।
- **Foundry Local (ডিভাইসে মডেল চালানো)** — [00-course-setup/README.md](./00-course-setup/README.md) এ নতুন "বিকল্প প্রদানকারী: Foundry Local" সেকশন, যা ইনস্টলেশন (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, এবং Microsoft Agent Framework এ `FoundryLocalManager` সংযোগ সম্পর্কে।
- **Microsoft Foundry তে LangChain / LangGraph এজেন্ট হোস্টিং** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) এ নতুন সেকশন এবং রানযোগ্য স্যাম্পল [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) যা `langchain-azure-ai[hosting]` এবং `ResponsesHostServer` ( `/responses` প্রোটোকল) ব্যবহার করে, ভিত্তি: [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)।
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) এ নতুন "বাস্তব বিশ্বের উদাহরণ: Microsoft Project Opal" সেকশন, Opal কে একজন এন্টারপ্রাইজ কম্পিউটার-ব্যবহার এজেন্ট হিসেবে উপস্থাপন করে এবং কোর্সের ধারণাগুলোর সাথে মানায় (মানব-ইন-দ্য-লুপ, বিশ্বাস/নিরাপত্তা, পরিকল্পনা, স্কিল)।
- **দ্বিতীয় লেসন ০২ Python স্যাম্পল** — যোগ করা হয়েছে [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) ("পরিবর্তিত" দেখুন — পুরাতন Semantic Kernel নোটবুক থেকে মাইগ্রেট করা) এবং লেসন README তে লিঙ্ক করা হয়েছে।
- **মডেল এবং প্রোভাইডারস** সেকশন [STUDY_GUIDE.md](./STUDY_GUIDE.md) এ যোগ করা হয়েছে।

### পরিবর্তিত

- **Chat Completions → Responses API (Python)।** যেসব স্যাম্পল সরাসরি মডেল কল করত সেগুলো Chat Completions থেকে Responses API তে মাইগ্রেট করা হয়েছে (`client.responses.create(input=..., store=False)`, `resp.output_text`), `OpenAI` ক্লায়েন্ট ব্যবহার করে স্টেবল Azure OpenAI `/openai/v1/` এন্ডপয়েন্টের বিরুদ্ধে (কোন `api_version` নেই)। প্রভাবিত স্যাম্পলগুলো:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — সম্পূর্ণ ফাংশন-কলিং ওয়াকথ্রু (টুল স্কিমা Responses ফরম্যাটে ফ্ল্যাটেন করা, টুল রেজাল্ট `function_call_output`, `max_output_tokens` ইত্যাদি হিসাবে ফেরত)।

- **GitHub মডেল → Azure OpenAI।** GitHub মডেলগুলি অব্যবহৃত হচ্ছে (সারি হচ্ছে **জুলাই 2026**-এ) এবং এটি Responses API সমর্থন করে না। সমস্ত GitHub মডেল কোড পাথগুলি Python ও .NET নমুনায় Azure OpenAI / Microsoft Foundry তে রূপান্তরিত হয়েছে:
  - Python: পাঠ 08 ওয়ার্কফ্লো নোটবুক (`01`–`03`), পাঠ 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)।
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + সংযুক্ত `.md` ডকুমেন্টগুলি, এবং পাঠ 08 dotNET ওয়ার্কফ্লো নোটবুক/`.md` (`01`–`03`) এখন `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` ব্যবহার করে `AzureCliCredential` সহ।
- **Semantic Kernel → Microsoft Agent Framework।** প্রাক্তন `02-semantic-kernel.ipynb` পুনর্লিখিত হয়েছে Microsoft Agent Framework সহ Azure OpenAI (Responses API) ব্যবহার করে এবং এর নাম পরিবর্তন করে `02-python-agent-framework-azure-openai.ipynb` করা হয়েছে।
- **`FoundryChatClient` + `as_agent` তে স্ট্যান্ডার্ডাইজ করা হয়েছে।** README এবং নোটবুক কোড যা `AzureAIProjectAgentProvider` উল্লেখ করেছে তা পাঠ 01 এবং ফ্রেমওয়ার্কের নিজস্ব নমুনাগুলিতে ব্যবহৃত প্রচলিত প্যাটার্নে স্ট্যান্ডার্ডাইজ করা হয়েছে: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` সহ `provider.as_agent(...)`। এটি পাঠ 02–14-এর README ও নোটবুকগুলোতে আপডেট করা হয়েছে (যেমন, পাঠ 13 মেমোরি, সমস্ত পাঠ 14 নোটবুক, `11-agentic-protocols/code_samples/github-mcp/app.py`)।
- **পণ্য নামকরণ।** ইংরেজি বিষয়বস্তু জুড়ে নাম পরিবর্তন করা হয়েছে:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (পরিবর্তন করেনি: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", এবং পরিবেশ-চর পরিবর্তনশীল নামসমূহ।)
- **নির্ভরশীলতা** ([requirements.txt](../../requirements.txt)):
  - পিন করা হয়েছে `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`।
  - পিন করা হয়েছে `openai>=1.108.1` (Responses API এর জন্য ন্যূনতম)।
  - সরানো হয়েছে `azure-ai-inference` (মাইগ্রেট করা GitHub মডেল নমুনাগুলিতে ব্যবহৃত ছিল)।
- **পরিবেশ কনফিগারেশন** ([.env.example](../../.env.example)): GitHub মডেল ভেরিয়েবলগুলি (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) সরানো হয়েছে; যোগ করা হয়েছে `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, এবং ঐচ্ছিক `AZURE_OPENAI_API_KEY`; নামকরণ আপডেট করা হয়েছে Microsoft Foundry অনুসারে।
- **ডকুমেন্টেশন** — উপরের জন্য আপডেট করা হয়েছে [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), এবং [STUDY_GUIDE.md](./STUDY_GUIDE.md) (পরিবেশ ভেরিয়েবল সেটআপ, যাচাইকরণ স্নিপেট, প্রদানকারী নির্দেশিকা, নামকরণ)।

### সরানো হয়েছে

- GitHub মডেল অনবোর্ডিং ধাপ এবং পরিবেশ ভেরিয়েবলগুলি সেটআপ ডকুমেন্টগুলি থেকে (Azure OpenAI / Microsoft Foundry দ্বারা প্রতিস্থাপিত)।

### নিরাপত্তা / গোপনীয়তা (সর্বজনীন শেয়ার ক্লিনআপ)

- সত্যিকার **Azure সাবস্ক্রিপশন আইডি**, রিসোর্স-গ্রুপ / রিসোর্স নাম, এবং Bing কানেকশন আইডি, সাথে ডেভেলপার **স্থানীয় ফাইল পাথ এবং ব্যবহারকারীর নাম** ফাঁস হওয়া Jupyter নোটবুক এক্সিকিউশন আউটপুটগুলি মুছে ফেলা হয়েছে:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- নিশ্চিত করা হয়েছে ট্র্যাককৃত ইংরেজি বিষয়বস্তুতে কোন API কী, টোকেন, সাবস্ক্রিপশন আইডি অথবা ব্যক্তিগত পাথ অবশিষ্ট নেই (অবশিষ্ট `GITHUB_TOKEN` উল্লেখগুলি হলো GitHub Actions টোকেন ও লেসন 11 সেটআপে GitHub MCP সার্ভার PAT — উভয়ই বৈধ এবং GitHub মডেলের সাথে সম্পর্কহীন)।

### নোট এবং পরিচিত সীমাবদ্ধতা

- **চালানো/কম্পাইল করা হয়নি।** এগুলো API/নামকরণের সঠিকতার জন্য আপডেটকৃত শিক্ষামূলক নমুনা; সেগুলো সরাসরি Azure রিসোর্সের বিরুদ্ধে চালানো হয়নি, এবং .NET নমুনাগুলো এই পরিবেশে কম্পাইল হয়নি। নিজের Microsoft Foundry / Azure OpenAI ডিপ্লয়মেন্টে যাচাই করুন।
- **মডেল ডিপ্লয়মেন্ট Responses API সমর্থন করতে হবে।** `gpt-4.1-mini`, `gpt-4.1`, অথবা `gpt-5.x` মডেলের মত একটি ডিপ্লয়মেন্ট ব্যবহার করুন। পুরোনো মডেলগুলো Responses এর মূল ক্ষমতা সমর্থন করে, কিন্তু প্রতিটি বৈশিষ্ট্য নয়।
- **Agent-framework সংস্করণ।** নমুনাগুলো সর্বশেষ MAF (`>=1.10.0`) লক্ষ করে তৈরি। প্রচলিত এজেন্ট-তৈরির কল হচ্ছে `client.as_agent(...)`; API গুলো ফ্রেমওয়ার্কের প্রকাশিত ডকস এবং ইনস্টল করা বিল্ডের বিরুদ্ধে যাচাই করা হয়েছে। আপনি যদি ভিন্ন সংস্করণ ব্যবহার করেন, তবে পদ্ধতির উপলভ্যতা নিশ্চিত করুন (`as_agent` বনাম `create_agent`)।
- **পাঠ 08 ওয়ার্কফ্লো নোটবুক 04** ইচ্ছাকৃতভাবে `AzureAIAgentClient` (যা `agent-framework-azure-ai` থেকে) রাখে কারণ এটি Microsoft Foundry Agent Service হোস্টেড টুল ব্যবহার করে (Bing grounding, কোড ইন্টারপ্রিটার); এটি ইতিমধ্যে Responses-ভিত্তিক।
- **.NET ডিফল্ট ডিপ্লয়মেন্ট।** পূর্বে পাঠ 08 dotNET ওয়ার্কফ্লো নমুনা দুটি একটি নির্দিষ্ট মডেল হার্ড-কোড করেছিল; এখন তারা ডিফল্ট করে `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) ব্যবহার করে। যদি একটি নমুনা মাল্টিমোডাল/ভিশন ইনপুটের উপর নির্ভরশীল হয়, তাহলে `AZURE_OPENAI_DEPLOYMENT` একটি উপযুক্ত মডেলে সেট করুন।
- **Foundry Local** একটি OpenAI-অনুকূল **Chat Completions** endpoint প্রকাশ করে এবং স্থানীয় উন্নয়নের জন্য ডিজাইন করা হয়েছে; সম্পূর্ণ Responses API বৈশিষ্ট্য সেটের জন্য Azure OpenAI / Microsoft Foundry ব্যবহার করুন।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->