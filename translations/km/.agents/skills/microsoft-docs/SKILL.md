---
name: microsoft-docs
description: ស្វែងរកឯកសារផ្លូវការរបស់ Microsoft ដើម្បីស្វែងរកគំនិត មេរៀនបណ្តាញ និងឧទាហរណ៍កូដនានាទាក់ទងនឹង
  Azure, .NET, Agent Framework, Aspire, VS Code, GitHub និងជាច្រើនទៀត។ ប្រើ Microsoft
  Learn MCP ជាមូលដ្ឋានលំនាំដើម ជាមួយ Context7 និង Aspire MCP សម្រាប់មាតិកាដែលនៅក្រៅ
  learn.microsoft.com។
---
# Microsoft Docs

ជំនាញស្រាវជ្រាវសម្រាប់បរិស្ថានបច្ចេកវិទ្យា Microsoft។ គ្របដណ្តប់លើ learn.microsoft.com និងឯកសារដែលរស់នៅខាងក្រៅវា (VS Code, GitHub, Aspire, Agent Framework repos)។

---

## ដើមហើយ: Microsoft Learn MCP

ប្រើឧបករណ៍ទាំងនេះសម្រាប់ **អ្វីៗទាំងអស់នៅលើ learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows និងផ្សេងទៀត។ នេះគឺជាឧបករណ៍សម្រាប់សំណួរឯកសារយ៉ាងច្រើនរបស់ Microsoft។

| ឧបករណ៍ | គោលបំណង |
|------|---------|
| `microsoft_docs_search` | ស្វែងរកនៅ learn.microsoft.com — គំនិត, មគ្គុរហារណ៍, មេរៀន, ការកំណត់រចនាសម្ព័ន្ធ |
| `microsoft_code_sample_search` | ស្វែងរកកូដដែលដំណើរការបានពីឯកសារ Learn។ ផ្ទេរចេញ `language` (`python`, `csharp`, ល. ) សម្រាប់លទ្ធផលល្អបំផុត |
| `microsoft_docs_fetch` | ទទួលបានមាតិកាភាពពេញលេញពី URL ពិសេស (នៅពេលសេចក្ដីបកស្រាយស្វែងរកមិនគ្រប់គ្រាន់) |

ប្រើ `microsoft_docs_fetch` បន្ទាប់ពីស្វែងរកនៅពេលអ្នកត្រូវការមេរៀនពេញលេញ សេចក្ដីជ្រើសរើសកំណត់រចនាសម្ព័ន្ធទាំងអស់ ឬពេលសេចក្ដីបកស្រាយស្វែងរកត្រូវបានកាត់ក្នុង។

---

## ករណីលើកលែង: ពេលណាដែលត្រូវប្រើឧបករណ៍ផ្សេងទៀត

ប្រភេទខាងក្រោមរស់នៅ **ខាងក្រៅ** learn.microsoft.com។ ប្រើឧបករណ៍ដែលបានបញ្ជាក់ជាផ្លាស់ប្តូរ។

### Aspire — ប្រើ Aspire MCP Server (ពេញចិត្ត) ឬ Context7

ឯកសារ Aspire រស់នៅលើ **aspire.dev**, មិនមែន Learn ទេ។ ឧបករណ៍ល្អបំផុតអាស្រ័យលើកំណែ Aspire CLI របស់អ្នក៖

**CLI 13.2+** (ផ្ដល់អនុសាសន៍) — ម៉ាស៊ីនបម្រើ Aspire MCP មានឧបករណ៍ស្វែងរកឯកសាររួមបញ្ចូល៖

| ឧបករណ៍ MCP | ពណ៌នា |
|----------|-------------|
| `list_docs` | បញ្ជីឯកសារទាំងអស់ដែលមានពី aspire.dev |
| `search_docs` | ស្វែងរកតាមពាក្យអត្ថន័យសំខាន់ៗមានទំងន់ជាមួយមាតិការបស់ aspire.dev |
| `get_doc` | ទាញយកឯកសារពិសេសមួយតាម slug |

វាទាំងនេះចាប់ផ្ដើមនៅក្នុង Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028))។ ដើម្បីធ្វើបច្ចុប្បន្នភាព: `aspire update --self --channel daily`។

**CLI 13.1** — ម៉ាស៊ីនបម្រើ MCP ផ្ដល់ការស្វែងរកការតភ្ជាប់ (`list_integrations`, `get_integration_docs`) ប៉ុន្តែមិនមានស្វែងរកឯកសារ។ ត្រលប់ទៅ Context7៖

