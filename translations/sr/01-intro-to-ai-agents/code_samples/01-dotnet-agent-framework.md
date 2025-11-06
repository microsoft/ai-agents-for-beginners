<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "23afd9be7b6ba5b69a44c3b6a78e07f6",
  "translation_date": "2025-11-06T10:06:46+00:00",
  "source_file": "01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.md",
  "language_code": "sr"
}
-->
# 🌍 AI туристички агент са Microsoft Agent Framework (.NET)

## 📋 Преглед сценарија

Овај нотебук показује како да направите интелигентног агента за планирање путовања користећи Microsoft Agent Framework за .NET. Агенат може аутоматски генерисати персонализоване итинераре за једнодневне излете на насумично одабране дестинације широм света.

**Кључне могућности:**
- 🎲 **Насумично одабирање дестинације**: Користи прилагођени алат за избор места за одмор
- 🗺️ **Интелигентно планирање путовања**: Креира детаљне итинераре за сваки дан
- 🔄 **Стриминг у реалном времену**: Подржава тренутне и стриминг одговоре
- 🛠️ **Интеграција прилагођених алата**: Показује како проширити могућности агента

## 🔧 Техничка архитектура

### Основне технологије
- **Microsoft Agent Framework**: Најновија .NET имплементација за развој AI агената
- **Интеграција GitHub модела**: Користи GitHub-ову услугу за инференцију AI модела
- **Компатибилност са OpenAI API**: Ослања се на OpenAI клијентске библиотеке са прилагођеним ендпоинтима
- **Сигурна конфигурација**: Управљање API кључевима засновано на окружењу

### Кључне компоненте
1. **AIAgent**: Главни оркестратор агента који управља током разговора
2. **Прилагођени алати**: Функција `GetRandomDestination()` доступна агенту
3. **Chat Client**: Интерфејс за разговор подржан GitHub моделима
4. **Подршка за стриминг**: Способност генерисања одговора у реалном времену

### Шема интеграције
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 Почетак рада

**Предуслови:**
- .NET 10.0 или новији
- Приступни токен за GitHub Models API
- Конфигурисане променљиве окружења у `.env` датотеци

**Потребне променљиве окружења:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Покрените узорак кода испод редом да бисте видели агента за путовања у акцији!

---

## .NET апликација у једној датотеци: Пример AI туристичког агента

Погледајте `01-dotnet-agent-framework.cs` за комплетан узорак кода који се може покренути.

```bash
dotnet run 01-dotnet-agent-framework.cs
```

### Узорак кода

```csharp
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

// Extract configuration from environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI Client Options
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Create AI Agent with Travel Planning Capabilities
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip (Non-Streaming)
Console.WriteLine(await agent.RunAsync("Plan me a day trip"));

// Execute Agent: Plan a Day Trip (Streaming Response)
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    Console.Write(update);
}
```

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.