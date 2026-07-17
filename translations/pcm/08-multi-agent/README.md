[![Multi-Agent Design](../../../translated_images/pcm/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Click the image above to view video of this lesson)_

# Multi-agent design patterns

As soon as you start to wok on project wey get multiple agents, you go need to reason about multi-agent design pattern. But e no too clear immediately when to switch to multi-agents and wetin advantages dem be.

## Introduction

For dis lesson, we wan answer di questions dem:

- Wetin be di scenarios wey multi-agents fit make sense?
- Wetin be di advantages of use multi-agents rather than one single agent wey dey do plenty task?
- Wetin be di building blocks to implement multi-agent design pattern?
- How we fit see how di multiple agents dey interact with each oda?

## Learning Goals

After dis lesson, you suppose fit:

- Identify scenarios wey multi-agents fit work well.
- Recognize advantages of use multi-agents over single agent.
- Understand building blocks to implement multi-agent design pattern.

Wetin be di bigger picture?

*Multi agents na design pattern wey allow different agents to work together to achieve one target.*

Di pattern dey widely used for many areas like robotics, autonomous systems, and distributed computing.

## Scenarios Weh Multi-Agents Fit Work

Wetin be good scenarios to use multi-agents? Di answer be say many situations get advantage when you use plenty agents, especially for these cases:

- **Big workload**: You fit divide big workload into smaller task dem, then assign different agents to do am, so e fit run faster. Example na for big data processing task.
- **Complex tasks**: Complex tasks fit break down into small small subtasks, each agent go sabi one part of di task well well. Example na autonomous vehicles wey get different agents to manage navigation, obstacle detection, and communication with other vehicles.
- **Different expertise**: Different agents fit get different skills to handle parts of di task better than just one agent. Like for healthcare where agents fit handle diagnostics, treatment plans, and patient monitoring.

## Advantages of Using Multi-Agents Over Single Agent

Single agent fit run simple tasks well, but for complex task, multiple agents get many advantages:

- **Specialization**: Each agent fit specialize for one task. If one agent no specialize, e fit confuse when e face complex task, e fit do wrong task.
- **Scalability**: E easier to add more agents than overload one agent.
- **Fault Tolerance**: If one agent fail, others fit still dey work, so system no go crash.

Make we use example: we wan book trip for one user. Single agent system go handle everything like finding flights, booking hotel and rental cars. To fit do all these, agent go need many tools, e fit make system complex and hard to maintain. But multi-agent system fit get one agent for flights, one for hotels, one for rental cars. That one go make system modular, easy to maintain, and fit scale.

Compare am to travel bureau wey be mom-and-pop shop vs travel bureau wey be franchise. Mom-and-pop get one agent wey dey handle everything. Franchise get different agents to handle different parts of trip booking.

## Building Blocks to Implement Multi-Agent Design Pattern

Before you fit implement multi-agent design pattern, you need sabi di building blocks wey dey inside.

Make we use example again: booking trip for user. Di building blocks include:

- **Agent Communication**: Agents wey dey find flights, book hotel and rental cars need talk and share info about user preferences and constraints. You go decide how dem go communicate. Like flight agent go communicate with hotel agent to make sure say hotel booking match flight date. So agents need share info about travel dates and you must decide *which agents dey share info and how dem dey do am*.
- **Coordination Mechanisms**: Agents need coordinate their work to satisfy user preferences and constraints. For example, user fit want hotel near airport but rental cars fit only dey airport. So hotel booking agent need coordinate with rental car agent to meet user expectation. You must decide *how agents dey coordinate their actions*.
- **Agent Architecture**: Agents need one internal structure to fit make decisions and learn from user interaction. Flight agent go need structure to decide which flights to recommend. So you must decide *how agents dey make decisions and learn*. Example, flight agent fit use machine learning model to recommend flights based on user past preferences.
- **Visibility into Multi-Agent Interactions**: You need see how multiple agents dey interact. That one mean you need tools to track agent activities and interaction. This fit be logging tools, monitoring, visualization, and performance metrics.
- **Multi-Agent Patterns**: Different patterns dey to implement multi-agent systems like centralized, decentralized, and hybrid architectures. You must pick pattern wey best suit your use case.
- **Human in the loop**: Most times human go dey involved, you need tell agents when to ask human for help. Example, user fit ask for specific hotel or flight wey agents no recommend or confirm something before booking.

## Visibility into Multi-Agent Interactions

E important make you fit see how different agents dey interact. This visibility dey help to debug, optimize and make system effective. To do dis, you need tools and technique to track agent activities. This fit be logging, monitoring, visualization tools, and performance metrics.

Example, for booking trip for user, you fit get dashboard wey show status of each agent, user preferences, constraints, and how agents dey interact. Dashboard fit show travel dates, flights flight agent recommend, hotels hotel agent recommend, rental cars rental car agent recommend. This one go clear how agents dey work together and if dem meet user needs.

Make we look each aspect in detail.

- **Logging and Monitoring Tools**: You want keep log for each action agent take. Log go show which agent do am, action, time and outcome. Dis info fit use for debugging, optimization and more.

- **Visualization Tools**: Visualization tools fit help you see how agents dey interact in better way. Like graph wey show info flow between agents. E fit help you find bottlenecks, inefficiencies and other system wahala.

- **Performance Metrics**: Performance metrics fit help you track how effective multi-agent system be. Like time to complete task, number of tasks per time, accuracy of agents recommendation. Dis fit help improve and optimize system.

## Multi-Agent Patterns

Make we enter some clear patterns wey fit use to create multi-agent apps. Here be some wey good to consider:

### Group chat

Dis pattern useful if you wan build group chat app where many agents fit talk to each other. Common use cases include team work, customer support, and social networking.

For dis pattern, every agent represent one user for group chat and dem dey send messages to each other using messaging protocol. Agents fit send messages to group, receive messages from group, and reply to messages from other agents.

Dis pattern fit implement by centralized architecture where all messages go through central server, or decentralized wen messages dey exchange directly.

![Group chat](../../../translated_images/pcm/multi-agent-group-chat.ec10f4cde556babd.webp)

### Hand-off

Dis pattern dey useful if you want build app where many agents fit hand over tasks to each other.

Common use cases na customer support, task management, and workflow automation.

For dis pattern, each agent represent one task or step for workflow, and agents fit hand off tasks to oda agents based on rules wey dem don set before.

![Hand off](../../../translated_images/pcm/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Collaborative filtering

Dis pattern dey useful if you wan create app where multiple agents fit work together to give recommendations to users.

Reason why you go want multiple agents collaborate na because each agent fit get different expertise and fit contribute for recommendation process different ways.

Example be say user want recommendation on best stock to buy for stock market.

- **Industry expert**: One agent fit be expert for one specific industry.
- **Technical analysis**: Another agent fit be expert for technical analysis.
- **Fundamental analysis**: Another agent fit be expert for fundamental analysis. When dem collaborate, dem fit give user more complete recommendation.

![Recommendation](../../../translated_images/pcm/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Refund process

Imagine say customer dey try get refund for product, many agents fit dey involved but make we split am between agents wey specific for refund process and agents wey general for other business parts.

**Agents wey specific for refund process**:

These agents fit dey involved for refund:

- **Customer agent**: Agent wey represent customer, e dey start refund process.
- **Seller agent**: Agent wey represent seller, e dey process refund.
- **Payment agent**: Agent wey represent payment, e dey give refund back to customer.
- **Resolution agent**: Agent wey represent resolution process, e dey solve any problems wey come up during refund.
- **Compliance agent**: Agent wey make sure say refund process dey follow laws and policies.

**General agents**:

These agents fit work for other business parts too.

- **Shipping agent**: Agent wey handle shipping, e dey send product back to seller. Agent fit work for refund and general shipping for product purchase.
- **Feedback agent**: Agent wey collect customer feedback. E fit happen anytime no be only for refund.
- **Escalation agent**: Agent wey dey escalate issues to higher support level. Fit use this agent anytime you need escalate problem.
- **Notification agent**: Agent wey dey send notifications to customer during refund stages.
- **Analytics agent**: Agent wey analyze refund data.
- **Audit agent**: Agent wey audit refund process to ensure say dem dey do am well.
- **Reporting agent**: Agent wey generate reports on refund process.
- **Knowledge agent**: Agent wey maintain knowledge base for refund and other business info.
- **Security agent**: Agent wey ensure security of refund process.
- **Quality agent**: Agent wey ensure quality of refund process.

Many agents dem list for refund process and some general agents for other business parts. Hope dis one help you know how to decide which agents to use for your multi-agent system.

## Assignment

Design multi-agent system for customer support process. Identify agents wey involved, their roles and responsibilities, and how dem dey interact. Consider both agents specific for customer support and general agents wey fit work for other business parts.


> Make you reason small before you read dis solution, you fit need more agents pass wetin you dey think.

> TIP: Reason about di different stages for customer support process and also think about agents wey you go need for any system.

## Solution

[Solution](./solution/solution.md)

## Knowledge checks

### Question 1

Which kain scenario be di best fit for multi-agent system?

- [ ] A1: One support bot dey answer common questions with one knowledge base and small set of tools.
- [ ] A2: Refund workflow need separate fraud, payment, and compliance roles, each get him own tools, and dem results must dey coordinated.
- [ ] A3: Same simple classification request dey come thousands times per hour.

### Question 2

When one single agent usually better choice?

- [ ] A1: Di work fit be handled with one set of instructions and tools, without need specialist handoffs.
- [ ] A2: Di agent get access to more than one tool.
- [ ] A3: Di workflow need separate roles with different permissions and independent audit trails.

[Solution quiz](./solution/solution-quiz.md)

## Summary

For dis lesson, we don look di multi-agent design pattern, including di scenarios wey multi-agents dey apply, di advantages of to use multi-agents over one single agent, di building blocks to implement di multi-agent design pattern, plus how to fit see how di multiple agents dey interact with each other.

### Get More Questions about di Multi-Agent Design Pattern?

Join di [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, attend office hours and get your AI Agents questions answered.

## Additional resources

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework documentation</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentic design patterns</a>


## Previous Lesson

[Planning Design](../07-planning-design/README.md)

## Next Lesson

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->