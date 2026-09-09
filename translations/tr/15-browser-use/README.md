# Bilgisayar Kullanım Ajanları (CUA) Oluşturma

Bilgisayar kullanım ajanları, bir kişi gibi web siteleriyle etkileşime girebilir: bir tarayıcı açarak, sayfayı inceleyerek ve gördüklerinden sonraki en iyi işlemi yaparak. Bu derste, Airbnb'de arama yapan, yapılandırılmış liste verilerini çıkaran ve Stockholm'deki en ucuz konaklamayı belirleyen bir tarayıcı otomasyon ajanı oluşturacaksınız.

Ders, AI destekli gezinme için Browser-Use, tarayıcı kontrolü için Playwright ve Chrome DevTools Protocol (CDP), görme özellikli akıl yürütme için Azure OpenAI ve yapılandırılmış çıkarım için Pydantic'i birleştirir.

## Giriş

Bu ders şunları kapsayacak:

- Bilgisayar kullanım ajanlarının API-only otomasyona göre ne zaman daha uygun olduğunu anlama
- Güvenilir tarayıcı yaşam döngüsü yönetimi için Browser-Use ile Playwright ve CDP'yi birleştirme
- Dinamik web sayfalarından liste verilerini çıkarmak için Azure OpenAI görme ve yapılandırılmış Pydantic çıktısını kullanma
- Ajan-öncelikli, aktör-öncelikli veya hibrit tarayıcı otomasyon iş akışını ne zaman kullanacağınıza karar verme

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra, şunları bileceksiniz:

- Browser-Use'i Azure OpenAI ve Playwright ile yapılandırmak
- Gerçek bir web sitesinde gezinip dinamik UI öğelerini işleyen bir tarayıcı otomasyon iş akışı oluşturmak
- Görünür sayfa içeriğinden yazılı sonuçlar çıkarmak ve bunları sonraki iş mantığına dönüştürmek
- Tarayıcı görevinin ne kadar öngörülebilir olduğuna göre ajan ve aktör kalıpları arasında seçim yapmak

## Kod Örneği

Bu derste bir not defteri eğitimi bulunmaktadır:

- [15-browser-user.ipynb](./15-browser-user.ipynb): CDP üzerinden bir Chrome oturumu başlatır, Airbnb'de Stockholm listelerinde arama yapar, Browser-Use görme ile fiyatları çıkarır ve en ucuz seçeneği yapılandırılmış veri olarak döndürür.

## Önkoşullar

- Python 3.12+
- Ortamınızda yapılandırılmış Azure OpenAI dağıtımı
- Yerel olarak kurulu Chrome veya Chromium
- Yüklü Playwright bağımlılıkları
- Async Python hakkında temel aşinalık

## Kurulum

