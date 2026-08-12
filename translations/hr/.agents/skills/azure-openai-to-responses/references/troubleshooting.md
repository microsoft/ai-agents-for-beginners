# Rješavanje problema, tablica rizika i zamke

## Rješavanje problema s 400-ima

| Pogreška | Popravak |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definicija alata koristi stari ugniježđeni format Chat Completions | Izravnajte iz `{"type": "function", "function": {"name": ...}}` u `{"type": "function", "name": ..., "parameters": ...}` — name, opis, parametri idu na najvišu razinu |
| `unknown_parameter: input[N].tool_calls` | Rezultati alata u višekratnim okretima koriste stari Chat Completions format | Zamijenite `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` sa stavkama `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` alat nedostaje niz `required` | Kada je `strict: true`, sve osobine moraju biti navedene u `required` i mora se postaviti `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` alat nema `additionalProperties: false` | Dodajte `"additionalProperties": false` objektu parametara |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID funkcijskog poziva za few-shot ima pogrešan prefiks | ID-evi funkcijskih poziva moraju počinjati s `fc_` (npr. `fc_example1`), a ne s `call_` |
| `missing_required_parameter: text.format.name` | Dodajte ključ `"name"` u riječnik formata (npr. `"name": "Output"`) |
| `invalid_type: text.format` | Provjerite je li `text.format` riječnik s ključevima `type`, `name`, `strict`, `schema` — a ne string |
| `invalid input content type` | Koristite sadržajne tipove `input_text`/`output_text` umjesto Chat `text` |
| `invalid input content type` (slika) | Tip sadržaja slike još koristi `"type": "image_url"` | Promijenite u `"type": "input_image"` |
| `Expected object, got string` na `image_url` | `image_url` je još uvijek ugniježđeni objekt `{"url": "..."}` | Izravnajte u običan string: `"image_url": "https://..."` ili `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` za `max_output_tokens` | Minimum je **16** na Azure OpenAI. Koristite 50+ za testove, 1000+ za produkciju. |
| `429 Too Many Requests` tijekom streaminga | Ograničenje frekvencije. Omotajte streaming u `try/except`, pošaljite JSON pogreške frontend-u, implementirajte povratak/pokušaj ponovo. |
| `KeyError: 'innererror'` kod pogreške filtera sadržaja | Struktura tijela pogreške filtera sadržaja promijenjena u Responses API | Chat Completions je koristio `error.body["innererror"]["content_filter_result"]`; Responses API koristi `error.body["content_filters"][0]["content_filter_results"]` (množina, unutar niza). Prepišite sav pristup `innererror`. |

---

## Tablica rizika migracije

