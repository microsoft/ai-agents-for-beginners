---
name: microsoft-docs
---
# Microsoft Docs

মাইক্রোসফট প্রযুক্তি ইকোসিস্টেমের জন্য গবেষণা দক্ষতা। learn.microsoft.com এবং এর বাইরের ডকুমেন্টেশন (VS Code, GitHub, Aspire, Agent Framework রেপোস) কভার করে।

---

## ডিফল্ট: Microsoft Learn MCP

**learn.microsoft.com** এ সবকিছুর জন্য এই সরঞ্জামগুলি ব্যবহার করুন — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, এবং আরও অনেক কিছু। এটি মাইক্রোসফট ডকুমেন্টেশন কুয়েরির প্রায় সব ক্ষেত্রে প্রধান সরঞ্জাম।

| সরঞ্জাম | উদ্দেশ্য |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com এ অনুসন্ধান — ধারণা, গাইড, টিউটোরিয়াল, কনফিগারেশন |
| `microsoft_code_sample_search` | Learn ডকুমেন্ট থেকে কার্যকর কোড স্নিপেট খুঁজুন। সেরা ফলাফলের জন্য `language` (`python`, `csharp`, ইত্যাদি) ব্যবহার করুন |
| `microsoft_docs_fetch` | নির্দিষ্ট URL থেকে সম্পূর্ণ পাতা বিষয়বস্তু পান (যখন অনুসন্ধান উদ্ধৃতি যথেষ্ট নয়) |

অনুসন্ধানের পরে `microsoft_docs_fetch` ব্যবহার করুন যখন আপনাকে সম্পূর্ণ টিউটোরিয়াল, সব কনফিগারেশন অপশন, অথবা যখন অনুসন্ধান উদ্ধৃতি কাটা পড়ে।

---

## ব্যতিক্রম: কখন অন্যান্য সরঞ্জাম ব্যবহার করবেন

নিম্নলিখিত বিভাগগুলি **learn.microsoft.com এর বাইরে** রয়েছে। নির্দিষ্ট সরঞ্জামগুলি ব্যবহার করুন।

### Aspire — Aspire MCP Server (প্রাধান্যপ্রাপ্ত) বা Context7 ব্যবহার করুন

Aspire ডকুমেন্টগুলি **aspire.dev** এ থাকে, Learn এ নয়। সেরা সরঞ্জাম আপনার Aspire CLI সংস্করণের উপর নির্ভর করে:

**CLI 13.2+** (সুপারিশকৃত) — Aspire MCP সার্ভার বিল্ট-ইন ডকুমেন্টেশন অনুসন্ধান সরঞ্জাম অন্তর্ভুক্ত করে:

| MCP সরঞ্জাম | বর্ণনা |
|----------|-------------|
| `list_docs` | aspire.dev থেকে সব উপলব্ধ ডকুমেন্টেশন তালিকা করে |
| `search_docs` | aspire.dev বিষয়বস্তুতে ওজনযুক্ত লেক্সিকাল অনুসন্ধান |
| `get_doc` | নির্দিষ্ট ডকুমেন্ট স্লাগ দ্বারা পুনরুদ্ধার করে |

এগুলি Aspire CLI 13.2 তে প্রবেশ করেছে ([PR #14028](https://github.com/microsoft/aspire/pull/14028))। আপডেট করতে: `aspire update --self --channel daily` ব্যবহার করুন।

**CLI 13.1** — MCP সার্ভার ইন্টিগ্রেশন লুকআপ (`list_integrations`, `get_integration_docs`) দেয় কিন্তু ডকুমেন্ট অনুসন্ধান **দিয়ে না**। Context7 ব্যবহার করুন:

| লাইব্রেরি আইডি | ব্যবহার ক্ষেত্র |
|---|---|
| `/microsoft/aspire.dev` | প্রাথমিক — গাইড, ইন্টিগ্রেশন, CLI রেফারেন্স, ডিপ্লয়মেন্ট |
| `/microsoft/aspire` | রানটাইম উৎস — API অন্তর্নিহিত, বাস্তবায়ন বিস্তারিত |
| `/communitytoolkit/aspire` | কমিউনিটি ইন্টিগ্রেশন — Go, Java, Node.js, Ollama |

### VS Code — Context7 ব্যবহার করুন

VS Code ডকুমেন্টগুলি **code.visualstudio.com** এ থাকে, Learn এ নয়।

| লাইব্রেরি আইডি | ব্যবহার ক্ষেত্র |
|---|---|
| `/websites/code_visualstudio` | ব্যবহারকারী ডকস — সেটিংস, বৈশিষ্ট্য, ডিবাগিং, রিমোট ডেভ |
| `/websites/code_visualstudio_api` | এক্সটেনশন API — ওয়েবভিউ, TreeViews, কমান্ড, অবদান পয়েন্ট |

### GitHub — Context7 ব্যবহার করুন

GitHub ডকস **docs.github.com** এবং **cli.github.com** এ থাকে।

| লাইব্রেরি আইডি | ব্যবহার ক্ষেত্র |
|---|---|
| `/websites/github_en` | অ্যাকশন, API, রিপোজ, সিকিউরিটি, অ্যাডমিন, কপাইলট |
| `/websites/cli_github` | GitHub CLI (`gh`) কমান্ড এবং ফ্ল্যাগ |

### Agent Framework — Learn MCP + Context7 ব্যবহার করুন

Agent Framework টিউটোরিয়ালগুলি learn.microsoft.com এ আছে (`microsoft_docs_search` ব্যবহার করুন), কিন্তু **GitHub রেপোতে** এমন API স্তরের বিস্তারিত আছে যা প্রায়শই প্রকাশিত ডকসের চেয়ে এগিয়ে — বিশেষ করে DevUI REST API রেফারেন্স, CLI অপশন, এবং .NET ইন্টিগ্রেশন।

| লাইব্রেরি আইডি | ব্যবহার ক্ষেত্র |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | টিউটোরিয়াল — DevUI গাইড, ট্র্যাকিং, ওয়ার্কফ্লো অর্কেস্ট্রেশন |
| `/microsoft/agent-framework` | API বিস্তারিত — DevUI REST এন্ডপয়েন্ট, CLI ফ্ল্যাগ, অথ, .NET `AddDevUI`/`MapDevUI` |

**DevUI টিপ:** Learn ওয়েবসাইট থেকে হাউ-টু গাইড এবং রেপো থেকে API স্তরের নির্দিষ্ট তথ্য (এন্ডপয়েন্ট স্কিমা, প্রক্সি কনফিগ, অথ টোকেন) অনুসন্ধান করুন।

---

## Context7 সেটআপ

যেকোন Context7 কুয়েরির জন্য, প্রথমে লাইব্রেরি আইডি নির্ধারণ করুন (সেশন প্রতি একবার):

1. প্রযুক্তি নাম নিয়ে `mcp_context7_resolve-library-id` কল করুন
2. ফিরে আসা লাইব্রেরি আইডি এবং নির্দিষ্ট কুয়েরি নিয়ে `mcp_context7_query-docs` কল করুন

---

## কার্যকর কুয়েরি লিখন

নির্দিষ্ট হোন — সংস্করণ, উদ্দেশ্য, এবং ভাষা অন্তর্ভুক্ত করুন:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

প্রসঙ্গ অন্তর্ভুক্ত করুন:
- প্রাসঙ্গিক হলে **সংস্করণ** (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **কাজের উদ্দেশ্য** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- পলিগ্লট ডকসের জন্য **ভাষা** (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->