# പ്രശ്നപരിഹാരം, അപകട പട്ടിക & ഗൊച്ചാസ്

## 400s പ്രശ്നപരിഹാരം

| പിശക് | പരിഹാരം |
|-------|-----|
| `missing_required_parameter: tools[0].name` | ടൂൾ നിർവചനം പഴയ Chat Completions ന്റെ നസ്‌റ്റുചെയ്ത ഫോർമാറ്റ് ഉപയോഗിക്കുന്നു | `{"type": "function", "function": {"name": ...}}` ൽ നിന്നു `{"type": "function", "name": ..., "parameters": ...}` എന്ന കൊണ്ട് ഫ്‌ളാറ്റൻ ചെയ്യുക — name, description, parameters മുകളിൽ തലത്തിൽ വന്നിരിക്കണം |
| `unknown_parameter: input[N].tool_calls` | മൽട്ടി-ടേൺ ടൂൾ ഫലം പഴയ Chat Completions ഫോർമാറ്റ് ഉപയോഗിക്കുന്നു | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` എന്നത് `response.output` ഐറ്റങ്ങൾക്ക് + `{"type": "function_call_output", "call_id": ..., "output": ...}` കൊണ്ട് മാറ്റുക |
| `invalid_function_parameters: 'required' is required` | `strict: true` ടൂളിൽ `required` അറേ കാണാൻ കഴിയുന്നില്ല | `strict: true` ആയാൽ എല്ലാ പ്രോപ്പർട്ടീസുകളും `required` ലിസ്റ്റിൽ ഉൾപ്പെടുത്തണം, കൂടാതെ `additionalProperties: false` സെറ്റ് ചെയ്യണം |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` ടൂളിൽ `additionalProperties: false` കാണാൻ കഴിയുന്നില്ല | `"additionalProperties": false` പാരാമീറ്ററുകളുടെ ഒബ്ജക്റ്റിൽ ചേർക്കുക |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID യുടെ പ്രിഫിക്സ് തെറ്റാണ് | ഫംഗ്ഷൻ കോളിന് `_fc` എന്നത് തുടങ്ങണം (ഉദാ: `fc_example1`), `call_` അല്ല |
| `missing_required_parameter: text.format.name` | ഫോർമാറ്റ് ഡിക്കിൽ `"name"` കീ ചേർക്കൂ (ഉദാ, `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` ഒരു ഡിക്‌ഷനറിയായി(`type`, `name`, `strict`, `schema` കീകൾ ഉള്ളത്) ഉറപ്പാക്കുക — സ്ട്രിംഗ് അല്ലാതിരിക്കുക |
| `invalid input content type` | Chat `text` ഉപയോഗിക്കുന്നതിന് പകരം `input_text`/`output_text` കോൺറെന്റ് ടൈപ്പുകൾ ഉപയോഗിക്കുക |
| `invalid input content type` (image) | ഇമേജ് കോൺറെന്റ് ഇനി `"type": "image_url"` ഉപയോഗിക്കുന്നു | `"type": "input_image"` ആയി മാറ്റുക |
| `Expected object, got string` on `image_url` | `image_url` ഇനിയും നസ്‌റ്റുചെയ്ത ഒബ്ജക്റ്റ് ആണ് `{"url": "..."}` | ഒരു ലളിതമായ സ്ട്രിംഗ് ആയി ഫ്‌ളാറ്റൻ ചെയ്യുക: `"image_url": "https://..."` അല്ലെങ്കിൽ `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAIയിൽ കുറഞ്ഞത് **16** ആണ്. പരീക്ഷണങ്ങൾക്കായി 50+ ഉപയോഗിക്കുക, പ്രൊഡക്ഷനിൽ 1000+ ആണ് ശുപാർശ. |
| `429 Too Many Requests` during streaming | നിരക്ക് പരിധി കുറവാണ്. streaming `try/except` ൽ പൊതിയുക, error JSON ഫ്രണ്ട്എന്റിലേക്ക് നൽകുക, ബാക്കോഫ്/റെട്രി നടപ്പാക്കുക. |
| `KeyError: 'innererror'` on content filter error | Responses APIയിൽ content filter പിശക് ബോഡി ഘടന മാറ്റം | Chat Completions `error.body["innererror"]["content_filter_result"]` ഉപയോഗിച്ചിരുന്നു; Responses API `error.body["content_filters"][0]["content_filter_results"]` (ബഹുഭു: ഒരുarrayയിൽ). എല്ലാ `innererror` ആക്സസ് പുനഃസംരചിക്കുക. |

---

## മൈഗ്രേഷൻ അപകട പട്ടിക

| ലക്ഷണം | സാധ്യതയുള്ള തകർച്ച | പരിഹാരം |
|---------|---------------|-----|
| ശൂന്യമായ `output_text` / ട്രങ്കേറ്റഡ് പ്രതികരണം | `max_output_tokens` തർക്കം മോഡലുകൾക്കായി വളരെ കുറവാണ് | `max_output_tokens=1000` അല്ലെങ്കിൽ അതിലധികം സജ്ജമാക്കുക — reasoning ടോക്കണുകൾ പരിധിയിലായി കണക്കാക്കപ്പെടുന്നു |
| `400 invalid_type: text.format` | `response_format` സ്ട്രിംഗ് പാസ്സാക്കിയതു; `text.format` ഡിച്ച് പാസ്സാക്കണം | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` ഉപയോഗിക്കുക |
| `/openai/v1/responses` ൽ `404 Not Found` | തെറ്റായ `base_url` — `/openai/v1/` സഫിക്സ് ഇല്ല | ഉറപ്പാക്കുക `base_url=f"{endpoint}/openai/v1/"` (ട്രെയ്‌ലിംഗ് സ്ലാഷ് ഉൾപ്പെടെ) |
| `401 Unauthorized` `OpenAI()` ലേക്ക് മാറിയതിന് ശേഷം | `api_key` സെറ്റ് ചെയ്‌തിട്ടില്ല അല്ലെങ്കിൽ ടോക്കൺ പ്രൊവൈഡർ ശരിയായി പാസ്സായിട്ടില്ല | EntraID: `api_key=token_provider` (Callable). API കീയ്ക്കായി: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| മോഡൽ `deployment not found` തിരിച്ചു നൽകുന്നു | `model` പാരാമീറ്റർ നിങ്ങളുടെ Azure ഡിപ്ലോയ്‌മെന്റ് നാമവുമായി പൊരുത്തപ്പെടുന്നില്ല | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` ഉപയോഗിക്കുക — ഇത് മോഡൽ അല്ല, ഡിപ്ലോയ്‌മെന്റ് നാമം ആണ് |
| `json.loads(resp.output_text)` `JSONDecodeError` എററർ ഉയരുന്നു | സ്കീമ പ്രാബല്യം ഇല്ല അല്ലെങ്കിൽ മോഡൽ സ്ട്രിക്റ്റ് JSON പിന്തുണയ്ക്കുന്നില്ല | സ്കീമയിൽ `"strict": True` ഉറപ്പാക്കുക; മോഡൽ സ്ട്രക്ചર્ડ ഔട്ട്പുട്ട് പിന്തുണയ്ക്കുകയാണെന്ന് പരിശോധന നടത്തുക |
| Streaming ൽ `delta` ഇവന്റുകൾ കാണപ്പെടുന്നില്ല | തെറ്റായ ഇവന്റ് തരം പരിശോധിക്കുന്നു | `event.type == "response.output_text.delta"` ഉപയോഗിക്കുക, Chat ന്റെ `chat.completion.chunk` അല്ല |
| മൈഗ്രേഷൻക്ക് ശേഷം ചിത്രം ഇൻപുട്ടിൽ `400` പിശക് | ഇമേജ് കോൺറെന്റ് ടൈപ്പ് അപ്‌ഡേറ്റ് ചെയ്‌തിട്ടില്ല | `"type": "image_url"` → `"type": "input_image"` ആയി മാറ്റുക; `"image_url": {"url": "..."}` → `"image_url": "..."` ലളിതമായ സ്ട്രിംഗ് ആയി ഫ്‌ളാറ്റൻ ചെയ്യുക |
| ടൂൾ കോളുകൾ അനന്തമായി ലൂപ്പ് ചെയ്യുന്നു | ഫോളോ-അപ്പ് `input` ൽ ടൂൾ ഫലം കാണുന്നില്ല | ടൂൾ നടപ്പാക്കിയശേഷം, അടുത്ത അഭ്യർത്ഥനയിലെ `input` ൽ `{"type": "function_call_output", "call_id": ..., "output": ...}` ഇനം ചേർക്കുക |
| GPT-5 അല്ലെങ്കിൽ o-സമ്പ്രദായങ്ങളോടുള്ള `temperature` പിശക് | 1 അല്ലാത്ത സാംഗത്യമുള്ള `temperature` മൂല്യം | GPT-5, o-സമ്പ്രദായ മോഡലുകൾക്കായി `temperature` നീക്കം ചെയ്യുക അല്ലെങ്കിൽ 1 ആക്കി സജ്ജമാക്കുക (o1, o3-mini, o3, o4-mini) |
| o-സമ്പ്രദായങ്ങളോടുള്ള `top_p` പിശക് | `top_p` പിന്തുണപ്പെടുത്തുന്നില്ല | o-സമ്പ്രദായ മോഡലിലേക്ക് നിശോധിക്കുന്നപ്പോൾ `top_p` നീക്കം ചെയ്യുക |
| `max_completion_tokens` തിരിച്ചറിയുന്നില്ല | Azure-നിർദ്ദിഷ്ട പാരാമീറ്റർ ഉപയോഗിക്കുന്നു | `max_completion_tokens` ന്റെ പകരം `max_output_tokens` ഉപയോഗിക്കുക. o-സമ്പ്രദായത്തിന് 4096+ സജ്ജമാക്കുക (reasoning ടോക്കൺ പരിധിയിൽ കണക്കാക്കപ്പെട്ടു). |
| o-സമ്പ്രదായത്തിൽ നിന്ന് ശൂന്യമായ / ട്രങ്കേറ്റഡ് ഔട്ട്പുട്ട് | `max_output_tokens` വളരെ താഴെയാണ് | ഓ-സീരീസ് reasoning ടോക്കൺ ഉപയോഗിക്കുന്നു. `max_output_tokens=4096` അല്ലെങ്കിൽ അതിൽ ഉയർന്ന മൂല്യം സജ്ജമാക്കുക — 500-1000 അല്ല. |
| `400 integer_below_min_value` `max_output_tokens` ൽ | മൂല്യം 16 ലെ താഴെയാണ് | Azure OpenAI `max_output_tokens >= 16` ഉറപ്പാക്കുന്നു. smoke ടെസ്റ്റിനായി 50+, പ്രൊഡക്ഷനായി 1000+ ഉപയോഗിക്കുക. പഴയ `max_tokens` ൽ അതിനൊന്നുമില്ല. |
| Streaming മധ്യത്തിൽ `429 Too Many Requests` | Azure OpenAI നിരക്കിന്റെ പരിധി | സ്റ്റ്രീമിംഗ് കുത്തകക്ക് പിഴവില്ലാതെ ഒറ്റപ്പെട്ടു പോകുന്നു. എല്ലായ്പ്പോഴും `async for event in await coroutine:` ട്രൈ/എക്സെപ്റ്റിൽ പൊതിയുക, `{"error": str(e)}` ഫ്രണ്ട്എന്റിലേക്ക് നൽകുക. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | തെറ്റായ ടെനന്റ് അല്ലെങ്കിൽ ലോഗിൻ ചെയ്തില്ല | `tenant_id=os.getenv("AZURE_TENANT_ID")` വ്യക്തമായി പാസ്സായി നൽകുക. ലൊക്കലായി `azd auth login --tenant <tenant-id>` റൺ ചെയ്യുക. |
| GitHub മോഡലുകൾ ഉപയോഗിച്ച് `404 Not Found` (`models.github.ai`) | GitHub മോഡലുകൾ Responses API പിന്തുണയില്ല | GitHub മോഡൽ കോഡ് പാത മുഴുവൻ നീക്കം ചെയ്യുക. Azure OpenAI, OpenAI അല്ലെങ്കിൽ പരിഗണനക്കോപ്പുള്ള ലോക്കൽ എൻഡ്‌പോയിന്റ് മാത്രം ഉപയോഗിക്കുക (ഉദാ, Ollama Responses പിന്തുണയുമായി). |
| MAF `OpenAIChatCompletionClient` ഇനിയും Chat Completions ഉപയോഗിക്കുന്നു | 1.0.0+ ൽ പാഴ്‌സ് ചെയ്യാത്ത MAF ക്ലയന്റ് | MAF 1.0.0+ ൽ, `OpenAIChatClient` Responses API ലം മുഖ്യമായി ഉപയോഗിക്കുന്നു. `OpenAIChatCompletionClient` മാറ്റി `OpenAIChatClient` ഉപയോഗിക്കുക. pre-1.0.0 ൽ `agent-framework-openai>=1.0.0` അപ്ഡേറ്റ് ചെയ്യുക. |
| LangChain ഏജന്റ് ടൂൾ കോളുകൾ ഉപയോഗിച്ച് ശൂന്യമായ ഫോലം നൽകുന്നു അല്ലെങ്കിൽ പരാജയപ്പെടുന്നു | `ChatOpenAI` Responses API ഉപയോഗിക്കുന്നില്ല | `ChatOpenAI(...)` ൽ `use_responses_api=True` ചേർക്കുക. മറുപടി സന്ദേശങ്ങളിൽ `.content` ൽ നിന്ന് `.text` ആയി മാറ്റുക. |
| content filter പിശക് കൈകാര്യം ചെയ്യുമ്പോൾ `KeyError: 'innererror'` | Responses APIയെ അടിസ്ഥാനമാക്കി പിശക് ബോഡി ഘടന മാറ്റം | `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` പുനഃരചിക്കുക. `innererror` വ്രാപ്പർ ഇല്ലായ്മ; content filter വിവരങ്ങൾ ഇപ്പോൾ ടോപ്പ്-ലെവൽ `content_filters` ആറേയിൽ, ഓരോ എൻട്രിയിലെ `content_filter_results` (പുല്പറാൾ) ഉൾപ്പെടെ. |
| `/openai/deployments/.../chat/completions` ലേക്ക് റാ HTTP കോളിൽ 404 | പഴയ Chat Completions REST എൻഡ്പോയിന്റ് | URL പുനർലേഖനം `/openai/v1/responses`. അഭ്യർത്ഥന ബോഡി മാറ്റം: `messages` → `input`, `max_output_tokens` + `store: false` ചേർക്കുക, `api-version` ക്വറി പാറ മാറ്റുക. മറുപടി പാഴ്സിംഗ് മാറ്റം: `choices[0].message.content` → `output[0].content[0].text` (കുറിപ്പ്: `output_text` SDK സൗകര്യപ്രദമാകുന്നു, കാച്ച_RAW_REST JSONയിൽ ഇല്ല). |

---

## ഗൊച്ചാസ്

1. മുമ്പ് ചാറ്റ് ഉപയോഗിച്ച് സംഭാഷണ അവസ്ഥ കൈകാര്യം ചെയ്തിരുന്നെങ്കിൽ, Responses-നൊപ്പം നിങ്ങളുടെ സ്വന്തം അവസ്ഥ വ്യക്തമായി കൈകാര്യം ചെയ്യുക.
2. പാരമ്പര്യമായ `max_tokens` ൽ നിന്ന് `max_output_tokens` നെ മുൻഗണന നൽകുക.
3. `gpt-5` ലേക്ക് മൈഗ്രേറ്റ് ചെയ്യുമ്പോൾ, `temperature` നിർദ്ദേശിക്കാതെ അല്ലെങ്കിൽ `1` ആയി സജ്ജമാക്കിയിരിക്കണമെന്ന് ഉറപ്പാക്കുക.
4. ചാറ്റിൽ `content[].type: "text"` നെ Responses ൽ `content[].type: "input_text"` ആയി മാറ്റുക ഉപയോക്താവിന്റെയും സിസ്റ്റത്തിന്റെയും ഇൻപുട്ടുകൾക്ക്.
5. `text.format` ക്ക് ഒരു അനുയോജ്യമായ ഡിക്‌ഷനറി നൽകുക (ഉദാ: `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ലളിതമായ സ്ട്രിംഗ് അല്ല.
6. `seed` പാരാമീറ്റർ Responses ൽ പിന്തുണയ്ക്കുന്നില്ല; അഭ്യർത്ഥനകളിൽ നിന്ന് അത് നീക്കം ചെയ്യുക.
7. **Reasoning**: മൂല കോഡ് ഇതിനകം ഉപയോഗിച്ചിരുന്നാൽ മാത്രം `reasoning` ഉൾപ്പെടുത്തുക. ഇത് ഇല്ലാത്ത API കോൾസുകളിൽ ചേർക്കാൻ ശ്രമിക്കരുത് — പല മോഡലുകളും (ഉദാ: gpt-4o-mini) ഈ പാരാമീറ്റർ പിന്തുണയ്ക്കുന്നില്ല.
8. **`max_output_tokens` വലിപ്പം**: reasoning മോഡലുകൾക്ക് (GPT-5-mini, GPT-5, o-സീരീസ്), `max_output_tokens=4096` അല്ലെങ്കിൽ അതിൽ കൂടുതൽ സജ്ജമാക്കുക — 50–1000 അല്ല. മോഡൽ കാണുന്ന ഔട്ട്പുട്ടും മുൻപ് reasoning ടോക്കണുകൾ ഉപയോഗിക്കുന്നു; വളരെ കുറഞ്ഞ പരിധി ട്രങ്കേറ്റഡ് അല്ലെങ്കിൽ ശൂന്യമായ ഫലം ഉണ്ടാക്കും.
9. **O-സീരീസ് `max_completion_tokens`**: മൂല കോഡ് `max_completion_tokens` (o-സീരീസ് Azure-നിർദ്ദിഷ്ടം) ഉപയോഗിച്ചിരുന്നെങ്കിൽ, അത് `max_output_tokens` ൽ മാറ്റുക. Responses API `max_completion_tokens` സ്വീകരിക്കുന്നില്ല.
10. **O-സീരീസ് `reasoning_effort`**: മൂല കോഡ് `reasoning_effort` (താഴ്ന്നത്/മധ്യ/ഉയർന്ന) ഉപയോഗിച്ചിരുന്നെങ്കിൽ, Responses API കോൾിൽ `reasoning={"effort": "<value>"}` എന്നാക്കുക.
11. **O-സീരീസ് streaming വൈകിപ്പ്**: O-സീരീസ് മോഡലുകൾ പുറത്ത് വരുന്നതിന് മുമ്പ് ഇൻറേണൽ reasoning നടത്തുന്നു. streaming ചെയ്യുമ്പോൾ, ആദ്യത്തെ `response.output_text.delta` ഇവന്റിനുമുന്നിൽ ദീർഘമായ ഒരു വൈകിപ്പ് പ്രതീക്ഷിക്കുക. ഇത് സാധാരണമാണ് — മോഡൽ reasoning ചെയ്യുകയാണ്, തടസ്സപ്പെടുന്നതല്ല.
9. **`_azure_ad_token_provider` ഇല്ലാതായി**: `AsyncOpenAI` / `OpenAI` ൽ `_azure_ad_token_provider` സവിശേഷത ഇല്ല. ഈ ആട്രിബ്യൂട്ടിലേക്ക് ആക്സസ് നടത്തുന്ന ടെസ്റ്റുകൾ അല്ലെങ്കിൽ കോഡ് `AttributeError` ഉണ്ടാകാം. ടോക്കൺ പ്രൊവൈഡർ `api_key` ആയി പാസ്സാക്കിയിട്ടുള്ളതിനാൽ ക്ലയന്റ് ഒബ്ജക്റ്റിൽ പരിശോധന അളക്കാനാകില്ല.
10. **Snapshot / ഗോൾഡൻ ഫയലുകൾ**: ടെസ്റ്റ് സ്യൂട്ട് snapshot ടെസ്റ്റിംഗ് ഉപയോഗിക്കുന്നുവെങ്കിൽ, **എല്ലാ** Chat Completions streaming രൂപങ്ങൾ (`choices[0]`, `content_filter_results`, `function_call` മുതലായവ) അടങ്ങിയ snapshot ഫയലുകളും പുതിയ Responses രൂപത്തിലേക്ക് അപ്ഡേറ്റ് ചെയ്യണം. ഇത് മിസ്സ് ചെയ്യുക എളുപ്പമാണ്, snapshot അസേർഷൻ പരാജയങ്ങൾക്ക് കാരണമാകും.
11. **Mock മോങ്കിപ്പാച്ച് പാത**: മോങ്കിപ്പാച്ച് ലക്ഷ്യം `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (അഥവാ സിങ്കിനായി `Responses.create`) ആയി മാറി. പഴയ പാത ഉപയോഗിക്കുന്നതിൽ മൗനം വഹിക്കും — മോക്ക് ഇടപെടുകയില്ല, ടെസ്റ്റുകൾ യഥാർത്ഥ API-വിൽ എത്തുകയും പരാജയപ്പെടുകയും ചെയ്യും.
12. **`input` അല്ല `messages`**: മോക്ക് ഫങ്ഷനുകൾ `kwargs.get("input")` പാരായണം ചെയ്യണം, `kwargs.get("messages")` അല്ല. Responses API സംഭാഷണ ചരിത്രത്തിനായി `input` ഉപയോഗിക്കുന്നു.
13. **Env വാരിയബിൾ നാമം**: Azure Identity SDK `ManagedIdentityCredential(client_id=...)` ഉപയോഗിക്കുന്നതിന് `AZURE_CLIENT_ID` ( `AZURE_OPENAI_CLIENT_ID` അല്ല) ഉപയോഗിക്കുന്നു. ടെസ്റ്റുകളിൽ, .env ഫയലുകളിൽ, ആപ്പ് സെറ്റിംഗ്സിലും Bicep/ഇൻഫ്രയിലും പുനർനിർവചിക്കുക.
14. **`max_output_tokens` കുറഞ്ഞത് 16 ആണ്**: Azure OpenAI 16-ൽ താഴെയുള്ള മൂല്യങ്ങളെ `400 integer_below_min_value` കൊണ്ട് తిరസ്ക്കരിക്കും. smoke ടെസ്റ്റിനായി `50`, പ്രൊഡക്ഷനായി `1000+` ഉപയോഗിക്കുക. പഴയ `max_tokens` യ്ക്ക് ഇത്തരം അതിതൻമല്ല.
15. **`tenant_id` AzureDeveloperCliCredential-നായി**: Azure OpenAI റിസോഴ്‌സ് വ്യത്യസ്ത ടെനന്റിൽ ഉണ്ടെങ്കിൽ, `tenant_id` വ്യക്തമായി പാസ്സു ചെയ്യണം — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. ഇല്ലാതെ, ക്രെഡൻഷ്യൽ തെറ്റായ ടെനന്റ് ഉപയോഗിച്ച് മൗനമായി `401` തിരിച്ച് നൽകും.
16. **സ്റ്റ്രീമിംഗിൽ നിരക്ക് പരിധികൾ വ്യത്യസ്തമായി പ്രത്യക്ഷപ്പെടും**: Chat Completions ഉപയോഗിക്കുമ്പോൾ 429 സാധാരണയായി സ്റ്റ്രീം തുടങ്ങുന്നതിൽ തടസ്സം സൃഷ്ടിക്കും. Responses API streaming ഉപയോഗിക്കുമ്പോൾ, 429 സ്റ്റ്രീമിന്റെ നടുനിലയിൽ സംഭവിക്കും — അസിങ്ക് ഇറ്ററേറ്റർ എക്സെപ്ഷൻ ഉയർത്തും. എല്ലായ്പ്പോഴും streaming ലൂപ്പിനെ `try/except` ൽ പൊതിയുകയും error JSON ലൈൻ ഫ്രണ്ട്എന്റിലേക്ക് നൽകുകയും ചെയ്യുക.

17. **വെബ് ആപ്പുകൾക്കായി സ്ട്രീമിങ് പിശക് കൈകാര്യം ചെയ്യൽ അനിവാര്യമാണ്**: പാറ്റേൺ `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` നിർണ്ണായകമാണ്. ഇതില്ലാതെ, SSE/JSONL സ്ട്രീം സർവർ-വശം anumang പിശകിൽ മൗനം ചെലുത്തി മരിക്കും, ഫ്രണ്ട്‌എൻഡ് തളരും.  
18. **ടൂൾ നിർവചനങ്ങൾ ഫ്ലാറ്റ് ഫോർമാറ്റ് ഉപയോഗിച്ചിരിക്കണം**: Responses API `{"type": "function", "name": ..., "parameters": ...}` പ്രതീക്ഷിക്കുന്നു — Chat Completions-ലെ നസ്റ്റ് ചെയ്ത രൂപം `{"type": "function", "function": {"name": ..., "parameters": ...}}` അല്ല. ഫംഗ്ഷൻ-കോളിംഗ് കോഡിനുള്ള ഏറ്റവും സാധാരണ മൈഗ്രേഷൻ പിശക് ഇതാണ്.  
19. **`pydantic_function_tool()` അനുയോജ്യമല്ല**: `openai.pydantic_function_tool()` ഹെൽപ്പർ പഴയ നസ്റ്റ് ചെയ്ത ഫോർമാറ്റ് ഇപ്പോഴും ജനറേറ്റ് ചെയ്യുന്നു. `responses.create()` ഉപയോഗിക്കുമ്പോൾ ഇത് ഉപയോഗിക്കരുത്. ടൂൾ സ്കീമകൾ മാന്യുവലായി നിർവ്വചിക്കുക അല്ലെങ്കിൽ ഔട്ട്‌പുട്ട് ഫ്ലാറ്റ് ചെയ്യുക.  
20. **ടൂൾ ഫലങ്ങൾ `function_call_output` ആണ് ഉപയോഗിക്കുന്നത്, `role: tool` അല്ല**: ഒരു ടൂൾ പ്രവർത്തിപ്പിച്ചതിനു ശേഷം `{"type": "function_call_output", "call_id": ..., "output": ...}` ചേർക്കുക — `{"role": "tool", "tool_call_id": ..., "content": ...}` അല്ല. അസിസ്റ്റന്റിന്റെ ടൂൾ അഭ്യർത്ഥനയ്ക്ക് `messages.extend(response.output)` ഉപയോഗിക്കുക — മാന്യുവൽ `{"role": "assistant", "tool_calls": [...]}` ഡിക്കციൻറെസറി അല്ല.  
21. **`strict: true` ന് `required` + `additionalProperties: false` ആവശ്യമാണ്**: ടൂളിൽ `strict: true` ഉപയോഗിക്കുമ്പോൾ, ഓരോ പ്രോപ്പർട്ടിക്കും `required` അറെയിൽ ഉൾപ്പെടണം, കൂടാതെ `additionalProperties` ആണ് `false` ആയിരിക്കണം. ഏതൊന്നും ലഭിക്കാത്ത പക്ഷം 400 പിശക് വരും.  
22. **ഫംഗ്ഷൻ കോളിന് ഐഡികൾ പ്രത്യേക പ്രിഫിക്സുകൾ ഉണ്ട്**: ഫ്യൂ-ഷോട്ട് `function_call` ഇനങ്ങൾ `input` ൽ നൽകുമ്പോൾ, `id` ഫീൽഡ് `fc_` ഉപയോഗിച്ച് തുടങ്ങണം, `call_id` ഫീൽഡ് `call_` കൊണ്ട് തുടങ്ങണം (ഉദാ: `"id": "fc_example1", "call_id": "call_example1"`). പഴയ Chat Completions ലെ `call_` പ്രിഫിക്സ് `id` ആയി ഉപയോഗിക്കുന്നത് നിരസിക്കപ്പെടും.  
23. **GitHub Models Responses API പിന്തുണയ്ക്കുന്നില്ല**: ആപ്പിന് GitHub Models കോഡ് പാത (`base_url` `models.github.ai` അല്ലെങ്കിൽ `models.inference.ai.azure.com` സൂചിപ്പിക്കുന്നത്) ഉണ്ടെങ്കിൽ, അത് പൂർണ്ണമായും നീക്കം ചെയ്യുക. മൈഗ്രേഷൻ പാതയില്ല — Azure OpenAI, OpenAI, അല്ലെങ്കിൽ അനുയോജ്യമായ ലോക്കൽ എന്റ്പോയിന്റിലേക്ക് മാറുക.  
24. **ഉള്ളടക്ക ഫിൽറ്റർ പിശക് ബോഡി ഘടന മാറി**: Chat Completions പിശകുകൾ `error.body["innererror"]["content_filter_result"]` (ഏകവചനം) ഉപയോഗിച്ചിരുന്നു. Responses API പിശകുകൾ `error.body["content_filters"][0]["content_filter_results"]` (ബഹുവചനം, ഒരു അറെയ് ഉള്ളിൽ) ഉപയോഗിക്കുന്നു. `innererror` കീ ഇനി നിലവിലില്ല. നേരിട്ട് `innererror` ആക്‌സസ് ചെയ്ത കോഡ് റൺടൈമിൽ `KeyError` ഉത്പാദിപ്പിക്കും — ഉള്ളടക്ക ഫിൽറ്റർ യഥാർത്ഥത്തിൽ പ്രവർത്തിക്കുമ്പോഴെ മാത്രം ഇത് പ്രത്യക്ഷപ്പെടുന്നതിനാൽ മൈഗ്രേഷനിൽ ഇത് ശ്രദ്ധിക്കാതെ പോകാം. മൈഗ്രേഷൻ സമയത്ത് എല്ലായ്പ്പോഴും `innererror` grep ചെയ്യുക.  
25. **റോ ഹ്ട്ടപി കോളുകൾക്ക് URL + ബോഡി പുനഃരചനം ആവശ്യമാണ്**: Azure OpenAI REST നെ സിദ്ധമായും (`requests`, `httpx`, `aiohttp` വഴി) `/openai/deployments/{name}/chat/completions?api-version=...` ഉപയോഗിച്ച് വിളിക്കുന്ന ആപ്പുകൾ `/openai/v1/responses` എന്നിലേക്ക് മാറണം. അഭ്യർത്ഥന ബോഡി `messages`-ന്റെ സഥാനത്തു `input` ഉപയോഗിക്കുന്നു, കൂടാതെ `max_output_tokens` ഉം `store` ഉം ആവശ്യമാണ്, `api-version` ക്വറി പാരാമീറ്റർ ഒഴിവാക്കിയിട്ടുണ്ട്. പ്രതികരണ ബോഡി ടെക്സ്റ്റ് `output[0].content[0].text` ൽ ആണ് — **`output_text` അല്ല**, അത് SDK സൗകര്യമുള്ള പ്രോപ്പർട്ടി ആണ്, റോ REST JSON ൽ ഇല്ല.  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->