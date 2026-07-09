# Problemos sprendimas, Rizikos lentelė ir Pastebėjimai

## 400 klaidų sprendimas

| Klaida | Sprendimas |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Įrankio apibrėžime naudojamas senas Chat Completions įdėtas formatas | Supaprastinkite iš `{"type": "function", "function": {"name": ...}}` į `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters dedami į viršutinį lygį |
| `unknown_parameter: input[N].tool_calls` | Daugiasluoksniai įrankių rezultatai naudoja seną Chat Completions formatą | Pakeiskite `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` į `response.output` elementus + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` įrankyje trūksta `required` masyvo | Kai `strict: true`, visi parametrai turi būti įtraukti į `required`, ir turi būti nustatyta `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` įrankyje trūksta `additionalProperties: false` | Pridėkite `"additionalProperties": false` prie parametrų objekto |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Trumpoms funkcijų iškvietimo ID pradžia neteisinga | Funkcijų iškvietimo ID turi prasidėti nuo `fc_` (pvz., `fc_example1`), o ne nuo `call_` |
| `missing_required_parameter: text.format.name` | Pridėkite `"name"` raktą prie formato žodyno (pvz., `"name": "Output"`) |
| `invalid_type: text.format` | Užtikrinkite, kad `text.format` būtų žodynas su raktiniais žodžiais `type`, `name`, `strict`, `schema` – ne eilutė |
| `invalid input content type` | Naudokite `input_text`/`output_text` turinio tipus vietoje Chat `text` |
| `invalid input content type` (vaizdas) | Vaizdo turinys vis dar naudoja `"type": "image_url"` | Pakeiskite į `"type": "input_image"` |
| `Expected object, got string` prie `image_url` | `image_url` vis dar yra įdėtas objektas `{"url": "..."}` | Supaprastinkite į eilutę: `"image_url": "https://..."` arba `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` prie `max_output_tokens` | Minimalus yra **16** Azure OpenAI. Naudokite 50+ testams, 1000+ gamybai. |
| `429 Too Many Requests` srauto metu | Per daug užklausų. Apvyniokite srautą `try/except`, grąžinkite klaidos JSON į frontendą, įgyvendinkite atidėjimą/perbandymą. |
| `KeyError: 'innererror'` turinio filtro klaidos metu | Turinio filtro klaidos kūno struktūra pasikeitė Responses API | Chat Completions naudojo `error.body["innererror"]["content_filter_result"]`; Responses API naudoja `error.body["content_filters"][0]["content_filter_results"]` (daugybinė, masyve). Perrašykite visus `innererror` pasiekiamus kelius. |

---

## Migracijos rizikos lentelė

