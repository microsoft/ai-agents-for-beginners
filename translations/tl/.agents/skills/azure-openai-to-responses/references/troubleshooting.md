# Pag-troubleshoot, Talaan ng Panganib & Mga Paalala

## Pag-troubleshoot ng 400s

| Error | Ayusin |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Ang depinisyon ng tool ay gumagamit ng lumang nested format ng Chat Completions | I-flatten mula sa `{"type": "function", "function": {"name": ...}}` patungong `{"type": "function", "name": ..., "parameters": ...}` — ang name, description, parameters ay ilalagay sa top level |
| `unknown_parameter: input[N].tool_calls` | Ang multi-turn na mga resulta ng tool ay gumagamit ng lumang format ng Chat Completions | Palitan ang `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` gamit ang mga item ng `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Ang `strict: true` na tool ay walang `required` array | Kapag `strict: true`, lahat ng properties ay dapat naka-lista sa `required` at dapat may nakalagay na `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Ang `strict: true` na tool ay walang `additionalProperties: false` | Idagdag ang `"additionalProperties": false` sa parameters object |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Mali ang prefix ng Few-shot function_call ID | Dapat nagsisimula ang ID ng function call sa `fc_` (hal., `fc_example1`), hindi `call_` |
| `missing_required_parameter: text.format.name` | Magdagdag ng `"name"` na key sa format dict (hal., `"name": "Output"`) |
| `invalid_type: text.format` | Siguraduhing ang `text.format` ay isang dict na may mga key na `type`, `name`, `strict`, `schema` — hindi string |
| `invalid input content type` | Gamitin ang `input_text`/`output_text` na mga content type sa halip na Chat `text` |
| `invalid input content type` (image) | Ang image content ay gumagamit pa rin ng `"type": "image_url"` | Palitan sa `"type": "input_image"` |
| `Expected object, got string` sa `image_url` | Ang `image_url` ay isa pang nested object pa rin na `{"url": "..."}` | I-flatten sa plain na string: `"image_url": "https://..."` o `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` para sa `max_output_tokens` | Ang minimum ay **16** sa Azure OpenAI. Gumamit ng 50+ para sa mga tests, 1000+ para sa produksyon. |
| `429 Too Many Requests` habang streaming | Rate limited. Balutin ang streaming sa `try/except`, i-yield ang error JSON sa frontend, ipatupad ang backoff/retry. |
| `KeyError: 'innererror'` sa content filter error | Nagbago ang structure ng laman ng content filter error sa Responses API | Ginagamit ng Chat Completions ang `error.body["innererror"]["content_filter_result"]`; ang Responses API ay gumagamit ng `error.body["content_filters"][0]["content_filter_results"]` (plural, nasa array). Isulat muli ang lahat ng `innererror` access. |

---

## Talaan ng Panganib sa Migration

