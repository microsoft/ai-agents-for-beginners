<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:59:57+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "hr"
}
-->
# 🎯 Planiranje i dizajnerski obrasci s GitHub modelima (.NET)

## 📋 Ciljevi učenja

Ovaj priručnik prikazuje planiranje i dizajnerske obrasce na razini poduzeća za izradu inteligentnih agenata koristeći Microsoft Agent Framework u .NET-u s GitHub modelima. Naučit ćete kako kreirati agente koji mogu razložiti složene probleme, planirati višekorake rješenja i izvršavati sofisticirane radne procese koristeći značajke .NET-a na razini poduzeća.

## ⚙️ Preduvjeti i postavljanje

**Razvojno okruženje:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code s C# ekstenzijom
- Pristup GitHub Models API-ju

**Potrebne ovisnosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracija okruženja (.env datoteka):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Pokretanje koda

Ova lekcija uključuje implementaciju .NET aplikacije u jednoj datoteci. Za pokretanje:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Ili koristite naredbu dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementacija koda

Kompletna implementacija dostupna je u `07-dotnet-agent-framework.cs`, koja prikazuje:

- Učitavanje konfiguracije okruženja s DotNetEnv
- Konfiguriranje OpenAI klijenta za GitHub modele
- Definiranje strukturiranih podatkovnih modela (Plan i TravelPlan) s JSON serializacijom
- Kreiranje AI agenta sa strukturiranim izlazom koristeći JSON shemu
- Izvršavanje zahtjeva za planiranje s tipiziranim odgovorima

## Ključni koncepti

### Strukturirano planiranje s tipiziranim modelima

Agent koristi C# klase za definiranje strukture izlaza planiranja:

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

### JSON shema za strukturirane izlaze

Agent je konfiguriran da vraća odgovore koji odgovaraju shemi TravelPlan:

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

### Upute za agenta za planiranje

Agent djeluje kao koordinator, delegirajući zadatke specijaliziranim pod-agentima:

- FlightBooking: Za rezervaciju letova i pružanje informacija o letovima
- HotelBooking: Za rezervaciju hotela i pružanje informacija o hotelima
- CarRental: Za rezervaciju automobila i pružanje informacija o najmu automobila
- ActivitiesBooking: Za rezervaciju aktivnosti i pružanje informacija o aktivnostima
- DestinationInfo: Za pružanje informacija o destinacijama
- DefaultAgent: Za rukovanje općim zahtjevima

## Očekivani izlaz

Kada pokrenete agenta s zahtjevom za planiranje putovanja, analizirat će zahtjev i generirati strukturirani plan s odgovarajućim dodjelama zadataka specijaliziranim agentima, formatiran kao JSON koji odgovara shemi TravelPlan.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.