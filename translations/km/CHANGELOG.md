# បញ្ជីការផ្លាស់ប្តូរ

ការផ្លាស់ប្តូរដែលគួរឱ្យចាប់អារម្មណ៍ទាំងអស់បង្ហាញក្នុងឯកសារនេះសម្រាប់វគ្គសិក្សា **AI Agents for Beginners**។

## [ចេញផ្សាយ] — ២០២៦-០៧-១៤

ការចេញផ្សាយនេះផ្លាស់ប្តូរវគ្គសិក្សាចេញពីម៉ូដែលរាជ្យទាំងពីរថ្មីពីការដកចេញ អំឡុងពេលបម្លែងកំណត់ត្រាណូតប៊ុកនៅ វគ្គសិក្សា ទៅ API Microsoft Agent Framework ដែលមានស្ថេរភាព ហើយផ្ទៀងផ្ទាត់កំណត់ត្រាណូតប៊ុក Python ទល់នឹងការដាក់ពិនិត្យសកម្ម Microsoft Foundry។

### បានផ្លាស់ប្តូរ

- **ផ្លាស់ទីចេញពីម៉ូដែលដែលត្រូវដកចេញ (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`) ។** ទាំងពីរ `gpt-4.1` និង `gpt-4.1-mini` ឥឡូវត្រូវបានដកចេញ (កាលបរិច្ឆេទផុតវ័យបោះពុម្ភផ្សាយ **១៤ តុលា ២០២៦**)។ បានប្តូរចំណាំទាំងអស់ក្នុងវគ្គសិក្សា (ឯកសារ, `.env.example`, កំណត់ត្រាណូត Python/.NET និងឧទាហរណ៍) ជាមួយ `gpt-5-mini` ដែលមិនត្រូវដកចេញ។ ឧទាហរណ៍ផ្លាស់ទីម៉ូដែលក្នុងវគ្គសិក្សា ១៦ រក្សាភាពខុសគ្នារវាងតូច/ធំដោយប្រើ `gpt-5-nano` (តូច) និង `gpt-5-mini` (ធំ)។ ឯកសារភាគីទីបីដែលមានភាពប្រើប្រាស់ ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)) អត្ថបទ GitHub Models ប្រវត្តិសាស្ត្រ និងកំណត់សំគាល់សមត្ថភាព skill `azure-openai-to-responses` ត្រូវបានទុកដដែលដោយសារ។
- **កំណត់ត្រាណូត handoff វគ្គសិក្សា ១៤ បានបម្លែងទៅ API មានស្ថេរភាព។** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) ឥឡូវប្រើ `agent_framework.orchestrations.HandoffBuilder` ជាមួយ `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, ការផ្ទៀងផ្ទាត់ប្រភេទ event បែបឆ(Stream) និង `FoundryChatClient` (ជំនួសសញ្ញា `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` មុន 1.0 ដែលត្រូវបានដកចេញ)។
- **កំណត់ត្រាណូត human-in-the-loop វគ្គសិក្សា ១៤ បានបម្លែងទៅ API មានស្ថេរភាព។** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) ឥឡូវបញ្ឈប់តាម `ctx.request_info(...)` + `@response_handler` (ជំនួស `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` ដែលត្រូវបានដកចេញ), បង្កើតជាមួយ `WorkflowBuilder(start_executor=..., output_executors=[...])`, បញ្ជាលទ្ធផលរចនាសម្ព័នតាម `default_options={"response_format": ...}`, ហើយប្រើចម្លើយ script ដើម្បីឲ្យកំណត់ត្រាណូតធ្វើការ ដោយគ្មានការរាំងខ្ទប់ `input()`។
- **ការកំណត់បរិស្ថាន** ([.env.example](../../.env.example)): ប្តូរឈ្មោះការចេញផ្សាយម៉ូដែលទៅ `gpt-5-mini`; បន្ថែម `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (វគ្គសិក្សា ១៦ ថ្នាំងម៉ូដែល) និង `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` ដែលមិនមានពីមុន (វគ្គ ១៥ ការប្រើប្រាស់កម្មវិធីរុករក)។
- **ការពឹងផ្អែក** ([requirements.txt](../../requirements.txt)): បិទកំណាត់ `agent-framework`, `agent-framework-foundry`, និង `agent-framework-openai` ទៅស្មើ `~=1.10.0` សម្រាប់កំណត់ត្រាដែលមានការត្រួតពិនិត្យខ្ពស់។ (កំណែ 1.11.0 មានការផ្លាស់ប្តូរបង្ករាស់មុខងារដែលវគ្គសិក្សានេះប្រើ)។

### កំណត់សម្គាល់ និងកំណត់ចំណាំ

- **បានផ្ទៀងផ្ទាត់ជាមួយ Microsoft Foundry ដែលប្រតិបត្តិការ។** កំណត់ត្រា Python ត្រូវបានរត់ណែនាំជាភាសាឥតក្បាលជាមួយ `nbconvert` ទល់នឹងគំរូ Microsoft Foundry ដែលប្រើ `gpt-5-mini` (និង `gpt-5-nano` សម្រាប់វគ្គ ១៦ ថ្នាំងម៉ូដែល)។ សូមដាក់ជំនួសម៉ូដែលដែលមិនត្រូវដកចេញក្នុងគម្រោងផ្ទាល់ខ្លួនរបស់អ្នក; កំណត់ត្រាណូតអានឈ្មោះការចេញផ្សាយពី `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`។
- **នៅតែត្រូវការបន្ថែមធនធានសម្រាប់វគ្គសិក្សាមួយចំនួន។** វគ្គ ០៥ ត្រូវការស្វែងរក Azure AI; ការងារជំហាន Bing នៅវគ្គ ០៨ (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) ត្រូវការតភ្ជាប់ Bing និងឧបករណ៍ Microsoft Foundry Agent Service ដែលរៀបចំ; វគ្គ ១៣ (Cognee) និង វគ្គ ១៧ (Foundry Local) ត្រូវការបរិស្ថានរត់ផ្ទាល់ខ្លួន។

## [ចេញផ្សាយ] — ២០២៦-០៧-១៣

ការចេញផ្សាយនេះបន្ថែមវគ្គសិក្សាថ្មីពីរដែលបញ្ចប់ជំពូកនៃការដាក់ពង្រីក — ការពង្រីកស្វ័យប្រវត្តិទៅ Microsoft Foundry និងការចុះទៅតាមការប្រើប្រាស់ក្នុងកុំព្យូទ័រតែមួយ — នឹងបន្ទាត់សាកល្បង បញ្ជីផ្លូវចរចារវគ្គសិក្សាថ្មី ជំនាញអ្នករៀនថ្មី និងយីហោទំនើប។

### បានបន្ថែម

- **វគ្គ ១៦ — ការដាក់បញ្ជូនភ្នាក់ងារដែលអាចពង្រីកបានជាមួយ Microsoft Foundry។** វគ្គថ្មី [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) និងកំណត់ត្រាណូតអាចដំណើរការ [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) ស្ថាបនាភ្នាក់ងារគាំទ្រពិភាក្សាជាក់ស្តែង (ឧបករណ៍, RAG, អង្គចងចាំ, ការត្រួតពិនិត្យម៉ូដែល, ការកែប្រែឆ្លើយតប, ការអនុម័តដោយមនុស្ស, ជើងទីពិនិត្យ, ការតាមដាន OpenTelemetry), ជាមួយគំនូរសកម្មភាពអភិវឌ្ឍន៍/ដាក់បញ្ចូល/រត់, ការត្រួតពិនិត្យចំណេះដឹង ការផ្តល់បAssignment និងការប្រឈម។
- **វគ្គ ១៧ — ការបង្កើតភ្នាក់ងារ AI ផ្នែកមូលដ្ឋានជាមួយ Foundry Local និង Qwen។** វគ្គថ្មី [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) និងកំណត់ត្រាណូត [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) ស្ថាបនាជំនួយការជួសជុលគ្រប់ពេលព្រមទាំងនៅលើឧបករណ៍ដោយផ្ទាល់ (ហៅមុខងារ Qwen តាម Foundry Local, ឧបករណ៍ឯកសារក្នុង sandbox, RAG ផ្នែកមូលដ្ឋានជាមួយ Chroma, ម៉ូឌុល MCP ក្នុងសំណុំមូលដ្ឋានតាមចូលខ្លួន) ជាមួយគំនូរមូលដ្ឋានតែប៉ុណ្ណោះ / mRAG / ការហៅឧបករណ៍, ការត្រួតពិនិត្យចំណេះដឹង, ការផ្តល់បAssignment និងការប្រឈម។
- **បន្ទាត់សាកល្បង Smoke-Test ។** ប្រតិបត្តិការថ្មី [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) ជាមួយបន្ទាត់ព្រួតឯកសារ [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) និងបញ្ជីផ្នែករបស់វគ្គផ្សេងៗក្រោម [tests/](./tests/README.md) សម្រាប់ភ្នាក់ងារដែលអាចដាក់បញ្ចូលបាននៅវគ្គ ០១, ០៤, ០៥, និង ១៦, ជាមួយ README បង្ហាញការតភ្ជាប់បញ្ជីជាមួយវគ្គសិក្សារបស់វា និងឈ្មោះភ្នាក់ងារគ្រប់គ្រង។ វគ្គ ១៦ មានផ្នែក "ការផ្ទៀងផ្ទាត់ភ្នាក់ងារដោយសាកល្បង Smoke Tests"; វគ្គ ០១/០៤/០៥ មានជម្រើសបញ្ជាក់សាកល្បង smoke-test។
- **ជំនាញអ្នករៀន។** ជំនាញភ្នាក់ងារថ្មីនៅក្រោម `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (រួមបញ្ចូលដំណឹងណែនាំវគ្គ ១៦ និង ១៧), និង [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (របៀបផ្ទៀងផ្ទាត់ឧទាហរណ៍កំណត់ត្រាណូតជាមួយ Microsoft Foundry / Azure OpenAI ដំណើរការ)។
- **កម្មវិធីរត់ផ្ទៀងផ្ទាត់កំណត់ត្រាណូត។** ថ្មី [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) រត់កំណត់ត្រាណូត Python គ្រប់មួយដោយគ្មានក្បាលជាមួយ `nbconvert` ហើយបង្ហាញ matrix PASS/FAIL (បូក `results.json`)។ វាដឹងដើម repo និង Python ដោយស្វ័យប្រវត្តិ, មិនរួមបញ្ចូលកំណត់ត្រាណូតដែលអត់ទាក់ទងវគ្គសិក្សា (`.venv`, `site-packages`, `translations`, ឯកសារគំរូ skill) និងកំណត់ត្រាណូត .NET ជាមូលដ្ឋាន, ហើយគាំទ្រ `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, និង `-Python`។
- **ការត្រួតពិនិត្យផ្លូវចរចារ វគ្គសិក្សា។** បន្ថែមតំណភ្ជាប់វគ្គមុន/បន្ទាប់ទៅវគ្គ ១១–១៥ (មុនមិនមាន) ដូច្នេះវគ្គទាំងមូលចងខ្សែ ០០ → ១៨ ទាំងពីរទិស។
- **រូបថ្មថ្មី។** រូបថ្មវគ្គសិក្សាសម្រាប់វគ្គ ១៦ និង ១៧ ជាមួយរូបភាពសង្គមផ្ទុកមូលដ្ឋាន [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) ដែលឥឡូវផ្សព្វផ្សាយពីវគ្គសិក្សាថ្មីពីរ និង URL `aka.ms/ai-agents-beginners`។
- **ការពឹងផ្អែក** ([requirements.txt](../../requirements.txt)): បន្ថែម `foundry-local-sdk` និង `chromadb` សម្រាប់វគ្គ ១៧។

### បានផ្លាស់ប្តូរ

- **តារាងវគ្គសិក្សាក្នុង [README.md](./README.md)**៖ វគ្គ ១៦ និង ១៧ ឥឡូវតំណភ្ជាប់ទៅមាតិកា (មុនបានចុះថា "មកឆាប់ៗនេះ"); រូបភាព repo ប្ដូរទៅជាទ្រង់ទ្រាយ `repo-thumbnailv3.png`។
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**៖ បន្ថែមវគ្គ ១៦ និង ១៧ ទៅផែនទីមេរៀន និងផ្លូវរៀន និងផ្នែក "Validating Deployed Agents with Smoke Tests"។
- **[AGENTS.md](./AGENTS.md)**៖ កែប្រែចំនួន/ពិពណ៌នា វគ្គសិក្សា (០០–១៨), បន្ថែមផ្នែកបញ្ជាក់ការត្រួតពិនិត្យ smoke-testing និងបន្ថែមឧទាហរណ៍ឈ្មោះវគ្គ ១៦/១៧។
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**៖ "Previous Lesson" ឥឡូវសល្មមទៅវគ្គ ១៧ (មុន ១៥) បិទខ្សែ។
- **ការតម្រុយឈ្មោះម៉ូដែលបានតម្រឹមលើម៉ូដែលមិនត្រូវដកចេញ។** ប្ដូរពូជពាក្យទាំងអស់ `gpt-4o` / `gpt-4o-mini` ក្នុងវគ្គសិក្សា (ឯកសារ, `.env.example`, កំណត់ត្រាណូត Python/.NET និងឧទាហរណ៍) ជាមួយ `gpt-4.1-mini` — `gpt-4o` (គ្រប់កំណែ) នឹងដកចេញក្នុងឆ្នាំ ២០២៦។ ឧទាហរណ៍ភ្ជាប់ម៉ូដែលវគ្គសិក្សា ១៦ រក្សាភាពខុសគ្នារវាងតូច/ធំ ដោយប្រើ `gpt-4.1-mini` (តូច) និង `gpt-4.1` (ធំ)។ កំណត់ត្រាណូត Python ឥឡូវជ្រើសម៉ូដែលពីអថេរបរិស្ថាន (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) ជំនួសការកំណត់ឈ្មោះម៉ូដែលជាក់លាក់។

### កំណត់សម្គាល់ និងកំណត់ចំណាំ

- **មិនបានរត់លើ Azure ផ្ទាល់។** កំណត់ត្រាណូតវគ្គសិក្សាថ្មីគឺជាឧទាហរណ៍សិក្សា; សូមរត់ និងផ្ទៀងផ្ទាត់វាជាមួយ Microsoft Foundry / Foundry Local របស់អ្នកផ្ទាល់។ បន្ទាត់សាកល្បង smoke-test ត្រូវការឲ្យអ្នកដាក់ភ្នាក់ងារវគ្គសិក្សា និងកំណត់រចនាសម្ងាត់ Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) ជាមួយតួនាទី **Azure AI User** នៅលើគម្រោង Foundry។
- **វគ្គ ១៧ គឺមានតែផ្នែកមូលដ្ឋានក្នុងតែប៉ុណ្ណោះ។** វាងតម្រូវមិនមានច្រក Foundry Responses ដូច្នេះសកម្មភាពសាកល្បង smoke-test មិនអនុវត្ត; សូមផ្ទៀងផ្ទាត់ដោយរត់កំណត់ត្រាណូតលើកុំព្យូទ័ររបស់អ្នក។

## [ចេញផ្សាយ] — ២០២៦-០៧-០៦

ការចេញផ្សាយនេះផ្លាស់ប្តូរវគ្គសិក្សាទៅ **Azure OpenAI Responses API**, តម្រឹមឈ្មោះផលិតផលមួយទៀតទៅលើ **Microsoft Foundry** និង **Microsoft Agent Framework (MAF)**, ដកចេញ GitHub Models, បច្ចុប្បន្នភាពកំណែ SDK, ហើយបន្ថែមមាតិកាថ្មីអំពីម៉ូដែលក្នុងស្ទង់ និងការចាក់បង្ហាញគ្រឿងម៉ាស៊ីនផ្សេងៗលើ Foundry។

### បានបន្ថែម

- **ជំនាញផ្លាស់ទី** — តំឡើងជំនាញ Agent [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (ពី [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) នៅក្រោម `.agents/skills/`, រួមមានការគេចង្ហាញ និងស្គេន Script។
- **Foundry Local (រត់ម៉ូដែលលើឧបករណ៍ផ្ទាល់ខ្លួន)** — ផ្នែកថ្មី "Alternative Provider: Foundry Local" ក្នុង [00-course-setup/README.md](./00-course-setup/README.md) ពិពណ៌នាអំពីការតំឡើង (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, និងការតភ្ជាប់ `FoundryLocalManager` ទៅ Microsoft Agent Framework តាមរយៈ `OpenAIChatClient`។
- **កាន់កាប់ភ្នាក់ងារ LangChain / LangGraph លើ Microsoft Foundry** — ផ្នែកថ្មីក្នុង [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) និងឧទាហរណ៍ដែលអាចដំណើរការ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ប្រើ `langchain-azure-ai[hosting]` និង `ResponsesHostServer` (ប្រព័ន្ធ `/responses`), dựa trên [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)។
- **Microsoft Project Opal** — ផ្នែកថ្មី "ឧទាហរណ៍ពិភពអាជីវកម្មពិត: Microsoft Project Opal" ក្នុង [15-browser-use/README.md](./15-browser-use/README.md) ដែលបង្ហាញ Opal ជាភ្នាក់ងារប្រើប្រាស់កុំព្យូទ័រប្រកបដោយអាជីវកម្ម និងភ្ជាប់វាដល់យុទ្ធសាស្រ្តវគ្គសិក្សា (មនុស្សក្នុងខ្សែ, វិស័ទនភាព/សុវត្ថិភាព, ការធ្វើផែនការ, ជំនាញ)។
- **ឧទាហរណ៍ Python ទីពីរវគ្គ ០២** — បន្ថែម [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (មើល "បានផ្លាស់ប្តូរ" — ផ្លាស់ពីកំណត់ត្រាណូត Semantic Kernel មុន) និងភ្ជាប់វាទៅ README វគ្គសិក្សា។
- ផ្នែក ម៉ូដែល និង ផ្ដល់សេវា ត្រូវបន្ថែមទៅ [STUDY_GUIDE.md](./STUDY_GUIDE.md)។

### បានផ្លាស់ប្តូរ

- **Chat Completions → Responses API (Python).** ឧទាហរណ៍ដែលហៅម៉ូដែលដោយផ្ទាល់ត្រូវបានផ្លាស់ប្តូរពី Chat Completions ទៅ Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), ប្រើ `OpenAI` client ទល់នឹង Azure OpenAI `/openai/v1/` endpoint ដែលមានស្ថេរភាព (គ្មាន `api_version`)។ ឧទាហរណ៍ដែលពាក់ព័ន្ធរួមមាន:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — ដំណើរឆ្លងកាត់ការហៅមុខងារពេញលេញ (រាងពត៌មានបម្រែបម្រួលឧបករណ៍ទៅទ្រង់ទ្រាយ Responses, លទ្ធផលឧបករណ៍ត្រឡប់ជា `function_call_output`, `max_output_tokens`, ជាដើម)។

- **ម៉ូដែល GitHub → Azure OpenAI.** ម៉ូដែល GitHub ត្រូវបានដកចេញ (នឹងផ្អាកប្រើប្រាស់ចាប់តាំងពី **ខែកក្កដា ២០២៦**) ហើយមិនគាំទ្រកម្មវិធីប្រើប្រាស់ Responses API ទេ។ គ្រោងផ្លូវកូដម៉ូដែល GitHub ត្រូវបានបំលែងទៅ Azure OpenAI / Microsoft Foundry ទាំង Python និង .NET ឧទាហរណ៍ទាំងអស់៖
  - Python៖ សៀវភៅកំណត់ត្រាដំណើរការបង្រៀនមេរៀនទី 08 (`01`–`03`), មេរៀនទី 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)។
  - .NET៖ `01`–`04`, `07`, `08` កូដ `*-dotnet-agent-framework.cs` និងឯកសារ `.md` មិត្តភក្តិ, និងសៀវភៅកំណត់ត្រាដំណើរការដំណាក់កាល dotNET នៃមេរៀនទី 08/`.md` (`01`–`03`) ឥឡូវប្រើ `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` ជាមួយ `AzureCliCredential`។
- **Semantic Kernel → Microsoft Agent Framework.** សៀវភៅកំណត់ត្រាចាស់ `02-semantic-kernel.ipynb` ត្រូវបានសរសេរឡើងវិញដើម្បីប្រើ Microsoft Agent Framework ជាមួយ Azure OpenAI (Responses API) ហើយបានប្ដូរឈ្មោះទៅជា `02-python-agent-framework-azure-openai.ipynb`។
- **ធម្មតាកាត់ទុកជា `FoundryChatClient` + `as_agent`.** README និងកូដសៀវភៅកំណត់ត្រាដែលយោង `AzureAIProjectAgentProvider` ត្រូវបានធម្មតាកាត់ជាទម្រង់រឹងរូសដែលប្រើដោយមេរៀនទី 01 និងឧទាហរណ៍របស់ framework: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` ជាមួយ `provider.as_agent(...)`។ បានកែប្រែទាំង README និងសៀវភៅកំណត់ត្រា មេរៀនទី 02 ដល់ 14 (ឧទាហរណ៍ មេរៀនទី 13 memory, សៀវភៅកំណត់ត្រា មេរៀន 14 ទាំងអស់, `11-agentic-protocols/code_samples/github-mcp/app.py`)។
- **ការដាក់ឈ្មោះផលិតផល។** បានប្ដូរឈ្មោះក្នុងមាតិកាអង់គ្លេសទាំងមូល៖
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (មិនផ្លាស់ប្តូរ៖ "Azure OpenAI", "Azure AI Search", "Azure AI Inference", និងឈ្មោះអថេរបរិស្ថាន)។
- **ការគាំទ្រ** ([requirements.txt](../../requirements.txt)):
  - បិទភ្ជាប់ `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`។
  - បិទភ្ជាប់ `openai>=1.108.1` (អប្បបរមាសម្រាប់ Responses API)។
  - លុបចេញ `azure-ai-inference` (បានប្រើតែចំពោះឧទាហរណ៍ GitHub Models ដែលបានបម្លែង)។
- **ការកំណត់បរិស្ថាន** ([.env.example](../../.env.example))៖ បានចេញអថេរបរិស្ថានជាមួយ GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); បញ្ចូល `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, និងជាជ្រើសរើស `AZURE_OPENAI_API_KEY`; ប្ដូរឈ្មោះទៅ Microsoft Foundry។
- **ឯកសារ** — បានបន្ទាន់សម័យ [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), និង [STUDY_GUIDE.md](./STUDY_GUIDE.md) សម្រាប់ខាងលើ (ការកំណត់អថេរបរិស្ថាន, ខ្លឹមសារ​ផ្ទៀងផ្ទាត់ការ, ការណែនាំអ្នកផ្គត់ផ្គង់, ឈ្មោះ)។

### បានដកចេញ

- ជំហានចូលប្រើម៉ូដែល GitHub និងអថេរបរិស្ថាន ចេញពីឯកសារកំណត់ (បានជំនួសដោយ Azure OpenAI / Microsoft Foundry)។

### សុវត្ថិភាព / ភាពឯកជន (ការសម្អាតការចែករំលែកសាធារណៈ)

- បានសម្អាតលទ្ធផលដំណើរការសៀវភៅកំណត់ត្រា Jupyter ដែល​បានបង្ហាញ **លេខសម្គាល់ការជាវ Azure ជាក់ស្តែង**, ឈ្មោះក្រុមធនធាន / ធនធាន, និងលេខសម្គាល់ការតភ្ជាប់ Bing, បូករួមផ្លូវឯកសារបណ្ដាលផ្ទាល់ និងឈ្មោះអ្នកប្រើក្នុងតំបន់ អ្នកអភិវឌ្ឍ នៅក្នុង៖
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- បានផ្ទៀងផ្ទាត់មិនមានកូនសោ API, Token, លេខសម្គាល់ជាវ, ឬផ្លូវផ្ទាល់ខ្លួននៅក្នុងមាតិកាភាសាអង់គ្លេស ដែលត្រូវបានតាមដានទេ (រាល់ឯកសារ `GITHUB_TOKEN` នៅក្នុង ការងារប្រតិបត្ដិ GitHub Actions និង GitHub MCP server PAT ក្នុងការកំណត់មេរៀនទី 11 គឺត្រឹមត្រូវ និងមិនទាក់ទងរបស់ម៉ូដែល GitHub)។

### ទេសក្តី និងកម្រិតដឹង

- **មិនបានដំណើរការ/បង្កCompilation។** ឧទាហរណ៍សម្រាប់ការបង្រៀនទាំងនេះបានផ្លាស់ប្ដូរដោយចេតនាដើម្បីឱ្យត្រឹមត្រូវ API/ការដាក់ឈ្មោះ; មិនបានដំណើរការជាមួយធនធាន Azure ទំនើបទេ, និងឧទាហរណ៍ .NET មិនបានបង្កCompilation ក្នុងបរិយាកាសនេះទេ។ សូមវាយតម្លៃជាមួយ Microsoft Foundry / Azure OpenAI នៃអ្នកផ្ទាល់។
- **ការដាក់ម៉ូដែលត្រូវតែគាំទ្រ Responses API។** ប្រើការដាក់ដំណើរការដូចជា `gpt-4.1-mini`, `gpt-4.1`, ឬម៉ូដែល `gpt-5.x`។ ម៉ូដែលចាស់គាំទ្រលក្ខណៈ Responses ផ្នែកគ្រឹះ ប៉ុន្តែមិនគ្រប់លក្ខណៈទេ។
- **កំណែស្នូល agent-framework។** ឧទាហរណ៍ផ្តោតទៅកាន់ MAF ថ្មីជាងគេ (`>=1.10.0`)។ ការហៅបង្កើតប៉ុនសិទ្ឋិធម្មតាៗគឺ `client.as_agent(...)`; API ត្រូវបានវាយតម្លៃជាមួយឯកសារបោះពុម្ពរបស់ framework និងប្រមូល build មួយ។ ប្រសិនបើអ្នកបិទភ្ជាប់កំណែផ្សេង សូមពិនិត្យមើលកំណត់មុខងារ (`as_agent` ឬ `create_agent`)។
- **សៀវភៅកំណត់ត្រាដំណើរការមេរៀនទី 08, លេខ 04** មិនបដិសេធ `AzureAIAgentClient` (ពី `agent-framework-azure-ai`) ព្រោះវាប្រើឧបករណ៍សេវាកម្ម Microsoft Foundry Agent Service (ការបណ្តាល Bing, កម្មវិធីបកប្រែមកដំណើរការ); វាប្រើប្រាស់រួច Responses។
- **ការដាក់ម៉ូដែលលំនាំដើមក្នុង .NET។** ឧទាហរណ៍ dotNET មេរៀនទី 08 ខ្លះ បានកូដផ្ទុកម៉ូដែលច្បាស់លាស់ មុននេះ; ឥឡូវនេះការដាក់ម៉ូដែលលំនាំដើមមាន `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`)។ ប្រសិនបើឧទាហរណ៍ត្រូវការបញ្ចូល multimodal/vision, សូមកំណត់ `AZURE_OPENAI_DEPLOYMENT` ទៅម៉ូដែលសមរម្យ។
- **Foundry មូលដ្ឋានក្នុងតំបន់** ផ្ដល់ចំណុចបញ្ចប់មុខងារ **Chat Completions** ដែលសមស្របនឹង OpenAI សម្រាប់ការអភិវឌ្ឍក្នុងតំបន់; សូមប្រើ Azure OpenAI / Microsoft Foundry សម្រាប់មុខងារ Responses API ពេញលេញ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->