# മാറ്റങ്ങൾ രേഖപ്പെടുത്തൽ

**AI Agents for Beginners** കോഴ്സ് സംബന്ധിച്ച എല്ലാ ശ്രദ്ധേയമായ മാറ്റങ്ങളും ഈ ഫയലിൽ രേഖപ്പെടുത്തിയിട്ടുണ്ട്.

## [മോഷ്ടിക്കപ്പെട്ടിട്ടില്ല] — 2026-07-06

ഈ റിലീസ് കോഴ്സ് **Azure OpenAI Responses API**-യിലേക്ക് മാറ്റുന്നു, **Microsoft Foundry**-യിലും **Microsoft Agent Framework (MAF)**-യിലും ഉത്പന്ന നാമകരണം ഏകരൂപമാക്കുന്നു, GitHub Models പിന്‍വലിക്കുന്നു, SDK പതിപ്പുകൾ അപ്‌ഡേറ്റ് ചെയ്യുന്നു, Foundry-യില്‍ പ്രാദേശിക മോഡലുകളും മറ്റു ഫ്രെയിംവർക്കുകളും ഹോസ്റ്റ് ചെയ്യുന്നതിനെ കുറിച്ച് പുതിയ ഉള്ളടക്കങ്ങൾ ചേർക്കുന്നു.

### ചേർത്തുവെച്ചത്

- **മൈഗ്രേഷൻ സ്‌കിൽ** — `.agents/skills/`-ലേക്ക് [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) ഏജന്റ് സ്‌കിൽ ഇൻസ്റ്റാൾ ചെയ്തു ([Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses) നിന്നുള്ളത്) അതിന്റെ റഫറൻസുകളും സ്കാനർ സ്ക്രിപ്റ്റും ഉൾപ്പെടെ.
- **ഫൗണ്ടറി ലോക്കൽ (മോഡലുകൾ ഡിവൈസിൽ റൺ ചെയ്യുക)** — [00-course-setup/README.md](./00-course-setup/README.md) ൽ പുതിയ "Alternative Provider: Foundry Local" വിഭാഗം, ഇൻസ്റ്റാൾ ചെയ്യൽ (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, `FoundryLocalManager`-നെ Microsoft Agent Framework-ലേക്ക് `OpenAIChatClient` മുഖേന വയറിങ് ചെയ്യൽ ഉൾപ്പെടെ.
- **Microsoft Foundry-യിൽ LangChain / LangGraph ഏജന്റുകൾ ഹോസ്റ്റ് ചെയ്യുക** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ൽ പുതിയ സെക്ഷൻ, കൂടാതെ `langchain-azure-ai[hosting]`യും `ResponsesHostServer`-ഉം ( `/responses` പ്രോട്ടോക്കോൾ) ഉപയോഗിച്ചുള്ള ഒരിക്കൽ പ്രവർത്തിപ്പിക്കാവുന്ന സാമ്പിൾ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) അടിസ്ഥാനമാക്കി.
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) ൽ പുതിയ "യഥാർത്ഥ ലോക ഉദാഹരണം: Microsoft Project Opal" വിഭാഗം, Opal നെ ഒരു എന്റർപ്രൈസ് കമ്പ്യൂട്ടർ-ഉപയോഗ ഏജന്റായി കാണിച്ച് കോഴ്സ് ആശയങ്ങൾ (ഹ്യൂമൻ-ഇൻ-ദ ലൂപ്പ്, വിശ്വാസം/സുരക്ഷ, പ്ലാനിംഗ്, സ്‌കിലുകൾ) അവശ്യമാക്കുന്നു.
- **രണ്ടാമത്തെ പാഠം 02 Python സാമ്പിൾ** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) ചേർത്തു ("മാറ്റിയത്" കാണുക — മുന്‍ സിമാന്റിക് കർണൽ നോട്ട്‌ബുക്ക്-ലിൽ നിന്നും മാറ്റി), പാഠം README-യിൽ ലിങ്ക് ചേർത്തു.
- [STUDY_GUIDE.md](./STUDY_GUIDE.md)ൽ **Models and Providers** വിഭാഗം ചേർത്തു.

### മാറ്റം വരുത്തിയത്

