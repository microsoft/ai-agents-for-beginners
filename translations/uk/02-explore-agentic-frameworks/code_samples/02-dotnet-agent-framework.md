# 🔍 Дослідження Microsoft Agent Framework - Базовий агент (.NET)

## 📋 Навчальні цілі

Цей приклад досліджує основні концепції Microsoft Agent Framework через реалізацію базового агента на .NET. Ви дізнаєтесь основні патерни агентів та зрозумієте, як працюють інтелектуальні агенти за лаштунками, використовуючи C# та екосистему .NET.

### Що Ви відкриєте для себе

- 🏗️ **Архітектура Агента**: Розуміння базової структури ШІ агентів на .NET
- 🛠️ **Інтеграція інструментів**: Як агенти використовують зовнішні функції для розширення можливостей  
- 💬 **Потік розмови**: Управління багатокроковими розмовами та контекстом за допомогою керування потоками
- 🔧 **Патерни конфігурації**: Найкращі практики для налаштування та керування агентами на .NET

## 🎯 Ключові концепції, що розглядаються

### Принципи агентної платформи

- **Автономність**: Як агенти приймають незалежні рішення, використовуючи абстракції ШІ .NET
- **Реактивність**: Реагування на зміни середовища та введення користувача
- **Проактивність**: Ініціатива, що базується на цілях та контексті
- **Соціальна здатність**: Взаємодія через природну мову з нитками розмови

### Технічні компоненти

- **AIAgent**: Основна оркестрація агента та управління розмовами (.NET)
- **Функції інструментів**: Розширення можливостей агента через методи та атрибути C#
- **Інтеграція Azure OpenAI**: Використання мовних моделей через API відповідей Azure OpenAI
- **Безпечна конфігурація**: Керування кінцевими точками на основі середовища

## 🔧 Технічний стек

### Основні технології

- Microsoft Agent Framework (.NET)
- Інтеграція Azure OpenAI (API відповідей)
- Патерни клієнта Azure.AI.OpenAI
- Конфігурація на основі середовища з DotNetEnv

### Можливості агента

- Розуміння та генерація природної мови
- Виклики функцій та використання інструментів з атрибутами C#
- Відповіді з урахуванням контексту через сесії розмов
- Розширювана архітектура з патернами впровадження залежностей

## 📚 Порівняння фреймворків

Цей приклад демонструє підхід Microsoft Agent Framework у порівнянні з іншими агентними фреймворками:

| Особливість | Microsoft Agent Framework | Інші фреймворки |
|---------|-------------------------|------------------|
| **Інтеграція** | Рідна екосистема Microsoft | Різноманітна сумісність |
| **Простота** | Чистий, інтуїтивний API | Часто складне налаштування |
| **Розширюваність** | Легка інтеграція інструментів | Залежить від фреймворку |
| **Готовність до підприємств** | Створений для виробництва | Залежить від фреймворку |

## 🚀 Початок роботи

### Вимоги

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або новіша версія
- [Підписка Azure](https://azure.microsoft.com/free/) з ресурсом Azure OpenAI та розгортанням моделі
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — увійдіть за допомогою `az login`

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
# Потім увійдіть у систему, щоб AzureCliCredential міг отримати токен
az login
```

### Приклад коду

Щоб запустити приклад коду,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Або використовуючи dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Дивіться [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) для повного коду.

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

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

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

## 🎓 Основні висновки

1. **Архітектура агента**: Microsoft Agent Framework забезпечує чистий, типобезпечний підхід до створення ШІ агентів на .NET
2. **Інтеграція інструментів**: Функції, прикрашені атрибутами `[Description]`, стають доступними інструментами для агента
3. **Контекст розмови**: Управління сесіями дозволяє багатокрокові розмови з повним усвідомленням контексту
4. **Управління конфігурацією**: Змінні середовища та безпечне управління обліковими даними відповідають найкращим практикам .NET
5. **Azure OpenAI Responses API**: Агент використовує API відповідей Azure OpenAI через SDK Azure.AI.OpenAI

## 🔗 Додаткові ресурси

- [Документація Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI у Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->