# 🎯 Planlegging og designmønstre med Azure OpenAI (Responses API) (.NET)

## 📋 Læringsmål

Denne notatboken demonstrerer enterprise-klasse planleggings- og designmønstre for å bygge intelligente agenter ved bruk av Microsoft Agent Framework i .NET med Azure OpenAI (Responses API). Du vil lære å lage agenter som kan dekomponere komplekse problemer, planlegge flerstegs løsninger, og utføre sofistikerte arbeidsflyter med .NETs enterprise-funksjoner.

## ⚙️ Forutsetninger og oppsett

**Utviklingsmiljø:**
- .NET 9.0 SDK eller høyere
- Visual Studio 2022 eller VS Code med C#-utvidelse
- En Azure-abonnement med en Azure OpenAI-ressurs og modellutrulling
- Azure CLI — logg inn med `az login`

**Nødvendige avhengigheter:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Miljøkonfigurasjon (.env-fil):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Kjøre koden

Denne leksjonen inkluderer en .NET Single File App-implementering. For å kjøre den:

```bash
# Gjør filen kjørbar (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Kjør applikasjonen
./07-dotnet-agent-framework.cs
```

Eller bruk kommandoen dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kodeimplementering

Den komplette implementeringen er tilgjengelig i `07-dotnet-agent-framework.cs`, som demonstrerer:

- Laste miljøkonfigurasjon med DotNetEnv
- Konfigurere Azure OpenAI-klienten og lage en AI-agent ved bruk av `GetChatClient().AsAIAgent()`
- Definere strukturerte datamodeller (Plan og TravelPlan) med JSON-serialisering
- Lage en AI-agent med strukturert utdata ved bruk av JSON-skjema
- Utføre planleggingsforespørsler med typesikre responser

## Nøkkelbegreper

### Strukturert planlegging med typesikre modeller

Agenten bruker C#-klasser for å definere strukturen til planleggingsutdataene:

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

### JSON-skjema for strukturerte utdata

Agenten er konfigurert til å returnere svar som samsvarer med TravelPlan-skjemaet:

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

### Instruksjoner for planleggingsagenten

Agenten fungerer som koordinator og delegerer oppgaver til spesialiserte under-agenter:

- FlightBooking: For å bestille flyreiser og gi flyinformasjon
- HotelBooking: For å bestille hoteller og gi hotellinformasjon
- CarRental: For å bestille biler og gi informasjon om bilutleie
- ActivitiesBooking: For å bestille aktiviteter og gi aktivitetsinformasjon
- DestinationInfo: For å gi informasjon om destinasjoner
- DefaultAgent: For å håndtere generelle forespørsler

## Forventet resultat

Når du kjører agenten med en reiseplanleggingsforespørsel, vil den analysere forespørselen og generere en strukturert plan med passende oppgavefordeling til spesialiserte agenter, formatert som JSON som samsvarer med TravelPlan-skjemaet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->