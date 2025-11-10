<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T10:00:07+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "sl"
}
-->
# 🎯 Načrtovanje in vzorci oblikovanja z modeli GitHub (.NET)

## 📋 Cilji učenja

Ta zvezek prikazuje načrtovanje in vzorce oblikovanja na ravni podjetja za gradnjo inteligentnih agentov z uporabo Microsoft Agent Framework v .NET z modeli GitHub. Naučili se boste ustvariti agente, ki lahko razčlenijo kompleksne probleme, načrtujejo rešitve v več korakih in izvajajo sofisticirane delovne tokove z uporabo funkcij na ravni podjetja v .NET.

## ⚙️ Predpogoji in nastavitev

**Razvojno okolje:**
- .NET 9.0 SDK ali novejši
- Visual Studio 2022 ali VS Code z razširitvijo za C#
- Dostop do API-ja modelov GitHub

**Potrebne odvisnosti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguracija okolja (.env datoteka):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Zagon kode

Ta lekcija vključuje implementacijo aplikacije .NET Single File. Za zagon:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Ali uporabite ukaz dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementacija kode

Celotna implementacija je na voljo v `07-dotnet-agent-framework.cs`, ki prikazuje:

- Nalaganje konfiguracije okolja z DotNetEnv
- Konfiguriranje OpenAI odjemalca za modele GitHub
- Definiranje strukturiranih podatkovnih modelov (Plan in TravelPlan) z JSON serializacijo
- Ustvarjanje AI agenta s strukturiranim izhodom z uporabo JSON sheme
- Izvajanje načrtovalnih zahtev z odgovori, ki so varni glede na tip

## Ključni koncepti

### Strukturirano načrtovanje z modeli, varnimi glede na tip

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

Agent deluje kot koordinator, ki naloge delegira specializiranim pod-agentom:

- FlightBooking: Za rezervacijo letov in zagotavljanje informacij o letih
- HotelBooking: Za rezervacijo hotelov in zagotavljanje informacij o hotelih
- CarRental: Za rezervacijo avtomobilov in zagotavljanje informacij o najemu avtomobilov
- ActivitiesBooking: Za rezervacijo aktivnosti in zagotavljanje informacij o aktivnostih
- DestinationInfo: Za zagotavljanje informacij o destinacijah
- DefaultAgent: Za obravnavo splošnih zahtev

## Pričakovani izhod

Ko zaženete agenta z zahtevo za načrtovanje potovanja, bo analiziral zahtevo in ustvaril strukturiran načrt z ustreznimi dodelitvami nalog specializiranim agentom, formatiran kot JSON, ki ustreza shemi TravelPlan.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.