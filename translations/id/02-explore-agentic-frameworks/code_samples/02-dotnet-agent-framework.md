<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T13:21:52+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "id"
}
-->
# 🔍 Menjelajahi Microsoft Agent Framework - Agen Dasar (.NET)

## 📋 Tujuan Pembelajaran

Contoh ini mengeksplorasi konsep dasar Microsoft Agent Framework melalui implementasi agen dasar di .NET. Anda akan mempelajari pola-pola agen inti dan memahami cara kerja agen cerdas di balik layar menggunakan C# dan ekosistem .NET.

### Apa yang Akan Anda Temukan

- 🏗️ **Arsitektur Agen**: Memahami struktur dasar agen AI di .NET  
- 🛠️ **Integrasi Alat**: Bagaimana agen menggunakan fungsi eksternal untuk memperluas kemampuan  
- 💬 **Alur Percakapan**: Mengelola percakapan multi-putaran dan konteks dengan manajemen thread  
- 🔧 **Pola Konfigurasi**: Praktik terbaik untuk pengaturan dan manajemen agen di .NET  

## 🎯 Konsep Utama yang Dibahas

### Prinsip Framework Agen

- **Otonomi**: Bagaimana agen membuat keputusan independen menggunakan abstraksi AI .NET  
- **Reaktivitas**: Merespons perubahan lingkungan dan masukan pengguna  
- **Proaktivitas**: Mengambil inisiatif berdasarkan tujuan dan konteks  
- **Kemampuan Sosial**: Berinteraksi melalui bahasa alami dengan thread percakapan  

### Komponen Teknis

- **AIAgent**: Orkestrasi agen inti dan manajemen percakapan (.NET)  
- **Fungsi Alat**: Memperluas kemampuan agen dengan metode dan atribut C#  
- **Integrasi OpenAI**: Memanfaatkan model bahasa melalui API .NET standar  
- **Konfigurasi Aman**: Manajemen kunci API berbasis lingkungan  

## 🔧 Teknologi yang Digunakan

### Teknologi Inti

- Microsoft Agent Framework (.NET)  
- Integrasi API Model GitHub  
- Pola klien kompatibel OpenAI  
- Konfigurasi berbasis lingkungan dengan DotNetEnv  

### Kemampuan Agen

- Pemahaman dan generasi bahasa alami  
- Pemanggilan fungsi dan penggunaan alat dengan atribut C#  
- Respons yang sadar konteks dengan thread percakapan  
- Arsitektur yang dapat diperluas dengan pola injeksi dependensi  

## 📚 Perbandingan Framework

Contoh ini menunjukkan pendekatan Microsoft Agent Framework dibandingkan dengan framework agen lainnya:

| Fitur | Microsoft Agent Framework | Framework Lainnya |
|-------|---------------------------|-------------------|
| **Integrasi** | Ekosistem Microsoft asli | Kompatibilitas bervariasi |
| **Kesederhanaan** | API yang bersih dan intuitif | Sering kali pengaturan kompleks |
| **Ekstensibilitas** | Integrasi alat yang mudah | Bergantung pada framework |
| **Siap untuk Perusahaan** | Dibangun untuk produksi | Bervariasi tergantung framework |

## 🚀 Memulai

### Prasyarat

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) atau lebih tinggi  
- [Token akses API Model GitHub](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Variabel Lingkungan yang Diperlukan

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
  

### Contoh Kode

Untuk menjalankan contoh kode,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
Atau menggunakan CLI dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Lihat [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) untuk kode lengkapnya.

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
  

## 🎓 Kesimpulan Utama

1. **Arsitektur Agen**: Microsoft Agent Framework menyediakan pendekatan yang bersih dan aman tipe untuk membangun agen AI di .NET  
2. **Integrasi Alat**: Fungsi yang dihiasi dengan atribut `[Description]` menjadi alat yang tersedia untuk agen  
3. **Konteks Percakapan**: Manajemen thread memungkinkan percakapan multi-putaran dengan kesadaran konteks penuh  
4. **Manajemen Konfigurasi**: Variabel lingkungan dan penanganan kredensial yang aman mengikuti praktik terbaik .NET  
5. **Kompatibilitas OpenAI**: Integrasi Model GitHub bekerja dengan mulus melalui API yang kompatibel dengan OpenAI  

## 🔗 Sumber Daya Tambahan

- [Dokumentasi Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)  
- [Marketplace Model GitHub](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->