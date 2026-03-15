[![可信赖的 AI 代理](../../../translated_images/zh-CN/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(点击上方图片观看本课视频)_

# 构建可信赖的 AI 代理

## 介绍

本课将涵盖：

- 如何构建和部署安全有效的 AI 代理
- 开发 AI 代理时的重要安全考虑
- 开发 AI 代理时如何维护数据和用户隐私

## 学习目标

完成本课后，您将了解如何：

- 识别和减轻创建 AI 代理时的风险
- 实施安全措施，确保数据和访问权限的正确管理
- 创建维护数据隐私并提供优质用户体验的 AI 代理

## 安全

首先来看如何构建安全的代理应用。安全意味着 AI 代理按设计执行。作为代理应用的构建者，我们有方法和工具最大化安全性：

### 构建系统消息框架

如果您曾用大型语言模型（LLM）构建 AI 应用，您会知道设计坚固的系统提示或系统消息有多重要。这些提示设定了元规则、指令和指南，指导 LLM 如何与用户和数据交互。

对于 AI 代理，系统提示更为重要，因为 AI 代理需要极其具体的指令来完成我们为其设计的任务。

为了创建可扩展的系统提示，我们可以使用一个系统消息框架来构建应用中的一个或多个代理：

![构建系统消息框架](../../../translated_images/zh-CN/system-message-framework.3a97368c92d11d68.webp)

#### 步骤 1：创建元系统消息

元提示将被 LLM 用来生成我们创建的代理的系统提示。我们将其设计为模板，以便高效创建多个代理（如有需要）。

这是我们给 LLM 的一个元系统消息示例：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 步骤 2：创建基本提示

下一步是创建一个基本提示，描述 AI 代理。您应包括代理的角色、代理将完成的任务以及代理的其他职责。

示例：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 步骤 3：向 LLM 提供基本系统消息

现在我们可以通过将元系统消息和我们的基本系统消息一同作为系统消息来优化它。

这将生成一个更适合指导 AI 代理的系统消息：

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### 步骤 4：迭代和改进

该系统消息框架的价值在于能够更容易地扩展多代理系统消息的创建，同时随着时间推移改进系统消息。很少有系统消息能在首次使用时就满足完整用例。通过更改基本系统消息并运行系统，可以进行小幅调整和改进，以便比较和评估结果。

## 理解威胁

要构建可信赖的 AI 代理，了解并缓解对 AI 代理的风险和威胁非常重要。我们只看部分对 AI 代理的不同威胁，以及如何更好地进行规划和准备。

![理解威胁](../../../translated_images/zh-CN/understanding-threats.89edeada8a97fc0f.webp)

### 任务和指令

**描述：** 攻击者试图通过提示或操纵输入更改 AI 代理的指令或目标。

**缓解措施：** 执行验证检查和输入过滤，检测潜在危险提示，避免其被 AI 代理处理。由于这些攻击通常需要频繁与代理交互，限制对话轮数也是防止此类攻击的方法。

### 访问关键系统

**描述：** 如果 AI 代理访问存储敏感数据的系统和服务，攻击者可能会破坏代理与这些服务之间的通信。这些可能是直接攻击，也可能是通过代理间接获取这些系统信息的尝试。

**缓解措施：** AI 代理应只按需访问系统，以防止此类攻击。代理与系统间的通信也应保持安全。实施身份验证和访问控制是保护这类信息的另一种方式。

### 资源和服务过载

**描述：** AI 代理可访问不同工具和服务以完成任务。攻击者可利用此能力通过 AI 代理发送大量请求来攻击这些服务，可能导致系统故障或高额费用。

**缓解措施：** 实施策略限制 AI 代理对服务请求次数。限制对话轮数和请求次数也是防止此类攻击的方法。

### 知识库投毒

**描述：** 这类攻击不直接针对 AI 代理，而是针对 AI 代理使用的知识库和其他服务。可能破坏 AI 代理在完成任务时使用的数据或信息，导致对用户产生偏见或意外响应。

**缓解措施：** 定期验证 AI 代理工作流中使用的数据。确保数据访问安全，仅由可信人员更改，以避免此类攻击。

### 级联错误

**描述：** AI 代理访问各种工具和服务以完成任务。攻击者引发的错误可能导致连接系统故障，使攻击范围更广且更难排查。

**缓解措施：** 避免方法之一是让 AI 代理在受限环境中运行，比如在 Docker 容器中执行任务，防止直接系统攻击。创建回退机制和重试逻辑也是防止更大系统故障的方法。

## 人机协作

构建可信赖 AI 代理系统的另一有效方法是利用人机协作。它创建了一个流程，允许用户在运行中向代理提供反馈。用户本质上充当多代理系统中的代理，通过批准或终止运行过程进行交互。

![人机协作](../../../translated_images/zh-CN/human-in-the-loop.5f0068a678f62f4f.webp)

以下代码片段展示使用 Microsoft Agent Framework 实现此概念：

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# 创建带有人类参与审批的提供者
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# 创建带有人类审批步骤的代理
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# 用户可以审核并批准响应
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 结论

构建可信赖的 AI 代理需要精心设计、强健的安全措施和持续迭代。通过实施结构化元提示系统、理解潜在威胁以及应用缓解策略，开发者可以创建既安全又有效的 AI 代理。此外，融入人机协作方式确保 AI 代理始终符合用户需求，同时最小化风险。随着 AI 持续发展，保持对安全、隐私和伦理问题的积极关注，将是培养 AI 驱动系统信任与可靠性的关键。

### 对构建可信赖 AI 代理有更多疑问吗？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者交流，参加办公时间，解答您的 AI 代理问题。

## 额外资源

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">负责任 AI 概述</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成式 AI 模型和 AI 应用的评估</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全系统消息</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">风险评估模板</a>

## 上一课

[Agentic RAG](../05-agentic-rag/README.md)

## 下一课

[规划设计模式](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力保证准确性，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而引起的任何误解或错误解释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->