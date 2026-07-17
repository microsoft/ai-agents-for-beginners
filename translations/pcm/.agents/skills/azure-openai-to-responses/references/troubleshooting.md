# Troubleshooting, Risk Table & Gotchas

## Troubleshooting 400s

| Error | Fix |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Tool definition dey use old Chat Completions nested format | Flatten am from `{"type": "function", "function": {"name": ...}}` to `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters go for top level |
| `unknown_parameter: input[N].tool_calls` | Multi-turn tool results dey use old Chat Completions format | Change `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` to `response.output` items + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` tool no get `required` array | When `strict: true`, all properties gats dey for `required` and `additionalProperties: false` must dey set |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` tool no get `additionalProperties: false` | Add `"additionalProperties": false` for inside parameters object |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID get wrong prefix | Function call IDs must start `fc_` (tori: `fc_example1`), no be `call_` |
| `missing_required_parameter: text.format.name` | Add `"name"` key for format dict (e.g., `"name": "Output"`) |
| `invalid_type: text.format` | Make sure `text.format` be dict with `type`, `name`, `strict`, `schema` keys — no be string |
| `invalid input content type` | Use `input_text`/`output_text` content types instead of Chat `text` |
| `invalid input content type` (image) | Image content still dey use `"type": "image_url"` | Change am to `"type": "input_image"` |
| `Expected object, got string` on `image_url` | `image_url` still na nested object `{"url": "..."}` | Flatten am to plain string: `"image_url": "https://..."` or `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Minimum na **16** for Azure OpenAI. Use 50+ for tests, 1000+ for production. |
| `429 Too Many Requests` during streaming | Dem limit your rate. Wrap streaming inside `try/except`, yield error JSON to frontend, do backoff/retry. |
| `KeyError: 'innererror'` on content filter error | Content filter error body structure don change for Responses API | Chat Completions use `error.body["innererror"]["content_filter_result"]`; Responses API dey use `error.body["content_filters"][0]["content_filter_results"]` (plural, inside array). Rewrite all `innererror` access. |

---

## Migration Risk Table

