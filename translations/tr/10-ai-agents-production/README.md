# Üretimde AI Ajanları: Gözlemlenebilirlik ve Değerlendirme

[![Üretimde AI Ajanları](../../../translated_images/tr/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

AI ajanları deneysel prototiplerden gerçek dünya uygulamalarına doğru ilerledikçe, davranışlarını anlamak, performanslarını izlemek ve çıktıları sistematik olarak değerlendirmek önem kazanır.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bilecek/anlayacaksınız:
- Ajan gözlemlenebilirliği ve değerlendirmesinin temel kavramları
- Ajanların performansını, maliyetlerini ve etkinliğini iyileştirme teknikleri
- AI ajanlarınızı neyin ve nasıl sistematik olarak değerlendireceğiniz
- AI ajanlarını üretime dağıtırken maliyetleri nasıl kontrol edeceğiniz
- Microsoft Agent Framework ile oluşturulmuş ajanları nasıl enstrümante edeceğiniz

Amaç, "kara kutu" ajanlarınızı şeffaf, yönetilebilir ve güvenilir sistemlere dönüştürmek için gerekli bilgiyle donatmaktır.

_**Not:** Güvenli ve güvenilir AI Ajanları dağıtmak önemlidir. Ayrıca [Güvenilir AI Ajanları Oluşturma](./06-building-trustworthy-agents/README.md) dersine göz atın._

## İzler ve Span'lar

Gözlemlenebilirlik araçları, örneğin [Langfuse](https://langfuse.com/) veya [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), genellikle ajan çalıştırmalarını izler ve span'lar olarak temsil eder.

- **İz (Trace)**, bir ajan görevini baştan sona (ör. bir kullanıcı sorgusunu işleme) temsil eder.
- **Span'lar** iz içindeki bireysel adımlardır (ör. bir dil modelini çağırma veya veri getirme gibi).

![Langfuse'ta iz ağacı](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Gözlemlenebilirlik olmadan, bir AI ajanı "kara kutu" gibi gelebilir — iç durumu ve muhakemesi opak olur, bu da sorunları teşhis etmeyi veya performansı optimize etmeyi zorlaştırır. Gözlemlenebilirlikle ajanlar "cam kutular" haline gelir; bu, güven oluşturmak ve beklenen şekilde çalıştıklarından emin olmak için hayati bir şeffaflık sağlar. 

## Gözlemlenebilirliğin Üretim Ortamlarında Neden Önemli Olduğu

AI ajanlarını üretim ortamlarına taşımak yeni zorluklar ve gereksinimler getirir. Gözlemlenebilirlik artık "iyi olur" seviyesinde değil, kritik bir yetenektir:

*   **Hata Ayıklama ve Kök Neden Analizi**: Bir ajan başarısız olduğunda veya beklenmeyen bir çıktı ürettiğinde, gözlemlenebilirlik araçları hatanın kaynağını belirlemek için gereken izleri sağlar. Bu, birden çok LLM çağrısı, araç etkileşimleri ve koşullu mantık içerebilen karmaşık ajanlarda özellikle önemlidir.
*   **Gecikme ve Maliyet Yönetimi**: AI ajanları sıklıkla token başına veya çağrı başına faturalandırılan LLM'ler ve diğer harici API'lere dayanır. Gözlemlenebilirlik bu çağrıların hassas takibini sağlar, aşırı yavaş veya pahalı işlemleri tespit etmeye yardımcı olur. Bu, ekiplerin prompt'ları optimize etmesini, daha verimli modeller seçmesini veya operasyonel maliyetleri yönetmek ve iyi bir kullanıcı deneyimi sağlamak için iş akışlarını yeniden tasarlamasını mümkün kılar.
*   **Güven, Güvenlik ve Uyumluluk**: Birçok uygulamada, ajanların güvenli ve etik davranmasını sağlamak önemlidir. Gözlemlenebilirlik ajan eylemlerinin ve kararlarının bir denetleme izini sağlar. Bu, prompt enjeksiyonu, zararlı içerik üretimi veya kişisel olarak tanımlanabilir bilgilerin (PII) yanlış kullanımı gibi sorunları tespit etmek ve hafifletmek için kullanılabilir. Örneğin, bir ajanın belirli bir yanıtı neden verdiğini veya belirli bir aracı neden kullandığını anlamak için izleri inceleyebilirsiniz.
*   **Sürekli İyileştirme Döngüleri**: Gözlemlenebilirlik verileri yinelemeli geliştirme sürecinin temelidir. Ajanların gerçek dünyadaki performansını izleyerek ekipler iyileştirme alanlarını belirleyebilir, modelleri ince ayar için veri toplayabilir ve yapılan değişikliklerin etkisini doğrulayabilir. Bu, üretim görüşlerinin (çevrimiçi değerlendirmeden) çevrimdışı deneylere ve geliştirmelere bilgi sağlayan bir geri bildirim döngüsü oluşturur; sonuç olarak ajan performansı kademeli olarak iyileşir.

## İzlenecek Temel Metrikler

Ajan davranışını izlemek ve anlamak için çeşitli metrik ve sinyaller takip edilmelidir. Belirli metrikler ajanın amacına göre değişebilir, ancak bazıları evrensel olarak önemlidir.

Gözlemlenebilirlik araçlarının izlediği en yaygın metriklerden bazıları şunlardır:

**Gecikme:** Ajan ne kadar hızlı yanıt veriyor? Uzun bekleme süreleri kullanıcı deneyimini olumsuz etkiler. Ajan çalıştırmalarını izleyerek görevler ve bireysel adımlar için gecikmeyi ölçmelisiniz. Örneğin, tüm model çağrıları için 20 saniye alan bir ajan, daha hızlı bir model kullanılarak veya model çağrılarını paralel çalıştırarak hızlandırılabilir.

**Maliyetler:** Bir ajan çalıştırmasının maliyeti nedir? AI ajanları token başına faturalandırılan LLM çağrılarına veya harici API'lere dayanır. Sık araç kullanımı veya birden fazla prompt hızla maliyetleri artırabilir. Örneğin, bir ajan marjinal kalite iyileştirmesi için bir LLM'yi beş kez çağırıyorsa, maliyetin haklı olup olmadığını veya çağrı sayısını azaltıp daha ucuz bir model kullanıp kullanamayacağınızı değerlendirmeniz gerekir. Gerçek zamanlı izleme ayrıca beklenmedik artışları tespit etmeye yardımcı olabilir (örn. aşırı API döngülerine neden olan hatalar).

**İstek Hataları:** Ajan kaç istekte başarısız oldu? Bu, API hatalarını veya başarısız araç çağrılarını içerebilir. Üretimde ajanın bunlara karşı daha dayanıklı olması için geri dönüşler veya yeniden denemeler ayarlayabilirsiniz. Örn. LLM sağlayıcısı A kapalıysa, yedek olarak LLM sağlayıcısı B'ye geçersiniz.

**Kullanıcı Geri Bildirimi:** Doğrudan kullanıcı değerlendirmelerini uygulamak değerli içgörüler sağlar. Bu, açık değerlendirmeleri içerebilir (beğeni/beğenmeme, 1-5 yıldız gibi) veya metinsel yorumlar. Tutarlı olumsuz geri bildirimler, ajanın beklendiği gibi çalışmadığına işaret eder.

**Dolaylı Kullanıcı Geri Bildirimi:** Kullanıcı davranışları, açık değerlendirme olmasa bile dolaylı geri bildirim sağlar. Bu, anında soruyu yeniden ifade etme, tekrar eden sorgular veya bir yeniden dene düğmesine tıklama gibi davranışları içerebilir. Örn. kullanıcıların aynı soruyu tekrar tekrar sorduğunu görüyorsanız, bu ajanının beklendiği gibi çalışmadığının bir işaretidir.

**Doğruluk:** Ajan ne sıklıkla doğru veya istenen çıktılar üretiyor? Doğruluk tanımları değişkenlik gösterir (örn. problem çözme doğruluğu, bilgi alma doğruluğu, kullanıcı memnuniyeti). İlk adım, ajanın başarı kriterinin ne olduğunu tanımlamaktır. Doğruluğu otomatik kontroller, değerlendirme puanları veya görev tamamlama etiketleriyle izleyebilirsiniz. Örneğin, izleri "başarılı" veya "başarısız" olarak işaretlemek.

**Otomatik Değerlendirme Metrikleri:** Otomatik eval'ler de kurabilirsiniz. Örneğin, bir LLM'yi ajanın çıktısını yardımcı olup olmadığı, doğru olup olmadığı gibi ölçmek için puanlama amacıyla kullanabilirsiniz. Ajana ilişkin farklı yönleri puanlamanıza yardımcı olan birkaç açık kaynak kütüphane de vardır. Örn. RAG ajanları için [RAGAS](https://docs.ragas.io/) veya zararlı dil ya da prompt enjeksiyonunu tespit etmek için [LLM Guard](https://llm-guard.com/).

Uygulamada, bu metriklerin bir kombinasyonu AI ajanının sağlığını en iyi şekilde kapsar. Bu bölümün [örnek defterinde](./code_samples/10-expense_claim-demo.ipynb) bu metriklerin gerçek örneklerde nasıl göründüğünü göstereceğiz ancak önce tipik bir değerlendirme iş akışının nasıl göründüğünü öğreneceğiz.

## Ajanınızı Araçlandırın

İzleme verilerini toplamak için kodunuzu enstrümante etmeniz gerekir. Amaç, gözlemlenebilirlik platformu tarafından yakalanabilecek, işlenebilecek ve görselleştirilebilecek izler ve metrikler yayacak şekilde ajan kodunu araçlandırmaktır.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) LLM gözlemlenebilirliği için endüstri standardı olarak öne çıkmıştır. Telemetri verisi üretmek, toplamak ve dışa aktarmak için bir dizi API, SDK ve araç sağlar. 

Mevcut ajan çerçevelerini saran ve OpenTelemetry span'larını bir gözlemlenebilirlik aracına kolayca aktarmayı sağlayan birçok enstrümantasyon kütüphanesi vardır. Microsoft Agent Framework, OpenTelemetry ile yerel olarak entegre olur. Aşağıda bir MAF ajanını araçlandırmaya ilişkin bir örnek bulunmaktadır:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Ajanın yürütülmesi otomatik olarak izlenir
    pass
```

Bu bölümdeki [örnek defter](./code_samples/10-expense_claim-demo.ipynb), MAF ajanınızı nasıl enstrümante edeceğinizi gösterecektir.

**Elle Span Oluşturma:** Enstrümantasyon kütüphaneleri iyi bir temel sağlar, ancak daha ayrıntılı veya özel bilgiye ihtiyaç duyulan durumlar sıkça ortaya çıkar. Özel uygulama mantığı eklemek için elle span'lar oluşturabilirsiniz. Daha da önemlisi, otomatik veya elle oluşturulmuş span'ları özel özniteliklerle (etiketler veya meta veriler olarak da bilinir) zenginleştirebilirsiniz. Bu öznitelikler işe özgü verileri, ara hesaplamaları veya hata ayıklama ya da analiz için yararlı olabilecek herhangi bir bağlamı içerebilir; örneğin `user_id`, `session_id` veya `model_version`.

Span ve izleri elle oluşturma örneği için [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) ile:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ajan Değerlendirmesi

Gözlemlenebilirlik bize metrikler sağlar, ancak değerlendirme bu verileri (ve testleri) analiz ederek bir AI ajanın ne kadar iyi performans gösterdiğini ve nasıl geliştirilebileceğini belirleme sürecidir. Başka bir deyişle, bu izler ve metrikler elinizde olduğunda, ajanın yargılanması ve kararlar alınması için bunları nasıl kullanırsınız?

Düzenli değerlendirme önemlidir çünkü AI ajanları genellikle deterministik değildir ve güncellemeler veya model davranışındaki kaymalarla evrilebilir — değerlendirme olmadan "akıllı ajanın" gerçekten işini iyi yapıp yapmadığını veya gerileme yaşayıp yaşamadığını bilemezsiniz.

AI ajanları için iki değerlendirme kategorisi vardır: **çevrimiçi değerlendirme** ve **çevrimdışı değerlendirme**. Her ikisi de değerlidir ve birbirini tamamlar. Genellikle herhangi bir ajan dağıtımından önce asgari gerekli adım olduğu için çevrimdışı değerlendirme ile başlarız.

### Çevrimdışı Değerlendirme

![Langfuse'ta veri kümesi öğeleri](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Bu, ajanı kontrollü bir ortamda, genellikle canlı kullanıcı sorguları yerine test veri kümeleri kullanarak değerlendirmeyi içerir. Beklenen çıktı veya doğru davranışın bilindiği küratörlü veri kümelerini kullanırsınız ve ardından ajanınızı bunlar üzerinde çalıştırırsınız.

Örneğin, bir matematik metin problemi ajanı oluşturduysanız, bilinen cevapları olan 100 problemden oluşan bir [test veri kümesine](https://huggingface.co/datasets/gsm8k) sahip olabilirsiniz. Çevrimdışı değerlendirme genellikle geliştirme sırasında (ve CI/CD boru hatlarının bir parçası olabilir) iyileştirmeleri kontrol etmek veya gerilemelere karşı koruma sağlamak için yapılır. Avantajı, zemindeki gerçek sonuçlara sahip olduğunuz için **tekrarlanabilir olması ve net doğruluk metrikleri alabilmenizdir**. Ayrıca kullanıcı sorgularını simüle ederek ajanın yanıtlarını ideal cevaplarla karşılaştırabilir veya yukarıda açıklandığı gibi otomatik metrikler kullanabilirsiniz.

Çevrimdışı değerlendirmenin temel zorluğu, test veri kümenizin kapsamlı ve alakalı kalmasını sağlamaktır — ajan sabit bir test kümesinde iyi performans gösterebilir ancak üretimde çok farklı sorgularla karşılaşabilir. Bu nedenle, test setlerini gerçek dünya senaryolarını yansıtan yeni uç durumlar ve örneklerle güncel tutmalısınız​. Küçük "smoke test" örnekleri ile daha geniş değerlendirme setlerinin bir karışımı faydalıdır: hızlı kontroller için küçük setler ve daha geniş performans ölçümleri için büyük setler​.

### Çevrimiçi Değerlendirme 

![Gözlemlenebilirlik metrikleri genel bakışı](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Bu, ajanı canlı, gerçek dünya ortamında, yani üretimde gerçek kullanım sırasında değerlendirmeyi ifade eder. Çevrimiçi değerlendirme, ajan performansını gerçek kullanıcı etkileşimlerinde izlemeyi ve sonuçları sürekli olarak analiz etmeyi içerir.

Örneğin, canlı trafikte başarı oranlarını, kullanıcı memnuniyeti puanlarını veya diğer metrikleri izleyebilirsiniz. Çevrimiçi değerlendirmenin avantajı, **laboratuvar ortamında tahmin edemeyebileceğiniz durumları yakalaması**dır — ajanınızın etkinliği zaman içinde giriş desenleri değiştikçe model kaymasını gözlemleyebilir ve test verilerinizde olmayan beklenmedik sorguları ya da durumları tespit edebilirsiniz​. Bu, ajanın vahşi doğada nasıl davrandığına dair gerçek bir tablo sunar.

Çevrimiçi değerlendirme genellikle tartışıldığı gibi açık ve kapanışsız kullanıcı geri bildirimlerini toplama ve ayrıca gölge testleri veya A/B testleri yürütmeyi içerebilir (yeni bir ajan sürümü karşılaştırma amacıyla paralel olarak çalıştırılır). Zorluk, canlı etkileşimler için güvenilir etiketler veya puanlar elde etmenin zor olabilmesidir — kullanıcı geri bildirimlerine veya kullanıcıların sonucu tıklayıp tıklamadığı gibi sonraki adım metriklerine güvenebilirsiniz.

### İkisini Birleştirme

Çevrimiçi ve çevrimdışı değerlendirmeler birbirini dışlamaz; birbirlerini tamamlarlar. Çevrimiçi izlemeden elde edilen içgörüler (örn. ajanın kötü performans gösterdiği yeni kullanıcı sorgusu türleri) çevrimdışı test veri kümelerini artırmak ve iyileştirmek için kullanılabilir. Tersine, çevrimdışı testlerde iyi performans gösteren ajanlar daha güvenle dağıtılabilir ve çevrimiçi olarak izlenebilir.

Aslında birçok ekip bir döngü benimser:

_değerlendir çevrimdışı -> dağıt -> çevrimiçi izle -> yeni hata vakalarını topla -> çevrimdışı veri kümesine ekle -> ajanı iyileştir -> tekrarla_.

## Yaygın Sorunlar

AI ajanlarını üretime dağıtırken çeşitli zorluklarla karşılaşabilirsiniz. İşte bazı yaygın sorunlar ve olası çözümleri:

| **Sorun**    | **Olası Çözüm**   |
| ------------- | ------------------ |
| AI Ajanı görevleri tutarlı bir şekilde gerçekleştirmiyor | - AI Ajanına verilen prompt'u iyileştirin; hedefleri net bir şekilde belirtin.<br>- Görevleri alt görevlere bölmenin ve bunları birden çok ajan tarafından ele almanın yardımcı olup olmayacağını belirleyin. |
| AI Ajanı sürekli döngülere giriyor  | - Ajanın işlemi ne zaman durduracağını bilmesi için net sonlandırma şartları ve koşulları sağlayın.<br>- Muhakeme ve planlama gerektiren karmaşık görevler için muhakeme görevlerinde uzmanlaşmış daha büyük bir model kullanın. |
| AI Ajanının araç çağrıları iyi performans göstermiyor   | - Aracın çıktısını ajan sisteminin dışında test edin ve doğrulayın.<br>- Tanımlanan parametreleri, promptları ve araç isimlendirmesini iyileştirin.  |
| Çok Ajanlı sistem tutarlı performans göstermiyor | - Her ajana verilen promptları daha spesifik ve birbirinden ayırt edici olacak şekilde geliştirin.<br>- Hangi ajanın doğru olduğuna karar vermek için "yönlendirme" veya kontrolör ajanı kullanarak hiyerarşik bir sistem kurun. |

Bu sorunların birçoğu, gözlemlenebilirlik devredeyken daha etkili bir şekilde tespit edilebilir. Daha önce tartıştığımız izler ve metrikler, ajan iş akışında problemin tam olarak nerede olduğunu belirlemeye yardımcı olarak hata ayıklamayı ve optimizasyonu çok daha verimli hale getirir.

## Maliyetleri Yönetme
Here are some strategies to manage the costs of deploying AI agents to production:

**Daha Küçük Modellerin Kullanımı:** Küçük Dil Modelleri (SLMs) belirli ajan tabanlı kullanım durumlarında iyi performans gösterebilir ve maliyetleri önemli ölçüde azaltır. Daha önce bahsedildiği gibi, performansı belirlemek ve daha büyük modellerle karşılaştırmak için bir değerlendirme sistemi kurmak, bir SLM'in kullanım durumunuzda ne kadar iyi performans göstereceğini anlamanın en iyi yoludur. Niyet sınıflandırması veya parametre çıkarımı gibi daha basit görevler için SLM'leri kullanmayı, daha karmaşık muhakeme gerektiren görevler içinse daha büyük modelleri ayırmayı düşünün.

**Yönlendirici Model Kullanımı:** Benzer bir strateji, çeşitli model ve boyutlar kullanmaktır. İstekleri karmaşıklığa göre en uygun modellere yönlendirmek için bir LLM/SLM veya sunucusuz fonksiyon kullanabilirsiniz. Bu, doğru görevlerde performansı sağlarken maliyetleri azaltmaya da yardımcı olacaktır. Örneğin, basit sorguları daha küçük, daha hızlı modellere yönlendirin ve yalnızca karmaşık akıl yürütme görevleri için pahalı büyük modelleri kullanın.

**Yanıtları Önbellekleme:** Yaygın istekleri ve görevleri tespit etmek ve yanıtları ajan tabanlı sisteminizden geçmeden önce sağlamak, benzer isteklerin hacmini azaltmanın iyi bir yoludur. Bir isteğin önbelleğe alınmış isteklere ne kadar benzediğini daha temel AI modelleri kullanarak belirleyen bir akış bile uygulayabilirsiniz. Bu strateji, sık sorulan sorular veya yaygın iş akışları için maliyetleri önemli ölçüde azaltabilir.

## Bunun pratikte nasıl çalıştığını görelim

In the [bu bölümün örnek not defteri](./code_samples/10-expense_claim-demo.ipynb), we’ll see examples of how we can use observability tools to monitor and evaluate our agent.


### Üretimdeki AI Ajanları hakkında daha fazla sorunuz mu var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanlarınızla ilgili sorularınıza yanıt bulmak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) sunucusuna katılın.

## Önceki Ders

[Metabiliş Tasarım Deseni](../09-metacognition/README.md)

## Sonraki Ders

[Ajan Tabanlı Protokoller](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Feragatname:
Bu belge, yapay zeka çeviri hizmeti Co-op Translator (https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki hâliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->