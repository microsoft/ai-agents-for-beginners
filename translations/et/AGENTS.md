# AGENTS.md

## Projekti ülevaade

See hoidla sisaldab "Tehisintellekti agendid algajatele" - põhjalikku õppeprogrammi, mis õpetab kõike, mida on vaja tehisintellekti agentide loomiseks. Kursus koosneb 18 õppetükist (nummerdatud 00–18), mis hõlmavad põhialuseid, disainimustreid, raamistikke, tootmispaigaldust, kohalikku/seadmesiseset agenti ja tehisintellekti agentide turvalisust.

**Peamised tehnoloogiad:**
- Python 3.12+
- Interaktiivseks õppimiseks Jupyter märkmed
- Tehisintellekti raamistikud: Microsoft Agent Framework (MAF)
- Azure'i tehisintellekti teenused: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arhitektuur:**
- Õppetükkide põhine struktuur (00-15+ kataloogid)
- Igas õppetükis on: README dokumentatsioon, koodi näited (Jupyter märkmed) ja pildid
- Mitmekeelne tugi automatiseeritud tõlketehnoloogia kaudu
- Üks Python märkme iga õppetüki kohta, kasutades Microsoft Agent Frameworki

## Paigaldus käsud

### Eeltingimused
- Python 3.12 või uuem versioon
- Azure'i tellimus (Microsoft Foundry jaoks)
- Azure CLI installitud ja autentitud (`az login`)

### Esmane seadistus

