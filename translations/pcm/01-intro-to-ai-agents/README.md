[![Intro to AI Agents](../../../translated_images/pcm/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Click di image wey dey top so make you watch di video for dis lesson)_

# Introdakshon to AI Agents and Agent Use Cases

Welcome to di **AI Agents for Beginners** course! Dis course dey give you di basic tin dem — plus real working code — to start to build AI Agents from ground up.

Come greet us for <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — e full with learners and AI builders wey dey happy to answer any question.

Before we start to build, mek we sure say we actually sabi wetin AI Agent *be* and when e make sense to use am.

---

## Introdakshon

Dis lesson dey cover:

- Wetin AI Agents be, and di different kain wey dey exist
- Which kain task AI Agents sabi do well
- Di main building blocks wey you go use when you dey design Agentic solution

## Learning Goals

By di end of dis lesson, you go fit:

- Talk say wetin AI Agent be and how e different from regular AI solution
- Know when to use AI Agent (and when e no good)
- Draw basic Agentic solution design for real-world problem

---

## Defining AI Agents and Types of AI Agents

### Wetin be AI Agents?

Dis na simple way to think am:

> **AI Agents na systems wey dey allow Large Language Models (LLMs) to actually *do things* — by giving dem tools and knowledge to act on di world, no be only to respond to prompts.**

Make we break am down small:

- **System** — AI Agent no be just one tin. E be collection of parts wey dey work together. For di core, every agent get three pieces:
  - **Environment** — Di place wey di agent dey work. For travel booking agent, na di booking platform itself.
  - **Sensors** — How di agent dey read di current state of di environment. Our travel agent fit check hotel availability or flight prices.
  - **Actuators** — How di agent dey take action. Di travel agent fit book room, send confirmation, or cancel reservation.

![Wetin Be AI Agents?](../../../translated_images/pcm/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agents dey exist before LLMs, but na LLMs dey make modern agents powerful. Dem fit understand natural language, reason about context, and turn vague user request to concrete plan of action.

- **Perform Actions** — Without agent system, LLM just generate text. Inside agent system, di LLM fit *execute* steps — search database, call API, send message.

- **Access to Tools** — Di tools wey di agent fit use depend on (1) environment wey e dey run and (2) wetin di developer decide to give am. Travel agent fit search flights but no fit edit customer records — na wetin you wire up e be.

- **Memory + Knowledge** — Agents fit get short-term memory (di current conversation) and long-term memory (customer database, past interactions). Di travel agent fit "remember" say you like window seats.

---

### Di Different Kain AI Agents

No all agents be the same. Dis na breakdown of main types, using travel booking agent as example:

| **Agent Type** | **Wetn e Dey Do** | **Travel Agent Example** |
|---|---|---|
| **Simple Reflex Agents** | E follow hard-coded rules — no memory, no planning. | If e see complaint email → e go forward am go customer service. Na only dat. |
| **Model-Based Reflex Agents** | E keep internal model of world and e update am as tins dey change. | E dey track historical flight prices, e go flag routes wey suddenly expensive. |
| **Goal-Based Agents** | E get goal and e dey figure how to reach am step by step. | E go book full trip (flight, car, hotel) from where you dey to your destination. |
| **Utility-Based Agents** | E no go only find *one* solution — e find *best* one by weighing pros and cons. | E balance cost with convenience to find trip wey fit your preference pass all. |
| **Learning Agents** | E dey improve as time dey go by learning from feedback. | E go adjust future booking recommendation based on survey after trip. |
| **Hierarchical Agents** | High-level agent go break work into smaller tasks then e give to lower-level agents. | If person ask "cancel trip", e go split am into: cancel flight, cancel hotel, cancel car rental — each one to different sub-agent. |
| **Multi-Agent Systems (MAS)** | Many independent agents dey work together (or compete). | Cooperative: separate agents dey handle hotels, flights, entertainment. Competitive: many agents dey compete to fill hotel rooms at best price. |

---

## When to Use AI Agents

Just because you fit use AI Agent no mean say you suppose always use am. Dis na some situations wey agents really shine:

![When to use AI Agents?](../../../translated_images/pcm/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Open-Ended Problems** — When you no fit pre-program steps to solve di problem. You need di LLM to find wetin to do dynamically.
- **Multi-Step Processes** — Tasks wey require using tools for many turns, no be just one lookup or generate.
- **Improvement Over Time** — When you want system to dey smarter based on user feedback or environment signals.

We go talk more about when (and when *no*) to use AI Agents for **Building Trustworthy AI Agents** lesson for dis course later.

---

## Basics of Agentic Solutions

### Agent Development

Di first tin you go do when you dey build agent na to define *wetin e fit do* — e tools, actions, and behaviors.

For dis course, we dey use **Microsoft Foundry Agent Service** as main platform. E support:

- Models from providers like OpenAI, Mistral, and Meta (Llama)
- Licensed data from providers like Tripadvisor
- Standardized OpenAPI 3.0 tool definitions

### Agentic Patterns

You dey communicate with LLMs through prompts. With agents, you no fit always craft every prompt manually — di agent need to take action steps many times. Na there **Agentic Patterns** come. Dem be reusable strategies for prompting and managing LLMs way wey dey scalable and reliable.

Dis course structure dey focus on di most common and useful agentic patterns.

### Agentic Frameworks

Agentic Frameworks dey give developers ready-made templates, tools, and infrastructure to build agents. Dem dey make am easy to:

- Wire tools and capabilities together
- Watch wetin agent dey do (and debug if e get problem)
- Collaborate across many agents

For dis course, we dey focus on **Microsoft Agent Framework (MAF)** for building ready-for-production agents.

---

## Code Samples

Ready to see am for action? Here be code samples for dis lesson:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## You Get Questions?

Join the [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to connect with other learners, attend office hours, and make community answer your AI Agent questions.


---

## Smoke-Test Dis Agent (Optional)

Once you learn how to deploy agents for [Lesson 16](../16-deploying-scalable-agents/README.md), you fit add quick post-deploy health check for dis lesson's `TravelAgent` with ready-made catalog [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Check [`tests/README.md`](../tests/README.md) to find how to run am.

---

## Previous Lesson

[Course Setup](../00-course-setup/README.md)

## Next Lesson

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->