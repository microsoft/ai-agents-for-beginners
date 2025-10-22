<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T13:06:26+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "tr"
}
-->
[![Yapay Zeka Ajanlarına Giriş](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.tr.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Yapay Zeka Ajanlarına ve Kullanım Alanlarına Giriş

"Yeni Başlayanlar için Yapay Zeka Ajanları" kursuna hoş geldiniz! Bu kurs, Yapay Zeka Ajanları oluşturmak için temel bilgiler ve uygulamalı örnekler sunar.

Bu kursa katılarak diğer öğrenenlerle ve Yapay Zeka Ajanı geliştiricileriyle tanışabilir ve kursla ilgili sorularınızı sorabilirsiniz.

Bu kursa başlamak için, önce Yapay Zeka Ajanlarının ne olduğunu ve bunları oluşturduğumuz uygulamalarda ve iş akışlarında nasıl kullanabileceğimizi daha iyi anlamaya çalışacağız.

## Giriş

Bu ders şunları kapsar:

- Yapay Zeka Ajanları nedir ve farklı türleri nelerdir?
- Yapay Zeka Ajanları için en uygun kullanım alanları nelerdir ve bize nasıl yardımcı olabilirler?
- Ajanik Çözümler tasarlarken temel yapı taşları nelerdir?

## Öğrenme Hedefleri
Bu dersi tamamladıktan sonra:

- Yapay Zeka Ajanı kavramlarını ve diğer yapay zeka çözümlerinden nasıl farklılaştığını anlayabileceksiniz.
- Yapay Zeka Ajanlarını en verimli şekilde uygulayabileceksiniz.
- Hem kullanıcılar hem de müşteriler için üretken bir şekilde Ajanik çözümler tasarlayabileceksiniz.

## Yapay Zeka Ajanlarını Tanımlama ve Türleri

### Yapay Zeka Ajanları Nedir?

Yapay Zeka Ajanları, **Büyük Dil Modellerinin (LLM)** **eylem gerçekleştirmesini** sağlayan, LLM'lere **araçlara erişim** ve **bilgi** vererek yeteneklerini genişleten **sistemlerdir**.

Bu tanımı daha küçük parçalara ayıralım:

- **Sistem** - Ajanları yalnızca tek bir bileşen olarak değil, birçok bileşenden oluşan bir sistem olarak düşünmek önemlidir. Bir Yapay Zeka Ajanının temel bileşenleri şunlardır:
  - **Ortam** - Yapay Zeka Ajanının çalıştığı tanımlı alan. Örneğin, bir seyahat rezervasyonu yapan Yapay Zeka Ajanımız varsa, ortam, ajanın görevleri tamamlamak için kullandığı seyahat rezervasyon sistemi olabilir.
  - **Sensörler** - Ortamlar bilgi sağlar ve geri bildirimde bulunur. Yapay Zeka Ajanları, ortamın mevcut durumu hakkında bilgi toplamak ve yorumlamak için sensörleri kullanır. Seyahat Rezervasyon Ajanı örneğinde, seyahat rezervasyon sistemi otel müsaitliği veya uçuş fiyatları gibi bilgiler sağlayabilir.
  - **Eyleyiciler** - Yapay Zeka Ajanı, ortamın mevcut durumunu aldıktan sonra, mevcut görev için ortamı değiştirmek üzere hangi eylemi gerçekleştireceğine karar verir. Seyahat rezervasyon ajanı için bu, kullanıcı için uygun bir odayı rezerve etmek olabilir.

![Yapay Zeka Ajanları Nedir?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.tr.png)

**Büyük Dil Modelleri** - Ajan kavramı, LLM'lerin oluşturulmasından önce de vardı. LLM'lerle Yapay Zeka Ajanları oluşturmanın avantajı, insan dilini ve veriyi yorumlama yetenekleridir. Bu yetenek, LLM'lerin çevresel bilgileri yorumlamasını ve ortamı değiştirmek için bir plan tanımlamasını sağlar.

**Eylem Gerçekleştirme** - Yapay Zeka Ajanı sistemleri dışında, LLM'ler yalnızca bir kullanıcının isteğine göre içerik veya bilgi üretmekle sınırlıdır. Yapay Zeka Ajanı sistemlerinde ise, LLM'ler kullanıcının isteğini yorumlayarak ve ortamlarında mevcut araçları kullanarak görevleri yerine getirebilir.

**Araçlara Erişim** - LLM'nin hangi araçlara erişimi olduğu, 1) çalıştığı ortam ve 2) Yapay Zeka Ajanını geliştiren kişi tarafından tanımlanır. Seyahat ajanı örneğimizde, ajanın araçları, rezervasyon sisteminde mevcut işlemlerle sınırlıdır ve/veya geliştirici, ajanın araç erişimini yalnızca uçuşlarla sınırlayabilir.

**Hafıza+Bilgi** - Hafıza, kullanıcı ile ajan arasındaki konuşma bağlamında kısa vadeli olabilir. Uzun vadede, ortamın sağladığı bilgilerin dışında, Yapay Zeka Ajanları diğer sistemlerden, hizmetlerden, araçlardan ve hatta diğer ajanlardan bilgi alabilir. Seyahat ajanı örneğinde, bu bilgi, bir müşteri veritabanında bulunan kullanıcının seyahat tercihleri olabilir.

### Farklı Ajan Türleri

Artık Yapay Zeka Ajanlarının genel bir tanımına sahip olduğumuza göre, bazı özel ajan türlerine ve bunların bir seyahat rezervasyonu yapan Yapay Zeka Ajanına nasıl uygulanabileceğine bakalım.

| **Ajan Türü**                | **Açıklama**                                                                                                                       | **Örnek**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Basit Refleks Ajanları**      | Önceden tanımlanmış kurallara dayalı olarak anında eylemler gerçekleştirir.                                                                                  | Seyahat ajanı, e-postanın bağlamını yorumlar ve seyahat şikayetlerini müşteri hizmetlerine yönlendirir.                                                                                                                          |
| **Model Tabanlı Refleks Ajanları** | Dünyanın bir modeline ve bu modeldeki değişikliklere dayalı olarak eylemler gerçekleştirir.                                                              | Seyahat ajanı, geçmiş fiyat verilerine erişerek önemli fiyat değişiklikleri olan rotaları önceliklendirir.                                                                                                             |
| **Hedef Tabanlı Ajanlar**         | Belirli hedeflere ulaşmak için planlar oluşturur, hedefi yorumlar ve ona ulaşmak için gerekli eylemleri belirler.                                  | Seyahat ajanı, mevcut konumdan varış noktasına gerekli seyahat düzenlemelerini (araba, toplu taşıma, uçuşlar) belirleyerek bir yolculuk rezervasyonu yapar.                                                                                |
| **Fayda Tabanlı Ajanlar**      | Tercihleri dikkate alır ve hedeflere ulaşmak için sayısal olarak ödünleri tartar.                                               | Seyahat ajanı, seyahat rezervasyonu yaparken maliyet ve rahatlık arasında denge kurarak faydayı maksimize eder.                                                                                                                                          |
| **Öğrenen Ajanlar**           | Geri bildirimlere yanıt vererek ve eylemlerini buna göre ayarlayarak zamanla gelişir.                                                        | Seyahat ajanı, müşteri geri bildirimlerini kullanarak gelecekteki rezervasyonlarda ayarlamalar yapar.                                                                                                               |
| **Hiyerarşik Ajanlar**       | Birden fazla ajanı katmanlı bir sistemde barındırır, üst düzey ajanlar görevleri alt düzey ajanlar için alt görevlere böler. | Seyahat ajanı, bir seyahati iptal ederken görevi alt görevlere (örneğin, belirli rezervasyonları iptal etmek) böler ve alt düzey ajanların bunları tamamlamasını sağlar, ardından üst düzey ajana rapor verir.                                     |
| **Çoklu Ajan Sistemleri (MAS)** | Ajanlar görevleri bağımsız olarak, işbirlikçi veya rekabetçi bir şekilde tamamlar.                                                           | İşbirlikçi: Birden fazla ajan, oteller, uçuşlar ve eğlence gibi belirli seyahat hizmetlerini rezerve eder. Rekabetçi: Birden fazla ajan, müşterileri otele yerleştirmek için paylaşılan bir otel rezervasyon takvimini yönetir ve rekabet eder. |

## Yapay Zeka Ajanları Ne Zaman Kullanılır?

Önceki bölümde, farklı ajan türlerinin seyahat rezervasyonu senaryolarında nasıl kullanılabileceğini açıklamak için Seyahat Ajanı kullanım senaryosunu kullandık. Bu uygulamayı kurs boyunca kullanmaya devam edeceğiz.

Şimdi Yapay Zeka Ajanlarının en iyi kullanıldığı kullanım alanlarına bakalım:

![Yapay Zeka Ajanları Ne Zaman Kullanılır?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.tr.png)

- **Açık Uçlu Problemler** - LLM'nin bir görevi tamamlamak için gereken adımları belirlemesine izin vermek, çünkü bu adımlar her zaman bir iş akışına sabitlenemez.
- **Çok Adımlı Süreçler** - Yapay Zeka Ajanının, tek seferlik bilgi alımı yerine, birden fazla adımda araçları veya bilgileri kullanmasını gerektiren karmaşıklık düzeyine sahip görevler.  
- **Zamanla Gelişim** - Ajanın, ortamından veya kullanıcılarından geri bildirim alarak zamanla gelişebileceği ve daha iyi fayda sağlayabileceği görevler.

Yapay Zeka Ajanlarını kullanmaya dair daha fazla hususu Güvenilir Yapay Zeka Ajanları Oluşturma dersinde ele alıyoruz.

## Ajanik Çözümlerin Temelleri

### Ajan Geliştirme

Bir Yapay Zeka Ajanı sistemi tasarlamanın ilk adımı, araçları, eylemleri ve davranışları tanımlamaktır. Bu kursta, ajanlarımızı tanımlamak için **Azure AI Agent Service** kullanmaya odaklanıyoruz. Bu hizmet şu özellikleri sunar:

- OpenAI, Mistral ve Llama gibi Açık Modellerin seçimi
- Tripadvisor gibi sağlayıcılar aracılığıyla Lisanslı Veri kullanımı
- Standartlaştırılmış OpenAPI 3.0 araçlarının kullanımı

### Ajanik Kalıplar

LLM'lerle iletişim, istemler aracılığıyla gerçekleşir. Yapay Zeka Ajanlarının yarı otonom doğası göz önüne alındığında, ortamda bir değişiklikten sonra LLM'yi manuel olarak yeniden istemek her zaman mümkün veya gerekli değildir. **Ajanik Kalıplar**, LLM'yi birden fazla adımda daha ölçeklenebilir bir şekilde istememize olanak tanır.

Bu kurs, mevcut popüler Ajanik kalıplardan bazılarına ayrılmıştır.

### Ajanik Çerçeveler

Ajanik Çerçeveler, geliştiricilerin ajanik kalıpları kod aracılığıyla uygulamasına olanak tanır. Bu çerçeveler, daha iyi Yapay Zeka Ajanı iş birliği için şablonlar, eklentiler ve araçlar sunar. Bu avantajlar, Yapay Zeka Ajanı sistemlerinin daha iyi gözlemlenmesi ve sorunlarının giderilmesi yeteneklerini sağlar.

Bu kursta, araştırma odaklı AutoGen çerçevesini ve Semantic Kernel'den üretime hazır Agent çerçevesini keşfedeceğiz.

### Yapay Zeka Ajanları Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve Yapay Zeka Ajanlarıyla ilgili sorularınızı yanıtlamak için [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) topluluğuna katılın.

## Önceki Ders

[Kurs Kurulumu](../00-course-setup/README.md)

## Sonraki Ders

[Ajanik Çerçeveleri Keşfetmek](../02-explore-agentic-frameworks/README.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.