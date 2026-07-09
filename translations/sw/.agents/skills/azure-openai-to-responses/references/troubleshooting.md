# Utatuzi wa Matatizo, Jedwali la Hatari & Vidokezo Muhimu

## Utatuzi wa matatizo ya 400s

| Hitilafu | Marekebisho |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Ufafanuzi wa chombo unatumia muundo wa zamani wa Chat Completions | Punguza kutoka `{"type": "function", "function": {"name": ...}}` hadi `{"type": "function", "name": ..., "parameters": ...}` — jina, maelezo, vigezo ziwe ngazi ya juu |
| `unknown_parameter: input[N].tool_calls` | Matokeo ya chombo ya mizunguko mingi yanatumia muundo wa zamani wa Chat Completions | Badilisha `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` kwa vitu vya `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Chombo kilicho na `strict: true` kinakosa orodha ya `required` | Wakati `strict: true`, mali zote lazima ziandikwe kwenye `required` na `additionalProperties: false` lazima iwe imewekwa |
| `invalid_function_parameters: 'additionalProperties' is required` | Chombo kilicho na `strict: true` kinakosa `additionalProperties: false` | Ongeza `"additionalProperties": false` kwenye kitu cha vigezo |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Kitambulisho cha function_call cha few-shot kina kionzi kibaya | Vitambulisho vya function call lazima vianze na `fc_` (mfano, `fc_example1`), si `call_` |
| `missing_required_parameter: text.format.name` | Ongeza ufunguo wa `"name"` kwenye kamusi ya format (mfano, `"name": "Output"`) |
| `invalid_type: text.format` | Hakikisha `text.format` ni kamusi yenye funguo `type`, `name`, `strict`, `schema` — si mfuatano wa herufi |
| `invalid input content type` | Tumia aina za yaliyomo `input_text`/`output_text` badala ya Chat `text` |
| `invalid input content type` (picha) | Aina ya yaliyomo ya picha bado inatumia `"type": "image_url"` | Badilisha kuwa `"type": "input_image"` |
| `Expected object, got string` kwenye `image_url` | `image_url` bado ni kitu kilichojumuishwa `{"url": "..."}` | Punguza kuwa mfuatano wa herufi: `"image_url": "https://..."` au `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` kwa `max_output_tokens` | Chini ya kiwango cha chini **16** kwenye Azure OpenAI. Tumia 50+ kwa majaribio, 1000+ kwa uzalishaji. |
| `429 Too Many Requests` wakati wa uchezaji wa mtiririko | Kiwango kimezuiwa. Zungusha uchezaji wa mtiririko ndani ya `try/except`, tolea JSON ya hitilafu kwa mbeleza, tumia upunguzaji/marudio. |
| `KeyError: 'innererror'` kwenye hitilafu ya kichujio cha yaliyomo | Muundo wa mwili wa hitilafu ya kichujio cha yaliyomo umepata mabadiliko katika Responses API | Chat Completions ilitumia `error.body["innererror"]["content_filter_result"]`; Responses API inatumia `error.body["content_filters"][0]["content_filter_results"]` (zaidisho, ndani ya orodha). Rekebisha upatikanaji wote wa `innererror`. |

---

## Jedwali la Hatari za Uhamiaji

| Dalili | Hitilafu Inayoweza Kutokea | Marekebisho |
|---------|---------------|-----|
| `output_text` tupu / jibu lililokatizwa | `max_output_tokens` iko chini mno kwa mifano ya hoja | Weka `max_output_tokens=1000` au zaidi — tokeni za hoja zinahesabiwa kwenye kikomo |
| `400 invalid_type: text.format` | Ilipitishwa mfuatano wa herufi `response_format` badala ya kamusi ya `text.format` | Tumia `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` kwenye `/openai/v1/responses` | `base_url` si sahihi — inakosa mwisho wa `/openai/v1/` | Hakikisha `base_url=f"{endpoint}/openai/v1/"` (ikiwa na slash ya mwisho) |
| `401 Unauthorized` baada ya kubadilisha kuwa `OpenAI()` | `api_key` haijapewa au mtoaji wa tokeni hajapewa kwa usahihi | Kwa EntraID: `api_key=token_provider` (inaweza kuitwa). Kwa ufunguo wa API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Mfano unarejesha `deployment not found` | Parameta ya `model` haifanani na jina la uanzishaji wako wa Azure | Tumia `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — hili ni jina la uanzishaji, si jina la mfano |
| `json.loads(resp.output_text)` linaleta `JSONDecodeError` | Kiwango hakitekelezwi au mfano hauungi mkono JSON imara | Hakikisha `"strict": True` ndani ya schema, na hakiki mfano unaunga mkono matokeo yaliyo na muundo |
| Mtiririko hauleti matukio ya `delta` | Kuangalia aina ya tukio isiyo sahihi | Chuja kwa `event.type == "response.output_text.delta"`, si `chat.completion.chunk` za Chat |
| Hitilafu ya `400` kwenye ingizo la picha baada ya uhamiaji | Aina ya yaliyomo ya picha haijasasishwa | Badilisha `"type": "image_url"` → `"type": "input_image"` na punguza `"image_url": {"url": "..."}` → `"image_url": "..."` (mfuatano safi) |
| Mizunguko ya simu za zana haikomi | Matokeo ya chombo hayajajumuishwa kwa `input` inayofuata | Baada ya kutekeleza chombo, ongeza kipengee `{"type": "function_call_output", "call_id": ..., "output": ...}` kwenye `input` kwa ombi lufuatao |
| Hitilafu ya `temperature` na GPT-5 au mfululizo wa o | Thamani ya wazi ya `temperature` sio 1 | Ondoa `temperature` au weka thamani 1 kwa mifano ya GPT-5 na mfululizo wa o (o1, o3-mini, o3, o4-mini) |
| Hitilafu ya `top_p` na mfululizo wa o | `top_p` haitekelezwi | Ondoa `top_p` wakati unalenga mifano ya mfululizo wa o |
| `max_completion_tokens` haikutambuliwa | Kutumia parametro maalum ya Azure | Badilisha `max_completion_tokens` na `max_output_tokens`. Weka 4096+ kwa mfululizo wa o (tokeni za hoja zinahesabiwa kwenye kikomo). |
| Matokeo tupu au yaliyokatizwa kutoka mfululizo wa o | `max_output_tokens` ni ndogo mno | Mfululizo wa o hutumia tokeni za hoja ndani. Weka `max_output_tokens=4096` au zaidi — sio 500–1000. |
| `400 integer_below_min_value` kwa `max_output_tokens` | Thamani ni chini ya 16 | Azure OpenAI inalazimisha `max_output_tokens >= 16`. Tumia 50+ kwa majaribio, 1000+ kwa uzalishaji. |
| `429 Too Many Requests` katikati ya mtiririko | Kiwango kimezuiwa na Azure OpenAI | Mtiririko huvunjika kimya bila kushughulikia makosa. Daima zungusha `async for event in await coroutine:` ndani ya `try/except` na toa `{"error": str(e)}` kwa mbeleza. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Mpakani si sahihi au haujajiandikisha | Pitia `tenant_id=os.getenv("AZURE_TENANT_ID")` waziwazi. Endesha `azd auth login --tenant <tenant-id>` eneo lako. |
| `404 Not Found` unapotumia Mifano ya GitHub (`models.github.ai`) | Mifano ya GitHub haitekelezi Responses API | Ondoa kabisa njia ya msimbo wa Mifano ya GitHub. Tumia Azure OpenAI, OpenAI, au mwisho wa huduma unaoendana wa ndani (mfano, Ollama yenye msaada wa Responses). |
| MAF `OpenAIChatCompletionClient` bado inatumia Chat Completions | Kutumia mteja wa zamani wa MAF katika 1.0.0+ | Katika MAF 1.0.0+, `OpenAIChatClient` hutumia Responses API kwa default. Badilisha `OpenAIChatCompletionClient` na `OpenAIChatClient`. Kwa pre-1.0.0, sasisha kwa `agent-framework-openai>=1.0.0`. |
| Maajenti wa LangChain kurudisha ujazo au kushindwa na simu za zana | `ChatOpenAI` haijatumia Responses API | Ongeza `use_responses_api=True` kwenye `ChatOpenAI(...)`. Pia badilisha `.content` → `.text` kwenye ujumbe wa majibu. |
| `KeyError: 'innererror'` katika mshughulikiaji wa hitilafu ya kichujio cha yaliyomo | Muundo wa mwili wa hitilafu umebadilika katika Responses API | Andika upya `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Kifuniko cha `innererror` kimeondoka; maelezo ya kichujio sasa yamo kwenye orodha ya ngazi ya juu `content_filters` yenye `content_filter_results` ndani ya kila kipengee. |
| Simu ya moja kwa moja ya HTTP kwenda `/openai/deployments/.../chat/completions` inarejesha 404 | Mwangalizi wa zamani wa Chat Completions REST endpoint | Rekebisha URL kuwa `/openai/v1/responses`. Badilisha mwili wa ombi: `messages` → `input`, ongeza `max_output_tokens` + `store: false`, toa parametro ya query `api-version`. Badilisha uchambuzi wa jibu: `choices[0].message.content` → `output[0].content[0].text` (kumbuka: `output_text` ni sifa ya urahisi wa SDK, si sehemu ya raw REST JSON). |

---

## Vidokezo Muhimu

1. Ikiwa ulitumia Chat Completions awali kwa hali ya mazungumzo, simamia hali yako mwenyewe waziwazi kwa Responses.
2. Upende `max_output_tokens` badala ya `max_tokens` ya zamani.
3. Unapohamia kwa `gpt-5`, hakikisha `temperature` haijatolewa au imewekwa `1`.
4. Badilisha Chat `content[].type: "text"` kwa Responses `content[].type: "input_text"` kwa ingizo za mtumiaji/mfumo.
5. Kwa `text.format`, toa kamusi sahihi (mfano, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), si mfuatano wa herufi.
6. Parameta ya `seed` haitekelezwi kwenye Responses; ondoa kwenye maombi.
7. **Hoja**: Jumuisha `reasoning` tu ikiwa msimbo wa awali ulikuwa unaitumia. Usiongeze `reasoning` kwenye simu za API ambazo hazikuwa nazo — mifano mingi (mfano, gpt-4o-mini) haisaidii parameta hii.
8. **Ukubwa wa `max_output_tokens`**: Kwa mifano ya hoja (GPT-5-mini, GPT-5, mfululizo wa o), tumia `max_output_tokens=4096` au zaidi — si 50–1000. Mfano hutumia tokeni za hoja ndani kabla ya kutoa matokeo yanayoonekana; mipaka ya chini sana husababisha majibu yaliyokatizwa au tupu.
9. **O-series `max_completion_tokens`**: Ikiwa msimbo awali ulikuwa unatumia `max_completion_tokens` (ya Azure maalum kwa mfululizo wa o), badilisha na `max_output_tokens`. Responses API haikubali `max_completion_tokens`.
10. **O-series `reasoning_effort`**: Ikiwa msimbo awali unatumia `reasoning_effort` (chini/kati/juu), hamisha kuwa `reasoning={"effort": "<thamani>"}` katika simu za Responses API.
11. **Kuchelewesha mtiririko wa mfululizo wa O**: Mifano ya mfululizo wa o hufanya hoja za ndani kabla ya kutoa matokeo. Unapocheza mtiririko, tarajia kuchelewa kwa matukio ya kwanza ya `response.output_text.delta`. Hii ni hali ya kawaida — mfano unahesabu, haumei.
9. **`_azure_ad_token_provider` imeondoka**: `AsyncOpenAI` / `OpenAI` haina sifa ya `_azure_ad_token_provider`. Majaribio au msimbo unaohitaji sifa hii utaanguka na `AttributeError`. Mtoaji wa tokeni hupitishwa kama `api_key` na hawezi kupitiwa kwenye kifaa cha mteja.
10. **Faili za snapshot / dhahabu**: Ikiwa suite ya mtihani inatumia mtihani wa snapshot, **faili zote** za snapshot zenye maumbo ya matiririko ya Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, nk) lazima zibadilishwe kwa maumbo mapya ya Responses. Hii ni rahisi kukosa na husababisha makosa ya uthibitisho wa snapshot.
11. **Njia ya monkeypatch ya mock**: Lengo la monkeypatch hubadilika kutoka `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (au `Responses.create` kwa sync). Kutumia njia ya zamani kimya hakutafanya chochote — mock haitawazuia, na majaribio hugonga API halisi au huanguka.
12. **`input` si `messages`**: Funguo za mock lazima zisisome `kwargs.get("input")` si `kwargs.get("messages")`. Responses API hutumia `input` kwa rekodi za mazungumzo.
13. **Majina ya mabadiliko ya mazingira**: Azure Identity SDK hutumia `AZURE_CLIENT_ID` (si `AZURE_OPENAI_CLIENT_ID`) kwa `ManagedIdentityCredential(client_id=...)`. Badilisha majina katika majaribio, faili za `.env`, mipangilio ya programu, na Bicep/infrastructure.
14. **Kiwango cha chini cha `max_output_tokens` ni 16**: Azure OpenAI hukataa thamani chini ya 16 na `400 integer_below_min_value`. Tumia 50 kwa majaribio ya harufu, 1000+ kwa uzalishaji. `max_tokens` ya zamani haikuwa na kiwango kama hicho.
15. **`tenant_id` kwa `AzureDeveloperCliCredential`**: Wakati rasilimali ya Azure OpenAI iko kwenye mpakani tofauti, lazima upitie `tenant_id` wazi — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Bila hilo, cheti hutumia mpakani mbaya kimya na kurudisha `401`.
16. **Vikwazo vya kiwango vinaonekana tofauti katika mtiririko**: Kwa Chat Completions, 429 ilizuia kabisa kuanza mtiririko. Kwa streaming ya Responses API, 429 inaweza kutokea **katikati ya mtiririko** — iterator async huleta kosa. Daima zungusha mzunguko wa mtiririko ndani ya `try/except` na toa mstari wa JSON wa hitilafu ili mbeleza ishughulikie kwa upole.

