# 课程设置

## 介绍

本课将介绍如何运行本课程的代码示例。

## 加入其他学习者并获取帮助

在开始克隆你的代码库之前，请加入[AI Agents For Beginners Discord 频道](https://aka.ms/ai-agents/discord)以获取设置帮助、课程相关问题或与其他学习者交流。

## 克隆或派生此代码库

首先，请克隆或派生 GitHub 仓库。这将生成你自己的课程材料版本，以便你能运行、测试和调整代码！

可以点击链接 <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">派生仓库</a>

现在你应该拥有本课程的派生版本，链接如下：

![Forked Repo](../../../translated_images/zh-CN/forked-repo.33f27ca1901baa6a.webp)

### 浅克隆（推荐用于工作坊 / Codespaces）

  > 当你下载完整历史记录和所有文件时，完整仓库可能很大（约 3 GB）。如果你只参加工作坊或只需要部分课程序号，浅克隆（或稀疏克隆）将下载更少内容。

#### 快速浅克隆 —— 最小历史记录，含全部文件

将下面命令中的 `<your-username>` 替换为你的派生 URL（或者上游 URL，如果你愿意）。

只克隆最新提交历史（下载量小）：

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

克隆特定分支：

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（稀疏）克隆 — 最小 blobs + 仅选定文件夹

这使用部分克隆和稀疏检出（需要 Git 2.25+，推荐使用支持部分克隆的现代 Git）：

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

进入仓库文件夹：

```bash
cd ai-agents-for-beginners
```

然后指定你想要的文件夹（以下示例展示了两个文件夹）：

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

克隆并确认文件后，如果你只需要文件且想释放空间（无 git 历史），请删除仓库元数据（💀不可逆——你将失去所有 Git 功能）：

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（推荐以避免本地大文件下载）

- 通过 [GitHub UI](https://github.com/codespaces) 为此仓库创建新的 Codespace。

- 在新创建的 Codespace 终端中，运行上述浅克隆/稀疏克隆命令之一，将你需要的课程序号文件夹带入 Codespace 工作区。
- 可选：在 Codespaces 内克隆后，删除 .git 以回收额外空间（见上方删除命令）。
- 注意：如果你选择直接在 Codespaces 中打开仓库（无额外克隆），请注意Codespaces会构建devcontainer环境，可能仍然会配置超过你所需。

#### 提示

- 如果想编辑/提交代码，始终将克隆 URL 替换为你的派生地址。
- 如果以后需要更多历史或文件，可以拉取或调整稀疏检出以包含额外文件夹。

## 运行代码

本课程提供一系列 Jupyter 笔记本，让你通过实践体验构建 AI Agents。

示例代码使用 **Microsoft Agent Framework (MAF)** 和 `FoundryChatClient`，通过 **Microsoft Foundry** 连接到 **Microsoft Foundry Agent Service V2**（Responses API）。

所有 Python 笔记本命名均为 `*-python-agent-framework.ipynb`。

## 要求

- Python 3.12+
  - <strong>注意</strong>：如果你没安装 Python 3.12，请务必安装。然后使用 python3.12 创建虚拟环境，确保从 requirements.txt 文件安装正确版本。
  
    > 示例

    创建 Python 虚拟环境目录：

    ```bash
    python -m venv venv
    ```

    然后激活虚拟环境：

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+：对于使用 .NET 的示例代码，确保安装 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)或更高版本。然后检查已安装的 .NET SDK 版本：

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — 认证所需。安装地址 [aka.ms/installazurecli](https://aka.ms/installazurecli)。
- **Azure 订阅** — 用于访问 Microsoft Foundry 和 Microsoft Foundry Agent Service。
- **Microsoft Foundry 项目** — 具有已部署模型的项目（例如 `gpt-5-mini`）。参见下文[步骤 1](#步骤-1：创建-microsoft-foundry-项目)。

本库根目录包含 `requirements.txt` 文件，列出了运行示例代码所需的所有 Python 包。

你可以在代码库根目录终端运行以下命令安装：

```bash
pip install -r requirements.txt
```

我们建议创建 Python 虚拟环境，以避免冲突和问题。

## 设置 VSCode

确保 VSCode 中使用的是正确的 Python 版本。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 设置 Microsoft Foundry 和 Microsoft Foundry Agent Service

### 步骤 1：创建 Microsoft Foundry 项目

你需要一个 Microsoft Foundry **hub** 和 <strong>项目</strong>，项目中部署了模型以运行笔记本。

1. 访问 [ai.azure.com](https://ai.azure.com) 并使用你的 Azure 账号登录。
2. 创建一个 **hub**（或使用现有的）。参见：[集线器资源概述](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 内创建一个 <strong>项目</strong>。
4. 从 **Models + Endpoints** → **Deploy model** 部署一个模型（例如 `gpt-5-mini`）。

### 步骤 2：获取你的项目端点和模型部署名称

登录 Microsoft Foundry 门户，进入你的项目：

- <strong>项目端点</strong> —— 转到 **Overview** 页面，复制端点 URL。

![Project Connection String](../../../translated_images/zh-CN/project-endpoint.8cf04c9975bbfbf1.webp)

- <strong>模型部署名称</strong> —— 转到 **Models + Endpoints**，选择已部署的模型，记录 **Deployment name**（如 `gpt-5-mini`）。

### 步骤 3：通过 `az login` 登录 Azure

大多数笔记本通过你的 **Azure CLI 登录** 认证 —— 使用 `azure-identity` 包的 `AzureCliCredential` 或 `DefaultAzureCredential`（两者都拾取你的 `az login` 会话） —— 因此它们不需要 API 密钥。一些课程和可选集成使用 API 密钥；请检查各课的前置条件了解是否需要额外环境变量。此步骤要求通过 Azure CLI 登录。

1. **安装 Azure CLI**（如果尚未安装）：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. <strong>登录</strong>，运行：

    ```bash
    az login
    ```

    如果你在无浏览器的远程或 Codespace 环境中：

    ```bash
    az login --use-device-code
    ```

3. **如果提示，选择订阅** —— 选择包含你的 Foundry 项目的订阅。

4. <strong>验证</strong>是否已登录：

    ```bash
    az account show
    ```

> **为何使用 `az login`？** 笔记本使用 `azure-identity` 包的 `AzureCliCredential`（或 `DefaultAzureCredential`，也拾取 Azure CLI 登录）认证。这意味着你的 Azure CLI 会话提供凭据 —— `.env` 文件中无需 API 密钥或机密。这是[安全最佳实践](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

### 步骤 4：创建你的 `.env` 文件

复制示例文件：

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

打开 `.env` 并填写以下两个值：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 变量 | 来源 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 门户 → 你的项目 → **Overview** 页面 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 门户 → **Models + Endpoints** → 已部署的模型名称 |

大多数课程就这样完成！笔记本会自动通过你的 `az login` 会话进行认证。

### 步骤 5：安装 Python 依赖

```bash
pip install -r requirements.txt
```

我们建议在你先前创建的虚拟环境内运行此命令。

## 可选设置：Azure AI Search（第 5 和第 16 课）

第 5 课（Agentic RAG）和第 16 课的笔记本默认使用<strong>内存中知识库</strong> —— 无需额外 Azure 资源。如果想用真实的<strong>Azure AI 搜索</strong>索引支持它们，请注意<strong>第 16 课笔记本当前使用基于密钥的认证</strong>：只有在同时设置了 `AZURE_SEARCH_SERVICE_ENDPOINT` 和 `AZURE_SEARCH_API_KEY` 时，才会从内存搜索切换到 Azure AI 搜索，否则保持内存搜索 —— 因此要连接真实索引，你必须同时设置管理密钥。基于 Microsoft Entra ID（RBAC）的无密钥认证是推荐用于你自己生产代码的方式，与课程中其它部分使用的 `az login` 流一致。

以下 RBAC 步骤适用于本设置指南示例及你自己的代码。但不能使第 16 课笔记本实现无密钥认证；第 16 课仍然需要端点和管理密钥才能使用 Azure AI 搜索。

1. **在你的搜索服务上启用基于角色的访问控制：**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. <strong>为自己分配所需角色</strong>（创建/加载索引和查询权限）：

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **将端点添加到你的 `.env` 文件：**

| 变量 | 来源 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 门户 → 你的 **Azure AI Search** 资源 → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | 必需（搭配端点），启用第 16 课笔记本中的 Azure AI 搜索，使用基于密钥认证。Azure 门户 → <strong>设置</strong> → <strong>密钥</strong> → 主管理密钥 |

> **为何使用无密钥？** 管理密钥授予对搜索服务的完全写入权限，且可能通过 `.env` 文件泄露。通过 RBAC，改用你的 `az login` 身份 —— 即课程笔记本使用的无密钥 Entra ID 模式（通过 `AzureCliCredential` / `DefaultAzureCredential`）。见[使用角色连接 Azure AI 搜索](https://learn.microsoft.com/azure/search/search-security-rbac)。

详情请参见[Azure AI 搜索设置指南](./AzureSearch.md)，内含 Python 与 .NET 的索引创建示例。

## 直接调用 Azure OpenAI 的额外设置（第 6 和第 8 课）

第 6 和第 8 课中的某些笔记本直接调用<strong>Azure OpenAI</strong>（使用 **Responses API**），而非通过 Microsoft Foundry 项目。这些示例以前使用 GitHub Models，现已弃用且不支持 Responses API。请将以下变量添加到你的 `.env` 文件：

| 变量 | 来源 |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure 门户 → 你的 **Azure OpenAI** 资源 → <strong>密钥和端点</strong> → 端点（例如 `https://<your-resource>.openai.azure.com`） |
| `AZURE_OPENAI_DEPLOYMENT` | 你已部署的支持 Responses API 的模型名称（例如 `gpt-5-mini`） |
| `AZURE_OPENAI_API_KEY` | 可选 — 仅在你使用基于密钥认证而非 `az login` / Entra ID 时需要 |

> Responses API 使用稳定的 `/openai/v1/` 端点，无需 `api-version`。请使用 `az login` 登录以实现无密钥 Entra ID 认证。

## 替代提供商：MiniMax（兼容 OpenAI）

[MiniMax](https://platform.minimaxi.com/) 通过兼容 OpenAI 的 API 提供大上下文模型（最大支持 204K 令牌）。由于 Microsoft Agent Framework 的 `OpenAIChatClient` 可与任何兼容 OpenAI 的端点一起使用，你可以将 MiniMax 作为 `OpenAIChatClient` 使用的课程中的替代选项。

将以下变量添加到你的 `.env` 文件：

| 变量 | 来源 |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API 密钥 |
| `MINIMAX_BASE_URL` | 使用 `https://api.minimax.io/v1`（默认值） |
| `MINIMAX_MODEL_ID` | 使用的模型名称（例如 `MiniMax-M3`） |

<strong>示例模型</strong>：`MiniMax-M3`（推荐）、`MiniMax-M2.7`、`MiniMax-M2.7-highspeed`（更快响应）。模型名称和可用性随时间变化，访问权限可能依帐户而异。

使用 `OpenAIChatClient` 的代码示例（如第 14 课酒店预订流程）将在设置了 `MINIMAX_API_KEY` 时自动检测并使用你的 MiniMax 配置。


## 替代提供商：Novita AI（兼容 OpenAI）

[Novita AI](https://novita.ai/llm-api) 提供一个兼容 OpenAI 的 API，支持开源及前沿的 LLM（DeepSeek、Llama、Qwen 等）。由于 Microsoft Agent Framework 的 `OpenAIChatClient` 可与任何兼容 OpenAI 的端点配合使用，您可以将 Novita AI 用作 Azure OpenAI 或 OpenAI 的直接替代方案。

将以下变量添加到您的 `.env` 文件中：

| 变量 | 位置 |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI 控制面板](https://novita.ai/settings/key-management) → API 密钥 |
| `NOVITA_BASE_URL` | 使用 `https://api.novita.ai/openai/v1`（默认值） |
| `NOVITA_MODEL_ID` | 要使用的模型名（例如 `moonshotai/kimi-k3`） |

<strong>示例模型</strong>：`moonshotai/kimi-k3`、`zai-org/glm-5.2`、`deepseek/deepseek-v4-flash-0731`。Novita AI 还托管许多其他开源模型系列（Llama、Qwen、GLM 等）— 请查阅 [Novita AI 模型库](https://novita.ai/llm-api) 获取当前可用模型列表及其模型 ID。

当前示例不会自动使用 `NOVITA_*` 变量。要使用 Novita AI，请在构造您运行的示例中的 `OpenAIChatClient` 时显式传递这些值。

## 替代提供商：Foundry Local（设备上运行模型）

[Foundry Local](https://foundrylocal.ai) 是一个轻量级运行时，能够通过兼容 OpenAI 的 API <strong>完全在您自己的机器上</strong> 下载、管理和服务语言模型— 无需云服务。

由于 Microsoft Agent Framework 的 `OpenAIChatClient` 可用于任何兼容 OpenAI 的端点，Foundry Local 是 Azure OpenAI 的本地直接替代方案。

**1. 安装 Foundry Local**

```bash
# Windows 系统
winget install Microsoft.FoundryLocal

# macOS 系统
brew install foundrylocal
```

**2. 下载并运行模型**（这也会启动本地服务）：

```bash
foundry model list          # 查看可用模型
foundry model run phi-4-mini
```

**3. 安装用于发现本地端点的 Python SDK：**

```bash
pip install foundry-local-sdk
```

**4. 指向 Microsoft Agent Framework 使用您的本地模型：**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 下载（如果需要）并在本地提供模型，然后发现端点/端口。
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # 例如 http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local始终为“not-required”
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **注意：** Foundry Local 暴露了一个兼容 OpenAI 的 <strong>聊天补全</strong> 端点，适合本地开发和离线场景。完整的 **响应 API** 功能集（包含有状态对话等）请使用 Azure OpenAI 或 Microsoft Foundry 项目。

## 课时8 额外设置（Bing 绑定工作流）

课时8的条件工作流笔记本通过 Microsoft Foundry 使用 **Bing 绑定**。如果您计划运行该示例，请将此变量添加到您的 `.env` 文件中：

| 变量 | 位置 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry 门户 → 您的项目 → <strong>管理</strong> → <strong>已连接资源</strong> → 您的 Bing 连接 → 复制连接 ID |

## 故障排除

### macOS 上的 SSL 证书验证错误

如果您在 macOS 上遇到类似错误：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

这是 macOS 上 Python 的已知问题，系统 SSL 证书未自动信任。请按顺序尝试以下解决方案：

**选项1：运行 Python 的安装证书脚本（推荐）**

```bash
# 将 3.XX 替换为你安装的 Python 版本（例如，3.12 或 3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**选项2：在您的笔记本中使用 `connection_verify=False`（仅适用于 GitHub Models 笔记本）**

在第6课的笔记本（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）中，已经包含了注释掉的解决方法。遇到证书错误时取消注释 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如果遇到证书错误，请禁用 SSL 验证
)
```

> **⚠️ 警告：** 禁用 SSL 验证 (`connection_verify=False`) 会跳过证书验证，从而降低安全性。仅在开发环境作为临时解决方案使用，切勿在生产环境中使用。

**选项3：安装并使用 `truststore`**

```bash
pip install truststore
```

然后在您的笔记本或脚本顶部调用网络请求前添加以下内容：

```python
import truststore
truststore.inject_into_ssl()
```

## 卡住了？

如果您在运行此设置时遇到任何问题，请加入我们的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社区 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">提交问题</a>。

## 下一课

您现在已准备好运行本课程的代码。祝您在 AI 代理世界中学习愉快！

[AI 代理介绍及应用场景](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->