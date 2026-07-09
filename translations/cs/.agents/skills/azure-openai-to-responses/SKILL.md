---
name: azure-openai-to-responses
license: MIT
---
# Migrace Python aplikací z Azure OpenAI Chat Completions na Responses API

> **AUTORITATIVNÍ POKYNY — POSTUPUJTE PŘESNĚ**
>
> Tento skript migruje Pythonové kódy používající Azure OpenAI Chat Completions
> na jednotné Responses API. Postupujte přesně podle těchto instrukcí.
> Nevymýšlejte si převody parametrů ani tvary API.

---

## Spouštěče

Aktivujte tento skript, když uživatel chce:
- Migrovat Python aplikaci z Azure OpenAI Chat Completions na Responses API
- Aktualizovat použití Python OpenAI SDK na nejnovější tvar API vůči Azure OpenAI
- Připravit Python kód pro GPT-5 nebo novější modely vyžadující Responses na Azure
- Přepnout z `AzureOpenAI`/`AsyncAzureOpenAI` na standardní klienty `OpenAI`/`AsyncOpenAI` s endpointem v1
- Opravit varování o deprekacích týkající se konstruktorů `AzureOpenAI` nebo `api_version`

---

## ⚠️ Kompatibilita modelu — NEJPRVE ZKONTROLUJTE

> **Před migrací ověřte, že vaše nasazení Azure OpenAI podporuje Responses API.**

### 1. Rychlý test nasazení (nejrychlejší)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Poznámka**: `max_output_tokens` má na Azure OpenAI **minimum 16**. Hodnoty pod 16 vrací chybu 400. Pro testy používejte 50+.

Pokud to vrátí 404, model nasazení ještě Responses nepodporuje — podívejte se níže na reference nebo znovu nasaďte podporovaný model.

### 2. Zkontrolujte dostupné modely ve vaší oblasti (doporučeno)

Spusťte vestavěný nástroj kompatibility modelů, abyste viděli, co je dostupné s podporou Responses API právě v dané oblasti:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Tento dotaz běží na Azure ARM živě a zobrazuje matici kompatibility — které modely podporují Responses, strukturovaný výstup, nástroje atd. Použijte `--filter gpt-5.1,gpt-5.2` pro omezení výsledků nebo `--json` pro skriptování.

### 3. Kompletní reference podpory modelů

