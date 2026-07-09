---
name: azure-openai-to-responses
license: MIT
---
# Migreeri Pythoni rakendused Azure OpenAI Chat Completions-ist Responses API-le

> **VÕIMAS JUHEND — JÄLGI TÄPSELT**
>
> See oskus migreerib Python koodibaasid, mis kasutavad Azure OpenAI Chat Completions-e
> ühtse Responses API-le. Järgi neid juhiseid täpselt.
> Ära improviseeri parameetrite sidumisi ega leiuta API vorme.

---

## Käivitajad

Aktiveeri see oskus, kui kasutaja soovib:
- Migreerida Pythoni rakendust Azure OpenAI Chat Completions-ist Responses API-le
- Uuendada Python OpenAI SDK kasutust uusimale API vormile Azure OpenAI vastu
- Valmistada Python koodi ette GPT-5 või uuematele mudelitele, mis nõuavad Responses kasutamist Azure’is
- Lülituda `AzureOpenAI`/`AsyncAzureOpenAI` kliendilt tavapärasele `OpenAI`/`AsyncOpenAI` kliendile, kasutades v1 lõpp-punkti
- Parandada deprekeerimishoiatusi, mis on seotud `AzureOpenAI` konstruktori või `api_version`-iga

---

## ⚠️ Mudeli Ühilduvus — KONTROLLI EESMALT

> **Enne migreerimist veendu, et sinu Azure OpenAI juurutus toetab Responses API-d.**

### 1. Tee kiire test oma juurutuse puhul (kiireim)

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

> **Märkus**: Azure OpenAI-s on `max_output_tokens` väärtusel **minimaalselt 16**. Väärtused alla 16 põhjustavad 400 vea. Kasuta suitsutestiks väärtust 50+.

Kui see tagastab 404, siis sinu juurutuse mudel ei toeta veel Responses-e — vaata allolevat viidet või tee juurutus uuesti toetatud mudeliga.

### 2. Kontrolli oma regiooni saadaval olevaid mudeleid (soovitatav)

Käivita sisseehitatud mudeli ühilduvuse tööriist, et näha, millised mudelid sinu regioonis toetavad Responses API-d:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

See päring töötab Azure ARM-i live andmetega ja näitab ühilduvuse maatriksit — millised mudelid toetavad Responses, struktureeritud väljundit, tööriistu jne. Kasuta `--filter gpt-5.1,gpt-5.2` tulemuste kitsendamiseks või `--json` skriptimiseks.

### 3. Täielik mudeli toe viide

