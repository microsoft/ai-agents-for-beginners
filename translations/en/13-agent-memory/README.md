<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T15:58:02+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "en"
}
-->
# Memory for AI Agents 

When discussing the unique advantages of building AI Agents, two key aspects often come up: the ability to use tools to complete tasks and the ability to improve over time. Memory is the cornerstone of creating self-improving agents that can deliver better experiences for users.

In this lesson, we’ll explore what memory means for AI Agents, how to manage it, and how to use it to enhance our applications.

## Introduction

This lesson will cover:

• **Understanding AI Agent Memory**: What memory is and why it’s crucial for agents.

• **Implementing and Storing Memory**: Practical approaches to adding memory capabilities to AI agents, focusing on short-term and long-term memory.

• **Making AI Agents Self-Improving**: How memory enables agents to learn from past interactions and improve over time.

## Learning Goals

By the end of this lesson, you’ll be able to:

• **Distinguish between different types of AI agent memory**, including working, short-term, and long-term memory, as well as specialized forms like persona and episodic memory.

• **Implement and manage short-term and long-term memory for AI agents** using the Semantic Kernel framework, tools like Mem0 and Whiteboard memory, and integrations with Azure AI Search.

• **Understand the principles behind self-improving AI agents** and how effective memory management systems support continuous learning and adaptation.

## Understanding AI Agent Memory

At its core, **memory for AI agents refers to the mechanisms that allow them to retain and recall information**. This could include specific details from a conversation, user preferences, past actions, or learned patterns.

Without memory, AI applications are often stateless, meaning every interaction starts from scratch. This results in a repetitive and frustrating user experience where the agent "forgets" previous context or preferences.

### Why is Memory Important?

An agent’s intelligence is closely tied to its ability to recall and use past information. Memory enables agents to be:

• **Reflective**: Learning from past actions and outcomes.

• **Interactive**: Maintaining context throughout an ongoing conversation.

• **Proactive and Reactive**: Anticipating needs or responding appropriately based on historical data.

• **Autonomous**: Acting more independently by leveraging stored knowledge.

The goal of implementing memory is to make agents more **reliable and capable**.

### Types of Memory

#### Working Memory

Think of this as a temporary workspace an agent uses during a single, ongoing task or thought process. It holds immediate information needed to compute the next step.

For AI agents, working memory often captures the most relevant information from a conversation, even if the full chat history is lengthy or truncated. It focuses on extracting key elements like requirements, proposals, decisions, and actions.

**Working Memory Example**

In a travel booking agent, working memory might capture the user’s current request, such as "I want to book a trip to Paris." This specific requirement is held in the agent’s immediate context to guide the current interaction.

#### Short-Term Memory

This type of memory retains information for the duration of a single conversation or session. It provides context for the current chat, allowing the agent to refer back to previous turns in the dialogue.

**Short-Term Memory Example**

If a user asks, "How much would a flight to Paris cost?" and then follows up with "What about accommodation there?", short-term memory ensures the agent knows "there" refers to "Paris" within the same conversation.

#### Long-Term Memory

This is information that persists across multiple conversations or sessions. It allows agents to remember user preferences, historical interactions, or general knowledge over extended periods. This is key for personalization.

**Long-Term Memory Example**

A long-term memory might store that "Ben enjoys skiing and outdoor activities, likes coffee with a mountain view, and wants to avoid advanced ski slopes due to a past injury." This information, learned from previous interactions, influences recommendations in future travel planning sessions, making them highly personalized.

#### Persona Memory

This specialized memory type helps an agent maintain a consistent "personality" or "persona." It allows the agent to remember details about itself or its intended role, making interactions more coherent and focused.

**Persona Memory Example**

If the travel agent is designed to be an "expert ski planner," persona memory might reinforce this role, ensuring its responses align with an expert’s tone and knowledge.

#### Workflow/Episodic Memory

