# 课程设置

## 介绍

本课将介绍如何运行本课程的代码示例。

## 加入其他学习者并获取帮助

在开始克隆你的仓库之前，加入 [AI Agents For Beginners Discord 频道](https://aka.ms/ai-agents/discord) 以获取任何设置方面的帮助、有关课程的任何问题，或与其他学习者建立联系。

## 克隆或派生此仓库

首先，请克隆或派生该 GitHub 仓库。这将创建你自己的课程材料副本，以便你可以运行、测试和调整代码！

这可以通过单击链接来完成 <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">派生此仓库</a>

你现在应该在以下链接中拥有此课程的你自己的派生版本：

![已派生的仓库](../../../translated_images/zh-CN/forked-repo.33f27ca1901baa6a.webp)

### 浅克隆（建议用于研讨会 / Codespaces）

  >整个仓库在下载完整历史记录和所有文件时可能很大（约 ~3 GB）。如果你只参加研讨会或只需要几个课程文件夹，浅克隆（或稀疏克隆）通过截断历史记录和/或跳过 blob 来避免大部分下载。

#### 快速浅克隆 — 最少历史，所有文件

将下面命令中的 `<your-username>` 替换为你的派生 URL（或如果你愿意则使用上游 URL）。

要仅克隆最新提交历史（小下载）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

要克隆特定分支：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（稀疏）克隆 — 最少 blob + 仅选定文件夹

此方法使用部分克隆和 sparse-checkout（需要 Git 2.25+，并建议使用支持部分克隆的现代 Git）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

进入仓库文件夹：

```bash|powershell
cd ai-agents-for-beginners
```

然后指定你想要的文件夹（下面示例显示两个文件夹）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

克隆并验证文件后，如果你只需要文件并想释放空间（无 git 历史），请删除仓库元数据（💀不可逆 — 你将失去所有 Git 功能：无法提交、拉取、推送或访问历史记录）。

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（建议以避免本地大规模下载）

- 通过 [GitHub UI](https://github.com/codespaces) 为此仓库创建一个新的 Codespace。  

- 在新创建的 Codespace 的终端中，运行上面的浅克隆/稀疏克隆命令之一，只将你需要的课程文件夹带入 Codespace 工作区。
- 可选：在 Codespaces 内克隆后，删除 .git 以回收额外空间（见上面的删除命令）。
- 注意：如果你更愿意直接在 Codespaces 中打开仓库（而不额外克隆），请注意 Codespaces 会构建 devcontainer 环境，可能仍会提供超过你所需的内容。在全新的 Codespace 内克隆浅副本可以让你更好地控制磁盘使用。

#### 小贴士

- 如果你想编辑/提交，始终将克隆 URL 替换为你的派生仓库。
- 如果你以后需要更多历史或文件，可以获取它们或调整 sparse-checkout 以包含其他文件夹。

## 运行代码

本课程提供了一系列 Jupyter Notebook，让你通过动手实践来构建 AI 代理并运行它们。

代码示例使用 **Microsoft Agent Framework (MAF)** 与 `AzureAIProjectAgentProvider`，它通过 **Microsoft Foundry** 连接到 **Azure AI Agent Service V2**（Responses API）。

所有 Python 笔记本均标记为 `*-python-agent-framework.ipynb`。

## 要求

- Python 3.12+
  - **注意**：如果你没有安装 Python3.12，请确保安装它。然后使用 python3.12 创建你的虚拟环境，以确保从 requirements.txt 文件安装正确的版本。
  
    >示例

    创建 Python 虚拟环境目录：

    ```bash|powershell
    python -m venv venv
    ```

    然后激活虚拟环境以便：

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: 对于使用 .NET 的示例代码，请确保安装 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本。然后，检查你已安装的 .NET SDK 版本：

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 需要用于身份验证。请从 [aka.ms/installazurecli](https://aka.ms/installazurecli) 安装。
- **Azure 订阅** — 用于访问 Microsoft Foundry 和 Azure AI Agent Service。
- **Microsoft Foundry 项目** — 一个部署了模型的项目（例如 `gpt-4o`）。见下面的 [步骤 1](../../../00-course-setup)。

我们在此仓库根目录中包含了一个 `requirements.txt` 文件，其中包含运行代码示例所需的所有 Python 包。

你可以在仓库根目录的终端中运行以下命令来安装它们：

```bash|powershell
pip install -r requirements.txt
```

我们建议创建 Python 虚拟环境以避免任何冲突和问题。

## 设置 VSCode

确保在 VSCode 中使用正确版本的 Python。

![图片](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 设置 Microsoft Foundry 和 Azure AI Agent Service

### 步骤 1：创建 Microsoft Foundry 项目

你需要一个 Azure AI Foundry 的 **hub** 和带有已部署模型的 **project** 才能运行笔记本。

1. 转到 [ai.azure.com](https://ai.azure.com) 并使用你的 Azure 帐户登录。
2. 创建一个 **hub**（或使用现有的）。参见：[Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)。
3. 在 hub 内创建一个 **project**。
4. 从 **Models + Endpoints** → **Deploy model** 部署一个模型（例如 `gpt-4o`）。

### 步骤 2：检索你的项目端点和模型部署名称

在 Microsoft Foundry 门户中的你的项目：

- **Project Endpoint** — 转到 **Overview** 页面并复制端点 URL。

![项目连接字符串](../../../translated_images/zh-CN/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — 转到 **Models + Endpoints**，选择你部署的模型，并记下 **Deployment name**（例如 `gpt-4o`）。

### 步骤 3：使用 `az login` 登录 Azure

所有笔记本都使用 **`AzureCliCredential`** 进行身份验证 — 无需管理 API 密钥。这要求你通过 Azure CLI 登录。

1. 如果尚未安装 **Azure CLI**，请安装： [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 通过运行以下命令 **登录**：

    ```bash|powershell
    az login
    ```

    或者，如果你在没有浏览器的远程/Codespace 环境中：

    ```bash|powershell
    az login --use-device-code
    ```

3. 如果提示，请 **选择订阅** — 选择包含你的 Foundry 项目的订阅。

4. **验证** 你已登录：

    ```bash|powershell
    az account show
    ```

> **为什么使用 `az login`？** 笔记本使用 `azure-identity` 包中的 `AzureCliCredential` 进行身份验证。这意味着你的 Azure CLI 会话提供凭据 — 无需在 `.env` 文件中存放 API 密钥或机密。这是一个 [安全最佳实践](https://learn.microsoft.com/azure/developer/ai/keyless-connections)。

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

打开 `.env` 并填写这两个值：

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

对于大多数课程就到这里为止！笔记本会通过你的 `az login` 会话自动进行身份验证。

### 步骤 5：安装 Python 依赖项

```bash|powershell
pip install -r requirements.txt
```

我们建议在你之前创建的虚拟环境中运行此命令。

## 课程 5（Agentic RAG）的附加设置

课程 5 使用 **Azure AI Search** 进行检索增强生成（RAG）。如果你计划运行该课程，请将这些变量添加到你的 `.env` 文件中：

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## 课程 6 和 课程 8（GitHub Models）的附加设置

第 6 课和第 8 课中的一些笔记本使用 **GitHub Models** 而不是 Azure AI Foundry。如果你计划运行这些示例，请将这些变量添加到你的 `.env` 文件中：

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## 课程 8（Bing Grounding 工作流）的附加设置

第 8 课中的条件工作流笔记本使用通过 Azure AI Foundry 的 **Bing grounding**。如果你计划运行该示例，请将此变量添加到你的 `.env` 文件中：

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## 故障排除

### macOS 上的 SSL 证书验证错误

如果你在 macOS 上遇到如下错误：

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

这是 Python 在 macOS 上的已知问题，系统 SSL 证书未自动被信任。请按顺序尝试以下解决方案：

**选项 1：运行 Python 的安装证书脚本（推荐）**

```bash
# 将 3.XX 替换为你已安装的 Python 版本（例如 3.12 或 3.13）：
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**选项 2：在你的笔记本中使用 `connection_verify=False`（仅适用于 GitHub Models 的笔记本）**

在 Lesson 6 笔记本（`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`）中，已经包含了一个被注释掉的解决方法。在创建客户端时取消注释 `connection_verify=False`：

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 如果遇到证书错误，请禁用 SSL 验证
)
```

> **⚠️ 警告：** 禁用 SSL 验证（`connection_verify=False`）通过跳过证书验证来降低安全性。仅在开发环境中作为临时解决方法使用，切勿在生产环境中使用。

**选项 3：安装并使用 `truststore`**

```bash
pip install truststore
```

然后在笔记本或脚本顶部在进行任何网络调用之前添加以下内容：

```python
import truststore
truststore.inject_into_ssl()
```

## 遇到困难？

如果你在运行此设置时遇到任何问题，请加入我们的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社区 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">创建一个 issue</a>。

## 下一课

你现在已经准备好运行本课程的代码。祝你在 AI 代理的世界中学习愉快！

[AI 代理简介和代理用例](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免责声明：
本文件已使用人工智能翻译服务 Co‑op Translator（https://github.com/Azure/co-op-translator）进行翻译。我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文档的原文应被视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或曲解，我们不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->