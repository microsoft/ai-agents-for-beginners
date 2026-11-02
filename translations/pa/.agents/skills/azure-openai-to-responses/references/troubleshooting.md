# ਟਰੱਬਲਸ਼ੂਟਿੰਗ, ਜੋਖਮ ਟੇਬਲ ਅਤੇ ਗੌਟਚਾਜ਼

## 400 ਐਰਰਾਂ ਦੀ ਟਰੱਬਲਸ਼ੂਟਿੰਗ

| ਐਰਰ | ਠੀਕ ਕਰਨ ਦਾ ਢੰਗ |
|-------|-----|
| `missing_required_parameter: tools[0].name` | ਟੂਲ ਦੀ ਪਰਿਭਾਸ਼ਾ ਪੁਰਾਣੇ Chat Completions ਨੇਸਟਡ ਫਾਰਮੈਟ ਦਾ ਉਪਯੋਗ ਕਰਦੀ ਹੈ | `{"type": "function", "function": {"name": ...}}` ਤੋਂ `{"type": "function", "name": ..., "parameters": ...}` ਤੱਕ ਫਲੈਟ ਕਰੋ — ਨਾਮ, ਵਰਣਨ, ਪੈਰਾਮੀਟਰ ਸਿਖਰਲੇ ਪੱਧਰ 'ਤੇ ਜਾਣ |
| `unknown_parameter: input[N].tool_calls` | ਬਹੁ-ਦੌਰ ਟੂਲ ਨਤੀਜੇ ਪੁਰਾਣੇ Chat Completions ਫਾਰਮੈਟ ਦਾ ਉਪਯੋਗ ਕਰਦੇ ਹਨ | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ਨੂੰ `response.output` ਆਈਟਮਾਂ + `{"type": "function_call_output", "call_id": ..., "output": ...}` ਨਾਲ ਬਦਲੋ |
| `invalid_function_parameters: 'required' is required` | `strict: true` ਟੂਲ ਵਿੱਚ `required` ਐਰੇ ਨਹੀਂ ਹੈ | ਜਦੋਂ `strict: true` ਹੁੰਦਾ ਹੈ, ਤਾਂ ਸਾਰੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ `required` ਵਿੱਚ ਦਿੱਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ `additionalProperties: false` ਸੈੱਟ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` ਟੂਲ ਵਿੱਚ `additionalProperties: false` ਨਹੀਂ ਹੈ | ਪੈਰਾਮੀਟਰ ਓਬਜੈਕਟ ਵਿੱਚ `"additionalProperties": false` ਸ਼ਾਮਿਲ ਕਰੋ |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID ਵਿੱਚ ਗਲਤ ਪ੍ਰੀਫਿਕਸ ਹੈ | ਫੰਕਸ਼ਨ ਕਾਲ IDਜ਼ ਦੀ ਸ਼ੁਰੂਆਤ `fc_` ਨਾਲ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ (ਜਿਵੇਂ `fc_example1`), ਨਾ ਕਿ `call_` ਨਾਲ |
| `missing_required_parameter: text.format.name` | ਫਾਰਮੈਟ ਡਿਕਟ ਵਿੱਚ `"name"` ਕੀ ਸ਼ਾਮਿਲ ਕਰੋ (ਜਿਵੇਂ `"name": "Output"`) |
| `invalid_type: text.format` | ਯਕੀਨੀ ਬਣਾਓ ਕਿ `text.format` ਇੱਕ ਡਿਕਟ ਹੈ ਜਿਸ ਵਿੱਚ `type`, `name`, `strict`, `schema` ਕੁੰਜੀਆਂ ਹਨ — ਸਤਰਿੰਗ ਨਹੀਂ |
| `invalid input content type` | Chat ਦੇ `text` ਦੀ ਥਾਂ `input_text`/`output_text` ਸਮੱਗਰੀ ਟਾਈਪ ਵਰਤੋਂ |
| `invalid input content type` (ਚਿੱਤਰ) | ਚਿੱਤਰ ਸਮੱਗਰੀ ਹਾਲੇ `"type": "image_url"` ਵਰਤਦੀ ਹੈ | ਇਸ ਨੂੰ `"type": "input_image"` ਵਿੱਚ ਬਦਲੋ |
| `Expected object, got string` on `image_url` | `image_url` ਹਾਲੇ ਨੇਸਟਡ ਓਬਜੈਕਟ `{"url": "..."}` ਹੈ | ਇਸ ਨੂੰ ਸਾਦੇ ਸਤਰਿੰਗ ਵਿੱਚ ਫਲੈਟ ਕਰੋ: `"image_url": "https://..."` ਜਾਂ `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI 'ਤੇ ਘੱਟੋ ਘੱਟ **16** ਹੈ। ਟੈਸਟ ਲਈ 50+ ਅਤੇ ਪ੍ਰੋਡਕਸ਼ਨ ਲਈ 1000+ ਵਰਤੋਂ |
| `429 Too Many Requests` streaming ਦੌਰਾਨ | ਦਰ ਖਪਤ ਸੀਮਿਤ ਹੈ। ਸਟ੍ਰੀਮਿੰਗ ਨੂੰ `try/except` ਵਿੱਚ ਲਪੇਟੋ, ਐਰਰ JSON ਨੂੰ ਫਰੰਟਐਂਡ ਤੇ ਦੇਵੋ, ਬੈਕਆਫ/ਰੀਟ੍ਰਾਈ ਲਾਗੂ ਕਰੋ |
| `KeyError: 'innererror'` content filter ਐਰਰ 'ਤੇ | Responses API ਵਿੱਚ content filter ਐਰਰ ਬਾਡੀ ਢਾਂਚਾ ਬਦਲ ਗਿਆ | Chat Completions `error.body["innererror"]["content_filter_result"]` ਵਰਤਦਾ ਸੀ; Responses API ਹੁਣ `error.body["content_filters"][0]["content_filter_results"]` (ਬਹੁਵਚਨ, ਐਰੇ ਵਿੱਚ) ਵਰਤਦਾ ਹੈ। ਸਾਰੇ `innererror` ਪਹੁੰਚ ਨੂੰ ਦੁਬਾਰਾ ਲਿਖੋ |

