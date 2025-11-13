<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:00:15+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ru"
}
-->
# 🔍 Исследование Microsoft Agent Framework - Базовый агент (.NET)

## 📋 Цели обучения

Этот пример изучает основные концепции Microsoft Agent Framework через реализацию базового агента в .NET. Вы узнаете ключевые паттерны работы агентов и поймете, как интеллектуальные агенты функционируют на уровне C# и экосистемы .NET.

### Что вы узнаете

- 🏗️ **Архитектура агента**: Понимание базовой структуры AI-агентов в .NET
- 🛠️ **Интеграция инструментов**: Как агенты используют внешние функции для расширения возможностей  
- 💬 **Поток общения**: Управление многократными диалогами и контекстом с помощью управления потоками
- 🔧 **Паттерны конфигурации**: Лучшие практики настройки и управления агентами в .NET

## 🎯 Основные концепции

### Принципы агентного фреймворка

- **Автономность**: Как агенты принимают независимые решения, используя абстракции AI в .NET
- **Реактивность**: Реакция на изменения окружающей среды и пользовательские запросы
- **Проактивность**: Инициативные действия на основе целей и контекста
- **Социальные способности**: Взаимодействие через естественный язык с использованием потоков общения

### Технические компоненты

- **AIAgent**: Основная оркестрация агента и управление диалогами (.NET)
- **Функции инструментов**: Расширение возможностей агента с помощью методов и атрибутов C#
- **Интеграция OpenAI**: Использование языковых моделей через стандартизированные API .NET
- **Безопасная конфигурация**: Управление API-ключами на основе окружения

## 🔧 Технический стек

### Основные технологии

- Microsoft Agent Framework (.NET)
- Интеграция GitHub Models API
- Клиентские паттерны, совместимые с OpenAI
- Конфигурация на основе окружения с DotNetEnv

### Возможности агента

- Понимание и генерация естественного языка
- Вызов функций и использование инструментов с атрибутами C#
- Ответы с учетом контекста и потоков общения
- Расширяемая архитектура с паттернами внедрения зависимостей

## 📚 Сравнение фреймворков

Этот пример демонстрирует подход Microsoft Agent Framework в сравнении с другими агентными фреймворками:

| Функция | Microsoft Agent Framework | Другие фреймворки |
|---------|-------------------------|------------------|
| **Интеграция** | Родная экосистема Microsoft | Разнообразная совместимость |
| **Простота** | Чистый, интуитивно понятный API | Часто сложная настройка |
| **Расширяемость** | Легкая интеграция инструментов | Зависимость от фреймворка |
| **Готовность к предприятиям** | Разработан для продакшена | Зависит от фреймворка |

## 🚀 Начало работы

### Предварительные требования

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или выше
- [Токен доступа GitHub Models API](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### Необходимые переменные окружения

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

### Пример кода

Чтобы запустить пример кода,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Или используя CLI dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Смотрите [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) для полного кода.

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

## 🎓 Основные выводы

1. **Архитектура агента**: Microsoft Agent Framework предоставляет чистый, типобезопасный подход к созданию AI-агентов в .NET
2. **Интеграция инструментов**: Функции, декорированные атрибутами `[Description]`, становятся доступными инструментами для агента
3. **Контекст общения**: Управление потоками позволяет вести многократные диалоги с полным учетом контекста
4. **Управление конфигурацией**: Переменные окружения и безопасная обработка учетных данных соответствуют лучшим практикам .NET
5. **Совместимость с OpenAI**: Интеграция GitHub Models работает безупречно через совместимые с OpenAI API

## 🔗 Дополнительные ресурсы

- [Документация Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Marketplace GitHub Models](https://github.com/marketplace?type=models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->