<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:35:33+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "tr"
}
-->
# 🔍 Agentik Çerçeveleri Keşfetmek - Temel Agent (.NET)

## 📋 Öğrenme Hedefleri

Bu not defteri, Microsoft Agent Framework'ün temel kavramlarını .NET'te bir temel agent uygulaması üzerinden inceliyor. C# ve .NET ekosistemini kullanarak akıllı ajanların nasıl çalıştığını ve temel agentik desenleri öğreneceksiniz.

**Keşfedecekleriniz:**
- 🏗️ **Agent Mimarisi**: .NET'teki yapay zeka ajanlarının temel yapısını anlama
- 🛠️ **Araç Entegrasyonu**: Ajanların yeteneklerini genişletmek için harici fonksiyonları nasıl kullandığı  
- 💬 **Konuşma Akışı**: Çoklu dönüşlü konuşmaları ve bağlamı iş parçacığı yönetimi ile nasıl yöneteceğiniz
- 🔧 **Yapılandırma Desenleri**: .NET'te ajan kurulum ve yönetimi için en iyi uygulamalar

## 🎯 Kapsanan Temel Kavramlar

### Agentik Çerçeve İlkeleri
- **Otonomi**: Ajanların .NET yapay zeka soyutlamalarını kullanarak bağımsız kararlar alması
- **Reaktivite**: Çevresel değişikliklere ve kullanıcı girdilerine yanıt verme
- **Proaktivite**: Hedefler ve bağlam temelinde inisiyatif alma
- **Sosyal Yetenek**: Konuşma iş parçacıkları aracılığıyla doğal dilde etkileşim kurma

### Teknik Bileşenler
- **AIAgent**: Temel ajan orkestrasyonu ve konuşma yönetimi (.NET)
- **Araç Fonksiyonları**: C# yöntemleri ve öznitelikleri ile ajan yeteneklerini genişletme
- **OpenAI Entegrasyonu**: Standartlaştırılmış .NET API'leri aracılığıyla dil modellerinden yararlanma
- **Çevre Yönetimi**: DotNetEnv ile güvenli yapılandırma ve kimlik bilgisi yönetimi

## ⚙️ Ön Koşullar ve Kurulum

**Gerekli Bağımlılıklar:**
- .NET 9.0 SDK veya üstü
- Visual Studio 2022 veya C# uzantılı VS Code

**NuGet Paketleri:**
- `Microsoft.Extensions.AI` - Temel yapay zeka soyutlamaları
- `Microsoft.Extensions.AI.OpenAI` - OpenAI entegrasyonu (önizleme)
- `DotNetEnv` - Çevre değişkeni yönetimi

**Çevre Yapılandırması (.env dosyası):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Teknik Yığın

**Temel Teknolojiler:**
- Microsoft Agent Framework (.NET)
- GitHub Modelleri API entegrasyonu
- OpenAI uyumlu istemci desenleri
- DotNetEnv ile çevreye dayalı yapılandırma

**Ajan Yetenekleri:**
- Doğal dil anlama ve üretimi
- C# öznitelikleri ile fonksiyon çağırma ve araç kullanımı
- Konuşma iş parçacıkları ile bağlama duyarlı yanıtlar
- Bağımlılık enjeksiyon desenleri ile genişletilebilir mimari

## 📚 Çerçeve Karşılaştırması

Bu örnek, Microsoft Agent Framework'ün .NET'teki yaklaşımını diğer platformlarla karşılaştırır:

| Özellik | .NET Agent Framework | Python Eşdeğerleri |
|---------|---------------------|-------------------|
| **Tip Güvenliği** | C# ile güçlü tipleme | Dinamik tipleme |
| **Entegrasyon** | Yerel .NET ekosistemi | Çeşitli uyumluluk |
| **Performans** | Derlenmiş kod performansı | Yorumlanmış yürütme |
| **Kurumsal Hazır** | Üretim için tasarlanmış .NET uygulamaları | Çerçeveye göre değişir |
| **Araçlar** | Visual Studio entegrasyonu | IDE'ye bağlı |

## 🚀 Başlarken

Aşağıdaki hücreleri takip ederek .NET'te ilk temel agentinizi oluşturun ve temel agentik kavramları anlayın!

## 📦 Kurulum ve Ayar

Bu örnek, çalıştırılabilir bir .NET Tek Dosya Uygulaması olarak mevcuttur. Tam uygulama için eşlik eden `02-dotnet-agent-framework.cs` dosyasına bakın.

Bu örneği çalıştırmak için:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Veya dotnet CLI kullanarak:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Kod İncelemesi

Tam uygulama şunları içerir:

### 1. Paket Bağımlılıkları

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

### 2. Temel İçe Aktarmalar

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Çevre Yapılandırması

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Araç Fonksiyon Tanımı

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

### 5. Yapılandırma ve İstemci Ayarı

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

### 6. Ajan Yapılandırması

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

### 7. Ajan Başlatma

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

### 8. Konuşma Yönetimi

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Temel Çıkarımlar

1. **Ajan Mimarisi**: Microsoft Agent Framework, .NET'te yapay zeka ajanları oluşturmak için temiz, tip güvenli bir yaklaşım sunar
2. **Araç Entegrasyonu**: `[Description]` öznitelikleriyle süslenmiş fonksiyonlar, ajan için kullanılabilir araçlar haline gelir
3. **Konuşma Bağlamı**: İş parçacığı yönetimi, tam bağlam farkındalığı ile çoklu dönüşlü konuşmaları mümkün kılar
4. **Yapılandırma Yönetimi**: Çevre değişkenleri ve güvenli kimlik bilgisi yönetimi .NET en iyi uygulamalarını takip eder
5. **OpenAI Uyumluluğu**: GitHub Modelleri entegrasyonu, OpenAI uyumlu API'ler aracılığıyla sorunsuz çalışır

## 🔗 Ek Kaynaklar

- [Microsoft Agent Framework Belgeleri](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Modelleri Pazarı](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Tek Dosya Uygulamaları](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.