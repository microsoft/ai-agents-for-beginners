---
name: azure-openai-to-responses
license: MIT
---
# ផ្លាស់ប្តូរកម្មវិធី Python ពី Azure OpenAI Chat Completions ទៅ Responses API

> **ការណែនាំមានសណ្ឋាន — អនុវត្តតាមយ៉ាងម៉ត់ចត់**
>
> ជំនាញនេះបម្រើការផ្លាស់ប្តូរកូដ Python ដែលប្រើ Azure OpenAI Chat Completions
> ទៅ Responses API តែមួយគត់។ សូមអនុវត្តតាមបទបញ្ជាទាំងនេះយ៉ាងម៉ត់ចត់។
> កុំបង្កើតការ​ផ្គូផ្គងអថេរឬបង្កើតរូបរាង API ថ្មីៗឡើយ។

---

## ការផ្ទាំងចាប់ផ្តើម

សកម្មភាពជំនាញនេះនៅពេលដែលអ្នកប្រើប្រាស់ចង់:
- ផ្លាស់ប្តូរកម្មវិធី Python ពី Azure OpenAI Chat Completions ទៅ Responses API
- បន្ថែមការប្រើប្រាស់ Python OpenAI SDK ទៅរូបរាង API ថ្មី ដែលឆ្លošបញ្ចូលជាមួយ Azure OpenAI
- ត្រៀមកូដ Python សម្រាប់ម៉ូដែល GPT-5 ឬថ្មីជាងដែលទាមទារ Responses នៅលើ Azure
- ផ្លាស់ពី `AzureOpenAI`/`AsyncAzureOpenAI` ទៅ client `OpenAI`/`AsyncOpenAI` ផ្លូវការដោយប្រើចំណុចបញ្ចប់ v1
- កែបញ្ហាផ្សព្វផ្សាយថា `AzureOpenAI` constructors ឬ `api_version`

---

## ⚠️ ភាពត្រូវគ្នាសម្រាប់ម៉ូដែល — សូមពិនិត្យជាមុន

> **មុននឹងផ្លាស់ប្តូរ សូមបញ្ជាក់ថាការដំឡើង Azure OpenAI របស់អ្នកគាំទ្រ Responses API។**

### 1. សាកល្បងបឋម (លឿនបំផុត)

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

> **ចំណាំ**: `max_output_tokens` មានតម្លៃតិចបំផុត 16 នៅលើ Azure OpenAI។ តម្លៃក្រោម 16 នឹងបញ្ជូនកំហុស 400។ សូមប្រើ 50 ឬច្រើនសម្រាប់សាកល្បងបឋម។

ប្រសិនបើវាតបណ្ដោយ 404 នោះម៉ូដែលក្នុងការដំឡើងមិនគាំទ្រ Responses ទេ — សូមពិនិត្យប្រភពខាងក្រោម ឬដំឡើងម្តងទៀតជាមួយម៉ូដែលគាំទ្រ។

### 2. ពិនិត្យម៉ូដែលមានក្នុងតំបន់របស់អ្នក (ផ្ដល់អនុសាសន៍)

ដំណើរការឧបករណ៍ត្រួតពិនិត្យភាពត្រូវគ្នារបស់ម៉ូដែលដើម្បីមើលអ្វីមានជាមួយការគាំទ្រ Responses API ក្នុងតំបន់ជាក់លាក់របស់អ្នក៖

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

វាស្វែងរក Azure ARM តាមពេលវេលាពិត និងបង្ហាញម៉ាទ្រីសភាពត្រូវគ្នា — ម៉ូដែលណាដែលគាំទ្រ Responses, ផលប៉ះពាល់សំខាន់ៗ, ឧបករណ៍ជាដើម។ ប្រើ `--filter gpt-5.1,gpt-5.2` ដើម្បីបណ្តុះតម្រុយឬ `--json` សម្រាប់ស្គ្រីប។

### 3. ឯកសារភាពគាំទ្រម៉ូដែលពេញលេញ

