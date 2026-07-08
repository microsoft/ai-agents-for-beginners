# Kurssin asennus

## Johdanto

Tässä oppitunnissa käydään läpi, miten ajetaan tämän kurssin koodiesimerkit.

## Liity muiden oppijoiden seuraan ja hae apua

Ennen kuin alat kloonata repositoriotasi, liity [AI Agents For Beginners Discord -kanavalle](https://aka.ms/ai-agents/discord) saadaksesi apua asennuksessa, vastauksia kurssin kysymyksiin tai verkostoituaksesi muiden oppijoiden kanssa.

## Kloonaa tai haarauta tämä repository

Aloita kloonaamalla tai haarauttamalla GitHub-repositorio. Näin saat oman version kurssimateriaalista, jotta voit suorittaa, testata ja säätää koodia!

Tämä onnistuu klikkaamalla linkkiä <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">haarauta repo</a>

Sinulla pitäisi nyt olla oma haarautettu version tästä kurssista seuraavassa linkissä:

![Forked Repo](../../../translated_images/fi/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (suositeltu työpajaa / Codespacesia varten)

  >Täysi repositorio voi olla suuri (~3 GB), kun lataat koko historian ja kaikki tiedostot. Jos osallistut vain työpajaan tai tarvitset vain muutaman oppitunnin kansion, matala kloonaus (tai harva kloonaus) välttää suurimman osan latauksesta lyhentämällä historiaa ja/tai ohittamalla blobit.

#### Pikainen matala kloonaus — minimihistoria, kaikki tiedostot

Korvaa alla komennoista `<your-username>` haarautuksesi URL-osoitteella (tai upstream-URL:llä, jos haluat).

Kloonaa vain viimeisin commit-historia (pieni lataus):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Kloonaa tietty haara:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osittainen (sparse) kloonaus — minimiblogit ja valitut kansiot ainoastaan

Tämä käyttää osittaista kloonausta ja sparse-checkouttia (vaatii Git 2.25+ ja suositeltava nykyaikainen Git, jossa on osittainen kloonaustuki):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Mene repositoriokansioon:

```bash|powershell
cd ai-agents-for-beginners
```

Määritä sitten, mitkä kansiot haluat (esimerkki näyttää kaksi kansiota):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Kloonaamisen ja tiedostojen tarkistamisen jälkeen, jos tarvitset vain tiedostoja ja haluat vapauttaa tilaa (ei git-historiaa), poista repositoryn metatiedot (💀 peruuttamaton — menetät kaikki Git-toiminnot: ei committeja, vetämisiä, työntöjä tai historian tarkastelua).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespacesin käyttö (suositeltu paikallisten suurten latausten välttämiseen)

- Luo uusi Codespace tälle repoille [GitHub UI:n](https://github.com/codespaces) kautta.  

- Uuden luodun codespacen terminaalissa aja jokin yllä olevista matalan/kaukaisen kloonauksen komennoista, jotta saat tarvittavat oppituntikansiot Codespace-työtilaan.
- Valinnainen: kloonauksen jälkeen Codespacessa poista .git vapauttaaksesi lisää tilaa (katso poistokomentoja yllä).
- Huom: Jos haluat avata repositorion suoraan Codespacesissa (ilman ylimääräistä kloonausta), huomaa että Codespaces rakentaa devcontainer-ympäristön ja saattaa silti tarjota enemmän kuin tarvitset. Matalaa kopiointia käyttävä loppukahva uudessa Codespacessa antaa enemmän hallintaa levykäytöstä.

#### Vinkkejä

- Korvaa aina kloonaus URL haarautuksellasi, jos haluat muokata/commitata.
- Jos myöhemmin tarvitset enemmän historiaa tai tiedostoja, voit hakea niitä tai säätää sparse-checkout mukaan lisäkansioita.

## Koodin ajaminen

Tämä kurssi tarjoaa joukon Jupyter-muistikirjoja, joita voit ajaa saadaksesi käytännön kokemusta tekoälytekijöiden rakentamisesta.

Koodiesimerkit käyttävät **Microsoft Agent Frameworkia (MAF)** `FoundryChatClient` -asiakkaan kanssa, joka yhdistyy **Microsoft Foundry Agent Service V2**:een (Responses API) kautta **Microsoft Foundryn**.

Kaikki Python-muistikirjat on merkitty `*-python-agent-framework.ipynb`.

## Vaatimukset

- Python 3.12+
  - **HUOM**: Jos sinulla ei ole asennettuna Python 3.12:ta, varmista, että asennat sen. Luo sitten virtuaaliympäristö käyttämällä python3.12 varmistaaksesi oikeiden versioiden asennuksen requirements.txt -tiedostosta.
  
    >Esimerkki

    Luo Python-virtuaaliympäristön kansio:

    ```bash|powershell
    python -m venv venv
    ```

    Aktivoi sitten virtuaaliympäristö:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Näiden .NET-koodien käyttöön varmista, että asennat [.NET 10 SDK:n](https://dotnet.microsoft.com/download/dotnet/10.0) tai uudemman. Tarkista asennetun SDK:n versio:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Vaaditaan tunnistautumiseen. Asenna osoitteesta [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Pääsy Microsoft Foundryyn ja Microsoft Foundry Agent Serviceen.
- **Microsoft Foundry Project** — Projekti, jossa on käyttöönotettu malli (esim. `gpt-4o`). Katso [Vaihe 1](#vaihe-1-luo-microsoft-foundry-projekti) alla.

Olemme sisällyttäneet tähän repojuureen `requirements.txt`-tiedoston, joka sisältää kaikki tarvittavat Python-paketit koodiesimerkkien ajamiseen.

Voit asentaa ne ajamalla seuraavan komennon terminaalissa repositorion juuressa:

```bash|powershell
pip install -r requirements.txt
```

Suosittelemme Python-virtuaaliympäristön luomista ristiriitojen ja ongelmien välttämiseksi.

## VSCode-asennus

Varmista, että käytät VSCodessa oikeaa Python-versiota.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundryn ja Microsoft Foundry Agent Servicen asennus

### Vaihe 1: Luo Microsoft Foundry -projekti

Sinulla täytyy olla Microsoft Foundry **hub** ja **projekti** käyttöönotetulla mallilla muistiinpanojen ajamista varten.

1. Mene osoitteeseen [ai.azure.com](https://ai.azure.com) ja kirjaudu sisään Azure-tililläsi.
2. Luo **hub** (tai käytä olemassa olevaa). Katso: [Hub-resurssien yleiskatsaus](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Luo hubissa **projekti**.
4. Ota käyttöön malli (esim. `gpt-4o`) kohdasta **Models + Endpoints** → **Deploy model**.

### Vaihe 2: Hae projektisi päätepisteen URL ja mallin käyttöönoton nimi

Microsoft Foundry -portaalissa projektistasi:

- **Projektin päätepiste** — Mene **Overview**-sivulle ja kopioi päätepisteen URL.

![Project Connection String](../../../translated_images/fi/project-endpoint.8cf04c9975bbfbf1.webp)

- **Mallin käyttöönoton nimi** — Mene **Models + Endpoints**, valitse käyttöönotettu mallisi ja huomaa **Deployment name** (esim. `gpt-4o`).

### Vaihe 3: Kirjaudu Azuren kautta `az login` -komennolla

Kaikki muistikirjat käyttävät **`AzureCliCredential`** tunnistautumiseen — ei API-avaimia hallittavana. Tämä edellyttää, että olet kirjautuneena Azure CLI:n kautta.

1. **Asenna Azure CLI**, jos et ole vielä asentanut: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Kirjaudu sisään** ajamalla:

    ```bash|powershell
    az login
    ```

    Tai jos olet etäympäristössä/Codespacessa ilman selainta:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Valitse tilauksesi**, jos sinulta pyydetään — valitse se, jossa Foundry-projektisi on.

4. **Varmista** että olet kirjautunut:

    ```bash|powershell
    az account show
    ```

> **Miksi `az login`?** Muistikirjat todentavat käyttäen `AzureCliCredential`-kirjastoa `azure-identity`-paketista. Tämä tarkoittaa, että Azure CLI -istuntosi tarjoaa tunnistautumistiedot — ei API-avaimia tai salaisuuksia `.env`-tiedostossasi. Tämä on [turvallisuuskäytäntö](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

Avaa `.env`-tiedosto ja täytä seuraavat arvot:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Muuttuja | Mistä löytyy |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portal → projektisi → **Overview**-sivu |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portal → **Models + Endpoints** → käyttöönotetun mallisi nimi |

Siinä se useimmille oppitunneille! Muistikirjat tunnistautuvat automaattisesti `az login` -istunnon kautta.

### Vaihe 5: Asenna Python-riippuvuudet

```bash|powershell
pip install -r requirements.txt
```

Suosittelemme tämän ajamista siellä virtuaaliympäristössä, jonka loit aikaisemmin.

## Lisäasetukset Oppituntia 5 varten (Agentic RAG)

Oppitunti 5 käyttää **Azure AI Search**ia hakuun perustuvaan generointiin. Jos aiot ajaa tämän oppitunnin, lisää nämä muuttujat `.env`-tiedostoon:

| Muuttuja | Mistä löytyy |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portal → **Azure AI Search** -resurssisi → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portal → **Azure AI Search** -resurssisi → **Settings** → **Keys** → pääavaimen avain |

## Lisäasetukset oppitunteihin, jotka kutsuvat Azure OpenAI:ta suoraan (Oppitunnit 6 ja 8)

Jotkut muistikirjat oppitunneilla 6 ja 8 käyttävät **Azure OpenAI**:ta suoraan (käyttäen **Responses API:ta**) sijaan että menisivät Microsoft Foundryn kautta. Nämä mallit käyttivät aiemmin GitHub-malleja, jotka ovat vanhentuneet (eläkkeellä heinäkuu 2026) eikä ne tue Responses API:ta. Jos aiot ajaa nämä, lisää nämä muuttujat `.env`-tiedostoosi:

| Muuttuja | Mistä löytyy |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-portal → **Azure OpenAI** -resurssisi → **Keys and Endpoint** → päätepiste (esim. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Käyttöönotetun mallin nimi (esim. `gpt-4o-mini`) joka tukee Responses API:ta |
| `AZURE_OPENAI_API_KEY` | Valinnainen — vain jos käytät avainpohjaista autentikointia `az login` / Entra ID:n sijaan |

> Responses API käyttää vakaata `/openai/v1/` päätepistettä, joten `api-version` ei ole tarpeen. Kirjaudu sisään `az login`-komennolla käyttöönotettuun avaimettomaan Entra ID -autentikointiin.

## Vaihtoehtoinen palveluntarjoaja: MiniMax (OpenAI-yhteensopiva)

[MiniMax](https://platform.minimaxi.com/) tarjoaa suurikonseptisia malleja (jopa 204K tokeniin asti) OpenAI-yhteensopivan API:n kautta. Koska Microsoft Agent Frameworkin `OpenAIChatClient` toimii minkä tahansa OpenAI-yhteensopivan päätepisteen kanssa, voit käyttää MiniMaxia Azure OpenAI:n tai OpenAI:n vaihtoehtona.

Lisää nämä muuttujat `.env`-tiedostoon:

| Muuttuja | Mistä löytyy |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-avaimet |
| `MINIMAX_BASE_URL` | Käytä `https://api.minimax.io/v1` (oletusarvo) |
| `MINIMAX_MODEL_ID` | Käytettävän mallin nimi (esim. `MiniMax-M3`) |

**Esimerkkimalleja**: `MiniMax-M3` (suositeltu), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (nopeammat vastaukset). Mallien nimet ja saatavuus voivat muuttua ajan mittaan ja pääsy tiettyyn malliin voi riippua tilistäsi tai alueestasi — tarkista [MiniMax Platform](https://platform.minimaxi.com/) ajantasainen lista. Jos `MiniMax-M3` ei ole tililläsi saatavilla, aseta `MINIMAX_MODEL_ID` malliin, johon sinulla on pääsy (esim. `MiniMax-M2.7`).

Koodiesimerkit, jotka käyttävät `OpenAIChatClient`ia (esim. Oppitunti 14 hotelli-varausprosessissa) tunnistavat ja käyttävät automaattisesti MiniMaxin asetuksiasi, kun `MINIMAX_API_KEY` on asetettu.

## Vaihtoehtoinen palveluntarjoaja: Foundry Local (ajo mallit paikallisesti)

[Foundry Local](https://foundrylocal.ai) on kevyt ajonaikainen ympäristö, joka lataa, hallinnoi ja palvelee kielimalleja **kokonaan omalla koneellasi** OpenAI-yhteensopivan API:n kautta — ei pilveä, ei Azuren tilausta eikä API-avaimia. Erinomainen vaihtoehto offline-kehitykseen, pilvikustannusten välttämiseen tai datan pitämiseen paikallisena.

Koska Microsoft Agent Frameworkin `OpenAIChatClient` toimii minkä tahansa OpenAI-yhteensopivan päätepisteen kanssa, Foundry Local on helppo local-vaihtoehto Azure OpenAI:lle.

**1. Asenna Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Lataa ja aja malli** (käynnistää myös local-palvelun):

```bash
foundry model list          # näytä saatavilla olevat mallit
foundry model run phi-4-mini
```

**3. Asenna Python SDK**, jolla löydät local-päätepisteen:

```bash
pip install foundry-local-sdk
```

**4. Kohdista Microsoft Agent Framework paikalliseen malliin:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Lataa (tarvittaessa) ja palvelee mallin paikallisesti, sitten löytää päätepisteen/portin.
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

> **Huom:** Foundry Local tarjoaa OpenAI-yhteensopivan **Chat Completions** -päätepisteen. Käytä sitä paikalliseen kehitykseen ja offline-tilanteisiin. Täysimittaiselle **Responses API** -toiminnallisuudelle (tilalliset keskustelut, syvällinen työkalujen orkestrointi, agenttityyppinen kehitys) suuntaa **Azure OpenAI**:in tai **Microsoft Foundryn** projektin puoleen kuten oppitunneissa. Katso [Foundry Local dokumentaatio](https://foundrylocal.ai) ajankohtainen mallikatalogi ja alustatuki.

## Lisäasetukset Oppituntia 8 varten (Bingin perustaminen työnkulkuun)


Ehtolauseisiin perustuva työnkulun muistikirja oppitunnissa 8 käyttää **Bing-rajapintaa** Microsoft Foundryn kautta. Jos aiot suorittaa tämän esimerkin, lisää tämä muuttuja `.env`-tiedostoosi:

| Muuttuja | Sijainti |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry -portaali → projektisi → **Hallinta** → **Yhdistetyt resurssit** → Bing-yhteytesi → kopioi yhteyden tunnus |

## Vianetsintä

### SSL-varmenteen varmennusvirheet macOS-käyttöjärjestelmässä

Jos käytät macOS:ää ja kohtaat virheen kuten:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Tämä on tunnettu ongelma Pythonissa macOS:llä, jossa järjestelmän SSL-varmenteita ei luoteta automaattisesti. Kokeile seuraavia ratkaisuja järjestyksessä:

**Vaihtoehto 1: Suorita Pythonin Install Certificates -skripti (suositeltu)**

```bash
# Korvaa 3.XX asentamallasi Python-versiolla (esim. 3.12 tai 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Vaihtoehto 2: Käytä `connection_verify=False` muistikirjassasi (vain GitHub Models -muistikirjoille)**

Oppitunnin 6 muistikirjassa (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) on jo kommentoitu kiertotie. Poista kommenttimerkki `connection_verify=False`-kohdasta, kun luot asiakkaan:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Poista SSL-varmennuksen tarkistus käytöstä, jos kohtaat varmennevirheitä
)
```

> **⚠️ Varoitus:** SSL-varmennuksen poistaminen käytöstä (`connection_verify=False`) heikentää turvallisuutta ohittamalla varmenteen tarkastuksen. Käytä tätä vain väliaikaisena kiertotienä kehitysympäristöissä, ei koskaan tuotannossa.

**Vaihtoehto 3: Asenna ja käytä `truststore`-kirjastoa**

```bash
pip install truststore
```

Lisää sitten seuraava koodirivi muistikirjasi tai skriptisi alkuun ennen verkkokutsuja:

```python
import truststore
truststore.inject_into_ssl()
```

## Jumiuduitko jonnekin?

Jos sinulla on ongelmia tämän asetuksen suorittamisessa, liity mukaan <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordiin</a> tai <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">avaa ongelmailmoitus</a>.

## Seuraava oppitunti

Olet nyt valmis suorittamaan tämän kurssin koodin. Hauskaa oppimista lisää tekoälyagenttien maailmasta! 

[Johdanto tekoälyagentteihin ja agenttien käyttötapauksiin](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->