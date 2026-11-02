# Riešenie problémov, tabuľka rizík a úskalia

## Riešenie problémov s chybami 400

| Chyba | Oprava |
|-------|--------|
| `missing_required_parameter: tools[0].name` | Definícia nástroja používa starý vnorený formát Chat Completions | Zplošťte z `{"type": "function", "function": {"name": ...}}` na `{"type": "function", "name": ..., "parameters": ...}` — meno, popis, parametre idú na hornú úroveň |
| `unknown_parameter: input[N].tool_calls` | Výsledky nástroja pri viackrát prebiehajúcom rozhovore používajú starý formát Chat Completions | Nahraďte `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` položkami `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Nástroj s `strict: true` nemá pole `required` | Keď je `strict: true`, všetky vlastnosti musia byť uvedené v `required` a musí byť nastavené `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Nástroj s `strict: true` postráda `additionalProperties: false` | Pridajte `"additionalProperties": false` do objektu parametrov |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID funkčného volania vo formáte "few-shot" má nesprávny prefix | ID funkčných volaní musia začínať na `fc_` (napr. `fc_example1`), nie `call_` |
| `missing_required_parameter: text.format.name` | Pridajte kľúč `"name"` do formátovacieho slovníka (napr. `"name": "Output"`) |
| `invalid_type: text.format` | Uistite sa, že `text.format` je slovník s kľúčmi `type`, `name`, `strict`, `schema` — nie reťazec |
| `invalid input content type` | Použite typy obsahu `input_text`/`output_text` namiesto Chat `text` |
| `invalid input content type` (obrázok) | Obsah obrázka stále používa `"type": "image_url"` | Zmeňte na `"type": "input_image"` |
| `Expected object, got string` na `image_url` | `image_url` je stále vnorený objekt `{"url": "..."}` | Zplošťte na obyčajný reťazec: `"image_url": "https://..."` alebo `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` pre `max_output_tokens` | Minimálna hodnota je **16** na Azure OpenAI. Použite 50+ pre testy, 1000+ pre produkciu. |
| `429 Too Many Requests` počas streamovania | Limitovanie rýchlosti. Obalte streamovanie do `try/except`, vráťte chybový JSON na front-end, implementujte spätný odklad/pokračovanie. |
| `KeyError: 'innererror'` pri chybe filtra obsahu | Štruktúra obsahu chyby filtra sa zmenila v Responses API | Chat Completions používal `error.body["innererror"]["content_filter_result"]`; Responses API používa `error.body["content_filters"][0]["content_filter_results"]` (v množnom čísle, v poli). Prepíšte všetky prístupy k `innererror`. |

---

## Tabuľka rizík migrácie

