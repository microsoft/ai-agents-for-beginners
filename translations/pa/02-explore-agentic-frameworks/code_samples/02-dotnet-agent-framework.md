<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:34:25+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "pa"
}
-->
# 🔍 ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਦੀ ਖੋਜ - ਬੇਸਿਕ ਏਜੰਟ (.NET)

## 📋 ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਹ ਨੋਟਬੁੱਕ Microsoft Agent Framework ਦੇ ਮੁੱਢਲੇ ਸਿਧਾਂਤਾਂ ਨੂੰ .NET ਵਿੱਚ ਇੱਕ ਬੇਸਿਕ ਏਜੰਟ ਦੇ ਨImplementation ਰਾਹੀਂ ਸਮਝਾਉਂਦੀ ਹੈ। ਤੁਸੀਂ ਕੋਰ ਏਜੰਟਿਕ ਪੈਟਰਨ ਸਿੱਖੋਗੇ ਅਤੇ ਸਮਝੋਗੇ ਕਿ C# ਅਤੇ .NET ecosystem ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਮਰਥ ਏਜੰਟ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ।

**ਤੁਹਾਨੂੰ ਕੀ ਪਤਾ ਲੱਗੇਗਾ:**
- 🏗️ **ਏਜੰਟ ਆਰਕੀਟੈਕਚਰ**: .NET ਵਿੱਚ AI ਏਜੰਟਾਂ ਦੀ ਬੁਨਿਆਦੀ ਬਣਤਰ ਨੂੰ ਸਮਝਣਾ
- 🛠️ **ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਕਿਵੇਂ ਏਜੰਟ ਬਾਹਰੀ ਫੰਕਸ਼ਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਮਰਥਾ ਵਧਾਉਂਦੇ ਹਨ  
- 💬 **ਕੰਵਰਸੇਸ਼ਨ ਫਲੋ**: ਮਲਟੀ-ਟਰਨ ਗੱਲਬਾਤਾਂ ਅਤੇ ਥ੍ਰੈਡ ਮੈਨੇਜਮੈਂਟ ਨਾਲ ਸੰਦਰਭ ਦਾ ਪ੍ਰਬੰਧਨ
- 🔧 **ਕੰਫਿਗਰੇਸ਼ਨ ਪੈਟਰਨ**: .NET ਵਿੱਚ ਏਜੰਟ ਸੈਟਅਪ ਅਤੇ ਮੈਨੇਜਮੈਂਟ ਲਈ ਸ੍ਰੇਸ਼ਠ ਤਰੀਕੇ

## 🎯 ਮੁੱਖ ਸਿਧਾਂਤ

### ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਦੇ ਸਿਧਾਂਤ
- **ਆਟੋਨੋਮੀ**: .NET AI abstractions ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਏਜੰਟ ਕਿਵੇਂ ਸੁਤੰਤਰ ਫੈਸਲੇ ਲੈਂਦੇ ਹਨ
- **ਰੀਐਕਟਿਵਿਟੀ**: ਵਾਤਾਵਰਣ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਅਤੇ ਯੂਜ਼ਰ ਇਨਪੁਟਸ ਦਾ ਜਵਾਬ ਦੇਣਾ
- **ਪ੍ਰੋਐਕਟਿਵਿਟੀ**: ਲਕਸ਼ਾਂ ਅਤੇ ਸੰਦਰਭ ਦੇ ਆਧਾਰ 'ਤੇ ਪਹਲ ਕਰਨਾ
- **ਸੋਸ਼ਲ ਐਬਿਲਿਟੀ**: ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਰਾਹੀਂ ਗੱਲਬਾਤ ਥ੍ਰੈਡਾਂ ਨਾਲ ਸੰਚਾਰ ਕਰਨਾ