1. **Klooni või loo hoidla fork:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # VÕI
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Loo ja aktiveeri Python virtuaalkeskkond:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windowsis: venv\Scripts\activate
   ```

3. **Paigalda sõltuvused:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Määra keskkonnamuutujad:**
   ```bash
   cp .env.example .env
   # Muuda .env oma API võtmete ja lõpp-punktidega
   ```

### Nõutavad keskkonnamuutujad

**Microsoft Foundry** jaoks (nõutud):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekti lõpp-punkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Mudeli paigalduse nimi (nt gpt-5-mini)

**Azure AI Search** jaoks (õppetükk 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search lõpp-punkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API võti

Autentimine: Käivita enne märkmike käivitamist `az login` (kasutab `AzureCliCredential`).

## Arendustöövoog

### Jupyter märkmike käivitamine

Igas õppetükis on mitmeid Jupyter märkmeid erinevate raamistike jaoks:

1. **Käivita Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Liigu õppetüki kataloogi** (nt `01-intro-to-ai-agents/code_samples/`)

3. **Ava ja käivita märkmed:**
   - `*-python-agent-framework.ipynb` - Kasutades Microsoft Agent Frameworki (Python)
   - `*-dotnet-agent-framework.ipynb` - Kasutades Microsoft Agent Frameworki (.NET)

### Töötamine Microsoft Agent Frameworkiga

**Microsoft Agent Framework + Microsoft Foundry:**
- Nõuab Azure'i tellimust
- Kasutab `FoundryChatClient` Agent Service V2 jaoks (agentid nähtavad Foundry portaalis)
- Tootmisvalmis koos sisseehitatud jälgitavusega
- Failimall: `*-python-agent-framework.ipynb`

## Testimise juhised

See on õppehoidla koos näidiskoodiga, mitte tootmiskood automatiseeritud testidega. Oma seadistuse ja muudatuste kinnitamiseks:

### Käsitsi testimine

1. **Testi Python keskkond:**
   ```bash
   python --version  # Peaks olema 3.12 või uuem
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testi märkmiku täitmist:**
   ```bash
   # Muuda märkmik skriptiks ja käivita (testib importimisi)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Kontrolli keskkonnamuutujaid:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Üksikute märkmete käivitamine

Ava märkmed Jupyteris ja täida lahtrid järjestikku. Iga märkmik on iseseisev ja sisaldab:
- Impordilaused
- Konfiguratsiooni laadimine
- Näidis agentide rakendused
- Oodatavad väljundid markdown-lahtrites

### Paigaldatud agentide suitsutestimine

Õppetükkides, kus agent on paigaldatud Microsoft Foundry majutatud agendina (01, 04, 05, 16), kaasatakse hoidlas suitsutesti kataloogid kataloogis `tests/`, mida käitab `.github/workflows/smoke-test.yml` töövoog kaudu [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) tegevust. Need on kerged järelturbeväravad (kas agent on kättesaadav ja järgib põhilisi päringut ootusi), mis täiendavad hindamistoru õppetükkides 10 ja 16. Vaata [tests/README.md](./tests/README.md) kataloogi-õppetüki-agendi kaardistust. Õppetükk 17 töötab lokaalselt Foundry Localiga ja ei oma majutatud lõpp-punkti, seega valideeritakse seda tema märkmike otse jooksutamisega.

## Koodi stiil

### Pythoni soovitused

- **Python versioon**: 3.12+
- **Koodi stiil**: Järgi standardseid Python PEP 8 soovitusi
- **Märkmikud**: Kasuta selgeid markdown lahtrid kontseptsioonide selgitamiseks
- **Impordid**: Grupeeri tava-raamatukogu, kolmandate osapoolte ja kohalikud impordid eraldi

### Jupyteri märkmike soovitused

- Sisalda kirjeldavad markdown lahtrid enne koodilahtrite järel
- Lisa märkmikesse väljundite näited viitamiseks
- Kasuta selgeid muutujate nimesid, mis vastavad õppetüki kontseptsioonidele
- Hoia märkmike täitmiskord lineaarne (lahter 1 → 2 → 3...)

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

## Koostamine ja kasutuselevõtt

### Dokumentatsiooni koostamine

See hoidla kasutab dokumentatsiooniks Markdowni:
- Iga õppetüki kaustas README.md failid
- Peamine README.md hoiuala juures
- Automaatne tõlketehnoloogia GitHub Actions'i kaudu

### CI/CD torujuhe

Asub kataloogis `.github/workflows/`:

1. **co-op-translator.yml** - Automaatne tõlge üle 50 keelde
2. **welcome-issue.yml** - Uute probleemide looja tervitamine
3. **welcome-pr.yml** - Uute pull requesti panustajate tervitamine

### Kasutuselevõtt

See on õppehoidla – ei ole kasutuselevõtu protsessi. Kasutajad:
1. Loovad hoidla fork’i või kloonivad selle
2. Käivitavad märkmed kohapeal või GitHub Codespaces’is
3. Õpivad, muutes ja proovides näiteid

## Pull Requesti juhised

### Enne esitamist

1. **Testi oma muudatusi:**
   - Käivita täielikult mõjutatud märkmed
   - Kontrolli, et kõik lahtrid täidetakse ilma vigadeta
   - Veendu, et väljundid on sobivad

2. **Dokumentatsiooni uuendused:**
   - Uuenda README.md, kui lisad uusi kontseptsioone
   - Lisa märkmetesse kommentaarid keeruka koodi jaoks
   - Veendu, et markdown lahtrid selgitavad eesmärki

3. **Failimuudatused:**
   - Väldi `.env` failide commitimist (kasuta `.env.example`)
   - Ära commiti `venv/` või `__pycache__/` katalooge
   - Hoia märkmike väljundid, kui need demonstreerivad kontseptsioone
   - Eemalda ajutised failid ja varukoopiad märkmetest (`*-backup.ipynb`)

### PR pealkirja formaat

Kasuta kirjeldavaid pealkirju:
- `[Lesson-XX] Lisa uus näide teemal <kontseptsioon>`
- `[Fix] Paranda kirjaviga lesson-XX README-s`
- `[Update] Paranda koodi näidet lesson-XX`
- `[Docs] Uuenda paigaldusjuhiseid`

### Nõutavad kontrollid

- Märkmikud peavad käivituma ilma vigadeta
- README failid peavad olema selged ja täpsed
- Järgi olemasolevaid koodimustreid hoidlas
- Säilita ühtsus teiste õppetükkidega

## Täiendavad märkused

### Tavalised lõksud

1. **Python versiooni mittevastavus:**
   - Veendu, et kasutatakse Python 3.12 või uuemat
   - Mõned paketid ei pruugi töötada vanemates versioonides
   - Kasuta `python3 -m venv`, et täpsustada Python versioon eksplitsiitselt

2. **Keskkonnamuutujad:**
   - Loo alati `.env` fail `.env.example` põhjal
   - Ära commiti `.env` faili (see on `.gitignore`-s)
   - Logi sisse `az login` abil võtmepõhise Entra ID asemel

3. **Pakettide konfliktid:**
   - Kasuta värsket virtuaalkeskkonda
   - Paigalda sõltuvused `requirements.txt`-st, mitte üksikpakkidena
   - Mõned märkmed võivad vajada lisa pakette, mis on mainitud nende markdown lahtrites

4. **Azure teenused:**
   - Azure AI teenused nõuavad aktiivset tellimust
   - Mõned funktsioonid on regioonipõhised
   - Veendu, et sinu Azure OpenAI mudeli paigaldus toetab Responses API-d

### Õppimisrada

Soovitatav õppetükkide järjekord:
1. **00-course-setup** - Alusta siit keskkonna seadistamiseks
2. **01-intro-to-ai-agents** - Mõista AI agendi põhialuseid
3. **02-explore-agentic-frameworks** - Õpi erinevate raamistike kohta
4. **03-agentic-design-patterns** - Põhjalikud disainimustrid
5. Jätka järgnevate nummerdatud õppetükkidega järjest

### Raamistiku valik

Vali raamistik vastavalt oma eesmärkidele:
- **Kõik õppetükid**: Microsoft Agent Framework (MAF) koos `FoundryChatClient`-iga
- **Agentid registreeritakse serveripoolsel Microsoft Foundry Agent Service V2-s ning on nähtavad Foundry portaalis**

### Abi saamine

- Liitu [Microsoft Foundry kogukonna Discordiga](https://aka.ms/ai-agents/discord)
- Tutvu õppetükkide README failidega spetsiifilise juhendamise jaoks
- Vaata peamist [README.md](./README.md) kursuse ülevaate saamiseks
- Tutvu [Course Setup](./00-course-setup/README.md) üksikasjalike seadistusjuhistega

### Panustamine

See on avatud haridusprojekt. Panustused on teretulnud:
- Paranda koodi näiteid
- Paranda kirjavead või vead
- Lisa täpsustavaid kommentaare
- Paku uusi õppetükkide teemasid
- Tõlgi täiendavatesse keeltesse

Vaata [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) praeguste vajaduste kohta.

## Projekti spetsiifiline kontekst

### Mitmekeelne tugi

See hoidla kasutab automatiseeritud tõlketehnoloogiat:
- Toetab üle 50 keele
- Tõlked asuvad kaustades `/translations/<lang-code>/`
- GitHub Actions töövoog haldab tõlketeisendusi
- Allika failid on inglise keeles hoidla juures

### Õppetükkide struktuur

Iga õppetükk järgib järjekindlat mustrit:
1. Video pisipilt koos lingiga
2. Kirjalik õppetüki sisu (README.md)
3. Koodi näited mitmes raamistikus
4. Õpieesmärgid ja eeltingimused
5. Lisamaterjalide lingid

### Koodi näidiste nimed

Formaat: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Õppetükk 1, MAF Python
- `14-sequential.ipynb` - Õppetükk 14, MAF keerulisemad mustrid
- `16-python-agent-framework.ipynb` - Õppetükk 16, tootmisvalmis klienditoe agent
- `17-local-agent-foundry-local.ipynb` - Õppetükk 17, kohalik agent kasutades Foundry Local + Qwen

### Erikataloogid

- `translated_images/` - Lokaliseeritud pildid tõlgete jaoks
- `images/` - Originaalpildid ingliskeelse sisu jaoks
- `.devcontainer/` - VS Code arenduskonteineri konfiguratsioon
- `.github/` - GitHub Actions töövood ja mallid

### Sõltuvused

Peamised paketid `requirements.txt`-s:
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