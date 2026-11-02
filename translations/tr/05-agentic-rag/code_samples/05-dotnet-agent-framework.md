# 🔍 Microsoft Foundry (.NET) ile Kurumsal RAG

## 📋 Öğrenme Hedefleri

Bu not defteri, Microsoft Foundry ile .NET'te Microsoft Agent Framework kullanarak kurumsal düzeyde Retrieval-Augmented Generation (RAG) sistemlerinin nasıl oluşturulacağını göstermektedir. Üretim hazır ajanlar oluşturmayı öğreneceksiniz; bu ajanlar belgelerde arama yapabilir ve kurumsal güvenlik ve ölçeklenebilirlikle doğru, bağlama duyarlı yanıtlar sağlayabilir.

**Oluşturacağınız Kurumsal RAG Özellikleri:**
- 📚 **Belge Zekası**: Azure AI servisleriyle gelişmiş belge işleme
- 🔍 **Anlamsal Arama**: Kurumsal özelliklerle yüksek performanslı vektör araması
- 🛡️ **Güvenlik Entegrasyonu**: Rol tabanlı erişim ve veri koruma desenleri
- 🏢 **Ölçeklenebilir Mimari**: İzlemeli üretim hazır RAG sistemleri

## 🎯 Kurumsal RAG Mimarisi

### Temel Kurumsal Bileşenler
- **Microsoft Foundry**: Güvenlik ve uyumluluk ile yönetilen kurumsal AI platformu
- **Kalıcı Ajanlar**: Konuşma geçmişi ve bağlam yönetimine sahip durumlu ajanlar
- **Vektör Deposu Yönetimi**: Kurumsal düzeyde belge indeksleme ve erişim
- **Kimlik Entegrasyonu**: Azure AD kimlik doğrulaması ve rol tabanlı erişim kontrolü

### .NET Kurumsal Avantajları
- **Tip Güvenliği**: RAG işlemleri ve veri yapıları için derleme zamanı doğrulaması
- **Async Performans**: Engellemeyen belge işleme ve arama işlemleri
- **Bellek Yönetimi**: Büyük belge koleksiyonları için verimli kaynak kullanımı
- **Entegrasyon Desenleri**: Bağımlılık enjeksiyonlu yerel Azure servis entegrasyonu

## 🏗️ Teknik Mimari

### Kurumsal RAG İş Akışı
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Temel .NET Bileşenleri
- **Azure.AI.Agents.Persistent**: Durum kalıcılığıyla kurumsal ajan yönetimi
- **Azure.Identity**: Güvenli Azure servis erişimi için entegre kimlik doğrulama
- **Microsoft.Agents.AI.AzureAI**: Azure'a optimize edilmiş ajan çerçevesi uygulaması
- **System.Linq.Async**: Yüksek performanslı asenkron LINQ işlemleri

## 🔧 Kurumsal Özellikler & Avantajlar

### Güvenlik & Uyumluluk
- **Azure AD Entegrasyonu**: Kurumsal kimlik yönetimi ve kimlik doğrulama
- **Rol Tabanlı Erişim**: Belge erişimi ve işlemler için ince detaylı izinler
- **Veri Koruma**: Hassas belgeler için dinamik ve beklemede şifreleme
- **Denetim Kaydı**: Uyumluluk gereksinimleri için kapsamlı etkinlik takibi

### Performans & Ölçeklenebilirlik
- **Bağlantı Havuzu**: Verimli Azure servis bağlantısı yönetimi
- **Asenkron İşleme**: Yüksek verimli senaryolar için engellemeyen işlemler
- **Önbellekleme Stratejileri**: Sık erişilen belgeler için akıllı önbellekleme
- **Yük Dengeleme**: Büyük ölçekli dağıtımlar için dağıtık işlem

### Yönetim & İzleme
- **Sağlık Kontrolleri**: RAG sistem bileşenleri için yerleşik izleme
- **Performans Ölçümleri**: Arama kalitesi ve yanıt sürelerine detaylı analizler
- **Hata Yönetimi**: Tekrar deneme politikaları ile kapsamlı istisna yönetimi
- **Konfigürasyon Yönetimi**: Doğrulamalı ortam bazlı ayarlar

## ⚙️ Ön Gereksinimler & Kurulum

**Geliştirme Ortamı:**
- .NET 9.0 SDK veya üzeri
- Visual Studio 2022 veya C# uzantılı VS Code
- Microsoft Foundry erişimi olan Azure aboneliği

**Gerekli NuGet Paketleri:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure Kimlik Doğrulaması Kurulumu:**
```bash
# Azure CLI'yi yükleyin ve kimlik doğrulaması yapın
az login
az account set --subscription "your-subscription-id"
```

**Ortam Konfigürasyonu:**
* Microsoft Foundry yapılandırması (Azure CLI ile otomatik yönetilir)
* Doğru Azure aboneliğine kimlik doğruladığınızdan emin olun

## 📊 Kurumsal RAG Desenleri

### Belge Yönetimi Desenleri
- **Toplu Yükleme**: Büyük belge koleksiyonlarının verimli işlenmesi
- **Artımlı Güncellemeler**: Gerçek zamanlı belge ekleme ve değişiklikler
- **Sürüm Kontrolü**: Belge sürümlendirme ve değişim takibi
- **Meta Veri Yönetimi**: Zengin belge özellikleri ve taksonomi

