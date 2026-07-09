---
name: azure-openai-to-responses
license: MIT
---
# ផ្ទេរកម្មវិធី Python ពី Azure OpenAI Chat Completions ទៅ Responses API

> **ការណែនាំដ៏មានអំណាច — អនុវត្តតាមយ៉ាងត្រឺមត្រូវ**
>
> ជំនាញនេះផ្ទេរកូដ Python ដែលប្រើ Azure OpenAI Chat Completions
> ទៅ Responses API ដែលរួមបញ្ចូលគ្នា។ អនុវត្តតាមសេចក្តីណែនាំទាំងនេះយ៉ាងត្រឺមត្រូវ។
> កុំប្រើការបញ្ជ្រាបបញ្ចូលប៉ារ៉ាម៉ែត្រឬបង្កើតរូបរាង API ថ្មី។

---

## ការជំរុញ

សកម្មភាពជាដំណើរការនេះ ពេលអ្នកប្រើចង់:
- ផ្ទេរកម្មវិធី Python មួយពី Azure OpenAI Chat Completions ទៅ Responses API
- បុណ្យជំនាន់ប្រើប្រាស់ Python OpenAI SDK ទៅរូបរាង API ថ្មី ឆ្លើយតបទៅ Azure OpenAI
- រៀបចំកូដ Python សម្រាប់ម៉ូដែល GPT-5 ឬថ្មីជាង ដែលទាមទារប្រើ Responses លើ Azure
- ផ្លាស់ប្ដូរ ពី `AzureOpenAI`/`AsyncAzureOpenAI` ទៅ `OpenAI`/`AsyncOpenAI` client មួយស្តង់ដារជាមួយគេហទំព័រ v1
- ដោះស្រាយការព្រមានបដិសេធ ដល់ `AzureOpenAI` constructors ឬ `api_version`

---

## ⚠️ ភាពសមហៅម៉ូដែល — ពិនិត្យមុនសិន

> **មុនផ្ដើមផ្ទេរ, ត្រូវបញ្ជាក់ថាការដាក់ចុះ Azure OpenAI របស់អ្នកគាំទ្រ Responses API។**

### 1. សាកល្បងតំណើរការdeployment (រហ័សបំផុត)

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

> **ចំណាំ**: `max_output_tokens` មាន **អប្បបរមា 16** លើ Azure OpenAI។ តម្លៃតិចជាង 16 នឹងបញ្ចូនកំហុស 400។ ប្រើ 50+ សម្រាប់សាកល្បង។

បើវាគេបញ្ចូនកំហុស 404, ម៉ូដែល deployment មិនគាំទ្រ Responses យ៉ាងទូលំទូលាយទេ — សូមពិនិត្យយោងខាងក្រោមឬប្តូរឱ្យមានម៉ូដែលគាំទ្រ។

### 2. ពិនិត្យម៉ូដែលមាននៅក្នុងតំបន់របស់អ្នក (ណែនាំ)

ប្រើឧបករណ៍សមហៅម៉ូដែលដែលបានសាងសង់រួច ដើម្បីមើលថាម៉ូដែលណាដែលគាំទ្រ Responses API ក្នុងតំបន់ឡើងវិញជាក់លាក់របស់អ្នក៖

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

វាស្នើសុំតាម Azure ARM បន្តរហ័ស និងបង្ហាញពហុកោណភាពសមហៅម៉ូដែល — ម៉ូដែលណាដែលគាំទ្រ Responses, បញ្ចេញចេញមានរចនាសម្ព័ន្ធ, ឧបករណ៍ ជាដើម។ ប្រើ `--filter gpt-5.1,gpt-5.2` ដើម្បីជម្រាបលទ្ធផលឬ `--json` សម្រាប់ script។

### 3. ឯកសារពេញលេញសម្រាប់ការគាំទ្រម៉ូដែល

