---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI ചാറ്റ് പൂർത്തീകരണങ്ങളിൽ നിന്നുള്ള Python ആപ്ലിക്കേഷനുകൾ Responses APIയിലേക്ക്മാറ്റുക

> **അധികാരപരമായ മാർഗ്ഗനിർദ്ദേശം — കൃത്യമായി പിന്തുടരുക**
>
> ഈ സ്‌കിൽ Azure OpenAI ചാറ്റ് പൂർത്തീകരണങ്ങൾ ഉപയോഗിക്കുന്ന Python കോഡ്‌ബേസുകളെ
> ഏകീകൃത Responses APIയിലേക്ക് മാറ്റുന്നു. ഈ നിർദ്ദേശങ്ങൾ കൃത്യമായി പിന്തുടരുക.
> പാരാമീറ്റർ മാപ്പിംഗുകൾ അനായാസമായി നിർമിക്കരുത് അല്ലെങ്കിൽ API രൂപങ്ങൾ കണ്ടുപിടിക്കരുത്.

---

## ട്രിഗറുകൾ

ഉപയോക്താവ് ആവശ്യപ്പെടുമ്പോൾ ഈ സ്‌കിൽ സജീവമാക്കുക:
- Azure OpenAI ചാറ്റ് പൂർത്തീകരണങ്ങളിൽ നിന്നുള്ള Python ആപ്പ് Responses APIയിലേക്ക് മാറ്റുക
- Python OpenAI SDK ഉപയോഗം പുതിയ API രൂപത്തിലേക്ക് അപ്ഗ്രേഡ് ചെയ്യുക Azure OpenAIയ്ക്ക് എതിരെ
- Responses ആവശ്യമായ GPT-5 അല്ലെങ്കിൽ പുതിയ മോഡലുകളിലേക്ക് Python കോഡ് തയ്യാറാക്കുക Azureയിൽ
- `AzureOpenAI`/`AsyncAzureOpenAI`ൽ നിന്നു സധാരണമായ `OpenAI`/`AsyncOpenAI` ക്ലയന്റ് ഉപയോഗിച്ച് v1 എണ്ഡ്പോയിന്റിലേക്ക് മാറുക
- `AzureOpenAI` കൺസ്ട്രക്ടറുകളോ `api_version`-ലോ ബന്ധപ്പെട്ട ഡിപ്രെക്കേഷൻ മുന്നറിയിപ്പുകൾ പരിഹരിക്കുക

---

## ⚠️ മോഡൽ അനുയോജ്യത — ആദ്യം പരിശോധിക്കുക

> **മാറ്റം ചെയ്യുന്നതിന് മുമ്പ്, നിങ്ങളുടെ Azure OpenAI ഡിപ്ലോയ്മെന്റ് Responses API പിന്തുണയോക്കുകയാണ് എന്ന് സ്ഥിരീകരിക്കുക.**

### 1. നിങ്ങളുടെ ഡിപ്ലോയ്മെന്റ് ദ്രുതപരിശോധനം (ഏറ്റവും വേഗം)

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

> **കുറിപ്പ്**: Azure OpenAIയിൽ `max_output_tokens`-ന് കുറഞ്ഞത്രം 16 ആണ്. 16-ൽ താഴെയുള്ള മൂല്യങ്ങൾ 400 പിശക് നൽകും. Smoke test-കൾക്ക് 50+ ഉപയോഗിക്കുക.

ഇത് 404 തിരിച്ചുനൽകുന്നുണ്ടെങ്കിൽ, ആ ഡിപ്ലോയ്മെന്റിലെ മോഡൽ ഇനിയും Responses പിന്തുണക്കാത്തതാണ് — താഴെയുള്ള റഫറൻസ് പരിശോധിക്കുക അല്ലെങ്കിൽ പിന്തുണയുള്ള മോഡലുള്ള ഡിപ്ലോയ്മെൻറ് വീണ്ടും സജ്ജമാക്കുക.

### 2. നിങ്ങളുടെ മേഖലയിലെ ലഭ്യമായ മോഡലുകൾ പരിശോധിക്കുക (ശിപാർശ)

Responses API പിന്തുണയുള്ള മോഡലുകൾ ലഭ്യമാണ് എന്ന് കാണാൻ ബിൽറ്റ്-ഇൻ മോഡൽ അനുയോജ്യത ഉപകരണം നടത്തുക:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

ഇത് Azure ARM ലീവിലേക്ക് ക്വറി നടത്തുന്നു, ഒരു അനുയോജ്യത മെട്രിക്‌സ് കാണിക്കുന്നു — എവിടെ Responses, ഘടിത ഔട്ട്പുട്ട്, ഉപകരണങ്ങൾ തുടങ്ങിയവ പിന്തുണയ്ക്കുന്നു. ഫിൽട്ടർ ചെയ്യാൻ `--filter gpt-5.1,gpt-5.2` ഉപയോഗിക്കുക അല്ലെങ്കിൽ സ്ക്രിപ്റ്റിംഗിന് `--json`.

### 3. പൂർണ്ണ മോഡൽ പിന്തുണ റഫറൻസ്

