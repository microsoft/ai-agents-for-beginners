# 🎯 Planeerimine ja disainimustrid Azure OpenAI-ga (Responses API) (.NET)

## 📋 Õpieesmärgid

See märkmik tutvustab ettevõtte tasemel planeerimis- ja disainimustreid nutikate agentide ehitamiseks, kasutades Microsoft Agent Frameworki .NET-is koos Azure OpenAI (Responses API)-ga. Õpite looma agente, kes suudavad lahutada keerukaid probleeme väiksemateks osadeks, planeerida mitmeastmelisi lahendusi ja teostada keerukaid töövooge .NET-i ettevõttefunktsioonidega.

## ⚙️ Nõuded ja seadistamine

**Arendus keskkond:**
- .NET 9.0 SDK või uuem
- Visual Studio 2022 või VS Code C# laiendusega
- Azure tellimus, millel on Azure OpenAI ressurss ja mudeli juurutus
- Azure CLI — logi sisse käsuga `az login`

**Nõutavad sõltuvused:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Keskkonna konfiguratsioon (.env fail):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Koodi käivitamine

See õppetund sisaldab .NET Single File App rakendust. Selle käivitamiseks:

```bash
# Tee fail käivitatavaks (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Käivita rakendus
./07-dotnet-agent-framework.cs
```

Või kasuta `dotnet run` käsku:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Koodi teostus

Täielik teostus on kättesaadav failis `07-dotnet-agent-framework.cs`, mis tutvustab:

- Keskkonna konfiguratsiooni laadimist DotNetEnv abil
- Azure OpenAI kliendi seadistamist Responses API jaoks
- Struktureeritud andmemudelite (Plan ja TravelPlan) määratlemist JSON serialiseerimisega
- AI agendi loomist struktureeritud väljundiga, kasutades JSON skeemi
- Planeerimis-päringute teostamist tüübikindlate vastustega

## Põhikontseptsioonid

### Struktureeritud planeerimine tüübikindlate mudelitega

Agent kasutab C# klasse planeerimise väljundi struktuuri määratlemiseks:

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

### JSON skeem struktureeritud väljundite jaoks

Agent on seadistatud tagastama vastuseid vastavalt TravelPlan skeemile:

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

Agent tegutseb koordinaatorina, määrates ülesandeid spetsialiseeritud alaagentidele:

- FlightBooking: lennupiletite broneerimiseks ja lennuinfo pakkumiseks
- HotelBooking: hotellide broneerimiseks ja info pakkumiseks
- CarRental: autorendi broneerimiseks ja info pakkumiseks
- ActivitiesBooking: tegevuste broneerimiseks ja info pakkumiseks
- DestinationInfo: sihtkohtade info pakkumiseks
- DefaultAgent: üldpäringute käsitlemiseks

## Oodatav väljund

Kui käivitate agendi reisi planeerimise päringuga, analüüsib see päringut ja genereerib struktureeritud plaani koos sobivate ülesannete määranguga spetsialiseeritud agentidele, vormindatuna JSON-ina, mis vastab TravelPlan skeemile.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->