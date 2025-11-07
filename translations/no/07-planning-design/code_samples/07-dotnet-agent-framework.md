<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:57:50+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "no"
}
-->
# 🎯 Planlegging og designmønstre med GitHub-modeller (.NET)

## 📋 Læringsmål

Denne notatboken viser planleggings- og designmønstre på bedriftsnivå for å bygge intelligente agenter ved hjelp av Microsoft Agent Framework i .NET med GitHub-modeller. Du vil lære å lage agenter som kan dele opp komplekse problemer, planlegge løsninger i flere steg og utføre sofistikerte arbeidsflyter med .NETs enterprise-funksjoner.

## ⚙️ Forutsetninger og oppsett

**Utviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-utvidelse
- Tilgang til GitHub Models API

**Nødvendige avhengigheter:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Miljøkonfigurasjon (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Kjøre koden

Denne leksjonen inkluderer en .NET Single File App-implementering. For å kjøre den:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Eller bruk kommandoen dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kodeimplementering

Den komplette implementeringen er tilgjengelig i `07-dotnet-agent-framework.cs`, som demonstrerer:

- Laste inn miljøkonfigurasjon med DotNetEnv
- Konfigurere OpenAI-klient for GitHub-modeller
- Definere strukturerte datamodeller (Plan og TravelPlan) med JSON-serialisering
- Lage en AI-agent med strukturert output ved hjelp av JSON-skjema
- Utføre planleggingsforespørsler med type-sikre svar

## Nøkkelkonsepter

### Strukturert planlegging med type-sikre modeller

Agenten bruker C#-klasser for å definere strukturen til planleggingsutganger:

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

### JSON-skjema for strukturerte utganger

Agenten er konfigurert til å returnere svar som samsvarer med TravelPlan-skjemaet:

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

### Instruksjoner for planleggingsagenten

Agenten fungerer som en koordinator og delegerer oppgaver til spesialiserte underagenter:

- FlightBooking: For å bestille flyreiser og gi flyinformasjon
- HotelBooking: For å bestille hoteller og gi hotellinformasjon
- CarRental: For å bestille biler og gi bilutleieinformasjon
- ActivitiesBooking: For å bestille aktiviteter og gi aktivitetsinformasjon
- DestinationInfo: For å gi informasjon om destinasjoner
- DefaultAgent: For å håndtere generelle forespørsler

## Forventet resultat

Når du kjører agenten med en reiseplanleggingsforespørsel, vil den analysere forespørselen og generere en strukturert plan med passende oppgavefordeling til spesialiserte agenter, formatert som JSON som samsvarer med TravelPlan-skjemaet.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.