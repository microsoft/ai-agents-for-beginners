# 🎯 Планирование и шаблоны проектирования с Azure OpenAI (Responses API) (.NET)

## 📋 Цели обучения

В этой тетрадке демонстрируются корпоративные шаблоны планирования и проектирования для создания интеллектуальных агентов с использованием Microsoft Agent Framework в .NET с Azure OpenAI (Responses API). Вы научитесь создавать агентов, способных разбирать сложные задачи, планировать многошаговые решения и выполнять сложные рабочие процессы с использованием корпоративных функций .NET.

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

**Конфигурация среды (.env файл):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## Запуск кода

В этом уроке реализовано приложение .NET Single File App. Чтобы запустить его:

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

Полная реализация доступна в файле `07-dotnet-agent-framework.cs`, который демонстрирует:

- Загрузку конфигурации среды с помощью DotNetEnv
- Конфигурирование клиента Azure OpenAI и создание AI агента с помощью `GetChatClient().AsAIAgent()`
- Определение структурированных моделей данных (Plan и TravelPlan) с сериализацией JSON
- Создание AI агента со структурированным выводом с использованием JSON схемы
- Выполнение запросов на планирование с типобезопасными ответами

## Ключевые понятия

### Структурированное планирование с типобезопасными моделями

Агент использует C# классы для определения структуры выходных данных планирования:

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

### JSON схема для структурированных выходных данных

Агент настроен на возврат ответов, соответствующих схеме TravelPlan:

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

Агент выступает в роли координатора, делегируя задачи специализированным подагентам:

- FlightBooking: для бронирования авиарейсов и предоставления информации о рейсах
- HotelBooking: для бронирования отелей и предоставления информации о них
- CarRental: для аренды автомобилей и предоставления информации об аренде
- ActivitiesBooking: для бронирования мероприятий и предоставления информации о них
- DestinationInfo: для предоставления информации о направлениях путешествий
- DefaultAgent: для обработки общих запросов

## Ожидаемый результат

При запуске агента с запросом на планирование поездки он проанализирует запрос и создаст структурированный план с соответствующими назначениями задач специализированным агентам в формате JSON, соответствующем схеме TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->