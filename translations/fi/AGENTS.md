# AGENTS.md

## Projektin yleiskatsaus

Tämä arkisto sisältää "AI Agents for Beginners" -laajan koulutuskursin, joka opettaa kaiken tarvittavan tekoälyagenttien rakentamiseen. Kurssi koostuu 18 oppitunnista, jotka kattavat perusteet, suunnittelumallit, kehykset ja tekoälyagenttien tuotantokäyttöönottamisen.

**Keskeiset teknologiat:**
- Python 3.12+
- Jupyter-muistikirjat interaktiiviseen oppimiseen
- AI-kehykset: Microsoft Agent Framework (MAF)
- Azure AI -palvelut: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkkitehtuuri:**
- Oppituntiperusteinen rakenne (00-15+ hakemistoa)
- Jokaisessa oppitunnissa on: README-dokumentaatio, koodiesimerkit (Jupyter-muistikirjat) ja kuvat
- Monikielinen tuki automaattisen käännösjärjestelmän kautta
- Yksi Python-muistikirja per oppitunti, käyttäen Microsoft Agent Frameworkia

## Asetuskomennot

### Edellytykset
- Python 3.12 tai uudempi
- Azure-tilaus (Microsoft Foundrytä varten)
- Azure CLI asennettuna ja todennettuna (`az login`)

### Alustava asetus

