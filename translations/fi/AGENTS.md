# AGENTS.md

## Projektin yleiskuvaus

Tämä repositorio sisältää "AI Agents for Beginners" -laajan opetuskokonaisuuden, joka opettaa kaiken tarvittavan AI-agenttien rakentamiseen. Kurssi koostuu 18 oppitunnista (numeroitu 00-18) käsittäen perusteet, suunnittelumallit, kehykset, tuotantokäyttöön viemiseksi, paikalliset/laitteella toimivat agentit sekä AI-agenttien turvallisuuden.

**Keskeiset teknologiat:**
- Python 3.12+
- Interaktiiviseen oppimiseen Jupyter Notebookit
- AI-kehykset: Microsoft Agent Framework (MAF)
- Azure AI -palvelut: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkkitehtuuri:**
- Oppituntipohjainen rakenne (00-15+ hakemistoja)
- Jokaisessa oppitunnissa README-dokumentaatio, koodiesimerkit (Jupyter Notebookit) ja kuvat
- Monikielinen tuki automaattisen käännösjärjestelmän kautta
- Yksi Python-notebook per oppitunti Microsoft Agent Frameworkilla

## Asennuskomennot

### Esivaatimukset
- Python 3.12 tai uudempi
- Azure-tilaus (Microsoft Foundryn käyttöön)
- Azure CLI asennettuna ja autentikoituna (`az login`)

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
   source venv/bin/activate  # Windowsilla: venv\Scripts\activate
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

### Vaaditut ympäristömuuttujat

Microsoft Foundrylle (pakollinen):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry -projektin päätepiste
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mallin käyttöönoton nimi (esimerkiksi gpt-5-mini)

