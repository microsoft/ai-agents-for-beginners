# 更新日志

所有对 **AI 入门代理** 课程的重要更新均记录在此文件中。

## [发布] — 2026-07-14

本次发布将课程从两个新弃用的模型中移除，将剩余的课程笔记本迁移至稳定的 Microsoft Agent Framework API，并将 Python 笔记本针对实时 Microsoft Foundry 部署进行了验证。

### 变更

- **移除了弃用的模型（`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`）。** `gpt-4.1` 和 `gpt-4.1-mini` 均已弃用（正式退役日期为 **2026 年 10 月 14 日**）。将课程中的所有引用（文档、`.env.example`，Python/.NET 笔记本和示例）替换为非弃用的 `gpt-5-mini`。第 16 课的模型路由示例依然使用 `gpt-5-nano`（小型）和 `gpt-5-mini`（大型）形成大小对比。第三方文件 ([15-browser-use/llms.txt](../../15-browser-use/llms.txt))、历史 GitHub Models 文本以及 `azure-openai-to-responses` 技能的能力说明有意保持不变。
- **第 14 课交接笔记本迁移至稳定 API。** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) 现在使用 `agent_framework.orchestrations.HandoffBuilder` 搭配 `.with_start_agent(...)`、`HandoffAgentUserRequest.create_response(...)`、基于 `event.type` 的流式处理，以及 `FoundryChatClient`（替代已移除的 pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` 符号）。
- **第 14 课人机交互笔记本迁移至稳定 API。** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) 现在通过 `ctx.request_info(...)` + `@response_handler`（替代已移除的 `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`）实现暂停，使用 `WorkflowBuilder(start_executor=..., output_executors=[...])` 构建，通过 `default_options={"response_format": ...}` 传递结构化输出，且使用脚本化回答使笔记本无需阻塞 `input()` 即可无人值守运行。
- <strong>环境配置</strong>（[.env.example](../../.env.example)）：模型部署名称切换为 `gpt-5-mini`；新增 `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL`（第 16 课路由）以及之前遗漏的 `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`（第 15 课浏览器使用）。
- <strong>依赖项</strong>（[requirements.txt](../../requirements.txt)）：将 `agent-framework`、`agent-framework-foundry` 和 `agent-framework-openai` 固定为 `~=1.10.0` 版本，以确保自洽且经过验证的版本集（1.11.0 版本包含对本课程所用接口的实验性破坏性变更）。

### 备注与已知限制

- **已针对实时 Microsoft Foundry 验证。** Python 笔记本使用 `nbconvert` 无头执行，针对 Microsoft Foundry 项目使用 `gpt-5-mini`（第 16 课路由使用 `gpt-5-nano`）进行了测试。请在自己的项目中部署相当的非弃用模型；笔记本从环境变量 `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` 读取部署名称。
- <strong>部分课程仍需额外资源。</strong>第 05 课需要 Azure AI 搜索；第 08 课的 Bing 基础工作流（`04.python-agent-framework-workflow-aifoundry-condition.ipynb`）需要连接 Bing 和 Microsoft Foundry Agent Service 托管工具；第 13 课（Cognee）和第 17 课（Foundry Local）需要它们各自的运行时环境。

## [发布] — 2026-07-13

本次发布新增了两个完成部署流程的新课程——使代理可扩展至 Microsoft Foundry 以及缩减至单台工作站，此外还包含一次冒烟测试管道、更新后的课程导航、新增学习者技能和品牌更新。

### 新增

- **第 16 课——使用 Microsoft Foundry 部署可扩展代理。** 新课程 [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) 及可运行笔记本 [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb)，构建生产级客户支持代理（工具、RAG、记忆、模型路由、响应缓存、人类审批、评估门控及 OpenTelemetry 跟踪），包括开发/部署/运行时的 Mermaid 图示、知识检测、作业和挑战。
- **第 17 课——使用 Foundry Local 和 Qwen 创建本地 AI 代理。** 新课程 [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) 及笔记本 [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb)，构建完全本地运行的工程助理（通过 Foundry Local 使用 Qwen 函数调用、沙箱文件工具、本地 RAG 使用 Chroma、可选本地 MCP），含本地专用 / 本地 RAG / 调用工具的图示、知识检测、作业和挑战。
- **冒烟测试管道。** 新增 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) 工作流 [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml)，以及针对第 01、04、05 和 16 课部署代理的每课目录，位于 [tests/](./tests/README.md)，含索引 README 将每个目录映射到对应课程序列号及托管代理名称。第 16 课新增“使用冒烟测试验证已部署代理”章节；第 01/04/05 课增加可选冒烟测试指引。
- **学习者技能。** 新增 .agents/skills/ 下的代理技能：[deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md)、[local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md)（涵盖第 16 和 17 课内容），以及 [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md)（如何针对实时 Microsoft Foundry / Azure OpenAI 环境验证笔记本示例）。
- **笔记本验证运行器。** 新增 [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1)，使用 `nbconvert` 无头执行每个 Python 笔记本并打印 PASS/FAIL 矩阵（以及 `results.json`）。自动检测仓库根目录和 Python 环境，默认排除非课程笔记本（`.venv`、`site-packages`、`translations`、技能模板资源）和 .NET 笔记本，支持 `-Filter`、`-Timeout`、`-List`、`-IncludeDotnet` 和 `-Python` 参数。
- **课程导航。** 为第 11 至 15 课添加了“上一课/下一课”链接（此前缺失），使整个课程从 00 至 18 课双向串联。
- **新缩略图。** 为第 16 和 17 课新增课程缩略图，刷新了仓库社交图像 [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png)（现展示两门新课及 `aka.ms/ai-agents-beginners` 链接）。
- <strong>依赖项</strong>（[requirements.txt](../../requirements.txt)）：为第 17 课新增了 `foundry-local-sdk` 和 `chromadb` 依赖。

### 变更

- **主 [README.md](./README.md)** 课程序列表：第 16 和 17 课现已链接到课程内容（此前标记为“敬请期待”）；仓库图像更新为 `repo-thumbnailv3.png`。
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**：将第 16 和 17 课加入逐课指南及学习路径，并新增“使用冒烟测试验证已部署代理”章节。
- **[AGENTS.md](./AGENTS.md)**：更新课程数目/描述（00–18 课），新增冒烟测试验证章节，添加第 16 和 17 课示例命名示范。
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**：“上一课”链接更改为第 17 课（原为第 15 课），完成课程链路闭合。
- **对非弃用模型的标准化引用。** 将课程中所有 `gpt-4o` / `gpt-4o-mini` 的引用（文档、`.env.example`、Python/.NET 笔记本及示例）替换为 `gpt-4.1-mini` — `gpt-4o`（所有版本）将于 2026 年退役。第 16 课模型路由示例保持用 `gpt-4.1-mini`（小型）和 `gpt-4.1`（大型）形成大小对比。Python 笔记本现在从环境变量 (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) 选择模型，而非硬编码模型名称。

### 备注与已知限制

- **未针对实时 Azure 执行。** 新课程笔记本为教学示例；请针对你自己的 Microsoft Foundry / Foundry Local 环境运行和验证。冒烟测试工作流要求你部署课中代理，并在 Foundry 项目范围内为 Azure OIDC 密钥（`AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_SUBSCRIPTION_ID`）配置具有 **Azure AI 用户** 角色。
- **第 17 课仅限本地运行。** 它没有 Foundry Responses 端点，因此冒烟测试操作不适用；请通过在工作站上运行笔记本进行验证。

## [发布] — 2026-07-06

本次发布将课程迁移至 **Azure OpenAI Responses API**，将产品命名标准化为 **Microsoft Foundry** 和 **Microsoft Agent Framework (MAF)**，废弃 GitHub Models，更新 SDK 版本，新增本地模型及在 Foundry 上托管其他框架的内容。

### 新增

- <strong>迁移技能</strong> — 安装了 [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) 代理技能（来自 [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)），放置在 `.agents/skills/`，含其引用及扫描脚本。
- **Foundry Local（本地运行模型）** — 在 [00-course-setup/README.md](./00-course-setup/README.md) 中新增“替代提供者：Foundry Local”章节，介绍安装方法（`winget` / `brew`）、`foundry model run`、`foundry-local-sdk`，以及通过 `OpenAIChatClient` 将 `FoundryLocalManager` 绑定到 Microsoft Agent Framework。
- **在 Microsoft Foundry 上托管 LangChain / LangGraph 代理** — 在 [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) 新增章节，并提供了可运行示例 [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)，使用 `langchain-azure-ai[hosting]` 和 `ResponsesHostServer`（`/responses` 协议），基于 [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)。
- **Microsoft Project Opal** — 在 [15-browser-use/README.md](./15-browser-use/README.md) 中新增“真实案例示范：Microsoft Project Opal”章节，将 Opal 作为企业计算使用代理，并映射至课程概念（人机交互、信任/安全、规划、技能）。
- **第二个第 02 课 Python 示例** — 新增了 [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb)（见“变更”——从此前的 Semantic Kernel 笔记本迁移而来），并将其链接至课程 README。
- **新增“模型与提供者”章节** 于 [STUDY_GUIDE.md](./STUDY_GUIDE.md)。

### 变更

- **Chat Completions → Responses API（Python）。** 直接调用模型的示例迁移至 Responses API（使用 `client.responses.create(input=..., store=False)`，结果通过 `resp.output_text` 获取），使用 `OpenAI` 客户端调用稳定的 Azure OpenAI `/openai/v1/` 终结点（无 `api_version`）。涉及示例包括：
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — 完整函数调用演练（工具架构转换为 Responses 格式，工具结果作为 `function_call_output`、`max_output_tokens` 等返回）。

- **GitHub 模型 → Azure OpenAI。** GitHub 模型已弃用（**2026 年 7 月退休**），且不支持 Responses API。所有 GitHub 模型代码路径均已转换为 Azure OpenAI / Microsoft Foundry，覆盖 Python 和 .NET 示例：
  - Python：第 08 课工作流笔记本（`01`–`03`）、第 14 课（`14-handoff`、`14-human-loop`、`hotel_booking_workflow_sample.py`）。
  - .NET：`01`–`04`、`07`、`08` `*-dotnet-agent-framework.cs` 及配套的 `.md` 文档，以及第 08 课 dotNET 工作流笔记本/`.md`（`01`–`03`）现在使用 `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` 并结合 `AzureCliCredential`。
- **语义内核 → Microsoft Agent Framework。** 之前的 `02-semantic-kernel.ipynb` 现已重写为使用带有 Azure OpenAI（Responses API）的 Microsoft Agent Framework，并重命名为 `02-python-agent-framework-azure-openai.ipynb`。
- **统一使用 `FoundryChatClient` + `as_agent`。** README 和笔记本中引用的 `AzureAIProjectAgentProvider` 代码统一采用第 01 课和框架自带示例中使用的标准模式：`FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` 配合 `provider.as_agent(...)`。已在第 02–14 课的 README 和笔记本中更新（例如，第 13 课内存，第 14 课所有笔记本，`11-agentic-protocols/code_samples/github-mcp/app.py`）。
- **产品命名。** 英文内容整体重命名：
  - “Azure AI Foundry” / “Azure AI Studio” → **Microsoft Foundry**
  - “Azure AI Agent Service” → **Microsoft Foundry Agent Service**
  - （不变：“Azure OpenAI”、“Azure AI Search”、“Azure AI Inference” 以及环境变量名称。）
- <strong>依赖项</strong> ([requirements.txt](../../requirements.txt))：
  - 固定 `agent-framework>=1.10.0`、`agent-framework-foundry>=1.10.0`、`agent-framework-openai>=1.10.0`。
  - 固定 `openai>=1.108.1`（Responses API 的最低版本）。
  - 移除 `azure-ai-inference`（仅在迁移的 GitHub 模型示例中使用）。
- <strong>环境配置</strong> ([.env.example](../../.env.example))：移除 GitHub 模型变量 (`GITHUB_TOKEN`、`GITHUB_ENDPOINT`、`GITHUB_MODEL_ID`)；新增 `AZURE_OPENAI_ENDPOINT`、`AZURE_OPENAI_DEPLOYMENT` 和可选的 `AZURE_OPENAI_API_KEY`；命名统一为 Microsoft Foundry。
- <strong>文档</strong> — 更新了 [00-course-setup/README.md](./00-course-setup/README.md)、[AGENTS.md](./AGENTS.md)、[README.md](./README.md) 和 [STUDY_GUIDE.md](./STUDY_GUIDE.md) 以反映上述内容（环境变量设置、验证代码片段、提供程序指南、命名）。

### 已移除

- GitHub 模型入门步骤及环境变量，从设置文档中移除（已由 Azure OpenAI / Microsoft Foundry 取代）。

### 安全 / 隐私（公开共享清理）

- 清理了泄露真实 **Azure 订阅 ID**、资源组 / 资源名称、Bing 连接 ID 以及开发者 <strong>本地文件路径和用户名</strong> 的 Jupyter 笔记本执行输出，涉及：
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- 确认在已跟踪的英文内容中，未残留任何 API 密钥、令牌、订阅 ID 或个人路径（剩余的 `GITHUB_TOKEN` 引用为工作流中的 GitHub Actions 令牌和第 11 课设置中的 GitHub MCP 服务器 PAT，均合法且与 GitHub 模型无关）。

### 备注及已知限制

- **未执行/编译。** 这些均为为 API/命名正确性更新的教学示例；未在实时 Azure 资源上运行，且 .NET 示例未在此环境下编译。请根据你自己的 Microsoft Foundry / Azure OpenAI 部署进行验证。
- **模型部署必须支持 Responses API。** 使用诸如 `gpt-4.1-mini`、`gpt-4.1` 或 `gpt-5.x` 的部署。旧模型支持核心 Responses 功能，但并非所有特性。
- **Agent-framework 版本。** 示例针对最新 MAF（`>=1.10.0`）。典型的代理创建调用为 `client.as_agent(...)`；API 已依据框架发布文档及安装的构建进行验证。若固定不同版本，请确认方法可用性（`as_agent` vs `create_agent`）。
- **第 08 课工作流笔记本 04** 有意保留 `AzureAIAgentClient`（来自 `agent-framework-azure-ai`），因为使用了 Microsoft Foundry Agent Service 托管工具（Bing 基础知识、代码解释器）；其已基于 Responses。
- **.NET 默认部署。** 两个第 08 课 dotNET 工作流示例之前硬编码了特定模型；现默认使用 `AZURE_OPENAI_DEPLOYMENT`（`gpt-4.1-mini`）。若示例依赖多模态/视觉输入，请将 `AZURE_OPENAI_DEPLOYMENT` 设置为合适模型。
- **Foundry Local** 暴露了一个兼容 OpenAI 的 <strong>聊天补全</strong> 端点，旨在本地开发；完整的 Responses API 功能请使用 Azure OpenAI / Microsoft Foundry。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->