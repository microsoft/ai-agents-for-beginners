# Multi agent design patterns

As soon as you start working on a project that involves multiple agents, you will need to consider the multi-agent design pattern. However, it might not be immediately clear when to switch to multi-agents and what the advantages are.

## Introduction

In this lesson, we're looking to answer the following questions:

- What are the scenarios where multi-agents are applicable to?
- What are the advantages of using multi-agents over just one singular agent doing multiple tasks?
- What are the building blocks of implementing the multi-agent design pattern?
- How do we have visibility to how the multiple agents are interacting with each other

## Learning Goals

After this lesson, you should be able to:

- Identify scenarios where multi-agents are applicable
- Recognize the advantages of using multi-agents over a singular agent.
- Comprehend the building blocks of implementing the multi-agent design pattern.

What's the bigger picture?

*Multi agents are a design pattern that allows multiple agents to work together to achieve a common goal*.

This pattern is widely used in various fields, including robotics, autonomous systems, and distributed computing.

## Scenarios Where Multi-Agents Are Applicable

So what scenarios are a good use case for using multi-agents? The answer is that there are many scenarios where employing multiple agents is beneficial especially in the following cases:

- **Large workloads**: Large workloads can be divided into smaller tasks and assigned to different agents, allowing for parallel processing and faster completion. An example of this is in the case of a large data processing task.
- **Complex tasks**: Complex tasks, like large workloads, can be broken down into smaller subtasks and assigned to different agents, each specializing in a specific aspect of the task. A good example of this is in the case of autonomous vehicles where different agents manage navigation, obstacle detection, and communication with other vehicles.
- **Diverse expertise**: Different agents can have diverse expertise, allowing them to handle different aspects of a task more effectively than a single agent. For this case, a good example is in the case of healthcare where agents can manage diagnostics, treatment plans, and patient monitoring.

## Advantages of Using Multi-Agents Over a Singular Agent

A single agent system could work well for simple tasks, but for more complex tasks, using multiple agents can provide several advantages:

- **Specialization**: Each agent can be specialized for a specific task. Lack of specialization in a single agent means you have an agent that can do everything but might get confused on what to do when faced with a complex task. It might for example end up doing a task that it is not best suited for.
- **Scalability**: It is easier to scale systems by adding more agents rather than overloading a single agent.
- **Fault Tolerance**: If one agent fails, others can continue functioning, ensuring system reliability.

Let's take an example, let's book a trip for a user. A single agent system would have to handle all aspects of the trip booking process, from finding flights to booking hotels and rental cars. To achieve this with a single agent, the agent would need to have tools for handling all these tasks. This could lead to a complex and monolithic system that is difficult to maintain and scale. A multi-agent system, on the other hand, could have different agents specialized in finding flights, booking hotels, and rental cars. This would make the system more modular, easier to maintain, and scalable.

Compare this to a travel bureau run as a mom and pop store versus a travel bureau run as a franchise. The mom and pop store would have a single agent handling all aspects of the trip booking process, while the franchise would have different agents handling different aspects of the trip booking process.

## Building Blocks of Implementing the Multi-Agent Design Pattern

Before you can implement the multi-agent design pattern, you need to understand the building blocks that make up the pattern.

Let's make this more concrete by again looking at the example of booking a trip for a user. In this case, the building blocks would include:

- **Agent Communication**: Agents for finding flights, booking hotels, and rental cars need to communicate and share information about the user's preferences and constraints. You need to decide on the protocols and methods for this communication. What this means concretely is that the agent for finding flights needs to communicate with the agent for booking hotels to ensure that the hotel is booked for the same dates as the flight. That means that the agents need to share information about the user's travel dates, meaning that you need to decide *which agents are sharing info and how they are sharing info*.
- **Coordination Mechanisms**: Agents need to coordinate their actions to ensure that the user's preferences and constraints are met. A user preference could be that they want a hotel close to the airport whereas a constraint could be that rental cars are only available at the airport. This means that the agent for booking hotels needs to coordinate with the agent for booking rental cars to ensure that the user's preferences and constraints are met. This means that you need to decide *how the agents are coordinating their actions*.
- **Agent Architecture**: Agents need to have the internal structure to make decisions and learn from their interactions with the user. This means that the agent for finding flights needs to have the internal structure to make decisions about which flights to recommend to the user. This means that you need to decide *how the agents are making decisions and learning from their interactions with the user*. Examples of how an agent learns and improves could be that the agent for finding flights could use a machine learning model to recommend flights to the user based on their past preferences.
- **Visibility into Multi-Agent Interactions**: You need to have visibility into how the multiple agents are interacting with each other. This means that you need to have tools and techniques for tracking agent activities and interactions. This could be in the form of logging and monitoring tools, visualization tools, and performance metrics.
- **Multi-Agent Patterns**: There are different patterns for implementing multi-agent systems, such as centralized, decentralized, and hybrid architectures. You need to decide on the pattern that best fits your use case.
- **Human in the loop**: In most cases, you will have a human in the loop and you need to instruct the agents when to ask for human intervention. This could be in the form of a user asking for a specific hotel or flight that the agents have not recommended or asking for confirmation before booking a flight or hotel.

## Visibility into Multi-Agent Interactions

It's important that you have visibility into how the multiple agents are interacting with each other. This visibility is essential for debugging, optimizing, and ensuring the overall system's effectiveness. To achieve this, you need to have tools and techniques for tracking agent activities and interactions. This could be in the form of logging and monitoring tools, visualization tools, and performance metrics.

For example, in the case of booking a trip for a user, you could have a dashboard that shows the status of each agent, the user's preferences and constraints, and the interactions between agents. This dashboard could show the user's travel dates, the flights recommended by the flight agent, the hotels recommended by the hotel agent, and the rental cars recommended by the rental car agent. This would give you a clear view of how the agents are interacting with each other and whether the user's preferences and constraints are being met.

