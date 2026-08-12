# 🌍 Агенти Подорожей на базі Microsoft Agent Framework (.NET)

## 📋 Огляд сценарію

Цей приклад демонструє, як створити інтелектуального агента для планування подорожей за допомогою Microsoft Agent Framework для .NET. Агенти можуть автоматично генерувати персоналізовані маршрути одноденних поїздок випадковими напрямками по всьому світу.

### Основні можливості:

- 🎲 **Випадковий вибір напрямку**: Використовує спеціальний інструмент для вибору місць відпочинку
- 🗺️ **Інтелектуальне планування поїздок**: Створює детальні по днях маршрути
- 🔄 **Потокова обробка в реальному часі**: Підтримує як миттєві, так і потокові відповіді
- 🛠️ **Інтеграція користувацьких інструментів**: Демонструє, як розширювати можливості агента

## 🔧 Технічна архітектура

### Основні технології

- **Microsoft Agent Framework**: Остання реалізація на .NET для розробки AI агентів
- **Azure OpenAI (Responses API)**: Використовує Azure OpenAI Responses API для інференсу моделі
- **Azure Identity**: Безпечний вхід за допомогою `AzureCliCredential` (`az login`)
- **Безпечна конфігурація**: Управління точками доступу на основі оточення

### Ключові компоненти

1. **AIAgent**: Головний координатор агента, що керує потоком розмови
2. **Користувацькі інструменти**: функція `GetRandomDestination()` доступна агенту
3. **Responses Client**: Інтерфейс розмов на основі Azure OpenAI Responses
4. **Підтримка потокової обробки**: Можливості генерації відповідей в реальному часі

### Патерн інтеграції

```mermaid
graph LR
    A[Запит користувача] --> B[ІІ Агент]
    B --> C[Azure OpenAI (API відповідей)]
    B --> D[Інструмент Випадковий напрямок]
    C --> E[План подорожі]
    D --> E
```

## 🚀 Початок роботи

### Вимоги

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або вища версія
- [Передплата Azure](https://azure.microsoft.com/free/) з ресурсом Azure OpenAI та розгортанням моделі
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — вхід через `az login`

### Необхідні змінні оточення

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Потім увійдіть, щоб AzureCliCredential міг отримати токен
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Потім увійдіть у систему, щоб AzureCliCredential міг отримати токен
az login
```

### Приклад коду

Щоб запустити приклад коду,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Або за допомогою dotnet CLI:

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

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

1. **Архітектура агента**: Microsoft Agent Framework забезпечує чистий, типобезпечний підхід до створення AI агентів на .NET
2. **Інтеграція інструментів**: Функції, прикрашені атрибутами `[Description]`, стають доступними інструментами для агента
3. **Управління конфігурацією**: Змінні оточення та безпечне керування обліковими даними відповідають найкращим практикам .NET
4. **Azure OpenAI Responses API**: Агент використовує Azure OpenAI Responses API через Azure.AI.OpenAI SDK

## 🔗 Додаткові ресурси

- [Документація Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI у Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->