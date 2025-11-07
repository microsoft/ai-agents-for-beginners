# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Learning Objectives

This notebook demonstrates how to build sophisticated enterprise-grade multi-agent systems using the Microsoft Agent Framework in .NET with GitHub Models. You'll learn to orchestrate multiple specialized agents working together through structured workflows, leveraging .NET's enterprise features for production-ready solutions.

**Enterprise Multi-Agent Capabilities You'll Build:**
- 👥 **Agent Collaboration**: Type-safe agent coordination with compile-time validation
- 🔄 **Workflow Orchestration**: Declarative workflow definition with .NET's async patterns
- 🎭 **Role Specialization**: Strongly-typed agent personalities and expertise domains
- 🏢 **Enterprise Integration**: Production-ready patterns with monitoring and error handling

## ⚙️ Prerequisites & Setup

**Development Environment:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code with C# extension
- Azure subscription (for persistent agents)

**Required NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Code Sample

The complete working code for this lesson is available in the accompanying C# file: [`08-dotnet-agent-framework.cs`](./08-dotnet-agent-framework.cs)

To run the sample:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Or using the .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## What This Sample Demonstrates

This multi-agent workflow system creates a hotel travel recommendation service with two specialized agents:

1. **FrontDesk Agent**: A travel agent that provides activity and location recommendations
2. **Concierge Agent**: Reviews recommendations to ensure authentic, non-touristy experiences

The agents work together in a workflow where:
- The FrontDesk agent receives the initial travel request
- The Concierge agent reviews and refines the recommendation
- The workflow streams responses in real-time

## Key Concepts

### Agent Coordination
The sample demonstrates type-safe agent coordination using the Microsoft Agent Framework with compile-time validation.

### Workflow Orchestration
Uses declarative workflow definition with .NET's async patterns to connect multiple agents in a pipeline.

### Streaming Responses
Implements real-time streaming of agent responses using async enumerables and event-driven architecture.

### Enterprise Integration
Shows production-ready patterns including:
- Environment variable configuration
- Secure credential management
- Error handling
- Asynchronous event processing
