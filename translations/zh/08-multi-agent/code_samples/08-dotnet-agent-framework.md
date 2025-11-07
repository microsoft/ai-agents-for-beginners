<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:13:59+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "zh"
}
-->
# 🤝 企业级多代理工作流系统 (.NET)

## 📋 学习目标

本笔记本展示了如何使用 .NET 中的 Microsoft Agent Framework 和 GitHub 模型构建复杂的企业级多代理系统。您将学习如何通过结构化工作流协调多个专业代理，利用 .NET 的企业功能构建生产级解决方案。

**您将构建的企业级多代理功能：**
- 👥 **代理协作**：类型安全的代理协调，支持编译时验证
- 🔄 **工作流编排**：使用 .NET 异步模式进行声明式工作流定义
- 🎭 **角色专精**：强类型的代理个性和专业领域
- 🏢 **企业集成**：生产级模式，包含监控和错误处理

## ⚙️ 前置条件与设置

**开发环境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或安装了 C# 扩展的 VS Code
- Azure 订阅（用于持久化代理）

**所需的 NuGet 包：**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## 代码示例

本课程的完整代码可在随附的 C# 文件中找到：[`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

运行示例代码：

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

或者使用 .NET CLI：

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## 本示例展示内容

此多代理工作流系统创建了一个酒店旅行推荐服务，包含两个专业代理：

1. **前台代理**：一个提供活动和地点推荐的旅行代理
2. **礼宾代理**：审查推荐内容，确保提供真实且非游客化的体验

代理通过以下工作流协作：
- 前台代理接收初始旅行请求
- 礼宾代理审查并优化推荐内容
- 工作流实时流式传输响应

## 核心概念

### 代理协调
示例展示了使用 Microsoft Agent Framework 进行类型安全的代理协调，并支持编译时验证。

### 工作流编排
使用 .NET 异步模式进行声明式工作流定义，将多个代理连接到一个管道中。

### 流式响应
通过异步枚举和事件驱动架构实现代理响应的实时流式传输。

### 企业集成
展示了生产级模式，包括：
- 环境变量配置
- 安全凭证管理
- 错误处理
- 异步事件处理

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。