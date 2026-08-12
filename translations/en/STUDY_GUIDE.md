# AI Agents for Beginners - Study Guide

Use this guide as a practical companion while you move through the course. It is
not meant to replace the lessons. It helps you decide where to start, what to
look for in each lesson, and how to connect the ideas into a small working agent
demo.

If this is your first time here, start simple:

1. Read the [Course Setup](./00-course-setup/README.md).
2. Complete Lessons 01-06 in order.
3. Keep one small demo idea in mind as you learn.
4. After each lesson, ask: "What can my agent do now that it could not do
   before?"

## A Simple Demo To Keep In Mind

A good way to learn agents is to follow one demo idea through the course.

Example demo: **a course helper agent**.

The user asks:

> "I want to learn how agents use tools. Find the right lessons, summarize what
> I should read first, and give me a short practice task."

A regular chatbot can answer from what it already knows. An agent can do more:

1. **Read or search course files** to find the right lessons.
2. **Use tools** to retrieve lesson links, examples, or supporting material.
3. **Plan** a short learning path instead of giving one long answer.
4. **Use context** from the current conversation to stay focused on the learner's
   goal.
5. **Remember useful preferences** if the application supports memory.
6. **Show traces, citations, or logs** so the user can understand what happened.
7. **Apply guardrails** before taking risky actions or using sensitive data.

As you study each lesson, come back to this demo and ask: what new capability
would this lesson add?

## What You Are Building Toward

By the end of the course, you should be able to explain and build agent systems
that combine these parts:

| Part | Plain-language meaning | In the demo |
|------|------------------------|-------------|
| Model | The reasoning engine that interprets the user's request | Understands that the learner wants lessons about tool use |
| Tools | Functions, APIs, files, browsers, or services the agent can use | Searches the repo or retrieves lesson content |
| Knowledge | Documents or data used to ground the answer | Course README files and lesson material |
| Context | Information included in the next model call | The user's goal and the tool results |
| Memory | Information saved for later use | The learner prefers hands-on Python examples |
| Planning | Breaking a larger goal into smaller steps | Find lessons, summarize them, suggest practice |
| Orchestration | Routing work across tools, steps, or agents | A planner calls a search tool, then a summarizer |
| Trust | Safety, security, evaluation, and observability | Logs tool calls and asks before high-impact actions |

## Models and Providers

The course code samples use the **Microsoft Agent Framework (MAF)** and target the **Azure OpenAI Responses API** — the recommended API going forward, which combines chat completions, tool calling, multimodal input, and stateful conversations in a single API surface. You connect either through a **Microsoft Foundry** project (with `FoundryChatClient`) or to Azure OpenAI directly (with `OpenAIChatClient`).

As you work through the lessons, you have a few provider options:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — the primary path used across the lessons. Sign in with `az login` for keyless Entra ID authentication.
- **Foundry Local** — run models fully on-device through an OpenAI-compatible API (no cloud, no API keys). Ideal for offline or cost-free experimentation. See [Course Setup](./00-course-setup/README.md).
- **MiniMax** — an OpenAI-compatible provider with large-context models, usable as a drop-in alternative.

> **Note:** GitHub Models is deprecated (retiring July 2026) and does not support the Responses API. The samples have been updated to use Azure OpenAI / Microsoft Foundry instead.

## Choose Your Learning Path

You can take the full course in order, or jump to a path based on what you want
to build.

| If your goal is to... | Start with | Then study |
|-----------------------|------------|------------|
| Understand what agents are | 01, 02, 03 | 04, 05, 06 |
| Build an agent that uses tools | 04 | 05, 07, 14 |
| Build a RAG-based agent | 05 | 04, 06, 12 |
| Design multi-step workflows | 07 | 08, 09, 14 |
| Understand multi-agent systems | 08 | 07, 09, 11 |
| Prepare agents for production | 06, 10 | 12, 13, 16, 18 |
| Deploy and scale agents on Foundry | 10, 16 | 06, 13, 18 |
| Build local / offline-first agents | 17 | 04, 05, 11 |
| Explore protocols and browser automation | 11, 15 | 10, 18 |

Tip: if you are new to agents, do not skip Lessons 01-06. They give you the
vocabulary you will need for the rest of the course.

## Lesson-by-Lesson Guide

