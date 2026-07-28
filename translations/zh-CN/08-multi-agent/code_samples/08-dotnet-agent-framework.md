# 🤝 企业多智能体工作流系统（.NET）

## 📋 学习目标

本笔记本展示了如何使用.NET中的Microsoft Agent框架和Azure OpenAI（Responses API）构建复杂的企业级多智能体系统。您将学习如何通过结构化工作流协调多个专业化智能体协同工作，利用.NET的企业功能实现生产就绪的解决方案。

**您将构建的企业多智能体能力：**
- 👥 <strong>智能体协作</strong>：使用编译时验证的类型安全智能体协调
- 🔄 <strong>工作流编排</strong>：使用.NET异步模式的声明式工作流定义
- 🎭 <strong>角色专业化</strong>：强类型智能体角色和专业领域
- 🏢 <strong>企业集成</strong>：具备监控和错误处理的生产就绪模式

## ⚙️ 前提条件与设置

**开发环境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或带有 C# 扩展的 VS Code
- Azure 订阅（用于持久化智能体）

**必需的 NuGet 包：**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## 代码示例

本课的完整工作代码可在附带的 C# 文件中获取：[ `08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

运行示例：

```bash
# 使文件可执行（Linux/macOS）
chmod +x 08-dotnet-agent-framework.cs

# 运行示例
./08-dotnet-agent-framework.cs
```

或使用 .NET CLI：

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## 本示例演示内容

该多智能体工作流系统创建了一个酒店旅行推荐服务，包含两个专业智能体：

1. **FrontDesk Agent**：提供活动和地点推荐的旅行智能体
2. **Concierge Agent**：审核推荐以确保真实、非旅游化的体验

智能体共同在一个工作流中协作：
- FrontDesk智能体接收初始旅行请求
- Concierge智能体审核并优化推荐
- 工作流实时流式传输响应

## 关键概念

### 智能体协调
本示例展示了使用Microsoft Agent框架进行类型安全的智能体协调，具备编译时验证。

### 工作流编排
使用.NET异步模式的声明式工作流定义，将多个智能体连接成管道。

### 流式响应
实现使用异步可枚举和事件驱动架构的智能体响应实时流式传输。

### 企业集成
展示生产就绪模式，包括：
- 环境变量配置
- 安全凭据管理
- 错误处理
- 异步事件处理

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->