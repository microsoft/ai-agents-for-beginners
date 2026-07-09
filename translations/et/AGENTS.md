# AGENTS.md

## Projekti ülevaade

See hoidla sisaldab "AI Agente Algajatele" - põhjalik haridusprogramm, mis õpetab kõike, mida AI Agente loomiseks vaja. Kursus koosneb 18 õppetunnist, mis hõlmavad põhiteadmisi, disainimustreid, raamistikke ja AI agentide tootmispaigutust.

**Peamised tehnoloogiad:**
- Python 3.12+
- Jupyter märkmikud interaktiivseks õppimiseks
- AI raamistikeks: Microsoft Agent Framework (MAF)
- Azure AI teenused: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektuur:**
- Õppetundidel põhinev struktuur (00-15+ kataloogid)
- Igas õppetunnis sisaldub: README dokumentatsioon, koodinäited (Jupyter märkmikud) ja pildid
- Automaatse tõlketeenusega mitmekeelne tugi
- Üks Python märkmik iga õppetunni kohta Microsoft Agent Frameworki kasutades

## Seadistuskäsud

### Eeltingimused
- Python 3.12 või uuem
- Azure tellimus (Microsoft Foundry jaoks)
- Azure CLI installitud ja autentitud (`az login`)

### Esmane seadistus

