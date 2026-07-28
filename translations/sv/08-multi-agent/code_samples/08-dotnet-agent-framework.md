# 🤝 Företags Multi-Agent Arbetsflödessystem (.NET)

## 📋 Läromål

Den här anteckningsboken visar hur man bygger sofistikerade företagsklassade multi-agent system med Microsoft Agent Framework i .NET med Azure OpenAI (Responses API). Du lär dig att orkestrera flera specialiserade agenter som samarbetar genom strukturerade arbetsflöden, och utnyttjar .NET:s företagsfunktioner för produktionsklara lösningar.

**Företags Multi-Agent Möjligheter Du Kommer Att Bygga:**
- 👥 **Agent-samarbete**: Typ-säker agentkoordinering med kompileringstid-validering
- 🔄 **Arbetsflödesorkestrering**: Deklarativ arbetsflödesdefinition med .NET:s async-mönster
- 🎭 **Rollspecialisering**: Stark typade agentpersonligheter och expertområden
- 🏢 **Företagsintegration**: Produktionsklara mönster med övervakning och felhantering

## ⚙️ Förutsättningar & Installation

**Utvecklingsmiljö:**
- .NET 9.0 SDK eller senare
- Visual Studio 2022 eller VS Code med C#-extension
- Azure-prenumeration (för permanenta agenter)

**Nödvändiga NuGet-paket:**
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

## Kodexempel

Den kompletta fungerande koden för denna lektion finns i bifogade C#-filen: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

För att köra exemplet:

```bash
# Gör filen körbar (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Kör exemplet
./08-dotnet-agent-framework.cs
```

Eller med .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Vad detta exempel visar

Det här multi-agent arbetsflödessystemet skapar en hotellrese-rekommendationstjänst med två specialiserade agenter:

1. **FrontDesk Agent**: En reseagent som ger rekommendationer om aktiviteter och platser
2. **Concierge Agent**: Granskar rekommendationerna för att säkerställa autentiska, icke-turistiga upplevelser

Agenterna samarbetar i ett arbetsflöde där:
- FrontDesk-agenten tar emot den initiala reseförfrågan
- Concierge-agenten granskar och förfinar rekommendationen
- Arbetsflödet strömmar svar i realtid

## Nyckelkoncept

### Agentkoordinering
Exemplet demonstrerar typ-säker agentkoordinering med Microsoft Agent Framework och kompileringstid-validering.

### Arbetsflödesorkestrering
Använder deklarativ arbetsflödesdefinition med .NET:s async-mönster för att koppla samman flera agenter i en pipeline.

### Strömmande svar
Implementerar realtidsströmning av agentsvar med async enumerables och händelsestyrd arkitektur.

### Företagsintegration
Visar produktionsklara mönster inklusive:
- Miljövariabelkonfiguration
- Säker hantering av autentiseringsuppgifter
- Felhantering
- Asynkron händelsebearbetning

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->