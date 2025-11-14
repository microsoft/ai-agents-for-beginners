<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:43:44+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "zh"
}
-->
# 🎨 使用 GitHub 模型的智能代理设计模式 (.NET)

## 📋 学习目标

本笔记展示了使用 Microsoft Agent Framework 和 GitHub 模型集成在 .NET 中构建智能代理的企业级设计模式。您将学习使代理具备生产就绪、易维护和可扩展性的专业模式和架构方法。

**企业设计模式：**
- 🏭 **工厂模式**：通过依赖注入实现标准化的代理创建
- 🔧 **建造者模式**：流畅的代理配置和设置
- 🧵 **线程安全模式**：并发对话管理
- 📋 **仓库模式**：有组织的工具和能力管理

## 🎯 .NET 特定的架构优势

### 企业功能
- **强类型**：编译时验证和 IntelliSense 支持
- **依赖注入**：内置 DI 容器集成
- **配置管理**：IConfiguration 和 Options 模式
- **异步编程**：一流的异步编程支持

### 生产就绪模式
- **日志集成**：ILogger 和结构化日志支持
- **健康检查**：内置监控和诊断功能
- **配置验证**：通过数据注解实现强类型验证
- **错误处理**：结构化异常管理

## 🔧 技术架构

### 核心 .NET 组件
- **Microsoft.Extensions.AI**：统一的 AI 服务抽象
- **Microsoft.Agents.AI**：企业级代理编排框架
- **GitHub 模型集成**：高性能 API 客户端模式
- **配置系统**：appsettings.json 和环境集成

### 设计模式实现
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ 展示的企业模式

### 1. **创建型模式**
- **代理工厂**：通过一致的配置实现集中化代理创建
- **建造者模式**：用于复杂代理配置的流畅 API
- **单例模式**：共享资源和配置管理
- **依赖注入**：松耦合和可测试性

### 2. **行为型模式**
- **策略模式**：可互换的工具执行策略
- **命令模式**：封装的代理操作，支持撤销/重做
- **观察者模式**：事件驱动的代理生命周期管理
- **模板方法**：标准化的代理执行工作流

### 3. **结构型模式**
- **适配器模式**：GitHub 模型 API 集成层
- **装饰器模式**：代理能力增强
- **外观模式**：简化的代理交互接口
- **代理模式**：延迟加载和缓存以提升性能

## ⚙️ 前置条件与设置

**开发环境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或带有 C# 扩展的 VS Code
- GitHub 模型 API 访问权限

**NuGet 依赖项：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**配置 (.env 文件)：**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 .NET 设计原则

### SOLID 原则
- **单一职责**：每个组件都有一个明确的目的
- **开闭原则**：可扩展而无需修改
- **里氏替换原则**：基于接口的工具实现
- **接口隔离原则**：专注且内聚的接口
- **依赖倒置原则**：依赖抽象而非具体实现

### 清晰架构
- **领域层**：核心代理和工具抽象
- **应用层**：代理编排和工作流
- **基础设施层**：GitHub 模型集成和外部服务
- **表现层**：用户交互和响应格式化

## 🔒 企业级考量

### 安全性
- **凭证管理**：通过 IConfiguration 安全处理 API 密钥
- **输入验证**：强类型和数据注解验证
- **输出清理**：安全的响应处理和过滤
- **审计日志**：全面的操作跟踪

### 性能
- **异步模式**：非阻塞 I/O 操作
- **连接池**：高效的 HTTP 客户端管理
- **缓存**：响应缓存以提升性能
- **资源管理**：正确的资源释放和清理模式

### 可扩展性
- **线程安全**：支持并发代理执行
- **资源池化**：高效的资源利用
- **负载管理**：速率限制和压力处理
- **监控**：性能指标和健康检查

## 🚀 生产部署

- **配置管理**：基于环境的设置
- **日志策略**：结构化日志记录，支持关联 ID
- **错误处理**：全局异常处理和适当的恢复机制
- **监控**：应用洞察和性能计数器
- **测试**：单元测试、集成测试和负载测试模式

准备好使用 .NET 构建企业级智能代理了吗？让我们设计一个强大的架构吧！ 🏢✨

## 代码示例

完整的工作示例请参见 [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs)。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。