- **Živý dotaz**: `python migrate.py models` (viz výše — specifické pro oblast, vždy aktuální)
- **Prohlížení dostupnosti**: [Souhrnná tabulka modelů a dostupnost v oblastech](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Rychlý start & pokyny**: **https://aka.ms/openai/start**

### ⚠️ Omezení starších modelů

> **UPOZORNĚNÍ**: Starší modely (např. `gpt-4o`, `gpt-4`) nemusí plně podporovat všechny funkce Responses API.
>
> Známá omezení u starších modelů:
> - **Parametr `reasoning`**: Nepodporován u `gpt-4o-mini`, `gpt-4o` a mnoha modelů bez uvažování. Migrujte `reasoning` pouze pokud byl v původním kódu.
> - **Parametr `seed`**: V Responses API vůbec nepodporován — odstraňte ze všech požadavků.
> - **Strukturovaný výstup přes `text.format`**: Starší modely nemusí důsledně vynucovat JSON schémata s `strict: true`.
> - **Orchestrace nástrojů**: GPT-5+ řídí volání nástrojů jako součást vnitřního uvažování. Starší modely na Responses stále fungují, ale bez hluboké integrace.
> - **Omezení teploty**: Při migraci na `gpt-5` musí být teplota vynechána nebo nastavena na `1`. Starší modely toto omezení nemají.

### Modely řady O (o1, o3-mini, o3, o4-mini)

Modely řady O mají unikátní omezení parametrů. Při migraci aplikací cílících na o-sérii:

- **`temperature`**: Musí být `1` (nebo vynecháno). Modely řady O nepřijímají jiné hodnoty.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikace používající Azure-specifický `max_completion_tokens` musí přejít na `max_output_tokens`. Nastavte vysoké hodnoty (4096+), protože tokeny uvažování se počítají do limitu.
- **`reasoning_effort`**: Pokud aplikace používá `reasoning_effort` (low/medium/high), ponechte jej — Responses API tento parametr u o-série podporuje.
- **Chování streamování**: Modely o-série mohou bufferovat výstup do dokončení uvažování, než začnou generovat delta události textu. Streamování stále funguje, ale první `response.output_text.delta` může dorazit s větším zpožděním než u GPT modelů.
- **`top_p`**: Nepodporován u modelů o-série — odstraňte pokud je přítomen.
- **Použití nástrojů**: Modely o-série podporují nástroje přes Responses API stejně jako GPT modely, ale kvalita řízení volání nástrojů závisí na modelu.

**Akce — proaktivní oznámení o modelu**: Při skenování zjistěte, na jaký model aplikace cílí (názvy nasazení, env vars, konfigurace). Pokud je model `gpt-4o` nebo starší (ne gpt-4.1+), proaktivně informujte uživatele:
- Migrace bude fungovat pro základní text, chat, streamování a nástroje na současném modelu.
- Novější modely (`gpt-5.1`, `gpt-5.2`) nabízejí lepší orchestraci nástrojů, vynucování strukturovaného výstupu, uvažování a dostupnost v různých regionech.
- Měli by zvážit upgrade svého nasazení, až budou připraveni — migrace není blokována.

Neblokujte ani nepřekážejte migraci kvůli verzi modelu. Toto je jen informační upozornění.

### GitHub Models NEpodporuje Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) nepodporuje Responses API.**

Pokud kód obsahuje cestu pro GitHub Models (hledejte `base_url` odkazující na `models.github.ai` nebo `models.inference.ai.azure.com`), **odstraňte ji úplně** během migrace. Responses API vyžaduje Azure OpenAI, OpenAI nebo kompatibilní lokální endpoint (např. Ollama s podporou Responses).

Akce během skenování:
- Označit všechny GitHub Models cesty pro odstranění.

---

## Migrace frameworku

Mnoho aplikací používá vyšší vrstvy frameworků nad OpenAI. Při jejich migraci se mění vlastní API frameworku — nejen základní OpenAI volání.

### Microsoft Agent Framework (MAF)

**Nejprve zkontrolujte vaši verzi MAF** — migrace závisí na tom, zda máte MAF 1.0.0+ nebo předběžnou beta/rc verzi.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **již používá Responses API** — není potřeba migrace. Pokud kód používá starý `OpenAIChatCompletionClient` (který používá `chat.completions.create`), nahraďte jej `OpenAIChatClient`.

| Předtím | Poté |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Pro kontrolu verze: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF před 1.0.0 (beta/rc vydání)

Ve starších verzích MAF `OpenAIChatClient` používal Chat Completions. Aktualizujte na `agent-framework-openai>=1.0.0`, kde `OpenAIChatClient` používá Responses API jako výchozí.

Jinak není třeba měnit nic — API `Agent` a nástrojů zůstává stejné.

### LangChain (`langchain-openai`)

Přidejte `use_responses_api=True` do `ChatOpenAI()`. Také upravte přístup k odpovědi z `.content` na `.text`.

| Předtím | Poté |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Kompletní příklady před/po najdete v [cheat-sheet.md](./references/cheat-sheet.md).

---

## Pokyny pro migraci frontendů

> **Responses API je záležitost serverové strany.** Migrujte svůj Python backend; HTTP smlouva frontendu by měla zůstat nezměněna, pokud backend není pouze tenká propust — v tom případě zvažte přijetí tvaru požadavků Responses pro odstranění překladové vrstvy. Pokud frontend volá OpenAI přímo s klientským klíčem, přesuňte tato volání na backend.

### Deprekace `@microsoft/ai-chat-protocol`

NPM balíček `@microsoft/ai-chat-protocol` je deprecated a měl by být nahrazen [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Pokud jej najdete ve frontendu:

1. Nahraďte CDN skript:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Odstraňte instanci `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Nahraďte `client.getStreamedCompletion(messages)` přímým voláním `fetch()` na backend streaming endpoint.
4. Nahraďte `for await (const response of result)` za `for await (const chunk of readNDJSONStream(response.body))`.
5. Aktualizujte přístup k vlastnostem z `response.delta.content` / `response.error` na `chunk.delta.content` / `chunk.error`.

---

## Cíle

- Vyjmenovat všechna místa v Pythonu, která používají Chat Completions nebo staré Completions vůči Azure OpenAI.
- Navrhnout plán migrace a pořadí kroků pro Python kód.
- Provést bezpečné, minimální změny pro přechod na Responses API.
- Aktualizovat volající, aby zpracovávali schéma výstupu Responses; žádné kompatibilní obaly.
- Spustit testy/linty; opravit drobné chyby způsobené migrací.
- Připravit malé, snadno recenzovatelné změny a poskytnout souhrn s diffy (necommitovat).

---

## Zásady

- Měnit pouze soubory uvnitř git workspace. Nikdy ne mimo něj.
- Neponechávat zpětně kompatibilní shimy; migrujte kód na nový tvar API.
- Nezanechávat poe-tombstone komentáře nebo záložní soubory.
- Zachovat streamovací sémantiku, pokud byla předtím použita; jinak použít nestreamovací.
- V režimu schvalování žádat o souhlas před spuštěním příkazů nebo síťových volání.
- Nespouštět `git add`/`git commit`/`git push`; generovat pouze úpravy v pracovní kopii.

---

## Krok 0: Migrace Azure OpenAI klienta (předpoklad)

Pokud kód používá konstruktory `AzureOpenAI` nebo `AsyncAzureOpenAI`, nejprve migrujte na standardní konstruktory `OpenAI` / `AsyncOpenAI`. Azure-specifické konstruktory jsou deprecated v `openai>=1.108.1`.

### Proč API cesta v1?

Nový endpoint `/openai/v1` používá standardní klient `OpenAI()` místo `AzureOpenAI()`, nevyžaduje parametr `api_version` a funguje stejně na OpenAI i Azure OpenAI. Stejný kód klienta je připravený na budoucnost — není potřeba spravovat verze.

### Klíčové změny

| Předtím | Poté |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Odstranit úplně |

### Checklista úklidu

- Odstraňte argument `api_version` z konstrukce klienta.
- Odstraňte proměnné prostředí `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` z `.env`, nastavení aplikace a Bicep/infra souborů.
- Přejmenujte `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` v `.env`, nastavení aplikace, Bicep/infra a testovacích konfiguracích (standardní konvence Azure Identity SDK).
- Zajistěte verzi `openai>=1.108.1` v `requirements.txt` nebo `pyproject.toml`.

### Migrace proměnných prostředí

| Starý env var | Akce | Poznámky |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Odstranit** | S endpointem v1 není třeba `api_version` |
| `AZURE_OPENAI_API_VERSION` | **Odstranit** | Totéž co výše |
| `AZURE_OPENAI_CLIENT_ID` | **Přejmenovat** → `AZURE_CLIENT_ID` | Standardní konvence Azure Identity SDK pro `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Zachovat** | Pořád potřeba pro konstrukci `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Zachovat** | Používá se jako parametr `model` v `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Zachovat** | Používá se jako `api_key` pro autentizaci na klíč |

Pro příklady nastavení klienta (sync, async, EntraID, API klíč, multi-tenant) viz [cheat-sheet.md](./references/cheat-sheet.md).

---

## Krok 1: Detekce starých volání

Spusťte skript [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py), aby se našla všechna volání vyžadující migraci:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Nebo proveďte ruční vyhledávání — každý výskyt je cílem migrace:

```bash
# Volání staré API (nutno přepsat)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Zastaralé konstruktory klienta Azure (nutno nahradit)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Vzory přístupu k tvaru odpovědi (nutno aktualizovat)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definice nástrojů ve starém vnořeném formátu (nutno vyrovnat)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Výsledky nástrojů ve starém formátu (nutno převést na function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Zastaralé parametry (nutno odstranit nebo přejmenovat)
rg "response_format"
rg "max_tokens\b"        # přejmenovat na max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Zastaralé proměnné prostředí (vyčistit)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # mělo by být AZURE_CLIENT_ID

# Endpointy GitHub Models (nutno odstranit — Responses API není podporováno)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Legacy vzory na úrovni frameworku (nutno aktualizovat)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: nahradit OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: vyžaduje use_responses_api=True

# Testovací infrastruktura (nutno aktualizovat)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Přístup k chybovému tělu filtru obsahu (nutno aktualizovat — struktura se změnila)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # starý singulární tvar — nyní content_filter_results (množné číslo) uvnitř pole content_filters

# Surová HTTP volání na endpoint Chat Completions (nutno aktualizovat URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristiky (detekce a přepis)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Konstruktory klienta Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Nástroje**: převést definice nástrojů pro volání funkcí z vnořeného formátu (`{"type": "function", "function": {"name": ...}}`) na plochý formát Responses (`{"type": "function", "name": ...}`); použít `tool_choice`; vracet výsledky nástroje jako položky `{"type": "function_call_output", "call_id": ..., "output": ...}` (nikoli `{"role": "tool", ...}`).
- **Otočky nástrojů**: když model vrací volání funkcí, připojit položky `response.output` do konverzace (nikoli ručně slovník `{"role": "assistant", "tool_calls": [...]}`), poté připojit položky `function_call_output` za každý výsledek.
- **Pár ukázek volání nástrojů**: pokud konverzace obsahuje pevně zakódované příklady volání nástrojů, převést je na `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` položky. ID musí začínat na `fc_`.
- **`pydantic_function_tool()`**: tento pomocník stále generuje starý vnořený formát a je **nekompatibilní** s `responses.create()`. Nahradit ručními definicemi nástrojů nebo plochým wrapperem.
- **Vícekolové**: uchovávat historii konverzace v aplikaci; předávat předchozí kola přes položky `input`.
- **Formátování**: nahradit vrchní úroveň Chat `response_format` s `text.format` ve Responses. Kanonický tvar: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Položky obsahu**: nahradit Chat `content[].type: "text"` za Responses `content[].type: "input_text"` pro uživatelské/systémové příspěvky.
- **Položky obsahu obrázku**: nahradit Chat `content[].type: "image_url"` za Responses `content[].type: "input_image"`. Pole `image_url` se mění z vnořeného objektu `{"url": "..."}` na plochý řetězec. Viz cheat sheet pro příklady před/po.
- **Úsilí o uvažování**: **migrace `reasoning` pouze pokud již existuje v původním kódu**.
- **Zpracování chyb filtrů obsahu**: struktura těla chyby se změnila. Chat Completion používal `error.body["innererror"]["content_filter_result"]` (jednotné číslo); Responses API používá `error.body["content_filters"][0]["content_filter_results"]` (množné číslo, uvnitř pole). Kód přistupující k `innererror` vyvolá `KeyError`. Přepsat na novou cestu.
- **Přímé HTTP volání**: pokud aplikace volá REST API Azure OpenAI přímo (pomocí `requests`, `httpx`, atd.) přes `/openai/deployments/{name}/chat/completions?api-version=...`, přepsat na `/openai/v1/responses`. Tělo požadavku se mění: `messages` → `input`, přidat `max_output_tokens` a `store: false`, odebrat query parametr `api-version`. Tělo odpovědi se mění: `choices[0].message.content` → `output[0].content[0].text` (pozn.: `output_text` je vlastnost SDK, která není v surovém REST JSON).

---

## Krok 2: Aplikujte migraci

### Poznámky k migraci (Chat Completions → Responses)

- **Proč migrovat**: Responses je sjednocené API pro text, nástroje a streamování; Chat Completions je zastaralé. S GPT-5 je k dosažení nejlepšího výkonu vyžadován Responses.
- **HTTP**: Azure endpoint přechází z `/openai/deployments/{name}/chat/completions` na `/openai/v1/responses`.
- **Pole**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` zůstává beze změny.
- **Formátování**: `response_format` → `text.format` s odpovídajícím objektem.
- **Položky obsahu**: nahradit Chat `content[].type: "text"` za Responses `content[].type: "input_text"` pro systémové/uživatelské příspěvky.
- **Položky obsahu obrázku**: nahradit Chat `content[].type: "image_url"` za Responses `content[].type: "input_image"`. Plošné zjednodušení pole `image_url` ze `{"image_url": {"url": "..."}}` na `{"image_url": "..."}` (obyčejný řetězec – HTTPS URL nebo `data:image/...;base64,...` data URI).

### Referenční mapování parametrů

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (pole položek) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (beze změny) |
| `stop` | `stop` (beze změny) |
| `frequency_penalty` | `frequency_penalty` (beze změny) |
| `presence_penalty` | `presence_penalty` (beze změny) |
| `tools` / volání funkcí | `tools` (beze změny) |
| `seed` | **Odebrat** (není podporováno) |
| `store` | `store` (nastaveno na `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (plochý řetězec) |

Pro úplné příklady kódu před a po migraci viz [cheat-sheet.md](./references/cheat-sheet.md).

Pro migraci testovací infrastruktury (mocks, snapshots, assertions) viz [test-migration.md](./references/test-migration.md).

Pro řešení problémů a varování viz [troubleshooting.md](./references/troubleshooting.md).

---

## Uchovávání dat a stav

- Nastavit `store: false` u všech požadavků Responses.
- Nespoléhat se na předchozí ID zpráv či kontext uchovávaný serverem; stav spravovat na straně klienta a minimalizovat metadata.

---

## Akceptační kritéria

### Kódové podmínky (vše musí projít)

- [ ] Žádné shody pro `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` v migrovaných souborech.
- [ ] Žádné shody pro `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — všichni konstruktory používají `OpenAI`/`AsyncOpenAI` s v1 endpointem.
- [ ] Žádné shody pro `rg "models\.github\.ai|models\.inference\.ai\.azure"` — odstraňují se cesty kódů GitHub Models.
- [ ] Žádné shody pro `rg "OpenAIChatCompletionClient"` — kód MAF verze 1.0.0+ používá `OpenAIChatClient` (který používá Responses API). Před verze 1.0.0: upgrade na `agent-framework-openai>=1.0.0`.
- [ ] Všechny volání `ChatOpenAI(...)` obsahují `use_responses_api=True`.
- [ ] Žádné shody pro `rg "choices\[0\]"` — veškerý přístup k odpovědím používá `resp.output_text` nebo schéma výstupu Responses.
- [ ] Není žádný `response_format` na vrchní úrovni; veškerý strukturovaný výstup používá `text={"format": {...}}`.
- [ ] `openai>=1.108.1` a `azure-identity` v `requirements.txt` nebo `pyproject.toml`; závislosti přeinstalovány.
- [ ] `store=False` nastaveno v každém volání `responses.create`.
- [ ] Žádné `api_version` v konstrukci klienta; `AZURE_OPENAI_API_VERSION` odstraněno z env souborů a infrastruktury.

### Podmínky testovací infrastruktury (vše musí projít)

- [ ] Žádné shody pro `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Žádné shody pro `rg "_azure_ad_token_provider" tests/` — aserce upraveny, aby kontrolovaly `isinstance(client, AsyncOpenAI)` nebo `base_url`.
- [ ] Žádné shody pro `rg "prompt_filter_results|content_filter_results" tests/` — odebrány specifické Azure mocky filtrů.
- [ ] Mock fixture používají `kwargs.get("input")` nikoli `kwargs.get("messages")`.
- [ ] Snapshot / zlaté soubory aktualizovány na formato streamování Responses (žádné `choices[0]`, `function_call`, `logprobs` atd.).
- [ ] `pytest` proběhne bez chyb po všech aktualizacích testů.

### Chování (ověřit manuálně nebo testovacím rámcem)

- [ ] **Základní dokončení**: non-streaming `responses.create` vrátí neprázdný `output_text`.
- [ ] **Parita streamování**: pokud původní kód používal streamování, migrovaný kód streamuje a yielduje `response.output_text.delta` události s neprázdnými delta změnami.
- [ ] **Strukturovaný výstup**: pokud se používá `text.format` s `json_schema`, `json.loads(resp.output_text)` uspěje a odpovídá schématu.
- [ ] **Smyčka volání nástrojů**: pokud jsou použity nástroje, model provádí volání nástrojů, aplikace je spouští a další požadavek vrátí finální `output_text` (bez nekonečné smyčky).
- [ ] **Async parita**: pokud byl používán `AsyncAzureOpenAI`, ekvivalent `AsyncOpenAI` funguje s `await`.
- [ ] **Míra chyb**: žádné nové chyby 400/401/404 oproti stavu před migrací.

### Výstupy

- Shrnutí zahrnuje editované soubory, počty legacy volání před/po a další kroky.
- Změny jsou pouze v pracovním stromu (bez commitů).

---

## Požadavky na verzi SDK

| Balíček | Minimální verze |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Nejnovější (pro autentizaci EntraID) |

---

## Reference

- [Cheat Sheet — všechny ukázky kódu](./references/cheat-sheet.md)
- [Test Migration — mocky, snapshoty, aserce](./references/test-migration.md)
- [Řešení problémů — chyby, tabulka rizik, nástrahy](./references/troubleshooting.md)
- [detect_legacy.py — automatizovaný skener](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentace](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Životní cyklus verze Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Reference OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->