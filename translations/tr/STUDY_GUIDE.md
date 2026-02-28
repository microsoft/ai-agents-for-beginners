# Yeni Başlayanlar için Yapay Zeka Ajanları - Çalışma Rehberi ve Kurs Özeti

Bu rehber, "Yeni Başlayanlar için Yapay Zeka Ajanları" kursunun özetini sunar ve Yapay Zeka Ajanları oluşturmak için temel kavramları, çerçeveleri ve tasarım kalıplarını açıklar.

## 1. Yapay Zeka Ajanlarına Giriş

**Yapay Zeka Ajanları Nedir?**
Yapay Zeka Ajanları, Büyük Dil Modelleri'nin (LLM'ler) yeteneklerini **araçlar**, **bilgi** ve **hafıza** erişimi vererek genişleten sistemlerdir. Sadece eğitim verisine dayanarak metin üreten standart bir dil modeli sohbet botunun aksine, bir Yapay Zeka Ajanı:
- Çevresini **algılayabilir** (sensörler veya girişler aracılığıyla).
- Bir problemi çözmek için **akıl yürütebilir**.
- Çevreyi değiştirmek için **eylemde bulunabilir** (aktüatörler veya araç çalıştırma yoluyla).

**Bir Ajanın Temel Bileşenleri:**
- **Çevre**: Ajanın faaliyet gösterdiği alan (örneğin bir rezervasyon sistemi).
- **Sensörler**: Bilgi toplama mekanizmaları (örneğin bir API okuma).
- **Aktüatörler**: Eylem gerçekleştirme mekanizmaları (örneğin e-posta gönderme).
- **Beyin (LLM)**: Hangi eylemlerin yapılacağına karar veren planlama ve akıl yürütme motoru.

## 2. Ajanik Çerçeveler

Kurs, ajanlar oluşturmak için **Microsoft Agent Framework (MAF)** ile **Azure AI Foundry Agent Service V2** kullanmaktadır:

| Bileşen | Odak Noktası | En Uygun Kullanım |
|---------|--------------|-------------------|
| **Microsoft Agent Framework** | Ajanlar, araçlar ve iş akışları için birleşik Python/C# SDK | Araçlar kullanarak ajan oluşturma, çoklu ajan iş akışları ve üretim kalıpları. |
| **Azure AI Foundry Agent Service** | Yönetilen bulut çalışma zamanı | Yerleşik durum yönetimi, gözlemlenebilirlik ve güven ile güvenli, ölçeklenebilir dağıtım. |

## 3. Ajanik Tasarım Kalıpları

Tasarım kalıpları, ajanların sorunları güvenilir bir şekilde çözmek için nasıl çalıştığını yapılandırmaya yardımcı olur.

### **Araç Kullanım Kalıbı** (Ders 4)
Bu kalıp, ajanların dış dünya ile etkileşime geçmesini sağlar.
- **Kavram**: Ajana, kullanılabilir fonksiyonlar ve parametrelerin bir listesinden oluşan bir "şema" sağlanır. LLM, kullanıcının isteğine dayanarak *hangi* aracın *hangi* argümanlarla çağrılacağına karar verir.
- **Akış**: Kullanıcı İsteği -> LLM -> **Araç Seçimi** -> **Araç Çalıştırma** -> LLM (araç çıktısı ile) -> Son Yanıt.
- **Kullanım Alanları**: Gerçek zamanlı veri alma (hava durumu, hisse senedi fiyatları), hesaplamalar yapma, kod çalıştırma.

### **Planlama Kalıbı** (Ders 7)
Bu kalıp, ajanların karmaşık, çok adımlı görevleri çözmesini sağlar.
- **Kavram**: Ajan, yüksek seviyeli bir hedefi daha küçük alt görevlere böler.
- **Yaklaşımlar**:
  - **Görev Parçalama**: "Bir seyahat planla"yı "Uçak rezervasyonu", "Otel rezervasyonu", "Araba kiralama"ya bölme.
  - **Yinelemeli Planlama**: Önceki adımların çıktısına göre planı tekrar değerlendirme (örneğin uçak doluysa farklı bir tarih seçme).
- **Uygulama**: Genellikle yapılandırılmış plan (örneğin JSON) oluşturan bir "Planlayıcı" ajan içerir ve bu plan diğer ajanlar tarafından yürütülür.

## 4. Tasarım İlkeleri

Ajan tasarlarken üç boyut göz önünde bulundurulur:
- **Alan**: Ajanlar insanları ve bilgiyi birbirine bağlamalı, erişilebilir ama dikkat dağıtmayan olmalıdır.
- **Zaman**: Ajanlar *Geçmiş*ten öğrenmeli, *Şimdi*de ilgili yönlendirmeler sağlamalı ve *Gelecek* için uyum sağlamalıdır.
- **Çekirdek**: Belirsizliği kabul eder, ancak şeffaflık ve kullanıcı kontrolü yoluyla güven tesis eder.

## 5. Önemli Derslerin Özeti

- **Ders 1**: Ajanlar sadece modeller değil, sistemdir. Algılar, akıl yürütür ve eylemde bulunur.
- **Ders 2**: Microsoft Agent Framework, araç çağırma ve durum yönetimini soyutlar.
- **Ders 3**: Tasarımı şeffaflık ve kullanıcı kontrolü gözeterek yapın.
- **Ders 4**: Araçlar ajanın "elleridir". LLM'in nasıl kullanacağını anlaması için şema tanımı kritik önemdedir.
- **Ders 7**: Planlama, ajanın karmaşık iş akışlarını yönetmesini sağlayan "yönetici işlevidir".

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle oluşabilecek herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->