---
name: azure-openai-to-responses
license: MIT
---
# Migrácia Python aplikácií z Azure OpenAI Chat Completions na Responses API

> **AUTORITATÍVNE USMERNENIE — POSTUPUJTE PRESNE**
>
> Tento skill migruje Python kódy používajúce Azure OpenAI Chat Completions
> na jednotné Responses API. Dodržiavajte tieto inštrukcie presne.
> Neimprovizujte mapovanie parametrov ani nevymýšľajte nové tvary API.

---

## Spúšťače

Aktivujte tento skill, keď používateľ chce:
- Migrovať Python aplikáciu z Azure OpenAI Chat Completions na Responses API
- Aktualizovať použitie Python OpenAI SDK na najnovší tvar API proti Azure OpenAI
- Pripraviť Python kód pre GPT-5 alebo novšie modely, ktoré vyžadujú Responses na Azure
- Prejsť z `AzureOpenAI`/`AsyncAzureOpenAI` na štandardný `OpenAI`/`AsyncOpenAI` klient s v1 endpointom
- Opraviť upozornenia na zastaranie týkajúce sa konštruktorov `AzureOpenAI` alebo `api_version`

---

## ⚠️ Kompatibilita modelu — SKONTROLUJTE NAJVPRV

> **Pred migráciou overte, či vaše Azure OpenAI nasadenie podporuje Responses API.**

### 1. Rýchly test nasadenia (najrýchlejší)

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

> **Poznámka**: `max_output_tokens` má na Azure OpenAI **minimálnu hodnotu 16**. Hodnoty pod 16 vrátia chybu 400. Pre rýchle testy použite hodnotu 50 a viac.

Ak to vráti 404, model nasadenia ešte nepodporuje Responses — pozrite referenciu nižšie alebo znovu nasadte podporovaný model.

### 2. Skontrolujte dostupné modely vo vašom regióne (odporúčané)

Spustite vstavaný nástroj pre kompatibilitu modelov, aby ste videli, čo je dostupné s podporou Responses API vo vašom regióne:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Táto požiadavka oslovuje Azure ARM v reálnom čase a zobrazí maticu kompatibility — ktoré modely podporujú Responses, štruktúrovaný výstup, nástroje atď. Použite `--filter gpt-5.1,gpt-5.2` pre zúženie výsledkov alebo `--json` pre skriptovanie.

### 3. Kompletná referencia podpory modelov

