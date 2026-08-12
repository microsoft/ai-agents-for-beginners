# 🎯 Azure OpenAI ile Planlama ve Tasarım Kalıpları (Responses API) (.NET)

## 📋 Öğrenme Hedefleri

Bu not defteri, Azure OpenAI (Responses API) ile .NET'te Microsoft Agent Framework kullanarak zeki ajanlar oluşturmak için kurumsal düzeyde planlama ve tasarım kalıplarını göstermektedir. Karmaşık problemleri parçalayabilen, çok adımlı çözümler planlayabilen ve .NET'in kurumsal özellikleriyle gelişmiş iş akışlarını yürütebilen ajanlar oluşturmayı öğreneceksiniz.

## ⚙️ Ön Koşullar ve Kurulum

**Geliştirme Ortamı:**
- .NET 9.0 SDK veya üzeri
- Visual Studio 2022 veya C# eklentili VS Code
- Azure OpenAI kaynağı ve model dağıtımı olan bir Azure aboneliği
- Azure CLI — `az login` ile oturum açın

**Gerekli Bağımlılıklar:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Ortam Yapılandırması (.env dosyası):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Kodu Çalıştırma

Bu ders, .NET Tek Dosya Uygulaması uygulaması içerir. Çalıştırmak için:

```bash
# Dosyayı çalıştırılabilir yap (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Uygulamayı çalıştır
./07-dotnet-agent-framework.cs
```

Ya da dotnet run komutunu kullanın:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Kod Uygulaması

Tam uygulama `07-dotnet-agent-framework.cs` dosyasında mevcuttur. Bu dosya şunları gösterir:

- DotNetEnv ile ortam yapılandırmasının yüklenmesi
- `GetChatClient().AsAIAgent()` kullanarak Azure OpenAI istemcisinin yapılandırılması ve bir yapay zeka ajanı oluşturulması
- JSON serileştirmesi ile yapılandırılmış veri modellerinin (Plan ve TravelPlan) tanımlanması
- JSON şeması kullanarak yapılandırılmış çıktı sağlayan bir yapay zeka ajanı oluşturulması
- Tip güvenli yanıtlarla planlama isteklerinin gerçekleştirilmesi

## Temel Kavramlar

### Tip Güvenli Modellerle Yapılandırılmış Planlama

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

### Yapılandırılmış Çıktılar İçin JSON Şeması

Ajan, TravelPlan şemasına uygun yanıtlar dönecek şekilde yapılandırılmıştır:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
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

Ajan, görevleri uzman alt ajanlara devreden bir koordinatör olarak görev yapar:

- FlightBooking: Uçuş rezervasyonları yapmak ve uçuş bilgileri sağlamak için
- HotelBooking: Otel rezervasyonları yapmak ve otel bilgileri sağlamak için
- CarRental: Araç kiralama işlemleri yapmak ve araç kiralama bilgileri sağlamak için
- ActivitiesBooking: Aktivite rezervasyonları yapmak ve aktivite bilgileri sağlamak için
- DestinationInfo: Varış noktaları hakkında bilgi sağlamak için
- DefaultAgent: Genel istekleri yönetmek için

## Beklenen Çıktı

Seyahat planlama isteğiyle ajan çalıştırıldığında, istek analiz edilir ve uzman ajanlara uygun görev atamaları yapılmış yapılandırılmış bir plan oluşturulur. Çıktı, TravelPlan şemasına uygun JSON formatındadır.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->