# Riešenie problémov, tabuľka rizík a úskalia

## Riešenie problémov s chybami 400

| Chyba | Oprava |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definícia nástroja používa starý vnorený formát Chat Completions | Zjednodušte z `{"type": "function", "function": {"name": ...}}` na `{"type": "function", "name": ..., "parameters": ...}` — názov, popis, parametre idú na hornú úroveň |
| `unknown_parameter: input[N].tool_calls` | Výsledky nástroja pri viackolovej interakcii používajú starý formát Chat Completions | Nahraďte `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` položkami `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Nástroj s `strict: true` postráda pole `required` | Pri `strict: true` musia byť všetky vlastnosti uvedené v `required` a nastavené `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Nástroj s `strict: true` postráda `additionalProperties: false` | Pridajte `"additionalProperties": false` do objektu parametrov |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID volania funkcie pre few-shot má nesprávny prefix | ID volaní funkcií musia začínať `fc_` (napr. `fc_example1`), nie `call_` |
| `missing_required_parameter: text.format.name` | Pridajte kľúč `"name"` do slovníka formátu (napr. `"name": "Output"`) |
| `invalid_type: text.format` | Overte, že `text.format` je slovník s kľúčmi `type`, `name`, `strict`, `schema` — nie je to reťazec |
| `invalid input content type` | Používajte typy obsahu `input_text`/`output_text` namiesto Chat `text` |
| `invalid input content type` (obrázok) | Obsah obrázka stále používa `"type": "image_url"` | Zmeňte na `"type": "input_image"` |
| `Expected object, got string` na `image_url` | `image_url` je stále vnorený objekt `{"url": "..."}` | Zjednodušte na obyčajný reťazec: `"image_url": "https://..."` alebo `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` pre `max_output_tokens` | Minimálna hodnota je **16** u Azure OpenAI. Používajte 50+ pre testy, 1000+ do produkcie. |
| `429 Too Many Requests` počas streamovania | Obmedzenie počtu požiadaviek. Obalte streamovanie do `try/except`, vráťte chybový JSON na frontend, implementujte časový odstup/opakovanie. |
| `KeyError: 'innererror'` pri chybe filtru obsahu | Štruktúra tela chyby filtra obsahu sa zmenila v Responses API | Chat Completions používal `error.body["innererror"]["content_filter_result"]`; Responses API využíva `error.body["content_filters"][0]["content_filter_results"]` (v množnom čísle, v poli). Prepíšte všetky prístupy k `innererror`. |

---

## Tabuľka rizík migrácie

