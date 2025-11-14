<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:12:56+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "en"
}
-->
# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Learning Objectives

This notebook explains how to create advanced enterprise-level multi-agent systems using the Microsoft Agent Framework in .NET with GitHub Models. You'll learn to coordinate multiple specialized agents working together through structured workflows, utilizing .NET's enterprise features for production-ready solutions.

**Enterprise Multi-Agent Capabilities You'll Develop:**
- 👥 **Agent Collaboration**: Type-safe agent coordination with compile-time validation
- 🔄 **Workflow Orchestration**: Declarative workflow definition using .NET's async patterns
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

The complete working code for this lesson is available in the accompanying C# file: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

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

The agents collaborate in a workflow where:
- The FrontDesk agent handles the initial travel request
- The Concierge agent reviews and refines the recommendation
- The workflow streams responses in real-time

## Key Concepts

### Agent Coordination
The sample showcases type-safe agent coordination using the Microsoft Agent Framework with compile-time validation.

### Workflow Orchestration
Demonstrates declarative workflow definition using .NET's async patterns to connect multiple agents in a pipeline.

### Streaming Responses
Implements real-time streaming of agent responses using async enumerables and event-driven architecture.

### Enterprise Integration
Illustrates production-ready patterns including:
- Environment variable configuration
- Secure credential management
- Error handling
- Asynchronous event processing

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.