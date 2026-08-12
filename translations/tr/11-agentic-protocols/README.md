# Agentik Protokollerin Kullanımı (MCP, A2A ve NLWeb)

[![Agentik Protokoller](../../../translated_images/tr/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Bu dersin videosunu görüntülemek için yukarıdaki resme tıklayın)_

AI ajanlarının kullanımı arttıkça, standartlaştırma, güvenlik sağlama ve açık inovasyonu destekleme ihtiyacı da artmaktadır. Bu derste, bu ihtiyacı karşılamayı amaçlayan 3 protokolü ele alacağız - Model Context Protocol (MCP), Agent to Agent (A2A) ve Natural Language Web (NLWeb).

## Giriş

Bu derste şunları ele alacağız:

• **MCP'nin** AI Ajanlarının kullanıcı görevlerini tamamlamak için dış araçlara ve verilere erişimini nasıl sağladığı.

• **A2A'nın** farklı AI ajanları arasında iletişim ve iş birliği sağlaması.

• **NLWeb'in** AI Ajanlarının içerikleri keşfetmesine ve etkileşimde bulunmasına olanak sağlayan doğal dil arayüzlerini herhangi bir web sitesine nasıl getirdiği.

## Öğrenme Hedefleri

• AI ajanları bağlamında MCP, A2A ve NLWeb'in temel amacı ve faydalarını **tanımlamak**.

• Her protokolün LLM'ler, araçlar ve diğer ajanlar arasındaki iletişim ve etkileşimi nasıl kolaylaştırdığını **açıklamak**.

• Karmaşık ajanik sistemler oluşturmadaki her protokolün farklı rollerini **tanımak**.

## Model Context Protocol

**Model Context Protocol (MCP)**, uygulamaların LLM'lere bağlam ve araç sağlaması için standartlaştırılmış açık bir standarttır. Bu, AI Ajanlarının tutarlı bir şekilde bağlanabileceği farklı veri kaynaklarına ve araçlara yönelik "evrensel bir adaptör" sağlar.

MCP'nin bileşenlerine, doğrudan API kullanımına kıyasla faydalarına ve AI ajanlarının MCP sunucusunu nasıl kullanabileceğine dair bir örneğe bakalım.

### MCP Temel Bileşenler

MCP, **istemci-sunucu mimarisi** üzerinde çalışır ve temel bileşenleri şunlardır:

• **Hostlar**, MCP Sunucusuna bağlantıyı başlatan LLM uygulamalarıdır (örneğin VSCode gibi bir kod düzenleyici).

• **İstemciler**, ana uygulamanın içinde sunucularla bire bir bağlantı kuran bileşenlerdir.

• **Sunucular**, belirli yetenekleri açığa çıkaran hafif programlardır.

Protokolde, MCP Sunucusunun yetenekleri olan üç temel ilkel bulunmaktadır:

• **Araçlar**: AI ajanının bir işlemi gerçekleştirmek için çağırabileceği ayrı işlemler veya fonksiyonlardır. Örneğin, bir hava durumu servisi "hava durumu al" aracını sunabilir ya da bir e-ticaret sunucusu "ürün satın al" aracını sunabilir. MCP sunucuları her aracın adını, açıklamasını ve giriş/çıkış şemasını yetenekler listesinde ilan eder.

• **Kaynaklar**: MCP sunucusunun sağlayabileceği salt okunur veri öğeleri veya belgeler olup, istemciler bunları talep üzerine alabilir. Örnekler arasında dosya içerikleri, veritabanı kayıtları veya günlük dosyaları bulunur. Kaynaklar metin (kod veya JSON gibi) ya da ikili (resim veya PDF gibi) olabilir.

• **İstekler (Prompts)**: Daha karmaşık iş akışlarına olanak tanıyan önerilen önceden tanımlı şablonlardır.

### MCP'nin Faydaları

MCP, AI Ajanları için önemli avantajlar sunar:

• **Dinamik Araç Keşfi**: Ajanlar, bir sunucudan mevcut araçların bir listesini ve ne yaptıklarını dinamik olarak alabilirler. Bu, geleneksel API'lerle karşılaştırıldığında, entegrasyonların genellikle statik kodlama gerektirmesi ve API değişikliklerinin kod güncellemelerini zorunlu kılması yerine, MCP'nin "bir kez entegre et" yaklaşımı ile daha büyük uyarlanabilirlik sağlar.

• **LLM'ler Arası İnteroperabilite**: MCP farklı LLM'ler arasında çalışır ve daha iyi performans için çekirdek modellerin değiştirilmesine esneklik sağlar.

• **Standart Güvenlik**: MCP standart bir kimlik doğrulama yöntemi içerir, bu da ek MCP sunucularına erişim eklerken ölçeklenebilirliği artırır. Bu, farklı anahtarlar ve kimlik doğrulama türlerini yönetmekten daha basittir.

### MCP Örneği

![MCP Diagram](../../../translated_images/tr/mcp-diagram.e4ca1cbd551444a1.webp)

Bir kullanıcı MCP tarafından desteklenen bir AI yardımcısı kullanarak uçak bileti rezervasyonu yapmak istiyor olsun.

1. **Bağlantı**: AI asistanı (MCP istemcisi), bir havayolu tarafından sağlanan MCP sunucusuna bağlanır.

2. **Araç Keşfi**: İstemci, havayolunun MCP sunucusuna, "Hangi araçlarınız mevcut?" diye sorar. Sunucu "uçuş arama" ve "uçuş rezervasyonu yap" gibi araçlarla cevap verir.

3. **Araç Çağrısı**: Siz sonra AI asistana, "Lütfen Portland'dan Honolulu'ya uçuş ara." dersiniz. AI asistanı, kendi LLM'sini kullanarak "uçuş arama" aracını çağırması gerektiğini belirler ve uygun parametreleri (kalkış yeri, varış yeri) MCP sunucusuna gönderir.

4. **Yürütme ve Yanıt**: MCP sunucusu, bir sarmalayıcı olarak, havayolunun dahili rezervasyon API'sini gerçek olarak çağırır. Ardından uçuş bilgilerini (örneğin JSON verisi) alır ve AI asistana geri gönderir.

5. **İleri Etkileşim**: AI asistanı uçuş seçeneklerini sunar. Siz bir uçuş seçtiğinizde, asistan aynı MCP sunucusundaki "uçuş rezervasyonu yap" aracını çağırabilir ve rezervasyonu tamamlar.

## Agent-to-Agent Protokolü (A2A)

MCP, LLM'leri araçlara bağlamaya odaklanırken, **Agent-to-Agent (A2A) protokolü** bunu bir adım ileriye taşıyarak farklı AI ajanlarının iletişim ve iş birliği yapmasını sağlar. A2A, farklı organizasyonlar, ortamlar ve teknoloji yığınları arasında AI ajanlarını ortak bir görevi tamamlamak üzere bağlar.

A2A'nın bileşenlerini ve faydalarını inceleyecek, ayrıca seyahat uygulamamızda nasıl uygulanabileceğine dair bir örnek vereceğiz.

### A2A Temel Bileşenler

A2A, ajanlar arasında iletişimi sağlama ve kullanıcının alt görevini tamamlamak için birlikte çalışma üzerinde odaklanır. Protokolün her bileşeni buna katkı sağlar:

#### Ajan Kartı

MCP sunucusunun araç listesini paylaşmasına benzer şekilde, bir Ajan Kartında şunlar vardır:
- Ajanın Adı.
- Tamamladığı genel görevlerin **açıklaması**.
- Diğer ajanların (veya insan kullanıcıların) ajanı ne zaman ve neden çağırmaları gerektiğini anlamalarına yardımcı olmak için **belirli becerilerin listesi** ve açıklamaları.
- Ajanın **mevcut Uç Nokta URL'si**.
- Ajanın **sürümü** ve yanıt akışı ile push bildirimleri gibi **yetkinlikleri**.

#### Ajan Yürütücüsü

Ajan Yürütücüsü, **kullanıcı sohbetinin bağlamını uzak ajana geçirerek**, uzak ajanın tamamlanması gereken görevi anlamasını sağlar. Bir A2A sunucusunda, bir ajan gelen talepleri ayrıştırmak ve kendi dahili araçlarını kullanarak görevleri yürütmek için kendi Büyük Dil Modelini (LLM) kullanır.

#### Eser (Artifact)

Uzak ajan istenen görevi tamamladığında, çalışmasının sonucu bir eser olarak oluşturulur. Bir eser, **ajan çalışmasının sonucunu**, **tamamlanan şeyin açıklamasını** ve protokol aracılığıyla gönderilen **metin bağlamını** içerir. Eser gönderildikten sonra, uzak ajanla bağlantı ihtiyaç duyulana kadar kapatılır.

#### Olay Kuyruğu

Bu bileşen, **güncellemeleri işlemek ve mesajları iletmek** için kullanılır. Özellikle, görev tamamlanma sürelerinin uzun olabileceği durumlarda, ajanlar arası bağlantının görev tamamlanmadan önce kapanmasını önlemek açısından üretimde önemli bir rol oynar.

### A2A'nın Faydaları

• **Gelişmiş İş Birliği**: Farklı satıcılar ve platformlardan ajanların etkileşimde bulunmasını, bağlam paylaşmasını ve birlikte çalışmasını sağlayarak, geleneksel olarak bağlantısız sistemler arasında kesintisiz otomasyon imkanı verir.

• **Model Seçim Esnekliği**: Her A2A ajanı isteklerini karşılamak için hangi LLM'yi kullanacağına kendisi karar verebilir, bu da bazı MCP senaryolarındaki tek LLM bağlantısının aksine ajan başına optimize edilmiş veya ince ayarlanmış modellerin kullanılmasına olanak tanır.

• **Yerleşik Kimlik Doğrulama**: Kimlik doğrulama doğrudan A2A protokolüne entegre edilmiştir ve ajan etkileşimleri için sağlam bir güvenlik çerçevesi sağlar.

### A2A Örneği

![A2A Diagram](../../../translated_images/tr/A2A-Diagram.8666928d648acc26.webp)

Seyahat rezervasyon senaryomuzu bu defa A2A kullanarak genişletelim.

1. **Kullanıcıdan Çoklu Ajan İsteği**: Kullanıcı, bir "Seyahat Ajanı" A2A istemcisi/ajanı ile etkileşime geçer ve belki şöyle der: "Lütfen önümüzdeki hafta Honolulu'ya uçuşlar, otel ve kiralık araba dahil tam bir gezi ayarla."

2. **Seyahat Ajanı Tarafından Orkestrasyon**: Seyahat Ajanı bu karmaşık isteği alır. LLM'sini kullanarak görevi değerlendirir ve diğer uzman ajanlarla etkileşimde bulunması gerektiğine karar verir.

3. **Ajanlar Arası İletişim**: Seyahat Ajanı, A2A protokolünü kullanarak "Havayolu Ajanı", "Otel Ajanı" ve "Araç Kiralama Ajanı" gibi farklı şirketler tarafından oluşturulan alt ajanlara bağlanır.

4. **Yetkili Görev Yürütme**: Seyahat Ajanı, bu uzman ajanlara belirli görevler gönderir (örneğin "Honolulu'ya uçuş bul", "Otel rezervasyonu yap", "Araba kirala"). Bu uzman ajanların her biri, kendi LLM'leri ve kendi araçlarıyla (ki bu MCP sunucuları olabilir) rezervasyonun kendi bölümünü yapar.

5. **Birleştirilmiş Yanıt**: Tüm alt ajanlar görevlerini tamamladığında, Seyahat Ajanı sonuçları (uçuş detayları, otel onayı, araç kiralama rezervasyonu) derler ve kullanıcıya sohbet tarzında kapsamlı bir yanıt gönderir.

## Doğal Dil Webi (NLWeb)

Web siteleri, kullanıcıların internet genelinde bilgi ve verilere eriştikleri ana yol olmuştur.

NLWeb'in farklı bileşenlerine, NLWeb'in faydalarına ve seyahat uygulamamız bağlamında nasıl çalıştığına bakalım.

### NLWeb Bileşenleri

- **NLWeb Uygulaması (Temel Servis Kodu)**: Doğal dil sorularını işleyen sistemdir. Platformun farklı parçalarını bağlayarak yanıtlar oluşturur. Bir web sitesinin doğal dil özelliklerini güçlendiren **motor** olarak düşünebilirsiniz.

- **NLWeb Protokolü**: Bir web sitesi ile doğal dil etkileşimi için **temel kurallar dizisi**dir. Yanıtları JSON formatında (genellikle Schema.org kullanarak) geri gönderir. Amacı, "Yapay Zeka Webi" için basit bir temel oluşturmaktır, tıpkı HTML'nin çevrimiçi belgelerin paylaşılmasını mümkün kılması gibi.

- **MCP Sunucusu (Model Context Protocol Uç Noktası)**: Her NLWeb kurulumu ayrıca bir **MCP sunucusu** olarak da çalışır. Bu, diğer AI sistemleriyle **araçları (örneğin "sor" yöntemi) ve verileri paylaşabileceği** anlamına gelir. Pratikte, bu web sitesinin içeriğinin ve yeteneklerinin AI ajanları tarafından kullanılmasını sağlar ve sitenin daha geniş "ajan ekosistemi" parçası haline gelmesine olanak tanır.

- **Yerleştirme Modelleri**: Bu modeller, web sitesi içeriğini sayısal temsillere dönüştürmek için kullanılır; bu temsillere vektörler (embedding) denir. Bu vektörler, bilgisayarların karşılaştırıp arayabileceği anlamı yakalar. Özel bir veritabanında saklanırlar ve kullanıcılar hangi yerleştirme modelini kullanacaklarını seçebilirler.

- **Vektör Veritabanı (Geri Getirme Mekanizması)**: Web sitesi içeriğinin yerleştirmelerini saklayan veritabanıdır. Biri soru sorduğunda, NLWeb hızlıca en alakalı bilgileri bulmak için vektör veritabanına bakar. Benzerliklerine göre sıralanmış olası yanıtların hızlı bir listesini verir. NLWeb, Qdrant, Snowflake, Milvus, Azure AI Search ve Elasticsearch gibi farklı vektör depolama sistemleriyle çalışır.

### NLWeb Örneği

![NLWeb](../../../translated_images/tr/nlweb-diagram.c1e2390b310e5fe4.webp)

Seyahat rezervasyon web sitemizi tekrar düşünelim, ancak bu sefer NLWeb tarafından destekleniyor.

1. **Veri Alımı**: Seyahat sitesinin mevcut ürün katalogları (örneğin uçuş listeleri, otel açıklamaları, tur paketleri) Schema.org kullanılarak veya RSS beslemeleri yoluyla biçimlendirilir. NLWeb araçları bu yapılandırılmış verileri alır, yerleştirmeler oluşturur ve bunları yerel veya uzaktaki bir vektör veritabanında saklar.

2. **Doğal Dil Sorgusu (İnsan)**: Bir kullanıcı siteyi ziyaret eder ve menüde gezinmek yerine sohbet arayüzüne şöyle yazar: "Önümüzdeki hafta Honolulu'da havuzlu aile dostu bir otel bul." 

3. **NLWeb İşleme**: NLWeb uygulaması bu sorguyu alır. Anlamak için sorguyu bir LLM'ye gönderir ve aynı zamanda ilgili otel listelerini aramak için vektör veritabanını kontrol eder.

4. **Doğru Sonuçlar**: LLM, veritabanından gelen arama sonuçlarını yorumlar, "aile dostu", "havuz" ve "Honolulu" kriterlerine göre en iyi eşleşmeleri belirler ve doğal dil yanıtı oluşturur. Hayati olarak yanıt, web sitesinin kataloğundaki gerçek otellere atıfta bulunur; uydurma bilgi içermez.

5. **AI Ajan Etkileşimi**: NLWeb, bir MCP sunucusu olarak hizmet verdiğinden, harici bir AI seyahat ajanı da bu sitenin NLWeb örneğine bağlanabilir. AI ajanı doğrudan siteye sorgulama yapmak için `ask` MCP yöntemini kullanabilir: `ask("Honolulu bölgesinde otelin önerdiği vegan dostu restoranlar var mı?")`. NLWeb örneği bunu işler, yüklüyse restoran bilgisi veritabanını kullanır ve yapılandırılmış JSON yanıtı döner.

### MCP/A2A/NLWeb hakkında Daha Fazla Sorunuz Mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanlarınız hakkındaki sorularınızı sormak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) sunucusuna katılın.

## Kaynaklar

- [Yeni Başlayanlar için MCP](https://aka.ms/mcp-for-beginners)  
- [MCP Dokümantasyonu](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Deposu](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Ajan Çerçevesi](https://aka.ms/ai-agents-beginners/agent-framework)

## Önceki Ders

[Üretimde AI Ajanları](../10-ai-agents-production/README.md)

## Sonraki Ders

[AI Ajanları için Bağlam Mühendisliği](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->