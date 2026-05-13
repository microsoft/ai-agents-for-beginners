[![Intro to AI Agents](../../../translated_images/pcm/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Click di piksha wey dey above to watch di video for dis lesson)_

# Introduction to AI Agents and Agent Use Cases

Welcome to di **AI Agents for Beginners** course! Dis course go give you di basic sabi — plus real workin code — to start build AI Agents from scratch.

Come greet for <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — e full with learners and AI builders wey dey happy to answer questions.

Before we begin to build, mek we make sure say we really understand wetin AI Agent *be* and when e make sense to use am.

---

## Introduction

Dis lesson go cover:

- Wetin AI Agents be, and di different kain wey dey
- Which kain tasks AI Agents dey best for
- Di main building blocks wey you go use when you dey design Agentic solution

## Learning Goals

By di end of dis lesson, you suppose fit:

- Explain wetin AI Agent be and how e different from normal AI solution
- Know when to choose AI Agent (and when no to)
- Draw small basic Agentic solution design for real-world wahala

---

## Defining AI Agents and Types of AI Agents

### Wetin be AI Agents?

Na so simple way to think am be this:

> **AI Agents na systems wey dey make Large Language Models (LLMs) actually *do tins* — by giving dem tools and knowledge to act for di world, no be only answer prompts.**

Make we break am down small:

- **System** — AI Agent no be only one tin. E be collection of parts wey dey work together. Every agent get three main parts:
  - **Environment** — Di space wey di agent dey work. For travel booking agent, na di booking platform e go be.
  - **Sensors** — How di agent dey read di current state of im environment. Our travel agent fit check hotel availability or flight price.
  - **Actuators** — How di agent go take do tins. Di travel agent fit book room, send confirmation, or cancel booking.

![What Are AI Agents?](../../../translated_images/pcm/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agents dey before LLMs, but na LLMs dey make modern agents strong. Dem fit understand natural language, reason about context, and change vague user request to clear plan.

- **Perform Actions** — Without agent system, LLM go just generate text. But inside agent system, LLM fit actually *do* steps — search database, call API, send message.

- **Access to Tools** — Wetin tools agent fit use depend on (1) di environment wey e dey run and (2) wetin developer decide to give am. Travel agent fit search flights but no fit edit customer record — na wetin you connect gidigba.

- **Memory + Knowledge** — Agents fit get short-term memory (current conversation) and long-term memory (customer database, past interactions). Travel agent fit "remember" say you like window seat.

---

### Different Types of AI Agents

No be all agents be the same. See di breakdown of main types, using travel booking agent as example:

| **Agent Type** | **Wet E Dey Do** | **Travel Agent Example** |
|---|---|---|
| **Simple Reflex Agents** | Dey follow hard-coded rules — no memory, no planning. | See complaint email → forward am to customer service. Na all. |
| **Model-Based Reflex Agents** | Get internal model of di world and dey update am as tins change. | Track flight price history and warn when prices high well well. |
| **Goal-Based Agents** | Get goal and dey find how to reach am step by step. | Book full trip (flights, car, hotel) from your current location go your destination. |
| **Utility-Based Agents** | No just find *one* solution — find *best* one by weighing tradeoffs. | Balance cost versus convenience to get trip wey best fit your choice. |
| **Learning Agents** | Dey improve over time by learning from feedback. | Change future booking tips based on survey after trip. |
| **Hierarchical Agents** | Top-level agent break work into small tasks and give to sub-agents. | "Cancel trip" split into: cancel flight, cancel hotel, cancel car rental — each done by sub-agent. |
| **Multi-Agent Systems (MAS)** | Many independent agents dey work together (or compete). | Cooperative: separate agents handle hotels, flights, and entertainment. Competitive: many agents compete to fill hotel rooms at best price. |

---

## When to Use AI Agents

Just because you fit use AI Agent no mean say you suppose always use am. Dis na tins wey agents really shine:

![When to use AI Agents?](../../../translated_images/pcm/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Open-Ended Problems** — When steps to solve wahala no fit pre-program. You need LLM to find path dynamically.
- **Multi-Step Processes** — Tasks wey need tools at many turns, no be just one quick search or generation.
- **Improvement Over Time** — When you want system to become smarter based on user feedback or environment signals.

We go talk more about when (and when *no* to) use AI Agents inside **Building Trustworthy AI Agents** lesson later.

---

## Basics of Agentic Solutions

### Agent Development

First tin you go do to build agent na to define *wetin e fit do* — e tools, actions, and behaviors.

For dis course, we dey use **Azure AI Agent Service** as main platform. E support:

- Models from providers like OpenAI, Mistral, and Meta (Llama)
- Licensed data from providers like Tripadvisor
- Standardized OpenAPI 3.0 tool definitions

### Agentic Patterns

You dey talk with LLMs through prompts. With agents, you no fit always design every prompt by hand — agent need to act in many steps. Na so **Agentic Patterns** from. Dem be reusable strategies for prompting and arranging LLMs well well.

Dis course na around di most common and useful agentic patterns.

### Agentic Frameworks

Agentic Frameworks dey give developers ready-made templates, tools, and setup to build agents. Dem make am easier to:

- Connect tools and capabilities
- Check wetin agent dey do (and debug when e no work)
- Work together with many agents

For dis course, we focus on **Microsoft Agent Framework (MAF)** for building ready-for-production agents.

---

## Code Samples

Ready to see am work? Here be code samples for dis lesson:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Got Questions?

Join [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to connect with other learners, attend office hours, and get your AI Agent questions answered by community.

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