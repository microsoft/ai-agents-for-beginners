---
name: azure-openai-to-responses
license: MIT
---
# Siirrä Python-sovellukset Azure OpenAI Chat Completions -palvelusta Responses API:in

> **VIRALLINEN OHJEISTUS — NOUDATA TARKKAASTI**
>
> Tämä taito siirtää Python-koodikantoja, jotka käyttävät Azure OpenAI Chat Completions -palvelua
> yhtenäistetylle Responses API:lle. Noudata näitä ohjeita täsmällisesti.
> Älä improvisoi parametristojen tulkintaa tai keksi API:n muotoja.

---

## Laukaisijat

Aktivoi tämä taito, kun käyttäjä haluaa:
- Siirtää Python-sovelluksen Azure OpenAI Chat Completions -palvelusta Responses API:in
- Päivittää Python OpenAI SDK:n uusimpaan API-muotoon Azure OpenAI -ympäristössä
- Valmistella Python-koodi GPT-5- tai uudempia malleja varten, jotka vaativat Responses-rajapinnan Azuren kautta
- Vaihtaa `AzureOpenAI`/`AsyncAzureOpenAI` standardiin `OpenAI`/`AsyncOpenAI` asiakasohjelmaan v1-päätepisteellä
- Korjata käytöstäpoistovaroitukset, jotka liittyvät `AzureOpenAI`-konstruktoreihin tai `api_version`-parametriin

---

## ⚠️ Malliyhteensopivuus — TARKISTA ENSIN

> **Ennen siirtämistä varmista, että Azure OpenAI -ympäristösi tukee Responses API:a.**

### 1. Testaa pikaisesti ympäristösi (nopein tapa)

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

> **Huom:** Azure OpenAI:ssa `max_output_tokens` on **vähintään 16**. Alle 16 arvot palauttavat 400-virheen. Käytä 50+ arvoa pikakokeissa.

Jos tämä palauttaa 404:n, käyttämäsi mallin tuki Responsesille ei ole vielä saatavilla — tarkista alla oleva viite tai ota käyttöön tuettu malli uudelleen.

### 2. Tarkista alueellasi saatavilla olevat mallit (suositeltu)

Suorita sisäänrakennettu malliyhteensopivuutta testaava työkalu nähdäksesi, mitä Responses API tukee juuri omalla alueellasi:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Tämä tekee live-kyselyn Azure ARM:iin ja näyttää yhteensopivuusmatriisin — mitkä mallit tukevat Responsesia, rakenteellista outputtia, työkaluja jne. Käytä `--filter gpt-5.1,gpt-5.2` rajataksesi tuloksia tai `--json` skriptaamiseen.

### 3. Kattava mallituen viite

