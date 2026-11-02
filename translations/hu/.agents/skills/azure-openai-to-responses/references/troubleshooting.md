# Hibakeresés, Kockázati tábla és Buktatók

## 400-as hibák hibakeresése

| Hiba | Javítás |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Az eszköz definíció régi, Chat Completions beágyazott formátumot használ | Lapítsuk ki a `{"type": "function", "function": {"name": ...}}` formátumot `{"type": "function", "name": ..., "parameters": ...}` formátumra — a name, description, parameters a legfelső szinten legyen |
| `unknown_parameter: input[N].tool_calls` | Többfordulós eszköz eredmények régi Chat Completions formátumot használnak | Cseréljük a `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` elemeket a `response.output` elemekre + `{"type": "function_call_output", "call_id": ..., "output": ...}` formátumra |
| `invalid_function_parameters: 'required' is required` | `strict: true` eszköz hiányzó `required` tömbbel | Ha `strict: true`, akkor az összes tulajdonságnak szerepelnie kell a `required` listában, és az `additionalProperties: false` beállítást meg kell adni |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` eszköz hiányzó `additionalProperties: false` beállítással | Adjuk hozzá az `"additionalProperties": false` paraméter objektumhoz |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID rossz előtaggal | A function call ID-knak `fc_`-val kell kezdődniük (pl. `fc_example1`), nem `call_`-lal |
| `missing_required_parameter: text.format.name` | Adjuk hozzá a `"name"` kulcsot a format szótárhoz (pl. `"name": "Output"`) |
| `invalid_type: text.format` | Győződjünk meg róla, hogy a `text.format` egy szótár `type`, `name`, `strict`, `schema` kulcsokkal — ne legyen egy egyszerű string |
| `invalid input content type` | Használjunk `input_text`/`output_text` tartalomtípusokat Chat `text` helyett |
| `invalid input content type` (kép) | A kép tartalomtípus még mindig `"type": "image_url"` | Cseréljük `"type": "input_image"`-re |
| `Expected object, got string` az `image_url`-en | Az `image_url` még mindig egy beágyazott objektum `{"url": "..."}` | Lapítsuk ki sima stringre: `"image_url": "https://..."` vagy `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` a `max_output_tokens`-nál | Az Azure OpenAI-nál minimum **16** az érték. Tesztekhez használjunk 50+-et, élesben 1000+-et. |
| `429 Too Many Requests` streaming közben | Lekorlátozták a hívásokat. Csomagoljuk a stream-et `try/except` blokkba, adjuk vissza a hiba JSON-t frontendnek, implementáljunk visszaállási/kísérleti logikát. |
| `KeyError: 'innererror'` a tartalomszűrő hiba esetén | A tartalomszűrő hibák struktúrája változott a Responses API-ban | A Chat Completions a `error.body["innererror"]["content_filter_result"]`-t használta; a Responses API a `error.body["content_filters"][0]["content_filter_results"]` (többesszám, tömbben) kulcsot használja. Írjuk át az összes `innererror` elérést. |

---

## Migrációs Kockázati Tábla

| Tünet | Valószínű hiba | Javítás |
|---------|---------------|-----|
| Üres `output_text` / levágott válasz | `max_output_tokens` túl alacsony érvelő modelleknél | Állítsuk be `max_output_tokens=1000` vagy magasabb értékre — az érvelés tokenjei beleszámítanak a limitbe |
| `400 invalid_type: text.format` | `response_format` stringet adtak át `text.format` dictionary helyett | Használjuk a `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` formátumot |
| `404 Not Found` a `/openai/v1/responses` végponton | Hibás `base_url` — hiányzik a `/openai/v1/` utótag | Győződjünk meg róla, hogy `base_url=f"{endpoint}/openai/v1/"` (az utolsó perjellel együtt) |
| `401 Unauthorized` az `OpenAI()` használat átállása után | `api_key` nincs beállítva vagy hibás token szolgáltató | EntraID esetén: `api_key=token_provider` (hívható). API kulcs esetén: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| A modell `deployment not found` hibát ad vissza | A `model` paraméter nem egyezik az Azure üzembe helyezés nevével | Használjuk `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]`-et — ez az üzembe helyezés neve, nem a modell neve |
| `json.loads(resp.output_text)` JSONDecodeError-t dob | A séma nincs kikényszerítve vagy a modell nem támogatja a szigorú JSON-t | Győződjünk meg róla, hogy a séma tartalmazza `"strict": True`-t, és a modell támogatja a strukturált kimenetet |
| A stream nem ad ki `delta` eseményeket | Rossz eseménytípust szűrünk | Szűrjünk az `event.type == "response.output_text.delta"` értékre, ne a Chat `chat.completion.chunk` eseményre |
| Kép bemenet `400` hibát ad migráció után | A kép tartalomtípus nincs frissítve | Cseréljük `"type": "image_url"` → `"type": "input_image"` és lapítsuk ki a `"image_url": {"url": "..."}` → `"image_url": "..."` (sima string) |
| Az eszközhívások végtelen ciklusba kerülnek | Hiányzik az eszköz eredmény a következő `input`-ból | Egy eszköz végrehajtása után adjunk hozzá egy `{"type": "function_call_output", "call_id": ..., "output": ...}` elemet a következő kérés `input`-jához |
| `temperature` hiba GPT-5 vagy o-sorozat esetén | Explicit `temperature` érték 1-től eltérő | Távolítsuk el a `temperature` paramétert vagy állítsuk 1-re GPT-5 és o-sorozat modellekhez (o1, o3-mini, o3, o4-mini) |
| `top_p` hiba o-sorozat esetén | `top_p` nem támogatott | Távolítsuk el a `top_p` paramétert, amikor o-sorozat modelleket célozunk |
| `max_completion_tokens` nem ismert | Azure-specifikus paramétert használnak | Cseréljük ki a `max_completion_tokens`-t `max_output_tokens`-re. Állítsuk 4096+-ra o-sorozatnál (az érvelő tokenek beszámítanak a limitbe). |
| Üres vagy levágott kimenet o-sorozatról | `max_output_tokens` túl alacsony | Az o-sorozat belső érvelő tokeneket használ. Állítsuk be `max_output_tokens=4096` vagy magasabbra — ne 500–1000-re. |
| `400 integer_below_min_value` a `max_output_tokens`-nál | Érték kevesebb, mint 16 | Az Azure OpenAI előírja, hogy `max_output_tokens >= 16` legyen. Használjunk 50+-et smoke tesztekhez, 1000+-et éles környezetben. |
| `429 Too Many Requests` streaming közben | Lekorlátozta az Azure OpenAI | A stream hiba nélkül megszakad. Mindig csomagoljuk `async for event in await coroutine:`-t `try/except`-be és adjunk vissza `{"error": str(e)}` JSON sorokat a frontendnek. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Hibás tenant vagy nincs bejelentkezve | Adjunk át explicit módon `tenant_id=os.getenv("AZURE_TENANT_ID")` paramétert. Lokálisan futtassuk `azd auth login --tenant <tenant-id>` parancsot. |
| `404 Not Found` GitHub modellek (`models.github.ai`) használata közben | A GitHub modellek nem támogatják a Responses API-t | Távolítsuk el teljesen a GitHub modellek kódútvonalát. Használjunk Azure OpenAI-t, OpenAI-t vagy kompatibilis helyi végpontot (pl. Ollama Responses támogatással). |
| MAF `OpenAIChatCompletionClient` még mindig használja a Chat Completions-t | Legacy MAF kliens 1.0.0+ verzióban | MAF 1.0.0+ esetén az `OpenAIChatClient` alapértelmezetten a Responses API-t használja. Cseréljük az `OpenAIChatCompletionClient`-et `OpenAIChatClient`-re. Régebbi verzió előtt frissítsünk `agent-framework-openai>=1.0.0`-ra. |
| LangChain agent üres választ ad vagy hibázik eszközhívásokkor | `ChatOpenAI` nem használja a Responses API-t | Adjunk hozzá `use_responses_api=True` paramétert a `ChatOpenAI(...)`-hoz. Változtassuk meg a válasz üzenetek `.content` mezőjét `.text`-re. |
| `KeyError: 'innererror'` a tartalomszűrő hiba kezelésénél | A hiba test szerkezete változott a Responses API-ban | Írjuk át `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Az `innererror` burkoló megszűnt; a tartalomszűrő részletek most egy legfelsőbb szintű `content_filters` tömbben vannak, minden elemben `content_filter_results` (többesszám). |
| RAW HTTP hívás `/openai/deployments/.../chat/completions` végpontra 404-et ad | Régi Chat Completions REST végpont | Írjuk át az URL-t `/openai/v1/responses`-re. Változtassuk a kérés törzsét: `messages` → `input`, adjuk hozzá `max_output_tokens` + `store: false`, vegyük ki az `api-version` lekérdezési paramétert. Változtassuk meg a válasz feldolgozást: `choices[0].message.content` → `output[0].content[0].text` (az `output_text` SDK kényelem, a raw REST JSON-ban nincs). |

