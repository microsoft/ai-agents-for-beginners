# AGENTS.md

## Projekti ülevaade

See repositoorium sisaldab "AI Agents for Beginners" - põhjalikku õppekurssi, mis õpetab kõike, mida on vaja AI-agentide ehitamiseks. Kursus koosneb 15+ õppetunnist, mis käsitlevad aluseid, disainimustreid, raamistikke ja tootmisse viimist AI-agentide jaoks.

**Olulised tehnoloogiad:**
- Python 3.12+
- Jupyter Notebookid interaktiivseks õppimiseks
- AI-raamistikud: Microsoft Agent Framework (MAF)
- Azure AI teenused: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arhitektuur:**
- Õppetundidel põhinev struktuur (00-15+ kaustad)
- Igas õppetunnis on: README dokumentatsioon, näidiskoodid (Jupyter notebookid) ja pildid
- Mitmekeelne tugi automatiseeritud tõlkesüsteemi kaudu
- Igas õppetunnis üks Python notebook, mis kasutab Microsoft Agent Frameworki

## Seadistamise käsud

### Nõuded
- Python 3.12 või uuem
- Azure tellimus (Azure AI Foundry jaoks)
- Azure CLI paigaldatud ja autentitud (`az login`)

### Esialgne seadistamine

1. **Klooni või forgi repositoorium:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # või
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Loo ja aktiveeri Python virtuaalne keskkond:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windowsis: venv\Scripts\activate
   ```

3. **Paigalda sõltuvused:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Sea keskkonnamuutujad:**
   ```bash
   cp .env.example .env
   # Redigeeri .env-faili, sisesta sinna oma API-võtmed ja lõpp-punktid
   ```

### Nõutavad keskkonnamuutujad

Azure AI Foundry jaoks (nõutud):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-4o)

Azure AI Search jaoks (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Autentimine: Enne notebookide käivitamist käivita `az login` (kasutab `AzureCliCredential`).

## Arendustöövoog

### Jupyter Notebookide käivitamine

Igas õppetunnis on mitu Jupyter notebooki erinevate raamistikute jaoks:

1. **Käivita Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Liigu õppetunni kataloogi** (nt `01-intro-to-ai-agents/code_samples/`)

3. **Ava ja käivita notebooke:**
   - `*-python-agent-framework.ipynb` - Kasutades Microsoft Agent Frameworki (Python)
   - `*-dotnet-agent-framework.ipynb` - Kasutades Microsoft Agent Frameworki (.NET)

### Töötamine Microsoft Agent Frameworkiga

**Microsoft Agent Framework + Azure AI Foundry:**
- Nõuab Azure'i tellimust
- Kasutab `AzureAIProjectAgentProvider` Agent Service V2 jaoks (agendid nähtavad Foundry portaalis)
- Tootmiskõlbulik koos sisseehitatud jälgitavusega
- Faili muster: `*-python-agent-framework.ipynb`

## Testimise juhised

See on õppeprojekt koos näidiskoodiga, mitte tootmiskood automatiseeritud testidega. Oma seadistuse ja muudatuste kinnitamiseks:

### Käsitsi testimine

1. **Testi Python keskkonda:**
   ```bash
   python --version  # Peab olema 3.12 või uuem
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testi notebooki käivitamist:**
   ```bash
   # Teisenda märkmik skriptiks ja käivita (testide impordid)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Kontrolli keskkonnamuutujaid:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Individuaalsete notebookide käivitamine

Ava notebookid Jupyteri sees ja täida lahtrid järjestikku. Iga notebook on iseseisev ja sisaldab:
- Import-lauseid
- Konfiguratsiooni laadimist
- Näidisagentide rakendusi
- Oodatud väljundeid markdown-lahtrites

## Koodi stiil

### Pythoni konventsioonid

- **Python versioon**: 3.12+
- **Koodi stiil**: Järgi tavalisi Python PEP 8 konventsioone
- **Notebookid**: Kasuta selgeid markdown-lahtreid kontseptsioonide selgitamiseks
- **Impordid**: Grupeeri standardteegi-, kolmanda osapoole- ja kohalike impordide järgi

### Jupyteri notebooki konventsioonid

- Lisa koodilahtrite ette kirjeldavad markdown-lahtrid
- Lisa näidistulemusi notebookidesse viitamiseks
- Kasuta selgeid muutujate nimesid, mis vastavad õppetunni kontseptsioonidele
- Hoolitse, et notebooki täitmise järjekord oleks lineaarne (lahter 1 → 2 → 3...)

### Failide korraldus

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Koostamine ja juurutamine

### Dokumentatsiooni koostamine

See repositoorium kasutab dokumentatsiooni jaoks Markdowni:
- README.md failid iga õppetunni kaustas
- Põhifail README.md repositooriumi juures
- Automatiseeritud tõlkesüsteem GitHub Actionsi kaudu

### CI/CD torujuhe

Asub kaustas `.github/workflows/`:

1. **co-op-translator.yml** - Automaatne tõlge 50+ keelde
2. **welcome-issue.yml** - Tervitab uusi issue loojaid
3. **welcome-pr.yml** - Tervitab uusi pull requesti panustajaid

### Juurutamine

See on õppevaramu - puudub juurutusprotsess. Kasutajad:
1. Forki või klooni repositoorium
2. Käivita notebooke lokaalselt või GitHub Codespaces'is
3. Õpi, muutes ja katsetades näiteid

## Pull Requesti juhised

### Enne esitamist

1. **Testi oma muudatusi:**
   - Käivita mõjutatud notebookid täielikult
   - Kinnita, et kõik lahtrid käivituvad ilma vigadeta
   - Kontrolli, et väljundid on sobivad

2. **Dokumentatsiooni uuendused:**
   - Uuenda README.md faili, kui lisad uusi kontseptsioone
   - Lisa notebookidesse kommentaarid keeruka koodi jaoks
   - Veendu, et markdown-lahtrid selgitavad eesmärki

3. **Failimuudatused:**
   - Väldi `.env` failide commitimist (kasuta `.env.example`)
   - Ära commiti `venv/` ega `__pycache__/` kaustu
   - Jäta notebookite väljundid alles, kui need demonstreerivad kontseptsioone
   - Eemalda ajutised failid ja varufailid (`*-backup.ipynb`)

### PR pealkirja formaat

Kasuta kirjeldavaid pealkirju:
- `[Lesson-XX] Lisa uus näide <kontseptsiooni>`
- `[Fix] Paranda trükiviga lesson-XX README-s`
- `[Update] Paranda koodinäidet lesson-XX`
- `[Docs] Uuenda seadistamise juhiseid`

### Nõutavad kontrollid

- Notebookid peaksid käivituma ilma vigadeta
- README failid peaksid olema selged ja täpsed
- Järgi olemasolevaid koodimustreid repositooriumis
- Hoia järjepidevust teiste õppetundidega

## Täiendavad märkused

### Levinumad probleemid

1. **Pythoni versiooni mittevastavus:**
   - Kinnita, et kasutatakse Python 3.12+
   - Mõned paketid ei pruugi vanemate versioonidega töötada
   - Kasuta `python3 -m venv`, et määrata Python versioon selgelt

2. **Keskkonnamuutujad:**
   - Alati loo `.env` `.env.example`-st
   - Ära commiti `.env` faili (see on `.gitignore`-is)
   - GitHubi token vajab sobivaid õigusi

3. **Pakettide konfliktid:**
   - Kasuta värsket virtuaalset keskkonda
   - Paigalda `requirements.txt`-ist, mitte üksikku paketti kaupa
   - Mõned notebookid võivad vajada täiendavaid pakette, mis on mainitud nende markdown-lahtrites

4. **Azure teenused:**
   - Azure AI teenused nõuavad aktiivset tellimust
   - Mõned funktsioonid on piirkonnapõhised
   - GitHubi mudelitele kehtivad tasuta taseme piirangud

### Õppimistee

Soovituslik edasiliikumine õppetundide kaudu:
1. **00-course-setup** - Alusta siit keskkonna seadistamiseks
2. **01-intro-to-ai-agents** - Saada aru AI-agentide alustest
3. **02-explore-agentic-frameworks** - Õpi erinevate raamistikute kohta
4. **03-agentic-design-patterns** - Põhilised disainimustrid
5. Jätka nummerdatud õppetundide kaudu järjestikku

### Raamistiku valik

Vali raamistik vastavalt oma eesmärkidele:
- **Kõik õppetunnid**: Microsoft Agent Framework (MAF) koos `AzureAIProjectAgentProvider`-ga
- **Agendid registreeritakse serveripoolselt** Azure AI Foundry Agent Service V2-s ja need on nähtavad Foundry portaalis

### Abi saamine

- Liitu [Microsoft Foundry kogukonna Discord](https://aka.ms/ai-agents/discord)
- Vaata õppetundide README-faile konkreetse juhenduse jaoks
- Vaata põhifaili [README.md](./README.md) kursuse ülevaate saamiseks
- Viita [Kursuse seadistamine](./00-course-setup/README.md) üksikasjalike seadistusjuhiste jaoks

### Panustamine

See on avatud õppeprojekt. Panused on teretulnud:
- Paranda koodinäiteid
- Paranda trükivigu või vigu
- Lisa selgitavaid kommentaare
- Paku uusi õppetundide teemasid
- Tõlgi lisakeeltesse

Vaata [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) praeguste vajaduste kohta.

## Projektispetsiifiline kontekst

### Mitmekeelne tugi

See repositoorium kasutab automatiseeritud tõlkesüsteemi:
- Toetatud 50+ keelt
- Tõlked asuvad kaustades `/translations/<lang-code>/`
- GitHub Actions töövoog haldab tõlkevärskendusi
- Allikfailid on inglise keeles repositooriumi juures

### Õppetunni struktuur

Iga õppetund järgib ühtlast mustrit:
1. Video pisipilt lingiga
2. Kirjeldatud õppetunni sisu (README.md)
3. Koodinäited mitmes raamistikus
4. Õpieesmärgid ja eeltingimused
5. Lisamaterjalid lingitult

### Koodinäidiste nimetamine

Vorming: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1. õppetund, MAF Python
- `14-sequential.ipynb` - 14. õppetund, MAF edasijõudnud mustrid

### Eraldi kaustad

- `translated_images/` - Lokaliseeritud pildid tõlgetele
- `images/` - Originaalpildid ingliskeelse sisu jaoks
- `.devcontainer/` - VS Code arendus-konteineri konfiguratsioon
- `.github/` - GitHub Actions töövood ja mallid

### Sõltuvused

Olulisemad paketid failist `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agentide vahelise protokolli tugi
- `azure-ai-inference`, `azure-ai-projects` - Azure AI teenused
- `azure-identity` - Azure autentimine (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integratsioon
- `mcp[cli]` - Model Context Protocoli tugi

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastutusest loobumine:
Seda dokumenti on tõlgitud tehisintellektil põhineva tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüame tagada tõlgete täpsust, pidage palun meeles, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Algset dokumenti selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->