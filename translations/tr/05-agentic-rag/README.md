<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T13:15:44+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "tr"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.tr.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Agentic RAG

Bu ders, büyük dil modellerinin (LLM'ler) dış kaynaklardan bilgi çekerken bir sonraki adımlarını bağımsız olarak planladığı yeni bir yapay zeka paradigması olan Agentic Retrieval-Augmented Generation (Agentic RAG) hakkında kapsamlı bir genel bakış sunar. Statik "bilgi getir-sonra oku" desenlerinden farklı olarak, Agentic RAG, araç veya fonksiyon çağrıları ve yapılandırılmış çıktılarla kesintiye uğrayan yinelemeli LLM çağrılarını içerir. Sistem sonuçları değerlendirir, sorguları iyileştirir, gerekirse ek araçlar çağırır ve tatmin edici bir çözüme ulaşana kadar bu döngüye devam eder.

## Giriş

Bu derste şunlar ele alınacaktır:

- **Agentic RAG'ı Anlamak:** Büyük dil modellerinin (LLM'ler) dış veri kaynaklarından bilgi çekerken bir sonraki adımlarını bağımsız olarak planladığı yeni yapay zeka paradigmasını öğrenin.
- **Yinelemeli Maker-Checker Stili:** Doğruluğu artırmak ve hatalı sorguları ele almak için tasarlanmış, araç veya fonksiyon çağrıları ve yapılandırılmış çıktılarla kesintiye uğrayan yinelemeli LLM çağrıları döngüsünü kavrayın.
- **Pratik Uygulamaları Keşfetmek:** Doğruluk öncelikli ortamlar, karmaşık veri tabanı etkileşimleri ve uzun iş akışları gibi Agentic RAG'ın öne çıktığı senaryoları belirleyin.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bilecek/anlayacaksınız:

- **Agentic RAG'ı Anlamak:** Büyük dil modellerinin (LLM'ler) dış veri kaynaklarından bilgi çekerken bir sonraki adımlarını bağımsız olarak planladığı yeni yapay zeka paradigmasını öğrenin.
- **Yinelemeli Maker-Checker Stili:** Doğruluğu artırmak ve hatalı sorguları ele almak için tasarlanmış, araç veya fonksiyon çağrıları ve yapılandırılmış çıktılarla kesintiye uğrayan yinelemeli LLM çağrıları döngüsünü kavrayın.
- **Akıl Yürütme Sürecine Sahip Olmak:** Sistemin, önceden tanımlanmış yollar olmadan sorunlara nasıl yaklaşacağına karar verme yeteneğini anlayın.
- **İş Akışı:** Agentic bir modelin, pazar trend raporlarını bağımsız olarak getirme, rakip verilerini belirleme, iç satış metriklerini ilişkilendirme, bulguları sentezleme ve stratejiyi değerlendirme kararlarını nasıl verdiğini öğrenin.
- **Yinelemeli Döngüler, Araç Entegrasyonu ve Bellek:** Sistemin, tekrarlayan döngülerden kaçınmak ve bilinçli kararlar almak için adımlar arasında durumu ve belleği koruyarak döngüsel bir etkileşim modeline nasıl güvendiğini öğrenin.
- **Hata Modlarını Ele Alma ve Kendini Düzeltme:** Yineleme ve yeniden sorgulama, tanı araçlarını kullanma ve insan gözetimine başvurma gibi sistemin sağlam kendini düzeltme mekanizmalarını keşfedin.
- **Ajansın Sınırları:** Alan spesifik özerklik, altyapı bağımlılığı ve güvenlik sınırlarına saygı odaklanarak Agentic RAG'ın sınırlamalarını anlayın.
- **Pratik Kullanım Durumları ve Değer:** Doğruluk öncelikli ortamlar, karmaşık veri tabanı etkileşimleri ve uzun iş akışları gibi Agentic RAG'ın öne çıktığı senaryoları belirleyin.
- **Yönetim, Şeffaflık ve Güven:** Açıklanabilir akıl yürütme, önyargı kontrolü ve insan gözetimi dahil olmak üzere yönetim ve şeffaflığın önemini öğrenin.

