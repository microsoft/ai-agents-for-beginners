<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-05-21T09:28:07+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "zh"
}
-->
# Lesson 11: Model Context Protocol (MCP) 集成

## Model Context Protocol (MCP) 简介

Model Context Protocol（MCP）是一种先进的框架，旨在标准化 AI 模型与客户端应用之间的交互。MCP 作为 AI 模型与应用之间的桥梁，提供了一致的接口，无论底层模型实现如何。

MCP 的关键特点：

- **标准化通信**：MCP 建立了应用与 AI 模型之间的通用语言
- **增强的上下文管理**：支持高效传递上下文信息给 AI 模型
- **跨平台兼容**：支持包括 C#、Java、JavaScript、Python 和 TypeScript 等多种编程语言
- **无缝集成**：使开发者能够轻松将不同的 AI 模型集成到应用中

MCP 在 AI 代理开发中尤为重要，它允许代理通过统一协议与各种系统和数据源交互，使代理更灵活、更强大。

## 学习目标
- 了解 MCP 是什么以及它在 AI 代理开发中的作用
- 搭建并配置用于 GitHub 集成的 MCP 服务器
- 使用 MCP 工具构建多代理系统
- 使用 Azure Cognitive Search 实现 RAG（检索增强生成）

## 先决条件
- Python 3.8 及以上版本
- Node.js 14 及以上版本
- Azure 订阅
- GitHub 账号
- 具备 Semantic Kernel 的基础知识

## 设置说明

1. **环境搭建**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **配置 Azure 服务**
   - 创建 Azure Cognitive Search 资源
   - 设置 Azure OpenAI 服务
   - 在 `.env` 文件中配置环境变量

3. **MCP 服务器搭建**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## 项目结构

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## 核心组件

### 1. 多代理系统
- GitHub 代理：仓库分析
- Hackathon 代理：项目推荐
- Events 代理：技术活动建议

### 2. Azure 集成
- 使用 Cognitive Search 进行活动索引
- 使用 Azure OpenAI 提升代理智能
- 实现 RAG 模式

### 3. MCP 工具
- GitHub 仓库分析
- 代码检查
- 元数据提取

## 代码讲解

示例展示了：
1. MCP 服务器集成
2. 多代理编排
3. Azure Cognitive Search 集成
4. RAG 模式实现

主要功能：
- 实时 GitHub 仓库分析
- 智能项目推荐
- 利用 Azure Search 进行活动匹配
- 使用 Chainlit 实现流式响应

## 运行示例

详细的设置步骤和更多信息，请参阅 [Github MCP Server Example README](./code_samples/github-mcp/README.md)。

1. 启动 MCP 服务器：
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. 启动应用程序：
   ```bash
   chainlit run app.py -w
   ```

3. 测试集成：
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## 故障排除

常见问题及解决方案：
1. MCP 连接问题
   - 确认服务器已启动
   - 检查端口是否被占用
   - 确认 GitHub 令牌有效

2. Azure Search 问题
   - 验证连接字符串
   - 检查索引是否存在
   - 确认文档上传成功

## 后续步骤
- 探索更多 MCP 工具
- 实现自定义代理
- 增强 RAG 功能
- 添加更多活动来源

## 资源
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**免责声明**：  
本文件已使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保准确性，但请注意自动翻译可能存在错误或不准确之处。原始语言版本的文件应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们不承担任何责任。