- **Live-kysely**: `python migrate.py models` (katso yllä — aina aluekohtainen ja ajan tasalla)
- **Selaa saatavuutta**: [Mallien yhteenvetotaulukko ja alueelliset saatavuudet](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Pikakäynnistys & ohjeistus**: **https://aka.ms/openai/start**

### ⚠️ Vanhempien mallien rajoitukset

> **VAROITUS**: Vanhemmat mallit (esim. `gpt-4o`, `gpt-4`) eivät välttämättä tue kaikkia Responses API:n ominaisuuksia täydellisesti.
>
> Tunnetut rajaukset vanhemmilla malleilla:
> - **`reasoning`-parametri**: Ei tuettu `gpt-4o-mini`, `gpt-4o` ja monilla ei-pohjautuvilla malleilla. Siirrä `reasoning`-parametri vain, jos se oli jo alkuperäisessä koodissa.
> - **`seed`-parametri**: Ei tuettu Responses API:ssa lainkaan — poista kaikista pyynnöistä.
> - **Rakenteellinen output `text.format`:lla**: Vanhemmat mallit eivät välttämättä luotettavasti vaadi `strict: true` JSON-skeemoja.
> - **Työkalujen ohjaus**: GPT-5+ ohjaa työkalukutsuja osana sisäistä päättelyä. Vanhemmat Response-mallit toimivat edelleen mutta eivät tätä syvää integraatiota.
> - **Lämpötilarajoitukset**: Kun siirrytään `gpt-5`-malliin, lämpötila jätettävä pois tai asetettava arvoon `1`. Vanhemmilla malleilla ei tätä rajoitusta ole.

### O-sarjan päättelymallit (o1, o3-mini, o3, o4-mini)

O-sarjan malleilla on omat parametrierot huomioitava. Kun siirrät sovelluksia, jotka käyttävät o-sarjan malleja:

- **`temperature`**: Täytyy olla `1` (tai poissa). O-sarjan mallit eivät hyväksy muita arvoja.
- **`max_completion_tokens` → `max_output_tokens`**: Azure-spesifisiä `max_completion_tokens`-käyttöjä tulee vaihtaa `max_output_tokens`-parametriin. Aseta korkeat arvot (4096+) koska päättelyyn käytetyt tokenit rajaavat määrää.
- **`reasoning_effort`**: Jos sovellus käyttää `reasoning_effort` (low/medium/high), säilytä se — Responses API tukee sitä o-sarjan malleissa.
- **Striimauskäyttäytyminen**: O-mallit voivat tallentaa outputin kunnes päättely on valmis ennen tekstin delta-tapahtumia. Striimaus toimii edelleen, mutta ensimmäinen `response.output_text.delta` voi viivästyä pidempään kuin GPT-malleilla.
- **`top_p`**: Ei tuettu o-sarjassa — poista jos on käytössä.
- **Työkalujen käyttö**: O-sarjan mallit tukevat työkaluja Responses API:n kautta kuten GPT-mallit, mutta työkalukutsujen ohjauksen laatu vaihtelee mallikohtaisesti.

**Toimenpide — ennakoiva mallineuvonta**: Skannausvaiheessa tarkista, mitä mallia sovellus käyttää (käyttöönottojen nimet, ympäristömuuttujat, konfiguraatio). Jos malli on `gpt-4o` tai vanhempi (ei gpt-4.1+), kerro käyttäjälle:
- Siirto toimii perus tekstin, chatin, striimauksen ja työkalujen osalta sille mallille.
- Uudemmat mallit (`gpt-5.1`, `gpt-5.2`) tarjoavat paremman työkalujen ohjauksen, rakenteisen outputin vaatimuksen, päättelyn ja alueiden välisen saatavuuden.
- Heidän kannattaa harkita päivitystä käyttöönsä, kun se sopii — päivitys ei ole migraation este.

Älä estä tai kieltäydy siirrosta malliversion perusteella. Neuvonta on informatiivista.

### GitHub-mallit EIVÄT tue Responses API:a

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ei tue Responses API:a.**

Jos koodipohjassa on GitHub Models -koodireitti (etsi `base_url` osoittamaan `models.github.ai` tai `models.inference.ai.azure.com`), **poista se kokonaan** migraation yhteydessä. Responses API vaatii Azure OpenAI:n, OpenAI:n tai yhteensopivan paikallisen päätepisteen (esim. Ollama) tuen.

Toimenpide skannauksen aikana:
- Merkitse kaikki GitHub Models -koodireitit poistettaviksi.

---

## Kehyksen migraatio

Monet sovellukset käyttävät OpenAI:n päällä korkeampia kehyksiä. Migroitaessa näitä, kehysmuutokset ovat API-pinnan muutoksia — eivät vain perustason OpenAI-kutsujen.

### Microsoft Agent Framework (MAF)

**Tarkista ensin MAF-versiosi** — migraatio riippuu siitä, onko versiosi MAF 1.0.0+ vai ennen 1.0.0 beta/rc-versio.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **käyttää jo Responses API:a** — migraatiota ei tarvita. Jos koodissa on perinteinen `OpenAIChatCompletionClient` (joka käyttää `chat.completions.create`), vaihda se `OpenAIChatClient`-luokkaan.

| Ennen | Jälkeen |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Tarkista versio komennolla: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc -julkaisut)

Pre-1.0.0-versiossa `OpenAIChatClient` käytti Chat Completions -palvelua. Päivitä versioon `agent-framework-openai>=1.0.0`, jossa `OpenAIChatClient` käyttää oletuksena Responses API:a.

Muita muutoksia ei tarvita — `Agent` ja työkalujen API:t säilyvät ennallaan.

### LangChain (`langchain-openai`)

Lisää `use_responses_api=True` `ChatOpenAI()`-kutsuun. Päivitä myös vastausten käyttö `.content`-kentästä `.text`-kenttään.

