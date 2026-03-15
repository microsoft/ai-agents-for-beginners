# AGENTS.md

## Projektin yleiskuvaus

Tämä repositorio sisältää "AI Agents for Beginners" -oppimiskokonaisuuden, joka on kattava koulutuskokonaisuus, joka opettaa kaiken tarvittavan AI-agenttien rakentamiseen. Kurssi koostuu yli 15 oppitunnista, jotka käsittelevät perusteita, suunnittelumalleja, kehyksiä ja AI-agenttien tuotantoon vientiä.

**Keskeiset teknologiat:**
- Python 3.12+
- Jupyter-muistikirjat interaktiiviseen oppimiseen
- AI-kehykset: Microsoft Agent Framework (MAF)
- Azure AI -palvelut: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkkitehtuuri:**
- Oppituntipohjainen rakenne (00-15+ hakemistot)
- Jokainen oppitunti sisältää: README-dokumentaation, koodiesimerkkejä (Jupyter-muistikirjat) ja kuvia
- Monikielinen tuki automaattisen käännösjärjestelmän kautta
- Yksi Python-muistikirja per oppitunti käyttäen Microsoft Agent Frameworkia

## Asennuskomennot

### Esivaatimukset
- Python 3.12 tai uudempi
- Azure-tilaus (Azure AI Foundrylle)
- Azure CLI asennettuna ja kirjautuneena sisään (`az login`)

### Alustava asennus

1. **Kloonaa tai forkkaa repositorio:**
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

4. **Aseta ympäristömuuttujat:**
   ```bash
   cp .env.example .env
   # Muokkaa .env-tiedostoa lisäämällä API-avaimesi ja päätepisteesi
   ```

### Vaadittavat ympäristömuuttujat

Azure AI Foundrylle (Pakollinen):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry -projektin päätepiste
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mallin käyttöönoton nimi (esim. gpt-4o)

