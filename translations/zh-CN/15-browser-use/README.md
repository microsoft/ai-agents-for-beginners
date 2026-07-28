# 构建计算机使用代理（CUA）

计算机使用代理能够像人一样与网站交互：通过打开浏览器、检查页面，并根据看到的内容采取最佳后续操作。在本课中，你将构建一个浏览器自动化代理，它能够搜索 Airbnb，提取结构化的房源数据，并识别斯德哥尔摩最便宜的住宿。

本课结合了 AI 驱动导航的 Browser-Use，Playwright 和 Chrome DevTools 协议 (CDP) 进行浏览器控制，Azure OpenAI 实现视觉感知推理，以及 Pydantic 实现结构化提取。

## 介绍

本课将涵盖：

- 了解何时计算机使用代理比仅使用 API 自动化更合适
- 将 Browser-Use 与 Playwright 和 CDP 结合，实现可靠的浏览器生命周期管理
- 使用 Azure OpenAI 视觉功能和结构化 Pydantic 输出从动态网页提取房源数据
- 决定何时使用以代理为主、以执行者为主或混合的浏览器自动化工作流

## 学习目标

完成本课后，你将知道如何：

- 配置 Browser-Use 以集成 Azure OpenAI 和 Playwright
- 构建浏览器自动化工作流，导航真实网站并处理动态 UI 元素
- 从可见页面内容中提取类型化结果，并将其转化为下游业务逻辑
- 根据浏览器任务的可预测性，选择代理模式还是执行者模式

## 代码示例

本课包含一个笔记本教程：

- [15-browser-user.ipynb](./15-browser-user.ipynb)：通过 CDP 启动 Chrome 会话，搜索 Airbnb 上斯德哥尔摩房源，利用 Browser-Use 视觉提取价格，并返回最便宜的选项作为结构化数据。

## 前提条件

- Python 3.12 及以上版本
- 已在你的环境中配置 Azure OpenAI 部署
- 本地安装 Chrome 或 Chromium
- 安装 Playwright 依赖
- 对异步 Python 有基本了解

## 设置

安装笔记本中使用的包：

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

