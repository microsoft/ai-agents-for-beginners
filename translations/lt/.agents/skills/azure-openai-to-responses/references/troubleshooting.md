# Trikčių šalinimas, rizikos lentelė ir sunkumai

## 400 klaidų trikčių šalinimas

| Klaida | Sprendimas |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Įrankio apibrėžimas naudoja seną Chat Completions įdėtą formatą | Pertvarkykite iš `{"type": "function", "function": {"name": ...}}` į `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters turi būti aukščiausiame lygyje |
| `unknown_parameter: input[N].tool_calls` | Daugiapakopiai įrankių rezultatai naudoja seną Chat Completions formatą | Pakeiskite `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` su `response.output` elementais + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` įrankiui trūksta `required` masyvo | Kai `strict: true`, visi savybės turi būti išvardytos `required`, o `additionalProperties: false` turi būti nustatyta |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` įrankiui trūksta `additionalProperties: false` | Pridėkite `"additionalProperties": false` prie parametrų objekto |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID turi netinkamą priešdėlį | Function call ID turi prasidėti `fc_` (pvz., `fc_example1`), o ne `call_` |
| `missing_required_parameter: text.format.name` | Pridėkite `"name"` raktą į formato žodyną (pvz., `"name": "Output"`) |
| `invalid_type: text.format` | Įsitikinkite, kad `text.format` yra žodynas su raktai `type`, `name`, `strict`, `schema`, o ne eilutė |
| `invalid input content type` | Naudokite `input_text`/`output_text` turinio tipus vietoje Chat `text` |
| `invalid input content type` (paveikslėlis) | Paveikslėlio turinys dar naudoja `"type": "image_url"` | Pakeiskite į `"type": "input_image"` |
| `Expected object, got string` apie `image_url` | `image_url` vis dar yra įdėtas objektas `{"url": "..."}` | Pakeiskite į paprastą eilutę: `"image_url": "https://..."` arba `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` dėl `max_output_tokens` | Minimalus kiekis yra **16** Azure OpenAI. Testams naudokite 50+, gamybai 1000+. |
| `429 Too Many Requests` transliavimo metu | Peržengtas greičio ribojimas. Apvyniokite transliavimą `try/except`, grąžinkite klaidos JSON front-endui, įgyvendinkite atidėjimą/pakartojimą. |
| `KeyError: 'innererror'` dėl turinio filtro klaidos | Turinio filtro klaidos struktūra pasikeitė Responses API | Chat Completions naudojo `error.body["innererror"]["content_filter_result"]`; Responses API naudoja `error.body["content_filters"][0]["content_filter_results"]` (daugiskaita, masyve). Pervairuokite visus `innererror` naudojimus. |

---

## Migracijos rizikos lentelė

| Simptomas | Tikėtina klaida | Sprendimas |
|---------|---------------|-----|
| Tuščias `output_text` / sutrumpinta atsakymo dalis | `max_output_tokens` per mažas protavimo modeliams | Nustatykite `max_output_tokens=1000` ar daugiau — protavimo tokenai skaičiuojami į limitą |
| `400 invalid_type: text.format` | Perdavėte `response_format` eilutę vietoje `text.format` žodyno | Naudokite `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` adresui `/openai/v1/responses` | Klaidingas `base_url` — trūksta `/openai/v1/` galūnės | Užtikrinkite `base_url=f"{endpoint}/openai/v1/"` (su skliausteliu pabaigoje) |
| `401 Unauthorized` po perėjimo prie `OpenAI()` | `api_key` nenustatytas arba neteisingai perduotas token tiekėjas | EntraID atveju: `api_key=token_provider` (kviečiamas objektas). API raktas: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modelis grąžina `deployment not found` | `model` parametras neatitinka jūsų Azure diegimo pavadinimo | Naudokite `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — tai diegimo pavadinimas, ne modelio vardas |
| `json.loads(resp.output_text)` meta `JSONDecodeError` | Schema neprivaloma arba modelis nepalaiko griežto JSON | Užtikrinkite `strict: True` schemoje ir patikrinkite modelio struktūrinį palaikymą |
| Transliavimas neišmeta `delta` įvykių | Tikrina netinkamą įvykio tipą | Filtruokite pagal `event.type == "response.output_text.delta"`, o ne Chat `chat.completion.chunk` |
| 400 klaida dėl paveikslėlio įvesties po migracijos | Paveikslėlio turinio tipas nepakeistas | Pakeiskite `"type": "image_url"` į `"type": "input_image"` ir pertvarkykite `"image_url": {"url": "..."}` į `"image_url": "..."` (paprasta eilutė) |
| Įrankio kvietimų ciklas nesibaigia | Trūksta įrankio rezultato tolesniame `input` | Po įrankio vykdymo pridėkite `{"type": "function_call_output", "call_id": ..., "output": ...}` į kitos užklausos `input` |
| `temperature` klaida su GPT-5 arba o-serijos modeliais | Aiškus `temperature` reikšmės nurodymas, išskyrus 1 | Pašalinkite `temperature` arba nustatykite į `1` GPT-5 ir o-serijos modeliams (o1, o3-mini, o3, o4-mini) |
| `top_p` klaida su o-serijos modeliais | `top_p` nepalaikomas | Pašalinkite `top_p`, kai naudojate o-serijos modelius |
| `max_completion_tokens` nepripažįstamas | Naudojamas Azure specifinis parametras | Pakeiskite `max_completion_tokens` į `max_output_tokens`. Nustatykite 4096+ o-serijai (protavimo tokenai įskaičiuojami į limitą). |
| Tuščias / sutrumpintas o-serijos išvesties rezultatas | `max_output_tokens` per mažas | O-serija naudoja vidinius protavimo tokenus. Nustatykite `max_output_tokens=4096` arba daugiau — ne 500–1000. |
| `400 integer_below_min_value` dėl `max_output_tokens` | Reikšmė mažesnė nei 16 | Azure OpenAI reikalauja `max_output_tokens >= 16`. Naudokite 50+ testams, 1000+ gamybai. |
| `429 Too Many Requests` vidury transliavimo | Azure OpenAI apribojimai | Srautas nutraukiamas tyliai be klaidų apdorojimo. Visada apvyniokite `async for event in await coroutine:` `try/except` ir grąžinkite `{"error": str(e)}` į priekį. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Netinkamas nuomininkas arba neprisijungta | Aiškiai perduokite `tenant_id=os.getenv("AZURE_TENANT_ID")`. Vietoje vykdykite `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` naudojant GitHub modelius (`models.github.ai`) | GitHub modeliai nepalaiko Responses API | Pašalinkite GitHub modelių kodo kelią. Naudokite Azure OpenAI, OpenAI arba suderinamą lokalų endpoint (pvz., Ollama su Responses palaikymu). |
| MAF `OpenAIChatCompletionClient` vis dar naudoja Chat Completions | Naudojamas senasis MAF klientas versijoje 1.0.0 ar vėliau | MAF 1.0.0+ `OpenAIChatClient` pagal nutylėjimą naudoja Responses API. Pakeiskite `OpenAIChatCompletionClient` į `OpenAIChatClient`. Iki 1.0.0 versijų atnaujinkite į `agent-framework-openai>=1.0.0`. |
| LangChain agentas grąžina tuščią atsakymą arba nepavyksta su įrankių kvietimais | `ChatOpenAI` nenaudoja Responses API | Pridėkite `use_responses_api=True` į `ChatOpenAI(...)`. Taip pat pakeiskite `.content` į `.text` atsakymų žinutėse. |
| `KeyError: 'innererror'` turinio filtro klaidų apdorojime | Klaidos kūno struktūra pasikeitė Responses API | Pervairuokite `error.body["innererror"]["content_filter_result"]["jailbreak"]` į `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` apvadas dingo; turinio filtro detalės dabar yra aukščiausio lygio `content_filters` masyve su `content_filter_results` (daugiskaita) kiekviename įraše. |
| Žiedinis HTTP kvietimas `/openai/deployments/.../chat/completions` grąžina 404 | Senoji Chat Completions REST sąsaja | Pervairuokite URL į `/openai/v1/responses`. Pakeiskite užklausos kūną: `messages` → `input`, pridėkite `max_output_tokens` ir `store: false`, pašalinkite `api-version` užklausos parametrą. Pakeiskite atsakymo analizę: `choices[0].message.content` → `output[0].content[0].text` (pažymėtina: `output_text` yra SDK patogumo savybė, neprieinama žaliaviniame JSON). |

