# Utatuzi wa Matatizo, Meza ya Hatari & Vidokezo vya Tahadhari

## Utatuzi wa Matatizo ya 400s

| Hitilafu | Suluhisho |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Ufafanuzi wa chombo unatumia muundo wa zamani wa Chat Completions ulio ndani | Punguza kutoka `{"type": "function", "function": {"name": ...}}` hadi `{"type": "function", "name": ..., "parameters": ...}` — jina, maelezo, vigezo ziwe ngazi ya juu |
| `unknown_parameter: input[N].tool_calls` | Matokeo ya zamu nyingi ya chombo yanatumia muundo wa zamani wa Chat Completions | Badilisha `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` na vitu vya `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Chombo cha `strict: true` hakina safu ya `required` | Wakati `strict: true`, mali zote lazima ziwe zimetajwa katika `required` na `additionalProperties: false` lazima iwe imewekwa |
| `invalid_function_parameters: 'additionalProperties' is required` | Chombo cha `strict: true` hakina `additionalProperties: false` | Ongeza `"additionalProperties": false` kwenye kitu cha vigezo |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Kitambulisho cha function_call kidogo kina awali isiyo sahihi | Vitambulisho vya function call lazima vianze na `fc_` (mfano, `fc_example1`), si `call_` |
| `missing_required_parameter: text.format.name` | Ongeza ufunguo wa `"name"` kwenye kamusi ya format (mfano, `"name": "Output"`) |
| `invalid_type: text.format` | Hakikisha `text.format` ni kamusi yenye vishale vya `type`, `name`, `strict`, `schema` — si mstringi |
| `invalid input content type` | Tumia aina za maudhui `input_text`/`output_text` badala ya Chat `text` |
| `invalid input content type` (picha) | Aina ya maudhui ya picha bado inatumia `"type": "image_url"` | Badilisha kuwa `"type": "input_image"` |
| `Expected object, got string` kwenye `image_url` | `image_url` bado ni kitu kilicho ndani `{"url": "..."}` | Punguza kuwa mstringi rahisi: `"image_url": "https://..."` au `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` kwa `max_output_tokens` | Kiwango cha chini ni **16** kwenye Azure OpenAI. Tumia 50+ kwa majaribio, 1000+ kwa uzalishaji. |
| `429 Too Many Requests` wakati wa utiririshaji | Kiwango cha maombi kimedhibitiwa. Weka utiririshaji ndani ya `try/except`, tosha JSON ya kosa kwa frontend, tekeleza kuchelewesha/rejea. |
| `KeyError: 'innererror'` kwenye hitilafu ya kisafishaji maudhui | Muundo wa mwili wa kosa wa kisafishaji maudhui umebadilika katika Responses API | Chat Completions walitumia `error.body["innererror"]["content_filter_result"]`; Responses API inatumia `error.body["content_filters"][0]["content_filter_results"]` (ya kiwanda, ndani ya array). Andika upya matumizi yote ya `innererror`. |

---

## Meza ya Hatari za Uhamisho

| Dalili | Makosa Yanayowezekana | Suluhisho |
|---------|---------------|-----|
| `output_text` tupu / majibu yaliyokatwa | `max_output_tokens` ni chini sana kwa mifano ya kufikiri | Weka `max_output_tokens=1000` au zaidi — tokeni za kufikiri huhesabiwa kwa kikomo |
| `400 invalid_type: text.format` | Ilipitisha mstringi wa `response_format` badala ya kamusi ya `text.format` | Tumia `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` kwenye `/openai/v1/responses` | `base_url` sio sahihi — hauna kiambatanisho cha `/openai/v1/` | Hakikisha `base_url=f"{endpoint}/openai/v1/"` (na slash ya mwisho) |
| `401 Unauthorized` baada ya kubadili kwa `OpenAI()` | `api_key` haijawekwa au mtoaji tokeni hana maelezo sahihi | Kwa EntraID: `api_key=token_provider` (kazi inayoweza kupitishwa). Kwa API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Mfano unarudisha `deployment not found` | Parameta ya `model` hailingani na jina la uenezi wako Azure | Tumia `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — hili ni jina la uenezi, si jina la mfano |
| `json.loads(resp.output_text)` inaleta `JSONDecodeError` | Mipangilio haitekwi au mfano hauungi mkono JSON kali | Hakikisha `"strict": True` katika schema, na thibitisha mfano unaunga mkono matokeo yaliyopangwa |
| Utiririshaji haujatoa matukio ya `delta` | Kupata aina ya tukio isiyo sahihi | Chuja kwa `event.type == "response.output_text.delta"`, si Chat's `chat.completion.chunk` |
| Hitilafu ya `400` kwa picha iliyotumwa baada ya uhamisho | Aina ya maudhui ya picha haijasasishwa | Badilisha `"type": "image_url"` → `"type": "input_image"` na punguza `"image_url": {"url": "..."}` → `"image_url": "..."` (mstringi rahisi) |
| Mzunguko usioisha wa miito ya zana | Matokeo ya chombo hayajumuishiwa katika `input` inayofuata | Baada ya kutekeleza chombo, ongeza kipengee cha `{"type": "function_call_output", "call_id": ..., "output": ...}` kwa `input` katika ombi linalofuata |
| Hitilafu ya `temperature` na GPT-5 au mfululizo wa o | Thamani ya `temperature` iliyo wazi si 1 | Ondoa `temperature` au weka `1` kwa mifano ya GPT-5 na mfululizo wa o (o1, o3-mini, o3, o4-mini) |
| Hitilafu ya `top_p` na mfululizo wa o | `top_p` haitekelezwi | Ondoa `top_p` unapotumia mifano ya mfululizo wa o |
| `max_completion_tokens` haikutambuliwa | Kutumia parameta ya kipekee ya Azure | Badilisha `max_completion_tokens` na `max_output_tokens`. Weka 4096+ kwa mfululizo wa o (tokeni za kufikiri huhesabiwa kwa kikomo). |
| Matokeo tupu au yaliyokatwa kutoka kwa mfululizo wa o | `max_output_tokens` ni chini sana | Mfululizo wa o hutumia tokeni za kufikiri kwa ndani. Weka `max_output_tokens=4096` au zaidi — si 500–1000. |
| Hitilafu ya `400 integer_below_min_value` kwa `max_output_tokens` | Thamani chini ya 16 | Azure OpenAI inahakikisha `max_output_tokens >= 16`. Tumia 50+ kwa majaribio ya harufu, 1000+ kwa uzalishaji. |
| `429 Too Many Requests` wakati wa katikati ya mtiririko | Kiwango cha maombi kimezimwa na Azure OpenAI | Mtiririko huvunjika kimya bila usimamizi wa makosa. Kila mara weka `async for event in await coroutine:` ndani ya `try/except` na tosha `{"error": str(e)}` kwa frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Mkodishaji sio sahihi au haujajiandikisha | Pitia `tenant_id=os.getenv("AZURE_TENANT_ID")` waziwazi. Tumia `azd auth login --tenant <tenant-id>` mahali pa kazi. |
| `404 Not Found` ukitumia GitHub Models (`models.github.ai`) | GitHub Models haitekelezi Responses API | Ondoa njia ya code ya GitHub Models kabisa. Tumia Azure OpenAI, OpenAI, au sehemu ya localhost inayoungwa mkono (mfano, Ollama na msaada wa Responses). |
| MAF `OpenAIChatCompletionClient` bado inatumia Chat Completions | Kutumia mteja wa zamani wa MAF katika 1.0.0+ | Katika MAF 1.0.0+, `OpenAIChatClient` hutumia Responses API chaguo-msingi. Badilisha `OpenAIChatCompletionClient` na `OpenAIChatClient`. Kwa toleo la kabla ya 1.0.0, sasisha kwa `agent-framework-openai>=1.0.0`. |
| Wakili wa LangChain hurudisha tupu au kushindwa na miito ya zana | `ChatOpenAI` haitumii Responses API | Ongeza `use_responses_api=True` kwa `ChatOpenAI(...)`. Pia badilisha `.content` → `.text` kwenye ujumbe wa majibu. |
| `KeyError: 'innererror'` katika mshughulikiaji wa hitilafu ya kisafishaji maudhui | Muundo wa mwili wa kosa umebadilika katika Responses API | Andika upya `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Mfuko wa `innererror` umeondolewa; maelezo ya kisafishaji maudhui sasa yako kwenye safu ya ngazi ya juu `content_filters` yenye `content_filter_results` (ya viwanda) ndani ya kila kipengee. |
| Miito ya HTTP ghafi kwenda `/openai/deployments/.../chat/completions` inarudisha 404 | Sehemu ya zamani ya Chat Completions REST | Andika upya URL kuwa `/openai/v1/responses`. Badilisha mwili wa ombi: `messages` → `input`, ongeza `max_output_tokens` + `store: false`, toa parameta ya query `api-version`. Badilisha usomaji wa majibu: `choices[0].message.content` → `output[0].content[0].text` (kumbuka: `output_text` ni mali ya urahisi ya SDK, si sehemu ya JSON ghafi ya REST). |

---

## Vidokezo vya Tahadhari

1. Ikiwa ulitumia Chat Completions kwa hali ya mazungumzo hapo awali, simamia hali yako wazi kwa Responses.
2. Upende `max_output_tokens` kuliko `max_tokens` ya zamani.
3. Unapohamia kwa `gpt-5`, hakikisha `temperature` haijawekwa au imewekwa `1`.
4. Badilisha Chat `content[].type: "text"` na Responses `content[].type: "input_text"` kwa pembejeo za mtumiaji/mfumo.
5. Kwa `text.format`, toa kamusi sahihi (mfano, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), si mstringi rahisi.
6. Kipengele cha `seed` hakitekelezwi katika Responses; ondoa kwenye maombi.
7. **Kufikiri**: Jumuisha `reasoning` tu ikiwa msimbo wa awali ulikuwa ukitumia. Usiongeze `reasoning` kwa miito ya API isiyo nayo — mifano mingi isiyo ya kufikiri haitekelezi parameta hii.
8. **Ukubwa wa `max_output_tokens`**: Kwa mifano ya kufikiri (GPT-5-mini, GPT-5, mfululizo wa o), tumia `max_output_tokens=4096` au zaidi — si 50–1000. Mfano hutumia tokeni za kufikiri ndani kabla ya kutoa matokeo yanayoonekana; mipaka ya chini huleta majibu yaliyokatwa au tupu.
9. **`max_completion_tokens` ya mfululizo wa O**: Ikiwa msimbo wa awali ulitumia `max_completion_tokens` (ya kipekee Azure kwa mfululizo wa o), badilisha na `max_output_tokens`. Responses API haiungi mkono `max_completion_tokens`.
10. **`reasoning_effort` ya mfululizo wa O**: Ikiwa msimbo wa awali unatumia `reasoning_effort` (chini/kati/juu), himiriza kwa `reasoning={"effort": "<value>"}` katika mwito wa API wa Responses.
11. **Kuchelewa kwa utiririshaji mfululizo wa O**: Mifano ya mfululizo wa o hufanya kufikiri ndani kabla ya kutoa matokeo. Unapoitiririsha, tarajia ucheleweshaji mrefu kabla ya tukio la kwanza la `response.output_text.delta`. Hii ni kawaida — mfano anafikiri, si kushindwa.
9. **`_azure_ad_token_provider` imeondoka**: `AsyncOpenAI` / `OpenAI` haina sifa ya `_azure_ad_token_provider`. Majaribio au msimbo unaoingia kwenye sifa hii utakosa kwa `AttributeError`. Mtoaji tokeni hutolewa kama `api_key` na hawezi kulindwa kwenye kitu cha mteja.
10. **Faili za awamu / za dhahabu**: Ikiwa suite ya mtihani inatumia mtihani wa snapshot, faili zote za snapshot zenye sura za kuvuja Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, n.k.) lazima zisasishwe kwa sura mpya ya Responses. Hii ni rahisi kupuuzwa na husababisha kushindwa kwa uthibitisho wa snapshot.
11. **Njia ya mock monkeypatch**: Lengo la monkeypatch linabadilika kutoka `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (au `Responses.create` kwa synchronous). Kutumia njia ya zamani hakutafanya chochote kimya — mock haitakamata, na majaribio yatafikisha API halisi au kushindwa.
12. **`input` si `messages`**: Kazi za mock lazima zisome `kwargs.get("input")` si `kwargs.get("messages")`. Responses API inatumia `input` kwa historia ya mazungumzo.
13. **Jina la mabadiliko ya mazingira**: Azure Identity SDK inatumia `AZURE_CLIENT_ID` (sio `AZURE_OPENAI_CLIENT_ID`) kwa `ManagedIdentityCredential(client_id=...)`. Badilisha katika majaribio, faili `.env`, mipangilio ya app, na Bicep/infrastructure.
14. **Kiwango cha chini cha `max_output_tokens` ni 16**: Azure OpenAI hukataa thamani chini ya 16 kwa `400 integer_below_min_value`. Tumia 50 kwa majaribio ya harufu, 1000+ kwa uzalishaji. `max_tokens` ya zamani haikukatika chini kama hii.
15. **`tenant_id` kwa `AzureDeveloperCliCredential`**: Wakati rasilimali ya Azure OpenAI iko kwenye tenant tofauti, lazima upitishe `tenant_id` waziwazi — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Bila hiyo, leseni hutumia tenant isiyo sahihi kimya na kurejesha `401`.
16. **Mipaka ya kiwango hujitokeza tofauti katika utiririshaji**: Kwa Chat Completions, 429 kawaida ilizuia mtiririko kuanza. Kwa utiririshaji wa Responses API, 429 inaweza kutokea katikati ya mtiririko — iterator async hutoa istisnai. Kila mara weka mzunguko wa utiririshaji ndani ya `try/except` na tosha mstari wa JSON la kosa ili frontend iweze kushughulikia kwa upole.

