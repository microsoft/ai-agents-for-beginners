<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2c9703548140bafa2d6a77406552542",
  "translation_date": "2025-10-03T14:38:51+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "tr"
}
-->
# AI Ajanları için Bellek
[![Ajan Belleği](../../../translated_images/lesson-13-thumbnail.959e3bc52d210c64a614a3bece6b170a2c472138dc0a14c7fbde07306ef95ae7.tr.png)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

AI ajanları oluşturmanın benzersiz faydalarını tartışırken, genellikle iki şey öne çıkar: görevleri tamamlamak için araçları çağırma yeteneği ve zamanla gelişme yeteneği. Bellek, kullanıcılarımıza daha iyi deneyimler sunabilecek kendini geliştiren ajanlar oluşturmanın temelinde yer alır.

Bu derste, AI ajanları için belleğin ne olduğunu, nasıl yönetileceğini ve uygulamalarımızın yararına nasıl kullanılacağını inceleyeceğiz.

## Giriş

Bu derste şunlar ele alınacak:

• **AI Ajan Belleğini Anlamak**: Belleğin ne olduğu ve ajanlar için neden önemli olduğu.

• **Belleği Uygulama ve Depolama**: AI ajanlarınıza bellek özellikleri eklemek için kısa ve uzun vadeli belleğe odaklanan pratik yöntemler.

• **AI Ajanlarını Kendini Geliştiren Hale Getirme**: Belleğin ajanların geçmiş etkileşimlerden öğrenmesini ve zamanla gelişmesini nasıl sağladığı.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları öğrenmiş olacaksınız:

• **AI ajan belleğinin farklı türlerini ayırt etmek**, çalışma belleği, kısa vadeli ve uzun vadeli bellek gibi, ayrıca kişilik ve epizodik bellek gibi özel türler.

• **AI ajanları için kısa ve uzun vadeli belleği uygulamak ve yönetmek**, Semantic Kernel çerçevesini kullanarak, Mem0 ve Whiteboard bellek gibi araçlardan yararlanarak ve Azure AI Search ile entegre ederek.

• **Kendini geliştiren AI ajanlarının arkasındaki prensipleri anlamak** ve sağlam bellek yönetim sistemlerinin sürekli öğrenme ve uyum sağlamaya nasıl katkıda bulunduğunu görmek.

## AI Ajan Belleğini Anlamak

Temelde, **AI ajanları için bellek, bilgiyi saklama ve hatırlama mekanizmalarını ifade eder**. Bu bilgi, bir konuşma hakkındaki spesifik detaylar, kullanıcı tercihleri, geçmiş eylemler veya öğrenilmiş kalıplar olabilir.

Bellek olmadan, AI uygulamaları genellikle durumsuzdur, yani her etkileşim sıfırdan başlar. Bu, ajanın önceki bağlamı veya tercihleri "unutması" nedeniyle tekrarlayan ve hayal kırıklığı yaratan bir kullanıcı deneyimine yol açar.

### Bellek Neden Önemlidir?

Bir ajanın zekası, geçmiş bilgileri hatırlama ve kullanma yeteneğiyle yakından ilişkilidir. Bellek, ajanların şu özelliklere sahip olmasını sağlar:

• **Düşünceli**: Geçmiş eylemlerden ve sonuçlardan öğrenme.

• **Etkileşimli**: Süregelen bir konuşma boyunca bağlamı koruma.

• **Proaktif ve Tepkisel**: Geçmiş verilere dayanarak ihtiyaçları tahmin etme veya uygun şekilde yanıt verme.

• **Otonom**: Saklanan bilgiyi kullanarak daha bağımsız çalışabilme.

Bellek uygulamanın amacı, ajanları daha **güvenilir ve yetenekli** hale getirmektir.

### Bellek Türleri

#### Çalışma Belleği

Bunu, bir ajanın tek bir görev veya düşünce süreci sırasında kullandığı bir tür "not kağıdı" olarak düşünebilirsiniz. Bir sonraki adımı hesaplamak için gerekli olan anlık bilgileri tutar.

AI ajanları için çalışma belleği genellikle bir konuşmadan en alakalı bilgileri yakalar, hatta tam sohbet geçmişi uzun veya kısaltılmış olsa bile. Gereksinimler, öneriler, kararlar ve eylemler gibi temel unsurları çıkarmaya odaklanır.

**Çalışma Belleği Örneği**

Bir seyahat rezervasyon ajanında, çalışma belleği kullanıcının mevcut talebini, örneğin "Paris'e bir gezi rezervasyonu yapmak istiyorum" gibi, yakalayabilir. Bu spesifik gereklilik, mevcut etkileşimi yönlendirmek için ajanın anlık bağlamında tutulur.

#### Kısa Vadeli Bellek

Bu tür bellek, tek bir konuşma veya oturum süresince bilgiyi tutar. Mevcut sohbetin bağlamıdır ve ajanın diyalogdaki önceki dönüşlere atıfta bulunmasını sağlar.

**Kısa Vadeli Bellek Örneği**

Bir kullanıcı "Paris'e bir uçuş ne kadar tutar?" diye sorar ve ardından "Oradaki konaklama ne durumda?" diye devam ederse, kısa vadeli bellek ajanın "orada" kelimesinin "Paris" anlamına geldiğini bilmesini sağlar.

#### Uzun Vadeli Bellek

Bu, birden fazla konuşma veya oturum boyunca devam eden bilgidir. Kullanıcı tercihlerini, geçmiş etkileşimleri veya genel bilgileri uzun süreli olarak hatırlamasını sağlar. Kişiselleştirme için önemlidir.

**Uzun Vadeli Bellek Örneği**

Uzun vadeli bellek, "Ben kayak yapmayı ve açık hava aktivitelerini sever, dağ manzaralı kahveyi tercih eder ve geçmişteki bir yaralanma nedeniyle ileri seviye kayak pistlerinden kaçınmak ister" gibi bilgileri saklayabilir. Bu bilgi, önceki etkileşimlerden öğrenilir ve gelecekteki seyahat planlama oturumlarında önerileri son derece kişiselleştirilmiş hale getirir.

#### Kişilik Belleği

Bu özel bellek türü, bir ajanın tutarlı bir "kişilik" veya "rol" geliştirmesine yardımcı olur. Ajana kendisi veya amaçlanan rolü hakkında detayları hatırlama imkanı verir, böylece etkileşimler daha akıcı ve odaklı hale gelir.

**Kişilik Belleği Örneği**

Eğer seyahat ajanı "uzman bir kayak planlayıcısı" olarak tasarlanmışsa, kişilik belleği bu rolü güçlendirebilir ve yanıtlarının bir uzmanın tonu ve bilgisiyle uyumlu olmasını sağlayabilir.

#### İş Akışı/Epizodik Bellek

Bu bellek, bir ajanın karmaşık bir görev sırasında izlediği adımların sırasını, başarılarını ve başarısızlıklarını saklar. Geçmişteki "bölümleri" veya deneyimleri hatırlayarak öğrenme sağlar.

**Epizodik Bellek Örneği**

Eğer ajan belirli bir uçuşu rezerve etmeye çalışmış ancak müsaitlik nedeniyle başarısız olmuşsa, epizodik bellek bu başarısızlığı kaydedebilir ve ajanın alternatif uçuşları denemesine veya sonraki bir girişimde kullanıcıyı daha bilgilendirici bir şekilde bilgilendirmesine olanak tanır.

#### Varlık Belleği

Bu, konuşmalardan belirli varlıkları (insanlar, yerler veya şeyler) ve olayları çıkarıp hatırlamayı içerir. Ajana tartışılan temel unsurların yapılandırılmış bir anlayışını oluşturma imkanı verir.

**Varlık Belleği Örneği**

Geçmiş bir seyahat hakkında yapılan bir konuşmadan, ajan "Paris," "Eiffel Kulesi," ve "Le Chat Noir restoranında akşam yemeği" gibi varlıkları çıkarabilir. Gelecekteki bir etkileşimde, ajan "Le Chat Noir"i hatırlayabilir ve orada yeni bir rezervasyon yapmayı teklif edebilir.

#### Yapılandırılmış RAG (Retrieval Augmented Generation)

RAG daha geniş bir teknik olsa da, "Yapılandırılmış RAG" güçlü bir bellek teknolojisi olarak öne çıkar. Konuşmalar, e-postalar, görüntüler gibi çeşitli kaynaklardan yoğun, yapılandırılmış bilgi çıkarır ve yanıtların doğruluğunu, hatırlama kapasitesini ve hızını artırır. Klasik RAG yalnızca anlamsal benzerliğe dayanırken, Yapılandırılmış RAG bilgilerin iç yapısıyla çalışır.

**Yapılandırılmış RAG Örneği**

Sadece anahtar kelimeleri eşleştirmek yerine, Yapılandırılmış RAG bir e-postadan uçuş detaylarını (varış yeri, tarih, saat, havayolu) ayrıştırabilir ve bunları yapılandırılmış bir şekilde saklayabilir. Bu, "Salı günü Paris'e hangi uçuşu rezerve ettim?" gibi kesin sorgulara olanak tanır.

## Belleği Uygulama ve Depolama

AI ajanları için bellek uygulamak, **bellek yönetimi** sürecini içerir. Bu süreç, bilgiyi oluşturma, depolama, geri çağırma, entegre etme, güncelleme ve hatta "unutma" (veya silme) işlemlerini kapsar. Geri çağırma özellikle kritik bir unsurdur.

### Özel Bellek Araçları

Ajan belleğini depolamak ve yönetmek için Mem0 gibi özel araçlar kullanabilirsiniz. Mem0, ajanların ilgili etkileşimleri hatırlamasına, kullanıcı tercihlerini ve gerçek bağlamı saklamasına ve zamanla başarı ve başarısızlıklardan öğrenmesine olanak tanıyan kalıcı bir bellek katmanı olarak çalışır. Buradaki fikir, durumsuz ajanların durumsal hale gelmesidir.

Mem0, **iki aşamalı bir bellek hattı: çıkarma ve güncelleme** üzerinden çalışır. Öncelikle, bir ajanın dizisine eklenen mesajlar Mem0 hizmetine gönderilir ve bu hizmet, bir Büyük Dil Modeli (LLM) kullanarak sohbet geçmişini özetler ve yeni anıları çıkarır. Daha sonra, LLM destekli bir güncelleme aşaması, bu anıları ekleyip eklememeye, değiştirmeye veya silmeye karar verir ve bunları vektör, grafik ve anahtar-değer veritabanlarını içerebilen hibrit bir veri deposunda saklar. Bu sistem ayrıca çeşitli bellek türlerini destekler ve varlıklar arasındaki ilişkileri yönetmek için grafik belleği içerebilir.

### RAG ile Bellek Depolama

Mem0 gibi özel bellek araçlarının ötesinde, **Azure AI Search gibi güçlü arama hizmetlerini bellekleri depolamak ve geri çağırmak için bir arka uç olarak kullanabilirsiniz**, özellikle yapılandırılmış RAG için.

Bu, ajanın yanıtlarını kendi verilerinizle temellendirmenizi sağlar ve daha alakalı ve doğru cevaplar sunar. Azure AI Search, kullanıcıya özel seyahat anılarını, ürün kataloglarını veya herhangi bir alanla ilgili bilgiyi depolamak için kullanılabilir.

Azure AI Search, **Yapılandırılmış RAG** gibi özellikleri destekler ve konuşma geçmişleri, e-postalar veya hatta görüntüler gibi büyük veri setlerinden yoğun, yapılandırılmış bilgi çıkarma ve geri çağırma konusunda mükemmeldir. Bu, geleneksel metin parçalama ve gömme yaklaşımlarına kıyasla "insanüstü doğruluk ve hatırlama" sağlar.

## AI Ajanlarını Kendini Geliştiren Hale Getirme

Kendini geliştiren ajanlar için yaygın bir model, bir **"bilgi ajanı"** tanıtmayı içerir. Bu ayrı ajan, kullanıcı ile ana ajan arasındaki konuşmayı gözlemler. Rolü şunları yapmaktır:

1. **Değerli bilgiyi belirleme**: Konuşmanın herhangi bir kısmının genel bilgi veya belirli bir kullanıcı tercihi olarak kaydedilmeye değer olup olmadığını belirleme.

2. **Çıkarma ve özetleme**: Konuşmadan temel öğrenimi veya tercihi damıtma.

3. **Bilgi tabanında saklama**: Çıkarılan bilgiyi, genellikle bir vektör veritabanında, daha sonra geri çağırılmak üzere kalıcı hale getirme.

4. **Gelecek sorguları destekleme**: Kullanıcı yeni bir sorgu başlattığında, bilgi ajanı ilgili saklanan bilgiyi geri çağırır ve bunu kullanıcının istemine ekler, ana ajana kritik bağlam sağlar (RAG'e benzer şekilde).

### Bellek için Optimizasyonlar

• **Gecikme Yönetimi**: Kullanıcı etkileşimlerini yavaşlatmamak için, bilgiyi saklamanın veya geri çağırmanın değerli olup olmadığını hızlıca kontrol etmek için daha ucuz ve hızlı bir model kullanılabilir. Daha karmaşık çıkarma/geri çağırma süreci yalnızca gerektiğinde devreye girer.

• **Bilgi Tabanı Bakımı**: Büyüyen bir bilgi tabanı için, daha az sıklıkla kullanılan bilgiler "soğuk depolama"ya taşınabilir, böylece maliyetler yönetilebilir.

## Ajan Belleği Hakkında Daha Fazla Sorunuz mu Var?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) topluluğuna katılarak diğer öğrenenlerle tanışabilir, ofis saatlerine katılabilir ve AI ajanlarıyla ilgili sorularınıza yanıt alabilirsiniz.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.