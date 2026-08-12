# Pag-troubleshoot, Talaan ng Panganib at Mga Paalala

## Pag-troubleshoot ng 400s

| Error | Solusyon |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Ang depinisyon ng tool ay gumagamit ng lumang pagkaka-nest ng Chat Completions | I-flatten mula sa `{"type": "function", "function": {"name": ...}}` papuntang `{"type": "function", "name": ..., "parameters": ...}` — ang name, description, parameters ay ilalagay sa pinakamataas na lebel |
| `unknown_parameter: input[N].tool_calls` | Ang resulta ng multi-turn tool ay gumagamit ng lumang format ng Chat Completions | Palitan ang `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` ng `response.output` items + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` tool ay walang `required` array | Kapag `strict: true`, lahat ng properties ay kailangang nakalista sa `required` at dapat itakda ang `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` tool ay walang `additionalProperties: false` | Idagdag ang `"additionalProperties": false` sa parameters object |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Mali ang prefix ng few-shot function_call ID | Ang function call IDs ay dapat magsimula sa `fc_` (hal., `fc_example1`), hindi `call_` |
| `missing_required_parameter: text.format.name` | Idagdag ang key na `"name"` sa format dict (hal., `"name": "Output"`) |
| `invalid_type: text.format` | Siguraduhin na ang `text.format` ay isang dict na may mga key na `type`, `name`, `strict`, `schema` — hindi isang string |
| `invalid input content type` | Gamitin ang `input_text`/`output_text` na content types imbes na Chat `text` |
| `invalid input content type` (image) | Ang image content ay gumagamit pa rin ng `"type": "image_url"` | Palitan sa `"type": "input_image"` |
| `Expected object, got string` sa `image_url` | Ang `image_url` ay isang nested object pa rin na `{"url": "..."}` | I-flatten sa simpleng string: `"image_url": "https://..."` o `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` para sa `max_output_tokens` | Ang minimum ay **16** sa Azure OpenAI. Gumamit ng 50+ para sa mga pagsubok, 1000+ para sa produksyon. |
| `429 Too Many Requests` habang nag-streaming | Na-rate limit. I-wrap ang streaming sa `try/except`, i-yield ang error JSON sa frontend, ipatupad ang backoff/retry. |
| `KeyError: 'innererror'` sa content filter error | Nagbago ang istruktura ng error body sa Responses API | Ginamit ng Chat Completions ang `error.body["innererror"]["content_filter_result"]`; ginagamit ng Responses API ang `error.body["content_filters"][0]["content_filter_results"]` (plural, sa loob ng array). Isulat muli lahat ng `innererror` access. |

---

## Talaan ng Panganib sa Migration

| Sintomas | Posibleng Mali | Solusyon |
|---------|---------------|-----|
| Walang laman o may putol na tugon sa `output_text` | Masyadong mababa ang `max_output_tokens` para sa reasoning models | Itakda ang `max_output_tokens=1000` o mas mataas — ang reasoning tokens ay bibilangin sa limitasyon |
| `400 invalid_type: text.format` | Pinalampas ang `response_format` bilang string sa halip na dict na `text.format` | Gamitin ang `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` sa `/openai/v1/responses` | Mali ang `base_url` — kulang ang suffix na `/openai/v1/` | Siguraduhin na `base_url=f"{endpoint}/openai/v1/"` (naka-trailing slash) |
| `401 Unauthorized` pagkatapos lumipat sa `OpenAI()` | Hindi naitakda ang `api_key` o hindi tamang ipinasa ang token provider | Para sa EntraID: `api_key=token_provider` (ang callable). Para sa API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Nagbabalik ang model ng `deployment not found` | Hindi tumutugma ang `model` param sa pangalan ng Azure deployment | Gamitin ang `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — ito ang pangalan ng deployment, hindi pangalan ng model |
| Nag-raise ang `json.loads(resp.output_text)` ng `JSONDecodeError` | Hindi naipinatupad ang schema o hindi sinusuportahan ng model ang strict JSON | Siguraduhin na `"strict": True` sa schema, at i-verify na sinusuportahan ng model ang structured output |
| Walang `delta` events na lumalabas sa streaming | Tiningnan ang maling uri ng event | Salain sa `event.type == "response.output_text.delta"`, hindi ang Chat na `chat.completion.chunk` |
| `400` error sa image input pagkatapos ng migration | Hindi na-update ang image content type | Palitan ang `"type": "image_url"` → `"type": "input_image"` at i-flatten ang `"image_url": {"url": "..."}` → `"image_url": "..."` (simpleng string) |
| Infinite loop sa tool calls | Nawawala ang tool result sa follow-up na `input` | Pagkatapos gamitin ang isang tool, idagdag ang `{"type": "function_call_output", "call_id": ..., "output": ...}` na item sa `input` sa susunod na request |
| `temperature` error sa GPT-5 o o-series | May nakalatag na value ng `temperature` maliban sa 1 | Alisin ang `temperature` o itakda ito sa `1` para sa GPT-5 at o-series models (o1, o3-mini, o3, o4-mini) |
| `top_p` error sa o-series | Hindi sinusuportahan ang `top_p` | Alisin ang `top_p` kapag target ang o-series models |
| Hindi kinikilala ang `max_completion_tokens` | Gumagamit ng Azure-specific na parameter | Palitan ang `max_completion_tokens` ng `max_output_tokens`. Itakda sa 4096+ para sa o-series (binibilang ng reasoning tokens ang limitasyon). |
| Walang laman o putol na output mula sa o-series | Masyadong mababa ang `max_output_tokens` | Ginagamit ng o-series ang reasoning tokens nang internal. Itakda ang `max_output_tokens=4096` o mas mataas — hindi 500–1000. |
| `400 integer_below_min_value` para sa `max_output_tokens` | Value na mas mababa sa 16 | Pinipilit ng Azure OpenAI na `max_output_tokens >= 16`. Gumamit ng 50+ para sa smoke tests, 1000+ para sa produksyon. |
| `429 Too Many Requests` habang nasa kalagitnaan ng streaming | Na-rate limit ng Azure OpenAI | Ang streaming ay pasaktang nang walang error handling. Laging i-wrap ang `async for event in await coroutine:` sa `try/except` at mag-yield ng `{"error": str(e)}` sa frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Mali ang tenant o hindi naka-login | Ipasang `tenant_id=os.getenv("AZURE_TENANT_ID")` nang tahasan. Patakbuhin ang `azd auth login --tenant <tenant-id>` nang lokal. |
| `404 Not Found` gamit ang GitHub Models (`models.github.ai`) | Hindi sinusuportahan ng GitHub Models ang Responses API | Alisin ang GitHub Models code path nang buo. Gamitin ang Azure OpenAI, OpenAI, o isang compatible na local endpoint (hal., Ollama na may suporta sa Responses). |
| MAF `OpenAIChatCompletionClient` pa rin ang gamit ang Chat Completions | Gumagamit ng legacy MAF client sa 1.0.0+ | Sa MAF 1.0.0+, ang `OpenAIChatClient` ay awtomatikong gamit ang Responses API. Palitan ang `OpenAIChatCompletionClient` ng `OpenAIChatClient`. Para sa pre-1.0.0, i-upgrade sa `agent-framework-openai>=1.0.0`. |
| LangChain agent ay walang laman o pumapalya sa tool calls | Hindi gumagamit ng Responses API ang `ChatOpenAI` | Idagdag ang `use_responses_api=True` sa `ChatOpenAI(...)`. Palitan din ang `.content` → `.text` sa mga response messages. |
| `KeyError: 'innererror'` sa content filter error handler | Nagbago ang istruktura ng error body sa Responses API | Isulat muli ang `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Wala na ang `innererror` wrapper; ang mga detalye ng content filter ay nasa top-level na `content_filters` array na may `content_filter_results` (plural) sa loob bawat entry. |
| Raw HTTP call sa `/openai/deployments/.../chat/completions` ay nagbabalik ng 404 | Lumang Chat Completions REST endpoint | Palitan ang URL sa `/openai/v1/responses`. Palitan ang request body: `messages` → `input`, idagdag ang `max_output_tokens` + `store: false`, alisin ang query param na `api-version`. Palitan ang response parsing: `choices[0].message.content` → `output[0].content[0].text` (paalala: ang `output_text` ay isang property ng SDK para sa convenience, wala ito sa raw REST JSON). |

---

## Mga Paalala

1. Kung dati kang gumamit ng Chat Completions para sa estado ng pag-uusap, pamahalaan ang sariling estado nang tahasan gamit ang Responses.
2. Mas piliin ang `max_output_tokens` kaysa lumang `max_tokens`.
3. Kapag nag-migrate sa `gpt-5`, siguraduhing hindi nakasaad ang `temperature` o ito ay nakaset sa `1`.
4. Palitan ang Chat na `content[].type: "text"` ng Responses na `content[].type: "input_text"` para sa mga user/system inputs.
5. Para sa `text.format`, magbigay ng wastong dict (hal., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), hindi isang plain na string.
6. Hindi sinusuportahan ang `seed` parameter sa Responses; alisin ito mula sa mga request.
7. **Reasoning**: Isama lamang ang `reasoning` kung ginamit na ito sa orihinal na code. Huwag magdagdag ng `reasoning` sa mga API call na hindi ito ginamit — maraming non-reasoning models ang hindi sumusuporta sa parameter na ito.
8. **Sukat ng `max_output_tokens`**: Para sa mga reasoning models (GPT-5-mini, GPT-5, o-series), gamitin ang `max_output_tokens=4096` o mas mataas — hindi 50–1000. Ang model ay gumagamit ng reasoning tokens nang internal bago gumawa ng nakikitang output; ang sobrang baba na limitasyon ay nagdudulot ng putol o walang sagot.
9. **`max_completion_tokens` ng O-series**: Kung gamit sa orihinal na code ang `max_completion_tokens` (Azure-specific para sa o-series), palitan ito ng `max_output_tokens`. Hindi tinatanggap ng Responses API ang `max_completion_tokens`.
10. **`reasoning_effort` ng O-series**: Kung ginamit sa orihinal na code ang `reasoning_effort` (low/medium/high), ilipat ito sa `reasoning={"effort": "<value>"}` sa mga tawag sa Responses API.
11. **Streaming delay ng O-series**: Ang mga o-series models ay nagsasagawa ng internal na reasoning bago gumawa ng output. Kapag nag-streaming, asahan ang mas matagal na delay bago ang unang `response.output_text.delta` event. Normal ito — nagkakaroon lang ng reasoning ang model, hindi ito nagka-crash.
9. **Wala na ang `_azure_ad_token_provider`**: Ang `AsyncOpenAI` / `OpenAI` ay walang attribute na `_azure_ad_token_provider`. Ang mga tests o code na gumagamit nito ay mabibigo na may `AttributeError`. Ang token provider ay ipinapasa bilang `api_key` at hindi maaaring makita sa client object.
10. **Snapshot / golden files**: Kung gumagamit ang test suite ng snapshot testing, **lahat** ng snapshot files na naglalaman ng Chat Completions streaming shapes (`choices[0]`, `content_filter_results`, `function_call`, atbp.) ay kailangang i-update sa bagong Response shape. Madaling makaligtaan ito at nagdudulot ng snapshot assertion failures.
11. **Mock monkeypatch path**: Nagbago ang monkeypatch target mula sa `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (o `Responses.create` para sa sync). Ang paggamit ng lumang path ay tahimik na walang epekto — hindi makaka-intercept ang mock, at matatamaan ng tests ang totoong API o mabibigo.
12. **`input` hindi `messages`**: Kailangang basahin ng mock functions ang `kwargs.get("input")` hindi `kwargs.get("messages")`. Ginagamit ng Responses API ang `input` para sa conversation history.
13. **Pangalan ng Env var**: Ginagamit ng Azure Identity SDK ang `AZURE_CLIENT_ID` (hindi `AZURE_OPENAI_CLIENT_ID`) para sa `ManagedIdentityCredential(client_id=...)`. Palitan ito sa tests, `.env` files, app settings, at Bicep/infra.
14. **Minimum na `max_output_tokens` ay 16**: Tinanggihan ng Azure OpenAI ang mga value na mas mababa sa 16 na may `400 integer_below_min_value`. Gumamit ng 50 para sa smoke tests, 1000+ para sa produksyon. Ang lumang `max_tokens` ay walang ganitong minimum.
15. **`tenant_id` para sa `AzureDeveloperCliCredential`**: Kapag ang Azure OpenAI resource ay nasa ibang tenant, **kailangang** ipasa nang tahasan ang `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Kung wala ito, tahimik na gagamit ang credential ng maling tenant at magbabalik ng `401`.
16. **Iba ang pagpapakita ng rate limits sa streaming**: Sa Chat Completions, kadalasang pinipigilan ng 429 ang pagsisimula ng stream. Sa Responses API streaming, maaring mangyari ang 429 **habang nag-stream** — magtataas ang async iterator ng exception. Laging i-wrap ang streaming loop sa `try/except` at mag-yield ng error JSON line para maayos itong mapamahalaan ng frontend.

17. **Mandatory ang paghawak ng error sa streaming para sa web apps**: Ang pattern na `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` ay kritikal. Kung wala ito, tahimik na hihinto ang SSE/JSONL stream sa anumang error sa server-side at magha-hang ang frontend.
18. **Dapat flat format ang tool definitions**: Ang Responses API ay inaasahan ang `{"type": "function", "name": ..., "parameters": ...}` — hindi ang Chat Completions na nested na `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Ito ang pinaka-karaniwang error sa pag-migrate para sa code na tumatawag ng function.
19. **Hindi compatible ang `pydantic_function_tool()`**: Ang helper na `openai.pydantic_function_tool()` ay nagge-generate pa rin ng lumang nested format. Huwag gamitin ito sa `responses.create()`. Mag-define ng tool schemas nang mano-mano o i-flatten ang output.
20. **Gumagamit ang tool results ng `function_call_output`, hindi `role: tool`**: Pagkatapos mag-execute ng tool, idagdag ang `{"type": "function_call_output", "call_id": ..., "output": ...}` — hindi `{"role": "tool", "tool_call_id": ..., "content": ...}`. Para sa tool request ng assistant, gamitin ang `messages.extend(response.output)` — hindi manual na dictionary na `{"role": "assistant", "tool_calls": [...]}`.
21. **Kailangan ng `required` + `additionalProperties: false` kapag may `strict: true`**: Kapag gumagamit ng `strict: true` sa tool, lahat ng property ay dapat nakalista sa `required` array at ang `additionalProperties` ay dapat `false`. Kapag may kulang, magreresulta ito ng 400 error.
22. **May partikular na prefix ang Function call IDs**: Kapag nagbibigay ng few-shot na `function_call` items sa `input`, ang `id` field ay dapat magsimula sa `fc_` at ang `call_id` field ay dapat magsimula sa `call_` (hal. `"id": "fc_example1", "call_id": "call_example1"`). Ang paggamit ng lumang Chat Completions na prefix na `call_` para sa `id` ay tinatanggihan.
23. **Hindi suportado ng GitHub Models ang Responses API**: Kung ang app ay may GitHub Models code path (`base_url` na nakaturo sa `models.github.ai` o `models.inference.ai.azure.com`), alisin ito nang buo. Walang migration path — lumipat sa Azure OpenAI, OpenAI, o compatible na local endpoint.
24. **Nagbago ang istruktura ng error body ng content filter**: Ginagamit ng Chat Completions error ang `error.body["innererror"]["content_filter_result"]` (singular). Ang Responses API error ay gumagamit ng `error.body["content_filters"][0]["content_filter_results"]` (plural, nasa loob ng array). Wala na ang `innererror` key. Ang code na direktang gumagamit ng `innererror` ay magta-throw ng `KeyError` sa runtime — madaling hindi mapansin ito sa migration dahil lalabas lang kapag na-trigger ang content filter. Palaging i-grep ang `innererror` sa migration.
25. **Kailangang baguhin ang URL + body para sa raw HTTP calls**: Ang apps na direktang tumatawag sa Azure OpenAI REST (gamit ang `requests`, `httpx`, `aiohttp`) gamit ang `/openai/deployments/{name}/chat/completions?api-version=...` ay kailangang lumipat sa `/openai/v1/responses`. Ang request body ay gumagamit ng `input` imbes na `messages`, nangangailangan ng `max_output_tokens` at `store`, at hindi na kailangan ang `api-version` query param. Ang response body text ay nasa `output[0].content[0].text` — **hindi** `output_text`, na isang SDK convenience property na wala sa raw REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->