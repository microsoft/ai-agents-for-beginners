# AGENTS.md

## Projectoverzicht

Deze repository bevat "AI Agents voor Beginners" - een uitgebreide educatieve cursus die alles leert wat nodig is om AI Agents te bouwen. De cursus bestaat uit 15+ lessen die de basisprincipes, ontwerp patronen, frameworks en productie-implementatie van AI-agents behandelen.

**Belangrijkste Technologieën:**
- Python 3.12+
- Jupyter Notebooks voor interactief leren
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architectuur:**
- Les-gebaseerde structuur (00-15+ mappen)
- Elke les bevat: README-documentatie, codevoorbeelden (Jupyter notebooks) en afbeeldingen
- Meertalige ondersteuning via geautomatiseerd vertaalsysteem
- Eén Python-notebook per les met Microsoft Agent Framework

## Setup-commando's

### Vereisten
- Python 3.12 of hoger
- Azure-abonnement (voor Azure AI Foundry)
- Azure CLI geïnstalleerd en geverifieerd (`az login`)

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

3. **Installeer dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Stel omgevingsvariabelen in:**
   ```bash
   cp .env.example .env
   # Bewerk .env met uw API-sleutels en eindpunten
   ```

### Vereiste Omgevingsvariabelen

Voor **Azure AI Foundry** (Verplicht):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Naam van model deployment (bijv. gpt-4o)

