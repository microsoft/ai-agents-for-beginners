# Yuuz Agentic Protocols (MCP, A2A and NLWeb)

[![Agentic Protocols](../../../translated_images/pcm/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik di image wey dey up dere to watch video for dis lesson)_

As people dey use AI agents grow, e mean say protocol wey go make e standard, secure, and support open innovation dey necessary. For dis lesson, we go talk 3 protocols wey dey try provide dis need - Model Context Protocol (MCP), Agent to Agent (A2A) and Natural Language Web (NLWeb).

## Introduction

For dis lesson, we go cover:

• How **MCP** dey allow AI Agents access external tools and data to fit complete user task dem.

• How **A2A** dey enable communication and collaboration among different AI agents.

• How **NLWeb** dey bring natural language interfaces for any website so AI Agents fit find and interact with di content.

## Learning Goals

• **Identify** di main purpose and benefits of MCP, A2A, and NLWeb for AI agents matter.

• **Explain** how each protocol dey help communication and interaction between LLMs, tools, and other agents.

• **Recognize** di different roles each protocol dey play for build complex agentic systems.

## Model Context Protocol

The **Model Context Protocol (MCP)** na open standard wey provide standardized way for applications to provide context and tools to LLMs. E dey allow one "universal adaptor" to connect to different data sources and tools wey AI Agents fit use consistently.

Make we check di parts of MCP, di benefits if we compare am with direct API use, plus example how AI agents fit use MCP server.

### MCP Core Components

MCP dey work with **client-server architecture** and e core parts na:

• **Hosts** na LLM applications (like code editor wey be VSCode) wey dey start connection to MCP Server.

• **Clients** na parts inside host application wey keep one-to-one connections with servers.

• **Servers** na lightweight programs wey dey show specific abilities.

For protocol, dem include three core primitives wey be di powers of MCP Server:

• **Tools**: These na separate actions or functions wey AI agent fit call to do action. For example, weather service fit show "get weather" tool or e-commerce server fit show "purchase product" tool. MCP servers go show tool name, description, and input/output schema for their capabilities list.

• **Resources**: Na read-only data or documents wey MCP server fit provide and clients fit request anytime. Examples na file contents, database records, or log files. Resources fit be text (like code or JSON) or binary (like images or PDFs).

• **Prompts**: Dem na predefined templates wey suggest prompts, allow for complex workflows.

### Benefits of MCP

MCP get big advantages for AI Agents:

• **Dynamic Tool Discovery**: Agents fit dynamically get list of tools wey server get plus description. This no be like old API wey need static coding for integration, so anytime API change, code go need update. MCP na "integrate once" way, e dey flexible.

• **Interoperability Across LLMs**: MCP fit work with different LLMs, so you fit change core models for better performance.

• **Standardized Security**: MCP get standard authentication way, e go easy to add access to more MCP servers. E simple pass to manage different keys and authentication types for normal APIs.

### MCP Example

![MCP Diagram](../../../translated_images/pcm/mcp-diagram.e4ca1cbd551444a1.webp)

Imagine say user wan book flight with AI assistant powered by MCP.

1. **Connection**: AI assistant (MCP client) connect to MCP server wey airline provide.

2. **Tool Discovery**: Client ask airline MCP server, "Which tools you get?" Server reply with tools like "search flights" and "book flights".

3. **Tool Invocation**: You ask AI assistant, "Make una search flight from Portland to Honolulu." AI assistant use LLM sabi say e need call "search flights" tool and send parameters (origin, destination) to MCP server.

4. **Execution and Response**: MCP server act as wrapper call airline booking API, get flight info (e.g., JSON data) then send am back to AI assistant.

5. **Further Interaction**: AI assistant show flight options. When you pick flight, e fit call "book flight" tool on same MCP server finish booking.

## Agent-to-Agent Protocol (A2A)

MCP dey connect LLMs to tools, but **Agent-to-Agent (A2A) protocol** take am further by allow communication and collaboration between different AI agents. A2A connect AI agents across organizations, environments and tech stacks to do shared task.

We go look components and benefits of A2A, plus example how e fit work for our travel app.

### A2A Core Components

A2A focus on communication among agents and make dem work together to finish user subtask. Every part for protocol help do dis:

#### Agent Card

Like MCP server dey share tools list, Agent Card get:
- Agent Name.
- **description of the general tasks** wey e dey do.
- **list of specific skills** plus description to help other agents or people know when to call that agent.
- **current Endpoint URL** of agent
- **version** and **capabilities** like streaming response and push notification.

#### Agent Executor

Agent Executor dey pass user chat context to remote agent, cause remote agent need am to understand task. For A2A server, agent use im own Large Language Model (LLM) to parse requests and do tasks with im own tools.

#### Artifact

After remote agent finish task, im create artifact. Artifact get result of work, description of wetin e do, and text context wey protocol pass. After artifact send, connection close till e needed again.

#### Event Queue

Dis part dey handle updates and pass messages. E important for agentic production system so connection no close before task finish, especially when task fit take time.

### Benefits of A2A

• **Enhanced Collaboration**: E allow agents from different vendors and platform to interact, share context, and work together, automate smoothly across systems wey no connect before.

• **Model Selection Flexibility**: Every A2A agent fit choose which LLM e go use do im work, so agents fit get optimized or tuned models, no be like MCP wey fit dey only one LLM connection.

• **Built-in Authentication**: Authentication dey in-built for A2A protocol, give strong security for interaction among agents.

### A2A Example

![A2A Diagram](../../../translated_images/pcm/A2A-Diagram.8666928d648acc26.webp)

Make we expand our travel booking story, but this time with A2A.

1. **User Request to Multi-Agent**: User talk to "Travel Agent" A2A client/agent, maybe say, "Book entire trip to Honolulu for next week, including flight, hotel, and rental car".

2. **Orchestration by Travel Agent**: Travel Agent catch dis complex request. E use LLM reason the task and find say e need connect to other special agents.

3. **Inter-Agent Communication**: Travel Agent use A2A protocol connect to downstream agents like "Airline Agent", "Hotel Agent" and "Car Rental Agent" wey different companies create.

4. **Delegated Task Execution**: Travel Agent send specific tasks to these specialized agents (e.g., "Find flights to Honolulu," "Book hotel," "Rent car"). Each agent use their LLM and tools (fit be MCP servers) do im part of booking.

5. **Consolidated Response**: When all downstream agents finish, Travel Agent collect results (flight info, hotel confirmation, car rental) then send full chat-style reply to user.

## Natural Language Web (NLWeb)

Websites don be main way for people to get info and data for internet.

Make we check di parts of NLWeb, benefits of NLWeb and example how our NLWeb work by looking our travel app.

### Components of NLWeb

- **NLWeb Application (Core Service Code)**: Na system wey process natural language questions. E connect parts of platform to create responses. You fit think am as **engine wey power natural language feature** of website.

- **NLWeb Protocol**: Na **basic rules for natural language interaction** with website. E return responses in JSON (often use Schema.org). Di idea na to create simple foundation for “AI Web,” just like HTML make e easy to share documents online.

- **MCP Server (Model Context Protocol Endpoint)**: Every NLWeb setup still dey function as **MCP server**. Dis one mean e fit **share tools (like “ask” method) and data** with other AI systems. For practice, e make website content and ability usable by AI agents, make website part of bigger “agent ecosystem.”

- **Embedding Models**: These models dey use to **convert website content into numerical vectors (embeddings)**. Dis vectors carry meaning in way computers fit compare and search. Dem store am in special database, and users fit choose which embedding model dem go use.

- **Vector Database (Retrieval Mechanism)**: Dis database **store website content embedding**. When person ask question, NLWeb go check vector database to quickly find best info. E give fast list of possibles, rank am by similarity. NLWeb fit work with Qdrant, Snowflake, Milvus, Azure AI Search, Elasticsearch and others.

### NLWeb by Example

![NLWeb](../../../translated_images/pcm/nlweb-diagram.c1e2390b310e5fe4.webp)

Think about our travel booking website again, but now, e powered by NLWeb.

1. **Data Ingestion**: Di travel website product catalogs (like flight listings, hotel descriptions, tour packages) format with Schema.org or load through RSS feeds. NLWeb tools take in di structured data, create embeddings, and store for local or remote vector database.

2. **Natural Language Query (Human)**: User come website, instead of search with menu, e type for chat interface: "Find me family-friendly hotel for Honolulu with pool for next week".

3. **NLWeb Processing**: NLWeb app receive dis query. E send am to LLM to understand and at same time check vector database for hotel listings wey relate.

4. **Accurate Results**: LLM help check search result from database, find best match base on "family-friendly," "pool," "Honolulu," then e format natural language response. Important thing be say response refer to actual hotels for website catalog, no fake info.

5. **AI Agent Interaction**: Because NLWeb na MCP server, external AI travel agent fit connect to website NLWeb instance. AI agent fit use `ask` MCP method to query website like: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. NLWeb go process am, use restaurant info database (if loaded), then return structured JSON response.

### Get More Questions about MCP/A2A/NLWeb?

Join [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, attend office hours and get answers for your AI Agents questions.

## Resources

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Previous Lesson

[AI Agents in Production](../10-ai-agents-production/README.md)

## Next Lesson

[Context Engineering for AI Agents](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->