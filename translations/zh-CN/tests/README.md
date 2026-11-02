# 代理烟雾测试

本文件夹包含你在课程中构建的代理的<strong>烟雾测试目录</strong>。
烟雾测试是对<strong>部署在 Microsoft Foundry 上的托管代理</strong>进行的廉价、快速的检查，
用于确认它是否可达、响应正常，并遵循其最基本的提示预期。
它是第一个门槛——不是你在[第10课](../10-ai-agents-production/README.md)和
[第16课](../16-deploying-scalable-agents/README.md)中学习的完整评估流程的替代。


这些目录由 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub 操作通过 [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
工作流调用使用。

## 如何运行

1. <strong>将课程代理部署</strong>到 Microsoft Foundry 作为托管代理（参见
   第16课的部署工作流）。记录<strong>代理名称</strong>和你的
   **Foundry 项目端点**。
2. 添加这些仓库机密（设置 → 机密和变量 → 操作）：
   `AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_SUBSCRIPTION_ID`。联合
   身份需要在<strong>Foundry 项目范围</strong>拥有<strong>Azure AI 用户</strong>角色。
3. 在<strong>操作 (Actions)</strong> 选项卡中，运行<strong>Smoke-test hosted agents（托管代理烟雾测试）</strong>，
   选择对应课程的 `tests_file`，然后输入匹配的 `agent_name` 和
   `project_endpoint`。

## 目录 → 课程 → 代理名称

| 目录 | 课程 | 作为代理部署 |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – AI 代理入门](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – 工具使用](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – 代理式 RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – 部署可扩展代理](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## 哪些课程有烟雾测试？

烟雾测试适用于你<strong>部署代理</strong>并且其文本回复可以
根据已知内容断言的课程。概念类、仅本地运行的课程，
或产生非确定性创意输出的课程则故意排除：

- **第17课（创建本地 AI 代理）** 完全在你的工作站上通过
  Foundry Local 运行，且<strong>不</strong>公开 Foundry Responses 端点，因此
  本操作不适用。请通过本地运行笔记本进行验证。
- 设计模式和理论课程（02、03、06、07、09、12）没有发布一个
  可部署的代理用于烟雾测试。

## 目录模式（快速参考）

每个目录是包含顶层 `tests` 数组的 JSON 文档。每个项提交
一个提示并对回复进行断言：

| 字段 | 含义 |
|-------|---------|
| `id` | 日志中打印的唯一步骤标识符。 |
| `description` | 人类可读的目的描述。 |
| `prompt` | 发送给代理的消息。 |
| `assertions.status` | 预期的 HTTP 状态码（默认 200）。 |
| `assertions.contains_any` | 如果回复包含任一这些子串则通过。 |
| `assertions.contains_all` | 如果回复包含所有这些子串则通过。 |
| `assertions.contains_none` | 如果回复不包含任何这些子串则通过。 |
| `save_response_id_as` | 保存回复 ID 用于后续多轮步骤调用。 |
| `use_previous_response_id` | 本轮请求将与已保存的回复 ID 链接发送。 |

断言是大小写不敏感的子串检查。查看
[操作文档](https://github.com/marketplace/actions/ai-smoke-test)了解
完整模式，包括 Foundry 管理的会话资源。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->