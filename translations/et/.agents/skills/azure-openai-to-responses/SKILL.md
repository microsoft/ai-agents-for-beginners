---
name: azure-openai-to-responses
license: MIT
---
# Pythoni rakenduste migreerimine Azure OpenAI Chat Completions-ist Responses API-le

> **AUTORITEETNE JUHEND — JÄLGI TÄPSELT**
>
> See oskus migreerib Pythoni koodibaasid, mis kasutavad Azure OpenAI Chat Completions-i,
> ühtsesse Responses API-sse. Järgi neid juhiseid täpselt.
> Ära improviseeri parameetrite sobitamist ega leiuta API-kujusid.

---

## Tõuked

Aktiveeri see oskus, kui kasutaja soovib:
- Migreerida Python-rakendust Azure OpenAI Chat Completions-ist Responses API-le
- Uuendada Python OpenAI SDK kasutust uusimale API kujule Azure OpenAI vastu
- Valmistada Python-koodi ette GPT-5 või uuemate mudelite jaoks, mis vajavad Responses Azure’is
- Lülituda `AzureOpenAI`/`AsyncAzureOpenAI` kliendilt standardsele `OpenAI`/`AsyncOpenAI` kliendile v1 endpoint’iga
- Parandada aegunud hoiatusi, mis on seotud `AzureOpenAI` konstruktori või `api_version`-iga

---

## ⚠️ Mudeli ühilduvus — KONTROLLI ENNE

> **Enne migreerimist veendu, et sinu Azure OpenAI juurutus toetab Responses API-d.**

### 1. Tee kiire test (kõige kiirem)

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

> **Märkus**: Azure OpenAI-s on `max_output_tokens` vähim väärtus **16**. Väärtused alla 16 annavad 400 vea. Kasuta suitsutestide jaoks 50+ väärtust.

Kui see tagastab 404, siis juurutuse mudel ei toeta Responses veel — vaata allpool viidet või juuruta uuesti toetatud mudeliga.

### 2. Kontrolli piirkonnas saadaolevaid mudeleid (soovitatav)

Käivita sisseehitatud mudeli ühilduvuse tööriist, et näha, mis on saadaval vastava piirkonna Responses API toe osas:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

See päring küsib Azure ARM-i otse ja kuvab ühilduvusmatriisi — millised mudelid toetavad Responses, struktureeritud väljundit, tööriistu jms. Kasuta `--filter gpt-5.1,gpt-5.2`, et tulemusi kitsendada või `--json` skriptimiseks.

### 3. Täielik mudelitugi viide

