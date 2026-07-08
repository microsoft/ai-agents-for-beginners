---
name: azure-openai-to-responses
license: MIT
---
# Migrasi Aplikasi Python dari Azure OpenAI Chat Completions ke Responses API

> **PANDUAN BERWENANG — IKUTI DENGAN TEPAT**
>
> Skill ini memigrasikan kode Python yang menggunakan Azure OpenAI Chat Completions
> ke Responses API yang terpadu. Ikuti instruksi ini dengan tepat.
> Jangan berimprovisasi pemetaan parameter atau membuat bentuk API sendiri.

---

## Pemicu

Aktifkan skill ini ketika pengguna ingin:
- Memigrasikan aplikasi Python dari Azure OpenAI Chat Completions ke Responses API
- Meningkatkan penggunaan SDK OpenAI Python ke bentuk API terbaru untuk Azure OpenAI
- Mempersiapkan kode Python untuk model GPT-5 atau yang lebih baru yang membutuhkan Responses di Azure
- Beralih dari klien `AzureOpenAI`/`AsyncAzureOpenAI` ke klien standar `OpenAI`/`AsyncOpenAI` dengan endpoint v1
- Memperbaiki peringatan deprecation terkait konstruktor `AzureOpenAI` atau `api_version`

---

## ⚠️ Kompatibilitas Model — PERIKSA TERLEBIH DAHULU

> **Sebelum migrasi, verifikasi deployment Azure OpenAI Anda mendukung Responses API.**

### 1. Tes singkat deployment Anda (paling cepat)

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

> **Catatan**: `max_output_tokens` memiliki **minimum 16** di Azure OpenAI. Nilai di bawah 16 mengembalikan kesalahan 400. Gunakan 50+ untuk tes singkat.

Jika ini mengembalikan 404, model deployment belum mendukung Responses — periksa referensi di bawah atau deploy ulang dengan model yang didukung.

### 2. Periksa model yang tersedia di region Anda (disarankan)

Jalankan alat kompatibilitas model bawaan untuk melihat yang tersedia dengan dukungan Responses API di region spesifik Anda:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Ini melakukan query langsung ke Azure ARM dan menampilkan matriks kompatibilitas — model mana yang mendukung Responses, output terstruktur, alat, dll. Gunakan `--filter gpt-5.1,gpt-5.2` untuk mempersempit hasil atau `--json` untuk scripting.

### 3. Referensi dukungan model lengkap

