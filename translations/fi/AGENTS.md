# AGENTS.md

## Projektin yleiskatsaus

Tämä arkisto sisältää "AI Agents for Beginners" -laajan koulutuskokonaisuuden, joka opettaa kaiken tarvittavan AI-agenttien rakentamiseen. Kurssi koostuu yli 15 oppitunnista, jotka kattavat perusteet, suunnittelumallit, kehysratkaisut ja AI-agenttien käyttöönoton tuotantoon.

**Keskeiset teknologiat:**
- Python 3.12+
- Jupyter-muistikirjat interaktiiviseen oppimiseen
- AI-kehykset: Microsoft Agent Framework (MAF)
- Azure AI -palvelut: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkkitehtuuri:**
- Oppituntirakenteinen (00-15+ hakemistot)
- Jokainen oppitunti sisältää: README-dokumentaation, koodiesimerkkejä (Jupyter-muistikirjoja) ja kuvia
- Monikielinen tuki automaattisen käännösjärjestelmän kautta
- Yksi Python-muistikirja per oppitunti käyttäen Microsoft Agent Frameworkia

## Asennuskomennot

### Esivaatimukset
- Python 3.12 tai uudempi
- Azure-tilaus (Azure AI Foundrylle)
- Azure CLI asennettuna ja todennettuna (`az login`)

### Alkuasetukset

