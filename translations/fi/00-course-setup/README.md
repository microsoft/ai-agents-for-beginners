# Kurssin Asetus

## Johdanto

Tässä oppitunnissa käsitellään, miten tämän kurssin koodiesimerkit suoritetaan.

## Liity Muiden Oppijoiden Seuraan ja Hanki Apua

Ennen kuin alat kloonata omaa repoa, liity [AI Agents For Beginners Discord -kanavalle](https://aka.ms/ai-agents/discord) saadaksesi apua asennuksessa, kysyäksesi kurssiin liittyviä asioita tai yhdistääksesi muihin oppijoihin.

## Kloonaa tai Haarukoi Tämä Repo

Aloita kloonaamalla tai haarukoimalla GitHub-repositorio. Tämä luo oman version kurssimateriaalista, jotta voit suorittaa, testata ja muokata koodia!

Tämä onnistuu klikkaamalla linkkiä <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">haarakoi repo</a>

Sinulla pitäisi nyt olla oma haarautunut versio tästä kurssista seuraavan linkin kautta:

![Haarautettu Repo](../../../translated_images/fi/forked-repo.33f27ca1901baa6a.webp)

### Pinnallinen Klooni (suositeltu työpajoihin / Codespaces)

  >Koko repositorio voi olla suuri (~3 GB) kun lataat koko historian ja kaikki tiedostot. Jos osallistut vain työpajaan tai tarvitset vain muutaman oppitunnin kansion, pinnallinen klooni (tai harvinainen klooni) välttelee suurimman osan tuosta latauksesta katkaisemalla historian ja/tai ohittamalla blobit.

#### Nopea pinnallinen klooni — minimihistoria, kaikki tiedostot

Korvaa `<your-username>` alla komennoissa haarukointisi URL-osoitteella (tai upstream-URL:llä, jos haluat).

Kloonaa vain viimeisin commit-historia (pieni lataus):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Kloonaa tietty haara:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osittainen (harvinainen) klooni — minimiblogit + vain valitut kansiot

Tämä käyttää osittaista kloonausta ja sparse-checkoutia (vaatii Git 2.25+ ja suositellaan modernia Gitiä osittaisen kloonauksen tuella):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Siirry repokansioon:

```bash|powershell
cd ai-agents-for-beginners
```

Määritä sitten mitkä kansiot haluat (esimerkki näyttää kaksi kansiota):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Kloonaamisen ja tiedostojen varmistamisen jälkeen, jos tarvitset vain tiedostot etkä historiaa, poista repositorion metatiedot (💀 peruuttamatonta — menetät kaiken Gitin toiminnallisuuden: ei committeja, pullauksia, pushauksia tai historian käyttöä).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespacesin Käyttö (suositeltu välttämään suuria paikallisia latauksia)

- Luo uusi Codespace tälle repolle [GitHubin UI:n](https://github.com/codespaces) kautta.

- Ajossa uuden codespacen terminaalissa suorita jokin yllä olevista pinnallisista/harvoista kloonauskomennoista, niin saat vain tarvitut oppituntikansiot Codespace-työtilaan.
- Valinnainen: kloonauksen jälkeen Codespacessa poista .git vapauttaaksesi tilaa (katso poistokäskyt yllä).
- Huom: Jos haluat avata repoon suoraan Codespacessa (ilman ylimääräistä kloonausta), ole tietoinen, että Codespaces rakentaa devcontainer-ympäristön ja saattaa silti ladata enemmän kuin tarvitset. Pinnallisen kopion kloonaaminen tuoreeseen Codespaceen antaa sinulle enemmän hallintaa levykäyttöön.

#### Vinkkejä

- Vaihda aina kloonaus-URL omaan haarukkoosi, jos haluat tehdä muokkauksia/committeja.
- Jos myöhemmin tarvitset enemmän historiaa tai tiedostoja, voit hakea ne tai säätää sparse-checkoutia sisältämään lisää kansioita.

## Koodin Suorittaminen

Tämä kurssi tarjoaa sarjan Jupyter-muistikirjoja, joita voit käyttää käytännön kokemuksen saamiseksi tekoälyagenttien rakentamisesta.

Koodiesimerkit käyttävät **Microsoft Agent Frameworkia (MAF)** `FoundryChatClient`-asiakkaalla, joka yhdistää **Microsoft Foundry Agent Service V2**:een (Responses API) Microsoft Foundryn kautta.

Kaikki Python-muistikirjat on nimetty muotoon `*-python-agent-framework.ipynb`.

## Vaatimukset

- Python 3.12+
  - **HUOM:** Jos sinulla ei ole Python3.12 asennettuna, varmista että asennat sen. Luo sitten venv käyttämällä python3.12 varmistaaksesi, että vaaditut versiot asennetaan requirements.txt-tiedostosta.
  
    >Esimerkki

    Luo Python-venv-kansio:

    ```bash|powershell
    python -m venv venv
    ```

    Aktivoi sitten venv-ympäristö:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET-koodiesimerkkejä varten, varmista että asennat [.NET 10 SDK:n](https://dotnet.microsoft.com/download/dotnet/10.0) tai sitä uudempaa. Tarkista sitten asennettu SDK-versio:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Tarvitaan autentikointiin. Asenna osoitteesta [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-tilaus** — Microsoft Foundryn ja Microsoft Foundry Agent Servicen käyttöä varten.
- **Microsoft Foundry -projekti** — Projekti, johon on otettu käyttöön malli (esim. `gpt-5-mini`). Katso [Vaihe 1](#vaihe-1-luo-microsoft-foundry-projekti) alla.

Repositorion juuressa on mukana `requirements.txt`, joka sisältää kaikki Python-paketit, joita tarvitset koodiesimerkkien suorittamiseen.

Asenna ne suorittamalla seuraava komento terminaalissasi repositorion juuressa:

```bash|powershell
pip install -r requirements.txt
```

Suosittelemme Python-virtuaaliympäristön luomista ristiriitojen ja ongelmien välttämiseksi.

## VSCode-asennus

Varmista, että käytät oikeaa Python-versiota VSCodessa.

![kuva](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundryn ja Microsoft Foundry Agent Servicen Asetus

### Vaihe 1: Luo Microsoft Foundry -projekti

Tarvitset Microsoft Foundry **hubin** ja **projektin**, johon on otettu käyttöön malli suorittaaksesi muistikirjat.

1. Mene osoitteeseen [ai.azure.com](https://ai.azure.com) ja kirjaudu sisään Azure-tililläsi.
2. Luo **hub** (tai käytä olemassa olevaa). Katso: [Hub-resurssien yleiskatsaus](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Luo hubin sisällä **projekti**.
4. Ota käyttöön malli (esim. `gpt-5-mini`) kohdasta **Models + Endpoints** → **Deploy model**.

### Vaihe 2: Hanki Projektisi Päätepisteen ja Mallin Ubemiesnimi

Microsoft Foundry -portaalissa:

- **Projektin päätepiste** — Mene **Overview**-sivulle ja kopioi päätepisteen URL-osoite.

![Projektin Yhteysmerkkijono](../../../translated_images/fi/project-endpoint.8cf04c9975bbfbf1.webp)

- **Mallin käyttöönoton nimi** — Mene **Models + Endpoints** -kohtaan, valitse käyttöönotettu mallisi, ja ota muistiin **Deployment name** (esim. `gpt-5-mini`).

### Vaihe 3: Kirjaudu Azureen komennolla `az login`

Kaikki muistikirjat käyttävät autentikointiin **`AzureCliCredential`ia** — API-avaimia ei tarvitse hallita. Tämä vaatii sisäänkirjautumisen Azure CLI:n kautta.

1. **Asenna Azure CLI** jos se ei ole vielä asennettuna: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Kirjaudu sisään** suorittamalla:

    ```bash|powershell
    az login
    ```

    Tai jos olet etä-/Codespace-ympäristössä ilman selainta:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Valitse tilaus** jos pyydetään — valitse tilaamasi Foundry-projektiin liittyvä tilaus.

4. **Varmista** että olet kirjautunut sisään:

    ```bash|powershell
    az account show
    ```

> **Miksi `az login`?** Muistikirjat autentikoituvat käyttämällä `AzureCliCredential`a `azure-identity`-paketista. Tämä tarkoittaa, että Azure CLI -istuntosi antaa tunnukset — ei API-avaimia tai salasanoja `.env`-tiedostossasi. Tämä on [tietoturvan paras käytäntö](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Vaihe 4: Luo `.env`-tiedostosi

Kopioi esimerkkitiedosto:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Avaa `.env` ja täytä nämä kaksi arvoa:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Muuttuja | Missä se löytyy |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portaali → projektisi → **Overview**-sivu |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portaali → **Models + Endpoints** → käyttöönotetun mallin nimi |

Siinä kaikki suurin osaan oppitunneista! Muistikirjat autentikoituvat automaattisesti `az login` -istuntosi kautta.

### Vaihe 5: Asenna Python-riippuvuudet

```bash|powershell
pip install -r requirements.txt
```

Suosittelemme suorittamaan tämän virtuaaliympäristössä, jonka loit aiemmin.

## Lisäasetukset oppitunnille 5 (Agentic RAG)

Oppitunti 5 käyttää **Azure AI Search** -hakua täydentävänä generaationa. Jos aiot suorittaa tämän oppitunnin, lisää nämä muuttujat `.env`-tiedostoon:

| Muuttuja | Missä se löytyy |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portaali → **Azure AI Search** -resurssisi → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portaali → **Azure AI Search** -resurssisi → **Settings** → **Keys** → pääkäyttäjäavain |

## Lisäasetukset oppitunneille, jotka kutsuvat Azure OpenAI:ta suoraan (oppitunnit 6 ja 8)

Joissakin oppitunnin 6 ja 8 muistikirjoissa kutsutaan **Azure OpenAI** suoraan (käyttäen **Responses API:ta**) ilman Microsoft Foundry -projektia. Nämä esimerkit käyttivät aiemmin GitHub-malleja, jotka ovat vanhentuneita (poistuvat käytöstä heinäkuussa 2026) eikä ne tue Responses API:a. Jos aiot suorittaa nämä esimerkit, lisää nämä muuttujat `.env`-tiedostoon:

| Muuttuja | Missä se löytyy |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-portaali → **Azure OpenAI** -resurssi → **Keys and Endpoint** → Päätepiste (esim. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Käyttöönotetun mallin nimi (esim. `gpt-5-mini`), joka tukee Responses API:a |
| `AZURE_OPENAI_API_KEY` | Valinnainen — vain jos käytät avainperusteista autentikointia `az login` / Entra ID:n sijaan |

> Responses API käyttää vakaata `/openai/v1/` päätepistettä, joten `api-version` ei ole tarpeen. Kirjaudu sisään `az login`-komennolla käyttääksesi avaimettoman Entra ID -autentikoinnin.

## Vaihtoehtoinen Palveluntarjoaja: MiniMax (OpenAI-yhteensopiva)

[MiniMax](https://platform.minimaxi.com/) tarjoaa suurikontekstisia malleja (jopa 204K tokenia) OpenAI-yhteensopivan API:n kautta. Koska Microsoft Agent Frameworkin `OpenAIChatClient` toimii minkä tahansa OpenAI-yhteensopivan päätepisteen kanssa, voit käyttää MiniMaxia suoraan Azure OpenAI:n tai OpenAI:n sijaan.

Lisää nämä muuttujat `.env`-tiedostoon:

| Muuttuja | Missä se löytyy |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Avaimet |
| `MINIMAX_BASE_URL` | Käytä `https://api.minimax.io/v1` (oletusarvo) |
| `MINIMAX_MODEL_ID` | Mallin nimi käytettäväksi (esim. `MiniMax-M3`) |

**Esimerkkejä malleista**: `MiniMax-M3` (suositeltu), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (nopeammat vastaukset). Mallien nimet ja saatavuus voivat muuttua ajan mittaan, ja pääsy tiettyyn malliin voi riippua tilistäsi tai alueestasi — tarkista ajantasainen lista [MiniMax Platformista](https://platform.minimaxi.com/). Jos `MiniMax-M3` ei ole tililläsi saatavilla, aseta `MINIMAX_MODEL_ID` malliin, johon sinulla on pääsy (esim. `MiniMax-M2.7`).

Koodiesimerkit, jotka käyttävät `OpenAIChatClient`ia (esim. oppitunnin 14 hotellivaraus), havaitsevat automaattisesti ja käyttävät MiniMax-konfiguraatiotasi kun `MINIMAX_API_KEY` on asetettu.

## Vaihtoehtoinen Palveluntarjoaja: Foundry Local (Suorita mallit laitteella)

[Foundry Local](https://foundrylocal.ai) on kevyt suoritusympäristö, joka lataa, hallinnoi ja palvelee kielimalleja **kokonaan omalla koneellasi** OpenAI-yhteensopivan API:n kautta — ei pilveä, ei Azure-tilausta, eikä API-avaimia. Erinomainen vaihtoehto offline-kehitykseen, kokeiluun ilman pilvikuluja tai datan pitämiseen laitteella.

Koska Microsoft Agent Frameworkin `OpenAIChatClient` toimii minkä tahansa OpenAI-yhteensopivan päätepisteen kanssa, Foundry Local on paikallinen suora vaihtoehto Azure OpenAI:lle.

**1. Asenna Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Lataa ja suorita malli** (aloittaa myös paikallisen palvelun):

```bash
foundry model list          # näytä saatavilla olevat mallit
foundry model run phi-4-mini
```

**3. Asenna Python SDK** paikallisen päätepisteen löytämistä varten:

```bash
pip install foundry-local-sdk
```

**4. Ohjaa Microsoft Agent Framework käyttämään paikallista malliasi:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Lataa (tarvittaessa) ja tarjoaa mallin paikallisesti, sitten löytää päätepisteen/portin.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # esim. http://localhost:<port>/v1
    api_key=manager.api_key,        # aina "ei-vaadittu" Foundry Localille
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Huom:** Foundry Local tarjoaa OpenAI-yhteensopivan **Chat Completions** -päätepisteen. Käytä sitä paikallisessa kehityksessä ja offline-tilanteissa. Täyden **Responses API** -toimintojen (tilausten hallinta, työkalujen syvä orkestrointi ja agenttityyppinen kehitys) saamiseksi suuntaa kohti **Azure OpenAI** tai **Microsoft Foundry** -projektia kuten oppitunneissa. Katso [Foundry Localin dokumentaatio](https://foundrylocal.ai) ajantasaiset malliluettelot ja alustatuki.

## Lisäasetukset Oppitunnille 8 (Bing Grounding -työnkulku)


Ehdollisen työnkulun muistikirja oppitunnissa 8 käyttää **Bing-perusta** Microsoft Foundryn kautta. Jos aiot suorittaa tämän esimerkin, lisää tämä muuttuja `.env`-tiedostoosi:

| Muuttuja | Mistä löytää |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry -portaali → projekti → **Hallinta** → **Yhdistetyt resurssit** → Bing-yhteytesi → kopioi yhteyden tunnus |

## Vianmääritys

### SSL-varmenteen vahvistusvirheet macOS:llä

Jos käytät macOS:ää ja kohtaat virheen, kuten:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Tämä on tunnettu ongelma Pythonissa macOS:llä, jossa järjestelmän SSL-varmenteisiin ei automaattisesti luoteta. Kokeile seuraavia ratkaisuja järjestyksessä:

**Vaihtoehto 1: Suorita Pythonin Install Certificates -skripti (suositeltu)**

```bash
# Korvaa 3.XX asennetulla Python-versiollasi (esim. 3.12 tai 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Vaihtoehto 2: Käytä `connection_verify=False` muistikirjassasi (vain GitHub Models -muistikirjoille)**

Oppitunnin 6 muistikirjassa (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) on jo mukana kommentoitu kiertotie. Poista kommentointi `connection_verify=False`-riviltä, kun luot asiakasta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Poista SSL-varmennuksen tarkistus käytöstä, jos kohtaat varmennevirheitä
)
```

> **⚠️ Varoitus:** SSL-varmenetarkistuksen poistaminen käytöstä (`connection_verify=False`) heikentää turvallisuutta ohittamalla varmenteen validoinnin. Käytä tätä vain väliaikaisena ratkaisuna kehitysympäristöissä, ei tuotannossa.

**Vaihtoehto 3: Asenna ja käytä `truststore`-kirjastoa**

```bash
pip install truststore
```

Lisää sitten seuraava koodi muistikirjasi tai skriptisi alkuun ennen kuin teet verkko-operaatioita:

```python
import truststore
truststore.inject_into_ssl()
```

## Jumiuduitko johonkin?

Jos kohtaat ongelmia tämän asetuksen kanssa, liity <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordiin</a> tai <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">avaa issue</a>.

## Seuraava oppitunti

Olet nyt valmis suorittamaan tämän kurssin koodin. Hauskaa oppimista lisää tekoälyagenttien maailmasta! 

[Johdatus tekoälyagentteihin ja agenttien käyttötapauksiin](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->