### ਤਕਨੀਕੀ ਹਿੱਸੇ
- **AIAgent**: ਕੋਰ ਏਜੰਟ orchestration ਅਤੇ ਗੱਲਬਾਤ ਮੈਨੇਜਮੈਂਟ (.NET)
- **ਟੂਲ ਫੰਕਸ਼ਨ**: C# ਮੈਥਡਸ ਅਤੇ attributes ਨਾਲ ਏਜੰਟ ਸਮਰਥਾ ਵਧਾਉਣਾ
- **OpenAI ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: .NET APIs ਰਾਹੀਂ ਭਾਸ਼ਾ ਮਾਡਲ ਦੀ ਵਰਤੋਂ
- **Environment Management**: DotNetEnv ਨਾਲ ਸੁਰੱਖਿਅਤ ਕੰਫਿਗਰੇਸ਼ਨ ਅਤੇ credential ਹੈਂਡਲਿੰਗ

## ⚙️ ਪੂਰਵ ਸ਼ਰਤਾਂ ਅਤੇ ਸੈਟਅਪ

**ਲੋੜੀਂਦੇ Dependencies:**
- .NET 9.0 SDK ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ
- Visual Studio 2022 ਜਾਂ VS Code C# ਐਕਸਟੈਂਸ਼ਨ ਨਾਲ

**NuGet ਪੈਕੇਜ:**
- `Microsoft.Extensions.AI` - ਕੋਰ AI abstractions
- `Microsoft.Extensions.AI.OpenAI` - OpenAI ਇੰਟੀਗ੍ਰੇਸ਼ਨ (preview)
- `DotNetEnv` - Environment variable ਮੈਨੇਜਮੈਂਟ

**Environment Configuration (.env ਫਾਈਲ):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 ਤਕਨੀਕੀ ਸਟੈਕ

**ਕੋਰ ਤਕਨਾਲੋਜੀ:**
- Microsoft Agent Framework (.NET)
- GitHub Models API ਇੰਟੀਗ੍ਰੇਸ਼ਨ
- OpenAI-compatible client patterns
- DotNetEnv ਨਾਲ Environment-ਅਧਾਰਿਤ ਕੰਫਿਗਰੇਸ਼ਨ

**ਏਜੰਟ ਸਮਰਥਾ:**
- ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੀ ਸਮਝ ਅਤੇ ਜਨਰੇਸ਼ਨ
- C# attributes ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਅਤੇ ਟੂਲ ਵਰਤੋਂ
- ਗੱਲਬਾਤ ਥ੍ਰੈਡਾਂ ਨਾਲ ਸੰਦਰਭ-ਜਾਗਰੂਕ ਜਵਾਬ
- Dependency injection patterns ਨਾਲ ਵਧਾਉਣਯੋਗ ਆਰਕੀਟੈਕਚਰ

## 📚 ਫਰੇਮਵਰਕ ਦੀ ਤੁਲਨਾ

ਇਹ ਉਦਾਹਰਨ .NET ਵਿੱਚ Microsoft Agent Framework ਦੇ ਦ੍ਰਿਸ਼ਟੀਕੋਣ ਨੂੰ ਹੋਰ ਪਲੇਟਫਾਰਮਾਂ ਨਾਲ ਤੁਲਨਾ ਕਰਦੀ ਹੈ:

| ਫੀਚਰ | .NET Agent Framework | Python ਸਮਾਨ |
|---------|---------------------|-------------------|
| **ਟਾਈਪ ਸੇਫਟੀ** | C# ਨਾਲ ਮਜ਼ਬੂਤ typing | Dynamic typing |
| **ਇੰਟੀਗ੍ਰੇਸ਼ਨ** | ਮੂਲ .NET ecosystem | ਵੱਖ-ਵੱਖ compatibility |
| **ਪਰਫਾਰਮੈਂਸ** | Compiled code performance | Interpreted execution |
| **ਐਂਟਰਪ੍ਰਾਈਜ਼ ਤਿਆਰ** | ਪ੍ਰੋਡਕਸ਼ਨ .NET apps ਲਈ ਬਣਾਇਆ ਗਿਆ | Framework 'ਤੇ ਨਿਰਭਰ |
| **ਟੂਲਿੰਗ** | Visual Studio ਇੰਟੀਗ੍ਰੇਸ਼ਨ | IDE-ਨਿਰਭਰ |

