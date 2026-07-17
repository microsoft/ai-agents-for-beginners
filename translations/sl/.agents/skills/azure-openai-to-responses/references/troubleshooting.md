# Odpravljanje težav, tabela tveganj in pasti

## Odpravljanje težav s 400 napakami

| Napaka | Popravek |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definicija orodja uporablja staro, znotraj gnezdeno obliko Chat Completions | Pretvorite iz `{"type": "function", "function": {"name": ...}}` v `{"type": "function", "name": ..., "parameters": ...}` — ime, opis, parametri morajo biti na najvišji ravni |
| `unknown_parameter: input[N].tool_calls` | Rezultati večkrožnih klicev orodij uporabljajo staro obliko Chat Completions | Zamenjajte `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` z elementi `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Pri orodju z `strict: true` manjka polje `required` | Če je `strict: true`, morajo biti vse lastnosti navedene v `required` in nastavljeno mora biti `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Pri orodju z `strict: true` manjka `additionalProperties: false` | Dodajte `"additionalProperties": false` v objekt parametrov |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID funkcijskega klica večstrežnega načina ima napačen predpono | ID-ji funkcijskih klicev morajo začeti z `fc_` (npr. `fc_example1`), ne z `call_` |
| `missing_required_parameter: text.format.name` | Dodajte ključ `"name"` v slovar formata (npr. `"name": "Output"`) |
| `invalid_type: text.format` | Prepričajte se, da je `text.format` slovar s ključi `type`, `name`, `strict`, `schema` — ne niz |
| `invalid input content type` | Namesto Chat `text` uporabite vsebinske tipe `input_text`/`output_text` |
| `invalid input content type` (slika) | Vsebinski tip slike še vedno uporablja `"type": "image_url"` | Spremenite v `"type": "input_image"` |
| `Expected object, got string` na `image_url` | `image_url` je še vedno gnezden objekt `{"url": "..."}` | Pretvorite v navaden niz: `"image_url": "https://..."` ali `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` za `max_output_tokens` | Minimum je **16** pri Azure OpenAI. Za teste uporabite 50+, za produkcijo 1000+. |
| `429 Too Many Requests` med pretakanjem | Omejitev hitrosti. Ovitje pretakanja v `try/except`, na sprednji del pošljite JSON z napako, izvedite ponovni poskus / čakanje. |
| `KeyError: 'innererror'` na napaki filtra vsebine | Struktura telesa napake filtra vsebine se je spremenila v Responses API | Chat Completions je uporabil `error.body["innererror"]["content_filter_result"]`; Responses API uporablja `error.body["content_filters"][0]["content_filter_results"]` (v množini, znotraj tabele). Prepišite vse dostope do `innererror`. |

---

## Tabela tveganj pri migraciji

