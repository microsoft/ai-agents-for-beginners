# ಸಮಸ್ಯೆ ನಿವಾರಣೆ, ಅಪಾಯದ పట్టಿಕೆ ಮತ್ತು ಗೊತ್ತಿರಬೇಕಾದ ಅಂಶಗಳು

## 400 ದೋಷಗಳ ಪರಿಹಾರ

| ದೋಷ | ಪರಿಹಾರ |
|-------|-----|
| `missing_required_parameter: tools[0].name` | ಸಾಧನ ವ್ಯಾಖ್ಯಾನವು ಹಳೆಯ ಚಾಟ್ ಪೂರ್ಣೀಕರಣಗಳ ನೆಸ್ಟೆಡ್ ಫಾರ್ಮ್ಯಾಟ್ ಬಳಸುತ್ತದೆ | `{"type": "function", "function": {"name": ...}}` ನಿಂದ `{"type": "function", "name": ..., "parameters": ...}` ಗೆ ಫ್ಲಾಟನ್ ಮಾಡಿ — name, description, parameters ಗಳನ್ನುトップ ಮಟ್ಟದಲ್ಲಿ ಇಡಿ |
| `unknown_parameter: input[N].tool_calls` | ಬಹು-ತಿರುವು ಸಾಧನ ಫಲಿತಾಂಶಗಳು ಹಳೆಯ ಚಾಟ್ ಪೂರ್ಣೀಕರಣ ಫಾರ್ಮ್ಯಾಟ್ ಬಳಸುತ್ತವೆ | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ಅನ್ನು `response.output` ಐಟಂಗಳೊಂದಿಗೆ + `{"type": "function_call_output", "call_id": ..., "output": ...}` ಗೆ ಬದಲಿಸಿ |
| `invalid_function_parameters: 'required' is required` | `strict: true` ಸಾಧನದಲ್ಲಿ `required` ಅರೆ ಈಡಿಲ್ಲ | `strict: true` ಇದ್ದಾಗ ಎಲ್ಲಾ ಗುಣಲಕ್ಷಣಗಳು `required`ನಲ್ಲಿ ಪಟ್ಟಿಯಾಗಿ ಇರಬೇಕು ಮತ್ತು `additionalProperties: false` ಸೆಟ್ ಮಾಡಬೇಕು |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` ಸಾಧನದಲ್ಲಿ `additionalProperties: false` ಇಲ್ಲ | ಪರಿಮాణಗಳ ವಸ್ತುವಿಗೆ `"additionalProperties": false` ಸೇರಿಸಿ |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ಫ್ಯೂ-ಶಾಟ್ function_call ID ಯಲ್ಲಿ ತಪ್ಪು ಪ್ರೀಫಿಕ್ಸ್ ಇದೆ | ಫಂಕ್ಷನ್ ಕಾಲ್ ಐಡಿಗಳು `fc_` (ಉದಾ: `fc_example1`) ನಿಂದ ಆರಂಭಿಸಬೇಕು, `call_` ಅಲ್ಲ |
| `missing_required_parameter: text.format.name` | ಫಾರ್ಮ್ಯಾಟ್ ಡಿಕ್ಷನರಿಯಲ್ಲಿ `"name"` ಕೀ ಸೇರಿಸಿ (ಉದಾ: `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` ಅನ್ನು `type`, `name`, `strict`, `schema` ಕೀಗಳನ್ನೊಳಗೊಂಡ ಡಿಕ್ಷನರಿ ಆಗಿರಿಸಬೇಕು — ಸರಳ ಸ್ಟ್ರಿಂಗ್ ಅಲ್ಲ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ |
| `invalid input content type` | ಚಾಟ್ `text` ಬದಲು `input_text`/`output_text` ವಿಷಯ ಪ್ರಕಾರಗಳನ್ನು ಬಳಸಿ |
| `invalid input content type` (ಚಿತ್ರ) | ಚಿತ್ರ ವಿಷಯದಲ್ಲಿ ಇನ್ನೂ `"type": "image_url"` ಬಳಸಲಾಗಿದೆ | `"type": "input_image"` ಗೆ ಬದಲಿಸಿ |
| `Expected object, got string` on `image_url` | `image_url` ಇನ್ನೂ ನೆಸ್ಟೆಡ್ ವಸ್ತು `{"url": "..."}` ಆಗಿದೆ | ಸರಳ ಸ್ಟ್ರಿಂಗ್ ಆಗಿ ಫ್ಲಾಟನ್ ಮಾಡಿ: `"image_url": "https://..."` ಅಥವಾ `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI ನಲ್ಲಿ ಕನಿಷ್ಠ 16 ಇರುತ್ತದೆ. ಪರೀಕ್ಷೆಗಳಿಗೆ 50+ ಮತ್ತು ಉತ್ಪಾದನೆಗೆ 1000+ ಬಳಸಿ. |
| `429 Too Many Requests` ಸ್ಟ್ರೀಮಿಂಗ್ ವೇಳೆ | ದರ ಮಿತಿ ಸಾಧನೆಯಾಗಿದೆ. ಸ್ಟ್ರೀಮಿಂಗ್ ಅನ್ನು `try/except` ನಲ್ಲಿ ಸುತ್ತಿಸಿ, ದೋಷದ JSON ಅನ್ನು ಫ್ರಂಟೆಂಡ್‌ಗೆ ನೀಡಿರಿ, ಬ್ಯಾಕ್ಆಫ್/ಪುನರಾವೃತ್ತಿ ಅನುಷ್ಠಾನಗೊಳ್ಳಬೇಕು. |
| `KeyError: 'innererror'` ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷದಲ್ಲಿ | Responses API ನಲ್ಲಿ ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷದ ದೇಹದ ರಚನೆ ಬದಲಾಗಿದೆ | ಚಾಟ್ ಪೂರ್ಣೀಕರಣ ಕ್ಲಾಸ್‌ನಲ್ಲಿ ಬಳಸುತ್ತಿದ್ದ `error.body["innererror"]["content_filter_result"]` ಬದಲಾಗಿ Responses API ನಲ್ಲಿ `error.body["content_filters"][0]["content_filter_results"]` (ಬಹುವಚನ, ಅರೆ ಪಟ್ಟಿಯೊಳಗೆ) ಬಳಸಿ. ಎಲ್ಲಾ `innererror` ಪ್ರವೇಶಗಳನ್ನು ಮರುಬರೆ ಹೇಳಿ. |

