<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:47:13+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "tr"
}
-->
# 🎨 GitHub Modelleri ile Etkili Tasarım Kalıpları (.NET)

## 📋 Öğrenme Hedefleri

Bu not defteri, Microsoft Agent Framework'ü kullanarak GitHub Modelleri entegrasyonu ile akıllı ajanlar oluşturmak için kurumsal düzeyde tasarım kalıplarını gösterir. Üretime hazır, sürdürülebilir ve ölçeklenebilir ajanlar oluşturmayı sağlayan profesyonel kalıpları ve mimari yaklaşımları öğreneceksiniz.

**Kurumsal Tasarım Kalıpları:**
- 🏭 **Factory Pattern**: Bağımlılık enjeksiyonu ile standartlaştırılmış ajan oluşturma
- 🔧 **Builder Pattern**: Akıcı ajan yapılandırma ve kurulum
- 🧵 **Thread-Safe Patterns**: Eşzamanlı konuşma yönetimi
- 📋 **Repository Pattern**: Düzenli araç ve yetenek yönetimi

## 🎯 .NET'e Özgü Mimari Avantajlar

### Kurumsal Özellikler
- **Güçlü Tipleme**: Derleme zamanı doğrulama ve IntelliSense desteği
- **Bağımlılık Enjeksiyonu**: Dahili DI konteyner entegrasyonu
- **Yapılandırma Yönetimi**: IConfiguration ve Options kalıpları
- **Async/Await**: Birinci sınıf asenkron programlama desteği

### Üretime Hazır Kalıplar
- **Günlükleme Entegrasyonu**: ILogger ve yapılandırılmış günlükleme desteği
- **Sağlık Kontrolleri**: Dahili izleme ve tanılama
- **Yapılandırma Doğrulama**: Veri açıklamaları ile güçlü tipleme
- **Hata Yönetimi**: Yapılandırılmış istisna yönetimi

## 🔧 Teknik Mimari

### Temel .NET Bileşenleri
- **Microsoft.Extensions.AI**: Birleşik AI hizmet soyutlamaları
- **Microsoft.Agents.AI**: Kurumsal ajan orkestrasyon çerçevesi
- **GitHub Modelleri Entegrasyonu**: Yüksek performanslı API istemci kalıpları
- **Yapılandırma Sistemi**: appsettings.json ve ortam entegrasyonu

### Tasarım Kalıbı Uygulaması
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Gösterilen Kurumsal Kalıplar

### 1. **Oluşturma Kalıpları**
- **Agent Factory**: Tutarlı yapılandırma ile merkezi ajan oluşturma
- **Builder Pattern**: Karmaşık ajan yapılandırması için akıcı API
- **Singleton Pattern**: Paylaşılan kaynaklar ve yapılandırma yönetimi
- **Bağımlılık Enjeksiyonu**: Gevşek bağlama ve test edilebilirlik

### 2. **Davranışsal Kalıplar**
- **Strategy Pattern**: Değiştirilebilir araç yürütme stratejileri
- **Command Pattern**: Geri alma/yeniden yapma ile kapsüllenmiş ajan işlemleri
- **Observer Pattern**: Olay odaklı ajan yaşam döngüsü yönetimi
- **Template Method**: Standartlaştırılmış ajan yürütme iş akışları

### 3. **Yapısal Kalıplar**
- **Adapter Pattern**: GitHub Modelleri API entegrasyon katmanı
- **Decorator Pattern**: Ajan yeteneklerini geliştirme
- **Facade Pattern**: Basitleştirilmiş ajan etkileşim arayüzleri
- **Proxy Pattern**: Performans için tembel yükleme ve önbellekleme

## ⚙️ Ön Koşullar ve Kurulum

**Geliştirme Ortamı:**
- .NET 9.0 SDK veya üstü
- Visual Studio 2022 veya C# uzantılı VS Code
- GitHub Modelleri API erişimi

**NuGet Bağımlılıkları:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Yapılandırma (.env dosyası):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 .NET Tasarım İlkeleri

### SOLID İlkeleri
- **Tek Sorumluluk**: Her bileşenin net bir amacı var
- **Açık/Kapalı**: Değiştirilmeden genişletilebilir
- **Liskov Substitution**: Arayüz tabanlı araç uygulamaları
- **Arayüz Ayrımı**: Odaklanmış, uyumlu arayüzler
- **Bağımlılık Tersine Çevirme**: Somutlamalara değil soyutlamalara bağlılık

### Temiz Mimari
- **Domain Katmanı**: Temel ajan ve araç soyutlamaları
- **Uygulama Katmanı**: Ajan orkestrasyonu ve iş akışları
- **Altyapı Katmanı**: GitHub Modelleri entegrasyonu ve harici hizmetler
- **Sunum Katmanı**: Kullanıcı etkileşimi ve yanıt biçimlendirme

## 🔒 Kurumsal Hususlar

### Güvenlik
- **Kimlik Bilgisi Yönetimi**: IConfiguration ile güvenli API anahtarı yönetimi
- **Girdi Doğrulama**: Güçlü tipleme ve veri açıklama doğrulaması
- **Çıktı Temizleme**: Güvenli yanıt işleme ve filtreleme
- **Denetim Günlükleme**: Kapsamlı işlem takibi

### Performans
- **Asenkron Kalıplar**: Bloklama olmayan I/O işlemleri
- **Bağlantı Havuzu**: Verimli HTTP istemci yönetimi
- **Önbellekleme**: Performansı artırmak için yanıt önbellekleme
- **Kaynak Yönetimi**: Uygun kaynak temizleme ve bertaraf kalıpları

### Ölçeklenebilirlik
- **Thread Safety**: Eşzamanlı ajan yürütme desteği
- **Kaynak Havuzu**: Verimli kaynak kullanımı
- **Yük Yönetimi**: Hız sınırlama ve geri basınç yönetimi
- **İzleme**: Performans metrikleri ve sağlık kontrolleri

## 🚀 Üretim Dağıtımı

- **Yapılandırma Yönetimi**: Ortama özgü ayarlar
- **Günlükleme Stratejisi**: Korelasyon kimlikleri ile yapılandırılmış günlükleme
- **Hata Yönetimi**: Uygun kurtarma ile genel istisna yönetimi
- **İzleme**: Uygulama içgörüleri ve performans sayaçları
- **Test**: Birim testleri, entegrasyon testleri ve yük test kalıpları

.NET ile kurumsal düzeyde akıllı ajanlar oluşturmaya hazır mısınız? Hadi sağlam bir şeyler tasarlayalım! 🏢✨

## Kod Örneği

Tam çalışan bir örnek için [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) dosyasına bakın.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.