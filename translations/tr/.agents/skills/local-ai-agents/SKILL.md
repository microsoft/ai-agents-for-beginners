---
name: local-ai-agents
license: MIT
---
# Foundry Local ve Qwen ile Yerel AI Ajanları Oluşturma

> [Ders 17 – Yerel AI Ajanları Oluşturma](../../../17-creating-local-ai-agents/README.md) için yardımcı beceri.
> Bir öğrenicinin tamamen kendi makinesinde düşünen, araçları çağıran ve
> dokümantasyon araması yapan bir ajan oluşturmasına yardımcı olmak için kullanın — bulut çıkarımı olmadan. Her öneriyi ders içeriği ve çalıştırılabilir not defteri ile temel alın.




- Gizlilik, maliyet veya çevrimdışı nedenlerle ajanı **tamamen cihazda** çalıştırmak.
- **Foundry Local** ile yerel bir modeli sunmak ve OpenAI uyumlu uç nokta üzerinden bağlanmak.
- Güvenilir yerel araç çağrıları için **Qwen fonksiyon çağırma** modelini kullanmak.
- **Yerel RAG** (Chroma) veya **yerel MCP sunucusu** eklemek.
- **Hibrit** yerel/bulut yönlendirme stratejisi tasarlamak.




strateji: **SLM'yi düzenleyici olarak bırakın ve ağır işleri araçlara yaptırın.** Modelin kod tabanını *bilmesi* gerekmez — sadece `read_file` ve `search_docs`’i ne zaman çağıracağını bilmesi gerekir. Bu, bir SLM'nin güçlü yanına oynar (araç seçimi gibi sınırlı kararlar) ve zayıf yanından (geniş bilgi, uzun çok adımlı mantık) uzaklaşır.

## Neden bu belirli parçalar

- **Foundry Local**, **OpenAI uyumlu HTTP uç noktası** açar, böylece bulut ajan kodu yalnızca `base_url` değiştirerek (ve yerel geçici API anahtarı kullanarak) aktarılır. Ayrıca makine için en iyi derlemeyi (CPU/GPU/NPU) otomatik seçer.
- **Qwen** modelleri fonksiyon çağırmaya yönelik eğitilmiş olup tutarlı ve düzgün biçimde araç çağrıları yapar — bu, yerel *sohbet* modelini yerel *ajan* haline getirir.

- **MCP** bir taşıma protokolüdür, bulut hizmeti değil: bir MCP sunucusu `stdio` üzerinden yerelde çalışabilir.

## Kurulum gereklilikleri

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # local placeholder
```





Öğrenciyi şu not defterine yönlendirin
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Kutu içi araçlar**: her dosya aracı yol çözümleyip tek bir proje kökünün dışındakileri reddeder — yerelde bile bir araç kullanıcının izinleriyle çalışır.

- **Yerel RAG**: belgeleri bir Chroma koleksiyonuna ekle; `search_docs` en iyi k parçayı döndürür.
- **Yerel MCP**: yerel bir sunucuya `stdio` üzerinden bağlan; bunu bir proje dizinine sınırla ve çıktıları doğrula.

## Hibrit yönlendirme (yerel modellerden biri olarak)

| Durum | Nerede çalışır |
|-----------|---------------|

| Basit, sınırlı görev | Yerel SLM (ucuz, hızlı) |

| Bulut kesintisi | Yerel SLM (kibar düşüş) |

Bu, Ders 16’dan model yönlendirme fikrini yansıtır, çalışma istasyonu bir rotadır. Ajanın tamamen başarısız olmak yerine kalitenin düşmesine izin veren yerel geri dönüşlü tasarımları tercih edin.

## Asistan için koruma önlemleri


- Öğrenicinin açıkça gizlilik/çevrimdışı hedefi varsa kod veya veri buluta göndermeyin — tüm hattı yerelde tutun.
- SLM kalitesi için gerçekçi beklentiler belirleyin; modelin ezber bilgisinden çok araçlara ve RAG'a dayanın.
- Ders 17’nin **Foundry Responses uç noktası yoktur**, dolayısıyla bulut duman testi geçerli değildir — doğrulamayı not defterini yerelde çalıştırarak yapın.

## Asistan için koruyucu kurallar

- Her dosya/araç işlemini izole edilmiş bir proje dizini içinde tutun.
- Öğrencinin belirtilen hedefi gizlilik/çevrimdışı ise kodu veya veriyi buluta göndermeyin — tüm süreci yerel tutun.
- SLM kalitesi için gerçekçi beklentiler belirleyin; modele ezberletilmiş bilgiden çok araçlara ve RAG'a güvenin.
- Ders 17'nin **hiçbir** Foundry Yanıtları uç noktası olmadığını unutmayın, bu yüzden bulut duman testi işlemi geçerli değil — doğrulamayı not defterini yerel çalıştırarak yapın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->