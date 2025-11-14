<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:24:42+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "tr"
}
-->
# 🛠️ GitHub Modelleri ile Gelişmiş Araç Kullanımı (.NET)

## 📋 Öğrenme Hedefleri

Bu not defteri, Microsoft Agent Framework'ü .NET ile GitHub Modelleri kullanarak kurumsal düzeyde araç entegrasyon desenlerini göstermektedir. C#'ın güçlü tip kontrolü ve .NET'in kurumsal özelliklerinden yararlanarak birden fazla özel araca sahip gelişmiş ajanlar oluşturmayı öğreneceksiniz.

**Ustalaşacağınız Gelişmiş Araç Yetkinlikleri:**
- 🔧 **Çoklu Araç Mimarisi**: Birden fazla özel yeteneğe sahip ajanlar oluşturma
- 🎯 **Tip Güvenli Araç Çalıştırma**: C#'ın derleme zamanı doğrulamasından yararlanma
- 📊 **Kurumsal Araç Desenleri**: Üretime hazır araç tasarımı ve hata yönetimi
- 🔗 **Araç Bileşimi**: Karmaşık iş akışları için araçları birleştirme

## 🎯 .NET Araç Mimarisi Avantajları

### Kurumsal Araç Özellikleri
- **Derleme Zamanı Doğrulama**: Güçlü tip kontrolü, araç parametrelerinin doğruluğunu sağlar
- **Bağımlılık Enjeksiyonu**: IoC konteyner entegrasyonu ile araç yönetimi
- **Async/Await Desenleri**: Kaynak yönetimi ile engellemeyen araç çalıştırma
- **Yapılandırılmış Günlükleme**: Araç çalıştırma izleme için yerleşik günlükleme entegrasyonu

### Üretime Hazır Desenler
- **Hata Yönetimi**: Tiplenmiş istisnalarla kapsamlı hata yönetimi
- **Kaynak Yönetimi**: Doğru imha desenleri ve bellek yönetimi
- **Performans İzleme**: Yerleşik metrikler ve performans sayaçları
- **Yapılandırma Yönetimi**: Doğrulama ile tip güvenli yapılandırma

## 🔧 Teknik Mimari

### Temel .NET Araç Bileşenleri
- **Microsoft.Extensions.AI**: Birleşik araç soyutlama katmanı
- **Microsoft.Agents.AI**: Kurumsal düzeyde araç orkestrasyonu
- **GitHub Modelleri Entegrasyonu**: Bağlantı havuzlaması ile yüksek performanslı API istemcisi

### Araç Çalıştırma Boru Hattı
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Araç Kategorileri ve Desenler

### 1. **Veri İşleme Araçları**
- **Girdi Doğrulama**: Veri açıklamaları ile güçlü tip kontrolü
- **Dönüşüm İşlemleri**: Tip güvenli veri dönüştürme ve biçimlendirme
- **İş Mantığı**: Alan spesifik hesaplama ve analiz araçları
- **Çıktı Biçimlendirme**: Yapılandırılmış yanıt oluşturma

### 2. **Entegrasyon Araçları**
- **API Bağlayıcıları**: HttpClient ile RESTful servis entegrasyonu
- **Veritabanı Araçları**: Veri erişimi için Entity Framework entegrasyonu
- **Dosya İşlemleri**: Doğrulama ile güvenli dosya sistemi işlemleri
- **Harici Servisler**: Üçüncü taraf servis entegrasyon desenleri

### 3. **Yardımcı Araçlar**
- **Metin İşleme**: Dize manipülasyonu ve biçimlendirme araçları
- **Tarih/Saat İşlemleri**: Kültür duyarlı tarih/saat hesaplamaları
- **Matematiksel Araçlar**: Hassas hesaplamalar ve istatistiksel işlemler
- **Doğrulama Araçları**: İş kurallarının doğrulanması ve veri doğrulama

## ⚙️ Ön Koşullar ve Kurulum

**Geliştirme Ortamı:**
- .NET 9.0 SDK veya üstü
- Visual Studio 2022 veya C# eklentisi ile VS Code
- GitHub Modelleri API erişimi

**Gerekli NuGet Paketleri:**
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

.NET'te güçlü, tip güvenli araç yetenekleriyle kurumsal düzeyde ajanlar oluşturmaya hazır mısınız? Hadi profesyonel çözümler tasarlayalım! 🏢⚡

## 💻 Kod Uygulaması

Tam C# uygulaması, `04-dotnet-agent-framework.cs` adlı eşlik eden dosyada mevcuttur. Bu .NET Tek Dosya Uygulaması şunları göstermektedir:

- GitHub Modelleri yapılandırması için ortam değişkenlerini yükleme
- C# yöntemlerini ve özniteliklerini kullanarak özel araçlar tanımlama
- Araç entegrasyonu ile bir AI ajanı oluşturma
- Konuşma dizilerini yönetme
- Araç çağrımı ile ajan isteklerini çalıştırma

Örneği çalıştırmak için:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Ya da .NET CLI kullanarak:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.