# Yeni Başlayanlar İçin Yapay Zeka Ajanları - Çalışma Rehberi

Bu rehberi, kurs boyunca ilerlerken pratik bir yoldaş olarak kullanın. Bu,
derslerin yerini alması amaçlanmamıştır. Nereden başlayacağınıza, her dersle
ne aramanız gerektiğine ve fikirleri küçük bir çalışan ajan demosunda nasıl birleştireceğinize
karar vermeniz için yardımcı olur.

Eğer buraya ilk kez geliyorsanız, basit başlayın:

1. [Kurs Kurulumu](./00-course-setup/README.md)'nu okuyun.
2. Ders 01-06'yı sırayla tamamlayın.
3. Öğrenirken aklınızda küçük bir demo fikri tutun.
4. Her dersten sonra sorun: "Ajanım şimdi önceden yapamadığı neyi yapabiliyor?"


## Aklınızda Tutmanız Gereken Basit Bir Demo

Ajanları öğrenmenin iyi bir yolu, kurs boyunca tek bir demo fikrini takip etmektir.

Örnek demo: **bir kurs yardımcısı ajan**.

Kullanıcı sorar:

> "Ajanların araçları nasıl kullandığını öğrenmek istiyorum. Doğru dersleri bul, önce
> ne okumam gerektiğini özetle ve bana kısa bir uygulama görevi ver."

Normal bir sohbet botu bildiğiyle cevap verebilir. Bir ajan ise daha fazlasını yapabilir:

1. **Doğru dersleri bulmak için kurs dosyalarını oku veya ara.**
2. **Araçları kullanarak** ders bağlantılarını, örnekleri veya destekleyici materyali al.
3. **Uzun bir cevap vermek yerine** kısa bir öğrenme yolu planla.
4. **Mevcut sohbetin bağlamını kullan** ve öğrenenin hedefinde odaklan.
5. Uygulama belleği destekliyorsa, **yararlı tercihleri hatırla.**
6. Kullanıcının neler olduğunu anlaması için **izleri, alıntıları veya günlükleri göster.**
7. Riskli eylemlerden veya hassas verilerden önce **koruyucu önlemler uygula.**


eklerdi?


## Hedeflediğiniz Şey

Kursun sonunda, şu parçalardan oluşan ajan sistemlerini açıklayabilmeli ve inşa
edebilmelisiniz:

| Parça | Günlük dilde anlamı | Demoda |
|------|------------------------|-------------|
| Model | Kullanıcının isteğini yorumlayan akıl yürütme motoru | Öğrenenin araç kullanımıyla ilgili dersler istediğini anlar |
| Araçlar | Ajanın kullanabileceği fonksiyonlar, API’ler, dosyalar, tarayıcılar veya servisler | Depoyu arar veya ders içeriğini getirir |
| Bilgi | Cevabı dayandırmak için kullanılan belgeler veya veriler | Kurs README dosyaları ve ders materyali |
| Bağlam | Sonraki model çağrısına dahil edilen bilgi | Kullanıcının hedefi ve araç sonuçları |
| Bellek | Sonraki kullanımlar için saklanan bilgi | Öğrenen rahat olması için Python örneklerini tercih eder |
| Planlama | Daha büyük hedefi küçük adımlara bölme | Dersleri bul, özetle, pratik öner |
| Orkestrasyon | İş yükünü araçlar, adımlar veya ajanlar arasında yönlendirme | Bir planlayıcı önce arama aracını, sonra özetleyiciyi çağırır |
| Güven | Güvenlik, emniyet, değerlendirme ve gözlemlenebilirlik | Araç çağrılarını kaydeder ve yüksek riskli işlemler öncesi sorar |

## Modeller ve Sağlayıcılar

Kurs kod örnekleri, **Microsoft Agent Framework (MAF)** kullanır ve hedef olarak

multimodal giriş ve durumlu sohbetleri tek bir API yüzeyinde birleştiren önerilen API.

OpenAI (`OpenAIChatClient`) ile yapılır.

Dersler boyunca birkaç sağlayıcı seçeneğiniz vardır:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — derslerde kullanılan ana yol.

