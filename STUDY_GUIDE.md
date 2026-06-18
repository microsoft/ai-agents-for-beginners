# AI Agents for Beginners - Study Guide

This guide is a quick companion to the course. Use it to choose where to start,
what to review before each lesson, and how the lessons fit together.

## What This Course Builds Toward

AI agents extend language models with the ability to use tools, keep useful
context, coordinate work, and operate with guardrails. A useful agent system
usually combines several parts:

- **Model reasoning:** The language model interprets goals, plans next steps,
  and turns tool results into useful responses.
- **Tools:** Functions, APIs, files, browsers, and services that let the agent
  act outside the model.
- **Knowledge:** Retrieved documents, data stores, search indexes, or domain
  facts used to ground responses.
- **Memory and context:** Short-term conversation state, longer-term user or
  task memory, and context engineering strategies that decide what reaches the
  next model call.
- **Orchestration:** Planning, routing, handoffs, multi-agent workflows, and
  protocol integrations.
- **Operations and trust:** Evaluation, observability, security controls, and
  audit trails for production use.

## Recommended Learning Paths

If you are new to agents, follow the lessons in order through Lesson 6 before
jumping into specific patterns. Those early lessons establish the mental model
for agents, frameworks, design principles, tools, RAG, and trustworthy behavior.

| Goal | Suggested lessons |
|------|-------------------|
| Understand the basics | 01, 02, 03, 04 |
| Build agents that use data and tools | 04, 05, 07 |
| Design multi-step or multi-agent workflows | 07, 08, 09, 14 |
| Prepare for production | 06, 10, 12, 13, 18 |
| Explore protocols and browser automation | 11, 15 |

## Lesson Map

| Lesson | Main idea | Review when you need to |
|--------|-----------|-------------------------|
| 01 - Intro to AI Agents | Agents are systems that reason, use context, and take actions through tools. | Explain what makes an agent different from a chatbot. |
| 02 - Agentic Frameworks | Frameworks provide structure for model access, tools, state, and agent workflows. | Choose the right framework/runtime for a sample. |
| 03 - Agentic Design Principles | Good agent design starts with transparency, user control, and consistent experiences. | Turn a use case into a user-centered agent design. |
| 04 - Tool Use | Tools let agents retrieve information, call APIs, calculate, or update external systems. | Define tool schemas and decide when a tool should be called. |
| 05 - Agentic RAG | RAG grounds agent responses in retrieved knowledge and can be part of the agent loop. | Connect search or documents to agent responses. |
| 06 - Trustworthy Agents | Trustworthy agents need guardrails, safe system messages, human oversight, and threat awareness. | Add safety checks before an agent takes action. |
| 07 - Planning Design | Planning decomposes larger goals into smaller tasks that can be routed and executed. | Build or debug a multi-step agent workflow. |
| 08 - Multi-Agent Design | Multi-agent systems split work across specialized agents and coordinate their outputs. | Decide whether one agent is enough or a team of agents is clearer. |
| 09 - Metacognition | Metacognition helps agents inspect, critique, and improve their own work. | Add reflection or quality checks to agent output. |
| 10 - AI Agents in Production | Production agents need observability, evaluation, cost control, and operational feedback loops. | Move from a notebook demo to a monitored application. |
| 11 - Agentic Protocols | Protocols such as MCP and A2A help agents connect to tools and other agents in standard ways. | Integrate agents with external tool servers or agent-to-agent workflows. |
| 12 - Context Engineering | Context engineering controls what information is written, selected, compressed, or isolated. | Debug missing, stale, excessive, or conflicting context. |
| 13 - Agent Memory | Memory lets agents retain useful information across turns, sessions, or longer-term stores. | Decide what should be remembered and how it should be retrieved. |
| 14 - Microsoft Agent Framework | Microsoft Agent Framework provides agent, workflow, and orchestration building blocks. | Learn the framework-specific primitives used across samples. |
| 15 - Computer Use Agents | Computer use agents interact with browsers and UI surfaces to complete tasks. | Build or reason about browser-based automation. |
| 18 - Securing AI Agents | Cryptographic receipts create verifiable records of agent tool calls and action history. | Add auditability or tamper-evidence to higher-risk agent actions. |

## Key Concepts To Revisit

### Tools

Tools are the main way agents act. A good tool definition should have a clear
name, narrow purpose, typed inputs, predictable output, and safe failure modes.
If the model chooses the wrong tool, inspect the tool names, descriptions, and
the amount of tool context loaded into the prompt.

### Planning and Orchestration

Planning is useful when a task has dependencies, checkpoints, or separate areas
of expertise. Keep plans small enough to inspect. When using several agents,
make the handoff format explicit so each agent knows what it received and what
it must return.

### Context and Memory

Context is the working set for the next model call. Memory is information saved
for later use. Before adding memory, decide whether the information is accurate,
useful beyond the current turn, safe to store, and easy to delete or update.

### Evaluation and Observability

Agent quality should be measured with repeatable examples, traces, feedback, and
cost/latency data. In production, the question is not only "did it answer?" but
"which model, tools, context, and decisions produced this answer?"

### Trust and Security

Trustworthy agents need more than a helpful prompt. Use guardrails, least
privilege tools, human approval for high-impact actions, redaction for sensitive
data, and receipts or logs when actions need to be audited later.

## Quick Self-Check

Before you finish a lesson, try answering these questions:

1. What decision did the agent make that a normal chatbot could not make alone?
2. What tools, knowledge, or memory did the agent depend on?
3. What could go wrong if the tool returned bad data or the context was stale?
4. How would you observe, evaluate, or audit the agent behavior?
5. What user control or human review would be needed before using this pattern
   in a real application?
