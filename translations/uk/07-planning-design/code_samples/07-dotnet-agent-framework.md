# 🎯 Планування та шаблони проєктування з Azure OpenAI (Responses API) (.NET)

## 📋 Мета навчання

Цей ноутбук демонструє корпоративного рівня шаблони планування та проєктування для створення інтелектуальних агентів за допомогою Microsoft Agent Framework у .NET з Azure OpenAI (Responses API). Ви навчитесь створювати агентів, які можуть розкладати складні задачі, планувати багатокрокові рішення та виконувати складні робочі процеси з корпоративними функціями .NET.

## ⚙️ Вимоги та налаштування

**Середовище розробки:**
- .NET 9.0 SDK або вище
- Visual Studio 2022 або VS Code з розширенням C#
- Підписка Azure з ресурсом Azure OpenAI та розгортанням моделі
- Azure CLI — увійдіть за допомогою `az login`

**Необхідні залежності:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Конфігурація середовища (.env файл):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Запуск коду

У цьому уроці є реалізація .NET Single File App. Щоб запустити її:

```bash
# Зробіть файл виконуваним (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Запустіть додаток
./07-dotnet-agent-framework.cs
```

Або використайте команду dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Реалізація коду

Повна реалізація доступна у `07-dotnet-agent-framework.cs`, де демонструється:

- Завантаження конфігурації середовища з DotNetEnv
- Налаштування клієнта Azure OpenAI та створення AI агента за допомогою `GetChatClient().AsAIAgent()`
- Визначення структурованих моделей даних (Plan та TravelPlan) з JSON серіалізацією
- Створення AI агента із структурованим виводом за допомогою JSON схеми
- Виконання запитів на планування з типобезпечними відповідями

## Ключові концепції

### Структуроване планування з типобезпечними моделями

Агент використовує класи C# для визначення структури вихідних даних планування:

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

Агент налаштовано на повернення відповідей, що відповідають схемі TravelPlan:

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

### Інструкції агента планування

Агент діє як координатор, делегуючи завдання спеціалізованим підагентам:

- FlightBooking: для бронювання авіарейсів та надання інформації про рейси
- HotelBooking: для бронювання готелів та надання інформації про готелі
- CarRental: для бронювання автомобілів та надання інформації про оренду автомобілів
- ActivitiesBooking: для бронювання активностей та надання інформації про активності
- DestinationInfo: для надання інформації про місця призначення
- DefaultAgent: для обробки загальних запитів

## Очікуваний результат

Коли ви запустите агента з запитом для планування подорожі, він проаналізує запит і сформує структурований план із відповідним розподілом завдань спеціалізованим агентам, відформатованим у вигляді JSON відповідно до схеми TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->