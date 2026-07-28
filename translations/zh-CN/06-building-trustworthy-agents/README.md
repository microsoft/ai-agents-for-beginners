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

- 识别并减轻创建 AI 代理时的风险
- 实施安全措施以确保数据和访问权限得到适当管理
- 创建维护数据隐私并提供优质用户体验的 AI 代理

## 安全

让我们先看看如何构建安全的代理应用。安全意味着 AI 代理按照设计执行。作为代理应用的构建者，我们有方法和工具来最大化安全性：

### 建立系统消息框架

如果您曾使用大型语言模型（LLM）构建 AI 应用，您会明白设计强健的系统提示或系统消息的重要性。这些提示确定了元规则、指令和指南，指导 LLM 如何与用户和数据交互。

对于 AI 代理来说，系统提示更为重要，因为 AI 代理需要非常具体的指令来完成我们为其设计的任务。

为了创建可扩展的系统提示，我们可以使用系统消息框架来构建应用中的一个或多个代理：

![建立系统消息框架](../../../translated_images/zh-CN/system-message-framework.3a97368c92d11d68.webp)

#### 第一步：创建元系统消息

元提示将由 LLM 用来生成我们所创建代理的系统提示。我们将其设计为模板，以便能高效地创建多个代理（如果需要）。

以下是我们给 LLM 的一个元系统消息示例：

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 第二步：创建基础提示

下一步是创建一个基础提示来描述 AI 代理。您应包括代理的角色、代理将完成的任务，以及代理的其他职责。

以下是一个示例：

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 第三步：向 LLM 提供基础系统消息

现在我们可以通过提供元系统消息作为系统消息，并结合基础系统消息来优化该系统消息。

这样会生成一个更适合指导 AI 代理的系统消息：

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

#### 第四步：迭代与改进

该系统消息框架的价值在于可以更容易地扩展多个代理的系统消息创建，并随着时间推移改进您的系统消息。很少有系统消息会第一次就完全符合用例需求。通过更改基础系统消息并运行系统来进行小幅调整和改进，可让您对比和评估效果。

## 理解威胁

要构建可信赖的 AI 代理，理解并减轻风险和威胁至关重要。下面仅展示 AI 代理面临的一些不同威胁，以及您如何更好地规划和准备应对它们。

![理解威胁](../../../translated_images/zh-CN/understanding-threats.89edeada8a97fc0f.webp)

### 任务和指令

**描述：** 攻击者试图通过提示或操纵输入改变 AI 代理的指令或目标。

**缓解措施：** 执行验证检查和输入过滤，检测潜在危险提示，防止其被 AI 代理处理。由于此类攻击通常需要多次与代理交互，限制对话轮数也是防止此类攻击的一个方法。

### 访问关键系统

**描述：** 如果 AI 代理有权访问存储敏感数据的系统和服务，攻击者可以破坏代理与这些服务之间的通信。攻击可以是直接的，也可以是通过代理间接获得这些系统信息的尝试。

**缓解措施：** AI 代理应基于“最小权限”原则访问系统，以防范这类攻击。代理与系统间的通信也应当安全，实施身份验证和访问控制是保护信息的另一种方法。

### 资源和服务过载

**描述：** AI 代理可以访问不同工具和服务来完成任务。攻击者可能利用此能力，通过代理向这些服务发送大量请求，导致系统故障或高昂成本。

**缓解措施：** 实施政策限制 AI 代理对某服务的请求次数。限制对话轮数和代理请求数也是防范此类攻击的手段。

### 知识库投毒

**描述：** 此类攻击并不直接针对 AI 代理，而是针对其用以完成任务的知识库和其他服务。攻击可能涉及篡改数据或信息，导致 AI 代理对用户给出有偏见或非预期的回答。

**缓解措施：** 定期验证 AI 代理工作流中使用的数据。确保访问数据的安全性，仅允许可信人员进行更改，以防止此类攻击。

### 连锁错误

**描述：** AI 代理访问各种工具和服务以完成任务。攻击者引发的错误可能导致代理连接的其他系统故障，使攻击范围更广且难以排查。

**缓解措施：** 一种避免方法是让 AI 代理在受限环境中运行，例如在 Docker 容器内执行任务，防止直接系统攻击。创建回退机制及错误重试逻辑，当某些系统返回错误时也可防止更大系统故障。

## 人在回路中

另一构建可信赖 AI 代理系统的有效方法是采用“人在回路中”。这营造了一个流程，让用户在运行过程中向代理提供反馈。用户实质上充当多代理系统中的代理，提供批准或终止正在运行的过程。

![人在回路中](../../../translated_images/zh-CN/human-in-the-loop.5f0068a678f62f4f.webp)

下面是使用 Microsoft Agent Framework 实现该概念的代码片段：

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# 使用人工审核创建提供者
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 创建带有人类审核步骤的代理
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# 用户可以审查并批准响应
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## 结论

构建可信赖的 AI 代理需要精心设计、强有力的安全措施以及持续迭代。通过实施结构化的元提示系统、理解潜在威胁并采取缓解策略，开发者可以创建既安全又有效的 AI 代理。此外，融入“人在回路中”的方法确保 AI 代理与用户需求保持一致，同时最大限度降低风险。随着 AI 不断发展，保持对安全、隐私和伦理问题的前瞻性关注，将是培养 AI 驱动系统信任与可靠性的关键。

## 代码示例

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb)：元提示系统消息框架的逐步演示。
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb)：可信赖代理的预操作审批门、风险分层和审计日志。

### 对构建可信赖 AI 代理有更多疑问？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 与其他学习者交流，参加办公时间，获取您的 AI 代理问题解答。

## 附加资源

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">负责任的人工智能概述</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">生成式 AI 模型及 AI 应用评估</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">安全系统消息</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">风险评估模板</a>

## 上一课

[Agentic RAG](../05-agentic-rag/README.md)

## 下一课

[规划设计模式](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->