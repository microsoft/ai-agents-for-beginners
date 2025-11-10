<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:58:07+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "nl"
}
-->
# 🎯 Planning & Ontwerppatronen met GitHub-modellen (.NET)

## 📋 Leerdoelen

Dit notebook demonstreert planning en ontwerppatronen van ondernemingsniveau voor het bouwen van intelligente agenten met behulp van het Microsoft Agent Framework in .NET met GitHub-modellen. Je leert agenten te maken die complexe problemen kunnen ontleden, oplossingen in meerdere stappen kunnen plannen en geavanceerde workflows kunnen uitvoeren met de enterprise-functies van .NET.

## ⚙️ Vereisten & Setup

**Ontwikkelomgeving:**
- .NET 9.0 SDK of hoger
- Visual Studio 2022 of VS Code met C#-extensie
- Toegang tot GitHub Models API

**Benodigde afhankelijkheden:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Omgevingsconfiguratie (.env-bestand):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Code uitvoeren

Deze les bevat een implementatie van een .NET Single File App. Om deze uit te voeren:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Of gebruik de dotnet run-opdracht:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Code-implementatie

De volledige implementatie is beschikbaar in `07-dotnet-agent-framework.cs`, waarin wordt gedemonstreerd:

- Het laden van omgevingsconfiguratie met DotNetEnv
- Het configureren van de OpenAI-client voor GitHub-modellen
- Het definiëren van gestructureerde datamodellen (Plan en TravelPlan) met JSON-serialisatie
- Het creëren van een AI-agent met gestructureerde output via JSON-schema
- Het uitvoeren van planningsverzoeken met type-veilige reacties

## Belangrijke concepten

### Gestructureerd plannen met type-veilige modellen

De agent gebruikt C#-klassen om de structuur van planningsoutputs te definiëren:

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

### JSON-schema voor gestructureerde outputs

De agent is geconfigureerd om reacties te retourneren die overeenkomen met het TravelPlan-schema:

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

### Instructies voor de planningsagent

De agent fungeert als coördinator en delegeert taken aan gespecialiseerde sub-agenten:

- FlightBooking: Voor het boeken van vluchten en het verstrekken van vluchtinformatie
- HotelBooking: Voor het boeken van hotels en het verstrekken van hotelinformatie
- CarRental: Voor het boeken van auto's en het verstrekken van autoverhuurinformatie
- ActivitiesBooking: Voor het boeken van activiteiten en het verstrekken van informatie over activiteiten
- DestinationInfo: Voor het verstrekken van informatie over bestemmingen
- DefaultAgent: Voor het afhandelen van algemene verzoeken

## Verwachte output

Wanneer je de agent uitvoert met een reisplanningsverzoek, zal deze het verzoek analyseren en een gestructureerd plan genereren met passende taaktoewijzingen aan gespecialiseerde agenten, geformatteerd als JSON dat voldoet aan het TravelPlan-schema.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.