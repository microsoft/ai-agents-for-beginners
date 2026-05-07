[![Intro to AI Agents](../../../translated_images/zh-CN/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(点击上方图片观看本课视频)_

# AI 代理及代理应用简介

欢迎参加<strong>AI 代理入门</strong>课程！本课程为你提供基础知识——以及可实际运行的代码——帮助你从零开始构建 AI 代理。

来<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord 社区</a>打个招呼吧——这里汇聚了许多学习者和 AI 构建者，乐于回答你的问题。

在开始构建之前，让我们确保真正了解什么是 AI 代理，以及何时适合使用它们。

---

## 介绍

本课内容包括：

- AI 代理是什么，以及不同类型代理的分类
- 哪些任务最适合由 AI 代理执行
- 设计代理解决方案时所用的核心构建模块

## 学习目标

完成本课后，你应该能够：

- 解释 AI 代理是什么，以及它与常规 AI 解决方案有何不同
- 理解何时应使用 AI 代理（何时不应使用）
- 为实际问题绘制一个基础的代理解决方案设计框架

---

## 定义 AI 代理及代理类型

### 什么是 AI 代理？

可以这样简单理解：

> **AI 代理是让大型语言模型(LLM)真正<em>做事</em>的系统——通过赋予它们工具和知识，让它们操控世界，而不仅仅是响应提示。**

我们来详细拆解一下：

- <strong>系统</strong> — AI 代理不是单个实体，它是由多部分协作组成的系统。每个代理的核心包含三部分：
  - <strong>环境</strong> — 代理所工作的空间。以旅游预订代理为例，就是预订平台本身。
  - <strong>传感器</strong> — 代理感知环境当前状态的方式。我们的旅游代理可能会检查酒店空房情况或机票价格。
  - <strong>执行器</strong> — 代理执行操作的方式。旅游代理或许会预订房间、发送确认信息或取消订单。

![What Are AI Agents?](../../../translated_images/zh-CN/what-are-ai-agents.1ec8c4d548af601a.webp)

- <strong>大型语言模型</strong> — 代理在 LLM 出现之前就存在，但 LLM 使现代代理更加强大。它们能理解自然语言、推理上下文，并将模糊的用户请求转化为具体的行动方案。

- <strong>执行操作</strong> — 如果没有代理系统，LLM 仅生成文本。代理系统内，LLM 可以<em>执行</em>步骤——比如搜索数据库、调用 API、发送消息。

- <strong>工具访问</strong> — 代理能用哪些工具，取决于(1)其运行的环境和(2)开发者赋予它的能力。旅游代理可能能搜索航班但不能修改客户记录——这由你连接的组件决定。

- <strong>记忆与知识</strong> — 代理可以拥有短期记忆（当前对话）和长期记忆（客户数据库、过去的交互）。旅游代理或许“记得”你偏好靠窗座位。

---

### 不同类型的 AI 代理

代理构建方式各异。以下以旅游预订代理为例，列出主要代理类型：

| <strong>代理类型</strong> | <strong>功能</strong> | <strong>旅游代理示例</strong> |
|---|---|---|
| <strong>简单反射代理</strong> | 遵循硬编码规则——无记忆，无计划。 | 看到投诉邮件 → 转发给客服。仅此而已。 |
| <strong>基于模型的反射代理</strong> | 拥有内部世界模型，并随着环境变化更新它。 | 跟踪历史机票价格，标记突然上涨的航线。 |
| <strong>基于目标的代理</strong> | 心怀目标，逐步设计如何实现它。 | 规划完整行程（航班、汽车、酒店），从当前位置到目的地。 |
| <strong>基于效用的代理</strong> | 不仅找<em>一个</em>解决方案，还通过权衡利弊找到<em>最佳</em>方案。 | 权衡成本与便利，找到符合偏好的最佳行程。 |
| <strong>学习型代理</strong> | 通过反馈不断学习进步。 | 根据旅行后的调查结果调整未来预订推荐。 |
| <strong>分层代理</strong> | 高层代理将任务拆分成子任务，并分派给下级代理。 | “取消行程”请求拆分为：取消航班、取消酒店、取消租车——由子代理分别处理。 |
| **多代理系统（MAS）** | 多个独立代理协作（或竞争）。 | 协作：独立代理分别处理酒店、航班和娱乐。竞争：多个代理竞争以最佳价格填满酒店房间。 |

---

## 何时使用 AI 代理

能用 AI 代理不代表任何时候都应该用。以下情况代理尤其适合：

![When to use AI Agents?](../../../translated_images/zh-CN/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>开放式问题</strong> — 解决步骤无法预先编程，需要 LLM 动态确定路径。
- <strong>多步骤流程</strong> — 任务需在多个回合使用工具，而非单次查找或生成。
- <strong>持续改进</strong> — 希望系统能根据用户反馈或环境信号不断变得更智能。

稍后课程中的<strong>构建可信 AI 代理</strong>章节将深入探讨何时（以及何时<em>不</em>）使用 AI 代理。

---

## 代理解决方案基础

### 代理开发

构建代理的第一步是定义<em>它能做什么</em>——包括工具、动作和行为。

本课程使用<strong>Azure AI Agent Service</strong>作为主要平台，支持：

- OpenAI、Mistral 和 Llama 等开源模型
- Tripadvisor 等供应商的授权数据
- 标准化 OpenAPI 3.0 工具定义

### 代理模式

你通过提示与 LLM 交互。使用代理时，不能总依靠手工定制每个提示——代理需要跨多步骤采取行动。这时<strong>代理模式（Agentic Patterns）</strong>就派上用场了。它们是可复用的策略，用于更可扩展、更可靠地提示和协调 LLM。

本课程围绕最常用和最实用的代理模式展开。

### 代理框架

代理框架为开发者提供现成的模板、工具和基础设施，使构建代理更便捷。它们帮助你：

- 连接工具和功能
- 观察代理行为（出现问题时调试）
- 多代理协作

本课程重点讲解用于构建生产级代理的<strong>Microsoft Agent Framework (MAF)</strong>。

---

## 代码示例

准备好现场演示了吗？以下是本课的代码示例：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有问题吗？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者交流，参加答疑时间，并由社区解答你的 AI 代理问题。

---

## 上一课

[课程设置](../00-course-setup/README.md)

## 下一课

[探究代理框架](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于关键信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->