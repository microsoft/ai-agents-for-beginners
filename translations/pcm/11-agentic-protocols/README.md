# Using Agentic Protocols (MCP, A2A na NLWeb)

[![Agentic Protocols](../../../translated_images/pcm/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Click di pikshua wey dey up so make you fit watch video of dis lesson)_

As AI agents dey grow, so na im di need for protocols wey go make sure say everything dey standard, secure, and support open innovation dey grow too. For dis lesson, we go tok about 3 protocols wey wan meet dis need - Model Context Protocol (MCP), Agent to Agent (A2A) and Natural Language Web (NLWeb).

## Introduction

For dis lesson, we go cover:

• How **MCP** dey allow AI Agents to access external tools and data to finish user tasks.

• How **A2A** dey make communication and collabo between different AI agents possible.

• How **NLWeb** dey bring natural language interfaces to any website so AI Agents fit find and interact with di content.

## Learning Goals

• **Identify** di main purpose and benefits of MCP, A2A, and NLWeb inside di context of AI agents.

• **Explain** how every protocol dey help communication and interaction between LLMs, tools, and other agents.

• **Recognize** di specific roles wey each protocol play for building complex agentic systems.

## Model Context Protocol

The **Model Context Protocol (MCP)** na open standard wey dey provide one standardized way for applications to provide context and tools to LLMs. Dis one dey enable a "universal adaptor" to different data sources and tools wey AI Agents fit connect to consistently.

Make we look di components of MCP, di benefits wey e get compared to direct API use, plus example of how AI agents fit use MCP server.

### MCP Core Components

MCP dey operate on **client-server architecture** and di core components be:

• **Hosts** na LLM applications (example be code editor like VSCode) wey dey start connection to MCP Server.

• **Clients** na components inside di host application wey dey maintain one-to-one connection with servers.

• **Servers** na light programs wey dey expose specific capabilities.

Inside di protocol, dem get three main primitives wey be capabilities of MCP Server:

• **Tools**: Na discrete actions or functions wey AI agent fit call to perform action. E.g., weather service fit get "get weather" tool, or e-commerce server fit get "purchase product" tool. MCP servers dey advertise each tool name, description, and input/output schema for their capabilities list.

• **Resources**: Na read-only data or documents wey MCP server fit provide, and clients fit collect dem when dem want. Examples na file contents, database records, or log files. Resources fit be text (like code or JSON) or binary (like images or PDFs).

• **Prompts**: Na predefined templates wey dey give suggested prompts, to allow more complex workflows.

### Benefits of MCP

MCP get big advantages for AI Agents:

• **Dynamic Tool Discovery**: Agents fit dynamically receive list of available tools from server together wit descriptions of wetin dem dey do. Dis different from old APIs wey need static coding for integrations, so anytime API change, you go need change code. MCP na "integrate once" way, e make am flexible.

• **Interoperability Across LLMs**: MCP fit work with different LLMs, so you fit decide to switch core models to find better performance.

• **Standardized Security**: MCP get standard authentication method, e dey make am easy to scale when you wan add access to more MCP servers. E easy pass to manage different keys and auth types for different traditional APIs.

### MCP Example

![MCP Diagram](../../../translated_images/pcm/mcp-diagram.e4ca1cbd551444a1.webp)

Imagine say user wan book flight using AI assistant wey MCP power.

1. **Connection**: AI assistant (di MCP client) connect to MCP server wey airline provide.

2. **Tool Discovery**: Client ask airline MCP server, "Wetin tools you get?" Server go answer for tools like "search flights" and "book flights".

3. **Tool Invocation**: You fit tell AI assistant, "Make you search flight from Portland go Honolulu." AI assistant, using LLM, go know say e need call "search flights" tool and e go pass parameters (origin, destination) to MCP server.

4. **Execution and Response**: MCP server, wey be wrapper, go make real call to airline internal booking API. E go receive flight info (e.g., JSON data) and send am back to AI assistant.

5. **Further Interaction**: AI assistant go show flight options. When you select flight, assistant fit call "book flight" tool on same MCP server to complete booking.

## Agent-to-Agent Protocol (A2A)

While MCP focus on connecting LLMs to tools, **Agent-to-Agent (A2A) protocol** dey take am one step further by making communication and collaboration between different AI agents possible. A2A dey connect AI agents from different organizations, environments, and tech stacks to finish shared task.

We go check components and benefits of A2A, plus example of how e fit work for travel app.

### A2A Core Components

A2A dey enable communication between agents and make dem work together to finish user task. Each protocol component get role:

#### Agent Card

Like how MCP server dey share list of tools, Agent Card get:
- Name of Agent.
- **description of general tasks** wey e dey do.
- **list of specific skills** with description to help other agents (or even humans) understand when and why dem go call dat agent.
- **current Endpoint URL** of di agent.
- **version** and **capabilities** of di agent like streaming responses and push notifications.

#### Agent Executor

Agent Executor dey responsible to **pass user chat context to remote agent**, because remote agent need am to understand wetin e suppose do. For A2A server, agent dey use e own Large Language Model (LLM) to parse requests and execute tasks with e own internal tools.

#### Artifact

After remote agent don finish requested task, im work product dey create as artifact. Artifact **get result of agent work**, **description of wetin e do**, plus **text context** wey dem send through protocol. After artifact send, connection with remote agent go close until next time e need am.

#### Event Queue

Dis dey handle **updates and pass messages**. E important well well for production of agentic systems so connection between agents no go close before task finish, especially when some tasks fit take long time.

### Benefits of A2A

• **Enhanced Collaboration**: E make agents from different vendors and platforms fit interact, share context, and work together, helping automation between systems wey no usually connect.

• **Model Selection Flexibility**: Each A2A agent fit choose which LLM e use for e requests, so e fit use optimized or tuned models per agent, no be like one LLM for some MCP cases.

• **Built-in Authentication**: Authentication dey built into A2A protocol for strong security for agent interaction.

### A2A Example

![A2A Diagram](../../../translated_images/pcm/A2A-Diagram.8666928d648acc26.webp)

Make we extend travel booking example, but now with A2A.

1. **User Request to Multi-Agent**: User talk to "Travel Agent" A2A client/agent, talk say, "Please book whole trip to Honolulu for next week, including flights, hotel, and rental car".

2. **Orchestration by Travel Agent**: Travel Agent receive dis complex request. E use e LLM to reason and know say e need to work with other specialized agents.

3. **Inter-Agent Communication**: Travel Agent use A2A protocol to connect to other agents like "Airline Agent," "Hotel Agent," and "Car Rental Agent," wey different companies create.

4. **Delegated Task Execution**: Travel Agent send specific tasks to these specialized agents ("Find flights to Honolulu," "Book hotel," "Rent car"). Each of those specialized agents, running own LLMs and using own tools (fit be MCP servers), dey do their part of booking.

5. **Consolidated Response**: After all agents finish their tasks, Travel Agent gather results (flight details, hotel confirm, car rental booking) and send chat-style full response back to user.

## Natural Language Web (NLWeb)

Websites don long be main way wey people dey access information and data on internet.

Make we look different components of NLWeb, benefits of NLWeb and example of how NLWeb dey work for our travel app.

### Components of NLWeb

- **NLWeb Application (Core Service Code)**: Na system wey process natural language questions. E connect different parts of platform to create responses. You fit see am as **engine wey power natural language features** of website.

- **NLWeb Protocol**: Na **basic rules set for natural language interaction** with website. E send back responses in JSON format (normally using Schema.org). Purpose na to create simple base for “AI Web,” like HTML help share documents online.

- **MCP Server (Model Context Protocol Endpoint)**: Every NLWeb setup also work as **MCP server**. This mean e fit **share tools (like “ask” method) and data** with other AI systems. Dis make website content and power usable by AI agents, make website part of bigger “agent ecosystem.”

- **Embedding Models**: These models dey **convert website content into number representations wey dem dey call vectors** (embeddings). These vectors dey capture meaning so computer fit compare and search. Dem dey store am for special database, and users fit choose which embedding model dem want use.

- **Vector Database (Retrieval Mechanism)**: Dis database **stores embeddings of website content**. When person ask question, NLWeb go check vector database quick to find correct info. E go give correct answer list based on similarity. NLWeb dey work with many vector storage systems like Qdrant, Snowflake, Milvus, Azure AI Search, and Elasticsearch.

### NLWeb by Example

![NLWeb](../../../translated_images/pcm/nlweb-diagram.c1e2390b310e5fe4.webp)

Make we reason our travel booking website again, but dis time e dey powered by NLWeb.

1. **Data Ingestion**: Travel website product catalogs (like flights listings, hotel descriptions, tour packages) dey formatted using Schema.org or loaded with RSS feeds. NLWeb tools go ingest this structured data, make embeddings, and store for local or remote vector database.

2. **Natural Language Query (Human)**: User visit website, instead of dey navigate menus, e type for chat interface: "Find family-friendly hotel with pool for next week for Honolulu".

3. **NLWeb Processing**: NLWeb app receive dis query. E send am go LLM to understand and also search vector database for matching hotel listings.

4. **Accurate Results**: LLM help interpret search results, find best matches based on "family-friendly," "pool," and "Honolulu" criteria, then format natural language response. E important say response refer to real hotels from website catalog, no fake info.

5. **AI Agent Interaction**: Because NLWeb dey serve as MCP server, external AI travel agent fit connect to this website NLWeb instance. AI agent fit use `ask` MCP method to ask website: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. NLWeb instance go process am, use restaurant info database (if loaded), and send structured JSON response.

### Get More Questions about MCP/A2A/NLWeb?

Join [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, attend office hours and get your AI Agents questions answered.

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