---
name: azure-openai-to-responses
license: MIT
description: 'Migrasi aplikasi Python dari Azure OpenAI Chat Completions ke Responses
  API. Meliputi migrasi klien AzureOpenAI/AsyncAzureOpenAI ke endpoint v1, penstriman,
  alat, output berstruktur, multi-sesi, pengesahan EntraID, dan pemeriksaan keserasian
  model. Berfokus pada Python dan khusus untuk Azure OpenAI. GUNA UNTUK: migrasi ke
  responses API, bertukar dari chat completions, openai responses, peningkatan openai
  SDK, migrasi responses API, berpindah dari completions ke responses, migrasi gpt-5,
  migrasi python azure openai, chat completions ke responses, AzureOpenAI ke klien
  OpenAI, peningkatan python azure openai. JANGAN GUNA UNTUK: membina aplikasi baru
  dari awal (mulakan terus dengan responses), migrasi Node/TypeScript/C#/Java/Go (kemahiran
  ini hanya untuk Python), persediaan infrastruktur Azure (guna azure-prepare), penyebaran
  model (guna microsoft-foundry).'
---
# Migrasi Aplikasi Python daripada Azure OpenAI Chat Completions ke Responses API

> **PANDUAN BERWIBAWA — IKUTI DENGAN TEPAT**
>
> Kemahiran ini memindahkan pangkalan kod Python yang menggunakan Azure OpenAI Chat Completions
> ke Responses API yang bersatu. Ikuti arahan ini dengan tepat.
> Jangan mengubah suai pemetaan parameter atau mencipta bentuk API baru.

---

## Pencetus

Aktifkan kemahiran ini apabila pengguna ingin:
- Memindahkan aplikasi Python daripada Azure OpenAI Chat Completions ke Responses API
- Meningkatkan penggunaan SDK OpenAI Python ke bentuk API terkini dengan Azure OpenAI
- Menyediakan kod Python untuk model GPT-5 atau yang lebih baru yang memerlukan Responses di Azure
- Beralih dari `AzureOpenAI`/`AsyncAzureOpenAI` ke klien standard `OpenAI`/`AsyncOpenAI` dengan titik akhir v1
- Memperbaiki amaran deprecasi berkaitan konstruktor `AzureOpenAI` atau `api_version`

---

## ⚠️ Keserasian Model — PERIKSA DULU

> **Sebelum migrasi, sahkan penyebaran Azure OpenAI anda menyokong Responses API.**

### 1. Ujian ringkas penyebaran anda (pantas)

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

> **Nota**: `max_output_tokens` mempunyai **minimum 16** di Azure OpenAI. Nilai di bawah 16 akan menghasilkan ralat 400. Gunakan 50+ untuk ujian ringkas.

Jika ini mengembalikan 404, model penyebaran tidak menyokong Responses lagi — semak rujukan di bawah atau lakukan penyebaran semula dengan model yang disokong.

### 2. Semak model tersedia di rantau anda (disyorkan)

Jalankan alat keserasian model terbina dalam untuk melihat apa yang tersedia dengan sokongan Responses API di rantau anda:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Ini mengquery ARM Azure secara langsung dan menunjukkan matriks keserasian — model mana yang menyokong Responses, output berstruktur, alat, dan lain-lain. Gunakan `--filter gpt-5.1,gpt-5.2` untuk mengehadkan hasil atau `--json` untuk skrip.

### 3. Rujukan lengkap sokongan model

