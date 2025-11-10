<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:57:06+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "tr"
}
-->
# 🎯 GitHub Modelleri ile Planlama ve Tasarım Kalıpları (.NET)

## 📋 Öğrenme Hedefleri

Bu not defteri, Microsoft Agent Framework'ü kullanarak GitHub Modelleri ile akıllı ajanlar oluşturmak için kurumsal düzeyde planlama ve tasarım kalıplarını göstermektedir. Karmaşık problemleri parçalayabilen, çok adımlı çözümler planlayabilen ve .NET'in kurumsal özellikleriyle gelişmiş iş akışlarını gerçekleştirebilen ajanlar oluşturmayı öğreneceksiniz.

## ⚙️ Ön Koşullar ve Kurulum

**Geliştirme Ortamı:**
- .NET 9.0 SDK veya üstü
- Visual Studio 2022 veya C# eklentisi ile VS Code
- GitHub Modelleri API erişimi

**Gerekli Bağımlılıklar:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Ortam Yapılandırması (.env dosyası):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Kodun Çalıştırılması

Bu ders, bir .NET Tek Dosya Uygulaması uygulamasını içerir. Çalıştırmak için:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Ya da dotnet run komutunu kullanabilirsiniz:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kod Uygulaması

Tam uygulama `07-dotnet-agent-framework.cs` dosyasında mevcuttur ve şunları göstermektedir:

- DotNetEnv ile ortam yapılandırmasının yüklenmesi
- GitHub Modelleri için OpenAI istemcisinin yapılandırılması
- JSON serileştirme ile yapılandırılmış veri modellerinin (Plan ve TravelPlan) tanımlanması
- JSON şeması kullanarak yapılandırılmış çıktı ile bir AI ajanı oluşturulması
- Tür güvenli yanıtlarla planlama isteklerinin yürütülmesi

## Temel Kavramlar

### Tür Güvenli Modellerle Yapılandırılmış Planlama

Ajan, planlama çıktılarının yapısını tanımlamak için C# sınıflarını kullanır:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### Yapılandırılmış Çıktılar için JSON Şeması

Ajan, TravelPlan şemasına uygun yanıtlar döndürecek şekilde yapılandırılmıştır:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Planlama Ajanı Talimatları

Ajan, görevleri uzman alt ajanlara devreden bir koordinatör olarak hareket eder:

- FlightBooking: Uçuş rezervasyonu yapmak ve uçuş bilgileri sağlamak
- HotelBooking: Otel rezervasyonu yapmak ve otel bilgileri sağlamak
- CarRental: Araç kiralama rezervasyonu yapmak ve araç kiralama bilgileri sağlamak
- ActivitiesBooking: Etkinlik rezervasyonu yapmak ve etkinlik bilgileri sağlamak
- DestinationInfo: Seyahat noktaları hakkında bilgi sağlamak
- DefaultAgent: Genel talepleri ele almak

## Beklenen Çıktı

Ajanı bir seyahat planlama isteğiyle çalıştırdığınızda, isteği analiz eder ve TravelPlan şemasına uygun olarak yapılandırılmış bir plan oluşturur. Bu plan, ilgili görevleri uzman ajanlara uygun şekilde atayarak JSON formatında sunar.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.