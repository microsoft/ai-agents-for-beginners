# 构建计算机使用代理（CUA）

计算机使用代理可以像人类一样与网站交互：通过打开浏览器，检查页面，并根据所见采取最佳下一步行动。在本课中，你将构建一个浏览器自动化代理，搜索 Airbnb，提取结构化的房源数据，并识别斯德哥尔摩最便宜的住宿。

本课结合了用于 AI 驱动导航的 Browser-Use，控制浏览器的 Playwright 和 Chrome DevTools 协议（CDP），具备视觉推理能力的 Azure OpenAI，以及用于结构化提取的 Pydantic。

## 介绍

本课将涵盖：

- 了解何时计算机使用代理比仅用 API 自动化更合适
- 结合 Browser-Use、Playwright 和 CDP 实现可靠的浏览器生命周期管理
- 使用 Azure OpenAI 视觉能力和结构化的 Pydantic 输出从动态网页中提取房源数据
- 决定何时采用以代理为先、以执行者为先或混合浏览器自动化工作流

## 学习目标

完成本课后，你将学会如何：

- 配置 Browser-Use 联合 Azure OpenAI 和 Playwright
- 构建浏览器自动化工作流，导航真实网站并处理动态 UI 元素
- 从可见页面内容中提取类型化结果，并转化为后续业务逻辑
- 根据浏览器任务的可预测性选择代理模式或执行者模式

## 代码示例

本课包含一个笔记本教程：

- [15-browser-user.ipynb](./15-browser-user.ipynb)：通过 CDP 启动 Chrome 会话，在 Airbnb 上搜索斯德哥尔摩的房源，利用 Browser-Use 视觉提取价格，并返回最便宜的房源作为结构化数据。

## 先决条件

- Python 3.12+
- 配置好的 Azure OpenAI 部署环境
- 本地安装的 Chrome 或 Chromium
- 已安装 Playwright 依赖
- 对异步 Python 有基本了解

## 设置

安装笔记本中使用的软件包：

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

该笔记本演示了一个混合浏览器自动化工作流：

1. Chrome 启动时启用 CDP，以便 Playwright 和 Browser-Use 共享同一浏览器会话。
2. Browser-Use 代理处理开放式导航任务，例如打开 Airbnb、关闭弹窗和搜索斯德哥尔摩。
3. 使用结构化的 Pydantic 模式检查活动页面，提取房源标题、每晚价格、评分和链接。
4. Python 逻辑比较提取的房源，突出最便宜的结果。

这种方法保留了 Browser-Use 擅长的灵活视觉推理，同时在需要时提供确定性的浏览器控制。

## 关键要点和最佳实践

### 何时使用代理 vs 执行者

| 场景 | 使用代理 | 使用执行者 |
|----------|-----------|-----------|
| 动态布局 | 是，AI 能适应页面变化 | 否，脆弱的选择器会崩溃 |
| 结构已知 | 否，代理比直接控制慢 | 是，快速且精确 |
| 查找元素 | 是，自然语言效果好 | 否，需要精确选择器 |
| 时间控制 | 否，较不可预测 | 是，可以完全控制等待和重试 |
| 复杂工作流 | 是，能处理意外 UI 状态 | 否，需要显式分支 |

### Browser-Use 最佳实践

1. 从代理开始，用于探索和动态导航。
2. 当交互变得可预测时切换到直接页面控制。
3. 使用结构化输出模型，确保提取数据经过验证且类型安全。
4. 在触发可见 UI 变化的操作后有策略地添加延迟。
5. 迭代过程中截图，便于调试失败。
6. 预期网站会变化，设计弹窗和布局变动的备选方案。
7. 结合代理和执行者模式，兼顾灵活性与精确性。

### 浏览器代理的安全防护措施

浏览器代理操作的是实时网站，因此需要比只调用已知 API 的脚本更严格的边界。在从笔记本演示转向真实工作流之前，定义代理可见、点击和提交的范围。

1. **限定浏览环境。** 在独立浏览器配置文件或沙箱中运行代理，限制到任务所需的域名。
2. **分离观察和操作。** 先让代理搜索、读取和提取数据；提交表单、发送消息、预订、购买、删除记录或更改账户设置前需用户显式批准。
3. **避免在提示和记录中暴露机密。** 不在模型上下文中放置密码、支付信息、会话 Cookie 或原始个人数据。用户应负责认证，且敏感字段从日志中打码。
4. **把页面内容当作不可信输入。** 网站可能包含针对代理的指令，而非用户指令。代理应忽略要求更改目标、泄露数据、禁用防护或访问无关网站的页面文本。
5. **在风险步骤使用确定性检查。** 在请求用户批准最终步骤前，通过代码验证当前 URL、页面标题、选中项、价格、接收方和操作摘要。
6. **设定预算和停止条件。** 限制代理可执行的操作次数、重试次数、标签页数和时长。遇到页面状态不明时停止操作，避免盲目点击。
7. **记录有用证据，避免记录全部内容。** 保留操作摘要、时间戳、URL、选中元素描述和截图引用，便于回顾失败，不保存不必要的敏感页面内容。