- **ស្វែងរកផ្ទាល់**: `python migrate.py models` (មើលខាងលើ — តំបន់ជាក់លាក់ និងទាន់សម័យអស់ពេល)
- **មើលការចេញលក់**: [តារាងសង្ខេបម៉ូដែល និងភាពមានដែនប្រៀប](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **ការចាប់ផ្តើមលឿន & សេចក្ដីណែនាំ**: **https://aka.ms/openai/start**

### ⚠️ កំណត់នៃម៉ូដែលចាស់

> **ការព្រមាន**: ម៉ូដែលចាស់ (ដែលមានមុន `gpt-4.1`) ប្រហែលមិនគាំទ្រពេញលេញលក្ខណៈ Responses API ទេ។
>
> កំណត់ដែលគេស្គាល់ទាក់ទងទៅម៉ូដែលចាស់៖
> - **ប៉ារ៉ាម៉ែត្រ `reasoning`**: មិនគាំទ្រនៅម៉ូដែលមិន reasoning ជាច្រើនទេ។ គ្រាន់តែផ្លាស់ប្តូរ `reasoning` ប្រសិនបើវាមានរួចនៅក្នុងកូដដើម។
> - **ប៉ារ៉ាម៉ែត្រ `seed`**: មិនគាំទ្រនៅ Responses API ទេ — ត្រូវដកចេញពីសំណើទាំងអស់។
> - **លទ្ធផលមានរចនាសម្ព័ន្ធតាម `text.format`**: ម៉ូដែលចាស់ប្រហែលមិនអនុវត្ត JSON schemas `strict: true` យ៉ាងម៉ត់ចត់ទេ។
> - **ការផ្គុងគ្នាឧបករណ៍**: GPT-5+ គ្រប់គ្រងការហៅឧបករណ៍ជាផ្នែកនៃការគិតនៅខាងក្នុង។ ម៉ូដែលចាស់នៅ Responses នៅមុខមុនក៏ដំណើរការបាន ប៉ុន្តែមិនមានការចូលរួមជ្រៅនេះទេ។
> - **កម្រិតសីតុណ្ហភាព**: ពេលផ្លាស់ប្តូរទៅ `gpt-5` តម្លៃសីតុណ្ហភាពត្រូវតែបោះបង់ ឬកំណត់ជា `1`។ ម៉ូដែលចាស់មិនមានកំណត់បែបនេះ។

### ម៉ូដែល reasoning ស៊េរី O (o1, o3-mini, o3, o4-mini)

ម៉ូដែលស៊េរី O មានកំណត់ប៉ារ៉ាម៉ែត្រ ពេលផ្លាស់ប្តូរកម្មវិធីដែលគោលបំណងទៅម៉ូដែលស៊េរី O:

- **`temperature`**: ត្រូវតែជា `1` (ឬករណីមិនប្រើ)។ ម៉ូដែលស៊េរី O មិនទទួលតម្លៃផ្សេងទេ។
- **`max_completion_tokens` → `max_output_tokens`**: កម្មវិធីប្រើ `max_completion_tokens` ជាពិសេសរបស់ Azure ត្រូវប្ដូរទៅ `max_output_tokens`។ កំណត់តម្លៃខ្ពស់ (4096+) ព្រោះ reasoning tokens នឹងរាប់ក្នុងកម្រិតដឹកនាំ។
- **`reasoning_effort`**: ប្រសិនបើកម្មវិធីប្រើ `reasoning_effort` (ទាប/មធ្យម/ខ្ពស់) សូមរក្សាទុក — Responses API គាំទ្រប៉ារ៉ាម៉ែត្រនេះសម្រាប់ម៉ូដែលស៊េរី O។
- **អាកប្បកិរិយាស្ទ្រីម**: ម៉ូដែលស៊េរី O អាចផ្ទុកលទ្ធផលរហូតដល់ការគិតបញ្ចប់មុនផ្ទុកព្រឹត្តិការ delta អត្ថបទ។ ស្ទ្រីមមិនប្រែប្រួល ប៉ុន្តែ `response.output_text.delta` ជាលើកដំបូងប្រហែលមកយឺតជាងម៉ូដែល GPT។
- **`top_p`**: មិនគាំទ្រលើស៊េរី o — ត្រូវដកចេញប្រសិនបើមាន។
- **ការប្រើឧបករណ៍**: ម៉ូដែលស៊េរី O គាំទ្រឧបករណ៍តាម Responses API ដូចម៉ូដែល GPT ប៉ុន្តែគុណភាពការគ្រប់គ្រងការហៅឧបករណ៍ខុសគ្នា។

**សកម្មភាព — ផ្ដល់ដំណឹងជាមុនអំពីម៉ូដែល**: ក្នុងដំណាក់កាលស្កេន ប្រើប្រាស់ដឹងថា ម៉ូដែលកំណត់គោលបំណងកម្មវិធី (ឈ្មោះ deployment, រលកបរិស្ថាន, config) បើម៉ូដែលមុន `gpt-4.1` (មិនមែន gpt-4.1+) សូមប្រាប់អ្នកប្រើប្រាស់ជាមុន:
- ការផ្លាស់ប្តូរនឹងធ្វើការជាមួយអត្ថបទមូលដ្ឋាន, ជជែក, ស្ទ្រីម និងឧបករណ៍លើម៉ូដែលបច្ចុប្បន្ន។
- ម៉ូដែលថ្មី (`gpt-5.1`, `gpt-5.2`) ផ្តល់ជូនការគ្រប់គ្រងឧបករណ៍ល្អប្រសើរ លទ្ធផលមានរចនាសម្ព័ន្ធល្អ ការគិត និងមាននៅតំបន់ជាយថាហេតុ។
- ពួកគេគួរជម្រាបជូនការដំឡើងរបស់ពួកគេនៅពេលដែលពេញចិត្ត — វាមិនរាំងស្ងើចការផ្លាស់ប្តូរទេ។

កុំរាំងស្ងើច ឬបដិសេធការផ្លាស់ប្តូរដោយផ្អែកលើកំណែម៉ូដែលទេ។ ការណែនាំនេះគ្រាន់តែជាសេចក្ដីជ្រាបតែប៉ុណ្ណោះ។

### ម៉ូដែល GitHub មិនគាំទ្រ Responses API

> **ម៉ូដែល GitHub (`models.github.ai`, `models.inference.ai.azure.com`) មិនគាំទ្រ Responses API ទេ។**

ប្រសិនបើកូដដើមមានផ្លូវលេខ GitHub Models (មើល `base_url` បង្ហាញទៅ `models.github.ai` ឬ `models.inference.ai.azure.com`), **លុបទាំងស្រុង** ពេលផ្លាស់ប្តូរ។ Responses API ត្រូវប្រើ Azure OpenAI, OpenAI, ឬចំណុចបញ្ចប់មូលដ្ឋានសមស្រប (ឧ. Ollama មានការគាំទ្រ Responses)។

សកម្មភាពនៅពេលស្កេន:
- សម្គាល់ផ្លូវលេខកូដ GitHub Models សម្រាប់លុបចេញ។

---

## ការផ្លាស់ប្តូរគ្រឹះសម្ព័ន្ធ

កម្មវិធីជាច្រើនប្រើ framework ដាន់ខ្ពស់លើ OpenAI។ ពេលផ្លាស់ប្តូរទាំងនេះ ការផ្លាស់ប្តូរជាក្នុង API ឯករាជ្យរបស់ framework មិនមែនត្រឹមតែកូដ OpenAI រុំៗទេ។

### Microsoft Agent Framework (MAF)

**ពិនិត្យកំណែ MAF របស់អ្នកមុន** — ការផ្លាស់ប្តូរនេះអាស្រ័យលើថា អ្នកកំពុងប្រើ MAF 1.0.0+ ឬ beta/rc មុន 1.0.0។

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ប្រើ Responses API រួចហើយ** — មិនចាំបាច់ផ្លាស់ប្តូរ។ ប្រសិនបើកូដប្រើ `OpenAIChatCompletionClient` ចាស់ (ប្រើ `chat.completions.create`), ប្ដូរទៅ `OpenAIChatClient`។

| មុន | បន្ទាប់ |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

ដើម្បីពិនិត្យកំណែ៖ `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)" `

#### MAF មុន 1.0.0 (បោះពុម្ព beta/rc)

នៅក្នុង MAF មុន 1.0.0, `OpenAIChatClient` ប្រើ Chat Completions។ ធ្វើបច្ចុប្បន្នភាពទៅ `agent-framework-openai>=1.0.0` ដែល `OpenAIChatClient` ប្រើ Responses API ដោយស្វ័យប្រវត្តិ។

មិនចាំបាច់ផ្លាស់ប្តូរផ្សេងៗទៀត — `Agent` និង API ឧបករណ៍នៅដដែល។

### LangChain (`langchain-openai`)

បន្ថែម `use_responses_api=True` ទៅក្នុង `ChatOpenAI()`។ ក៏បន្ទាន់សម័យការចូលប្រើលទ្ធផលពី `.content` ទៅ `.text`។

| មុន | បន្ទាប់ |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

សម្រាប់ឧទាហរណ៍កូដពេញលេញ មុន/ក្រោយសូមមើល [cheat-sheet.md](./references/cheat-sheet.md)។

---

## គន្លឹះផ្លាស់ប្តូរផ្នែកមុខ

> **Responses API គឺជាបញ្ហាផ្នែកបម្រើ។** សូមផ្លាស់ប្តូរផ្នែកក្រោយ Python របស់អ្នក។ កិច្ចសន្យា HTTP ផ្នែកមុខគួរតែមិនផ្លាស់ប្ដូរទេ លើកលែងតែផ្នែកក្រោយជាផ្នែកឆ្លាតទៅផ្នែកមុខ — ក្នុងករណីនោះ សូមពិចារណាការយករូបរាងសំណើ Responses ដើម្បីបញ្ចប់ជាតទៅជំនួសស្រទាប់បកប្រែ។ ប្រសិនបើផ្នែកមុខហៅ OpenAI ដោយផ្ទាល់ដោយ key មួយផ្នែកមុខ សូមផ្លាស់ប្ដូរហៅទៅផ្នែកក្រោយ ជាចម្បង។

### ការលះបង់ `@microsoft/ai-chat-protocol`

បណ្ដុំនិពន្ធ npm `@microsoft/ai-chat-protocol` លះបង់ និងគួរត្រូវបានជំនួសដោយ [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream)។ ប្រសិនបើអ្នកជួបប្រទៈវានៅផ្នែកមុខ៖

១. ជំនួសតេកដ្ឋាន script CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
 ២. លុបការបង្កើត `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`) ។
