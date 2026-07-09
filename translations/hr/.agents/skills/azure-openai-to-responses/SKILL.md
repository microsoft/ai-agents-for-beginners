---
name: azure-openai-to-responses
license: MIT
---
# Migrirajte Python aplikacije s Azure OpenAI Chat Completions na Responses API

> **AUTORITATIVNI PRAVILNIK — SLJEDITI TOČNO**
>
> Ova vještina migrira Python kodne baze koje koriste Azure OpenAI Chat Completions
> na jedinstveni Responses API. Slijedite ove upute precizno.
> Ne improvizirajte mapiranja parametara niti ne izmišljajte oblike API-ja.

---

## Okidači

Aktivirajte ovu vještinu kada korisnik želi:
- Migrirati Python aplikaciju s Azure OpenAI Chat Completions na Responses API
- Nadograditi korištenje Python OpenAI SDK-a na najnoviji oblik API-ja za Azure OpenAI
- Pripremiti Python kod za GPT-5 ili novije modele koji zahtijevaju Responses na Azureu
- Prebaciti se s `AzureOpenAI`/`AsyncAzureOpenAI` na standardni `OpenAI`/`AsyncOpenAI` klijent s v1 endpointom
- Popraviti upozorenja o zastarjelosti vezana uz `AzureOpenAI` konstruktore ili `api_version`

---

## ⚠️ Kompatibilnost modela — PRVO PROVJERITE

> **Prije migracije, provjerite da vaša Azure OpenAI implementacija podržava Responses API.**

### 1. Brzi test implementacije (najbrže)

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

> **Napomena**: `max_output_tokens` ima **minimalno 16** na Azure OpenAI. Vrijednosti ispod 16 vraćaju pogrešku 400. Za brzo testiranje koristite 50+.

Ako ovo vraća 404, model implementacije još ne podržava Responses — provjerite referencu dolje ili ponovno implementirajte s podržanim modelom.

### 2. Provjerite dostupne modele u vašoj regiji (preporučeno)

Pokrenite ugrađeni alat za provjeru kompatibilnosti modela da vidite što je dostupno s podrškom Responses API-ja u vašoj specifičnoj regiji:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Ovo upituje Azure ARM uživo i prikazuje matricu kompatibilnosti — koji modeli podržavaju Responses, strukturirani izlaz, alate itd. Koristite `--filter gpt-5.1,gpt-5.2` za sužavanje rezultata ili `--json` za skriptiranje.

### 3. Referenca potpune podrške modela

