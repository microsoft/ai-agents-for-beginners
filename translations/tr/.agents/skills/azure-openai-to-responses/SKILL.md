---
name: azure-openai-to-responses
license: MIT
---
# Python Uygulamalarını Azure OpenAI Chat Completions'dan Responses API'ye Taşıma

> **YETKİLİ REHBER — TAM OLARAK UYUN**
>
> Bu beceri, Azure OpenAI Chat Completions kullanan Python kod tabanlarını
> birleşik Responses API'ye taşır. Bu talimatları tam olarak izleyin.
> Parametre eşlemeleri için doğaçlama yapmayın veya API şekilleri icat etmeyin.

---

## Tetikleyiciler

Kullanıcı istediğinde bu beceriyi etkinleştirin:
- Bir Python uygulamasını Azure OpenAI Chat Completions'dan Responses API'ye taşımak
- Python OpenAI SDK kullanımını Azure OpenAI'ye karşı en yeni API şekline yükseltmek
- Azure'da Responses gerektiren GPT-5 veya daha yeni modeller için Python kodunu hazırlamak
- `AzureOpenAI`/`AsyncAzureOpenAI`'den v1 uç noktası ile standart `OpenAI`/`AsyncOpenAI` istemcisine geçmek
- `AzureOpenAI` yapıcıları veya `api_version` ile ilgili kullanımdan kaldırma uyarılarını düzeltmek

---

## ⚠️ Model Uyumluluğu — ÖNCE KONTROL EDİN

> **Taşımadan önce, Azure OpenAI dağıtımınızın Responses API'yi desteklediğinden emin olun.**

### 1. Dağıtımınızı hızlı test edin (en hızlı)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Not**: Azure OpenAI'de `max_output_tokens`'ın **minimumu 16'dır**. 16'nın altındaki değerler 400 hatası döndürür. Hızlı testler için 50+ kullanın.

Eğer bu 404 dönerse, dağıtımın modeli henüz Responses'ı desteklemiyor demektir — aşağıdaki referansa bakın veya desteklenen bir modelle yeniden dağıtın.

### 2. Bölgenizde mevcut modelleri kontrol edin (önerilen)

Yerel bölgenizde Responses API desteği olan modelleri görmek için yerleşik model uyumluluk aracını çalıştırın:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Bu, Azure ARM'i canlı olarak sorgular ve bir uyumluluk matrisi gösterir — hangi modeller Responses, yapısal çıktı, araçlar vb destekler. Sonuçları daraltmak için `--filter gpt-5.1,gpt-5.2`; betikleme için `--json` kullanabilirsiniz.

### 3. Tam model destek referansı

