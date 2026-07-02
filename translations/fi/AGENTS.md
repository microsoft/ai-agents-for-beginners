# AGENTS.md

## Projektin yleiskatsaus

Tämä repositorio sisältää "AI Agents for Beginners" -kokonaisvaltaisen koulutuskokonaisuuden, joka opettaa kaiken tarvittavan tekoälyagenttien rakentamiseen. Kurssi koostuu 18 oppitunnista, jotka käsittelevät perusteita, suunnittelumalleja, kehityskehyksiä ja tekoälyagenttien tuotantoon viennin.

**Keskeiset teknologiat:**
- Python 3.12+
- Jupyter-muistikirjat interaktiiviseen oppimiseen
- AI-kehykset: Microsoft Agent Framework (MAF)
- Azure AI -palvelut: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkkitehtuuri:**
- Oppituntiperustainen rakenne (00-15+ hakemistot)
- Jokainen oppitunti sisältää: README-dokumentaation, koodiesimerkkejä (Jupyter-muistikirjat) ja kuvia
- Monikielituki automaattisen käännösjärjestelmän kautta
- Yksi Python-muistikirja per oppitunti, joka käyttää Microsoft Agent Frameworkia

## Asennuskomennot

### Esivaatimukset
- Python 3.12 tai uudempi
- Azure-tilaus (Azure AI Foundrylle)
- Azure CLI asennettuna ja autentikoituna (`az login`)

### Alkuasetukset

