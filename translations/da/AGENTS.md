# AGENTS.md

## Projektoversigt

Dette repository indeholder "AI Agenter for Begyndere" - et omfattende uddannelseskursus, der lærer alt, hvad der behøves for at bygge AI-agenter. Kurset består af 18 lektioner, der dækker fundamenter, designmønstre, frameworks og produktionsimplementering af AI-agenter.

**Nøgle teknologier:**
- Python 3.12+
- Jupyter Notebooks til interaktiv læring
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkitektur:**
- Lektionbaseret struktur (00-15+ mapper)
- Hver lektion indeholder: README dokumentation, kodeeksempler (Jupyter notebooks) og billeder
- Understøttelse af flere sprog via automatiseret oversættelsessystem
- En Python-notebook pr. lektion, der bruger Microsoft Agent Framework

## Opsætningskommandoer

### Forudsætninger
- Python 3.12 eller nyere
- Azure-abonnement (til Azure AI Foundry)
- Azure CLI installeret og autentificeret (`az login`)

### Første opsætning

1. **Klon eller fork repositoryet:**  
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```
  
2. **Opret og aktiver Python virtuelt miljø:**  
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
   # Rediger .env med dine API-nøgler og endpoints
   ```
  
### Krævede miljøvariabler

For **Azure AI Foundry** (påkrævet):  
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry projekt-endpoint  
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model-implementeringsnavn (f.eks. gpt-4o)

For **Azure AI Search** (Lektion 05 - RAG):  
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint  
- `AZURE_SEARCH_API_KEY` - Azure AI Search API nøgle

Autentificering: Kør `az login` før du kører notebooks (bruger `AzureCliCredential`).

## Udviklingsworkflow

### Kørsel af Jupyter Notebooks

Hver lektion indeholder flere Jupyter notebooks til forskellige frameworks:

1. **Start Jupyter:**  
   ```bash
   jupyter notebook
   ```
  
2. **Naviger til lektionens mappe** (fx `01-intro-to-ai-agents/code_samples/`)

3. **Åbn og kør notebooks:**  
   - `*-python-agent-framework.ipynb` - Bruger Microsoft Agent Framework (Python)  
   - `*-dotnet-agent-framework.ipynb` - Bruger Microsoft Agent Framework (.NET)

### Arbejde med Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**  
- Kræver Azure-abonnement  
- Bruger `AzureAIProjectAgentProvider` for Agent Service V2 (agenter synlige i Foundry-portalen)  
- Produktionsklar med indbygget observabilitet  
- Filmønster: `*-python-agent-framework.ipynb`

## Testinstruktioner

Dette er et uddannelsesrepository med eksempel kode frem for produktionskode med automatiserede tests. For at verificere opsætning og ændringer:

### Manuel test

1. **Test Python-miljø:**  
   ```bash
   python --version  # Skal være 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```
  
2. **Test notebook-udførelse:**  
   ```bash
   # Konverter notebook til script og kør (tester imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```
  
