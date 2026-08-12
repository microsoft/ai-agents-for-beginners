---
name: microsoft-docs
description: ស្វែងរកឯកសារផ្លូវការរបស់ Microsoft ដើម្បីរកមើល គំនិត មេរៀន និងឧទាហរណ៍កូដ
  នៅលើ Azure, .NET, Agent Framework, Aspire, VS Code, GitHub និងផ្សេងទៀត។ ប្រើ Microsoft
  Learn MCP ជាលំនាំដើម ហើយប្រើ Context7 និង Aspire MCP សម្រាប់មាតិកាដែលស្ថិតនៅខាងក្រៅ
  learn.microsoft.com។
---
# ឯកសារ Microsoft

ជំនាញសម្រាប់ស្រាវជ្រាវក្នុងប្រព័ន្ធបច្ចេកវិទ្យា Microsoft។ គ្របដណ្ដប់ learn.microsoft.com និងឯកសារដែលស្ថិតនៅក្រៅវា (VS Code, GitHub, Aspire, repos របស់ Agent Framework).

---

## លំនាំដើម: Microsoft Learn MCP

ប្រើឧបករណ៍ទាំងនេះសម្រាប់ **អ្វីៗគ្រប់យ៉ាងនៅលើ learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows និងផ្សេងទៀត។ នេះជាឧបករណ៍សំខាន់សម្រាប់សំណើរសុំឯកសាររបស់ Microsoft ភាគច្រើន។

| Tool | គោលបំណង |
|------|---------|
| `microsoft_docs_search` | ស្វែងរក learn.microsoft.com — គំនិត, មគ្គុទ្ទេសក៍, មេរៀន, ការកំណត់រចនាសម្ព័ន្ធ |
| `microsoft_code_sample_search` | រកឈ្លុះកូដដែលដំណើរការ​បានពីឯកសារ Learn. បញ្ជូន `language` (`python`, `csharp`, ល.) សម្រាប់លទ្ធផលល្អបំផុត |
| `microsoft_docs_fetch` | យកខ្លឹមសារទំព័រពេញពី URL ណាតែមួយ (ពេលដែលខ្លឹមសារកាត់ស្រង់ពីការស្វែងរកមិនគ្រប់គ្រាន់) |

ប្រើ `microsoft_docs_fetch` បន្ទាប់ពីស្វែងរកពេលអ្នកត្រូវការមេរៀនពេញលេញ, ជម្រើសការកំណត់រចនាសម្ព័ន្ធទាំងអស់, ឬពេលដែលខ្លឹមសារកាត់ស្រង់ពីការស្វែងរកត្រូវបានកាត់បន្ថយ។

---

## ករណីពិសេស: ពេលណាចាំបាច់ប្រើឧបករណ៍ផ្សេងៗ

ប្រភេទដូចតទៅស្ថិតនៅក្រៅ **learn.microsoft.com**។ សូមប្រើឧបករណ៍ដែលបានបញ្ជាក់ជំនួស។

### .NET Aspire — ប្រើ Aspire MCP Server (បានផ្តល់អាទិភាព) ឬ Context7

ឯកសារ Aspire ស្ថិតលើ **aspire.dev**, មិនមែន Learn ទេ។ ឧបករណ៍ល្អបំផុតអាស្រ័យលើកំណែ Aspire CLI របស់អ្នក៖

**CLI 13.2+** (ណែនាំ) — Aspire MCP server រួមបញ្ចូលឧបករណ៍ស្វែងរកឯកសារដែលមានស្រាប់៖

| ឧបករណ៍ MCP | ពណ៌នា |
|----------|-------------|
| `list_docs` | រាយបញ្ជីឯកសារទាំងអស់ដែលមានលើ aspire.dev |
| `search_docs` | ការស្វែងរកឯកសារតាមអក្សរដែលមានទំងន់នៅក្នុងមាតិកា aspire.dev |
| `get_doc` | យកឯកសារតាម slug ណាមួយ |

ទាំងនេះត្រូវបានបញ្ចូលក្នុង Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). ដើម្បីធ្វើអាប់ដេត៖ `aspire update --self --channel daily`. យោង៖ https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP server មានការស្វែងរក integrations (`list_integrations`, `get_integration_docs`) ប៉ុន្តែមិនមានស្វែងរកឯកសារ **ទេ**។ ត្រូវធ្វើ fallback ទៅ Context7:

