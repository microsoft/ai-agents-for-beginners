<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:16:11+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "tr"
}
-->
# 🤝 Kurumsal Çoklu-Ajan İş Akışı Sistemleri (.NET)

## 📋 Öğrenme Hedefleri

Bu not defteri, Microsoft Agent Framework'ü kullanarak .NET ile GitHub Modelleri üzerinden gelişmiş kurumsal düzeyde çoklu-ajan sistemleri oluşturmayı gösterir. Birden fazla uzmanlaşmış ajanın yapılandırılmış iş akışları aracılığıyla birlikte çalışmasını düzenlemeyi öğrenecek ve .NET'in kurumsal özelliklerini üretime hazır çözümler için kullanacaksınız.

**Oluşturacağınız Kurumsal Çoklu-Ajan Özellikleri:**
- 👥 **Ajan İşbirliği**: Derleme zamanında doğrulama ile tür güvenli ajan koordinasyonu
- 🔄 **İş Akışı Düzenleme**: .NET'in async desenleriyle deklaratif iş akışı tanımı
- 🎭 **Rol Uzmanlaşması**: Güçlü türde ajan kişilikleri ve uzmanlık alanları
- 🏢 **Kurumsal Entegrasyon**: İzleme ve hata yönetimi ile üretime hazır desenler

## ⚙️ Ön Koşullar ve Kurulum

**Geliştirme Ortamı:**
- .NET 9.0 SDK veya üstü
- Visual Studio 2022 veya C# uzantılı VS Code
- Azure aboneliği (kalıcı ajanlar için)

**Gerekli NuGet Paketleri:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Kod Örneği

Bu ders için tam çalışan kod, eşlik eden C# dosyasında mevcuttur: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Örneği çalıştırmak için:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Ya da .NET CLI kullanarak:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Bu Örnek Ne Gösteriyor?

Bu çoklu-ajan iş akışı sistemi, iki uzmanlaşmış ajan ile bir otel seyahat öneri hizmeti oluşturur:

1. **FrontDesk Agent**: Aktivite ve konum önerileri sağlayan bir seyahat ajanı
2. **Concierge Agent**: Önerileri gözden geçirerek otantik, turistik olmayan deneyimler sağlar

Ajanlar şu şekilde bir iş akışında birlikte çalışır:
- FrontDesk ajanı ilk seyahat talebini alır
- Concierge ajanı öneriyi gözden geçirir ve geliştirir
- İş akışı yanıtları gerçek zamanlı olarak yayınlar

## Temel Kavramlar

### Ajan Koordinasyonu
Örnek, Microsoft Agent Framework kullanarak tür güvenli ajan koordinasyonunu derleme zamanında doğrulama ile gösterir.

### İş Akışı Düzenleme
Birden fazla ajanı bir boru hattında bağlamak için .NET'in async desenleriyle deklaratif iş akışı tanımı kullanır.

### Akış Yanıtları
Async enumerables ve olay odaklı mimari kullanarak ajan yanıtlarının gerçek zamanlı akışını uygular.

### Kurumsal Entegrasyon
Üretime hazır desenleri gösterir, bunlar arasında:
- Ortam değişkeni yapılandırması
- Güvenli kimlik bilgisi yönetimi
- Hata yönetimi
- Asenkron olay işleme

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.