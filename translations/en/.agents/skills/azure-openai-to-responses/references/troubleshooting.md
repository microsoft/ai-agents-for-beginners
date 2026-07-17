# Troubleshooting, Risk Table & Gotchas

## Troubleshooting 400s

| Error | Fix |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Tool definition uses old Chat Completions nested format | Flatten from `{"type": "function", "function": {"name": ...}}` to `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters go at the top level |
| `unknown_parameter: input[N].tool_calls` | Multi-turn tool results use old Chat Completions format | Replace `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` with `response.output` items + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` tool missing `required` array | When `strict: true`, all properties must be listed in `required` and `additionalProperties: false` must be set |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` tool missing `additionalProperties: false` | Add `"additionalProperties": false` to the parameters object |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID has wrong prefix | Function call IDs must start with `fc_` (e.g., `fc_example1`), not `call_` |
| `missing_required_parameter: text.format.name` | Add `"name"` key to the format dict (e.g., `"name": "Output"`) |
| `invalid_type: text.format` | Ensure `text.format` is a dict with `type`, `name`, `strict`, `schema` keys — not a string |
| `invalid input content type` | Use `input_text`/`output_text` content types instead of Chat `text` |
| `invalid input content type` (image) | Image content still uses `"type": "image_url"` | Change to `"type": "input_image"` |
| `Expected object, got string` on `image_url` | `image_url` is still a nested object `{"url": "..."}` | Flatten to a plain string: `"image_url": "https://..."` or `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Minimum is **16** on Azure OpenAI. Use 50+ for tests, 1000+ for production. |
| `429 Too Many Requests` during streaming | Rate limited. Wrap streaming in `try/except`, yield error JSON to frontend, implement backoff/retry. |
| `KeyError: 'innererror'` on content filter error | Content filter error body structure changed in Responses API | Chat Completions used `error.body["innererror"]["content_filter_result"]`; Responses API uses `error.body["content_filters"][0]["content_filter_results"]` (plural, inside an array). Rewrite all `innererror` access. |

---

## Migration Risk Table

