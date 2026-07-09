# 🎨 Агентні шаблони проєктування з Azure OpenAI (Responses API) (.NET)

## 📋 Цілі навчання

Цей приклад демонструє корпоративні шаблони проєктування для створення інтелектуальних агентів із використанням Microsoft Agent Framework у .NET з інтеграцією Azure OpenAI (Responses API). Ви вивчите професійні шаблони та архітектурні підходи, які роблять агентів готовими до виробництва, підтримуваними та масштабованими.

### Корпоративні шаблони проєктування

- 🏭 **Factory Pattern**: Стандартизоване створення агентів з ін'єкцією залежностей
- 🔧 **Builder Pattern**: Покрокова конфігурація та налаштування агентів
- 🧵 **Thread-Safe Patterns**: Керування паралельними розмовами
- 📋 **Repository Pattern**: Організоване керування інструментами та можливостями

## 🎯 Архітектурні переваги .NET

### Корпоративні функції

- **Сильна типізація**: Валідація під час компіляції та підтримка IntelliSense
- **Ін'єкція залежностей**: Вбудована інтеграція DI контейнера
- **Керування конфігурацією**: Патерни IConfiguration і Options
- **Async/Await**: Першокласна підтримка асинхронного програмування

### Шаблони, готові до виробництва

- **Інтеграція логування**: Підтримка ILogger та структурованого логування
- **Перевірки стану**: Вбудований моніторинг і діагностика
- **Валідація конфігурації**: Сильна типізація з анотаціями даних
- **Обробка помилок**: Структуроване керування виключеннями

## 🔧 Технічна архітектура

### Основні компоненти .NET

- **Microsoft.Extensions.AI**: Уніфіковані абстракції AI-сервісів
- **Microsoft.Agents.AI**: Корпоративний фреймворк оркестрації агентів
- **Azure OpenAI (Responses API)**: Високопродуктивні патерни клієнтського API
- **Система конфігурації**: appsettings.json та інтеграція з оточенням

### Реалізація шаблонів проєктування

```mermaid
graph LR
    A[IServiceCollection] --> B[Конструктор агента]
    B --> C[Конфігурація]
    C --> D[Реєстр інструментів]
    D --> E[AI агент]
```

## 🏗️ Демонстрація корпоративних шаблонів

### 1. **Шаблони створення**

- **Agent Factory**: Централізоване створення агентів зі стабільною конфігурацією
- **Builder Pattern**: Fluent API для складної конфігурації агентів
- **Singleton Pattern**: Спільні ресурси та керування конфігурацією
- **Dependency Injection**: Слабке зв’язування та тестованість

### 2. **Поведінкові шаблони**

- **Strategy Pattern**: Змінні стратегії виконання інструментів
- **Command Pattern**: Інкапсульовані операції агента з undo/redo
- **Observer Pattern**: Подієво-орієнтоване керування життєвим циклом агента
- **Template Method**: Стандартизовані робочі потоки виконання агента

### 3. **Структурні шаблони**

- **Adapter Pattern**: Слой інтеграції Azure OpenAI (Responses API)
- **Decorator Pattern**: Розширення можливостей агентів
- **Facade Pattern**: Спрощені інтерфейси взаємодії агента
- **Proxy Pattern**: Ліниве завантаження та кешування для продуктивності

## 📚 Принципи проєктування .NET

### Принципи SOLID

- **Єдина відповідальність**: Кожен компонент має одну чітку мету
- **Відкритість/Закритість**: Розширюваність без модифікації
- **Підстановка Лісков**: Реалізації інструментів на основі інтерфейсів
- **Розділення інтерфейсів**: Сфокусовані, цілісні інтерфейси
- **Інверсія залежностей**: Залежність від абстракцій, а не від конкретики

### Чиста архітектура

- **Domain Layer**: Основні абстракції агентів та інструментів
- **Application Layer**: Оркестрація агента та робочі процеси
- **Infrastructure Layer**: Інтеграція Azure OpenAI (Responses API) та зовнішніх сервісів
- **Presentation Layer**: Взаємодія з користувачем та форматування відповідей

## 🔒 Корпоративні аспекти

### Безпека

- **Керування обліковими даними**: Безпечне опрацювання API-ключів з IConfiguration
- **Валідація введення**: Сильна типізація та валідація анотаціями даних
- **Санітизація виводу**: Безпечна обробка та фільтрація відповідей
- **Аудит логування**: Комплексне відстеження операцій

### Продуктивність

- **Асинхронні шаблони**: Неблокуючі операції введення/виведення
- **Пулінг з'єднань**: Ефективне керування HTTP-клієнтом
- **Кешування**: Кешування відповідей для покращення продуктивності
- **Керування ресурсами**: Правильне вивільнення і очищення ресурсів

### Масштабованість

- **Потокобезпечність**: Підтримка паралельного виконання агентів
- **Пулінг ресурсів**: Ефективне використання ресурсів
- **Керування навантаженням**: Обмеження частоти та керування зворотним тиском
- **Моніторинг**: Метрики продуктивності та перевірки стану

## 🚀 Виробниче розгортання

- **Керування конфігурацією**: Налаштування, специфічні для середовища
- **Стратегія логування**: Структуроване логування з кореляційними ідентифікаторами
- **Обробка помилок**: Глобальна обробка винятків з належним відновленням
- **Моніторинг**: Application Insights та лічильники продуктивності
- **Тестування**: Юніт-тести, інтеграційні тести та патерни навантажувального тестування

Готові створити інтелектуальних агентів корпоративного рівня з .NET? Давайте спроєктуємо щось надійне! 🏢✨

## 🚀 Початок роботи

### Вимоги

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або вище
- [Підписка Azure](https://azure.microsoft.com/free/) з ресурсом Azure OpenAI та розгортанням моделі
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — увійдіть за допомогою `az login`

### Необхідні змінні середовища

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Потім увійдіть, щоб AzureCliCredential міг отримати токен
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Потім увійдіть, щоб AzureCliCredential міг отримати токен
az login
```

### Приклад коду

Щоб запустити приклад коду,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Або за допомогою dotnet CLI:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Дивіться [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) для повного коду.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.13.1

using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using Azure.AI.OpenAI;
using Azure.Identity;

// Tool Function: Random Destination Generator
// This static method will be available to the agent as a callable tool
// The [Description] attribute helps the AI understand when to use this function
// This demonstrates how to create custom tools for AI agents
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // List of popular vacation destinations around the world
    // The agent will randomly select from these options
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

    // Generate random index and return selected destination
    // Uses System.Random for simple random selection
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
var AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
"Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?"

Always prioritize user preferences. If they mention a specific destination like "Bali" or "Paris," focus your planning on that location rather than suggesting alternatives.
""";

// Create AI Agent with Advanced Travel Planning Capabilities
// Get the Responses client for the deployment and create the AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->