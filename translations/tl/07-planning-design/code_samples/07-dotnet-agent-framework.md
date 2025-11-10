<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:58:46+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "tl"
}
-->
# 🎯 Pagpaplano at Mga Disenyo ng Pattern gamit ang GitHub Models (.NET)

## 📋 Mga Layunin sa Pag-aaral

Ipinapakita ng notebook na ito ang mga disenyo ng pattern at pagpaplano na pang-enterprise para sa paggawa ng mga intelligent agents gamit ang Microsoft Agent Framework sa .NET na may GitHub Models. Matutunan mong gumawa ng mga agent na kayang mag-decompose ng mga komplikadong problema, magplano ng mga solusyong multi-step, at magpatupad ng mga sopistikadong workflow gamit ang mga enterprise features ng .NET.

## ⚙️ Mga Kinakailangan at Setup

**Kapaligiran sa Pag-develop:**
- .NET 9.0 SDK o mas mataas
- Visual Studio 2022 o VS Code na may C# extension
- Access sa GitHub Models API

**Mga Kinakailangang Dependency:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konpigurasyon ng Kapaligiran (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Pagpapatakbo ng Code

Kasama sa araling ito ang isang .NET Single File App na implementasyon. Para patakbuhin ito:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

O gamitin ang utos na dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementasyon ng Code

Ang kumpletong implementasyon ay makikita sa `07-dotnet-agent-framework.cs`, na nagpapakita ng:

- Pag-load ng konpigurasyon ng kapaligiran gamit ang DotNetEnv
- Pag-configure ng OpenAI client para sa GitHub Models
- Pagde-define ng mga structured data model (Plan at TravelPlan) gamit ang JSON serialization
- Paglikha ng AI agent na may structured output gamit ang JSON schema
- Pagpapatupad ng mga planning request na may type-safe na mga tugon

## Mga Pangunahing Konsepto

### Structured Planning gamit ang Type-Safe Models

Gumagamit ang agent ng mga C# class para idefine ang istruktura ng mga planning output:

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

### JSON Schema para sa Structured Outputs

Ang agent ay naka-configure upang magbalik ng mga tugon na tumutugma sa TravelPlan schema:

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

### Mga Instruksyon para sa Planning Agent

Ang agent ay kumikilos bilang isang coordinator, na nag-aatas ng mga gawain sa mga espesyal na sub-agent:

- FlightBooking: Para sa pag-book ng mga flight at pagbibigay ng impormasyon sa flight
- HotelBooking: Para sa pag-book ng mga hotel at pagbibigay ng impormasyon sa hotel
- CarRental: Para sa pag-book ng mga kotse at pagbibigay ng impormasyon sa car rental
- ActivitiesBooking: Para sa pag-book ng mga aktibidad at pagbibigay ng impormasyon sa aktibidad
- DestinationInfo: Para sa pagbibigay ng impormasyon tungkol sa mga destinasyon
- DefaultAgent: Para sa paghawak ng mga pangkalahatang kahilingan

## Inaasahang Output

Kapag pinatakbo mo ang agent gamit ang isang travel planning request, susuriin nito ang kahilingan at gagawa ng isang structured na plano na may naaangkop na mga task assignment sa mga espesyal na agent, na naka-format bilang JSON na tumutugma sa TravelPlan schema.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.