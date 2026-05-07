[![Intro to AI Agents](../../../translated_images/en/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Click the image above to watch the video for this lesson)_

# Introduction to AI Agents and Agent Use Cases

Welcome to the **AI Agents for Beginners** course! This course gives you the foundational knowledge — and real working code — to start building AI Agents from scratch.

Come say hi in the <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — it's full of learners and AI builders who are happy to answer questions.

Before we jump into building, let's make sure we actually understand what an AI Agent *is* and when it makes sense to use one.

---

## Introduction

This lesson covers:

- What AI Agents are, and the different types that exist
- Which kinds of tasks AI Agents are best suited for
- The core building blocks you'll use when designing an Agentic solution

## Learning Goals

By the end of this lesson, you should be able to:

- Explain what an AI Agent is and how it's different from a regular AI solution
- Know when to reach for an AI Agent (and when not to)
- Sketch out a basic Agentic solution design for a real-world problem

---

## Defining AI Agents and Types of AI Agents

### What are AI Agents?

Here's a simple way to think about it:

> **AI Agents are systems that let Large Language Models (LLMs) actually *do things* — by giving them tools and knowledge to act on the world, not just respond to prompts.**

Let's unpack that a bit:

- **System** — An AI Agent isn't just one thing. It's a collection of parts working together. At its core, every agent has three pieces:
  - **Environment** — The space the agent works in. For a travel booking agent, this would be the booking platform itself.
  - **Sensors** — How the agent reads the current state of its environment. Our travel agent might check hotel availability or flight prices.
  - **Actuators** — How the agent takes action. The travel agent might book a room, send a confirmation, or cancel a reservation.

![What Are AI Agents?](../../../translated_images/en/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agents existed before LLMs, but LLMs are what make modern agents so powerful. They can understand natural language, reason about context, and turn a vague user request into a concrete plan of action.

- **Perform Actions** — Without an agent system, an LLM just generates text. Inside an agent system, the LLM can actually *execute* steps — searching a database, calling an API, sending a message.

- **Access to Tools** — What tools the agent can use depends on (1) the environment it's running in and (2) what the developer chose to give it. A travel agent might be able to search flights but not edit customer records — it's all about what you wire up.

- **Memory + Knowledge** — Agents can have short-term memory (the current conversation) and long-term memory (a customer database, past interactions). The travel agent might "remember" that you prefer window seats.

---

### The Different Types of AI Agents

Not all agents are built the same. Here's a breakdown of the main types, using a travel booking agent as the running example:

| **Agent Type** | **What It Does** | **Travel Agent Example** |
|---|---|---|
| **Simple Reflex Agents** | Follows hard-coded rules — no memory, no planning. | Sees a complaint email → forwards it to customer service. That's it. |
| **Model-Based Reflex Agents** | Keeps an internal model of the world and updates it as things change. | Tracks historical flight prices and flags routes that are suddenly expensive. |
| **Goal-Based Agents** | Has a goal in mind and figures out how to reach it step by step. | Books a full trip (flights, car, hotel) starting from your current location to get you to your destination. |
| **Utility-Based Agents** | Doesn't just find *a* solution — finds the *best* one by weighing tradeoffs. | Balances cost vs. convenience to find the trip that scores highest for your preferences. |
| **Learning Agents** | Gets better over time by learning from feedback. | Adjusts future booking recommendations based on post-trip survey results. |
| **Hierarchical Agents** | A high-level agent breaks work into subtasks and delegates to lower-level agents. | A "cancel trip" request gets split into: cancel flight, cancel hotel, cancel car rental — each handled by a sub-agent. |
| **Multi-Agent Systems (MAS)** | Multiple independent agents working together (or competing). | Cooperative: separate agents handle hotels, flights, and entertainment. Competitive: multiple agents compete to fill hotel rooms at the best price. |

---

## When to Use AI Agents

Just because you *can* use an AI Agent doesn't mean you always *should*. Here are the situations where agents really shine:

![When to use AI Agents?](../../../translated_images/en/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Open-Ended Problems** — When the steps to solve a problem can't be pre-programmed. You need the LLM to figure out the path dynamically.
- **Multi-Step Processes** — Tasks that require using tools across several turns, not just a single lookup or generation.
- **Improvement Over Time** — When you want the system to get smarter based on user feedback or environmental signals.

We'll dig deeper into when (and when *not*) to use AI Agents in the **Building Trustworthy AI Agents** lesson later in the course.

---

## Basics of Agentic Solutions

### Agent Development

The first thing you do when building an agent is define *what it can do* — its tools, actions, and behaviors.

In this course, we use the **Azure AI Agent Service** as our main platform. It supports:

- Open models like OpenAI, Mistral, and Llama
- Licensed data from providers like Tripadvisor
- Standardized OpenAPI 3.0 tool definitions

### Agentic Patterns

You communicate with LLMs through prompts. With agents, you can't always hand-craft every prompt manually — the agent needs to take action across many steps. That's where **Agentic Patterns** come in. They're reusable strategies for prompting and orchestrating LLMs in a more scalable, reliable way.

This course is structured around the most common and useful agentic patterns.

### Agentic Frameworks

Agentic Frameworks give developers ready-made templates, tools, and infrastructure for building agents. They make it easier to:

- Wire up tools and capabilities
- Observe what the agent is doing (and debug when it goes wrong)
- Collaborate across multiple agents

In this course, we focus on the **Microsoft Agent Framework (MAF)** for building production-ready agents.

---

## Code Samples

Ready to see it in action? Here are the code samples for this lesson:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Got Questions?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to connect with other learners, attend office hours, and get your AI Agent questions answered by the community.

---

## Previous Lesson

[Course Setup](../00-course-setup/README.md)

## Next Lesson

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->