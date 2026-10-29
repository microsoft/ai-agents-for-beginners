# AGENTS.md

## Projektoversigt

Dette repository indeholder "AI Agenter for Begyndere" - et omfattende uddannelsesforløb, der lærer alt nødvendigt for at bygge AI Agenter. Kurset består af 18 lektioner (nummereret 00-18), der dækker grundlæggende principper, designmønstre, frameworks, produktionsudrulning, lokale/på-enhed agenter og sikkerhed for AI agenter.

**Nøgle teknologier:**
- Python 3.12+
- Jupyter Notebooks til interaktiv læring
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektur:**
- Lektion-baseret struktur (00-18 mapper)
- Hver lektion indeholder: README dokumentation, kodeeksempler (Jupyter notebooks) og billeder
- Multisprog support via automatisk oversættelsessystem
- Ét Python notebook pr. lektion med Microsoft Agent Framework

## Setup kommandoer

### Forudsætninger
- Python 3.12 eller nyere
- Azure abonnement (til Microsoft Foundry)
- Azure CLI installeret og autentificeret (`az login`)

### Initial opsætning

1. **Klon eller fork repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Opret og aktivér Python virtuelt miljø:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Installer afhængigheder:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Opsæt miljøvariabler:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Påkrævede miljøvariabler

For **Microsoft Foundry** (påkrævet):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projektendepunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modeludrulningsnavn (f.eks. gpt-5-mini)

For **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endepunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API nøgle

Autentificering: Kør `az login` før du kører notebooks (bruger `AzureCliCredential`).

## Udviklingsarbejdsgang

### Kørsel af Jupyter Notebooks

Hver lektion indeholder flere Jupyter notebooks til forskellige frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Skift til en lektionmappe** (f.eks. `01-intro-to-ai-agents/code_samples/`)

3. **Åbn og kør notebooks:**
   - `*-python-agent-framework.ipynb` - Brug Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Brug Microsoft Agent Framework (.NET)

### Arbejde med Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Kræver Azure abonnement
- Bruger `FoundryChatClient` til Agent Service V2 (agenter synlige i Foundry portalen)
- Produktionsklar med indbygget overvågning
- Filnavnmønster: `*-python-agent-framework.ipynb`

## Testvejledning

Dette er et uddannelsesrepository med eksempel kode i stedet for produktionskode med automatiske tests. For at verificere din opsætning og ændringer:

### Manuel test

1. **Test Python miljø:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook kørsel:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificer miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Kør individuelle notebooks

Åbn notebooks i Jupyter og udfør celler sekventielt. Hver notebook er selvstændig og indeholder:
- Import-sætninger
- Konfigurationsindlæsning
- Eksempelagent-implementeringer
- Forventede output i markdown-celler

### Røgtest af udrullede agenter

For lektioner hvor en agent er udrullet som en Microsoft Foundry hostet agent (01, 04, 05, 16), leverer repoet røgtest-kataloger under `tests/`, som køres af `.github/workflows/smoke-test.yml` workflowet via [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) action. Dette er en letvægts post-udrulningsport (er agenten tilgængelig og følger basale promptforventninger?), som supplerer evalueringspipelinjen i Lektion 10 og 16. Se [tests/README.md](./tests/README.md) for kortlægning af katalog-til-lektion-til-agent. Lektion 17 kører lokalt med Foundry Local og har ikke et hostet endepunkt, så den valideres ved direkte at køre sin notebook.

## Kodestil

### Python konventioner

- **Python version**: 3.12+
- **Kodestil**: Følg standard Python PEP 8 konventioner
- **Notebooks**: Brug klare markdown-celler til at forklare koncepter
- **Imports**: Gruppér efter standardbibliotek, tredjepart, lokale imports

### Jupyter Notebook konventioner

- Inkluder beskrivende markdown-celler før kodeceller
- Tilføj output-eksempler i notebooks til reference
- Brug klare variabelnavne, der matcher lektionens koncepter
- Hold notebook kørselsrækkefølge lineær (celle 1 → 2 → 3...)

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

## Byg og Udrulning

### Opbygning af dokumentation

Dette repository bruger Markdown til dokumentation:
- README.md filer i hver lektionmappe
- Hoved README.md i repository rod
- Automatisk oversættelsessystem via GitHub Actions

### CI/CD pipeline

Findes i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversættelse til 50+ sprog
2. **welcome-issue.yml** - Byder nye issues skabere velkommen
3. **welcome-pr.yml** - Byder nye pull request bidragydere velkommen