- **Query langsung**: `python migrate.py models` (lihat di atas — khusus rantau, sentiasa terkini)
- **Layari ketersediaan**: [Jadual ringkasan model dan ketersediaan rantau](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Mula cepat & panduan**: **https://aka.ms/openai/start**

### ⚠️ Had model lama

> **AMARAN**: Model lama (yang lebih tua daripada `gpt-4.1`) mungkin tidak menyokong semua ciri Responses API sepenuhnya.
>
> Had yang diketahui dengan model lama:
> - **Parameter `reasoning`**: Tidak disokong oleh banyak model bukan beralasan. Hanya migrasi `reasoning` jika sudah wujud dalam kod asal.
> - **Parameter `seed`**: Tidak disokong langsung dalam Responses API — keluarkan dari semua permintaan.
> - **Output berstruktur melalui `text.format`**: Model lama mungkin tidak menguatkuasakan skema JSON `strict: true` dengan stabil.
> - **Pengurusan alat**: GPT-5+ menguruskan panggilan alat sebagai sebahagian daripada alasan dalaman. Model lama pada Responses masih berfungsi tetapi tiada integrasi mendalam ini.
> - **Had suhu**: Apabila migrasi ke `gpt-5`, suhu mesti tidak dimasukkan atau ditetapkan kepada `1`. Model lama tiada had sebegini.

### Model beralasan siri O (o1, o3-mini, o3, o4-mini)

Model siri O mempunyai had parameter unik. Apabila migrasi aplikasi yang mensasarkan model siri O:

- **`temperature`**: Mesti `1` (atau tidak dimasukkan). Model siri O tidak menerima nilai lain.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikasi yang menggunakan `max_completion_tokens` khusus Azure mesti bertukar ke `max_output_tokens`. Tetapkan nilai tinggi (4096+) kerana token beralasan dikira dalam had.
- **`reasoning_effort`**: Jika aplikasi menggunakan `reasoning_effort` (rendah/sederhana/tinggi), kekalkan — Responses API menyokong parameter ini untuk model siri O.
- **Tingkah laku streaming**: Model siri O mungkin menyimpan output sehingga alasan selesai sebelum mengeluarkan acara delta teks. Streaming masih berfungsi, tetapi `response.output_text.delta` pertama mungkin tiba lewat berbanding model GPT.
- **`top_p`**: Tidak disokong pada siri O — keluarkan jika ada.
- **Penggunaan alat**: Model siri O menyokong alat melalui Responses API sama seperti model GPT, tetapi kualiti pengurusan panggilan alat berbeza mengikut model.

**Tindakan — nasihat model proaktif**: Semasa fasa imbasan, periksa model yang dituju aplikasi (nama penyebaran, pembolehubah persekitaran, konfigurasi). Jika model lebih tua daripada `gpt-4.1` (bukan gpt-4.1+), beritahu pengguna secara proaktif:
- Migrasi akan berfungsi untuk teks asas, chat, streaming, dan alat pada model semasa mereka.
- Model terbaru (`gpt-5.1`, `gpt-5.2`) menawarkan pengurusan alat lebih baik, penguatkuasaan output berstruktur, beralasan, dan ketersediaan merentas rantau.
- Mereka patut pertimbangkan untuk menaik taraf penyebaran apabila bersedia — ia tidak menghalang migrasi.

Jangan halang atau tolak migrasi berdasarkan versi model. Nasihat adalah untuk maklumat sahaja.

### GitHub Models TIDAK menyokong Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) tidak menyokong Responses API.**

Jika pangkalan kod ada laluan kod GitHub Models (cari `base_url` yang menunjuk ke `models.github.ai` atau `models.inference.ai.azure.com`), **buang sepenuhnya** semasa migrasi. Responses API memerlukan Azure OpenAI, OpenAI, atau titik akhir tempatan yang serasi (contohnya, Ollama dengan sokongan Responses).

Tindakan semasa imbasan:
- Tandakan mana-mana laluan kod GitHub Models untuk dikeluarkan.

---

## Migrasi Kerangka Kerja

Banyak aplikasi menggunakan kerangka kerja peringkat tinggi di atas OpenAI. Apabila memigrasi ini, perubahan API kerangka kerja sendiri — bukan hanya panggilan OpenAI asas.

### Microsoft Agent Framework (MAF)

**Periksa versi MAF anda dahulu** — migrasi bergantung sama ada anda pada MAF 1.0.0+ atau beta/rc sebelum 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **sudah menggunakan Responses API** — tiada migrasi diperlukan. Jika pangkalan kod menggunakan `OpenAIChatCompletionClient` warisan (yang menggunakan `chat.completions.create`), gantikan dengan `OpenAIChatClient`.

| Sebelum | Selepas |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Untuk periksa versi anda: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF sebelum 1.0.0 (rilis beta/rc)

Pada MAF sebelum 1.0.0, `OpenAIChatClient` menggunakan Chat Completions. Tingkatkan ke `agent-framework-openai>=1.0.0` di mana `OpenAIChatClient` menggunakan Responses API secara lalai.

Tiada perubahan lain diperlukan — API `Agent` dan alat kekal sama.

### LangChain (`langchain-openai`)

Tambah `use_responses_api=True` ke `ChatOpenAI()`. Juga kemas kini akses respons daripada `.content` ke `.text`.

| Sebelum | Selepas |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Untuk contoh kod lengkap sebelum/selepas, lihat [cheat-sheet.md](./references/cheat-sheet.md).

---

## Panduan Migrasi Frontend

> **Responses API adalah perkara sisi pelayan.** Migrasikan backend Python anda; kontrak HTTP frontend harus kekal tidak berubah kecuali backend anda hanya laluan nipis — dalam kes itu, pertimbangkan menggunakan bentuk permintaan Responses untuk menghapuskan lapisan terjemahan. Jika frontend memanggil OpenAI secara langsung dengan kunci sisi klien, alihkan panggilan itu ke backend terlebih dahulu.

### Deprecation `@microsoft/ai-chat-protocol`

Pakej npm `@microsoft/ai-chat-protocol` sudah usang dan perlu digantikan dengan [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Jika anda menjumpainya di frontend:

1. Gantikan tag skrip CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Keluarkan instansiasi `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Gantikan `client.getStreamedCompletion(messages)` dengan panggilan `fetch()` terus ke titik akhir streaming backend.
4. Gantikan `for await (const response of result)` dengan `for await (const chunk of readNDJSONStream(response.body))`.
5. Kemas kini akses sifat daripada `response.delta.content` / `response.error` ke `chunk.delta.content` / `chunk.error`.

---

## Matlamat

- Senaraikan semua tapak panggilan Python yang menggunakan Chat Completions atau Completions warisan terhadap Azure OpenAI.
- Cadangkan pelan migrasi dan susunan untuk pangkalan kod Python.
- Buat suntingan selamat dan minimum untuk beralih ke Responses API.
- Kemas kini pemanggil untuk menggunakan skema output Responses; tiada pembungkus keserasian belakang.
- Jalankan ujian/lint; baiki kerosakan kecil yang diperkenalkan oleh migrasi.
- Sediakan set perubahan kecil yang boleh dikaji dan berikan ringkasan akhir dengan perbezaan (jangan komit).

---

## Panduan Keselamatan

- Hanya ubah fail dalam ruang kerja git. Jangan tulis luar ruang kerja.
- Jangan simpan shim keserasian belakang; migrasi kod ke bentuk API baru.
- Jangan tinggalkan komen peralihan/tanda kubur atau fail sandaran.
- Kekalkan semantik streaming jika sebelum ini digunakan; jika tidak, guna bukan streaming.
- Minta kelulusan sebelum menjalankan arahan atau panggilan rangkaian jika dalam mod kelulusan.
- Jangan jalankan `git add`/`git commit`/`git push`; hasilkan suntingan pokok kerja sahaja.

---

## Langkah 0: Migrasi Klien Azure OpenAI (Prasyarat)

Jika pangkalan kod menggunakan konstruktor `AzureOpenAI` atau `AsyncAzureOpenAI`, migrasi ke konstruktor standard `OpenAI` / `AsyncOpenAI` terlebih dahulu. Konstruktor khusus Azure ini sudah usang dalam `openai>=1.108.1`.

### Mengapa laluan API v1?

Titik akhir baru `/openai/v1` menggunakan klien standard `OpenAI()` dan bukan `AzureOpenAI()`, tidak memerlukan parameter `api_version`, dan berfungsi sama rata di OpenAI dan Azure OpenAI. Kod klien yang sama ini tahan masa depan — tiada pengurusan versi diperlukan.

### Perubahan penting

| Sebelum | Selepas |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Keluarkan sepenuhnya |

### Senarai semak pembersihan

- Keluarkan argumen `api_version` daripada konstruktor klien.
- Keluarkan pembolehubah persekitaran `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` dari `.env`, tetapan aplikasi, dan fail Bicep/infra.
- Namakan semula `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` dalam `.env`, tetapan aplikasi, Bicep/infra, dan fixtur ujian (konvensyen SDK Identiti Azure standard).
- Pastikan `openai>=1.108.1` dalam `requirements.txt` atau `pyproject.toml`.

### Migrasi pembolehubah persekitaran

| Pembolehubah lama | Tindakan | Nota |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Keluarkan** | Tiada `api_version` diperlukan dengan titik akhir v1 |
| `AZURE_OPENAI_API_VERSION` | **Keluarkan** | Sama seperti di atas |
| `AZURE_OPENAI_CLIENT_ID` | **Namakan semula** → `AZURE_CLIENT_ID` | Konvensyen SDK Identiti Azure standard untuk `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Simpan** | Masih diperlukan untuk pembinaan `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Simpan** | Digunakan sebagai parameter `model` dalam `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Simpan** | Digunakan sebagai `api_key` untuk pengesahan berasaskan kunci |

Untuk contoh kod penyediaan klien (sync, async, EntraID, kunci API, berbilang penyewa), lihat [cheat-sheet.md](./references/cheat-sheet.md).

---

## Langkah 1: Kenal Pasti Tapak Panggilan Warisan

Jalankan skrip [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) untuk mencari semua tapak panggilan yang perlu dimigrasi:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Atau jalankan carian ini secara manual — setiap padanan adalah sasaran migrasi:

```bash
# Panggilan API Legacy (perlu tulis semula)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Pembina klien Azure yang telah usang (perlu gantikan)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Corak akses bentuk respons (perlu kemas kini)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definisi alat dalam format bertingkat lama (perlu ratakan)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Keputusan alat dalam format lama (perlu tukar kepada function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Parameter yang telah usang (perlu keluarkan atau tukar nama)
rg "response_format"
rg "max_tokens\b"        # tukar nama kepada max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Pembolehubah persekitaran yang telah usang (bersihkan)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # sepatutnya AZURE_CLIENT_ID

# Titik hujung Model GitHub (perlu keluarkan — API Respons tidak disokong)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Corak legacy tahap rangka kerja (perlu kemas kini)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: gantikan dengan OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: perlu use_responses_api=True

# Infrastruktur ujian (perlu kemas kini)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Akses badan ralat penapis kandungan (perlu kemas kini — struktur telah berubah)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # bentuk tunggal lama — sekarang content_filter_results (jamak) di dalam tatasusunan content_filters

# Panggilan HTTP mentah ke titik hujung Chat Completions (perlu kemas kini URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristik (mengesan dan menulis semula)

- **Klien Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Pembina klien Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Alat**: tukar definisi alat panggilan fungsi daripada format bersarang (`{"type": "function", "function": {"name": ...}}`) ke format Respon rata (`{"type": "function", "name": ...}`); guna `tool_choice`; pulangkan hasil alat sebagai item `{"type": "function_call_output", "call_id": ..., "output": ...}` (bukan `{"role": "tool", ...}`).
- **Pusingan alat**: apabila model memulangkan panggilan fungsi, tambah item `response.output` ke perbualan (bukan kamus manual `{"role": "assistant", "tool_calls": [...]}`), kemudian tambah item `function_call_output` untuk setiap hasil.
- **Contoh alat tembakan sedikit**: jika perbualan termasuk contoh panggilan alat keras kod, tukar kepada item `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID mesti bermula dengan `fc_`.
- **`pydantic_function_tool()`**: pembantu ini masih menjana format bersarang lama dan **tidak serasi** dengan `responses.create()`. Gantikan dengan definisi alat manual atau pembungkus pemesejan.
- **Multi-pusingan**: kekalkan sejarah perbualan dalam aplikasi; hantar pusingan sebelumnya melalui item `input`.
- **Pemformatan**: ganti `response_format` peringkat atas Chat dengan `text.format` dalam Responses. Bentuk kanonik: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Item kandungan**: ganti Chat `content[].type: "text"` dengan Responses `content[].type: "input_text"` untuk pusingan pengguna/sistem.
- **Item kandungan imej**: ganti Chat `content[].type: "image_url"` dengan Responses `content[].type: "input_image"`. Medan `image_url` berubah daripada objek bersarang `{"url": "..."}` menjadi rentetan rata. Lihat helaian cheat untuk contoh sebelum/selepas.
- **Usaha penalaran**: **hanya migrasikan `reasoning` jika ia sudah wujud dalam kod asal**.
- **Pengendalian ralat penapis kandungan**: struktur badan ralat berubah. Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]` (tunggal); Respon API menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, dalam tatasusunan). Kod yang mengakses `innererror` akan menaikkan `KeyError`. Tulis semula untuk menggunakan laluan baru.
- **Panggilan HTTP mentah**: jika aplikasi memanggil Azure OpenAI REST API secara langsung (melalui `requests`, `httpx`, dll.) menggunakan `/openai/deployments/{name}/chat/completions?api-version=...`, tulis semula kepada `/openai/v1/responses`. Badan permintaan berubah: `messages` → `input`, tambah `max_output_tokens` dan `store: false`, keluarkan param kueri `api-version`. Badan tindak balas berubah: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` adalah sifat kemudahan SDK yang tiada dalam JSON REST mentah).

