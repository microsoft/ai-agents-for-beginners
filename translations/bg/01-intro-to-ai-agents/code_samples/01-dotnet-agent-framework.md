# 🌍 AI Туристически агент с Microsoft Agent Framework (.NET)

## 📋 Преглед на сценария

Този пример демонстрира как да изградите интелигентен агент за планиране на пътувания, използвайки Microsoft Agent Framework за .NET. Агентът може автоматично да генерира персонализирани еднодневни маршрути за случайни дестинации по света.

### Ключови възможности:

- 🎲 **Избор на случайна дестинация**: Използва персонализиран инструмент за избор на ваканционни места
- 🗺️ **Интелигентно планиране на пътуване**: Създава подробни дневни маршрути
- 🔄 **Поточно предаване в реално време**: Поддържа както незабавни, така и поточни отговори
- 🛠️ **Интеграция на персонализиран инструмент**: Демонстрира как да се разширят възможностите на агента

## 🔧 Техническа архитектура

### Основни технологии

- **Microsoft Agent Framework**: Най-новата .NET имплементация за разработка на AI агенти
- **Azure OpenAI (API за отговори)**: Използва API за отговори на Azure OpenAI за извличане от модела
- **Azure Identity**: Сигурно влизане чрез `AzureCliCredential` (`az login`)
- **Сигурна конфигурация**: Управление на крайни точки чрез променливи на средата

### Ключови компоненти

1. **AIAgent**: Основният агент, който управлява потока на разговора
2. **Персонализирани инструменти**: Функция `GetRandomDestination()` достъпна за агента
3. **Responses Client**: Интерфейс за разговор, базиран на Azure OpenAI Responses
4. **Поддръжка на поточно предаване**: Възможности за генериране на отговори в реално време

### Интеграционен модел

```mermaid
graph LR
    A[Потребителска заявка] --> B[AI агент]
    B --> C[Azure OpenAI (API за отговори)]
    B --> D[Инструмент GetRandomDestination]
    C --> E[Пътеводител за пътуване]
    D --> E
```

## 🚀 Започване

### Изисквания

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или по-нова версия
- [Azure абонамент](https://azure.microsoft.com/free/) с ресурс Azure OpenAI и разгръщане на модел
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — влезте с `az login`

### Задължителни променливи на средата

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# След това влезте, за да може AzureCliCredential да получи токен
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# След това влезте, за да може AzureCliCredential да получи токен
az login
```

### Примерен код

За да стартирате примерния код,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Или използвайки dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Вижте [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) за пълния код.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@9.*
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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Основни изводи

1. **Архитектура на агента**: Microsoft Agent Framework осигурява ясен, типово-сигурен подход за изграждане на AI агенти в .NET
2. **Интеграция на инструменти**: Функциите с атрибути `[Description]` стават достъпни инструменти за агента
3. **Управление на конфигурацията**: Променливите на средата и сигурната обработка на идентификационни данни следват най-добрите практики на .NET
4. **Azure OpenAI Responses API**: Агентът използва Azure OpenAI Responses API чрез Azure.AI.OpenAI SDK

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