| Ennen | Jälkeen |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Täydellisiä esimerkkejä ennen/jälkeen koodista on [cheat-sheet.md](./references/cheat-sheet.md) tiedostossa.

---

## Frontend-migraatio-ohjeet

> **Responses API on palvelinpuolen asia.** Siirrä Python-taustapalvelimesi — frontendin HTTP-sopimus ei saa muuttua, ellei taustapalvelimesi ole pelkkä ohituskerros — tällöin harkitse Responses-pyynnön muodon käyttöönottoa kääntämiskerroksen poistamiseksi. Jos frontend kutsuu OpenAI:ta suoraan asiakaspuolen avaimella, siirrä nämä kutsut ensin taustapalvelimelle.

### `@microsoft/ai-chat-protocol` käytöstä poistettu

`@microsoft/ai-chat-protocol` npm-paketti on käytöstä poistettu ja se tulisi korvata paketin [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) avulla. Jos kohtaat sen frontendissä:

1. Korvaa CDN-skripti:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Poista `AIChatProtocolClient`-instanssi (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Korvaa `client.getStreamedCompletion(messages)` suoralla `fetch()`-kutsulla backendin striimauspäätepisteeseen.
4. Korvaa `for await (const response of result)` muotoon `for await (const chunk of readNDJSONStream(response.body))`.
5. Päivitä ominaisuuksien käyttö muotoon `response.delta.content` / `response.error` → `chunk.delta.content` / `chunk.error`.

---

## Tavoitteet

- Listaa kaikki Python-kutsupaikat, jotka käyttävät Chat Completions tai vanhaa Completions-rajapintaa Azure OpenAI:ta vastaan.
- Ehdota siirtosuunnitelmaa ja suoritustapaa Python-koodikannalle.
- Tee turvallisia, minimaalisia muutoksia siirtymiseksi Responses API:in.
- Päivitä kutsujat käsittelemään Responsesin mallin mukaisia vastauksia; älä tee taaksepäin yhteensopivia kuoria.
- Aja testit ja linttaukset; korjaa migraation aiheuttamat pienet rikkinäisyydet.
- Valmistele pieniä, tarkistettavia muutospaketteja ja tarjoa lopuksi yhteenveto diffien kera (älä tee sitoumuksia).

---

## Suojakaiteet

- Muokkaa vain tiedostoja, jotka ovat git-työtilan sisällä. Älä koskaan kirjoita sen ulkopuolelle.
- Älä säilytä vanhaan yhteensopivuutta tekevää koodia; siirrä koodi uuteen API-muotoon.
- Älä jätä hautakivi-/siirtymäkommentteja tai varmuuskopioita.
- Säilytä striimaussemantiikka, jos sitä aiemmin käytettiin; muuten käytä ei-striimaavaa toimintoa.
- Pyydä hyväksyntää ennen komentojen tai verkkokutsujen suorittamista, jos olet hyväksymistilassa.
- Älä aja `git add`/`git commit`/`git push` komentoja; tee vain työtilamuokkauksia.

---

## Vaihe 0: Azure OpenAI -asiakkaan migraatio (esivaatimus)

Jos koodipohja käyttää `AzureOpenAI` tai `AsyncAzureOpenAI` -konstruktoreita, siirry ensin käyttämään standardia `OpenAI` / `AsyncOpenAI` -konstruktoria. Azuren spesifiset konstruktorit ovat käytöstä poistetut `openai>=1.108.1`:ssä.

### Miksi v1 API-päätepiste?

Uusi `/openai/v1` -päätepiste käyttää standardia `OpenAI()`-asiakasta `AzureOpenAI()` sijaan, ei tarvitse `api_version`-parametria ja toimii samoin sekä OpenAI:ssa että Azure OpenAI:ssa. Sama asiakas on tulevaisuuden kestävä — versioiden hallintaa ei tarvita.

### Keskeiset muutokset

| Ennen | Jälkeen |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Poista kokonaan |

### Siivouslista

- Poista `api_version`-argumentti asiakasolion rakentamisesta.
- Poista `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` ympäristömuuttujat `.env`, sovellusasetuksista ja Bicep/infra-tiedostoista.
- Nimeä `AZURE_OPENAI_CLIENT_ID` uudelleen → `AZURE_CLIENT_ID` `.env`-tiedostossa, sovellusasetuksissa, Bicep/infra ja testifiksatuureissa (standardia Azure Identity SDK -käytäntöä).
- Varmista, että `openai>=1.108.1` on `requirements.txt` tai `pyproject.toml` tiedostossa.

### Ympäristömuuttujien migraatio

| Vanha ym. muuttuja | Toimenpide | Huomautukset |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Poista** | Ei tarvita `api_version` v1-päätepisteellä |
| `AZURE_OPENAI_API_VERSION` | **Poista** | Sama kuin yllä |
| `AZURE_OPENAI_CLIENT_ID` | **Nimeä uudelleen** → `AZURE_CLIENT_ID` | Standardi Azure Identity SDK -käytäntö `ManagedIdentityCredential(client_id=...)`-parametrille |
| `AZURE_OPENAI_ENDPOINT` | **Pidä** | Tarpeen edelleen `base_url`-rakennukseen |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Pidä** | Käytetään `model`-parametrina `responses.create`-kutsuissa |
| `AZURE_OPENAI_API_KEY` | **Pidä** | Käytetään `api_key`-tunnuksena avaintunnistukseen |

Asiakkaan asennusesimerkit (synkroniset, asynkroniset, EntraID, API-avain, multi-tenant) löytyvät [cheat-sheet.md](./references/cheat-sheet.md) tiedostosta.

---

## Vaihe 1: Havaitse vanhentuneet kutsupaikat

Suorita [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) skrypti löytääksesi kaikki migraatiota tarvitsevat kutsupaikat:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Tai suorita seuraavat haut manuaalisesti — jokainen osuma on migraation kohde:

```bash
# Perintö-API-kutsut (täytyy kirjoittaa uudelleen)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Vanhentuneet Azure-asiakasrakentajat (täytyy korvata)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Vastausrakenteen käyttömallit (täytyy päivittää)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Työkalumääritelmät vanhassa sisäkkäisessä muodossa (täytyy tasoittaa)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Työkalujen tulokset vanhassa muodossa (täytyy muuntaa function_call_output-muotoon)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Vanhentuneet parametrit (täytyy poistaa tai nimetä uudelleen)
rg "response_format"
rg "max_tokens\b"        # nimeä uudelleen max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Vanhentuneet ympäristömuuttujat (siivoa)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # pitäisi olla AZURE_CLIENT_ID

# GitHub Models -päätepisteet (täytyy poistaa — Responses API ei tuettu)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Kehyskohtaiset perintömallit (täytyy päivittää)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: korvaa OpenAIChatClientilla
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: tarvitsee use_responses_api=True

# Testausinfrastruktuuri (täytyy päivittää)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Sisältösuodattimen virheen rungon käyttö (täytyy päivittää — rakenne muuttunut)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # vanha yksikkömuoto — nyt content_filter_results (monikko) content_filters-taulukon sisällä

# Raakat HTTP-kutsut Chat Completions -päätepisteeseen (täytyy päivittää URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristiikat (havainto ja uudelleenkirjoitus)

- **Chat Completions -asiakas**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure-asiakasluokat**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Työkalut**: muunna funktiokutsutyökalujen määritelmät sisäkkäisestä muodosta (`{"type": "function", "function": {"name": ...}}`) tasaiseksi Responses-muodoksi (`{"type": "function", "name": ...}`); käytä `tool_choice`; palauta työkalun tulokset kohteina `{"type": "function_call_output", "call_id": ..., "output": ...}` (ei `{"role": "tool", ...}`).
- **Työkalujen edestakainen käsittely**: kun malli palauttaa funktiokutsuja, lisää `response.output` -kohteet keskusteluun (ei manuaalisesti `{"role": "assistant", "tool_calls": [...]}`-sanakirjana), ja lisää sitten `function_call_output` -kohteet kunkin tuloksen kohdalla.
- **Muistisääntötyökaluesimerkit**: jos keskustelu sisältää kovakoodattuja työkalukutsu-esimerkkejä, muunna ne `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` -kohteiksi. Tunnisteiden tulee alkaa `fc_`.
- **`pydantic_function_tool()`**: tämä apuohjelma tuottaa edelleen vanhan sisäkkäisen muodon ja on **yhteensopimaton** `responses.create()` kanssa. Korvaa manuaalisilla työkalumääritelmillä tai tasoittavalla wrapperilla.
- **Monimutkaiset vuorotukset**: ylläpidä keskusteluhistoriaa sovelluksessa; välitä edelliset vuorot `input`-kohteiden kautta.
- **Muotoilu**: korvaa Chatin ylimmän tason `response_format` Responsesin `text.format` -kentällä. Kanoninen rakenne: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Sisältökohteet**: korvaa Chatin `content[].type: "text"` Responsesin `content[].type: "input_text"` -tyypillä käyttäjä-/järjestelmävuoroissa.
- **Kuvien sisältökohteet**: korvaa Chatin `content[].type: "image_url"` Responsesin `content[].type: "input_image"` -tyypillä. `image_url`-kenttä muuttuu sisäkkäisestä objektista `{"url": "..."}` tasaiseksi merkkijonoksi. Katso tiivistelmä ennen/jälkeen-esimerkeistä.
- **Perustelupyrkimys**: **siirrä `reasoning` vain, jos se on jo alkuperäisessä koodissa**.
- **Sisällön suodatusvirheiden käsittely**: virherunko muuttui. Chat Completions käytti `error.body["innererror"]["content_filter_result"]` (yksikkö); Responses API käyttää `error.body["content_filters"][0]["content_filter_results"]` (monikko, taulukon sisällä). Koodi, joka käyttää `innererror`-kenttää, heittää `KeyError`-poikkeuksen. Kirjoita uudelleen käyttämään uutta polkua.
- **Raakana HTTP-kutsut**: jos sovellus kutsuu Azure OpenAI REST API:ta suoraan (`requests`, `httpx` tms.) käyttöliittymällä `/openai/deployments/{name}/chat/completions?api-version=...`, muunna kutsut `/openai/v1/responses`:ksi. Pyynnön runko muuttuu: `messages` → `input`, lisää `max_output_tokens` ja `store: false`, poista `api-version`-kyselyparametri. Vastausrakenne muuttuu: `choices[0].message.content` → `output[0].content[0].text` (huom: `output_text` on SDK-optiokäytännön ominaisuus, jota ei ole raakassa REST JSON:ssa).

---

## Vaihe 2: Käytä migraatiota

### Migraatiomuistiinpanot (Chat Completions → Responses)

- **Miksi migroida**: Responses on yhdistetty API tekstiä, työkaluja ja suoratoistoa varten; Chat Completions on vanhentunut. GPT-5:n kanssa Responses on vaatimus parhaalle suorituskyvylle.
- **HTTP**: Azure-päätepiste vaihtuu osoitteesta `/openai/deployments/{name}/chat/completions` osoitteeseen `/openai/v1/responses`.
- **Kentät**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` pysyy ennallaan.
- **Muotoilu**: `response_format` → `text.format` asianmukaisella objektilla.
- **Sisältökohteet**: korvaa Chatin `content[].type: "text"` Responsesin `content[].type: "input_text"` -tyypillä järjestelmä-/käyttäjävuoroissa.
- **Kuvien sisältökohteet**: korvaa Chatin `content[].type: "image_url"` Responsesin `content[].type: "input_image"` -tyypillä. Muuta `image_url`-kenttämuoto `{"image_url": {"url": "..."}}` tasaiseksi muodoksi `{"image_url": "..."}` (pelkkä merkkijono — joko HTTPS-URL tai `data:image/...;base64,...` data-URI).

### Parametrien vastaavuustaulukko

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (taulukko kohteista) |
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

Täydelliset ennen/jälkeen-koodiesimerkit löytyvät tiedostosta [cheat-sheet.md](./references/cheat-sheet.md).

Testausinfrastruktuurin migraation (mokkit, snapshotit, toteamukset) ohjeet löytyvät tiedostosta [test-migration.md](./references/test-migration.md).

Virheenkorjausohjeet ja ongelmatilanteiden taulukot löytyvät tiedostosta [troubleshooting.md](./references/troubleshooting.md).

---

## Datan säilytys ja tila

- Aseta `store: false` kaikkiin Responses-pyyntöihin.
- Älä luota aiempiin viestitunnuksiin tai palvelimella säilytettyyn kontekstiin; pidä tila asiakashallintaisena ja minimoi metadata.

---

## Hyväksymiskriteerit

### Kooditason portit (kaikkien tulee mennä läpi)

- [ ] Ei yhtään osumaa haulla `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` migroiduissa tiedostoissa.
- [ ] Ei yhtään osumaa haulla `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — kaikki rakentajat käyttävät `OpenAI`/`AsyncOpenAI` v1-päätepistettä.
- [ ] Ei yhtään osumaa haulla `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub-mallien koodipolut poistettu.
- [ ] Ei yhtään osumaa haulla `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ koodi käyttää `OpenAIChatClient` (joka käyttää Responses API:ta). Versioissa ennen 1.0.0 päivitä `agent-framework-openai>=1.0.0`.
- [ ] Kaikkien `ChatOpenAI(...)` kutsujen mukana on `use_responses_api=True`.
- [ ] Ei yhtään osumaa haulla `rg "choices\[0\]"` — kaikki vastausten käsittelyt käyttävät `resp.output_text` tai Responsesin vastausrakennetta.
- [ ] Ylätasolla ei ole `response_format`-kenttää; kaikki jäsennelty output käyttää `text={"format": {...}}`.
- [ ] `openai>=1.108.1` ja `azure-identity` ovat `requirements.txt`ssä tai `pyproject.toml`:ssa; riippuvuudet on asennettu uudelleen.
- [ ] `store=False` on asetettu jokaisessa `responses.create`-kutsussa.
- [ ] Asiakasluonnissa ei ole `api_version`-määritystä; `AZURE_OPENAI_API_VERSION` on poistettu ympäristömuuttujista ja infrasta.

### Testausinfrastruktuurin portit (kaikkien tulee mennä läpi)

- [ ] Ei yhtään osumaa haulla `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Ei yhtään osumaa haulla `rg "_azure_ad_token_provider" tests/` — toteamukset päivitetty tarkistamaan `isinstance(client, AsyncOpenAI)` tai `base_url`.
- [ ] Ei yhtään osumaa haulla `rg "prompt_filter_results|content_filter_results" tests/` — Azure-spesifiset suodatinmokkit poistettu.
- [ ] Mokkien konfiguraatio käyttää `kwargs.get("input")` eikä `kwargs.get("messages")`.
- [ ] Snapshotit / kultaiset tiedostot päivitetty Responsesin suoratoistorakenteeseen (ei `choices[0]`, `function_call`, `logprobs` ym.).
- [ ] `pytest` läpäisee ilman virheitä kaikkien testipäivitysten jälkeen.

### Käyttäytymisen portit (tarkasta manuaalisesti tai testiharsolla)

- [ ] **Peruskompletio**: ei-suoratoistava `responses.create` palauttaa ei-tyhjän `output_text` -kentän.
- [ ] **Suoratoistotasa-arvo**: jos alkuperäinen koodi käytti suoratoistoa, migroitu koodi suoratoistaa ja tuottaa `response.output_text.delta` -tapahtumia ei-tyhjillä delta-tiedoilla.
- [ ] **Jäsennelty output**: jos käytetään `text.format` jäsentämisellä `json_schema` mukaan, `json.loads(resp.output_text)` onnistuu ja vastaa skeemaa.
- [ ] **Työkalukutsusilmukka**: jos työkaluja käytetään, malli tekee työkalukutsuja, sovellus suorittaa ne ja seuraava pyyntö palauttaa lopullisen `output_text` (ei loputonta silmukkaa).
- [ ] **Async-tasa-arvo**: jos käytössä oli `AsyncAzureOpenAI`, vastaava `AsyncOpenAI` toimii `await`-kutsuilla.
- [ ] **Virhesuhde**: ei uusia 400/401/404 virheitä verrattuna migraatiota edeltävään tilaan.

### Toimitukset

- Yhteenveto sisältää muokatut tiedostot, ennen/jälkeen-lukemat perintöisen koodin kutsuista ja seuraavat askeleet.
- Muutokset ovat vain työpuun muokkauksia (ei commiteja).

---

## SDK-version vaatimukset

| Paketti | Vähimmäisversio |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Uusin (EntraID-authentikointia varten) |

---

## Viitteet

- [Muistisääntö — kaikki koodikatkelmat](./references/cheat-sheet.md)
- [Testin migraatio — mokkit, snapshotit, toteamukset](./references/test-migration.md)
- [Virheenkorjaus — virheet, riskitaulukko, ansat](./references/troubleshooting.md)
- [detect_legacy.py — automatisoitu skanneri](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentaatio](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API-version elinkaaritiedot](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API viite](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->