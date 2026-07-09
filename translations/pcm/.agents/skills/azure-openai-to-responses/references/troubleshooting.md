# Troubleshooting, Risk Table & Gotchas

## Troubleshooting 400s

| Error | Fix |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Tool definition dey use old Chat Completions nested format | Flatten from `{"type": "function", "function": {"name": ...}}` to `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters go for top level |
| `unknown_parameter: input[N].tool_calls` | Multi-turn tool results dey use old Chat Completions format | Replace `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` wit `response.output` items + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` tool no get `required` array | When `strict: true`, all properties must dey listed for `required` and `additionalProperties: false` must dey set |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` tool no get `additionalProperties: false` | Add `"additionalProperties": false` for the parameters object |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID get wrong prefix | Function call IDs must start wit `fc_` (e.g., `fc_example1`), no be `call_` |
| `missing_required_parameter: text.format.name` | Add `"name"` key for the format dict (e.g., `"name": "Output"`) |
| `invalid_type: text.format` | Make sure sey `text.format` be dict wit `type`, `name`, `strict`, `schema` keys — no be string |
| `invalid input content type` | Use `input_text`/`output_text` content types instead of Chat `text` |
| `invalid input content type` (image) | Image content still dey use `"type": "image_url"` | Change am to `"type": "input_image"` |
| `Expected object, got string` on `image_url` | `image_url` still be nested object `{"url": "..."}` | Flatten am to plain string: `"image_url": "https://..."` or `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Minimum na **16** for Azure OpenAI. Use 50+ for tests, 1000+ for production. |
| `429 Too Many Requests` during streaming | Dem limit your rate. Wrap streaming inside `try/except`, yield error JSON go frontend, do backoff/retry. |
| `KeyError: 'innererror'` on content filter error | Content filter error body structure change inside Responses API | Chat Completions use `error.body["innererror"]["content_filter_result"]`; Responses API dey use `error.body["content_filters"][0]["content_filter_results"]` (plural, inside array). Rewrite all `innererror` access. |

---

## Migration Risk Table

