# 🌍 AI туристички агент са Microsoft Agent Framework (.NET)

## 📋 Преглед сценарија

Овај пример показује како изградити интелигентног агента за планирање путовања користећи Microsoft Agent Framework за .NET. Агент може аутоматски генерисати персонализоване дневне планове путовања за случајне дестинације широм света.

### Кључне могућности:

- 🎲 **Случајан избор дестинације**: Користи прилагођени алат за избор туристичких места
- 🗺️ **Интелигентно планирање путовања**: Креира детаљне дневне планове путовања
- 🔄 **Стриминг у реалном времену**: Подржава и одговоре одмах и стриминг одговоре
- 🛠️ **Интеграција прилагођених алата**: Показује како продужити могућности агента

## 🔧 Техничка архитектура

### Основне технологије

- **Microsoft Agent Framework**: Најновија .NET имплементација за развој AI агената
- **Azure OpenAI (Responses API)**: Користи Azure OpenAI Responses API за извршење модела
- **Azure Identity**: Сигурна пријава преко `AzureCliCredential` (`az login`)
- **Сигурна конфигурација**: Управљање крајњим тачкама засновано на окружењу

### Кључне компоненте

1. **AIAgent**: Главни агент који организује ток разговора
2. **Прилагођени алати**: функција `GetRandomDestination()` доступна агенту
3. **Responses клијент**: Разговорски интерфејс базиран на Azure OpenAI Responses
4. **Подршка за стриминг**: Могућности генерисања одговора у реалном времену

### Образац интеграције

```mermaid
graph LR
    A[Кориснички захтев] --> B[AI агент]
    B --> C[Azure OpenAI (Responses API)]
    B --> D[Алатка GetRandomDestination]
    C --> E[План путовања]
    D --> E
```

## 🚀 Почетак рада

### Захтеви

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или виша верзија
- [Azure претплата](https://azure.microsoft.com/free/) са Azure OpenAI ресурсом и распоређеним моделом
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — пријава преко `az login`

### Потребне променљиве окружења

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Затим се пријавите да AzureCliCredential може да добије токен
az login
```

```powershell
# ПоверШел
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Онда се пријавите да би AzureCliCredential могао да добије токен
az login
```

### Пример кода

Да бисте покренули пример кода,

```bash
# зш/баш
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Или користећи dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Погледајте [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) за комплетан код.

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

## 🎓 Кључне поуке

1. **Архитектура агента**: Microsoft Agent Framework пружа чист, тип-безбедан приступ изградњи AI агената у .NET-у
2. **Интеграција алата**: Функције украшене атрибутима `[Description]` постају доступни алати агенту
3. **Управљање конфигурацијом**: Променљиве окружења и сигурна обрада акредитива прате најбоље праксе .NET-а
4. **Azure OpenAI Responses API**: Агент користи Azure OpenAI Responses API преко Azure.AI.OpenAI SDK

## 🔗 Додатни ресурси

- [Документација Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI у Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->