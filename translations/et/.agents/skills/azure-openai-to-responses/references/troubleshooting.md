# Tõrkeotsing, Riskitabel ja Põhjuslikud Vead

## 400 veateadete tõrkeotsing

| Viga | Parandus |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Tööriista definitsioon kasutab vana Chat Completions kronnformaat | Tõmba lahti struktuur vormist `{"type": "function", "function": {"name": ...}}` kujule `{"type": "function", "name": ..., "parameters": ...}` — nimi, kirjeldus, parameetrid on peatasandil |
| `unknown_parameter: input[N].tool_calls` | Mitme vooru tööriista tulemused kasutavad vana Chat Completions formaati | Asenda `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` üksustega `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` tööriistast puudub `required` massiiv | Kui `strict: true`, peavad kõik omadused olema loetletud `required` sees ja `additionalProperties: false` peab olema määratud |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` tööriistast puudub `additionalProperties: false` | Lisa parameetrite objektile `"additionalProperties": false` |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Vähese näitega function_call ID-l vale eesliide | Funktsiooni kõnekoodid peavad algama `fc_` (nt `fc_example1`), mitte `call_` |
| `missing_required_parameter: text.format.name` | Lisa formaadi sõnastikku `"name"` võti (nt `"name": "Output"`) |
| `invalid_type: text.format` | Veendu, et `text.format` on sõnastik koos võtmetega `type`, `name`, `strict`, `schema` — mitte string |
| `invalid input content type` | Kasuta Chat'i `text` asemel `input_text`/`output_text` sisutüüpe |
| `invalid input content type` (pilt) | Pildisisu kasutab endiselt `"type": "image_url"` | Muuda `"type": "input_image"` |
| `Expected object, got string` viga `image_url` puhul | `image_url` on endiselt pesastatud objekt `{"url": "..."}` | Tõmba lahti ja kasuta tavalist stringi: `"image_url": "https://..."` või `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` `max_output_tokens` puhul | Azure OpenAI minimaalne on **16**. Testidel kasuta 50+ ja tootmises 1000+. |
| `429 Too Many Requests` voogedastuse ajal | Päringute limiit ületatud. Pane voogedastus `try/except` ploki sisse, edasta veateade JSONina frontendile, rakenda tagasilöök-katsetus. |
| `KeyError: 'innererror'` sisu filtri veas | Sisu filtri vea keha struktuur muutus Responses API-s | Chat Completions kasutas `error.body["innererror"]["content_filter_result"]`; Responses API-s on `error.body["content_filters"][0]["content_filter_results"]` (mitmus, massiivis). Kirjuta kõik `innererror` pääsud ümber. |

---

## Migratsiooni riskitabel

| Sümptom | Tõenäoline viga | Parandus |
|---------|---------------|-----|
| Tühi `output_text` / katkestatud vastus | Liiga madal `max_output_tokens` mõtlemismudelite puhul | Sea `max_output_tokens=1000` või rohkem — mõtlemistokeneid loetakse limiidi alla |
| `400 invalid_type: text.format` | Üles antud `response_format` oli string, mitte `text.format` sõnastik | Kasuta `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` `/openai/v1/responses` päringu puhul | Vale `base_url` — puudub `/openai/v1/` lõpp | Veendu, et `base_url=f"{endpoint}/openai/v1/"` (kaldkriips lõpus) |
| `401 Unauthorized` peale `OpenAI()` kasutusele võtmist | `api_key` pole määratud või tokenipakkujat ei saadetud õigesti | EntraID jaoks: `api_key=token_provider` (kõnelevaldne). API võtme puhul: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Mudel tagastab `deployment not found` | `model` parameeter ei vasta Azure juurutuse nimele | Kasuta `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — see on juurutuse nimi, mitte mudelinimi |
| `json.loads(resp.output_text)` viskab `JSONDecodeError` | Šeemat ei rakendata või mudel ei toeta range struktuuriga JSON-i | Veendu, et `schema` sisaldab `"strict": True` ja mudel toetab struktureeritud väljundit |
| Voogedastus ei paku `delta` sündmusi | Vale sündmuse tüübi kontroll | Filtreeri `event.type == "response.output_text.delta"`, mitte Chat'i `chat.completion.chunk` |
| `400` pildisisendi vead pärast migratsiooni | Pildisisu tüüp pole uuendatud | Muuda `"type": "image_url"` → `"type": "input_image"` ja tõmba lahti `"image_url": {"url": "..."}` → `"image_url": "..."` (tavaline string) |
| Tööriista kõned jäävad lõputusse tsüklisse | Järgmise sisendi `input` seadetes puudub tööriista tulemus | Pärast tööriista täitmist lisa järgmise päringu `input` sisse üksus `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `temperature` viga GPT-5 või o-seeria puhul | Selgesõnaline `temperature` väärtus, mis pole 1 | Eemalda `temperature` või sea see `1`-ks GPT-5 ja o-seeria mudelite puhul (o1, o3-mini, o3, o4-mini) |
| `top_p` viga o-seeria mudelite puhul | `top_p` pole toetatud | Eemalda `top_p` kasutamisel o-seeria mudelite jaoks |
| `max_completion_tokens` pole tunnustatud | Kasutatakse Azure’i spetsiifilist parameetrit | Asenda `max_completion_tokens` parameetriga `max_output_tokens`. Sea väärtuseks o-seeriale 4096+ (mõtlemistokeneid loetakse limiidi alla). |
| O-seeria tühi või katkestatud väljund | Liiga madal `max_output_tokens` | O-seeria kasutab sisemiselt mõtlemistokeneid. Sea `max_output_tokens=4096` või kõrgem — mitte 500–1000. |
| `400 integer_below_min_value` `max_output_tokens` puhul | Väärtus allpool 16 | Azure OpenAI nõuab `max_output_tokens >= 16`. Kasuta suitsutestidel 50+ ja tootmises 1000+. |
| `429 Too Many Requests` voogu keskel | Azure OpenAI-l piirang | Voog katkeb vaikides ilma veateateta. Kata alati `async for event in await coroutine:` tsükkel `try/except` plokiga ja edasta `{"error": str(e)}` frontendile. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Vale tenant või pole sisse logitud | Pane selgelt `tenant_id=os.getenv("AZURE_TENANT_ID")`. Käivita lokaalselt `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` GitHub mudelite puhul (`models.github.ai`) | GitHub mudelid ei toeta Responses API-d | Eemalda GitHub mudelite kooditee täielikult. Kasuta Azure OpenAI, OpenAI või sobivat kohalikku lõpp-punkti (nt Ollama Responses toe jaoks). |
| MAF `OpenAIChatCompletionClient` kasutab ikka Chat Completions | Kasutatakse vananenud MAF klienti versioonis 1.0.0+ | MAF 1.0.0+ `OpenAIChatClient` kasutab vaikimisi Responses API-d. Asenda `OpenAIChatCompletionClient` `OpenAIChatClient`-iga. Enne 1.0.0 uuenda `agent-framework-openai>=1.0.0`. |
| LangChain agendi vastus tühi või ebaõnnestub tööriistakutsude tõttu | `ChatOpenAI` ei kasuta Responses API-d | Lisa `use_responses_api=True` `ChatOpenAI(...)`. Muuda ka `.content` → `.text` vastusteks. |
| `KeyError: 'innererror'` sisu filtri vea töötlejas | Veateate keha struktuur muutus Responses API-s | Kirjuta ümber `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` kesta enam pole, sisu filtrite detailid on nüüd tipp-taseme `content_filters` massiivis koos mitmusega `content_filter_results` iga üksuse sees. |
| Päris HTTP kõne `/openai/deployments/.../chat/completions` tagastab 404 | Vana Chat Completions REST lõpp-punkt | Kirjuta URL ümber `/openai/v1/responses`-ks. Muuda päringu keha: `messages` → `input`, lisa `max_output_tokens` ja `store: false`, eemalda `api-version` parameeter. Muuda vastuse parsimist: `choices[0].message.content` → `output[0].content[0].text` (märkus: `output_text` on SDK mugavusomadus, pole otseses REST JSON-is). |

---

## Põhjuslikud vead

1. Kui kasutasid varem Chat Completions vestluse oleku hoidmeks, halda olekut nüüd selgesõnaliselt Responses abil.
2. Eelista `max_output_tokens` asemel vana `max_tokens` kasutamist.
3. Kui migrereid `gpt-5` peale, veendu, et `temperature` pole määratud või on seatud `1`.
4. Asenda Chat `content[].type: "text"` Responses `content[].type: "input_text"`-ga kasutaja/süsteemi sisenditel.
5. `text.format` puhul anna korralik sõnastik (nt `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), mitte lihtne string.
6. Parameeter `seed` ei ole Responses API-s toetatud; eemalda see päringutest.
7. **Reasoning (mõtlemine)**: Kaasa `reasoning` ainult kui seda originaalkoodis juba kasutati. Ära lisa `reasoning` API kõnedesse, kus seda polnud — paljud mudelid (nt gpt-4o-mini) seda ei toeta.
8. **`max_output_tokens` suurus**: Mõtlemismudelite (GPT-5-mini, GPT-5, o-seeria) puhul kasuta `max_output_tokens=4096` või rohkem — mitte 50–1000. Mudel kasutab sisemiselt mõtlemistokeneid enne nähtava väljundi genereerimist; liiga madal piir põhjustab katkestatud või tühje vastuseid.
9. **O-seeria `max_completion_tokens`**: Kui originaalkood kasutas `max_completion_tokens` (Azure’i spetsiifiline o-seeriale), asenda see `max_output_tokens`-ga. Responses API ei aktsepteeri `max_completion_tokens`.
10. **O-seeria `reasoning_effort`**: Kui originaalkood kasutab `reasoning_effort` (madal/keskmine/kõrge), migreeri see vormi `reasoning={"effort": "<väärtus>"}` Responses API kõnes.
11. **O-seeria voogedastuse viivitus**: O-seeria mudelid teevad sisemisi mõtlemiskäike enne väljundi genereerimist. Voogedastuse puhul oota pikemat viivitust enne esimest `response.output_text.delta` sündmust. See on normaalne — mudel mõtleb, mitte ei ole hangunud.
9. **`_azure_ad_token_provider` on kadunud**: `AsyncOpenAI` / `OpenAI` objektidel pole `_azure_ad_token_provider` omadust. Testid või kood, mis sellele viitavad, kukuvad `AttributeError`-i. Tokeni pakkuja antakse edasi `api_key` kaudu ja seda ei ole võimalik kliendi objektil inspektida.
10. **Snapshot / golden failid**: Kui testkomplekt kasutab snapshot testimist, peavad **kõik** snapshot failid, mis sisaldavad Chat Completions voogedastuse kujusid (`choices[0]`, `content_filter_results`, `function_call`, jne) olema uuendatud uue Responses kujule. Seda on lihtne märkamata jätta ja see põhjustab snapshot võrdluse ebaõnnestumisi.
11. **Mock monkeypatch tee muutus**: Monkeypatch sihtkoht muudeti `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (või `Responses.create` süntroonis). Vanast teest kasutamisel ei juhtu midagi - mock ei püüa katseid kinni, testid lähevad otse reaalse API peale või ebaõnnestuvad.
12. **`input`, mitte `messages`**: Mock funktsioonid peavad lugema `kwargs.get("input")`, mitte `kwargs.get("messages")`. Responses API kasutab vestlusloo hoidmiseks `input`-i.
13. **Keskkonnamuutuja nimetused**: Azure Identity SDK kasutab `AZURE_CLIENT_ID` (mitte `AZURE_OPENAI_CLIENT_ID`) `ManagedIdentityCredential(client_id=...)` jaoks. Nimeta ümber testides, `.env` failides, rakenduse seadetes ja Bicep/infra skriptides.
14. **`max_output_tokens` miinimum on 16**: Azure OpenAI lükkab alla alla 16 väärtused koodiga `400 integer_below_min_value`. Kasuta suitsutestides väärtust 50 ja tootmises 1000+. Vana `max_tokens` puhul sellist miinimumi polnud.
15. **`tenant_id` `AzureDeveloperCliCredential` jaoks**: Kui Azure OpenAI ressurss asub teises tandentis, **pead** `tenant_id` selgesõnaliselt määrama — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Muul juhul kasutab kasutajatunnistus vaikimisi vale tenant’i ja tagastab `401`.
16. **Päringute limiidid voogedastusel avalduvad teisiti**: Chat Completions puhul takistas 429 tavaliselt voo käivitumist. Responses API voogedastuse puhul võib 429 tekkida **voo keskel** — asünkroonne iteratsioon viskab erindi. Kata alati voogedastuse tsükkel `try/except` plokiga ja edasta veateade JSON-i reana, et frontend saaks selle ereda moodi töödelda.

17. **Voogedastusvea käsitlemine on veebirakenduste jaoks kohustuslik**: Muster `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` on kriitiline. Ilma selleta sureb SSE/JSONL voog serveripoolse vea korral vaikselt välja ja kasutajaliides hangub.
18. **Tööriistade definitsioonid peavad kasutama lamedat formaati**: Responses API ootab `{"type": "function", "name": ..., "parameters": ...}`, mitte Chat Completions'i pesastatud `{"type": "function", "function": {"name": ..., "parameters": ...}}`. See on kõige levinum migratsiooniviga funktsiooni kutsumise koodis.
19. **`pydantic_function_tool()` on sobimatu**: Abikäsk `openai.pydantic_function_tool()` genereerib endiselt vana pesastatud formaadi. Ära kasuta seda koos `responses.create()`-ga. Määra tööriistade skeemid käsitsi või lamenda väljund.
20. **Tööriista tulemused kasutavad `function_call_output`, mitte `role: tool`**: Pärast tööriista käivitamist lisa `{"type": "function_call_output", "call_id": ..., "output": ...}`, mitte `{"role": "tool", "tool_call_id": ..., "content": ...}`. Assistiendi tööriista päringu puhul kasuta `messages.extend(response.output)`, mitte käsitsi loodud `{"role": "assistant", "tool_calls": [...]}` sõnastikku.
21. **`strict: true` nõuab `required` + `additionalProperties: false`**: Kui kasutad tööriistal `strict: true`, peab iga omadus olema kirjas `required` massiivis ja `additionalProperties` peab olema `false`. Ühegi puudumine põhjustab 400 veateate.
22. **Funktsioonikõnede ID-del on kindlad eesliited**: Kui esitad vähese näitega `function_call` elemente `input` sees, peab `id` väli algama `fc_` ja `call_id` väli `call_`-ga (nt `"id": "fc_example1", "call_id": "call_example1"`). Vana Chat Completions `call_` eesliite kasutamine `id` jaoks lükatakse tagasi.
23. **GitHub Models ei toeta Responses API-t**: Kui rakendusel on GitHub Models kooditee (`base_url`, mis osutab `models.github.ai` või `models.inference.ai.azure.com`), eemalda see täielikult. Migratsioonirada puudub — vaheta Azure OpenAI, OpenAI või ühilduva lokaalse lõpp-punkti vastu.
24. **Sisufiltri veakuva struktuur muutus**: Chat Completions vigades kasutati `error.body["innererror"]["content_filter_result"]` (ainsus). Responses API vigades kasutatakse `error.body["content_filters"][0]["content_filter_results"]` (mitmus, massiivi sees). Võtit `innererror` enam ei ole. Kood, mis otse `innererror`-ile ligi pääseb, tõstab käitusaegse `KeyError` — seda on migratsioonis lihtne tähelepanuta jätta, sest see ilmneb ainult siis, kui sisufilter tegelikult käivitub. Alati otsi `innererror` migratsiooni ajal.
25. **Tooreid HTTP-kõnesid tuleb ümber kirjutada URL-i ja keha osas**: Rakendused, mis kutsuvad Azure OpenAI REST-i otse (kasutades `requests`, `httpx`, `aiohttp`) ja kasutavad `/openai/deployments/{name}/chat/completions?api-version=...`, peavad vahetama `/openai/v1/responses` vastu. Taotluskeha kasutab `input` asemel `messages`, nõuab `max_output_tokens` ja `store` atribuute ning `api-version` päringupärand jäetakse ära. Vastuskeha tekst asub `output[0].content[0].text`-s — **mitte** `output_text`, mis on SDK mugavusatribuut ja puudub toore REST JSON-i sees.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->