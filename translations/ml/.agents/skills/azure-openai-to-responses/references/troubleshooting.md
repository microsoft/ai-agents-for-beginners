# തകരാര്‍ പരിഹാരങ്ങള്‍, റിസ്ക്ക് പട്ടിക & ശ്രദ്ധിക്കേണ്ട കാര്യങ്ങള്‍

## 400 ബന്ധപ്പെട്ട പിശകുകള്‍ പരിഹരിക്കല്‍

| പിശക് | പരിഹാരം |
|-------|-----|
| `missing_required_parameter: tools[0].name` | ടൂൾ നിർവചനം പഴയ Chat Completions നസ്റ്റ് ഫോർമാറ്റുകൾ ഉപയോഗിക്കുന്നു | `{"type": "function", "function": {"name": ...}}`-ൽ നിന്നു `{"type": "function", "name": ..., "parameters": ...}`-ലേക്ക് ഫ്ലാറ്റ് ചെയ്യുക — പേര്, വിശദീകരണം, പാരാമീറ്ററുകൾ മുകളിൽ നൽകണം |
| `unknown_parameter: input[N].tool_calls` | മൾട്ടി-ടേൺ ടൂൾ ഫലങ്ങൾ പഴയ Chat Completions ഫോർമാറ്റ് ഉപയോഗിക്കുന്നു | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` മാറ്റി `response.output` ഇനങ്ങൾ + `{"type": "function_call_output", "call_id": ..., "output": ...}` ഉപയോഗിക്കുക |
| `invalid_function_parameters: 'required' is required` | `strict: true` ടൂളിൽ `required` അറേ കാണുന്നില്ല | `strict: true` ആയപ്പോൾ, എല്ലാ പ്രോപ്പർട്ടികളും `required`-ലിസ്റ്റിൽ ഉൾപ്പെടുത്തണം, കൂടാതെ `additionalProperties: false` ഉണ്ടായിരിക്കണം |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` ടൂളിൽ `additionalProperties: false` കാണുന്നില്ല | പാരാമീറ്ററുകളുടെ ഒബ്ജക്റ്റിൽ `"additionalProperties": false` ചേർക്കുക |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ഐഡി തെറ്റായ പ്രിഫിക്സ് എടുത്തിരിക്കുന്നു | ഫങ്ഷൻ കോളിന്റ ഐഡികൾ `fc_` (ഉദാഹരണം: `fc_example1`) എന്ന പ്രിഫിക്സ് ഉപയോഗിക്കണം, `call_` അല്ല |
| `missing_required_parameter: text.format.name` | ഫോർമാറ്റ് ഡിക്ഷണറിയില `"name"` കീ ചേർക്കുക (ഉദാ: `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` dict ആയിരിക്കണം, `type`, `name`, `strict`, `schema` കീസുള്‍പ്പെടെ — string അല്ല |
| `invalid input content type` | Chat `text`-ന്റെ പകരം `input_text`/`output_text` കൺറെന്റ് ടൈപ്പുകൾ ഉപയോഗിക്കുക |
| `invalid input content type` (image) | ഇമേജ് കൺറെന്റ് `"type": "image_url"` എന്ന് ഇപ്പോഴും ഉപയോഗിക്കുന്നു | `"type": "input_image"` ആയി മാറ്റുക |
| `Expected object, got string` on `image_url` | `image_url` ഇനത്തിൽ nested object `{"url": "..."}` ഇപ്പോഴും ഉണ്ട | ഫ്ലാറ്റ് ചെയ്ത് സാദാരണ സ്ട്രിങാക്കി മാറ്റുക: `"image_url": "https://..."` അല്ലെങ്കിൽ `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI-യിൽ കുറവ് തീരുവ **16** ആണ്. ടെസ്റ്റുകൾക്കായി 50+ ഉപയോഗിക്കുക, പ്രൊഡക്ഷനായി 1000+ തീരുമാനിക്കുക. |
| `429 Too Many Requests` during streaming | റേറ്റ് ലിമിറ്റഡ് ആണ്. സ്റ്റ്രീമിംഗ് try/except-ൽ ഘടിപ്പിച്ച്, എറർ JSON ഫ്രണ്ട്‌എന്‍ഡിലേക്ക് നൽകുക, ബാക്ക്ഓഫ്/റിട്രൈ നടപ്പിലാക്കുക. |
| `KeyError: 'innererror'` on content filter error | Responses API-യിൽ content filter പിഴവിന്റെ ബോഡി ഘടന മാറ്റി | Chat Completions `error.body["innererror"]["content_filter_result"]` ഉപയോഗിച്ചിരുന്നു; Responses API `error.body["content_filters"][0]["content_filter_results"]` (ബഹുവചനവും ആറെ ഉൾക്കൊള്ളുന്നു) ഉപയോഗിക്കുന്നു. എല്ലാ `innererror` ആക്സസ് പുനഃരചയിക്കുക. |

---

## മൈഗ്രേഷൻ റിസ്ക്ക് പട്ടിക

| ലക്ഷണം | സാധ്യതയുള്ള പിശക് | പരിഹാരം |
|---------|---------------|-----|
| ശൂന്യമായ `output_text` / മുറിച്ചെടുത്ത പ്രതികരണം | `max_output_tokens` കുറവാണ് റീസണിംഗ് മോഡലുകളിൽ | `max_output_tokens=1000` അല്ലെങ്കിൽ അതിനുശേഷം ക്രമീകരിക്കുക — റീസണിംഗ് ടോക്കണുകൾ പരിധിയിൽ കണക്കാക്കപ്പെടുന്നു |
| `400 invalid_type: text.format` | `text.format` dict പകരം `response_format` string പാസായപ്പോള്‍ | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` ഉപയോഗിക്കുക |
| `/openai/v1/responses`-ൽ `404 Not Found` | തെറ്റായ `base_url` — `/openai/v1/` സഫിക്സ് കാണുന്നില്ല | `base_url=f"{endpoint}/openai/v1/"` (ട്രെയിലിംഗ് പ്രക്രിയയോടെ) ഉറപ്പാക്കുക |
| `OpenAI()`-യിൽ മാറിയ ശേഷം `401 Unauthorized` | `api_key` സെറ്റ് ചെയ്‌തിട്ടില്ല അല്ലെങ്കിൽ ടോക്കൺ പ്രൊവൈഡർ ശരിയായി പാസായിട്ടില്ല | EntraID-യ്ക്ക്: `api_key=token_provider` (കലബിൾ). API കീക്കായി: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| മോഡൽ `deployment not found` പറയുന്നു | `model` പാരാമീറ്റർ നിങ്ങളുടെ Azure ഡിപ്പ്ലോയ്മെന്‍റ് നാമത്തോട് പൊരുത്തപ്പെടുന്നില്ല | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` ഉപയോഗിക്കുക — ഇത് ഡിപ്പ്ലോയ്മെന്‍റ് നാമമാണ്, മോഡൽ നാമം അല്ല |
| `json.loads(resp.output_text)` `JSONDecodeError` ഉയരുന്നു | സ്ക്കീമ പാലനമില്ല അല്ലെങ്കിൽ മോഡൽ സ്ട്രിക്റ്റ് JSON പിന്തുണയില്ല | സ്ക്കീമയിൽ `"strict": True` ഉറപ്പാക്കുക, മോഡൽ സ്ട്രക്ചേഡ് ഔട്ട്‌പുട്ട് പിന്തുണയ്ക്കുന്നതായി പരിശോധന നടത്തുക |
| സ്റ്റ്രീമിംഗ് `delta` ഇവന്റുകൾ കാണിക്കുന്നില്ല | തെറ്റായ ഇവന്റ് ടൈപ്പ് പരിശോധിക്കുന്നു | `event.type == "response.output_text.delta"` ഫിൽട്ടർ ചെയ്യുക, Chat-ന്റെ `chat.completion.chunk` അല്ല |
| മൈഗ്രേഷൻ കഴിഞ്ഞിട്ടില്ലാത്ത ഇമേജ് ഇൻപുട്ടിൽ `400` പിശക് | ഇമേജ് കൺറെന്റ് ടൈപ്പ് അപ്ഡേറ്റ് ചെയ്തിട്ടില്ല | `"type": "image_url"` → `"type": "input_image"` ആക്കുക, `"image_url": {"url": "..."}` → `"image_url": "..."` (സാദാരണ സ്ട്രിംഗ്) ആക്കി ഫ്ലാറ്റ് ചെയ്യുക |
| ടൂൾ കോൾസ് അനന്തമായി ലൂപ് ചെയ്യുന്നു | ഫോളോ-അപ്പ് `input`-ൽ ടൂൾ ഫലമില്ല | ഒരു ടൂൾ നടപ്പാക്കിയ ശേഷം, അടുത്ത അഭ്യർത്ഥനയിലെ `input`-ൽ `{"type": "function_call_output", "call_id": ..., "output": ...}` ഇനം ചേർക്കുക |
| GPT-5 അല്ലെങ്കിൽ o-സീരീസ് ഉപയോഗിച്ച് `temperature` പിശക് | 1 അല്ലാത്ത explicit `temperature` മൂല്യം | GPT-5, o-സീരീസ് മോഡലുകൾക്കായി `temperature` നീക്കം ചെയ്യുക അല്ലെങ്കിൽ 1 ആക്കി സജ്ജീകരിക്കുക (o1, o3-mini, o3, o4-mini) |
| o-സീരീസിൽ `top_p` പിശക് | `top_p` പിന്തുണയില്ല | o-സീരീസ് മോഡലുകളിൽ നിന്ന് `top_p` നീക്കം ചെയ്യുക |
| `max_completion_tokens` തിരിച്ചറിയപ്പെടുന്നില്ല | അസ്യൂർ-നിർദിഷ്ട പാരാമീറ്റർ ഉപയോഗിക്കുന്നു | `max_completion_tokens` പകരം `max_output_tokens` ഉപയോഗിക്കുക. o-സീരീസ്‌ക്ക് 4096+ സെറ്റ് ചെയ്യുക (റീസണിംഗ് ടോക്കണുകൾ പരിധിയിൽ കണക്കാക്കുന്നു) |
| o-സീരീസിൽ നിന്നുള്ള ശൂന്യമായ/മുറച്ചെടുത്ത ഔട്ട്‌പുട്ട് | `max_output_tokens` വളരെ കുറവ് | o-സീരീസ് അകത്തുണ്ടാകുന്ന റീസണിംഗ് ടോക്കണുകൾ ഉപയോഗിക്കുന്നു. `max_output_tokens=4096` അല്ലെങ്കിൽ അതിൽക്കൂടുതൽ സെറ്റ് ചെയ്യുക — 500–1000 അല്ല. |
| `400 integer_below_min_value` `max_output_tokens`-ന് | മൂല്യം 16-ന് താഴെ | അസ്യൂർ OpenAI `max_output_tokens >= 16` എങ്ങനെ നിർബന്ധിക്കുന്നു. സ്മോക്ക് ടെസ്റ്റുകൾക്ക് 50+, പ്രൊഡക്ഷനായി 1000+ ഉപയോഗിക്കുക |
| മിഡ്-സ്ട്രീമിൽ `429 Too Many Requests` | അസ്യൂർ OpenAI-ന്റെ റേറ്റ് പരിധി | സ്റ്റ്രീം കൈകാര്യം ചെയ്യുന്ന സമയത്ത് പിശക് ഇല്ലാതെ തകരുന്നത് സാധാരണമല്ല. സ്ട്രീമിംഗ് ലൂപ്പ് `try/except`-ൽ പൊതിഞ്ഞ് `{"error": str(e)}` ഫ്രണ്ട്‌എന്‍ഡിലേയ്ക്ക് നൽകുക. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | തെറ്റ് ടനന്റ് അല്ലെങ്കിൽ ലോഗിൻ ചെയ്തിട്ടില്ല | `tenant_id=os.getenv("AZURE_TENANT_ID")` സമ്മതിക്കുക. പ്രാദേശികമായി `azd auth login --tenant <tenant-id>` 실행ിക്കുക. |
| GitHub മോഡലുകൾ ഉപയോഗിച്ച് (`models.github.ai`) `404 Not Found` | GitHub മോഡലുകൾ Responses API പിന്തുണയ്ക്കുന്നില്ല | GitHub മോഡൽ കോഡ് പാത മുഴുവനായി നീക്കം ചെയ്യുക. Azure OpenAI, OpenAI അല്ലെങ്കിൽ Responses പിന്തുണയുള്ള അനുയോജ്യമായ ലോക്കൽ എന്റ്പോയിന്റ് (ഉദാ: Ollama) ഉപയോഗിക്കുക. |
| MAF `OpenAIChatCompletionClient` ഇപ്പോഴും Chat Completions ഉപയോഗിക്കുന്നു | 1.0.0+ ലെ പാരമ്പര്യ MAF ക്ലയന്റ് ഉപയോഗിക്കുന്നു | MAF 1.0.0+ ൽ `OpenAIChatClient` സ്വയമേവ Responses API ഉപയോഗിക്കുന്നു. `OpenAIChatCompletionClient`-നെ `OpenAIChatClient`-ൽ മാറ്റുക. pre-1.0.0 ആണെങ്കിൽ `agent-framework-openai>=1.0.0`-യിലേക്കു അപ്ഗ്രേഡ് ചെയ്യുക. |
| LangChain ഏജന്റ് ടൂൾ കോൾസ് കൊണ്ടോ ഷൂന്യമോ പരാജയപ്പെടുകയോ ചെയ്യുന്നു | `ChatOpenAI` Responses API ഉപയോഗിക്കുന്നില്ല | `ChatOpenAI(...)`-യിലേക്ക് `use_responses_api=True` ചേർക്കുക. മറുപടിയിലുള്ള `.content` → `.text` ആയി മാറ്റിവെക്കുക. |
| content filter error handler-ൽ `KeyError: 'innererror'` | Responses API-യിലെ പിശക് ബോഡി ഘടന മാറ്റപ്പെട്ടിരിക്കുന്നു | `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` എന്നാക്കി പുനഃരചയിക്കുക. `innererror` ഓവർലെപ്പ് പോയി; content filter വിശദാംശങ്ങൾ ഇപ്പോൾ ടോപ്‌ലെവൽ `content_filters` അരേയിൽ ഉണ്ട്, ഓരോ ഇനത്തിനുള്ളിൽ `content_filter_results` (ബഹുവചനവും). |
| `/openai/deployments/.../chat/completions`-ന് റോ ഡ്യൂ HTTP കോളിന് 404 | പഴയ Chat Completions REST എന്റ്പോയിന്റ് | URL `/openai/v1/responses` ആയി മാറ്റുക. അഭ്യർത്ഥന ബോഡി: `messages` → `input`, `max_output_tokens` + `store: false` ചേർക്കുക, `api-version` ക്വറി പാരാമീറ്റർ നീക്കം ചെയ്യുക. പ്രതികരണ പരാമർശം: `choices[0].message.content` → `output[0].content[0].text` (ശ്രദ്ധിക്കുക: `output_text` SDK സൗകര്യമാത്രമാണ്, റദ് REST JSON-ൽ ഇല്ല). |

---

## ശ്രദ്ധിക്കേണ്ട കാര്യങ്ങൾ

1. മുന്‍പ് Chat Completions സംഭാഷണ സ്ഥിതിവിവരം ഉപയോഗിച്ചിരുന്നെങ്കിൽ, Responses-ഉം കൂടാതെ നിങ്ങളുടെ സ്വന്തം സ്ഥിതിവിവരം വ്യക്തമായി കൈകാര്യം ചെയ്യുക.
2. പഴയ `max_tokens`-മുപരി `max_output_tokens`-ഉടേതായി ഉപയോഗിക്കുക.
3. `gpt-5`-ലേക്ക് മൈഗ്രേറ്റ് ചെയ്യുമ്പോൾ, `temperature` പ്രത്യേകിച്ചും സൂചിപ്പിച്ചിട്ടില്ലെങ്കിൽ അല്ലെങ്കിൽ `1` ആക്കി സജ്ജീകരിക്കപ്പെട്ടിരിക്കണം.
4. Chat-ന്റെ `content[].type: "text"`-നെ Responses-ൽ `content[].type: "input_text"` ആയി ഉപയോക്താവ്/സിസ്റ്റം ഇൻപുട്ടുകൾക്കായി മാറ്റുക.
5. `text.format`-നായി ഉചിതമായ ഡിക്ഷണറി നൽകുക (ഉദാ: `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), പLAIN സ്ട്രിംഗ് അല്ല.
6. Responses-ൽ `seed` പാരാമീറ്റർ പിന്തുണയ്‌ക്കാനില്ല; അതിന് അഭ്യർത്ഥനകളിൽ നിന്നും നീക്കം ചെയ്യുക.
7. **Reasoning**: മുകളിൽ ഉപയോഗിച്ചിട്ടുള്ള പ്രോഗ്രാമിൽ മാത്രമേ `reasoning` ഉൾപ്പെടുത്തേണ്ടതാണ്. ശേഷിയില്ലാത്ത API കോളുകളിൽ `reasoning` ചേർക്കേണ്ടതില്ല — പല റീസണിംഗ് മോഡലുകളും ഈ പാരാമീറ്റർ പിന്തുണയില്ല.
8. **`max_output_tokens` വലിപ്പീകരണം**: റീസണിംഗ് മോഡലുകൾ (GPT-5-mini, GPT-5, o-സീരീസ്) ഉപയോഗിക്കുമ്പോൾ, `max_output_tokens=4096` അല്ലെങ്കിൽ അതിൽ കനത്താക്കുക — 50–1000 അല്ല. മോഡൽ പ്രത്യക്ഷമായ ഔട്ട്‌പുട്ട് ഉൽപ്പാദിപ്പിക്കുന്നതിന് മുൻപ് റീസണിംഗ് ടോക്കണുകൾ അകത്ത് ഉപയോഗിക്കുന്നു; വളരെ കുറഞ്ഞ പരിധി ഉള്ളപ്പോൾ മുറിച്ചെടുത്തോ ശൂന്യമോ പ്രതികരണങ്ങൾ ഉണ്ടാകും.
9. **O-സീരീസ് `max_completion_tokens`**: മുന്നിലേക്ക് ഉപയോഗിച്ചിരുന്ന `max_completion_tokens` (o-സീരീസ് പ്രത്യേകത), മാറ്റി `max_output_tokens` ഉപയോഗിക്കുക. Responses API `max_completion_tokens` അംഗീകരിക്കുന്നില്ല.
10. **O-സീരീസ് `reasoning_effort`**: മുന്നിലാണ് `reasoning_effort` (low/medium/high) ഉപയോഗിച്ചിട്ടുള്ളത്, Responses API-യിൽ ഇത് `reasoning={"effort": "<value>"}` ആയി മാറ്റുക.
11. **O-സീരീസ് സ്ട്രീമിംഗ് കാലതാമസം**: O-സീരീസ് മോഡലുകൾ ഔട്ട്‌പുട്ട് ഉൽപ്പാദിപ്പിക്കുന്നതിന് മുമ്പ് അകത്ത് റീസണിംഗ് നടത്തുന്നു. സ്ട്രീമിംഗ് സമയത്ത് ആദ്യ `response.output_text.delta` ഇവന്റ് വരേണ്ടതിന് മുമ്പ് കൂടുതൽ വൈകിപ്പ് പ്രതീക്ഷിക്കുക. ഇതിന് സാധാരണം — മോഡൽ വിവേചനം നടത്തുകയാണ്, അറ്റകുറ്റപ്പണി അല്ല.
9. **`_azure_ad_token_provider` പോയി**: `AsyncOpenAI` / `OpenAI`-കൾക്ക് `_azure_ad_token_provider` ആട്രിബ്യൂട്ട് ഇല്ല. ഈ ആട്രിബ്യൂട്ടിലേക്ക് ആക്‌സസ് ചെയ്യുന്ന ടെസ്റ്റുകൾ/കോഡ് `AttributeError` ഉണ്ടാകും. ടോക്കൺ പ്രൊവൈഡർ `api_key` ആയി പാസ്സ് ചെയ്യുന്നതാണ്, ക്ലയന്റ് ഒബ്ജക്റ്റിൽ ഇൻസ്പെക്റ്റ് ചെയ്യാനാകുന്നവയല്ല.
10. **Snapshot / golden files**: ടെസ്റ്റ് സ്യൂട്ട് സ്നാപ്ഷോട്ട് ടെസ്റ്റിംഗ് ഉപയോഗിക്കുന്ന പക്ഷം, Chat Completions-ന്റെ സ്ട്രീമിംഗ് ഷേപ്പുകളുള്ള എല്ലാ സ്നാപ്ഷോട്ട് ഫയലുകളും Responses-ന്റെ പുതിയ ഷേപ്പിലേക്ക് അപ്ഡേറ്റ് ചെയ്യണം. ഇത് കാണാതെയായി നിൽക്കുന്നത് സ്നാപ്ഷോട്ട് അസർഷൻ ഫെയ്‌ലറുകൾക്കും കാരണമാകും.
11. **Mock monkeypatch പാത**: മൺകീപാച്ച് ടാർഗറ്റ് `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (അല്ലെങ്കിൽ sync-നായി `Responses.create`) ആയി മാറി. പഴയ പാത ഉപയോഗിക്കുന്നത് മൂക്കു തുടരില്ല — മൺകീപാച്ച് ഇടപെടാതെ, ടെസ്റ്റുകൾ യഥാർത്ഥ API-യിലേക്ക് പോവുകയും അല്ലെങ്കിൽ പരാജയപ്പെടുകയും ചെയ്യും.
12. **`input` അല്ല `messages`**: മൺക് ഫങ്ഷനുകൾ `kwargs.get("input")` വായിക്കണം, `kwargs.get("messages")` അല്ല. Responses API സംഭാഷണ ചരിത്രത്തിന് `input` ഉപയോഗിക്കുന്നു.
13. **Env വേരിയബിൾ നാമകരണം**: Azure Identity SDK `ManagedIdentityCredential(client_id=...)`-ക്കായി `AZURE_CLIENT_ID` (പഴയ `AZURE_OPENAI_CLIENT_ID` അല്ല) ഉപയോഗിക്കുന്നു. ടെസ്റ്റുകളിൽ, `.env` ഫയലുകളിൽ, ആപ്പ് ക്രമീകരണങ്ങളിൽ, Bicep/Infrastructure-ൽ ഇത് മാറ്റുക.
14. **`max_output_tokens`-ന് കുറഞ്ഞത് 16**: Azure OpenAI 16-ൽ താഴെയുള്ള മൂല്യങ്ങളെ `400 integer_below_min_value` കൊണ്ട് തള്ളും. സ്മോക്ക് ടെസ്റ്റുകൾക്ക് 50, പ്രൊഡക്ഷൻക്ക് 1000+ ഉപയോഗിച്ചെടുക്കുക. പഴയ `max_tokens`-ിനു ഇത്തരം കുറഞ്ഞ പരിധിയില്ലായിരുന്നു.
15. **`AzureDeveloperCliCredential`-ക്ക് `tenant_id` ആവശ്യമുണ്ട്**: Azure OpenAI റിസോഴ്സ് വേറെ ടനന്റിൽ ഇരിക്കുന്നപ്പോൾ, നിർബന്ധമായും `tenant_id` വ്യക്തമാക്കണം — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. ഇത് ഇല്ലാതിരുന്നാൽ കരുദിശ തെറ്റായ ടനന്റ് ഉപയോഗിച്ച് ചേർന്നു, `401` പിഴവ് സംഭാവിക്കുന്നു.
16. **സ്റ്റ്രീമിംഗിൽ റേറ്റ് ലിമിറ്റുകൾ വ്യത്യസ്തമായി പ്രത്യക്ഷപ്പെടുന്നു**: Chat Completions-ൽ 429 പിഴവ് സാധാരണയായി സ്ട്രീം ആരംഭിക്കുന്നത് തടഞ്ഞിരുന്നു. Responses API-യുടെ സ്ട്രീം പദത്തിൽ 429 പിഴവ് സ്ട്രീമിനുള്ളിലായി സംഭവിക്കാം — അസിങ്ക്രോണസ് ഇറ്ററേറ്റർ അസൂയാ ഉയർത്തും. സ്ട്രീമിംഗ് ലൂപ് എല്ലാസമയം `try/except`-ൽ പൊതിഞ്ഞ് പിഴവ് JSON ലൈൻ ഫ്രണ്ട്‌എന്‍ഡിൽ പുറപ്പെടുവിക്കുക, വേഗം gracefully കൈകാര്യം ചെയ്യാനുള്ളതിനായി.

17. **വെബ് ആപ്പുകളിലേക്കുള്ള സ്ട്രീമിംഗ് പിശക് നിർവഹണം അനിവാര്യമാണ്**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` എന്ന രീതിയാണ് അത്യന്താപേക്ഷിതം. ഇതു ഇല്ലാതെ, SSE/JSONL സ്ട്രീം സർവർ-സൈഡ് പിശകിലൊരിക്കലും നിശ്ശബ്ദമായി മരിക്കുന്നു, ഫ്‌റണ്ട്‌എнда് ഹാങ്ങ് ചെയ്യുന്നു.
18. **ടൂൾ നിർവചനങ്ങൾ ഫ്ലാറ്റ് ഫോർമാറ്റിൽ ചെയ്യണം**: Responses API ക്ക് `{"type": "function", "name": ..., "parameters": ...}` ആണ് പ്രതീക്ഷിക്കുക — Chat Completions ന്റെ നൊക്കം നൽകിയ `{"type": "function", "function": {"name": ..., "parameters": ...}}` അല്ല. ഫംഗ്ഷൻ-കോളിംഗ് കോഡിനുള്ള ഏറ്റവും സാധാരണമായ മാറ്റത്വ պിശകാണ് ഇത്.
19. **`pydantic_function_tool()` അനുകൂലമല്ല**: `openai.pydantic_function_tool()` സഹായശീലം പഴയ നൊക്കം സൃഷ്ടിക്കുന്നു. ഇതു `responses.create()` ൽ ഉപയോഗിക്കരുത്. ടൂൾ സ്കീമmler കയർ ഉപയോഗിച്ച് നിർവചിക്കുക അല്ലെങ്കിൽ ഔട്ട്പുട്ട് ഫ്ലാറ്റൻ ചെയ്യുക.
20. **ടൂൾ ഫലങ്ങൾ `function_call_output` ഉപയോഗിക്കുക, `role: tool` അല്ല**: ഒരു ടൂൾ പ്രവർത്തിപ്പിച്ചതിന് ശേഷം `{"type": "function_call_output", "call_id": ..., "output": ...}` ചേർക്കുക — `{"role": "tool", "tool_call_id": ..., "content": ...}` അല്ല. അസിസ്റ്റന്റിന്റെ ടൂൾ അഭ്യർത്ഥനയ്ക്ക് `messages.extend(response.output)` ഉപയോഗിക്കുക — കൈയോടെ `{"role": "assistant", "tool_calls": [...]}` എന്ന dict ഉപയോഗിക്കരുത്.
21. **`strict: true` ഉപയോഗിക്കുന്നത് `required` + `additionalProperties: false` ആവശ്യമാണ്**: ഒരു ടൂളിൽ `strict: true` ഉപയോഗിക്കുമ്പോൾ എല്ലാ പ്രോപ്പർട്ടികളും `required` നമ്പറിൽ പെടണം, കൂടാതെ `additionalProperties` വിസ്താരമില്ലാത്തതായി (`false`) ആണ് നിശ്ചയിക്കേണ്ടത്. ഏതെങ്കിലും ഒന്ന് ഇല്ലെങ്കിൽ 400 പിശക് വന്നു.
22. **ഫംഗ്ഷൻ കോൾ ഐഡികൾക്ക് പ്രത്യേക മുൻനാമങ്ങൾ ഉണ്ട്**: few-shot `function_call` ഇനങ്ങൾ `input`ൽ ഉപയോഗിക്കുമ്പോൾ, `id` ഫീൽഡ് `fc_` കൊണ്ടു തുടങ്ങണം, `call_id` ഫീൽഡ് നിങ്ങളുടെ `call_` കൊണ്ടു തുടങ്ങണം (ഉദാഹരണം: `"id": "fc_example1", "call_id": "call_example1"`). പഴയ Chat Completions ന്റെ `call_` മുൻനാമം `id`-ക്കായി ഉപയോഗിക്കുന്നത് നിരസിക്കപ്പെടുന്നു.
23. **GitHub മോഡലുകൾ Responses API പിന്തുണയ്ക്കുന്നില്ല**: ആപ്പിന് GitHub Models കോഡ് പാത ഉണ്ടെങ്കിൽ (`base_url` `models.github.ai` അല്ലെങ്കിൽ `models.inference.ai.azure.com` ഉൾപ്പെടുന്ന), അത് പൂർണ്ണമായി നീക്കം ചെയ്യുക. മാറ്റാനായ മാർഗമില്ല — Azure OpenAI, OpenAI അല്ലെങ്കിൽ ഒരു അനുയോജ്യമായ ലോക്കൽ എൻഡ്‌പോയിന്റിലേക്ക് മാറുക.
24. **കണ്ടന്റ് ഫിൽട്ടർ പിശക് ശരീരത്തിന്റെ ഘടന മാറിയിരിക്കുന്നു**: Chat Completions പിശകുകൾ `error.body["innererror"]["content_filter_result"]` (ഏകവചനം) ഉപയോഗിച്ചിരുന്നു. Responses API പിശകുകൾ `error.body["content_filters"][0]["content_filter_results"]` (ബഹുവചനം, ഒരു അസൂത്രിതമായ അറേയിൽ) ഉപയോഗിക്കുന്നു. `innererror` കീ ഇനി ഇല്ലാതായി. നേരിട്ട് `innererror` ആക്സസ് ചെയ്യുന്ന കോഡ് രൺടൈംിൽ `KeyError` ഉയർത്തും — ഇത് മാറ്റം സമയത്ത് കണ്ടെത്താൻ ബുദ്ധിമുട്ടുള്ളതാണ്, കാരണം ഉള്ളടക്ക ഫിൽട്ടർ യാഥാർത്ഥ്യത്തിൽ പ്രവർത്തിക്കുമ്പോഴാണ് അത് പ്രത്യക്ഷപ്പെടുക. മാർഗമാറ്റം ചെയ്യുമ്പോൾ എല്ലായ്പ്പോഴും `innererror` അഭിനിവേശം ചെയ്യുക.
25. **Raw HTTP കോളുകൾക്ക് URL + ബോഡി പുനഃരചയനം വേണം**: Azure OpenAI REST നേരിട്ട് വിളിക്കുന്ന ആപ്പുകൾ (`requests`, `httpx`, `aiohttp` വഴി) `/openai/deployments/{name}/chat/completions?api-version=...` ഉപയോഗിക്കുന്നു എങ്കിൽ `/openai/v1/responses` ആയി മാറണം. അഭ്യർത്ഥനയുടെ ബോഡി `messages` അല്ലാതെ `input` ഉപയോഗിക്കുന്നു, `max_output_tokens` ഉം `store` ഉം ആവശ്യമാണ്, കൂടാതെ `api-version` ക്വറി പാരാമീറ്റർ ഒഴിവാക്കുന്നു. മറുപടി ബോഡിയിലെ ടെക്സ്റ്റ് `output[0].content[0].text` ൽ ആണ് — **`output_text` അല്ല**, അത് ഒരു SDK സൗകര്യ പ്രോപ്പർട്ടിയാണ്, raw REST JSON-ൽ ഇല്ല.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->