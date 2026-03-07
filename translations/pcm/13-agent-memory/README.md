# Memori for AI Agents 
[![Agent Memori](../../../translated_images/pcm/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Wen we dey tok about wetin make e special to create AI Agents, two main tins de usually come up: di ability to call tools make dem complete tasks and di ability to improve with time. Memori na di foundation wey dey make self-improving agents fit give better experience to our users.

For dis lesson, we go look wetin memori mean for AI Agents and how we fit manage am and use am make our applications benefit.

## Introduction

Dis lesson go cover:

• **Understandin di AI Agent Memori**: Wetin memori be and why e important for agents.

• **Implementin and Storin Memori**: Practical ways to add memori capability to your AI agents, wey go focus on short-term and long-term memori.

• **Make AI Agents Self-Improvin**: How memori dey enable agents learn from past interactions and improve with time.

## Available Implementations

Dis lesson get two complete notebook tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implements memori using Mem0 and Azure AI Search with Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implements structured memori using Cognee, wey dey automatically build knowledge graph backed by embeddings, dey visualize di graph, and sabi do intelligent retrieval

## Learning Goals

After you finish dis lesson, you go sabi how to:

• **Differentiate between various types of AI agent memori**, including working, short-term, and long-term memori, plus special forms like persona and episodic memori.

• **Implement and manage short-term and long-term memori for AI agents** using Microsoft Agent Framework, and use tools like Mem0, Cognee, Whiteboard memory, and integrate with Azure AI Search.

• **Understand di principles behind self-improving AI agents** and how proper memori management systems dey help continuous learning and adaptation.

## Understanding AI Agent Memory

For im root, **memori for AI agents mean di mechanisms wey make dem fit retain and recall information**. Dis information fit be specific details about one conversation, user preferences, past actions, or even learned patterns.

Without memori, AI apps dey often stateless, wey mean say every interaction go start from scratch. Dis one dey cause repetitive and frustrating user experience where di agent "go forget" previous context or preferences.

### Why is Memory Important?

Di intelligence of an agent dey strongly connected to im ability to recall and use past information. Memori make agents fit:

• **Reflective**: Learn from past actions and outcomes.

• **Interactive**: Keep context across ongoing conversation.

• **Proactive and Reactive**: Anticipate needs or respond well based on historical data.

• **Autonomous**: Work more independently by drawing on saved knowledge.

Di goal of implementing memori na to make agents more **reliable and capable**.

### Types of Memory

#### Working Memory

Think am like scratch paper wey agent dey use during one single, ongoing task or thought process. E hold immediate information wey agent need to compute di next step.

For AI agents, working memori dey often capture di most relevant information from one conversation, even if di full chat history long or truncated. E dey focus on extracting key elements like requirements, proposals, decisions, and actions.

**Working Memory Example**

For one travel booking agent, working memori fit capture wetin user dey request now, like "I want to book a trip to Paris". Dis specific requirement go remain for agent immediate context to guide di current interaction.

#### Short Term Memory

Dis kain memori dey keep information for di duration of one conversation or session. Na di context of di current chat, wey allow di agent refer back to previous turns for di dialogue.

**Short Term Memory Example**

If user ask, "How much would a flight to Paris cost?" and then follow with "What about accommodation there?", short-term memori go make sure say di agent sabi say "there" mean "Paris" inside di same conversation.

#### Long Term Memory

Dis one na information wey dey persist across many conversations or sessions. E allow agents remember user preferences, past interactions, or general knowledge for long time. Dis one dey important for personalization.

**Long Term Memory Example**

Long-term memori fit store say "Ben enjoys skiing and outdoor activities, likes coffee with a mountain view, and wants to avoid advanced ski slopes due to a past injury". Dis kind information wey agent learn from previous interactions go influence recommendations for future travel planning, make dem very personalized.

#### Persona Memory

Dis specialized memori help agent develop one consistent "personality" or "persona". E allow di agent remember details about itself or im intended role, make interactions more smooth and focused.

**Persona Memory Example**
If di travel agent design to be "expert ski planner," persona memori fit reinforce dis role, make im responses follow an expert tone and knowledge.

#### Workflow/Episodic Memory

Dis memori dey store di sequence of steps an agent take during complex task, including successes and failures. E be like remembering specific "episodes" or past experiences to learn from them.

**Episodic Memory Example**

If di agent try book one flight but e fail because e no available, episodic memori fit record dis failure, so that agent fit try alternative flights or tell di user about di issue in a better way next time.

#### Entity Memory

Dis one involve extracting and remembering specific entities (like people, places, or things) and events from conversations. E allow di agent build structured understanding of di key elements wey dem discuss.

**Entity Memory Example**

From one conversation about past trip, di agent fit extract "Paris," "Eiffel Tower," and "dinner at Le Chat Noir restaurant" as entities. For future interaction, di agent fit recall "Le Chat Noir" and offer to make new reservation there.

#### Structured RAG (Retrieval Augmented Generation)

Even though RAG na broader technique, "Structured RAG" dey highlighted as powerful memori technology. E dey extract dense, structured information from different sources (conversations, emails, images) and use am to improve precision, recall, and speed for responses. Different from classic RAG wey only rely on semantic similarity, Structured RAG dey work with di inherent structure of information.

**Structured RAG Example**

Instead of just matching keywords, Structured RAG fit parse flight details (destination, date, time, airline) from one email and store dem in structured way. Dis one allow precise queries like "What flight did I book to Paris on Tuesday?"

## Implementing and Storing Memory

To implement memori for AI agents, you go follow systematic process of **memori management**, wey include generating, storing, retrieving, integrating, updating, and even "forgetting" (or deleting) information. Retrieval na one very important part.

### Specialized Memory Tools

#### Mem0

One way to store and manage agent memori na to use specialized tools like Mem0. Mem0 dey work as persistent memori layer, wey make agents fit recall relevant interactions, store user preferences and factual context, and learn from successes and failures over time. Di idea na make stateless agents turn stateful.

E dey work through **two-phase memori pipeline: extraction and update**. First, messages wey add to agent thread dey send go Mem0 service, wey dey use Large Language Model (LLM) to summarize conversation history and extract new memories. Afterwards, one LLM-driven update phase go decide whether to add, modify, or delete these memories, then store dem in hybrid data store wey fit include vector, graph, and key-value databases. Dis system still support different memory types and fit include graph memory to manage relationships between entities.

#### Cognee

Another strong approach na to use **Cognee**, one open-source semantic memori for AI agents wey dey transform structured and unstructured data into queryable knowledge graphs backed by embeddings. Cognee get **dual-store architecture** wey combine vector similarity search with graph relationships, so agents fit understand not just wetin similar be, but how concepts relate to each other.

E strong for **hybrid retrieval** wey blend vector similarity, graph structure, and LLM reasoning - from raw chunk lookup to graph-aware question answering. Di system maintain **living memory** wey dey evolve and grow but still dey queryable as one connected graph, supporting both short-term session context and long-term persistent memori.

Di Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) dey show how to build this unified memori layer, with practical examples of ingesting different data sources, visualizing di knowledge graph, and querying with different search strategies wey fit specific agent needs.

### Storing Memory with RAG

Apart from specialized memori tools like mem0, you fit use strong search services like **Azure AI Search as a backend for storing and retrieving memories**, especially for structured RAG.

Dis one allow you ground your agent responses with your own data, to make answers more relevant and accurate. Azure AI Search fit store user-specific travel memories, product catalogs, or any domain-specific knowledge.

Azure AI Search get capabilities like **Structured RAG**, wey dey excel for extracting and retrieving dense, structured information from big datasets like conversation histories, emails, or even images. Dis one dey give "superhuman precision and recall" compared to traditional text chunking and embedding approaches.

## Making AI Agents Self-Improve

One common pattern for self-improving agents na to introduce a **"knowledge agent"**. Dis separate agent dey observe di main conversation between di user and di primary agent. Im role na to:

1. **Identify valuable information**: Decide if any part of di conversation worth saving as general knowledge or as specific user preference.

2. **Extract and summarize**: Distill di important learning or preference from di conversation.

3. **Store in a knowledge base**: Save dis extracted information, many times for vector database, so e fit retrieve am later.

4. **Augment future queries**: When user start new query, di knowledge agent go retrieve relevant stored info and attach am to user prompt, give important context to di primary agent (similar to RAG).

### Optimizations for Memory

• **Latency Management**: To avoid slow down user interactions, you fit use cheaper, faster model first to quickly check if information worth to store or retrieve, then only call the more complex extraction/retrieval process when necessary.

• **Knowledge Base Maintenance**: For growing knowledge base, less-used information fit move go "cold storage" to manage costs.

## Got More Questions About Agent Memory?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, attend office hours and make your AI Agents questions clear.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate with AI translation service [Co-op Translator] (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automatic translations fit get mistakes or no too accurate. Make you treat the original document wey dey inside im native language as the main/authoritative source. If na important information, better make professional human translator do the translation. We no go responsible for any misunderstanding or wrong interpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->