| Simptomas | Tikėtina klaida | Sprendimas |
|---------|---------------|-----|
| Tuščias `output_text` / sutrumpintas atsakymas | `max_output_tokens` per mažas samprotavimo modeliams | Nustatykite `max_output_tokens=1000` arba didesnį — samprotavimų tokenai įskaityti į limitą |
| `400 invalid_type: text.format` | Perduotas `response_format` kaip eilutė vietoje `text.format` žodyno | Naudokite `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` adresu `/openai/v1/responses` | Neteisingas `base_url` – trūksta `/openai/v1/` užbaigimo | Užtikrinkite `base_url=f"{endpoint}/openai/v1/"` (su galiniu skliaustu) |
| `401 Unauthorized` po perėjimo prie `OpenAI()` | `api_key` nenustatytas arba tokeno palaikytojas neteisingai perduotas | EntraID: `api_key=token_provider` (kviestinis objektas). API raktui: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Modelis grąžina `deployment not found` | `model` parametras nesutampa su jūsų Azure diegimo vardu | Naudokite `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — tai diegimo pavadinimas, ne modelio pavadinimas |
| `json.loads(resp.output_text)` metą `JSONDecodeError` | Schema neprimesta arba modelis nepalaiko griežto JSON | Užtikrinkite `"strict": True` schemoje ir patikrinkite, ar modelis palaiko struktūruotą išvestį |
| Srautas nepateikia `delta` įvykių | Neteisingas įvykio tipo tikrinimas | Filtruokite pagal `event.type == "response.output_text.delta"`, ne Chat `chat.completion.chunk` |
| `400` klaida prie vaizdo įvesties po migracijos | Vaizdo turinio tipas ne atnaujintas | Pakeiskite `"type": "image_url"` į `"type": "input_image"` ir supaprastinkite `"image_url": {"url": "..."}` į `"image_url": "..."` (eilutė) |
| Įrankio kvietimai vyksta begaliniu ciklu | Trūksta įrankio rezultato sekantį `input` | Po įrankio vykdymo pridėkite `{"type": "function_call_output", "call_id": ..., "output": ...}` elementą į `input` kitame užklausoje |
| `temperature` klaida su GPT-5 arba o serija | Aiški `temperature` reikšmė skirtinga nuo 1 | Pašalinkite `temperature` arba nustatykite į `1` GPT-5 ir o serijos modeliams (o1, o3-mini, o3, o4-mini) |
| `top_p` klaida su o serija | `top_p` nepalaikomas | Pašalinkite `top_p`, kai taikote o serijos modeliams |
| `max_completion_tokens` nepripažįstamas | Naudoja Azure specifinį parametrą | Pakeiskite `max_completion_tokens` į `max_output_tokens`. Nustatykite 4096+ o serijai (samprotavimų tokenai įskaičiuojami į limitą). |
| Tuščia/sutrumpinta išvestis iš o serijos | `max_output_tokens` per mažas | O serija naudoja viduje samprotavimų tokenus. Nustatykite `max_output_tokens=4096` arba didesnį — ne 500–1000. |
| `400 integer_below_min_value` prie `max_output_tokens` | Reikšmė mažesnė nei 16 | Azure OpenAI prižiūri, kad `max_output_tokens >= 16`. Naudokite 50+ dūmų testams, 1000+ gamybai. |
| `429 Too Many Requests` srauto viduryje | Azure OpenAI ribo užklausų dažnį | Srautas nutraukiamas tyliai be klaidos apdorojimo. Visada apvyniokite `async for event in await coroutine:` į `try/except` ir pateikite `{"error": str(e)}` frontendui. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Netinkamas nuomininkas arba nepavyko prisijungti | Perduokite `tenant_id=os.getenv("AZURE_TENANT_ID")` tiesiogiai. Vietoje vykdykite `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` naudojant GitHub modelius (`models.github.ai`) | GitHub modeliai nepalaiko Responses API | Visiškai pašalinkite GitHub modelių kodo kelią. Naudokite Azure OpenAI, OpenAI arba suderinamą vietinį galinį tašką (pvz., Ollama su Responses palaikymu). |
| MAF `OpenAIChatCompletionClient` vis dar naudoja Chat Completions | Naudoja seną MAF klientą versijoje 1.0.0+ | MAF 1.0.0+ `OpenAIChatClient` naudoja Responses API pagal nutylėjimą. Pakeiskite `OpenAIChatCompletionClient` į `OpenAIChatClient`. Iki 1.0.0 versijos atnaujinkite į `agent-framework-openai>=1.0.0`. |
| LangChain agentas grąžina tuštumą arba klaidą dėl įrankio kvietimų | `ChatOpenAI` nenaudoja Responses API | Įtraukite `use_responses_api=True` į `ChatOpenAI(...)`. Taip pat pakeiskite `.content` į `.text` atsakymų žinutėse. |
| `KeyError: 'innererror'` turinio filtro klaidos tvarkytuve | Klaidos kūno struktūra pasikeitė Responses API | Perrašykite `error.body["innererror"]["content_filter_result"]["jailbreak"]` į `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` apvalkalas dingo; turinio filtro detalės dabar yra aukščiausio lygio `content_filters` masyve su `content_filter_results` (dauginės formos) kiekviename įraše. |
| Žalias HTTP kvietimas į `/openai/deployments/.../chat/completions` grąžina 404 | Senas Chat Completions REST galinis taškas | Perrašykite URL į `/openai/v1/responses`. Pakeiskite užklausos kūną: `messages` į `input`, pridėkite `max_output_tokens` + `store: false`, pašalinkite užklausos parametrą `api-version`. Pakeiskite atsakymo analizę: `choices[0].message.content` į `output[0].content[0].text` (pastaba: `output_text` yra SDK patogumo savybė, kurios nėra žaliame REST JSON). |

---

## Pastebėjimai

1. Jei anksčiau naudojote Chat Completions pokalbių būsenai, valdykite savo būseną aiškiai naudodami Responses.
2. Pirmenybę teikite `max_output_tokens` prieš senąjį `max_tokens`.
3. Pereinant prie `gpt-5`, užtikrinkite, kad `temperature` nebūtų nurodytas arba būtų nustatytas į `1`.
4. Pakeiskite Chat `content[].type: "text"` į Responses `content[].type: "input_text"` vartotojo/sistemos įvedimams.
5. Dėl `text.format` pateikite tinkamą žodyną (pvz., `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ne paprastą eilutę.
6. Parametras `seed` nėra palaikomas Responses; pašalinkite jį iš užklausų.
7. **Samprotavimas**: Įtraukite `reasoning` tik jei originalus kodas jau jį naudojo. Nenaudokite `reasoning` API kvietimuose, kuriuose jo nebuvo – daug modelių (pvz., gpt-4o-mini) nepalaiko šio parametro.
8. **`max_output_tokens` dydis**: Samprotavimo modeliams (GPT-5-mini, GPT-5, o serija) naudokite `max_output_tokens=4096` arba daugiau – ne 50–1000. Modelis viduje naudoja samprotavimo tokenus prieš generuojant matomą rezultatą; per mažas limitas sukelia sutrumpintus arba tuščius atsakymus.
9. **O serijos `max_completion_tokens`**: Jei originalus kodas naudojo `max_completion_tokens` (Azure specifinis o serijai), pakeiskite į `max_output_tokens`. Responses API nepriima `max_completion_tokens`.
10. **O serijos `reasoning_effort`**: Jei originalus kodas naudoja `reasoning_effort` (low/medium/high), pakeiskite į `reasoning={"effort": "<value>"}` Responses API kvietimuose.
11. **O serijos srauto vėlavimas**: O serijos modeliai vykdo vidinį samprotavimą prieš išvesties generavimą. Srauto metu tikėkitės ilgesnio laukimo iki pirmojo `response.output_text.delta` įvykio. Tai normalu – modelis samprotauja, o ne įstringa.
9. **`_azure_ad_token_provider` nebeegzistuoja**: `AsyncOpenAI` / `OpenAI` neturi `_azure_ad_token_provider` atributo. Testai ar kodas, kurie jį naudoja, atmes `AttributeError`. Tokeno tiekėjas perduodamas kaip `api_key` ir nėra prieinamas kliento objekte.
10. **Snapshot / aukso failai**: Jei testų rinkinys naudoja snapų testavimą, **visi** snapų failai, turintys Chat Completions srauto struktūras (`choices[0]`, `content_filter_results`, `function_call` ir kt.) turi būti atnaujinti į naują Responses formą. Tai lengva praleisti ir sukelia snapų patvirtinimo klaidas.
11. **Mock monkeypatch kelias**: Monkeypatch tikslas keičiasi iš `openai.resources.chat.AsyncCompletions.create` į `openai.resources.responses.AsyncResponses.create` (arba `Responses.create` sinchroniniam). Naudojant seną kelią tyliai neveiks – mockas neužkirs kelio, testai kils prie realaus API arba nepavyks.
12. **`input` ne `messages`**: Mock funkcijos turi skaityti `kwargs.get("input")`, o ne `kwargs.get("messages")`. Responses API naudoja `input` pokalbių istorijai.
13. **Aplinkos kintamųjų pavadinimai**: Azure Identity SDK naudoja `AZURE_CLIENT_ID` (ne `AZURE_OPENAI_CLIENT_ID`) `ManagedIdentityCredential(client_id=...)`. Pervardykite testuose, `.env` failuose, programos nustatymuose ir Bicep/infrastruktūroje.
14. **`max_output_tokens` minimalus 16**: Azure OpenAI atmeta mažesnes reikšmes nei 16 su `400 integer_below_min_value`. Naudokite 50 dūmų testams, 1000+ gamybai. Senasis `max_tokens` šio minimalaus limito neturėjo.
15. **`tenant_id` AzureDeveloperCliCredential**: Kai Azure OpenAI ištekliai yra kitame nuomininke, privalote aiškiai perduoti `tenant_id` – `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Be to, prisijungimas tyliai naudos neteisingą nuomininką ir grąžins `401`.
16. **Ribojimai sraute pasireiškia kitaip**: Su Chat Completions, 429 dažniausiai neleisdavo pradėti srauto. Su Responses API srautu, 429 gali įvykti **srauto viduryje** – asinchroninis iteratorius meta išimtį. Visada apvyniokite srauto ciklą į `try/except` ir pateikite klaidos JSON eilutę, kad frontendas galėtų tai gražiai apdoroti.

17. **Srautinio transliavimo klaidų tvarkymas yra privalomas žiniatinklio programoms**: Šablonas `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` yra kritiškai svarbus. Be jo SSE/JSONL srautas tyliai nutrūksta dėl bet kokios serverio pusės klaidos, o frontend'as užstringa.
18. **Įrankių apibrėžimai turi būti naudojami plokščiu formatu**: Responses API tikisi `{"type": "function", "name": ..., "parameters": ...}` — ne Chat Completions įdėtą `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Tai dažniausia klaida migruojant funkcijų iškvietimo kodą.
19. **`pydantic_function_tool()` yra nesuderinamas**: `openai.pydantic_function_tool()` pagalbinė funkcija vis dar generuoja seną įdėtą formatą. Nenaudokite jos su `responses.create()`. Apibrėžkite įrankio schemas rankiniu būdu arba plokštinkite išvestį.
20. **Įrankio rezultatai naudoja `function_call_output`, o ne `role: tool`**: Po įrankio vykdymo pridėkite `{"type": "function_call_output", "call_id": ..., "output": ...}` — o ne `{"role": "tool", "tool_call_id": ..., "content": ...}`. Padėjėjo įrankio paklausai naudokite `messages.extend(response.output)` — ne rankinį `{"role": "assistant", "tool_calls": [...]}` žodyną.
21. **`strict: true` reikalauja `required` + `additionalProperties: false`**: Naudojant `strict: true` su įrankiu, kiekviena savybė turi būti įtraukta į `required` masyvą, o `additionalProperties` turi būti `false`. Jei trūksta bet kurio, sistema grąžins 400 klaidą.
22. **Funkcijos iškvietimo ID turi specifinius prefiksus**: Pateikiant keletą `function_call` elementų `input` lauke, `id` laukas turi prasidėti `fc_`, o `call_id` laukas turi prasidėti `call_` (pvz., `"id": "fc_example1", "call_id": "call_example1"`). Senas Chat Completions `call_` prefiksas `id` laukui nepriimamas.
23. **GitHub modeliai nepalaiko Responses API**: Jei programoje yra GitHub modelių kodo kelias (`base_url`, nukreipiantis į `models.github.ai` arba `models.inference.ai.azure.com`), jį reikia visiškai pašalinti. Migracijos kelio nėra — pereikite prie Azure OpenAI, OpenAI arba suderinamo vietinio galo taško.
24. **Turinio filtro klaidos kūno struktūra pasikeitė**: Chat Completions klaidos naudojo `error.body["innererror"]["content_filter_result"]` (vienaskaita). Responses API klaidos naudoja `error.body["content_filters"][0]["content_filter_results"]` (daugiskaita, masyvo viduje). `innererror` raktas nebėra. Kode, kuris tiesiogiai pasiekia `innererror`, bus išmesta `KeyError` vykdymo metu — tai lengva praleisti migracijos metu, nes klaida pasireiškia tik kai turinio filtras tikrai įsijungia. Visada grep'inkite `innererror` migracijos metu.
25. **Žaliavinius HTTP kvietimus reikia perrašyti URL + kūną**: Programos, kurios tiesiogiai naudoja Azure OpenAI REST (per `requests`, `httpx`, `aiohttp`) kviesdamos `/openai/deployments/{name}/chat/completions?api-version=...` turi pereiti prie `/openai/v1/responses`. Užklausos kūnas naudoja `input` vietoje `messages`, reikalauja `max_output_tokens` ir `store`, o `api-version` užklausos parametras pašalinamas. Atsakymo kūno tekstas yra `output[0].content[0].text` — **ne** `output_text`, kuris yra SDK patogumo savybė, kurios nėra žaliaviniame REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->