1. **Klooni või forki hoidla:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # VOI
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
   # Redigeeri .env faili koos oma API võtmete ja lõpp-punktidega
   ```

### Nõutavad keskkonnamuutujad

**Microsoft Foundry jaoks** (nõutav):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekti lõpp-punkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mudeli paigutuse nimi (nt gpt-4o)

**Azure AI Search jaoks** (Õppetund 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search lõpp-punkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API võti

Autentimine: Käivita `az login` enne märkmike käivitamist (kasutab `AzureCliCredential`).

## Arenduse töövoog

### Jupyter märkmike käivitamine

Igas õppetunnis on mitu Jupyter märkmikku erinevate raamistikute jaoks:

1. **Käivita Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Liigu õppetunni kataloogi** (nt `01-intro-to-ai-agents/code_samples/`)

3. **Ava ja järgi märkmikke:**
   - `*-python-agent-framework.ipynb` - Kasutab Microsoft Agent Frameworki (Python)
   - `*-dotnet-agent-framework.ipynb` - Kasutab Microsoft Agent Frameworki (.NET)

### Microsoft Agent Frameworkiga töötamine

**Microsoft Agent Framework + Microsoft Foundry:**
- Nõuab Azure tellimust
- Kasutab `FoundryChatClient` Agent Service V2 jaoks (agendid nähtavad Foundry portaalis)
- Tootmiskõlbulik sisseehitatud jälgitavusega
- Failimuster: `*-python-agent-framework.ipynb`

## Testimise juhised

See on hariduslik hoidla näidiskoodiga, mitte tootmiskood automatiseeritud testidega. Seadistuse ja muudatuste kontrollimiseks:

### Käsitsi testimine

1. **Testi Python keskkond:**
   ```bash
   python --version  # Peaks olema 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testi märkmiku täitmist:**
   ```bash
   # Muuda märkmik skriptiks ja käivita (testib impordid)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Kontrolli keskkonnamuutujaid:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Individuaalsete märkmike käivitamine

Ava märkmikud Jupytris ja täida lahtrid järjestikku. Iga märkmik on iseseisev ja sisaldab:
- Import käsud
- Konfiguratsiooni laadimine
- Näidistüüpi agentide rakendusi
- Oodatud väljundeid markdown lahtrites

## Koodistiil

### Python konventsioonid

- **Python versioon**: 3.12+
- **Koodistiil**: Järgi standardseid Python PEP 8 konventsioone
- **Märkmikud**: Kasuta selgeid markdown lahtrid kontseptsioonide selgitamiseks
- **Importimine**: Grupeeri standardraamatukogu, kolmanda osapoole ja kohalikke importimisi

### Jupyter märkmike konventsioonid

- Lisa kirjeldavad markdown lahtrid enne koodilahtrid
- Lisa märkmikesse väljundite näited viitamiseks
- Kasuta selgeid muutujate nimesid, mis vastavad õppetunni kontseptsioonidele
- Hoia märkmiku täitmise järjekord lineaarne (lahter 1 → 2 → 3...)

### Failide organiseerimine

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Koostamine ja paigaldamine

### Dokumentatsiooni koostamine

See hoidla kasutab dokumentatsiooni jaoks Markdowni:
- README.md failid iga õppetunni kaustas
- Peamine README.md hoidla juurest
- Automaatne tõlketeenus GitHub Actionsi kaudu

### CI/CD torujuhe

Asub kataloogis `.github/workflows/`:

1. **co-op-translator.yml** - Automaatne tõlkimine 50+ keelde
2. **welcome-issue.yml** - Uute probleemide loomise tervitamine
3. **welcome-pr.yml** - Uute pull requesti autorite tervitamine

### Paigaldamine

See on hariduslik hoidla - paigaldusprotsessi ei ole. Kasutajad:
1. Forki või klooni hoidla
2. Käivita märkmikud kohapeal või GitHub Codespaces keskkonnas
3. Õpi, muutes ja katsetades näiteid

## Pull request'i juhised

### Enne esitamist

1. **Testi oma muudatusi:**
   - Käivita täielikult mõjutatud märkmiked
   - Veendu, et kõik lahtrid täidetakse ilma vigadeta
   - Kontrolli, et väljundid on sobivad

2. **Dokumentatsiooni uuendused:**
   - Uuenda README.md kui lisad uusi kontseptsioone
   - Lisa märkmikesse kommentaare keerulise koodi kohta
   - Veendu, et markdown lahtrid selgitavad eesmärki

3. **Failimuudatused:**
   - Väldi `.env` failide commititamist (kasuta `.env.example`)
   - Ära comitti `venv/` või `__pycache__/` katalooge
   - Hoia märkmike väljundid säilitatud, kui need demonstreerivad kontseptsioone
   - Eemalda ajutised failid ja varukoopiad (`*-backup.ipynb`)

### PR pealkirja formaat

Kasuta kirjeldavaid pealkirju:
- `[Lesson-XX] Lisa uus näide teemal <kontseptsioon>`
- `[Fix] Paranda trükiviga õppetunni XX README-s`
- `[Update] Paranda koodinäidet õppetunni XX jaoks`
- `[Docs] Uuenda seadistusjuhiseid`

### Nõutavad kontrollid

- Märkmike lahtrid peaksid täituma veatult
- README failid peaksid olema selged ja täpsed
- Järgi hoidla olemasolevaid koodimustreid
- Säilita kooskõla teiste õppetundidega

## Täiendavad märkused

### Sageli esinevad probleemid

1. **Python versiooni mittevastavus:**
   - Veendu, et kasutatakse Python 3.12+ versiooni
   - Mõned paketid ei pruugi töötada vanemate versioonidega
   - Kasuta `python3 -m venv` konkreetse Python versiooni määramiseks

2. **Keskkonnamuutujad:**
   - Loo alati `.env` faili `.env.example` põhjal
   - Ära committeeri `.env` faili (see on `.gitignore` lisatud)
   - Logi sisse `az login` abil võtmepõhise Entra ID autentimiseta

3. **Pakettide konfliktid:**
   - Kasuta uut virtuaalkeskkonda
   - Paigalda `requirements.txt` failist, mitte üksikute pakettidena
   - Mõned märkmikud võivad vajada täiendavaid pakette, mis on märgitud markdown lahtrites

4. **Azure teenused:**
   - Azure AI teenused nõuavad aktiivset tellimust
   - Mõned funktsioonid on piirkonnaspetsiifilised
   - Veendu, et sinu Azure OpenAI mudeli paigutus toetab Responses API-d

### Õppimise rada

Soovitatav õppetundide järjekord:
1. **00-course-setup** - Alusta siit keskkonna seadistamiseks
2. **01-intro-to-ai-agents** - Õpi AI agentide põhialuseid
3. **02-explore-agentic-frameworks** - Tutvu erinevate raamistikega
4. **03-agentic-design-patterns** - Põhjalikud disainimustrid
5. Jätka numbrite järjekorras järgmiste õppetundidega

### Raamistiku valik

Vali raamistik oma eesmärkide järgi:
- **Kõigis õppetundides**: Microsoft Agent Framework (MAF) koos `FoundryChatClient`-iga
- **Agendid registreeruvad serveripoolselt** Microsoft Foundry Agent Service V2-s ja on nähtavad Foundry portaalis

### Abi saamine

- Liitu [Microsoft Foundry Community Discordi](https://aka.ms/ai-agents/discord)
- Vaata õppetundide README faile spetsiifiliste juhiste jaoks
- Tutvu peamise [README.md](./README.md) kursuse ülevaatega
- Vaata [Kursuse Seadistust](./00-course-setup/README.md) detailsete juhiste jaoks

### Panustamine

See on avatud haridusprojekt. Panused on oodatud:
- Paranda koodinäited
- Paranda trükivigu või vigu
- Lisa selgitavaid kommentaare
- Paku uusi õppetundide teemasid
- Tõlgi lisakeeltesse

Vaata [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) jooksvaid vajadusi.

## Projekti spetsiifiline kontekst

### Mitmekeelne tugi

See hoidla kasutab automaatset tõlketeenust:
- Toetab 50+ keelt
- Tõlked asuvad kataloogides `/translations/<lang-code>/`
- GitHub Actions töövoog haldab tõlkeuuendusi
- Allikfailid on inglise keeles hoidla juures

### Õppetunni struktuur

Iga õppetund järgib järjepidevat mustrit:
1. Videopildi pisipilt koos lingiga
2. Kirjalik õppetunni sisu (README.md)
3. Koodinäited mitmes raamistikus
4. Õpieesmärgid ja eeltingimused
5. Lisamaterjalide lingid

### Koodinäidete nimed

Vorming: `<õppetunni-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Õppetund 1, MAF Python
- `14-sequential.ipynb` - Õppetund 14, MAF keerukamad mustrid

### Erikataloogid

- `translated_images/` - Lokaliseeritud pildid tõlgete jaoks
- `images/` - Originaalpildid ingliskeelse sisu jaoks
- `.devcontainer/` - VS Code arenduse konteineri konfiguratsioon
- `.github/` - GitHub Actions töövood ja mallid

### Sõltuvused

Olulised paketid `requirements.txt` failist:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-agent protokolli tugi
- `azure-ai-inference`, `azure-ai-projects` - Azure AI teenused
- `azure-identity` - Azure autentimine (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integreerimine
- `mcp[cli]` - Model Context Protocoli tugi

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->