| Sintomas | Posibleng Mali | Ayusin |
|---------|---------------|-----|
| Walang laman `output_text` / naputol na sagot | Masyadong mababa ang `max_output_tokens` para sa reasoning models | Itakda ang `max_output_tokens=1000` o mas mataas — binibilang ng reasoning tokens laban sa limitasyon |
| `400 invalid_type: text.format` | Nagpasa ng string na `response_format` sa halip na dict ng `text.format` | Gamitin ang `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` sa `/openai/v1/responses` | Mali ang `base_url` — kulang ng `/openai/v1/` na suffix | Siguraduhing `base_url=f"{endpoint}/openai/v1/"` (na may trailing slash) |
| `401 Unauthorized` pagkatapos lumipat sa `OpenAI()` | Hindi na-set ang `api_key` o hindi tama ang pagkaipasa ng token provider | Para sa EntraID: `api_key=token_provider` (ang callable). Para sa API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Nagbabalik ang model ng `deployment not found` | Hindi tugma ang `model` param sa pangalan ng Azure deployment mo | Gamitin ang `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — ito ang pangalan ng deployment, hindi ng model |
| Nag-raise ng `JSONDecodeError` ang `json.loads(resp.output_text)` | Hindi naipinatutupad ang schema o hindi sinusuportahan ng model ang strict JSON | Siguraduhing meron `"strict": True` sa schema, at i-verify na sinusuportahan ng model ang structured output |
| Walang lumabas na `delta` events sa streaming | Tinitingnan ang maling uri ng event | I-filter ang `event.type == "response.output_text.delta"`, hindi ang Chat na `chat.completion.chunk` |
| `400` error sa image input pagkatapos ng migration | Hindi na-update ang image content type | Palitan ang `"type": "image_url"` sa `"type": "input_image"` at i-flatten ang `"image_url": {"url": "..."}` sa `"image_url": "..."` (plain na string) |
| Paulit-ulit ang tool calls | Kulang ng tool result sa follow-up na `input` | Pagkatapos gamitin ang tool, idagdag ang item na `{"type": "function_call_output", "call_id": ..., "output": ...}` sa `input` sa susunod na request |
| Error sa `temperature` gamit ang GPT-5 o o-series | Eksplikadong value ng `temperature` na iba sa 1 | Alisin ang `temperature` o itakda sa `1` para sa GPT-5 at o-series models (o1, o3-mini, o3, o4-mini) |
| Error sa `top_p` gamit ang o-series | Hindi sinusuportahan ang `top_p` | Alisin ang `top_p` kapag nagtatrabaho sa o-series models |
| Hindi kinikilala ang `max_completion_tokens` | Gumagamit ng parameter na spesipiko sa Azure | Palitan ang `max_completion_tokens` ng `max_output_tokens`. Itakda sa 4096+ para sa o-series (binibilang ng reasoning tokens laban sa limit). |
| Walang laman o napurol na output mula sa o-series | Masyadong mababa ang `max_output_tokens` | Gumagamit ang o-series ng reasoning tokens internally. Itakda ang `max_output_tokens=4096` o mas mataas — hindi 500–1000. |
| `400 integer_below_min_value` para sa `max_output_tokens` | Mas mababa sa 16 ang value | Ipinapatupad ng Azure OpenAI ang `max_output_tokens >= 16`. Gumamit ng 50+ para sa smoke tests, 1000+ para sa produksyon. |
| `429 Too Many Requests` sa kalagitnaan ng stream | Na-rate limit ng Azure OpenAI | Ang stream ay biglang titigil nang walang error handling. Palaging balutin ang `async for event in await coroutine:` sa `try/except` at i-yield ang `{"error": str(e)}` sa frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Mali ang tenant o hindi naka-login | Ibigay nang eksakto ang `tenant_id=os.getenv("AZURE_TENANT_ID")`. Patakbuhin ang `azd auth login --tenant <tenant-id>` sa local machine. |
| `404 Not Found` kapag gumagamit ng GitHub Models (`models.github.ai`) | Hindi sinusuportahan ng GitHub Models ang Responses API | Alisin nang buo ang GitHub Models na code path. Gumamit ng Azure OpenAI, OpenAI, o compatible na local endpoint (hal., Ollama na may support sa Responses). |
| MAF `OpenAIChatCompletionClient` ginagamit pa rin ang Chat Completions | Ginagamit ang legacy na MAF client sa 1.0.0+ | Sa MAF 1.0.0+, default nang gumagamit ang `OpenAIChatClient` ng Responses API. Palitan ang `OpenAIChatCompletionClient` ng `OpenAIChatClient`. Para sa pre-1.0.0, mag-upgrade sa `agent-framework-openai>=1.0.0`. |
| Nagbabalik ang LangChain agent ng walang laman o pumapalya sa tool calls | `ChatOpenAI` hindi gumagamit ng Responses API | Idagdag ang `use_responses_api=True` sa `ChatOpenAI(...)`. Palitan din ang `.content` → `.text` sa response messages. |
| `KeyError: 'innererror'` sa content filter error handler | Nagbago ang structure ng error body sa Responses API | Isulat muli ang `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Wala na ang wrapper na `innererror`; ang detalye ng content filter ay nasa top-level na `content_filters` array na may `content_filter_results` (plural) sa bawat entry. |
| Raw HTTP call sa `/openai/deployments/.../chat/completions` ay nagbabalik ng 404 | Lumang Chat Completions REST endpoint | Isulat muli ang URL sa `/openai/v1/responses`. Palitan ang body ng request: `messages` → `input`, idagdag ang `max_output_tokens` + `store: false`, alisin ang query param na `api-version`. Palitan ang pag-parse ng sagot: `choices[0].message.content` → `output[0].content[0].text` (tandaan: ang `output_text` ay convenience property sa SDK, hindi bahagi ng raw na REST JSON). |

---

## Mga Paalala

