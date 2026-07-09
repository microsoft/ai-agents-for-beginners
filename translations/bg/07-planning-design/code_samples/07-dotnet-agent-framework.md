# 🎯 Планиране и дизайнерски шаблони с Azure OpenAI (Responses API) (.NET)

## 📋 Цели на обучението

Този бележник демонстрира корпоративни шаблони за планиране и дизайн за създаване на интелигентни агенти с помощта на Microsoft Agent Framework в .NET с Azure OpenAI (Responses API). Ще научите как да създавате агенти, които могат да разграждат сложни проблеми, да планират многоредови решения и да изпълняват сложни работни потоци с корпоративните функции на .NET.

## ⚙️ Предварителни изисквания и настройка

**Среда за разработка:**
- .NET 9.0 SDK или по-нова версия
- Visual Studio 2022 или VS Code с C# разширение
- Абонамент за Azure с ресурс Azure OpenAI и разгръщане на модел
- Azure CLI — влезте с `az login`

**Необходими зависимости:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Конфигурация на околната среда (.env файл):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Стартиране на кода

Този урок включва реализация на .NET Single File App. За да го стартирате:

```bash
# Направете файла изпълним (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Стартирайте приложението
./07-dotnet-agent-framework.cs
```

Или използвайте командата dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Реализация на кода

Пълната реализация е налична в `07-dotnet-agent-framework.cs`, която демонстрира:

- Зареждане на конфигурация на околната среда с DotNetEnv
- Конфигуриране на клиента Azure OpenAI за Responses API
- Дефиниране на структурирани модели за данни (Plan и TravelPlan) с JSON сериализация
- Създаване на AI агент със структуриран изход, използвайки JSON схема
- Изпълнение на заявки за планиране с типобезопасни отговори

## Основни концепции

### Структурирано планиране с типобезопасни модели

Агентът използва C# класове, за да дефинира структурата на плановите изходни данни:

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

### JSON схема за структурирани изходи

Агентът е конфигуриран да връща отговори, съответстващи на схемата TravelPlan:

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

### Инструкции за планиращия агент

Агентът действа като координатор, делегирайки задачи на специализирани подагенти:

- FlightBooking: За резервиране на полети и предоставяне на информация за полети
- HotelBooking: За резервации на хотели и предоставяне на информация за хотели
- CarRental: За наем на коли и предоставяне на информация за коли под наем
- ActivitiesBooking: За резервиране на активности и предоставяне на информация за активности
- DestinationInfo: За предоставяне на информация за дестинации
- DefaultAgent: За обработка на общи заявки

## Очакван изход

Когато стартирате агента с заявка за планиране на пътуване, той ще анализира заявката и ще генерира структуриран план с подходящо разпределение на задачи към специализирани агенти, форматиран като JSON, съответстващ на схемата TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->