---

## Sunkumai

1. Jei anksčiau naudojote Chat Completions pokalbio būsenai valdyti, atsakingai valdykite savo būseną naudodami Responses.
2. Rinkitės `max_output_tokens` vietoje senos `max_tokens`.
3. Migracijos į `gpt-5` metu užtikrinkite, kad `temperature` nėra nurodytas arba yra nustatytas į `1`.
4. Pakeiskite Chat `content[].type: "text"` į Responses `content[].type: "input_text"` vartotojo / sistemos įvestims.
5. Dėl `text.format` pateikite tinkamą žodyną (pvz., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ne paprastą eilutę.
6. Parametras `seed` nėra palaikomas Responses; pašalinkite jį iš užklausų.
7. **Protavimas**: Įtraukkite `reasoning` tik jei originalus kodas jį jau naudojo. Nenaudokite `reasoning` API kvietimuose, kurie jo neturėjo — dauguma ne protavimo modelių šio parametro nepalaiko.
8. **`max_output_tokens` dydis**: Protavimo modeliams (GPT-5-mini, GPT-5, o-serija) naudokite `max_output_tokens=4096` ar daugiau — ne 50–1000. Modelis viduje naudoja protavimo tokenus prieš generuodamas matomą išvestį; per mažas limitas lemia sutrumpintas ar tuščias atsakymus.
9. **O-serijos `max_completion_tokens`**: Jei originalus kodas naudojo Azure specifinį `max_completion_tokens`, pakeiskite į `max_output_tokens`. Responses API nepriima `max_completion_tokens`.
10. **O-serijos `reasoning_effort`**: Jei originalus kodas naudoja `reasoning_effort` (žemas/vidutinis/aukštas), migravus naudokite `reasoning={"effort": "<value>"}` Responses API kvietime.
11. **O-serijos transliavimo delsimas**: O-serijos modeliai atlieka vidinį protavimą prieš generuodami išvestį. Transliuojant tikėkitės ilgesnio delsimo prieš pirmą `response.output_text.delta` įvykį. Tai normalu — modelis protauja, o ne užstrigo.
9. **`_azure_ad_token_provider` panaikintas**: `AsyncOpenAI` / `OpenAI` neturi `_azure_ad_token_provider` atributo. Testai ar kodas, kuris prie jo prieina, sugrius su `AttributeError`. Tokeno tiekėjas perduodamas kaip `api_key` ir nėra prieinamas klientų objekte.
10. **Snapshot / 'golden' failai**: Jei testų aibė naudoja snapshot testavimą, **visi** snapshot failai, kuriuose yra Chat Completions transliavimo formos (`choices[0]`, `content_filter_results`, `function_call` ir kt.) turi būti atnaujinti į naują Responses formą. Tai lengva praleisti ir sukelia snapshot klaidas.
11. **Mock monkeypatch kelias**: Monkeypatch tikslas pasikeitė iš `openai.resources.chat.AsyncCompletions.create` į `openai.resources.responses.AsyncResponses.create` (arba `Responses.create` sinchroniniam variantui). Naudojant seną kelią nieko neįvyks — prijungimas neveiks, testai kreipsis į tikrą API arba nepavyks.
12. **`input`, o ne `messages`**: Mock funkcijos turi skaityti `kwargs.get("input")`, o ne `kwargs.get("messages")`. Responses API naudoja `input` pokalbio istorijai.
13. **Aplinkos kintamųjų pavadinimai**: Azure Identity SDK naudoja `AZURE_CLIENT_ID` (ne `AZURE_OPENAI_CLIENT_ID`) `ManagedIdentityCredential(client_id=...)` atvejui. Pervadinkite testuose, `.env` failuose, programos nustatymuose ir Bicep/infrastruktūroje.
14. **`max_output_tokens` minimumas – 16**: Azure OpenAI atsisako reikšmių mažesnių už 16 su `400 integer_below_min_value`. Naudokite 50 testams, 1000+ gamybai. Senasis `max_tokens` neturėjo tokio minimalaus reikalavimo.
15. **`tenant_id` `AzureDeveloperCliCredential`**: Kai Azure OpenAI ištekliai yra kitame nuomininke, privalote aiškiai perduoti `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Be to, kredencialas tyliai naudoja netinkamą tenantą ir grąžina `401`.
16. **Greičio ribojimai transliavime pasireiškia kitaip**: Su Chat Completions 429 dažnai neleisdavo pradėti srauto. Su Responses API transliavimu, 429 gali įvykti **transliacijos viduryje** — asinchroninis iteratoriaus ciklas išmeta išimtį. Visada apvyniokite transliavimo ciklą `try/except` ir grąžinkite klaidos JSON eilutę, kad front-end galėtų tvarkingai apdoroti.

17. **Srautinio perdavimo klaidų tvarkymas yra privalomas tinklo programėlėms**: Šablonas `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` yra kritinis. Be jo, SSE/JSONL srautas tyliai nutrūksta ant bet kokios serverio pusės klaidos ir frontend'as užstringa.
18. **Įrankių apibrėžimai turi naudoti plokščią formatą**: Atsakymų API laukia `{"type": "function", "name": ..., "parameters": ...}` — o ne Chat Completions įdėtą `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Tai yra dažniausia migracijos klaida funkcijų kvietimo kode.
19. **`pydantic_function_tool()` yra nesuderinamas**: `openai.pydantic_function_tool()` pagalbinė funkcija vis dar generuoja seną įdėtą formatą. Nenaudokite jos su `responses.create()`. Apibrėžkite įrankių schemas rankiniu būdu arba supaprastinkite išvestį.
20. **Įrankių rezultatai naudoja `function_call_output`, o ne `role: tool`**: Įvykdžius įrankį pridėkite `{"type": "function_call_output", "call_id": ..., "output": ...}` — o ne `{"role": "tool", "tool_call_id": ..., "content": ...}`. Asistentės įrankio užklausai naudokite `messages.extend(response.output)` — o ne rankinį `{"role": "assistant", "tool_calls": [...]}` žodyną.
21. **`strict: true` reikalauja `required` + `additionalProperties: false`**: Naudojant `strict: true` įrankiui, kiekviena savybė turi būti išvardinta `required` masyve ir `additionalProperties` turi būti `false`. Kuri nors trūkstama reikšmė sukelia 400 klaidą.
22. **Funkcijos kvietimų ID turi specifinius prefiksus**: Kai pateikiami keli `function_call` elementai `input`, `id` laukas turi prasidėti nuo `fc_`, o `call_id` laukas nuo `call_` (pvz., `"id": "fc_example1", "call_id": "call_example1"`). Naudojant senojo Chat Completions `call_` prefiksą `id` lauke yra atmesta.
23. **GitHub Models nepalaiko Responses API**: Jei programėlė turi GitHub Models kodo kelią (`base_url` nukreipia į `models.github.ai` arba `models.inference.ai.azure.com`), visiškai jį pašalinkite. Nėra migracijos kelio — pereikite prie Azure OpenAI, OpenAI arba suderinamo vietinio galo taško.
24. **Turinio filtrų klaidų pranešimų struktūra pasikeitė**: Chat Completions klaidos naudojo `error.body["innererror"]["content_filter_result"]` (vienaskaita). Responses API klaidos naudoja `error.body["content_filters"][0]["content_filter_results"]` (daugiskaita, masyvo viduje). Rakto `innererror` nebėra. Kodas, tiesiogiai pasiekiantis `innererror`, vykdymo metu kels `KeyError` — tai lengva praleisti migracijos metu, nes tai pasimato tik kai iš tikrųjų suveikia turinio filtras. Migracijos metu visada ieškokite `innererror`.
25. **Žemos lygio HTTP kvietimams reikalingas URL + kūno perrašymas**: Programėlės, tiesiogiai kviečiančios Azure OpenAI REST (per `requests`, `httpx`, `aiohttp`) naudodamos `/openai/deployments/{name}/chat/completions?api-version=...` turi pereiti prie `/openai/v1/responses`. Užklausos kūnas naudoja `input` vietoje `messages`, reikalauja `max_output_tokens` ir `store`, o `api-version` užklausos parametras pašalinamas. Atsakymo kūnas tekstas yra `output[0].content[0].text` — **ne** `output_text`, kuris yra SDK patogumo savybė ir nėra žemo lygio REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->