| Symptom | Likely Mistake | Fix |
|---------|---------------|-----|
| Empty `output_text` / truncated response | `max_output_tokens` too low for reasoning models | Set `max_output_tokens=1000` or higher — reasoning tokens dey count against the limit |
| `400 invalid_type: text.format` | You pass `response_format` string instead of `text.format` dict | Use `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` on `/openai/v1/responses` | Wrong `base_url` — `/openai/v1/` suffix dey miss | Make sure `base_url=f"{endpoint}/openai/v1/"` (with trailing slash) dey |
| `401 Unauthorized` after switching to `OpenAI()` | `api_key` no set or token provider no pass well | For EntraID: `api_key=token_provider` (the callable). For API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model returns `deployment not found` | `model` param no match your Azure deployment name | Use `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — na the deployment name, no be model name |
| `json.loads(resp.output_text)` raise `JSONDecodeError` | Schema no enforced or model no support strict JSON | Make sure `"strict": True` dey for schema, plus check model fit support structured output |
| Streaming no yield `delta` events | You dey check wrong event type | Filter on `event.type == "response.output_text.delta"`, no be Chat `chat.completion.chunk` |
| `400` error on image input after migration | Image content type no updated | Change `"type": "image_url"` → `"type": "input_image"` and flatten `"image_url": {"url": "..."}` → `"image_url": "..."` (plain string) |
| Tool calls just dey loop forever | Missing tool result for follow-up `input` | After you run tool, add `{"type": "function_call_output", "call_id": ..., "output": ...}` to top `input` for next request |
| `temperature` error with GPT-5 or o-series | Explicit `temperature` value no be 1 | Remove `temperature` or set am to `1` for GPT-5 and o-series models (o1, o3-mini, o3, o4-mini) |
| `top_p` error with o-series | `top_p` no dey supported | Remove `top_p` when you dey use o-series models |
| `max_completion_tokens` no dey recognized | You dey use Azure-specific parameter | Change `max_completion_tokens` to `max_output_tokens`. Set to 4096+ for o-series (reasoning tokens dey count against the limit). |
| Empty/truncated output from o-series | `max_output_tokens` dey too low | O-series internally dey use reasoning tokens. Set `max_output_tokens=4096` or higher — no be 500–1000. |
| `400 integer_below_min_value` for `max_output_tokens` | Value below 16 | Azure OpenAI gats `max_output_tokens >= 16`. Use 50+ for smoke tests, 1000+ for production. |
| `429 Too Many Requests` mid-stream | Dem limit your rate for Azure OpenAI | Stream break dey silent if error handling no dey. Always wrap `async for event in await coroutine:` inside `try/except` and yield `{"error": str(e)}` to frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Wrong tenant or no login | Pass `tenant_id=os.getenv("AZURE_TENANT_ID")` clearly. Run `azd auth login --tenant <tenant-id>` for your machine. |
| `404 Not Found` using GitHub Models (`models.github.ai`) | GitHub Models no support Responses API | Remove the GitHub Models code path completely. Use Azure OpenAI, OpenAI, or local endpoint wey dey compatible (e.g., Ollama with Responses support). |
| MAF `OpenAIChatCompletionClient` still dey use Chat Completions | Dey use old MAF client for 1.0.0+ | For MAF 1.0.0+, `OpenAIChatClient` go use Responses API by default. Change `OpenAIChatCompletionClient` to `OpenAIChatClient`. For pre-1.0.0, upgrade to `agent-framework-openai>=1.0.0`. |
| LangChain agent return empty or e fail with tool calls | `ChatOpenAI` no dey use Responses API | Add `use_responses_api=True` to `ChatOpenAI(...)`. Also change `.content` → `.text` for response messages. |
| `KeyError: 'innererror'` for content filter error handler | Error body structure change for Responses API | Rewrite `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` wrapper don vanish; content filter info now dey inside a top-level `content_filters` array wey get `content_filter_results` (plural) inside each entry. |
| Raw HTTP call to `/openai/deployments/.../chat/completions` return 404 | Old Chat Completions REST endpoint | Rewrite URL to `/openai/v1/responses`. Change request body: `messages` → `input`, add `max_output_tokens` + `store: false`, remove `api-version` query param. Change response parsing: `choices[0].message.content` → `output[0].content[0].text` (note: `output_text` na SDK convenience property, no dey raw REST JSON). |

---

## Gotchas

1. If you bin dey use Chat Completions for conversation state before, now you gats manage your own state clearly with Responses.
2. Make you prefer `max_output_tokens` instead of old `max_tokens`.
3. When you dey migrate to `gpt-5`, make sure sey you no specify `temperature` or e set to `1`.
4. Replace Chat `content[].type: "text"` with Responses `content[].type: "input_text"` for user/system inputs.
5. For `text.format`, you gats supply correct dict (e.g., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), no be plain string.
6. The `seed` parameter no dey supported for Responses; comot am from requests.
7. **Reasoning**: Only include `reasoning` if the original code bin already dey use am. No add `reasoning` to API calls wey no get am — plenty non-reasoning models no fit handle dis parameter.
8. **`max_output_tokens` sizing**: For reasoning models (GPT-5-mini, GPT-5, o-series), make you set `max_output_tokens=4096` or more — no be 50–1000. The model dey use reasoning tokens inside before e generate visible output; if e low, e fit cause truncated or empty response.
9. **O-series `max_completion_tokens`**: If original code bin dey use `max_completion_tokens` (Azure-specific for o-series), change am to `max_output_tokens`. Responses API no dey accept `max_completion_tokens`.
10. **O-series `reasoning_effort`**: If original code dey use `reasoning_effort` (low/medium/high), migrate am to `reasoning={"effort": "<value>"}` for Responses API call.
11. **O-series streaming delay**: O-series models dey reason inside before dem generate output. For streaming, expect longer delay before first `response.output_text.delta` event. Na normal thing — model just dey reason, e no hang.
9. **`_azure_ad_token_provider` don disappear**: `AsyncOpenAI` / `OpenAI` no get `_azure_ad_token_provider` attribute. Tests or code wey try access am go fail with `AttributeError`. Token provider dey pass as `api_key` and you no fit inspect am for client object.
10. **Snapshot / golden files**: If test suite dey do snapshot testing, **all** snapshot files wey contain Chat Completions streaming shapes (`choices[0]`, `content_filter_results`, `function_call`, etc.) gats update to new Responses shape. Na easy one to miss and e dey cause snapshot assertion failure.
11. **Mock monkeypatch path**: The monkeypatch target don change from `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (or `Responses.create` for sync). If you still use old path, e no go do anything quietly — mock no go intercept, and tests go hit real API or fail.
12. **`input` no be `messages`**: Mock functions must read `kwargs.get("input")` no be `kwargs.get("messages")`. Responses API dey use `input` for conversation history.
13. **Env var naming**: Azure Identity SDK dey use `AZURE_CLIENT_ID` (no be `AZURE_OPENAI_CLIENT_ID`) for `ManagedIdentityCredential(client_id=...)`. Rename am for tests, `.env` files, app settings, and Bicep/infra.
14. **`max_output_tokens` minimum na 16**: Azure OpenAI no go accept values below 16 with `400 integer_below_min_value`. Use `50` for smoke tests, `1000`+ for production. Old `max_tokens` no get such minimum.
15. **`tenant_id` for `AzureDeveloperCliCredential`**: If Azure OpenAI resource dey for different tenant, you **must** pass `tenant_id` clearly — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. If no, credential go quietly dey use wrong tenant and give `401`.
16. **Rate limits dey show differently for streaming**: With Chat Completions, 429 normally no let stream start. With Responses API streaming, 429 fit happen **mid-stream** — async iterator go throw exception. Always wrap streaming loop inside `try/except` and yield error JSON line so frontend fit handle am well.