设置笔记本使用的 Azure OpenAI 环境变量：

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# 可选：省略时默认为最新的API版本
AZURE_OPENAI_API_VERSION=...
```

## 架构概览

笔记本展示了一个混合浏览器自动化工作流：

1. 启动带 CDP 的 Chrome，Playwright 和 Browser-Use 可以共享同一浏览器会话。
2. Browser-Use 代理负责开放式导航任务，如打开 Airbnb、关闭弹窗和搜索斯德哥尔摩。
3. 使用结构化的 Pydantic 模式检查当前页面，提取房源标题、每晚价格、评分和网址。
4. Python 逻辑对提取的房源进行比较，并突出显示最便宜的结果。

这种方法既保留了 Browser-Use 擅长的灵活视觉推理，也在需要时提供确定性的浏览器控制。

## 关键要点与最佳实践

### 何时使用代理与执行者

| 场景 | 使用代理 | 使用执行者 |
|----------|-----------|-----------|
| 动态布局 | 是，AI 可以适应页面变化 | 否，脆弱的选择器可能出错 |
| 已知结构 | 否，代理比直接控制慢 | 是，快速且精准 |
| 查找元素 | 是，自然语言效果好 | 否，需精准选择器 |
| 时间控制 | 否，较不可预测 | 是，完全控制等待和重试 |
| 复杂工作流 | 是，能处理意外 UI 状态 | 否，需要显式分支 |

### Browser-Use 最佳实践

1. 初期探索和动态导航时使用代理。
2. 交互变得可预测后切换至直接页面控制。
3. 使用结构化输出模型，确保提取数据经过验证且类型安全。
4. 在触发可见 UI 变化的操作后，策略性地添加延迟。
5. 迭代过程中截图，便于调试失败原因。
6. 预期网站会变化，设计弹窗和布局变动的回退策略。
7. 混合代理和执行者模式，实现灵活性与精确性的结合。

### 浏览器代理的安全防护措施

浏览器代理操作的是实时网站，因此它需要比仅调用已知 API 的脚本更严格的边界。在从笔记本示例移至真实工作流前，要定义代理可查看、点击和提交的范围。

1. **限定浏览环境。** 让代理在专用浏览器配置文件或沙箱中运行，并限制其访问任务所需域名。
2. **区分观察与操作。** 让代理先搜索、读取和提取数据；在提交表单、发送消息、预订、购买、删除记录或更改账户设置前，必须有明确批准步骤。
3. **不要在提示和追踪中包含秘密。** 不要将密码、支付信息、会话 Cookie 或原始个人数据放入模型上下文。让用户负责身份验证，并从日志中删去敏感字段。
4. **将页面内容视为不可信输入。** 网站可能包含专门针对代理的指令，而非用户。代理应忽略要求更改目标、泄露数据、关闭安全保护或访问无关网站的页面文本。
5. **在风险操作前做确定性检查。** 在请求用户批准最终步骤之前，通过代码验证当前 URL、页面标题、选中项、价格、收件人和操作摘要。
6. **设定预算和停止条件。** 限制代理可执行的操作次数、重试次数、标签页数量和运行时间。当页面状态不明确时停止操作，而不是继续点击。
7. **记录有用证据，而非全部信息。** 保存操作摘要、时间戳、URL、选中元素描述以及截图引用，方便失败时回溯，不存储不必要的敏感页面内容。

在 Airbnb 示例中，安全的默认操作是搜索房源并提取价格。登录、联系房主或完成预订应作为单独的用户批准操作。

### 现实世界应用

- 旅游预订和价格监控
- 电子商务价格比较和库存检查
- 从动态网站结构化提取数据
- 视觉感知的 UI 测试和验证
- 网站监控和警报
- 多步骤流程中的智能表单填写

## 现实案例：微软 Project Opal

你在本课构建的代理是一个小型且本地的 **计算机使用代理（CUA）** —— 一种像人一样驱动浏览器的程序。微软将这一理念带入企业，推出了 Microsoft 365 Copilot 中的 **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** 功能。

使用 Project Opal，你只需描述任务，代理便能代表你使用 **计算机使用，在安全的 Windows 365 云电脑上** 操作，跨越组织中的基于浏览器的应用、网站和数据。它 <strong>异步后台运行</strong>，你可随时引导工作或接管控制。典型任务包括：

- 管理安全组成员请求
- 收集并验证合规检查的审计证据
- IT 事件的分拣（更新工单状态、分配负责人、关闭重复票据）
- 汇编 Excel 数据形成财务结算报告

Opal 是一个值得借鉴的示例，展示了什么是 **生产级、可信赖** 的计算机使用代理——它也强化了前几课中的概念：

| 本课程中的概念 | Project Opal 的实践 |
|------------------------|-----------------------------|
| <strong>人机协同</strong>（第06课） | Opal 会暂停等待登录凭据、敏感数据或模糊指令，未经明确确认绝不输入密码或提交表单。你可以在任务中途<em>接管控制</em>或<em>归还控制</em>。 |
| <strong>可信且安全的代理</strong>（第06与18课） | 运行在隔离的 Windows 365 云电脑上，默认仅允许浏览器访问（通过 Intune 强制阻止其他计算机访问），使用<em>你的</em>身份访问授权资源，且记录每步操作以便审计。 |
| <strong>规划与元认知</strong>（第07与09课） | Opal 先生成工作计划，然后在每一步监督自身推理，若检测到可疑行为会暂停。 |
| **可复用功能/工具**（第04课） | <strong>技能</strong>让你编写可重复任务的指令（从 `.md` 文件导入或用 Opal 编写），并在多次对话中重用。 |

> **可用性：** Project Opal 目前向 [Frontier 早期访问计划](https://adoption.microsoft.com/copilot/frontier-program/)中的用户开放，需订阅 Microsoft 365 Copilot，且管理员必须完成设置。由于它是试验性质的 Frontier 功能，能力可能会随时间变化。

## 额外资源

- [开始使用 Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright 集成模板](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use 执行者参数和内容提取](https://docs.browser-use.com/customize/actor/all-parameters)
- [课程设置](../00-course-setup/README.md)

## 上一课

[探索微软代理框架](../14-microsoft-agent-framework/README.md)

## 下一课

[部署可扩展代理](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->