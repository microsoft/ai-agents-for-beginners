---
name: azure-openai-to-responses
license: MIT
---
# Python ആപ്ലിക്കേഷനുകൾ Azure OpenAI ചാറ്റ് പൂർത്തീകരണങ്ങളിൽനിന്ന് Responses API-യ്ക്ക് മൈഗ്രേറ്റ് ചെയ്യുക

> **ഓതെന്റിക്കേറ്റഡ് മാർഗനിർദ്ദേശം — കൃത്യമായി പാലിക്കുക**
>
> ഈ സ്കിൽ Azure OpenAI ചാറ്റ് പൂർത്തീകരണങ്ങൾ ഉപയോക്തൃ Python കോഡ്‌ബേസുകൾ Responses API-യിലേക്ക് മൈഗ്രേറ്റ് ചെയ്യുന്നു.
> ഈ നിർദ്ദേശങ്ങൾ കൃത്യമായി പിന്തുടരുക.
> പാരാമീറ്റർ മാപ്പിങ്ങുകൾ സ്വന്തം നിലയിൽ നിർമിക്കേണ്ടതില്ല അല്ലെങ്കിൽ API ആകൃതികൾ കണ്ടെത്തേണ്ടതില്ല.

---

## ട്രിഗറുകൾ

ഉപയോക്താവ് താഴെപ്പറഞ്ഞതിൽ заинтересованы വച്ചാൽ ഈ സ്കിൽ സജീവമാക്കുക:
- Azure OpenAI ചാറ്റ് പൂർത്തീകരണങ്ങളിൽനിന്ന് Responses API-യിലേക്ക് Python ആപ്പ് മൈഗ്രേറ്റ് ചെയ്യുക
- Python OpenAI SDK ഉപയോഗം Azure OpenAI-യെതിരെ ഏറ്റവും പുതിയ API ആകൃതിയിലേക്ക് അപ്ഗ്രേഡ് ചെയ്യുക
- Responses ആവശ്യമായ GPT-5 അല്ലെങ്കിൽ പുതിയ മോഡലുകൾക്കായി Python കോഡ് തയ്യാറാക്കുക
- `AzureOpenAI`/`AsyncAzureOpenAI`-ഇൽനിന്ന് സ്റ്റാൻഡേർഡ് `OpenAI`/`AsyncOpenAI` ക്ലയന്റ് v1 എൻഡ്‌പോയിന്റിലേക്ക് മാറ്റുക
- `AzureOpenAI` കോൺസ്ട്രക്ടറുകൾക്കോ `api_version`-സംബന്ധിച്ച ഡിപ്രീക്കേഷൻ മുന്നറിയിപ്പുകൾ പരിഹരിക്കുക

---

## ⚠️ മോഡൽ സാദ്ധ്യത — ആദ്യം പരിശോധിക്കുക

> **മൈഗ്രേറ്റ് ചെയ്‌തുതുടങ്ങുന്നതിനു മുൻപ്, നിങ്ങളുടെ Azure OpenAI വിന്യാസം Responses API പിന്തുണയ്ക്കുന്നുണ്ടോ എന്ന് ഉറപ്പാക്കിയിരിക്കണം.**

### 1. നിങ്ങളുടെ വിന്യാസം വേഗത്തിൽ ടെസ്റ്റ് ചെയ്യുക (എത്രയും വേഗം)

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

> **കുറിപ്പ്**: Azure OpenAI-യിൽ `max_output_tokens`-ന് കുറഞ്ഞത് **16** ആണ്. 16-ലേയ്ക്ക് താഴെയുള്ള മൂല്യങ്ങൾ 400 പിശക് തിരികെ നൽകും. പുക പരീക്ഷണങ്ങൾക്ക് 50+ ഉപയോഗിക്കുക.

ഇത് 404 തിരികെ നൽകുകയാണെങ്കിൽ, വിന്യാസത്തിലെ മോഡൽ ഇപ്പോഴും Responses പിന്തുണക്കാതെ വരികയാണ് — താഴെ നൽകിയ റഫറൻസ് പരിശോധിക്കുകയോ പിന്തുണയുള്ള മോഡൽ ഉപയോഗിച്ച് വീണ്ടും വിന്യസിക്കുകയോ ചെയ്യുക.

### 2. നിങ്ങളുടെ പ്രദേശത്ത് ലഭ്യമായ മോഡലുകൾ പരിശോധിക്കുക (ശുപാർശ ചെയ്യുന്നു)

Responses API പിന്തുണയുള്ള നിങ്ങളുടെ പ്രത്യേക ഭാഗത്ത് ലഭ്യമായ മോഡലുകളെ കാണാൻ ഉൾപ്പെടുത്തിയ മോഡൽ സാദ്ധ്യത ഉപകരണം പ്രവർത്തിപ്പിക്കുക:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

ഇത് Azure ARM ലൈവിൽ ചോദ്യം ചെയ്തു ഒരു സാദ്ധ്യത മാട്രിക്സ് കാണിക്കുന്നു — ഏതു മോഡലുകൾ Responses, ഘടനാബദ്ധമായ output, ടൂളുകൾ തുടങ്ങിയവ പിന്തുണക്കുന്നതും. ഫിൽട്ടർ ചെയ്യാൻ `--filter gpt-5.1,gpt-5.2` ഉപയോഗിക്കുക അല്ലെങ്കിൽ സ്ക്രിപ്റ്റിംഗിനായി `--json` ഉപയോഗിക്കുക.

### 3. സമ്പൂർണ മോഡൽ പിന്തുണ റഫറൻസ്

