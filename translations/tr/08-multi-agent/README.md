[![Çoklu Temsilci Tasarımı](../../../translated_images/tr/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Dersi izlemek için yukarıdaki görsele tıklayın)_

# Çoklu Temsilci Tasarım Kalıpları

Birden çok temsilci içeren bir projede çalışmaya başlar başlamaz, çoklu temsilci tasarım kalıbını dikkate almanız gerekir. Ancak, ne zaman çoklu temsilcilere geçileceği ve avantajlarının neler olduğu hemen net olmayabilir.

## Giriş

Bu derste şu sorulara cevap arıyoruz:

- Çoklu temsilcilerin uygulanabilir olduğu senaryolar nelerdir?
- Tek bir temsilciye göre çoklu temsilci kullanmanın avantajları nelerdir?
- Çoklu temsilci tasarım kalıbını uygulamanın yapı taşları nelerdir?
- Birden çok temsilcinin nasıl birbirleriyle etkileşimde bulunduğunu nasıl görebiliriz?

## Öğrenme Hedefleri

Bu dersten sonra şunları yapabilmelisiniz:

- Çoklu temsilci uygulamalarının uygun olduğu senaryoları belirlemek
- Tek bir temsilciye kıyasla çoklu temsilci kullanımının avantajlarını tanımak
- Çoklu temsilci tasarım kalıbının yapı taşlarını kavramak

Daha geniş resim nedir?

*Çoklu temsilciler, birden fazla temsilcinin ortak bir amacı gerçekleştirmek üzere birlikte çalışmasına olanak tanıyan bir tasarım kalıbıdır*.

Bu kalıp, robotik, otonom sistemler ve dağıtık bilişim gibi çeşitli alanlarda yaygın olarak kullanılmaktadır.

## Çoklu Temsilcilerin Uygulanabilir Olduğu Senaryolar

Peki, çoklu temsilci kullanımı için iyi olan senaryolar nelerdir? Cevap, özellikle aşağıdaki durumlarda birden fazla temsilci kullanmanın faydalı olduğu pek çok senaryonun olduğudur:

- **Büyük iş yükleri**: Büyük iş yükleri daha küçük görevlere bölünüp farklı temsilcilere atanabilir; böylece paralel işlem yapılır ve tamamlanma daha hızlı olur. Bunu iyi örnekleyen durum büyük bir veri işleme görevidir.
- **Karmaşık görevler**: Büyük iş yüklerinde olduğu gibi karmaşık görevler de daha küçük alt görevlere ayrılabilir ve her biri görevin belirli bir yönünde uzmanlaşmış temsilcilere atanabilir. Örneğin, otonom araçlarda farklı temsilciler navigasyon, engel tespiti ve araçlar arası iletişimi yönetir.
- **Çeşitli uzmanlıklar**: Farklı temsilciler farklı uzmanlıklara sahip olabilir, böylece tek bir temsilciden daha etkili bir şekilde görevin farklı yönlerini ele alabilirler. Bu duruma iyi bir örnek sağlık sektöründe, temsilcilerin teşhis, tedavi planları ve hasta takibini yönetmesidir.

## Tek Bir Temsilciye Göre Çoklu Temsilci Kullanmanın Avantajları

Tek bir temsilci sistemi basit görevler için iyi çalışabilir, ancak daha karmaşık görevlerde çoklu temsilciler kullanmak çeşitli avantajlar sağlar:

- **Uzmanlaşma**: Her temsilci belirli bir görev için uzmanlaşabilir. Tek bir temsilcide uzmanlaşma eksikliği, temsilcinin her şeyi yapabilmesi ama karmaşık bir görevle karşılaştığında ne yapacağını karıştırabilmesi anlamına gelir. Örneğin, en uygun olmadığı bir görevi yapmak zorunda kalabilir.
- **Ölçeklenebilirlik**: Tek bir temsilciyi aşırı yüklemek yerine daha fazla temsilci ekleyerek sistemleri ölçeklendirmek daha kolaydır.
- **Hata Toleransı**: Bir temsilci arızalanırsa diğerleri çalışmaya devam edebilir; böylece sistem güvenilirliği sağlanır.

Bir örnek alalım, bir kullanıcı için seyahat rezervasyonu yapalım. Tek bir temsilci sistemi, uçuş bulmaktan otel ve araç kiralama rezervasyonuna kadar seyahat rezervasyonu sürecinin tüm yönlerini ele almak zorunda kalır. Tek bir temsilcide tüm bu görevleri yönetmek için araçlar bulunmalıdır. Bu durum bakımı ve ölçeklendirmesi zor karmaşık ve tek parça bir sistem yaratabilir. Buna karşılık çoklu temsilci sisteminde, farklı temsilciler uçuş bulma, otel ve araç kiralama rezervasyonunda uzmanlaşabilir. Bu da sistemi daha modüler, bakımı kolay ve ölçeklenebilir yapar.

Bunu, tek bir dükkan olarak işletilen bir seyahat bürosuyla, franchise olarak işletilen bir seyahat bürosunu karşılaştırmaya benzetebilirsiniz. Tek dükkanda bir temsilci seyahat rezervasyonunun tüm yönlerini yönetirken, franchise'da farklı temsilciler rezervasyon sürecinin farklı yönleriyle ilgilenir.

## Çoklu Temsilci Tasarım Kalıbını Uygulamanın Yapı Taşları

Çoklu temsilci tasarım kalıbını uygulamadan önce, kalıbı oluşturan yapı taşlarını anlamalısınız.

Bunu daha somut hale getirmek için tekrar bir kullanıcının seyahat rezervasyon örneğine bakalım. Bu durumda yapı taşları şunları içerebilir:

- **Temsilciler Arası İletişim**: Uçuş arama, otel ve araç kiralama rezervasyonu temsilcileri, kullanıcının tercihleri ve kısıtlamaları hakkında bilgi paylaşmak için iletişim kurmalıdır. Bu iletişim protokolleri ve yöntemleri belirlenmelidir. Örneğin, uçuş arayan temsilci, otel rezervasyon temsilcisiyle aynı tarihlerde otel rezervasyonu yapılmasını sağlamak için iletişim kurmalıdır. Bu da temsilcilerin *hangi bilgileri paylaştığı ve nasıl paylaştığına* karar vermeniz gerektiği anlamına gelir.
- **Koordinasyon Mekanizmaları**: Temsilciler, kullanıcının tercih ve kısıtlamalarının karşılandığından emin olmak için hareketlerini koordine etmelidir. Kullanıcının tercihi havaalanına yakın bir otel isterken, kısıtlama araba kiralama hizmetinin sadece havalimanında bulunması olabilir. Bu durumda otel rezervasyon temsilcisi, araba kiralama temsilcisiyle koordinasyon sağlamalıdır. Bu da temsilcilerin *nasıl koordinasyon sağladıklarını* belirlemeniz gerektiği anlamına gelir.
- **Temsilci Mimarisi**: Temsilcilerin, kullanıcının tercihleriyle etkileşimlerinden öğrenmek ve karar vermek için iç yapıya sahip olmaları gerekir. Örneğin uçuş arama temsilcisi, kullanıcıya hangi uçuşları önereceğine karar vermek için iç yapıya sahip olmalıdır. Bu, temsilcilerin *kullanıcıyla etkileşimlerinden nasıl karar verdiklerini ve öğrendiklerini* belirlemeniz gerektiği anlamına gelir. Örneğin, geçmiş tercihlere dayanarak uçuşları önermek için makine öğrenimi modeli kullanılabilir.
- **Çoklu Temsilci Etkileşimleri Görünürlüğü**: Birden çok temsilcinin nasıl etkileşimde bulunduğunu görebilmeniz gerekir. Bu, temsilci faaliyetlerini ve etkileşimlerini izlemek için araçlar ve teknikler gerektirir. Loglama, izleme araçları, görselleştirme araçları ve performans ölçütleri buna örnektir.
- **Çoklu Temsilci Kalıpları**: Çoklu temsilci sistemler için merkezi, merkezi olmayan ve hibrit mimariler gibi farklı kalıplar vardır. Kullanım durumunuza en uygun kalıbı seçmelisiniz.
- **İnsan döngüde**: Çoğu durumda, izne ihtiyaç duyulduğunda insan müdahalesinin ne zaman isteneceğine ilişkin talimat vermeniz gerekir. Bu, ajanların önermediği belirli bir otel veya uçuşun kullanıcının istemesi ya da rezervasyon öncesi onay talebi şeklinde olabilir.

## Çoklu Temsilci Etkileşimlerini Görme

Birden çok temsilcinin nasıl etkileşimde bulunduğunu görmeniz önemlidir. Bu görünürlük, hata ayıklama, optimizasyon ve genel sistem etkinliği için gereklidir. Bunu sağlamak için temsilci faaliyetleri ve etkileşimleri izlemek için araçlar ve tekniklere ihtiyacınız vardır. Bu, loglama ve izleme araçları, görselleştirme araçları ve performans ölçütleri şeklinde olabilir.

Örneğin, bir kullanıcının seyahat rezervasyonu durumunda, her temsilcinin durumu, kullanıcının tercih ve kısıtlamaları ile temsilciler arasındaki etkileşimleri gösteren bir kontrol paneli olabilir. Bu panel, kullanıcının seyahat tarihlerini, uçuş temsilcisinin önerdiği uçuşları, otel temsilcisinin önerdiği otelleri ve araç kiralama temsilcisinin önerdiği araçları gösterebilir. Böylece temsilcilerin nasıl etkileşimde bulunduğunu ve kullanıcının tercih ve kısıtlamalarının karşılanıp karşılanmadığını açıkça görebilirsiniz.

Bunların her bir yönüne daha detaylı bakalım.

- **Loglama ve İzleme Araçları**: Her temsilcinin gerçekleştirdiği her eylemin loglanmasını istersiniz. Bir log kaydı, eylemi gerçekleştiren temsilci, yapılan eylem, eylemin gerçekleştiği zaman ve eylemin sonucu hakkında bilgiler içerebilir. Bu bilgiler hata ayıklama, optimizasyon ve diğer amaçlar için kullanılabilir.

- **Görselleştirme Araçları**: Görselleştirme araçları, temsilciler arasındaki etkileşimleri daha sezgisel görmenize yardımcı olabilir. Örneğin, temsilciler arasındaki bilgi akışını gösteren bir grafik olabilirdi. Bu, sistemdeki darboğazlar, verimsizlikler ve diğer sorunları tespit etmeye yardımcı olabilir.

- **Performans Ölçütleri**: Performans ölçütleri, çoklu temsilci sistemin etkinliğini izlemenize yardımcı olabilir. Örneğin, bir görevin tamamlanma süresi, birim zamanda tamamlanan görev sayısı ve temsilcilerin yaptığı önerilerin doğruluğu gibi. Bu bilgiler, iyileştirme alanlarını belirleyip sistemi optimize etmekte fayda sağlar.

## Çoklu Temsilci Kalıpları

Çoklu temsilci uygulamaları oluşturmak için kullanabileceğimiz bazı somut kalıplara bakalım. İşte dikkate alınmaya değer bazı ilginç kalıplar:

### Grup sohbeti

Bu kalıp, birden fazla temsilcinin birbirleriyle iletişim kurabildiği bir grup sohbet uygulaması oluşturmak istediğinizde kullanışlıdır. Tipik kullanım alanları takım işbirliği, müşteri desteği ve sosyal ağlardır.

Bu kalıpta, her temsilci grup sohbette bir kullanıcıyı temsil eder ve mesajlar mesajlaşma protokolü kullanılarak temsilciler arasında iletilir. Temsilciler grup sohbetine mesaj gönderebilir, grup sohbetinden mesaj alabilir ve diğer temsilcilerin mesajlarına yanıt verebilir.

Bu kalıp, tüm mesajların merkezi bir sunucu üzerinden yönlendirildiği merkezi mimari veya mesajların doğrudan alışverişi yapılan merkezi olmayan mimari ile uygulanabilir.

![Grup sohbeti](../../../translated_images/tr/multi-agent-group-chat.ec10f4cde556babd.webp)

### Görev devri

Bu kalıp, birden fazla temsilcinin görevleri birbirlerine devredebileceği bir uygulama oluşturmak istediğinizde kullanışlıdır.

Bu kalıba tipik senaryolar müşteri desteği, görev yönetimi ve iş akışı otomasyonudur.

Bu kalıpta, her temsilci bir görev ya da iş akışındaki bir adımı temsil eder ve temsilciler önceden tanımlanmış kurallara göre görevleri diğer temsilcilere devredebilir.

![Görev devri](../../../translated_images/tr/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### İş birliğine dayalı filtreleme

Bu kalıp, birden fazla temsilcinin iş birliği yaparak kullanıcılar için önerilerde bulunacağı bir uygulama oluşturmak istediğinizde kullanışlıdır.

Çoklu temsilcilerin iş birliği yapmasının nedeni, her temsilcinin farklı uzmanlık alanlarına sahip olması ve öneri sürecine farklı şekillerde katkıda bulunabilmesidir.

Örneğin, bir kullanıcının borsada en iyi hisse senedine yönelik öneri istediği duruma bakalım.

- **Sektör uzmanı**: Bir temsilci belirli bir sektörde uzmandır.
- **Teknik analiz**: Diğer bir temsilci teknik analiz konusunda uzmandır.
- **Temel analiz**: Bir diğer temsilci ise temel analiz konusunda uzmandır. Bu temsilciler iş birliği yaparak kullanıcılara daha kapsamlı öneriler sunabilir.

![Öneri](../../../translated_images/tr/multi-agent-filtering.d959cb129dc9f608.webp)

## Senaryo: İade süreci

Bir müşterinin ürün iadesi talebinde bulunduğu bir senaryoyu düşünün, bu süreçte pek çok temsilci yer alabilir ancak süreci, iade sürecine özgü temsilciler ve diğer süreçlerde de kullanılabilen genel temsilciler arasında bölelim.

**İade sürecine özgü temsilciler**:

İşte iade sürecinde yer alabilecek bazı temsilciler:

- **Müşteri temsilcisi**: Bu temsilci müşteriyi temsil eder ve iade sürecini başlatmaktan sorumludur.
- **Satıcı temsilcisi**: Bu temsilci satıcıyı temsil eder ve iadeyi işler.
- **Ödeme temsilcisi**: Bu temsilci ödeme sürecini temsil eder ve müşterinin ödemesini iade etmekten sorumludur.
- **Çözüm temsilcisi**: Bu temsilci çözüm sürecini temsil eder ve iade sürecinde ortaya çıkabilecek sorunları çözmekten sorumludur.
- **Uyum temsilcisi**: Bu temsilci uyum sürecini temsil eder ve iade sürecinin düzenlemelere ve politikalara uygun olmasını sağlar.

**Genel temsilciler**:

Bu temsilciler, işinizin diğer bölümlerinde de kullanılabilir.

- **Nakliye temsilcisi**: Bu temsilci nakliye sürecini temsil eder ve ürünü satıcıya geri göndermekten sorumludur. Bu temsilci hem iade sürecinde hem de örneğin ürün satın alma durumundaki genel nakliyede kullanılabilir.
- **Geri bildirim temsilcisi**: Bu temsilci geri bildirim sürecini temsil eder ve müşteriden geri bildirim toplamaktan sorumludur. Geri bildirim her zaman, sadece iade sürecinde değil, alınabilir.
- **Yükseltme temsilcisi**: Bu temsilci yükseltme sürecini temsil eder ve destek sorunlarını daha üst seviyeye taşımakla sorumludur. Bu tür bir temsilci, herhangi bir süreçte sorun yükseltmeniz gerektiğinde kullanılabilir.
- **Bildirim temsilcisi**: Bu temsilci bildirim sürecini temsil eder ve iade sürecinin çeşitli aşamalarında müşteriye bildirimler gönderir.
- **Analitik temsilcisi**: Bu temsilci analitik süreci temsil eder ve iade süreciyle ilgili verileri analiz etmekten sorumludur.
- **Denetim temsilcisi**: Bu temsilci denetim sürecini temsil eder ve iade sürecinin doğru şekilde yürütüldüğünden emin olmak için denetim yapar.
- **Raporlama temsilcisi**: Bu temsilci raporlama sürecini temsil eder ve iade süreci hakkında raporlar hazırlar.
- **Bilgi temsilcisi**: Bu temsilci bilgi sürecini temsil eder ve iade süreciyle ilgili bilgi tabanını yönetir. Bu temsilci hem iadeler hem de işinizin diğer bölümleri hakkında bilgi sahibi olabilir.
- **Güvenlik temsilcisi**: Bu temsilci güvenlik sürecini temsil eder ve iade sürecinin güvenliğini sağlar.
- **Kalite temsilcisi**: Bu temsilci kalite sürecini temsil eder ve iade sürecinin kalitesini sağlar.

Önceki satırlarda, hem iade sürecine özgü hem de işinizin diğer bölümlerinde kullanılabilen genel temsilciler için oldukça fazla temsilci listelenmiştir. Umarım bu, çoklu temsilci sisteminizde hangi temsilcileri kullanacağınıza karar vermeniz konusunda size bir fikir verir.

## Ödev

Bir müşteri destek süreci için çoklu temsilci sistemi tasarlayın. Süreçte yer alan temsilcileri, rollerini ve sorumluluklarını ve birbirleriyle nasıl etkileşimde bulunduklarını belirleyin. Hem müşteri destek sürecine özgü temsilcileri hem de işinizin diğer bölümlerinde kullanılabilen genel temsilcileri göz önünde bulundurun.


> Aşağıdaki çözümü okumadan önce bir düşünün, düşündüğünüzden daha fazla ajan gerekebilir.

> İPUCU: Müşteri destek sürecinin farklı aşamalarını düşünün ve ayrıca herhangi bir sistem için gereken ajanları göz önünde bulundurun.

## Çözüm

[Çözüm](./solution/solution.md)

## Bilgi Kontrolleri

### Soru 1

Çok ajanlı sistem için en uygun senaryo hangisidir?

- [ ] A1: Bir destek botu, tek bir bilgi tabanı ve küçük araç setiyle yaygın soruları yanıtlar.
- [ ] A2: Bir geri ödeme iş akışı, her biri kendi araçlarına sahip ayrı sahtekarlık, ödeme ve uyumluluk rolleri gerektirir ve sonuçlar koordine edilmelidir.
- [ ] A3: Aynı basit sınıflandırma isteği saatte binlerce kez gelmektedir.

### Soru 2

Tek bir ajan genellikle ne zaman daha iyi bir tercihtir?

- [ ] A1: Görev, uzman geçişi olmadan bir talimat ve araç seti ile yönetilebilir.
- [ ] A2: Ajanın birden fazla araca erişimi vardır.
- [ ] A3: İş akışı, farklı izinlere ve bağımsız denetim izlerine sahip ayrı roller gerektirir.

[Çözüm sınavı](./solution/solution-quiz.md)

## Özet

Bu derste, çok ajanlı tasarım deseni, çok ajanların uygulanabilir olduğu senaryolar, tek bir ajana göre çok ajan kullanmanın avantajları, çok ajanlı tasarım deseninin kurucu blokları ve çoklu ajanların birbirleriyle nasıl etkileşime geçtiğine dair görünürlük sahibi olma konularını inceledik.

### Çok Ajanlı Tasarım Deseni Hakkında Daha Fazla Sorunuz Mu Var?

Diğer öğrenenlerle tanışmak, danışma saatlerine katılmak ve AI Ajanları sorularınıza yanıt almak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) topluluğuna katılın.

## Ek Kaynaklar

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework dokümantasyonu</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentic tasarım desenleri</a>


## Önceki Ders

[Planlama Tasarımı](../07-planning-design/README.md)

## Sonraki Ders

[AI Ajanlarında Metabiliş](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->