# Ajanik Protokollerin Kullanımı (MCP, A2A ve NLWeb)

[![Ajanik Protokoller](../../../translated_images/tr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Yukarıdaki görsele tıklayarak bu dersin videosunu izleyin)_

Yapay zeka ajanlarının kullanımı arttıkça, standartlaştırmayı, güvenliği ve açık inovasyonu destekleyen protokollere olan ihtiyaç da artıyor. Bu derste, bu ihtiyacı karşılamayı amaçlayan 3 protokolü ele alacağız - Model Bağlam Protokolü (MCP), Ajanlar Arası (A2A) ve Doğal Dil Web (NLWeb).

## Giriş

Bu derste ele alacağız:

• **MCP**'nin AI Ajanlarının kullanıcı görevlerini tamamlamak için harici araçlara ve verilere erişmesini nasıl sağladığını.

• **A2A**'nın farklı AI ajanları arasında iletişim ve işbirliğini nasıl mümkün kıldığını.

• **NLWeb**'in herhangi bir web sitesine doğal dil arayüzleri getirerek AI Ajanlarının içeriği keşfetmesini ve etkileşime girmesini nasıl sağladığını.

## Öğrenme Hedefleri

• **Belirleyin** MCP, A2A ve NLWeb'in AI ajanları bağlamındaki temel amacı ve faydalarını.

• **Açıklayın** her protokolün LLM'ler, araçlar ve diğer ajanlar arasındaki iletişim ve etkileşimi nasıl kolaylaştırdığını.

• **Tanıyın** her protokolün karmaşık ajan sistemleri inşa etmedeki ayrı rollerini.

## Model Bağlam Protokolü

**Model Bağlam Protokolü (MCP)**, uygulamaların LLM'lere bağlam ve araç sağlaması için standartlaştırılmış bir yol sunan açık bir standarttır. Bu, AI Ajanlarının tutarlı bir şekilde bağlanabileceği farklı veri kaynaklarına ve araçlara yönelik bir "evrensel adaptör"e olanak tanır.

MCP'nin bileşenlerine, doğrudan API kullanımına kıyasla avantajlarına ve AI ajanlarının bir MCP sunucusunu nasıl kullanabileceğine ilişkin bir örneğe bakalım.

### MCP Temel Bileşenleri

MCP, **istemci-sunucu mimarisi** üzerine çalışır ve temel bileşenleri şunlardır:

• **Host'lar** LLM uygulamalarıdır (örneğin VSCode gibi bir kod düzenleyicisi) ve MCP Sunucusuna bağlantıları başlatırlar.

• **İstemciler** host uygulama içindeki, sunucularla bire bir bağlantıları sürdüren bileşenlerdir.

• **Sunucular** belirli yetenekleri açığa çıkaran hafif programlardır.

Protokolde MCP Sunucusunun yetenekleri olan üç temel yapı taşı bulunur:

• **Araçlar**: Bunlar bir AI ajanının bir eylemi gerçekleştirmek için çağırabileceği ayrı eylemler veya fonksiyonlardır. Örneğin, bir hava durumu servisi "get weather" aracı sunabilir veya bir e-ticaret sunucusu "purchase product" aracı sunabilir. MCP sunucuları her aracın adını, açıklamasını ve giriş/çıkış şemasını yetenekler listesinde bildirir.

• **Kaynaklar**: Bunlar MCP sunucusunun sağlayabileceği salt okunur veri öğeleri veya belgeler olup istemciler bunları talep üzerine alabilir. Örnekler; dosya içerikleri, veri tabanı kayıtları veya günlük dosyalarıdır. Kaynaklar metin (kod veya JSON gibi) veya ikili (görseller veya PDF'ler gibi) olabilir.

• **İstemler**: Bunlar daha karmaşık iş akışlarına olanak tanıyan önerilen istemleri sağlayan ön tanımlı şablonlardır.

### MCP'nin Yararları

MCP, AI Ajanları için önemli avantajlar sunar:

• **Dinamik Araç Keşfi**: Ajanlar, bir sunucudan hangi araçların mevcut olduğunu ve ne yaptıklarına dair açıklamalarla birlikte dinamik olarak bir araç listesi alabilir. Bu, entegrasyonlar için genellikle statik kodlama gerektiren geleneksel API'lerle tezat oluşturur; yani herhangi bir API değişikliği kod güncellemelerini gerektirir. MCP, "bir kez entegre et" yaklaşımı sunar ve daha büyük bir uyum yeteneği sağlar.

• **LLM'ler Arası Birlikte Çalışabilirlik**: MCP farklı LLM'ler arasında çalışır, daha iyi performans değerlendirmesi için çekirdek modelleri değiştirme esnekliği sağlar.

• **Standartlaştırılmış Güvenlik**: MCP standart bir kimlik doğrulama yöntemi içerir, ek MCP sunucularına erişim eklerken ölçeklenebilirliği iyileştirir. Bu, çeşitli geleneksel API'ler için farklı anahtarları ve kimlik doğrulama türlerini yönetmekten daha basittir.

### MCP Örneği

![MCP Diyagramı](../../../translated_images/tr/mcp-diagram.e4ca1cbd551444a1.webp)

Bir kullanıcının MCP tarafından desteklenen bir AI asistanı kullanarak uçak bileti rezervasyonu yapmak istediğini hayal edin.

1. **Bağlantı**: AI asistanı (MCP istemcisi) bir havayolunun sağladığı MCP sunucusuna bağlanır.

2. **Araç Keşfi**: İstemci havayolunun MCP sunucusuna "Hangi araçlara sahipsiniz?" diye sorar. Sunucu "search flights" ve "book flights" gibi araçlarla yanıt verir.

3. **Araç Çağırma**: Ardından AI asistanına, "Lütfen Portland'dan Honolulu'ya bir uçuş ara" dersiniz. AI asistanı, LLM'ini kullanarak "search flights" aracını çağırması gerektiğini belirler ve ilgili parametreleri (kalkış yeri, varış yeri) MCP sunucusuna iletir.

4. **Yürütme ve Yanıt**: Bir sarmalayıcı olarak hareket eden MCP sunucusu, havayolunun dahili rezervasyon API'sine gerçek çağrıyı yapar. Ardından uçuş bilgilerini (ör. JSON verisi) alır ve AI asistanına geri gönderir.

5. **İleri Etkileşim**: AI asistanı uçuş seçeneklerini sunar. Bir uçuş seçtikten sonra, asistan rezervasyonu tamamlamak için aynı MCP sunucusunda "book flight" aracını çağırabilir.

## Ajanlar Arası Protokol (A2A)

MCP, LLM'leri araçlara bağlamaya odaklanırken, **Ajanlar Arası (A2A) protokolü** bir adım daha ileri giderek farklı AI ajanları arasında iletişim ve işbirliğini mümkün kılar. A2A, ortak bir görevi tamamlamak için farklı kuruluşlar, ortamlar ve teknoloji yığınları arasında AI ajanlarını birbirine bağlar.

A2A'nın bileşenlerini ve faydalarını ve seyahat uygulamamızda nasıl uygulanabileceğine dair bir örneği inceleyeceğiz.

### A2A Temel Bileşenleri

A2A, ajanlar arasında iletişimi etkinleştirmeye ve onların kullanıcıya ait bir alt görevi birlikte tamamlamasına odaklanır. Protokolün her bileşeni buna katkıda bulunur:

#### Ajan Kartı

Bir MCP sunucusunun araç listesini paylaşmasına benzer şekilde, bir Ajan Kartı şunlara sahiptir:
- Ajanın Adı.
- Tamamladığı görevlerin genel **açıklaması**.
- Diğer ajanların (ve hatta insan kullanıcıların) o ajanı ne zaman ve neden çağırmak isteyeceklerini anlamasına yardımcı olmak için açıklamalarla birlikte **belirli becerilerin bir listesi**.
- Ajanın **geçerli Uç Nokta URL'si**
- Ajanın **sürümü** ve **yetenekleri**, örneğin akışlı yanıtlar ve push bildirimleri.

#### Ajan Yürütücüsü

Ajan Yürütücüsü, **kullanıcı sohbetinin bağlamını uzak ajana aktarmaktan** sorumludur; uzak ajanın tamamlanması gereken görevi anlaması için buna ihtiyacı vardır. Bir A2A sunucusunda, bir ajan gelen istekleri ayrıştırmak ve kendi dahili araçlarını kullanarak görevleri yürütmek için kendi Büyük Dil Modeli'ni (LLM) kullanır.

#### Artefakt

Uzak bir ajan istenen görevi tamamladığında, çalışmasının ürünü bir artefakt olarak oluşturulur. Bir artefakt **ajanın çalışmasının sonucunu içerir**, **tamamlanan şeyin açıklamasını** ve protokol aracılığıyla gönderilen **metin bağlamını** içerir. Artefakt gönderildikten sonra uzak ajanla olan bağlantı, tekrar gerektiğinde kadar kapatılır.

#### Olay Kuyruğu

Bu bileşen **güncellemeleri işlemek ve mesaj iletmek** için kullanılır. Özellikle görev tamamlama süreleri daha uzun olabileceği durumlarda, ajanlar arasındaki bağlantının görev tamamlanmadan önce kapanmasını önlemek için üretimde ajanik sistemler için özellikle önemlidir.

### A2A'nın Faydaları

• **Gelişmiş İşbirliği**: Farklı satıcılar ve platformlardan gelen ajanların etkileşimde bulunmasına, bağlam paylaşmasına ve birlikte çalışmasına olanak tanır; geleneksel olarak ayrı sistemler arasında sorunsuz otomasyonu kolaylaştırır.

• **Model Seçimi Esnekliği**: Her A2A ajanı, isteklerini hizmet etmek için hangi LLM'i kullanacağına kendisi karar verebilir; bu, her ajan için optimize edilmiş veya ince ayarlı modellere izin verir, bazı MCP senaryolarındaki tek bir LLM bağlantısının aksine.

• **Yerleşik Kimlik Doğrulama**: Kimlik doğrulama doğrudan A2A protokolüne entegre edilmiştir ve ajan etkileşimleri için sağlam bir güvenlik çerçevesi sağlar.

### A2A Örneği

![A2A Diyagramı](../../../translated_images/tr/A2A-Diagram.8666928d648acc26.webp)

Seyahat rezervasyon senaryomuzu A2A kullanarak genişletelim.

1. **Kullanıcıdan Çok Ajanlı İsteğe**: Bir kullanıcı, muhtemelen bir "Seyahat Ajanı" A2A istemcisine/ajanına, "Lütfen gelecek hafta için Honolulu'ya tüm seyahati rezerve et, uçuşlar, bir otel ve kiralık araba dahil" diyerek etkileşimde bulunur.

2. **Seyahat Ajanı tarafından Orkestrasyon**: Seyahat Ajanı bu karmaşık isteği alır. LLM'ini kullanarak görevi mantıksallaştırır ve diğer uzman ajanlarla etkileşime geçmesi gerektiğini belirler.

3. **Ajanlar Arası İletişim**: Seyahat Ajanı ardından A2A protokolünü kullanarak farklı şirketler tarafından oluşturulmuş "Havayolu Ajanı", "Otel Ajanı" ve "Araç Kiralama Ajanı" gibi aşağı yönlü ajanlara bağlanır.

4. **Delegasyonlu Görev Yürütme**: Seyahat Ajanı bu uzman ajanlara belirli görevler gönderir (ör., "Honolulu'ya uçuş bul", "Bir otel rezerve et", "Bir araba kirala"). Bu uzman ajanların her biri kendi LLM'lerini çalıştırır ve kendi araçlarını (bunlar MCP sunucuları da olabilir) kullanarak rezervasyonun belirli kısmını yerine getirir.

5. **Konsolide Yanıt**: Tüm aşağı yönlü ajanlar görevlerini tamamladıktan sonra, Seyahat Ajanı sonuçları (uçuş ayrıntıları, otel onayı, araç kiralama rezervasyonu) derler ve kullanıcıya sohbet tarzında kapsamlı bir yanıt gönderir.

## Doğal Dil Web (NLWeb)

Web siteleri uzun süredir kullanıcıların internette bilgi ve verilere erişmesinin birincil yolu olmuştur.

NLWeb'in farklı bileşenlerine, NLWeb'in faydalarına ve seyahat uygulamamıza bakarak NLWeb'in nasıl çalıştığına bir örneğe bakalım.

### NLWeb'in Bileşenleri

- **NLWeb Uygulaması (Core Service Code)**: Doğal dil sorularını işleyen sistem. Yanıtlar oluşturmak için platformun farklı parçalarını birbirine bağlar. Bunu bir web sitesinin doğal dil özelliklerini güçlendiren **motoru** olarak düşünebilirsiniz.

- **NLWeb Protokolü**: Bu, bir web sitesiyle doğal dil etkileşimi için **temel kurallar dizisidir**. Yanıtları JSON formatında (çoğunlukla Schema.org kullanarak) geri gönderir. Amacı, HTML'in çevrimiçi belgeleri paylaşılabilir kıldığı şekilde "AI Web" için basit bir temel oluşturmaktır.

- **MCP Server (Model Context Protocol Endpoint)**: Her NLWeb kurulumu aynı zamanda bir **MCP sunucusu** olarak da çalışır. Bu, diğer AI sistemleriyle **"ask" metodu gibi araçları ve verileri paylaşabileceği** anlamına gelir. Pratikte, bu web sitesinin içeriğinin ve yeteneklerinin AI ajanları tarafından kullanılmasını sağlar ve sitenin daha geniş "ajan ekosistemi"nin bir parçası olmasına izin verir.

- **Embedding Modelleri**: Bu modeller web sitesi içeriğini vektör adı verilen sayısal temsillere (embeddings) **dönüştürmek için** kullanılır. Bu vektörler bilgisayarların karşılaştırıp arama yapabileceği şekilde anlamı yakalar. Özel bir veritabanında saklanırlar ve kullanıcılar hangi embedding modelini kullanmak istediklerini seçebilir.

- **Vektör Veritabanı (Getirme Mekanizması)**: Bu veritabanı web sitesi içeriğinin **embeddings'lerini saklar**. Birisi soru sorduğunda, NLWeb en alakalı bilgiyi hızlıca bulmak için vektör veritabanını kontrol eder. Benzerliğe göre sıralanmış olası cevapların hızlı bir listesini sunar. NLWeb, Qdrant, Snowflake, Milvus, Azure AI Search ve Elasticsearch gibi farklı vektör depolama sistemleriyle çalışır.

### NLWeb Örneği

![NLWeb](../../../translated_images/tr/nlweb-diagram.c1e2390b310e5fe4.webp)

Seyahat rezervasyon web sitemizi tekrar düşünün, ancak bu sefer NLWeb tarafından destekleniyor.

1. **Veri Alımı**: Seyahat sitesinin mevcut ürün katalogları (ör. uçuş listeleri, otel açıklamaları, tur paketleri) Schema.org kullanılarak biçimlendirilir veya RSS beslemeleri aracılığıyla yüklenir. NLWeb'in araçları bu yapılandırılmış verileri alır, embedding'ler oluşturur ve bunları yerel veya uzak bir vektör veritabanında depolar.

2. **Doğal Dil Sorgusu (İnsan)**: Bir kullanıcı siteyi ziyaret eder ve menülerde gezinmek yerine sohbet arayüzüne: "Gelecek hafta için Honolulu'da havuzu olan aile dostu bir otel bul" yazabilir.

3. **NLWeb İşleme**: NLWeb uygulaması bu sorguyu alır. Sorguyu anlamak için bir LLM'e gönderir ve aynı zamanda ilgili otel listelerini bulmak için vektör veritabanını arar.

4. **Doğru Sonuçlar**: LLM, veritabanından gelen arama sonuçlarını yorumlamaya, "aile dostu", "havuz" ve "Honolulu" kriterlerine göre en iyi eşleşmeleri belirlemeye yardımcı olur ve ardından doğal dilde bir yanıt formatlar. Kritik olarak, yanıt web sitesinin katalogundaki gerçek otellere atıfta bulunur ve uydurma bilgilerden kaçınır.

5. **AI Ajan Etkileşimi**: NLWeb bir MCP sunucusu olarak hizmet verdiği için, harici bir AI seyahat ajanı da bu web sitesinin NLWeb örneğine bağlanabilir. AI ajanı daha sonra siteyi doğrudan sorgulamak için `ask` MCP yöntemini kullanabilir: `ask("Honolulu bölgesinde otelin önerdiği vegan-dostu restoranlar var mı?")`. NLWeb örneği bunu işler, restoran bilgileri veritabanını (yüklendiyse) kullanır ve yapılandırılmış bir JSON yanıtı döner.

### MCP/A2A/NLWeb hakkında daha fazla sorunuz mu var?

Diğer öğrenenlerle buluşmak, ofis saatlerine katılmak ve AI Ajanlarınızla ilgili sorularınızı yanıtlatmak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) katılın.

## Kaynaklar

- [MCP Başlangıç](https://aka.ms/mcp-for-beginners)  
- [MCP Belgeleri](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Deposu](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Feragatname:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstermemize rağmen, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki metni yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->