---
name: azure-openai-to-responses
license: MIT
---
# Migrácia Python aplikácií z Azure OpenAI Chat Completions na Responses API

> **AUTORITATÍVNE POKYNY — PRESNE DODRŽIAVAJTE**
>
> Táto schopnosť migruje Python kódy používajúce Azure OpenAI Chat Completions
> na jednotné Responses API. Presne dodržiavajte tieto pokyny.
> Nepoužívajte improvizované mapovania parametrov ani nevymýšľajte tvary API.

---

## Spúšťače

Aktivujte túto schopnosť, keď používateľ chce:
- Migrovať Python aplikáciu z Azure OpenAI Chat Completions na Responses API
- Aktualizovať použitie Python OpenAI SDK na najnovší tvar API pre Azure OpenAI
- Pripraviť Python kód pre modely GPT-5 alebo novšie, ktoré vyžadujú Responses na Azure
- Prejsť z `AzureOpenAI`/`AsyncAzureOpenAI` na štandardného klienta `OpenAI`/`AsyncOpenAI` s koncovým bodom v1
- Opraviť varovania o zastaraní súvisiace s konštruktormi `AzureOpenAI` alebo `api_version`

---

## ⚠️ Kompatibilita modelov — NAJPRV SKONTROLUJTE

> **Pred migráciou si overte, či vaša Azure OpenAI nasadenie podporuje Responses API.**

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

> **Poznámka**: `max_output_tokens` má na Azure OpenAI **minimum 16**. Hodnoty pod 16 vracajú chybu 400. Použite 50+ pre rýchle testy.

Ak toto vráti 404, model v nasadení zatiaľ Responses nepodporuje — pozrite si referenciu nižšie alebo znovu nasadte podporovaný model.

### 2. Skontrolujte dostupné modely vo vašom regióne (odporúčané)

Spustite vstavaný nástroj kompatibility modelov, aby ste videli, aké modely s podporou Responses API sú dostupné vo vašom regióne:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Toto robí live dotaz na Azure ARM a zobrazuje maticu kompatibility — ktoré modely podporujú Responses, štruktúrovaný výstup, nástroje atď. Použite `--filter gpt-5.1,gpt-5.2` na zúženie výsledkov alebo `--json` pre skriptovanie.

### 3. Kompletná referencia podpory modelov

