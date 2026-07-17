---
name: azure-openai-to-responses
license: MIT
---
# Prenos Python aplikacij iz Azure OpenAI Chat Completions na Responses API

> **AVTORITETNA NAVODILA — UPOŠTEVAJTE Natančno**
>
> Ta veščina prenese Python kode, ki uporabljajo Azure OpenAI Chat Completions
> na enoten Responses API. Natančno upoštevajte ta navodila.
> Ne improvizirajte z mapiranjem parametrov ali ne izmišljajte oblik API.

---

## Sprožilci

Aktivirajte to veščino, ko uporabnik želi:
- Prenesti Python aplikacijo iz Azure OpenAI Chat Completions na Responses API
- Nadgraditi uporabo Python OpenAI SDK na najnovejšo obliko API z Azure OpenAI
- Pripraviti Python kodo za GPT-5 ali novejše modele, ki zahtevajo Responses na Azure
- Preklopiti iz `AzureOpenAI`/`AsyncAzureOpenAI` na standardni `OpenAI`/`AsyncOpenAI` klient z v1 endpointom
- Popraviti opozorila o zastarelosti, ki se nanašajo na konstruktorje `AzureOpenAI` ali `api_version`

---

## ⚠️ Združljivost modelov — PREVERITE NAJPREJ

> **Pred prenosom preverite, ali vaša Azure OpenAI namestitev podpira Responses API.**

### 1. Najhitrejši test namestitve (smoke-test)

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

> **Opomba**: `max_output_tokens` ima **minimalno vrednost 16** na Azure OpenAI. Vrednosti pod 16 vrnejo napako 400. Za testiranje uporabite 50+.

Če to vrne 404, model namestitve še ne podpira Responses — glejte spodnjo referenco ali znova namestite z podprtim modelom.

### 2. Preverite razpoložljive modele v vaši regiji (priporočeno)

Zaženite vgrajeno orodje za združljivost modelov, da vidite, kateri modeli podpirajo Responses API v vaši regiji:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

To poizveduje Azure ARM v živo in prikaže matriko združljivosti — kateri modeli podpirajo Responses, strukturiran izhod, orodja itd. Uporabite `--filter gpt-5.1,gpt-5.2` za omejitev rezultatov ali `--json` za skriptiranje.

### 3. Polna referenca podpore modelov