---

## ਮਾਈਗ੍ਰੇਸ਼ਨ ਜੋਖਮ ਟੇਬਲ

| ਲੱਛਣ | ਸੰਭਾਵਿਤ ਗਲਤੀ | ਠੀਕ ਕਰਨ ਦਾ ਢੰਗ |
|---------|---------------|-----|
| ਖਾਲੀ `output_text` / ਕੱਟਿਆ ਹੋਇਆ ਜਵਾਬ | reasoning ਮਾਡਲਾਂ ਲਈ `max_output_tokens` ਬਹੁਤ ਘੱਟ ਹੈ | `max_output_tokens=1000` ਜਾਂ ਇਸ ਤੋਂ ਵੱਧ ਸੈੱਟ ਕਰੋ — reasoning ਟੋਕਨ ਗਿਣਤੀ ਲਿਮਿਟ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੁੰਦੇ ਹਨ |
| `400 invalid_type: text.format` | `text.format` ਡਿਕਟ ਦੀ ਥਾਂ `response_format` ਸਤਰਿੰਗ ਦਿੱਤੀ ਗਈ | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` ਵਰਤੋਂ |
| `/openai/v1/responses` 'ਤੇ `404 Not Found` | ਗਲਤ `base_url` — `/openai/v1/` ਸਫਿਕਸ ਮੌਜੂਦ ਨਹੀਂ | ਯਕੀਨੀ ਬਣਾਓ `base_url=f"{endpoint}/openai/v1/"` (ਟਰੈਲਿੰਗ ਸਲੈਸ਼ ਨਾਲ) |
| `401 Unauthorized` OpenAI() ਵਿੱਚ ਬਦਲਾਅ ਤੋਂ ਬਾਅਦ | `api_key` ਸੈੱਟ ਨਹੀਂ ਹੋਇਆ ਜਾਂ ਟੋਕਨ ਪ੍ਰਦਾਇਕ ਸਹੀ ਤਰ੍ਹਾਂ ਨਹੀਂ ਦਿੱਤਾ | EntraID ਲਈ: `api_key=token_provider` (ਕਾਲੇਬਲ). API ਕੀ ਲਈ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| ਮਾਡਲ `deployment not found` ਵਾਪਸ ਕਰਦਾ ਹੈ | `model` ਪੈਰਾਮ ਤੁਹਾਡੇ Azure ਡਿਪਲੋਇਮੈਂਟ ਨਾਮ ਨਾਲ ਮੇਲ ਨਹੀਂ ਖਾਂਦਾ | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` ਵਰਤੋਂ — ਇਹ ਡਿਪਲੋਇਮੈਂਟ ਨਾਮ ਹੈ, ਮਾਡਲ ਨਾਮ ਨਹੀਂ |
| `json.loads(resp.output_text)` ਵਿੱਚ `JSONDecodeError` | ਸਕੀਮਾ ਲਾਗੂ ਨਹੀਂ ਹੈ ਜਾਂ ਮਾਡਲ ਸਖਤ JSON ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦਾ | ਸਕੀਮਾ ਵਿੱਚ `"strict": True"` ਯਕੀਨੀ ਬਣਾਓ ਅਤੇ ਮਾਡਲ ਸਟ੍ਰਕਚਰਡ ਆਉਟਪੁੱਟ ਸਮਰਥਨ ਕਰਦਾ ਹੈ ਜਾਂ ਨਹੀਂ ਵੇਖੋ |
| Streaming ਵਿੱਚ ਕੋਈ `delta` ਇਵੈਂਟ ਨਹੀਂ ਆ ਰਿਹਾ | ਗਲਤ ਇਵੈਂਟ ਕਿਸਮ ਦੀ ਜਾਂਚ ਕਰਨਾ | `event.type == "response.output_text.delta"` 'ਤੇ ਫਿਲਟਰ ਕਰੋ, ਨਾ ਕਿ Chat ਦਾ `chat.completion.chunk` |
| ਮਾਈਗ੍ਰੇਸ਼ਨ ਤੋਂ ਬਾਅਦ ਚਿੱਤਰ ਇਨਪੁੱਟ 'ਤੇ `400` ਐਰਰ | ਚਿੱਤਰ ਸਮੱਗਰੀ ਦੀ ਕਿਸਮ ਅਪਡੇਟ ਨਹੀਂ ਕੀਤੀ ਗਈ | `"type": "image_url"` → `"type": "input_image"` ਅਤੇ `"image_url": {"url": "..."}` ਫਲੈਟ ਕਰਕੇ `"image_url": "..."` ਵਿੱਚ ਬਦਲੋ (ਸਧਾਰਨ ਸਤਰਿੰਗ) |
| ਟੂਲ ਕਾਲ ਅਨੰਤ ਚੱਕਰ ਵਿੱਚ ਫੈਸਲੇ ਕਰਦੇ ਹਨ | ਫਾਲੋ-ਅੱਪ `input` ਵਿੱਚ ਟੂਲ ਨਤੀਜਾ ਗੁੰਮ ਹੈ | ਟੂਲ ਚਲਾਉਣ ਤੋਂ ਬਾਅਦ, ਅਗਲੇ ਰਿਕੁਏਸਟ ਵਿੱਚ `input` 'ਚ `{"type": "function_call_output", "call_id": ..., "output": ...}` ਆਈਟਮ ਜੋੜੋ |
| GPT-5 ਜਾਂ o-ਸੀਰੀਜ਼ ਨਾਲ `temperature` ਐਰਰ | 1 ਦੇ ਇਲਾਵਾ ਕਿਸੇ ਹੋਰ `temperature` ਦੀ ਕਦਰ | GPT-5 ਅਤੇ o-ਸੀਰੀਜ਼ ਮਾਡਲਾਂ ਲਈ `temperature` ਹਟਾਓ ਜਾਂ 1 ਸੈੱਟ ਕਰੋ (o1, o3-mini, o3, o4-mini) |
| o-ਸੀਰੀਜ਼ ਨਾਲ `top_p` ਐਰਰ | `top_p` ਸਮਰਥਿਤ ਨਹੀਂ | o-ਸੀਰੀਜ਼ ਮਾਡਲਾਂ ਦੇ ਲਈ `top_p` ਹਟਾਓ |
| `max_completion_tokens` ਪਛਾਣਯੋਗ ਨਹੀਂ | Azure ਵਿਸ਼েষ ਪੈਰਾਮੀਟਰ ਵਰਤ ਰਹੇ | `max_completion_tokens` ਨੂੰ `max_output_tokens` ਨਾਲ ਬਦਲੋ। o- ਸੀਰੀਜ਼ ਲਈ 4096+ ਸੈੱਟ ਕਰੋ (reasoning ਟੋਕਨ ਲਿਮਿਟ ਵਿੱਚ ਸ਼ਾਮਿਲ) |
| o-ਸੀਰੀਜ਼ ਤੋਂ ਖਾਲੀ/ਕੱਟਿਆ ਹੋਇਆ ਆਉਟਪੁੱਟ | `max_output_tokens` ਬਹੁਤ ਘੱਟ | o-ਸੀਰੀਜ਼ ਅੰਦਰੋਨੀ ਤੌਰ ਤੇ reasoning ਟੋਕਨ ਵਰਤਦਾ ਹੈ। `max_output_tokens=4096` ਜਾਂ ਵੱਧ ਸੈੱਟ ਕਰੋ — 500–1000 ਨਹੀਂ |
| `400 integer_below_min_value` ਲਈ `max_output_tokens` | 16 ਤੋਂ ਘੱਟ ਕਦਰ | Azure OpenAI `max_output_tokens >= 16` ਲਾਗੂ ਕਰਦਾ ਹੈ। ਸੌਖੇ ਟੈਸਟ ਲਈ 50+, ਪ੍ਰੋਡਕਸ਼ਨ ਲਈ 1000+ ਵਰਤੋਂ |
| `429 Too Many Requests` ਮੱਧ-ਸਟਰੀਮ | Azure OpenAI ਵੱਲੋਂ ਦਰ ਸੀਮਾ | ਸਟਰੀਮ ਖ਼ਾਮੋਸ਼ੀ ਨਾਲ ਟੁੱਟ ਜਾਂਦਾ ਹੈ ਬਿਨਾਂ ਐਰਰ ਹੈਂਡਲਿੰਗ ਦੇ। ਹਮੇਸ਼ਾ `async for event in await coroutine:` ਨੂੰ `try/except` ਵਿੱਚ ਲਪੇਟੋ ਅਤੇ ਫਰੰਟਐਂਡ ਨੂੰ `{"error": str(e)}` ਦਿਓ |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | ਗਲਤ ਟੈਨੈਂਟ ਜਾਂ ਲੋਗਇਨ ਨਹੀਂ ਕੀਤਾ | ਵੱਖਰੇ `tenant_id=os.getenv("AZURE_TENANT_ID")` ਸਪੱਸ਼ਟ ਤੌਰ ਤੇ ਦਿਓ। ਲੋਕਲ ਵਿੱਚ `azd auth login --tenant <tenant-id>` ਚਲਾਓ |
| GitHub Models (`models.github.ai`) ਨਾਲ `404 Not Found` | GitHub Models Responses API ਨੂੰ ਸਹਿਯੋਗ ਨਹੀਂ ਕਰਦਾ | GitHub Models ਦਾ ਕੋਡ ਰਾਹ ਪੂਰੀ ਤਰ੍ਹਾਂ ਹਟਾਓ। Azure OpenAI, OpenAI ਜਾਂ ਇੱਕ ਅਨੁਕੂਲ ਲੋਕਲ ਐਂਡਪੌਇੰਟ (ਜਿਵੇਂ Ollama Responses ਸਹਿਯੋਗ ਨਾਲ) ਵਰਤੋਂ |
| MAF `OpenAIChatCompletionClient` ਹਾਲੇ ਵੀ Chat Completions ਵਰਤਦਾ ਹੈ | 1.0.0+ ਵਿੱਚ ਲੇਗਸੀ MAF ਕਲਾਇੰਟ ਵਰਤੋਂ | MAF 1.0.0+ ਵਿੱਚ `OpenAIChatClient` ਡਿਫ਼ਾਲਟ ਤੌਰ ਤੇ Responses API ਵਰਤਦਾ ਹੈ। `OpenAIChatCompletionClient` ਨੂੰ `OpenAIChatClient` ਨਾਲ ਬਦਲੋ। 1.0.0 ਤੋਂ ਪਹਿਲਾਂ, `agent-framework-openai>=1.0.0` ਨੂੰ ਅਪਗ੍ਰੇਡ ਕਰੋ |
| LangChain ਏਜੰਟ ਖਾਲੀ ਵਾਪਸੀ ਜਾਂ ਟੂਲ ਕਾਲਾਂ ਨਾਲ ਫੇਲ | `ChatOpenAI` Responses API ਨਹੀਂ ਵਰਤਦਾ | `ChatOpenAI(...)` ਵਿੱਚ `use_responses_api=True` ਸ਼ਾਮਿਲ ਕਰੋ। ਨਾਲ ਹੀ ਪ੍ਰਤੀਕਿਰਿਆ ਦੇ ਮੈਸੇਜਾਂ ਵਿੱਚ `.content` → `.text` ਕਰੋ |
| content filter ਐਰਰ ਹੈਂਡਲਰ ਵਿੱਚ `KeyError: 'innererror'` | Responses API ਵਿੱਚ ਐਰਰ ਬਾਡੀ ਦਾ ਢਾਂਚਾ ਬਦਲ ਗਿਆ |  `error.body["innererror"]["content_filter_result"]["jailbreak"]` ਨੂੰ `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` ਨਾਲ ਦੁਬਾਰਾ ਲਿਖੋ। `innererror` ਵ੍ਰੈੱਪਰ ਹਟ ਗਿਆ ਹੈ; ਹੁਣ ਸਮੱਗਰੀ ਫਿਲਟਰ ਵੇਰਵੇ ਉੱਤੇ-ਪੱਧਰੀ `content_filters` ਐਰੇ ਵਿੱਚ ਅਤੇ ਹਰ ਐਂਟਰੀ ਵਿੱਚ `content_filter_results` (ਬਹੁਵਚਨ) ਹਨ |
| `/openai/deployments/.../chat/completions` 'ਤੇ ਕੱਚਾ HTTP ਕਾਲ 404 ਵਾਪਸ ਕਰਦਾ ਹੈ | ਪੁਰਾਣਾ Chat Completions REST ਏਂਡਪੌਇੰਟ | URL ਨੂੰ `/openai/v1/responses` 'ਤੇ ਦੁਬਾਰਾ ਲਿਖੋ। ਬੇਨਤੀ ਬਾਡੀ: `messages` → `input`, `max_output_tokens` ਅਤੇ `store: false` ਸ਼ਾਮਿਲ ਕਰੋ, `api-version` ਕਵੇਰੀ ਪੈਰਾਮ ਹਟਾਓ। ਜਵਾਬ ਵਿਖੇ: `choices[0].message.content` → `output[0].content[0].text` (ਧਿਆਨ: `output_text` SDK ਸੁਵਿਧਾ ਹੈ, ਕੱਚੇ REST JSON ਵਿੱਚ ਨਹੀਂ) |

