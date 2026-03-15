# Yeni Başlayanlar için AI Ajanları - Çalışma Rehberi ve Kurs Özeti

Bu rehber, "Yeni Başlayanlar için AI Ajanları" kursunun özetini sağlar ve AI Ajanları oluşturmak için temel kavramları, çerçeveleri ve tasarım desenlerini açıklar.

## 1. AI Ajanlarına Giriş

**AI Ajanları Nedir?**  
AI Ajanları, Büyük Dil Modellerinin (LLM'ler) yeteneklerini **araçlar**, **bilgi** ve **hafıza** erişimi vererek genişleten sistemlerdir. Sadece eğitim verilerine dayanarak metin üreten standart bir LLM sohbet botunun aksine, bir AI Ajan:  
- Çevresini **algılar** (sensörler veya girdiler aracılığıyla).  
- Bir problemi çözmek için **akıl yürütür**.  
- Çevreyi değiştirmek için **harekete geçer** (aktüatörler veya araç yürütme yoluyla).

**Bir Ajanın Temel Bileşenleri:**  
- **Ortam**: Ajansın işlediği alan (örneğin, bir rezervasyon sistemi).  
- **Sensörler**: Bilgi toplama mekanizmaları (örneğin, bir API'yi okuma).  
- **Aktüatörler**: Eylem gerçekleştirme mekanizmaları (örneğin, bir e-posta gönderme).  
- **Beyin (LLM)**: Hangi eylemlerin alınacağına karar veren ve planlayan akıl yürütme motoru.

## 2. Ajansal Çerçeveler

Kurs, ajanlar oluşturmak için **Microsoft Agent Framework (MAF)** ile **Azure AI Foundry Agent Service V2** kullanmaktadır:

| Bileşen | Odak | En Uygun |
|---------|-------|----------|
| **Microsoft Agent Framework** | Ajanlar, araçlar ve iş akışları için birleşik Python/C# SDK'sı | Araçlarla ajanlar oluşturmak, çoklu ajan iş akışları ve üretim desenleri. |
| **Azure AI Foundry Agent Service** | Yönetilen bulut çalışma zamanı | Dahili durum yönetimi, gözlemlenebilirlik ve güven ile güvenli, ölçeklenebilir dağıtım. |

## 3. Ajansal Tasarım Desenleri

Tasarım desenleri, ajanların güvenilir şekilde problem çözmek için nasıl çalıştığını yapılandırmaya yardımcı olur.

### **Araç Kullanımı Deseni** (Ders 4)  
Bu desen, ajanların dış dünya ile etkileşime girmesini sağlar.  
- **Kavram**: Ajana bir "şema" (kullanılabilir fonksiyonlar ve parametrelerin listesi) verilir. LLM, kullanıcının isteğine dayanarak *hangi* aracı çağıracağını ve *hangi* argümanlarla çağıracağını belirler.  
- **Akış**: Kullanıcı İsteği -> LLM -> **Araç Seçimi** -> **Araç Yürütme** -> LLM (araç çıktısı ile) -> Nihai Yanıt.  
- **Kullanım Alanları**: Gerçek zamanlı veri alma (hava durumu, hisse fiyatları), hesaplamalar yapma, kod yürütme.

### **Planlama Deseni** (Ders 7)  
Bu desen, ajanların karmaşık çok adımlı görevleri çözmesini sağlar.  
- **Kavram**: Ajan, yüksek seviyeli bir hedefi daha küçük alt görevlere ayırır.  
- **Yaklaşımlar**:  
  - **Görev Parçalama**: "Bir gezi planla" görevini "Uçak bileti al", "Otel ayarla", "Araba kirala" alt görevlerine bölmek.  
  - **Yinelemeli Planlama**: Önceki adımların çıktısına dayanarak planı yeniden değerlendirmek (örneğin, uçak doluysa farklı bir tarih seçmek).  
- **Uygulama**: Genellikle yapılandırılmış bir plan (örneğin JSON) oluşturan "Planlayıcı" ajan içerir, ardından diğer ajanlar tarafından yürütülür.

## 4. Tasarım İlkeleri

Ajan tasarlarken üç boyutu göz önünde bulundurun:  
- **Mekan**: Ajanlar insanları ve bilgiyi bağlamalı, erişilebilir ancak göze batmamalıdır.  
- **Zaman**: Ajanlar *Geçmişten* öğrenmeli, *Şimdi* ilgili teşvikler sağlamalı ve *Geleceğe* uyum sağlamalıdır.  
- **Çekirdek**: Belirsizliği kabul edin ancak şeffaflık ve kullanıcı kontrolü sayesinde güven oluşturun.

## 5. Önemli Derslerin Özeti

- **Ders 1**: Ajanlar sadece modeller değil, sistemlerdir. Algılar, akıl yürütür ve hareket eder.  
- **Ders 2**: Microsoft Agent Framework, araç çağırma ve durum yönetiminin karmaşıklığını soyutlar.  
- **Ders 3**: Şeffaflık ve kullanıcı kontrolünü dikkate alarak tasarım yapın.  
- **Ders 4**: Araçlar, ajanın "elleridir". Şema tanımı, LLM'nin araçları nasıl kullanacağını anlaması için çok önemlidir.  
- **Ders 7**: Planlama, ajanın karmaşık iş akışlarını yönetmesini sağlayan "yürütücü fonksiyondur".

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi diliyle resmi ve yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek herhangi bir yanlış anlama veya yorum hatasından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->