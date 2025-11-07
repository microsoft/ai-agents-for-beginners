<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:38:27+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "tl"
}
-->
# 🔍 Pagsusuri sa Agentic Frameworks - Basic Agent (.NET)

## 📋 Mga Layunin sa Pag-aaral

Ang notebook na ito ay naglalahad ng mga pangunahing konsepto ng Microsoft Agent Framework sa pamamagitan ng isang simpleng implementasyon ng agent sa .NET. Matutunan mo ang mga pangunahing pattern ng agentic at mauunawaan kung paano gumagana ang mga intelligent agents gamit ang C# at ang .NET ecosystem.

**Ano ang Matutuklasan Mo:**
- 🏗️ **Arkitektura ng Agent**: Pag-unawa sa pangunahing istruktura ng AI agents sa .NET
- 🛠️ **Integrasyon ng Tool**: Paano ginagamit ng mga agent ang mga panlabas na function upang mapalawak ang kakayahan  
- 💬 **Daloy ng Usapan**: Pamamahala ng multi-turn na usapan at konteksto gamit ang thread management
- 🔧 **Mga Pattern ng Konfigurasyon**: Mga pinakamahusay na kasanayan para sa pag-setup at pamamahala ng agent sa .NET

## 🎯 Mga Pangunahing Konseptong Saklaw

### Mga Prinsipyo ng Agentic Framework
- **Autonomy**: Paano gumagawa ng mga independiyenteng desisyon ang mga agent gamit ang .NET AI abstractions
- **Reactivity**: Pagtugon sa mga pagbabago sa kapaligiran at input ng user
- **Proactivity**: Pagkilos batay sa mga layunin at konteksto
- **Social Ability**: Pakikipag-ugnayan gamit ang natural na wika sa pamamagitan ng mga thread ng usapan

### Mga Teknikal na Komponent
- **AIAgent**: Pangunahing orkestrasyon ng agent at pamamahala ng usapan (.NET)
- **Tool Functions**: Pagpapalawak ng kakayahan ng agent gamit ang mga C# method at attribute
- **OpenAI Integration**: Paggamit ng mga modelo ng wika sa pamamagitan ng standardized na .NET APIs
- **Pamamahala ng Kapaligiran**: Secure na konfigurasyon at paghawak ng kredensyal gamit ang DotNetEnv

## ⚙️ Mga Kinakailangan at Setup

**Mga Kinakailangang Dependency:**
- .NET 9.0 SDK o mas mataas
- Visual Studio 2022 o VS Code na may C# extension

**NuGet Packages:**
- `Microsoft.Extensions.AI` - Pangunahing AI abstractions
- `Microsoft.Extensions.AI.OpenAI` - OpenAI integration (preview)
- `DotNetEnv` - Pamamahala ng environment variable

**Konfigurasyon ng Kapaligiran (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Teknikal na Stack

**Pangunahing Teknolohiya:**
- Microsoft Agent Framework (.NET)
- Integrasyon ng GitHub Models API
- Mga pattern ng OpenAI-compatible client
- Konfigurasyon batay sa kapaligiran gamit ang DotNetEnv

**Kakayahan ng Agent:**
- Pag-unawa at pagbuo ng natural na wika
- Pagtawag ng function at paggamit ng tool gamit ang C# attributes
- Mga tugon na may konteksto gamit ang mga thread ng usapan
- Extensible na arkitektura gamit ang dependency injection patterns

## 📚 Paghahambing ng Framework

Ipinapakita ng halimbawang ito ang diskarte ng Microsoft Agent Framework sa .NET kumpara sa ibang mga platform:

| Tampok | .NET Agent Framework | Katumbas sa Python |
|--------|-----------------------|--------------------|
| **Type Safety** | Malakas na typing gamit ang C# | Dynamic typing |
| **Integrasyon** | Katutubong .NET ecosystem | Iba't ibang compatibility |
| **Pagganap** | Pagganap ng compiled code | Interpreted execution |
| **Handa para sa Enterprise** | Ginawa para sa production .NET apps | Nag-iiba depende sa framework |
| **Tooling** | Integrasyon ng Visual Studio | Depende sa IDE |

## 🚀 Pagsisimula

Sundin ang mga cell sa ibaba upang bumuo ng iyong unang simpleng agent sa .NET at maunawaan ang mga pangunahing konsepto ng agentic!

## 📦 Pag-install at Setup

Ang halimbawang ito ay magagamit bilang isang runnable .NET Single File App. Tingnan ang kasamang `02-dotnet-agent-framework.cs` file para sa kumpletong implementasyon.

Upang patakbuhin ang halimbawang ito:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

O gamit ang dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Paglalakad sa Code

Kasama sa kumpletong implementasyon ang:

### 1. Mga Dependency ng Package

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```

### 2. Mahahalagang Imports

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Konfigurasyon ng Kapaligiran

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Kahulugan ng Tool Function

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
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
```

### 5. Konfigurasyon at Setup ng Client

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```

### 6. Konfigurasyon ng Agent

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```

### 7. Inisyal na Pagsisimula ng Agent

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```

### 8. Pamamahala ng Usapan

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Mga Pangunahing Aral

1. **Arkitektura ng Agent**: Ang Microsoft Agent Framework ay nagbibigay ng malinis, type-safe na diskarte sa pagbuo ng AI agents sa .NET
2. **Integrasyon ng Tool**: Ang mga function na may `[Description]` attributes ay nagiging magagamit na mga tool para sa agent
3. **Konteksto ng Usapan**: Ang pamamahala ng thread ay nagbibigay-daan sa multi-turn na usapan na may buong konteksto
4. **Pamamahala ng Konfigurasyon**: Ang mga environment variable at secure na paghawak ng kredensyal ay sumusunod sa pinakamahusay na kasanayan ng .NET
5. **OpenAI Compatibility**: Ang integrasyon ng GitHub Models ay gumagana nang maayos sa pamamagitan ng OpenAI-compatible APIs

## 🔗 Karagdagang Mga Mapagkukunan

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.