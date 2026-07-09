# 🎯 Planning & Design Patterns wit Azure OpenAI (Responses API) (.NET)

## 📋 Wetin You Go Learn

Dis notebook dey show beta enterprise-level planning and design patterns for build intelligent agents using Microsoft Agent Framework for .NET wit Azure OpenAI (Responses API). You go learn how to create agents wey fit break complex wahala down, plan multi-step solutions, and run sharp workflows wit .NET enterprise features dem.

## ⚙️ Wetin You Need & Setup

**Development Environment:**
- .NET 9.0 SDK or above
- Visual Studio 2022 or VS Code wit C# extension
- One Azure subscription get Azure OpenAI resource and model deployment
- Azure CLI — signin wit `az login`

**Required Dependencies:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Environment Configuration (.env file):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## How To Run The Code

Dis lesson get .NET Single File App implementation inside am. To run am:

```bash
# Mek the file fit run (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run di application
./07-dotnet-agent-framework.cs
```

Or use dotnet run command:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## How Code Dey Work

Full implementation dey for `07-dotnet-agent-framework.cs`, wey show:

- How to load environment configuration wit DotNetEnv
- How to setup Azure OpenAI client for Responses API
- How to define structured data models (Plan and TravelPlan) wit JSON serialization
- How to create AI agent wit structured output using JSON schema
- How to run planning requests using type-safe responses

## Main Things Wey You Gotta Sabi

### Planning Wey Get Structure Wit Type-Safe Models

Di agent dey use C# classes to define how planning output go be:

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

Di agent dey set make e return response wey match TravelPlan schema:

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

### Instructions for Planning Agent

Di agent dey act like coordinator, e dey delegate tasks go sub-agents wey sabi their work:

- FlightBooking: To book flights and give flight info
- HotelBooking: To book hotels and give hotel info
- CarRental: To book cars and give car rental info
- ActivitiesBooking: To book activities and give activity info
- DestinationInfo: To give info about destinations
- DefaultAgent: To handle general requests

## Wetin You Go See As Output

When you run di agent wit travel planning request, e go check the request well well and create structured plan wit correct task assignment go specialized agents, and e go format am as JSON wey follow TravelPlan schema well.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->