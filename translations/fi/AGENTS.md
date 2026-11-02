# AGENTS.md

## Projektin yleiskatsaus

Tämä repositorio sisältää "AI Agents for Beginners" -oppimateriaalin, joka on kattava koulutuskokonaisuus, joka opettaa kaiken tarvittavan AI-agenttien rakentamiseen. Kurssi koostuu 18 oppitunnista (numeroitu 00-18), jotka kattavat perusteet, suunnittelumallit, kehykset, tuotantoon vienti, paikalliset/laitteella toimivat agentit ja AI-agenttien turvallisuuden.

**Keskeiset teknologiat:**
- Python 3.12+
- Jupyter-muistiinpanot vuorovaikutteiseen oppimiseen
- AI-kehykset: Microsoft Agent Framework (MAF)
- Azure AI -palvelut: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkkitehtuuri:**
- Oppituntipohjainen rakenne (00-18-kansiot)
- Jokainen oppitunti sisältää: README-dokumentaation, koodiesimerkkejä (Jupyter-muistiinpanot) ja kuvia
- Monikielinen tuki automaattisen käännösjärjestelmän kautta
- Yksi Python-muistiinpano per oppitunti käyttäen Microsoft Agent Frameworkia

## Asennuskomennot

### Esivaatimukset
- Python 3.12 tai uudempi
- Azure-tilaus (Microsoft Foundrylle)
- Azure CLI asennettuna ja autentikoituna (`az login`)

### Alkutoimet

1. **Kloonaa tai tee fork repositoriosta:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Luo ja aktivoi Pythonin virtuaaliympäristö:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Asenna riippuvuudet:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aseta ympäristömuuttujat:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Vaaditut ympäristömuuttujat

Microsoft Foundrylle (vaadittu):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry -projektin päätepiste
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mallin käyttöönoton nimi (esim. gpt-5-mini)

