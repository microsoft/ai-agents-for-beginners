# മാറ്റങ്ങൾ രേഖ

**പ്രാരംഭക്കാർക്കുള്ള AI ഏജന്റുകൾ** കോഴ്സിലെ പ്രധാനപ്പെട്ട എല്ലാ മാറ്റങ്ങളും ഈ ഫയലിൽ രേഖപ്പെടുത്തിയിട്ടുണ്ട്.

## [പ്രകാശം] — 2026-07-14

ഈ റിലീസ് കോഴ്‌സ് രണ്ടോളം പുതിയതായി ഉപേക്ഷിച്ച മോഡലുകളിലിരുന്ന് നീക്കംചെയ്യുന്നു, ശേഷിച്ച പാഠം നോട്ട്‌ബുക്കുകൾ സ്തിരമായ Microsoft Agent Framework API കടക്കുന്നു, പൈതൺ നോട്ട്‌ബുക്കുകൾ ഒരു പ്രവർത്തനക്ഷമമായ Microsoft Foundry വിന്യാസത്തോട് പൊരുത്തപ്പെടുത്തുന്നു.

### മാറ്റം വരുത്തിയത്

- **ഉപേക്ഷിച്ച മോഡലുകളിൽ നിന്നു സ്ഥലം മാറ്റം (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** ഇരുപുരാണിയായ `gpt-4.1` ഉം `gpt-4.1-mini` ഉം ഇപ്പോൾ ഉപേക്ഷിക്കപ്പെട്ടവയാണ് (പ്രസിദ്ധീകരിച്ച വിരമിക്കൽ തീയതി **14 ഒക്ടോബർ 2026**). എല്ലാ കോഴ്‌സ് റഫറൻസുകളും (ഡോക്സ്, `.env.example`, പൈതൺ/.NET നോട്ട്‌ബുക്കുകൾ, സാമ്പിൾസ്) ഉപേക്ഷിക്കാത്ത `gpt-5-mini`-യാൽ മാറ്റിവെച്ചു. പാഠം 16-ന്റെ മോഡൽ-റൂട്ടിംഗ് ഉദാഹരണത്തിൽ ചെറിയ/വലിയ വരെപരമായ വ്യത്യാസം നിലനിർതുന്നു `gpt-5-nano` (ചെറിയ) കൂടാതെ `gpt-5-mini` (വലിയ) ഉപയോഗിച്ച്. വന്‍ഭാഗം മൂന്നാം-പക്ഷ ഫയലുകൾ ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), ചരിത്ര GitHub മോഡലുകൾ ടെക്സ്റ്റ്, `azure-openai-to-responses` സ്കിൽ ശേഷിക്കുന്ന ശേഷിയുള്ള കുറിപ്പുകൾ ഇടപെട്ടില്ല.
- **പാഠം 14 ഹാൻഡ്ഓഫ് നോട്ട്‌ബുക്ക് സ്തിരമായ API-ലേക്ക് മാറ്റി.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) ഇനി `agent_framework.orchestrations.HandoffBuilder` ഉപയോഗിച്ച് `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` അധിഷ്ഠിത സ്ട്രീമിംഗ്, `FoundryChatClient` (പഴയപാട്‌ 1.0 മുൻപുള്ള `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` ചിഹ്നങ്ങൾ മാറ്റിവെട്ടി) ഉപയോഗിക്കുന്നു.
- **പാഠം 14 ഹ്യൂമൻ-ഇൻ-ദ-ലൂപ്പ് നോട്ട്‌ബുക്ക് സ്തിരമായ API-ലേക്ക് മാറ്റി.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) ഇനി `ctx.request_info(...)` + `@response_handler` ഉപയോഗിച്ച് താൽക്കാലികമായി നിർത്തുന്നു (ഇടപെട്ടത് പഴയ `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), `WorkflowBuilder(start_executor=..., output_executors=[...])` ഉപയോഗിച്ചു നിർമ്മിക്കുന്നു, സങ്കേതബദ്ധമായ ഔട്ട്പുട്ട് `default_options={"response_format": ...}` വഴി നടത്തി, നോട്ട്ബുക്ക് തടസ്സമില്ലാതെ പ്രവർത്തിക്കാൻ (ഇൻപുട്ട് അല്ലെങ്കിൽ തടസമില്ലാതെ) സ്ക്രിപ്റ്റ് ചെയ്ത ഉത്തരം ഉപയോഗിക്കുന്നു.
- **പരിസ്ഥിതി ക്രമീകരണം** ([.env.example](../../.env.example)): മോഡൽ വിന്യാസ പേർ `gpt-5-mini` ആയാക്കി; കൂട്ടിച്ചേർത്തതു `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (പാഠം 16 റൂട്ടിംഗ്) കൂടാതെ മുമ്പ് കാണാനില്ലാത്ത `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (പാഠം 15 ബ്രൗസർ ഉപയോഗം).
- **അനുബന്ധങ്ങൾ** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry`, `agent-framework-openai` നു `~=1.10.0` എന്ന പതിപ്പിൽ പിണ്ഡിപ്പിച്ചു, സ്ഥിരവും സ്ഥിരീകരിക്കപ്പെട്ട സജ്ജമായ ഒരു സെറ്റ് (1.11.0 പരീക്ഷണാത്മകമായ തെറ്റുകൾ ഉള്ള മാറ്റങ്ങൾ കൊണ്ടു വരും).

### കുറിപ്പുകളും അറിയപ്പെടുന്ന പരിമിതികളും

- **പൈതൺ നോട്ട്‌ബുക്കുകൾ നിലവിലുള്ള Microsoft Foundry-യുമായി പരിശോധന നടത്തി.** `gpt-5-mini` (പാഠം 16 റൂട്ടിംഗ് വേണ്ടി `gpt-5-nano`) ഉപയോഗിച്ച് Microsoft Foundry പ്രോജക്ടിൽ `nbconvert`-ഉടെ ഹെഡ്‌ലസ് പ്രവർത്തനമായ നിർവഹണം ചെയ്തു. വിചാരാർത്ഥം അംഗീകരിക്കാത്ത മോഡലുകൾ നിങ്ങളുടെ തന്നെ പ്രോജക്ടിൽ വിന്യസിക്കണം; നോട്ട്‌ബുക്കുകൾ വിന്യാസത്തിന് പേരായി `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` ഉപയോഗിക്കുന്നു.
- **കജ്ജർ പാഠങ്ങൾക്കായി അധികവനിതകൾ ആവശ്യമാണ്.** പാഠം 05 ആസുറേ AI സെർച്ച് ആവശ്യമാണ്; പാഠം 08 ബിംഗ്-അടിസ്ഥാന വർക്ക്ഫ്ലോ (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) ബിംഗ് ബന്ധവും Microsoft Foundry ഏജന്റ് സർവീസ് ഹോസ്റ്റുചെയ്‌ത ഉപകരണങ്ങളും ആവശ്യമാണ്; പാഠം 13 (Cognee)യും പാഠം 17 (Foundry Local) യ്ക്ക് അവരുടെ സ്വന്തം റൺടൈമുകൾ ആവശ്യമാണ്.

## [പ്രകാശം] — 2026-07-13

ഈ റിലീസ് രണ്ട് പുതിയ പാഠങ്ങൾ ചേർത്തിരിക്കുന്നു, വിന്യാസമായ അർച്ചിനെ പൂർത്തിയാക്കുന്നു — ഏജന്റുകളെ Microsoft Foundry-യിലേക്ക് സ്കെയ്ല് ചെയ്ത് ഒറ്റ ജോലിസ്ഥലത്തിലേക്ക് താഴ്ത്തുന്നു — കൂടാതെ സ്മോക്ക് ടെസ്റ്റ് പൈപ്പ്ലൈൻ, പുതുക്കിയ കോഴ്‌സ് നാവിഗേഷൻ, പുതിയ പഠനാനുഭവങ്ങൾ, ആൻഡ് അപ്ഡേറ്റുചെയ്‌ത ബ്രാൻഡിംഗ്.

### ചേർത്തത്

- **പാഠം 16 — Microsoft Foundry-യുമായി സ്കെയില 가능한 ഏജന്റുകൾ വിന്യാസം.** പുതിയ പാഠം [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) കൂടാതെ പ്രവർത്തനക്ഷമമായ നോട്ട്‌ബുക്ക് [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) നിർമ്മിക്കുന്നു ഉത്പാദന വാണിജ്യ-സപ്പോർട്ട് ഏജന്റ് (ഉപകരണങ്ങൾ, RAG, മെമ്മറി, മോഡൽ റൂട്ടിംഗ്, പ്രതികരണ കാഷിംഗ്, മനുഷ്യനുവാദം, വിലയിരുത്തൽ ഗേറ്റ്, OpenTelemetry ട്രേസിംഗ്), സൃഷ്ടിപരിച്ഛേദം/വിന്യാസ/റൺടൈം Mermaid ചിത്രങ്ങൾ, ഒരു അറിവ് പരിശോധന, ഒരു അസൈന്മെന്റ്, ഒരു വെല്ലുവിളി.
- **പാഠം 17 — Foundry Local-ഉം Qwen-ഉം ഉപയോഗിച്ച് പ്രാദേശിക AI ഏജന്റുകൾ സൃഷ്ടിക്കൽ.** പുതിയ പാഠം [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) കൂടാതെ നോട്ട്‌ബുക്ക് [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) ഒരു പൂർണ്ണമായി ഉപകരണത്തിൽ അധിഷ്ഠിത എഞ്ചിനീയറിംഗ് അസിസ്റ്റന്റ് (Qwen ഫംഗ്ഷൻ കോൾ അംഗീകരിച്ച് Foundry Local-ൽ, സാൻഡ്‌ബോക്സ്ഡ് ഫയൽ ഉപകരണങ്ങൾ, പ്രാദേശിക RAG Chroma ഉപയോഗിച്ച്, ഐച്ഛിക പ്രാദേശിക MCP), പ്രാദേശിക മാത്രം / പ്രാദേശിക-RAG / ഉപകരണ കോളിങ് ചിത്രങ്ങൾ, അറിവ് പരിശോധന, അസൈന്മെന്റ്, വെല്ലുവിളി എന്നിവ ചേർത്ത്.
- **സ്മോക്ക്-ടെസ്റ്റ് പൈപ്പ്ലൈൻ.** പുതിയ [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) വർക്ക്‌ഫ്ലോ [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) കൂടാതെ പാഠങ്ങങ്ങളിൽ 01, 04, 05, 16 ലെ വിന്യസിക്കാൻ കഴിയുന്ന ഏജന്റുകൾക്ക് വേണ്ടി [tests/](./tests/README.md) കീഴിലുള്ള പാഠന അസൂത്രണങ്ങൾ, ഓരോ അസൂത്രണവും അതിന്റെ പാഠവും ഹോസ്റ്റുചെയ്‌ത ഏജന്റ് നാമവും തെളിയിക്കുന്ന README. പാഠം 16-ന് ഒരു "വിന്യസിച്ച ഏജന്റിന് സ്മോക്ക് ടെസ്റ്റുകൾ ഉപയോഗിച്ച് പരിശോധിക്കൽ" വിഭാഗം; പാഠങ്ങൾ 01/04/05 മുൻഗണനാ സ്മോക്ക്-ടെസ്റ്റ് സൂചന ചേർത്തു.
- **പഠനാനുഭവങ്ങൾ.** പുതിയ ഏജന്റ് സ്കിലുകൾ `.agents/skills/`ൽ: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (പാഠങ്ങൾ 16, 17 കൊണ്ടുള്ള മാർഗ്ഗനിർദ്ദേശം ഉൾക്കൊള്ളുന്നു), [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (Microsoft Foundry / Azure OpenAI ലെ ഒരു ലൈവിന്റെ പശ്ചാത്തലംകൊണ്ട് നോട്ട്‌ബുക്ക് സാമ്പിളുകൾ എങ്ങനെ പരിശോദിക്കാമെന്ന്).
- **നോട്ട്ബുക്ക് സാധുത പരിശോധന റണ്ണർ.** പുതിയ [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) എല്ലാ പൈതൺ നോട്ട്‌ബുക്കുകളും ഹെട്ലെസായി `nbconvert` ഉപയോഗിച്ച് പ്രവർത്തിപ്പിച്ച് PASS/FAIL മാട്രിക്സ്(പ്ലസും `results.json`) പ്രിന്റ് ചെയ്യുന്നു. അത് സ്വയം റിപൊ റൂട്ട്‌ ആയി പോളും, പൈതൺ കണ്ടെത്തും, കോഴ്സ് പുറത്തുള്ള നോട്ട്‌ബുക്കുകൾ (`.venv`, `site-packages`, `translations`, സ്കിൽ ടെംപ്ലേറ്റ് അസറ്റ്സ്) കൂടാതെ `.NET` നോട്ട്‌ബുക്കുകളും ഒഴിവാക്കും, `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, `-Python` ملاتړിക്കുന്നു.
- **കോഴ്‌സ് നാവിഗേഷൻ.** പാഠങ്ങൾ 11–15 ലേക്ക് മുൻപ് കാണാനില്ലാത്ത മുൻപ്/അടുത്ത പാഠം ലിങ്കുകൾ ചേർത്തു, 00 മുതൽ 18 വരെ ദിശകളിൽ കോഴ്‌സ് മുഴുവനും നിര.
- **പുതിയ തമ്പ്നെയിലുകൾ.** പാഠങ്ങൾ 16, 17 ന്റെ തമ്പ്നെയിലുകൾ, പുതുക്കിയ റിപ്പൊ സോഷ്യൽ ചിത്രം [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (ഇപ്പോൾ രണ്ട് പുതിയ പാഠങ്ങളും `aka.ms/ai-agents-beginners` URL പ്രചാരിപ്പിക്കുന്നു).
- **അനുബന്ധങ്ങൾ** ([requirements.txt](../../requirements.txt)): പാഠം 17ക്കായി `foundry-local-sdk` എന്നും `chromadb` എന്നും ചേർത്തു.

### മാറ്റം വരുത്തിയത്

- **പ്രധാന [README.md](./README.md)** പാഠ പട്ടിക: പാഠങ്ങൾ 16, 17 ഇനി അവരുടെ ഉള്ളടക്കത്തിലേക്ക് ലിങ്ക് ചെയ്യുന്നു (മുൻപ് "വരാൻ വന്നു"); റിപ്പൊ ചിത്രം `repo-thumbnailv3.png` ആയി അപ്‌ഡേറ്റ് ചെയ്തു.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: പാഠം ബൈ പാഠം ഗൈഡിലും പഠന പാതകളിലും പാഠങ്ങൾ 16, 17 ചേർത്തുവേക്കുകയും "വിന്യസിച്ച ഏജന്റുകൾക്ക് സ്മോക്ക് ടെസ്റ്റുകൾ ഉപയോഗിച്ച് പരിശോധന" എന്ന ഭാഗവും ചേർത്തു.
- **[AGENTS.md](./AGENTS.md)**: പാഠങ്ങളുടെ എണ്ണം/വിവരണം (00–18) അപ്‌ഡേറ്റ് ചെയ്തു, സ്മോക്ക്-ടെസ്റ്റിംഗ് പരിശോധനാംശവും പാഠം 16/17 സാമ്പിൾ നാമ ദൃശ്യങ്ങളുമു ചേർത്തു.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "മുൻപത്തെ പാഠം" ഇനി പാഠം 17-നെ ചൂണ്ടുന്നു (മുമ്പ് പാഠം 15), സീരീസ് പൂർത്തിയാക്കുന്നു.
- **ഉപേക്ഷിക്കാത്ത മോഡലുകളിൽ സ്റ്റാൻഡേർഡ് റഫറൻസുകൾ.** എല്ലാ `gpt-4o` / `gpt-4o-mini` റഫറൻസുകളും കോഴ്സിൽ നിന്നും (ഡോക്സ്, `.env.example`, പൈതൺ/.NET നോട്ട്‌ബുക്കുകൾ, സാമ്പിളുകൾ) `gpt-4.1-mini`-യാൽ മാറ്റി — `gpt-4o` എല്ലാ പതിപ്പുകളും 2026-ൽ വിരമിക്കുന്നു. പാഠം 16 മോഡൽ റൂട്ടിംഗ് ഉദാഹരണത്തിൽ ചെറിയ/വലിയ തിരിച്ചറിയൽ `gpt-4.1-mini` (ചെറിയ) കൂടാതെ `gpt-4.1` (വലിയ) ഉപയോഗിച്ച് തുടരുന്നു. പൈതൺ നോട്ട്‌ബുക്കുകൾ ഇനി മോഡൽ പേരുകൾ ഹാർഡ്‌കോഡ് ചെയ്യാതെ പരിസ്ഥിതി ചലകങ്ങളിൽ നിന്ന് തിരഞ്ഞെടുക്കുന്നു (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`).

### കുറിപ്പുകളും അറിയപ്പെടുന്ന പരിമിതികളും

- **ലൈവ് ആസുറേ യിൽ പ്രവർത്തിച്ചിട്ടില്ല.** പുതിയ പാഠങ്ങളുടെ നോട്ട്‌ബുക്കുകൾ പഠന സാമ്പിൾസ്; നിങ്ങളുടെ സ്വന്തം Microsoft Foundry / Foundry Local സജ്ജീകരണത്തിൽ ഇവ പ്രവർത്തിപ്പിച്ച് പരിശോധിക്കുക. സ്മോക്ക്-ടെസ്റ്റ് വർക്ക്‌ഫ്ലോയ്ക്ക് പാഠം ഏജന്റ് വിന്യസിച്ചും, Azure OIDC രഹസ്സുകൾ (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) **Azure AI User** റോളോടെ Foundry പ്രോജക്ട് പരിധിയിൽ ക്രമീകരിച്ചിട്ടുണ്ടാകണം.
- **പാഠം 17 പ്രാദേശിക മാത്രം.** അതിന് Foundry Responses എന്റ്പോയിന്റ് ഇല്ല, അതിനാൽ സ്മോക്ക്-ടെസ്റ്റ് പ്രവർത്തനം ബാധകമല്ല; നിങ്ങളുടെ ജോലിസ്ഥലത്ത് നോട്ട്‌ബുക്ക് പ്രവർത്തിപ്പിച്ച് പരിശോധിക്കണം.

## [പ്രകാശം] — 2026-07-06

ഈ റിലീസ് കോഴ്സ് **Azure OpenAI Responses API**-യിലേക്ക് മാറ്റം വരുത്തുന്നു, **Microsoft Foundry**-യും **Microsoft Agent Framework (MAF)**-ഉം ഉൽപ്പന്ന നാമകരണത്തിൽ സുസ്ഥിരത നൽകുന്നു, GitHub മോഡലുകൾ വിരമിക്കുന്നു, SDK പതിപ്പുകൾ പുതുക്കുന്നു, പ്രാദേശിക മോഡലുകൾക്കും Foundry ല് മറ്റു ഫ്രെയിംവർകുകളെ ഹോസ്റ്റ് ചെയ്യുന്നതിനും പുതിയ ഉള്ളടക്കം ചേർക്കുന്നു.

### ചേർത്തത്

- **മൈഗ്രേഷൻ സ്കിൽ** — `.agents/skills/`-ൽ [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) ഏജന്റ് സ്കിൽ ഇൻസ്റ്റാൾ ചെയ്തു ([Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses))-ൽ നിന്നും, അതിന്റെ റഫറൻസുകളും സ്കാനർ സ്ക്രിപ്റ്റും ഉൾപ്പെടെ.
- **Foundry Local (ഉപകരണത്തിൽ മോഡലുകൾ പ്രവർത്തിപ്പിക്കൽ)** — [00-course-setup/README.md](./00-course-setup/README.md)-ലെയും പുതിയ "Alternative Provider: Foundry Local" വിഭാഗം; ഇൻസ്റ്റാൾ (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, Microsoft Agent Framework-അയേക്കുള്ള `FoundryLocalManager` വൈയർ ചെയ്യൽ `OpenAIChatClient` വഴി ഉൾപ്പെടുന്നു.
- **Microsoft Foundry-ൽ LangChain / LangGraph ഏജന്റുകൾ ഹോസ്റ്റിംഗ്** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md)-ൽ പുതിയ വിഭാഗം, പ്രവർത്തനക്ഷമമായ സാമ്പിൾ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), `langchain-azure-ai[hosting]` ഉം `/responses` പ്രോട്ടോക്കോൾ ഉപയോഗിക്കുന്ന `ResponsesHostServer` ഉം ഉപയോഗിച്ച്, [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) അടിസ്ഥാനമാക്കിയുള്ളത്.
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md)-ൽ പുതിയ "യഥാർത്ഥ ലോക ഉദാഹരണം: Microsoft Project Opal" വിഭാഗം, Opal ഒരു എന്റർപ്രൈസ് കമ്പ്യൂട്ടർ-ഉപയോഗ ഏജന്റായി രൂപപ്പെടുത്തിയിട്ടുണ്ട്, കോഴ്‌സ് ആശയങ്ങളോട് (ഹ്യൂമൻ-ഇൻ-ദ-ലൂപ്പ്, ആമുഖം/സുരക്ഷ, പദ്ധതിയിടൽ, സ്കിലുകൾ) ബന്ധിപ്പിക്കുന്നു.
- **രണ്ടാമത്തെ പാഠം 02 പൈതൺ സാമ്പിൾ** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) ചേർത്തു (മാറ്റം കാണുക — പഴയ Semantic Kernel നോട്ട്‌ബുക്കിൽ നിന്നു മൈഗ്രേറ്റ് ചെയ്തു), പാഠം READMEയിൽ ലിങ്കുചെയ്‌ത്.
- **STUDY_GUIDE.md-ൽ** മോഡലുകളും പ്രൊവൈഡർമാരും വിഭാഗം ചേർത്തു.