## 🚀 ਸ਼ੁਰੂਆਤ

ਹੇਠਾਂ ਦਿੱਤੇ ਸੈੱਲਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ ਤਾਂ ਜੋ .NET ਵਿੱਚ ਆਪਣਾ ਪਹਿਲਾ ਬੇਸਿਕ ਏਜੰਟ ਬਣਾਉਣ ਅਤੇ ਮੁੱਢਲੇ ਏਜੰਟਿਕ ਸਿਧਾਂਤਾਂ ਨੂੰ ਸਮਝਣ ਲਈ!

## 📦 ਇੰਸਟਾਲੇਸ਼ਨ ਅਤੇ ਸੈਟਅਪ

ਇਹ ਉਦਾਹਰਨ ਇੱਕ runnable .NET Single File App ਵਜੋਂ ਉਪਲਬਧ ਹੈ। ਪੂਰੀ Implementation ਲਈ `02-dotnet-agent-framework.cs` ਫਾਈਲ ਦੇਖੋ।

ਇਸ ਉਦਾਹਰਨ ਨੂੰ ਚਲਾਉਣ ਲਈ:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

ਜਾਂ dotnet CLI ਦੀ ਵਰਤੋਂ ਕਰਕੇ:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 ਕੋਡ ਵਾਕਥਰੂ

ਪੂਰੀ Implementation ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ:

### 1. ਪੈਕੇਜ Dependencies

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

### 2. ਜ਼ਰੂਰੀ Imports

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Environment Configuration

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. ਟੂਲ ਫੰਕਸ਼ਨ ਡਿਫਿਨੀਸ਼ਨ

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

### 5. ਕੰਫਿਗਰੇਸ਼ਨ ਅਤੇ ਕਲਾਇੰਟ ਸੈਟਅਪ

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

### 6. ਏਜੰਟ ਕੰਫਿਗਰੇਸ਼ਨ

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

### 7. ਏਜੰਟ ਇਨਿਸ਼ੀਅਲਾਈਜ਼ੇਸ਼ਨ

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

### 8. ਗੱਲਬਾਤ ਮੈਨੇਜਮੈਂਟ

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 ਮੁੱਖ ਸਿੱਖਿਆ

1. **ਏਜੰਟ ਆਰਕੀਟੈਕਚਰ**: Microsoft Agent Framework .NET ਵਿੱਚ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਇੱਕ ਸਾਫ਼, type-safe ਦ੍ਰਿਸ਼ਟੀਕੋਣ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ
2. **ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: `[Description]` attributes ਨਾਲ ਸਜਾਏ ਫੰਕਸ਼ਨ ਏਜੰਟ ਲਈ ਉਪਲਬਧ ਟੂਲ ਬਣ ਜਾਂਦੇ ਹਨ
3. **ਗੱਲਬਾਤ ਸੰਦਰਭ**: ਥ੍ਰੈਡ ਮੈਨੇਜਮੈਂਟ ਮਲਟੀ-ਟਰਨ ਗੱਲਬਾਤਾਂ ਨੂੰ ਪੂਰੇ ਸੰਦਰਭ ਜਾਗਰੂਕਤਾ ਨਾਲ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ
4. **ਕੰਫਿਗਰੇਸ਼ਨ ਮੈਨੇਜਮੈਂਟ**: Environment variables ਅਤੇ ਸੁਰੱਖਿਅਤ credential ਹੈਂਡਲਿੰਗ .NET ਦੇ ਸ੍ਰੇਸ਼ਠ ਤਰੀਕਿਆਂ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹਨ
5. **OpenAI Compatibility**: GitHub Models ਇੰਟੀਗ੍ਰੇਸ਼ਨ OpenAI-compatible APIs ਰਾਹੀਂ ਬੇਰੁਕਾਵਟ ਕੰਮ ਕਰਦਾ ਹੈ

## 🔗 ਵਾਧੂ ਸਰੋਤ

- [Microsoft Agent Framework Documentation](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।