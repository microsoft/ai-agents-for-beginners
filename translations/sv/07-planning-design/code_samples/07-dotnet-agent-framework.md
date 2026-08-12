# 🎯 Planering & Designmönster med Azure OpenAI (Responses API) (.NET)

## 📋 Inlärningsmål

Denna anteckningsbok visar företagsklassade planerings- och designmönster för att bygga intelligenta agenter med Microsoft Agent Framework i .NET med Azure OpenAI (Responses API). Du kommer att lära dig att skapa agenter som kan dela upp komplexa problem, planera flerstegs-lösningar och utföra sofistikerade arbetsflöden med .NET:s företagsfunktioner.

## ⚙️ Förutsättningar & Installation

**Utvecklingsmiljö:**
- .NET 9.0 SDK eller senare
- Visual Studio 2022 eller VS Code med C#-tillägg
- Ett Azure-abonnemang med en Azure OpenAI-resurs och en modelldriftsättning
- Azure CLI — logga in med `az login`

**Nödvändiga beroenden:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Miljökonfiguration (.env-fil):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Köra Koden

Den här lektionen inkluderar en .NET Single File App-implementation. För att köra den:

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

## Kodimplementering

Den kompletta implementeringen finns i `07-dotnet-agent-framework.cs`, som demonstrerar:

- Ladda miljökonfiguration med DotNetEnv
- Konfigurera Azure OpenAI-klienten och skapa en AI-agent med `GetChatClient().AsAIAgent()`
- Definiera strukturerade datamodeller (Plan och TravelPlan) med JSON-serialisering
- Skapa en AI-agent med strukturerad utdata med JSON-schema
- Utföra planeringsförfrågningar med typsäkra svar

## Nyckelkoncept

### Strukturerad planering med typsäkra modeller

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

Agenten är konfigurerad att återvända svar som matchar TravelPlan-schemat:

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

### Instruktioner för planeringsagenten

Agenten agerar som en koordinator som delegerar uppgifter till specialiserade underagenter:

- FlightBooking: För att boka flyg och ge flyginformation
- HotelBooking: För att boka hotell och ge hotellsinformation
- CarRental: För att boka bilar och ge biluthyrningsinformation
- ActivitiesBooking: För att boka aktiviteter och ge aktivitetsinformation
- DestinationInfo: För att ge information om destinationer
- DefaultAgent: För att hantera allmänna förfrågningar

## Förväntad Utdata

När du kör agenten med en resa planeringsförfrågan kommer den analysera förfrågan och generera en strukturerad plan med lämpliga uppgiftsfördelningar till specialiserade agenter, formaterad som JSON som följer TravelPlan-schemat.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->