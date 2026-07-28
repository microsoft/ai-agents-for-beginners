# 课程设置

## 介绍

本课将介绍如何运行本课程的代码示例。

## 加入其他学习者并获取帮助

在开始克隆您的仓库之前，请加入[AI Agents For Beginners Discord频道](https://aka.ms/ai-agents/discord)，以便获取设置帮助、课程问题解答，或与其他学习者连接。

## 克隆或 Fork 本仓库

首先，请克隆或 Fork GitHub 仓库。这样您就拥有了课程材料的个人版本，可以运行、测试和修改代码！

您可以点击链接来 <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">Fork 仓库</a>

现在您应该拥有了本课程的个人分叉版本，链接如下：

![Forked Repo](../../../translated_images/zh-CN/forked-repo.33f27ca1901baa6a.webp)

### 浅克隆（推荐用于工作坊 / Codespaces）

  >下载完整历史和所有文件时，完整仓库可能很大（约3 GB）。如果您只是参加工作坊或只需要几个课程文件夹，浅克隆（或稀疏克隆）通过截断历史和/或跳过大文件避免了大部分下载。

#### 快速浅克隆 — 最少历史，所有文件

将以下命令中的 `<your-username>` 替换为您的 Fork URL（或如果您喜欢，则使用上游 URL）。

只克隆最新提交历史（下载量小）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

克隆指定分支：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分克隆（稀疏克隆）— 最少大文件 + 只选定文件夹

该方法使用部分克隆和稀疏检出（需要 Git 2.25+，推荐现代 Git 支持部分克隆）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

进入仓库文件夹：

```bash|powershell
cd ai-agents-for-beginners
```

然后指定你需要的文件夹（以下示例显示两个文件夹）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

克隆并验证文件后，如果您只需要文件并想释放空间（无 git 历史），请删除仓库元数据（💀不可逆 — 会丢失所有 Git 功能：无提交、拉取、推送或历史访问）。

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（推荐避免本地大文件下载）

- 通过 [GitHub UI](https://github.com/codespaces) 为此仓库创建新的 Codespace。  

- 在新建 Codespace 的终端中运行上述浅克隆或稀疏克隆命令，仅将您需要的课程文件夹带入 Codespace 工作区。
- 可选：在 Codespaces 内克隆后，删除 .git 以回收额外空间（见上方删除命令）。
- 注意：如果您更愿意直接在 Codespaces 打开仓库（无额外克隆），请注意 Codespaces 会构建 devcontainer 环境，可能仍会配置超出需求的内容。在新 Codespace 内克隆浅拷贝可更好控制磁盘使用。

#### 小贴士

- 如果您希望编辑/提交，请始终替换为您 Fork 的克隆 URL。
- 以后如果需要更多历史或文件，可以抓取或调整稀疏检出以包含额外文件夹。

## 运行代码

本课程提供一系列可运行的 Jupyter Notebook，让您亲自动手构建 AI 代理。

代码示例使用<strong>微软代理框架（Microsoft Agent Framework，MAF）</strong>及 `FoundryChatClient`，通过<strong>Microsoft Foundry</strong>连接<strong>Microsoft Foundry Agent Service V2</strong>（Responses API）。

所有 Python 笔记本均标记为 `*-python-agent-framework.ipynb`。

## 要求

- Python 3.12+
  - <strong>注意</strong>：如果未安装 Python 3.12，请确保安装。然后使用 python3.12 创建虚拟环境，确保从 requirements.txt 文件安装正确版本。
  
    >例如

    创建 Python 虚拟环境目录：

    ```bash|powershell
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

- .NET 10+：对于使用 .NET 的示例代码，请确保安装 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本。然后检查已安装的 .NET SDK 版本：

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 必需的身份验证工具。安装请访问 [aka.ms/installazurecli](https://aka.ms/installazurecli)。
- **Azure 订阅** — 访问 Microsoft Foundry 和 Microsoft Foundry Agent Service 所需。
- **Microsoft Foundry 项目** — 需已部署模型的项目（示例：`gpt-5-mini`）。见下方[步骤1](#步骤1：创建-microsoft-foundry-项目)。

仓库根目录包含 `requirements.txt` 文件，列出了运行示例代码所需的所有 Python 包。

您可以在终端的仓库根目录运行以下命令安装：

```bash|powershell
pip install -r requirements.txt
```

推荐创建 Python 虚拟环境以避免冲突和问题。

## 设置 VSCode

确保 VSCode 使用的是正确版本的 Python。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 设置 Microsoft Foundry 和 Microsoft Foundry Agent Service

### 步骤1：创建 Microsoft Foundry 项目

您需要一个 Microsoft Foundry **hub** 和带已部署模型的 **project** 才能运行笔记本。

1. 访问 [ai.azure.com](https://ai.azure.com)，使用 Azure 账号登录。
2. 创建一个 **hub**（或使用已有的）。详情见：[Hub资源概述](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 内创建一个 **project**。
4. 在 **Models + Endpoints** → **Deploy model** 部署模型（例如 `gpt-5-mini`）。

### 步骤2：获取项目端点和模型部署名称

从 Microsoft Foundry 门户项目里：

- <strong>项目端点</strong> — 进入 **Overview** 页面，复制端点 URL。

![Project Connection String](../../../translated_images/zh-CN/project-endpoint.8cf04c9975bbfbf1.webp)

- <strong>模型部署名称</strong> — 前往 **Models + Endpoints**，选择已部署模型，记录 **Deployment name**（如 `gpt-5-mini`）。

### 步骤3：通过 `az login` 登录 Azure

所有笔记本使用 **`AzureCliCredential`** 认证 — 无需管理 API 密钥。需要通过 Azure CLI 登录。

1. 如果尚未安装 Azure CLI，请安装：[aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 运行以下命令登录：

    ```bash|powershell
    az login
    ```

    若在无浏览器的远程/Codespace 环境：

    ```bash|powershell
    az login --use-device-code
    ```

3. 若提示，<strong>选择订阅</strong> — 选择包含 Foundry 项目的订阅。

4. <strong>验证登录状态</strong>：

    ```bash|powershell
    az account show
    ```

> **为何使用 `az login`？** 笔记本通过 `azure-identity` 包里的 `AzureCliCredential` 进行认证。这意味着 Azure CLI 会话提供凭据 — 不需在 `.env` 文件中保存 API 密钥或秘密。此为一项[安全最佳实践](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

### 步骤4：创建 `.env` 文件

复制示例文件：

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

打开 `.env` 文件，填写以下两个变量：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 变量 | 位置 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 门户 → 项目 → **Overview** 页 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 门户 → **Models + Endpoints** → 已部署模型名称 |

以上为大多数课程的全部配置！笔记本会通过您的 `az login` 会话自动认证。

### 步骤5：安装 Python 依赖

```bash|powershell
pip install -r requirements.txt
```

建议在之前创建的虚拟环境中运行该命令。

## 课程5（Agentic RAG）额外设置

课程5 使用 **Azure AI Search** 支持检索增强生成。若您计划运行该课程，请在 `.env` 文件添加以下变量：

| 变量 | 位置 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 门户 → 您的 **Azure AI Search** 资源 → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure 门户 → 您的 **Azure AI Search** 资源 → <strong>设置</strong> → <strong>密钥</strong> → 主管理员密钥 |

## 直接调用 Azure OpenAI 的额外设置（课程6和8）

课程6和8中的部分笔记本直接调用 **Azure OpenAI**（使用 **Responses API**），而非通过 Microsoft Foundry 项目。之前这些示例使用 GitHub Models，现已弃用（将于2026年7月退役）且不支持 Responses API。若计划运行这些示例，请将以下变量添加到 `.env` 文件：

| 变量 | 位置 |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure 门户 → 您的 **Azure OpenAI** 资源 → <strong>密钥和端点</strong> → 端点（例如 `https://<your-resource>.openai.azure.com`） |
| `AZURE_OPENAI_DEPLOYMENT` | 已部署且支持 Responses API 的模型名称（例如 `gpt-5-mini`） |
| `AZURE_OPENAI_API_KEY` | 可选 — 如果您使用基于密钥的认证而非 `az login` / Entra ID 时填写 |

> Responses API 使用稳定的 `/openai/v1/` 端点，不需要 `api-version`。登录 `az login` 以使用无密钥的 Entra ID 认证。

## 替代提供者：MiniMax（兼容 OpenAI）

[MiniMax](https://platform.minimaxi.com/) 通过兼容 OpenAI 的 API 提供大上下文模型（最高支持204K token）。微软代理框架的 `OpenAIChatClient` 兼容所有 OpenAI 端点，您可将 MiniMax 作为 Azure OpenAI 或 OpenAI 的替代方案。

将以下变量添加到 `.env` 文件：

| 变量 | 位置 |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax 平台](https://platform.minimaxi.com/) → API 密钥 |
| `MINIMAX_BASE_URL` | 使用 `https://api.minimax.io/v1`（默认） |
| `MINIMAX_MODEL_ID` | 使用的模型名称（例如 `MiniMax-M3`） |

<strong>示例模型</strong>：`MiniMax-M3`（推荐），`MiniMax-M2.7`，`MiniMax-M2.7-highspeed`（响应更快）。模型名称和可用性会随时变动，访问权限取决于账户或地区 — 请查看[MiniMax 平台](https://platform.minimaxi.com/)获取最新列表。如果 `MiniMax-M3` 不对账户开放，请设置 `MINIMAX_MODEL_ID` 为您可用的模型（例如 `MiniMax-M2.7`）。

使用 `OpenAIChatClient` 的代码示例（例如第14课酒店预订流程）在设置了 `MINIMAX_API_KEY` 时会自动检测并使用您的 MiniMax 配置。

## 替代提供者：Foundry Local（本地运行模型）

[Foundry Local](https://foundrylocal.ai) 是轻量级运行时，可完全在您本机下载、管理并提供语言模型的 OpenAI 兼容 API — 无需云服务，无需 Azure 订阅，也无需 API 密钥。非常适合离线开发、实验和避免云端费用，或将数据保留在本地。

由于微软代理框架的 `OpenAIChatClient` 兼容任何 OpenAI 端点，Foundry Local 是 Azure OpenAI 的本地替代方案。

**1. 安装 Foundry Local**

```bash
# Windows（视窗操作系统）
winget install Microsoft.FoundryLocal

# macOS（苹果操作系统）
brew install foundrylocal
```

**2. 下载并运行模型**（同时启动本地服务）：

```bash
foundry model list          # 查看可用模型
foundry model run phi-4-mini
```

**3. 安装 Python SDK**，用于发现本地端点：

```bash
pip install foundry-local-sdk
```

**4. 将微软代理框架指向您的本地模型：**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 下载（如果需要）并在本地提供模型服务，然后发现端点/端口。
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # 例如 http://localhost:<port>/v1
    api_key=manager.api_key,        # 对于 Foundry Local 始终为“not-required”
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **注意：** Foundry Local 暴露 OpenAI 兼容的<strong>聊天完成</strong>端点，适用于本地开发和离线场景。若需完整的<strong>Responses API</strong>功能（支持有状态对话、深度工具编排及代理式开发），请使用本文示例中的 **Azure OpenAI** 或 **Microsoft Foundry** 项目。详见[Foundry Local 文档](https://foundrylocal.ai)了解当前模型目录及平台支持。

## 课程8（Bing 依托工作流）额外设置


第8课中的条件工作流笔记本使用了通过 Microsoft Foundry 实现的 **Bing 覆盖**。如果你打算运行该示例，请将此变量添加到你的 `.env` 文件中：

| 变量 | 获取位置 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry 门户 → 你的项目 → <strong>管理</strong> → <strong>已连接资源</strong> → 你的 Bing 连接 → 复制连接 ID |

## 故障排除

### macOS 上的 SSL 证书验证错误

如果你使用 macOS 并遇到如下错误：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

这是 macOS 上 Python 的已知问题，系统 SSL 证书不会被自动信任。请按顺序尝试以下解决方案：

**选项 1：运行 Python 的安装证书脚本（推荐）**

```bash
# 将3.XX替换为您安装的Python版本（例如，3.12或3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**选项 2：在笔记本中使用 `connection_verify=False`（仅适用于 GitHub Models 笔记本）**

在第 6 课的笔记本（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）中，已包含了一个注释掉的解决方法。创建客户端时取消注释 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如果遇到证书错误，请禁用SSL验证
)
```

> **⚠️ 警告：** 禁用 SSL 验证 (`connection_verify=False`) 会跳过证书验证，从而降低安全性。仅在开发环境做为临时解决方案使用，绝不可在生产环境中使用。

**选项 3：安装并使用 `truststore`**

```bash
pip install truststore
```

然后在笔记本或脚本的顶部网络调用之前添加以下内容：

```python
import truststore
truststore.inject_into_ssl()
```

## 卡住了吗？

如果你在运行此设置时遇到任何问题，请加入我们的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社区 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">创建一个问题</a>。

## 下一课

你现在已准备好运行本课程的代码。祝你在 AI 代理的世界中学习愉快！

[AI 代理简介及代理用例](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->