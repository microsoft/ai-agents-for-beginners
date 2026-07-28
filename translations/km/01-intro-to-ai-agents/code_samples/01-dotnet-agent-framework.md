# 🌍 អាជីវករ​ដំណើរកម្សាន្ត AI ជាមួយ Microsoft Agent Framework (.NET)

## 📋 ទិដ្ឋភាពសេណារីយ៉ូ

ឧទាហរណ៍នេះបង្ហាញពីរបៀបបង្កើតភ្នាក់ងារគ្រប់គ្រងផែនការដំណើរកម្សាន្តឆ្លាតវៃដោយប្រើ Microsoft Agent Framework សម្រាប់ .NET។ ភ្នាក់ងារនេះអាចបង្កើតផែនការប្រកបដោយផ្ទាល់ខ្លួនសម្រាប់ដំណើរទស្សនកិច្ចមួយថ្ងៃចំពោះទីកន្លែងច្របូកច្របល់នៅជុំវិញពិភពលោកដោយស្វ័យប្រវត្តិ។

### សមត្ថភាពសំខាន់ៗ៖

- 🎲 **ការជ្រើសរើសទីកន្លែងចៃដន្យ**៖ ប្រើឧបករណ៍ប្តូរប្ដូរដើម្បីជ្រើសទីកន្លែងចំណាកស្រុក
- 🗺️ **ការរៀបចំផែនការដំណើរស្មារតី**៖ បង្កើតផែនការដំណើរជាប្រចាំមួយថ្ងៃម្ដង
- 🔄 **ការផ្សាយបន្តផ្ទាល់ Real-time**៖ គាំទ្រពីចម្លើយផ្ទាល់ខ្លួននិងចម្លើយផ្សាយបន្តផ្ទាល់
- 🛠️ **ការរួមបញ្ចូលឧបករណ៍ផ្ទាល់ខ្លួន**៖ បង្ហាញរបៀបពង្រីកសមត្ថភាពភ្នាក់ងារ

## 🔧 ស្ថាបត្យកម្មបច្ចេកទេស

### បច្ចេកវិទ្យាមនុស្សមូល

- **Microsoft Agent Framework**៖ ការអនុវត្ត .NET ថ្មីសម្រាប់ការអភិវឌ្ឍភ្នាក់ងារ AI
- **Azure OpenAI (Responses API)**៖ ប្រើ API Responses របស់ Azure OpenAI សម្រាប់ការរំពឹងទ្រព្យម៉ូដែល
- **Azure Identity**៖ ចូលប្រើដោយមានសុវត្ថិភាពជាមួយ `AzureCliCredential` (`az login`)
- **ការគ្រប់គ្រងការកំណត់ប្រព័ន្ធយ៉ាងសុវត្ថិភាព**៖ ការគ្រប់គ្រងចំណុចទីតាំងដោយផ្អែកលើបរិយាកាស

### គ្រឿងសង្ហារឹមសំខាន់ៗ

1. **AIAgent**៖ អ្នកបង្កើតភ្នាក់ងារសំខាន់ដែលគ្រប់គ្រងចរន្តការសន្ទនា
2. **ឧបករណ៍ផ្ទាល់ខ្លួន**៖ មុខងារ `GetRandomDestination()` ដែលមានសម្រាប់ភ្នាក់ងារ
3. **Responses Client**៖ ផ្ទាំងចរន្តសន្ទនារបស់ Azure OpenAI Responses
4. **គាំទ្រការផ្សាយបន្តផ្ទាល់**៖ សមត្ថភាពបង្កើតចម្លើយពេលវេលាពិត

### គំរូរួមបញ្ចូល

```mermaid
graph LR
    A[សំណើរអ្នកប្រើប្រាស់] --> B[អ្នកមិនដឹងអ្វីទេ AI]
    B --> C[Azure OpenAI (API ចម្លើយ)]
    B --> D[ឧបករណ៍ GetRandomDestination]
    C --> E[វិធីដំណើរកំសាន្ត]
    D --> E
```

## 🚀 ចាប់ផ្ដើម

### វត្ថុដែលត្រូវមានមុន

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ឬខ្ពស់ជាងនេះ
- មួយ [Azure subscription](https://azure.microsoft.com/free/) មានធនធាន Azure OpenAI និងការដឹកជញ្ជូនម៉ូដែល
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — ចូលប្រើជាមួយ `az login`

### បរិយាកាសប្រេនជាដាច់ខាតដែលត្រូវការ

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# បន្ទាប់មកចូលគណនី ដើម្បីអោយ AzureCliCredential អាចទទួលបានតូកិនបាន
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# បន្ទាប់មកចូលដំណើរការ ដើម្បីឲ្យ AzureCliCredential អាចទទួលបាន token
az login
```

### ឧទាហរណ៍កូដ

ដើម្បីរត់ឧទាហរណ៍កូដនេះ,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

ឬប្រើប្រាស់ dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

មើល [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) សម្រាប់កូដពេញលេញ។

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

## 🎓 ចំណុចអ្វីដែលបានរៀន

1. **ស្ថាបត្យកម្មភ្នាក់ងារ**៖ Microsoft Agent Framework ផ្ដល់មធ្យោបាយស្អាត និងប្រើប្រាស់ប្រភេទយ៉ាងសុវត្ថិភាពសម្រាប់កសាងភ្នាក់ងារ AI ក្នុង .NET
2. **ការរួមបញ្ចូលឧបករណ៍**៖ មុខងារ​ដែល​ត្រូវ​បាន​តុបតែងដោយ attribute `[Description]` ជាឧបករណ៍ដែលអាចប្រើបានសម្រាប់ភ្នាក់ងារ
3. **ការគ្រប់គ្រងការកំណត់**៖ អថេរ​បរិយាកាស និងការដោះស្រាយឯកសារយោងយ៉ាងសុវត្ថិភាពជាប់តាមជំនាញល្អបំផុតរបស់ .NET
4. **Azure OpenAI Responses API**៖ ភ្នាក់ងារប្រើ API របស់ Azure OpenAI Responses តាមរយៈ Azure.AI.OpenAI SDK

## 🔗 ឯកសារបន្ថែម

- [ឯកសារលម្អិត Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI ក្នុង Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->