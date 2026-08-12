# Bilgisayar Kullanım Ajanları (CUA) Oluşturma

Bilgisayar kullanım ajanları, bir kişinin yapacağı gibi web siteleriyle etkileşime girebilir: bir tarayıcı açarak, sayfayı inceleyerek ve gördüklerinden sonraki en iyi eylemi gerçekleştirerek. Bu derste, Airbnb'de arama yapan, yapılandırılmış liste verilerini çıkaran ve Stockholm'deki en ucuz konaklamayı belirleyen bir tarayıcı otomasyon ajanı oluşturacaksınız.

Ders, yapay zeka destekli gezinme için Browser-Use'u, tarayıcı kontrolü için Playwright ve Chrome DevTools Protokolü (CDP) ile Azure OpenAI'yi görsel destekli çıkarım için ve yapılandırılmış çıkarım için Pydantic'i birleştirir.

## Giriş

Bu ders şunları kapsayacaktır:

- Bilgisayar kullanım ajanlarının ne zaman sadece API otomasyonundan daha uygun olduğunu anlama
- Güvenilir tarayıcı yaşam döngüsü yönetimi için Browser-Use ile Playwright ve CDP'yi birleştirme
- Dinamik web sayfalarından liste verilerini çıkarmak için Azure OpenAI görsel ve yapılandırılmış Pydantic çıkışı kullanma
- Ne zaman ajan-öncelikli, aktör-öncelikli veya karma bir tarayıcı otomasyon iş akışı kullanmaya karar verme

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra, şunları bileceksiniz:

- Azure OpenAI ve Playwright ile Browser-Use'u yapılandırmak
- Gerçek bir web sitesinde gezinme yapan ve dinamik UI öğeleriyle başa çıkan bir tarayıcı otomasyon iş akışı oluşturmak
- Görünür sayfa içeriğinden yazılı sonuçlar çıkarmak ve bunları sonrası iş mantığına dönüştürmek
- Tarayıcı görevinin ne kadar öngörülebilir olduğuna göre ajan ve aktör kalıplarından birini seçmek

## Kod Örneği

Bu ders bir defter eğitimini içerir:

- [15-browser-user.ipynb](./15-browser-user.ipynb): CDP üzerinden bir Chrome oturumu başlatır, Airbnb'de Stockholm listelerinde arama yapar, Browser-Use görseliyle fiyatları çıkarır ve en ucuz seçeneği yapılandırılmış veri olarak döndürür.

## Önkoşullar

- Python 3.12+
- Ortamınızda Azure OpenAI dağıtımı yapılandırılmış olmalı
- Yerel olarak Chrome veya Chromium yüklü
- Playwright bağımlılıkları kurulu
- Async Python konusunda temel bilgi

## Kurulum

