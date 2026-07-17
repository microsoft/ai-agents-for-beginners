# 🎯 Planning & Design Patterns wit Azure OpenAI (Responses API) (.NET)

## 📋 Wetin You Go Learn

Dis notebook dey show how to plan and design tin dem wey big company fit use to build smart agents with Microsoft Agent Framework for .NET wit Azure OpenAI (Responses API). You go learn how to create agents wey fit break complex wahala down, plan how to solve am for many steps, and run better fine workflows wit ÐOTNET enterprise features.

## ⚙️ Wetin You Need & How To Setup

**Development Environment:**
- .NET 9.0 SDK or more
- Visual Studio 2022 or VS Code with C# extension
- Azure subscription wit Azure OpenAI resource and model deployment
- Azure CLI — login wit `az login`

**Dependencies We Need:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Environment Config (.env file):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## How To Run The Code

Dis lesson get .NET Single File App implementation. To run am:

```bash
# Make di file fit run (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run di app
./07-dotnet-agent-framework.cs
```

Or use dotnet run command:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## How Di Code Dem Work

Full implement dey for `07-dotnet-agent-framework.cs`, wey show:

- How to load environment config wit DotNetEnv
- How to set Azure OpenAI client and create AI agent using `GetChatClient().AsAIAgent()`
- How to define structured data models (Plan and TravelPlan) wit JSON serialization
- How to create AI agent wit structured output using JSON schema
- How to run planning requests with type-safe responses

## Important Ideas

### Structured Planning Wit Type-Safe Models

Di agent dey use C# classes to define how planning outputs go look like:

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

Di agent dey configured to return answers wey match di TravelPlan schema:

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

### Instructions for Planning Agent

Di agent dey work as coordinator, e dey send work go to special sub-agents:

- FlightBooking: For book flight and give flight info
- HotelBooking: For book hotel and give hotel info
- CarRental: For book car and give car rental info
- ActivitiesBooking: For book activities and give activity info
- DestinationInfo: For give info about destinations
- DefaultAgent: For handle general requests

## Wetin You Go See As Output

When you run agent wit travel planning request, e go check di request and create one structured plan wit beta task assignations to di special agents, e go format am as JSON wey follow di TravelPlan schema.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->