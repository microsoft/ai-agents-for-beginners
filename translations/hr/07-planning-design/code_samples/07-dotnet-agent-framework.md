# 🎯 Obrasci planiranja i dizajna s Azure OpenAI (Responses API) (.NET)

## 📋 Ciljevi učenja

Ovaj bilježnik prikazuje obrasce planiranja i dizajna poslovne razine za izgradnju inteligentnih agenata korištenjem Microsoft Agent Frameworka u .NET-u s Azure OpenAI (Responses API). Naučit ćete kako stvoriti agente koji mogu razložiti složene probleme, planirati višestepena rješenja i izvoditi sofisticirane radne tokove s poduzećnim značajkama .NET-a.

## ⚙️ Preduvjeti i postavljanje

**Razvojno okruženje:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code s C# ekstenzijom
- Pretplata na Azure s Azure OpenAI resursom i implementacijom modela
- Azure CLI — prijavite se pomoću `az login`

**Potrebne ovisnosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracija okruženja (.env datoteka):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Pokretanje koda

Ova lekcija uključuje .NET aplikaciju jedne datoteke. Za pokretanje:

```bash
# Napravite datoteku izvršnom (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Pokrenite aplikaciju
./07-dotnet-agent-framework.cs
```

Ili koristite naredbu dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementacija koda

Potpuna implementacija dostupna je u `07-dotnet-agent-framework.cs`, koja prikazuje:

- Učitavanje konfiguracije okruženja s DotNetEnv
- Konfiguriranje Azure OpenAI klijenta za Responses API
- Definiranje strukturiranih modela podataka (Plan i TravelPlan) s JSON serijalizacijom
- Izrada AI agenta sa strukturiranim izlazom koristeći JSON shemu
- Izvršavanje zahtjeva za planiranjem s tip-sigurnim odgovorima

## Ključni koncepti

### Strukturirano planiranje s tip-sigurnim modelima

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

### Upute za planirajućeg agenta

Agent djeluje kao koordinator, delegirajući zadatke specijaliziranim pod-agonima:

- FlightBooking: Za rezervaciju letova i pružanje informacija o letovima
- HotelBooking: Za rezervaciju hotela i pružanje informacija o hotelima
- CarRental: Za rezervaciju automobila i pružanje informacija o najmu vozila
- ActivitiesBooking: Za rezervaciju aktivnosti i pružanje informacija o aktivnostima
- DestinationInfo: Za pružanje informacija o destinacijama
- DefaultAgent: Za obradu općih zahtjeva

## Očekivani izlaz

Kad pokrenete agenta sa zahtjevom za planiranje putovanja, on će analizirati zahtjev i generirati strukturirani plan s odgovarajućim dodjelama zadataka specijaliziranim agentima, formatiran kao JSON koji odgovara shemi TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->