17. **Streaming error handling na wajib for web apps**: Pattern wey be `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` important. Without am, SSE/JSONL stream go die for silent if any server-side error happen and frontend go freeze.
18. **Tool definitions must use flat format**: Responses API dey expect `{"type": "function", "name": ..., "parameters": ...}` — no be Chat Completions nested `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Na the most common mistake wey dey happen when dem dey migrate function-calling code.
19. **`pydantic_function_tool()` no dey compatible**: The `openai.pydantic_function_tool()` helper still dey generate old nested format. No use am with `responses.create()`. Make you define tool schemas by yourself or make you flatten the output.
20. **Tool results dey use `function_call_output`, no be `role: tool`**: After you run tool, add `{"type": "function_call_output", "call_id": ..., "output": ...}` — no be `{"role": "tool", "tool_call_id": ..., "content": ...}`. For assistant tool request, use `messages.extend(response.output)` — no use manual `{"role": "assistant", "tool_calls": [...]}` dict.
21. **`strict: true` need `required` + `additionalProperties: false`**: If you dey use `strict: true` for tool, every property suppose dey for `required` array and `additionalProperties` must be `false`. If you miss any of dem, e go cause 400 error.
22. **Function call IDs get special prefixes**: If you dey provide few-shot `function_call` items for `input`, the `id` field must start with `fc_` and `call_id` field must start with `call_` (e.g., `"id": "fc_example1", "call_id": "call_example1"`). If you use old Chat Completions `call_` prefix for `id`, e no go work.
23. **GitHub Models no dey support Responses API**: If your app get GitHub Models code path (`base_url` wey point `models.github.ai` or `models.inference.ai.azure.com`), make you remove am complete. No migration path dey — switch to Azure OpenAI, OpenAI, or local endpoint wey fit work.
24. **Content filter error body structure don change**: Chat Completions error use `error.body["innererror"]["content_filter_result"]` (singular). Responses API error dem use `error.body["content_filters"][0]["content_filter_results"]` (plural, inside array). The `innererror` key no exist again. Code wey dey access `innererror` direct go raise `KeyError` for runtime — e easy to miss am for migration because e go show only when content filter really trigger. Always search for `innererror` during migration.
25. **Raw HTTP calls need URL + body rewrite**: Apps wey dey call Azure OpenAI REST direct (via `requests`, `httpx`, `aiohttp`) using `/openai/deployments/{name}/chat/completions?api-version=...` must change to `/openai/v1/responses`. For request body, use `input` instead of `messages`, add `max_output_tokens` and `store`, and drop the `api-version` query param. Response body text dey for `output[0].content[0].text` — **no be** `output_text`, wey na SDK convenience property wey no dey for raw REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->