| Príznak | Pravdepodobná chyba | Oprava |
|---------|-------------------|--------|
| Prázdny `output_text` / skrátená odpoveď | `max_output_tokens` príliš nízke pre modely s rozumovaním | Nastavte `max_output_tokens=1000` alebo viac — výpočet tokenov pre rozumovanie sa počíta do limitu |
| `400 invalid_type: text.format` | Preniesli ste reťazec `response_format` namiesto slovníka `text.format` | Použite `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` na `/openai/v1/responses` | Nesprávna `base_url` — chýba prípona `/openai/v1/` | Uistite sa, že `base_url=f"{endpoint}/openai/v1/"` (s lomkou na konci) |
| `401 Unauthorized` po prechode na `OpenAI()` | `api_key` nie je nastavený alebo token provider nebol správne odovzdaný | Pre EntraID: `api_key=token_provider` (volateľné). Pre API kľúč: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model vracia `deployment not found` | Parameter `model` nezodpovedá názvu Azure deploymentu | Použite `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — toto je názov deploymentu, nie modelu |
| `json.loads(resp.output_text)` vyhadzuje `JSONDecodeError` | Schéma nie je vynútená alebo model nepodporuje prísny JSON | Uistite sa, že v schéme je `"strict": True`, a overte, či model podporuje štruktúrovaný výstup |
| Streamovanie nevracia žiadne `delta` udalosti | Kontrola nesprávneho typu udalostí | Filtrujte podľa `event.type == "response.output_text.delta"`, nie podľa Chat `chat.completion.chunk` |
| `400` chyba na obrázkový vstup po migrácii | Typ obsahu obrázku neaktualizovaný | Zmeňte `"type": "image_url"` → `"type": "input_image"` a zplošťte `"image_url": {"url": "..."}` → `"image_url": "..."` (obyčajný reťazec) |
| Volania nástroja sa nekonečne opakujú | Chýba výsledok nástroja v následnom `input` | Po vykonaní nástroja pridajte do `input` v ďalšom requeste položku `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| Chyba `temperature` pri GPT-5 alebo o-series | Explicitná hodnota `temperature` okrem 1 | Odstráňte `temperature` alebo nastavte na `1` pre GPT-5 a modely o-series (o1, o3-mini, o3, o4-mini) |
| Chyba `top_p` pri o-series | `top_p` nie je podporovaný | Odstráňte `top_p` pri cielení na modely o-series |
| Nerozpoznané `max_completion_tokens` | Používanie parametra špecifického pre Azure | Nahraďte `max_completion_tokens` za `max_output_tokens`. Pre o-series nastavte 4096+ (tokeny pre rozumovanie sa počítajú do limitu). |
| Prázdny alebo skrátený výstup z o-series | `max_output_tokens` príliš nízke | O-series používa vnútorné tokeny pre rozumovanie. Nastavte `max_output_tokens=4096` alebo viac — nie 500–1000. |
| `400 integer_below_min_value` pre `max_output_tokens` | Hodnota pod 16 | Azure OpenAI vyžaduje `max_output_tokens >= 16`. Použite 50+ pre základné testy, 1000+ pre produkciu. |
| `429 Too Many Requests` počas streamovania | Limitovanie Azure OpenAI | Streamovanie sa ticho preruší bez chybového hlásenia. Vždy obalujte `async for event in await coroutine:` do `try/except` a vráťte `{"error": str(e)}` na front-end. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Nesprávny tenant alebo neprihlásenie | Explicitne odovzdajte `tenant_id=os.getenv("AZURE_TENANT_ID")`. Lokálne spustite `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` pri používaní GitHub Models (`models.github.ai`) | GitHub Models nepodporuje Responses API | Odstráňte úplne cestu kódu pre GitHub Models. Použite Azure OpenAI, OpenAI alebo kompatibilný lokálny endpoint (napr. Ollama s podporou Responses). |
| MAF `OpenAIChatCompletionClient` stále používa Chat Completions | Používanie legacy MAF klienta v 1.0.0+ | V MAF 1.0.0+ používa `OpenAIChatClient` defaultne Responses API. Nahraďte `OpenAIChatCompletionClient` za `OpenAIChatClient`. Pre verziu pred 1.0.0 upgradujte na `agent-framework-openai>=1.0.0`. |
| LangChain agent vracia prázdny výstup alebo zlyháva pri volaniach nástrojov | `ChatOpenAI` nepoužíva Responses API | Pridajte `use_responses_api=True` do `ChatOpenAI(...)`. Tiež zmeňte `.content` → `.text` v odpovediach správ. |
| `KeyError: 'innererror'` v spracovaní chyby filtra obsahu | Štruktúra chyby sa zmenila v Responses API | Prepíšte `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Wrapper `innererror` zmizol; detaily filtra obsahu sú teraz v poli `content_filters` na najvyššej úrovni s množným `content_filter_results` v každej položke. |
| Surový HTTP volanie na `/openai/deployments/.../chat/completions` vracia 404 | Starý REST endpoint Chat Completions | Prepíšte URL na `/openai/v1/responses`. Zmeňte telo požiadavky: `messages` → `input`, pridajte `max_output_tokens` + `store: false`, odstráňte dotazovací parameter `api-version`. Zmeny v parsovaní odpovede: `choices[0].message.content` → `output[0].content[0].text` (poznámka: `output_text` je vlastnosť SDK, nie je v surovom REST JSON). |

---

## Úskalia

1. Ak ste predtým používali Chat Completions na stav rozhovoru, spravujte si stav explicitne s Responses.
2. Uprednostňujte `max_output_tokens` pred starým `max_tokens`.
3. Pri migrácii na `gpt-5` sa uistite, že `temperature` nie je určená alebo je nastavená na `1`.
4. Nahraďte Chat `content[].type: "text"` za Responses `content[].type: "input_text"` pre používateľské/systemové vstupy.
5. Pre `text.format` dodajte správny slovník (napr. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), nie obyčajný reťazec.
6. Parameter `seed` nie je v Responses podporovaný; odstráňte ho z požiadaviek.
7. **Rozumovanie**: Zahrňujte `reasoning` iba ak pôvodný kód ho už používal. Nepridávajte `reasoning` volaniam API, ktoré ho nemali — veľa modelov bez rozumovania tento parameter nepodporuje.
8. **Veľkosť `max_output_tokens`**: Pre modely s rozumovaním (GPT-5-mini, GPT-5, o-series) používajte `max_output_tokens=4096` alebo viac — nie 50–1000. Model používa interné tokeny rozumovania pred generovaním viditeľného výstupu; príliš nízke limity spôsobujú skrátené alebo prázdne odpovede.
9. **O-series `max_completion_tokens`**: Ak pôvodný kód používal `max_completion_tokens` (Azure špecifické pre o-series), nahraďte ho `max_output_tokens`. Responses API neprijíma `max_completion_tokens`.
10. **O-series `reasoning_effort`**: Ak pôvodný kód používa `reasoning_effort` (low/medium/high), migrujte ho na `reasoning={"effort": "<hodnota>"}` v volaní Responses API.
11. **O-series oneskorenie pri streamovaní**: Modely o-series vykonávajú vnútorné rozumovanie pred generovaním výstupu. Pri streamovaní očakávajte dlhšie oneskorenie pred prvou udalosťou `response.output_text.delta`. Je to normálne — model rozmýšľa, nezamrzol.
9. **`_azure_ad_token_provider` už nie je**: `AsyncOpenAI` / `OpenAI` nemajú atribút `_azure_ad_token_provider`. Testy alebo kód, ktorý k nemu pristupuje, zlyhá s `AttributeError`. Poskytovateľ tokenu je odovzdaný ako `api_key` a nedá sa skontrolovať na klientskom objekte.
10. **Snapshoty / golden súbory**: Ak testovacia sada používa snapshot testovanie, **všetky** snapshot súbory obsahujúce tvary Chat Completions streamingu (`choices[0]`, `content_filter_results`, `function_call` atď.) musia byť aktualizované na nový tvar Responses. Je to ľahké prehliadnuť a spôsobuje chyby pri asertácii snapshotov.
11. **Monkeypatch cestu**: Cieľ monkeypatchu sa mení zo `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (alebo `Responses.create` pre synchronné volanie). Použitie starej cesty ticho nefunguje — mock nezachytí volania a testy volajú skutočné API alebo zlyhávajú.
12. **`input` nie `messages`**: Mock funkcie musia čítať `kwargs.get("input")`, nie `kwargs.get("messages")`. Responses API používa `input` pre históriu rozhovoru.
13. **Názvy env premenných**: Azure Identity SDK používa `AZURE_CLIENT_ID` (nie `AZURE_OPENAI_CLIENT_ID`) pre `ManagedIdentityCredential(client_id=...)`. Premenujte v testoch, `.env` súboroch, nastaveniach aplikácie a Bicep/infra.
14. **Minimálna hodnota `max_output_tokens` je 16**: Azure OpenAI odmieta hodnoty pod 16 s chybou `400 integer_below_min_value`. Pre základné testy použite 50, pre produkciu 1000+. Starý `max_tokens` nemal takýto limit.
15. **`tenant_id` pre `AzureDeveloperCliCredential`**: Ak je Azure OpenAI zdroj v inom tenante, **musíte** explicitne odovzdať `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Bez toho credential ticho používa nesprávny tenant a vracia `401`.
16. **Limity rýchlosti sa prejavujú inak pri streamovaní**: S Chat Completions 429 typicky zabránilo štartu streamu. S Responses API streamovaním môže 429 nastať **počas streamu** — asynchrónny iterátor vyhodí výnimku. Vždy obalte streamovaciu slučku do `try/except` a vráťte chybový JSON riadok, aby front-end vedel chybu pekne spracovať.

17. **Spracovanie chýb streamovania je povinné pre webové aplikácie**: Vzor `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` je kľúčový. Bez neho SSE/JSONL stream ticho zanikne pri akejkoľvek chybe na strane servera a frontend visí.
18. **Definície nástrojov musia používať plochý formát**: Responses API očakáva `{"type": "function", "name": ..., "parameters": ...}` — nie vnorený formát Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Toto je najčastejšia chyba pri migrácii pre kód volajúci funkcie.
19. **`pydantic_function_tool()` nie je kompatibilný**: Pomocná funkcia `openai.pydantic_function_tool()` stále generuje starý vnorený formát. Nepoužívajte ju s `responses.create()`. Definujte schémy nástrojov manuálne alebo výstup zplošťte.
20. **Výsledky nástrojov používajú `function_call_output`, nie `role: tool`**: Po vykonaní nástroja pridajte `{"type": "function_call_output", "call_id": ..., "output": ...}` — nie `{"role": "tool", "tool_call_id": ..., "content": ...}`. Pre žiadosť asistenta o nástroj používajte `messages.extend(response.output)` — nie manuálny slovník `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` vyžaduje `required` + `additionalProperties: false`**: Pri použití `strict: true` na nástroji musí byť každá vlastnosť uvedená v poli `required` a `additionalProperties` musí byť `false`. Chýbanie ktoréhokoľvek spôsobí chybu 400.
22. **ID volania funkcií majú špecifické prefixy**: Pri poskytovaní položiek `function_call` vo formáte few-shot v `input` musí pole `id` začínať na `fc_` a pole `call_id` na `call_` (napr. `"id": "fc_example1", "call_id": "call_example1"`). Použitie starého prefixu Chat Completions `call_` pre `id` sa odmieta.
23. **GitHub Models nepodporuje Responses API**: Ak aplikácia má GitHub Models kódovú cestu (`base_url` ukazujúcu na `models.github.ai` alebo `models.inference.ai.azure.com`), odstráňte ju úplne. Neexistuje migrácia — prepnite na Azure OpenAI, OpenAI alebo kompatibilný lokálny endpoint.
24. **Štruktúra tela chyby filtra obsahu sa zmenila**: Chyby Chat Completions používali `error.body["innererror"]["content_filter_result"]` (v jednotnom čísle). Chyby Responses API používajú `error.body["content_filters"][0]["content_filter_results"]` (v množnom čísle, v poli). Kľúč `innererror` už neexistuje. Kód priamo pristupujúci k `innererror` vyvolá za behu `KeyError` — toto sa ľahko prehliadne pri migrácii, pretože sa prejaví len keď filter obsahu naozaj spustí. Pri migrácii vždy vyhľadajte `innererror`.
25. **Priame HTTP volania vyžadujú prepísanie URL + tela**: Aplikácie volajúce Azure OpenAI REST priamo (cez `requests`, `httpx`, `aiohttp`) pomocou `/openai/deployments/{name}/chat/completions?api-version=...` musia prejsť na `/openai/v1/responses`. Telo požiadavky používa `input` namiesto `messages`, vyžaduje `max_output_tokens` a `store`, a parameter `api-version` sa vynecháva. Text v odpovedi je v `output[0].content[0].text` — **nie** v `output_text`, čo je pohodlné vlastnosť SDK, ktorá v surovom REST JSON nie je.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->