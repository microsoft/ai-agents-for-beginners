# AI Agents for Beginners - Study Guide

Use dis guide as beta practical companion while you dey move through di course. E no
suppose replace di lessons. E dey help you decide where to start, wetin to
look for for each lesson, and how to join di ideas make small working agent
demo.

If dis na your first time here, start simple:

1. Read di [Course Setup](./00-course-setup/README.md).
2. Complete Lessons 01-06 for order.
3. Keep one small demo idea for mind as you dey learn.
4. After each lesson, ask: "Wetyn my agent fit do now wey e no fit do
   before?"

## Simple Demo To Keep For Mind

One beta way to learn agents na to follow one demo idea through di course.

Example demo: **course helper agent**.

User go ask:

> "I want make I learn how agents dey use tools. Find correct lessons, summarize wetin
> I suppose read first, and give me one short practice task."

Normal chatbot fit answer from wetin e sabi. Agent fit do more:

1. **Read or search course files** to find correct lessons.
2. **Use tools** to find lesson links, examples, or supporting material.
3. **Plan** short learning path instead of to give one long answer.
4. **Use context** from di current talk to stay focused on wetin di learner
   want.
5. **Remember useful preferences** if di app get memory.
6. **Show traces, citations, or logs** so that user go fit understand wetin happen.
7. **Apply guardrails** before to do risky action or to use sensitive data.

As you dey study each lesson, comot come back to dis demo and ask: wetin new skill
this lesson go add?

## Wetin You Dey Build To

By di end of course, you suppose fit explain and build agent system dem wey
combine dis parts:

| Part | Plain-language meaning | For di demo |
|------|------------------------|-------------|
| Model | Di reasoning engine wey go interpret di user's request | Understand say di learner want lessons about tool use |
| Tools | Functions, APIs, files, browsers, or services wey di agent fit use | Search di repo or bring lesson content |
| Knowledge | Documents or data wey dem use ground di answer | Course README files and lesson material |
| Context | Information wey dey inside di next model call | Di user's goal and di tool results |
| Memory | Information wey dem save for later use | Di learner dey like hands-on Python examples |
| Planning | Break bigger goal into small steps | Find lessons, summarize dem, suggest practice |
| Orchestration | Route work across tools, steps, or agents | Planner call search tool, then summarizer |
| Trust | Safety, security, evaluation, and observability | Log tool calls and ask before high-impact actions |

## Models and Providers

Di course code samples dey use **Microsoft Agent Framework (MAF)** and e target **Azure OpenAI Responses API** — di API wey dem recommend to use forward, wey combine chat completions, tool calling, multimodal input, and stateful conversations all for one API surface. You fit connect through **Microsoft Foundry** project (with `FoundryChatClient`) or to Azure OpenAI direct (with `OpenAIChatClient`).

As you dey work through di lessons, you get few provider options:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — na di main path wey dem dey use for all di lessons. Sign in with `az login` for keyless Entra ID authentication.
- **Foundry Local** — run models fully on-device through OpenAI-compatible API (no cloud, no API keys). Beta for offline or cost-free experiment. See [Course Setup](./00-course-setup/README.md).
- **MiniMax** — OpenAI-compatible provider with large-context models, wey you fit use as drop-in alternative.

> **Note:** GitHub Models don retire (retiring July 2026) and e no dey support di Responses API again. Di samples don update to use Azure OpenAI / Microsoft Foundry instead.

## Choose Your Learning Path

You fit take full course for order or jump to path wey match wetin you want
build.

| If your goal na to... | Start with | Then study |
|-----------------------|------------|------------|
| Understand wetin agents be | 01, 02, 03 | 04, 05, 06 |
| Build agent wey dey use tools | 04 | 05, 07, 14 |
| Build RAG-based agent | 05 | 04, 06, 12 |
| Design multi-step workflows | 07 | 08, 09, 14 |
| Understand multi-agent systems | 08 | 07, 09, 11 |
| Prepare agents for production | 06, 10 | 12, 13, 16, 18 |
| Deploy and scale agents for Foundry | 10, 16 | 06, 13, 18 |
| Build local / offline-first agents | 17 | 04, 05, 11 |
| Explore protocols and browser automation | 11, 15 | 10, 18 |

Tip: If you be new to agents, no skip Lessons 01-06. Dem go give you di
vocabulary wey you go need for di rest of di course.

## Lesson-by-Lesson Guide

