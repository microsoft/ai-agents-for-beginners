# ಸಮಸ್ಯೆ ಪರಿಹಾರ, ಅಪಾಯದ ತಾಳಿಕೆ & ಗಮನಿಸಬೇಕಾದವುಗಳು

## 400 ದೋಷಗಳನ್ನು ತಪಾಸಣೆ

| ದೋಷ | ಪರಿಹಾರ |
|-------|-----|
| `missing_required_parameter: tools[0].name` | ಉಪಕರಣ ವ್ಯಾಖ್ಯಾನವು ಹಳೆಯ ಚಾಟ್ ಸಂಪೂರ್ಣೀಕರಣಗಳ ನಿಸರ್ಗೀಕೃತ ಫಾರ್ಮ್ಯಾಟ್ ಬಳಸುತ್ತಿದೆ | `{"type": "function", "function": {"name": ...}}` ರಿಂದ `{"type": "function", "name": ..., "parameters": ...}` ಗೆ ರಫ್ಲಾಟ್ ಮಾಡಿ — name, description, parameters ಮೇಲ್ಭಾಗದಲ್ಲಿ ಇರಬೇಕು |
| `unknown_parameter: input[N].tool_calls` | ಬಹು-ತಿರುವು ಉಪಕರಣ ಫಲಿತಾಂಶಗಳು ಹಳೆಯ ಚಾಟ್ ಸಂಪೂರ್ಣೀಕರಣಗಳ ಫಾರ್ಮ್ಯಾಟ್ ಬಳಕೆ ಮಾಡಿವೆ | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ಅನ್ನು `response.output` ಐಟಂಗಳೊಂದಿಗೆ ಪ್ರತಿಷ್ಠಾಪಿಸಿ + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` ಉಪಕರಣವು `required` ಸರಣಿಯನ್ನು ತಪ್ಪಿಸಿದೆ | `strict: true` ಇದ್ದಾಗ ಎಲ್ಲಾ ಗುಣಲಕ್ಷಣಗಳನ್ನು `required` ನಲ್ಲಿ ಸೂಚಿಸಬೇಕು ಮತ್ತು `additionalProperties: false` ಹೊಂದಿರಬೇಕು |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` ಉಪಕರಣವು `additionalProperties: false` ತಪ್ಪಿಸಿದೆ | ಪರಾಮೀತಿಯ ವಸ್ತುವಿಗೆ `"additionalProperties": false` ಸೇರಿಸಿ |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ಫ್ಯೂ-ಶಾಟ್ function_call ID ಗೆ ತಪ್ಪು ಪೂರ್ವಾಹ್ನ | ಫಂಕ್ಷನ್ ಕಾಲ್ ID ಗಳು `fc_` (ಉದಾ: `fc_example1`) ಒದಗಿಸಬೇಕು, `call_` ಅಲ್ಲ |
| `missing_required_parameter: text.format.name` | ಫಾರ್ಮ್ಯಾಟ್ дик್ಟ್ ಗೆ `"name"` ಕೀ ಸೇರಿಸಿ (ಉದಾ: `"name": "Output"`) |
| `invalid_type: text.format` | `text.format`ವು ಸ್ಟ್ರಿಂಗ್ ಅಲ್ಲದೇ `type`, `name`, `strict`, `schema` ಕೀಗಳೊಂದಿಗೆ dict ಆಗಿರಬೇಕು ಎಂದು ಖಚಿತಪಡಿಸಿ |
| `invalid input content type` | ಚಾಟ್ `text` ಬದಲಾಗಿ `input_text`/`output_text` ವಿಷಯ ಪ್ರಕಾರಗಳನ್ನು ಬಳಸಿ |
| `invalid input content type` (ಚಿತ್ರ) | ಚಿತ್ರ ವಿಷಯ ಇನ್ನು `"type": "image_url"` ಬಳಸುತ್ತಿದೆ | `"type": "input_image"` ಗೆ ಬದಲಾಯಿಸಿ |
| `Expected object, got string` on `image_url` | `image_url` ಇನ್ನೂ `{"url": "..."}` ಅಂತ вложенный объект ಆಗಿದೆ | ಸರಳ ಸ್ಟ್ರಿಂಗ್ ಆಗಿ ಫ್ಲ್ಯಾಟ್ ಮಾಡಿ: `"image_url": "https://..."` ಅಥವಾ `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | ಅಳತೆ ಕನಿಷ್ಟವು **16** ಆಗಿದೆ ಅಜೂರ್ OpenAI ನಲ್ಲಿ. ಪರೀಕ್ಷೆಗಳಿಗೆ 50+ ಮತ್ತು ಉತ್ಪಾದನಿಗೆ 1000+ ಬಳಸಿ. |
| `429 Too Many Requests` during streaming | ದರ ಮಿತಿ ಮೀರಿದೆ. ಸ್ಟ್ರೀಮಿಂಗ್ try/except ನಲ್ಲಿ ಆವರಿಸಿ, ಎ frenteಗೆ ದೋಷ JSON ನೀಡಿರಿ, ಬ್ಯಾಕ್ಓಫ್/ಮರುಪ್ರಯತ್ನವನ್ನು ಜಾರಿಗೊಳಿಸಿ. |
| `KeyError: 'innererror'` on content filter error | ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷ ದೇಹದ ರಚನೆ Responses APIಯಲ್ಲಿ ಬದಲಾಗಿದೆ | ಚಾಟ್ ಸಂಪೂರ್ಣೀಕರಣವು ಬಳಸಿದ `error.body["innererror"]["content_filter_result"]`; ರೆಸ್ಪಾನ್ಸಸ್ API `error.body["content_filters"][0]["content_filter_results"]` (ಬಹುವಚನ, ಒಂದು ಸರಣಿಯೊಳಗೆ) ಉಪಯೋಗಿಸುತ್ತದೆ. ಎಲ್ಲಾ `innererror` ಪ್ರವೇಶವನ್ನು ಮರು ಬರೆಯಿರಿ. |

---

## ಸ್ಥಳಾಂತರ ಅಪಾಯದ ತಾಳಿಕೆ

| ಲಕ್ಷಣ | ಸಾಧ್ಯ ತಪ್ಪು | ಪರಿಹಾರ |
|---------|---------------|-----|
| ಖಾಲಿ `output_text` / ಕಡಿತಗೊಂಡ ಪ್ರತಿಕ್ರಿಯೆ | ಆಲೋಚನೆ ಮಾದರಿಗಳಿಗೆ `max_output_tokens` ತುಂಬಾ ಕಡಿಮೆಯಾಗಿದೆ | `max_output_tokens=1000` ಅಥವಾ ಹೆಚ್ಚಿನದರಾಗಿ ಸೆಟ್ ಮಾಡಿ — ಆಲೋಚನೆ ಟೋಕನ್ಗಳು ಮಿತಿಗೆ ವಿರುದ್ಧವಾಗಿ ಲೆಕ್ಕ ಹಾಕುತ್ತವೆ |
| `400 invalid_type: text.format` | `text.format` dict ಬದಲಾಗಿ `response_format` ಸ್ಟ್ರಿಂಗ್ ಪಾಸಾಗಿದೆ | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` ಬಳಸಿ |
| `/openai/v1/responses` ನಲ್ಲಿ `404 Not Found` | ತಪ್ಪು `base_url` — `/openai/v1/` ಸರಣಿಯು ಕೊರತೆಯಾಗಿದೆ | `base_url=f"{endpoint}/openai/v1/"` (ಒಳಗು ಗುಣಚಿಹ್ನೆಯೊಂದಿಗೆ) ಖಚಿತಪಡಿಸಿ |
| `401 Unauthorized` `OpenAI()` ಗೆ ಬದಲಾಯಿಸಿದ ನಂತರ | `api_key` ಸೆಟ್ ಆಗಿಲ್ಲ ಅಥವಾ ಟೋಕನ್ պրೊವೈಡರ್ ಸರಿಯಾಗಿ ಪಾಸಾಗಿಲ್ಲ | EntraID ಗೆ: `api_key=token_provider` (ಕಾಲಬಲ್). API ಕಿಗೆ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| ಮಾದರಿ `deployment not found` ತೆರೆಯುತ್ತದೆ | `model` ಪರಾಮಿತಿ ನಿಮ್ಮ ಅಜೂರ್ ಡಿಪ್ಲಾಯ್ಮೆಂಟ್ ಹೆಸರಿನಿಂದ ಹೊಂದಿಕೆಯಾಗುತ್ತಿಲ್ಲ | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` ಬಳಸಿ — ಇದು ಡಿಪ್ಲಾಯ್ಮೆಂಟ್ ಹೆಸರು, ಮಾದರಿ ಹೆಸರು ಅಲ್ಲ |
| `json.loads(resp.output_text)` ನಲ್ಲಿ `JSONDecodeError` | ಸ್ಕೀಮಾ ಅನುಷ್ಠಾನಗೊಳ್ಳದಿರಬೇಕು ಅಥವಾ ಮಾದರಿ ಕಟ್ಟುನಿಟ್ಟಾದ JSON ಬೆಂಬಲಿಸುವುದಿಲ್ಲ | ಸ್ಕೀಮಾದಲ್ಲಿ `"strict": True"` ಇದೆ ಎಂದು ಖಚಿತಪಡಿಸಿ, ಮತ್ತು ಮಾದರಿ ಸಂರಚಿತ ಅವುಟುಟ್ ಬೆಂಬಲಿಸುತ್ತದೆ ಎಂದು ಪರಿಶೀಲಿಸಿ |
| ಸ್ಟ್ರೀಮಿಂಗ್ ಯಾವುದೇ `delta` ಘಟನೆಗಳನ್ನು ನೀಡುವುದಿಲ್ಲ | ತಪ್ಪು ಘಟನೆ ಪ್ರಕಾರವನ್ನು ಪರಿಶೀಲಿಸಲಾಗಿದೆ | `event.type == "response.output_text.delta"` ಮೇಲೆ ಫಿಲ್ಟರ್ ಮಾಡಿ, ಚಾಟ್‌ನ `chat.completion.chunk` ಅಲ್ಲ |
| ಸ್ಥಳಾಂತರದ ನಂತರ ಚಿತ್ರ ಇನ್ಪುಟ್‌ನಲ್ಲಿ `400` ದೋಷ | ಚಿತ್ರ ವಿಷಯ ಪ್ರಕಾರ ನವೀಕರಿಸಲಾಗಿಲ್ಲ | `"type": "image_url"` → `"type": "input_image"` ಗೆ ಬದಲಾಯಿಸಿ ಮತ್ತು `"image_url": {"url": "..."}` → `"image_url": "..."` (ಸರಳ ಸ್ಟ್ರಿಂಗ್) ಫ್ಲ್ಯಾಟ್ ಮಾಡಿ |
| ಉಪಕರಣ ಕರೆಗಳು ಅನಂತವಾಗಿವೆ | ನಂತರದ `input` ನಲ್ಲಿ ಉಪಕರಣ ಫಲಿತಾಂಶ ತಪ್ಪಿದೆ | ಉಪಕರಣವನ್ನು ಕಾರ್ಯನಿರ್ವಹಿಸಿದ ನಂತರ, ಮುಂದಿನ ವಿನಂತಿಯಲ್ಲಿ `input` ನಲ್ಲಿ `{"type": "function_call_output", "call_id": ..., "output": ...}` ಐಟಂ ಸೇರಿಸಿ |
| GPT-5 ಅಥವಾ o-ಸೀರಿ ಜತೆ `temperature` ದೋಷ | ಸ್ಪಷ್ಟ `temperature` ಮೌಲ್ಯ 1 ಬದಲಿಗೆಯಾಗಿದೆ | GPT-5 ಮತ್ತು o-ಸೀರಿ ಮಾದರಿಗಳ (o1, o3-mini, o3, o4-mini) ಗೆ `temperature` ಅಳಿಸಿರಿ ಅಥವಾ 1 ಗೆ ಹೊಂದಿಸಿ |
| o-ಸೀರಿ ಜತೆ `top_p` ದೋಷ | `top_p` ಬೆಂಬಲವಿಲ್ಲ | o-ಸೀರಿ ಮಾದರಿಗಳಿಗೆ ಗುರಿ ಹೊಂದಿಸುವಾಗ `top_p` ತೆಗೆದುಹಾಕಿ |
| `max_completion_tokens` ಗುರುತಿಸಲ್ಪಡುವುದಿಲ್ಲ | ಅಜೂರ್-ನಿರ್ದಿಷ್ಟ ಪರಾಮಿತಿ ಬಳಕೆ ಮಾಡುತ್ತಿದೆ | `max_completion_tokens` ಬದಲು `max_output_tokens` ಬಳಸಿ. o-ಸೀರಿ (ಆಲೋಚನೆ ಟೋಕನ್ಗಳು ಮಿತಿಗೆ ವಿರುದ್ಧವಾಗಿ ಲೆಕ್ಕ ನಿಯಂತ್ರಿಸುವುದು) ಗಾಗಿ 4096+ ಸೆಟ್ ಮಾಡಿ. |
| o-ಸೀರಿ ನಿಂದ ಖಾಲಿ/ಕಡಿತಗೊಂಡ ಅವುಟುಟ್ | `max_output_tokens` ತುಂಬಾ ಕಡಿಮೆ | o-ಸೀರಿ ಆಂತರಿಕವಾಗಿ ಆಲೋಚನೆ ಟೋಕನ್ಗಳನ್ನು ಬಳಸುತ್ತದೆ. `max_output_tokens=4096` ಅಥವಾ ಹೆಚ್ಚಿನಗೆ ಸೆಟ್ ಮಾಡಿರಿ — 500–1000 ಅಲ್ಲ. |
| `400 integer_below_min_value` `max_output_tokens` ಗಾಗಿ | 16 ಕಿಂತ ಕಡಿಮೆ ಮೌಲ್ಯ | ಅಜೂರ್ OpenAI `max_output_tokens >= 16` ಜಾರಿಗೊಳಿಸುತ್ತದೆ. ಧೂಮಪಾನ ಪರೀಕ್ಷೆಗಳಿಗೆ 50+, ಉತ್ಪಾದನಿಗೆ 1000+ ಬಳಸಿ. |
| ಸ್ಟ್ರೀಮ್‌ನ ಮಧ್ಯದಲ್ಲಿ `429 Too Many Requests` | ಅಜೂರ್ OpenAIರಿಂದ ದರ ಮಿತಿಗಟ್ಟಲಾಗಿದೆ | ಸ್ಟ್ರೀಮ್ ದೋಷ ನಿರ್ವಹಣೆ ಇಲ್ಲದೆ ಸಿಲ silently ಯಾಗಿ ಮುರಿಯಬಹುದು. ಯಾವಾಗಲೂ `async for event in await coroutine:` ಅನ್ನು try/except ನಲ್ಲಿ ಆವರಿಸಿ ಮತ್ತು `{"error": str(e)}` ಯನ್ನು ಫ್ರಂಟ್‌ಎಂಡ್‌ಗೆ ನೀಡಿರಿ. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | ತಪ್ಪು ಟೆನಂಟ್ ಅಥವಾ ಲಾಗಿನ್ ಆಗಿಲ್ಲ | ಸ್ಪಷ್ಟವಾಗಿ `tenant_id=os.getenv("AZURE_TENANT_ID")` ಪಾಸ್ ಮಾಡಿ. ಸ್ಥಳೀಯವಾಗಿ `azd auth login --tenant <tenant-id>` ನಡಿಸಿ. |
| GitHub ಮಾದರಿಗಳು (`models.github.ai`) ಬಳಸಿ `404 Not Found` | GitHub ಮಾದರಿಗಳು Responses API ಬೆಂಬಲಿಸುತ್ತಿಲ್ಲ | GitHub ಮಾದರಿ ಕೋಡ್ ಪಾಥ್ ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆಯಿರಿ. ಅಜೂರ್ OpenAI, OpenAI ಅಥವಾ ಹೊಂದಿಕೊಳ್ಳುವ ಸ್ಥಳೀಯ ಎಂಡ್ಪಾಯಿಂಟ್ (ಉದಾ: Ollama Responses ಬೆಂಬಲದೊಂದಿಗೆ) ಬಳಸಿ. |
| MAF `OpenAIChatCompletionClient` ಇನ್ನೂ ಚಾಟ್ ಸಂಪೂರ್ಣೀಕರಣ ಬಳಕೆಮಾಡುತ್ತಿದೆ | 1.0.0+ ನಲ್ಲಿ ಹಳೆಯ MAF ಕ್ಲಯಿಂಟ್ ಬಳಕೆ | MAF 1.0.0+ ನಲ್ಲಿ ಡಿಫಾಲ್ಟ್‌గా `OpenAIChatClient` Responses API ಬಳಕೆಮಾಡುತ್ತದೆ. `OpenAIChatCompletionClient` ಬದಲು `OpenAIChatClient` ಬಳಸಿ. 1.0.0 ಹಿಂದಿನದಾಗಿ ಇದ್ದರೆ `agent-framework-openai>=1.0.0`ಗೆ ನವೀಕರಿಸಿರಿ. |
| LangChain ಏಜೆಂಟ್ ಖಾಲಿ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುವುದು ಅಥವಾ ಉಪಕರಣ ಕರೆಗಳಲ್ಲಿ ವಿಫಲವಾಗಿದೆ | `ChatOpenAI` Responses API ಬಳಕೆಮಾಡುತ್ತಿಲ್ಲ | `ChatOpenAI(...)` ಗೆ `use_responses_api=True` ಸೇರಿಸಿ. ಪ್ರತಿಕ್ರಿಯೆ ಸಂದೇಶಗಳ `.content` ಅನ್ನು `.text` ಗೆ ಬದಲಾಯಿಸಿ. |
| ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷ ನಿರ್ವಹಕದಲ್ಲಿ `KeyError: 'innererror'` | Responses APIಯಲ್ಲಿ ದೋಷ ದೇಹದ ರಚನೆ ಬದಲಾಗಿದೆ | `error.body["innererror"]["content_filter_result"]["jailbreak"]` ಅನ್ನು ಮರುಬರೆಯಿರಿ → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` ಮಡಿಕೆ ತೆಗೆಯಲಾಗಿದೆ; ಲೇಖನ ಫಿಲ್ಟರ್ ವಿವರಗಳು ಈಗ ಟಾಪ್ ಲೆವಲ್ `content_filters` ಸರಣಿಯಲ್ಲಿ ಮತ್ತು ಪ್ರತಿಯೊಂದು ಒಳಗಿನ `content_filter_results` (ಬಹುವಚನ). |
| ಇಲ್ಲಿಗೆ `/openai/deployments/.../chat/completions` ಗೆ ರಾ HTTP ಕರೆ 404 ಸಶಃಮಾದ್ಯತೆ | ಹಳೆಯ ಚಾಟ್ ಸಂಪೂರ್ಣೀಕರಣ REST ಎಂಡ್ಪಾಯಿಂಟ್ | URL ಅನ್ನು `/openai/v1/responses` ಗೆ ಮರುಬರೆಯಿರಿ. ವಿನಂತಿ ದೇಹಮಾಡಾಣಿಕೆ: `messages` → `input`, `max_output_tokens` + `store: false` ಸೇರಿಸಿ, `api-version` ಕ್ವೆರಿ ಪ್ಯಾರಾಮ್ ತೆಗೆದುಹಾಕಿ. ಪ್ರತಿಕ್ರಿಯೆ ವಿಶ್ಲೇಷಣೆ: `choices[0].message.content` → `output[0].content[0].text` (ಗಮನಿಸಿ: `output_text` SDK ಅನುಕೂಲತೆಯ ಗುಣಲಕ್ಷಣ, ರಾ REST JSON ನಲ್ಲಿ ಇಲ್ಲ). |

---

## ಗಮನಿಸಬೇಕಾದವುಗಳು

1. ನೀವು ಹಿಂದೆ ಚಾಟ್ ಸಂಪೂರ್ಣೀಕರಣಗಳನ್ನು ಸಂವಾದ ಸ್ಥಿತಿಗಾಗಿ ಬಳಸಿದ್ದರೆ, ಪ್ರತಿಕ್ರಿಯೆಗೊಳಿಸುವ ಮೂಲಕ ನಿಮ್ಮದೇ ಸ್ಥಿತಿಯನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ನಿರ್ವಹಿಸಿ.
2. ಹಳೆಯ `max_tokens` ಬದಲು `max_output_tokens` ಆದ್ಯತೆಯಿಂದ ಬಳಸಿ.
3. `gpt-5` ಗೆ ಸ್ಥಳಾಂತರಿಸುವಾಗ, `temperature` ಅನ್ನು ಸೂಚಿಸಬೇಡಿ ಅಥವಾ 1ಕ್ಕೆ ಸೆಟ್ ಮಾಡಿರಿ.
4. ಚಾಟ್ `content[].type: "text"` ಅನ್ನು ಬಳಕೆದಾರ/ಸಿಸ್ಟಂ ಇನ್‌ಪುಟ್‌ಗಳಿಗೆ Responses `content[].type: "input_text"` ಗೆ ಬದಲಾಯಿಸಿ.
5. `text.format` ಗೆ ಸರಿಯಾದ dict ಒದಗಿಸಿ (ಉದಾ: `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ಸರಳ ಸ್ಟ್ರಿಂಗ್ ಅಲ್ಲ.
6. Responses ನಲ್ಲಿ `seed` ಪರಾಮಿತಿ ಬೆಂಬಲಿಸಲ್ಪಟ್ಟಿಲ್ಲ; ವಿನಂತಿಗಳಿಂದ ಇದನ್ನು ತೆಗೆದುಹಾಕಿ.
7. **ಆಲೋಚನೆ**: ಮೂಲ ಕೋಡ್ ಈಗಾಗಲೇ ಇದನ್ನು ಬಳಸಿದ್ದರೆ ಮಾತ್ರ `reasoning` ಸೇರಿಸಿ. ಆಗೇ ಇಲ್ಲದ API ಕರೆಗಳಿಗೆ `reasoning` ಸೇರಿಸಬೇಡಿ — ಬಹುತೇಕ ಮಾದರಿಗಳು (ಉದಾ: gpt-4o-mini) ಈ ಪರಾಮಿತಿಯನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ.
8. **`max_output_tokens` ಗಾತ್ರಾಸ್ಪದ**: ಆಲೋಚನೆ ಮಾದರಿಗಳಿಗೆ (GPT-5-mini, GPT-5, o-ಸೀರಿ) `max_output_tokens=4096` ಅಥವಾ ಹೆಚ್ಚಿನದನ್ನು ಬಳಸಿ — 50–1000 ಅಲ್ಲ. ಮಾದರಿ ದೃಶ್ಯಾವತೃತಿಯ ಮೊದಲಿಗೆ ಆಲೋಚನೆ ಟೋಕನ್ಗಳನ್ನು ಆಂತರಿಕವಾಗಿ ಬಳಸುತ್ತದೆ; ಬೆಳಕು ಕಡಿಮೆ ಇದ್ದರೆ ಕಡಿತಗೊಂಡ ಅಥವಾ ಖಾಲಿ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಬರುತ್ತವೆ.
9. **O-ಸೀರಿ `max_completion_tokens`**: ಮೂಲ ಕೋಡ್ `max_completion_tokens` (ಅಜೂರ್-ನಿರ್ದಿಷ್ಟ o-ಸೀರಿ ಗಾಗಿ) ಬಳಸಿದರೆ, ಅದನ್ನು `max_output_tokens` ಗೆ ಬದಲಾಯಿಸಿ. Responses API `max_completion_tokens` ಸ್ವೀಕರಿಸುವುದಿಲ್ಲ.
10. **O-ಸೀರಿ `reasoning_effort`**: ಮೂಲ ಕೋಡ್ `reasoning_effort` (ಕೆಳಗೆ/ಮಧ್ಯಮ/ಮೇಲ್ಮಟ್ಟ) ಬಳಸಿದರೆ, Responses API ಕರೆಗಳಲ್ಲಿ ಅದನ್ನು `reasoning={"effort": "<value>"}` ಗೆ ಸ್ಥಳಾಂತರಿಸಿ.
11. **O-ಸೀರಿ ಸ್ಟ್ರೀಮಿಂಗ್ ವಿಳಂಬ**: o-ಸೀರಿ ಮಾದರಿಗಳು ಹೊರತುಪಡಿಸುವ ಮೊದಲು ಆಂತರಿಕ ಆಲೋಚನೆ ನಡೆಸುತ್ತವೆ. ಸ್ಟ್ರೀಮಿಂಗ್ ವೇಳೆ ಮೊದಲು `response.output_text.delta` ಘಟನೆಗೆ ಹೆಚ್ಚು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳಬಹುದು. ಇದು ಸಾಮಾನ್ಯ — ಮಾದರಿ ಅಲೆಯುತ್ತಿಲ್ಲ, ಆಲೋಚಿಸುತ್ತಿದೆ.
9. **`_azure_ad_token_provider` ಸಿಗುವುದಿಲ್ಲ**: `AsyncOpenAI` / `OpenAI` ನಲ್ಲಿ `_azure_ad_token_provider` ಗುಣಲಕ್ಷಣವಿಲ್ಲ. ಪರೀಕ್ಷೆಗಳು ಅಥವಾ ಕೋಡ್ ಇದನ್ನು ಪ್ರವೇಶಿಸಿದರೆ `AttributeError` ತರುತ್ತದೆ. ಟೋಕನ್ ಪ್ರೊವೈಡರ್ `api_key` ಆಗಿ ಪಾಸ್ ಆಗಿದ್ದು ಕ್ಲಯಿಂಟ್ ವಸ್ತುನಲ್ಲಿ ಪರಿಶೀಲಿಸಲಾಗುವುದಿಲ್ಲ.
10. **ನಿರೀಕ್ಷೆ / ಗೋಲ್ಡನ್ ಫೈಲುಗಳು**: ಪರೀಕ್ಷಾ ತುದಿ ನಿರೀಕ್ಷೆ ಪರೀಕ್ಷೆ ಬಳಕೆ ಮಾಡಿದ್ದರೆ, **ಎಲ್ಲಾ** ನಿರೀಕ್ಷೆ ಫೈಲುಗಳು ಚಾಟ್ ಸಂಪೂರ್ಣೀಕರಣಗಳ ಸ್ಟ್ರೀಮಿಂಗ್ ಆಕಾರವನ್ನು (`choices[0]`, `content_filter_results`, `function_call`, ಇತ್ಯಾದಿ) Responses ಆಕಾರಕ್ಕೆ ನವೀಕರಿಸಬೇಕು. ಇದು ಸುಲಭವಾಗಿ ಗಮನಹರಿಸಲಾಗದು ಮತ್ತು ನಿರೀಕ್ಷೆ ದೃಢೀಕರಣ ದೋಷಗಳಾಗಿಸುತ್ತದೆ.
11. **ಮೋಕ್ ಮಂಕಿಪ್ಯಾಚ್ ಮಾರ್ಗ**: ಮಂಕಿಪ್ಯಾಚ್ ಗುರಿ `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ಅಥವಾ `Responses.create` ಸಿಂಕ್ ಗಾಗಿ) ಗೆ ಬದಲಾಗಿದೆ. ಹಳೆಯ ಮಾರ್ಗವನ್ನು ಬಳಕೆ ಮಾಡುವುದರಿಂದ ಮಂಕಿ ಸಂವಹನ ಆಗುವುದಿಲ್ಲ, ಪರೀಕ್ಷೆಗಳು ನಿಜವಾದ API ಗೆ ಹೊಡೆದುಕೊಳ್ಳುತ್ತವೆ ಅಥವಾ ವಿಫಲವಾಗುತ್ತವೆ.
12. **`input` ಅಲ್ಲ `messages`**: ಮೋಕ್ ಕಾರ್ಯಗಳು `kwargs.get("input")` ಅನ್ನು ಓದಬೇಕು, `kwargs.get("messages")` ಅಲ್ಲ. Responses API ಸಂವಾದ ಇತಿಹಾಸಕ್ಕೆ `input` ಅನ್ನು ಬಳಕೆಮಾಡುತ್ತದೆ.
13. **ಪರಿಸರ 변수 ಹೆಸರು**: ಅಜೂರ್ ಐಡೆಂಟಿಟಿ SDK `ManagedIdentityCredential(client_id=...)` ಗೆ `AZURE_CLIENT_ID` (`AZURE_OPENAI_CLIENT_ID` ಅಲ್ಲ) ಬಳಸುತ್ತದೆ. ಪರೀಕ್ಷೆಗಳು, `.env` ಫೈಲುಗಳು, ಅಪ್ಲಿಕೇಶನ್ ಸೆಟ್ಟಿಂಗ್ಗಳು, ಮತ್ತು Bicep/ಅಧಾರದಲ್ಲಿ ಮರುನಾಮಕರಣ ಮಾಡಿ.
14. **`max_output_tokens` ಕನಿಷ್ಠ ಮೌಲ್ಯ 16**: ಅಜೂರ್ OpenAI 16 ಕಿಂತ ಕಡಿಮೆ ಮೌಲ್ಯವನ್ನು `400 integer_below_min_value` ಮೂಲಕ ತಿರಸ್ಕರಿಸುತ್ತದೆ. ಧೂಮಪಾನ ಪರೀಕ್ಷೆಗಳಿಗೆ 50, ಉತ್ಪಾದನಿಗೆ 1000+ ಬಳಸಿ. ಹಳೆಯ `max_tokens` ಗೆ ಇಂತಹ ಕನಿಷ್ಠ ಮೌಲ್ಯವಿರಲಿಲ್ಲ.
15. **`AzureDeveloperCliCredential` ಗಾಗಿ `tenant_id`**: ಅಜೂರ್ OpenAI ಸಂಪನ್ಮೂಲವು ವಿಭಿನ್ನ ಟೆನಂಟ್‌ನಲ್ಲಿ ಇದ್ದಾಗ ನೀವು ಸ್ಪಷ್ಟವಾಗಿ `tenant_id` ಪಾಸ್ ಮಾಡಬೇಕು — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. ಅದನ್ನು ಹೊರತುಪಡಿಸಿದರೆ, ಕ್ರೆಡೆನ್ಶಿಯಲ್ ತಪ್ಪು ಟೆನಂಟ್ ಬಳಸಿ ಮೌನವಾಗಿ `401` ಹೊಂದುತ್ತದೆ.
16. **ಸ್ಟ್ರೀಮಿಂಗ್‌ನಲ್ಲಿ ದರ ಮಿತಿಗಳು ವಿಭಿನ್ನವಾಗಿ ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತವೆ**: ಚಾಟ್ ಸಂಪೂರ್ಣೀಕರಣಗಳೊಂದಿಗೆ 429 ಸಾಮಾನ್ಯವಾಗಿ ಸ್ಟ್ರೀಮ್ ಪ್ರಾರಂಭವಾಗಲು ತಡೆಯುತ್ತಿತ್ತು. Responses API ಸ್ಟ್ರೀಮಿಂಗ್‌ನೊಂದಿಗೆ, 429 **ಮಧ್ಯ-ಸ್ಟ್ರೀಮ್** ನಲ್ಲಿ ಸಂಭವಿಸಬಹುದು — ಅಸಿಂಕ್ ಇಟರೇಟರ್ uitzonderling ಎರುತ್ತದೆ. ಯಾವಾಗಲೂ ಸ್ಟ್ರೀಮಿಂಗ್ ಲಾಜಿಕ್ನ್ನು try/except ನಲ್ಲಿ ಆವರಿಸಿ ಮತ್ತು ಮುಂಭಾಗಗೆ ದೋಷ JSON ಸಾಲು ನೀಡುವುದರಿಂದ ಅದನ್ನು ಸೌಲಭ್ಯಕರವಾಗಿ ನಿರ್ವಹಿಸಲು ಬಯಸಿ.

17. **ವೆಬ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗಾಗಿ ಸ್ಟ್ರೀಮಿಂಗ್ ದೋಷ ನಿರ್ವಹಣೆ ಅನಿವಾರ್ಯವಾಗಿದೆ**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` ಪ್ಯಾಟರ್ನ್ ಅತ್ಯಂತ ಮುಖ್ಯವಾಗಿದೆ. ಇದಿಲ್ಲದೆ, SSE/JSONL ಸ್ಟ್ರೀಮ್ ಯಾವುದೇ ಸರ್ವರ್-ಬದಿಯ ದೋಷದಲ್ಲಿ ಮೌನವಾಗಿ ನಿಲ್ಲುತ್ತದೆ ಮತ್ತು ಮುಂಭಾಗ ಸ್ಥಗಿತಗೊಳ್ಳುತ್ತದೆ.
18. **ಟೂಲ್ ವ್ಯಾಖ್ಯಾನಗಳು ಫ್ಲಾಟ್ ಫಾರ್ಮ್ಯಾಟ್ ಬಳಸಬೇಕು**: Responses API ಗೆ `{"type": "function", "name": ..., "parameters": ...}` ನಿರೀಕ್ಷಿಸಲಾಗಿದೆ — ಚಾಟ್ ಕಾಂಪ್ಲೀಷನ್ ನಿಷ್ಟಿತ `{"type": "function", "function": {"name": ..., "parameters": ...}}` ಅಲ್ಲ. ಇದು ಫಂಕ್ಷನ್-ಕಾಲಿಂಗ್ ಕೋಡ್‌ನ ಸಾಮಾನ್ಯ ಮೌಲ್ಯಸ್ಥಾನದ ದೋಷವಾಗಿದೆ.
19. **`pydantic_function_tool()` ಅನನ್ಯೋಗ್ಯವಾಗಿದೆ**: `openai.pydantic_function_tool()` ಸಹಾಯಕ ಇನ್ನೂ ಹಳೆಯ ನಿಷ್ಟಿತ ಫಾರ್ಮ್ಯಾಟ್ ಸೃಷ್ಟಿಸುತ್ತದೆ. ಇದನ್ನು `responses.create()` ಜತೆ ಉಪಯೋಗಿಸಬೇಡಿ. ಟೂಲ್ ಸ್ಕೀಮಾಗಳನ್ನು ಕೈಯಿಂದ ವ್ಯಾಖ್ಯಾನಿಸಿ ಅಥವಾ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಫ್ಲ್ಯಾಟ್ ಮಾಡಿ.
20. **ಟೂಲ್ ಫಲಿತಾಂಶಗಳು `function_call_output` ಬಳಸುತ್ತವೆ, `role: tool` ಅಲ್ಲ**: ಟೂಲ್ ಕಾರ್ಯಗತಗೊಳಿಸಿದ ನಂತರ, `{"type": "function_call_output", "call_id": ..., "output": ...}` ಅನ್ನು ಸೇರಿಸಿ — `{"role": "tool", "tool_call_id": ..., "content": ...}` ಅಲ್ಲ. ಸಹಾಯಕನ ಟೂಲ್ ವಿನಂತಿಗೆ, `messages.extend(response.output)` ಉಪಯೋಗಿಸಿ — ಕೈಯಿಂದ `{"role": "assistant", "tool_calls": [...]}` ಡಿಕ್ಟ್ ಬೇಡ.
21. **`strict: true` ಗೆ `required` + `additionalProperties: false` ಅಗತ್ಯ**: ಟೂಲ್ ಮೇಲೆ `strict: true` ಬಳಸುವಾಗ, ಪ್ರತಿ ಗುಣ ಲಕ್ಷಣವನ್ನು `required` ಅರೆನಲ್ಲಿ ಮಾಹಿತಿ ನೀಡಬೇಕು ಮತ್ತು `additionalProperties` ನ್ನು `false` ಆಗಿರಬೇಕು. ಯಾವುದಾದರೂ ಕೊರತೆ 400 ದೋಷ ಉಂಟುಮಾಡುತ್ತದೆ.
22. **ಫಂಕ್ಷನ್ ಕಾಲ್ ಐಡಿಗಳು ವಿಶೇಷ ಪೂರ್ವಪ್ರತ್ಯಯಗಳನ್ನು ಹೊಂದಿರಬೇಕು**: `input` ನಲ್ಲಿ ಫ್ಯೂ-ಶಾಟ್ `function_call` ಐಟಂಗಳನ್ನು ಒದಗಿಸುವಾಗ, `id` ಕ್ಷೇತ್ರ `fc_` ನಲ್ಲಿ ಪ್ರಾರಂಭವಾಗಬೇಕು ಮತ್ತು `call_id` ಕ್ಷೇತ್ರ `call_` ನಲ್ಲಿ ಪ್ರಾರಂಭವಾಗಬೇಕು (ಉದಾಹರಣೆಗೆ, `"id": "fc_example1", "call_id": "call_example1"`). ಹಳೆಯ ಚಾಟ್ ಕಾಂಪ್ಲೀಷನ್ `call_` ಪೂರ್ವಪ್ರತ್ಯಯವನ್ನು `id` ಗೆ ಬಳಸುವುದು ನಿರಾಕರಿಸಲಾಗುತ್ತದೆ.
23. **GitHub ಮಾದರಿಗಳು Responses API ಅನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ**: ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ GitHub Models ಕೋಡ್ ಮಾರ್ಗವಿದ್ದರೆ (`base_url` `models.github.ai` ಅಥವಾ `models.inference.ai.azure.com` ತೋರಿಸುತ್ತಿದ್ದರೆ), ಅದನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದು ಹಾಕಿ. ಸ್ಥಳಾಂತರ ಮಾರ್ಗ ಇಲ್ಲ — Azure OpenAI, OpenAI ಅಥವಾ ಹೊಂದಾಣಿಕೆಯ ಸ್ಥಳೀಯ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗೆ ಬದಲಾಯಿಸಿ.
24. **ಮಾಹಿತಿ ಫಿಲ್ಟರ್ ದೋಷ ದೇಹದ ರಚನೆ ಬದಲಾಗಿದೆ**: ಚಾಟ್ ಕಾಂಪ್ಲೀಷನ್ ದೋಷಗಳು `error.body["innererror"]["content_filter_result"]` (ಏಕವಚನ) ಬಳಸಿದ್ದು, Responses API ದೋಷಗಳು `error.body["content_filters"][0]["content_filter_results"]` (ಬಹುವಚನ, ಪಟ್ಟಿಯಲ್ಲಿ) ಬಳಸುತ್ತವೆ. `innererror` ಕೀ ಈಗ ಇಲ್ಲ. ನೇರವಾಗಿ `innererror` Access ಮಾಡುವುದು ರನ್‌ಟೈಮ್‌ನಲ್ಲಿ `KeyError` ಉಂಟುಮಾಡುತ್ತದೆ — ಇದು ಸ್ಥಳಾಂತರ ವೇಳೆ ಕಾಣಿಸಿಕೊಳ್ಳುವುದಿಲ್ಲ, ಇವು ಮಾತ್ರ ಫಿಲ್ಟರ್ ತೊಡಗಿದಾಗ ಗೋಚರಿಸುತ್ತದೆ. ಮರೆಯದೆ ಸ್ಥಳಾಂತರ ವೇಳೆ `innererror` ಗೆ grep ಹಾಕಿ.
25. **ಕಚ್ಛಾ HTTP ಕರೆಗಳಿಗೆ URL + ದೇಹ ಪರಿಷ್ಕರಣೆ ಅಗತ್ಯ**: ಸ್ವತಃ Azure OpenAI REST ಕರೆಗಳು (`requests`, `httpx`, `aiohttp` ಮೂಲಕ) `/openai/deployments/{name}/chat/completions?api-version=...` ಬಳಕೆ ಮಾಡುವ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು `/openai/v1/responses` ಕ್ಕೆ ಬದಲಾಗಬೇಕು. ವಿನಂತಿ ದೇಹದಲ್ಲಿ `messages` ಬದಲಿಗೆ `input` ಇದೆ, `max_output_tokens` ಮತ್ತು `store` ಅಗತ್ಯವಿದೆ, ಮತ್ತು `api-version` ಕ್ವೇರಿ ಪ್ಯಾರಾಮ್ ಕಡಿತಗೊಳಿಸಲಾಗಿದೆ. ಪ್ರತಿಕ್ರಿಯೆ ದೇಹ ಪಠ್ಯವು `output[0].content[0].text` ನಲ್ಲಿ ಇದೆ — **`output_text` ಅಲ್ಲ**, ಇದು SDK ಅನುಕೂಲತೆ ಗೊಳಿಸಿರುವ ಗುಣಲಕ್ಷಣ, ಆದರೆ ಕಚ್ಛಾ REST JSON ನಲ್ಲಿ ಸಿಗುವುದಿಲ್ಲ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->