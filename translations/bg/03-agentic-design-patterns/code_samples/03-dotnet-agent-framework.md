# 🎨 Дизайнерски модели за агентска дейност с Azure OpenAI (Responses API) (.NET)

## 📋 Цели на обучението

Този пример демонстрира корпоративни дизайнерски модели за изграждане на интелигентни агенти, използващи Microsoft Agent Framework в .NET с интеграция на Azure OpenAI (Responses API). Ще научите професионални модели и архитектурни подходи, които правят агентите готови за продукция, поддържани и мащабируеми.

### Корпоративни дизайнерски модели

- 🏭 **Фабричен модел**: Стандартизирано създаване на агенти с внедряване на зависимости
- 🔧 **Builder модел**: Плавна конфигурация и настройка на агенти
- 🧵 **Потокобезопасни модели**: Конкурентно управление на разговори
- 📋 **Repository модел**: Организирано управление на инструменти и възможности

## 🎯 Архитектурни предимства специфични за .NET

### Корпоративни характеристики

- **Силно писане на типове**: Проверка при компилация и поддръжка на IntelliSense
- **Внедряване на зависимости**: Вградена интеграция на DI контейнер
- **Управление на конфигурация**: Патерни IConfiguration и Options
- **Async/Await**: Първокласна поддръжка за асинхронно програмиране

### Модели подходящи за продукция

- **Интеграция на логване**: Поддръжка на ILogger и структурирано логване
- **Проверки на здравето**: Вградено наблюдение и диагностика
- **Потвърждение на конфигурация**: Силно типизиране с анотации за данни
- **Обработка на грешки**: Структурирано управление на изключения

## 🔧 Техническа архитектура

### Основни .NET компоненти

- **Microsoft.Extensions.AI**: Единни абстракции за AI услуги
- **Microsoft.Agents.AI**: Корпоративна рамка за оркестрация на агенти
- **Azure OpenAI (Responses API)**: Високопроизводителни модели за API клиент
- **Система за конфигурация**: appsettings.json и интеграция с околна среда

### Имплементация на дизайнерски модели

```mermaid
graph LR
    A[IServiceCollection] --> B[Съставител на агенти]
    B --> C[Конфигурация]
    C --> D[Регистър на инструменти]
    D --> E[AI агент]
```

## 🏗️ Демонстрирани корпоративни модели

### 1. **Създаващи модели**

- **Agent Factory**: Централизирано създаване на агенти с консистентна конфигурация
- **Builder модел**: Плавен API за комплексна конфигурация на агенти
- **Singleton модел**: Общи ресурси и управление на конфигурация
- **Внедряване на зависимости**: Слаба свързаност и тестируемост

### 2. **Поведенчески модели**

- **Strategy модел**: Подменяеми стратегии за изпълнение на инструменти
- **Command модел**: Инкапсулирани операции на агент с undo/redo
- **Observer модел**: Упрaвление на жизнения цикъл на агента, базирано на събития
- **Template Method**: Стандартизирани работни потоци за изпълнение на агенти

### 3. **Структурни модели**

- **Adapter модел**: Интеграционен слой за Azure OpenAI (Responses API)
- **Decorator модел**: Усъвършенстване на възможностите на агента
- **Facade модел**: Оптимизирани потребителски интерфейси за взаимодействие с агента
- **Proxy модел**: Лениво зареждане и кеширане за повишаване на производителността

## 📚 Принципи на проектиране в .NET

### SOLID принципи

- **Единствена отговорност**: Всеки компонент има една ясна цел
- **Отворен/Затворен**: Разширяем без модификация
- **Заместител на Лисков**: Имплементации на инструменти базирани на интерфейс
- **Разделяне на интерфейси**: Фокусирани, кохерентни интерфейси
- **Инверсия на зависимости**: Зависимост от абстракции, а не от конкретни класове

### Чиста архитектура

- **Домейн слой**: Основни абстракции на агенти и инструменти
- **Пригоден слой**: Оркестрация на агенти и работни потоци
- **Инфраструктурен слой**: Интеграция с Azure OpenAI (Responses API) и външни услуги
- **Презентационен слой**: Взаимодействие с потребителя и форматиране на отговори

## 🔒 Корпоративни съображения

### Сигурност

- **Управление на удостоверения**: Сигурна обработка на API ключове с IConfiguration
- **Валидиция на вход**: Силно типизиране и проверка на анотации за данни
- **Очистка на изход**: Сигурна обработка и филтриране на отговори
- **Аудит логване**: Изчерпателно проследяване на операции

### Производителност

- **Асинхронни модели**: Неблокиращи I/O операции
- **Пул обслужване на връзки**: Ефективно управление на HTTP клиенти
- **Кеширане**: Кеширане на отговори за подобрена производителност
- **Управление на ресурси**: Коректно отстраняване и модели за почистване

### Мащабируемост

- **Потокобезопасност**: Поддръжка на конкурентно изпълнение на агенти
- **Пул на ресурси**: Ефективно използване на ресурси
- **Управление на натоварването**: Ограничаване на скоростта и обработка на обратно налягане
- **Наблюдение**: Метрики за производителност и проверки на здравето

## 🚀 Разгръщане в продукция

- **Управление на конфигурация**: Настройки специфични за околната среда
- **Логваща стратегия**: Структурирано логване с корелационни ID
- **Обработка на грешки**: Глобално обработване на изключения с правилно възстановяване
- **Наблюдение**: Информация за приложението и броячи на производителността
- **Тестване**: Модулни тестове, интеграционни тестове и модели за натоварване

Готови ли сте да изградите интелигентни агенти на корпоративно ниво с .NET? Нека проектираме нещо здраво! 🏢✨

## 🚀 За начало

### Предварителни условия

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или по-нова версия
- Абонамент в [Azure](https://azure.microsoft.com/free/) с ресурс Azure OpenAI и разгръщане на модел
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — влезте с `az login`

### Необходими променливи на околната среда

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
# След това влезте, за да може AzureCliCredential да получи токен
az login
```

### Примерен код

За да стартирате примерния код,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Или използвайки dotnet CLI:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Вижте [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) за пълния код.

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
var session = await agent.CreateSessionAsync();

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
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->