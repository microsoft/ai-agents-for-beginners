# 🎯 Планирање и образци дизајна са Azure OpenAI (Responses API) (.NET)

## 📋 Циљеви учења

Овај нотебук демонстрира образце планирања и дизајна на нивоу предузећа за израду интелигентних агената користећи Microsoft Agent Framework у .NET-у са Azure OpenAI (Responses API). Научићете како да креирате агенте који могу да разложе сложене проблеме, испланирају вишестепена решења и изврше сложене токове рада користећи предузетничке могућности .NET-а.

## ⚙️ Захтеви и подешавање

**Развојно окружење:**
- .NET 9.0 SDK или новији
- Visual Studio 2022 или VS Code са C# екстензијом
- Azure претплата са Azure OpenAI ресурсом и имплементацијом модела
- Azure CLI — пријавите се са `az login`

**Потребне зависности:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Конфигурација окружења (.env фајл):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Покретање кода

Ова лекција укључује имплементацију .NET Single File апликације. Да бисте је покренули:

```bash
# Учини датотеку извршном (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Покрени апликацију
./07-dotnet-agent-framework.cs
```

Или користите команду dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Имплементација кода

Комплетна имплементација доступна је у `07-dotnet-agent-framework.cs`, која демонстрира:

- Учитавање конфигурације окружења помоћу DotNetEnv
- Конфигурисање Azure OpenAI клијента и креирање AI агента користећи `GetChatClient().AsAIAgent()`
- Дефинисање структурираних модела података (Plan и TravelPlan) са JSON серијализацијом
- Креирање AI агента са структурираним излазом користећи JSON шему
- Извршавање захтева за планирање са типски безбедним одговорима

## Кључни појмови

### Структурирано планирање са типски безбедним моделима

Агент користи C# класе за дефинисање структуре излаза планирања:

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

### JSON шема за структуриране излазне податке

Агент је конфигурисан да враћа одговоре који одговарају TravelPlan шеми:

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

### Упутства за агента планирања

Агент делује као координатор, додељујући задатке специјализованим подагентима:

- FlightBooking: За резервацију летова и пружање информација о летовима
- HotelBooking: За резервацију хотела и пружање информација о хотелима
- CarRental: За резервацију аутомобила и пружање информација о изнајмљивању
- ActivitiesBooking: За резервацију активности и пружање информација о активностима
- DestinationInfo: За пружање информација о дестинацијама
- DefaultAgent: За обраду општих захтева

## Очекујани резултат

Када покренете агента са захтевом за планирање путовања, он ће анализирати захтев и генерисати структурирани план са одговарајућим доделама задатака специјализованим агентима, форматиран као JSON који одговара TravelPlan шеми.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->