---
name: azure-openai-to-responses
license: MIT
---
# Migrirajte Python aplikacije s Azure OpenAI Chat Completions na Responses API

> **AUTORITATIVNE UPUTE — SLJEDITE TOČNO**
>
> Ova vještina migrira Python kodne baze koje koriste Azure OpenAI Chat Completions
> na jedinstveni Responses API. Slijedite ove upute točno.
> Nemojte improvizirati preslikavanja parametara ili izmišljati oblike API-ja.

---

## Okidači

Aktivirajte ovu vještinu kada korisnik želi:
- Migrirati Python aplikaciju s Azure OpenAI Chat Completions na Responses API
- Nadograditi korištenje Python OpenAI SDK-a na najnoviji oblik API-ja za Azure OpenAI
- Pripremiti Python kod za GPT-5 ili novije modele koji zahtijevaju Responses na Azureu
- Prebaciti se s `AzureOpenAI`/`AsyncAzureOpenAI` na standardnog `OpenAI`/`AsyncOpenAI` klijenta s v1 krajnjom točkom
- Popraviti upozorenja o zastarjelosti vezana uz `AzureOpenAI` konstruktore ili `api_version`

---

## ⚠️ Kompatibilnost modela — PRVO PROVJERITE

> **Prije migracije provjerite podržava li vaša Azure OpenAI implementacija Responses API.**

### 1. Brzi test implementacije (najs brži)

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

> **Napomena**: `max_output_tokens` ima **minimum od 16** na Azure OpenAI. Vrijednosti ispod 16 vraćaju 400 pogrešku. Za brze testove koristite 50+.

Ako ovo vrati 404, model implementacije još ne podržava Responses — provjerite referencu dolje ili ponovno implementirajte s podržanim modelom.

### 2. Provjerite dostupne modele u svojoj regiji (preporučeno)

Pokrenite ugrađeni alat za kompatibilnost modela i pogledajte što je dostupno s podrškom za Responses API u vašoj regiji:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Ovo izvlači podatke iz Azure ARM uživo i prikazuje matricu kompatibilnosti — koji modeli podupiru Responses, strukturirani izlaz, alate itd. Koristite `--filter gpt-5.1,gpt-5.2` za sužavanje rezultata ili `--json` za skriptiranje.

### 3. Puni referentni popis podržanih modela