### മാറ്റം വരുത്തിയത്

- **ചാറ്റ് പൂർത്തീകരണങ്ങൾ → Responses API (Python).** നേരിട്ടു മോഡൽ വിളിച്ച് പ്രവർത്തിച്ച സാമ്പിൾസ് Chat Completions-നിന്ന് Responses API-യിലേക്ക് മാറ്റിയിട്ടുണ്ട് (`client.responses.create(input=..., store=False)`, `resp.output_text`), സ്ഥിരമായ Azure OpenAI `/openai/v1/` എൻഡ്‌പോയിന്റിൽ `OpenAI` ക്ലയന്റ് ഉപയോഗിച്ച് (ആപ്‌ഐ പതിപ്പ് ഇല്ല). ബാധിച്ച സാമ്പിൾസ് ഉൾപ്പെടുന്നു:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — പൂർണ്ണമായ ഫംഗ്ഷൻ-കാളിങ് നടത്തിപ്പ് (ഉപകരണ സ്കീമ Responses ഫോർമാറ്റിലേക്ക് മൂടിയത്, ഫംഗ്ഷൻ ഫലം `function_call_output`, `max_output_tokens` മുതലായവയായി തിരിച്ചുകൊടുത്തു).

- **GitHub മോഡലുകൾ → Azure OpenAI.** GitHub മോഡലുകൾ പ്രായോഗികമല്ല (ജൂലൈ 2026-ൽ വിരമിക്കുന്നു) കൂടാതെ Responses API-നെ പിന്തുണയ്ക്കില്ല. Python, .NET സാമ്പിളുകളിലെ എല്ലാ GitHub മോഡൽ കോഡ് പാതകളും Azure OpenAI / Microsoft Foundry-യിലേക്ക് പരിവർത്തനം ചെയ്‌തു:
  - Python: പാഠം 08 വർക്ക്‌ഫ്ലോ നോട്ട്ബുക്കുകൾ (`01`–`03`), പാഠം 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + അനുബന്ധ `.md` ഡോക്യുമെന്റുകൾ, പാഠം 08 dotNET വർക്ക്‌ഫ്ലോ നോട്ട്ബുക്കുകൾ/`.md` (`01`–`03`) ഇനി `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` എന്ന വ്യവസ്ഥയോടും `AzureCliCredential` ഉപയോഗിച്ചും പ്രവർത്തിക്കുന്നു.
