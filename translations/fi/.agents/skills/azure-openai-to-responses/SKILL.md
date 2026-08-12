---
name: azure-openai-to-responses
license: MIT
---
# Siirrä Python-sovellukset Azure OpenAI Chat Completionsista Responses API:iin

> **VIRALLINEN OHJEISTUS — NOUDATA TARKASTI**
>
> Tämä taito siirtää Python-koodikantoja, jotka käyttävät Azure OpenAI Chat Completionsia
> yhdistettyyn Responses API:iin. Noudata näitä ohjeita täsmällisesti.
> Älä improvisoi parametrien vastaavuuksia tai keksitä API-muotoja.

---

## Laukaisijat

Aktivoi tämä taito, kun käyttäjä haluaa:
- Siirtää Python-sovelluksen Azure OpenAI Chat Completionsista Responses API:iin
- Päivittää Python OpenAI SDK:n käyttö uusimpaan API-muotoon Azure OpenAIta vasten
- Valmistella Python-koodi GPT-5 tai uudemmille malleille, jotka vaativat Responses API:n Azurella
- Vaihtaa `AzureOpenAI`/`AsyncAzureOpenAI` -asiakas standardiin `OpenAI`/`AsyncOpenAI`-asiakkaaseen v1-päätepisteellä
- Korjata vanhentumisvaroitukset, jotka liittyvät `AzureOpenAI` -konstruktoreihin tai `api_version`-parametriin

---

## ⚠️ Mallin yhteensopivuus — TARKISTA ENSIN

> **Ennen siirtoa varmista, että Azure OpenAI -asennuksesi tukee Responses API:a.**

### 1. Testaa asennus nopeasti (nopein)

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

> **Huom:** `max_output_tokens`:illa on **minimiarvo 16** Azure OpenAI:ssa. Alle 16 arvot palauttavat 400-virheen. Käytä 50+:aa nopeisiin testeihin.

Jos tämä palauttaa 404:n, asennuksen malli ei vielä tue Responses API:a — tarkista alla oleva viite tai ota käyttöön uusi malli, joka tukee.

### 2. Tarkista käytettävissä olevat mallit alueellasi (suositeltu)

Suorita sisäänrakennettu mallien yhteensopivuustyökalu nähdäksesi, mitä Responses API -tuki sisältää juuri sinun alueellasi:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Tämä kysely Azure ARM:lta näyttää yhteensopivuusmatriisin — mitkä mallit tukevat Responses API:a, rakenteellista tulostetta, työkaluja jne. Käytä `--filter gpt-5.1,gpt-5.2` tulosten rajaamiseen tai `--json` skriptausta varten.

### 3. Täydellinen mallituen viite

