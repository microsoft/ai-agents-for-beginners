# Odpravljanje težav, tabela tveganj in pasti

## Odpravljanje težav pri 400 napakah

| Napaka | Popravek |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definicija orodja uporablja staro gnezdeno obliko Chat Completions | Preoblikujte iz `{"type": "function", "function": {"name": ...}}` v `{"type": "function", "name": ..., "parameters": ...}` — ime, opis, parametri so na najvišji ravni |
| `unknown_parameter: input[N].tool_calls` | Rezultati orodij za več korakov uporabljajo staro obliko Chat Completions | Zamenjajte `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` z elementi `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Orodje z `strict: true` nima polja `required` | Ko je `strict: true`, morajo biti vse lastnosti navedene v `required` in `additionalProperties: false` mora biti nastavljeno |
| `invalid_function_parameters: 'additionalProperties' is required` | Orodje z `strict: true` nima `additionalProperties: false` | Dodajte `"additionalProperties": false` v objekt parametrov |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID klica funkcije pri Few-shot ima napačen predpono | ID klicev funkcij mora začeti z `fc_` (npr. `fc_example1`), ne `call_` |
| `missing_required_parameter: text.format.name` | Dodajte ključ `"name"` slovarju formata (npr. `"name": "Output"`) |
| `invalid_type: text.format` | Poskrbite, da je `text.format` slovar s ključi `type`, `name`, `strict`, `schema` — ne niz |
| `invalid input content type` | Namesto Chat `text` uporabite vsebinske tipe `input_text`/`output_text` |
| `invalid input content type` (slika) | Vsebina slike še vedno uporablja `"type": "image_url"` | Spremenite v `"type": "input_image"` |
| `Expected object, got string` na `image_url` | `image_url` je še vedno gnezden objekt `{"url": "..."}` | Pretvorite v navaden niz: `"image_url": "https://..."` ali `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` za `max_output_tokens` | Minimum je **16** pri Azure OpenAI. Za teste uporabite 50+, za produkcijo 1000+. |
| `429 Too Many Requests` med tokovno oddajo | Omejitev hitrosti. Ovijte tokovno oddajo v `try/except`, preusmerite JSON z napako na frontend, implementirajte zamik/poskus ponovitve. |
| `KeyError: 'innererror'` pri napaki filtra vsebine | Struktura telesa napake filtra vsebine se je spremenila v Responses API-ju | Chat Completions je uporabljal `error.body["innererror"]["content_filter_result"]`; Responses API uporablja `error.body["content_filters"][0]["content_filter_results"]` (množina, znotraj polja). Prepišite vse dostopanje do `innererror`. |

---

## Tabela tveganj pri migraciji

| Simptomi | Verjetna napaka | Popravek |
|---------|---------------|-----|
| Prazen `output_text` / prerekončan odziv | Premajhen `max_output_tokens` za modele za sklepanje | Nastavite `max_output_tokens=1000` ali več — sklepanja štejejo proti omejitvi |
| `400 invalid_type: text.format` | Posredovan niz `response_format` namesto slovarja `text.format` | Uporabite `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` na `/openai/v1/responses` | Napačen `base_url` — manjka `/openai/v1/` zadnji del | Poskrbite, da je `base_url=f"{endpoint}/openai/v1/"` (z zadnjo poševnico) |
| `401 Unauthorized` po zamenjavi na `OpenAI()` | `api_key` ni nastavljen ali pa token provider ni pravilen | Za EntraID: `api_key=token_provider` (izvedljiva funkcija). Za API ključ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model vrne `deployment not found` | `model` parameter ne ustreza imenu vašega Azure nameščanja | Uporabite `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — to je ime nameščanja, ne ime modela |
| `json.loads(resp.output_text)` sproži `JSONDecodeError` | Shema ni prisiljena ali model ne podpira strogega JSON | Poskrbite za `"strict": True` v shemi in preverite podporo modela za strukturiran izhod |
| Tokovna oddaja ne vrne dogodkov `delta` | Preverjanie napačnega tipa dogodkov | Filtrirajte na `event.type == "response.output_text.delta"`, ne na Chat `chat.completion.chunk` |
| `400` napaka na vhodni sliki po migraciji | Tip vsebine slike ni posodobljen | Spremenite `"type": "image_url"` → `"type": "input_image"` in poenostavite `"image_url": {"url": "..."}` → `"image_url": "..."` (navaden niz) |
| Klici orodij se neskončno ponavljajo | Manjka rezultat orodja v nadaljnjem `input` | Po izvedbi orodja dodajte element `{"type": "function_call_output", "call_id": ..., "output": ...}` v `input` naslednjega zahtevka |
| Napaka `temperature` z GPT-5 ali o-serijo | Izrecno vrednost `temperature` drugačno od 1 | Odstranite `temperature` ali nastavite na `1` za GPT-5 in o-serijo modelov (o1, o3-mini, o3, o4-mini) |
| Napaka `top_p` z o-serijo | `top_p` ni podprt | Odstranite `top_p` pri ciljanju modelov o-serije |
| `max_completion_tokens` ni prepoznan | Uporaba Azure-specifičnega parametra | Zamenjajte `max_completion_tokens` z `max_output_tokens`. Nastavite na 4096+ za o-serijo (razmišljalni tokeni štejejo proti omejitvi). |
| Prazen/prirezan izhod iz o-serije | Premajhen `max_output_tokens` | O-serija notranje uporablja razmišljalne tokene. Nastavite `max_output_tokens=4096` ali več — ne 500–1000. |
| `400 integer_below_min_value` za `max_output_tokens` | Vrednost pod 16 | Azure OpenAI zahteva `max_output_tokens >= 16`. Za teste uporabite 50+, za produkcijo 1000+. |
| `429 Too Many Requests` sredi tokovne oddaje | Omejitev hitrosti pri Azure OpenAI | Tok se hitro prekine tiho brez obravnave napake. Vedno ovijte `async for event in await coroutine:` v `try/except` in pošljite `{"error": str(e)}` na frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Napačen najemnik ali neprijavljen | Izrecno podajte `tenant_id=os.getenv("AZURE_TENANT_ID")`. Zaženite lokalno `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` pri uporabi GitHub Modelov (`models.github.ai`) | GitHub modeli ne podpirajo Responses API | Takoj odstranite kodo za GitHub Modele. Uporabite Azure OpenAI, OpenAI ali združljiv lokalni endpoint (npr. Ollama z podporo Responses). |
| MAF `OpenAIChatCompletionClient` še vedno uporablja Chat Completions | Uporaba starega MAF klienta v 1.0.0+ | V MAF 1.0.0+ `OpenAIChatClient` po privzetku uporablja Responses API. Zamenjajte `OpenAIChatCompletionClient` z `OpenAIChatClient`. Za pre-1.0.0 nadgradite na `agent-framework-openai>=1.0.0`. |
| LangChain agent vrača prazno ali spodleti pri klicih orodij | `ChatOpenAI` ne uporablja Responses API | Dodajte `use_responses_api=True` v `ChatOpenAI(...)`. Prav tako spremenite `.content` → `.text` pri odzivnih sporočilih. |
| `KeyError: 'innererror'` v upravljalniku napak filtra vsebine | Struktura telesa napake se je spremenila v Responses API-ju | Prepišite `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Ovitek `innererror` je izginil; podrobnosti filtra vsebine so sedaj v glavnem polju `content_filters` kot množina znotraj vsakega vnosa `content_filter_results` (množina). |
| Neposredni HTTP klic na `/openai/deployments/.../chat/completions` vrne 404 | Stari Chat Completions REST endpoint | Prepišite URL v `/openai/v1/responses`. Spremenite telo zahtevka: `messages` → `input`, dodajte `max_output_tokens` + `store: false`, odstranite `api-version` query parameter. Spremenite pardiranje odziva: `choices[0].message.content` → `output[0].content[0].text` (opomba: `output_text` je lastnost SDK, ni vključen v surov REST JSON). |

---

## Pasti

1. Če ste prej uporabljali Chat Completions za stanje pogovora, upravljajte svoje stanje izrecno z Responses.
2. Raje uporabite `max_output_tokens` kot zastareli `max_tokens`.
3. Pri migraciji na `gpt-5` poskrbite, da `temperature` ni določen ali je nastavljen na `1`.
4. Zamenjajte Chat `content[].type: "text"` z Responses `content[].type: "input_text"` za uporabniške/sistemske vhode.
5. Za `text.format` zagotovite pravilen slovar (npr. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ne navaden niz.
6. Parametra `seed` Responses ne podpirajo; odstranite ga iz zahtevkov.
7. **Razmišljanje**: Vključite `reasoning` samo, če ga je originalna koda že uporabljala. Ne dodajajte `reasoning` v API klice, kjer tega ni bilo — mnogi modeli (npr. gpt-4o-mini) tega parametra ne podpirajo.
8. **Velikost `max_output_tokens`**: Za modele za sklepanje (GPT-5-mini, GPT-5, o-serija) uporabite `max_output_tokens=4096` ali več — ne 50–1000. Model interno uporablja razmišljalne tokene preden generira vidni izhod; prenizka omejitev povzroči prirezan ali prazen odgovor.
9. **O-serija `max_completion_tokens`**: Če je originalna koda uporabljala `max_completion_tokens` (Azure-specifično za o-serijo), zamenjajte z `max_output_tokens`. Responses API ne sprejema `max_completion_tokens`.
10. **O-serija `reasoning_effort`**: Če originalna koda uporablja `reasoning_effort` (low/medium/high), migrirajte ga v `reasoning={"effort": "<vrednost>"}` v klicu Responses API.
11. **O-serija zakasnitev tokovne oddaje**: Modeli o-serije izvajajo notranje razmišljanje pred generiranjem izhoda. Pri tokovni oddaji pričakujte daljši zamik pred prvim dogodkom `response.output_text.delta`. To je normalno — model razmišlja, ni zmrznjen.
9. **`_azure_ad_token_provider` ni več**: `AsyncOpenAI` / `OpenAI` nimata atributa `_azure_ad_token_provider`. Testi ali koda, ki dostopa do tega atributa, bo spodletela z `AttributeError`. Token provider se posreduje kot `api_key` in ni dostopen za pregled na klientu.
10. **Datoteke posnetkov / zlate datoteke**: Če testni nabor uporablja testiranje posnetkov, je potrebno POSODOBITI VSE posnetke, ki vsebujejo oblike tokovne oddaje Chat Completions (`choices[0]`, `content_filter_results`, `function_call` itd.) na novo obliko Responses. To je lahko spregledano in povzroči napake pri potrditvi posnetka.
11. **Pot za lažni opomnik**: Cilj monkeypatch se spremeni iz `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (ali `Responses.create` za sinhrone klice). Uporaba stare poti nič ne naredi tiho — lažni opomnik ne prestreže klica, testi dostopajo do pravega API ali spodletijo.
12. **`input`, ne `messages`**: Lažne funkcije morajo brati `kwargs.get("input")`, ne `kwargs.get("messages")`. Responses API uporablja `input` za zgodovino pogovora.
13. **Poimenovanje okolijskih spremenljivk**: Azure Identity SDK uporablja `AZURE_CLIENT_ID` (ne `AZURE_OPENAI_CLIENT_ID`) za `ManagedIdentityCredential(client_id=...)`. Preimenujte v testih, `.env` datotekah, nastavitvah aplikacij in Bicep/infrastrukturi.
14. **Minimalna vrednost `max_output_tokens` je 16**: Azure OpenAI zavrne vrednosti pod 16 z `400 integer_below_min_value`. Za teste uporabite 50, za produkcijo 1000+. Stari `max_tokens` ni imel takega minimuma.
15. **`tenant_id` za `AzureDeveloperCliCredential`**: Če je Azure OpenAI vir v drugem najemniku, morate IZRECNO podati `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Brez tega po tihem uporablja napačen najemnik in vrne `401`.
16. **Omejitve hitrosti se pri tokovni oddaji pojavijo drugače**: Pri Chat Completions je 429 običajno preprečil začetek toka. Pri Responses API tokovni oddaji se lahko 429 zgodi SREDI TOKA — asinhroni iterator sproži izjemo. Vedno ovijte zanko tokovne oddaje v `try/except` in pošljite vrstico z napako v JSON, da jo frontend lahko prijazno obdela.

17. **Obvezno je upravljanje z napakami pri pretakanju za spletne aplikacije**: Vzorec `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` je ključnega pomena. Brez tega se SSE/JSONL tok tiho prekine ob kateri koli napaki na strežniški strani, frontend pa se zatakne.
18. **Definicije orodij morajo uporabljati ploski format**: Responses API pričakuje `{"type": "function", "name": ..., "parameters": ...}` — ne pa Chat Completions gnezdenega `{"type": "function", "function": {"name": ..., "parameters": ...}}`. To je najpogostejša migracijska napaka v kodi za klic funkcij.
19. **`pydantic_function_tool()` ni združljiv**: Pomočnik `openai.pydantic_function_tool()` še vedno generira star gnezden format. Ne uporabljajte ga z `responses.create()`. Sheme orodij definirajte ročno ali izravnajte izhod.
20. **Rezultati orodij uporabljajo `function_call_output`, ne `role: tool`**: Po izvedbi orodja dodajte `{"type": "function_call_output", "call_id": ..., "output": ...}` — ne `{"role": "tool", "tool_call_id": ..., "content": ...}`. Za zahtevo po orodju asistenta uporabite `messages.extend(response.output)` — ne ročni slovar `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` zahteva `required` + `additionalProperties: false`**: Pri uporabi `strict: true` na orodju mora biti vsak atribut naveden v polju `required`, `additionalProperties` pa mora biti `false`. Izpustitev kateregakoli povzroči napako 400.
22. **ID-ji klicev funkcij imajo specifične predpone**: Pri podajanju elementov `function_call` z nekaj primeri v `input` mora polje `id` začeti s `fc_`, polje `call_id` pa z `call_` (npr. `"id": "fc_example1", "call_id": "call_example1"`). Uporaba stare predpone `call_` za `id` iz Chat Completions je zavrnjena.
23. **GitHub Models ne podpira Responses API**: Če aplikacija vsebuje pot kode za GitHub Models (`base_url` kaže na `models.github.ai` ali `models.inference.ai.azure.com`), jo odstranite v celoti. Ni migracijske poti — preklopite na Azure OpenAI, OpenAI ali združljiv lokalni endpoint.
24. **Struktura telesa napake filtriranja vsebine se je spremenila**: Napake Chat Completions so uporabljale `error.body["innererror"]["content_filter_result"]` (ednino). Napake Responses API uporabljajo `error.body["content_filters"][0]["content_filter_results"]` (množina, znotraj tabele). Ključ `innererror` ne obstaja več. Koda, ki neposredno dostopa do `innererror`, bo ob izvajanju sprožila `KeyError` — to je lahko spregledano pri migraciji, ker se pojavi le, ko filter vsebine dejansko sproži napako. Med migracijo vedno iščite `innererror`.
25. **Goli HTTP klici potrebujejo prepis URL in telesa**: Aplikacije, ki kličejo Azure OpenAI REST neposredno (prek `requests`, `httpx`, `aiohttp`) s potjo `/openai/deployments/{name}/chat/completions?api-version=...`, morajo preklopiti na `/openai/v1/responses`. Telo zahteve uporablja `input` namesto `messages`, zahteva `max_output_tokens` in `store`, ter parameter poizvedbe `api-version` je odstranjena. Besedilo odgovora je v `output[0].content[0].text` — **ne** `output_text`, ki je lastnost SDK za priročnost, ki ni prisotna v surovem REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->