# Copyright (c) Microsoft. All rights reserved.

"""
Sample: Host a LangChain / LangGraph agent as a Microsoft Foundry hosted agent.

This sample shows how to take an agent built with LangGraph and expose it through
the Microsoft Foundry hosted-agent **Responses** protocol using the
`langchain_azure_ai.agents.hosting` package. Foundry then manages the runtime,
sessions, scaling, identity, and protocol endpoints while your agent logic stays
in LangGraph.

The Responses API is the recommended API for agent-style development in Foundry:
it provides OpenAI-compatible chat, streaming, response history, and conversation
threading in a single API surface.

Prerequisites
-------------
- An Azure subscription and a Microsoft Foundry project.
- A deployed chat model that supports the Responses API (e.g. gpt-5-mini or gpt-5-nano).
- Python 3.10+ and the Azure CLI signed in (`az login`).
- Install the hosting extra:
      pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
- Set environment variables:
      FOUNDRY_PROJECT_ENDPOINT=https://<resource>.services.ai.azure.com/api/projects/<project>
      FOUNDRY_MODEL_NAME=gpt-5-mini

Run locally
-----------
    python 14-langchain-hosted-agent.py

Then send a Responses request to the local server:
    curl -sS -H "Content-Type: application/json" \
      -X POST http://localhost:8088/responses \
      -d '{"input":"Give me one tip for testing hosted agents.","stream":false}'

Deploy to Foundry (Azure Developer CLI)
---------------------------------------
    azd ext install azure.ai.agents
    azd auth login
    azd ai agent init -m <sample-manifest-url>
    azd ai agent run          # runs the container locally (requires Docker)
    azd provision             # if a new Foundry project/model is needed
    azd deploy                # packages + rolls out to the Foundry hosted runtime

See: https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents
"""

import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

# Scope used to request tokens for the Foundry project's OpenAI-compatible endpoint.
_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    """Create a ChatOpenAI bound to the Foundry project's Responses endpoint."""
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")

    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)

    # The project's OpenAI-compatible client exposes the Responses-capable base URL.
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    # A minimal LangGraph agent. Add your own tools to the list to give it capabilities.
    graph = create_agent(build_chat_model(), tools=[])

    # ResponsesHostServer exposes the compiled graph over POST /responses and emits
    # Responses API server-sent events (response.created, response.output_text.delta,
    # response.completed) when a request sets "stream": true.
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
