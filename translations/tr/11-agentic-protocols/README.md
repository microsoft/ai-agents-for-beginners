# Agentik Protokollerin Kullanımı (MCP, A2A ve NLWeb)

[![Agentik Protokoller](../../../translated_images/tr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Bu derse ait videoyu izlemek için yukarıdaki resme tıklayın)_

AI ajanlarının kullanımı arttıkça, standartlaştırmayı, güvenliği sağlayan ve açık inovasyonu destekleyen protokollere olan ihtiyaç da artmaktadır. Bu derste, bu ihtiyacı karşılamaya yönelik 3 protokolü ele alacağız - Model Context Protocol (MCP), Agent to Agent (A2A) ve Natural Language Web (NLWeb).

## Giriş

Bu derste aşağıdakileri öğreneceğiz:

• **MCP'nin** AI Ajanlarının kullanıcı görevlerini tamamlamak için dış araçlar ve verilere erişimini nasıl sağladığını.

• **A2A'nın** farklı AI ajanları arasında iletişim ve iş birliği olanağı nasıl sunulduğunu.

• **NLWeb'in** herhangi bir web sitesine doğal dil arayüzleri getirerek AI Ajanlarının içeriği keşfetmesini ve etkileşimde bulunmasını nasıl sağladığını.

## Öğrenme Hedefleri

• AI ajanları bağlamında MCP, A2A ve NLWeb'in temel amacını ve faydalarını **belirlemek**.

• Her protokolün LLM'ler, araçlar ve diğer ajanlar arasındaki iletişim ve etkileşimi nasıl kolaylaştırdığını **açıklamak**.

• Karmaşık ajan sistemleri oluşturmadaki her protokolün farklı rollerini **tanımak**.

## Model Context Protocol

**Model Context Protocol (MCP)**, uygulamaların LLM'lere bağlam ve araçlar sağlaması için standart bir yol sunan açık bir standarttır. Bu, AI Ajanlarının farklı veri kaynakları ve araçlara tutarlı şekilde bağlanmasını sağlayan bir "evrensel adaptör" işlevi görür.

MCP'nin bileşenlerine, doğrudan API kullanımına kıyasla avantajlarına ve AI ajanlarının bir MCP sunucusunu nasıl kullanabileceğine bakalım.

### MCP Temel Bileşenleri

MCP, **istemci-sunucu mimarisi** üzerine kurulu olup temel bileşenleri şunlardır:

• **Ev Sahipleri (Hosts)**, bir MCP sunucusuna bağlantı başlatan LLM uygulamalarıdır (örneğin, VSCode gibi bir kod editörü).

• **İstemciler (Clients)**, ev sahibi uygulama içinde sunucularla bire bir bağlantı sürdüren bileşenlerdir.

• **Sunucular (Servers)**, belirli yetenekleri sunan hafif programlardır.

Protokolde MCP Sunucusunun yetenekleri olan üç temel primitif vardır:

• **Araçlar (Tools)**: AI ajanın çağırarak işlem yapabileceği ayrı eylemler veya fonksiyonlardır. Örneğin, bir hava durumu servisi "hava durumu al" aracı sunabilir veya bir e-ticaret sunucusu "ürün satın al" aracını sunabilir. MCP sunucuları, her aracın adını, açıklamasını ve giriş/çıkış şemasını yetenek listelerinde bildirir.

• **Kaynaklar (Resources)**: MCP sunucusunun sağlayabileceği salt okunur veri öğeleri veya dokümanlardır ve istemciler bunları talep üzerine alabilir. Örnekler arasında dosya içeriği, veritabanı kayıtları veya günlük dosyaları bulunur. Kaynaklar metin (kod veya JSON gibi) ya da ikili (görüntü veya PDF gibi) olabilir.

• **İstemde Bulunanlar (Prompts)**: Önerilen istemleri sağlayan önceden tanımlanmış şablonlardır ve daha karmaşık iş akışlarına olanak tanır.

### MCP'nin Faydaları

MCP, AI Ajanları için önemli avantajlar sunar:

• **Dinamik Araç Keşfi**: Ajanlar, sunucudan mevcut araçların listesini ve ne yaptıklarına dair açıklamaları dinamik olarak alabilir. Bu, genellikle entegrasyonlar için statik kodlama gerektiren geleneksel API'lere kıyasla farklıdır; API değişiklikleri kod güncellemeleri ister. MCP, "bir kez entegre et" yaklaşımıyla daha yüksek uyum sağlar.

• **LLM'ler Arası Birlikte Çalışabilirlik**: MCP, farklı LLM'ler arasında çalışır ve daha iyi performans için temel modelleri değiştirme esnekliği sunar.

• **Standartlaştırılmış Güvenlik**: MCP, standart bir kimlik doğrulama yöntemi içerir, bu da ek MCP sunucularına erişim eklerken ölçeklenebilirliği artırır. Bu, çeşitli geleneksel API'ler için farklı anahtarlar ve kimlik doğrulama türleri yönetmekten daha basittir.

### MCP Örneği

![MCP Diagram](../../../translated_images/tr/mcp-diagram.e4ca1cbd551444a1.webp)

Bir kullanıcının MCP destekli bir AI asistanıyla uçuş rezervasyonu yapmak istediğini hayal edin.

1. **Bağlantı**: AI asistanı (MCP istemcisi), bir havayolu tarafından sağlanan MCP sunucusuna bağlanır.

2. **Araç Keşfi**: İstemci havayolunun MCP sunucusuna "Hangi araçlara sahipsiniz?" diye sorar. Sunucu "uçuş ara" ve "uçuş rezervasyonu" gibi araçları listeler.

3. **Araç Çağrısı**: Ardından kullanıcı AI asistanına "Portland'dan Honolulu'ya uçuş ara" der. AI asistanı, LLM'siyle "uçuş ara" aracını çağırması gerektiğini belirler ve ilgili parametreleri (kalkış, varış) MCP sunucusuna iletir.

4. **İcra ve Yanıt**: MCP sunucusu, bir sarmalayıcı (wrapper) olarak havayolunun dahili rezervasyon API'sini çağırır. Gelen uçuş bilgilerini (örneğin JSON verisi) alır ve AI asistanına geri gönderir.

5. **İleri Etkileşim**: AI asistanı uçuş seçeneklerini sunar. Kullanıcı bir uçuş seçtikten sonra, asistan aynı MCP sunucusunda "uçuş rezervasyonu" aracını çağırarak rezervasyonu tamamlar.

## Ajanlar Arası Protokol (A2A)

MCP, LLM'leri araçlara bağlamaya odaklanırken, **Ajanlar Arası (A2A) protokolü** bir adım daha ileri giderek farklı AI ajanları arasında iletişim ve iş birliği sağlar. A2A, farklı organizasyonlar, ortamlar ve teknoloji yığınları arasında AI ajanlarını ortak bir görevi tamamlamak için bağlar.

A2A'nın bileşenlerini ve faydalarını inceleyeceğiz ve seyahat uygulamamızda nasıl uygulanabileceğine dair bir örnek göreceğiz.

### A2A Temel Bileşenleri

A2A, ajanların iletişim kurmasını ve kullanıcı alt görevini tamamlamak için birlikte çalışmasını sağlar. Protokolün her bileşeni buna katkı sağlar:

#### Ajan Kartı

MCP sunucusunun araç listesini paylaşmasına benzer şekilde, Ajan Kartı şunlara sahiptir:
- Ajanın Adı.
- Tamamladığı genel görevlerin **açıklaması**.
- Diğer ajanların (veya insan kullanıcıların) ne zaman ve neden bu ajanı çağırmak isteyeceklerini anlamalarına yardımcı olacak **özgül yeteneklerin listesi** ve açıklamaları.
- Ajanın **şimdiki Uç Nokta URL'si**.
- Ajanın **sürümü** ve akış yanıtları ile anlık bildirimler gibi **yetenekleri**.

#### Ajan Yürütücüsü

Ajan Yürütücüsü, **kullanıcı sohbet bağlamını uzak ajana iletmekten** sorumludur; uzak ajan, tamamlanacak görevi anlamak için buna ihtiyaç duyar. Bir A2A sunucusunda, ajan gelen istekleri anlamak ve dahili araçlarıyla görevleri yerine getirmek için kendi Büyük Dil Modelini (LLM) kullanır.

#### Eser (Artifact)

Uzak ajan istenen görevi tamamladıktan sonra, çalışma ürünü bir eser olarak oluşturulur. Eser **ajan çalışmasının sonucunu**, **tamamlanan işin açıklamasını** ve protokol yoluyla gönderilen **metin bağlamını** içerir. Eser gönderildikten sonra uzak ajanla bağlantı, tekrar gerekene kadar kapatılır.

#### Olay Kuyruğu

Bu bileşen, **güncellemeleri yönetmek ve mesajları iletmek** için kullanılır. Özellikle üretimde, ajanlar arasındaki bağlantının görev tamamlanmadan kapanmasını önlemek için çok önemlidir; çünkü görevin tamamlanması uzun sürebilir.

### A2A'nın Faydaları

• **Gelişmiş İş Birliği**: Farklı satıcı ve platformlardan ajanların etkileşime geçmesini, bağlam paylaşmasını ve birlikte çalışmasını sağlar; geleneksel olarak ayrık sistemler arasında sorunsuz otomasyon kolaylaştırır.

• **Model Seçimi Esnekliği**: Her A2A ajanı isteklerini hangi LLM ile karşılayacağına karar verebilir, böylece MCP’nin bazı durumlarındaki tek LLM bağlantısına kıyasla her ajan için optimize edilmiş veya ince ayar yapılmış modeller kullanılabilir.

• **Yerleşik Kimlik Doğrulama**: Kimlik doğrulama doğrudan A2A protokolüne entegre edilmiştir ve ajanlar arasındaki etkileşimlerde güçlü bir güvenlik altyapısı sağlar.

### A2A Örneği

![A2A Diagram](../../../translated_images/tr/A2A-Diagram.8666928d648acc26.webp)

Seyahat rezervasyonu senaryomuzu genişletelim, ancak bu sefer A2A kullanarak.

1. **Kullanıcı Çok Ajanlı İstem**: Bir kullanıcı "Gelecek hafta için Honolulu'ya uçuş, otel ve araç kiralama dahil tüm seyahati rezerve et" diyerek "Seyahat Ajanı" A2A istemcisi/ajani ile etkileşimde bulunur.

2. **Seyahat Ajanı Orkestrasyonu**: Seyahat Ajanı bu karmaşık isteği alır. Görevi anlamak için LLM'sini kullanır ve diğer uzmanlaşmış ajanlarla etkileşime geçmesi gerektiğine karar verir.

3. **Ajanlar Arası İletişim**: Seyahat Ajanı sonra A2A protokolünü kullanarak, farklı şirketler tarafından oluşturulmuş "Havayolu Ajanı", "Otel Ajanı" ve "Araç Kiralama Ajanı" gibi alt ajanlara bağlanır.

4. **Delege Edilen Görev İcraatı**: Seyahat Ajanı bu uzmanlaşmış ajanlara belirli görevler (örneğin "Honolulu uçuşlarını bul", "Otel rezerve et", "Araç kirala") gönderir. Bu uzman ajanlar, kendi LLM'lerini çalıştırır ve kendi araçlarını (kendileri de MCP sunucuları olabilir) kullanarak rezervasyonun kendi bölümlerini tamamlar.

5. **Konsolide Yanıt**: Tüm alt ajanlar görevlerini tamamladıktan sonra Seyahat Ajanı sonuçları (uçuş ayrıntıları, otel onayı, araç kiralama rezervasyonu) derler ve kullanıcıya kapsamlı, sohbet tarzında yanıt gönderir.

## Doğal Dil Web (NLWeb)

Web siteleri, uzun süredir kullanıcıların internet üzerinden bilgi ve verilere erişiminin temel yolu olmuştur.

NLWeb'in farklı bileşenlerini, NLWeb'in faydalarını ve seyahat uygulamamıza bakarak NLWeb'in nasıl çalıştığını görelim.

### NLWeb Bileşenleri

- **NLWeb Uygulaması (Temel Hizmet Kodu)**: Doğal dil sorularını işleyen sistemdir. Platformun farklı parçalarını yanıtlar oluşturmak için bağlar. Bir web sitesinin doğal dil özelliklerini çalıştıran **motor** olarak düşünebilirsiniz.

- **NLWeb Protokolü**: Bir web sitesiyle doğal dil etkileşimi için **temel kurallar seti**dir. Yanıtları JSON formatında (çoğunlukla Schema.org kullanarak) gönderir. Amacı, HTML'nin belge paylaşımını mümkün kıldığı gibi, “Yapay Zeka Webi” için basit bir temel oluşturmaktır.

- **MCP Sunucusu (Model Context Protocol Uç Noktası)**: Her NLWeb yapılandırması aynı zamanda bir **MCP sunucusu** olarak da çalışır. Bu, başka AI sistemleriyle **araçlar (örneğin bir “sorma” metodu) ve veri paylaşımı** yapabileceği anlamına gelir. Pratikte, web sitesinin içeriği ve yetenekleri AI ajanlarınca kullanılabilir hale gelir ve site daha geniş “ajan ekosistemi”nin parçası olur.

- **Embedding Modelleri**: Bunlar, web sitesi içeriğini **vektör adı verilen sayısal temsillere dönüştürmek** için kullanılır. Bu vektörler, anlamı bilgisayarların karşılaştırıp arayabileceği şekilde yakalar. Özel bir veritabanında saklanır ve kullanıcılar kullanılacak embedding modelini seçebilir.

- **Vektör Veritabanı (Erişim Mekanizması)**: Bu veritabanı, **web sitesi içeriğinin embeddinglerini saklar**. Bir soru sorulduğunda, NLWeb vektör veritabanına bakarak en ilgili bilgileri hızlıca bulur. Benzerlik sırasına göre derecelendirilmiş olası yanıtların hızlı listesini sağlar. NLWeb; Qdrant, Snowflake, Milvus, Azure AI Search ve Elasticsearch gibi farklı vektör depolama sistemleriyle çalışır.

### NLWeb Örnek

![NLWeb](../../../translated_images/tr/nlweb-diagram.c1e2390b310e5fe4.webp)

Seyahat rezervasyon web sitemize tekrar bakalım; bu sefer NLWeb destekli.

1. **Veri Alımı**: Seyahat sitesinin mevcut ürün katalogları (ör. uçuş listeleri, otel tanımları, tur paketleri) Schema.org kullanılarak formatlanır veya RSS beslemeleriyle yüklenir. NLWeb'in araçları bu yapılandırılmış verileri alır, embedding'ler oluşturur ve bunları yerel veya uzak bir vektör veritabanında saklar.

2. **Doğal Dil Sorgusu (İnsan)**: Bir kullanıcı siteyi ziyaret eder ve menülere tıklamak yerine sohbet arayüzüne yazar: "Gelecek hafta için havuzlu, aile dostu bir otel bul Honolulu'da."

3. **NLWeb İşleme**: NLWeb uygulaması bu sorguyu alır. Sorguyu anlamak için LLM'ye gönderir ve eşzamanlı olarak vektör veritabanında ilgili otel kayıtlarını arar.

4. **Doğru Sonuçlar**: LLM, veritabanından gelen arama sonuçlarını yorumlamaya ve "aile dostu," "havuz" ve "Honolulu" kriterlerine göre en iyi eşleşmeleri belirlemeye yardımcı olur, sonrasında doğal dille yanıtı formatlar. Önemli olarak, yanıt gerçek otel kataloglarına referans verir; uydurma bilgi içermez.

5. **AI Ajan Etkileşimi**: NLWeb bir MCP sunucusu olarak hizmet verdiği için, harici bir AI seyahat ajanı da bu sitedeki NLWeb örneğine bağlanabilir. AI ajanı `ask` MCP metoduyla siteyi doğrudan sorgulayabilir: `ask("Oteller tarafından önerilen Honolulu bölgesinde vegan dostu restoranlar var mı?")`. NLWeb örneği bunu işler, varsa restoran veritabanını kullanır ve yapılandırılmış JSON yanıt döner.

### MCP/A2A/NLWeb Hakkında Daha Fazla Sorunuz mu Var?

Başka öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanları ile ilgili sorularınızı sormak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)'a katılın.

## Kaynaklar

- [MCP Yeni Başlayanlar için](https://aka.ms/mcp-for-beginners)  
- [MCP Dokümantasyonu](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Deposu](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Önceki Ders

[Üretimde AI Ajanları](../10-ai-agents-production/README.md)

## Sonraki Ders

[AI Ajanları için Bağlam Mühendisliği](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->