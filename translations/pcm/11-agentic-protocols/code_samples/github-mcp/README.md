# Github MCP Server Example

## Description

Na demo wey dem create for the AI Agents Hackathon wey Microsoft Reactor host.

Dem dey use the tools to recommend hackathon projects based on wetin user Github repos show. Dem dey do am like this:

1. **Github Agent** - Dey use the Github MCP Server to fetch repos and information about those repos.
2. **Hackathon Agent** - E go carry the data wey Github Agent bring come come up with creative hackathon project ideas based on the projects, the languages wey the user use and the project tracks for the AI Agents hackathon.
3. **Events Agent** - Based on wetin the hackathon agent suggest, the events agent go recommend relevant events from the AI Agent Hackathon series.

## Running the code 

### Environment Variables

Dis demo dey use Microsoft Agent Framework, Azure OpenAI Service, the Github MCP Server and Azure AI Search.

Make sure say you don set the correct environment variables to fit use these tools:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

To connect to the MCP server, dis demo dey use Chainlit as the chat interface. 

If you wan run the server, use this command for your terminal:

```bash
chainlit run app.py -w
```

Dis one go start your Chainlit server for `localhost:8000` and e go also populate your Azure AI Search Index with the `event-descriptions.md` content. 

## Connecting to the MCP Server

To connect to the Github MCP Server, select the "plug" icon underneath the "Type your message here.." chat box:

![MCP Konnekt](../../../../../translated_images/pcm/mcp-chainlit-1.7ed66d648e3cfb28.webp)

From there you fit click on the "Connect an MCP" to add the command wey go connect to the Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Change "[YOUR PERSONAL ACCESS TOKEN]" to your real Personal Access Token. 

After you connect, you suppose see a (1) next to the plug icon to show say e don connect. If e no show, try restart the chainlit server with `chainlit run app.py -w`.

## Using the Demo 

To start the agent workflow wey dey recommend hackathon projects, you fit type message like: 

"Recommend hackathon projects for the Github user koreyspace"

The Router Agent go analyze your request and decide which combination of agents (GitHub, Hackathon, and Events) fit handle your query best. The agents go work together to give better recommendations based on GitHub repository analysis, project ideation, and relevant tech events.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Abeg note: Dis document na AI don translate wit the Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make everything correct, abeg sabi say automated translations fit get errors or no too correct. The original document for im original language na di authoritative source wey you suppose rely on. If na important information, e better make professional human translator do am. We no dey responsible for any misunderstanding or wrong interpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->