1. Kung dati kang gumamit ng Chat Completions para sa conversation state, pamahalaan ang sarili mong state nang tahasan gamit ang Responses.
2. Mas piliin ang `max_output_tokens` kaysa sa legacy na `max_tokens`.
3. Kapag nag-migrate sa `gpt-5`, siguraduhing hindi nakasaad ang `temperature` o ito ay nakatakda sa `1`.
4. Palitan ang Chat `content[].type: "text"` ng Responses `content[].type: "input_text"` para sa mga user/system inputs.
5. Para sa `text.format`, magbigay ng tamang dict (hal., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), hindi plain na string.
6. Hindi sinusuportahan ang `seed` parameter sa Responses; alisin ito sa mga request.
7. **Reasoning**: Isama lamang ang `reasoning` kung ginamit na ito sa orihinal na code. Huwag magdagdag ng `reasoning` sa mga API call na wala nito — maraming models (hal., gpt-4o-mini) ang hindi sumusuporta sa parameter na ito.
8. **Sukat ng `max_output_tokens`**: Para sa reasoning models (GPT-5-mini, GPT-5, o-series), gamitin ang `max_output_tokens=4096` o mas mataas — hindi 50–1000. Ginagamit ng model ang reasoning tokens internally bago gumawa ng nakikitang output; ang masyadong mababang limitasyon ay nagdudulot ng naputol o walang laman na sagot.
9. **`max_completion_tokens` sa O-series**: Kung ginamit ng orihinal na code ang `max_completion_tokens` (Azure-specific para sa o-series), palitan ito ng `max_output_tokens`. Hindi tinatanggap ng Responses API ang `max_completion_tokens`.
10. **`reasoning_effort` sa O-series**: Kung ginagamit ng orihinal na code ang `reasoning_effort` (mababaw/katamtaman/mataas), i-migrate ito sa `reasoning={"effort": "<value>"}` sa tawag ng Responses API.
11. **Delay sa streaming ng O-series**: Gumagawa muna ng internal reasoning ang O-series models bago gumawa ng output. Kapag streaming, asahan ang mas mahabang delay bago lumabas ang unang `response.output_text.delta` na event. Normal ito — nagrereasoning ang model, hindi na-hang.
9. **Wala na ang `_azure_ad_token_provider`**: Ang `AsyncOpenAI` / `OpenAI` ay walang `_azure_ad_token_provider` attribute. Ang mga tests o code na sumusubok i-access ito ay gagalaw ng `AttributeError`. Ang token provider ay ipinapasa bilang `api_key` at hindi mare-review sa client object.
10. **Snapshot / golden files**: Kung gumagamit ang test suite ng snapshot testing, **lahat** ng snapshot files na may mga Chat Completions streaming shapes (`choices[0]`, `content_filter_results`, `function_call`, atbp.) ay dapat i-update sa bagong shape ng Responses. Madaling makaligtaan ito at nagdudulot ng mga snapshot assertion failures.
11. **Mock monkeypatch path**: Nagbabago ang target ng monkeypatch mula sa `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (o `Responses.create` para sa sync). Ang paggamit ng lumang path ay hindi magkakaroon ng epekto — hindi ma-intercept ang mock, at ang tests ay tatamaan ang tunay na API o mabibigo.
12. **`input` hindi `messages`**: Dapat basahin ng mock functions ang `kwargs.get("input")` hindi `kwargs.get("messages")`. Ginagamit ng Responses API ang `input` para sa conversation history.
13. **Pangalan ng env var**: Ginagamit ng Azure Identity SDK ang `AZURE_CLIENT_ID` (hindi `AZURE_OPENAI_CLIENT_ID`) para sa `ManagedIdentityCredential(client_id=...)`. Palitan ito sa tests, `.env` files, app settings, at Bicep/infra.
14. **Minimum ng `max_output_tokens` ay 16**: Tinanggihan ng Azure OpenAI ang mga value na mas mababa sa 16 na may `400 integer_below_min_value`. Gumamit ng 50 para sa smoke tests, 1000+ para sa produksyon. Wala namang ganitong minimum ang lumang `max_tokens`.
15. **`tenant_id` para sa `AzureDeveloperCliCredential`**: Kapag ang Azure OpenAI resource ay nasa ibang tenant, **kailangang** ipasa ang `tenant_id` nang tahasan — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Kapag wala ito, tahasan nitong ginagamit ang maling tenant at nagbabalik ng `401`.
16. **Iba ang paglitaw ng rate limits sa streaming**: Sa Chat Completions, karaniwang napipigilan ang stream na magsimula kapag may 429. Sa streaming gamit ang Responses API, puwedeng mangyari ang 429 **habang nasa gitna ng stream** — ang async iterator ay nag-raise ng exception. Palaging balutin ang streaming loop sa `try/except` at i-yield ang linya ng error JSON para ma-handle ito ng frontend ng maayos.

17. **Mandatory ang paghawak ng error sa streaming para sa mga web app**: Ang pattern na `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` ay kritikal. Kung wala ito, tahimik na namamatay ang SSE/JSONL stream kapag may anumang error sa server-side at nagha-hang ang frontend.
18. **Dapat gumagamit ng flat format ang mga depinisyon ng tool**: Inaasahan ng Responses API ang `{"type": "function", "name": ..., "parameters": ...}` — hindi ang nested na `{"type": "function", "function": {"name": ..., "parameters": ...}}` ng Chat Completions. Ito ang pinakakaraniwang error sa migration para sa code na tumatawag ng function.
19. **Hindi compatible ang `pydantic_function_tool()`**: Ang helper na `openai.pydantic_function_tool()` ay patuloy na gumagawa ng lumang nested na format. Huwag gamitin ito kasama ang `responses.create()`. Manu-manong ideklara ang mga schema ng tool o i-flatten ang output.
20. **Gumagamit ang mga resulta ng tool ng `function_call_output`, hindi `role: tool`**: Pagkatapos patakbuhin ang tool, idagdag ang `{"type": "function_call_output", "call_id": ..., "output": ...}` — hindi `{"role": "tool", "tool_call_id": ..., "content": ...}`. Para sa kahilingan ng assistant sa tool, gamitin ang `messages.extend(response.output)` — hindi manu-manong `{"role": "assistant", "tool_calls": [...]}` na dict.
21. **Kinakailangan ng `strict: true` ang `required` + `additionalProperties: false`**: Kapag ginamit ang `strict: true` sa isang tool, dapat nakalista lahat ng property sa array na `required` at ang `additionalProperties` ay dapat `false`. Ang kakulangan sa alinman ay magdudulot ng 400 na error.
22. **May mga tiyak na prefix ang mga Function call ID**: Kapag nagbibigay ng few-shot `function_call` items sa `input`, dapat magsimula sa `fc_` ang `id` field at ang `call_id` field ay dapat magsimula sa `call_` (halimbawa, `"id": "fc_example1", "call_id": "call_example1"`). Tinanggihan ang paggamit ng lumang Chat Completions prefix na `call_` para sa `id`.
23. **Hindi sinusuportahan ng GitHub Models ang Responses API**: Kung may code path ang app sa GitHub Models (`base_url` na nakaturo sa `models.github.ai` o `models.inference.ai.azure.com`), alisin ito nang buo. Wala nang daan sa migration — lumipat sa Azure OpenAI, OpenAI, o isang compatible na lokal na endpoint.
24. **Nagbago ang istruktura ng error body ng content filter**: Ginamit ng Chat Completions error ang `error.body["innererror"]["content_filter_result"]` (isahan). Ginagamit ng Responses API error ang `error.body["content_filters"][0]["content_filter_results"]` (maramihan, nasa loob ng array). Wala na ang key na `innererror`. Ang code na direktang nag-a-access sa `innererror` ay magtataas ng `KeyError` sa runtime — madaling hindi mapansin ito sa migration dahil lumalabas lang ito kapag na-trigger ang content filter. Palaging i-grep ang `innererror` sa panahon ng migration.
25. **Kailangang i-rewrite ang URL + body sa mga raw na HTTP call**: Ang mga app na tumatawag diretso sa Azure OpenAI REST (gamit ang `requests`, `httpx`, `aiohttp`) gamit ang `/openai/deployments/{name}/chat/completions?api-version=...` ay kailangang lumipat sa `/openai/v1/responses`. Ginagamit sa request body ang `input` sa halip na `messages`, kinakailangan ang `max_output_tokens` at `store`, at tinanggal ang `api-version` query param. Ang teksto ng response body ay nasa `output[0].content[0].text` — **hindi** `output_text`, na isang convenience property ng SDK na wala sa raw REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->