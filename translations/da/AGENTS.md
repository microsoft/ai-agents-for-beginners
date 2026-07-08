# AGENTS.md

## Projektoversigt

Dette repository indeholder "AI Agents for Beginners" - et omfattende undervisningskursus, der lærer alt, hvad der er nødvendigt for at bygge AI-agenter. Kurset består af 18 lektioner, der dækker grundlæggende principper, designmønstre, frameworks og produktionsudrulning af AI-agenter.

**Nøgle-teknologier:**
- Python 3.12+
- Jupyter-notebooks til interaktiv læring
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektur:**
- Lektion-baseret struktur (00-15+ mapper)
- Hver lektion indeholder: README-dokumentation, kodeeksempler (Jupyter-notebooks) og billeder
- Flersproget understøttelse via automatiseret oversættelsessystem
- En Python-notebook per lektion, der bruger Microsoft Agent Framework

## Opsætningskommandoer

### Forudsætninger
- Python 3.12 eller højere
- Azure-abonnement (til Microsoft Foundry)
- Azure CLI installeret og autentificeret (`az login`)

### Første opsætning

1. **Klon eller fork repository'et:**
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

4. **Sæt miljøvariabler:**
   ```bash
   cp .env.example .env
   # Rediger .env med dine API-nøgler og slutpunkter
   ```

### Krævede miljøvariabler

For **Microsoft Foundry** (påkrævet):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekt-endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modeldeployeringens navn (fx gpt-4o)

For **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search-endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nøgle

Autentificering: Kør `az login` før kørsel af notebooks (bruger `AzureCliCredential`).

## Udviklingsworkflow

### Kørsel af Jupyter-notebooks

Hver lektion indeholder flere Jupyter-notebooks for forskellige frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en lektionsmappe** (fx `01-intro-to-ai-agents/code_samples/`)

3. **Åbn og kør notebooks:**
   - `*-python-agent-framework.ipynb` - Bruger Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Bruger Microsoft Agent Framework (.NET)

### Arbejde med Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Kræver Azure-abonnement
- Bruger `FoundryChatClient` til Agent Service V2 (agenter synlige i Foundry-portalen)
- Produktionsklar med indbygget observabilitet
- Fil mønster: `*-python-agent-framework.ipynb`

## Testinstruktioner

Dette er et undervisningsrepository med eksempel-kode snarere end produktionskode med automatiserede tests. For at verificere din opsætning og ændringer:

### Manuel test

1. **Test Python-miljø:**
   ```bash
   python --version  # Bør være 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook-kørsel:**
   ```bash
   # Konverter notebook til script og kør (tester imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Bekræft miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Kørsel af individuelle notebooks

Åbn notebooks i Jupyter og kør cellerne sekventielt. Hver notebook er selvstændig og inkluderer:
- Import-udsagn
- Konfigurationsindlæsning
- Eksempel på agent-implementeringer
- Forventede output i markdown-celler

## Kodestil

### Python-konventioner

- **Python-version**: 3.12+
- **Kodestil**: Følg standard Python PEP 8-konventioner
- **Notebooks**: Brug klare markdown-celler til forklaring af koncepter
- **Imports**: Gruppér efter standardbibliotek, tredjepart, lokale imports

### Jupyter Notebook-konventioner

- Inkluder beskrivende markdown-celler før kodeceller
- Tilføj output-eksempler i notebooks som reference
- Brug klare variabelnavne, der matcher lektionskoncepter
- Hold notebook-kørselens rækkefølge lineær (celle 1 → 2 → 3...)

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

## Bygning og Udrulning

### Bygning af dokumentation

Dette repository bruger Markdown til dokumentation:
- README.md filer i hver lektionsmappe
- Hoved README.md i repository-roden
- Automatiseret oversættelsessystem via GitHub Actions

### CI/CD Pipeline

Ligger i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversættelse til 50+ sprog
2. **welcome-issue.yml** - Velkomst til nye issue-oprettere
3. **welcome-pr.yml** - Velkomst til nye pull request-bidragsydere

### Udrulning

Dette er et undervisningsrepository - ingen udrulningsproces. Brugere:
1. Fork eller klon repository
2. Kør notebooks lokalt eller i GitHub Codespaces
3. Lær ved at modificere og eksperimentere med eksempler

## Retningslinjer for Pull Requests

### Før indsending

1. **Test dine ændringer:**
   - Kør alle berørte notebooks fuldstændigt
   - Bekræft at alle celler kører uden fejl
   - Kontroller at output er passende

