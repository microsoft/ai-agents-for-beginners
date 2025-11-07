<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:21:43+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "zh"
}
-->
# 🛠️ 使用 GitHub 模型的高级工具 (.NET)

## 📋 学习目标

本笔记本展示了使用 Microsoft Agent Framework 和 GitHub 模型在 .NET 中进行企业级工具集成的模式。您将学习如何构建具有多种专业工具的复杂代理，充分利用 C# 的强类型和 .NET 的企业功能。

**您将掌握的高级工具能力：**
- 🔧 **多工具架构**：构建具有多种专业功能的代理
- 🎯 **类型安全的工具执行**：利用 C# 的编译时验证
- 📊 **企业工具模式**：生产级工具设计和错误处理
- 🔗 **工具组合**：结合工具实现复杂的业务工作流

## 🎯 .NET 工具架构优势

### 企业工具特性
- **编译时验证**：强类型确保工具参数的正确性
- **依赖注入**：通过 IoC 容器管理工具
- **异步模式**：使用 Async/Await 实现非阻塞工具执行和资源管理
- **结构化日志**：内置日志集成，用于监控工具执行

### 生产级模式
- **异常处理**：通过类型化异常进行全面的错误管理
- **资源管理**：正确的资源释放模式和内存管理
- **性能监控**：内置指标和性能计数器
- **配置管理**：类型安全的配置和验证

## 🔧 技术架构

### 核心 .NET 工具组件
- **Microsoft.Extensions.AI**：统一的工具抽象层
- **Microsoft.Agents.AI**：企业级工具编排
- **GitHub 模型集成**：高性能 API 客户端，支持连接池

### 工具执行管道
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ 工具类别与模式

### 1. **数据处理工具**
- **输入验证**：通过数据注解实现强类型验证
- **转换操作**：类型安全的数据转换和格式化
- **业务逻辑**：领域特定的计算和分析工具
- **输出格式化**：生成结构化响应

### 2. **集成工具**
- **API 连接器**：使用 HttpClient 集成 RESTful 服务
- **数据库工具**：通过 Entity Framework 进行数据访问
- **文件操作**：安全的文件系统操作并进行验证
- **外部服务**：第三方服务集成模式

### 3. **实用工具**
- **文本处理**：字符串操作和格式化工具
- **日期/时间操作**：支持文化差异的日期/时间计算
- **数学工具**：精确计算和统计操作
- **验证工具**：业务规则验证和数据校验

## ⚙️ 前提条件与设置

**开发环境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或安装了 C# 扩展的 VS Code
- GitHub 模型 API 访问权限

**所需 NuGet 包：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**环境配置 (.env 文件)：**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

准备好在 .NET 中构建企业级代理，拥有强大的类型安全工具功能了吗？让我们一起设计专业级解决方案吧！ 🏢⚡

## 💻 代码实现

完整的 C# 实现可在配套文件 `04-dotnet-agent-framework.cs` 中找到。此 .NET 单文件应用程序演示了：

- 加载 GitHub 模型配置的环境变量
- 使用 C# 方法和属性定义自定义工具
- 创建集成工具的 AI 代理
- 管理会话线程
- 执行代理请求并调用工具

运行示例：

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

或者使用 .NET CLI：

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。