---

## ವರ್ಗಾವಣೆ ಅಪಾಯದ ಪಟ್ಟಿಕೆ

| ಲಕ್ಷಣ | ಸಂಭವನೀಯ ತಪ್ಪು | ಪರಿಹಾರ |
|---------|---------------|-----|
| ಖಾಲಿ `output_text` / ಕಡಿತ ಉತ್ತರ | ಯುಕ್ತಿಮಾಡುವ ಮಾದರಿಗಳಿಗಾಗಿ `max_output_tokens` ಹೆಚ್ಚು ಕಡಿಮೆ | `max_output_tokens=1000` ಅಥವಾ ಹೆಚ್ಚಿನ ಮೌಲ್ಯವನ್ನು ನಿಗದಿ ಮಾಡಿ — ಯುಕ್ತಿ ಟೋಕನ್ ಗಳು ಮಿತಿ ವಿರುದ್ಧವಾಗಿ ಲೆಕ್ಕಿಸಬೇಕಾಗುತ್ತದೆ |
| `400 invalid_type: text.format` | `text.format` ಡಿಕ್ಷನರಿಯ ಬದಲು `response_format` ಸ್ಟ್ರಿಂಗ್ ಬಳಿ ಬಂದಿದೆ | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` ಬಳಸಿ |
| `/openai/v1/responses` ನಲ್ಲಿ `404 Not Found` | ತಪ್ಪು `base_url` — `/openai/v1/` ಸಫಿಕ್ಸ್ ಇಲ್ಲ | `base_url=f"{endpoint}/openai/v1/"` (ದೋಣಿ ಅಕ್ಷರದೊಂದಿಗೆ) ಇರಬೇಕೆಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ |
| `401 Unauthorized` `OpenAI()` ಗೆ ಬದಲಿಸಿದ ನಂತರ | `api_key` ಸೆಟ್ ಆಗಿಲ್ಲ ಅಥವಾ ಟೋಕನ್ ಪ್ರೊವೈಡರ್ ಸರಿಯಾಗಿ ನೀಡಿಲ್ಲ | EntraIDಗಾಗಿ: `api_key=token_provider` (ಕಾಲೇಬಲ್ ಆಗಿರುವ) ಆಗಿರಬೇಕು. API ಕೀಗಾಗಿ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| ಮಾದರಿ `deployment not found` ತಿರುಗಿಸುತ್ತಿದೆ | `model` ಪರಿಮಾಣವು ನಿಮ್ಮ Azure ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಹೆಸರಿನ ಜೊತೆಗೆ ಹೊಂದಿಕೆಯಾಗುವುದಿಲ್ಲ | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` ಬಳಸಿರಿ — ಇದು ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಹೆಸರು, ಮಾದರಿ ಹೆಸರು ಅಲ್ಲ |
| `json.loads(resp.output_text)` ನಲ್ಲಿ `JSONDecodeError` | ಸ್ಕೀಮಾ ಅನುಷ್ಠಾನಗೊಳ್ಳಲಿಲ್ಲ ಅಥವಾ ಮಾದರಿ ಕಠಿಣ JSON ಬೆಂಬಲಿಸುವುದಿಲ್ಲ | ಸ್ಕೀಮಾದಲ್ಲಿ `"strict": True` ಇದೆ ಎಂದು ಖಚಿತಮಾಡಿ ಮತ್ತು ಮಾದರಿ ರಚನಾತ್ಮಕ ಔಟ್‌ಪುಟ್ ಬೆಂಬಲಿಸುವುದನ್ನು ಪರಿಶೀಲಿಸಿ |
| ಸ್ಟ್ರೀಮಿಂಗ್ `delta` ಕಾರ್ಯಕ್ರಮಗಳನ್ನು ನೀಡುವುದಿಲ್ಲ | ತಪ್ಪಾದ ಕಾರ್ಯಕ್ರಮ ವಿಧವನ್ನು ಪರಿಶೀಲಿಸಲಾಗುತ್ತಿದೆ | ಚಾಟ್ `chat.completion.chunk` ಅಲ್ಲ, `event.type == "response.output_text.delta"` ತFiltering ಮಾಡಿ |
| ವರ್ಗಾವಣೆಯ ನಂತರ ಚಿತ್ರ ಇನ್ಪುಟ್‌ನಲ್ಲಿ `400` ದೋಷ | ಚಿತ್ರ ವಿಷಯ ಪ್ರಕಾರ ನವೀಕರಿಸಲಾಗಿಲ್ಲ | `"type": "image_url"` ಅನ್ನು `"type": "input_image"` ಗೆ ಬದಲಿಸಿ ಮತ್ತು `"image_url": {"url": "..."}` ಅನ್ನು `"image_url": "..."` (ಸರಳ ಸ್ಟ್ರಿಂಗ್) ಗೆ ಫ್ಲಾಟ್ ಮಾಡಿ |
| ಸಾಧನ ಕರೆಗಳ ಲೂಪ್ ಅನಂತವಾಗಿದೆ | ಅನುಸರಿಸುವ `input` ನಲ್ಲಿ ಸಾಧನ ಫಲಿತಾಂಶ ಇಲ್ಲ | ಸಾಧನವನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿದ ನಂತರ, ಮುಂದಿನ ವಿನಂತಿಯಲ್ಲಿನ `input` ಗೆ `{"type": "function_call_output", "call_id": ..., "output": ...}` ಐಟಂ ಸೇರಿಸಿ |
| GPT-5 ಅಥವಾ o-ಸೇತ್ರ ಮಾದರಿಗಳಲ್ಲಿ `temperature` ದೋಷ | 1 ಹೊರಗಿನ ಸ್ಪಷ್ಟ `temperature` ಮೌಲ್ಯ | GPT-5 ಮತ್ತು o-ಸೇತ್ರ ಮಾದರಿಗಳ (o1, o3-mini, o3, o4-mini) ಪ್ರಕಾರ `temperature` ಅನ್ನು ತೆಗೆದುಹಾಕಿ ಅಥವಾ 1 ಗೆ ಸೆಟ್ ಮಾಡಿ |
| o-ಸೇತ್ರದಲ್ಲಿ `top_p` ದೋಷ | `top_p` ಬೆಂಬಲಿಸಲ್ಪಡುವುದಿಲ್ಲ | o-ಸೇತ್ರ ಮಾದರಿಗಳನ್ನು ಗುರಿ ಮಾಡಿದಾಗ `top_p` ತೆಗೆದುಹಾಕಿ |
| `max_completion_tokens` ಗುರುತಿಸಲ್ಪಡುತ್ತಿಲ್ಲ | Azure-ನಿರ್ದಿಷ್ಟ ಪರಿಮಾಣ ಬಳಕೆ | `max_completion_tokens` ಬದಲು `max_output_tokens` ಬಳಸಿ. o-ಸೇತ್ರಕ್ಕಾಗಿ 4096+ ನಿಗದಿಮಾಡಿ (ಯುಕ್ತಿ ಟೋಕನ್ ಗಳು ಮಿತಿ ವಿರುದ್ಧವಾಗಿ ಲೆಕ್ಕವಾಗುತ್ತವೆ). |
| o-ಸೇತ್ರದಿಂದ ಖಾಲಿ/ಕಡಿತ ಔಟ್‌ಪುಟ್ | `max_output_tokens` ತುಂಬಾ ಕಡಿತವಾಗಿದೆ | o-ಸೇತ್ರ ಆಂತರಿಕವಾಗಿ ಯುಕ್ತಿ ಟೋಕನ್ ಗಳನ್ನು ಬಳಕೆ ಮಾಡುತ್ತದೆ. `max_output_tokens=4096` ಅಥವಾ ಹೆಚ್ಚಿನ ಮೌಲ್ಯ ನಿಗದಿಮಾಡಿ — 500–1000 ಅಲ್ಲ. |
| `max_output_tokens`ಗಾಗಿ `400 integer_below_min_value` | ಮೌಲ್ಯ 16 ಕಿಂತ ಕೀಳಿದೆ | Azure OpenAI ಕನಿಷ್ಠ `max_output_tokens >= 16` ಬೇಕು ಎಂದು ಜಾರಿಗೆ ತರಿಸುತ್ತದೆ. ಧೂಮಪಾನ ಪರೀಕ್ಷೆಗಳಿಗೆ 50+, ಉತ್ಪಾದನೆಗೆ 1000+ ಬಳಸಿ. |
| ಸ್ಟ್ರೀಂ ಅಂತರದಲ್ಲಿ `429 Too Many Requests` | Azure OpenAI ದಿಂದ ದರ ಮಿತಿ ಮುಟ್ಟಿದೆ | ಸ್ಟ್ರೀಂ ತೊಂದರೆಗಳಿಗೆ ಸಮಸ್ಯೆಗಳಿಲ್ಲದೆ ಮುರಿಯುತ್ತದೆ. ಸದಾ `async for event in await coroutine:` ಅನ್ನು `try/except` ನಲ್ಲಿ ಸುತ್ತಿಸಿ ಮತ್ತು `{"error": str(e)}` ಅನ್ನು ಫ್ರಂಟೆಂಡ್ಗೆ ನೀಡಿ. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | ತಪ್ಪಾದ ಟೆನೆಂಟ್ ಅಥವಾ ಲಾಗಿನ್ ಆಗಿಲ್ಲ | ಸ್ಪಷ್ಟವಾಗಿ `tenant_id=os.getenv("AZURE_TENANT_ID")` ಪಾಸ್ಮಾಡಿ. ಸ್ಥಳೀಯವಾಗಿ `azd auth login --tenant <tenant-id>` ರನ್ ಮಾಡಿ. |
| GitHub Models (`models.github.ai`) ಬಳಕೆ `404 Not Found` | GitHub Models Responses API ಬೆಂಬಲಿಸುವುದಿಲ್ಲ | GitHub Models ಕೋಡ್ ಮಾರ್ಗವನ್ನು ಸಂಪೂರ್ಣ ತೆಗೆಯಿರಿ. Azure OpenAI, OpenAI ಅಥವಾ ಹೊಂದಾಣಿಕೆಯ ಸ್ಥಳೀಯ ಎಂಡ್ಪಾಯಿಂಟ್ಗಳನ್ನು ಬಳಸಿ (ಉದಾ: Ollama with Responses support). |
| MAF `OpenAIChatCompletionClient` ಇನ್ನೂ ಚಾಟ್ ಪೂರ್ಣೀಕರಣಗಳು ಬಳಸುತ್ತಿದೆ | 1.0.0+ ನಲ್ಲಿ ಹಳೆಯ MAF ಕ್ಲೈಂಟ್ ಬಳಕೆ | MAF 1.0.0+ ನಲ್ಲಿ `OpenAIChatClient` ಡೀಫಾಲ್ಟ್ ರೀತಿಯಲ್ಲಿ Responses API ಬಳಸುತ್ತದೆ. `OpenAIChatCompletionClient` ಅನ್ನು `OpenAIChatClient` ಗೆ ಬದಲಿಸಿ. 1.0.0 ಪೂರ್ವಕ್ಕೆ `agent-framework-openai>=1.0.0` ಗೆ ಅಪ್‌ಗ್ರೇಡ್ ಮಾಡಿ. |
| LangChain ಏಜೆಂಟ್ ಖಾಲಿ ಅಥವಾ ಸಾಧನ ಕರೆಗಳಲ್ಲಿ ವಿಫಲ | `ChatOpenAI` Responses API ಬಳಸುತ್ತಿಲ್ಲ | `ChatOpenAI(...)` ಗೆ `use_responses_api=True` ಸೇರಿಸಿ. ಜೊತೆಗೆ ಪ್ರತಿಕ್ರಿಯಾ ಸಂದೇಶಗಳಲ್ಲಿ `.content` ಇದ್ದೇ `.text` ಗೆ ಬದಲಿಸಿ. |
| ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷ ನಿರ್ವಹಣೆಯಲ್ಲಿ `KeyError: 'innererror'` | Responses API ನಲ್ಲಿ ದೋಷ ದೇಹದ ರಚನೆ ಬದಲಾಗಿದೆ | `error.body["innererror"]["content_filter_result"]["jailbreak"]` ಅನ್ನು `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` ಗೆ ಮರುಬರೆಸಿ. `innererror` ಆವರಣ ಇಲ್ಲ, ವಿಷಯ ಫಿಲ್ಟರ್ ವಿವರಗಳು ಈಗ ಮೇಲ್ಮಟ್ಟದ `content_filters` ಪಟ್ಟಿಯಲ್ಲಿದೆ ಮತ್ತು ಪ್ರತಿ ನಮೂನೆಯಲ್ಲಿ `content_filter_results` (ಬಹುವಚನ) ಇದೆ. |
| `/openai/deployments/.../chat/completions` ಗೆ ಕಚ್ಚಾ HTTP ಕರೆ 404 ತಿರುಗಿಸುತ್ತದೆ | ಹಳೆಯ ಚಾಟ್ ಪೂರ್ಣೀಕರಣ REST ಎಂಡ್ಪಾಯಿಂಟ್ | URL ಅನ್ನು `/openai/v1/responses` ಗೆ ಮರುಬರೆಸಿ. ವಿನಂತಿ ದೇಹ: `messages` → `input`, `max_output_tokens` + `store: false` ಸೇರಿಸಿ, `api-version` query ಪ್ಯಾರಾಮ್ ತೆಗೆದುಹಾಕಿ. ಪ್ರತಿಕ್ರಿಯೆ ವಿಶ್ಲೇಷಣೆ: `choices[0].message.content` → `output[0].content[0].text` (ಗಮನಿಸಿ: `output_text` SDK ಅನುಕೂಲತೆ, ಕಚ್ಚಾ REST JSON ನಲ್ಲಿ ಇಲ್ಲ). |