- **ស្នើសុំក្នុងរយៈពេលបច្ចុប្បន្ន**: `python migrate.py models` (មើលខាងលើ — តំបន់ជាក់លាក់, ថ្មីៗជានិច្ច)
- **រុករកភាពមាន**: [តារាងសង្ខេបម៉ូដែល និងភាពមានតំបន់](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **ការចាប់ផ្ដើមរហ័ស & នីតិវិធី**: **https://aka.ms/openai/start**

### ⚠️ ការកំណត់កម្លាំងម៉ូដែលចាស់ៗ

> **ប្រយ័ត្ន**: ម៉ូដែលចាស់ៗ (ឧ. `gpt-4o`, `gpt-4`) ប្រហែលមិនគាំទ្រជំពូកនូវមុខងារ Responses API ទាំងមូល។
>
> ការកំណត់កម្លាំងដែលបានចេះបញ្ចេញជាមួយម៉ូដែលចាស់ៗ:
> - **ប៉ារ៉ាម៉ែត្រ `reasoning`**: មិនគាំទ្រលើ `gpt-4o-mini`, `gpt-4o` និងម៉ូដែលមិន reasoning ជាច្រើនទេ។ ផ្ទេរប៉ារ៉ាម៉ែត្រ `reasoning` បើមានរួចនៅក្នុងកូដដើមតែប៉ុណ្ណោះ។
> - **ប៉ារ៉ាម៉ែត្រ `seed`**: មិនគាំទ្រនៅ Responses API ទាំងស្រុង — លុបចេញពីសំណើទាំងអស់។
> - **ផលបញ្ចេញមានរចនាសម្ព័ន្ធតាម `text.format`**: ម៉ូដែលចាស់ៗប្រហែលមិនស្តាំស្តាប់ `strict: true` JSON schemas យ៉ាងម៉ឺងម៉ាត់។
> - **ការរៀបចំឧបករណ៍**: GPT-5+ រៀបចំការហៅឧបករណ៍ជាផ្នែកនៃវិចារណកថាផ្ទៃក្នុង។ ម៉ូដែលចាស់ៗនៅ Responses នៅតែដំណើរការប៉ុន្តែមិនមានការអង្គការជ្រាលជ្រៅនេះ។
> - **ការកំណត់សីតុណ្ហភាព**: ពេលផ្ទេរទៅ `gpt-5`, សីតុណ្ហភាពត្រូវតែបោះបង់ឬកំណត់ជា `1`។ ម៉ូដែលចាស់ៗមិនមានការបំប៉ននេះ។

### ម៉ូដែល reasoning ជួរដើម O-series (o1, o3-mini, o3, o4-mini)

ម៉ូដែលជួរដើម O-series មានការកំណត់ប៉ារ៉ាម៉ែត្រពិសេសមួយចំនួន។ នៅពេលផ្ទេរកម្មវិធីដែលផ្ទាល់មកម៉ូដែលជួរនេះ:

- **`temperature`**: ត្រូវតែនៅ `1` (ឬមិនមាន). ម៉ូដែល O-series មិនទទួលតម្លៃផ្សេងទេ។
- **`max_completion_tokens` → `max_output_tokens`**: កម្មវិធីប្រើ `max_completion_tokens` ជាពិសេសរបស់ Azure ត្រូវផ្លាស់ទៅ `max_output_tokens`។ កំណត់តម្លៃខ្ពស់ (4096+) ព្រោះ reasoning tokens គណនាថ្នាក់ការកំណត់។
- **`reasoning_effort`**: ប្រសិនបើយើងប្រើ `reasoning_effort` (ទាប/មធ្យម/ខ្ពស់), រក្សាទុកវា — Responses API គាំទ្រប៉ារ៉ាម៉ែត្រ​នេះសម្រាប់ម៉ូដែល O-series។
- **អាកប្បកិរិយាស្ទ្រីមមេ**: ម៉ូដែល O-series ប្រហែលតម្រៀបចេញសាច់ប្រាក់រហូតដល់ reasoning បញ្ចប់ មុនបញ្ចេញព្រឹត្តិការណ៍ delta អត្ថបទ। ស្ទ្រីមមិនមានបញ្ហា, ប៉ុន្តែ `response.output_text.delta` ដំបូងអាចមកយឺតជាងម៉ូដែល GPT។
- **`top_p`**: មិនគាំទ្រលើ O-series — លុបចេញបើមាន។
- **ការប្រើប្រាស់ឧបករណ៍**: ម៉ូដែល O-series គាំទ្រឧបករណ៍តាម Responses API ដូចម៉ូដែល GPT ប៉ុន្តែគុណភាពការអង្គការហៅឧបករណ៍ខុសគ្នាដោយម៉ូដែល។

**សកម្មភាព — ណែនាំម៉ូដែលជាមុនមុខ**: នៅដំណាក់កាលស្កេន, ពិនិត្យមើលម៉ូដែលដែលកម្មវិធីដាក់ពាក្យបណ្ដាញ (ឈ្មោះ deployment, អថិជន env, ការកំណត់ config)។ បើម៉ូដែលគឺ `gpt-4o` ឬចាស់ជាង (មិនមែន gpt-4.1+) ប្រាប់អ្នកប្រើជាមុន:
- ការផ្លាស់ប្ដូរកម្មវិធីនឹងដំណើរការសម្រាប់អត្ថបទមូលដ្ឋាន, ជជែក, ស្ទ្រីម, និងឧបករណ៍លើម៉ូដែលបច្ចុប្បន្ន។
- ម៉ូដែលថ្មីជាង (`gpt-5.1`, `gpt-5.2`) ផ្ដល់នូវការអង្គការឧបករណ៍ល្អ, ការបង្ខំចេញមានរចនាសម្ព័ន្ធ, reasoning និងភាពមាននៅក្នុងតំបន់ជាច្រើន។
- ពួកគេគួរប្រញាប់ប្រាប់ការបង្កើនការដាក់ពាក្យបណ្ដាញរបស់ពួកគេពេលត្រៀម — វាមិនបិទការផ្ទេរនោះទេ។

កុំបិទឬបដិសេធការផ្ទេរដោយផ្អែកលើកំណែម៉ូដែល។ ការណែនាំគឺសម្រាប់ព័ត៌មាន។

### GitHub Models មិនគាំទ្រ Responses API ទេ

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) មិនគាំទ្រ Responses API។**

