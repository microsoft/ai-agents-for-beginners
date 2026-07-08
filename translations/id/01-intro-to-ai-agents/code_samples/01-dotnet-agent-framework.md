# 🌍 Agen Perjalanan AI dengan Microsoft Agent Framework (.NET)

## 📋 Ikhtisar Skenario

Contoh ini menunjukkan bagaimana membangun agen perencanaan perjalanan cerdas menggunakan Microsoft Agent Framework untuk .NET. Agen ini dapat secara otomatis menghasilkan rencana perjalanan harian yang dipersonalisasi untuk tujuan acak di seluruh dunia.

### Kemampuan Utama:

- 🎲 **Pemilihan Tujuan Acak**: Menggunakan alat khusus untuk memilih tempat liburan
- 🗺️ **Perencanaan Perjalanan Cerdas**: Membuat rencana perjalanan rinci harian
- 🔄 **Streaming Waktu Nyata**: Mendukung respons langsung dan streaming
- 🛠️ **Integrasi Alat Kustom**: Menunjukkan cara memperluas kemampuan agen

## 🔧 Arsitektur Teknis

### Teknologi Inti

- **Microsoft Agent Framework**: Implementasi .NET terbaru untuk pengembangan agen AI
- **Azure OpenAI (Responses API)**: Menggunakan Azure OpenAI Responses API untuk inferensi model
- **Azure Identity**: Masuk aman melalui `AzureCliCredential` (`az login`)
- **Konfigurasi Aman**: Manajemen endpoint berbasis lingkungan

### Komponen Kunci

1. **AIAgent**: Orkestrator utama agen yang menangani alur percakapan
2. **Alat Kustom**: Fungsi `GetRandomDestination()` tersedia untuk agen
3. **Klien Responses**: Antarmuka percakapan berbasis Azure OpenAI Responses
4. **Dukungan Streaming**: Kemampuan menghasilkan respons waktu nyata

### Pola Integrasi

```mermaid
graph LR
    A[Permintaan Pengguna] --> B[Agen AI]
    B --> C[Azure OpenAI (API Respons)]
    B --> D[Alat GetRandomDestination]
    C --> E[Itinerary Perjalanan]
    D --> E
```

## 🚀 Memulai

### Prasyarat

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) atau lebih tinggi
- [Langganan Azure](https://azure.microsoft.com/free/) dengan sumber daya Azure OpenAI dan penyebaran model
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — masuk dengan `az login`

### Variabel Lingkungan yang Diperlukan

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Kemudian masuk agar AzureCliCredential dapat memperoleh token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Kemudian masuk agar AzureCliCredential dapat memperoleh token
az login
```

### Contoh Kode

Untuk menjalankan contoh kode,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Atau menggunakan CLI dotnet:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Lihat [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) untuk kode lengkap.

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

## 🎓 Poin Penting

1. **Arsitektur Agen**: Microsoft Agent Framework menyediakan pendekatan yang bersih dan tipe-aman untuk membangun agen AI di .NET
2. **Integrasi Alat**: Fungsi yang dilengkapi atribut `[Description]` menjadi alat yang tersedia untuk agen
3. **Manajemen Konfigurasi**: Variabel lingkungan dan penanganan kredensial aman mengikuti praktik terbaik .NET
4. **Azure OpenAI Responses API**: Agen menggunakan Azure OpenAI Responses API melalui SDK Azure.AI.OpenAI

## 🔗 Sumber Daya Tambahan

- [Dokumentasi Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI di Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Aplikasi Berkas Tunggal .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->