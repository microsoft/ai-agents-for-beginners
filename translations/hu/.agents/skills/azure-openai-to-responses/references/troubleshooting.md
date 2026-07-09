# Hibaelhárítás, Kockázati Táblázat & Csapdák

## 400-as hibák hibaelhárítása

| Hiba | Javítás |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Az eszköz definíciója régi Chat Completions beágyazott formátumot használ | Laposítsd ki a `{"type": "function", "function": {"name": ...}}` -ről `{"type": "function", "name": ..., "parameters": ...}` formátumra — a név, leírás, paraméterek a felső szinten legyenek |
| `unknown_parameter: input[N].tool_calls` | Több fordulós eszköz eredmények régi Chat Completions formátumot használnak | Cseréld a `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` elemeket `response.output` elemekre + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` eszköz hiányzó `required` tömb | Ha `strict: true`, minden tulajdonságot fel kell sorolni a `required` mezőben és az `additionalProperties: false` kell legyen beállítva |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` eszköz hiányzó `additionalProperties: false` | Add hozzá az `"additionalProperties": false` mezőt a paraméter objektumhoz |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call azonosító rossz előtaggal | A hívásazonosítóknak `fc_`-vel kell kezdődniük (pl. `fc_example1`), nem `call_` -lal |
| `missing_required_parameter: text.format.name` | Add hozzá a `"name"` kulcsot a formátum szótárhoz (pl. `"name": "Output"`) |
| `invalid_type: text.format` | Győződj meg róla, hogy a `text.format` egy szótár `type`, `name`, `strict`, `schema` kulcsokkal — ne pedig egy string |
| `invalid input content type` | Használj `input_text`/`output_text` tartalomtípusokat a Chat `text` helyett |
| `invalid input content type` (kép) | A képtartalom még mindig a `"type": "image_url"` típust használja | Válts `"type": "input_image"` típusra |
| `Expected object, got string` az `image_url`-nél | Az `image_url` még mindig beágyazott objektum `{"url": "..."}` | Egyszerű stringgé laposítsd `"image_url": "https://..."` vagy `"image_url": "data:image/...;base64,..."` formátumban |
| `integer below minimum value` a `max_output_tokens` esetén | Minimum érték Azure OpenAI-nál **16**. Tesztekhez használj 50+-ot, éleshez 1000+-ot. |
| `429 Too Many Requests` folyamatos adatfolyam során | Korlátozás lépett életbe. Csomagold a stream feldolgozást `try/except` blokkba, küldj hibajelzést JSON formátumban a frontendnek, implementálj visszakapcsolást / újrapróbálkozást. |
| `KeyError: 'innererror'` tartalomszűrő hiba esetén | A tartalomszűrő hibák válaszstruktúrája változott a Responses API-ban | A Chat Completions `error.body["innererror"]["content_filter_result"]` használ, a Responses API viszont `error.body["content_filters"][0]["content_filter_results"]` (többes szám, tömbben). Írd át az összes `innererror` hivatkozást. |

---

## Migrációs Kockázati Táblázat

