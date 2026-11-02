---
name: azure-openai-to-responses
license: MIT
---
# Migrace Python aplikací z Azure OpenAI Chat Completions na Responses API

> **AUTORITATIVNÍ POKYNY — POSTUPUJTE PŘESNĚ**
>
> Tento nástroj migruje Pythonové kódy používající Azure OpenAI Chat Completions
> na sjednocené Responses API. Postupujte podle těchto pokynů přesně.
> Nepřidávejte vlastní mapování parametrů ani nevymýšlejte tvary API.

---

## Spouštěče

Aktivujte tento nástroj, pokud uživatel chce:
- Migrovat Python aplikaci z Azure OpenAI Chat Completions na Responses API
- Aktualizovat používání Python OpenAI SDK na nejnovější tvar API pro Azure OpenAI
- Připravit Python kód pro modely GPT-5 nebo novější, které vyžadují Responses na Azure
- Přepnout z `AzureOpenAI`/`AsyncAzureOpenAI` na standardní klienty `OpenAI`/`AsyncOpenAI` s endpointem v1
- Opravit upozornění na zastaralost týkající se konstruktorů `AzureOpenAI` nebo `api_version`

---

## ⚠️ Kompatibilita modelu — NEJDŘÍVE ZKONTROLUJTE

> **Před migrací ověřte, zda vaše nasazení Azure OpenAI podporuje Responses API.**

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

> **Poznámka**: `max_output_tokens` má na Azure OpenAI **minimálně 16**. Hodnoty pod 16 vedou k chybě 400. Pro rychlé testy používejte 50+.

Pokud vrátí 404, model nasazení ještě Responses nepodporuje — podívejte se na referenci níže nebo nasazení přenastavte s podporovaným modelem.

### 2. Zkontrolujte dostupné modely ve vaší oblasti (doporučeno)

Spusťte vestavěný nástroj kompatibility modelů, abyste viděli, co je k dispozici s podporou Responses API ve vaší konkrétní oblasti:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Toto dotazuje Azure ARM v reálném čase a zobrazuje matici kompatibility — které modely podporují Responses, strukturovaný výstup, nástroje atd. Použijte `--filter gpt-5.1,gpt-5.2` pro omezení výsledků nebo `--json` pro skriptování.

### 3. Kompletní reference podpory modelů