- **Semantic Kernel → Microsoft Agent Framework.** മുൻ `02-semantic-kernel.ipynb` Microsoft Agent Framework Azure OpenAI (Responses API) ഉപയോഗിച്ച് എഴുതിവെച്ചുവും പുനർനാമകരിച്ചും `02-python-agent-framework-azure-openai.ipynb` ആയി മാറ്റിയിട്ടുണ്ട്.
- **`FoundryChatClient` + `as_agent`-ൽ മാനദണ്ഡം.** READMEയും നോട്ട്ബുക്ക് കോഡും, മുൻപ് `AzureAIProjectAgentProvider` ഉദ്ധരിച്ചിരിക്കുന്നവ, പാഠം 01-ൽ ഉപയോഗിക്കുന്ന മാനദണ്ഡത്തിലുള്ള മാതൃകയിലേയ്ക്ക് അസാധാരണ പരിഷ്കരിച്ചു; അതായത് `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` കൂടാതെ `provider.as_agent(...)` എന്ന രീതിയിലാണ്. ഇത് പാഠം 02–14യുടെ README-കളും നോട്ട്ബുക്കുകളും അപ്ഡേറ്റ് ചെയ്തിട്ടുണ്ട് (ഉദാഹരണത്തിന്, പാഠം 13 മെമ്മറി, എല്ലാ പാഠം 14 നോട്ട്ബുക്കുകളും, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **ഉല്പന്ന നാമകരണം.** ഇംഗ്ലീഷ് ഉള്ളടക്കത്തിൽ താഴെപറയുന്നപോലെ പുനർനാമകരണം:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (മാറ്റം ഇല്ല: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", പരിസ്ഥിതി-വേരിയബിൾ നാമങ്ങൾ.)
- **അനുഭവങ്ങൾ** ([requirements.txt](../../requirements.txt)):
  - പിനതിരുത്തുകയും ചെയ്തിരിക്കുന്നു: `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - പിനതിരുത്തുകയും ചെയ്തിരിക്കുന്നു: `openai>=1.108.1` (Responses APIയ്ക്ക് കുറഞ്ഞത്).
  - ഒഴിവാക്കി: `azure-ai-inference` (GitHub മോഡൽ സാമ്പിളുകൾ മാറ്റിയതിൽ മാത്രമേ ഉപയോഗിച്ചുള്ളൂ).
- **പരിസ്ഥിതി ക്രമീകരണം** ([.env.example](../../.env.example)): GitHub മോഡൽ വേരിയബിൾസ് (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) നീക്കം ചെയ്തിരിക്കുന്നു; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, ആവശ്യമായ `AZURE_OPENAI_API_KEY` ചേർത്തിട്ടുണ്ട്; Microsoft Foundry നാമകരണം ചെയ്തു.
- **ഡോക്യുമെന്റേഷൻ** — മുകളിൽ പറയപ്പെട്ടതിനനുസരിച്ച് [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), [STUDY_GUIDE.md](./STUDY_GUIDE.md) അപ്ഡേറ്റ് ചെയ്തിട്ടുണ്ട് (പരിസ്ഥിതി വേരിയബിൾസ് ക്രമീകരണം, പരിശോധന സ്നിപ്പെറ്റ്, പ്രൊവൈഡർ മാർഗനിർദ്ദേശം, നാമകരണങ്ങൾ).

### നീക്കംചെയ്തവ

- GitHub മോഡൽ ഓൺബോർഡിംഗ് ഘട്ടങ്ങളും പരിസ്ഥിതി വേരിയബിൾസും സെറ്റപ്പ് ഡോക്യുമെന്റുകളിൽ നിന്ന് (Azure OpenAI / Microsoft Foundry ഉപയോക്താക്കൾ മാറ്റി).

### ഭദ്രത / ഗോപ്യത (പൊതു പങ്കുവെക്കൽ ശുചീകരണം)

- യഥാർത്ഥ **Azure Subscription ID**, റിസോഴ്‌സ് ഗ്രൂപ്പ് / റിസോഴ്‌സ് നാമങ്ങൾ, Bing കണക്ഷൻ ID, ഡെവലപ്പർ **പ്രാദേശിക ഫയൽ പാതകളും ഉപയോക്തൃനാമങ്ങളും** ചൊറിയുന്ന Jupyter നോട്ട്ബുക്ക് ലേഖനം ക്ലിയർ ചെയ്തിരിക്കുന്നു:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- മൂന്നാം വ്യക്തി API കീകൾ, ടോകണുകൾ, സബ്സ്ക്രിപ്ഷൻ ഐഡികൾ, വ്യക്തിഗത പാതകൾ ഇംഗ്ലീഷ് ഉള്ളടക്കത്തിൽ കണ്ടെത്താനായിട്ടില്ല (മിച്ചംശങ്ങൾ GitHub പ്രവർത്തന ടോക്കൺ, GitHub MCP സർവർ PAT എന്നിവയിൽ മാത്രമാണ് — ആ ഗിറ്റ്ഹബ് മോഡൽസുമായി ബന്ധമില്ലാത്തവ).

### കുറിപ്പുകളും അറിയപ്പെടുന്ന നിയന്ത്രണങ്ങളും

- **നടത്തിയിട്ടില്ല/കമ്പൈൽ ചെയ്‌തിരിയില്ല.** ഇവ വിദ്യാഭ്യാസ സാമ്പിളുകളാണ്, API/നാമകരണം ശരിയാക്കിയിട്ടുണ്ട്; നിലവിലുള്ള Azure റിസോഴ്‌സുകളിൽ പ്രവർത്തിപ്പിച്ചിട്ടില്ല, .NET സാമ്പിളുകൾ ഈ പരിസരത്തിൽ കമ്പൈൽ ചെയ്തിട്ടില്ല. നിങ്ങളുടെ സ്വന്തം Microsoft Foundry / Azure OpenAI ഡിപ്ലോയ്മെന്റ് ഉപയോഗിച്ച് സ്ഥിരീകരിക്കുക.
- **മോഡൽ ഡിപ്ലോയ്മെന്റ് Responses API പിന്തുണയ്ക്കണം.** `gpt-4.1-mini`, `gpt-4.1`, അല്ലെങ്കിൽ `gpt-5.x` മോഡൽ പോലുള്ള ഡിപ്ലോയ്മെന്റ് ഉപയോഗിക്കുക. പഴയ മോഡലുകൾ Responses അടിസ്ഥാന പ്രവർത്തനങ്ങൾ പിന്തുണയ്ക്കുന്നുവെങ്കിലും എല്ലാ ഫീച്ചറും അല്ല.
- **Agent-framework പതിപ്പ്.** സാമ്പിളുകൾ ഏറ്റവും പുതിയ MAF (`>=1.10.0`) ഉദ്ദേശിക്കുന്നതാണ്. ഔദ്യോഗിക ഏജന്റ് നിർമ്മാണ കോൾ `client.as_agent(...)`; APIകൾ ഫ്രെയിംവർക്കിന്റെ പ്രസിദ്ധീകരിച്ച ഡോക്യുമെന്റേഷനിലും ഇൻസ്റ്റാൾ ചെയ്ത ബിൽഡിലും പരിശോധന നടത്തിയിട്ടുണ്ട്. മറ്റ് പതിപ്പുകൾ ഉപയോഗിച്ച് ഉറപ്പു വരുത്തുക (`as_agent` vs `create_agent` ലഭ്യത).
- **പാഠം 08 വർക്‌ഫ്ലോ നോട്ട്ബുക്ക് 04** നിയമിതമായും `AzureAIAgentClient` (`agent-framework-azure-ai` ലσίനായി) സൂക്ഷിക്കുന്നു കാരണം അത് Microsoft Foundry Agent Service ഹോസ്റ്റ് ചെയ്ത ഉപകരണങ്ങൾ (Bing ഗ്രൗണ്ടിംഗ്, കോഡ് ഇന്റർപ്രീറ്റർ) ഉപയോഗിക്കുന്നു; ഇതിനകം Responses അടിസ്ഥാനത്തിലാണ്.
- **.NET ഡിഫോൾട്ട് ഡിപ്ലോയ്‌മെന്റ്.** പാടം 08 dotNET വർക്ഫ്ലോ സാമ്പിളുകൾ നേരത്തേ ഒരു പ്രത്യേക മോഡൽ ഹാർഡ്‌കോഡ് ചെയ്തിരുന്നു; ഇപ്പോള്‍ ഇവ `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) ഡിഫോൾട്ട് ചെയ്യുന്നു. ഒരു സാമ്പിൾ മൾട്ടിമോഡൽ/വിഷൻ ഇൻപുട്ടിൽ ആശ്രയിച്ചിരിക്കുകയാണെങ്കിൽ, `AZURE_OPENAI_DEPLOYMENT` ഒരു അനുയോജ്യമായ മോഡലായി സജ്ജമാക്കുക.
- **Foundry Local** OpenAI-സൗഹൃദ **ചാറ്റ് കംപ്ലീഷൻസ്** എന്റ്‌പോയിന്റ് തുറന്നു പ്രാദേശിക വികസനത്തിന് ഉദ്ദേശിച്ചതാണ; പൂർണ്ണ Responses API ഫീച്ചറിനായി Azure OpenAI / Microsoft Foundry ഉപയോഗിക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->