- **Upit uživo**: `python migrate.py models` (vidi gore — specifično za regiju, uvijek ažurirano)
- **Pregled dostupnosti**: [Tablica sažetka modela i dostupnosti po regijama](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Brzi početak & upute**: **https://aka.ms/openai/start**

### ⚠️ Ograničenja starijih modela

> **UPOZORENJE**: Stariji modeli (npr. `gpt-4o`, `gpt-4`) možda ne podržavaju sve značajke Responses API-ja u potpunosti.
>
> Poznata ograničenja starijih modela:
> - **parametar `reasoning`**: Nije podržan na `gpt-4o-mini`, `gpt-4o` i mnogim modelima bez reasoning funkcionalnosti. Migrirajte `reasoning` samo ako je već postojao u izvornom kodu.
> - **parametar `seed`**: Nije podržan u Responses API-ju — uklonite iz svih zahtjeva.
> - **Strukturirani izlaz putem `text.format`**: Stariji modeli možda ne primjenjuju pouzdano JSON sheme s `strict: true`.
> - **Orkestracija alata**: GPT-5+ upravlja pozivima alata kao dio internog rezoniranja. Stariji modeli na Responses i dalje rade ali bez ove duboke integracije.
> - **Ograničenja temperature**: Kod migracije na `gpt-5`, temperatura mora biti izostavljena ili postavljena na `1`. Stariji modeli nemaju ovo ograničenje.

### O-serija reasoning modeli (o1, o3-mini, o3, o4-mini)

O-serija modela ima jedinstvena ograničenja parametara. Prilikom migracije aplikacija koje ciljaju o-seriju modele:

- **`temperature`**: Mora biti `1` (ili izostavljeno). O-serija modeli ne prihvaćaju druge vrijednosti.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikacije koje koriste Azure-specifični `max_completion_tokens` moraju se prebaciti na `max_output_tokens`. Postavite visoke vrijednosti (4096+) jer tokeni rezoniranja se računaju u limit.
- **`reasoning_effort`**: Ako aplikacija koristi `reasoning_effort` (low/medium/high), zadržite ga — Responses API podržava ovaj parametar za o-seriju modela.
- **Streaming ponašanje**: O-serija modeli mogu pohraniti izlaz dok rezoniranje ne završi prije emitiranja tekstualnih delta događaja. Streaming i dalje radi, ali prvi `response.output_text.delta` može stići s većim kašnjenjem nego kod GPT modela.
- **`top_p`**: Nije podržan na o-seriji — uklonite ako postoji.
- **Korištenje alata**: O-serija modeli podržavaju alate putem Responses API-ja isto kao GPT modeli, ali kvaliteta orkestracije poziva alata varira ovisno o modelu.

**Akcija — proaktivni savjet za modele**: Tijekom faze skeniranja, provjerite koji model aplikacija cilja (nazivi implementacija, varijable okoline, konfiguracija). Ako je model `gpt-4o` ili stariji (ne gpt-4.1+), proaktivno obavijestite korisnika:
- Migracija će raditi za osnovni tekst, chat, streaming i alate na njihovom trenutnom modelu.
- Noviji modeli (`gpt-5.1`, `gpt-5.2`) nude bolju orkestraciju alata, provedbu strukturiranog izlaza, rezoniranje i dostupnost preko regija.
- Trebali bi razmotriti nadogradnju implementacije kada budu spremni — to ne blokira migraciju.

Nemojte blokirati ili odbiti migraciju na temelju verzije modela. Savjet je informativan.

### GitHub modeli NE podržavaju Responses API

> **GitHub modeli (`models.github.ai`, `models.inference.ai.azure.com`) ne podržavaju Responses API.**

Ako kodna baza ima GitHub Models put koda (potražite `base_url` koji pokazuje na `models.github.ai` ili `models.inference.ai.azure.com`), **potpuno ga uklonite** tijekom migracije. Responses API zahtijeva Azure OpenAI, OpenAI ili kompatibilan lokalni endpoint (npr. Ollama s podrškom za Responses).

Akcija tijekom skeniranja:
- Označite sve GitHub Models putove koda za uklanjanje.

---

## Migracija frameworka

Mnoge aplikacije koriste frameworke višeg nivoa na vrhu OpenAI. Prilikom njihove migracije mijenja se i API frameworka — ne samo osnovni OpenAI pozivi.

### Microsoft Agent Framework (MAF)

**Prvo provjerite vašu verziju MAF-a** — migracija ovisi o tome je li to MAF 1.0.0+ ili pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **već koristi Responses API** — migracija nije potrebna. Ako kodna baza koristi legacijski `OpenAIChatCompletionClient` (koji koristi `chat.completions.create`), zamijenite ga s `OpenAIChatClient`.

| Prije | Poslije |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Za provjeru verzije: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc izdanja)

U pre-1.0.0 MAF, `OpenAIChatClient` je koristio Chat Completions. Nadogradite na `agent-framework-openai>=1.0.0` gdje `OpenAIChatClient` podrazumijevano koristi Responses API.

Nisu potrebne druge promjene — `Agent` i API za alate ostaju isti.

### LangChain (`langchain-openai`)

Dodajte `use_responses_api=True` u `ChatOpenAI()`. Također ažurirajte pristup rezultatu s `.content` na `.text`.

| Prije | Poslije |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Za potpune primjere koda prije/nakon, vidite [cheat-sheet.md](./references/cheat-sheet.md).

---

## Smjernice za migraciju frontenda

> **Responses API je briga poslužiteljske strane.** Migrirajte vaš Python backend; HTTP ugovor frontenda ne bi trebao biti promijenjen osim ako vaš backend nije tanak posrednik — u tom slučaju razmotrite usvajanje Requests oblika Responses API-ja da izbacite sloj prijevoda. Ako frontend poziva OpenAI direktno s ključem s klijentske strane, prvo te pozive premjestite na backend.

### Deprecacija `@microsoft/ai-chat-protocol`

