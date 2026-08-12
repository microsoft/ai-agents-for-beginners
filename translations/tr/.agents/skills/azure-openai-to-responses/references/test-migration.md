# Test Altyapısı Geçişi

Bir kod tabanını Chat Completions'dan Responses API'ye geçirirken, **testler öngörülebilir şekillerde bozulur**. Bu referans neyin düzeltilmesi gerektiğini kapsar.

---

## Akış Yanıtlarını Taklit Etme (Python pytest)

### Temel taklit sınıfları

```python
class MockResponseEvent:
    """Simulates a Responses API streaming event."""
    def __init__(self, event_type: str, delta: str | None = None):
        self.type = event_type
        self.delta = delta

class AsyncResponseIterator:
    """Async iterator that yields Responses API streaming events from a string answer."""
    def __init__(self, answer: str):
        self.event_index = 0
        self.events = []
        for i, word in enumerate(answer.split(" ")):
            # Beyaz boşlukları koruyun: İlk kelime hariç tüm kelimelerin önüne boşluk ekleyin
            if i > 0:
                word = " " + word
            self.events.append(MockResponseEvent("response.output_text.delta", delta=word))
        self.events.append(MockResponseEvent("response.completed"))

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.event_index < len(self.events):
            event = self.events[self.event_index]
            self.event_index += 1
            return event
        raise StopAsyncIteration
```

### Mesaj içeriğine göre taklit yanıtları yönlendirme

Gerçek uygulamalar, isteme dayalı farklı cevaplar sunar. `input` ile yönlendirin (`messages` değil):

```python
async def mock_acreate(*args, **kwargs):
    # Yanıtlar API'si 'input' kullanır, 'messages' değil
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch yolları

| İstemci türü | Monkeypatch yolu |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (senkron) | `openai.resources.responses.Responses.create` |

> **Önce** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Sonra** (Responses): `openai.resources.responses.AsyncResponses.create`

### Tam fixture örneği

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent ve AsyncResponseIterator sınıfları burada ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Taklit fixture'larını güncelleyin

`ChatCompletionChunk` tabanlı taklitleri yukarıdaki `MockResponseEvent` / `AsyncResponseIterator` kalıbı ile değiştirin. Temel değişiklikler:

| Önce (Chat Completions taklidi) | Sonra (Responses taklidi) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` parçacığında | `event.type == "response.completed"` |
| Azure'ye özgü `prompt_filter_results` parçacığı | Tamamen kaldırın |
| Azure'ye özgü her seçim için `content_filter_results` | Tamamen kaldırın |
| Taklitte `kwargs.get("messages")` | Taklitte `kwargs.get("input")` |

---

## 2. Anlık görüntü / golden dosyaları güncelleyin

Test seti anlık görüntü testini kullanıyorsa (örneğin, `pytest-snapshot`, syrupy veya elle hazırlanmış JSONL anlık görüntüleri), beklenen çıktı şekli değişir:

**Önce** (Chat Completions akış JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Sonra** (Responses API akış JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Yeni şekil oldukça basitleşmiş — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` veya `content_filter_results` alanları yok. Tüm anlık görüntü dosyalarını güncelleyin veya yeniden oluşturun.

> **İpucu**: Geçişten sonra testleri otomatik olarak yeniden oluşturmak için `--snapshot-update` (pytest-snapshot) veya `--update-snapshots` (syrupy) ile çalıştırın.

---

## 3. Test doğrulamalarını güncelleyin

Yaygın doğrulama kopmaları:

| Eski doğrulama | Sorun | Yeni doğrulama |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI`'de `_azure_ad_token_provider` özniteliği yok | `isinstance(client, AsyncOpenAI)` ve `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` üzerinde `api_version` yok | Tamamen kaldırın |
| `isinstance(client, AsyncAzureOpenAI)` | İstemci türü değişti | `isinstance(client, AsyncOpenAI)` |

---

## 4. Test fixture'larında ortam değişkenlerini güncelleyin

Testler genellikle ortam değişkenlerini `monkeypatch.setenv` ile ayarlar. Bunları güncelleyin:

| Eski ortam değişkeni | Yeni ortam değişkeni | Notlar |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standart Azure Identity SDK kuralı |
| `AZURE_OPENAI_VERSION` | Kaldır | `api_version` gerekmez |
| `AZURE_OPENAI_API_VERSION` | Kaldır | `api_version` gerekmez |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Tut (hala `base_url` için gerekli) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Tut (`model` parametresi için dağıtım adı) |

---

## 5. Geçiş gerektiren test kodlarını arayın

```bash
# Teste özgü eski desenler
rg "ChatCompletionChunk" tests/
rg "AsyncCompletions\.create" tests/
rg "chat\.completions" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results" tests/
rg "content_filter_results" tests/
rg "AZURE_OPENAI_VERSION|AZURE_OPENAI_API_VERSION" tests/
rg "AZURE_OPENAI_CLIENT_ID" tests/
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->