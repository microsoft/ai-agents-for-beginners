# 🤝 Kurumsal Çoklu Ajan İş Akışı Sistemleri (.NET)

## 📋 Öğrenme Hedefleri

Bu defter, Azure OpenAI (Yanıtlar API) ile .NET'te Microsoft Ajan Çerçevesi kullanarak gelişmiş kurumsal seviyede çoklu ajan sistemleri oluşturmayı gösterir. Yapılandırılmış iş akışları aracılığıyla birlikte çalışan birden fazla uzmanlaşmış ajanı düzenlemeyi, üretime hazır çözümler için .NET'in kurumsal özelliklerinden yararlanmayı öğreneceksiniz.

**Oluşturacağınız Kurumsal Çoklu Ajan Yetkinlikleri:**
- 👥 **Ajan İşbirliği**: Derleme zamanında doğrulama ile tür güvenli ajan koordinasyonu
- 🔄 **İş Akışı Düzenleme**: .NET’in asenkron modelleri ile bildirisel iş akışı tanımı
- 🎭 **Rol Uzmanlaşması**: Güçlü yazımlı ajan kişilikleri ve uzmanlık alanları
- 🏢 **Kurumsal Entegrasyon**: İzleme ve hata yönetimi ile üretime hazır desenler

## ⚙️ Ön Koşullar ve Kurulum

**Geliştirme Ortamı:**
- .NET 9.0 SDK veya üzeri
- Visual Studio 2022 veya C# eklentili VS Code
- Azure aboneliği (kalıcı ajanlar için)

**Gerekli NuGet Paketleri:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Kod Örneği

Bu dersin tam çalışan kodu, beraberindeki C# dosyasında mevcuttur: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Örneği çalıştırmak için:

```bash
# Dosyayı çalıştırılabilir yap (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Örneği çalıştır
./08-dotnet-agent-framework.cs
```

Ya da .NET CLI kullanarak:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Bu Örnek Neyi Gösteriyor

Bu çoklu ajan iş akışı sistemi, iki uzmanlaşmış ajanla otel seyahat öneri servisi oluşturur:

1. **FrontDesk Ajanı**: Aktivite ve lokasyon önerileri veren bir seyahat danışmanı
2. **Concierge Ajanı**: Önerileri gerçek, turistik olmayan deneyimler sağlamak için gözden geçirir

Ajanlar şu şekilde bir iş akışında birlikte çalışır:
- FrontDesk ajanı ilk seyahat talebini alır
- Concierge ajanı öneriyi inceler ve geliştirir
- İş akışı yanıtları gerçek zamanlı olarak akıtır

## Temel Kavramlar

### Ajan Koordinasyonu
Örnek, Microsoft Ajan Çerçevesi kullanarak derleme zamanında doğrulama ile tür güvenli ajan koordinasyonunu gösterir.

### İş Akışı Düzenleme
Birden fazla ajanı bir boru hattında bağlamak için .NET’in asenkron modelleriyle bildirisel iş akışı tanımı kullanır.

### Akış Yanıtları
Asenkron koleksiyonlar ve olay güdümlü mimari kullanarak ajan yanıtlarının gerçek zamanlı akışını uygular.

### Kurumsal Entegrasyon
Aşağıdaki üretime hazır desenleri gösterir:
- Ortam değişkeni yapılandırması
- Güvenli kimlik bilgisi yönetimi
- Hata yönetimi
- Asenkron olay işleme

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->