| Simptom | Vjerojatna greška | Popravak |
|---------|---------------|-----|
| Prazan `output_text` / skraćeni odgovor | `max_output_tokens` prenizak za modele rezoniranja | Postavite `max_output_tokens=1000` ili više — rezonantni tokeni se računaju u limit |
| `400 invalid_type: text.format` | Proslijeđen `response_format` string umjesto `text.format` riječnika | Koristite `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` na `/openai/v1/responses` | Pogrešan `base_url` — nedostaje sufiks `/openai/v1/` | Osigurajte `base_url=f"{endpoint}/openai/v1/"` (s završnim kosim crtom) |
| `401 Unauthorized` nakon prelaska na `OpenAI()` | `api_key` nije postavljen ili token provider nije ispravno proslijeđen | Za EntraID: `api_key=token_provider` (pozivna funkcija). Za API ključ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model vraća `deployment not found` | `model` parametar ne odgovara nazivu vašeg Azure deploymenta | Koristite `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — to je naziv deploymenta, ne modela |
| `json.loads(resp.output_text)` baca `JSONDecodeError` | Šema nije nametnuta ili model ne podržava striktni JSON | Osigurajte `"strict": True` u šemi, i provjerite podršku modela za strukturirani izlaz |
| Streaming ne daje `delta` događaje | Provjerava se pogrešan tip događaja | Filtrirajte na `event.type == "response.output_text.delta"`, a ne na Chat `chat.completion.chunk` |
| `400` pogreška na ulaz slike nakon migracije | Tip sadržaja slike nije ažuriran | Promijenite `"type": "image_url"` → `"type": "input_image"` i izravnajte `"image_url": {"url": "..."}` → `"image_url": "..."` (obični string) |
| Alat poziva beskonačno petljanje | Nedostaje rezultat alata u sljedećem `input` | Nakon pokretanja alata, dodajte stavku `{"type": "function_call_output", "call_id": ..., "output": ...}` u `input` u sljedećem zahtjevu |
| Pogreška `temperature` s GPT-5 ili o-serijom | Izričita vrijednost `temperature` različita od 1 | Uklonite `temperature` ili postavite na `1` za GPT-5 i o-seriju modele (o1, o3-mini, o3, o4-mini) |
| Pogreška `top_p` s o-serijom | `top_p` nije podržan | Uklonite `top_p` kod ciljanih o-serija modela |
| `max_completion_tokens` nije prepoznat | Korištenje Azure-specifičnog parametra | Zamijenite `max_completion_tokens` s `max_output_tokens`. Postavite na 4096+ za o-seriju (rezonantni tokeni se računaju). |
| Prazan/skraćeni izlaz iz o-serije | `max_output_tokens` prenizak | O-serija koristi rezonantne tokene interno. Postavite `max_output_tokens=4096` ili više — ne 500–1000. |
| `400 integer_below_min_value` za `max_output_tokens` | Vrijednost ispod 16 | Azure OpenAI nameće `max_output_tokens >= 16`. Koristite 50+ za testove, 1000+ za produkciju. |
| `429 Too Many Requests` usred streama | Ograničenje frekvencije od Azure OpenAI | Stream se tiho prekida bez rukovanja greškom. Uvijek omotajte `async for event in await coroutine:` u `try/except` i pošaljite `{"error": str(e)}` frontendu. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Pogrešan tenant ili nije prijavljen | Proslijedite `tenant_id=os.getenv("AZURE_TENANT_ID")` eksplicitno. Pokrenite `azd auth login --tenant <tenant-id>` lokalno. |
| `404 Not Found` korištenjem GitHub modela (`models.github.ai`) | GitHub modeli ne podržavaju Responses API | Uklonite potpuno GitHub modele iz koda. Koristite Azure OpenAI, OpenAI, ili kompatibilni lokalni endpoint (npr. Ollama s podrškom za Responses). |
| MAF `OpenAIChatCompletionClient` još koristi Chat Completions | Korištenje legacy MAF klijenta u 1.0.0+ verziji | U MAF 1.0.0+, `OpenAIChatClient` po defaultu koristi Responses API. Zamijenite `OpenAIChatCompletionClient` s `OpenAIChatClient`. Za verzije prije 1.0.0, nadogradite na `agent-framework-openai>=1.0.0`. |
| LangChain agent vraća prazan ili neuspješan ishod s pozivima alata | `ChatOpenAI` ne koristi Responses API | Dodajte `use_responses_api=True` u `ChatOpenAI(...)`. Također promijenite `.content` → `.text` na porukama odgovora. |
| `KeyError: 'innererror'` u handleru pogreške filtera sadržaja | Struktura tijela pogreške promijenjena u Responses API | Prepišite `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Wrapper `innererror` je uklonjen; detalji filtera sadržaja sada su u vrhovnom nizu `content_filters` sa `content_filter_results` (množina) u svakoj stavci. |
| Sirovi HTTP poziv na `/openai/deployments/.../chat/completions` vraća 404 | Stari Chat Completions REST endpoint | Prepišite URL na `/openai/v1/responses`. Promijenite tijelo zahtjeva: `messages` → `input`, dodajte `max_output_tokens` + `store: false`, uklonite query parametar `api-version`. Promijenite parsiranje odgovora: `choices[0].message.content` → `output[0].content[0].text` (napomena: `output_text` je svojstvo SDK-a, nije u sirovom REST JSON-u). |

