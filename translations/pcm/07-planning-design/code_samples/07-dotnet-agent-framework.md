<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-11T14:19:03+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "pcm"
}
-->
# 🎯 Planning & Design Patterns wit GitHub Models (.NET)

## 📋 Wetin You Go Learn

Dis notebook dey show enterprise-level planning and design patterns wey you fit use build smart agents wit Microsoft Agent Framework for .NET wit GitHub Models. You go learn how to create agents wey fit break down big problems, plan step-by-step solutions, and run advanced workflows wit .NET enterprise features.

## ⚙️ Wetin You Need & Setup

**Development Environment:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code wit C# extension
- GitHub Models API access

**Required Dependencies:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Environment Configuration (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## How to Run Di Code

Dis lesson get .NET Single File App implementation. To run am:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Or use di dotnet run command:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Code Implementation

Di full implementation dey inside `07-dotnet-agent-framework.cs`, e dey show:

- How to load environment configuration wit DotNetEnv
- How to configure OpenAI client for GitHub Models
- How to define structured data models (Plan and TravelPlan) wit JSON serialization
- How to create AI agent wey dey give structured output wit JSON schema
- How to run planning requests wit type-safe responses

## Key Concepts

### Structured Planning wit Type-Safe Models

Di agent dey use C# classes to define di structure of planning outputs:

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

### JSON Schema for Structured Outputs

Di agent dey configured to return responses wey match di TravelPlan schema:

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

### Planning Agent Instructions

Di agent dey act like coordinator, e dey share tasks give specialized sub-agents:

- FlightBooking: To book flights and provide flight info
- HotelBooking: To book hotels and provide hotel info
- CarRental: To book cars and provide car rental info
- ActivitiesBooking: To book activities and provide activity info
- DestinationInfo: To provide info about destinations
- DefaultAgent: To handle general requests

## Wetin You Go See

When you run di agent wit travel planning request, e go analyze di request and generate structured plan wit correct task assignments to di specialized agents, e go format am as JSON wey match di TravelPlan schema.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di one wey you go take as di correct source. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->