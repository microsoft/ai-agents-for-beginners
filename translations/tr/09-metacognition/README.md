<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T13:07:00+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "tr"
}
-->
[![Çoklu Ajan Tasarımı](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.tr.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_
# AI Ajanlarında Metakognisyon

## Giriş

AI ajanlarında metakognisyon dersine hoş geldiniz! Bu bölüm, AI ajanlarının kendi düşünme süreçlerini nasıl değerlendirebileceğini merak eden yeni başlayanlar için tasarlanmıştır. Dersin sonunda, temel kavramları anlayacak ve metakognisyonu AI ajan tasarımında uygulamak için pratik örneklerle donanmış olacaksınız.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra:

1. Ajan tanımlarındaki akıl yürütme döngülerinin etkilerini anlayabileceksiniz.
2. Kendini düzeltebilen ajanlara yardımcı olmak için planlama ve değerlendirme tekniklerini kullanabileceksiniz.
3. Görevleri yerine getirmek için kodu manipüle edebilen kendi ajanlarınızı oluşturabileceksiniz.

## Metakognisyona Giriş

Metakognisyon, kişinin kendi düşünme süreçleri üzerine düşünmesini içeren üst düzey bilişsel süreçlere atıfta bulunur. AI ajanları için bu, kendi eylemlerini öz farkındalık ve geçmiş deneyimlere dayanarak değerlendirme ve ayarlama yeteneği anlamına gelir. "Düşünme üzerine düşünme" olarak da adlandırılan metakognisyon, ajan tabanlı AI sistemlerinin geliştirilmesinde önemli bir kavramdır. AI sistemlerinin kendi iç süreçlerinin farkında olması, davranışlarını izleyebilmesi, düzenleyebilmesi ve buna göre uyarlayabilmesi anlamına gelir. Tıpkı bizim bir ortamı analiz ederken veya bir problemi çözerken yaptığımız gibi. Bu öz farkındalık, AI sistemlerinin daha iyi kararlar almasına, hataları tanımlamasına ve zamanla performanslarını iyileştirmesine yardımcı olabilir. Bu durum, Turing testi ve AI'nın dünyayı ele geçirip geçiremeyeceği tartışmasıyla da bağlantılıdır.

Ajan tabanlı AI sistemleri bağlamında metakognisyon, şu gibi zorlukların üstesinden gelmeye yardımcı olabilir:
- Şeffaflık: AI sistemlerinin akıl yürütme ve kararlarını açıklayabilmesini sağlama.
- Akıl Yürütme: AI sistemlerinin bilgiyi sentezleme ve sağlam kararlar alma yeteneğini artırma.
- Uyum Sağlama: AI sistemlerinin yeni ortamlara ve değişen koşullara uyum sağlamasına olanak tanıma.
- Algı: AI sistemlerinin çevrelerinden gelen verileri tanıma ve yorumlama doğruluğunu artırma.

### Metakognisyon Nedir?

Metakognisyon, "düşünme üzerine düşünme" olarak adlandırılan, kişinin bilişsel süreçlerinin öz farkındalığını ve öz düzenlemesini içeren üst düzey bir bilişsel süreçtir. AI alanında metakognisyon, ajanlara stratejilerini ve eylemlerini değerlendirme ve uyarlama yeteneği kazandırarak problem çözme ve karar verme yeteneklerini geliştirir. Metakognisyonu anlayarak, yalnızca daha zeki değil, aynı zamanda daha uyumlu ve verimli AI ajanları tasarlayabilirsiniz. Gerçek bir metakognisyonda, AI'nın kendi akıl yürütmesi hakkında açıkça akıl yürüttüğünü görebilirsiniz.

Örnek: “Daha ucuz uçuşları önceliklendirdim çünkü… Direkt uçuşları kaçırıyor olabilirim, bu yüzden tekrar kontrol edeyim.”
Seçtiği rotayı nasıl veya neden seçtiğini takip etme.
- Geçen sefer kullanıcı tercihlerine fazla güvendiği için hata yaptığını fark edip, yalnızca nihai öneriyi değil, karar verme stratejisini de değiştirme.
- “Kullanıcı ‘çok kalabalık’ dediğinde, yalnızca belirli cazibe merkezlerini kaldırmakla kalmayıp, ‘en popüler’ sıralaması yaparken yöntemimin hatalı olduğunu fark etmeliyim” gibi kalıpları teşhis etme.

### AI Ajanlarında Metakognisyonun Önemi

Metakognisyon, AI ajan tasarımında birkaç nedenden dolayı kritik bir rol oynar:

![Metakognisyonun Önemi](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.tr.png)

- Öz Değerlendirme: Ajanlar kendi performanslarını değerlendirebilir ve geliştirilmesi gereken alanları belirleyebilir.
- Uyum Sağlama: Ajanlar, geçmiş deneyimlere ve değişen ortamlara dayalı olarak stratejilerini değiştirebilir.
- Hata Düzeltme: Ajanlar, hataları bağımsız olarak tespit edip düzeltebilir, bu da daha doğru sonuçlara yol açar.
- Kaynak Yönetimi: Ajanlar, eylemlerini planlayarak ve değerlendirerek zaman ve hesaplama gücü gibi kaynakları optimize edebilir.

## Bir AI Ajanının Bileşenleri

Metakognitif süreçlere dalmadan önce, bir AI ajanının temel bileşenlerini anlamak önemlidir. Bir AI ajanı tipik olarak şu bileşenlerden oluşur:

- Persona: Ajanın kullanıcılarla nasıl etkileşim kurduğunu tanımlayan kişilik ve özellikler.
- Araçlar: Ajanın gerçekleştirebileceği yetenekler ve işlevler.
- Beceriler: Ajanın sahip olduğu bilgi ve uzmanlık.

Bu bileşenler, belirli görevleri yerine getirebilen bir "uzmanlık birimi" oluşturmak için birlikte çalışır.

**Örnek**:
Bir seyahat acentesini düşünün; bu ajan yalnızca tatilinizi planlamakla kalmaz, aynı zamanda gerçek zamanlı verilere ve önceki müşteri deneyimlerine dayalı olarak rotasını ayarlar.

### Örnek: Bir Seyahat Acentesi Hizmetinde Metakognisyon

Bir AI destekli seyahat acentesi hizmeti tasarladığınızı hayal edin. Bu ajan, "Seyahat Acentesi," kullanıcıların tatillerini planlamalarına yardımcı olur. Metakognisyonu dahil etmek için Seyahat Acentesi, öz farkındalık ve geçmiş deneyimlere dayanarak eylemlerini değerlendirmeli ve ayarlamalıdır. İşte metakognisyonun nasıl bir rol oynayabileceği:

#### Mevcut Görev

Mevcut görev, bir kullanıcının Paris'e bir gezi planlamasına yardımcı olmaktır.

#### Görevi Tamamlama Adımları

1. **Kullanıcı Tercihlerini Topla**: Kullanıcıya seyahat tarihleri, bütçe, ilgi alanları (ör. müzeler, mutfak, alışveriş) ve özel gereksinimler hakkında sorular sor.
2. **Bilgi Topla**: Kullanıcının tercihleriyle eşleşen uçuş seçeneklerini, konaklama yerlerini, cazibe merkezlerini ve restoranları ara.
3. **Öneriler Oluştur**: Uçuş detayları, otel rezervasyonları ve önerilen aktivitelerle kişiselleştirilmiş bir gezi planı sun.
4. **Geri Bildirime Göre Ayarla**: Kullanıcıdan öneriler hakkında geri bildirim iste ve gerekli ayarlamaları yap.

#### Gerekli Kaynaklar

- Uçuş ve otel rezervasyon veritabanlarına erişim.
- Paris'teki cazibe merkezleri ve restoranlar hakkında bilgi.
- Önceki etkileşimlerden kullanıcı geri bildirim verileri.

#### Deneyim ve Öz Değerlendirme

Seyahat Acentesi, performansını değerlendirmek ve geçmiş deneyimlerden öğrenmek için metakognisyon kullanır. Örneğin:

1. **Kullanıcı Geri Bildirimini Analiz Etme**: Seyahat Acentesi, hangi önerilerin beğenildiğini ve hangilerinin beğenilmediğini belirlemek için kullanıcı geri bildirimlerini gözden geçirir. Gelecekteki önerilerini buna göre ayarlar.
2. **Uyum Sağlama**: Eğer bir kullanıcı daha önce kalabalık yerlerden hoşlanmadığını belirtmişse, Seyahat Acentesi gelecekte yoğun turist noktalarını yoğun saatlerde önermemeye çalışır.
3. **Hata Düzeltme**: Seyahat Acentesi, geçmişte dolu bir oteli önerme gibi bir hata yaptıysa, önerilerde bulunmadan önce uygunluğu daha titizlikle kontrol etmeyi öğrenir.

#### Pratik Geliştirici Örneği

İşte Seyahat Acentesi'nin metakognisyonu dahil eden kodunun basitleştirilmiş bir örneği:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Metakognisyon Neden Önemlidir?

- **Öz Değerlendirme**: Ajanlar performanslarını analiz edebilir ve geliştirilmesi gereken alanları belirleyebilir.
- **Uyum Sağlama**: Ajanlar, geri bildirim ve değişen koşullara dayalı olarak stratejilerini değiştirebilir.
- **Hata Düzeltme**: Ajanlar, hataları bağımsız olarak tespit edip düzeltebilir.
- **Kaynak Yönetimi**: Ajanlar, zaman ve hesaplama gücü gibi kaynakları optimize edebilir.

Metakognisyonu dahil ederek, Seyahat Acentesi daha kişiselleştirilmiş ve doğru seyahat önerileri sunabilir, böylece genel kullanıcı deneyimini geliştirebilir.

---

## 2. Ajanlarda Planlama

Planlama, AI ajan davranışının kritik bir bileşenidir. Mevcut durumu, kaynakları ve olası engelleri göz önünde bulundurarak bir hedefe ulaşmak için gerekli adımları belirlemeyi içerir.

### Planlamanın Unsurları

- **Mevcut Görev**: Görevi net bir şekilde tanımlayın.
- **Görevi Tamamlama Adımları**: Görevi yönetilebilir adımlara ayırın.
- **Gerekli Kaynaklar**: Gerekli kaynakları belirleyin.
- **Deneyim**: Planlamayı bilgilendirmek için geçmiş deneyimleri kullanın.

**Örnek**:
Seyahat Acentesi'nin bir kullanıcının seyahatini etkili bir şekilde planlamasına yardımcı olmak için atması gereken adımlar şunlardır:

### Seyahat Acentesi için Adımlar

1. **Kullanıcı Tercihlerini Topla**
   - Kullanıcıdan seyahat tarihleri, bütçe, ilgi alanları ve özel gereksinimler hakkında bilgi iste.
   - Örnekler: "Ne zaman seyahat etmeyi planlıyorsunuz?" "Bütçe aralığınız nedir?" "Tatilde hangi aktivitelerden hoşlanırsınız?"

2. **Bilgi Topla**
   - Kullanıcı tercihlerini temel alarak ilgili seyahat seçeneklerini ara.
   - **Uçuşlar**: Kullanıcının bütçesi ve tercih edilen seyahat tarihleri içinde mevcut uçuşları ara.
   - **Konaklama**: Kullanıcının konum, fiyat ve olanak tercihlerini karşılayan otel veya kiralık mülkleri bul.
   - **Cazibe Merkezleri ve Restoranlar**: Kullanıcının ilgi alanlarına uygun popüler cazibe merkezlerini, aktiviteleri ve yemek seçeneklerini belirle.

3. **Öneriler Oluştur**
   - Toplanan bilgileri kişiselleştirilmiş bir gezi planına dönüştür.
   - Kullanıcının tercihlerini göz önünde bulundurarak uçuş seçenekleri, otel rezervasyonları ve önerilen aktiviteler gibi detayları sun.

4. **Gezi Planını Kullanıcıya Sun**
   - Önerilen gezi planını kullanıcıya incelemesi için paylaş.
   - Örnek: "İşte Paris geziniz için önerilen bir plan. Uçuş detaylarını, otel rezervasyonlarını ve önerilen aktiviteler ve restoranların bir listesini içeriyor. Düşüncelerinizi bana bildirin!"

5. **Geri Bildirim Topla**
   - Kullanıcıdan önerilen gezi planı hakkında geri bildirim iste.
   - Örnekler: "Uçuş seçeneklerini beğendiniz mi?" "Otel ihtiyaçlarınıza uygun mu?" "Eklemek veya çıkarmak istediğiniz aktiviteler var mı?"

6. **Geri Bildirime Göre Ayarla**
   - Kullanıcının geri bildirimine göre gezi planını değiştir.
   - Uçuş, konaklama ve aktivite önerilerini kullanıcının tercihlerine daha iyi uyacak şekilde değiştir.

7. **Son Onay**
   - Güncellenmiş gezi planını kullanıcıya son onay için sun.
   - Örnek: "Geri bildiriminize göre düzenlemeler yaptım. İşte güncellenmiş plan. Her şey size uygun görünüyor mu?"

8. **Rezervasyonları Yap ve Onayla**
   - Kullanıcı planı onayladıktan sonra uçuşları, konaklamaları ve önceden planlanmış aktiviteleri rezerve edin.
   - Onay detaylarını kullanıcıya gönderin.

9. **Sürekli Destek Sağla**
   - Kullanıcının seyahatten önce ve seyahat sırasında herhangi bir değişiklik veya ek talep için size ulaşabilmesini sağlayın.
   - Örnek: "Seyahatiniz sırasında herhangi bir yardıma ihtiyacınız olursa, bana her zaman ulaşabilirsiniz!"

### Örnek Etkileşim

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage within a booing request
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Düzeltici RAG Sistemi

Öncelikle RAG Aracı ile Önleyici Bağlam Yükleme arasındaki farkı anlamakla başlayalım.

![RAG ve Bağlam Yükleme](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.tr.png)

### Retrieval-Augmented Generation (RAG)

RAG, bir geri alma sistemi ile bir üretici modeli birleştirir. Bir sorgu yapıldığında, geri alma sistemi harici bir kaynaktan ilgili belgeleri veya verileri alır ve bu alınan bilgiler, üretici modele giriş olarak eklenir. Bu, modelin daha doğru ve bağlamsal olarak uygun yanıtlar üretmesine yardımcı olur.

Bir RAG sisteminde, ajan bir bilgi tabanından ilgili bilgileri alır ve bunları uygun yanıtlar veya eylemler oluşturmak için kullanır.

### Düzeltici RAG Yaklaşımı

Düzeltici RAG yaklaşımı, RAG tekniklerini kullanarak hataları düzeltmeye ve AI ajanlarının doğruluğunu artırmaya odaklanır. Bu, şunları içerir:

1. **İpucu Tekniği**: Ajanı ilgili bilgileri almaya yönlendiren belirli ipuçlarını kullanma.
2. **Araç**: Ajanın alınan bilginin alaka düzeyini değerlendirmesini ve doğru yanıtlar oluşturmasını sağlayan algoritmalar ve mekanizmalar uygulama.
3. **Değerlendirme**: Ajanın performansını sürekli olarak değerlendirme ve doğruluğunu ve verimliliğini artırmak için ayarlamalar yapma.

#### Örnek: Bir Arama Ajanında Düzeltici RAG

Bir kullanıcının sorgularını yanıtlamak için web'den bilgi alan bir arama ajanını düşünün. Düzeltici RAG yaklaşımı şunları içerebilir:

1. **İpucu Tekniği**: Kullanıcının girdisine dayalı olarak arama sorguları oluşturma.
2. **Araç**: Doğal dil işleme ve makine öğrenimi algoritmalarını kullanarak arama sonuçlarını sıralama ve filtreleme.
3. **Değerlendirme**: Kullanıcı geri bildirimlerini analiz ederek alınan bilgideki yanlışlıkları belirleme ve düzeltme.

### Seyahat Acentesinde Düzeltici RAG

Düzeltici RAG (Retrieval-Augmented Generation), AI'nın bilgi alıp üretme yeteneğini geliştirirken yanlışlıkları düzeltir. Seyahat Acentesi'nin Düzeltici RAG yaklaşımını kullanarak daha doğru ve ilgili seyahat önerileri sunmasını nasıl sağlayabileceğimize bakalım.

Bu şunları içerir:

- **İpucu Tekniği:** Ajanı ilgili bilgileri almaya yönlendiren belirli ipuçlarını kullanma.
- **Araç:** Ajanın alınan bilginin alaka düzeyini değerlendirmesini ve doğru yanıtlar oluşturmasını sağlayan algoritmalar ve mekanizmalar uygulama.
- **Değerlendirme:** Ajanın performansını sürekli olarak değerlendirerek doğruluğunu ve verimliliğini artırmak için ayarlamalar yapma.

#### Seyahat Acentesinde Düzeltici RAG Uygulama Adımları

1. **İlk Kullanıcı Etkileşimi**
   - Seyahat Acentesi, kullanıcıdan hedef, seyahat tarihleri, bütçe ve ilgi alanları gibi ilk tercihleri toplar.
   - Örnek:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Bilgi Alma**
   - Seyahat Acentesi, kullanıcı tercihleri temelinde uçuşlar, konaklamalar, cazibe merkezleri ve restoranlar hakkında bilgi alır.
   - Örnek:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **İlk Önerileri Oluşturma**
   - Seyahat Acentesi, alınan bilgileri kullanarak kişiselleştirilmiş bir gezi planı oluşturur.
   - Örnek:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Kullanıcı Geri Bildirimi Toplama**
   - Seyahat Acentesi, ilk öneriler hakkında kullanıcıdan geri bildirim ister.
   - Örnek:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Düzeltici RAG Süreci**
   - **İpucu Tekniği**: Seyahat Acentesi, kullanıcı geri bildirimine dayalı olarak yeni arama sorguları oluşturur.
     - Örnek:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Araç**: Seyahat Acentesi, yeni arama sonuçlarını sıralamak ve filtrelemek için algoritmalar kullanır, geri bildirime dayalı olarak alaka düzeyine vurgu yapar.
     - Örnek:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Değerlendirme**: Seyahat Acentesi, kullanıcı geri bildirimlerini analiz ederek önerilerinin alaka düzeyini ve doğruluğunu sürekli olarak değerlendirir ve gerekli ayarlamaları yapar.
     - Örnek:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Pratik Örnek

İşte Seyahat Acent
```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Önceden Bağlam Yükleme

Önceden bağlam yükleme, bir sorguyu işlemeye başlamadan önce modelin ilgili bağlam veya arka plan bilgisini yüklemesini içerir. Bu, modelin sürecin başından itibaren bu bilgilere erişebilmesini sağlar ve ek veri almaya gerek kalmadan daha bilinçli yanıtlar üretmesine yardımcı olur.

İşte bir seyahat acentesi uygulaması için Python'da önceden bağlam yüklemenin nasıl görünebileceğine dair basit bir örnek:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Açıklama

1. **Başlatma (`__init__` metodu)**: `TravelAgent` sınıfı, Paris, Tokyo, New York ve Sydney gibi popüler destinasyonlar hakkında bilgi içeren bir sözlüğü önceden yükler. Bu sözlük, her destinasyon için ülke, para birimi, dil ve başlıca cazibe merkezleri gibi ayrıntıları içerir.

2. **Bilgi Alma (`get_destination_info` metodu)**: Bir kullanıcı belirli bir destinasyon hakkında sorgu yaptığında, `get_destination_info` metodu önceden yüklenmiş bağlam sözlüğünden ilgili bilgileri alır.

Bağlamı önceden yükleyerek, seyahat acentesi uygulaması kullanıcı sorgularına gerçek zamanlı olarak harici bir kaynaktan bilgi almaya gerek kalmadan hızlı bir şekilde yanıt verebilir. Bu, uygulamayı daha verimli ve duyarlı hale getirir.

### İterasyondan Önce Bir Hedefle Planı Başlatma

Bir hedefle planı başlatmak, sürece başlamadan önce net bir hedef veya sonuç belirlemeyi içerir. Bu hedefi baştan tanımlayarak, model bunu iteratif süreç boyunca bir rehber olarak kullanabilir. Bu, her iterasyonun istenen sonuca daha yakın olmasını sağlar ve süreci daha verimli ve odaklı hale getirir.

İşte bir seyahat acentesi için bir hedefle seyahat planını başlatmanın ve ardından iterasyon yapmanın nasıl görünebileceğine dair bir örnek:

### Senaryo

Bir seyahat acentesi, bir müşteriye özel bir tatil planı oluşturmak istiyor. Amaç, müşterinin tercihlerine ve bütçesine göre memnuniyetini en üst düzeye çıkaran bir seyahat programı oluşturmaktır.

### Adımlar

1. Müşterinin tercihlerini ve bütçesini tanımlayın.
2. Bu tercihlere dayalı olarak başlangıç planını oluşturun.
3. Planı iyileştirmek için iterasyon yaparak müşterinin memnuniyetini optimize edin.

#### Python Kodu

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Example usage
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Kod Açıklaması

1. **Başlatma (`__init__` metodu)**: `TravelAgent` sınıfı, her biri ad, maliyet ve aktivite türü gibi özelliklere sahip potansiyel destinasyonların bir listesiyle başlatılır.

2. **Planı Başlatma (`bootstrap_plan` metodu)**: Bu metod, müşterinin tercihleri ve bütçesi temelinde başlangıç seyahat planını oluşturur. Destinasyon listesini iterasyonla tarar ve müşterinin tercihleriyle eşleşen ve bütçeye uyan destinasyonları plana ekler.

3. **Tercihleri Eşleştirme (`match_preferences` metodu)**: Bu metod, bir destinasyonun müşterinin tercihleriyle eşleşip eşleşmediğini kontrol eder.

4. **Planı İterasyonla Geliştirme (`iterate_plan` metodu)**: Bu metod, başlangıç planını iyileştirir ve müşterinin tercihleri ve bütçe kısıtlamalarını göz önünde bulundurarak her destinasyonu daha iyi bir eşleşmeyle değiştirmeye çalışır.

5. **Maliyet Hesaplama (`calculate_cost` metodu)**: Bu metod, mevcut planın toplam maliyetini ve potansiyel yeni bir destinasyonu hesaplar.

#### Örnek Kullanım

- **Başlangıç Planı**: Seyahat acentesi, müşterinin gezi yapma tercihlerine ve 2000 dolarlık bütçesine dayalı olarak bir başlangıç planı oluşturur.
- **Geliştirilmiş Plan**: Seyahat acentesi, planı iterasyonla geliştirerek müşterinin tercihlerini ve bütçesini optimize eder.

Bir hedefle planı başlatarak (örneğin, müşteri memnuniyetini en üst düzeye çıkarmak) ve planı iyileştirmek için iterasyon yaparak, seyahat acentesi müşteriye özel ve optimize edilmiş bir seyahat programı oluşturabilir. Bu yaklaşım, seyahat planının baştan itibaren müşterinin tercihleri ve bütçesiyle uyumlu olmasını sağlar ve her iterasyonla daha da iyileşir.

### LLM Kullanarak Yeniden Sıralama ve Puanlama

Büyük Dil Modelleri (LLM'ler), alınan belgelerin veya oluşturulan yanıtların alaka düzeyini ve kalitesini değerlendirerek yeniden sıralama ve puanlama için kullanılabilir. İşte nasıl çalıştığı:

**Alma:** İlk alma adımı, sorguya dayalı olarak bir dizi aday belge veya yanıt getirir.

**Yeniden Sıralama:** LLM, bu adayları değerlendirir ve alaka düzeyleri ve kalitelerine göre yeniden sıralar. Bu adım, en alakalı ve yüksek kaliteli bilgilerin önce sunulmasını sağlar.

**Puanlama:** LLM, her adaya alaka düzeylerini ve kalitelerini yansıtan puanlar atar. Bu, kullanıcı için en iyi yanıtın veya belgenin seçilmesine yardımcı olur.

LLM'leri yeniden sıralama ve puanlama için kullanarak, sistem daha doğru ve bağlamsal olarak alakalı bilgiler sağlayabilir ve genel kullanıcı deneyimini iyileştirebilir.

İşte bir seyahat acentesinin, kullanıcı tercihlerini temel alarak seyahat destinasyonlarını yeniden sıralamak ve puanlamak için bir Büyük Dil Modeli (LLM) kullanabileceği bir örnek:

#### Senaryo - Tercihlere Göre Seyahat

Bir seyahat acentesi, müşteriye en iyi seyahat destinasyonlarını önermek istiyor. LLM, en alakalı seçeneklerin sunulmasını sağlamak için destinasyonları yeniden sıralamak ve puanlamak için yardımcı olacak.

#### Adımlar:

1. Kullanıcı tercihlerini toplayın.
2. Potansiyel seyahat destinasyonlarının bir listesini alın.
3. Kullanıcı tercihlerini temel alarak destinasyonları yeniden sıralamak ve puanlamak için LLM'yi kullanın.

Azure OpenAI Hizmetlerini kullanarak önceki örneği nasıl güncelleyebileceğinize dair bir örnek:

#### Gereksinimler

1. Bir Azure aboneliğiniz olmalı.
2. Bir Azure OpenAI kaynağı oluşturun ve API anahtarınızı alın.

#### Örnek Python Kodu

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Example usage
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Kod Açıklaması - Tercih Kitapçısı

1. **Başlatma**: `TravelAgent` sınıfı, her biri ad ve açıklama gibi özelliklere sahip potansiyel seyahat destinasyonlarının bir listesiyle başlatılır.

2. **Öneriler Alma (`get_recommendations` metodu)**: Bu metod, kullanıcının tercihlerini temel alarak Azure OpenAI hizmeti için bir istem oluşturur ve Azure OpenAI API'sine bir HTTP POST isteği yapar.

3. **İstem Oluşturma (`generate_prompt` metodu)**: Bu metod, kullanıcının tercihlerini ve destinasyon listesini içeren bir istem oluşturur. İstem, modelin destinasyonları yeniden sıralamasını ve puanlamasını yönlendirir.

4. **API Çağrısı**: `requests` kütüphanesi, Azure OpenAI API uç noktasına bir HTTP POST isteği yapmak için kullanılır. Yanıt, yeniden sıralanmış ve puanlanmış destinasyonları içerir.

5. **Örnek Kullanım**: Seyahat acentesi, kullanıcı tercihlerini (örneğin, gezi ve çeşitli kültürlere ilgi) toplar ve Azure OpenAI hizmetini kullanarak yeniden sıralanmış ve puanlanmış seyahat önerileri alır.

`your_azure_openai_api_key` yerine gerçek Azure OpenAI API anahtarınızı ve `https://your-endpoint.com/...` yerine Azure OpenAI dağıtımınızın gerçek uç nokta URL'sini koymayı unutmayın.

LLM'yi yeniden sıralama ve puanlama için kullanarak, seyahat acentesi müşterilere daha kişiselleştirilmiş ve alakalı seyahat önerileri sunabilir ve genel deneyimlerini geliştirebilir.

### RAG: İstem Tekniği vs Araç

Bilgi Alma Destekli Üretim (RAG), hem bir istem tekniği hem de bir araç olarak kullanılabilir. İkisi arasındaki farkı anlamak, projelerinizde RAG'yi daha etkili bir şekilde kullanmanıza yardımcı olabilir.

#### RAG Bir İstem Tekniği Olarak

**Nedir?**

- Bir istem tekniği olarak RAG, büyük bir veri kümesinden veya veritabanından ilgili bilgilerin alınmasını yönlendirmek için belirli sorgular veya istemler oluşturmayı içerir. Bu bilgiler daha sonra yanıtlar veya eylemler oluşturmak için kullanılır.

**Nasıl Çalışır:**

1. **İstemleri Oluşturun**: Görev veya kullanıcının girdisine dayalı olarak iyi yapılandırılmış istemler veya sorgular oluşturun.
2. **Bilgi Alın**: İstemleri kullanarak önceden var olan bir bilgi tabanından veya veri kümesinden ilgili verileri arayın.
3. **Yanıt Oluşturun**: Alınan bilgileri üretici yapay zeka modelleriyle birleştirerek kapsamlı ve tutarlı bir yanıt oluşturun.

**Seyahat Acentesi Örneği**:

- Kullanıcı Girdisi: "Paris'teki müzeleri ziyaret etmek istiyorum."
- İstem: "Paris'teki en iyi müzeleri bulun."
- Alınan Bilgi: Louvre Müzesi, Musée d'Orsay gibi detaylar.
- Oluşturulan Yanıt: "İşte Paris'teki en iyi müzeler: Louvre Müzesi, Musée d'Orsay ve Centre Pompidou."

#### RAG Bir Araç Olarak

**Nedir?**

- Bir araç olarak RAG, bilgi alma ve üretim sürecini otomatikleştiren entegre bir sistemdir ve geliştiricilerin her sorgu için manuel olarak istem oluşturmasına gerek kalmadan karmaşık yapay zeka işlevlerini uygulamasını kolaylaştırır.

**Nasıl Çalışır:**

1. **Entegrasyon**: RAG'yi yapay zeka aracının mimarisine entegre ederek, bilgi alma ve üretim görevlerini otomatik olarak yönetmesini sağlayın.
2. **Otomasyon**: Araç, kullanıcı girdisinden nihai yanıtın oluşturulmasına kadar tüm süreci yönetir.
3. **Verimlilik**: Bilgi alma ve üretim sürecini kolaylaştırarak, daha hızlı ve daha doğru yanıtlar sağlar.

**Seyahat Acentesi Örneği**:

- Kullanıcı Girdisi: "Paris'teki müzeleri ziyaret etmek istiyorum."
- RAG Aracı: Otomatik olarak müzeler hakkında bilgi alır ve bir yanıt oluşturur.
- Oluşturulan Yanıt: "İşte Paris'teki en iyi müzeler: Louvre Müzesi, Musée d'Orsay ve Centre Pompidou."

### Karşılaştırma

| Özellik               | İstem Tekniği                                      | Araç                                                  |
|-----------------------|----------------------------------------------------|------------------------------------------------------|
| **Manuel vs Otomatik**| Her sorgu için manuel istem oluşturma.             | Bilgi alma ve üretim için otomatik süreç.            |
| **Kontrol**           | Bilgi alma süreci üzerinde daha fazla kontrol.     | Bilgi alma ve üretimi otomatikleştirir.              |
| **Esneklik**          | Belirli ihtiyaçlara göre özelleştirilmiş istemlere izin verir. | Büyük ölçekli uygulamalar için daha verimli.         |
| **Karmaşıklık**       | İstemlerin oluşturulması ve ayarlanmasını gerektirir. | Bir yapay zeka aracının mimarisine kolayca entegre edilir. |

### Pratik Örnekler

**İstem Tekniği Örneği:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Araç Örneği:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Alaka Düzeyini Değerlendirme

Alaka düzeyini değerlendirme, yapay zeka aracının performansının önemli bir yönüdür. Bu, aracın aldığı ve oluşturduğu bilgilerin kullanıcı için uygun, doğru ve faydalı olmasını sağlar. Yapay zeka araçlarında alaka düzeyini değerlendirme yöntemlerini, pratik örnekleri ve teknikleri inceleyelim.

#### Alaka Düzeyini Değerlendirmede Temel Kavramlar

1. **Bağlam Farkındalığı**:
   - Aracın, kullanıcının sorgusunun bağlamını anlaması ve ilgili bilgileri alması gerekir.
   - Örnek: Bir kullanıcı "Paris'teki en iyi restoranlar" diye sorarsa, araç kullanıcının tercihlerine (örneğin, mutfak türü ve bütçe) göre önerilerde bulunmalıdır.

2. **Doğruluk**:
   - Aracın sağladığı bilgilerin doğru ve güncel olması gerekir.
   - Örnek: Kapalı veya kötü yorumlar almış restoranlar yerine, açık ve iyi yorumlara sahip restoranları önermek.

3. **Kullanıcı Niyeti**:
   - Aracın, kullanıcının sorgusunun arkasındaki niyeti anlaması ve en alakalı bilgileri sağlaması gerekir.
   - Örnek: Bir kullanıcı "bütçe dostu oteller" diye sorarsa, araç uygun fiyatlı seçeneklere öncelik vermelidir.

4. **Geri Bildirim Döngüsü**:
   - Kullanıcı geri bildirimlerini sürekli olarak toplamak ve analiz etmek, aracın alaka düzeyi değerlendirme sürecini iyileştirmesine yardımcı olur.
   - Örnek: Önceki önerilerle ilgili kullanıcı derecelendirmelerini ve geri bildirimlerini dahil etmek.

#### Alaka Düzeyini Değerlendirme için Pratik Teknikler

1. **Alaka Puanlama**:
   - Kullanıcının sorgusu ve tercihleriyle ne kadar iyi eşleştiğine bağlı olarak her alınan öğeye bir alaka puanı atayın.
   - Örnek:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Filtreleme ve Sıralama**:
   - Alakasız öğeleri filtreleyin ve kalanları alaka puanlarına göre sıralayın.
   - Örnek:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Return top 10 relevant items
     ```

3. **Doğal Dil İşleme (NLP)**:
   - Kullanıcının sorgusunu anlamak ve ilgili bilgileri almak için NLP tekniklerini kullanın.
   - Örnek:

     ```python
     def process_query(query):
         # Use NLP to extract key information from the user's query
         processed_query = nlp(query)
         return processed_query
     ```

4. **Kullanıcı Geri Bildirimi Entegrasyonu**:
   - Sağlanan önerilerle ilgili kullanıcı geri bildirimlerini toplayın ve gelecekteki alaka değerlendirmelerini ayarlamak için kullanın.
   - Örnek:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Örnek: Seyahat Acentesinde Alaka Düzeyini Değerlendirme

İşte Seyahat Acentesi'nin seyahat önerilerinin alaka düzeyini nasıl değerlendirebileceğine dair pratik bir örnek:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Return top 10 relevant items

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Niyetle Arama

Niyetle arama, bir kullanıcının sorgusunun altında yatan amacı veya hedefini anlamayı ve en alakalı ve faydalı bilgileri almayı ve oluşturmayı içerir. Bu yaklaşım, yalnızca anahtar kelimeleri eşleştirmekten öteye geçer ve kullanıcının gerçek ihtiyaçlarını ve bağlamını kavramaya odaklanır.

#### Niyetle Aramada Temel Kavramlar

1. **Kullanıcı Niyetini Anlama**:
   - Kullanıcı niyeti üç ana kategoriye ayrılabilir: bilgilendirici, yönlendirici ve işlem odaklı.
     - **Bilgilendirici Niyet**: Kullanıcı bir konu hakkında bilgi arar (örneğin, "Paris'teki en iyi müzeler nelerdir?").
     - **Yönlendirici Niyet**: Kullanıcı belirli bir web sitesine veya sayfaya gitmek ister (örneğin, "Louvre Müzesi resmi web sitesi").
     - **İşlem Odaklı Niyet**: Kullanıcı bir işlem gerçekleştirmek ister, örneğin uçak bileti rezervasyonu yapmak veya bir satın alma işlemi yapmak (örneğin, "Paris'e uçak bileti al").

2. **Bağlam Farkındalığı**:
   - Kullanıcının sorgusunun bağlamını analiz etmek, niyetini doğru bir şekilde belirlemede yardımcı olur. Bu, önceki etkileşimleri, kullanıcı tercihlerini ve mevcut sorgunun özel ayrıntılarını dikkate almayı içerir.

3. **Doğal Dil İşleme (NLP)**:
   - Kullanıcıların sağladığı doğal dil sorgularını anlamak ve yorumlamak için NLP teknikleri kullanılır. Bu, varlık tanıma, duygu analizi ve sorgu ayrıştırma gibi görevleri içerir.

4. **Kişiselleştirme**:
   - Kullanıcının geçmişi, tercihleri ve geri bildirimlerine dayalı olarak arama sonuçlarını kişiselleştirmek, alınan bilgilerin alaka düzeyini artırır.
#### Pratik Bir Örnek: Seyahat Acentasında Amaç Odaklı Arama

Seyahat Acentası'nı bir örnek olarak ele alalım ve amaç odaklı aramanın nasıl uygulanabileceğini görelim.

1. **Kullanıcı Tercihlerinin Toplanması**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Kullanıcı Amacını Anlama**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Bağlam Farkındalığı**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Sonuçları Arama ve Kişiselleştirme**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **Örnek Kullanım**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Bir Araç Olarak Kod Üretimi

Kod üreten ajanlar, karmaşık problemleri çözmek ve görevleri otomatikleştirmek için yapay zeka modellerini kullanarak kod yazıp çalıştırır.

### Kod Üreten Ajanlar

Kod üreten ajanlar, çeşitli programlama dillerinde kod yazıp çalıştırmak için üretici yapay zeka modellerini kullanır. Bu ajanlar, karmaşık problemleri çözebilir, görevleri otomatikleştirebilir ve kod üreterek değerli içgörüler sağlayabilir.

#### Pratik Uygulamalar

1. **Otomatik Kod Üretimi**: Veri analizi, web kazıma veya makine öğrenimi gibi belirli görevler için kod parçacıkları oluşturma.
2. **SQL'i RAG Olarak Kullanma**: Veritabanlarından veri almak ve manipüle etmek için SQL sorguları kullanma.
3. **Problem Çözme**: Algoritmaları optimize etmek veya verileri analiz etmek gibi belirli problemleri çözmek için kod oluşturma ve çalıştırma.

#### Örnek: Veri Analizi için Kod Üreten Ajan

Bir kod üreten ajan tasarladığınızı hayal edin. İşte nasıl çalışabileceği:

1. **Görev**: Bir veri kümesini analiz ederek eğilimleri ve desenleri belirlemek.
2. **Adımlar**:
   - Veri kümesini bir veri analizi aracına yükleyin.
   - Verileri filtrelemek ve birleştirmek için SQL sorguları oluşturun.
   - Sorguları çalıştırarak sonuçları alın.
   - Sonuçları görselleştirmeler ve içgörüler oluşturmak için kullanın.
3. **Gerekli Kaynaklar**: Veri kümesine erişim, veri analizi araçları ve SQL yetenekleri.
4. **Deneyim**: Geçmiş analiz sonuçlarını kullanarak gelecekteki analizlerin doğruluğunu ve alaka düzeyini artırma.

### Örnek: Seyahat Acentası için Kod Üreten Ajan

Bu örnekte, kullanıcıların seyahatlerini planlamalarına yardımcı olmak için kod üreten ve çalıştıran bir ajan olan Seyahat Acentası'nı tasarlayacağız. Bu ajan, seyahat seçeneklerini getirme, sonuçları filtreleme ve üretici yapay zeka kullanarak bir seyahat planı oluşturma gibi görevleri yerine getirebilir.

#### Kod Üreten Ajanın Genel Görünümü

1. **Kullanıcı Tercihlerinin Toplanması**: Kullanıcıdan varış noktası, seyahat tarihleri, bütçe ve ilgi alanları gibi bilgileri toplar.
2. **Veri Getirmek için Kod Üretimi**: Uçuşlar, oteller ve gezilecek yerler hakkında veri almak için kod parçacıkları oluşturur.
3. **Üretilen Kodu Çalıştırma**: Gerçek zamanlı bilgi almak için üretilen kodu çalıştırır.
4. **Seyahat Planı Oluşturma**: Alınan verileri kişiselleştirilmiş bir seyahat planına dönüştürür.
5. **Geri Bildirime Göre Ayarlama**: Kullanıcı geri bildirimi alır ve sonuçları iyileştirmek için kodu yeniden üretir.

#### Adım Adım Uygulama

1. **Kullanıcı Tercihlerinin Toplanması**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Veri Getirmek için Kod Üretimi**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Üretilen Kodu Çalıştırma**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Seyahat Planı Oluşturma**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Geri Bildirime Göre Ayarlama**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Çevresel Farkındalık ve Akıl Yürütme Kullanımı

Tablonun şemasına dayalı olarak sorgu oluşturma sürecini geliştirmek, çevresel farkındalık ve akıl yürütme kullanılarak mümkün olabilir.

İşte bunun nasıl yapılabileceğine dair bir örnek:

1. **Şemayı Anlama**: Sistem, tablonun şemasını anlayacak ve bu bilgiyi sorgu oluşturmayı temellendirmek için kullanacaktır.
2. **Geri Bildirime Göre Ayarlama**: Sistem, geri bildirime dayalı olarak kullanıcı tercihlerini ayarlayacak ve şemadaki hangi alanların güncellenmesi gerektiğini düşünecektir.
3. **Sorguları Oluşturma ve Çalıştırma**: Sistem, yeni tercihlere dayalı olarak sorgular oluşturacak ve çalıştıracaktır.

İşte bu kavramları içeren güncellenmiş bir Python kodu örneği:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Açıklama - Geri Bildirime Dayalı Rezervasyon

1. **Şema Farkındalığı**: `schema` sözlüğü, geri bildirime dayalı olarak tercihlerin nasıl ayarlanması gerektiğini tanımlar. Bu, `favorites` ve `avoid` gibi alanları ve bunlara karşılık gelen ayarlamaları içerir.
2. **Tercihleri Ayarlama (`adjust_based_on_feedback` metodu)**: Bu metot, kullanıcı geri bildirimlerine ve şemaya dayalı olarak tercihleri ayarlar.
3. **Çevreye Dayalı Ayarlamalar (`adjust_based_on_environment` metodu)**: Bu metot, şema ve geri bildirimlere dayalı olarak ayarlamaları özelleştirir.
4. **Sorguları Oluşturma ve Çalıştırma**: Sistem, ayarlanmış tercihlere dayalı olarak veri almak için kod oluşturur ve bu sorguların çalıştırılmasını simüle eder.
5. **Seyahat Planı Oluşturma**: Sistem, yeni uçuş, otel ve gezilecek yer verilerine dayalı olarak güncellenmiş bir seyahat planı oluşturur.

Sistemi çevreye duyarlı hale getirerek ve şemaya dayalı akıl yürütme yaparak, daha doğru ve alakalı sorgular oluşturulabilir. Bu da daha iyi seyahat önerileri ve daha kişiselleştirilmiş bir kullanıcı deneyimi sağlar.

### SQL'i Bir Retrieval-Augmented Generation (RAG) Tekniği Olarak Kullanma

SQL (Structured Query Language), veritabanlarıyla etkileşim kurmak için güçlü bir araçtır. Retrieval-Augmented Generation (RAG) yaklaşımının bir parçası olarak kullanıldığında, SQL, AI ajanlarında yanıtları veya eylemleri bilgilendirmek ve oluşturmak için veritabanlarından ilgili verileri alabilir. Seyahat Acentası bağlamında SQL'in bir RAG tekniği olarak nasıl kullanılabileceğini inceleyelim.

#### Temel Kavramlar

1. **Veritabanı Etkileşimi**:
   - SQL, veritabanlarını sorgulamak, ilgili bilgileri almak ve verileri manipüle etmek için kullanılır.
   - Örnek: Bir seyahat veritabanından uçuş detaylarını, otel bilgilerini ve gezilecek yerleri almak.

2. **RAG ile Entegrasyon**:
   - SQL sorguları, kullanıcı girdilerine ve tercihlerine göre oluşturulur.
   - Alınan veriler, kişiselleştirilmiş öneriler veya eylemler oluşturmak için kullanılır.

3. **Dinamik Sorgu Oluşturma**:
   - AI ajanı, bağlama ve kullanıcı ihtiyaçlarına göre dinamik SQL sorguları oluşturur.
   - Örnek: Bütçe, tarihler ve ilgi alanlarına göre sonuçları filtrelemek için SQL sorgularını özelleştirme.

#### Uygulamalar

- **Otomatik Kod Üretimi**: Belirli görevler için kod parçacıkları oluşturma.
- **SQL'i RAG Olarak Kullanma**: Verileri manipüle etmek için SQL sorguları kullanma.
- **Problem Çözme**: Problemleri çözmek için kod oluşturma ve çalıştırma.

**Örnek**:
Bir veri analizi ajanı:

1. **Görev**: Bir veri kümesini analiz ederek eğilimleri bulma.
2. **Adımlar**:
   - Veri kümesini yükleyin.
   - Verileri filtrelemek için SQL sorguları oluşturun.
   - Sorguları çalıştırarak sonuçları alın.
   - Görselleştirmeler ve içgörüler oluşturun.
3. **Kaynaklar**: Veri kümesine erişim, SQL yetenekleri.
4. **Deneyim**: Geçmiş sonuçları kullanarak gelecekteki analizleri iyileştirme.

#### Pratik Örnek: Seyahat Acentasında SQL Kullanımı

1. **Kullanıcı Tercihlerinin Toplanması**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL Sorguları Oluşturma**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL Sorgularını Çalıştırma**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Öneriler Oluşturma**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Örnek SQL Sorguları

1. **Uçuş Sorgusu**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Otel Sorgusu**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Gezilecek Yer Sorgusu**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

SQL'i Retrieval-Augmented Generation (RAG) tekniğinin bir parçası olarak kullanarak, Seyahat Acentası gibi AI ajanları, doğru ve kişiselleştirilmiş öneriler sağlamak için dinamik olarak ilgili verileri alabilir ve kullanabilir.

### Metakognisyon Örneği

Metakognisyonun bir uygulamasını göstermek için, bir problemin çözüm sürecinde karar verme sürecini "düşünen" basit bir ajan oluşturalım. Bu örnekte, bir ajan bir otel seçimini optimize etmeye çalışacak, ancak hatalar veya alt-optimal seçimler yaptığında kendi akıl yürütmesini değerlendirecek ve stratejisini ayarlayacaktır.

Bunu, fiyat ve kalite kombinasyonuna dayalı olarak otelleri seçen bir ajan örneğiyle simüle edeceğiz. Ancak, ajan "kararlarını" gözden geçirip stratejisini buna göre ayarlayacaktır.

#### Bu Metakognisyonu Nasıl Gösterir:

1. **İlk Karar**: Ajan, kalite etkisini anlamadan en ucuz oteli seçecektir.
2. **Yansıma ve Değerlendirme**: İlk seçimden sonra, ajan otelin "kötü" bir seçim olup olmadığını kullanıcı geri bildirimiyle kontrol edecektir. Eğer otelin kalitesinin çok düşük olduğunu görürse, akıl yürütmesini gözden geçirir.
3. **Stratejiyi Ayarlama**: Ajan, yansımasına dayanarak stratejisini ayarlar ve "en ucuz" yerine "en yüksek kalite" seçeneğine geçer, böylece gelecekteki karar verme sürecini iyileştirir.

İşte bir örnek:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Ajanların Metakognitif Yetenekleri

Buradaki anahtar, ajanın:
- Önceki seçimlerini ve karar verme sürecini değerlendirme yeteneği.
- Bu yansıma temelinde stratejisini ayarlama yeteneği, yani metakognisyonun devreye girmesi.

Bu, sistemin iç geri bildirimlere dayalı olarak akıl yürütme sürecini ayarlayabildiği basit bir metakognisyon biçimidir.

### Sonuç

Metakognisyon, AI ajanlarının yeteneklerini önemli ölçüde artırabilecek güçlü bir araçtır. Metakognitif süreçleri entegre ederek, daha akıllı, uyarlanabilir ve verimli ajanlar tasarlayabilirsiniz. Ek kaynakları kullanarak AI ajanlarında metakognisyonun büyüleyici dünyasını daha fazla keşfedebilirsiniz.

### Metakognisyon Tasarım Deseni Hakkında Daha Fazla Sorunuz mu Var?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) adresine katılarak diğer öğrenenlerle tanışabilir, ofis saatlerine katılabilir ve AI Ajanları hakkındaki sorularınıza yanıt alabilirsiniz.

## Önceki Ders

[Çoklu Ajan Tasarım Deseni](../08-multi-agent/README.md)

## Sonraki Ders

[Üretimde AI Ajanları](../10-ai-agents-production/README.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.