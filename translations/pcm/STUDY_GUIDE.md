# AI Agents for Beginners - Study Guide & Course Summary

Dis guide dey provide summary of di "AI Agents for Beginners" course and explain di main tins, frameworks, and design patterns for building AI Agents.

## 1. Introduction to AI Agents

**Wetin be AI Agents?**  
AI Agents na systems wey dey extend di power of Large Language Models (LLMs) by giving dem access to **tools**, **knowledge**, and **memory**. E different from normal LLM chatbot wey only dey generate text based on dia training data, AI Agent fit:  
- **See** dia environment (through sensors or inputs).  
- **Think** about how to solve problem.  
- **Do** tins to change di environment (through actuators or tool execution).

**Main Parts of Agent:**  
- **Environment**: Di space wey di agent dey operate for (e.g., booking system).  
- **Sensors**: Di way wey dey gather information (e.g., reading API).  
- **Actuators**: Di way wey dey perform action (e.g., send email).  
- **Brain (LLM)**: Di reasoning engine wey dey plan and decide wetin to do.

## 2. Agentic Frameworks

Di course dey use **Microsoft Agent Framework (MAF)** with **Azure AI Foundry Agent Service V2** for building agents:

| Component                     | Focus                                             | Best For                                                     |
|-------------------------------|--------------------------------------------------|--------------------------------------------------------------|
| **Microsoft Agent Framework**  | Unified Python/C# SDK for agents, tools, workflows | Building agents with tools, multi-agent workflows, production patterns. |
| **Azure AI Foundry Agent Service** | Managed cloud runtime                            | Secure, scalable deployment with built-in state management, observability, and trust. |

## 3. Agentic Design Patterns

Design patterns help organize how agents dey work to solve problem well well.

### **Tool Use Pattern** (Lesson 4)  
Dis pattern dey enable agents to interact with di outside world.  
- **Concept**: Di agent get "schema" (list of available functions and their parameters). Di LLM go choose *which* tool to call and *what* arguments to use based on di user request.  
- **Flow**: User Request -> LLM -> **Tool Selection** -> **Tool Execution** -> LLM (with tool output) -> Final Response.  
- **Use Cases**: To collect real-time data (weather, stock prices), do calculations, run code.

### **Planning Pattern** (Lesson 7)  
Dis pattern dey help agents solve big, multi-step tasks.  
- **Concept**: Di agent break big goal into series of smaller subtasks.  
- **Approaches**:  
  - **Task Decomposition**: Break "Plan a trip" into "Book flight", "Book hotel", "Rent car".  
  - **Iterative Planning**: Check di plan again based on wetin happen before (e.g., if flight full, pick another date).  
- **Implementation**: Sometimes get "Planner" agent wey create structured plan (like JSON) wey other agents go follow.

## 4. Design Principles

When you dey design agents, think three main tins:  
- **Space**: Agents suppose connect people and knowledge, dey accessible but no too annoying.  
- **Time**: Agents suppose learn from *Past*, give correct nudges for *Now*, and change for *Future*.  
- **Core**: Accept say no be everything sure but build trust through transparency and let user get control.

## 5. Summary of Key Lessons

- **Lesson 1**: Agents na systems, no be just models. Dem fit see, reason, and act.  
- **Lesson 2**: Microsoft Agent Framework dey handle di hard parts of tool calling and state management.  
- **Lesson 3**: Design with transparency and user control.  
- **Lesson 4**: Tools na di "hands" of agent. Schema definition important so LLM go sabi how to use dem.  
- **Lesson 7**: Planning na di "executive function" of agent, e help tackle complex workflows.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document na translations wey AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) help do. Even though we dey try make am correct, abeg sabi say automated translations fit get error or mistake. Di original document wey de na im true and correct one. If na important info, e better make professional human translation do am. We no get any responsibility for any confusion or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->