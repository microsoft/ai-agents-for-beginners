<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:38:03+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "id"
}
-->
# 🔍 Menjelajahi Kerangka Agentic - Agen Dasar (.NET)

## 📋 Tujuan Pembelajaran

Notebook ini mengeksplorasi konsep dasar dari Microsoft Agent Framework melalui implementasi agen dasar di .NET. Anda akan mempelajari pola-pola agentic inti dan memahami cara kerja agen cerdas di balik layar menggunakan C# dan ekosistem .NET.

**Apa yang Akan Anda Pelajari:**
- 🏗️ **Arsitektur Agen**: Memahami struktur dasar agen AI di .NET
- 🛠️ **Integrasi Alat**: Bagaimana agen menggunakan fungsi eksternal untuk memperluas kemampuan  
- 💬 **Alur Percakapan**: Mengelola percakapan multi-putaran dan konteks dengan manajemen thread
- 🔧 **Pola Konfigurasi**: Praktik terbaik untuk pengaturan dan manajemen agen di .NET

## 🎯 Konsep Utama yang Dibahas

### Prinsip Kerangka Agentic
- **Otonomi**: Bagaimana agen membuat keputusan independen menggunakan abstraksi AI .NET
- **Reaktivitas**: Merespons perubahan lingkungan dan masukan pengguna
- **Proaktivitas**: Mengambil inisiatif berdasarkan tujuan dan konteks
- **Kemampuan Sosial**: Berinteraksi melalui bahasa alami dengan thread percakapan

### Komponen Teknis
- **AIAgent**: Orkestrasi agen inti dan manajemen percakapan (.NET)
- **Fungsi Alat**: Memperluas kemampuan agen dengan metode dan atribut C#
- **Integrasi OpenAI**: Memanfaatkan model bahasa melalui API .NET yang terstandarisasi
- **Manajemen Lingkungan**: Penanganan konfigurasi dan kredensial yang aman dengan DotNetEnv

## ⚙️ Prasyarat & Pengaturan

**Dependensi yang Dibutuhkan:**
- .NET 9.0 SDK atau lebih tinggi
- Visual Studio 2022 atau VS Code dengan ekstensi C#

**Paket NuGet:**
- `Microsoft.Extensions.AI` - Abstraksi AI inti
- `Microsoft.Extensions.AI.OpenAI` - Integrasi OpenAI (pratinjau)
- `DotNetEnv` - Manajemen variabel lingkungan

**Konfigurasi Lingkungan (file .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Tumpukan Teknis

**Teknologi Inti:**
- Microsoft Agent Framework (.NET)
- Integrasi API Model GitHub
- Pola klien kompatibel OpenAI
- Konfigurasi berbasis lingkungan dengan DotNetEnv

**Kemampuan Agen:**
- Pemahaman dan generasi bahasa alami
- Pemanggilan fungsi dan penggunaan alat dengan atribut C#
- Respons yang sadar konteks dengan thread percakapan
- Arsitektur yang dapat diperluas dengan pola injeksi dependensi

## 📚 Perbandingan Kerangka

Contoh ini menunjukkan pendekatan Microsoft Agent Framework di .NET dibandingkan dengan platform lain:

| Fitur | Kerangka Agen .NET | Padanan Python |
|-------|---------------------|----------------|
| **Keamanan Tipe** | Pengetikan kuat dengan C# | Pengetikan dinamis |
| **Integrasi** | Ekosistem .NET asli | Kompatibilitas bervariasi |
| **Performa** | Performa kode terkompilasi | Eksekusi terinterpretasi |
| **Siap untuk Perusahaan** | Dibangun untuk aplikasi produksi .NET | Bervariasi berdasarkan kerangka |
| **Alat** | Integrasi Visual Studio | Bergantung pada IDE |

## 🚀 Memulai

Ikuti langkah-langkah di bawah ini untuk membangun agen dasar pertama Anda di .NET dan memahami konsep agentic yang mendasar!

## 📦 Instalasi dan Pengaturan

Contoh ini tersedia sebagai Aplikasi File Tunggal .NET yang dapat dijalankan. Lihat file `02-dotnet-agent-framework.cs` yang menyertai untuk implementasi lengkapnya.

Untuk menjalankan contoh ini:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Atau menggunakan CLI dotnet:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Penjelasan Kode

Implementasi lengkap mencakup:

### 1. Dependensi Paket

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

### 2. Impor Esensial

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Konfigurasi Lingkungan

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

### 5. Pengaturan Konfigurasi dan Klien

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

### 8. Manajemen Percakapan

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Poin Penting

1. **Arsitektur Agen**: Microsoft Agent Framework menyediakan pendekatan yang bersih dan aman tipe untuk membangun agen AI di .NET
2. **Integrasi Alat**: Fungsi yang dihiasi dengan atribut `[Description]` menjadi alat yang tersedia untuk agen
3. **Konteks Percakapan**: Manajemen thread memungkinkan percakapan multi-putaran dengan kesadaran konteks penuh
4. **Manajemen Konfigurasi**: Variabel lingkungan dan penanganan kredensial yang aman mengikuti praktik terbaik .NET
5. **Kompatibilitas OpenAI**: Integrasi Model GitHub bekerja dengan mulus melalui API yang kompatibel dengan OpenAI

## 🔗 Sumber Daya Tambahan

- [Dokumentasi Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Marketplace Model GitHub](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [Aplikasi File Tunggal .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.