បើកូដមានបណ្តោយកូដ GitHub Models (ស្វែងរក `base_url` ទៅ `models.github.ai` ឬ `models.inference.ai.azure.com`), **លុបទាំងស្រុង** នៅពេលផ្ទេរ។ Responses API ត្រូវការ Azure OpenAI, OpenAI, ឬក៏ច្រកសោតំបន់ដូចតំបន់ Ollama ដែលគាំទ្រ Responses។

សកម្មភាពក្នុងដំណាក់កាលស្កេន:
- សម្គាល់បណ្តោយកូដ GitHub Models សម្រាប់លុបចេញ។

---

## ការផ្ទេរស៊ារ

កម្មវិធីជាច្រើនប្រើបរិដ្ឋានកម្រិតខ្ពស់លើ OpenAI។ នៅពេលផ្ទេរទាំងនេះ, API របស់បរិដ្ឋានផ្ទាល់ខ្លួនផ្លាស់ប្ដូរ — មិនមែនតែការហៅ OpenAI ខាងក្រោមទេ។

### Microsoft Agent Framework (MAF)

**ពិនិត្យកំណែ MAF របស់អ្នកមុនសិន** — ការផ្ទេរគឺអាស្រ័យលើថាតើអ្នកនៅលើ MAF 1.0.0+ ឬមុន 1.0.0 beta/rc។

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **បានប្រើ Responses API ប្រហែល** — មិនចាំបាច់ផ្ទេរទេ។ ប្រសិនបើកូដប្រើ legacy `OpenAIChatCompletionClient` (ប្រើ `chat.completions.create`), ប្តូរទៅ `OpenAIChatClient`។

| មុន | បន្ទាប់ |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

ដើម្បីពិនិត្យកំណែ: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"` 

#### MAF មុន 1.0.0 (beta/rc)

នៅក្នុង MAF មុន 1.0.0, `OpenAIChatClient` ប្រើ Chat Completions។ កែលម្អទៅ `agent-framework-openai>=1.0.0` ដែល `OpenAIChatClient` ប្រើ Responses API ដោយលំនាំដើម។

គ្មានការផ្លាស់ប្តូរផ្សេងទៀត — API `Agent` និងឧបករណ៍នៅដដែល។

### LangChain (`langchain-openai`)

បន្ថែម `use_responses_api=True` ទៅ `ChatOpenAI()`។ ក៏បញ្ចូលការចូលប្រើចម្លើយ ពី `.content` ទៅ `.text`។

| មុន | បន្ទាប់ |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

សម្រាប់ឧទាហរណ៍កូដពេញលេញមុន/បន្ទាប់ សូមមើល [cheat-sheet.md](./references/cheat-sheet.md)។

---

## គន្លឹះការផ្ទេរពីខាងមុខ (Frontend) 

> **Responses API គឺជាបញ្ហាសម្រាប់ផ្នែកម៉ាស៊ីនបម្រើ (server-side)។** ផ្ទេរផ្នែក backend Python របស់អ្នក; សេវាកម្ម HTTP ខាងមុខគួរតែគ្មានការផ្លាស់ប្ដូរឡើយ លុះត្រាទេ ប្រសិនបើ backend របស់អ្នកគឺផ្ទាត់តួការហៅ — ក្នុងករណីនោះ, ពិចារណាទទួលយករូបរាងសំណើ Responses ដើម្បីបញ្ចប់ជំហានបកប្រែ។ ប្រសិនបើ frontend ហៅ OpenAI ដោយប្រើកូនសោ client-side, បញ្ជូនការហៅទាំងនោះទៅ backend ជាមុន។

