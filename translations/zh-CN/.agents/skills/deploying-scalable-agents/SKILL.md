---
name: deploying-scalable-agents
license: MIT
---
# 使用 Microsoft Foundry 部署可扩展代理

> 配合 [第16课 – 部署可扩展代理](../../../16-deploying-scalable-agents/README.md) 的辅助技能。
> 用于帮助学习者将代理从原型推进到可扩展的可观察
> 生产部署。所有建议均基于课程内容和
> 可运行的笔记本；不得自行发明 Foundry API。

## 触发条件

当学习者想要时激活此技能：
- 将代理部署到 Microsoft Foundry 作为<strong>托管代理</strong>，并使其具有版本管理/可观察性。
- 在 **客户端托管、托管代理和代理工作流** 部署模式之间做选择。
- 添加 <strong>模型路由</strong>、<strong>响应缓存</strong> 或 <strong>有边界并发</strong> 以控制延迟和成本。
- 添加<strong>评估门控</strong>，避免错误的代理版本投产。
- 为高风险操作添加<strong>人机审核</strong>步骤。
- 使用 **OpenTelemetry** 追踪为生产环境代理添加监测。
- 对已部署代理进行<strong>冒烟测试</strong>，作为快速的部署后门控。

## 核心思维模型

生产代理主要是模型（约80%）的<em>运行骨架</em>，
而非模型本身。将所有建议映射到下述关注点之一：

| 关注点 | 原型 → 生产 |
|---------|------------------------|
| 托管 | 笔记本 → 版本化托管服务 |
| 身份 | 你的 `az login` → 托管身份 + 有范围的 RBAC |
| 状态 | 内存中 → 外部线程/内存存储 |
| 故障 | 追踪错误 → 重试、回退、警报 |
| 成本 | “几分钱” → 追踪、路由、缓存、预算 |
| 质量 | 目测 → 自动评估门控 |
| 信任 | 你批准 → 策略 + 人机审核 |

## 部署模式（选择一种，或组合使用）

1. <strong>客户端托管</strong> — 推理循环在你进程中运行。最大控制权；你负责扩展和状态管理。
2. **托管代理（Foundry Agent Service）** — Foundry 托管循环、存储线程、执行 RBAC/内容安全，门户显示代理。控制较少，运维复杂度大幅降低。
3. <strong>代理工作流</strong> — 多代理/工具组成的图形，带分支、审批节点和持久化检查点。

## 生命周期（代理交付的循环）

`创建 → 版本化 → 评估（门控）→ 托管部署 → 在线观察 → 收集故障 → 重复`。
**离线评估是门控，而非事后附加** — 未达到门限的版本不会交付。
在线可观察性将实际故障反馈
至离线测试集。

## 扩展与成本控制手段（优先顺序）

1. <strong>模型选型适当</strong> — 使用能通过评估门控的最小模型。
2. <strong>按复杂度路由</strong> — 简单请求用小而快的模型，复杂推理用大的模型（自定义分类器或 Foundry 模型路由器）。
3. <strong>缓存</strong> — 对近似重复请求无需调用模型即可提供服务。
4. **无状态设计 + 有界并发** — 状态外部化；带退避的重试。

## 关键模式复现

引导学习者关注笔记本中的以下内容
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- <strong>请求处理器</strong>：缓存 → 按复杂度路由 → 追踪跨度 → 运行 → 缓存。
- <strong>评估门控</strong>：对离线测试集评分；返回 `pass_rate >= threshold`，仅当为真时才部署。
- <strong>人工审批</strong>：针对大额退款等操作用 `@tool(approval_mode="always_require")`。
- <strong>追踪</strong>：用 `tracer.start_as_current_span(...)` 包裹每个请求，并设置 `routed.model`、`customer.id` 等属性。

## 已部署代理的冒烟测试

部署后，验证端点是否真正响应（部署成功也可能无响应）。
使用 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
操作，通过 [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
和 [`tests/`](../../../tests/README.md) 中的目录。运行程序将每个
提示 POST 到 `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
并断言回复文本。身份需在 Foundry 项目范围内拥有<strong>Azure AI User</strong>角色；
令牌受众必须是 `https://ai.azure.com/`。

多重门控：<strong>冒烟测试</strong>（可达且响应，每次部署）→ <strong>离线评估</strong>（足够好才投产，晋升前）→ <strong>在线评估</strong>（实际表现，持续进行）。



## 企业级控制

- **RBAC**：为每个托管代理分配最小权限的托管身份。
- **生产环境的 MCP**：将每个 MCP 服务器视为不可信边界 — 固定版本、限定身份、验证输出、限流，绝不泄露密钥。

## 助手的安全护栏

- 优先使用全课程推荐的标准 `FoundryChatClient(...)` + `provider.as_agent(...)` 模式。
- 不得承诺未经验证的实时 Azure 结果；建议使用冒烟测试工作流确认部署。
- 评估与成本建议保持绑定：评估设定质量底线，路由/缓存带来接近该底线的成本控制。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->