---

## Langkah 2: Terapkan Migrasi

### Nota migrasi (Chat Completions → Responses)

- **Kenapa migrasi**: Responses adalah API bersatu untuk teks, alat, dan penstriman; Chat Completions adalah warisan. Dengan GPT-5, Responses diperlukan untuk prestasi terbaik.
- **HTTP**: titik akhir Azure beralih daripada `/openai/deployments/{name}/chat/completions` kepada `/openai/v1/responses`.
- **Medan**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` kekal.
- **Pemformatan**: `response_format` → `text.format` dengan objek yang sesuai.
- **Item kandungan**: Gantikan Chat `content[].type: "text"` dengan Responses `content[].type: "input_text"` untuk pusingan sistem/pengguna.
- **Item kandungan imej**: Gantikan Chat `content[].type: "image_url"` dengan Responses `content[].type: "input_image"`. Ratakan medan `image_url` daripada `{"image_url": {"url": "..."}}` kepada `{"image_url": "..."}` (rentetan biasa — sama ada URL HTTPS atau URI data `data:image/...;base64,...`).

### Rujukan pemadanan parameter

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (susunan item) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objek) |
| `temperature` | `temperature` (tidak berubah) |
| `stop` | `stop` (tidak berubah) |
| `frequency_penalty` | `frequency_penalty` (tidak berubah) |
| `presence_penalty` | `presence_penalty` (tidak berubah) |
| `tools` / panggilan fungsi | `tools` (tidak berubah) |
| `seed` | **Buang** (tidak disokong) |
| `store` | `store` (tetapkan kepada `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (rentetan rata) |

