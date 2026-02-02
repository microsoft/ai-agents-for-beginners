# AI Agents for Beginners - Study Guide & Course Summary

Dis guide dey provide summary of di "AI Agents for Beginners" course and explain key concepts, frameworks, and design patterns for building AI Agents.

## 1. Introduction to AI Agents

**Wetin be AI Agents?**  
AI Agents na systems wey extend di capabilities of Large Language Models (LLMs) by givin dem access to **tools**, **knowledge**, and **memory**. No be like normal LLM chatbot wey just dey generate text based on training data, AI Agent fit:  
- **Perceive** im environment (through sensors or inputs).  
- **Reason** about how to solve problem.  
- **Act** to change di environment (through actuators or tool execution).  

**Key Components of an Agent:**  
- **Environment**: Di space wey di agent dey operate (e.g., booking system).  
- **Sensors**: Mechanisms to gather information (e.g., read API).  
- **Actuators**: Mechanisms to perform actions (e.g., send email).  
- **Brain (LLM)**: Di reasoning engine wey plan and decide which actions to take.  

## 2. Agentic Frameworks

Di course cover three main frameworks for building agents:

| Framework | Focus | Best For |
|-----------|-------|----------|
| **Semantic Kernel** | Production-ready SDK for .NET/Python | Enterprise applications, to combine AI with existing code. |
| **AutoGen** | Multi-agent collaboration | Complex scenarios wey need plenty specialized agents dey talk to each other. |
| **Azure AI Agent Service** | Managed cloud service | Secure, scalable deployment with built-in state management. |

## 3. Agentic Design Patterns

Design patterns dey help structure how agents dey operate to solve problems steady.

### **Tool Use Pattern** (Lesson 4)  
Dis pattern make agents fit interact with outside world.  
- **Concept**: Di agent get "schema" (list of available functions and parameters). Di LLM go decide *which* tool to use and *what* arguments based on user request.  
- **Flow**: User Request -> LLM -> **Tool Selection** -> **Tool Execution** -> LLM (with tool output) -> Final Response.  
- **Use Cases**: Get real-time data (weather, stock prices), do calculations, run code.  

### **Planning Pattern** (Lesson 7)  
Dis pattern make agents fit solve complex, multi-step tasks.  
- **Concept**: Di agent break high-level goal down to small smaller subtasks.  
- **Approaches**:  
  - **Task Decomposition**: Split "Plan a trip" into "Book flight", "Book hotel", "Rent car".  
  - **Iterative Planning**: Re-check plan based on output from previous steps (e.g., if flight full, choose another date).  
- **Implementation**: Usually get "Planner" agent wey generate structured plan (e.g., JSON) then other agents go execute am.  

## 4. Design Principles

When you dey design agents, reason about three dimensions:  
- **Space**: Agents suppose connect people and knowledge, dey accessible but no too obvious.  
- **Time**: Agents suppose learn from *Past*, give relevant nudges for *Now*, and adjust for *Future*.  
- **Core**: Accept say things fit no sure but build trust through transparency and user control.  

## 5. Summary of Key Lessons

- **Lesson 1**: Agents na systems, no be only models. Dem perceive, reason, and act.  
- **Lesson 2**: Frameworks like Semantic Kernel and AutoGen dey simplify tool calling and state management.  
- **Lesson 3**: Design with transparency and user control.  
- **Lesson 4**: Tools be di "hands" of agent. Schema definition important make LLM fit understand how to use dem.  
- **Lesson 7**: Planning na di "executive function" of agent, e dey enable am handle complex workflows.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator). Even if we dey try make am correct, abeg sabi say machine translation fit get mistake or no too correct. Di original document for e own language na im be di correct one. If na serious matter, e better make person wey sabi do human translation check am. We no go take responsibility if person no understand well or if dem use dis translation wrong.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->