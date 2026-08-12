# Memory for AI Agents 
[![Agent Memory](../../../translated_images/pcm/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Wen we dey talk about di unique beta wey AI Agents fit get, two tins na di main tins wey dem dey focus: di ability to use tools to finish work and di ability to improve as time dey go. Memory na di foundation for to create agent wey fit improve by itself and fit create beta experience for our users.

For dis lesson, we go see wetin memory mean for AI Agents and how we fit manage am and use am for di good tins for our applications.

## Introduction

Dis lesson go cover:

• **Understanding AI Agent Memory**: Wetin memory be and why e important for agents.

• **Implementing and Storing Memory**: Practical ways to add memory power to your AI agents, fokusing on short-term and long-term memory.

• **Making AI Agents Self-Improving**: How memory dey allow agents learn from past tins dem do and improve as time dey go.

## Available Implementations

Dis lesson get two main notebook tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implements memory using Mem0 and Azure AI Search with Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implements structured memory using Cognee, automatically building knowledge graph backed by embeddings, visualizing graph, and intelligent retrieval

## Learning Goals

After you finish dis lesson, you go sabi how to:

• **Differentiate between different types of AI agent memory**, including working, short-term, and long-term memory, plus special kinds like persona and episodic memory.

• **Implement and manage short-term and long-term memory for AI agents** using Microsoft Agent Framework, using tools like Mem0, Cognee, Whiteboard memory, and connect to Azure AI Search.

• **Understand di principles behind self-improving AI agents** and how beta memory management system dey help dem learn and adapt always.

## Understanding AI Agent Memory

For im core, **memory for AI agents na di way dem fit keep and recall information**. Dis information fit be correct detail about one conversation, person choice, tins wey dem don do before, or even patterns wey dem don learn.

If memory no dey, AI applications dey usually stateless, meaning say every time interaction dey start from zero. Dis one dey cause repeated and frustrating experience for user where agent "dey forget" previous gist or choice.

### Why e Important to get Memory?

An agent intelligence dey strongly connected to how e fit remember and use old information. Memory fit make agents:

• **Reflective**: Dem dey learn from wetin don happen before.

• **Interactive**: Dem fit maintain context for ongoing talk.

• **Proactive and Reactive**: Dem fit look forward to needs or answer proper based on historical data.

• **Autonomous**: Dem fit work more independently by using stored knowledge.

Di purpose for putting memory na to make agents more **reliable and capable**.

### Types of Memory

#### Working Memory

Think am like piece of scratch paper wey agent dey use during one task or thought wey dey go on. E dey hold immediate tins wey e need to do next step.

For AI agents, working memory dey capture di most important tins from one conversation, even if full chat history long or cut short. E dey focus on picking key tins like requirements, proposals, decisions, and actions.

**Working Memory Example**

For travel booking agent, working memory fit capture wetin user dey ask now, like "I want to book trip go Paris". Dis demand dey for agent immediate context so e fit guide di current talk.

#### Short Term Memory

Dis kind memory keep tins for just one talk or session. Na di context for that chat wey dey go on so agent fit refer back to tins wey dem talk before for conversation.

For [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK samples, dis na di `AgentSession`, wey dem create wit `agent.create_session()`. Di session na short-term built-in memory for di framework: e dey hold conversation context while session dey go, but e no dey keep dis info when session finish or app start again. Use long-term memory for facts and choice wey suppose last across sessions, usually for one database, vector index, or other permanent store.

**Short Term Memory Example**

If user ask, "How much flight to Paris go cost?" then follow up with "How about place to stay?" short-term memory dey ensure say agent sabi "there" mean "Paris" for same talk.

#### Long Term Memory

Dis na information wey dey last for many talks or sessions. E make agents fit remember user choice, past talks, or general knowledge for long time. Dis one important for personalization.

**Long Term Memory Example**

Long-term memory fit store say "Ben like skiing and outdoor activities, enjoy coffee with mountain view, and no like advanced ski slopes cause e get past injury". Dis info, wey e don learn before, dey affect beta travel plan recommendations for future, make dem personalized.

#### Persona Memory

Dis special memory type dey help agent get consistent "personality" or "persona". E allow agent remember tins about itself or role wey e dey play, to make interaction more smooth and focused.

**Persona Memory Example**
If travel agent design to be "expert ski planner," persona memory fit help reinforce dis role, make im responses align wit expert tone and knowledge.

#### Workflow/Episodic Memory

Dis memory keep sequence of steps wey agent take for one serious task, including success and failure. E be like to remember specific "episodes" or past experience make e learn from dem.

**Episodic Memory Example**

If agent try book particular flight but e no work cause e no get, episodic memory fit record dis failure, so agent fit try other flights or tell user about problem with more correct info for next try.

#### Entity Memory

Dis one na to pick and keep specific entities (people, places, or tins) and events from talk. E allow agent build structured understanding of key tins wey dem yarn.

**Entity Memory Example**

From talk about past trip, agent fit pick "Paris," "Eiffel Tower," and "dinner at Le Chat Noir restaurant" as entities. For future talk, agent fit remember "Le Chat Noir" and offer to book new reservation for there.

#### Structured RAG (Retrieval Augmented Generation)

Even though RAG na broader method, "Structured RAG" na strong memory technology. E dey extract dense, structured info from different sources (talks, emails, images) and use am to make responses more precise, quick and accurate. Unlike old RAG wey rely only for semantic similarity, Structured RAG dey use actual structure of info.

**Structured RAG Example**

Instead of just match keywords, Structured RAG fit parse flight details (where you go, date, time, airline) from email and store am properly. E go fit answer precise questions like "Which flight I book to Paris on Tuesday?"

## Implementing and Storing Memory

To implement memory for AI agents e get one systematic process called **memory management**, wey get to do with making, storing, finding, joining, updating, and even "forgetting" (or deleting) info. Finding back info na very important part.

### Specialized Memory Tools

#### Mem0

One way to store and manage agent memory na to use special tools like Mem0. Mem0 sabi as persistent memory layer, e let agents remember important gist, keep user preferences and facts, and learn from wetin succeed or fail as time dey pass. Idea be say stateless agents go turn stateful.

E dey work through **two-phase memory pipeline: extraction and update**. First, messages wey agent thread get dey sent to Mem0 service, wey use Large Language Model (LLM) to summarize talk history and pick new memories. Then, LLM-driven update phase dey decide if e go add, change, or delete memories, and e dey store those memories inside hybrid data store wey fit get vector, graph, and key-value databases. Dis system fit support many types of memory and e fit use graph memory to manage relationships between entities.

#### Cognee

Another strong way na to use **Cognee**, open-source semantic memory for AI agents wey fit change structured and unstructured data into knowledge graphs backed by embeddings. Cognee get **dual-store architecture** wey dey combine vector similarity search and graph relationships, so agents fit understand not only wetin similar but how concepts dey connect one another.

E good for **hybrid retrieval** wey join vector similarity, graph structure, and LLM reasoning - from raw chunk lookup to graph-aware question answer. Di system get **living memory** wey dey grow, change, but still fit query as one connected graph, supporting both short-term session context and long-term memory wey no loss.

The Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) show how to build this unified memory layer, wit real example of bringing different data inside, visualizing the knowledge graph, and searching with different strategies for agent needs.

### Storing Memory with RAG

Beyond special memory tools like Mem0, you fit use strong search services like **Azure AI Search as backend to keep and find memory**, especially for structured RAG.

Dis one go help ground your agent responses wit your own data, to make answers more relevant and precise. Azure AI Search fit store user travel memory, product catalog, or any other domain knowledge.

Azure AI Search fit support feature like **Structured RAG**, wey dey good for taking dense, structured information from big datasets like talks, emails, or pictures. E get "superhuman precision and recall" when you compare am with old text chunking and embedding methods.

## Making AI Agents Self-Improve

Common method to create self-improving agents na to introduce **"knowledge agent"**. Dis other agent dey watch how user and main agent dey talk. Im role be to:

1. **Identify important tin dem**: Check if any part of talk worthy to save as general knowledge or user preference.

2. **Extract and summarize**: Take important lesson or preference from talk.

3. **Store inside knowledge base**: Keep dis info, usually in vector database, so as to bring am back later.

4. **Support future queries**: When user start new question, knowledge agent go find stored related info and add am to user prompt, give important context to main agent (like RAG).

### Optimizations for Memory

• **Latency Management**: To prevent slow down for user talk, one cheaper, faster model fit use first to check if info important to keep or retrieve, only use complex extraction/retrieval when necessary.

• **Knowledge Base Maintenance**: For big knowledge base, less used info fit move to "cold storage" to save cost.

## You Get More Questions About Agent Memory?

Join [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, join office hours and get your AI Agents questions answered.
## Previous Lesson

[Context Engineering for AI Agents](../12-context-engineering/README.md)

## Next Lesson

[Exploring Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->