| Simptom | Verjetna napaka | Popravek |
|---------|---------------|-----|
| Prazen `output_text` / skrajšan odziv | `max_output_tokens` prenizek za modele za zaključevanje razmišljanja | Nastavite `max_output_tokens=1000` ali več — število zaključnih tokenov šteje v omejitev |
| `400 invalid_type: text.format` | Posredovan nizek `response_format` namesto slovarja `text.format` | Uporabite `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` na `/openai/v1/responses` | Napačen `base_url` — manjka `/openai/v1/` na koncu | Poskrbite, da je `base_url=f"{endpoint}/openai/v1/"` (s končnim poševnikom) |
| `401 Unauthorized` po prehodu na `OpenAI()` | `api_key` ni nastavljen ali je posredovan nepravilen token provider | Za EntraID: `api_key=token_provider` (klicni objekt). Za API ključ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model vrne `deployment not found` | Parameter `model` ne ustreza imenu vaše Azure namestitve | Uporabite `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — to je ime namestitve, ne ime modela |
| `json.loads(resp.output_text)` sproži `JSONDecodeError` | Shema ni prisiljena ali model ne podpira strogega JSON | Poskrbite za `"strict": True` v shemi in preverite, da model podpira strukturirane izhode |
| Pretakanje ne vrne nobenih dogodkov `delta` | Preverjanje napačnega tipa dogodka | Filtrirajte po `event.type == "response.output_text.delta"`, ne po Chat `chat.completion.chunk` |
| Napaka 400 na sliki po migraciji | Vsebinski tip slike ni posodobljen | Spremenite `"type": "image_url"` → `"type": "input_image"` in razširite `"image_url": {"url": "..."}` → `"image_url": "..."` (navaden niz) |
| Klici orodij se neskončno ponavljajo | Manjka rezultat orodja v nadaljnem `input` | Po izvedbi orodja dodajte element `{"type": "function_call_output", "call_id": ..., "output": ...}` v `input` v naslednji zahtevi |
| Napaka pri `temperature` z GPT-5 ali o-serijo | Izrecna vrednost `temperature` drugačna od 1 | Odstranite `temperature` ali nastavite na `1` za GPT-5 in modele o-serije (o1, o3-mini, o3, o4-mini) |
| Napaka `top_p` z o-serijo | `top_p` ni podprt | Odstranite `top_p`, če ciljate modele o-serije |
| `max_completion_tokens` ni prepoznan | Uporaba parametra specifičnega za Azure | Zamenjajte `max_completion_tokens` z `max_output_tokens`. Nastavite na 4096+ za o-serijo (zaključevalni tokeni štejejo v omejitev). |
| Prazen ali skrajšan izhod o-serije | `max_output_tokens` prenizek | O-serija uporablja notranje zaključne tokene. Nastavite `max_output_tokens=4096` ali več — ne 500–1000. |
| `400 integer_below_min_value` za `max_output_tokens` | Vrednost pod 16 | Azure OpenAI zahteva `max_output_tokens >= 16`. Za osnovne teste uporabite 50+, za produkcijo 1000+. |
| `429 Too Many Requests` sredi pretakanja | Ograjenost s strani Azure OpenAI | Tok poteka tiho prekine brez upravljanja napake. Vedno ovijte `async for event in await coroutine:` v `try/except` in sprednjemu delu pošljite `{"error": str(e)}`. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Napačen najemnik (tenant) ali niste prijavljeni | Izrecno posredujte `tenant_id=os.getenv("AZURE_TENANT_ID")`. Lokalno zaženite `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` pri uporabi GitHub Modelov (`models.github.ai`) | GitHub Models ne podpira Responses API | Popolnoma odstranite pot kode za GitHub Models. Uporabite Azure OpenAI, OpenAI ali lokalni kompatibilen konektor (npr. Ollama z podporo Responses). |
| MAF `OpenAIChatCompletionClient` še vedno uporablja Chat Completions | Uporaba starega MAF klienta v verziji 1.0.0+ | V MAF 1.0.0+ `OpenAIChatClient` privzeto uporablja Responses API. Zamenjajte `OpenAIChatCompletionClient` z `OpenAIChatClient`. Za verzije pod 1.0.0 nadgradite na `agent-framework-openai>=1.0.0`. |
| Agent LangChain vrača prazen ali ne uspe s klici orodij | `ChatOpenAI` ne uporablja Responses API | Dodajte `use_responses_api=True` v `ChatOpenAI(...)`. Spremenite tudi `.content` → `.text` v odzivnih sporočilih. |
| `KeyError: 'innererror'` v upravljalniku napak filtra vsebine | Struktura telesa napake se je spremenila v Responses API | Prepišite `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Ovijalec `innererror` je odstranjen; podrobnosti filtra vsebine so zdaj v tabeli na vrhnji ravni `content_filters` s poljem `content_filter_results` (v množini) v vsakem zapisu. |
| Neposredni HTTP klic na `/openai/deployments/.../chat/completions` vrne 404 | Stari REST endpoint za Chat Completions | Prepišite URL v `/openai/v1/responses`. Spremenite telo zahteve: `messages` → `input`, dodajte `max_output_tokens` + `store: false`, odstranite poizvedovalni parameter `api-version`. Spremenite razčlenjevanje odgovora: `choices[0].message.content` → `output[0].content[0].text` (upoštevajte: `output_text` je priročna lastnost SDK, ni v surovem REST JSON). |