- **Poizvedba v živo**: `python migrate.py models` (glejte zgoraj — specifično za regijo, vedno posodobljeno)
- **Poglejte razpoložljivost**: [Pregledna tabela modelov in razpoložljivost po regijah](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Hiter začetek & navodila**: **https://aka.ms/openai/start**

### ⚠️ Omejitve starejših modelov

> **OPOZORILO**: Starejši modeli (pred `gpt-4.1`) morda ne podpirajo vseh funkcij Responses API v celoti.
>
> Znane omejitve starejših modelov:
> - **Parameter `reasoning`**: Ni podprt na številnih modelih brez reasoning logike. Prenesite `reasoning` samo, če je bil že v izvorni kodi.
> - **Parameter `seed`**: V Responses API sploh ni podprt — odstranite ga iz vseh zahtevkov.
> - **Strukturiran izhod z `text.format`**: Starejši modeli morda ne upoštevajo zanesljivo JSON shem `strict: true`.
> - **Orkestracija orodij**: GPT-5+ orkestrira klice orodij kot del notranjega reasoning-a. Starejši modeli pri Responses delujejo, vendar brez globoke integracije.
> - **Omejitve temperature**: Pri prenosu na `gpt-5` mora biti temperatura izpuščena ali nastavljena na `1`. Starejši modeli te omejitve nimajo.

### O-serija reasoning modeli (o1, o3-mini, o3, o4-mini)

O-serijski modeli imajo posebne omejitve parametrov. Pri prenosu aplikacij, ki ciljajo o-serijo:

- **`temperature`**: Mora biti `1` (ali izpuščena). O-serijski modeli ne sprejemajo drugih vrednosti.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikacije, ki uporabljajo Azure-specifični `max_completion_tokens`, morajo preklopiti na `max_output_tokens`. Nastavite visoke vrednosti (4096+), ker se reasoning tokeni štejejo proti omejitvi.
- **`reasoning_effort`**: Če aplikacija uporablja `reasoning_effort` (low/medium/high), ohranite — Responses API podpira ta parameter za o-serijo.
- **Streaming vedenje**: O-serijski modeli lahko zadržijo izhod do konca reasoning-a, preden sprostijo tekstovne delta dogodke. Streaming deluje, vendar lahko prvi `response.output_text.delta` prispe po daljšem zamiku kot pri GPT modelih.
- **`top_p`**: Ni podprt na o-seriji — odstranite, če je prisoten.
- **Uporaba orodij**: O-serijski modeli podpirajo orodja preko Responses API enako kot GPT modeli, ampak kakovost orkestracije klicev se razlikuje med modeli.

**Dejanje — proaktivno svetovanje glede modela**: Med pregledom preverite, kateri model aplikacija cilja (imena namestitev, env vars, konfiguracija). Če je model starejši od `gpt-4.1` (ne gpt-4.1+), uporabnika proaktivno obvestite:
- Prenos bo deloval za osnovni tekst, klepete, streaming in orodja na njihovem trenutnem modelu.
- Novejši modeli (`gpt-5.1`, `gpt-5.2`) nudijo boljšo orkestracijo orodij, uveljavljanje strukturiranega izhoda, reasoning in razpoložljivost čez regije.
- Naj razmislijo o nadgradnji namestitve, ko bodo pripravljeni — to ne ovira prenosa.

Ne blokirajte ali zavrnite prenosa zaradi različice modela. Svetovanje je informativno.

### GitHub modeli NE podpirajo Responses API

> **GitHub modeli (`models.github.ai`, `models.inference.ai.azure.com`) ne podpirajo Responses API.**

Če koda vsebuje potek kode za GitHub modele (preverite `base_url`, ki kaže na `models.github.ai` ali `models.inference.ai.azure.com`), **ga popolnoma odstranite** med prenosom. Responses API zahteva Azure OpenAI, OpenAI ali združljiv lokalni endpoint (npr. Ollama z podporo Responses).

Dejanje med pregledom:
- Oznaka vseh poti kode za GitHub modele za odstranitev.

---

## Prenos okvira

Veliko aplikacij uporablja višje nivojske okvire na vrhu OpenAI. Pri prenosu teh se spremeni API okvira — ne samo osnovni OpenAI klici.

### Microsoft Agent Framework (MAF)

**Preverite svojo različico MAF najprej** — prenos je odvisen od tega, ali imate MAF 1.0.0+ ali predhodno beta/rc različico.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **že uporablja Responses API** — prenos ni potreben. Če koda uporablja legacy `OpenAIChatCompletionClient` (ki uporablja `chat.completions.create`), zamenjajte z `OpenAIChatClient`.

| Pred | Po |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Za preverjanje različice: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc izdaje)

V pre-1.0.0 MAF je `OpenAIChatClient` uporabljal Chat Completions. Nadgradite na `agent-framework-openai>=1.0.0`, kjer `OpenAIChatClient` privzeto uporablja Responses API.

Druge spremembe niso potrebne — `Agent` in orodni API ostaneta enaka.

### LangChain (`langchain-openai`)

Dodajte `use_responses_api=True` v `ChatOpenAI()`. Prav tako spremenite dostop do odgovora iz `.content` v `.text`.

| Pred | Po |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Za celostne primere kode pred in po, si oglejte [cheat-sheet.md](./references/cheat-sheet.md).

---

## Navodila za prenos na frontendu

> **Responses API je zadeva na strani strežnika.** Prenesite vaš Python backend; HTTP protokol frontenda naj ostane nespremenjen, razen če je backend zgolj tanek prehod — v tem primeru razmislite o uporabi oblike responses zahtevkov za odpravo prevajanja. Če frontend kliče OpenAI direktno s klientskim ključem, premaknite te klice na backend.

### Odstranitev `@microsoft/ai-chat-protocol`

