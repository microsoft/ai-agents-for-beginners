# 使用自治协议（MCP，A2A 和 NLWeb）

[![Agentic Protocols](../../../translated_images/zh-CN/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(点击上方图片观看本课视频)_

随着 AI 代理的普及，对确保标准化、安全性并支持开放创新的协议需求也在增长。本课将介绍满足这一需求的三种协议——模型上下文协议（MCP）、代理间协议（A2A）和自然语言网页（NLWeb）。

## 介绍

本课内容包括：

• **MCP** 如何让 AI 代理访问外部工具和数据以完成用户任务。

• **A2A** 如何支持不同 AI 代理之间的通信与协作。

• **NLWeb** 如何为任意网站带来自然语言界面，使 AI 代理能够发现并与内容交互。

## 学习目标

• <strong>识别</strong> MCP、A2A 和 NLWeb 在 AI 代理背景下的核心目的和优势。

• <strong>解释</strong> 每种协议如何促进 LLM、工具及其他代理之间的通信与交互。

• <strong>认识</strong> 每种协议在构建复杂自治系统中扮演的不同角色。

## 模型上下文协议

**模型上下文协议（Model Context Protocol，MCP）** 是一个开放标准，提供应用向 LLM 传递上下文和工具的标准化方法。这使得 AI 代理可以通过“通用适配器”以一致方式连接到不同的数据源和工具。

让我们看看 MCP 的组成部分、相比直接调用 API 的优势，以及 AI 代理如何使用 MCP 服务器的示例。

### MCP 核心组件

MCP 采用<strong>客户端-服务器架构</strong>，核心组件包括：

• **Hosts（宿主）** 是启动与 MCP 服务器连接的 LLM 应用（例如代码编辑器 VSCode）。

• **Clients（客户端）** 是宿主应用中与服务器保持一对一连接的组件。

• **Servers（服务器）** 是暴露特定能力的轻量级程序。

协议中包含的三个核心基本元素是 MCP 服务器的能力：

• **Tools（工具）**：AI 代理调用执行特定操作的离散功能。例如，气象服务可能暴露“获取天气”工具，电商服务器可能暴露“购买产品”工具。MCP 服务器会在能力列表中公布每个工具的名称、描述以及输入/输出架构。

• **Resources（资源）**：MCP 服务器可提供的只读数据项或文档，客户端按需检索。示例包括文件内容、数据库记录或日志文件。资源可以是文本（如代码或 JSON）或二进制文件（如图像或 PDF）。

• **Prompts（提示）**：预定义的模板，提供建议提示，支持更复杂的工作流程。

### MCP 的优势

MCP 为 AI 代理带来显著优势：

• <strong>动态工具发现</strong>：代理可以动态获取服务器上可用工具列表及其功能描述。与传统 API 不同，后者通常需要静态编码集成，任何 API 变更都需更新代码，而 MCP 采用“一次集成”方式，提高了适应能力。

• **跨 LLM 的互操作性**：MCP 支持不同 LLM，灵活切换核心模型以优化性能。

• <strong>标准化安全</strong>：MCP 包含标准认证方式，便于扩展访问多个 MCP 服务器，简化了传统 API 中需管理多种密钥和认证方式的复杂性。

### MCP 示例

![MCP Diagram](../../../translated_images/zh-CN/mcp-diagram.e4ca1cbd551444a1.webp)

假设用户想通过基于 MCP 的 AI 助手预订机票。

1. <strong>连接</strong>：AI 助手（MCP 客户端）连接到航空公司提供的 MCP 服务器。

2. <strong>工具发现</strong>：客户端询问航空公司的 MCP 服务器“你有哪些可用工具？”服务器返回“搜索航班”和“预订航班”等工具。

3. <strong>调用工具</strong>：用户对 AI 助手说：“帮我搜索从波特兰到檀香山的航班。”助手使用其 LLM 确认需调用“搜索航班”工具，并将相关参数（出发地、目的地）传给 MCP 服务器。

4. <strong>执行与响应</strong>：MCP 服务器作为封装调用航空公司内部预订 API，接收航班信息（如 JSON 数据）并返回给 AI 助手。

5. <strong>后续交互</strong>：AI 助手展示航班选项。用户选定后，助手可能调用同一 MCP 服务器上的“预订航班”工具完成预订。

## 代理间协议（A2A）

MCP 专注于连接 LLM 与工具，而<strong>代理间协议（Agent-to-Agent，A2A）</strong>更进一步，支持不同 AI 代理之间的通信与协作。A2A 连接了来自不同组织、环境和技术栈的 AI 代理，共同完成共享任务。

我们将探讨 A2A 的组成与优点，同时展示其在旅游应用中的应用示例。

### A2A 核心组件

A2A 旨在实现代理之间的通信与协作完成用户子任务。协议的每个组件都贡献于此：

#### 代理卡片

类似 MCP 服务器共享工具列表，代理卡片包含：
- 代理名称。
- <strong>完成的一般任务说明</strong>。
- <strong>具体技能列表</strong>及描述，帮助其他代理（甚至人类用户）理解何时何因调用该代理。
- 代理当前的 **端点 URL**。
- 代理的 <strong>版本</strong> 和 <strong>能力</strong>，如流响应和推送通知。

#### 代理执行器

代理执行器负责<strong>将用户对话上下文传递给远程代理</strong>，远程代理需要此信息以理解需完成的任务。在 A2A 服务器中，代理使用自己的大型语言模型（LLM）解析请求并用自身内部工具执行任务。

#### 工件

远程代理完成任务后，其成果以工件形式创建。工件<strong>包含代理工作结果</strong>、<strong>完成内容描述</strong>及协议传递的<strong>文本上下文</strong>。工件发送后，远程代理连接关闭，直到再次需要。

#### 事件队列

该组件用于<strong>处理更新和传递消息</strong>。在生产环境中，事件队列对避免任务完成前代理连接关闭尤其重要，因任务完成时间可能较长。

### A2A 优势

• <strong>增强协作</strong>：支持不同供应商和平台的代理互相交互、共享上下文并协作，促进跨传统断层系统的无缝自动化。

• <strong>模型选择灵活</strong>：每个 A2A 代理可自主选择用于服务请求的 LLM，便于针对每个代理优化或微调模型，区别于某些 MCP 场景中单一 LLM 连接。

• <strong>内建认证</strong>：认证机制直接集成于 A2A 协议，为代理交互提供强健安全框架。

### A2A 示例

![A2A Diagram](../../../translated_images/zh-CN/A2A-Diagram.8666928d648acc26.webp)

让我们扩展旅游预订场景，使用 A2A。

1. <strong>用户请求多代理</strong>：用户通过“旅行代理”A2A 客户端/代理交互，说：“帮我预订下周去檀香山的全程行程，包括航班、酒店和租车。”

2. <strong>旅行代理协调</strong>：旅行代理接收复杂请求，使用其 LLM 进行推理，确定需与其他专门代理交互。

3. <strong>代理间通信</strong>：旅行代理通过 A2A 协议连接下游专门代理，如不同公司的“航空代理”、“酒店代理”和“租车代理”。

4. <strong>任务分配执行</strong>：旅行代理向专门代理发送具体任务（如“寻找檀香山航班”、“预订酒店”、“租车”），各自代理运行自身 LLM，使用各自工具（可能是 MCP 服务器）完成对应预订部分。

5. <strong>汇总响应</strong>：所有下游代理完成任务后，旅行代理整合结果（航班详情、酒店确认、租车订单）并以聊天形式回复用户。

## 自然语言网页（NLWeb）

网站长期以来是用户访问互联网上信息和数据的主要方式。

我们来了解 NLWeb 的不同组成部分、其优势，以及通过旅游应用示例了解 NLWeb 工作原理。

### NLWeb 组成部分

- **NLWeb 应用程序（核心服务代码）**：处理自然语言问题的系统，连接平台各部分生成响应。可视作赋能网站自然语言功能的<strong>引擎</strong>。

- **NLWeb 协议**：网站自然语言交互的<strong>基本规则集</strong>，以 JSON 格式（经常使用 Schema.org）返回响应。旨在为“AI 网”创建简单基础，类似 HTML 使得在线共享文档成为可能。

- **MCP 服务器（模型上下文协议端点）**：每个 NLWeb 设置也作为<strong>MCP 服务器</strong>，可<strong>与其他 AI 系统共享工具（如“ask”方法）和数据</strong>。这使得网站内容和功能可供 AI 代理使用，推动网站成为更大“代理生态系统”的一部分。

- <strong>嵌入模型</strong>：用于将网站内容转换成称为向量（嵌入）的数值表示的模型。这些向量以计算机可比较和搜索的方式捕捉含义。它们存储在专用数据库中，用户可选择使用的嵌入模型。

- **向量数据库（检索机制）**：存储网站内容嵌入的数据库。当有人提问时，NLWeb 查询向量数据库迅速找到最相关信息，返回按相似度排序的可能答案列表。NLWeb 支持多种向量存储系统，如 Qdrant、Snowflake、Milvus、Azure AI Search 和 Elasticsearch。

### NLWeb 示例

![NLWeb](../../../translated_images/zh-CN/nlweb-diagram.c1e2390b310e5fe4.webp)

再看我们的旅游预订网站，这次由 NLWeb 驱动。

1. <strong>数据摄取</strong>：旅游网站现有的产品目录（如航班列表、酒店描述、旅游套餐）用 Schema.org 格式化或通过 RSS 订阅。NLWeb 工具摄取该结构化数据，创建嵌入并存储在本地或远程向量数据库。

2. **自然语言查询（人类）**：用户访问网站，不通过菜单导航，而是在聊天界面输入：“帮我找下周檀香山带泳池的适合家庭的酒店。”

3. **NLWeb 处理**：NLWeb 应用接收该查询，将查询发送给 LLM 理解，同时在向量数据库中搜索相关酒店列表。

4. <strong>准确结果</strong>：LLM 协助解释数据库的搜索结果，根据“适合家庭”、“泳池”、“檀香山”等标准识别最佳匹配，并格式化自然语言回复。关键是此回复参照网站实际酒店目录，避免生成虚假信息。

5. **AI 代理交互**：因 NLWeb 作为 MCP 服务器，外部 AI 旅行代理可连接此网站的 NLWeb 实例。该代理可使用 `ask` MCP 方法直接查询网站：`ask("酒店推荐的檀香山地区有任何素食餐厅吗？")`。NLWeb 实例将处理并利用餐厅信息数据库（如果已加载），返回结构化 JSON 响应。

### 对 MCP/A2A/NLWeb 还有更多疑问吗？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，与其他学习者交流，参加答疑时段，获取 AI 代理相关问题的解答。

## 资源

- [MCP 入门](https://aka.ms/mcp-for-beginners)  
- [MCP 文档](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb 仓库](https://github.com/nlweb-ai/NLWeb)
- [Microsoft 代理框架](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## 上一课

[生产中的 AI 代理](../10-ai-agents-production/README.md)

## 下一课

[AI 代理的上下文工程](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->