### ការបន្សល់ទុក `@microsoft/ai-chat-protocol`

កញ្ចប់ `@microsoft/ai-chat-protocol` npm ត្រូវបានបដិសេធ និងគួរត្រូវបានជំនួសដោយ [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream)។ ប្រសិនបើបានឃើញវានៅ frontend:

1. ជំនួស tag ស្គ្រីប CDN៖
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. លុបការបង្កើត `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`)។
3. ជំនួស `client.getStreamedCompletion(messages)` ជាមួយការហៅ `fetch()` ផ្ទាល់ទៅ backend streaming endpoint។
4. ជំនួស `for await (const response of result)` ជាមួយ `for await (const chunk of readNDJSONStream(response.body))`។
5. តម្រូវការចូលទៅគុណលក្ខណៈ ពី `response.delta.content` / `response.error` ទៅ `chunk.delta.content` / `chunk.error`។

---

## គោលបំណង

- រាប់គ្រប់កន្លែងហៅ Python ប្រើ Chat Completions ឬ legacy Completions ទល់ Azure OpenAI។
- ផ្តល់គម្រោងផ្ទេរនិងលំដាប់សម្រាប់កូដ Python។
- អនុវត្តការកែប្រែផ្នែកតូចៗ និងមានសុវត្ថិភាព ដើម្បីប្តូរទៅ Responses API។
- បច្ចុប្បន្នភាពអ្នកហៅដើម្បីប្រើរចនាសម្ព័ន្ធលទ្ធផល Responses; គ្មានការអាប់រកូដរវាងកំណត់។
- បាញ់តេស្ត/ការត្រួតពិនិត្យ; ដោះស្រាយកំហុសតូចៗដែលបង្ករដោយការផ្ទេរ។
- រៀបចំកំណែដែលតូច ងាយធ្វើការពិនិត្យ ហើយផ្តល់សង្ខេបចុងក្រោយជាមួយភាពខុសគ្នា (កុំ commit)។

---

## ការការពារ

- តែផ្លាស់ប្ដូរក្នុងឯកសារខាងក្នុង workspace git ទេ។ កុំសរសេរទៅក្រៅ។
- កុំរក្សាភាពត្រង់តាមរយៈ backward-compatible shims; ផ្ទេរកូដទៅរូបរាង API ថ្មី។
- កុំទុកមតិកំពុងផ្លាស់ប្ដូរ ឬឯកសារបម្រុងទុក។
- រក្សាភាពមានអត្ថន័យក្នុងការស្ទ្រីមបើត្រូវបានប្រើពីមុនមក; បើមិនទេប្រើមិនស្ទ្រីម។
- សុំយល់ព្រមមុនរត់ពាក្យបញ្ជាទាំងឡាយ ឬហៅបណ្តាញបើនៅក្នុងរបៀបយល់ព្រម។
- កុំរត់ `git add`/`git commit`/`git push`; បង្កើតការផ្លាស់ប្ដូរជាការងារតែមួយ។

---

## ជំហាន 0: ផ្ទេរអតិថិជន Azure OpenAI (លក្ខខណ្ឌមុន)

ប្រសិនបើកូដប្រើ constructors `AzureOpenAI` ឬ `AsyncAzureOpenAI`, ផ្លាស់ទៅ `OpenAI` / `AsyncOpenAI` តាមរយៈ constructors ស្តង់ដារមុន។ Constructors មួយចំនួនជាពិសេស Azure ត្រូវបានបដិសេធនៅ `openai>=1.108.1`។

### ហេតុអ្វីបានជា ផ្លូវចូល API v1?

ច្រកថ្មី `/openai/v1` ប្រើ `OpenAI()` client stំយ៉ោងផ្ទាល់ពេល `AzureOpenAI()`, មិនត្រូវការ parameter `api_version`, និងដំណើរការដូចគ្នា លើ OpenAI និង Azure OpenAI។ កូដ client ដូចគ្នានេះមានភាពរឹងមាំនាពេលអនាគត — មិនមានការគ្រប់គ្រងកំណែទេ។

### ការផ្លាស់ប្ដូរចម្បង

| មុន | បន្ទាប់ |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | លុបចេញសព្វនៅទាំងមូល |

### បញ្ជីរៀបចំសំណុំ

