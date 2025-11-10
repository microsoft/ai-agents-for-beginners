<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:38:13+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ms"
}
-->
# 🔍 Meneroka Kerangka Agenik - Agen Asas (.NET)

## 📋 Objektif Pembelajaran

Notebook ini meneroka konsep asas Kerangka Agen Microsoft melalui pelaksanaan agen asas dalam .NET. Anda akan mempelajari corak agenik teras dan memahami bagaimana agen pintar berfungsi di belakang tabir menggunakan C# dan ekosistem .NET.

**Apa yang Akan Anda Pelajari:**
- 🏗️ **Arkitektur Agen**: Memahami struktur asas agen AI dalam .NET
- 🛠️ **Integrasi Alat**: Bagaimana agen menggunakan fungsi luaran untuk memperluaskan keupayaan  
- 💬 **Aliran Perbualan**: Mengurus perbualan berbilang giliran dan konteks dengan pengurusan thread
- 🔧 **Corak Konfigurasi**: Amalan terbaik untuk persediaan dan pengurusan agen dalam .NET

## 🎯 Konsep Utama yang Diliputi

### Prinsip Kerangka Agenik
- **Autonomi**: Bagaimana agen membuat keputusan secara bebas menggunakan abstraksi AI .NET
- **Reaktiviti**: Bertindak balas terhadap perubahan persekitaran dan input pengguna
- **Proaktiviti**: Mengambil inisiatif berdasarkan matlamat dan konteks
- **Kebolehan Sosial**: Berinteraksi melalui bahasa semula jadi dengan thread perbualan

### Komponen Teknikal
- **AIAgent**: Orkestrasi agen teras dan pengurusan perbualan (.NET)
- **Fungsi Alat**: Memperluaskan keupayaan agen dengan kaedah dan atribut C#
- **Integrasi OpenAI**: Memanfaatkan model bahasa melalui API .NET yang standard
- **Pengurusan Persekitaran**: Konfigurasi selamat dan pengendalian kelayakan dengan DotNetEnv

## ⚙️ Prasyarat & Persediaan

**Keperluan Kebergantungan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan sambungan C#

**Pakej NuGet:**
- `Microsoft.Extensions.AI` - Abstraksi AI teras
- `Microsoft.Extensions.AI.OpenAI` - Integrasi OpenAI (pratonton)
- `DotNetEnv` - Pengurusan pembolehubah persekitaran

**Konfigurasi Persekitaran (fail .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Tumpuan Teknikal

**Teknologi Teras:**
- Kerangka Agen Microsoft (.NET)
- Integrasi API Model GitHub
- Corak klien yang serasi dengan OpenAI
- Konfigurasi berasaskan persekitaran dengan DotNetEnv

**Keupayaan Agen:**
- Pemahaman dan penjanaan bahasa semula jadi
- Panggilan fungsi dan penggunaan alat dengan atribut C#
- Respons yang sedar konteks dengan thread perbualan
- Arkitektur yang boleh diperluaskan dengan corak suntikan kebergantungan

## 📚 Perbandingan Kerangka

Contoh ini menunjukkan pendekatan Kerangka Agen Microsoft dalam .NET berbanding platform lain:

| Ciri | Kerangka Agen .NET | Setara Python |
|------|---------------------|---------------|
| **Keselamatan Jenis** | Pengetikan kuat dengan C# | Pengetikan dinamik |
| **Integrasi** | Ekosistem .NET asli | Keserasian yang pelbagai |
| **Prestasi** | Prestasi kod yang dikompilasi | Pelaksanaan yang ditafsirkan |
| **Sedia untuk Perusahaan** | Dibina untuk aplikasi pengeluaran .NET | Berbeza mengikut kerangka |
| **Alat** | Integrasi Visual Studio | Bergantung pada IDE |

## 🚀 Memulakan

Ikuti sel di bawah untuk membina agen asas pertama anda dalam .NET dan memahami konsep agenik asas!

## 📦 Pemasangan dan Persediaan

Contoh ini tersedia sebagai Aplikasi Fail Tunggal .NET yang boleh dijalankan. Lihat fail `02-dotnet-agent-framework.cs` yang disertakan untuk pelaksanaan lengkap.

Untuk menjalankan contoh ini:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Atau menggunakan CLI dotnet:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Penjelasan Kod

Pelaksanaan lengkap termasuk:

### 1. Kebergantungan Pakej

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

### 2. Import Penting

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Konfigurasi Persekitaran

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definisi Fungsi Alat

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

### 5. Persediaan Konfigurasi dan Klien

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

### 6. Konfigurasi Agen

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

### 7. Inisialisasi Agen

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

### 8. Pengurusan Perbualan

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Pengajaran Utama

1. **Arkitektur Agen**: Kerangka Agen Microsoft menyediakan pendekatan yang bersih dan selamat jenis untuk membina agen AI dalam .NET
2. **Integrasi Alat**: Fungsi yang dihiasi dengan atribut `[Description]` menjadi alat yang tersedia untuk agen
3. **Konteks Perbualan**: Pengurusan thread membolehkan perbualan berbilang giliran dengan kesedaran konteks penuh
4. **Pengurusan Konfigurasi**: Pembolehubah persekitaran dan pengendalian kelayakan yang selamat mengikuti amalan terbaik .NET
5. **Keserasian OpenAI**: Integrasi Model GitHub berfungsi dengan lancar melalui API yang serasi dengan OpenAI

## 🔗 Sumber Tambahan

- [Dokumentasi Kerangka Agen Microsoft](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Marketplace Model GitHub](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [Aplikasi Fail Tunggal .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.