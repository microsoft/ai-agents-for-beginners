# 🎯 Planning & Ontwerppatronen met Azure OpenAI (Responses API) (.NET)

## 📋 Leerdoelen

Deze notebook toont ondernemingsniveau planning en ontwerppatronen voor het bouwen van intelligente agenten met het Microsoft Agent Framework in .NET met Azure OpenAI (Responses API). Je leert agenten maken die complexe problemen kunnen ontleden, meerstapsoplossingen plannen en geavanceerde workflows uitvoeren met de enterprise-functies van .NET.

## ⚙️ Vereisten & Setup

**Ontwikkelomgeving:**
- .NET 9.0 SDK of hoger
- Visual Studio 2022 of VS Code met C# extensie
- Een Azure-abonnement met een Azure OpenAI-resource en een model-implementatie
- De Azure CLI — inloggen met `az login`

**Benodigde afhankelijkheden:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Omgevingsconfiguratie (.env-bestand):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Code Uitvoeren

Deze les bevat een .NET Single File App-implementatie. Om deze uit te voeren:

```bash
# Maak het bestand uitvoerbaar (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Voer de applicatie uit
./07-dotnet-agent-framework.cs
```

Of gebruik het dotnet run-commando:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Code Implementatie

De volledige implementatie is beschikbaar in `07-dotnet-agent-framework.cs`, welke demonstreert:

- Laden van omgevingsconfiguratie met DotNetEnv
- Configureren van de Azure OpenAI-client en het creëren van een AI-agent met `GetChatClient().AsAIAgent()`
- Definiëren van gestructureerde datamodellen (Plan en TravelPlan) met JSON-serialisatie
- Creëren van een AI-agent met gestructureerde output met JSON-schema
- Uitvoeren van planningsaanvragen met type-veilige reacties

## Kernconcepten

### Gestructureerde Planning met Type-veilige Modellen

De agent gebruikt C#-klassen om de structuur van planningsuitvoer te definiëren:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### JSON-schema voor Gestructureerde Uitvoer

De agent is geconfigureerd om reacties terug te geven die overeenkomen met het TravelPlan-schema:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Instructies voor de Planning Agent

De agent fungeert als coördinator en delegeert taken aan gespecialiseerde subagenten:

- FlightBooking: Voor het boeken van vluchten en het verstrekken van vluchtinformatie
- HotelBooking: Voor het boeken van hotels en het verstrekken van hotelinformatie
- CarRental: Voor het boeken van auto’s en het verstrekken van autoverhuur informatie
- ActivitiesBooking: Voor het boeken van activiteiten en het verstrekken van activiteiteninformatie
- DestinationInfo: Voor het verstrekken van informatie over bestemmingen
- DefaultAgent: Voor het afhandelen van algemene verzoeken

## Verwachte Uitvoer

Wanneer je de agent uitvoert met een reisschema-planningsverzoek, zal deze het verzoek analyseren en een gestructureerd plan genereren met passende taaktoewijzingen aan gespecialiseerde agenten, geformatteerd als JSON conform het TravelPlan-schema.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->