`@microsoft/ai-chat-protocol` npm paket je zastario i treba ga zamijeniti s [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Ako ga pronađete na frontendu:

1. Zamijenite CDN skriptu:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Uklonite instanciranje `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Zamijenite `client.getStreamedCompletion(messages)` s izravnim `fetch()` pozivom na backend streaming endpoint.
4. Zamijenite `for await (const response of result)` s `for await (const chunk of readNDJSONStream(response.body))`.
5. Ažurirajte pristup svojstvima s `response.delta.content` / `response.error` na `chunk.delta.content` / `chunk.error`.

---

## Ciljevi

- Popisati sve Python pozive koji koriste Chat Completions ili legacijske Completions na Azure OpenAI.
- Predložiti plan i redoslijed migracije za Python kodnu bazu.
- Primijeniti sigurne, minimalne izmjene za prebacivanje na Responses API.
- Ažurirati pozivatelje da koriste Responses izlaznu shemu; bez prihrana za kompatibilnost unatrag.
- Pokrenuti testove/lintove; popraviti trivijalne prekide uvedene migracijom.
- Pripremiti male, pregledne promjene i pružiti konačni sažetak s razlikama (ne izvršavati commit).

---

## Sigurnosne mjere

- Mijenjati samo datoteke unutar git radnog prostora. Nikada ne pisati izvan.
- Ne čuvati kompatibilnost unazad; migrirati kod na novi oblik API-ja.
- Ne ostavljati komentare za prijelaz ili rezervne datoteke.
- Čuvati streaming semantiku ako je ranije korišten; inače koristiti bez streaminga.
- Tražiti odobrenje prije pokretanja naredbi ili mrežnih poziva ako je u načinu odobrenja.
- Ne pokretati `git add`/`git commit`/`git push`; producirati samo izmjene radnog stabla.

---

## Korak 0: Migracija Azure OpenAI klijenta (Preduvjet)

Ako kodna baza koristi `AzureOpenAI` ili `AsyncAzureOpenAI` konstruktore, prvo migrirajte na standardne `OpenAI` / `AsyncOpenAI` konstruktore. Azure-specifični konstruktori su zastarjeli u `openai>=1.108.1`.

### Zašto v1 API putanja?

Novi `/openai/v1` endpoint koristi standardni `OpenAI()` klijent umjesto `AzureOpenAI()`, ne zahtijeva `api_version` parametar i radi jednako na OpenAI i Azure OpenAI. Isti klijentski kod je budućnosti bez potrebe za upravljanjem verzijama.

### Ključne promjene

| Prije | Poslije |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Ukloni u potpunosti |

### Popis za čišćenje

- Uklonite `api_version` argument iz konstrukcije klijenta.
- Uklonite `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` varijable okoline iz `.env`, postavki aplikacije i Bicep/infra datoteka.
- Preimenujte `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` u `.env`, postavkama aplikacije, Bicep/infra i testnim podacima (standardna konvencija Azure Identity SDK-a).
- Osigurajte `openai>=1.108.1` u `requirements.txt` ili `pyproject.toml`.

### Migracija varijabli okoline

| Stara varijabla | Akcija | Napomene |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Ukloni** | Nije potreban `api_version` s v1 endpointom |
| `AZURE_OPENAI_API_VERSION` | **Ukloni** | Isto kao gore |
| `AZURE_OPENAI_CLIENT_ID` | **Preimenuj** → `AZURE_CLIENT_ID` | Standardna konvencija Azure Identity SDK-a za `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Zadrži** | Još uvijek potreban za konstrukciju `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Zadrži** | Koristi se kao `model` parametar u `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Zadrži** | Koristi se kao `api_key` za autentikaciju pomoću ključa |

Za primjere postavljanja klijenta (sinkroni, asinkroni, EntraID, API ključ, višekorisnički), pogledajte [cheat-sheet.md](./references/cheat-sheet.md).

---

## Korak 1: Otkrivanje legacijski poziva

Pokrenite skriptu [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) da nađete sve pozive koji trebaju migraciju:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Ili ručno obavite ove pretrage — svaki pogodak je cilj migracije:

```bash
# Naslijeđeni API pozivi (mora se prepisati)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Zastarjeli Azure konstruktori klijenta (mora se zamijeniti)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Obrasci pristupa obliku odgovora (mora se ažurirati)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definicije alata u starom ugniježđenom formatu (mora se pojednostaviti)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Rezultati alata u starom formatu (mora se pretvoriti u function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Zastarjeli parametri (mora se ukloniti ili preimenovati)
rg "response_format"
rg "max_tokens\b"        # preimenuj u max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Zastarjele varijable okruženja (očistiti)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # trebalo bi biti AZURE_CLIENT_ID

# GitHub Models krajnje točke (mora se ukloniti — Responses API nije podržan)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Naslijeđeni obrasci na razini okvira (mora se ažurirati)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: zamijeni s OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: treba use_responses_api=True

# Infrastruktura testiranja (mora se ažurirati)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Pristup tijelu pogreške filtra sadržaja (mora se ažurirati — struktura je promijenjena)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # stari jedinični oblik — sada content_filter_results (množina) unutar niza content_filters

# Neobrađeni HTTP pozivi na Chat Completions krajnju točku (mora se ažurirati URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristike (detektiraj i prepiši)

- **Klijent za Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure konstruktori klijenta**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Alati**: pretvori definicije funkcija alata iz ugniježđenog formata (`{"type": "function", "function": {"name": ...}}`) u ravni format Responses (`{"type": "function", "name": ...}`); koristi `tool_choice`; vraćaj rezultate alata kao stavke `{"type": "function_call_output", "call_id": ..., "output": ...}` (ne `{"role": "tool", ...}`).
- **Povratne obrade alata**: kada model vraća pozive funkcija, dodaj stavke `response.output` u razgovor (ne ručni rječnik `{"role": "assistant", "tool_calls": [...]}`), zatim dodaj stavke `function_call_output` za svaki rezultat.
- **Nekoliko primjera poziva alata**: ako razgovor uključuje unaprijed definirane primjere poziva alata, pretvori ih u stavke `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID-ovi moraju počinjati s `fc_`.
- **`pydantic_function_tool()`**: ovaj pomoćni alat još uvijek generira stari ugniježđeni format i **nije kompatibilan** s `responses.create()`. Zamijeni ručnim definicijama alata ili slojem za izravnavanje.
- **Višekratni okretaji**: održavaj povijest razgovora u aplikaciji; prosljeđuj prethodne okretaje putem stavki `input`.
- **Formatiranje**: zamijeni Chatovu vrhunsku postavku `response_format` s `text.format` u Responses. Kanonski oblik: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Stavke sadržaja**: zamijeni Chat `content[].type: "text"` s Responses `content[].type: "input_text"` za korisničke/sistemske okretaje.
- **Stavke slike u sadržaju**: zamijeni Chat `content[].type: "image_url"` s Responses `content[].type: "input_image"`. Polje `image_url` mijenja se iz ugniježđenog objekta `{"url": "..."}` u ravni string. Pogledaj cheat sheet za primjere prije i poslije.
- **Napori u razmišljanju**: **migriraj samo `reasoning` ako već postoji u izvornom kodu**.
- **Rukovanje pogreškama filtra sadržaja**: struktura tijela pogreške se promijenila. Chat Completions je koristio `error.body["innererror"]["content_filter_result"]` (jednina); Responses API koristi `error.body["content_filters"][0]["content_filter_results"]` (množina, unutar niza). Kod koji pristupa `innererror` će baciti `KeyError`. Prepiši da koristi novi put.
- **Izravni HTTP pozivi**: ako aplikacija izravno poziva Azure OpenAI REST API (putem `requests`, `httpx` itd.) koristeći `/openai/deployments/{name}/chat/completions?api-version=...`, prepiši na `/openai/v1/responses`. Tijelo zahtjeva se mijenja: `messages` → `input`, dodaj `max_output_tokens` i `store: false`, ukloni query parametar `api-version`. Tijelo odgovora se mijenja: `choices[0].message.content` → `output[0].content[0].text` (napomena: `output_text` je SDK svojstvo pogodnosti koje nije prisutno u sirovom REST JSON-u).

---

## Korak 2: Primijeni migraciju

### Napomene o migraciji (Chat Completions → Responses)

- **Zašto migrirati**: Responses je objedinjeni API za tekst, alate i streaming; Chat Completions je zastario. S GPT-5, Responses je potreban za najbolju izvedbu.
- **HTTP**: Azure endpoint se prebacuje s `/openai/deployments/{name}/chat/completions` na `/openai/v1/responses`.
- **Polja**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` ostaje.
- **Formatiranje**: `response_format` → `text.format` s ispravnim objektom.
- **Stavke sadržaja**: Zamijeni Chat `content[].type: "text"` s Responses `content[].type: "input_text"` za sistemske/korisničke okretaje.
- **Stavke slike u sadržaju**: Zamijeni Chat `content[].type: "image_url"` s Responses `content[].type: "input_image"`. Izravnaj polje `image_url` iz `{"image_url": {"url": "..."}}` u `{"image_url": "..."}` (običan string — HTTPS URL ili `data:image/...;base64,...` data URI).

### Referenca preslikavanja parametara

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (niz stavki) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (nepromijenjeno) |
| `stop` | `stop` (nepromijenjeno) |
| `frequency_penalty` | `frequency_penalty` (nepromijenjeno) |
| `presence_penalty` | `presence_penalty` (nepromijenjeno) |
| `tools` / pozivi funkcija | `tools` (nepromijenjeno) |
| `seed` | **Ukloni** (nije podržano) |
| `store` | `store` (postavljeno na `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ravni string) |