- លុប argument `api_version` ពីការបង្កើត client។
- លុបអថិជនបរិស្ថាន `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` ពី `.env`, app settings, និងឯកសារ Bicep/infra។
- ប្តូរឈ្មោះ `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` នៅ `.env`, app settings, Bicep/infra, និង test fixtures (តាមរយៈប្រព័ន្ធសម្របសម្រួល Azure Identity SDK)។
- ធានា `openai>=1.108.1` នៅក្នុង `requirements.txt` ឬ `pyproject.toml`។

### ផ្ទេរអថិជនបរិស្ថាន

| អថិជនបរិស្ថានចាស់ | សកម្មភាព | ចំណាំ |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **លុប** | មិនចាំបាច់មាន `api_version` ជាមួយច្រក v1 |
| `AZURE_OPENAI_API_VERSION` | **លុប** | ដូចគ្នាខាងលើ |
| `AZURE_OPENAI_CLIENT_ID` | **ប្តូរឈ្មោះ** → `AZURE_CLIENT_ID` | ប្រព័ន្ធ Azure Identity SDK សម្រាប់ `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **រក្សាទុក** | នៅត្រូវការ សម្រាប់បង្កើត `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **រក្សាទុក** | ប្រើជារ៉េបីង `model` ក្នុង `responses.create` |
| `AZURE_OPENAI_API_KEY` | **រក្សាទុក** | ប្រើជា `api_key` សម្រាប់អនុញ្ញាតដោយ key |

សម្រាប់ឧទាហរណ៍កូដការតំឡើង client (sync, async, EntraID, API key, multi-tenant), សូមមើល [cheat-sheet.md](./references/cheat-sheet.md)។

---

## ជំហាន 1: ពិនិត្យកន្លែងហៅ legacy

រត់ script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) ដើម្បីស្វែងរកគ្រប់កន្លែងហៅដែលត្រូវការផ្លាស់ប្ដូរ:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

ឬរត់ស្វែងរកទាំងនេះដោយដៃ — គ្រប់ការចងក្រងគឺជាគោលដៅផ្ទេរ:

```bash
# ការហៅ API ចាស់ (ត្រូវសរសេរឡើងវិញ)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# តំណាងអតីត Azure client (ត្រូវប្ដូរ)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# លំនាំចូលដំណើរការឆ្លើយតប (ត្រូវអាប់ដេត)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# សេចក្ដីកំណត់ឧបករណ៍ក្នុងទ្រង់ទ្រាយច្របល់ចាស់ (ត្រូវបញ្ច្រាស)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# លទ្ធផលឧបករណ៍ក្នុងទ្រង់ទ្រាយចាស់ (ត្រូវបំលែងទៅ function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# ប៉ារ៉ាម៉ែត្រចាស់ (ត្រូវដកចេញ ឬប្ដូរឈ្មោះ)
rg "response_format"
rg "max_tokens\b"        # ប្ដូរឈ្មោះទៅ max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# បរិស្ថានថេរDeprecated (ត្រូវសំអាត)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # គួរតែជា AZURE_CLIENT_ID

# ចំណុចបញ្ចប់ម៉ូដែល GitHub (ត្រូវដកចេញ — មិនគាំទ្រ API Responses)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# លំនាំវេទិកាចាស់ (ត្រូវអាប់ដេត)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: ប្ដូរជា OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: ត្រូវការប្រើ use_responses_api=True

# គម្រោងសាកល្បង (ត្រូវអាប់ដេត)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# ការចូលដំណើរការរចនាសម្ព័ន្ធកំហុសចម្រាញ់មាតិការជាថ្មី (ត្រូវអាប់ដេត — រចនាសម្ព័ន្ធបានផ្លាស់ប្តូរ)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # ទម្រង់ចាស់ឯក (បច្ចុប្បន្ន content_filter_results (ភាគពាស) នៅក្នុងថ្នាក់ content_filters)

# ការហៅ HTTP ដើមទៅចំណុចបញ្ចប់ Chat Completions (ត្រូវបម្លែង URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### គន្លឹះ (ពិនិត្យនិងសរសេរឡើងវិញ)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`។

