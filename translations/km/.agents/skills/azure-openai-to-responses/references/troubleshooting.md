# ការដោះស្រាយបញ្ហា, តារាងហានិភ័យ និងចំណុចប្រយ័ត្ន

## ការដោះស្រាយបញ្ហា 400s

| កំហុស | ការជួសជុល |
|-------|-----|
| `missing_required_parameter: tools[0].name` | ការកំណត់ឧបករណ៍ប្រើទម្រង់ nested ចាស់ Chat Completions | បង្រួមពី `{"type": "function", "function": {"name": ...}}` ទៅជា `{"type": "function", "name": ..., "parameters": ...}` — ឈ្មោះ, ពណ៌នា, ជំហានប៉ារ៉ាម៉ែត្រត្រូវបានដាក់នៅកម្រិតលើ |
| `unknown_parameter: input[N].tool_calls` | លទ្ធផលឧបករណ៍ multi-turn ប្រើទម្រង់ចាស់ Chat Completions | ជំនួស `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ជាធាតុ `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | ឧបករណ៍ `strict: true` ខ្វះអារៀក `required` | នៅពេល `strict: true`, លក្ខណៈទាំងអស់ត្រូវតែបញ្ជាក់ក្នុង `required` ហើយតំរូវបន្ថែម `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | ឧបករណ៍ `strict: true` ខ្វះ `additionalProperties: false` | បន្ថែម `"additionalProperties": false` ទៅក្នុងវត្ថុ parameters |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | លេខសម្គាល់ function_call few-shot មាន prefix ខុស | លេខសម្គាល់ function_call ត្រូវចាប់ផ្តើមជាមួយ `fc_` (ឧ. `fc_example1`), មិនមែន `call_` ទេ |
| `missing_required_parameter: text.format.name` | បន្ថែមសោ `"name"` ទៅ dict ទ្រង់ទ្រាយ (ឧ. `"name": "Output"`) |
| `invalid_type: text.format` | ធានា `text.format` ជា dict ដែលមានសោ `type`, `name`, `strict`, `schema` — មិនមែនជាសរសេរទេ |
| `invalid input content type` | ប្រើប្រភេទខ្លឹមសារ `input_text`/`output_text` ជំពូក Chat `text` |
| `invalid input content type` (រូបភាព) | ប្រភេទខ្លឹមសាររូបភាពនៅតែប្រើ `"type": "image_url"` | ប្តូរទៅជា `"type": "input_image"` |
| `Expected object, got string` លើ `image_url` | `image_url` នៅតែជាវត្ថុ nested `{"url": "..."}` | បង្រួមជាសរសេរធម្មតា: `"image_url": "https://..."` ឬ `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` សម្រាប់ `max_output_tokens` | តំលៃទាបជាង **16** នៅលើ Azure OpenAI។ ប្រើ 50+ សម្រាប់តេស្ត, 1000+ សម្រាប់ផលិតកម្ម។ |
| `429 Too Many Requests` ពេលបញ្ជូនបណ្តាយ | កំណត់អត្រា។ ប្រើ try/except ជុំវិញការបញ្ជូនបណ្តាយ, ផ្ដល់ JSON ផ្ទាល់ខ្លួនទៅ frontend, អនុវត្ត backoff/retry។ |
| `KeyError: 'innererror'` លើកំហុសចម្រៀងខ្លឹមសារ | រចនាសម្ព័ន្ធ error body ក្នុង Responses API ផ្លាស់ប្តូរ | Chat Completions ប្រើ `error.body["innererror"]["content_filter_result"]`; Responses API ប្រើ `error.body["content_filters"][0]["content_filter_results"]` (ជាច្រើនក្នុង array). ប្តូរទាំងអស់នៃការចូលប្រើ `innererror`។ |

---

## តារាងហានិភ័យការផ្លាស់ប្តូរ

| រោគសញ្ញា | ភាសាខុស | ការជួសជុល |
|---------|---------------|-----|
| ខ្វះ `output_text` / ប្រតិកម្មចាប់ត្រង់ | `max_output_tokens` តិចពេកសម្រាប់ម៉ូឌែលហេតុផល | កំណត់ `max_output_tokens=1000` ឬខ្ពស់ជាងនេះ — លេខរាប់ token reasoning គឺដល់កម្រិតរួមក្នុង |
| `400 invalid_type: text.format` | បញ្ជូនសរសេរ `response_format` ជំនួស `text.format` dict | ប្រើ `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` នៅ `/openai/v1/responses` | `base_url` ខុស — ខ្វះផ្នែកបញ្ចប់ `/openai/v1/` | ប្រាកដថា `base_url=f"{endpoint}/openai/v1/"` (មានស្លាកចុង) |
| `401 Unauthorized` បន្ទាប់ពីផ្លាស់ប្តូរ `OpenAI()` | មិនបានកំណត់ `api_key` ឬ មិនបានផ្តល់ token provider មកត្រឹមត្រូវ | សម្រាប់ EntraID: `api_key=token_provider` (callable). សម្រាប់ API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| ម៉ូឌែលបញ្ជូន `deployment not found` | `model` មិនត្រូវនឹងឈ្មោះ deployment Azure របស់អ្នក | ប្រើ `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — នេះជាឈ្មោះ deployment មិនមែន model name ទេ |
| `json.loads(resp.output_text)` ផ្អែក `JSONDecodeError` | Schema មិនបានបង្ខំ ឬ ម៉ូឌែលមិនគាំទ្រ JSON កញ្ជឿ | ធានា `"strict": True` នៅក្នុង schema និងផ្ទៀងផ្ទាត់ម៉ូឌែលគាំទ្រលទ្ធផលមានរចនាសម្ព័ន្ធ |
| ប្រតិកម្មបញ្ជូនបណ្តាយមិនមានព្រឹត្តិការណ៍ `delta` | កំពុងត្រួតពិនិត្យប្រភេទព្រឹត្តិការណ៍ខុស | រំលាក់ទៅលើ `event.type == "response.output_text.delta"`, មិនមែន Chat `chat.completion.chunk` ទេ |
| កំហុស `400` លើ input រូបភាព បន្ទាប់ពីផ្លាស់ប្តូរ | ប្រភេទខ្លឹមសាររូបភាពមិនបានធ្វើបច្ចុប្បន្នភាព | ប្ដូរ `"type": "image_url"` → `"type": "input_image"` និងបង្រួម `"image_url": {"url": "..."}` → `"image_url": "..."` (សាច់ដួង) |
| ការហៅឧបករណ៍ចាប់ត្រង់រហូត | ខ្វះលទ្ធផលឧបករណ៍ក្នុង `input` បន្ត | បន្ទាប់ពីប្រតិបត្តិឧបករណ៍ បន្ថែមធាតុ `{"type": "function_call_output", "call_id": ..., "output": ...}` ទៅ `input` សម្រាប់ការស្នើសុំបន្ទាប់ |
| កំហុស `temperature` ជាមួយ GPT-5 ឬ o-series | តម្លៃ `temperature` ផ្សេងពី 1 ត្រូវបានបញ្ជាក់ | លុប `temperature` ឬកំណត់ជា `1` សម្រាប់ម៉ូឌែល GPT-5 និង o-series (o1, o3-mini, o3, o4-mini) |
| កំហុស `top_p` ជាមួយ o-series | `top_p` មិនគាំទ្រ | លុប `top_p` នៅពេលគោលដៅម៉ូឌែល o-series |
| `max_completion_tokens` មិនបានទទួលស្គាល់ | ប្រើប៉ារ៉ាម៉ែត្រ Azure ជាក់លាក់ | ជំនួស `max_completion_tokens` ជា `max_output_tokens`។ កំណត់ 4096+ សម្រាប់ o-series (token reasoning គឺចូលចិត្តកំណត់កម្រិត) |
| លទ្ធផលទទេ/ចាប់ត្រង់ពី o-series | `max_output_tokens` តិចពេក | O-series ប្រើ token reasoning ខាងក្នុង។ កំណត់ `max_output_tokens=4096` ឬខ្ពស់ជាងនេះ — មិនមែន 500–1000 ទេ។ |
| `400 integer_below_min_value` សម្រាប់ `max_output_tokens` | តម្លៃក្រោម 16 | Azure OpenAI អនុវត្ត `max_output_tokens >= 16`។ ប្រើ 50+ សម្រាប់តេស្ត, 1000+ សម្រាប់ផលិតកម្ម។ |
| `429 Too Many Requests` នៅកណ្តាលបណ្តាយ | ដាក់កំណត់អត្រាដោយ Azure OpenAI | បណ្តាយរលំបាក់ទៅដោយមិនមានកំហុស។ ជាប្រចាំ ប្រើ `try/except` ជុំវិញ `async for event in await coroutine:` ហើយផ្ដល់ `{"error": str(e)}` ទៅ frontend។ |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | tenant ខុស ឬ មិនបានចូល | ផ្ដល់ `tenant_id=os.getenv("AZURE_TENANT_ID")` ឲ្យច្បាស់។ ដំណើរការ `azd auth login --tenant <tenant-id>` នៅក្នុងម៉ាស៊ីនមូលដ្ឋាន។ |
| `404 Not Found` ប្រើ GitHub Models (`models.github.ai`) | GitHub Models មិនគាំទ្រ Responses API | លុបផ្លូវកូដ GitHub Models ចោល។ ប្រើ Azure OpenAI, OpenAI, ឬ endpoint ផ្លូវការ (ឧ. Ollama ជាមួយគាំទ្រការឆ្លើយតប) |
| MAF `OpenAIChatCompletionClient` នៅតែប្រើ Chat Completions | ប្រើ client legacy MAF ក្នុង 1.0.0+ | នៅ MAF 1.0.0+, `OpenAIChatClient` ប្រើ Responses API ដោយលំនាំដើម។ ជំនួស `OpenAIChatCompletionClient` ជា `OpenAIChatClient`។ សម្រាប់មុន 1.0.0, ឡើងកម្រិតទៅ `agent-framework-openai>=1.0.0`។ |
| LangChain agent បញ្ជូនទទេ ឬ ខកខានជាមួយហៅឧបករណ៍ | `ChatOpenAI` មិនប្រើ Responses API | បន្ថែម `use_responses_api=True` ទៅក្នុង `ChatOpenAI(...)`។ ក៏ប្ដូរ `.content` → `.text` លើសារ response។ |
| `KeyError: 'innererror'` នៅក្នុងអ្នកចុះបញ្ជីក្រងខ្លឹមសារ | រចនាសម្ព័ន្ធ error body ផ្លាស់ប្តូរ ក្នុង Responses API | ប្ដូរ `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`។ ប្រអប់ `innererror` បានផុត; ព័ត៌មានក្រងខ្លឹមសារបច្ចុប្បន្ននៅក្នុង array `content_filters` ដែលមាន `content_filter_results` (ពហុ) ខាងក្នុងធាតុរៀងរាល់ខ្នាត។ |
| ការហៅ HTTP ដើមទៅ `/openai/deployments/.../chat/completions` ប្រើ 404 | ចំណុចចេញ REST Chat Completions ប្រាក់ចាស់ | ប្ដូរអាសយដ្ឋានទៅ `/openai/v1/responses`។ ប្រែសំណើៈ `messages` → `input`, បន្ថែម `max_output_tokens` + `store: false`, ដក `api-version` query param។ ប្រែការពន្យល់លទ្ធផល: `choices[0].message.content` → `output[0].content[0].text` (ចំណាំ: `output_text` ជាគុណសម្បត្តិក្នុង SDK មិនមែន JSON REST ដើម)។ |

