# Yeni Başlayanlar için Yapay Zeka Ajanları - Çalışma Rehberi ve Kurs Özeti

Bu rehber, "Yeni Başlayanlar için Yapay Zeka Ajanları" kursunun özetini sunar ve Yapay Zeka Ajanları oluşturmak için temel kavramları, çerçeveleri ve tasarım kalıplarını açıklar.

## 1. Yapay Zeka Ajanlarına Giriş

**Yapay Zeka Ajanları nedir?**  
Yapay Zeka Ajanları, Büyük Dil Modellerinin (LLM'ler) yeteneklerini **araçlar**, **bilgi** ve **hafıza** erişimi vererek genişleten sistemlerdir. Sadece eğitim verilerine dayanarak metin üreten standart bir LLM sohbet botundan farklı olarak, bir Yapay Zeka Ajanı:  
- Çevresini **algılayabilir** (sensörler veya girdiler aracılığıyla).  
- Bir problemi nasıl çözeceği konusunda **akıl yürütebilir**.  
- Çevreyi değiştirmek için **harekete geçebilir** (eylem cihazları veya araç çalıştırma yoluyla).  

**Bir Ajanın Temel Bileşenleri:**  
- **Çevre**: Ajanın faaliyet gösterdiği alan (örneğin, bir rezervasyon sistemi).  
- **Sensörler**: Bilgi toplama mekanizmaları (örneğin, bir API okumak).  
- **Eylem Cihazları**: Eylem gerçekleştirme mekanizmaları (örneğin, e-posta göndermek).  
- **Beyin (LLM)**: Hangi eylemlerin alınacağına karar veren ve planlama yapan akıl yürütme motoru.  

## 2. Ajan Çerçeveleri

Kurs, ajan oluşturmak için üç ana çerçeveyi kapsar:

| Çerçeve | Odak | En İyi Kullanım Alanı |
|---------|------|----------------------|
| **Semantic Kernel** | .NET/Python için üretime hazır SDK | Kurumsal uygulamalar, yapay zekanın mevcut kodla entegrasyonu. |
| **AutoGen** | Çok ajanlı iş birliği | Birbirleriyle konuşan birden fazla uzmanlaşmış ajanın gerektiği karmaşık senaryolar. |
| **Azure AI Agent Service** | Yönetilen bulut hizmeti | Yerleşik durum yönetimi ile güvenli, ölçeklenebilir dağıtım. |

## 3. Ajan Tasarım Kalıpları

Tasarım kalıpları, ajanların sorunları güvenilir şekilde çözmek için nasıl yapılandırılacağını gösterir.

### **Araç Kullanım Kalıbı** (Ders 4)  
Bu kalıp, ajanların dış dünyayla etkileşim kurmasını sağlar.  
- **Kavram**: Ajana "şema" (mevcut fonksiyonlar ve parametreleri listesi) sağlanır. LLM, kullanıcının isteğine dayanarak *hangi* aracı ve *hangi* argümanlarla çağıracağına karar verir.  
- **Akış**: Kullanıcı İsteği -> LLM -> **Araç Seçimi** -> **Araç Çalıştırma** -> LLM (araç çıktısı ile) -> Nihai Yanıt.  
- **Kullanım Alanları**: Gerçek zamanlı veri alma (hava durumu, hisse senedi fiyatları), hesaplamalar yapma, kod çalıştırma.  

### **Planlama Kalıbı** (Ders 7)  
Bu kalıp, ajanların karmaşık, çok aşamalı görevleri çözmesini sağlar.  
- **Kavram**: Ajan, yüksek seviyeli bir hedefi daha küçük alt görevlere ayırır.  
- **Yaklaşımlar**:  
  - **Görev Parçalama**: "Bir seyahat planla" görevini "Uçak bileti ayırt", "Otel ayırt", "Araba kirala" olarak bölmek.  
  - **Yinelemeli Planlama**: Önceki adımların çıktısına göre planı yeniden değerlendirmek (örneğin, uçak doluysa farklı bir tarih seçmek).  
- **Uygulama**: Genellikle yapılandırılmış bir plan (örneğin JSON) oluşturan bir "Planlayıcı" ajan içerir; bu plan diğer ajanlar tarafından uygulanır.  

## 4. Tasarım İlkeleri

Ajan tasarlarken üç boyutu dikkate alın:  
- **Mekan**: Ajanlar insanları ve bilgiyi bağlamalı, erişilebilir ama rahatsız edici olmamalıdır.  
- **Zaman**: Ajanlar *Geçmiş*ten öğrenmeli, *Şimdi*de ilgili yönlendirmeler sağlamalı ve *Gelecek* için uyum sağlamalıdır.  
- **Çekirdek**: Belirsizliği kabul edin ancak şeffaflık ve kullanıcı kontrolü ile güven oluşturun.  

## 5. Önemli Derslerin Özeti

- **Ders 1**: Ajanlar sadece modeller değil, sistemlerdir. Algılar, akıl yürütür ve eylemde bulunurlar.  
- **Ders 2**: Semantic Kernel ve AutoGen gibi çerçeveler, araç çağırma ve durum yönetimi karmaşasını soyutlar.  
- **Ders 3**: Şeffaflık ve kullanıcı kontrolüyle tasarım yapın.  
- **Ders 4**: Araçlar, ajanın "elleridir". Şema tanımı, LLM'nin nasıl kullanacağını anlaması için kritiktir.  
- **Ders 7**: Planlama, ajanın karmaşık iş akışlarını yönetmesini sağlayan "yönetici fonksiyondur".

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi tavsiye edilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya hatalı yorumlamalardan sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->