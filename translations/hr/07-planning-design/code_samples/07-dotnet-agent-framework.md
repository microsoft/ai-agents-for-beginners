# 🎯 Obrasci planiranja i dizajna s Azure OpenAI (Responses API) (.NET)

## 📋 Ciljevi učenja

Ovaj bilježnik prikazuje obrasce planiranja i dizajna razine poduzeća za izgradnju inteligentnih agenata pomoću Microsoft Agent Frameworka u .NET-u s Azure OpenAI (Responses API). Naučit ćete kako stvoriti agente koji mogu dekonstruirati složene probleme, planirati višestepena rješenja i izvršavati složene tijekove rada koristeći enterprise značajke .NET-a.

## ⚙️ Preduvjeti i postavljanje

**Razvojno okruženje:**
- .NET 9.0 SDK ili noviji
- Visual Studio 2022 ili VS Code sa C# ekstenzijom
- Pretplata na Azure s Azure OpenAI resursom i rasporedom modela
- Azure CLI — prijavite se s `az login`

**Potrebe za ovisnostima:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracija okruženja (datoteka .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Pokretanje koda

Ova lekcija uključuje implementaciju .NET Single File App. Za pokretanje:

```bash
# Postavite datoteku kao izvršnu (Linux/macOS)
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
- Konfiguriranje Azure OpenAI klijenta i stvaranje AI agenta pomoću `GetChatClient().AsAIAgent()`
- Definiranje strukturiranih modela podataka (Plan i TravelPlan) s JSON serijalizacijom
- Stvaranje AI agenta sa strukturiranim izlazom koristeći JSON shemu
- Izvršavanje zahtjeva za planiranje s tipiziranim odgovorima

## Ključni pojmovi

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

Agent je konfiguriran da vraća odgovore koji odgovaraju TravelPlan shemi:

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

### Upute za planirajućeg agenta

Agent djeluje kao koordinator, delegirajući zadatke specijaliziranim pod-agentima:

- FlightBooking: Za rezervaciju letova i pružanje informacija o letovima
- HotelBooking: Za rezervaciju hotela i pružanje informacija o hotelima
- CarRental: Za najam automobila i pružanje informacija o najmu automobila
- ActivitiesBooking: Za rezervaciju aktivnosti i pružanje informacija o aktivnostima
- DestinationInfo: Za pružanje informacija o destinacijama
- DefaultAgent: Za rukovanje općim zahtjevima

## Očekivani izlaz

Kada pokrenete agenta s zahtjevom za planiranje putovanja, on će analizirati zahtjev i generirati strukturirani plan s odgovarajućim dodjelama zadataka specijaliziranim agentima, formatiran kao JSON koji slijedi TravelPlan shemu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->