17. **Kushughulikia makosa ya uenezaji ni lazima kwa programu za wavuti**: Mchoro `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` ni muhimu sana. Bila hiyo, mtiririko wa SSE/JSONL unakufa kimya kimya kwa kosa lolote la upande wa seva na mbele ya mtumiaji huganda.
18. **Ufafanuzi wa zana lazima utumie muundo mzito**: API ya Majibu inatarajia `{"type": "function", "name": ..., "parameters": ...}` — si ile inayojumuisha ya Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Hii ni kosa linalojitokeza mara kwa mara wakati wa uhamishaji kwa msimbo wa kuita kazi.
19. **`pydantic_function_tool()` haifanyi kazi**: Msaidizi `openai.pydantic_function_tool()` bado hutengeneza muundo wa zamani uliojumuishwa. Usitumie pamoja na `responses.create()`. Tafsiri mipangilio ya zana kwa mkono au pambanua towe.
20. **Matokeo ya zana hutumia `function_call_output`, si `role: tool`**: Baada ya kutekeleza zana, ongeza `{"type": "function_call_output", "call_id": ..., "output": ...}` — si `{"role": "tool", "tool_call_id": ..., "content": ...}`. Kwa ombi la zana la msaidizi, tumia `messages.extend(response.output)` — si kamusi ya mkono `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` inahitaji `required` + `additionalProperties: false`**: Unapotumia `strict: true` kwenye zana, kila sifa lazima iandikwe kwenye orodha ya `required` na `additionalProperties` iwe `false`. Kukosekana kwa moja kunasababisha kosa la 400.
22. **Vitambulisho vya mwito wa kazi vina vionyesho maalum**: Unapotoa vitu vya `function_call` vya few-shot kwenye `input`, shamba la `id` lazima lianze na `fc_` na shamba la `call_id` liwe na mwanzo wa `call_` (mfano, `"id": "fc_example1", "call_id": "call_example1"`). Kutumia kiambishi cha zamani cha Chat Completions cha `call_` kwa `id` hutupwa.
23. **GitHub Models haitegemezi API ya Majibu**: Ikiwa programu ina njia ya msimbo wa GitHub Models (`base_url` inaonyesha `models.github.ai` au `models.inference.ai.azure.com`), ondoa kabisa. Hakuna njia ya uhamishaji — badilisha kwenda Azure OpenAI, OpenAI, au kiunganishi cha mahali kinacholingana.
24. **Muundo wa mwili wa kosa la kichujio cha maudhui umebadilika**: Makosa ya Chat Completions yalitumia `error.body["innererror"]["content_filter_result"]` (kimoja). Makosa ya API ya Majibu hutumia `error.body["content_filters"][0]["content_filter_results"]` (wingi, ndani ya safu). Mkononi `innererror` haina tena. Msimbo unaoingia moja kwa moja `innererror` utakata `KeyError` wakati wa kuendesha — hii ni rahisi isigundulike wakati wa uhamishaji kwa sababu inaonekana tu pale kichujio cha maudhui kinapoanza. Tafadhali tafuta kila wakati `innererror` wakati wa uhamishaji.
25. **Mawaiti ya moja kwa moja ya HTTP yanahitaji kuandika upya URL + mwili**: Programu zinazoita Azure OpenAI REST moja kwa moja (kupitia `requests`, `httpx`, `aiohttp`) kwa kutumia `/openai/deployments/{name}/chat/completions?api-version=...` lazima zibadilishe kwenda `/openai/v1/responses`. Mwili wa ombi hutumia `input` badala ya `messages`, unahitaji `max_output_tokens` na `store`, na kigezo cha `api-version` kinatupwa. Maandishi ya mwili wa jibu yako katika `output[0].content[0].text` — **si** `output_text`, ambayo ni mali ya msaada wa SDK isiyo katika JSON ya raw REST.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->