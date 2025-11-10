<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T08:57:46+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "zh"
}
-->
# 🔍 使用 Azure AI Foundry 构建企业级 RAG (.NET)

## 📋 学习目标

本笔记本演示如何使用 Microsoft Agent Framework 和 Azure AI Foundry 在 .NET 中构建企业级的检索增强生成 (RAG) 系统。您将学习如何创建生产级代理，能够搜索文档并提供准确、具有上下文的响应，同时具备企业级的安全性和可扩展性。

**您将构建的企业级 RAG 功能：**
- 📚 **文档智能**：通过 Azure AI 服务进行高级文档处理
- 🔍 **语义搜索**：具有企业功能的高性能向量搜索
- 🛡️ **安全集成**：基于角色的访问和数据保护模式
- 🏢 **可扩展架构**：具有监控功能的生产级 RAG 系统

## 🎯 企业级 RAG 架构

### 核心企业组件
- **Azure AI Foundry**：具有安全性和合规性的托管企业 AI 平台
- **持久化代理**：具有会话历史和上下文管理的状态代理
- **向量存储管理**：企业级文档索引和检索
- **身份集成**：Azure AD 身份验证和基于角色的访问控制

### .NET 企业优势
- **类型安全**：对 RAG 操作和数据结构进行编译时验证
- **异步性能**：非阻塞的文档处理和搜索操作
- **内存管理**：针对大型文档集合的高效资源利用
- **集成模式**：与 Azure 服务的原生集成和依赖注入

## 🏗️ 技术架构

### 企业级 RAG 流程
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### 核心 .NET 组件
- **Azure.AI.Agents.Persistent**：具有状态持久性的企业代理管理
- **Azure.Identity**：集成身份验证以安全访问 Azure 服务
- **Microsoft.Agents.AI.AzureAI**：优化 Azure 的代理框架实现
- **System.Linq.Async**：高性能异步 LINQ 操作

## 🔧 企业功能与优势

### 安全性与合规性
- **Azure AD 集成**：企业身份管理和身份验证
- **基于角色的访问**：对文档访问和操作的细粒度权限控制
- **数据保护**：对敏感文档进行静态和传输加密
- **审计日志**：全面的活动跟踪以满足合规要求

### 性能与可扩展性
- **连接池**：高效的 Azure 服务连接管理
- **异步处理**：适用于高吞吐量场景的非阻塞操作
- **缓存策略**：针对频繁访问的文档进行智能缓存
- **负载均衡**：适用于大规模部署的分布式处理

### 管理与监控
- **健康检查**：内置的 RAG 系统组件监控
- **性能指标**：关于搜索质量和响应时间的详细分析
- **错误处理**：全面的异常管理和重试策略
- **配置管理**：具有验证功能的环境特定设置

## ⚙️ 前提条件与设置

**开发环境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或带有 C# 扩展的 VS Code
- 具有 AI Foundry 访问权限的 Azure 订阅

**所需 NuGet 包：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure 身份验证设置：**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**环境配置：**
* Azure AI Foundry 配置（通过 Azure CLI 自动处理）
* 确保您已认证到正确的 Azure 订阅

## 📊 企业级 RAG 模式

### 文档管理模式
- **批量上传**：高效处理大型文档集合
- **增量更新**：实时添加和修改文档
- **版本控制**：文档版本管理和变更跟踪
- **元数据管理**：丰富的文档属性和分类体系

### 搜索与检索模式
- **混合搜索**：结合语义和关键词搜索以获得最佳结果
- **分面搜索**：多维过滤和分类
- **相关性调优**：针对特定领域需求的自定义评分算法
- **结果排序**：结合业务逻辑的高级排序

### 安全模式
- **文档级安全**：对每个文档的细粒度访问控制
- **数据分类**：自动敏感性标记和保护
- **审计追踪**：对所有 RAG 操作的全面日志记录
- **隐私保护**：PII 检测和信息遮蔽功能

## 🔒 企业安全功能

### 身份验证与授权
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### 数据保护
- **加密**：对文档和搜索索引进行端到端加密
- **访问控制**：与 Azure AD 集成以管理用户和组权限
- **数据驻留**：地理数据位置控制以满足合规性
- **备份与恢复**：自动化备份和灾难恢复功能

## 📈 性能优化

### 异步处理模式
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### 内存管理
- **流式处理**：处理大型文档而不会出现内存问题
- **资源池化**：高效重用昂贵资源
- **垃圾回收**：优化的内存分配模式
- **连接管理**：正确的 Azure 服务连接生命周期

### 缓存策略
- **查询缓存**：缓存频繁执行的搜索
- **文档缓存**：对热门文档进行内存缓存
- **索引缓存**：优化的向量索引缓存
- **结果缓存**：智能缓存生成的响应

## 📊 企业应用场景

### 知识管理
- **企业 Wiki**：智能搜索公司知识库
- **政策与流程**：自动化合规和流程指导
- **培训材料**：智能学习与发展辅助
- **研究数据库**：学术和研究论文分析系统

### 客户支持
- **支持知识库**：自动化客户服务响应
- **产品文档**：智能产品信息检索
- **故障排除指南**：上下文问题解决辅助
- **FAQ 系统**：从文档集合动态生成 FAQ

### 合规监管
- **法律文档分析**：合同和法律文档智能处理
- **合规监控**：自动化法规合规检查
- **风险评估**：基于文档的风险分析和报告
- **审计支持**：智能文档发现以支持审计

## 🚀 生产部署

### 监控与可观察性
- **Application Insights**：详细的遥测和性能监控
- **自定义指标**：业务特定的 KPI 跟踪和警报
- **分布式追踪**：跨服务的端到端请求追踪
- **健康仪表盘**：实时系统健康和性能可视化

### 可扩展性与可靠性
- **自动扩展**：基于负载和性能指标的自动扩展
- **高可用性**：具有故障转移功能的多区域部署
- **负载测试**：在企业负载条件下进行性能验证
- **灾难恢复**：自动化备份和恢复程序

准备好构建能够处理敏感文档的企业级 RAG 系统了吗？让我们为企业架构智能知识系统吧！ 🏢📖✨

## 代码实现

本课程的完整工作代码示例可在 `05-dotnet-agent-framework.cs` 中找到。

运行示例：

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

或者直接使用 `dotnet run`：

```bash
dotnet run 05-dotnet-agent-framework.cs
```

代码演示了以下内容：

1. **包安装**：安装 Azure AI Agents 所需的 NuGet 包
2. **环境配置**：加载 Azure AI Foundry 端点和模型设置
3. **文档上传**：上传文档以进行 RAG 处理
4. **向量存储创建**：创建用于语义搜索的向量存储
5. **代理配置**：设置具有文件搜索功能的 AI 代理
6. **查询执行**：对上传的文档运行查询

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。