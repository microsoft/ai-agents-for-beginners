# Github MCP Server Príklad

## Popis

Toto bolo demo vytvorené pre AI Agents Hackathon, ktorý organizoval Microsoft Reactor.

Nástroj sa používa na odporúčanie hackathonových projektov na základe Github repozitárov používateľa.
To sa robí takto:

1. **Github Agent** - Používa Github MCP Server na získanie repozitárov a informácií o týchto repozitároch.
2. **Hackathon Agent** - Berie údaje od Github Agenta a prichádza s kreatívnymi nápadmi na hackathonové projekty na základe projektov, jazykov, ktoré používateľ používa, a tém projektov pre AI Agents hackathon.
3. **Events Agent** - Na základe návrhov Hackathon Agenta odporučí Events Agent relevantné podujatia zo série AI Agent Hackathon.
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

Na pripojenie k Github MCP Serveru vyberte ikonu "plug" pod chatovacím políčkom "Type your message here..":

![Pripojenie MCP](../../../../../translated_images/sk/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Odtiaľ môžete kliknúť na tlačidlo "Connect an MCP" na pridanie príkazu na pripojenie k Github MCP Serveru:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

After connecting, you should see a (1) next to the plug icon to confirm that its connected. If not, try restarting the chainlit server with `chainlit run app.py -w`.

## Using the Demo 

To start the agent workflow of recommending hackathon projects, you can type a message like: 

"Recommend hackathon projects for the Github user koreyspace"

The Router Agent will analyze your request and determine which combination of agents (GitHub, Hackathon, and Events) is best suited to handle your query. The agents work together to provide comprehensive recommendations based on GitHub repository analysis, project ideation, and relevant tech events.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vylúčenie zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->