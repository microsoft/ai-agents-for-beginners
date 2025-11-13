<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T12:26:33+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "tr"
}
-->
# 🔍 Microsoft Agent Framework'ü Keşfetmek - Temel Agent (.NET)

## 📋 Öğrenme Hedefleri

Bu örnek, Microsoft Agent Framework'ün temel kavramlarını .NET'te bir temel agent uygulaması üzerinden keşfetmektedir. C# ve .NET ekosistemini kullanarak akıllı agentlerin nasıl çalıştığını ve temel agentik desenleri öğreneceksiniz.

### Keşfedecekleriniz

- 🏗️ **Agent Mimarisi**: .NET'teki yapay zeka agentlerinin temel yapısını anlama  
- 🛠️ **Araç Entegrasyonu**: Agentlerin yeteneklerini genişletmek için harici fonksiyonları nasıl kullandığı  
- 💬 **Konuşma Akışı**: Çoklu dönüşlü konuşmaları ve bağlamı thread yönetimi ile nasıl yöneteceğiniz  
- 🔧 **Konfigürasyon Desenleri**: .NET'te agent kurulum ve yönetimi için en iyi uygulamalar  

## 🎯 Ele Alınan Temel Kavramlar

### Agentik Framework İlkeleri

- **Otonomi**: Agentlerin .NET AI soyutlamalarını kullanarak bağımsız kararlar alması  
- **Reaktivite**: Çevresel değişikliklere ve kullanıcı girdilerine tepki verme  
- **Proaktivite**: Hedefler ve bağlam temelinde inisiyatif alma  
- **Sosyal Yetenek**: Konuşma thread'leri aracılığıyla doğal dilde etkileşim kurma  

### Teknik Bileşenler

- **AIAgent**: Temel agent orkestrasyonu ve konuşma yönetimi (.NET)  
- **Araç Fonksiyonları**: C# metodları ve attributeleri ile agent yeteneklerini genişletme  
- **OpenAI Entegrasyonu**: Standartlaştırılmış .NET API'leri aracılığıyla dil modellerinden yararlanma  
- **Güvenli Konfigürasyon**: Çevreye dayalı API anahtarı yönetimi  

## 🔧 Teknik Yığın

### Temel Teknolojiler

- Microsoft Agent Framework (.NET)  
- GitHub Models API entegrasyonu  
- OpenAI uyumlu istemci desenleri  
- DotNetEnv ile çevreye dayalı konfigürasyon  

### Agent Yetenekleri

- Doğal dil anlama ve üretme  
- C# attributeleri ile fonksiyon çağırma ve araç kullanımı  
- Konuşma thread'leri ile bağlam farkındalığına sahip yanıtlar  
- Bağımlılık enjeksiyonu desenleri ile genişletilebilir mimari  

## 📚 Framework Karşılaştırması

Bu örnek, Microsoft Agent Framework yaklaşımını diğer agentik frameworklerle karşılaştırmaktadır:

| Özellik | Microsoft Agent Framework | Diğer Frameworkler |
|---------|-------------------------|------------------|
| **Entegrasyon** | Microsoft ekosistemine özgü | Çeşitli uyumluluk |
| **Basitlik** | Temiz, sezgisel API | Genellikle karmaşık kurulum |
| **Genişletilebilirlik** | Kolay araç entegrasyonu | Framework'e bağlı |
| **Kurumsal Hazır** | Üretim için tasarlanmış | Framework'e göre değişir |

## 🚀 Başlarken

### Ön Koşullar

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) veya daha yüksek  
- [GitHub Models API erişim tokeni](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Gerekli Çevre Değişkenleri

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### Örnek Kod

Kod örneğini çalıştırmak için,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Veya dotnet CLI kullanarak:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Tam kod için [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) dosyasına bakın.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
var AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
"Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?"

Always prioritize user preferences. If they mention a specific destination like "Bali" or "Paris," focus your planning on that location rather than suggesting alternatives.
""";

// Create AI Agent with Advanced Travel Planning Capabilities
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```
  

## 🎓 Temel Çıkarımlar

1. **Agent Mimarisi**: Microsoft Agent Framework, .NET'te yapay zeka agentleri oluşturmak için temiz ve tür güvenli bir yaklaşım sunar  
2. **Araç Entegrasyonu**: `[Description]` attributeleri ile süslenmiş fonksiyonlar, agent için kullanılabilir araçlar haline gelir  
3. **Konuşma Bağlamı**: Thread yönetimi, çoklu dönüşlü konuşmaların tam bağlam farkındalığı ile yönetilmesini sağlar  
4. **Konfigürasyon Yönetimi**: Çevre değişkenleri ve güvenli kimlik bilgisi yönetimi, .NET en iyi uygulamalarını takip eder  
5. **OpenAI Uyumluluğu**: GitHub Models entegrasyonu, OpenAI uyumlu API'ler aracılığıyla sorunsuz çalışır  

## 🔗 Ek Kaynaklar

- [Microsoft Agent Framework Belgeleri](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Tek Dosya Uygulamaları](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->