---
name: azure-openai-to-responses
license: MIT
---
# Migrirajte Python aplikacije z Azure OpenAI Chat Completions na Responses API

> **AVTORITETNA NAVODILA — UPORABLJAJTE NATANČNO**
>
> Ta veščina migrira Python kode, ki uporabljajo Azure OpenAI Chat Completions
> na enotni Responses API. Natančno sledite tem navodilom.
> Ne improvizirajte preslikav parametrov ali ne izumljajte oblik API-ja.

---

## Sprožilci

Aktivirajte to veščino, ko uporabnik želi:
- Migrirati Python aplikacijo iz Azure OpenAI Chat Completions na Responses API
- Nadgraditi uporabo Python OpenAI SDK na najnovejšo obliko API za Azure OpenAI
- Pripraviti Python kodo za modele GPT-5 ali novejše, ki potrebujejo Responses na Azure
- Preklopiti iz `AzureOpenAI`/`AsyncAzureOpenAI` na standardni `OpenAI`/`AsyncOpenAI` odjemalec z v1 končno točko
- Popraviti opozorila o upokojitvi, ki so povezana z gradniki `AzureOpenAI` ali `api_version`

---

## ⚠️ Združljivost modelov — PREVERITE NAZAJ

> **Pred migracijo preverite, ali vaša Azure OpenAI namestitev podpira Responses API.**

### 1. Opravi hitri test namestitve (najhitreje)

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

> **Opomba**: `max_output_tokens` ima **minimalno vrednost 16** na Azure OpenAI. Vrednosti pod 16 vrnejo napako 400. Za hitre teste uporabite vrednost 50+.

Če je vrnjena napaka 404, model namestitve še ne podpira Responses — preverite referenco spodaj ali ponovno namestite z modelom, ki je podprt.

### 2. Preverite razpoložljive modele v vaši regiji (priporočeno)

Zaženite orodje za preverjanje združljivosti modelov, da preverite, kateri modeli v vaši regiji podpirajo Responses API:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

To poizveduje Azure ARM v živo in prikazuje matriko združljivosti — kateri modeli podpirajo Responses, strukturiran izhod, orodja itd. Uporabite `--filter gpt-5.1,gpt-5.2` za omejitev rezultatov ali `--json` za skriptiranje.

### 3. Popolna referenca podpore modelov

