<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:54:01+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "en"
}
-->
# 🎯 Planning & Design Patterns with GitHub Models (.NET)

## 📋 Learning Objectives

This notebook showcases enterprise-level planning and design patterns for creating intelligent agents using the Microsoft Agent Framework in .NET with GitHub Models. You'll learn how to build agents capable of breaking down complex problems, planning multi-step solutions, and executing advanced workflows using .NET's enterprise features.

## ⚙️ Prerequisites & Setup

**Development Environment:**
- .NET 9.0 SDK or later
- Visual Studio 2022 or VS Code with the C# extension
- Access to GitHub Models API

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

This lesson includes a .NET Single File App implementation. To execute it:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Alternatively, use the dotnet run command:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Code Implementation

The full implementation is provided in `07-dotnet-agent-framework.cs`, which demonstrates:

- Loading environment configuration using DotNetEnv
- Setting up the OpenAI client for GitHub Models
- Defining structured data models (Plan and TravelPlan) with JSON serialization
- Building an AI agent with structured output using JSON schema
- Executing planning requests with type-safe responses

## Key Concepts

### Structured Planning with Type-Safe Models

The agent utilizes C# classes to define the structure of planning outputs:

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

The agent is configured to return responses that align with the TravelPlan schema:

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

The agent serves as a coordinator, assigning tasks to specialized sub-agents:

- FlightBooking: Responsible for booking flights and providing flight details
- HotelBooking: Responsible for booking hotels and providing hotel details
- CarRental: Responsible for booking cars and providing car rental details
- ActivitiesBooking: Responsible for booking activities and providing activity details
- DestinationInfo: Responsible for providing information about destinations
- DefaultAgent: Handles general requests

## Expected Output

When the agent processes a travel planning request, it will evaluate the request and produce a structured plan with appropriate task assignments to specialized agents, formatted as JSON adhering to the TravelPlan schema.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.