- **ലൈവ് ക്വറി**: `python migrate.py models` (മുകളിൽ കാണാം — മേഖലയനുസൃതം, എല്ലായ്പ്പോഴും പുതുക്കിയതും)
- **ലഭ്യത ബ്രൗസ് ചെയ്യുക**: [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **പ്രാരംഭവും മാർഗ്ഗനിർദ്ദേശവും**: **https://aka.ms/openai/start**

### ⚠️ പഴയ മോഡലുകളുടെ പരിമിതികൾ

> **മുന്നറിയിപ്പ്**: പഴയ മോഡലുകൾ (ഉദാഹരണത്തിന് `gpt-4o`, `gpt-4`) Responses APIയുടെ എല്ലാ സവിശേഷതകളും സമ്പൂർണ്ണമായി പിന്തുണയ്ക്കില്ല.
>
> പഴയ മോഡലുകളിലെ അറിയപ്പെട്ട പരിമിതികൾ:
> - **`reasoning` പാരാമീറ്റർ**: `gpt-4o-mini`, `gpt-4o` എന്നിവയിലും പല നോണ്-റിയസണിംഗ് മോഡലുകളിലും പിന്തുണയില്ല. ആദ്യം കോഡിൽ ഉണ്ടെങ്കിൽ മാത്രം `reasoning` മാറ്റുക.
> - **`seed` പാരാമീറ്റര്**: Responses APIയിൽ ഒന്നും പിന്തുണയില്ല — എല്ലാ അഭ്യർത്ഥനകളിൽ നിന്നും നീക്കംചെയ്യുക.
> - **`text.format` മുഖേന ഘടിത ഔട്ട്പുട്ട്**: പഴയ മോഡലുകൾ `strict: true` JSON സ്കീമകൾ ഉറപ്പാക്കാൻ വിശ്വസ്തമല്ല.
> - **ടൂൾ ഓർക്കസ്ട്രേഷൻ**: GPT-5+.tools കോൾസ് ഉൾപ്പെടുത്തുന്നത് റിയാസണിംഗിന്റെ ഭാഗമാണ്. പഴയ മോഡലുകൾ Responses-ൽ പ്രവർത്തിച്ചാലും ഈ ആഴത്തിലുള്ള സംയോജനം ഏറെയാണ്.
> - **തെമ്പറേച്ചർ നിയന്ത്രണങ്ങൾ**: `gpt-5`-ലേക്ക് മാറുമ്പോൾ, താപനില ഒഴിവാക്കുകയോ 1-അക്കമാക്കുകയോ വേണം. പഴയ മോഡലുകൾക്ക് ഇതിലെ നിയന്ത്രണമില്ല.

### O-സീരീസ് റിയാസണിംഗ് മോഡലുകൾ (o1, o3-mini, o3, o4-mini)

O-സീരീസ് മോഡലുകൾക്ക് പ്രത്യേക പാരാമീറ്റർ നിയന്ത്രണങ്ങൾ ഉണ്ട്. O-സീരീസ് മോഡലുകൾ ലക്ഷ്യമിടുന്ന ആപ്ലിക്കേഷനുകൾ മാറ്റുമ്പോൾ:

- **`temperature`**: 1 ആക്കണമോ ഒഴിവാക്കണമോ. O-സീരീസ് മോഡലുകൾ മറ്റെന്തെങ്കിലും മൂല്യങ്ങൾ സ്വീകരിക്കില്ല.
- **`max_completion_tokens` → `max_output_tokens`**: Azure-നിർദിഷ്ടമായ `max_completion_tokens` ഉപയോഗിക്കുന്ന ആപ്ലിക്കേഷനുകൾ `max_output_tokens`-ലേക്ക് മാറണം. Reasoning ടോക്കൺ പരിധിക്കുപുറം കണക്കാക്കുമ്പോൾ ഉയർന്ന മൂല്യങ്ങൾ (4096+) സജ്ജീകരിക്കുക.
- **`reasoning_effort`**: ആപ്പ് `reasoning_effort` (low/medium/high) ഉപയോഗിക്കുന്നുവെങ്കിൽ തുടരും — O-സീരീസിന് Responses API ഈ പാരാമീറ്റർ പിന്തുണയ്ക്കുന്നു.
- **സ്റ്റ്രീമിംഗ് പെരുമാറ്റം**: റിയാസണിംഗ് പൂർത്തിയാകുന്നത് വരെ O-സീരീസ് മോഡലുകൾ ഔട്ട്പുട്ട് ബഫർ ചെയ്യാം പിന്നീട് ടെക്സ്റ്റ് ഡെൽറ്റാ ഇവന്റുകൾ അയക്കും. സ്റ്റ്രീമിംഗ് ഇപ്പോഴും പ്രവർത്തിക്കുന്നു, പക്ഷേ ആദ്യ `response.output_text.delta` GPT മോഡലുകളെ അപേക്ഷിച്ച് കൂടുതൽ വൈകിയെത്തും.
- **`top_p`**: O-സീരീസ് പിന്തുണയില്ല — ഉണ്ടെങ്കിൽ നീക്കംചെയ്യുക.
- **ടൂൾ ഉപയോഗം**: O-സീരീസ് മോഡലുകൾ Responses API വഴിയുള്ള ടൂളുകൾ പിന്തുണയ്ക്കുന്നു GPT മോഡലുകൾ പോലെ, എന്നാൽ ടൂൾ കോൾ ഓർക്കസ്ട്രേഷൻ നിലവാരം മോഡലുകളിങ്ങനെ വ്യത്യാസപ്പെടുന്നു.

**പ്രവർത്തി — പ്രോആക്റ്റീവ് മോഡൽ ഉപദേശം**: സ്കാൻ ഘട്ടത്തിൽ, ആപ്ലിക്കേഷൻ ലക്ഷ്യമിടുന്ന മോഡൽ പരിശോധിക്കുക (ഡിപ്ലോയ്മെന്റ് നാമങ്ങൾ, എൻവ് വേരിയബിളുകൾ, കോൺഫിഗ്). മോഡൽ `gpt-4o` അല്ലെങ്കിൽ പഴയതായാൽ (gpt-4.1+ അല്ലാത്തത്), പ്രോആക്റ്റീവായി ഉപയോക്താവിന് പറയുക:
- ശരാശരി ടെക്സ്റ്റ്, ചാറ്റ്, സ്റ്റ്രീമിംഗ്, ടൂളുകൾ ഓർക്കസ്ട്രേഷനിൽ ഈ മൈഗ്രേഷൻ പ്രവര്‍ത്തിക്കും.
- പുതിയ മോഡലുകൾ (`gpt-5.1`, `gpt-5.2`) നല്ല ടൂൾ ഓർക്കസ്ട്രേഷൻ, ഘടിത ഔട്ട്പുട്ട് ഉറപ്പാക്കൽ, റിയാസണിംഗ്, കറോസ്-റീജിയൻ ലഭ്യത നൽകുന്നു.
- അവർ തയ്യാറാകുമ്പോൾ അവരുടെ ഡിപ്ലോയ്മെന്റ് അപ്ഗ്രേഡു പരിഗണിക്കണം — മൈഗ്രേഷനിൽ തടസ്സം കൾക്കില്ല.

മോഡൽ പതിപ്പിനെ അടിസ്ഥാനമാക്കി മൈഗ്രേഷൻ തടയുകയോ നിരസിക്കുകയോ ചെയ്തുകൊണ്ടിരിക്കരുത്. ഈ ഉപദേശം വിവരാത്മകമാണു്.

### GitHub മോഡലുകൾ Responses API പിന്തുണയ്ക്കുന്നില്ല

> **GitHub മോഡലുകൾ (`models.github.ai`, `models.inference.ai.azure.com`) Responses API പിന്തുണയ്ക്കുന്നില്ല.**

കോഡ്‌ബേസിൽ GitHub മോഡലുകൾക്കായുള്ള കോഡ് പാത ഉണ്ടെങ്കിൽ (`base_url` `models.github.ai` അല്ലെങ്കിൽ `models.inference.ai.azure.com` കാണുമ്പോൾ), മൈഗ്രേഷനിൽ **മുറിച്ച് കളയുക**. Responses APIക്ക് Azure OpenAI, OpenAI, അല്ലെങ്കിൽ അനുയോജ്യമായ ലോക്കൽ എണ്ഡ്പോയിന്റ് (ഉദാ: Ollama Responses പിന്തുണയോടുകൂടി) ആവശ്യമുണ്ട്.

സ്കാൻ സമയത്ത് നടപടി:
- GitHub മോഡൽ കോഡ് പാതകളും നീക്കണമെന്ന് ഫ്ലാഗ് ചെയ്യുക.

---

## ഫ്രെയിംവർക്ക് മൈഗ്രേഷൻ

OpenAIയ്ക്കു മുകളിൽ പ്രവർത്തിക്കുന്ന ഉയർന്ന തലത്തിലുള്ള ഫ്രെയിംവർക്കുകൾ പല ആപ്പുകൾ ഉപയോഗിക്കുന്നു. ഇവ മൈഗ്രേറ്റ് ചെയ്യുമ്പോൾ, ഫ്രെയിംവർക്ക് തന്നെ API മാറ്റങ്ങൾ ഉണ്ടാകുന്നു — OpenAI കോൾസ് മാത്രമല്ല.

### Microsoft Agent Framework (MAF)

**നിങ്ങളുടെ MAF പതിപ്പ് ആദ്യം പരിശോധിക്കുക** — മൈഗ്രേഷൻ MAF 1.0.0+ ആണോ അല്ലെങ്കിൽ 1.0.0-മുൽസവറീസുകൾ/റിസർവിസ് (ബിർട/ആർസി) ആണോ എന്ന് ആശ്രയിച്ചിരിക്കും.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ഇപ്പൊഴാണ് Responses API ഉപയോഗിക്കുന്നത്** — മൈഗ്രേഷൻ ആവശ്യമില്ല. കോഡ്‌ബേസിൽ പഴയ `OpenAIChatCompletionClient` (ഇത് `chat.completions.create` ഉപയോഗിക്കുന്നു) ഉണ്ടെങ്കിൽ, അത് `OpenAIChatClient`-ൽ മാറ്റുക.

| മുമ്പ് | അക്രമം |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

നിങ്ങളുടെ പതിപ്പ് പരിശോധിക്കാൻ: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (ബിർട/ആർസി റിലീസുകൾ)

മുൻ-1.0.0 MAF-ൽ `OpenAIChatClient` Chat Completions ഉപയോഗിച്ചിരുന്നു. `agent-framework-openai>=1.0.0`-ലേക്ക് അപ്ഗ്രേഡ് ചെയ്യുക, ഇവിടെ `OpenAIChatClient` Responses API ഡീഫോൾട്ട് ആയി ഉപയോഗിക്കുന്നു.

മറ്റ് മാറ്റങ്ങൾ ആവശ്യമില്ല — `Agent` ഉം ടൂൾ APIകൾ തന്നെ തുടരും.

### LangChain (`langchain-openai`)

`ChatOpenAI()`-യിൽ `use_responses_api=True` ചേർക്കുക. കൂടാതെ പ്രതികരണ ആക്സസ് `.content`-യിൽ നിന്ന് `.text`-ലേക്ക് മാറ്റുക.

| മുമ്പ് | അക്രമം |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

പൂർണ്ണ മുൻ/പിന്നീട് കോഡ് ഉദാഹരണങ്ങൾക്കായി [cheat-sheet.md](./references/cheat-sheet.md) കാണുക.

---

## ഫ്രണ്ട്‌എൻഡ് മൈഗ്രേഷൻ മാർഗ്ഗനിർദ്ദേശം

> **Responses API സേർവർ-വശ ബന്ധമാണ്.** Python ബാക്ക്‌എന്റും മാറ്റുക; ഫ്രണ്ട്‌എൻഡിന്റെ HTTP കരാർ മാറ്റേണ്ടതില്ല, ബാക്ക്‌എന്റ് തണുത്ത പാസ്സ്-ത്രൂ ആയിരിക്കും എങ്കിൽ മാത്രം Responses അഭ്യർത്ഥന രൂപം സ്വീകരിക്കുക പരിഗണിക്കുക. ഫ്രണ്ട്‌എൻഡ് നേരിട്ട് OpenAIക്കയുമായി ക്ലയന്റ്-സൈഡ് കീ ഉപയോഗിച്ചാൽ, ആദ്യം ആ കോളുകൾ ബാക്ക്‌എന്റിലേക്കു മാറ്റുക.

### `@microsoft/ai-chat-protocol` ഡിപ്രെക്കേഷൻ

`@microsoft/ai-chat-protocol` npm പാക്കേജ് ഡിപ്രെക്കേറ്റ് ചെയ്യപ്പെട്ടതാണ്, ഇത് [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) കൊണ്ട് മാറ്റേണ്ടതാണ്. ഫ്രണ്ട്‌എൻഡിൽ ഇത് കണ്ടാൽ:

1. CDN സ്ക്രിപ്റ്റ് ടാഗ് മാറ്റുക:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` വിപുലീകരണം നീക്കംചെയ്യുക (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. `client.getStreamedCompletion(messages)` മാറി നേരിട്ട് പിന്‍ബാക്ക് സ്ട്രീമിംഗ് എണ്ഡ്പോയിന്റിലേക്ക് `fetch()` വിളിക്കുക.
4. `for await (const response of result)` കൂടാതെ `for await (const chunk of readNDJSONStream(response.body))` ഉപയോഗിക്കുക.
5. പ്രോപ്പർട്ടി ആക്സസ് `response.delta.content`/`response.error`-ൽ നിന്ന് `chunk.delta.content`/`chunk.error`-ലേക്ക് മാറ്റുക.

---

## ലക്ഷ്യങ്ങൾ

- Azure OpenAIക്ക് എതിരായി ചാറ്റ് പൂർത്തീകരണങ്ങൾ അല്ലെങ്കിൽ ലെഗസി പൂർത്തീകരണങ്ങൾ ഉപയോഗിക്കുന്ന എല്ലാ Python കോൾ സൈറ്റുകളും എണ്ണുക.
- Python കോഡ്‌ബേസിന്റെ മൈഗ്രേഷൻ പ്ലാനും ക്രമവും നിർദ്ദേശിക്കുക.
- Responses API-യിലേക്ക് സുരക്ഷിതവും അല്പപരിവർത്തനവും ഉപയോഗിച്ച് മാറ്റം ചെയ്യുക.
- Responses ഔട്ട്പുട്ട് സ്കീമ ഉപയോഗിക്കാൻ കോൾ ചെയ്യുന്നവരുടെ കോഡ് അപ്ഡേറ്റ് ചെയ്യുക; ബാക്ക്വാർഡ്-കമ്പാറ്റിബിൽ റാപ്പർസ് ഒഴിവാക്കി.
- ടെസ്റ്റുകളും ലിൻറ്റുകളും ഓട്ടു; മൈഗ്രേഷനാൽ വരള്ള ലഘു തകരാറുകൾ പരിഹരിക്കുക.
- ചെറിയ, അവലോകനയോഗ്യമായ മാറ്റസെറ്റുകൾ തയ്യാറാക്കുക, ഡിഫ്‌സുമായി അവസാന ഘട്ടം സമർപിക്കുക (കമ്മിറ്റ് ചെയ്തു മാറ്റരുത്).

---

## ഗാർഡ്‌റെയ്ൽസ്

- ഗിറ്റ് വർക്ക്‌സ്പേസിനുള്ളിൽ മാത്രം ഫയലുകൾ മാറ്റുക. പുറത്ത് എഴുതരുത്.
- പിന്‍റപ്പം സംവരണം ഷിമുകൾ ആവശ്യമില്ല; കോഡ് പുതിയ API രൂപത്തിലേക്ക് മാറ്റുക.
- ടോംബ്സോൺ/ട്രാൻസിഷൻ കമന്റുകളും ബാക്ക്‌അപ്പ് ഫയലുകളും വിട്ടുവീഴ്‌ക്കരുത്.
- മുമ്പ് ഉപയോഗിച്ചിരുന്നെങ്കിൽ സ്റ്റ്രീമിംഗ് സവിശേഷതകൾ നിലനിര്‍ത്തുക; അല്ലെങ്കിൽ സ്റ്റ്രീം ഇല്ലാത്ത മാര്‍ഗം ഉപയോഗിക്കുക.
- അംഗീകാരമോഡിൽ ആണെങ്കിൽ കമാൻഡ് അല്ലെങ്കിൽ നെറ്റ്‌വർക്ക് കോൾ നടത്തുന്നതിന് മുമ്പ് അംഗീകാരം ആവശ്യപ്പെടുക.
- `git add`/`git commit`/`git push` ഓടിക്കരുത്; വെർക്ക്-ട്രീ എഡിറ്റുകൾ മാത്രം നൽകുക.

---

## ഘട്ടം 0: Azure OpenAI ക്ലയന്റ് മൈഗ്രേഷൻ (പ്രാഥമികകാരം)

കോഡ്‌ബേസ് `AzureOpenAI` അല്ലെങ്കിൽ `AsyncAzureOpenAI` കൺസ്ട്രക്ടറുകൾ ഉപയോഗിക്കുന്നുവെങ്കിൽ, ആദ്യം സാധാരണ `OpenAI` / `AsyncOpenAI` കൺസ്ട്രക്ടറുകളിലേക്ക് മാറുക. Azure-നിർദിഷ്ട കൺസ്ട്രക്ടറുകൾ `openai>=1.108.1`-ൽ ഡിപ്രെകേറ്റഡ് ആണ്.

### v1 API പാതയുടെ കാര്യം എന്ത്?

പുതിയ `/openai/v1` എണ്ഡ്‌പോയിന്റ് `AzureOpenAI()`-ലും പകരം സാധാരണ `OpenAI()` ക്ലയന്റ് ഉപയോഗിക്കുന്നു, `api_version` പാരാമീറ്റർ ആവശ്യമില്ല, OpenAI-നും Azure OpenAI-നും ഒരുപോലെ പ്രവർത്തിക്കുന്നു. ഒരു കോഡ് പിന്തുണ എളുപ്പമാണ് — പതിപ്പ് മാനേജ്‌മെന്റ് ആവശ്യമില്ല.

### പ്രധാന മാറ്റങ്ങൾ

| മുമ്പ് | ശേഷം |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | പൂർണ്ണമായും നീക്കം |

### സുശ്രൂഷാ ചെക്ക്ലിസ്റ്റ്

- ക്ലയന്റ് നിർമ്മാണത്തിൽ നിന്നും `api_version` പാരാമീറ്റർ നീക്കംചെയ്യുക.
- `.env`, ആപ്പ് സെറ്റിംഗുകൾ, ബൈസിപ്പ്/ഇൻഫ്ര ഫയലുകളിൽ നിന്നും `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` എൻവിയരൺമെന്റ് വേരിയബിളുകൾ നീക്കംചെയ്യുക.
- `.env`, ആപ്പ് സെറ്റിംഗുകൾ, ബൈസിപ്പ്/ഇൻഫ്ര, ടെസ്റ്റ് ഫിക്സ്ചറുകളിൽ `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` എന്നാക്കി പുനർനാമകരണം നടത്തുക (സ്റ്റാൻഡേർഡ് Azure ഐഡെന്റിറ്റി SDK പ്രക്രിയ).
- `requirements.txt` അല്ലെങ്കിൽ `pyproject.toml` ഡോക്യുമെന്റുകളിൽ `openai>=1.108.1` ഉറപ്പാക്കുക.

### എൻവಿಯറൺമെന്റ് വേരിയബിൾ മാറ്റം

| പഴയ എൻവ് വാരിയബിൾ | നടപടി | കുറിപ്പുകൾ |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **നീക്കം** | v1 എണ്ഡ്‌പോയിന്റിന് `api_version` വേണ്ടത് അല്ല |
| `AZURE_OPENAI_API_VERSION` | **നീക്കം** | മുകളിലുള്ളതിന്റെ പോലെയാണ് |
| `AZURE_OPENAI_CLIENT_ID` | **പുനർനാമകരണം** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)`-ന് സ്റ്റാൻഡേർഡ് Azure ഐഡെന്റിറ്റി SDK ചട്ടം |
| `AZURE_OPENAI_ENDPOINT` | **തുടരുക** | `base_url` നിർമ്മാണത്തിന് ഇതു വേണ്ടതാണ് |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **തുടരുക** | `responses.create`-ൽ `model` പാരാമീറ്ററായി ഉപയോഗിക്കുന്നു |
| `AZURE_OPENAI_API_KEY` | **തുടരുക** | കീ അധിഷ്ടിത അംഗീകാരം ആവശ്യത്തിന് |

ക്ലയന്റ് സെറ്റപ്പ് കോഡ് ഉദാഹരണങ്ങൾക്കായി (സിങ്ക്, അസിങ്ക്, EntraID, API കീ, മൾട്ടി-ടെന്നന്റ്) [cheat-sheet.md](./references/cheat-sheet.md) കാണുക.

---

## ഘട്ടം 1: ലെഗസി കോൾ സൈറ്റുകൾ കണ്ടെത്തുക

മൈഗ്രേഷനുമായി ബന്ധപ്പെട്ട എല്ലാ കോൾ സൈറ്റുകളും കണ്ടെത്താൻ [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) സ്ക്രിപ്റ്റ് ഓടിക്കുക:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

അല്ലെങ്കിൽ ഈ തിരച്ചിലുകൾ കൈമടി നടത്താം — ഓരോ പൊരുത്തവും മൈഗ്രേഷൻ ലക്ഷ്യമാണ്:

```bash
# പാരമ്പര്യ API കോളുകൾ (മറുപടി എഴുതേണ്ടത് അനിവാര്യമാണ്)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# പഴക്കി Azure ക്ലയന്റ് കൺസ്ട്രക്ടറുകൾ (മാറേണ്ടതാണ്)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# മറുപടി ആകൃതി ആക്സസ് രീതി (പുതുക്കേണ്ടതാണ്)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# പഴയ നെട്ടിയിലുള്ള ടൂൾ నిర్వചനങ്ങൾ (സമതലമാക്കേണ്ടതാണ്)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# പഴയ രീതിയിലുള്ള ടൂൾ ഫലങ്ങൾ (function_call_output ആയി മാറ്റേണ്ടതാണ്)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# പഴയപരിഹരങ്ങൾ (അപരിഹരമാക്കുകയോ പേരുചെറിയുകയോ ചെയ്യേണ്ടതാണ്)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens ആക്കുക
rg "['\"]seed['\"]"      # remove entirely

# പഴയ പരിസ്ഥിതി വേരിയബിളുകൾ (ശുദ്ധിയാക്കുക)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # ആഴർ_CLIENT_ID ആകണം

# GitHub മോഡൽ എന്റ്പോയിന്റുകൾ (അയയ്ക്കേണ്ട - Responses API പിന്തുണയില്ല)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# ഫ്രെയിംവർക്ക് നിലപാടില്ലായ്മകൾ (പുതുക്കേണ്ടത്)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient അഥവാ മാറുക
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True ആവശ്യമുണ്ട്

# ടെസ്റ്റ് ഇൻഫ്രാസ്ട്രക്ചർ (പുതുക്കേണ്ടതാണ്)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# ഉള്ളടക്കം ഫിൽട്ടർ പിശക് ബോഡി ആക്‌സസ് (പുതുക്കേണ്ടത് - ഘടന മാറ്റം)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # പഴയ ഏകവചനം - ഇപ്പോൾ content_filter_results (ബഹുവചനം) content_filters അറെയിൽ

# Chat Completions എൻഡ്‌പോയിന്റിലേക്ക് Raw HTTP കോളുകൾ (URL അപ്ഡേറ്റ് ചെയ്യേണ്ടത്)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### ഹ്യൂറിസ്റ്റിക്സ് (കണ്ടെത്താനും പുനർമാറ്റത്തിനും)

- **ചാറ്റ് പൂർത്തീകരണ ക്ലയന്റ്**: `client.chat.completions.create` → `client.responses.create(...)`.

- **ആസൂർ ക്ലൈന്റ് കൺസ്ട്രക്ടറുകൾ**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **ടൂളുകൾ**: ഫംക്ഷൻ-കോളിംഗ് ടൂൾ നിർവചനങ്ങളെ നസ്റ്റിലായ ഫോർമാറ്റിൽ നിന്നു് (`{"type": "function", "function": {"name": ...}}`) ഫ്ലാറ്റ് Responses ഫോർമാറ്റിലേക്ക് മാറ്റുക (`{"type": "function", "name": ...}`); `tool_choice` ഉപയോഗിക്കുക; ടൂൾ ഫലങ്ങൾ `{"type": "function_call_output", "call_id": ..., "output": ...}` അംശങ്ങളായി ( `{"role": "tool", ...}` അല്ല) തിരികെ നൽകുക.
- **ടൂൾ റൗണ്ട്-ട്രിപ്സ്**: മോഡൽ ഫംക്ഷൻ കോളുകൾ തിരിച്ചുനൽകുമ്പോൾ, സംഭാഷണത്തിലേക്ക് `response.output` അംശങ്ങൾ ചേർക്കുക (മാനുവൽ `{"role": "assistant", "tool_calls": [...]}` ഡിക്ഷണറി അല്ല), പിന്നെ ഫലം ലഭിക്കുന്ന ഓരോ ഫംക്ഷൻ കോളിന് `function_call_output` അംശങ്ങൾ ചേർക്കുക.
- **ഫ്യൂ-ഷോട്ട് ടൂൾ ഉദാഹരണങ്ങൾ**: സംഭാഷണത്തിൽ ഹാർഡ്‌കോഡഡ് ടൂൾ കോളിങ് ഉദാഹരണങ്ങൾ ഉണ്ടെങ്കിൽ അവ `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` അംശങ്ങളായി മാറ്റുക. ഐഡികൾ `fc_` എന്നതോടെ തുടങ്ങണം.
- **`pydantic_function_tool()`**: ഈ ഹെൽപർ ഇപ്പോഴും പഴയ നസ്റ്റിലായ ഫോർമാറ്റ് ജനറേറ്റ് ചെയ്യുന്നു, `responses.create()`-യുമായി **കമ്പാറ്റിബിൾ അല്ല**. മാനുവൽ ടൂൾ നിർവചനങ്ങളോ ഫ്ലാറ്റ് ചെയ്യുന്ന റാപ്പറോ ഉപയോഗിക്കുക.
- **മൾട്ടി-ടേൺ**: ആപ്പ് സംഭാഷണ ചരിത്രം നിലനിർത്തുക; മുൻപ് പറഞ്ഞ ടേണുകൾ `input` അംശങ്ങളിലൂടെ പാസ്സാക്കുക.
- **ഫോർമാറ്റിംഗ്**: ചാറ്റിന്റെ ടോപ്പ് ലെവൽ `response_format`-നെ Responses-ൽ `text.format`으로 മാറ്റുക. പാരമ്പര്യ രൂപം: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **കോണ്ടന്റ് അംശങ്ങൾ**: ചാറ്റ് `content[].type: "text"`-നെ Responds-ലെ `content[].type: "input_text"`으로 മാറ്റുക, യൂസർ/സിസ്റ്റം ടേണുകൾക്കായി.
- **ഇമേജ് കോൺറന്റ് അംശങ്ങൾ**: ചാറ്റ് `content[].type: "image_url"`-നെ Responses-ലെ `content[].type: "input_image"`으로 മാറ്റുക. `image_url` ഫീൽഡ് നസ്റ്റിലായ ഒബ്ജക്റ്റ് `{"url": "..."}` മുതൽ ഫ്ലാറ്റ് സ്ട്രിങ്ങായി മാറും. മുൻപ്/പിന്നീട് ഉദാഹരണങ്ങൾക്കായി ചീറ്റ്ഷീറ്റ് കാണുക.
- **റീസണിംഗ് ശ്രമം**: **അമലെ റീസണിംഗ് ഉള്ളെങ്കിൽ മാത്രം മൈഗ്രേറ്റ് ചെയ്യുക**.
- **കോണ്ടന്റ് ഫിൽട്ടർ എറർ ഹാൻഡ്ലിംഗ്**: എറർ ബോഡിയുടെ ഘടന മാറി. ചാറ്റ് കോമ്പ്ലീഷൻസ് `error.body["innererror"]["content_filter_result"]` (ഏകവചനം) ഉപയോഗിച്ചിരുന്നു; Responses API `error.body["content_filters"][0]["content_filter_results"]` (ബഹുവചനം, ഒരു അറേയിൽ) ഉപയോഗിക്കുന്നു. `innererror` ആക്സസ് ചെയ്യുന്ന കോഡ് `KeyError` ഉയർത്തും. പുതിയ പാത ഉപയോഗിച്ച് പുനർനിർമ്മിക്കുക.
- **റോ ഹ്റ്റ്ട്പ് കോൾസ്**: ആപ്പ് Azure OpenAI REST API നേരിട്ട് (requests, httpx മുതലായവ) `/openai/deployments/{name}/chat/completions?api-version=...` വഴി വിളിച്ചാൽ, ഇത് `/openai/v1/responses` ആയി പുനഃരചിക്കുക. റിക്വസ്റ്റ് ബോഡി മാറുന്നു: `messages` → `input`, `max_output_tokens` ചേർക്കുക, `store: false` ചേർക്കുക, `api-version` ക്വറി പാരാമി നീക്കം ചെയ്യുക. റെസ്പോൺസ് ബോഡി: `choices[0].message.content` → `output[0].content[0].text` (അവഗണന ചെയ്യേണ്ടത്: `output_text` SDK സൗകര്യമാസ്യം, റോ JSON-ൽ ഇല്ല).

---

## ഘട്ടം 2: മൈഗ്രേഷൻ പ്രയോഗിക്കുക

### മൈഗ്രേഷൻ കുറിപ്പുകൾ (ചാറ്റ് കോമ്പ്ലീഷൻസ് → Responses)

- **എന്തിന് മൈഗ്രേറ്റ് ചെയ്യണം**: ടെക്സ്റ്റിനു, ടൂളുകൾക്കും, സ്ട്രീമിങ്ങിനും ഒരുമിച്ചുള്ള API ആണ് Responses; ചാറ്റ് കോമ്പ്ലീഷൻസ് പാരമ്പര്യം മാത്രമാണ്. GPT-5-നോട് കൂട്ടി മികച്ച പ്രകടനത്തിനായി Responses വേണമെന്നതാണ്.
- **HTTP**: Azure എൻഡ്‌പോയിന്റ് `/openai/deployments/{name}/chat/completions` മുതൽ `/openai/v1/responses` ആയി മാറുന്നു.
- **ഫീൽഡുകൾ**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` అదే നിലയിൽ.
- **ഫോർമാറ്റിംഗ്**: `response_format` → `text.format` (ഒരുവസ്തുക്കൾ).
- **കോണ്ടന്റ് അംശങ്ങൾ**: ചാറ്റ് `content[].type: "text"` → Responses `content[].type: "input_text"` (സിസ്റ്റം/യൂസർ ടേൺ).
- **ഇമേജ് കോൺറന്റ് അംശങ്ങൾ**: ചാറ്റ് `content[].type: "image_url"` → Responses `content[].type: "input_image"`. `image_url` ഫീൽഡ് നസ്റ്റിലായ {"image_url": {"url": "..."}}ൽ നിന്നു് {"image_url": "..."} (സാദാരണ സ്ട്രിംഗ് – HTTPS URL അല്ലെങ്കിൽ `data:image/...;base64,...` ഡേറ്റാ URI).

### പാരാമീറ്റർ മാപ്പിംഗ് റഫറൻസ്

| ചാറ്റ് കോമ്പ്ലീഷൻസ് | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (അംശങ്ങളുടെ അറേ) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (ഒബ്ജക്റ്റ്) |
| `temperature` | `temperature` (മാറാനില്ല) |
| `stop` | `stop` (മാറാനില്ല) |
| `frequency_penalty` | `frequency_penalty` (മാറാനില്ല) |
| `presence_penalty` | `presence_penalty` (മാറാനില്ല) |
| `tools` / function-calling | `tools` (മാറാനില്ല) |
| `seed` | **നീക്കം ചെയ്യുക** (മદદവരുന്നില്ല) |
| `store` | `store` (`false` ആയി സജ്ജീകരിക്കൽ) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ഫ്ലാറ്റ് സ്ട്രിംഗ്) |

