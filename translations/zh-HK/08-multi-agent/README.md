[![多智能體設計](../../../translated_images/zh-HK/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(按上方圖片以觀看本課堂的影片)_

# 多智能體設計模式

As soon as you start working on a project that involves multiple agents, you will need to consider the multi-agent design pattern. However, it might not be immediately clear when to switch to multi-agents and what the advantages are.

## 介紹

In this lesson, we're looking to answer the following questions:

- What are the scenarios where multi-agents are applicable to?
- What are the advantages of using multi-agents over just one singular agent doing multiple tasks?
- What are the building blocks of implementing the multi-agent design pattern?
- How do we have visibility to how the multiple agents are interacting with each other?

## 學習目標

After this lesson, you should be able to:

- Identify scenarios where multi-agents are applicable
- Recognize the advantages of using multi-agents over a singular agent.
- Comprehend the building blocks of implementing the multi-agent design pattern.

What's the bigger picture?

*多智能體是一種設計模式，讓多個智能體一起協作以達成共同目標*。

This pattern is widely used in various fields, including robotics, autonomous systems, and distributed computing.

## 適用多智能體的情境

So what scenarios are a good use case for using multi-agents? The answer is that there are many scenarios where employing multiple agents is beneficial especially in the following cases:

- **大量工作量**: 大量工作量可以被拆分成較小的任務並分派給不同的智能體，允許並行處理與更快速完成。舉例來說，像是大型資料處理工作。
- **複雜任務**: 複雜任務，如同大量工作量一樣，可以被拆解為較小的子任務並分派給不同的智能體，每個智能體專精於任務的特定面向。舉例來說，在自駕車情境中，不同智能體管理導航、障礙物偵測與與其他車輛的通訊。
- **多樣專業**: 不同智能體可以擁有不同的專業，使它們能比單一智能體更有效率地處理任務的各個面向。就此情況而言，一個很好的例子是在醫療領域，智能體可以分別負責診斷、治療計畫與病患監測。

## 使用多智能體相對於單一智能體的優勢

A single agent system could work well for simple tasks, but for more complex tasks, using multiple agents can provide several advantages:

- **專精**: 每個智能體可以針對特定任務專精。單一智能體缺乏專精意味著你會有一個什麼都能做但在面對複雜任務時可能不知所措的智能體。例如，它可能最終做了一個它並非最適合的任務。
- **可擴展性**: 與其讓單一智能體過載，透過增加更多智能體來擴展系統會更容易。
- **容錯性**: 如果一個智能體失效，其他智能體仍可繼續運作，確保系統可靠性。

Let's take an example, let's book a trip for a user. A single agent system would have to handle all aspects of the trip booking process, from finding flights to booking hotels and rental cars. To achieve this with a single agent, the agent would need to have tools for handling all these tasks. This could lead to a complex and monolithic system that is difficult to maintain and scale. A multi-agent system, on the other hand, could have different agents specialized in finding flights, booking hotels, and rental cars. This would make the system more modular, easier to maintain, and scalable.

Compare this to a travel bureau run as a mom-and-pop store versus a travel bureau run as a franchise. The mom-and-pop store would have a single agent handling all aspects of the trip booking process, while the franchise would have different agents handling different aspects of the trip booking process.

## 實作多智能體設計模式的構成要素

Before you can implement the multi-agent design pattern, you need to understand the building blocks that make up the pattern.

Let's make this more concrete by again looking at the example of booking a trip for a user. In this case, the building blocks would include:

- **智能體通訊**: 負責尋找航班、預訂飯店與租車的智能體需要彼此通訊並分享使用者的偏好與限制。你需要決定用於此通訊的協定與方法。具體而言，尋找航班的智能體需要與預訂飯店的智能體溝通以確保飯店的預訂日期與航班相同。這代表智能體需要共享使用者的旅行日期，因此你需要決定 *哪些智能體在共享資訊以及如何共享資訊*。
- **協調機制**: 智能體需要協調它們的行動以確保使用者的偏好與限制被滿足。使用者的偏好可能是想要一間靠近機場的飯店，而限制可能是租車只在機場提供。這表示預訂飯店的智能體需要與預訂租車的智能體協調以滿足這些偏好與限制。這代表你需要決定 *智能體如何協調它們的行動*。
- **智能體架構**: 智能體需要具備內部結構來做決策並從與使用者的互動中學習。這表示尋找航班的智能體需要具備內部結構來決定要向使用者推薦哪些航班。這代表你需要決定 *智能體如何做決策並從與使用者的互動中學習*。智能體如何學習與改進的範例可能是：尋找航班的智能體可以使用機器學習模型，根據使用者過去的偏好來推薦航班。
- **多智能體互動的可視性**: 你需要能夠看見多個智能體如何互動。這表示你需要有追蹤智能體活動與互動的工具與技術。這可以採用日誌與監控工具、視覺化工具與效能指標的形式。
- **多智能體模式**: 在實作多智能體系統時有不同的模式，例如集中式、去中心化與混合式架構。你需要決定哪種模式最適合你的使用情境。
- **人類介入**: 在大多數情況下，你會讓人類參與流程，你需要指示智能體何時尋求人類介入。這可能是使用者要求特定飯店或航班而智能體尚未推薦，或在預訂航班或飯店前要求確認。

## 對多智能體互動的可視性

It's important that you have visibility into how the multiple agents are interacting with each other. This visibility is essential for debugging, optimizing, and ensuring the overall system's effectiveness. To achieve this, you need to have tools and techniques for tracking agent activities and interactions. This could be in the form of logging and monitoring tools, visualization tools, and performance metrics.

For example, in the case of booking a trip for a user, you could have a dashboard that shows the status of each agent, the user's preferences and constraints, and the interactions between agents. This dashboard could show the user's travel dates, the flights recommended by the flight agent, the hotels recommended by the hotel agent, and the rental cars recommended by the rental car agent. This would give you a clear view of how the agents are interacting with each other and whether the user's preferences and constraints are being met.

Let's look at each of these aspects more in detail.

- **Logging and Monitoring Tools**: You want to have logging done for each action taken by an agent. A log entry could store information on the agent that took the action, the action taken, the time the action was taken, and the outcome of the action. This information can then be used for debugging, optimizing and more.

- **Visualization Tools**: Visualization tools can help you see the interactions between agents in a more intuitive way. For example, you could have a graph that shows the flow of information between agents. This could help you identify bottlenecks, inefficiencies, and other issues in the system.

- **Performance Metrics**: Performance metrics can help you track the effectiveness of the multi-agent system. For example, you could track the time taken to complete a task, the number of tasks completed per unit of time, and the accuracy of the recommendations made by the agents. This information can help you identify areas for improvement and optimize the system.

## 多智能體模式

Let's dive into some concrete patterns we can use to create multi-agent apps. Here are some interesting patterns worth considering:

### 群組聊天

This pattern is useful when you want to create a group chat application where multiple agents can communicate with each other. Typical use cases for this pattern include team collaboration, customer support, and social networking.

In this pattern, each agent represents a user in the group chat, and messages are exchanged between agents using a messaging protocol. The agents can send messages to the group chat, receive messages from the group chat, and respond to messages from other agents.

This pattern can be implemented using a centralized architecture where all messages are routed through a central server, or a decentralized architecture where messages are exchanged directly.

![群組聊天](../../../translated_images/zh-HK/multi-agent-group-chat.ec10f4cde556babd.webp)

### 交接

This pattern is useful when you want to create an application where multiple agents can hand off tasks to each other.

Typical use cases for this pattern include customer support, task management, and workflow automation.

In this pattern, each agent represents a task or a step in a workflow, and agents can hand off tasks to other agents based on predefined rules.

![交接](../../../translated_images/zh-HK/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### 協同過濾

This pattern is useful when you want to create an application where multiple agents can collaborate to make recommendations to users.

Why you would want multiple agents to collaborate is because each agent can have different expertise and can contribute to the recommendation process in different ways.

Let's take an example where a user wants a recommendation on the best stock to buy on the stock market.

- **產業專家**:. One agent could be an expert in a specific industry.
- **技術分析**: Another agent could be an expert in technical analysis.
- **基本面分析**: and another agent could be an expert in fundamental analysis. By collaborating, these agents can provide a more comprehensive recommendation to the user.

![推薦](../../../translated_images/zh-HK/multi-agent-filtering.d959cb129dc9f608.webp)

## 範例情境：退款流程

Consider a scenario where a customer is trying to get a refund for a product, there can be quite a few agents involved in this process but let's divide it up between agents specific for this process and general agents that can be used in other processes.

**針對退款流程的專屬智能體**:

Following are some agents that could be involved in the refund process:

- **顧客智能體**: This agent represents the customer and is responsible for initiating the refund process.
- **賣方智能體**: This agent represents the seller and is responsible for processing the refund.
- **付款智能體**: This agent represents the payment process and is responsible for refunding the customer's payment.
- **調解智能體**: This agent represents the resolution process and is responsible for resolving any issues that arise during the refund process.
- **合規智能體**: This agent represents the compliance process and is responsible for ensuring that the refund process complies with regulations and policies.

**通用智能體**:

These agents can be used by other parts of your business.

- **運送智能體**: This agent represents the shipping process and is responsible for shipping the product back to the seller. This agent can be used both for the refund process and for general shipping of a product via a purchase for example.
- **回饋智能體**: This agent represents the feedback process and is responsible for collecting feedback from the customer. Feedback could be had at any time and not just during the refund process.
- **升級智能體**: This agent represents the escalation process and is responsible for escalating issues to a higher level of support. You can use this type of agent for any process where you need to escalate an issue.
- **通知智能體**: This agent represents the notification process and is responsible for sending notifications to the customer at various stages of the refund process.
- **分析智能體**: This agent represents the analytics process and is responsible for analyzing data related to the refund process.
- **稽核智能體**: This agent represents the audit process and is responsible for auditing the refund process to ensure that it is being carried out correctly.
- **報告智能體**: This agent represents the reporting process and is responsible for generating reports on the refund process.
- **知識智能體**: This agent represents the knowledge process and is responsible for maintaining a knowledge base of information related to the refund process. This agent could be knowledgeable both on refunds and other parts of your business.
- **安全智能體**: This agent represents the security process and is responsible for ensuring the security of the refund process.
- **品質智能體**: This agent represents the quality process and is responsible for ensuring the quality of the refund process.

There's quite a few agents listed previously both for the specific refund process but also for the general agents that can be used in other parts of your business. Hopefully this gives you an idea on how you can decide on which agents to use in your multi-agent system.

## 作業

Design a multi-agent system for a customer support process. Identify the agents involved in the process, their roles and responsibilities, and how they interact with each other. Consider both agents specific to the customer support process and general agents that can be used in other parts of your business.
> 在閱讀以下解答之前先想一想，你可能比想像中需要更多的代理。
> 提示：想一想客戶支援流程的不同階段，並考慮任何系統所需的代理。

## Solution

[解決方案](./solution/solution.md)

## Knowledge checks

Question: When should you consider using multi-agents?

- [ ] A1: 當你有少量工作負載且任務簡單時。
- [ ] A2: 當你有大量工作負載
- [ ] A3: 當任務簡單時。

[解答測驗](./solution/solution-quiz.md)

## Summary

在本課中，我們探討了多代理設計模式，包括適用多代理的情境、使用多代理相較於單一代理的優勢、實作多代理設計模式的組成要素，以及如何掌握多個代理之間互動的可見性。

### Got More Questions about the Multi-Agent Design Pattern?

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流、參加辦公時間，並獲得你關於 AI 代理的問題解答。

## Additional resources

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework 文件</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">代理式設計模式</a>


## Previous Lesson

[規劃設計](../07-planning-design/README.md)

## Next Lesson

[AI 代理中的元認知](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原文（母語版本）應視為具權威性的版本。如涉及重要資訊，建議委託專業人工翻譯。我們對因使用本翻譯而引致的任何誤解或誤釋概不承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->