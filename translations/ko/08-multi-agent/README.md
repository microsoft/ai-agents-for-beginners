[![멀티 에이전트 설계](../../../translated_images/ko/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(위의 이미지를 클릭하여 이 수업의 비디오를 보세요)_

# 멀티 에이전트 디자인 패턴

As soon as you start working on a project that involves multiple agents, you will need to consider the multi-agent design pattern. However, it might not be immediately clear when to switch to multi-agents and what the advantages are.

## 소개

In this lesson, we're looking to answer the following questions:

- What are the scenarios where multi-agents are applicable to?
- What are the advantages of using multi-agents over just one singular agent doing multiple tasks?
- What are the building blocks of implementing the multi-agent design pattern?
- How do we have visibility to how the multiple agents are interacting with each other?

## 학습 목표

After this lesson, you should be able to:

- Identify scenarios where multi-agents are applicable
- Recognize the advantages of using multi-agents over a singular agent.
- Comprehend the building blocks of implementing the multi-agent design pattern.

What's the bigger picture?

*멀티 에이전트는 여러 에이전트가 공동의 목표를 달성하기 위해 함께 작업할 수 있게 하는 디자인 패턴입니다*.

This pattern is widely used in various fields, including robotics, autonomous systems, and distributed computing.

## 멀티 에이전트가 적용되는 시나리오

So what scenarios are a good use case for using multi-agents? The answer is that there are many scenarios where employing multiple agents is beneficial especially in the following cases:

- **Large workloads**: Large workloads can be divided into smaller tasks and assigned to different agents, allowing for parallel processing and faster completion. An example of this is in the case of a large data processing task.
- **Complex tasks**: Complex tasks, like large workloads, can be broken down into smaller subtasks and assigned to different agents, each specializing in a specific aspect of the task. A good example of this is in the case of autonomous vehicles where different agents manage navigation, obstacle detection, and communication with other vehicles.
- **Diverse expertise**: Different agents can have diverse expertise, allowing them to handle different aspects of a task more effectively than a single agent. For this case, a good example is in the case of healthcare where agents can manage diagnostics, treatment plans, and patient monitoring.

## 단일 에이전트보다 멀티 에이전트를 사용하는 장점

A single agent system could work well for simple tasks, but for more complex tasks, using multiple agents can provide several advantages:

- **Specialization**: Each agent can be specialized for a specific task. Lack of specialization in a single agent means you have an agent that can do everything but might get confused on what to do when faced with a complex task. It might for example end up doing a task that it is not best suited for.
- **Scalability**: It is easier to scale systems by adding more agents rather than overloading a single agent.
- **Fault Tolerance**: If one agent fails, others can continue functioning, ensuring system reliability.

Let's take an example, let's book a trip for a user. A single agent system would have to handle all aspects of the trip booking process, from finding flights to booking hotels and rental cars. To achieve this with a single agent, the agent would need to have tools for handling all these tasks. This could lead to a complex and monolithic system that is difficult to maintain and scale. A multi-agent system, on the other hand, could have different agents specialized in finding flights, booking hotels, and rental cars. This would make the system more modular, easier to maintain, and scalable.

Compare this to a travel bureau run as a mom-and-pop store versus a travel bureau run as a franchise. The mom-and-pop store would have a single agent handling all aspects of the trip booking process, while the franchise would have different agents handling different aspects of the trip booking process.

## 멀티 에이전트 디자인 패턴 구현의 구성 요소

Before you can implement the multi-agent design pattern, you need to understand the building blocks that make up the pattern.

Let's make this more concrete by again looking at the example of booking a trip for a user. In this case, the building blocks would include:

- **Agent Communication**: Agents for finding flights, booking hotels, and rental cars need to communicate and share information about the user's preferences and constraints. You need to decide on the protocols and methods for this communication. What this means concretely is that the agent for finding flights needs to communicate with the agent for booking hotels to ensure that the hotel is booked for the same dates as the flight. That means that the agents need to share information about the user's travel dates, meaning that you need to decide *which agents are sharing info and how they are sharing info*.
- **Coordination Mechanisms**: Agents need to coordinate their actions to ensure that the user's preferences and constraints are met. A user preference could be that they want a hotel close to the airport whereas a constraint could be that rental cars are only available at the airport. This means that the agent for booking hotels needs to coordinate with the agent for booking rental cars to ensure that the user's preferences and constraints are met. This means that you need to decide *how the agents are coordinating their actions*.
- **Agent Architecture**: Agents need to have the internal structure to make decisions and learn from their interactions with the user. This means that the agent for finding flights needs to have the internal structure to make decisions about which flights to recommend to the user. This means that you need to decide *how the agents are making decisions and learning from their interactions with the user*. Examples of how an agent learns and improves could be that the agent for finding flights could use a machine learning model to recommend flights to the user based on their past preferences.
- **Visibility into Multi-Agent Interactions**: You need to have visibility into how the multiple agents are interacting with each other. This means that you need to have tools and techniques for tracking agent activities and interactions. This could be in the form of logging and monitoring tools, visualization tools, and performance metrics.
- **Multi-Agent Patterns**: There are different patterns for implementing multi-agent systems, such as centralized, decentralized, and hybrid architectures. You need to decide on the pattern that best fits your use case.
- **Human in the loop**: In most cases, you will have a human in the loop and you need to instruct the agents when to ask for human intervention. This could be in the form of a user asking for a specific hotel or flight that the agents have not recommended or asking for confirmation before booking a flight or hotel.

## 멀티 에이전트 상호작용에 대한 가시성

It's important that you have visibility into how the multiple agents are interacting with each other. This visibility is essential for debugging, optimizing, and ensuring the overall system's effectiveness. To achieve this, you need to have tools and techniques for tracking agent activities and interactions. This could be in the form of logging and monitoring tools, visualization tools, and performance metrics.

For example, in the case of booking a trip for a user, you could have a dashboard that shows the status of each agent, the user's preferences and constraints, and the interactions between agents. This dashboard could show the user's travel dates, the flights recommended by the flight agent, the hotels recommended by the hotel agent, and the rental cars recommended by the rental car agent. This would give you a clear view of how the agents are interacting with each other and whether the user's preferences and constraints are being met.

Let's look at each of these aspects more in detail.

- **Logging and Monitoring Tools**: You want to have logging done for each action taken by an agent. A log entry could store information on the agent that took the action, the action taken, the time the action was taken, and the outcome of the action. This information can then be used for debugging, optimizing and more.

- **Visualization Tools**: Visualization tools can help you see the interactions between agents in a more intuitive way. For example, you could have a graph that shows the flow of information between agents. This could help you identify bottlenecks, inefficiencies, and other issues in the system.

- **Performance Metrics**: Performance metrics can help you track the effectiveness of the multi-agent system. For example, you could track the time taken to complete a task, the number of tasks completed per unit of time, and the accuracy of the recommendations made by the agents. This information can help you identify areas for improvement and optimize the system.

## 멀티 에이전트 패턴

Let's dive into some concrete patterns we can use to create multi-agent apps. Here are some interesting patterns worth considering:

### 그룹 채팅

This pattern is useful when you want to create a group chat application where multiple agents can communicate with each other. Typical use cases for this pattern include team collaboration, customer support, and social networking.

In this pattern, each agent represents a user in the group chat, and messages are exchanged between agents using a messaging protocol. The agents can send messages to the group chat, receive messages from the group chat, and respond to messages from other agents.

This pattern can be implemented using a centralized architecture where all messages are routed through a central server, or a decentralized architecture where messages are exchanged directly.

![그룹 채팅](../../../translated_images/ko/multi-agent-group-chat.ec10f4cde556babd.webp)

### 핸드오프

This pattern is useful when you want to create an application where multiple agents can hand off tasks to each other.

Typical use cases for this pattern include customer support, task management, and workflow automation.

In this pattern, each agent represents a task or a step in a workflow, and agents can hand off tasks to other agents based on predefined rules.

![핸드오프](../../../translated_images/ko/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### 협업 필터링

This pattern is useful when you want to create an application where multiple agents can collaborate to make recommendations to users.

Why you would want multiple agents to collaborate is because each agent can have different expertise and can contribute to the recommendation process in different ways.

Let's take an example where a user wants a recommendation on the best stock to buy on the stock market.

- **Industry expert**:. One agent could be an expert in a specific industry.
- **Technical analysis**: Another agent could be an expert in technical analysis.
- **Fundamental analysis**: and another agent could be an expert in fundamental analysis. By collaborating, these agents can provide a more comprehensive recommendation to the user.

![추천](../../../translated_images/ko/multi-agent-filtering.d959cb129dc9f608.webp)

## 시나리오: 환불 프로세스

Consider a scenario where a customer is trying to get a refund for a product, there can be quite a few agents involved in this process but let's divide it up between agents specific for this process and general agents that can be used in other processes.

**환불 프로세스에 특화된 에이전트**:

Following are some agents that could be involved in the refund process:

- **Customer agent**: This agent represents the customer and is responsible for initiating the refund process.
- **Seller agent**: This agent represents the seller and is responsible for processing the refund.
- **Payment agent**: This agent represents the payment process and is responsible for refunding the customer's payment.
- **Resolution agent**: This agent represents the resolution process and is responsible for resolving any issues that arise during the refund process.
- **Compliance agent**: This agent represents the compliance process and is responsible for ensuring that the refund process complies with regulations and policies.

**일반 에이전트**:

These agents can be used by other parts of your business.

- **Shipping agent**: This agent represents the shipping process and is responsible for shipping the product back to the seller. This agent can be used both for the refund process and for general shipping of a product via a purchase for example.
- **Feedback agent**: This agent represents the feedback process and is responsible for collecting feedback from the customer. Feedback could be had at any time and not just during the refund process.
- **Escalation agent**: This agent represents the escalation process and is responsible for escalating issues to a higher level of support. You can use this type of agent for any process where you need to escalate an issue.
- **Notification agent**: This agent represents the notification process and is responsible for sending notifications to the customer at various stages of the refund process.
- **Analytics agent**: This agent represents the analytics process and is responsible for analyzing data related to the refund process.
- **Audit agent**: This agent represents the audit process and is responsible for auditing the refund process to ensure that it is being carried out correctly.
- **Reporting agent**: This agent represents the reporting process and is responsible for generating reports on the refund process.
- **Knowledge agent**: This agent represents the knowledge process and is responsible for maintaining a knowledge base of information related to the refund process. This agent could be knowledgeable both on refunds and other parts of your business.
- **Security agent**: This agent represents the security process and is responsible for ensuring the security of the refund process.
- **Quality agent**: This agent represents the quality process and is responsible for ensuring the quality of the refund process.

There's quite a few agents listed previously both for the specific refund process but also for the general agents that can be used in other parts of your business. Hopefully this gives you an idea on how you can decide on which agents to use in your multi-agent system.

## 과제

Design a multi-agent system for a customer support process. Identify the agents involved in the process, their roles and responsibilities, and how they interact with each other. Consider both agents specific to the customer support process and general agents that can be used in other parts of your business.
> 읽기 전에 잠시 생각해 보세요. 다음 해답을 읽기 전에, 생각보다 더 많은 에이전트가 필요할 수 있습니다.

> 팁: 고객 지원 프로세스의 다양한 단계와 시스템에 필요한 에이전트를 고려해 보세요.

## 솔루션

[솔루션](./solution/solution.md)

## 지식 점검

Question: 멀티 에이전트를 언제 고려해야 하나요?

- [ ] A1: 작업량이 적고 작업이 단순할 때.
- [ ] A2: 작업량이 많을 때
- [ ] A3: 작업이 단순할 때.

[솔루션 퀴즈](./solution/solution-quiz.md)

## 요약

이 강의에서는 멀티-에이전트 설계 패턴을 살펴보았습니다. 멀티-에이전트가 적용되는 시나리오, 단일 에이전트보다 멀티-에이전트를 사용할 때의 이점, 멀티-에이전트 설계 패턴을 구현하는 구성 요소, 그리고 여러 에이전트가 서로 어떻게 상호작용하는지에 대한 가시성을 확보하는 방법을 다루었습니다.

### 멀티-에이전트 설계 패턴에 대해 더 궁금한 점이 있나요?

다른 학습자들과 만나고, 오피스 아워에 참석하고, AI 에이전트 관련 질문에 답을 얻으려면 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)에 참여하세요.

## 추가 자료

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework 문서</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">에이전틱 설계 패턴</a>


## 이전 강의

[Planning Design](../07-planning-design/README.md)

## 다음 강의

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
면책사항:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의해 주십시오. 원문(원어로 된 문서)을 정본으로 간주해야 합니다. 중요한 정보의 경우 전문 번역가에 의한 번역을 권장합니다. 이 번역의 사용으로 인해 발생한 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->