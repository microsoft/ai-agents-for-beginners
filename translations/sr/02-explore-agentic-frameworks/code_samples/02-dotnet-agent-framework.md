<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:40:06+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "sr"
}
-->
# 🔍 Истраживање агентичких оквира - Основни агент (.NET)

## 📋 Циљеви учења

Овај нотес истражује основне концепте Microsoft Agent Framework-а кроз имплементацију основног агента у .NET-у. Научићете основне агентичке шаблоне и разумети како интелигентни агенти функционишу изнутра користећи C# и .NET екосистем.

**Шта ћете открити:**
- 🏗️ **Архитектура агента**: Разумевање основне структуре AI агената у .NET-у
- 🛠️ **Интеграција алата**: Како агенти користе спољне функције за проширење могућности  
- 💬 **Ток конверзације**: Управљање разговорима са више корака и контекстом уз управљање нитима
- 🔧 **Шаблони конфигурације**: Најбоље праксе за подешавање и управљање агентима у .NET-у

## 🎯 Кључни концепти

### Принципи агентичког оквира
- **Аутономија**: Како агенти доносе независне одлуке користећи .NET AI апстракције
- **Реактивност**: Реаговање на промене у окружењу и унос корисника
- **Проактивност**: Предузимање иницијативе на основу циљева и контекста
- **Социјална способност**: Комуникација кроз природни језик уз токове разговора

### Техничке компоненте
- **AIAgent**: Основна оркестрација агента и управљање разговорима (.NET)
- **Функције алата**: Проширење могућности агента помоћу C# метода и атрибута
- **OpenAI интеграција**: Коришћење језичких модела кроз стандардизоване .NET API-је
- **Управљање окружењем**: Сигурно подешавање и руковање акредитивима уз DotNetEnv

## ⚙️ Предуслови и подешавање

**Потребне зависности:**
- .NET 9.0 SDK или новији
- Visual Studio 2022 или VS Code са C# екстензијом

**NuGet пакети:**
- `Microsoft.Extensions.AI` - Основне AI апстракције
- `Microsoft.Extensions.AI.OpenAI` - OpenAI интеграција (преглед)
- `DotNetEnv` - Управљање променљивим окружења

**Конфигурација окружења (.env датотека):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Технички стек

**Основне технологије:**
- Microsoft Agent Framework (.NET)
- Интеграција GitHub Models API-ја
- Клијентски шаблони компатибилни са OpenAI
- Конфигурација заснована на окружењу уз DotNetEnv

**Могућности агента:**
- Разумевање и генерисање природног језика
- Позивање функција и коришћење алата уз C# атрибуте
- Одговори свесни контекста уз токове разговора
- Проширива архитектура уз шаблоне убризгавања зависности

## 📚 Поређење оквира

Овај пример демонстрира приступ Microsoft Agent Framework-а у .NET-у у поређењу са другим платформама:

| Карактеристика | .NET Agent Framework | Python еквиваленти |
|----------------|-----------------------|--------------------|
| **Типска сигурност** | Јака типизација уз C# | Динамичка типизација |
| **Интеграција** | Нативни .NET екосистем | Различита компатибилност |
| **Перформансе** | Перформансе компилираног кода | Интерпретирано извршење |
| **Спремност за предузећа** | Дизајнирано за продукцијске .NET апликације | Зависи од оквира |
| **Алатке** | Интеграција са Visual Studio-ом | Зависи од IDE-а |

## 🚀 Почетак рада

Пратите кораке испод да изградите свој први основни агент у .NET-у и разумете основне агентичке концепте!

## 📦 Инсталација и подешавање

Овај пример је доступан као извршна .NET апликација у једној датотеци. Погледајте пратећу датотеку `02-dotnet-agent-framework.cs` за комплетну имплементацију.

Да бисте покренули овај пример:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Или користећи dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Преглед кода

Комплетна имплементација укључује:

### 1. Зависности пакета

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

### 2. Основни увози

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Конфигурација окружења

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Дефиниција функције алата

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

### 5. Подешавање и конфигурација клијента

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

### 6. Конфигурација агента

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

### 7. Иницијализација агента

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

### 8. Управљање разговорима

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Кључни закључци

1. **Архитектура агента**: Microsoft Agent Framework пружа чист, типски сигуран приступ изградњи AI агената у .NET-у
2. **Интеграција алата**: Функције означене атрибутима `[Description]` постају доступни алати за агента
3. **Контекст разговора**: Управљање нитима омогућава разговоре са више корака уз потпуну свест о контексту
4. **Управљање конфигурацијом**: Променљиве окружења и сигурно руковање акредитивима прате најбоље праксе .NET-а
5. **Компатибилност са OpenAI**: Интеграција GitHub Models-а функционише беспрекорно кроз OpenAI компатибилне API-је

## 🔗 Додатни ресурси

- [Microsoft Agent Framework документација](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET апликације у једној датотеци](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.