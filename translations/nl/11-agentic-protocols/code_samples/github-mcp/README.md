# Github MCP Server Voorbeeld

## Beschrijving

Dit was een demo gemaakt voor de AI Agents Hackathon georganiseerd via de Microsoft Reactor.

De tool wordt gebruikt om hackathonprojecten aan te bevelen op basis van iemands Github repos.
Dit wordt gedaan door:

1. **Github Agent** - Maakt gebruik van de Github MCP Server om repos en informatie over die repos op te halen.
2. **Hackathon Agent** - Neemt de gegevens van de Github Agent en bedenkt creatieve hackathonprojectideeën op basis van de projecten, de door de gebruiker gebruikte talen en de projecttracks van de AI Agents-hackathon.
3. **Events Agent** - Op basis van de suggesties van de Hackathon Agent zal de Events Agent relevante evenementen uit de AI Agent Hackathon-serie aanbevelen.
## De code uitvoeren 

### Omgevingsvariabelen

Deze demo gebruikt Microsoft Agent Framework, Azure OpenAI Service, de Github MCP Server en Azure AI Search.

Zorg ervoor dat u de juiste omgevingsvariabelen hebt ingesteld om deze tools te gebruiken:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## De Chainlit-server uitvoeren

Om verbinding te maken met de MCP-server gebruikt deze demo Chainlit als chatinterface. 

Om de server te starten, gebruik de volgende opdracht in uw terminal:

```bash
chainlit run app.py -w
```

Dit zou uw Chainlit-server op `localhost:8000` moeten starten en tevens uw Azure AI Search Index vullen met de inhoud van `event-descriptions.md`. 

## Verbinden met de MCP-server

Om verbinding te maken met de Github MCP Server, selecteer het pictogram "plug" onder het chatvak "Type your message here..":

![MCP Verbinden](../../../../../translated_images/nl/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Vanaf daar kunt u op "Connect an MCP" klikken om de opdracht toe te voegen om verbinding te maken met de Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Vervang "[YOUR PERSONAL ACCESS TOKEN]" door uw daadwerkelijke Personal Access Token. 

Na het verbinden zou u een (1) naast het plug-pictogram moeten zien om te bevestigen dat het verbonden is. Als dat niet het geval is, probeer de chainlit-server te herstarten met `chainlit run app.py -w`.

## De demo gebruiken 

Om de agent-workflow te starten voor het aanbevelen van hackathonprojecten, kunt u een bericht typen zoals: 

"Recommend hackathon projects for the Github user koreyspace"

De Router Agent zal uw verzoek analyseren en bepalen welke combinatie van agents (GitHub, Hackathon en Events) het meest geschikt is om uw vraag af te handelen. De agents werken samen om uitgebreide aanbevelingen te geven op basis van GitHub-repositoryanalyse, projectideevorming en relevante techevenementen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vrijwaring**:
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->