- **Live dotaz**: `python migrate.py models` (viď vyššie — špecifické pre región, vždy aktuálne)
- **Prehľad dostupnosti**: [Tabuľka súhrnu modelov a dostupnosť v regiónoch](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Rýchly štart a pokyny**: **https://aka.ms/openai/start**

### ⚠️ Obmedzenia starších modelov

> **UPOZORNENIE**: Staršie modely (napr. `gpt-4o`, `gpt-4`) nemusia úplne podporovať všetky funkcie Responses API.
>
> Známne obmedzenia starších modelov:
> - **Parameter `reasoning`**: Nie je podporovaný na `gpt-4o-mini`, `gpt-4o` a mnohých modeloch bez reasoningu. Migrujte parameter `reasoning` iba ak už bol v pôvodnom kóde.
> - **Parameter `seed`**: V Responses API vôbec nepodporovaný — odstráňte zo všetkých požiadaviek.
> - **Štruktúrovaný výstup cez `text.format`**: Staršie modely nemusia spoľahlivo vynucovať JSON schémy s `strict: true`.
> - **Orchestrace nástrojov**: GPT-5+ orchestruje volania nástrojov ako súčasť vnútorného reasoning. Staršie modely na Responses stále fungujú, ale bez tejto hlbokej integrácie.
> - **Obmedzenia teploty**: Pri migrácii na `gpt-5` musí byť parameter teploty vynechaný alebo nastavený na `1`. Staršie modely takéto obmedzenie nemajú.

### Modely o-série reasoning (o1, o3-mini, o3, o4-mini)

Modely o-série majú unikátne obmedzenia parametrov. Pri migrácii aplikácií cieľujúcich tieto modely:

- **`temperature`**: Musí byť `1` (alebo vynechané). Modely o-série neakceptujú iné hodnoty.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikácie používajúce Azure špecifický `max_completion_tokens` musia prejsť na `max_output_tokens`. Nastavte vysoké hodnoty (4096+) lebo tokeny reasoning sa počítajú proti limitu.
- **`reasoning_effort`**: Ak aplikácia používa `reasoning_effort` (nízke/stredné/vysoké), zachovajte ho — Responses API tento parameter pre o-sériu podporuje.
- **Správanie streamingu**: Modely o-série môžu bufferovať výstup, kým reasoning neskončí, pred emitovaním delta udalostí textu. Streaming stále funguje, ale prvý `response.output_text.delta` môže prísť s oneskorením oproti GPT modelom.
- **`top_p`**: Nie je podporovaný na o-sérii — odstráňte ak je prítomný.
- **Používanie nástrojov**: Modely o-série podporujú nástroje cez Responses API rovnako ako GPT modely, ale kvalita orchestrace volaní nástrojov sa líši podľa modelu.

**Akcia — proaktívne upozornenie na model**: Počas fázy skenovania skontrolujte, na ktorý model aplikácia cieli (názvy deploymentov, env premenné, konfigurácia). Ak je to model `gpt-4o` alebo starší (nie gpt-4.1+), upozornite používateľa:
- Migrácia bude fungovať pre základný text, chat, streaming a nástroje na jeho súčasnom modeli.
- Novšie modely (`gpt-5.1`, `gpt-5.2`) ponúkajú lepšiu orchestráciu nástrojov, vynucovanie štruktúrovaného výstupu, reasoning a dostupnosť cez regióny.
- Mali by zvážiť aktualizáciu nasadenia, keď budú pripravení — nie je to blokujúce pre migráciu.

Nemanipulujte ani neblokujte migráciu kvôli verzii modelu. Toto upozornenie má informatívny charakter.

### GitHub Models nepodporujú Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) nepodporujú Responses API.**

Ak má kódová báza cestu GitHub Models (hľadajte `base_url` ukazujúci na `models.github.ai` alebo `models.inference.ai.azure.com`), **odstráňte ju úplne** počas migrácie. Responses API vyžaduje Azure OpenAI, OpenAI alebo kompatibilný lokálny endpoint (napr. Ollama s podporou Responses).

Akcia počas skenovania:
- Označiť všetky cesty kódu GitHub Models na odstránenie.

---

## Migrácia frameworku

Mnohé aplikácie používajú vyššie vrstvy frameworkov nad OpenAI. Pri ich migrácii sa menia API týchto frameworkov — nielen základné OpenAI volania.

### Microsoft Agent Framework (MAF)

**Najprv skontrolujte svoju verziu MAF** — migrácia závisí od toho, či máte MAF 1.0.0+ alebo pred-bežnú verziu beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **už používa Responses API** — migrácia nie je potrebná. Ak kód používa legacy `OpenAIChatCompletionClient` (ktorý používa `chat.completions.create`), nahraďte ho `OpenAIChatClient`.

| Pred | Po |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Na zistenie verzie použite: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pred 1.0.0 (beta/rc verzie)

V predbežných verziách MAF `OpenAIChatClient` používal Chat Completions. Aktualizujte na `agent-framework-openai>=1.0.0`, kde `OpenAIChatClient` štandardne používa Responses API.

Žiadne ďalšie zmeny nie sú potrebné — `Agent` a API pre nástroje zostávajú nezmenené.

### LangChain (`langchain-openai`)

Pridajte `use_responses_api=True` do `ChatOpenAI()`. Tiež aktualizujte prístup k odpovedi z `.content` na `.text`.

| Pred | Po |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Pre kompletné príklady kódu pred/po pozrite [cheat-sheet.md](./references/cheat-sheet.md).

---

## Pokyny na migráciu frontendu

> **Responses API je záležitosť serverovej strany.** Migrujte svoj Python backend; HTTP kontrakt frontendu by mal zostať nezmenený, pokiaľ váš backend nie je iba tenkou vrstvou — v tom prípade zvážte použitie tvaru žiadosti Responses API a odstránenie prekladovej vrstvy. Ak frontend volá OpenAI priamo s klientským kľúčom, presuňte tieto volania najskôr na backend.

### Deprecácia `@microsoft/ai-chat-protocol`

NPM balík `@microsoft/ai-chat-protocol` je zastaraný a mal by byť nahradený [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Ak ho nájdete vo fronte:

1. Nahraďte CDN skriptový tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Odstráňte inštanciu `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Nahraďte `client.getStreamedCompletion(messages)` priamym volaním `fetch()` na backend streaming endpoint.
4. Nahraďte `for await (const response of result)` za `for await (const chunk of readNDJSONStream(response.body))`.
5. Aktualizujte prístup k vlastnostiam z `response.delta.content` / `response.error` na `chunk.delta.content` / `chunk.error`.

---

## Ciele

- Vypísať všetky Python volania používajúce Chat Completions alebo legacy Completions proti Azure OpenAI.
- Navrhnúť plán a poradie migrácie pre Python kód.
- Použiť bezpečné, minimálne úpravy na prechod na Responses API.
- Aktualizovať volania, aby spotrebovali schému výstupu Responses; bez spätnoväzbových wrapperov.
- Spustiť testy/linty; opraviť drobné porušenia spôsobené migráciou.
- Pripraviť malé, prehliadnuteľné zmeny a poskytnúť záverečný súhrn so zmenami (nevykonávať commit).

---

## Zásady

- Upraviť len súbory v git pracovnom priestore. Nikdy mimo neho.
- Nezachovávať spätnoväzbové shim-y; migrovať kód na nový tvar API.
- Nezanechávať poznámky o prechode ani záložné súbory.
- Zachovať streaming semantiku, ak bola predtým použitá; inak použiť ne-streaming.
- Požiadať o schválenie pred spustením príkazov alebo sieťových volaní, ak je režim schválenia.
- Nespúšťať `git add`/`git commit`/`git push`; robiť len úpravy pracovného stromu.

---

## Krok 0: Migrácia Azure OpenAI Klienta (predpoklad)

Ak kód používa konštruktory `AzureOpenAI` alebo `AsyncAzureOpenAI`, najprv migrujte na štandardné konštruktory `OpenAI` / `AsyncOpenAI`. Azure-špecifické konštruktory sú zastarané v `openai>=1.108.1`.

### Prečo API cesta v1?

Nový koncový bod `/openai/v1` používa štandardného klienta `OpenAI()` namiesto `AzureOpenAI()`, nevyžaduje parameter `api_version` a funguje rovnako pre OpenAI aj Azure OpenAI. Rovnaký kód klienta je budúcnosti odolný — nie je potrebná správa verzií.

### Kľúčové zmeny

| Pred | Po |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Odstrániť úplne |

### Kontrolný zoznam čistenia

- Odstrániť argument `api_version` z konštrukcie klienta.
- Odstrániť premenné prostredia `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` z `.env`, nastavení aplikácie a Bicep/infrastruktúrnych súborov.
- Premenovať `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` v `.env`, nastaveniach aplikácie, Bicep/infrastruktúre a testovacích fixutrách (štandardná konvencia Azure Identity SDK).
- Zaistiť `openai>=1.108.1` v `requirements.txt` alebo `pyproject.toml`.

### Migrácia premenných prostredia

| Stará env var | Akcia | Poznámky |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Odstrániť** | `api_version` nie je potrebný s v1 endpointom |
| `AZURE_OPENAI_API_VERSION` | **Odstrániť** | Rovnako ako vyššie |
| `AZURE_OPENAI_CLIENT_ID` | **Premenovať** → `AZURE_CLIENT_ID` | Štandardná konvencia Azure Identity SDK pre `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Ponechať** | Stále potrebné pre konštrukciu `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Ponechať** | Používa sa ako parameter `model` v `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Ponechať** | Používa sa ako `api_key` pre autentifikáciu pomocou kľúča |

Pre ukážky nastavenia klienta (sync, async, EntraID, API kľúč, multi-tenant), pozrite [cheat-sheet.md](./references/cheat-sheet.md).

---

## Krok 1: Detekcia legacy volaní

Spustite skript [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) pre nájdenie všetkých volaní, ktoré je potrebné migrovať:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Alebo tieto vyhľadávania vykonajte manuálne — každý nájdený výskyt je cieľom migrácie:

```bash
# Volania Legacy API (treba prepísať)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Zastarané konštruktory Azure klienta (treba nahradiť)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Prístupy ku tvarom odpovedí (treba aktualizovať)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definície nástrojov v starom vnorenom formáte (treba zjednotiť)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Výsledky nástrojov v starom formáte (treba previesť na function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Zastarané parametre (treba odstrániť alebo premenovať)
rg "response_format"
rg "max_tokens\b"        # premenovať na max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Zastarané premenné prostredia (treba vyčistiť)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # malo by byť AZURE_CLIENT_ID

# GitHub Models endpointy (treba odstrániť — Responses API nie je podporované)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Legacy vzory na úrovni frameworku (treba aktualizovať)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: nahradiť OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: potrebuje use_responses_api=True

# Testovacia infraštruktúra (treba aktualizovať)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Prístup k telu chyby filtrov obsahu (treba aktualizovať — štruktúra sa zmenila)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # starý jednotný tvar — teraz content_filter_results (množné číslo) v poli content_filters

# Surové HTTP volania na endpoint Chat Completions (treba aktualizovať URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristiky (detekcia a prepísanie)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure klientské konstruktory**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Nástroje**: previesť definície nástrojov na volanie funkcií z vnoreného formátu (`{"type": "function", "function": {"name": ...}}`) na plochý formát Responses (`{"type": "function", "name": ...}`); používať `tool_choice`; vrátiť výsledky nástrojov ako položky `{"type": "function_call_output", "call_id": ..., "output": ...}` (nie `{"role": "tool", ...}`).
- **Prechod nástrojov tam a späť**: keď model vráti volania funkcií, pripojiť položky `response.output` do konverzácie (nie manuálny slovník `{"role": "assistant", "tool_calls": [...]}`), následne pripojiť položky `function_call_output` pre každý výsledok.
- **Príklady nástrojov s málo vzorkami**: ak konverzácia obsahuje pevne zabudované príklady volaní nástrojov, previesť ich na položky `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID musia začínať na `fc_`.
- **`pydantic_function_tool()`**: tento pomocník stále generuje starý vnorený formát a **nie je kompatibilný** s `responses.create()`. Nahradiť manuálnymi definíciami nástrojov alebo obalom na zploštenie.
- **Viackolové**: uchovávať históriu konverzácie v aplikácii; odovzdávať predchádzajúce kolá cez položky `input`.
- **Formátovanie**: nahradiť najvyššiu úroveň `response_format` Chat-u za `text.format` v Responses. Kanonický tvar: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Položky obsahu**: nahradiť Chat `content[].type: "text"` za Responses `content[].type: "input_text"` pre kolá používateľa/systému.
- **Položky obsahu obrázkov**: nahradiť Chat `content[].type: "image_url"` za Responses `content[].type: "input_image"`. Pole `image_url` sa mení z vnoreného objektu `{"url": "..."}` na plochý reťazec. Pozri štartovací prehľad pre príklady pred a po.
- **Úsilie o zdôvodnenie**: **migruje sa iba `reasoning`, ak už existuje v pôvodnom kóde**.
- **Spracovanie chýb filtra obsahu**: štruktúra chybového tela sa zmenila. Chat Completions používal `error.body["innererror"]["content_filter_result"]` (jednotné číslo); Responses API používa `error.body["content_filters"][0]["content_filter_results"]` (množné číslo, vo vnútri poľa). Kód pristupujúci k `innererror` vyvolá `KeyError`. Prepísať, aby používal novú cestu.
- **Priame HTTP volania**: ak aplikácia volá priamo Azure OpenAI REST API (cez `requests`, `httpx` atď.) s `/openai/deployments/{name}/chat/completions?api-version=...`, prepísať na `/openai/v1/responses`. Telo požiadavky sa mení: `messages` → `input`, pridať `max_output_tokens` a `store: false`, odstrániť dotazový parameter `api-version`. Telo odpovede sa mení: `choices[0].message.content` → `output[0].content[0].text` (pozn.: `output_text` je vlastnosť SDK, ktorá neexistuje v surovom REST JSON).

---

## Krok 2: Použiť migráciu

### Poznámky k migrácii (Chat Completions → Responses)

- **Prečo migrovať**: Responses je jednotné API pre text, nástroje a streamovanie; Chat Completions je zastarané. S GPT-5 je Responses nevyhnutné pre najlepší výkon.
- **HTTP**: Azure endpoint prepína z `/openai/deployments/{name}/chat/completions` na `/openai/v1/responses`.
- **Polia**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` zostáva.
- **Formátovanie**: `response_format` → `text.format` s vhodným objektom.
- **Položky obsahu**: Nahradiť Chat `content[].type: "text"` za Responses `content[].type: "input_text"` pre kolá systému/používateľa.
- **Položky obsahu obrázkov**: Nahradiť Chat `content[].type: "image_url"` za Responses `content[].type: "input_image"`. Zploštiť pole `image_url` z `{"image_url": {"url": "..."}}` na `{"image_url": "..."}` (obyčajný reťazec — buď HTTPS URL alebo `data:image/...;base64,...` dátové URI).

### Reference mapovania parametrov

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (pole položiek) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (bez zmeny) |
| `stop` | `stop` (bez zmeny) |
| `frequency_penalty` | `frequency_penalty` (bez zmeny) |
| `presence_penalty` | `presence_penalty` (bez zmeny) |
| `tools` / volanie funkcií | `tools` (bez zmeny) |
| `seed` | **Odstrániť** (není podporované) |
| `store` | `store` (nastavené na `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (plochý reťazec) |

Pre kompletné príklady kódu pred a po, pozri [cheat-sheet.md](./references/cheat-sheet.md).

Pre migráciu testovej infraštruktúry (mocky, snapshoty, tvrdenia), pozri [test-migration.md](./references/test-migration.md).

Pre riešenie problémov a časté nástrahy, pozri [troubleshooting.md](./references/troubleshooting.md).

---

## Uchovávanie dát a stav

- Nastaviť `store: false` na všetkých požiadavkách Responses.
- Nespoliehať sa na predchádzajúce ID správ ani na serverom uložený kontext; udržiavať stav spravovaný klientom a minimalizovať metadata.

---

## Akceptačné kritériá

### Brány na úrovni kódu (všetky musia prejsť)

- [ ] Nula zhôd pre `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` v migrovaných súboroch.
- [ ] Nula zhôd pre `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — všetky konstruktory používajú `OpenAI`/`AsyncOpenAI` s v1 endpointom.
- [ ] Nula zhôd pre `rg "models\.github\.ai|models\.inference\.ai\.azure"` — kódy ciest pre GitHub modely odstránené.
- [ ] Nula zhôd pre `rg "OpenAIChatCompletionClient"` — kód MAF 1.0.0+ používa `OpenAIChatClient` (ktorý používa Responses API). V pre-1.0.0 upgradovať na `agent-framework-openai>=1.0.0`.
- [ ] Všetky volania `ChatOpenAI(...)` obsahujú `use_responses_api=True`.
- [ ] Nula zhôd pre `rg "choices\[0\]"` — všetok prístup k odpovedi používa `resp.output_text` alebo schému výstupu Responses.
- [ ] Žiadny `response_format` na najvyššej úrovni; všetok štruktúrovaný výstup používa `text={"format": {...}}`.
- [ ] `openai>=1.108.1` a `azure-identity` v `requirements.txt` alebo `pyproject.toml`; závislosti preinštalované.
- [ ] `store=False` nastavené pri každom volaní `responses.create`.
- [ ] Žiadna `api_version` v konštrukcii klienta; `AZURE_OPENAI_API_VERSION` odstránený z env súborov a infraštruktúry.

### Brány testovej infraštruktúry (všetky musia prejsť)

- [ ] Nula zhôd pre `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Nula zhôd pre `rg "_azure_ad_token_provider" tests/` — tvrdenia aktualizované, aby kontrolovali `isinstance(client, AsyncOpenAI)` alebo `base_url`.
- [ ] Nula zhôd pre `rg "prompt_filter_results|content_filter_results" tests/` — špecifické Azure filtre mocky odstránené.
- [ ] Mock fixture používa `kwargs.get("input")` namiesto `kwargs.get("messages")`.
- [ ] Snapshoty / zlaté súbory aktualizované na tvar streaming Responses (žiadne `choices[0]`, `function_call`, `logprobs` atď.).
- [ ] `pytest` prechádza bez chýb po všetkých aktualizáciách testov.

### Brány správania (overiť manuálne alebo cez testovací rámec)

- [ ] **Základné dokončenie**: nestreamujúce `responses.create` vráti neprázdny `output_text`.
- [ ] **Parita streamovania**: ak pôvodný kód používal streamovanie, migrovaný kód streamuje a vydáva udalosti `response.output_text.delta` s neprázdnymi deltami.
- [ ] **Štruktúrovaný výstup**: pri použití `text.format` s `json_schema`, `json.loads(resp.output_text)` prejde a zodpovedá schéme.
- [ ] **Slučka volkania nástrojov**: ak sa používajú nástroje, model vydáva volania nástrojov, aplikácia ich vykoná a následná požiadavka vráti finálny `output_text` (nie nekonečnú slučku).
- [ ] **Asynchrónna parita**: ak bol použitý `AsyncAzureOpenAI`, ekvivalentný `AsyncOpenAI` pracuje s `await`.
- [ ] **Miera chýb**: žiadne nové chyby 400/401/404 v porovnaní s pred-migračnou základňou.

### Výstupy

- Súhrn zahŕňa upravené súbory, počty starých volaní pred/potom a ďalšie kroky.
- Zmeny sú výlučne pracovné úpravy (bez commitov).

---

## Požiadavky na verziu SDK

| Balík | Minimálna verzia |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Najnovšia (pre autentifikáciu EntraID) |

---

## Referencie

- [Cheat Sheet — všetky kódy](./references/cheat-sheet.md)
- [Test Migration — mocky, snapshoty, tvrdenia](./references/test-migration.md)
- [Troubleshooting — chyby, tabuľka rizík, nástrahy](./references/troubleshooting.md)
- [detect_legacy.py — automatizovaný skener](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API docs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Životný cyklus verzií Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->