---

## ಗೊತ್ತಿರಬೇಕಾದ ಅಂಶಗಳು

1. ನೀವು ಹಿಂದಿಗೆ ಚಾಟ್ ಪೂರ್ಣೀಕರಣಗಳನ್ನು ಸಂವಹನ ಸ್ಥಿತಿ үчүн ಬಳಸಿದರೆ, Responses ಸಹಾಯದಿಂದ ಸ್ವಯಂ ಸ್ಥಿತಿಯನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ನಿರ್ವಹಿಸಿ.
2. ಹಳೆಯ `max_tokens` ಬದಲು `max_output_tokens` ನ್ನು ಆದ್ಯತೆಯಾಗಿ ಉಪಯೋಗಿಸಿ.
3. `gpt-5` ಗೆ ವರ್ಗಾವಣೆಯಾಗುವಾಗ, `temperature` ಅನ್ನು ಸೂಚಿಸಬೇಡಿ ಅಥವಾ 1 ಇಟ್ಟುಕೊಳ್ಳಿ.
4. ಚಾಟ್ `content[].type: "text"` ಅನ್ನು Responses ನಲ್ಲಿ ಬಳಕೆದಾರ/ಸಿಸ್ಟಮ್ ಇನ್ಪುಟ್ಗೆ `content[].type: "input_text"` ಗೆ ಬದಲಿಸಿ.
5. `text.format` ಗಾಗಿ ಸರಿಯಾದ ಡಿಕ್ಷನರಿ ಒದಗಿಸಿ (ಉದಾ: `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ಸರಳ ಸ್ಟ್ರಿಂಗ್ ಅಲ್ಲ.
6. Responses ನಲ್ಲಿ `seed` ಪರಿಮಾಣವನ್ನು ಬೆಂಬಲಿಸಲ್ಪಡುವುದಿಲ್ಲ; ವಿನಂತಿಗಳಿಂದ ಅದನ್ನು ತೆಗೆದುಹಾಕಿ.
7. **ಯುಕ್ತಿ**: ಮೂಲ ಕೋಡ್ ಈಗಾಗಲೇ ಯುಕ್ತಿಯನ್ನು ಬಳಸುತ್ತಿದ್ದರೆ ಮಾತ್ರ ಅದನ್ನು ಸೇರಿಸಿ. ಯುಕ್ತಿ ಇಲ್ಲದ API ಕರೆಗಳಲ್ಲಿ `reasoning` ಸೇರಿಸಬೇಡಿ — ಅನೇಕ ಯುಕ್ತಿ ಇಲ್ಲದ ಮಾದರಿಗಳು ಈ ಪರಿಮಾಣವನ್ನು ಬೆಂಬಲಿಸದು.
8. **`max_output_tokens` ಗಾತ್ರ**: ಯುಕ್ತಿ ಮಾದರಿಗಳಿಗ (GPT-5-mini, GPT-5, o-ಸೇರೀಸ್) `max_output_tokens=4096` ಅಥವಾ ಹೆಚ್ಚು ಬಳಸಿ — 50–1000 ಅಲ್ಲ. ಮಾದರಿ ದೃಶ್ಯಮಾನದ ಔಟ್‌ಪುಟ್ ಗೆ ಮುನ್ನ ಆಂತರಿಕವಾಗಿ ಯುಕ್ತಿ ಟೋಕನ್ ಗಳನ್ನು ಬಳಸುತ್ತದೆ; ಕಡಿಮೆ ಮಿತಿ ಕಡಿತ ಅಥವಾ ಖಾಲಿ ಉತ್ತರಕ್ಕೆ ಕಾರಣವಾಗುತ್ತದೆ.
9. **o-ಸೇರೀಸ್ `max_completion_tokens`**: ಮೂಲ ಕೋಡ್ `max_completion_tokens` (o-ಸೇರೀಸ್ ಗಾಗಿ Azure-ನಿರ್ದಿಷ್ಟ) ಬಳಸಿದ್ದರೆ, ಅದನ್ನು `max_output_tokens` ಗೆ ಬದಲಿಸಿ. Responses API `max_completion_tokens` ನ್ನು ಅಂಗೀಕರಿಸುವುದಿಲ್ಲ.
10. **o-ಸೇರೀಸ್ `reasoning_effort`**: ಮೂಲ ಕೋಡ್ `reasoning_effort` (low/medium/high) ಬಳಸಿದ್ದರೆ, ಅದನ್ನು Responses API ಕರೆಗಳಲ್ಲಿ `reasoning={"effort": "<value>"}` ಗೆ ವರ್ಗಾಯಿಸಿ.
11. **o-ಸೇರೀಸ್ ಸ್ಟ್ರೀಮಿಂಗ್ ತಡ**: o-ಸೇರೀಸ್ ಮಾದರಿ ಔಟ್‌ಪುಟ್ ಉತ್ಪಾದನೆ ಮೊದಲು ಆಂತರಿಕ ಯುಕ್ತಿಯನ್ನು ನಡೆಸುತ್ತದೆ. ಸ್ಟ್ರೀಮಿಂಗ್ ಗೆ ಮೊದಲ `response.output_text.delta` ಇವೆಂಟ್ ಮುಂಚೆ ಹೆಚ್ಚು ತಡ ಸಾದ್ಯ. ಇದು ಸಾಮಾನ್ಯ — ಮಾದರಿ ಯುಕ್ತಿ ನಡೆಸುತ್ತಿದೆ, ಹ್ಯಾಗ್ ಆಗಿಲ್ಲ.
9. **`_azure_ad_token_provider` ಇಲ್ಲ**: `AsyncOpenAI` / `OpenAI` वस्तುವಿನಲ್ಲಿ `_azure_ad_token_provider` ಗುಣಲಕ್ಷಣವಿಲ್ಲ. ಪರೀಕ್ಷೆಗಳು ಅಥವಾ ಕೋಡ್ ಇದನ್ನು ಪ್ರವೇಶಿಸುವುದು `AttributeError` ಉಂಟುಮಾಡುತ್ತದೆ. ಟೋಕನ್ ಪ್ರೊವೈಡರ್‌ ಅನ್ನು `api_key` ರೂಪದಲ್ಲಿ ಪಾಸ್ ಮಾಡಲಾಗುತ್ತದೆ ಮತ್ತು ಕ್ಲೈಂಟ್ ವಸ್ತುವಿನಲ್ಲಿ ಪರಿಶೀಲನೆಗೆ ಅಲ್ಲ.
10. **ಸ್ನ್ಯಾಪ್‌ಶಾಟ್ / ಗೋಲ್ಡನ್ ಫೈಲ್‌ಗಳು**: ಪರೀಕ್ಷಾ ಸೆಟ್‌ವು ಸ್ನ್ಯಾಪ್‌ಶಾಟ್ ಪರೀಕ್ಷೆ ಬಳಸಿದರೆ, ಚಾಟ್ ಪೂರ್ಣೀಕರಣಗಳ ಸ್ಟ್ರೀಮಿಂಗ್ ಆಕಾರಗಳಾದ (`choices[0]`, `content_filter_results`, `function_call` ಇತ್ಯಾದಿ) ಎಲ್ಲಾ ಫೈಲ್‌ಗಳನ್ನು ಹೊಸ Responses ಆಕಾರಕ್ಕೆ ನವೀಕರಿಸಬೇಕು. ಇದನ್ನು ಮಿಸ್ ಮಾಡುವುದು ಸುಲಭವಲ್ಲ ಮತ್ತು ಸ್ನ್ಯಾಪ್‌ಶಾಟ್ ದೃಢೀಕರಣ ದೋಷಗಳಿಗೆ ಕಾರಣವಾಗುತ್ತದೆ.
11. **ಮಾಂಕಿ-ಪ್ಯಾಚ್ ಮಾರ್ಗ**: ಮಾಂಕಿಪ್ಯಾಚ್ ಗುರಿ ಹಳೆಯದು: `openai.resources.chat.AsyncCompletions.create` → ಹೊಸದು: `openai.resources.responses.AsyncResponses.create` (ಅಥವಾ ಸಿಂಕ್ ಗೆ `Responses.create`). ಹಳೆಯ ಮಾರ್ಗ ಬಳಕೆ ಮಾಡಬಹುದಾದ ಪರಿಣಾಮವಿಲ್ಲ — ಮಾಂಕಿ ಹಿಡಿಯುವುದಿಲ್ಲ, ಪರೀಕ್ಷೆಗಳು ನಿಜವಾದ API ಗೆ ಹೋದಿರುತ್ತವೆ ಅಥವಾ ವಿಫಲವಾಗುತ್ತವೆ.
12. **`input` ಅಲ್ಲ `messages`**: ಮಾಂಕಿ ಫಂಗಳಗಳು `kwargs.get("input")` ಓದಬೇಕು, `kwargs.get("messages")` ಅಲ್ಲ. Responses API ಸಂವಹನ ಇತಿಹಾಸಕ್ಕಾಗಿ `input` ಬಳಸುತ್ತದೆ.
13. **ಪರಿಸರ ವ್ಯತ್ಯಯದ ಹೆಸರು**: Azure Identity SDK `ManagedIdentityCredential(client_id=...)` ಗಾಗಿ `AZURE_CLIENT_ID` ( `AZURE_OPENAI_CLIENT_ID` ಅಲ್ಲ) ಬಳಸುತ್ತದೆ. ಪರೀಕ್ಷೆ, `.env` ಫೈಲ್‌ಗಳು, ಅಪ್ಲಿಕೇಶನ್ ಸೆಟ್ಟಿಂಗ್ಗಳು ಮತ್ತು Bicep/ಇನ್ಫ್ರಾ ನಲ್ಲಿ ಈ ಹೆಸರು ಬದಲಾಯಿಸಿ.
14. **`max_output_tokens` ಕನಿಷ್ಠ 16**: Azure OpenAI 16 ಕೆಳಗಿನ ಮೌಲ್ಯಗಳನ್ನು `400 integer_below_min_value` ನೊಂದಿಗೆ ನಿರಾಕರಿಸುತ್ತದೆ. ಧೂಮಪಾನ ಪರೀಕ್ಷೆಗಳಿಗೆ 50, ಉತ್ಪಾದನೆಗೆ 1000+ ಬಳಸಿ. ಹಳೆಯ `max_tokens` ಗೆ ಇಂಥ ಕನಿಷ್ಠತೆ ಇರಲಿಲ್ಲ.
15. **`AzureDeveloperCliCredential` ಗಾಗಿ `tenant_id`**: Azure OpenAI ಸಂಪನ್ಮೂಲ ಬೇರೆ ಟೆನೆಂಟ್‌ನಲ್ಲಿ ಇದ್ದರೆ, ನೀವು ಸ್ಪಷ್ಟವಾಗಿ `tenant_id` ಪಾಸ್ ಮಾಡಬೇಕು — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. ಇಲ್ಲದೆ ಇದ್ದರೆ, ಈ ಕ್ರೆಡೆನ್ಶಿಯಲ್ ತಪ್ಪು ಟೆನೆಂಟ್ ಬಳಸುವುದು ಮತ್ತು `401` ಅನ್ನು ನೀಡುವುದು.
16. **ಸ್ಟ್ರೀಮಿಂಗ್ ನಲ್ಲಿ ದರ ಮಿತಿಗಳನ್ನು ವಿಭಿನ್ನವಾಗಿ ತೋರಿಕೆ ಮಾಡುತ್ತದೆ**: ಚಾಟ್ ಪೂರ್ಣೀಕರದಲ್ಲಿ, 429 ಸಾಮಾನ್ಯವಾಗಿ ಸ್ಟ್ರೀಮ್ ಪ್ರಾರಂಭಿಸುವುದನ್ನು ನಿಲ್ಲಿಸುತ್ತಿತ್ತು. Responses API ಸ್ಟ್ರೀಮಿಂಗ್ ನಲ್ಲಿ, 429 **ಮಧ್ಯ-ಸ್ಟ್ರೀಮ್** ನಲ್ಲಿ ಸಂಭವಿಸಬಹುದು — ಅಸಿಂಕ್ ಇಟರೇಟರ್ ದೋಷವನ್ನು ಏರುತ್ತದೆ. ಸದಾ ಸ್ಟ್ರೀಮಿಂಗ್ ಲೂಪನ್ನು `try/except` ನಲ್ಲಿ ಸುತ್ತಿಸಿ ಮತ್ತು ದೋಷ JSON ಲೈನ್ ಅನ್ನು ಮತ್ತೆ ಪ್ರಜ್ಞಾಪೂರ್ವಕವಾಗಿ ಫ್ರಂಟೆಂಡ್‌ಗೆ ನೀಡಿರಿ.

17. **ವೆಬ್ ಅಪ್ಲಿಕೇಶನ್ಗಳಿಗೆ ಸ್ಟ್ರೀಮಿಂಗ್ ದೋಷ ನಿರ್ವಹಣೆ ಕಡ್ಡಾಯವಾಗಿದೆ**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` ಮಾದರಿ ಅತ್ಯಂತ ಮುಖ್ಯವಾಗಿದೆ. ಇದಿಲ್ಲದೆ, SSE/JSONL ಸ್ಟ್ರೀಮ್ ಯಾವುದೇ ಸರ್ವರ್-ಬದಿಯ ದೋಷದಲ್ಲಿ ಮುಂಭಾಗದಲ್ಲಿ ಯಾವುದೇ ತಡವಾಗದೆ ನಿಗ್ರಹಿಸುತ್ತದೆ ಮತ್ತು frontend ಹ್ಯಾಂಗ್ ಆಗುತ್ತದೆ.
18. **ಉಪಕರಣ ನಿರ್ಧಾರಗಳು ಫ್ಲಾಟ್ ಫಾರ್ಮ್ಯಾಟ್ ಬಳಸಬೇಕು**: Responses API ವೀಕ್ಷಿಸುತ್ತದೆ `{"type": "function", "name": ..., "parameters": ...}` — Chat Completions ನೆಸ್ಟ್ ಮಾಡಿದ `{"type": "function", "function": {"name": ..., "parameters": ...}}` ಅಲ್ಲ. ಇದು ಫಂಕ್ಷನ್-ಕಾಲಿಂಗ್ ಕೋಡ್‌ನಲ್ಲಿನ ಅತ್ಯಂತ ಸಾಮಾನ್ಯ ಮಾರ್ಗಾಂತರ ದೋಷವಾಗಿದೆ.
19. **`pydantic_function_tool()` ತುಂಡು ಹೊಂದಿಲ್ಲ**: `openai.pydantic_function_tool()` ಸಹಾಯಕರಾಗಿ ಇಂದಿಗೂ ಹಳೆಯ ನೆಸ್ಟ್ ಮಾಡಿದ ಫಾರ್ಮ್ಯಾಟ್ ತಯಾರಿಸುತ್ತದೆ. ಇದನ್ನು `responses.create()` ಜೊತೆ ಬಳಸಬೇಡಿ. ಉಪಕರಣ ಸ್ಕೀಮಾಗಳನ್ನು ಕೈಯಿಂದ ವ್ಯಾಖ್ಯಾನಿಸಿ ಅಥವಾ ಔಟ್‌పುಟ್ ಅನ್ನು ಫ್ಲ್ಯಾಟ್ ಮಾಡಿ.
20. **ಉಪಕರಣ ಫಲಿತಾಂಶಗಳು `function_call_output` ಬಳಸುತ್ತವೆ, `role: tool` ಅಲ್ಲ**: ಉಪಕರಣ ಕಾರ್ಯಗತಗೊಳಿಸಿದ ನಂತರ, `{"type": "function_call_output", "call_id": ..., "output": ...}` ಸೇರಿಸಿ — `{"role": "tool", "tool_call_id": ..., "content": ...}` ಅಲ್ಲ. ಸಹಾಯಕ ಉಪಕರಣ ವಿನಂತಿಗೆ, `messages.extend(response.output)` ಬಳಸಬೇಕು — ಕೈಯಿಂದ `{"role": "assistant", "tool_calls": [...]}` ಡಿಕ್ಟ್ ಮಾಡಬೇಡಿ.
21. **`strict: true`ಗೆ `required` + `additionalProperties: false` ಅಗತ್ಯವಿದೆ**: ಉಪಕರಣದಲ್ಲಿ `strict: true` ಬಳಸುವಾಗ, ಪ್ರತಿಯೊಂದು ಗುಣಧರ್ಮವೂ `required` ಅರೆನೆಯಲ್ಲಿ ಪಟ್ಟಿಯಾಗಿರಬೇಕು ಮತ್ತು `additionalProperties` ಮಿತಿ `false` ಆಗಿರಬೇಕು. ಇದರಲ್ಲಿ ಯಾವುದಾದರೂ ಕಾಣದಿದ್ದರೆ 400 ದೋಷ ಉಂಟಾಗುತ್ತದೆ.
22. **ಫಂಕ್ಷನ್ ಕಾಲ್ ಐಡಿಗಳಿಗೆ ನಿರ್ದಿಷ್ಟ ಪ್ರಿಫಿಕ್ಸ್ ಇರುತ್ತವೆ**: `input` ನಲ್ಲಿ ಕೆಲವು ಫಂಕ್ಷನ್ ಕಾಲ್ ಐಟಂಗಳನ್ನು ನೀಡುವಾಗ, `id` ಕ್ಷೇತ್ರವು `fc_` ಸಹಿತ ಪ್ರಾರಂಭವಾಗಿರಬೇಕು ಮತ್ತು `call_id` ಕ್ಷೇತ್ರವು `call_` ಸಹಿತ ಪ್ರಾರಂಭವಾಗಿರಬೇಕು (ಉದಾಹರಣೆ: `"id": "fc_example1", "call_id": "call_example1"`). ಹಳೆಯ Chat Completions ರ `call_` ಪ್ರಿಫಿಕ್ಸ್ ಅನ್ನು `id` ಗೆ ಬಳಸುವುದು ನಿರಾಕರಿಸಲಾಗುತ್ತದೆ.
23. **GitHub Models Responses API ಬೆಂಬಲಿಸುವುದಿಲ್ಲ**: ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿದ್ದರೆ GitHub Models ಕೋಡ್ ಪಾಠ (base_url `models.github.ai` ಅಥವಾ `models.inference.ai.azure.com` ಕಡೆಗೆ ಸೂಚಿಸುತ್ತಿದೆ), ಅದನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕಿ. ಯಾವುದೇ ಮಾರ್ಗಾಂತರ ಮಾರ್ಗವಿಲ್ಲ — ಇದನ್ನು Azure OpenAI, OpenAI ಅಥವಾ ಹೊಂದಿಕೆಯಾಗುವ ಸ್ಥಳೀಯ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗೆ ಬದಲಿಸಿ.
24. **ವಿಷಯ ಫಿಲ್ಟರ್ ದೋಷ ದೇಹದ ರಚನೆ ಬದಲಾಗಿದೆ**: Chat Completions ದೋಷಗಳು `error.body["innererror"]["content_filter_result"]` (ಏಕವಚನ) ಬಳಸುತ್ತಿದ್ದರು. Responses API ದೋಷಗಳು `error.body["content_filters"][0]["content_filter_results"]` (ಬಹುವಚನ, ಸರಣಿಯೊಳಗೆ) ಬಳಸುತ್ತವೆ. `innererror` ಕೀ ಈಗ ಇಲ್ಲ. ನೇರವಾಗಿ `innererror` ಗೆ ಪ್ರವೇಶಿಸುವ ಕೋಡ್ ರನ್‌ಟೈಮ್‌ನಲ್ಲಿ `KeyError` ಬಿರುಗಾಳಿ ಮಾಡುತ್ತದೆ — ಇದು ಮಾರ್ಗಾಂತರದಲ್ಲಿ ನೋಡಲು ಕಷ್ಟ, ಏಕೆಂದರೆ ಇದು ವಿಷಯ ಫಿಲ್ಟರ್_TRIGGER ಆಗುವಾಗ ಮಾತ್ರ ಕಾಣಿಸುತ್ತದೆ. ಮಾರ್ಗಾಂತರ ವೇಳೆ ಯಾವಾಗಲೂ `innererror` ಗೆ ಗ್ರೀಪ್ ಮಾಡಿ.
25. **ಕಚ್ಚಾ HTTP ಕರೆಗಳಿಗೆ URL + ದೇಹ ಮರುಬರೆದ ಅಗತ್ಯವಿದೆ**: ಅಪ್ಲಿಕೇಶನ್ಗಳು Azure OpenAI REST ನೇರವಾಗಿ (requests, httpx, aiohttp ಮೂಲಕ) `/openai/deployments/{name}/chat/completions?api-version=...` ಬಳಸುಂಕೊಳ್ಳುತ್ತಿರುದಾದರೆ, `/openai/v1/responses` ಗೆ ಬದಲಿ ಮಾಡಬೇಕು. ವಿನಂತಿಯ ದೇಹದಲ್ಲಿ `messages` ಬದಲು `input` ಬಳಸಲಾಗುತ್ತದೆ, `max_output_tokens` ಮತ್ತು `store` ಅಗತ್ಯವಿರುತ್ತವೆ ಮತ್ತು `api-version` ಕೇಳುವ ಪರಿಮಾಣವನ್ನು ತೆಗೆದುಹಾಕಲಾಗುತ್ತದೆ. ಪ್ರತಿಕ್ರಿಯೆಯ ದೇಹ ಪಠ್ಯ `output[0].content[0].text` ನಲ್ಲಿ ಇದೆ — **ಕಡ್ಡಾಯವಲ್ಲ** `output_text`, ಇದು SDK ಸೌಕರ್ಯದ ಗುಣ, ಕಚ್ಚಾ REST JSON ನಲ್ಲಿ ಇಲ್ಲ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->