## Agentic RAG Nedir?

Agentic Retrieval-Augmented Generation (Agentic RAG), büyük dil modellerinin (LLM'ler) dış kaynaklardan bilgi çekerken bir sonraki adımlarını bağımsız olarak planladığı yeni bir yapay zeka paradigmasıdır. Statik "bilgi getir-sonra oku" desenlerinden farklı olarak, Agentic RAG, araç veya fonksiyon çağrıları ve yapılandırılmış çıktılarla kesintiye uğrayan yinelemeli LLM çağrılarını içerir. Sistem sonuçları değerlendirir, sorguları iyileştirir, gerekirse ek araçlar çağırır ve tatmin edici bir çözüme ulaşana kadar bu döngüye devam eder. Bu yinelemeli “maker-checker” stili, doğruluğu artırır, hatalı sorguları ele alır ve yüksek kaliteli sonuçlar sağlar.

Sistem, başarısız sorguları yeniden yazarak, farklı bilgi getirme yöntemleri seçerek ve yanıtını tamamlamadan önce Azure AI Search'teki vektör arama, SQL veri tabanları veya özel API'ler gibi birden fazla aracı entegre ederek akıl yürütme sürecine aktif olarak sahip çıkar. Agentic bir sistemin ayırt edici özelliği, akıl yürütme sürecine sahip olma yeteneğidir. Geleneksel RAG uygulamaları önceden tanımlanmış yollara dayanırken, agentic bir sistem, bulduğu bilginin kalitesine dayalı olarak adımların sırasını bağımsız olarak belirler.

## Agentic Retrieval-Augmented Generation (Agentic RAG) Tanımı

Agentic Retrieval-Augmented Generation (Agentic RAG), büyük dil modellerinin (LLM'ler) yalnızca dış veri kaynaklarından bilgi çekmekle kalmayıp, aynı zamanda bir sonraki adımlarını bağımsız olarak planladığı bir yapay zeka geliştirme paradigmasıdır. Statik "bilgi getir-sonra oku" desenlerinden veya dikkatlice yazılmış istem dizilerinden farklı olarak, Agentic RAG, araç veya fonksiyon çağrıları ve yapılandırılmış çıktılarla kesintiye uğrayan yinelemeli LLM çağrıları döngüsünü içerir. Her adımda, sistem elde ettiği sonuçları değerlendirir, sorgularını iyileştirip iyileştirmeyeceğine karar verir, gerekirse ek araçlar çağırır ve tatmin edici bir çözüme ulaşana kadar bu döngüye devam eder.

Bu yinelemeli “maker-checker” çalışma stili, doğruluğu artırmak, yapılandırılmış veri tabanlarına yönelik hatalı sorguları ele almak (ör. NL2SQL) ve dengeli, yüksek kaliteli sonuçlar sağlamak için tasarlanmıştır. Sadece dikkatlice tasarlanmış istem zincirlerine güvenmek yerine, sistem akıl yürütme sürecine aktif olarak sahip çıkar. Başarısız olan sorguları yeniden yazabilir, farklı bilgi getirme yöntemleri seçebilir ve yanıtını tamamlamadan önce Azure AI Search'teki vektör arama, SQL veri tabanları veya özel API'ler gibi birden fazla aracı entegre edebilir. Bu, aşırı karmaşık orkestrasyon çerçevelerine olan ihtiyacı ortadan kaldırır. Bunun yerine, nispeten basit bir “LLM çağrısı → araç kullanımı → LLM çağrısı → …” döngüsü, sofistike ve iyi temellendirilmiş çıktılar sağlayabilir.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.tr.png)

## Akıl Yürütme Sürecine Sahip Olmak

Bir sistemi “agentic” yapan ayırt edici özellik, akıl yürütme sürecine sahip olma yeteneğidir. Geleneksel RAG uygulamaları genellikle model için bir yol önceden tanımlayan insanlara dayanır: neyin ne zaman getirileceğini özetleyen bir düşünce zinciri.
Ancak bir sistem gerçekten agentic olduğunda, problemi nasıl ele alacağına içsel olarak karar verir. Sadece bir komut dosyasını çalıştırmaz; bulduğu bilginin kalitesine dayalı olarak adımların sırasını bağımsız olarak belirler.
Örneğin, bir ürün lansman stratejisi oluşturması istendiğinde, tüm araştırma ve karar verme iş akışını açıklayan bir isteme tamamen güvenmez. Bunun yerine, agentic model bağımsız olarak şu kararları verir:

1. Bing Web Grounding kullanarak mevcut pazar trend raporlarını getirir.
2. Azure AI Search kullanarak ilgili rakip verilerini belirler.
3. Azure SQL Database kullanarak geçmiş iç satış metriklerini ilişkilendirir.
4. Azure OpenAI Service aracılığıyla koordine edilen bulguları bütüncül bir stratejiye sentezler.
5. Stratejiyi boşluklar veya tutarsızlıklar açısından değerlendirir ve gerekirse başka bir bilgi getirme turunu başlatır.
Tüm bu adımlar—sorguları iyileştirme, kaynakları seçme, yanıttan “memnun” olana kadar yineleme—model tarafından kararlaştırılır, bir insan tarafından önceden yazılmış değildir.

## Yinelemeli Döngüler, Araç Entegrasyonu ve Bellek

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.tr.png)

