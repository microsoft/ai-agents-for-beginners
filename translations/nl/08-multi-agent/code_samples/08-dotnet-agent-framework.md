<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:17:16+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "nl"
}
-->
# 🤝 Enterprise Multi-Agent Workflow Systemen (.NET)

## 📋 Leerdoelen

Deze notebook laat zien hoe je geavanceerde multi-agent systemen van ondernemingsniveau kunt bouwen met het Microsoft Agent Framework in .NET en GitHub-modellen. Je leert meerdere gespecialiseerde agents te orkestreren die samenwerken via gestructureerde workflows, waarbij je gebruik maakt van de enterprise-functies van .NET voor productieklare oplossingen.

**Enterprise Multi-Agent Mogelijkheden die je zult bouwen:**
- 👥 **Agent Samenwerking**: Type-veilige coördinatie van agents met validatie tijdens compilatie
- 🔄 **Workflow Orchestratie**: Declaratieve workflowdefinitie met de async-patronen van .NET
- 🎭 **Rol Specialisatie**: Sterk getypeerde agent persoonlijkheden en expertisegebieden
- 🏢 **Enterprise Integratie**: Productieklaar met monitoring en foutafhandeling

## ⚙️ Vereisten & Setup

**Ontwikkelomgeving:**
- .NET 9.0 SDK of hoger
- Visual Studio 2022 of VS Code met C# extensie
- Azure-abonnement (voor persistente agents)

**Vereiste NuGet-pakketten:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Codevoorbeeld

De volledige werkende code voor deze les is beschikbaar in het bijbehorende C# bestand: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Om het voorbeeld uit te voeren:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Of gebruik de .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Wat Dit Voorbeeld Demonstreert

Dit multi-agent workflowsysteem creëert een hotelreisaanbevelingsservice met twee gespecialiseerde agents:

1. **FrontDesk Agent**: Een reisagent die activiteiten en locatieaanbevelingen biedt
2. **Concierge Agent**: Beoordeelt aanbevelingen om authentieke, niet-toeristische ervaringen te garanderen

De agents werken samen in een workflow waarin:
- De FrontDesk agent het initiële reisverzoek ontvangt
- De Concierge agent de aanbeveling beoordeelt en verfijnt
- De workflow reacties in real-time streamt

## Belangrijke Concepten

### Agent Coördinatie
Het voorbeeld demonstreert type-veilige coördinatie van agents met het Microsoft Agent Framework en validatie tijdens compilatie.

### Workflow Orchestratie
Maakt gebruik van declaratieve workflowdefinitie met de async-patronen van .NET om meerdere agents in een pijplijn te verbinden.

### Streaming Reacties
Implementeert real-time streaming van agentreacties met behulp van async enumerables en event-driven architectuur.

### Enterprise Integratie
Toont productieklare patronen, waaronder:
- Configuratie van omgevingsvariabelen
- Beveiligd beheer van inloggegevens
- Foutafhandeling
- Asynchrone verwerking van gebeurtenissen

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.