Voor **Azure AI Search** (Les 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-sleutel

Authenticatie: Voer `az login` uit voordat je notebooks draait (gebruikt `AzureCliCredential`).

## Ontwikkelworkflow

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
- Gebruikt `AzureAIProjectAgentProvider` voor Agent Service V2 (agents zichtbaar in Foundry portal)
- Productieklaar met ingebouwde observability
- Bestandsformaat: `*-python-agent-framework.ipynb`

## Testinstructies

Dit is een educatieve repository met voorbeeldcode in plaats van productiesoftware met geautomatiseerde tests. Om je setup en wijzigingen te verifiëren:

### Handmatig Testen

1. **Test de Python-omgeving:**
   ```bash
   python --version  # Moet 3.12+ zijn
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook-uitvoering:**
   ```bash
   # Zet notebook om naar script en voer uit (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Controleer omgevingsvariabelen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Individuele Notebooks Draaien

Open notebooks in Jupyter en voer cellen achtereenvolgens uit. Elke notebook is zelfstandig en bevat:
- Import statements
- Configuratie laden
- Voorbeeld agent-implementaties
- Verwachte outputs in markdowncellen

## Code Stijl

### Python Conventies

- **Python Versie**: 3.12+
- **Code Stijl**: Volg de standaard Python PEP 8 conventies
- **Notebooks**: Gebruik duidelijke markdowncellen om concepten uit te leggen
- **Imports**: Groepeer standaardbibliotheek, third-party en lokale imports

### Jupyter Notebook Conventies

- Voeg beschrijvende markdowncellen toe voor codecellen
- Voeg outputvoorbeelden toe in notebooks ter referentie
- Gebruik duidelijke variabelenamen die bij de lesconcepten passen
- Houd de volgorde van notebook-uitvoering lineair (cel 1 → 2 → 3...)

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

## Bouw en Implementatie

### Documentatie bouwen

Deze repository gebruikt Markdown voor documentatie:
- README.md-bestanden in elke lesmap
- Hoofd README.md in de root van de repository
- Geautomatiseerd vertaalsysteem via GitHub Actions

### CI/CD Pipeline

Te vinden in `.github/workflows/`:

1. **co-op-translator.yml** - Automatische vertaling naar 50+ talen
2. **welcome-issue.yml** - Verwelkomt nieuwe issue aanmakers
3. **welcome-pr.yml** - Verwelkomt nieuwe pull request bijdragers

### Implementatie

Dit is een educatieve repository - geen implementatieproces. Gebruikers:
1. Forken of clonen de repository
2. Draaien notebooks lokaal of in GitHub Codespaces
3. Leren door voorbeelden te wijzigen en experimenteren

## Richtlijnen voor Pull Requests

### Voor het Indienen

1. **Test je wijzigingen:**
   - Draai getroffen notebooks volledig
   - Verifieer dat alle cellen zonder fouten uitvoeren
   - Controleer of outputs passend zijn

2. **Documentatie updates:**
   - Werk README.md bij bij nieuwe concepten
   - Voeg commentaar toe in notebooks bij complexe code
   - Zorg dat markdowncellen het doel uitleggen

3. **Bestandswijzigingen:**
   - Vermijd het committen van `.env`-bestanden (gebruik `.env.example`)
   - Commit geen `venv/` of `__pycache__/` mappen
   - Houd notebook outputs als ze concepten demonstreren
   - Verwijder tijdelijke bestanden en backup-notebooks (`*-backup.ipynb`)

### PR Titel Formaat

Gebruik beschrijvende titels:
- `[Lesson-XX] Nieuwe voorbeeld toegevoegd voor <concept>`
- `[Fix] Typfout gecorrigeerd in lesson-XX README`
- `[Update] Verbeter codevoorbeeld in lesson-XX`
- `[Docs] Setup instructies bijgewerkt`

### Vereiste Checks

- Notebooks moeten zonder fouten uitvoeren
- README-bestanden moeten duidelijk en accuraat zijn
- Volg bestaande codepatronen in de repository
- Houd consistentie met andere lessen

## Aanvullende Notities

### Veelvoorkomende Valkuilen

1. **Python versie mismatch:**
   - Zorg dat Python 3.12+ wordt gebruikt
   - Sommige pakketten werken niet met oudere versies
   - Gebruik `python3 -m venv` om expliciet Python-versie te specificeren

2. **Omgevingsvariabelen:**
   - Maak altijd `.env` aan vanaf `.env.example`
   - Commit het `.env`-bestand niet (staat in `.gitignore`)
   - GitHub-token moet juiste permissies hebben

3. **Pakketconflicten:**
   - Gebruik een verse virtuele omgeving
   - Installeer vanuit `requirements.txt` in plaats van losse pakketten
   - Sommige notebooks vereisen extra pakketten zoals vermeld in hun markdowncellen

4. **Azure-services:**
   - Azure AI-services vereisen een actief abonnement
   - Sommige features zijn regio-specifiek
   - Beperkingen van gratis tier zijn van toepassing op GitHub Models

### Leerpad

Aanbevolen volgorde van de lessen:
1. **00-course-setup** - Begin hier voor de environment setup
2. **01-intro-to-ai-agents** - Begrijp AI-agent fundamentals
3. **02-explore-agentic-frameworks** - Leer over verschillende frameworks
4. **03-agentic-design-patterns** - Kernontwerppatronen
5. Ga verder met de genummerde lessen op volgorde

### Framework Selectie

Kies framework op basis van je doelen:
- **Alle lessen**: Microsoft Agent Framework (MAF) met `AzureAIProjectAgentProvider`
- **Agents registreren server-side** in Azure AI Foundry Agent Service V2 en zijn zichtbaar in de Foundry portal

### Hulp Krijgen

- Word lid van de [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Bekijk de README-bestanden van de lessen voor specifieke aanwijzingen
- Check de hoofd-[README.md](./README.md) voor cursusoverzicht
- Raadpleeg [Course Setup](./00-course-setup/README.md) voor gedetailleerde setup-instructies

### Bijdragen

Dit is een open educatief project. Bijdragen zijn welkom:
- Verbeter codevoorbeelden
- Corrigeer typfouten of fouten
- Voeg verduidelijkende commentaren toe
- Stel nieuwe lesthema’s voor
- Vertaal naar extra talen

Zie [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) voor actuele behoeften.

## Projectspecifieke Context

### Meertalige Ondersteuning

Deze repository gebruikt een geautomatiseerd vertaalsysteem:
- 50+ talen ondersteund
- Vertalingen in `/translations/<lang-code>/` mappen
- GitHub Actions workflow regelt vertaalupdates
- Brondocumenten in het Engels in repository root

### Lesstructuur

Elke les volgt een consistent patroon:
1. Videominiatuur met link
2. Geschreven lesinhoud (README.md)
3. Codevoorbeelden in meerdere frameworks
4. Leerdoelen en vereisten
5. Extra leermaterialen gelinkt

### Naamgeving Codevoorbeelden

Formaat: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Les 1, MAF Python
- `14-sequential.ipynb` - Les 14, MAF geavanceerde patronen

### Speciale Mappen

- `translated_images/` - Gelokaliseerde afbeeldingen voor vertalingen
- `images/` - Originele afbeeldingen voor Engelse inhoud
- `.devcontainer/` - VS Code ontwikkelcontainer configuratie
- `.github/` - GitHub Actions workflows en templates

### Dependencies

Belangrijke pakketten uit `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol ondersteuning
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure authenticatie (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integratie
- `mcp[cli]` - Model Context Protocol ondersteuning

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->