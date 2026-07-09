# Řešení problémů, tabulka rizik a úskalí

## Řešení problémů s chybami 400

| Chyba | Oprava |
|-------|---------|
| `missing_required_parameter: tools[0].name` | Definice nástroje používá starý formát Chat Completions ve vnoření | Zploštit z `{"type": "function", "function": {"name": ...}}` na `{"type": "function", "name": ..., "parameters": ...}` — jméno, popis, parametry jdou na horní úroveň |
| `unknown_parameter: input[N].tool_calls` | Výsledky nástrojů v multi-turn používají starý formát Chat Completions | Nahradit `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` položkami `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` nástroj postrádá pole `required` | Pokud je `strict: true`, všechny vlastnosti musí být uvedeny v `required` a musí být nastaveno `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` nástroj postrádá `additionalProperties: false` | Přidat `"additionalProperties": false` do objektu parametrů |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Funkce s few-shot ID volání má špatný prefix | ID volání funkce musí začínat `fc_` (např. `fc_example1`), ne `call_` |
| `missing_required_parameter: text.format.name` | Přidat klíč `"name"` do formátu (například `"name": "Output"`) |
| `invalid_type: text.format` | Ujistit se, že `text.format` je slovník s klíči `type`, `name`, `strict`, `schema` — ne řetězec |
| `invalid input content type` | Použít typy obsahu `input_text`/`output_text` místo Chat `text` |
| `invalid input content type` (obrázek) | Typ obsahu obrázku stále používá `"type": "image_url"` | Změnit na `"type": "input_image"` |
| `Expected object, got string` u `image_url` | `image_url` je stále vnořený objekt `{"url": "..."}` | Zploštit na prostý řetězec: `"image_url": "https://..."` nebo `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` u `max_output_tokens` | Minimum je **16** na Azure OpenAI. Pro testy používejte 50+, pro produkci 1000+. |
| `429 Too Many Requests` během streamování | Omezena rychlost. Zabalte streamování do `try/except`, vydejte chybové JSON na frontend, implementujte zpětný off/retry. |
| `KeyError: 'innererror'` při chybě filtru obsahu | Struktura těla chyby filtru obsahu se změnila v Responses API | Chat Completions používal `error.body["innererror"]["content_filter_result"]`; Responses API používá `error.body["content_filters"][0]["content_filter_results"]` (v množném čísle, uvnitř pole). Přepište všechny přístupy k `innererror`. |

---

## Tabulka rizik migrace

