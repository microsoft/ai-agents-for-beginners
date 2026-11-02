# Řešení problémů, tabulka rizik a úskalí

## Řešení problémů s chybami 400

| Chyba | Oprava |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definice nástroje používá starý vnořený formát Chat Completions | Zjednodušit z `{"type": "function", "function": {"name": ...}}` na `{"type": "function", "name": ..., "parameters": ...}` — název, popis a parametry jsou na nejvyšší úrovni |
| `unknown_parameter: input[N].tool_calls` | Výsledky nástroje v rámci více kol používají starý formát Chat Completions | Nahradit `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` položkami `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Nástroj s `strict: true` postrádá pole `required` | Při `strict: true` musí být všechny vlastnosti uvedeny v `required` a musí být nastaveno `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Nástroj s `strict: true` postrádá `additionalProperties: false` | Přidat `"additionalProperties": false` do objektu parametrů |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID funkčního volání few-shot má špatný prefix | ID funkčních volání musí začínat na `fc_` (např. `fc_example1`), nikoli na `call_` |
| `missing_required_parameter: text.format.name` | Přidat klíč `"name"` do slovníku formátu (např. `"name": "Output"`) |
| `invalid_type: text.format` | Zajistit, že `text.format` je slovník s klíči `type`, `name`, `strict`, `schema` — ne řetězec |
| `invalid input content type` | Použít obsahové typy `input_text`/`output_text` místo Chat `text` |
| `invalid input content type` (obrázek) | Obsah obrázku stále používá `"type": "image_url"` | Změnit na `"type": "input_image"` |
| `Expected object, got string` u `image_url` | `image_url` je stále vnořený objekt `{"url": "..."}` | Zjednodušit na prostý řetězec: `"image_url": "https://..."` nebo `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` pro `max_output_tokens` | Minimum na Azure OpenAI je **16**. Pro testy použijte 50+, pro produkci 1000+. |
| `429 Too Many Requests` během streamování | Omezování rychlosti. Zabalte streamování do `try/except`, vydejte chybový JSON na frontend, implementujte zpětný odstup/opakování. |
| `KeyError: 'innererror'` u chyby filtru obsahu | Struktura těla chyby filtru obsahu se změnila v Responses API | Chat Completions používal `error.body["innererror"]["content_filter_result"]`; Responses API používá `error.body["content_filters"][0]["content_filter_results"]` (v množném čísle, uvnitř pole). Přepište všechny přístupy k `innererror`. |

---

## Tabulka rizik migrace