Azure AI Searchille (Oppitunti 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search -päätepiste
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-avain

Todennus: Suorita `az login` ennen muistikirjojen käynnistämistä (käyttää `AzureCliCredential`).

## Kehitystyönkulku

### Jupyter-muistikirjojen suorittaminen

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
- Vaatii Azure-tilauksen
- Käyttää `AzureAIProjectAgentProvider` Agent Service V2:lle (agentit näkyvät Foundryn portaalissa)
- Tuotantovalmiina sisäänrakennetulla havainnoinnilla
- Tiedostotyyppi: `*-python-agent-framework.ipynb`

## Testausohjeet

Tämä on koulutusmateriaali, joka sisältää esimerkkikoodia eikä tuotantokoodia automatisoiduilla testeillä. Varmistaaksesi asennuksen ja muutokset:

### Manuaalinen testaus

1. **Testaa Python-ympäristö:**
   ```bash
   python --version  # Pitäisi olla 3.12 tai uudempi
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testaa muistikirjojen suoritus:**
   ```bash
   # Muunna muistikirja skriptiksi ja suorita (testaa tuontia)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Tarkista ympäristömuuttujat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Yksittäisten muistikirjojen suorittaminen

Avaa muistikirjat Jupyterissa ja suorita solut järjestyksessä. Jokainen muistikirja on itsenäinen ja sisältää:
- Tuontilauseet
- Konfiguraation latauksen
- Esimerkkitoiminnot agenteista
- Odotetut tulosteet markdown-soluissa

## Koodityyli

### Pythonin konventiot

- **Python-versio**: 3.12+
- **Koodityyli**: Noudata Pythonin standardia PEP 8 -käytäntöä
- **Muistikirjat**: Käytä selkeitä markdown-soluja konseptien selittämiseen
- **Tuonnit**: Ryhmitä standardikirjasto-, kolmannen osapuolen ja paikalliset tuonnit

### Jupyter-muistikirjojen konventiot

- Sisällytä kuvailevia markdown-soluja ennen koodisoluja
- Lisää muistikirjoihin esimerkkejä tulosteista viitteeksi
- Käytä selkeitä muuttujanimikkeitä, jotka vastaavat oppitunnin käsitteitä
- Säilytä suoritusjärjestys lineaarisena (solu 1 → 2 → 3...)

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

## Rakennus ja käyttöönottaminen

### Dokumentaation rakentaminen

Tämä repositorio käyttää Markdownia dokumentaatiossa:
- README.md-tiedostot jokaisessa oppituntikansiossa
- Pääasiallinen README.md repositorion juurihakemistossa
- Automaattinen käännösjärjestelmä GitHub Actionsin kautta

### CI/CD-putki

Sijaitsee kansiossa `.github/workflows/`:

1. **co-op-translator.yml** - Automaattinen käännös yli 50 kielelle
2. **welcome-issue.yml** - Tervehtii uusia issue-luoja käyttäjiä
3. **welcome-pr.yml** - Tervehtii uusia pull request -tekijöitä

### Käyttöönottaminen

Tämä on koulutusmateriaali - ei varsinaista käyttöönottoprosessia. Käyttäjät:
1. Forkkaa tai kloonaa repositorio
2. Suorittavat muistikirjoja paikallisesti tai GitHub Codespacesissa
3. Oppivat muokkaamalla ja kokeilemalla esimerkkejä

## Pull request -ohjeet

### Ennen lähettämistä

1. **Testaa muutoksesi:**
   - Suorita vaikutukset muistikirjat kokonaan
   - Varmista, että kaikki solut suorittuvat ilman virheitä
   - Tarkista, että tulosteet ovat asianmukaisia

2. **Dokumentaation päivitys:**
   - Päivitä README.md, jos lisäät uusia käsitteitä
   - Lisää kommentteja muistikirjoihin monimutkaisten koodien kohdalla
   - Varmista, että markdown-soluissa selitetään tarkoitus

3. **Tiedostojen muuttaminen:**
   - Vältä `.env`-tiedostojen sitomista (käytä `.env.example`-tiedostoa)
   - Älä sitoudu `venv/` tai `__pycache__/` hakemistoja
   - Säilytä muistikirjojen tulosteet silloin, kun ne havainnollistavat konsepteja
   - Poista väliaikaiset tiedostot ja varmuuskopiointimuistikirjat (`*-backup.ipynb`)

### PR-otsikkomuoto

Käytä kuvailevia otsikoita:
- `[Lesson-XX] Lisää uusi esimerkki aiheesta <concept>`
- `[Fix] Korjaa kirjoitusvirhe oppitunnissa XX README`
- `[Update] Paranna koodiesimerkkiä oppitunnissa XX`
- `[Docs] Päivitä asennusohjeet`

### Vaatimukset tarkistuksille

- Muistikirjat tulee suorittaa ilman virheitä
- README-tiedostojen pitää olla selkeitä ja tarkkoja
- Noudata repositorion olemassa olevia koodimalleja
- Säilytä johdonmukaisuus muiden oppituntien kanssa

## Lisähuomiot

### Yleisiä haasteita

1. **Python-version ristiriidat:**
   - Varmista, että käytössä on Python 3.12+
   - Jotkut paketit eivät toimi vanhemmilla versioilla
   - Käytä `python3 -m venv` määrittelemään Python-versio eksplisiittisesti

2. **Ympäristömuuttujat:**
   - Luo aina `.env` tiedosto `.env.example` pohjalta
   - Älä sitoudu `.env` tiedostoa (se on .gitignore:ssa)
   - GitHub-tunnuksella tulee olla tarvittavat oikeudet

3. **Paketin yhteensopimattomuudet:**
   - Käytä uutta virtuaaliympäristöä
   - Asenna paketit `requirements.txt`:n kautta, ei yksittäisinä
   - Jotkin muistikirjat saattavat vaatia lisäpaketteja, jotka mainitaan markdown-soluissa

4. **Azure-palvelut:**
   - Azure AI -palvelut vaativat aktiivisen tilauksen
   - Jotkut ominaisuudet ovat aluekohtaisia
   - GitHub-mallit rajoittuvat ilmaiskerroksen rajoituksiin

### Oppimispolku

Suositeltu etenemisjärjestys oppituntien läpi:
1. **00-course-setup** - Aloita tästä ympäristön asetuksissa
2. **01-intro-to-ai-agents** - Ymmärrä AI-agenttien perusteet
3. **02-explore-agentic-frameworks** - Tutustu eri kehyksiin
4. **03-agentic-design-patterns** - Ydin suunnittelumallit
5. Jatka numeroitujen oppituntien mukaisesti peräkkäin

### Kehyksen valinta

Valitse kehys tavoitteidesi mukaan:
- **Kaikki oppitunnit**: Microsoft Agent Framework (MAF) yhdessä `AzureAIProjectAgentProvider`:n kanssa
- Agentit rekisteröityvät palvelinpuolella Azure AI Foundry Agent Service V2:ssa ja näkyvät Foundryn portaalissa

### Apua saat

- Liity [Microsoft Foundry Community Discordiin](https://aka.ms/ai-agents/discord)
- Tarkista oppituntien README-tiedostot erityisohjeita varten
- Katso pääasiallinen [README.md](./README.md) kurssin yleiskuvaukseen
- Tutustu [Course Setup](./00-course-setup/README.md) tarkempiin asennusohjeisiin

### Osallistuminen

Tämä on avoin koulutusprojekti. Osallistuminen tervetullutta:
- Paranna koodiesimerkkejä
- Korjaa kirjoitusvirheitä tai virheitä
- Lisää selventäviä kommentteja
- Ehdota uusia oppituntiaiheita
- Käännä muihin kieliin

Katso [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) nykyiset tarpeet.

## Projektiin liittyvä konteksti

### Monikielinen tuki

Tämä repositorio käyttää automaattista käännösjärjestelmää:
- Yli 50 kieltä tuettuna
- Käännökset kansioissa `/translations/<lang-code>/`
- GitHub Actions -työnkulku hoitaa käännöspäivitykset
- Lähdetiedostot ovat englanniksi repositorion juuressa

### Oppituntirakenne

Jokainen oppitunti noudattaa yhtenäistä kaavaa:
1. Videon pikkukuva ja linkki
2. Kirjoitettu oppituntisisältö (README.md)
3. Koodiesimerkit useissa kehyksissä
4. Oppimistavoitteet ja esivaatimukset
5. Lisäoppimateriaalit linkattuina

### Koodiesimerkkien nimeäminen

Muoto: `<oppitunti-numero>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Oppitunti 1, MAF Python
- `14-sequential.ipynb` - Oppitunti 14, MAF kehittyneet mallit

### Erityiskansiot

- `translated_images/` - Lokalisoidut kuvat käännöksiä varten
- `images/` - Alkuperäiset kuvat englanninkieliselle sisällölle
- `.devcontainer/` - VS Code -kehityssäiliön asetukset
- `.github/` - GitHub Actionsin työnkulut ja mallit

### Riippuvuudet

Tärkeimmät paketit `requirements.txt` tiedostosta:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent -protokollan tuki
- `azure-ai-inference`, `azure-ai-projects` - Azure AI -palvelut
- `azure-identity` - Azure-todennus (AzureCliCredential)
- `azure-search-documents` - Azure AI Search -integraatio
- `mcp[cli]` - Model Context Protocolin tuki

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen omalla kielellä tulee pitää ensisijaisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattitaitoista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->