# AI Ajanları için Bellek 
[![Ajan Belleği](../../../translated_images/tr/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

AI Ajanları oluşturmanın benzersiz faydalarını tartışırken, genellikle iki şey üzerinde durulur: görevleri tamamlamak için araçları çağırabilme yeteneği ve zaman içinde gelişme yeteneği. Bellek, kullanıcılarımıza daha iyi deneyimler sunabilecek kendini geliştiren ajanlar oluşturmanın temelinde yatar.

Bu derste, AI Ajanları için belleğin ne olduğunu ve bunu uygulamalarımızın yararına nasıl yönetip kullanabileceğimizi inceleyeceğiz.

## Giriş

Bu ders şunları kapsayacak:

• **AI Ajan Belleğini Anlama**: Belleğin ne olduğu ve ajanlar için neden önemli olduğu.

• **Belleği Uygulama ve Depolama**: Kısa süreli ve uzun süreli belleğe odaklanarak AI ajanlarınıza bellek yetenekleri eklemek için pratik yöntemler.

• **AI Ajanlarını Kendini Geliştirir Hale Getirme**: Belleğin ajanların geçmiş etkileşimlerden öğrenmesini ve zaman içinde gelişmesini nasıl sağladığı.

## Mevcut Uygulamalar

Bu ders iki kapsamlı notebook eğitimi içerir:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Microsoft Agent Framework ile Mem0 ve Azure AI Search kullanarak belleği uygular

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Cognee kullanarak yapılandırılmış belleği uygular, gömülerle desteklenen bir bilgi grafiğini otomatik olarak oluşturur, grafiği görselleştirir ve akıllı getirme sağlar

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

• **Çalışma, kısa süreli ve uzun süreli bellek dahil olmak üzere çeşitli AI ajan bellek türlerini ayırt edebilmek**, ayrıca persona ve epizodik bellek gibi özel formları tanımak.

• **Microsoft Agent Framework kullanarak AI ajanları için kısa süreli ve uzun süreli belleği uygulayıp yönetebilmek**, Mem0, Cognee, Whiteboard bellek gibi araçlardan yararlanmak ve Azure AI Search ile entegrasyon sağlamak.

• **Kendini geliştiren AI ajanlarının arkasındaki ilkeleri anlamak** ve sağlam bellek yönetimi sistemlerinin sürekli öğrenme ve uyum sağlamaya nasıl katkıda bulunduğunu kavramak.

## AI Ajan Belleğini Anlamak

Özünde, **AI ajanları için bellek, onların bilgiyi saklamalarını ve hatırlamalarını sağlayan mekanizmalara atıfta bulunur**. Bu bilgi bir konuşmayla ilgili belirli ayrıntılar, kullanıcı tercihleri, geçmiş eylemler veya öğrenilmiş kalıplar olabilir.

Bellek olmadan, AI uygulamaları genellikle durumsuzdur (stateless); yani her etkileşim sıfırdan başlar. Bu, ajanın önceki bağlamı veya tercihleri "unuttuğu" tekrar eden ve sinir bozucu bir kullanıcı deneyimine yol açar.

### Bellek Neden Önemlidir?

Bir ajanın zekâsı, büyük ölçüde geçmiş bilgileri hatırlama ve kullanma yeteneğine bağlıdır. Bellek ajanların şunları yapmasına olanak tanır:

• **Düşünceli (Reflective)**: Geçmiş eylemlerden ve sonuçlardan öğrenme.

• **Etkileşimli (Interactive)**: Devam eden bir konuşma boyunca bağlamı koruma.

• **Proaktif ve Reaktif**: Tarihsel verilere dayanarak ihtiyaçları öngörme veya uygun şekilde yanıt verme.

• **Otonom**: Saklı bilgiden yararlanarak daha bağımsız çalışabilme.

Belleği uygulamanın amacı, ajanları daha **güvenilir ve yetenekli** hale getirmektir.

### Bellek Türleri

#### Çalışma Belleği

Bunu, bir ajanın tek bir devam eden görev veya düşünce süreci sırasında kullandığı bir not kâğıdı olarak düşünün. Bir sonraki adımı hesaplamak için gereken anlık bilgiyi tutar.

AI ajanları için çalışma belleği genellikle bir konuşmadan en alakalı bilgileri yakalar, konuşma geçmişi uzun veya kırpılmış olsa bile. Gereksinimler, teklif önerileri, kararlar ve eylemler gibi ana unsurları çıkarmaya odaklanır.

**Çalışma Belleği Örneği**

Bir seyahat rezervasyon ajanında, çalışma belleği kullanıcının mevcut isteğini yakalayabilir; örneğin "Paris'e bir gezi rezervasyonu yapmak istiyorum". Bu belirli gereksinim, mevcut etkileşimi yönlendirmek için ajanın anlık bağlamında tutulur.

#### Kısa Süreli Bellek

Bu bellek türü bir konuşma veya oturum süresince bilgiyi tutar. Mevcut sohbetin bağlamıdır ve ajanın diyaloğun önceki turlarına atıfta bulunmasını sağlar.

**Kısa Süreli Bellek Örneği**

Eğer bir kullanıcı "Paris'e bir uçak bileti ne kadar olur?" diye sorup sonra "Peki konaklama ne olacak?" diye devam ederse, kısa süreli bellek ajanın aynı konuşma içinde "orada"nın "Paris"i ifade ettiğini bilmesini sağlar.

#### Uzun Süreli Bellek

Bu, birden çok konuşma veya oturum boyunca devam eden bilgilerdir. Kullanıcı tercihlerini, geçmiş etkileşimleri veya uzun süreli genel bilgileri hatırlamayı sağlar. Kişiselleştirme için önemlidir.

**Uzun Süreli Bellek Örneği**

Uzun süreli bir bellek, "Ben kayak ve açık hava etkinliklerinden hoşlanır, dağ manzaralı kahve sever ve geçmişteki bir yaralanma nedeniyle ileri seviye kayak pistlerinden kaçınmak ister" gibi bilgiyi depolayabilir. Bu bilgi, gelecekteki seyahat planlama oturumlarında tavsiyeleri etkiler ve onları son derece kişiselleştirir.

#### Persona Belleği

Bu özel bellek türü bir ajanın tutarlı bir "kişilik" veya "persona" geliştirmesine yardımcı olur. Ajanın kendisi veya rolü hakkında ayrıntıları hatırlamasına olanak tanır ve etkileşimleri daha akıcı ve odaklı hale getirir.

**Persona Belleği Örneği**
Eğer seyahat ajanı "uzman kayak planlayıcısı" olarak tasarlanmışsa, persona belleği bu rolü pekiştirebilir ve cevaplarının bir uzmanın tonuna ve bilgisine uygun olmasını etkileyebilir.

#### İş Akışı/Episodik Bellek

Bu bellek, bir ajanın karmaşık bir görev sırasında attığı adımların sırasını, başarılarını ve hatalarını depolar. Bunu belirli "epizodları" veya geçmiş deneyimleri hatırlamak gibi düşünebilirsiniz.

**Episodik Bellek Örneği**

Eğer ajan belirli bir uçuşu rezerve etmeye çalıştı ama müsait olmama nedeniyle başarısız olduysa, epizodik bellek bu hatayı kaydedebilir; böylece ajan sonraki bir denemede alternatif uçuşları denemek veya kullanıcıyı daha bilgili bir şekilde bilgilendirmek için bu kaydı kullanabilir.

#### Varlık Belleği

Bu, konuşmalardan belirli varlıkları (kişi, yer veya nesne gibi) ve olayları çıkarıp hatırlamayı içerir. Ajanın konuşulan ana öğelerin yapılandırılmış bir anlayışını oluşturmasına izin verir.

**Varlık Belleği Örneği**

Geçmiş bir geziyle ilgili bir konuşmadan ajan "Paris", "Eyfel Kulesi" ve "Le Chat Noir restoranında akşam yemeği" gibi varlıkları çıkarabilir. Gelecekteki bir etkileşimde ajan "Le Chat Noir"u hatırlayıp orada yeni bir rezervasyon yapmayı teklif edebilir.

#### Yapılandırılmış RAG (Retrieval Augmented Generation)

RAG daha geniş bir teknik olsa da, "Yapılandırılmış RAG" güçlü bir bellek teknolojisi olarak vurgulanır. Konuşmalar, e-postalar, görüntüler gibi çeşitli kaynaklardan yoğun, yapılandırılmış bilgiyi çıkarır ve yanıtların doğruluğunu, geri çağırma yeteneğini ve hızını artırmak için kullanır. Klasik RAG yalnızca anlamsal benzerliğe dayanırken, Yapılandırılmış RAG bilgilerin içsel yapısıyla çalışır.

**Yapılandırılmış RAG Örneği**

Sadece anahtar kelime eşleştirmesi yapmak yerine, Yapılandırılmış RAG bir e-postadan uçuş detaylarını (varış yeri, tarih, saat, havayolu) ayrıştırıp bunları yapılandırılmış bir şekilde depolayabilir. Bu, "Salı günü Paris'e hangi uçuşu ayırttım?" gibi kesin sorgulara olanak tanır.

## Belleği Uygulama ve Depolama

AI ajanları için bellek uygulamak, **bellek yönetimi**nin sistematik bir sürecini içerir; bu süreç bilgiyi oluşturma, depolama, alma, entegre etme, güncelleme ve hatta "unutma" (veya silme) adımlarını kapsar. Alma (retrieval) özellikle kritik bir unsurdur.

### Özelleşmiş Bellek Araçları

#### Mem0

Ajan belleğini depolamak ve yönetmek için kullanılan bir yol, Mem0 gibi özelleşmiş araçlardır. Mem0, ajanların ilgili etkileşimleri hatırlamasına, kullanıcı tercihlerini ve gerçek bağlamı depolamasına ve zaman içinde başarılarından ve hatalarından öğrenmesine olanak tanıyan kalıcı bir bellek katmanı olarak çalışır. Buradaki fikir, durumsuz ajanların durumsal hale gelmesidir.

Bu sistem, **iki aşamalı bir bellek hattı: çıkarım ve güncelleme** yoluyla çalışır. Önce, bir ajanın dizisine eklenen mesajlar Mem0 hizmetine gönderilir; Mem0, konuşma geçmişini özetlemek ve yeni anıları çıkarmak için bir Büyük Dil Modeli (LLM) kullanır. Ardından, LLM destekli bir güncelleme aşaması, bu anıların eklenip eklenmeyeceğini, değiştirilip değiştirilmeyeceğini veya silinip silinmeyeceğini belirler ve bunları vektör, grafik ve anahtar-değer veritabanlarını içerebilecek hibrit bir veri deposunda saklar. Bu sistem ayrıca çeşitli bellek türlerini destekler ve varlıklar arasındaki ilişkileri yönetmek için grafik belleğini entegre edebilir.

#### Cognee

Başka güçlü bir yaklaşım, yapılandırılmış ve yapılandırılmamış verileri gömülerle desteklenen sorgulanabilir bilgi grafikleri haline dönüştüren açık kaynaklı bir semantik bellek olan **Cognee** kullanmaktır. Cognee, vektör benzerlik aramasını grafik ilişkileriyle birleştiren bir **çift depolama mimarisi** sunar; bu, ajanların yalnızca hangi bilgilerin benzer olduğunu değil, kavramların birbirleriyle nasıl ilişkili olduğunu da anlamasına olanak tanır.

Cognee, ham parça aramadan grafik farkındalıklı soru-cevaplamaya kadar vektör benzerliği, grafik yapısı ve LLM muhakemesini harmanlayan **karma alma (hybrid retrieval)** konusunda üstündür. Sistem, kısa süreli oturum bağlamını ve uzun süreli kalıcı belleği destekleyen, sorgulanabilir ve sürekli gelişen bir "canlı bellek"i tek bir bağlı grafik olarak sürdürür.

Cognee notebook eğitimi ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) bu birleşik bellek katmanını oluşturmayı gösterir; çeşitli veri kaynaklarını içeri aktarma, bilgi grafiğini görselleştirme ve farklı ajan ihtiyaçlarına uygun farklı arama stratejileriyle sorgulama konusunda pratik örnekler sunar.

### RAG ile Bellek Depolama

mem0 gibi özelleşmiş bellek araçlarının ötesinde, özellikle yapılandırılmış RAG için bellekleri depolamak ve almak için arka uç olarak **Azure AI Search** gibi güçlü arama hizmetlerinden yararlanabilirsiniz.

Bu, ajanın yanıtlarını kendi verilerinizle desteklemenize olanak tanır ve daha alakalı ve doğru yanıtlar sağlar. Azure AI Search, konuşma geçmişleri, e-postalar veya hatta görüntüler gibi büyük veri kümelerinden yoğun, yapılandırılmış bilgiyi çıkarmada ve elde etmede başarı sağlayan **Yapılandırılmış RAG** gibi yetenekleri destekler. Bu, geleneksel metin parçalama ve gömü yaklaşımlarına kıyasla "insanüstü hassasiyet ve geri çağırma" sağlar.

## AI Ajanlarının Kendini Geliştirmesini Sağlama

Kendini geliştiren ajanlar için yaygın bir desen, bir **"bilgi ajanı"** (knowledge agent) tanımlamaktır. Bu ayrı ajan, kullanıcı ile birincil ajan arasındaki ana konuşmayı gözlemler. Rolü şunlardır:

1. **Değerli bilgiyi belirlemek**: Konuşmanın herhangi bir bölümünün genel bilgi veya belirli bir kullanıcı tercihi olarak kaydedilmeye değer olup olmadığını tespit etmek.

2. **Çıkarmak ve özetlemek**: Konuşmadan temel öğrenmeyi veya tercihi damıtmak.

3. **Bilgi tabanına kaydetmek**: Bu çıkarılan bilgiyi genellikle bir vektör veritabanında kalıcı hale getirmek, böylece daha sonra alınabilmesini sağlamak.

4. **Gelecekteki sorguları güçlendirmek**: Kullanıcı yeni bir sorgu başlattığında, bilgi ajanı ilgili saklanan bilgileri alır ve bunları kullanıcının prompt'una ekler; böylece birincil ajana kritik bağlam sağlanır (RAG benzeri).

### Bellek İçin Optimizasyonlar

• **Gecikme Yönetimi**: Kullanıcı etkileşimlerini yavaşlatmamak için, başlangıçta bilgiyi hızlıca depolamaya veya almaya değer olup olmadığını kontrol etmek için daha ucuz ve daha hızlı bir model kullanılabilir; yalnızca gerektiğinde daha karmaşık çıkarım/erişim süreci çağrılır.

• **Bilgi Tabanı Bakımı**: Büyüyen bir bilgi tabanı için daha az kullanılan bilgiler maliyetleri yönetmek amacıyla "soğuk depolamaya" (cold storage) taşınabilir.

## Ajan Belleği Hakkında Daha Fazla Sorunuz Mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanlarıyla ilgili sorularınızı yanıtlatmak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) topluluğuna katılın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Feragatname:
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya eksiklikler içerebileceğini lütfen unutmayın. Belgenin özgün diliyle yazılmış hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanılması sonucu ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->