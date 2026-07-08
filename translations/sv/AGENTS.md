# AGENTS.md

## Projektöversikt

Det här arkivet innehåller "AI Agents for Beginners" - en omfattande utbildningskurs som lär ut allt som behövs för att bygga AI-agenter. Kursen består av 18 lektioner som täcker grundläggande principer, designmönster, ramverk och produktionssättning av AI-agenter.

**Nyckelteknologier:**
- Python 3.12+
- Jupyter Notebooks för interaktivt lärande
- AI-ramverk: Microsoft Agent Framework (MAF)
- Azure AI-tjänster: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektur:**
- Lektionbaserad struktur (00-15+ kataloger)
- Varje lektion innehåller: README-dokumentation, kodexempel (Jupyter-notebooks) och bilder
- Flerspråkigt stöd via automatiserat översättningssystem
- En Python-notebook per lektion som använder Microsoft Agent Framework

## Installationskommandon

### Förutsättningar
- Python 3.12 eller senare
- Azure-prenumeration (för Microsoft Foundry)
- Azure CLI installerad och autentiserad (`az login`)

### Initial installation

1. **Klona eller forka arkivet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Skapa och aktivera virtuell Python-miljö:**
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

### Obligatoriska miljövariabler

För **Microsoft Foundry** (Obligatoriskt):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint för Microsoft Foundry-projekt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Namn på modelldistribution (t.ex. gpt-4o)

För **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint för Azure AI Search
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nyckel

Autentisering: Kör `az login` innan du kör notebooks (använder `AzureCliCredential`).

## Utvecklingsarbetsflöde

### Köra Jupyter-notebooks

Varje lektion innehåller flera Jupyter-notebooks för olika ramverk:

1. **Starta Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigera till en lektionskatalog** (t.ex. `01-intro-to-ai-agents/code_samples/`)

3. **Öppna och kör notebooks:**
   - `*-python-agent-framework.ipynb` - Använder Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Använder Microsoft Agent Framework (.NET)

### Arbeta med Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Kräver Azure-prenumeration
- Använder `FoundryChatClient` för Agent Service V2 (agenter synliga i Foundry-portalen)
- Produktionsredo med inbyggd observabilitet
- Filformat: `*-python-agent-framework.ipynb`

## Testinstruktioner

Detta är ett utbildningsarkiv med exempel på kod snarare än produktionskod med automatiska tester. För att verifiera din setup och ändringar:

### Manuell testning

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
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Köra enskilda notebooks

Öppna notebooks i Jupyter och exekvera celler sekventiellt. Varje notebook är självständig och innehåller:
- Importera satser
- Konfigurationsladdning
- Exempel på agent-implementeringar
- Förväntade resultat i markdown-celler

## Kodstil

### Python-konventioner

- **Python-version**: 3.12+
- **Kodstil**: Följ standardiserade Python PEP 8-konventioner
- **Notebooks**: Använd tydliga markdown-celler för att förklara koncept
- **Importer**: Gruppera efter standardbibliotek, tredjepart, lokala importer

### Jupyter Notebook-konventioner

- Inkludera beskrivande markdown-celler före kodceller
- Lägg till output-exempel i notebooks för referens
- Använd tydliga variabelnamn som matchar lektionskoncept
- Håll exekveringsordningen linjär (cell 1 → 2 → 3 ...)

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

Det här arkivet använder Markdown för dokumentation:
- README.md-filer i varje lektionsmapp
- Huvud-README.md i arkivets rot
- Automatiserat översättningssystem via GitHub Actions

### CI/CD-pipeline

Finns i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk översättning till 50+ språk
2. **welcome-issue.yml** - Hälsar nya issuesskapare välkomna
3. **welcome-pr.yml** - Hälsar nya pull request-bidragsgivare välkomna

### Distribution

Detta är ett utbildningsarkiv - ingen distributionsprocess. Användare:
1. Forkar eller klonar arkivet
2. Kör notebooks lokalt eller i GitHub Codespaces
3. Lär sig genom att modifiera och experimentera med exempel

## Riktlinjer för pull requests

### Innan du skickar in

1. **Testa dina ändringar:**
   - Kör de påverkade notebooks helt
   - Verifiera att alla celler körs utan fel
   - Kontrollera att output är passande

