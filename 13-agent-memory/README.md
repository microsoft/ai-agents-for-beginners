# Memory for AI Agents 
[![Agent Memory](./images/lesson-13-thumbnail.png)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

When discussing the unique benefits of creating AI Agents, two things are mainly discussed: the ability to call tools to complete tasks and the the ability to improve over time. Memory is at the foundation of creating self-improving agent that can create better experiences for our users.

In this lesson, we will look at what memory is for AI Agents and how we can manage it and use it for the benefit of our applications.

## Introduction

This lesson will cover:

• **Understanding AI Agent Memory**: What memory is and why it's essential for agents.

• **Implementing and Storing Memory**: Practical methods for adding memory capabilities to your AI agents, focusing on short-term and long-term memory.

• **Making AI Agents Self-Improving**: How memory enables agents to learn from past interactions and improve over time.

## Available Implementations

This lesson includes two comprehensive notebook tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implements memory using Mem0 and Azure AI Search with Semantic Kernel framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implements structured memory using Cognee, automatically building knowledge graph backed by embeddings, visualizing graph, and intelligent retrieval

## Learning Goals

After completing this lesson, you will know how to:

• **Differentiate between various types of AI agent memory**, including working, short-term, and long-term memory, as well as specialized forms like persona and episodic memory.

• **Implement and manage short-term and long-term memory for AI agents** using the Semantic Kernel framework, leveraging tools like Mem0, Cognee, Whiteboard memory, and integrating with Azure AI Search.

• **Understand the principles behind self-improving AI agents** and how robust memory management systems contribute to continuous learning and adaptation.

## Understanding AI Agent Memory

At its core, **memory for AI agents refers to the mechanisms that allow them to retain and recall information**. This information can be specific details about a conversation, user preferences, past actions, or even learned patterns.

Without memory, AI applications are often stateless, meaning each interaction starts from scratch. This leads to a repetitive and frustrating user experience where the agent "forgets" previous context or preferences.

### Why is Memory Important?

an agent's intelligence is deeply tied to its ability to recall and utilize past information. Memory allows agents to be:

• **Reflective**: Learning from past actions and outcomes.

• **Interactive**: Maintaining context over an ongoing conversation.

• **Proactive and Reactive**: Anticipating needs or responding appropriately based on historical data.

• **Autonomous**: Operating more independently by drawing on stored knowledge.

The goal of implementing memory is to make agents more **reliable and capable**.

### Types of Memory

#### Working Memory

Think of this as a piece of scratch paper an agent uses during a single, ongoing task or thought process. It holds immediate information needed to compute the next step.

For AI agents, working memory often captures the most relevant information from a conversation, even if the full chat history is long or truncated. It focuses on extracting key elements like requirements, proposals, decisions, and actions.

**Working Memory Example**

In a travel booking agent, working memory might capture the user's current request, such as "I want to book a trip to Paris". This specific requirement is held in the agent's immediate context to guide the current interaction.

#### Short Term Memory

This type of memory retains information for the duration of a single conversation or session. It's the context of the current chat, allowing the agent to refer back to previous turns in the dialogue.

**Short Term Memory Example**

If a user asks, "How much would a flight to Paris cost?" and then follows up with "What about accommodation there?", short-term memory ensures the agent knows "there" refers to "Paris" within the same conversation.

#### Long Term Memory

This is information that persists across multiple conversations or sessions. It allows agents to remember user preferences, historical interactions, or general knowledge over extended periods. This is important for personalization.

**Long Term Memory Example**

A long-term memory might store that "Ben enjoys skiing and outdoor activities, likes coffee with a mountain view, and wants to avoid advanced ski slopes due to a past injury". This information, learned from previous interactions, influences recommendations in future travel planning sessions, making them highly personalized.

#### Persona Memory

This specialized memory type helps an agent develop a consistent "personality" or "persona". It allows the agent to remember details about itself or its intended role, making interactions more fluid and focused.

**Persona Memory Example**
If the travel agent is designed to be an "expert ski planner," persona memory might reinforce this role, influencing its responses to align with an expert's tone and knowledge.

#### Workflow/Episodic Memory

This memory stores the sequence of steps an agent takes during a complex task, including successes and failures. It's like remembering specific "episodes" or past experiences to learn from them.

**Episodic Memory Example**

If the agent attempted to book a specific flight but it failed due to unavailability, episodic memory could record this failure, allowing the agent to try alternative flights or inform the user about the issue in a more informed way during a subsequent attempt.

#### Entity Memory

This involves extracting and remembering specific entities (like people, places, or things) and events from conversations. It allows the agent to build a structured understanding of key elements discussed.

**Entity Memory Example**

From a conversation about a past trip, the agent might extract "Paris," "Eiffel Tower," and "dinner at Le Chat Noir restaurant" as entities. In a future interaction, the agent could recall "Le Chat Noir" and offer to make a new reservation there.

#### Structured RAG (Retrieval Augmented Generation)

While RAG is a broader technique, "Structured RAG" is highlighted as a powerful memory technology. It extracts dense, structured information from various sources (conversations, emails, images) and uses it to enhance precision, recall, and speed in responses. Unlike classic RAG that relies solely on semantic similarity, Structured RAG works with the inherent structure of information.

**Structured RAG Example**

Instead of just matching keywords, Structured RAG could parse flight details (destination, date, time, airline) from an email and store them in a structured way. This allows precise queries like "What flight did I book to Paris on Tuesday?"

## Implementing and Storing Memory

Implementing memory for AI agents involves a systematic process of **memory management**, which includes generating, storing, retrieving, integrating, updating, and even "forgetting" (or deleting) information. Retrieval is a particularly crucial aspect.

### Specialized Memory Tools

#### Mem0

One way to store and manage agent memory is using specialized tools like Mem0. Mem0 works as a persistent memory layer, allowing agents to recall relevant interactions, store user preferences and factual context, and learn from successes and failures over time. The idea here is that stateless agents turn into stateful ones.

It works through a **two-phase memory pipeline: extraction and update**. First, messages added to an agent's thread are sent to the Mem0 service, which uses a Large Language Model (LLM) to summarize conversation history and extract new memories. Subsequently, an LLM-driven update phase determines whether to add, modify, or delete these memories, storing them in a hybrid data store that can include vector, graph, and key-value databases. This system also supports various memory types and can incorporate graph memory for managing relationships between entities.

#### Cognee

Another powerful approach is using **Cognee**, an open-source semantic memory for AI agents that transforms structured and unstructured data into queryable knowledge graphs backed by embeddings. Cognee provides a **dual-store architecture** combining vector similarity search with graph relationships, enabling agents to understand not just what information is similar, but how concepts relate to each other.

It excels at **hybrid retrieval** that blends vector similarity, graph structure, and LLM reasoning - from raw chunk lookup to graph-aware question answering. The system maintains **living memory** that evolves and grows while remaining queryable as one connected graph, supporting both short-term session context and long-term persistent memory.

The Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrates building this unified memory layer, with practical examples of ingesting diverse data sources, visualizing the knowledge graph, and querying with different search strategies tailored to specific agent needs.

### Storing Memory with RAG

Beyond specialized memory tools like mem0 , you can leverage robust search services like **Azure AI Search as a backend for storing and retrieving memories**, especially for structured RAG.

This allows you to ground your agent's responses with your own data, ensuring more relevant and accurate answers. Azure AI Search can be used to store user-specific travel memories, product catalogs, or any other domain-specific knowledge.

Azure AI Search supports capabilities like **Structured RAG**, which excels at extracting and retrieving dense, structured information from large datasets like conversation histories, emails, or even images. This provides "superhuman precision and recall" compared to traditional text chunking and embedding approaches.

## Making AI Agents Self-Improve

A common pattern for self-improving agents involves introducing a **"knowledge agent"**. This separate agent observes the main conversation between the user and the primary agent. Its role is to:

1. **Identify valuable information**: Determine if any part of the conversation is worth saving as general knowledge or a specific user preference.

2. **Extract and summarize**: Distill the essential learning or preference from the conversation.

3. **Store in a knowledge base**: Persist this extracted information, often in a vector database, so it can be retrieved later.

4. **Augment future queries**: When the user initiates a new query, the knowledge agent retrieves relevant stored information and appends it to the user's prompt, providing crucial context to the primary agent (similar to RAG).

### Optimizations for Memory

• **Latency Management**: To avoid slowing down user interactions, a cheaper, faster model can be used initially to quickly check if information is valuable to store or retrieve, only invoking the more complex extraction/retrieval process when necessary.

• **Knowledge Base Maintenance**: For a growing knowledge base, less frequently used information can be moved to "cold storage" to manage costs.

## Got More Questions About Agent Memory?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.
