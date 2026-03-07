# How Dem Dey Use Agentic Protocols (MCP, A2A and NLWeb)

[![Agentic Protocols](../../../translated_images/pcm/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Click the image wey dey above make you watch the video for this lesson)_

As di use of AI agents dey grow, so di need for protocols wey go make everything standard, secure, and support open innovation dey increase too. For dis lesson, we go cover 3 protocols wey dey try meet dis need - Model Context Protocol (MCP), Agent to Agent (A2A) and Natural Language Web (NLWeb).

## Introduction

For dis lesson, we go cover:

• How **MCP** dey allow AI Agents to access external tools and data to complete user tasks.

• How **A2A** dey enable communication and collaboration between different AI agents.

• How **NLWeb** dey bring natural language interfaces to any website wey go make AI Agents fit discover and interact with the content.

## Learning Goals

• **Identify** di main purpose and benefits of MCP, A2A, and NLWeb for AI agents.

• **Explain** how each protocol dey help communication and interaction between LLMs, tools, and other agents.

• **Recognize** di different roles wey each protocol dey play for building complex agentic systems.

## Model Context Protocol

Di **Model Context Protocol (MCP)** na open standard wey provide one standardized way for applications to give context and tools to LLMs. Dis one dey enable "universal adaptor" to different data sources and tools wey AI Agents fit connect to in one consistent way.

Make we look di components of MCP, di benefits compared to direct API usage, and one example of how AI agents fit use one MCP server.

### MCP Core Components

MCP dey work with **client-server architecture** and di core components na:

• **Hosts** na LLM applications (for example a code editor like VSCode) wey dey start di connections to an MCP Server.

• **Clients** na components wey dey inside di host application wey dey maintain one-to-one connections with servers.

• **Servers** na lightweight programs wey dey expose specific capabilities.

Inside di protocol, three core primitives dey wey be di capabilities of an MCP Server:

• **Tools**: Na discrete actions or functions wey AI agent fit call to perform action. For example, weather service fit expose "get weather" tool, or e-commerce server fit expose "purchase product" tool. MCP servers dey show each tool name, description, and input/output schema for their capabilities listing.

• **Resources**: Na read-only data items or documents wey MCP server fit provide, and clients fit retrieve dem on demand. Examples na file contents, database records, or log files. Resources fit be text (like code or JSON) or binary (like images or PDFs).

• **Prompts**: Na predefined templates wey dey give suggested prompts, make e possible to do more complex workflows.

### Benefits of MCP

MCP dey give big advantages for AI Agents:

• **Dynamic Tool Discovery**: Agents fit dynamically receive list of available tools from server plus descriptions of wetin dem dey do. Dis one different from traditional APIs wey dey require static coding for integrations, wey mean any API change fit need code updates. MCP dey give "integrate once" approach, wey make am flexible well well.

• **Interoperability Across LLMs**: MCP dey work across different LLMs, e dey give flexibility to switch core models to test for better performance.

• **Standardized Security**: MCP get standard authentication method, e dey make scaling easier when you wan add access to more MCP servers. E simple pass to manage different keys and authentication types across many traditional APIs.

### MCP Example

![MCP Diagram](../../../translated_images/pcm/mcp-diagram.e4ca1cbd551444a1.webp)

Make we imagine say user wan book flight using AI assistant wey MCP power.

1. **Connection**: Di AI assistant (di MCP client) go connect to an MCP server wey airline provide.

2. **Tool Discovery**: Di client go ask di airline MCP server, "Wetin tools una get?" Di server go reply with tools like "search flights" and "book flights".

3. **Tool Invocation**: You go tell di AI assistant, "Make you search for flight from Portland to Honolulu." Di AI assistant, using im LLM, go sabi say e need call the "search flights" tool and e go pass di relevant parameters (origin, destination) to di MCP server.

4. **Execution and Response**: Di MCP server, wey act as wrapper, go make di real call to di airline internal booking API. E go receive di flight information (e.g., JSON data) and send am back to di AI assistant.

5. **Further Interaction**: Di AI assistant go show di flight options. When you select flight, di assistant fit invoke di "book flight" tool for di same MCP server, finish di booking.

## Agent-to-Agent Protocol (A2A)

While MCP dey focus on connecting LLMs to tools, di **Agent-to-Agent (A2A) protocol** go one step further by enabling communication and collaboration between different AI agents. A2A dey connect AI agents across different organizations, environments and tech stacks to complete one shared task.

We go check di components and benefits of A2A, plus one example how e fit apply for our travel application.

### A2A Core Components

A2A dey focus on enabling communication between agents and make dem work together to finish part of user task. Every component of di protocol dey contribute to this:

#### Agent Card

Like how MCP server dey share list of tools, an Agent Card get:
- Di Name of di Agent .
- A **description of di general tasks** wey e dey do.
- A **list of specific skills** with descriptions to help other agents (or even human users) understand when and why dem go want call that agent.
- Di **current Endpoint URL** of di agent
- Di **version** and **capabilities** of di agent like streaming responses and push notifications.

#### Agent Executor

Di Agent Executor na person wey dey responsible for **passing di context of di user chat to di remote agent**, di remote agent need am to understand di task wey dem need complete. For one A2A server, agent go use im own Large Language Model (LLM) to parse incoming requests and run tasks using im own internal tools.

#### Artifact

When remote agent don finish di requested task, im work product go come out as an artifact. An artifact **get di result of di agent's work**, **description of wetin dem complete**, and di **text context** wey dem send through di protocol. After di artifact don send, di connection with di remote agent go close till e need am again.

#### Event Queue

Dis component dey use for **handling updates and passing messages**. E important for production agentic systems so dat connection between agents no go close before task finish, especially when task fit take long time.

### Benefits of A2A

• **Enhanced Collaboration**: E enable agents from different vendors and platforms to interact, share context, and work together, make automation fit occur across systems wey before no connect.

• **Model Selection Flexibility**: Each A2A agent fit choose which LLM e wan use for its requests, make dem fit use optimized or fine-tuned models per agent, not like when one setup dey force single LLM connection like some MCP cases.

• **Built-in Authentication**: Authentication dey inside A2A protocol, e provide strong security framework for agent interactions.

### A2A Example

![A2A Diagram](../../../translated_images/pcm/A2A-Diagram.8666928d648acc26.webp)

Make we expand our travel booking scenario, but dis time make we use A2A.

1. **User Request to Multi-Agent**: User go interact with "Travel Agent" A2A client/agent, fit tell am, "Please book an entire trip to Honolulu for next week, including flights, a hotel, and a rental car".

2. **Orchestration by Travel Agent**: Travel Agent go receive this complex request. E go use im LLM to reason about di task and decide say e need to talk to other specialized agents.

3. **Inter-Agent Communication**: Travel Agent go then use A2A protocol to connect to downstream agents, like "Airline Agent," "Hotel Agent," and "Car Rental Agent" wey different companies create.

4. **Delegated Task Execution**: Travel Agent go send specific tasks to these specialized agents (e.g., "Find flights to Honolulu," "Book a hotel," "Rent a car"). Each specialized agent, wey dey run im own LLMs and dey use im own tools (wey fit be MCP servers themselves), go do im part of di booking.

5. **Consolidated Response**: When all downstream agents don finish their tasks, Travel Agent go compile di results (flight details, hotel confirmation, car rental booking) and send one complete, chat-style response back to di user.

## Natural Language Web (NLWeb)

Websites don long be di main way wey users dey access information and data across di internet.

Make we look di different components of NLWeb, di benefits of NLWeb and one example how our NLWeb dey work by checking our travel application.

### Components of NLWeb

- **NLWeb Application (Core Service Code)**: Di system wey dey process natural language questions. E connect di different parts of di platform to create responses. You fit reason am as di **engine wey power di natural language features** of a website.

- **NLWeb Protocol**: Na **basic set of rules for natural language interaction** with website. E dey send back responses for JSON format (often using Schema.org). Di purpose na to create simple foundation for di “AI Web,” same way HTML make e possible to share documents online.

- **MCP Server (Model Context Protocol Endpoint)**: Each NLWeb setup still dey function as an **MCP server**. Dis one mean say e fit **share tools (like an “ask” method) and data** with other AI systems. For practice, dis one make di website content and abilities usable by AI agents, make di site become part of di wider “agent ecosystem.”

- **Embedding Models**: Dem models dey use to **convert website content into numerical representations wey dem dey call vectors** (embeddings). These vectors capture meaning in a way computers fit compare and search. Dem dey store dem inside special database, and users fit choose which embedding model dem wan use.

- **Vector Database (Retrieval Mechanism)**: Dis database **stores di embeddings of di website content**. When person ask question, NLWeb go check di vector database to quickly find di most relevant information. E go give fast list of possible answers, ranked by similarity. NLWeb fit work with different vector storage systems like Qdrant, Snowflake, Milvus, Azure AI Search, and Elasticsearch.

### NLWeb by Example

![NLWeb](../../../translated_images/pcm/nlweb-diagram.c1e2390b310e5fe4.webp)

Make we think about our travel booking website again, but dis time e dey powered by NLWeb.

1. **Data Ingestion**: Di travel website product catalogs (e.g., flight listings, hotel descriptions, tour packages) dem format using Schema.org or dem load via RSS feeds. NLWeb tools go ingest this structured data, create embeddings, and store dem for local or remote vector database.

2. **Natural Language Query (Human)**: User go visit di website and instead of dey waka through menus, e go type for chat interface: "Find me a family-friendly hotel in Honolulu with a pool for next week".

3. **NLWeb Processing**: Di NLWeb application go receive dis query. E go send di query to an LLM to understand am and at di same time go search im vector database for relevant hotel listings.

4. **Accurate Results**: Di LLM go help interpret di search results from di database, find di best matches based on "family-friendly," "pool," and "Honolulu" criteria, then format natural language response. Important thing be say di response go refer to real hotels from di website catalog, so e no go dey make things up.

5. **AI Agent Interaction**: Because NLWeb dey serve as an MCP server, external AI travel agent fit also connect to dis website NLWeb instance. Di AI agent fit then use di `ask` MCP method to query di website directly: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. Di NLWeb instance go process am, use im database of restaurant information (if e load am), and return structured JSON response.

### Got More Questions about MCP/A2A/NLWeb?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Resources

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate by AI translation service [Co-op Translator] (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translations fit get mistakes or no too accurate. The original document for im original language na the correct source wey you suppose follow. If na important matter, make professional human translator do am. We no go responsible for any misunderstanding or wrong interpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->