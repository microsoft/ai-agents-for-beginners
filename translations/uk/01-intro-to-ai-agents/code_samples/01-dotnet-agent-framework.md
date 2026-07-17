# 🌍 Штучний інтелект як туристичний агент з Microsoft Agent Framework (.NET)

## 📋 Огляд сценарію

Цей приклад демонструє, як створити інтелектуального агента для планування подорожей за допомогою Microsoft Agent Framework для .NET. Агент може автоматично генерувати персоналізовані маршрути одноденних поїздок до випадкових напрямків по всьому світу.

### Ключові можливості:

- 🎲 **Вибір випадкового напрямку**: Використовує власний інструмент для вибору місць відпочинку
- 🗺️ **Інтелектуальне планування подорожі**: Створює докладні маршрути по днях
- 🔄 **Потокова передача в реальному часі**: Підтримка миттєвих і потокових відповідей
- 🛠️ **Інтеграція власних інструментів**: Демонструє розширення можливостей агента

## 🔧 Технічна архітектура

### Основні технології

- **Microsoft Agent Framework**: Остання реалізація для .NET для розробки AI агентів
- **Azure OpenAI (Responses API)**: Використання Azure OpenAI Responses API для моделювання
- **Azure Identity**: Безпечний вхід через `AzureCliCredential` (`az login`)
- **Безпечна конфігурація**: Керування кінцевими точками через середовище

### Ключові компоненти

1. **AIAgent**: Основний агент-організатор, що керує потоком розмови
2. **Власні інструменти**: функція `GetRandomDestination()` доступна агенту
3. **Responses Client**: Інтерфейс розмови на основі Azure OpenAI Responses
4. **Підтримка потокової передачі**: Можливості генерації відповідей у реальному часі

### Шаблон інтеграції

```mermaid
graph LR
    A[Запит користувача] --> B[AI Агент]
    B --> C[Azure OpenAI (API відповіді)]
    B --> D[Інструмент GetRandomDestination]
    C --> E[План подорожі]
    D --> E
```

## 🚀 Початок роботи

### Вимоги

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або новіша версія
- Обліковий запис [Azure](https://azure.microsoft.com/free/) з ресурсом Azure OpenAI і розгортанням моделі
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — увійдіть за допомогою `az login`

### Необхідні системні змінні середовища

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Потім увійдіть, щоб AzureCliCredential міг отримати токен
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Потім увійдіть, щоб AzureCliCredential міг отримати токен
az login
```

### Приклад коду

Щоб запустити приклад коду,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Або використовуючи CLI dotnet:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Дивіться [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) для повного коду.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
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

## 🎓 Ключові висновки

1. **Архітектура агента**: Microsoft Agent Framework надає чистий, типобезпечний підхід для створення AI агентів у .NET
2. **Інтеграція інструментів**: Функції, прикрашені атрибутами `[Description]`, стають доступними інструментами для агента
3. **Управління конфігурацією**: Змінні середовища та безпечне керування обліковими даними відповідають найкращим практикам .NET
4. **Azure OpenAI Responses API**: Агент використовує Azure OpenAI Responses API через SDK Azure.AI.OpenAI

## 🔗 Додаткові ресурси

- [Документація Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI у Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Однофайлові додатки .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->