Za potpune primjere koda prije i poslije, vidi [cheat-sheet.md](./references/cheat-sheet.md).

Za migraciju testne infrastrukture (mockovi, snapshoti, asertacije), vidi [test-migration.md](./references/test-migration.md).

Za rješavanje problema i čestih zamki, vidi [troubleshooting.md](./references/troubleshooting.md).

---

## Čuvanje podataka i stanje

- Postavi `store: false` na svim Requests zahtjevima Responses.
- Ne oslanjaj se na prethodne ID-ove poruka niti na kontekst pohranjen na poslužitelju; drži stanje pod upravljanjem klijenta i minimiziraj metapodatke.

---

## Kriteriji prihvaćanja

### Vrata na razini koda (svi moraju proći)

- [ ] Nula podudaranja za `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` u migriranim datotekama.
- [ ] Nula podudaranja za `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — svi konstruktori koriste `OpenAI`/`AsyncOpenAI` s v1 endpointom.
- [ ] Nula podudaranja za `rg "models\.github\.ai|models\.inference\.ai\.azure"` — kodni putevi GitHub Models uklonjeni.
- [ ] Nula podudaranja za `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ kod koristi `OpenAIChatClient` (koji koristi Responses API). U verzijama prije 1.0.0, nadogradi na `agent-framework-openai>=1.0.0`.
- [ ] Svi pozivi `ChatOpenAI(...)` uključuju `use_responses_api=True`.
- [ ] Nula podudaranja za `rg "choices\[0\]"` — sav pristup odgovoru koristi `resp.output_text` ili Responses izlaznu šemu.
- [ ] Nema `response_format` na najvišoj razini; sav strukturirani izlaz koristi `text={"format": {...}}`.
- [ ] `openai>=1.108.1` i `azure-identity` u `requirements.txt` ili `pyproject.toml`; ovisnosti ponovno instalirane.
- [ ] `store=False` postavljeno na svaki poziv `responses.create`.
- [ ] Nema `api_version` u konstrukciji klijenta; `AZURE_OPENAI_API_VERSION` uklonjen iz env datoteka i infrastrukture.

