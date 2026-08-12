[![Yapay Zeka Ajanlarına Giriş](../../../translated_images/tr/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Yapay Zeka Ajanlarına ve Ajan Kullanım Alanlarına Giriş

**Yapay Zeka Ajanlarına Yeni Başlayanlar için** kursuna hoş geldiniz! Bu kurs, yapay zeka ajanlarını sıfırdan inşa etmeye başlamanız için temel bilgileri — ve gerçek çalışan kodları — sunar.

<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Topluluğu</a>'nda bize selam vermeye gelin — burası, soruları yanıtlamaktan memnun olan öğrenenler ve yapay zeka geliştiricileri ile dolu.

İnşa etmeye başlamadan önce, gerçekten bir Yapay Zeka Ajanının *ne olduğunu* ve ne zaman kullanmanın anlamlı olduğunu iyice anlayalım.

---

## Giriş

Bu ders şunları kapsar:

- Yapay Zeka Ajanlarının ne olduğu ve var olan farklı türleri
- Yapay Zeka Ajanlarının en uygun olduğu görev türleri
- Bir Ajanik çözüm tasarlarken kullanacağınız temel yapı taşları

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabilmelisiniz:

- Bir Yapay Zeka Ajanının ne olduğunu ve normal bir yapay zeka çözümünden nasıl farklı olduğunu açıklamak
- Ne zaman bir Yapay Zeka Ajanına başvurulacağını (ve ne zaman başvurulmaması gerektiğini) bilmek
- Gerçek bir dünya problemi için temel bir ajanik çözüm tasarımı taslağı hazırlamak

---

## Yapay Zeka Ajanlarını Tanımlama ve Yapay Zeka Ajan Türleri

### Yapay Zeka Ajanları Nedir?

İşte basit bir şekilde düşünmek:

> **Yapay Zeka Ajanları, Büyük Dil Modellerinin (LLM'lerin) gerçekten *bir şeyler yapmasını* sağlayan sistemlerdir — onlara sadece komutlara yanıt vermek yerine dünyada harekete geçmeleri için araçlar ve bilgi sunarlar.**

Bunu biraz açalım:

- **Sistem** — Bir Yapay Zeka Ajanı sadece tek bir şey değildir. Bir arada çalışan parçalardan oluşan bir bütündür. Temelinde, her ajanın üç parçası vardır:
  - **Ortam** — Ajanın çalıştığı alan. Bir seyahat rezervasyon ajanı için, rezervasyon platformunun kendisi olur.
  - **Sensörler** — Ajanın ortamın mevcut durumunu okuma biçimi. Seyahat ajanımız otel müsaitliğini veya uçuş fiyatlarını kontrol edebilir.
  - **Eyleyiciler (Aktüatörler)** — Ajanın eylem alma biçimi. Seyahat ajanı bir oda rezerve edebilir, onay gönderir veya rezervasyonu iptal edebilir.

![Yapay Zeka Ajanları Nedir?](../../../translated_images/tr/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Büyük Dil Modelleri** — Ajanlar LLM'lerden önce de vardı, ancak LLM'ler modern ajanları çok güçlü kılar. Doğal dili anlayabilir, bağlam üzerinde akıl yürütebilir ve belirsiz bir kullanıcı isteğini somut bir eylem planına dönüştürebilirler.

- **Eylemde Bulunmak** — Bir ajan sistemi olmadan LLM sadece metin üretir. Ajan sistemi içinde, LLM gerçekten *adımları yürütür* — bir veritabanında arama yapabilir, bir API arayabilir, mesaj gönderebilir.

- **Araçlara Erişim** — Ajanın kullanabileceği araçlar, (1) çalıştığı ortama ve (2) geliştiricinin ona verdiği yeteneklere bağlıdır. Bir seyahat ajanı uçuşları arayabilir ama müşteri kayıtlarını düzenleyemez — her şey sizin ona bağladıklarınıza bağlıdır.

- **Hafıza + Bilgi** — Ajanların kısa süreli hafızası (mevcut konuşma) ve uzun süreli hafızası (müşteri veritabanı, önceki etkileşimler) olabilir. Seyahat ajanı sizin pencere kenarı koltuğu tercih ettiğinizi "hatırlayabilir".

---

### Yapay Zeka Ajanlarının Farklı Türleri

Bütün ajanlar aynı şekilde inşa edilmez. İşte temel türlerin seyahat rezervasyon ajanı örneğiyle açıklaması:

| **Ajan Türü** | **Yaptığı İş** | **Seyahat Ajanı Örneği** |
|---|---|---|
| **Basit Refleks Ajanları** | Sert kodlanmış kuralları izler — hafıza yok, planlama yok. | Bir şikayet e-postası görür → müşteri hizmetlerine iletir. Hepsi bu. |
| **Model Tabanlı Refleks Ajanları** | Dünyanın dahili bir modelini tutar ve değişikliklere göre günceller. | Tarihsel uçuş fiyatlarını takip eder ve aniden pahalı olan rotaları işaretler. |
| **Amaç Odaklı Ajanlar** | Aklında bir hedef vardır ve ona adım adım ulaşmayı hesaplar. | Mevcut konumunuzdan varış noktanıza tam bir seyahat (uçuşlar, araç, otel) rezervasyonu yapar. |
| **Fayda Odaklı Ajanlar** | Sadece *bir* çözüm bulmaz — en *iyi* olanı, ödünleri tartarak bulur. | Maliyet ile rahatlık arasında denge kurarak tercihlerinize en yüksek puanı alan seyahati bulur. |
| **Öğrenen Ajanlar** | Geri bildirimlerden öğrenerek zaman içinde daha iyi olur. | Gezi sonrası anket sonuçlarına göre gelecekteki rezervasyon önerilerini ayarlar. |
| **Hiyerarşik Ajanlar** | Yüksek seviyeli ajan işleri alt görevlere ayırır ve alt ajanlara devreder. | "Seyahati iptal et" talebi: uçuş iptali, otel iptali, araç kiralama iptali alt ajanlar tarafından ayrı ayrı ele alınır. |
| **Çoklu Ajan Sistemleri (MAS)** | Birden çok bağımsız ajan birlikte (veya rekabet ederek) çalışır. | İş birliği: ayrı ajanlar otelleri, uçuşları ve eğlenceyi yönetir. Rekabet: birden çok ajan otel odalarını en iyi fiyatla doldurmak için yarışır. |

---

## Yapay Zeka Ajanlarını Ne Zaman Kullanmalı

Sadece *kullanabilirsiniz* diye her zaman *kullanmalısınız* anlamına gelmez. İşte ajanların gerçekten parladığı durumlar:

![Yapay Zeka Ajanları Ne Zaman Kullanılır?](../../../translated_images/tr/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Açık Uçlu Problemler** — Bir problemi çözmek için adımlar önceden programlanamaz. LLM'nin yolu dinamik olarak bulması gerekir.
- **Çok Adımlı Süreçler** — Tek bir arama veya üretim değil, birden fazla adımda araç kullanmayı gerektiren görevler.
- **Zamanla İyileşme** — Sistemin kullanıcı geri bildirimleri veya çevresel sinyallerle daha akıllı hale gelmesini istediğinizde.

Dersin ilerleyen bölümlerinde, **Güvenilir Yapay Zeka Ajanları İnşa Etmek** dersinde, yapay zeka ajanlarını ne zaman (ve ne zaman *kullanılmaması* gerektiğini) daha derinlemesine inceleyeceğiz.

---

## Ajanik Çözümlerin Temelleri

### Ajan Geliştirme

Bir ajan inşa ettiğinizde ilk yapacağınız şey, *neler yapabileceğini* tanımlamaktır — onun araçları, eylemleri ve davranışları.

Bu kursta, ana platform olarak **Microsoft Foundry Agent Servisi**ni kullanıyoruz. Destekler:

- OpenAI, Mistral, Meta (Llama) gibi sağlayıcılardan modeller
- Tripadvisor gibi sağlayıcılardan lisanslı veriler
- Standardize edilmiş OpenAPI 3.0 araç tanımları

### Ajanik Desenler

LLM'lerle iletişim kurarken istemler (prompt) kullanırsınız. Ajanlarda her istemi elle hazırlamanız her zaman mümkün olmaz — ajan birden fazla adımda harekete geçmelidir. İşte burada **Ajanik Desenler** devreye girer. Bunlar, LLM'leri daha ölçeklenebilir ve güvenilir biçimde yönlendirmek ve düzenlemek için yeniden kullanılabilir stratejilerdir.

Bu kurs en yaygın ve faydalı ajanik desenler etrafında yapılandırılmıştır.

### Ajanik Çerçeveler

Ajanik Çerçeveler, geliştiricilere ajanlar inşa etmek için hazır şablonlar, araçlar ve altyapı sağlar. Şunları kolaylaştırırlar:

- Araçları ve yetenekleri bağlamak
- Ajanın ne yaptığını gözlemlemek (ve yanlış gittiğinde hata ayıklamak)
- Birden fazla ajan arasında iş birliği yapmak

Bu kursta, üretime hazır ajanlar inşa etmek için **Microsoft Agent Framework (MAF)** üzerine odaklanıyoruz.

---

## Kod Örnekleri

Çalışırken görmek ister misiniz? İşte bu ders için kod örnekleri:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Sorularınız mı Var?

Diğer öğrenenlerle bağlantı kurmak, ofis saatlerine katılmak ve topluluktan Yapay Zeka Ajanı sorularınızı yanıtlatmak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)'a katılın.


---

## Bu Ajanı Hızlı Test Etme (İsteğe Bağlı)

[Ders 16’da](../16-deploying-scalable-agents/README.md) ajan dağıtmayı öğrendiğinizde, bu dersin `TravelAgent`'ı için hazır katalog [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) ile hızlı bir dağıtım sonrası sağlık kontrolü ekleyebilirsiniz. Nasıl çalıştırılacağını `tests/README.md` dosyasında görebilirsiniz.

---

## Önceki Ders

[Kurs Kurulumu](../00-course-setup/README.md)

## Sonraki Ders

[Ajanik Çerçeveleri Keşfetmek](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->