- **Foundry Local** — modelleri tamamen cihazda, OpenAI uyumlu API ile çalıştırır (bulut ve

- **MiniMax** — büyük bağlamlı modellerle OpenAI uyumlu alternatif sağlayıcı.


Responses API’yi desteklemez. Örnekler Azure OpenAI / Microsoft Foundry ile güncellendi.

## Öğrenme Yolunuzu Seçin

Kursun tamamını sırasıyla alabilir veya yapmak istediğinize göre bir yol seçebilirsiniz.

| Hedefiniz... | Şuradan başla | Sonra çalış |
|-----------------------|------------|------------|
| Ajanların ne olduğunu anlamak | 01, 02, 03 | 04, 05, 06 |
| Araç kullanan ajan inşa etmek | 04 | 05, 07, 14 |
| RAG tabanlı ajan yapmak | 05 | 04, 06, 12 |

| Çok ajanlı sistemleri anlamak | 08 | 07, 09, 11 |
| Ajanları üretime hazırlamak | 06, 10 | 12, 13, 16, 18 |

| Yerel / çevrimdışı ajanlar inşa etmek | 17 | 04, 05, 11 |


İpucu: Ajanlarda yeniyseniz, Ders 01-06'yı atlamayın. Bu dersler geri kalan
için gerekli kelime dağarcığını sağlar.

## Ders Ders Rehberi

| Ders | Öğrenecekleriniz | Dersten sonra deneyin |
|--------|----------------|---------------------------|
| [01 - AI Ajanlarına Giriş](./01-intro-to-ai-agents/README.md) | Bir ajanı basit bir sohbet botundan ayıran özellikler. | Demo fikirinizi bir ajan olarak açıklayın, sadece sohbet uygulaması olarak değil. |
| [02 - Ajanik Çerçeveler](./02-explore-agentic-frameworks/README.md) | Çerçevelerin modeller, araçlar, durum ve iş akışlarına nasıl yardımcı olduğu. | Demodaki hangi parçaların bir çerçeve tarafından yönetileceğini belirleyin. |
| [03 - Ajanik Tasarım Desenleri](./03-agentic-design-patterns/README.md) | Ajan davranışını tasarlamak için yaygın desenler. | Kodu yazmadan önce kullanıcı yolculuğunu taslak olarak çıkarın. |
| [04 - Araç Kullanımı](./04-tool-use/README.md) | Ajanların veri almak veya eylem yapmak için araçları nasıl çağırdığı. | Demo ajanınızın ihtiyacı olacak bir aracı tanımlayın. |
| [05 - Ajanik RAG](./05-agentic-rag/README.md) | Geri çağırmanın ajan cevaplarını doküman veya veri temelli yapması. | Demoda hangi bilgi kaynağının aranacağını belirleyin. |
| [06 - Güvenilir Ajanlar](./06-building-trustworthy-agents/README.md) | Koruyucu önlemler, denetim ve daha güvenli davranış ekleme. | Ajanın kullanıcıya önce sorması gereken bir kural ekleyin. |
| [07 - Planlama Tasarımı](./07-planning-design/README.md) | Ajanların büyük hedefleri küçük adımlara bölmesi. | Demo isteğiniz için üç adımlı plan yazın. |
| [08 - Çoklu Ajan Tasarımı](./08-multi-agent/README.md) | Uzman ajanlar arasında iş bölümü ne zaman yapılır. | Demoda bir veya birden fazla ajan gerekip gerekmediğine karar verin. |
| [09 - Metakognisyon](./09-metacognition/README.md) | Ajanların kendi çıktısını gözden geçirip iyileştirmesi. | Ajan cevap vermeden önce son bir kendini kontrol ekleyin. |
| [10 - Üretimde AI Ajanları](./10-ai-agents-production/README.md) | Bir ajanın demo aşamasından üretim aşamasına geçmesindeki değişiklikler. | İzleyeceğiniz şeyleri listeleyin: kalite, maliyet, gecikme, hatalar. |
| [11 - Ajanik Protokoller](./11-agentic-protocols/README.md) | Protokollerin ajanları araçlar ve diğer ajanlara bağlaması. | Entegrasyonu basitleştirecek standart protokolü belirleyin. |
| [12 - Bağlam Mühendisliği](./12-context-engineering/README.md) | Bağlamın seçilmesi, kesilmesi, izole edilmesi ve yönetilmesi. | İstek içine ne konmalı ve ne dışarda bırakılmalı karar verin. |

| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Ajanlar ve iş akışları için çerçeveye özgü yapı taşları, Microsoft Foundry'de LangChain/LangGraph ajanlarının barındırılması. | Demo adımlarınızı çerçeve kavramlarına eşleyin. |

| [16 - Ölçeklenebilir Ajanların Dağıtımı](./16-deploying-scalable-agents/README.md) | Bir ajanın prototipten ölçeklenebilir, izlenebilir üretim dağıtımına Microsoft Foundry üzerinde geçişi (barındırılan ajanlar, model yönlendirme, önbellekleme, değerlendirme kapıları, duman testleri). | Demo için hala gereken üretim kaygılarını listeleyin: barındırma, yönlendirme, maliyet, değerlendirme. |
| [17 - Yerel AI Ajanları Oluşturma](./17-creating-local-ai-agents/README.md) | Foundry Local ve Qwen kullanarak tamamen makinanızda çalışan yerel ajanlar inşa etmek (yerel araçlar, yerel RAG, yerel MCP). | Demodaki hangi kısımların gizli kalması ve yerelde çalışması gerektiğine karar verin. |
| [18 - AI Ajanlarını Güvence Altına Alma](./18-securing-ai-agents/README.md) | Ajan eylemlerini daha denetlenebilir ve değişiklik tespitine açık yapmak. | Demoda hangi eylemlerin kaydedilmesi veya makbuzlandırılması gerektiğine karar verin. |

## Duman Testleri ile Dağıtılan Ajanları Doğrulama

Bir ajan dağıttığınızda (Ders 16), **duman testi** dağıtımın gerçekten cevap verip
vermediğini kontrol etmek için en ucuz ilk kontroldür. Bu depo, Ders 01, 04,

hazır kataloglar sağlar ve bunlar

Eylemine bağlıdır. Dersi dağıttıktan sonra **Actions** sekmesinden çalıştırın.

10 ve 16) size ajanın *ne kadar iyi* olduğunu söyler.

