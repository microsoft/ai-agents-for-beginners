<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:39:53+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "bg"
}
-->
# 🔍 Изследване на агентни рамки - Основен агент (.NET)

## 📋 Цели на обучението

Този тетрадка разглежда основните концепции на Microsoft Agent Framework чрез имплементация на основен агент в .NET. Ще научите основни агентни модели и ще разберете как работят интелигентните агенти зад кулисите, използвайки C# и екосистемата на .NET.

**Какво ще откриете:**
- 🏗️ **Архитектура на агента**: Разбиране на основната структура на AI агенти в .NET
- 🛠️ **Интеграция на инструменти**: Как агентите използват външни функции за разширяване на възможностите  
- 💬 **Поток на разговори**: Управление на многократни разговори и контекст чрез управление на нишки
- 🔧 **Модели за конфигурация**: Най-добри практики за настройка и управление на агенти в .NET

## 🎯 Основни концепции

### Принципи на агентната рамка
- **Автономност**: Как агентите вземат независими решения, използвайки .NET AI абстракции
- **Реактивност**: Реагиране на промени в средата и входове от потребителя
- **Проактивност**: Инициатива, базирана на цели и контекст
- **Социална способност**: Взаимодействие чрез естествен език с нишки на разговори

### Технически компоненти
- **AIAgent**: Основна оркестрация на агента и управление на разговори (.NET)
- **Функции на инструменти**: Разширяване на възможностите на агента с методи и атрибути на C#
- **Интеграция с OpenAI**: Използване на езикови модели чрез стандартизирани .NET API
- **Управление на средата**: Сигурна конфигурация и управление на идентификационни данни с DotNetEnv

## ⚙️ Предварителни изисквания и настройка

**Необходими зависимости:**
- .NET 9.0 SDK или по-нова версия
- Visual Studio 2022 или VS Code с разширение за C#

**NuGet пакети:**
- `Microsoft.Extensions.AI` - Основни AI абстракции
- `Microsoft.Extensions.AI.OpenAI` - Интеграция с OpenAI (предварителна версия)
- `DotNetEnv` - Управление на променливи на средата

**Конфигурация на средата (.env файл):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Технически стек

**Основни технологии:**
- Microsoft Agent Framework (.NET)
- Интеграция с GitHub Models API
- Клиентски модели, съвместими с OpenAI
- Конфигурация, базирана на среда, с DotNetEnv

**Възможности на агента:**
- Разбиране и генериране на естествен език
- Извикване на функции и използване на инструменти с атрибути на C#
- Отговори, осъзнати за контекста, с нишки на разговори
- Разширяема архитектура с модели за внедряване на зависимости

## 📚 Сравнение на рамки

Този пример демонстрира подхода на Microsoft Agent Framework в .NET в сравнение с други платформи:

| Функция | .NET Agent Framework | Еквиваленти в Python |
|---------|---------------------|-------------------|
| **Типова безопасност** | Силно типизиране с C# | Динамично типизиране |
| **Интеграция** | Нативна екосистема на .NET | Разнообразна съвместимост |
| **Производителност** | Производителност на компилиран код | Интерпретирано изпълнение |
| **Готовност за предприятия** | Създаден за производствени .NET приложения | Зависи от рамката |
| **Инструменти** | Интеграция с Visual Studio | Зависи от IDE |

## 🚀 Започнете

Следвайте клетките по-долу, за да изградите своя първи основен агент в .NET и да разберете основните концепции на агентите!

## 📦 Инсталация и настройка

Този пример е наличен като изпълним .NET Single File App. Вижте придружаващия файл `02-dotnet-agent-framework.cs` за пълната имплементация.

За да изпълните този пример:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Или използвайки dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Разглеждане на кода

Пълната имплементация включва:

### 1. Зависимости на пакети

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```

### 2. Основни импорти

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Конфигурация на средата

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Дефиниция на функции на инструменти

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
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
    
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}
```

### 5. Настройка на конфигурация и клиент

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```

### 6. Конфигурация на агента

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```

### 7. Инициализация на агента

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```

### 8. Управление на разговори

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Основни изводи

1. **Архитектура на агента**: Microsoft Agent Framework предоставя чист, типово безопасен подход за изграждане на AI агенти в .NET
2. **Интеграция на инструменти**: Функции, декорирани с атрибути `[Description]`, стават достъпни инструменти за агента
3. **Контекст на разговори**: Управлението на нишки позволява многократни разговори с пълна осъзнатост за контекста
4. **Управление на конфигурация**: Променливите на средата и сигурното управление на идентификационни данни следват най-добрите практики на .NET
5. **Съвместимост с OpenAI**: Интеграцията с GitHub Models работи безпроблемно чрез съвместими с OpenAI API

## 🔗 Допълнителни ресурси

- [Документация на Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, произтичащи от използването на този превод.