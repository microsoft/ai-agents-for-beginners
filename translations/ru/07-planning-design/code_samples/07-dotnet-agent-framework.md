# 🎯 Планирование и шаблоны проектирования с Azure OpenAI (API ответов) (.NET)

## 📋 Цели обучения

Эта записная книжка демонстрирует корпоративные шаблоны планирования и проектирования для создания интеллектуальных агентов с использованием Microsoft Agent Framework в .NET с Azure OpenAI (API ответов). Вы научитесь создавать агентов, которые могут разбирать сложные задачи, планировать многоступенчатые решения и выполнять сложные рабочие процессы с использованием корпоративных возможностей .NET.

## ⚙️ Требования и настройка

**Среда разработки:**
- .NET 9.0 SDK или выше
- Visual Studio 2022 или VS Code с расширением C#
- Подписка Azure с ресурсом Azure OpenAI и развертыванием модели
- Azure CLI — войдите с помощью `az login`

**Необходимые зависимости:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Конфигурация окружения (файл .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Запуск кода

В этом уроке реализовано одноречное приложение .NET Single File App. Для запуска:

```bash
# Сделайте файл исполняемым (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Запустите приложение
./07-dotnet-agent-framework.cs
```

Или используйте команду dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Реализация кода

Полная реализация доступна в `07-dotnet-agent-framework.cs`, которая демонстрирует:

- Загрузку конфигурации окружения с помощью DotNetEnv
- Настройку клиента Azure OpenAI и создание AI-агента с помощью `GetChatClient().AsAIAgent()`
- Определение структурированных моделей данных (Plan и TravelPlan) с сериализацией в JSON
- Создание AI-агента с структурированным выводом с использованием JSON-схемы
- Выполнение запросов планирования с типобезопасными ответами

## Основные понятия

### Структурированное планирование с типобезопасными моделями

Агент использует классы C# для определения структуры вывода планирования:

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

### JSON-схема для структурированных ответов

Агент настроен возвращать ответы, соответствующие схеме TravelPlan:

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

### Инструкции для агента планирования

Агент действует как координатор, делегируя задачи специализированным под-агентам:

- FlightBooking: для бронирования авиабилетов и предоставления информации о рейсах
- HotelBooking: для бронирования отелей и предоставления информации об отелях
- CarRental: для аренды автомобилей и предоставления информации об аренде авто
- ActivitiesBooking: для бронирования мероприятий и предоставления информации о мероприятиях
- DestinationInfo: для предоставления информации о направлениях
- DefaultAgent: для обработки общих запросов

## Ожидаемый результат

При запуске агента с запросом на планирование путешествия он проанализирует запрос и сгенерирует структурированный план с соответствующим распределением задач между специализированными агентами, отформатированный в JSON в соответствии со схемой TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->