| Příznak | Pravděpodobná chyba | Oprava |
|---------|---------------|---------|
| Prázdný `output_text` / zkrácená odpověď | `max_output_tokens` příliš nízké pro modely s uvažováním | Nastavit `max_output_tokens=1000` nebo vyšší — tokeny uvažování se počítají do limitu |
| `400 invalid_type: text.format` | Předán `response_format` jako řetězec místo slovníku `text.format` | Použít `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` na `/openai/v1/responses` | Špatná hodnota `base_url` — chybí přípona `/openai/v1/` | Zajistit `base_url=f"{endpoint}/openai/v1/"` (s koncovým lomítkem) |
| `401 Unauthorized` po přepnutí na `OpenAI()` | `api_key` není nastaven nebo token provider nebyl správně předán | Pro EntraID: `api_key=token_provider` (volatelná funkce). Pro API klíč: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model vrací `deployment not found` | Parametr `model` neodpovídá názvu nasazení v Azure | Použít `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — to je název nasazení, ne jméno modelu |
| `json.loads(resp.output_text)` vyvolá `JSONDecodeError` | Schéma není vynucené nebo model nepodporuje přísné JSON | Zajistit `"strict": True` ve schématu, a ověřit, že model podporuje strukturovaný výstup |
| Streaming nevrací žádné události `delta` | Kontrola nesprávného typu události | Filtrovat na `event.type == "response.output_text.delta"`, ne na Chat `chat.completion.chunk` |
| `400` chyba na vstupu obrázku po migraci | Typ obsahu obrázku nebyl aktualizován | Změnit `"type": "image_url"` → `"type": "input_image"` a zploštit `"image_url": {"url": "..."}` → `"image_url": "..."` (prostý řetězec) |
| Volání nástroje smyčkuje nekonečně | Chybějící výsledek nástroje ve vstupu dalšího požadavku | Po provedení nástroje přidat položku `{"type": "function_call_output", "call_id": ..., "output": ...}` do `input` v dalším požadavku |
| Chyba s `temperature` u GPT-5 nebo o-series | Explicitní hodnota `temperature` jiná než 1 | Odstranit `temperature` nebo nastavit na `1` pro GPT-5 a modely o-series (o1, o3-mini, o3, o4-mini) |
| Chyba s `top_p` u o-series | `top_p` není podporováno | Odebrat `top_p` při cílení na modely o-series |
| `max_completion_tokens` není rozpoznáno | Použití parametru specifického pro Azure | Nahradit `max_completion_tokens` za `max_output_tokens`. Nastavit na 4096+ pro o-series (tokeny uvažování se počítají do limitu). |
| Prázdný nebo zkrácený výstup u o-series | `max_output_tokens` je příliš nízké | O-series používá interně tokeny pro uvažování. Nastavit `max_output_tokens=4096` nebo vyšší — ne 500–1000. |
| `400 integer_below_min_value` u `max_output_tokens` | Hodnota pod 16 | Azure OpenAI vyžaduje `max_output_tokens >= 16`. Použít 50+ pro testy, 1000+ pro produkci. |
| `429 Too Many Requests` během streamu | Rychlost omezena Azure OpenAI | Stream se tichounce přeruší bez chybové hlášky. Vždy obalovat `async for event in await coroutine:` do `try/except` a poskytovat `{"error": str(e)}` frontendu. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Špatný tenant nebo není přihlášeno | Explicitně předat `tenant_id=os.getenv("AZURE_TENANT_ID")`. Lokálně spustit `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` při použití GitHub Models (`models.github.ai`) | GitHub Models nepodporují Responses API | Odstranit zcela cestu kódu s GitHub Models. Používat Azure OpenAI, OpenAI nebo kompatibilní lokální endpoint (např. Ollama s podporou Responses). |
| MAF `OpenAIChatCompletionClient` stále používá Chat Completions | Používání starého MAF klienta ve verzi 1.0.0+ | V MAF 1.0.0+ používá `OpenAIChatClient` ve výchozím nastavení Responses API. Nahradit `OpenAIChatCompletionClient` za `OpenAIChatClient`. Pro verze pod 1.0.0 upgradovat na `agent-framework-openai>=1.0.0`. |
| LangChain agent vrací prázdné nebo selhává u volání nástrojů | `ChatOpenAI` nepoužívá Responses API | Přidat `use_responses_api=True` do `ChatOpenAI(...)`. Také změnit `.content` na `.text` u odpovědí zpráv. |
| `KeyError: 'innererror'` v handleru chyby filtru obsahu | Struktura těla chyby se změnila v Responses API | Přepsat `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Wrapper `innererror` zmizel; podrobnosti filtru obsahu jsou nyní v top-level poli `content_filters` s `content_filter_results` (množné číslo) uvnitř každé položky. |
| Při HTTP volání na `/openai/deployments/.../chat/completions` je vráceno 404 | Starý REST endpoint Chat Completions | Přepsat URL na `/openai/v1/responses`. Změnit tělo požadavku: `messages` → `input`, přidat `max_output_tokens` + `store: false`, odstranit parametr `api-version` z query. Změnit parsování odpovědi: `choices[0].message.content` → `output[0].content[0].text` (pozn.: `output_text` je SDK convenience property, není v raw REST JSON). |

---

## Úskalí

1. Pokud jste dříve používali Chat Completions pro stav konverzace, spravujte stav explicitně se Responses.
2. Preferujte `max_output_tokens` před starým `max_tokens`.
3. Při migraci na `gpt-5` zajistěte, aby `temperature` nebyla uvedena nebo byla nastavena na `1`.
4. Nahraďte Chat `content[].type: "text"` za Responses `content[].type: "input_text"` u vstupů uživatele/systému.
5. U `text.format` použijte správný slovník (např. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), ne obyčejný řetězec.
6. Parametr `seed` není v Responses podporován; odstraňte ho z požadavků.
7. **Uvažování**: Přidávejte `reasoning` jen pokud ho originální kód již používal. Nepřidávejte `reasoning` do API volání, která ho neměla — mnoho modelů (např. gpt-4o-mini) tento parametr nepodporuje.
8. **Velikost `max_output_tokens`**: Pro modely s uvažováním (GPT-5-mini, GPT-5, o-series) použijte `max_output_tokens=4096` nebo vyšší — ne 50–1000. Model interně používá tokeny uvažování před generováním viditelného výstupu; nízké limity způsobují zkrácené nebo prázdné odpovědi.
9. **O-series `max_completion_tokens`**: Pokud originální kód používal `max_completion_tokens` (Azure-specifické pro o-series), nahraďte jej `max_output_tokens`. Responses API nepřijímá `max_completion_tokens`.
10. **O-series `reasoning_effort`**: Pokud originální kód používá `reasoning_effort` (low/medium/high), přemigrujte to na `reasoning={"effort": "<hodnota>"}` v API volání Responses.
11. **Zpoždění streamování u o-series**: Modely o-series provádějí interní uvažování před generováním výstupu. Při streamování očekávejte delší zpoždění před první událostí `response.output_text.delta`. Je to normální — model uvažuje, není zaseknutý.
9. **`_azure_ad_token_provider` zmizel**: `AsyncOpenAI` / `OpenAI` nemají atribut `_azure_ad_token_provider`. Testy či kód, které tento atribut používají, skončí chybou `AttributeError`. Token provider se předává jako `api_key` a není viditelný na klientovi.
10. **Snapshot / golden files**: Pokud testovací sada používá snapshot testování, **všechny** snapshot soubory obsahující tvary streamování Chat Completions (`choices[0]`, `content_filter_results`, `function_call` atd.) musí být aktualizovány na novou strukturu Responses. To se snadno přehlédne a způsobuje chyby assertion ve snapshotech.
11. **Path pro mock monkeypatch**: Cílová cesta monkeypatch se změnila z `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (nebo `Responses.create` pro synchronní volání). Použití staré cesty nijak neblokuje — mock se neprovede a testy volají reálné API nebo končí chybou.
12. **`input` místo `messages`**: Mockovací funkce musí číst `kwargs.get("input")`, ne `kwargs.get("messages")`. Responses API používá `input` pro historii konverzace.
13. **Pojmenování proměnných prostředí**: Azure Identity SDK používá `AZURE_CLIENT_ID` (nikoli `AZURE_OPENAI_CLIENT_ID`) pro `ManagedIdentityCredential(client_id=...)`. Přejmenujte v testech, `.env` souborech, nastavení aplikace a Bicep/infrastruktuře.
14. **Minimum `max_output_tokens` je 16**: Azure OpenAI odmítá hodnoty pod 16 s chybou `400 integer_below_min_value`. Použijte 50 pro smoke testy, 1000+ pro produkci. Starý `max_tokens` takové minimum neměl.
15. **`tenant_id` pro `AzureDeveloperCliCredential`**: Když je Azure OpenAI zdroj v jiném tenantovi, musíte explicitně předat `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Bez toho credential používá špatný tenant a vrací `401`.
16. **Limity rychlosti se u streamování projevují jinak**: U Chat Completions 429 většinou zabránila spuštění streamu. U Responses API streamování může 429 nastat **během streamu** — asynchronní iterátor vyhodí výjimku. Vždy obalte smyčku streamování do `try/except` a vraťte chybovou JSON zprávu, aby ji frontend mohl dobře zpracovat.

