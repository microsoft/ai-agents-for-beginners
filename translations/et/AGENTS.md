# AGENTS.md

## Projekti ülevaade

Selles hoidlus on "Tehisintellekti agendid algajatele" – põhjalik hariduslik kursus, mis õpetab kõike, mida on vaja tehisintellekti agentide loomisel. Kursus koosneb 18 õppetunnist (numbritega 00–18), mis käsitlevad põhialuseid, disainimustreid, raamistikke, tootmisesse viimist, lokaalseid/seadmes olevaid agente ja tehisintellekti agentide turvalisust.

**Põhitehnoloogiad:**
- Python 3.12+
- Jupyter Notebooks interaktiivseks õppimiseks
- Tehisintellekti raamistikke: Microsoft Agent Framework (MAF)
- Azure AI teenused: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektuur:**
- Õppusepõhine struktuur (00-15+ kaustad)
- Igas õppetunnis on: README dokumentatsioon, koodinäited (Jupyter märkmikud) ja pildid
- Mitmekeelne tugi automaatse tõlketehnoloogiaga
- Igas õppetunnis üks Python märkmik, kasutades Microsoft Agent Frameworki

## Seadistuskäsud

### Eeltingimused
- Python 3.12 või uuem
- Azure tellimus (Microsoft Foundry jaoks)
- Azure CLI paigaldatud ja sisse logitud (`az login`)

### Algne seadistus

