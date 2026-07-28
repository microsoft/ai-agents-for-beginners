---
name: testing-course-samples
---
# 测试课程样例

验证课程笔记本和代码示例是否能在实际运行的
Microsoft Foundry / Azure OpenAI 环境下执行。仓库提供了一个运行脚本位于
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1)，
它可以无头执行每个 Python 笔记本，并打印通过/失败矩阵。

## 何时使用
- “验证所有笔记本 / 示例在我的 Azure 订阅下是否正常。”
- “在升级包或更改模型后对课程做冒烟测试。”
- “哪些课程依旧通过 / 失败？”

<strong>不</strong>要用此工具来替代 AI Smoke Test GitHub Action（用于验证<em>已部署</em>的
托管代理 — 见 [`tests/README.md`](../../../tests/README.md)）。本工具
是本地执行笔记本。

## 先决条件（先检查）
1. **Python 3.12+** 及课程依赖：`python -m pip install -r requirements.txt`
   还需要执行器：`python -m pip install nbconvert ipykernel`。
2. 仓库根目录需要 **`.env` 文件**（从 [`.env.example`](../../../../../.env.example) 复制），至少包含：
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry 项目端点
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — 一个未弃用的部署名称（例如 `gpt-5-mini`）
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) 和 `AZURE_OPENAI_DEPLOYMENT`
     用于直接调用 Azure OpenAI 的课程（课程 06、02-azure-openai、14 handoff/human-loop）。
3. 完成 **`az login`** — 示例使用 `AzureCliCredential` 认证（Entra ID，无密钥）。
4. 验证模型部署存在：
   运行命令 `az cognitiveservices account deployment list -g <rg> -n <account> -o table`。

## 运行验证
```powershell
# 所有Python笔记本（跳过.NET、.venv、site-packages、翻译、技能资源）
pwsh scripts/validate-notebooks.ps1

# 单个课时，每个单元格有较长的超时时间
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# 仅列出将要运行的内容（不执行）
pwsh scripts/validate-notebooks.ps1 -List

# 显式指定解释器（如果`python`不在PATH中，例如Windows商店别名）
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
该脚本会写出执行的副本、每个笔记本的日志、以及 `results.json` 到
`$env:TEMP\aiab-nbval`，并以失败数作为退出码。

临时失败（共享订阅的 HTTP 429 速率限制、偶发的
`AzureCliCredential` 令牌故障或超时）会自动重试
（`-Retries`，默认 2 次，带 `-RetryDelaySeconds` 退避，默认 20 秒）。如果某个
模型部署经常出现 429 错误，检查订阅的 GlobalStandard
TPM 配额（`az cognitiveservices usage list -l <region>`）——单个
部署容量增加无效，因为是<em>订阅</em>配额用尽了。

## 结果解读
- `PASS` — 笔记本全程运行无单元格错误。
- `FAIL` — 显示首个 `*Error` / `*Exception` 行；查看输出目录中的对应
  `log_*.txt` 获取完整回溯。
- 单个笔记本的失败由 `-Timeout`（每单元格计时）限制，所以卡住的
  人机交互单元格会抛出 `StdinNotImplementedError` 而非死锁。

## 需要额外资源的课程（无资源时预计失败）
| 课程 | 额外需求 |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — 含内存回退路径 |
| 11 MCP / GitHub | GitHub MCP 服务器 + PAT |
| 13 memory (cognee) | 配置好的 `cognee` 模型提供者 |
| 15 browser-use | Playwright 浏览器已安装 (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry 本地运行时 + 已下载的 Qwen 模型（设备端，无云） |
| `*-dotnet-*` 笔记本 | .NET Interactive 内核（默认排除；用 `-IncludeDotnet` 包含） |

## 反馈报告
按课程汇总为通过/失败表。区分真实回归
（需修复代码/配置缺陷）与环境缺失（缺少 Search/Foundry Local/PAT），
并引用每个真实失败对应的 `log_*.txt`。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->