# Otklanjanje poteškoća, Tablica rizika i Zamke

## Otklanjanje poteškoća s kodovima 400

| Pogreška | Popravak |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definicija alata koristi stari ugniježđeni format Chat Completions | Pretvorite iz `{"type": "function", "function": {"name": ...}}` u `{"type": "function", "name": ..., "parameters": ...}` — ime, opis i parametri idu na najvišu razinu |
| `unknown_parameter: input[N].tool_calls` | Rezultati alata za više okretaja koriste stari format Chat Completions | Zamijenite `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` s `response.output` stavkama + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` alat nema polje `required` | Kada je `strict: true`, sve osobine moraju biti navedene u `required`, a `additionalProperties: false` mora biti postavljeno |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` alat nema `additionalProperties: false` | Dodajte `"additionalProperties": false` u objekt parametara |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID za funkcijski poziv kod Few-shot ima pogrešan prefiks | ID-jevi funkcijskih poziva moraju počinjati s `fc_` (npr. `fc_example1`), a ne s `call_` |
| `missing_required_parameter: text.format.name` | Dodajte ključ `"name"` u format dict (npr. `"name": "Output"`) |
| `invalid_type: text.format` | Provjerite da je `text.format` dict s ključevima `type`, `name`, `strict`, `schema` — ne string |
| `invalid input content type` | Koristite tipove sadržaja `input_text`/`output_text` umjesto Chat `text` |
| `invalid input content type` (slika) | Tip sadržaja slike još koristi `"type": "image_url"` | Promijenite u `"type": "input_image"` |
| `Expected object, got string` na `image_url` | `image_url` je još u obliku ugniježđenog objekta `{"url": "..."}` | Pretvorite u običan string: `"image_url": "https://..."` ili `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` za `max_output_tokens` | Minimalna vrijednost je **16** na Azure OpenAI. Koristite 50+ za testove, 1000+ za produkciju. |
| `429 Too Many Requests` tijekom streamanja | Ograničenje brzine. Omotajte stream u `try/except`, pošaljite JSON grešku frontend-u, implementirajte backoff/retry. |
| `KeyError: 'innererror'` na greški filtra sadržaja | Strukturirano tijelo greške filtra sadržaja je promijenjeno u Responses API | Chat Completions je koristio `error.body["innererror"]["content_filter_result"]`; Responses API koristi `error.body["content_filters"][0]["content_filter_results"]` (u množini, unutar niza). Izmijenite sva pristupanja `innererror`. |

---

## Tablica rizika migracije