- **Canlı sorgu**: `python migrate.py models` (yukarıya bakın — bölgeye özgü, sürekli güncel)
- **Kullanılabilirlik tablosu**: [Model özet tablosu ve bölge kullanılabilirliği](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Hızlı başlangıç & rehberlik**: **https://aka.ms/openai/start**

### ⚠️ Eski model sınırlamaları

> **UYARI**: Eski modeller ( `gpt-4.1`'den önce olanlar) tüm Responses API özelliklerini tam desteklemeyebilir.
>
> Eski modellerle bilinen sınırlamalar:
> - **`reasoning` parametresi**: Birçok mantık çıkarımı yapmayan modelde desteklenmez. Orijinal kodda zaten varsa `reasoning` parametresini taşıyın.
> - **`seed` parametresi**: Responses API'de hiç desteklenmez — tüm isteklerden kaldırın.
> - **`text.format` ile yapısal çıktı**: Eski modeller `strict: true` JSON şemalarını güvenilir şekilde zorlamayabilir.
> - **Araç yönetimi**: GPT-5+ modelleri araç çağrılarını iç mantık çıkarımı parçası olarak yönetir. Eski modeller Responses API'de çalışır ama bu derin entegrasyondan yoksundur.
> - **Sıcaklık kısıtlamaları**: `gpt-5`'e taşınırken sıcaklık parametresi atlanmalı veya `1` olarak ayarlanmalıdır. Eski modellerde böyle kısıtlama yoktur.

### O serisi mantık çıkarımı modelleri (o1, o3-mini, o3, o4-mini)

O serisi modellerin benzersiz parametre kısıtlamaları vardır. O serisi modelleri hedefleyen uygulamaları taşırken:

- **`temperature`**: `1` olmalı (veya atlanmalı). O serisi modeller başka değer kabul etmez.
- **`max_completion_tokens` → `max_output_tokens`**: Azure'a özgü `max_completion_tokens` kullanan uygulamalar `max_output_tokens`’a geçmeli. Yüksek değerler (4096+) ayarlayın çünkü çıkarım tokenları limite sayılır.
- **`reasoning_effort`**: Uygulama `reasoning_effort` (düşük/orta/yüksek) kullanıyorsa, bırakın — Responses API bu parametreyi o serisi modellerde destekler.
- **Akış davranışı**: O serisi modeller, mantık işlemi tamamlanana kadar çıktıyı tamponlayıp sonra metin delta olayları gönderebilir. Akış çalışır ancak ilk `response.output_text.delta` GPT modellerine göre daha geç gelebilir.
- **`top_p`**: O serisinde desteklenmez — varsa kaldırın.
- **Araç kullanımı**: O serisi modeller Responses API aracılığıyla araçları GPT modelleri gibi destekler; ancak araç çağrı yönetimi modelden modele değişir.

**Eylem — proaktif model uyarısı**: Taranma aşamasında uygulamanın hedeflediği modeli kontrol edin (dağıtım adları, ortam değişkenleri, yapılandırma). Model `gpt-4.1` öncesiyse (gpt-4.1+ değilse), kullanıcıya şu bilgileri proaktif olarak verin:
- Mevcut model üzerinde temel metin, sohbet, akış ve araçlar için taşıma çalışacaktır.
- Daha yeni modeller (`gpt-5.1`, `gpt-5.2`) daha iyi araç yönetimi, yapısal çıktı zorlaması, çıkarım ve çapraz bölge kullanılabilirliği sunar.
- Dağıtımlarını hazır olduğunda yükseltmeleri önerilir — taşımayı engellemez.

Model sürümüne göre taşıma yapılmasını engellemeyin veya reddetmeyin. Bu uyarı bilgilendirme amaçlıdır.

### GitHub Modelleri Responses API'yi desteklemez

> **GitHub Modelleri (`models.github.ai`, `models.inference.ai.azure.com`) Responses API'yi desteklemez.**

Eğer kod tabanında GitHub Modelleri kod yolu varsa (`base_url`'un `models.github.ai` veya `models.inference.ai.azure.com`'a işaret ettiği) **taşıma sırasında tamamen kaldırın**. Responses API Azure OpenAI, OpenAI veya uyumlu yerel uç nokta (örneğin Responses destekli Ollama) gerektirir.

Taranma sırasında eylem:
- GitHub Modelleri kod yollarını kaldırmak üzere işaretleyin.

---

## Framework Taşıma

Birçok uygulama OpenAI üzerinde daha üst düzey framework'ler kullanır. Bunları taşırken, sadece alttaki OpenAI çağrıları değil, framework'ün kendi API değişiklikleri de olur.

### Microsoft Agent Framework (MAF)

**Önce MAF sürümünüzü kontrol edin** — taşıma MAF 1.0.0+ mu yoksa öncesi beta/rc mi olduğuna bağlıdır.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **zaten Responses API kullanır** — taşıma gerekmez. Kod tabanı eski `OpenAIChatCompletionClient` (chat.completions.create kullanan) kullanıyorsa, bunu `OpenAIChatClient` ile değiştirin.

| Önce | Sonra |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Sürüm kontrolü için: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc sürümleri)

Pre-1.0.0 MAF'de, `OpenAIChatClient` Chat Completions kullanıyordu. `agent-framework-openai>=1.0.0`'a yükseltin; burada `OpenAIChatClient` varsayılan olarak Responses API kullanır.

Başka değişiklik gerekmez — `Agent` ve araç API'leri aynı kalır.

### LangChain (`langchain-openai`)

`ChatOpenAI()`'ye `use_responses_api=True` ekleyin. Ayrıca cevap erişimini `.content`'ten `.text`'e güncelleyin.

| Önce | Sonra |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Tam önce/sonra kod örnekleri için [cheat-sheet.md](./references/cheat-sheet.md) dosyasına bakın.

---

## Ön Uç Taşıma Rehberi

> **Responses API sunucu tarafı ilgilidir.** Python arka ucunuzu taşıyın; ön ucun HTTP sözleşmesi değişmemeli, ta ki arka uç ince bir geçiş katmanıysa — bu durumda çeviri katmanını kaldırmak için Responses istek şeklini benimseyin. Ön uç OpenAI'ye doğrudan istemci tarafı anahtarıyla çağrı yapıyorsa, bu çağrıları önce bir arka uca taşıyın.

### `@microsoft/ai-chat-protocol` kullanımdan kaldırıldı

`@microsoft/ai-chat-protocol` npm paketi kullanımdan kaldırıldı ve yerine [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) kullanılmalıdır. Eğer bir ön uçta karşılaşırsanız:

1. CDN script etiketini değiştirin:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` örneklemesini kaldırın (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. `client.getStreamedCompletion(messages)`'ı doğrudan arka uç akış uç noktasına `fetch()` çağrısı ile değiştirin.
4. `for await (const response of result)` yerine `for await (const chunk of readNDJSONStream(response.body))` kullanın.
5. Özellik erişimini `response.delta.content` / `response.error`'den `chunk.delta.content` / `chunk.error`'e güncelleyin.

---

## Hedefler

- Azure OpenAI'ye karşı Chat Completions veya eski Completions kullanan tüm Python çağrı noktalarını listeleyin.
- Python kod tabanı için bir taşıma planı ve sıralaması önerin.
- Güvenli, minimum değişikliklerle Responses API'ye geçiş yapın.
- Çağrıcıları Responses çıktı şemasını tüketecek şekilde güncelleyin; geri uyumluluk sarmalayıcıları yok.
- Testler/denetimler çalıştırın; taşımadan kaynaklanan önemsiz hataları düzeltin.
- Küçük, incelemeye uygun değişiklik setleri hazırlayın ve dif’lerle birlikte son bir özet sağlayın (commit etmeyin).

---

## Koruyucu Önlemler

- Yalnızca git çalışma alanı içindeki dosyaları değiştirin. Hiçbir zaman dışına yazmayın.
- Geri uyumluluk sarmalayıcılarını korumayın; kodu yeni API şekline taşıyın.
- Mezar taşı/geçiş yorumları veya yedek dosyalar bırakmayın.
- Daha önce kullanılıyorsa akış özelliklerini koruyun; aksi halde akışsız kullanın.
- Onay modundaysanız, komutlar veya ağ çağrıları çalıştırmadan önce onay isteyin.
- `git add`/`git commit`/`git push` çalıştırmayın; sadece çalışma ağacı düzenlemeleri oluşturun.

---

## Adım 0: Azure OpenAI İstemci Taşıması (Önkoşul)

Eğer kod tabanı `AzureOpenAI` veya `AsyncAzureOpenAI` yapıcıları kullanıyorsa, önce standart `OpenAI` / `AsyncOpenAI` yapıcılarına geçin. Azure’a özgü yapıcılar `openai>=1.108.1` sürümünde kullanımdan kaldırılmıştır.

### Neden v1 API yolu?

Yeni `/openai/v1` uç noktası `AzureOpenAI()` yerine standart `OpenAI()` istemcisini kullanır, `api_version` parametresi gerekmez ve OpenAI ile Azure OpenAI arasında aynıdır. Aynı istemci kodu geleceğe hazırlıklıdır — sürüm yönetimi gerekmez.

### Önemli değişiklikler

| Önce | Sonra |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Tamamen kaldır |

### Temizlik kontrol listesi

- İstemci yapımından `api_version` argümanını kaldırın.
- `.env`, uygulama ayarları ve Bicep/altyapı dosyalarından `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` ortam değişkenlerini kaldırın.
- `.env`, uygulama ayarları, Bicep/altyapı ve test düzeneklerinde `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` olarak yeniden adlandırın (standart Azure Identity SDK konvansiyonu).
- `requirements.txt` veya `pyproject.toml`’de `openai>=1.108.1` sürümünü garantileyin.

### Ortam değişkeni taşıması

| Eski ortam değişkeni | İşlem | Notlar |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Kaldır** | v1 uç nokta ile `api_version` gerekmez |
| `AZURE_OPENAI_API_VERSION` | **Kaldır** | Yukarıdaki ile aynı |
| `AZURE_OPENAI_CLIENT_ID` | **Yeniden adlandır** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` için standart Azure Identity SDK konvansiyonu |
| `AZURE_OPENAI_ENDPOINT` | **Tut** | Hala `base_url` oluşturmak için gerekli |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Tut** | `responses.create` içinde `model` parametresi olarak kullanılır |
| `AZURE_OPENAI_API_KEY` | **Tut** | Anahtara dayalı kimlik doğrulama için `api_key` olarak kullanılır |

İstemci kurulum kodu örnekleri (senkron, asenkron, EntraID, API anahtarı, çok kiracılı) için [cheat-sheet.md](./references/cheat-sheet.md) dosyasına bakın.

---

## Adım 1: Eski Çağrı Noktalarını Tespit Et

Taşınması gereken tüm çağrı noktalarını bulmak için [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) betiğini çalıştırın:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Ya da bu aramaları elle yapın — her eşleşme taşınacak hedeftir:

```bash
# Eski API çağrıları (yeniden yazılmalı)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Kullanımdan kaldırılmış Azure istemci yapıcıları (değiştirilmeli)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Yanıt şekli erişim kalıpları (güncellenmeli)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Araç tanımları eski iç içe formatta (düzleştirilmeli)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Araç sonuçları eski formatta (function_call_output'a dönüştürülmeli)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Kullanımdan kaldırılmış parametreler (kaldırılmalı veya yeniden adlandırılmalı)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens olarak yeniden adlandır
rg "['\"]seed['\"]"      # remove entirely

# Kullanımdan kaldırılmış ortam değişkenleri (temizlenmeli)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID olmalı

# GitHub Modelleri uç noktaları (kaldırılmalı — Yanıtlar API desteklenmiyor)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Çerçeve düzeyi eski kalıplar (güncellenmeli)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient ile değiştir
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True gerektirir

# Test altyapısı (güncellenmeli)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# İçerik filtre hatası gövde erişimi (güncellenmeli — yapı değişti)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # eski tekil form — şimdi içerik_filtre_sonuçları (çoğul) içerik_filtreler dizisi içinde

# Chat Tamamlama uç noktasına ham HTTP çağrıları (URL güncellenmeli)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristikler (tespit ve yeniden yazma)

- **Chat Completions istemcisi**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure istemci yapıcıları**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Araçlar**: fonksiyon çağrısı araç tanımlarını iç içe formatından (`{"type": "function", "function": {"name": ...}}`) düz Responses formatına (`{"type": "function", "name": ...}`) dönüştürün; `tool_choice` kullanın; araç sonuçlarını `{"type": "function_call_output", "call_id": ..., "output": ...}` öğeleri olarak döndürün (`{"role": "tool", ...}` değil).
- **Araç tur dönüşümleri**: model fonksiyon çağrıları döndürdüğünde, `response.output` öğelerini görüşmeye ekleyin (manuel `{"role": "assistant", "tool_calls": [...]}` sözlüğü değil), sonra her sonuç için `function_call_output` öğelerini ekleyin.
- **Az sayıda örnek araç kullanımı**: görüşme sert kodlanmış araç çağrısı örnekleri içeriyorsa, bunları `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` öğelerine dönüştürün. Kimlikler `fc_` ile başlamalıdır.
- **`pydantic_function_tool()`**: bu yardımcı eski iç içe formatı üretmeye devam eder ve `responses.create()` ile **uyumlu değildir**. Elle araç tanımları veya düzleştirme sarmalayıcısı ile değiştirin.
- **Çok turlu**: görüşme geçmişini uygulamada tutun; önceki turları `input` öğeleri ile geçin.
- **Biçimlendirme**: Chat'in üst düzey `response_format` öğesini Responses'da `text.format` ile değiştirin. Kanonik şekil: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **İçerik öğeleri**: Chat `content[].type: "text"` öğesini, kullanıcı/sistem turları için Responses `content[].type: "input_text"` ile değiştirin.
- **Resim içerik öğeleri**: Chat `content[].type: "image_url"` öğesini Responses `content[].type: "input_image"` ile değiştirin. `image_url` alanı iç içe obje `{"url": "..."}` yerine düz bir string olarak değişir. Öncesi/sonrası örnekler için hile sayfasına bakınız.
- **Akıl yürütme çabası**: **sadece orijinal kodda zaten mevcutsa `reasoning` öğesini taşıyın**.
- **İçerik filtresi hata işleme**: hata gövdesi yapısı değişti. Chat Tamamlama `error.body["innererror"]["content_filter_result"]` (tekil) kullanırdı; Responses API `error.body["content_filters"][0]["content_filter_results"]` (çoğul, dizi içinde) kullanır. `innererror` erişen kod `KeyError` atar. Yeni yolu kullanacak şekilde yeniden yazın.
- **Ham HTTP çağrıları**: uygulama Azure OpenAI REST API'yi doğrudan `/openai/deployments/{name}/chat/completions?api-version=...` yoluyla çağırıyorsa, bunu `/openai/v1/responses` yoluna yeniden yazın. İstek gövdesi değişir: `messages` → `input`, `max_output_tokens` ve `store: false` eklenir, `api-version` sorgu parametresi kaldırılır. Yanıt gövdesi değişir: `choices[0].message.content` → `output[0].content[0].text` (not: `output_text` SDK kolaylığıdır, ham REST JSON'da yoktur).

---

## Adım 2: Geçişi Uygula

### Geçiş notları (Chat Tamamlama → Responses)

- **Neden geçiş yapılmalı**: Responses metin, araçlar ve akış için birleşik API'dir; Chat Tamamlama eski bir yöntemdir. GPT-5 ile en iyi performans için Responses zorunludur.
- **HTTP**: Azure uç noktası `/openai/deployments/{name}/chat/completions`'den `/openai/v1/responses`'e geçer.
- **Alanlar**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` değişmeden kalır.
- **Biçimlendirme**: `response_format` → uygun bir nesne ile `text.format`.
- **İçerik öğeleri**: Sistem/kullanıcı turları için Chat `content[].type: "text"` öğesi Responses `content[].type: "input_text"` ile değiştirildi.
- **Resim içerik öğeleri**: Chat `content[].type: "image_url"` öğesi Responses `content[].type: "input_image"` ile değiştirildi. `image_url` alanı `{"image_url": {"url": "..."}}` iç içe yapısından `{"image_url": "..."}` düz dizeye (HTTPS URL'si ya da `data:image/...;base64,...` veri URI'si) dönüştürüldü.

### Parametre eşleştirme referansı

| Chat Tamamlama | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (öğeler dizisi) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (nesne) |
| `temperature` | `temperature` (değişmedi) |
| `stop` | `stop` (değişmedi) |
| `frequency_penalty` | `frequency_penalty` (değişmedi) |
| `presence_penalty` | `presence_penalty` (değişmedi) |
| `tools` / fonksiyon çağrısı | `tools` (değişmedi) |
| `seed` | **Kaldır** (desteklenmiyor) |
| `store` | `store` (`false` olarak ayarlanır) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (düz string) |

Tam öncesi/sonrası kod örnekleri için bkz. [cheat-sheet.md](./references/cheat-sheet.md).

Test altyapısı geçişi (mocklar, anlık görüntüler, doğrulamalar) için bkz. [test-migration.md](./references/test-migration.md).

Hata ayıklama ve sık yaşanan sorunlar için bkz. [troubleshooting.md](./references/troubleshooting.md).

---

## Veri Saklama ve Durum

- Tüm Responses isteklerinde `store: false` ayarlayın.
- Önceki mesaj kimliklerine veya sunucu tarafında saklanan bağlama güvenmeyin; durumu istemci tarafında yönetin ve meta veriyi en aza indirin.

---

## Kabul Kriterleri

### Kod seviyesi kontroller (tümü geçmeli)

- [ ] Geçiş yapılan dosyalarda `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` aramasında sıfır eşleşme.
- [ ] Tüm yapıcılar `OpenAI`/`AsyncOpenAI` v1 uç noktası ile kullanılmalı, `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` sıfır eşleşmeli.
- [ ] GitHub Modelleri kod yolları kaldırıldı, `rg "models\.github\.ai|models\.inference\.ai\.azure"` sıfır eşleşmeli.
- [ ] MAF 1.0.0+ kod `OpenAIChatClient` kullanıyor, `OpenAIChatCompletionClient` için `rg "OpenAIChatCompletionClient"` sıfır eşleşmeli. 1.0.0 öncesi için `agent-framework-openai>=1.0.0` yükseltmesi yapılmalı.
- [ ] Tüm `ChatOpenAI(...)` çağrıları `use_responses_api=True` içeriyor.
- [ ] Yanıt erişimi tamamen `resp.output_text` veya Responses çıktı şeması ile, `rg "choices\[0\]"` sıfır eşleşmeli.
- [ ] Üst seviyede `response_format` yok; tüm yapılı çıktı `text={"format": {...}}` kullanmakta.
- [ ] `requirements.txt` veya `pyproject.toml` dosyalarında `openai>=1.108.1` ve `azure-identity` bulunuyor; bağımlılıklar yeniden yüklendi.
- [ ] Her `responses.create` çağrısında `store=False` ayarlandı.
- [ ] İstemci yapımında `api_version` yok; `AZURE_OPENAI_API_VERSION` ortam dosyalarından ve altyapıdan kaldırıldı.

### Test altyapısı kontrolleri (tümü geçmeli)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions"` testlerde sıfır eşleşme.
- [ ] `rg "_azure_ad_token_provider" tests/` sıfır eşleşmeli; doğrulamalar `isinstance(client, AsyncOpenAI)` veya `base_url` kontrolü yapacak şekilde güncellendi.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` sıfır eşleşmeli; Azure özel filtre mockları kaldırıldı.
- [ ] Mock donanımları `kwargs.get("input")` kullanıyor, `kwargs.get("messages")` değil.
- [ ] Anlık görüntü / altın dosyalar Responses akış şekline uygun şekilde güncellendi (örneğin, `choices[0]`, `function_call`, `logprobs` yok).
- [ ] Tüm test güncellemelerinden sonra `pytest` sıfır hata ile geçiyor.

### Davranışsal kontroller (manuel veya test düzeneği ile doğrula)

- [ ] **Temel tamamlama**: akışsız `responses.create` boş olmayan `output_text` döndürüyor.
- [ ] **Akış eşitliği**: orijinal kod akış kullanıyorsa, geçiş yapılan kod da akış sağlıyor ve `response.output_text.delta` etkinliklerini boş olmayan deltalarla veriyor.
- [ ] **Yapılı çıktı**: `text.format` ile `json_schema` kullanılıyorsa, `json.loads(resp.output_text)` başarılı oluyor ve şemaya uyuyor.
- [ ] **Araç çağrı döngüsü**: araçlar kullanılıyorsa model araç çağrıları yapıyor, uygulama bunları yürütüyor ve takip isteği son `output_text` döndürüyor (sonsuz döngü yok).
- [ ] **Eşzamanlılık eşitliği**: `AsyncAzureOpenAI` kullanıldıysa `AsyncOpenAI` karşılığı `await` ile çalışıyor.
- [ ] **Hata oranı**: geçiş öncesi temele kıyasla yeni 400/401/404 hatası yok.

### Teslimatlar

- Özet dosya düzenlemelerini, eski çağrı noktalarının geçiş öncesi/sonrası sayısını ve sonraki adımları içerir.
- Değişiklikler çalıştırılabilir durumdaki düzenlemeler (commit değil).

---

## SDK Sürüm Gereksinimleri

| Paket | Minimum Sürüm |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | En güncel (EntraID kimlik doğrulama için) |

---

## Referanslar

- [Hile Sayfası — tüm kod parçacıkları](./references/cheat-sheet.md)
- [Test Geçişi — mocklar, anlık görüntüler, doğrulamalar](./references/test-migration.md)
- [Hata Ayıklama — hatalar, risk tablosu, sık sorunlar](./references/troubleshooting.md)
- [detect_legacy.py — otomatik tarayıcı](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Başlangıç Kiti](https://aka.ms/openai/start)
- [Azure OpenAI Responses API belgeleri](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API sürüm yaşam döngüsü](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API referansı](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->