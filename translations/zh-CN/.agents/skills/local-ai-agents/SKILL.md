---
name: local-ai-agents
license: MIT
---
# 使用 Foundry Local 和 Qwen 创建本地 AI 代理

> 伴随 [第17课 – 创建本地 AI 代理](../../../17-creating-local-ai-agents/README.md) 的附加技能。
> 用它来帮助学习者构建一个能够推理、调用工具并且
> 完全在他们自己的机器上搜索文档的代理——无云推理。所有
> 建议均基于课程内容和可运行的笔记本。

## 触发条件

当学习者希望：
- 由于隐私、成本或离线需求而<strong>完全在设备上运行</strong>代理时。
- 使用 **Foundry Local** 在本地部署模型，并通过 OpenAI 兼容端点进行连接。
- 使用 <strong>Qwen 函数调用</strong>模型来驱动可靠的本地工具调用时。
- 添加 **本地 RAG**（Chroma）或 **本地 MCP 服务器**。
- 设计一个<strong>混合型</strong>本地/云路由策略。

## 核心思路模型

一个 SLM 以隐私、成本和离线操作为代价换取广度。成功的
策略是：<strong>让 SLM 进行协调，让工具承担繁重工作。</strong>模型不需要<em>了解</em>代码库——只需知道何时调用
`read_file` 和 `search_docs`。这发挥了 SLM 的优势（受限决策，
如工具选择），避免其弱点（广泛知识、长链推理）。



## 选择这些组件的原因

- **Foundry Local** 暴露了一个<strong>OpenAI 兼容的 HTTP 端点</strong>，所以云端的代理代码只需更改 `base_url`（并使用本地占位 API 密钥）即可迁移。同时自动为机器选择最佳构建（CPU/GPU/NPU）。
- **Qwen** 模型被训练为函数调用，可稳定产生格式良好的工具调用——这使得本地<em>聊天</em>模型转变为本地<em>代理</em>。
- **Chroma** 在进程内运行并将向量存储在磁盘上，因此整个 RAG 流程（嵌入 → 存储 → 检索 → 推理）保持本地。
- **MCP** 是一种传输协议，不是云服务：MCP 服务器可以在本地通过 `stdio` 运行。

## 必备设置

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # 本地占位符
```

约 8 GB 内存是实际最低要求；有 GPU/NPU 有助于性能但非必需。

## 关键模式复现

指引学习者使用笔记本
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb)：

- <strong>沙盒工具</strong>：每个文件工具解析路径，并拒绝超出单一项目根目录的请求——即使本地，工具也以用户权限运行。
- <strong>工具调用循环</strong>：用 OpenAI 工具 schema 注册工具，在本地执行请求的工具，反馈结果，循环直到给出最终答案。
- **本地 RAG**：将文档 upsert 到 Chroma 集合；`search_docs` 返回 top-k 文档块。
- **本地 MCP**：通过 `stdio` 连接本地服务器；以项目目录为作用域并验证其输出。

## 混合路由（本地作为模型之一）

| 情况 | 运行位置 |
|-----------|---------------|
| 敏感数据 / 离线 | 本地 SLM |
| 简单、受限任务 | 本地 SLM（廉价、快速） |
| 复杂多跳推理处理非敏感数据 | 云端模型 |
| 云服务中断 | 本地 SLM（渐进降级） |

这与第16课中的模型路由思想相呼应，工作站作为其中一条路由。优先考虑优雅降级到本地的设计，使代理质量降低而非完全失败。



## 助手的护栏

- 将每个文件/工具操作限定在沙盒项目目录内。
- 当学习者明确目标为隐私/离线时，不将代码或数据发送到云端——保持整个流程本地。
- 对 SLM 质量设定合理预期；依赖工具和 RAG 而非模型记忆知识。
- 注意第17课没有 Foundry Responses 端点，因此云端烟雾测试操作不适用——通过本地运行笔记本进行验证。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->