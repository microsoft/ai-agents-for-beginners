# AGENTS.md

## Projektöversikt

Detta repo innehåller "AI-agenter för nybörjare" - en omfattande utbildningskurs som lär ut allt som behövs för att bygga AI-agenter. Kursen består av 15+ lektioner som täcker grunder, designmönster, ramverk och produktionssättning av AI-agenter.

**Nyckelteknologier:**
- Python 3.12+
- Jupyter Notebook för interaktivt lärande
- AI-ramverk: Microsoft Agent Framework (MAF)
- Azure AI-tjänster: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkitektur:**
- Lektionbaserad struktur (00-15+ kataloger)
- Varje lektion innehåller: README-dokumentation, kodexempel (Jupyter notebooks) och bilder
- Flernivåspråkstöd via automatiserat översättningssystem
- En Python-notebook per lektion som använder Microsoft Agent Framework

## Uppstartskommandon

### Förutsättningar
- Python 3.12 eller högre
- Azure-prenumeration (för Azure AI Foundry)
- Azure CLI installerad och autentiserad (`az login`)

### Initial uppsättning

1. **Klona eller forka repot:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Skapa och aktivera Python-virtuell miljö:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # På Windows: venv\Scripts\activate
   ```

3. **Installera beroenden:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Konfigurera miljövariabler:**
   ```bash
   cp .env.example .env
   # Redigera .env med dina API-nycklar och slutpunkter
   ```

### Obligatoriska miljövariabler

För **Azure AI Foundry** (obligatoriskt):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry projekt-endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modellutplaceringens namn (t.ex. gpt-4o)

För **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search-endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nyckel

Autentisering: Kör `az login` innan du kör notebooks (använder `AzureCliCredential`).

## Utvecklingsarbetsflöde

### Köra Jupyter Notebooks

Varje lektion innehåller flera Jupyter notebooks för olika ramverk:

1. **Starta Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigera till lektionens katalog** (t.ex. `01-intro-to-ai-agents/code_samples/`)

3. **Öppna och kör notebooks:**
   - `*-python-agent-framework.ipynb` - Använder Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Använder Microsoft Agent Framework (.NET)

### Arbeta med Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Kräver Azure-prenumeration
- Använder `AzureAIProjectAgentProvider` för Agent Service V2 (agenter synliga i Foundry-portalen)
- Produktionsredo med inbyggd övervakning
- Filnamnsmönster: `*-python-agent-framework.ipynb`

## Testinstruktioner

Detta är ett utbildningsrepo med exempel kod snarare än produktionskod med automatiska tester. För att verifiera din setup och ändringar:

### Manuella tester

1. **Testa Python-miljön:**
   ```bash
   python --version  # Bör vara 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testa körning av notebook:**
   ```bash
   # Konvertera anteckningsbok till skript och kör (testar importer)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiera miljövariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Köra enskilda notebooks

Öppna notebooks i Jupyter och kör celler i ordning. Varje notebook är självständig och innehåller:
- Import-satser
- Konfigurationsladdning
- Exempelagent-implementationer
- Förväntade utdata i markdown-celler

## Kodstil

### Python-konventioner

- **Pythonversion**: 3.12+
- **Kodstil**: Följ standard PEP 8-konventioner för Python
- **Notebooks**: Använd tydliga markdown-celler för att förklara koncept
- **Imports**: Gruppera efter standardbibliotek, tredjeparts, lokala imports

### Jupyter Notebook-konventioner

- Inkludera beskrivande markdown-celler före kodceller
- Lägg till exempel på utdata i notebooks för referens
- Använd tydliga variabelnamn som matchar lektionens koncept
- Behåll linjär körordning i notebooks (cell 1 → 2 → 3...)

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

Detta repo använder Markdown för dokumentation:
- README.md-filer i varje lektionskatalog
- Huvud-README.md i reporötterna
- Automatiserat översättningssystem via GitHub Actions

### CI/CD-pipeline

Finns i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk översättning till 50+ språk
2. **welcome-issue.yml** - Hälsar nya issue-skapare välkomna
3. **welcome-pr.yml** - Hälsar nya PR-bidragsgivare välkomna

### Distribution

Detta är ett utbildningsrepo - ingen distributionsprocess. Användare:
1. Forkar eller klonar repot
2. Kör notebooks lokalt eller i GitHub Codespaces
3. Lär sig genom att modifiera och experimentera med exempel

## Riktlinjer för Pull Requests

### Innan inlämning

1. **Testa dina ändringar:**
   - Kör berörda notebooks helt
   - Kontrollera att alla celler kör utan fel
   - Se att utdata är lämpliga

2. **Dokumentationsuppdateringar:**
   - Uppdatera README.md om du lägger till nya koncept
   - Lägg till kommentarer i notebooks för komplex kod
   - Säkerställ att markdown-celler förklarar syftet

3. **Filsändringar:**
   - Undvik att committa `.env`-filer (använd `.env.example`)
   - Commita inte `venv/` eller `__pycache__/`-mappar
   - Behåll notebook-utdata när de visar koncept
   - Ta bort temporära filer och backup-notebooks (`*-backup.ipynb`)

### PR-titelformat

Använd beskrivande titlar:
- `[Lesson-XX] Lägg till nytt exempel för <concept>`
- `[Fix] Rätta stavfel i lesson-XX README`
- `[Update] Förbättra kodexempel i lesson-XX`
- `[Docs] Uppdatera installationsinstruktioner`

### Obligatoriska kontroller

- Notebooks ska köras utan fel
- README-filer ska vara klara och korrekta
- Följ befintliga kodmönster i repot
- Behåll konsekvens med andra lektioner

## Ytterligare anteckningar

### Vanliga fallgropar

1. **Pythonversionsfel:**
   - Säkerställ att Python 3.12+ används
   - Vissa paket fungerar inte med äldre versioner
   - Använd `python3 -m venv` för att specificera Python-version explicit

2. **Miljövariabler:**
   - Skapa alltid `.env` från `.env.example`
   - Committa inte `.env`-filen (finns i `.gitignore`)
   - GitHub-token behöver rätt behörigheter

3. **Paketkonflikter:**
   - Använd en ny virtuell miljö
   - Installera från `requirements.txt` istället för individuella paket
   - Vissa notebooks kan kräva extra paket nämnda i markdown-celler

4. **Azure-tjänster:**
   - Azure AI-tjänster kräver aktiv prenumeration
   - Vissa funktioner är regionsspecifika
   - Gratisnivåbegränsningar gäller för GitHub Models

### Lärandestig

Rekommenderad ordning för lektioner:
1. **00-course-setup** - Börja här för miljöuppsättning
2. **01-intro-to-ai-agents** - Förstå AI-agenters grunder
3. **02-explore-agentic-frameworks** - Lär om olika ramverk
4. **03-agentic-design-patterns** - Kärndesignmönster
5. Fortsätt i nummerordning

### Val av ramverk

Välj ramverk utifrån mål:
- **Alla lektioner**: Microsoft Agent Framework (MAF) med `AzureAIProjectAgentProvider`
- **Agenter registreras serversidan** i Azure AI Foundry Agent Service V2 och syns i Foundry-portalen

### Hjälp

- Gå med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Granska lektions-README-filer för specifik vägledning
- Kontrollera huvud-README.md för kursöversikt
- Se [Course Setup](./00-course-setup/README.md) för detaljerad installationsguide

### Bidra

Detta är ett öppet utbildningsprojekt. Bidrag välkomnas:
- Förbättra kodexempel
- Rätta stavfel eller buggar
- Lägg till förtydligande kommentarer
- Föreslå nya lektionsteman
- Översätt till fler språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) för aktuella behov.

## Projektspecifik kontext

### Flernivåspråkstöd

Detta repo använder ett automatiserat översättningssystem:
- 50+ språk stöds
- Översättningar i `/translations/<lang-code>/` kataloger
- GitHub Actions hanterar översättningsuppdateringar
- Källfiler är på engelska i reporötterna

### Lektionsstruktur

Varje lektion följer en konsekvent mall:
1. Videominiatyr med länk
2. Skrivet lektionsinnehåll (README.md)
3. Kodexempel i flera ramverk
4. Läromål och förkunskaper
5. Extra läromaterial länkade

### Kodexempelnamn

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, avancerade MAF-mönster

### Särskilda kataloger

- `translated_images/` - Lokalt översatta bilder
- `images/` - Originalbilder för engelskt innehåll
- `.devcontainer/` - VS Code utvecklingscontainerkonfiguration
- `.github/` - GitHub Actions arbetsflöden och mallar

### Beroenden

Viktiga paket från `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-till-agent-protokollstöd
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjänster
- `azure-identity` - Azure autentisering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search-integration
- `mcp[cli]` - Modell Context Protocol-stöd

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår genom användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->