---

## Zamke

1. Ako ste ranije koristili Chat Completions za stanje razgovora, sada upravljajte vlastitim stanjem eksplicitno uz Responses.
2. Preferirajte `max_output_tokens` umjesto legacy `max_tokens`.
3. Prilikom migracije na `gpt-5`, osigurajte da `temperature` nije specificirana ili da je postavljena na `1`.
4. Zamijenite Chat `content[].type: "text"` s Responses `content[].type: "input_text"` za korisničke/sistemske ulaze.
5. Za `text.format`, navedite odgovarajući riječnik (npr. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), a ne običan string.
6. Parametar `seed` nije podržan u Responses; uklonite ga iz zahtjeva.
7. **Rezoniranje**: Uključujte `reasoning` samo ako je originalni kod to već koristio. Nemojte dodavati `reasoning` u API pozive koji ga nisu imali — mnogi modeli bez rezoniranja ne podržavaju ovaj parametar.
8. **Veličina `max_output_tokens`**: Za modele rezoniranja (GPT-5-mini, GPT-5, o-serija) koristite `max_output_tokens=4096` ili više — ne 50–1000. Model interno koristi rezonantne tokene prije generiranja vidljivog izlaza; premali limiti uzrokuju skraćene ili prazne odgovore.
9. **O-serija `max_completion_tokens`**: Ako originalni kod koristi `max_completion_tokens` (Azure-specifično za o-seriju), zamijenite s `max_output_tokens`. Responses API ne prihvaća `max_completion_tokens`.
10. **O-serija `reasoning_effort`**: Ako originalni kod koristi `reasoning_effort` (low/medium/high), migrirajte ga u `reasoning={"effort": "<vrijednost>"}` u pozivu Responses API-ja.
11. **Kašnjenje kod streaminga o-serije**: O-serija modeli vrše interno rezoniranje prije generiranja izlaza. Kod streaminga očekujte dulje kašnjenje do prvog `response.output_text.delta` događaja. To je normalno — model rezonira, ne kuka.
9. **`_azure_ad_token_provider` je uklonjen**: `AsyncOpenAI` / `OpenAI` nemaju `_azure_ad_token_provider` atribut. Testovi ili kod koji pristupaju ovom atributu će baciti `AttributeError`. Token provider se prosljeđuje kao `api_key` i nije dostupan za inspekciju na klijentskom objektu.
10. **Snapshot / zlatne datoteke**: Ako testni skup koristi snapshot testiranje, **sve** snapshot datoteke koje sadrže Chat Completions streaming obrasce (`choices[0]`, `content_filter_results`, `function_call`, itd.) moraju se ažurirati na novi oblik Responses. Ovo je lako propustiti i uzrokuje pogreške u provjeri snapshot-a.
11. **Putanja za mock monkeypatch**: Cilj monkeypatch-a mijenja se s `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ili `Responses.create` za sinkroni). Korištenje stare putanje tiho neće raditi — mock neće presresti pozive i testovi će koristiti stvarni API ili pasti.
12. **`input` umjesto `messages`**: Mock funkcije moraju čitati `kwargs.get("input")` a ne `kwargs.get("messages")`. Responses API koristi `input` za povijest razgovora.
13. **Nazivi varijabli okoline**: Azure Identity SDK koristi `AZURE_CLIENT_ID` (ne `AZURE_OPENAI_CLIENT_ID`) za `ManagedIdentityCredential(client_id=...)`. Preimenujte u testovima, `.env` datotekama, postavkama aplikacije i Bicep/infra.
14. **Minimalna vrijednost `max_output_tokens` je 16**: Azure OpenAI odbacuje vrijednosti ispod 16 s `400 integer_below_min_value`. Koristite `50` za testove dima, `1000`+ za produkciju. Stari `max_tokens` nije imao takav minimum.
15. **`tenant_id` za `AzureDeveloperCliCredential`**: Kad je Azure OpenAI resurs u drugom tenant-u, morate eksplicitno proslijediti `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Bez toga, vjerodajnica tiho koristi pogrešan tenant i vraća `401`.
16. **Ograničenja frekvencije se drugačije pojavljuju u streamingu**: S Chat Completions, 429 je obično sprječavao početak streama. S Responses API streamingom, 429 može se dogoditi **usred streama** — async iterator baca iznimku. Uvijek omotajte streaming petlju u `try/except` i pošaljite JSON liniju s pogreškom kako bi frontend mogao elegantno rukovati. 