៣. ជំនួស `client.getStreamedCompletion(messages)` ជាមួយការហៅ `fetch()` ទៅចំណុចបញ្ចប់ការស្ទ្រីមនៅខាងក្រោយ។
៤. ជំនួស `for await (const response of result)` ជាមួយ `for await (const chunk of readNDJSONStream(response.body))`។
៥. អាប់ដេតការចូលប្រើគុណភាពពី `response.delta.content` / `response.error` ទៅ `chunk.delta.content` / `chunk.error`។

---

## គោលដៅ

- រាប់បញ្ចូលទីកន្លែងហៅ Python ទាំងអស់ប្រើ Chat Completions ឬ legacy Completions លើ Azure OpenAI។
- ផ្តល់ផែនការផ្លាស់ប្តូរ និងលំដាប់សម្រាប់កូដ Python។
- អនុវត្តកែប្រែយ៉ាងប្រុងប្រយ័ត្ន និងតិចតួច ដើម្បីផ្លាស់ទៅ Responses API។
- ដំឡើងអ្នកហៅឲ្យប្រើស្កីម៉ាផលិតផល Responses; គ្មានស្រោមទ្រនាប់សំរាប់ Backcompat។
- ដំណើរការប្រឡង/ប្រឡូល; ដោះស្រាយបញ្ហាធម្មតាដែលបង្កឡើងដោយការផ្លាស់ប្តូរ។
- ត្រៀមសំណុំផ្លាស់ប្តូរតូចៗអាចស្ទង់មើល និងផ្តល់សេចក្ដីសង្ខេបចុងក្រោយជាមួយតម្រឹម (កុំ commit)។