- **ചാറ്റ് പൂർത്തീകരണങ്ങൾ → Responses API (Python).** മോഡൽ നേരിട്ട് വിളിച്ചിരുന്നു എന്നു കാണുന്ന സാമ്പിളുകൾ Chat Completions-ൽ നിന്നും Responses API-യിലേക്ക് മാറ്റി (`client.responses.create(input=..., store=False)`, `resp.output_text`), `OpenAI` ക്ലയന്റ് ഉപയോഗിച്ച് സ്ഥിരതയുള്ള Azure OpenAI `/openai/v1/` എൻഡ്‌പോയിന്റ് (ആപിഐ പതിപ്പ് ഇല്ലാതെ) മുഖാന്തിരം. ബാധിച്ച സാമ്പിളുകൾ:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — ഫുള്‍ ഫങ്ഷൻ-കോളിങ് വാക്ക്‌ത്രൂ (ഉപകരണ സ്കീമ Responses ഫോർമാറ്റിലേക്ക് ഫ്ലാറ്റൻ ചെയ്തു, ഫംഗ്ഷൻ ഫലം `function_call_output`, `max_output_tokens` ആകെയുള്ളവയായി തിരിച്ചറിയുന്നു).
- **GitHub Models → Azure OpenAI.** GitHub Models പിന്‍വലിക്കുന്നു (**ജൂലൈ 2026** ന്), Responses API പിന്തുണില്ല. Python, .NET സാമ്പിളുകൾ Azure OpenAI / Microsoft Foundry-യിലേക്കു മാറ്റി:
  - Python: പാഠം 08 workflow നോട്ട്‌ബുക്കുകൾ (`01`–`03`), പാഠം 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + അതേപോലെ `.md` ഡോക്സ്, പാഠം 08 dotNET workflow നോട്ട് ബുക്കുകൾ/`.md` (`01`–`03`) ഇപ്പോൾ `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` ഉപയോഗിക്കുന്നു `AzureCliCredential`-നൊപ്പം.
- **സെമാന്റിക് കർണൽ → Microsoft Agent Framework.** പഴയ `02-semantic-kernel.ipynb` Microsoft Agent Framework Azure OpenAI (Responses API) ഉപയോഗിക്കാൻ പുനःരചിച്ചും `02-python-agent-framework-azure-openai.ipynb` ആയി പുനർനാമകരിച്ചത്.
- **`FoundryChatClient` + `as_agent`-ൽ ഏകരൂപമാക്കി.** `AzureAIProjectAgentProvider`-നെ സൂചിപ്പിച്ച README, നോട്ട് ബുക്ക് കോഡ്lektion 01-ൽ ഉപയോഗിച്ച canonical മാതൃകിയിലേക്ക് മാറ്റിയിരിക്കുന്നു: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` കൂടാതെ `provider.as_agent(...)`. പാഠം 02–14 READMEs, നോട്ട് ബുക്കുകളിൽ അപ്‌ഡേറ്റ് ചെയ്‌തു (ഉദാ: പാഠം 13 മെമ്മറി, പാഠം 14 എല്ലാ നോട്ട് ബുക്കുകളും, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **ഉത്പന്ന നാമകരണം.** ഇംഗ്ലീഷ് ഉള്ളടക്കത്തിൽ പുനർനാമകരണം:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (മാറ്റം ഇല്ല: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", പരിസ്ഥിതി വ്യത്യാസങ്ങളുടെ പേര്)
- **അനുഭ്രാന്തികൾ** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` പിന്‍മുന്നിൽ സൂചിപ്പിച്ചു.
  - Responses API സപ്പോർട്ടിനായി കുറഞ്ഞത് `openai>=1.108.1` പിന്‍മുന്നിൽ ചേർത്തു.
  - GitHub Models സാമ്പിളുകളിൽ മാത്രമുള്ള `azure-ai-inference` നീക്കി.
