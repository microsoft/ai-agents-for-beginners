# Ajan Duman Testleri

Bu klasör, kursta oluşturduğunuz ajanlar için **duman testi katalogları** içerir.
Bir duman testi, **Microsoft Foundry barındırılan dağıtılmış ajanın** erişilebilir, yanıt verir durumda
ve en temel istem beklentilerini takip ettiğini hızlı ve ucuz bir şekilde kontrol eden bir testtir.
Bu, [Ders 10](../10-ai-agents-production/README.md) ve
[Ders 16](../16-deploying-scalable-agents/README.md) öğrenilen tam değerlendirme sürecinin yerine geçmeyen ilk kapıdır.


Kataloglar, [AI Duman Testi](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action tarafından [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
iş akışı aracılığıyla tüketilir.

## Nasıl çalıştırılır

1. **Ders ajanınını** Microsoft Foundry'de barındırılan ajana dağıtın (dağıtım iş akışı için
   Ders 16'ya bakınız). **Ajan adını** ve
   **Foundry proje uç noktanızı** not edin.
2. Bu depo gizli anahtarlarını ekleyin (Ayarlar → Gizli anahtarlar ve değişkenler → Eylemler):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Federasyon kimliği,
   **Foundry proje kapsamı** altında **Azure AI Kullanıcısı** rolüne ihtiyaç duyar.
3. **Eylemler** sekmesinden, **Duman testi barındırılan ajanlar** iş akışını çalıştırın ve
   ders için `tests_file` seçin, ardından eşleşen `agent_name` ve
   `project_endpoint` sağlayın.

## Katalog → ders → ajan adı

| Katalog | Ders | Ajani olarak dağıt |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Yapay Zeka Ajanlarına Giriş](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Araç Kullanımı](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Ajanik RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Ölçeklenebilir Ajanların Dağıtımı](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Hangi derslerde duman testleri var?

Duman testleri, **bir ajan dağıttığınız** ve metin yanıtlarının bilinen içerikle karşılaştırılabildiği
derslere uygulanır. Kavramsal olan, yalnızca yerel çalışan,
veya kararsız yaratıcı çıktı üreten dersler kasıtlı olarak hariç tutulmuştur:

- **Ders 17 (Yerel AI Ajanları Oluşturma)** tamamen çalışma istasyonunuzda Foundry Local ile çalışır
  ve Foundry Yanıtlar uç noktası açmaz, bu nedenle bu eylem uygulanmaz.
  Yerel olarak defteri çalıştırarak doğrulayın.
- Tasarım deseni ve teori dersleri (02, 03, 06, 07, 09, 12) tek bir
  dağıtılabilir ajan sağlamadığından duman testi yoktur.

## Katalog şeması (hızlı referans)

Her katalog, üst düzeyinde bir `tests` dizisi içeren bir JSON belgesidir. Her giriş
bir istem gönderir ve yanıt üzerinde doğrulama yapar:

| Alan | Anlamı |
|-------|---------|
| `id` | Günlükte yazdırılan benzersiz adım tanımlayıcısı. |
| `description` | İnsan tarafından okunabilir amaç. |
| `prompt` | Ajan'a gönderilen mesaj. |
| `assertions.status` | Beklenen HTTP durumu (varsayılan 200). |
| `assertions.contains_any` | Yanıt bu alt dizelerden herhangi birini içeriyorsa geçer. |
| `assertions.contains_all` | Yanıt her alt dizeyi içeriyorsa geçer. |
| `assertions.contains_none` | Yanıt bu alt dizelerin hiçbirini içermezse geçer. |
| `save_response_id_as` | Daha sonra çok adımlı bir adım için yanıt kimliğini sakla. |
| `use_previous_response_id` | Bu turu saklanan bir yanıt kimliğine zincirle. |

Doğrulamalar, büyük/küçük harf duyarsız alt dize kontrolleridir. Tam şema için,
[eylem dokümantasyonuna](https://github.com/marketplace/actions/ai-smoke-test) bakın,
Foundry tarafından yönetilen konuşma kaynakları dahil.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->