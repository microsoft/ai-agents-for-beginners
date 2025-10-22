<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:41:42+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fi"
}
-->
# Kurssin asennus

## Johdanto

Tässä osiossa käsitellään, kuinka kurssin koodiesimerkit suoritetaan.

## Liity muiden oppijoiden joukkoon ja pyydä apua

Ennen kuin alat kloonata omaa reposi, liity [AI Agents For Beginners Discord-kanavalle](https://aka.ms/ai-agents/discord) saadaksesi apua asennukseen, kysymyksiin kurssista tai yhteyden muihin oppijoihin.

## Kloonaa tai haarauta tämä repo

Aloittaaksesi, kloonaa tai haarauta GitHub-repositorio. Näin saat oman version kurssimateriaalista, jota voit suorittaa, testata ja muokata!

Tämä onnistuu klikkaamalla linkkiä <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">haaraudu repo</a>

Sinulla pitäisi nyt olla oma haarautettu versio tästä kurssista seuraavassa linkissä:

![Haarautettu Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.fi.png)

### Pintakloonaus (suositeltu työpajaa / Codespacesia varten)

  >Koko repositorio voi olla suuri (~3 GB), kun lataat koko historian ja kaikki tiedostot. Jos osallistut vain työpajaan tai tarvitset vain muutaman oppituntikansion, pintakloonaus (tai osittainen kloonaus) välttää suurimman osan latauksesta rajoittamalla historiaa ja/tai ohittamalla tiedostot.

#### Nopea pintakloonaus — minimaalinen historia, kaikki tiedostot

Korvaa `<your-username>` alla olevissa komennoissa haarautumisesi URL-osoitteella (tai alkuperäisellä URL-osoitteella, jos haluat).

Kloonataksesi vain viimeisimmän commit-historian (pieni lataus):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Kloonataksesi tietyn haaran:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Osittainen (sparse) kloonaus — minimaaliset tiedostot + vain valitut kansiot

Tämä käyttää osittaista kloonausta ja sparse-checkoutia (vaatii Git 2.25+ ja suositellaan modernia Git-versiota, jossa on osittaisen kloonauksen tuki):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Siirry repo-kansioon:

Bashille:

```bash
cd ai-agents-for-beginners
```

Powershellille:

```powershell
Set-Location ai-agents-for-beginners
```

Määritä sitten haluamasi kansiot (esimerkki alla näyttää kaksi kansiota):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Kun olet kloonannut ja varmistanut tiedostot, jos tarvitset vain tiedostoja ja haluat vapauttaa tilaa (ilman git-historiaa), poista repositorion metadata (💀 peruuttamaton — menetät kaikki Git-toiminnot: ei committeja, hakuja, pushauksia tai historian käyttöä).

Linux/macOS:

```bash
rm -rf .git
```

Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespacesin käyttö (suositeltu paikallisten suurten latausten välttämiseksi)

- Luo uusi Codespace tälle repolle [GitHub-käyttöliittymän](https://github.com/codespaces) kautta.  

- Uudessa Codespacessa avatussa terminaalissa suorita yksi yllä olevista pintakloonaus-/osittaiskloonaus-komennoista tuodaksesi vain tarvitsemasi oppituntikansiot Codespace-työtilaan.
- Valinnainen: kloonauksen jälkeen Codespacesissa poista .git vapauttaaksesi lisätilaa (katso poistokäskyt yllä).
- Huomio: Jos haluat avata repositorion suoraan Codespacesissa (ilman ylimääräistä kloonausta), huomaa, että Codespaces rakentaa devcontainer-ympäristön ja saattaa silti varata enemmän kuin tarvitset. Kloonaamalla pintakopion uudessa Codespacessa saat enemmän hallintaa levytilan käytöstä.

#### Vinkkejä

- Korvaa aina kloonaus-URL haarautumisellasi, jos haluat muokata/commitoida.
- Jos myöhemmin tarvitset lisää historiaa tai tiedostoja, voit hakea ne tai säätää sparse-checkoutia sisällyttämään lisää kansioita.

## Koodin suorittaminen

Tämä kurssi tarjoaa sarjan Jupyter Notebooks -tiedostoja, joita voit käyttää saadaksesi käytännön kokemusta AI-agenttien rakentamisesta.

Koodiesimerkit käyttävät joko:

**Vaatii GitHub-tilin - Ilmainen**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Merkitty nimellä (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Merkitty nimellä (autogen.ipynb)

**Vaatii Azure-tilauksen**:
3) Azure AI Foundry + Azure AI Agent Service. Merkitty nimellä (azureaiagent.ipynb)

Suosittelemme kokeilemaan kaikkia kolmea esimerkkiä nähdäksesi, mikä toimii sinulle parhaiten.

Valitsemasi vaihtoehto määrittää, mitkä asennusvaiheet sinun tulee suorittaa alla:

## Vaatimukset

- Python 3.12+
  - **NOTE**: Jos sinulla ei ole Python3.12 asennettuna, varmista, että asennat sen. Luo sitten venv python3.12:lla varmistaaksesi, että oikeat versiot asennetaan requirements.txt-tiedostosta.
  
    >Esimerkki

    Luo Python venv-hakemisto:

    ``` bash
    python3 -m venv venv
    ```

    Aktivoi sitten venv-ympäristö:

    macOS ja Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- GitHub-tili - Pääsy GitHub Models Marketplaceen
- Azure-tilaus - Pääsy Azure AI Foundryyn
- Azure AI Foundry -tili - Pääsy Azure AI Agent Serviceen

Olemme sisällyttäneet `requirements.txt`-tiedoston tämän repositorion juureen, joka sisältää kaikki tarvittavat Python-paketit koodiesimerkkien suorittamiseen.

Voit asentaa ne suorittamalla seuraavan komennon terminaalissa repositorion juuressa:

```bash
pip install -r requirements.txt
```
Suosittelemme luomaan Python-virtuaaliympäristön välttääksesi ristiriitoja ja ongelmia.

## VSCode-asennus
Varmista, että käytät oikeaa Python-versiota VSCode:ssa.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Näytteiden asennus GitHub Models -käyttöön 

### Vaihe 1: Hanki GitHubin henkilökohtainen käyttöoikeustoken (PAT)

Tämä kurssi hyödyntää GitHub Models Marketplacea, joka tarjoaa ilmaisen pääsyn suuriin kielimalleihin (LLM), joita käytät AI-agenttien rakentamiseen.

GitHub Models -käyttöön tarvitset [GitHubin henkilökohtaisen käyttöoikeustokenin](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Tämä onnistuu menemällä <a href="https://github.com/settings/personal-access-tokens" target="_blank">henkilökohtaisten käyttöoikeustokenien asetuksiin</a> GitHub-tililläsi.

Noudata [vähimmän oikeuden periaatetta](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) luodessasi tokenia. Tämä tarkoittaa, että sinun tulisi antaa tokenille vain ne oikeudet, joita se tarvitsee kurssin koodiesimerkkien suorittamiseen.

1. Valitse `Fine-grained tokens` -vaihtoehto näytön vasemmasta reunasta siirtymällä **Developer settings** -kohtaan.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.fi.png)

    Valitse sitten `Generate new token`.

    ![Luo token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.fi.png)

2. Anna tokenille kuvaava nimi, joka heijastaa sen tarkoitusta, jotta se on helppo tunnistaa myöhemmin.


    🔐 Tokenin kestoa koskeva suositus

    Suositeltu kesto: 30 päivää
    Turvallisemman käytännön vuoksi voit valita lyhyemmän ajanjakson—esimerkiksi 7 päivää 🛡️
    Se on hyvä tapa asettaa henkilökohtainen tavoite ja suorittaa kurssi, kun oppimisen motivaatio on korkealla 🚀.

    ![Tokenin nimi ja voimassaoloaika](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.fi.png)

3. Rajoita tokenin käyttöoikeus tämän repositorion haarautumiseen.

    ![Rajoita käyttöoikeus haarautuneeseen repositorioon](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.fi.png)

4. Rajoita tokenin käyttöoikeudet: **Permissions**-kohdassa, klikkaa **Account**-välilehteä ja paina "+ Add permissions" -painiketta. Avautuu pudotusvalikko. Etsi **Models** ja valitse sen ruutu.
    ![Lisää Models-käyttöoikeus](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.fi.png)

5. Varmista tarvittavat käyttöoikeudet ennen tokenin luomista. ![Varmista käyttöoikeudet](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.fi.png)

6. Ennen tokenin luomista varmista, että olet valmis tallentamaan tokenin turvalliseen paikkaan, kuten salasananhallintaohjelmaan, sillä sitä ei näytetä uudelleen luomisen jälkeen. ![Tallenna token turvallisesti](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.fi.png)

Kopioi juuri luomasi token. Lisää se nyt tähän kurssiin sisältyvään `.env`-tiedostoon.


### Vaihe 2: Luo `.env`-tiedosto

Luo `.env`-tiedosto suorittamalla seuraava komento terminaalissasi.

```bash
cp .env.example .env
```

Tämä kopioi esimerkkitiedoston ja luo `.env`-tiedoston hakemistoosi, jossa täytät ympäristömuuttujien arvot.

Kun olet kopioinut tokenisi, avaa `.env`-tiedosto suosikkitekstieditorissasi ja liitä token `GITHUB_TOKEN`-kenttään.
![GitHub Token -kenttä](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.fi.png)


Nyt sinun pitäisi pystyä suorittamaan tämän kurssin koodiesimerkit.

## Azure AI Foundry- ja Azure AI Agent Service -näytteiden asennus

### Vaihe 1: Hanki Azure-projektisi päätepiste


Seuraa ohjeita hubin ja projektin luomiseksi Azure AI Foundryssa täältä: [Hub-resurssien yleiskatsaus](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


Kun olet luonut projektisi, sinun täytyy hankkia projektisi yhteysmerkkijono.

Tämä onnistuu menemällä projektisi **Yleiskatsaus**-sivulle Azure AI Foundry -portaalissa.

![Projektin yhteysmerkkijono](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.fi.png)

### Vaihe 2: Luo `.env`-tiedosto

Luo `.env`-tiedosto suorittamalla seuraava komento terminaalissasi.

```bash
cp .env.example .env
```

Tämä kopioi esimerkkitiedoston ja luo `.env`-tiedoston hakemistoosi, jossa täytät ympäristömuuttujien arvot.

Kun olet kopioinut tokenisi, avaa `.env`-tiedosto suosikkitekstieditorissasi ja liitä token `PROJECT_ENDPOINT`-kenttään.

### Vaihe 3: Kirjaudu Azureen

Turvallisuuskäytännön mukaisesti käytämme [avaimetonta autentikointia](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) kirjautuaksemme Azure OpenAI:hin Microsoft Entra ID:n avulla. 

Avaa seuraavaksi terminaali ja suorita `az login --use-device-code` kirjautuaksesi Azure-tilillesi.

Kun olet kirjautunut sisään, valitse tilauksesi terminaalissa.


## Lisäympäristömuuttujat - Azure Search ja Azure OpenAI 

Agentic RAG -oppitunnille - oppitunti 5 - on näytteitä, jotka käyttävät Azure Searchia ja Azure OpenAI:ta.

Jos haluat suorittaa nämä näytteet, sinun täytyy lisätä seuraavat ympäristömuuttujat `.env`-tiedostoosi:

### Yleiskatsaus-sivu (Projekti)

- `AZURE_SUBSCRIPTION_ID` - Tarkista **Projektin tiedot** projektisi **Yleiskatsaus**-sivulta.

- `AZURE_AI_PROJECT_NAME` - Katso projektisi **Yleiskatsaus**-sivun yläosasta.

- `AZURE_OPENAI_SERVICE` - Löydät tämän **Sisältyvät ominaisuudet**-välilehdeltä **Azure OpenAI Service** -kohdasta **Yleiskatsaus**-sivulla.

### Hallintakeskus

- `AZURE_OPENAI_RESOURCE_GROUP` - Mene **Projektin ominaisuudet**-kohtaan **Yleiskatsaus**-sivulla **Hallintakeskuksessa**.

- `GLOBAL_LLM_SERVICE` - **Liitetyt resurssit**-kohdassa, etsi **Azure AI Services** -yhteyden nimi. Jos ei ole listattu, tarkista **Azure-portaali** resurssiryhmästäsi AI Services -resurssin nimi.

### Mallit + Päätepisteet -sivu

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Valitse upotusmallisi (esim. `text-embedding-ada-002`) ja huomioi **Deployment name** mallin tiedoista.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Valitse chat-mallisi (esim. `gpt-4o-mini`) ja huomioi **Deployment name** mallin tiedoista.

### Azure-portaali

- `AZURE_OPENAI_ENDPOINT` - Etsi **Azure AI services**, klikkaa sitä, mene **Resurssien hallinta**, **Avaimet ja päätepiste**, selaa alas "Azure OpenAI endpoints" kohtaan ja kopioi se, jossa lukee "Language APIs".

- `AZURE_OPENAI_API_KEY` - Samalta näytöltä, kopioi AVAIN 1 tai AVAIN 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Etsi **Azure AI Search** -resurssisi, klikkaa sitä ja katso **Yleiskatsaus**.

- `AZURE_SEARCH_API_KEY` - Mene sitten **Asetukset** ja sitten **Avaimet** kopioidaksesi ensisijaisen tai toissijaisen hallinta-avaimen.

### Ulkoinen verkkosivu

- `AZURE_OPENAI_API_VERSION` - Käy [API-version elinkaari](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) -sivulla kohdassa **Viimeisin GA API -julkaisu**.

### Avaimeton autentikointi

Sen sijaan, että kovakoodaisimme tunnistetietosi, käytämme avaimetonta yhteyttä Azure OpenAI:n kanssa. Tätä varten tuomme `DefaultAzureCredential`-luokan ja kutsumme myöhemmin `DefaultAzureCredential`-funktiota saadaksemme tunnistetiedot.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Jäikö jokin epäselväksi?
Jos sinulla on ongelmia tämän asennuksen kanssa, liity <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordiin</a> tai <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">luo ongelmaraportti</a>.

## Seuraava oppitunti

Olet nyt valmis suorittamaan kurssin koodin. Mukavia hetkiä AI-agenttien maailmaan tutustuessa!

[Johdatus AI-agentteihin ja niiden käyttötapauksiin](../01-intro-to-ai-agents/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.