| Library ID | ប្រើសម្រាប់ |
|---|---|
| `/microsoft/aspire.dev` | ចម្បង — ការណែនាំ, ការរួមបញ្ចូល, ឯកសារយោង CLI, ការដាក់ប្រើ |
| `/dotnet/aspire` | ប្រភព runtime — ខាងក្នុង API, ព័ត៌មានអំពីការអនុវត្ត |
| `/communitytoolkit/aspire` | ការរួមបញ្ចូលសហគមន៍ — Go, Java, Node.js, Ollama |

### VS Code — ប្រើ Context7

ឯកសារ VS Code ស្ថិតនៅលើ **code.visualstudio.com**, មិនមែន Learn ទេ។

| Library ID | ប្រើសម្រាប់ |
|---|---|
| `/websites/code_visualstudio` | ឯកសារអ្នកប្រើ — ការកំណត់, មុខងារ, ការបំបាត់បញ្ហា, ការអភិវឌ្ឍពីចម្ងាយ |
| `/websites/code_visualstudio_api` | API ផ្នែកបន្ថែម — webviews, TreeViews, ពាក្យបញ្ជា, ចំណុចរួមចំណែក |

### GitHub — ប្រើ Context7

ឯកសារ GitHub ស្ថិតលើ **docs.github.com** និង **cli.github.com**។

| Library ID | ប្រើសម្រាប់ |
|---|---|
| `/websites/github_en` | Actions, API, repos, សុវត្ថិភាព, ការគ្រប់គ្រង, Copilot |
| `/websites/cli_github` | បញ្ជា និង flags សម្រាប់ GitHub CLI (`gh`) |

### Agent Framework — ប្រើ Learn MCP + Context7

មេរៀន Agent Framework មាននៅលើ learn.microsoft.com (ប្រើ `microsoft_docs_search`), ប៉ុន្តែ **repo GitHub** មានព័ត៌មានអំពីកម្រិត API ដែលជាញឹកញាប់នៅមុខឯកសារដែលបានបោះពុម្ពផ្សាយ — ជាពិសេសយោង DevUI REST API, ជម្រើស CLI, និងការរួមបញ្ចូល .NET។

| Library ID | ប្រើសម្រាប់ |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | មេរៀន — មគ្គុទេសក៍ DevUI, ការតាមដាន, ការរៀបចំលំហាត់ការងារ |
| `/microsoft/agent-framework` | ព័ត៌មានលម្អិត API — DevUI REST endpoints, CLI flags, auth, .NET `AddDevUI`/`MapDevUI` |

**គន្លឹះ DevUI:** សូមស្វែងរកពីប្រភពវេបសាយ Learn សម្រាប់មគ្គុទេសក៍ពីរបៀបធ្វើ ហើយបន្ទាប់មកពិនិត្យប្រភព repo សម្រាប់ព័ត៌មានលម្អិតកម្រិត API (schema នៃ endpoint, ការកំណត់ proxy, auth tokens)។

---

## ការកំណត់ Context7

សម្រាប់សំណើ Context7 ទាំងអស់ សូមដោះស្រាយ ID បណ្ណាល័យ ជាមុន (ម្តងក្នុងមួយសម័យ)៖

1. ហៅ `mcp_context7_resolve-library-id` ជាមួយឈ្មោះបច្ចេកវិទ្យា
2. ហៅ `mcp_context7_query-docs` ជាមួយ ID បណ្ណាល័យដែលបានត្រឡប់មកវិញ និងសំណើច្បាស់លាស់

---

## ការសរសេរសំណើដែលមានប្រសិទ្ធភាព

ត្រូវច្បាស់លាស់ — រួមបញ្ចូលកំណែ, គោលបំណង, និងភាសា៖

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

Include context:
- **កំណែ** នៅពេលដែលពាក់ព័ន្ធ (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **គោលបំណងការងារ** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **ភាសា** សម្រាប់ឯកសារពហុភាសា (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែដោយ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ក្នុងខណៈដែលយើងខិតខំធ្វើឱ្យមានភាពត្រឹមត្រូវ សូមចំណាំថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬ ភាពមិនត្រឹមត្រូវ. ឯកសារដើមក្នុងភាសាមូលដ្ឋានគួរត្រូវបានចាត់ទុកថាជាប្រភពយោងផ្លូវការ. សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ យើងណែនាំឱ្យប្រើសេវាបកប្រែដោយអ្នកជំនាញមនុស្ស. យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬ ការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->