2. **Dokumentationsopdateringer:**
   - Opdater README.md ved tilføjelse af nye koncepter
   - Tilføj kommentarer i notebooks for kompleks kode
   - Sørg for, at markdown-celler forklarer formålet

3. **Filændringer:**
   - Undgå at committe `.env` filer (brug `.env.example`)
   - Commit ikke `venv/` eller `__pycache__/` mapper
   - Behold notebook-outputs når de demonstrerer koncepter
   - Fjern midlertidige filer og backup-notebooks (`*-backup.ipynb`)

### PR-titelformat

Brug beskrivende titler:
- `[Lesson-XX] Tilføj nyt eksempel for <koncept>`
- `[Fix] Ret stavefejl i lesson-XX README`
- `[Update] Forbedr kodeeksempel i lesson-XX`
- `[Docs] Opdater opsætningsinstruktioner`

### Krævede checks

- Notebooks bør eksekvere uden fejl
- README-filer bør være klare og præcise
- Følg eksisterende kode-mønstre i repository
- Oprethold konsistens med andre lektioner

## Yderligere noter

### Almindelige faldgruber

1. **Python version mismatch:**
   - Sørg for at bruge Python 3.12+
   - Nogle pakker virker ikke med ældre versioner
   - Brug `python3 -m venv` for eksplicit at specificere Python-version

2. **Miljøvariabler:**
   - Opret altid `.env` ud fra `.env.example`
   - Commit ikke `.env` filen (den er i `.gitignore`)
   - Login med `az login` for nøglefri Entra ID-autentificering

3. **Pakke-konflikter:**
   - Brug et friskt virtual environment
   - Installer fra `requirements.txt` i stedet for enkeltpakker
   - Nogle notebooks kan kræve ekstra pakker, som nævnes i deres markdown-celler

4. **Azure-tjenester:**
   - Azure AI-tjenester kræver aktivt abonnement
   - Nogle funktioner er regionsspecifikke
   - Sørg for, at din Azure OpenAI-modeludrulning understøtter Responses API

### Læringsforløb

Anbefalet progression gennem lektionerne:
1. **00-course-setup** - Start her for opsætning af miljø
2. **01-intro-to-ai-agents** - Forstå AI agent grundprincipper
3. **02-explore-agentic-frameworks** - Lær om forskellige frameworks
4. **03-agentic-design-patterns** - Kerne designmønstre
5. Fortsæt sekventielt gennem nummererede lektioner

### Framework-udvælgelse

Vælg framework baseret på dine mål:
- **Alle lektioner**: Microsoft Agent Framework (MAF) med `FoundryChatClient`
- **Agenter registreres server-side** i Microsoft Foundry Agent Service V2 og er synlige i Foundry-portalen

### Få hjælp

- Deltag i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Gennemgå lektions README-filer for specifik vejledning
- Se hoved [README.md](./README.md) for kursusoversigt
- Se [Course Setup](./00-course-setup/README.md) for detaljerede opsætningsinstruktioner

### Bidrag

Dette er et åbent undervisningsprojekt. Bidrag er velkomne:
- Forbedre kodeeksempler
- Ret stavefejl eller fejl
- Tilføj forklarende kommentarer
- Foreslå nye lektions-emner
- Oversæt til flere sprog

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for aktuelle behov.

## Projektspecifik kontekst

### Flersproget støtte

Dette repository bruger et automatiseret oversættelsessystem:
- Understøtter 50+ sprog
- Oversættelser i `/translations/<lang-code>/` mapper
- GitHub Actions workflow håndterer oversættelsesopdateringer
- Kildefiler er på engelsk i repository-roden

### Lektionsstruktur

Hver lektion følger et ensartet mønster:
1. Video thumbnail med link
2. Skrevet lektionsindhold (README.md)
3. Kodeeksempler i flere frameworks
4. Læringsmål og forudsætninger
5. Ekstra læringsressourcer linket

### Navngivning af kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF avancerede mønstre

### Specielle mapper

- `translated_images/` - Lokalt oversatte billeder til oversættelser
- `images/` - Originale billeder til engelsk indhold
- `.devcontainer/` - VS Code udviklingscontainer konfiguration
- `.github/` - GitHub Actions workflows og skabeloner

### Afhængigheder

Nøglepakker fra `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-til-Agent protokolstøtte
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjenester
- `azure-identity` - Azure autentificering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integration
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->