| Symptom | Likely Mistake | Fix |
|---------|---------------|-----|
| Empty `output_text` / truncated response | `max_output_tokens` too low for reasoning models | Set `max_output_tokens=1000` or higher — reasoning tokens dey count against the limit |
| `400 invalid_type: text.format` | You pass `response_format` string instead of `text.format` dict | Use `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` on `/openai/v1/responses` | Wrong `base_url` — `/openai/v1/` suffix dey miss | Make sure `base_url=f"{endpoint}/openai/v1/"` (with trailing slash) dey |
| `401 Unauthorized` after you switch to `OpenAI()` | `api_key` no set or token provider no pass correctly | For EntraID: `api_key=token_provider` (the callable). For API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model dey return `deployment not found` | `model` param no match your Azure deployment name | Use `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — na the deployment name, no be model name |
| `json.loads(resp.output_text)` dey raise `JSONDecodeError` | Schema no dey enforced or model no support strict JSON | Make sure `"strict": True` dey inside schema, and check sey model support structured output |
| Streaming no dey give any `delta` events | You dey check wrong event type | Filter on `event.type == "response.output_text.delta"`, no be Chat's `chat.completion.chunk` |
| `400` error on image input after migration | Image content type not update | Change `"type": "image_url"` → `"type": "input_image"` and flatten `"image_url": {"url": "..."}` → `"image_url": "..."` (plain string) |
| Tool calls dey loop forever | Missing tool result for follow-up `input` | After you use tool, append `{"type": "function_call_output", "call_id": ..., "output": ...}` item for next request `input` |
| `temperature` error wit GPT-5 or o-series | Explicit `temperature` value wey no be 1 | Remove `temperature` or set am to `1` for GPT-5 and o-series models (o1, o3-mini, o3, o4-mini) |
| `top_p` error wit o-series | `top_p` no dey supported | Remove `top_p` if you dey target o-series models |
| `max_completion_tokens` no dey recognized | You dey use Azure-specific parameter | Replace `max_completion_tokens` with `max_output_tokens`. Set am to 4096+ for o-series (reasoning tokens dey count against the limit). |
| Empty/truncated output from o-series | `max_output_tokens` too low | O-series dey use reasoning tokens inside. Set `max_output_tokens=4096` or higher — no be 500–1000. |
| `400 integer_below_min_value` for `max_output_tokens` | Value lower than 16 | Azure OpenAI dey enforce `max_output_tokens >= 16`. Use 50+ for smoke tests, 1000+ for production. |
| `429 Too Many Requests` mid-stream | Azure OpenAI rate limit | Stream break silent without error handling. Always wrap `async for event in await coroutine:` inside `try/except` and yield `{"error": str(e)}` go frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Wrong tenant or you never log in | Pass `tenant_id=os.getenv("AZURE_TENANT_ID")` explicitly. Run `azd auth login --tenant <tenant-id>` locally. |
| `404 Not Found` while you dey use GitHub Models (`models.github.ai`) | GitHub Models no dey support Responses API | Remove GitHub Models code path complete. Use Azure OpenAI, OpenAI, or compatible local endpoint (e.g., Ollama wit Responses support). |
| MAF `OpenAIChatCompletionClient` still dey use Chat Completions | Using legacy MAF client inside 1.0.0+ | For MAF 1.0.0+, `OpenAIChatClient` dey use Responses API by default. Replace `OpenAIChatCompletionClient` wit `OpenAIChatClient`. For pre-1.0.0, upgrade to `agent-framework-openai>=1.0.0`. |
| LangChain agent dey return empty or e dey fail wit tool calls | `ChatOpenAI` no dey use Responses API | Add `use_responses_api=True` to `ChatOpenAI(...)`. Also change `.content` → `.text` for response messages. |
| `KeyError: 'innererror'` for content filter error handler | Error body structure change in Responses API | Rewrite `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. The `innererror` wrapper no dey again; content filter details dey for top-level `content_filters` array wit `content_filter_results` (plural) inside every entry. |
| Raw HTTP call to `/openai/deployments/.../chat/completions` dey return 404 | Old Chat Completions REST endpoint | Rewrite URL to `/openai/v1/responses`. Change request body: `messages` → `input`, add `max_output_tokens` + `store: false`, remove `api-version` query param. Change response parsing: `choices[0].message.content` → `output[0].content[0].text` (note: `output_text` na SDK convenience property, no dey the raw REST JSON). |

---

## Gotchas