Agentic bir sistem, döngüsel bir etkileşim modeline dayanır:

- **İlk Çağrı:** Kullanıcının hedefi (ör. kullanıcı istemi) LLM'ye sunulur.
- **Araç Çağırma:** Model, eksik bilgi veya belirsiz talimatlar tespit ederse, daha fazla bağlam toplamak için bir araç veya bilgi getirme yöntemi seçer—örneğin, bir vektör veri tabanı sorgusu (ör. özel veriler üzerinde Azure AI Search Hibrit arama) veya yapılandırılmış bir SQL çağrısı.
- **Değerlendirme ve İyileştirme:** Dönen verileri gözden geçirdikten sonra, model bilginin yeterli olup olmadığına karar verir. Değilse, sorguyu iyileştirir, farklı bir araç dener veya yaklaşımını ayarlar.
- **Tatmin Olana Kadar Tekrarla:** Bu döngü, modelin nihai, iyi temellendirilmiş bir yanıt sunmak için yeterli netlik ve kanıta sahip olduğuna karar verene kadar devam eder.
- **Bellek ve Durum:** Sistem, adımlar arasında durumu ve belleği koruduğu için, önceki girişimleri ve sonuçlarını hatırlayabilir, tekrarlayan döngülerden kaçınabilir ve ilerledikçe daha bilinçli kararlar alabilir.

Zamanla, bu, modelin karmaşık, çok adımlı görevleri insanın sürekli müdahalesine veya istemi yeniden şekillendirmesine gerek kalmadan yönlendirmesini sağlayan bir gelişen anlayış hissi yaratır.

## Hata Modlarını Ele Alma ve Kendini Düzeltme

Agentic RAG’ın özerkliği, aynı zamanda sağlam kendini düzeltme mekanizmalarını da içerir. Sistem çıkmaza girdiğinde—örneğin, alakasız belgeler getirildiğinde veya hatalı sorgularla karşılaşıldığında—şunları yapabilir:

