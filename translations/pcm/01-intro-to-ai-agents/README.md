[![Intro to AI Agents](../../../translated_images/pcm/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Click di picture wey dey up make you fit watch dis lesson video)_


# Introduction to AI Agents and Agent Use Cases

Welcome to the "AI Agents for Beginners" course! Dis course dey give basic knowledge and sample wey you fit use to build AI Agents.

Join the <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> make you meet oda learners and AI Agent Builders and ask any question wey you get about dis course.

To start dis course, we go begin by make we understand wetin AI Agents be and how we fit use dem for the apps and workflows wey we dey build.

## Introduction

This lesson cover:

- Wetin be AI Agents and wetin be the different kain agents?
- Which use cases better for AI Agents and how dem fit help us?
- Wetin be some basic building blocks wen you dey design Agentic Solutions?

## Learning Goals
After you finish dis lesson, you suppose fit:

- Understand AI Agent concepts and how dem different from oda AI solutions.
- Use AI Agents well and sabi how to apply dem efficiently.
- Design Agentic solutions wey go work well for users and customers.

## Defining AI Agents and Types of AI Agents

### What are AI Agents?

AI Agents na **systems** wey make **Large Language Models(LLMs)** fit **perform actions** by giving LLMs **access to tools** and **knowledge**.

Make we break dis definition small-small:

- **System** - E important make you think of agents no be only one component but na system wey get many components. For the basic level, the components of an AI Agent be:
  - **Environment** - Na the defined space wey the AI Agent dey operate. For example, if we get travel booking AI Agent, the environment fit be the travel booking system wey the AI Agent dey use to complete tasks.
  - **Sensors** - Environments get information and dem dey give feedback. AI Agents dey use sensors to gather and interpret this information about the current state of the environment. For the Travel Booking Agent example, the travel booking system fit provide information like hotel availability or flight prices.
  - **Actuators** - Once the AI Agent don receive the current state of the environment, for the current task the agent go decide which action to perform to change the environment. For the travel booking agent, e fit dey to book an available room for the user.

![What Are AI Agents?](../../../translated_images/pcm/what-are-ai-agents.1ec8c4d548af601a.webp)

**Large Language Models** - The concept of agents dey before dem create LLMs. The advantage to build AI Agents with LLMs na their ability to interpret human language and data. Dis ability make LLMs fit understand environmental information and make plan to change the environment.

**Perform Actions** - Outside AI Agent systems, LLMs limited to situations wey action na to generate content or information based on user prompt. Inside AI Agent systems, LLMs fit do tasks by understanding the user's request and using tools wey dey for their environment.

**Access To Tools** - Which tools the LLM get access to dey defined by 1) the environment e dey operate and 2) the developer of the AI Agent. For our travel agent example, the agent tools dey limited by the operations wey dey the booking system, and/or the developer fit limit the agent tool access to flights only.

**Memory+Knowledge** - Memory fit be short-term for the conversation between the user and the agent. For long-term, outside the information wey environment provide, AI Agents fit also fetch knowledge from oda systems, services, tools, and even oda agents. For the travel agent example, dis knowledge fit be the information about the user's travel preferences wey dey for customer database.

### The different types of agents

Now we don get general definition of AI Agents, make we look some specific agent types and how dem fit apply to a travel booking AI agent.

| **Agent Type**                | **Description**                                                                                                                       | **Example**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simple Reflex Agents**      | Dem dey perform immediate actions based on predefined rules.                                                                          | Travel agent go interpret the context of the email and forward travel complaints to customer service.                                                                                                                          |
| **Model-Based Reflex Agents** | Dem dey perform actions based on a model of the world and changes to that model.                                                       | Travel agent go prioritize routes wey get big price changes based on access to historical pricing data.                                                                                                                     |
| **Goal-Based Agents**         | Dem dey create plans to achieve specific goals by interpreting the goal and deciding actions to reach am.                              | Travel agent go book journey by deciding the necessary travel arrangements (car, public transit, flights) from the current location to the destination.                                                                        |
| **Utility-Based Agents**      | Dem dey consider preferences and weigh tradeoffs numerically to decide how to achieve goals.                                          | Travel agent go maximize utility by weighing convenience versus cost when e dey book travel.                                                                                                                                 |
| **Learning Agents**           | Dem dey improve over time by responding to feedback and adjusting actions accordingly.                                                 | Travel agent go improve by using customer feedback from post-trip surveys to make adjustments for future bookings.                                                                                                           |
| **Hierarchical Agents**       | Dem get many agents for different levels, with higher-level agents wey break tasks into subtasks for lower-level agents to finish.     | Travel agent go cancel trip by dividing the task into subtasks (for example, cancel specific bookings) and make lower-level agents complete dem, then report back to the higher-level agent.                                   |
| **Multi-Agent Systems (MAS)** | Agents fit complete tasks independently, either cooperatively or competitively.                                                       | Cooperative: Many agents book specific travel services like hotels, flights, and entertainment. Competitive: Many agents manage and compete over one shared hotel booking calendar to book customers into the hotel.            |

## When to Use AI Agents

For the earlier section, we use the Travel Agent example to explain how the different types of agents fit different travel booking scenarios. We go continue to use this application throughout the course.

Make we check the kinds of use cases wey AI Agents best for:

![When to use AI Agents?](../../../translated_images/pcm/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Open-Ended Problems** - make the LLM decide the steps wey dey needed to finish a task because you no fit always hardcode every step into a workflow.
- **Multi-Step Processes** - tasks wey need some complexity where the AI Agent go need to use tools or information across multiple turns instead of one-shot retrieval.  
- **Improvement Over Time** - tasks where the agent fit improve over time by receiving feedback from the environment or users so e go give better results.

We go cover more considerations about using AI Agents for the Building Trustworthy AI Agents lesson.

## Basics of Agentic Solutions

### Agent Development

The first step to design AI Agent system na to define the tools, actions, and behaviors. For this course, we focus on using the **Azure AI Agent Service** to define our Agents. E get features like:

- Selection of Open Models such as OpenAI, Mistral, and Llama
- Use of Licensed Data through providers such as Tripadvisor
- Use of standardized OpenAPI 3.0 tools

### Agentic Patterns

Communication with LLMs dey through prompts. Because AI Agents get semi-autonomous nature, e no always possible or necessary to manually reprompt the LLM after environment change. We dey use **Agentic Patterns** wey allow us to prompt the LLM across multiple steps in more scalable way.

Dis course divided into some of the popular Agentic patterns wey dey now.

### Agentic Frameworks

Agentic Frameworks make developers fit implement agentic patterns with code. These frameworks get templates, plugins, and tools wey help better AI Agent collaboration. Dem dey give better observability and troubleshooting for AI Agent systems.

For this course, we go explore the Microsoft Agent Framework (MAF) for building production-ready AI agents.

## Sample Codes

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Got More Questions about AI Agents?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) make you meet other learners, attend office hours and get your AI Agents questions answered.

## Previous Lesson

[Course Setup](../00-course-setup/README.md)

## Next Lesson

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document na AI translation wey dem do wit [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automatic translation fit get mistakes or wrong parts. The original document for im original language na the correct, authoritative source. If na important tori, better make person wey sabi do professional human translation handle am. We no go responsible for any misunderstanding or wrong interpretation wey fit come from this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->