| Lesson | Wetin you go learn | Try dis one after lesson finish |
|--------|-----------------|-----------------------------|
| [01 - Intro to AI Agents](./01-intro-to-ai-agents/README.md) | Wetin make agent different from ordinary chatbot. | Explain your demo idea as agent, no be just chat app. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | How frameworks dey help with models, tools, state, and workflows. | Identify which parts of your demo framework go manage. |
| [03 - Agentic Design Patterns](./03-agentic-design-patterns/README.md) | Common pattern for designing agent behavior. | Sketch user journey before you write code. |
| [04 - Tool Use](./04-tool-use/README.md) | How agents dey call tools to get data or do action. | Define one tool wey your demo agent go need. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | How retrieval dey ground agent answers in documents or data. | Decide wetin knowledge source your demo go search. |
| [06 - Trustworthy Agents](./06-building-trustworthy-agents/README.md) | How to add guardrails, oversight, and safer behavior. | Add one rule wen agent must ask user first. |
| [07 - Planning Design](./07-planning-design/README.md) | How agents dey break big goals into small steps. | Write three-step plan for your demo request. |
| [08 - Multi-Agent Design](./08-multi-agent/README.md) | When to share work across specialised agents. | Decide if your demo need one or more agent. |
| [09 - Metacognition](./09-metacognition/README.md) | How agents fit review and improve their own output. | Add final self-check before agent respond. |
| [10 - AI Agents in Production](./10-ai-agents-production/README.md) | Wetin change when agent move from demo go production. | List wetin you go monitor: quality, cost, latency, failures. |
| [11 - Agentic Protocols](./11-agentic-protocols/README.md) | How protocols connect agents to tools and other agents. | Identify where standard protocol fit simplify integration. |
| [12 - Context Engineering](./12-context-engineering/README.md) | How to select, trim, isolate, and manage context. | Decide wetin suppose dey for prompt and wetin no suppose. |
| [13 - Agent Memory](./13-agent-memory/README.md) | How agents fit save useful information across interaction. | Choose one safe preference your demo fit remember. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Framework-specific building blocks for agents and workflows, plus hosting LangChain/LangGraph agents on Microsoft Foundry. | Map your demo steps to framework concepts. |
| [15 - Computer Use Agents](./15-browser-use/README.md) | How agents fit interact with browser or UI surfaces, plus real-world example like Microsoft Project Opal. | Pick one browser task wey still go need user confirmation. |
| [16 - Deploying Scalable Agents](./16-deploying-scalable-agents/README.md) | How to turn agent from prototype to big, observable production for Microsoft Foundry (hosted agents, model routing, caching, evaluation gates, smoke tests). | List production worries your demo still get: hosting, routing, cost, evaluation. |
| [17 - Creating Local AI Agents](./17-creating-local-ai-agents/README.md) | How to build local-first agents wey run fully for your machine with Foundry Local and Qwen (local tools, local RAG, local MCP). | Decide which parts of your demo suppose stay private and run locally. |
| [18 - Securing AI Agents](./18-securing-ai-agents/README.md) | How to make agent actions more audit-able and tamper-evident. | Decide wetin actions for your demo need to dey logged or get receipt. |

## Validating Deployed Agents with Smoke Tests

When you deploy agent (Lesson 16), **smoke test** na di cheapest first
check wey deployment dey answer. Dis repo get ready-to-run
catalog under [tests/](./tests/README.md) for deployable agents for Lessons
01, 04, 05, and 16, wey connect to
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Action. Run dem from **Actions** tab after you deploy di lesson agent.
Smoke tests na first gate — offline and online evaluation (Lessons 10 and 16)
dey tell you how *good* di agent be.

## Key Ideas for Beginner-Friendly Terms

### Tools

Tool na wetin di agent fit call to do work outside di model. Beta tool
get clear name, narrow job, typed inputs, predictable output, and safe fale
way.

For course helper demo, tool fit be:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG and Knowledge

RAG dey help agent answer from source material instead of to guess. For dis
course, that source material fit be lesson READMEs, code samples, or external
resources wey lessons link to.

Use RAG when answer suppose base on documents, data, or current
project files.

### Planning

Planning dey beta when di request get more than one step. Make plans short and
visible so developer or user fit check am well.

For the demo, plan fit be:

1. Find lessons wey relate to tool use.
2. Summarize di most important lessons.
3. Suggest one practice task.

### Context

Context na wetin model see now. Small context fit make agent miss important detail.
Too much context fit make agent slow, costly,
or easy to confuse.

Good context engineering na to choose right info for di next model
call.

### Memory

Memory na information wey dem save for later. No save everything. Save info
when e useful, safe, and easy to update or delete.

For example, to remember say "di learner like Python examples" fit useful.
To remember sensitive personal data normal no good.

### Evaluation and Observability

Evaluation dey ask: Agent do correct thing?

Observability dey ask: We fit see how e happen?

For production agents, dey keep track of model calls, tool calls, retrieved context,
latency, cost, failures, and user feedback.

### Trust and Security

Trustworthy agents need pass beta prompt. Use least-privilege tools,
human approval for big-impact actions, data redaction where e need, plus logs or
receipts for actions wey must dey audited.

## 15-Minute Review Routine

Use dis routine after each lesson:

1. **Summarize di lesson inside one sentence.**
2. **Name di new agent capability.** For example: tool use, retrieval,
   planning, memory, observability, or security.
3. **Add am to the course helper demo.** Wetin change for di demo now?
4. **Find di risk.** Wetin fit go wrong if dis capability misuse?
5. **Write one test question.** How you go check say agent dey behave well?

## Quick Self-Check

Before you continue, try answer dis questions:

1. Wetin agent fit do wey regular chatbot no fit do by itself?
2. Which tool your agent need first, and why?
3. Which knowledge source suppose ground di agent's answer?
4. Which context suppose dey inside di next model call?
5. Wetin agent suppose remember, and wetin e suppose no store?
6. When agent suppose ask for human approval?
7. Which logs, traces, or receipts fit help you debug or audit di agent later?


## Suggested Capstone Exercise

For di end of di course, build small agent wey go help learner waka through dis
repository.

Minimum version:

- Accept topic from di user.
- Find di most correct lessons.
- Summarize wetin dem go first read.
- Suggest one hands-on practice task.
- Show which lesson files or links dem use.

Stretch version:

- Remember di learner preferred programming language.
- Use simple plan before you answer.
- Add self-check step before di final response.
- Log tool calls and di sources wey you find.
- Ask for confirmation before you open browser or do UI automation tasks.

Dis one go give you small but real way to practice tools, RAG, planning,
context, memory, observability, and trust for one project.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->