1. **Kloonaa tai tee fork arkistosta:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # TAI
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Luo ja aktivoi Python-virtuaaliympäristö:**
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
   # Muokkaa .env tiedostoa API-avaimillasi ja päätepisteilläsi
   ```

### Vaaditut ympäristömuuttujat

Microsoft Foundrylle (Pakollinen):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry -projektin päätepiste
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mallin käyttöönoton nimi (esim. gpt-4o)

Azure AI Searchille (Oppitunti 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search -päätepiste
- `AZURE_SEARCH_API_KEY` - Azure AI Search -avaimen API-avain

Todennus: Suorita `az login` ennen muistikirjojen käynnistämistä (käyttää `AzureCliCredential`).

## Kehitystyön työnkulku

### Jupyter-muistikirjojen suorittaminen

Jokaisessa oppitunnissa on useita Jupyter-muistikirjoja eri kehyksille:

1. **Käynnistä Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Siirry oppitunnin hakemistoon** (esim. `01-intro-to-ai-agents/code_samples/`)

3. **Avaa ja suorita muistikirjat:**
   - `*-python-agent-framework.ipynb` - Käyttäen Microsoft Agent Frameworkia (Python)
   - `*-dotnet-agent-framework.ipynb` - Käyttäen Microsoft Agent Frameworkia (.NET)

### Työskentely Microsoft Agent Frameworkin kanssa

**Microsoft Agent Framework + Microsoft Foundry:**
- Vaatii Azure-tilauksen
- Käyttää `FoundryChatClient` Agent Service V2:lle (agentit näkyvät Foundry-portaalissa)
- Tuotantovalmiina sisäänrakennetulla havaittavuudella
- Tiedostokuvio: `*-python-agent-framework.ipynb`

## Testausohjeet

Tämä on koulutusarkisto esimerkkikoodilla, ei tuotantokoodilla automaattisilla testeillä. Tarkista asennus ja muutokset seuraavasti:

### Manuaalinen testaus

1. **Testaa Python-ympäristö:**
   ```bash
   python --version  # Pitäisi olla 3.12 tai uudempi
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testaa muistikirjan suoritus:**
   ```bash
   # Muunna muistikirja skriptiksi ja suorita (testaa tuonnit)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Varmista ympäristömuuttujat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Yksittäisten muistikirjojen suoritus

Avaa muistikirjat Jupyterissä ja suorita solut peräkkäin. Jokainen muistikirja on itsenäinen ja sisältää:
- Tuontilausekkeet
- Konfiguraation lataamisen
- Esimerkkiajagenttien toteutukset
- Odotetut tulosteet markdown-soluissa

## Koodityyli

### Python-käytännöt

- **Python-versio**: 3.12+
- **Koodityyli**: Noudata vakiintuneita Python PEP 8 -käytäntöjä
- **Muistikirjat**: Käytä selkeitä markdown-soluja käsitteiden selittämiseen
- **Tuonnit**: Ryhmittele standardikirjasto, kolmannen osapuolen ja paikalliset tuonnit

### Jupyter-muistikirjan käytännöt

- Sisällytä selittäviä markdown-soluja ennen koodisoluja
- Lisää esimerkkejä tulosteista muistikirjoihin viitteeksi
- Käytä selkeitä muuttujien nimiä, jotka vastaavat oppitunnin käsitteitä
- Säilytä lineaarinen suoritusjärjestys (solu 1 → 2 → 3...)

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

### Dokumentaation luominen

Tämä arkisto käyttää Markdownia dokumentaatiossa:
- README.md-tiedostot jokaisen oppitunnin kansiossa
- Pääasiallinen README.md arkiston juuritasolla
- Automaattinen käännösjärjestelmä GitHub Actionsin kautta

### CI/CD-putki

Sijaitsee kansiossa `.github/workflows/`:

1. **co-op-translator.yml** - Automaattinen käännös 50+ kielelle
2. **welcome-issue.yml** - Tervetuloa uusille issueiden tekijöille
3. **welcome-pr.yml** - Tervetuloa uusille pull request -tekijöille

### Käyttöönotto

Tämä on koulutusarkisto - ei käyttöönotto-prosessia. Käyttäjät:
1. Forkkaa tai kloonaa arkisto
2. Suorita muistikirjat paikallisesti tai GitHub Codespaces -ympäristössä
3. Opi muokkaamalla ja kokeilemalla esimerkkejä

## Pull Request -ohjeet

### Ennen lähettämistä

1. **Testaa muutoksesi:**
   - Suorita kaikki vaikuttavat muistikirjat kokonaan
   - Varmista, että kaikki solut suoritetaan ilman virheitä
   - Tarkista, että tulosteet ovat asianmukaisia

2. **Dokumentaatiopäivitykset:**
   - Päivitä README.md, jos lisäät uusia käsitteitä
   - Lisää kommentteja muistikirjoihin monimutkaisesta koodista
   - Varmista, että markdown-soluissa selitetään tarkoitus

3. **Tiedostomuutokset:**
   - Vältä `.env`-tiedostojen sitouttamista (käytä `.env.example`-tiedostoa)
   - Älä sitouta `venv/` tai `__pycache__/` hakemistoja
   - Säilytä muistikirjojen tulosteet, kun ne havainnollistavat käsitteitä
   - Poista väliaikaiset tiedostot ja varmuuskopioidut muistikirjat (`*-backup.ipynb`)

### PR-otsikon muoto

Käytä kuvaavia otsikoita:
- `[Lesson-XX] Lisää uusi esimerkki käsitteelle <concept>`
- `[Fix] Korjaa kirjoitusvirhe oppitunnin XX README:ssä`
- `[Update] Paranna koodiesimerkkiä oppitunnissa XX`
- `[Docs] Päivitä asetusohjeet`

### Vaaditut tarkistukset

- Muistikirjojen tulisi suorittua ilman virheitä
- README-tiedostojen tulisi olla selkeitä ja tarkkoja
- Noudata arkiston olemassa olevia koodimalleja
- Säilytä johdonmukaisuus muiden oppituntien kanssa

## Lisähuomiot

### Yleiset sudenkuopat

1. **Python-version epäsuhta:**
   - Varmista, että käytössä on Python 3.12+
   - Jotkut paketit eivät toimi vanhemmilla versioilla
   - Käytä `python3 -m venv` määrittääksesi Python-version selkeästi

2. **Ympäristömuuttujat:**
   - Luo aina `.env` tiedosto `.env.example` pohjalta
   - Älä sitouta `.env`-tiedostoa (se on `.gitignore`-tiedostossa)
   - Kirjaudu sisään `az login` avulla avaimettomaan Entra ID -todennukseen

3. **Paketin ristiriidat:**
   - Käytä uutta virtuaaliympäristöä
   - Asenna `requirements.txt` pohjalta yksittäisten pakettien sijaan
   - Jotkin muistikirjat voivat vaatia lisäpaketteja, jotka mainitaan niiden markdown-soluissa

4. **Azure-palvelut:**
   - Azure AI -palvelut vaativat aktiivisen tilauksen
   - Jotkin ominaisuudet ovat aluekohtaisia
   - Varmista, että Azure OpenAI -mallisi käyttöönotto tukee Responses APIa

### Oppimispolku

Suositeltava eteneminen oppitunneissa:
1. **00-course-setup** - Aloita tästä ympäristön asettamiseksi
2. **01-intro-to-ai-agents** - Ymmärrä tekoälyagenttien perusteet
3. **02-explore-agentic-frameworks** - Tutustu eri kehyksiin
4. **03-agentic-design-patterns** - Keskeiset suunnittelumallit
5. Jatka numeroiduissa oppitunneissa peräkkäin

### Kehyksen valinta

Valitse kehys tavoitteidesi mukaan:
- **Kaikki oppitunnit**: Microsoft Agent Framework (MAF) käyttäen `FoundryChatClient`
- **Agentit rekisteröityvät palvelinpuolella** Microsoft Foundry Agent Service V2:ssa ja näkyvät Foundry-portaalissa

### Apua saaminen

- Liity [Microsoft Foundry Community Discordiin](https://aka.ms/ai-agents/discord)
- Tarkista oppituntien README-tiedostot saadaksesi erityisohjeita
- Katso pääasiallinen [README.md](./README.md) kurssin yleiskuvaukseen
- Katso [Course Setup](./00-course-setup/README.md) yksityiskohtaisiin asetusohjeisiin

### Osallistuminen

Tämä on avoin koulutusprojekti. Panokset ovat tervetulleita:
- Paranna koodiesimerkkejä
- Korjaa kirjoitusvirheitä tai virheitä
- Lisää selventäviä kommentteja
- Ehdota uusia oppitunteja
- Käännä lisäkielille

Katso [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) nykyisiä tarpeita varten.

## Projektikohtainen konteksti

### Monikielinen tuki

Tämä arkisto käyttää automaattista käännösjärjestelmää:
- Yli 50 kieltä tuettu
- Käännökset sijaitsevat hakemistoissa `/translations/<lang-code>/`
- GitHub Actions -työnkulku hoitaa käännösten päivitykset
- Lähdetiedostot ovat englanniksi arkiston juuressa

### Oppirakenne

Jokainen oppitunti noudattaa johdonmukaista rakennetta:
1. Videon pikkukuva linkillä
2. Kirjoitettu oppimateriaali (README.md)
3. Koodiesimerkit useissa kehyksissä
4. Oppimistavoitteet ja edellytykset
5. Lisäoppimateriaalien linkitykset

### Koodiesimerkkien nimeäminen

Muoto: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Oppitunti 1, MAF Python
- `14-sequential.ipynb` - Oppitunti 14, MAF edistyneet mallit

### Erityishakemistot

- `translated_images/` - Käännetyt kuvat käännöksiä varten
- `images/` - Alkuperäiset kuvat englanninkieliselle sisällölle
- `.devcontainer/` - VS Code kehityssäiliön määritykset
- `.github/` - GitHub Actions -työnkulut ja mallit

### Riippuvuudet

Keskeiset paketit `requirements.txt` -tiedostosta:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokollatuki
- `azure-ai-inference`, `azure-ai-projects` - Azure AI -palvelut
- `azure-identity` - Azure-todennus (AzureCliCredential)
- `azure-search-documents` - Azure AI Search -integraatio
- `mcp[cli]` - Model Context Protocolin tuki

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->