- **Otsepäring**: `python migrate.py models` (vt ülal — piirkonnapõhine, alati ajakohane)
- **Sirvi saadavust**: [Mudelite kokkuvõtte tabel ja piirkonna saadavus](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Kiirkäivitus & juhised**: **https://aka.ms/openai/start**

### ⚠️ Vanemate mudelite piirangud

> **HOIATUS**: Vanemad mudelid (enne `gpt-4.1`) ei pruugi kõiki Responses API funktsioone täielikult toetada.
>
> Tuntud piirangud vanematel mudelitel:
> - **`reasoning` parameeter**: Paljude mitte-loogikapõhiste mudelite puhul ei toetata. Migreeri `reasoning` ainult siis, kui see oli originaalkoodis juba olemas.
> - **`seed` parameeter**: Responses API-s üldse mitte toetatud — eemalda kõikidest päringutest.
> - **Struktureeritud väljund `text.format` kaudu**: Vanemad mudelid ei pruugi usaldusväärselt sundida `strict: true` JSON skeeme.
> - **Tööriistade orkestreerimine**: GPT-5+ orkestrib tööriistakõnesid kui sisemist loogikat. Vanemad mudelid Responses API-s töötavad jätkuvalt, kuid ilma sügava integreerimiseta.
> - **Temperatuuri piirangud**: Migreerides `gpt-5` peale, tuleb temperatuur jätta välja või seada väärtuseks `1`. Vanematel mudelitel sellist piirangut ei ole.

### O-seeria loogikamudelid (o1, o3-mini, o3, o4-mini)

O-seeria mudelitel on spetsiifilised parameetrite piirangud. Migreerides rakendusi, mis kasutavad o-seeria mudeleid:

- **`temperature`**: Peab olema `1` (või ära jätetud). O-seeria mudelid ei aktsepteeri teisi väärtusi.
- **`max_completion_tokens` → `max_output_tokens`**: Rakendused, mis kasutavad Azure-spetsiifilist `max_completion_tokens` tuleb üle viia `max_output_tokens` kasutamiseks. Seadista kõrged väärtused (4096+), sest loogikatokendid arvestatakse limiidi sees.
- **`reasoning_effort`**: Kui rakendus kasutab `reasoning_effort` (low/medium/high), siis säilita see — Responses API toetab seda o-seeria mudelite puhul.
- **Streaming käitumine**: O-seeria mudelid võivad koondada väljundit kuni loogika lõpuni, enne kui teksti delta sündmusi väljastavad. Streaming töötab endiselt, kuid esimene `response.output_text.delta` võib saabuda hiljem kui GPT mudelite puhul.
- **`top_p`**: O-seeria mudelitel pole toetust — eemalda, kui esineb.
- **Tööriistade kasutus**: O-seeria mudelid toetavad tööriistu Response API kaudu samamoodi nagu GPT mudelid, kuid tööriistade kõne orkestreerimise kvaliteet varieerub mudelite lõikes.

**Tegevus — ennetav mudelinõuanne**: Skaneerimise faasis kontrolli, millist mudelit rakendus kasutab (juurutuse nimed, keskkonnamuutujad, konfiguratsioon). Kui mudel on vanem kui `gpt-4.1` (st mitte gpt-4.1+), anna kasutajale teada:
- Migreerimine töötab nende olemasoleval mudelil põhiteksti, chati, voogedastuse ja tööriistade puhul.
- Uuemad mudelid (`gpt-5.1`, `gpt-5.2`) pakuvad paremat tööriistade orkestreerimist, struktureeritud väljundi jõustamist, loogikat ja piirkondadevahelist saadavust.
- Võiksid kaaluda juurutuse uuendamist, kui valmis ollakse — see ei blokeeri migreerimist.

Ära takista ega keela migreerimist mudeliversiooni alusel. Nõuanne on informatiivne.

### GitHub Models ei toeta Responses API-d

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ei toeta Responses API-d.**

Kui koodibaasis on GitHub Models koodirada (otsi `base_url`, mis osutab `models.github.ai` või `models.inference.ai.azure.com` peale), **eemalda see täielikult** migreerimise ajal. Responses API nõuab Azure OpenAI, OpenAI või ühilduvat lokaalset endpoint’i (nt Ollama Responses toe korral).

Tegevus skaneerimise ajal:
- Märgi kõik GitHub Models koodirajad eemaldamiseks.

---

## Raamistiku migreerimine

Paljud rakendused kasutavad OpenAI peal kõrgema taseme raamistikke. Migreerides neid, muutub ka raamistiku enda API, mitte ainult OpenAI-põhised päringud.

### Microsoft Agent Framework (MAF)

**Kontrolli esmalt oma MAF versiooni** — migreerimine sõltub sellest, kas oled MAF 1.0.0+ või varasema 1.0.0 beta/rc versiooniga.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **kasutab juba Responses API-d** — migreerimine pole vajalik. Kui kood kasutab vananenud `OpenAIChatCompletionClient` (kasutab `chat.completions.create`), asenda see `OpenAIChatClient`-iga.

| Enne | Pärast |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Versiooni kontrollimiseks: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF enne 1.0.0 (beta/rc versioonid)

Enne 1.0.0 MAF-is kasutas `OpenAIChatClient` Chat Completions-it. Uuenda `agent-framework-openai>=1.0.0`-le, kus `OpenAIChatClient` kasutab vaikimisi Responses API-d.

Muid muudatusi pole vaja — `Agent` ja tööriistade API-d jäävad samaks.

### LangChain (`langchain-openai`)

Lisa `use_responses_api=True` `ChatOpenAI()` konstruktori parameetrite hulka. Uuenda ka vastuse kasutamine `.content` asemel `.text`.

| Enne | Pärast |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Täielike enne/pärast koodinäidete jaoks vt [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontendi migreerimise juhised

> **Responses API on serveripoolne teema.** Migreeri oma Python backend; frontendi HTTP leping peaks jääma muutumatuks, välja arvatud juhul, kui backend on lihtsalt õhuke läbipääs — sel juhul kaalu Responses päringu kuju kasutamist, et tõlkekihist vabaneda. Kui frontend kutsub OpenAI otse kliendipoolse võtmega, vii need kõned backend’i.

### `@microsoft/ai-chat-protocol` aegumine

`@microsoft/ai-chat-protocol` npm pakett on aegunud ja tuleks asendada [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) paketiga. Kui kohtad seda frontendis:

1. Asenda CDN skripti silt:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Eemalda `AIChatProtocolClient` loomine (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Asenda `client.getStreamedCompletion(messages)` otsese `fetch()` kõnega backend’i voogedastus endpoint’ile.
4. Asenda `for await (const response of result)` tsükkel `for await (const chunk of readNDJSONStream(response.body))` tsükliga.
5. Uuenda omaduste ligipääsu `response.delta.content` / `response.error` → `chunk.delta.content` / `chunk.error`.

---

## Eesmärgid

- Loetle kõik Pythoni kõnekohad, mis kasutavad Chat Completions või vananenud Completions-i Azure OpenAI vastu.
- Paku migreerimisplaani ja järjekorda Pythoni koodibaasi jaoks.
- Rakenda turvalisi ja minimaalseid muudatusi Responses API-le üleminekuks.
- Uuenda kutsujaid kasutama Responses väljundi skeemi; tagurpidi ühilduvuse abiühendid puuduvad.
- Käivita testid/lintimine; paranda kergeid rikkeid, mis migreerimisest tekkisid.
- Valmista väiksed, ülevaadatavad muudatuste kogumid ja anna lõplik kokkuvõte erinevustega (ära commiti).

---

## Kaitsemeetmed

- Muuda ainult faile git töökohas sees. Ära kirjuta väljaspool.
- Ära säilita tagurpidi ühilduvuse sileerimisi; migreeri kood uuele API kujule.
- Ära jäta maha lõpueide kommentaare ega varukoopiafaile.
- Säilita voogedastuse semantika, kui see oli varem kasutusel; muidu kasuta mitte-voogedastust.
- Küsi heakskiitu enne käskude või võrgukõnede käivitamist, kui olete heakskiitmise režiimis.
- Ära käivita `git add`/`git commit`/`git push`; tee ainult töölaua muutusi.

---

## Samm 0: Azure OpenAI kliendi migreerimine (eeldus)

Kui koodibaas kasutab `AzureOpenAI` või `AsyncAzureOpenAI` konstruktoreid, migreeri esmalt standardsetele `OpenAI` / `AsyncOpenAI` konstruktoritele. Azure-spetsiifilised konstruktorid on `openai>=1.108.1` versioonis aegunud.

### Miks v1 API tee?

Uus `/openai/v1` endpoint kasutab standardset `OpenAI()` klienti `AzureOpenAI()` asemel, ei nõua `api_version` parameetrit ja töötab nii OpenAI kui Azure OpenAI keskkondades identse käitumisega. Sama kliendikood on tulevikukindel — versioonihaldust pole vaja.

### Peamised muudatused

| Enne | Pärast |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Kogu ulatuses eemaldada |

### Puhastamise kontrollnimekiri

- Eemalda kliendi konstruktorist `api_version` argument.
- Eemalda `.env` failist, rakenduse seadistustest ja Bicep/infra failidest `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` keskkonnamuutujad.
- Nimeta `.env`, rakenduse seadistustes, Bicep/infra ja testimismeetodites `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` (tavapärane Azure Identity SDK konventsioon).
- Kontrolli, et `openai>=1.108.1` oleks kirjas `requirements.txt` või `pyproject.toml`.

### Keskkonnamuutjate migreerimine

| Vana keskkonnamuutuja | Tegevus | Märkused |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Eemalda** | V1 endpoint’iga `api_version` pole vaja |
| `AZURE_OPENAI_API_VERSION` | **Eemalda** | Sama mis üleval |
| `AZURE_OPENAI_CLIENT_ID` | **Nimeta ümber** → `AZURE_CLIENT_ID` | Tavapärane Azure Identity SDK konventsioon `ManagedIdentityCredential(client_id=...)` kasutamiseks |
| `AZURE_OPENAI_ENDPOINT` | **Säilita** | Endiselt vajalik `base_url` ehitamiseks |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Säilita** | Kasutatakse `model` parameetrina `responses.create` päringus |
| `AZURE_OPENAI_API_KEY` | **Säilita** | Kasutatakse võtme põhise autentimise jaoks `api_key`-na |

Näited kliendi seadistamiseks (sünkroonne, asünkroonne, EntraID, API võti, mitme üürniku tugi) vt [cheat-sheet.md](./references/cheat-sheet.md).

---

## Samm 1: Legacy kõnekohad tuvastamine

Käivita [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) skript, et leida kõik kõnekohad, mis vajavad migreerimist:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Või otsi need käsitsi — iga vaste on migreerimise sihtmärk:

```bash
# Pärand API kõned (peab ümber kirjutama)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Aegunud Azure kliendi konstruktorid (peab asendama)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Vastuse kuju juurdepääsu mustrid (peab uuendama)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Tööriistade definitsioonid vanas pesastatud formaadis (peab lamedamaks tegema)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Tööriista tulemused vanas formaadis (peab teisendama function_call_output'iks)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Aegunud parameetrid (peab eemaldama või ümber nimetama)
rg "response_format"
rg "max_tokens\b"        # ümber nimetama max_output_tokens-ks
rg "['\"]seed['\"]"      # remove entirely

# Aegunud keskkonnamuutujad (korista üles)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # peaks olema AZURE_CLIENT_ID

# GitHub mudelite otsapunktid (peab eemaldama — Vastuste API ei toetata)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Raamistiku tasandi pärandmustid (peab uuendama)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: asenda OpenAIChatClient'iga
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: vajab use_responses_api=True

# Testimise infrastruktuur (peab uuendama)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Sisu filtri vea keha juurdepääs (peab uuendama — struktuur muutunud)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # vana ainsuse vorm — nüüd content_filter_results (mitmus) content_filters massiivi sees

# Toored HTTP-kõned Chat Completions otsapunkti (peab uuendama URL-i)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristika (tuvasta ja ümberehita)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure kliendi konstruktorid**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Tööriistad**: teisenda funktsioonikõnete tööriistade definitsioonid süvitatud vormingust (`{"type": "function", "function": {"name": ...}}`) lamedasse Responses vormingusse (`{"type": "function", "name": ...}`); kasuta `tool_choice`; tagasta tööriista tulemused kui `{"type": "function_call_output", "call_id": ..., "output": ...}` üksused (mitte `{"role": "tool", ...}`).
- **Tööriistakõnede ringkäigud**: kui mudel tagastab funktsioonikõnesid, lisa `response.output` üksused vestlusele (mitte käsitsi `{"role": "assistant", "tool_calls": [...]}` sõnastik), seejärel lisa iga tulemuse kohta `function_call_output` üksused.
- **Mõned näited tööriistade kasutamisest**: kui vestlus sisaldab kõvasti kodeeritud tööriistakõnede näiteid, teisenda need `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` üksusteks. ID-d peavad algama `fc_`.
- **`pydantic_function_tool()`**: see abimees genereerib endiselt vana süvitatud vormingut ja ei ole **ühilduv** `responses.create()`-ga. Asenda see käsitsi tehtud tööriistade definitsioonidega või lamedaks muutuva wrapperiga.
- **Mitme sammuga**: säilita vestluse ajalugu rakenduses; edasta eelnevad sammud `input` üksustena.
- **Vormindamine**: asenda Chati ülataseme `response_format` Responsesi `text.format`-iga. Kanoniline kuju: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Sisuüksused**: asenda Chati `content[].type: "text"` Responsesi `content[].type: "input_text"`-iga kasutaja/süsteemi pöörete puhul.
- **Pildisisuüksused**: asenda Chati `content[].type: "image_url"` Responsesi `content[].type: "input_image"`-ga. Väli `image_url` muutub süvitatud objektist `{"url": "..."}` lamedaks stringiks. Vaata mälestuslehte enne/pärast näidete jaoks.
- **Põhjendustöö (reasoning)**: **migreeri `reasoning` ainult kui see juba originaalkoodis eksisteerib**.
- **Sisufiltri veakäsitlus**: vea keha struktuur muutus. Chat Completions kasutas `error.body["innererror"]["content_filter_result"]` (ainsus); Responses API kasutab `error.body["content_filters"][0]["content_filter_results"]` (mitmus, massiivi sees). Kood, mis kasutab `innererror` põhjustab `KeyError`. Kirjuta ümber uue tee kasutamiseks.
- **Puhaste HTTP päringute kutsed**: kui rakendus kutsub Azure OpenAI REST API otse (kasutades `requests`, `httpx` jne.) ja URL on `/openai/deployments/{name}/chat/completions?api-version=...`, kirjuta see ümber kui `/openai/v1/responses`. Päringu keha muutub: `messages` → `input`, lisa `max_output_tokens` ja `store: false`, eemalda `api-version` päringus. Vastuse keha muutub: `choices[0].message.content` → `output[0].content[0].text` (märkus: `output_text` on SDK mugavusomadus, mis puudub puhases REST JSONis).

---

## Samm 2: Rakenda migratsioon

### Migratsiooni märkmed (Chat Completions → Responses)

- **Miks migreerida**: Responses on ühtne API tekstile, tööriistadele ja voogesitusele; Chat Completions on pärand. GPT-5 puhul on Responses vajalik parima jõudluse jaoks.
- **HTTP**: Azure lõpp-punkt muutub `/openai/deployments/{name}/chat/completions`-lt `/openai/v1/responses`-le.
- **Väljad**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` jääb samaks.
- **Vormindamine**: `response_format` → `text.format` sobiva objektiga.
- **Sisuüksused**: asenda Chati `content[].type: "text"` Responsesi `content[].type: "input_text"`-ga süsteemi/kasutaja pöörete puhul.
- **Pildisisuüksused**: asenda Chati `content[].type: "image_url"` Responsesi `content[].type: "input_image"`-ga. Lameda `image_url` väljaga `{"image_url": {"url": "..."}}` → `{"image_url": "..."}` (lihtne string — kas HTTPS URL või `data:image/...;base64,...` andmete URI).

### Parameetrite võrdlustabel

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (üksuste Massiiv) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (muutmata) |
| `stop` | `stop` (muutmata) |
| `frequency_penalty` | `frequency_penalty` (muutmata) |
| `presence_penalty` | `presence_penalty` (muutmata) |
| `tools` / funktsioonikõned | `tools` (muutmata) |
| `seed` | **Eemalda** (ei toetata) |
| `store` | `store` (määra `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (lamed string) |

Täielike enne/järel koodinäidete jaoks vaata [cheat-sheet.md](./references/cheat-sheet.md).

Testimise infrastruktuuri migratsiooniks (mockid, hetktõmmised, kinnitused) vaata [test-migration.md](./references/test-migration.md).

Tõrgete ja raskuste korral vaata [troubleshooting.md](./references/troubleshooting.md).

---

## Andmete säilitamine ja olek

- Sea kõigile Responses päringutele `store: false`.
- Ära sõltu eelmiste sõnumite ID-dest ega serveris hoitavast kontekstist; hoia olek kliendipoolne ja minimiseer metaandmed.

---

## Aktsepteerimise kriteeriumid

### Kooditasandi nõuded (kõik peavad olema läbitud)

- [ ] Pole leitud vasteid `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` migreeritud failides.
- [ ] Pole leitud vasteid `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — kõik konstruktorid kasutavad `OpenAI`/`AsyncOpenAI` v1 lõpp-punkti.
- [ ] Pole leitud vasteid `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub mudelite kooditeed eemaldatud.
- [ ] Pole leitud vasteid `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ kood kasutab `OpenAIChatClient` (kasutab Responses API). Enne 1.0.0 värskenda `agent-framework-openai>=1.0.0`-ks.
- [ ] Kõik `ChatOpenAI(...)` kutseid sisaldavad `use_responses_api=True`.
- [ ] Pole leitud vasteid `rg "choices\[0\]"` — kõik vastuse ligipääsud kasutavad `resp.output_text` või Responses väljundiskeemi.
- [ ] Puudub ülataseme `response_format`; kogu struktureeritud väljund kasutab `text={"format": {...}}`.
- [ ] `openai>=1.108.1` ja `azure-identity` on `requirements.txt` või `pyproject.toml` failides; sõltuvused uuesti paigaldatud.
- [ ] Kõigil `responses.create` kutsedel on `store=False`.
- [ ] Ei ole `api_version` kliendi konstrueerimisel; `AZURE_OPENAI_API_VERSION` eemaldatud keskkonnafailidest ja infrastruktuurist.

### Testimise infrastruktuuri nõuded (kõik peavad läbi minema)

- [ ] Pole leitud vasteid `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Pole leitud vasteid `rg "_azure_ad_token_provider" tests/` — veendumiseks uuendatud, et kontrollida `isinstance(client, AsyncOpenAI)` või `base_url`.
- [ ] Pole leitud vasteid `rg "prompt_filter_results|content_filter_results" tests/` — Azure spetsiifilised filtrimockid eemaldatud.
- [ ] Mock-fikstuurid kasutavad `kwargs.get("input")` mitte `kwargs.get("messages")`.
- [ ] Hetktõmmised / kuldfailid uuendatud Responses voogedastuse kujule (ilma `choices[0]`, `function_call`, `logprobs` jne.).
- [ ] `pytest` läbib kõik testid ilma vigadeta pärast kõigi testide uuendamist.

### Käitumuslikud nõuded (kinnita käsitsi või testimise abil)

- [ ] **Põhikõne**: mittevoogesitav `responses.create` tagastab mitte-tühi `output_text`.
- [ ] **Voogesituse vastavus**: kui algne kood kasutas voogesitust, siis migreeritud kood voogesitab ja väljastab `response.output_text.delta` sündmusi mitte-tühjade deltas.
- [ ] **Struktureeritud väljund**: kui kasutatakse `text.format` koos `json_schema`-ga, siis `json.loads(resp.output_text)` õnnestub ja vastab skeemile.
- [ ] **Tööriistakutseloop**: kui kasutatakse tööriistu, siis mudel esitab tööriistakutsed, rakendus täidab need ja järgneva päringu tagastab lõpliku `output_text` (puudub lõputu tsükkel).
- [ ] **Asünkroonne vastavus**: kui kasutati `AsyncAzureOpenAI`-d, siis `AsyncOpenAI` ekvivalent töötab koos `await`-iga.
- [ ] **Vigade määr**: võrreldes eelmise olekuga ei esine uusi 400/401/404 vigu.

### Tarnitavad tulemused

- Kokkuvõte sisaldab muudetud faile, enne/pärast loendust pärandkõne kohtadest ja järgmisi samme.
- Muudatused on üksnes tööpuu muudatused (ilma commit'ideta).

---

## SDK versiooninõuded

| Pakett | Minimaalne versioon |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Viimane (EntraID autentimiseks) |

---

## Viited

- [Vihik — kõik koodinäited](./references/cheat-sheet.md)
- [Testimise migratsioon — mockid, hetktõmmised, kinnitused](./references/test-migration.md)
- [Tõrkeotsing — vead, riskitabel, lõksud](./references/troubleshooting.md)
- [detect_legacy.py — automaatne skanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Käivituspakett](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentatsioon](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API versiooni elutsükkel](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API viide](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->