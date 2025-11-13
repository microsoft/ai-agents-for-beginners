<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcc874e190347bd6a095aed56dc16de8",
  "translation_date": "2025-11-13T14:44:29+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "uk"
}
-->
# 🎨 Агентні шаблони дизайну з моделями GitHub (.NET)

## 📋 Навчальні цілі

Цей приклад демонструє шаблони дизайну корпоративного рівня для створення інтелектуальних агентів за допомогою Microsoft Agent Framework у .NET з інтеграцією моделей GitHub. Ви дізнаєтеся про професійні шаблони та архітектурні підходи, які роблять агентів готовими до виробництва, зручними для обслуговування та масштабованими.

### Корпоративні шаблони дизайну

- 🏭 **Шаблон фабрики**: Стандартизоване створення агентів із використанням впровадження залежностей
- 🔧 **Шаблон будівельника**: Гнучка конфігурація та налаштування агентів
- 🧵 **Потокобезпечні шаблони**: Управління паралельними розмовами
- 📋 **Шаблон репозиторію**: Організоване управління інструментами та можливостями

## 🎯 Архітектурні переваги .NET

### Корпоративні функції

- **Сильна типізація**: Перевірка під час компіляції та підтримка IntelliSense
- **Впровадження залежностей**: Вбудована інтеграція контейнера DI
- **Управління конфігурацією**: Шаблони IConfiguration та Options
- **Async/Await**: Підтримка асинхронного програмування першого класу

### Шаблони, готові до виробництва

- **Інтеграція журналювання**: Підтримка ILogger та структурованого журналювання
- **Перевірка стану**: Вбудований моніторинг та діагностика
- **Перевірка конфігурації**: Сильна типізація з анотаціями даних
- **Обробка помилок**: Структуроване управління винятками

## 🔧 Технічна архітектура

### Основні компоненти .NET

- **Microsoft.Extensions.AI**: Уніфіковані абстракції AI-сервісів
- **Microsoft.Agents.AI**: Корпоративна структура оркестрації агентів
- **Інтеграція моделей GitHub**: Шаблони високопродуктивного API-клієнта
- **Система конфігурації**: Інтеграція appsettings.json та середовища

### Реалізація шаблонів дизайну

```mermaid
graph LR
    A[IServiceCollection] --> B[Agent Builder]
    B --> C[Configuration]
    C --> D[Tool Registry]
    D --> E[AI Agent]
```

## 🏗️ Демонстрація корпоративних шаблонів

### 1. **Шаблони створення**

- **Фабрика агентів**: Централізоване створення агентів із послідовною конфігурацією
- **Шаблон будівельника**: Гнучкий API для складної конфігурації агентів
- **Шаблон одиночки**: Управління спільними ресурсами та конфігурацією
- **Впровадження залежностей**: Слабке зв'язування та тестованість

### 2. **Поведінкові шаблони**

- **Шаблон стратегії**: Змінні стратегії виконання інструментів
- **Шаблон команди**: Інкапсульовані операції агентів із підтримкою скасування/повтору
- **Шаблон спостерігача**: Управління життєвим циклом агентів на основі подій
- **Шаблон методу шаблону**: Стандартизовані робочі процеси виконання агентів

### 3. **Структурні шаблони**

- **Шаблон адаптера**: Шар інтеграції API моделей GitHub
- **Шаблон декоратора**: Розширення можливостей агентів
- **Шаблон фасаду**: Спрощені інтерфейси взаємодії з агентами
- **Шаблон проксі**: Ліниве завантаження та кешування для підвищення продуктивності

## 📚 Принципи дизайну .NET

### Принципи SOLID

- **Єдина відповідальність**: Кожен компонент має одну чітку мету
- **Відкритість/закритість**: Розширюваність без модифікації
- **Замінність Лісков**: Реалізації інструментів на основі інтерфейсів
- **Розділення інтерфейсу**: Сфокусовані, узгоджені інтерфейси
- **Інверсія залежностей**: Залежність від абстракцій, а не конкретних реалізацій

### Чиста архітектура

- **Доменний шар**: Основні абстракції агентів та інструментів
- **Шар застосунку**: Оркестрація агентів та робочі процеси
- **Інфраструктурний шар**: Інтеграція моделей GitHub та зовнішніх сервісів
- **Шар презентації**: Взаємодія з користувачем та форматування відповідей

## 🔒 Корпоративні аспекти

### Безпека

- **Управління обліковими даними**: Безпечна обробка API-ключів за допомогою IConfiguration
- **Перевірка введення**: Сильна типізація та перевірка з анотаціями даних
- **Санітизація виводу**: Безпечна обробка та фільтрація відповідей
- **Журналювання аудиту**: Комплексне відстеження операцій

### Продуктивність

- **Асинхронні шаблони**: Неблокуючі операції вводу/виводу
- **Пулінг з'єднань**: Ефективне управління HTTP-клієнтами
- **Кешування**: Кешування відповідей для підвищення продуктивності
- **Управління ресурсами**: Правильна утилізація та очищення

### Масштабованість

- **Потокобезпека**: Підтримка паралельного виконання агентів
- **Пулінг ресурсів**: Ефективне використання ресурсів
- **Управління навантаженням**: Обмеження швидкості та обробка зворотного тиску
- **Моніторинг**: Метрики продуктивності та перевірка стану

## 🚀 Розгортання у виробництво

- **Управління конфігурацією**: Налаштування, специфічні для середовища
- **Стратегія журналювання**: Структуроване журналювання з ідентифікаторами кореляції
- **Обробка помилок**: Глобальна обробка винятків із належним відновленням
- **Моніторинг**: Application Insights та лічильники продуктивності
- **Тестування**: Шаблони модульного, інтеграційного та навантажувального тестування

Готові створювати інтелектуальних агентів корпоративного рівня з .NET? Давайте спроектуємо щось надійне! 🏢✨

## 🚀 Початок роботи

### Попередні вимоги

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або новіший
- [Токен доступу до API моделей GitHub](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### Необхідні змінні середовища

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```

```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```

### Приклад коду

Щоб запустити приклад коду,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Або за допомогою CLI dotnet:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Дивіться [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) для повного коду.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

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
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
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
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->