1. **Kloonaa tai haarauta repositorio:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # TAI
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Luo ja aktivoi Pythonin virtuaaliympäristö:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windowsissa: venv\Scripts\activate
   ```

3. **Asenna riippuvuudet:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Määritä ympäristömuuttujat:**
   ```bash
   cp .env.example .env
   # Muokkaa .env tiedostoa API-avaimillasi ja päätepisteilläsi
   ```

### Vaadittavat ympäristömuuttujat

**Azure AI Foundrylta** (pakollinen):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundryn projektin päätepiste
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mallin käyttöönoton nimi (esim. gpt-4o)

**Azure AI Searchille** (Oppitunti 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search -päätepiste
- `AZURE_SEARCH_API_KEY` - Azure AI Searchin API-avain

Autentikointi: Suorita `az login` ennen muistikirjojen ajoa (käyttää `AzureCliCredential`-luokkaa).

## Kehitystyön työnkulku

### Jupyter-muistikirjojen ajaminen

Jokainen oppitunti sisältää useita Jupyter-muistikirjoja eri kehyksille:

1. **Käynnistä Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Siirry oppitunnin hakemistoon** (esim. `01-intro-to-ai-agents/code_samples/`)

3. **Avaa ja suorita muistikirjat:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Frameworkin käyttö (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Frameworkin käyttö (.NET)

### Microsoft Agent Frameworkin käyttö

**Microsoft Agent Framework + Azure AI Foundry:**
- Edellyttää Azure-tilausta
- Käyttää `AzureAIProjectAgentProvider` Agent Service V2:lle (agentit näkyvät Foundry-portaalissa)
- Tuotantovalmis sisäänrakennetulla valvonnalla
- Tiedostomuoto: `*-python-agent-framework.ipynb`

## Testausohjeet

Tämä on koulutuksellinen repositorio, jossa on esimerkkikoodia eikä tuotantokoodia automaattisilla testeillä. Varmistaaksesi ympäristösi ja muutoksesi:

### Manuaalinen testaus

1. **Testaa Python-ympäristö:**
   ```bash
   python --version  # Pitäisi olla 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testaa muistikirjan suoritus:**
   ```bash
   # Muunna muistikirja skriptiksi ja suorita (testaa tuontia)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Varmista ympäristömuuttujat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Yksittäisten muistikirjojen ajaminen

Avaa muistikirjat Jupyterissa ja suorita solut peräkkäin. Jokainen muistikirja on itsenäinen ja sisältää:
- Tuontilauseet
- Asetusten latauksen
- Esimerkkitoiminnot agenteille
- Odotetut tulosteet markdown-soluissa

## Koodityyli

### Pythonin käytännöt

- **Python-versio:** 3.12+
- **Koodityyli:** Noudata standardia Python PEP 8 -käytäntöä
- **Muistikirjat:** Käytä selkeitä markdown-soluja käsitteiden selittämiseen
- **Tuonnit:** Ryhmittele vakio-, kolmannen osapuolen ja paikallisiin

### Jupyter-muistikirjojen käytännöt

- Sisällytä kuvaavia markdown-soluja ennen koodisoluja
- Lisää tulosten esimerkit muistikirjoihin viitteeksi
- Käytä selkeitä muuttujanimiä, jotka vastaavat oppitunnin käsitteitä
- Pidä muistikirjan suoritusjärjestys lineaarisena (solu 1 → 2 → 3…)

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

## Rakennus ja käyttöönotto

### Dokumentaation rakentaminen

Tässä repositoriossa käytetään Markdownia dokumentaatiolle:
- README.md-tiedostot jokaisessa oppituntikansiossa
- Pää-README.md repositorion juurissa
- Automaattinen käännösjärjestelmä GitHub Actionseilla

### CI/CD-putki

Sijaitsee kansiossa `.github/workflows/`:

1. **co-op-translator.yml** - Automaattinen käännös yli 50 kielelle
2. **welcome-issue.yml** - Tervehtii uusia issueiden luojia
3. **welcome-pr.yml** - Tervehtii uusia pull request -kontribuuttoreita

### Käyttöönotto

Tämä on koulutuksellinen repositorio - ei käyttöönottoprosessia. Käyttäjät:
1. Haarauttavat tai kloonaavat repositorion
2. Suorittavat muistikirjat paikallisesti tai GitHub Codespacesissa
3. Opiskelevat muokkaamalla ja kokeilemalla esimerkkejä

## Pull request -ohjeet

### Ennen lähettämistä

1. **Testaa muutoksesi:**
   - Suorita kaikki vaikuttuneet muistikirjat kokonaan
   - Varmista, että kaikki solut suoritetaan ilman virheitä
   - Tarkista, että tulosteet ovat sopivia

2. **Dokumentaation päivitykset:**
   - Päivitä README.md, jos lisäät uusia käsitteitä
   - Lisää kommentteja muistikirjoihin monimutkaista koodia varten
   - Varmista, että markdown-solut selittävät tarkoituksen

3. **Tiedostomuutokset:**
   - Vältä `.env`-tiedostojen tallentamista (käytä `.env.example` -tiedostoa)
   - Älä tallenna `venv/` tai `__pycache__/` -hakemistoja
   - Säilytä muistikirjojen tulosteet, kun ne havainnollistavat käsitteitä
   - Poista väliaikaiset tiedostot ja backup-muistikirjat (`*-backup.ipynb`)

### PR-otsikon muotoilu

Käytä kuvaavia otsikoita:
- `[Lesson-XX] Lisää uusi esimerkki aiheesta <concept>`
- `[Fix] Korjaa kirjoitusvirhe oppitunnin XX README:ssä`
- `[Update] Paranna koodiesimerkkiä oppitunnissa XX`
- `[Docs] Päivitä asennusohjeet`

### Vaadittavat tarkistukset

- Muistikirjojen tulee toimia ilman virheitä
- README-tiedostojen tulee olla selkeitä ja täsmällisiä
- Noudata olemassa olevia koodimalleja repositoriossa
- Säilytä johdonmukaisuus muiden oppituntien kanssa

## Lisätiedot

### Yleiset sudenkuopat

1. **Python-version yhteensopimattomuus:**
   - Varmista Python 3.12+ käyttö
   - Jotkin paketit eivät toimi vanhemmilla versioilla
   - Käytä `python3 -m venv` määrittämään Python-versio eksplisiittisesti

2. **Ympäristömuuttujat:**
   - Luo aina `.env` tiedosto `.env.example` pohjalta
   - Älä tallenna `.env`-tiedostoa (on `.gitignore`-listalla)
   - GitHub-tokenilla tulee olla asianmukaiset oikeudet

3. **Paketin ristiriidat:**
   - Käytä uutta virtuaaliympäristöä
   - Asenna paketit mieluummin `requirements.txt`-tiedostosta kuin yksitellen
   - Jotkin muistikirjat voivat vaatia lisäpaketteja, jotka mainitaan niiden markdown-soluissa

4. **Azure-palvelut:**
   - Azure AI -palvelut vaativat aktiivisen tilauksen
   - Osa ominaisuuksista on aluetta rajoitettuja
   - GitHub-malleihin sovelletaan ilmaisversion rajoituksia

### Oppimispolku

Suositeltu eteneminen oppitunneissa:
1. **00-course-setup** - Aloita tästä ympäristön asetuksissa
2. **01-intro-to-ai-agents** - Ymmärrä tekoälyagentin perusteet
3. **02-explore-agentic-frameworks** - Tutustu eri kehyksiin
4. **03-agentic-design-patterns** - Keskeiset suunnittelumallit
5. Jatka numeroiduilla oppitunneilla järjestyksessä

### Kehyksen valinta

Valitse kehys tavoitteidesi mukaisesti:
- **Kaikki oppitunnit**: Microsoft Agent Framework (MAF) `AzureAIProjectAgentProvider`-palvelulla
- **Agentit rekisteröityvät palvelinpuolella** Azure AI Foundry Agent Service V2:ssa ja näkyvät Foundry-portaalissa

### Apua saat

- Liity [Microsoft Foundry Community Discordiin](https://aka.ms/ai-agents/discord)
- Tutustu oppituntien README-tiedostoihin tarkempaa ohjeistusta varten
- Katso pää-README-tiedosto kurssin yleiskuvaukseen
- Katso [Course Setup](./00-course-setup/README.md) yksityiskohtaiset asennusohjeet

### Osallistuminen

Tämä on avoin koulutusprojekti. Panoksesi ovat tervetulleita:
- Paranna koodiesimerkkejä
- Korjaa kirjoitusvirheitä tai muita virheitä
- Lisää selventäviä kommentteja
- Ehdota uusia oppitunteja
- Käännä lisää kieliä

Katso [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) nykyiset tarvealueet.

## Projektikohtainen konteksti

### Monikielituki

Tämä repositorio käyttää automaattista käännösjärjestelmää:
- Yli 50 kieltä tuettuna
- Käännökset kansioissa `/translations/<lang-code>/`
- GitHub Actions -työnkulku päivittää käännökset automaattisesti
- Lähdetiedostot ovat englanniksi repositorion juuressa

### Oppituntirakenne

Jokainen oppitunti noudattaa yhtenäistä kaavaa:
1. Videoesikatselukuva linkillä
2. Kirjallinen oppituntisisältö (README.md)
3. Koodiesimerkit useissa kehyksissä
4. Oppimistavoitteet ja esivaatimukset
5. Lisäresurssit linkitettynä

### Koodiesimerkkien nimeäminen

Muoto: `<oppitunnin-numero>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Oppitunti 1, MAF Python
- `14-sequential.ipynb` - Oppitunti 14, MAF:n edistyneet mallit

### Erityishakemistot

- `translated_images/` - Paikallistetut kuvat käännöksiä varten
- `images/` - Alkuperäiset kuvat englanninkielisille sisällöille
- `.devcontainer/` - VS Code -kehityssäiliöasetukset
- `.github/` - GitHub Actions -työnkulut ja -mallit

### Riippuvuudet

Tärkeitä paketteja `requirements.txt`-tiedostosta:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent -protokollatuki
- `azure-ai-inference`, `azure-ai-projects` - Azure AI -palvelut
- `azure-identity` - Azure-autentikointi (AzureCliCredential)
- `azure-search-documents` - Azure AI Search -integraatio
- `mcp[cli]` - Model Context Protocol -tuki

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->