<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:16:50+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "da"
}
-->
# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Læringsmål

Denne notebook viser, hvordan man bygger avancerede multi-agent systemer i enterprise-klassen ved hjælp af Microsoft Agent Framework i .NET med GitHub-modeller. Du vil lære at orkestrere flere specialiserede agenter, der arbejder sammen gennem strukturerede workflows, og udnytte .NET's enterprise-funktioner til produktionsklare løsninger.

**Enterprise Multi-Agent Funktioner Du Vil Bygge:**
- 👥 **Agent Samarbejde**: Type-sikker agentkoordinering med validering ved kompileringstidspunktet
- 🔄 **Workflow Orkestrering**: Deklarativ workflow-definition med .NET's asynkrone mønstre
- 🎭 **Rolle Specialisering**: Stærkt typede agentpersonligheder og ekspertiseområder
- 🏢 **Enterprise Integration**: Produktionsklare mønstre med overvågning og fejlhåndtering

## ⚙️ Forudsætninger & Opsætning

**Udviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-udvidelse
- Azure-abonnement (til vedvarende agenter)

**Påkrævede NuGet-pakker:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Eksempelkode

Den komplette fungerende kode til denne lektion findes i den medfølgende C#-fil: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

For at køre eksemplet:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Eller ved hjælp af .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Hvad Dette Eksempel Demonstrerer

Dette multi-agent workflow-system skaber en hotelrejseanbefalingstjeneste med to specialiserede agenter:

1. **FrontDesk Agent**: En rejseagent, der giver anbefalinger om aktiviteter og lokationer
2. **Concierge Agent**: Gennemgår anbefalingerne for at sikre autentiske, ikke-turistede oplevelser

Agenterne arbejder sammen i et workflow, hvor:
- FrontDesk-agenten modtager den indledende rejseanmodning
- Concierge-agenten gennemgår og forfiner anbefalingen
- Workflowet streamer svar i realtid

## Centrale Begreber

### Agent Koordinering
Eksemplet demonstrerer type-sikker agentkoordinering ved hjælp af Microsoft Agent Framework med validering ved kompileringstidspunktet.

### Workflow Orkestrering
Bruger deklarativ workflow-definition med .NET's asynkrone mønstre til at forbinde flere agenter i en pipeline.

### Streaming Svar
Implementerer realtidsstreaming af agentsvar ved hjælp af asynkrone enumerables og event-drevet arkitektur.

### Enterprise Integration
Viser produktionsklare mønstre, herunder:
- Konfiguration af miljøvariabler
- Sikker håndtering af legitimationsoplysninger
- Fejlhåndtering
- Asynkron eventbehandling

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.