17. **Zpracování chyb při streamování je povinné pro webové aplikace**: Vzor `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` je kritický. Bez něj stream SSE/JSONL tiše přestane fungovat při jakékoliv chybě na straně serveru a frontend zamrzne.
18. **Definice nástrojů musí používat plochý formát**: API Responses očekává `{"type": "function", "name": ..., "parameters": ...}` — nikoli zanořený formát Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Toto je nejčastější chyba při migraci kódu volajícího funkce.
19. **`pydantic_function_tool()` není kompatibilní**: Pomocná funkce `openai.pydantic_function_tool()` stále generuje starý zanořený formát. Nepoužívejte ji spolu s `responses.create()`. Schémata nástrojů definujte ručně nebo výstup spláchněte do plochého formátu.
20. **Výsledky nástrojů používají `function_call_output`, ne `role: tool`**: Po spuštění nástroje přidejte `{"type": "function_call_output", "call_id": ..., "output": ...}` — nikoli `{"role": "tool", "tool_call_id": ..., "content": ...}`. Pro požadavek asistenta na nástroj použijte `messages.extend(response.output)` — ne manuální slovník `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` vyžaduje `required` + `additionalProperties: false`**: Při použití `strict: true` u nástroje musí být každá vlastnost uvedena v poli `required` a `additionalProperties` musí být `false`. Chybějící kterákoliv z těchto podmínek způsobí chybu 400.
22. **ID volání funkcí mají specifické předpony**: Při předávání několika `function_call` položek ve `input` musí pole `id` začínat na `fc_` a pole `call_id` na `call_` (např. `"id": "fc_example1", "call_id": "call_example1"`). Použití staré předpony `call_` z Chat Completions v poli `id` je odmítnuto.
23. **GitHub Models nepodporuje Responses API**: Pokud aplikace obsahuje kódovou cestu GitHub Models (`base_url` směřuje na `models.github.ai` nebo `models.inference.ai.azure.com`), odstraňte ji úplně. Neexistuje migrační cesta — přepněte na Azure OpenAI, OpenAI nebo kompatibilní lokální endpoint.
24. **Struktura chybového těla filtrů obsahu se změnila**: Chyby Chat Completions používaly `error.body["innererror"]["content_filter_result"]` (jednotné číslo). Chyby Responses API používají `error.body["content_filters"][0]["content_filter_results"]` (množné číslo v poli). Klíč `innererror` už neexistuje. Kód, který přímo přistupuje k `innererror`, vyvolá za běhu `KeyError` — při migraci je to snadné přehlédnout, protože se chyba projeví jen když filtr obsahu skutečně zasáhne. Při migraci vždy prohledejte `innererror`.
25. **Surová HTTP volání potřebují přepis URL a těla**: Aplikace volající Azure OpenAI REST přímo (pomocí `requests`, `httpx`, `aiohttp`) přes `/openai/deployments/{name}/chat/completions?api-version=...` musí přepnout na `/openai/v1/responses`. Tělo požadavku používá `input` místo `messages`, vyžaduje `max_output_tokens` a `store`, a parametr dotazu `api-version` je odebrán. Text odpovědi je v `output[0].content[0].text` — **nikoli** v `output_text`, což je vlastnost SDK pro pohodlí, která v surovém REST JSON není.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->