# Yapay Zeka Ajanları için Bellek  
[![Agent Memory](../../../translated_images/tr/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Yapay Zeka Ajanları oluşturmanın benzersiz faydalarından bahsederken, genellikle iki şey öne çıkar: görevleri tamamlamak için araçları çağırabilme yeteneği ve zamanla gelişebilme yeteneği. Bellek, kullanıcılarımız için daha iyi deneyimler yaratabilen, kendini geliştiren bir ajan oluşturmanın temelidir.

Bu derste, Yapay Zeka Ajanları için belleğin ne olduğunu ve uygulamalarımızın yararına nasıl yönetip kullanabileceğimizi inceleyeceğiz.

## Giriş

Bu ders şunları kapsayacaktır:

• **Yapay Zeka Ajan Belleğini Anlamak**: Belleğin ne olduğu ve ajanlar için neden önemli olduğu.

• **Belleği Uygulamak ve Depolamak**: AI ajanlarınıza kısa vadeli ve uzun vadeli bellek yetenekleri eklemek için pratik yöntemler.

• **Yapay Zeka Ajanlarını Kendini Geliştiren Hale Getirmek**: Belleğin ajanların geçmiş etkileşimlerden öğrenmesini ve zamanla gelişmesini nasıl sağladığı.

## Mevcut Uygulamalar

Bu ders iki kapsamlı not defteri eğitimi içerir:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Mem0 ve Microsoft Agent Framework ile Azure AI Search kullanarak belleği uygular

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Cognee kullanarak yapılandırılmış belleği uygular, gömülerle desteklenen otomatik bilgi grafiği oluşturur, grafiği görselleştirir ve akıllı sorgulama yapar

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bileceksiniz:

• **Yapay zeka ajan belleğinin çeşitli türleri arasında ayrım yapmayı**, çalışma belleği, kısa vadeli ve uzun vadeli bellek ile persona ve epizodik bellek gibi özel biçimleri içeren.

• **Microsoft Agent Framework kullanarak yapay zeka ajanları için kısa vadeli ve uzun vadeli belleği uygulamayı ve yönetmeyi**, Mem0, Cognee, Whiteboard belleği gibi araçları kullanarak ve Azure AI Search ile entegrasyon yaparak.

• **Kendini geliştiren yapay zeka ajanlarının arkasındaki prensipleri anlamayı** ve güçlü bellek yönetim sistemlerinin sürekli öğrenme ve uyuma nasıl katkıda bulunduğunu.

## Yapay Zeka Ajan Belleğini Anlamak

Özünde, **yapay zeka ajanları için bellek, onların bilgileri tutmasını ve hatırlamasını sağlayan mekanizmalardır**. Bu bilgi, bir konuşmaya ait spesifik detaylar, kullanıcı tercihleri, geçmiş eylemler veya öğrenilmiş kalıplar olabilir.

Bellek yoksa yapay zeka uygulamaları genellikle durumsuzdur; yani her etkileşim sıfırdan başlar. Bu da ajanın önceki bağlamı veya tercihleri "unutması" sonucunda tekrarlayan ve sinir bozucu bir kullanıcı deneyimi ortaya çıkarır.

### Bellek Neden Önemlidir?

Bir ajanın zekası, geçmiş bilgileri hatırlayıp kullanabilme yeteneğiyle derin şekilde bağlıdır. Bellek, ajanların:

• **Düşünümsel Olmasını**: Geçmiş eylemlerden ve sonuçlardan öğrenmesini sağlar.

• **Etkileşimli Olmasını**: Devam eden bir konuşmadaki bağlamı korumasını sağlar.

• **Proaktif ve Reaktif Olmasını**: İhtiyaçları önceden tahmin edebilmesini veya geçmiş verilere dayalı uygun yanıtlar vermesini sağlar.

• **Özerk Olmasını**: Saklanan bilgileri kullanarak daha bağımsız hareket etmesini sağlar.

Bellek uygulamanın hedefi, ajanları daha **güvenilir ve yetkin** hale getirmektir.

### Bellek Türleri

#### Çalışma Belleği

Bunu, bir ajanın tek bir devam eden görev veya düşünce süreci sırasında kullandığı bir not kağıdı gibi düşünebilirsiniz. Bir sonraki adımı hesaplamak için gereken anlık bilgileri tutar.

AI ajanları için çalışma belleği, genellikle bir konuşmadan en ilgili bilgileri yakalar, tam sohbet geçmişi uzun veya kısaltılmış olsa bile. Gereksinimler, teklifler, kararlar ve eylemler gibi anahtar unsurların çıkarılmasına odaklanır.

**Çalışma Belleği Örneği**

Bir seyahat rezervasyon ajanında, çalışma belleği kullanıcının anlık talebini, örneğin "Paris'e bir seyahat rezervasyonu yapmak istiyorum" ifadesini yakalayabilir. Bu spesifik gereksinim, mevcut etkileşimi yönlendirmek için ajanın anlık bağlamında tutulur.

#### Kısa Vadeli Bellek

Bu bellek türü, bilgiyi tek bir konuşma veya oturum süresince saklar. Mevcut sohbetin bağlamıdır; ajanın diyaloğun önceki turlarına referans vermesini sağlar.

[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK örneklerinde, bu `AgentSession` ile eşlenir ve `agent.create_session()` ile oluşturulur. Oturum, framework’un yerleşik kısa vadeli belleğidir: konuşma bağlamını aynı oturum boyunca kullanılabilir tutar ancak oturum sona erdiğinde veya uygulama yeniden başlatıldığında bu bağlam korunmaz. Gerçekler ve tercihlerin oturumlar arasında sürmesi gereken durumlar için, genellikle bir veritabanı, vektör indeks veya başka kalıcı bir depolama kullanılarak uzun vadeli bellek uygulanmalıdır.

**Kısa Vadeli Bellek Örneği**

Bir kullanıcı "Paris'e uçak bileti ne kadar tutar?" diye sorup ardından "Orada konaklama ne durumda?" diye devam ederse, kısa vadeli bellek, ajanın "orada" kelimesinin aynı konuşmada "Paris"e atıfta bulunduğunu bilmesini sağlar.

#### Uzun Vadeli Bellek

Bu, birden fazla konuşma veya oturum boyunca sürdürülen bilgidir. Ajanların kullanıcı tercihlerini, geçmiş etkileşimleri veya genel bilgileri uzun süre hatırlamasını sağlar. Kişiselleştirme için önemlidir.

**Uzun Vadeli Bellek Örneği**

Uzun vadeli bellek, "Ben kayak ve açık hava aktivitelerini sever, dağ manzaralı kahveyi tercih eder ve geçmiş bir sakatlanma nedeniyle ileri düzey pistlerden kaçınır" gibi bilgileri depolayabilir. Bu bilgi, önceki etkileşimlerden öğrenilir ve gelecekteki seyahat planlama oturumlarında önerileri yüksek derecede kişiselleştirir.

#### Persona Belleği

Bu özel bellek türü, bir ajanın tutarlı bir "kişilik" veya "persona" geliştirmesine yardımcı olur. Ajanın kendisi veya hedeflenen rolü hakkında ayrıntıları hatırlayabilmesini sağlar ve etkileşimleri daha akıcı ve odaklı hale getirir.

**Persona Belleği Örneği**  
Eğer seyahat ajanı "uzman kayak planlayıcısı" olarak tasarlandıysa, persona belleği bu rolü pekiştirir ve yanıtlarını bir uzmanın tonu ve bilgisi doğrultusunda şekillendirir.

#### İş Akışı/Epizodik Bellek

Bu bellek, ajanın karmaşık bir görev sırasında attığı adımların dizisini, başarılarını ve başarısızlıklarını saklar. Spesifik "bölümleri" veya geçmiş deneyimleri hatırlamak ve bunlardan öğrenmek gibidir.

**Epizodik Bellek Örneği**

Eğer ajan belli bir uçak biletini rezerve etmeye çalıştı ancak müsaitlik problemi nedeniyle başarısız olduysa, epizodik bellek bu hatayı kaydedebilir ve sonraki denemede alternatif uçuşlar denemesi veya kullanıcıyı daha bilgilendirici bir şekilde bilgilendirmesi için kullanabilir.

#### Öğe Belleği

Konuşmalardan belirli varlıkları (insanlar, yerler veya nesneler gibi) ve olayları çıkarıp hatırlamayı içerir. Ajanın konuşulmuş anahtar unsurlar hakkında yapılandırılmış bir anlayış oluşturmasını sağlar.

**Öğe Belleği Örneği**

Geçmiş bir seyahat hakkında yapılan bir konuşmadan ajan "Paris," "Eyfel Kulesi" ve "Le Chat Noir restoranında akşam yemeği" gibi varlıkları çıkarabilir. Gelecekteki bir etkileşimde ajan "Le Chat Noir"u hatırlayarak orada yeniden rezervasyon yapmayı teklif edebilir.

#### Yapılandırılmış RAG (Retrieval Augmented Generation)

RAG daha geniş bir teknik olmakla birlikte, "Yapılandırılmış RAG" güçlü bir bellek teknolojisi olarak öne çıkar. Konuşmalar, e-postalar, görüntüler gibi çeşitli kaynaklardan yoğun, yapılandırılmış bilgiler çıkarır ve bunları yanıtların doğruluğunu, hatırlamasını ve hızını artırmak için kullanır. Klasik RAG'in yalnızca anlamsal benzerliğe dayanmasının aksine, Yapılandırılmış RAG bilgi yapısının kendisiyle çalışır.

**Yapılandırılmış RAG Örneği**

Sadece anahtar kelimeleri eşleştirmek yerine, Yapılandırılmış RAG bir e-postadan uçuş ayrıntılarını (varış yeri, tarih, saat, havayolu) ayrıştırabilir ve bunları yapılandırılmış biçimde saklayabilir. Böylece "Salı günü Paris'e hangi uçuşu ayırttım?" gibi kesin sorgulara olanak tanır.

## Belleği Uygulamak ve Depolamak

AI ajanları için belleği uygulamak, bilgi üretme, depolama, geri getirme, bütünleştirme, güncelleme ve hatta **unutma** (veya silme) gibi adımları içeren sistematik bir **bellek yönetimi** süreci gerektirir. Geri çağırma özellikle kritik bir aşamadır.

### Özel Bellek Araçları

#### Mem0

Ajan belleğini depolamak ve yönetmek için özel araçlardan biri Mem0'dır. Mem0, ajanların ilgili etkileşimleri hatırlamasına, kullanıcı tercihlerini ve gerçek bağlamı depolamasına ve zaman içinde başarılar ile başarısızlıklardan öğrenmesine olanak tanıyan kalıcı bir bellek katmanı olarak çalışır. Buradaki fikir, durumsuz ajanların durumlu hale dönüşmesidir.

İşleyişi **iki aşamalı bellek boru hattı: çıkarım ve güncelleme** şeklindedir. Önce, ajan dizisine eklenen mesajlar Mem0 servisine gönderilir; burada bir Büyük Dil Modeli (LLM) konuşma geçmişini özetler ve yeni anıları çıkarır. Daha sonra LLM destekli bir güncelleme aşaması, bu anıların eklenip eklenmeyeceğine, değiştirilip değiştirilmemesine veya silinmesine karar verir ve bunları vektör, grafik ve anahtar-değer veri tabanlarını içerebilen hibrit bir veri deposunda saklar. Sistem birçok bellek türünü destekler ve varlıklar arasındaki ilişkileri yönetmek için grafik belleği içerebilir.

#### Cognee

Başka güçlü bir yaklaşım, yapılandırılmış ve yapılandırılmamış verileri sorgulanabilir gömülü bilgi grafikleri haline dönüştüren açık kaynak semantic bellek aracı **Cognee**dir. Cognee, vektör benzerlik araması ile grafik ilişkilerini birleştiren **ikili depolama mimarisi** sağlar ve bu sayede ajanların yalnızca hangi bilginin benzer olduğunu değil, kavramların birbirleriyle nasıl ilişkili olduğunu anlamalarına olanak tanır.

Ham parça aramadan grafik tabanlı soru yanıtlamaya kadar, vektör benzerliği, grafik yapısı ve LLM akıl yürütmesini harmanlayan **karma geri çağırmada (hybrid retrieval)** üstün performans gösterir. Sistem, kısa vadeli oturum bağlamını ve uzun vadeli kalıcı belleği destekleyen, sorgulanabilir ve tek bir bağlı grafik olarak gelişen ve büyüyen **yaşayan bellek** tutar.

Cognee not defteri eğitimi ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)), çeşitli veri kaynaklarının içe aktarılması, bilgi grafiğinin görselleştirilmesi ve belli ajan ihtiyaçlarına uygun farklı arama stratejileri ile sorgulama yapmayı göstererek bu birleşik bellek katmanının nasıl oluşturulacağını pratik örneklerle sunar.

### Belleği RAG ile Depolamak

Mem0 gibi özel bellek araçlarının yanı sıra, kalıcı anıları depolamak ve geri çağırmak için sağlam arama servisleri kullanabilirsiniz. Özellikle yapılandırılmış RAG için **Azure AI Search** bu amaçla etkin bir arka uç görevi görebilir.

Bu, ajanın yanıtlarını kendi verilerinizle destekleyerek daha alakalı ve doğru cevaplar alınmasını sağlar. Azure AI Search, kullanıcıya özgü seyahat anılarını, ürün kataloglarını veya başka alan özel bilgilerini depolamak için kullanılabilir.

Azure AI Search, yapılandırılmış RAG olanaklarını destekler ve konuşma geçmişi, e-postalar veya hatta görüntüler gibi büyük veri setlerinden yoğun, yapılandırılmış bilgilerin çıkarılması ve çağrılmasında üstün doğruluk ve geri çağırma sağlar. Bu, geleneksel metin parçalayıcı ve gömme yaklaşımlarına kıyasla "insanüstü doğruluk ve geri çağırma" sunar.

## Yapay Zeka Ajanlarının Kendini Geliştirmesini Sağlamak

Kendini geliştiren ajanlar için yaygın bir desen, bir **"bilgi ajanı"** tanımlamaktır. Bu ayrı ajan, kullanıcı ile ana ajan arasındaki ana konuşmayı gözlemler. Rolü şunlardır:

1. **Değerli bilgiyi tespit etmek**: Konuşmanın herhangi bir bölümünün genel bilgi veya belli bir kullanıcı tercihi olarak kaydedilmeye değer olup olmadığını belirlemek.

2. **Çıkarmak ve özetlemek**: Konuşmadan temel öğrenme veya tercihi özetlemek.

3. **Bilgi tabanına kaydetmek**: Bu çıkarılan bilgiyi genellikle bir vektör veritabanında kalıcı olarak depolamak, böylece ileride geri çağrılabilmesini sağlamak.

4. **Gelecekteki sorguları desteklemek**: Kullanıcı yeni bir sorgu başlattığında, bilgi ajanı ilgili depolanmış bilgileri getirip kullanıcının istemine ekler, böylece ana ajana kritik bağlam sağlar (RAG benzeri).

### Bellek İçin Optimizasyonlar

• **Gecikme Yönetimi**: Kullanıcı etkileşimlerini yavaşlatmamak için, başlangıçta daha ucuz ve hızlı bir model kullanılarak bilginin depolanmaya veya geri çağrılmaya değer olup olmadığı hızlıca kontrol edilir, daha karmaşık çıkarım/geri çağırma süreci sadece ihtiyaç olduğunda tetiklenir.

• **Bilgi Tabanı Bakımı**: Büyüyen bir bilgi tabanı için, daha nadiren kullanılan bilgiler maliyeti yönetmek için "soğuk depolama"ya taşınabilir.

## Ajan Belleği Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, çalışma saatlerine katılmak ve Yapay Zeka Ajanlarınızla ilgili sorularınızı sormak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) sunucusuna katılın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->