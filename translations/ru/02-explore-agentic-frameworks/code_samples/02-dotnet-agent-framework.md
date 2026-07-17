# 🔍 Изучение Microsoft Agent Framework — базовый агент (.NET)

## 📋 Цели обучения

В этом примере рассматриваются основные концепции Microsoft Agent Framework через реализацию базового агента на .NET. Вы изучите ключевые агентские шаблоны и поймёте, как работают интеллектуальные агенты на практике с использованием C# и экосистемы .NET.

### Что вы узнаете

- 🏗️ **Архитектура агента**: понимание базовой структуры ИИ-агентов в .NET
- 🛠️ **Интеграция инструментов**: как агенты используют внешние функции для расширения возможностей  
- 💬 **Поток диалога**: управление многошаговыми диалогами и контекстом с помощью управления потоками
- 🔧 **Шаблоны конфигурации**: лучшие практики настройки и управления агентом в .NET

## 🎯 Основные рассмотренные понятия

### Принципы агентской архитектуры

- **Автономия**: как агенты принимают независимые решения с помощью абстракций ИИ в .NET
- **Реактивность**: ответ на изменения в окружении и вводы пользователя
- **Проактивность**: проявление инициативы на основе целей и контекста
- **Социальные способности**: взаимодействие через естественный язык в рамках диалоговых потоков

### Технические компоненты

- **AIAgent**: ядро оркестрации агента и управление диалогами (.NET)
- **Функции инструментов**: расширение возможностей агента с помощью методов и атрибутов C#
- **Интеграция Azure OpenAI**: использование языковых моделей через API ответов Azure OpenAI
- **Безопасная конфигурация**: управление конечными точками на основе окружения

## 🔧 Технический стек

### Основные технологии

- Microsoft Agent Framework (.NET)
- Интеграция Azure OpenAI (API ответов)
- Клиентские паттерны Azure.AI.OpenAI
- Конфигурация на основе окружения с помощью DotNetEnv

### Возможности агента

- Понимание и генерация естественного языка
- Вызов функций и использование инструментов с помощью атрибутов C#
- Ответы с учётом контекста в сессиях диалогов
- Расширяемая архитектура с паттернами внедрения зависимостей

## 📚 Сравнение фреймворков

В этом примере показан подход Microsoft Agent Framework в сравнении с другими агентскими фреймворками:

| Функция | Microsoft Agent Framework | Другие фреймворки |
|---------|-------------------------|------------------|
| **Интеграция** | Родная экосистема Microsoft | Разнообразная совместимость |
| **Простота** | Чистый, интуитивный API | Часто сложная настройка |
| **Расширяемость** | Простая интеграция инструментов | Зависит от фреймворка |
| **Готовность к корпоративному использованию** | Спроектировано для продакшена | Зависит от фреймворка |

## 🚀 Начало работы

### Требования

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или выше
- [Подписка Azure](https://azure.microsoft.com/free/) с ресурсом Azure OpenAI и развертыванием модели
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — войдите в систему через `az login`

### Необходимые переменные окружения

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Затем войдите в систему, чтобы AzureCliCredential мог получить токен
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Затем выполните вход, чтобы AzureCliCredential мог получить токен
az login
```

### Пример кода

Для запуска примера кода,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Или используя dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Смотрите [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) для полного кода.

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

## 🎓 Основные выводы

1. **Архитектура агента**: Microsoft Agent Framework обеспечивает чистый, типобезопасный подход к созданию ИИ-агентов на .NET
2. **Интеграция инструментов**: функции с атрибутами `[Description]` становятся доступными инструментами для агента
3. **Контекст диалогов**: управление сессиями позволяет вести многошаговые диалоги с полной осведомлённостью о контексте
4. **Управление конфигурацией**: переменные окружения и безопасная обработка учетных данных следуют лучшим практикам .NET
5. **API ответов Azure OpenAI**: агент использует API ответов Azure OpenAI через SDK Azure.AI.OpenAI

## 🔗 Дополнительные ресурсы

- [Документация Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI в Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->