- **Live dotaz**: `python migrate.py models` (viď vyššie — špecifické pre región, vždy aktuálne)
- **Prehliadanie dostupnosti**: [Prehľadová tabuľka modelov a dostupnosť v regiónoch](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Rýchly štart & usmernenia**: **https://aka.ms/openai/start**

### ⚠️ Obmedzenia starších modelov

> **UPOZORNENIE**: Staršie modely (pred `gpt-4.1`) nemusia plne podporovať všetky funkcie Responses API.
>
> Známé obmedzenia u starších modelov:
> - **parameter `reasoning`**: Nie je podporovaný na mnohých modeloch bez reasoning. Migrujte `reasoning` iba ak bol už prítomný v pôvodnom kóde.
> - **parameter `seed`**: V Responses API vôbec nie je podporovaný — odstráňte zo všetkých požiadaviek.
> - **Štruktúrovaný výstup pomocou `text.format`**: Staršie modely nemusia spoľahlivo vynucovať JSON schémy s `strict: true`.
> - **Orchestrace nástrojov**: GPT-5+ orchestruje volania nástrojov ako súčasť vnútorného reasoning. Staršie modely na Responses stále fungujú, ale bez tejto hlbokej integrácie.
> - **Obmedzenia teploty**: Pri migrácii na `gpt-5` musí byť teplota vynechaná alebo nastavená na `1`. Staršie modely takéto obmedzenie nemajú.

### O-series reasoning modely (o1, o3-mini, o3, o4-mini)

Modely O-series majú jedinečné parametrové obmedzenia. Pri migrácii aplikácií cieľujúcich O-series modely:

- **`temperature`**: Musí byť `1` (alebo vynechané). O-series modely neprijímajú iné hodnoty.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikácie používajúce Azure špecifické `max_completion_tokens` musia prejsť na `max_output_tokens`. Nastavte vysoké hodnoty (4096+), lebo tokeny reasoning sa ráta k limitu.
- **`reasoning_effort`**: Ak aplikácia využíva `reasoning_effort` (low/medium/high), zachovajte ho — Responses API tento parameter podporuje pre O-series modely.
- **Streaming správanie**: O-series modely môžu bufferovať výstup až do ukončenia reasoning pred emitovaním textových delta udalostí. Streaming stále funguje, ale prvý `response.output_text.delta` môže prísť s väčším oneskorením než u GPT modelov.
- **`top_p`**: Nie je podporované na O-series — odstráňte ak sa vyskytuje.
- **Použitie nástrojov**: O-series modely podporujú nástroje cez Responses API rovnako ako GPT modely, ale kvalita orchestrace volaní nástrojov závisí od modelu.

**Akcia — proaktívne upozornenie na model**: Počas fázy skenovania skontrolujte, na ktorý model appka cieli (mená deploymentov, env premenne, konfigurácia). Ak model predchádza `gpt-4.1` (nie gpt-4.1+), proaktívne upozornite používateľa:
- Migrácia bude fungovať pre základný text, chat, streaming a nástroje na ich aktuálnom modeli.
- Novšie modely (`gpt-5.1`, `gpt-5.2`) ponúkajú lepšiu orchestrace nástrojov, vynucovanie štruktúrovaného výstupu, reasoning a dostupnosť v rôznych regiónoch.
- Mali by zvážiť upgrade nasadenia, keď budú pripravení — migráciu to neblokuje.

Neblokujte ani neodmietajte migráciu na základe verzie modelu. Upozornenie má informatívny charakter.

### GitHub Models NEpodporujú Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) nepodporujú Responses API.**

Ak má kódová báza cestu pre GitHub Models (hľadajte `base_url` ukazujúci na `models.github.ai` alebo `models.inference.ai.azure.com`), **odstráňte ju úplne** počas migrácie. Responses API vyžaduje Azure OpenAI, OpenAI alebo kompatibilný lokálny endpoint (napr. Ollama s podporou Responses).

Akcia počas skenu:
- Označte všetky cesty kódu GitHub Models na odstránenie.

---

## Migrácia frameworku

Mnoho aplikácií používa vyššie úrovňové frameworky nad OpenAI. Pri ich migrácii sa mení API samotného frameworku — nie len podkladové OpenAI volania.

### Microsoft Agent Framework (MAF)

**Najskôr skontrolujte vašu verziu MAF** — migrácia závisí od toho, či máte MAF 1.0.0+ alebo predbežnú beta/rc verziu pred 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **už používa Responses API** — migrácia nie je potrebná. Ak kód používa starý `OpenAIChatCompletionClient` (používajúci `chat.completions.create`), nahraďte ho `OpenAIChatClient`.

| Predtým | Po migrácii |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Pre kontrolu verzie použite: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pred 1.0.0 (beta/rc verzie)

V predbežných verziách MAF `OpenAIChatClient` používal Chat Completions. Upgradujte na `agent-framework-openai>=1.0.0`, kde `OpenAIChatClient` štandardne používa Responses API.

Iné zmeny nie sú potrebné — API `Agent` a nástrojov zostáva rovnaké.

### LangChain (`langchain-openai`)

Pridajte `use_responses_api=True` k `ChatOpenAI()`. Tiež upravte prístup k odpovedi z `.content` na `.text`.

| Predtým | Po migrácii |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Kompletné príklady kódov pred a po nájdete v [cheat-sheet.md](./references/cheat-sheet.md).

---

## Usmernenie pre migráciu frontendu

> **Responses API je záležitosť serverovej strany.** Migrujte back-end Pythonu; HTTP rozhranie frontendu by malo ostať nezmenené, pokiaľ váš backend nie je tenká priepustka — v tom prípade zvážte použitie tvaru Requests Responses API aby ste eliminovali vrstvu prekladu. Ak frontend volá OpenAI priamo s kľúčom klienta, presuňte tieto volania najskôr na backend.

### Deprecácia `@microsoft/ai-chat-protocol`

Npm balíček `@microsoft/ai-chat-protocol` je zastaraný a mal by byť nahradený [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Ak ho nájdete vo fronte:

1. Nahraďte CDN script tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Odstráňte inštanciu `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Nahraďte `client.getStreamedCompletion(messages)` priamym volaním `fetch()` na backend streaming endpoint.
4. Nahraďte `for await (const response of result)` s `for await (const chunk of readNDJSONStream(response.body))`.
5. Aktualizujte prístup k vlastnostiam z `response.delta.content` / `response.error` na `chunk.delta.content` / `chunk.error`.

---

## Ciele

- Vyhľadať všetky Python volania používajúce Chat Completions alebo staré Completions proti Azure OpenAI.
- Navrhnúť plán migrácie a poradové usporiadanie pre Python kód.
- Aplikovať bezpečné, minimálne úpravy pre prechod na Responses API.
- Aktualizovať volajúce strany na používanie výstupnej schémy Responses; žiadne spätné kompatibilné obaly.
- Spustiť testy/linty; opraviť triviálne chyby spôsobené migráciou.
- Pripraviť malé, prehľadné zmeny a poskytnúť konečné zhrnutie s diffmi (nezapracovávať do verziovacieho systému).

---

## Bezpečnostné opatrenia

- Upravujte iba súbory nachádzajúce sa vo vašom git workspace. Nikdy mimo.
- Nemožno zachovávať spätné kompatibilné shimy; migrujte kód na nový tvar API.
- Nezanechávajte komentáre prechodovej fázy alebo záložné súbory.
- Zachovajte streaming správanie, ak bolo predtým použité; inak používajte ne-streaming.
- Pri režime s požiadavkou schválenia žiadajte o potvrdenie pred spustením príkazov alebo sieťových volaní.
- Nespúšťajte `git add`/`git commit`/`git push`; produkujte iba úpravy pracovného stromu.

---

## Krok 0: Migrácia Azure OpenAI klienta (predpoklad)

Ak kód používa konštruktory `AzureOpenAI` alebo `AsyncAzureOpenAI`, najskôr migrujte na štandardné konštruktory `OpenAI` / `AsyncOpenAI`. Azure špecifické konštruktory sú zastarané v `openai>=1.108.1`.

### Prečo v1 API cesta?

Nový endpoint `/openai/v1` používa štandardný klient `OpenAI()` namiesto `AzureOpenAI()`, nevyžaduje parameter `api_version` a funguje rovnako na OpenAI aj Azure OpenAI. Rovnaký klientovací kód je budúcnosti odolný — nie je potrebná žiadna správa verzií.

### Kľúčové zmeny

| Predtým | Po migrácii |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Odstrániť úplne |

### Kontrolný zoznam upratovania

- Odstráňte argument `api_version` z konštrukcie klienta.
- Odstráňte environmentálne premenné `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` zo `.env`, nastavení app a Bicep/infra súborov.
- Premenujte `AZURE_OPENAI_CLIENT_ID` na `AZURE_CLIENT_ID` v `.env`, nastaveniach app, Bicep/infra a testovacích fixtures (štandardná konvencia Azure Identity SDK).
- Zabezpečte `openai>=1.108.1` v `requirements.txt` alebo `pyproject.toml`.

### Migrácia environmentálnych premenných

| Staré env var | Akcia | Poznámky |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Odstrániť** | Pri v1 endpoint sa `api_version` nevyžaduje |
| `AZURE_OPENAI_API_VERSION` | **Odstrániť** | Rovnako ako vyššie |
| `AZURE_OPENAI_CLIENT_ID` | **Premenovať** → `AZURE_CLIENT_ID` | Štandardná konvencia Azure Identity SDK pre `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Zachovať** | Stále potrebné pre konštrukciu `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Zachovať** | Používa sa ako `model` parameter v `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Zachovať** | Používa sa ako `api_key` pre autentifikáciu kľúčom |

Pre príklady nastavenia klienta (sync, async, EntraID, API kľúč, multi-tenant) pozrite [cheat-sheet.md](./references/cheat-sheet.md).

---

## Krok 1: Detekcia starých volaní

Spustite skript [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) na nájdenie všetkých volaní, ktoré je potrebné migrovať:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Alebo spustite tieto vyhľadávania manuálne — každý nájdený zápas je cieľom migrácie:

```bash
# Volania zastaralého API (treba prepísať)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Zastaralé konštruktory Azure klientov (treba nahradiť)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Vzory prístupu k štruktúre odpovede (treba aktualizovať)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definície nástrojov v starej vnorené forme (treba zjednotiť)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Výsledky nástrojov v starom formáte (treba previesť na function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Zastaralé parametre (treba odstrániť alebo premenovať)
rg "response_format"
rg "max_tokens\b"        # premenovať na max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Zastaralé premenné prostredia (upratať)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # malo by byť AZURE_CLIENT_ID

# GitHub Models endpointy (treba odstrániť — API odpovedí nie je podporované)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Vzory úrovne frameworku (treba aktualizovať)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: nahradiť OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: potrebuje use_responses_api=True

# Testovacia infraštruktúra (treba aktualizovať)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Prístup k telu chyby filtrov obsahu (treba aktualizovať — štruktúra sa zmenila)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # stará jednotná forma — teraz content_filter_results (množné číslo) vo vnútri poľa content_filters

# Surové HTTP volania na endpoint Chat Completions (treba aktualizovať URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristiky (detekcia a prepísanie)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Konstruktory Azure klientov**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Nástroje**: konvertujte definície nástrojov na volanie funkcií z vnoreného formátu (`{"type": "function", "function": {"name": ...}}`) do plochého formátu Responses (`{"type": "function", "name": ...}`); používajte `tool_choice`; vracajte výsledky nástrojov ako položky `{"type": "function_call_output", "call_id": ..., "output": ...}` (nie `{"role": "tool", ...}`).
- **Obojsmerné volania nástrojov**: keď model vracia volania funkcií, pridajte položky `response.output` do konverzácie (nie manuálny slovník `{"role": "assistant", "tool_calls": [...]}`), potom pridajte položky `function_call_output` pre každý výsledok.
- **Príklady nástrojov s niekoľkými príkladmi**: ak konverzácia obsahuje hardcoded príklady volaní nástrojov, konvertujte ich na položky `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID musia začínať s `fc_`.
- **`pydantic_function_tool()`**: tento pomocný nástroj stále generuje starý vnorený formát a **nie je kompatibilný** s `responses.create()`. Nahraďte manuálnymi definíciami nástrojov alebo wrapperom na zploštenie.
- **Viacnásobné kolá**: uchovávajte históriu konverzácie v aplikácii; predchádzajúce kolá posielajte cez položky `input`.
- **Formátovanie**: nahraďte vrcholový `response_format` v Chate za `text.format` v Responses. Kanonický tvar: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Položky obsahu**: nahraďte v Chate `content[].type: "text"` za v Responses `content[].type: "input_text"` pre užívateľské/systémové kolá.
- **Položky obsahu obrázkov**: nahraďte v Chate `content[].type: "image_url"` za v Responses `content[].type: "input_image"`. Pole `image_url` sa mení z vnoreného objektu `{"url": "..."}` na plochý reťazec. Pozrite prehľadový list pre príklady pred/po.
- **Úsilie o odôvodnenie**: **migrujte `reasoning` len ak už existuje v pôvodnom kóde**.
- **Spracovanie chýb filtra obsahu**: štruktúra tela chyby sa zmenila. Chat Completions používal `error.body["innererror"]["content_filter_result"]` (jednotné číslo); Responses API používa `error.body["content_filters"][0]["content_filter_results"]` (množné, v poli). Kód pristupujúci k `innererror` vyvolá `KeyError`. Prepracujte na nový cestu.
- **Priame HTTP volania**: ak aplikácia volá Azure OpenAI REST API priamo (cez `requests`, `httpx` atď.) pomocou `/openai/deployments/{name}/chat/completions?api-version=...`, prepíšte na `/openai/v1/responses`. Telo požiadavky sa mení: `messages` → `input`, pridajte `max_output_tokens` a `store: false`, odstráňte query parameter `api-version`. Telo odpovede sa mení: `choices[0].message.content` → `output[0].content[0].text` (poznámka: `output_text` je pohodlná vlastnosť SDK, nie je prítomná v surovom REST JSON).

---

## Krok 2: Aplikujte migráciu

### Poznámky k migrácii (Chat Completions → Responses)

- **Prečo migrovať**: Responses je jednotné API pre text, nástroje a streamovanie; Chat Completions je zastarané. S GPT-5 je Responses nutné pre najlepšie výkony.
- **HTTP**: Azure endpoint sa prepína z `/openai/deployments/{name}/chat/completions` na `/openai/v1/responses`.
- **Polia**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` zostáva rovnaké.
- **Formátovanie**: `response_format` → `text.format` so správnym objektom.
- **Položky obsahu**: Nahraďte v Chate `content[].type: "text"` za v Responses `content[].type: "input_text"` pre systémové/užívateľské kolá.
- **Položky obsahu obrázkov**: Nahraďte v Chate `content[].type: "image_url"` za v Responses `content[].type: "input_image"`. Zplošťte pole `image_url` z `{"image_url": {"url": "..."}}` na `{"image_url": "..."}` (čistý reťazec — buď HTTPS URL alebo `data:image/...;base64,...` data URI).

### Referencia mapovania parametrov

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (pole položiek) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (nezmenené) |
| `stop` | `stop` (nezmenené) |
| `frequency_penalty` | `frequency_penalty` (nezmenené) |
| `presence_penalty` | `presence_penalty` (nezmenené) |
| `tools` / volanie funkcií | `tools` (nezmenené) |
| `seed` | **Odstrániť** (není podporované) |
| `store` | `store` (nastavené na `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (plochý reťazec) |

Pre kompletné príklady kódu pred/po pozrite [cheat-sheet.md](./references/cheat-sheet.md).

Pre migráciu testovacej infraštruktúry (mocks, snapshots, assertions) pozrite [test-migration.md](./references/test-migration.md).

Pre riešenie problémov a úskalia pozrite [troubleshooting.md](./references/troubleshooting.md).

---

## Uchovávanie dát a stav

- Nastavte `store: false` na všetkých požiadavkách Responses.
- Nespoliehajte sa na predchádzajúce ID správ alebo serverom uložený kontext; stav udržiavajte klientsky a minimalizujte metadata.

---

## Akceptačné kritériá

### Brány na úrovni kódu (všetky musia prejsť)

- [ ] Nulové zhody pre `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` v migrovaných súboroch.
- [ ] Nulové zhody pre `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — všetky konstruktory používajú `OpenAI`/`AsyncOpenAI` s v1 endpointom.
- [ ] Nulové zhody pre `rg "models\.github\.ai|models\.inference\.ai\.azure"` — odstránené cesty kódu GitHub modelov.
- [ ] Nulové zhody pre `rg "OpenAIChatCompletionClient"` — kód MAF 1.0.0+ používa `OpenAIChatClient` (ktorý používa Responses API). V pred 1.0.0 upgradujte na `agent-framework-openai>=1.0.0`.
- [ ] Všetky volania `ChatOpenAI(...)` obsahujú `use_responses_api=True`.
- [ ] Nulové zhody pre `rg "choices\[0\]"` — všetky prístupy k odpovediam používajú `resp.output_text` alebo schému výstupu Responses.
- [ ] Žiadne `response_format` na vrcholovej úrovni; všetok štruktúrovaný výstup používa `text={"format": {...}}`.
- [ ] `openai>=1.108.1` a `azure-identity` v `requirements.txt` alebo `pyproject.toml`; závislosti znovu nainštalované.
- [ ] `store=False` nastavené na každom volaní `responses.create`.
- [ ] Žiadne `api_version` v konštrukcii klienta; `AZURE_OPENAI_API_VERSION` odstránený z env súborov a infraštruktúry.

### Brány testovacej infraštruktúry (všetky musia prejsť)

- [ ] Nulové zhody pre `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Nulové zhody pre `rg "_azure_ad_token_provider" tests/` — assertion aktualizované na kontrolu `isinstance(client, AsyncOpenAI)` alebo `base_url`.
- [ ] Nulové zhody pre `rg "prompt_filter_results|content_filter_results" tests/` — odstránené Azure-špecifické filtre mocky.
- [ ] Mock fixtures používajú `kwargs.get("input")`, nie `kwargs.get("messages")`.
- [ ] Snapshoty / golden súbory aktualizované na tvar Responses streamovania (bez `choices[0]`, `function_call`, `logprobs` atď.).
- [ ] `pytest` prebehne bez zlyhaní po všetkých aktualizáciách testov.

### Brány správania (overiť manuálne alebo cez testovací harness)

- [ ] **Základné dokončenie**: ne-streamované `responses.create` vracia neprázdny `output_text`.
- [ ] **Rovnosť streamu**: ak pôvodný kód používal streamovanie, migrovaný kód streamuje a vydáva udalosti `response.output_text.delta` s neprázdnymi deltas.
- [ ] **Štruktúrovaný výstup**: ak sa používa `text.format` s `json_schema`, `json.loads(resp.output_text)` prejde a zodpovedá schéme.
- [ ] **Smyčka volania nástrojov**: ak sa používajú nástroje, model vydáva volania nástrojov, aplikácia ich vykoná a následná požiadavka vracia finálny `output_text` (bez nekonečnej slučky).
- [ ] **Asynchrónna rovnosť**: ak sa používal `AsyncAzureOpenAI`, ekvivalent `AsyncOpenAI` funguje s `await`.
- [ ] **Miera chýb**: žiadne nové chyby 400/401/404 oproti baseline pred migráciou.

### Výstupy

- Súhrn zahŕňa upravené súbory, počet starých volaní pred/po a ďalšie kroky.
- Zmeny sú iba vo working tree (žiadne commity).

---

## Požiadavky na verziu SDK

| Balík | Minimálna verzia |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Najnovšia (pre EntraID autentifikáciu) |

---

## Referencie

- [Cheat Sheet — všetky ukážky kódu](./references/cheat-sheet.md)
- [Migrácia testov — mocky, snapshoty, assertions](./references/test-migration.md)
- [Riešenie problémov — chyby, tabuľka rizík, úskalia](./references/troubleshooting.md)
- [detect_legacy.py — automatický skener](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API docs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Lifecycle verzií Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Referenčný manuál OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->