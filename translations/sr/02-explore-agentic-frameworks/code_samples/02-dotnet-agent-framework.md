# 🔍 Истраживање Microsoft Agent Framework - Основни агент (.NET)

## 📋 Учебни циљеви

Овај пример истражује основне концепте Microsoft Agent Framework кроз основну имплементацију агента у .NET-у. Научићете основне агентике обрасце и разумети како интелигентни агенти функционишу испод хаубе користећи C# и .NET екосистем.

### Шта ћете открити

- 🏗️ **Архитектура агента**: Разумевање основне структуре AI агената у .NET
- 🛠️ **Интеграција алата**: Како агенти користе спољне функције за проширење могућности  
- 💬 **Ток разговора**: Управљање вишетоковним разговорима и контекстом са управљањем нитима
- 🔧 **Обрасци конфигурације**: Најбоље праксе за подешавање и управљање агентом у .NET

## 🎯 Кључни покривени појмови

### Принципи агентичког оквира

- **Аутономија**: Како агенти доносе независне одлуке користећи .NET AI апстракције
- **Реактивност**: Одговарање на промене окружења и корисничке уносе
- **Проактивност**: Иницирање акција на основу циљева и контекста
- **Друштвена способност**: Интерakcија кроз природни језик са нитима разговора

### Техничке компоненте

- **AIAgent**: Основна организација агента и управљање разговорима (.NET)
- **Функције алата**: Проширење могућности агента са C# методама и атрибутима
- **Интеграција Azure OpenAI**: Користећи језичке моделе преко Azure OpenAI Responses API-ја
- **Сигурна конфигурација**: Управљање крајњим тачкама на основу окружења

## 🔧 Технички стек

### Основне технологије

- Microsoft Agent Framework (.NET)
- Интеграција Azure OpenAI (Responses API)
- Обрасци клијента Azure.AI.OpenAI
- Конфигурација заснована на окружењу уз DotNetEnv

### Могућности агента

- Разумевање и генерисање природног језика
- Позивање функција и коришћење алата са C# атрибутима
- Одговори свесни контекста уз разговорне сесије
- Проширива архитектура уз обрасце dependency injection

## 📚 Поређење оквира

Овај пример демонстрира приступ Microsoft Agent Framework у поређењу са другим агентичким оквирима:

| Карактеристика | Microsoft Agent Framework | Други оквири |
|---------|-------------------------|------------------|
| **Интеграција** | Нативни Microsoft екосистем | Различита компатибилност |
| **Једноставност** | Јасан, интуитиван API | Често сложено подешавање |
| **Проширивост** | Лака интеграција алата | Зависно од оквира |
| **Спремност за предузећа** | Намена за производњу | Варира по оквиру |

## 🚀 Почетак рада

### Претпоставке

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новији
- [Azure претплата](https://azure.microsoft.com/free/) са Azure OpenAI ресурсом и моделом за имплементацију
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — пријавите се користећи `az login`

### Потребне променљиве окружења

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Затим се пријавите како би AzureCliCredential могао да добије токен
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Затим се пријавите како би AzureCliCredential могао да добије токен
az login
```

### Пример кода

Да бисте покренули пример кода,

```bash
# зш/баш
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

## 🎓 Кључне поуке

1. **Архитектура агента**: Microsoft Agent Framework пружа чист, типски безбедан приступ изградњи AI агената у .NET
2. **Интеграција алата**: Функције украшене атрибутима `[Description]` постају доступни алати за агента
3. **Контекст разговора**: Управљање сесијом омогућава вишетоковне разговоре са пуним свесношћу о контексту
4. **Управљање конфигурацијом**: Променљиве окружења и сигурно руковање акредитивима прате најбоље праксе .NET-а
5. **Azure OpenAI Responses API**: Агент користи Azure OpenAI Responses API преко Azure.AI.OpenAI SDK-а

## 🔗 Додатни ресурси

- [Microsoft Agent Framework документација](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI у Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET апликације са једним фајлом](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->