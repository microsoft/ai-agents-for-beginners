<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T11:54:25+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "en"
}
-->
# Lesson 11: Model Context Protocol (MCP) Integration

## Introduction to Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an advanced framework designed to standardize how AI models interact with client applications. MCP acts as a bridge between AI models and the applications that utilize them, offering a consistent interface regardless of the specific model implementation.

Key features of MCP:

- **Standardized Communication**: MCP defines a common language for applications to interact with AI models.
- **Improved Context Management**: Facilitates efficient transfer of contextual information to AI models.
- **Cross-platform Compatibility**: Supports multiple programming languages, including C#, Java, JavaScript, Python, and TypeScript.
- **Easy Integration**: Simplifies the process of incorporating various AI models into applications.

MCP is especially useful in the development of AI agents, as it enables them to interact with diverse systems and data sources through a unified protocol, making the agents more adaptable and capable.

## Learning Objectives
- Understand what MCP is and its importance in AI agent development.
- Set up and configure an MCP server for GitHub integration.
- Create a multi-agent system using MCP tools.
- Implement RAG (Retrieval Augmented Generation) with Azure Cognitive Search.

## Prerequisites
- Python 3.8+
- Node.js 14+
- Azure subscription
- GitHub account
- Basic knowledge of Semantic Kernel

## Setup Instructions

1. **Environment Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure Azure Services**
   - Create an Azure Cognitive Search resource.
   - Set up the Azure OpenAI service.
   - Configure environment variables in the `.env` file.

3. **MCP Server Setup**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Project Structure

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Core Components

### 1. Multi-Agent System
- GitHub Agent: Analyzes repositories.
- Hackathon Agent: Provides project recommendations.
- Events Agent: Suggests tech events.

### 2. Azure Integration
- Cognitive Search for indexing events.
- Azure OpenAI for agent intelligence.
- RAG pattern implementation.

### 3. MCP Tools
- Analyzing GitHub repositories.
- Inspecting code.
- Extracting metadata.

## Code Walkthrough

The sample demonstrates:
1. Integration of the MCP server.
2. Orchestration of multiple agents.
3. Integration with Azure Cognitive Search.
4. Implementation of the RAG pattern.

Key features:
- Real-time analysis of GitHub repositories.
- Intelligent project recommendations.
- Event matching using Azure Search.
- Streaming responses with Chainlit.

## Running the Sample

For detailed setup instructions and additional information, refer to the [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Start the MCP server:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Launch the application:
   ```bash
   chainlit run app.py -w
   ```

3. Test the integration:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Troubleshooting

Common issues and their solutions:
1. MCP Connection Issues
   - Ensure the server is running.
   - Check if the port is available.
   - Verify GitHub tokens.

2. Azure Search Issues
   - Confirm connection strings are correct.
   - Check if the index exists.
   - Verify document uploads.

## Next Steps
- Explore additional MCP tools.
- Develop custom agents.
- Enhance RAG capabilities.
- Add more event sources.
- **Advanced**: Check out [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) for examples of agent-to-agent communication.

## Resources
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.