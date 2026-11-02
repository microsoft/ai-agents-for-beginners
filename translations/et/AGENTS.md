# AGENTS.md

## Projekti Ülevaade

See hoidla sisaldab "AI Agente Algajatele" - põhjalikku haridusprogrammi, mis õpetab kõike, mida on vaja AI agentide loomiseks. Kursus koosneb 18 õppetunnist (numbritega 00-18), mis hõlmavad aluseid, disainimustreid, raamistikke, tootmiskasutusse viimist, lokaalseid/seadmesiseseid agente ja AI agentide turvalisust.

**Põhitehnoloogiad:**
- Python 3.12+
- Jupyter märkmikud interaktiivseks õppimiseks
- AI raamistikud: Microsoft Agent Framework (MAF)
- Azure AI teenused: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektuur:**
- Õppetunnipõhine struktuur (kaustad 00-18)
- Igas õppetunnis on: README dokumentatsioon, koodinäited (Jupyter märkmikud) ja pildid
- Mitmekeelne tugi automaatse tõlkesüsteemi kaudu
- Iga õppetunni kohta üks Python märkmik, kasutades Microsoft Agent Frameworki

## Seadistuskäsud

### Eeltingimused
- Python 3.12 või uuem
- Azure tellimus (Microsoft Foundry jaoks)
- Azure CLI paigaldatud ja autentitud (`az login`)

### Esmane seadistus

1. **Kloonige või hargnema hoidla:**
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

4. **Sea keskkonnamuutujad:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Nõutavad Keskkonnamuutujad

Microsoft Foundry jaoks (nõutav):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekti endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mudeli juurutuse nimi (näiteks gpt-5-mini)