This memory stores the sequence of steps an agent takes during a complex task, including successes and failures. It’s like remembering specific "episodes" or past experiences to learn from them.

**Episodic Memory Example**

If the agent tried to book a specific flight but it failed due to unavailability, episodic memory could record this failure, enabling the agent to try alternative flights or inform the user about the issue in a more informed way during a subsequent attempt.

#### Entity Memory

This involves extracting and remembering specific entities (like people, places, or things) and events from conversations. It allows the agent to build a structured understanding of key elements discussed.

**Entity Memory Example**

From a conversation about a past trip, the agent might extract "Paris," "Eiffel Tower," and "dinner at Le Chat Noir restaurant" as entities. In a future interaction, the agent could recall "Le Chat Noir" and offer to make a new reservation there.

#### Structured RAG (Retrieval Augmented Generation)

While RAG is a broader technique, "Structured RAG" is highlighted as a powerful memory technology. It extracts dense, structured information from various sources (conversations, emails, images) and uses it to enhance precision, recall, and speed in responses. Unlike classic RAG that relies solely on semantic similarity, Structured RAG works with the inherent structure of information.

**Structured RAG Example**

Instead of just matching keywords, Structured RAG could parse flight details (destination, date, time, airline) from an email and store them in a structured way. This allows precise queries like "What flight did I book to Paris on Tuesday?"

## Implementing and Storing Memory

Implementing memory for AI agents involves a systematic process of **memory management**, which includes generating, storing, retrieving, integrating, updating, and even "forgetting" (or deleting) information. Retrieval is particularly important.

### Specialized Memory Tools

One way to store and manage agent memory is by using specialized tools like Mem0. Mem0 acts as a persistent memory layer, enabling agents to recall relevant interactions, store user preferences and factual context, and learn from successes and failures over time. The idea is to transform stateless agents into stateful ones.

It operates through a **two-phase memory pipeline: extraction and update**. First, messages added to an agent’s thread are sent to the Mem0 service, which uses a Large Language Model (LLM) to summarize conversation history and extract new memories. Then, an LLM-driven update phase determines whether to add, modify, or delete these memories, storing them in a hybrid data store that can include vector, graph, and key-value databases. This system also supports various memory types and can incorporate graph memory for managing relationships between entities.

### Storing Memory with RAG

Beyond specialized memory tools like Mem0, you can use robust search services like **Azure AI Search as a backend for storing and retrieving memories**, especially for structured RAG.

This allows you to ground your agent’s responses with your own data, ensuring more relevant and accurate answers. Azure AI Search can be used to store user-specific travel memories, product catalogs, or any other domain-specific knowledge.

Azure AI Search supports capabilities like **Structured RAG**, which excels at extracting and retrieving dense, structured information from large datasets like conversation histories, emails, or even images. This provides "superhuman precision and recall" compared to traditional text chunking and embedding approaches.

## Making AI Agents Self-Improve

A common approach for self-improving agents involves introducing a **"knowledge agent"**. This separate agent observes the main conversation between the user and the primary agent. Its role is to:

1. **Identify valuable information**: Determine if any part of the conversation is worth saving as general knowledge or a specific user preference.

2. **Extract and summarize**: Distill the essential learning or preference from the conversation.

3. **Store in a knowledge base**: Persist this extracted information, often in a vector database, so it can be retrieved later.

4. **Augment future queries**: When the user initiates a new query, the knowledge agent retrieves relevant stored information and appends it to the user’s prompt, providing crucial context to the primary agent (similar to RAG).

### Optimizations for Memory

• **Latency Management**: To avoid slowing down user interactions, a cheaper, faster model can be used initially to quickly check if information is valuable to store or retrieve, only invoking the more complex extraction/retrieval process when necessary.

• **Knowledge Base Maintenance**: For a growing knowledge base, less frequently used information can be moved to "cold storage" to manage costs.

## Got More Questions About Context Engineering?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to connect with other learners, attend office hours, and get your AI Agents questions answered.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.