---

## បញ្ជីសុវត្ថិភាព

- ត្រូវកែប្រែគ្រាន់តែឯកសារក្នុងបរិវេណ git ប៉ុណ្ណោះ។ មិនចោលពីក្រៅនោះទេ។
- មិនផ្ដល់ការកាន់កាប់សមត្ថភាពមុន; ផ្លាស់ប្តូរកូដទៅរូបរាង API ថ្មី។
- មិនទុកមតិយោបល់ការផ្លាស់ប្ដូរ ឬឯកសារបម្រុងទុកទាន់ពេលបានឡើយ។
- គោរពភាពស្ទ្រីមបើវាបានគេចនា; បើមិនដូច្នោះប្រើមិនស្ទ្រីម។
- សុំអនុម័តមុនពេលដំណើរការការបញ្ជា ឬហៅបណ្ដាញ ប្រសិនបើនៅនៅមុខងារអនុម័ត។
- មិនដំណើរការ `git add`/`git commit`/`git push`; ផលិតតែការកែប្រែទិន្នន័យនៅក្នុង working-tree។

---

## ជំហាន 0: ផ្លាស់ប្តូរ Azure OpenAI Client (លក្ខខណ្ឌមុន)

ប្រសិនបើកូដប្រើ constructors `AzureOpenAI` ឬ `AsyncAzureOpenAI`, សូមផ្លាស់ទៅ constructors `OpenAI` / `AsyncOpenAI` ផ្លូវការដំបូង។ constructors របស់ Azure សម្រាប់ `openai>=1.108.1` ត្រូវបានលះបង់។

### ហេតុអ្វីត្រូវប្រើផ្លូវ API v1?

ចំណុចបញ្ចប់ថ្មី `/openai/v1` ប្រើ client `OpenAI()` ផ្លូវការមិនយោង `AzureOpenAI()`, មិនចាំបាច់ប៉ារ៉ាម៉ែត្រ `api_version`, និងដំណើរការដូចគ្នាតាម OpenAI និង Azure OpenAI។ កូដ client ដូចគ្នា អនាគតធានា — មិនចាំបាច់គ្រប់គ្រងកំណែ។

### ការផ្លាស់ប្តូរសំខាន់ៗ

| មុន | បន្ទាប់ |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | លុបទាំងស្រុង |

### បញ្ជីសម្អាត

- លុបប៉ារ៉ាម៉ែត្រ `api_version` ពីការបង្កើត client។
- លុបបរិស្ថានបម្លែង `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` ពី `.env`, app settings និងឯកសារ Bicep/infra។
- ប្ដូរ `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` ក្នុង `.env`, app settings, Bicep/infra, និង test fixtures (ស្តង់ដារ Azure Identity SDK)។
- ប្រាកដថា `openai>=1.108.1` នៅក្នុង `requirements.txt` ឬ `pyproject.toml`។

### ផ្លាស់ប្តូរបរិស្ថានបម្លែង

