[![Multi-Agent Design](../../../translated_images/tr/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Bu dersin videosunu izlemek için yukarıdaki resme tıklayın)_

# Çoklu ajan tasarım desenleri

Birden çok ajanı içeren bir proje üzerinde çalışmaya başladığınız anda, çoklu ajan tasarım desenini dikkate almanız gerekecektir. Ancak, ne zaman çoklu ajanlara geçileceği ve avantajlarının ne olduğu hemen anlaşılmayabilir.

## Giriş

Bu derste aşağıdaki soruları yanıtlamayı hedefliyoruz:

- Çoklu ajanların uygulanabilir olduğu senaryolar nelerdir?
- Tek bir ajanın birden çok görevi yapmasına kıyasla çoklu ajan kullanmanın avantajları nelerdir?
- Çoklu ajan tasarım desenini uygulamanın yapı taşları nelerdir?
- Birden çok ajanın birbirleriyle nasıl etkileşimde bulunduğuna dair nasıl görünürlük sağlanır?

## Öğrenme Hedefleri

Bu dersten sonra şunları yapabilmelisiniz:

- Çoklu ajanların uygulanabilir olduğu senaryoları tanımlamak
- Tek bir ajana kıyasla çoklu ajan kullanmanın avantajlarını tanımak.
- Çoklu ajan tasarım deseninin yapı taşlarını kavramak.

Daha büyük resim nedir?

*Çoklu ajanlar, ortak bir hedefi gerçekleştirmek için birden çok ajanın birlikte çalışmasına olanak tanıyan bir tasarım desenidir*.

Bu desen, robotik, otonom sistemler ve dağıtık hesaplama dahil olmak üzere çeşitli alanlarda yaygın olarak kullanılmaktadır.

## Çoklu Ajanların Uygun Olduğu Senaryolar

Peki, hangi senaryolar çoklu ajan kullanımına iyi bir örnek olabilir? Cevap, özellikle aşağıdaki durumlarda çoklu ajan kullanmanın faydalı olduğu birçok senaryo vardır:

- **Büyük iş yükleri**: Büyük iş yükleri daha küçük görevlere bölünebilir ve farklı ajanlara atanabilir; bu, paralel işlemeye ve daha hızlı tamamlanmaya olanak tanır. Bunun bir örneği büyük veri işleme görevidir.
- **Karmaşık görevler**: Karmaşık görevler, büyük iş yüklerinde olduğu gibi daha küçük alt görevlere bölünebilir ve her biri görevin belirli bir yönünde uzmanlaşmış farklı ajanlara atanabilir. Örneğin, otonom araçlarda farklı ajanlar navigasyon, engel tespiti ve diğer araçlarla iletişimi yönetir.
- **Çeşitli uzmanlıklar**: Farklı ajanlar farklı uzmanlıklara sahip olabilir, böylece tek bir ajan yerine görevin farklı yönlerini daha etkili şekilde ele alabilirler. Bu duruma iyi bir örnek, teşhis, tedavi planları ve hasta izlemesini yöneten sağlık hizmetleri ajanslarıdır.

## Tek Bir Ajana Göre Çoklu Ajan Kullanmanın Avantajları

Tek bir ajan sistemi basit görevlerde iyi çalışabilir, ancak daha karmaşık görevlerde, çoklu ajan kullanımı birkaç avantaj sağlar:

- **Uzmanlaşma**: Her ajan belirli bir göreve uzmanlaşabilir. Tek bir ajandaki uzmanlaşmanın eksikliği, her şeyi yapabilen ancak karmaşık bir görevle karşılaştığında ne yapacağını şaşırabilecek bir ajanınız olması anlamına gelir. Örneğin, en iyi olduğu görevden farklı bir görevi üstlenebilir.
- **Ölçeklenebilirlik**: Sistemi, tek bir ajana fazla yük yüklemek yerine daha fazla ajan ekleyerek ölçeklendirmek daha kolaydır.
- **Hata Toleransı**: Bir ajan başarısız olursa, diğerleri çalışmaya devam edebilir; böylece sistem güvenilirliği sağlanır.

Bir örnek alalım; bir kullanıcı için bir seyahat rezervasyonu yapalım. Tek ajanlı bir sistem, uçuş bulmaktan otel ve araç kiralama rezervasyonlarına kadar tüm seyahat rezervasyon sürecini yönetmek zorunda kalır. Bunu tek bir ajanla başarmak için ajan, bu görevlerin tümünü yapabilmek için araçlara sahip olmalı. Bu da bakımı ve ölçeklendirmeyi zorlaştıran karmaşık ve tek parça bir sistemle sonuçlanabilir. Çoklu ajanlı sistem ise uçuş arama, otel rezervasyonu ve araç kiralama alanlarında uzmanlaşmış farklı ajanları içerebilir. Bu sistem daha modüler, bakımı kolay ve ölçeklenebilir olur.

Bunu, annesi-babası tarafından işletilen bir seyahat ofisi ile franchise olarak işletilen bir seyahat bürosu arasında karşılaştırabilirsiniz. Anneleri-babası tarafından işletilen ofiste tek bir ajan seyahat rezervasyonunun tüm aşamalarını yönetirken, franchise bürosunda farklı ajanlar seyahat rezervasyon sürecinin farklı yönlerini yönetir.

## Çoklu Ajan Tasarım Desenini Uygulamanın Yapı Taşları

Çoklu ajan tasarım desenini uygulamadan önce, deseni oluşturan yapı taşlarını anlamanız gerekir.

Bunu daha somut yapmak için tekrar bir kullanıcı için seyahat rezervasyonu örneğine bakalım. Bu durumda, yapı taşları şunları içerir:

- **Ajan İletişimi**: Uçuş bulma, otel rezervasyonu ve araç kiralama ajanlarının, kullanıcının tercihleri ve kısıtlamaları hakkında bilgi alışverişi yapmaları gerekir. Bu iletişim için hangi protokollerin ve yöntemlerin kullanılacağına karar vermelisiniz. Somut olarak, uçuş bulma ajanının otel rezervasyonu yapan ajanla iletişim kurması gerekir; böylece otelin, uçuş tarihleriyle aynı tarihlerde rezerve edildiğinden emin olunur. Bu, ajanların kullanıcının seyahat tarihleri hakkında bilgi paylaşması gerektiği anlamına gelir; yani *hangi ajanların bilgi paylaştığı ve nasıl paylaştığı* karar verilmelidir.
- **Koordinasyon Mekanizmaları**: Ajanlar, kullanıcının tercihleri ve kısıtlamalarının karşılandığından emin olmak için eylemlerini koordine etmelidirler. Örneğin, kullanıcının tercihi havaalanına yakın bir otel olması iken, kısıtlama araç kiralamanın sadece havaalanında mümkün olması olabilir. Bu durumda otel rezervasyonu yapan ajan, araç kiralama yapan ajanla koordine olmalıdır. Bu nedenle *ajanların eylemlerini nasıl koordine ettiği* belirlenmelidir.
- **Ajan Mimarisi**: Ajanlar, karar verme ve kullanıcı ile etkileşimlerinden öğrenme yapısına sahip olmalıdır. Örneğin, uçuş bulma ajanı, kullanıcıya hangi uçuşları önereceğine karar verebilmek için dahili bir yapıya sahip olmalıdır. Bu nedenle *ajanların karar verme ve kullanıcı etkileşimlerinden öğrenme şekli* belirlenmelidir. Bir ajanın nasıl öğrendiği ve geliştirildiğine örnek olarak, uçuş bulma ajanının, kullanıcının geçmiş tercihleri temelinde uçuşlar önermek için makine öğrenimi modeli kullanması verilebilir.
- **Çoklu Ajan Etkileşimlerine Görünürlük**: Birden çok ajanın birbirleriyle nasıl etkileşimde bulunduğunu görmeniz gerekir. Bunun için ajan faaliyetlerini ve etkileşimlerini takip eden araç ve tekniklere sahip olmalısınız. Bu, günlük kaydı ve izleme araçları, görselleştirme araçları ve performans metrikleri şeklinde olabilir.
- **Çoklu Ajan Desenleri**: Merkezi, merkezi olmayan ve hibrit mimariler gibi çoklu ajan sistemlerini uygulamak için farklı desenler vardır. Kullanım durumunuza en uygun deseni seçmeniz gerekir.
- **İnsanın Döngüde Olması**: Çoğu durumda, döngüde bir insan olacaktır ve ajanlara ne zaman insan müdahalesi isteneceği talimatını vermeniz gerekir. Bu, ajanların önermediği belirli bir otel veya uçuşu kullanıcı talep etmesi ya da uçuş veya otellerin rezervasyonu öncesinde onay istemesi şeklinde olabilir.

## Çoklu Ajan Etkileşimlerine Görünürlük

Birden çok ajanın nasıl etkileşimde bulunduğunu görmeniz önemlidir. Bu görünürlük, hata ayıklama, optimizasyon ve genel sistem etkinliğini sağlama açısından gereklidir. Bunu başarmak için ajan faaliyetlerini ve etkileşimlerini izleyen araçlar ve tekniklere sahip olmalısınız. Bu, günlük kaydı ve izleme araçları, görselleştirme araçları ve performans metrikleri şeklinde olabilir.

Örneğin, bir kullanıcı için seyahat rezervasyonu yaparken, her ajanın durumunu, kullanıcının tercihlerini ve kısıtlamalarını ve ajanlar arasındaki etkileşimleri gösteren bir gösterge panonuz olabilir. Bu pano, kullanıcının seyahat tarihlerini, uçuş ajanının önerdiği uçuşları, otel ajanının önerdiği otelleri ve araç kiralama ajanının önerdiği araçları gösterebilir. Bu, ajanların birbirleriyle nasıl etkileşimde bulunduğu ve kullanıcının tercihleri ile kısıtlamalarının karşılanıp karşılanmadığı konusunda net bir görünüm sağlar.

Bu yönlerin her birine daha detaylı bakalım.

- **Günlük Kaydı ve İzleme Araçları**: Her ajanın yaptığı her işlem için günlük kaydı yapılmasını istersiniz. Bir günlük kaydı, işlemi yapan ajan, yapılan işlem, işlemin yapıldığı zaman ve işlemin sonucu hakkında bilgi depolayabilir. Bu bilgiler hata ayıklama, optimizasyon ve daha fazlası için kullanılabilir.

- **Görselleştirme Araçları**: Görselleştirme araçları, ajanlar arasındaki etkileşimleri daha sezgisel bir şekilde görmenize yardımcı olabilir. Örneğin, ajanlar arasındaki bilgi akışını gösteren bir grafik olabilir. Bu, sistemdeki darboğazları, verimsizlikleri ve diğer sorunları tespit etmenize yardımcı olabilir.

- **Performans Metrikleri**: Performans metrikleri, çoklu ajan sisteminin etkinliğini takip etmenize yardımcı olabilir. Örneğin, bir görevin tamamlanma süresini, birim zamandaki tamamlanan görev sayısını ve ajanlar tarafından yapılan önerilerin doğruluğunu izleyebilirsiniz. Bu bilgiler iyileştirme alanlarını belirlemenize ve sistemi optimize etmenize olanak tanır.

## Çoklu Ajan Desenleri

Çoklu ajan uygulamaları oluşturmak için kullanabileceğimiz bazı somut desenlere bakalım. İşte dikkate alınması gereken bazı ilginç desenler:

### Grup sohbeti

Bu desen, birden fazla ajanın birbirleriyle iletişim kurabileceği bir grup sohbeti uygulaması oluşturmak istediğinizde faydalıdır. Bu deseni için tipik kullanım alanları ekip işbirliği, müşteri desteği ve sosyal ağdır.

Bu desende, her ajan grup sohbetindeki bir kullanıcıyı temsil eder ve mesajlar ajanlar arasında bir mesajlaşma protokolü kullanılarak değiştirilir. Ajanlar grup sohbetine mesaj gönderebilir, grup sohbetinden mesaj alabilir ve diğer ajanlardan gelen mesajlara yanıt verebilir.

Bu desen, tüm mesajların merkezi bir sunucu aracılığıyla yönlendirildiği merkezi bir mimariyle veya mesajların doğrudan değiştirildiği merkezi olmayan bir mimariyle uygulanabilir.

![Group chat](../../../translated_images/tr/multi-agent-group-chat.ec10f4cde556babd.webp)

### Görev devri

Bu desen, birden çok ajanın görevleri birbirlerine devredebileceği bir uygulama oluşturmak istediğinizde faydalıdır.

Tipik kullanım alanları müşteri desteği, görev yönetimi ve iş akışı otomasyonudur.

Bu desende, her ajan bir görev veya iş akışındaki bir adımı temsil eder ve ajanlar önceden belirlenmiş kurallara göre görevleri diğer ajanlara devredebilir.

![Hand off](../../../translated_images/tr/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### İşbirlikçi filtreleme

Bu desen, birden çok ajanın kullanıcıya önerilerde bulunmak üzere işbirliği yapabileceği bir uygulama oluşturmak istediğinizde faydalıdır.

Neden birden çok ajanın işbirliği yapmasını istersiniz? Çünkü her ajan farklı uzmanlıklara sahip olabilir ve öneri sürecine farklı şekillerde katkıda bulunabilir.

Bir kullanıcının borsada satın alınacak en iyi hisse senedi için öneri istediği bir örnek alalım.

- **Sektör uzmanı**: Bir ajan belirli bir sektörde uzmandır.
- **Teknik analiz**: Başka bir ajan teknik analizde uzmandır.
- **Temel analiz**: Diğer bir ajan temel analizde uzmandır. Bu ajanlar işbirliği yaparak kullanıcıya daha kapsamlı bir öneri sunabilir.

![Recommendation](../../../translated_images/tr/multi-agent-filtering.d959cb129dc9f608.webp)

## Senaryo: İade süreci

Bir müşterinin bir ürün için iade talebinde bulunduğu bir senaryoyu düşünün; bu süreçte oldukça fazla ajan yer alabilir ancak bu ajanları, bu sürece özgü ajanlar ve diğer süreçlerde kullanılabilecek genel ajanlar olarak ayıralım.

**İade sürecine özgü ajanlar**:

İade sürecinde yer alabilecek ajanlar şunlardır:

- **Müşteri ajanı**: Bu ajan müşteriyi temsil eder ve iade sürecini başlatmaktan sorumludur.
- **Satıcı ajanı**: Bu ajan satıcıyı temsil eder ve iade işlemini yürütmekten sorumludur.
- **Ödeme ajanı**: Bu ajan ödeme sürecini temsil eder ve müşterinin ödemenin iadesi işlemini yönetir.
- **Çözüm ajanı**: Bu ajan çözüm sürecini temsil eder ve iade sürecinde ortaya çıkan sorunların çözülmesinden sorumludur.
- **Uyum ajanı**: Bu ajan uyum sürecini temsil eder ve iade sürecinin düzenlemeler ve politikalar ile uyumlu olmasını sağlar.

**Genel ajanlar**:

Bu ajanlar işinizin diğer bölümlerinde de kullanılabilir.

- **Nakliye ajanı**: Bu ajan nakliye sürecini temsil eder ve ürünün satıcıya geri gönderilmesinden sorumludur. Bu ajan hem iade süreci hem de örneğin bir satın alma yoluyla ürünün genel nakliyesi için kullanılabilir.
- **Geri bildirim ajanı**: Bu ajan geri bildirim sürecini temsil eder ve müşteriden geri bildirim toplamaktan sorumludur. Geri bildirim iade süreci dışında her zaman alınabilir.
- **Yükseltme ajanı**: Bu ajan yükseltme sürecini temsil eder ve sorunları daha yüksek destek seviyesine taşımaktan sorumludur. Sorun yükseltmeniz gereken her süreçte bu tür ajanı kullanabilirsiniz.
- **Bildirim ajanı**: Bu ajan bildirim sürecini temsil eder ve iade sürecinin çeşitli aşamalarında müşteriye bildirimler göndermekten sorumludur.
- **Analitik ajanı**: Bu ajan analitik sürecini temsil eder ve iade süreciyle ilgili verileri analiz etmekten sorumludur.
- **Denetim ajanı**: Bu ajan denetim sürecini temsil eder ve iade sürecinin doğru şekilde yürütüldüğünü denetlemekten sorumludur.
- **Raporlama ajanı**: Bu ajan raporlama sürecini temsil eder ve iade süreci ile ilgili raporlar oluşturmakla görevlidir.
- **Bilgi ajanı**: Bu ajan bilgi sürecini temsil eder ve iade süreci ile ilgili bilgi tabanını yönetmekten sorumludur. Bu ajan hem iadeler hem de işinizin diğer bölümleri hakkında bilgi sahibi olabilir.
- **Güvenlik ajanı**: Bu ajan güvenlik sürecini temsil eder ve iade sürecinin güvenliğini sağlamaktan sorumludur.
- **Kalite ajanı**: Bu ajan kalite sürecini temsil eder ve iade sürecinin kalitesini sağlamaktan sorumludur.

Önceden listelenen ajanlar, iade sürecine özgü olanlar ve işinizin diğer bölümlerinde kullanılabilecek genel ajanlar olmak üzere oldukça fazladır. Umarım bu, çoklu ajan sisteminizde hangi ajanları kullanacağınıza nasıl karar vereceğiniz hakkında size bir fikir verir.

## Ödev

Bir müşteri destek süreci için çoklu ajan sistemi tasarlayın. Süreçte yer alan ajanları, rolleri ve sorumluluklarını, birbirleriyle nasıl etkileşim kurduklarını belirleyin. Hem müşteri destek sürecine özgü ajanları hem de işinizin diğer bölümlerinde kullanılabilecek genel ajanları göz önünde bulundurun.
> Aşağıdaki çözümü okumadan önce bir düşünün, düşündüğünüzden daha fazla ajana ihtiyacınız olabilir.

> İPUCU: Müşteri destek sürecinin farklı aşamalarını düşünün ve ayrıca herhangi bir sistem için gereken ajanları göz önünde bulundurun.

## Çözüm

[Çözüm](./solution/solution.md)

## Bilgi kontrolü

Soru: Çoklu ajan kullanmayı ne zaman düşünmelisiniz?

- [ ] A1: Küçük bir iş yükünüz ve basit bir göreviniz olduğunda.
- [ ] A2: Büyük bir iş yükünüz olduğunda
- [ ] A3: Basit bir göreviniz olduğunda.

[Çözüm sınavı](./solution/solution-quiz.md)

## Özet

Bu derste, çoklu ajan tasarım desenine baktık; çoklu ajanların uygulanabilir olduğu senaryolar, tek bir ajana göre çoklu ajan kullanmanın avantajları, çoklu ajan tasarım deseninin uygulanmasının yapı taşları ve birden fazla ajanın birbirleriyle nasıl etkileşime girdiğine dair görünürlük nasıl sağlanır gibi konuları ele aldık.

### Çoklu Ajan Tasarım Deseni Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanları ile ilgili sorularınıza yanıt almak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)'a katılın.

## Ek kaynaklar

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework belgeleri</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentic tasarım desenleri</a>

## Önceki Ders

[Planlama Tasarımı](../07-planning-design/README.md)

## Sonraki Ders

[AI Ajanlarında Üstbiliş](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, yapay zeka çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda oluşabilecek herhangi bir yanlış anlama veya yanlış yorumlama nedeniyle sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->