# 🎯 Planning & Ontwerppatronen met Azure OpenAI (Responses API) (.NET)

## 📋 Leerdoelen

Deze notebook toont enterprise-grade planning- en ontwerppatronen voor het bouwen van intelligente agenten met het Microsoft Agent Framework in .NET met Azure OpenAI (Responses API). Je leert agenten te creëren die complexe problemen kunnen ontleden, meerstapsoplossingen kunnen plannen en geavanceerde workflows kunnen uitvoeren met de enterprise-functies van .NET.

## ⚙️ Vereisten & Setup

**Ontwikkelomgeving:**
- .NET 9.0 SDK of hoger
- Visual Studio 2022 of VS Code met C# extensie
- Een Azure-abonnement met een Azure OpenAI-resource en een modeldeployement
- De Azure CLI — aanmelden met `az login`

**Vereiste Afhankelijkheden:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Omgevingsconfiguratie (.env bestand):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Code Uitvoeren

Deze les bevat een .NET Single File App implementatie. Om deze uit te voeren:

```bash
# Maak het bestand uitvoerbaar (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Voer de applicatie uit
./07-dotnet-agent-framework.cs
```

Of gebruik de dotnet run opdracht:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Code Implementatie

De volledige implementatie is beschikbaar in `07-dotnet-agent-framework.cs`, waarin wordt gedemonstreerd:

- Het laden van omgevingsconfiguratie met DotNetEnv
- Het configureren van de Azure OpenAI client voor de Responses API
- Het definiëren van gestructureerde datamodellen (Plan en TravelPlan) met JSON-serialisatie
- Het creëren van een AI-agent met gestructureerde output via JSON-schema
- Het uitvoeren van planningsaanvragen met typeveilige antwoorden

## Kernconcepten

### Gestructureerde Planning met Typeveilige Modellen

De agent gebruikt C#-klassen om de structuur van planningsuitkomsten te definiëren:

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

### JSON Schema voor Gestructureerde Outputs

De agent is geconfigureerd om antwoorden terug te geven die overeenkomen met het TravelPlan-schema:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Planning Agent Instructies

De agent fungeert als coördinator, die taken delegeert aan gespecialiseerde subagenten:

- FlightBooking: Voor het boeken van vluchten en geven van vluchtinformatie
- HotelBooking: Voor het boeken van hotels en geven van hotelinformatie
- CarRental: Voor het boeken van auto's en geven van autoverhuurinformatie
- ActivitiesBooking: Voor het boeken van activiteiten en geven van activiteitinformatie
- DestinationInfo: Voor het geven van informatie over bestemmingen
- DefaultAgent: Voor het afhandelen van algemene verzoeken

## Verwachte Output

Wanneer je de agent uitvoert met een reisplanningsverzoek, zal deze het verzoek analyseren en een gestructureerd plan genereren met passende taaktoewijzingen aan gespecialiseerde agenten, geformatteerd als JSON volgens het TravelPlan-schema.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->