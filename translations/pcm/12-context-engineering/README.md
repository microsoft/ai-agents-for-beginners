# Context Engineering for AI Agents

[![Context Engineering](../../../translated_images/pcm/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Click di image wey de above to watch video for dis lesson)_

To sabi di complexity of di application wey you dey build AI agent for dey important to make correct one. We need build AI Agents wey go fit manage information well well to handle complex wahala pass just prompt engineering.

For dis lesson, we go look wetin context engineering be and how e take work for building AI agents.

## Introduction

Dis lesson go cover:

• **Wet in be Context Engineering** and why e different from prompt engineering.

• **Ways to do correct Context Engineering**, including how to write, select, compress, and separate information.

• **Common Context Wahala** wey fit spoil your AI agent and how to fix am.

## Learning Goals

After you finish dis lesson, you go sabi how to:

• **Define context engineering** and sabi how e differ from prompt engineering.

• **Identify main parts of context** for Large Language Model (LLM) applications.

• **Use strategies to write, select, compress, and separate context** to make agent work well.

• **Know common context wahala** like poisoning, distraction, confusion, and clash, and how to solve dem.

## Wetin be Context Engineering?

For AI Agents, context na wetin de control how AI Agent go plan to take action. Context Engineering na di work to make sure say AI Agent get correct information to complete di next step for di task. Di context window get limit size, so as agent builders we need make systems and ways to manage how to add, remove, and compress di information wey dey inside di context window.

### Prompt Engineering vs Context Engineering

Prompt engineering dey focus only on one set of static instructions to guide AI Agents with set of rules. Context engineering na how to manage changing information wey include di first prompt to make sure say AI Agent get wetin e need over time. Di main idea of context engineering na to make dis process fit run again and be trustworthy.

### Types of Context

[![Types of Context](../../../translated_images/pcm/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

E important to remember say context no be just one thing. Di information wey AI Agent need fit come from many different places and na our work to make sure agent fit access all these places:

Di kinds of context AI agent fit need to manage include:

• **Instructions:** Dis dey like di agent "rules" – prompts, system messages, few-shot examples (wey show AI how to do something), and description of tools wey e fit use. Na here prompt engineering and context engineering meet.

• **Knowledge:** Dis cover facts, information wen dem collect from databases, or long-term memories wey agent don get. E fit also include using Retrieval Augmented Generation (RAG) system if agent need to access diff knowledge stores and databases.

• **Tools:** Dis na definitions of external functions, APIs and MCP Servers wey agent fit use, plus feedback (results) wey e dey get from dem.

• **Conversation History:** Na ongoing talk wey dey happen with user. As time dey go, these talks go dey longer and more complex, and e mean say dem go take space for context window.

• **User Preferences:** Information wey dem learn about wetin user like or no like over time. Dem fit store dis kind info and use am when dem dey make important decisions to help user.

## Strategies for Effective Context Engineering

### Planning Strategies

[![Context Engineering Best Practices](../../../translated_images/pcm/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Good context engineering start with good planning. Here na one way wey go help you start to sabi how to apply context engineering:

1. **Define Clear Results** - Results of tasks wey AI Agents go do suppose dey clear. Answer di question - "How di world go be when AI Agent finish im task?" In other words, wetin change, information, or response user go get after dem interact with AI Agent.
2. **Map the Context** - After you don define results for AI Agent, you go need answer di question "Wetin AI Agent need to know to complete dis task?". Dis na how you go start map di context of where di information dey.
3. **Create Context Pipelines** - Now wey you sabi where di information dey, you for answer di question "How Agent go take get dis information?". Dis fit be done in different ways like RAG, using MCP servers, and other tools.

### Practical Strategies

Planning na correct but as information enter our agent context window, we need to get practical strategies to handle am:

#### Managing Context

Even though some information go dey add to context window automatically, context engineering na to take active control for dis information using some strategies:

 1. **Agent Scratchpad**
 Dis allow AI Agent to note down correct information about current tasks and user interactions during one session. E for dey outside di context window for file or runtime object wey agent fit later check for dis session if e need am.

 2. **Memories**
 Scratchpads good to manage information outside of context window for one session. Memories allow agents store and still get correct information across many sessions. This one fit cover summaries, user preferences, and feedback for better work later.

 3. **Compressing Context**
  When context window big and e near limit, you fit use methods like summarization and trimming. Dis fit mean keep only di important information or delete older messages.
  
 4. **Multi-Agent Systems**
  To develop multi-agent system na one way for context engineering because each agent get im own context window. How to share and pass context to different agents na another thing to plan for when you dey build these systems.
  
 5. **Sandbox Environments**
  If agent need run some code or process large information for one document, dis fit take many tokens for process results. Instead of keep all inside context window, agent fit use sandbox environment to run dis code and only read results plus other important info.
  
 6. **Runtime State Objects**
   Dis na to create containers of information to handle situations when Agent need access to certain info. For complex task, dis go allow Agent store results of each small task step by step, make context dey connected only to that small task.

#### Inspecting Context

After you apply one of these strategies, e good to check wetin di next model call really receive. One useful debugging question be:

> Did the agent load too much context, wrong context, or miss context wey e need?

You no need log raw prompts, tool outputs, or memory contents to answer dat question. For production, you should prefer small context inspection records wey capture counts, ids, hashes, and policy labels:

- **Selection:** Track how many candidate chunks, tools, or memories dem check, how many dem pick, and which rule or score make others to dey filter out.
- **Compression:** Record source range or trace id, summary id, estimated token count before and after compression, and whether raw content bin comot from next call.
- **Isolation:** Note which subtask run inside separate agent, session, or sandbox, which summary dem return, and if big tool output remain outside di main agent context.
- **Memory and RAG:** Store retrieval document ids, memory ids, scores, selected ids and redaction status instead of the full retrieved text.
- **Safety and privacy:** Prefer hashes, ids, token buckets, and policy labels above sensitive prompt text, tool arguments, tool results, or user memory bodies.

Di goal no be make you keep more context. Di goal na to leave enough proof wey developer fit tell which context strategy run and whether e change next model call as dem intend.

### Example of Context Engineering

Make we talk say we want AI agent to **"Book me a trip to Paris."**

• Simple agent wey dey use only prompt engineering fit just reply: **"Okay, when you want go Paris?**". E go just process your direct question when user ask am.

• Agent wey use context engineering strategies wey we talk about go do way more. Before e even respond, im system fit:

  ◦ **Check your calendar** for free dates (carry real-time data).

 ◦ **Recall past travel preferences** (from long-term memory) like your preferred airline, budget, or if you like direct flights.

 ◦ **Identify available tools** for flight and hotel booking.

- Then, example response fit be like: "Hey [Your Name]! I see say you free the first week of October. Make I find direct flights to Paris on [Preferred Airline] inside your usual budget of [Budget]?". Dis correct context-aware response show di power of context engineering.

## Common Context Wahala

### Context Poisoning

**Wet in be:** When hallucination (false info wey LLM produce) or error enter context and dem dey reference am plenty times, e fit make agent pursue impossible goals or do nonsense strategies.

**Wetin to do:** Use **context validation** and **quarantine**. Check info before you add to long-term memory. If you find say e fit be poisoning, start fresh context threads to stop bad info from spread.

**Travel Booking Example:** Your agent dey hallucinate **direct flight from one small local airport to far international city** wey no get international flights. Dis fake flight detail dey saved for context. Later, when you ask agent to book, e go dey try find ticket for this impossible route, leading to repeated errors.

**Solution:** Make e get step wey **check if flight really dey and di routes with real-time API** _before_ e add flight detail to agent working context. If check fail, e place wrong info for "quarantine" and no use am again.

### Context Distraction

**Wet in be:** When context too big so model start focus too much on old history instead of wetin e learn during training, e lead to repetitive or useless actions. Models fit start make mistakes even before context window fill up.

**Wetin to do:** Use **context summarization**. Regularly compress info to short summaries, keep important details but remove repeated history. Dis go help reset di focus.

**Travel Booking Example:** You don dey talk plenty about dream travel places for long time, include detailed story about your backpacking trip from two years ago. When you finally ask to **"find me cheap flight for** **next month****,"** agent go confuse with old irrelevant details and e go keep dey ask about your backpacking things or old plans, forget your current request.

**Solution:** After certain turns or when context big, agent suppose **make summary of recent and relevant parts of conversation** – focus on your current travel dates and where you want go – and use that short summary for next LLM call, discard less relevant old chat.

### Context Confusion

**Wet in be:** When too much unnecessary context dey, mostly in form of plenty available tools, e fit make model respond bad or call wrong tools. Smaller models dey prone to dis most.

**Wetin to do:** Use **tool loadout management** with RAG techniques. Store tool descriptions for vector database and pick _only_ most relevant tools for each task. Research show say make tools no pass 30.

**Travel Booking Example:** Your agent get access to plenty tools: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, and others. You ask, **"How best I fit waka for Paris?"** Because of many tools, agent go confuse and fit try call `book_flight` _inside_ Paris, or `rent_car` even when you like public transport, because tool descriptions fit overlap or e no fit sabi which best.

**Solution:** Use **RAG for tool descriptions**. When you ask about waka for Paris, system go dynamically bring _only_ most relevant tools like `rent_car` or `public_transport_info` based on your question, show focused "loadout" of tools to LLM.

### Context Clash

**Wet in be:** When conflicting info dey inside context, e fit cause inconsistent reasoning or bad final responses. Dis dey happen when info come in stages, and early wrong assumptions still dey for context.

**Wetin to do:** Use **context pruning** and **offloading**. Pruning mean remove old or conflicting info as new details come. Offloading mean give model separate "scratchpad" workspace to process info without full context get problem.


**Travel Booking Example:** You first tell your agent, **"I want to fly economy class."** Later for di conversation, you change your mind and talk, **"Actually, for dis trip, make we go business class."** If both instructions still dey for di context, di agent fit get conflicting search results or e fit confuse about which preference to put for front.

**Solution:** Make you do **context pruning**. When new instruction dey contradict old one, di old instruction go comot or dem go override am well for di context. Another way be say di agent fit use **scratchpad** to fix conflicting preferences before e decide, to make sure only di final, correct instruction na im go guide im action.

## You get More Questions About Context Engineering?

Join di [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, attend office hours and make your AI Agents questions get correct answer.
## Previous Lesson

[Agentic Protocols](../11-agentic-protocols/README.md)

## Next Lesson

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->