# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Learning Objectives

Dis notebook show how you fit build beta enterprise-grade multi-agent systems wey use Microsoft Agent Framework for .NET wit Azure OpenAI (Responses API). You go learn how to manage multiple specialised agents wey dey work together through structured workflows, wey use .NET enterprise features for solution wey dey ready for production.

**Enterprise Multi-Agent Capacities wey you go build:**
- 👥 **Agent Collaboration**: Type-safe agent coordination wit compile-time validation
- 🔄 **Workflow Orchestration**: Declarative workflow definition wit .NET async patterns
- 🎭 **Role Specialization**: Strongly-typed agent personalities and expertise domains
- 🏢 **Enterprise Integration**: Production-ready patterns wit monitoring and error handling

## ⚙️ Prerequisites & Setup

**Development Environment:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code wit C# extension
- Azure subscription (for persistent agents)

**Required NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Code Sample

Di complete working code for dis lesson dey for di accompanying C# file: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

To run di sample:

```bash
# Make di file fit run (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run di sample
./08-dotnet-agent-framework.cs
```

Or if you use di .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Wetin Dis Sample Dey Show

Dis multi-agent workflow system fit create hotel travel recommendation service wit two specialised agents:

1. **FrontDesk Agent**: Na travel agent wey dey provide activity and location recommendations
2. **Concierge Agent**: E dey review recommendations make sure say dem authentic, no be tourist wahala

Di agents dey work together for one workflow wey:
- Di FrontDesk agent dey receive di initial travel request
- Di Concierge agent dey review and improve di recommendation
- Di workflow dey stream responses for real-time

## Key Concepts

### Agent Coordination
Di sample dey show type-safe agent coordination wit Microsoft Agent Framework wit compile-time validation.

### Workflow Orchestration
E use declarative workflow definition wit .NET async patterns to connect multiple agents for pipeline.

### Streaming Responses
E implement real-time streaming of agent responses wit async enumerables and event-driven architecture.

### Enterprise Integration
E show production-ready patterns include:
- Environment variable configuration
- Secure credential management
- Error handling
- Asynchronous event processing

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->