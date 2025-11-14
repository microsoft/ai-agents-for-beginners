<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-11T11:58:18+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "pcm"
}
-->
# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Wetin You Go Learn

Dis notebook go show you how to build beta enterprise-level multi-agent systems wey dey use Microsoft Agent Framework for .NET with GitHub Models. You go sabi how to arrange many specialized agents wey dey work together through structured workflows, dey use .NET enterprise features for solutions wey fit production.

**Enterprise Multi-Agent Things We Go Build:**
- 👥 **Agent Collaboration**: Type-safe agent coordination wey get compile-time validation
- 🔄 **Workflow Orchestration**: Declarative workflow definition wey dey use .NET async patterns
- 🎭 **Role Specialization**: Strongly-typed agent personalities and expertise domains
- 🏢 **Enterprise Integration**: Production-ready patterns wey get monitoring and error handling

## ⚙️ Wetin You Need & Setup

**Development Environment:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code wey get C# extension
- Azure subscription (for persistent agents)

**NuGet Packages We You Go Need:**
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

The full working code for dis lesson dey inside the C# file wey follow am: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

To run the sample:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Or if you wan use the .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Wetin Dis Sample Dey Show

Dis multi-agent workflow system dey create one hotel travel recommendation service wey get two specialized agents:

1. **FrontDesk Agent**: Na travel agent wey dey give activity and location recommendations
2. **Concierge Agent**: E dey check recommendations to make sure say dem dey authentic and no be touristy experiences

How dem agents dey work together for workflow na like dis:
- FrontDesk agent go first collect the travel request
- Concierge agent go review and refine the recommendation
- Workflow go dey stream responses as e dey happen

## Key Concepts

### Agent Coordination
Dis sample dey show type-safe agent coordination wey dey use Microsoft Agent Framework with compile-time validation.

### Workflow Orchestration
E dey use declarative workflow definition wey dey use .NET async patterns to connect many agents for pipeline.

### Streaming Responses
E dey implement real-time streaming of agent responses wey dey use async enumerables and event-driven architecture.

### Enterprise Integration
E dey show production-ready patterns wey include:
- Environment variable configuration
- Secure credential management
- Error handling
- Asynchronous event processing

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->