Let's look at each of these aspects more in detail.

- **Logging and Monitoring Tools**: You want to have logging done for each action taken by an agent. A log entry could store information on the agent that took the action, the action taken, the time the action was taken, and the outcome of the action. This information can then be used for debugging, optimizing and more.

- **Visualization Tools**: Visualization tools can help you see the interactions between agents in a more intuitive way. For example, you could have a graph that shows the flow of information between agents. This could help you identify bottlenecks, inefficiencies, and other issues in the system.

- **Performance Metrics**: Performance metrics can help you track the effectiveness of the multi-agent system. For example, you could track the time taken to complete a task, the number of tasks completed per unit of time, and the accuracy of the recommendations made by the agents. This information can help you identify areas for improvement and optimize the system.

## Multi-Agent Patterns

Let's dive into some concrete patterns we can use to create multi-agent apps. Here are some interesting patterns worth considering:

### Group chat

This pattern is useful when you want to create a group chat application where multiple agents can communicate with each other. Typical use cases for this pattern include team collaboration, customer support, and social networking.

In this pattern, each agent represents a user in the group chat, and messages are exchanged between agents using a messaging protocol. The agents can send messages to the group chat, receive messages from the group chat, and respond to messages from other agents.

This pattern can be implemented using a centralized architecture where all messages are routed through a central server, or a decentralized architecture where messages are exchanged directly.

![Group chat](./images/multi-agent-group-chat.png)

### Hand-off

This pattern is useful when you want to create an application where multiple agents can hand off tasks to each other.

Typical use cases for this pattern include customer support, task management, and workflow automation.

In this pattern, each agent represents a task or a step in a workflow, and agents can hand off tasks to other agents based on predefined rules.

![Hand off](./images/multi-agent-hand-off.png)

### Collaborative filtering

This pattern is useful when you want to create an application where multiple agents can collaborate to make recommendations to users.

Why you would want multiple agents to collaborate is because each agent can have different expertise and can contribute to the recommendation process in different ways.

Let's take an example where a user wants a recommendation on the best stock to buy on the stock market.

- **Industry expert**:. One agent could be an expert in a specific industry.
- **Technical analysis**: Another agent could be an expert in technical analysis.
- **Fundamental analysis**: and another agent could be an expert in fundamental analysis. By collaborating, these agents can provide a more comprehensive recommendation to the user.

![Recommendation](./images/multi-agent-filtering.png)

## Scenario: Refund process

Consider a scenario where a customer is trying to get a refund for a product, there can be quite a few agents involved in this process but let's divide it up between agents specific for this process and general agents that can be used in other processes.

**Agents specific for the refund process**:

Following are some agents that could be involved in the refund process:

- **Customer agent**: This agent represents the customer and is responsible for initiating the refund process.
- **Seller agent**: This agent represents the seller and is responsible for processing the refund.
- **Payment agent**: This agent represents the payment process and is responsible for refunding the customer's payment.
- **Resolution agent**: This agent represents the resolution process and is responsible for resolving any issues that arise during the refund process.
- **Compliance agent**: This agent represents the compliance process and is responsible for ensuring that the refund process complies with regulations and policies.

**General agents**:

These agents can be used by other parts of your business.

- **Shipping agent**: This agent represents the shipping process and is responsible for shipping the product back to the seller. This agent can be used both for the refund process and for general shipping of a product via a purchase for example.
- **Feedback agent**: This agent represents the feedback process and is responsible for collecting feedback from the customer. Feedback could be had at any time and not just during the refund process.
- **Escalation agent**: This agent represents the escalation process and is responsible for escalating issues to a higher level of support. You can use this type of agent for any process where you need to escalate an issue.
- **Notification agent**: This agent represents the notification process and is responsible for sending notifications to the customer at various stages of the refund process.
- **Analytics agent**: This agent represents the analytics process and is responsible for analyzing data related to the refund process.
- **Audit agent**: This agent represents the audit process and is responsible for auditing the refund process to ensure that it is being carried out correctly.
- **Reporting agent**: This agent represents the reporting process and is responsible for generating reports on the refund process.
- **Knowledge agent**: This agent represents the knowledge process and is responsible for maintaining a knowledge base of information related to the refund process. RThis agent could be knowledgeable both on refunds and other parts of your business.
- **Security agent**: This agent represents the security process and is responsible for ensuring the security of the refund process.
- **Quality agent**: This agent represents the quality process and is responsible for ensuring the quality of the refund process.

There's quite a few agents listed previously both for the specific refund process but also for the general agents that can be used in other parts of your business. Hopefully this gives you an idea on how you can decide on which agents to use in your multi agent system.

## Assignment

Design a multi-agent system for a customer support process. Identify the agents involved in the process, their roles and responsibilities, and how they interact with each other. Consider both agents specific to the customer support process and general agents that can be used in other parts of your business.

> Have a think before you read the following solution, you may need more agents than you think.

> TIP: Think about the different stages of the customer support process and also consider agents needed for any system.

## Solution

[Solution](./solution/solution.md)

## Knowledge checks

Question: When should you consider using multi-agents?

- [] A1: When you have a small workload and a simple task.
- [] A2: When you have a large workload
- [] A3: When you have a simple task.

[Solution quiz](./solution/solution-quiz.md)

## Summary

In this lesson, we've looked at the multi-agent design pattern, including the scenarios where multi-agents are applicable, the advantages of using multi-agents over a singular agent, the building blocks of implementing the multi-agent design pattern, and how to have visibility into how the multiple agents are interacting with each other.

## Additional resources

- <a href="https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/intro.html" target="_blank">AutoGen design patterns</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentic design patterns</a>
