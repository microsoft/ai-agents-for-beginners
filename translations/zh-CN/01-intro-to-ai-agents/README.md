[![Intro to AI Agents](../../../translated_images/zh-CN/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(点击上方图片观看本节视频)_

# AI 代理介绍及代理用例

欢迎来到 **AI 代理入门** 课程！本课程为你提供基础知识和实用代码，助你从零开始构建 AI 代理。

欢迎加入 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord 社区</a>，这里汇聚了众多学习者和 AI 开发者，乐于解答你的问题。

在开始构建之前，让我们先理清什么是 AI 代理，以及何时使用它们才合适。

---

## 介绍

本节内容包括：

- 什么是 AI 代理，以及不同类型的 AI 代理
- AI 代理最适合处理的任务类型
- 设计代理解决方案时的核心构建模块

## 学习目标

完成本节后，你应该能够：

- 解释 AI 代理的概念及其与普通 AI 解决方案的区别
- 了解何时应选择使用 AI 代理（以及何时不该使用）
- 绘制针对实际问题的基本代理解决方案设计草图

---

## AI 代理及代理类型定义

### 什么是 AI 代理？

简单来说：

> **AI 代理是让大型语言模型（LLM）真正“做事”的系统——通过赋予它们工具和知识，来作用于现实世界，而不仅仅是响应提示。**

具体拆解：

- <strong>系统</strong> — AI 代理不是单一事物，而是多个部分协同工作的集合。每个代理核心包含三部分：
  - <strong>环境</strong> — 代理工作的空间。对于旅游预订代理，它就是预订平台本身。
  - <strong>传感器</strong> — 代理感知当前环境状态的方式。我们的旅游代理会检查酒店可用性或机票价格。
  - <strong>执行器</strong> — 代理采取行动的方式。旅游代理可能预订房间、发送确认或取消预订。

![What Are AI Agents?](../../../translated_images/zh-CN/what-are-ai-agents.1ec8c4d548af601a.webp)

- <strong>大型语言模型</strong> — 代理在 LLM 出现前就存在，但 LLM 让现代代理更加强大。它们能理解自然语言、推理上下文，将模糊的用户请求转化为具体行动计划。

- <strong>执行动作</strong> — 没有代理系统，LLM 只有生成文本的能力。置于代理系统中，LLM 能真正执行步骤——搜索数据库、调用 API、发送消息。

- <strong>接入工具</strong> — 代理可用的工具取决于（1）其运行环境，（2）开发提供了哪些工具。旅游代理可能能搜索航班但不能修改客户记录——这取决于你的配置。

- **记忆 + 知识** — 代理可拥有短期记忆（当前对话）和长期记忆（客户数据库、过往交互）。旅游代理可能“记得”你偏好靠窗座位。

---

### 不同类型的 AI 代理

代理类型各异，以下用旅游预订代理作为例子：

| <strong>代理类型</strong> | <strong>功能描述</strong> | <strong>旅游代理示例</strong> |
|---|---|---|
| <strong>简单反射代理</strong> | 遵循硬编码规则——无记忆，无规划。 | 看到投诉邮件→转发客服。仅此而已。 |
| <strong>基于模型的反射代理</strong> | 内部维护世界模型，并随变化更新。 | 跟踪历史机票价格，标记突然昂贵的航线。 |
| <strong>基于目标的代理</strong> | 有具体目标，逐步策划达成路径。 | 预订完整行程（机票、租车、酒店），从你所在地到目的地。 |
| <strong>基于效用的代理</strong> | 不仅找到「一个」方案，而是权衡得到「最佳」方案。 | 平衡费用与便利性，找到最符合偏好的行程。 |
| <strong>学习型代理</strong> | 通过反馈不断学习并改进。 | 根据旅行后调查结果调整未来推荐。 |
| <strong>层级代理</strong> | 高层代理分解任务，委派底层代理完成。 | “取消行程”请求拆分为取消机票、取消酒店、取消租车，由子代理处理。 |
| **多代理系统（MAS）** | 多个独立代理协作（或竞争）。 | 协作：不同代理负责酒店、航班和娱乐。竞争：多个代理争夺最优酒店房价。 |

---

## 何时使用 AI 代理

能用 AI 代理不代表总该用。代理真正发光的场景包括：

![When to use AI Agents?](../../../translated_images/zh-CN/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>开放式问题</strong> — 解决步骤无法预编程，需要 LLM 动态寻找路径。
- <strong>多步骤流程</strong> — 需跨多轮使用工具，而非单次查询或生成。
- <strong>持续改进</strong> — 希望系统基于用户反馈或环境信号不断变聪明。

本课程后续的 **构建可信赖的 AI 代理** 章节会更深入探讨何时适合（或不适合）使用 AI 代理。

---

## 代理解决方案基础

### 代理开发

构建代理的首要任务是定义代理能做什么——其工具、动作和行为。

课程中我们使用 **Azure AI Agent Service** 作为主要平台，支持：

- 来自 OpenAI、Mistral 和 Meta（Llama）等提供商的模型
- 来自 Tripadvisor 等提供商的授权数据
- 标准化的 OpenAPI 3.0 工具定义

### 代理模式

与 LLM 通信依赖提示。代理需要跨多步骤行动，不能手工逐条设计所有提示。这时就用上了<strong>代理模式</strong>，它是可复用的提示与调度策略，助你更高效、可靠地组织 LLM 工作。

本课程围绕最常用和最实用的代理模式展开。

### 代理框架

代理框架为开发者提供现成模板、工具和基础设施，简化：

- 工具与功能的整合
- 观察代理运行状态（及调试问题）
- 多代理协作开发

本课程侧重于构建生产级代理的 **微软代理框架（MAF）**。

---

## 代码示例

准备好实践了吗？本节的代码示例：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有问题？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者讨论，参加办公时间，社区将助你解答 AI 代理相关疑问。

---

## 上一节

[课程设置](../00-course-setup/README.md)

## 下一节

[探索代理框架](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->