Defterde kullanılan paketleri yükleyin:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Defter tarafından kullanılan Azure OpenAI ortam değişkenlerini ayarlayın:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opsiyonel: Atlanırsa varsayılan olarak en son API sürümü kullanılır
AZURE_OPENAI_API_VERSION=...
```

## Mimari Genel Bakış

Defter karma bir tarayıcı otomasyon iş akışını gösterir:

1. Chrome, Playwright ve Browser-Use'un aynı tarayıcı oturumunu paylaşabilmesi için CDP etkin olarak başlar.
2. Bir Browser-Use ajanı, Airbnb'yi açmak, açılır pencereleri kapatmak ve Stockholm için arama yapmak gibi açık uçlu gezinme görevlerini yönetir.
3. Aktif sayfa, liste başlıkları, gecelik fiyatlar, değerlendirmeler ve URL'leri çıkarmak için yapılandırılmış bir Pydantic şemasıyla incelenir.
4. Python mantığı, çıkarılan listeleri karşılaştırır ve en ucuz sonucu vurgular.

Bu yöntem, Browser-Use'un iyi olduğu esnek, görsel tabanlı çıkarımı korurken gerektiğinde belirleyici tarayıcı kontrolü sağlar.

## Temel Çıkarımlar ve En İyi Uygulamalar

### Ne Zaman Ajan Kullanılır Ne Zaman Aktör

| Senaryo | Ajan Kullan | Aktör Kullan |
|----------|-----------|-----------|
| Dinamik düzenler | Evet, yapay zeka sayfa değişikliklerine uyum sağlayabilir | Hayır, kırılgan seçiciler zarar görebilir |
| Bilinen yapı | Hayır, ajan doğrudan kontrolden daha yavaştır | Evet, hızlı ve hassas |
| Öğe bulma | Evet, doğal dil çok iyi çalışır | Hayır, kesin seçiciler gereklidir |
| Zamanlama kontrolü | Hayır, daha az öngörülebilir | Evet, beklemeler ve denemeler üzerinde tam kontrol |
| Karmaşık iş akışları | Evet, beklenmedik UI durumlarını yönetir | Hayır, açık dallanma gerektirir |

### Browser-Use En İyi Uygulamalar

1. Keşif ve dinamik gezinme için ajanla başla.
2. Etkileşim öngörülebilir hale geldiğinde doğrudan sayfa kontrolüne geç.
3. Çıkarılan verinin doğrulanması ve tip güvenliği için yapılandırılmış çıktı modelleri kullan.
4. Görünür UI değişikliklerini tetikleyen işlemlerden sonra stratejik olarak gecikmeler ekle.
5. Hatalar daha kolay hata ayıklanabilmesi için tekrar ederken ekran görüntüleri yakala.
6. Web sitelerinin değişeceğini bekle ve açılır pencereler ve düzen kaymaları için yedek stratejiler tasarla.
7. Hem esneklik hem de kesinlik için ajan ve aktör kalıplarını birleştir.

### Tarayıcı Ajanları için Güvenlik Koruyucuları

Tarayıcı ajanları canlı web sitelerinde çalıştığından, yalnızca bilinen bir API'yi çağıran bir betikten daha sıkı sınırlandırmalara ihtiyaç duyarlar. Bir defter demosundan gerçek bir iş akışına geçmeden önce, ajanın neyi görebileceği, neye tıklayabileceği ve neyi gönderebileceği konusundaki kontrolleri tanımlayın.

1. **Gezinme ortamını sınırla.** Ajanı adanmış bir tarayıcı profili veya sandbox içinde çalıştır, ve görevin gerektirdiği alanlarla sınırla.
2. **Gözlem ile hareketi ayır.** Ajanın önce arama yapmasına, okumasına ve veri çıkarmasına izin ver; form gönderme, mesaj gönderme, seyahat rezervasyonu yapma, satın alma yapma, kayıtları silme veya hesap ayarlarını değiştirme gibi işlemler için açıkça onay adımı gerektir.
3. **Şifreleri ve izleri istemlerde tutma.** Model bağlamına parola, ödeme bilgileri, oturum çerezleri veya ham kişisel veri koyma. Doğrulama için kullanıcı müdahalesine izin ver ve hassas alanları günlüklerden çıkar.
4. **Sayfa içeriğini güvenilmez giriş olarak ele al.** Bir web sitesi, ajan için değil kullanıcı için yazılmış talimatlar içerebilir. Ajan, amacı değiştirmesini, veri açığa çıkarmasını, korumaları devre dışı bırakmasını veya alakasız siteleri ziyaret etmesini isteyen sayfa metinlerini görmezden gelmelidir.
5. **Riskli adımlar için belirleyici kontroller kullan.** Nihai adımı onaylamadan önce mevcut URL, sayfa başlığı, seçili öğe, fiyat, alıcı ve işlem özetini kodla doğrula.
6. **Bütçeleri ve durdurma koşullarını belirle.** Ajanın kullanabileceği işlem sayısını, yeniden denemeleri, sekmeleri ve dakikaları sınırla. Sayfa durumu belirsiz olduğunda tıklamaya devam etmek yerine dur.
7. **Her şeyi değil, faydalı kanıtları kaydet.** Hata olursa incelemeyi kolaylaştırmak için işlem özetlerini, zaman damgalarını, URL'leri, seçili öğe açıklamalarını ve ekran görüntüsü referanslarını tut; gereksiz hassas sayfa içeriğini depolama.

Airbnb örneğinde, güvenli varsayılan liste araması yapmak ve fiyatları çıkarmaktır. Giriş yapmak, ev sahibiyle iletişim kurmak veya rezervasyonu tamamlamak kullanıcı onaylı ayrı bir işlem olmalıdır.

### Gerçek Dünya Uygulamaları

- Seyahat rezervasyonu ve fiyat takibi
- E-ticaret fiyat karşılaştırması ve stok kontrolü
- Dinamik web sitelerinden yapılandırılmış çıkarım
- Görüş farkındalıklı UI testi ve doğrulama
- Web sitesi izleme ve uyarı
- Çok adımlı iş akışlarında akıllı form doldurma

## Gerçek Dünya Örneği: Microsoft Project Opal

Bu derste oluşturduğunuz ajan, bir **bilgisayar kullanım ajanı (CUA)**'nın küçük, yerel bir versiyonudur — bir kişinin yaptığı gibi bir tarayıcıyı yöneten bir program. Microsoft bu fikri Microsoft 365 Copilot içindeki **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** ile kurumsal düzeye getiriyor.

Project Opal ile, bir görevi tanımlarsınız ve ajan, **güvenli bir Windows 365 Cloud PC’de bilgisayar kullanımı yaparak**, kuruluşunuzun tarayıcı tabanlı uygulamalarında, sitelerinde ve verilerinde sizin adınıza çalışır. İşler **arka planda asenkron olarak yürütülür**, ve siz istediğiniz zaman çalışmayı yönlendirebilir veya kontrolü devralabilirsiniz. Örnek işler şunlardır:

- Güvenlik grubu üyelik isteklerini yönetmek
- Uyumluluk incelemeleri için denetim kanıtı toplamak ve doğrulamak
- BT vakalarını sınıflandırmak (bilet durumu güncellemek, sahip atamak, çoğaltmaları kapatmak)
- Excel verilerini finansal kapanış sunumuna derlemek

Opal, **üretim kalitesinde, güvenilir** bir bilgisayar kullanım ajanının nasıl göründüğüne dair faydalı bir referanstır — ve önceki derslerdeki kavramları güçlendirir:

| Bu kurstaki kavram | Project Opal nasıl uygular |
|------------------------|-----------------------------|
| **İnsan döngüde** (Ders 06) | Opal, giriş bilgileri, hassas veri veya belirsiz talimatlar için duraklar, parola veya form göndermez; görev ortasında *Kontrolü Al* ve *Kontrolü Geri Ver* seçenekleri vardır. |
| **Güvenilir ve güvenli ajanlar** (Dersler 06 & 18) | İzole Windows 365 Cloud PC'de çalışır, varsayılan olarak sadece tarayıcı erişimi vardır (diğer bilgisayar erişimi engellenir, Intune ile uygulanır), *sizin* kimliğinizi kullanır ve sadece yetkili olduğunuz verilere erişir, ve her işlemi denetim için kaydeder. |
| **Planlama & üstbiliş** (Dersler 07 & 09) | Opal önce iş için bir plan oluşturur, sonra her adımda kendi çıkarımını denetler ve şüpheli etkinlik fark ederse duraklar. |
| **Yeniden kullanılabilir yetenekler / araçlar** (Ders 04) | **Yetenekler** ile tekrarlanabilir işler için talimat yazabilirsiniz (bir `.md` dosyasından içe aktarılır veya Opal ile oluşturulur) ve bunları sohbetlerde yeniden kullanabilirsiniz. |

> **Mevcudiyet:** Project Opal şu anda Microsoft 365 Copilot aboneliği ile [Frontier erken erişim programı](https://adoption.microsoft.com/copilot/frontier-program/) kullanıcılarına açıktır ve yöneticiniz kurulumu tamamlamalıdır. Deneysel bir Frontier özelliği olduğundan, yetenekler zamanla değişebilir.

## Ek Kaynaklar

- [Project Opal ile başlayın (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright entegrasyon şablonu](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktör parametreleri ve içerik çıkarımı](https://docs.browser-use.com/customize/actor/all-parameters)
- [Ders Kurulumu](../00-course-setup/README.md)

## Önceki Ders

[Microsoft Agent Framework'u Keşfetmek](../14-microsoft-agent-framework/README.md)

## Sonraki Ders

[Ölçeklenebilir Ajanları Yayınlamak](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->