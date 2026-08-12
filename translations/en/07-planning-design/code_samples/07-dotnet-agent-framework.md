# 🎯 Planning & Design Patterns with Azure OpenAI (Responses API) (.NET)

## 📋 Learning Objectives

This notebook demonstrates enterprise-grade planning and design patterns for building intelligent agents using the Microsoft Agent Framework in .NET with Azure OpenAI (Responses API). You'll learn to create agents that can decompose complex problems, plan multi-step solutions, and execute sophisticated workflows with .NET's enterprise features.

## ⚙️ Prerequisites & Setup

**Development Environment:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code with C# extension
- An Azure subscription with an Azure OpenAI resource and a model deployment
- The Azure CLI — sign in with `az login`

**Required Dependencies:**
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

## Running the Code

This lesson includes a .NET Single File App implementation. To run it:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Or use the dotnet run command:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Code Implementation

The complete implementation is available in `07-dotnet-agent-framework.cs`, which demonstrates:

- Loading environment configuration with DotNetEnv
- Configuring the Azure OpenAI client and creating an AI agent using `GetChatClient().AsAIAgent()`
- Defining structured data models (Plan and TravelPlan) with JSON serialization
- Creating an AI agent with structured output using JSON schema
- Executing planning requests with type-safe responses

## Key Concepts

### Structured Planning with Type-Safe Models

The agent uses C# classes to define the structure of planning outputs:

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

The agent is configured to return responses matching the TravelPlan schema:

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

The agent acts as a coordinator, delegating tasks to specialized sub-agents:

- FlightBooking: For booking flights and providing flight information
- HotelBooking: For booking hotels and providing hotel information
- CarRental: For booking cars and providing car rental information
- ActivitiesBooking: For booking activities and providing activity information
- DestinationInfo: For providing information about destinations
- DefaultAgent: For handling general requests

## Expected Output

When you run the agent with a travel planning request, it will analyze the request and generate a structured plan with appropriate task assignments to specialized agents, formatted as JSON conforming to the TravelPlan schema.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->