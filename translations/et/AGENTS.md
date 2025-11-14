<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5f54aa3f419865e5d58bcfddb1d3198",
  "translation_date": "2025-10-11T10:54:27+00:00",
  "source_file": "AGENTS.md",
  "language_code": "et"
}
-->
# AGENTS.md

## Projekti Ülevaade

See repositoorium sisaldab "AI Agendid Algajatele" - põhjalikku hariduskursust, mis õpetab kõike, mida on vaja AI agentide loomiseks. Kursus koosneb enam kui 15 õppetunnist, mis hõlmavad põhialuseid, disainimustreid, raamistikke ja AI agentide tootmisse juurutamist.

**Peamised tehnoloogiad:**
- Python 3.12+
- Jupyter Notebooks interaktiivseks õppimiseks
- AI raamistikud: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI teenused: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (saadaval tasuta tasand)

**Arhitektuur:**
- Õppetundide põhine struktuur (00-15+ kataloogid)
- Iga õppetund sisaldab: README dokumentatsiooni, koodinäiteid (Jupyter Notebooks) ja pilte
- Mitmekeelne tugi automatiseeritud tõlkesüsteemi kaudu
- Mitmed raamistikuvõimalused iga õppetunni jaoks (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Seadistamise Käsklused

### Eeltingimused
- Python 3.12 või uuem
- GitHub konto (GitHub Models - tasuta tasand)
- Azure tellimus (valikuline, Azure AI teenuste jaoks)

### Esmane Seadistamine

1. **Klooni või hargne repositoorium:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Loo ja aktiveeri Python virtuaalne keskkond:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Paigalda sõltuvused:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Seadista keskkonnamuutujad:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Nõutavad Keskkonnamuutujad

**GitHub Models (Tasuta):**
- `GITHUB_TOKEN` - GitHubi isiklik juurdepääsutoken

**Azure AI Teenused** (valikuline):
- `PROJECT_ENDPOINT` - Azure AI Foundry projekti lõpp-punkt
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API võti
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI lõpp-punkti URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Vestlusmudeli juurutamise nimi
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Embedding-mudeli juurutamise nimi
- Täiendav Azure konfiguratsioon, nagu näidatud `.env.example` failis

## Arenduse Töövoog

### Jupyter Notebookide Käivitamine

Iga õppetund sisaldab mitmeid Jupyter notebooke erinevate raamistikute jaoks:

1. **Käivita Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Liigu õppetunni kataloogi** (nt `01-intro-to-ai-agents/code_samples/`)

3. **Ava ja käivita notebookid:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel raamistikuga
   - `*-autogen.ipynb` - AutoGen raamistikuga
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Azure AI Agent Service raamistikuga

### Töö Erinevate Raamistiketega

**Semantic Kernel + GitHub Models:**
- Tasuta tasand saadaval GitHubi kontoga
- Sobib õppimiseks ja katsetamiseks
- Failimuster: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Tasuta tasand saadaval GitHubi kontoga
- Mitme agendi orkestreerimise võimalused
- Failimuster: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsofti uusim raamistik
- Saadaval Pythonis ja .NET-is
- Failimuster: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Nõuab Azure tellimust
- Tootmiskõlblikud funktsioonid
- Failimuster: `*-azureaiagent.ipynb`

## Testimise Juhised

See on hariduslik repositoorium näidiskoodiga, mitte tootmiskoodiga, millel on automaatsed testid. Seadistuse ja muudatuste kontrollimiseks:

### Käsitsi Testimine

1. **Testi Python keskkonda:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Testi notebookide käivitamist:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Kontrolli keskkonnamuutujaid:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Üksikute Notebookide Käivitamine

Ava notebookid Jupyteris ja käivita lahtrid järjestikku. Iga notebook on iseseisev ja sisaldab:
- Import-lauseid
- Konfiguratsiooni laadimist
- Näidisagentide rakendusi
- Oodatud väljundeid markdown lahtrites

## Koodistiil

### Python Konventsioonid

- **Python Versioon**: 3.12+
- **Koodistiil**: Järgi standardseid Python PEP 8 konventsioone
- **Notebookid**: Kasuta selgeid markdown lahtrid kontseptsioonide selgitamiseks
- **Importid**: Rühmitatud standardraamatukogu, kolmanda osapoole ja kohalike importide järgi

### Jupyter Notebook Konventsioonid

- Lisa kirjeldavad markdown lahtrid enne koodilahtrit
- Lisa väljundnäited notebookidesse viitamiseks
- Kasuta selgeid muutujanimesid, mis vastavad õppetunni kontseptsioonidele
- Hoia notebooki käivitamise järjekord lineaarne (lahter 1 → 2 → 3...)

### Failide Organisatsioon

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

## Ehitamine ja Juurutamine

### Dokumentatsiooni Ehitamine

See repositoorium kasutab dokumentatsiooniks Markdowni:
- README.md failid igas õppetunni kaustas
- Peamine README.md repositooriumi juurtes
- Automatiseeritud tõlkesüsteem GitHub Actionsi kaudu

### CI/CD Töövoog

Asub `.github/workflows/` kataloogis:

1. **co-op-translator.yml** - Automaatne tõlge 50+ keelde
2. **welcome-issue.yml** - Tervitab uusi probleemide loojad
3. **welcome-pr.yml** - Tervitab uusi pull requesti panustajaid

### Juurutamine

See on hariduslik repositoorium - juurutamisprotsessi pole. Kasutajad:
1. Hargnevad või kloonivad repositooriumi
2. Käivitavad notebookid lokaalselt või GitHub Codespacesis
3. Õpivad, muutes ja katsetades näiteid

## Pull Request Juhised

### Enne Esitamist

1. **Testi oma muudatusi:**
   - Käivita mõjutatud notebookid täielikult
   - Kontrolli, et kõik lahtrid töötavad veatult
   - Veendu, et väljundid on sobivad

2. **Dokumentatsiooni uuendused:**
   - Uuenda README.md, kui lisad uusi kontseptsioone
   - Lisa kommentaarid notebookidesse keeruka koodi jaoks
   - Veendu, et markdown lahtrid selgitavad eesmärki

3. **Failimuudatused:**
   - Väldi `.env` failide commitimist (kasuta `.env.example`)
   - Ära commit'i `venv/` või `__pycache__/` katalooge
   - Hoia notebooki väljundid, kui need demonstreerivad kontseptsioone
   - Eemalda ajutised failid ja varukoopia notebookid (`*-backup.ipynb`)

### PR Pealkirja Formaat

Kasuta kirjeldavaid pealkirju:
- `[Lesson-XX] Lisa uus näide <kontseptsiooni> jaoks`
- `[Fix] Paranda kirjaviga õppetunnis-XX README-s`
- `[Update] Paranda koodinäide õppetunnis-XX`
- `[Docs] Uuenda seadistusjuhiseid`

### Nõutavad Kontrollid

- Notebookid peavad töötama veatult
- README failid peavad olema selged ja täpsed
- Järgi olemasolevaid koodimustreid repositooriumis
- Säilita järjepidevus teiste õppetundidega

## Täiendavad Märkused

### Levinud Probleemid

1. **Python versiooni mittevastavus:**
   - Veendu, et kasutad Python 3.12+ versiooni
   - Mõned paketid ei pruugi töötada vanemate versioonidega
   - Kasuta `python3 -m venv`, et määrata Python versioon selgelt

2. **Keskkonnamuutujad:**
   - Loo alati `.env` fail `.env.example` põhjal
   - Ära commit'i `.env` faili (see on `.gitignore` failis)
   - GitHub token vajab sobivaid õigusi

3. **Pakettide konfliktid:**
   - Kasuta värsket virtuaalset keskkonda
   - Paigalda `requirements.txt` failist, mitte individuaalseid pakette
   - Mõned notebookid võivad vajada täiendavaid pakette, mis on mainitud nende markdown lahtrites

4. **Azure teenused:**
   - Azure AI teenused nõuavad aktiivset tellimust
   - Mõned funktsioonid on piirkonnaspetsiifilised
   - Tasuta tasandi piirangud kehtivad GitHub Modelsile

### Õppimise Tee

Soovitatav õppetundide järjestus:
1. **00-course-setup** - Alusta siit keskkonna seadistamiseks
2. **01-intro-to-ai-agents** - Mõista AI agentide põhialuseid
3. **02-explore-agentic-frameworks** - Õpi erinevate raamistikute kohta
4. **03-agentic-design-patterns** - Põhilised disainimustrid
5. Jätka nummerdatud õppetundidega järjestikku

### Raamistiku Valik

Vali raamistik vastavalt oma eesmärkidele:
- **Õppimine/Prototüüpimine**: Semantic Kernel + GitHub Models (tasuta)
- **Mitme agendi süsteemid**: AutoGen
- **Uusimad funktsioonid**: Microsoft Agent Framework (MAF)
- **Tootmisse juurutamine**: Azure AI Agent Service

### Abi Saamine

- Liitu [Azure AI Foundry Community Discordiga](https://aka.ms/ai-agents/discord)
- Vaata õppetundide README faile konkreetsete juhiste jaoks
- Kontrolli peamist [README.md](./README.md) kursuse ülevaate jaoks
- Vaata [Course Setup](./00-course-setup/README.md) üksikasjalike seadistusjuhiste jaoks

### Panustamine

See on avatud haridusprojekt. Panustamine on teretulnud:
- Paranda koodinäiteid
- Paranda kirjavigu või vigu
- Lisa selgitavaid kommentaare
- Soovita uusi õppetundide teemasid
- Tõlgi täiendavatesse keeltesse

Vaata [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) praeguste vajaduste jaoks.

## Projekti-Spetsiifiline Kontekst

### Mitmekeelne Tugi

See repositoorium kasutab automatiseeritud tõlkesüsteemi:
- 50+ keelt toetatud
- Tõlked asuvad `/translations/<lang-code>/` kataloogides
- GitHub Actions töövoog haldab tõlkeuuendusi
- Algfailid on inglise keeles repositooriumi juurtes

### Õppetundide Struktuur

Iga õppetund järgib järjepidevat mustrit:
1. Video pisipilt koos lingiga
2. Kirjalik õppetunni sisu (README.md)
3. Koodinäited mitmes raamistikus
4. Õpieesmärgid ja eeltingimused
5. Täiendavad õppematerjalid lingitud

### Koodinäidete Nimeandmine

Formaat: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Õppetund 4, Semantic Kernel
- `07-autogen.ipynb` - Õppetund 7, AutoGen
- `14-python-agent-framework.ipynb` - Õppetund 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Õppetund 14, MAF .NET

### Erilised Kataloogid

- `translated_images/` - Lokaliseeritud pildid tõlgete jaoks
- `images/` - Originaalpildid ingliskeelse sisu jaoks
- `.devcontainer/` - VS Code arenduskonteineri konfiguratsioon
- `.github/` - GitHub Actions töövood ja mallid

### Sõltuvused

Peamised paketid `requirements.txt` failist:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen raamistik
- `semantic-kernel` - Semantic Kernel raamistik
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI teenused
- `azure-search-documents` - Azure AI otsingu integreerimine
- `chromadb` - Vektori andmebaas RAG näidete jaoks
- `chainlit` - Vestluse UI raamistik
- `browser_use` - Brauseri automatiseerimine agentide jaoks
- `mcp[cli]` - Mudeli konteksti protokolli tugi
- `mem0ai` - Mälu haldamine agentide jaoks

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.