# 使用智能代理协议（MCP、A2A 和 NLWeb）

[![智能代理协议](../../../translated_images/zh-CN/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(点击上方图片查看本课视频)_

随着 AI 代理的使用增加，对确保标准化、安全性并支持开放创新的协议需求也在增长。在本课中，我们将介绍三种旨在满足此需求的协议 —— Model Context Protocol（MCP）、Agent to Agent（A2A）和 Natural Language Web（NLWeb）。

## 介绍

在本课中，我们将覆盖：

• **MCP** 如何允许 AI 代理访问外部工具和数据以完成用户任务。

• **A2A** 如何使不同 AI 代理之间实现通信与协作。

• **NLWeb** 如何将自然语言界面带到任意网站，使 AI 代理能够发现并与网站内容交互。

## 学习目标

• **识别** MCP、A2A 和 NLWeb 在 AI 代理背景下的核心目的与优势。

• **解释** 每个协议如何促进 LLM、工具和其他代理之间的通信与交互。

• **识别** 每个协议在构建复杂代理系统时所扮演的不同角色。

## Model Context Protocol

**Model Context Protocol（MCP）** 是一个开放标准，提供了一种标准化方式，使应用程序可以向 LLM 提供上下文和工具。这使得 AI 代理可以以一致的方式连接到不同的数据源和工具，相当于一个“通用适配器”。

让我们看看 MCP 的组件、与直接使用 API 相比的好处，以及 AI 代理如何使用 MCP 服务器的示例。

### MCP 核心组件

MCP 采用**客户端-服务器架构**，核心组件包括：

• **Hosts** 是启动与 MCP Server 连接的 LLM 应用（例如像 VSCode 这样的代码编辑器）。

• **Clients** 是宿主应用内的组件，维护与服务器的一对一连接。

• **Servers** 是暴露特定能力的轻量级程序。

协议中包含三种核心原语，它们是 MCP 服务器的能力：

• **Tools**：这些是 AI 代理可以调用以执行操作的离散动作或函数。例如，天气服务可能暴露一个“get weather”工具，或电子商务服务器可能暴露一个“purchase product”工具。MCP 服务器在其能力列表中公布每个工具的名称、描述和输入/输出模式。

• **Resources**：这些是 MCP 服务器可以提供的只读数据项或文档，客户端可以按需检索。例如文件内容、数据库记录或日志文件。Resources 可以是文本（如代码或 JSON）或二进制（如图像或 PDF）。

• **Prompts**：这些是预定义的模板，提供建议的提示，允许更复杂的工作流。

### MCP 的好处

MCP 为 AI 代理提供显著优势：

• **动态工具发现**：代理可以动态接收服务器提供的可用工具列表以及它们的功能描述。这与传统 API 形成对比，传统 API 通常需要为集成进行静态编码，任何 API 变更都需要代码更新。MCP 提供“一次集成”的方法，带来更强的适应性。

• **跨 LLM 的互操作性**：MCP 能在不同的 LLM 之间工作，提供更换核心模型以评估更好性能的灵活性。

• **标准化的安全性**：MCP 包含标准的认证方法，在添加对更多 MCP 服务器的访问时提升可扩展性。这比为各种传统 API 管理不同密钥和认证类型更简单。

### MCP 示例

![MCP 图示](../../../translated_images/zh-CN/mcp-diagram.e4ca1cbd551444a1.webp)

想象用户想用由 MCP 提供支持的 AI 助手预订机票。

1. **连接**：AI 助手（MCP 客户端）与航空公司提供的 MCP 服务器建立连接。

2. **工具发现**：客户端询问航空公司的 MCP 服务器：“你们有什么可用工具？”服务器回复诸如“search flights”和“book flights”之类的工具。

3. **工具调用**：然后你对 AI 助手说：“请帮我搜索一趟从 Portland 到 Honolulu 的航班。”AI 助手使用其 LLM，识别需要调用“search flights”工具，并将相关参数（出发地、目的地）传递给 MCP 服务器。

4. **执行与响应**：作为包装器的 MCP 服务器调用航空公司的内部预订 API。然后它接收航班信息（例如 JSON 数据）并将其发送回 AI 助手。

5. **后续交互**：AI 助手展示航班选项。一旦你选择了航班，助理可能会在同一 MCP 服务器上调用“book flight”工具，完成预订。

## Agent-to-Agent Protocol (A2A)

当 MCP 专注于将 LLM 连接到工具时，**Agent-to-Agent（A2A）协议** 更进一步，能够实现不同 AI 代理之间的通信与协作。A2A 将来自不同组织、环境和技术栈的 AI 代理连接起来，以完成共同任务。

我们将检查 A2A 的组件和好处，并通过我们的旅行应用示例说明其应用方式。

### A2A 核心组件

A2A 专注于使代理之间能够通信并协同完成用户的子任务。协议的每个组件都有助于此目标：

#### Agent Card

类似于 MCP 服务器共享工具列表，Agent Card 包含：
- Agent 的名称。
- 它完成的一般任务的**描述**。
- 帮助其他代理（或甚至人类用户）理解何时以及为什么调用该代理的**具体技能列表**及其描述。
- 代理的**当前 Endpoint URL**。
- 代理的**版本**和**能力**，例如流式响应和推送通知。

#### Agent Executor

Agent Executor 负责**将用户聊天的上下文传递给远程代理**，远程代理需要这些上下文以理解需要完成的任务。在 A2A 服务器中，代理使用其自己的大语言模型（LLM）解析传入请求并使用其内部工具执行任务。

#### Artifact

一旦远程代理完成请求的任务，其工作成果会作为 artifact 创建。artifact **包含代理工作结果**、**已完成内容的描述**以及通过协议发送的**文本上下文**。artifact 发送后，与远程代理的连接会关闭，直到再次需要为止。

#### Event Queue

此组件用于**处理更新和传递消息**。在生产环境中，事件队列在代理系统中特别重要，以防在任务完成之前代理间的连接被关闭，尤其是当任务完成可能需要较长时间时。

### A2A 的好处

• **增强的协作**：它使来自不同供应商和平台的代理能够交互、共享上下文并协同工作，促进传统上互不连通系统之间的无缝自动化。

• **模型选择灵活性**：每个 A2A 代理可以决定使用哪个 LLM 来处理其请求，允许为每个代理优化或微调模型，这不同于某些 MCP 场景中的单一 LLM 连接。

• **内置认证**：认证直接集成到 A2A 协议中，为代理交互提供稳健的安全框架。

### A2A 示例

![A2A 图示](../../../translated_images/zh-CN/A2A-Diagram.8666928d648acc26.webp)

让我们扩展之前的旅行预订场景，但这次使用 A2A。

1. **用户向多代理请求**：用户与一个“Travel Agent” A2A 客户端/代理交互，例如说：“请帮我为下周预订一次完整的檀香山旅行，包括航班、酒店和租车”。

2. **Travel Agent 的编排**：Travel Agent 收到这个复杂请求。它使用其 LLM 推理任务并确定需要与其他专门代理交互。

3. **代理间通信**：Travel Agent 使用 A2A 协议连接到下游代理，例如由不同公司创建的“Airline Agent”、“Hotel Agent”和“Car Rental Agent”。

4. **委派任务执行**：Travel Agent 向这些专门代理发送特定任务（例如，“查找飞往檀香山的航班”，“预订酒店”，“租一辆车”）。每个专门代理运行自己的 LLM 并利用其自己的工具（这些工具本身也可能是 MCP 服务器），执行其特定的预订部分。

5. **汇总响应**：一旦所有下游代理完成其任务，Travel Agent 汇总结果（航班详情、酒店确认、租车预订），并以聊天式的综合响应返回给用户。

## Natural Language Web (NLWeb)

长期以来，网站一直是用户访问互联网信息和数据的主要方式。

让我们看看 NLWeb 的不同组件、NLWeb 的好处，以及通过我们的旅行应用示例了解 NLWeb 的工作方式。

### NLWeb 的组件

- **NLWeb Application (Core Service Code)**：处理自然语言问题的系统。它连接平台的不同部分以生成响应。可以将其视为为网站提供自然语言功能的**引擎**。

- **NLWeb Protocol**：这是与网站进行自然语言交互的**基本规则集**。它以 JSON 格式（通常使用 Schema.org）返回响应。其目的是为“AI Web”创建一个简单的基础，就像 HTML 使在线共享文档成为可能一样。

- **MCP Server (Model Context Protocol Endpoint)**：每个 NLWeb 部署也可作为一个**MCP 服务器**。这意味着它可以**与其他 AI 系统共享工具（例如“ask”方法）和数据**。在实践中，这使得网站的内容和能力对 AI 代理可用，允许该网站成为更广泛“代理生态系统”的一部分。

- **Embedding Models**：这些模型用于将网站内容**转换为称为向量（embeddings）的数值表示**。这些向量以计算机可比较和搜索的方式捕捉含义。它们存储在专门的数据库中，用户可以选择他们想要使用的 embedding 模型。

- **Vector Database (Retrieval Mechanism)**：该数据库**存储网站内容的 embeddings**。当有人提出问题时，NLWeb 会检查向量数据库以快速找到最相关的信息。它会按相似性排名给出一份可能答案的快速列表。NLWeb 可与不同的向量存储系统配合使用，例如 Qdrant、Snowflake、Milvus、Azure AI Search 和 Elasticsearch。

### NLWeb 示例

![NLWeb 图示](../../../translated_images/zh-CN/nlweb-diagram.c1e2390b310e5fe4.webp)

再考虑我们的旅行预订网站，但这次它由 NLWeb 提供支持。

1. **数据摄取**：旅行网站现有的产品目录（例如航班列表、酒店描述、旅游套餐）使用 Schema.org 格式化或通过 RSS feed 加载。NLWeb 的工具摄取这些结构化数据，创建 embeddings，并将其存储在本地或远程的向量数据库中。

2. **自然语言查询（人类）**：用户访问网站，不是通过导航菜单，而是在聊天界面输入：“帮我找一个下周在檀香山有泳池、适合家庭的酒店”。

3. **NLWeb 处理**：NLWeb 应用接收到该查询。它将查询发送给 LLM 进行理解，同时在向量数据库中搜索相关的酒店列表。

4. **准确结果**：LLM 有助于解释数据库的搜索结果，根据“适合家庭”“泳池”和“檀香山”等条件识别最佳匹配，然后格式化为自然语言响应。关键是，响应引用的是网站目录中的实际酒店，避免生成虚构信息。

5. **AI 代理交互**：因为 NLWeb 也作为 MCP 服务器，外部的 AI 旅行代理也可以连接到该网站的 NLWeb 实例。AI 代理然后可以使用 `ask("该酒店是否推荐檀香山地区的任何素食友好餐厅？")` MCP 方法直接查询网站。NLWeb 实例会处理该查询，利用其已加载的餐厅信息数据库（如果已加载），并返回结构化的 JSON 响应。

### 对 MCP/A2A/NLWeb 有更多问题吗？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 与其他学习者见面，参加答疑时间并获得关于 AI 代理的问题解答。

## 资源

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免责声明：
本文档已使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原文应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而导致的任何误解或错误解释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->