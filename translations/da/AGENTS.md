# AGENTS.md

## Projektoversigt

Dette repository indeholder "AI Agenter for Begyndere" - et omfattende undervisningsforløb, der lærer alt, hvad der skal til for at bygge AI-agenter. Kurset består af 15+ lektioner, der dækker grundlæggende principper, designmønstre, frameworks og produktionsudrulning af AI-agenter.

**Nøgleteknologier:**
- Python 3.12+
- Jupyter Notebooks til interaktiv læring
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkitektur:**
- Lektion-baseret struktur (00-15+ mapper)
- Hver lektion indeholder: README dokumentation, kodeeksempler (Jupyter notebooks) og billeder
- Flere sprog understøttes via automatisk oversættelsessystem
- En Python notebook pr. lektion ved brug af Microsoft Agent Framework

## Setup-kommandoer

### Forudsætninger
- Python 3.12 eller nyere
- Azure-abonnement (til Azure AI Foundry)
- Azure CLI installeret og godkendt (`az login`)

### Initial Setup

1. **Klon eller fork repositoryet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Opret og aktiver Python virtuel miljø:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # På Windows: venv\Scripts\activate
   ```

3. **Installer afhængigheder:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Opsæt miljøvariabler:**
   ```bash
   cp .env.example .env
   # Rediger .env med dine API-nøgler og endepunkter
   ```

### Nødvendige miljøvariabler

For **Azure AI Foundry** (påkrævet):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry projekt-endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment navn (f.eks. gpt-4o)

For **Azure AI Search** (lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nøgle

Godkendelse: Kør `az login` før kørsel af notebooks (bruger `AzureCliCredential`).

## Udviklingsworkflow

### Kørsel af Jupyter Notebooks

Hver lektion indeholder flere Jupyter notebooks til forskellige frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en lektionsmappe** (f.eks. `01-intro-to-ai-agents/code_samples/`)

3. **Åbn og kør notebooks:**
   - `*-python-agent-framework.ipynb` - Brug af Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Brug af Microsoft Agent Framework (.NET)

### Arbejde med Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Kræver Azure-abonnement
- Bruger `AzureAIProjectAgentProvider` til Agent Service V2 (agenter synlige i Foundry-portalen)
- Produktionsklar med indbygget overvågning
- Filmønster: `*-python-agent-framework.ipynb`

## Testinstruktioner

Dette er et læringsrepository med eksempel kode og ikke produktionskode med automatiserede tests. For at verificere din opsætning og ændringer:

### Manuel test

1. **Test Python-miljø:**
   ```bash
   python --version  # Bør være 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook-eksekvering:**
   ```bash
   # Konverter notesbog til script og kør (tester import)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Bekræft miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Kørsel af individuelle notebooks

Åbn notebooks i Jupyter og kør celler sekventielt. Hver notebook er selvstændig og inkluderer:
- Import-sætninger
- Konfigurations-indlæsning
- Eksempel agenter implementeringer
- Forventede output i markdown-celler

## Kodekonventioner

### Python-konventioner

- **Python-version**: 3.12+
- **Kode-stil**: Følg standard Python PEP 8 konventioner
- **Notebooks**: Brug klare markdown-celler til at forklare koncepter
- **Imports**: Grupper efter standardbibliotek, tredjepart, lokale imports

### Jupyter Notebook-konventioner

- Inkluder beskrivende markdown-celler før kodeceller
- Tilføj output-eksempler i notebooks til reference
- Brug klare variabelnavne, der matcher lektionens koncepter
- Hold notebook-eksekveringsrækkefølgen lineær (celle 1 → 2 → 3 ...)

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

## Build og Udrulning

### Bygning af dokumentation

Dette repository bruger Markdown til dokumentation:
- README.md filer i hver lektionsmappe
- Hoved README.md i repository roden
- Automatiseret oversættelsessystem via GitHub Actions

### CI/CD Pipeline

Findes i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversættelse til 50+ sprog
2. **welcome-issue.yml** - Byder nye issue-oprettere velkommen
3. **welcome-pr.yml** - Byder nye pull request bidragydere velkommen

### Udrulning

Dette er et undervisningsrepository - ingen udrulningsproces. Brugere:
1. Forker eller kloner repositoryet
2. Kører notebooks lokalt eller i GitHub Codespaces
3. Lærer ved at ændre og eksperimentere med eksempler

## Retningslinjer for Pull Requests

### Før submission

1. **Test dine ændringer:**
   - Kør berørte notebooks fuldstændigt
   - Bekræft at alle celler kører uden fejl
   - Tjek at output er passende

2. **Opdatering af dokumentation:**
   - Opdater README.md hvis nye koncepter tilføjes
   - Tilføj kommentarer i notebooks for kompleks kode
   - Sikr, at markdown-celler forklarer formålet

3. **Filændringer:**
   - Undgå at committe `.env` filer (brug `.env.example`)
   - Commit ikke `venv/` eller `__pycache__/` mapper
   - Behold notebook output når det demonstrerer koncepter
   - Fjern midlertidige filer og backup notebooks (`*-backup.ipynb`)

### PR titelformat

Brug beskrivende titler:
- `[Lesson-XX] Tilføj nyt eksempel for <koncept>`
- `[Fix] Ret stavefejl i lesson-XX README`
- `[Update] Forbedr kodeeksempel i lesson-XX`
- `[Docs] Opdater setup instruktioner`

### Krævede checks

- Notebooks skal køre uden fejl
- README filer skal være klare og korrekte
- Følg eksisterende kode mønstre i repository
- Vedligehold konsekvens med andre lektioner

## Yderligere bemærkninger

### Almindelige faldgruber

1. **Python versions uoverensstemmelse:**
   - Sørg for, at Python 3.12+ anvendes
   - Nogle pakker virker ikke med ældre versioner
   - Brug `python3 -m venv` til eksplicit at vælge Python-version

2. **Miljøvariabler:**
   - Opret altid `.env` ud fra `.env.example`
   - Commit ikke `.env` fil (er i `.gitignore`)
   - GitHub token skal have passende tilladelser

3. **Pakke-konflikter:**
   - Brug et frisk virtuelt miljø
   - Installer fra `requirements.txt` fremfor enkeltpakker
   - Nogle notebooks kan kræve yderligere pakker nævnt i markdown-celler

4. **Azure services:**
   - Azure AI services kræver aktivt abonnement
   - Nogle funktioner er regionsspecifikke
   - Gratis tier begrænsninger gælder for GitHub Models

### Læringsforløb

Anbefalet rækkefølge gennem lektionerne:
1. **00-course-setup** - Start her for opsætning af miljø
2. **01-intro-to-ai-agents** - Forstå AI-agenters grundprincipper
3. **02-explore-agentic-frameworks** - Lær om forskellige frameworks
4. **03-agentic-design-patterns** - Kernedesignmønstre
5. Fortsæt sekventielt gennem nummererede lektioner

### Framework valg

Vælg framework baseret på dine mål:
- **Alle lektioner**: Microsoft Agent Framework (MAF) med `AzureAIProjectAgentProvider`
- **Agenter registreres server-side** i Azure AI Foundry Agent Service V2 og er synlige i Foundry-portalen

### Få hjælp

- Deltag i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Gennemgå lektionernes README-filer for specifikke vejledninger
- Se hoved [README.md](./README.md) for kursusoversigt
- Se [Course Setup](./00-course-setup/README.md) for detaljeret opsætning

### Bidrag

Dette er et åbent undervisningsprojekt. Bidrag er velkomne:
- Forbedre kodeeksempler
- Ret stavefejl eller fejl
- Tilføj forklarende kommentarer
- Forslå nye lektionsemner
- Oversæt til flere sprog

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for aktuelle behov.

## Projektspecifik kontekst

### Multisprog understøttelse

Dette repository bruger et automatiseret oversættelsessystem:
- 50+ sprog understøttet
- Oversættelser i `/translations/<lang-code>/` mapper
- GitHub Actions workflow håndterer oversættelsesopdateringer
- Kildefiler er på engelsk i repository roden

### Lektionsstruktur

Hver lektion følger et konsistent mønster:
1. Video-thumbnail med link
2. Skriftligt lektionsindhold (README.md)
3. Kodeeksempler i flere frameworks
4. Læringsmål og forudsætninger
5. Ekstra læringsressourcer linket

### Navngivning af kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF avancerede mønstre

### Specielle mapper

- `translated_images/` - Lokalt oversatte billeder
- `images/` - Originale billeder til engelsk indhold
- `.devcontainer/` - VS Code udviklingscontainer konfiguration
- `.github/` - GitHub Actions workflows og templates

### Afhængigheder

Nøglepakker fra `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-til-agent protokol support
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure-autentificering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integration
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->