| Tünet | Valószínű Hiba | Javítás |
|---------|---------------|-----|
| Üres `output_text` / levágott válasz | `max_output_tokens` túl alacsony az érvelő modelleknél | Állítsd `max_output_tokens=1000` vagy magasabb értékre — az érvelő tokenek beleszámítanak a limitbe |
| `400 invalid_type: text.format` | `response_format` stringet adtak meg `text.format` szótár helyett | Használd a `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` formátumot |
| `404 Not Found` a `/openai/v1/responses` végponton | Hibás `base_url` — hiányzik az `/openai/v1/` utótag | Győződj meg róla, hogy `base_url=f"{endpoint}/openai/v1/"` (vesszővel lezárt) |
| `401 Unauthorized` `OpenAI()`-ra váltás után | Nem állították be az `api_key`-et vagy nem adták át helyesen a token szolgáltatót | EntraID-hez: `api_key=token_provider` (hívható). API kulcshoz: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| A modell `deployment not found` visszaadása | A `model` paraméter nem egyezik az Azure telepítés nevével | Használd `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — ez a telepítés neve, nem a modellé |
| `json.loads(resp.output_text)` `JSONDecodeError`-t dob | Nem kényszerítették a séma használatát vagy a modell nem támogatja a szigorú JSON-t | Biztosítsd, hogy a séma tartalmazza a `"strict": True` értéket, és ellenőrizd, hogy a modell támogatja a strukturált kimenetet |
| A streaming nem ad ki `delta` eseményeket | Rossz eseménytípust vizsgálnak | Szűrj `event.type == "response.output_text.delta"` eseményre, ne a Chat `chat.completion.chunk`-jára |
| `400` hiba képbemenet esetén migráció után | A képtartalom típusa nem frissült | Válts `"type": "image_url"` → `"type": "input_image"` és laposítsd a `"image_url": {"url": "..."}` → `"image_url": "..."` (egyszerű string) formára |
| Az eszközhívások végtelen ciklusba kerülnek | Az eszköz eredménye hiányzik a következő `input`-ból | Egy eszköz végrehajtása után adj hozzá a következő kérés `input` mezőjéhez egy `{"type": "function_call_output", "call_id": ..., "output": ...}` elemet |
| `temperature` hiba GPT-5 vagy o-sorozat esetén | Explicit `temperature` érték más mint 1 | Távolítsd el a `temperature` paramétert vagy állítsd `1`-re GPT-5 és o-sorozat modellek (o1, o3-mini, o3, o4-mini) esetén |
| `top_p` hiba o-sorozattal | `top_p` nem támogatott | Távolítsd el a `top_p` paramétert célzottan o-sorozat modelleknél |
| `max_completion_tokens` nem ismert | Azure-specifikus paraméter használata | Cseréld le `max_completion_tokens`-t `max_output_tokens`-re. Állítsd 4096+-ra o-sorozat modelleknél (az érvelő tokenek beleszámítanak a limitbe). |
| Üres vagy levágott kimenet o-sorozattól | `max_output_tokens` túl alacsony | Az o-sorozat modellek belsőleg érvelő tokeneket használnak. Állítsd `max_output_tokens=4096` vagy magasabbra — nem 500–1000-ra. |
| `400 integer_below_min_value` a `max_output_tokens`-nál | Érték 16 alatt | Az Azure OpenAI érvényesíti a `max_output_tokens >= 16` feltételt. Használj 50+ értéket tesztekhez, 1000+ értéket éles környezethez. |
| `429 Too Many Requests` adatfolyam közben | Azure OpenAI korlátozás | A stream hiba nélkül megszakad hiba kezelés nélkül. Mindig csomagold be az `async for event in await coroutine:` ciklust `try/except` blokkba, és adj vissza `{"error": str(e)}` JSON-t a frontendnek. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Hibás bérlő vagy nincs bejelentkezve | Add meg explicit módon `tenant_id=os.getenv("AZURE_TENANT_ID")`. Futtasd helyileg az `azd auth login --tenant <tenant-id>` parancsot. |
| `404 Not Found` GitHub Modellek (`models.github.ai`) használatakor | A GitHub Modellek nem támogatják a Responses API-t | Távolítsd el teljesen a GitHub Modellek kódfoltot. Használj Azure OpenAI-t, OpenAI-t, vagy kompatibilis helyi végpontot (pl. Ollama Responses támogatással). |
| A MAF `OpenAIChatCompletionClient` még mindig Chat Completions-t használ | Régi MAF kliens használata 1.0.0+ verzióban | A MAF 1.0.0+ verzióban az `OpenAIChatClient` alapból a Responses API-t használja. Cseréld az `OpenAIChatCompletionClient`-et `OpenAIChatClient`-re. Pre-1.0.0 változat esetén frissíts `agent-framework-openai>=1.0.0`-ra. |
| LangChain ügynök üres választ vagy hibát ad eszközhívásoknál | A `ChatOpenAI` nem használja a Responses API-t | Add hozzá a `use_responses_api=True` paramétert a `ChatOpenAI(...)`-hoz. Változtasd `.content` → `.text` a válasz üzeneteknél. |
| `KeyError: 'innererror'` tartalomszűrő hiba kezeléskor | A válasz test szerkezete megváltozott a Responses API-ban | Írd át az `error.body["innererror"]["content_filter_result"]["jailbreak"]` hivatkozást `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` formára. Az `innererror` burkoló megszűnt; a tartalomszűrő részletek egy felső szintű `content_filters` tömbben vannak, amelyben minden elem belsejében többes számú `content_filter_results` található. |
| Nyers HTTP hívás a `/openai/deployments/.../chat/completions` végpontra 404-et ad | Régi Chat Completions REST végpont | Írd át az URL-t `/openai/v1/responses`-re. A kérés törzsét módosítsd: `messages` → `input`, add hozzá a `max_output_tokens` + `store: false`, távolítsd el az `api-version` lekérdezési paramétert. A válasz feldolgozása változzon: `choices[0].message.content` → `output[0].content[0].text` (megjegyzés: `output_text` csak SDK kényelmi property, nem szerepel nyers REST JSON-ban). |

---

## Csapdák

1. Ha korábban Chat Completions-t használtál a beszélgetési állapot kezelésére, akkor a Responses használatával kezeld saját állapotodat explicit módon.
2. Részesítsd előnyben a `max_output_tokens`-t a régi `max_tokens` paraméter helyett.
3. Amikor átállsz `gpt-5`-re, győződj meg arról, hogy a `temperature` nincs megadva, vagy `1`-re van állítva.
4. Cseréld ki a Chat `content[].type: "text"` típust a Responses `content[].type: "input_text"` típusra felhasználói/rendszer bemeneteknél.
5. A `text.format` esetén adj meg megfelelő szótárat (pl. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ne sima sztringet.
6. A `seed` paraméter nem támogatott a Responses-ben; távolítsd el a kérésekből.
7. **Érvelés (Reasoning)**: Csak akkor add hozzá a `reasoning` mezőt, ha az eredeti kód már használta. Ne adj hozzá `reasoning`-et olyan API hívásokhoz, amelyeknél nem volt — sok modell (pl. gpt-4o-mini) nem támogatja ezt a paramétert.
8. **`max_output_tokens` méretezése**: Érvelő modelleknél (GPT-5-mini, GPT-5, o-sorozat) használd a `max_output_tokens=4096` vagy magasabb értéket — nem 50–1000-et. A modell belsőleg érvelő tokeneket használ a látható kimenet generálása előtt; a túl alacsony limitek levágott vagy üres válaszokat okoznak.
9. **O-sorozat `max_completion_tokens`**: Ha az eredeti kód használta a `max_completion_tokens` (Azure-specifikus o-sorozat paraméter), cseréld le `max_output_tokens`-re. A Responses API nem fogadja el a `max_completion_tokens`-t.
10. **O-sorozat `reasoning_effort`**: Ha az eredeti kód használja a `reasoning_effort` (low/medium/high), migráld át `reasoning={"effort": "<érték>"}` formába a Responses API hívásoknál.
11. **O-sorozat streaming késleltetés**: Az o-sorozat modellek belső érvelést végeznek mielőtt kimenetet generálnának. Streaming esetén számíts hosszabb késleltetésre az első `response.output_text.delta` esemény előtt. Ez normális — a modell érvel, nem akadt el.
9. **`_azure_ad_token_provider` eltűnt**: Az `AsyncOpenAI` / `OpenAI` objektumoknak nincs `_azure_ad_token_provider` attribútuma. A tesztek vagy kód, ami ezt az attribútumot eléri, `AttributeError`-t kap. A token szolgáltató az `api_key` paraméterként kerül átadásra, és nem elérhető a kliens objektumon.
10. **Snapshot / arany fájlok**: Ha a tesztcsomag snapshot tesztelést használ, akkor **minden** snapshot fájlt, ami Chat Completions streaming alakokat tartalmaz (`choices[0]`, `content_filter_results`, `function_call`, stb.) frissíteni kell az új Responses formára. Ezt könnyű elfelejteni, és snapshot állítási hibákhoz vezet.
11. **Mock monkeypatch útvonal**: A monkeypatch célpont változik az `openai.resources.chat.AsyncCompletions.create` -ről az `openai.resources.responses.AsyncResponses.create` (vagy `Responses.create` szinkron esetén) végpontra. A régi útvonal használata néma hatást eredményez — a mock nem fog interceptálni, és a tesztek a valódi API-hoz mennek vagy hibáznak.
12. **`input` nem `messages`**: A mock függvényeknek a `kwargs.get("input")`-et kell olvasniuk, nem a `kwargs.get("messages")`-t. A Responses API az `input` mezőt használja a beszélgetési előzményekhez.
13. **Környezeti változó név**: Az Azure Identity SDK a `AZURE_CLIENT_ID` (nem `AZURE_OPENAI_CLIENT_ID`) nevet használja a `ManagedIdentityCredential(client_id=...)` esetén. Nevezd át ezt a tesztekben, `.env` fájlokban, alkalmazás beállításoknál és Bicep/infrastruktúra szkriptekben.
14. **`max_output_tokens` minimum 16**: Az Azure OpenAI elutasítja a 16 alatti értékeket `400 integer_below_min_value` hibával. Használj 50-et a gyors tesztekhez, 1000+ értéket éles környezetben. A régi `max_tokens`-nak nem volt ilyen minimuma.
15. **`tenant_id` az `AzureDeveloperCliCredential`-hez**: Amikor az Azure OpenAI erőforrás másik bérlőben van, kötelező explicit módon átadni a `tenant_id` paramétert — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Enélkül a hitelesítő rossz bérlőt használ néma hibával és visszaad `401`-et.
16. **Korlátozások megjelenése streamingben**: Chat Completions esetén a 429-es hiba általában megakadályozta a stream elindulását. Responses API streamingben a 429 előfordulhat **stream közben** — az aszinkron iterátor kivételt dob. Mindig csomagold be a streaming ciklust `try/except` blokkba, és adj vissza JSON hibasort, hogy a frontend megfelelően kezelhesse.

17. **A streaming hibakezelés kötelező webalkalmazásoknál**: A `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` mintázat kritikus. Enélkül az SSE/JSONL stream bármilyen szerveroldali hiba esetén csendben megszakad, és a frontend lefagy.
18. **Az eszközdefinícióknak lapos formátumot kell használniuk**: A Responses API elvárja a `{"type": "function", "name": ..., "parameters": ...}` formátumot — nem a Chat Completions beágyazott `{"type": "function", "function": {"name": ..., "parameters": ...}}` formátumot. Ez a leggyakoribb migrációs hiba a függvényhívó kódban.
19. **A `pydantic_function_tool()` inkompatibilis**: Az `openai.pydantic_function_tool()` segédfüggvény még mindig a régi beágyazott formátumot generálja. Ne használd a `responses.create()`-el együtt. Az eszköz sémákat definiáld kézzel, vagy lapítsd le a kimenetet.
20. **Az eszköz eredmények `function_call_output` típusúak, nem `role: tool`**: Az eszköz végrehajtása után add hozzá a `{"type": "function_call_output", "call_id": ..., "output": ...}` objektumot — ne a `{"role": "tool", "tool_call_id": ..., "content": ...}`-et. Az asszisztens eszközhívásához használd a `messages.extend(response.output)`-t — ne egy kézi `{"role": "assistant", "tool_calls": [...]}` szótárat.
21. **A `strict: true` használata megköveteli a `required` + `additionalProperties: false` beállításokat**: Ha egy eszközön `strict: true` van, minden tulajdonságnak szerepelnie kell a `required` tömbben, és az `additionalProperties` értéke `false` kell legyen. Ezek hiánya 400-as hibát okoz.
22. **A függvényhívás azonosítóknak speciális előtagjaik vannak**: Amikor few-shot `function_call` elemeket adsz meg az `input`-ban, az `id` mezőnek `fc_` előtaggal kell kezdődnie, és a `call_id` mezőnek `call_` előtaggal (pl. `"id": "fc_pelda1", "call_id": "call_pelda1"`). A régi Chat Completions `call_` előtag az `id` mezőnél elutasításra kerül.
23. **A GitHub Models nem támogatja a Responses API-t**: Ha az alkalmazásban van GitHub Models kódszakasz (`base_url`, ami `models.github.ai` vagy `models.inference.ai.azure.com`-ra mutat), távolítsd el teljesen. Nincs migrációs útvonal — válts Azure OpenAI-ra, OpenAI-ra vagy kompatibilis helyi végpontra.
24. **A tartalomszűrő hiba törzs szerkezete megváltozott**: A Chat Completions hibák az `error.body["innererror"]["content_filter_result"]` (egyesszám) mezőt használták. A Responses API hibái az `error.body["content_filters"][0]["content_filter_results"]` (többesszám, tömbön belül) szerkezetet használják. Az `innererror` kulcs már nem létezik. Az olyan kód, ami közvetlenül hozzáfér az `innererror`-hez, futási időben `KeyError`-t dob — ezt migráció során könnyű észrevenni, mert csak akkor történik, ha a tartalomszűrő ténylegesen aktiválódik. Mindig keress rá az `innererror`-re migrációkor.
25. **A nyers HTTP hívásokat URL + törzs újraírása szükséges**: Azok az alkalmazások, amelyek az Azure OpenAI REST-et közvetlenül hívják (`requests`, `httpx`, `aiohttp` használatával) a `/openai/deployments/{name}/chat/completions?api-version=...` végponton, át kell hogy térjenek a `/openai/v1/responses`-re. A kérés törzse az `input` mezőt használja `messages` helyett, szükséges a `max_output_tokens` és a `store`, és az `api-version` lekérdezési paraméter elhagyandó. A válasz törzs szövege az `output[0].content[0].text` mezőben van — **nem** az `output_text`-ben, ami egy SDK kényelmi tulajdonság, és nincs jelen a nyers REST JSON-ban.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->