<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-30T13:03:17+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "en"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.en.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Click the image above to view video of this lesson)_

# Multi-agent design patterns

When working on a project involving multiple agents, it's essential to consider the multi-agent design pattern. However, it may not be immediately obvious when to transition to multi-agents or what benefits they offer.

## Introduction

In this lesson, we aim to address the following questions:

- What scenarios are suitable for multi-agents?
- What are the benefits of using multi-agents compared to a single agent handling multiple tasks?
- What are the key components of implementing the multi-agent design pattern?
- How can we monitor the interactions between multiple agents?

## Learning Goals

By the end of this lesson, you should be able to:

- Identify scenarios where multi-agents are applicable.
- Understand the advantages of using multi-agents over a single agent.
- Grasp the foundational elements of implementing the multi-agent design pattern.

What's the bigger picture?

*Multi-agents are a design pattern that enables multiple agents to collaborate to achieve a shared goal.*

This approach is widely applied in fields such as robotics, autonomous systems, and distributed computing.

## Scenarios Where Multi-Agents Are Applicable

What situations are ideal for using multi-agents? There are numerous scenarios where employing multiple agents is advantageous, particularly in the following cases:

- **Large workloads**: Large tasks can be divided into smaller ones and assigned to different agents, enabling parallel processing and quicker completion. For instance, processing large datasets.
- **Complex tasks**: Complex tasks can be broken into subtasks, with each assigned to agents specializing in specific aspects. A good example is autonomous vehicles, where different agents handle navigation, obstacle detection, and communication with other vehicles.
- **Diverse expertise**: Agents with varied expertise can tackle different aspects of a task more effectively than a single agent. For example, in healthcare, agents can manage diagnostics, treatment plans, and patient monitoring.

## Advantages of Using Multi-Agents Over a Singular Agent

While a single agent system may suffice for simple tasks, multi-agents offer several benefits for more complex tasks:

- **Specialization**: Each agent can focus on a specific task. A single agent trying to handle everything may struggle with complex tasks or perform suboptimally.
- **Scalability**: Adding more agents is easier than overloading a single agent.
- **Fault Tolerance**: If one agent fails, others can continue functioning, ensuring system reliability.

For example, consider booking a trip for a user. A single agent system would need to handle all aspects—finding flights, booking hotels, and rental cars—requiring tools for each task. This could result in a complex, monolithic system that's hard to maintain and scale. A multi-agent system, however, could have specialized agents for flights, hotels, and rental cars, making the system modular, easier to maintain, and scalable.

Compare this to a small family-run travel agency versus a franchise. The family-run agency might rely on one person handling everything, while the franchise would have specialized staff for different aspects of trip planning.

## Building Blocks of Implementing the Multi-Agent Design Pattern

To implement the multi-agent design pattern, you need to understand its key components.

Using the example of booking a trip for a user, the building blocks include:

- **Agent Communication**: Agents for flights, hotels, and rental cars must share information about the user's preferences and constraints. For instance, the flight agent must communicate with the hotel agent to ensure the hotel is booked for the same dates as the flight. You need to decide *which agents share information and how*.
- **Coordination Mechanisms**: Agents must coordinate their actions to meet the user's preferences and constraints. For example, if the user prefers a hotel near the airport but rental cars are only available at the airport, the hotel and rental car agents must coordinate. You need to decide *how agents coordinate their actions*.
- **Agent Architecture**: Agents must have internal structures to make decisions and learn from user interactions. For example, the flight agent might use a machine learning model to recommend flights based on past preferences. You need to decide *how agents make decisions and learn*.
- **Visibility into Multi-Agent Interactions**: Tools and techniques are needed to monitor agent activities and interactions, such as logging, visualization tools, and performance metrics.
- **Multi-Agent Patterns**: Decide on the architecture—centralized, decentralized, or hybrid—that best suits your use case.
- **Human in the loop**: Agents should know when to seek human intervention, such as confirming a booking or handling specific user requests.

## Visibility into Multi-Agent Interactions

