# Github MCP Server Ukázka

## Popis

Toto byla ukázka vytvořená pro AI Agents Hackathon pořádaný prostřednictvím Microsoft Reactor.

The tools is used to recommend hackathon projects based on a user's Github repos.
This is done by:

1. **Github Agent** - Používá Github MCP Server k získávání repozitářů a informací o těchto repozitářích.
2. **Hackathon Agent** - Bere data od Github Agenta a vymýšlí kreativní nápady na hackathon projekty na základě projektů, jazyků používaných uživatelem a tématických okruhů pro AI Agents hackathon.
3. **Events Agent** - Na základě návrhů Hackathon Agenta Events Agent doporučí relevantní události ze série AI Agent Hackathon.
## Running the code 

### Environment Variables

This demo uses Microsoft Agent Framework, Azure OpenAI Service, the Github MCP Server and Azure AI Search.

Make sure that you have the proper environment variables set to use these tools:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

To connect to the MCP server, this demo use Chainlit as a chat interface. 

To run the server, use the following command in your terminal:

```bash
chainlit run app.py -w
```

This should start your Chainlit server on `localhost:8000` as well as populate your Azure AI Search Index with the `event-descriptions.md` content. 

## Connecting to the MCP Server

To connect to the Github MCP Server, select the "plug" icon underneath the "Type your message here.." chat box:

![Připojení MCP](../../../../../translated_images/cs/mcp-chainlit-1.7ed66d648e3cfb28.webp)

From there you can click on the "Connect an MCP" to add the command to connect to the Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

After connecting, you should see a (1) next to the plug icon to confirm that its connected. If not, try restarting the chainlit server with `chainlit run app.py -w`.

## Using the Demo 

To start the agent workflow of recommending hackathon projects, you can type a message like: 

"Doporučte projekty na hackathon pro uživatele Github koreyspace"

The Router Agent will analyze your request and determine which combination of agents (GitHub, Hackathon, and Events) is best suited to handle your query. The agents work together to provide comprehensive recommendations based on GitHub repository analysis, project ideation, and relevant tech events.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Prohlášení o vyloučení odpovědnosti:
Tento dokument byl přeložen pomocí služby pro překlad využívající umělou inteligenci [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, berte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za rozhodující zdroj. U kritických informací doporučujeme využít profesionální lidský překlad. Nejsme odpovědní za žádná nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->