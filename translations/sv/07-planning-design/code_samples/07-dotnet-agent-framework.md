# 🎯 Planering och designmönster med Azure OpenAI (Responses API) (.NET)

## 📋 Lärandemål

Detta anteckningsbok visar företagsklassade planerings- och designmönster för att bygga intelligenta agenter med Microsoft Agent Framework i .NET med Azure OpenAI (Responses API). Du lär dig att skapa agenter som kan dela upp komplexa problem, planera flerstegs-lösningar och utföra sofistikerade arbetsflöden med .NET:s företagsfunktioner.

## ⚙️ Förutsättningar och installation

**Utvecklingsmiljö:**
- .NET 9.0 SDK eller senare
- Visual Studio 2022 eller VS Code med C#-tillägg
- En Azure-prenumeration med en Azure OpenAI-resurs och en modelldistribution
- Azure CLI — logga in med `az login`

**Nödvändiga beroenden:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Miljökonfiguration (.env-fil):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Köra koden

Denna lektion inkluderar en .NET Single File App-implementation. För att köra den:

```bash
# Gör filen körbar (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Kör applikationen
./07-dotnet-agent-framework.cs
```

Eller använd kommandot dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kodimplementation

Den kompletta implementeringen finns i `07-dotnet-agent-framework.cs`, som demonstrerar:

- Laddning av miljökonfiguration med DotNetEnv
- Konfigurering av Azure OpenAI-klienten för Responses API
- Definiering av strukturerade datamodeller (Plan och TravelPlan) med JSON-serialisering
- Skapande av en AI-agent med strukturerad output med JSON-schema
- Utförande av planeringsförfrågningar med typ-säkra svar

## Nyckelkoncept

### Strukturerad planering med typ-säkra modeller

Agenten använder C#-klasser för att definiera strukturen för planeringsutdata:

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

### JSON-schema för strukturerad output

Agenten är konfigurerad att returnera svar som överensstämmer med TravelPlan-schemat:

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

### Instruktioner för planeringsagenten

Agenten fungerar som en koordinator och delegerar uppgifter till specialiserade underagenter:

- FlightBooking: För bokning av flyg och tillhandahållande av flyginformation
- HotelBooking: För bokning av hotell och tillhandahållande av hotellinformation
- CarRental: För bokning av bilar och tillhandahållande av biluthyrningsinformation
- ActivitiesBooking: För bokning av aktiviteter och tillhandahållande av aktivitetsinformation
- DestinationInfo: För att tillhandahålla information om destinationer
- DefaultAgent: För att hantera allmänna förfrågningar

## Förväntad output

När du kör agenten med en reseplaneringsförfrågan kommer den att analysera förfrågan och generera en strukturerad plan med lämpliga uppgiftsfördelningar till specialiserade agenter, formaterad som JSON i enlighet med TravelPlan-schemat.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->