| Príznak | Pravdepodobná chyba | Oprava |
|---------|---------------|-----|
| Prázdny `output_text` / skrátená odpoveď | `max_output_tokens` príliš nízke pre modely s odôvodňovaním | Nastavte `max_output_tokens=1000` alebo viac — tokeny odôvodňovania sa počítajú do limitu |
| `400 invalid_type: text.format` | Bola predaná reťazcová hodnota `response_format` namiesto slovníka `text.format` | Použite `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` na `/openai/v1/responses` | Nesprávna hodnota `base_url` — chýba prípona `/openai/v1/` | Uistite sa, že `base_url=f"{endpoint}/openai/v1/"` (s lomítkom na konci) |
| `401 Unauthorized` po prepnutí na `OpenAI()` | `api_key` nie je nastavený alebo token provider nebol správne odovzdaný | Pre EntraID: `api_key=token_provider` (volateľný objekt). Pre API kľúč: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model vracia `deployment not found` | Parameter `model` neodpovedá názvu Azure nasadenia | Použite `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — toto je názov nasadenia, nie modelu |
| `json.loads(resp.output_text)` vyhadzuje `JSONDecodeError` | Schéma nie je vynútená alebo model nepodporuje prísny JSON | Uistite sa, že je v schéme `"strict": True` a overte, či model podporuje štruktúrovaný výstup |
| Streamovanie nevydáva žiadne udalosti `delta` | Kontrolujete nesprávny typ udalosti | Filtrujte podľa `event.type == "response.output_text.delta"`, nie podľa Chat `chat.completion.chunk` |
| Chyba 400 na obrazový vstup po migrácii | Typ obsahu obrázka nebol aktualizovaný | Zmeňte `"type": "image_url"` → `"type": "input_image"` a zjednodušte `"image_url": {"url": "..."}` → `"image_url": "..."` (obyčajný reťazec) |
| Volanie nástroja sa nekonečne opakuje | Chýba výsledok nástroja vo vstupnom poli v nasledujúcej požiadavke | Po vykonaní nástroja pridajte do `input` v ďalšej požiadavke položku `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| Chyba `temperature` pri GPT-5 alebo sérii o | Explicitná hodnota `temperature` iná než 1 | Odstráňte `temperature` alebo nastavte na `1` pre modely GPT-5 a o-serie (o1, o3-mini, o3, o4-mini) |
| Chyba `top_p` pri o-serii | `top_p` nie je podporované | Odstráňte `top_p` pri cieľovej o-serii modelov |
| `max_completion_tokens` nie je rozpoznané | Používate parameter špecifický pre Azure | Nahraďte `max_completion_tokens` parametrom `max_output_tokens`. Pre o-serie nastavte 4096+ (tokeny odôvodňovania sa počítajú do limitu). |
| Prázdny/skrátený výstup z o-serie | `max_output_tokens` je príliš nízke | O-serie používajú interné tokeny odôvodňovania. Nastavte `max_output_tokens=4096` alebo viac — nie 500–1000. |
| `400 integer_below_min_value` pre `max_output_tokens` | Hodnota je pod 16 | Azure OpenAI vyžaduje `max_output_tokens >= 16`. Používajte 50+ pre testovanie dymom, 1000+ do produkcie. |
| `429 Too Many Requests` uprostred streamu | Obmedzenie cez Azure OpenAI | Stream sa ticho preruší bez spracovania chyby. Vždy obalujte `async for event in await coroutine:` do `try/except` a posielajte `{"error": str(e)}` na frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Nesprávny tenant alebo neprihlásený používateľ | Explicitne odovzdajte `tenant_id=os.getenv("AZURE_TENANT_ID")`. Lokálne spustite `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` pri použití GitHub modelov (`models.github.ai`) | GitHub modely nepodporujú Responses API | Kompletné odstránenie použitia GitHub modelov. Používajte Azure OpenAI, OpenAI alebo kompatibilný lokálny endpoint (napr. Ollama s podporou Responses). |
| MAF `OpenAIChatCompletionClient` stále používa Chat Completions | Používate starý MAF klient v 1.0.0+ | V MAF 1.0.0+ používa `OpenAIChatClient` predvolene Responses API. Nahraďte `OpenAIChatCompletionClient` za `OpenAIChatClient`. Pri verzii nižšej ako 1.0.0 aktualizujte na `agent-framework-openai>=1.0.0`. |
| LangChain agent vracia prázdne alebo zlyháva pri volaniach nástrojov | `ChatOpenAI` nepoužíva Responses API | Pridajte `use_responses_api=True` do `ChatOpenAI(...)`. Zmeňte tiež `.content` na `.text` v odpovediach správ. |
| `KeyError: 'innererror'` v spracovaní chyby filtra obsahu | Zmenená štruktúra tela chyby v Responses API | Prepíšte `error.body["innererror"]["content_filter_result"]["jailbreak"]` na `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Zábal `innererror` zmizol; detaily filtra obsahu sú v top-level poli `content_filters` a v každom zázname pole `content_filter_results` (množné číslo). |
| Priamý HTTP požiadavok na `/openai/deployments/.../chat/completions` vracia 404 | Starý REST endpoint Chat Completions | Prepíšte URL na `/openai/v1/responses`. Zmeňte telo požiadavky: `messages` → `input`, pridajte `max_output_tokens` + `store: false`, odstráňte query parameter `api-version`. Zmeňte spracovanie odpovede: `choices[0].message.content` → `output[0].content[0].text` (poznámka: `output_text` je vlastnosť SDK, nie v surovom REST JSON). |

---

## Úskalia

1. Ak ste predtým používali Chat Completions na stav konverzácie, spravujte svoj vlastný stav explicitne s Responses.
2. Uprednostňujte `max_output_tokens` namiesto starého `max_tokens`.
3. Pri migrácii na `gpt-5` sa uistite, že `temperature` nie je špecifikovaná alebo je nastavená na `1`.
4. Nahraďte Chat `content[].type: "text"` za Responses `content[].type: "input_text"` pre vstupy používateľa/systému.
5. Pre `text.format` poskytnite platný slovník (napr. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), nie obyčajný reťazec.
6. Parameter `seed` nie je v Responses podporovaný; odstráňte ho z požiadaviek.
7. **Odôvodňovanie**: Zahrňte `reasoning` iba, ak ho pôvodný kód už používal. Nepridávajte `reasoning` do volaní API, ktoré ho nemali — mnoho modelov (napr. gpt-4o-mini) tento parameter nepodporuje.
8. **Veľkosť `max_output_tokens`**: Pre modely s odôvodňovaním (GPT-5-mini, GPT-5, o-serie) používajte `max_output_tokens=4096` alebo viac — nie 50–1000. Model interné tokeny odôvodňovania používa ešte pred generovaním viditeľného výstupu; príliš nízky limit spôsobuje skrátené alebo prázdne odpovede.
9. **O-serie `max_completion_tokens`**: Ak pôvodný kód používal `max_completion_tokens` (špecifické pre Azure o-serie), nahraďte ho `max_output_tokens`. Responses API `max_completion_tokens` neprijíma.
10. **O-serie `reasoning_effort`**: Ak pôvodný kód používa `reasoning_effort` (low/medium/high), preveďte ho do `reasoning={"effort": "<hodnota>"}` vo volaní Responses API.
11. **O-serie streamingové oneskorenie**: Modely o-serie vykonávajú interné odôvodňovanie pred generovaním výstupu. Pri streamovaní očakávajte dlhšie oneskorenie pred prvou udalosťou `response.output_text.delta`. Je to normálne — model odôvodňuje, nie je zaseknutý.
9. **`_azure_ad_token_provider` už neexistuje**: `AsyncOpenAI` / `OpenAI` nemajú atribút `_azure_ad_token_provider`. Testy alebo kód, ktorý pristupuje k tomuto atribútu, zlyhá s `AttributeError`. Token provider sa odovzdáva ako `api_key` a nie je prístupný na inšpekciu v klientovi.
10. **Snapshot / zlaté súbory**: Ak testovací balík používa snapshot testovanie, **všetky** snapshot súbory obsahujúce tvary streamovania Chat Completions (`choices[0]`, `content_filter_results`, `function_call` atď.) musia byť aktualizované na nový tvar Responses. Toto sa ľahko prehliadne a spôsobuje zlyhania asercie snapshotov.
11. **Cieľ úpravy počas testovania (monkeypatch)**: Cieľ monkeypatch sa mení z `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (alebo `Responses.create` pre synchronné volania). Použitie starej cesty ticho nič neurobí — mock nebude zachytený a testy zasiahnu skutočné API alebo zlyhajú.
12. **`input` nie `messages`**: Mock funkcie musia čítať `kwargs.get("input")` nie `kwargs.get("messages")`. Responses API používa `input` pre históriu konverzácie.
13. **Názvoslovie pre environmentálne premenné**: Azure Identity SDK používa `AZURE_CLIENT_ID` (nie `AZURE_OPENAI_CLIENT_ID`) pre `ManagedIdentityCredential(client_id=...)`. Preverte v testoch, `.env` súboroch, nastaveniach aplikácie a Bicep/infra.
14. **Minimum `max_output_tokens` je 16**: Azure OpenAI odmieta hodnoty pod 16 s chybou `400 integer_below_min_value`. Používajte 50 pre dymové testy, 1000+ do produkcie. Starý parameter `max_tokens` také minimum nemal.
15. **`tenant_id` pre `AzureDeveloperCliCredential`**: Keď je Azure OpenAI zdroj v inom tenante, musíte explicitne odovzdať `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Bez toho používateľ ticho používa nesprávny tenant a vráti `401`.
16. **Limit počtu požiadaviek sa prejavuje inak pri streamovaní**: Pri Chat Completions chyba 429 obvykle zabránila spusteniu streamu. Pri streamovaní Responses API sa 429 môže vyskytnúť **počas streamu** — asynchrónny iterátor vyhodí výnimku. Vždy obalujte slučku streamovania do `try/except` a posielajte chybový JSON riadok, aby ho frontend vedel správne spracovať.

17. **Obsluha chýb streamovania je povinná pre webové aplikácie**: Vzor `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` je kľúčový. Bez neho SSE/JSONL stream ticho prestane fungovať pri akejkoľvek chybe na serverovej strane a frontend zamrzne.
18. **Definície nástrojov musia používať plochý formát**: Responses API očakáva `{"type": "function", "name": ..., "parameters": ...}` — nie vnorený formát Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Toto je najčastejšia chyba pri migrácii kódu používajúceho volanie funkcií.
19. **`pydantic_function_tool()` je nekompatibilný**: Pomocník `openai.pydantic_function_tool()` stále generuje starý vnorený formát. Nepoužívajte ho s `responses.create()`. Definujte schémy nástrojov ručne alebo splošťujte výstup.
20. **Výsledky nástrojov používajú `function_call_output`, nie `role: tool`**: Po vykonaní nástroja pridajte `{"type": "function_call_output", "call_id": ..., "output": ...}` — nie `{"role": "tool", "tool_call_id": ..., "content": ...}`. Pre požiadavku nástroja asistenta používajte `messages.extend(response.output)` — nie manuálnu slovníkovú štruktúru `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` vyžaduje `required` + `additionalProperties: false`**: Pri použití `strict: true` u nástroja musí byť každá vlastnosť uvedená v poli `required` a `additionalProperties` musí byť `false`. Chýbanie ktorejkoľvek z týchto položiek spôsobí chybu 400.
22. **ID volaní funkcií majú špecifické prefixy**: Pri poskytovaní niekoľkých položiek `function_call` v `input` musí pole `id` začínať na `fc_` a pole `call_id` na `call_` (napr. `"id": "fc_example1", "call_id": "call_example1"`). Použitie starého prefixu `call_` z Chat Completions pre `id` je odmietnuté.
23. **GitHub Models nepodporuje Responses API**: Ak aplikácia obsahuje kódovú cestu pre GitHub Models (`base_url` ukazujúce na `models.github.ai` alebo `models.inference.ai.azure.com`), úplne ju odstráňte. Neexistuje migračná cesta — prepnite na Azure OpenAI, OpenAI alebo kompatibilný lokálny endpoint.
24. **Štruktúra tela chyby filtra obsahu sa zmenila**: Chyby Chat Completions používali `error.body["innererror"]["content_filter_result"]` (v jednotnom čísle). Chyby Responses API používajú `error.body["content_filters"][0]["content_filter_results"]` (v množnom čísle, v poli). Kľúč `innererror` už neexistuje. Kód, ktorý priamo pristupuje k `innererror`, počas behu vyvolá `KeyError` — toto sa ľahko prehliadne pri migrácii, pretože sa to prejaví iba keď sa filter obsahu skutočne spustí. Pri migrácii vždy hľadajte `innererror`.
25. **Priame HTTP volania potrebujú prepísať URL a telo požiadavky**: Aplikácie, ktoré volajú Azure OpenAI REST priamo (pomocou `requests`, `httpx`, `aiohttp`) s `/openai/deployments/{name}/chat/completions?api-version=...` sa musia prepnúť na `/openai/v1/responses`. Telo požiadavky používa `input` namiesto `messages`, vyžaduje `max_output_tokens` a `store` a parameter `api-version` v URL sa odstraňuje. Text odpovede sa nachádza v `output[0].content[0].text` — **nie** v `output_text`, ktoré je vlastnosťou SDK nie prítomnou v surovom REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->