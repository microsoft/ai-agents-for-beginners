# Memory for AI Agents 
[![Agent Memory](../../../translated_images/pcm/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

When we dey talk about di unique beta wey AI Agents fit bring, two tins be di main tins wey dem dey discuss: di ability to use tools to finish work and di ability to improve over time. Memory na wetin dey foundation of creating self-improving agent wey fit create beta experiences for our users.

For dis lesson, we go look wetin memory mean for AI Agents and how we fit manage am and use am make e benefit our applications.

## Introduction

Dis lesson go cover:

• **Understanding AI Agent Memory**: Wetin memory be and why e important for agents.

• **Implementing and Storing Memory**: How to take add memory capabilities to your AI agents, focus on short-term and long-term memory.

• **Making AI Agents Self-Improving**: How memory dey enable agents to learn from past interactions and improve over time.

## Available Implementations

Dis lesson get two full notebook tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implements memory using Mem0 and Azure AI Search with Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implements structured memory using Cognee, automatically dey build knowledge graph backed by embeddings, dey show graph, plus intelligent retrieval

## Learning Goals

After you finish dis lesson, you go sabi how to:

• **Differentiate between different AI agent memory types**, including working, short-term, and long-term memory, plus special kinds like persona and episodic memory.

• **Implement and manage short-term and long-term memory for AI agents** using Microsoft Agent Framework, use tools like Mem0, Cognee, Whiteboard memory, plus integrate with Azure AI Search.

• **Understand how self-improving AI agents work** and how strong memory management systems dey help continuous learning and adaptation.

## Understanding AI Agent Memory

Basically, **memory for AI agents na di way wey dem fit keep and recall info**. Dis info fit be specific detail about conversation, user preference, past actions, or learned patterns.

Without memory, AI apps go be like stateless, meaning every time interaction go start from zero. Dis one go cause repetitive and frustrating user experience where di agent go "forgets" old context or preference.

### Why Memory Important?

An agent intelligence dey strongly based on how e fit recall and use past info. Memory make agents:

• **Reflective**: Learn from past actions and results.

• **Interactive**: Hold context during ongoing talk.

• **Proactive and Reactive**: Fit predict needs or react well based on past data.

• **Autonomous**: Dey work more independently by using stored knowledge.

Di aim of implementing memory na to make agents more **reliable and capable**.

### Types of Memory

#### Working Memory

Think am like scratch paper wey agent go use during one task or thought process wey e dey do. E hold di info wey e need immediately to do next step.

For AI agents, working memory dey capture di most important info from conversation, even if di full chat history long or cut. E dey focus on di key things like requirements, proposals, decisions, and actions.

**Working Memory Example**

For travel booking agent, working memory fit hold di user's current request, like "I want to book trip go Paris". Dis specific request dey inside agent immediate context to guide di current talk.

#### Short Term Memory

Dis kind memory dey hold info for one conversation or session duration. Na di context of current chat, wey allow agent to refer back to previous dialogue turns.

For [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK samples, e be like `AgentSession`, wey dem create with `agent.create_session()`. Di session na di framework built-in short-term memory: e hold conversation context while di same session dey used, but di context no dey keep after session end or app restart. Use long-term memory for facts or preferences wey suppose last through sessions, normally through database, vector index, or other persistent store.

**Short Term Memory Example**

If user ask, "How much flight to Paris go cost?" then follow up with "What about accommodation there?", short-term memory go make sure agent sabi "there" mean "Paris" inside dat conversation.

#### Long Term Memory

Dis one be info wey last across multiple conversations or sessions. E allow agents remember user preferences, past interactions, or general knowledge for longer time. E important for personal touch.

**Long Term Memory Example**

Long-term memory fit keep say "Ben like skiing and outdoor activities, like coffee with mountain view, and e no like advanced ski slopes because injury before". Dis info, wey e learn from past chats, go help make future travel sessions them personalized.

#### Persona Memory

Dis kind special memory dey help agent get steady "personality" or "persona". E allow agent remember tins about itself or e role, make interactions smooth and focused.

**Persona Memory Example**

If travel agent suppose be "expert ski planner," persona memory go firm up that role, affect how e respond with expert tone and knowledge.

#### Workflow/Episodic Memory

Dis memory dey keep track of steps wey agent do for complex task, including wetin succeed and wetin fail. E be like remembering specific "episodes" or old experiences to learn from dem.

**Episodic Memory Example**

If agent try book flight but fail because no availability, episodic memory fit record dis, make agent fit try different flights or tell user better info later.

#### Entity Memory

Dis one involve to extract and remember specific entities (people, places, or tins) plus events from conversation. E let agent build structured understanding of important things discussed.

**Entity Memory Example**

From conversation about past trip, agent fit pull out "Paris," "Eiffel Tower," and "dinner at Le Chat Noir restaurant" as entities. For future talk, agent fit remember "Le Chat Noir" and offer to book new reservation there.

#### Structured RAG (Retrieval Augmented Generation)

Even though RAG na big technique, "Structured RAG" na powerful memory technology. E dey extract detailed, structured info from different sources (talks, emails, pictures) to improve accuracy, recall, and fast response. Unlike normal RAG wey only dey use semantic similarity, Structured RAG dey use info structure.

**Structured RAG Example**

Instead of just match keywords, Structured RAG fit parse flight details (destination, date, time, airline) from email and store am structured. Dis one fit handle exact questions like "Which flight I book to Paris on Tuesday?"

## Implementing and Storing Memory

To implement memory for AI agents, you go need proper process for **memory management**: generate, store, retrieve, integrate, update, and even "forget" (or delete) info. Retrieval na very important part.

### Specialized Memory Tools

#### Mem0

One way to store and manage agent memory na to use special tools like Mem0. Mem0 works as persistent memory layer, so agents fit remember relevant talks, keep user preferences and factual context, plus learn from wins and fails over time. The idea be say stateless agents go turn stateful.

E work with **two-phase memory pipeline: extraction and update**. First, messages added to agent thread dey send to Mem0 service, wey use Large Language Model (LLM) to summarize chat history and extract new memories. Next, LLM-driven update phase go decide whether to add, change, or delete memories, store them for hybrid data store wey fit get vector, graph, and key-value databases. Dis system sabi many memory types and fit use graph memory to manage relationships between entities.

#### Cognee

Another strong way na to use **Cognee**, open-source semantic memory for AI agents wey fit turn structured and unstructured data into queryable knowledge graphs wey get embeddings backing am. Cognee get **dual-store architecture** wey join vector similarity search plus graph relationships, so agents fit sabi not only wetin info similar, but also how different concepts relate.

E sabi **hybrid retrieval** wey mix vector similarity, graph structure, and LLM reasoning - from raw chunk lookup to graph-aware question answer. System dey keep **living memory** wey grow and change but still dey queryable as one connected graph, support short-term session context and long-term persistent memory.

Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) dey show how to build dis single memory layer, with practical examples of ingesting different data sources, showing knowledge graph, and querying with different search styles fit for agent needs.

### Storing Memory with RAG

Besides special tools like mem0 , you fit use strong search services like **Azure AI Search as backend to store and retrieve memories**, especially for structured RAG.

Dis one allow you ground your agent responses with your own data, make answers more relevant and correct. Azure AI Search fit hold user-specific travel memories, product catalogs, or any other special knowledge.

Azure AI Search support things like **Structured RAG**, wey dey good at extracting and retrieving dense, structured info from huge datasets like chat histories, emails, or pictures. E give "superhuman precision and recall" compared to normal text chunking and embedding ways.

## Making AI Agents Self-Improve

Common way for self-improving agents na to make **"knowledge agent"**. Dis one separate agent go watch main conversation between user and main agent. E role na to:

1. **Identify valuable information**: Decide if any part of conversation worth to save as general knowledge or specific user preference.

2. **Extract and summarize**: Take important learning or preference from conversation.

3. **Store inside knowledge base**: Keep extracted info, normally for vector database, so e fit be retrieved later.

4. **Add context for future queries**: When user start new query, knowledge agent go bring relevant stored info join user prompt, give important context to main agent (similar to RAG).

### Optimizations for Memory

• **Latency Management**: To prevent slow user experience, cheaper and faster model fit dey used first to quickly check if info worth to store or retrieve, then call complex extraction/retrieval only if needed.

• **Knowledge Base Maintenance**: For growing knowledge base, less used info fit move go "cold storage" to reduce costs.

## Got More Questions About Agent Memory?

Join di [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, attend office hours, and get your AI Agents questions answered.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->