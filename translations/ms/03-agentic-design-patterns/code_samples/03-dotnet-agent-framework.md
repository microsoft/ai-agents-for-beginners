# 🎨 Corak Reka Bentuk Agensik dengan Azure OpenAI (Responses API) (.NET)

## 📋 Objektif Pembelajaran

Contoh ini menunjukkan corak reka bentuk kelas perusahaan bagi membina ejen pintar menggunakan Microsoft Agent Framework dalam .NET dengan integrasi Azure OpenAI (Responses API). Anda akan mempelajari corak profesional dan pendekatan seni bina yang menjadikan agen sedia untuk produksi, mudah dijaga dan boleh diskalakan.

### Corak Reka Bentuk Perusahaan

- 🏭 **Corak Kilang**: Penciptaan agen yang standard dengan suntikan kebergantungan
- 🔧 **Corak Pembina**: Konfigurasi dan penyediaan agen secara fasih
- 🧵 **Corak Selamat-Tali**: Pengurusan perbualan serentak
- 📋 **Corak Repositori**: Pengurusan alat dan keupayaan yang tersusun

## 🎯 Manfaat Seni Bina Khusus .NET

### Ciri-ciri Perusahaan

- **Pengetikan Kuat**: Pengesahan masa kompilasi dan sokongan IntelliSense
- **Suntikan Kebergantungan**: Integrasi kontena DI terbina dalam
- **Pengurusan Konfigurasi**: Corak IConfiguration dan Options
- **Async/Await**: Sokongan pengaturcaraan tak segerak kelas pertama

### Corak Sedia Produksi

- **Integrasi Log**: ILogger dan sokongan log berstruktur
- **Pemeriksaan Kesihatan**: Pemantauan dan diagnostik terbina dalam
- **Pengesahan Konfigurasi**: Pengetikan kuat dengan anotasi data
- **Pengendalian Ralat**: Pengurusan pengecualian berstruktur

## 🔧 Seni Bina Teknikal

### Komponen Teras .NET

- **Microsoft.Extensions.AI**: Abstraksi perkhidmatan AI bersatu
- **Microsoft.Agents.AI**: Rangka kerja orkestrasi agen perusahaan
- **Azure OpenAI (Responses API)**: Corak klien API berprestasi tinggi
- **Sistem Konfigurasi**: appsettings.json dan integrasi persekitaran

### Pelaksanaan Corak Reka Bentuk

```mermaid
graph LR
    A[Koleksi Perkhidmatan] --> B[Pembina Ejen]
    B --> C[Konfigurasi]
    C --> D[Daftar Alat]
    D --> E[Ejen AI]
```

## 🏗️ Corak Perusahaan Ditunjukkan

### 1. **Corak Kreatif**

- **Kilang Agen**: Penciptaan agen berpusat dengan konfigurasi konsisten
- **Corak Pembina**: API fasih untuk konfigurasi agen kompleks
- **Corak Singleton**: Sumber dan pengurusan konfigurasi dikongsi
- **Suntikan Kebergantungan**: Pautan longgar dan kebolehujian

### 2. **Corak Tingkah Laku**

- **Corak Strategi**: Strategi pelaksanaan alat boleh ditukar ganti
- **Corak Arahan**: Operasi agen terbungkus dengan undo/redo
- **Corak Pemerhati**: Pengurusan kitaran hidup agen berasaskan acara
- **Kaedah Templat**: Aliran kerja pelaksanaan agen yang distandardkan

### 3. **Corak Struktur**

- **Corak Penyesuai**: Lapisan integrasi Azure OpenAI (Responses API)
- **Corak Dekorator**: Peningkatan keupayaan agen
- **Corak Fasad**: Antara muka interaksi agen yang dipermudahkan
- **Corak Proksi**: Pemuatan malas dan cache untuk prestasi

## 📚 Prinsip Reka Bentuk .NET

### Prinsip SOLID

- **Tanggungjawab Tunggal**: Setiap komponen mempunyai satu tujuan jelas
- **Terbuka/Tertutup**: Boleh dikembangkan tanpa pengubahsuaian
- **Penggantian Liskov**: Pelaksanaan alat berasaskan antara muka
- **Pengasingan Antara Muka**: Antara muka fokus dan kohesif
- **Pembalikan Kebergantungan**: Bergantung pada abstraksi, bukan konkrit

### Seni Bina Bersih

- **Lapisan Domain**: Abstraksi teras agen dan alat
- **Lapisan Aplikasi**: Orkestrasi agen dan aliran kerja
- **Lapisan Infrastruktur**: Integrasi Azure OpenAI (Responses API) dan perkhidmatan luaran
- **Lapisan Pembentangan**: Interaksi pengguna dan pemformatan tindak balas

## 🔒 Pertimbangan Perusahaan

### Keselamatan

- **Pengurusan Credential**: Pengendalian kunci API selamat dengan IConfiguration
- **Pengesahan Input**: Pengetikan kuat dan pengesahan anotasi data
- **Sanitisasi Output**: Pemprosesan dan penapisan tindak balas selamat
- **Log Audit**: Penjejakan operasi menyeluruh

### Prestasi

- **Corak Async**: Operasi I/O tanpa penyekat
- **Penggiliran Sambungan**: Pengurusan klien HTTP cekap
- **Caching**: Cache tindak balas untuk prestasi dipertingkat
- **Pengurusan Sumber**: Pola pelupusan dan pembersihan yang betul

### Skalabiliti

- **Keselamatan Tali**: Sokongan pelaksanaan agen serentak
- **Penggiliran Sumber**: Penggunaan sumber cekap
- **Pengurusan Beban**: Had kadar dan pengendalian tekanan balik
- **Pemantauan**: Metrik prestasi dan pemeriksaan kesihatan

## 🚀 Pengeluaran Produksi

- **Pengurusan Konfigurasi**: Tetapan khusus persekitaran
- **Strategi Log**: Log berstruktur dengan ID korelasi
- **Pengendalian Ralat**: Pengendalian pengecualian global dengan pemulihan betul
- **Pemantauan**: Wawasan aplikasi dan pemantau prestasi
- **Ujian**: Ujian unit, ujian integrasi, dan corak ujian beban

Sedia untuk membina agen pintar kelas perusahaan dengan .NET? Mari bina sesuatu yang kukuh! 🏢✨

## 🚀 Memulakan

### Pra-syarat

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) atau lebih tinggi
- [Langganan Azure](https://azure.microsoft.com/free/) dengan sumber Azure OpenAI dan pelaksanaan model
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — log masuk dengan `az login`

### Pembolehubah Persekitaran Diperlukan

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Kemudian log masuk supaya AzureCliCredential dapat memperoleh token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Kemudian daftar masuk supaya AzureCliCredential dapat memperoleh token
az login
```

### Kod Contoh

Untuk menjalankan contoh kod,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

Atau menggunakan CLI dotnet:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Lihat [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) untuk kod lengkap.

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
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->