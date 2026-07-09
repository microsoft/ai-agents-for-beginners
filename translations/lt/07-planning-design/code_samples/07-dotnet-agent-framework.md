# 🎯 Planavimas ir dizaino modeliai su Azure OpenAI (Responses API) (.NET)

## 📋 Mokymosi tikslai

Šiame užraše demonstruojami įmonės lygio planavimo ir dizaino modeliai intelektualių agentų kūrimui naudojant Microsoft Agent Framework .NET su Azure OpenAI (Responses API). Išmoksite kurti agentus, kurie gali suskaidyti sudėtingas problemas, planuoti kelių žingsnių sprendimus ir vykdyti sudėtingus darbo procesus su .NET įmonės funkcijomis.

## ⚙️ Pradiniai parametrai ir nustatymai

**Vystymo aplinka:**
- .NET 9.0 SDK arba naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu
- Azure prenumerata su Azure OpenAI resursu ir modelio diegimu
- Azure CLI — prisijungimas su `az login`

**Reikalingi priklausomybių paketai:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Aplinkos konfigūracija (.env failas):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Kodo paleidimas

Ši pamoka apima .NET vieno failo programos įgyvendinimą. Norėdami paleisti:

```bash
# Padarykite failą vykdomu (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Paleiskite programą
./07-dotnet-agent-framework.cs
```

Arba naudokite dotnet run komandą:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kodo įgyvendinimas

Visas įgyvendinimas yra faile `07-dotnet-agent-framework.cs`, kuriame demonstruojama:

- Aplinkos konfigūracijos užkėlimas su DotNetEnv
- Azure OpenAI kliento konfigūravimas Responses API
- Struktūrizuotų duomenų modelių (Plan ir TravelPlan) apibrėžimas su JSON serializavimu
- AI agento kūrimas su struktūrizuotu išvestimi naudojant JSON schemą
- Planavimo užklausų vykdymas su tipais saugiomis atsakymų struktūromis

## Pagrindinės sąvokos

### Struktūrizuotas planavimas su tipais saugiais modeliais

Agentas naudoja C# klases apibrėžti planavimo išvesties struktūrą:

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

### JSON schema struktūrizuotoms išvestims

Agentas yra konfigūruotas grąžinti atsakymus, atitinkančius TravelPlan schemą:

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

### Planavimo agento nurodymai

Agentas veikia kaip koordinatorius, deleguodamas užduotis specializuotiems sub-agentams:

- FlightBooking: Skrydžių užsakymui ir informacijos apie skrydžius teikimui
- HotelBooking: Viešbučių užsakymui ir informacijos apie viešbučius teikimui
- CarRental: Automobilių užsakymui ir informacijos apie automobilių nuomą teikimui
- ActivitiesBooking: Veiklų užsakymui ir informacijos apie veiklas teikimui
- DestinationInfo: Informacijos apie tikslus teikimui
- DefaultAgent: Bendrų užklausų tvarkymui

## Tikėtinas rezultatas

Paleidus agentą su kelionės planavimo užklausa, jis analizuos užklausą ir sukurs struktūrizuotą planą su tinkamu užduočių paskirstymu specializuotiems agentams, formatuotą kaip JSON, atitinkantį TravelPlan schemą.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->