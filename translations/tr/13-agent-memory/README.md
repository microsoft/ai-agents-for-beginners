# AI Ajanları için Bellek
[![Agent Memory](../../../translated_images/tr/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

AI Ajanları oluşturmanın benzersiz faydaları tartışılırken, çoğunlukla iki şey ele alınır: görevleri tamamlamak için araç çağırabilme yeteneği ve zamanla gelişebilme yeteneği. Bellek, kullanıcılarımıza daha iyi deneyimler sunabilen kendini geliştiren ajanlar oluşturmanın temelidir.

Bu derste, AI Ajanlar için bellek nedir, nasıl yönetilir ve uygulamalarımızın faydası için nasıl kullanılır gibi konuları inceleyeceğiz.

## Giriş

Bu ders şunları içerecektir:

• **AI Ajan Belleğini Anlamak**: Belleğin ne olduğu ve ajanlar için neden önemli olduğu.

• **Bellek Uygulama ve Depolama**: AI ajanlarınıza bellek yetenekleri eklemek için pratik yöntemler; kısa ve uzun süreli bellek odaklı.

• **AI Ajanlarının Kendini Geliştirmesi**: Belleğin, ajanların geçmiş etkileşimlerden öğrenmesini ve zamanla gelişmesini nasıl sağladığı.

## Mevcut Uygulamalar

Bu ders iki kapsamlı not defteri eğitimini içerir:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Microsoft Agent Framework ile Mem0 ve Azure AI Search kullanarak belleği uygular

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Cognee kullanarak yapılandırılmış bellek uygular, gömülerle desteklenen bilgi grafiği otomatik olarak oluşturur, grafiği görselleştirir ve akıllı veri alma yapar

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bileceksiniz:

• **AI ajan bellek tipleri arasında ayrım yapabilme**, çalışma, kısa süreli ve uzun süreli belleklerin yanı sıra persona ve epizodik bellek gibi özel türler de dahil.

• **Microsoft Agent Framework kullanarak kısa ve uzun süreli belleği uygulama ve yönetme**, Mem0, Cognee, Whiteboard belleği gibi araçları kullanma ve Azure AI Search ile entegrasyon.

• **Kendini geliştiren AI ajanlarının prensiplerini anlama** ve sağlam bellek yönetim sistemlerinin sürekli öğrenme ve uyuma nasıl katkı sağladığını kavrama.

## AI Ajan Belleğini Anlamak

Temelde, **AI ajanları için bellek, bilgiyi saklamalarını ve hatırlamalarını sağlayan mekanizmalar anlamına gelir**. Bu bilgi, bir konuşma hakkındaki özel detaylar, kullanıcı tercihleri, geçmiş eylemler ya da öğrenilen kalıplar olabilir.

Bellek olmadan, AI uygulamaları genellikle durum bilgisi olmayan (state-less) olur, yani her etkileşim sıfırdan başlar. Bu durum, ajanın önceki bağlamı veya tercihleri "unutması" ile tekrarlayan ve kullanıcı için sinir bozucu deneyime yol açar.

### Bellek Neden Önemlidir?

Bir ajanın zekası, büyük ölçüde geçmiş bilgileri hatırlama ve kullanma becerisiyle bağlantılıdır. Bellek, ajanların:

• **Yansıtıcı** olmalarını sağlar: Geçmiş eylemlerden ve sonuçlardan öğrenme.

• **Etkileşimli** olmalarını sağlar: Devam eden bir konuşma boyunca bağlamı koruma.

• **Proaktif ve Reaktif** olmalarını sağlar: İhtiyaçları önceden tahmin etme veya tarihsel verilere dayanarak uygun tepki verme.

• **Özerk** olmalarını sağlar: Depolanmış bilgiden çekerek daha bağımsız hareket etme.

Bellek uygulamanın amacı, ajanları daha **güvenilir ve yetenekli** hale getirmektir.

### Bellek Türleri

#### Çalışma Belleği

Bunu, bir ajan tarafından tek bir devam eden görev veya düşünce süreci boyunca kullanılan bir taslak kağıdı gibi düşünebilirsiniz. Bir sonraki adımı hesaplamak için gereken anlık bilgiyi tutar.

AI ajanları için çalışma belleği genellikle bir konuşmanın en alakalı bilgilerini yakalar, sohbet geçmişi uzun veya kısaltılmış olsa bile. Gereksinimler, teklifler, kararlar ve eylemler gibi anahtar öğeleri çıkarma üzerine odaklanır.

**Çalışma Belleği Örneği**

Bir seyahat rezervasyon ajanında, çalışma belleği kullanıcının mevcut isteğini yakalayabilir, örneğin "Paris'e bir gezi rezervasyonu yapmak istiyorum". Bu özel gereksinim, mevcut etkileşimi yönlendirmek için ajanın anlık bağlamında tutulur.

#### Kısa Süreli Bellek

Bu bellek türü, tek bir konuşma veya oturum süresince bilgiyi tutar. Şu anki sohbetin bağlamıdır ve ajanın diyaloğun önceki turlarına atıfta bulunmasını sağlar.

[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK örneklerinde bu, `AgentSession` ile eşleşir, `agent.create_session()` ile oluşturulur. Oturum, frameworkün yerleşik kısa süreli belleğidir: aynı oturum kullanıldığı sürece konuşma bağlamı erişilebilir tutulur, ancak oturum sona erdiğinde veya uygulama yeniden başlatıldığında bu bağlam kalıcı olmaz. Oturumlar arasında yaşamaları gereken gerçekler ve tercihler için genellikle bir veritabanı, vektör indeksi veya başka kalıcı bir depolama ile uzun süreli bellek kullanın.

**Kısa Süreli Bellek Örneği**

Bir kullanıcı, "Paris'e uçak bileti ne kadar tutar?" diye sorarsa ve ardından "Orada konaklama nasıl?" diye devam ederse, kısa süreli bellek ajanın aynı konuşma içinde "orada" nın "Paris" anlamına geldiğini bilmesini sağlar.

#### Uzun Süreli Bellek

Birden çok konuşma veya oturum boyunca kalan bilgidir. Ajanların kullanıcı tercihlerini, geçmiş etkileşimleri veya genel bilgileri uzun süre hatırlamasını sağlar. Bu kişiselleştirme için önemlidir.

**Uzun Süreli Bellek Örneği**

Uzun süreli bellek, "Ben kayak ve açık hava aktivitelerini sever, dağ manzaralı kahveyi tercih eder ve geçmişteki bir yaralanma nedeniyle ileri kayak pistlerinden kaçınır" bilgisini saklayabilir. Bu önceki etkileşimlerden öğrenilmiş bilgi, gelecekteki seyahat planlama oturumlarındaki önerileri son derece kişiselleştirir.

#### Persona Belleği

Bu özelleşmiş bellek türü, bir ajanın tutarlı bir "kişilik" veya "persona" geliştirmesine yardımcı olur. Ajanın kendisi veya amacı hakkında detayları hatırlamasını sağlayarak, etkileşimleri daha akıcı ve odaklı hale getirir.

**Persona Belleği Örneği**
Seyahat ajanı "uzman kayak planlayıcısı" olarak tasarlanmışsa, persona belleği bu rolü pekiştirir ve yanıtlarını bir uzman ton ve bilgi seviyesine uygun hale getirir.

#### İş Akışı/Epizodik Bellek

Bu bellek, bir ajanın karmaşık bir görev sırasında attığı adımların sırasını, başarılarını ve başarısızlıklarını saklar. Geçmiş deneyimler veya "epizodları" hatırlamak ve bunlardan öğrenmek gibidir.

**Epizodik Bellek Örneği**

Ajan belirli bir uçuşu rezerve etmeye çalıştı ancak müsaitlik olmadığı için başarısız olduysa, epizodik bellek bu hatayı kaydedebilir ve ajan sonraki denemede alternatif uçuşları deneyebilir ya da kullanıcıyı daha bilgili şekilde bilgilendirebilir.

#### Varlık Belleği

Konuşmalardan belirli varlıklar (kişi, yer veya nesne gibi) ve olaylar çıkarma ve hatırlamayı içerir. Ajanın tartışılan önemli öğeler hakkında yapılandırılmış bir anlayış geliştirmesini sağlar.

**Varlık Belleği Örneği**

Geçmiş bir seyahat hakkındaki konuşmadan ajanın "Paris", "Eyfel Kulesi" ve "Le Chat Noir restoranında akşam yemeği" gibi varlıkları çıkarması mümkündür. Gelecekteki bir etkileşimde ajan "Le Chat Noir"u hatırlayarak orada yeni bir rezervasyon yapmayı teklif edebilir.

#### Yapılandırılmış RAG (Retrieval Augmented Generation)

RAG daha geniş bir tekniktir, ancak "Yapılandırılmış RAG" güçlü bir bellek teknolojisi olarak öne çıkar. Konuşma, e-posta, resim gibi çeşitli kaynaklardan yoğun, yapılandırılmış bilgiyi çıkarır ve yanıtların doğruluğunu, hatırlanmasını ve hızını artırmak için kullanır. Klasik RAG'ın sadece anlamsal benzerliğe dayanmasının aksine, Yapılandırılmış RAG bilgilerin doğal yapısıyla çalışır.

**Yapılandırılmış RAG Örneği**

Anahtar kelime eşleştirmek yerine, Yapılandırılmış RAG bir e-posta içinden uçuş detaylarını (varış yeri, tarih, saat, havayolu) ayrıştırabilir ve yapılandırılmış şekilde depolayabilir. Böylece "Salı günü Paris'e hangi uçuşu ayırttım?" gibi kesin sorgular yapılabilir.

## Belleği Uygulama ve Depolama

AI ajanları için bellek uygulamak, bilgi üretme, depolama, alma, bütünleştirme, güncelleme ve hatta "unutma" (veya silme) süreçlerini içeren sistematik bir **bellek yönetimi** sürecidir. Veri alma aşaması özellikle kritik bir unsurdur.

### Özelleşmiş Bellek Araçları

#### Mem0

Ajan belleğini saklamanın ve yönetmenin bir yolu, Mem0 gibi özel araçlar kullanmaktır. Mem0, ajanların ilgili etkileşimleri hatırlamasına, kullanıcı tercihleri ve gerçekçi bağlamları depolamasına, başarı ve başarısızlıklardan zamanla öğrenmesine olanak tanıyan kalıcı bir bellek katmanı olarak çalışır. Amaç, durum bilgisiz ajanların durum bilgili hale gelmesidir.

Bu, **iki aşamalı bir bellek iş akışı: çıkarma ve güncelleme** yoluyla işler. Önce, bir ajan sohbetine eklenen mesajlar Mem0 servisine gönderilir, burada Büyük Dil Modeli (LLM) konuşma geçmişini özetler ve yeni bellekleri çıkarır. Ardından LLM destekli güncelleme aşaması, bu bellekleri ekleyip değiştirme veya silme kararını verir, ve bunlar vektör, grafik ve anahtar-değer veritabanlarını içerebilen karma bir veri deposuna kaydedilir. Bu sistem farklı bellek türlerini destekler ve varlıklar arasındaki ilişkileri yönetmek için grafik belleği ekleyebilir.

#### Cognee

Diğer güçlü yaklaşım, yapılandırılmış ve yapılandırılmamış verileri gömülerle desteklenen sorgulanabilir bilgi grafiğine dönüştüren açık kaynak kodlu semantik bellek olan **Cognee** kullanmaktır. Cognee, vektörel benzerlik araması ile grafik ilişkilerini birleştiren **çift deposu mimarisine** sahiptir, böylece ajanlar sadece hangi bilgilerin benzer olduğunu değil, kavramların birbirleriyle nasıl ilişkili olduğunu da anlar.

Vektör benzerliği, grafik yapısı ve LLM mantığını harmanlayan **karma veri alma** konusunda üstündür - ham parça aramasından grafik-bilinçli soru yanıta kadar. Sistem, kısa süreli oturum bağlamı ve uzun süreli kalıcı belleği destekleyerek, bağlantılı tek bir grafik olarak sorgulanabilir şekilde gelişen ve büyüyen **yaşayan bellek** tutar.

Cognee not defteri eğitimi ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)), çeşitli veri kaynaklarını alma, bilgi grafiğini görselleştirme ve farklı arama stratejileriyle sorgulama örneklerini içeren bu birleşik bellek katmanını oluşturmayı gösterir.

### Belleği RAG ile Depolama

Mem0 gibi özel bellek araçlarının ötesinde, özellikle yapılandırılmış RAG için, bellekleri depolamak ve almak için sağlam arama hizmetleri olarak **Azure AI Search** kullanılabilir.

Bu, ajanınızın yanıtlarını kendi verilerinizle güçlendirmenizi sağlar ve daha alakalı ve doğru cevaplar sunar. Azure AI Search, kullanıcıya özgü seyahat anılarını, ürün kataloglarını veya herhangi bir başka alana özgü bilgileri depolamak için kullanılabilir.

Azure AI Search, konuşma geçmişleri, e-postalar veya hatta görüntüler gibi büyük veri kümelerinden yoğun, yapılandırılmış bilgileri çıkarmada ve almadaki üstün özellikleriyle **Yapılandırılmış RAG**'yi destekler. Bu, geleneksel metin parçalayıcı ve gömme yaklaşımlarına kıyasla "insanüstü hassasiyet ve hatırlama" sağlar.

## AI Ajanlarının Kendini Geliştirmesini Sağlama

Kendini geliştiren ajanlar için yaygın bir model, ayrı bir **"bilgi ajanı"** kullanmaktır. Bu ajan, kullanıcı ile birincil ajan arasındaki ana konuşmayı gözlemler. Rolü:

1. **Değerli bilgiyi belirlemek**: Konuşmanın herhangi bir bölümünün genel bilgi veya özel kullanıcı tercihi olarak kaydedilmeye değer olup olmadığını anlamak.

2. **Çıkarma ve özetleme**: Konuşmadan temel öğrenmeyi veya tercihi özlü şekilde çıkarmak.

3. **Bilgi tabanına kaydetme**: Çıkarılan bu bilgiyi, genellikle bir vektör veritabanında kalıcı hale getirmek ve daha sonra erişilebilir kılmak.

4. **Gelecekteki sorguları zenginleştirme**: Kullanıcı yeni bir sorgu başlattığında, bilgi ajanı ilgili kaydedilmiş bilgileri alır ve kullanıcının promptuna ekler, birincil ajan için kritik bağlam sağlar (RAG benzeri).

### Bellek için Optimizasyonlar

• **Gecikme Yönetimi**: Kullanıcı etkileşimlerini yavaşlatmamak için, önce daha ucuz ve hızlı bir model kullanılarak bilginin kaydedilmeye ya da alınmaya değer olup olmadığı hızlıca kontrol edilir, yalnızca gerektiğinde daha karmaşık çıkarma/geri alma süreçleri devreye sokulur.

• **Bilgi Tabanı Bakımı**: Büyüyen bir bilgi tabanı için daha az kullanılan bilgiler maliyeti yönetmek adına "soğuk depolamaya" taşınabilir.

## Ajan Belleği Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanlar ile ilgili sorularınızı cevaplamak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) topluluğuna katılın.
## Önceki Ders

[AI Ajanlar için Bağlam Mühendisliği](../12-context-engineering/README.md)

## Sonraki Ders

[Microsoft Agent Framework'ü Keşfetmek](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->