- **Query langsung**: `python migrate.py models` (lihat di atas — per region, selalu terbaru)
- **Lihat ketersediaan**: [Tabel ringkasan model dan ketersediaan regional](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Panduan & permulaan cepat**: **https://aka.ms/openai/start**

### ⚠️ Keterbatasan model lama

> **PERINGATAN**: Model-model lama (misal, `gpt-4o`, `gpt-4`) mungkin tidak mendukung semua fitur Responses API secara penuh.
>
> Keterbatasan yang diketahui dengan model lama:
> - **Parameter `reasoning`**: Tidak didukung pada `gpt-4o-mini`, `gpt-4o`, dan banyak model tanpa reasoning. Migrasikan `reasoning` hanya jika sudah ada di kode asli.
> - **Parameter `seed`**: Tidak didukung sama sekali di Responses API — hapus dari semua permintaan.
> - **Output terstruktur melalui `text.format`**: Model lama mungkin tidak selalu menerapkan skema JSON `strict: true` dengan andal.
> - **Orkestrasi alat**: GPT-5+ mengorkestrasi pemanggilan alat sebagai bagian dari reasoning internal. Model lama di Responses masih bekerja tapi kurang integrasi dalam.
> - **Keterbatasan temperatur**: Saat migrasi ke `gpt-5`, temperatur harus dihilangkan atau diset ke `1`. Model lama tidak memiliki batasan ini.

### Model reasoning seri O (o1, o3-mini, o3, o4-mini)

Model seri O memiliki batasan parameter unik. Saat migrasi aplikasi yang menargetkan model seri O:

- **`temperature`**: Harus `1` (atau dihilangkan). Model seri O tidak menerima nilai lain.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikasi yang menggunakan `max_completion_tokens` khusus Azure harus beralih ke `max_output_tokens`. Tetapkan nilai tinggi (4096+) karena token reasoning dihitung terhadap batas.
- **`reasoning_effort`**: Jika aplikasi menggunakan `reasoning_effort` (rendah/sedang/tinggi), pertahankan — Responses API mendukung parameter ini untuk model seri O.
- **Perilaku streaming**: Model seri O dapat menunda output sampai reasoning selesai sebelum mengeluarkan event delta teks. Streaming masih berfungsi, tetapi delta `response.output_text.delta` pertama mungkin terlambat dibanding model GPT.
- **`top_p`**: Tidak didukung di seri O — hapus jika ada.
- **Penggunaan alat**: Model seri O mendukung alat melalui Responses API sama seperti model GPT, tapi kualitas orkestrasi alat bervariasi menurut model.

**Tindakan — advis model proaktif**: Saat fase scan, cek model apa yang ditarget aplikasi (nama deployment, env vars, konfigurasi). Jika model `gpt-4o` atau lebih lama (bukan gpt-4.1+), beri tahu pengguna secara proaktif:
- Migrasi akan berfungsi untuk teks dasar, chat, streaming, dan alat di model mereka sekarang.
- Model yang lebih baru (`gpt-5.1`, `gpt-5.2`) menawarkan orkestrasi alat lebih baik, penerapan output terstruktur, reasoning, dan ketersediaan lintas region.
- Mereka harus mempertimbangkan upgrade deployment saat siap — ini tidak menghalangi migrasi.

Jangan blokir atau tolak migrasi berdasarkan versi model. Advisory ini bersifat informasional.

### GitHub Models TIDAK mendukung Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) tidak mendukung Responses API.**

Jika kode memiliki jalur kode GitHub Models (cari `base_url` yang mengarah ke `models.github.ai` atau `models.inference.ai.azure.com`), **hapus seluruhnya** saat migrasi. Responses API membutuhkan Azure OpenAI, OpenAI, atau endpoint lokal kompatibel (misal Ollama dengan dukungan Responses).

Tindakan saat scan:
- Tandai semua jalur kode GitHub Models untuk dihapus.

---

## Migrasi Framework

Banyak aplikasi menggunakan framework tingkat tinggi di atas OpenAI. Saat migrasi, perubahan terjadi pada API framework itu sendiri — bukan hanya panggilan OpenAI dasar.

### Microsoft Agent Framework (MAF)

**Periksa versi MAF Anda dulu** — migrasi bergantung pada apakah Anda menggunakan MAF 1.0.0+ atau beta/rc pra-1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **sudah memakai Responses API** — tidak perlu migrasi. Jika kode menggunakan `OpenAIChatCompletionClient` lama (menggunakan `chat.completions.create`), ganti dengan `OpenAIChatClient`.

| Sebelumnya | Sesudah |
|----------|---------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Untuk cek versi: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pra-1.0.0 (rilis beta/rc)

Di MAF pra-1.0.0, `OpenAIChatClient` menggunakan Chat Completions. Upgrade ke `agent-framework-openai>=1.0.0` dimana `OpenAIChatClient` memakai Responses API secara default.

Tidak perlu perubahan lain — API `Agent` dan alat tetap sama.

### LangChain (`langchain-openai`)

Tambahkan `use_responses_api=True` ke `ChatOpenAI()`. Juga ubah akses respons dari `.content` ke `.text`.

| Sebelumnya | Sesudah |
|----------|---------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Untuk contoh kode lengkap sebelum/sesudah, lihat [cheat-sheet.md](./references/cheat-sheet.md).

---

## Panduan Migrasi Frontend

> **Responses API adalah masalah sisi server.** Migrasikan backend Python Anda; kontrak HTTP frontend sebaiknya tetap sama kecuali backend hanya meneruskan dengan tipis — dalam kasus itu, pertimbangkan memakai bentuk permintaan Responses untuk menghilangkan lapisan translasi. Jika frontend langsung memanggil OpenAI dengan kunci sisi-klien, pindahkan panggilan itu ke backend dulu.

### Deprecation `@microsoft/ai-chat-protocol`

Paket npm `@microsoft/ai-chat-protocol` sudah deprecated dan harus diganti dengan [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Jika ditemukan di frontend:

1. Ganti tag skrip CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Hapus instansiasi `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Ganti `client.getStreamedCompletion(messages)` dengan panggilan `fetch()` langsung ke endpoint streaming backend.
4. Ganti `for await (const response of result)` dengan `for await (const chunk of readNDJSONStream(response.body))`.
5. Perbarui akses properti dari `response.delta.content` / `response.error` ke `chunk.delta.content` / `chunk.error`.

---

## Tujuan

- Menemukan semua lokasi panggilan Python yang menggunakan Chat Completions atau Completions lama terhadap Azure OpenAI.
- Mengusulkan rencana migrasi dan urutan untuk kode Python.
- Menerapkan perubahan minimal dan aman untuk beralih ke Responses API.
- Memperbarui pemanggil agar menggunakan skema output Responses; tanpa pembungkus kompatibilitas lama.
- Menjalankan tes/lint; memperbaiki gangguan kecil akibat migrasi.
- Mempersiapkan perubahan kecil yang bisa ditinjau dan menyediakan ringkasan akhir dengan diff (jangan commit).

---

## Batasan

- Hanya ubah file di dalam workspace git. Jangan menulis di luar.
- Jangan mempertahankan shim kompatibilitas lama; migrasikan kode ke bentuk API baru.
- Jangan meninggalkan komentar transisi atau file cadangan.
- Pertahankan semantik streaming jika sebelumnya dipakai; jika tidak, gunakan non-streaming.
- Minta persetujuan sebelum menjalankan perintah atau panggilan jaringan jika dalam mode persetujuan.
- Jangan menjalankan `git add`/`git commit`/`git push`; hanya hasil edit working-tree.

---

## Langkah 0: Migrasi Klien Azure OpenAI (Prasyarat)

Jika kode menggunakan konstruktor `AzureOpenAI` atau `AsyncAzureOpenAI`, migrasikan dulu ke konstruktor standar `OpenAI` / `AsyncOpenAI`. Konstruktor khusus Azure sudah deprecated di `openai>=1.108.1`.

### Mengapa jalur API v1?

Endpoint baru `/openai/v1` menggunakan klien standar `OpenAI()` bukan `AzureOpenAI()`, tidak memerlukan parameter `api_version`, dan bekerja sama di OpenAI dan Azure OpenAI. Kode klien sama ini tahan masa depan — tidak perlu manajemen versi.

### Perubahan utama

| Sebelumnya | Sesudah |
|----------|---------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Hapus sepenuhnya |

### Checklist pembersihan

- Hapus argumen `api_version` dari konstruksi klien.
- Hapus variabel lingkungan `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` dari `.env`, pengaturan aplikasi, dan file Bicep/infra.
- Ganti nama `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` di `.env`, pengaturan aplikasi, Bicep/infra, dan fixture tes (konvensi standar Azure Identity SDK).
- Pastikan `openai>=1.108.1` di `requirements.txt` atau `pyproject.toml`.

### Migrasi variabel lingkungan

| Env var lama | Tindakan | Catatan |
|-------------|----------|---------|
| `AZURE_OPENAI_VERSION` | **Hapus** | Tidak perlu `api_version` dengan endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Hapus** | Sama seperti di atas |
| `AZURE_OPENAI_CLIENT_ID` | **Ganti nama** → `AZURE_CLIENT_ID` | Konvensi standar Azure Identity SDK untuk `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Tetap** | Masih diperlukan untuk konstruksi `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Tetap** | Digunakan sebagai parameter `model` di `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Tetap** | Digunakan sebagai `api_key` untuk autentikasi berbasis kunci |

Contoh kode setup klien (sinkron, asinkron, EntraID, API key, multi-tenant), lihat [cheat-sheet.md](./references/cheat-sheet.md).

---

## Langkah 1: Deteksi Lokasi Panggilan Lama

Jalankan skrip [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) untuk menemukan semua lokasi panggilan yang perlu migrasi:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Atau jalankan pencarian ini secara manual — setiap kecocokan adalah target migrasi:

```bash
# Panggilan API warisan (harus ditulis ulang)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Konstruktor klien Azure yang sudah tidak digunakan (harus diganti)
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

# Parameter yang sudah tidak digunakan (harus dihapus atau diganti nama)
rg "response_format"
rg "max_tokens\b"        # ganti nama menjadi max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Variabel lingkungan yang sudah tidak digunakan (bersihkan)
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

# Akses badan kesalahan filter konten (harus diperbarui — struktur berubah)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # bentuk tunggal lama — sekarang content_filter_results (jamak) di dalam array content_filters

# Panggilan HTTP mentah ke endpoint Chat Completions (harus memperbarui URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristik (deteksi dan tulis ulang)

- **Klien Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Konstruktor klien Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Alat**: konversi definisi alat pemanggil fungsi dari format bersarang (`{"type": "function", "function": {"name": ...}}`) menjadi format datar Responses (`{"type": "function", "name": ...}`); gunakan `tool_choice`; kembalikan hasil alat sebagai item `{"type": "function_call_output", "call_id": ..., "output": ...}` (bukan `{"role": "tool", ...}`).
- **Putaran alat**: ketika model mengembalikan panggilan fungsi, tambahkan item `response.output` ke percakapan (bukan dict manual `{"role": "assistant", "tool_calls": [...]}`), lalu tambahkan item `function_call_output` untuk setiap hasil.
- **Contoh alat few-shot**: jika percakapan menyertakan contoh panggilan alat yang dikodekan keras, ubah menjadi item `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID harus diawali dengan `fc_`.
- **`pydantic_function_tool()`**: helper ini masih menghasilkan format bersarang lama dan **tidak kompatibel** dengan `responses.create()`. Ganti dengan definisi alat manual atau pembungkus perataan.
- **Multi-turn**: pertahankan riwayat percakapan di aplikasi; teruskan giliran sebelumnya melalui item `input`.
- **Format**: gantikan `response_format` tingkat atas Chat dengan `text.format` dalam Responses. Bentuk kanonik: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Item konten**: gantikan `content[].type: "text"` Chat dengan `content[].type: "input_text"` Responses untuk giliran pengguna/sistem.
- **Item konten gambar**: gantikan `content[].type: "image_url"` Chat dengan `content[].type: "input_image"` Responses. Field `image_url` berubah dari objek bersarang `{"url": "..."}` menjadi string datar. Lihat lembar contekan untuk contoh sebelum/sesudah.
- **Upaya penalaran**: **hanya migrasikan `reasoning` jika sudah ada di kode asli**.
- **Penanganan error penyaring konten**: struktur badan error berubah. Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]` (tunggal); Responses API menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, di dalam array). Kode yang mengakses `innererror` akan memunculkan `KeyError`. Ubah untuk menggunakan jalur baru.
- **Panggilan HTTP mentah**: jika aplikasi memanggil REST API Azure OpenAI secara langsung (via `requests`, `httpx`, dll.) menggunakan `/openai/deployments/{name}/chat/completions?api-version=...`, ubah menjadi `/openai/v1/responses`. Body permintaan berubah: `messages` → `input`, tambahkan `max_output_tokens` dan `store: false`, hilangkan parameter query `api-version`. Body respons berubah: `choices[0].message.content` → `output[0].content[0].text` (catatan: `output_text` adalah properti kemudahan SDK yang tidak terdapat dalam JSON REST mentah).

---

## Langkah 2: Terapkan Migrasi

### Catatan migrasi (Chat Completions → Responses)

- **Mengapa migrasi**: Responses adalah API terpadu untuk teks, alat, dan streaming; Chat Completions adalah legacy. Dengan GPT-5, Responses diperlukan untuk kinerja terbaik.
- **HTTP**: endpoint Azure berganti dari `/openai/deployments/{name}/chat/completions` menjadi `/openai/v1/responses`.
- **Field**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` tetap.
- **Format**: `response_format` → `text.format` dengan objek yang sesuai.
- **Item konten**: Gantikan `content[].type: "text"` Chat dengan `content[].type: "input_text"` Responses untuk giliran sistem/pengguna.
- **Item konten gambar**: Gantikan `content[].type: "image_url"` Chat dengan `content[].type: "input_image"` Responses. Ratakan field `image_url` dari `{"image_url": {"url": "..."}}` menjadi `{"image_url": "..."}` (string polos — baik URL HTTPS atau URI data `data:image/...;base64,...`).

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
| `store` | `store` (diset ke `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (string datar) |

Untuk contoh kode lengkap sebelum/sesudah, lihat [cheat-sheet.md](./references/cheat-sheet.md).

Untuk migrasi infrastruktur pengujian (mock, snapshot, assertion), lihat [test-migration.md](./references/test-migration.md).

Untuk pemecahan masalah error dan permasalahan, lihat [troubleshooting.md](./references/troubleshooting.md).

---

## Retensi Data & Status

- Setel `store: false` pada semua permintaan Responses.
- Jangan mengandalkan ID pesan sebelumnya atau konteks yang disimpan server; kelola status klien secara lokal dan minimalkan metadata.

---

## Kriteria Penerimaan

### Gerbang tingkat kode (semua harus lolos)

- [ ] Nol hasil pencarian untuk `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` di file yang sudah dimigrasi.
- [ ] Nol hasil pencarian untuk `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — semua konstruktor menggunakan `OpenAI`/`AsyncOpenAI` dengan endpoint v1.
- [ ] Nol hasil pencarian untuk `rg "models\.github\.ai|models\.inference\.ai\.azure"` — jalur kode Model GitHub dihapus.
- [ ] Nol hasil pencarian untuk `rg "OpenAIChatCompletionClient"` — kode MAF 1.0.0+ menggunakan `OpenAIChatClient` (yang menggunakan Responses API). Untuk pre-1.0.0, upgrade ke `agent-framework-openai>=1.0.0`.
- [ ] Semua panggilan `ChatOpenAI(...)` mencantumkan `use_responses_api=True`.
- [ ] Nol hasil pencarian untuk `rg "choices\[0\]"` — semua akses respons menggunakan `resp.output_text` atau skema output Responses.
- [ ] Tidak ada `response_format` tingkat atas; semua output terstruktur menggunakan `text={"format": {...}}`.
- [ ] `openai>=1.108.1` dan `azure-identity` ada di `requirements.txt` atau `pyproject.toml`; dependensi sudah diinstal ulang.
- [ ] `store=False` disetel di setiap panggilan `responses.create`.
- [ ] Tidak ada `api_version` dalam konstruksi klien; `AZURE_OPENAI_API_VERSION` dihapus dari file env dan infrastruktur.

### Gerbang infrastruktur pengujian (semua harus lolos)

- [ ] Nol hasil pencarian untuk `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Nol hasil pencarian untuk `rg "_azure_ad_token_provider" tests/` — assertion diperbarui untuk memeriksa `isinstance(client, AsyncOpenAI)` atau `base_url`.
- [ ] Nol hasil pencarian untuk `rg "prompt_filter_results|content_filter_results" tests/` — mock filter khusus Azure dihapus.
- [ ] Fixture mock menggunakan `kwargs.get("input")` bukan `kwargs.get("messages")`.
- [ ] Snapshot/golden file diperbarui menjadi bentuk streaming Responses (tanpa `choices[0]`, `function_call`, `logprobs`, dll.).
- [ ] `pytest` lulus tanpa error setelah semua pembaruan pengujian.

### Gerbang perilaku (verifikasi manual atau melalui perangkat uji)

- [ ] **Penyelesaian dasar**: `responses.create` non-streaming mengembalikan `output_text` tidak kosong.
- [ ] **Paritas streaming**: jika kode asli menggunakan streaming, kode migrasi melakukan streaming dan menghasilkan event `response.output_text.delta` dengan delta tidak kosong.
- [ ] **Output terstruktur**: jika menggunakan `text.format` dengan `json_schema`, `json.loads(resp.output_text)` berhasil dan sesuai skema.
- [ ] **Loop pemanggilan alat**: jika menggunakan alat, model melakukan panggilan alat, aplikasi mengeksekusi, dan permintaan lanjutan mengembalikan `output_text` final (tidak terjadi loop tak berujung).
- [ ] **Paritas Async**: jika menggunakan `AsyncAzureOpenAI`, ekuivalennya `AsyncOpenAI` bekerja dengan `await`.
- [ ] **Tingkat error**: tidak terjadi error 400/401/404 baru dibanding baseline sebelum migrasi.

### Deliverables

- Ringkasan mencakup file yang diedit, hitungan lokasi panggilan legacy sebelum/sesudah, dan langkah berikutnya.
- Perubahan hanya pengeditan pohon kerja (tidak ada commit).

---

## Persyaratan Versi SDK

| Paket | Versi Minimum |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Terbaru (untuk autentikasi EntraID) |

---

## Referensi

- [Lembar Contekan — semua potongan kode](./references/cheat-sheet.md)
- [Migrasi Pengujian — mock, snapshot, assertion](./references/test-migration.md)
- [Pemecahan Masalah — error, tabel risiko, permasalahan](./references/troubleshooting.md)
- [detect_legacy.py — pemindai otomatis](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Dokumentasi API Azure OpenAI Responses](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Siklus hidup versi API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Referensi API OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->