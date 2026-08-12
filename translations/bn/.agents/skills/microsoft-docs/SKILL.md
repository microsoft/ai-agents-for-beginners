---
name: microsoft-docs
---
# Microsoft Docs

Microsoft প্রযুক্তি ইকোসিস্টেমের জন্য গবেষণা দক্ষতা। Covers learn.microsoft.com and documentation that lives outside it (VS Code, GitHub, Aspire, Agent Framework repos).

---

## ডিফল্ট: Microsoft Learn MCP

Use these tools for **everything on learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, and more. এটি Microsoft ডকুমেন্টেশন সম্পর্কিত অধিকাংশ অনুসন্ধানের জন্য প্রধান টুল।

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com-এ অনুসন্ধান — ধারণা, গাইড, টিউটোরিয়াল, কনফিগারেশন |
| `microsoft_code_sample_search` | Learn ডকুমেন্টেশন থেকে কাজ করা কোড স্নিপেট খুঁজুন। সেরা ফলাফলের জন্য `language` (`python`, `csharp`, ইত্যাদি) পাস করুন |
| `microsoft_docs_fetch` | একটি নির্দিষ্ট URL থেকে পূর্ণ পেজ কনটেন্ট নিন (যখন সার্চ এক্সসার্প্ট যথেষ্ট নয়) |

Search করার পরে যখন আপনাকে সম্পূর্ণ টিউটোরিয়াল, সমস্ত কনফিগ অপশন, বা যখন সার্চ এক্সসার্প্ট কাটা হয় তখন `microsoft_docs_fetch` ব্যবহার করুন।

---

## ব্যতিক্রম: কখন অন্য টুল ব্যবহার করবেন

নিচের ক্যাটাগরিগুলো learn.microsoft.com-এর **বাইরে** অবস্থিত। পরিবর্তে নির্দিষ্ট টুলটি ব্যবহার করুন।

### .NET Aspire — Aspire MCP Server ব্যবহার করুন (প্রস্তাবিত) অথবা Context7

Aspire ডকুমেন্টেশন **aspire.dev**-এ থাকে, Learn-এ নয়। সর্বোত্তম টুল আপনার Aspire CLI ভার্সনের উপর নির্ভর করে:

**CLI 13.2+** (প্রস্তাবিত) — Aspire MCP সার্ভারে বিল্ট-ইন ডকস সার্চ টুল রয়েছে:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev থেকে সমস্ত উপলব्ध ডকুমেন্টেশন তালিকাভুক্ত করে |
| `search_docs` | aspire.dev কন্টেন্ট জুড়ে ওজনভিত্তিক লেক্সিকাল সার্চ |
| `get_doc` | slug দ্বারা একটি নির্দিষ্ট ডকুমেন্ট রিট্রিভ করে |

These ship in Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). আপডেট করতে: `aspire update --self --channel daily`. রেফ: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP সার্ভার ইন্টিগ্রেশন লুকআপ (`list_integrations`, `get_integration_docs`) প্রদান করে কিন্তু **not** ডক্স সার্চ করে না। Context7-এ ফিরুন:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | প্রাথমিক — গাইড, ইন্টিগ্রেশন, CLI রেফারেন্স, ডিপ্লয়মেন্ট |
| `/dotnet/aspire` | রানটাইম সোর্স — API অভ্যন্তরীণ বিষয়সমূহ, ইমপ্লিমেন্টেশন বিবরণ |
| `/communitytoolkit/aspire` | কমিউনিটি ইন্টিগ্রেশন — Go, Java, Node.js, Ollama |

### VS Code — Context7 ব্যবহার করুন

VS Code ডকুমেন্টেশন **code.visualstudio.com**-এ থাকে, Learn-এ নয়।

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | ইউজার ডকস — সেটিংস, ফিচার, ডিবাগিং, রিমোট ডেভ |
| `/websites/code_visualstudio_api` | এক্সটেনশন API — webviews, TreeViews, commands, contribution points |

### GitHub — Context7 ব্যবহার করুন

GitHub ডকুমেন্টেশন **docs.github.com** এবং **cli.github.com**-এ থাকে।

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repos, security, admin, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) কমান্ড ও ফ্ল্যাগ |

### Agent Framework — Learn MCP + Context7 ব্যবহার করুন

Agent Framework টিউটোরিয়ালগুলো learn.microsoft.com-এ আছে (use `microsoft_docs_search`), কিন্তু **GitHub repo**-তে API-লেভেল বিস্তারিত আছে যা প্রায়ই প্রকাশিত ডকসের থেকে এগিয়ে থাকে — বিশেষত DevUI REST API রেফারেন্স, CLI অপশন, এবং .NET ইন্টিগ্রেশন।

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | টিউটোরিয়াল — DevUI গাইড, ট্রেসিং, ওয়ার্কফ্লো অর্কেস্ট্রেশন |
| `/microsoft/agent-framework` | API বিবরণ — DevUI REST endpoints, CLI ফ্ল্যাগ, auth, .NET `AddDevUI`/`MapDevUI` |

DevUI টিপ: How-to গাইডগুলির জন্য Learn ওয়েবসাইট সোর্সকে কুয়েরি করুন, তারপর API-লেভেল স্পেসিফিকস (endpoint schemas, proxy config, auth tokens) জন্য রিপো সোর্স দেখুন।

---

## Context7 সেটআপ

প্রতিটি Context7 কুয়েরির জন্য, প্রথমে লাইব্রেরি ID রেজল্ভ করুন (সেশন প্রতি একবার):

1. প্রযুক্তি নামের সঙ্গে `mcp_context7_resolve-library-id` কল করুন
2. রিটার্ন করা লাইব্রেরি ID এবং একটি নির্দিষ্ট কুয়েরি নিয়ে `mcp_context7_query-docs` কল করুন

---

## কার্যকর কুয়েরি লেখা

নির্দিষ্টভাবে লিখুন — ভার্সন, উদ্দেশ্য, এবং ভাষা অন্তর্ভুক্ত করুন:

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

প্রাসঙ্গিক কনটেক্সট অন্তর্ভুক্ত করুন:
- **ভার্সন** যখন প্রাসঙ্গিক (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **কাজের উদ্দেশ্য** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **ভাষা** পলিগ্লট ডকসের জন্য (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
অস্বীকৃতি:
এই নথিটি AI অনুবাদ সেবা Co-op Translator (https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে লক্ষ করুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসম্পূর্ণতা থাকতে পারে। মুল নথিটি তার নিজ ভাষায়ই কর্তৃপক্ষপূর্ণ উৎস হিসেবে গণ্য করা উচিত। গুরুত্বপূর্ণ তথ্যের ক্ষেত্রে পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->