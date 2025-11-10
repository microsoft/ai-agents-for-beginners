<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:31:02+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ru"
}
-->
# 🔍 Исследование агентных фреймворков - Базовый агент (.NET)

## 📋 Цели обучения

Этот ноутбук изучает основные концепции Microsoft Agent Framework через реализацию базового агента в .NET. Вы узнаете ключевые агентные шаблоны и поймете, как работают интеллектуальные агенты на основе C# и экосистемы .NET.

**Что вы узнаете:**
- 🏗️ **Архитектура агента**: Понимание базовой структуры AI-агентов в .NET
- 🛠️ **Интеграция инструментов**: Как агенты используют внешние функции для расширения возможностей  
- 💬 **Поток общения**: Управление многократными диалогами и контекстом с помощью управления потоками
- 🔧 **Шаблоны конфигурации**: Лучшие практики настройки и управления агентами в .NET

## 🎯 Основные концепции

### Принципы агентного фреймворка
- **Автономность**: Как агенты принимают независимые решения, используя абстракции AI в .NET
- **Реактивность**: Реакция на изменения окружающей среды и пользовательские запросы
- **Проактивность**: Инициативные действия на основе целей и контекста
- **Социальные способности**: Взаимодействие через естественный язык с помощью потоков общения

### Технические компоненты
- **AIAgent**: Основная оркестрация агента и управление диалогами (.NET)
- **Функции инструментов**: Расширение возможностей агента с помощью методов и атрибутов C#
- **Интеграция OpenAI**: Использование языковых моделей через стандартизированные API .NET
- **Управление окружением**: Безопасная настройка и обработка учетных данных с DotNetEnv

## ⚙️ Предварительные требования и настройка

**Необходимые зависимости:**
- .NET 9.0 SDK или выше
- Visual Studio 2022 или VS Code с расширением C#

**Пакеты NuGet:**
- `Microsoft.Extensions.AI` - Основные абстракции AI
- `Microsoft.Extensions.AI.OpenAI` - Интеграция OpenAI (предварительная версия)
- `DotNetEnv` - Управление переменными окружения

**Конфигурация окружения (.env файл):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Технический стек

**Основные технологии:**
- Microsoft Agent Framework (.NET)
- Интеграция API моделей GitHub
- Клиентские шаблоны, совместимые с OpenAI
- Конфигурация на основе окружения с DotNetEnv

**Возможности агента:**
- Понимание и генерация естественного языка
- Вызов функций и использование инструментов с атрибутами C#
- Ответы с учетом контекста с помощью потоков общения
- Расширяемая архитектура с шаблонами внедрения зависимостей

## 📚 Сравнение фреймворков

Этот пример демонстрирует подход Microsoft Agent Framework в .NET по сравнению с другими платформами:

| Функция | Фреймворк агента .NET | Эквиваленты Python |
|---------|-----------------------|--------------------|
| **Типизация** | Строгая типизация с C# | Динамическая типизация |
| **Интеграция** | Родная экосистема .NET | Разнообразная совместимость |
| **Производительность** | Производительность компилируемого кода | Интерпретируемое выполнение |
| **Готовность к корпоративному использованию** | Разработан для производственных приложений .NET | Зависит от фреймворка |
| **Инструменты** | Интеграция с Visual Studio | Зависимость от IDE |

## 🚀 Начало работы

Следуйте инструкциям ниже, чтобы создать своего первого базового агента в .NET и понять основные концепции агентного фреймворка!

## 📦 Установка и настройка

Этот пример доступен как исполняемое приложение .NET Single File App. Полная реализация находится в файле `02-dotnet-agent-framework.cs`.

Чтобы запустить пример:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Или используя dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Обзор кода

Полная реализация включает:

### 1. Зависимости пакетов

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

### 2. Основные импорты

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Конфигурация окружения

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Определение функций инструментов

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

### 5. Настройка и клиентская конфигурация

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

### 6. Конфигурация агента

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

### 7. Инициализация агента

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

### 8. Управление диалогами

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Основные выводы

1. **Архитектура агента**: Microsoft Agent Framework предоставляет чистый, строго типизированный подход к созданию AI-агентов в .NET
2. **Интеграция инструментов**: Функции, декорированные атрибутами `[Description]`, становятся доступными инструментами для агента
3. **Контекст диалога**: Управление потоками позволяет вести многократные диалоги с полным учетом контекста
4. **Управление конфигурацией**: Переменные окружения и безопасная обработка учетных данных соответствуют лучшим практикам .NET
5. **Совместимость с OpenAI**: Интеграция моделей GitHub работает без проблем через совместимые API OpenAI

## 🔗 Дополнительные ресурсы

- [Документация Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Marketplace моделей GitHub](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.