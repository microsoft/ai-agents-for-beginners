<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:04:25+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "zh"
}
-->
# 第十一课：模型上下文协议（MCP）集成

## 模型上下文协议（MCP）简介

模型上下文协议（MCP）是一种先进的框架，旨在标准化AI模型与客户端应用之间的交互。MCP充当AI模型与使用它们的应用之间的桥梁，无论底层模型的实现如何，都提供一致的接口。

MCP的关键特点：

- **标准化通信**：MCP为应用与AI模型之间的通信建立了通用语言  
- **增强的上下文管理**：支持高效地向AI模型传递上下文信息  
- **跨平台兼容性**：支持多种编程语言，包括C#、Java、JavaScript、Python和TypeScript  
- **无缝集成**：使开发者能够轻松将不同的AI模型集成到应用中  

MCP在AI代理开发中尤为重要，因为它允许代理通过统一协议与各种系统和数据源交互，使代理更加灵活和强大。

## 学习目标
- 了解MCP是什么及其在AI代理开发中的作用  
- 设置并配置MCP服务器以实现GitHub集成  
- 使用MCP工具构建多代理系统  
- 使用Azure Cognitive Search实现RAG（检索增强生成）  

## 前置条件
- Python 3.8及以上版本  
- Node.js 14及以上版本  
- Azure订阅  
- GitHub账户  
- 对Semantic Kernel的基本了解  

## 设置说明

1. **环境设置**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **配置Azure服务**  
   - 创建Azure Cognitive Search资源  
   - 设置Azure OpenAI服务  
   - 在`.env`文件中配置环境变量  

3. **MCP服务器设置**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## 项目结构

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## 核心组件

### 1. 多代理系统
- GitHub代理：仓库分析  
- Hackathon代理：项目推荐  
- Events代理：技术活动建议  

### 2. Azure集成
- 使用Cognitive Search进行活动索引  
- 使用Azure OpenAI提供代理智能  
- 实现RAG模式  

### 3. MCP工具
- GitHub仓库分析  
- 代码检查  
- 元数据提取  

## 代码讲解

示例展示了以下内容：  
1. MCP服务器集成  
2. 多代理编排  
3. Azure Cognitive Search集成  
4. RAG模式实现  

主要功能：  
- 实时GitHub仓库分析  
- 智能项目推荐  
- 使用Azure Search进行活动匹配  
- 使用Chainlit进行流式响应  

## 运行示例

有关详细的设置说明和更多信息，请参考[Github MCP Server Example README](./code_samples/github-mcp/README.md)。

1. 启动MCP服务器：  
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

常见问题及解决方法：  
1. MCP连接问题  
   - 确保服务器正在运行  
   - 检查端口是否可用  
   - 确认GitHub令牌  

2. Azure Search问题  
   - 验证连接字符串  
   - 检查索引是否存在  
   - 确认文档上传  

## 后续步骤
- 探索更多MCP工具  
- 实现自定义代理  
- 增强RAG功能  
- 添加更多活动来源  
- **高级**：查看[mcp-agents/](../../../11-mcp/code_samples/mcp-agents)以了解代理间通信示例  

## 资源
- [MCP入门指南](https://aka.ms/mcp-for-beginners)  
- [MCP文档](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search文档](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel指南](https://learn.microsoft.com/semantic-kernel/)  

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们概不负责。