---

## Pasti

1. Če ste prej uporabljali Chat Completions za stanje pogovora, upravljajte stanje sami eksplicitno z Responses.
2. Raje uporabite `max_output_tokens` kot starejši `max_tokens`.
3. Pri prehodu na `gpt-5` zagotovite, da `temperature` ni določena ali je nastavljena na `1`.
4. Zamenjajte Chat `content[].type: "text"` z Responses `content[].type: "input_text"` za uporabniške / sistemske vnose.
5. Za `text.format` uporabite pravi slovar (npr. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ne navaden niz.
6. Parameter `seed` ni podprt v Responses; odstranite ga iz zahtev.
7. **Razmišljanje**: `reasoning` vključite le, če ga je originalna koda že uporabljala. Ne dodajajte `reasoning` v klice API, ki ga niso imeli — veliko modelov brez razmišljanja tega ne podpira.
8. **Velikost `max_output_tokens`**: Za modele za zaključevanje razmišljanja (GPT-5-mini, GPT-5, o-serija) uporabite `max_output_tokens=4096` ali več — ne 50–1000. Model uporablja notranje zaključne tokene pred generiranjem vidnega izhoda; prenizke omejitve povzročijo skrajšane ali prazne odgovore.
9. **O-serija `max_completion_tokens`**: Če je originalna koda uporabljala `max_completion_tokens` (specifično za Azure o-serijo), ga nadomestite z `max_output_tokens`. Responses API ne sprejema `max_completion_tokens`.
10. **O-serija `reasoning_effort`**: Če originalna koda uporablja `reasoning_effort` (nizko/srednje/visoko), ga prenesite kot `reasoning={"effort": "<vrijednost>"}` v klicu Responses API.
11. **O-serija zakasnitev pri pretakanju**: Modeli o-serije izvajajo notranje razmišljanje pred generiranjem izhoda. Pri pretakanju pričakujte daljšo zamudo pred prvim dogodkom `response.output_text.delta`. To je normalno — model razmišlja, ni zaustavljen.
9. **_azure_ad_token_provider je odstranjen**: `AsyncOpenAI` / `OpenAI` nimata atributa `_azure_ad_token_provider`. Testi ali koda, ki dostopa do tega atributa, bodo izgubili z `AttributeError`. Token provider se posreduje kot `api_key` in ga ni mogoče pregledovati na klientu.
10. **Snaphot / zlate datoteke**: Če testni paket uporablja snapshot testiranje, morajo biti **vse** snapshot datoteke, ki vsebujejo oblike pretakanja Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, itd.), posodobljene na novo obliko Responses. To je lahko zlahka spregledano in povzroča napake preverjanja snapshotov.
11. **Pot monkeypatcha**: Cilj monkeypatcha se spremeni iz `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ali `Responses.create` za sinhrone). Uporaba stare poti ne naredi nič opaznega — mok ni prepoznan, testi izvajajo pravi API ali propadejo.
12. **`input` ne `messages`**: Moke funkcije morajo brati `kwargs.get("input")`, ne `kwargs.get("messages")`. Responses API uporablja `input` za zgodovino pogovora.
13. **Imenovanje spremenljivk okolja**: Azure Identity SDK uporablja `AZURE_CLIENT_ID` (ne `AZURE_OPENAI_CLIENT_ID`) za `ManagedIdentityCredential(client_id=...)`. Preimenujte v testih, `.env` datotekah, nastavitvah aplikacij in v Bicep/infra.
14. **Minimalna vrednost `max_output_tokens` je 16**: Azure OpenAI zavrne vrednosti pod 16 z napako `400 integer_below_min_value`. Za osnovne teste uporabite 50, za produkcijo 1000+. Stari `max_tokens` ni imel takšne minimalne vrednosti.
15. **`tenant_id` za `AzureDeveloperCliCredential`**: Če je Azure OpenAI vir v drugem najemniku (tenantu), morate **izrecno** posredovati `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Brez tega bo poverilnica tiho uporabljala napačnega najemnika in vrnila `401`.
16. **Omejitve hitrosti se pri pretakanju pojavijo drugače**: Pri Chat Completions je 429 običajno preprečil začetek toka. Pri pretakanju Responses API se 429 lahko zgodi **sredi toka** — asinhroni iterator sproži izjemo. Vedno ovijte zanko pretakanja v `try/except` in pošljite vnaprej določeno vrstico z napako JSON, da jo frontend lahko elegantno obravnava.