- **Live-kysely**: `python migrate.py models` (katso yllä — aluekohtainen, aina ajan tasalla)
- **Selaa saatavuutta**: [Mallin yhteenvetotaulukko ja alueiden saatavuus](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Nopeasti alkuun & ohjeistus**: **https://aka.ms/openai/start**

### ⚠️ Vanhempien mallien rajoitukset

> **VAROITUS**: Vanhemmat mallit (`gpt-4.1`-version edeltävät) eivät välttämättä tue kaikkia Responses API:n ominaisuuksia täysin.
>
> Tunnetut rajoitukset vanhemmilla malleilla:
> - **`reasoning`-parametri**: Ei tuettu monilla ei-päättelymalleilla. Siirrä `reasoning` vain, jos se oli jo alkuperäisessä koodissa.
> - **`seed`-parametri**: Ei lainkaan tuettu Responses API:ssa — poista kaikista pyynnöistä.
> - **Rakenteellinen tulos `text.format`-kohdassa**: Vanhemmat mallit eivät välttämättä luotettavasti vaadi `strict: true` JSON-skeemaa.
> - **Työkalujen orkestrointi**: GPT-5+ ohjaa työkalukutsuja sisäisen päättelyn osana. Vanhemmat mallit Responses API:ssa toimivat edelleen, mutta ilman syvää integraatiota.
> - **Lämpötilarajoitukset**: Kun siirrytään `gpt-5`:een, lämpötila pitää jättää pois tai asettaa arvoon `1`. Vanhemmilla malleilla ei ole tätä rajoitusta.

### O-sarjan päättelymallit (o1, o3-mini, o3, o4-mini)

O-sarjan malleilla on erityisiä parametrirajoituksia. Kun siirrät sovelluksia, jotka käyttävät o-sarjan malleja:

- **`temperature`**: Täytyy olla `1` (tai pois). O-sarjan mallit eivät hyväksy muita arvoja.
- **`max_completion_tokens` → `max_output_tokens`**: Azure-spesifistä `max_completion_tokens` -parametria käyttävät sovellukset vaihtavat `max_output_tokens`-parametriin. Aseta korkeat arvot (4096+) koska päättelytokenit lasketaan mukaan rajoitukseen.
- **`reasoning_effort`**: Jos sovellus käyttää `reasoning_effort`-parametria (low/medium/high), pidä se — Responses API tukee sitä o-sarjan malleilla.
- **Virtauskäytös (streaming)**: O-sarjan mallit voivat puskuroida tulosteen kunnes päättely on valmis ennen tekstideltatapahtumia. Virtaus toimii, mutta ensimmäinen `response.output_text.delta` voi saapua viiveellä verrattuna GPT-malleihin.
- **`top_p`**: Ei tuettu o-sarjalla — poista jos on.
- **Työkalujen käyttö**: O-sarjan mallit tukevat työkaluja Responses API:n kautta samalla tavalla kuin GPT-mallit, mutta työkalukutsujen orkestroinnin laatu vaihtelee mallin mukaan.

**Toiminta — proaktiivinen mallineuvonta**: Tarkastuksen aikana tarkista, mitä mallia sovellus käyttää (asennusten nimet, ympäristömuuttujat, konfiguraatio). Jos malli on ennen `gpt-4.1`-versiota (ei gpt-4.1+), kerro käyttäjälle proaktiivisesti:
- Siirto toimii perustekstin, chatin, striimauksen ja työkalujen osalta nykyisellä mallilla.
- Uudemmat mallit (`gpt-5.1`, `gpt-5.2`) tarjoavat paremman työkalujen orkestroinnin, rakenteellisen tulosteen hallinnan, päättelyn ja alueiden yli toimivuuden.
- Heidän kannattaa harkita päivitystä, kun ovat valmiita — päivitys ei estä siirtoa.

Älä estä tai kiellä siirtoa malliversion perusteella. Neuvonta on tiedoksi.

### GitHub Models ei tue Responses API:a

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ei tue Responses API:a.**

Jos koodikannassa on GitHub Models -koodi (etsi `base_url` osoittamaan `models.github.ai` tai `models.inference.ai.azure.com`), **poista se kokonaan** migraation aikana. Responses API vaatii Azure OpenAI:n, OpenAI:n tai yhteensopivan paikallisen päätepisteen (esim. Ollama Responses-tuella).

Toiminta tarkastuksen aikana:
- Merkitse kaikki GitHub Models -koodipolut poistettaviksi.

---

## Kehyksen siirto

Monet sovellukset käyttävät korkeamman tason kehyksiä OpenAI:n päällä. Kun siirrät näitä, myös kehyksen oma API muuttuu — ei pelkästään OpenAI-kutsut.

### Microsoft Agent Framework (MAF)

**Tarkista ensin MAF-versiosi** — siirto riippuu siitä, onko käytössäsi MAF 1.0.0+ vai beta/rc-versio ennen 1.0.0:aa.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **käyttää jo Responses API:a** — siirtoa ei tarvita. Jos koodikanta käyttää vanhaa `OpenAIChatCompletionClient`:ia (joka käyttää `chat.completions.create`), vaihda se `OpenAIChatClient`:iin.

| Ennen | Jälkeen |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Tarkista versio: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF ennen 1.0.0 (beta/rc-julkaisut)

Ennen 1.0.0 MAF:n `OpenAIChatClient` käytti Chat Completionsia. Päivitä `agent-framework-openai>=1.0.0`:aan, jossa `OpenAIChatClient` käyttää Responses API:a oletuksena.

Muita muutoksia ei tarvita — `Agent` ja työkalujen API:t pysyvät ennallaan.

### LangChain (`langchain-openai`)

Lisää `use_responses_api=True` `ChatOpenAI()`-kutsuun. Päivitä myös vastauksen pääsy `.content` -> `.text`.

| Ennen | Jälkeen |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Täydelliset esimerkit ennen/jälkeen on [cheat-sheet.md](./references/cheat-sheet.md) tiedostossa.

---

## Frontend-siirto-ohjeet

> **Responses API on palvelinpuolen asia.** Siirrä Python-backend; frontendin HTTP-sopimuksen tulisi pysyä samana, ellei backend ole ohut välitys — silloin harkitse Responses-pyyntömuodon käyttöä käännöstason poistamiseksi. Jos frontend kutsuu OpenAI:ta suoraan client-side-avaimella, siirrä nämä kutsut ensin backendille.

### `@microsoft/ai-chat-protocol` on poistunut käytöstä

`@microsoft/ai-chat-protocol` npm-paketti on vanhentunut ja se tulisi korvata [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) -paketilla. Jos kohtaat sen frontendissä:

1. Korvaa CDN-skriptitagi:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Poista `AIChatProtocolClient`-instanssi (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Korvaa `client.getStreamedCompletion(messages)` suoraan backendin striimaus-päätepisteen `fetch()`-kutsulla.
4. Korvaa `for await (const response of result)` lukemalla `for await (const chunk of readNDJSONStream(response.body))`.
5. Päivitä pääsy ominaisuuksiin `response.delta.content` / `response.error` -> `chunk.delta.content` / `chunk.error`.

---

## Tavoitteet

- Luetella kaikki Python-kutsukohdat, jotka käyttävät Chat Completions tai perinteisiä Completions Azure OpenAIta vasten.
- Ehdottaa migraatiopäivä- ja -järjestyssuunnitelma Python-koodikannalle.
- Soveltaa turvallisia, pieniä muutoksia Responses API:hin siirtymiseksi.
- Päivittää kutsujat käsittelemään Responses API:n tuloskaavion; ei taaksepäin yhteensopivia kääreitä.
- Ajaa testit/lintit; korjaa pienet siirron aikana tulleet virheet.
- Valmistele pieniä, tarkastettavia muutossarjoja ja tarjoa lopullinen yhteenveto diffeineen (älä tee committeja).

---

## Rajat

- Muuta vain tiedostoja git-työtilan sisällä. Älä koskaan kirjoita niiden ulkopuolelle.
- Älä säilytä taaksepäin yhteensopivia kääreitä; siirrä koodi uuteen API-muotoon.
- Älä jätä poisheittäviä tai siirtymäkommentteja tai varmuuskopiotiedostoja.
- Säilytä striimaussemantiikka, jos sitä on käytetty ennen; muuten käytä ei-striimaavaa tapaa.
- Pyydä hyväksyntä ennen komentojen tai verkkokutsujen suorittamista, jos olet hyväksyntätilassa.
- Älä aja `git add`/`git commit`/`git push` -komentoja; tee vain työtilan muokkauksia.

---

## Vaihe 0: Azure OpenAI -asiakkaan siirto (edellytys)

Jos koodikanta käyttää `AzureOpenAI` tai `AsyncAzureOpenAI`-konstruktoreita, siirry ensin käyttämään standardia `OpenAI` / `AsyncOpenAI`-konstruktoria. Azure-spesifiset konstruktorit on poistettu käytöstä `openai>=1.108.1`:ssä.

### Miksi v1 API-polku?

Uusi `/openai/v1` -päätepiste käyttää standardia `OpenAI()`-asiakasta `AzureOpenAI()` sijaan, ei vaadi `api_version`-parametria, ja toimii samalla tavalla sekä OpenAI:n että Azure OpenAI:n kanssa. Sama asiakaskoodi on tulevaisuuden kestävä — ei versiohallintaa tarvitse.

### Tärkeimmät muutokset

| Ennen | Jälkeen |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Poista kokonaan |

### Siivouslista

- Poista `api_version`-argumentti asiakasrakennettaessa.
- Poista ympäristömuuttujat `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` `.env`-tiedostosta, sovelluksen asetuksista ja Bicep/infra-tiedostoista.
- Nimeä `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` `.env`:ssä, sovelluksen asetuksissa, Bicep/infra-tiedostoissa ja testifixtuureissa (standard Azure Identity SDK -käytäntö).
- Varmista `openai>=1.108.1` `requirements.txt`:ssä tai `pyproject.toml`:ssa.

### Ympäristömuuttujien migrointi

| Vanha ympäristömuuttuja | Toimenpide | Huomautuksia |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Poista** | Ei `api_version`-tarvetta v1-päätepisteessä |
| `AZURE_OPENAI_API_VERSION` | **Poista** | Sama kuin yllä |
| `AZURE_OPENAI_CLIENT_ID` | **Nimeä uudelleen** → `AZURE_CLIENT_ID` | Standardi Azure Identity SDK -käytäntö `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Säilytä** | Tarvitaan edelleen `base_url`:n muodostamiseen |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Säilytä** | Käytetään `model`-parametrina `responses.create`-kutsussa |
| `AZURE_OPENAI_API_KEY` | **Säilytä** | Käytetään avainpohjaisessa autentikoinnissa `api_key`:nä |

Asiakkaan alustuskoodiesimerkkejä (synkroninen, asynkroninen, EntraID, API-avaimet, monivuokralainen) löydät [cheat-sheet.md](./references/cheat-sheet.md).

---

## Vaihe 1: Vanhojen kutsupisteiden havaitseminen

Suorita [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) skripti löytääksesi kaikki migraatiota vaativat kutsukohdat:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Tai etsi manuaalisesti — jokainen osuma on migraatiokohde:

```bash
# Perintöjärjestelmän API-kutsut (täytyy kirjoittaa uudelleen)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Vanhentuneet Azure-asiakasrakentajat (täytyy korvata)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Vastausmuodon käyttökuviot (täytyy päivittää)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Työkalumääritelmät vanhassa sisäkkäisessä muodossa (täytyy tasoittaa)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Työkalun tulokset vanhassa muodossa (täytyy muuntaa function_call_output-muotoon)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Vanhentuneet parametrit (täytyy poistaa tai nimetä uudelleen)
rg "response_format"
rg "max_tokens\b"        # nimeä uudelleen max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Vanhentuneet ympäristömuuttujat (siivota)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # pitäisi olla AZURE_CLIENT_ID

# GitHub-mallien päätepisteet (täytyy poistaa — Responses API ei tuettu)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Kehyskerroksen vanhat mallit (täytyy päivittää)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: korvaa OpenAIChatClientillä
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: tarvitsee use_responses_api=True

# Testausinfrastruktuuri (täytyy päivittää)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Sisällön suodattimen virherungon käyttö (täytyy päivittää — rakenne muuttunut)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # vanha yksikkömuoto — nyt content_filter_results (monikko) content_filters-taulukossa

# Raaka HTTP-kutsut Chat Completions -päätepisteeseen (täytyy päivittää URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Arvaukset (havaitse ja uudelleenkirjoita)

- **Chat Completions -asiakas**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure-asiakasrakentajat**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Työkalut**: muunna funktiokutsutyökalujen määritelmät sisäkkäisestä muodosta (`{"type": "function", "function": {"name": ...}}`) tasaiseksi Responses-muodoksi (`{"type": "function", "name": ...}`); käytä `tool_choice`; palauta työkalujen tulokset `{"type": "function_call_output", "call_id": ..., "output": ...}` -kohteina (ei `{"role": "tool", ...}`).
- **Työkalujen pyöräytykset**: kun malli palauttaa funktiokutsuja, lisää `response.output` -kohteet keskusteluun (ei manuaalista `{"role": "assistant", "tool_calls": [...]}` sanakirjaa), lisää sitten `function_call_output` -kohteet kunkin tuloksen osalta.
- **Esimerkit työkalun käytöstä**: jos keskustelussa on kovakoodattuja esimerkkejä työkalukutsuista, muunna ne `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` -kohteiksi. ID:t tulee aloittaa `fc_`.
- **`pydantic_function_tool()`**: tämä apufunktio tuottaa edelleen vanhaa sisäkkäistä muotoa eikä ole yhteensopiva `responses.create()` kanssa. Korvaa manuaalisilla työkalumääritelmillä tai tasoittavalla wrapperilla.
- **Monikierroksisuus**: ylläpidä keskusteluhistoriaa sovelluksessa; välitä aiemmat kierrokset `input`-kohteina.
- **Muotoilu**: korvaa Chatin päällä oleva `response_format` Responses-muodon `text.format` -muodolla. Kaanoninen muoto: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Sisältökohteet**: korvaa Chatin `content[].type: "text"` Responsesin `content[].type: "input_text"` käyttäjä-/järjestelmävuoroissa.
- **Kuvien sisältökohteet**: korvaa Chatin `content[].type: "image_url"` Responsesin `content[].type: "input_image"`. `image_url`-kenttä muuttuu sisäkkäisestä objektista `{"url": "..."}` tasaiseksi merkkijonoksi. Katso pikakäsikirjasta ennen/jälkeen -esimerkit.
- **Päätöksentekoponnistelu**: **siirrä `reasoning` vain, jos se on jo alkuperäisessä koodissa**.
- **Sisällön suodattimen virheenkäsittely**: virheen runkorakenne muuttui. Chat Completionit käyttivät `error.body["innererror"]["content_filter_result"]` (yksikköinen); Responses API käyttää `error.body["content_filters"][0]["content_filter_results"]` (monikossa, taulukon sisällä). Koodi, joka käyttää `innererror`, aiheuttaa `KeyError`-poikkeuksen. Kirjoita uudelleen käyttämään uutta polkua.
- **Raakad HTTP-kutsut**: jos sovellus kutsuu Azure OpenAI REST API:a suoraan (käyttäen esim. `requests`, `httpx`) polulla `/openai/deployments/{name}/chat/completions?api-version=...`, muunna poluksi `/openai/v1/responses`. Pyynnön runko muuttuu: `messages` → `input`, lisätään `max_output_tokens` ja `store: false`, poistetaan `api-version` kyselyparametri. Vastauksen runko muuttuu: `choices[0].message.content` → `output[0].content[0].text` (huomaa: `output_text` on SDK:n mukavuusominaisuus, jota ei ole raakapalvelimen JSON:ssa).

---

## Vaihe 2: Käytä migraatiota

### Migraatiomuistiinpanot (Chat Completions → Responses)

- **Miksi migratoida**: Responses on yhtenäinen API tekstille, työkaluilla ja suoratoistolle; Chat Completions on vanhentunut. GPT-5:n kanssa Responses vaaditaan parhaan suorituskyvyn takaamiseksi.
- **HTTP**: Azure-päätepiste vaihtuu `/openai/deployments/{name}/chat/completions` → `/openai/v1/responses`.
- **Kentät**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` pysyy ennallaan.
- **Muotoilu**: `response_format` → `text.format` asianmukaisessa objektissa.
- **Sisältökohteet**: korvaa Chatin `content[].type: "text"` Responsesin `content[].type: "input_text"` järjestelmä/käyttäjä-vuoroissa.
- **Kuvien sisältökohteet**: korvaa Chatin `content[].type: "image_url"` Responsesin `content[].type: "input_image"`. Tasoita `image_url`-kenttä muodosta `{"image_url": {"url": "..."}}` muotoon `{"image_url": "..."}` (tavallinen merkkijono – joko HTTPS URL tai `data:image/...;base64,...`-tietourli).

### Parametrien vastaavuustaulukko

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (taulukko kohteita) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekti) |
| `temperature` | `temperature` (muuttumaton) |
| `stop` | `stop` (muuttumaton) |
| `frequency_penalty` | `frequency_penalty` (muuttumaton) |
| `presence_penalty` | `presence_penalty` (muuttumaton) |
| `tools` / funktiokutsut | `tools` (muuttumaton) |
| `seed` | **Poista** (ei tuettu) |
| `store` | `store` (asetettu arvoon `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (tasainen merkkijono) |

Täydellisiin koodi-esimerkkeihin ennen/jälkeen katso [cheat-sheet.md](./references/cheat-sheet.md).

Testausinfrastruktuurin migraatioon (mokkaukset, tallenteet, varmistukset) katso [test-migration.md](./references/test-migration.md).

Vianetsintään liittyen, katso [troubleshooting.md](./references/troubleshooting.md).

---

## Datan säilytys ja tila

- Aseta `store: false` kaikissa Responses-pyynnöissä.
- Älä perusta aiempiin viesti-ID:hin tai palvelimen säilyttämään kontekstiin; pidä tila asiakkaan hallinnassa ja minimoi metatiedot.

---

## Hyväksymiskriteerit

### Kooditason portit (kaikki täytyy läpäistä)

- [ ] Ei yhtään osumaa haulla `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` migroiduissa tiedostoissa.
- [ ] Ei yhtään osumaa haulla `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` – kaikki rakentajat käyttävät `OpenAI`/`AsyncOpenAI` v1-päätepisteellä.
- [ ] Ei yhtään osumaa haulla `rg "models\.github\.ai|models\.inference\.ai\.azure"` – GitHub-mallipolut poistettu.
- [ ] Ei yhtään osumaa haulla `rg "OpenAIChatCompletionClient"` – MAF 1.0.0+ koodi käyttää `OpenAIChatClient`-luokkaa (joka käyttää Responses API:ta). Ennen 1.0.0 versiota päivitä `agent-framework-openai>=1.0.0`:ään.
- [ ] Kaikki `ChatOpenAI(...)`-kutsut sisältävät `use_responses_api=True`.
- [ ] Ei yhtään osumaa haulla `rg "choices\[0\]"` – kaikki vastauksen käyttö käyttää `resp.output_text` tai Responsesin ulostulon skeemaa.
- [ ] Ei `response_format` korkeimmalla tasolla; kaikki jäsennelty ulostulo käyttää `text={"format": {...}}`.
- [ ] `openai>=1.108.1` ja `azure-identity` `requirements.txt`- tai `pyproject.toml`-tiedostoissa; riippuvuudet asennettu uudelleen.
- [ ] `store=False` asetettu kaikissa `responses.create` -kutsussa.
- [ ] Ei `api_version` asiakasrakentamisessa; `AZURE_OPENAI_API_VERSION` poistettu ympäristömuuttujista ja infrasta.

### Testausinfrastruktuurin portit (kaikki täytyy läpäistä)

- [ ] Ei yhtään osumaa haulla `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Ei yhtään osumaa haulla `rg "_azure_ad_token_provider" tests/` – varmennukset päivitetty tarkistamaan `isinstance(client, AsyncOpenAI)` tai `base_url`.
- [ ] Ei yhtään osumaa haulla `rg "prompt_filter_results|content_filter_results" tests/` – Azure-spesifiset suodatinmokat poistettu.
- [ ] Mokkien fixturet käyttävät `kwargs.get("input")`, eivät `kwargs.get("messages")`.
- [ ] Tallenne / golden-tiedostot päivitetty Responsesin suoratoistomuotoon (ei `choices[0]`, `function_call`, `logprobs` jne.).
- [ ] `pytest` läpäisee ilman virheitä kaikkien testipäivitysten jälkeen.

### Käyttäytymisen portit (tarkista manuaalisesti tai testiohjelmalla)

- [ ] **Perusvalmius**: ei-suoratoistava `responses.create` palauttaa ei-tyhjän `output_text`:in.
- [ ] **Suoratoiston yhtenevyys**: jos alkuperäinen koodi käytti suoratoistoa, migroidun koodin suoratoisto toimii ja palauttaa `response.output_text.delta` -tapahtumia, joissa on ei-tyhjiä osia.
- [ ] **Jäsennelty ulostulo**: jos käytössä on `text.format` `json_schema`lla, `json.loads(resp.output_text)` onnistuu ja vastaa skeemaa.
- [ ] **Työkalukutsusilmukka**: jos työkaluja käytetään, malli tekee työkalukutsuja, sovellus suorittaa niitä, ja seuraava pyyntö palauttaa lopullisen `output_text`:in (ei ikuista silmukkaa).
- [ ] **Async-yhtenevyys**: jos `AsyncAzureOpenAI` oli käytössä, `AsyncOpenAI`-vastaava toimii `await`-avainsanalla.
- [ ] **Virheiden määrä**: ei uusia 400/401/404-virheitä verrattuna migraatiota edeltävään tasoon.

### Toimitukset

- Yhteenveto sisältää muutetut tiedostot, ennen/jälkeen lukumäärän vanhoista kutsupaikoista sekä jatkotoimenpiteet.
- Muutokset ovat vain työpuun muokkauksia (ei committeja).

---

## SDK-versioiden vaatimukset

| Paketti | Vähimmäisversio |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Uusin (EntraID-todennukseen) |

---

## Viitteet

- [Pikakäsikirja — kaikki koodikatkelmat](./references/cheat-sheet.md)
- [Testimigraatio — mokit, tallenteet, varmennukset](./references/test-migration.md)
- [Vianetsintä — virheet, riskitaulukko, sudenkuopat](./references/troubleshooting.md)
- [detect_legacy.py — automaattinen skanneri](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Aloituspaketti](https://aka.ms/openai/start)
- [Azure OpenAI Responses API -dokumentaatio](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API -version elinkaaritiedot](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API -viite](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->