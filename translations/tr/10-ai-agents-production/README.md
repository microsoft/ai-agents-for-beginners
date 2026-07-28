# Üretimde AI Ajanları: İzlenebilirlik & Değerlendirme

[![Üretimde AI Ajanları](../../../translated_images/tr/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

AI ajanları deneysel prototiplerden gerçek dünya uygulamalarına geçerken, davranışlarını anlamak, performanslarını izlemek ve çıktıları sistematik olarak değerlendirmek önem kazanmaktadır.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bilecek/anlayacaksınız:
- Ajan izlenebilirliği ve değerlendirmesinin temel kavramları
- Ajanların performansını, maliyetlerini ve etkinliğini artırmak için teknikler
- AI ajanlarınızı sistematik olarak neyi ve nasıl değerlendireceğiniz
- AI ajanlarını üretime alırken maliyetleri nasıl kontrol edeceğiniz
- Microsoft Agent Framework ile oluşturulan ajanları nasıl enstrüman edeceğiniz

Amaç, "kutu karası" ajanlarınızı şeffaf, yönetilebilir ve güvenilir sistemlere dönüştürme bilgisi ile donatmaktır.

_**Not:** Güvenli ve güvenilir AI ajanları dağıtmak önemlidir. Ayrıca [Güvenilir AI Ajanları Oluşturma](../06-building-trustworthy-agents/README.md) dersine de göz atın._

## İzler ve Aralıklar

[Langfuse](https://langfuse.com/) veya [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) gibi izlenebilirlik araçları genellikle ajan çalıştırmalarını izler (trace) ve aralıklar (span) olarak temsil eder.

- **İz (Trace):** Başlangıçtan sona bir ajan görevinin tamamını temsil eder (örneğin bir kullanıcı sorgusunu işlemek).
- **Aralıklar (Spans):** İz içindeki bireysel adımlardır (örneğin bir dil modeli çağrısı yapmak veya veri almak).

![Langfuse'da İzin Ağacı](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Resim URL'si açıklama amacıyla korunmuştur -->

İzlenebilirlik olmadan, bir AI ajanı "kara kutu" gibi olabilir - iç durumu ve mantığı opak olup, sorunları teşhis etmek veya performansı optimize etmek zorlaşır. İzlenebilirlikle ajanlar "cam kutular" haline gelir, bu da güven inşa etmek ve istenildiği gibi çalıştıklarından emin olmak için hayati şeffaflık sağlar. 

## Üretim Ortamlarında İzlenebilirliğin Önemi

AI ajanlarını üretim ortamlarına geçirmek yeni zorluklar ve gereksinimler getirir. İzlenebilirlik artık "iyi olur" değil, kritik bir yetenektir:

*   **Hata Ayıklama ve Kök Neden Analizi**: Bir ajan başarısız olduğunda veya beklenmedik çıktı ürettiğinde, izlenebilirlik araçları hata kaynağını belirlemek için gereken izleri sağlar. Bu, birden fazla LLM çağrısı, araç etkileşimleri ve koşullu mantık içeren karmaşık ajanlarda özellikle önemlidir.
*   **Gecikme ve Maliyet Yönetimi**: AI ajanları sıklıkla token başına veya çağrı başına ücretlendirilen LLM’lere ve diğer dış API'lere dayanır. İzlenebilirlik bu çağrıları hassas takip etmeye olanak tanır; aşırı yavaş veya pahalı operasyonları belirlemeye yardımcı olur. Bu, ekiplerin istemleri optimize etmelerini, daha verimli modeller seçmelerini veya iş akışlarını yeniden tasarlamalarını sağlayarak operasyonel maliyetleri yönetir ve iyi bir kullanıcı deneyimi garanti eder.
*   **Güven, Güvenlik ve Uyumluluk**: Birçok uygulamada ajanların güvenli ve etik davranması önemlidir. İzlenebilirlik ajanın eylemlerinin ve kararlarının denetim izini sağlar. Bu, istem enjeksiyonu, zararlı içerik üretimi veya kişisel tanımlayıcı bilgilerin (PII) kötü kullanımı gibi sorunları tespit edip azaltmak için kullanılabilir. Örneğin, bir ajan neden belirli bir yanıt verdiğini veya belirli bir aracı kullandığını anlamak için izler incelenebilir.
*   **Sürekli İyileştirme Döngüleri**: İzlenebilirlik verileri yinelemeli geliştirme sürecinin temelidir. Ekipler gerçek dünyadaki performansı izleyerek geliştirme alanlarını belirler, modelleri ince ayar yapmak için veri toplar ve değişiklik etkisini doğrular. Bu, çevrimiçi değerlendirmeden üretim içgörülerinin çevrimdışı deney ve iyileştirmeyi bilgilendirdiği geri bildirim döngüsü oluşturur, ajan performansını ilerledikçe artırır.

## Takip Edilecek Ana Metrixler

Ajan davranışını izlemek ve anlamak için çeşitli metrikler ve sinyaller takip edilmelidir. Spesifik metrikler ajanın amacına göre değişebilir, ancak bazıları evrensel olarak önemlidir.

İşte izlenebilirlik araçlarının takip ettiği en yaygın metriklerden bazıları:

**Gecikme (Latency):** Ajan ne kadar hızlı yanıt veriyor? Uzun bekleme süreleri kullanıcı deneyimini olumsuz etkiler. Görevler ve bireysel adımlar için gecikme sürelerini izleyerek ajan çalıştırmalarını takip etmelisiniz. Örneğin, tüm model çağrıları 20 saniye süren bir ajan daha hızlı bir model kullanarak veya model çağrılarını paralel yaparak hızlandırılabilir.

**Maliyetler:** Ajan çalıştırması başına ne kadar harcama oluyor? AI ajanları token başına ücretlendirilen LLM çağrılarına veya dış API'lere dayanır. Sık araç kullanımı veya çoklu istemler maliyetleri hızla artırabilir. Örneğin, küçük kalite artışı için bir ajan birkaç kez LLM çağırıyorsa, maliyetin haklı olup olmadığı ve çağrı sayısının azaltılıp azaltılamayacağı değerlendirilmelidir. Gerçek zamanlı izleme beklenmedik artışları (ör. aşırı API döngüleri oluşturan hatalar) tespit etmeye de yardımcı olur.

**İstek Hataları:** Ajan kaç istek yaparken başarısız oldu? Bu API hatalarını veya başarısız araç çağrılarını içerebilir. Üretimde ajanınızı bunlara karşı daha dayanıklı yapmak için yedekleme veya deneme mekanizmaları kurabilirsiniz. Örneğin, LLM sağlayıcı A kapalıysa, yedek olarak LLM sağlayıcı B'ye geçersiniz.

**Kullanıcı Geri Bildirimi:** Doğrudan kullanıcı değerlendirmeleri değerli içgörüler sağlar. Bu açık derecelendirmeler (👍beğeni/👎beğenmeme, ⭐1-5 yıldız) veya metin yorumları içerebilir. Sürekli olumsuz geri bildirim, ajanın beklenen şekilde çalışmadığının göstergesidir.

**Dolaylı Kullanıcı Geri Bildirimi:** Kullanıcı davranışları açık derecelendirme olmadan da dolaylı geri bildirim sağlar. Bu, hemen sorunun yeniden formüle edilmesi, tekrar eden sorgular veya yeniden dene düğmesine tıklanması gibi durumları içerir. Örneğin, kullanıcıların aynı soruyu tekrar tekrar sorması, ajanın beklenen şekilde çalışmadığının işaretidir.

**Doğruluk:** Ajan ne sıklıkla doğru veya istenilen çıktı üretir? Doğruluk tanımları değişir (örneğin, problem çözme doğruluğu, bilgi alma doğruluğu, kullanıcı memnuniyeti). İlk adım, ajanın başarısının neye benzediğini tanımlamaktır. Doğruluğu otomatik kontroller, değerlendirme puanları veya görev tamamlanma etiketleri ile takip edebilirsiniz. Örneğin, izleri "başarılı" veya "başarısız" olarak işaretlemek.

**Otomatik Değerlendirme Metrixleri:** Ayrıca otomatik değerlendirmeler kurabilirsiniz. Örneğin, bir LLM'yi ajanın çıktısını puanlamak için kullanabilirsiniz; yardımcı, doğru veya değil gibi. Ayrıca, ajanların farklı yönlerini puanlamanıza yardımcı olan çeşitli açık kaynak kütüphaneler vardır. Örneğin, RAG ajanları için [RAGAS](https://docs.ragas.io/) veya zararlı dil ve istem enjeksiyonunu tespit etmek için [LLM Guard](https://llm-guard.com/).

Pratikte, bu metriklerin kombinasyonu bir AI ajanın sağlığının en iyi kapsamını sağlar. Bu bölümün [örnek not defterinde](./code_samples/10-expense_claim-demo.ipynb) bu metriklerin gerçek örneklerde nasıl göründüğünü göstereceğiz, ancak önce tipik bir değerlendirme iş akışının nasıl olduğunu öğreneceğiz.

## Ajanınızı Enstrüman Edin

İzleme verisi toplamak için kodunuzu enstrüman etmeniz gerekir. Amaç, ajan kodunu izler ve metrikler yayacak şekilde enstrüman etmektir; böylece bunlar bir izlenebilirlik platformu tarafından yakalanabilir, işlenebilir ve görselleştirilebilir.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) LLM izlenebilirliği için sektör standardı olarak ortaya çıkmıştır. Telemetri verisi üretmek, toplamak ve dışa aktarmak için API’ler, SDK’lar ve araçlar seti sağlar.

OpenTelemetry aralıklarını izlenebilirlik aracına kolayca dışa aktarmak için var olan ajan çerçevelerini saran birçok enstrüman kütüphanesi vardır. Microsoft Agent Framework OpenTelemetry ile yerel olarak entegredir. Aşağıda bir MAF ajanını enstrüman etme örneği bulunmaktadır:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Ajan yürütmesi otomatik olarak izlenir
    pass
```

Bu bölümdeki [örnek not defteri](./code_samples/10-expense_claim-demo.ipynb) MAF ajanın nasıl enstrüman edileceğini gösterecek.

**Manuel Aralık Oluşturma:** Enstrüman kütüphaneleri iyi bir temel sağlar, ancak daha detaylı veya özel bilgi gerektiği durumlar olur. Özel uygulama mantığı eklemek için manuel olarak aralıklar oluşturabilirsiniz. Daha önemlisi, otomatik veya manuel oluşturulan aralıklar özel niteliklerle (etiketler veya meta veri olarak da bilinir) zenginleştirilebilir. Bu nitelikler işe özgü veriler, ara hesaplamalar veya hata ayıklama ve analiz için faydalı olabilecek bağlamlar içerebilir; örneğin `user_id`, `session_id` veya `model_version`.

[Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) ile manuel olarak izler ve aralıklar oluşturma örneği:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ajan Değerlendirmesi

İzlenebilirlik bize metrikler sağlar, ancak değerlendirme o verileri analiz etme (ve test yapma) sürecidir, AI ajanın ne kadar iyi performans gösterdiğini ve nasıl geliştirilebileceğini belirlemek için. Başka bir deyişle, izler ve metrikler elinizde olduğunda, bunları ajanı nasıl yargılamak ve karar vermek için kullanırsınız?

Düzenli değerlendirme önemlidir çünkü AI ajanları sıklıkla belirli olmaktan uzaktır ve evrilebilir (güncellemeler veya model davranışının kayması yoluyla) – değerlendirme olmadan, "akıllı ajanınızın" işini iyi yapıp yapmadığını veya gerilediğini bilemezsiniz.

AI ajanları için iki değerlendirme kategorisi vardır: **çevrimiçi değerlendirme** ve **çevrimdışı değerlendirme**. Her ikisi değerlidir ve birbirini tamamlar. Genellikle herhangi bir ajan dağıtmadan önce minimum gerekli adım olan çevrimdışı değerlendirme ile başlarız.

### Çevrimdışı Değerlendirme

![Langfuse’de Veri Kümesi Öğeleri](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Bu, ajanı kontrollü bir ortamda, genellikle canlı kullanıcı sorguları yerine test veri kümeleri kullanarak değerlendirmeyi içerir. Beklenen çıktı veya doğru davranışı bildiğiniz özenle hazırlanmış veri kümeleri kullanılır ve ajanın bunlar üzerinde çalıştırılır.

Örneğin, bir matematik kelime problemleri ajanı oluşturduysanız, bilinen cevapları olan 100 problemsel [test veri kümeniz](https://huggingface.co/datasets/gsm8k) olabilir. Çevrimdışı değerlendirme genellikle geliştirme sırasında (ve CI/CD hatlarının bir parçası olabilir) iyileştirmeler kontrolü veya gerilemeleri engellemek için yapılır. Faydası **tekrarlanabilir olması ve temel gerçek bilginizin olduğu durumlarda net doğruluk metrikleri alabilmenizdir**. Ayrıca kullanıcı sorgularını simüle edip ajanın yanıtlarını ideal cevaplara karşı ölçebilir veya yukarıda açıklandığı gibi otomatik metrikler kullanabilirsiniz.

Çevrimdışı değerlendirmenin temel zorluğu test veri kümenizin kapsamlı ve güncel kalmasını sağlamaktır – ajan sabit bir test setinde iyi performans gösterse bile üretimde çok farklı sorgularla karşılaşabilir. Bu nedenle, gerçek dünya senaryolarını yansıtan yeni uç durumlar ve örneklerle test setlerini güncel tutmalısınız. Küçük “duman testi” vakaları ile daha geniş performans metrikleri için büyük değerlendirme setlerinin karışımı yararlıdır: hızlı kontroller için küçük setler ve daha geniş performans için büyük setler.

### Çevrimiçi Değerlendirme

![İzlenebilirlik metrikleri genel bakışı](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Bu, ajanın canlı, gerçek dünya ortamında, yani üretimde gerçek kullanım sırasında değerlendirilmesini ifade eder. Çevrimiçi değerlendirme gerçek kullanıcı etkileşimlerinde ajanın performansını izler ve sonuçları sürekli analiz eder.

Örneğin, canlı trafiğe başarı oranları, kullanıcı memnuniyeti puanları veya diğer metrikleri takip edebilirsiniz. Çevrimiçi değerlendirmenin avantajı **bir laboratuvar ortamında beklemediğiniz şeyleri yakalayabilmesidir** – zamanla modelin kaymasını (ajanın etkinliğinin girdi kalıpları değiştikçe azalması) gözlemleyebilir ve test verilerinizde olmayan beklenmedik sorgular veya durumları yakalayabilirsiniz. Bu, ajanın doğal ortamda nasıl davrandığına gerçek bir bakış sağlar.

Çevrimiçi değerlendirme genellikle dolaylı ve açık kullanıcı geri bildirimleri toplamayı içerir ve mümkünse yeni ajan sürümü eskiyle karşılaştırmak için paralel koşan gölge testleri veya A/B testleri yapılır. Zorluk, canlı etkileşimler için güvenilir etiketler veya puanlar almak olabilir – kullanıcı geri bildirimi veya sonrasında ölçülen metriklere (örneğin, kullanıcının sonucu tıklayıp tıklamadığı) dayanabilirsiniz.

### İkisini Kombinlemek

Çevrimiçi ve çevrimdışı değerlendirmeler birbirini dışlamaz; oldukça tamamlayıcıdır. Çevrimiçi izlemeden gelen içgörüler (örneğin, ajanın zayıf performans gösterdiği yeni kullanıcı sorgusu türleri) çevrimdışı test veri kümelerini artırmak ve geliştirmek için kullanılabilir. Tersine, çevrimdışı testlerde iyi performans gösteren ajanlar daha güvenle dağıtılır ve çevrimiçi olarak izlenir.

Aslında birçok ekip şu döngüyü benimser:

_çevrimdışı değerlendirme -> dağıtım -> çevrimiçi izleme -> yeni başarısızlık vakaları toplama -> çevrimdışı veri setine ekleme -> ajanı iyileştirme -> tekrarlama_.

## Yaygın Sorunlar

AI ajanlarını üretime alırken çeşitli zorluklarla karşılaşabilirsiniz. İşte bazı yaygın sorunlar ve olası çözümler:

| **Sorun**    | **Olası Çözüm**   |
| ------------- | ------------------ |
| AI Ajanı işleri tutarlı şekilde yapamıyor | - Ajan için verilen istemi netleştirin ve hedefleri açık yapın.<br>- Görevleri alt görevlere bölmek ve bunları birden fazla ajanla halletmek yardımcı olabilir.<br> |
| AI Ajanı sürekli döngülere giriyor | - Ajanın süreci ne zaman durduracağını bilmesi için açık bitirme koşulları oluşturun.<br>- Akıl yürütme ve planlama gerektiren karmaşık görevlerde, bu işleri için özel büyük model kullanın.<br> |
| AI Ajan arac çağrıları iyi performans göstermiyor | - Aracın çıktısını ajan sisteminin dışında test edip doğrulayın.<br>- Tanımlanan parametreleri, istemleri ve araç adlandırmalarını gözden geçirin.<br> |
| Çoklu Ajan sistemi tutarlı çalışmıyor | - Her ajana verilen istemleri özel ve birbirinden farklı olacak şekilde düzenleyin.<br>- Doğru ajanı belirlemek için "yönlendirme" veya kontrol ajanı kullanarak hiyerarşik sistem kurun.<br> |

Bu sorunların çoğu izlenebilirlik sayesinde daha etkili tespit edilebilir. Daha önce bahsettiğimiz izler ve metrikler, ajan iş akışında sorunların nerede olduğunu tam olarak bulmaya yardımcı olarak hata ayıklamayı ve optimizasyonu çok daha verimli kılar.

## Maliyet Yönetimi


AI ajanlarını üretime dağıtmanın maliyetlerini yönetmek için bazı stratejiler şunlardır:

**Daha Küçük Modeller Kullanmak:** Küçük Dil Modelleri (SLM'ler) belirli ajan kullanım durumlarında iyi performans gösterebilir ve maliyetleri önemli ölçüde düşürür. Daha önce de belirtildiği gibi, bir değerlendirme sistemi kurmak ve performansı daha büyük modellerle karşılaştırmak, bir SLM'nin kullanım durumunuzda ne kadar iyi performans göstereceğini anlamanın en iyi yoludur. Basit görevler için örneğin niyet sınıflandırması veya parametre çıkarımı gibi, SLM'leri kullanmayı düşünün; karmaşık muhakeme için ise daha büyük modelleri ayırın.

**Yönlendirici Model Kullanmak:** Benzer bir strateji, çeşitli model ve boyutlar kullanmaktır. LLM/SLM veya sunucusuz fonksiyonlar kullanarak, karmaşıklığa göre isteği en uygun modellere yönlendirebilirsiniz. Bu, maliyetleri azaltmaya yardımcı olurken doğru görevlerde performansı da sağlar. Örneğin, basit sorguları daha küçük, hızlı modellere yönlendirin ve yalnızca karmaşık muhakeme görevleri için pahalı büyük modelleri kullanın.

**Yanıtları Önbelleğe Alma:** Ortak istek ve görevleri tanımlayıp, yanıtları ajanik sisteminizden geçmeden önce sağlamak, benzer istek hacmini azaltmanın iyi bir yoludur. Daha temel AI modelleri kullanarak bir isteğin önbelleğe alınmış isteklere ne kadar benzediğini belirlemek için bir akış bile uygulayabilirsiniz. Bu strateji, sık sorulan sorular veya yaygın işler için maliyetleri önemli ölçüde azaltabilir.

## Pratikte bunun nasıl çalıştığını görelim

[Bu bölümün örnek not defterinde](./code_samples/10-expense_claim-demo.ipynb), ajanımızı izlemek ve değerlendirmek için gözlemlenebilirlik araçlarını nasıl kullanabileceğimize dair örnekler göreceğiz.


### Üretimde AI Ajanları hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, çalışma saatlerine katılmak ve AI Ajanları sorularınıza yanıt almak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) topluluğuna katılın.

## Önceki Ders

[Metakognisyon Tasarım Deseni](../09-metacognition/README.md)

## Sonraki Ders

[Ajanik Protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->