- **പരിസ്ഥിതി കോൺഫിഗറേഷൻ** ([.env.example](../../.env.example)): GitHub Models-സംബന്ധമായ വാരിേയബിളുകൾ നീക്കി (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); ചേർത്തു `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, വിവേചനം യുള്ള `AZURE_OPENAI_API_KEY`; നാമകരണം Microsoft Foundry-ൽ അപ്‌ഡേറ്റ് ചെയ്തു.
- **ഡോക്യുമെന്റേഷൻ** — മുകളിൽ പറഞ്ഞവയ്ക്ക് അനുയോജ്യമായി [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), [STUDY_GUIDE.md](./STUDY_GUIDE.md) അപ്‌ഡേറ്റ് ചെയ്തു (സെറ്റ് അപ്പ് പരിസ്ഥിതി വ്യത്യാസങ്ങൾ, പരിശോധന സ്നിപ്പറ്റ്, പ്രൊവൈഡർ മാർഗനിർദ്ദേശങ്ങൾ, നാമവ്യവസ്ഥ).

### നീക്കിയവ

- GitHub Models ഓൺബോർഡിംഗ് ഘട്ടങ്ങളും പരിസ്ഥിതി വ്യത്യാസങ്ങളും സെറ്റ് അപ്പ് ഡോക്യുമെന്റുകളിൽ നിന്നു നീക്കി (Azure OpenAI / Microsoft Foundry മൂലം മാറിയതിന്റെ പേരിൽ).

### സുരക്ഷ / സ്വകാര്യത (പബ്ലിക് ഷെയറിംഗ് ക്ലീനപ്പുകൾ)

- Jupyter നോട്ട് ബുക്ക് എക്സിക്യൂഷൻ ഔട്ട്പുട്ടുകളിൽ നിന്നും യഥാർത്ഥ **Azure സബ്സ്ക്രിപ്ഷൻ ID**, റിസോർസ്-ഗ്രൂപ്പ് / റിസോർസ് നാമങ്ങൾ, Bing കണക്ഷൻ ID, ഡെവലപ്പർ **ലോകൽ ഫയൽ പാതകളും യൂസർനാമുകളും** മായ്ചു:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- API കീകൾ, ടോക്കണുകൾ, സബ്സ്ക്രിപ്ഷൻ IDകൾ, അല്ലെങ്കിൽ വ്യക്തിഗത പാതകൾ ഇംഗ്ലീഷ് ഉള്ളടക്കത്തില്‍ ഉണ്ടാകാത്തത് സ്ഥിരീകരിച്ചു (`GITHUB_TOKEN` റഫറൻസുകൾ GitHub ആക്ഷൻസിലെ ടോക്കണും പാഠം 11 സെറ്റ് അപ്പിലെ GitHub MCP സർവർ PAT-ഉം മാത്രം, അവ GitHub Models-നൊപ്പം ബന്ധപ്പെട്ടതല്ല).

### കുറിപ്പുകളും അറിയപ്പെട്ട പരിമിതികളും

- **നടത്തപ്പെട്ടിട്ടില്ല/കോമ്പൈൽ ചെയ്യപ്പെടാത്തവ.** API/നാമകരണം ശരിയാക്കൽക്കായി അപ്ഡേറ്റ് ചെയ്ത വിദ്യാഭ്യാസ സാമ്പിളുകൾ; സജീവ Azure സ്രോതസുകളോട് പരീക്ഷിച്ചിട്ടില്ല, .NET സാമ്പിളുകൾ ഈ പരിസരത്തിൽ കോമ്പൈൽ ചെയ്തിട്ടില്ല. നിങ്ങളുടെ സ്വന്തം Microsoft Foundry / Azure OpenAI ഡിസ്പ്ലോയ്മെന്റിനോട് താരതമ്യം ചെയ്യുക.
- **മോഡൽ ഡിപ്ലോയ്മെന്റ് Responses API നെ പിന്തുണയ്ക്കണം.** `gpt-4o-mini`, `gpt-4.1`, അല്ലെങ്കിൽ `gpt-5.x` മോഡലുകൾ പോലുള്ള ഡിപ്ലോയ്മെന്റ് ഉപയോഗിക്കുക. പഴയ മോഡലുകൾ Responses കോർ ഫീച്ചറുകളെ പിന്തുണയ്ക്കുന്നു, എന്നാൽ എല്ലാ ഫീച്ചറുകളും അല്ല.
- **Agent-framework വെർഷൻ.** സാമ്പിളുകൾ ഏറ്റവും പുതിയ MAF (`>=1.10.0`)-നെയാണ് ലക്ഷ്യമിടുന്നത്. കാനോണിക്കൽ ഏജന്റ് സൃഷ്ടി കോൾ `client.as_agent(...)`; APIകൾ ഫ്രെയിംവർക്ക് പ്രസിദ്ധീകരിച്ച ഡോക്യുമെന്റേഷനും ഇൻസ്റ്റാൾ ചെയ്ത ബിൽഡ്-ഉം മൂലം സ്ഥിരീകരിച്ചിട്ടുണ്ട്. വ്യത്യസ്ത വേർഷൻ പിന്‍മുന്നിൽ വയ്ക്കുമ്പോൾ, available method (`as_agent` vs `create_agent`) ഉറപ്പാക്കുക.
- **പാഠം 08 workflow നോട്ട് ബുക്ക് 04** ഉദ്ദേശപൂർവ്വം `AzureAIAgentClient` (from `agent-framework-azure-ai`) വച്ചിരിക്കുന്നു കാരണം Microsoft Foundry Agent Service ഹോസ്റ്റ് ചെയ്ത ടൂളുകൾ (Bing ഗ്രൗണ്ടിംഗ്, കോഡ് ഇൻടർപ്രിറ്റർ) ഉപയോഗിക്കുന്നു; ഇത് ഇതിനകം Responses അടിസ്ഥാനമായതാണ്.
- **.NET ഡിഫോൾട്ട് ഡിപ്ലോയ്മെന്റ്.** പാഠം 08 dotNET workflow സാമ്പിളുകൾ മുൻപ് `gpt-4o` ഹാർഡ് കോഡ്ചെയ്തിരുന്നു; ഇപ്പോൾ `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`) ആണ് ഡിഫോൾട്ട്. ഒരു സാമ്പിൾ മെറ്റമോഡല്‍/വിഷൻ ഇൻപുട്ട് ആശ്രയിച്ചുള്ളതാണ് എങ്കിൽ, `AZURE_OPENAI_DEPLOYMENT` യോജിച്ചതായി സജ്ജമാക്കുക.
- **Foundry Local** OpenAI അനുയോജ്യമായ **Chat Completions** എൻഡ്‌പോയിന്റ് തുറക്കുന്നു; പ്രാദേശിക ഡെവലപ്മെൻറിന് ഉദ്ദേശിച്ചതാണ്; Responses API-യുടെ മുഴുവൻ ഫീച്ചറുകൾക്കായി Azure OpenAI / Microsoft Foundry ഉപയോഗിക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->