---

## Buktatók

1. Ha korábban Chat Completions-t használtál a beszélgetési állapot kezelésére, akkor kezeljük explicit módon az állapotot a Responses segítségével.
2. Részesítsd előnyben a `max_output_tokens` paramétert a régi `max_tokens` helyett.
3. `gpt-5`-re való migrációkor győződj meg róla, hogy a `temperature` nincs megadva vagy 1-re van állítva.
4. Cseréld le a Chat `content[].type: "text"`-et Responses `content[].type: "input_text"`-re a felhasználói és rendszerbemeneteknél.
5. A `text.format` esetén adj meg megfelelő szótárat (pl. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ne egyszerű stringet.
6. A `seed` paraméter nincs támogatva a Responses API-ban; távolítsd el a kérésből.
7. **Érvelés**: Csak akkor add hozzá a `reasoning`-et, ha az eredeti kód már használta. Ne adj hozzá `reasoning`-et olyan API hívásokhoz, amelyek nem tartalmazták — sok nem érvelő modell nem támogatja ezt a paramétert.
8. **`max_output_tokens` méretezése**: Érvelő modellekhez (GPT-5-mini, GPT-5, o-sorozat) használj `max_output_tokens=4096` vagy nagyobb értéket — ne 50–1000-et. A modell belsőleg használ érvelő tokeneket mielőtt látható kimenetet generál; ha a limit túl alacsony, a válasz levágott vagy üres lesz.
9. **O-sorozat `max_completion_tokens`**: Ha az eredeti kód használta az Azure-specifikus `max_completion_tokens` paramétert, cseréld ki `max_output_tokens`-re. A Responses API nem fogadja el a `max_completion_tokens`-t.
10. **O-sorozat `reasoning_effort`**: Ha az eredeti kód használta a `reasoning_effort` (low/medium/high) paramétert, migráld azt a Responses API `reasoning={"effort": "<érték>"}` formátumára.
11. **O-sorozat streamelési késleltetés**: Az o-sorozat modellek belső érvelést végeznek mielőtt kimenetet generálnak. Streamelés közben számíts arra, hogy az első `response.output_text.delta` esemény később érkezik. Ez normális — a modell érvel, nem akadt el.
9. **`_azure_ad_token_provider` megszűnt**: Az `AsyncOpenAI` / `OpenAI` nem rendelkezik `_azure_ad_token_provider` attribútummal. A tesztek vagy kód, ami ehhez az attribútumhoz hozzáférne, `AttributeError`-ral fog futni. A token szolgáltató az `api_key`-ként van átadva és nem elérhető közvetlenül a kliens objektumon.
10. **Snapshot / golden fájlok**: Ha a tesztcsomag snapshot tesztelést használ, akkor **minden** snapshot fájlt, ami Chat Completions stream formákat (pl. `choices[0]`, `content_filter_results`, `function_call`, stb.) tartalmaz, frissíteni kell az új Responses formára. Ezt könnyű elfelejteni és snapshot hibákat okoz.
11. **Mock monkeypatch útvonal**: A monkeypatch célpontja megváltozott `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (vagy szinkron esetén `Responses.create`). A régi útvonal használata csendben nem csinál semmit — a mock nem avatkozik be, a tesztek a valós API-t érik el vagy hibáznak.
12. **`input`, nem `messages`**: A mock függvényeknek a `kwargs.get("input")`-et kell olvasniuk, nem a `kwargs.get("messages")`-t. A Responses API az `input` mezőt használja a beszélgetési előzményekhez.
13. **Környezeti változó elnevezés**: Az Azure Identity SDK az `AZURE_CLIENT_ID`-t használja (nem az `AZURE_OPENAI_CLIENT_ID`-t) a `ManagedIdentityCredential(client_id=...)` esetén. Nevezd át a tesztekben, `.env` fájlokban, alkalmazás beállításokban és Bicep/infrastruktúránál.
14. **`max_output_tokens` minimum 16**: Az Azure OpenAI visszautasítja a 16 alatti értékeket `400 integer_below_min_value` hibával. Smoke tesztekhez használj 50-et, élesben 1000+-et. A régi `max_tokens`-nak nem volt ilyen minimuma.
15. **`tenant_id` az `AzureDeveloperCliCredential`-hez**: Ha az Azure OpenAI erőforrás más tenantban van, explicit módon meg kell adni a `tenant_id`-t — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Enélkül a hitelesítő csendben rossz tenantot használ, és `401`-et ad vissza.
16. **A kvóták máshogy jelennek meg streamelésnél**: Chat Completions esetén a 429 általában megakadályozta a stream elindulását. Responses API streaming esetén a 429 előfordulhat **stream közben** — az async iterátor kivételt dob. Mindig csomagold `try/except`-be a stream ciklust és adj vissza hibás JSON sort, hogy a frontend szépen kezelje.

17. **A streaming hibakezelés kötelező webalkalmazásoknál**: A `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` minta kritikus fontosságú. Enélkül az SSE/JSONL stream bármely szerveroldali hiba esetén csendben meghal, és a frontend lefagy.
18. **A eszközdefinícióknak lapos formátumot kell használniuk**: A Responses API a `{"type": "function", "name": ..., "parameters": ...}` formátumot várja — nem a Chat Completions beágyazott `{"type": "function", "function": {"name": ..., "parameters": ...}}` formátumot. Ez a leggyakoribb migrációs hiba funkcióhívó kódok esetén.
19. **A `pydantic_function_tool()` inkompatibilis**: Az `openai.pydantic_function_tool()` segédfüggvény még mindig a régi beágyazott formátumot generálja. Ne használd `responses.create()`-szal. Definiáld az eszköz sémáit manuálisan, vagy laposítsd az eredményt.
20. **Az eszköz eredményei a `function_call_output` típust használják, nem a `role: tool`-t**: Egy eszköz végrehajtása után csatolj `{"type": "function_call_output", "call_id": ..., "output": ...}` elemeket — nem pedig `{"role": "tool", "tool_call_id": ..., "content": ...}` formátumot. Az asszisztens eszközkéréséhez használd a `messages.extend(response.output)` metódust — ne manuálisan állítsd elő a `{"role": "assistant", "tool_calls": [...]}` szótárt.
21. **A `strict: true` használata megköveteli a `required` + `additionalProperties: false` beállítást**: Ha egy eszközön `strict: true` van beállítva, akkor minden tulajdonságnak benne kell lennie a `required` tömbben, és az `additionalProperties` értéke `false` kell legyen. Ha bármelyik hiányzik, 400-as hibát kapsz.
22. **A funkcióhívás ID-k konkrét előtagokkal rendelkeznek**: Amikor few-shot `function_call` elemeket adsz meg az `input`-ban, az `id` mezőnek `fc_` előtaggal kell kezdődnie, a `call_id` mezőnek pedig `call_` előtaggal (pl. `"id": "fc_example1", "call_id": "call_example1"`). A régi Chat Completions `call_` előtag használata az `id` mezőnél elutasításra kerül.
23. **A GitHub Models nem támogatja a Responses API-t**: Ha az alkalmazásban van GitHub Models kódszakasz (`base_url`, amely `models.github.ai` vagy `models.inference.ai.azure.com`-ra mutat), távolítsd el teljesen. Nincs migrációs út — válts Azure OpenAI-ra, OpenAI-ra vagy kompatibilis helyi végpontra.
24. **A tartalomszűrő hiba törzs szerkezete megváltozott**: A Chat Completions hibák a `error.body["innererror"]["content_filter_result"]` (egyes szám) struktúrát használták. A Responses API hibái a `error.body["content_filters"][0]["content_filter_results"]` (többes szám, tömbön belül) formátumot használják. Az `innererror` kulcs már nem létezik. Az a kód, amely közvetlenül hozzáfér az `innererror`-höz, futásidőben `KeyError`-t dob — ezt könnyű figyelmen kívül hagyni migrációkor, mert csak akkor bukkan elő, ha a tartalomszűrő valóban aktiválódik. Mindig keress rá az `innererror`-re migráció közben.
25. **A nyers HTTP hívások URL és törzs átírást igényelnek**: Azok az alkalmazások, amelyek Azure OpenAI REST-et közvetlenül hívnak (például `requests`, `httpx`, `aiohttp` segítségével) az `/openai/deployments/{name}/chat/completions?api-version=...` végpontot, váltaniuk kell az `/openai/v1/responses` végpontra. A kérés törzse `input` mezőt használ `messages` helyett, szükséges a `max_output_tokens` és `store`, és az `api-version` query paramétert el kell hagyni. A válasz törzsének szövege az `output[0].content[0].text` mezőben van — **nem** az `output_text`-ben, ami egy SDK kényelmi tulajdonság, és nincs meg a nyers REST JSON-ban.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->