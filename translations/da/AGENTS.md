# AGENTS.md

## Projektoversigt

Dette repository indeholder "AI-agenter for begyndere" - et omfattende undervisningsforløb, der lærer alt, hvad der er nødvendigt for at bygge AI-agenter. Kurset består af 18 lektioner (nummereret 00-18), der dækker grundlæggende principper, designmønstre, frameworks, produktion-udrulning, lokale/enhedsbårne agenter og sikkerhed for AI-agenter.

**Nøgleteknologier:**
- Python 3.12+
- Jupyter Notebooks til interaktiv læring
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektur:**
- Lektion-baseret struktur (00-15+ mapper)
- Hver lektion indeholder: README-dokumentation, kodeeksempler (Jupyter notebooks) og billeder
- Multisprog-understøttelse via automatiseret oversættelsessystem
- Ét Python-notebook per lektion der bruger Microsoft Agent Framework

## Opsætningskommandoer

### Forudsætninger
- Python 3.12 eller nyere
- Azure-abonnement (til Microsoft Foundry)
- Azure CLI installeret og autentificeret (`az login`)

### Initial opsætning

1. **Klon eller fork repositoryet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Opret og aktiver Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # På Windows: venv\Scripts\activate
   ```

3. **Installer afhængigheder:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Sæt miljøvariabler op:**
   ```bash
   cp .env.example .env
   # Rediger .env med dine API-nøgler og slutpunkter
   ```

### Krævede miljøvariabler

For **Microsoft Foundry** (påkrævet):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekt endepunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modeludrulningsnavn (f.eks. gpt-5-mini)

For **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endepunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API nøgle

Autentificering: Kør `az login` før du kører notebooks (benytter `AzureCliCredential`).

## Udviklingsworkflow

### Kørsel af Jupyter Notebooks

Hver lektion indeholder flere Jupyter notebooks for forskellige frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en lektionsmappe** (f.eks. `01-intro-to-ai-agents/code_samples/`)

3. **Åbn og kør notebooks:**
   - `*-python-agent-framework.ipynb` - Brug af Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Brug af Microsoft Agent Framework (.NET)

### Arbejde med Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Kræver Azure-abonnement
- Bruger `FoundryChatClient` for Agent Service V2 (agenter synlige i Foundry-portalen)
- Produktionsklar med indbygget observabilitet
- Filmønster: `*-python-agent-framework.ipynb`

## Testinstruktioner

Dette er et undervisningsrepository med eksempel-kode i stedet for produktionskode med automatiserede tests. For at verificere din opsætning og ændringer:

### Manuel test

1. **Test Python-miljøet:**
   ```bash
   python --version  # Skal være 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook-eksekvering:**
   ```bash
   # Konverter note bog til script og kør (tester imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificer miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Kørsel af individuelle notebooks

Åbn notebooks i Jupyter og udfør cellerne sekventielt. Hver notebook er selvstændig og indeholder:
- Import-sætninger
- Konfigurationsindlæsning
- Eksempel på agent-implementeringer
- Forventede output i markdown-celler

### Smoke-test af udrullede agenter

For lektioner, hvor en agent er udrullet som en Microsoft Foundry-hostet agent (01, 04, 05, 16), leverer repoet smoke-test kataloger under `tests/`, som køres af `.github/workflows/smoke-test.yml` workflowet via [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) actionen. Disse er en letvægts post-udrulnings-gate (er agenten tilgængelig og følger basale promptforventninger?), som supplerer evalueringspipelinens lektioner 10 og 16. Se [tests/README.md](./tests/README.md) for katalog-til-lektion-til-agent mapping. Lektion 17 kører lokalt med Foundry Local og har ikke noget hostet endepunkt, så den valideres ved direkte kørsel af dens notebook.

## Kodestil

### Python-konventioner

- **Python Version**: 3.12+
- **Kodestil**: Følg standard Python PEP 8 konventioner
- **Notebooks**: Brug klare markdown-celler til at forklare koncepter
- **Imports**: Grupper efter standardbibliotek, tredjepart, lokale imports

### Jupyter Notebook-konventioner

- Inkluder beskrivende markdown-celler før kodeceller
- Tilføj output-eksempler i notebooks til reference
- Brug klare variabelnavne, der matcher lektionskoncepter
- Hold notebook-eksekveringsrækkefølgen lineær (celle 1 → 2 → 3...)

### Filorganisation

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Byg og Udrul

### Byg dokumentation

Dette repository bruger Markdown til dokumentation:
- README.md filer i hver lektionsmappe
- Hoved-README.md i repositoryets rod
- Automatiseret oversættelsessystem via GitHub Actions

### CI/CD Pipeline

Placering i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversættelse til 50+ sprog
2. **welcome-issue.yml** - Velkomst til nye issue-oprettere
3. **welcome-pr.yml** - Velkomst til nye pull request-bidragsydere

### Udrulning

Dette er et undervisningsrepository - ingen udrulningsproces. Brugere:
1. Fork eller klon repositoryet
2. Kør notebooks lokalt eller i GitHub Codespaces
3. Lær ved at modificere og eksperimentere med eksempler

## Retningslinjer for Pull Requests

### Før indsendelse

1. **Test dine ændringer:**
   - Kør de berørte notebooks fuldstændigt
   - Bekræft at alle celler kører uden fejl
   - Kontrollér at output er passende

2. **Opdater dokumentation:**
   - Opdater README.md hvis nye koncepter tilføjes
   - Tilføj kommentarer i notebooks til kompleks kode
   - Sørg for, at markdown-celler forklarer formålet

3. **Filændringer:**
   - Undgå at commite `.env` filer (brug `.env.example`)
   - Commit ikke `venv/` eller `__pycache__/` mapper
   - Behold notebook-output når de viser koncepter
   - Fjern midlertidige filer og backup-notebooks (`*-backup.ipynb`)

### PR-titel format

Brug beskrivende titler:
- `[Lesson-XX] Tilføj nyt eksempel til <concept>`
- `[Fix] Rettelse af fejl i lesson-XX README`
- `[Update] Forbedr kodeeksempel i lesson-XX`
- `[Docs] Opdater opstillingsinstruktioner`

### Påkrævede checks

- Notebooks skal køre uden fejl
- README-filer skal være klare og korrekte
- Følg eksisterende kode-mønstre i repositoryet
- Oprethold konsistens med andre lektioner

## Yderligere noter

### Almindelige faldgruber

1. **Python version mismatch:**
   - Sikr brug af Python 3.12+
   - Nogle pakker virker måske ikke på ældre versioner
   - Brug `python3 -m venv` for eksplicit at specificere Python-version

2. **Miljøvariabler:**
   - Opret altid en `.env` fra `.env.example`
   - Commit ikke `.env` filen (den er i `.gitignore`)
   - Log ind med `az login` for nøglefri Entra ID-autentificering

3. **Pakke-konflikter:**
   - Brug et frisk virtual environment
   - Installer fra `requirements.txt` fremfor enkeltpakker
   - Nogle notebooks kan kræve ekstra pakker nævnt i deres markdown-celler

4. **Azure services:**
   - Azure AI services kræver aktivt abonnement
   - Nogle funktioner er regionsspecifikke
   - Sikr at din Azure OpenAI modeludrulning understøtter Responses API

### Læringsvej

Anbefalet progression gennem lektionerne:
1. **00-course-setup** - Start her for miljøopsætning
2. **01-intro-to-ai-agents** - Forståelse af AI-agenters grundlæggende
3. **02-explore-agentic-frameworks** - Lær om forskellige frameworks
4. **03-agentic-design-patterns** - Centrale designmønstre
5. Fortsæt gennem nummererede lektioner sekventielt

### Framework valg

Vælg framework baseret på dine mål:
- **Alle lektioner**: Microsoft Agent Framework (MAF) med `FoundryChatClient`
- **Agenter registreres server-side** i Microsoft Foundry Agent Service V2 og er synlige i Foundry-portalen

### Få hjælp

- Deltag i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Gennemgå lektions-README filer for specifik vejledning
- Se hoved-[README.md](./README.md) for kursusoversigt
- Henvis til [Course Setup](./00-course-setup/README.md) for detaljerede opsætningsinstruktioner

### Bidrag

Dette er et åbent undervisningsprojekt. Bidrag er velkomne:
- Forbedr kodeeksempler
- Rett fejl eller slå fejl op
- Tilføj forklarende kommentarer
- Foreslå nye lektionsemner
- Oversæt til yderligere sprog

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for nuværende behov.

## Projektspecifik kontekst

### Flersproget understøttelse

Dette repository bruger et automatiseret oversættelsessystem:
- 50+ sprog understøttet
- Oversættelser i `/translations/<lang-code>/` mapper
- GitHub Actions workflow håndterer oversættelsesopdateringer
- Kildefiler er på engelsk i repository-roden

### Lektionsstruktur

Hver lektion følger et ensartet mønster:
1. Videominiature med link
2. Skriftligt lektionsindhold (README.md)
3. Kodeeksempler i flere frameworks
4. Læringsmål og forudsætninger
5. Ekstra læringsressourcer linket

### Navngivning af kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF avancerede mønstre
- `16-python-agent-framework.ipynb` - Lektion 16, produktions kundeservice agent
- `17-local-agent-foundry-local.ipynb` - Lektion 17, lokal agent med Foundry Local + Qwen

### Specielle mapper

- `translated_images/` - Lokaliserede billeder til oversættelser
- `images/` - Originale billeder til engelsk indhold
- `.devcontainer/` - VS Code udviklingscontainer konfiguration
- `.github/` - GitHub Actions workflows og skabeloner

### Afhængigheder

Nøglepakker fra `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-til-agent protokol support
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure autentificering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integration
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->