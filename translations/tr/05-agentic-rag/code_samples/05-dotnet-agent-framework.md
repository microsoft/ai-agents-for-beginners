<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:02:44+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "tr"
}
-->
# 🔍 Azure AI Foundry ile Kurumsal RAG (.NET)

## 📋 Öğrenme Hedefleri

Bu not defteri, Microsoft Agent Framework'ü .NET ile kullanarak kurumsal düzeyde Geri Alımlı Üretim (RAG) sistemleri oluşturmayı gösterir. Belgeler arasında arama yapabilen ve kurumsal güvenlik ve ölçeklenebilirlik ile doğru, bağlama duyarlı yanıtlar sağlayabilen üretime hazır ajanlar oluşturmayı öğreneceksiniz.

**Oluşturacağınız Kurumsal RAG Özellikleri:**
- 📚 **Belge Zekası**: Azure AI hizmetleri ile gelişmiş belge işleme
- 🔍 **Semantik Arama**: Kurumsal özelliklere sahip yüksek performanslı vektör arama
- 🛡️ **Güvenlik Entegrasyonu**: Rol tabanlı erişim ve veri koruma desenleri
- 🏢 **Ölçeklenebilir Mimari**: İzleme ile üretime hazır RAG sistemleri

## 🎯 Kurumsal RAG Mimarisi

### Temel Kurumsal Bileşenler
- **Azure AI Foundry**: Güvenlik ve uyumluluk ile yönetilen kurumsal AI platformu
- **Kalıcı Ajanlar**: Konuşma geçmişi ve bağlam yönetimi ile durum bilgisi olan ajanlar
- **Vektör Deposu Yönetimi**: Kurumsal düzeyde belge indeksleme ve alma
- **Kimlik Entegrasyonu**: Azure AD kimlik doğrulama ve rol tabanlı erişim kontrolü

### .NET Kurumsal Avantajları
- **Tip Güvenliği**: RAG işlemleri ve veri yapıları için derleme zamanı doğrulama
- **Asenkron Performans**: Bloklama yapmayan belge işleme ve arama işlemleri
- **Bellek Yönetimi**: Büyük belge koleksiyonları için verimli kaynak kullanımı
- **Entegrasyon Desenleri**: Bağımlılık enjeksiyonu ile yerel Azure hizmet entegrasyonu

## 🏗️ Teknik Mimari

### Kurumsal RAG Boru Hattı
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Temel .NET Bileşenleri
- **Azure.AI.Agents.Persistent**: Durum kalıcılığı ile kurumsal ajan yönetimi
- **Azure.Identity**: Güvenli Azure hizmet erişimi için entegre kimlik doğrulama
- **Microsoft.Agents.AI.AzureAI**: Azure'a optimize edilmiş ajan çerçeve uygulaması
- **System.Linq.Async**: Yüksek performanslı asenkron LINQ işlemleri

## 🔧 Kurumsal Özellikler ve Avantajlar

### Güvenlik ve Uyumluluk
- **Azure AD Entegrasyonu**: Kurumsal kimlik yönetimi ve kimlik doğrulama
- **Rol Tabanlı Erişim**: Belge erişimi ve işlemleri için ince ayarlı izinler
- **Veri Koruma**: Hassas belgeler için dinlenme ve aktarım sırasında şifreleme
- **Denetim Günlüğü**: Uyumluluk gereksinimleri için kapsamlı etkinlik takibi

### Performans ve Ölçeklenebilirlik
- **Bağlantı Havuzu**: Verimli Azure hizmet bağlantı yönetimi
- **Asenkron İşleme**: Yüksek verim senaryoları için bloklama yapmayan işlemler
- **Önbellek Stratejileri**: Sık erişilen belgeler için akıllı önbellekleme
- **Yük Dengeleme**: Büyük ölçekli dağıtımlar için dağıtılmış işleme

### Yönetim ve İzleme
- **Sağlık Kontrolleri**: RAG sistem bileşenleri için yerleşik izleme
- **Performans Metrikleri**: Arama kalitesi ve yanıt süreleri hakkında ayrıntılı analiz
- **Hata Yönetimi**: Yeniden deneme politikaları ile kapsamlı istisna yönetimi
- **Yapılandırma Yönetimi**: Doğrulama ile ortam spesifik ayarlar

## ⚙️ Ön Koşullar ve Kurulum

**Geliştirme Ortamı:**
- .NET 9.0 SDK veya üstü
- Visual Studio 2022 veya C# uzantılı VS Code
- Azure AI Foundry erişimi olan Azure aboneliği

**Gerekli NuGet Paketleri:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure Kimlik Doğrulama Ayarı:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Ortam Yapılandırması:**
* Azure AI Foundry yapılandırması (Azure CLI aracılığıyla otomatik olarak işlenir)
* Doğru Azure aboneliğine kimlik doğrulaması yapıldığından emin olun

## 📊 Kurumsal RAG Desenleri

### Belge Yönetimi Desenleri
- **Toplu Yükleme**: Büyük belge koleksiyonlarının verimli işlenmesi
- **Artımlı Güncellemeler**: Gerçek zamanlı belge ekleme ve değiştirme
- **Sürüm Kontrolü**: Belge sürümlendirme ve değişiklik takibi
- **Meta Veri Yönetimi**: Zengin belge öznitelikleri ve taksonomi