---

## ਗੌਟਚਾਜ਼

1. ਜੇ ਤੁਸੀਂ ਪਹਿਲਾਂ ਗੱਲਬਾਤ ਦੀ ਸਥਿਤੀ ਲਈ Chat Completions ਵਰਤਦੇ ਸਨ, ਤਾਂ ਹੁਣ Responses ਨਾਲ ਆਪਣੀ ਸਥਿਤੀ ਖੁਦ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰੋ।
2. ਲੇਗਸੀ `max_tokens` ਦੀ ਥਾਂ `max_output_tokens` ਵਰਤੋਂ।
3. `gpt-5` ਵਿੱਚ ਮਾਈਗ੍ਰੇਟ ਕਰਨ ਸਮੇਂ ਯਕੀਨੀ ਬਣਾਓ ਕਿ `temperature` ਨਾਹ ਦੱਸਿਆ ਗਿਆ ਹੋਵੇ ਜਾਂ ਇਹ `1` ਤੇ ਸੈੱਟ ਹੈ।
4. ਯੂਜ਼ਰ/ਸਿਸਟਮ ਇਨਪੁੱਟ ਲਈ Chat `content[].type: "text"` ਨੂੰ Responses `content[].type: "input_text"` ਨਾਲ ਬਦਲੋ।
5. `text.format` ਲਈ ਠੀਕ ਡਿਕਟ ਦਿਓ (ਜਿਵੇਂ `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ਸਧਾਰਨ ਸਤਰਿੰਗ ਨਹੀਂ।
6. Responses ਵਿੱਚ `seed` ਪੈਰਾਮੀਟਰ ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਹੁੰਦਾ; ਇਸਨੂੰ ਬਿਨਤੀ ਤੋਂ ਹਟਾਓ।
7. **Reasoning**: ਕੇਵਲ ਉਹਨਾਂ API ਕਾਲਾਂ ਵਿੱਚ reasoning ਸ਼ਾਮਿਲ ਕਰੋ ਜਿੱਥੇ ਮੂਲ ਕੋਡ ਨੇ ਇਸਦਾ ਉਪਯੋਗ ਕੀਤਾ ਸੀ। ਜੋ ਪ੍ਰਭਾਵੀ ਮਾਡਲ reasoning ਨਹੀਂ ਕਰਦੇ ਉਹਨਾਂ ਵਿੱਚ ਇਹ ਪੈਰਾਮੀਟਰ ਨਾ ਜੋੜੋ।
8. **`max_output_tokens` ਦਾ ਅਕਾਰ**: reasoning ਮਾਡਲਾਂ (GPT-5-mini, GPT-5, o-ਸੀਰੀਜ਼) ਲਈ `max_output_tokens=4096` ਜਾਂ ਉਸ ਤੋਂ ਵੱਧ ਸੈੱਟ ਕਰੋ — 50–1000 ਨਹੀਂ। ਮਾਡਲ ਅੰਦਰੂਨੀ ਤੌਰ ਤੇ reasoning ਟੋਕਨ ਵਰਤਦਾ ਹੈ ਜੋ ਦ੍ਰਸ਼ਯਮਾਨ ਆਉਟਪੁੱਟ ਦੇ ਪਹਿਲਾਂ ਹੁੰਦੇ ਹਨ; ਬਹੁਤ ਘੱਟ ਸੈਟਿੰਗ truncated ਜਾਂ ਖਾਲੀ ਜਵਾਬਾਂ ਦਾ ਕਾਰਨ ਬਣਦੀ ਹੈ।
9. **O-ਸੀਰੀਜ਼ `max_completion_tokens`**: ਜੇ ਮੂਲ ਕੋਡ ਨੇ `max_completion_tokens` (o-ਸੀਰੀਜ਼ ਲਈ Azure ਵਿਸ਼ੇਸ਼) ਵਰਤਿਆ ਹੈ, ਤਦ ਇਸ ਨੂੰ `max_output_tokens` ਨਾਲ ਬਦਲੋ। Responses API `max_completion_tokens` ਨਹੀਂ ਮੰਨਦੀ।
10. **O-ਸੀਰੀਜ਼ `reasoning_effort`**: ਜੇ ਮੂਲ ਕੋਡ `reasoning_effort` ਵਰਤਦਾ ਹੈ (low/medium/high), ਤਦ ਇਸਨੂੰ Responses API ਕਾਲ ਵਿੱਚ `reasoning={"effort": "<value>"}` ਵਿੱਚ ਮਾਈਗ੍ਰੇਟ ਕਰੋ।
11. **O-ਸੀਰੀਜ਼ ਸਟ੍ਰੀਮਿੰਗ ਦੇਰੀ**: O-ਸੀਰੀਜ਼ ਮਾਡਲ ਆਉਟਪੁੱਟ ਪੈਦਾ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਅੰਦਰੂਨੀ reasoning ਕਰਦੇ ਹਨ। ਜਦੋਂ ਸਟ੍ਰੀਮਿੰਗ ਹੋ ਰਹੀ ਹੋਵੇ ਤਾਂ ਪਹਿਲਾ `response.output_text.delta` ਇਵੈਂਟ ਆਉਣ ਵਿੱਚ ਜ਼ਿਆਦਾ ਦੇਰੀ ਆਮ ਗੱਲ ਹੈ — ਮਾਡਲ reasoning ਕਰ ਰਿਹਾ ਹੈ, ਹਿਂਗ ਨਹੀਂ।
9. **`_azure_ad_token_provider` ਮੁਕ ਗਿਆ**: `AsyncOpenAI` / `OpenAI` ਵਿੱਚ ਕਿਸੇ `_azure_ad_token_provider` ਐਟ੍ਰਿਬਿਊਟ ਦੀ ਗੈਰਮੌਜੂਦਗੀ ਹੈ। ਟੈਸਟਾਂ ਜਾਂ ਕੋਡ ਜੋ ਇਸ ਐਟ੍ਰਿਬਿਊਟ ਐਕਸੈੱਸ ਕਰਦੇ ਹਨ, `AttributeError` ਨਾਲ ਫੇਲ ਹੋਣਗੇ। ਟੋਕਨ ਪ੍ਰਦਾਇਕ `api_key` ਵਜੋਂ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਕਲਾਇੰਟ ਓਬਜੈਕਟ ਤੇ ਇੰਸਪੈਕਟ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ।
10. **ਸਨੇਪਸ਼ਾਟ / ਗੋਲਡਨ ਫਾਈਲਾਂ**: ਜੇ ਟੈਸਟ ਸੂਟ ਸਨੇਪਸ਼ਾਟ ਟੈਸਟਿੰਗ ਵਰਤਦਾ ਹੈ, ਤਾਂ ਸਾਰੇ ਸਨੇਪਸ਼ਾਟ ਫਾਈਲਾਂ ਜਿਨ੍ਹਾਂ ਵਿੱਚ Chat Completions ਸਟ੍ਰੀਮਿੰਗ ਸ਼ੇਪਾਂ (`choices[0]`, `content_filter_results`, `function_call` ਆਦਿ) ਹਨ, ਉਹਨੂੰ ਨਵੀਂ Responses ਸ਼ੇਪ ਦੇ ਅਨੁਕੂਲ ਅਪਡੇਟ ਕਰਨ ਦੀ ਲੋੜ ਹੈ। ਇਹ ਆਸਾਨੀ ਨਾਲ ਛੁਟ ਸਕਦਾ ਹੈ ਅਤੇ ਸਨੇਪਸ਼ਾਟ ਦਲੀਲਾਂ ਦੀਆਂ ਗਲਤੀਆਂ ਕਰਦਾ ਹੈ।
11. **ਮੌਕ ਮੰਕੀਪੈਚ ਪਾਥ**: ਮੰਕੀਪੈਚ ਟਾਰਗਟ `openai.resources.chat.AsyncCompletions.create` ਤੋਂ `openai.resources.responses.AsyncResponses.create` (ਜਾਂ ਐਸਿੰਕ ਦੇ ਲਈ `Responses.create`) ਵਿੱਚ ਬਦਲ ਗਿਆ ਹੈ। ਪੁਰਾਣਾ ਪਾਥ ਬਿਨਾ ਕਿਸੇ ਧੁਨੀ ਦੇ ਕੁਝ ਨਹੀਂ ਕਰਦਾ — ਮੌਕ ਇੰਟਰਸੈਪਟ ਨਹੀਂ ਕਰੇਗਾ ਅਤੇ ਟੈਸਟ ਸੱਚੇ API ਨੂੰ ਲੱਗ ਜਾਣਗੇ ਜਾਂ ਫੇਲ ਹੋਣਗੇ।
12. **`input` ਨਾ ਕਿ `messages`**: ਮੌਕ ਫੰਕਸ਼ਨਾਂ ਨੂੰ `kwargs.get("input")` ਪੜ੍ਹਨਾ ਚਾਹੀਦਾ ਹੈ ਨਾ ਕਿ `kwargs.get("messages")`। Responses API ਗੱਲਬਾਤ ਇਤਿਹਾਸ ਲਈ `input` ਵਰਤਦਾ ਹੈ।
13. **ਪਰਿਆਵਰਨ ਵੈਰੀਏਬਲ ਨਾਂ**: Azure Identity SDK `ManagedIdentityCredential(client_id=...)` ਲਈ `AZURE_CLIENT_ID` ਵਰਤਦਾ ਹੈ (ਨਹੀਂ `AZURE_OPENAI_CLIENT_ID`)। ਟੈਸਟਾਂ, `.env` ਫਾਈਲਾਂ, ਐਪ ਸੈਟਿੰਗਜ਼ ਅਤੇ Bicep/ਇੰਫਰਾ ਵਿੱਚ ਇਹਨਾਂ ਨੂੰ ਬਦਲੋ।
14. **`max_output_tokens` ਦੀ ਘੱਟੋ-ਘੱਟ ਕਦਰ 16 ਹੈ**: Azure OpenAI 16 ਤੋਂ ਘੱਟ ਕਦਰਾਂ ਨੂੰ `400 integer_below_min_value` ਨਾਲ ਰੱਦ ਕਰਦਾ ਹੈ। ਸੌਖੇ ਟੈਸਟ ਲਈ 50 ਵਰਤੋਂ, ਪ੍ਰੋਡਕਸ਼ਨ ਲਈ 1000+। ਪੁਰਾਣਾ `max_tokens` ਅਜਿਹਾ ਘੱਟੋ-ਘੱਟ ਨਹੀਂ ਸੀ।
15. **`tenant_id` `AzureDeveloperCliCredential` ਲਈ**: ਜਦੋਂ Azure OpenAI ਸਰੋਤ ਵੱਖਰੇ ਟੈਨੈਂਟ ਵਿੱਚ ਹੋਵੇ, ਤਦ ਤੁਹਾਨੂੰ `tenant_id` ਸਪੱਸ਼ਟ ਤੌਰ ਤੇ ਦੇਣਾ ਜਰੂਰੀ ਹੈ — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`। ਇਸ ਦੇ ਬਿਨਾ ਕ੍ਰੈਡੈਂਸ਼ੀਅਲ ਗਲਤ ਟੈਨੈਂਟ ਸ੍ਹਮਤ ਤੌਰ 'ਤੇ ਵਰਤੇਗਾ ਅਤੇ `401` ਵਾਪਸ ਕਰੇਗਾ।
16. **ਸਟ੍ਰੀਮਿੰਗ ਵਿੱਚ ਦਰ ਸੀਮਾਵਾਂ ਵੱਖਰੇ ਢੰਗ ਨਾਲ ਸਾਹਮਣੇ ਆਦੀਆਂ ਹਨ**: Chat Completions ਨਾਲ, 429 ਆਮ ਤੌਰ ਤੇ ਸਟ੍ਰੀਮ ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਰੋਕਦਾ ਸੀ। Responses API ਸਟ੍ਰੀਮਿੰਗ ਵਿੱਚ, 429 ਮੱਧ-ਸਟ੍ਰੀਮ ਵੀ ਆ ਸਕਦਾ ਹੈ — ਐਸਿੰਕ ਇਟਰੇਟਰ ਛੁਟਕਾਰਾ ਦਿੰਦਾ ਹੈ। ਹਮੇਸ਼ਾ ਸਟ੍ਰੀਮਿੰਗ ਲੂਪ ਨੂੰ `try/except` ਵਿੱਚ ਲਪੇਟੋ ਅਤੇ ਐਰਰ JSON ਲਾਈਨ ਯੀਲਡ ਕਰੋ ਤਾਂ ਜੋ ਫਰੰਟਐਂਡ ਇਸਨੂੰ ਢਾਂਗ ਨਾਲ ਹੈਂਡਲ ਕਰ ਸਕੇ।

17. **ਵੈੱਬ ਐਪਸ ਲਈ ਸਟ੍ਰੀਮਿੰਗ ਐਰਰ ਹੈਂਡਲਿੰਗ ਜ਼ਰੂਰੀ ਹੈ**: ਪੈਟਰਨ `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` ਬਹੁਤ ਮਹੱਤਵਪੂਰਨ ਹੈ। ਇਸ ਦੇ ਬਿਨਾਂ, SSE/JSONL ਸਟਰਿਮ ਕਿਸੇ ਵੀ ਸਰਵਰ-ਸਾਈਡ ਐਰਰ 'ਤੇ ਚੁੱਪਚਾਪ ਰੁਕ ਜਾਂਦੀ ਹੈ ਅਤੇ ਫਰੰਟਐਂਡ ਫ੍ਰੀਜ਼ ਹੋ ਜਾਂਦਾ ਹੈ।
18. **ਟੂਲ ਪਰਿਭਾਸ਼ਾਵਾਂ ਫਲੈਟ ਫਾਰਮੈਟ ਨੂੰ ਵਰਤਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ**: Responses API ਨੂੰ `{"type": "function", "name": ..., "parameters": ...}` ਦੀ ਉਮੀਦ ਹੈ — ਚੈਟ ਕંપਲੀਸ਼ਨਜ਼ ਦੇ nested `{"type": "function", "function": {"name": ..., "parameters": ...}}` ਨਹੀਂ। ਇਹ ਫੰਕਸ਼ਨ-ਕਾਲਿੰਗ ਕੋਡ ਲਈ ਸਭ ਤੋਂ ਆਮ ਮਾਈਗ੍ਰੇਸ਼ਨ ਗਲਤੀ ਹੈ।
19. **`pydantic_function_tool()` ਅਣਕੰਪੈਟਬਲ ਹੈ**: `openai.pydantic_function_tool()` ਹੈਲਪਰ ਅਜੇ ਵੀ ਪੁਰਾਣਾ nested ਫਾਰਮੈਟ ਬਣਾਉਂਦਾ ਹੈ। ਇਸ ਨੂੰ `responses.create()` ਨਾਲ ਵਰਤੋਂ ਨ ਕਰੋ। ਟੂਲ ਸਕੀਮਾਂ ਨੂੰ ਮੈਨੁਅਲ ਤੌਰ 'ਤੇ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ ਜਾਂ ਆਉਟਪੁੱਟ ਨੂੰ ਫਲੈਟ ਕਰੋ।
20. **ਟੂਲ ਨਤੀਜੇ `function_call_output` ਵਰਤਦੇ ਹਨ, `role: tool` ਨਹੀਂ**: ਟੂਲ ਚਲਾਉਣ ਤੋਂ ਬਾਅਦ, `{"type": "function_call_output", "call_id": ..., "output": ...}` ਸ਼ਾਮਲ ਕਰੋ — `{"role": "tool", "tool_call_id": ..., "content": ...}` ਨਹੀਂ। ਸਹਾਇਕ ਦੀ ਟੂਲ ਬੇਨਤੀ ਲਈ, `messages.extend(response.output)` ਵਰਤੋਂ — ਮੈਨੁਅਲ `{"role": "assistant", "tool_calls": [...]}` ਡਿਕਸ਼ਨਰੀ ਨਹੀਂ।
21. **`strict: true` ਲਈ `required` + `additionalProperties: false` ਲਾਜ਼ਮੀ ਹੈ**: ਜਦੋਂ ਟੂਲ 'ਤੇ `strict: true` ਵਰਤਦੇ ਹੋ, ਹਰ ਗੁਣ `required` ਸੂਚੀ ਵਿੱਚ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ `additionalProperties` `false` ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਕਿਸੇ ਵੀਦੀ ਗ਼ੈਰ ਮੌਜੂਦਗੀ 400 ਐਰਰ ਪੈਦਾ ਕਰਦੀ ਹੈ।
22. **ਫੰਕਸ਼ਨ ਕਾਲ ID ਲਈ ਵਿਸ਼ੇਸ਼ ਪ੍ਰੀਫਿਕਸ ਹੁੰਦੇ ਹਨ**: ਜਦੋਂ `input` ਵਿੱਚ ਕੁਝ-ਚੋਟਾ `function_call` ਆਈਟਮ ਦਿੱਤੇ ਜਾਂਦੇ ਹਨ, ਤਾਂ `id` ਫੀਲਡ `fc_` ਨਾਲ ਸ਼ੁਰੂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ `call_id` ਫੀਲਡ `call_` ਨਾਲ (ਜਿਵੇਂ `"id": "fc_example1", "call_id": "call_example1"`). ਪਹਿਲਾਂ ਵਾਲਾ ਚੈਟ ਕંપਲੀਸ਼ਨਜ਼ `call_` ਪ੍ਰੀਫਿਕਸ `id` ਲਈ ਮਨਜ਼ੂਰ ਨਹੀਂ ਕੀਤਾ ਜਾਂਦਾ।
23. **GitHub ਮਾਡਲਜ਼ Responses API ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦੇ**: ਜੇ ਐਪ ਵਿੱਚ GitHub ਮਾਡਲਜ਼ ਕੋਡ ਪਾਥ (`base_url` ਜੋ `models.github.ai` ਜਾਂ `models.inference.ai.azure.com` ਵੱਲ ਇਸ਼ਾਰਾ ਕਰਦਾ ਹੈ) ਹੈ, ਤਾਂ ਇਸ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਹਟਾ ਦਿਓ। ਮਾਈਗ੍ਰੇਸ਼ਨ ਦਾ ਕੋਈ ਰਸਤਾ ਨਹੀਂ ਹੈ — Azure OpenAI, OpenAI ਜਾਂ ਅਨੁਕੂਲ ਲੋਕਲ ਏਂਡਪੌਇੰਟ 'ਤੇ ਸਵਿੱਚ ਕਰੋ।
24. **ਕੰਟੈਂਟ ਫਿਲਟਰ ਐਰਰ ਬਾਡੀ ਦੀ ਬਣਤਰ ਬਦਲ ਗਈ ਹੈ**: ਚੈਟ ਕંપਲੀਸ਼ਨਜ਼ ਦੇ ਐਰਰਾਂ ਵਿੱਚ `error.body["innererror"]["content_filter_result"]` (ਇੱਕਵਚਨ) ਹੁੰਦਾ ਸੀ। Responses API ਦੇ ਐਰਰਾਂ ਵਿੱਚ `error.body["content_filters"][0]["content_filter_results"]` (ਬਹੁਵਚਨ, ਇੱਕ ਐਰੇ ਵਿੱਚ) ਹੁੰਦਾ ਹੈ। `innererror` ਕੀ ਹੁਣ ਨਹੀਂ ਰਹੀ। ਜੋ ਕੋਡ ਸਿੱਧਾ `innererror` ਨੂੰ ਐਕਸੈਸ ਕਰਦਾ ਹੈ ਉਹ ਰਨਟਾਈਮ 'ਤੇ `KeyError` ਦਿੰਦਾ ਹੈ — ਇਹ ਮਾਈਗ੍ਰੇਸ਼ਨ ਵਿੱਚ ਆਸਾਨੀ ਨਾਲ ਨਾ ਧਿਆਨ ਦਿੱਤਾ ਜਾਣ ਵਾਲਾ ਮਾਮਲਾ ਹੈ ਕਿਉਂਕਿ ਇਹ ਤਦ ਹੀ ਨਜ਼ਰ ਆਉਂਦਾ ਹੈ ਜਦੋਂ ਕੰਟੈਂਟ ਫਿਲਟਰ ਸੱਚਮੁੱਚ ਟ੍ਰਿਗਰ ਹੁੰਦਾ ਹੈ। ਹਮੇਸ਼ਾ ਮਾਈਗ੍ਰੇਸ਼ਨ ਦੌਰਾਨ `innererror` ਲਈ ਗ੍ਰੈਪ ਕਰੋ।
25. **ਕੱਚੇ HTTP ਕਾਲਾਂ ਲਈ URL + ਬਾਡੀ ਦੁਬਾਰਾ ਲਿਖਾਈ ਲੋੜੀਂਦੀ ਹੈ**: ਜੇ ਐਪ Azure OpenAI REST ਨੂੰ ਸਿੱਧਾ (ਜਿਵੇਂ `requests`, `httpx`, `aiohttp` ਰਾਹੀਂ) `/openai/deployments/{name}/chat/completions?api-version=...` ਤੇ ਕਾਲ ਕਰ ਰਹੀ ਹੈ, ਤਾਂ ਇਸਨੂੰ `/openai/v1/responses` ਨਾਲ ਬਦਲੋ। ਰਿਕੁਏਸਟ ਬਾਡੀ ਵਿੱਚ `messages` ਦੀ ਬਜਾਏ `input` ਵਰਤੋ, `max_output_tokens` ਅਤੇ `store` ਲੋੜੀਂਦੇ ਹਨ, ਅਤੇ `api-version` ਕੁਏਰੀ ਪੈਰਾਮ ਹਟਾ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ। ਰਿਸਪਾਂਸ ਬਾਡੀ ਦਾ ਟੈਕਸਟ `output[0].content[0].text` 'ਤੇ ਹੁੰਦਾ ਹੈ — **ਨਹੀਂ** `output_text`, ਜੋ ਕਿ ਇੱਕ SDK ਸੁਵਿਧਾ ਗੁਣ ਹੈ ਜੋ ਕੱਚੇ REST JSON ਵਿੱਚ ਮੌਜੂਦ ਨਹੀਂ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->