# Migrasi Infrastruktur Tes

Saat memigrasi basis kode dari Chat Completions ke Responses API, **tes gagal dengan cara yang dapat diprediksi**. Referensi ini membahas apa yang harus diperbaiki.

---

## Mocking Respons Streaming (Python pytest)

### Kelas mock inti

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
            # Pertahankan spasi: tambahkan spasi di depan semua kata kecuali yang pertama
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

### Mengarahkan mock respons berdasarkan isi pesan

Aplikasi nyata memberikan jawaban berbeda berdasarkan prompt. Arahkan berdasarkan `input` (bukan `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API Responses menggunakan 'input' bukan 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Path monkeypatch

| Tipe Klien | Path Monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sinkron) | `openai.resources.responses.Responses.create` |

> **Sebelum** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Sesudah** (Responses): `openai.resources.responses.AsyncResponses.create`

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

## 1. Perbarui mock fixtures

Gantikan mock berbasis `ChatCompletionChunk` dengan pola `MockResponseEvent` / `AsyncResponseIterator` di atas. Perubahan kunci:

| Sebelum (mock Chat Completions) | Sesudah (mock Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` di chunk | `event.type == "response.completed"` |
| Chunk khusus Azure `prompt_filter_results` | Hapus sepenuhnya |
| `content_filter_results` per pilihan khusus Azure | Hapus sepenuhnya |
| `kwargs.get("messages")` di mock | `kwargs.get("input")` di mock |

---

## 2. Perbarui snapshot / file golden

Jika suite tes menggunakan snapshot testing (misal, `pytest-snapshot`, syrupy, atau snapshot JSONL buatan tangan), bentuk keluaran yang diharapkan berubah:

**Sebelum** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Sesudah** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Bentuk baru jauh lebih sederhana — tidak ada bidang `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, atau `content_filter_results`. Perbarui atau buat ulang semua file snapshot.

> **Tip**: Jalankan tes dengan `--snapshot-update` (pytest-snapshot) atau `--update-snapshots` (syrupy) setelah migrasi untuk menggenerasi ulang secara otomatis.

---

## 3. Perbarui assertion tes

Kerusakan assertion umum:

| Assertion lama | Masalah | Assertion baru |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` tidak memiliki atribut `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` dan `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Tidak ada `api_version` pada `OpenAI`/`AsyncOpenAI` | Hapus sepenuhnya |
| `isinstance(client, AsyncAzureOpenAI)` | Tipe klien berubah | `isinstance(client, AsyncOpenAI)` |

---

## 4. Perbarui variabel lingkungan di fixture tes

Tes sering mengatur variabel lingkungan lewat `monkeypatch.setenv`. Perbarui ini:

| Variabel lingkungan lama | Variabel lingkungan baru | Catatan |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Konvensi standar Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Hapus | Tidak perlu `api_version` |
| `AZURE_OPENAI_API_VERSION` | Hapus | Tidak perlu `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Tetap (masih diperlukan untuk `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Tetap (nama deployment untuk param `model`) |

---

## 5. Cari kode tes yang perlu migrasi

```bash
# Pola warisan spesifik untuk pengujian
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
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->