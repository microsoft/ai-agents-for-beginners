[![Intro to AI Agents](../../../translated_images/tr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Bu dersin videosunu izlemek için yukarıdaki resme tıklayın)_

# Yapay Zeka Ajanlarına ve Ajan Kullanım Alanlarına Giriş

**Yapay Zeka Ajanları Yeni Başlayanlar İçin** kursuna hoş geldiniz! Bu kurs size temel bilgileri — ve gerçek çalışan kodu — sunarak Yapay Zeka Ajanlarını sıfırdan inşa etmeye başlamanızı sağlar.

Sorularınızı yanıtlamaktan mutluluk duyan öğrenenler ve yapay zeka geliştiricileriyle dolu olan <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Topluluğu</a>'nda selam verin.

İnşa etmeye başlamadan önce, aslında bir Yapay Zeka Ajanının *ne olduğunu* ve ne zaman kullanmanın mantıklı olduğunu anlayalım.

---

## Giriş

Bu ders şunları kapsar:

- Yapay Zeka Ajanlarının ne olduğu ve var olan farklı türleri
- Yapay Zeka Ajanlarının en iyi kullanıldığı görev türleri
- Bir Ajanik çözüm tasarlarken kullanacağınız temel yapı taşları

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabiliyor olmalısınız:

- Yapay Zeka Ajanının ne olduğunu ve sıradan bir yapay zeka çözümünden nasıl farklı olduğunu açıklamak
- Ne zaman bir Yapay Zeka Ajanına başvurmanız gerektiğini (ve ne zaman gerekmediğini) bilmek
- Gerçek dünya sorunları için temel bir Ajanik çözüm tasarımı çizebilmek

---

## Yapay Zeka Ajanlarının Tanımı ve Yapay Zeka Ajan Türleri

### Yapay Zeka Ajanları Nedir?

Basit bir şekilde şöyle düşünebilirsiniz:

> **Yapay Zeka Ajanları, Büyük Dil Modellerinin (LLM’lerin) sadece istemlere yanıt vermekle kalmayıp dünyada *eylem yapabilmesini* sağlayan sistemlerdir — onlara araçlar ve bilgi sunarak hareket etmelerini sağlarlar.**

Bunu biraz açalım:

- **Sistem** — Bir Yapay Zeka Ajanı sadece tek bir şey değildir. Bir arada çalışan parçalardan oluşan bir koleksiyondur. Temelde, her ajanın üç parçası vardır:
  - **Ortam** — Ajanın çalıştığı alan. Bir seyahat rezervasyon ajanı için bu, rezervasyon platformunun kendisi olur.
  - **Sensörler** — Ajanın ortamının mevcut durumunu nasıl okuduğu. Seyahat ajanımız otel müsaitliğini veya uçuş fiyatlarını kontrol edebilir.
  - **Eyleyiciler** — Ajanın nasıl hareket ettiği. Seyahat ajanı bir oda rezervasyonu yapabilir, onay gönderebilir veya bir rezervasyonu iptal edebilir.

![What Are AI Agents?](../../../translated_images/tr/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Büyük Dil Modelleri** — Ajanlar, LLM’lerden önce vardı ama modern ajanları bu LLM’ler bu kadar güçlü yapıyor. Doğal dili anlayabilir, bağlam hakkındaki çıkarımlar yapabilir ve belirsiz kullanıcı isteklerini somut eylem planlarına çevirebilirler.

- **Eylem Yapmak** — Bir ajan sistemi olmadan, bir LLM sadece metin üretir. Bir ajan sisteminin içinde, LLM gerçekten *adımları yürütür* — bir veritabanını arar, bir API çağırır, mesaj gönderir.

- **Araçlara Erişim** — Ajanın hangi araçları kullanabileceği (1) içinde çalıştığı ortama ve (2) geliştiricinin verdiği araçlara bağlıdır. Seyahat ajanı uçuşları arayabilir ama müşteri kayıtlarını düzenleyemeyebilir — tamamen sizin bağladığınız şeylere bağlıdır.

- **Hafıza + Bilgi** — Ajanlar kısa süreli hafızaya (şimdiki konuşma) ve uzun süreli hafızaya (müşteri veritabanı, geçmiş etkileşimler) sahip olabilirler. Seyahat ajanı pencere kenarı koltuğu tercih ettiğinizi "hatırlayabilir".

---

### Yapay Zeka Ajanlarının Farklı Türleri

Tüm ajanlar aynı şekilde yapılmaz. İşte ana türlerin bir dökümü, seyahat rezervasyon ajanı örneği üzerinden:

| **Ajan Türü** | **Ne Yapar** | **Seyahat Ajanı Örneği** |
|---|---|---|
| **Basit Refleks Ajanları** | Sert kodlanmış kuralları izler — hafıza yok, planlama yok. | Bir şikayet e-postası görür → müşteri hizmetlerine iletir. Hepsi bu. |
| **Model-Tabanlı Refleks Ajanları** | Dünyanın içsel bir modelini tutar ve değiştikçe günceller. | Tarihsel uçuş fiyatlarını takip eder ve aniden pahalılaşan rotaları işaretler. |
| **Hedef-Tabanlı Ajanlar** | Aklında bir hedef vardır ve ona ulaşmak için adım adım plan yapar. | Mevcut konumunuzdan hedefinize tam bir seyahat (uçuşlar, araba, otel) rezervasyonu yapar. |
| **Yarar-Tabanlı Ajanlar** | Sadece *bir* çözüm bulmakla kalmaz — takasları değerlendirerek *en iyi* çözümü bulur. | Maliyet ve konforu dengeler, tercihlerinize en uygun seyahati bulur. |
| **Öğrenen Ajanlar** | Geri bildirimlerden öğrenerek zamanla daha iyi olur. | Seyahat sonrası anket sonuçlarına göre gelecek rezervasyon tavsiyelerini ayarlar. |
| **Hiyerarşik Ajanlar** | Yüksek seviyeli bir ajan işi alt görevlere böler ve aşağı seviyedeki ajanlara devreder. | "Seyahati iptal et" isteği: uçuş iptali, otel iptali, araç kiralama iptali şeklinde alt ajana verilir. |
| **Çoklu Ajan Sistemleri (MAS)** | Birden fazla bağımsız ajan birlikte (veya rekabet ederek) çalışır. | İşbirlikçi: farklı ajanlar otelleri, uçuşları ve eğlenceyi yönetir. Rekabetçi: birden fazla ajan en iyi fiyata otel odası doldurmak için yarışır. |

---

## Yapay Zeka Ajanlarını Ne Zaman Kullanmalı?

Sadece *kullanabiliyor* olmanız her zaman *kullanmanız* gerektiği anlamına gelmez. İşte ajanların gerçekten parladığı durumlar:

![When to use AI Agents?](../../../translated_images/tr/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Açık Uçlu Problemler** — Sorunu çözmek için adımlar önceden programlanamaz. LLM'nin yolu dinamik olarak bulması gerekir.
- **Çok Adımlı Süreçler** — Tek bir arama veya üretimden çok, çoklu tur araç kullanımı gereken görevler.
- **Zaman İçinde İyileşme** — Sistem, kullanıcı geri bildirimi veya çevresel sinyallere göre daha akıllı hale gelmeli.

Kursun ilerleyen derslerinde **Güvenilir Yapay Zeka Ajanları İnşası** dersinde ne zaman (ve ne zaman *kullanılmayacağını*) daha derinlemesine inceleyeceğiz.

---

## Ajanik Çözümlerin Temelleri

### Ajan Geliştirme

Bir ajan inşa ederken ilk yapacağınız şey *ne yapabileceğini* tanımlamaktır — araçları, eylemleri ve davranışları.

Bu kursta ana platform olarak **Azure AI Agent Service** kullanıyoruz. Bu platform şunları destekler:

- OpenAI, Mistral ve Meta (Llama) gibi sağlayıcılardan modeller
- Tripadvisor gibi sağlayıcılardan lisanslı veriler
- Standartlaştırılmış OpenAPI 3.0 araç tanımları

### Ajanik Desenler

LLM’lerle iletişim kurmak için istemler (promptlar) kullanırsınız. Ajanlarda her zaman her istemi elle yazamazsınız — ajan çoklu adım boyunca eylem yapmalıdır. İşte burada **Ajanik Desenler** devreye girer. Bunlar, LLM’leri daha ölçeklenebilir ve güvenilir şekilde yönlendirmek ve düzenlemek için tekrar kullanılabilir stratejilerdir.

Bu kurs, en yaygın ve kullanışlı ajanik desenler etrafında yapılandırılmıştır.

### Ajanik Çerçeveler

Ajanik Çerçeveler, geliştiricilere ajanlar inşa etmek için hazır şablonlar, araçlar ve altyapı sunar. Şu konuları kolaylaştırırlar:

- Araçları ve yetenekleri bağlamak
- Ajanın ne yaptığını gözlemlemek (başarısız olduğunda hata ayıklamak için)
- Birden fazla ajan arasında iş birliği yapmak

Bu kursta, üretime hazır ajanlar oluşturmak için **Microsoft Agent Framework (MAF)** üzerine odaklanıyoruz.

---

## Kod Örnekleri

İncelemeye hazır mısınız? İşte bu dersin kod örnekleri:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Sorularınız mı var?

Diğer öğrenenlerle bağlantı kurmak, ofis saatlerine katılmak ve toplumdan Yapay Zeka Ajanları hakkındaki sorularınızı yanıtlamak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)'a katılın.

---

## Önceki Ders

[Course Setup](../00-course-setup/README.md)

## Sonraki Ders

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->