Azure AI Searchille (Oppitunti 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search -päätepiste
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-avain

Autentikointi: Suorita `az login` ennen muistiinpanojen ajamista (käyttää `AzureCliCredential`).

## Kehitysprosessi

### Jupyter-muistiinpanojen suorittaminen

Jokainen oppitunti sisältää useita Jupyter-muistiinpanoja eri kehyksille:

1. **Käynnistä Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Siirry oppituntikansioon** (esim. `01-intro-to-ai-agents/code_samples/`)

3. **Avaa ja suorita muistiinpanot:**
   - `*-python-agent-framework.ipynb` - Käyttäen Microsoft Agent Frameworkia (Python)
   - `*-dotnet-agent-framework.ipynb` - Käyttäen Microsoft Agent Frameworkia (.NET)

### Työskentely Microsoft Agent Frameworkin kanssa

Microsoft Agent Framework + Microsoft Foundry:
- Vaatii Azure-tilauksen
- Käyttää `FoundryChatClient` Agent Service V2:lle (agentit näkyvissä Foundry-portaalissa)
- Tuotantovalmius sisäänrakennetulla havaittavuudella
- Tiedostokuvio: `*-python-agent-framework.ipynb`

## Testausohjeet

Tämä on opetuksellinen repositorio, joka sisältää esimerkkikoodia, ei tuotantokoodia automaattisilla testeillä. Varmistaaksesi asennuksesi ja muutokset:

### Manuaalinen testaus

1. **Testaa Python-ympäristö:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testaa muistiinpanojen suoritus:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Varmista ympäristömuuttujat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Yksittäisten muistiinpanojen suorittaminen

Avaa muistiinpanot Jupyterissa ja suorita solut peräkkäin. Jokainen muistiinpano on itsenäinen ja sisältää:
- Tuontilauseet
- Konfiguraation lataamisen
- Esimerkkitoimintojen toteutukset
- Odotetut tulosteet markdown-soluissa

### Räkätestaus käyttöön otetuilla agenteilla

Oppitunneilla, joissa agentti on käyttöön otettu Microsoft Foundryn isännöimänä agenttina (01, 04, 05, 16), repositorio sisältää räkätestauskatalogit `tests/`-kansiossa, joita suorittaa `.github/workflows/smoke-test.yml`-työnkulku AI Smoke Test -toiminnon ([AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)) avulla. Nämä ovat kevyitä julkaisuportteja (onko agenttiin yhteys ja noudattaako se peruskehotemalleja?), jotka täydentävät arviointiputkea oppitunneilla 10 ja 16. Katso [tests/README.md](./tests/README.md) katalogin, oppitunnin ja agentin välinen vastaavuus. Oppitunti 17 ajetaan paikallisesti Foundry Localin kanssa eikä sillä ole isännöityä päätepistettä, joten sitä validoidaan suorittamalla sen muistiinpano suoraan.

## Koodityyli

### Python-käytännöt

- Python-versio: 3.12+
- Koodityyli: Noudata tavallisia Python PEP 8 -käytäntöjä
- Muistiinpanot: Käytä selkeitä markdown-soluja konseptien selittämiseen
- Tuodut kirjastot: Ryhmittele standardikirjasto, kolmannen osapuolen ja paikalliset tuonnit

### Jupyter-muistiinpanojen käytännöt

- Sisällytä kuvailevia markdown-soluja ennen koodisoluja
- Lisää lähtöesimerkkejä muistiinpanoihin viitteeksi
- Käytä selkeitä muuttujien nimiä, jotka vastaavat oppitunnin käsitteitä
- Pidä muistiinpanojen suoritusjärjestys lineaarisena (solu 1 → 2 → 3...)

### Tiedostojen järjestely

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Kääntäminen ja käyttöönotto

### Dokumentaation rakentaminen

Tämä repositorio käyttää Markdown-muotoa dokumentaatiossa:
- README.md -tiedostot kussakin oppituntikansiossa
- Pää-README.md repositorion juuressa
- Automaattinen käännösjärjestelmä GitHub Actionsin kautta

### CI/CD-putki

Sijaitsee `.github/workflows/`-kansiossa:

1. **co-op-translator.yml** - Automaattinen käännös yli 50 kielelle
2. **welcome-issue.yml** - Tervehtii uusia issueiden tekijöitä
3. **welcome-pr.yml** - Tervehtii uusia pull request -tekijöitä

### Käyttöönotto

Tämä on opetuksellinen repositorio - ei käyttöönottoprosessia. Käyttäjät:
1. Forkkaa tai kloonaa repositorio
2. Aja muistiinpanot paikallisesti tai GitHub Codespacesissa
3. Opiskele muokkaamalla ja kokeilemalla esimerkkejä

## Pull request -ohjeet

### Ennen lähettämistä

1. **Testaa muutokset:**
   - Suorita vaikutusalueen muistiinpanot kokonaan
   - Tarkista, että kaikki solut suorittuvat ilman virheitä
   - Varmista, että tulosteet ovat sopivia

2. **Dokumentaation päivitykset:**
   - Päivitä README.md, jos lisäät uusia käsitteitä
   - Lisää kommentteja muistiinpanoihin monimutkaisesta koodista
   - Varmista, että markdown-solut selittävät tarkoituksen

3. **Tiedostomuutokset:**
   - Vältä `.env`-tiedostojen commitoimista (käytä `.env.example`)
   - Älä commitoi `venv/` tai `__pycache__/` -kansioita
   - Säilytä muistiinpanojen tulosteet, kun ne havainnollistavat käsitteitä
   - Poista väliaikaiset tiedostot ja varakopiot (`*-backup.ipynb`)

### PR-otsikon muoto

Käytä kuvaavia otsikoita:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Vaaditut tarkastukset

- Muistiinpanojen tulee suorittua ilman virheitä
- README-tiedostojen tulee olla selkeitä ja tarkkoja
- Noudata olemassa olevia koodimalleja repositoriossa
- Säilytä yhtenäisyys muiden oppituntien kanssa

## Lisätietoja

### Yleisiä sudenkuoppia

1. **Python-version ristiriita:**
   - Varmista, että käytössä on Python 3.12+
   - Jotkut paketit eivät välttämättä toimi vanhemmilla versioilla
   - Käytä `python3 -m venv` määritelläksesi Python-version eksplisiittisesti

2. **Ympäristömuuttujat:**
   - Luo aina `.env` tiedostosta `.env.example`
   - Älä commitoi `.env` tiedostoa (se on `.gitignore`-kansiossa)
   - Kirjaudu sisään `az login` avulla avaimesidonnaiseen Entra ID -autentikointiin

3. **Paketin ristiriidat:**
   - Käytä uutta virtuaaliympäristöä
   - Asenna `requirements.txt` kautta, älä yksittäisiä paketteja
   - Joissakin muistiinpanoissa saattaa vaatia lisäpaketteja, jotka mainitaan niiden markdown-soluissa

4. **Azure-palvelut:**
   - Azure AI -palvelut vaativat aktiivisen tilauksen
   - Jotkut ominaisuudet ovat aluekohtaisia
   - Varmista, että Azure OpenAI -mallin käyttöönotto tukee Responses APIa

### Oppimispolku

Suositeltu eteneminen oppituntien läpi:
1. **00-course-setup** - Aloita täältä ympäristön asennukseen
2. **01-intro-to-ai-agents** - Ymmärrä AI-agenttien perusteet
3. **02-explore-agentic-frameworks** - Tutustu erilaisiin kehyksiin
4. **03-agentic-design-patterns** - Keskeiset suunnittelumallit
5. Jatka numeroidusti peräkkäin oppitunneissa

### Kehyksen valinta

Valitse kehys tavoitteidesi perusteella:
- Kaikissa oppitunneissa: Microsoft Agent Framework (MAF) käyttäen `FoundryChatClient`
- Agentit rekisteröityvät palvelinpuolella Microsoft Foundry Agent Service V2:ssa ja näkyvät Foundry-portaalissa

### Avun saaminen

- Liity [Microsoft Foundry Community Discordiin](https://aka.ms/ai-agents/discord)
- Tutustu oppituntien README-tiedostoihin saadaksesi tarkempia ohjeita
- Katso pää-README.md (./README.md) kurssin yleiskatsaukseen
- Katso [Course Setup](./00-course-setup/README.md) yksityiskohtaiset asennusohjeet

### Osallistuminen

Tämä on avoin koulutusprojekti. Osallistumista otetaan vastaan:
- Paranna koodiesimerkkejä
- Korjaa kirjoitusvirheitä tai virheitä
- Lisää selventäviä kommentteja
- Ehdota uusia oppitunteja
- Käännä lisäkielille

Katso [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) tämänhetkisiin tarpeisiin.

## Projektikohtainen konteksti

### Monikielinen tuki

Tämä repositorio käyttää automaattista käännösjärjestelmää:
- Yli 50 kieltä tuettuna
- Käännökset sijaitsevat `/translations/<lang-code>/` -kansioissa
- GitHub Actions -työnkulku huolehtii käännöspäivityksistä
- Lähdetiedostot ovat englanniksi repositorion juuressa

### Oppituntirakenne

Jokainen oppitunti noudattaa johdonmukaista rakennetta:
1. Video-thumbnail-linkki
2. Kirjallinen oppituntisisältö (README.md)
3. Koodiesimerkit eri kehyksissä
4. Oppimistavoitteet ja esivaatimukset
5. Lisäoppimateriaalit linkitettyinä

### Koodiesimerkkien nimeäminen

Muoto: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Oppitunti 1, MAF Python
- `14-sequential.ipynb` - Oppitunti 14, MAF edistyneet mallit
- `16-python-agent-framework.ipynb` - Oppitunti 16, tuotantotason asiakastukitoiminto
- `17-local-agent-foundry-local.ipynb` - Oppitunti 17, paikallinen agentti Foundry Localilla + Qwenillä

### Erikoiskansiot

- `translated_images/` - Paikallistetut kuvat käännöksille
- `images/` - Alkuperäiset kuvat englanninkieliselle sisällölle
- `.devcontainer/` - VS Code -kehityssäiliön asetukset
- `.github/` - GitHub Actions -työnkulut ja -mallit

### Riippuvuudet

Keskeiset paketit `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agenttien välinen protokollatuki
- `azure-ai-inference`, `azure-ai-projects` - Azure AI -palvelut
- `azure-identity` - Azure-autentikointi (AzureCliCredential)
- `azure-search-documents` - Azure AI Search -integraatio
- `mcp[cli]` - Model Context Protocol -tuki

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->