- **Poizvedba v živo**: `python migrate.py models` (glej zgoraj — specifično za regijo, vedno posodobljeno)
- **Brskanje po razpoložljivosti**: [Povzetek tabel in razpoložljivost regij](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Hitri začetek in smernice**: **https://aka.ms/openai/start**

### ⚠️ Omejitve starejših modelov

> **OPOZORILO**: Starejši modeli (npr. `gpt-4o`, `gpt-4`) morda ne podpirajo vseh funkcij Responses API v celoti.
>
> Znane omejitve starejših modelov:
> - **Parameter `reasoning`**: ni podprt na `gpt-4o-mini`, `gpt-4o` in mnogih modelih brez reasoning. `reasoning` migrirajte samo, če je že bil prisoten v originalni kodi.
> - **Parameter `seed`**: ni podprt v Responses API sploh — odstranite ga iz vseh zahtevkov.
> - **Strukturiran izhod prek `text.format`**: starejši modeli morda ne zagotovijo doslednega `strict: true` JSON sheme.
> - **Orkestracija orodij**: GPT-5+ orkestrira klice orodij kot del notranjega reasoning procesa. Starejši modeli na Responses še delujejo, a nimajo te globoke integracije.
> - **Omejitve temperature**: pri migraciji na `gpt-5` je treba temperaturo izpustiti ali nastaviti na `1`. Starejši modeli nimate te omejitve.

### Modeli vrste O (o1, o3-mini, o3, o4-mini)

Modeli vrste O imajo posebne omejitve parametrov. Pri migraciji aplikacij, ki ciljajo O-serijo:

- **`temperature`**: mora biti `1` (ali izpuščeno). Modeli vrste O ne sprejemajo drugih vrednosti.
- **`max_completion_tokens` → `max_output_tokens`**: aplikacije, ki uporabljajo Azure-specifični `max_completion_tokens`, morajo preklopiti na `max_output_tokens`. Nastavite visoke vrednosti (4096+), ker štejejo tudi tokeni reasoning-a.
- **`reasoning_effort`**: če aplikacija uporablja `reasoning_effort` (nizka/srednja/visoka), jo ohranite — Responses API podporo ta parameter za O-serijo.
- **Vedenje predvajanja (streaming)**: modeli vrste O lahko zadržujejo izhod do zaključka reasoning preden oddajo dogodke spremembe besedila. Streaming še deluje, a prvi `response.output_text.delta` lahko prispe z zamudo v primerjavi z GPT modeli.
- **`top_p`**: ni podprt na O-seriji — odstranite, če je prisoten.
- **Uporaba orodij**: modeli vrste O podpirajo orodja preko Responses API enako kot GPT modeli, a se kakovost orkestracije klicev razlikuje po modelih.

**Ukrep — proaktiven nasvet o modelu**: med fazo skeniranja preverite, kateri model aplikacija cilja (imena namestitev, okoljske spremenljivke, konfiguracija). Če je model `gpt-4o` ali starejši (ne gpt-4.1+), uporabniku proaktivno sporočite:
- Migracija bo delovala za osnovno besedilo, klepet, streaming in orodja na njihovem trenutnem modelu.
- Novejši modeli (`gpt-5.1`, `gpt-5.2`) nudijo boljšo orkestracijo orodij, uveljavljanje strukturiranega izhoda, reasoning in razpoložljivost prek regij.
- Priporočajo nadgradnjo svoje namestitve, ko bo pripravljeno — to ne blokira migracije.

Ne blokirajte in ne zavrnite migracije na podlagi različice modela. Nasvet ima informativen namen.

### GitHub Models ne podpirajo Responses API

> **GitHub modeli (`models.github.ai`, `models.inference.ai.azure.com`) ne podpirajo Responses API.**

Če baza kode vsebuje klicne poti GitHub Modelov (poglejte za `base_url`, ki kaže na `models.github.ai` ali `models.inference.ai.azure.com`), **jih med migracijo popolnoma odstranite**. Responses API zahteva Azure OpenAI, OpenAI ali združljivo lokalno končno točko (npr. Ollama z podporo Responses).

Ukrep med skeniranjem:
- Označite vse poti kode GitHub Modelov za odstranitev.

---

## Migracija ogrodja

Veliko aplikacij uporablja višje nivoje ogrodij nad OpenAI. Pri njihovi migraciji se spremeni lastni API ogrodja — ne samo osnovni klici OpenAI.

### Microsoft Agent Framework (MAF)

**Najprej preverite svojo verzijo MAF** — migracija je odvisna, ali ste na MAF 1.0.0+ ali na pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` že uporablja Responses API — migracija ni potrebna. Če baza kode uporablja legacy `OpenAIChatCompletionClient` (ki uporablja `chat.completions.create`), ga zamenjajte z `OpenAIChatClient`.

| Pred | Po |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Za preverjanje verzije: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc izdaje)

V pre-1.0.0 MAF je `OpenAIChatClient` uporabljal Chat Completions. Nadgradite na `agent-framework-openai>=1.0.0`, kjer `OpenAIChatClient` privzeto uporablja Responses API.

Druge spremembe niso potrebne — API-ji `Agent` in orodij ostajajo isti.

### LangChain (`langchain-openai`)

Dodajte `use_responses_api=True` v `ChatOpenAI()`. Prav tako posodobite dostop do odziva iz `.content` na `.text`.

| Pred | Po |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Za popolne primere pred in po, glej [cheat-sheet.md](./references/cheat-sheet.md).

---

## Navodila za frontend migracijo

> **Responses API je zadeva strežniške strani.** Migrirajte vaš Python backend; HTTP pogodba frontend-a naj ostane nespremenjena, razen če je vaš backend le tanek prenosnik — v tem primeru razmislite o uporabi forme Responses zahteve, da odpravite prevajalsko plast. Če frontend kliče OpenAI neposredno s klientskim ključem, premaknite te klice najprej na backend.

### Odprava `@microsoft/ai-chat-protocol`

npm paket `@microsoft/ai-chat-protocol` je ukinjen in naj bo zamenjan z [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Če ga zasledite v frontendu:

1. Zamenjajte CDN script tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Odstranite inštanciranje `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Zamenjajte `client.getStreamedCompletion(messages)` z neposrednim `fetch()` klicem na backend streaming endpoint.
4. Zamenjajte `for await (const response of result)` z `for await (const chunk of readNDJSONStream(response.body))`.
5. Posodobite dostop do lastnosti iz `response.delta.content` / `response.error` na `chunk.delta.content` / `chunk.error`.

---

## Cilji

- Naštejte vse Python klicne točke, ki uporabljajo Chat Completions ali legacy Completions proti Azure OpenAI.
- Predlagajte načrt in zaporedje migracije Python kode.
- Uporabite varne, minimalne popravke za preklop na Responses API.
- Posodobite klice, da sprejemajo Response izhodno shemo; brez ovij za združljivost nazaj.
- Zaženite teste/linte; popravite trivijalne prekinitve zaradi migracije.
- Pripravite majhne, pregledne spremembe in zagotovite končno povzetek z razlikami (ne opravite commit).

---

## Varovalke

- Spremembe izvajajte samo znotraj delovnega prostora git. Nikoli ne pišite zunaj.
- Ne ohranjajte shims za združljivost nazaj; migrirajte kodo na novo obliko API.
- Ne puščajte komentarjev o prehodu ali rezervnih datotek.
- Ohranjajte streaming semantiko, če je bila prej uporabljena; sicer uporabite nestreaming.
- Pred izvajanjem ukazov ali omrežnih klicev v načinu odobritve zahajte za odobritev.
- Ne izvajajte `git add`/`git commit`/`git push`; ustvarjajte le spremembe v delovnem drevesu.

---

## Korak 0: Migracija Azure OpenAI odjemalca (predpogoj)

Če baza uporablja gradnike `AzureOpenAI` ali `AsyncAzureOpenAI`, najprej migrirajte na standardne gradnike `OpenAI` / `AsyncOpenAI`. Azure-specifični gradniki so upokojeni v `openai>=1.108.1`.

### Zakaj uporabljati v1 API pot?

Nova končna točka `/openai/v1` uporablja standardnega odjemalca `OpenAI()` namesto `AzureOpenAI()`, ne zahteva parametra `api_version` in deluje enako z OpenAI in Azure OpenAI. Enaka koda odjemalca je odporna na prihodnje spremembe — brez potrebe po upravljanju verzij.

### Ključne spremembe

| Pred | Po |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Odstranite v celoti |

### Kontrolni seznam čiščenja

- Odstranite argument `api_version` iz gradnje odjemalca.
- Odstranite okoljske spremenljivke `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` iz `.env`, nastavitev aplikacije in Bicep/infra datotek.
- Preimenujte `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` v `.env`, nastavitvah app, Bicep/infra in testnih pripomočkih (standardna konvencija Azure Identity SDK).
- Zagotovite `openai>=1.108.1` v `requirements.txt` ali `pyproject.toml`.

### Migracija okoljskih spremenljivk

| Stara okoljska spremenljivka | Ukrep | Opombe |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Odstranite** | Ni potrebe po `api_version` z v1 končno točko |
| `AZURE_OPENAI_API_VERSION` | **Odstranite** | Isto kot zgoraj |
| `AZURE_OPENAI_CLIENT_ID` | **Preimenujte** → `AZURE_CLIENT_ID` | Standardna konvencija Azure Identity SDK za `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Ohranite** | Še vedno potreben za gradnjo `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Ohranite** | Uporablja se kot `model` parameter v `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Ohranite** | Uporablja se kot `api_key` za avtorizacijo z ključem |

Za primere nastavitve odjemalcev (sinhrono, asinhrono, EntraID, API ključ, več najemnikov), glej [cheat-sheet.md](./references/cheat-sheet.md).

---

## Korak 1: Zaznajte Legacy klicne točke

Zaženite skripto [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py), da najdete vse klicne točke, ki potrebujejo migracijo:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Ali te iskanja izvedite ročno — vsak ujemajoči klic je cilj migracije:

```bash
# Klici zastarele API (je treba prepisati)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Zastarele konstruktorje odjemalcev Azure (je treba zamenjati)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Vzorce dostopa do oblike odziva (je treba posodobiti)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definicije orodij v starem vgnjenem formatu (je treba poravnati)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Rezultati orodij v starem formatu (je treba pretvoriti v function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Zastareli parametri (je treba odstraniti ali preimenovati)
rg "response_format"
rg "max_tokens\b"        # preimenuj v max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Zastarele okoljske spremenljivke (počistiti)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # bi moralo biti AZURE_CLIENT_ID

# GitHub Modeli končne točke (je treba odstraniti — Responses API ni podprt)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Zastareli vzorci na ravni ogrodja (je treba posodobiti)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: zamenjaj z OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: potrebuje use_responses_api=True

# Testna infrastruktura (je treba posodobiti)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Dostop do telesa napake filtra vsebine (je treba posodobiti — struktura se je spremenila)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # stara edninska oblika — zdaj content_filter_results (množinsko) znotraj polja content_filters

# Surovi HTTP klici na končno točko Chat Completions (je treba posodobiti URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Hevristike (zaznaj in prepiši)

- **Chat Completions odjemalec**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Konstruktorji Azure strank**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Orodja**: pretvori definicije orodij za klice funkcij iz gnezdene oblike (`{"type": "function", "function": {"name": ...}}`) v ploski format Responses (`{"type": "function", "name": ...}`); uporabi `tool_choice`; vrni rezultate orodij kot elemente `{"type": "function_call_output", "call_id": ..., "output": ...}` (ne `{"role": "tool", ...}`).
- **Povratni klici orodij**: ko model vrne klice funkcij, dodaj elemente `response.output` k pogovoru (ne ročni slovar `{"role": "assistant", "tool_calls": [...]}`), nato dodaj elemente `function_call_output` za vsak rezultat.
- **Primeri orodij z nekaj primeri**: če pogovor vključuje vnaprej kodirane primere klicev orodij, jih pretvori v elemente `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID-ji morajo začeti z `fc_`.
- **`pydantic_function_tool()`**: ta pomočnik še vedno ustvarja staro gnezdeno obliko in NI združljiv z `responses.create()`. Zamenjaj z ročnimi definicijami orodij ali ovojnim slojem za sploščitev.
- **Večkratni klici**: shrani zgodovino pogovora v aplikaciji; prejšnje vrstice posreduj preko elementov `input`.
- **Oblikovanje**: nadomesti zgornjo raven `response_format` v Chat z `text.format` v Responses. Kanonična oblika: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Vsebinski elementi**: nadomesti Chat `content[].type: "text"` z Responses `content[].type: "input_text"` za vrstice uporabnika/sistema.
- **Vsebinski elementi slik**: nadomesti Chat `content[].type: "image_url"` z Responses `content[].type: "input_image"`. Polje `image_url` se spremeni iz gnezdenega objekta `{"url": "..."}` v plosko nizovno obliko. Glej prevarantski list za primere pred in po.
- **Poglobljeno razmišljanje**: **migrirajte `reasoning` le, če je že prisoten v izvirni kodi**.
- **Obravnava napake filtrov vsebine**: struktura telesa napake se je spremenila. Chat Completions je uporabljal `error.body["innererror"]["content_filter_result"]` (ednina); Responses API uporablja `error.body["content_filters"][0]["content_filter_results"]` (množina, znotraj polja). Koda, ki dostopa do `innererror`, bo sprožila `KeyError`. Prepiši za uporabo nove poti.
- **Surovi HTTP klici**: če aplikacija neposredno kliče Azure OpenAI REST API (prek `requests`, `httpx` itd.) z `/openai/deployments/{name}/chat/completions?api-version=...`, prepiši na `/openai/v1/responses`. Telo zahtevka se spremeni: `messages` → `input`, dodaj `max_output_tokens` in `store: false`, odstrani `api-version` query parameter. Telo odgovora se spremeni: `choices[0].message.content` → `output[0].content[0].text` (opomba: `output_text` je uporabniška lastnost SDK, ni prisotna v surovem REST JSON).

---

## Korak 2: Uporabi migracijo

### Opombe o migraciji (Chat Completions → Responses)

- **Zakaj migrirati**: Responses je združeni API za besedilo, orodja in pretakanje; Chat Completions je zastarel. Pri GPT-5 je Responses nujen za najboljšo zmogljivost.
- **HTTP**: Azure končna točka preide z `/openai/deployments/{name}/chat/completions` na `/openai/v1/responses`.
- **Polja**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` ostaja nespremenjena.
- **Oblikovanje**: `response_format` → `text.format` s pravilnim objektom.
- **Vsebinski elementi**: Nadomesti Chat `content[].type: "text"` z Responses `content[].type: "input_text"` za vrstice sistema/uporabnika.
- **Vsebinski elementi slik**: Nadomesti Chat `content[].type: "image_url"` z Responses `content[].type: "input_image"`. Izplasti polje `image_url` iz `{"image_url": {"url": "..."}}` v `{"image_url": "..."}` (navaden niz — bodisi HTTPS URL ali `data:image/...;base64,...` podatkovni URI).

### Referenca preslikave parametrov

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (polje elementov) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (nespremenjeno) |
| `stop` | `stop` (nespremenjeno) |
| `frequency_penalty` | `frequency_penalty` (nespremenjeno) |
| `presence_penalty` | `presence_penalty` (nespremenjeno) |
| `tools` / klic funkcij | `tools` (nespremenjeno) |
| `seed` | **Odstrani** (ni podprto) |
| `store` | `store` (nastavi na `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ploski niz) |

Za popolne primere kode pred/potem glej [cheat-sheet.md](./references/cheat-sheet.md).

Za migracijo testne infrastrukture (moki, posnetki, trditve) glej [test-migration.md](./references/test-migration.md).

Za odpravljanje težav in posebnosti glej [troubleshooting.md](./references/troubleshooting.md).

---

## Zadrževanje podatkov in stanje

- Nastavi `store: false` na vseh zahtevkih Responses.
- Ne zanašaj se na prejšnje ID-je sporočil ali na kontekst, shranjen na strežniku; upravljanje stanja naj bo na odjemalski strani in minimiziraj metapodatke.

---

## Merila za sprejem

### Vrata na ravni kode (vsi morajo uspeti)

- [ ] Ni ujemanj za `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` v migriranih datotekah.
- [ ] Ni ujemanj za `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — vsi konstruktorji uporabljajo `OpenAI`/`AsyncOpenAI` z v1 končno točko.
- [ ] Ni ujemanj za `rg "models\.github\.ai|models\.inference\.ai\.azure"` — odstranjene so kode poti GitHub modelov.
- [ ] Ni ujemanj za `rg "OpenAIChatCompletionClient"` — koda MAF 1.0.0+ uporablja `OpenAIChatClient` (ki uporablja Responses API). Pred 1.0.0 nadgradnja na `agent-framework-openai>=1.0.0`.
- [ ] Vsi klici `ChatOpenAI(...)` vsebujejo `use_responses_api=True`.
- [ ] Ni ujemanj za `rg "choices\[0\]"` — ves dostop do odzivov uporablja `resp.output_text` ali shemo izhoda Responses.
- [ ] Ni `response_format` na vrhnji ravni; vse strukturirane izhode uporabljajo `text={"format": {...}}`.
- [ ] `openai>=1.108.1` in `azure-identity` v `requirements.txt` ali `pyproject.toml`; odvisnosti ponovno nameščene.
- [ ] `store=False` nastavljeno na vsakem klicu `responses.create`.
- [ ] Ni `api_version` pri konstrukciji klienta; `AZURE_OPENAI_API_VERSION` odstranjen iz okolijskih datotek in infrastrukture.

### Vrata testne infrastrukture (vsi morajo uspeti)

- [ ] Ni ujemanj za `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Ni ujemanj za `rg "_azure_ad_token_provider" tests/` — trditve posodobljene za preverjanje `isinstance(client, AsyncOpenAI)` ali `base_url`.
- [ ] Ni ujemanj za `rg "prompt_filter_results|content_filter_results" tests/` — odstranjeni Azure-specifični filtri in moki.
- [ ] Moki uporabljajo `kwargs.get("input")` ne `kwargs.get("messages")`.
- [ ] Posodobljene datoteke snapshot / golden na obliko pretakanja Responses (brez `choices[0]`, `function_call`, `logprobs` itd.).
- [ ] `pytest` uspešno zaključi brez napak po vseh posodobitvah testov.

### Vrata vedenja (ročno preverjanje ali preko testiranja)

- [ ] **Osnovna dokončanja**: `responses.create` z nepretakanjem vrne ne-prazen `output_text`.
- [ ] **Pariteta pretakanja**: če je izvirna koda uporabljala pretakanje, migrirana vrne tok in sprošča dogodke `response.output_text.delta` z ne-praznimi delta vrednostmi.
- [ ] **Strukturiran izhod**: če se uporablja `text.format` z `json_schema`, `json.loads(resp.output_text)` uspe in ustreza shemi.
- [ ] **Zanka klicev orodij**: če so uporabljena orodja, model izvede klice orodij, aplikacija jih izvede, nato nadaljnja zahteva vrne končni `output_text` (brez neskončne zanke).
- [ ] **Asinhrona pariteta**: če je bil uporabljen `AsyncAzureOpenAI`, enakovreden `AsyncOpenAI` deluje z `await`.
- [ ] **Stopnja napak**: brez novih 400/401/404 napak v primerjavi z bazo pred migracijo.

### Dobave

- Povzetek vključuje urejene datoteke, štetje primerov klicev zastarele kode pred in po ter nadaljnje korake.
- Spremembe so samo lokalne spremembe (brez committov).

---

## Zahteve za različice SDK

| Paket | Najnižja različica |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Najnovejša (za avtorizacijo EntraID) |

---

## Reference

- [Prevarantski list — vsi kodički](./references/cheat-sheet.md)
- [Migracija testov — moki, posnetki, trditve](./references/test-migration.md)
- [Odpravljanje težav — napake, tabela tveganj, posebnosti](./references/troubleshooting.md)
- [detect_legacy.py — avtomatizirani skener](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Osnovni komplet Azure OpenAI](https://aka.ms/openai/start)
- [Dokumentacija Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Življenjski cikel verzije Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Referenca OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->