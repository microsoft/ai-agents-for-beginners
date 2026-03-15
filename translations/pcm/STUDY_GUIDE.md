# AI Agents for Beginners - Study Guide & Course Summary

Dis guide dey provide one summary of di "AI Agents for Beginners" course and e explain key concepts, frameworks, and design patterns for building AI Agents.

## 1. Introduction to AI Agents

**Wetìn be AI Agents?**
AI Agents na systems wey dey extend di capabilities of Large Language Models (LLMs) by giving dem access to **tools**, **knowledge**, and **memory**. E no be like normal LLM chatbot wey just dey generate text based on training data, AI Agent fit:
- **Perceive** e environment (through sensors or inputs).
- **Reason** how e go solve problem.
- **Act** to change di environment (with actuators or tool execution).

**Key Components of an Agent:**
- **Environment**: Di space wey di agent dey operate (like booking system).
- **Sensors**: Way dem gather information (like reading API).
- **Actuators**: How dem perform actions (like sending email).
- **Brain (LLM)**: Di reasoning engine wey dey plan and decide wetin action to take.

## 2. Agentic Frameworks

Di course dey use **Microsoft Agent Framework (MAF)** with **Azure AI Foundry Agent Service V2** to build agents:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Unified Python/C# SDK for agents, tools, and workflows | Building agents with tools, multi-agent workflows, and production patterns. |
| **Azure AI Foundry Agent Service** | Managed cloud runtime | Secure, scalable deployment with built-in state management, observability, and trust. |

## 3. Agentic Design Patterns

Design patterns dey help arrange how agents go operate to solve problem well.

### **Tool Use Pattern** (Lesson 4)
Dis pattern dey enable agents make dem interact wit di outside world.
- **Concept**: Di agent get "schema" (list of available functions plus their parameters). Di LLM dey decide *which* tool to call and *what* arguments e go carry based on wetin di user ask.
- **Flow**: User Request -> LLM -> **Tool Selection** -> **Tool Execution** -> LLM (with tool output) -> Final Response.
- **Use Cases**: Fetch real-time data (weather, stock prices), do calculations, run code.

### **Planning Pattern** (Lesson 7)
Dis pattern dey enable agents to solve complex, multi-step work.
- **Concept**: Di agent dey break down one big goal to smaller smaller tasks.
- **Approaches**:
  - **Task Decomposition**: Break "Plan a trip" into "Book flight", "Book hotel", "Rent car".
  - **Iterative Planning**: Recheck di plan based on how previous step waka (like if flight full, choose another date).
- **Implementation**: Usually involve "Planner" agent wey fit generate structured plan (like JSON) wey other agents go execute.

## 4. Design Principles

When you dey design agents, consider three things:
- **Space**: Agents suppose connect people and knowledge, dey accessible but no too dey disturb.
- **Time**: Agents suppose learn from *Past*, give relevant nudges for *Now*, and adjust for *Future*.
- **Core**: Accept say things fit sometimes be uncertain but make trust through transparency and user control.

## 5. Summary of Key Lessons

- **Lesson 1**: Agents dey system, no be only models. Dem dey perceive, reason, and act.
- **Lesson 2**: Microsoft Agent Framework dey simplify how tools dey call and how state dey manage.
- **Lesson 3**: Design with transparency and user control for mind.
- **Lesson 4**: Tools na di "hands" of di agent. Schema definition important so LLM go sabi how to use dem.
- **Lesson 7**: Planning na di "executive function" of agent to handle complex workflows.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg make you sabi say automated translation fit get errors or mistakes. Di original document wey dey im own language na di correct one. For important matter, e better make professional human translator do am. We no go responsible for any misunderstanding or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->