- **Azure client constructors**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Tools**: បម្លែងការកំណត់ឧបករណ៍ហៅមុខងារពីទ្រង់ទ្រាយជ្រុលជ្រៅ (`{"type": "function", "function": {"name": ...}}`) ទៅទ្រង់ទ្រាយ Responses ខ្ពស់ (`{"type": "function", "name": ...}`); ប្រើ `tool_choice`; ត្រឡប់លទ្ធផលឧបករណ៍ជា ឥឡូវជា`{"type": "function_call_output", "call_id": ..., "output": ...}` (មិនមែន `{"role": "tool", ...}` ទេ)។
- **Tool round-trips**: ពេលម៉ូដែលបញ្ចេញការហៅមុខងារ ភ្ជាប់ធាតុ `response.output` ទៅក្នុងការសន្ទនា (មិនមែន dict ដាក់ដោយដៃ `{"role": "assistant", "tool_calls": [...]}`) បន្ទាប់ពីនោះភ្ជាប់ធាតុ `function_call_output` សម្រាប់លទ្ធផលនីមួយៗ។
- **Few-shot tool examples**: ប្រសិនបើការសន្ទនាមានឧទាហរណ៍ហៅឧបករណ៍ចងក្រងជាមុន បម្លែងទៅជា `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`។ អត្តសញ្ញាណត្រូវចាប់ផ្តើមជាមួយ `fc_`។
- **`pydantic_function_tool()`**: ជំនួយនេះនៅតែបង្កើតទ្រង់ទ្រាយជ្រុលជ្រៅចាស់ហើយ **មិនសមស្រប** ជាមួយ `responses.create()` ទេ។ ជំនួសដោយការកំណត់ឧបករណ៍ដោយដៃ ឬប្រអប់ដោះស្រាយការបញ្ចូល។
- **Multi-turn**: រក្សាប្រវត្តិសន្ទនាក្នុងកម្មវិធី; ផ្ញើរ​ជំហាន​មុនតាមរយៈធាតុ `input`។
- **Formatting**: ជំនួស `response_format` កំពូល Chat ជា `text.format` ក្នុង Responses។ រូបរាងធម្មតា៖ `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`។
- **Content items**: ជំនួស Chat `content[].type: "text"` ជា Responses `content[].type: "input_text"` សម្រាប់ជំហានអ្នកប្រើ/ប្រព័ន្ធ។
- **Image content items**: ជំនួស Chat `content[].type: "image_url"` ជា Responses `content[].type: "input_image"`។ វាល `image_url` ផ្លាស់ប្តូរពីអOBJECT ជ្រុលជ្រៅ `{"url": "..."}` ទៅខ្សែអក្សរខ្លួនឯង។ មើលតារាង cheat sheet សម្រាប់ឧទាហរណ៍មុន/ក្រោយ។
- **Reasoning effort**: **តែផ្ទេរពី `reasoning` ប៉ុណ្ណោះ ប្រសិនបើវាមានរួចហើយក្នុងកូដដើម**។
- **Content filter error handling**: រចនាសម្ព័ន្ធរាងកាយកំហុសបានផ្លាស់ប្តូរ។ Chat Completions ប្រើ `error.body["innererror"]["content_filter_result"]` (វត្ថុទ едидཅራយ); Responses API ប្រើ `error.body["content_filters"][0]["content_filter_results"]` (បណ្ដាល, នៅក្នុងអារ័យ)។ កូដដែលចូលដំណើរការ `innererror` នឹងបណ្តាលឲ្យកើត `KeyError`។ សរសេរឡើងវិញដើម្បីប្រើផ្លូវថ្មី។
- **Raw HTTP calls**: ប្រសិនបើកម្មវិធីហៅ Azure OpenAI REST API ត្រង់ (ឧ. `requests`, `httpx`) ដោយប្រើ `/openai/deployments/{name}/chat/completions?api-version=...`, សរសេរឡើងវិញទៅ `/openai/v1/responses`។ រូបរាងរាងកាយការស្នើរ​ផ្លាស់ប្តូរ៖ `messages` → `input` ហើយបន្ថែម `max_output_tokens` និង `store: false`, លុប `api-version` query param។ រូបរាងរាងកាយការឆ្លើយតបផ្លាស់ប្តូរ៖ `choices[0].message.content` → `output[0].content[0].text` (ចំណាំ៖ `output_text` ជាលក្ខណៈងាយស្រួលនៅ SDK មិនមាននៅ raw REST JSON)។

---

## ជំហានទី ២: អនុវត្តការផ្លាស់ទី

### សម្គាល់ការផ្លាស់ទី (Chat Completions → Responses)