| លេខសម្គាល់បណ្ណាល័យ | ប្រើសម្រាប់ |
|---|---|
| `/microsoft/aspire.dev` | ប្រភេទដើម — មគ្គុរ​ហារណ៍, ការតភ្ជាប់, ឯកសារមានCLI, ការបញ្ចូលទៅ |
| `/microsoft/aspire` | ប្រភពដំណើរការ — ខាងក្នុង API, ព័ត៌មានអំពីការអនុវត្ត |
| `/communitytoolkit/aspire` | ការតភ្ជាប់សហគមន៍ — Go, Java, Node.js, Ollama |

### VS Code — ប្រើ Context7

ឯកសារ VS Code រស់នៅលើ **code.visualstudio.com**, មិនមែន Learn ទេ។

| លេខសម្គាល់បណ្ណាល័យ | ប្រើសម្រាប់ |
|---|---|
| `/websites/code_visualstudio` | ឯកសារ​ប្រើប្រាស់ — ការកំណត់, មុខងារ, ការឈប់បញ្ឈប់, ការអភិវឌ្ឍពីចម្ងាយ |
| `/websites/code_visualstudio_api` | API បន្ថែម — webviews, TreeViews, ពាក្យបញ្ជា, ចំណុចរួមចំណែក |

### GitHub — ប្រើ Context7

ឯកសារ GitHub រស់នៅលើ **docs.github.com** និង **cli.github.com**។

| លេខសម្គាល់បណ្ណាល័យ | ប្រើសម្រាប់ |
|---|---|
| `/websites/github_en` | ការប្រតិបត្តិ, API, repos, សុវត្ថិភាព, អ្នកដឹកនាំ, Copilot |
| `/websites/cli_github` | ពាក្យបញ្ជា និងទង់ដែងទៅ GitHub CLI (`gh`) |

### Agent Framework — ប្រើ Learn MCP + Context7

មេរៀន Agent Framework ស្ថិតនៅលើ learn.microsoft.com (ប្រើ `microsoft_docs_search`), ប៉ុន្តែ **GitHub repo** មានព័ត៌មានលម្អិត API ដែលជានិច្ចមួយនៅមុខឯកសារចេញផ្សាយ — ជាពិសេស DevUI REST API សេចក្ដីយោង, ជម្រើស CLI និងការតភ្ជាប់ .NET។

| លេខសម្គាល់បណ្ណាល័យ | ប្រើសម្រាប់ |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | មេរៀន — មគ្គុររបស់ DevUI, ការតាមដាន, ការរៀបចំដំណើរការ workflow |
| `/microsoft/agent-framework` | ព័ត៌មានលម្អិត API — DevUI REST endpoints, ទង់ដែង CLI, អាជ្ញាសិទ្ធ, .NET `AddDevUI`/`MapDevUI` |

**របៀបប្រើ DevUI៖** សួរទៅកាន់ប្រភពគេហទំព័រ Learn សម្រាប់មគ្គុរបង្ហាញរបៀបធ្វើ បន្ទាប់មកប្រភព repo សម្រាប់ព័ត៌មានលម្អិត API (ស្កីម៉ាស្ត័រ endpoints, ការកំណត់ proxy, សញ្ញាអាជ្ញា)។

---

## ការតំឡើង Context7

សម្រាប់សំណួរណាមួយបណ្តាញ Context7 សូមកំណត់លេខសម្គាល់បណ្ណាល័យជាមុន (មួយដងក្នុងមួយវគ្គថ្នាក់រៀន)៖

1. ហៅ `mcp_context7_resolve-library-id` ជាមួយឈ្មោះបច្ចេកវិទ្យា
2. ហៅ `mcp_context7_query-docs` ជាមួយលេខសម្គាល់បណ្ណាល័យដែលបានត្រឡប់មក និងសំណួរប្រភេទពិសេស

---

## ការសរសេរការស្វែងរកឱ្យមានប្រសិទ្ធភាព

ត្រូវមានព័ត៌មានច្បាស់លាស់ — រួមបញ្ចូលកំណែ, គោលបំណង និងភាសា៖

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

រួមបញ្ចូលបរិបទ៖
- **កំណែ** នៅពេលដែលជាប់សមាជិក (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **គោលបំណងភារកិច្ច** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **ភាសា** សម្រាប់ឯកសារពហុភាសា (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->