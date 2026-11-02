---
name: azure-openai-to-responses
license: MIT
---
# Migrasi Aplikasi Python dari Azure OpenAI Chat Completions ke Responses API

> **PANDUAN OTORITATIF — IKUTI DENGAN TEPAT**
>
> Skill ini memigrasi basis kode Python yang menggunakan Azure OpenAI Chat Completions
> ke Responses API yang terpadu. Ikuti instruksi ini dengan tepat.
> Jangan mengimprovisasi pemetaan parameter atau menciptakan bentuk API baru.

---

## Pemicu

Aktifkan skill ini ketika pengguna ingin:
- Memigrasi aplikasi Python dari Azure OpenAI Chat Completions ke Responses API
- Memperbarui penggunaan SDK Python OpenAI ke bentuk API terbaru terhadap Azure OpenAI
- Mempersiapkan kode Python untuk model GPT-5 atau yang lebih baru yang memerlukan Responses di Azure
- Beralih dari `AzureOpenAI`/`AsyncAzureOpenAI` ke klien standar `OpenAI`/`AsyncOpenAI` dengan endpoint v1
- Memperbaiki peringatan deprecation terkait konstruktor `AzureOpenAI` atau `api_version`

---

## ⚠️ Kecocokan Model — PERIKSA TERLEBIH DAHULU

> **Sebelum migrasi, pastikan deployment Azure OpenAI Anda mendukung Responses API.**

### 1. Uji cepat deployment Anda (paling cepat)

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

> **Catatan**: `max_output_tokens` memiliki **minimum 16** di Azure OpenAI. Nilai di bawah 16 akan mengembalikan error 400. Gunakan nilai 50+ untuk uji cepat.

Jika ini mengembalikan 404, model deployment belum mendukung Responses — cek referensi di bawah atau deploy ulang dengan model yang didukung.

### 2. Periksa model yang tersedia di wilayah Anda (disarankan)

Jalankan alat kompatibilitas model bawaan untuk melihat apa yang tersedia dengan dukungan Responses API di wilayah spesifik Anda:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Ini melakukan query langsung ke Azure ARM dan menampilkan matriks kompatibilitas — model mana yang mendukung Responses, output terstruktur, tool, dll. Gunakan `--filter gpt-5.1,gpt-5.2` untuk mempersempit hasil atau `--json` untuk scripting.

### 3. Referensi dukungan model lengkap