Paket npm `@microsoft/ai-chat-protocol` je zastarel in ga je treba zamenjati z [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Če ga najdete v frontend kodi:

1. Zamenjajte CDN skriptni tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Odstranite instanciranje `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Zamenjajte `client.getStreamedCompletion(messages)` z direktnim klicem `fetch()` na backend streaming endpoint.
4. Zamenjajte `for await (const response of result)` z `for await (const chunk of readNDJSONStream(response.body))`.
5. Posodobite dostop do lastnosti iz `response.delta.content` / `response.error` na `chunk.delta.content` / `chunk.error`.

---

## Cilji

- Našteti vse Python klice, ki uporabljajo Chat Completions ali legacy Completions proti Azure OpenAI.
- Predlagati načrt in vrstni red prenosa Python kode.
- Izvesti varne, minimalne spremembe za preklop na Responses API.
- Posodobiti klice, da porabijo Responses izhodno shemo; brez nazaj združljivih ovojnic.
- Zagnati teste/linte; popraviti trivialne napake, povzete s prenosom.
- Pripraviti majhne, pregledne spremembe in zagotoviti končni povzetek z razlikami (ne izvajajte commita).

---

## Zagotovila

- Spreminjajte samo datoteke znotraj git workspace. Nikoli zunaj.
- Ne ohranjajte nazaj združljivih ovojnic; prenesite kodo na novo obliko API.
- Ne puščajte grobov/komentarjev prehoda ali varnostnih kopij.
- Ohranite streaming semantiko, če je bila prej uporabljena; sicer uporabite ne-streaming.
- Zaženi vprašaj za odobritev pred tekom ukazov ali omrežnih klicev, če ste v režimu odobritve.
- Ne zaženite `git add`/`git commit`/`git push`; ustvarite samo popravke delovnega drevesa.

---

## Korak 0: Prenos Azure OpenAI klienta (predpogoj)

Če koda uporablja konstruktorje `AzureOpenAI` ali `AsyncAzureOpenAI`, najprej prenesite na standardne konstruktorje `OpenAI` / `AsyncOpenAI`. Azure-specifični konstruktorji so zastareli v `openai>=1.108.1`.

### Zakaj uporabljati v1 API pot?

Novi `/openai/v1` endpoint uporablja standardni `OpenAI()` klient namesto `AzureOpenAI()`, ne zahteva parametra `api_version` in deluje enako za OpenAI in Azure OpenAI. Enaka koda je pripravljena za prihodnost — ni potrebe po upravljanju različic.

### Ključne spremembe

| Pred | Po |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Odstranite v celoti |

### Kontrolni seznam čiščenja

- Odstranite `api_version` argument iz konstruktorja klienta.
- Odstranite okoljske spremenljivke `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` iz `.env`, nastavitvenih datotek in Bicep/infrastrukturnih datotek.
- Preimenujte `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` v `.env`, nastavitvah aplikacije, Bicep/infrastrukturnih datotek in testnih priborih (standardna konvencija Azure Identity SDK).
- Poskrbite, da je `openai>=1.108.1` v `requirements.txt` ali `pyproject.toml`.

### Migracija okoljskih spremenljivk

| Stara env spremenljivka | Dejanje | Opombe |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Odstrani** | Pri v1 endpointu ni potrebe za `api_version` |
| `AZURE_OPENAI_API_VERSION` | **Odstrani** | Enako kot zgoraj |
| `AZURE_OPENAI_CLIENT_ID` | **Preimenuj** → `AZURE_CLIENT_ID` | Standardna konvencija Azure Identity SDK za `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Ohrani** | Še vedno potreben za konstrukcijo `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Ohrani** | Uporablja se kot parameter `model` v `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Ohrani** | Uporablja se kot `api_key` za avtentikacijo z ključem |

Za primere nastavitve klienta (sinhrono, asinhrono, EntraID, API ključ, več najemnikov) si oglejte [cheat-sheet.md](./references/cheat-sheet.md).

---

## Korak 1: Detekcija legacy klicev

Zaženite skripto [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py), da najdete vse klicne točke, ki jih je treba prenesti:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Ali pa izvedite te iskalne poizvedbe ročno — vsak zadetek je cilj prenosa:

```bash
# Klici zastarele API (potrebna ponovna pisava)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Zastarele konstruktorje Azure odjemalcev (potrebno zamenjati)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Vzorce dostopa do oblike odziva (potrebno posodobiti)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definicije orodij v starem gnezdenem formatu (potrebno sploščiti)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Rezultati orodij v starem formatu (potrebno pretvoriti v function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Zastareli parametri (odstraniti ali preimenovati)
rg "response_format"
rg "max_tokens\b"        # preimenuj v max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Zastarele okoljske spremenljivke (počistiti)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # mora biti AZURE_CLIENT_ID

# GitHub Models končne točke (odstraniti — Responses API ni podprt)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Zastareli vzorci na ravni ogrodja (potrebno posodobiti)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: zamenjaj z OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: zahteva use_responses_api=True

# Testna infrastruktura (potrebno posodobiti)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Dostop do telesa napake filtra vsebine (potrebno posodobiti — struktura se je spremenila)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # stara samostalna oblika — zdaj content_filter_results (množina) znotraj polja content_filters

# Neobdelani HTTP klici za Chat Completions končno točko (potrebno posodobiti URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Hevristike (detekcija in prepisovanje)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Konstruktorji odjemalcev Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Orodja**: pretvorite definicije orodij za klic funkcij iz gnezdene oblike (`{"type": "function", "function": {"name": ...}}`) v plosko obliko Responses (`{"type": "function", "name": ...}`); uporabite `tool_choice`; rezultate orodja vrnite kot elemente `{"type": "function_call_output", "call_id": ..., "output": ...}` (ne kot `{"role": "tool", ...}`).
- **Povratni klici orodij**: ko model vrne klice funkcij, prilepite elemente `response.output` v pogovor (ne sami ročno `{"role": "assistant", "tool_calls": [...]}` slovar), nato pa prilepite elemente `function_call_output` za vsak rezultat.
- **Primeri orodij z nekaj strelčki**: če pogovor vključuje vnaprej določene primere klicev orodij, jih pretvorite v elemente `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID-ji morajo začeti z `fc_`.
- **`pydantic_function_tool()`**: ta pomočnik še vedno ustvarja staro gnezdeno obliko in ni **združljiv** z `responses.create()`. Zamenjajte z ročnimi definicijami orodij ali ovojnico za sploščitev.
- **Večkratni krogi**: ohranjajte zgodovino pogovora v aplikaciji; prejšnje poteze pošljite preko elementov `input`.
- **Oblika**: zamenjajte Chat-ov najvišji `response_format` z `text.format` v Responses. Kanonična oblika: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Vsebinski elementi**: zamenjajte Chat `content[].type: "text"` z Responses `content[].type: "input_text"` za poteze uporabnika/sistema.
- **Vsebinski elementi slik**: zamenjajte Chat `content[].type: "image_url"` z Responses `content[].type: "input_image"`. Polje `image_url` se spremeni iz gnezdenega objekta `{"url": "..."}` v plosko nizko vrednost. Oglejte si priročnik za primere pred in po.
- **Razlage**: **preselite `reasoning` samo, če že obstaja v originalni kodi**.
- **Upravljanje napak filtrov vsebine**: struktura telesa napake se je spremenila. Chat Completions je uporabljal `error.body["innererror"]["content_filter_result"]` (ednina); Responses API uporablja `error.body["content_filters"][0]["content_filter_results"]` (množina, znotraj polja). Koda, ki dostopa do `innererror`, bo pričela `KeyError`. Prepišite na novo pot.
- **Surovi HTTP klici**: če aplikacija neposredno kliče Azure OpenAI REST API (prek `requests`, `httpx` ipd.) z `/openai/deployments/{name}/chat/completions?api-version=...`, prepišite na `/openai/v1/responses`. Telo zahteve se spremeni: `messages` → `input`, dodajte `max_output_tokens` in `store: false`, odstranite parametar poizvedbe `api-version`. Telo odgovora se spremeni: `choices[0].message.content` → `output[0].content[0].text` (opomba: `output_text` je lastnost priročnosti v SDK, ni prisotna v surovem REST JSON).

---

## Korak 2: Uporabi migracijo

### Opombe k migraciji (Chat Completions → Responses)

- **Zakaj migrirati**: Responses je združeni API za besedilo, orodja in pretočne podatke; Chat Completions je zastarel. Z GPT-5 je Responses obvezen za najboljšo zmogljivost.
- **HTTP**: Azure endpoint preide z `/openai/deployments/{name}/chat/completions` na `/openai/v1/responses`.
- **Polja**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` ostane nespremenjen.
- **Oblika**: `response_format` → `text.format` s pravilnim objektom.
- **Vsebinski elementi**: zamenjajte Chat `content[].type: "text"` z Responses `content[].type: "input_text"` za poteze sistema/uporabnika.
- **Vsebinski elementi slik**: zamenjajte Chat `content[].type: "image_url"` z Responses `content[].type: "input_image"`. Sploščite polje `image_url` iz `{"image_url": {"url": "..."}}` v `{"image_url": "..."}` (navaden niz — bodisi HTTPS URL ali `data:image/...;base64,...` podatkovni URI).

### Referenca preslikave parametrov

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (polje elementov) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (brez sprememb) |
| `stop` | `stop` (brez sprememb) |
| `frequency_penalty` | `frequency_penalty` (brez sprememb) |
| `presence_penalty` | `presence_penalty` (brez sprememb) |
| `tools` / klic funkcij | `tools` (brez sprememb) |
| `seed` | **Odstranite** (ni podprto) |
| `store` | `store` (nastavljeno na `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ploski niz) |

