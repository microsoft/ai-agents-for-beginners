# 🌍 Ejen Pelancongan AI dengan Microsoft Agent Framework (.NET)

## 📋 Gambaran Keseluruhan Senario

Contoh ini menunjukkan cara membina ejen perancangan perjalanan pintar menggunakan Microsoft Agent Framework untuk .NET. Ejen ini boleh secara automatik menghasilkan jadual perjalanan sehari yang diperibadikan untuk destinasi rawak di seluruh dunia.

### Kebolehan Utama:

- 🎲 **Pemilihan Destinasi Rawak**: Menggunakan alat tersuai untuk memilih tempat percutian
- 🗺️ **Perancangan Perjalanan Pintar**: Mencipta jadual perjalanan sehari demi sehari yang terperinci
- 🔄 **Penstriman Masa Nyata**: Menyokong tindak balas segera dan penstriman
- 🛠️ **Integrasi Alat Tersuai**: Menunjukkan bagaimana memperluas kebolehan ejen

## 🔧 Seni Bina Teknikal

### Teknologi Teras

- **Microsoft Agent Framework**: Pelaksanaan .NET terkini untuk pembangunan ejen AI
- **Azure OpenAI (Responses API)**: Menggunakan API Tindak Balas Azure OpenAI untuk inferens model
- **Azure Identity**: Log masuk selamat melalui `AzureCliCredential` (`az login`)
- **Konfigurasi Selamat**: Pengurusan titik akhir berdasarkan persekitaran

### Komponen Utama

1. **AIAgent**: Pengendali utama ejen yang mengendalikan aliran perbualan
2. **Alat Tersuai**: Fungsi `GetRandomDestination()` tersedia untuk ejen
3. **Klien Tindak Balas**: Antara muka perbualan berasaskan Azure OpenAI Responses
4. **Sokongan Penstriman**: Kebolehan menjana tindak balas masa nyata

### Corak Integrasi

```mermaid
graph LR
    A[Permintaan Pengguna] --> B[Ejen AI]
    B --> C[Azure OpenAI (API Respons)]
    B --> D[Alat Destinasi Rawak]
    C --> E[Itinerari Perjalanan]
    D --> E
```

## 🚀 Mula

### Prasyarat

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) atau lebih tinggi
- Sebuah [langganan Azure](https://azure.microsoft.com/free/) dengan sumber Azure OpenAI dan penempatan model
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — log masuk dengan `az login`

### Pembolehubah Persekitaran Diperlukan

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Kemudian daftar masuk supaya AzureCliCredential dapat memperoleh token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Kemudian log masuk supaya AzureCliCredential dapat mendapatkan token
az login
```

### Contoh Kod

Untuk menjalankan contoh kod,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Atau menggunakan CLI dotnet:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Lihat [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) untuk kod lengkap.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
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

## 🎓 Pengajaran Utama

1. **Seni Bina Ejen**: Microsoft Agent Framework menyediakan pendekatan yang bersih dan selamat jenis untuk membina ejen AI dalam .NET
2. **Integrasi Alat**: Fungsi yang dihiasi dengan atribut `[Description]` menjadi alat yang tersedia untuk ejen
3. **Pengurusan Konfigurasi**: Pembolehubah persekitaran dan pengendalian kelayakan selamat mengikut amalan terbaik .NET
4. **API Tindak Balas Azure OpenAI**: Ejen menggunakan API Tindak Balas Azure OpenAI melalui SDK Azure.AI.OpenAI

## 🔗 Sumber Tambahan

- [Dokumentasi Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI dalam Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Aplikasi Fail Tunggal .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->