Monitoring how agents interact is crucial for debugging, optimization, and ensuring system effectiveness. Tools and techniques for tracking agent activities and interactions include logging, visualization tools, and performance metrics.

For example, a dashboard could display the status of each agent, user preferences, and agent interactions, such as travel dates, flight recommendations, hotel options, and rental car suggestions. This provides a clear view of agent interactions and whether user preferences are being met.

Key aspects include:

- **Logging and Monitoring Tools**: Log each action taken by an agent, including details like the agent, action, time, and outcome. This data aids debugging and optimization.
- **Visualization Tools**: Graphs or other visualizations can show information flow between agents, helping identify bottlenecks or inefficiencies.
- **Performance Metrics**: Track metrics like task completion time, throughput, and recommendation accuracy to identify areas for improvement.

## Multi-Agent Patterns

Here are some patterns for creating multi-agent applications:

### Group chat

This pattern is ideal for group chat applications where multiple agents communicate. Use cases include team collaboration, customer support, and social networking.

Agents represent users, exchanging messages via a messaging protocol. Messages can be routed through a central server (centralized architecture) or exchanged directly (decentralized architecture).

![Group chat](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.en.png)

### Hand-off

This pattern is useful for applications where agents hand off tasks to each other, such as customer support, task management, or workflow automation.

Agents represent tasks or workflow steps, passing tasks to others based on predefined rules.

![Hand off](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.en.png)

### Collaborative filtering

This pattern is for applications where agents collaborate to make recommendations. Each agent contributes based on its expertise.

For example, recommending stocks to buy:

- **Industry expert**: One agent specializes in a specific industry.
- **Technical analysis**: Another agent focuses on technical analysis.
- **Fundamental analysis**: A third agent handles fundamental analysis.

Together, they provide comprehensive recommendations.

![Recommendation](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.en.png)

## Scenario: Refund process

Consider a customer seeking a refund. Agents can be divided into those specific to the refund process and general agents usable elsewhere.

**Agents specific to the refund process**:

- **Customer agent**: Initiates the refund process.
- **Seller agent**: Processes the refund.
- **Payment agent**: Handles payment refunds.
- **Resolution agent**: Resolves issues during the refund process.
- **Compliance agent**: Ensures regulatory and policy compliance.

**General agents**:

- **Shipping agent**: Manages product returns and general shipping tasks.
- **Feedback agent**: Collects customer feedback, usable beyond refunds.
- **Escalation agent**: Handles issue escalation across processes.
- **Notification agent**: Sends updates to customers.
- **Analytics agent**: Analyzes refund-related data.
- **Audit agent**: Audits the refund process for accuracy.
- **Reporting agent**: Generates reports on refunds.
- **Knowledge agent**: Maintains a knowledge base for refunds and other processes.
- **Security agent**: Ensures process security.
- **Quality agent**: Monitors process quality.

These examples illustrate how to decide which agents to include in a multi-agent system.

## Assignment
Design a multi-agent system for a customer support process. Identify the agents involved in the process, their roles and responsibilities, and how they interact with each other. Consider both agents specific to the customer support process and general agents that can be used in other parts of your business.

> Think carefully before reading the solution below; you might need more agents than you initially expect.

> TIP: Consider the various stages of the customer support process and also think about agents required for any system.

## Solution

[Solution](./solution/solution.md)

## Knowledge checks

Question: When should you consider using multi-agents?

- [ ] A1: When you have a small workload and a simple task.
- [ ] A2: When you have a large workload
- [ ] A3: When you have a simple task.

[Solution quiz](./solution/solution-quiz.md)

## Summary

In this lesson, we explored the multi-agent design pattern, including the situations where multi-agents are suitable, the benefits of using multiple agents compared to a single agent, the fundamental components of implementing the multi-agent design pattern, and how to monitor the interactions between multiple agents.

### Have More Questions about the Multi-Agent Design Pattern?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to connect with other learners, attend office hours, and get your AI Agents questions answered.

## Additional resources

- 

## Previous Lesson

[Planning Design](../07-planning-design/README.md)

## Next Lesson

[Metacognition in AI Agents](../09-metacognition/README.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.