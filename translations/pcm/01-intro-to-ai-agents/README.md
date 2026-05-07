[![Intro to AI Agents](../../../translated_images/pcm/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik di piksha wey dey up dere to watch di video for dis lekshan)_

# Introduction to AI Agents and Agent Use Cases

Welcome to di **AI Agents for Beginners** course! Dis course go gi you di basic knowledge — plus real working code — to start to build AI Agents from scratch.

Make you come greet for di <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — e full of learners and AI builders wey happy to answer questions.

Bifor we start to build, make we sure say we sabi wetin be AI Agent *be* and wen e make sense to use one.

---

## Introduction

Dis lekshan cover:

- Wetin AI Agents be, and di different types wey dey
- Which kind tasks AI Agents dey best for
- Di main building blocks wey you go use wen you dey design one Agentic solution

## Learning Goals

By di end of dis lekshan, you go fit:

- Explain wetin AI Agent be and how e different from regular AI solution
- Know wen to reach for AI Agent (and wen no to)
- Sketch out basic Agentic solution design for real-world wahala

---

## Defining AI Agents and Types of AI Agents

### Wetin be AI Agents?

Dis na simple way to think am:

> **AI Agents na systems wey make Large Language Models (LLMs) actually *do tins* — by giving dem tools and knowledge to act for di world, no be only to respond to prompts.**

Make we unpack am small:

- **System** — AI Agent no be just one tin. E dey made up of parts wey dey work together. For e core, every agent get three parts:

  - **Environment** — Di space wey di agent dey work inside. For travel booking agent, na di booking platform itself be dat.

  - **Sensors** — How di agent dey read di current state of im environment. Our travel agent fit check hotel availability or flight prices.

  - **Actuators** — How di agent dey take action. Di travel agent fit book room, send confirmation, or cancel reservation.

![What Are AI Agents?](../../../translated_images/pcm/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agents dey before LLMs, but na LLMs dey make modern agents powerful. Dem fit understand natural language, reason about context, and turn vague user request to solid plan of action.

- **Perform Actions** — Without agent system, LLM just dey generate text. But inside agent system, LLM fit *execute* steps — search database, call API, send message.

- **Access to Tools** — Di tools wey agent fit use depend on (1) di environment wey e dey run and (2) wetin di developer choose to give am. Travel agent fit search flights but no fit edit customer record — na wetin you wire up.

- **Memory + Knowledge** — Agents fit get short-term memory (di current conversation) and long-term memory (customer database, past interactions). Travel agent fit "remember" say you like window seats.

---

### Di Different Types of AI Agents

No be all agents dem build di same way. Below na di main types, using travel booking agent as example:

| **Agent Type** | **Wetin E Dey Do** | **Travel Agent Example** |
|---|---|---|
| **Simple Reflex Agents** | E dey follow code rules — no memory, no planning. | When e see complaint email → e send am go customer service. Na so e go. |
| **Model-Based Reflex Agents** | E keep internal model of di world and dey update am as tins change. | E dey track historical flight prices and dey flag routes wey sudden expensive. |
| **Goal-Based Agents** | E get goal and dey find how to reach am step by step. | E fit book full trip (flights, car, hotel) from where you dey go your destination. |
| **Utility-Based Agents** | No just find *one* solution — e go find *best* one by weighing tradeoffs. | E balance cost vs. convenience to find trip wey best match your preferences. |
| **Learning Agents** | E dey improve over time by learning from feedback. | E dey adjust future booking recommendations based on survey after trip. |
| **Hierarchical Agents** | High-level agent go break work into small tasks and give lower-level agents. | To "cancel trip" request, e go split am: cancel flight, cancel hotel, cancel car rental — each na different sub-agent. |
| **Multi-Agent Systems (MAS)** | Many independent agents dey work together (or compete). | Cooperative: different agents dey handle hotels, flights, entertainment. Competitive: plenty agents dey compete to fill hotel rooms at best price. |

---

## Wen to Use AI Agents

No be because you fit use AI Agent mean say you suppose always use am. These na tins wey agents dey shine for:

![When to use AI Agents?](../../../translated_images/pcm/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Open-Ended Problems** — Wen di steps to solve problem no fit pre-program. You need LLM to figure path dynamically.

- **Multi-Step Processes** — Tasks wey need use tools for many steps, no be one-time lookup or generation.

- **Improvement Over Time** — Wen you want system to sabi more based on user feedback or environment signals.

Later for di course, we go dey go deeper into wen (and wen *no*) to use AI Agents for **Building Trustworthy AI Agents** lekshan.

---

## Basics of Agentic Solutions

### Agent Development

Di first tin you go do wen you dey build agent na to define *wetin e fit do* — im tools, actions, and behaviours.

For dis course, we dey use **Azure AI Agent Service** as main platform. E support:

- Open models like OpenAI, Mistral, and Llama
- Licensed data from providers like Tripadvisor
- Standardized OpenAPI 3.0 tool definitions

### Agentic Patterns

You dey communicate with LLMs through prompts. With agents, you no fit hand-write every prompt — di agent need to take action across many steps. Na di **Agentic Patterns** dem dey use. Dem be reusable strategies for prompting and controlling LLMs in bigger, more reliable way.

Dis course na about di most common and useful agentic patterns.

### Agentic Frameworks

Agentic Frameworks dey give developers ready-made templates, tools, and infrastructure to build agents. E make am easier to:

- Wire up tools and capabilities
- Observe wetin di agent dey do (and debug wen e go wrong)
- Collaborate across many agents

For dis course, we focus on **Microsoft Agent Framework (MAF)** to build production-ready agents.

---

## Code Samples

You ready to see how e dey work? Here be di code samples for dis lekshan:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Got Questions?

Join di [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to connect with other learners, attend office hours, and get your AI Agent questions answered by di community.

---

## Previous Lesson

[Course Setup](../00-course-setup/README.md)

## Next Lesson

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg know say automated translation fit get some errors or wahala. Di original document for im own language na di correct source. For important information, better human professional translation betta. We no go responsible for any misunderstanding or incorrect meaning wey fit dey because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->