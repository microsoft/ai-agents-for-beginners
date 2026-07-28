# Sorun Giderme, Risk Tablosu ve Tuzaklar

## 400 Serisi Hataların Sorun Giderilmesi

| Hata | Düzeltme |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Araç tanımı eski Chat Completions iç içe yapısını kullanıyor | `{"type": "function", "function": {"name": ...}}` biçimini `{"type": "function", "name": ..., "parameters": ...}` olarak düzeltilmelidir — name, description, parameters en üst seviyeye çıkarılmalı |
| `unknown_parameter: input[N].tool_calls` | Çok aşamalı araç sonuçları eski Chat Completions formatını kullanıyor | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` yerine `response.output` öğeleri ve `{"type": "function_call_output", "call_id": ..., "output": ...}` kullanılmalı |
| `invalid_function_parameters: 'required' is required` | `strict: true` ayarlı araç için `required` dizisi eksik | `strict: true` ise, tüm özellikler `required` içinde listelenmeli ve `additionalProperties: false` ayarlanmalı |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` ayarlı araç için `additionalProperties: false` eksik | Parametreler nesnesine `"additionalProperties": false` ekleyin |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Few-shot function_call ID'si yanlış önek kullanıyor | Fonksiyon çağrısı ID'leri `fc_` ile başlamalı (örn. `fc_example1`), `call_` ile değil |
| `missing_required_parameter: text.format.name` | Format sözlüğüne `"name"` anahtarı ekleyin (örn. `"name": "Output"`) |
| `invalid_type: text.format` | `text.format` anahtarının string değil, `type`, `name`, `strict`, `schema` anahtarlarını içeren bir sözlük olduğundan emin olun |
| `invalid input content type` | Chat `text` yerine `input_text`/`output_text` içerik türleri kullanın |
| `invalid input content type` (resim) | Resim içeriği hâlâ `"type": "image_url"` kullanıyor | `"type": "input_image"` olarak değiştirin |
| `Expected object, got string` on `image_url` | `image_url` hâlâ iç içe nesne olarak `{"url": "..."}` | Düz string olarak `"image_url": "https://..."` veya `"image_url": "data:image/...;base64,..."` biçimine getirin |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI minimum değeri **16**dır. Testlerde 50+ ve üretim için 1000+ kullanın. |
| `429 Too Many Requests` streaming sırasında | Rate limit uygulandı. Streaming'i `try/except` içinde sarın, hatayı frontend'e JSON olarak iletin, geri çekilme/yeniden deneme uygulayın. |
| `KeyError: 'innererror'` içerik filtre hata mesajında | Responses API'da içerik filtre hata gövdesi yapısı değişti | Chat Completions `error.body["innererror"]["content_filter_result"]` kullanıyordu; Responses API `error.body["content_filters"][0]["content_filter_results"]` (çoğul, dizi içinde) kullanır. Tüm `innererror` erişimleri yeniden yazılmalı. |

---

## Geçiş Risk Tablosu