- **Upit uživo**: `python migrate.py models` (vidi gore — specifično za regiju, uvijek ažurno)
- **Pregled dostupnosti**: [Tablica sažetka modela i dostupnost po regijama](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Brzi početak i upute**: **https://aka.ms/openai/start**

### ⚠️ Ograničenja starijih modela

> **UPOZORENJE**: Stariji modeli (oni prije `gpt-4.1`) možda ne podržavaju sve značajke Responses API-ja u potpunosti.
>
> Poznata ograničenja kod starijih modela:
> - **parametar `reasoning`**: Nije podržan na mnogim modelima bez rasuđivanja. Migrirajte `reasoning` samo ako je već postojao u izvornom kodu.
> - **parametar `seed`**: Uopće nije podržan u Responses API-ju — uklonite ga iz svih zahtjeva.
> - **Strukturirani izlaz preko `text.format`**: Stariji modeli možda ne primjenjuju `strict: true` JSON sheme pouzdano.
> - **Orkestracija alata**: GPT-5+ upravlja pozivima alata kao dio unutarnjeg rasuđivanja. Stariji modeli na Responses rade, ali nemaju tu duboku integraciju.
> - **Ograničenja temperature**: Prilikom migracije na `gpt-5`, temperature treba izostaviti ili postaviti na `1`. Stariji modeli nemaju takvo ograničenje.

### O-serija modela za rasuđivanje (o1, o3-mini, o3, o4-mini)

O-serija modeli imaju jedinstvena ograničenja parametara. Prilikom migracije aplikacija za o-serija modele:

- **`temperature`**: Mora biti `1` (ili izostavljeno). O-serija modeli ne prihvaćaju druge vrijednosti.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikacije koje koriste Azure-specifični `max_completion_tokens` moraju prijeći na `max_output_tokens`. Postavite visoke vrijednosti (4096+) jer tokeni za rasuđivanje računaju prema ograničenju.
- **`reasoning_effort`**: Ako aplikacija koristi `reasoning_effort` (low/medium/high), zadržite ga — Responses API podržava ovaj parametar za o-serija modele.
- **Streaming ponašanje**: O-serija modeli mogu spremati izlaz dok se rasuđivanje ne završi prije emitiranja delta događaja teksta. Streaming i dalje funkcionira, ali prvi `response.output_text.delta` može stići nakon duže odgode nego kod GPT modela.
- **`top_p`**: Nije podržano na o-seriji — uklonite ako je prisutno.
- **Korištenje alata**: O-serija modeli podržavaju alate preko Responses API na isti način kao GPT modeli, ali kvaliteta orkestracije poziva alata varira ovisno o modelu.

**Akcija — proaktivni savjet o modelu**: Tijekom faze skeniranja provjerite koji model aplikacija cilja (imena implementacije, varijable okoline, konfiguracija). Ako model prethodi `gpt-4.1` (nije gpt-4.1+), proaktivno obavijestite korisnika:
- Migracija će raditi za osnovni tekst, chat, streaming i alate na njihovom trenutnom modelu.
- Noviji modeli (`gpt-5.1`, `gpt-5.2`) nude bolje orkestriranje alata, provođenje strukturiranih izlaza, rasuđivanje i dostupnost preko regija.
- Trebali bi razmotriti nadogradnju svoje implementacije kad budu spremni — to ne sprječava migraciju.

Nemojte blokirati ili odbiti migraciju na temelju verzije modela. Savjet je informativan.

### GitHub modeli NE podržavaju Responses API

> **GitHub modeli (`models.github.ai`, `models.inference.ai.azure.com`) ne podržavaju Responses API.**

Ako kodna baza ima GitHub Models kodni put (potražite `base_url` usmjeren na `models.github.ai` ili `models.inference.ai.azure.com`), **uklonite ga u potpunosti** tijekom migracije. Responses API zahtijeva Azure OpenAI, OpenAI ili kompatibilnu lokalnu krajnju točku (npr. Ollama s podrškom za Responses).

Akcija tijekom skeniranja:
- Označite sve GitHub Models kodne putove za uklanjanje.

---

## Migracija okvira

Mnoge aplikacije koriste višerazinske okvire na vrhu OpenAI-a. Prilikom migriranja tih okvira, mijenjaju se njihove API promjene — ne samo osnovni OpenAI pozivi.

### Microsoft Agent Framework (MAF)

**Najprije provjerite vašu verziju MAF-a** — migracija ovisi o tome jeste li na MAF 1.0.0+ ili pretbeta/rc verziji ispod 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **već koristi Responses API** — nije potrebna migracija. Ako kodna baza koristi zastarjeli `OpenAIChatCompletionClient` (koji koristi `chat.completions.create`), zamijenite ga s `OpenAIChatClient`.

| Prije | Poslije |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Za provjeru verzije: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc verzije)

U pre-1.0.0 MAF-u, `OpenAIChatClient` je koristio Chat Completions. Nadogradite na `agent-framework-openai>=1.0.0` gdje `OpenAIChatClient` koristi Responses API po defaultu.

Nema drugih potrebnih promjena — `Agent` i alati API ostaju isti.

### LangChain (`langchain-openai`)

Dodajte `use_responses_api=True` u `ChatOpenAI()`. Također ažurirajte pristup odgovoru s `.content` na `.text`.

| Prije | Poslije |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Za potpune primjere prije i poslije, pogledajte [cheat-sheet.md](./references/cheat-sheet.md).

---

## Upute za migraciju frontenda

> **Responses API je serverska briga.** Migrirajte vaš Python backend; HTTP ugovor frontenda treba ostati nepromijenjen osim ako vaš backend nije tanak prolaz — u tom slučaju razmotrite usvajanje Responses zahtjeva da uklonite sloj prevođenja. Ako frontend poziva OpenAI direktno s klijentskim ključem, premjestite te pozive prvo na backend.

### Deprecacija `@microsoft/ai-chat-protocol`