1. **Klooni või forgi hoidla:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # Või
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Loo ja aktiveeri Pythoni virtuaalne keskkond:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windowsis: venv\Scripts\activate
   ```

3. **Paigalda sõltuvused:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Seadista keskkonnamuutujad:**
   ```bash
   cp .env.example .env
   # Muuda .env fail oma API võtmeste ja otspunktidega
   ```

### Nõutavad keskkonnamuutujad

Microsoft Foundry jaoks (nõutav):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekti lõpp-punkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mudeli juurutamise nimi (nt gpt-4.1-mini)

Azure AI Search jaoks (õppetund 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search lõpp-punkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API võti

Autentimine: Käivita `az login` enne märkmike töötamist (kasutab `AzureCliCredential`).

## Arenduse töövoog

### Jupyter Notebooks käivitamine

Igas õppetunnis on mitu Jupyteri märkmikku erinevate raamistike jaoks:

1. **Käivita Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Mine õppetunni kausta** (nt `01-intro-to-ai-agents/code_samples/`)

3. **Ava ja käivita märkmikud:**
   - `*-python-agent-framework.ipynb` - Kasutades Microsoft Agent Frameworki (Python)
   - `*-dotnet-agent-framework.ipynb` - Kasutades Microsoft Agent Frameworki (.NET)

### Töötamine Microsoft Agent Frameworkiga

**Microsoft Agent Framework + Microsoft Foundry:**
- Nõuab Azure tellimust
- Kasutab `FoundryChatClient` Agent Service V2 jaoks (agentid nähtavad Foundry portaalis)
- Tootmiseks valmis koos sisse ehitatud jälgitavusega
- Failinime muster: `*-python-agent-framework.ipynb`

## Testimise juhised

See on hariduslik hoidla koos näidiskoodiga, mitte tootmiskood automatiseeritud testidega. Oma seadistuse ja muudatuste kontrollimiseks:

### Käsitsi testimine

1. **Testi Python keskkonda:**
   ```bash
   python --version  # Peaks olema 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testi märkmiku töötamist:**
   ```bash
   # Konverteeri märkmik skriptiks ja käivita (testib imporde)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Kontrolli keskkonnamuutujaid:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Individuaalsete märkmike kasutamine

Ava märkmikud Jupyters ja käivita lahtrid järjestikku. Iga märkmik on iseseisev ja sisaldab:
- Impordilaused
- Konfiguratsiooni laadimine
- Näidisagentide rakendused
- Oodatud väljundid markdown lahtrites

### Juurutatud agentide kiiretestimine

Õppetundides, kus agent on juurutatud Microsoft Foundry hostitud agendina (01, 04, 05, 16), sisaldab hoidla testi-katalooge `tests/` all, mida jooksutatakse `.github/workflows/smoke-test.yml` töövoo kaudu, kasutades [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) toimingut. Need on kergekaalulised juurutamisejärgsed kontrollid (kas agent on kättesaadav ja täidab põhilisi prompti ootusi?), täiustades hindamisprotsessi õppetundides 10 ja 16. Vaata [tests/README.md](./tests/README.md) faili kataloogi-õppetunni-agendi kaardistuse kohta. Õppetund 17 jookseb lokaalselt Foundry Localiga ja tal puudub hostitud lõpp-punkt, seega valideeritakse see oma märkmiku otsekäivitamisega.

## Koodi stiil

### Pythoni konventsioonid

- **Python versioon**: 3.12+
- **Koodi stiil**: Järgi tavapärast Python PEP 8 konventsiooni
- **Märkmikud**: Kasuta selgeid markdown lahtrid mõistete selgitamiseks
- **Impordid**: Rühmitage standardteegi, kolmanda osapoole ja kohalike importide kaupa

### Jupyteri märkmiku konventsioonid

- Lisa kirjeldavad markdown lahtrid enne koodilahtrit
- Lisa märkmikesse väljundi näited viitamiseks
- Kasuta selgeid muutujate nimesid, mis vastavad õppetunni mõistetele
- Hoia märkmiku täitmise järjekord lineaarsena (lahter 1 → 2 → 3...)

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

## Ehitamine ja juurutamine

### Dokumentatsiooni ehitamine

Selles hoidlus kasutatakse dokumentatsiooniks Markdownit:
- README.md failid igas õppetunni kaustas
- Peamine README.md hoidla juures
- Automaatne tõlketehnoloogia GitHub Actions kaudu

### CI/CD torujuhe

Asub `.github/workflows/` kaustas:

1. **co-op-translator.yml** - Automaatne tõlge 50+ keelde
2. **welcome-issue.yml** - Uute probleemide looja tervitamine
3. **welcome-pr.yml** - Uue pull requesti autorite tervitamine

### Juurutamine

See on hariduslik hoidla – puudub juurutamisprotsess. Kasutajad:
1. Tegema forki või kloonima hoidla
2. Jookseb märkmikke lokaalselt või GitHub Codespaces keskkonnas
3. Õppida, muutes ja katsetades näiteid

## Pull Requesti juhised

### Enne esitamist

1. **Testi oma muudatusi:**
   - Käivita mõjutatud märkmikud täielikult
   - Kontrolli, et kõik lahtrid töötavad ilma vigadeta
   - Veendu, et väljundid oleksid sobivad

2. **Dokumentatsiooni uuendused:**
   - Uuenda README.md, kui lisad uusi mõisteid
   - Lisa märkmikesse kommentaare keeruka koodi jaoks
   - Veendu, et markdown lahtrid selgitavad eesmärki

3. **Failimuudatused:**
   - Väldi `.env` failide kommitimist (kasuta `.env.example`)
   - Ära kommiti `venv/` ega `__pycache__/` kaustu
   - Hoia märkmiku väljundid, kui need demonstreerivad mõisteid
   - Eemalda ajutised failid ja varukoopiad (`*-backup.ipynb`)

### PR pealkirja vorming

Kasuta kirjeldavaid pealkirju:
- `[Lesson-XX] Lisa uus näide mõiste kohta <concept>`
- `[Fix] Paranda trükiviga õppetund-XX README-s`
- `[Update] Paranda koodinäidet õppetund-XX`
- `[Docs] Uuenda seadistusjuhiseid`

### Nõutavad kontrollid

- Märkmikud peaksid jooksma ilma vigadeta
- README failid peaksid olema selged ja õigemad
- Järgi olemasolevaid koodimustreid hoidlasse
- Hoia järjepidevust teiste õppetundidega

## Täiendavad märkused

### Levinumad lõksud

1. **Python versiooni mittevastavus:**
   - Veendu, et kasutad Python 3.12 või uuemat
   - Mõned paketid ei pruugi töötada vanemate versioonidega
   - Kasuta `python3 -m venv` Python versiooni selgeks määramiseks

2. **Keskkonnamuutujad:**
   - Loo alati `.env` fail `.env.example` põhjal
   - Ära kommiti `.env` faili (see on `.gitignore` failis)
   - Logi sisse `az login` võtmeteta Entra ID autentimiseks

3. **Pakettide konfliktid:**
   - Kasuta uut virtuaalset keskkonda
   - Paigalda `requirements.txt` abil, mitte üksikute pakettidena
   - Mõned märkmikud võivad vajada lisapakette, mis on toodud nende markdown lahtrites

4. **Azure teenused:**
   - Azure AI teenused vajavad aktiivset tellimust
   - Mõned funktsioonid on regioonipõhised
   - Veendu, et sinu Azure OpenAI mudeli juurutus toetab Responses API-t

### Õppimise rada

Soovitav õppetundide järjestus:
1. **00-course-setup** – alustuseks keskkonna seadistamiseks
2. **01-intro-to-ai-agents** – tehisintellekti agentide põhimõtete mõistmiseks
3. **02-explore-agentic-frameworks** – erinevate raamistike õppimiseks
4. **03-agentic-design-patterns** – põhidisainimustrid
5. Jätka nummerdatud õppetundidega järjestikku

### Raamistiku valik

Vali raamistik oma eesmärkide põhjal:
- **Kõik õppetunnid**: Microsoft Agent Framework (MAF) koos `FoundryChatClient`-iga
- **Agendid registreeritakse serveripoolselt** Microsoft Foundry Agent Service V2-s ja on nähtavad Foundry portalil

### Abi saamine

- Liitu [Microsoft Foundry Kogukonna Discordiga](https://aka.ms/ai-agents/discord)
- Tutvu õppetundide README failidega konkreetse juhendi saamiseks
- Vaata peamist [README.md](./README.md) kursuse ülevaateks
- Viita [Course Setup](./00-course-setup/README.md) üksikasjalike seadistusjuhiste jaoks

### Panustamine

See on avatud haridusprojekt. Panused on teretulnud:
- Koodinäidete täiustamine
- Trükivigade või vigade parandamine
- Täpsustavate kommentaaride lisamine
- Uute õppetundide teemade ettepanek
- Tõlkimine lisakeeltesse

Vaata [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) hetke vajadusi.

## Projekti spetsiifiline kontekst

### Mitmekeelne tugi

See hoidla kasutab automaatset tõlketeenust:
- Toetatud 50+ keelt
- Tõlked kaustades `/translations/<lang-code>/`
- GitHub Actions töövoog haldab tõlkeuuendusi
- Allikfailid on inglise keeles hoidla juures

### Õppetunni struktuur

Iga õppetund järgib järjepidevat mustrit:
1. Videopildi pisipilt lingiga
2. Kirjalik õppetunni sisu (README.md)
3. Koodinäited mitmes raamistikus
4. Õppeeesmärgid ja eeldused
5. Lisamaterjalid õppimiseks lingituna

### Koodinäidete nimetamine

Vorming: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Õppetund 1, MAF Python
- `14-sequential.ipynb` - Õppetund 14, MAF keerukamad mustrid
- `16-python-agent-framework.ipynb` - Õppetund 16, tootmiskasutuses klienditoe agent
- `17-local-agent-foundry-local.ipynb` - Õppetund 17, lokaalne agent koos Foundry Local ja Qwen'iga

### Erikaustad

- `translated_images/` - Lokaliseeritud pildid tõlgete jaoks
- `images/` - Originaalpildid ingliskeelsele sisule
- `.devcontainer/` - VS Code arenduskonteineri konfiguratsioon
- `.github/` - GitHub Actions töövood ja mallid

### Sõltuvused

Peamised paketid `requirements.txt` failist:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-agent protokolli tugi
- `azure-ai-inference`, `azure-ai-projects` - Azure AI teenused
- `azure-identity` - Azure autentimine (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integratsioon
- `mcp[cli]` - Model Context Protocol tugi

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->