സമ്പൂർണ്ണ മുൻനിർത്തലും/പിന്നീട് കാൽവുകൾക്കായി [cheat-sheet.md](./references/cheat-sheet.md) കാണുക.

ടെസ്റ്റ് ഇൻഫ്രാസ്ട്രക്ചർ മൈഗ്രേഷനും (മോക്കുകൾ, സ്നാപ്ഷോട്ടുകൾ, അസെർഷനുകൾ) വേണ്ടി [test-migration.md](./references/test-migration.md) കാണുക.

പിഴവുകളും പ്രശ്‌നങ്ങളും പരിഹരിക്കാനുള്ള മാർഗ്ഗങ്ങൾക്കായി [troubleshooting.md](./references/troubleshooting.md) കാണുക.

---

## ഡാറ്റ രെടൻഷൻ & സ്റ്റേറ്റ്

- എല്ലാ Responses അഭ്യർത്ഥനകളിലും `store: false` സജ്ജീകരിക്കുക.
- മുൻപ് പറഞ്ഞ സന്ദേശ ഐഡികൾ അല്ലെങ്കിൽ സർവർ-നൽകിയ കോൺടെക്സ്റ്റിൽ ആശ്രയിക്കേണ്ട; സ്റ്റേറ്റ് ക്ലയന്റ്-നിർവഹിതവും മിനิมൽ മെടാഡേറ്റയും ആക്കുക.