- **ហេតុផលបង្រ្កាប**: Responses គឺជា API មួយរួមសម្រាប់អត្ថបទ ឧបករណ៍ និងការចាក់បញ្ចាំង; Chat Completions គឺជាដែលមានប្រវត្ដិអតីត។ ជាមួយ GPT-5, Responses ត្រូវបានទាមទារ សម្រាប់ប្រសិទ្ធិភាពខ្ពស់បំផុត។
- **HTTP**: ចុងផ្លូវ Azure ប្តូរពី `/openai/deployments/{name}/chat/completions` ទៅ `/openai/v1/responses`។
- **វាល**: `messages` → `input`, `max_tokens` → `max_output_tokens`។ `temperature` មិនផ្លាស់ប្តូរ។
- **Formatting**: `response_format` → `text.format` ជាមួយវត្ថុដំណើរការ។
- **Content items**: ជំនួស Chat `content[].type: "text"` ជា Responses `content[].type: "input_text"` សម្រាប់ជំហានប្រព័ន្ធ/អ្នកប្រើ។
- **Image content items**: ជំនួស Chat `content[].type: "image_url"` ជា Responses `content[].type: "input_image"`។ បត់បែនវាល `image_url` ពី `{"image_url": {"url": "..."}}` ទៅ `{"image_url": "..."}` (ខ្សែអក្សរតែមួយ — អាចជ URL HTTPS ឬ URI ទិន្នន័យ `data:image/...;base64,...`)។

