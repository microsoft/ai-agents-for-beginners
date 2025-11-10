<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86273689a010b5efecaf7fa23104e0fb",
  "translation_date": "2025-11-07T08:26:09+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "zh"
}
-->
# 课程设置

## 简介

本课程将介绍如何运行课程中的代码示例。

## 加入其他学习者并获得帮助

在开始克隆您的代码库之前，请加入 [AI Agents For Beginners Discord 频道](https://aka.ms/ai-agents/discord)，以获得设置帮助、课程相关问题解答或与其他学习者交流。

## 克隆或分叉此代码库

首先，请克隆或分叉 GitHub 代码库。这将创建您自己的课程材料版本，以便您可以运行、测试和调整代码！

您可以通过点击以下链接来 <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">分叉代码库</a>。

现在，您应该在以下链接中拥有课程的分叉版本：

![分叉代码库](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.zh.png)

### 浅克隆（推荐用于工作坊 / Codespaces）

  >完整的代码库可能较大（约 3 GB），当您下载完整历史记录和所有文件时。如果您仅参加工作坊或只需要几个课程文件夹，浅克隆（或稀疏克隆）可以通过截断历史记录和/或跳过文件来避免大部分下载。

#### 快速浅克隆——最小历史记录，所有文件

在以下命令中将 `<your-username>` 替换为您的分叉 URL（或您偏好的上游 URL）。

仅克隆最新提交历史记录（下载量较小）：

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

克隆特定分支：

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 部分（稀疏）克隆——最小文件 + 仅选定文件夹

此方法使用部分克隆和稀疏检出（需要 Git 2.25+，推荐支持部分克隆的现代 Git）：

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

进入代码库文件夹：

```bash|powershell
cd ai-agents-for-beginners
```

然后指定您需要的文件夹（以下示例显示两个文件夹）：

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

在克隆并验证文件后，如果您只需要文件并希望释放空间（无 Git 历史记录），请删除代码库元数据（💀不可逆——您将失去所有 Git 功能：无法提交、拉取、推送或访问历史记录）。

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### 使用 GitHub Codespaces（推荐避免本地大文件下载）

- 通过 [GitHub UI](https://github.com/codespaces) 为此代码库创建一个新的 Codespace。

- 在新创建的 Codespace 的终端中，运行上述浅克隆/稀疏克隆命令，将您需要的课程文件夹带入 Codespace 工作区。
- 可选：在 Codespaces 中克隆后，移除 .git 以释放额外空间（参见上述删除命令）。
- 注意：如果您更喜欢直接在 Codespaces 中打开代码库（无需额外克隆），请注意 Codespaces 将构建开发容器环境，可能仍会配置超出您需要的内容。在新的 Codespace 中克隆浅拷贝可以更好地控制磁盘使用。

#### 提示

- 如果您想编辑/提交，请始终替换克隆 URL 为您的分叉。
- 如果您之后需要更多历史记录或文件，可以获取它们或调整稀疏检出以包含其他文件夹。

## 运行代码

本课程提供了一系列 Jupyter Notebooks，您可以通过它们亲身体验构建 AI Agents。

代码示例使用以下选项：

**需要 GitHub 账户 - 免费**：

1) Semantic Kernel Agent Framework + GitHub Models Marketplace。标记为 (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace。标记为 (autogen.ipynb)

**需要 Azure 订阅**：
3) Azure AI Foundry + Azure AI Agent Service。标记为 (azureaiagent.ipynb)

我们鼓励您尝试所有三种示例，看看哪种最适合您。

无论您选择哪种选项，都将决定您需要遵循的设置步骤：

## 要求

- Python 3.12+
  - **注意**：如果您尚未安装 Python3.12，请确保安装它。然后使用 python3.12 创建您的虚拟环境，以确保从 requirements.txt 文件中安装正确的版本。
  
    >示例

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

- .NET 10+：对于使用 .NET 的示例代码，请确保安装 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本。然后检查您安装的 .NET SDK 版本：

    ```bash|powershell
    dotnet --list-sdks
    ```

- 一个 GitHub 账户 - 用于访问 GitHub Models Marketplace
- Azure 订阅 - 用于访问 Azure AI Foundry
- Azure AI Foundry 账户 - 用于访问 Azure AI Agent Service

我们在代码库的根目录中包含了一个 `requirements.txt` 文件，其中包含运行代码示例所需的所有 Python 包。

您可以在代码库根目录的终端中运行以下命令来安装它们：

```bash|powershell
pip install -r requirements.txt
```

我们建议创建一个 Python 虚拟环境以避免任何冲突和问题。

## 设置 VSCode

确保您在 VSCode 中使用正确版本的 Python。

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## 使用 GitHub 模型的示例设置

### 第一步：获取您的 GitHub 个人访问令牌 (PAT)

本课程利用 GitHub Models Marketplace，提供免费访问大型语言模型 (LLMs)，您将使用它们来构建 AI Agents。

要使用 GitHub 模型，您需要创建一个 [GitHub 个人访问令牌](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)。

您可以通过访问您的 <a href="https://github.com/settings/personal-access-tokens" target="_blank">个人访问令牌设置</a> 来完成此操作。

请遵循 [最小权限原则](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) 创建令牌。这意味着您应该仅赋予令牌运行本课程代码示例所需的权限。

1. 在屏幕左侧的 **开发者设置** 中选择 `精细化令牌` 选项。

   ![开发者设置](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.zh.png)

   然后选择 `生成新令牌`。

   ![生成令牌](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.zh.png)

2. 输入一个描述性名称以反映令牌的用途，使其以后易于识别。

    🔐 令牌有效期建议

    推荐有效期：30 天
    为了更安全，可以选择更短的时间——例如 7 天 🛡️
    这是一个很好的方式来设定个人目标并在学习动力高涨时完成课程 🚀。

    ![令牌名称和有效期](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.zh.png)

3. 将令牌的范围限制为此代码库的分叉。

    ![限制范围到分叉代码库](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.zh.png)

4. 限制令牌的权限：在 **权限** 下，点击 **账户** 标签，然后点击 "+ 添加权限" 按钮。会出现一个下拉菜单。请搜索 **模型** 并勾选它。

    ![添加模型权限](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.zh.png)

5. 在生成令牌之前验证所需权限。![验证权限](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.zh.png)

6. 在生成令牌之前，请确保您准备好将令牌存储在安全的地方，例如密码管理器，因为生成后不会再次显示。![安全存储令牌](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.zh.png)

复制您刚刚创建的新令牌。现在，您需要将其添加到本课程包含的 `.env` 文件中。

### 第二步：创建您的 `.env` 文件

在终端中运行以下命令以创建 `.env` 文件。

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

这将复制示例文件并在您的目录中创建 `.env` 文件，您需要在其中填写环境变量的值。

复制令牌后，使用您喜欢的文本编辑器打开 `.env` 文件，并将令牌粘贴到 `GITHUB_TOKEN` 字段中。

![GitHub 令牌字段](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.zh.png)

现在，您应该可以运行本课程的代码示例。

## 使用 Azure AI Foundry 和 Azure AI Agent Service 的示例设置

### 第一步：获取您的 Azure 项目端点

按照以下步骤在 Azure AI Foundry 中创建一个中心和项目：[中心资源概述](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)

创建项目后，您需要获取项目的连接字符串。

您可以通过访问 Azure AI Foundry 门户中项目的 **概述** 页面来完成此操作。

![项目连接字符串](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.zh.png)

### 第二步：创建您的 `.env` 文件

在终端中运行以下命令以创建 `.env` 文件。

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

这将复制示例文件并在您的目录中创建 `.env` 文件，您需要在其中填写环境变量的值。

复制令牌后，使用您喜欢的文本编辑器打开 `.env` 文件，并将令牌粘贴到 `PROJECT_ENDPOINT` 字段中。

### 第三步：登录 Azure

作为安全最佳实践，我们将使用 [无密钥认证](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) 来通过 Microsoft Entra ID 认证到 Azure OpenAI。

接下来，打开终端并运行 `az login --use-device-code` 登录到您的 Azure 账户。

登录后，在终端中选择您的订阅。

## 额外环境变量 - Azure Search 和 Azure OpenAI 

对于 Agentic RAG 课程 - 第五课 - 有使用 Azure Search 和 Azure OpenAI 的示例。

如果您想运行这些示例，您需要在 `.env` 文件中添加以下环境变量：

### 概述页面（项目）

- `AZURE_SUBSCRIPTION_ID` - 在项目的 **概述** 页面中检查 **项目详情**。

- `AZURE_AI_PROJECT_NAME` - 查看项目 **概述** 页顶部。

- `AZURE_OPENAI_SERVICE` - 在 **概述** 页的 **包含的功能** 标签中找到 **Azure OpenAI 服务**。

### 管理中心

- `AZURE_OPENAI_RESOURCE_GROUP` - 在 **管理中心** 的 **概述** 页中访问 **项目属性**。

- `GLOBAL_LLM_SERVICE` - 在 **连接的资源** 下找到 **Azure AI 服务** 的连接名称。如果未列出，请检查 **Azure 门户** 中资源组下的 AI 服务资源名称。

### 模型 + 端点页面

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 选择您的嵌入模型（例如 `text-embedding-ada-002`），并从模型详情中记录 **部署名称**。

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - 选择您的聊天模型（例如 `gpt-4o-mini`），并从模型详情中记录 **部署名称**。

### Azure 门户

- `AZURE_OPENAI_ENDPOINT` - 查找 **Azure AI 服务**，点击它，然后转到 **资源管理**，**密钥和端点**，向下滚动到 "Azure OpenAI 端点"，复制标记为 "语言 API" 的端点。

- `AZURE_OPENAI_API_KEY` - 从同一屏幕复制密钥 1 或密钥 2。

- `AZURE_SEARCH_SERVICE_ENDPOINT` - 找到您的 **Azure AI 搜索** 资源，点击它，然后查看 **概述**。

- `AZURE_SEARCH_API_KEY` - 然后转到 **设置** 和 **密钥**，复制主或次级管理员密钥。

### 外部网页

- `AZURE_OPENAI_API_VERSION` - 访问 [API 版本生命周期](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) 页面下的 **最新 GA API 发布**。

### 设置无密钥认证

我们将使用无密钥连接到 Azure OpenAI，而不是硬编码您的凭据。为此，我们将导入 `DefaultAzureCredential`，稍后调用 `DefaultAzureCredential` 函数以获取凭据。

```python
# Python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## 遇到问题？
如果您在运行此设置时遇到任何问题，可以加入我们的 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 社区 Discord</a> 或 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">创建一个问题</a>。

## 下一课

您现在已经准备好运行本课程的代码了。祝您愉快地学习更多关于 AI 代理的知识！

[AI代理简介及应用场景](../01-intro-to-ai-agents/README.md)

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。