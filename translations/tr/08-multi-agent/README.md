<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T13:11:44+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "tr"
}
-->
[![Çoklu Ajan Tasarımı](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.tr.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Çoklu Ajan Tasarım Kalıpları

Birden fazla ajanın yer aldığı bir projede çalışmaya başladığınızda, çoklu ajan tasarım kalıbını dikkate almanız gerekecektir. Ancak, çoklu ajanlara ne zaman geçmeniz gerektiği ve bunun avantajlarının neler olduğu hemen net olmayabilir.

## Giriş

Bu derste şu sorulara cevap arıyoruz:

- Çoklu ajanların uygulanabilir olduğu senaryolar nelerdir?
- Çoklu ajanlar kullanmanın, birden fazla görevi yerine getiren tek bir ajan kullanmaya göre avantajları nelerdir?
- Çoklu ajan tasarım kalıbını uygulamanın yapı taşları nelerdir?
- Birden fazla ajanın birbirleriyle nasıl etkileşimde bulunduğunu nasıl görebiliriz?

## Öğrenme Hedefleri

Bu dersin ardından şunları yapabileceksiniz:

- Çoklu ajanların uygulanabilir olduğu senaryoları belirlemek.
- Çoklu ajanlar kullanmanın, tek bir ajana kıyasla avantajlarını tanımak.
- Çoklu ajan tasarım kalıbını uygulamanın yapı taşlarını anlamak.

Peki büyük resim nedir?

*Çoklu ajanlar, birden fazla ajanın ortak bir hedefe ulaşmak için birlikte çalışmasını sağlayan bir tasarım kalıbıdır.*

Bu kalıp, robotik, otonom sistemler ve dağıtık hesaplama gibi çeşitli alanlarda yaygın olarak kullanılmaktadır.

## Çoklu Ajanların Uygulanabilir Olduğu Senaryolar

Peki, çoklu ajanların iyi bir kullanım alanı olduğu senaryolar nelerdir? Cevap, çok sayıda senaryonun olduğudur, özellikle şu durumlarda çoklu ajanlar kullanmak faydalıdır:

- **Büyük iş yükleri**: Büyük iş yükleri daha küçük görevlere bölünebilir ve farklı ajanlara atanabilir, bu da paralel işlemeyi ve daha hızlı tamamlamayı sağlar. Bunun bir örneği, büyük bir veri işleme görevidir.
- **Karmaşık görevler**: Karmaşık görevler, büyük iş yükleri gibi, daha küçük alt görevlere bölünebilir ve her biri görevin belirli bir yönünde uzmanlaşmış farklı ajanlara atanabilir. Bunun iyi bir örneği, otonom araçlardır; burada farklı ajanlar navigasyonu, engel algılamayı ve diğer araçlarla iletişimi yönetir.
- **Çeşitli uzmanlıklar**: Farklı ajanlar, bir görevin farklı yönlerini tek bir ajandan daha etkili bir şekilde ele alabilmelerini sağlayan çeşitli uzmanlıklara sahip olabilir. Bunun iyi bir örneği, sağlık sektörüdür; burada ajanlar teşhis, tedavi planları ve hasta takibini yönetebilir.

## Çoklu Ajanlar Kullanmanın Tek Bir Ajana Göre Avantajları

Tek bir ajan sistemi basit görevler için iyi çalışabilir, ancak daha karmaşık görevler için birden fazla ajan kullanmak birkaç avantaj sağlayabilir:

- **Uzmanlaşma**: Her ajan belirli bir görev için uzmanlaşabilir. Tek bir ajanın uzmanlaşmaması, her şeyi yapabilen ancak karmaşık bir görevle karşılaştığında ne yapacağını şaşırabilecek bir ajana sahip olmanız anlamına gelir. Örneğin, en iyi yapamayacağı bir görevi yerine getirmeye çalışabilir.
- **Ölçeklenebilirlik**: Sistemleri, tek bir ajanı aşırı yüklemek yerine daha fazla ajan ekleyerek ölçeklendirmek daha kolaydır.
- **Hata Toleransı**: Bir ajan başarısız olursa, diğerleri çalışmaya devam edebilir ve sistemin güvenilirliğini sağlar.

Bir örnek üzerinden düşünelim: Bir kullanıcı için bir seyahat rezervasyonu yapalım. Tek bir ajan sistemi, seyahat rezervasyon sürecinin tüm yönlerini ele almak zorunda kalacaktır; uçuş bulmaktan otel ve araç kiralamaya kadar. Bunu tek bir ajanla başarmak için, ajanın tüm bu görevleri yerine getirebilecek araçlara sahip olması gerekir. Bu, bakımı ve ölçeklendirilmesi zor olan karmaşık ve tek parça bir sisteme yol açabilir. Öte yandan, çoklu ajan sistemi, uçuş bulma, otel rezervasyonu ve araç kiralama konusunda uzmanlaşmış farklı ajanlara sahip olabilir. Bu, sistemi daha modüler, bakımı daha kolay ve ölçeklenebilir hale getirir.

Bunu, bir aile işletmesi olarak yönetilen bir seyahat bürosu ile bir franchise olarak yönetilen bir seyahat bürosu arasında karşılaştırabilirsiniz. Aile işletmesi, seyahat rezervasyon sürecinin tüm yönlerini ele alan tek bir ajana sahip olacaktır, oysa franchise, sürecin farklı yönlerini ele alan farklı ajanlara sahip olacaktır.

## Çoklu Ajan Tasarım Kalıbını Uygulamanın Yapı Taşları

Çoklu ajan tasarım kalıbını uygulamadan önce, kalıbı oluşturan yapı taşlarını anlamanız gerekir.

Bir kullanıcı için seyahat rezervasyonu yapma örneğine tekrar bakarak bunu somutlaştıralım. Bu durumda, yapı taşları şunları içerecektir:

- **Ajan İletişimi**: Uçuş bulma, otel rezervasyonu ve araç kiralama ajanlarının, kullanıcının tercihleri ve kısıtlamaları hakkında bilgi paylaşması ve iletişim kurması gerekir. Bu iletişim için protokolleri ve yöntemleri belirlemeniz gerekir. Bu, uçuş bulma ajanın, otel rezervasyonu yapan ajanla iletişim kurarak otelin uçuşla aynı tarihlerde rezerve edilmesini sağlaması gerektiği anlamına gelir. Bu, ajanların kullanıcının seyahat tarihleri hakkında bilgi paylaşması gerektiği anlamına gelir; yani, *hangi ajanların bilgi paylaştığını ve nasıl paylaştığını* belirlemeniz gerekir.
- **Koordinasyon Mekanizmaları**: Ajanların, kullanıcının tercihlerini ve kısıtlamalarını karşılamak için eylemlerini koordine etmesi gerekir. Bir kullanıcı tercihi, havaalanına yakın bir otel isteyebilirken, bir kısıtlama, araç kiralamanın yalnızca havaalanında mevcut olması olabilir. Bu, otel rezervasyonu yapan ajanın, kullanıcının tercihlerini ve kısıtlamalarını karşılamak için araç kiralama ajanı ile koordinasyon sağlaması gerektiği anlamına gelir. Bu, *ajanların eylemlerini nasıl koordine ettiğini* belirlemeniz gerektiği anlamına gelir.
- **Ajan Mimarisi**: Ajanların, kullanıcıyla olan etkileşimlerinden öğrenmek ve kararlar almak için iç yapıya sahip olması gerekir. Örneğin, uçuş bulma ajanın, kullanıcıya hangi uçuşları önereceği konusunda kararlar almak için iç yapıya sahip olması gerekir. Bu, *ajanların kararları nasıl aldığı ve kullanıcıyla olan etkileşimlerinden nasıl öğrendiği* konusunda karar vermeniz gerektiği anlamına gelir. Bir ajanın nasıl öğrendiği ve geliştiğine dair örnekler, uçuş bulma ajanın, kullanıcının geçmiş tercihlerini temel alarak uçuşları önermek için bir makine öğrenimi modeli kullanması olabilir.
- **Çoklu Ajan Etkileşimlerine Görünürlük**: Birden fazla ajanın birbirleriyle nasıl etkileşimde bulunduğunu görmeniz gerekir. Bu, hata ayıklama, optimizasyon ve genel sistemin etkinliğini sağlamak için gereklidir. Bunu başarmak için, ajan etkinliklerini ve etkileşimlerini izlemek için araçlara ve tekniklere sahip olmanız gerekir. Bu, günlük kaydı ve izleme araçları, görselleştirme araçları ve performans ölçütleri şeklinde olabilir.
- **Çoklu Ajan Kalıpları**: Çoklu ajan sistemlerini uygulamak için merkezi, merkezi olmayan ve hibrit mimariler gibi farklı kalıplar vardır. Kullanım durumunuza en uygun kalıbı seçmeniz gerekir.
- **İnsan Döngüde**: Çoğu durumda, döngüde bir insan bulunacaktır ve ajanlara ne zaman insan müdahalesi isteyeceklerini öğretmeniz gerekir. Bu, ajanların önermediği belirli bir otel veya uçuşu talep eden bir kullanıcı ya da bir uçuş veya otel rezervasyonu yapmadan önce onay isteyen bir kullanıcı şeklinde olabilir.

## Çoklu Ajan Etkileşimlerine Görünürlük

Birden fazla ajanın birbirleriyle nasıl etkileşimde bulunduğunu görmeniz önemlidir. Bu görünürlük, hata ayıklama, optimizasyon ve genel sistemin etkinliğini sağlamak için gereklidir. Bunu başarmak için, ajan etkinliklerini ve etkileşimlerini izlemek için araçlara ve tekniklere sahip olmanız gerekir. Bu, günlük kaydı ve izleme araçları, görselleştirme araçları ve performans ölçütleri şeklinde olabilir.

Örneğin, bir kullanıcı için seyahat rezervasyonu yapma durumunda, her ajanın durumunu, kullanıcının tercihlerini ve kısıtlamalarını ve ajanlar arasındaki etkileşimleri gösteren bir kontrol paneline sahip olabilirsiniz. Bu kontrol paneli, kullanıcının seyahat tarihlerini, uçuş ajanının önerdiği uçuşları, otel ajanının önerdiği otelleri ve araç kiralama ajanının önerdiği araçları gösterebilir. Bu, ajanların birbirleriyle nasıl etkileşimde bulunduğunu ve kullanıcının tercihleri ve kısıtlamalarının karşılanıp karşılanmadığını net bir şekilde görmenizi sağlar.

Bu yönlere daha ayrıntılı bakalım:

- **Günlük Kaydı ve İzleme Araçları**: Her ajanın gerçekleştirdiği eylemler için günlük kaydı yapmak istersiniz. Bir günlük kaydı girdisi, eylemi gerçekleştiren ajan, gerçekleştirilen eylem, eylemin gerçekleştirildiği zaman ve eylemin sonucu hakkında bilgi içerebilir. Bu bilgiler, hata ayıklama, optimizasyon ve daha fazlası için kullanılabilir.
- **Görselleştirme Araçları**: Görselleştirme araçları, ajanlar arasındaki etkileşimleri daha sezgisel bir şekilde görmenize yardımcı olabilir. Örneğin, ajanlar arasındaki bilgi akışını gösteren bir grafik oluşturabilirsiniz. Bu, sistemdeki darboğazları, verimsizlikleri ve diğer sorunları belirlemenize yardımcı olabilir.
- **Performans Ölçütleri**: Performans ölçütleri, çoklu ajan sisteminin etkinliğini izlemenize yardımcı olabilir. Örneğin, bir görevi tamamlama süresini, birim zaman başına tamamlanan görev sayısını ve ajanların yaptığı önerilerin doğruluğunu izleyebilirsiniz. Bu bilgiler, iyileştirme alanlarını belirlemenize ve sistemi optimize etmenize yardımcı olabilir.

## Çoklu Ajan Kalıpları

Çoklu ajan uygulamaları oluşturmak için kullanabileceğimiz bazı somut kalıplara bakalım. İşte dikkate değer bazı ilginç kalıplar:

### Grup Sohbeti

Bu kalıp, birden fazla ajanın birbirleriyle iletişim kurabileceği bir grup sohbet uygulaması oluşturmak istediğinizde kullanışlıdır. Bu kalıbın tipik kullanım durumları arasında ekip iş birliği, müşteri desteği ve sosyal ağlar bulunur.

Bu kalıpta, her ajan grup sohbetindeki bir kullanıcıyı temsil eder ve mesajlar bir mesajlaşma protokolü kullanılarak ajanlar arasında değiştirilir. Ajanlar grup sohbete mesaj gönderebilir, grup sohbetten mesaj alabilir ve diğer ajanlardan gelen mesajlara yanıt verebilir.

Bu kalıp, tüm mesajların merkezi bir sunucu üzerinden yönlendirildiği merkezi bir mimari veya mesajların doğrudan değiştirildiği merkezi olmayan bir mimari kullanılarak uygulanabilir.

![Grup Sohbeti](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.tr.png)

### Görev Devri

Bu kalıp, birden fazla ajanın birbirlerine görev devredebileceği bir uygulama oluşturmak istediğinizde kullanışlıdır.

Bu kalıbın tipik kullanım durumları arasında müşteri desteği, görev yönetimi ve iş akışı otomasyonu bulunur.

Bu kalıpta, her ajan bir görevi veya bir iş akışındaki bir adımı temsil eder ve ajanlar, önceden tanımlanmış kurallara göre görevleri diğer ajanlara devredebilir.

![Görev Devri](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.tr.png)

### İş Birlikçi Filtreleme

Bu kalıp, birden fazla ajanın kullanıcıya önerilerde bulunmak için iş birliği yapabileceği bir uygulama oluşturmak istediğinizde kullanışlıdır.

Birden fazla ajanın iş birliği yapmasını istemenizin nedeni, her ajanın farklı bir uzmanlığa sahip olması ve öneri sürecine farklı şekillerde katkıda bulunabilmesidir.

Örneğin, bir kullanıcının borsada satın alınacak en iyi hisse senedi hakkında bir öneri istediğini düşünelim.

- **Sektör Uzmanı**: Bir ajan belirli bir sektörde uzman olabilir.
- **Teknik Analiz**: Başka bir ajan teknik analizde uzman olabilir.
- **Temel Analiz**: Ve başka bir ajan temel analizde uzman olabilir. Bu ajanlar iş birliği yaparak kullanıcıya daha kapsamlı bir öneri sunabilir.

![Öneri](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.tr.png)

## Senaryo: İade Süreci

Bir müşterinin bir ürün için iade almaya çalıştığı bir senaryoyu düşünelim; bu süreçte oldukça fazla ajan yer alabilir, ancak bunu bu sürece özgü ajanlar ve işinizin diğer bölümlerinde de kullanılabilecek genel ajanlar olarak ayıralım.

**İade Sürecine Özgü Ajanlar**:

İade sürecinde yer alabilecek bazı ajanlar şunlardır:

- **Müşteri Ajanı**: Bu ajan müşteriyi temsil eder ve iade sürecini başlatmaktan sorumludur.
- **Satıcı Ajanı**: Bu ajan satıcıyı temsil eder ve iade işlemini gerçekleştirmekten sorumludur.
- **Ödeme Ajanı**: Bu ajan ödeme sürecini temsil eder ve müşterinin ödemesini iade etmekten sorumludur.
- **Çözüm Ajanı**: Bu ajan çözüm sürecini temsil eder ve iade sürecinde ortaya çıkan sorunları çözmekten sorumludur.
- **Uyum Ajanı**: Bu ajan uyum sürecini temsil eder ve iade sürecinin düzenlemelere ve politikalara uygun olmasını sağlamaktan sorumludur.

**Genel Ajanlar**:

Bu ajanlar işinizin diğer bölümlerinde de kullanılabilir.

- **Kargo Ajanı**: Bu ajan kargo sürecini temsil eder ve ürünü satıcıya geri göndermekten sorumludur. Bu ajan hem iade süreci hem de örneğin bir satın alma yoluyla bir ürünün genel gönderimi için kullanılabilir.
- **Geri Bildirim Ajanı**: Bu ajan geri bildirim sürecini temsil eder ve müşteriden geri bildirim toplamaktan sorumludur. Geri bildirim herhangi bir zamanda alınabilir ve yalnızca iade sürecinde değil.
- **Yükseltme Ajanı**: Bu ajan yükseltme sürecini temsil eder ve sorunları daha üst bir destek seviyesine yükseltmekten sorumludur. Bu tür bir ajanı, bir sorunu yükseltmeniz gereken herhangi bir süreçte kullanabilirsiniz.
- **Bildirim Ajanı**: Bu ajan bildirim sürecini temsil eder ve iade sürecinin çeşitli aşamalarında müşteriye bildirim göndermekten sorumludur.
- **Analitik Ajanı**: Bu ajan analitik süreci temsil eder ve iade süreciyle ilgili verileri analiz etmekten sorumludur.
- **Denetim Ajanı**: Bu ajan denetim sürecini temsil eder ve iade sürecinin doğru bir şekilde yürütüldüğünden emin olmak için denetim yapmaktan sorumludur.
- **Raporlama Ajanı**: Bu ajan raporlama sürecini temsil eder ve iade süreciyle ilgili raporlar oluşturmaktan sorumludur.
- **Bilgi Ajanı**: Bu ajan bilgi sürecini temsil eder ve iade süreciyle ilgili bir bilgi tabanını sürdürmekten sorumludur. Bu ajan hem iadeler hem de işinizin diğer bölümleri hakkında bilgi sahibi olabilir.
- **Güvenlik Ajanı**: Bu ajan güvenlik sürecini temsil eder ve iade sürecinin güvenliğini sağlamaktan sorumludur.
- **Kalite Ajanı**: Bu ajan kalite sürecini temsil eder ve iade sürecinin kalitesini sağlamaktan sorumludur.

Yukarıda hem iade sürecine özgü hem de işinizin diğer bölümlerinde kullanılabilecek genel ajanlar listelenmiştir. Umarım bu, çoklu ajan sisteminizde hangi ajanları kullanacağınıza nasıl karar verebileceğiniz konusunda size bir fikir verir.

## Görev
Müşteri destek süreci için çoklu ajan sistemi tasarlayın. Süreçte yer alan ajanları, rollerini ve sorumluluklarını belirleyin ve birbirleriyle nasıl etkileşim kurduklarını açıklayın. Hem müşteri destek sürecine özgü ajanları hem de işinizin diğer bölümlerinde kullanılabilecek genel ajanları göz önünde bulundurun.

> Devam etmeden önce bir düşünün, ihtiyacınız olandan daha fazla ajana ihtiyaç duyabilirsiniz.

> İPUCU: Müşteri destek sürecinin farklı aşamalarını düşünün ve ayrıca herhangi bir sistem için gerekli ajanları göz önünde bulundurun.

## Çözüm

[Çözüm](./solution/solution.md)

## Bilgi Kontrolleri

Soru: Çoklu ajanları ne zaman kullanmayı düşünmelisiniz?

- [ ] A1: Küçük bir iş yükünüz ve basit bir göreviniz olduğunda.
- [ ] A2: Büyük bir iş yükünüz olduğunda.
- [ ] A3: Basit bir göreviniz olduğunda.

[Çözüm testi](./solution/solution-quiz.md)

## Özet

Bu derste, çoklu ajan tasarım desenini ele aldık. Çoklu ajanların hangi senaryolarda uygulanabilir olduğunu, tek bir ajana kıyasla çoklu ajanların avantajlarını, çoklu ajan tasarım desenini uygulamanın yapı taşlarını ve birden fazla ajanın birbirleriyle nasıl etkileşimde bulunduğunu görselleştirmenin yollarını inceledik.

### Çoklu Ajan Tasarım Deseni Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanları hakkındaki sorularınıza yanıt almak için [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) sunucusuna katılın.

## Ek Kaynaklar

- 

## Önceki Ders

[Planlama Tasarımı](../07-planning-design/README.md)

## Sonraki Ders

[AI Ajanlarında Metabiliş](../09-metacognition/README.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.