| Belirti | Muhtemel Hata | Düzeltme |
|---------|---------------|-----|
| Boş `output_text` / kesilmiş yanıt | `max_output_tokens` değerinin düşük olması (akıl yürütme modelleri için) | `max_output_tokens=1000` veya üzeri ayarlayın — akıl yürütme tokenları limite dahil edilir |
| `400 invalid_type: text.format` | Yanlışlıkla `text.format` sözlüğü yerine `response_format` stringi verilmiş | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` kullanın |
| `/openai/v1/responses` için `404 Not Found` hatası | Yanlış `base_url` — `/openai/v1/` son eki eksik | `base_url=f"{endpoint}/openai/v1/"` olarak (sonunda eğik çizgi ile) ayarlayın |
| `401 Unauthorized` `OpenAI()`'ye geçtikten sonra | `api_key` ayarlanmadı veya token sağlayıcı yanlış geçirildi | EntraID için: `api_key=token_provider` (çağrılabilir). API anahtarı için: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model `deployment not found` döndürüyor | `model` parametresi Azure dağıtım adınızla eşleşmiyor | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` kullanın — bu dağıtım adı, model adı değil |
| `json.loads(resp.output_text)` `JSONDecodeError` hatası veriyor | Şema uygulanmamış veya model katı JSON desteklemiyor | Şemada `"strict": True` olduğundan emin olun ve modelin yapılandırılmış çıktıyı desteklediğini doğrulayın |
| Streaming `delta` eventi vermiyor | Yanlış olay türü kontrolü | `event.type == "response.output_text.delta"` filtresi kullanın, Chat'in `chat.completion.chunk` türü değil |
| Geçiş sonrası resim girişiyle `400` hatası | Resim içerik türü güncellenmemiş | `"type": "image_url"` → `"type": "input_image"` değiştirin ve `"image_url": {"url": "..."}` → `"image_url": "..."` (düz string) yapın |
| Araç çağrıları sonsuz döngüye giriyor | Sonuç araç çağrısının takip eden `input` içinde olmaması | Araç çalıştırıldıktan sonra, sonraki istekte `input` içerisine `{"type": "function_call_output", "call_id": ..., "output": ...}` öğesi ekleyin |
| GPT-5 veya o-serisi ile `temperature` hatası | `temperature` açıkça 1 dışında bir değer | GPT-5 ve o-serisi modeller için `temperature` kaldırın veya 1 yapın (o1, o3-mini, o3, o4-mini) |
| o-serisi ile `top_p` hatası | `top_p` desteklenmiyor | o-serisi hedefliyorsanız `top_p` parametresini kaldırın |
| `max_completion_tokens` tanınmıyor | Azure'a özel parametre kullanımı | `max_completion_tokens` yerine `max_output_tokens` kullanın. o-serisi için 4096+ değer verin (akıl yürütme tokenları limite dahil edilir). |
| o-serisinden boş/kesilmiş çıktı | `max_output_tokens` çok düşük | O-serisi dahili olarak akıl yürütme tokenları kullanır. `max_output_tokens=4096` veya üstü yapılmalı — 500–1000 değil. |
| `max_output_tokens` için `400 integer_below_min_value` | Değer 16'nın altında | Azure OpenAI `max_output_tokens >= 16` zorunlu kılar. Duman testleri için 50+, üretim için 1000+ kullanın. |
| Yayın sırasında `429 Too Many Requests` | Azure OpenAI tarafından sınırlanmış | Akış hata yakalama olmadan sessizce kopar. `async for event in await coroutine:` döngüsünü `try/except` ile sarın ve frontend için `{"error": str(e)}` JSON'u yayınlayın. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Yanlış tenant veya giriş yapılmamış | `tenant_id=os.getenv("AZURE_TENANT_ID")` açıkça geçirin. Yerelde `azd auth login --tenant <tenant-id>` çalıştırın. |
| GitHub Modelleri (`models.github.ai`) ile `404 Not Found` | GitHub Modelleri Responses API'yi desteklemez | GitHub Modelleri kod yolunu tamamen kaldırın. Azure OpenAI, OpenAI veya Responses destekleyen yerel endpoit kullanın (örn. Ollama). |
| MAF `OpenAIChatCompletionClient` hâlâ Chat Completions kullanıyor | 1.0.0+ sürümünde eski MAF istemcisi kullanımı | MAF 1.0.0+ sürümünde, `OpenAIChatClient` varsayılan olarak Responses API kullanır. `OpenAIChatCompletionClient` yerine `OpenAIChatClient` kullanın. 1.0.0 öncesi için `agent-framework-openai>=1.0.0`'a yükseltin. |
| LangChain ajanı boş döndürüyor veya araç çağrılarıyla başarısız oluyor | `ChatOpenAI` Responses API kullanmıyor | `ChatOpenAI(...)` içinde `use_responses_api=True` ekleyin. Yanıt mesajlarında `.content` → `.text` değiştirin. |
| İçerik filtre hatası işlemede `KeyError: 'innererror'` | Responses API'da hata gövdesi yapısı değişti | `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]` olarak yeniden yazın. `innererror` sarmalayıcısı kalktı; filtre detayları `content_filters` dizisinde, her girişte çoğul `content_filter_results` var. |
| `/openai/deployments/.../chat/completions` için ham HTTP çağrısı 404 döndürüyor | Eski Chat Completions REST uç noktası | URL'yi `/openai/v1/responses` olarak değiştirin. İstek gövdesi: `messages` → `input`, `max_output_tokens` + `store: false` ekleyin, `api-version` sorgu parametresini çıkarın. Yanıt ayrıştırmada: `choices[0].message.content` → `output[0].content[0].text` kullanın (not: `output_text` SDK kolaylığıdır, ham REST JSON'da yoktur). |

