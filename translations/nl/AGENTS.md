# AGENTS.md

## Projectoverzicht

Deze repository bevat "AI Agents voor Beginners" - een uitgebreide educatieve cursus die alles leert wat nodig is om AI Agents te bouwen. De cursus bestaat uit 18 lessen die de basisprincipes, ontwerp patronen, frameworks en productie-implementatie van AI-agents behandelen.

**Belangrijke technologieën:**
- Python 3.12+
- Jupyter Notebooks voor interactief leren
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI-services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architectuur:**
- Les-gebaseerde structuur (00-15+ mappen)
- Elke les bevat: README-documentatie, codevoorbeelden (Jupyter notebooks) en afbeeldingen
- Meertalige ondersteuning via geautomatiseerd vertaalsysteem
- Eén Python-notebook per les met Microsoft Agent Framework

## Setup Commando's

### Vereisten
- Python 3.12 of hoger
- Azure-abonnement (voor Microsoft Foundry)
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

3. **Installeer de afhankelijkheden:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Stel omgevingsvariabelen in:**
   ```bash
   cp .env.example .env
   # Bewerk .env met uw API-sleutels en eindpunten
   ```

### Benodigde Omgevingsvariabelen

Voor **Microsoft Foundry** (Vereist):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Naam van model-implementatie (bijv. gpt-4o)