### Vrata testne infrastrukture (svi moraju proći)

- [ ] Nula podudaranja za `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Nula podudaranja za `rg "_azure_ad_token_provider" tests/` — asertacije ažurirane za provjeru `isinstance(client, AsyncOpenAI)` ili `base_url`.
- [ ] Nula podudaranja za `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specifični filter mockovi uklonjeni.
- [ ] Mock fixture koristi `kwargs.get("input")` a ne `kwargs.get("messages")`.
- [ ] Snapshot / zlatne datoteke ažurirane na Responses streaming oblik (nema `choices[0]`, `function_call`, `logprobs`, itd.).
- [ ] `pytest` prolazi bez neuspjeha nakon svih ažuriranja testova.

### Vrata ponašanja (provjera ručno ili kroz testni okruženje)

- [ ] **Osnovni završetak**: ne-streaming `responses.create` vraća ne-prazan `output_text`.
- [ ] **Paritet streaminga**: ako je originalni kod koristio streaming, migrirani kod streama i emitira događaje `response.output_text.delta` s ne-praznim djelatnim razlikama.
- [ ] **Strukturirani izlaz**: ako se koristi `text.format` s `json_schema`, `json.loads(resp.output_text)` uspijeva i odgovara šemi.
- [ ] **Petlja poziva alata**: ako se koriste alati, model izdaje pozive alata, aplikacija ih izvršava, i naknadni zahtjev vraća konačni `output_text` (nema beskonačne petlje).
- [ ] **Async paritet**: ako je korišten `AsyncAzureOpenAI`, ekvivalent `AsyncOpenAI` radi s `await`.
- [ ] **Stopa pogrešaka**: nema novih 400/401/404 pogrešaka u odnosu na bazu prije migracije.

### Rezultati

- Sažetak uključuje uređene datoteke, broj poziva stare verzije prije i poslije, te sljedeće korake.
- Promjene su samo uredničke u radnom stablu (bez commitova).

---

## Zahtjevi verzije SDK-a

| Paket | Minimalna verzija |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Najnovija (za EntraID autentifikaciju) |

---

## Reference

- [Cheat Sheet — svi primjeri koda](./references/cheat-sheet.md)
- [Migracija testova — mockovi, snapshoti, asertacije](./references/test-migration.md)
- [Rješavanje problema — pogreške, tablica rizika, zamke](./references/troubleshooting.md)
- [detect_legacy.py — automatizirani skener](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Životni ciklus verzije Azure OpenAI API-ja](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API referenca](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->