| បរិស្ថានបម្លែងចាស់ | សកម្មភាព | សម្គាល់ |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **លុប** | មិនត្រូវការ `api_version` ជាមួយចំណុចបញ្ចប់ v1 |
| `AZURE_OPENAI_API_VERSION` | **លុប** | ដូចគ្នា |
| `AZURE_OPENAI_CLIENT_ID` | **ប្ដូរឈ្មោះ** → `AZURE_CLIENT_ID` | ស្តង់ដារ Azure Identity SDK សម្រាប់ `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **រក្សាទុក** | ត្រូវការសម្រាប់បង្កើត `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **រក្សាទុក** | ប្រើជា `model` ប៉ារ៉ាម៉ែត្រ នៅ `responses.create` |
| `AZURE_OPENAI_API_KEY` | **រក្សាទុក** | ប្រើជា `api_key` សម្រាប់ការផ្ដល់សិទ្ធិដោយគ្រាប់សោ |

សម្រាប់ឧទាហរណ៍កូដ client (sync, async, EntraID, API key, multi-tenant) សូមមើល [cheat-sheet.md](./references/cheat-sheet.md)។

---

## ជំហាន 1: រកមើលទីកន្លែងហៅប្រពៃណីចាស់

ដំណើរការ script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) ដើម្បីស្វែងរកទីកន្លែងហៅទាំងអស់ដែលត្រូវការផ្លាស់ប្តូរ:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

ឬដំណើរការស្វែងរកទាំងនេះដោយដៃ — រាល់ការចេញផ្សាយជួបគ្នាជាគោលដៅផ្លាស់ប្តូរ:

```bash
# ការហៅ API ចាស់ (ត្រូវសរសេរឡើងវិញ)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# អ្នកបង្កើតថ្នាក់ Azure ដែលបានផ្អាកប្រើ (ត្រូវប្តូរ)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# លំនាំការចូលប្រើរូបរាងចម្លើយ (ត្រូវធ្វើបច្ចុប្បន្នភាព)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# ការបញ្ជាក់ឧបករណ៍ក្នុងទ្រង់ទ្រាយជាស្រទាប់ចាស់ (ត្រូវធ្វើបញ្ឈរច្រាស)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# លទ្ធផលឧបករណ៍ក្នុងទ្រង់ទ្រាយចាស់ (ត្រូវបម្លែងទៅ function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# ប៉ារ៉ាម៉ែត្រ​ដែលបានផ្អាកប្រើ (ត្រូវលុបឬប្តូរឈ្មោះ)
rg "response_format"
rg "max_tokens\b"        # ប្តូរឈ្មោះទៅ max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# អថេរបរិយាកាសដែលបានផ្អាកប្រើ (ត្រូវសម្អាត)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # គួរតែជា AZURE_CLIENT_ID

# ចំណុចគោល GitHub Models (ត្រូវលុប — មិនគាំទ្រ Responses API)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# លំនាំលំដាប់ស៊ុម legacy នៅលើ Framework (ត្រូវចាប់ផ្តើមបច្ចុប្បន្នភាព)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: ប្តូរទៅ OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: ត្រូវការ use_responses_api=True

# ហេដ្ឋារចនាសម្ព័ន្ធសាកល្បង (ត្រូវបច្ចុប្បន្នភាព)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# ការចូលប្រើរាងកាយកំហុសតម្រងខ្លឹមសារ (ត្រូវបច្ចុប្បន្នភាព — រចនាសម្ព័ន្ធបានផ្លាស់ប្តូរ)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # ទំរង់តែមួយចាស់ — ឥឡូវ content_filter_results (ពហុរូប) នៅខាងក្នុងអារេ content_filters

# ការហៅ HTTP ដើមទៅចំណុចផ្ដាច់ Chat Completions (ត្រូវបច្ចុប្បន្នភាព URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### វិធីសាស្រ្ត (រកឃើញ និងកែប្រែ)

- **Client Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **អ្នកតឹងតែងអតិថិជន Azure**៖ `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`។
- **ឧបករណ៍**៖ បម្លែងកំណត់នៃឧបករណ៍ហៅមុខងារពីទ្រង់ទ្រាយរក្សាទុកក្នុង nested (`{"type": "function", "function": {"name": ...}}`) ទៅទ្រង់ទ្រាយ Responses ជាត្រង់ (`{"type": "function", "name": ...}`)។ ប្រើ `tool_choice`។ ត្រឡប់លទ្ធផលឧបករណ៍ជារបស់ `{"type": "function_call_output", "call_id": ..., "output": ...}` (មិនមែនជា `{"role": "tool", ...}`)។
- **ការបង្រ្កាបឧបករណ៍ជាច្រើនដង**៖ ពេលម៉ូដែលត្រឡប់ការហៅមុខងារ សូមបន្ថែមធាតុ `response.output` ទៅក្នុងកិច្ចសន្ទនា (មិនមែនជាដីកសាន់ `{"role": "assistant", "tool_calls": [...]}`) បន្ទាប់មកបន្ថែមធាតុ `function_call_output` សម្រាប់លទ្ធផលនីមួយៗ។
- **ឧទាហរណ៍ឧបករណ៍ប៉ុន្មានដង**៖ ប្រសិនបើកិច្ចសន្ទនាមានឧទាហរណ៍ហៅឧបករណ៍ដាក់កូដម៉ានូ អ្នកត្រូវបម្លែងពួកវាទៅជា `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` ជាមួយខ្សែកូដ `{"type": "function_call_output", ...}`។ អត្តសញ្ញាណត្រូវចាប់ផ្តើមជាមួយ `fc_`។
- **`pydantic_function_tool()`**៖ ជំនួយនេះនៅតែបង្កើតទ្រង់ទ្រាយ nested ចាស់ ហើយមិន **ការព្រមព្រៀង** ជាមួយ `responses.create()`។ ជំនួសដោយកំណត់តែងឧបករណ៍ដោយដៃ ឬប្រើវ៉ារ៉ាប់បាច់បញ្ចូល។
- **ចំលងជាច្រើនជុំ**៖ រក្សាប្រវត្តិកិច្ចសន្ទនានៅក្នុងកម្មវិធី; បញ្ជូនជុំមុនៗតាមរយៈធាតុ `input`។
- **រចនាប័ទ្ម**៖ ជំនួស `response_format` នៅកំពូល Chat ជា `text.format` ក្នុង Responses។ ទ្រង់ទ្រាយស្តង់ដា៖ `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`។
- **ធាតុមាតិកា**៖ បម្លែង `content[].type: "text"` របស់ Chat ទៅជា `content[].type: "input_text"` សម្រាប់ជុំអ្នកប្រើ/ប្រព័ន្ធ ក្នុង Responses។
- **ធាតុំាតិការូបភាព**៖ បម្លែង `content[].type: "image_url"` របស់ Chat ទៅជា `content[].type: "input_image"` នៅក្នុង Responses។ ប្រស្នាក់ `image_url` បម្លែងពីអប្បបរមា nested `{"url": "..."}` ទៅខ្សែស្រឡាយត្រង់។ មើលស្លាកជំនួយសម្រាប់ឧទាហរណ៍មុន/បន្ទាប់។
- **ខិតខំពិចារណា**៖ **ចូរផ្លាស់ប្តូរ `reasoning` តែប៉ុណ្ណោះ ប្រសិនបើវាមានរួចហើយក្នុងកូដដើម**។
- **ដំណើរការខូចខាតក្នុងការត្រួតពិនិត្យមាតិកា**៖ រចនាសម្ព័ន្ធខ្លឹមសារខុស។ Chat Completions ប្រើ `error.body["innererror"]["content_filter_result"]` (ឯកជន); Responses API ប្រើ `error.body["content_filters"][0]["content_filter_results"]` (ពហុ បញ្ចូលក្នុងតារាង)។ កូដដែលចូលដល់ `innererror` នឹងបញ្ចេញ `KeyError`។ សូមសរសេរឡើងវិញដើម្បីប្រើផ្លូវថ្មី។
- **ហៅ HTTP ដំបូងគ្រប់គ្រាន់**៖ ប្រសិនបើកម្មវិធីហៅ REST API Azure OpenAI ដោយផ្ទាល់ (តាម `requests`, `httpx`, ល.) ដោយប្រើ `/openai/deployments/{name}/chat/completions?api-version=...` សូមបម្លែងទៅ `/openai/v1/responses`។ ខ្លឹមសារសំណើបម្លែង៖ `messages` → `input` ផ្ដល់ `max_output_tokens` និង `store: false` លុប `api-version` query។ ខ្លឹមសារឆ្លើយតបបម្លែង៖ `choices[0].message.content` → `output[0].content[0].text` (ចំណាំ៖ `output_text` គឺជាគុណលក្ខណៈ SDK មិនមានក្នុង JSON REST ដើម)។

---

## ជំហានទី 2៖ អនុវត្តការផ្លាស់ប្តូរ

### កំណត់សម្គាល់ការផ្លាស់ប្តូរ (Chat Completions → Responses)

- **ហេតុផលផ្លាស់ប្តូរ**៖ Responses ជា API ឯកសរ​សម្រាប់អត្ថបទ, ឧបករណ៍ និងការចាក់ទឹក។ Chat Completions ជាគំរូចាស់។ ជាមួយ GPT-5, Responses ត្រូវបានទាមទារសម្រាប់ប្រសិទ្ធភាពអតិបរមា។
- **HTTP**៖ ចំណុចបញ្ចូល Azure ផ្លាស់ពី `/openai/deployments/{name}/chat/completions` ទៅ `/openai/v1/responses`។
- **វាលទិន្នន័យ**៖ `messages` → `input`, `max_tokens` → `max_output_tokens`។ `temperature` មិនផ្លាស់ប្តូរ។
- **រចនាប័ទ្ម**៖ `response_format` → `text.format` ជាវត្ថុត្រឹមត្រូវ។
- **ធាតុមាតិកា**៖ ជំនួស `content[].type: "text"` របស់ Chat ជា `content[].type: "input_text"` សម្រាប់ជុំប្រព័ន្ធ/អ្នកប្រើក្នុង Responses។
- **ធាតុរូបភាព**៖ ជំនួស `content[].type: "image_url"` របស់ Chat ជា `content[].type: "input_image"` ក្នុង Responses។ ផ្លាស់ប្តូរជំនួសវាល `image_url` ពី `{"image_url": {"url": "..."}}` ទៅ `{"image_url": "..."}` (ខ្សែស្រឡាយត្រង់ — ទាំង អាសយដ្ឋាន HTTPS ឬ URI ទិន្នន័យ `data:image/...;base64,...`)។

### ឯកសារការកំណត់ផែនទីប៉ារ៉ាម៉ែត្រ

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (សារៈក្នុងអារ៉េ) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (វត្ថុ) |
| `temperature` | `temperature` (មិនផ្លាស់ប្តូរ) |
| `stop` | `stop` (មិនផ្លាស់ប្តូរ) |
| `frequency_penalty` | `frequency_penalty` (មិនផ្លាស់ប្តូរ) |
| `presence_penalty` | `presence_penalty` (មិនផ្លាស់ប្តូរ) |
| `tools` / ហៅមុខងារ | `tools` (មិនផ្លាស់ប្តូរ) |
| `seed` | **លុបចោល** (មិនគាំទ្រ) |
| `store` | `store` (កំណត់ជា `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ខ្សែស្រឡាយត្រង់) |