---

## ចំណុចប្រយ័ត្ន

1. ប្រសិនបើអ្នកបានប្រើ Chat Completions សម្រាប់ស្ថានភាពការពិភាក្សា មេវ្​ងគ្រប់គ្រងស្ថានភាពដោយខ្លួនឯងយ៉ាងច្បាស់ជាមួយ Responses។
2. ជ្រើសរើស `max_output_tokens` ជាជម្រើសល្អជាង `max_tokens` បុរាណ។
3. នៅពេលផ្លាស់ប្តូរ​ទៅ `gpt-5` ធានាថា `temperature` មិនត្រូវបានបញ្ជាក់ ឬកំណត់ជា `1`។
4. ជំនួស Chat `content[].type: "text"` ជា Responses `content[].type: "input_text"` សម្រាប់ចូលអ្នកប្រើ/ប្រព័ន្ធ។
5. សម្រាប់ `text.format`, ផ្ដល់ dict ត្រឹមត្រូវ (ឧ. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), មិនមែនសរសេរទេ។
6. គ្មានគាំទ្រពាក្យប៉ារ៉ាម៉ែត្រ `seed` នៅក្នុង Responses ត្រូវលុបវាចេញពីសំណើ។
7. **ការគិត**: រួមបញ្ចូលបានគិតតែនៅពេលកូដដើមបានប្រើវា។ កុំបន្ថែម `reasoning` ទៅសំណើ API ដែលមិនមានវា — ម៉ូឌែលមិនគិតភាគច្រើនមិនគាំទ្រពាក្យប៉ារ៉ាម៉ែត្រនេះ។
8. **ទំហំ `max_output_tokens`**: សម្រាប់ម៉ូឌែលគិត (GPT-5-mini, GPT-5, o-series), ប្រើ `max_output_tokens=4096` ឬខ្ពស់ជាង — មិនមែន 50–1000 ទេ។ ម៉ូឌែលប្រើ token គិតខាងក្នុងមុនបង្កើតលទ្ធផលមើលឃើញ; កំណត់ទាបនាំអោយលទ្ធផលចាប់ត្រង់ ឬទទេ។
9. **O-series `max_completion_tokens`**: ប្រសិនបើកូដដើមបានប្រើ `max_completion_tokens` (ជាក់លាក់ Azure សម្រាប់ o-series), ជំនួសជាមួយ `max_output_tokens`។ Responses API មិនទទួល `max_completion_tokens`។
10. **O-series `reasoning_effort`**: ប្រសិនបើកូដដើមប្រើ `reasoning_effort` (ទាប/មធ្យម/ខ្ពស់), ផ្លាស់ប្តូរតាម `reasoning={"effort": "<value>"}` ក្នុងការហៅ Responses API។
11. **ការពន្យារលំហូររបស់ o-series**: ម៉ូឌែល o-series ធ្វើការគិតខាងក្នុងមុនបង្កើតលទ្ធផល។ ភាពយឺតក្នុងការផ្ដល់ព្រឹត្តិការណ៍ `response.output_text.delta` ដំបូងគឺធម្មតា — ម៉ូឌែលកំពុងគិត មិនមែនជាប់នៅឡើយទេ។
9. **`_azure_ad_token_provider` អស់ទៅហើយ**: `AsyncOpenAI` / `OpenAI` មិនមានអានគុណ `_azure_ad_token_provider` ទេ។ តេស្តឬកូដដែលចូលដល់អានគុណនេះនឹងបរាជ័យជាមួយ `AttributeError`។ អ្នកផ្គត់ផ្គង់ token ត្រូវបានផ្ដល់ជា `api_key` ហើយមិនអាចផ្ទៀតផ្ទាត់បានលើ client object។
10. **ឯកសារតេស្ត Snapshot / golden files**: ប្រសិនបើក្រុមតេស្តប្រើតេស្ត snapshot, **ឯកសារ snapshot ទាំងអស់** ដែលមានរូបរាងបញ្ជូនបណ្តាយ Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, ល) ត្រូវបានធ្វើបច្ចុប្បន្នភាពជារូបរាង Responses ថ្មី។ វាយ៉ាងងាយខកខានហើយផ្សះផ្សាអោយមានករណីអះអាងតេស្តបរាជ័យ។
11. **ផ្លូវ Mock monkeypatch ផ្លាស់ប្តូរ**: ទិសដៅ monkeypatch ផ្លាស់ពី `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ឬ `Responses.create` សម្រាប់ sync)។ ប្រើផ្លូវចាស់ដោយផ្ទាល់ មិនមានអ្វីកើតឡើងទេ — mock មិនចាប់, និងតេស្តងេាង API ពិតមិនបាន។
12. **`input` មិនមែន `messages`**: មុខងារ mock ត្រូវអាន `kwargs.get("input")` មិនមែន `kwargs.get("messages")` ទេ។ Responses API ប្រើ `input` សម្រាប់ប្រវត្តិការពិភាក្សា។
13. **ការដាក់ឈ្មោះ environment variable**: Azure Identity SDK ប្រើ `AZURE_CLIENT_ID` (មិនមែន `AZURE_OPENAI_CLIENT_ID`) សម្រាប់ `ManagedIdentityCredential(client_id=...)`។ ឈ្មោះត្រូវបានផ្លាស់ប្ដូរនៅក្នុងតេស្ត, .env, ការកំណត់កម្មវិធី និង Bicep/infra។
14. **`max_output_tokens` ទាបបំផុតគឺ 16**: Azure OpenAI បដិសេធតម្លៃក្រោម 16 ជាមួយកំហុស `400 integer_below_min_value`។ ប្រើ 50 សម្រាប់តេស្តលឿន, 1000+ សម្រាប់ផលិតកម្ម។ `max_tokens` ចាស់មិនមានកម្រិតទាបនេះទេ។
15. **`tenant_id` សម្រាប់ `AzureDeveloperCliCredential`**: កន្លែង Azure OpenAI នៅ tenant ផ្សេង, អ្នក **ត្រូវតែ** បញ្ជាក់ `tenant_id` ច្បាស់ — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`។ បើមិនដាក់ វានឹងប្រើ tenant ខុស ដោយស្ងាត់ និងតប 401។
16. **កំណត់អត្រាសូម្បីបង្ហាញខុសគ្នានៅលើបណ្តាយ**: ជាមួយ Chat Completions, 429 ជាទូទៅបញ្ឈប់បណ្តាយមុនចាប់ផ្តើម។ ជាមួយ Responses API បណ្តាយ, 429 អាចកើត **កណ្ដាលបណ្តាយ** — ត្រូវបោះពុម្ពករណីកើតថ្មោង។ ជាប្រចាំប្រើ try/except ជុំវិញលុបចេញបណ្តាយ ហើយផ្ដល់ខ្សែ JSON error ក្រោយ ដើម្បីអនុញ្ញាត frontend ឆ្លើយតបទៅបានសមដៅ។