`@microsoft/ai-chat-protocol` npm paket je zastario i treba ga zamijeniti s [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Ako ga pronađete u frontendu:

1. Zamijenite CDN skriptu:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Uklonite instanciranje `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Zamijenite `client.getStreamedCompletion(messages)` direktnim `fetch()` pozivom na backend streaming endpoint.
4. Zamijenite `for await (const response of result)` s `for await (const chunk of readNDJSONStream(response.body))`.
5. Ažurirajte pristup svojstvima iz `response.delta.content` / `response.error` na `chunk.delta.content` / `chunk.error`.

---

## Ciljevi

- Izbrojite sve Python pozive koji koriste Chat Completions ili zastarjele Completions protiv Azure OpenAI.
- Predložite plan migracije i redoslijed za Python kodnu bazu.
- Primijenite sigurne, minimalne izmjene za prebacivanje na Responses API.
- Ažurirajte pozivače da koriste izlazne sheme Responses; bez omotača za retrokompatibilnost.
- Pokrenite testove/lintove; ispravite trivijalne greške nakon migracije.
- Pripremite male, pregledne skupove promjena i pružite konačni sažetak s razlikama (ne obvežite).

---

## Zaštitne mjere

- Mijenjajte datoteke samo unutar git radnog prostora. Nikada ne pišite izvan.
- Ne održavajte retrokompatibilne omotače; migrirajte kod na novi oblik API-ja.
- Ne ostavljajte komentare prijelaza ili sigurnosne kopije datoteka.
- Očuvajte semantiku streaminga ako je ranije korištena; inače koristite bez streaminga.
- Zatražite odobrenje prije pokretanja naredbi ili mrežnih poziva u režimu odobrenja.
- Nemojte pokretati `git add`/`git commit`/`git push`; napravite samo izmjene u radnom stablu.

---

## Korak 0: Migracija Azure OpenAI klijenta (preduvjet)

Ako kodna baza koristi `AzureOpenAI` ili `AsyncAzureOpenAI` konstruktore, najprije migrirajte na standardne `OpenAI` / `AsyncOpenAI` konstruktore. Azure-specifični konstruktori su zastarjeli u `openai>=1.108.1`.

### Zašto v1 API put?

Nova `/openai/v1` krajnja točka koristi standardnog klijenta `OpenAI()` umjesto `AzureOpenAI()`, ne zahtijeva `api_version` parametar i radi identično na OpenAI i Azure OpenAI. Isti klijentski kod je otporan na budućnost — nije potrebna uprava verzija.

### Ključne promjene

| Prije | Poslije |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Potpuno ukloni |

### Provjera i čišćenje

- Uklonite `api_version` argument iz konstrukcije klijenta.
- Uklonite varijable okoliša `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` iz `.env`, postavki aplikacije i Bicep/infra datoteka.
- Preimenujte `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` u `.env`, postavkama aplikacije, Bicep/infra i testnim podacima (standardna konvencija za Azure Identity SDK).
- Osigurajte `openai>=1.108.1` u `requirements.txt` ili `pyproject.toml`.

### Migracija varijabli okoliša

| Stara var var | Akcija | Napomene |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Ukloni** | Nije potreban `api_version` s v1 krajnjom točkom |
| `AZURE_OPENAI_API_VERSION` | **Ukloni** | Kao gore |
| `AZURE_OPENAI_CLIENT_ID` | **Preimenuj** → `AZURE_CLIENT_ID` | Standardna konvencija Azure Identity SDK za `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Zadrži** | Još uvijek je potreban za izgradnju `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Zadrži** | Koristi se kao parametar `model` u `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Zadrži** | Koristi se kao `api_key` za autentifikaciju na temelju ključa |

Za primjere postavljanja klijenta (sinkrono, asinkrono, EntraID, API ključ, višekorisnički), pogledajte [cheat-sheet.md](./references/cheat-sheet.md).

---

## Korak 1: Detekcija naslijeđenih poziva

Pokrenite skriptu [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) da pronađete sve pozive koje treba migrirati:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Ili pokrenite ove pretrage ručno — svaki pogodak je meta migracije:

```bash
# Pozivi naslijeđenog API-ja (mora se prepisati)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Zastarjeli konstruktori Azure klijenata (mora zamijeniti)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Obrasci pristupa obliku odgovora (mora se ažurirati)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definicije alata u starom ugniježdenom formatu (mora se izravnati)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Rezultati alata u starom formatu (mora se pretvoriti u function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Zastarjeli parametri (mora se ukloniti ili preimenovati)
rg "response_format"
rg "max_tokens\b"        # preimenuj u max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Zastarjele varijable okoline (očistiti)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # treba biti AZURE_CLIENT_ID

# GitHub Models krajnje točke (mora se ukloniti — Responses API nije podržan)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Naslijeđeni obrasci na razini okvira (mora se ažurirati)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: zamijeniti s OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: treba use_responses_api=True

# Infrastruktura testiranja (mora se ažurirati)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Pristup tijelu pogreške filtra sadržaja (mora se ažurirati — struktura se promijenila)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # stari jednina oblik — sada content_filter_results (množina) unutar niza content_filters

# Sirovi HTTP pozivi na Chat Completions krajnju točku (mora se ažurirati URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristike (otkrivanje i prepisivanje)

- **Chat Completions klijent**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure konstruktori klijenata**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Alati**: pretvorite definicije alata s pozivom funkcije iz ugniježđenog formata (`{"type": "function", "function": {"name": ...}}`) u ravni format Responses (`{"type": "function", "name": ...}`); koristite `tool_choice`; vraćajte rezultate alata kao stavke `{"type": "function_call_output", "call_id": ..., "output": ...}` (ne `{"role": "tool", ...}`).
- **Povratni pozivi alata**: kada model vraća pozive funkcija, dodajte stavke `response.output` u razgovor (ne ručno `{"role": "assistant", "tool_calls": [...]}` rječnik), zatim dodajte stavke `function_call_output` za svaki rezultat.
- **Primjeri alata u nekoliko snimki**: ako razgovor sadrži tvrdo kodirane primjere poziva alata, pretvorite ih u stavke `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID-ovi moraju počinjati s `fc_`.
- **`pydantic_function_tool()`**: ovaj pomoćni alat još uvijek generira stari ugniježđeni format i **nije kompatibilan** s `responses.create()`. Zamijenite ga ručnim definicijama alata ili slojem za ravnanje.
- **Višestruki krugovi**: održavajte povijest razgovora u aplikaciji; prosljeđujte prethodne krugove putem stavki `input`.
- **Formatiranje**: zamijenite Chatov top-level `response_format` s `text.format` u Responses. Kanonički oblik: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Stavke sadržaja**: zamijenite Chat `content[].type: "text"` s Responses `content[].type: "input_text"` za korisničke/sistemske krugove.
- **Stavke sadržaja slika**: zamijenite Chat `content[].type: "image_url"` s Responses `content[].type: "input_image"`. Polje `image_url` mijenja se iz ugniježđenog objekta `{"url": "..."}` u ravni string. Pogledajte varalicu za primjere prije/poslije.
- **Napori rezoniranja**: **migrirajte `reasoning` samo ako već postoji u izvornom kodu**.
- **Rukovanje pogreškama filtera sadržaja**: struktura tijela pogreške se promijenila. Chat Completions koristio je `error.body["innererror"]["content_filter_result"]` (jednina); Responses API koristi `error.body["content_filters"][0]["content_filter_results"]` (mnoga, unutar niza). Kod koji pristupa `innererror` digne će `KeyError`. Prepišite kod da koristi novi put.
- **RAW HTTP pozivi**: ako aplikacija izravno poziva Azure OpenAI REST API (putem `requests`, `httpx`, itd.) preko `/openai/deployments/{name}/chat/completions?api-version=...`, prepišite na `/openai/v1/responses`. Tijelo zahtjeva se mijenja: `messages` → `input`, dodajte `max_output_tokens` i `store: false`, uklonite parametar upita `api-version`. Tijelo odgovora se mijenja: `choices[0].message.content` → `output[0].content[0].text` (napomena: `output_text` je SDK svojstvo za jednostavnost, nema ga u sirovom REST JSON-u).

---

## Korak 2: Primjena migracije

### Napomene o migraciji (Chat Completions → Responses)

- **Zašto migrirati**: Responses je objedinjeni API za tekst, alate i streaming; Chat Completions je zastario. S GPT-5, Responses je obavezno za najbolju izvedbu.
- **HTTP**: Azure endpoint se mijenja iz `/openai/deployments/{name}/chat/completions` u `/openai/v1/responses`.
- **Polja**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` ostaje nepromijenjen.
- **Formatiranje**: `response_format` → `text.format` s odgovarajućim objektom.
- **Stavke sadržaja**: Zamijenite Chat `content[].type: "text"` s Responses `content[].type: "input_text"` za sistemske/korisničke krugove.
- **Stavke sadržaja slika**: Zamijenite Chat `content[].type: "image_url"` s Responses `content[].type: "input_image"`. Ravnajte polje `image_url` iz `{"image_url": {"url": "..."}}` u `{"image_url": "..."}` (obični string — HTTPS URL ili `data:image/...;base64,...` data URI).

### Referenca mapiranja parametara

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

Za potpune primjere koda prije/nakon, pogledajte [cheat-sheet.md](./references/cheat-sheet.md).

Za migraciju test infrastrukture (moci, snimke, tvrdnje), pogledajte [test-migration.md](./references/test-migration.md).

Za rješavanje pogrešaka i probleme, pogledajte [troubleshooting.md](./references/troubleshooting.md).

---

## Zadržavanje podataka i stanje

- Postavite `store: false` na svim Requests u Responses.
- Ne oslanjajte se na prethodne ID-ove poruka ili kontekst pohranjen na poslužitelju; držite stanje pod upravom klijenta i minimizirajte metapodatke.

---

## Kriteriji prihvaćanja

### Vrata na razini koda (svi moraju proći)

- [ ] Nema podudaranja za `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` u migriranim datotekama.
- [ ] Nema podudaranja za `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — svi konstruktori koriste `OpenAI`/`AsyncOpenAI` sa v1 endpointom.
- [ ] Nema podudaranja za `rg "models\.github\.ai|models\.inference\.ai\.azure"` — uklonjeni kodni putovi za GitHub modele.
- [ ] Nema podudaranja za `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ kod koristi `OpenAIChatClient` (koji koristi Responses API). U verzijama prije 1.0.0, nadogradite na `agent-framework-openai>=1.0.0`.
- [ ] Svi pozivi `ChatOpenAI(...)` uključuju `use_responses_api=True`.
- [ ] Nema podudaranja za `rg "choices\[0\]"` — sav pristup odgovorima koristi `resp.output_text` ili odgovarajući Responses output schema.
- [ ] Nema `response_format` na vrhunskoj razini; sav strukturirani izlaz koristi `text={"format": {...}}`.
- [ ] `openai>=1.108.1` i `azure-identity` u `requirements.txt` ili `pyproject.toml`; ovisnosti ponovno instalirane.
- [ ] `store=False` postavljeno na svaki poziv `responses.create`.
- [ ] Nema `api_version` u konstrukciji klijenta; `AZURE_OPENAI_API_VERSION` uklonjen iz env datoteka i infrastrukture.

### Vrata test infrastrukture (svi moraju proći)

- [ ] Nema podudaranja za `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Nema podudaranja za `rg "_azure_ad_token_provider" tests/` — tvrdnje ažurirane da provjeravaju `isinstance(client, AsyncOpenAI)` ili `base_url`.
- [ ] Nema podudaranja za `rg "prompt_filter_results|content_filter_results" tests/` — uklonjene Azure-specifične filter moke.
- [ ] Moke koriste `kwargs.get("input")` umjesto `kwargs.get("messages")`.
- [ ] Snimke / zlatne datoteke ažurirane za oblik Responses streaminga (bez `choices[0]`, `function_call`, `logprobs` itd.).
- [ ] `pytest` prolazi bez grešaka nakon svih ažuriranja.

### Funkcionalna vrata (provjera ručno ili putem test harnessa)

- [ ] **Osnovno dovršenje**: ne-streaming `responses.create` vraća neprazan `output_text`.
- [ ] **Paritet streama**: ako je originalni kod koristio streaming, migrirani kod streama i daje `response.output_text.delta` događaje s nepraznim deltakama.
- [ ] **Strukturirani izlaz**: ako se koristi `text.format` s `json_schema`, `json.loads(resp.output_text)` uspije i odgovara shemi.
- [ ] **Petlja poziva alata**: ako se koriste alati, model izdaje pozive alata, aplikacija ih izvršava, a naknadni zahtjev vraća konačni `output_text` (nema beskonačne petlje).
- [ ] **Asinkroni paritet**: ako je korišten `AsyncAzureOpenAI`, ekvivalent `AsyncOpenAI` radi s `await`.
- [ ] **Stopa pogrešaka**: nema novih 400/401/404 pogrešaka u usporedbi s prije migracije.

### Isporuke

- Sažetak uključuje uređene datoteke, broj poziva legacy API-ja prije/poslije, i sljedeće korake.
- Promjene su samo uređivanje u radnom stablu (bez commita).

---

## Zahtjevi verzije SDK-a

| Paket | Minimalna verzija |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Najnovija (za EntraID autentikaciju) |

---

## Reference

- [Varalica — svi primjeri koda](./references/cheat-sheet.md)
- [Migracija testova — moke, snimke, tvrdnje](./references/test-migration.md)
- [Rješavanje problema — pogreške, tablica rizika, zamke](./references/troubleshooting.md)
- [detect_legacy.py — automatski skener](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Životni ciklus verzije Azure OpenAI API-ja](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API referenca](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->