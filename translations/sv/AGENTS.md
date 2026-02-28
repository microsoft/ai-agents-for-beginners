# AGENTS.md

## Projektöversikt

Detta repository innehåller "AI-agenter för nybörjare" - en omfattande utbildningskurs som lär ut allt som behövs för att bygga AI-agenter. Kursen består av 15+ lektioner som täcker grunder, designmönster, ramverk och produktionssättning av AI-agenter.

**Nyckelteknologier:**
- Python 3.12+
- Jupyter Notebooks för interaktivt lärande
- AI-ramverk: Microsoft Agent Framework (MAF)
- Azure AI-tjänster: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkitektur:**
- Lektionbaserad struktur (00-15+ kataloger)
- Varje lektion innehåller: README-dokumentation, kodexempel (Jupyter notebooks) och bilder
- Flerspråkigt stöd via automatiskt översättningssystem
- En Python-notebook per lektion med Microsoft Agent Framework

## Installationskommandon

### Förutsättningar
- Python 3.12 eller högre
- Azure-prenumeration (för Azure AI Foundry)
- Azure CLI installerat och autentiserat (`az login`)

### Initial installation

1. **Klona eller fork:a repositoryt:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Skapa och aktivera Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # På Windows: venv\Scripts\activate
   ```

3. **Installera beroenden:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ställ in miljövariabler:**
   ```bash
   cp .env.example .env
   # Redigera .env med dina API-nycklar och slutpunkter
   ```

### Nödvändiga miljövariabler

För **Azure AI Foundry** (obligatoriskt):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry projekt-endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modelldistributionens namn (t.ex. gpt-4o)

För **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search-endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nyckel

Autentisering: Kör `az login` innan du kör notebooks (använder `AzureCliCredential`).

## Utvecklingsflöde

### Köra Jupyter Notebooks

Varje lektion innehåller flera Jupyter notebooks för olika ramverk:

1. **Starta Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigera till en lektionskatalog** (t.ex. `01-intro-to-ai-agents/code_samples/`)

3. **Öppna och kör notebooks:**
   - `*-python-agent-framework.ipynb` - Använder Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Använder Microsoft Agent Framework (.NET)

### Arbeta med Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Kräver Azure-prenumeration
- Använder `AzureAIProjectAgentProvider` för Agent Service V2 (agenter synliga i Foundry-portalen)
- Produktionsfärdigt med inbyggd övervakning
- Filnamnsmönster: `*-python-agent-framework.ipynb`

## Testinstruktioner

Detta är ett utbildningsrepository med exempel på kod snarare än produktionskod med automatiska tester. För att verifiera din installation och ändringar:

### Manuella tester

1. **Testa Python-miljön:**
   ```bash
   python --version  # Bör vara 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testa körning av notebook:**
   ```bash
   # Konvertera anteckningsbok till skript och kör (testar importeringar)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiera miljövariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Köra enskilda notebooks

Öppna notebooks i Jupyter och kör cellerna i ordning. Varje notebook är självständig och inkluderar:
- Importer
- Konfigurationsladdning
- Exempel på agent-implementationer
- Förväntade utdata i markdown-celler

## Kodstil

### Python-konventioner

- **Python-version:** 3.12+
- **Kodstil:** Följ standard PEP 8-konventioner för Python
- **Notebooks:** Använd tydliga markdown-celler för att förklara koncept
- **Import:** Gruppera standardbibliotek, tredjepart och lokala importer

### Jupyter Notebook-konventioner

- Inkludera beskrivande markdown-celler före kodceller
- Lägg till output-exempel i notebooks för referens
- Använd tydliga variabelnamn som matchar lektionskoncepten
- Håll exekveringsordningen i notebook linjär (cell 1 → 2 → 3...)

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

## Bygg och distribution

### Bygga dokumentation

Detta repository använder Markdown för dokumentation:
- README.md-filer i varje lektionsmapp
- Huvud-README.md i repositorys rot
- Automatiskt översättningssystem via GitHub Actions

### CI/CD-pipeline

Finns i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk översättning till 50+ språk
2. **welcome-issue.yml** - Hälsar nya issue-skapare välkomna
3. **welcome-pr.yml** - Hälsar nya pull request-bidragsgivare välkomna

### Distribution

Detta är ett utbildningsrepository - ingen distribueringsprocess. Användare:
1. Forkar eller klonar repositoryt
2. Kör notebooks lokalt eller i GitHub Codespaces
3. Lär genom att modifiera och experimentera med exempel

## Riktlinjer för Pull Requests

### Innan du skickar in

1. **Testa dina ändringar:**
   - Kör berörda notebooks helt
   - Verifiera att alla celler körs utan fel
   - Kontrollera att utdata är lämpliga

2. **Uppdatera dokumentation:**
   - Uppdatera README.md om nya koncept läggs till
   - Lägg till kommentarer i notebooks för komplex kod
   - Säkerställ att markdown-celler förklarar syftet

3. **Filändringar:**
   - Undvik att committa `.env`-filer (använd `.env.example`)
   - Commita inte `venv/` eller `__pycache__/`-kataloger
   - Behåll notebookutdata när de demonstrerar koncept
   - Ta bort temporära filer och backup-notebooks (`*-backup.ipynb`)

### PR-titelformat

Använd beskrivande titlar:
- `[Lesson-XX] Lägg till nytt exempel för <concept>`
- `[Fix] Korrigera stavfel i lesson-XX README`
- `[Update] Förbättra kodexempel i lesson-XX`
- `[Docs] Uppdatera installationsinstruktioner`

### Nödvändiga kontroller

- Notebooks ska köras utan fel
- README-filer ska vara tydliga och korrekta
- Följ befintliga kodmönster i repositoryt
- Behåll konsekvens med övriga lektioner

## Ytterligare anmärkningar

### Vanliga fallgropar

1. **Python-version mismatch:**
   - Säkerställ att Python 3.12+ används
   - Vissa paket fungerar inte med äldre versioner
   - Använd `python3 -m venv` för att ange Python-version explicit

2. **Miljövariabler:**
   - Skapa alltid `.env` från `.env.example`
   - Committa inte `.env`-filen (finns i `.gitignore`)
   - GitHub-token behöver rätt behörigheter

3. **Paketkonflikter:**
   - Använd en ny virtuell miljö
   - Installera från `requirements.txt` istället för enskilda paket
   - Vissa notebooks kan behöva extra paket som nämns i deras markdown-celler

4. **Azure-tjänster:**
   - Azure AI-tjänster kräver aktiv prenumeration
   - Vissa funktioner är regionsspecifika
   - Begränsningar i fri nivå gäller för GitHub Models

### Lärandespår

Rekommenderad ordning av lektioner:
1. **00-course-setup** - Börja här för miljöinstallation
2. **01-intro-to-ai-agents** - Förstå AI-agenters grunder
3. **02-explore-agentic-frameworks** - Lär dig om olika ramverk
4. **03-agentic-design-patterns** - Viktiga designmönster
5. Fortsätt genom numrerade lektioner i ordning

### Val av ramverk

Välj ramverk baserat på dina mål:
- **Alla lektioner:** Microsoft Agent Framework (MAF) med `AzureAIProjectAgentProvider`
- **Agenter registreras serverside** i Azure AI Foundry Agent Service V2 och syns i Foundry-portalen

### Hjälp och support

- Gå med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Läs lektions-README-filer för specifika instruktioner
- Se huvud-README.md för kursöversikt
- Läs [Course Setup](./00-course-setup/README.md) för detaljerade installationsinstruktioner

### Bidra

Detta är ett öppet utbildningsprojekt. Bidrag välkomnas:
- Förbättra kodexempel
- Korrigera stavfel eller fel
- Lägg till förklarande kommentarer
- Föreslå nya lektionsämnen
- Översätt till fler språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) för nuvarande behov.

## Projektspecifik kontext

### Flerspråkigt stöd

Detta repository använder ett automatiskt översättningssystem:
- Stöder 50+ språk
- Översättningar i `/translations/<lang-code>/`-kataloger
- GitHub Actions workflow hanterar översättningsuppdateringar
- Källfiler finns på engelska i repositorys rot

### Lektionsstruktur

Varje lektion följer ett konsekvent mönster:
1. Videominiatyr med länk
2. Skriftligt lektionsinnehåll (README.md)
3. Kodexempel i flera ramverk
4. Lärandemål och förkunskaper
5. Extra resurser kopplade

### Namngivning av kodexempel

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF avancerade mönster

### Speciella kataloger

- `translated_images/` - Lokalt översatta bilder
- `images/` - Originalbilder för engelskt innehåll
- `.devcontainer/` - VS Code utvecklingscontainer-konfiguration
- `.github/` - GitHub Actions workflows och mallar

### Beroenden

Viktiga paket från `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-till-agent-protokollstöd
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjänster
- `azure-identity` - Azure-autentisering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search-integration
- `mcp[cli]` - Model Context Protocol-stöd

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig märk att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->