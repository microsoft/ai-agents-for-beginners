---
name: deploying-scalable-agents
license: MIT
---
# Microsoft Foundry ile Ölçeklenebilir Ajanlar Dağıtmak

> [Ders 16 – Ölçeklenebilir Ajanlar Dağıtmak](../../../16-deploying-scalable-agents/README.md) için yardımcı beceri.
> Bir öğrenenin bir ajanı prototip aşamasından ölçeklenebilir, gözlemlenebilir
> üretim dağıtımına taşırken yardım etmek için kullanın. Her öneriyi ders içeriği ve
> çalıştırılabilir not defteri ile destekleyin; Foundry API'lerini uydurmayın.

## Tetikleyiciler

Bir öğrenen şu durumlarda bu beceriyi aktif edin:
- Bir ajanı Microsoft Foundry'ye **barındırılan ajan** olarak dağıtmak ve versiyonlamalı/gözlemlenebilir hale getirmek.
- **istemci barındırmalı, barındırılan ajan ve ajan-iş akışı** dağıtım desenleri arasında seçim yapmak.
- Gecikme ve maliyeti kontrol etmek için **model yönlendirmesi**, **yanıt önbellekleme** veya **sınırlı eşzamanlılık** eklemek.
- Kötü bir ajan sürümünün piyasaya sürülmesini önlemek için bir **değerlendirme kapısı** eklemek.
- Yüksek riskli işlemler için bir **insan-döngüde onay** adımı eklemek.
- Üretim gözlemlenebilirliği için bir ajana **OpenTelemetry** izleme aracı eklemek.
- Hızlı bir dağıtım sonrası kontrol için dağıtılmış ajanı **duman testi** yapmak.

## Temel zihinsel model

Bir üretim ajanı büyük ölçüde modelin *etrafındaki* operasyonel iskelet (%80 civarıdır),
modelin kendisi değildir. Her öneriyi aşağıdaki konulardan birine eşleyin:

| Konu | Prototip → Üretim |
|---------|------------------------|
| Barındırma | not defteri → versiyonlanmış barındırılan servis |
| Kimlik | sizin `az login` → yönetilen kimlik + kapsamlı RBAC |
| Durum | bellek içi → dışsal iş parçacığı/bellek deposu |
| Hata | hata izleme → tekrar denemeler, yedekler, uyarılar |
| Maliyet | "birkaç kuruş" → takip edilen, yönlendirilen, önbelleğe alınan, bütçelenen |
| Kalite | gözle görünür → otomatik değerlendirme kapısı |
| Güven | sizin onayınız → politika + insan-döngüde |

## Dağıtım desenleri (birini seçin veya birleştirin)

1. **İstemci barındırmalı** — akıl yürütme döngüsü sizin işlemde çalışır. Maksimum kontrol; ölçeklendirme/durum size aittir.
2. **Barındırılan ajan (Foundry Ajan Servisi)** — Foundry döngüyü barındırır, iş parçacıklarını depolar, RBAC/içerik güvenliğini uygular, ajanı portalda gösterir. Daha az kontrol, çok daha az operasyonel yüzey.
3. **Ajan iş akışı** — çoklu ajanlar/araçlar dallanma, onay düğümleri ve kalıcı kontrol noktaları ile bir grafikte birleşir.

## Yaşam döngüsü (ajanın sevk edildiği döngü)

`oluştur → versiyonla → değerlendir (kapı) → barındırılan dağıt → çevrimiçi gözlemle → hataları topla → tekrarla`.
**Çevrimdışı değerlendirme bir kapıdır, sonradan yapılan bir işlem değil** — bir sürüm
eşik değerini geçmediği sürece piyasaya sürülmez. Çevrimiçi gözlemlenebilirlik gerçek
hataları çevrimdışı test setine geri besler.

## Ölçeklendirme ve maliyet kaldıracı (öncelik sırasına göre)

1. **Modeli doğru boyutlandırın** — değerlendirme kapısından geçen en küçük modeli kullanın.
2. **Karmaşıklığa göre yönlendirin** — basit istekler için küçük/hızlı model, gerçek akıl yürütme için büyük model (kendin yap sınıflandırıcı veya Foundry Model Yönlendirici).
3. **Önbellek kullanın** — benzer tekrar eden istekleri model çağrısı yapmadan sunun.
4. **Durumsuz tasarım + sınırlı eşzamanlılık** — durumu dışsal yapın; başarısızlığa karşı denemeyi artırarak tekrarlayın.

## Yeniden üretilmesi gereken önemli desenler

Öğreneni şunlara yönlendirin, not defterinden
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **İstek işleyici**: önbellek → karmaşıklığa göre yönlendirme → izleme aralığı → çalıştır → önbellek.
- **Değerlendirme kapısı**: çevrimdışı test setini puanla; `pass_rate >= threshold` döndür ve sadece doğruysa dağıt.
- **İnsan onayı**: büyük iadeler gibi işlemler için `@tool(approval_mode="always_require")`.
- **İzleme**: her isteği `tracer.start_as_current_span(...)` ile sar ve `routed.model`, `customer.id` gibi öznitelikleri ayarla.

## Dağıtılmış ajanı duman testi yapmak

Dağıtımdan sonra, uç noktanın gerçekten yanıt verdiğini doğrulayın (yeşil dağıtım sessiz olabilir).
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
eylemini [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
içinden ve [`tests/`](../../../tests/README.md) kataloğuyla kullanın. Çalıştırıcı her
istemi `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
adresine gönderir ve yanıt metnini denetler. Kimliğin Foundry proje kapsamındaki **Azure AI Kullanıcısı** rolüne ihtiyacı vardır;
jeton hedef kitlesi `https://ai.azure.com/` olmalıdır.

Kapıları katmanlayın: **duman testi** (erişilebilir/yanıt veren, her dağıtım) → **çevrimdışı değerlendirme**
(dağıtıma uygun, terfi öncesi) → **çevrimiçi değerlendirme** (gerçek ortamda nasıl işliyor, sürekli).


## Kurumsal kontroller

- **RBAC**: her barındırılan ajana en az ayrıcalıkla yönetilen bir kimlik verin.
- **Üretimde MCP**: her MCP sunucusunu güvensiz sınır olarak değerlendirin — sürümü sabitleyin, kimliğini sınırlayın, çıktıları doğrulayın, oran sınırlaması yapın, asla sırları açığa çıkarmayın.

## Asistan için güvenlik önlemleri

- Ders boyunca kullanılan kanonik `FoundryChatClient(...)` + `provider.as_agent(...)` desenini tercih edin.
- Doğrulamamış canlı Azure sonuçları vaat etmeyin; dağıtımı doğrulamak için duman testi iş akışını önerin.
- Değerlendirme ve maliyet tavsiyelerini birbirine bağlayın: değerlendirme kalite tabanını belirler, yönlendirme/önbellekleme maliyeti bu tabana yakın tutar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->