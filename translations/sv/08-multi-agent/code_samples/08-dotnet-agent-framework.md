<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:16:42+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "sv"
}
-->
# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Inlärningsmål

Den här guiden visar hur man bygger avancerade företagsklassade multi-agent-system med Microsoft Agent Framework i .NET och GitHub-modeller. Du kommer att lära dig att orkestrera flera specialiserade agenter som samarbetar genom strukturerade arbetsflöden, och utnyttja .NET:s företagsfunktioner för produktionsklara lösningar.

**Funktioner för företagsklassade multi-agent-system som du kommer att bygga:**
- 👥 **Agent-samarbete**: Typ-säker agentkoordinering med validering vid kompilering
- 🔄 **Arbetsflödesorkestrering**: Deklarativ arbetsflödesdefinition med .NET:s asynkrona mönster
- 🎭 **Rollspecialisering**: Starkt typade agentpersonligheter och expertområden
- 🏢 **Företagsintegration**: Produktionsklara mönster med övervakning och felhantering

## ⚙️ Förutsättningar & Installation

**Utvecklingsmiljö:**
- .NET 9.0 SDK eller högre
- Visual Studio 2022 eller VS Code med C#-tillägg
- Azure-abonnemang (för persistenta agenter)

**Nödvändiga NuGet-paket:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Kodexempel

Den kompletta fungerande koden för denna lektion finns i den medföljande C#-filen: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

För att köra exemplet:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Eller med .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Vad detta exempel demonstrerar

Detta multi-agent arbetsflödessystem skapar en hotellrese-rekommendationstjänst med två specialiserade agenter:

1. **FrontDesk Agent**: En reseagent som ger aktivitets- och platsrekommendationer
2. **Concierge Agent**: Granskar rekommendationer för att säkerställa autentiska, icke-turistiska upplevelser

Agenterna samarbetar i ett arbetsflöde där:
- FrontDesk-agenten tar emot den initiala reseförfrågan
- Concierge-agenten granskar och förfinar rekommendationen
- Arbetsflödet strömmar svar i realtid

## Viktiga koncept

### Agentkoordinering
Exemplet demonstrerar typ-säker agentkoordinering med Microsoft Agent Framework och validering vid kompilering.

### Arbetsflödesorkestrering
Använder deklarativ arbetsflödesdefinition med .NET:s asynkrona mönster för att koppla flera agenter i en pipeline.

### Strömmande svar
Implementerar realtidsströmning av agentsvar med hjälp av asynkrona enumerables och händelsedriven arkitektur.

### Företagsintegration
Visar produktionsklara mönster inklusive:
- Konfiguration av miljövariabler
- Säker hantering av autentiseringsuppgifter
- Felhantering
- Asynkron händelsebearbetning

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.