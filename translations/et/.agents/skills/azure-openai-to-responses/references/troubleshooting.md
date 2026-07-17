# Tõrkeotsing, riskitabel ja tähelepanekud

## 400-tõrgete tõrkeotsing

| Tõrge | Parandus |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Tööriista definitsioon kasutab vana Chat Completions sisemist vormingut | Muutke struktuur `{"type": "function", "function": {"name": ...}}` vormingust `{"type": "function", "name": ..., "parameters": ...}` — nimi, kirjeldus ja parameetrid tuleks paigutada ülemisele tasemele |
| `unknown_parameter: input[N].tool_calls` | Mitme-käiguline tööriista tulemus kasutab vana Chat Completions vormingut | Asendage `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` kirjed `response.output` elementidega + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` tööriistast puudub `required` massiiv | Kui `strict: true`, peavad kõik omadused olema loetletud `required` sees ja `additionalProperties: false` peab olema määratud |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` tööriistast puudub `additionalProperties: false` | Lisage `"additionalProperties": false` parameetrite objektile |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Vähe-käiguline function_call ID-l vale eesliide | Function call ID-d peavad algama `fc_` (nt `fc_example1`), mitte `call_` |
| `missing_required_parameter: text.format.name` | Lisage vormingu sõnastikule `"name"` võti (nt `"name": "Output"`) |
| `invalid_type: text.format` | Kontrollige, et `text.format` on sõnastik, mis sisaldab võtmeid `type`, `name`, `strict`, `schema` — mitte string |
| `invalid input content type` | Kasutage Chat `text` asemel `input_text`/`output_text` sisutüüpe |
| `invalid input content type` (pilt) | Pildisisu kasutab endiselt `"type": "image_url"` | Muutke `"type": "input_image"` |
| `Expected object, got string` `image_url` juures | `image_url` on endiselt pesastatud objekt `{"url": "..."}` | Muutke tavalise stringi kujule: `"image_url": "https://..."` või `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` `max_output_tokens` puhul | Azure OpenAI minimaalne väärtus on **16**. Testimisel kasutage 50+, tootmises 1000+ |
| `429 Too Many Requests` voogedastuse ajal | Päringute arv on piiratud. Pakendage voog edastamine `try/except` blokki, edastage vigade JSON frontendile, rakendage tagasilükkamised/katsed uuesti |
| `KeyError: 'innererror'` sisufiltri tõrke korral | Sisufiltri tõrke keha struktuur muutunud Responses API-s | Chat Completions kasutas `error.body["innererror"]["content_filter_result"]`; Responses API-s tuleb kasutada `error.body["content_filters"][0]["content_filter_results"]` (mitmuses, massiivi sees). Kirjutage kogu `innererror` ligipääs ümber. |

---

## Migratsiooni riskitabel