Azure AI Searchille (Oppitunti 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search -päätepiste
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-avain

Autentikointi: Suorita `az login` ennen notebookien ajoa (käyttää `AzureCliCredential`-tunnistetta).

## Kehitystyön työnkulku

### Jupyter Notebookien ajaminen

Jokaisessa oppitunnissa on useita Jupyter-notebookeja eri kehyksille:

1. **Käynnistä Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Siirry oppitunnin kansioon** (esim. `01-intro-to-ai-agents/code_samples/`)

3. **Avaa ja suorita notebookit:**
   - `*-python-agent-framework.ipynb` - Käyttää Microsoft Agent Frameworkia (Python)
   - `*-dotnet-agent-framework.ipynb` - Käyttää Microsoft Agent Frameworkia (.NET)

### Microsoft Agent Frameworkin käyttö

**Microsoft Agent Framework + Microsoft Foundry:**
- Vaatii Azure-tilauksen
- Käyttää `FoundryChatClientia` Agent Service V2:lle (agentit näkyvät Foundry-portaalissa)
- Tuotantovalmiita sisäänrakennetulla havainnoinnilla
- Tiedostokuvio: `*-python-agent-framework.ipynb`

## Testausohjeet

Tämä on opetuksellinen repositorio esimerkkikoodilla, ei tuotantokoodi automatisoiduilla testeillä. Tarkista asennuksesi ja muutokset:

### Manuaalinen testaus

1. **Testaa Python-ympäristö:**
   ```bash
   python --version  # Pitäisi olla 3.12 tai uudempi
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testaa notebookin suoritus:**
   ```bash
   # Muunna muistikirja skriptiksi ja suorita (testaa tuonnit)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Varmista ympäristömuuttujat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Yksittäisten notebookien ajaminen

Avaa notebookit Jupyterissa ja suorita solut peräkkäin. Jokainen notebook on itsenäinen ja sisältää:
- Tuontilauseet
- Konfiguraation lataamisen
- Esimerkkien agenttien toteutukset
- Odotetut tulosteet markdown-soluissa

### Käyttöönotettujen agenttien savutestaus

Oppitunneissa, joissa agentti on käyttöönotettu Microsoft Foundryn isännöimänä agenttina (01, 04, 05, 16), repo sisältää savutestiluettelot `tests/`-kansiossa, jotka suorittaa `.github/workflows/smoke-test.yml`-työnkulku [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) -toiminnon kautta. Nämä ovat kevyitä käyttöönoton jälkeisiä porteja (onko agentti tavoitettavissa ja noudattaako se peruskehotteita?), täydentäen arviointiputkea oppitunneilla 10 ja 16. Katso [tests/README.md](./tests/README.md) luettelo-oppitunti-agentti-mappaus. Oppitunti 17 ajetaan paikallisesti Foundry Localilla eikä sillä ole isännöityä päätepistettä, joten se validoidaan ajamalla notebook suoranaisesti.

## Koodityyli

### Python-käytännöt

- **Python-versio**: 3.12+
- **Koodityyli**: Noudata standardeja Python PEP 8 -käytäntöjä
- **Notebookit**: Käytä selkeitä markdown-soluja selittämään käsitteitä
- **Tuonnit**: Ryhmittele standardikirjasto, kolmannen osapuolen ja paikallisiin tuonteihin

### Jupyter Notebook -käytännöt

- Sisällytä kuvailevia markdown-soluja koodisoluja ennen
- Lisää tulostesimerkkejä notebookeihin viitteeksi
- Käytä selkeitä muuttujien nimiä, jotka vastaavat oppitunnin käsitteitä
- Pidä notebookin suoritusjärjestys lineaarisena (solu 1 → 2 → 3...)

### Tiedostojen organisointi

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Rakentaminen ja käyttöönotto

### Dokumentaation rakentaminen

Tämä repositorio käyttää Markdownia dokumentaatioon:
- README.md-tiedostot jokaisessa oppitunnin kansiossa
- Pää-README.md repositorion juurihakemistossa
- Automaattinen käännösjärjestelmä GitHub Actionseilla

### CI/CD-putki

Sijaitsee hakemistossa `.github/workflows/`:

1. **co-op-translator.yml** - Automaattinen käännös yli 50 kielelle
2. **welcome-issue.yml** - Tervetulotoivotus uusille issueiden luojille
3. **welcome-pr.yml** - Tervetulotoivotus uusille pull requestin tekijöille

### Käyttöönotto

Tämä on opetuksellinen repositorio - ei käyttöönottoprosessia. Käyttäjät:
1. Forkkaa tai kloonaa repositorio
2. Suorita notebookit paikallisesti tai GitHub Codespacessa
3. Opiskele muokkaamalla ja kokeilemalla esimerkkejä

## Pull request -ohjeet

### Ennen lähettämistä

1. **Testaa muutoksesi:**
   - Suorita kaikki vaikuttavat notebookit kokonaan
   - Varmista, että kaikki solut suorittuvat ilman virheitä
   - Tarkista, että tulosteet ovat sopivia

2. **Dokumentaatiopäivitykset:**
   - Päivitä README.md, jos lisäät uusia käsitteitä
   - Lisää kommentteja monimutkaiseen koodiin notebookeissa
   - Varmista, että markdown-solut selittävät tarkoituksen

3. **Tiedostomuutokset:**
   - Vältä commit:a `.env`-tiedostoja (käytä `.env.example`-tiedostoa)
   - Älä commit:aa `venv/` tai `__pycache__/` -kansioita
   - Pidä notebookin tulosteet, jos ne demonstroivat käsitteitä
   - Poista väliaikaiset tiedostot ja varmuuskopiotiedostot (`*-backup.ipynb`)

### PR-otsikon muoto

Käytä kuvaavia otsikoita:
- `[Lesson-XX] Lisää uusi esimerkki <käsite>`
- `[Fix] Korjaa kirjoitusvirhe oppitunti-XX README:ssa`
- `[Update] Paranna koodiesimerkkiä oppitunti-XX:ssa`
- `[Docs] Päivitä asennusohjeet`

### Vaaditut tarkistukset

- Notebookien tulee suorittua ilman virheitä
- README-tiedostojen tulee olla selkeitä ja tarkkoja
- Noudata olemassa olevia koodimallien käytäntöjä
- Säilytä johdonmukaisuus muiden oppituntien kanssa

## Lisähuomiot

### Yleisiä sudenkuoppia

1. **Python-version yhteensopimattomuus:**
   - Varmista, että käytät Python 3.12+:aa
   - Jotkin paketit eivät toimi vanhemmilla versioilla
   - Käytä `python3 -m venv` määrittääksesi Python-version eksplisiittisesti

2. **Ympäristömuuttujat:**
   - Luo aina `.env` tiedostosta `.env.example`
   - Älä commit:aa `.env` tiedostoa (se on `.gitignore`-tiedostossa)
   - Kirjaudu sisään `az login` komennolla avaimettoman Entra ID -todennuksen käyttöä varten

3. **Pakettiristiriidat:**
   - Käytä uutta virtuaaliympäristöä
   - Asenna riippuvuudet `requirements.txt` tiedostosta yksittäisten pakettien sijaan
   - Joissain notebookeissa voidaan tarvita lisäpaketteja, jotka mainitaan niiden markdown-soluissa

4. **Azure-palvelut:**
   - Azure AI -palvelut vaativat aktiivisen tilauksen
   - Jotkin ominaisuudet ovat aluekohtaisia
   - Varmista, että Azure OpenAI -mallisi käyttöönotto tukee Responses API:ta

### Oppimispolku

Suositeltu eteneminen oppituntien läpi:
1. **00-course-setup** - Aloita tästä ympäristön pystytyksessä
2. **01-intro-to-ai-agents** - Ymmärrä AI-agenttien perusteet
3. **02-explore-agentic-frameworks** - Tutustu eri kehyksiin
4. **03-agentic-design-patterns** - Keskeiset suunnittelumallit
5. Jatka järjestelmällisesti numeroitujen oppituntien läpi

### Kehyksen valinta

Valitse kehys tavoitteidesi mukaan:
- **Kaikki oppitunnit**: Microsoft Agent Framework (MAF) `FoundryChatClient`-asiakkaalla
- **Agentit rekisteröityvät palvelinpuolelle** Microsoft Foundry Agent Service V2:ssa ja näkyvät Foundry-portaalissa

### Apua saa näistä

- Liity [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) -kanavalle
- Tarkista oppituntien README-tiedostot tarkkojen ohjeiden saamiseksi
- Katso pää-README.md:stä kurssin yleiskuvaus
- Ohjeet löytyy myös [Course Setup](./00-course-setup/README.md) -kansiosta

### Osallistuminen

Tämä on avoin opetushanke. Osallistumisia otetaan vastaan:
- Paranna koodiesimerkkejä
- Korjaa kirjoitusvirheitä tai virheitä
- Lisää selventäviä kommentteja
- Ehdota uusia oppituntiaiheita
- Käännä lisäkielille

Katso [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) nykyisistä tarpeista.

## Projektikohtainen konteksti

### Monikielituki

Tämä repositorio käyttää automaattista käännösjärjestelmää:
- Yli 50 kieltä tuettuna
- Käännökset kansioissa `/translations/<lang-code>/`
- GitHub Actions -työnkulku hoitaa käännösten päivitykset
- Lähdetiedostot ovat englanniksi repositorion juurissa

### Oppituntirakenne

Jokainen oppitunti noudattaa johdonmukaista kaavaa:
1. Videon pikkukuva ja linkki
2. Kirjoitettu oppisisältö (README.md)
3. Koodiesimerkit useissa kehyksissä
4. Oppimistavoitteet ja esivaatimukset
5. Lisäoppimateriaalit linkitettynä

### Koodiesimerkkien nimeäminen

Muoto: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Oppitunti 1, MAF Python
- `14-sequential.ipynb` - Oppitunti 14, MAF edistyneet mallit
- `16-python-agent-framework.ipynb` - Oppitunti 16, tuotantovalmiina asiakastukikäyttöagentti
- `17-local-agent-foundry-local.ipynb` - Oppitunti 17, paikallinen agentti Foundry Localilla + Qwen

### Erityiset kansiot

- `translated_images/` - Käännetyt kuvat käännöksiä varten
- `images/` - Alkuperäiset kuvat englanninkieliselle sisällölle
- `.devcontainer/` - VS Code kehityssäiliön konfiguraatio
- `.github/` - GitHub Actions -työnkulut ja mallipohjat

### Riippuvuudet

Keskeiset paketit `requirements.txt` tiedostosta:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent -protokollatuki
- `azure-ai-inference`, `azure-ai-projects` - Azure AI -palvelut
- `azure-identity` - Azure-todennus (AzureCliCredential)
- `azure-search-documents` - Azure AI Search -integraatio
- `mcp[cli]` - Model Context Protocol -tuki

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->