17. **Obvezno je upravljanje z napakami pretakanja za spletne aplikacije**: Vzorec `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` je ključnega pomena. Brez njega SSE/JSONL tok tiho preneha delovati ob kakršni koli napaki na strežniški strani, sprednji del pa se zatakne.
18. **Definicije orodij morajo uporabljati plosko obliko**: API za Odzive pričakuje `{"type": "function", "name": ..., "parameters": ...}` — ne pa vpete strukture `{"type": "function", "function": {"name": ..., "parameters": ...}}` kot pri Chat Completions. To je najpogostejša napaka pri migraciji kode za klic funkcij.
19. **`pydantic_function_tool()` ni združljiv**: Pomožna funkcija `openai.pydantic_function_tool()` še vedno ustvarja staro vpeto obliko. Ne uporabljajte je z `responses.create()`. Schemas za orodja definirajte ročno ali izravnajte izhod.
20. **Rezultati orodij uporabljajo `function_call_output`, ne `role: tool`**: Po izvajanju orodja dodajte `{"type": "function_call_output", "call_id": ..., "output": ...}` — ne pa `{"role": "tool", "tool_call_id": ..., "content": ...}`. Za zahtevo asistenta po orodju uporabite `messages.extend(response.output)` — ne ročni slovar `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` zahteva `required` + `additionalProperties: false`**: Ko uporabljate `strict: true` za orodje, mora biti vsak atribut naveden v polju `required`, `additionalProperties` pa mora biti `false`. Pomanjkanje kateregakoli povzroči napako 400.
22. **ID-ji klicev funkcij imajo specifične predpone**: Ko ponujate nekaj primerov `function_call` v `input`, mora polje `id` začeti z `fc_`, polje `call_id` pa z `call_` (npr. `"id": "fc_example1", "call_id": "call_example1"`). Uporaba stare Chat Completions predpone `call_` za `id` ni dovoljena.
23. **GitHub Models ne podpira API-ja Odzivov**: Če aplikacija vsebuje kodo za GitHub Models (`base_url` kazalo na `models.github.ai` ali `models.inference.ai.azure.com`), jo v celoti odstranite. Pot migracije ni — preklopite na Azure OpenAI, OpenAI ali združljiv lokalni končni točki.
24. **Struktura telesa napak filtrov vsebine se je spremenila**: Napake v Chat Completions so uporabljale `error.body["innererror"]["content_filter_result"]` (ednina). Napake v API-ju Odzivov uporabljajo `error.body["content_filters"][0]["content_filter_results"]` (množina, znotraj polja). Ključ `innererror` ne obstaja več. Koda, ki neposredno dostopa do `innererror`, bo sprožila `KeyError` med izvajanjem — to je lahko enostavno spregledati pri migraciji, ker se pojavi šele ob sprožitvi filtrov vsebine. Med migracijo vedno iščite `innererror`.
25. **Surovi HTTP klici potrebujejo prepis URL-ja in telesa zahteve**: Aplikacije, ki neposredno kličejo Azure OpenAI REST (prek `requests`, `httpx`, `aiohttp`) z `/openai/deployments/{name}/chat/completions?api-version=...`, morajo preiti na `/openai/v1/responses`. Telo zahteve uporablja `input` namesto `messages`, zahteva `max_output_tokens` in `store`, parametra `api-version` v poizvedbi pa ni več. Odzivno telo besedila je v `output[0].content[0].text` — **ne** v `output_text`, ki je priročna lastnost SDK-ja, a ni prisotna v surovem REST JSON-u.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->