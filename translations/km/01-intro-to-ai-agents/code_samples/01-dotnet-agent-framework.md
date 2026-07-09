# 🌍 អ្នកទេសចរណ៍ AI ជាមួយ Microsoft Agent Framework (.NET)

## 📋 ទិដ្ឋភាពស្ថានการณ์

ឧទាហរណ៍នេះបង្ហាញពីរបៀបបង្កើតអ្នកទេសចរណ៍ឆ្លាតវៃសម្រាប់ផែនការធ្វើដំណើរដោយប្រើ Microsoft Agent Framework សម្រាប់ .NET។ អ្នកទេសចរណ៍អាចបង្កើតយុទ្ធសាស្ត្រធ្វើដំណើរប្រចាំថ្ងៃឯកជនសម្រាប់គោលដៅចៃដន្យនៅជុំវិញពិភពលោកបានដោយស្វ័យប្រវត្តិ។

### មុខងារចម្បង:

- 🎲 **ជ្រើសរើសគោលដៅចៃដន្យ**: ប្រើ​ឧបករណ៍ផ្ទាល់ខ្លួនដើម្បីជ្រើសកន្លែងលំហែកាយ
- 🗺️ **ការធ្វើផែនការធ្វើដំណើរឆ្លាតវៃ**: បង្កើតយុទ្ធសាស្ត្រពីរបរ រៀបចំថ្ងៃក្នុងមួយថ្ងៃ
- 🔄 **ការចាក់ស្រោមផ្សាយពេលវេលាពិត**: គាំទ្រឆ្លើយតបទាំងភ្លាមៗ និងចាក់ស្រោមផ្សាយ
- 🛠️ **ការបញ្ចូលឧបករណ៍ផ្ទាល់ខ្លួន**: បង្ហាញរបៀបពង្រីកមុខងារអ្នកទេសចរណ៍

## 🔧 សំណង់បច្ចេកទេស

### បច្ចេកវិទ្យាគោល

- **Microsoft Agent Framework**: ការអនុវត្ត .NET ថ្មីបំផុតសម្រាប់ការអភិវឌ្ឍន៍អ្នកទេសចរណ៍ AI
- **Azure OpenAI (Responses API)**: ប្រើ Azure OpenAI Responses API សម្រាប់ការវិភាគម៉ូដែល
- **Azure Identity**: ចុះឈ្មោះយ៉ាងសុវត្ថិភាពតាម `AzureCliCredential` (`az login`)
- **ការគ្រប់គ្រងសុវត្ថិភាព**: គ្រប់គ្រងចំណុចចេញប្រែប្រួលតាមបរិយាកាស

### គ្រឿងផ្សំសំខាន់ៗ

1. **AIAgent**: អ្នកទេសចរណ៍សំខាន់ដែលគ្រប់គ្រងដំណើរជជែក
2. **ឧបករណ៍ផ្ទាល់ខ្លួន**: មុខងារ `GetRandomDestination()` មិនមានក្នុងអ្នកទេសចរណ៍
3. **Responses Client**: ចំណុចប្រទាក់នៃការជជែកប្រើ Azure OpenAI Responses
4. **ការគាំទ្រចាក់ស្រោមផ្សាយ**: មុខងារបង្កើតចម្លើយពេលវេលាពិត

### លំនាំការបញ្ចូល

```mermaid
graph LR
    A[សំណើអ្នកប្រើ] --> B[អេជង់ AI]
    B --> C[Azure OpenAI (Responses API)]
    B --> D[ឧបករណ៍ GetRandomDestination]
    C --> E[ព្រឹត្តិការណ៍ដំណើរកំសាន្ត]
    D --> E
```

## 🚀 ការចាប់ផ្តើម

### និយមន័យចាំបាច់

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) ឬខ្ពស់ជាងនេះ
- មាន [ការជាវ Azure](https://azure.microsoft.com/free/) ជាមួយធនធាន Azure OpenAI និងការបង្ហោះម៉ូដែល
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — ចូលប្រើដោយ `az login`

### ខ្ទង់បរិយាកាសចាំបាច់

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# បន្ទាប់មកចុះចូល ដើម្បីឱ្យ AzureCliCredential អាចទទួលបានសញ្ញាបត្រ(token)បាន។
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# បន្ទាប់មកចូលក្នុងដំណើរការ ដើម្បីឱ្យ AzureCliCredential អាចទទួលបាន​សញ្ញាប័ត្រ token
az login
```

### គំរូកូដ

ដើម្បីរត់ឧទាហរណ៍កូដ,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

ឬប្រើ dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

មើល [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) សម្រាប់កូដពេញលេញ។

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

## 🎓 ចំណុចសំខាន់ៗ

1. **សម្ព័ន្ធអ្នកទេសចរណ៍**: Microsoft Agent Framework ផ្តល់ជូនវិធីសាស្ត្របង្កើតអ្នកទេសចរណ៍ AI ដែលស្អាត និងមានសុវត្ថិភាពប្រភេទនៅក្នុង .NET
2. **ការបញ្ចូលឧបករណ៍**: មុខងារដែលបានតក្កតាក្នុង `[Description]` ក្លាយជាឧបករណ៍ដែលអាចប្រើសម្រាប់អ្នកទេសចរណ៍
3. **ការគ្រប់គ្រងកំណត់ដាក់**: វ៉ារ្យអេបញ្ជាក់បរិយាកាស និងការដោះស្រាយសម្ងាត់អត្តសញ្ញាណគោរពតាមពិធីល្អបំផុតរបស់ .NET
4. **Azure OpenAI Responses API**: អ្នកទេសចរណ៍ប្រើ Azure OpenAI Responses API តាមរយៈ Azure.AI.OpenAI SDK

## 🔗 ប្រភពជំនួយបន្ថែម

- [ឯកសារសម្រាប់ Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI នៅក្នុង Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [កម្មវិធី .NET Single File](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->