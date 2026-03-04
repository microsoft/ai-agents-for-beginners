# Üretimde Yapay Zeka Ajanları: Gözlemlenebilirlik ve Değerlendirme

[![Üretimde Yapay Zeka Ajanları](../../../translated_images/tr/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Yapay zeka ajanları deneysel prototiplerden gerçek dünya uygulamalarına geçtikçe, davranışlarını anlamak, performanslarını izlemek ve çıktıları sistematik olarak değerlendirmek önem kazanır.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bilecek/anlayacaksınız:
- Ajan gözlemlenebilirliği ve değerlendirmesinin temel kavramları
- Ajanların performansını, maliyetlerini ve etkililiğini artırma teknikleri
- Yapay zeka ajanlarınızı sistematik olarak neyi ve nasıl değerlendireceğiniz
- Yapay zeka ajanlarını üretime dağıtırken maliyetleri nasıl kontrol edeceğiniz
- AutoGen ile oluşturulmuş ajanları nasıl enstrümante edeceğiniz

Amaç, "kara kutu" ajanlarınızı şeffaf, yönetilebilir ve güvenilir sistemlere dönüştürmeniz için gerekli bilgiyle donatmaktır.

_**Not:** Güvenli ve güvenilir Yapay Zeka Ajanları dağıtmak önemlidir. Ayrıca [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md) dersine göz atın._

## İzler ve Span'lar

Langfuse veya Microsoft Foundry gibi gözlemlenebilirlik araçları genellikle ajan çalıştırmalarını izler (traces) ve span'lar olarak temsil eder.

- **İz (Trace)** bir kullanıcının sorgusunu ele almak gibi, bir ajan görevini baştan sona temsil eder.
- **Span'lar** iz içindeki bireysel adımlardır (ör. bir dil modelini çağırma veya veri alma gibi).

![Langfuse'da iz ağacı](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Gözlemlenebilirlik olmadan bir Yapay Zeka ajanı "siyah kutu" gibi hissedilebilir — iç durumu ve muhakemesi opak olur, bu da sorunları teşhis etmeyi veya performansı optimize etmeyi zorlaştırır. Gözlemlenebilirlikle birlikte ajanlar "cam kutular"a dönüşür; bu şeffaflık güven oluşturmak ve istenildiği gibi çalıştıklarından emin olmak için hayati önem taşır. 

## Üretim Ortamlarında Gözlemlenebilirliğin Önemi

Yapay zeka ajanlarını üretim ortamlarına geçirmek yeni bir dizi zorluk ve gereksinim getirir. Gözlemlenebilirlik artık "olması güzel olur" değil, kritik bir yetenektir:

*   **Hata Ayıklama ve Kök Neden Analizi:** Bir ajan başarısız olduğunda veya beklenmedik bir çıktı ürettiğinde, gözlemlenebilirlik araçları hatanın kaynağını belirlemek için gereken izleri sağlar. Bu, birçok LLM çağrısı, araç etkileşimleri ve koşullu mantık içerebilen karmaşık ajanlarda özellikle önemlidir.
*   **Gecikme (Latency) ve Maliyet Yönetimi:** Yapay zeka ajanları genellikle token başına veya çağrı başına ücretlendirilen LLM'lere ve diğer harici API'lere dayanır. Gözlemlenebilirlik bu çağrıların hassas izlenmesini sağlar ve aşırı yavaş veya pahalı işlemleri belirlemeye yardımcı olur. Bu, ekiplerin istemleri optimize etmesine, daha verimli modeller seçmesine veya operasyonel maliyetleri yönetmek ve iyi bir kullanıcı deneyimi sağlamak için iş akışlarını yeniden tasarlamasına olanak tanır.
*   **Güven, Güvenlik ve Uyum:** Birçok uygulamada ajanların güvenli ve etik şekilde davrandığından emin olmak önemlidir. Gözlemlenebilirlik ajan eylemlerinin ve kararlarının denetim izini sağlar. Bu, prompt enjeksiyonu, zararlı içerik üretimi veya kişisel olarak tanımlanabilir bilgilerin (PII) yanlış ele alınması gibi sorunları tespit edip hafifletmek için kullanılabilir. Örneğin, bir ajanın belirli bir yanıtı neden verdiğini veya neden belli bir aracı kullandığını anlamak için izleri inceleyebilirsiniz.
*   **Sürekli İyileştirme Döngüleri:** Gözlemlenebilirlik verileri yinelemeli bir geliştirme sürecinin temelidir. Ajanların gerçek dünyadaki performansını izleyerek ekipler iyileştirme alanlarını belirleyebilir, modelleri ince ayar için veri toplayabilir ve değişikliklerin etkisini doğrulayabilir. Bu, üretimden elde edilen çevrimiçi değerlendirme içgörülerinin çevrimdışı deneyleri ve iyileştirmeleri bilgilendirdiği bir geri bildirim döngüsü oluşturur; böylece ajan performansı kademeli olarak iyileşir.

## İzlenecek Temel Metrikler

Ajan davranışını izlemek ve anlamak için bir dizi metrik ve sinyal izlenmelidir. Spesifik metrikler ajanın amacına göre değişse de, bazıları evrensel olarak önemlidir.

Gözlemlenebilirlik araçlarının izlediği en yaygın metriklerden bazıları şunlardır:

**Gecikme:** Ajan ne kadar hızlı yanıt veriyor? Uzun bekleme süreleri kullanıcı deneyimini olumsuz etkiler. Ajan çalıştırmalarını izleyerek görevler ve bireysel adımlar için gecikmeyi ölçmelisiniz. Örneğin, tüm model çağrıları için 20 saniye alan bir ajan, daha hızlı bir model kullanılarak veya model çağrılarını paralel çalıştırarak hızlandırılabilir.

**Maliyetler:** Bir ajan çalıştırmasının maliyeti nedir? Yapay zeka ajanları token başına ücretlendirilen LLM çağrılarına veya harici API'lere dayanır. Sık araç kullanımı veya birden çok istem maliyetleri hızla artırabilir. Örneğin, bir ajan kaliteyi marjinal olarak iyileştirmek için bir LLM'yi beş kez çağırıyorsa, maliyetin haklı olup olmadığını veya çağrı sayısını azaltıp daha ucuz bir model kullanıp kullanamayacağınızı değerlendirmelisiniz. Gerçek zamanlı izleme ayrıca beklenmedik sıçramaları (ör. aşırı API döngülerine neden olan hatalar) tespit etmeye yardımcı olabilir.

**İstek Hataları:** Ajan kaç istekte başarısız oldu? Bu, API hatalarını veya başarısız araç çağrılarını içerebilir. Üretimde bu tür hatalara karşı ajanın daha dayanıklı olması için geriye dönüşler veya yeniden denemeler ayarlayabilirsiniz. Örn. LLM sağlayıcısı A devre dışıysa, yedek olarak LLM sağlayıcısı B'ye geçersiniz.

**Kullanıcı Geri Bildirimi:** Doğrudan kullanıcı değerlendirmelerini uygulamak değerli bilgiler sağlar. Bu, açık derecelendirmeleri (👍thumbs-up/👎down, ⭐1-5 yıldız) veya metin yorumlarını içerebilir. Tutarlı olumsuz geri bildirim, ajanın beklenildiği gibi çalışmadığının bir işareti olarak sizi uyarmalıdır. 

**Dolaylı Kullanıcı Geri Bildirimi:** Kullanıcı davranışları açık bir derecelendirme olmasa bile dolaylı geri bildirim sağlar. Bu, hemen soru yeniden ifade etme, tekrar eden sorgular veya yeniden deneme düğmesine tıklama gibi eylemleri içerebilir. Örn. kullanıcıların aynı soruyu tekrar tekrar sorduğunu görüyorsanız, bu ajanın beklenildiği gibi çalışmadığının bir işaretidir.

**Doğruluk:** Ajan ne sıklıkla doğru veya istenen çıktılar üretiyor? Doğruluk tanımları değişir (ör. problem çözme doğruluğu, bilgi alma doğruluğu, kullanıcı memnuniyeti). İlk adım, ajanın başarı için neye benzediğini tanımlamaktır. Doğruluğu otomatik kontroller, değerlendirme puanları veya görev tamamlama etiketleri ile izleyebilirsiniz. Örneğin, izleri "başarılı" veya "başarısız" olarak işaretlemek.

**Otomatik Değerlendirme Metrikleri:** Otomatik değerlendirmeler de kurabilirsiniz. Örneğin, bir LLM kullanarak ajanın çıktısını yardımcı olup olmadığı, doğru olup olmadığı gibi kriterlere göre puanlayabilirsiniz. Ayrıca ajanın farklı yönlerini puanlamanıza yardımcı olan birçok açık kaynak kütüphane vardır. Örn. RAG ajanları için [RAGAS](https://docs.ragas.io/) veya zararlı dil veya prompt enjeksiyonunu tespit etmek için [LLM Guard](https://llm-guard.com/).

Pratikte, bu metriklerin bir kombinasyonu bir Yapay Zeka ajanının sağlığı hakkında en iyi kapsamı sağlar. Bu bölümün [örnek not defterinde](./code_samples/10_autogen_evaluation.ipynb), bu metriklerin gerçek örneklerde nasıl göründüğünü göstereceğiz ama önce tipik bir değerlendirme iş akışının nasıl göründüğünü öğreneceğiz.

## Ajanınızı Enstrümante Edin

İzleme verisi toplamak için kodunuzu enstrümante etmeniz gerekir. Amaç, bir gözlemlenebilirlik platformu tarafından yakalanabilecek, işlenebilecek ve görselleştirilebilecek izler ve metrikler yayınlayacak şekilde ajan kodunu enstrümante etmektir.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) LLM gözlemlenebilirliği için endüstri standardı olarak ortaya çıktı. Telemetri verisi üretmek, toplamak ve dışa aktarmak için bir dizi API, SDK ve araç sağlar. 

Mevcut ajan çerçevelerini saran ve OpenTelemetry span'larını bir gözlemlenebilirlik aracına kolayca aktarmayı sağlayan birçok enstrümantasyon kütüphanesi vardır. Aşağıda AutoGen ajanını [OpenLit enstrümantasyon kütüphanesi](https://github.com/openlit/openlit) ile enstrümante etmeye dair bir örnek bulunmaktadır:

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

Bu bölümdeki [örnek not defteri](./code_samples/10_autogen_evaluation.ipynb) AutoGen ajanınızı nasıl enstrümante edeceğinizi gösterecektir.

**Manuel Span Oluşturma:** Enstrümantasyon kütüphaneleri iyi bir temel sağlasa da, daha ayrıntılı veya özel bilgi gerektiği durumlar sıkça olur. Özel uygulama mantığı eklemek için span'lar manuel olarak oluşturabilirsiniz. Daha da önemlisi, otomatik veya manuel oluşturulmuş span'ları özel özniteliklerle (etiketler veya meta veriler olarak da bilinir) zenginleştirebilirsiniz. Bu öznitelikler, işe özgü veriler, ara hesaplamalar veya hata ayıklama ya da analiz için faydalı olabilecek herhangi bir bağlamı içerebilir; örneğin `user_id`, `session_id` veya `model_version`.

[Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) ile izleri ve span'ları manuel oluşturma örneği:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ajan Değerlendirmesi

Gözlemlenebilirlik bize metrikler verir, ancak değerlendirme bu verileri (ve testleri yürütmeyi) analiz ederek bir Yapay Zeka ajanının ne kadar iyi performans gösterdiğini ve nasıl iyileştirilebileceğini belirleme sürecidir. Başka bir deyişle, bu izlere ve metriklere sahip olduğunuzda bunları ajanın yargılanması ve kararlar alınması için nasıl kullanırsınız?

Düzenli değerlendirme önemlidir çünkü Yapay Zeka ajanları genellikle deterministik değildir ve güncellemeler veya model davranışı kayması yoluyla evrilebilirler – değerlendirme olmadan "akıllı ajanın" gerçekten işini iyi yapıp yapmadığını veya gerileyip gerilemediğini bilemezsiniz.

Yapay zeka ajanları için iki değerlendirme kategorisi vardır: **çevrimiçi değerlendirme** ve **çevrimdışı değerlendirme**. Her ikisi de değerlidir ve birbirini tamamlar. Genellikle herhangi bir ajan dağıtmadan önce minimum gerekli adım olan çevrimdışı değerlendirme ile başlarız.

### Çevrimdışı Değerlendirme

![Langfuse'da veri seti öğeleri](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Bu, ajanı canlı kullanıcı sorguları yerine tipik olarak test veri setleri kullanarak kontrollü bir ortamda değerlendirmeyi içerir. Beklenen çıktının veya doğru davranışın ne olduğunu bildiğiniz küratörlü veri setlerini kullanırsınız ve ardından ajanınızı bunlar üzerinde çalıştırırsınız.

Örneğin, bir matematik kelime problemi ajanı oluşturduysanız, bilinen cevapları olan 100 problemin bulunduğu bir [test veri setiniz](https://huggingface.co/datasets/gsm8k) olabilir. Çevrimdışı değerlendirme genellikle geliştirme sırasında (ve CI/CD boru hatlarının bir parçası olabilir) iyileştirmeleri kontrol etmek veya regresyonlara karşı koruma sağlamak için yapılır. Yararı, **tekrar edilebilir olması ve gerçek doğruluk ölçümlerine ulaşabilmenizdir çünkü doğruluk zemini (ground truth) vardır**. Ayrıca kullanıcı sorgularını simüle edebilir ve ajanın yanıtlarını ideal cevaplarla karşılaştırabilir veya yukarıda açıklandığı gibi otomatik metrikler kullanabilirsiniz.

Çevrimdışı değerlendirmedeki temel zorluk, test veri setinizin kapsamlı ve ilgili kalmasını sağlamaktır – ajan sabit bir test kümesinde iyi performans gösterebilir ancak üretimde çok farklı sorgularla karşılaşabilir. Bu nedenle test kümelerini gerçek dünya senaryolarını yansıtan yeni uç durumlar ve örneklerle güncel tutmalısınız. Küçük "duman testi" vakaları ile daha geniş performans metrikleri için daha büyük değerlendirme setlerinin karışımı faydalıdır: hızlı kontroller için küçük setler ve daha geniş performans ölçümleri için büyük setler.

### Çevrimiçi Değerlendirme

![Gözlemlenebilirlik metrikleri genel görünümü](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Bu, ajanı canlı, gerçek dünya ortamında, yani üretimdeki gerçek kullanım sırasında değerlendirmeyi ifade eder. Çevrimiçi değerlendirme, ajanın gerçek kullanıcı etkileşimlerindeki performansını izlemeyi ve sonuçları sürekli analiz etmeyi içerir.

Örneğin, canlı trafik üzerinde başarı oranlarını, kullanıcı memnuniyeti puanlarını veya diğer metrikleri izleyebilirsiniz. Çevrimiçi değerlendirmenin avantajı, laboratuvar ortamında öngöremeyebileceğiniz şeyleri yakalamasıdır — model kaymasını zaman içinde gözlemleyebilir (ajanın etkinliği, giriş örüntüleri değiştikçe düşebilir) ve test verilerinizde olmayan beklenmedik sorguları veya durumları yakalayabilirsiniz. Bu, ajanın vahşi doğadaki davranışının gerçek bir resmini sağlar.

Çevrimiçi değerlendirme genellikle yukarıda tartışıldığı gibi dolaylı ve doğrudan kullanıcı geri bildirimlerini toplamayı içerir ve gölge testleri veya A/B testleri (yeni bir ajan sürümünün eskiyle karşılaştırmak için paralel çalıştırılması) yürütmeyi içerebilir. Zorluk, canlı etkileşimler için güvenilir etiketler veya puanlar elde etmenin zor olabilmesidir – kullanıcı geri bildirimine veya aşağı akış metriklerine (ör. kullanıcı sonucu tıkladı mı) güvenebilirsiniz.

### İkisinin Birleştirilmesi

Çevrimiçi ve çevrimdışı değerlendirmeler birbirini dışlamaz; birbirini tamamlarlar. Çevrimiçi izlemeden elde edilen içgörüler (örn. ajanın kötü performans gösterdiği yeni kullanıcı sorgusu türleri) çevrimdışı test veri setlerini zenginleştirmek ve geliştirmek için kullanılabilir. Tersine, çevrimdışı testlerde iyi performans gösteren ajanlar daha emin bir şekilde dağıtılıp çevrimiçi olarak izlenebilir.

Aslında birçok ekip şu döngüyü benimser:

_değerlendir (çevrimdışı) -> dağıt -> çevrimiçi izle -> yeni hata vakaları topla -> çevrimdışı veri setine ekle -> ajanı iyileştir -> tekrar_.

## Yaygın Sorunlar

Yapay zeka ajanlarını üretime dağıtırken çeşitli zorluklarla karşılaşabilirsiniz. İşte bazı yaygın sorunlar ve olası çözümleri:

| **Sorun**    | **Olası Çözüm**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Refine the prompt given to the AI Agent; be clear on objectives.<br>- Identify where dividing the tasks into subtasks and handling them by multiple agents can help. |
| AI Agent running into continuous loops  | - Ensure you have clear termination terms and conditions so the Agent knows when to stop the process.<br>- For complex tasks that require reasoning and planning, use a larger model that is specialized for reasoning tasks. |
| AI Agent tool calls are not performing well   | - Test and validate the tool's output outside of the agent system.<br>- Refine the defined parameters, prompts, and naming of tools.  |
| Multi-Agent system not performing consistently | - Refine prompts given to each agent to ensure they are specific and distinct from one another.<br>- Build a hierarchical system using a "routing" or controller agent to determine which agent is the correct one. |

Bu sorunların birçoğu gözlemlenebilirlik sağlandığında daha etkili bir şekilde tanımlanabilir. Daha önce tartıştığımız izler ve metrikler, ajan iş akışında sorunların tam olarak nerede meydana geldiğini belirlemeye yardımcı olur ve hata ayıklama ile optimizasyonu çok daha verimli hale getirir.

## Maliyet Yönetimi
İşte yapay zeka ajanlarını üretime dağıtmanın maliyetlerini yönetmek için bazı stratejiler:

**Küçük Modeller Kullanma:** Küçük Dil Modelleri (SLMs) belirli ajan tabanlı kullanım durumlarında iyi performans gösterebilir ve maliyetleri önemli ölçüde azaltır. Daha önce belirtildiği gibi, performansı belirlemek ve daha büyük modellerle karşılaştırmak için bir değerlendirme sistemi oluşturmak, bir SLM'in kullanım durumunuzda ne kadar iyi performans göstereceğini anlamanın en iyi yoludur. Niyet sınıflandırması veya parametre çıkarımı gibi daha basit görevler için SLM'leri kullanmayı düşünün; karmaşık akıl yürütme için ise daha büyük modelleri ayırın.

**Yönlendirici Model Kullanma:** Benzer bir strateji, farklı modeller ve boyutlar kullanmaktır. İstekleri karmaşıklığa göre en uygun modellere yönlendirmek için bir LLM/SLM veya sunucusuz fonksiyon kullanabilirsiniz. Bu, doğru görevlerde performansı sağlarken maliyetleri azaltmaya da yardımcı olur. Örneğin, basit sorguları daha küçük, daha hızlı modellere yönlendirin ve pahalı büyük modelleri yalnızca karmaşık akıl yürütme görevleri için kullanın.

**Yanıtları Önbellekleme:** Yaygın istekleri ve görevleri belirleyip yanıtları ajan sisteminizden geçmeden önce sağlamak, benzer isteklerin hacmini azaltmanın iyi bir yoludur. Daha temel yapay zeka modelleri kullanarak bir isteğin önbelleğe alınmış isteklerinize ne kadar benzediğini belirleyen bir akış bile uygulayabilirsiniz. Bu strateji, sık sorulan sorular veya ortak iş akışları için maliyetleri önemli ölçüde azaltabilir.

## Uygulamada bunun nasıl çalıştığını görelim

Bu bölümün [örnek not defterinde](./code_samples/10_autogen_evaluation.ipynb), ajanımızı izlemek ve değerlendirmek için gözlemlenebilirlik araçlarını nasıl kullanabileceğimize dair örnekler göreceğiz.

### Üretimdeki Yapay Zeka Ajanları Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve Yapay Zeka Ajanları ile ilgili sorularınıza yanıt almak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)'a katılın.

## Önceki Ders

[Metakognisyon Tasarım Deseni](../09-metacognition/README.md)

## Sonraki Ders

[Ajanik Protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Feragatname:
Bu belge, yapay zeka (YZ) çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hâli yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek herhangi bir yanlış anlaşılma veya hatalı yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->