- **Yineleme ve Yeniden Sorgulama:** Düşük değerli yanıtlar döndürmek yerine, model yeni arama stratejileri dener, veri tabanı sorgularını yeniden yazar veya alternatif veri setlerine bakar.
- **Tanı Araçlarını Kullanma:** Sistem, akıl yürütme adımlarını hata ayıklamasına veya getirilen verilerin doğruluğunu doğrulamasına yardımcı olacak ek işlevler çağırabilir. Azure AI Tracing gibi araçlar, sağlam gözlemlenebilirlik ve izleme sağlamak için önemli olacaktır.
- **İnsan Gözetimine Başvurma:** Yüksek riskli veya tekrar tekrar başarısız olan senaryolar için model, belirsizliği işaretleyebilir ve insan rehberliği talep edebilir. İnsan düzeltici geri bildirim sağladıktan sonra, model bu dersi ileriye dönük olarak dahil edebilir.

Bu yinelemeli ve dinamik yaklaşım, modelin sürekli olarak gelişmesini sağlar ve yalnızca tek seferlik bir sistem değil, belirli bir oturum sırasında hatalarından öğrenen bir sistem olmasını sağlar.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.tr.png)

## Ajansın Sınırları

Bir görev içinde özerkliğine rağmen, Agentic RAG, Genel Yapay Zeka ile eşdeğer değildir. “Agentic” yetenekleri, insan geliştiriciler tarafından sağlanan araçlar, veri kaynakları ve politikalarla sınırlıdır. Kendi araçlarını icat edemez veya belirlenen alan sınırlarının dışına çıkamaz. Bunun yerine, elindeki kaynakları dinamik olarak düzenlemede mükemmeldir.
Daha gelişmiş yapay zeka biçimlerinden temel farklar şunlardır:

1. **Alan Spesifik Özerklik:** Agentic RAG sistemleri, kullanıcı tanımlı hedeflere bilinen bir alan içinde ulaşmaya odaklanır ve sonuçları iyileştirmek için sorgu yeniden yazma veya araç seçimi gibi stratejiler uygular.
2. **Altyapıya Bağımlılık:** Sistemin yetenekleri, geliştiriciler tarafından entegre edilen araçlara ve verilere bağlıdır. İnsan müdahalesi olmadan bu sınırları aşamaz.
3. **Güvenlik Sınırlarına Saygı:** Etik kurallar, uyumluluk kuralları ve iş politikaları çok önemlidir. Ajanın özgürlüğü her zaman güvenlik önlemleri ve gözetim mekanizmalarıyla sınırlıdır (umarız?).

## Pratik Kullanım Durumları ve Değer

Agentic RAG, yinelemeli iyileştirme ve hassasiyet gerektiren senaryolarda öne çıkar:

1. **Doğruluk Öncelikli Ortamlar:** Uyum kontrolleri, düzenleyici analiz veya hukuki araştırmalarda, agentic model tekrar tekrar gerçekleri doğrulayabilir, birden fazla kaynağa başvurabilir ve tamamen doğrulanmış bir yanıt üretene kadar sorguları yeniden yazabilir.
2. **Karmaşık Veri Tabanı Etkileşimleri:** Sorguların genellikle başarısız olduğu veya ayarlama gerektirdiği yapılandırılmış verilerle çalışırken, sistem, Azure SQL veya Microsoft Fabric OneLake kullanarak sorgularını bağımsız olarak iyileştirebilir ve nihai getirinin kullanıcının niyetiyle uyumlu olmasını sağlayabilir.
3. **Uzun Süreli İş Akışları:** Yeni bilgiler ortaya çıktıkça daha uzun süren oturumlar gelişebilir. Agentic RAG, sürekli olarak yeni verileri dahil edebilir ve problem alanı hakkında daha fazla bilgi edindikçe stratejileri değiştirebilir.

## Yönetim, Şeffaflık ve Güven

Bu sistemler akıl yürütmede daha özerk hale geldikçe, yönetim ve şeffaflık çok önemlidir:

- **Açıklanabilir Akıl Yürütme:** Model, yaptığı sorguların, başvurduğu kaynakların ve sonuca ulaşmak için izlediği akıl yürütme adımlarının bir denetim izini sağlayabilir. Azure AI Content Safety ve Azure AI Tracing / GenAIOps gibi araçlar, şeffaflığı korumaya ve riskleri azaltmaya yardımcı olabilir.
- **Önyargı Kontrolü ve Dengeli Bilgi Getirme:** Geliştiriciler, dengeli ve temsilci veri kaynaklarının dikkate alındığından emin olmak için bilgi getirme stratejilerini ayarlayabilir ve önyargı veya çarpık desenleri tespit etmek için çıktıları düzenli olarak denetleyebilir.
- **İnsan Gözetimi ve Uyumluluk:** Hassas görevler için insan incelemesi gerekli olmaya devam eder. Agentic RAG, yüksek riskli kararlarda insan yargısının yerini almaz—daha kapsamlı bir şekilde doğrulanmış seçenekler sunarak onu destekler.

Eylemlerin net bir kaydını sağlayan araçlara sahip olmak çok önemlidir. Bunlar olmadan, çok adımlı bir süreci hata ayıklamak çok zor olabilir. Chainlit'in arkasındaki Literal AI'den bir Ajan çalıştırma örneğine bakın:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.tr.png)

## Sonuç

Agentic RAG, yapay zeka sistemlerinin karmaşık, veri yoğun görevleri nasıl ele aldığı konusunda doğal bir evrimi temsil eder. Döngüsel bir etkileşim modeli benimseyerek, araçları bağımsız olarak seçerek ve yüksek kaliteli bir sonuca ulaşana kadar sorguları iyileştirerek, sistem statik istem takibinin ötesine geçerek daha uyarlanabilir, bağlama duyarlı bir karar verici haline gelir. Hâlâ insan tanımlı altyapılar ve etik kurallarla sınırlı olsa da, bu agentic yetenekler, hem işletmeler hem de son kullanıcılar için daha zengin, daha dinamik ve nihayetinde daha faydalı yapay zeka etkileşimlerini mümkün kılar.

### Agentic RAG hakkında daha fazla sorunuz mu var?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) sunucusuna katılarak diğer öğrenenlerle tanışabilir, ofis saatlerine katılabilir ve AI Agents ile ilgili sorularınıza yanıt alabilirsiniz.

## Ek Kaynaklar

-
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Azure OpenAI Hizmeti ile Geri Alım Destekli Üretim (RAG) Uygulaması: Azure OpenAI Hizmeti ile kendi verilerinizi nasıl kullanacağınızı öğrenin. Bu Microsoft Learn modülü, RAG uygulamasını gerçekleştirmek için kapsamlı bir rehber sunar.
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Azure AI Foundry ile üretken yapay zeka uygulamalarının değerlendirilmesi: Bu makale, kamuya açık veri setleri üzerinde modellerin değerlendirilmesi ve karşılaştırılmasını, Agentic AI uygulamaları ve RAG mimarilerini içerir</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Agentic RAG Nedir | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Temsilci Tabanlı Geri Alım Destekli Üretim için Tam Kılavuz – RAG'den haberler</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: sorgu yeniden biçimlendirme ve kendi kendine sorgu ile RAG'ınızı hızlandırın! Hugging Face Açık Kaynaklı AI Tarif Kitabı</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">RAG'e Agentic Katmanlar Eklemek</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Bilgi Asistanlarının Geleceği: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Agentic RAG Sistemleri Nasıl Kurulur</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Azure AI Foundry Agent Hizmeti ile AI temsilcilerinizi ölçeklendirme</a>

### Akademik Makaleler

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Kendine Geri Bildirim ile İteratif İyileştirme</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Sözel Pekiştirmeli Öğrenme ile Dil Temsilcileri</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Büyük Dil Modelleri Araç-İnteraktif Eleştiri ile Kendini Düzeltebilir</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Agentic RAG Üzerine Bir Araştırma</a>

## Önceki Ders

[Araç Kullanımı Tasarım Deseni](../04-tool-use/README.md)

## Sonraki Ders

[Güvenilir AI Temsilcileri Oluşturma](../06-building-trustworthy-agents/README.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.