- **Live päring**: `python migrate.py models` (nagu eespool — spetsiifiline regioon, alati ajakohane)
- **Sirvi saadavust**: [Mudelite kokkuvõtte tabel ja regiooni saadavus](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Kiirstart & juhendamine**: **https://aka.ms/openai/start**

### ⚠️ Vanemate mudelite piirangud

> **HOIATUS**: Vanemad mudelid (nt `gpt-4o`, `gpt-4`) ei pruugi täielikult toetada kõiki Responses API omadusi.
>
> Tuntud piirangud vanemate mudelitega:
> - **`reasoning` parameeter**: Ei toeta `gpt-4o-mini`, `gpt-4o` ja paljud mitte-põhjendavad mudelid. Rända `reasoning` vaid kui see oli algses koodis olemas.
> - **`seed` parameeter**: Ei toeta Responses API-s üldse — eemalda kõikidest päringutest.
> - **Struktureeritud väljund `text.format` kaudu**: Vanemad mudelid ei pruugi korralikult tagada `strict: true` JSON skeemide järgimist.
> - **Tööriistade orkestreerimine**: GPT-5+ korraldab tööriistakõnesid sisemise põhjendamise osana. Vanemad mudelid Responses API-s töötavad, aga neil puudub see sügav integratsioon.
> - **Temperatuuri piirangud**: Migreerides `gpt-5`-le, tuleb temperatuuri välja jätta või seada `1`. Vanematel mudelitel sellist piirangut ei ole.

### O-seeria põhjendavad mudelid (o1, o3-mini, o3, o4-mini)

O-seeria mudelitel on unikaalsed parameetrite piirangud. Migreerides rakendusi, mis sihivad o-seeria mudeleid:

- **`temperature`**: Peab olema `1` (või välja jäetud). O-seeria mudelid ei aktsepteeri muid väärtusi.
- **`max_completion_tokens` → `max_output_tokens`**: Rakendused, mis kasutavad Azure-spetsiifilist `max_completion_tokens`, peavad üle minema `max_output_tokens`-ile. Sea kõrged väärtused (4096+), sest põhjenduse tokenid arvestatakse limiidi sisse.
- **`reasoning_effort`**: Kui rakendus kasutab `reasoning_effort` (madal/keskmine/kõrge), säilita see — Responses API toetab seda parameetrit o-seeria mudelite jaoks.
- **Voogedastuse käitumine**: O-seeria mudelid võivad väljundi vahemällu panna, kuni põhjendus lõpeb, enne kui teksti delta sündmused edastatakse. Voogedastus töötab siiski, aga esimene `response.output_text.delta` võib saabuda pikema viivitusega kui GPT mudelite puhul.
- **`top_p`**: Ei toetata o-seeria mudelitel — eemalda kui esineb.
- **Tööriistade kasutus**: O-seeria mudelid toetavad tööriistu Responses API kaudu samamoodi kui GPT mudelid, aga tööriistade kõnekorralduse kvaliteet varieerub mudelite kaupa.

**Tegevus — proaktiivne mudeli nõustamine**: Skaneerimise faasis kontrolli, millist mudelit rakendus sihib (juurutuse nimed, keskkonnamuutujad, konfiguratsioon). Kui mudel on `gpt-4o` või vanem (mitte gpt-4.1+), ütle kasutajale proaktiivselt:
- Migratsioon töötab põhilise teksti, vestluse, voogedastuse ja tööriistadega nende praeguse mudeli peal.
- Uuemad mudelid (`gpt-5.1`, `gpt-5.2`) pakuvad paremat tööriistade orkestreerimist, struktureeritud väljundi sundimist, põhjendamist ja piirkondadeülest saadavust.
- Nad võiksid kaaluda oma juurutuse uuendamist, kui valmis — see ei blokeeri migreerimist.

Ära blokeeri ega keela migreerimist mudeli versiooni põhjal. Nõustamine on informatiivne.

### GitHub Models ei toeta Responses API-d

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ei toeta Responses API-d.**

Kui koodibaasis on GitHub Models kooditee (otsi `base_url`i, mis osutab `models.github.ai` või `models.inference.ai.azure.com`-ile), **eemalda see täielikult** migreerimise ajal. Responses API nõuab Azure OpenAI, OpenAI või ühilduvat lokaalseid lõpp-punkti (nt Ollama koos Responses toe).

Toiming skaneerimise ajal:
- Märgista kõik GitHub Models kooditeed eemaldamiseks.

---

## Raamistiku Migratsioon

Paljud rakendused kasutavad OpenAI peal kõrgema taseme raamistikke. Nende migreerimisel muutub raamistiku oma API, mitte ainult OpenAI kutsete põhivorm.

### Microsoft Agent Framework (MAF)

**Kontrolli esmalt oma MAF versiooni** — migreerimine sõltub, kas oled MAF 1.0.0+ peal või allpool 1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **kasutab juba Responses API-d** — migreerimist ei ole vaja. Kui kood kasutab vananenud `OpenAIChatCompletionClient` (mis kasutab `chat.completions.create`), asenda see `OpenAIChatClient`-ga.

| Enne | Pärast |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Oma versiooni kontrollimiseks: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc versioonid)

Pre-1.0.0 MAF käitas `OpenAIChatClient` Chat Completions-ga. Uuenda `agent-framework-openai>=1.0.0` peale, kus `OpenAIChatClient` kasutab vaikimisi Responses API-d.

Ühtegi muudatust ei ole vaja — `Agent` ja tööriistade API-d jäävad samaks.

### LangChain (`langchain-openai`)