Za popolne primere kode pred in po si oglejte [cheat-sheet.md](./references/cheat-sheet.md).

Za migracijo testne infrastrukture (mocks, snapshots, trditve) glejte [test-migration.md](./references/test-migration.md).

Za odpravljanje napak in pasti glejte [troubleshooting.md](./references/troubleshooting.md).

---

## Hranjenje podatkov in stanje

- Nastavite `store: false` pri vseh zahtevah Responses.
- Ne zanašajte se na prejšnje ID-je sporočil ali kontekst, shranjen na strežniku; stanje naj ostane upravljano na strani odjemalca in zmanjšajte metapodatke.

---

## Sprejemni kriteriji

### Vratca na nivoju kode (vse morajo biti uspešne)

- [ ] Nobenih zadetkov za `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` v migriranih datotekah.
- [ ] Nobenih zadetkov za `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — vsi konstruktorji uporabljajo `OpenAI`/`AsyncOpenAI` z v1 endpointom.
- [ ] Nobenih zadetkov za `rg "models\.github\.ai|models\.inference\.ai\.azure"` — odstranjene poti kode GitHub modelov.
- [ ] Nobenih zadetkov za `rg "OpenAIChatCompletionClient"` — koda MAF 1.0.0+ uporablja `OpenAIChatClient` (ki uporablja Responses API). Pred različico 1.0.0 nadgradite na `agent-framework-openai>=1.0.0`.
- [ ] Vsi klici `ChatOpenAI(...)` vključujejo `use_responses_api=True`.
- [ ] Nobenih zadetkov za `rg "choices\[0\]"` — ves dostop do odgovorov uporablja `resp.output_text` ali shemo izhoda Responses.
- [ ] Ni `response_format` na najvišji ravni; vsa strukturirana izhodna podatka uporabljata `text={"format": {...}}`.
- [ ] `openai>=1.108.1` in `azure-identity` v `requirements.txt` ali `pyproject.toml`; ponovno nameščene odvisnosti.
- [ ] `store=False` nastavljeno pri vsakem klicu `responses.create`.
- [ ] Ni `api_version` pri konstrukciji odjemalca; `AZURE_OPENAI_API_VERSION` odstranjen iz okolijskih datotek in infrastrukture.

### Vratca testne infrastrukture (vse morajo biti uspešne)

- [ ] Nobenih zadetkov za `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Nobenih zadetkov za `rg "_azure_ad_token_provider" tests/` — trditve so posodobljene za preverjanje `isinstance(client, AsyncOpenAI)` ali `base_url`.
- [ ] Nobenih zadetkov za `rg "prompt_filter_results|content_filter_results" tests/` — odstranljeni so filtri za Azure.
- [ ] Mocks uporabljajo `kwargs.get("input")`, ne `kwargs.get("messages")`.
- [ ] Datoteke snapshot / golden so posodobljene na pretočno obliko Responses (brez `choices[0]`, `function_call`, `logprobs` itd.).
- [ ] `pytest` uspešno teče brez napak po vseh posodobitvah testov.