2. **Dokumentationsuppdateringar:**
   - Uppdatera README.md om nya koncept läggs till
   - Lägg till kommentarer i notebooks för komplex kod
   - Säkerställ att markdown-celler förklarar syftet

3. **Filändringar:**
   - Undvik att committa `.env`-filer (använd `.env.example`)
   - Committa inte `venv/` eller `__pycache__/` kataloger
   - Behåll notebook-output om de visar koncept
   - Ta bort temporära filer och backup-notebooks (`*-backup.ipynb`)

### PR-titelformat

Använd beskrivande titlar:
- `[Lesson-XX] Lägg till nytt exempel för <koncept>`
- `[Fix] Korrigera felskrivning i lesson-XX README`
- `[Update] Förbättra kodexempel i lesson-XX`
- `[Docs] Uppdatera installationsinstruktioner`

### Obligatoriska kontroller

- Notebooks ska köras utan fel
- README-filer ska vara tydliga och korrekta
- Följ existerande kodmönster i arkivet
- Behåll konsekvens med övriga lektioner

## Ytterligare anteckningar

### Vanliga fallgropar

1. **Python-version mismatch:**
   - Se till att Python 3.12+ används
   - Vissa paket fungerar inte med äldre versioner
   - Använd `python3 -m venv` för att explicit ange Python-version

2. **Miljövariabler:**
   - Skapa alltid `.env` från `.env.example`
   - Committa aldrig `.env`-filen (är i `.gitignore`)
   - Logga in med `az login` för autentisering utan nycklar via Entra ID

3. **Paketkonflikter:**
   - Använd en ny virtuell miljö
   - Installera via `requirements.txt` snarare än enskilda paket
   - Vissa notebooks kan kräva ytterligare paket nämnda i markdown-celler

4. **Azure-tjänster:**
   - Azure AI-tjänster kräver aktiv prenumeration
   - Vissa funktioner är regionspecifika
   - Se till att din Azure OpenAI modelldistribution stöder Responses API

### Lärandestig

Rekommenderad progression genom lektionerna:
1. **00-course-setup** - Börja här för miljösetup
2. **01-intro-to-ai-agents** - Förstå AI-agenters grunder
3. **02-explore-agentic-frameworks** - Lär dig om olika ramverk
4. **03-agentic-design-patterns** - Kärndesignmönster
5. Fortsätt genom numrerade lektioner i ordning

### Ramverksval

Välj ramverk utifrån dina mål:
- **Alla lektioner**: Microsoft Agent Framework (MAF) med `FoundryChatClient`
- **Agenter registreras server-side** i Microsoft Foundry Agent Service V2 och är synliga i Foundry-portalen

### Få hjälp

- Gå med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Granska lektions-README för specifika anvisningar
- Se huvud-[README.md](./README.md) för kursöversikt
- Följ [Course Setup](./00-course-setup/README.md) för detaljerad installationsguide

### Bidra

Detta är ett öppet utbildningsprojekt. Bidrag välkomnas:
- Förbättra kodexempel
- Rätta stavfel eller fel
- Lägg till förtydligande kommentarer
- Föreslå nya lektionsämnen
- Översätt till fler språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) för aktuella behov.

## Projektspecifik kontext

### Flerspråkigt stöd

Detta arkiv använder ett automatiserat översättningssystem:
- Stöd för 50+ språk
- Översättningar i `/translations/<lang-code>/` kataloger
- GitHub Actions hanterar översättningsuppdateringar
- Källfiler är på engelska i arkivets rot

### Lektionsstruktur

Varje lektion följer ett konsekvent mönster:
1. Videominiatyr med länk
2. Skrivet lektionsinnehåll (README.md)
3. Kodexempel i flera ramverk
4. Lärandemål och förkunskaper
5. Extra lärresurser länkade

### Namngivning av kodexempel

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF avancerade mönster

### Specialkataloger

- `translated_images/` - Lokaliserade bilder för översättningar
- `images/` - Originalbilder för engelskt innehåll
- `.devcontainer/` - VS Code utvecklingscontainer-konfiguration
- `.github/` - GitHub Actions arbetsflöden och mallar

### Beroenden

Viktiga paket från `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-till-agent protokollstöd
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjänster
- `azure-identity` - Azure autentisering (AzureCliCredential)
- `azure-search-documents` - Integrering av Azure AI Search
- `mcp[cli]` - Modell Context Protocol-stöd

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->