1. If before now you dey use Chat Completions for conversation state, make you manage your own state sharply wit Responses.
2. Prefer `max_output_tokens` pass old `max_tokens`.
3. When you dey migrate to `gpt-5`, make sure sey `temperature` no set or e set to `1`.
4. Change Chat `content[].type: "text"` to Responses `content[].type: "input_text"` for user/system inputs.
5. For `text.format`, give correct dict (e.g., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), no be plain string.
6. `seed` parameter no dey supported for Responses; remove am from requests.
7. **Reasoning**: Only include `reasoning` if di original code don already use am. No add `reasoning` for API calls wey never get am — plenty models (e.g., gpt-4o-mini) no support this parameter.
8. **`max_output_tokens` sizing**: For reasoning models (GPT-5-mini, GPT-5, o-series), use `max_output_tokens=4096` or higher — no be 50–1000. The model dey use reasoning tokens inside before e generate visible output; low limit fit cause truncated or empty responses.
9. **O-series `max_completion_tokens`**: If di original code dey use `max_completion_tokens` (Azure-specific for o-series), change am to `max_output_tokens`. The Responses API no accept `max_completion_tokens`.
10. **O-series `reasoning_effort`**: If the original code dey use `reasoning_effort` (low/medium/high), migrate am to `reasoning={"effort": "<value>"}` inside the Responses API call.
11. **O-series streaming delay**: O-series models dey do internal reasoning before e start output. When streaming, expect say delay go longer before the first `response.output_text.delta` event. Na normal thing — model dey reason, no be say e hang.
9. **`_azure_ad_token_provider` no dey again**: `AsyncOpenAI` / `OpenAI` no get `_azure_ad_token_provider` attribute. Tests or code wey dey access this attribute go fail wit `AttributeError`. The token provider na `api_key` you pass; you no fit inspect am for client object.
10. **Snapshot / golden files**: If your test suite dey use snapshot testing, **all** snapshot files wey get Chat Completions streaming shapes (`choices[0]`, `content_filter_results`, `function_call`, etc.) must update to the new Responses shape. E easy to miss and e fit cause snapshot assertion failure.
11. **Mock monkeypatch path**: The monkeypatch target change from `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (or `Responses.create` for sync). If you use old path, e no go do anything silently — the mock no go intercept, and tests go hit real API or fail.
12. **`input` no be `messages`**: Mock functions must read `kwargs.get("input")` no be `kwargs.get("messages")`. The Responses API dey use `input` for conversation history.
13. **Env var naming**: Azure Identity SDK dey use `AZURE_CLIENT_ID` (no be `AZURE_OPENAI_CLIENT_ID`) for `ManagedIdentityCredential(client_id=...)`. Rename am for tests, `.env` files, app settings, and Bicep/infra.
14. **`max_output_tokens` minimum na 16**: Azure OpenAI no go accept values under 16 wit `400 integer_below_min_value`. Use `50` for smoke tests, `1000`+ for production. Old `max_tokens` no get minimum like this.
15. **`tenant_id` for `AzureDeveloperCliCredential`**: When Azure OpenAI resource dey different tenant, you **must** pass `tenant_id` sharply — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. If you no do am, the credential go silently use wrong tenant and return `401`.
16. **Rate limits dey show different for streaming**: For Chat Completions, 429 fit stop stream from even start. For Responses API streaming, 429 fit happen **mid-stream** — the async iterator go raise exception. Always wrap streaming loop inside `try/except` and yield error JSON line so frontend fit handle am well.

17. **Streaming error handling na must for web apps**: Di pattern `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` dey important. If e no de, di SSE/JSONL stream go quietly die anytime error happen for server-side and frontend go freeze.
18. **Tool definitions must use flat format**: Di Responses API dey expect `{"type": "function", "name": ..., "parameters": ...}` — no be di Chat Completions nested `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Na dis one be di common migration mistake for function-calling code.
19. **`pydantic_function_tool()` no dey compatible**: Di `openai.pydantic_function_tool()` helper still dey generate di old nested format. No use am with `responses.create()`. Define tool schemas yourself or flatten di output.
20. **Tool results dey use `function_call_output`, no be `role: tool`**: After you run the tool, add `{"type": "function_call_output", "call_id": ..., "output": ...}` — no be `{"role": "tool", "tool_call_id": ..., "content": ...}`. For di assistant tool request, use `messages.extend(response.output)` — no be manual `{"role": "assistant", "tool_calls": [...]}` dict.
21. **`strict: true` need `required` + `additionalProperties: false`**: If you use `strict: true` for tool, every property suppose dey inside `required` array and `additionalProperties` must be `false`. If you miss either one, e go cause 400 error.
22. **Function call IDs get specific prefixes**: When you dey provide few-shot `function_call` items for `input`, di `id` field suppose start with `fc_` and di `call_id` field suppose start with `call_` (example: `"id": "fc_example1", "call_id": "call_example1"`). If you use old Chat Completions `call_` prefix for `id`, e no go work.
23. **GitHub Models no support Responses API**: If your app get GitHub Models code path (`base_url` wey point to `models.github.ai` or `models.inference.ai.azure.com`), remove am comot. No migration path dey — switch to Azure OpenAI, OpenAI, or beta compatible local endpoint.
24. **Content filter error body structure don change**: Chat Completions errors dey use `error.body["innererror"]["content_filter_result"]` (singular). Responses API errors dey use `error.body["content_filters"][0]["content_filter_results"]` (plural, inside array). Di `innererror` key no dey again. If your code dey directly access `innererror`, e go raise `KeyError` for runtime — dis one easy to miss if you dey migrate since e go show only if content filter actually trigger. Always check for `innererror` during migration.
25. **Raw HTTP calls need URL + body rewrite**: Apps wey dey call Azure OpenAI REST directly (via `requests`, `httpx`, `aiohttp`) wey dey use `/openai/deployments/{name}/chat/completions?api-version=...` must change to `/openai/v1/responses`. Di request body dey use `input` no be `messages`, e need `max_output_tokens` and `store`, and di `api-version` query param no dey again. Di response body text dey for `output[0].content[0].text` — **no be** `output_text`, wey be SDK convenience property wey no dey for raw REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->