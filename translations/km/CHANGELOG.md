# បច្ចុប្បន្នភាព

ការផ្លាស់ប្តូរប្រសើរទាំងអស់សម្រាប់វគ្គសិក្សា **ភ្នាក់ងារត្រួតពិនិត្យ AI សម្រាប់អ្នកចាប់ផ្តើម** ត្រូវបានរាយការណ៍នៅក្នុងឯកសារនេះ។

## [មិនទាន់ចេញផ្សាយ] — 2026-07-06

ការចេញផ្សាយនេះបានផ្លាស់ប្តូរវគ្គសិក្សាទៅកាន់ **Azure OpenAI Responses API** កំណត់ឈ្មោះផលិតផលយ៉ាងស្ដង់ដារលើ **Microsoft Foundry** និង **Microsoft Agent Framework (MAF)** បញ្ឈប់ការប្រើ GitHub Models, បច្ចុប្បន្នភាពកំណែ SDK នានា ហើយបន្ថែមមាតិការថ្មីអំពីម៉ូដែលក្នុងដើម និងការតភ្ជាប់បណ្ដាញផ្សេងនៅលើ Foundry។

### បានបន្ថែម

- **ជំនាញផ្លាស់ប្តូរ** — តំឡើងជំនាញភ្នាក់ងារដោយប្រើ [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (ពី [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) នៅក្នុង `.agents/skills/` រួមមានការដាក់បន្ទុក និងស្កេន។
- **Foundry Local (បើកម៉ូដែលលើឧបករណ៍)** — ផ្នែកថ្មី "Alternative Provider: Foundry Local" នៅក្នុង [00-course-setup/README.md](./00-course-setup/README.md) ពីការដំឡើង (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, និងភ្ជាប់ `FoundryLocalManager` ទៅ Microsoft Agent Framework តាមរយៈ `OpenAIChatClient`។
- **ផ្ទុកភ្នាក់ងារប្រើ LangChain / LangGraph លើ Microsoft Foundry** — ផ្នែកថ្មីនៅក្នុង [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ហើយមានឧទាហរណ៍រត់បាន [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ប្រើ `langchain-azure-ai[hosting]` និង `ResponsesHostServer` (ប្រព័ន្ធ `/responses`)，ផ្អែកលើ [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)។
- **គំរូ Microsoft Project Opal** — ផ្នែកថ្មី "ឧទាហរណ៍ពិត Microsoft Project Opal" នៅក្នុង [15-browser-use/README.md](./15-browser-use/README.md) ជាការតំណាង Opal ជាភ្នាក់ងារចំណាយកុំព្យូទ័រសម្រាប់សហគ្រាស និងតភ្ជាប់ការយល់ដឹងនេះទៅកាន់គំនិតវគ្គសិក្សា (មនុស្សក្នុងច្រក, ទំនុកចិត្ត / សុវត្ថិភាព, ការធ្វើផែនការ, ជំនាញ)។
- **គំរូភាសា Python នៅមេរៀនទីពីរ 02** — បន្ថែម [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (មើលចំណាត់ថ្នាក់ "បានផ្លាស់ប្តូរ" — ថ្មីពីសៀវភៅកំណត់ត្រា Semantic Kernel ដើម) ហើយភ្ជាប់វានៅក្នុង README វគ្គសិក្សា។
- ផ្នែក **ម៉ូដែល និងអ្នកផ្គត់ផ្គង់** ត្រូវបានបន្ថែមទៅ [STUDY_GUIDE.md](./STUDY_GUIDE.md)។

### បានផ្លាស់ប្តូរ

- **Chat Completions → Responses API (Python).** គំរូដែលហៅម៉ូដែលផ្ទាល់ ត្រូវបានផ្លាស់ប្តូរពី Chat Completions ទៅ Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`)，ប្រើ `OpenAI` client ទល់នឹងចុងបញ្ចប់ Azure OpenAI `/openai/v1/` ដែលមានស្ថិរភាព (គ្មាន `api_version`)។ គំរូដែលពាក់ព័ន្ធរួមមាន៖
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — ចំណុះការហៅមុខងារពេញលេញ (គំរូស្កេមាឧបករណ៍បានផ្លាស់ប្តូរទៅទ្រង់ទ្រាយ Responses, លទ្ធផលឧបករណ៍ត្រូវបានទម្លាក់ជា `function_call_output`, `max_output_tokens`, ឬផ្សេងៗ)។
- **GitHub Models → Azure OpenAI.** GitHub Models ត្រូវបានបញ្ឈប់ប្រើប្រាស់ (ចេញពីប្រើប្រាស់ចាប់ពី **ខែកក្កដាឆ្នាំ 2026**) ហើយមិនគាំទ្រ Responses API។ កូដគ្រប់ផ្លូវរបស់ GitHub Models ត្រូវបានបំលែងទៅ Azure OpenAI / Microsoft Foundry ចេញពីគំរូ Python និង .NET៖
  - Python៖ សៀវភៅកំណត់ត្រាចរន្តការងារវគ្គ 08 (`01`–`03`), វគ្គ 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)។
  - .NET៖ `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` និងឯកសារ `.md` ដែលនៅជាមួយ, និងសៀវភៅកំណត់ត្រាចរន្តការងារថ្មីវគ្គ 08 dotNET/`.md` (`01`–`03`) ប្រើ `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` ជាមួយ `AzureCliCredential`។
- **Semantic Kernel → Microsoft Agent Framework.** សៀវភៅកំណត់ត្រាចាស់ `02-semantic-kernel.ipynb` ត្រូវបានសរសេរឡើងវិញ ដើម្បីប្រើ Microsoft Agent Framework ជាមួយ Azure OpenAI (Responses API) ហើយបានប្តូរឈ្មោះទៅ `02-python-agent-framework-azure-openai.ipynb`។
- **ស្ដង់ដារលើ `FoundryChatClient` + `as_agent`.** README និងកូដសៀវភៅកំណត់ត្រាដែលយោងទៅកាន់ `AzureAIProjectAgentProvider` ត្រូវបានស្ដង់ដារលើវិធីសាស្រ្តត្រួតពិនិត្យដែលប្រើក្នុងវគ្គ 01 និងគំរូ Framework ផ្ទាល់៖ `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` ជាមួយ `provider.as_agent(...)`។ ការផ្លាស់ប្តូរបានប្រើនៅក្នុង README និងសៀវភៅកំណត់ត្រាវគ្គ 02–14 (ឧ. ការចងចាំវគ្គ 13, សៀវភៅកំណត់ត្រាវគ្គ 14 ទាំងអស់, `11-agentic-protocols/code_samples/github-mcp/app.py`)។
- **ការកំណត់ឈ្មោះផលិតផល។** បានប្តូរពាក្យនៅក្នុងមាតិការជាភាសាអង់គ្លេស៖
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (មិនបានផ្លាស់ប្តូរ៖ "Azure OpenAI", "Azure AI Search", "Azure AI Inference", និងឈ្មោះអថេរសេវាផ្សេងៗ)។
- **ការទាមទារ Dependencies** ([requirements.txt](../../requirements.txt))៖
  - កំណត់ជាក់លាក់ `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`។
  - កំណត់ជាក់លាក់ `openai>=1.108.1` (អប្បបរមាសម្រាប់ Responses API)។
  - ដកដង្ហើម `azure-ai-inference` (ដែលមាននៅក្នុងគំរូ GitHub Models ដែលបានផ្លាស់ប្តូរ)។
- **ការកំណត់បរិស្ថាន** ([.env.example](../../.env.example))៖ ដកបញ្ជីអថេរ GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) បន្ថែម `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` និងជម្រើស `AZURE_OPENAI_API_KEY`; ផ្លាស់ប្ដូរឈ្មោះ ទៅ Microsoft Foundry។
- **ឯកសារនានា** — បានបច្ចុប្បន្នភាព [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), និង [STUDY_GUIDE.md](./STUDY_GUIDE.md) សម្រាប់ការកំណត់បរិស្ថាន, ការត្រួតពិនិត្យ, ការណែនាំអ្នកផ្គត់ផ្គង់, និងឈ្មោះ។

### បានដកចេញ

- ជំហានចូលធ្វើការ GitHub Models និងអថេរបរិស្ថានពីឯកសារដំឡើង (បានជំនួសដោយ Azure OpenAI / Microsoft Foundry)។

### សុវត្ថិភាព / រក្សាឯកជនភាព (សំអាតការចែករំលែកសាធារណៈ)

- បានសម្អាតលទ្ធផលអនុវត្តការងារសៀវភៅកំណត់ត្រា Jupyter ដែលរំលាយ **លេខសម្គាល់ជាវិស្សមកាល Azure** ព័ត៌មានក្រុមធនធាន / ឈ្មោះធនធាន និងលេខសម្គាល់ការតភ្ជាប់ Bing ព្រមទាំងផ្លូវឯកសារផ្ទាល់ខ្លួន និងឈ្មោះអ្នកប្រើ:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- បានបញ្ជាក់ថាគ្មានកូនសោ API, ស្លាកសម្គាល់, លេខសម្គាល់ជាវិស្សមកាល ឬផ្លូវផ្ទាល់ខ្លួននៅក្នុងមាតិកាភាសាអង់គ្លេសដែលបានតាមដានទេ (ការយោង `GITHUB_TOKEN` នៅតែមាន គឺសម្រាប់ស្លាក GitHub Actions ក្នុង​ជំនួស និង GitHub MCP server PAT ក្នុងការដំឡើងវគ្គ 11  — ទាំងពីរជាការពិត និងមិនមានទាក់ទងនឹង GitHub Models)។

### សម្គាល់ និងកំណត់កម្រិតដែលទទួលស្គាល់

- **មិនបានអនុវត្ត/កំណត់ប្រែបម្លែង។** គំរូទាំងនេះគឺសម្រាប់ការអប់រំដែលបានបច្ចុប្បន្នភាពឱ្យត្រឹមត្រូវតាម API និងឈ្មោះ; មិនបានរត់លើធនធាន Azure ពិតប្រាកដ និងគំរូ .NET មិនបានកំណត់ប្រែបម្លែងនៅក្នុងបរិបទនេះទេ។ សូមផ្ទៀងផ្ទាត់ជាមួយកំណត់ត្រា Microsoft Foundry / Azure OpenAI របស់អ្នក។
- **ការចេញផ្សាយម៉ូដែលត្រូវជួយគាំទ្រ Responses API។** ប្រើការចេញផ្សាយដូចជា `gpt-4o-mini`, `gpt-4.1`, ឬម៉ូដែល `gpt-5.x`។ ម៉ូដែលចាស់គាំទ្រជម្រើស Responses សំខាន់ៗ ប៉ុន្តែមិនគាំទ្រពេញលេញគ្រប់មុខងារ។
- **កំណែ agent-framework។** គំរូទាំងនេះគោលដៅទៅកាន់ MAF ថ្មីបំផុត (`>=1.10.0`)។ សម្ភារបង្កើតភ្នាក់ងារតាមបែប canonical គឺ `client.as_agent(...)`។ API ត្រូវបានពិនិត្យផ្ទៀងផ្ទាត់ជាមួយឯកសារផ្សព្វផ្សាយនៃ Framework និងជាការតំឡើងដោយផ្ទាល់។ ប្រសិនបើប្រើកំណែផ្សេង សូមបញ្ជាក់មុខងារដែលអាចប្រើបាន (`as_agent` ឬ `create_agent`)។
- **សៀវភៅកំណត់ត្រាចរន្តការងារវគ្គ 08 សម្រាប់ 04** បានរក្សា `AzureAIAgentClient` (ពី `agent-framework-azure-ai`) ព្រោះវាប្រើឧបករណ៍ដែលផ្ទុកនៅលើ Microsoft Foundry Agent Service (ទិន្នន័យ Bing, អ្នកបកប្រែកូដ)។ វាមានមូលដ្ឋានលើ Responses។
- **ការចេញផ្សាយលំនាំដើម .NET។** គំរូចរន្តការងារវគ្គ 08 dotNET ពីមុនបានកំណត់ដោយដៃ `gpt-4o` ប៉ុន្តែឥឡូវនេះប្រើ `AZURE_OPENAI_DEPLOYMENT` («gpt-4o-mini») ជាលំនាំដើម។ ប្រសិនបើគំរូដែលទាមទារបញ្ចូល multimodal / ភាពវិចិត្រសូរប្រើតំឡើង `AZURE_OPENAI_DEPLOYMENT` ជាមួយម៉ូដែលសមរម្យ។
- **Foundry Local** ផ្តល់ចំនុចចូល OpenAI-compatible **Chat Completions** ហើយមានគោលបំណងសម្រាប់ការអភិវឌ្ឍនៅក្នុងឧបករណ៍មូលដ្ឋាន; សូមប្រើ Azure OpenAI / Microsoft Foundry សម្រាប់មុខងារ Responses API ពេញលេញ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->