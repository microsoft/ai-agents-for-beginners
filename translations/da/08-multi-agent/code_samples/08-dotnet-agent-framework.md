# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Læringsmål

Denne notesbog viser, hvordan man bygger sofistikerede enterprise-grade multi-agent systemer ved brug af Microsoft Agent Framework i .NET med Azure OpenAI (Responses API). Du lærer at orkestrere flere specialiserede agenter, der arbejder sammen gennem strukturerede workflows, og udnytter .NETs enterprise-funktioner til produktionsklare løsninger.

**Enterprise Multi-Agent kapabiliteter, du vil bygge:**
- 👥 **Agent samarbejde**: Typesikker agentkoordinering med compile-time validering
- 🔄 **Workflow orkestrering**: Deklarativ workflow-definering med .NETs async-mønstre
- 🎭 **Rollespecialisering**: Strongt-typede agentpersonligheder og ekspertisedomæner
- 🏢 **Enterprise integration**: Produktionsklare mønstre med overvågning og fejlbehandling

## ⚙️ Forudsætninger & opsætning

**Udviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-udvidelse
- Azure-abonnement (til vedvarende agenter)

**Påkrævede NuGet-pakker:**
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

## Kodeeksempel

Den fulde fungerende kode til denne lektion findes i den medfølgende C# fil: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

For at køre eksemplet:

```bash
# Gør filen eksekverbar (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Kør eksemplet
./08-dotnet-agent-framework.cs
```

Eller brug .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Hvad dette eksempel demonstrerer

Dette multi-agent workflow system skaber en hotelrejse-anbefalingsservice med to specialiserede agenter:

1. **FrontDesk Agent**: En rejseagent, der giver anbefalinger til aktiviteter og lokationer
2. **Concierge Agent**: Gennemgår anbefalinger for at sikre autentiske, ikke-turistede oplevelser

Agenterne arbejder sammen i et workflow, hvor:
- FrontDesk agenten modtager den oprindelige rejseanmodning
- Concierge agenten gennemgår og forbedrer anbefalingen
- Workflowen streamer svar i realtid

## Centrale koncepter

### Agentkoordinering
Eksemplet demonstrerer typesikker agentkoordinering ved hjælp af Microsoft Agent Framework med compile-time validering.

### Workflow orkestrering
Bruger deklarativ workflow-definering med .NETs async-mønstre til at forbinde flere agenter i en pipeline.

### Streaming af svar
Implementerer realtids-streaming af agentrespons ved brug af async enumerables og event-drevet arkitektur.

### Enterprise integration
Viser produktionsklare mønstre, herunder:
- Konfiguration af miljøvariabler
- Sikker håndtering af legitimationsoplysninger
- Fejlbehandling
- Asynkron eventbehandling

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->