# Kurssin asennus

## Johdanto

Tässä oppitunnissa käsitellään, kuinka suorittaa tämän kurssin koodiesimerkit.

## Liity muiden oppijoiden seuraan ja saa apua

Ennen kuin alat kloonata repositoriotasi, liity [AI Agents For Beginners Discord -kanavalle](https://aka.ms/ai-agents/discord) saadaksesi apua asennuksessa, kysymyksiä kurssista tai yhdistyäksesi muiden oppijoiden kanssa.

## Kloonaa tai haarauta tämä repo

Aloittaaksesi kloonaa tai haarauta GitHub-repositorio. Tämä luo sinulle oman version kurssin materiaalista, jotta voit suorittaa, testata ja muokata koodia!

Tämä onnistuu klikkaamalla linkkiä <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">haarauta repositorio</a>

Sinulla pitäisi nyt olla oma haarautettu versiosi tästä kurssista seuraavassa linkissä:

![Forked Repo](../../../translated_images/fi/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (suositellaan työpajalle / Codespacesille)

> Koko repositorio voi olla suuri (~3 GB), kun lataat koko historian ja kaikki tiedostot. Jos osallistut vain työpajaan tai tarvitset vain muutaman oppituntikansion, shallow clone (tai sparse clone) välttää suurimman osan latauksesta rajoittamalla historian ja/tai ohittamalla blobit.

#### Nopea shallow clone — minimaalinen historia, kaikki tiedostot

Korvaa `<your-username>` alla komennoissa haarautuneen URL-osoitteellasi (tai upstream URL:lla, jos haluat).

Ladkaa vain viimeisin commit-historia (pieni lataus):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ladkaa tietty haara:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osittainen (sparse) clone — minimaalinen blobien määrä + vain valitut kansiot

Tämä käyttää osittaista kloonausta ja sparse-checkoutia (vaatii Git 2.25+ ja suositellaan modernia Gitiä, jossa on osittainen kloonaustuki):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Siirry repositoriokansioon:

```bash|powershell
cd ai-agents-for-beginners
```

Sitten määritä, mitkä kansiot haluat (esimerkissä kaksi kansiota):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Kloonaamisen ja tiedostojen varmistamisen jälkeen, jos tarvitset vain tiedostot etkä Git-historiaa, poista repositorion metatiedot (💀peruuttamaton — menetät kaiken Git-toiminnallisuuden: ei committeja, pullauksia, pushauksia tai historiatietoja).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespacesin käyttäminen (suositellaan paikallisten suurien latausten välttämiseksi)

- Luo uusi Codespace tälle repositoriolle [GitHub UI:n kautta](https://github.com/codespaces).

- Uuden luodun Codespacen terminaalissa suorita yksi yllä mainituista shallow/sparse clone -komennoista tuodaksesi vain tarvitsemasi oppituntikansiot Codespace-työtilaan.
- Valinnainen: kloonauksen jälkeen Codespacesissa poista .git vapauttaaksesi tilaa (katso poistokäskyt yllä).
- Huomaa: Jos haluat avata repositorion suoraan Codespacesissa (ilman lisäkloonausta), ole tietoinen, että Codespaces rakentaa devcontainer-ympäristön ja saattaa silti varata enemmän kuin tarvitset. Shallow kloonaus uuden Codespacen sisällä antaa enemmän hallintaa levytilan käytöstä.

#### Vinkkejä

- Korvaa aina kloonaus-URL haarallasi, jos haluat muokata/commitata.
- Jos myöhemmin tarvitset enemmän historiaa tai tiedostoja, voit hakea ne tai säätää sparse-checkoutia sisältämään lisää kansioita.

## Koodin suorittaminen

Tämä kurssi tarjoaa joukon Jupyter-muisteja, joita voit suorittaa saadaksesi käytännön kokemusta AI-agenttien rakentamisesta.

Koodiesimerkit käyttävät **Microsoft Agent Frameworkia (MAF)** `AzureAIProjectAgentProvider`-rajapinnalla, joka yhdistää **Azure AI Agent Service V2**:een (Responses API) **Microsoft Foundryn** kautta.

Kaikki Python-muistikirjat ovat nimetty muodossa `*-python-agent-framework.ipynb`.

## Vaatimukset

- Python 3.12+
  - **HUOM:** Jos sinulla ei ole Python 3.12:tä asennettuna, varmista että asennat sen. Luo sitten virtuaaliympäristö python3.12:lla varmistaaksesi, että oikeat versiot asennetaan requirements.txt-tiedostosta.
  
    >Esimerkki

    Luo Python-virtuaaliympäristön hakemisto:

    ```bash|powershell
    python -m venv venv
    ```

    Aktivoi sitten virtuaaliympäristö seuraavasti:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Esimerkkikoodien .NET-versio, varmista että asennat [.NET 10 SDK:n](https://dotnet.microsoft.com/download/dotnet/10.0) tai myöhemmän version. Tarkista asennettu .NET SDK -versio:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Tarvitaan todennukseen. Asenna osoitteesta [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-tilaus** — Pääsy Microsoft Foundryyn ja Azure AI Agent Serviceen.
- **Microsoft Foundry -projekti** — Projekti, jossa on käytössä mallin lähetetty versio (esim. `gpt-4o`). Katso [Vaihe 1](#vaihe-1-luo-microsoft-foundry-projekti) alla.

Tämä repositorio sisältää `requirements.txt`-tiedoston juurihakemistossa, jossa on kaikki vaaditut Python-kirjastot koodiesimerkkien suorittamiseen.

Voit asentaa ne ajamalla seuraavan komennon terminaalissasi repositorion juuressa:

```bash|powershell
pip install -r requirements.txt
```

Suosittelemme Python-virtuaaliympäristön luomista ristiriitojen ja ongelmien välttämiseksi.

## VSCode:n asennus

Varmista, että käytät oikeaa Python-versiota VSCodessa.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundryn ja Azure AI Agent Servicen asennus

### Vaihe 1: Luo Microsoft Foundry -projekti

Tarvitset Azure AI Foundry **hubin** ja **projektin**, jossa on käytössä mallin deploy-versio, jotta voit ajaa muistikirjoja.

1. Mene osoitteeseen [ai.azure.com](https://ai.azure.com) ja kirjaudu sisään Azure-tililläsi.
2. Luo **hub** (tai käytä olemassa olevaa). Katso: [Hub resurssien yleiskatsaus](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Luo hubin sisällä **projekti**.
4. Lähetä malli (esim. `gpt-4o`) valitsemalla **Models + Endpoints** → **Deploy model**.

### Vaihe 2: Hanki projektisi päätepiste ja mallin deploy-nimi

Microsoft Foundry -portaalista projektissasi:

- **Projektin päätepiste** — Mene **Overview**-sivulle ja kopioi päätepisteen URL-osoite.

![Project Connection String](../../../translated_images/fi/project-endpoint.8cf04c9975bbfbf1.webp)

- **Mallin deploy-nimi** — Mene **Models + Endpoints** -kohtaan, valitse mallisi ja huomaa **Deployment name** (esim. `gpt-4o`).

### Vaihe 3: Kirjaudu Azureen `az login` -komennolla

Kaikki muistikirjat käyttävät todennukseen **`AzureCliCredential`** — ei API-avaimia hallittavaksi. Tämä edellyttää sisäänkirjautumista Azure CLI:n kautta.

1. **Asenna Azure CLI**, jos sitä ei ole vielä asennettu: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Kirjaudu sisään** ajamalla:

    ```bash|powershell
    az login
    ```

    Tai jos olet etä-/Codespace-ympäristössä ilman selainta:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Valitse tilauksesi**, jos sinulta kysytään — valitse se, jossa Foundry-projektisi sijaitsee.

4. **Varmista**, että olet kirjautunut sisään:

    ```bash|powershell
    az account show
    ```

> **Miksi `az login`?** Muistikirjat todennetaan `AzureCliCredential`-tunnisteella `azure-identity`-paketin kautta. Tämä tarkoittaa, että Azure CLI -istuntosi tarjoaa tunnistetiedot — ei API-avaimia tai salaisuuksia `.env`-tiedostossasi. Tämä on [turvallisuuden paras käytäntö](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Vaihe 4: Luo `.env`-tiedosto

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Muuttuja | Mistä löytää |
|----------|--------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portaali → projektisi → **Overview** -sivu |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portaali → **Models + Endpoints** → käytössä olevan mallin nimi |

Se on suurin osa oppitunneista! Muistikirjat todennetaan automaattisesti `az login` -sesiosi kautta.

### Vaihe 5: Asenna Python-riippuvuudet

```bash|powershell
pip install -r requirements.txt
```

Suosittelemme suorittamaan tämän juuri aikaisemmin luodussa virtuaaliympäristössä.

## Lisäasetukset Oppitunnille 5 (Agentic RAG)

Oppitunti 5 käyttää **Azure AI Searchia** retrieval-augmented generationiin. Jos aiot suorittaa tämän oppitunnin, lisää nämä muuttujat `.env`-tiedostoosi:

| Muuttuja | Mistä löytää |
|----------|--------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portaali → **Azure AI Search** -resurssisi → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portaali → **Azure AI Search** -resurssisi → **Settings** → **Keys** → pääavaimen |

## Lisäasetukset oppitunneille 6 ja 8 (GitHub-mallit)

Jotkut muistikirjat oppitunneissa 6 ja 8 käyttävät **GitHub-malleja** Azure AI Foundryn sijaan. Jos aiot suorittaa nämä esimerkit, lisää nämä muuttujat `.env`-tiedostoosi:

| Muuttuja | Mistä löytää |
|----------|--------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Käytä `https://models.inference.ai.azure.com` (oletusarvo) |
| `GITHUB_MODEL_ID` | Käytettävän mallin nimi (esim. `gpt-4o-mini`) |

## Vaihtoehtoinen tarjoaja: MiniMax (OpenAI-yhteensopiva)

[MiniMax](https://platform.minimaxi.com/) tarjoaa laajakontekstisia malleja (jopa 204K tokenia) OpenAI-yhteensopivan API:n kautta. Koska Microsoft Agent Frameworkin `OpenAIChatClient` toimii minkä tahansa OpenAI-yhteensopivan päätepisteen kanssa, voit käyttää MiniMaxia gitHub-mallien tai OpenAI:n tilalla.

Lisää nämä muuttujat `.env`-tiedostoosi:

| Muuttuja | Mistä löytää |
|----------|--------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-avaimet |
| `MINIMAX_BASE_URL` | Käytä `https://api.minimax.io/v1` (oletusarvo) |
| `MINIMAX_MODEL_ID` | Käytettävän mallin nimi (esim. `MiniMax-M3`) |

**Esimerkkimallit**: `MiniMax-M3` (suositeltu), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (nopeammat vastaukset). Mallin nimet ja saatavuus voivat muuttua ajan myötä, ja tiettyyn malliin pääsy saattaa riippua tilistäsi tai alueestasi — tarkista [MiniMax Platformista](https://platform.minimaxi.com/) ajantasainen lista. Jos `MiniMax-M3` ei ole tililläsi, aseta `MINIMAX_MODEL_ID` malliin, johon sinulla on pääsy (esim. `MiniMax-M2.7`).

Koodiesimerkit, jotka käyttävät `OpenAIChatClient`-luokkaa (esim. Oppitunti 14 hotellin varaus -työnkulku), havaitsevat ja käyttävät automaattisesti MiniMax-asetuksiasi, kun `MINIMAX_API_KEY` on asetettu.

## Lisäasetukset oppitunnille 8 (Bing Grounding Workflow)

Oppitunnin 8 ehtoinen työnkulku käyttää **Bing grounding** -toimintoa Azure AI Foundryn kautta. Jos aiot suorittaa tämän esimerkin, lisää tämä muuttuja `.env`-tiedostoosi:

| Muuttuja | Mistä löytää |
|----------|--------------|
| `BING_CONNECTION_ID` | Azure AI Foundry -portaali → projektisi → **Management** → **Connected resources** → Bing-yhteytesi → kopioi connection ID |

## Vianetsintä

### SSL-varmenteen vahvistusvirheet macOS:llä

Jos käytät macOS:ää ja kohtaat virheen kuten:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Tämä on tunnettu ongelma Pythonissa macOS:llä, jossa järjestelmän SSL-varmenteita ei automaattisesti luoteta. Kokeile seuraavia ratkaisuja tässä järjestyksessä:

**Vaihtoehto 1: Suorita Pythonin Install Certificates -skripti (suositeltu)**

```bash
# Korvaa 3.XX asentamallasi Python-versiolla (esim. 3.12 tai 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Vaihtoehto 2: Käytä `connection_verify=False` muistikirjassa (vain GitHub Models -muistikirjoille)**

Oppitunnin 6 muistikirjassa (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) on kommentiksi jätetty kiertotapa jo valmiina. Ota pois kommenttimerkinnät `connection_verify=False` -kohdalta, kun luot clientin:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Poista SSL-varmennuksen tarkistus käytöstä, jos kohtaat varmennevirheitä
)
```

> **⚠️ Varoitus:** SSL-varmennuksen poistaminen (`connection_verify=False`) heikentää turvallisuutta ohittamalla sertifikaatin tarkistuksen. Käytä tätä vain tilapäisenä ratkaisuna kehitysympäristöissä, ei koskaan tuotannossa.

**Vaihtoehto 3: Asenna ja käytä `truststore`-kirjastoa**

```bash
pip install truststore
```

Lisää sitten seuraava koodi muistikirjasi tai skriptisi alkuun ennen verkkokutsuja:

```python
import truststore
truststore.inject_into_ssl()
```

## Jumiuduitko johonkin?

Jos sinulla on ongelmia tämän asennuksen kanssa, tule käymään <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordissa</a> tai <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">luo issue</a>.
## Seuraava oppitunti

Olet nyt valmis suorittamaan tämän kurssin koodin. Hyvää oppimista lisää tekoälyagenttien maailmasta!

[Johdatus tekoälyagentteihin ja agenttien käyttötapauksiin](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->