## Yeni Başlayanlara Yönelik Önemli Fikirler

### Araçlar

Bir araç, ajanın modeli aşan işler için çağırabileceği bir şeydir. İyi bir araç açık
bir ada, sınırlı bir işe, yazılı girişlere, öngörülebilir çıktıya ve güvenli bir hataya sahip olmalıdır.




- `read_lesson(path)`
- `create_practice_task(topic)`



RAG ajanın tahmin etmek yerine kaynak materyalden cevap vermesini sağlar. Bu kursta,




### Planlama

Planlama, istek birden fazla adımdan oluşuyorsa işe yarar. Planlar kısa ve geliştirici


Demo için plan şöyle olabilir:


2. En alakalı dersleri özetle.


### Bağlam


yol açabilir. Çok fazla bağlam ise ajanı yavaşlatabilir, maliyeti artırabilir veya karıştırabilir.





Bellek, daha sonra kullanılmak üzere saklanan bilgidir. Her şeyi saklamayın. Bilgiyi


Örneğin, "öğrenenin Python örneklerini tercih ettiği" bilgisi yararlı olabilir.








Üretimdeki ajanlar için model çağrıları, araç çağrıları, alınan bağlam, gecikme, maliyet,




Güvenilir ajanlar sadece faydalı bir istemden fazlasını gerektirir. En az ayrıcalıklı
araçlar kullanın, yüksek etkili işlemler için insan onayı alın, gerekli yerlerde veri sansürleyin






1. **Dersi bir cümlede özetleyin.**
2. **Yeni ajan yeteneğini adlandırın.** Örneğin: araç kullanımı, geri çağırma,
   planlama, bellek, gözlemlenebilirlik veya güvenlik.
3. **Bunu kurs yardımcısı demoya ekleyin.** Demoda şimdi ne değişti?
4. **Riskleri bulun.** Bu yetenek yanlış kullanılırsa ne olabilir?






1. Bir ajan, normal bir sohbet botunun kendi başına yapamadığını ne yapabilir?
2. Ajanınızın önce hangi araca ihtiyacı olur ve neden?
3. Ajan cevabını hangi bilgi kaynağı desteklemeli?
4. Sonraki model çağrısına hangi bağlam dahil edilmeli?
5. Ajan neyi hatırlamalı ve neyi saklamaktan kaçınmalı?
6. Ajan ne zaman insan onayı istemeli?


## Önerilen Bitirme Projesi

Kurs sonunda, öğrenen kişinin bu
depoda gezinmesine yardımcı olan küçük bir ajan geliştirin.

Minimum sürüm:

- Kullanıcıdan bir konu kabul et.
- En alakalı dersleri bul.
- Öncelikle ne okunacağını özetle.
- Bir uygulamalı pratik görev öner.
- Hangi ders dosyalarının veya bağlantıların kullanıldığını göster.

Geliştirilmiş sürüm:

- Öğrenenin tercih ettiği programlama dilini hatırla.
- Yanıt vermeden önce basit bir plan yap.
- Nihai yanıttan önce kendini kontrol etme adımı ekle.
- Araç çağrılarını ve alınan kaynakları kaydet.
- Tarayıcıyı veya UI otomasyon görevlerini açmadan önce onay iste.

Bu, araçları, RAG'ı, planlamayı,
bağlamı, belleği, gözlemlenebilirliği ve güveni tek projede küçük ama gerçekçi bir şekilde pratiğe dökmeni sağlar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->