### Arama ve Alma Desenleri
- **Hibrit Arama**: Optimal sonuçlar için semantik ve anahtar kelime aramasını birleştirme
- **Fasetsel Arama**: Çok boyutlu filtreleme ve kategorilendirme
- **Alaka Ayarı**: Alan spesifik ihtiyaçlar için özel puanlama algoritmaları
- **Sonuç Sıralama**: İş mantığı entegrasyonu ile gelişmiş sıralama

### Güvenlik Desenleri
- **Belge Düzeyinde Güvenlik**: Her belge için ince ayarlı erişim kontrolü
- **Veri Sınıflandırması**: Otomatik hassasiyet etiketleme ve koruma
- **Denetim İzleri**: Tüm RAG işlemlerinin kapsamlı günlüğü
- **Gizlilik Koruması**: Kişisel Bilgi Tespiti ve sansürleme yetenekleri

## 🔒 Kurumsal Güvenlik Özellikleri

### Kimlik Doğrulama ve Yetkilendirme
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
- **Yedekleme ve Kurtarma**: Otomatik yedekleme ve felaket kurtarma yetenekleri

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
- **Akış İşleme**: Büyük belgeleri bellek sorunları olmadan işleme
- **Kaynak Havuzu**: Pahalı kaynakların verimli yeniden kullanımı
- **Çöp Toplama**: Optimize edilmiş bellek tahsis desenleri
- **Bağlantı Yönetimi**: Doğru Azure hizmet bağlantı yaşam döngüsü

### Önbellek Stratejileri
- **Sorgu Önbelleği**: Sıkça yapılan aramaları önbelleğe alma
- **Belge Önbelleği**: Sık kullanılan belgeler için bellek içi önbellekleme
- **İndeks Önbelleği**: Optimize edilmiş vektör indeks önbellekleme
- **Sonuç Önbelleği**: Üretilen yanıtların akıllı önbelleklemesi

## 📊 Kurumsal Kullanım Senaryoları

### Bilgi Yönetimi
- **Kurumsal Wiki**: Şirket bilgi tabanlarında akıllı arama
- **Politika ve Prosedürler**: Otomatik uyumluluk ve prosedür rehberliği
- **Eğitim Materyalleri**: Akıllı öğrenme ve geliştirme yardımı
- **Araştırma Veritabanları**: Akademik ve araştırma makalesi analiz sistemleri

### Müşteri Desteği
- **Destek Bilgi Tabanı**: Otomatik müşteri hizmetleri yanıtları
- **Ürün Belgeleri**: Akıllı ürün bilgisi alma
- **Sorun Giderme Kılavuzları**: Bağlama duyarlı problem çözme yardımı
- **SSS Sistemleri**: Belge koleksiyonlarından dinamik SSS oluşturma

### Düzenleyici Uyumluluk
- **Hukuki Belge Analizi**: Sözleşme ve hukuki belge zekası
- **Uyumluluk İzleme**: Otomatik düzenleyici uyumluluk kontrolü
- **Risk Değerlendirme**: Belge tabanlı risk analizi ve raporlama
- **Denetim Desteği**: Denetimler için akıllı belge keşfi

## 🚀 Üretim Dağıtımı

### İzleme ve Görünürlük
- **Application Insights**: Ayrıntılı telemetri ve performans izleme
- **Özel Metrikler**: İşe özel KPI takibi ve uyarılar
- **Dağıtılmış İzleme**: Hizmetler arasında uçtan uca istek takibi
- **Sağlık Panoları**: Gerçek zamanlı sistem sağlığı ve performans görselleştirme

### Ölçeklenebilirlik ve Güvenilirlik
- **Otomatik Ölçeklendirme**: Yük ve performans metriklerine dayalı otomatik ölçeklendirme
- **Yüksek Erişilebilirlik**: Çok bölgeli dağıtım ve hata toleransı
- **Yük Testi**: Kurumsal yük koşulları altında performans doğrulama
- **Felaket Kurtarma**: Otomatik yedekleme ve kurtarma prosedürleri

Hassas belgeleri ölçekli olarak işleyebilecek kurumsal düzeyde RAG sistemleri oluşturmaya hazır mısınız? Haydi, kurumsal için akıllı bilgi sistemleri tasarlayalım! 🏢📖✨

## Kod Uygulaması

Bu ders için tam çalışan kod örneği `05-dotnet-agent-framework.cs` dosyasında mevcuttur.

Örneği çalıştırmak için:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Ya da doğrudan `dotnet run` kullanın:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Kod şunları gösterir:

1. **Paket Kurulumu**: Azure AI Agents için gerekli NuGet paketlerini yükleme
2. **Ortam Yapılandırması**: Azure AI Foundry uç noktası ve model ayarlarını yükleme
3. **Belge Yükleme**: RAG işleme için bir belge yükleme
4. **Vektör Deposu Oluşturma**: Semantik arama için bir vektör deposu oluşturma
5. **Ajan Yapılandırması**: Dosya arama yetenekleri ile bir AI ajanı kurma
6. **Sorgu Yürütme**: Yüklenen belgeye karşı sorgular çalıştırma

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.