[![AI Ajanlarına Giriş](../../../translated_images/tr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Üstteki resme tıklayarak bu dersin videosunu izleyin)_


# Yapay Zeka Ajanlarına Giriş ve Ajan Kullanım Alanları

"AI Agents for Beginners" (Yeni Başlayanlar için Yapay Zeka Ajanları) kursuna hoş geldiniz! Bu kurs, Yapay Zeka Ajanları oluşturmak için temel bilgileri ve uygulamalı örnekleri sağlar.

Diğer öğrenenlerle ve Yapay Zeka Ajanı Oluşturucularıyla tanışmak ve bu kursla ilgili sorularınızı sormak için <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Topluluğu</a>'na katılın.

Bu kursa başlamak için, Yapay Zeka Ajanlarının ne olduğunu ve onları oluşturduğumuz uygulamalarda ve iş akışlarında nasıl kullanabileceğimizi daha iyi anlamakla başlıyoruz.

## Giriş

Bu ders şunları kapsar:

- Yapay Zeka Ajanları nedir ve farklı ajan türleri nelerdir?
- Hangi kullanım senaryoları Yapay Zeka Ajanları için daha uygundur ve bize nasıl yardımcı olurlar?
- Ajanik çözümler tasarlarken bazı temel yapı taşları nelerdir?

## Öğrenme Hedefleri
Bu dersi tamamladıktan sonra şunları yapabiliyor olmalısınız:

- Yapay Zeka Ajanı kavramlarını ve bunların diğer AI çözümlerinden nasıl farklılaştığını anlamak.
- Yapay Zeka Ajanlarını en verimli şekilde uygulamak.
- Hem kullanıcılar hem de müşteriler için ajanik çözümler üretken şekilde tasarlamak.

## Yapay Zeka Ajanlarını Tanımlama ve Ajan Türleri

### Yapay Zeka Ajanları nedir?

Yapay Zeka Ajanları, Büyük Dil Modelleri(LLMs)'nin yeteneklerini genişleterek LLM'lere araçlara ve bilgiye erişim sağlayarak eylem gerçekleştirmelerini mümkün kılan sistemlerdir.

Bu tanımı daha küçük parçalara ayıracak olalım:

- Sistem - Ajanları sadece tek bir bileşen olarak değil, birçok bileşenden oluşan bir sistem olarak düşünmek önemlidir. Temel düzeyde, bir Yapay Zeka Ajanının bileşenleri şunlardır:
  - Çevre - Yapay Zeka Ajanının çalıştığı tanımlı alan. Örneğin, bir seyahat rezervasyon ajanımız olsaydı, çevre ajanın görevleri tamamlamak için kullandığı seyahat rezervasyon sistemi olabilir.
  - Sensörler - Çevreler bilgiye sahiptir ve geri bildirim sağlar. Yapay Zeka Ajanları, çevrenin mevcut durumu hakkındaki bu bilgileri toplamak ve yorumlamak için sensörleri kullanır. Seyahat Rezervasyon Ajanı örneğinde, rezervasyon sistemi otel müsaitliği veya uçuş fiyatları gibi bilgiler sağlayabilir.
  - Aktüatörler - Yapay Zeka Ajanı çevrenin mevcut durumunu aldıktan sonra, mevcut görev için çevreyi değiştirmek adına hangi eylemi gerçekleştireceğine karar verir. Seyahat rezervasyon ajanı için bu, kullanıcı adına müsait bir odayı rezerve etmek olabilir.

![Ajanlar Nedir?](../../../translated_images/tr/what-are-ai-agents.1ec8c4d548af601a.webp)

**Büyük Dil Modelleri** - Ajan kavramı LLM'lerin ortaya çıkışından önce de vardı. LLM'lerle Yapay Zeka Ajanları oluşturmanın avantajı, insan dilini ve veriyi yorumlama yetenekleridir. Bu yetenek, LLM'lerin çevresel bilgileri yorumlamasını ve çevreyi değiştirmek için bir plan tanımlamasını sağlar.

**Eylem Gerçekleştirme** - Yapay Zeka Ajanı sistemleri dışında, LLM'ler eylem olarak genellikle kullanıcının istemine dayanarak içerik veya bilgi üretmekle sınırlıdır. Ajan sistemleri içinde, LLM'ler kullanıcının isteğini yorumlayarak ve çevrelerinde mevcut olan araçları kullanarak görevleri yerine getirebilirler.

**Araçlara Erişim** - LLM'nin hangi araçlara erişebileceği 1) çalıştığı çevre ve 2) ajanı geliştiren geliştirici tarafından tanımlanır. Seyahat ajanı örneğimizde, ajanın araçları rezervasyon sisteminde bulunan işlemlerle sınırlıdır ve/veya geliştirici ajanın uçuşlara erişimini kısıtlayabilir.

**Bellek+Bilgi** - Bellek, kullanıcı ile ajan arasındaki konuşma bağlamında kısa süreli olabilir. Uzun vadede, çevrenin sağladığı bilginin dışında Yapay Zeka Ajanları diğer sistemlerden, servislerden, araçlardan ve hatta diğer ajanlardan bilgi alabilir. Seyahat ajanı örneğinde, bu bilgi kullanıcıya ait seyahat tercihleri bilgisi olabilir ve müşteri veritabanında bulunabilir.

### Ajan türleri

Artık Yapay Zeka Ajanlarının genel bir tanımına sahip olduğumuza göre, bazı özel ajan türlerine ve bunların bir seyahat rezervasyon ajanına nasıl uygulanabileceğine bakalım.

| **Ajan Türü**                | **Açıklama**                                                                                                                       | **Örnek**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Basit Refleks Ajanlar**      | Önceden tanımlanmış kurallara dayalı olarak anında eylemler gerçekleştirir.                                                                                  | Seyahat acentesi e-postanın bağlamını yorumlar ve seyahat şikayetlerini müşteri hizmetlerine yönlendirir.                                                                                                                          |
| **Model Tabanlı Refleks Ajanlar** | Dünya modeline ve bu modeldeki değişikliklere dayalı eylemler gerçekleştirir.                                                              | Seyahat acentesi, geçmiş fiyat verilerine erişim sayesinde önemli fiyat değişikliklerine sahip rotaları önceliklendirir.                                                                                                             |
| **Hedef Tabanlı Ajanlar**         | Belirli hedeflere ulaşmak için hedefi yorumlayarak ve hedefe ulaşmak için eylemleri belirleyerek planlar oluşturur.                                  | Seyahat acentesi, mevcut konumdan varış noktasına gerekli seyahat düzenlemelerini (araba, toplu taşıma, uçuşlar) belirleyerek yolculuğu rezerve eder.                                                                                |
| **Fayda Tabanlı Ajanlar**      | Tercihleri göz önünde bulundurarak takasları sayısal olarak değerlendirir ve hedeflere nasıl ulaşılacağını belirler.                                               | Seyahat acentesi, seyahati rezerve ederken rahatlık ile maliyet arasındaki dengeyi tartarak faydayı maksimize eder.                                                                                                                                          |
| **Öğrenen Ajanlar**           | Geri bildirimlere yanıt vererek ve eylemleri buna göre ayarlayarak zaman içinde gelişir.                                                        | Seyahat acentesi, gezi sonrası anketlerden gelen müşteri geri bildirimlerini kullanarak gelecekteki rezervasyonlarda iyileştirmeler yapar.                                                                                                               |
| **Hiyerarşik Ajanlar**       | Çok seviyeli bir sistemde birden fazla ajan içerir; üst düzey ajanlar görevleri daha düşük düzey ajanların tamamlaması için alt görevlere böler. | Seyahat acentesi, bir seyahati iptal ederken görevi alt görevlere bölerek (örneğin belirli rezervasyonları iptal etme) alt düzey ajanların bunları tamamlamasını sağlar ve üst düzey ajana raporlar.                                     |
| **Çok Ajanlı Sistemler (MAS)** | Ajanlar görevleri bağımsız olarak, işbirlikçi veya rekabetçi şekilde tamamlar.                                                           | İşbirlikçi: Birden fazla ajan oteller, uçuşlar ve eğlence gibi belirli seyahat hizmetlerini rezerve eder. Rekabetçi: Birden fazla ajan paylaşılan bir otel rezervasyon takvimi üzerinde müşterileri otelde yerleştirmek için yarışır. |

## Ne Zaman Yapay Zeka Ajanları Kullanılmalı

Önceki bölümde, farklı ajan türlerinin seyahat rezervasyonunun farklı senaryolarında nasıl kullanılabileceğini açıklamak için Seyahat Acentesi kullanım durumunu kullandık. Kurs boyunca bu uygulamayı kullanmaya devam edeceğiz.

Yapay Zeka Ajanlarının en iyi kullanıldığı kullanım durumlarına bakalım:

![Yapay Zeka Ajanları ne zaman kullanılmalı?](../../../translated_images/tr/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Açık Uçlu Problemler** - LLM'nin bir görevi tamamlamak için gereken adımları belirlemesine izin verilir çünkü her zaman bir iş akışına sert kodlanamaz.
- **Çok Adımlı Süreçler** - AI Ajanının araçları veya bilgileri tek seferlik bir sorgulama yerine birden fazla tur boyunca kullanması gereken bir karmaşıklık seviyesini gerektiren görevler.
- **Zaman İçinde İyileşme** - Ajanın çevresinden veya kullanıcılardan gelen geri bildirimleri alarak zaman içinde iyileşebileceği görevler, daha iyi fayda sağlamak için.

Yapay Zeka Ajanları kullanmaya ilişkin daha fazla hususu Güvenilir AI Ajanları Oluşturma dersinde ele alıyoruz.

## Ajanik Çözümlerin Temelleri

### Ajan Geliştirme

Bir Yapay Zeka Ajanı sistemi tasarlamanın ilk adımı araçları, eylemleri ve davranışları tanımlamaktır. Bu kursta, Ajanlarımızı tanımlamak için **Azure AI Agent Service** kullanmaya odaklanıyoruz. Aşağıdaki özellikleri sunar:

- OpenAI, Mistral ve Llama gibi Açık Modellerin seçimi
- Tripadvisor gibi sağlayıcılar aracılığıyla Lisanslı Verilerin kullanımı
- Standartlaştırılmış OpenAPI 3.0 araçlarının kullanımı

### Ajanik Desenler

LLM'lerle iletişim istemler (prompts) aracılığıyla olur. Yarı otonom doğası nedeniyle, çevredeki bir değişiklikten sonra LLM'yi manuel olarak yeniden istemlememiz her zaman mümkün veya gerekli değildir. LLM'yi daha ölçeklenebilir bir şekilde birden fazla adım boyunca istemlemek için bize olanak sağlayan **Ajanik Desenler** kullanırız.

Bu kurs, şu anda popüler olan bazı ajanik desenlere ayrılmıştır.

### Ajanik Çerçeveler

Ajanik Çerçeveler, geliştiricilerin kod aracılığıyla ajanik desenleri uygulamalarına olanak tanır. Bu çerçeveler, daha iyi AI Ajanı iş birliği için şablonlar, eklentiler ve araçlar sunar. Bu faydalar, AI Ajanı sistemleri için daha iyi gözlemlenebilirlik ve sorun giderme yetenekleri sağlar.

Bu kursta, üretime hazır Yapay Zeka ajanları oluşturmak için Microsoft Agent Framework (MAF)'ı inceleyeceğiz.

## Örnek Kodlar

- Python: [Ajan Çerçevesi](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Ajan Çerçevesi](./code_samples/01-dotnet-agent-framework.md)

## Yapay Zeka Ajanları Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle buluşmak, ofis saatlerine katılmak ve Yapay Zeka Ajanları sorularınıza cevap almak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)'a katılın.

## Önceki Ders

[Kurs Kurulumu](../00-course-setup/README.md)

## Sonraki Ders

[Ajanik Çerçeveleri Keşfetmek](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için özen göstermemize rağmen, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki metin, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama nedeniyle sorumluluk kabul etmiyoruz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->