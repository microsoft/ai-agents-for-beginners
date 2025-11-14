<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:55:00+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "zh"
}
-->
# 🎯 使用 GitHub 模型 (.NET) 的规划与设计模式

## 📋 学习目标

本笔记展示了使用 Microsoft Agent Framework 和 GitHub 模型在 .NET 中构建智能代理的企业级规划与设计模式。您将学习如何创建能够分解复杂问题、规划多步骤解决方案并利用 .NET 企业功能执行复杂工作流的代理。

## ⚙️ 前置条件与设置

**开发环境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或安装了 C# 扩展的 VS Code
- GitHub Models API 访问权限

**所需依赖：**
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

## 运行代码

本课程包含一个 .NET 单文件应用程序实现。运行方法如下：

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

或者使用 dotnet run 命令：

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## 代码实现

完整实现可在 `07-dotnet-agent-framework.cs` 文件中找到，展示了以下内容：

- 使用 DotNetEnv 加载环境配置
- 配置 OpenAI 客户端以使用 GitHub 模型
- 使用 JSON 序列化定义结构化数据模型（Plan 和 TravelPlan）
- 使用 JSON schema 创建具有结构化输出的 AI 代理
- 执行规划请求并返回类型安全的响应

## 核心概念

### 使用类型安全模型进行结构化规划

代理使用 C# 类定义规划输出的结构：

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### 用 JSON Schema 定义结构化输出

代理被配置为返回符合 TravelPlan schema 的响应：

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### 规划代理指令

代理充当协调者，将任务分配给专门的子代理：

- FlightBooking：负责预订航班并提供航班信息
- HotelBooking：负责预订酒店并提供酒店信息
- CarRental：负责预订汽车并提供租车信息
- ActivitiesBooking：负责预订活动并提供活动信息
- DestinationInfo：负责提供目的地信息
- DefaultAgent：处理一般请求

## 预期输出

当您使用旅行规划请求运行代理时，它将分析请求并生成一个结构化计划，包含适当的任务分配给专门的代理，并以符合 TravelPlan schema 的 JSON 格式输出。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。