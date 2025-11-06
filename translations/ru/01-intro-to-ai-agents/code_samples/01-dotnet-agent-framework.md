# 🌍 AI Туристический Агент с Microsoft Agent Framework (.NET)

## 📋 Обзор сценария

Этот блокнот демонстрирует, как создать интеллектуального агента для планирования путешествий с использованием Microsoft Agent Framework для .NET. Агента можно использовать для автоматического создания персонализированных маршрутов однодневных поездок в случайные места по всему миру.

**Основные возможности:**
- 🎲 **Выбор случайного направления**: Использует пользовательский инструмент для выбора мест отдыха
- 🗺️ **Интеллектуальное планирование поездок**: Создает подробные маршруты по дням
- 🔄 **Потоковая передача в реальном времени**: Поддерживает как мгновенные, так и потоковые ответы
- 🛠️ **Интеграция пользовательских инструментов**: Демонстрирует, как расширить возможности агента

## 🔧 Техническая архитектура

### Основные технологии
- **Microsoft Agent Framework**: Последняя реализация .NET для разработки AI-агентов
- **Интеграция моделей GitHub**: Использует сервис вывода моделей AI от GitHub
- **Совместимость с OpenAI API**: Использует клиентские библиотеки OpenAI с пользовательскими конечными точками
- **Безопасная конфигурация**: Управление ключами API на основе окружения

### Основные компоненты
1. **AIAgent**: Основной оркестратор агента, который управляет потоком общения
2. **Пользовательские инструменты**: Функция `GetRandomDestination()`, доступная агенту
3. **Клиент чата**: Интерфейс общения, поддерживаемый моделями GitHub
4. **Поддержка потоковой передачи**: Возможности генерации ответов в реальном времени

### Схема интеграции
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 Начало работы

**Предварительные требования:**
- .NET 9.0 или выше
- Токен доступа к API моделей GitHub
- Переменные окружения, настроенные в файле `.env`

**Необходимые переменные окружения:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Запустите ячейки ниже по порядку, чтобы увидеть туристического агента в действии!

---

## .NET Single File App: AI Travel Agent Example

See `01-dotnet-agent-framework.cs` for the complete runnable code sample.

Запустите приведенный ниже пример кода:

```bash
dotnet run 01-dotnet-agent-framework.cs
```

### Sample Code

```csharp
static string GetRandomDestination()
{
    var destinations = new List<string>
    {
        "Paris, France",
        "Tokyo, Japan",
        "New York City, USA",
        "Sydney, Australia",
        "Rome, Italy",
        "Barcelona, Spain",
        "Cape Town, South Africa",
        "Rio de Janeiro, Brazil",
        "Bangkok, Thailand",
        "Vancouver, Canada"
    };
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Extract configuration from environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI Client Options
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Create AI Agent with Travel Planning Capabilities
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip (Non-Streaming)
Console.WriteLine(await agent.RunAsync("Plan me a day trip"));

// Execute Agent: Plan a Day Trip (Streaming Response)
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    Console.Write(update);
}
```