| Symptomy | Pravděpodobná chyba | Oprava |
|---------|---------------|-----|
| Prázdný `output_text` / zkrácená odpověď | `max_output_tokens` je příliš nízké pro modely pro odvozování | Nastavit `max_output_tokens=1000` či více — výpočetní tokeny se počítají do limitu |
| `400 invalid_type: text.format` | Předán řetězec `response_format` místo slovníku `text.format` | Použít `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` na `/openai/v1/responses` | Špatné `base_url` — chybí přípona `/openai/v1/` | Zajistit `base_url=f"{endpoint}/openai/v1/"` (s koncovým lomítkem) |
| `401 Unauthorized` po přechodu na `OpenAI()` | `api_key` není nastaven nebo poskytovatel tokenu není správně předán | Pro EntraID: `api_key=token_provider` (volatelný objekt). Pro API klíč: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model vrací `deployment not found` | Parametr `model` neodpovídá názvu nasazení v Azure | Použít `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — toto je název nasazení, ne modelu |
| `json.loads(resp.output_text)` vyvolá `JSONDecodeError` | Schéma není vynuceno nebo model nepodporuje striktní JSON | Zajistit `"strict": True` ve schématu a ověřit, že model podporuje strukturovaný výstup |
| Streaming nevrací žádné události `delta` | Kontrola nesprávného typu události | Filtrovat na `event.type == "response.output_text.delta"`, ne na Chat `chat.completion.chunk` |
| `400` chyba na vstup obrázku po migraci | Typ obsahu obrázku nebyl aktualizován | Změnit `"type": "image_url"` → `"type": "input_image"` a zjednodušit `"image_url": {"url": "..."}` → `"image_url": "..."` (prostý řetězec) |
| Nástroj volá cyklicky dokola | Chybí výsledek nástroje v následném `input` | Po spuštění nástroje přidat položku `{"type": "function_call_output", "call_id": ..., "output": ...}` do `input` v další žádosti |
| Chyba `temperature` u GPT-5 nebo o-série | Explicitní hodnota `temperature` jiná než 1 | Odstranit `temperature` nebo nastavit na `1` pro GPT-5 a modely o-série (o1, o3-mini, o3, o4-mini) |
| Chyba `top_p` u o-série | `top_p` není podporováno | Odstranit `top_p` při cílení na modely o-série |
| `max_completion_tokens` není rozpoznán | Použití parametru specifického pro Azure | Nahraďte `max_completion_tokens` parametrem `max_output_tokens`. Nastavte na 4096+ pro o-sérii (počítá se do limitu výpočetních tokenů). |
| Prázdný/zkrácený výstup z o-série | `max_output_tokens` je příliš nízké | O-série používá interně výpočetní tokeny, nastavte `max_output_tokens=4096` nebo vyšší — ne 500–1000. |
| `400 integer_below_min_value` pro `max_output_tokens` | Hodnota je pod 16 | Azure OpenAI vyžaduje `max_output_tokens >= 16`. Použijte 50+ pro základní testy, 1000+ pro produkci. |
| `429 Too Many Requests` uprostřed streamu | Omezování rychlosti Azure OpenAI | Stream se přeruší bez chybové hlášky. Vždy zabalte `async for event in await coroutine:` do `try/except` a vydejte `{"error": str(e)}` na frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Nesprávný tenant nebo není přihlášeno | Explicitně předat `tenant_id=os.getenv("AZURE_TENANT_ID")`. Spustit `azd auth login --tenant <tenant-id>` lokálně. |
| `404 Not Found` při použití GitHub Models (`models.github.ai`) | GitHub Models nepodporuje Responses API | Odstranit zcela cestu kódu GitHub Models. Používejte Azure OpenAI, OpenAI, nebo kompatibilní lokální endpoint (např. Ollama s podporou Responses). |
| MAF `OpenAIChatCompletionClient` stále používá Chat Completions | Používání legacy MAF klienta v 1.0.0+ | V MAF 1.0.0+ `OpenAIChatClient` standardně používá Responses API. Nahraďte `OpenAIChatCompletionClient` za `OpenAIChatClient`. Pro verze před 1.0.0 aktualizujte na `agent-framework-openai>=1.0.0`. |
| LangChain agent vrací prázdný výstup nebo padá při voláních nástrojů | `ChatOpenAI` nepoužívá Responses API | Přidat `use_responses_api=True` do `ChatOpenAI(...)`. Také změnit `.content` → `.text` v odpovědích. |
| `KeyError: 'innererror'` v handleru chyby filtru obsahu | Struktura těla chyby se změnila v Responses API | Přepište `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Wrapper `innererror` zmizel; detaily filtru obsahu jsou nyní v pole `content_filters` s množným `content_filter_results` uvnitř každé položky. |
| Přímé HTTP volání na `/openai/deployments/.../chat/completions` vrací 404 | Starý REST endpoint Chat Completions | Přepište URL na `/openai/v1/responses`. Změňte tělo požadavku: `messages` → `input`, přidejte `max_output_tokens` + `store: false`, odstraňte query parametr `api-version`. Změna parsování odpovědi: `choices[0].message.content` → `output[0].content[0].text` (pozn.: `output_text` je SDK konvenience, není v raw JSON REST odpovědi). |

---

## Úskalí

1. Pokud jste dříve využívali Chat Completions pro stav konverzace, spravujte vlastní stav explicitně pomocí Responses.
2. Preferujte `max_output_tokens` před starým `max_tokens`.
3. Při migraci na `gpt-5` zajistěte, aby `temperature` nebyla specifikována nebo byla nastavena na `1`.
4. Nahraďte Chat `content[].type: "text"` typem Responses `content[].type: "input_text"` pro vstupy uživatele/systému.
5. Pro `text.format` dodávejte správný slovník (např. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ne prostý řetězec.
6. Parametr `seed` není v Responses podporován; odstraňte jej z požadavků.
7. **Odvozování:** `reasoning` zahrňte pouze pokud jej původní kód již používal. Nepřidávejte `reasoning` do API volání, která jej neměla — mnoho nerazumějících modelů tento parametr nepodporuje.
8. **Velikost `max_output_tokens`:** U modelů pro odvozování (GPT-5-mini, GPT-5, o-série) použijte `max_output_tokens=4096` nebo více — ne 50–1000. Model používá interní výpočetní tokeny před generováním viditelného výstupu; příliš nízký limit způsobuje zkrácené nebo prázdné odpovědi.
9. **O-série `max_completion_tokens`:** Pokud původní kód používal `max_completion_tokens` (parametr specifický pro Azure u o-série), nahraďte jej `max_output_tokens`. Responses API nepřijímá `max_completion_tokens`.
10. **O-série `reasoning_effort`:** Pokud původní kód používá `reasoning_effort` (low/medium/high), přesuňte jej do `reasoning={"effort": "<hodnota>"}` v API volání Responses.
11. **Zpoždění streamování u o-série:** Modely o-série provádějí interní odvozování před generováním výstupu. Při streamování očekávejte delší prodlevu před první událostí `response.output_text.delta`. Je to normální — model odvozuje, není zaseknutý.
9. **`_azure_ad_token_provider` zmizel:** `AsyncOpenAI` / `OpenAI` nemají atribut `_azure_ad_token_provider`. Testy nebo kód, které k tomuto atributu přistupují, skončí `AttributeError`. Poskytovatel tokenů je předáván jako `api_key` a není na klientovi dostupný.
10. **Snapshot / golden soubory:** Pokud testovací sada používá snapshot testování, **všechny** snapshot soubory obsahující tvary streamování Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, atd.) musí být aktualizovány na nový tvar Responses. To se snadno přehlédne a způsobuje selhání testů při porovnání snapshotů.
11. **Cesta pro mock monkeypatch:** Cílová cesta pro monkeypatch se mění z `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (nebo `Responses.create` pro synchronní). Použití staré cesty nic neudělá — mock nebude zachycen a testy volají skutečné API nebo selžou.
12. **`input` místo `messages`:** Mock funkce musí číst `kwargs.get("input")`, ne `kwargs.get("messages")`. Responses API používá `input` pro historii konverzace.
13. **Pojmenování environmentálních proměnných:** Azure Identity SDK používá `AZURE_CLIENT_ID` (ne `AZURE_OPENAI_CLIENT_ID`) pro `ManagedIdentityCredential(client_id=...)`. Přejmenujte ve testech, `.env` souborech, nastaveních aplikace a Bicep/infrastruktuře.
14. **Minimální hodnota `max_output_tokens` je 16:** Azure OpenAI odmítá hodnoty pod 16 s chybou `400 integer_below_min_value`. Použijte `50` pro rychlé testy, `1000`+ pro produkci. Staré `max_tokens` nemělo takové minimum.
15. **`tenant_id` pro `AzureDeveloperCliCredential`:** Když je Azure OpenAI zdroj v jiném tenantu, **musíte** explicitně předat `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Bez toho použití nesprávného tenantu proběhne potichu a vrátí `401`.
16. **Limity rychlosti se u streamování projevují jinak:** S Chat Completions 429 obvykle zabránila spuštění streamu. S Responses API streamováním může 429 nastat **během streamu** — asynchronní iterátor vyvolá výjimku. Vždy zabalujte smyčku streamování do `try/except` a vydejte chybový JSON řádek, aby frontend s chybou správně naložil.

