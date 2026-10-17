# Kurssin asennus

## Johdanto

Tässä oppitunnissa käydään läpi, miten voit suorittaa tämän kurssin koodiesimerkit.

## Liity muiden oppijoiden seuraan ja saa apua

Ennen kuin alat kloonaamaan omaa repositoriotasi, liity [AI Agents For Beginners Discord -kanavalle](https://aka.ms/ai-agents/discord) saadaksesi apua asennuksessa, vastauksia kurssin kysymyksiin tai yhteyden muihin oppijoihin.

## Kloonaa tai haarauta (fork) tämä repo

Aloita kloonaamalla tai haarauttamalla GitHub-repositorio. Näin saat oman version kurssimateriaalista, jotta voit ajaa, testata ja muokata koodia!

Tämä onnistuu klikkaamalla linkkiä <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">haarauta repo</a>

Sinulla pitäisi nyt olla oma haarautettu versio tästä kurssista seuraavan linkin kautta:

![Forked Repo](../../../translated_images/fi/forked-repo.33f27ca1901baa6a.webp)

### Pinnallinen kloonaus (suositeltu työpajaan / Codespacesiin)

  >Koko repositorio voi olla suuri (~3 Gt) kun lataat koko historian ja kaikki tiedostot. Jos osallistut vain työpajaan tai tarvitset vain muutamia oppituntikansioita, pinnallinen kloonaus (tai harva kloonaus) lataa huomattavasti vähemmän.

#### Nopea pinnallinen kloonaus — vähäinen historia, kaikki tiedostot

Korvaa `<your-username>` alla olevissa komennoissa haarautuksesi URL-osoitteella (tai upstream-URL-osoitteella, jos haluat).

Kloonaa vain viimeisimmän commit-historian (pieni lataus):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Kloonaa tietty haara:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osittainen (harva) kloonaus — vähäiset tavuobjektit + valitut kansiot

Tämä käyttää osittaista kloonausta ja sparse-checkoutia (vaatii Git 2.25+ ja suositeltavaa on uudempi Git, jossa on osittaisen kloonauksen tuki):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Siirry repositorion kansioon:

```bash
cd ai-agents-for-beginners
```

Määrittele sitten haluamasi kansiot (esimerkki näyttää kaksi kansiota):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Kloonaamisen ja tiedostojen vahvistamisen jälkeen, jos tarvitset vain tiedostot ja haluat vapauttaa tilaa (ilman git-historiaa), poista repositorion metatiedot (💀 peruuttamaton — menetät kaiken Git-toiminnallisuuden):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespacesin käyttö (suositellaan paikallisten suurien latausten välttämiseksi)

- Luo uusi Codespace tälle repolle GitHubin käyttöliittymässä ([GitHub UI](https://github.com/codespaces)).  

- Uuden luodun Codespacen terminaalissa suorita yksi ylläolevista pinnallisista/harvoista kloonauskomennoista tuodaksesi vain tarvitut oppituntikansiot Codespace-työtilaan.
- Valinnainen: kloonauksen jälkeen Codespacesissa poista .git vapauttaaksesi tilaa (katso ylemmät poistokäskyt).
- Huomaa: Jos haluat avata reposi suoraan Codespacesissa (ilman erillistä kloonausta), huomaa että Codespaces rakentaa devcontainer-ympäristön ja voi silti provisioida enemmän kuin tarvitset.

#### Vinkkejä

- Korvaa aina kloonaus-URL omahaarautuksellasi, jos haluat muokata/tehdä committeja.
- Jos tarvitset myöhemmin lisää historiaa tai tiedostoja, voit hakea niitä tai säätää sparse-checkoutia lisätäksesi kansioita.

## Koodin suorittaminen

Tämä kurssi tarjoaa sarjan Jupyter-muistikirjoja, joita voit käyttää saadaksesi käytännön kokemusta AI-agenttien rakentamisesta.

Koodiesimerkeissä käytetään **Microsoft Agent Frameworkia (MAF)** `FoundryChatClient`-asiakkaalla, joka yhdistää **Microsoft Foundry Agent Service V2** (Responses API:n) kautta **Microsoft Foundryyn**.

Kaikki Python-muistikirjat on nimetty `*-python-agent-framework.ipynb`.

## Vaatimukset

- Python 3.12+
  - **HUOM**: Jos Python3.12 ei ole asennettuna, asenna se. Luo sitten virtuaaliympäristösi käyttämällä python3.12 varmistaaksesi oikeiden versioiden asennuksen requirements.txt-tiedostosta.
  
    >Esimerkki

    Luo Python-virtuaaliympäristön hakemisto:

    ```bash
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

- .NET 10+: Esimerkeissä käytettyjen .NET-koodien osalta, asenna [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) tai uudempi. Tarkista sen jälkeen asennettu .NET-sdk-versiosi:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — vaaditaan todennukseen. Asenna osoitteesta [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-tilaus** — pääsyä varten Microsoft Foundryhin ja Microsoft Foundry Agent Serviceen.
- **Microsoft Foundry -projekti** — projekti, jossa on otettu käyttöön malli (esim. `gpt-5-mini`). Katso [Vaihe 1](#vaihe-1-luo-microsoft-foundry-projekti) alla.

Olemme sisällyttäneet tämän repositorion juureen `requirements.txt`-tiedoston, joka sisältää kaikki tarvittavat Python-paketit koodiesimerkkien suorittamiseen.

Voit asentaa ne suorittamalla seuraavan komennon terminaalissasi repositorion juuressa:

```bash
pip install -r requirements.txt
```

Suosittelemme Python-virtuaaliympäristön luomista ristiriitojen ja ongelmien välttämiseksi.

## VSCode-asetukset

Varmista, että käytät oikeaa Python-versiota VSCodessa.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundryn ja Microsoft Foundry Agent Servicen asennus

### Vaihe 1: Luo Microsoft Foundry -projekti

Tarvitset Microsoft Foundry -**hubin** ja -**projektin** joissa on otettu käyttöön malli suorittaaksesi muistikirjoja.

1. Mene [ai.azure.com](https://ai.azure.com) ja kirjaudu sisään Azure-tililläsi.
2. Luo **hubi** (tai käytä olemassa olevaa). Katso: [Hub-ressurssien yleiskatsaus](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Hubeissa luo **projekti**.
4. Ota malli käyttöön (esim. `gpt-5-mini`) valitsemalla **Models + Endpoints** → **Deploy model**.

### Vaihe 2: Hanki projektisi päätepiste ja mallin käyttöönoton nimi

Löydät tiedot Microsoft Foundry -portaalista projektistasi:

- **Projektin päätepiste** — Mene **Overview**-sivulle ja kopioi päätepisteen URL.

![Project Connection String](../../../translated_images/fi/project-endpoint.8cf04c9975bbfbf1.webp)

- **Mallin käyttöönoton nimi** — Mene **Models + Endpoints** -kohtaan, valitse käyttöönotettu mallisi ja huomaa **Deployment name** (esim. `gpt-5-mini`).

### Vaihe 3: Kirjaudu Azureen komennolla `az login`

Useimmat muistikirjat tunnistautuvat **Azure CLI:n kirjautumisen** kautta — käyttämällä `AzureCliCredential` tai `DefaultAzureCredential` (molemmat hyödyntävät `az login` -istuntoasi) `azure-identity`-paketista — joten ne eivät tarvitse API-avaimia. Jotkut oppitunnit ja valinnaiset integraatiot käyttävät API-avaimia; tarkista kunkin oppitunnin vaatimukset mahdollisista lisäympäristömuuttujista. Tämä vaatii kirjautumisen Azure CLI:llä.

1. **Asenna Azure CLI** jos et ole vielä tehnyt niin: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Kirjaudu sisään** suorittamalla:

    ```bash
    az login
    ```

    Tai jos olet etäympäristössä/Codespacessa ilman selainta:

    ```bash
    az login --use-device-code
    ```

3. **Valitse tilauksesi** tarvittaessa — valitse se, jossa Foundry-projektisi on.

4. **Varmista** että olet kirjautunut sisään:

    ```bash
    az account show
    ```

> **Miksi `az login`?** Muistikirjat tunnistautuvat käyttämällä `AzureCliCredential` (tai `DefaultAzureCredential`, joka myös hyödyntää Azure CLI:n kirjautumista) `azure-identity`-paketista. Tämä tarkoittaa, että Azure CLI -istuntosi tarjoaa tunnistetiedot — ei API-avaimia tai salaisuuksia `.env`-tiedostossasi. Tämä on [turvallisuusparhaat käytännöt](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portaali → **Models + Endpoints** → käyttöönotetun mallisi nimi |

Tämä riittää useimpiin oppitunteihin! Muistikirjat tunnistautuvat automaattisesti `az login` -istuntosi kautta.

### Vaihe 5: Asenna Python-riippuvuudet

```bash
pip install -r requirements.txt
```

Suosittelemme tämän suorittamista aiemmin luomassasi virtuaaliympäristössä.

## Valinnainen asennus: Azure AI Search (oppitunnit 5 ja 16)

Oppituntien 5 (Agentic RAG) ja 16 muistikirjat toimivat heti käyttövalmiina **muistissa olevalla tietokannalla** — ei muita Azure-resursseja. Jos haluat käyttää niitä oikean **Azure AI Search** -indeksin kanssa, huomaa että **oppitunti 16 käyttää tällä hetkellä avainpohjaista todennusta**: se vaihtaa muistissa olevan haun sijasta Azure AI Searchiin vain kun **molemmat** `AZURE_SEARCH_SERVICE_ENDPOINT` **ja** `AZURE_SEARCH_API_KEY` ovat asetettuja, ja muuten pysyy muistissa toimivassa haussa — joten käyttöönottaaksesi oikean indeksin, sinun tulee asettaa myös ylläpitäjän avain. Avaimeton todennus Microsoft Entra ID:n (RBAC) avulla on suositeltu tapa omalle tuotantokoodillesi, ja se on yhdenmukainen `az login` -käytännön kanssa, jota kurssin muut muistikirjat käyttävät.

Alla olevat RBAC-vaiheet koskevat asennusoppaan esimerkkejä ja omaa koodiasi. Ne eivät mahdollista avaimetonta todennusta oppitunnin 16 muistikirjassa; oppitunto 16 vaatii silti sekä päätepisteen että ylläpitoavaimen käyttääkseen Azure AI Searchia.

1. **Ota käyttöön roolipohjainen pääsy** hakupalvelussasi:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Anna itsellesi vaaditut roolit** (luo/lataa indeksejä ja tee hakuja):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Lisää päätepiste** `.env`-tiedostoosi:

| Muuttuja | Missä se löytyy |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portaali → Azure AI Search -resurssisi → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Vaaditaan (päätepisteen kanssa) Azure AI Searchin käyttöönottoon oppitunnissa 16, joka käyttää avainpohjaista todennusta. Azure-portaali → **Asetukset** → **Avaimet** → pääadmin-avain |

> **Miksi avaimeton?** Admin-avaimet antavat täydet kirjoitusoikeudet hakupalveluusi ja voivat vuotaa `.env`-tiedostojen kautta. RBAC:n kanssa käytetään sen sijaan kirjautumistasi `az login` -identiteetillä — sama avaimeton Entra ID -malli kuin kurssin muistikirjoissa (käyttää `AzureCliCredential` / `DefaultAzureCredential`). Katso [Yhdistä Azure AI Searchiin roolien avulla](https://learn.microsoft.com/azure/search/search-security-rbac).

Katso [Azure AI Searchin asennusopas](./AzureSearch.md) täydellisistä indeksin luontiesimerkeistä Pythonilla ja .NET:llä.

## Lisäasennus oppitunteihin, jotka kutsuvat Azure OpenAI:ta suoraan (oppitunnit 6 ja 8)

Joissakin oppitunneissa 6 ja 8 kutsutaan **Azure OpenAI:ta** suoraan (käyttäen **Responses API:a**) ilman Microsoft Foundry -projektia. Nämä esimerkit käyttivät aiemmin GitHub-malleja, jotka ovat poistumassa ja eivät tue Responses API:a. Lisää nämä muuttujat `.env`-tiedostoosi:

| Muuttuja | Missä se löytyy |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-portaali → Azure OpenAI -resurssi → **Keys and Endpoint** → Päätepiste (esim. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Käyttöönotetun mallisi nimi (esim. `gpt-5-mini`), joka tukee Responses API:a |
| `AZURE_OPENAI_API_KEY` | Valinnainen — vain jos käytät avainpohjaista tunnistusta az login / Entra ID:n sijaan |

> Responses API käyttää vakaata `/openai/v1/` päätepistettä, joten erillistä `api-version`-asetusta ei tarvita. Kirjaudu sisään `az login`:lla käyttöönottaaksesi avaimettoman Entra ID -todennuksen.

## Vaihtoehtoinen tarjoaja: MiniMax (OpenAI-yhteensopiva)

[MiniMax](https://platform.minimaxi.com/) tarjoaa suurta kontekstia tukevia malleja (jopa 204K tokenia) OpenAI-yhteensopivan rajapinnan kautta. Koska Microsoft Agent Frameworkin `OpenAIChatClient` toimii minkä tahansa OpenAI-yhteensopivan päätepisteen kanssa, voit käyttää MiniMaxia suoraan vaihtoehtona oppitunneissa, jotka käyttävät `OpenAIChatClient`:iä.

Lisää nämä muuttujat `.env`-tiedostoosi:

| Muuttuja | Missä se löytyy |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax-alusta](https://platform.minimaxi.com/) → API-avaimet |
| `MINIMAX_BASE_URL` | Käytä `https://api.minimax.io/v1` (oletusarvo) |
| `MINIMAX_MODEL_ID` | Mallin nimi käytettäväksi (esim. `MiniMax-M3`) |

**Esimerkkimallit**: `MiniMax-M3` (suositeltu), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (nopeammat vastaukset). Mallien nimet ja saatavuus voivat muuttua ajan myötä, ja mallin käyttöoikeus voi riippua tilistäsi.

Koodiesimerkit, jotka käyttävät `OpenAIChatClient`:iä (esim. oppitunti 14 hotellivarauksen työnkulku), tunnistavat ja käyttävät automaattisesti MiniMax-konfiguraatiotasi, kun `MINIMAX_API_KEY` on asetettu.


## Vaihtoehtoinen tarjoaja: Novita AI (OpenAI-yhteensopiva)

[Novita AI](https://novita.ai/llm-api) tarjoaa OpenAI-yhteensopivan API:n avoimen lähdekoodin ja uusimpien LLM-mallien (DeepSeek, Llama, Qwen ja muita) käyttöön. Koska Microsoft Agent Frameworkin `OpenAIChatClient` toimii minkä tahansa OpenAI-yhteensopivan päätepisteen kanssa, voit käyttää Novita AI:ta suoraan vaihtoehtona Azure OpenAI:lle tai OpenAI:lle.

Lisää nämä muuttujat `.env`-tiedostoosi:

| Muuttuja | Missä se löytyy |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI -hallintapaneeli](https://novita.ai/settings/key-management) → API-avaimet |
| `NOVITA_BASE_URL` | Käytä `https://api.novita.ai/openai/v1` (oletusarvo) |
| `NOVITA_MODEL_ID` | Käytettävän mallin nimi (esim. `moonshotai/kimi-k3`) |

**Esimerkkimalleja**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI tarjoaa myös monia muita avoimen lähdekoodin malliperheitä (Llama, Qwen, GLM ja muita) — tarkista [Novita AI mallikirjasto](https://novita.ai/llm-api) ajantasainen lista saatavilla olevista malleista ja niiden mallitunnuksista.

Nykyiset esimerkit eivät automaattisesti käytä `NOVITA_*`-muuttujia. Käyttääksesi Novita AI:ta, välitä nämä arvot nimenomaisesti rakentaessasi `OpenAIChatClient`-asiakasta ajamassasi esimerkissä.

## Vaihtoehtoinen tarjoaja: Foundry Local (Suorita mallit paikallisesti laitteellasi)

[Foundry Local](https://foundrylocal.ai) on kevyt runtime, joka lataa, hallinnoi ja palvelee kielimalleja **täysin omalla koneellasi** OpenAI-yhteensopivan API:n kautta — pilveä ei tarvita.

Koska Microsoft Agent Frameworkin `OpenAIChatClient` toimii minkä tahansa OpenAI-yhteensopivan päätepisteen kanssa, Foundry Local on paikallinen suora vaihtoehto Azure OpenAI:lle.

**1. Asenna Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Lataa ja suorita malli** (tämä käynnistää myös paikallisen palvelun):

```bash
foundry model list          # näytä saatavilla olevat mallit
foundry model run phi-4-mini
```

**3. Asenna Python SDK**, jota käytetään paikallisen päätepisteen löytämiseen:

```bash
pip install foundry-local-sdk
```

**4. Ohjaa Microsoft Agent Framework paikalliseen malliisi:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Lataa (tarvittaessa) ja palvelee mallia paikallisesti, sitten löytää päätepisteen/portin.
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

> **Huom:** Foundry Local tarjoaa OpenAI-yhteensopivan **Chat Completions** -päätepisteen. Käytä sitä paikalliseen kehitykseen ja offline-tilanteisiin. Täydellistä **Responses API** -ominaisuussarjaa (tila-pohjaiset keskustelut jne.) varten käytä Azure OpenAI:ta tai Microsoft Foundry -projektia.

## Lisäasetukset Oppituntiin 8 (Bing Grounding -työnkulku)

Oppitunnin 8 ehdollinen työnkulku käyttää **Bing grounding** -toimintoa Microsoft Foundryn kautta. Jos aiot suorittaa kyseisen esimerkin, lisää tämä muuttuja `.env`-tiedostoosi:

| Muuttuja | Missä se löytyy |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundryn portaali → projektisi → **Hallinta** → **Yhdistetyt resurssit** → Bing-yhteytesi → kopioi yhteyden ID |

## Vianmääritys

### SSL-varmenteen vahvistusvirheet macOS:llä

Jos olet macOS-käyttöjärjestelmässä ja saat virheilmoituksen kuten:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Tämä on tunnettu Pythonin ongelma macOS:llä, jossa järjestelmän SSL-varmenteita ei luoteta automaattisesti. Kokeile seuraavia ratkaisuja tässä järjestyksessä:

**Vaihtoehto 1: Suorita Pythonin Install Certificates -skripti (suositeltu)**

```bash
# Korvaa 3.XX asennetulla Python-versiollasi (esim. 3.12 tai 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Vaihtoehto 2: Käytä `connection_verify=False` muistikirjassasi (vain GitHub Models -muistikirjoihin)**

Oppitunnin 6 muistikirjassa (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) on jo kommentoituna mukana kiertotie. Poista kommentti `connection_verify=False`-riviltä kun kohtaat varmennevirheitä:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Poista SSL-tarkistus käytöstä, jos kohtaat varmennevirheitä
)
```

> **⚠️ Varoitus:** SSL-tarkistuksen poistaminen käytöstä (`connection_verify=False`) heikentää turvallisuutta ohittamalla varmenteiden vahvistuksen. Käytä tätä vain väliaikaisena kiertotienä kehitysympäristöissä. Älä koskaan käytä tuotannossa.

**Vaihtoehto 3: Asenna ja käytä `truststore`-kirjastoa**

```bash
pip install truststore
```

Lisää sitten seuraava koodi muistikirjasi tai skriptisi alkuun ennen minkään verkkoyhteyden muodostamista:

```python
import truststore
truststore.inject_into_ssl()
```

## Jumiuduitko johonkin?

Jos sinulla on ongelmia tämän asennuksen kanssa, liity <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordiin</a> tai <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">avaa issue GitHubissa</a>.

## Seuraava oppitunti

Olet nyt valmis suorittamaan tämän kurssin koodit. Hauskaa oppimista tekoälyagenttien maailmasta! 

[Johdanto tekoälyagentteihin ja agenttien käyttötapauksiin](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->