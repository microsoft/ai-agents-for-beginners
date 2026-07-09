# 🎯 Планирање и обрасци пројектовања са Azure OpenAI (Responses API) (.NET)

## 📋 Циљеви учења

Овај бележник приказује пословне обрасце планирања и пројектовања за изградњу интелигентних агената користећи Microsoft Agent Framework у .NET-у са Azure OpenAI (Responses API). Научићете како да креирате агенте који могу да раставе сложене проблеме, планирају решења у више корака и извршавају сложене токове рада користећи пословне функције .NET-а.

## ⚙️ Захтеви и подешавање

**Развојно окружење:**
- .NET 9.0 SDK или новији
- Visual Studio 2022 или VS Code са C# екстензијом
- Azure претплата са Azure OpenAI ресурсом и распоређеним моделом
- Azure CLI — пријавите се са `az login`

**Потребне зависности:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Конфигурација окружења (.env фајл):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Покретање кода

Ова лекција укључује имплементацију .NET апликације у једном фајлу. Да је покренете:

```bash
# Направите фајл извршним (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Покрените апликацију
./07-dotnet-agent-framework.cs
```

Или користите команду dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Имплементација кода

Комплетна имплементација доступна је у `07-dotnet-agent-framework.cs`, која демонстрира:

- Учитавање конфигурације окружења уз помоћ DotNetEnv
- Конфигурисање Azure OpenAI клијента за Responses API
- Дефинисање структурисаних модела података (Plan и TravelPlan) са JSON сериализацијом
- Креирање AI агента са структурисаним излазом користећи JSON шему
- Извршавање захтева за планирање са типски безбедним одговорима

## Кључни појмови

### Структурирано планирање са типски безбедним моделима

Агент користи C# класе за дефинисање структуре планираних резултата:

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

### JSON шема за структурисане излазне податке

Агент је конфигурисан да враћа одговоре који одговарају TravelPlan шеми:

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

### Упутства за агента за планирање

Агент делује као координатор, делегирајући задатке специјализованим под-агентима:

- FlightBooking: за резервацију летова и пружање информација о летовима
- HotelBooking: за резервацију хотела и пружање информација о хотелима
- CarRental: за изнајмљивање аутомобила и пружање информација о изнајмљивању возила
- ActivitiesBooking: за резервацију активности и пружање информација о активностима
- DestinationInfo: за пружање информација о дестинацијама
- DefaultAgent: за обраду општих захтева

## Очекивани излаз

Када покренете агента са захтевом за планирање путовања, он ће анализирати захтев и генерисати структурисани план са одговарајућим расподелама задатака специјализованим агентима, форматирано као JSON у складу са TravelPlan шемом.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->