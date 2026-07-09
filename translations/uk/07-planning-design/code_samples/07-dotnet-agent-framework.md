# 🎯 Планування та шаблони проектування з Azure OpenAI (Responses API) (.NET)

## 📋 Навчальні цілі

Цей ноутбук демонструє корпоративні підходи до планування та шаблонів проектування для створення інтелектуальних агентів, використовуючи Microsoft Agent Framework у .NET з Azure OpenAI (Responses API). Ви навчитесь створювати агентів, які можуть розкладати складні проблеми, планувати багатокрокові рішення та виконувати складні робочі процеси з використанням корпоративних функцій .NET.

## ⚙️ Необхідні умови та налаштування

**Середовище розробки:**
- .NET 9.0 SDK або новіша версія
- Visual Studio 2022 або VS Code з розширенням C#
- Підписка Azure з ресурсом Azure OpenAI та розгортанням моделі
- Azure CLI — увійдіть за допомогою `az login`

**Необхідні залежності:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Конфігурація середовища (.env файл):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Запуск коду

У цьому уроці реалізовано .NET Single File App. Для запуску:

```bash
# Зробіть файл виконуваним (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Запустіть застосунок
./07-dotnet-agent-framework.cs
```

Або використовуйте команду dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Реалізація коду

Повна реалізація доступна у файлі `07-dotnet-agent-framework.cs`, де демонструються:

- Завантаження конфігурації середовища за допомогою DotNetEnv
- Налаштування клієнта Azure OpenAI для Responses API
- Визначення структурованих моделей даних (Plan та TravelPlan) з сериалізацією JSON
- Створення агента AI зі структурованим виводом за допомогою JSON-схеми
- Виконання запитів планування з типобезпечними відповідями

## Ключові поняття

### Структуроване планування з типобезпечними моделями

Агент використовує класи C# для визначення структури виводу планування:

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

### JSON-схема для структурованого виводу

Агент налаштований повертати відповіді, що відповідають схемі TravelPlan:

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

### Інструкції для агента планування

Агент виступає як координатор, делегуючи завдання спеціалізованим під-агентам:

- FlightBooking: для бронювання авіарейсів та надання інформації про рейси
- HotelBooking: для бронювання готелів та надання інформації про готелі
- CarRental: для бронювання автомобілів та надання інформації про оренду автомобілів
- ActivitiesBooking: для бронювання активностей та надання інформації про активності
- DestinationInfo: для надання інформації про напрямки
- DefaultAgent: для обробки загальних запитів

## Очікуваний результат

Коли ви запустите агента з запитом на планування подорожі, він проаналізує запит і створить структурований план з відповідним розподілом завдань спеціалізованим агентам, відформатований у вигляді JSON, що відповідає схемі TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->