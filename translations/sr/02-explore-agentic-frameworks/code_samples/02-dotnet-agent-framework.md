<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T14:18:49+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "sr"
}
-->
# 🔍 Истраживање Microsoft Agent Framework - Основни агент (.NET)

## 📋 Циљеви учења

Овај пример истражује основне концепте Microsoft Agent Framework-а кроз имплементацију основног агента у .NET-у. Научићете основне агенцијске обрасце и разумети како интелигентни агенти функционишу изнутра користећи C# и .NET екосистем.

### Шта ћете открити

- 🏗️ **Архитектура агента**: Разумевање основне структуре AI агената у .NET-у  
- 🛠️ **Интеграција алата**: Како агенти користе спољашње функције за проширење могућности  
- 💬 **Ток конверзације**: Управљање разговорима са више корака и контекстом уз управљање нитима  
- 🔧 **Шаблони конфигурације**: Најбоље праксе за подешавање и управљање агентима у .NET-у  

## 🎯 Кључни концепти

### Принципи агенцијског оквира

- **Аутономија**: Како агенти доносе независне одлуке користећи .NET AI апстракције  
- **Реактивност**: Реаговање на промене у окружењу и корисничке уносе  
- **Проактивност**: Предузимање иницијативе на основу циљева и контекста  
- **Социјална способност**: Комуникација кроз природни језик уз разговорне нити  

### Техничке компоненте

- **AIAgent**: Основна оркестрација агента и управљање конверзацијом (.NET)  
- **Функције алата**: Проширење могућности агента помоћу C# метода и атрибута  
- **Интеграција OpenAI**: Коришћење језичких модела кроз стандардизоване .NET API-је  
- **Сигурна конфигурација**: Управљање API кључевима засновано на окружењу  

## 🔧 Технички стек

### Основне технологије

- Microsoft Agent Framework (.NET)  
- Интеграција GitHub Models API  
- Клијентски обрасци компатибилни са OpenAI  
- Конфигурација заснована на окружењу уз DotNetEnv  

### Могућности агента

- Разумевање и генерисање природног језика  
- Позивање функција и коришћење алата уз C# атрибуте  
- Одговори свесни контекста уз разговорне нити  
- Проширива архитектура уз шаблоне за убризгавање зависности  

## 📚 Поређење оквира

Овај пример демонстрира приступ Microsoft Agent Framework-а у поређењу са другим агенцијским оквирима:

| Карактеристика | Microsoft Agent Framework | Други оквири |
|----------------|---------------------------|--------------|
| **Интеграција** | Нативни Microsoft екосистем | Различита компатибилност |
| **Једноставност** | Чист, интуитиван API | Често сложено подешавање |
| **Проширивост** | Лака интеграција алата | Зависи од оквира |
| **Спремност за предузећа** | Дизајниран за продукцију | Зависи од оквира |

## 🚀 Почетак рада

### Предуслови

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новији  
- [GitHub Models API приступни токен](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Потребне променљиве окружења

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

Да бисте покренули пример кода,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Или користећи dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Погледајте [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) за комплетан код.

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
  

## 🎓 Кључни закључци

1. **Архитектура агента**: Microsoft Agent Framework пружа чист, типски сигуран приступ за изградњу AI агената у .NET-у  
2. **Интеграција алата**: Функције означене атрибутима `[Description]` постају доступни алати за агента  
3. **Контекст конверзације**: Управљање нитима омогућава разговоре са више корака уз потпуну свест о контексту  
4. **Управљање конфигурацијом**: Променљиве окружења и сигурно руковање акредитивима прате најбоље праксе .NET-а  
5. **Компатибилност са OpenAI**: Интеграција GitHub Models ради беспрекорно кроз OpenAI компатибилне API-је  

## 🔗 Додатни ресурси

- [Microsoft Agent Framework документација](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET апликације у једној датотеци](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->