Voor **Azure AI Search** (Les 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API sleutel

Authenticatie: Voer `az login` uit voordat je de notebooks draait (gebruikt `AzureCliCredential`).

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

**Microsoft Agent Framework + Microsoft Foundry:**
- Vereist Azure-abonnement
- Gebruikt `FoundryChatClient` voor Agent Service V2 (agents zichtbaar in Foundry-portal)
- Productieklaar met ingebouwde observeerbaarheid
- Bestands patroon: `*-python-agent-framework.ipynb`

## Testinstructies

Dit is een educatieve repository met voorbeeldcode in plaats van productcode met geautomatiseerde tests. Om je setup en wijzigingen te verifiëren:

### Handmatig testen

1. **Test de Python-omgeving:**
   ```bash
   python --version  # Moet 3.12+ zijn
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook-uitvoering:**
   ```bash
   # Converteer notebook naar script en voer uit (test import)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifieer omgevingsvariabelen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Individuele notebooks draaien

Open notebooks in Jupyter en voer cellen sequentieel uit. Elke notebook is zelfvoorzienend en bevat:
- Import statements
- Configuratie laden
- Voorbeeld agent-implementaties
- Verwachte outputs in markdown cellen

## Code Stijl

### Python-conventies

- **Python-versie**: 3.12+
- **Code stijl**: Volg standaard Python PEP 8 conventies
- **Notebooks**: Gebruik duidelijke markdown cellen voor uitleg van concepten
- **Imports**: Groepeer op standaardbibliotheek, derde partij en lokale imports

### Jupyter Notebook-conventies

- Voeg beschrijvende markdown cellen toe voor codecellen
- Voeg uitvoervoorbeelden toe in notebooks als referentie
- Gebruik duidelijke variabelenamen die overeenkomen met lesconcepten
- Houd de uitvoeringsvolgorde van notebooks lineair (cel 1 → 2 → 3...)

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

## Bouw en Deployment

### Documentatie bouwen

Deze repository gebruikt Markdown voor documentatie:
- README.md-bestanden in elke lesmap
- Hoofd README.md in de hoofdmap van de repository
- Geautomatiseerd vertaalsysteem via GitHub Actions

### CI/CD Pipeline

Gelegen in `.github/workflows/`:

1. **co-op-translator.yml** - Automatische vertaling naar 50+ talen
2. **welcome-issue.yml** - Verwelkomt nieuwe issue makers
3. **welcome-pr.yml** - Verwelkomt nieuwe pull request bijdragers

### Deployment

Dit is een educatieve repository - er is geen deployment proces. Gebruikers:
1. Forken of clonen de repository
2. Runnen notebooks lokaal of in GitHub Codespaces
3. Leren door voorbeelden te wijzigen en mee te experimenteren

## Richtlijnen voor Pull Requests

### Voor het indienen

1. **Test je wijzigingen:**
   - Voer de betreffende notebooks helemaal uit
   - Controleer dat alle cellen uitgevoerd worden zonder fouten
   - Controleer dat uitvoer passend is

2. **Documentatie-updates:**
   - Werk README.md bij als er nieuwe concepten bijkomen
   - Voeg commentaar toe in notebooks bij complexe code
   - Zorg dat markdown cellen het doel uitleggen

3. **Bestandswijzigingen:**
   - Vermijd het committen van `.env`-bestanden (gebruik `.env.example`)
   - Commit geen `venv/` of `__pycache__/` mappen
   - Behoud notebook-uitvoer als die concepten aantoont
   - Verwijder tijdelijke bestanden en backup notebooks (`*-backup.ipynb`)

### PR Titelformaat

Gebruik beschrijvende titels:
- `[Lesson-XX] Voeg nieuw voorbeeld toe voor <concept>`
- `[Fix] Corrigeer typefout in lesson-XX README`
- `[Update] Verbeter codevoorbeeld in lesson-XX`
- `[Docs] Update setup-instructies`

### Verplichte controles

- Notebooks moeten foutloos uitvoeren
- README-bestanden moeten duidelijk en accuraat zijn
- Volg bestaande codepatronen in de repository
- Zorg voor consistentie met andere lessen

## Aanvullende Aantekeningen

### Veelvoorkomende valkuilen

1. **Python versie niet overeenkomend:**
   - Zorg dat Python 3.12+ wordt gebruikt
   - Sommige pakketten werken mogelijk niet met oudere versies
   - Gebruik `python3 -m venv` om Python-versie expliciet te specificeren

2. **Omgevingsvariabelen:**
   - Maak altijd `.env` aan vanuit `.env.example`
   - Commit het `.env` bestand niet (staat in `.gitignore`)
   - Log in met `az login` voor sleutelvrije Entra ID-authenticatie

3. **Pakketconflicten:**
   - Gebruik een verse virtuele omgeving
   - Installeer via `requirements.txt` in plaats van afzonderlijke pakketten
   - Sommige notebooks hebben extra pakketten nodig die vermeld staan in hun markdown cellen

4. **Azure-services:**
   - Azure AI-services vereisen een actief abonnement
   - Sommige functies zijn regio-specifiek
   - Zorg dat je Azure OpenAI model-implementatie de Responses API ondersteunt

### Leerroute

Aanbevolen volgorde voor lessen:
1. **00-course-setup** - Begin hier voor de omgeving setup
2. **01-intro-to-ai-agents** - Begrijp fundamentele AI-agentconcepten
3. **02-explore-agentic-frameworks** - Leer over verschillende frameworks
4. **03-agentic-design-patterns** - Kernontwerppatronen
5. Ga door met de genummerde lessen in volgorde

### Framework selectie

Kies het framework op basis van je doelen:
- **Alle lessen**: Microsoft Agent Framework (MAF) met `FoundryChatClient`
- **Agents registreren server-side** in Microsoft Foundry Agent Service V2 en zijn zichtbaar in de Foundry-portal

### Hulp krijgen

- Word lid van de [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Bekijk de README-bestanden van de lessen voor specifieke richtlijnen
- Check de hoofd [README.md](./README.md) voor cursusoverzicht
- Raadpleeg [Course Setup](./00-course-setup/README.md) voor gedetailleerde setup-instructies

### Bijdragen

Dit is een open educatief project. Bijdragen zijn welkom:
- Verbeter codevoorbeelden
- Corrigeer typefouten of fouten
- Voeg verduidelijkende opmerkingen toe
- Stel nieuwe lesonderwerpen voor
- Vertaal naar extra talen

Zie [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) voor huidige behoeften.

## Project-specifieke context

### Meertalige ondersteuning

Deze repository gebruikt een geautomatiseerd vertaalsysteem:
- 50+ talen ondersteund
- Vertalingen in `/translations/<lang-code>/` mappen
- GitHub Actions workflow beheert vertalingsupdates
- Brondocumenten zijn in het Engels in de hoofdmap van de repository

### Lesstructuur

Elke les volgt een consistent patroon:
1. Video thumbnail met link
2. Geschreven lesinhoud (README.md)
3. Codevoorbeelden in meerdere frameworks
4. Leerdoelen en vereisten
5. Extra leerbronnen gelinkt

### Naamgeving van codevoorbeelden

Formaat: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Les 1, MAF Python
- `14-sequential.ipynb` - Les 14, MAF geavanceerde patronen

### Speciale mappen

- `translated_images/` - Gelokaliseerde afbeeldingen voor vertalingen
- `images/` - Originele afbeeldingen voor Engelse inhoud
- `.devcontainer/` - VS Code ontwikkelingscontainer configuratie
- `.github/` - GitHub Actions workflows en sjablonen

### Afhankelijkheden

Belangrijke pakketten uit `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Ondersteuning voor Agent-to-Agent protocol
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-diensten
- `azure-identity` - Azure authenticatie (AzureCliCredential)
- `azure-search-documents` - Azure AI Search-integratie
- `mcp[cli]` - Model Context Protocol ondersteuning

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->