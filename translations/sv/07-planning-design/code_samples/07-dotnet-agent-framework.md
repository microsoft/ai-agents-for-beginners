<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:57:34+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "sv"
}
-->
# 🎯 Planering och designmönster med GitHub-modeller (.NET)

## 📋 Lärandemål

Den här notebooken demonstrerar företagsklassade planerings- och designmönster för att bygga intelligenta agenter med Microsoft Agent Framework i .NET med GitHub-modeller. Du kommer att lära dig att skapa agenter som kan bryta ner komplexa problem, planera lösningar i flera steg och utföra sofistikerade arbetsflöden med .NET:s företagsfunktioner.

## ⚙️ Förutsättningar och installation

**Utvecklingsmiljö:**
- .NET 9.0 SDK eller högre
- Visual Studio 2022 eller VS Code med C#-tillägg
- Åtkomst till GitHub Models API

**Nödvändiga beroenden:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Miljökonfiguration (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Köra koden

Den här lektionen inkluderar en .NET Single File App-implementation. För att köra den:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Eller använd kommandot dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kodimplementation

Den kompletta implementationen finns i `07-dotnet-agent-framework.cs`, som demonstrerar:

- Laddning av miljökonfiguration med DotNetEnv
- Konfigurering av OpenAI-klient för GitHub-modeller
- Definiering av strukturerade datamodeller (Plan och TravelPlan) med JSON-serialisering
- Skapande av en AI-agent med strukturerad output med hjälp av JSON-schema
- Utförande av planeringsförfrågningar med typ-säkra svar

## Viktiga koncept

### Strukturerad planering med typ-säkra modeller

Agenten använder C#-klasser för att definiera strukturen på planeringsutdata:

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

### JSON-schema för strukturerade utdata

Agenten är konfigurerad att returnera svar som matchar TravelPlan-schemat:

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

- FlightBooking: För att boka flyg och tillhandahålla flyginformation
- HotelBooking: För att boka hotell och tillhandahålla hotellinformation
- CarRental: För att boka bilar och tillhandahålla biluthyrningsinformation
- ActivitiesBooking: För att boka aktiviteter och tillhandahålla aktivitetsinformation
- DestinationInfo: För att tillhandahålla information om destinationer
- DefaultAgent: För att hantera allmänna förfrågningar

## Förväntad output

När du kör agenten med en reseplaneringsförfrågan kommer den att analysera förfrågan och generera en strukturerad plan med lämpliga uppgiftsfördelningar till specialiserade agenter, formaterad som JSON som följer TravelPlan-schemat.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.