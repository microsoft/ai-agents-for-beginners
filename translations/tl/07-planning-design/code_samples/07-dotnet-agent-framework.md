# 🎯 Pagpaplano at Mga Disenyo ng Pattern gamit ang Azure OpenAI (Responses API) (.NET)

## 📋 Mga Layunin sa Pagkatuto

Ipinapakita ng notebook na ito ang mga enterprise-grade na pagpaplano at disenyo ng pattern para sa pagbuo ng matatalinong mga ahente gamit ang Microsoft Agent Framework sa .NET kasama ang Azure OpenAI (Responses API). Matututuhan mong lumikha ng mga ahente na kayang hatiin ang mga komplikadong problema, magplano ng multi-step na mga solusyon, at magpatupad ng mga sopistikadong workflow gamit ang mga enterprise na tampok ng .NET.

## ⚙️ Mga Kinakailangan at Pag-setup

**Kapaligiran sa Pag-develop:**
- .NET 9.0 SDK o mas mataas pa
- Visual Studio 2022 o VS Code na may C# extension
- Isang Azure subscription na may Azure OpenAI resource at deployment ng modelo
- Ang Azure CLI — mag-sign in gamit ang `az login`

**Mga Kinakailangang Dependencies:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Pagkonpig ng Kapaligiran (.env file):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Pagsasagawa ng Code

Kasama sa leksyong ito ang isang .NET Single File App na implementasyon. Para patakbuhin ito:

```bash
# Gawing executable ang file (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Patakbuhin ang aplikasyon
./07-dotnet-agent-framework.cs
```

O gamitin ang dotnet run na utos:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Pagpapatupad ng Code

Ang buong implementasyon ay makikita sa `07-dotnet-agent-framework.cs`, na nagpapakita ng:

- Pag-load ng configuration ng kapaligiran gamit ang DotNetEnv
- Pagkonpig ng Azure OpenAI client para sa Responses API
- Pagdeklara ng mga structured data model (Plan at TravelPlan) gamit ang JSON serialization
- Paglikha ng AI agent na may structured output gamit ang JSON schema
- Pagsasagawa ng mga planning request na may type-safe na mga tugon

## Pangunahing Mga Konsepto

### Structured Planning gamit ang Type-Safe Models

Ginagamit ng agent ang mga klase ng C# para tukuyin ang istruktura ng mga output ng pagpaplano:

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

Nakakonpig ang agent upang magbalik ng mga tugon na tumutugma sa TravelPlan schema:

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

Gumaganap ang agent bilang tagapag-ugnay, na nagdedeliga ng mga gawain sa mga specialized na sub-agent:

- FlightBooking: Para sa pag-book ng mga flight at pagbibigay ng impormasyon tungkol sa flight
- HotelBooking: Para sa pag-book ng mga hotel at pagbibigay ng impormasyon tungkol sa hotel
- CarRental: Para sa pag-book ng mga sasakyan at pagbibigay ng impormasyon tungkol sa car rental
- ActivitiesBooking: Para sa pag-book ng mga aktibidad at pagbibigay ng impormasyon tungkol sa mga aktibidad
- DestinationInfo: Para sa pagbibigay ng impormasyon tungkol sa mga destinasyon
- DefaultAgent: Para sa paghawak ng mga pangkalahatang kahilingan

## Inaasahang Output

Kapag pinatakbo mo ang agent gamit ang isang kahilingan para sa pagpaplano ng paglalakbay, susuriin nito ang kahilingan at bubuo ng isang nakaayos na plano na may angkop na pagtatalaga ng mga gawain sa mga specialized na ahente, na naka-format bilang JSON na naaayon sa TravelPlan schema.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->