17. **ការដោះស្រាយកំហុសការចាក់ផ្សាយផ្ទាល់គឺចាំបាច់សម្រាប់កម្មវិធីបណ្តាញ**៖ រូបแบบ `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` គឺសំខាន់ណាស់។ បើគ្មានវា ស្ទ្រីម SSE/JSONL នោះនឹងដួលខ្លួនដោយស្ងៀមលើកំហុសពីផ្នែកម៉ាស៊ីនបម្រើណាមួយ ហើយផ្នែកមុខអ្នកប្រើនឹងផ្អាក។
18. **ការកំណត់ឧបករណ៍ត្រូវប្រើទ្រង់ទ្រាយរាបស្មើ**៖ Responses API រងចាំ `{"type": "function", "name": ..., "parameters": ...}` — មិនមែន `{"type": "function", "function": {"name": ..., "parameters": ...}}` ដែលជាទ្រង់ទ្រាយប្រាក់កប់ក្នុង Chat Completions ទេ។ នេះគឺជាកំហុសប្រចាំក្នុងការផ្លាស់ប្តូរជាលក្ខណៈទូទៅសម្រាប់កូដហៅមុខងារ។
19. **`pydantic_function_tool()` មិនត្រូវគ្នា**៖ ជំនួយការ `openai.pydantic_function_tool()` នៅតែបង្កើតទ្រង់ទ្រាយប្រាក់កប់ចាស់។ កុំប្រើវាជាមួយ `responses.create()`។ កំណត់ស្កីម៉ាឧបករណ៍ដោយដៃឬបញ្ច្រាសចេញ។
20. **លទ្ធផលឧបករណ៍ប្រើ `function_call_output` មិនមែន `role: tool`**៖ បន្ទាប់ពីបំពេញឧបករណ៍ បន្ថែម `{"type": "function_call_output", "call_id": ..., "output": ...}` — មិនមែន `{"role": "tool", "tool_call_id": ..., "content": ...}` ទេ។ សម្រាប់សំណើឧបករណ៍របស់ជំនួយការ ប្រើ `messages.extend(response.output)` — មិនមែន dict មួយដែលសរសេរជាម៉ានុយ `{"role": "assistant", "tool_calls": [...]}` ទេ។
21. **`strict: true` ត្រូវការជាមួយ `required` + `additionalProperties: false`**៖ នៅពេលប្រើ `strict: true` លើឧបករណ៍ តម្លៃគ្រប់អចិន្ត្រៃយ៍ត្រូវតែបញ្ចូលក្នុងអារ៉េ `required` ហើយ `additionalProperties` ត្រូវតែជា `false`។ ការខ្វះខាតមួយណាមួយនាំឲ្យកំហុស 400។
22. **អត្តសញ្ញាណហៅមុខងារមានឈ្មោះដាក់ជាក់លាក់**៖ នៅពេលផ្តល់ជាប្រភេទវត្ថុនៃ `function_call` ស្ទាត់ភាគរយក្នុង `input` វាល `id` ត្រូវចាប់ផ្តើមជាមួយ `fc_` ហើយវាល `call_id` ត្រូវចាប់ផ្តើមជាមួយ `call_` (ឧ. `"id": "fc_example1", "call_id": "call_example1"` )។ ការប្រើរួច prefix `call_` នៃ Chat Completions សម្រាប់ `id` ត្រូវបានបដិសេធ។
23. **GitHub Models មិនគាំទ្រ Responses API**៖ ប្រសិនបើកម្មវិធីមានផ្លូវកូដ GitHub Models (`base_url` បង្ហាញទៅ `models.github.ai` ឬ `models.inference.ai.azure.com`) ត្រូវដកចេញទាំងស្រុង។ មិនមានផ្លូវផ្លាស់ប្តូរ — ផ្លាស់ទៅ Azure OpenAI, OpenAI, ឬច្រកដែលត្រូវគ្នាក្នុងតំបន់។
24. **រចនាសម្ព័ន្ធខួរស្បែកកំហុសជម្រះមាតិកាបានផ្លាស់ប្តូរ**៖ កំហុស Chat Completions មាន `error.body["innererror"]["content_filter_result"]` (មួយ)។ កំហុស Responses API ប្រើ `error.body["content_filters"][0]["content_filter_results"]` (ច្រើន នៅក្នុងអារេមួយ)។ គន្លងជា `innererror` មិនមានទៀតទេ។ កូដដែលចូលដំណើរការនៅ `innererror` ត្រូវបង្កើត `KeyError` ពេលរត់ — នេះគឺឆាប់ចុះ ស្រួលខកចិត្តក្នុងការផ្លាស់ប្តូរព្រោះវាធ្វើការបង្ហាញតែពេលកម្មវិធីត្រូវបង្ហាញថាប្រព័ន្ធចម្រាស់មាតិកាដើរដោយពិត។ តែងតែស្វែងរក `innererror` នៅពេលផ្លាស់ប្តូរ។
25. **ការហៅ HTTP សុទ្ធត្រូវការកែប្រែ URL + រាងកាយ**៖ កម្មវិធីហៅ Azure OpenAI REST ដោយផ្ទាល់ (តាម `requests`, `httpx`, `aiohttp`) ប្រើ `/openai/deployments/{name}/chat/completions?api-version=...` ត្រូវបម្លែងទៅ `/openai/v1/responses`។ រាងកាយសំណើប្រើ `input` ជំនួស `messages`, តម្រូវឲ្យមាន `max_output_tokens` និង `store`, ហើយបាត់បង់ព៉ារ៉ាម៉ែត្រ `api-version` នៅ query string។ អត្ថបទខ្លឹមសារឆ្លើយតបស្ថិតនៅ `output[0].content[0].text` — **មិនមែន** `output_text` ដែលជារបស់មួយសេវាកម្ម SDK មិនមានក្នុង JSON REST ដើមឡើយ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->