17. **Utunzaji wa makosa ya mtiririko ni lazima kwa programu za wavuti**: Muda mfupi `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` ni muhimu sana. Bila yake, mtiririko wa SSE/JSONL unakufa kimya kwa kosa lolote upande wa seva na sehemu ya mbele inashikamaa.
18. **Maelezo ya zana lazima yatumie muundo wa wima**: API ya Majibu inatarajia `{"type": "function", "name": ..., "parameters": ...}` — sio ile ya Chat Completions iliyofichwa `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Hii ndilo kosa la kawaida zaidi la uhamiaji kwa msimbo wa kuita kazi.
19. **`pydantic_function_tool()` haifai**: Msaidizi wa `openai.pydantic_function_tool()` bado huunda muundo wa zamani uliofichwa. Usiyumize pamoja na `responses.create()`. Tafsiri vipimo vya zana kwa mikono au tambua mdogo wa mzilo.
20. **Matokeo ya zana yatumia `function_call_output`, si `role: tool`**: Baada ya kutekeleza zana, ongeza `{"type": "function_call_output", "call_id": ..., "output": ...}` — si `{"role": "tool", "tool_call_id": ..., "content": ...}`. Kwa ombi la zana la msaidizi, tumia `messages.extend(response.output)` — si kamusi ya mkono `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` inahitaji `required` + `additionalProperties: false`**: Unapotumia `strict: true` kwenye zana, kila mali lazima iwe katika safu ya `required` na `additionalProperties` lazima iwe `false`. Kukosa yoyote huleta kosa la 400.
22. **Vitambulisho vya simu ya kazi vina vifungu maalum**: Unapotumia vitu vya `function_call` vya few-shot katika `input`, sehemu ya `id` lazima ianze na `fc_` na sehemu ya `call_id` lazima ianze na `call_` (mfano, `"id": "fc_example1", "call_id": "call_example1"`). Kutumia kifungu cha zamani cha Chat Completions `call_` kwa `id` hukataliwa.
23. **GitHub Models haitegemezi API ya Majibu**: Ikiwa programu ina njia ya msimbo ya GitHub Models (`base_url` inashika `models.github.ai` au `models.inference.ai.azure.com`), iondoe wote kabisa. Hakuna njia ya uhamiaji — badilisha kwenda Azure OpenAI, OpenAI, au sehemu inayofanana ya ndani.
24. **Muundo wa mwili wa makosa ya kichujio cha maudhui umebadilika**: Makosa ya Chat Completions yalitumia `error.body["innererror"]["content_filter_result"]` (mmoja). Makosa ya API ya Majibu yanatumia `error.body["content_filters"][0]["content_filter_results"]` (wengi, ndani ya orodha). Kitufe cha `innererror` hakipo tena. Msimbo unaofikia moja kwa moja `innererror` utatoa `KeyError` wakati wa utekelezaji — hii ni rahisi kupuuzwa wakati wa uhamiaji kwa kuwa huonekana tu wakati kichujio cha maudhui kikitokea. Daima tafuta `innererror` wakati wa uhamiaji.
25. **Simu za moja kwa moja za HTTP zinahitaji badiliko la URL + mwili**: Programu zinazoita moja kwa moja Azure OpenAI REST (kwa kutumia `requests`, `httpx`, `aiohttp`) kwa `/openai/deployments/{name}/chat/completions?api-version=...` lazima zibadilishe kwenda `/openai/v1/responses`. Mwili wa ombi unatumia `input` badala ya `messages`, unahitaji `max_output_tokens` na `store`, na kigezo cha maswali `api-version` kinatolewa. Maandishi ya mwili wa jibu yamo katika `output[0].content[0].text` — **si** `output_text`, ambayo ni mali rahisi ya SDK isiyoonekana katika JSON halisi ya REST.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->