Azure AI Search jaoks (Õppetund 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API võti

Autentimine: Käivita `az login` enne märkmike kasutamist (kasutab `AzureCliCredential`).

## Arendusvoog

### Jupyter märkmike käivitamine

Igas õppetunnis on mitu Jupyter märkmikku erinevate raamistikudega:

1. **Käivita Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Mine õppetunni kausta** (nt `01-intro-to-ai-agents/code_samples/`)

3. **Ava ja käivita märkmikud:**
   - `*-python-agent-framework.ipynb` - Kasutades Microsoft Agent Frameworki (Python)
   - `*-dotnet-agent-framework.ipynb` - Kasutades Microsoft Agent Frameworki (.NET)

### Töö Microsoft Agent Frameworkiga

Microsoft Agent Framework + Microsoft Foundry:
- Nõuab Azure tellimust
- Kasutab `FoundryChatClient` Agent Service V2 jaoks (agentid nähtavad Foundry portaalis)
- Tootmiseks valmis koos sisseehitatud jälgitavusega
- Failimuster: `*-python-agent-framework.ipynb`

## Testimise Juhised

See on hariduslik hoidla koos näidiskoodiga, mitte tootmiskoodi automaatsete testidega. Oma seadistuse ja muudatuste kontrollimiseks:

### Käsitsi testimine

1. **Testi Python keskkond:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testi märkmiku täitmine:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Kontrolli keskkonnamuutujaid:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Individuaalsete Märkmike Käivitamine

Ava märkmikud Jupyters ja täida lahtrid järjestikku. Iga märkmik on iseseisev ning sisaldab:
- Impordilaused
- Konfiguratsiooni laadimine
- Näidistüüpi agentide rakendused
- Oodatud väljundid markdown lahtrites

### Paigaldatud Agentide Leegi Testimine

Õppetundides, kus agent on juurutatud Microsoft Foundry majutatava agendina (01, 04, 05, 16), sisaldab hoidla leegi-testide katalooge aadressil `tests/`, mida käivitab `.github/workflows/smoke-test.yml` töövoog [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) tegevuse kaudu. Need on kerged paigaldusjärgsed väravad (kas agent on saavutatav ja järgib põhikäske?), mis täiendavad hinnangute töövoogu õppetundides 10 ja 16. Vt [tests/README.md](./tests/README.md) kataloogi-jaotus õppetundide ja agentide vahel. Õppetund 17 töötab kohapeal Foundry Localiga ja tal puudub majutatud endpoint, seega kontrollitakse seda otse märkmiku käivitamisega.

## Koodi Stiil

### Python Konventsioonid

- **Python Versioon**: 3.12+
- **Koodi Stiil**: Järgi standardseid PEP 8 Python konventsioone
- **Märkmikud**: Kasuta selgeid markdown lahtrid kontseptsioonide selgitamiseks
- **Impordid**: Rühmiti standardteekide, kolmandate osapoolte ja kohalikeks importideks

### Jupyter Märkmiku Konventsioonid

- Lisada kirjeldavad markdown lahtrid enne koodilaule
- Märkmikesse lisada väljundi näiteid viitamiseks
- Kasutada selgeid muutujate nimesid, mis vastavad õppetunni mõistetele
- Jälgida märkmiku täitmise järjekord lineaarsena (lahter 1 → 2 → 3...)

### Failide Korraldus

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Ehitus ja Juurutamine

### Dokumentatsiooni Ehitus

See hoidla kasutab dokumentatsiooniks Markdowni:
- README.md failid igas õppetunni kaustas
- Peamine README.md hoidla juures
- Automaatne tõlketeenus GitHub Actions'i kaudu

### CI/CD Töövoog

Asub aadressil `.github/workflows/`:

1. **co-op-translator.yml** - Automaatne tõlge enam kui 50 keelde
2. **welcome-issue.yml** - Tervitab uusi probleemide loojad
3. **welcome-pr.yml** - Tervitab uusi pull request'i kaasautoreid

### Juurutamine

See on hariduslik hoidla - juurutusprotsessi pole. Kasutajad:
1. Hargnevad või kloonivad hoidla
2. Käivitavad märkmikud lokaalselt või GitHub Codespaces'is
3. Õpivad, muutes ja katsetades näiteid

## Pull Request'i Juhised

### Enne Esitamist

1. **Testi oma muudatusi:**
   - Käivita kõik mõjutatud märkmikud täielikult läbi
   - Kontrolli, et kõik lahtrid täituksid veatult
   - Veendu, et väljundid oleksid sobivad

2. **Dokumentatsiooni uuendused:**
   - Uuenda README.md, kui lisad uusi mõisteid
   - Lisa märkmikesse kommentaare keeruka koodi kohta
   - Veendu, et markdown lahtrid selgitaksid eesmärki

3. **Failimuudatused:**
   - Väldi `.env` failide lisamist (kasuta `.env.example`)
   - Ära lisa `venv/` ega `__pycache__/` kaustu
   - Säilita märkmike väljundid, kui need demonstreerivad mõisteid
   - Eemalda ajutised failid ja varukoopiad (`*-backup.ipynb`)

### PR Pealkirja Vorming

Kasuta kirjeldavaid pealkirju:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Vajalikud Kontrollid

- Märkmikud peaksid käivituma ilma vigadeta
- README failid peaksid olema selged ja täpsed
- Järgi hoidla kehtivaid koodistiilipatrone
- Säilita ühtsus teiste õppetundidega

## Täiendavad Märkused

### Levinud Probleemid

1. **Python versiooni mittevastavus:**
   - Veendu, et kasutatakse Python 3.12 või uuemat
   - Mõned paketid ei pruugi vanemate versioonidega töötada
   - Kasuta `python3 -m venv`, et määrata Python versioon selgelt

2. **Keskkonnamuutujad:**
   - Alati loo `.env` fail `.env.example` abil
   - Ära lisa `.env` faili (see on `.gitignore` sees)
   - Logi sisse kasutades `az login` võtmeteta Entra ID autentimiseks

3. **Pakettide konfliktid:**
   - Kasuta uut virtuaalkeskkonda
   - Paigalda paketid koos `requirements.txt`, mitte üksikult
   - Mõned märkmikud võivad vajada täiendavaid pakette, mis on märgitud nende markdown lahtrites

4. **Azure teenused:**
   - Azure AI teenused nõuavad aktiivset tellimust
   - Mõned funktsioonid on piirkonnapõhised
   - Veendu, et sinu Azure OpenAI mudeli juurutus toetab Responses API-d

### Õppeteekond

Soovitatud järjestus õppetundide läbimiseks:
1. **00-course-setup** - Alusta sealt, et seadistada keskkond
2. **01-intro-to-ai-agents** - Mõista AI agentide aluseid
3. **02-explore-agentic-frameworks** - Õpi erinevatest raamistikest
4. **03-agentic-design-patterns** - Põhistruktuurid disainimustrites
5. Jätka numbriliste õppetundidega järjestikku

### Raamistiku Valik

Vali raamistik vastavalt oma eesmärkidele:
- **Kõik õppetunnid**: Microsoft Agent Framework (MAF) koos `FoundryChatClient`
- **Agendid registreeritakse serveripoolselt** Microsoft Foundry Agent Service V2-s ja on nähtavad Foundry portaalis

### Abi Saamine

- Liitu [Microsoft Foundry Kogukonna Discordiga](https://aka.ms/ai-agents/discord)
- Vaata õppetundide README faile spetsiifilise juhendamise jaoks
- Tutvu peamise [README.md](./README.md) kursuse ülevaatega
- Vaata [Kursuse Seadistust](./00-course-setup/README.md) detailsete juhiste jaoks

### Panustamine

See on avatud haridusprojekt. Panused on teretulnud:
- Paranda koodinäiteid
- Paranda trükivigu või vigu
- Lisa selgitavaid kommentaare
- Paku uusi õppetundi teemasid
- Tõlgi täiendavatesse keeltesse

Vaata praeguseid vajadusi aadressil [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues).

## Projekti Spetsiifiline Kontekst

### Mitmekeelne Tugi

See hoidla kasutab automaatset tõlkesüsteemi:
- Toetab üle 50 keele
- Tõlked asuvad `/translations/<lang-code>/` kaustades
- GitHub Actions töövoog haldab tõlketegevusi
- Allikfailid on inglise keeles hoidla juures

### Õppetunni Struktuur

Iga õppetund järgib ühtlast mustrit:
1. Video pisipilt koos lingiga
2. Kirjalik õppetunni sisu (README.md)
3. Koodinäited mitmes raamistikus
4. Õpieesmärgid ja eeltingimused
5. Täiendavad õppe ressursid lingitud

### Koodinäidete Nimetamine

Vorming: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Õppetund 1, MAF Python
- `14-sequential.ipynb` - Õppetund 14, MAF arenenud mustrid
- `16-python-agent-framework.ipynb` - Õppetund 16, tootmiskasutuse klienditoe agent
- `17-local-agent-foundry-local.ipynb` - Õppetund 17, kohalik agent koos Foundry Local + Qwen

### Spetsiaalsed Kaustad

- `translated_images/` - Lokaliseeritud pildid tõlgete jaoks
- `images/` - Originaalpildid ingliskeelse sisu jaoks
- `.devcontainer/` - VS Code arendus konteineri konfiguratsioon
- `.github/` - GitHub Actions töövood ja mallid

### Sõltuvused

Olulised paketid aadressilt `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agenti-agendi protokolli tugi
- `azure-ai-inference`, `azure-ai-projects` - Azure AI teenused
- `azure-identity` - Azure autentimine (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integratsioon
- `mcp[cli]` - Mudeli konteksti protokolli tugi

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->