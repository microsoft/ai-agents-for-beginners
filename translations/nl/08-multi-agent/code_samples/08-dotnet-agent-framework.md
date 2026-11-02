# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Leerdoelen

Deze notebook demonstreert hoe je geavanceerde multi-agent systemen van ondernemingskwaliteit bouwt met behulp van het Microsoft Agent Framework in .NET met Azure OpenAI (Responses API). Je leert hoe je meerdere gespecialiseerde agenten samenwerkt via gestructureerde workflows, waarbij je gebruikmaakt van de enterprise functies van .NET voor productieklare oplossingen.

**Enterprise Multi-Agent Mogelijkheden die je bouwt:**
- 👥 **Agent Samenwerking**: Type-veilige agent coördinatie met compile-time validatie
- 🔄 **Workflow Orkestratie**: Declaratieve workflowdefinitie met de async patronen van .NET
- 🎭 **Rol Specialisatie**: Sterk getypeerde agent persoonlijkheden en expertisedomeinen
- 🏢 **Enterprise Integratie**: Productieklaar met monitoring en foutafhandeling

## ⚙️ Vereisten & Setup

**Ontwikkelomgeving:**
- .NET 9.0 SDK of hoger
- Visual Studio 2022 of VS Code met C# extensie
- Azure-abonnement (voor persistente agenten)

**Benodigde NuGet-pakketten:**
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

## Code Voorbeeld

De volledige werkende code voor deze les is beschikbaar in het bijbehorende C# bestand: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Om het voorbeeld uit te voeren:

```bash
# Maak het bestand uitvoerbaar (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Voer het voorbeeld uit
./08-dotnet-agent-framework.cs
```

Of via de .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Wat dit voorbeeld demonstreert

Dit multi-agent workflow systeem creëert een hotelreis aanbevelingsservice met twee gespecialiseerde agenten:

1. **FrontDesk Agent**: Een reisagent die activiteiten- en locatie-aanbevelingen geeft
2. **Concierge Agent**: Beoordeelt aanbevelingen om authentieke, niet-toeristische ervaringen te garanderen

De agenten werken samen in een workflow waarbij:
- De FrontDesk agent de initiële reisaanvraag ontvangt
- De Concierge agent de aanbeveling beoordeelt en verfijnt
- De workflow responsen in realtime streamt

## Kernconcepten

### Agent Coördinatie
Het voorbeeld demonstreert type-veilige agent coördinatie met het Microsoft Agent Framework en compile-time validatie.

### Workflow Orkestratie
Gebruik van declaratieve workflowdefinitie met de async patronen van .NET om meerdere agenten in een pipeline te verbinden.

### Real-time Streaming Responsen
Implementeert realtime streaming van agentresponsen met async enumerables en event-gedreven architectuur.

### Enterprise Integratie
Toont productieklare patronen waaronder:
- Configuratie via omgevingsvariabelen
- Veilige credential management
- Foutafhandeling
- Asynchrone eventverwerking

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->