# 🎯 Mga Pattern sa Pagpaplano at Disenyo gamit ang Azure OpenAI (Responses API) (.NET)

## 📋 Mga Layunin sa Pagkatuto

Ipinapakita ng notebook na ito ang mga enterprise-grade na pattern sa pagpaplano at disenyo para sa paggawa ng mga intelligent agents gamit ang Microsoft Agent Framework sa .NET kasama ang Azure OpenAI (Responses API). Matututuhan mong gumawa ng mga agent na kayang hatiin ang mga komplikadong problema, magplano ng multi-step na mga solusyon, at magpatupad ng sopistikadong mga workflows gamit ang mga enterprise na tampok ng .NET.

## ⚙️ Mga Kinakailangan at Pagsisimula

**Development Environment:**
- .NET 9.0 SDK o mas mataas pa
- Visual Studio 2022 o VS Code na may C# extension
- Isang Azure subscription na may Azure OpenAI resource at deployment ng modelo
- Ang Azure CLI — mag-sign in gamit ang `az login`

**Mga Kinakailangang Dependency:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Kumpigurasyon ng Kapaligiran (.env file):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Pagpatakbo ng Code

Kasama sa araling ito ang implementasyon ng .NET Single File App. Para patakbuhin ito:

```bash
# Gawing executable ang file (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Patakbuhin ang aplikasyon
./07-dotnet-agent-framework.cs
```

O gamitin ang dotnet run command:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Implementasyon ng Code

Ang kompletong implementasyon ay makikita sa `07-dotnet-agent-framework.cs`, na nagpapakita ng:

- Pag-load ng configuration ng kapaligiran gamit ang DotNetEnv
- Pag-configure ng Azure OpenAI client at paggawa ng AI agent gamit ang `GetChatClient().AsAIAgent()`
- Pagdeklara ng mga structured data model (Plan at TravelPlan) gamit ang JSON serialization
- Paglikha ng AI agent na may structured output gamit ang JSON schema
- Pagpapatupad ng mga plano ng request na may type-safe na mga sagot

## Mga Pangunahing Konsepto

### Structured na Pagpaplano gamit ang Type-Safe na Mga Models

Ginagamit ng agent ang mga klase sa C# upang tukuyin ang istruktura ng output ng pagpaplano:

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

Ang agent ay naka-configure upang magbalik ng mga tugon na tugma sa TravelPlan schema:

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

### Mga Tagubilin para sa Planning Agent

Gumaganap ang agent bilang coordinator, na nagdedelegate ng mga gawain sa mga specialized sub-agent:

- FlightBooking: Para sa pag-book ng mga flight at pagbibigay ng impormasyon tungkol sa mga flight
- HotelBooking: Para sa pag-book ng mga hotel at pagbibigay ng impormasyon tungkol sa mga hotel
- CarRental: Para sa pag-book ng mga kotse at pagbibigay ng impormasyon tungkol sa car rental
- ActivitiesBooking: Para sa pag-book ng mga aktibidad at pagbibigay ng impormasyon tungkol sa mga aktibidad
- DestinationInfo: Para sa pagbibigay ng impormasyon tungkol sa mga destinasyon
- DefaultAgent: Para sa paghawak ng mga pangkalahatang request

## Inaasahang Output

Kapag pinatakbo mo ang agent gamit ang request sa pagpaplano ng paglalakbay, susuriin nito ang kahilingan at gagawa ng isang structured na plano na may angkop na pagtatalaga ng mga gawain sa mga specialized agents, at naka-format bilang JSON na sumusunod sa TravelPlan schema.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->