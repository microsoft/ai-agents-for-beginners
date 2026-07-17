# 🌍 Туристический агент на базе искусственного интеллекта с Microsoft Agent Framework (.NET)

## 📋 Обзор сценария

В этом примере показано, как создать интеллектуального агента для планирования путешествий с использованием Microsoft Agent Framework для .NET. Агент может автоматически генерировать персонализированные маршруты однодневных поездок в случайные направления по всему миру.

### Ключевые возможности:

- 🎲 **Случайный выбор направления**: Использует специальный инструмент для выбора мест отдыха
- 🗺️ **Интеллектуальное планирование поездок**: Создает подробные маршруты по дням
- 🔄 **Потоковая передача в реальном времени**: Поддерживает как мгновенные, так и потоковые ответы
- 🛠️ **Интеграция пользовательских инструментов**: Демонстрирует расширение возможностей агента

## 🔧 Техническая архитектура

### Основные технологии

- **Microsoft Agent Framework**: Актуальная реализация для .NET для разработки ИИ-агентов
- **Azure OpenAI (Responses API)**: Использует Azure OpenAI Responses API для вывода модели
- **Azure Identity**: Безопасный вход через `AzureCliCredential` (`az login`)
- **Безопасная конфигурация**: Управление конечными точками через переменные окружения

### Основные компоненты

1. **AIAgent**: Главный оркестратор агента, управляющий потоком беседы
2. **Пользовательские инструменты**: Функция `GetRandomDestination()`, доступная агенту
3. **Клиент Responses**: Интерфейс общения на базе Azure OpenAI Responses
4. **Поддержка потоковой передачи**: Возможность генерации ответов в реальном времени

### Шаблон интеграции

```mermaid
graph LR
    A[Запрос пользователя] --> B[ИИ агент]
    B --> C[Azure OpenAI (API ответов)]
    B --> D[Инструмент GetRandomDestination]
    C --> E[План путешествия]
    D --> E
```

## 🚀 Начало работы

### Требования

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или выше
- Активная [подписка Azure](https://azure.microsoft.com/free/) с ресурсом Azure OpenAI и развернутой моделью
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — войдите с помощью `az login`

### Необходимые переменные окружения

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Затем войдите в систему, чтобы AzureCliCredential мог получить токен
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Затем войдите в систему, чтобы AzureCliCredential мог получить токен
az login
```

### Пример кода

Для запуска примера кода,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Или с помощью команды dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Полный код смотрите в файле [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs).

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

## 🎓 Ключевые выводы

1. **Архитектура агента**: Microsoft Agent Framework обеспечивает чистый и типобезопасный подход к созданию ИИ-агентов на .NET
2. **Интеграция инструментов**: Функции с атрибутом `[Description]` становятся доступными инструментами для агента
3. **Управление конфигурацией**: Переменные окружения и безопасная работа с учетными данными соответствуют лучшим практикам .NET
4. **Azure OpenAI Responses API**: Агент использует Azure OpenAI Responses API через SDK Azure.AI.OpenAI

## 🔗 Дополнительные ресурсы

- [Документация Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI в Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Однофайловые приложения .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->