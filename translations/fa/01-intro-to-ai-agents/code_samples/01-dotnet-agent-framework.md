# 🌍 نماینده سفر هوش مصنوعی با چهارچوب Microsoft Agent (.NET)

## 📋 مرور سناریو

این مثال نشان می‌دهد چگونه یک نماینده هوشمند برنامه‌ریزی سفر با استفاده از چهارچوب Microsoft Agent برای .NET بسازید. نماینده می‌تواند به طور خودکار برنامه‌های روزانه سفر شخصی‌سازی شده برای مقاصد تصادفی در سراسر جهان تولید کند.

### قابلیت‌های کلیدی:

- 🎲 **انتخاب مقصد تصادفی**: استفاده از ابزار سفارشی برای انتخاب نقاط تعطیلات
- 🗺️ **برنامه‌ریزی هوشمند سفر**: ایجاد برنامه‌های روز به روز دقیق
- 🔄 **پخش زنده در زمان واقعی**: پشتیبانی از پاسخ‌های فوری و پخش زنده
- 🛠️ **یکپارچه‌سازی ابزار سفارشی**: نمایش نحوه گسترش قابلیت‌های نماینده

## 🔧 معماری فنی

### فناوری‌های اصلی

- **چارچوب Microsoft Agent**: آخرین پیاده‌سازی .NET برای توسعه نماینده‌های هوش مصنوعی
- **Azure OpenAI (API پاسخ‌ها)**: استفاده از API پاسخ‌های Azure OpenAI برای استنتاج مدل
- **Azure Identity**: ورود امن با `AzureCliCredential` (`az login`)
- **پیکربندی امن**: مدیریت نقطه پایانی مبتنی بر محیط

### مؤلفه‌های کلیدی

1. **AIAgent**: هماهنگ‌کننده اصلی نماینده که جریان مکالمه را اداره می‌کند
2. **ابزارهای سفارشی**: تابع `GetRandomDestination()` که در دسترس نماینده است
3. **کلاینت پاسخ‌ها**: رابط مکالمه مبتنی بر پاسخ‌های Azure OpenAI
4. **پشتیبانی از پخش زنده**: قابلیت تولید پاسخ در زمان واقعی

### الگوی یکپارچه‌سازی

```mermaid
graph LR
    A[درخواست کاربر] --> B[عامل هوش مصنوعی]
    B --> C[آزور اوپن‌ای‌آی (API پاسخ‌ها)]
    B --> D[ابزار مقصد تصادفی]
    C --> E[برنامه سفر]
    D --> E
```

## 🚀 شروع به کار

### پیش‌نیازها

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا بالاتر
- اشتراک [Azure](https://azure.microsoft.com/free/) با منبع Azure OpenAI و استقرار مدل
- نصب [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — ورود با `az login`

### متغیرهای محیطی مورد نیاز

```bash
# زد شل/باش
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# سپس وارد شوید تا AzureCliCredential بتواند یک توکن دریافت کند
az login
```

```powershell
# پاورشل
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# سپس وارد شوید تا AzureCliCredential بتواند یک توکن دریافت کند
az login
```

### نمونه کد

برای اجرای نمونه کد،

```bash
# زد‌اِس‌اچ/بَش
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

یا با استفاده از dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

برای کد کامل به [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) مراجعه کنید.

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

## 🎓 نکات کلیدی

1. **معماری نماینده**: چارچوب Microsoft Agent رویکردی پاک و ایمن از نظر نوع برای ساخت نماینده‌های هوش مصنوعی در .NET فراهم می‌کند
2. **یکپارچه‌سازی ابزارها**: توابعی که با ویژگی `[Description]` تزئین شده‌اند، ابزارهای در دسترس برای نماینده می‌شوند
3. **مدیریت پیکربندی**: متغیرهای محیطی و مدیریت ایمن اعتبارنامه‌ها بهترین شیوه‌های .NET را دنبال می‌کنند
4. **API پاسخ‌های Azure OpenAI**: نماینده از API پاسخ‌های Azure OpenAI از طریق SDK Azure.AI.OpenAI استفاده می‌کند

## 🔗 منابع اضافی

- [مستندات چارچوب Microsoft Agent](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI در Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [برنامه‌های تک‌فایل .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->