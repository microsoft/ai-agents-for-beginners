# 🔍 Дослідження Microsoft Agent Framework - базовий агент (.NET)

## 📋 Цілі навчання

У цьому прикладі розглядаються основні концепції Microsoft Agent Framework через реалізацію базового агента на .NET. Ви дізнаєтеся основні агентські патерни і зрозумієте, як працюють інтелектуальні агенти під капотом за допомогою C# і екосистеми .NET.

### Що ви відкриєте для себе

- 🏗️ **Архітектура агента**: Розуміння базової структури AI агентів у .NET
- 🛠️ **Інтеграція інструментів**: Як агенти використовують зовнішні функції для розширення можливостей  
- 💬 **Потік розмови**: Управління багатокроковими розмовами та контекстом з керуванням потоками
- 🔧 **Патерни конфігурації**: Кращі практики налаштування та керування агентом у .NET

## 🎯 Основні розглянуті концепції

### Принципи агентської платформи

- **Автономність**: Як агенти приймають незалежні рішення за допомогою абстракцій AI у .NET
- **Реактивність**: Реагування на зміни в оточенні та введення користувача
- **Проактивність**: Ініціатива на основі цілей і контексту
- **Соціальна здатність**: Взаємодія через природну мову з потоками розмов

### Технічні компоненти

- **AIAgent**: Основне оркестрування агента та управління розмовами (.NET)
- **Функції інструментів**: Розширення можливостей агента методами та атрибутами C#
- **Інтеграція Azure OpenAI**: Використання мовних моделей через Azure OpenAI Responses API
- **Безпечна конфігурація**: Керування кінцевими точками на основі оточення

## 🔧 Технічний стек

### Основні технології

- Microsoft Agent Framework (.NET)
- Інтеграція Azure OpenAI (Responses API)
- Патерни клієнта Azure.AI.OpenAI
- Конфігурація на основі оточення з DotNetEnv

### Можливості агента

- Розуміння та генерація природної мови
- Виклик функцій та використання інструментів з атрибутами C#
- Відповіді з урахуванням контексту сесій розмов
- Розширювана архітектура з патернами впровадження залежностей

## 📚 Порівняння фреймворків

Цей приклад демонструє підхід Microsoft Agent Framework порівняно з іншими агентськими фреймворками:

| Особливість | Microsoft Agent Framework | Інші фреймворки |
|---------|-------------------------|------------------|
| **Інтеграція** | Рідна екосистема Microsoft | Різноманітна сумісність |
| **Простота** | Чистий, інтуїтивний API | Часто складне налаштування |
| **Розширюваність** | Легка інтеграція інструментів | Залежить від фреймворку |
| **Готовність для підприємств** | Створено для продакшену | Варіюється залежно від фреймворку |

## 🚀 Початок роботи

### Вимоги

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або вище
- Передплата [Azure](https://azure.microsoft.com/free/) з ресурсом Azure OpenAI та розгортанням моделі
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — увійдіть за допомогою `az login`

### Необхідні змінні середовища

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Потім увійдіть, щоб AzureCliCredential міг отримати токен
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
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

Або за допомогою dotnet CLI:

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

1. **Архітектура агента**: Microsoft Agent Framework забезпечує чистий, типобезпечний підхід до створення AI агентів у .NET
2. **Інтеграція інструментів**: Функції з атрибутами `[Description]` стають доступними інструментами для агента
3. **Контекст розмови**: Управління сесіями дозволяє вести багатокрокові розмови з повною обізнаністю про контекст
4. **Керування конфігурацією**: Змінні середовища та безпечне зберігання облікових даних відповідають кращим практикам .NET
5. **Azure OpenAI Responses API**: Агент використовує Azure OpenAI Responses API через SDK Azure.AI.OpenAI

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