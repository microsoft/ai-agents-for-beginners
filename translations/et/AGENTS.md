# AGENTS.md

## Projekti ülevaade

See hoidla sisaldab "AI Agents for Beginners" - põhjalikku õppekurssi, mis õpetab kõike, mis on vajalik AI agentide loomiseks. Kursus koosneb 15+ õppetunnist, mis käsitlevad põhialuseid, disainimustreid, raamistikke ja AI agentide tootmisse juurutamist.

**Põhitehnoloogiad:**
- Python 3.12+
- Jupyter Notebookid interaktiivseks õppimiseks
- AI raamistikud: Microsoft Agent Framework (MAF)
- Azure AI teenused: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arhitektuur:**
- Loengupõhine struktuur (00–15+ directories)
- Igas õppetunnis on: README dokumentatsioon, koodinäited (Jupyter notebookid) ja pildid
- Mitmekeelsus automatiseeritud tõlkesüsteemi kaudu
- Igas õppetunnis üks Python notebook, mis kasutab Microsoft Agent Frameworki

## Seadistamise käsud

### Eeltingimused
- Python 3.12 või uuem
- Azure tellimus (Azure AI Foundry jaoks)
- Azure CLI installitud ja autentitud (`az login`)

### Esialgne seadistus

1. **Klooni või fork’i hoidla:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # VÕI
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
   # Redigeeri .env-faili, sisestades oma API-võtmed ja lõpp-punktid.
   ```

### Nõutavad keskkonnamuutujad

For **Azure AI Foundry** (nõutav):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry projekti lõpp-punkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mudeli juurutuse nimi (nt gpt-4o)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search lõpp-punkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-võti

Autentimine: Käivita `az login` enne notebookide käivitamist (kasutab `AzureCliCredential`).

## Arenduse töövoog

### Jupyter notebookide käivitamine

Igas õppetunnis on mitu Jupyter notebooki erinevate raamistike jaoks:

1. **Käivita Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Liigu õppetunni kataloogi** (nt `01-intro-to-ai-agents/code_samples/`)

3. **Ava ja käivita notebookid:**
   - `*-python-agent-framework.ipynb` - Kasutab Microsoft Agent Frameworki (Python)
   - `*-dotnet-agent-framework.ipynb` - Kasutab Microsoft Agent Frameworki (.NET)

### Töötamine Microsoft Agent Frameworkiga

**Microsoft Agent Framework + Azure AI Foundry:**
- Nõuab Azure tellimust
- Kasutab `AzureAIProjectAgentProvider` Agent Service V2 jaoks (agendid nähtavad Foundry portaalis)
- Tootmiskõlbulik, sisseehitatud jälgitavusega
- Failimuster: `*-python-agent-framework.ipynb`

## Testimise juhised

See on õppehoidla koos näidiskoodiga, mitte tootmiskood automatiseeritud testidega. Oma seadistuse ja muudatuste kontrollimiseks:

### Käsitsi testimine

1. **Testi Python keskkonda:**
   ```bash
   python --version  # Peaks olema 3.12 või uuem
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testi notebookide täitmist:**
   ```bash
   # Muuda märkmik skriptiks ja käivita (testide impordid)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Kontrolli keskkonnamuutujaid:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Üksikute notebookide käivitamine

Ava notebookid Jupyteri keskkonnas ja täida lahtrid järjestikku. Iga notebook on iseseisev ja sisaldab:
- Impordiavaldisi
- Konfiguratsiooni laadimist
- Näidissagentide implementeeringuid
- Oodatud väljundit markdown-lahtrites

## Koodistiil

### Python konventsioonid

- **Pythoni versioon**: 3.12+
- **Koodi stiil**: Järgi standardseid Python PEP 8 konventsioone
- **Notebookid**: Kasuta selgeid markdown-lahtrid kontseptsioonide selgitamiseks
- **Impordid**: Rühmitada standardraamatukogu, kolmanda osapoole ja lokaalsed impordid

### Jupyteri notebooki konventsioonid

- Lisa kirjeldavad markdown-lahtrid enne koodilahtrid
- Lisa notebookidesse väljundinäited viitamiseks
- Kasuta selgeid muutujanimetusi, mis vastavad õppetunni kontseptsioonidele
- Hoia notebooki täitmise järjekord lineaarsena (lahter 1 → 2 → 3...)

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

See hoidla kasutab dokumentatsiooni jaoks Markdowni:
- README.md failid igas õppetunni kaustas
- Peamine README.md hoidla juures
- Automaatne tõlkesüsteem GitHub Actionsi kaudu

### CI/CD töövoog

Asub kataloogis `.github/workflows/`:

1. **co-op-translator.yml** - Automaatne tõlge 50+ keelde
2. **welcome-issue.yml** - Tervitab uusi issue loojaid
3. **welcome-pr.yml** - Tervitab uusi pull requesti kaasautoreid

### Juurutamine

See on õppehoidla - puudub juurutusprotsess. Kasutajad:
1. Forki või klooni hoidla
2. Käivita notebookid lokaalselt või GitHub Codespaces'is
3. Õpi, muutes ja katsetades näiteid

## Pull Requesti juhised

### Enne esitamist

1. **Testi oma muudatusi:**
   - Käivita mõjutatud notebookid täielikult
   - Kontrolli, et kõik lahtrid täituvad ilma vigadeta
   - Kontrolli, et väljundid on sobivad

2. **Dokumentatsiooni uuendused:**
   - Uuenda README.md, kui lisad uusi kontseptsioone
   - Lisa notebookidesse kommentaare keeruka koodi jaoks
   - Veendu, et markdown-lahtrid seletavad eesmärki

3. **Faili muudatused:**
   - Väldi `.env` failide commitimist (kasuta `.env.example`)
   - Ära commiti `venv/` ega `__pycache__/` katalooge
   - Hoia notebooki väljundeid, kui need demonstreerivad kontseptsioone
   - Eemalda ajutised failid ja varukoopia notebookid (`*-backup.ipynb`)

### PR pealkirja formaat

Kasuta kirjeldavaid pealkirju:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Nõutud kontrollid

- Notebookid peaksid täituma ilma vigadeta
- README failid peaksid olema selged ja täpsed
- Järgi olemasolevaid koodimustreid hoidlas
- Säilita järjepidevus teiste õppetundidega

## Lisamärkused

### Sageli esinevad probleemid

1. **Pythoni versiooni mittevastavus:**
   - Veendu, et kasutatakse Python 3.12+ versiooni
   - Mõned paketid ei pruugi vanemate versioonidega töötada
   - Kasuta `python3 -m venv`, et määrata Python versioon selgelt

2. **Keskkonnamuutujad:**
   - Loo alati `.env` fail `.env.example` põhjal
   - Ära commiti `.env` faili (see on `.gitignore`-is)
   - GitHubi token vajab sobivaid õigusi

3. **Pakkide konfliktid:**
   - Kasuta värsket virtuaalkeskkonda
   - Paigalda `requirements.txt` alusel, mitte üksikute pakettidena
   - Mõned notebookid võivad vajada täiendavaid pakette, mis on mainitud nende markdown-lahtrites

4. **Azure teenused:**
   - Azure AI teenused nõuavad aktiivset tellimust
   - Mõned funktsioonid on regioonispetsiifilised
   - Tasuta taseme piirangud kehtivad GitHub Models'i puhul

### Õppimise rada

Soovitatav järjekord õppetundide läbimiseks:
1. **00-course-setup** - Alusta siit keskkonna seadistamiseks
2. **01-intro-to-ai-agents** - Mõista AI agentide põhialuseid
3. **02-explore-agentic-frameworks** - Õpi erinevaid raamistikke
4. **03-agentic-design-patterns** - Põhilised disainimustrid
5. Jätka nummerdatud õppetundide järjekorras

### Raamistiku valik

Vali raamistik vastavalt oma eesmärkidele:
- **Kõik õppetunnid**: Microsoft Agent Framework (MAF) koos `AzureAIProjectAgentProvider`-ga
- **Agendid registreeritakse serveris** Azure AI Foundry Agent Service V2-s ja need on nähtavad Foundry portaalis

### Abi saamine

- Liitu [Microsoft Foundry kogukonna Discordiga](https://aka.ms/ai-agents/discord)
- Vaata õppetunni README-faile konkreetse juhendamise jaoks
- Vaata peamist [README.md](./README.md) kursuse ülevaate saamiseks
- Viita lehele [Kursuse seadistus](./00-course-setup/README.md) üksikasjalike seadistusjuhiste jaoks

### Panustamine

See on avatud õppeprojekt. Panused on teretulnud:
- Paranda koodinäiteid
- Paranda trükivead või vead
- Lisa täpsustavaid kommentaare
- Paku uusi õppetundide teemasid
- Tõlgi täiendavatesse keeltesse

See [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for current needs.

## Projekti-spetsiifiline kontekst

### Mitmekeelsuse tugi

See hoidla kasutab automatiseeritud tõlkesüsteemi:
- Toetatud 50+ keelt
- Tõlked asuvad kataloogides `/translations/<lang-code>/`
- GitHub Actionsi töövoog haldab tõlkeuuendusi
- Allikafailid on inglise keeles hoidla juures

### Õppetunni struktuur

Iga õppetund järgib järjepidevat mustrit:
1. Video pisipilt koos lingiga
2. Kirjalik õppetunni sisu (README.md)
3. Koodinäited mitmes raamistikus
4. Õpieesmärgid ja eeltingimused
5. Täiendavad õppematerjalid lingitult

### Koodinäidete nimetamine

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Õppetund 1, MAF Python
- `14-sequential.ipynb` - Õppetund 14, MAF edasijõudnud mustrid

### Spetsiaalsed kataloogid

- `translated_images/` - Lokaliseeritud pildid tõlgete jaoks
- `images/` - Originaalpildid ingliskeelse sisu jaoks
- `.devcontainer/` - VS Code arenduskonteineri konfiguratsioon
- `.github/` - GitHub Actions töövood ja mallid

### Sõltuvused

Peamised paketid failist `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-agent protokolli tugi
- `azure-ai-inference`, `azure-ai-projects` - Azure AI teenused
- `azure-identity` - Azure autentimine (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integratsioon
- `mcp[cli]` - Model Context Protocol tugi

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Lahtiütlus:
See dokument on tõlgitud tehisintellektil põhineva tõlketeenuse Co-op Translator (https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun pange tähele, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta ühegi arusaamatuse ega väärtõlgenduse eest, mis tuleneb selle tõlke kasutamisest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->