- **Query langsung**: `python migrate.py models` (lihat di atas — spesifik wilayah, selalu terbaru)
- **Lihat ketersediaan**: [Tabel ringkasan model dan ketersediaan wilayah](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Mulai cepat & panduan**: **https://aka.ms/openai/start**

### ⚠️ Batasan model lama

> **PERINGATAN**: Model lama (yang dibuat sebelum `gpt-4.1`) mungkin tidak sepenuhnya mendukung semua fitur Responses API.
>
> Batasan dikenal dengan model lama:
> - **Parameter `reasoning`**: Tidak didukung di banyak model non-reasoning. Hanya migrasi `reasoning` jika sudah ada di kode asli.
> - **Parameter `seed`**: Tidak didukung sama sekali dalam Responses API — hapus dari semua permintaan.
> - **Output terstruktur via `text.format`**: Model lama mungkin tidak menegakkan skema JSON `strict: true` dengan konsisten.
> - **Orkestrasi tool**: GPT-5+ mengorkestrasi panggilan tool sebagai bagian dari reasoning internal. Model lama di Responses masih bekerja tapi tanpa integrasi dalam.
> - **Batasan temperature**: Saat migrasi ke `gpt-5`, temperature harus dihilangkan atau diatur ke `1`. Model lama tidak memiliki batasan ini.

### Model reasoning seri O (o1, o3-mini, o3, o4-mini)

Model seri O memiliki batasan parameter unik. Saat migrasi aplikasi yang menarget model seri O:

- **`temperature`**: Harus `1` (atau dihilangkan). Model seri O tidak menerima nilai lain.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikasi yang menggunakan `max_completion_tokens` khusus Azure harus beralih ke `max_output_tokens`. Atur nilai tinggi (4096+) karena token reasoning menghitung batas.
- **`reasoning_effort`**: Jika aplikasi menggunakan `reasoning_effort` (low/medium/high), pertahankan — Responses API mendukung parameter ini untuk model seri O.
- **Perilaku streaming**: Model seri O dapat menahan output sampai reasoning selesai sebelum mengeluarkan event delta teks. Streaming tetap berfungsi, tapi `response.output_text.delta` pertama mungkin datang dengan delay lebih lama dibanding model GPT.
- **`top_p`**: Tidak didukung di seri O — hapus bila ada.
- **Penggunaan tool**: Model seri O mendukung tool via Responses API sama seperti model GPT, namun kualitas orkestrasi panggilan tool bervariasi per model.

**Tindakan — advisori model proaktif**: Saat fase pemindaian, periksa model mana yang ditarget aplikasi (nama deployment, env vars, config). Jika model dibuat sebelum `gpt-4.1` (bukan gpt-4.1+), beri tahu pengguna secara proaktif:
- Migrasi akan bekerja untuk teks dasar, chat, streaming, dan tool di model mereka saat ini.
- Model yang lebih baru (`gpt-5.1`, `gpt-5.2`) menawarkan orkestrasi tool yang lebih baik, penegakan output terstruktur, reasoning, dan ketersediaan lintas wilayah.
- Mereka harus mempertimbangkan upgrade deployment saat siap — ini tidak menghalangi migrasi.

Jangan blokir atau tolak migrasi berdasarkan versi model. Advisori ini bersifat informatif.

### GitHub Models TIDAK mendukung Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) tidak mendukung Responses API.**

Jika basis kode memiliki jalur kode GitHub Models (cari `base_url` yang menunjuk ke `models.github.ai` atau `models.inference.ai.azure.com`), **hapus sepenuhnya** saat migrasi. Responses API membutuhkan Azure OpenAI, OpenAI, atau endpoint lokal kompatibel (misal Ollama dengan dukungan Responses).

Tindakan saat scan:
- Tandai jalur kode GitHub Models untuk dihapus.

---

## Migrasi Framework

Banyak aplikasi menggunakan framework tingkat tinggi di atas OpenAI. Saat memigrasi ini, perubahan API terjadi juga di framework, bukan hanya panggilan OpenAI di bawahnya.

### Microsoft Agent Framework (MAF)

**Periksa versi MAF Anda dulu** — migrasi bergantung apakah Anda menggunakan MAF 1.0.0+ atau beta/rc pre-1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **sudah menggunakan Responses API** — tidak perlu migrasi. Jika basis kode memakai `OpenAIChatCompletionClient` legacy (yang menggunakan `chat.completions.create`), ganti dengan `OpenAIChatClient`.

| Sebelum | Sesudah |
|--------|---------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Untuk memeriksa versi Anda: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (rilis beta/rc)

Di MAF pre-1.0.0, `OpenAIChatClient` memakai Chat Completions. Upgrade ke `agent-framework-openai>=1.0.0` di mana `OpenAIChatClient` menggunakan Responses API secara default.

Tidak ada perubahan lain yang diperlukan — API `Agent` dan tool tetap sama.

### LangChain (`langchain-openai`)

Tambahkan `use_responses_api=True` ke `ChatOpenAI()`. Juga perbarui akses respons dari `.content` ke `.text`.

| Sebelum | Sesudah |
|--------|---------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Untuk contoh kode lengkap sebelum/sesudah, lihat [cheat-sheet.md](./references/cheat-sheet.md).

---

## Panduan Migrasi Frontend

> **Responses API adalah urusan sisi server.** Migrasikan backend Python Anda; kontrak HTTP frontend harus tetap sama kecuali backend Anda hanya penerus tipis — dalam kasus itu, pertimbangkan menggunakan bentuk request Responses untuk menghilangkan lapisan terjemahan. Jika frontend memanggil OpenAI langsung dengan kunci sisi klien, pindahkan panggilan tersebut ke backend terlebih dahulu.

### Deprecation `@microsoft/ai-chat-protocol`

Paket npm `@microsoft/ai-chat-protocol` sudah deprecated dan harus diganti dengan [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Jika Anda menemukannya di frontend:

1. Ganti tag skrip CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Hapus instansiasi `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Ganti `client.getStreamedCompletion(messages)` dengan panggilan `fetch()` langsung ke endpoint streaming backend.
4. Ganti `for await (const response of result)` menjadi `for await (const chunk of readNDJSONStream(response.body))`.
5. Perbarui akses properti dari `response.delta.content` / `response.error` menjadi `chunk.delta.content` / `chunk.error`.

---

## Tujuan

- Daftar semua panggilan Python yang menggunakan Chat Completions atau Completions legacy terhadap Azure OpenAI.
- Usulkan rencana migrasi dan urutan untuk basis kode Python.
- Terapkan suntingan minimal dan aman untuk beralih ke Responses API.
- Perbarui pemanggil untuk menggunakan skema output Responses; tidak ada pembungkus kompatibilitas mundur.
- Jalankan tes/lint; perbaiki kerusakan sepele akibat migrasi.
- Siapkan set perubahan kecil yang dapat ditinjau dan berikan ringkasan akhir dengan diff (jangan commit).

---

## Pembatasan

- Hanya modifikasi file di dalam workspace git. Jangan pernah tulis di luar.
- Jangan simpan shim kompatibilitas balik; migrasikan kode ke bentuk API baru.
- Jangan tinggalkan komentar transisi/tombstone atau file backup.
- Pertahankan semantik streaming jika sebelumnya digunakan; jika tidak, gunakan non-streaming.
- Minta persetujuan sebelum menjalankan perintah atau panggilan jaringan jika dalam mode persetujuan.
- Jangan menjalankan `git add`/`git commit`/`git push`; hasilkan hanya suntingan working-tree.

---

## Langkah 0: Migrasi Klien Azure OpenAI (Prasyarat)

Jika basis kode menggunakan konstruktor `AzureOpenAI` atau `AsyncAzureOpenAI`, migrasikan ke konstruktor standar `OpenAI` / `AsyncOpenAI` dulu. Konstruktor khusus Azure sudah deprecated di `openai>=1.108.1`.

### Kenapa jalur API v1?

Endpoint baru `/openai/v1` menggunakan klien standar `OpenAI()` bukan `AzureOpenAI()`, tidak butuh parameter `api_version`, dan bekerja identik di OpenAI dan Azure OpenAI. Kode klien ini tahan masa depan — tidak perlu pengelolaan versi.

### Perubahan utama

| Sebelum | Sesudah |
|--------|---------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Hapus seluruhnya |

### Daftar periksa pembersihan

- Hapus argumen `api_version` dari konstruksi klien.
- Hapus variabel lingkungan `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` dari `.env`, pengaturan aplikasi, dan file Bicep/infrastruktur.
- Ganti nama `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` di `.env`, pengaturan aplikasi, Bicep/infrastruktur, dan fixture tes (konvensi standar SDK Azure Identity).
- Pastikan `openai>=1.108.1` di `requirements.txt` atau `pyproject.toml`.

### Migrasi variabel lingkungan

| Variabel env lama | Aksi | Catatan |
|------------------|-------|---------|
| `AZURE_OPENAI_VERSION` | **Hapus** | Tidak perlu `api_version` dengan endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Hapus** | Sama seperti di atas |
| `AZURE_OPENAI_CLIENT_ID` | **Ganti nama** → `AZURE_CLIENT_ID` | Konvensi standar SDK Azure Identity untuk `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Simpan** | Masih perlu untuk konstruksi `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Simpan** | Digunakan sebagai parameter `model` dalam `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Simpan** | Digunakan sebagai `api_key` untuk autentikasi berbasis kunci |

Untuk contoh kode setup klien (sinkron, asinkron, EntraID, kunci API, multi-tenant), lihat [cheat-sheet.md](./references/cheat-sheet.md).

---

## Langkah 1: Deteksi Lokasi Panggilan Legacy

Jalankan skrip [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) untuk menemukan semua lokasi panggilan yang perlu migrasi:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Atau lakukan pencarian manual ini — setiap kecocokan adalah target migrasi:

```bash
# Panggilan API warisan (harus ditulis ulang)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Konstruktor klien Azure yang sudah usang (harus diganti)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Pola akses bentuk respons (harus diperbarui)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definisi alat dalam format bersarang lama (harus diratakan)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Hasil alat dalam format lama (harus dikonversi ke function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Parameter yang sudah usang (harus dihapus atau diganti nama)
rg "response_format"
rg "max_tokens\b"        # ganti nama menjadi max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Variabel lingkungan yang sudah usang (bersihkan)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # seharusnya AZURE_CLIENT_ID

# Endpoint Model GitHub (harus dihapus — API Respons tidak didukung)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Pola warisan tingkat kerangka kerja (harus diperbarui)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: ganti dengan OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: perlu use_responses_api=True

# Infrastruktur pengujian (harus diperbarui)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Akses isi kesalahan filter konten (harus diperbarui — struktur berubah)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # bentuk tunggal lama — sekarang content_filter_results (jamak) di dalam array content_filters

# Panggilan HTTP mentah ke endpoint Chat Completions (harus perbarui URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristik (deteksi dan tulis ulang)

- **Klien Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Konstruktor klien Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Alat**: ubah definisi alat panggilan fungsi dari format bersarang (`{"type": "function", "function": {"name": ...}}`) menjadi format Responses datar (`{"type": "function", "name": ...}`); gunakan `tool_choice`; kembalikan hasil alat sebagai item `{"type": "function_call_output", "call_id": ..., "output": ...}` (bukan `{"role": "tool", ...}`).
- **Putaran alat**: ketika model mengembalikan panggilan fungsi, tambahkan item `response.output` ke percakapan (bukan dict manual `{"role": "assistant", "tool_calls": [...]}`), lalu tambahkan item `function_call_output` untuk setiap hasil.
- **Contoh alat few-shot**: jika percakapan menyertakan contoh panggilan alat yang dikodekan keras, ubah menjadi item `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID harus dimulai dengan `fc_`.
- **`pydantic_function_tool()`**: pembantu ini masih menghasilkan format bersarang lama dan **tidak kompatibel** dengan `responses.create()`. Ganti dengan definisi alat manual atau pembungkus perataan.
- **Multi-putaran**: simpan riwayat percakapan dalam aplikasi; teruskan putaran sebelumnya melalui item `input`.
- **Pemformatan**: ganti `response_format` tingkat atas Chat dengan `text.format` di Responses. Bentuk kanonik: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Item konten**: ganti `content[].type: "text"` Chat dengan `content[].type: "input_text"` Responses untuk putaran pengguna/sistem.
- **Item konten gambar**: ganti `content[].type: "image_url"` Chat dengan `content[].type: "input_image"` Responses. Bidang `image_url` berubah dari objek bersarang `{"url": "..."}` menjadi string datar. Lihat cheat sheet untuk contoh sebelum/setelah.
- **Usaha penalaran**: **hanya migrasikan `reasoning` jika sudah ada dalam kode asli**.
- **Penanganan kesalahan filter konten**: struktur isi badan kesalahan berubah. Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]` (tunggal); Responses API menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, dalam array). Kode yang mengakses `innererror` akan menimbulkan `KeyError`. Tulis ulang untuk menggunakan jalur baru.
- **Panggilan HTTP mentah**: jika aplikasi memanggil REST API Azure OpenAI langsung (via `requests`, `httpx`, dll.) menggunakan `/openai/deployments/{name}/chat/completions?api-version=...`, ubah menjadi `/openai/v1/responses`. Isi permintaan berubah: `messages` → `input`, tambahkan `max_output_tokens` dan `store: false`, hilangkan parameter query `api-version`. Isi respons berubah: `choices[0].message.content` → `output[0].content[0].text` (catatan: `output_text` adalah properti kenyamanan SDK yang tidak ada di JSON REST mentah).

---

## Langkah 2: Terapkan Migrasi

### Catatan Migrasi (Chat Completions → Responses)

- **Mengapa migrasi**: Responses adalah API terpadu untuk teks, alat, dan streaming; Chat Completions adalah warisan. Dengan GPT-5, Responses diperlukan untuk kinerja terbaik.
- **HTTP**: endpoint Azure beralih dari `/openai/deployments/{name}/chat/completions` ke `/openai/v1/responses`.
- **Bidang**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` tetap.
- **Pemformatan**: `response_format` → `text.format` dengan objek yang tepat.
- **Item konten**: Ganti Chat `content[].type: "text"` dengan Responses `content[].type: "input_text"` untuk putaran sistem/pengguna.
- **Item konten gambar**: Ganti Chat `content[].type: "image_url"` dengan Responses `content[].type: "input_image"`. Ratakan bidang `image_url` dari `{"image_url": {"url": "..."}}` ke `{"image_url": "..."}` (string biasa — baik URL HTTPS atau URI data `data:image/...;base64,...`).

### Referensi pemetaan parameter

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array item) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objek) |
| `temperature` | `temperature` (tidak berubah) |
| `stop` | `stop` (tidak berubah) |
| `frequency_penalty` | `frequency_penalty` (tidak berubah) |
| `presence_penalty` | `presence_penalty` (tidak berubah) |
| `tools` / pemanggilan fungsi | `tools` (tidak berubah) |
| `seed` | **Hapus** (tidak didukung) |
| `store` | `store` (atur ke `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (string datar) |

Untuk contoh kode lengkap sebelum/setelah, lihat [cheat-sheet.md](./references/cheat-sheet.md).

Untuk migrasi infrastruktur pengujian (mock, snapshot, assertions), lihat [test-migration.md](./references/test-migration.md).

Untuk pemecahan masalah error dan gotcha, lihat [troubleshooting.md](./references/troubleshooting.md).

---

## Retensi Data & Status

- Atur `store: false` pada semua permintaan Responses.
- Jangan mengandalkan ID pesan sebelumnya atau konteks yang disimpan server; kelola status klien sendiri dan minimalkan metadata.

---

## Kriteria Penerimaan

### Gerbang tingkat kode (semua harus lolos)

- [ ] Tidak ada kecocokan untuk `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` di file yang telah dimigrasi.
- [ ] Tidak ada kecocokan untuk `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — semua konstruktor menggunakan `OpenAI`/`AsyncOpenAI` dengan endpoint v1.
- [ ] Tidak ada kecocokan untuk `rg "models\.github\.ai|models\.inference\.ai\.azure"` — jalur kode Model GitHub telah dihapus.
- [ ] Tidak ada kecocokan untuk `rg "OpenAIChatCompletionClient"` — kode MAF 1.0.0+ menggunakan `OpenAIChatClient` (yang menggunakan Responses API). Pada versi pra-1.0.0, tingkatkan ke `agent-framework-openai>=1.0.0`.
- [ ] Semua panggilan `ChatOpenAI(...)` menyertakan `use_responses_api=True`.
- [ ] Tidak ada kecocokan untuk `rg "choices\[0\]"` — semua akses respons menggunakan `resp.output_text` atau skema output Responses.
- [ ] Tidak ada `response_format` di tingkat atas; semua output terstruktur menggunakan `text={"format": {...}}`.
- [ ] `openai>=1.108.1` dan `azure-identity` ada dalam `requirements.txt` atau `pyproject.toml`; ketergantungan telah diinstal ulang.
- [ ] `store=False` diatur pada setiap panggilan `responses.create`.
- [ ] Tidak ada `api_version` dalam konstruktor klien; `AZURE_OPENAI_API_VERSION` dihapus dari file env dan infrastruktur.

### Gerbang infrastruktur pengujian (semua harus lolos)

- [ ] Tidak ada kecocokan untuk `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Tidak ada kecocokan untuk `rg "_azure_ad_token_provider" tests/` — assertion diperbarui untuk memeriksa `isinstance(client, AsyncOpenAI)` atau `base_url`.
- [ ] Tidak ada kecocokan untuk `rg "prompt_filter_results|content_filter_results" tests/` — mock filter spesifik Azure dihapus.
- [ ] Fixture mock menggunakan `kwargs.get("input")` bukan `kwargs.get("messages")`.
- [ ] File snapshot / golden diperbarui ke bentuk streaming Responses (tidak ada `choices[0]`, `function_call`, `logprobs`, dll.).
- [ ] `pytest` lulus tanpa kegagalan setelah semua pembaruan tes.

### Gerbang perilaku (verifikasi manual atau melalui test harness)

- [ ] **Penyelesaian dasar**: non-streaming `responses.create` mengembalikan `output_text` yang tidak kosong.
- [ ] **Paritas streaming**: jika kode asli menggunakan streaming, kode yang dimigrasi stream dan menghasilkan event delta `response.output_text.delta` dengan delta yang tidak kosong.
- [ ] **Output terstruktur**: jika menggunakan `text.format` dengan `json_schema`, `json.loads(resp.output_text)` berhasil dan cocok dengan skema.
- [ ] **Loop panggilan alat**: jika alat digunakan, model mengeluarkan panggilan alat, aplikasi mengeksekusinya, dan permintaan tindak lanjut mengembalikan `output_text` final (tidak terjadi loop tanpa akhir).
- [ ] **Paritas Async**: jika `AsyncAzureOpenAI` digunakan, ekuivalennya `AsyncOpenAI` bekerja dengan `await`.
- [ ] **Tingkat kesalahan**: tidak ada error 400/401/404 baru dibandingkan baseline sebelum migrasi.

### Hasil yang diserahkan

- Ringkasan mencakup file yang diedit, hitungan situs panggilan warisan sebelum/sesudah, dan langkah selanjutnya.
- Perubahan hanya di pohon kerja (tanpa commit).

---

## Persyaratan Versi SDK

| Paket | Versi Minimum |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Terbaru (untuk autentikasi EntraID) |

---

## Referensi

- [Cheat Sheet — semua potongan kode](./references/cheat-sheet.md)
- [Test Migration — mock, snapshot, assertions](./references/test-migration.md)
- [Troubleshooting — error, tabel risiko, gotcha](./references/troubleshooting.md)
- [detect_legacy.py — pemindai otomatis](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Dokumentasi Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Siklus hidup versi API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Referensi OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->