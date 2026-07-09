# ការដោះស្រាយបញ្ហា តារាងហានិភ័យ និង ចំណុចយ៉ាងចម្បង

## ការដោះស្រាយបញ្ហាអក្សរលេខ ៤០០

| បញ្ហា | ការជួសជុល |
|-------|-----|
| `missing_required_parameter: tools[0].name` | ការបំណល់ឧបករណ៍ប្រើទ្រង់ទ្រាយផ្លូវChat Completionsចាស់ | បង្រួមពី `{"type": "function", "function": {"name": ...}}` ទៅជា `{"type": "function", "name": ..., "parameters": ...}` — ឈ្មោះ ពិពណ៌នា ប៉ារ៉ាម៉េត្រត្រូវបានដាក់នៅលើកម្រិតលើ |
| `unknown_parameter: input[N].tool_calls` | លទ្ធផលឧបករណ៍ជាច្រើនជុំប្រើទ្រង់ទ្រាយចាស់ Chat Completions | ប្តូរ `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ជា items នៃ `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | ឧបករណ៍ `strict: true` ខ្វះអារ៉េ `required` | នៅពេល `strict: true`, គុណលក្ខណៈទាំងអស់ត្រូវបានបញ្ជីនៅក្នុង `required` ហើយត្រូវកំណត់ `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | ឧបករណ៍ `strict: true` ខ្វះ `additionalProperties: false` | បន្ថែម `"additionalProperties": false` នៅលើវត្ថុ parameters |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | អត្តសញ្ញាណ function_call ต่ำ prefix មិនត្រឹមត្រូវ | អត្តសញ្ញាណ function call ត្រូវចាប់ផ្តើមជាមួយ `fc_` (ឧទាហរណ៍ `fc_example1`), មិនមែន `call_` ទេ |
| `missing_required_parameter: text.format.name` | បន្ថែមកូនសោ `"name"` ទៅ dict format (ឧទាហរណ៍ `"name": "Output"`) |
| `invalid_type: text.format` | ប្រាកដថា `text.format` ជា dict ដែលមានកូនសោ `type`, `name`, `strict`, `schema` — មិនមែន string ទេ |
| `invalid input content type` | ប្រើប្រភេទមាតិកា `input_text`/`output_text` ជំនួស Chat `text` |
| `invalid input content type` (រូបភាព) | មាតិការូបភាពនៅតែប្រើ `"type": "image_url"` | ផ្លាស់ប្តូរ `"type": "input_image"` |
| `Expected object, got string` នៅលើ `image_url` | `image_url` នៅតែក្នុងវត្ថុ nested `{"url": "..."}` | បង្រួមទៅជាស្រដៀង string: `"image_url": "https://..."` ឬ `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` សម្រាប់ `max_output_tokens` | តម្លៃអប្បបរមា **16** នៅលើ Azure OpenAI។ ប្រើ 50+ សម្រាប់សាកល្បង, 1000+ សម្រាប់ផលិតកម្ម។ |
| `429 Too Many Requests` កំឡុងពេលបញ្ជូនស្ទ្រីម | ខ្នោះល្បឿន។ បង្វិលស្ទ្រីមជុំក្នុង `try/except` ហើយបញ្ចេញ JSON បញ្ជាក់កំហុសទៅមុខម៉ាស៊ីន, អនុវត្ត backoff/retry។ |
| `KeyError: 'innererror'` នៅក្នុងកំហុសម៉ាស៊ីនច្រោះមាតិកា | រចនាសម្ព័ន្ធ error body ផ្លាស់ប្ដូរនៅក្នុង Responses API | Chat Completions ប្រើ `error.body["innererror"]["content_filter_result"]`; Responses API ប្រើ `error.body["content_filters"][0]["content_filter_results"]` (ពហុp, នៅក្នុងអារេ)។ សរសេរឡើងវិញកូដចូលដំណើរការទាំងអស់ដែលប្រើ `innererror`។ |

---

## តារាងហានិភ័យការផ្លាស់ទី

| លក្ខណៈ | ការខកខានប្រហែល | ការជួសជុល |
|---------|---------------|-----|
| `output_text` ទទេ / ប្រតិបត្ដិការឆ្លើយតបខ្លះ | `max_output_tokens` ទាបពេកសម្រាប់ម៉ូដែលសំណួរ | តម្លើង `max_output_tokens=1000` ឬខ្ពស់ជាងនេះ — token សំណួរគិតក្នុងកំណត់ |
| `400 invalid_type: text.format` | បញ្ជូន `response_format` ជាពាក្យជំនួស dict `text.format` | ប្រើ `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` នៅ `/openai/v1/responses` | `base_url` មិនត្រឹមត្រូវ — ខ្វះបន្ទាត់បូកបិទ `/openai/v1/` | ប្រាកដថា `base_url=f"{endpoint}/openai/v1/"` (មានស្លេចចុងក្រោយ) |
| `401 Unauthorized` បន្ទាប់ពីប្ដូរទៅ `OpenAI()` | មិនកំណត់ `api_key` ឬ token provider មិនដំណើរការត្រឹមត្រូវ | សម្រាប់ EntraID: `api_key=token_provider` (callable)។ សម្រាប់ API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| ម៉ូដែលបង្ហាញ `deployment not found` | `model` មិនត្រូវនឹងឈ្មោះការចែកចាយ Azure របស់អ្នក | ប្រើ `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — នេះជាឈ្មោះការចែកចាយ មិនមែនឈ្មោះម៉ូដែលទេ |
| `json.loads(resp.output_text)` បង្កើតកំហុស `JSONDecodeError` | មិនបានអនុវត្ត schema ឬម៉ូដែលមិនគាំទ្រជួរដំណើរការ JSON ដែលតឹងរ៉ឹង | ប្រាកដថា `"strict": True` នៅក្នុង schema ហើយយល់ម៉ូដែលគាំទ្របានលទ្ធផលរៀបចំ |
| ការបញ្ជូនស្ទ្រីមមិនបង្ហាញព្រឹត្តិការណ៍ `delta` | ពិនិត្យប្រភេទព្រឹត្តិការណ៍មិនត្រឹមត្រូវ | តម្រៀបលើ `event.type == "response.output_text.delta"` មិនមែន Chat `chat.completion.chunk` ទេ |
| កំហុស 400 នៅលើ input រូបភាពបន្ទាប់ពីផ្លាស់ទី | មាតិការូបភាពមិនបានបន្ទាន់សម័យ | ផ្លាស់ប្តូរ `"type": "image_url"` → `"type": "input_image"` និង បង្រួម `"image_url": {"url": "..."}` → `"image_url": "..."` (string ធម្មតា) |
| ការហៅឧបករណ៍វិលរៀងៗ | ខ្វះលទ្ធផលឧបករណ៍ក្នុង `input` បន្ទាប់ | បន្ទាប់ពីអនុវត្តឧបករណ៍ បន្ថែម item `{"type": "function_call_output", "call_id": ..., "output": ...}` ទៅក្នុង `input` នៅសំណើបន្ទាប់ |
| កំហុស `temperature` ជាមួយ GPT-5 ឬ o-series | តម្លៃ `temperature` បញ្ជាក់ច្បាស់លាស់ មិនមែន 1 | ការដក `temperature` ឬកំណត់ជា `1` សម្រាប់ម៉ូដែល GPT-5 និង o-series (o1, o3-mini, o3, o4-mini) |
| កំហុស `top_p` ជាមួយ o-series | `top_p` មិនគាំទ្រ | ដក `top_p` ចេញនៅពេលបម្រើម៉ូដែល o-series |
| មិនទទួលស្គាល់ `max_completion_tokens` | ប្រើប៉ារ៉ាម៉ែត្រ Azure ពិសេស | ជំនួស `max_completion_tokens` ជា `max_output_tokens`។ កំណត់ទៅ 4096+ សម្រាប់ o-series (token reasoning គិតក្នុងកំណត់)។ |
| លទ្ធផលទទេ/ត្រូវបានកាត់បន្ថយពី o-series | តម្លៃ `max_output_tokens` ទាបពេក | o-series ប្រើ token reasoning ក្នុងខាងក្នុង។ កំណត់ `max_output_tokens=4096` ឬខ្ពស់ជាងនេះ — មិនមែន 500–1000 ទេ។ |
| `400 integer_below_min_value` សម្រាប់ `max_output_tokens` | តម្លៃទាបក្រោម 16 | Azure OpenAI កំណត់ `max_output_tokens >= 16`។ ប្រើ 50+ សម្រាប់សាកល្បង, 1000+ សម្រាប់ផលិតកម្ម។ |
| `429 Too Many Requests` កណ្ដាលបញ្ជូនស្ទ្រីម | ត្រូវបានកំerrenល្បឿនដោយ Azure OpenAI | ស្ទ្រីមបែកបាក់ដោយស្ងាត់ដោយគ្មានការដោះស្រាយកំហុស។ ការបង្ហាញតំរូវបន្លិច `async for event in await coroutine:` ត្រូវបានបង្ហូរជុំក្នុង `try/except` ហើយបញ្ចេញ `{"error": str(e)}` ទៅមុខម៉ាស៊ីន។ |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | នៅ tenant មិនត្រឹមត្រូវ ឬ មិនបានចូល | បញ្ជូន `tenant_id=os.getenv("AZURE_TENANT_ID")` ផ្ទាល់ក្រង់។ រត់ `azd auth login --tenant <tenant-id>` នៅក្នុងម៉ាស៊ីនក្នុងស្រុក។ |
| `404 Not Found` ប្រើឧបករណ៍ GitHub Models (`models.github.ai`) | GitHub Models មិនគាំទ្រ Responses API | លុបផ្លូវកូដ GitHub Models ពេញលេញ។ ប្រើ Azure OpenAI, OpenAI ឬចំណុចប្រទាក់មូលដ្ឋានដែលត្រូវតែមាន Responses (ឧ. Ollama ជាមួយការគាំទ្រ Responses)។ |
| MAF `OpenAIChatCompletionClient` នៅតែប្រើ Chat Completions | ប្រើម៉ាស៊ីន MAF មួយចាស់ នៅក្នុង version 1.0.0+ | នៅ MAF 1.0.0+ `OpenAIChatClient` ប្រើ Responses API ជាមូលដ្ឋាន។ ជំនួស `OpenAIChatCompletionClient` ជា `OpenAIChatClient`។ សម្រាប់មុន 1.0.0, ធ្វើការ upgrade ទៅ `agent-framework-openai>=1.0.0`។ |
| ព្រីនទ័របណ្ដាញ LangChain រើសលទ្ធផលទទេ ឬចាកចេញនៅពេលហៅឧបករណ៍ | `ChatOpenAI` មិនប្រើ Responses API | បន្ថែម `use_responses_api=True` ទៅ `ChatOpenAI(...)`។ ផ្លាស់ប្តូរ `.content` ទៅ `.text` នៅលើសារ response។ |
| `KeyError: 'innererror'` ក្នុងអ្នកដោះស្រាយកំហុសម៉ាស៊ីនច្រោះមាតិកា | រចនាសម្ព័ន្ធ error body ផ្លាស់ប្ដូរនៅក្នុង Responses API | សរសេរឡើងវិញ `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`។ ការវេចខ្ចប់ `innererror` ត្រូវបានលុបចោល; ព័ត៌មានអំពីការច្រោះមាតិកាកំពុងស្ថិតនៅក្នុងអារេជាន់ខ្ពស់ `content_filters` ជាមួយ `content_filter_results` (ពហុp) នៅក្នុងបញ្ចូលនីមួយៗ។ |
| ការហៅ HTTP ត្រង់ `/openai/deployments/.../chat/completions` ផ្ទុក 404 | ចំណុចបញ្ចប់ REST Chat Completions ចាស់ | សរសេរឡើងវិញ URL ទៅ `/openai/v1/responses`។ ផ្លាស់ប្តូររូបមន្តសំណើ៖ `messages` → `input`, បន្ថែម `max_output_tokens` + `store: false`, លុប query param `api-version`។ ផ្លាស់ប្តូរជួរដំណើរការឆ្លើយតប៖ `choices[0].message.content` → `output[0].content[0].text` (ចំណាំ៖ `output_text` ជាសម្បត្តិបន្ថែមនៅ SDK មិនមាននៅក្នុង JSON REST ដើម)។ |

