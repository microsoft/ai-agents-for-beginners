# 🛠️ Penggunaan Alat Lanjutan dengan Azure OpenAI (API Respons) (.NET)

## 📋 Objektif Pembelajaran

Buku nota ini menunjukkan corak integrasi alat tahap perusahaan menggunakan Microsoft Agent Framework dalam .NET dengan Azure OpenAI (API Respons). Anda akan belajar membina ejen canggih dengan pelbagai alat khusus, menggunakan jenis kuat C# dan ciri perusahaan .NET.

### Keupayaan Alat Lanjutan yang Akan Anda Kuasai

- 🔧 **Senibina Pelbagai Alat**: Membina ejen dengan pelbagai keupayaan khusus
- 🎯 **Pelaksanaan Alat Selamat Jenis**: Memanfaatkan pengesahan masa kompilasi C#
- 📊 **Corak Alat Perusahaan**: Reka bentuk alat sedia produksi dan pengendalian ralat
- 🔗 **Komposisi Alat**: Menggabungkan alat untuk aliran kerja perniagaan yang kompleks

## 🎯 Manfaat Senibina Alat .NET

### Ciri-Ciri Alat Perusahaan

- **Pengesahan Masa Kompilasi**: Typing yang kuat memastikan ketepatan parameter alat
- **Suntikan Kebergantungan**: Integrasi bekas IoC untuk pengurusan alat
- **Corak Async/Await**: Pelaksanaan alat tanpa penyekat dengan pengurusan sumber yang betul
- **Logging Berstruktur**: Integrasi logging terbina dalam untuk pemantauan pelaksanaan alat

### Corak Sedia Produksi

- **Pengendalian Pengecualian**: Pengurusan ralat menyeluruh dengan pengecualian bertip
- **Pengurusan Sumber**: Corak pelupusan yang betul dan pengurusan memori
- **Pemantauan Prestasi**: Metrik dan penunjuk prestasi terbina dalam
- **Pengurusan Konfigurasi**: Konfigurasi selamat jenis dengan pengesahan

## 🔧 Senibina Teknikal

### Komponen Alat Teras .NET

- **Microsoft.Extensions.AI**: Lapisan abstraksi alat bersatu
- **Microsoft.Agents.AI**: Orkestra alat tahap perusahaan
- **Azure OpenAI (API Respons)**: Klien API berprestasi tinggi dengan kolam sambungan

### Saluran Pelaksanaan Alat

```mermaid
graph LR
    A[Permintaan Pengguna] --> B[Analisis Ejen]
    B --> C[Pemilihan Alat]
    C --> D[Pengesahan Jenis]
    B --> E[Pengikatan Parameter]
    E --> F[Pelaksanaan Alat]
    C --> F
    F --> G[Pemprosesan Keputusan]
    D --> G
    G --> H[Respons]
```

## 🛠️ Kategori & Corak Alat

### 1. **Alat Pemprosesan Data**

- **Pengesahan Input**: Typing kuat dengan anotasi data
- **Operasi Penukaran**: Penukaran dan pemformatan data selamat jenis
- **Logik Perniagaan**: Alat pengiraan dan analisis khusus domain
- **Pemformatan Output**: Penjanaan respons berstruktur

### 2. **Alat Integrasi**

- **Penyambung API**: Integrasi perkhidmatan RESTful dengan HttpClient
- **Alat Pangkalan Data**: Integrasi Entity Framework untuk akses data
- **Operasi Fail**: Operasi sistem fail selamat dengan pengesahan
- **Perkhidmatan Luaran**: Corak integrasi perkhidmatan pihak ketiga

### 3. **Alat Utiliti**

- **Pemprosesan Teks**: Manipulasi rentetan dan utiliti pemformatan
- **Operasi Tarikh/Masa**: Pengiraan tarikh/masa berasaskan budaya
- **Alat Matematik**: Pengiraan ketepatan dan operasi statistik
- **Alat Pengesahan**: Pengesahan peraturan perniagaan dan verifikasi data

Sedia untuk membina ejen tahap perusahaan dengan keupayaan alat kuat dan selamat jenis dalam .NET? Mari kita mereka bentuk penyelesaian profesional! 🏢⚡

## 🚀 Bermula

### Prasyarat

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) atau lebih tinggi
- Sebuah [langganan Azure](https://azure.microsoft.com/free/) dengan sumber Azure OpenAI dan pelancaran model
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — log masuk dengan `az login`

### Pembolehubah Persekitaran Diperlukan

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Kemudian log masuk supaya AzureCliCredential boleh mendapatkan token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Kemudian daftar masuk supaya AzureCliCredential boleh mendapatkan token
az login
```

### Contoh Kod

Untuk menjalankan contoh kod,

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Atau menggunakan CLI dotnet:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Lihat [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) untuk kod lengkap.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

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
    .GetOpenAIResponseClient(deployment)
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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->