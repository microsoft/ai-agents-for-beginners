# 🌍 مائیکروسافٹ ایجنٹ فریم ورک (.NET) کے ساتھ AI ٹریول ایجنٹ

## 📋 منظرنامہ کا جائزہ

یہ مثال ظاہر کرتی ہے کہ کس طرح مائیکروسافٹ ایجنٹ فریم ورک فار .NET کا استعمال کرتے ہوئے ایک ذہین ٹریول پلاننگ ایجنٹ بنایا جائے۔ یہ ایجنٹ دنیا بھر کے مختلف مقامات کے لئے ذاتی نوعیت کے روزانہ کے دوروں کے لیے خودکار طریقے سے منصوبے تیار کر سکتا ہے۔

### اہم خصوصیات:

- 🎲 **بے ترتیب مقام کا انتخاب**: تعطیلات کی جگہوں کے انتخاب کے لئے ایک حسب ضرورت آلہ استعمال کرتا ہے
- 🗺️ **ذہین ٹرپ پلاننگ**: روزانہ کی تفصیلی منصوبہ بندی تیار کرتا ہے
- 🔄 **ریئل ٹائم اسٹریمنگ**: فوری اور اسٹریمنگ دونوں قسم کی جوابات کی حمایت کرتا ہے
- 🛠️ **حسب ضرورت آلہ انضمام**: ایجنٹ کی صلاحیتوں کو بڑھانے کے طریقے دکھاتا ہے

## 🔧 تکنیکی ساخت

### بنیادی تکنیکیں

- **مائیکروسافٹ ایجنٹ فریم ورک**: AI ایجنٹ کی ترقی کے لئے جدید ترین .NET نفاذ
- **ایزور اوپن AI (Responses API)**: ماڈل انفرنس کے لیے ایزور اوپن AI Responses API کا استعمال
- **ایزور شناخت**: `AzureCliCredential` (`az login`) کے ذریعے محفوظ سائن ان
- **محفوظ کنفیگریشن**: ماحول کی بنیاد پر اینڈپوائنٹ کا انتظام

### کلیدی اجزاء

1. **AIAgent**: مرکزی ایجنٹ جو گفتگو کے بہاؤ کو کنٹرول کرتا ہے
2. **حسب ضرورت آلات**: ایجنٹ کے لیے `GetRandomDestination()` فنکشن دستیاب ہے
3. **Responses کلائنٹ**: ایزور اوپن AI Responses پر مبنی گفتگو انٹرفیس
4. **اسٹریمنگ کی حمایت**: ریئل ٹائم جواب پیدا کرنے کی صلاحیت

### انضمامی پیٹرن

```mermaid
graph LR
    A[صارف کی درخواست] --> B[AI ایجنٹ]
    B --> C[Azure OpenAI (جوابات API)]
    B --> D[GetRandomDestination کا آلہ]
    C --> E[سفر کا روٹ]
    D --> E
```

## 🚀 شروع کرنے کا طریقہ

### ضروریاتِ پیشگی

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) یا اس سے زیادہ
- [Azure سبسکرپشن](https://azure.microsoft.com/free/) کے ساتھ ایک Azure OpenAI ریسورس اور ماڈل کی تعیناتی
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` کے ذریعے سائن ان کریں

### مطلوبہ ماحول متغیرات

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# پھر سائن ان کریں تاکہ AzureCliCredential ٹوکن حاصل کر سکے
az login
```

```powershell
# پاور شیل
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# پھر سائن ان کریں تاکہ AzureCliCredential ٹوکن حاصل کر سکے
az login
```

### نمونہ کوڈ

کوڈ مثال چلانے کے لئے،

```bash
# زی شیل / باش
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

یا dotnet CLI استعمال کریں:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

مکمل کوڈ کے لیے [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) دیکھیں۔

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

## 🎓 اہم سبق

1. **ایجنٹ فن تعمیر**: مائیکروسافٹ ایجنٹ فریم ورک .NET میں AI ایجنٹس بنانے کے لیے ایک صاف اور ٹائپ-سیف طریقہ فراہم کرتا ہے
2. **آلہ انضمام**: `[Description]` خصوصیات والے فنکشنز ایجنٹ کے لیے دستیاب آلات بن جاتے ہیں
3. **کنفیگریشن مینجمنٹ**: ماحول کے متغیرات اور محفوظ اسناد کا انتظام .NET کی بہترین عملی طریقوں کے مطابق ہوتا ہے
4. **ایزور اوپن AI Responses API**: ایجنٹ Azure.AI.OpenAI SDK کے ذریعے Azure OpenAI Responses API کا استعمال کرتا ہے

## 🔗 اضافی وسائل

- [مائیکروسافٹ ایجنٹ فریم ورک کی دستاویزات](https://learn.microsoft.com/agent-framework)
- [مائیکروسافٹ فاؤنڈری میں Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET سنگل فائل ایپس](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->