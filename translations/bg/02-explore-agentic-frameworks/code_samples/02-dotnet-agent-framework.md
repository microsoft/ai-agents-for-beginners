# 🔍 Изследване на Microsoft Agent Framework - Базов агент (.NET)

## 📋 Учебни цели

Този пример изследва основните концепции на Microsoft Agent Framework чрез базова реализация на агент в .NET. Ще научите основни агентни модели и ще разберете как интелигентните агенти работят зад кулисите, използвайки C# и .NET екосистемата.

### Какво ще откриете

- 🏗️ **Архитектура на агента**: Разбиране на основната структура на AI агентите в .NET
- 🛠️ **Интеграция на инструменти**: Как агентите използват външни функции за разширяване на възможностите  
- 💬 **Поток на разговора**: Управление на многоходови разговори и контекст с управление на нишки  
- 🔧 **Патерни за конфигуриране**: Най-добри практики за настройка и управление на агенти в .NET  

## 🎯 Обхванати ключови концепции

### Принципи на агентската рамка

- **Автономност**: Как агентите взимат независими решения чрез AI абстракции в .NET  
- **Реактивност**: Реагиране на промени в околната среда и входове от потребителя  
- **Проактивност**: Поемане на инициатива въз основа на цели и контекст  
- **Социална способност**: Взаимодействие чрез естествен език с нишки на разговори  

### Технически компоненти

- **AIAgent**: Основна оркестрация на агента и управление на разговори (.NET)  
- **Функции на инструментите**: Разширяване на възможностите на агента с методи и атрибути на C#  
- **Интеграция с Azure OpenAI**: Използване на езиковите модели чрез Azure OpenAI Responses API  
- **Сигурна конфигурация**: Управление на крайни точки базирано на средата  

## 🔧 Технически стек

### Основни технологии

- Microsoft Agent Framework (.NET)  
- Интеграция с Azure OpenAI (Responses API)  
- Патерни за клиент Azure.AI.OpenAI  
- Конфигурация базирана на средата с DotNetEnv  

### Възможности на агента

- Разбиране и генериране на естествен език  
- Извикване на функции и използване на инструменти с атрибути на C#  
- Отговори с осъзнаване на контекст със сесии на разговор  
- Разширяема архитектура с патерни за внедряване на зависимости  

## 📚 Сравнение на рамки

Този пример демонстрира подхода на Microsoft Agent Framework в сравнение с други агентски рамки:

| Функция | Microsoft Agent Framework | Други рамки |
|---------|-------------------------|------------------|
| **Интеграция** | Нативна екосистема на Microsoft | Разнообразна съвместимост |
| **Леснота на използване** | Чист, интуитивен API | Често сложна настройка |
| **Разширяемост** | Лесна интеграция на инструменти | Зависещо от рамката |
| **Подходящо за предприятия** | Създаден за продукция | Варира според рамката |

## 🚀 Започване

### Предварителни изисквания

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или по-нова версия  
- [Абонамент в Azure](https://azure.microsoft.com/free/) с ресурс Azure OpenAI и разгръщане на модел  
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — влезте с `az login`  

### Изисквани променливи на средата

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# След това влезте, за да може AzureCliCredential да получи токен
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Влезте, за да може AzureCliCredential да получи токен
az login
```

### Примерен код

За да стартирате примерния код,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Или чрез dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Вижте [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) за пълния код.

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

## 🎓 Основни изводи

1. **Архитектура на агента**: Microsoft Agent Framework осигурява чист, типобезопасен подход за изграждане на AI агенти в .NET  
2. **Интеграция на инструменти**: Функции, декорирани с атрибути `[Description]`, стават достъпни инструменти за агента  
3. **Контекст на разговора**: Управлението на сесии позволява многоходови разговори с пълно осъзнаване на контекста  
4. **Управление на конфигурация**: Променливи на средата и сигурно боравене с удостоверения следват най-добрите практики на .NET  
5. **Azure OpenAI Responses API**: Агентът използва Azure OpenAI Responses API чрез Azure.AI.OpenAI SDK  

## 🔗 Допълнителни ресурси

- [Документация на Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)  
- [Azure OpenAI в Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->