---

## ចំណុចយ៉ាងចម្បង

1. ប្រសិនបើអ្នកបានប្រើ Chat Completions សម្រាប់ការគ្រប់គ្រងស្ថានភាពសន្ទនា មanej់ស្ថានភាពឲ្យបានច្បាស់ជាមួយ Responses។
2. ជ្រើសរើស `max_output_tokens` ជំនួស `max_tokens` ជំនាន់ចាស់។
3. នៅពេលផ្លាស់ទីទៅ `gpt-5` ប្រាកដថា `temperature` មិនត្រូវបានអាចបញ្ជាក់ឬកំណត់ទៅជា `1`។
4. ជំនួស Chat `content[].type: "text"` ជា Responses `content[].type: "input_text"` សម្រាប់បញ្ចូលអ្នកប្រើ/ប្រព័ន្ធ។
5. សម្រាប់ `text.format`, ផ្គត់ផ្គង់ dict ត្រឹមត្រូវ (ឧ. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`) មិនមែន string ធម្មតាទេ។
6. ប៉ារ៉ាម៉ែត្រ `seed` មិនគាំទ্রেនៅក្នុង Responses; លុបវាចេញពីសំណើ។
7. **ការ reasoning**: រួមបញ្ចូលតែ `reasoning` ប្រសិនបើកូដដើមបានប្រើរួចហើយ។ កុំបន្ថែម `reasoning` ទៅក្នុងហៅ API ដែលមិនមានវា — ម៉ូដែលជាច្រើន (ឧ. gpt-4o-mini) មិនគាំទ្រ។
8. **ទំហំ `max_output_tokens`**: សម្រាប់ម៉ូដែល reasoning (GPT-5-mini, GPT-5, o-series), ប្រើ `max_output_tokens=4096` ឬខ្ពស់ជាងនេះ — មិនមែន 50–1000។ ម៉ូដែលប្រើ token reasoning ខាងក្នុងមុនបង្កើតលទ្ធផលដែលអាចមើលឃើញ; កំណត់ទាបពេកបណ្តាលឲ្យមានចម្លើយត្រូវបានកាត់បន្ថយ ឬទទេ។
9. **O-series `max_completion_tokens`**: ប្រសិនបើកូដដើមបានប្រើ `max_completion_tokens` (សម្រាប់ o-series ផ្ទាល់), ជំនួសដោយ `max_output_tokens`។ Responses API មិនទទួល `max_completion_tokens` ទេ។
10. **O-series `reasoning_effort`**: ប្រសិនបើកូដដើមប្រើ `reasoning_effort` (ទាប/មធ្យម/ខ្ពស់), ផ្លាស់ទីវាទៅជា `reasoning={"effort": "<value>"}` ក្នុងហៅ Responses API។
11. **ការពន្យារស្ទ្រីម o-series**: ម៉ូដែល o-series ធ្វើ reasoning ខាងក្នុងមុនបង្កើតលទ្ធផល។ នៅពេលប្រើស្ទ្រីម, រំពឹងថាពន្យារពេលយូរមុនព្រឹត្តិការណ៍ `response.output_text.delta` ដំបូង។ នេះធម្មតា — ម៉ូដែលកំពុង reasoning មិនមែនរអ៊ូរទេ។
9. **`_azure_ad_token_provider` បានបាត់**: `AsyncOpenAI` / `OpenAI` មិនមានគំនូស `_azure_ad_token_provider`។ ការធ្វើតេស្តឬកូដដែលចូលដំណើរការកូដនេះនឹងបរាជ័យជាមួយ `AttributeError`។ token provider ត្រូវបានផ្តល់ជាប៉ារ៉ាម៉ែត្រ `api_key` ហើយមិនអាចពិនិត្យបានលើ client object ទេ។
10. **ឯកសារ Snapshot / golden**: ប្រសិនបើ​ test suite ប្រើការសាកល្បង snapshot, **ឯកសារ snapshot ទាំងអស់** ដែលមានរាងលំហូរស្ទ្រីម Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, ល) ត្រូវបានបច្ចុប្បន្នភាពទៅរាង Responses ថ្មី។ វាងាយស្រួលខកខានហើយបណ្តាលឲ្យបរាជ័យ assertion។
11. **ផ្លូវ mocking monkeypatch**: គោលដៅ monkeypatch ផ្លាស់ពី `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ឬ `Responses.create` សម្រាប់ sync)។ ប្រើផ្លូវចាស់ដោយស្ងាត់គ្មានប្រយោជន៍ — mock មិនចាប់បានហើយតេស្តទាក់ទង API ពិតឬបរាជ័យ។
12. **`input` មិនមែន `messages`**: មុខងារ mock ត្រូវអាន `kwargs.get("input")` មិនមែន `kwargs.get("messages")` ទេ។ Responses API ប្រើ `input` សម្រាប់ប្រវត្តិសន្ទនា។
13. **ឈ្មោះបរិមាណបរិវេណ**: Azure Identity SDK ប្រើ `AZURE_CLIENT_ID` (មែនមិនមែន `AZURE_OPENAI_CLIENT_ID`) សម្រាប់ `ManagedIdentityCredential(client_id=...)`។ ប្ដូរឈ្មោះក្នុង test, ឯកសារ `.env`, ការកំណត់ app និង Bicep/ឧបករណ៍។
14. **អប្បបរមា `max_output_tokens` គឺ 16**: Azure OpenAI បដិសេធតម្លៃក្រោម 16 ជាមួយ error `400 integer_below_min_value`។ ប្រើ 50 សម្រាប់សាកល្បង, 1000+ សម្រាប់ផលិតកម្ម។ `max_tokens` ចាស់មិនមានអប្បបរមាណេះ។
15. **`tenant_id` សម្រាប់ `AzureDeveloperCliCredential`**: នៅពេលធនធាន Azure OpenAI ស្ថិតនៅ tenant ផ្សេងអ្នក **ត្រូវតែ** បញ្ជូន `tenant_id` ដោយផ្ទាល់ — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`។ បើគ្មានវា, credential ប្រើ tenant មិនត្រឹមត្រូវដោយស្ងាត់ ហើយបង្រ្កាប `401`។
16. **កំណាចល្បឿនបង្ហាញខុសគ្នានៅក្នុងស្ទ្រីម**: ជាមួយ Chat Completions, 429 ជាទូទៅទប់ស្កាត់ការចាប់ផ្ដើមស្ទ្រីម។ ជាមួយ Responses API streaming, 429 អាចកើតមាន **កណ្ដាលស្ទ្រីម** — iterator async បញ្ចេញកំហុស។ តែងតែបង្ហូរជុំក្នុង `try/except` ហើយបញ្ចេញបន្ទាត់ JSON កំហុស ដើម្បីមុខម៉ាស៊ីនអាចដោះស្រាយបានងាយស្រួល។

17. **ការដោះស្រាយកំហុសស្ត្រីមីថ្នាក់ចម្បងត្រូវការសម្រាប់កម្មវិធីគេប៊ Webb**: គំរូ `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` មានសារៈសំខាន់យ៉ាងខ្លាំង។ អត់មានវា ពន្លឺ SSE/JSONL នឹងបាត់បង់ដោយស្ងាត់នៅពេលមានកំហុសនៅផ្នែកម៉ាស៊ីនបម្រើ ហើយផ្នែកមុខនឹងផ្អាក។
18. **ការកំណត់ឧបករណ៍ត្រូវតែប្រើទ្រង់ទ្រាយរាបស្មើ**: Responses API គាំទ្រជា `{"type": "function", "name": ..., "parameters": ...}` មិនមែនជា Chat Completions ដែលមានទ្រង់ទ្រាយនៅក្នុង `{"type": "function", "function": {"name": ..., "parameters": ...}}` ទេ។ នេះគឺជាកំហុសធម្មតាក្នុងការផ្លាស់ប្ដូរសម្រាប់កូដហៅមុខងារ។
19. **`pydantic_function_tool()` មិនជាមួយគ្នា**: ជំនួយ `openai.pydantic_function_tool()` នៅតែបង្កើតទ្រង់ទ្រាយចាស់ជាចំណែក។ កុំប្រើវាជាមួយ `responses.create()`។ សូមកំណត់schemaឧបករណ៍ដោយដៃ ឬបញ្ចាក់លើការបញ្ចេញ។
20. **លទ្ធផលឧបករណ៍ប្រើ `function_call_output` មិនប្រើ `role: tool`**: បន្ទាប់ពីបំពេញឧបករណ៍ ត្រូវបន្ថែម `{"type": "function_call_output", "call_id": ..., "output": ...}` មិនមែន `{"role": "tool", "tool_call_id": ..., "content": ...}` ទេ។ សម្រាប់សំណើឧបករណ៍របស់ជំនួយការ សូមប្រើ `messages.extend(response.output)` មិនមែន dict ដៃជាមួយ `{"role": "assistant", "tool_calls": [...]}` ទេ។
21. **`strict: true` ត្រូវការជាមួយ `required` + `additionalProperties: false`**: ពេលប្រើ `strict: true` នៅលើឧបករណ៍ គ្រប់គ្រងលក្ខណៈលំដាប់ត្រូវត្រូវបានរាយនៅក្នុងអារេ `required` ហើយ `additionalProperties` ត្រូវតែជា `false`។ បាត់បង់មួយក្នុងចំណោមនេះ នាំឱ្យកំហុស 400។
22. **អត្តសញ្ញាណមុខងារហៅមានបុព្វបទជាក់លាក់**: ពេលផ្តល់ជាគំរូខ្លះៗ `function_call` ក្នុង `input` បំណែក `id` ត្រូវចាប់ផ្ដើមជាមួយ `fc_` ហើយបំណែក `call_id` ត្រូវចាប់ផ្ដើមជាមួយ `call_` (ឧទាហរណ៍ `"id": "fc_example1", "call_id": "call_example1"`). ការប្រើបុព្វបទចាស់ Chat Completions `call_` សម្រាប់ `id` ត្រូវបានបដិសេធ។
23. **GitHub Models មិនគាំទ្រ Responses API**: ប្រសិនបើកម្មវិធីមានផ្លូវកូដ GitHub Models (`base_url` បញ្ជូនទៅ `models.github.ai` ឬ `models.inference.ai.azure.com`), សូមដកចេញរួចរាល់។ មិនមានផ្លូវផ្លាស់ប្ដូរទេ — សូមប្ដូរទៅជា Azure OpenAI, OpenAI, ឬសេវាកម្មបច្ចេកទេសមួយស្រដៀង។
24. **រចនាសម្ព័ន្ធរាងកាយកំហុសម៉ាស៊ីនត្រួត Content filter បានផ្លាស់ប្តូរ**: កំហុស Chat Completions ប្រើ `error.body["innererror"]["content_filter_result"]` (ផ្សេងទេ)។ កំហុស Responses API ប្រើ `error.body["content_filters"][0]["content_filter_results"]` (ពហុវចនៈ នៅក្នុងអារេមួយ)។ គន្លឹះ `innererror` មិនមានទៀត។ កូដដែលចូលដំណើរការកាន់តែបន្តឹង `innererror` នឹងបង្កើត `KeyError` នៅពេលរហូត — នេះពិបាកសម្គាល់នៅពេលផ្លាស់ប្តូរ ព្រោះវាត្រូវតែកើតឡើងពេលត្រួតឆែកតែល filtered។ សូមរក `innererror` រយៈពេលផ្លាស់ប្ដូរ។
25. **ហៅ HTTP ត្រង់ត្រូវការផ្លាស់ប្ដូរ URL + ខ្លឹមសារ**: កម្មវិធីហៅ Azure OpenAI REST ផ្ទាល់ (តាម `requests`, `httpx`, `aiohttp`) ប្រើ `/openai/deployments/{name}/chat/completions?api-version=...` ត្រូវប្តូរទៅ `/openai/v1/responses`។ ខ្លឹមសារសំណើប្រើ `input` ជំនួស `messages` ត្រូវការចំនួន `max_output_tokens` និង `store` ហើយតម្លៃការស្នើសុំប្រែប្រួល `api-version` ត្រូវលុបចោល។ ខ្លឹមសារឆ្លើយតបមាននៅ `output[0].content[0].text` — **មិនមែន** `output_text` ដែលជាគុណលក្ខណៈ SDK មិនមាននៅក្នុង JSON REST ដើម។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->