| Lesson | What you learn | Try this after the lesson |
|--------|----------------|---------------------------|
| [01 - Intro to AI Agents](./01-intro-to-ai-agents/README.md) | What makes an agent different from a basic chatbot. | Explain your demo idea as an agent, not just a chat app. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | How frameworks help with models, tools, state, and workflows. | Identify which parts of your demo a framework would manage. |
| [03 - Agentic Design Patterns](./03-agentic-design-patterns/README.md) | Common patterns for designing agent behavior. | Sketch the user journey before writing code. |
| [04 - Tool Use](./04-tool-use/README.md) | How agents call tools to get data or take action. | Define one tool your demo agent would need. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | How retrieval grounds agent answers in documents or data. | Decide what knowledge source your demo should search. |
| [06 - Trustworthy Agents](./06-building-trustworthy-agents/README.md) | How to add guardrails, oversight, and safer behavior. | Add one rule for when the agent should ask the user first. |
| [07 - Planning Design](./07-planning-design/README.md) | How agents break larger goals into smaller steps. | Write a three-step plan for your demo request. |
| [08 - Multi-Agent Design](./08-multi-agent/README.md) | When to split work across specialized agents. | Decide whether your demo needs one agent or several. |
| [09 - Metacognition](./09-metacognition/README.md) | How agents can review and improve their own output. | Add a final self-check before the agent responds. |
| [10 - AI Agents in Production](./10-ai-agents-production/README.md) | What changes when an agent moves from demo to production. | List what you would monitor: quality, cost, latency, failures. |
| [11 - Agentic Protocols](./11-agentic-protocols/README.md) | How protocols connect agents to tools and other agents. | Identify where a standard protocol could simplify integration. |
| [12 - Context Engineering](./12-context-engineering/README.md) | How to select, trim, isolate, and manage context. | Decide what belongs in the prompt and what should stay out. |
| [13 - Agent Memory](./13-agent-memory/README.md) | How agents can save useful information across interactions. | Choose one safe preference your demo could remember. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Framework-specific building blocks for agents and workflows, plus hosting LangChain/LangGraph agents on Microsoft Foundry. | Map your demo steps to framework concepts. |
| [15 - Computer Use Agents](./15-browser-use/README.md) | How agents can interact with browser or UI surfaces, including real-world examples like Microsoft Project Opal. | Pick one browser task that should still require user confirmation. |
| [16 - Deploying Scalable Agents](./16-deploying-scalable-agents/README.md) | How to take an agent from prototype to a scalable, observable production deployment on Microsoft Foundry (hosted agents, model routing, caching, evaluation gates, smoke tests). | List the production concerns your demo still needs: hosting, routing, cost, evaluation. |
| [17 - Creating Local AI Agents](./17-creating-local-ai-agents/README.md) | How to build local-first agents that run entirely on your machine with Foundry Local and Qwen (local tools, local RAG, local MCP). | Decide which parts of your demo should stay private and run locally. |
| [18 - Securing AI Agents](./18-securing-ai-agents/README.md) | How to make agent actions more auditable and tamper-evident. | Decide what actions in your demo should be logged or receipted. |

## Validating Deployed Agents with Smoke Tests

When you deploy an agent (Lesson 16), a **smoke test** is the cheapest first
check that the deployment actually answers. This repo ships ready-to-run
catalogs under [tests/](./tests/README.md) for the deployable agents in Lessons
01, 04, 05, and 16, wired to the
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Action. Run them from the **Actions** tab after deploying the lesson's agent.
Smoke tests are a first gate — offline and online evaluation (Lessons 10 and 16)
tell you how *good* the agent is.

## Key Ideas In Beginner-Friendly Terms

### Tools

A tool is something the agent can call to do work outside the model. A good tool
has a clear name, a narrow job, typed inputs, predictable output, and a safe way
to fail.

For the course helper demo, a tool might be:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG and Knowledge

RAG helps the agent answer from source material instead of guessing. In this
course, that source material could be lesson READMEs, code samples, or external
resources linked from the lessons.

Use RAG when the answer should be grounded in documents, data, or current
project files.

### Planning

Planning is useful when the request has more than one step. Keep plans short and
visible enough for a developer or user to inspect.

For the demo, a plan might be:

1. Find lessons related to tool use.
2. Summarize the most relevant lessons.
3. Recommend one practice task.

### Context

Context is what the model sees right now. Too little context can make the agent
miss important details. Too much context can make the agent slower, more costly,
or easier to confuse.

Good context engineering means choosing the right information for the next model
call.

### Memory

Memory is information saved for later. Do not save everything. Save information
only when it is useful, safe, and easy to update or delete.

For example, remembering "the learner prefers Python examples" may be useful.
Remembering sensitive personal data usually is not.

### Evaluation and Observability

Evaluation asks: did the agent do the right thing?

Observability asks: can we see how it happened?

For production agents, keep track of model calls, tool calls, retrieved context,
latency, cost, failures, and user feedback.

### Trust and Security

Trustworthy agents need more than a helpful prompt. Use least-privilege tools,
human approval for high-impact actions, data redaction where needed, and logs or
receipts for actions that must be audited.

## A 15-Minute Review Routine

Use this routine after each lesson:

1. **Summarize the lesson in one sentence.**
2. **Name the new agent capability.** For example: tool use, retrieval,
   planning, memory, observability, or security.
3. **Add it to the course helper demo.** What changes in the demo now?
4. **Find the risk.** What could go wrong if this capability is misused?
5. **Write one test question.** How would you check that the agent behaves well?

## Quick Self-Check

Before moving on, try answering these questions:

1. What can an agent do that a regular chatbot cannot do by itself?
2. What tool would your agent need first, and why?
3. What knowledge source should ground the agent's answer?
4. What context should be included in the next model call?
5. What should the agent remember, and what should it avoid storing?
6. When should the agent ask for human approval?
7. What logs, traces, or receipts would help you debug or audit the agent later?


## Suggested Capstone Exercise

At the end of the course, build a small agent that helps a learner navigate this
repository.

Minimum version:

- Accept a topic from the user.
- Find the most relevant lessons.
- Summarize what to read first.
- Suggest one hands-on practice task.
- Show which lesson files or links were used.

Stretch version:

- Remember the learner's preferred programming language.
- Use a simple plan before answering.
- Add a self-check step before the final response.
- Log tool calls and retrieved sources.
- Ask for confirmation before opening browser or UI automation tasks.

This gives you a small but realistic way to practice tools, RAG, planning,
context, memory, observability, and trust in one project.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->