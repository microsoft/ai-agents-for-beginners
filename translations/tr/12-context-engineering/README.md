# AI Ajanları için Bağlam Mühendisliği

[![Bağlam Mühendisliği](../../../translated_images/tr/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Bu dersin videosunu izlemek için yukarıdaki resme tıklayın)_

Bir yapay zeka ajanı için oluşturduğunuz uygulamanın karmaşıklığını anlamak, güvenilir bir ajanın yapılması açısından önemlidir. İpuçları mühendisliğinin ötesinde karmaşık ihtiyaçları karşılamak için bilgiyi etkili bir şekilde yöneten AI Ajanları inşa etmemiz gerekiyor.

Bu derste, bağlam mühendisliği nedir ve AI ajanları oluşturmadaki rolü üzerine bakacağız.

## Giriş

Bu ders şunları kapsayacak:

• **Bağlam Mühendisliği nedir** ve neden ipucu mühendisliğinden farklıdır.

• **Etkili Bağlam Mühendisliği için stratejiler**, bilgi yazma, seçme, sıkıştırma ve izole etme dahil.

• AI ajanınızın raydan çıkmasına neden olabilecek **Yaygın Bağlam Hataları** ve bunların nasıl düzeltileceği.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bileceksiniz:

• **Bağlam mühendisliğini tanımlamak** ve bunu ipucu mühendisliğinden ayırt etmek.

• Büyük Dil Modeli (LLM) uygulamalarında bağlamın temel bileşenlerini **belirlemek**.

• Ajan performansını artırmak için bağlamı yazma, seçme, sıkıştırma ve izole etme stratejilerini **uygulamak**.

• Zehirlenme, dikkat dağınıklığı, karışıklık ve çatışma gibi **yaygın bağlam hatalarını tanımak** ve hafifletme tekniklerini uygulamak.

## Bağlam Mühendisliği Nedir?

AI Ajanları için bağlam, bir yapay zekâ ajanın belirli eylemleri planlamasını tetikleyen şeydir. Bağlam Mühendisliği, Yapay Zeka Ajanının görevde bir sonraki adımı tamamlamak için doğru bilgiye sahip olmasını sağlamaktır. Bağlam penceresi sınırlı büyüklüktedir, bu nedenle ajan geliştiricileri olarak bağlam penceresine eklenen, kaldırılan ve yoğunlaştırılan bilgiyi yönetmek için sistemler ve süreçler inşa etmemiz gerekmektedir.

### İpucu Mühendisliği ve Bağlam Mühendisliği Arasındaki Fark

İpucu mühendisliği, yapay zeka ajanlarını kurallar setiyle etkili şekilde yönlendirmek için tek bir statik talimat setine odaklanır. Bağlam mühendisliği ise ajanların zaman içinde neye ihtiyaç duyduğunu garanti altına almak için dinamik bilgi setini nasıl yöneteceğidir. Bağlam mühendisliğinin ana fikri bu süreci tekrarlanabilir ve güvenilir hale getirmektir.

### Bağlam Türleri

[![Bağlam Türleri](../../../translated_images/tr/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Bağlamın sadece tek bir şey olmadığını hatırlamak önemlidir. Yapay Zeka Ajanının ihtiyaç duyduğu bilgi farklı kaynaklardan gelebilir ve bunlara erişimini sağlamamız gerekir:

Bir AI ajanının yönetmesi gereken bağlam türleri şunları içerir:

• **Talimatlar:** Bu, ajanın "kuralları" gibidir – ipuçları, sistem mesajları, az örnekli örnekler (yapay zekaya bir şeyin nasıl yapılacağını gösterir) ve kullanabileceği araçların açıklamaları. İpucu mühendisliğinin odağı burada bağlam mühendisliğiyle birleşir.

• **Bilgi:** Gerçekler, veri tabanlarından alınan bilgiler veya ajan tarafından biriktirilmiş uzun süreli anılar. Bir ajan farklı bilgi depolarına ve veri tabanlarına erişim ihtiyacı varsa, Birleştirilmiş Geri Getirmeli Üretim (RAG) sistemi bu noktada entegre edilir.

• **Araçlar:** Ajanın çağırabileceği dış fonksiyonların, API'ların ve MCP Sunucularının tanımları, ayrıca bunları kullanmaktan elde ettiği geri bildirimler (sonuçlar).

• **Konuşma Geçmişi:** Kullanıcıyla devam eden diyalog. Zamanla bu konuşmalar uzar ve karmaşıklaşır, böylece bağlam penceresinde yer kaplar.

• **Kullanıcı Tercihleri:** Bir kullanıcının zaman içinde edindiği beğeni veya hoşlanmama bilgisi. Bunlar saklanabilir ve önemli kararlar alınırken kullanılabilir.

## Etkili Bağlam Mühendisliği İçin Stratejiler

### Planlama Stratejileri

[![Bağlam Mühendisliği En İyi Uygulamaları](../../../translated_images/tr/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

İyi bağlam mühendisliği iyi planlamayla başlar. İşte bağlam mühendisliği kavramını nasıl uygulamaya başlayacağınıza yardımcı olacak bir yaklaşım:

1. **Net Sonuçları Tanımlayın** - Yapay Zeka Ajanlarına atanacak görevlerin sonuçları net biçimde tanımlanmalıdır. "Yapay Zeka Ajanı işini bitirdiğinde dünya nasıl görünecek?" sorusunu yanıtlayın. Başka bir deyişle, kullanıcı yapay zeka ajanıyla etkileşim sonrası ne değişmeli, hangi bilgi ya da yanıtı almalı.
2. **Bağlamı Haritalayın** - Yapay Zeka Ajanının sonuçlarını tanımladıktan sonra "Bu görevi tamamlamak için yapay zeka ajanının hangi bilgiye ihtiyacı var?" sorusunu yanıtlamak gerekir. Böylece bu bilginin nerede bulunabileceğini haritalamaya başlayabilirsiniz.
3. **Bağlam Boru Hatları Oluşturun** - Bilginin nerede olduğunu bildiğinize göre, "Ajan bu bilgiyi nasıl alacak?" sorusunu yanıtlamanız gerekir. Bu RAG, MCP sunucularının ve diğer araçların kullanımı gibi çeşitli yollarla yapılabilir.

### Pratik Stratejiler

Planlama önemli ama bilgi ajanımızın bağlam penceresine akmaya başlayınca, bunu yönetmek için pratik stratejilere ihtiyacımız var:

#### Bağlam Yönetimi

Bazı bilgiler bağlam penceresine otomatik eklenecekken, bağlam mühendisliği bu bilgiyi daha aktif şekilde yönetmekle ilgilidir, ki bu birkaç strateji ile yapılabilir:

 1. **Ajan Not Defteri**
 Bu, AI Ajanının tek bir oturumda mevcut görevler ve kullanıcı etkileşimleriyle ilgili önemli bilgileri not almasını sağlar. Bu, bağlam penceresi dışında ajan tarafından gerektiğinde erişilebilen bir dosya veya çalışma zamanı nesnesinde bulunmalıdır.

 2. **Anılar**
 Not defterleri tek oturumun bağlam penceresi dışındaki bilgiyi yönetmek için iyiyken, anılar ajanların birden fazla oturum arası ilgili bilgiyi saklayıp geri çağırmasını sağlar. Bu özetler, kullanıcı tercihleri ve ileride yapılacak geliştirmeler için geri bildirimleri içerebilir.

 3. **Bağlamı Sıkıştırma**
  Bağlam penceresi büyüyüp sınırına yaklaşınca özetleme ve budama gibi teknikler kullanılır. Bu yöntem, sadece en alakalı bilgilerin tutulması veya eski mesajların kaldırılması anlamına gelir.
  
 4. **Çoklu Ajan Sistemleri**
  Çoklu ajan sistemleri geliştirmek, her ajanın kendi bağlam penceresine sahip olması nedeniyle bağlam mühendisliği türüdür. Bu bağlamın nasıl paylaşılıp farklı ajanlara aktarıldığı, bu sistemler inşa edilirken planlanması gereken bir başka konudur.
  
 5. **Sandbox Ortamları**
  Bir ajanın kod çalıştırması veya bir belgede büyük miktarda bilgi işlemesi gerekiyorsa, sonuçları işlemek çok fazla token gerektirebilir. Bu tümünün bağlam penceresinde tutulması yerine, ajan kodu çalıştırabilen ve sadece sonuçları ve diğer ilgili bilgileri okuyabilen bir sandbox ortamı kullanabilir.
  
 6. **Çalışma Zamanı Durum Nesneleri**
   Bu, Ajanın belirli bilgiye erişmesi gereken durumları yönetmek için bilgi konteynerleri oluşturularak yapılır. Karmaşık bir görevde, her alt görevin sonuçlarını adım adım depolayarak bağlamın sadece o belirli alt görevle bağlantılı kalmasını sağlar.

#### Bağlamı İnceleme

Bu stratejilerden birini uyguladıktan sonra, sonraki model çağrısının gerçekte ne aldığını kontrol etmek faydalıdır. Yararlı bir hata ayıklama sorusu şudur:

> Ajan çok fazla bağlam mı yükledi, yanlış bağlam mı aldı yoksa ihtiyaç duyduğu bağlamı mı kaçırdı?

Bu soruyu yanıtlamak için ham ipuçlarını, araç çıktılarını veya bellek içeriklerini kaydetmeniz gerekmez. Üretimde, sayı, kimlik, karma ve politika etiketlerini yakalayan küçük bağlam inceleme kayıtlarını tercih edin:

- **Seçim:** Kaç tane aday parça, araç veya belleğin değerlendirildiğini, kaçının seçildiğini ve diğerlerinin filtrelenmesine hangi kural veya skorun neden olduğunu takip edin.
- **Sıkıştırma:** Kaynak aralığı veya iz kimliği, özet kimliği, sıkıştırma öncesi ve sonrası tahmini token sayısı ve ham içeriğin sonraki çağrıda dışlanıp dışlanmadığını kaydedin.
- **İzolasyon:** Ayrı bir ajan, oturum veya sandbox'ta hangi alt görevin çalıştığını, dönen sınırlı özeti ve büyük araç çıktısının ana ajan bağlamının dışında kalıp kalmadığını not edin.
- **Bellek ve RAG:** Tam geri getirilen metin yerine geri getirme belge kimliklerini, bellek kimliklerini, puanları, seçilen kimlikleri ve sansür durumlarını saklayın.
- **Güvenlik ve gizlilik:** Hassas ipucu metni, araç argümanları, araç sonuçları veya kullanıcı belleği gövdeleri yerine karma, kimlik, token kovaları ve politika etiketlerini tercih edin.

Amaç daha fazla bağlam tutmak değil. Amaç geliştiricinin hangi bağlam stratejisinin çalıştığını ve bunun sonraki model çağrısını amaçlandığı gibi değiştirip değiştirmediğini anlayabileceği kadar kanıt bırakmaktır.

### Bağlam Mühendisliği Örneği

Diyelim ki bir AI ajanından **"Bana Paris'e bir gezi ayarla."** demek istiyoruz.

• Sadece ipucu mühendisliği kullanan basit bir ajan şöyle yanıt verebilir: **"Tamam, Paris'e ne zaman gitmek istersiniz?"**. O, yalnızca kullanıcının o anda sorduğu doğrudan soruyu işledi.

• Bu derste ele alınan bağlam mühendisliği stratejilerini kullanan bir ajan çok daha fazlasını yapardı. Yanıt vermeden önce sistem şu işlemleri yapabilir:

  ◦ Gerçek zamanlı verileri alarak **takviminizi kontrol etmek**.

 ◦ **Geçmiş seyahat tercihlerinizi hatırlamak** (uzun dönem belleğinden), örneğin tercih ettiğiniz havayolu, bütçe veya direkt uçuş tercih edip etmediğiniz.

 ◦ Uçuş ve otel rezervasyonu için **kullanılabilir araçları belirlemek**.

- Sonra örnek yanıt şöyle olabilir: "Hey [Adınız]! Ekim'in ilk haftası boş görünüyorsunuz. Alıştığınız bütçe içinde [Tercih Edilen Havayolu] ile Paris'e direkt uçuşlara bakmamı ister misiniz?". Bu daha zengin ve bağlam farkındalığı olan yanıt, bağlam mühendisliğinin gücünü gösterir.

## Yaygın Bağlam Hataları

### Bağlam Zehirlenmesi

**Nedir:** Bir halüsinasyonun (LLM tarafından üretilen yanlış bilgi) veya hatanın bağlama girmesi ve tekrar tekrar referans alınması sonucunda ajanın imkansız hedefler peşinde koşması veya alakasız stratejiler geliştirmesi.

**Ne yapılmalı:** **Bağlam doğrulaması** ve **karantina** uygulayın. Bilgiyi uzun dönem belleğe eklemeden önce doğrulayın. Olası zehirlenme saptanırsa, kötü bilginin yayılmasını önlemek için yeni bağlam dizileri başlatın.

**Seyahat Rezervasyonu Örneği:** Ajan, gerçekten uluslararası uçuş sunmayan küçük bir yerel havaalanından uzak bir uluslararası şehre **direkt uçuş** varmış gibi hatalı bilgi üretir. Bu var olmayan uçuş detayı bağlama kaydedilir. Sonra rezervasyon istediğinizde, bu imkansız rotanın biletlerini bulmak için ısrar eder ve hatalar tekrar eder.

**Çözüm:** Uçuş detayını ajan bağlamına eklemeden _önce_ gerçek zamanlı bir API ile **uçuşun varlığını ve rotaları doğrulayan** bir adım uygulayın. Doğrulama başarısız olursa, hatalı bilgi "karantinaya" alınır ve kullanılmaz.

### Bağlam Dikkat Dağınıklığı

**Nedir:** Bağlam o kadar büyür ki model, eğitim sırasında öğrendiklerini kullanmak yerine biriken geçmişe fazla odaklanır ve tekrarlayan ya da yararsız eylemler yapar. Modeller bağlam penceresi dolmadan da hata yapmaya başlayabilir.

**Ne yapılmalı:** **Bağlam özetlemesi** kullanılır. Biriken bilgileri periyodik olarak kısa özetlere sıkıştırın, önemli detayları tutup gereksiz geçmişi kaldırın. Bu odaklanmayı "sıfırlamaya" yardımcı olur.

**Seyahat Rezervasyonu Örneği:** Uzun süre hayalinizdeki çeşitli seyahat yerlerini konuştunuz, iki yıl önceki sırt çantalı yolculuğunuzun ayrıntılarını detaylıca anlattınız. Sonunda **"gelecek ay için ucuz bir uçuş bul"** dediğinizde, ajan eski ve alakasız ayrıntılarla saplanır, sırt çantanızı veya önceki seyahat programlarını sorar, mevcut isteğinizi görmezden gelir.

**Çözüm:** Belirli sayıda dönüşten sonra veya bağlam çok büyüyünce, ajan en güncel ve alakalı sohbet bölümlerini – mevcut seyahat tarihleri ve hedefe odaklanarak – özetleyip bu sıkıştırılmış özeti sonraki LLM çağrısında kullanmalı, daha az ilgili geçmiş sohbeti atmalıdır.

### Bağlam Karışıklığı

**Nedir:** Gereksiz bağlam (genellikle çok sayıda mevcut araç nedeniyle) modelin kötü yanıtlar üretmesine veya alakasız araç çağırmasına neden olur. Daha küçük modeller özellikle bu duruma eğilimlidir.

**Ne yapılmalı:** RAG teknikleri kullanarak **araç yüklenme yönetimi** uygulanmalıdır. Araç açıklamaları vektör veri tabanında saklanmalı ve her görev için sadece en alakalı araçlar seçilmelidir. Araştırmalar araç seçimlerinin 30’dan az tutulmasının faydalı olduğunu gösterir.

**Seyahat Rezervasyonu Örneği:** Ajanın `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` gibi onlarca arac erişimi var. Siz **"Paris içinde dolaşmanın en iyi yolu nedir?"** diye soruyorsunuz. Araç sayısının fazlalığı nedeniyle ajan karışır ve Paris içinde `book_flight` çağırmaya veya siz toplu taşıma tercih ettiğiniz halde `rent_car` çağırmaya çalışır çünkü araç açıklamaları örtüşebilir ya da en iyisini ayırt edemez.

**Çözüm:** Araç açıklamaları üzerinde **RAG kullanın**. Paris’te dolaşma sorusu sorulduğunda, sistem sorgunuza göre sadece `rent_car` veya `public_transport_info` gibi en alakalı araçları dinamik olarak getirerek LLM’e odaklanmış bir "yükleme" sunar.

### Bağlam Çatışması

**Nedir:** Bağlam içinde çelişkili bilgiler olduğunda tutarsız muhakemeye veya kötü son yanıtlara yol açar. Genellikle bilgi aşamalı geldiğinde ve erken yanlış varsayımlar bağlamda kalmaya devam ettiğinde ortaya çıkar.

**Ne yapılmalı:** **Bağlam budama** ve **yük boşaltma** kullanın. Budama, yeni detaylar gelirken eski veya çelişkili bilgilerin kaldırılmasıdır. Yük boşaltma, modele bilgiyi ana bağlamı karıştırmadan işlemek için ayrı bir "not defteri" çalışma alanı sağlar.


**Seyahat Rezervasyonu Örneği:** Başlangıçta temsilcinize, **"Ekonomi sınıfında uçmak istiyorum."** dersiniz. Konuşmanın ilerleyen kısmında fikrinizi değiştirip, **"Aslında, bu seyahat için business sınıfını tercih edelim."** dersiniz. Her iki talep de bağlamda kalırsa, temsilci çelişkili arama sonuçları alabilir veya hangi tercihe öncelik vereceği konusunda karışıklık yaşayabilir.

**Çözüm:** **bağlam budama** uygulayın. Yeni bir talep eski bir talebe aykırı olduğunda, eski talep bağlamdan kaldırılır veya açıkça geçersiz kılınır. Alternatif olarak, temsilci karar vermeden önce çelişen tercihleri uzlaştırmak için bir **not defteri** kullanabilir, böylece yalnızca son ve tutarlı talep hareketlerini yönlendirir.

## Bağlam Mühendisliği Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Temsilcisi sorularınızı sormak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) topluluğuna katılın.
## Önceki Ders

[Agentic Protocols](../11-agentic-protocols/README.md)

## Sonraki Ders

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->