1. **Kloonaa tai forkkaa arkisto:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # TAI
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Luo ja ota käyttöön Python-virtuaaliympäristö:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windowsilla: venv\Scripts\activate
   ```

3. **Asenna riippuvuudet:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aseta ympäristömuuttujat:**
   ```bash
   cp .env.example .env
   # Muokkaa .env tiedostoa API-avaimillasi ja päätepisteilläsi
   ```

### Pakolliset ympäristömuuttujat

Azure AI Foundrylle (vaaditaan):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundryn projekti-endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mallin käyttöönoton nimi (esim. gpt-4o)

Azure AI Search (Oppitunti 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-avain

Todennus: Suorita `az login` ennen muistikirjojen ajoa (käyttää `AzureCliCredential`).

## Kehitystyön kulku

### Jupyter-muistikirjojen suorittaminen

Jokaisella oppitunnilla useita Jupyter-muistikirjoja eri kehyksille:

1. **Käynnistä Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Siirry oppituntihakemistoon** (esim. `01-intro-to-ai-agents/code_samples/`)

3. **Avaa ja suorita muistikirjat:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Frameworkia (Python) käyttäen
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Frameworkia (.NET) käyttäen

### Microsoft Agent Frameworkin käyttö

**Microsoft Agent Framework + Azure AI Foundry:**
- Vaatii Azure-tilauksen
- Käyttää `AzureAIProjectAgentProvider` Agent Service V2:lle (agentit näkyvissä Foundry-portaalissa)
- Tuotantokelpoinen sisäänrakennetulla havaittavuudella
- Tiedostokuvio: `*-python-agent-framework.ipynb`

## Testiohjeet

Tämä on opetusarkisto esimerkkikoodilla, ei tuotantokoodilla automaattisilla testeillä. Varmista asetukset ja muutokset seuraavasti:

### Manuaalinen testaus

1. **Testaa Python-ympäristö:**
   ```bash
   python --version  # Pitäisi olla 3.12 tai uudempi
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testaa muistikirjojen suoritus:**
   ```bash
   # Muunna muistikirja skriptiksi ja suorita (testaa tuonnit)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Varmista ympäristömuuttujat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Yksittäisten muistikirjojen suoritus

Avaa muistikirjat Jupyteriä käyttäen ja suorita solut peräkkäin. Jokainen muistikirja on itsenäinen ja sisältää:
- Tuontilauseet
- Konfiguraation latauksen
- Esimerkkien agenttien toteutukset
- Odotetut tulosteet markdown-soluissa

## Koodityyli

### Python-konventiot

- **Python-versio**: 3.12+
- **Koodityyli**: Noudata standardia PEP 8 -koodityyliä
- **Muistikirjat**: Käytä selkeitä markdown-soluja konseptien selittämiseen
- **Tuonnit**: Ryhmittele standardikirjaston, kolmannen osapuolen ja paikalliset tuonnit

### Jupyter-muistikirjat

- Sisällytä kuvailevia markdown-soluja ennen koodisoluja
- Lisää muistikirjoihin esimerkkitulosteita viitteeksi
- Käytä selkeitä muuttujan nimiä, jotka vastaavat oppitunnin käsitteitä
- Pidä muistikirjan suoritusjärjestys lineaarisena (solu 1 → 2 → 3...)

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

Tämä arkisto käyttää Markdownia dokumentaatiossa:
- README.md-tiedostot kussakin oppituntikansiossa
- Pää-README.md arkiston juuressa
- Automaattinen käännösjärjestelmä GitHub Actionsin kautta

### CI/CD-putki

Sijaitsee kansiossa `.github/workflows/`:

1. **co-op-translator.yml** - Automaattinen käännös yli 50 kielelle
2. **welcome-issue.yml** - Toivottaa uudet issuejen tekijät tervetulleiksi
3. **welcome-pr.yml** - Toivottaa uudet pull requestien tekijät tervetulleiksi

### Käyttöönotto

Tämä on opetusarkisto – ei käyttöönottoprosessia. Käyttäjät:
1. Forkkaa tai kloonaa arkisto
2. Suorittavat muistikirjat paikallisesti tai GitHub Codespacesissa
3. Oppivat muokkaamalla ja kokeilemalla esimerkkejä

## Pull Request -ohjeet

### Ennen lähettämistä

1. **Testaa muutoksesi:**
   - Suorita kokonaan vaikutetut muistikirjat
   - Varmista, että kaikki solut suorittuvat ilman virheitä
   - Tarkista, että tulosteet ovat asianmukaisia

2. **Dokumentaatiopäivitykset:**
   - Päivitä README.md, jos lisäät uusia käsitteitä
   - Lisää kommentteja muistikirjoihin monimutkaisesta koodista
   - Varmista, että markdown-solut selittävät tarkoituksen

3. **Tiedostojen muutokset:**
   - Vältä `.env`-tiedostojen sitomista (käytä `.env.example`-tiedostoa)
   - Älä commitoi `venv/` tai `__pycache__/` hakemistoja
   - Säilytä muistikirjan tulosteet, kun ne havainnollistavat käsitteitä
   - Poista väliaikaiset tiedostot ja varmuuskopiotiedostot (`*-backup.ipynb`)

### PR-otsikon muoto

Käytä kuvaavia otsikoita:
- `[Lesson-XX] Lisää esimerkki aiheesta <concept>`
- `[Fix] Korjaa kirjoitusvirhe oppitunti-XX README:ssä`
- `[Update] Paranna koodiesimerkkiä oppitunti-XX`
- `[Docs] Päivitä asennusohjeet`

### Pakolliset tarkastukset

- Muistikirjojen tulee toimia ilman virheitä
- README-tiedostojen tulee olla selkeitä ja tarkkoja
- Noudata arkiston olemassa olevia koodimalleja
- Säilytä yhdenmukaisuus muiden oppituntien kanssa

## Lisätiedot

### Yleiset sudenkuopat

1. **Python-version yhteensopimattomuus:**
   - Varmista Python 3.12+ käyttö
   - Jotkin paketit eivät toimi vanhemmilla versioilla
   - Käytä `python3 -m venv` määrittääksesi Python-version eksplisiittisesti

2. **Ympäristömuuttujat:**
   - Luo aina `.env` `.env.example`-pohjasta
   - Älä sitomisiin `.env`-tiedostoa (se on .gitignore:ssa)
   - GitHub-tokenin pitää olla oikeilla käyttöoikeuksilla

3. **Paketin ristiriidat:**
   - Käytä uutta virtuaaliympäristöä
   - Asenna riippuvuudet `requirements.txt`:stä yksittäisten pakettien sijaan
   - Jotkin muistikirjat saattavat vaatia lisäpaketteja, jotka näkyvät niiden markdown-soluissa

4. **Azure-palvelut:**
   - Azure AI -palvelut edellyttävät aktiivista tilausta
   - Jotkin ominaisuudet ovat aluekohtaisia
   - Ilmaisversion rajoitukset koskevat GitHub-malleja

### Oppimispolku

Suositeltu eteneminen oppituntien läpi:
1. **00-course-setup** - Aloita ympäristön asetuksista
2. **01-intro-to-ai-agents** - Ymmärrä AI-agenttien perusteet
3. **02-explore-agentic-frameworks** - Tutustu erilaisiin kehyksiin
4. **03-agentic-design-patterns** - Keskeiset suunnittelumallit
5. Jatka numeroitujen oppituntien mukaan peräkkäin

### Kehyksen valinta

Valitse kehys tavoitteidesi mukaan:
- **Kaikki oppitunnit**: Microsoft Agent Framework (MAF) käyttäen `AzureAIProjectAgentProvider`
- Agentit rekisteröityvät palvelinpuolella Azure AI Foundry Agent Service V2:ssa ja näkyvät Foundry-portaalissa

### Apua saatavilla

- Liity [Microsoft Foundry Community Discordiin](https://aka.ms/ai-agents/discord)
- Tutustu oppituntien README-tiedostoihin ohjeiden saamiseksi
- Katso pää-README.md kurssin yleiskuvaukseen
- Katso [Course Setup](./00-course-setup/README.md) yksityiskohtaisia asennusohjeita varten

### Osallistuminen

Tämä on avoin opetushanke. Osallistumisia otetaan vastaan:
- Paranna koodiesimerkkejä
- Korjaa kirjoitusvirheitä tai virheitä
- Lisää selventäviä kommentteja
- Ehdota uusia oppitunteja
- Käännä lisäkielille

Katso [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) käynnissä olevista tarpeista.

## Projektikohtainen konteksti

### Monikielinen tuki

Tämä arkisto käyttää automaattista käännösjärjestelmää:
- Yli 50 kieltä tuettu
- Käännökset hakemistoissa `/translations/<lang-code>/`
- GitHub Actions -työnkulku hoitaa käännöspäivitykset
- Lähdetiedostot ovat englanniksi arkiston juuressa

### Oppituntirakenne

Jokainen oppitunti noudattaa yhtenäistä kaavaa:
1. Videon pikkukuva linkillä
2. Kirjoitettu oppituntisisältö (README.md)
3. Koodiesimerkit useissa kehyksissä
4. Oppimistavoitteet ja esivaatimukset
5. Lisäoppimateriaalien linkitykset

### Koodiesimerkkien nimeäminen

Muoto: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Oppitunti 1, MAF Python
- `14-sequential.ipynb` - Oppitunti 14, MAF edistyneet mallit

### Erityishakemistot

- `translated_images/` - Käännetyt kuvat käännöksiä varten
- `images/` - Alkuperäiset kuvat englanninkieliselle sisällölle
- `.devcontainer/` - VS Code -kehityssäiliön konfiguraatio
- `.github/` - GitHub Actions -työnkulut ja mallit

### Riippuvuudet

Keskeiset paketit `requirements.txt`-tiedostosta:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokollatuki
- `azure-ai-inference`, `azure-ai-projects` - Azure AI -palvelut
- `azure-identity` - Azure-todennus (AzureCliCredential)
- `azure-search-documents` - Azure AI Search -integraatio
- `mcp[cli]` - Model Context Protocol -tuki

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->