<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:57:43+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "da"
}
-->
# 🎯 Planlægning & Designmønstre med GitHub-modeller (.NET)

## 📋 Læringsmål

Denne notebook demonstrerer planlægnings- og designmønstre på virksomhedsniveau til opbygning af intelligente agenter ved hjælp af Microsoft Agent Framework i .NET med GitHub-modeller. Du vil lære at skabe agenter, der kan nedbryde komplekse problemer, planlægge løsninger i flere trin og udføre avancerede arbejdsgange med .NET's virksomhedsfunktioner.

## ⚙️ Forudsætninger & Opsætning

**Udviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-udvidelse
- Adgang til GitHub Models API

**Nødvendige afhængigheder:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Miljøkonfiguration (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Kørsel af koden

Denne lektion inkluderer en .NET Single File App-implementering. For at køre den:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Eller brug dotnet run-kommandoen:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementering af kode

Den komplette implementering findes i `07-dotnet-agent-framework.cs`, som demonstrerer:

- Indlæsning af miljøkonfiguration med DotNetEnv
- Konfiguration af OpenAI-klient til GitHub-modeller
- Definition af strukturerede datamodeller (Plan og TravelPlan) med JSON-serialisering
- Oprettelse af en AI-agent med struktureret output ved hjælp af JSON-schema
- Udførelse af planlægningsanmodninger med type-sikre svar

## Centrale begreber

### Struktureret planlægning med type-sikre modeller

Agenten bruger C#-klasser til at definere strukturen af planlægningsoutput:

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

### JSON-schema til strukturerede outputs

Agenten er konfigureret til at returnere svar, der matcher TravelPlan-schemaet:

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

### Instruktioner til planlægningsagenten

Agenten fungerer som koordinator og delegerer opgaver til specialiserede underagenter:

- FlightBooking: Til booking af fly og levering af flyinformation
- HotelBooking: Til booking af hoteller og levering af hotelinformation
- CarRental: Til booking af biler og levering af biludlejningsinformation
- ActivitiesBooking: Til booking af aktiviteter og levering af aktivitetsinformation
- DestinationInfo: Til levering af information om destinationer
- DefaultAgent: Til håndtering af generelle forespørgsler

## Forventet output

Når du kører agenten med en rejseplanlægningsanmodning, vil den analysere anmodningen og generere en struktureret plan med passende opgavefordeling til specialiserede agenter, formateret som JSON, der overholder TravelPlan-schemaet.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.