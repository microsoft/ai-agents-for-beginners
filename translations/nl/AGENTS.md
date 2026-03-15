# AGENTS.md

## Projectoverzicht

Deze repository bevat "AI Agents voor Beginners" - een uitgebreide educatieve cursus die alles leert wat nodig is om AI-agents te bouwen. De cursus bestaat uit meer dan 15 lessen die de fundamenten, ontwerp patronen, frameworks en productie-implementatie van AI-agents behandelen.

**Belangrijke technologieën:**
- Python 3.12+
- Jupyter Notebooks voor interactieve leerervaring
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architectuur:**
- Les-gebaseerde structuur (00-15+ mappen)
- Elke les bevat: README-documentatie, codevoorbeelden (Jupyter notebooks), en afbeeldingen
- Meertalige ondersteuning via geautomatiseerd vertalingssysteem
- Eén Python-notebook per les die Microsoft Agent Framework gebruikt

## Setup Commando's

### Vereisten
- Python 3.12 of hoger
- Azure-abonnement (voor Azure AI Foundry)
- Azure CLI geïnstalleerd en geauthenticeerd (`az login`)

### Initiële Setup

1. **Clone of fork de repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OF
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Maak en activeer een Python virtuele omgeving:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Op Windows: venv\Scripts\activate
   ```

3. **Installeer afhankelijkheden:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Stel omgevingsvariabelen in:**
   ```bash
   cp .env.example .env
   # Bewerk .env met uw API-sleutels en eindpunten
   ```

### Vereiste Omgevingsvariabelen

Voor **Azure AI Foundry** (vereist):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Naam van model deployment (bijv. gpt-4o)

Voor **Azure AI Search** (Les 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API sleutel

Authenticatie: Voer `az login` uit vóór het starten van notebooks (gebruikt `AzureCliCredential`).

## Ontwikkelingsworkflow

### Jupyter Notebooks draaien

Elke les bevat meerdere Jupyter notebooks voor verschillende frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigeer naar een lesmap** (bijv. `01-intro-to-ai-agents/code_samples/`)

3. **Open en voer notebooks uit:**
   - `*-python-agent-framework.ipynb` - Gebruik Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Gebruik Microsoft Agent Framework (.NET)

### Werken met Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Vereist Azure-abonnement
- Gebruikt `AzureAIProjectAgentProvider` voor Agent Service V2 (agents zichtbaar in Foundry portaal)
- Productieklaar met ingebouwde observability
- Bestandsnaam patroon: `*-python-agent-framework.ipynb`

## Testinstructies

Dit is een educatieve repository met voorbeeldcode in plaats van productiecode met geautomatiseerde tests. Om je setup en aanpassingen te verifiëren:

### Handmatig Testen

1. **Test Python-omgeving:**
   ```bash
   python --version  # Moet 3.12+ zijn
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test uitvoering notebook:**
   ```bash
   # Converteer notebook naar script en voer uit (test importeringen)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifieer omgevingsvariabelen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Individuele Notebooks uitvoeren

Open notebooks in Jupyter en voer cellen sequentieel uit. Elke notebook is op zichzelf staand en bevat:
- Import statements
- Configuratie laden
- Voorbeeld agent implementaties
- Verwachte outputs in markdown cellen

## Code Stijl

### Python Conventies

- **Python versie**: 3.12+
- **Code stijl**: Volg standaard Python PEP 8 conventies
- **Notebooks**: Gebruik duidelijke markdown cellen om concepten uit te leggen
- **Imports**: Groepeer op standaardbibliotheek, derde partij en lokale imports

### Jupyter Notebook Conventies

- Voeg beschrijvende markdown cellen toe vóór codecellen
- Voeg uitvoeringsvoorbeelden toe in notebooks ter referentie
- Gebruik duidelijke variabelenamen die passen bij lesconcepten
- Houd de volgorde van notebook uitvoering lineair (cel 1 → 2 → 3…)

### Bestandsorganisatie

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Build en Deploy

### Documentatie bouwen

Deze repository gebruikt Markdown voor documentatie:
- README.md bestanden in elke lesmap
- Hoofd README.md in de repository root
- Geautomatiseerd vertaalsysteem via GitHub Actions

### CI/CD Pipeline

Te vinden in `.github/workflows/`:

1. **co-op-translator.yml** - Automatische vertaling naar meer dan 50 talen
2. **welcome-issue.yml** - Verwelkomt nieuwe issue makers
3. **welcome-pr.yml** - Verwelkomt nieuwe pull request bijdragers

### Deployment

Dit is een educatieve repository - geen deployment proces. Gebruikers:
1. Forken of clonen de repository
2. Runnen notebooks lokaal of in GitHub Codespaces
3. Leren door voorbeelden aan te passen en te experimenteren

## Pull Request Richtlijnen

### Voor het indienen

1. **Test je veranderingen:**
   - Run de getroffen notebooks volledig
   - Verifieer dat alle cellen zonder fouten worden uitgevoerd
   - Controleer of outputs passend zijn

2. **Documentatie updates:**
   - Update README.md bij toevoeging van nieuwe concepten
   - Voeg commentaar toe in notebooks bij complexe code
   - Zorg dat markdown cellen het doel uitleggen

3. **Bestandswijzigingen:**
   - Vermijd het committen van `.env` bestanden (gebruik `.env.example`)
   - Commit geen `venv/` of `__pycache__/` mappen
   - Houd notebook outputs als ze concepten demonstreren
   - Verwijder tijdelijke bestanden en backup notebooks (`*-backup.ipynb`)

### PR Titel Formaat

Gebruik beschrijvende titels:
- `[Lesson-XX] Voeg nieuw voorbeeld toe voor <concept>`
- `[Fix] Corrigeer typefout in lesson-XX README`
- `[Update] Verbeter codevoorbeeld in lesson-XX`
- `[Docs] Update setup instructies`

### Vereiste Checks

- Notebooks moeten foutloos uitvoeren
- README bestanden moeten duidelijk en correct zijn
- Volg bestaande codepatronen in de repository
- Houd consistentie met andere lessen

## Aanvullende Notities

### Veelvoorkomende valkuilen

1. **Python versie mismatch:**
   - Zorg dat Python 3.12+ wordt gebruikt
   - Sommige packages werken niet met oudere versies
   - Gebruik `python3 -m venv` om expliciet Python versie te specificeren

2. **Omgevingsvariabelen:**
   - Maak altijd `.env` aan van `.env.example`
   - Commit geen `.env` bestand (staat in `.gitignore`)
   - GitHub token vereist juiste permissies

3. **Package conflicten:**
   - Gebruik een verse virtuele omgeving
   - Installeer vanaf `requirements.txt` in plaats van losse pakketten
   - Sommige notebooks vereisen extra packages genoemd in hun markdown cellen

4. **Azure services:**
   - Azure AI diensten vereisen een actief abonnement
   - Sommige functies zijn regio-specifiek
   - Gratis tier beperkingen gelden voor GitHub Models

### Leertraject

Aanbevolen volgorde van lessen:
1. **00-course-setup** - Begin hier voor omgeving setup
2. **01-intro-to-ai-agents** - Begrijp AI agent fundamenten
3. **02-explore-agentic-frameworks** - Leer verschillende frameworks kennen
4. **03-agentic-design-patterns** - Kern ontwerp patronen
5. Volg daarna de genummerde lessen op volgorde

### Framework Keuze

Kies framework afhankelijk van je doelen:
- **Alle lessen**: Microsoft Agent Framework (MAF) met `AzureAIProjectAgentProvider`
- **Agents registreren server-side** in Azure AI Foundry Agent Service V2 en zijn zichtbaar in Foundry portaal

### Hulp krijgen

- Word lid van de [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Bekijk de README-bestanden van de lessen voor specifieke begeleiding
- Raadpleeg de hoofd [README.md](./README.md) voor cursusoverzicht
- Zie [Course Setup](./00-course-setup/README.md) voor gedetailleerde setup instructies

### Bijdragen

Dit is een open educatief project. Bijdragen zijn welkom:
- Verbeter codevoorbeelden
- Corrigeer typefouten of fouten
- Voeg verduidelijkende opmerkingen toe
- Stel nieuwe lesonderwerpen voor
- Vertaal naar extra talen

Zie [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) voor huidige behoeften.

## Projectspecifieke Context

### Meertalige Ondersteuning

Deze repository gebruikt een geautomatiseerd vertaalsysteem:
- Meer dan 50 talen ondersteund
- Vertalingen in `/translations/<lang-code>/` mappen
- GitHub Actions workflow verzorgt vertaalupdates
- Brondocumenten zijn in het Engels in de root van de repository

### Lesstructuur

Elke les volgt een consistent patroon:
1. Videominiatuur met link
2. Geschreven lesinhoud (README.md)
3. Codevoorbeelden in meerdere frameworks
4. Leerdoelen en vereisten
5. Extra leerbronnen gelinkt

### Naamgeving Codevoorbeelden

Formaat: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Les 1, MAF Python
- `14-sequential.ipynb` - Les 14, MAF geavanceerde patronen

### Speciale Mappen

- `translated_images/` - Gelokaliseerde afbeeldingen voor vertalingen
- `images/` - Originele afbeeldingen voor Engelse inhoud
- `.devcontainer/` - VS Code development container configuratie
- `.github/` - GitHub Actions workflows en templates

### Afhankelijkheden

Belangrijke pakketten uit `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol ondersteuning
- `azure-ai-inference`, `azure-ai-projects` - Azure AI diensten
- `azure-identity` - Azure authenticatie (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integratie
- `mcp[cli]` - Model Context Protocol ondersteuning

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel wij streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->