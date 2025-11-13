<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T14:09:13+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "bg"
}
-->
# 🔍 Изследване на Microsoft Agent Framework - Основен агент (.NET)

## 📋 Цели на обучението

Този пример разглежда основните концепции на Microsoft Agent Framework чрез имплементация на основен агент в .NET. Ще научите основни модели на агентите и ще разберете как интелигентните агенти работят зад кулисите, използвайки C# и екосистемата на .NET.

### Какво ще откриете

- 🏗️ **Архитектура на агента**: Разбиране на основната структура на AI агентите в .NET
- 🛠️ **Интеграция на инструменти**: Как агентите използват външни функции за разширяване на възможностите  
- 💬 **Поток на разговори**: Управление на многократни разговори и контекст чрез управление на нишки
- 🔧 **Модели за конфигурация**: Най-добри практики за настройка и управление на агенти в .NET

## 🎯 Основни концепции

### Принципи на агентната рамка

- **Автономност**: Как агентите вземат независими решения, използвайки .NET AI абстракции
- **Реактивност**: Реагиране на промени в средата и входове от потребители
- **Проактивност**: Инициатива, базирана на цели и контекст
- **Социална способност**: Взаимодействие чрез естествен език с нишки на разговори

### Технически компоненти

- **AIAgent**: Основна оркестрация на агента и управление на разговори (.NET)
- **Функции на инструменти**: Разширяване на възможностите на агента с методи и атрибути на C#
- **Интеграция с OpenAI**: Използване на езикови модели чрез стандартизирани .NET API
- **Сигурна конфигурация**: Управление на API ключове, базирано на среда

## 🔧 Технически стек

### Основни технологии

- Microsoft Agent Framework (.NET)
- Интеграция с GitHub Models API
- Клиентски модели, съвместими с OpenAI
- Конфигурация, базирана на среда, с DotNetEnv

### Възможности на агента

- Разбиране и генериране на естествен език
- Извикване на функции и използване на инструменти с атрибути на C#
- Отговори, осъзнати за контекста, с нишки на разговори
- Разширяема архитектура с модели за внедряване на зависимости

## 📚 Сравнение на рамки

Този пример демонстрира подхода на Microsoft Agent Framework в сравнение с други рамки за агенти:

| Функция | Microsoft Agent Framework | Други рамки |
|---------|-------------------------|------------------|
| **Интеграция** | Нативна екосистема на Microsoft | Разнообразна съвместимост |
| **Простота** | Чист, интуитивен API | Често сложна настройка |
| **Разширяемост** | Лесна интеграция на инструменти | Зависима от рамката |
| **Готовност за предприятия** | Създаден за продукция | Варира според рамката |

## 🚀 Първи стъпки

### Предварителни изисквания

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или по-нова версия
- [GitHub Models API access token](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)

### Необходими променливи на средата

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

### Примерен код

За да изпълните примерния код,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Или използвайки dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Вижте [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) за пълния код.

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

## 🎓 Основни изводи

1. **Архитектура на агента**: Microsoft Agent Framework предоставя чист, типово безопасен подход за изграждане на AI агенти в .NET
2. **Интеграция на инструменти**: Функции, декорирани с атрибути `[Description]`, стават достъпни инструменти за агента
3. **Контекст на разговори**: Управлението на нишки позволява многократни разговори с пълна осведоменост за контекста
4. **Управление на конфигурация**: Променливи на средата и сигурно управление на идентификационни данни следват най-добрите практики на .NET
5. **Съвместимост с OpenAI**: Интеграцията с GitHub Models работи безпроблемно чрез API, съвместими с OpenAI

## 🔗 Допълнителни ресурси

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/agent-framework)
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->