| Symptom | Likely Mistake | Fix |
|---------|---------------|-----|
| Empty `output_text` / truncated response | `max_output_tokens` too low for reasoning models | Set `max_output_tokens=1000` or higher — reasoning tokens count against the limit |
| `400 invalid_type: text.format` | Passed `response_format` string instead of `text.format` dict | Use `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` on `/openai/v1/responses` | Wrong `base_url` — missing `/openai/v1/` suffix | Ensure `base_url=f"{endpoint}/openai/v1/"` (with trailing slash) |
| `401 Unauthorized` after switching to `OpenAI()` | `api_key` not set or token provider not passed correctly | For EntraID: `api_key=token_provider` (the callable). For API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model returns `deployment not found` | `model` param doesn't match your Azure deployment name | Use `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — this is the deployment name, not the model name |
| `json.loads(resp.output_text)` raises `JSONDecodeError` | Schema not enforced or model doesn't support strict JSON | Ensure `"strict": True` in schema, and verify model supports structured output |
| Streaming yields no `delta` events | Checking wrong event type | Filter on `event.type == "response.output_text.delta"`, not Chat's `chat.completion.chunk` |
| `400` error on image input after migration | Image content type not updated | Change `"type": "image_url"` → `"type": "input_image"` and flatten `"image_url": {"url": "..."}` → `"image_url": "..."` (plain string) |
| Tool calls loop infinitely | Missing tool result in follow-up `input` | After executing a tool, append a `{"type": "function_call_output", "call_id": ..., "output": ...}` item to `input` in the next request |
| `temperature` error with GPT-5 or o-series | Explicit `temperature` value other than 1 | Remove `temperature` or set to `1` for GPT-5 and o-series models (o1, o3-mini, o3, o4-mini) |
| `top_p` error with o-series | `top_p` not supported | Remove `top_p` when targeting o-series models |
| `max_completion_tokens` not recognized | Using Azure-specific parameter | Replace `max_completion_tokens` with `max_output_tokens`. Set to 4096+ for o-series (reasoning tokens count against the limit). |
| Empty/truncated output from o-series | `max_output_tokens` too low | O-series uses reasoning tokens internally. Set `max_output_tokens=4096` or higher — not 500–1000. |
| `400 integer_below_min_value` for `max_output_tokens` | Value below 16 | Azure OpenAI enforces `max_output_tokens >= 16`. Use 50+ for smoke tests, 1000+ for production. |
| `429 Too Many Requests` mid-stream | Rate limited by Azure OpenAI | Stream breaks silently without error handling. Always wrap `async for event in await coroutine:` in `try/except` and yield `{"error": str(e)}` to the frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Wrong tenant or not logged in | Pass `tenant_id=os.getenv("AZURE_TENANT_ID")` explicitly. Run `azd auth login --tenant <tenant-id>` locally. |
| `404 Not Found` using GitHub Models (`models.github.ai`) | GitHub Models does not support Responses API | Remove the GitHub Models code path entirely. Use Azure OpenAI, OpenAI, or a compatible local endpoint (e.g., Ollama with Responses support). |
| MAF `OpenAIChatCompletionClient` still using Chat Completions | Using legacy MAF client in 1.0.0+ | In MAF 1.0.0+, `OpenAIChatClient` uses Responses API by default. Replace `OpenAIChatCompletionClient` with `OpenAIChatClient`. For pre-1.0.0, upgrade to `agent-framework-openai>=1.0.0`. |
| LangChain agent returns empty or fails with tool calls | `ChatOpenAI` not using Responses API | Add `use_responses_api=True` to `ChatOpenAI(...)`. Also change `.content` → `.text` on response messages. |
| `KeyError: 'innererror'` in content filter error handler | Error body structure changed in Responses API | Rewrite `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. The `innererror` wrapper is gone; content filter details are now in a top-level `content_filters` array with `content_filter_results` (plural) inside each entry. |
| Raw HTTP call to `/openai/deployments/.../chat/completions` returns 404 | Old Chat Completions REST endpoint | Rewrite URL to `/openai/v1/responses`. Change request body: `messages` → `input`, add `max_output_tokens` + `store: false`, remove `api-version` query param. Change response parsing: `choices[0].message.content` → `output[0].content[0].text` (note: `output_text` is an SDK convenience property, not in the raw REST JSON). |

---

## Gotchas

1. If you previously used Chat Completions for conversation state, manage your own state explicitly with Responses.
2. Prefer `max_output_tokens` over legacy `max_tokens`.
3. When migrating to `gpt-5`, ensure `temperature` is not specified or is set to `1`.
4. Replace Chat `content[].type: "text"` with Responses `content[].type: "input_text"` for user/system inputs.
5. For `text.format`, supply a proper dict (e.g., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), not a plain string.
6. The `seed` parameter is not supported in Responses; remove it from requests.
7. **Reasoning**: Only include `reasoning` if the original code already used it. Do not add `reasoning` to API calls that didn't have it — many non-reasoning models don't support this parameter.
8. **`max_output_tokens` sizing**: For reasoning models (GPT-5-mini, GPT-5, o-series), use `max_output_tokens=4096` or higher — not 50–1000. The model uses reasoning tokens internally before generating visible output; too-low limits cause truncated or empty responses.
9. **O-series `max_completion_tokens`**: If the original code used `max_completion_tokens` (Azure-specific for o-series), replace with `max_output_tokens`. The Responses API does not accept `max_completion_tokens`.
10. **O-series `reasoning_effort`**: If the original code uses `reasoning_effort` (low/medium/high), migrate it to `reasoning={"effort": "<value>"}` in the Responses API call.
11. **O-series streaming delay**: O-series models perform internal reasoning before generating output. When streaming, expect a longer delay before the first `response.output_text.delta` event. This is normal — the model is reasoning, not hung.
9. **`_azure_ad_token_provider` is gone**: `AsyncOpenAI` / `OpenAI` have no `_azure_ad_token_provider` attribute. Tests or code that access this attribute will fail with `AttributeError`. The token provider is passed as `api_key` and is not inspectable on the client object.
10. **Snapshot / golden files**: If the test suite uses snapshot testing, **all** snapshot files containing Chat Completions streaming shapes (`choices[0]`, `content_filter_results`, `function_call`, etc.) must be updated to the new Responses shape. This is easy to miss and causes snapshot assertion failures.
11. **Mock monkeypatch path**: The monkeypatch target changes from `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (or `Responses.create` for sync). Using the old path silently does nothing — the mock won't intercept, and tests hit the real API or fail.
12. **`input` not `messages`**: Mock functions must read `kwargs.get("input")` not `kwargs.get("messages")`. The Responses API uses `input` for conversation history.
13. **Env var naming**: Azure Identity SDK uses `AZURE_CLIENT_ID` (not `AZURE_OPENAI_CLIENT_ID`) for `ManagedIdentityCredential(client_id=...)`. Rename in tests, `.env` files, app settings, and Bicep/infra.
14. **`max_output_tokens` minimum is 16**: Azure OpenAI rejects values below 16 with `400 integer_below_min_value`. Use `50` for smoke tests, `1000`+ for production. The old `max_tokens` had no such minimum.
15. **`tenant_id` for `AzureDeveloperCliCredential`**: When the Azure OpenAI resource is in a different tenant, you **must** pass `tenant_id` explicitly — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Without it, the credential silently uses the wrong tenant and returns `401`.
16. **Rate limits surface differently in streaming**: With Chat Completions, a 429 typically prevented the stream from starting. With Responses API streaming, a 429 can occur **mid-stream** — the async iterator raises an exception. Always wrap the streaming loop in `try/except` and yield an error JSON line so the frontend can handle it gracefully.

