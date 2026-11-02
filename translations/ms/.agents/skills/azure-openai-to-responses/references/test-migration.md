# Migrasi Infrastruktur Ujian

Apabila memindahkan kodbase daripada Chat Completions kepada Responses API, **ujian rosak dengan cara yang boleh diramal**. Rujukan ini merangkumi apa yang perlu diperbaiki.

---

## Memalsukan Streaming Responses (Python pytest)

### Kelas mock teras

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
            # Kekalkan ruang kosong: tambah ruang di hadapan semua perkataan kecuali yang pertama
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

### Menyampaikan mock responses berdasarkan kandungan mesej

Aplikasi sebenar memberikan jawapan berbeza berdasarkan prompt. Hantar berdasarkan `input` (bukan `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API Respon menggunakan 'input' bukan 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Laluan monkeypatch

| Jenis Klien | Laluan Monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Sebelum** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Selepas** (Responses): `openai.resources.responses.AsyncResponses.create`

### Contoh lengkap fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... kelas MockResponseEvent dan AsyncResponseIterator di sini ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Kemas kini mock fixtures

Gantikan mock berdasarkan `ChatCompletionChunk` dengan corak `MockResponseEvent` / `AsyncResponseIterator` di atas. Perubahan utama:

| Sebelum (mock Chat Completions) | Selepas (mock Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` dalam chunk | `event.type == "response.completed"` |
| chunk khusus Azure `prompt_filter_results` | Buang sepenuhnya |
| hasil penapisan kandungan khusus Azure per pilihan | Buang sepenuhnya |
| `kwargs.get("messages")` dalam mock | `kwargs.get("input")` dalam mock |

---

## 2. Kemas kini snapshot / fail golden

Jika suite ujian menggunakan ujian snapshot (contohnya, `pytest-snapshot`, syrupy, atau snapshot JSONL hasil tangan), bentuk output yang dijangka berubah:

**Sebelum** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Selepas** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Bentuk baru jauh lebih ringkas — tiada medan `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, atau `content_filter_results`. Kemas kini atau hasilkan semula semua fail snapshot.

> **Petua**: Jalankan ujian dengan `--snapshot-update` (pytest-snapshot) atau `--update-snapshots` (syrupy) selepas migrasi untuk menjana semula secara automatik.

---

## 3. Kemas kini pernyataan ujian

Kerusakan pernyataan biasa:

| Pernyataan Lama | Masalah | Pernyataan Baru |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` tiada atribut `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` dan `"/openai/v1/" dalam str(client.base_url)` |
| `client.api_version == "2024-..."` | Tiada `api_version` pada `OpenAI`/`AsyncOpenAI` | Buang sepenuhnya |
| `isinstance(client, AsyncAzureOpenAI)` | Jenis klien berubah | `isinstance(client, AsyncOpenAI)` |

---

## 4. Kemas kini pembolehubah persekitaran dalam fixtures ujian

Ujian sering menetapkan pembolehubah persekitaran melalui `monkeypatch.setenv`. Kemas kini ini:

| Pembolehubah persekitaran lama | Pembolehubah persekitaran baru | Nota |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Konvensyen SDK Identiti Azure standard |
| `AZURE_OPENAI_VERSION` | Buang | Tiada `api_version` diperlukan |
| `AZURE_OPENAI_API_VERSION` | Buang | Tiada `api_version` diperlukan |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Kekalkan (masih diperlukan untuk `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Kekalkan (nama penyebaran untuk parameter `model`) |

---

## 5. Cari kod ujian yang perlu dimigrasi

```bash
# Corak legasi khusus ujian
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
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->