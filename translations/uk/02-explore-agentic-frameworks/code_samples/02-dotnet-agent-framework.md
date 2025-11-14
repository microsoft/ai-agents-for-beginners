<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:41:04+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "uk"
}
-->
# 🔍 Дослідження агентних фреймворків - Базовий агент (.NET)

## 📋 Цілі навчання

Цей ноутбук досліджує основні концепції Microsoft Agent Framework через реалізацію базового агента в .NET. Ви дізнаєтеся про основні агентні шаблони та зрозумієте, як працюють інтелектуальні агенти за допомогою C# та екосистеми .NET.

**Що ви дізнаєтесь:**
- 🏗️ **Архітектура агента**: Розуміння базової структури AI-агентів у .NET
- 🛠️ **Інтеграція інструментів**: Як агенти використовують зовнішні функції для розширення можливостей  
- 💬 **Потік розмови**: Управління багатокроковими розмовами та контекстом за допомогою управління потоками
- 🔧 **Шаблони конфігурації**: Найкращі практики налаштування та управління агентами в .NET

## 🎯 Основні концепції

### Принципи агентного фреймворку
- **Автономність**: Як агенти приймають незалежні рішення, використовуючи абстракції AI у .NET
- **Реактивність**: Реагування на зміни в середовищі та введення користувача
- **Проактивність**: Ініціативність на основі цілей та контексту
- **Соціальна здатність**: Взаємодія через природну мову з потоками розмов

### Технічні компоненти
- **AIAgent**: Основна оркестрація агента та управління розмовами (.NET)
- **Функції інструментів**: Розширення можливостей агента за допомогою методів та атрибутів C#
- **Інтеграція OpenAI**: Використання мовних моделей через стандартизовані API .NET
- **Управління середовищем**: Безпечне налаштування та обробка облікових даних за допомогою DotNetEnv

## ⚙️ Попередні вимоги та налаштування

**Необхідні залежності:**
- .NET 9.0 SDK або новіший
- Visual Studio 2022 або VS Code з розширенням C#

**Пакети NuGet:**
- `Microsoft.Extensions.AI` - Основні абстракції AI
- `Microsoft.Extensions.AI.OpenAI` - Інтеграція OpenAI (попередній перегляд)
- `DotNetEnv` - Управління змінними середовища

**Конфігурація середовища (.env файл):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Технічний стек

**Основні технології:**
- Microsoft Agent Framework (.NET)
- Інтеграція API моделей GitHub
- Клієнтські шаблони, сумісні з OpenAI
- Конфігурація на основі середовища з DotNetEnv

**Можливості агента:**
- Розуміння та генерація природної мови
- Виклик функцій та використання інструментів за допомогою атрибутів C#
- Контекстно-залежні відповіді з потоками розмов
- Розширювана архітектура з шаблонами впровадження залежностей

## 📚 Порівняння фреймворків

Цей приклад демонструє підхід Microsoft Agent Framework у .NET порівняно з іншими платформами:

| Функція | .NET Agent Framework | Еквіваленти Python |
|---------|---------------------|-------------------|
| **Типізація** | Сильна типізація з C# | Динамічна типізація |
| **Інтеграція** | Рідна екосистема .NET | Різна сумісність |
| **Продуктивність** | Продуктивність компільованого коду | Інтерпретоване виконання |
| **Готовність до підприємств** | Розроблено для виробничих .NET додатків | Залежить від фреймворку |
| **Інструменти** | Інтеграція з Visual Studio | Залежність від IDE |

## 🚀 Початок роботи

Виконайте наведені нижче кроки, щоб створити свого першого базового агента в .NET і зрозуміти основні концепції агентів!

## 📦 Встановлення та налаштування

Цей приклад доступний як виконуваний .NET Single File App. Дивіться супровідний файл `02-dotnet-agent-framework.cs` для повної реалізації.

Щоб запустити цей приклад:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Або використовуючи CLI dotnet:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Огляд коду

Повна реалізація включає:

### 1. Залежності пакету

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

### 2. Основні імпорти

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Конфігурація середовища

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Визначення функцій інструментів

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

### 5. Налаштування та конфігурація клієнта

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

### 6. Конфігурація агента

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

### 7. Ініціалізація агента

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

### 8. Управління розмовами

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Основні висновки

1. **Архітектура агента**: Microsoft Agent Framework забезпечує чіткий, типізований підхід до створення AI-агентів у .NET
2. **Інтеграція інструментів**: Функції, позначені атрибутами `[Description]`, стають доступними інструментами для агента
3. **Контекст розмови**: Управління потоками дозволяє багатокрокові розмови з повним урахуванням контексту
4. **Управління конфігурацією**: Змінні середовища та безпечна обробка облікових даних відповідають найкращим практикам .NET
5. **Сумісність з OpenAI**: Інтеграція моделей GitHub працює безперешкодно через сумісні API OpenAI

## 🔗 Додаткові ресурси

- [Документація Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Маркетплейс моделей GitHub](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.