### Vratca vedenja (preverite ročno ali prek testnega okvirja)

- [ ] **Osnovna dokončanja**: nepretočni `responses.create` vrne poln `output_text`.
- [ ] **Pariteta pretoka**: če je originalna koda uporabljala pretok, migrirana koda pretaka in daje dogodke `response.output_text.delta` z ne-praznimi delta vrednostmi.
- [ ] **Strukturirani izhod**: če uporabljate `text.format` z `json_schema`, `json.loads(resp.output_text)` uspe in se ujema s shemo.
- [ ] **Zanka klica orodja**: če se uporabljajo orodja, model vrne klice orodij, aplikacija jih izvaja, nato pa zahteva na koncu vrne končni `output_text` (brez neskončne zanke).
- [ ] **Asinhrona pariteta**: če je bil uporabljen `AsyncAzureOpenAI`, je podoben `AsyncOpenAI`, ki deluje z `await`.
- [ ] **Stopnja napak**: brez novih 400/401/404 napak v primerjavi z osnovno linijo pred migracijo.

### Deliverables

- Povzetek vključuje urejene datoteke, štetje legacy klicnih mest pred in po, in naslednje korake.
- Spremembe so le delovni urejevalni popravki (brez commitov).

---

## Zahteve glede različice SDK

| Paket | Najmanjša različica |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Najnovejša (za avtentikacijo EntraID) |

---

## Reference

- [Priročnik — vsi odseki kode](./references/cheat-sheet.md)
- [Migracija testov — mocks, snapshots, trditve](./references/test-migration.md)
- [Odpravljanje težav — napake, tabela tveganj, pasti](./references/troubleshooting.md)
- [detect_legacy.py — avtomatizirani skener](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Življenjski cikel različic Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Referenca OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->