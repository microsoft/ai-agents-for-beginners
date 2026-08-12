[![Intro to AI Agents](../../../translated_images/zh-CN/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(点击上方图片观看本课视频)_

# AI 代理及代理使用案例简介

欢迎来到 **AI 代理初学者** 课程！本课程为您提供基础知识和真实工作代码，助您从零开始构建 AI 代理。

来 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord 社区</a> 打个招呼吧——那里聚集了许多学习者和 AI 构建者，他们乐于解答您的问题。

在开始构建之前，让我们先确保真正理解 AI 代理<em>是什么</em>，以及在何时使用它才合理。

---

## 介绍

本课将涵盖：

- 什么是 AI 代理以及存在的不同类型
- AI 代理最适合的任务类型
- 设计代理解决方案时您将使用的核心构建模块

## 学习目标

本课结束后，您应能：

- 说明什么是 AI 代理以及它与普通 AI 解决方案的区别
- 了解何时应使用 AI 代理（何时不应使用）
- 勾勒出真实世界问题的基础代理解决方案设计

---

## 定义 AI 代理及 AI 代理类型

### 什么是 AI 代理？

这里有一个简单的理解方式：

> **AI 代理是让大型语言模型（LLM）真正<em>做事</em>的系统——通过赋予它们工具和知识去作用于世界，而不仅仅是回应提示。**

我们来细说一下：

- <strong>系统</strong> — AI 代理不只是单一事物，而是多个部分协同工作的集合。每个代理核心都有三部分：
  - <strong>环境</strong> — 代理工作的空间。旅行预订代理的环境即为预订平台本身。
  - <strong>传感器</strong> — 代理感知当前环境状态的方式。旅行代理可能会查看酒店房态或航班价格。
  - <strong>执行器</strong> — 代理采取行动的方式。旅行代理可能会预订房间、发送确认信息或取消预订。

![什么是 AI 代理？](../../../translated_images/zh-CN/what-are-ai-agents.1ec8c4d548af601a.webp)

- <strong>大型语言模型</strong> — 代理早在 LLM 出现之前就有了，但正是 LLM 使现代代理变得强大。它们能理解自然语言、推理上下文，并将模糊的用户请求转化为具体行动计划。

- <strong>执行动作</strong> — 没有代理系统，LLM 只是文字生成器。但在代理系统中，LLM 可以<em>执行</em>步骤——搜索数据库、调用 API、发送消息。

- <strong>工具访问</strong> — 代理可用的工具取决于（1）它运行的环境，（2）开发者赋予它的能力。旅行代理可能能搜索航班但不能编辑客户记录——全部取决于您所连接的功能。

- <strong>记忆与知识</strong> — 代理可包含短期记忆（当前对话）和长期记忆（客户数据库、过去的交互）。旅行代理可能会“记住”您喜欢靠窗座位。

---

### 不同类型的 AI 代理

并非所有代理都是同一类型。以下是主要类型的划分，以旅行预订代理为例：

| <strong>代理类型</strong> | <strong>功能描述</strong> | <strong>旅行代理示例</strong> |
|---|---|---|
| <strong>简单反射代理</strong> | 遵循硬编码规则——无记忆，无规划。 | 看到投诉邮件 → 转发给客服，仅此而已。 |
| <strong>基于模型的反射代理</strong> | 保持内部环境模型并随变化更新。 | 跟踪历史航班价格，标记突然涨价的航线。 |
| <strong>目标驱动代理</strong> | 有明确目标，逐步规划达成路径。 | 预订完整行程（航班、汽车、酒店），从当前位置到目的地。 |
| <strong>效用驱动代理</strong> | 不只是找到<em>一个</em>方案，而是权衡得失找到<em>最优</em>方案。 | 平衡成本与便利，找出最符合您偏好的行程。 |
| <strong>学习型代理</strong> | 通过反馈不断改进。 | 根据行程后的调查结果调整未来推荐。 |
| <strong>分层代理</strong> | 高级代理拆分任务并委派给低级代理。 | “取消行程”请求拆分为取消航班、取消酒店、取消租车，各子代理处理。 |
| **多代理系统（MAS）** | 多个独立代理协作（或竞争）。 | 协作：分别处理酒店、航班和娱乐的代理。竞争：多个代理竞价填满酒店房间，争取最佳价格。 |

---

## 何时使用 AI 代理

只是因为<em>可以</em>用 AI 代理，不代表总是<em>应该</em>用。以下情况代理特别适合：

![何时使用 AI 代理？](../../../translated_images/zh-CN/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>开放式问题</strong> — 需要动态探索解决路径，无法预编程具体步骤。
- <strong>多步骤流程</strong> — 任务需多轮使用各种工具，而非单次查找或生成。
- <strong>持续改进</strong> — 系统需基于用户反馈或环境信号不断变聪明。

我们将在本课程后续的 **构建可信赖 AI 代理** 课程深入讲解何时（及何时不）使用 AI 代理。

---

## 代理解决方案基础

### 代理开发

构建代理的第一步是定义<em>它能做什么</em>——包括它的工具、动作和行为。

本课程采用 **Microsoft Foundry Agent Service** 作为主要平台。它支持：

- 来自 OpenAI、Mistral、Meta（Llama）等提供商的模型
- 来自 Tripadvisor 等提供商的授权数据
- 标准化的 OpenAPI 3.0 工具定义

### 代理模式

您通过提示与 LLM 交流。对代理来说，不能手工打造每个提示——代理需要跨多个步骤采取行动。此时，<strong>代理模式</strong> 派上用场。它们是可复用的提示及 LLM 编排策略，更具可扩展性和可靠性。

本课程围绕最常见、最实用的代理模式构建。

### 代理框架

代理框架为开发者提供现成的模板、工具和基础设施，方便构建代理。它们能简化：

- 工具和功能的连接
- 观察代理行为（和定位问题时调试）
- 多代理协作

本课程重点介绍用于构建生产级代理的 **Microsoft Agent Framework (MAF)**。

---

## 代码示例

准备好亲眼看看了吗？这里是本课的代码示例：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有问题？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，与其他学习者交流，参加答疑时间，由社区为您的 AI 代理问题提供解答。


---

## 快速测试这个代理（可选）

一旦您学会如何在 [第16课](../16-deploying-scalable-agents/README.md) 部署代理，就可以为本课的 `TravelAgent` 添加快速的部署后健康检查，使用预制目录 [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json)。查看 [`tests/README.md`](../tests/README.md) 了解运行方式。

---

## 上一课

[课程设置](../00-course-setup/README.md)

## 下一课

[探索代理框架](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->