17. **Streaming error handling is mandatory for web apps**: The pattern `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` is critical. Without it, the SSE/JSONL stream silently dies on any server-side error and the frontend hangs.
18. **Tool definitions must use flat format**: The Responses API expects `{"type": "function", "name": ..., "parameters": ...}` — not the Chat Completions nested `{"type": "function", "function": {"name": ..., "parameters": ...}}`. This is the most common migration error for function-calling code.
19. **`pydantic_function_tool()` is incompatible**: The `openai.pydantic_function_tool()` helper still generates the old nested format. Do not use it with `responses.create()`. Define tool schemas manually or flatten the output.
20. **Tool results use `function_call_output`, not `role: tool`**: After executing a tool, append `{"type": "function_call_output", "call_id": ..., "output": ...}` — not `{"role": "tool", "tool_call_id": ..., "content": ...}`. For the assistant's tool request, use `messages.extend(response.output)` — not a manual `{"role": "assistant", "tool_calls": [...]}` dict.
21. **`strict: true` requires `required` + `additionalProperties: false`**: When using `strict: true` on a tool, every property must be listed in the `required` array and `additionalProperties` must be `false`. Missing either causes a 400 error.
22. **Function call IDs have specific prefixes**: When providing few-shot `function_call` items in `input`, the `id` field must start with `fc_` and the `call_id` field must start with `call_` (e.g., `"id": "fc_example1", "call_id": "call_example1"`). Using the old Chat Completions `call_` prefix for `id` is rejected.
23. **GitHub Models does not support Responses API**: If the app has a GitHub Models code path (`base_url` pointing to `models.github.ai` or `models.inference.ai.azure.com`), remove it entirely. There is no migration path — switch to Azure OpenAI, OpenAI, or a compatible local endpoint.
24. **Content filter error body structure changed**: Chat Completions errors used `error.body["innererror"]["content_filter_result"]` (singular). Responses API errors use `error.body["content_filters"][0]["content_filter_results"]` (plural, inside an array). The `innererror` key no longer exists. Code that directly accesses `innererror` will raise `KeyError` at runtime — this is easy to miss in migration since it only surfaces when the content filter actually triggers. Always grep for `innererror` during migration.
25. **Raw HTTP calls need URL + body rewrite**: Apps calling Azure OpenAI REST directly (via `requests`, `httpx`, `aiohttp`) using `/openai/deployments/{name}/chat/completions?api-version=...` must switch to `/openai/v1/responses`. The request body uses `input` instead of `messages`, requires `max_output_tokens` and `store`, and the `api-version` query param is dropped. The response body text is at `output[0].content[0].text` — **not** `output_text`, which is an SDK convenience property not present in the raw REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->