在 Airbnb 示例中，安全默认行为是搜索房源并提取价格。登录、联系房东或完成预订应为用户批准的单独操作。

### 真实应用案例

- 旅行预订和价格监控
- 电子商务价格比较和库存检查
- 从动态网站结构化提取数据
- 具备视觉感知的 UI 测试和验证
- 网站监控和报警
- 多步骤流程的智能表单填写

## 真实案例：微软 Project Opal

本课中构建的代理是一个小型本地版本的<strong>计算机使用代理（CUA）</strong>——一种以类似人类方式驱动浏览器的程序。微软正将这一理念带给企业，推出了 Microsoft 365 Copilot 中的<strong>[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)</strong>功能。

通过 Project Opal，你描述一个任务，代理会代表你使用<strong>在安全的 Windows 365 云 PC 上的计算机使用</strong>，跨你组织内的基于浏览器的应用、站点和数据异步工作。你可以随时引导或接管其工作。示例任务包括：

- 管理安全组成员请求
- 为合规审查收集和验证审计证据
- IT 事件分类（更新票务状态、分配负责人、关闭重复）
- 将 Excel 数据汇总至财务结算报告

Opal 是一个生产级、值得信赖的计算机使用代理的有力示范，且强化了本课程中早期的概念：

| 本课程中的概念 | Project Opal 的应用 |
|------------------------|-----------------------------|
| <strong>人机协作</strong>（第 06 课） | Opal 在登录凭证、敏感数据或模糊指令时暂停，且绝不会在未明确确认的情况下输入密码或提交表单。可在任务中途<em>接管控制</em>和<em>返回控制</em>。 |
| <strong>可信和安全代理</strong>（第 06 和 18 课） | 运行在隔离的 Windows 365 云 PC 中，默认仅限浏览器访问（通过 Intune 强制阻止其它计算机访问），使用<em>你的</em>身份访问仅授权内容，且记录所有操作以便审计。 |
| <strong>规划与元认知</strong>（第 07 和 09 课） | Opal 先生成作业计划，然后在每步监督自身推理，检测异常时暂停。 |
| **可复用能力/工具**（第 04 课） | <strong>技能</strong>让你为重复作业编写指令（从 `.md` 文件导入或用 Opal 编写），并在对话中复用。 |

> **可用性：** Project Opal 当前面向拥有 Microsoft 365 Copilot 订阅的 [Frontier 早期访问计划](https://adoption.microsoft.com/copilot/frontier-program/)用户开放，且需管理员完成设置。作为实验性 Frontier 功能，其能力可能会随时间变化。

## 知识检测

在进入下一课前测试你的理解。

**1. 何时基于浏览器的计算机使用代理比仅用 API 流程更合适？**

<details>
<summary>答案</summary>

当任务依赖网页 UI 中可见内容，且网站没有提供所需 API，或者页面经常变化使得固定的 API 或选择器逻辑脆弱时，使用浏览器代理。如果存在用于同样任务的稳定 API，优先使用 API，因为它通常更快、更易测试且更安全。
</details>

**2. 在混合工作流中，哪些部分应由代理处理，哪些部分应由直接 Playwright 代码处理？**

<details>
<summary>答案</summary>

让代理处理开放式导航和动态 UI 状态，如找到正确页面或关闭意外弹窗。当页面结构已知且操作需要精准、重试、等待或确定性验证时，切换到直接 Playwright 控制。
</details>

**3. Airbnb 示例找到用户可能想预订的房源。工作流在登录、联系房东或完成预订前应做什么？**

<details>
<summary>答案</summary>

工作流应暂停并请求用户明确批准。请求前应显示所选房源、当前 URL、价格、日期和预期操作的清晰摘要。搜索和提取价格可以自动完成；账户访问、消息、购买和预订应由用户批准。
</details>

**4. 网页告诉代理忽略最初的指令，访问其他站点并暴露已保存的凭据。代理应如何处理该文本？**

<details>
<summary>答案</summary>

应将其视为不可信的页面内容，而非开发者或用户指令。代理应保持在允许的域名和任务范围内，拒绝泄露机密，避免遵循更改目标、禁用防护或跳转至无关站点的页面文字。
</details>

**5. 浏览器代理运行时应保留哪些证据，哪些应避免？**

<details>
<summary>答案</summary>

保留操作摘要、时间戳、URL、选中元素描述、验证结果和截图引用，以便回顾运行。避免保存密码、支付信息、会话 Cookie、原始个人数据或完整页面内容，除非有明确的保留和隐私需求。
</details>

## 附加资源

- [开始使用 Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright 集成模板](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use 执行者参数与内容提取](https://docs.browser-use.com/customize/actor/all-parameters)
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