3. **Bekræft miljøvariabler:**  
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```
  
### Kørsel af individuelle notebooks

Åbn notebooks i Jupyter og kør celler sekventielt. Hver notebook er selvstændig og indeholder:  
- Import-sætninger  
- Konfigurationsindlæsning  
- Eksempelagent-implementeringer  
- Forventede output i markdown-celler

## Kodestil

### Python-konventioner

- **Python-version**: 3.12+  
- **Kodestil**: Følg standard Python PEP 8-konventioner  
- **Notebooks**: Brug klare markdown-celler til at forklare koncepter  
- **Imports**: Grupper efter standardbibliotek, tredjepart, lokal import

### Jupyter Notebook-konventioner

- Inkludér beskrivende markdown-celler før kodeceller  
- Tilføj output-eksempler i notebooks til reference  
- Brug klare variabelnavne, som matcher lektionens koncepter  
- Hold notebook-udførelsesrækkefølgen lineær (celle 1 → 2 → 3...)

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
  
## Build og Deployment

### Bygning af dokumentation

Dette repository bruger Markdown til dokumentation:  
- README.md filer i hver lektion  
- Hoved README.md i repository-rod  
- Automatiseret oversættelsessystem via GitHub Actions

### CI/CD Pipeline

Findes i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversættelse til 50+ sprog  
2. **welcome-issue.yml** - Velkomst til nye issue-oprettere  
3. **welcome-pr.yml** - Velkomst til nye pull request-bidragsydere

### Deployment

Dette er et uddannelsesrepository - ingen deploymentsproces. Brugere:  
1. Fork eller klon repositoryet  
2. Kør notebooks lokalt eller i GitHub Codespaces  
3. Lær ved at ændre og eksperimentere med eksempler

## Pull Request Retningslinjer

### Før indsendelse

1. **Test dine ændringer:**  
   - Kør de berørte notebooks fuldstændigt  
   - Bekræft at alle celler udføres uden fejl  
   - Tjek at output er passende

2. **Dokumentationsopdateringer:**  
   - Opdater README.md ved tilføjelse af nye koncepter  
   - Tilføj kommentarer i notebooks til kompleks kode  
   - Sørg for at markdown-celler forklarer formålet

3. **Filændringer:**  
   - Undgå at committe `.env` filer (brug `.env.example`)  
   - Commit ikke `venv/` eller `__pycache__/` mapper  
   - Behold notebook-output, når de demonstrerer koncepter  
   - Fjern midlertidige filer og backup-notebooks (`*-backup.ipynb`)

### PR Titelformat

Brug beskrivende titler:  
- `[Lesson-XX] Tilføj nyt eksempel til <koncept>`  
- `[Fix] Korrigér tastefejl i lesson-XX README`  
- `[Update] Forbedr kodeeksempel i lesson-XX`  
- `[Docs] Opdater opsætningsinstruktioner`

### Krævede tjek

- Notebooks skal kunne køre uden fejl  
- README-filer skal være klare og nøjagtige  
- Følg eksisterende kodepatterns i repository  
- Oprethold konsistens med andre lektioner

## Yderligere bemærkninger

### Almindelige faldgruber

1. **Python-version mismatch:**  
   - Sørg for at bruge Python 3.12+  
   - Nogle pakker virker ikke med ældre versioner  
   - Brug `python3 -m venv` for eksplicit at angive Python-version

2. **Miljøvariabler:**  
   - Opret altid `.env` ud fra `.env.example`  
   - Commit ikke `.env`-fil (den er i `.gitignore`)  
   - GitHub-token skal have passende tilladelser

3. **Pakke-konflikter:**  
   - Brug et frisk virtuelt miljø  
   - Installer fra `requirements.txt` frem for enkelte pakker  
   - Nogle notebooks kræver ekstra pakker nævnt i markdown-celler

4. **Azure-tjenester:**  
   - Azure AI services kræver aktivt abonnement  
   - Nogle funktioner er regionspecifikke  
   - Gratis niveau har begrænsninger for GitHub Models

### Læringsvej

Anbefalet progression gennem lektioner:  
1. **00-course-setup** - Start her for miljøopsætning  
2. **01-intro-to-ai-agents** - Forstå AI-agent fundamenter  
3. **02-explore-agentic-frameworks** - Lær om forskellige frameworks  
4. **03-agentic-design-patterns** - Kerne designmønstre  
5. Fortsæt sekventielt gennem nummererede lektioner

### Framework valg

Vælg framework ud fra dine mål:  
- **Alle lektioner**: Microsoft Agent Framework (MAF) med `AzureAIProjectAgentProvider`  
- **Agenter registrerer server-side** i Azure AI Foundry Agent Service V2 og er synlige i Foundry-portalen

### Få hjælp

- Deltag i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)  
- Gennemgå lektionens README-filer for specifik vejledning  
- Se hoved [README.md](./README.md) for kursusoversigt  
- Se [Course Setup](./00-course-setup/README.md) for detaljerede opsætningsinstruktioner

### Bidrag

Dette er et åbent uddannelsesprojekt. Bidrag er velkomne:  
- Forbedr kodeeksempler  
- Ret tastefejl eller fejl  
- Tilføj forklarende kommentarer  
- Foreslå nye lektionsemner  
- Oversæt til flere sprog

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for aktuelle behov.

## Projektspecifik kontekst

### Understøttelse af flere sprog

Dette repository bruger et automatiseret oversættelsessystem:  
- 50+ understøttede sprog  
- Oversættelser i `/translations/<lang-code>/` mapper  
- GitHub Actions workflow håndterer oversættelsesopdateringer  
- Kildefiler er på engelsk i repository-rod

### Lektionstruktur

Hver lektion følger et ensartet mønster:  
1. Video-miniature med link  
2. Skriftligt lektionindhold (README.md)  
3. Kodeeksempler i flere frameworks  
4. Læringsmål og forudsætninger  
5. Ekstra læringsressourcer linket

### Navngivning af kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`  
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python  
- `14-sequential.ipynb` - Lektion 14, MAF avancerede mønstre

### Specielle mapper

- `translated_images/` - Lokaliserede billeder til oversættelser  
- `images/` - Originale billeder til engelsk indhold  
- `.devcontainer/` - VS Code udviklingscontainer konfiguration  
- `.github/` - GitHub Actions workflows og skabeloner

### Afhængigheder

Vigtige pakker fra `requirements.txt`:  
- `agent-framework` - Microsoft Agent Framework  
- `a2a-sdk` - Agent-til-Agent protokol support  
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services  
- `azure-identity` - Azure autentificering (AzureCliCredential)  
- `azure-search-documents` - Azure AI Search integration  
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->