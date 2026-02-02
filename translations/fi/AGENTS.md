# AGENTS.md

## Projektin yleiskatsaus

Tämä arkisto sisältää "AI Agents for Beginners" -koulutuskokonaisuuden, joka opettaa kaiken tarvittavan tekoälyagenttien rakentamiseen. Kurssi koostuu yli 15 oppitunnista, jotka kattavat perusteet, suunnittelumallit, kehykset ja tekoälyagenttien tuotantoon viemisen.

**Keskeiset teknologiat:**
- Python 3.12+
- Jupyter Notebookit interaktiiviseen oppimiseen
- Tekoälykehykset: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI -palvelut: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (ilmainen taso saatavilla)

**Arkkitehtuuri:**
- Oppituntipohjainen rakenne (hakemistot 00-15+)
- Jokainen oppitunti sisältää: README-dokumentaation, koodiesimerkit (Jupyter-notebookit) ja kuvia
- Monikielinen tuki automatisoidun käännösjärjestelmän avulla
- Useita kehysvaihtoehtoja per oppitunti (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Asennuskomennot

### Esivaatimukset
- Python 3.12 tai uudempi
- GitHub-tili (GitHub Models - ilmainen taso)
- Azure-tilaus (valinnainen, Azure AI -palveluille)

### Alkuasennus

1. **Kloonaa tai haarauta arkisto:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Luo ja aktivoi Python-virtuaaliympäristö:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Asenna riippuvuudet:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Määritä ympäristömuuttujat:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### Tarvittavat ympäristömuuttujat

**GitHub Models (ilmainen):**
- `GITHUB_TOKEN` - Henkilökohtainen käyttöoikeustunnus GitHubista

**Azure AI -palvelut** (valinnainen):
- `PROJECT_ENDPOINT` - Azure AI Foundry -projektin päätepiste
- `AZURE_OPENAI_API_KEY` - Azure OpenAI -API-avain
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI -päätepisteen URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Chat-mallin käyttöönoton nimi
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Upotusten käyttöönoton nimi
- Lisäasetukset löytyvät tiedostosta `.env.example`

## Kehitystyön kulku

### Jupyter-notebookien suorittaminen

Jokainen oppitunti sisältää useita Jupyter-notebookeja eri kehyksille:

1. **Käynnistä Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Siirry oppituntihakemistoon** (esim. `01-intro-to-ai-agents/code_samples/`)

3. **Avaa ja suorita notebookit:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel -kehys
   - `*-autogen.ipynb` - AutoGen-kehys
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Azure AI Agent Service

### Työskentely eri kehysten kanssa

**Semantic Kernel + GitHub Models:**
- Ilmainen taso saatavilla GitHub-tilillä
- Hyvä oppimiseen ja kokeiluun
- Tiedostomalli: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Ilmainen taso saatavilla GitHub-tilillä
- Moniagenttien orkestrointikyvyt
- Tiedostomalli: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoftin uusin kehys
- Saatavilla Pythonilla ja .NET:llä
- Tiedostomalli: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Vaatii Azure-tilauksen
- Tuotantovalmiit ominaisuudet
- Tiedostomalli: `*-azureaiagent.ipynb`

## Testausohjeet

Tämä on opetusarkisto, joka sisältää esimerkkikoodia eikä tuotantokoodia automaattisilla testeillä. Tarkista asennuksesi ja muutoksesi seuraavasti:

### Manuaalinen testaus

1. **Testaa Python-ympäristö:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Testaa notebookien suoritus:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Varmista ympäristömuuttujat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Yksittäisten notebookien suorittaminen

Avaa notebookit Jupyterissä ja suorita solut järjestyksessä. Jokainen notebook on itsenäinen ja sisältää:
- Tuontilauseet
- Konfiguraation lataus
- Esimerkkitoteutukset agenteille
- Odotetut tulokset markdown-soluissa

## Koodityyli

### Python-käytännöt

- **Python-versio**: 3.12+
- **Koodityyli**: Noudata Pythonin PEP 8 -käytäntöjä
- **Notebookit**: Käytä selkeitä markdown-soluja konseptien selittämiseen
- **Tuonnit**: Ryhmittele standardikirjasto, kolmannen osapuolen ja paikalliset tuonnit

### Jupyter-notebookien käytännöt

- Sisällytä kuvailevat markdown-solut ennen koodisoluja
- Lisää tulosesimerkkejä notebookeihin viitteeksi
- Käytä selkeitä muuttujanimiä, jotka vastaavat oppituntien konsepteja
- Pidä notebookien suoritusjärjestys lineaarisena (solu 1 → 2 → 3...)

### Tiedostojen järjestely

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## Rakentaminen ja käyttöönotto

### Dokumentaation rakentaminen

Tämä arkisto käyttää Markdownia dokumentaatioon:
- README.md-tiedostot jokaisessa oppituntihakemistossa
- Pää-README.md arkiston juurihakemistossa
- Automatisoitu käännösjärjestelmä GitHub Actionsin kautta

### CI/CD-putki

Sijaitsee hakemistossa `.github/workflows/`:

1. **co-op-translator.yml** - Automaattinen käännös yli 50 kielelle
2. **welcome-issue.yml** - Tervetuloviesti uusille issue-tekijöille
3. **welcome-pr.yml** - Tervetuloviesti uusille pull request -tekijöille

### Käyttöönotto

Tämä on opetusarkisto - ei käyttöönottoprosessia. Käyttäjät:
1. Haarauttavat tai kloonaavat arkiston
2. Suorittavat notebookit paikallisesti tai GitHub Codespacesissa
3. Oppivat muokkaamalla ja kokeilemalla esimerkkejä

## Pull Request -ohjeet

### Ennen lähettämistä

1. **Testaa muutoksesi:**
   - Suorita kaikki vaikuttavat notebookit kokonaan
   - Varmista, että kaikki solut suorittuvat ilman virheitä
   - Tarkista, että tulokset ovat asianmukaisia

2. **Dokumentaation päivitykset:**
   - Päivitä README.md, jos lisäät uusia konsepteja
   - Lisää kommentteja notebookeihin monimutkaiselle koodille
   - Varmista, että markdown-solut selittävät tarkoituksen

3. **Tiedostomuutokset:**
   - Älä sitoudu `.env`-tiedostoja (käytä `.env.example`)
   - Älä sitoudu `venv/`- tai `__pycache__/`-hakemistoja
   - Säilytä notebookien tulokset, kun ne havainnollistavat konsepteja
   - Poista väliaikaiset tiedostot ja varmuuskopiot (`*-backup.ipynb`)

### PR-otsikon muoto

Käytä kuvailevia otsikoita:
- `[Lesson-XX] Lisää uusi esimerkki <konsepti>`
- `[Fix] Korjaa kirjoitusvirhe lesson-XX README:ssä`
- `[Update] Paranna koodiesimerkkiä lesson-XX:ssa`
- `[Docs] Päivitä asennusohjeet`

### Vaaditut tarkistukset

- Notebookien tulee suorittua ilman virheitä
- README-tiedostojen tulee olla selkeitä ja tarkkoja
- Noudata arkiston olemassa olevia koodimalleja
- Säilytä yhdenmukaisuus muiden oppituntien kanssa

## Lisähuomioita

### Yleiset sudenkuopat

1. **Python-version yhteensopimattomuus:**
   - Varmista, että käytät Python 3.12+:aa
   - Jotkin paketit eivät toimi vanhemmilla versioilla
   - Käytä `python3 -m venv` määrittääksesi Python-version

2. **Ympäristömuuttujat:**
   - Luo aina `.env` tiedostosta `.env.example`
   - Älä sitoudu `.env`-tiedostoa (se on `.gitignore`-tiedostossa)
   - GitHub-tunnuksella tulee olla asianmukaiset oikeudet

3. **Pakettien ristiriidat:**
   - Käytä uutta virtuaaliympäristöä
   - Asenna `requirements.txt`-tiedostosta yksittäisten pakettien sijaan
   - Jotkin notebookit saattavat vaatia lisäpaketteja, jotka mainitaan niiden markdown-soluissa

4. **Azure-palvelut:**
   - Azure AI -palvelut vaativat aktiivisen tilauksen
   - Jotkin ominaisuudet ovat aluekohtaisia
   - Ilmaisen tason rajoitukset koskevat GitHub Models -malleja

### Oppimispolku

Suositeltu eteneminen oppitunneilla:
1. **00-course-setup** - Aloita tästä ympäristön asennuksella
2. **01-intro-to-ai-agents** - Ymmärrä tekoälyagenttien perusteet
3. **02-explore-agentic-frameworks** - Tutustu eri kehyksiin
4. **03-agentic-design-patterns** - Keskeiset suunnittelumallit
5. Jatka numeroitujen oppituntien läpi järjestyksessä

### Kehyksen valinta

Valitse kehys tavoitteidesi mukaan:
- **Oppiminen/prototyyppaus**: Semantic Kernel + GitHub Models (ilmainen)
- **Moniagenttijärjestelmät**: AutoGen
- **Uusimmat ominaisuudet**: Microsoft Agent Framework (MAF)
- **Tuotantokäyttö**: Azure AI Agent Service

### Avun saaminen

- Liity [Azure AI Foundry Community Discordiin](https://aka.ms/ai-agents/discord)
- Tarkista oppituntien README-tiedostot saadaksesi tarkempia ohjeita
- Katso pää-[README.md](./README.md) kurssin yleiskatsaukseen
- Viittaa [Course Setup](./00-course-setup/README.md) -ohjeisiin yksityiskohtaisissa asennusohjeissa

### Osallistuminen

Tämä on avoin opetusprojekti. Osallistuminen on tervetullutta:
- Paranna koodiesimerkkejä
- Korjaa kirjoitusvirheitä tai virheitä
- Lisää selventäviä kommentteja
- Ehdota uusia oppituntiaiheita
- Käännä lisäkielille

Katso [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) nykyiset tarpeet.

## Projektikohtainen konteksti

### Monikielinen tuki

Tämä arkisto käyttää automatisoitua käännösjärjestelmää:
- Yli 50 kieltä tuettuna
- Käännökset hakemistoissa `/translations/<kielikoodi>/`
- GitHub Actions -työnkulku käsittelee käännöspäivitykset
- Lähdetiedostot ovat englanniksi arkiston juurihakemistossa

### Oppituntien rakenne

Jokainen oppitunti noudattaa johdonmukaista mallia:
1. Videon pikkukuva ja linkki
2. Kirjallinen oppituntisisältö (README.md)
3. Koodiesimerkit useilla kehyksillä
4. Oppimistavoitteet ja esivaatimukset
5. Linkitetyt lisäoppimisresurssit

### Koodiesimerkkien nimeäminen

Muoto: `<oppitunti-numero>-<kehys-nimi>.ipynb`
- `04-semantic-kernel.ipynb` - Oppitunti 4, Semantic Kernel
- `07-autogen.ipynb` - Oppitunti 7, AutoGen
- `14-python-agent-framework.ipynb` - Oppitunti 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Oppitunti 14, MAF .NET

### Erityishakemistot

- `translated_images/` - Lokalisoidut kuvat käännöksiä varten
- `images/` - Alkuperäiset kuvat englanninkieliselle sisällölle
- `.devcontainer/` - VS Code -kehityskontin konfiguraatio
- `.github/` - GitHub Actions -työnkulut ja mallit

### Riippuvuudet

Keskeiset paketit tiedostosta `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen-kehys
- `semantic-kernel` - Semantic Kernel -kehys
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI -palvelut
- `azure-search-documents` - Azure AI Search -integraatio
- `chromadb` - Vektorikanta RAG-esimerkeille
- `chainlit` - Chat-käyttöliittymäkehys
- `browser_use` - Selaimen automaatio agenteille
- `mcp[cli]` - Model Context Protocol -tuki
- `mem0ai` - Muistinhallinta agenteille

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.