### ឯកសារអំពីតារាងផ្លាស់ទីប៉ារ៉ាម៉ែត្រ

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (អារេនៃធាតុ) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (វត្ថុ) |
| `temperature` | `temperature` (មិនផ្លាស់ប្តូរ) |
| `stop` | `stop` (មិនផ្លាស់ប្តូរ) |
| `frequency_penalty` | `frequency_penalty` (មិនផ្លាស់ប្តូរ) |
| `presence_penalty` | `presence_penalty` (មិនផ្លាស់ប្តូរ) |
| `tools` / function-calling | `tools` (មិនផ្លាស់ប្តូរ) |
| `seed` | **យកចេញ** (មិនគាំទ្រ) |
| `store` | `store` (កំណត់ជា `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ខ្សែអក្សរស្រួល) |

សម្រាប់ឧទាហរណ៍កូដពេញលេញ មុន និងបន្ទាប់ សូមមើល [cheat-sheet.md](./references/cheat-sheet.md)។

សម្រាប់ការផ្លាស់ទីបណ្តាញសាកល្បង (mocks, snapshots, assertions), សូមមើល [test-migration.md](./references/test-migration.md)។

សម្រាប់ដោះស្រាយកំហុស និងបញ្ហាផ្សេងៗ សូមមើល [troubleshooting.md](./references/troubleshooting.md)។

---

## ការរក្សាទុកទិន្នន័យ និងស្ថានភាព

- កំណត់ `store: false` លើការស្នើរ Responses ទាំងអស់។
- មិនពឹងផ្អែកលើអត្តសញ្ញាណសារមុន ឬបទបញ្ជាទន់ដែលរក្សាទុកដោយម៉ាស៊ីនមេ; រក្សាស្ថានភាពដោយអតិថិជនគ្រប់គ្រង និងបង្រួមMetadata។

---

## លក្ខខណ្ឌទទួលយក

### ច្រកកូដ (ត្រូវឆ្លងទាំងអស់)

- [ ] មិនមានតំណក្រងសម្រាប់ `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` នៅក្នុងឯកសារផ្លាស់ទី។
- [ ] មិនមានតំណក្រងសម្រាប់ `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — គ្រប់ constructor ប្រើ `OpenAI`/`AsyncOpenAI` ជាមួយចុងផ្លូវ v1។
- [ ] មិនមានតំណក្រងសម្រាប់ `rg "models\.github\.ai|models\.inference\.ai\.azure"` — ផ្លូវកូដ GitHub Models ត្រូវបានដកចេញ។
- [ ] មិនមានតំណក្រងសម្រាប់ `rg "OpenAIChatCompletionClient"` — កូដ MAF 1.0.0+ ប្រើ `OpenAIChatClient` (ដែលប្រើ Responses API)។ នៅមុន 1.0.0, ធ្វើឲ្យថ្មីទៅ `agent-framework-openai>=1.0.0`។
- [ ] ការហៅ `ChatOpenAI(...)` ទាំងអស់ មាន `use_responses_api=True`។
- [ ] មិនមានតំណក្រងសម្រាប់ `rg "choices\[0\]"` — ការចូលដំណើរការឆ្លើយតបទាំងអស់ប្រើ `resp.output_text` ឬ schema ផលប៉ះពាល់ Responses។
- [ ] គ្មាន `response_format` នៅកម្រិតកំពូល; ផលប៉ះពាល់ដែលមានរចនាប័ទ្មទាំងអស់ប្រើ `text={"format": {...}}`។
- [ ] មាន `openai>=1.108.1` និង `azure-identity` នៅក្នុង `requirements.txt` ឬ `pyproject.toml`; ការគ្រប់គ្រងផ្នែក依赖បានធ្វើឡើងវិញ។
- [ ] កំណត់ `store=False` លើការហៅ `responses.create` រាល់ដង។
- [ ] គ្មាន `api_version` នៅក្នុងការបង្កើត client; `AZURE_OPENAI_API_VERSION` ត្រូវបានយកចេញពីឯកសារ env និងឧបករណ៍។

### ច្រកបណ្តាញសាកល្បង (ត្រូវឆ្លងទាំងអស់)

- [ ] មិនមានតំណក្រងសម្រាប់ `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`។
- [ ] មិនមានតំណក្រងសម្រាប់ `rg "_azure_ad_token_provider" tests/` — សេចក្ដីបញ្ជាក់បានផ្លាស់ប្តូរដើម្បីពិនិត្យ `isinstance(client, AsyncOpenAI)` ឬ `base_url`។
- [ ] មិនមានតំណក្រងសម្រាប់ `rg "prompt_filter_results|content_filter_results" tests/` — mocks ភាពជាអ្នកត្រួតពិនិត្យប្រភេទ Azure ត្រូវបានដកចេញ។
- [ ] mock fixture ប្រើ `kwargs.get("input")` មិនមែន `kwargs.get("messages")` ទេ។
- [ ] snapshot / golden files ត្រូវបានធ្វើឲ្យទាន់សម័យទៅរូបរាង streaming Responses (គ្មាន `choices[0]`, `function_call`, `logprobs`, ... )។
- [ ] `pytest` ជោគជ័យដោយគ្មានកំហុសបន្ទាប់ពីហ្វឹកហាត់ទាំងអស់។

### ច្រកអាកប្បកិរិយា (ពិនិត្យដោយដៃ ឬតាមការសាកល្បង)

- [ ] **ការបញ្ចប់មូលដ្ឋាន**: non-streaming `responses.create` ត្រឡប់ `output_text` មិនទទេ។
- [ ] **ភាពស្រដៀងបន្តផ្ទាល់**: ប្រសិនបើកូដដើមប្រើការចាក់បញ្ចាំងជាបន្ត, កូដថ្មីធ្វើការចាក់បញ្ចាំង និងផ្តល់សេចក្ដី `response.output_text.delta` ជាមួយ delta មិនទទេ។
- [ ] **ផលប៉ះពាល់ដែលមានរចនាប័ទ្ម**: ប្រសិនបើប្រើ `text.format` ជាមួយ `json_schema`, `json.loads(resp.output_text)` ជោគជ័យ និងផ្គូផ្គងនឹង schema។
- [ ] **បន្ទាត់ហៅឧបករណ៍**: ប្រសិនបើប្រើឧបករណ៍, ម៉ូដែលធ្វើការហៅឧបករណ៍, កម្មវិធីអនុវត្តន៍ពួកវា, និងសំណើបន្ទាប់ត្រឡប់ `output_text` ចុងក្រោយ (គ្មានរង្វង់អនន្ធ)។
- [ ] **សមភាព Async**: ប្រសិន​បើ​ប្រើ `AsyncAzureOpenAI`, `AsyncOpenAI` ដែលសមនឹងវាធ្វើការដូចគ្នាជាមួយ `await`។
- [ ] **អត្រាកំហុស**: គ្មានកំហុស 400/401/404 ថ្មី ប្រៀបធៀបនឹងមូលដ្ឋានមុនការផ្លាស់ទី។

### ការផ្តល់

- សង្ខេបរួមមានឯកសារដែលបានកែប្រែ ចំនួនស្ថានីយ៍ហៅចាស់ មុន/ក្រោយ និងជំហានបន្ទាប់។
- ការផ្លាស់ប្តូរជាការកែប្រែ Trees នៅក្នុងធ្វើការបត់ច្រាស់ (មិនមែន commit)។

---

## កម្រិតកំណែ SDK ត្រូវការ

| កញ្ចប់ | កំណែអប្បបរមា |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | ថ្មីបំផុត (សម្រាប់អត្តសញ្ញាណ EntraID) |

---

## ឯកសារយោង

- [Cheat Sheet — កូដឧទាហរណ៍ទាំងអស់](./references/cheat-sheet.md)
- [Test Migration — mocks, snapshots, assertions](./references/test-migration.md)
- [Troubleshooting — កំហុស, តារាងហានិភ័យ, បញ្ហារូប](/references/troubleshooting.md)
- [detect_legacy.py — ឧបករណ៍ស្កេនស្វ័យប្រវត្តិ](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [ឯកសារ Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [ជីវប្រវត្តិការបញ្ចេញកំណែ Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [ឯកសារយោង OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->