[![Multi-Agent Design](../../../translated_images/pcm/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik di pikcha wey dey up so to watch video of dis lesson)_

# Multi-agent design patterns

As you start work for project wey get plenti agents, you go need to think about di multi-agent design pattern. But e fit no be clear sharp sharp when you go switch to multi-agents and wetin be di better tins.

## Introduction

For dis lesson, we dey try answer di beta questions dem:

- Wetin be di kain better case wey multi-agents fit work for?
- Wetin be di better tins wey multi-agents get pass just one agent wey dey do plenti tins?
- Wetin be di building blocks for make di multi-agent design pattern work?
- How we go fit see how di multiple agents dey take dey yarn with one another?

## Learning Goals

After dis lesson, you go fit:

- Identify di situations wey multi-agents fit work
- Know di better tins wey multi-agents get pass single agent.
- Understand di building blocks wey dey for di multi-agent design pattern.

Wetin be di big picture?

*Multi agents na design pattern wey make plenti agents fit work together to reach one common goal*.

Dis pattern di popular for different tins like robotics, autonomous systems, and distributed computing.

## Scenarios Where Multi-Agents Are Applicable

So, wetin be di kain situations wey good to use multi-agents? Di answer be say plenti tins fit benefit from many agents especially for dis kain situations:

- **Big workload**: Big workload fit chop into small small tasks and assign to haf agents, so dem fit work for di same time and finish quick. One example na for big data processing wahala.
- **Complex tasks**: Complex tasks, like big workload, fit be divided into small small subtasks and each agent fit specialize for one part of di task. One good example na autonomous cars where different agents dey handle navigation, obstacle detection, and making chat with other cars.
- **Different skills**: Different agents fit get different skills, wey go make dem handle different parts of task better pass one agent alone. One example na healthcare where agents dey diagnose, plan treatment, and dey monitor patient.

## Advantages of Using Multi-Agents Over a Singular Agent

One agent fit do simple tasks well, but for tori wey complex, multiple agents fit give tins wey better:

- **Specialization**: Each agent fit specialize for one task. When one agent no get specialization, e fit do everything but fit confuse when task complex. E fit end up doing task wey e no sabi well.
- **Scalability**: E easy to add agents more than overload one agent.
- **Fault Tolerance**: If one agent spoil, other agents fit still work well make everything steady.

Make we take example, make we book trip for person. One agent go need handle every part of booking trip, from finding flight to booking hotel and car rental. Make one agent do all dis, e go get tools to handle all dis tin. E go make system complex and hard to maintain or add more things. Multi-agent system fit get agents wey dey specialize for flight finding, hotel booking, and car rental. E go make system modular, easy to maintain, and scalable.

Compare am to travel agency wey be mom-and-pop store versus franchise. Mom-and-pop store go get one agent wey dey handle all trip booking, but franchise go get different agents wey dey handle different parts of di trip.

## Building Blocks of Implementing the Multi-Agent Design Pattern

Before you fit run multi-agent design pattern, you need sabi the building blocks wey dey make di pattern.

Make we use example of booking trip for person. Di building blocks fit include:

- **Agent Communication**: Agents wey dey find flights, book hotels, and rent cars go need dey talk and share info about person preferences and limits. You need decide di way and protocol wey dem go take talk. For example, agent wey dey find flight go talk to agent wey dey book hotel make sure hotel book for same dates with flight. That one mean say agents go share info about travel dates, so you need decide *which agents go share info and how dem go take share am*.
- **Coordination Mechanisms**: Agents go need arrange their work make sure person preferences and limits balance. Person fit want hotel close to airport, but limit fit be say rental cars dey only for airport. So, hotel booking agent need to arrange wit rental car agent to make sure person preferences and limits balance. You go decide *how agents go arrange their actions*.
- **Agent Architecture**: Agents need structure inside to make decisions and learn from wetin person do. So flight agent go need structure to decide which flight to recommend. You go decide *how agents go take make decisions and learn from interaction with person*. Example na say flight agent fit use machine learning to recommend flight based on past preferences.
- **Visibility into Multi-Agent Interactions**: You need fit see how agents dey interact with each other. You go need tools and methods to follow agent activities and interaction. E fit be logging, monitoring tools, visualization, and performance metrics.
- **Multi-Agent Patterns**: Different patterns dey for multi-agent system like centralized, decentralized, and hybrid architectures. You go select pattern wey best for your use case.
- **Human in the loop**: Most time, human go dey inside di loop and you need tell agents when dem go ask human for help. E fit be like user dey ask for particular hotel or flight wey agents never recommend or ask for confirmation before booking.

## Visibility into Multi-Agent Interactions

E important to get way to see how agents dey interact. Dis visibility na key to debug, optimize, and make sure system dey work well. You need tools to follow agent activities and interactions. E fit be logging, monitoring, visualization, or performance metrics.

For example, to book trip for person, you fit get dashboard wey show status of every agent, user preferences and limits, and how agents dey talk to each other. Dashboard fit show travel dates, flights wey flight agent recommend, hotels wey hotel agent recommend, and rental cars wey car agent recommend. E go give you clear view how agents dey interact and if preferences and limits dey met.

Make we check these tins more.

- **Logging and Monitoring Tools**: You want make logging dey for every action wey agent do. Log fit store info about agent wey do action, action wey happen, time wey action happen, and result. Dis info fit help debugging and optimization.
- **Visualization Tools**: Visualization fit help you see interaction between agents well well. For example, graph fit show how info dey flow between agents. E fit help find bottlenecks, waste, and other wahala.
- **Performance Metrics**: Metrics fit help track how well multi-agent system dey work. For example, fit track time to finish task, how many tasks dem finish for one time, and accuracy of agents recommendations. Info fit help find where to improve and optimize system.

## Multi-Agent Patterns

Make we check some specific patterns for multi-agent apps. Here dey some wey dey interesting:

### Group chat

Dis pattern good if you want create group chat app make many agents fit yarn with each other. Di common use na team work, customer support, and social network.

For dis pattern, every agent dey represent one user for group chat, and messages dey pass between agents using messaging protocol. Agents fit send messages to group, receive messages, and reply other agents messages.

Dis pattern fit use centralized system where all messages pass one server, or decentralized system where messages pass direct.

![Group chat](../../../translated_images/pcm/multi-agent-group-chat.ec10f4cde556babd.webp)

### Hand-off

Dis pattern good if you want app wey many agents fit hand off task to one another.

Common uses na customer support, task management, and workflow automation.

For dis pattern, every agent represent one task or workflow step, and agents fit hand over tasks based on rules wey dem set before.

![Hand off](../../../translated_images/pcm/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Collaborative filtering

Dis pattern good if you want app wey many agents fit work together to make recommendation to users.

Why you want many agents collaborate na because every agent get different skill and fit help for recommendation the way different.

Make we look example where user want recommendation for best stock to buy for stock market.

- **Industry expert**: One agent fit be expert for one particular industry.
- **Technical analysis**: Another agent fit be expert for technical analysis.
- **Fundamental analysis**: Another agent fit be expert for fundamental analysis. If dem join hand, dem fit give better recommendation to user.

![Recommendation](../../../translated_images/pcm/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Refund process

Imagine one situation where customer dey try get refund for product, e get plenti agents wey fit dey involved but make we split am to agents wey true true dey for refund process and general agents wey fit work for other business parts too.

**Agents wey true true dey for refund process**:

Here be some agents wey fit dey for refund:

- **Customer agent**: Dis one represent customer and e dey start refund process.
- **Seller agent**: Dis one represent seller and e dey handle refund process.
- **Payment agent**: Dis one dey handle payment and e dey refund money to customer.
- **Resolution agent**: Dis one dey fix any issue wey fit happen for refund process.
- **Compliance agent**: Dis one dey make sure refund dey follow rules and policies.

**General agents**:

These agents fit use for other business parts too.

- **Shipping agent**: Dis one dey handle shipping and e dey send product back to seller. E fit use for refund and general product shipping.
- **Feedback agent**: Dis one dey collect feedback from customer anytime.
- **Escalation agent**: Dis one dey carry issues go better support if need be. You fit use dis agent for any process wey need escalation.
- **Notification agent**: Dis one dey send message to customer for different stages of refund.
- **Analytics agent**: Dis one dey analyze data about refund process.
- **Audit agent**: Dis one dey check refund process to make sure e correct.
- **Reporting agent**: Dis one dey make report about refund process.
- **Knowledge agent**: Dis one dey keep info about refund and other business knowledge.
- **Security agent**: Dis one dey make sure refund process dey safe.
- **Quality agent**: Dis one dey make sure refund process quality good.

You see say e get plenti agents for refund and general agents for other business parts. Hope dis fit help you decide how to choose agents for your multi-agent system.

## Assignment

Design multi-agent system for customer support process. Identify agents wey dey involved, diir roles and responsibilites, and how dem dey work with one another. Think about agents wey dey specific for customer support and general agents wey fit work for other business parts.
> Make you reason well before you read di solution wey dey below, you fit need more agents pass wetin you dey think.

> TIP: Reason di different stages for customer support process and also think about agents wey system go need.

## Solution

[Solution](./solution/solution.md)

## Knowledge checks

Question: When you suppose think about to use multi-agents?

- [ ] A1: When work no too much and task simple.
- [ ] A2: When work plenty
- [ ] A3: When task simple.

[Solution quiz](./solution/solution-quiz.md)

## Summary

For dis lesson, we don check multi-agent design pattern, including di cases wey multi-agents fit work, di advantages wey multi-agents get pass single agent, di building blocks to fit implement di multi-agent design pattern, and how to fit see how di different agents dey interact with each other.

### You Dey Get More Questions About Di Multi-Agent Design Pattern?

Join di [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, attend office hours and get your AI Agents questions answer.

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
Dis document na wetin AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) translate. Even though we try make e correct, abeg sabi say automatic translation fit get some mistakes or errors. Di original document for dia own language remain di main correct source. If na for important mata, make you use professional human translation. We no go take responsibility for any confusion or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->