- **Dotaz v reálném čase**: `python migrate.py models` (viz výše — specifické pro region, vždy aktuální)
- **Prohlédnout dostupnost**: [Tabulka přehledu modelů a dostupnost v regionech](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Rychlý start & pokyny**: **https://aka.ms/openai/start**

### ⚠️ Omezení starších modelů

> **VAROVÁNÍ**: Starší modely (před `gpt-4.1`) nemusí plně podporovat všechny funkce Responses API.
>
> Známá omezení se staršími modely:
> - **parametr `reasoning`**: Není podporován u mnoha modelů bez reasoning. Migrujte `reasoning` pouze pokud byl již v původním kódu přítomen.
> - **parametr `seed`**: Není podporován v Responses API vůbec – odstraňte ze všech požadavků.
> - **Strukturovaný výstup přes `text.format`**: Starší modely nemusejí spolehlivě vynucovat `strict: true` JSON schémata.
> - **Orchestrace nástrojů**: GPT-5+ řídí volání nástrojů jako součást reasoning. Starší modely v Responses stále fungují, ale nemají tuto hlubokou integraci.
> - **Omezení teploty**: Při migraci na `gpt-5` musí být teplota vynechána nebo nastavena na `1`. Starší modely nejsou tímto omezeny.

### O-série reasoning modely (o1, o3-mini, o3, o4-mini)

O-série modelů má specifická omezení parametrů. Při migraci aplikací cílených na O-sérii:

- **`temperature`**: Musí být `1` (nebo vynecháno). O-série modely nepřijímají jiné hodnoty.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikace používající Azure-specifické `max_completion_tokens` musí přejít na `max_output_tokens`. Nastavte vysoké hodnoty (4096+) protože tokeny reasoning se počítají do limitu.
- **`reasoning_effort`**: Pokud aplikace používá `reasoning_effort` (low/medium/high), ponechejte jej — Responses API tento parametr u O-série modelů podporuje.
- **Chování streamingu**: O-série modely mohou bufferovat výstup, dokud reasoning neskončí, před odesláním delta událostí textu. Streaming stále funguje, ale první `response.output_text.delta` může přijít s delším zpožděním než u GPT modelů.
- **`top_p`**: Není podporován na O-sérii — odstraňte pokud je přítomen.
- **Používání nástrojů**: O-série modely podporují nástroje přes Responses API stejně jako GPT modely, ale kvalita orchestrací volání nástrojů se liší podle modelu.

**Akce — proaktivní doporučení ohledně modelu**: Během fáze skenování zkontrolujte, jaký model aplikace používá (názvy nasazení, proměnné prostředí, konfigurace). Pokud model předchází `gpt-4.1` (není gpt-4.1+), proaktivně uživateli sdělte:
- Migrace bude fungovat pro základní text, chat, streaming a nástroje na jejich aktuálním modelu.
- Novější modely (`gpt-5.1`, `gpt-5.2`) nabízí lepší orchestraci nástrojů, vynucení strukturovaného výstupu, reasoning a dostupnost v různých regionech.
- Měli by zvážit upgrade svého nasazení, až budou připraveni — není to ale blokující pro migraci.

Nezabraňujte ani neodmítejte migraci na základě verze modelu. Toto doporučení je pouze informativní.

### GitHub Models nepodporuje Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) nepodporují Responses API.**

Pokud kódová základna obsahuje cestu ke GitHub Models (hledejte `base_url` směřující na `models.github.ai` nebo `models.inference.ai.azure.com`), **odstraňte ji úplně** během migrace. Responses API vyžaduje Azure OpenAI, OpenAI nebo kompatibilní lokální endpoint (např. Ollama s podporou Responses).

Akce během skenování:
- Označte všechny GitHub Models cesty kódu k odstranění.

---

## Migrace frameworku

Mnoho aplikací používá nadstandardní frameworky nad OpenAI. Při migraci těchto se mění API samotného frameworku — nejen podkladové OpenAI volání.

### Microsoft Agent Framework (MAF)

**Nejdříve zkontrolujte svou verzi MAF** — migrace záleží na tom, zda používáte MAF 1.0.0+ nebo před-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **již používá Responses API** — migrace není potřeba. Pokud kód používá starý `OpenAIChatCompletionClient` (který používá `chat.completions.create`), nahraďte jej `OpenAIChatClient`.

| Před | Po |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Pro kontrolu verze: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF před-1.0.0 (beta/rc verze)

V před-1.0.0 MAF `OpenAIChatClient` používal Chat Completions. Upgradujte na `agent-framework-openai>=1.0.0`, kde `OpenAIChatClient` výchozí používá Responses API.

Žádné další změny nejsou potřeba — API `Agent` a nástrojů zůstávají stejné.

### LangChain (`langchain-openai`)

Přidejte `use_responses_api=True` do `ChatOpenAI()`. Také změňte přístup k odpovědi z `.content` na `.text`.

| Před | Po |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Kompletní příklady kódu před a po najdete v [cheat-sheet.md](./references/cheat-sheet.md).

---

## Pokyny pro migraci frontendu

> **Responses API je záležitost serverové strany.** Migrujte svůj Python backend; HTTP kontrakt frontendu by měl zůstat nezměněn, pokud není backend jen tenkým průchodem — v tom případě zvažte přijetí Requests tvaru Responses API k odstranění překladové vrstvy. Pokud frontend volá OpenAI přímo s klíčem na straně klienta, přesuňte tyto volání nejdříve na backend.

### Deprecace `@microsoft/ai-chat-protocol`

NPM balíček `@microsoft/ai-chat-protocol` je zastaralý a měl by být nahrazen [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Pokud ho najdete ve frontendu:

1. Nahraďte CDN tag skriptu:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Odstraňte instanci `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Nahraďte `client.getStreamedCompletion(messages)` přímým voláním `fetch()` na backendový streaming endpoint.
4. Nahraďte `for await (const response of result)` cyklem `for await (const chunk of readNDJSONStream(response.body))`.
5. Aktualizujte přístupy k vlastnostem z `response.delta.content` / `response.error` na `chunk.delta.content` / `chunk.error`.

---

## Cíle

- Vypište všechna místa v Python kódu využívající Chat Completions nebo staré Completions vůči Azure OpenAI.
- Navrhněte plán migrace a pořadí změn pro Python kód.
- Proveďte bezpečné, minimální úpravy ke změně na Responses API.
- Aktualizujte volající, aby používali výstupní schéma Responses; bez zpětných kompatibilních obalů.
- Spusťte testy/linty; opravte drobné porušení způsobené migrací.
- Připravte malé, snadno kontrolovatelné změnové sady a poskytněte závěrečné shrnutí s rozdíly (neprovádějte commit).

---

## Zásady

- Měňte pouze soubory uvnitř git workspace. Nikdy nepište mimo něj.
- Neponechávejte shimové vrstvy zpětné kompatibility; migrujte kód na nový tvar API.
- Nezanechávejte přechodové komentáře ani záložní soubory.
- Zachovejte streamovací sémantiku, pokud byla používána; jinak používejte nestreamovací režim.
- Žádejte schválení před spuštěním příkazů nebo síťových volání v režimu schvalování.
- Nespouštějte `git add`/`git commit`/`git push`; dělejte pouze úpravy ve stromu pracovního prostoru.

---

## Krok 0: Migrace Azure OpenAI klienta (předpoklad)

Pokud kód používá konstruktory `AzureOpenAI` nebo `AsyncAzureOpenAI`, migrujte nejdříve na standardní `OpenAI` / `AsyncOpenAI` konstruktory. Azure-specifické konstruktory jsou zastaralé od `openai>=1.108.1`.

### Proč cesta API v1?

Nový endpoint `/openai/v1` používá standardního klienta `OpenAI()` místo `AzureOpenAI()`, nevyžaduje parametr `api_version` a pracuje stejně na OpenAI i Azure OpenAI. Stejný klient je budoucnostově kompatibilní — není potřeba spravovat verze.

### Klíčové změny

| Před | Po |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Odstranit úplně |

### Kontrolní seznam úklidu

- Odstraňte argument `api_version` z konstrukce klienta.
- Odstraňte proměnné prostředí `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` z `.env`, nastavení aplikace i Bicep/infra souborů.
- Přejmenujte `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` v `.env`, nastavení aplikace, Bicep/infra a testovacích fixturních souborech (standardní konvence Azure Identity SDK).
- Zajistěte `openai>=1.108.1` v `requirements.txt` nebo `pyproject.toml`.

### Migrace proměnných prostředí

| Starý env var | Akce | Poznámky |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Odstranit** | S endpointem v1 není třeba `api_version` |
| `AZURE_OPENAI_API_VERSION` | **Odstranit** | Totéž jako výše |
| `AZURE_OPENAI_CLIENT_ID` | **Přejmenovat** → `AZURE_CLIENT_ID` | Standardní konvence Azure Identity SDK pro `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Zachovat** | Stále potřeba pro konstrukci `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Zachovat** | Používá se jako parametr `model` v `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Zachovat** | Používá se jako `api_key` pro autentizaci pomocí klíče |

Příklady nastavení klienta (synch, asynch, EntraID, API klíč, multi-tenant) najdete v [cheat-sheet.md](./references/cheat-sheet.md).

---

## Krok 1: Detekujte stará volání

Spusťte skript [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py), který najde všechna volání, jež je třeba migrovat:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Nebo spusťte tyto vyhledávací dotazy ručně — každý výskyt je cílem migrace:

```bash
# Volání zastaralého API (nutno přepsat)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Zastaralé konstruktory Azure klientů (nutno nahradit)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Vzory přístupu ke struktuře odpovědi (nutno aktualizovat)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definice nástrojů ve starém vnořeném formátu (nutno zploštit)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Výsledky nástrojů ve starém formátu (nutno převést na function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Zastaralé parametry (nutno odstranit nebo přejmenovat)
rg "response_format"
rg "max_tokens\b"        # přejmenovat na max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Zastaralé proměnné prostředí (uklidit)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # mělo by být AZURE_CLIENT_ID

# Koncové body GitHub Models (nutno odstranit — Responses API není podporováno)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Zastaralé vzory na úrovni frameworku (nutno aktualizovat)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: nahradit za OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: potřeba use_responses_api=True

# Testovací infrastruktura (nutno aktualizovat)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Přístup k tělu chyby filtru obsahu (nutno aktualizovat — struktura se změnila)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # starý singulární tvar — nyní content_filter_results (množné číslo) uvnitř pole content_filters

# Surová HTTP volání na endpoint Chat Completions (nutno aktualizovat URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristika (detekce a přepis)

- **Klient Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Konstruktory klienta Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Nástroje**: převést definice nástrojů pro volání funkcí z vnořeného formátu (`{"type": "function", "function": {"name": ...}}`) na plochý formát Responses (`{"type": "function", "name": ...}`); použít `tool_choice`; vracet výsledky nástrojů jako položky `{"type": "function_call_output", "call_id": ..., "output": ...}` (nikoli `{"role": "tool", ...}`).
- **Návrat nástrojů**: když model vrací volání funkcí, připojit položky `response.output` do konverzace (nikoli ručně `{"role": "assistant", "tool_calls": [...]}` slovník), poté připojit položky `function_call_output` pro každý výsledek.
- **Příklady nástrojů s několika pokusy**: pokud konverzace obsahuje pevně zakódované příklady volání nástrojů, převést je na položky `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID musí začínat `fc_`.
- **`pydantic_function_tool()`**: tento pomocný nástroj stále generuje starý vnořený formát a **není kompatibilní** s `responses.create()`. Nahraďte ručními definicemi nástrojů nebo obalem pro zploštění.
- **Více kol**: uchovávat historii konverzace v aplikaci; předávat předchozí kola přes položky `input`.
- **Formátování**: nahradit vrcholové `response_format` v Chatu objektem `text.format` v Responses. Kanonický tvar: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Položky obsahu**: nahradit Chat `content[].type: "text"` položkami Responses `content[].type: "input_text"` pro tahy uživatele/systému.
- **Položky obrazového obsahu**: nahradit Chat `content[].type: "image_url"` položkami Responses `content[].type: "input_image"`. Pole `image_url` se mění z vnořeného objektu `{"url": "..."}` na plochý řetězec. Viz cheat sheet pro příklady před/po.
- **Úsilí o odůvodnění**: **migrujte `reasoning` pouze pokud již existuje v původním kódu**.
- **Zpracování chyb filtru obsahu**: struktura chybového těla se změnila. Chat Completions používal `error.body["innererror"]["content_filter_result"]` (singulár); Responses API používá `error.body["content_filters"][0]["content_filter_results"]` (plurál, uvnitř pole). Kód přistupující k `innererror` vyvolá `KeyError`. Přepište na použití nové cesty.
- **Surová HTTP volání**: pokud aplikace volá přímo Azure OpenAI REST API (pomocí `requests`, `httpx` atd.) přes `/openai/deployments/{name}/chat/completions?api-version=...`, přepište na `/openai/v1/responses`. Tělo požadavku se mění: `messages` → `input`, přidat `max_output_tokens` a `store: false`, odstranit query parametr `api-version`. Tělo odpovědi se mění: `choices[0].message.content` → `output[0].content[0].text` (pozn.: `output_text` je vlastnost SDK pro jednodušší přístup, není přítomna v syrovém REST JSON).

---

## Krok 2: Použití migrace

### Poznámky k migraci (Chat Completions → Responses)

- **Proč migrovat**: Responses je sjednocené API pro text, nástroje a streamování; Chat Completions je zastaralé. S GPT-5 je Responses požadováno pro nejlepší výkon.
- **HTTP**: Azure endpoint se přepíná z `/openai/deployments/{name}/chat/completions` na `/openai/v1/responses`.
- **Pole**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` zůstává.
- **Formátování**: `response_format` → `text.format` s vhodným objektem.
- **Položky obsahu**: nahradit Chat `content[].type: "text"` položkami Responses `content[].type: "input_text"` pro tahy systému/uživatele.
- **Položky obrazového obsahu**: nahradit Chat `content[].type: "image_url"` položkami Responses `content[].type: "input_image"`. Zploštit pole `image_url` z `{"image_url": {"url": "..."}}` na `{"image_url": "..."}` (prostý řetězec — HTTPS URL nebo `data:image/...;base64,...` data URI).

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
| `seed` | **Odstranit** (není podporováno) |
| `store` | `store` (nastaveno na `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (plochý řetězec) |

Kompletní příklady kódu před a po najdete v [cheat-sheet.md](./references/cheat-sheet.md).

Pro migraci testovací infrastruktury (mocks, snapshots, assertions) viz [test-migration.md](./references/test-migration.md).

Pro řešení problémů a často se vyskytující chyby viz [troubleshooting.md](./references/troubleshooting.md).

---

## Uchovávání dat & stav

- Nastavte `store: false` u všech požadavků Responses.
- Nespoléhejte se na předchozí ID zpráv nebo kontext uložený na serveru; stavební stav spravujte na klientovi a minimalizujte metadata.

---

## Akceptační kritéria

### Kódové kontroly (všechny musí projít)

- [ ] Žádné shody pro `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` v migrovaných souborech.
- [ ] Žádné shody pro `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — všechny konstruktory používají `OpenAI`/`AsyncOpenAI` s v1 endpointem.
- [ ] Žádné shody pro `rg "models\.github\.ai|models\.inference\.ai\.azure"` — cesty kódu GitHub Models odstraněny.
- [ ] Žádné shody pro `rg "OpenAIChatCompletionClient"` — kód MAF 1.0.0+ používá `OpenAIChatClient` (který používá Responses API). U verzí před 1.0.0 přejděte na `agent-framework-openai>=1.0.0`.
- [ ] Všechny volání `ChatOpenAI(...)` obsahují `use_responses_api=True`.
- [ ] Žádné shody pro `rg "choices\[0\]"` — veškerý přístup k odpovědi používá `resp.output_text` nebo schéma výstupu Responses.
- [ ] Není žádný `response_format` na nejvyšší úrovni; veškerý strukturovaný výstup používá `text={"format": {...}}`.
- [ ] `openai>=1.108.1` a `azure-identity` v `requirements.txt` nebo `pyproject.toml`; závislosti přebudovány.
- [ ] Nastaveno `store=False` u každého volání `responses.create`.
- [ ] Žádná `api_version` při konstrukci klienta; `AZURE_OPENAI_API_VERSION` odstraněn z environmentálních souborů a infrastruktury.

### Kontroly testovací infrastruktury (všechny musí projít)

- [ ] Žádné shody pro `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Žádné shody pro `rg "_azure_ad_token_provider" tests/` — assertace aktualizovány tak, aby kontrolovaly `isinstance(client, AsyncOpenAI)` nebo `base_url`.
- [ ] Žádné shody pro `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specifické filtry odebrány.
- [ ] Mock fixtures používají `kwargs.get("input")` místo `kwargs.get("messages")`.
- [ ] Soubory snapshot/golden aktualizovány na tvar streamování Responses (bez `choices[0]`, `function_call`, `logprobs` atd.).
- [ ] `pytest` projde bez chyb po všech aktualizacích testů.

### Chování (ověřit ručně nebo pomocí test harness)

- [ ] **Základní dokončení**: ne-streamované `responses.create` vrací neprázdný `output_text`.
- [ ] **Parita streamu**: pokud původní kód používal streamování, migrovaný kód streamuje a vydává události `response.output_text.delta` s neprázdnými deltami.
- [ ] **Strukturovaný výstup**: pokud se používá `text.format` s `json_schema`, `json.loads(resp.output_text)` uspěje a odpovídá schématu.
- [ ] **Smyčka volání nástroje**: pokud jsou použity nástroje, model vydává volání nástroje, aplikace je spouští a následný požadavek vrací konečný `output_text` (bez nekonečné smyčky).
- [ ] **Async parita**: pokud byl použit `AsyncAzureOpenAI`, funguje ekvivalent `AsyncOpenAI` s `await`.
- [ ] **Míra chyb**: žádné nové chyby 400/401/404 oproti před-migračnímu základu.

### Výstupy

- Shrnutí obsahuje upravené soubory, počty před/po starých voláních a další kroky.
- Změny jsou pouze úpravy pracovního stromu (žádné commity).

---

## Požadavky na verze SDK

| Balíček | Minimální verze |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Nejnovější (pro EntraID autentizaci) |

---

## Reference

- [Cheat Sheet — všechny ukázky kódu](./references/cheat-sheet.md)
- [Test Migration — mocky, snapshoty, assertace](./references/test-migration.md)
- [Troubleshooting — chyby, tabulka rizik, nástrahy](./references/troubleshooting.md)
- [detect_legacy.py — automatizovaný skener](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API docs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Životní cyklus verze Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->