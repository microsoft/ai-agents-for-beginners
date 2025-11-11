
[![Intro to AI Agents](./images/lesson-1-thumbnail.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Click the image above to view video of this lesson)_


# Introduction to AI Agents and Agent Use Cases

Welcome to the "AI Agents for Beginners" course! This course provides fundamental knowledge and applied samples for building AI Agents.

Join the <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> to meet other learners and AI Agent Builders and ask any questions you have about this course.

To start this course, we begin by getting a better understanding of what AI Agents are and how we can use them in the applications and workflows we build.

## Introduction

This lesson covers:

- What are AI Agents and what are the different types of agents?
- What use cases are best for AI Agents and how can they help us?
- What are some of the basic building blocks when designing Agentic Solutions?

## Learning Goals
After completing this lesson, you should be able to:

- Understand AI Agent concepts and how they differ from other AI solutions.
- Apply AI Agents most efficiently.
- Design Agentic solutions productively for both users and customers.

## Defining AI Agents and Types of AI Agents

### What are AI Agents?

AI Agents are **systems** that enable **Large Language Models(LLMs)** to **perform actions** by extending their capabilities by giving LLMs **access to tools** and **knowledge**.

Let's break this definition into smaller parts:

- **System** - It's important to think about agents not as just a single component but as a system of many components. At the basic level, the components of an AI Agent are:
  - **Environment** - The defined space where the AI Agent is operating. For example, if we had a travel booking AI Agent, the environment could be the travel booking system that the AI Agent uses to complete tasks.
  - **Sensors** - Environments have information and provide feedback. AI Agents use sensors to gather and interpret this information about the current state of the environment. In the Travel Booking Agent example, the travel booking system can provide information such as hotel availability or flight prices.
  - **Actuators** - Once the AI Agent receives the current state of the environment, for the current task the agent determines what action to perform to change the environment. For the travel booking agent, it might be to book an available room for the user.

![What Are AI Agents?](./images/what-are-ai-agents.png)

**Large Language Models** - The concept of agents existed before the creation of LLMs. The advantage of building AI Agents with LLMs is their ability to interpret human language and data. This ability enables LLMs to interpret environmental information and define a plan to change the environment.

**Perform Actions** - Outside of AI Agent systems, LLMs are limited to situations where the action is generating content or information based on a user's prompt. Inside AI Agent systems, LLMs can accomplish tasks by interpreting the user's request and using tools that are available in their environment.

**Access To Tools** - What tools the LLM has access to is defined by 1) the environment it's operating in and 2) the developer of the AI Agent. For our travel agent example, the agent's tools are limited by the operations available in the booking system, and/or the developer can limit the agent's tool access to flights.

**Memory+Knowledge** - Memory can be short-term in the context of the conversation between the user and the agent. Long-term, outside of the information provided by the environment, AI Agents can also retrieve knowledge from other systems, services, tools, and even other agents. In the travel agent example, this knowledge could be the information on the user's travel preferences located in a customer database.

### The different types of agents

Now that we have a general definition of AI Agents, let us look at some specific agent types and how they would be applied to a travel booking AI agent.

| **Agent Type**                | **Description**                                                                                                                       | **Example**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simple Reflex Agents**      | Perform immediate actions based on predefined rules.                                                                                  | Travel agent interprets the context of the email and forwards travel complaints to customer service.                                                                                                                          |
| **Model-Based Reflex Agents** | Perform actions based on a model of the world and changes to that model.                                                              | Travel agent prioritizes routes with significant price changes based on access to historical pricing data.                                                                                                             |
| **Goal-Based Agents**         | Create plans to achieve specific goals by interpreting the goal and determining actions to reach it.                                  | Travel agent books a journey by determining necessary travel arrangements (car, public transit, flights) from the current location to the destination.                                                                                |
| **Utility-Based Agents**      | Consider preferences and weigh tradeoffs numerically to determine how to achieve goals.                                               | Travel agent maximizes utility by weighing convenience vs. cost when booking travel.                                                                                                                                          |
| **Learning Agents**           | Improve over time by responding to feedback and adjusting actions accordingly.                                                        | Travel agent improves by using customer feedback from post-trip surveys to make adjustments to future bookings.                                                                                                               |
| **Hierarchical Agents**       | Feature multiple agents in a tiered system, with higher-level agents breaking tasks into subtasks for lower-level agents to complete. | Travel agent cancels a trip by dividing the task into subtasks (for example, canceling specific bookings) and having lower-level agents complete them, reporting back to the higher-level agent.                                     |
| **Multi-Agent Systems (MAS)** | Agents complete tasks independently, either cooperatively or competitively.                                                           | Cooperative: Multiple agents book specific travel services such as hotels, flights, and entertainment. Competitive: Multiple agents manage and compete over a shared hotel booking calendar to book customers into the hotel. |

## When to Use AI Agents

In the earlier section, we used the Travel Agent use-case to explain how the different types of agents can be used in different scenarios of travel booking. We will continue to use this application throughout the course.

Let's look at the types of use cases that AI Agents are best used for:

![When to use AI Agents?](./images/when-to-use-ai-agents.png)


- **Open-Ended Problems** - allowing the LLM to determine needed steps to complete a task because it can't always be hardcoded into a workflow.
- **Multi-Step Processes** - tasks that require a level of complexity in which the AI Agent needs to use tools or information over multiple turns instead of single shot retrieval.  
- **Improvement Over Time** - tasks where the agent can improve over time by receiving feedback from either its environment or users in order to provide better utility.

We cover more considerations of using AI Agents in the Building Trustworthy AI Agents lesson.

## Basics of Agentic Solutions

### Agent Development

The first step in designing an AI Agent system is to define the tools, actions, and behaviors. In this course, we focus on using the **Azure AI Agent Service** to define our Agents. It offers features like:

- Selection of Open Models such as OpenAI, Mistral, and Llama
- Use of Licensed Data through providers such as Tripadvisor
- Use of standardized OpenAPI 3.0 tools

### Agentic Patterns

Communication with LLMs is through prompts. Given the semi-autonomous nature of AI Agents, it isn't always possible or required to manually reprompt the LLM after a change in the environment. We use **Agentic Patterns** that allow us to prompt the LLM over multiple steps in a more scalable way.

This course is divided into some of the current popular Agentic patterns.

### Agentic Frameworks

Agentic Frameworks allow developers to implement agentic patterns through code. These frameworks offer templates, plugins, and tools for better AI Agent collaboration. These benefits provide abilities for better observability and troubleshooting of AI Agent systems.

In this course, we will explore the research-driven AutoGen framework and the production-ready Agent framework from Semantic Kernel.

## Sample Codes

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Got More Questions about AI Agents?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Previous Lesson

[Course Setup](../00-course-setup/README.md)

## Next Lesson

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)