---

## Tuzaklar

1. Daha önce Chat Completions ile konuşma durumunu yönetiyorsanız, Responses ile durumunuzu açıkça yönetin.
2. Miras `max_tokens` yerine `max_output_tokens` tercih edin.
3. `gpt-5`'e geçerken `temperature` belirtilmemeli veya `1` olmalı.
4. Chat input'ları için `content[].type: "text"` yerine Responses için `content[].type: "input_text"` kullanın.
5. `text.format` için uygun sözlük sağlayın (örn. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), düz string değil.
6. Responses'da `seed` parametresi desteklenmez; isteklerden kaldırın.
7. **Akıl yürütme**: Sadece orijinal kod zaten kullanıyorsa `reasoning` ekleyin. Önceki çağrılarda olmayan `reasoning` eklemeyin — birçok akıl yürütme dışı model desteklemez.
8. **`max_output_tokens` boyutlandırması**: Akıl yürütme modelleri (GPT-5-mini, GPT-5, o-serisi) için `max_output_tokens=4096` veya üstü kullanın — 50–1000 değil. Model görünür çıktı üretmeden önce dahili akıl yürütme tokenları kullanır; düşük sınırlar boş veya kesilmiş sonuçlara neden olur.
9. **O-serisi `max_completion_tokens`**: Orijinal kod `max_completion_tokens` kullandıysa (o-serisi için Azure'a özel), `max_output_tokens` ile değiştirin. Responses API `max_completion_tokens` kabul etmez.
10. **O-serisi `reasoning_effort`**: Orijinal kod `reasoning_effort` (düşük/orta/yüksek) kullanıyorsa, Responses API çağrısında `reasoning={"effort": "<değer>"}` olarak geçirin.
11. **O-serisi streaming gecikmesi**: O-serisi modeller çıktıdan önce dahili akıl yürütme yapar. Streaming'de ilk `response.output_text.delta` olayına kadar daha uzun gecikme bekleyin. Bu normaldir — model donmamıştır, akıl yürütüyordur.
9. **`_azure_ad_token_provider` kaldırıldı**: `AsyncOpenAI` / `OpenAI` nesnelerinde `_azure_ad_token_provider` özelliği yoktur. Testler veya kod bu özelliğe erişirse `AttributeError` alır. Token sağlayıcı `api_key` olarak geçirilir ve istemci nesnesinde erişilemez.
10. **Anlık görüntü / altın dosyalar**: Test paketi snapshot testi kullanıyorsa, Chat Completions streaming şekillerini (`choices[0]`, `content_filter_results`, `function_call`, vb.) içeren **tüm** snapshot dosyaları yeni Responses şekline güncellenmelidir. Bu gözden kaçabilir ve snapshot doğrulama hatalarına neden olur.
11. **Mock monkeypatch yolu**: Monkeypatch hedefi `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` olarak değişti (senkron için `Responses.create`). Eski yolu kullanmak mock'un tetiklenmemesine ve gerçek API'ye gitmesine veya testlerin başarısız olmasına yol açar.
12. **`input` olmalı, `messages` değil**: Mock fonksiyonlar `kwargs.get("input")` okumalı, `kwargs.get("messages")` değil. Responses API konuşma geçmişi için `input` kullanır.
13. **Ortam değişkeni isimlendirmesi**: Azure Identity SDK `ManagedIdentityCredential(client_id=...)` için `AZURE_CLIENT_ID` kullanır (`AZURE_OPENAI_CLIENT_ID` değil). Testlerde, `.env` dosyalarında, uygulama ayarlarında ve Bicep/infra'da bu isimlendirmeyi değiştirin.
14. **`max_output_tokens` minimum 16**: Azure OpenAI 16'nın altındaki değerleri `400 integer_below_min_value` ile reddeder. Duman testleri için 50, üretimde 1000+ kullanın. Eski `max_tokens`'da böyle minimum yoktu.
15. **`AzureDeveloperCliCredential` için `tenant_id`**: Azure OpenAI kaynağı farklı tenant'taysa `tenant_id` açıkça verilmelidir — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Aksi takdirde yetkilendirme gizlice yanlış tenant'ı kullanır ve `401` döner.
16. **Rate limitler streamingde farklı görünür**: Chat Completions'da 429 genellikle stream başlamazken oluşurdu. Responses API streaming'de, 429 **yayın sırasında** olabilir — asenkron iterator istisna fırlatır. Streaming döngüsünü `try/except` ile sarın ve frontend'e hata JSON satırı yayınlayın, böylece düzgün ele alınabilir.

17. **Web uygulamaları için streaming hata yönetimi zorunludur**: `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` deseni kritiktir. Olmazsa, SSE/JSONL akışı herhangi bir sunucu tarafı hatasında sessizce sona erer ve ön yüz takılır.
18. **Araç tanımları düz formatta olmalıdır**: Yanıtlar API'si `{"type": "function", "name": ..., "parameters": ...}` bekler — Chat Completions iç içe `{"type": "function", "function": {"name": ..., "parameters": ...}}` değil. Bu, fonksiyon çağırma kodu için en yaygın taşıma hatasıdır.
19. **`pydantic_function_tool()` uyumsuzdur**: `openai.pydantic_function_tool()` yardımcısı hala eski iç içe formatı üretir. `responses.create()` ile kullanmayın. Araç şemalarını manuel tanımlayın veya çıktıyı düzleştirin.
20. **Araç sonuçları `function_call_output` kullanır, `role: tool` değil**: Bir aracı çalıştırdıktan sonra `{"type": "function_call_output", "call_id": ..., "output": ...}` ekleyin — `{"role": "tool", "tool_call_id": ..., "content": ...}` değil. Asistanın araç isteği için `messages.extend(response.output)` kullanın — manuel `{"role": "assistant", "tool_calls": [...]}` sözlüğü değil.
21. **`strict: true` için `required` + `additionalProperties: false` gerekir**: Bir araçta `strict: true` kullanılırken her özellik `required` dizisinde listelenmelidir ve `additionalProperties` `false` olmalıdır. Eksik biri 400 hatası oluşturur.
22. **Fonksiyon çağrısı kimlikleri belirli önekler taşır**: `input` içinde az sayıda `function_call` öğesi sağlarken, `id` alanı `fc_` ile başlamalı ve `call_id` alanı `call_` ile başlamalıdır (örn., `"id": "fc_example1", "call_id": "call_example1"`). Eski Chat Completions `call_` öneki `id` için kabul edilmez.
23. **GitHub Modelleri Yanıtlar API'sini desteklemez**: Uygulamada GitHub Modelleri kod yolu (`base_url` `models.github.ai` veya `models.inference.ai.azure.com` adresine işaret ediyor) varsa tamamen kaldırın. Taşıma yolu yoktur — Azure OpenAI, OpenAI veya uyumlu yerel bir uç noktaya geçin.
24. **İçerik filtresi hata gövde yapısı değişti**: Chat Completions hataları `error.body["innererror"]["content_filter_result"]` (tekil) kullanırken, Yanıtlar API hataları `error.body["content_filters"][0]["content_filter_results"]` (çoğul, bir dizi içinde) kullanır. `innererror` anahtarı artık yok. Doğrudan `innererror` erişen kod çalışma zamanında `KeyError` yükseltir — bu, içerik filtresi gerçekten tetiklenince ortaya çıktığı için taşıma sırasında kolayca kaçabilir. Taşıma sırasında hep `innererror` için arama yapın.
25. **Ham HTTP çağrıları URL + gövde yeniden yazımı gerektirir**: Azure OpenAI REST'i doğrudan çağıran uygulamalar (`requests`, `httpx`, `aiohttp` ile) `/openai/deployments/{name}/chat/completions?api-version=...` yerine `/openai/v1/responses` geçmelidir. İstek gövdesi `messages` yerine `input` kullanır, `max_output_tokens` ve `store` gerektirir ve `api-version` sorgu parametresi kaldırılır. Yanıt gövdesi metni `output[0].content[0].text` konumundadır — **`output_text` değil**, bu SDK kolaylık özelliği olup ham REST JSON'da yoktur.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->