Lisa `use_responses_api=True` `ChatOpenAI()`-le. Värskenda ka response juurdepääsu `.content`-lt `.text`-ile.

| Enne | Pärast |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Täielike enne/pärast koodinäidete jaoks vaata [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontendi Migratsiooni Juhised

> **Responses API on serveripoolne teema.** Migreeri oma Python backend; frontendi HTTP leping peaks jääma muutumatuks, kui su backend ei ole ainult õhuke pass-through — sel juhul kaalu Responses päringu vormi kasutuselevõttu tõlketasandi kaotamiseks. Kui frontend kutsub OpenAI otse kliendipoolselt võtmega, tõsta need kutseid esmalt backendile.

### `@microsoft/ai-chat-protocol` deprekeerimine

`@microsoft/ai-chat-protocol` npm pakett on aegunud ja tuleks asendada [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) pakiga. Kui kohtad seda frontendis:

1. Asenda CDN skripti silt:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Eemalda `AIChatProtocolClient` instantsimine (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Asenda `client.getStreamedCompletion(messages)` otsese `fetch()` kõnega backend voogedastuse lõpp-punkti.
4. Asenda `for await (const response of result)` `for await (const chunk of readNDJSONStream(response.body))`-ga.
5. Uuenda omaduste lugemist `response.delta.content` / `response.error` → `chunk.delta.content` / `chunk.error`.

---

## Eesmärgid

- Loenda kõik Python kutse kohad, mis kasutavad Chat Completions või vananenud Completions Azure OpenAI vastu.
- Paku migreerimisplaan ja järjekord Python koodibaasile.
- Rakenda ohutuid, minimaalseid muudatusi, et lülituda Responses API-le.
- Uuenda kutsujaid tarbima Responses väljundi skeemi; ärge kasutage tagasisobivaid kapsleid.
- Käivita testid/lindid; paranda kergeid murranguid, mis migreerimisega kaasnesid.
- Valmista ette väiksed, muudetavad muudatuste komplektid ja anna lõplik kokkuvõte koos erinevustega (ära commiti).

---

## Julgestustrossid

- Muuda ainult faile git tööruumis. Ära kirjuta väljaspool seda.
- Ära säilita tagasikompatavuse shimme; migreeri kood uude API vormi.
- Ära jäta maha hauakivilike kommentaare ega varukoopia faile.
- Säilita voogedastuse semantikat, kui seda varem kasutati; muidu kasuta mitte-voogedastust.
- Küsi heakskiitu käsu või võrgu kutsumise käivitamiseks, kui oled heakskiidu režiimis.
- Ära käivita `git add`/`git commit`/`git push`; tee ainult tööpuu muudatusi.

---

## Etapp 0: Azure OpenAI kliendi migreerimine (Eeltingimus)

Kui koodibaas kasutab `AzureOpenAI` või `AsyncAzureOpenAI` konstruktoreid, migreeri esmalt tavapäraste `OpenAI` / `AsyncOpenAI` konstruktorite peale. Azure-spetsiifilised konstruktorid on deprekeeritud `openai>=1.108.1` versioonis.

### Miks v1 API rada?

Uus `/openai/v1` lõpp-punkt kasutab tavalist `OpenAI()` klienti `AzureOpenAI()` asemel, ei vaja `api_version` parameetrit ja töötab identselt OpenAI ja Azure OpenAI puhul. Sama kliendikood on tulevikukindel — versioonihaldust pole vaja.

### Peamised muudatused

| Enne | Pärast |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Eemalda täielikult |

### Puhastamise kontrollnimekiri

- Eemalda `api_version` argument kliendi konstrueerimisest.
- Eemalda `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` keskkonnamuutujad `.env`, rakenduse seadete ja Bicep/infra failidest.
- Nimeta `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` ümber `.env`, rakenduse seadetes, Bicep/infra ja testide fixture’is (standard Azure Identity SDK tava).
- Tagada `openai>=1.108.1` olemasolu `requirements.txt` või `pyproject.toml` failis.

### Keskkonnamuutujate migreerimine

| Vana keskkonnamuutuja | Tegevus | Märkused |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Eemalda** | v1 lõpp-punktiga pole `api_version` vaja |
| `AZURE_OPENAI_API_VERSION` | **Eemalda** | Sama mis ülal |
| `AZURE_OPENAI_CLIENT_ID` | **Nimeta ümber** → `AZURE_CLIENT_ID` | Standard Azure Identity SDK tava `ManagedIdentityCredential(client_id=...)` jaoks |
| `AZURE_OPENAI_ENDPOINT` | **Hoia alles** | Endiselt vajalik `base_url` ehitamiseks |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Hoia alles** | Kasutatakse `model` parameetrina `responses.create`-s |
| `AZURE_OPENAI_API_KEY` | **Hoia alles** | Kasutatakse võti-põhiseks autentimiseks `api_key`-na |

Kliendi seadistuse koodinäidete (sync, async, EntraID, API võti, mitme rentnikuga) jaoks vaata [cheat-sheet.md](./references/cheat-sheet.md).

---

## Etapp 1: Tuvasta vananenud kutsekohad

Käivita [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) skript, et leida kõik kohad, mida tuleb migreerida:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Või otsi käsitsi — iga vaste on migreerimise sihtmärgiks:

```bash
# Pärand API kõned (peab ümber kirjutama)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Vana Azure kliendi konstruktoreid (peab asendama)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Vastuse kuju juurdepääsu mustrid (peab uuendama)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Tööriistade definitsioonid vanas pesastatud formaadis (peab tasandama)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Tööriistade tulemused vanas formaadis (peab teisendama funktisooni_call_output kujule)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Vanaemad parameetrid (peab eemaldama või ümber nimetama)
rg "response_format"
rg "max_tokens\b"        # ümber nimetama max_output_tokens-iks
rg "['\"]seed['\"]"      # remove entirely

# Vana keskkonnamuutujad (peab puhastama)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # peaks olema AZURE_CLIENT_ID

# GitHub mudelite otspunktid (peab eemaldama — Vastuste APIt ei toetata)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Raamistiku tasemel pärand mustrid (peab uuendama)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: asenda OpenAIChatClient-iga
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: vajab use_responses_api=True

# Testimisinfrastruktuur (peab uuendama)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Sisu filtri vea keha juurdepääs (peab uuendama — struktuur muutunud)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # vanaainsusvorm — nüüd content_filter_results (mitmus) content_filters massiivi sees

# Toored HTTP kõned Chat Completions otspunkti (peab uuendama URLi)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristika (tuvasta ja kirjuta ümber)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure kliendi konstruktoreid**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Tööriistad**: teisenda funktsioonikõnede tööriistade definitsioonid pesastatud vormingust (`{"type": "function", "function": {"name": ...}}`) lameda Responses vormingusse (`{"type": "function", "name": ...}`); kasuta `tool_choice`; tagasta tööriista tulemused kui `{"type": "function_call_output", "call_id": ..., "output": ...}` üksused (mitte `{"role": "tool", ...}`).
- **Tööriista ringkäigud**: kui mudel tagastab funktsioonikõnesid, lisa `response.output` üksused vestlusele (mitte käsitsi `{"role": "assistant", "tool_calls": [...]}` sõnastik), seejärel lisa iga tulemuse jaoks `function_call_output` üksused.
- **Mõned tööriista näited**: kui vestluses on kõvadeks kodeeritud tööriista kõnede näited, teisenda need `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` üksusteks. ID-d peavad algama `fc_`.
- **`pydantic_function_tool()`**: see abivahend genereerib endiselt vana pesastatud vormingu ja EI OLE ühilduv `responses.create()`-ga. Asenda see käsitsi tööriista definitsioonidega või lameda ümbrisega.
- **Mitmekordne vahetus**: hoia vestlusajalugu rakenduses; edasta varasemad vahetused `input` üksuste kaudu.
- **Vormindamine**: asenda Chati tipp-taseme `response_format` Responses-is `text.format`-iga. Kanoniline kuju: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Sisuüksused**: asenda Chati `content[].type: "text"` Responses `content[].type: "input_text"`-iga kasutaja/süsteemi vahetuste jaoks.
- **Pildi sisuüksused**: asenda Chati `content[].type: "image_url"` Responses `content[].type: "input_image"`-ga. Väli `image_url` muutub pesastatud objektist `{"url": "..."}` labaseks stringiks. Vaata kiirpäälehte enne/pärast näidete kohta.
- **Põhjenduspingutus**: **migreeri `reasoning` ainult juhul, kui see on olemas algses koodis**.
- **Sisufiltri veakäsitlus**: vea keha struktuur muutus. Chat Completions kasutas `error.body["innererror"]["content_filter_result"]` (ainsus); Responses API kasutab `error.body["content_filters"][0]["content_filter_results"]` (mitmus, massiivis). Kood, mis pääseb ligi `innererror`-ile, viskab `KeyError`. Kirjuta ümber, et kasutada uut rada.
- **Märkamata HTTP kõned**: kui rakendus kutsub otse Azure OpenAI REST API-d (nt `requests`, `httpx` jms.) kaudu `/openai/deployments/{name}/chat/completions?api-version=...`, kirjuta ümber `/openai/v1/responses`-ks. Päringu keha muutub: `messages` → `input`, lisa `max_output_tokens` ja `store: false`, eemalda `api-version` päringus. Vastuse keha muutub: `choices[0].message.content` → `output[0].content[0].text` (märkus: `output_text` on SDK mugavuse omadus, mida ei ole REST JSON-is).

---

## Samm 2: Migreeri

### Migratsiooni märkmed (Chat Completions → Responses)

- **Miks migreerida**: Responses on ühtne API tekstiks, tööriistadeks ja voogedastuseks; Chat Completions on vananenud. GPT-5-ga on Responses parima jõudluse saamiseks kohustuslik.
- **HTTP**: Azure otsapunkt muutub `/openai/deployments/{name}/chat/completions`-st `/openai/v1/responses`-ks.
- **Väljad**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` jääb samaks.
- **Vormindamine**: `response_format` → `text.format` korrektse objektina.
- **Sisuüksused**: asenda Chati `content[].type: "text"` Responses `content[].type: "input_text"`-iga süsteemi/kasutaja vahetustes.
- **Pildi sisuüksused**: asenda Chati `content[].type: "image_url"` Responses `content[].type: "input_image"`-ga. Lase `image_url` välja lameda `{"image_url": {"url": "..."}}` asemel vormingusse `{"image_url": "..."}` (lihtne string — HTTPS URL või `data:image/...;base64,...` andme URI).

### Parameetrite kaardistuse viide

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (üksuste massiiv) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (muutumatu) |
| `stop` | `stop` (muutumatu) |
| `frequency_penalty` | `frequency_penalty` (muutumatu) |
| `presence_penalty` | `presence_penalty` (muutumatu) |
| `tools` / funktsioonikõned | `tools` (muutumatu) |
| `seed` | **Eemalda** (pole toetatud) |
| `store` | `store` (määra `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (laineline string) |

Täielike enne/peale koodi näidete jaoks vaata [cheat-sheet.md](./references/cheat-sheet.md).

Testimise infrastruktuuri migratsiooni (mock'id, hetkepildid, kinnitus) jaoks vaata [test-migration.md](./references/test-migration.md).

Veaotsingu ja probleemide lahendamise jaoks vaata [troubleshooting.md](./references/troubleshooting.md).

---

## Andmete säilitamine ja olek

- Sea kõigi Responses päringute puhul `store: false`.
- Ära tuginene varasemate sõnumite ID-dele ega serveris hoitavale kontekstile; hoia olek kliendipoolne ja minimialise metaandmete hulgaga.

---

## Aktsepteerimiskriteeriumid

### Koodi taseme tõkked (kõik peavad läbima)

- [ ] Migreritud failides ei tohi olla vasteid `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"`.
- [ ] Ei tohi olla vasteid `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — kõik konstruktorid kasutavad `OpenAI`/`AsyncOpenAI` v1 otsapunktiga.
- [ ] Ei tohi olla vasteid `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Mudelite koodirajad on eemaldatud.
- [ ] Ei tohi olla vasteid `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ kood kasutab `OpenAIChatClient` (mis kasutab Responses API-d). Enne 1.0.0 versiooni tõsta tasemele `agent-framework-openai>=1.0.0`.
- [ ] Kõik `ChatOpenAI(...)` kutseid sisaldavad `use_responses_api=True`.
- [ ] Ei tohi olla vasteid `rg "choices\[0\]"` — kogu vastuse ligipääs kasutab `resp.output_text` või Responses väljundiskeemi.
- [ ] Topp-tasemel ei tohi olla `response_format`; kogu struktureeritud väljund kasutab `text={"format": {...}}`.
- [ ] Failides `requirements.txt` või `pyproject.toml` on `openai>=1.108.1` ja `azure-identity`; sõltuvused paigaldatud uuesti.
- [ ] Iga `responses.create` kutsel on `store=False`.
- [ ] Kliendi loomisel pole `api_version`-i; `AZURE_OPENAI_API_VERSION` on eemaldatud keskkonnafailidest ja infrastruktuurist.

### Testimise infrastruktuuri tõkked (kõik peavad läbima)

- [ ] Ei tohi olla vasteid `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Ei tohi olla vasteid `rg "_azure_ad_token_provider" tests/` — kinnitusaktsioone on muudetud kontrollimaks `isinstance(client, AsyncOpenAI)` või `base_url`.
- [ ] Ei tohi olla vasteid `rg "prompt_filter_results|content_filter_results" tests/` — Azure-põhised filtri mock'id on eemaldatud.
- [ ] Mock-fixtuurid kasutavad `kwargs.get("input")` mitte `kwargs.get("messages")`.
- [ ] Hetkepilt / kuldread failid on uuendatud Responses voogedastuskuju jaoks (pole `choices[0]`, `function_call`, `logprobs` jne).
- [ ] `pytest` läbib kõik testid vigadeta pärast kõiki uuendusi.

### Käitumise tõkked (manuaalne kontroll või testimisraami kaudu)

- [ ] **Põhiline täitmine**: mitte-voogedastav `responses.create` tagastab mitte-tühi `output_text`.
- [ ] **Voogedastuse vastavus**: kui algne kood kasutas voogedastust, voogedastab migreeritud kood ja edastab `response.output_text.delta` sündmusi mitte-tühjade delta-dega.
- [ ] **Struktureeritud väljund**: kui kasutatakse `text.format` koos `json_schema`-ga, õnnestub `json.loads(resp.output_text)` ja see vastab skeemile.
- [ ] **Tööriista-kõne tsükkel**: kui kasutatakse tööriistu, teeb mudel tööriista-kõnesid, rakendus täidab need ja järgmiseks päringuks tagastatakse lõplik `output_text` (ei ole lõputut tsüklit).
- [ ] **Asünkroonne vastavus**: kui kasutati `AsyncAzureOpenAI`-d, siis `AsyncOpenAI` ekvivalent töötab koos `await`-iga.
- [ ] **Veamäär**: pärast migratsiooni ei ole uusi 400/401/404 vigu võrreldes baasajaga.

### Tarnekohustused

- Kokkuvõte sisaldab muudetud faile, vana kutsepiste enne/pärast loendust ja järgmisi samme.
- Muudatused on ainult tööpuu muudatused (ilma commit'ideta).

---

## SDK versiooni nõuded

| Pakett | Miinimumversioon |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Viimane (EntraID autentimiseks) |

---

## Viited

- [Kiirpääleht — kõik koodinäited](./references/cheat-sheet.md)
- [Testimise migratsioon — mock'id, hetkepildid, kinnitused](./references/test-migration.md)
- [Veaotsing — vead, riskide tabel, lõksud](./references/troubleshooting.md)
- [detect_legacy.py — automatiseeritud skanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI algkomplekt](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentatsioon](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API versiooni elutsükkel](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API viide](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->