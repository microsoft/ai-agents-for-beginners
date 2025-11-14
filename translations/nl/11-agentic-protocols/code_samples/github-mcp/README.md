<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T18:33:23+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "nl"
}
-->
# Github MCP Server Voorbeeld

## Beschrijving

Dit is een demo die is gemaakt voor de AI Agents Hackathon, georganiseerd door Microsoft Reactor.

De tool wordt gebruikt om hackathonprojecten aan te bevelen op basis van de Github-repositories van een gebruiker. Dit gebeurt door:

1. **Github Agent** - Het gebruik van de Github MCP Server om repositories en informatie over die repositories op te halen.
2. **Hackathon Agent** - Neemt de gegevens van de Github Agent en bedenkt creatieve ideeën voor hackathonprojecten op basis van de projecten, gebruikte programmeertalen door de gebruiker en de projecttracks van de AI Agents Hackathon.
3. **Events Agent** - Op basis van de suggesties van de Hackathon Agent zal de Events Agent relevante evenementen uit de AI Agents Hackathon-serie aanbevelen.

## Code uitvoeren 

### Omgevingsvariabelen

Deze demo maakt gebruik van Azure Open AI Service, Semantic Kernel, de Github MCP Server en Azure AI Search.

Zorg ervoor dat je de juiste omgevingsvariabelen hebt ingesteld om deze tools te gebruiken:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## De Chainlit Server starten

Om verbinding te maken met de MCP Server, gebruikt deze demo Chainlit als chatinterface.

Om de server te starten, gebruik je het volgende commando in je terminal:

```bash
chainlit run app.py -w
```

Dit zou je Chainlit-server moeten starten op `localhost:8000` en je Azure AI Search Index vullen met de inhoud van `event-descriptions.md`.

## Verbinden met de MCP Server

Om verbinding te maken met de Github MCP Server, selecteer je het "stekker"-icoon onder het chatvak "Typ hier je bericht...":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.nl.png)

Van daaruit kun je klikken op "Connect an MCP" om het commando toe te voegen om verbinding te maken met de Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Vervang "[YOUR PERSONAL ACCESS TOKEN]" door je eigen Personal Access Token.

Na het verbinden zou je een (1) naast het stekker-icoon moeten zien om te bevestigen dat de verbinding is gemaakt. Zo niet, probeer dan de Chainlit-server opnieuw te starten met `chainlit run app.py -w`.

## De demo gebruiken 

Om het agent-workflowproces te starten voor het aanbevelen van hackathonprojecten, kun je een bericht typen zoals:

"Beveel hackathonprojecten aan voor de Github-gebruiker koreyspace"

De Router Agent zal je verzoek analyseren en bepalen welke combinatie van agents (GitHub, Hackathon en Events) het meest geschikt is om je vraag te behandelen. De agents werken samen om uitgebreide aanbevelingen te geven op basis van de analyse van Github-repositories, projectideeën en relevante technische evenementen.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.