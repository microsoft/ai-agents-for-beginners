[![Intro to AI Agents](../../../translated_images/tr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# AI Ajanlara ve Ajan Kullanım Senaryolarına Giriş

**Yeni Başlayanlar için AI Ajanları** kursuna hoş geldiniz! Bu kurs, sıfırdan AI Ajanları oluşturmak için temel bilgileri — ve gerçek çalışan kodları — sunar.

Sorularınızı yanıtlamaktan memnun olan öğrenenler ve AI geliştiricileri ile dolu olan <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Topluluğu</a>'nda selam vermeye gelin.

Yapmaya başlamadan önce, AI Ajanın *nedir* ve ne zaman kullanmanın mantıklı olduğunu gerçekten anladığımızdan emin olalım.

---

## Giriş

Bu ders şunları kapsar:

- AI Ajanların ne olduğu ve var olan farklı türleri
- Hangi tür görevlerin AI Ajanlar için en uygun olduğu
- Bir Ajanik çözüm tasarlarken kullanacağınız temel yapı taşları

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabilmelisiniz:

- Bir AI Ajanın ne olduğunu ve sıradan AI çözümlerinden nasıl farklı olduğunu açıklayabilmek
- Ne zaman bir AI Ajana başvurmanız (ve ne zaman başvurmamanız) gerektiğini bilmek
- Gerçek dünya problemleri için temel bir Ajanik çözüm taslağı çizebilmek

---

## AI Ajanları Tanımlama ve AI Ajan Türleri

### AI Ajanlar nedir?

Bunu anlamanın basit bir yolu şöyle:

> **AI Ajanlar, Büyük Dil Modellerinin (LLM) yalnızca istemlere yanıt vermekle kalmayıp — araçlar ve bilgi vererek dünyada *işler yapmasına* olanak tanıyan sistemlerdir.**

Bunu biraz açalım:

- **Sistem** — Bir AI Ajan tek başına bir şey değildir. Bir arada çalışan parçalar koleksiyonudur. Her ajan temelde üç parçaya sahiptir:
  - **Çevre** — Ajanın çalıştığı alan. Bir seyahat rezervasyon ajanı için bu, rezervasyon platformunun kendisi olur.
  - **Sensörler** — Ajanın çevresinin mevcut durumunu okuma yöntemi. Seyahat ajanımız otel müsaitliğini veya uçuş fiyatlarını kontrol edebilir.
  - **Aktüatörler** — Ajanın eylemde bulunma şekli. Seyahat ajanı bir oda ayırtabilir, onay gönderir veya rezervasyonu iptal edebilir.

![What Are AI Agents?](../../../translated_images/tr/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Büyük Dil Modelleri** — Ajanlar LLM’lerden önce vardı ancak LLM’ler modern ajanları bu kadar güçlü kılan şeydir. Doğal dili anlayabilir, bağlam hakkında mantık yürütebilir ve belirsiz kullanıcı isteğini somut bir eylem planına dönüştürebilirler.

- **Eylemde Bulunma** — Bir ajan sistemi olmadan LLM sadece metin üretir. Bir ajan sistemi içinde, LLM gerçekten adımlar *yürütür* — bir veritabanında arama yapar, API çağırır, mesaj gönderir.

- **Araçlara Erişim** — Ajanın kullanabileceği araçlar şuna bağlıdır: (1) çalıştığı ortam ve (2) geliştiricinin ajana verdiği seçenekler. Bir seyahat ajanı uçuşları arayabilir ancak müşteri kayıtlarını düzenleyemez — tamamen kurduğunuz ağ ile ilgilidir.

- **Bellek + Bilgi** — Ajanların kısa süreli belleği (şimdiki konuşma) ve uzun süreli belleği (müşteri veritabanı, geçmiş etkileşimler) olabilir. Seyahat ajanı, pencere kenarı koltuğu tercih ettiğinizi "hatırlayabilir".

---

### AI Ajanların Farklı Türleri

Tüm ajanlar aynı şekilde inşa edilmemiştir. İşte ana türlerin bir dökümü, seyahat rezervasyon ajanını örnek alarak:

| **Ajan Türü** | **Ne Yapar** | **Seyahat Ajanı Örneği** |
|---|---|---|
| **Basit Refleks Ajanlar** | Sert kodlanmış kuralları takip eder — hafıza veya planlama yok. | Şikayet e-postası görür → bunu müşteri hizmetlerine yönlendirir. Hepsi bu. |
| **Model Tabanlı Refleks Ajanlar** | Dünyanın içsel bir modelini tutar ve değişikliklere göre günceller. | Tarihsel uçuş fiyatlarını takip eder ve aniden pahalı olan güzergahları işaretler. |
| **Hedef Tabanlı Ajanlar** | Akılda bir hedef vardır ve adım adım nasıl ulaşılacağını bulur. | Mevcut konumunuzdan varış noktanıza kadar tüm seyahati (uçuş, araba, otel) ayırtır. |
| **Fayda Tabanlı Ajanlar** | Sadece bir çözüm bulmaz — tercihleriniz için en yüksek puanı alan en iyi çözümü bulur. | Maliyet ile kolaylığı dengeler ve tercihlerinize en uygun seyahati önerir. |
| **Öğrenen Ajanlar** | Geri bildirimlerden öğrenerek zaman içinde gelişir. | Gelecekteki rezervasyon önerilerini, yolculuk sonrası anket sonuçlarına göre ayarlar. |
| **Hiyerarşik Ajanlar** | Üst düzey bir ajan işi alt görevlerle böler ve bunları alt ajanlara devreder. | "Seyahat iptal" talebi; uçuş iptali, otel iptali, araba kiralama iptali olarak alt ajanlara ayrılır. |
| **Çoklu Ajan Sistemleri (MAS)** | Birbirinden bağımsız birden çok ajan birlikte (ya da rekabet halinde) çalışır. | İşbirlikçi: oteller, uçuşlar ve eğlence ayrı ajanlar tarafından yönetilir. Rekabetçi: çeşitli ajanlar en iyi fiyata otel odası doldurmak için yarışır. |

---

## AI Ajanlar Ne Zaman Kullanılır

Sadece bir AI Ajan *kullanabilmeniz*, her zaman *kullanmanız gerektiği* anlamına gelmez. İşte ajanların gerçekten parladığı durumlar:

![When to use AI Agents?](../../../translated_images/tr/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Açık Uçlu Problemler** — Sorunu çözmek için adımlar önceden programlanamaz. LLM’in yolu dinamik olarak kendisinin çözmesi gerekir.
- **Çok Adımlı Süreçler** — Tek bir sorgulu veya üretimli işlemden fazlasını gerektiren, birden çok turda araç kullanmayı içeren görevler.
- **Zamanla İyileşme** — Sistem, kullanıcı geri bildirimi veya çevresel sinyallere dayanarak daha akıllı hale gelmeli ise.

Kursun ilerleyen dersinde, **Güvenilir AI Ajanlar Oluşturma** dersinde, AI Ajanların ne zaman (ve ne zaman *kullanılmaması* gerektiği) konusuna daha derinlemesine bakacağız.

---

## Ajanik Çözümlerin Temelleri

### Ajan Geliştirme

Bir ajan oluştururken yaptığınız ilk şey, *ne yapabileceğini* tanımlamaktır — araçları, eylemleri ve davranışları.

Bu kursta, ana platform olarak **Azure AI Agent Service**’i kullanıyoruz. Şunları destekler:

- OpenAI, Mistral ve Llama gibi açık modeller
- Tripadvisor gibi sağlayıcılardan lisanslı veriler
- Standardize edilmiş OpenAPI 3.0 araç tanımları

### Ajanik Desenler

LLM’lerle, istemler aracılığıyla iletişim kurarsınız. Ajanlarda her zaman her istemi elle yazamazsınız — ajan, çok sayıda adımda eylemde bulunmalı. İşte burada **Ajanik Desenler** devreye girer. Bunlar, LLM’leri daha ölçeklenebilir, güvenilir şekilde yönlendirme ve düzenleme için tekrar kullanılabilir stratejilerdir.

Bu kurs, en yaygın ve faydalı ajanik desenler etrafında yapılandırılmıştır.

### Ajanik Çerçeveler

Ajanik Çerçeveler, geliştiricilere hazır şablonlar, araçlar ve altyapı sağlar. Ajan inşasını kolaylaştırır:

- Araçları ve yetenekleri bağlamak
- Ajanın ne yaptığını izlemek (ve hata ayıklamak)
- Birden çok ajan arasında işbirliği yapmak

Bu kursta, üretime hazır ajanlar oluşturmak için **Microsoft Agent Framework (MAF)** üzerinde yoğunlaşıyoruz.

---

## Kod Örnekleri

Uygulamada görmek ister misiniz? İşte bu dersin kod örnekleri:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Sorularınız mı Var?

Diğer öğrenenlerle bağlantı kurmak, ofis saatlerine katılmak ve topluluktan AI Ajan sorularınıza cevap almak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)’a katılın.

---

## Önceki Ders

[Course Setup](../00-course-setup/README.md)

## Sonraki Ders

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı AI çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, ana dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek herhangi bir yanlış anlaşılma veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->