| Sümptom | Tõenäoline viga | Parandus |
|---------|---------------|-----|
| Tühi `output_text` / katkendlik vastus | `max_output_tokens` liiga madal põhjendusmudelite puhul | Määrake `max_output_tokens=1000` või rohkem — põhjendusmudelid loevad tokeneid piirangu hulka |
| `400 invalid_type: text.format` | Edastati `response_format` string `text.format` sõnastiku asemel | Kasutage `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` `/openai/v1/responses` lõpus | Vale `base_url` — puudub `/openai/v1/` lõpp | Veenduge, et `base_url=f"{endpoint}/openai/v1/"` (kaasalõpuga kaldkriips) |
| `401 Unauthorized` pärast üleminekut `OpenAI()` kasutamisele | `api_key` pole määratud või tokeni pakkuja polnud korrektselt edasi antud | EntraID puhul: `api_key=token_provider` (kõneldav). API võtme puhul: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Mudel tagastab `deployment not found` | `model` parameeter ei vasta teie Azure käivitusnimele | Kasutage `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — see on käivitusnime, mitte mudeli nimi |
| `json.loads(resp.output_text)` tõstab `JSONDecodeError` | Skeem pole kohaldatud või mudel ei toeta rangeid JSON-väljundeid | Veenduge, et skeemil on `"strict": True` ja kontrollige, et mudel toetab struktureeritud väljundit |
| Voogedastus ei saada ühtegi `delta` sündmust | Kontrollitakse vale sündmuse tüüpi | Filtreerige `event.type == "response.output_text.delta"`, mitte Chat-i `chat.completion.chunk` |
| `400` tõrge pildisisendi puhul pärast migratsiooni | Pildisisu tüüp pole uuendatud | Muutke `"type": "image_url"` → `"type": "input_image"` ja lagundage `"image_url": {"url": "..."}` → `"image_url": "..."` (tavaline string) |
| Tööriistakutsed korduvad lõpmatuseni | Järgmises päringus puudub tööriista tulemus `input`-s | Pärast tööriista käivitamist lisage järgneva päringu sisendi lõppu `{"type": "function_call_output", "call_id": ..., "output": ...}` kirje |
| `temperature` tõrge GPT-5 või o-seeria puhul | Selgelt määratud `temperature` väärtus erinev 1-st | Eemaldage `temperature` või seadke see `1`-ks GPT-5 ja o-seeria mudelite jaoks (o1, o3-mini, o3, o4-mini) |
| `top_p` tõrge o-seeria puhul | `top_p` ei ole toetatud | Eemaldage `top_p` kasutamine o-seeria mudelite puhul |
| `max_completion_tokens` tundmatu parameeter | Kasutatakse Azure-spetsiifilist parameetrit | Asendage `max_completion_tokens` parameetriga `max_output_tokens`. O-seeriale seadke väärtuseks 4096+ (põhjendusmudeli tokenid loevad kaasa) |
| O-seeria tühi või katkendlik väljund | `max_output_tokens` liiga madal | O-seeria kasutab sisemiselt põhjendus-tekeneid. Määrake `max_output_tokens=4096` või rohkem — mitte vahemikus 500–1000 |
| `400 integer_below_min_value` `max_output_tokens` puhul | Väärtus alla 16 | Azure OpenAI nõuab, et `max_output_tokens >= 16`. Kasutage 50+ suitsutestide jaoks, 1000+ tootmises |
| `429 Too Many Requests` voogu edastades | Azure OpenAI päringute limiit ületatud | Voog katkeb vaikselt ilma veahalduseta. Pakkige iga `async for event in await coroutine:` tsükkel `try/except` plokki ja edastage frontendile `{"error": str(e)}` |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Vale rentnik või pole sisse logitud | Edastage `tenant_id=os.getenv("AZURE_TENANT_ID")` selgesõnaliselt. Käivitage kohapeal `azd auth login --tenant <tenant-id>` |
| `404 Not Found` GitHub mudelite kasutamisel (`models.github.ai`) | GitHub mudelid ei toeta Responses API-d | Eemaldage GitHub mudelite kooditee täielikult. Kasutage Azure OpenAI, OpenAI või ühilduvat kohalikku lõpp-punkti (nt Ollama Responses toe jaoks) |
| MAF `OpenAIChatCompletionClient` kasutab endiselt Chat Completions | Kasutatakse vana MAF klienti versioonis 1.0.0+ | MAF 1.0.0+ puhul kasutab `OpenAIChatClient` vaikimisi Responses API-t. Asendage `OpenAIChatCompletionClient` `OpenAIChatClient`-ga. Versioonide eel 1.0.0 puhul uuendage `agent-framework-openai>=1.0.0`. |
| LangChain agent tagastab tühja või kukub tööriistakutse tõttu läbi | `ChatOpenAI` ei kasuta Responses API-t | Lisage `use_responses_api=True` `ChatOpenAI(...)`. Muutke vastuses `.content` → `.text`. |
| `KeyError: 'innererror'` sisufiltri tõrke käsitlemisel | Veateate keha struktuur muutunud Responses API-s | Kirjutage `error.body["innererror"]["content_filter_result"]["jailbreak"]` ümber `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` kiht on eemaldatud; sisufiltri üksikasjad on nüüd tipptaseme `content_filters` massiivis, kus igal elemendil on mitmuses `content_filter_results`. |
| Otse HTTP-kõne `/openai/deployments/.../chat/completions` annab 404 | Vana Chat Completions REST lõpp-punkt | Ümber suunake URL `/openai/v1/responses`. Muutke päringu keha: `messages` → `input`, lisage `max_output_tokens` + `store: false`, eemaldage päringu parameeter `api-version`. Muutke vastuse töötlemist: `choices[0].message.content` → `output[0].content[0].text` (pange tähele: `output_text` on SDK mugavusomadus, mida ei ole toore REST JSON-is). |

---

## Tähelepanekud

1. Kui varem kasutasite vestluse oleku haldamiseks Chat Completionsit, hallake oma olekut nüüd ekspliciitselt Responses abil.
2. Eelistage `max_output_tokens` vanale `max_tokens` parameetrile.
3. Kui migreerite `gpt-5` mudelile, veenduge, et `temperature` ei oleks määratud või oleks seatud väärtusele `1`.
4. Asendage Chat `content[].type: "text"` Responses `content[].type: "input_text"`-ga kasutaja või süsteemi sisendite puhul.
5. `text.format` puhul kasutage korrektset sõnastikku (nt `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), mitte puhast stringi.
6. `seed` parameeter ei ole Responses API-s toetatud; eemaldage see päringutest.
7. **Põhjendus**: Lisage `reasoning` ainult siis, kui algne kood seda juba kasutas. Ärge lisage `reasoning` parameetrit API-kutsetesse, kus seda varem polnud — paljud mitte-põhjendavad mudelid seda ei toeta.
8. **`max_output_tokens` suuruse valik**: Põhjendusmudelite (GPT-5-mini, GPT-5, o-seeria) puhul kasutage `max_output_tokens=4096` või rohkem — mitte 50–1000. Mudel kasutab enne nähtava väljundi genereerimist sisemiselt põhjendus-tokenid; liiga madalad piirangud põhjustavad katkendlikke või tühje vastuseid.
9. **O-seeria `max_completion_tokens`**: Kui algne kood kasutas Azure-spetsiifilist `max_completion_tokens` parameetrit, asendage see `max_output_tokens` parameetriga. Responses API ei toeta `max_completion_tokens`-i.
10. **O-seeria `reasoning_effort`**: Kui algne kood kasutas `reasoning_effort` (low/medium/high), migreerige see Responses API-sse kui `reasoning={"effort": "<väärtus>"}`.
11. **O-seeria voogedastuse viivitus**: O-seeria mudelid teostavad sisemist põhjendamist enne väljundi genereerimist. Voogedastuse puhul oodake pikemat viivitust enne esimest `response.output_text.delta` sündmust. See on normaalne — mudel on põhjendamas, mitte kinni jäänud.
9. **`_azure_ad_token_provider` on eemaldatud**: `AsyncOpenAI` / `OpenAI` objektidel ei ole `_azure_ad_token_provider` atribuuti. Testid või kood, mis sellele viitab, ebaõnnestuvad `AttributeError`-iga. Tokeni pakkuja edastatakse `api_key` kaudu ja seda ei saa kliendi objektist otse lugeda.
10. **Snapshots / kuldsed failid**: Kui testikomplekt kasutab snapshot-testimist, peavad KÕIK snapshot-failid, mis sisaldavad Chat Completions voogedastuse kujundeid (`choices[0]`, `content_filter_results`, `function_call` jms), olema uuendatud uuele Responses vormingule. Selle möödaviimine põhjustab snapshot-erialduste ebaõnnestumisi.
11. **Mock monkeypatch tee**: Monkeypatch sihtkoht muutus `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (või sünkroonseks `Responses.create`). Vana tee kasutamine ei taga, et mock interceptib kõnesid — testid kas kasutavad päris API-t või küsitakse läbi.
12. **`input`, mitte `messages`**: Mock-funktsioonides tuleb lugeda `kwargs.get("input")`, mitte `kwargs.get("messages")`. Responses API kasutab `input` vestluse ajaloo jaoks.
13. **Keskkonnamuutuja nimed**: Azure Identity SDK kasutab `AZURE_CLIENT_ID` (mitte `AZURE_OPENAI_CLIENT_ID`) `ManagedIdentityCredential(client_id=...)` jaoks. Nimede muuta testides, `.env` failides, rakenduse seadetes ja Bicep/infra skriptides.
14. **`max_output_tokens` miinimum on 16**: Azure OpenAI keeldub väiksematest väärtustest veaga `400 integer_below_min_value`. Kasutage suitsutestidele `50` ja tootmiseks `1000+`. Vanal `max_tokens` parameetril sellist piirangut polnud.
15. **`tenant_id` `AzureDeveloperCliCredential` jaoks**: Kui Azure OpenAI ressurss asub teises tenantis, PEATE andma `tenant_id` selgesõnaliselt — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Ilma selleta kasutatakse vaikimisi valesid rentnike ja tagastatakse `401`.
16. **Päringute limiidid avalduvad voogedastuses eraldi**: Chat Completions kasutamisel takistas 429 tüüpi viga tavaliselt voo algust. Responses API voogedastusel võib 429 esineda VOOS (keset voogu) — async iterator tõstab erandi. Pakkige voogedraama tsükkel alati `try/except` plokki ja edastage vigade JSON postitus frontendile, et see saaks vea korrektselt töödelda.

17. **Voogedastuse vea käitlemine on veebiäppide jaoks kohustuslik**: Muster `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` on kriitiline. Ilma selleta sureb SSE/JSONL voog serveripoolse vea korral vaikselt välja ja kasutajaliides hangub.
18. **Tööriistade definitsioonid peavad olema lamedas formaadis**: Responses API eeldab `{"type": "function", "name": ..., "parameters": ...}` — mitte Chat Completions pesastatud `{"type": "function", "function": {"name": ..., "parameters": ...}}`. See on kõige levinum migratsiooniviga funktsioonide kutsumise koodi puhul.
19. **`pydantic_function_tool()` ei sobi kokku**: `openai.pydantic_function_tool()` abimees genereerib endiselt vana pesastatud formaadi. Ära kasuta seda koos `responses.create()`-ga. Määra tööriista skeemid käsitsi või lamevormista väljund.
20. **Tööriistade tulemused kasutavad `function_call_output`, mitte `role: tool`**: Pärast tööriista käivitamist lisa `{"type": "function_call_output", "call_id": ..., "output": ...}` — mitte `{"role": "tool", "tool_call_id": ..., "content": ...}`. Assistentide tööriistapäringu puhul kasuta `messages.extend(response.output)` — mitte käsitsi loodud `{"role": "assistant", "tool_calls": [...]}` sõnastikku.
21. **`strict: true` vajab `required` + `additionalProperties: false`**: Kui tööriistal on kasutusel `strict: true`, peab iga atribuut olema listitud `required` massiivis ja `additionalProperties` peab olema `false`. Mõlema puudumine põhjustab 400 vea.
22. **Funktsioonikõnede ID-del on kindlad eesliited**: Kui sisendis kasutatakse vähese arvu näidislahendusega `function_call` elemente, peab `id` väli algama `fc_` ja `call_id` väli algama `call_` (nt `"id": "fc_example1", "call_id": "call_example1"`). Vanade Chat Completions `call_` eesliite kasutamine `id` puhul lükatakse tagasi.
23. **GitHub Models ei toeta Responses API-d**: Kui äpil on GitHub Models kooditee (`base_url`, mis osutab `models.github.ai` või `models.inference.ai.azure.com`), eemalda see täielikult. Migratsiooniteed puudub — kasuta Azure OpenAI, OpenAI või sobivat kohalikku lõpp-punkti.
24. **Sisu filtri veateate keha struktuur on muutunud**: Chat Completions vead kasutasid `error.body["innererror"]["content_filter_result"]` (ainsuses). Responses API vead kasutavad `error.body["content_filters"][0]["content_filter_results"]` (mitmuses, massiivi sees). Võtit `innererror` enam ei eksisteeri. Kood, mis otse juurde pääseb `innererror`-ile, viskab käitusajal `KeyError` — seda on migratsiooni ajal lihtne märkamata jätta, kuna see avaldub ainult siis, kui sisu filter tegelikult käivitub. Alati otsi migratsiooni ajal `innererror` järgi.
25. **Puhaste HTTP kõnede puhul on vaja URL-i ja keha ümberkirjutust**: Äpid, mis kutsuvad Azure OpenAI REST-i otse (`requests`, `httpx`, `aiohttp` kaudu) kasutades `/openai/deployments/{name}/chat/completions?api-version=...`, peavad lülituma `/openai/v1/responses` peale. Päringu kehast kasutatakse `input` asemel `messages`, nõutakse `max_output_tokens` ja `store`, ning `api-version` parameeter jäetakse välja. Vastuse keha tekst on nähtaval `output[0].content[0].text` juures — **mitte** `output_text`, mis on SDK mugavusomadus, mida puhas REST JSON ei sisalda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->