សម្រាប់ឧទាហរណ៍កូដពេញលេញ មុន/បន្ទាប់ គឺមើលបាន [cheat-sheet.md](./references/cheat-sheet.md)។

សម្រាប់ផ្លាស់ប្តូរគ្រឹះស្ថានតេស្ត (mocks, snapshots, assertions) សូមមើល [test-migration.md](./references/test-migration.md)។

សម្រាប់ដោះស្រាយកំហុស និងការប្រើប្រាស់ មាននៅ [troubleshooting.md](./references/troubleshooting.md)។

---

## ការផ្ទុកទិន្នន័យ និងស្ថានភាព

- កំណត់ `store: false` លើសំណើ Responses ទាំងអស់។
- មិនពឹងផ្អែកលើអត្តសញ្ញាណសារមុន ឬបរិបទដែលបានរក្សាទុកនៅម៉ាស៊ីនបម្រើ; រក្សាស្ថានភាពដោយការគ្រប់គ្រងរបស់អតិថិជន ហើយកាត់បន្ថយ metadata។

---

## លក្ខខណ្ឌទទួលយក

### ច្រកកូដកម្រិត (ទាំងអស់ត្រូវតែជោគជ័យ)

- [ ] គ្មានការប្រកួតផ្គូផ្គងសម្រាប់ `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` ក្នុងឯកសារ ដែលបានផ្លាស់ប្តូរ។
- [ ] គ្មានការប្រកួតផ្គូផ្គងសម្រាប់ `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — អ្នកតឹងតែងទាំងអស់ប្រើ `OpenAI`/`AsyncOpenAI` ជាមួយចំណុចបញ្ចូល v1។
- [ ] គ្មានការប្រកួតផ្គូផ្គងសម្រាប់ `rg "models\.github\.ai|models\.inference\.ai\.azure"` — គន្លងកូដ GitHub Models បានដកចេញ។
- [ ] គ្មានការប្រកួតផ្គូផ្គងសម្រាប់ `rg "OpenAIChatCompletionClient"` — កូដ MAF 1.0.0+ ប្រើ `OpenAIChatClient` (ដែលប្រើ Responses API)។ ក្នុងមុន-1.0.0, ធ្វើការដំឡើងទៅ `agent-framework-openai>=1.0.0`។
- [ ] ការហៅ `ChatOpenAI(...)` ទាំងអស់រួមបញ្ចូល `use_responses_api=True`។
- [ ] គ្មានការប្រកួតផ្គូផ្គងសម្រាប់ `rg "choices\[0\]"` — ការចូលប្រើលទ្ធផលទាំងអស់ប្រើ `resp.output_text` ឬទ្រង់ទ្រាយ output Responses។
- [ ] មិនមាន `response_format` លើកំពូល; លទ្ធផលមានរចនាសម្ព័ន្ធទាំងអស់ប្រើ `text={"format": {...}}`។
- [ ] មាន `openai>=1.108.1` និង `azure-identity` ក្នុង `requirements.txt` ឬ `pyproject.toml`; តម្រូវការត្រូវបានដំឡើងឡើងវិញ។
- [ ] ចុះបញ្ជី `store=False` លើការហៅ `responses.create` ទាំងអស់។
- [ ] មិនមាន `api_version` ក្នុងការបង្កើតអតិថិជន; ការ​លុប `AZURE_OPENAI_API_VERSION` ពីឯកសារ env និងអាគារពាក់ព័ន្ធ។

### ច្រកសំណង់តេស្ត (ទាំងអស់ត្រូវតែជោគជ័យ)

- [ ] គ្មានការប្រកួតផ្គូផ្គងសម្រាប់ `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`។
- [ ] គ្មានការប្រកួតផ្គូផ្គងសម្រាប់ `rg "_azure_ad_token_provider" tests/` — បញ្ញត្តិបានធ្វើបច្ចុប្បន្នភាព ដើម្បីពិនិត្យ `isinstance(client, AsyncOpenAI)` ឬ `base_url`។
- [ ] គ្មានការប្រកួតផ្គូផ្គងសម្រាប់ `rg "prompt_filter_results|content_filter_results" tests/` — mocks គោលលក្ខណៈ filter របស់ Azure បានដកចេញ។
- [ ] mock fixture ប្រើ `kwargs.get("input")` មិនមែន `kwargs.get("messages")`។
- [ ] Snapshot / golden files បានបន្ទាន់សម័យទៅទ្រង់ទ្រាយ streaming Responses (គ្មាន `choices[0]`, `function_call`, `logprobs` ទេ)។
- [ ] `pytest` ការបញ្ចប់ជោគជ័យ ដោយគ្មានបរាជ័យក្រោយការកែប្រែទាំងអស់។

### ច្រករបៀបអនុវត្ត (ត្រួតពិនិត្យដោយដៃ ឬតាម test harness)

- [ ] **ការបញ្ចប់មូលដ្ឋាន**៖ `responses.create` មិនស្ទ្រីម ត្រូវត្រឡប់ `output_text` មិនទទេ។
- [ ] **ភាពស្ទ្រីមស្មើភាព**៖ ប្រសិនបើកូដដើមប្រើការស្ទ្រីម កូដដែលបានផ្លាស់ប្តូរនឹងស្ទ្រីម និងបញ្ចេញព្រឹត្តិការណ៍ `response.output_text.delta` ជាមួយ delta មិនទទេ។
- [ ] **លទ្ធផលមានរចនាសម្ព័ន្ធ**៖ ប្រសិនបើប្រើ `text.format` ជាមួយ `json_schema`, `json.loads(resp.output_text)` ត្រូវជោគជ័យ និងមានផ្ទឹងទៅនឹង schema។
- [ ] **វដ្តហៅឧបករណ៍**៖ ប្រសិនបើប្រើឧបករណ៍ ម៉ូដែលហៅឧបករណ៍ កម្មវិធីអនុវត្ត ពេលបន្ទាប់សំណើត្រឡប់ `output_text` ចុងក្រោយ (គ្មានវដ្តអតិផរណា)។
- [ ] **ភាពស្មើភាព Async**៖ ប្រសិនបើប្រើ `AsyncAzureOpenAI` វិធីសាស្រ្តស្មើគ្នា `AsyncOpenAI` នឹងដំណើរការជាមួយ `await`។
- [ ] **អត្រាកំហុស**៖ មិនមានកំហុស 400/401/404 ថ្មីប្រៀបធៀបទៅមុនពេលផ្លាស់ប្តូរ។

### ទំនុកចរន្ត

- សេចក្ដីសង្ខេបរួមមានឯកសារ​ដែលបានកែប្រែ ចំនួនកន្លែងហៅប្រពៃណីមុន/បន្ទាប់ និងជំហានបន្ទាប់។
- ប្រែប្រួលគឺជាការកែសម្រួលក្នុងផ្ទះបាយ (working-tree edits) មិនមែនជាការបញ្ជូន commit ទេ។

---

## តម្រូវការដំណើរការកំណែ SDK

| កញ្ចប់ | កំណែអប្បបរមា |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | ថ្មីបំផុត (សម្រាប់​អត្តសញ្ញាណ EntraID) |

---

## ឯកសារយោង

- [តារាងជំនួយ — ជួរខ្សែខ្លីកូដទាំងអស់](./references/cheat-sheet.md)
- [ការផ្លាស់ប្តូរទំហំតេស្ត — mocks, snapshots, assertions](./references/test-migration.md)
- [ដោះស្រាយបញ្ហា — កំហុស, តារាងហានិភ័យ, បញ្ហា](./references/troubleshooting.md)
- [detect_legacy.py — កម្មវិធីស្កេនស្វ័យប្រវត្តិ](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [ឯកសារ API Azure OpenAI Responses](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [ជីវិត API Azure OpenAI សិល្បៈ](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [ឯកសារយោង API Responses OpenAI](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->