Untuk contoh kod lengkap sebelum/selepas, lihat [cheat-sheet.md](./references/cheat-sheet.md).

Untuk migrasi infrastruktur ujian (mock, snapshot, penegasan), lihat [test-migration.md](./references/test-migration.md).

Untuk penyelesaian masalah ralat dan masalah biasa, lihat [troubleshooting.md](./references/troubleshooting.md).

---

## Penyimpanan Data & Keadaan

- Tetapkan `store: false` pada semua permintaan Responses.
- Jangan bergantung pada ID mesej sebelumnya atau konteks yang disimpan pelayan; urus keadaan secara klien dan minimakan metadata.

---

## Kriteria Penerimaan

### Pintu aras kod (semua mesti lulus)

- [ ] Tiada padanan untuk `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` dalam fail yang telah dimigrasi.
- [ ] Tiada padanan untuk `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — semua pembina guna `OpenAI`/`AsyncOpenAI` dengan titik akhir v1.
- [ ] Tiada padanan untuk `rg "models\.github\.ai|models\.inference\.ai\.azure"` — laluan kod Model GitHub dibuang.
- [ ] Tiada padanan untuk `rg "OpenAIChatCompletionClient"` — kod MAF 1.0.0+ guna `OpenAIChatClient` (yang guna Responses API). Dalam pra-1.0.0, naik taraf kepada `agent-framework-openai>=1.0.0`.
- [ ] Semua panggilan `ChatOpenAI(...)` sertakan `use_responses_api=True`.
- [ ] Tiada padanan untuk `rg "choices\[0\]"` — semua akses respons guna `resp.output_text` atau skema output Responses.
- [ ] Tiada `response_format` di peringkat atas; semua output berstruktur guna `text={"format": {...}}`.
- [ ] `openai>=1.108.1` dan `azure-identity` dalam `requirements.txt` atau `pyproject.toml`; kebergantungan dipasang semula.
- [ ] `store=False` ditetapkan pada setiap panggilan `responses.create`.
- [ ] Tiada `api_version` dalam pembinaan klien; `AZURE_OPENAI_API_VERSION` dibuang dari fail persekitaran dan infrastruktur.

### Pintu infrastruktur ujian (semua mesti lulus)

- [ ] Tiada padanan untuk `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Tiada padanan untuk `rg "_azure_ad_token_provider" tests/` — penegasan diubah untuk periksa `isinstance(client, AsyncOpenAI)` atau `base_url`.
- [ ] Tiada padanan untuk `rg "prompt_filter_results|content_filter_results" tests/` — mock penapis khusus Azure dibuang.
- [ ] Mock fixture guna `kwargs.get("input")` bukan `kwargs.get("messages")`.
- [ ] Fail snapshot / emas dikemas kini kepada bentuk penstriman Responses (tiada `choices[0]`, `function_call`, `logprobs`, dll.).
- [ ] `pytest` lulus tanpa kegagalan selepas semua kemas kini ujian.

