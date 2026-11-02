# 🔍 Menjelajahi Microsoft Agent Framework - Agen Dasar (.NET)

## 📋 Tujuan Pembelajaran

Contoh ini mengeksplorasi konsep dasar Microsoft Agent Framework melalui implementasi agen dasar di .NET. Anda akan mempelajari pola agen inti dan memahami bagaimana agen cerdas bekerja secara mendalam menggunakan C# dan ekosistem .NET.

### Apa yang Akan Anda Temukan

- 🏗️ **Arsitektur Agen**: Memahami struktur dasar agen AI di .NET
- 🛠️ **Integrasi Alat**: Bagaimana agen menggunakan fungsi eksternal untuk memperluas kemampuan  
- 💬 **Alur Percakapan**: Mengelola percakapan multi-putar dan konteks dengan manajemen thread
- 🔧 **Pola Konfigurasi**: Praktik terbaik untuk pengaturan dan manajemen agen di .NET

## 🎯 Konsep Kunci yang Dibahas

### Prinsip Framework Agenik

- **Otonomi**: Bagaimana agen membuat keputusan mandiri menggunakan abstraksi AI .NET
- **Reaktivitas**: Merespons perubahan lingkungan dan input pengguna
- **Proaktivitas**: Mengambil inisiatif berdasarkan tujuan dan konteks
- **Kemampuan Sosial**: Berinteraksi melalui bahasa alami dengan utas percakapan

### Komponen Teknis

- **AIAgent**: Orkestrasi inti agen dan manajemen percakapan (.NET)
- **Fungsi Alat**: Memperluas kemampuan agen dengan metode dan atribut C#
- **Integrasi Azure OpenAI**: Memanfaatkan model bahasa melalui Azure OpenAI Responses API
- **Konfigurasi Aman**: Manajemen endpoint berbasis lingkungan

## 🔧 Tumpukan Teknologi

### Teknologi Inti

- Microsoft Agent Framework (.NET)
- Integrasi Azure OpenAI (Responses API)
- Pola klien Azure.AI.OpenAI
- Konfigurasi berbasis lingkungan dengan DotNetEnv

### Kemampuan Agen

- Pemahaman dan generasi bahasa alami
- Pemanggilan fungsi dan penggunaan alat dengan atribut C#
- Respons yang sadar konteks dengan sesi percakapan
- Arsitektur yang dapat diperluas dengan pola dependency injection

## 📚 Perbandingan Framework

Contoh ini menunjukkan pendekatan Microsoft Agent Framework dibandingkan dengan framework agenik lainnya:

| Fitur | Microsoft Agent Framework | Framework Lain |
|---------|-------------------------|------------------|
| **Integrasi** | Ekosistem Microsoft asli | Kompatibilitas bervariasi |
| **Kesederhanaan** | API yang bersih dan intuitif | Sering konfigurasi kompleks |
| **Ekstensibilitas** | Integrasi alat mudah | Bergantung pada framework |
| **Siap Enterprise** | Dibangun untuk produksi | Bervariasi menurut framework |

## 🚀 Memulai

### Prasyarat

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) atau lebih tinggi
- [Langganan Azure](https://azure.microsoft.com/free/) dengan sumber daya Azure OpenAI dan penyebaran model
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — masuk dengan `az login`

### Variabel Lingkungan yang Diperlukan

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Kemudian masuk agar AzureCliCredential dapat memperoleh token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Kemudian masuk agar AzureCliCredential dapat mengambil token
az login
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

Lihat [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) untuk kode lengkap.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

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
// Get the Responses client for the deployment and create the AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Kesimpulan Utama

1. **Arsitektur Agen**: Microsoft Agent Framework menyediakan pendekatan yang bersih dan type-safe untuk membangun agen AI di .NET
2. **Integrasi Alat**: Fungsi yang diberi atribut `[Description]` menjadi alat yang tersedia untuk agen
3. **Konteks Percakapan**: Manajemen sesi memungkinkan percakapan multi-putar dengan kesadaran konteks penuh
4. **Manajemen Konfigurasi**: Variabel lingkungan dan penanganan kredensial aman mengikuti praktik terbaik .NET
5. **Azure OpenAI Responses API**: Agen menggunakan Azure OpenAI Responses API melalui Azure.AI.OpenAI SDK

## 🔗 Sumber Daya Tambahan

- [Dokumentasi Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI di Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Aplikasi Single File .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->