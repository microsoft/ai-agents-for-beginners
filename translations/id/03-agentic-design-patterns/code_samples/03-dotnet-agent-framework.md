# 🎨 Pola Desain Agentic dengan Azure OpenAI (Responses API) (.NET)

## 📋 Tujuan Pembelajaran

Contoh ini menunjukkan pola desain kelas perusahaan untuk membangun agen cerdas menggunakan Microsoft Agent Framework di .NET dengan integrasi Azure OpenAI (Responses API). Anda akan mempelajari pola profesional dan pendekatan arsitektur yang membuat agen siap produksi, mudah dipelihara, dan dapat diskalakan.

### Pola Desain Perusahaan

- 🏭 **Factory Pattern**: Pembuatan agen yang distandarisasi dengan dependency injection
- 🔧 **Builder Pattern**: Konfigurasi dan pengaturan agen secara fluent
- 🧵 **Pola Aman-Thread**: Manajemen percakapan secara konkuren
- 📋 **Repository Pattern**: Pengelolaan alat dan kemampuan yang terorganisir

## 🎯 Manfaat Arsitektur Khusus .NET

### Fitur Perusahaan

- **Strong Typing**: Validasi waktu kompilasi dan dukungan IntelliSense
- **Dependency Injection**: Integrasi container DI bawaan
- **Manajemen Konfigurasi**: Pola IConfiguration dan Options
- **Async/Await**: Dukungan pemrograman asinkron kelas pertama

### Pola Siap Produksi

- **Integrasi Logging**: Dukungan ILogger dan logging terstruktur
- **Health Checks**: Monitoring dan diagnosa bawaan
- **Validasi Konfigurasi**: Strong typing dengan anotasi data
- **Penanganan Error**: Manajemen pengecualian terstruktur

## 🔧 Arsitektur Teknis

### Komponen Inti .NET

- **Microsoft.Extensions.AI**: Abstraksi layanan AI terpadu
- **Microsoft.Agents.AI**: Kerangka kerja orkestrasi agen perusahaan
- **Azure OpenAI (Responses API)**: Pola klien API berperforma tinggi
- **Sistem Konfigurasi**: appsettings.json dan integrasi lingkungan

### Implementasi Pola Desain

```mermaid
graph LR
    A[IServiceCollection] --> B[Pembuat Agen]
    B --> C[Konfigurasi]
    C --> D[Registri Alat]
    D --> E[Agen AI]
```

## 🏗️ Pola Perusahaan yang Ditunjukkan

### 1. **Pola Kreasi**

- **Agent Factory**: Pembuatan agen terpusat dengan konfigurasi konsisten
- **Builder Pattern**: API fluent untuk konfigurasi agen kompleks
- **Singleton Pattern**: Pengelolaan sumber daya dan konfigurasi bersama
- **Dependency Injection**: Loose coupling dan kemudahan pengujian

### 2. **Pola Perilaku**

- **Strategy Pattern**: Strategi eksekusi alat yang dapat dipertukarkan
- **Command Pattern**: Operasi agen yang dikapsulkan dengan undo/redo
- **Observer Pattern**: Manajemen siklus hidup agen berbasis peristiwa
- **Template Method**: Alur kerja eksekusi agen yang distandarisasi

### 3. **Pola Struktural**

- **Adapter Pattern**: Lapisan integrasi Azure OpenAI (Responses API)
- **Decorator Pattern**: Peningkatan kemampuan agen
- **Facade Pattern**: Antarmuka interaksi agen yang disederhanakan
- **Proxy Pattern**: Lazy loading dan caching untuk performa

## 📚 Prinsip Desain .NET

### Prinsip SOLID

- **Single Responsibility**: Masing-masing komponen memiliki satu tujuan jelas
- **Open/Closed**: Ekstensibel tanpa modifikasi
- **Liskov Substitution**: Implementasi alat berbasis antarmuka
- **Interface Segregation**: Antarmuka yang fokus dan kohesif
- **Dependency Inversion**: Bergantung pada abstraksi, bukan konkret

### Arsitetur Bersih

- **Domain Layer**: Abstraksi inti agen dan alat
- **Application Layer**: Orkestrasi agen dan alur kerja
- **Infrastructure Layer**: Integrasi Azure OpenAI (Responses API) dan layanan eksternal
- **Presentation Layer**: Interaksi pengguna dan format respons

## 🔒 Pertimbangan Perusahaan

### Keamanan

- **Manajemen Kredensial**: Penanganan kunci API yang aman dengan IConfiguration
- **Validasi Input**: Strong typing dan validasi anotasi data
- **Sanitasi Output**: Pemrosesan dan penyaringan respons yang aman
- **Audit Logging**: Pelacakan operasi yang komprehensif

### Performa

- **Pola Async**: Operasi I/O tanpa blocking
- **Connection Pooling**: Manajemen klien HTTP yang efisien
- **Caching**: Caching respons untuk peningkatan performa
- **Manajemen Sumber Daya**: Pola disposal dan pembersihan yang tepat

### Skalabilitas

- **Thread Safety**: Dukungan eksekusi agen konkuren
- **Resource Pooling**: Pemanfaatan sumber daya yang efisien
- **Manajemen Beban**: Pembatasan laju dan penanganan tekanan balik
- **Monitoring**: Metrik performa dan pemeriksaan kesehatan

## 🚀 Deploy Produksi

- **Manajemen Konfigurasi**: Pengaturan spesifik lingkungan
- **Strategi Logging**: Logging terstruktur dengan correlation ID
- **Penanganan Error**: Penanganan pengecualian global dengan pemulihan tepat
- **Monitoring**: Insights aplikasi dan penghitung performa
- **Pengujian**: Pola unit test, integration test, dan load test

Siap membangun agen cerdas kelas perusahaan dengan .NET? Mari kita arsitek sesuatu yang kokoh! 🏢✨

## 🚀 Memulai

### Prasyarat

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) atau lebih tinggi
- Sebuah [langganan Azure](https://azure.microsoft.com/free/) dengan sumber daya Azure OpenAI dan penerapan model
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — masuk dengan `az login`

### Variabel Lingkungan yang Dibutuhkan

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Kemudian masuk agar AzureCliCredential dapat mendapatkan token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Kemudian masuk sehingga AzureCliCredential dapat memperoleh token
az login
```

### Kode Contoh

Untuk menjalankan contoh kode,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Atau menggunakan dotnet CLI:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Lihat [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) untuk kode lengkap.

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

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
var session = await agent.CreateSessionAsync();

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->