- **ലൈവ് ചോദ്യം**: `python migrate.py models` (മുകളിൽ കാണിച്ചിരിക്കുന്നതാണ് — പ്രദേശം-നിർദിഷ്ടം, എപ്പോഴും അപ് ടു ഡേറ്റ്)
- **ലഭ്യത ബ്രൗസ് ചെയ്യുക**: [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **ക്വിക്സ്റ്റാർട്ട് & മാർഗനിർദ്ദേശം**: **https://aka.ms/openai/start**

### ⚠️ പഴയ മോഡൽ പരിധികൾ

> **മുന്നറിയിപ്പ്**: പഴയ മോഡലുകൾ (`gpt-4.1` മുമ്പുള്ളത്) Responses API എല്ലാ ഫീച്ചറുകളും പൂർണമായി പിന്തുണക്കാതെ വരിവച്ചേക്കാം.
>
> പഴയ മോഡലുകൾക്കുള്ള അറിയപ്പെട്ട പരിധികൾ:
> - **`reasoning` പാരാമീറ്റർ**: അനേകം reasoning-മില്ലാത്ത മോഡലുകളിൽ പിന്തുണയില്ല. മൈഗ്രേറ്റുചെയ്യുന്നത് മുൻകാല കോഡിൽ `reasoning` ഉണ്ടെങ്കിൽ മാത്രം.
> - **`seed` പാരാമീറ്റർ**: Responses API-ൽ എല്ലാവിധത്തിലും പിന്തുണയില്ല — എല്ലാതരം അപേക്ഷകളിൽ നിന്നും നീക്കംചെയ്യുക.
> - **ഘടനാബദ്ധമായ output `text.format` വഴി**: പഴയ മോഡലുകൾക്ക് `strict: true` JSON സ്കീമകൾ ഉറപ്പുവരുത്താൻ സാദ്ധ്യത ഇല്ല.
> - **ടൂൾ ഓർക്കസ്ട്രേഷൻ**: GPT-5+ തങ്ങളുടെ ആന്തരിക reasoning-ന്റെ ഭാഗമായി ടൂൾ കോൾസ് ഓർക്കസ്ട്രേറ്റ് ചെയ്യുന്നു. Responses-ൽ പഴയ മോഡലുകൾ ഇപ്പോഴും പ്രവർത്തിക്കുന്നു, പക്ഷേ ആഴത്തിലുള്ള ഈ സംയോജനം ഇല്ല.
> - **ടെംപറേച്ചർ നിയന്ത്രണങ്ങൾ**: `gpt-5`--ലേക്ക് മൈഗ്രേറ്റ് ചെയ്യുമ്പോൾ, ടെംപറേച്ചർ ഒഴിവാകേണ്ടതോളം അല്ലെങ്കിൽ `1` ആകണം. പഴയ മോഡലുകൾക്ക് ഇത്തരം നിയന്ത്രണം ഇല്ല.

### ഒ-സീരിസ reasoning മോഡലുകൾ (o1, o3-mini, o3, o4-mini)

ഒ-സീരിസ മോഡലുകൾക്ക് അനുപാതമായ പാരാമീറ്റർ നിയന്ത്രണങ്ങൾ ഉണ്ട്. ഒ-സീരിസ മോഡലുകൾ ലക്ഷ്യമാക്കി ആപ്പുകൾ മൈഗ്രേറ്റ് ചെയ്യുമ്പോൾ:

- **`temperature`**: `1` ആകണം (അല്ലെങ്കിൽ ഒഴിവാക്കാം). ഒ-സീരിസ മോഡലുകൾ മറ്റെവിടത്തും വിലകളെ സ്വീകരിച്ചുകൊള്ളില്ല.
- **`max_completion_tokens` → `max_output_tokens`**: Azure-സ്വതന്ത്രമായ `max_completion_tokens` ഉപയോഗിക്കുന്ന ആപ്പുകൾ `max_output_tokens`-നായി മാറണം. reasoning ടോക്കണുകൾ പരിധിക്കു എതിരെ എണ്ണപ്പെടുന്നതിനാൽ വലിയ മൂല്യങ്ങൾ (4096+) സജ്ജമാക്കുക.
- **`reasoning_effort`**: ആപ്പ് `reasoning_effort` (low/medium/high) ഉപയോഗിച്ചാൽ അത് സൂക്ഷിക്കുക — Responses API ഒ-സീരിസ മോഡലുകൾക്കുള്ള ഈ പാരാമീറ്റർ പിന്തുണയ്ക്കുന്നു.
- **സ്റ്റ്രീമിംഗ് പെരുമാറ്റം**: ഒ-സീരിസ മോഡലുകൾ reasoning പൂർത്തിയാകുന്നത് വരെ ഔട്ട്‌പുട്ട് ബഫർ ചെയ്ത് പിന്നീട് ടെക്സ്റ്റ് ഡെൽറ്റ ഇവന്റുകൾ സൃഷ്ടിക്കാം. സ്റ്റ്രീമിംഗ് ഇപ്പോഴും പ്രവർത്തിക്കുകയായിരുന്നില്ലെങ്കിലും ആദ്യം വരുന്ന `response.output_text.delta` GPT മോഡലുകളേക്കാൾ കുറച്ച് വൈകാൻ സാധ്യതയുണ്ട്.
- **`top_p`**: ഒ-സീരിസിൽ പിന്തുണയില്ല — ഉണ്ടായിരുന്നെങ്കിൽ നീക്കം ചെയ്യുക.
- **ടൂൾ ഉപയോഗം**: ഒ-സീരിസ മോഡലുകൾ Responses API വഴി ടൂളുകൾ പിന്തുണയ്ക്കുന്നു, ജിപിടി മോഡലുകൾ പോലെ, പക്ഷേ ടൂൾ കോൾ ഓർക്കസ്ട്രേഷൻ ഗുണനിലവാരം മോഡൽ അനുസരിച്ച് വ്യത്യാസപ്പെടും.

**പ്രവർത്തനം — മുൻകരുതൽ മോഡൽ ഉപദേശം**: സ്കാൻ ഘട്ടത്തിൽ, ആപ്പ് ഏതൊരു മോഡലിനെ ലക്ഷ്യമാക്കിയിട്ടുണ്ട് (വിന്യാസ നാമങ്ങൾ, പരിസ്ഥിതി വ്യത്യാസങ്ങൾ, കോൺഫിഗ്) എങ്കിൽ പരിശോധിക്കുക. മോഡൽ `gpt-4.1`-നെക്കാൾ പഴക്കമുള്ളതാണ് (gpt-4.1+ അല്ല), ഉപയോക്താവിനെ മുൻകൂട്ടി അറിയിക്കുക:
- അടിസ്ഥാന തരം ടെക്സ്‌റ്റ്, ചാറ്റ്, സ്റ്റ്രീമിംഗ്, ടൂളുകൾ അവരുടെ നിലവിലെ മോഡലിൽ മൈഗ്രേറ്റ് പ്രവർത്തിക്കും.
- പുതിയ മോഡലുകൾ (`gpt-5.1`, `gpt-5.2`) മെച്ചപ്പെട്ട ടൂൾ ഓർക്കസ്ട്രേഷൻ, ഘടനാബദ്ധമായ output ഉറപ്പാക്കൽ, reasoning, എന്നിവയും പ്രദേശാന്തര ലഭ്യതയും ഉണ്ട്.
- അവർ തയ്യാറായപ്പോൾ വിന്യാസം അപ്ഗ്രേഡ് ചെയ്യുന്നത് പരിഗണിക്കണം — മൈഗ്രേഷനിൽ തടസ്സം അല്ല.

മോഡൽ പതിപ്പിനെ അടിസ്ഥാനപ്പെടുത്തി മൈഗ്രേറ്റ് ചെയ്യുന്നത് തടയുകയോ നിഷേധിക്കുകയോ വേണ്ടതല്ല. ഒരു വിവരോപദേശം മാത്രമാണ്.

### GitHub മോഡലുകൾ Responses API-യെ പിന്തുണയ്ക്കുന്നില്ല

> **GitHub മോഡലുകൾ (`models.github.ai`, `models.inference.ai.azure.com`) Responses API-യെ പിന്തുണയ്ക്കുന്നില്ല.**

കോഡ്‌ബേസിൽ GitHub മോഡൽ കോഡ് പാതയുണ്ടെങ്കിൽ (`base_url` `models.github.ai` അല്ലെങ്കിൽ `models.inference.ai.azure.com`-ലേക്ക് പോയിരിക്കുന്നു എന്ന് പരിശോധിക്കുക), മൈഗ്രേഷനിൽ അത് **പൂർണ്ണമായും നീക്കുക**. Responses API-ക്ക് Azure OpenAI, OpenAI, അല്ലെങ്കിൽ അനുകൂലമായ ലോക്കൽ എൻഡ്‌പോയിന്റ് (ഉദാ: Ollama Responses പിന്തുണയോടെ) വേണം.

സ്കാൻ ഘട്ടത്തിൽ പ്രവർത്തനം:
- GitHub മോഡൽ കോഡ് പാതകൾ നീക്കാൻ ഫ്ലാഗ് ചെയ്യുക.

---

## ഫ്രെയിംവർക്ക് മൈഗ്രേഷൻ

പല ആപ്പുകളും OpenAIയ്ക്ക് മുകളിലുള്ള ഉയർന്ന നിലയിലെ ട്രെയ്ഡ് ഫ്രെയിംവർക്കുകൾ ഉപയോഗിക്കുന്നു. ഇത് മൈഗ്രേറ്റ് ചെയ്യുമ്പോൾ ഫ്രെയിംവർക്കിലെ സ്വന്തം API മാറ്റങ്ങൾ വരും — വെറും അടിത്തറ OpenAI വിളികളിൽ മാറ്റമല്ല.

### Microsoft Agent Framework (MAF)

**നിങ്ങളുടെ MAF പതിപ്പ് ആദ്യം പരിശോധിക്കുക** — മൈഗ്രേഷൻ MAF 1.0.0+ ആണ് എന്നോ മുൻ 1.0.0 ബീറ്റ/ആർസി പതിപ്പ് ആണ് എന്നോ ആശ്രയിച്ചിരിക്കുന്നു.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ഇപ്പോഴേതും Responses API ഉപയോഗിക്കുന്നു** — മൈഗ്രേഷൻ ആവശ്യമില്ല. ലെഗസി `OpenAIChatCompletionClient` (ഉപയോഗിക്കുന്നത് `chat.completions.create`) ഉപയോഗിക്കുകയാണെങ്കിൽ, അത് `OpenAIChatClient` ആയി മാറ്റുക.

| മുമ്പ് | പിന്നെ |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

പതിപ്പ് പരിശോധിക്കാൻ: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`  

#### MAF മുൻ 1.0.0 (ബീറ്റ/ആർസി റിലീസുകൾ)

മുൻ 1.0.0 MAF-ൽ `OpenAIChatClient` ചാറ്റ് പൂർത്തീകരണങ്ങൾ ഉപയോഗിച്ചിരുന്നു. `agent-framework-openai>=1.0.0`-ൽ അപ്ഗ്രേഡ് ചെയ്യുക, ഇവിടെ `OpenAIChatClient` Responses API ഡീഫോൾട്ടായി ഉപയോഗിക്കുന്നു.

മറ്റു മാറ്റങ്ങൾ ആവശ്യമില്ല — `Agent` ടൂൾ APIകൾ ഒരുപോലെ തുടരും.

### LangChain (`langchain-openai`)

`ChatOpenAI()`-ക്ക് `use_responses_api=True` ചേർക്കുക. കൂടാതെ `.content` ൽ നിന്നുള്ള അവശന പ്രാപനം `.text` ആയി അപ്ഡേറ്റ് ചെയ്യുക.

| മുമ്പ് | പിന്നെ |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

പൂര്‍ണ്ണമായി ശേഷിക്കുന്ന മുന്‍-പിന്നണി കോഡ് ഉദാഹരണങ്ങള്‍ക്കായി [cheat-sheet.md](./references/cheat-sheet.md) കാണുക.

---

## ഫ്രണ്ട്‌എൻഡ് മൈഗ്രേഷൻ മാർഗനിർദ്ദേശം

> **Responses API ഒരു സെർവർ-സൈഡ് വിഷയം ആണ്.** നിങ്ങളുടെ Python ബാക്ക്‌എൻഡ് മൈഗ്രേറ്റ് ചെയ്യുക; ഫ്രണ്ട്‌എൻഡ് HTTP കരാറ് മാറ്റേണ്ടതില്ല, നിങ്ങളുടെ ബാക്ക്‌എൻഡ് ഒരു സുതാര്യ പാസ്സും അല്ലെങ്കിൽ — അെങ്കിലും Responses അഭ്യർത്ഥന ആകൃതി സ്വീകരിക്കാൻ പരിഗണിക്കുക, ഇത് പരിഭാഷപ്പെടുത്തൽ ഘട്ടം ഒഴിവാക്കും. ഫ്രണ്ട്‌എൻഡ് നേരിട്ട് OpenAI-യെ ക്ലയന്റ്-സൈഡ് കീ ഉപയോഗിച്ച് വിളിക്കുകയാണെങ്കിൽ, ആ വിളികൾ ആദ്യം ബാക്ക്‌എൻഡിലേക്ക് മാറ്റുക.

### `@microsoft/ai-chat-protocol` നിഷേധപ്പെടുത്തൽ

`@microsoft/ai-chat-protocol` npm പാക്കേജ് നിഷേധിക്കപ്പെട്ടു, അത് [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) ഉപയോഗിച്ച് മാറ്റുക. ഫ്രണ്ട്‌എൻഡിൽ ഇത് കണ്ടാൽ:

1. CDN സ്‌ക്രിപ്റ്റ് ടാഗ് മാറ്റുക:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` ഉൽപ്പത്തി നീക്കുക (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. `client.getStreamedCompletion(messages)`-നെ നേരിട്ട് ബാക്ക്‌എൻഡ് സ്‌ട്രിമിംഗ് എൻഡ്‌പോയിന്റിലേക്ക് `fetch()` വിളിയിലേക്ക് മാറ്റുക.
4. `for await (const response of result)`-നെ `for await (const chunk of readNDJSONStream(response.body))` ആയി മാറ്റുക.
5. പ്രോപ്പർട്ടി പ്രാപനം `response.delta.content` / `response.error`-ൽ നിന്ന് `chunk.delta.content` / `chunk.error` ആയി മാറ്റുക.

---

## ലക്ഷ്യങ്ങൾ

- Azure OpenAIയ്ക്ക് എതിരെ Chat Completions അല്ലെങ്കിൽ ലെഗസി Completions ഉപയോഗിക്കുന്ന Python കോൾ സൈറ്റുകൾ എണ്ണുക.
- Python കോഡ്‌ബേസിനായി ഒരു മൈഗ്രേഷൻ പദ്ധതി നിർദ്ദേശിക്കുകയും പടികളായി നിർദ്ദേശിക്കുകയും ചെയ്യുക.
- Responses API-യിലേക്ക് മാറുന്നതിന് സുരക്ഷിതവും കുറഞ്ഞ മാറ്റങ്ങളും നിർവഹിക്കുക.
- Responses output സ്കീമ ഉപയോഗിച്ച് കോൾ ചെയ്തവർ അപ്ഡേറ്റ് ചെയ്യുക; പാശ്വസാന്ഗീക വെറുപ്പുകൾ ഇല്ല.
- ടെസ്റ്റുകളും ലിന്റുകളും നടത്തുക; മൈഗ്രേഷൻ കൊണ്ടുവരുന്ന ലഘുവായ പിശകുകൾ പരിഹരിക്കുക.
- ചെറിയ, അവലോകനയോഗ്യമായ മാറ്റ സെറ്റുകൾ തയ്യാറാക്കുക; ഡിഫുകൾ സഹിതം അവസാന സംഗ്രഹം നൽകുക (കമ്മിറ്റ് ചെയ്യേണ്ടതില്ല).

---

## ഗാർഡ്റെയിൽസ്

- ഗിറ്റ് വർക്ക്‌സ്‌പേസിനുള്ളിലുള്ള ഫയലുകൾ മാത്രമേ മാറ്റുക. പുറത്തുപോവാതെ എഴുതരുത്.
- പാശ്വസാന്ഗീകമായ ഷിംമുകൾ സൂക്ഷിക്കേണ്ടതില്ല; പുതിയ API ആകൃതിയിലേക്ക് കോഡ് മാറ്റുക.
- ടോംബ്‌സ്റ്റോൺ/ട്രാൻസിഷൻ കമന്റുകളും ബാക്കപ്പ് ഫയലുകളും ഒഴിവാക്കുക.
- മുമ്പ് ഉപയോഗിച്ചത് പോലെ സ്റ്റ്രീമിംഗ് സെമാന്റിക്സ് സൂക്ഷിക്കുക; അല്ലെങ്കിൽ സ്റ്റ്രീം ചെയ്യാത്ത രീതിയിലാക്കുക.
- അനുമതി മോഡിൽ നിന്ന് കമാൻഡുകൾ അല്ലെങ്കിൽ നെറ്റ്‌വർക്ക് കോൾ നടത്താൻ മുൻകൂർ അംഗീകാരം ചോദിക്കുക.
- `git add`/`git commit`/`git push` چلക്കുക; പ്രവർത്തന നിലക്കാരനെ മാത്രമേ ഉൽപ്പത്തി ചെയ്യരുത്.

---

## ഘട്ടം 0: Azure OpenAI ക്ലയന്റ് മൈഗ്രേഷൻ ( മുൻ‌ഷര്ിയ )

കോഡ്‌ബേസിൽ `AzureOpenAI` അല്ലെങ്കിൽ `AsyncAzureOpenAI` കോൺസ്ട്രക്ടറുകൾ ഉപയോഗിക്കുന്നുവെങ്കിൽ, ആദ്യം സ്റ്റാൻഡേർഡ് `OpenAI` / `AsyncOpenAI` കോൺസ്ട്രക്ടറുകളിലേക്ക് മൈഗ്രേറ്റ് ചെയ്യുക. Azure-സ്വതന്ത്ര കോൺസ്ട്രക്ടറുകൾ `openai>=1.108.1`-ൽ ഡിപ്രീക്കേറ്റ് ചെയ്തു.

### എത്രയോ വലിയ v1 API പാത എന്തുകൊണ്ടാണ്?

പുതിയ `/openai/v1` എൻഡ്‌പോയിന്റ് `AzureOpenAI()`-ന്റെ പകരം സ്റ്റാൻഡേർഡ് `OpenAI()` ക്ലയന്റ് ഉപയോഗിക്കുന്നു, `api_version` പാരാമീറ്റർ വേണ്ടാതെയിരിക്കുന്നു, OpenAI-യും Azure OpenAI-യും ഒരുപോലെ പ്രവർത്തിക്കുന്നു. ഒരേ ക്ലയന്റ് കോഡ് ഭാവിയിൽ എല്ലാ പതിപ്പിലും പ്രവർത്തിക്കും — വേർഷൻ മാനേജ്മെന്റ് ആവശ്യമില്ല.

### പ്രധാന മാറ്റങ്ങൾ

| മുമ്പ് | പിന്നെ |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | പൂർണ്ണമായും നീക്കംചെയ്യുക |

### ശുചീകരണ ചെക്ക്ലിസ്റ്റ്

- ക്ലയന്റ് നിർമ്മാണത്തിൽ നിന്നും `api_version` പാരാമീറ്റർ നീക്കം ചെയ്യുക.
- `.env`, ആപ്പ് സജ്ജീകരണങ്ങൾ, Bicep/ഇൻഫ്ര ഫയലുകളിൽ നിന്നും `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` പരിസ്ഥിതി വ്യത്യാസങ്ങൾ നീക്കം ചെയ്യുക.
- `.env`, ആപ്പ് സജ്ജീകരണങ്ങൾ, Bicep/ഇൻഫ്ര, ടെസ്റ്റ് ഫിക്സ്ചറുകളിൽ `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` എന്നാക്കി പേരുമാറ്റം നടത്തുക (സ്റ്റാൻഡേർഡ് Azure Identity SDK കൺവെൻഷൻ).
- `openai>=1.108.1` `requirements.txt` അല്ലെങ്കിൽ `pyproject.toml`-ൽ ഉറപ്പാക്കുക.

### പരിസ്ഥിതി വ്യത്യാസം മൈഗ്രേഷൻ

| പഴയ env var | നടപടി | കുറിപ്പുകൾ |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **നീക്കംചെയ്യുക** | v1 എൻഡ്‌പോയിന്റിൽ `api_version` ആവശ്യമില്ല |
| `AZURE_OPENAI_API_VERSION` | **നീക്കംചെയ്യുക** | മുകളിലുള്ളതുപോലെ |
| `AZURE_OPENAI_CLIENT_ID` | **പേരുമാറ്റം** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)`-നുള്ള സ്റ്റാൻഡേർഡ് Azure Identity SDK കൺവെൻഷൻ |
| `AZURE_OPENAI_ENDPOINT` | **തനിക്കാവശ്യമാണ്** | ഇപ്പോഴും `base_url` നിർമ്മാണത്തിന് ആവശ്യം |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **തനിക്കാവശ്യമാണ്** | `responses.create`-ൽ `model` പാരാമീറ്ററായി ഉപയോഗിക്കുന്നു |
| `AZURE_OPENAI_API_KEY` | **തനിക്കാവശ്യമാണ്** | കീ അടിസ്ഥാനAuth-ഇക്കായി `api_key` ആയി ഉപയോഗിക്കുന്നു |

ക്ലയന്റ് സെറ്റ്‌അപ്പ് കോഡ് ഉദാഹരണങ്ങൾക്കായി (സിങ്ക്, അസിങ്ക്, EntraID, API കീ, മൾട്ടി-ടെനന്റ്) [cheat-sheet.md](./references/cheat-sheet.md) കാണുക.

---

## ഘട്ടം 1: ലെഗസി കോൾ സൈറ്റുകൾ കണ്ടെത്തുക

[detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) സ്ക്രിപ്റ്റ് പ്രവർത്തിപ്പിച്ച് മൈഗ്രേഷൻ ആവശ്യമായ എല്ലാ കോൾ സൈറ്റുകളും കണ്ടെത്തുക:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

അല്ലെങ്കിൽ താഴെപ്പറയുന്ന തിരച്ചിലുകൾ دستیമായി നടത്തുക — ഓരോ പൊരുത്തവും മൈഗ്രേഷൻ ലക്ഷ്യം:

```bash
# ലെഗസി API കോൾസുകൾ (പുതിയതായി എഴുതണം)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# പഴയ ആസ്യൂർ ക്ലയന്റ് കന്സ്ട്രക്ടേഴ്സ് (മാറ്റേണ്ടത്)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# റസ്പോൺസ് ഷേപ്പ് ആക്‌സസ് സാങ്കേതികവഴികൾ (പുതുക്കണം)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# പഴയ നെസ്റ്റഡ് ഫോർമാറ്റിലുള്ള ടൂൾ നിർവചനങ്ങൾ (സാരമാക്കണം)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# പഴയ ഫോർമാറ്റിലുള്ള ടൂൾ ഫലങ്ങൾ (function_call_output ആക്കി മാറ്റണം)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# പഴങ്കാല പാരാമീറ്ററുകൾ (ഒഴിവാക്കണം അല്ലെങ്കിൽ പുനർനാമകരണം വേണം)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens എന്ന് പുനർനാമകരണം ചെയ്യുക
rg "['\"]seed['\"]"      # remove entirely

# പഴങ്കാല എന്‍വി വേരി (ശുദ്ധീകരണം)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID ആകണം

# GitHub മോഡൽ എൻഡ്‌പോയിന്റ്‌സ് (ഒഴിവാക്കണം — Responses API പിന്തുണയില്ല)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# ഫ്രെയിംവർക്ക് തലത്തിലുള്ള ലെഗസി സാങ്കേതികവഴികൾ (പുതുക്കണം)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient ആയി മാറ്റുക
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True ആവശ്യം

# ടെസ്റ്റ് അടിസ്ഥാനഘടന (പുതുക്കണം)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# ഉള്ളടക്ക ഫിൽട്ടർ പിശക് ബോഡി ആക്‌സസ് (പുതുക്കണം — ഘടന മാറി)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # പഴയ ഏകവചന രൂപം — ഇപ്പോൾ content_filter_results (ബഹുവചനം) content_filters ആറിയിൽ ഉൾപ്പെടും

# Chat Completions എൻഡ്‌പോയിന്റിലേക്ക് Raw HTTP കോൾസ് (URL പുതുക്കണം)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### ഹ്യൂറിസ്റ്റിക്കുകൾ (കണ്ടെടുത്ത് പുനഃരൂപപ്പെടുത്തുക)

- **ചാറ്റ് പൂർത്തീകരണ ക്ലയന്റ്**: `client.chat.completions.create` → `client.responses.create(...)`.

- **അസ്യൂർ ക്ലയന്റ് കൺസ്ട്രക്ടറുകൾ**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **ടൂളുകൾ**: ഫംഗ്ഷൻ-കോൾ ചെയ്യുന്ന ടൂൾ നിർവചനങ്ങൾ നസ്‌തികളായ ഫോർമാറ്റിൽ നിന്ന് (`{"type": "function", "function": {"name": ...}}`) ഫ്‌ളാറ്റ് Responses ഫോർമാറ്റിലേക്ക് (`{"type": "function", "name": ...}`) പരിവർത്തനം ചെയ്യുക; `tool_choice` ഉപയോഗിക്കുക; ടൂൾ ഫലങ്ങൾ `{"type": "function_call_output", "call_id": ..., "output": ...}` ഇനങ്ങളായി തിരിച്ചയയ്ക്കുക (`{"role": "tool", ...}` അല്ല).
- **ടൂൾ റൗണ്ട്-ട്രിപ്പ്**: മോഡൽ ഫംഗ്ഷൻ കോൾ തിരിച്ച് നൽകുമ്പോൾ, സംഭാഷണത്തിനായി `response.output` ഇനങ്ങൾ ചേർക്കുക (മാനുവൽ `{"role": "assistant", "tool_calls": [...]}` ഡിക്റ്റ് ഇല്ല), ശേഷം ഓരോ ഫലത്തിനും `function_call_output` ഇനങ്ങൾ ചേർക്കുക.
- **ഫ്യൂ-ഷോട്ട് ടൂൾ ഉദാഹരണങ്ങൾ**: സംഭാഷണത്തിൽ ഹാർഡ്‌കോഡുചെയ്ത ടൂൾ കോൾ ഉദാഹരണങ്ങൾ ഉണ്ടെങ്കിൽ അവ `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` ഇനങ്ങളാക്കി മാറ്റുക. ഐഡികൾ `fc_` നാല് തുടക്കം വയ്ക്കണം.
- **`pydantic_function_tool()`**: ഈ ഹെൽപ്പർ ഇപ്പോഴും പഴയ നസ്റ്റെഡ് ഫോർമാറ്റ് സൃഷ്ടിക്കുന്നതിനാൽ `responses.create()` യുമായി **അന്വയം ഇല്ല**. മാനുവൽ ടൂൾ നിർവചനങ്ങളോ ഫ്‌ളാറ്റനിങ്ങ് റാപ്പറോ ഉപയോഗിക്കുക.
- **മൾട്ടി-ടേൺ**: ആപ്പിൽ സംഭാഷണ ചരിത്രം സൂക്ഷിക്കുക; മുൻ ടേൺ `input` ഇനങ്ങൾ വഴി പാസ്സ് ചെയ്യുക.
- **ഫോർമാറ്റിംഗ്**: ചാറ്റിന്റെ ടോപ്പ്-ലെവൽ `response_format` Responses ൽ `text.format` ആയി മാറ്റുക. കാനോണിക്കൽ രൂപം: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **ഉള്ളടക്ക ഇനങ്ങൾ**: ചാറ്റ് `content[].type: "text"` Responses ൽ `content[].type: "input_text"` ആക്കി മാറ്റുക (ഉപയോക്താവ്/സിസ്റ്റം ടേണുകൾക്കായി).
- **ഇമേജ് ഉള്ളടക്കം ഇനങ്ങൾ**: ചാറ്റ് `content[].type: "image_url"` Responses ൽ `content[].type: "input_image"` ആക്കി മാറ്റുക. `image_url` ഫീൽഡ് നസ്റ്റെഡ് ഒബ്‌ജക്റ്റ് `{"url": "..."}` നിന്ന് ഫ്‌ളാറ്റ് സ്ട്രിങ്ങാക്കി മാറ്റുന്നു. മുൻപ്/ശേഷം ഉദാഹരണങ്ങൾക്ക് ചീറ്റ്ഷീറ്റ് കാണുക.
- **റീസണിംഗ് ശ്രമം**: **മൂല കോഡിൽ ഇതിനകം `reasoning` ഉണ്ടെങ്കിൽ മാത്രം മൈഗ്രേറ്റ് ചെയ്യുക**.
- **ഉള്ളടക്ക ഫിൽട്ടർ പിശക് കൈകാര്യം**: പിശക് ബോഡി ഘടന മാറി. ചാറ്റ് കോംപ്ലിഷൻസ് ഒരു ഏകമായ `error.body["innererror"]["content_filter_result"]` ഉപയോഗിച്ചിരുന്നപ്പോൾ; Responses API ൽ `error.body["content_filters"][0]["content_filter_results"]` (പലവുമുള്ള, ഒരു അറേയിലുള്ളത്) ആയി മാറി. `innererror` ആക്സസ് ചെയ്യുന്ന കോഡ് `KeyError` ഉയർത്തും. പുതിയ പാത്ത് ഉപയോഗിച്ച് പുനഃരചിക്കുക.
- **റോ ഹ്ട്ട്പ് കോൾസ്**: ആപ്പ് എഴുതി നേരിട്ടു അസ്യൂർ OpenAI REST API ഉപയോഗിക്കുകയെങ്കിൽ (`requests`, `httpx` മുതലായവ വഴി) `/openai/deployments/{name}/chat/completions?api-version=...` നിന്ന് `/openai/v1/responses` ആയി മാറ്റുക. റിക്വസ്റ്റ് ബോഡി മാറുന്നു: `messages` → `input`, `max_output_tokens` ചേർക്കുക, `store: false` ചേർക്കുക, `api-version` ക്വയറി പാറാം നീക്കുക. റെസ്പോൺസ് ബോഡി മാറുന്നു: `choices[0].message.content` → `output[0].content[0].text` (കുറിപ്പ്: `output_text` SDK സാന്ദ്രതയുടെ പ്രോപർട്ടി, റോ REST JSON-ൽ ഇല്ല).

---

## ഘട്ടം 2: മൈഗ്രേഷൻ പ്രയോഗിക്കുക

### മൈഗ്രേഷൻ കുറിപ്പുകൾ (ചാറ്റ് കോംപ്ലിഷൻസ് →_RESPONSES_)

- **എന്തുകൊണ്ട് മൈഗ്രേറ്റ് ചെയ്യണം**: ടെക്സ്‌റ്റ്, ടൂളുകൾ, സ്റ്റ്രീമിംഗ് എന്നിവയ്ക്കുള്ള ഏകീകൃത API ആണ് Responses; ചാറ്റ് കോംപ്ലിഷൻസ് പഴയതാണ്. GPT-5-ന് മികച്ച പ്രകടനത്തിന് Responses അനിവാര്യമാണ്.
- **HTTP**: അസ്യൂർ എന്റ്പോയിന്റ് `/openai/deployments/{name}/chat/completions` നിന്ന് `/openai/v1/responses` ആയി മാറുന്നു.
- **ഫീൽഡുകൾ**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` മാറ്റമില്ല.
- **ഫോർമാറ്റിംഗ്**: `response_format` → `text.format` ഒരു ശരിയായ ഒബ്ജക്റ്റ് ആയി.
- **ഉള്ളടക്ക ഇനങ്ങൾ**: ചാറ്റ് `content[].type: "text"` Responses ൽ `content[].type: "input_text"` ആക്കി മാറ്റുക (സിസ്റ്റം/ഉപയോക്താവ് ടേണുകൾക്ക്).
- **ഇമേജ് ഉള്ളടക്ക ഇനങ്ങൾ**: ചാറ്റ് `content[].type: "image_url"` Responses ൽ `content[].type: "input_image"` ആക്കി മാറ്റുക. `image_url` ഫീൽഡ് ഡാറ്റാ ഫ്രോം `{"image_url": {"url": "..."}}` → `{"image_url": "..."}` (സാധാരണ സ്ട്രിംഗ് — HTTPS URL അല്ലെങ്കിൽ `data:image/...;base64,...` ഡാറ്റാ യു ആർ ഐ).

### പാരാമീറ്റർ മാപ്പിംഗ് റഫറൻസ്

| ചാറ്റ് കോംപ്ലിഷൻസ് | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (ഇനങ്ങളുടെ അറേ) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (ഒബ്ജക്റ്റ്) |
| `temperature` | `temperature` (മാറാതെ) |
| `stop` | `stop` (മാറാതെ) |
| `frequency_penalty` | `frequency_penalty` (മാറാതെ) |
| `presence_penalty` | `presence_penalty` (മാറാതെ) |
| `tools` / function-calling | `tools` (മാറാതെ) |
| `seed` | **നീക്കം ചെയ്യുക** (സഹായിക്കുന്നില്ല) |
| `store` | `store` ( `false` ആക്കി സജ്ജമാക്കി) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ഫ്‌ളാറ്റ് സ്ട്രിംഗ്) |

പൂര്‍ണ്ണമായ മുന്‍നെതിരെ കോഡ് ഉദാഹരണങ്ങള്‍ക്ക്, [cheat-sheet.md](./references/cheat-sheet.md) കാണുക.

ടെസ്റ്റ് ഇൻഫ്രാസ്ട്രക്ചർ മൈഗ്രേഷനു (മോക്സ്, സ്നാപ്ഷോട്ടുകൾ, അസർ‌ഷനുകൾ), [test-migration.md](./references/test-migration.md) കാണുക.

പിശകുകൾ, ഗോട്ട്‌ചാസ് എന്നിവക്കുള്ള പ്രശ്നപരിഹാരത്തിന് [troubleshooting.md](./references/troubleshooting.md) കാണുക.

---

## ഡാറ്റ സംരക്ഷണം & സ്ഥിതി

- മുഴുവൻ Responses അഭ്യർത്ഥനകളിലും `store: false` സജ്ജമാക്കുക.
- മുൻ സന്ദേശ ഐഡികളിലും സെർവർ സൂക്ഷിക്കുന്ന സാഹചര്യത്തിലും ആശ്രയിക്കരുത്; സ്ഥിതി ക്ലയന്റ് നിയന്ത്രിക്കുന്നതായിരിക്കണം, മेटാഡേറ്റ കുറയ്ക്കുക.

---

## സ്വീകരണ മാനദണ്ഡങ്ങൾ

### കോഡ് തലത്തിലെ ഗേറ്റുകൾ (എല്ലാം കടന്നു പോകണം)

- [ ] മൈഗ്രേറ്റുചെയ്‌ത ഫയലുകളിൽ `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` സീറോ പൊരുത്തങ്ങൾ.
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` സീറോ പൊരുത്തങ്ങൾ — എല്ലാ കണ്‍സ്ട്രക്ടറുകളും `OpenAI`/`AsyncOpenAI` v1 എന്റ്പോയിന്റ് ഉപയോഗിക്കുന്നു.
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` സീറോ പൊരുത്തങ്ങൾ — GitHub മോഡൽ കോഡ് പാതകൾ നീക്കം ചെയ്തു.
- [ ] `rg "OpenAIChatCompletionClient"` സീറോ പൊരുത്തങ്ങൾ — MAF 1.0.0+ കോഡ് `OpenAIChatClient` (Responses API ഉപയോഗിക്കുന്നു) ആണ്. 1.0.0 മുന്‍പ്, `agent-framework-openai>=1.0.0` അപ്ഡേറ്റ് ചെയ്യുക.
- [ ] എല്ലാ `ChatOpenAI(...)` കോളുകളിലും `use_responses_api=True` ഉണ്ടാകണം.
- [ ] `rg "choices\[0\]"` സീറോ പൊരുത്തങ്ങൾ — എല്ലാം റെസ്പോൺസ് ആക്സസ് `resp.output_text` അല്ലെങ്കിൽ Responses ഔട്ട്‌പുട്ട് സ്കീമ ഉപയോഗിക്കുന്നു.
- [ ] ടോപ്പ് ലെവലിലെ `response_format` ഇല്ല; എല്ലാ ഘടനാപരമായ ഔട്ട്‌പുട്ട് `text={"format": {...}}` ഉപയോഗിക്കുന്നു.
- [ ] `openai>=1.108.1` കൂടാതെ `azure-identity` `requirements.txt` അല്ലെങ്കിൽ `pyproject.toml` ൽ; ഡിപെൻഡൻസികൾ പുനഃസ്ഥാപിച്ചു.
- [ ] എല്ലാ `responses.create` കോളുകളിലും `store=False` സജ്ജമാക്കി.
- [ ] ക്ലയന്റ് കൺസ്ട്രക്ഷനിൽ `api_version` ഇല്ല; `AZURE_OPENAI_API_VERSION` എൻവിർ ഫയലുകളിലും ഇൻഫ്രാസ്ട്രക്ചർ നിന്ന് നീക്കംചെയ്തു.

### ടെസ്റ്റ് ഇൻഫ്രാസ്ട്രക്ചർ ഗേറ്റുകൾ (എല്ലാം കടന്നു പോകണം)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` സീറോ പൊരുത്തങ്ങൾ.
- [ ] `rg "_azure_ad_token_provider" tests/` സീറോ പൊരുത്തങ്ങൾ — അസർ‌ഷനുകൾ अद्यतनപ്പെടുത്തി `isinstance(client, AsyncOpenAI)` അല്ലെങ്കിൽ `base_url` പരിശോധിക്കുക.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` സീറോ പൊരുത്തങ്ങൾ — അസ്യൂർ-നിർദ്ദിഷ്ട ഫിൽട്ടർ മോക്സ് നീക്കംചെയ്തു.
- [ ] മോക് ഫിക്ഷറുകൾ `kwargs.get("input")` ഉപയോഗിക്കുന്നു, `kwargs.get("messages")` അല്ല.
- [ ] സ്നാപ്ഷോട്ട് / ഗോൾഡൻ ഫയലുകൾ Responses സ്റ്റ്രീമിംഗ് രൂപത്തിലേക്ക് പുതുക്കിയത് ( `choices[0]`, `function_call`, `logprobs` ഇല്ല).
- [ ] എല്ലാ ടെസ്റ്റ് അപ്‌ഡേറ്റുകൾ കഴിഞ്ഞ് `pytest` പാസ്സ് കൂടാതെ വീഴ്ചകള്‍ ഒന്നും ഇല്ല.

### പെരുമാറ്റ ഗേറ്റുകൾ (അന്വേഷണം കൈകാര്യം ചെയ്യുക അല്ലെങ്കിൽ ടെസ്റ്റ് ഹാർനെസ് വഴി)

- [ ] **അടിസ്ഥാനഅവസാനം**: നോൺ-സ്റ്റ്രീമിംഗ് `responses.create` ശൂന്യമല്ലാത്ത `output_text` റിട്ടേൺ ചെയ്യണം.
- [ ] **സ്റ്റ്രീം പാരിറ്റി**: ഒറിജിനൽ കോഡ് streaming ഉപയോഗിച്ചിരുന്നെങ്കിൽ, മാറ്റിയ കോഡ് സ്റ്റ്രീം ചെയ്ത് ശൂന്യമല്ലാത്ത ഡെൽറ്റകളുമായി `response.output_text.delta` ഇവന്റുകൾ നൽകണം.
- [ ] **ഘടനാപരമായ ഔട്ട്‌പുട്ട്**: `text.format` `json_schema` ഉപയോഗിച്ച് വിനിയോഗിച്ചാൽ, `json.loads(resp.output_text)` വിജയം ആകും, സ്കീമയുമായി പൊരുത്തപ്പെടും.
- [ ] **ടൂൾ-കോൾ ലൂപ്പ്**: ടൂളുകൾ ഉപയോഗിക്കുന്നുവെങ്കിൽ, മോഡൽ ടൂൾ ചൊല്ലുകൾ പുറത്തിറക്കും, ആപ്പ് അവ നടപ്പിലാക്കും, പിന്നാലെ ഫോലോ-അപ്പ് അഭ്യർത്ഥന അന്തിമ `output_text` നൽകും (അനന്ത ലൂപ്പ് ഇല്ല).
- [ ] **Async പാരിറ്റി**: `AsyncAzureOpenAI` ഉപയോഗിച്ചിരുന്നെങ്കിൽ, `AsyncOpenAI` തുല്യമായി `await` ഉപയോഗിച്ച് പ്രവർത്തിക്കും.
- [ ] **പിശക് നിരക്ക്**: മൈഗ്രേഷനു മുമ്പുള്ള അടിസ്ഥാനരേഖയുമായി താരതമ്യം ചെയ്താൽ 400/401/404 പുതിയ പിശകുകൾ ഇല്ല.

### ഡെലിവറബിൾസുകൾ

- സംഗ്രഹത്തിൽ എഡിറ്റുചെയ്‌ത ഫയലുകൾ, പഴയകേൾ കാൾ സൈറ്റുകളുടെ മുൻപ്/ശേഷം എണ്ണങ്ങൾ, അടുത്ത ഘട്ടങ്ങൾ ഉൾപ്പെടുത്തണം.
- മാറ്റങ്ങൾ വേർക്കിങ്-ട്രീ എഡിറ്റുകൾ മാത്രം (കമ്മിറ്റുകൾ ഇല്ല).

---

## SDK വേർഷൻ ആവശ്യകതകൾ

| പാക്കേജ് | നെ strings തീർക്കുന്ന വേർഷൻ |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | നിലവിലുള്ളത് (EntraID ഓത്തിനായി) |

---

## റഫറൻസുകൾ

- [ചീറ്റ്ഷീറ്റ് — എല്ലാ കോഡ് സ്നിപ്പറ്റുകളും](./references/cheat-sheet.md)
- [ടസ്റ്റ് മൈഗ്രേഷൻ — മോക്സ്, സ്നാപ്ഷോട്ടുകൾ, അസർ‌ഷനുകൾ](./references/test-migration.md)
- [ട്രബ്ഷൂട്ടിംഗ് — പിശകുകൾ, റിസ്ക്ക് പട്ടിക, ഗോട്ട്‌ചാസ്](./references/troubleshooting.md)
- [detect_legacy.py — ഓട്ടോമേറ്റഡ് സ്കാനർ](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [അസ്യൂർ OpenAI സ്റ്റാർട്ടർ കിറ്റ്](https://aka.ms/openai/start)
- [അസ്യൂർ OpenAI Responses API ഡോക്സ്](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [അസ്യൂർ OpenAI API വേർഷൻ ലൈഫ്‌ഐക്ൾ](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API റഫറൻസ്](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->