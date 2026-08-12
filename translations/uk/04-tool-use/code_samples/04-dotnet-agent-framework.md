# 🛠️ Розширене використання інструментів з Azure OpenAI (Responses API) (.NET)

## 📋 Навчальні цілі

Цей блокнот демонструє шаблони інтеграції інструментів корпоративного рівня з використанням Microsoft Agent Framework у .NET з Azure OpenAI (Responses API). Ви навчитеся створювати складних агентів з кількома спеціалізованими інструментами, використовуючи сильну типізацію C# і можливості .NET для підприємств.

### Розвинені можливості інструментів, якими ви оволодієте

- 🔧 **Архітектура з кількома інструментами**: Створення агентів з кількома спеціалізованими можливостями
- 🎯 **Типобезпечне виконання інструментів**: Використання перевірки під час компіляції C#
- 📊 **Корпоративні шаблони інструментів**: Проєктування інструментів для робочого середовища і обробка помилок
- 🔗 **Композиція інструментів**: Комбінування інструментів для складних бізнес-процесів

## 🎯 Переваги архітектури інструментів у .NET

### Можливості інструментів для підприємств

- **Перевірка під час компіляції**: Сильна типізація забезпечує коректність параметрів інструментів
- **Впровадження залежностей**: Інтеграція контейнера IoC для керування інструментами
- **Патерни Async/Await**: Неблокуюче виконання інструментів з правильною обробкою ресурсів
- **Структуроване логування**: Вбудована інтеграція логування для моніторингу виконання інструментів

### Готові для виробництва шаблони

- **Обробка виключень**: Комплексне управління помилками з типізованими виключеннями
- **Управління ресурсами**: Коректні шаблони знищення і керування пам’яттю
- **Моніторинг продуктивності**: Вбудовані метрики та лічильники продуктивності
- **Управління конфігурацією**: Типобезпечна конфігурація з валідацією

## 🔧 Технічна архітектура

### Основні компоненти інструментів .NET

- **Microsoft.Extensions.AI**: Єдиний рівень абстракції інструментів
- **Microsoft.Agents.AI**: Оркестрування інструментів корпоративного рівня
- **Azure OpenAI (Responses API)**: Високопродуктивний клієнт API з пулом з’єднань

### Конвеєр виконання інструментів

```mermaid
graph LR
    A[Запит користувача] --> B[Аналіз агента]
    B --> C[Вибір інструменту]
    C --> D[Перевірка типу]
    B --> E[Прив’язка параметрів]
    E --> F[Виконання інструменту]
    C --> F
    F --> G[Обробка результату]
    D --> G
    G --> H[Відповідь]
```

## 🛠️ Категорії та шаблони інструментів

### 1. **Інструменти обробки даних**

- **Перевірка вхідних даних**: Сильна типізація з анотаціями даних
- **Операції трансформації**: Типобезпечне перетворення та форматування даних
- **Бізнес-логіка**: Інструменти для специфічних доменних розрахунків та аналізу
- **Форматування виводу**: Структуроване генерування відповідей

### 2. **Інтеграційні інструменти**

- **API конектори**: Інтеграція RESTful служб через HttpClient
- **Інструменти роботи з БД**: Інтеграція Entity Framework для доступу до даних
- **Файлові операції**: Безпечні операції з файловою системою з перевіркою
- **Зовнішні служби**: Шаблони інтеграції сторонніх сервісів

### 3. **Утиліти**

- **Обробка тексту**: Маніпуляції рядками та утиліти форматування
- **Операції з датами/часом**: Обчислення з урахуванням культури
- **Математичні інструменти**: Точні розрахунки та статистичні операції
- **Інструменти перевірки**: Валідація бізнес-правил і перевірка даних

Готові створювати агентів корпоративного рівня з потужними типобезпечними можливостями в .NET? Давайте спроєктуємо професійні рішення! 🏢⚡

## 🚀 Початок роботи

### Вимоги

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) або новіший
- Наявність [підписки Azure](https://azure.microsoft.com/free/) з ресурсом Azure OpenAI та розгортанням моделі
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — увійти за допомогою `az login`

### Необхідні змінні середовища

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Потім увійдіть, щоб AzureCliCredential міг отримати токен
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Потім увійдіть, щоб AzureCliCredential міг отримати токен
az login
```

### Приклад коду

Щоб запустити приклад коду,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Або використовуючи dotnet CLI:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Перегляньте [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) для повного коду.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

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
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
await using var session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
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