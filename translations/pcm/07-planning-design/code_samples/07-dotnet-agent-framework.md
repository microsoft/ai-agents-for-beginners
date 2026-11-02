# 🎯 Planning & Design Patterns wit Azure OpenAI (Responses API) (.NET)

## 📋 Wetin You Go Learn

Dis notebook show how to do big-big planning and design patterns to build smart agents + Microsoft Agent Framework for .NET wit Azure OpenAI (Responses API). You go sabi how to make agents wey fit break palava dem down, plan many-step solutions, and run sophisticated workflow dem wit .NET enterprise features dem.

## ⚙️ Things You Need & How To Setup

**Development Environment:**
- .NET 9.0 SDK or pass am
- Visual Studio 2022 or VS Code wit C# extension
- Azure subscription wey get Azure OpenAI resource and model deployment
- Azure CLI — sign in wit `az login`

**Dependencies Wey You Need:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Environment Configuration (.env file):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## How To Run The Code

Dis lesson get .NET Single File App wey you fit run. To run am:

```bash
# Make di file fit run (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run di application
./07-dotnet-agent-framework.cs
```

Or you fit use dotnet run command:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## How The Code Take Work

Full implementation dey `07-dotnet-agent-framework.cs`, wey show:

- How to load environment config with DotNetEnv
- How to setup Azure OpenAI client and make AI agent wit `GetChatClient().AsAIAgent()`
- How to define structured data models (Plan and TravelPlan) wit JSON serialization
- How to create AI agent wey get structured output using JSON schema
- How to run planning requests wit type-safe responses

## Main Tori Dem

### Structured Planning Wit Type-Safe Models

The agent dey use C# classes to define how planning outputs supposed be structured:

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

### JSON Schema For Structured Outputs

The agent dem set am to return responses wey match the TravelPlan schema:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
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

The agent dey act as coordinator, e go pass tasks to different special agents:

- FlightBooking: To book flights and give flight info
- HotelBooking: To book hotels and give hotel info
- CarRental: To book cars and give car rental info
- ActivitiesBooking: To book activities and give activity info
- DestinationInfo: To give info about destinations
- DefaultAgent: To handle general requests

## Wetin You Go See As Result

When you run the agent with travel planning request, e go check the request, then create structured plan wit correct tasks wey go reach special agents, dem go arrange am as JSON wey follow the TravelPlan schema.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->