17. **Obrada pogrešaka u streamingu obavezna je za web aplikacije**: Uzorak `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` je ključan. Bez njega SSE/JSONL stream tiho prestaje raditi pri bilo kojoj pogrešci na strani servera i frontend se zamrzava.
18. **Definicije alata moraju koristiti ravni format**: Responses API očekuje `{"type": "function", "name": ..., "parameters": ...}` — a ne ugniježđeni Chat Completions format `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Ovo je najčešća pogreška migracije za kod koji poziva funkcije.
19. **`pydantic_function_tool()` nije kompatibilan**: Pomoćna funkcija `openai.pydantic_function_tool()` još uvijek generira stari ugniježđeni format. Nemojte je koristiti s `responses.create()`. Definirajte sheme alata ručno ili izravnajte izlaz.
20. **Rezultati alata koriste `function_call_output`, a ne `role: tool`**: Nakon izvršavanja alata, dodajte `{"type": "function_call_output", "call_id": ..., "output": ...}` — a ne `{"role": "tool", "tool_call_id": ..., "content": ...}`. Za zahtjev asistenta za alat, koristite `messages.extend(response.output)` — a ne ručno `{"role": "assistant", "tool_calls": [...]}` rječnik.
21. **`strict: true` zahtijeva `required` + `additionalProperties: false`**: Kada koristite `strict: true` na alatu, svaka svojstvo mora biti navedeno u polju `required` i `additionalProperties` mora biti `false`. Nedostatak bilo kojeg uzrokuje 400 pogrešku.
22. **ID-ovi poziva funkcija imaju specifične prefikse**: Kada pružate nekoliko primjera `function_call` stavki u `input`, polje `id` mora započinjati s `fc_`, a polje `call_id` mora započinjati s `call_` (npr. `"id": "fc_primjer1", "call_id": "call_primjer1"`). Korištenje starog Chat Completions prefiksa `call_` za `id` odbija se.
23. **GitHub Models ne podržava Responses API**: Ako aplikacija ima GitHub Models kodni put (`base_url` usmjeren na `models.github.ai` ili `models.inference.ai.azure.com`), u potpunosti ga uklonite. Nema puta migracije — pređite na Azure OpenAI, OpenAI ili kompatibilnu lokalnu krajnju točku.
24. **Struktura tijela pogreške filtera sadržaja promijenjena**: Pogreške Chat Completions koristile su `error.body["innererror"]["content_filter_result"]` (jednina). Pogreške Responses API koriste `error.body["content_filters"][0]["content_filter_results"]` (množina, unutar polja). Ključ `innererror` više ne postoji. Kod koji direktno pristupa `innererror` će tijekom izvođenja podići `KeyError` — lako se može previdjeti u migraciji jer se pojavljuje samo kad se filter sadržaja stvarno aktivira. Uvijek pretražite `innererror` tijekom migracije.
25. **Sirovi HTTP pozivi zahtijevaju prepisivanje URL-a i tijela**: Aplikacije koje pozivaju Azure OpenAI REST izravno (putem `requests`, `httpx`, `aiohttp`) koristeći `/openai/deployments/{name}/chat/completions?api-version=...` moraju prijeći na `/openai/v1/responses`. Tijelo zahtjeva koristi `input` umjesto `messages`, zahtijeva `max_output_tokens` i `store`, a query parametar `api-version` se uklanja. Tekst tijela odgovora nalazi se u `output[0].content[0].text` — **ne** u `output_text`, koji je SDK-ova pomoćna svojstva i nije prisutan u sirovom REST JSON-u.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->