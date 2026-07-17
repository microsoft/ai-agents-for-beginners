# 🎯 Načrtovanje in vzorci oblikovanja z Azure OpenAI (Responses API) (.NET)

## 📋 Cilji učenja

Ta zvezek prikazuje načrte in vzorce oblikovanja na ravni podjetja za izdelavo pametnih agentov z uporabo Microsoft Agent Framework v .NET z Azure OpenAI (Responses API). Naučili se boste ustvarjati agente, ki lahko razbijejo kompleksne probleme, načrtujejo večstopenjske rešitve in izvajajo zapletene poteke dela z uporabo podjetniških funkcij .NET.

## ⚙️ Zahteve in nastavitev

**Razvojno okolje:**
- .NET 9.0 SDK ali novejši
- Visual Studio 2022 ali VS Code s C# razširitvijo
- Azure naročnina z Azure OpenAI virom in namestitvijo modela
- Azure CLI — prijava z `az login`

**Zahtevane odvisnosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracija okolja (datoteka .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Zagon kode

Ta lekcija vsebuje izvedbo aplikacije .NET Single File App. Za zagon:

```bash
# Naredite datoteko izvedljivo (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Zaženite aplikacijo
./07-dotnet-agent-framework.cs
```

Ali uporabite ukaz dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Izvedba kode

Celotna izvedba je na voljo v `07-dotnet-agent-framework.cs`, kjer je prikazano:

- Nalaganje konfiguracije okolja z DotNetEnv
- Konfiguracija Azure OpenAI odjemalca in ustvarjanje AI agenta z `GetChatClient().AsAIAgent()`
- Definiranje strukturiranih podatkovnih modelov (Plan in TravelPlan) z JSON serializacijo
- Ustvarjanje AI agenta s strukturiranim izhodom z uporabo JSON sheme
- Izvajanje načrtovalskih zahtev z varnimi odgovori glede na tip

## Ključni pojmi

### Strukturirano načrtovanje z varnimi modeli

Agent uporablja C# razrede za definiranje strukture načrtovalnih izhodov:

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

### JSON shema za strukturirane izhode

Agent je nastavljen tako, da vrača odgovore, ki ustrezajo shemi TravelPlan:

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

### Navodila načrtovalnemu agentu

Agent deluje kot koordinator in delegira naloge specializiranim podagentom:

- FlightBooking: Za rezervacijo letov in zagotavljanje informacij o letih
- HotelBooking: Za rezervacijo hotelov in zagotavljanje informacij o hotelih
- CarRental: Za rezervacijo avtomobilov in zagotavljanje informacij o najemu avtomobilov
- ActivitiesBooking: Za rezervacijo aktivnosti in zagotavljanje informacij o aktivnostih
- DestinationInfo: Za zagotavljanje informacij o destinacijah
- DefaultAgent: Za obdelavo splošnih zahtev

## Pričakovani izhod

Ko zaženete agenta z zahtevo za načrtovanje potovanja, bo ta analiziral zahtevo in ustvaril strukturiran načrt z ustrezno dodelitvijo nalog specializiranim agentom, formatirano kot JSON, ki ustreza shemi TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->