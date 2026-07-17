# 🎯 Обрасци планирања и дизајна са Azure OpenAI (Responses API) (.NET)

## 📋 Циљеви учења

Овај нотебоок демонстрира обрасце планирања и дизајна у предузећу за изградњу интелигентних агената користећи Microsoft Agent Framework у .NET-у са Azure OpenAI (Responses API). Учићете како да креирате агенте који могу да разложе сложене проблеме, планирају више корака решења и извршавају софистициране токове послова са функцијама предузећа у .NET-у.

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

**Конфигурација окружења (.env датотека):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Покретање кода

Овај час укључује имплементацију .NET апликације у једном фајлу. Да бисте је покренули:

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

Потпуна имплементација доступна је у `07-dotnet-agent-framework.cs`, која демонстрира:

- Учитавање конфигурације окружења помоћу DotNetEnv
- Конфигурисање Azure OpenAI клијента и креирање AI агента користећи `GetChatClient().AsAIAgent()`
- Дефинисање структуираних модела података (Plan и TravelPlan) са JSON серијализацијом
- Креирање AI агента са структуираним излазом користећи JSON шему
- Извршавање захтева за планирање са типски безбедним одговорима

## Кључни појмови

### Структурирано планирање са моделима типски безбедним

Агент користи C# класе да дефинише структуру планираних резултата:

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

### JSON шема за структуиране излазе

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

### Упутства за агента за планирање

Агент делује као координатор, додељујући задатке специјализованим под-агентима:

- FlightBooking: За резервацију летова и пружање информација о летовима
- HotelBooking: За резервацију хотела и пружање информација о хотелима
- CarRental: За изнајмљивање аутомобила и пружање информација о изнајмљивању
- ActivitiesBooking: За резервацију активности и пружање информација о активностима
- DestinationInfo: За пружање информација о дестинацијама
- DefaultAgent: За руковање општим захтевима

## Очекивани излаз

Када покренете агента са захтевом за планирање путовања, он ће анализирати захтев и генерисати структуиран план са одговарајућом доделом задатака специјализованим агентима, форматиран као JSON који одговара TravelPlan шеми.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->