# Using Agentic Protocols (MCP, A2A and NLWeb)

[![Agentic Protocols](../../../translated_images/pcm/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Click di image wey dey up to watch dis lesson video)_

As AI agents dey increase, na so protocol wey go make everything standard, secure, and support open innovation dey important. For dis lesson, we go talk about 3 protocols wey wan fulfill dis need - Model Context Protocol (MCP), Agent to Agent (A2A) and Natural Language Web (NLWeb).

## Introduction

For dis lesson, we go cover:

• How **MCP** dey help AI Agents access external tools and data dem need to finish user task dem.

• How **A2A** dey enable communication and cooperation between different AI agents.

• How **NLWeb** dey bring natural language interface to any website wey AI Agents fit find and interact with di content.

## Learning Goals

• **Identify** di main purpose and benefit of MCP, A2A, and NLWeb for AI agents context.

• **Explain** how each protocol dey help communication and interaction between LLMs, tools, and other agents.

• **Recognize** di different role wey each protocol get for building complex agentic systems.

## Model Context Protocol

Di **Model Context Protocol (MCP)** na open standard wey provide one standard way for apps to give context and tools to LLMs. E dey make "universal adaptor" possible so AI Agents fit connect to different data sources and tools in one consistent way.

Make we check di parts wey dey MCP, di benefits compared to direct API use, and example how AI agents fit use MCP server.

### MCP Core Components

MCP dey run on **client-server architecture** and di main components be:

• **Hosts** na LLM apps (example na code editor like VSCode) wey dey start connection to MCP Server.

• **Clients** na part inside di host app wey maintain one-to-one connection with servers.

• **Servers** na lightweight programs wey dey show specific capabilities.

Inside di protocol, three core primitives dey, and na dem be capabilities of MCP Server:

• **Tools**: Dem be specific actions or functions wey AI agent fit call to perform action. For example, weather service fit get "get weather" tool, or e-commerce server fit get "purchase product" tool. MCP servers go tell every tool name, description, and input/output schema for their capabilities list.

• **Resources**: Dem be read-only data or documents wey MCP server fit provide, and clients fit collect dem anytime dem want. Example na file contents, database records, or log files. Resources fit be text (like code or JSON) or binary (like images or PDFs).

• **Prompts**: Dem be ready-made templates wey suggest prompts to allow more complex workflow.

### Benefits of MCP

MCP get big advantages for AI Agents:

• **Dynamic Tool Discovery**: Agents fit dynamically get list of tools wey server get with description of wetin dem do. This different from traditional APIs wey usually need static coding for integration, meaning if API change, code must update. MCP na "integrate once" style, so e dey more flexible.

• **Interoperability Across LLMs**: MCP fit work with different LLMs, e give flexibility to change core models to find better performance.

• **Standardized Security**: MCP get standard authentication way, e make am easier to scale when you dey add access to more MCP servers. E simpler than managing different keys and authentication kinds for many traditional APIs.

### MCP Example

![MCP Diagram](../../../translated_images/pcm/mcp-diagram.e4ca1cbd551444a1.webp)

Imagine say user wan book flight with AI assistant wey MCP power.

1. **Connection**: AI assistant (MCP client) connect to MCP server wey airline provide.

2. **Tool Discovery**: Client ask airline MCP server, "Which tool una get?" Server go answer with tools like "search flights" and "book flights".

3. **Tool Invocation**: You come talk AI assistant, "Abeg search flight from Portland to Honolulu." AI assistant use LLM find say e need call "search flights" tool and e send parameters (origin, destination) to MCP server.

4. **Execution and Response**: MCP server, wey dey like wrapper, call airline internal booking API. E collect flight info (like JSON) and send back to AI assistant.

5. **Further Interaction**: AI assistant show you flight options. When you select flight, assistant fit call "book flight" tool on same MCP server to finish booking.

## Agent-to-Agent Protocol (A2A)

While MCP focus on to connect LLMs to tools, **Agent-to-Agent (A2A) protocol** carry am one step further as e enable communication and collaboration between different AI agents. A2A connect AI agents from different organizations, environments and tech stacks to finish shared task.

We go look A2A parts and benefits plus example how e fit work for our travel app.

### A2A Core Components

A2A dey focus on communication between agents and to make dem work together to finish part of user task. Every part for protocol get role for this:

#### Agent Card

Like how MCP server share list of tools, Agent Card get:
- Agent Name.
- **description of general tasks** wey e fit do.
- **list of specific skills** with description to help other agents (or humans) know when and why to call am.
- **current Endpoint URL** of agent.
- **version** and **capabilities** like streaming responses and push notifications.

#### Agent Executor

Agent Executor dey responsible to **pass user chat context to remote agent**, so remote agent fit understand the task. For A2A server, agent use im own LLM to parse request and do tasks with im internal tools.

#### Artifact

When remote agent finish task, e work product na artifact. Artifact **get result of agent work**, **description of wetin e finish**, and **text context** wey protocol carry. After artifact send, connection close until again e need am.

#### Event Queue

Dis part handle **updates and pass messages**. E important for production agentic systems to make sure connection no close before task finish, especially when e fit take long time.

### Benefits of A2A

• **Better Collaboration**: E make agents from different vendors and platforms fit interact, share context and work together, making automation smooth across disconnected systems.

• **Model Selection Flexibility**: Each A2A agent fit choose LLM wey e use to serve its requests, so e fit use optimized or fine-tuned models per agent, unlike one LLM connection inside MCP.

• **Built-in Authentication**: Authentication dey inside A2A protocol, e provide strong security for agent interaction.

### A2A Example

![A2A Diagram](../../../translated_images/pcm/A2A-Diagram.8666928d648acc26.webp)

Make we expand our travel booking story but dis time using A2A.

1. **User Request to Multi-Agent**: User talk to "Travel Agent" A2A client/agent, maybe say, "Abeg book whole trip go Honolulu for next week, flight, hotel and rental car."

2. **Travel Agent Orchestrates**: Travel Agent receive complex request. E use LLM reason task and find say e need to connect with other special agents.

3. **Inter-Agent Communication**: Travel Agent use A2A protocol connect to downstream agents like "Airline Agent," "Hotel Agent," "Car Rental Agent" wey different companies make.

4. **Delegated Task Execution**: Travel Agent send task parts to special agents (e.g., "Find flights to Honolulu," "Book hotel," "Rent car"). Each agent run their own LLM and use their own tools (like MCP servers) to do their part of booking.

5. **Consolidated Response**: When all agents finish task, Travel Agent compile results (flight details, hotel confirm, car rent booking) and send full chat-style response to user.

## Natural Language Web (NLWeb)

Websites don be main way users dey find info and data for internet long time.

Make we check NLWeb parts, benefits and example of how NLWeb work for our travel app.

### Components of NLWeb

- **NLWeb Application (Core Service Code)**: Na system wey process natural language questions. E connect parts of platform to create responses. You fit think am as **engine wey power natural language features** for website.

- **NLWeb Protocol**: Na **basic rules for natural language interaction** with website. E dey send responses in JSON format (often Schema.org). Purpose na to make simple base for “AI Web,” like HTML do for documents online.

- **MCP Server (Model Context Protocol Endpoint)**: Every NLWeb setup also work as **MCP server**. That mean e fit **share tools (like “ask” method) and data** with other AI systems. This one make website content and features usable by AI agents, so site fit be part of bigger “agent ecosystem.”

- **Embedding Models**: These models dey use to **turn website content into numbers called vectors** (embeddings). Vectors dey carry meaning in way computers fit compare and search. Dem store am for special database, user fit choose embedding model wey dem want.

- **Vector Database (Retrieval Mechanism)**: This database **store embeddings of website content**. When person ask question, NLWeb go check vector database to quickly find best info. E come give list of best answers wey dem rank by similarity. NLWeb work with vector storage system like Qdrant, Snowflake, Milvus, Azure AI Search, and Elasticsearch.

### NLWeb by Example

![NLWeb](../../../translated_images/pcm/nlweb-diagram.c1e2390b310e5fe4.webp)

Consider our travel booking website again, but this time we use NLWeb.

1. **Data Ingestion**: Travel website product catalog (flight listings, hotel description, tour packages) dem format with Schema.org or load through RSS feeds. NLWeb tools take this structured data, make embeddings and store for local or remote vector database.

2. **Natural Language Query (Human)**: User go website, no dey run menu, just type for chat interface: "Find me family-friendly hotel for Honolulu with pool for next week."

3. **NLWeb Processing**: NLWeb app receive query. E send query to LLM for understanding and at the same time search vector database for correct hotel listings.

4. **Accurate Results**: LLM help interpret search result from database, find best match based on "family-friendly," "pool," and "Honolulu" and format natural language answer. Important: answer go refer real hotels from website catalog, no fake info.

5. **AI Agent Interaction**: Since NLWeb dey serve as MCP server, external AI travel agent fit also connect to NLWeb website. AI agent fit use `ask` MCP method to ask site directly: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. NLWeb go process, use restaurant info database (if loaded), and return structured JSON response.

### Still get questions about MCP/A2A/NLWeb?

Join di [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, join office hours and get your AI Agents questions answered.

## Resources

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Previous Lesson

[AI Agents in Production](../10-ai-agents-production/README.md)

## Next Lesson

[Context Engineering for AI Agents](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->