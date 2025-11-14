# 🎯 Planning & Design Patterns with GitHub Models (.NET)

## 📋 Learning Objectives

This notebook demonstrates enterprise-grade planning and design patterns for building intelligent agents using the Microsoft Agent Framework in .NET with GitHub Models. You'll learn to create agents that can decompose complex problems, plan multi-step solutions, and execute sophisticated workflows with .NET's enterprise features.

## ⚙️ Prerequisites & Setup

**Development Environment:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code with C# extension
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
- Configuring OpenAI client for GitHub Models
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

The agent acts as a coordinator, delegating tasks to specialized sub-agents:

- FlightBooking: For booking flights and providing flight information
- HotelBooking: For booking hotels and providing hotel information
- CarRental: For booking cars and providing car rental information
- ActivitiesBooking: For booking activities and providing activity information
- DestinationInfo: For providing information about destinations
- DefaultAgent: For handling general requests

## Expected Output

When you run the agent with a travel planning request, it will analyze the request and generate a structured plan with appropriate task assignments to specialized agents, formatted as JSON conforming to the TravelPlan schema.