Not defterinde kullanılan paketleri yükleyin:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Not defteri tarafından kullanılan Azure OpenAI ortam değişkenlerini ayarlayın:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# İsteğe bağlı: Atlandığında varsayılan olarak en son API sürümünü kullanır
AZURE_OPENAI_API_VERSION=...
```

## Mimari Genel Bakış

Not defteri hibrit bir tarayıcı otomasyon iş akışını gösterir:

1. Chrome, hem Playwright hem de Browser-Use'un aynı tarayıcı oturumunu paylaşabilmesi için CDP etkin olarak başlar.
2. Bir Browser-Use ajanı, Airbnb'yi açmak, açılır pencereleri kapatmak ve Stockholm'de arama yapmak gibi açık uçlu gezinme görevlerini yönetir.
3. Aktif sayfa, listelerin başlıklarını, gecelik fiyatları, değerlendirmeleri ve URL'leri çıkarmak için yapılandırılmış bir Pydantic şeması ile incelenir.
4. Python mantığı çıkarılan listeleri karşılaştırır ve en ucuz sonucu vurgular.

Bu yaklaşım, Browser-Use'ın iyi olduğu esnek, görmeye dayalı akıl yürütmeyi korurken ihtiyacınız olduğunda kesin tarayıcı kontrolü sağlar.

## Temel Çıkarımlar ve En İyi Uygulamalar

### Ajan ve Aktör kullanımı için ne zaman

| Senaryo | Ajan Kullan | Aktör Kullan |
|----------|-----------|-----------|
| Dinamik düzenler | Evet, AI sayfa değişikliklerine uyum sağlar | Hayır, kırılgan seçiciler bozulabilir |
| Bilinen yapı | Hayır, ajan doğrudan kontrolden daha yavaştır | Evet, hızlı ve hassas |
| Öğeleri bulma | Evet, doğal dil iyi çalışır | Hayır, kesin seçiciler gereklidir |
| Zamanlama kontrolü | Hayır, daha az öngörülebilir | Evet, beklemeler ve denemeler üzerinde tam kontrol |
| Karmaşık iş akışları | Evet, beklenmeyen UI durumlarını yönetir | Hayır, açık dallanma gerekir |

### Browser-Use En İyi Uygulamalar

1. Keşif ve dinamik gezinme için bir ajanla başlayın.
2. Etkileşim öngörülebilir olduğunda doğrudan sayfa kontrolüne geçin.
3. Çıkarılan verinin doğrulandığı ve tip güvenli olduğu yapılandırılmış çıktı modelleri kullanın.
4. Görünür UI değişikliklerini tetikleyen işlemlerden sonra stratejik gecikmeler ekleyin.
5. Hata ayıklamayı kolaylaştırmak için yineleme sırasında ekran görüntüleri alın.
6. Web sitelerinin değişmesini bekleyin ve açılır pencereler ile düzen değişiklikleri için yedek stratejiler tasarlayın.
7. Esneklik ve doğruluk için ajan ve aktör kalıplarını harmanlayın.

### Tarayıcı Ajanları için Güvenlik Önlemleri

Tarayıcı ajanları canlı web sitelerinde çalıştığından, yalnızca bilinen bir API çağıran bir betikten daha sıkı sınırlar gerekir. Bir not defteri demosundan gerçek iş akışına geçmeden önce, ajanın ne görebileceği, neye tıklayabileceği ve neyi gönderebileceği konusunda kontroller tanımlayın.

1. **Gezinme ortamını kapsamlı belirleyin.** Ajanı, görev için gereken etki alanları ile sınırlı özel bir tarayıcı profili veya kum havuzunda çalıştırın.
2. **Gözlem ile eylemi ayırın.** Ajana önce arama yapma, okuma ve veri çıkarma izni verin; formları gönderme, mesaj gönderme, seyahat rezervasyonu yapma, satın alma, kayıt silme veya hesap ayarlarını değiştirme gibi işlemler için açık onay adımı gerektir.
3. **Şifreleri ve gizli bilgileri istemlere ve izlere koymayın.** Parolalar, ödeme bilgileri, oturum çerezleri veya ham kişisel verileri model bağlamına koymayın. Kimlik doğrulama için kullanıcıyı devralmaya izin verin ve günlüklerden hassas alanları sansürleyin.
4. **Sayfa içeriğini güvenilmez giriş olarak değerlendirin.** Bir web sitesi, kullanıcı için değil agent için talimat içerebilir. Ajan, hedefini değiştirmesini isteyen, verileri ifşa eden, korumaları devre dışı bırakan veya ilgisiz siteleri ziyaret etmeye zorlayan sayfa metinlerini görmezden gelmelidir.
5. **Riskli adımlar için belirleyici kontroller kullanın.** Nihai adımı kullanıcının onaylamasını istemeden önce mevcut URL, sayfa başlığı, seçilen öğe, fiyat, alıcı ve eylem özetini kod ile doğrulayın.
6. **Bütçeleri ve durdurma koşullarını belirleyin.** Ajanın kullanabileceği işlem, deneme, sekme ve dakika sayılarını sınırlayın. Sayfa durumu belirsizse tıklamaya devam etmek yerine durdurun.
7. **Her şeyi değil faydalı kanıtları kaydedin.** Başarı özetleri, zaman damgaları, URL'ler, seçilen öğe açıklamaları ve ekran görüntüsü referanslarını tutarak hataların incelenmesini sağlayın, gereksiz hassas sayfa içeriğini saklamaktan kaçının.

Airbnb örneğinde varsayılan güvenli işlem, listelerde arama yapıp fiyatları çıkarmaktır. Giriş yapma, ev sahibiyle iletişim veya rezervasyon tamamlama ayrı, kullanıcı onaylı işlem olmalıdır.

### Gerçek Dünya Uygulamaları

- Seyahat rezervasyonu ve fiyat takibi
- E-ticaret fiyat karşılaştırması ve stok kontrolü
- Dinamik web sitelerinden yapılandırılmış çıkarım
- Görüş odaklı UI testi ve doğrulama
- Web sitesi izleme ve uyarılandırma
- Çok adımlı formlarda zeki form doldurma

## Gerçek Dünya Örneği: Microsoft Project Opal

Bu derste oluşturduğunuz ajan, bir **bilgisayar kullanım ajanı (CUA)**’nın küçük, yerel bir versiyonudur — bir kişinin kullandığı şekilde tarayıcıyı yöneten bir program. Microsoft aynı fikri, Microsoft 365 Copilot'taki bir özellik olan **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** ile kurumsal ortama getiriyor.

Project Opal ile bir görevi tanımlarsınız ve ajan, kuruluşunuzun tarayıcı tabanlı uygulamaları, siteleri ve verileri üzerinde **Windows 365 Bulut PC'de güvenli bilgisayar kullanımı** ile sizin adınıza çalışır. **Arka planda asenkron çalışır** ve istediğiniz zaman işi yönlendirebilir veya kontrolü üstlenebilirsiniz. Örnek işler arasında:

- Güvenlik grup üyelik taleplerini yönetmek
- Uyumluluk incelemeleri için denetim kanıtları toplamak ve doğrulamak
- BT olaylarını triyaj etmek (bilet durumunu güncellemek, sahip atamak, kopyaları kapatmak)
- Excel verilerini finansal kapanış sunumuna derlemek

Opal, **üretim kalitesinde, güvenilir** bir bilgisayar kullanım ajanının nasıl göründüğüne dair yararlı bir referans sunar — ve önceki derslerdeki kavramları pekiştirir:

| Bu kurstaki kavram | Project Opal uygulaması |
|------------------------|-----------------------------|
| **İnsan döngüde** (Ders 06) | Opal giriş bilgileri, hassas veriler veya belirsiz talimatlar için duraklar ve asla şifre girmez veya formları göndermek için açık onay olmadan işlem yapmaz. Görev sırasında *Kontrolü Üstlenebilir* ve *Kontrolü Geri Verebilirsiniz*. |
| **Güvenilir ve güvenli ajanlar** (Dersler 06 & 18) | İzole edilmiş bir Windows 365 Bulut PC'de çalışır, varsayılan olarak yalnızca tarayıcı erişimine izin verir (diğer bilgisayar erişimi Intune ile engellenir), *kendi* kimliğinizi kullanır, sadece yetkinizle erişime izin verir ve tüm eylemleri denetlenebilirlik için kaydeder. |
| **Planlama ve üstbiliş** (Dersler 07 & 09) | Opal önce işi için bir plan oluşturur, sonra kendi akıl yürütmesini adım adım denetler ve şüpheli etkinlik fark ederse duraklar. |
| **Yeniden kullanılabilir yetenekler / araçlar** (Ders 04) | **Beceriler** tekrarlanabilir işler için talimat yazmanıza (bir `.md` dosyasından içe aktarılabilir veya Opal ile oluşturulabilir) ve bunları konuşmalar arasında yeniden kullanmanıza olanak tanır. |

> **Erişilebilirlik:** Project Opal şu anda Microsoft 365 Copilot aboneliğiyle [Frontier erken erişim programı](https://adoption.microsoft.com/copilot/frontier-program/) kullanıcılarına sunulmaktadır ve yöneticinizin kurulumu tamamlaması gerekir. Deneysel bir Frontier özelliği olduğundan, özellikler zamanla değişebilir.

## Bilgi Kontrolü

Bir sonraki derse geçmeden önce anlayışınızı test edin.

**1. Bir tarayıcı tabanlı bilgisayar kullanım ajanı, yalnızca API iş akışına göre ne zaman daha uygundur?**

<details>
<summary>Cevap</summary>

Görev web UI'da görünenlere bağlıysa, site gerekli API'yi sunmuyorsa veya sayfa sık değişiyorsa (sabit API veya seçici mantığı kırılgan olur), tarayıcı ajanı kullanın. Aynı görev için stabil bir API varsa, genellikle daha hızlı, test edilmesi kolay ve güvenli olduğu için API tercih edilmelidir.
</details>

**2. Hibrit iş akışında, hangi kısımlar ajan tarafından, hangi kısımlar doğrudan Playwright kodu tarafından yönetilmelidir?**

<details>
<summary>Cevap</summary>

Ajana açık uçlu gezinme ve dinamik UI durumları gibi işleri bırakın, örneğin doğru sayfayı bulma veya beklenmeyen açılır pencereleri kapatma. Sayfa yapısı bilindiğinde ve işlem hassasiyet, deneme, bekleme veya belirleyici doğrulama gerektirdiğinde doğrudan Playwright kontrolüne geçin.
</details>

**3. Airbnb örneği, kullanıcının rezervasyon yapmak isteyebileceği bir liste bulur. İş akışı oturum açmadan, ev sahibi ile iletişim kurmadan veya rezervasyon yapmadan önce ne olmalıdır?**

<details>
<summary>Cevap</summary>

İş akışı durmalı ve açık kullanıcı onayı istemelidir. Öncesinde, seçilen liste, mevcut URL, fiyat, tarih ve yapılacak işlem açıkça özetlenmelidir. Arama yapmak ve fiyat çıkarmak bağımsız olabilir; hesap erişimi, mesajlar, satın alımlar ve rezervasyonlar kullanıcı onaylı olmalıdır.
</details>

**4. Bir web sayfası, ajanı özgün talimatlarını görmezden gelmeye, başka bir siteye gitmeye ve kayıtlı kimlik bilgilerini açığa çıkarmaya çağırıyor. Ajan bu metni nasıl değerlendirmelidir?**

<details>
<summary>Cevap</summary>

Bunu güvenilmez sayfa içeriği olarak değerlendirin, geliştirici veya kullanıcı talimatı olarak değil. Ajan izin verilen etki alanı ve görev kapsamı içinde kalmalı, sırları ifşa etmeyi reddetmeli ve hedefi değiştiren, korumaları devre dışı bırakan veya ilgisiz sitelere gönderen metni takip etmemelidir.
</details>

**5. Bir tarayıcı ajanı çalışırken hangi kanıtlar tutulmalı ve nelerden kaçınılmalıdır?**

<details>
<summary>Cevap</summary>

İşlem özetlerini, zaman damgalarını, URL'leri, seçilen öğe açıklamalarını, doğrulama sonuçlarını ve ekran görüntüsü referanslarını saklayın ki işlemler incelenebilsin. Parolalar, ödeme bilgileri, oturum çerezleri, ham kişisel veriler veya tüm sayfa içerikleri yalnızca belirli bir saklama ve gizlilik nedeni varsa saklanmalıdır.
</details>

## Ek Kaynaklar

- [Project Opal (Frontier) ile Başlayın](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright entegrasyon şablonu](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktör parametreleri ve içerik çıkarımı](https://docs.browser-use.com/customize/actor/all-parameters)
- [Ders Kurulumu](../00-course-setup/README.md)

## Önceki Ders

[Microsoft Agent Framework'ü Keşfetme](../14-microsoft-agent-framework/README.md)

## Sonraki Ders

[Ölçeklenebilir Ajanların Dağıtımı](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->