### Pintu kelakuan (sahkan secara manual atau melalui hab ujian)

- [ ] **Lengkap asas**: `responses.create` tanpa penstriman pulangkan `output_text` tidak kosong.
- [ ] **Kesetaraan penstriman**: jika kod asal guna penstriman, kod migrasi menstrim dan hasilkan acara `response.output_text.delta` dengan delta tidak kosong.
- [ ] **Output berstruktur**: jika guna `text.format` dengan `json_schema`, `json.loads(resp.output_text)` berjaya dan padan dengan skema.
- [ ] **Gelung panggilan alat**: jika alat digunakan, model keluarkan panggilan alat, aplikasi laksanakan, dan permintaan susulan pulangkan `output_text` akhir (tiada gelung tanpa henti).
- [ ] **Kesetaraan Async**: jika `AsyncAzureOpenAI` digunakan, yang setara `AsyncOpenAI` berfungsi dengan `await`.
- [ ] **Kadar ralat**: tiada ralat 400/401/404 baru berbanding garisan asas pra-migrasi.

### Hasil Dihantar

- Ringkasan termasuk fail yang diedit, kiraan tapak panggilan warisan sebelum/selepas, dan langkah seterusnya.
- Perubahan adalah suntingan pokok kerja sahaja (tiada komit).

---

## Keperluan Versi SDK

| Pek | Versi Minimum |
|----|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Terkini (untuk pengesahan EntraID) |

---

## Rujukan

- [Helaian Cheat — semua petikan kod](./references/cheat-sheet.md)
- [Migrasi Ujian — mock, snapshot, penegasan](./references/test-migration.md)
- [Penyelesaian Masalah — ralat, jadual risiko, halangan](./references/troubleshooting.md)
- [detect_legacy.py — pengimbas automatik](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Kit Permulaan Azure OpenAI](https://aka.ms/openai/start)
- [Dokumen Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Kitar Hayat Versi API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Rujukan OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->