17. **Zpracování chyb ve streamování je pro webové aplikace povinné**: Vzorec `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` je kritický. Bez něj SSE/JSONL stream tichounce umírá při jakékoli chybě na straně serveru a frontend zamrzá.
18. **Definice nástrojů musí používat plochý formát**: Responses API očekává `{"type": "function", "name": ..., "parameters": ...}` — nikoli vnořený formát Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Toto je nejčastější chyba při migraci u kódu volajícího funkce.
19. **`pydantic_function_tool()` není kompatibilní**: Pomocník `openai.pydantic_function_tool()` stále generuje starý vnořený formát. Nepoužívejte jej s `responses.create()`. Definujte schémata nástrojů ručně nebo výstup zploštěte.
20. **Výsledky nástrojů používají `function_call_output`, ne `role: tool`**: Po vykonání nástroje přidejte `{"type": "function_call_output", "call_id": ..., "output": ...}` — nikoli `{"role": "tool", "tool_call_id": ..., "content": ...}`. Pro požadavek asistenta na nástroj použijte `messages.extend(response.output)` — ne manuální slovník `{"role": "assistant", "tool_calls": [...]}`.
21. **Pro `strict: true` je potřeba `required` + `additionalProperties: false`**: Při použití `strict: true` u nástroje musí být každá vlastnost uvedena v poli `required` a `additionalProperties` musí být `false`. Chybějící některé z nich způsobí chybu 400.
22. **ID volání funkcí mají specifické prefixy**: Při poskytování položek `function_call` ve stylu few-shot v `input` musí pole `id` začínat na `fc_` a pole `call_id` musí začínat na `call_` (např. `"id": "fc_example1", "call_id": "call_example1"`). Použití starého prefixu Chat Completions `call_` pro `id` je odmítnuto.
23. **GitHub Models nepodporují Responses API**: Pokud aplikace má cestu GitHub Models (`base_url` ukazující na `models.github.ai` nebo `models.inference.ai.azure.com`), odstraňte ji úplně. Neexistuje migrační cesta — přejděte na Azure OpenAI, OpenAI nebo kompatibilní lokální endpoint.
24. **Struktura těla chyby filtrování obsahu se změnila**: Chyby v Chat Completions používaly `error.body["innererror"]["content_filter_result"]` (jednotné číslo). Chyby v Responses API používají `error.body["content_filters"][0]["content_filter_results"]` (množné číslo, uvnitř pole). Klíč `innererror` již neexistuje. Kód, který přímo přistupuje k `innererror`, během běhu vyhodí `KeyError` — toto je snadné při migraci přehlédnout, protože se projeví jen když filtr obsahu skutečně zasáhne. Při migraci vždy projděte kód pro `innererror`.
25. **Surové HTTP volání vyžaduje přepis URL a těla požadavku**: Aplikace volající Azure OpenAI REST přímo (přes `requests`, `httpx`, `aiohttp`) s cestou `/openai/deployments/{name}/chat/completions?api-version=...` musí přejít na `/openai/v1/responses`. Tělo požadavku používá `input` místo `messages`, vyžaduje `max_output_tokens` a `store` a parametr dotazu `api-version` se odstraňuje. Text odpovědi je v `output[0].content[0].text` — **nikoli** `output_text`, což je pohodlná vlastnost SDK, která v surovém REST JSON není.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->