| Simptom | Vjerojatna pogreška | Popravak |
|---------|---------------|-----|
| Prazan `output_text` / skraćeni odgovor | `max_output_tokens` prenizak za modele sa zaključivanjem | Postavite `max_output_tokens=1000` ili više — tokeni za zaključivanje se računaju u ograničenje |
| `400 invalid_type: text.format` | Proslijeđen je string `response_format` umjesto dict `text.format` | Koristite `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` na `/openai/v1/responses` | Pogrešan `base_url` — nedostaje `/openai/v1/` na kraju | Provjerite `base_url=f"{endpoint}/openai/v1/"` (s kosom crtom na kraju) |
| `401 Unauthorized` nakon prelaska na `OpenAI()` | `api_key` nije postavljen ili token provider nije pravilno proslijeđen | Za EntraID: `api_key=token_provider` (pozivajući objekt). Za API ključ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model vraća `deployment not found` | Parametar `model` ne odgovara imenu Vaše Azure implementacije | Koristite `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — to je ime implementacije, ne modela |
| `json.loads(resp.output_text)` baca `JSONDecodeError` | Shema nije prisiljena ili model ne podržava striktni JSON | Osigurajte `"strict": True` u shemi i provjerite da model podržava strukturirani izlaz |
| Streaming ne vraća `delta` događaje | Provjera pogrešnog tipa događaja | Filtrirajte događaje na `event.type == "response.output_text.delta"`, ne na Chat `chat.completion.chunk` |
| `400` greška na unos slike nakon migracije | Tip sadržaja slike nije ažuriran | Promijenite `"type": "image_url"` → `"type": "input_image"` i izravnajte `"image_url": {"url": "..."}` → `"image_url": "..."` (obični string) |
| Pozivi alata se beskonačno ponavljaju | Nedostaje rezultat alata u sljedećem `input` | Nakon izvršenja alata, dodajte stavku `{"type": "function_call_output", "call_id": ..., "output": ...}` u `input` u sljedećem zahtjevu |
| Greška `temperature` s GPT-5 ili o-serijom | Izričita vrijednost `temperature` različita od 1 | Uklonite `temperature` ili postavite na `1` za GPT-5 i o-seriju (o1, o3-mini, o3, o4-mini) |
| `top_p` greška s o-serijom | `top_p` nije podržan | Uklonite `top_p` kad ciljate o-seriju |
| `max_completion_tokens` nije prepoznat | Korištenje Azure-specifičnog parametra | Zamijenite `max_completion_tokens` s `max_output_tokens`. Postavite na 4096+ za o-seriju (tokeni završnog zaključivanja se računaju za limit). |
| Prazan/skraćeni izlaz iz o-serije | `max_output_tokens` prenizak | O-serija koristi interne tokene za zaključivanje. Postavite `max_output_tokens=4096` ili više — ne 500–1000. |
| `400 integer_below_min_value` za `max_output_tokens` | Vrijednost ispod 16 | Azure OpenAI zahtijeva `max_output_tokens >= 16`. Koristite 50+ za testove, 1000+ za produkciju. |
| `429 Too Many Requests` usred streamanja | Ograničenje brzine od Azure OpenAI | Stream se prekida tiho bez error handlinga. Uvijek omotajte `async for event in await coroutine:` u `try/except` i pošaljite `{"error": str(e)}` frontend-u. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Pogrešan tenant ili niste prijavljeni | Proslijedite `tenant_id=os.getenv("AZURE_TENANT_ID")` eksplicitno. Pokrenite `azd auth login --tenant <tenant-id>` lokalno. |
| `404 Not Found` koristeći GitHub modele (`models.github.ai`) | GitHub modeli ne podržavaju Responses API | Uklonite potpuno kod za GitHub modele. Koristite Azure OpenAI, OpenAI ili kompatibilan lokalni endpoint (npr. Ollama s podrškom za Responses). |
| MAF `OpenAIChatCompletionClient` još koristi Chat Completions | Korištenje legacy MAF klijenta u 1.0.0+ | U MAF 1.0.0+, `OpenAIChatClient` koristi Responses API po defaultu. Zamijenite `OpenAIChatCompletionClient` s `OpenAIChatClient`. Za verzije prije 1.0.0, nadogradite na `agent-framework-openai>=1.0.0`. |
| LangChain agent vraća prazan odgovor ili ne uspijeva s pozivima alata | `ChatOpenAI` ne koristi Responses API | Dodajte `use_responses_api=True` u `ChatOpenAI(...)`. Također promijenite `.content` → `.text` na odgovorima poruka. |
| `KeyError: 'innererror'` u handleru greške filtra sadržaja | Strukturirano tijelo greške promijenjeno u Responses API | Prepišite `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` omot je uklonjen; detalji filtra sadržaja sada su u vrhu u nizu `content_filters` s `content_filter_results` (množina) u svakom unosu. |
| Osnovni HTTP poziv na `/openai/deployments/.../chat/completions` vraća 404 | Stari REST endpoint za Chat Completions | Prepišite URL na `/openai/v1/responses`. Promijenite tijelo zahtjeva: `messages` → `input`, dodajte `max_output_tokens` + `store: false`, uklonite query parametar `api-version`. Promijenite parsiranje odgovora: `choices[0].message.content` → `output[0].content[0].text` (napomena: `output_text` je svojstvo SDK-a, nema ga u izvornom REST JSON-u). |

---

## Zamke

1. Ako ste prethodno koristili Chat Completions za stanje razgovora, upravljajte vlastitim stanjem eksplicitno s Responses.
2. Preferirajte `max_output_tokens` umjesto legacy `max_tokens`.
3. Kod migracije na `gpt-5`, osigurajte da `temperature` nije specificirana ili je postavljena na `1`.
4. Zamijenite Chat `content[].type: "text"` sa Responses `content[].type: "input_text"` za korisničke/sistemske unose.
5. Za `text.format` dostavite ispravan dict (npr. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ne običan string.
6. Parametar `seed` nije podržan u Responses; uklonite ga iz zahtjeva.
7. **Razmišljanje**: Uključite `reasoning` samo ako ga je originalni kod već koristio. Nemojte dodavati `reasoning` u API pozive koji ga nisu imali — mnogi modeli (npr. gpt-4o-mini) ne podržavaju taj parametar.
8. **Dimenzioniranje `max_output_tokens`**: Za modele za zaključivanje (GPT-5-mini, GPT-5, o-serija), koristite `max_output_tokens=4096` ili više — ne 50–1000. Model koristi tokene za zaključivanje interno prije generiranja vidljivog izlaza; preniski limiti uzrokuju skraćene ili prazne odgovore.
9. **O-serija `max_completion_tokens`**: Ako je originalni kod koristio `max_completion_tokens` (Azure-specifično za o-seriju), zamijenite s `max_output_tokens`. Responses API ne prihvaća `max_completion_tokens`.
10. **O-serija `reasoning_effort`**: Ako originalni kod koristi `reasoning_effort` (low/medium/high), migrirajte ga u `reasoning={"effort": "<vrijednost>"}` u Responses API pozivu.
11. **O-serija kašnjenje kod streamanja**: O-serija modeli izvode unutarnje zaključivanje prije generiranja izlaza. Kod streamanja očekujte duže čekanje prije prvog `response.output_text.delta` događaja. To je normalno — model razmišlja, nije zapeo.
9. **`_azure_ad_token_provider` je uklonjen**: `AsyncOpenAI` / `OpenAI` nemaju atribut `_azure_ad_token_provider`. Testovi ili kod koji pristupa ovom atributu će odustati s `AttributeError`. Token provider se prosljeđuje kao `api_key` i nije dostupan za inspekciju na objektu klijenta.
10. **Snapshot / zlatne datoteke**: Ako testni paket koristi snapshot testiranje, **sve** snapshot datoteke koje sadrže oblike Chat Completions streaming-a (`choices[0]`, `content_filter_results`, `function_call` itd.) moraju biti ažurirane na novi oblik Responses. Ovo je lako propustiti i uzrokuje neuspjehe u asertacijama snapshot-a.
11. **Putanje za mocking monkeypatch**: Cilj za monkeypatch se mijenja s `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ili `Responses.create` za sinkroni kod). Korištenje stare putanje ne radi tiho — mock se neće uhvatiti i testovi će koristiti stvarni API ili pasti.
12. **`input` umjesto `messages`**: Mock funkcije moraju čitati `kwargs.get("input")` ne `kwargs.get("messages")`. Responses API koristi `input` za povijest razgovora.
13. **Nazivi varijabli okoline**: Azure Identity SDK koristi `AZURE_CLIENT_ID` (ne `AZURE_OPENAI_CLIENT_ID`) za `ManagedIdentityCredential(client_id=...)`. Preimenujte u testovima, `.env` datotekama, postavkama aplikacije i Bicep/infrastrukturi.
14. **Minimalna vrijednost `max_output_tokens` je 16**: Azure OpenAI odbija vrijednosti ispod 16 s `400 integer_below_min_value`. Koristite `50` za testove, `1000`+ za produkciju. Stari `max_tokens` nije imao takvu minimalnu vrijednost.
15. **`tenant_id` za `AzureDeveloperCliCredential`**: Kada je Azure OpenAI resurs u drugom tenant-u, morate eksplicitno proslijediti `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Bez toga, credential tiho koristi pogrešan tenant i vraća `401`.
16. **Ograničenja brzine se drugačije pojavljuju u streamanju**: Kod Chat Completions, 429 je obično spriječio pokretanje streama. Kod Responses API streamanja, 429 se može dogoditi **usred streama** — asinhroni iterator baca iznimku. Uvijek omotajte petlju streamanja u `try/except` i pošaljite JSON liniju s greškom kako bi frontend mogao hijematski obraditi grešku.

17. **Rukovanje greškama tijekom streaminga je obavezno za web aplikacije**: Uzorak `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` je kritičan. Bez njega SSE/JSONL stream tiho prestaje raditi na bilo kojoj grešci na strani servera i frontend se zamrzava.
18. **Definicije alata moraju koristiti ravni format**: Responses API očekuje `{"type": "function", "name": ..., "parameters": ...}` — ne ugniježđeni format za Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Ovo je najčešća greška pri migraciji koda za pozivanje funkcija.
19. **`pydantic_function_tool()` nije kompatibilan**: `openai.pydantic_function_tool()` pomoćnik još uvijek generira stari ugniježđeni format. Nemojte ga koristiti s `responses.create()`. Definirajte sheme alata ručno ili poravnajte izlaz.
20. **Rezultati alata koriste `function_call_output`, a ne `role: tool`**: Nakon izvršenja alata dodajte `{"type": "function_call_output", "call_id": ..., "output": ...}` — ne `{"role": "tool", "tool_call_id": ..., "content": ...}`. Za zahtjev asistenta za alat koristite `messages.extend(response.output)` — ne ručni rječnik `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` zahtijeva `required` + `additionalProperties: false`**: Kada koristite `strict: true` na alatu, svako svojstvo mora biti navedeno u nizu `required` i `additionalProperties` mora biti `false`. Nedostatak bilo kojeg od ovih uzrokuje 400 grešku.
22. **ID-ovi poziva funkcije imaju specifične prefikse**: Kada se u `input` daju few-shot `function_call` stavke, polje `id` mora početi s `fc_` a polje `call_id` mora početi s `call_` (npr. `"id": "fc_example1", "call_id": "call_example1"`). Korištenje starog Chat Completions prefiksa `call_` za `id` je odbijeno.
23. **GitHub Models ne podržava Responses API**: Ako aplikacija ima GitHub Models put koda (`base_url` usmjeren na `models.github.ai` ili `models.inference.ai.azure.com`), u potpunosti ga uklonite. Ne postoji put migracije — prebacite se na Azure OpenAI, OpenAI ili kompatibilnu lokalnu krajnju točku.
24. **Struktura tijela greške content filtera se promijenila**: Chat Completions greške su koristile `error.body["innererror"]["content_filter_result"]` (jednina). Responses API greške koriste `error.body["content_filters"][0]["content_filter_results"]` (množina, unutar niza). Ključ `innererror` više ne postoji. Kod koji direktno pristupa `innererror` će podići `KeyError` prilikom izvođenja — lako je to propustiti pri migraciji jer se pojavljuje samo kad content filter zaista reagira. Uvijek pretražujte za `innererror` tijekom migracije.
25. **Raw HTTP pozivi zahtijevaju prepravljanje URL-a i tijela zahtjeva**: Aplikacije koje pozivaju Azure OpenAI REST direktno (putem `requests`, `httpx`, `aiohttp`) koristeći `/openai/deployments/{name}/chat/completions?api-version=...` moraju prijeći na `/openai/v1/responses`. Tijelo zahtjeva koristi `input` umjesto `messages`, zahtijeva `max_output_tokens` i `store`, a query parametar `api-version` se uklanja. Tekst tijela odgovora je na `output[0].content[0].text` — **ne** `output_text`, koji je SDK sigurnosna pogodnost i nije prisutan u sirovom REST JSON-u.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->