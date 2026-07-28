[![Agentic RAG](../../../translated_images/tr/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Bu dersin videosunu izlemek için üstteki görsele tıklayın)_

# Agentik RAG

Bu ders, dış kaynaklardan bilgi çekerken kendi sonraki adımlarını otonom olarak planlayan büyük dil modellerini (LLM'ler) içeren gelişmekte olan bir AI paradigması olan Agentik Retrieval-Augmented Generation (Agentik RAG) hakkında kapsamlı bir genel bakış sunar. Statik retrieval-then-read kalıplarının aksine, Agentik RAG, araç veya fonksiyon çağrıları ve yapılandırılmış çıktılarla kesintiye uğrayan LLM'ye yinelemeli çağrılar içerir. Sistem, sonuçları değerlendirir, sorguları iyileştirir, gerekirse ek araçlar çağırır ve tatmin edici bir çözüm elde edilene kadar bu döngüyü sürdürür.

## Giriş

Bu ders şunları kapsayacaktır

- **Agentik RAG’ı Anlamak:** Büyük dil modellerinin (LLM’ler) dış veri kaynaklarından bilgi çekerken kendi sonraki adımlarını otonom olarak planladığı gelişmekte olan AI paradigması hakkında bilgi edinin.
- **Yinelemeli Maker-Checker Stili:** Doğruluğu artırmak ve bozuk sorguları yönetmek için tasarlanmış, araç veya fonksiyon çağrıları ve yapılandırılmış çıktılarla kesintiye uğrayan LLM’ye yinelemeli çağrılar döngüsünü kavrayın.
- **Pratik Uygulamalarını Keşfetmek:** Agentik RAG’ın parladığı durumları tanımlayın; doğruluk öncelikli ortamlar, karmaşık veritabanı etkileşimleri ve genişletilmiş iş akışları gibi.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bilecek/anlayacaksınız:

- **Agentik RAG’ı Anlamak:** Büyük dil modellerinin (LLM’ler) dış veri kaynaklarından bilgi çekerken kendi sonraki adımlarını otonom olarak planladığı gelişmekte olan AI paradigması hakkında bilgi sahibi olun.
- **Yinelemeli Maker-Checker Stili:** Doğruluğu artırmak ve bozuk sorguları yönetmek için tasarlanmış, araç veya fonksiyon çağrıları ve yapılandırılmış çıktılarla kesintiye uğrayan LLM’ye yinelemeli çağrılar döngüsünü kavrayın.
- **Muhakeme Sürecine Sahip Olmak:** Sistemin muhakeme sürecini sahiplenme becerisini kavrayın; problem çözmek için önceden tanımlanmış yollara bağlı kalmadan kararlar almasını anlayın.
- **İş Akışı:** Bir agent modelinin, piyasa trend raporlarını bağımsız olarak çekmeyi, rakip verileri tanımlamayı, dahili satış metriklerini ilişkilendirmeyi, bulguları sentezlemeyi ve stratejiyi değerlendirmeyi nasıl kendi kendine karar verdiğini anlayın.
- **Yinelemeli Döngüler, Araç Entegrasyonu ve Bellek:** Sistemin döngüsel etkileşim modeline bağlı olduğunu, adımlar arasında durum ve belleği koruyarak tekrar eden döngülerden kaçındığını ve bilgilere dayalı kararlar aldığını öğrenin.
- **Başarısızlık Modlarıyla Baş Etme ve Öz Düzeltme:** Sisteminin sağlam öz düzeltme mekanizmalarını keşfedin; yineleme ve yeniden sorgulama, tanısal araçların kullanımı ve insan denetimine başvurma gibi.
- **Ajansın Sınırları:** Agentik RAG’ın sınırlarını anlayın; alan odaklı özerklik, altyapıya bağımlılık ve koruma önlemlerine saygı gibi konulara odaklanın.
- **Pratik Kullanım Durumları ve Değeri:** Agentik RAG’ın parladığı ortamları belirleyin; doğruluk öncelikli ortamlar, karmaşık veritabanı etkileşimleri ve genişletilmiş iş akışları gibi.
- **Yönetim, Şeffaflık ve Güven:** Açıklanabilir muhakeme, önyargı kontrolü ve insan denetimi dahil yönetim ve şeffaflığın önemini öğrenin.

## Agentik RAG Nedir?

Agentik Retrieval-Augmented Generation (Agentik RAG), büyük dil modellerinin (LLM’ler) dış kaynaklardan bilgi çekerken kendi sonraki adımlarını otonom olarak planladığı gelişmekte olan bir AI paradigmasıdır. Statik retrieval-then-read kalıplarının aksine, Agentik RAG, araç veya fonksiyon çağrıları ve yapılandırılmış çıktılarla kesintiye uğrayan, LLM’ye yinelemeli çağrılar içerir. Sistem, sonuçları değerlendirir, sorguları iyileştirir, gerekirse ek araçlar çağırır ve tatmin edici bir çözüm elde edilene kadar bu döngüyü sürdürür. Bu yinelemeli “maker-checker” stili doğruluğu artırır, bozuk sorgularla başa çıkar ve yüksek kaliteli sonuçlar sağlar.

Sistem muhakeme sürecine aktif olarak sahip çıkar; başarısız sorguları yeniden yazar, farklı retrieval yöntemlerini seçer, Azure AI Search’teki vektör araması, SQL veritabanları veya özel API’ler gibi birden çok aracı entegre eder ve cevabını nihai hale getirmeden önce bunları kullanır. Agentik sistemin ayırt edici niteliği, muhakeme sürecine sahip çıkabilme yeteneğidir. Geleneksel RAG uygulamaları önceden tanımlanmış yollara dayanırken, agentik bir sistem bulduğu bilginin kalitesine göre adımların sırasını otonom şekilde belirler.

## Agentik Retrieval-Augmented Generation (Agentik RAG) Tanımı

Agentik Retrieval-Augmented Generation (Agentik RAG), LLM'lerin dış veri kaynaklarından bilgi çekmekle kalmayıp aynı zamanda kendi sonraki adımlarını otonom olarak planladığı gelişmekte olan AI geliştirme paradigmasıdır. Statik retrieval-then-read kalıplarının veya dikkatle yazılmış prompt dizilerinin aksine, Agentik RAG, LLM’ye yinelemeli çağrılar döngüsünü, araç veya fonksiyon çağrıları ve yapılandırılmış çıktılarla kesintiye uğrayan bir biçimde içerir. Sistem her aşamada elde edilen sonuçları değerlendirir, sorguları iyileştirmeyi kararlaştırır, gerekirse ek araçlar çağırır ve tatmin edici sonuca ulaşana kadar bu döngüyü devam ettirir.

Bu yinelemeli “maker-checker” çalışma stili, doğruluğu artırmak, yapılandırılmış veritabanlarına yönelik bozuk sorgulara (örn. NL2SQL) çözüm getirmek ve dengeli, yüksek kaliteli sonuçlar sağlamak için tasarlanmıştır. Sadece dikkatle tasarlanmış prompt zincirlerine dayanmak yerine, sistem muhakeme sürecine aktif olarak sahip çıkar. Başarısız olan sorguları yeniden yazar, farklı retrieval yöntemleri seçer ve Azure AI Search'teki vektör araması, SQL veritabanları veya özel API’ler gibi birden çok aracı entegre eder. Bu sayede fazla karmaşık orkestrasyon çerçevelerine gerek kalmaz. Oldukça basit bir “LLM çağrısı → araç kullanımı → LLM çağrısı → …” döngüsü, gelişmiş ve sağlam çıktılar üretebilir.

![Agentik RAG Temel Döngüsü](../../../translated_images/tr/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Muhakeme Sürecine Sahip Olmak

Bir sistemi “agentik” yapan ayırt edici özellik, muhakeme sürecine sahip çıkabilme becerisidir. Geleneksel RAG uygulamaları genellikle insanın modele neyi ne zaman çekmesi gerektiğini belirten bir düşünce zinciri yolunu önceden tanımlamasına dayanır.
Ancak gerçek anlamda agentik bir sistem, problemi nasıl ele alacağına içsel olarak karar verir. Sadece bir betiği uygulamakla kalmaz; bulduğu bilginin kalitesine göre adımların sırasını otonom biçimde belirler.
Örneğin, bir ürün lansman stratejisi oluşturması istendiğinde, tüm araştırma ve karar alma iş akışını detaylandıran bir prompt’a sadece güvenmez. Bunun yerine agentik model bağımsız olarak şunları yapmaya karar verir:

1. Bing Web Grounding kullanarak mevcut piyasa trend raporlarını çekmek
2. Azure AI Search kullanarak ilgili rakip verileri tanımlamak
3. Azure SQL Database kullanarak geçmiş iç satış metriklerini ilişkilendirmek
4. Azure OpenAI Hizmeti aracılığıyla tüm bulguları tutarlı bir stratejiye sentezlemek
5. Stratejiyi boşluklar veya tutarsızlıklar açısından değerlendirmek ve gerekirse yeniden veri çekmek için başka bir tur başlatmak
Bu adımların tamamı—sorguları iyileştirmek, kaynakları seçmek, cevaptan “memnun” kalıncaya kadar yinelemek—model tarafından karar verilir, insan önceden script yazmaz.

## Yinelemeli Döngüler, Araç Entegrasyonu ve Bellek

![Araç Entegrasyonu Mimarisi](../../../translated_images/tr/tool-integration.0f569710b5c17c10.webp)

Agentik bir sistem, döngüsel bir etkileşim modeline dayanır:

- **Başlangıç Çağrısı:** Kullanıcının hedefi (yani kullanıcı promptu), LLM’ye sunulur.
- **Araç Çağrısı:** Model eksik bilgi veya belirsiz talimat tespit ederse, daha fazla bağlam toplamak için bir araç veya retrieval yöntemi seçer—örneğin bir vektör veritabanı sorgusu (Azure AI Search Hibrit arama gibi özel veriler üzerinde) ya da yapılandırılmış SQL çağrısı.
- **Değerlendirme & İyileştirme:** Dönen veriyi inceledikten sonra model, bilginin yeterli olup olmadığına karar verir. Değilse sorguyu iyileştirir, farklı araç dener veya yaklaşımını değiştirir.
- **Tatmin Olana Kadar Tekrarlama:** Model, kesin ve mantıklı bir yanıt verebilmek için yeterli netlik ve kanıt sağladığını belirleyene kadar bu döngüyü sürdürür.
- **Bellek & Durum:** Sistem, adımlar boyunca durum ve belleği koruduğundan, önceki denemeleri ve sonuçlarını hatırlayabilir, böylece tekrarlayan döngülerden kaçınır ve ilerlerken daha bilinçli kararlar verir.

Zamanla bu, gelişen bir anlayış duygusu yaratır ve modelin karmaşık, çok aşamalı görevlerde sürekli insan müdahalesine veya prompt yeniden şekillendirmeye gerek kalmadan gezinmesini sağlar.

## Başarısızlık Modlarıyla Baş Etme ve Öz Düzeltme

Agentik RAG’ın özerkliği aynı zamanda sağlam öz düzeltme mekanizmalarını içerir. Sistem çıkmaza girdiğinde—örneğin alakasız belgeler çektiğinde veya bozuk sorgularla karşılaştığında—şunları yapabilir:

- **Yineleme ve Yeniden Sorgulama:** Düşük değerli yanıtlar vermek yerine, model yeni arama stratejileri deneyebilir, veritabanı sorgularını yeniden yazabilir veya alternatif veri kümelerine bakabilir.
- **Tanısal Araçları Kullanma:** Sistem, muhakeme adımlarını debug etmeye veya çekilen verinin doğruluğunu teyit etmeye yardımcı olacak ek fonksiyonlar çağırabilir. Azure AI Tracing gibi araçlar sağlam gözlemlenebilirlik ve izleme sağlar.
- **İnsan Denetimine Başvurma:** Yüksek riskli veya tekrar eden başarısız durumlarda model belirsizliği işaret edebilir ve insan rehberliği talep edebilir. İnsan düzeltici geri bildirim sağladıktan sonra model bunu geleceğe taşıyabilir.

Bu yinelemeli ve dinamik yaklaşım, modelin sürekli gelişmesini sağlar; böylece model yalnızca tek seferlik değil, hatalarından öğrenen bir sistem haline gelir.

![Öz Düzeltme Mekanizması](../../../translated_images/tr/self-correction.da87f3783b7f174b.webp)

## Ajansın Sınırları

Kendi içinde bir görevde otonom olmasına rağmen, Agentik RAG Yapay Genel Zekâ ile aynı değildir. “Agentik” yetenekleri, insan geliştiriciler tarafından sağlanan araçlar, veri kaynakları ve politikalarla sınırlıdır. Kendi araçlarını yaratamaz veya belirlenen alan sınırlarının dışına çıkamaz. Bunun yerine, mevcut kaynakları dinamik olarak yönetmekte üstün performans gösterir.
Daha gelişmiş AI formlarından temel farklar şunlardır:

1. **Alan Odaklı Özerklik:** Agentik RAG sistemleri, kullanıcı tarafından tanımlanmış hedefleri bilinen bir alan dahilinde gerçekleştirmeye odaklıdır, sorgu yazma veya araç seçimi gibi stratejilerle sonuçları iyileştirir.
2. **Altyapıya Bağımlılık:** Sistemin yetenekleri, geliştiricilerin entegre ettiği araçlara ve verilere bağlıdır. İnsan müdahalesi olmadan bu sınırları aşamaz.
3. **Koruma Önlemlerine Saygı:** Etik kurallar, uyumluluk yönergeleri ve iş politikaları çok önemlidir. Agentin özgürlüğü daima güvenlik önlemleri ve denetim mekanizmaları ile sınırlandırılmıştır (umarız ki).

## Pratik Kullanım Durumları ve Değeri

Agentik RAG, yinelemeli iyileştirme ve kesinlik gerektiren durumlarda parlamaktadır:

1. **Doğruluk Öncelikli Ortamlar:** Uyum kontrolleri, düzenleyici analizler veya hukuki araştırmalarda agentik model, gerçekleri defalarca doğrulayabilir, birden çok kaynağa başvurabilir ve tamamen doğrulanmış bir yanıt oluşturana kadar sorguları yeniden yazabilir.
2. **Karmaşık Veritabanı Etkileşimleri:** Yapılandırılmış verilerle uğraşırken sorguların sık sık başarısız olabileceği veya ayar gerektirebileceği durumlarda sistem, Azure SQL veya Microsoft Fabric OneLake kullanarak sorgularını otonom biçimde iyileştirip son retrieval'ın kullanıcının niyetiyle uyumlu olmasını sağlar.
3. **Uzun Süreli İş Akışları:** Daha uzun oturumlar, yeni bilgiler ortaya çıktıkça evrilebilir. Agentik RAG, problem alanını öğrenirken sürekli yeni verileri dahil edip stratejileri değiştirebilir.

## Yönetim, Şeffaflık ve Güven

Bu sistemler muhakemede daha otonom hale geldikçe, yönetim ve şeffaflık çok önemlidir:

- **Açıklanabilir Muhakeme:** Model, yaptığı sorguların, başvurduğu kaynakların ve sonucuna ulaşmak için izlediği muhakeme adımlarının denetim izini sağlayabilir. Azure AI Content Safety ve Azure AI Tracing / GenAIOps gibi araçlar şeffaflığı korumaya ve riskleri azaltmaya yardımcı olur.
- **Önyargı Kontrolü ve Dengeli Retrieval:** Geliştiriciler, dengeli ve temsilci veri kaynaklarının dikkate alındığından emin olmak için retrieval stratejilerini ayarlayabilir ve Azure Machine Learning kullanan gelişmiş veri bilimi organizasyonları için özel modellerle çıktıları düzenli olarak önyargı veya çarpıklık açısından denetleyebilir.
- **İnsan Denetimi ve Uyumluluk:** Hassas görevlerde insan incelemesi hala önemlidir. Agentik RAG, yüksek riskli kararlarda insan yargısını değiştirmez—onu daha kapsamlı doğrulanmış seçenekler sunarak destekler.

Eylemlerin açık bir kaydını sunan araçlara sahip olmak çok önemlidir. Bunlar olmadığı takdirde, çok aşamalı bir sürecin hata ayıklaması çok zordur. Aşağıda, Agent çalıştırmasından Literal AI (Chainlit arkası şirket) tarafından verilmiş bir örnek verilmiştir:

![AgentRunExample](../../../translated_images/tr/AgentRunExample.471a94bc40cbdc0c.webp)

## Sonuç

Agentik RAG, AI sistemlerinin karmaşık ve veri yoğun görevleri nasıl ele aldığı konusunda doğal bir evrimi temsil eder. Döngüsel bir etkileşim modeli benimseyerek, araçları otonom seçerek ve yüksek kaliteli sonuç elde edilene kadar sorguları iyileştirerek, sistem statik prompt takibinin ötesine geçip daha uyumlu, bağlama duyarlı bir karar verici haline gelir. İnsan tanımlı altyapılar ve etik yönergelerle hâlâ sınırlı olsa da, bu agentik yetenekler hem işletmeler hem de son kullanıcılar için daha zengin, dinamik ve nihayetinde daha faydalı AI etkileşimlerine olanak tanır.

### Agentik RAG hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Agent sorularınızı yanıtlamak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)’a katılın.

## Ek Kaynaklar

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Azure OpenAI Hizmeti ile Retrieval Augmented Generation (RAG) Uygulaması: Kendi verilerinizi Azure OpenAI Hizmeti ile nasıl kullanacağınızı öğrenin. Bu Microsoft Learn modülü, RAG uygulaması için kapsamlı bir rehber sunar</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Microsoft Foundry ile üretken AI uygulamalarının değerlendirilmesi: Bu makale, halka açık veri setlerinde modellerin değerlendirilmesi ve karşılaştırılmasını, Agentik AI uygulamaları ve RAG mimarilerini içerir</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Agentik RAG Nedir | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentik RAG: Ajan Bazlı Retrieval Augmented Generation için Kapsamlı Rehber – Generation RAG Haberleri</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: sorgu yeniden biçimlendirme ve kendi sorgunla RAG'ini hızlandır! Hugging Face Açık Kaynak AI Tarif Kitabı</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">RAG'e Agentik Katmanlar Eklemek</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Bilgi Asistanlarının Geleceği: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Agentik RAG Sistemleri Nasıl Kurulur</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Microsoft Foundry Agent Servisini AI ajanlarınızı ölçeklendirmek için kullanmak</a>

### Akademik Makaleler

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Kendi Geri Bildirimiyle Yinelemeli İyileştirme</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Sözlü Pekiştirmeli Öğrenmeli Dil Ajanları</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Büyük Dil Modelleri Araçlarla Etkileşimli Eleştiriyle Kendi Kendini Düzeltebilir</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Agentic RAG Üzerine Bir Anket</a>

## Bu Ajanı Hızlı Test Etme (İsteğe Bağlı)

[Ders 16](../16-deploying-scalable-agents/README.md) içinde ajanları dağıtmayı öğrendikten sonra, bu dersin `TravelRAGAgent`'ını, yanıtlarının bilgi tabanına dayanıp dayanmadığını kontrol etmek için [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) ile hızlıca test edebilirsiniz. Çalıştırmak için, bkz. [`tests/README.md`](../tests/README.md).

## Önceki Ders

[Araç Kullanımı Tasarım Deseni](../04-tool-use/README.md)

## Sonraki Ders

[Güvenilir AI Ajanları Oluşturma](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->