# 🎯 Planlægning & Designmønstre med Azure OpenAI (Responses API) (.NET)

## 📋 Læringsmål

Denne notesbog demonstrerer virksomhedsgrade planlægnings- og designmønstre til opbygning af intelligente agenter ved hjælp af Microsoft Agent Framework i .NET med Azure OpenAI (Responses API). Du lærer at skabe agenter, som kan nedbryde komplekse problemer, planlægge flerstegs løsninger og udføre sofistikerede workflows med .NET's virksomhedsfeatures.

## ⚙️ Forudsætninger & Opsætning

**Udviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-udvidelsen
- Et Azure-abonnement med en Azure OpenAI-ressource og en modeludrulning
- Azure CLI — log ind med `az login`

**Nødvendige afhængigheder:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Miljøkonfiguration (.env-fil):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Kørsel af Koden

Denne lektion inkluderer en .NET single file app-implementering. For at køre den:

```bash
# Gør filen eksekverbar (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Kør applikationen
./07-dotnet-agent-framework.cs
```

Eller brug dotnet run-kommandoen:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kodeimplementering

Den komplette implementering findes i `07-dotnet-agent-framework.cs`, som demonstrerer:

- Indlæsning af miljøkonfiguration med DotNetEnv
- Konfiguration af Azure OpenAI-klienten og oprettelse af en AI-agent ved hjælp af `GetChatClient().AsAIAgent()`
- Definition af strukturerede datamodeller (Plan og TravelPlan) med JSON-serialisering
- Oprettelse af en AI-agent med struktureret output via JSON-skema
- Udførelse af planlægningsforespørgsler med typesikre svar

## Centrale Begreber

### Struktureret Planlægning med Typesikre Modeller

Agenten bruger C#-klasser til at definere strukturen af planlægningsresultater:

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

### JSON-skema for Strukturerede Output

Agenten er konfigureret til at returnere svar, som matcher TravelPlan-skemaet:

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

### Instruktioner til Planlægningsagenten

Agenten fungerer som en koordinator, der delegerer opgaver til specialiserede underagenter:

- FlightBooking: Til booking af flyrejser og levering af flyinformation
- HotelBooking: Til booking af hoteller og levering af hotelinformation
- CarRental: Til booking af biler og levering af billejeinformation
- ActivitiesBooking: Til booking af aktiviteter og levering af aktivitetsinformation
- DestinationInfo: Til levering af information om destinationer
- DefaultAgent: Til håndtering af generelle forespørgsler

## Forventet Output

Når du kører agenten med en rejseplanlægningsforespørgsel, vil den analysere forespørgslen og generere en struktureret plan med passende opgavefordeling til specialiserede agenter, formateret som JSON i overensstemmelse med TravelPlan-skemaet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->