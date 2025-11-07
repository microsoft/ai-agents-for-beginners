<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T10:00:57+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "et"
}
-->
# 🎯 Planeerimine ja disainimustrid GitHubi mudelitega (.NET)

## 📋 Õpieesmärgid

See märkmik tutvustab ettevõtte tasemel planeerimise ja disainimustreid intelligentsete agentide loomiseks, kasutades Microsoft Agent Frameworki .NET-is koos GitHubi mudelitega. Õpid looma agente, kes suudavad keerulisi probleeme lahendada, mitmeastmelisi lahendusi planeerida ja keerukaid töövooge täita, kasutades .NET-i ettevõtte funktsioone.

## ⚙️ Eeltingimused ja seadistamine

**Arenduskeskkond:**
- .NET 9.0 SDK või uuem
- Visual Studio 2022 või VS Code koos C# laiendusega
- Juurdepääs GitHubi mudelite API-le

**Nõutavad sõltuvused:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Keskkonna konfiguratsioon (.env fail):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Koodi käivitamine

See õppetund sisaldab .NET-i ühe faili rakenduse implementatsiooni. Selle käivitamiseks:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Või kasuta käsku dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Koodi implementatsioon

Täielik implementatsioon on saadaval failis `07-dotnet-agent-framework.cs`, mis demonstreerib:

- Keskkonna konfiguratsiooni laadimist DotNetEnv abil
- OpenAI kliendi seadistamist GitHubi mudelite jaoks
- Struktureeritud andmemudelite (Plan ja TravelPlan) määratlemist koos JSON-serialiseerimisega
- AI agendi loomist struktureeritud väljundiga, kasutades JSON-skeemi
- Planeerimispäringute täitmist tüübikindlate vastustega

## Põhimõisted

### Struktureeritud planeerimine tüübikindlate mudelitega

Agent kasutab C# klasse, et määratleda planeerimise väljundite struktuur:

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

### JSON-skeem struktureeritud väljundite jaoks

Agent on konfigureeritud tagastama vastuseid, mis vastavad TravelPlan skeemile:

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

### Planeerimisagendi juhised

Agent tegutseb koordinaatorina, delegeerides ülesandeid spetsialiseeritud alamagentidele:

- FlightBooking: Lennupiletite broneerimiseks ja lennuinfo pakkumiseks
- HotelBooking: Hotellide broneerimiseks ja hotellide info pakkumiseks
- CarRental: Autode broneerimiseks ja autorendi info pakkumiseks
- ActivitiesBooking: Tegevuste broneerimiseks ja tegevuste info pakkumiseks
- DestinationInfo: Sihtkohtade info pakkumiseks
- DefaultAgent: Üldiste päringute käsitlemiseks

## Oodatav väljund

Kui käivitate agendi reisiplaneerimise päringuga, analüüsib see päringut ja genereerib struktureeritud plaani, määrates sobivad ülesanded spetsialiseeritud agentidele. Väljund vormistatakse JSON-is, mis vastab TravelPlan skeemile.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.