### Arama & Erişim Desenleri
- **Hibrit Arama**: Optimal sonuçlar için anlamsal ve anahtar kelime aramasının birleşimi
- **Faceted Arama**: Çok boyutlu filtreleme ve kategorilendirme
- **Alaka Ayarı**: Alan bazlı özel puanlama algoritmaları
- **Sonuç Sıralama**: İş mantığı entegrasyonlu gelişmiş sıralama

### Güvenlik Desenleri
- **Belge Düzeyi Güvenlik**: Belge başına ince ayrıntılı erişim kontrolü
- **Veri Sınıflandırması**: Otomatik hassasiyet etiketleme ve koruma
- **Denetim İzleri**: Tüm RAG işlemlerinin kapsamlı kaydı
- **Gizlilik Koruması**: Kişisel kimlik bilgisi tespiti ve sansürleme yetenekleri

## 🔒 Kurumsal Güvenlik Özellikleri

### Kimlik Doğrulama & Yetkilendirme
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Veri Koruma
- **Şifreleme**: Belgeler ve arama indeksleri için uçtan uca şifreleme
- **Erişim Kontrolleri**: Kullanıcı ve grup izinleri için Azure AD entegrasyonu
- **Veri Yerleşimi**: Uyumluluk için coğrafi veri konumu kontrolleri
- **Yedekleme & Kurtarma**: Otomatik yedekleme ve felaket kurtarma yetenekleri

## 📈 Performans Optimizasyonu

### Asenkron İşleme Desenleri
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Bellek Yönetimi
- **Akış İşleme**: Bellek sorunları olmadan büyük belgelerin işlenmesi
- **Kaynak Havuzu**: Pahalı kaynakların verimli yeniden kullanımı
- **Çöp Toplama**: Optimize edilmiş bellek tahsis desenleri
- **Bağlantı Yönetimi**: Doğru Azure servis bağlantı yaşam döngüsü

### Önbellekleme Stratejileri
- **Sorgu Önbellekleme**: Sık yürütülen aramaları önbelleğe alma
- **Belge Önbellekleme**: "Sıcak" belgeler için bellek içi önbellekleme
- **İndeks Önbellekleme**: Optimize edilmiş vektör indeks önbellekleme
- **Sonuç Önbellekleme**: Üretilen yanıtların akıllı önbelleklemesi

## 📊 Kurumsal Kullanım Senaryoları

### Bilgi Yönetimi
- **Kurumsal Wiki**: Şirket bilgi tabanlarında akıllı arama
- **Politika & Prosedürler**: Otomatik uyumluluk ve prosedür rehberliği
- **Eğitim Materyalleri**: Akıllı öğrenme ve geliştirme desteği
- **Araştırma Veritabanları**: Akademik ve araştırma makalesi analiz sistemleri

### Müşteri Desteği
- **Destek Bilgi Tabanı**: Otomatik müşteri hizmetleri yanıtları
- **Ürün Dokümantasyonu**: Akıllı ürün bilgi alma
- **Sorun Giderme Kılavuzları**: Bağlamsal sorun çözme yardımı
- **SSS Sistemleri**: Belge koleksiyonlarından dinamik SSS oluşturma

### Düzenleyici Uyumluluk
- **Hukuki Belge Analizi**: Sözleşme ve hukuki belge zekası
- **Uyumluluk İzleme**: Otomatik düzenleyici uyumluluk kontrolü
- **Risk Değerlendirmesi**: Belge tabanlı risk analizi ve raporlama
- **Denetim Desteği**: Denetimler için akıllı belge keşfi

## 🚀 Üretim Dağıtımı

### İzleme & Gözlemlenebilirlik
- **Application Insights**: Detaylı telemetri ve performans izleme
- **Özel Ölçümler**: İşe özel KPI izleme ve uyarılar
- **Dağıtık İzleme**: Hizmetler arası uçtan uca istek takibi
- **Sağlık Panelleri**: Gerçek zamanlı sistem sağlık ve performans görselleştirme

### Ölçeklenebilirlik & Güvenilirlik
- **Otomatik Ölçeklendirme**: Yük ve performans metriklerine göre otomatik ölçeklendirme
- **Yüksek Erişilebilirlik**: Hata geçiş özellikli çok bölge dağıtımı
- **Yük Testi**: Kurumsal yük koşullarında performans doğrulaması
- **Felaket Kurtarma**: Otomatik yedekleme ve kurtarma prosedürleri

Hassas belgeleri ölçekle yönetebilen kurumsal sınıf RAG sistemleri oluşturmaya hazır mısınız? Haydi kurumsal için akıllı bilgi sistemleri tasarlayalım! 🏢📖✨

## Kod Uygulaması

Bu ders için tam işleyen kod örneği `05-dotnet-agent-framework.cs` dosyasında mevcuttur. 

Örneği çalıştırmak için:

```bash
# Betiği çalıştırılabilir yap (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# .NET Tek Dosya Uygulamasını çalıştır
./05-dotnet-agent-framework.cs
```

Veya doğrudan `dotnet run` kullanabilirsiniz:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kod şunları göstermektedir:

1. **Paket Kurulumu**: Azure AI Ajanları için gerekli NuGet paketlerini kurma
2. **Ortam Yapılandırması**: Microsoft Foundry uç noktası ve model ayarlarını yükleme
3. **Belge Yükleme**: RAG işleme için belge yükleme
4. **Vektör Deposu Oluşturma**: Anlamsal arama için vektör deposu oluşturma
5. **Ajan Yapılandırması**: Dosya arama yetenekleriyle AI ajanı kurma
6. **Sorgu Çalıştırma**: Yüklenen belgeler üzerinde sorgular çalıştırma

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->