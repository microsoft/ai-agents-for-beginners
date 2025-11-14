<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T14:50:12+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "en"
}
-->
# Github MCP Server Example

## Description

This is a demo created for the AI Agents Hackathon hosted by Microsoft Reactor.

The tool is designed to recommend hackathon projects based on a user's Github repositories. It works as follows:

1. **Github Agent** - Uses the Github MCP Server to retrieve repositories and gather information about them.
2. **Hackathon Agent** - Processes the data from the Github Agent to generate creative hackathon project ideas based on the user's projects, programming languages, and the project tracks for the AI Agents Hackathon.
3. **Events Agent** - Based on the suggestions from the Hackathon Agent, the Events Agent recommends relevant events from the AI Agents Hackathon series.

## Running the code 

### Environment Variables

This demo utilizes Azure Open AI Service, Semantic Kernel, the Github MCP Server, and Azure AI Search.

Ensure that the appropriate environment variables are set to use these tools:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

To connect to the MCP server, this demo uses Chainlit as a chat interface.

To start the server, run the following command in your terminal:

```bash
chainlit run app.py -w
```

This will launch your Chainlit server on `localhost:8000` and populate your Azure AI Search Index with the content from `event-descriptions.md`.

## Connecting to the MCP Server

To connect to the Github MCP Server, click the "plug" icon below the "Type your message here..." chat box:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.en.png)

From there, click "Connect an MCP" to add the command for connecting to the Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token.

Once connected, you should see a (1) next to the plug icon, indicating a successful connection. If not, try restarting the Chainlit server using `chainlit run app.py -w`.

## Using the Demo 

To initiate the agent workflow for recommending hackathon projects, you can type a message like:

"Recommend hackathon projects for the Github user koreyspace"

The Router Agent will evaluate your request and determine the best combination of agents (GitHub, Hackathon, and Events) to handle your query. These agents collaborate to provide detailed recommendations based on GitHub repository analysis, project ideation, and relevant tech events.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.