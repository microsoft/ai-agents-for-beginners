# 🎯 Načrtovanje in oblikovalski vzorci z Azure OpenAI (Responses API) (.NET)

## 📋 Cilji učenja

Ta zvezek prikazuje načrte in oblikovalske vzorce na ravni podjetja za gradnjo inteligentnih agentov z uporabo Microsoft Agent Framework v .NET s Azure OpenAI (Responses API). Naučili se boste ustvarjati agente, ki lahko razdelijo kompleksne probleme, načrtujejo rešitve v več korakih in izvajajo zapletene delovne tokove s podjetniškimi funkcijami .NET.

## ⚙️ Zahteve in namestitev

**Razvojno okolje:**
- .NET 9.0 SDK ali novejši
- Visual Studio 2022 ali VS Code z razširitvijo za C#
- Naročnina na Azure z viri Azure OpenAI in nameščeno modelno instanco
- Azure CLI — prijava z `az login`

**Zahtevane odvisnosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracija okolja (datoteka .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Zagon kode

Ta lekcija vsebuje .NET aplikacijo v eni datoteki. Za zagon:

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

Celotna izvedba je na voljo v `07-dotnet-agent-framework.cs`, ki prikazuje:

- Nalaganje konfiguracije okolja z DotNetEnv
- Konfiguriranje Azure OpenAI odjemalca za Responses API
- Definiranje strukturiranih modelov podatkov (Plan in TravelPlan) z JSON seralizacijo
- Ustvarjanje AI agenta z strukturiranim izhodom preko JSON sheme
- Izvajanje načrtovalnih zahtevkov z vrsto-varnimi odgovori

## Ključni pojmi

### Strukturirano načrtovanje z vrsto-varnimi modeli

Agent uporablja C# razrede za definiranje strukture izhodov načrtovanja:

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

Agent je konfiguriran za vračanje odgovorov, ki ustrezajo shemi TravelPlan:

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

### Navodila za načrtovalnega agenta

Agent deluje kot koordinator in delegira naloge specializiranim podagentom:

- FlightBooking: za rezerviranje letov in posredovanje informacij o letih
- HotelBooking: za rezervacijo hotelov in posredovanje informacij o hotelih
- CarRental: za najem vozil in posredovanje informacij o najemu avtomobilov
- ActivitiesBooking: za rezervacijo aktivnosti in posredovanje informacij o dejavnostih
- DestinationInfo: za posredovanje informacij o destinacijah
- DefaultAgent: za obravnavo splošnih zahtevkov

## Pričakovani izhod

Ko zaženete agenta z zahtevkom za načrtovanje potovanja, bo analiziral zahtevo in ustvaril strukturiran načrt z ustrezno dodelitvijo nalog specializiranim agentom, oblikovan kot JSON, ki ustreza shemi TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->