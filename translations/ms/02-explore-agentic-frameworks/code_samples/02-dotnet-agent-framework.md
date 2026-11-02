# 🔍 Menerokai Rangka Kerja Ejen Microsoft - Ejen Asas (.NET)

## 📋 Objektif Pembelajaran

Contoh ini meneroka konsep asas Rangka Kerja Ejen Microsoft melalui pelaksanaan ejen asas dalam .NET. Anda akan mempelajari corak teras ejenik dan memahami bagaimana ejen pintar berfungsi menggunakan C# dan ekosistem .NET.

### Apa Yang Akan Anda Temui

- 🏗️ **Seni Bina Ejen**: Memahami struktur asas ejen AI dalam .NET
- 🛠️ **Integrasi Alat**: Bagaimana ejen menggunakan fungsi luar untuk meluaskan keupayaan  
- 💬 **Aliran Perbualan**: Mengurus perbualan berbilang pusingan dan konteks dengan pengurusan thread
- 🔧 **Corak Konfigurasi**: Amalan terbaik untuk penyediaan dan pengurusan ejen dalam .NET

## 🎯 Konsep Utama Yang Diterokai

### Prinsip Rangka Kerja Ejenik

- **Autonomi**: Bagaimana ejen membuat keputusan secara bebas menggunakan abstraksi AI .NET
- **Reaktiviti**: Bertindak balas terhadap perubahan persekitaran dan input pengguna
- **Proaktiviti**: Mengambil inisiatif berdasarkan matlamat dan konteks
- **Kebolehan Sosial**: Berinteraksi melalui bahasa semula jadi dengan thread perbualan

### Komponen Teknikal

- **AIAgent**: Orkestrasi teras ejen dan pengurusan perbualan (.NET)
- **Fungsi Alat**: Meluaskan keupayaan ejen dengan kaedah dan atribut C#
- **Integrasi Azure OpenAI**: Memanfaatkan model bahasa melalui API Respon Azure OpenAI
- **Konfigurasi Selamat**: Pengurusan titik akhir berasaskan persekitaran

## 🔧 Tim Teknikal

### Teknologi Teras

- Rangka Kerja Ejen Microsoft (.NET)
- Integrasi Azure OpenAI (API Respon)
- Corak klien Azure.AI.OpenAI
- Konfigurasi berasaskan persekitaran dengan DotNetEnv

### Keupayaan Ejen

- Pemahaman dan penjanaan bahasa semula jadi
- Panggilan fungsi dan penggunaan alat dengan atribut C#
- Respon peka konteks dengan sesi perbualan
- Seni bina boleh luaskan dengan corak suntikan kebergantungan

## 📚 Perbandingan Rangka Kerja

Contoh ini menunjukkan pendekatan Rangka Kerja Ejen Microsoft berbanding rangka kerja ejenik lain:

| Ciri | Rangka Kerja Ejen Microsoft | Rangka Kerja Lain |
|---------|-------------------------|------------------|
| **Integrasi** | Ekosistem asli Microsoft | Keserasian pelbagai |
| **Kesederhanaan** | API yang bersih, intuitif | Selalunya penyediaan rumit |
| **Kebolehluasan** | Integrasi alat mudah | Bergantung pada rangka kerja |
| **Sedia untuk Perusahaan** | Dibina untuk pengeluaran | Berbeza mengikut rangka kerja |

## 🚀 Memulakan

### Prasyarat

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) atau lebih tinggi
- Sebuah [langganan Azure](https://azure.microsoft.com/free/) dengan sumber Azure OpenAI dan penyebaran model
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — log masuk dengan `az login`

### Pembolehubah Persekitaran Diperlukan

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Kemudian daftar masuk supaya AzureCliCredential dapat mendapatkan token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Kemudian daftar masuk supaya AzureCliCredential boleh mendapatkan token
az login
```

### Contoh Kod

Untuk menjalankan contoh kod,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Atau menggunakan CLI dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Lihat [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) untuk kod lengkap.

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

## 🎓 Isi Penting

1. **Seni Bina Ejen**: Rangka Kerja Ejen Microsoft menyediakan pendekatan bersih dan selamat jenis untuk membina ejen AI dalam .NET
2. **Integrasi Alat**: Fungsi yang dihias dengan atribut `[Description]` menjadi alat tersedia untuk ejen
3. **Konteks Perbualan**: Pengurusan sesi membolehkan perbualan berbilang pusingan dengan kesedaran konteks penuh
4. **Pengurusan Konfigurasi**: Pembolehubah persekitaran dan pengendalian kelayakan selamat mengikut amalan terbaik .NET
5. **Azure OpenAI Responses API**: Ejen menggunakan API Respon Azure OpenAI melalui SDK Azure.AI.OpenAI

## 🔗 Sumber Tambahan

- [Dokumentasi Rangka Kerja Ejen Microsoft](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI dalam Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Aplikasi Fail Tunggal .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->