### Udrulning

Dette er et uddannelsesrepository - ingen udrulningsproces. Brugere:
1. Forgrener eller kloner repository
2. Kører notebooks lokalt eller i GitHub Codespaces
3. Lærer ved at modificere og eksperimentere med eksempler

## Retningslinjer for Pull Requests

### Før indsendelse

1. **Test dine ændringer:**
   - Kør berørte notebooks fuldstændigt
   - Verificer at alle celler kan køres uden fejl
   - Tjek at output er passende

2. **Opdater dokumentation:**
   - Opdater README.md hvis nye koncepter tilføjes
   - Tilføj kommentarer i notebooks for kompleks kode
   - Sørg for markdown-celler forklarer formålet

3. **Filændringer:**
   - Undgå at committe `.env` filer (brug `.env.example`)
   - Commit ikke `venv/` eller `__pycache__/` mapper
   - Behold notebook outputs, når de demonstrerer koncepter
   - Fjern midlertidige filer og backup notebooks (`*-backup.ipynb`)

### PR titel format

Brug beskrivende titler:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Påkrævede tjek

- Notebooks skal køre uden fejl
- README filer skal være klare og korrekte
- Følg eksisterende kode mønstre i repository
- Oprethold konsistens med andre lektioner

## Yderligere noter

### Almindelige faldgruber

1. **Python versions mismatch:**
   - Sørg for at bruge Python 3.12+
   - Nogle pakker fungerer måske ikke med ældre versioner
   - Brug `python3 -m venv` til eksplicit at angive Python version

2. **Miljøvariabler:**
   - Opret altid `.env` fra `.env.example`
   - Commit ikke `.env` fil (den er i `.gitignore`)
   - Log ind med `az login` for nøglefri Entra ID autentificering

3. **Pakke-konflikter:**
   - Brug et frisk virtuelt miljø
   - Installer fra `requirements.txt` fremfor individuelle pakker
   - Nogle notebooks kan kræve ekstra pakker nævnt i deres markdown-celler

4. **Azure tjenester:**
   - Azure AI services kræver aktivt abonnement
   - Nogle funktioner er regionsspecifikke
   - Sørg for, at din Azure OpenAI modeludrulning understøtter Responses API

### Læringssti

Anbefalet rækkefølge gennem lektionerne:
1. **00-course-setup** - Start her for miljøopsætning
2. **01-intro-to-ai-agents** - Forstå AI agent grundprincipper
3. **02-explore-agentic-frameworks** - Lær om forskellige frameworks
4. **03-agentic-design-patterns** - Kerne designmønstre
5. Fortsæt sekventielt gennem nummererede lektioner

### Framework valg

Vælg framework baseret på dine mål:
- **Alle lektioner**: Microsoft Agent Framework (MAF) med `FoundryChatClient`
- **Agenter registreres server-side** i Microsoft Foundry Agent Service V2 og er synlige i Foundry portalen

### Få hjælp

- Deltag i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Gennemgå lektionernes README filer for specifik vejledning
- Tjek hoved-[README.md](./README.md) for kursusoversigt
- Se [Course Setup](./00-course-setup/README.md) for detaljerede opsætningsinstruktioner

### Bidrag

Dette er et åbent uddannelsesprojekt. Bidrag velkomne:
- Forbedr kodeeksempler
- Ret stavefejl eller fejl
- Tilføj forklarende kommentarer
- Forslå nye lektionsemner
- Oversæt til flere sprog

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for aktuelle behov.

## Projekt-specifik kontekst

### Multisprog support

Dette repository bruger et automatiseret oversættelsessystem:
- Understøtter 50+ sprog
- Oversættelser i `/translations/<lang-code>/` mapper
- GitHub Actions workflow håndterer opdateringer til oversættelser
- Kildefiler er på engelsk i repository rod

### Lektionsstruktur

Hver lektion følger et ensartet mønster:
1. Videominiature med link
2. Skrevet lektionindhold (README.md)
3. Kodeeksempler i flere frameworks
4. Læringsmål og forudsætninger
5. Ekstra læringsressourcer linket

### Navngivning af kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF avancerede mønstre
- `16-python-agent-framework.ipynb` - Lektion 16, produktionskunde-support agent
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
- `azure-ai-inference`, `azure-ai-projects` - Azure AI tjenester
- `azure-identity` - Azure autentificering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integration
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->