---

## അംഗീകാരം ക്രൈറ്റീരിയ

### കോഡ്-തലത്തിലുള്ള ഗെയ്റ്റുകൾ (മൊത്തം പാസ്സാകണം)

- [ ] മൈഗ്രേറ്റ് ചെയ്ത ഫയലുകളിൽ `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` എന്നതിനുള്ള പൂജ്യം ഫലങ്ങൾ.
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("`-ന്റെ പൂജ്യം; എല്ലാ കൺസ്ട്രക്ടറുകളും `OpenAI`/`AsyncOpenAI` ഉപയോഗിച്ച് v1 എൻഡ്‌പോയിന്റ് ഉപയോഗിക്കുന്നു.
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"`-ന്റെ പൂജ്യം — GitHub മോഡൽ കോഡ് പാതകൾ നീക്കം ചെയ്തിട്ടുണ്ട്.
- [ ] `rg "OpenAIChatCompletionClient"`-ന്റെ പൂജ്യം — MAF 1.0.0+ കോഡ് `OpenAIChatClient` ഉപയോഗിക്കുന്നു (Responses API). പ്രീ-1.0.0-ൽ `agent-framework-openai>=1.0.0` ആയി അപ്ഗ്രേഡ് ചെയ്യുക.
- [ ] എല്ലാ `ChatOpenAI(...)` കോൾസിലും `use_responses_api=True` ഉൾപ്പെടുത്തിയിട്ടുണ്ട്.
- [ ] `rg "choices\[0\]"`-ന്റെ പൂജ്യം — എല്ലാ റെസ്പോൺസ് ആക്‌സസ് `resp.output_text` അല്ലെങ്കിൽ Responses ഔട്ട്പുട്ട് സ്കീമ ഉപയോഗിക്കുന്നു.
- [ ] മുൻനിലവാര നിരക്കിൽ ടോപ്പ് ലെവലിൽ ഒന്നും `response_format` ഉപയോഗിക്കരുത്; എല്ലാ സ്ട്രക്സ്ചേച്ചർഡ് ഔട്ട്പുട്ടിനും `text={"format": {...}}` ഉപയോഗിക്കുക.
- [ ] `openai>=1.108.1` & `azure-identity` `requirements.txt` അല്ലെങ്കിൽ `pyproject.toml` -ൽ; ഡിപ്പൻഡൻസികൾ പുനഃസ്ഥാപിച്ചിരിക്കുന്നു.
- [ ] ഓരോ `responses.create` കോൾഷിലും `store=False` സജ്ജീകരിച്ചു.
- [ ] ക്ലയന്റ് കൺസ്ട്രക്ഷനിൽ `api_version` ഇല്ല; `AZURE_OPENAI_API_VERSION` എൻവ്ഫയലുകളിൽ നിന്നും ഇൻഫ്രയിൽ നിന്നും നീക്കംചെയ്‌തു.

### ടെസ്റ്റ് ഇൻഫ്രാസ്ട്രക്ചർ ഗെയ്റ്റുകൾ (എല്ലാം പാസ്സാവണം)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`-ന്റെ പൂജ്യം.
- [ ] `rg "_azure_ad_token_provider" tests/`-ന്റെ പൂജ്യം — അസെർഷനുകൾ `isinstance(client, AsyncOpenAI)` അല്ലെങ്കിൽ `base_url` പരിശോധിക്കാൻ അപ്ഡേറ്റുചെയ്‌തു.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/`-ന്റെ പൂജ്യം — Azure-സാങ്കേതിക ഫിൽട്ടർ മോകുകൾ നീക്കംചെയ്‌തു.
- [ ] മോക് ഫിക്‌ചറുകൾ `kwargs.get("input")` ഉപയോഗിക്കുന്നു, `kwargs.get("messages")` അല്ല.
- [ ] സ്നാപ്ഷോട്ട് / ഗോൾഡൻ ഫയലുകൾ Responses സ്ട്രീമിംഗ് രൂപത്തിൽ അപ്ഡേറ്റുചെയ്‌തു ( `choices[0]`, `function_call`, `logprobs` ഇല്ല).
- [ ] എല്ലാ ടെസ്റ്റ് അപ്ഡേറ്റുകൾക്കുശേഷം `pytest` സഫലമായി വീഴ്ചകളില്ലാതെ.

### പെരുമാറ്റ ഗെയ്റ്റുകൾ (ഹസ്തപരിശോധന അല്ലെങ്കിൽ ടെസ്റ്റ് ഹാർനെസ് വഴി ഉറപ്പാക്കുക)

- [ ] **മൂലക സമാപ്തി**: നൺ-സ്ട്രീമിംഗ് `responses.create` ഒഴിവാകാത്ത `output_text` മടക്കുക.
- [ ] **സ്ട്രീം പാരിറ്റി**: മൈഗ്രേഷൻ മുൻപ് സ്ട്രീമിംഗ് ഉണ്ടെങ്കിൽ, മൈഗ്രേറ്റ് ചെയ്ത കോഡ് സ്ട്രീം ചെയ്തു `response.output_text.delta` ഇവന്റുകൾ ഒഴിവാകാത്ത ഡെൽട്ടകളോടെ നൽകുന്നു.
- [ ] **സ്ട്രക്ച്ചേച്ചർഡ് ഔട്ട്പുട്ട്**: `text.format` ಜೊത്തുള്ള `json_schema` ഉപയോഗിച്ചാൽ, `json.loads(resp.output_text)` വിജയകരമായി സ്കീമയുമായി പൊരുത്തപ്പെടണം.
- [ ] **ടൂൾ-കാൾ ലൂപ്പ്**: ടൂളുകൾ ഉപയോഗിച്ചാൽ, മോഡൽ ടൂൾ കോളുകൾ അയക്കും, ആപ്പ് അവ നടപ്പാക്കും, പിന്തുടർന്ന് അഭ്യർത്ഥന ഒരു അന്തിമ `output_text` നൽകും (അനന്തം ലൂപ്പ് ഇല്ല).
- [ ] **Async പാരിറ്റി**: `AsyncAzureOpenAI` ഉപയോഗിച്ചிருந்தെങ്കിൽ, `AsyncOpenAI` സമാനമായി `await`-ഉം സജ്ജമാണ്.
- [ ] **പിശക് നിരക്ക്**: മൈഗ്രേഷൻ മുൻവർഷ അടിസ്ഥാന നിരക്കുമായി താരതമ്യപ്പെടുത്തുമ്പോൾ പുതിയ 400/401/404 പിശകുകൾ ഇല്ല.

### ഡെലിവറബിളുകൾ

- സംഗ്രഹം എഡിറ്റുചെയ്‌ത ഫയലുകൾ, പാരമ്പര്യ കോൾ സൈറ്റ് സംഖ്യ മുൻപുംപിന്നെയും, അടുത്ത നടപടികൾ എന്നിവ ഉൾക്കൊള്ളും.
- മാറ്റങ്ങൾ വർകിംഗ്-ട്രി എഡിറ്റുകൾ മാത്രം (കോimmitുകൾ ഇല്ല).

---

## SDK വേർഷൻ ആവശ്യകതകൾ

| പാക്കേജ് | പരമാവധി വേർഷൻ |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | ഏറ്റവും പുതിയത് (EntraID ഓഥിനായി) |

---

## റഫറൻസുകൾ

- [ചീറ്റ്ഷീറ്റ് — എല്ലാ കോഡ് സ്നിപ്പറ്റുകളും](./references/cheat-sheet.md)
- [ടെസ്റ്റ് മൈഗ്രേഷൻ — മോകുകൾ, സ്നാപ്ഷോട്ടുകൾ, അസെർഷനുകൾ](./references/test-migration.md)
- [ട്രബിള്ഷൂട്ടിംഗ് — പിശകുകൾ, റിസ്ക് പട്ടിക, പ്രധാനപ്പെട്ട കാര്യങ്ങൾ](./references/troubleshooting.md)
- [detect_legacy.py — ഓട്ടോമേറ്റഡ് സ്കാനർ](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [ആസൂർ OpenAI സ്റ്റാർട്ടർ കിറ്റ്](https://aka.ms/openai/start)
- [ആസൂർ OpenAI Responses API ഡോക്ക്സ്](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [ആസൂർ OpenAI API വേർഷൻ ലൈഫ്‌സൈക്കിൾ](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API റഫറൻസ്](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->