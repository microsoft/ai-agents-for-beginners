# Kurssin asennus

## Johdanto

Tässä oppitunnissa käydään läpi, miten suorittaa tämän kurssin koodiesimerkit.

## Liity muihin oppijoihin ja hae apua

Ennen kuin aloitat reposiitorion kloonaamisen, liity [AI Agents For Beginners - Discord -kanavalle](https://aka.ms/ai-agents/discord) saadaksesi apua asennuksessa, vastauksia kurssiin liittyviin kysymyksiin tai ollaksesi yhteydessä muihin oppijoihin.

## Kloonaa tai Forkkaa tämä Repo

Aloittaaksesi kloonaa tai forkaa GitHub-repositorio. Tämä luo oman version kurssimateriaaleista, jotta voit suorittaa, testata ja muokata koodia!

Tämän voi tehdä klikkaamalla linkkiä <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forkkaa repo</a>

Sinulla pitäisi nyt olla oma forkattu versio tästä kurssista seuraavassa linkissä:

![Forkattu repo](../../../translated_images/fi/forked-repo.33f27ca1901baa6a.webp)

### Pintakloonaus (suositeltu työpajalle / Codespacesille)

  > Koko repositorio voi olla suuri (~3 GB), jos lataat koko historian ja kaikki tiedostot. Jos osallistut vain työpajaan tai tarvitset vain muutamia oppituntikansioita, pintakloonaus (tai sparse-kloonaus) välttää suurimman osan latauksesta katkaisemalla historian ja/tai ohittamalla blobit.

#### Nopea pintakloonaus — minimaalinen historia, kaikki tiedostot

Korvaa `<your-username>` alla olevissa komennoissa fork-URL:llasi (tai upstream-URL:lla, jos haluat).

Toistaaksesi vain viimeisimmän commit-historian (pieni lataus):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Kloonaaaksesi tietyn haaran:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osittainen (sparse) kloonaus — minimaaliset blobit + vain valitut kansiot

Tämä käyttää osittaista kloonausta ja sparse-checkoutia (vaatii Git 2.25+; suositeltu moderni Git, jossa on osittaisen kloonauksen tuki):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Siirry repo-kansioon:

```bash|powershell
cd ai-agents-for-beginners
```

Sitten määritä, mitkä kansiot haluat (alla olevassa esimerkissä näytetään kaksi kansiota):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Kloonauksen ja tiedostojen varmennuksen jälkeen, jos tarvitset vain tiedostoja ja haluat vapauttaa tilaa (ei git-historiaa), poista repositorion metatiedot (💀 peruuttamaton — menetät kaiken Git-toiminnallisuuden: ei committeja, pull- tai push-toimintoja tai historian saatavuutta).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespacesin käyttö (suositeltu suurten paikallisten latausten välttämiseksi)

- Luo uusi Codespace tälle repolle [GitHubin käyttöliittymän](https://github.com/codespaces) kautta.  

- Uuden Codespacen terminaalissa suorita jokin yllä olevista shallow/sparse -kloonauskomennoista tuodaksesi vain tarvitsemasi oppituntikansiot Codespace-työtilaan.
- Valinnainen: kloonauksen jälkeen Codespacessa poista .git vapauttaaksesi lisätilaa (katso poistokomentoesimerkit yllä).
- Huom: Jos haluat avata reposiitorion suoraan Codespacessa (ilman erillistä kloonausta), ole tietoinen siitä, että Codespaces rakentaa devcontainer-ympäristön ja saattaa silti provisionoida enemmän kuin tarvitset. Kloonaamalla pintakopio tuoreen Codespacen sisälle saat paremman hallinnan levytilankäytöstä.

#### Vinkkejä

- Vaihda kloonaus-URL aina omaan forkkiisi, jos haluat muokata/commitoida.
- Jos tarvitset myöhemmin enemmän historiaa tai tiedostoja, voit hakea ne tai säätää sparse-checkoutia lisätäksesi kansioita.

## Koodin suorittaminen

Tämä kurssi tarjoaa sarjan Jupyter-kannettavia (Notebooks), joita voit suorittaa saadaksesi käytännön kokemusta AI-agenttien rakentamisesta.

Koodiesimerkeissä käytetään Microsoft Agent Frameworkia (MAF) yhdessä `AzureAIProjectAgentProvider`-palveluntarjoajan kanssa, joka yhdistää Azure AI Agent Service V2:een (Responses API) Microsoft Foundryn kautta.

Kaikki Python-kannettavat on merkitty nimellä `*-python-agent-framework.ipynb`.

## Vaatimukset

- Python 3.12+
  - **HUOM:** Jos sinulla ei ole Python 3.12 asennettuna, asenna se. Luo sitten virtuaaliympäristösi käyttäen python3.12 varmistaaksesi, että requirements.txt-tiedostosta asennetaan oikeat versiot.
  
    > Esimerkki

    Luo Python-venv-kansio:

    ```bash|powershell
    python -m venv venv
    ```

    Aktivoi sitten venv-ympäristö seuraavasti:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET:iä käyttävien esimerkkien osalta asenna [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) tai uudempi. Tarkista sitten asennettu .NET SDK -versiosi:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Kirjautumista varten. Asenna osoitteesta [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-tilaus** — Pääsyä Microsoft Foundryyn ja Azure AI Agent Serviceen varten.
- **Microsoft Foundry -projekti** — Projekti, jossa on käytössä oleva malli (esim. `gpt-4o`). Katso alla [Vaihe 1](../../../00-course-setup).

Olemme lisänneet `requirements.txt`-tiedoston tämän repositorion juureen, joka sisältää kaikki tarvittavat Python-paketit koodiesimerkkien suorittamiseen.

Voit asentaa ne suorittamalla seuraavan komennon terminaalissasi repositorion juurihakemistossa:

```bash|powershell
pip install -r requirements.txt
```

Suosittelemme Python-virtuaaliympäristön luomista konfliktien ja ongelmien välttämiseksi.

## VSCode:n asennus

Varmista, että käytät oikeaa Python-versiota VSCodessa.

![kuva](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Määritä Microsoft Foundry ja Azure AI Agent Service

### Vaihe 1: Luo Microsoft Foundry -projekti

Tarvitset Azure AI Foundry -hubin ja -projektin, jossa on käytössä oleva malli, jotta voit suorittaa kannettavat.

1. Siirry [ai.azure.com](https://ai.azure.com) ja kirjaudu Azure-tililläsi.
2. Luo **hub** (tai käytä olemassa olevaa). Katso: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Luo hubin sisällä **project**.
4. Ota malli käyttöön (esim. `gpt-4o`) valitsemalla **Models + Endpoints** → **Deploy model**.

### Vaihe 2: Nouda projektisi päätepiste ja mallin käyttöönoton nimi

Microsoft Foundry -portaalista projektisi kohdalta:

- **Project Endpoint** — Siirry **Overview**-sivulle ja kopioi endpoint-URL.

![Projektin päätepiste](../../../translated_images/fi/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Siirry **Models + Endpoints**-kohtaan, valitse käyttöönotettu mallisi ja ota talteen **Deployment name** (esim. `gpt-4o`).

### Vaihe 3: Kirjaudu Azureen komennolla `az login`

Kaikki kannettavat käyttävät todennukseen **`AzureCliCredential`** — ei API-avaimia hallittavana. Tämä vaatii, että olet kirjautuneena Azure CLI:llä.

1. **Asenna Azure CLI**, jos et ole vielä asentanut: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Kirjaudu sisään** suorittamalla:

    ```bash|powershell
    az login
    ```

    Tai jos olet etä-/Codespace-ympäristössä ilman selainta:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Valitse tilaus**, jos sinua pyydetään — valitse se, jossa Foundry-projektisi sijaitsee.

4. **Varmista**, että olet kirjautunut sisään:

    ```bash|powershell
    az account show
    ```

> **Miksi `az login`?** Kannettavat todennetaan `AzureCliCredential`-luokalla `azure-identity`-paketista. Tämä tarkoittaa, että Azure CLI -istuntosi tarjoaa tarvittavat tunnistetiedot — ei API-avaimia tai salaisuuksia .env-tiedostossasi. Tämä on [tietoturvan paras käytäntö](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Muuttuja | Mistä löytää |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portaali → projektisi → **Overview**-sivu |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portaali → **Models + Endpoints** → käyttöönotetun mallisi nimi |

Siinä kaikki useimpiin oppitunteihin! Kannettavat todennetaan automaattisesti `az login` -istuntosi kautta.

### Vaihe 5: Asenna Python-riippuvuudet

```bash|powershell
pip install -r requirements.txt
```

Suosittelemme suorittamaan tämän aiemmin luodussa virtuaaliympäristössä.

## Lisäasetukset oppitunnille 5 (Agentic RAG)

Oppitunti 5 käyttää **Azure AI Searchia** retrieval-augmented generation -toimintoihin. Jos aiot suorittaa kyseisen oppitunnin, lisää nämä muuttujat `.env`-tiedostoosi:

| Muuttuja | Mistä löytää |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portaali → Azure AI Search -resurssisi → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portaali → Azure AI Search -resurssisi → **Settings** → **Keys** → primary admin key |

## Lisäasetukset oppitunneille 6 ja 8 (GitHub-mallit)

Joissain oppituntien 6 ja 8 kannettavissa käytetään **GitHub Models** -palvelua Azure AI Foundryn sijaan. Jos aiot suorittaa nämä esimerkit, lisää nämä muuttujat `.env`-tiedostoosi:

| Muuttuja | Mistä löytää |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Käytä `https://models.inference.ai.azure.com` (oletusarvo) |
| `GITHUB_MODEL_ID` | Mallin nimi käytettäväksi (esim. `gpt-4o-mini`) |

## Lisäasetukset oppitunnille 8 (Bing Grounding -työnkulku)

Oppitunnon 8 ehdollinen työnkulku käyttää **Bing-groundingia** Azure AI Foundryn kautta. Jos aiot suorittaa tämän esimerkin, lisää tämä muuttuja `.env`-tiedostoosi:

| Muuttuja | Mistä löytää se |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry -portaali → projektisi → **Management** → **Connected resources** → Bing-yhteytesi → kopioi connection ID |

## Vianmääritys

### SSL-varmenteen vahvistusvirheet macOS:ssä

Jos käytät macOS:ää ja kohtaat virheen kuten:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Tämä on tunnettu ongelma Pythonin kanssa macOS:ssä, jossa järjestelmän SSL-sertifikaatteja ei välttämättä luoteta automaattisesti. Kokeile seuraavia ratkaisuja tässä järjestyksessä:

**Vaihtoehto 1: Suorita Pythonin Install Certificates -skripti (suositeltu)**

```bash
# Korvaa 3.XX asennetun Python-version numerolla (esim. 3.12 tai 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Vaihtoehto 2: Käytä `connection_verify=False` kannettavassasi (vain GitHub Models -kannettaville)**

Lesson 6 -kannettavassa (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) on jo kommentoitu kiertotie mukana. Poista kommenttimerkintä `connection_verify=False`-riviltä, kun luot clientin:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Poista SSL-varmennuksen tarkistus käytöstä, jos kohtaat varmennevirheitä
)
```

> **⚠️ Varoitus:** SSL-tarkistuksen poistaminen käytöstä (`connection_verify=False`) heikentää turvallisuutta ohittamalla sertifikaattien validoinnin. Käytä tätä vain väliaikaisena kiertotienä kehitysympäristöissä, älä koskaan tuotannossa.

**Vaihtoehto 3: Asenna ja käytä `truststore`-kirjastoa**

```bash
pip install truststore
```

Lisää sitten seuraava koodinpätkä kannettavan tai skriptin alkuun ennen verkkokutsujen tekemistä:

```python
import truststore
truststore.inject_into_ssl()
```

## Jumiuduitko jonnekin?

Jos sinulla on ongelmia tämän asennuksen kanssa, tule Slackiin tai hyppää meidän <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> -kanavalle tai <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">luo issue</a>.

## Seuraava oppitunti

Olet nyt valmis suorittamaan tämän kurssin koodin. Hauskaa oppimista lisää AI-agenttien maailmasta! 

[Johdanto AI-agentteihin ja agenttien käyttötapauksiin](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty tekoälykäännöspalvelulla Co-op Translator (https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ota huomioon, että automaattisissa käännöksissä voi olla virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää luotettavana lähteenä. Kriittisen tiedon osalta suosittelemme ammattimaista ihmiskäännöstä. Emme ole vastuussa mistään tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->