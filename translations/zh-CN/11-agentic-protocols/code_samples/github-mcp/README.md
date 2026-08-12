# Github MCP 服务器示例

## 描述

这是为通过 Microsoft Reactor 举办的 AI Agents Hackathon 创建的演示。

该工具用于根据用户的 Github 仓库推荐黑客马拉松项目。  
实现方式如下：

1. **Github Agent** - 使用 Github MCP 服务器检索仓库及其信息。  
2. **Hackathon Agent** - 获取来自 Github Agent 的数据，并基于项目、用户使用的语言以及 AI Agents 黑客马拉松的项目赛道提出有创意的黑客马拉松项目想法。  
3. **Events Agent** - 根据 Hackathon Agent 的建议，Events Agent 将推荐来自 AI Agent Hackathon 系列的相关活动。  

## 运行代码 

### 环境变量

此演示使用 Microsoft Agent Framework、Azure OpenAI Service、Github MCP Server 和 Azure AI Search。

请确保已设置正确的环境变量以使用这些工具：

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## 运行 Chainlit 服务器

要连接到 MCP 服务器，此演示使用 Chainlit 作为聊天界面。 

要运行服务器，请在终端中使用以下命令：

```bash
chainlit run app.py -w
```

这应该会在 `localhost:8000` 上启动你的 Chainlit 服务器，并将 `event-descriptions.md` 的内容填充到你的 Azure AI Search 索引中。 

## 连接到 MCP 服务器

要连接到 Github MCP 服务器，选择位于聊天框 "Type your message here.." 下方的 "plug" 图标：

![MCP 连接](../../../../../translated_images/zh-CN/mcp-chainlit-1.7ed66d648e3cfb28.webp)

在那里，你可以点击 "Connect an MCP" 来添加连接到 Github MCP 服务器的命令：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

将 "[YOUR PERSONAL ACCESS TOKEN]" 替换为你的实际个人访问令牌。 

连接后，你应该会在 plug 图标旁看到一个 (1) 来确认它已连接。如果没有，请尝试使用 `chainlit run app.py -w` 重启 chainlit 服务器。

## 使用演示 

要开始推荐黑客马拉松项目的代理工作流程，你可以输入如下消息： 

"为 Github 用户 koreyspace 推荐黑客马拉松项目"

Router Agent 将分析你的请求并确定哪种代理组合（GitHub、Hackathon 和 Events）最适合处理你的查询。各代理协同工作，根据 GitHub 仓库分析、项目构思和相关技术活动提供全面的推荐。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免责声明：
本文件由 AI 翻译服务 Co-op Translator (https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原文应被视为权威来源。对于重要信息，建议采用专业的人工翻译。因使用本翻译而产生的任何误解或误读，我们不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->