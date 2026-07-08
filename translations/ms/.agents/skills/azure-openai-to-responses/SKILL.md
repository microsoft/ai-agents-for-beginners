---
name: azure-openai-to-responses
license: MIT
description: 'Migrasi aplikasi Python dari Azure OpenAI Chat Completions ke Responses
  API. Meliputi migrasi klien AzureOpenAI/AsyncAzureOpenAI ke titik akhir v1, penstriman,
  alat, keluaran berstruktur, pelbagai pusingan, pengesahan EntraID, dan pemeriksaan
  keserasian model. Fokus pada Python, khusus Azure OpenAI. GUNA UNTUK: migrasi ke
  responses API, bertukar dari chat completions, openai responses, naik taraf SDK
  openai, migrasi responses API, pindah dari completions ke responses, migrasi gpt-5,
  migrasi python azure openai, chat completions ke responses, AzureOpenAI ke OpenAI
  client, naik taraf python azure openai. JANGAN GUNA UNTUK: membina aplikasi baru
  dari awal (mula terus dengan responses), migrasi Node/TypeScript/C#/Java/Go (kemahiran
  ini khusus Python sahaja), penyediaan infrastruktur Azure (guna azure-prepare),
  penyebaran model (guna microsoft-foundry).'
---
# Migrasi Aplikasi Python dari Azure OpenAI Chat Completions ke Responses API

> **PANDUAN AUTORITATIF — IKUTI DENGAN TEPAT**
>
> Kemahiran ini memindahkan pangkalan kod Python yang menggunakan Azure OpenAI Chat Completions
> ke Responses API yang bersatu. Ikuti arahan ini dengan tepat.
> Jangan mengubah pemetaan parameter atau mereka bentuk API.

---

## Pencetus

Aktifkan kemahiran ini apabila pengguna ingin:
- Memindahkan aplikasi Python dari Azure OpenAI Chat Completions ke Responses API
- Meningkatkan penggunaan SDK OpenAI Python ke bentuk API terkini terhadap Azure OpenAI
- Menyediakan kod Python untuk model GPT-5 atau terbaru yang memerlukan Responses pada Azure
- Beralih dari `AzureOpenAI`/`AsyncAzureOpenAI` ke klien standard `OpenAI`/`AsyncOpenAI` dengan endpoint v1
- Memperbaiki amaran nyahgunaan berkaitan konstruktor `AzureOpenAI` atau `api_version`

---

## ⚠️ Keserasian Model — SEMAK DAHULU

> **Sebelum memigrasi, sahkan penyebaran Azure OpenAI anda menyokong Responses API.**

### 1. Ujian asap penyebaran anda (paling pantas)

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

> **Nota**: `max_output_tokens` mempunyai **minimum 16** pada Azure OpenAI. Nilai di bawah 16 akan memberikan ralat 400. Gunakan 50+ untuk ujian asap.

Jika ini memulangkan 404, model penyebaran belum menyokong Responses — semak rujukan di bawah atau pasang semula dengan model yang disokong.

### 2. Semak model tersedia di rantau anda (disyorkan)

Jalankan alat keserasian model terbina dalam untuk melihat apa yang tersedia dengan sokongan Responses API dalam rantau khusus anda:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Ini menjalankan pertanyaan langsung Azure ARM dan menunjukkan matriks keserasian — model yang menyokong Responses, output berstruktur, alatan, dan lain-lain. Gunakan `--filter gpt-5.1,gpt-5.2` untuk menyempitkan keputusan atau `--json` untuk penulisan skrip.

### 3. Rujukan sokongan model penuh

- **Pertanyaan langsung**: `python migrate.py models` (lihat di atas — khusus rantau, sentiasa terkini)
- **Layari ketersediaan**: [Jadual ringkasan model dan ketersediaan rantau](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Panduan & permulaan pantas**: **https://aka.ms/openai/start**

### ⚠️ Had model lama

> **AMARAN**: Model lama (contohnya, `gpt-4o`, `gpt-4`) mungkin tidak menyokong sepenuhnya semua ciri Responses API.
>
> Had diketahui dengan model lama:
> - **parameter `reasoning`**: Tidak disokong pada `gpt-4o-mini`, `gpt-4o`, dan banyak model tanpa reasoning. Hanya migrasi `reasoning` jika sudah wujud dalam kod asal.
> - **parameter `seed`**: Tidak disokong langsung dalam Responses API — buang dari semua permintaan.
> - **Output berstruktur melalui `text.format`**: Model lama mungkin tidak menguatkuasakan skema JSON `strict: true` dengan boleh dipercayai.
> - **Orkestrasi alat**: GPT-5+ mengorkestrasi panggilan alat sebagai sebahagian daripada reasoning dalaman. Model lama di Responses masih berfungsi tetapi tiada integrasi mendalam ini.
> - **Had suhu**: Bila migrasi ke `gpt-5`, suhu mesti dibuang atau ditetapkan ke `1`. Model lama tidak mempunyai had ini.

### Model reasoning siri O (o1, o3-mini, o3, o4-mini)

Model siri O mempunyai had parameter unik. Apabila memigrasi aplikasi yang sasarkan model siri O:

- **`temperature`**: Mesti `1` (atau dibuang). Model siri O tidak menerima nilai lain.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikasi yang menggunakan `max_completion_tokens` khusus Azure mesti bertukar ke `max_output_tokens`. Tetapkan nilai tinggi (4096+) kerana token reasoning dikira dalam had.
- **`reasoning_effort`**: Jika aplikasi menggunakan `reasoning_effort` (rendah/sederhana/tinggi), simpan — Responses API menyokong parameter ini untuk model siri O.
- **Tingkah laku strim**: Model siri O mungkin menyimpan output sehingga reasoning selesai sebelum mengeluarkan acara delta teks. Strim masih berfungsi, tetapi `response.output_text.delta` pertama akan tiba lewat berbanding model GPT.
- **`top_p`**: Tidak disokong pada siri O — buang jika wujud.
- **Penggunaan alat**: Model siri O menyokong alat melalui Responses API sama seperti model GPT, tetapi kualiti orkestrasi panggilan alat berbeza mengikut model.

**Tindakan — nasihat model proaktif**: Semasa fasa imbasan, semak model mana aplikasi sasar (nama penyebaran, pembolehubah persekitaran, konfigurasi). Jika model adalah `gpt-4o` atau lebih lama (bukan gpt-4.1+), beritahu pengguna secara proaktif:
- Migrasi akan berfungsi untuk teks asas, sembang, strim, dan alat pada model semasa mereka.
- Model lebih baru (`gpt-5.1`, `gpt-5.2`) menawarkan orkestrasi alat lebih baik, penguatkuasaan output berstruktur, reasoning, dan ketersediaan rentas rantau.
- Mereka harus mempertimbangkan peningkatan penyebaran bila bersedia — ia tidak menghalang migrasi.

Jangan blok atau tolak migrasi berdasarkan versi model. Nasihat ini hanya maklumat.

### GitHub Models tidak menyokong Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) tidak menyokong Responses API.**

Jika pangkalan kod mempunyai laluan kod GitHub Models (cari `base_url` mengarah ke `models.github.ai` atau `models.inference.ai.azure.com`), **buang sepenuhnya** semasa migrasi. Responses API memerlukan Azure OpenAI, OpenAI, atau endpoint tempatan kompatibel (contohnya, Ollama dengan sokongan Responses).

Tindakan semasa imbas:
- Tandakan mana-mana laluan kod GitHub Models untuk pelupusan.

---

## Migrasi Kerangka Kerja

Banyak aplikasi menggunakan kerangka kerja tingkat tinggi di atas OpenAI. Apabila memigrasi ini, perubahan API kerangka kerja juga perlu — bukan hanya panggilan OpenAI dasar.

### Microsoft Agent Framework (MAF)

**Semak versi MAF anda dahulu** — migrasi bergantung sama ada anda menggunakan MAF 1.0.0+ atau beta/rc sebelum 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **sudah menggunakan Responses API** — tiada migrasi diperlukan. Jika pangkalan kod menggunakan `OpenAIChatCompletionClient` warisan (menggunakan `chat.completions.create`), ganti dengan `OpenAIChatClient`.

| Sebelum | Selepas |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Untuk semak versi anda: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)" `

#### MAF sebelum 1.0.0 (rilis beta/rc)

Dalam MAF sebelum 1.0.0, `OpenAIChatClient` menggunakan Chat Completions. Tingkatkan ke `agent-framework-openai>=1.0.0` yang mana `OpenAIChatClient` menggunakan Responses API secara lalai.

Tiada perubahan lain diperlukan — API `Agent` dan alat kekal sama.

### LangChain (`langchain-openai`)

Tambah `use_responses_api=True` ke `ChatOpenAI()`. Juga kemas kini akses respons dari `.content` ke `.text`.

| Sebelum | Selepas |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Untuk contoh kod lengkap sebelum/selepas, lihat [cheat-sheet.md](./references/cheat-sheet.md).

---

## Panduan Migrasi Frontend

> **Responses API adalah kebimbangan bahagian server.** Migrasikan backend Python anda; kontrak HTTP frontend harus kekal tidak berubah kecuali backend anda hanya bertindak sebagai laluan nipis — dalam kes itu, pertimbangkan untuk menggunakan bentuk permintaan Responses untuk menghapuskan lapisan terjemahan. Jika frontend memanggil OpenAI secara langsung dengan kunci sisi-klien, alihkan panggilan itu ke backend terlebih dahulu.

### Penyahgunaan `@microsoft/ai-chat-protocol`

Pakej npm `@microsoft/ai-chat-protocol` telah disyahguna dan harus digantikan dengan [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Jika anda menjumpainya di frontend:

1. Ganti tag skrip CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Alih keluar penciptaan `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Ganti `client.getStreamedCompletion(messages)` dengan panggilan `fetch()` terus ke endpoint strim backend.
4. Ganti `for await (const response of result)` dengan `for await (const chunk of readNDJSONStream(response.body))`.
5. Kemas kini akses sifat dari `response.delta.content` / `response.error` ke `chunk.delta.content` / `chunk.error`.

---

## Matlamat

- Senaraikan semua lokasi panggilan Python menggunakan Chat Completions atau Completions warisan terhadap Azure OpenAI.
- Cadangkan pelan migrasi dan pengurutan untuk pangkalan kod Python.
- Laksanakan pengubahsuaian selamat dan minimal untuk bertukar ke Responses API.
- Kemas kini pemanggil untuk menggunakan skema output Responses; tiada pembalut keserasian belakang.
- Jalankan ujian/lint; betulkan kerosakan kecil yang diperkenalkan oleh migrasi.
- Sediakan set perubahan kecil yang boleh disemak dan berikan ringkasan akhir dengan perbezaan (jangan komit).

---

## Kawalan Keselamatan

- Hanya ubah fail dalam workspace git. Jangan tulis di luar.
- Jangan kekalkan shims keserasian belakang; migrasikan kod ke bentuk API baru.
- Jangan tinggalkan komen peralihan/tombstone atau fail sandaran.
- Kekalkan semantik strim jika digunakan sebelum ini; jika tidak gunakan tanpa strim.
- Minta kelulusan sebelum menjalankan arahan atau panggilan rangkaian jika dalam mod kelulusan.
- Jangan jalankan `git add`/`git commit`/`git push`; hasilkan edit pokok kerja sahaja.

---

## Langkah 0: Migrasi Klien Azure OpenAI (Prasyarat)

Jika pangkalan kod menggunakan konstruktor `AzureOpenAI` atau `AsyncAzureOpenAI`, migrasikan ke konstruktor standard `OpenAI` / `AsyncOpenAI` terlebih dahulu. Konstruktor khusus Azure ini telah disyahguna dalam `openai>=1.108.1`.

### Mengapa laluan API v1?

Endpoint baru `/openai/v1` menggunakan klien standard `OpenAI()` dan bukannya `AzureOpenAI()`, tidak memerlukan parameter `api_version`, dan berfungsi seragam antara OpenAI dan Azure OpenAI. Kod klien yang sama ini tahan masa depan — tiada pengurusan versi diperlukan.

### Perubahan utama

| Sebelum | Selepas |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Buang sepenuhnya |

### Senarai semak pembersihan

- Buang argumen `api_version` dari pembinaan klien.
- Buang pembolehubah persekitaran `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` dari `.env`, tetapan aplikasi, dan fail Bicep/infrastruktur.
- Namakan semula `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` dalam `.env`, tetapan aplikasi, Bicep/infrastruktur, dan fixture ujian (konvensyen standard Azure Identity SDK).
- Pastikan `openai>=1.108.1` dalam `requirements.txt` atau `pyproject.toml`.

### Migrasi pembolehubah persekitaran

| Pembolehubah persekitaran lama | Tindakan | Nota |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Buang** | Tiada `api_version` diperlukan dengan endpoint v1 |
| `AZURE_OPENAI_API_VERSION` | **Buang** | Sama seperti di atas |
| `AZURE_OPENAI_CLIENT_ID` | **Namakan semula** → `AZURE_CLIENT_ID` | Konvensyen standard Azure Identity SDK untuk `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Simpan** | Masih diperlukan untuk pembinaan `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Simpan** | Digunakan sebagai param `model` dalam `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Simpan** | Digunakan sebagai `api_key` untuk pengesahan berasaskan kunci |

Untuk contoh kod penyediaan klien (sync, async, EntraID, kunci API, pelbagai penyewa), lihat [cheat-sheet.md](./references/cheat-sheet.md).

---

## Langkah 1: Kenal Pasti Tapak Panggilan Warisan

Jalankan skrip [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) untuk mencari semua tapak panggilan yang perlu dipindahkan:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Atau jalankan carian ini secara manual — setiap padanan adalah sasaran migrasi:

```bash
# Panggilan API lama (perlu ditulis semula)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Pembina klien Azure usang (perlu diganti)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Corak capaian bentuk respon (perlu dikemas kini)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definisi alat dalam format tertanam lama (perlu diratakan)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Keputusan alat dalam format lama (perlu ditukar ke function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Parameter usang (perlu dibuang atau dinamakan semula)
rg "response_format"
rg "max_tokens\b"        # namakan semula kepada max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Pembolehubah persekitaran usang (perlu dibersihkan)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # sepatutnya AZURE_CLIENT_ID

# Titik hujung Model GitHub (perlu dibuang — API Respon tidak disokong)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Corak legasi peringkat rangka kerja (perlu dikemas kini)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: ganti dengan OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: perlu use_responses_api=True

# Infrastruktur ujian (perlu dikemas kini)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Akses badan ralat penapis kandungan (perlu dikemas kini — struktur berubah)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # bentuk singular lama — kini content_filter_results (jamak) dalam tatasusunan content_filters

# Panggilan HTTP mentah ke titik hujung Chat Completions (perlu kemas kini URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristik (kenal pasti dan tulis semula)

- **Klien Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Pembina klien Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Alat**: menukar definisi alat panggilan fungsi dari format bersarang (`{"type": "function", "function": {"name": ...}}`) ke format Respons rata (`{"type": "function", "name": ...}`); gunakan `tool_choice`; kembalikan hasil alat sebagai item `{"type": "function_call_output", "call_id": ..., "output": ...}` (bukan `{"role": "tool", ...}`).
- **Pusingan balik alat**: apabila model mengembalikan panggilan fungsi, tambahkan item `response.output` ke dalam perbualan (bukan dikt manual `{"role": "assistant", "tool_calls": [...]}`), kemudian tambahkan item `function_call_output` untuk setiap hasil.
- **Contoh alat beberapa tembakan**: jika perbualan termasuk contoh panggilan alat keras kod, tukar ke item `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. ID mesti bermula dengan `fc_`.
- **`pydantic_function_tool()`**: pembantu ini masih menjana format lama bersarang dan **tidak serasi** dengan `responses.create()`. Gantikan dengan definisi alat manual atau pembungkus pelurusan.
- **Pusingan berganda**: kekalkan sejarah perbualan dalam aplikasi; hantarkan giliran sebelumnya melalui item `input`.
- **Pemformatan**: gantikan `response_format` peringkat atas Chat dengan `text.format` dalam Respons. Bentuk kanonik: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Item kandungan**: gantikan Chat `content[].type: "text"` dengan Respons `content[].type: "input_text"` untuk giliran pengguna/sistem.
- **Item kandungan imej**: gantikan Chat `content[].type: "image_url"` dengan Respons `content[].type: "input_image"`. Medan `image_url` berubah dari objek bersarang `{"url": "..."}` ke rentetan rata. Lihat helaian cheat untuk contoh sebelum / selepas.
- **Usaha penalaran**: **hanya migrasi `reasoning` jika sudah ada dalam kod asal**.
- **Pengendalian ralat penapis kandungan**: struktur badan ralat berubah. Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]` (tunggal); API Respons menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, dalam susunan). Kod yang mengakses `innererror` akan menyebabkan `KeyError`. Tulis semula untuk menggunakan laluan baru.
- **Panggilan HTTP mentah**: jika aplikasi memanggil REST API Azure OpenAI secara langsung (melalui `requests`, `httpx`, dll.) menggunakan `/openai/deployments/{name}/chat/completions?api-version=...`, tulis semula ke `/openai/v1/responses`. Badan permintaan berubah: `messages` → `input`, tambah `max_output_tokens` dan `store: false`, keluarkan param pertanyaan `api-version`. Badan respons berubah: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` adalah sifat kemudahan SDK yang tidak terdapat dalam JSON REST mentah).

---

## Langkah 2: Laksanakan Migrasi

### Nota migrasi (Chat Completions → Responses)

- **Mengapa migrasi**: Responses adalah API bersatu untuk teks, alat, dan penstriman; Chat Completions adalah warisan. Dengan GPT-5, Responses diperlukan untuk prestasi terbaik.
- **HTTP**: titik akhir Azure bertukar dari `/openai/deployments/{name}/chat/completions` ke `/openai/v1/responses`.
- **Medan**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` kekal.
- **Pemformatan**: `response_format` → `text.format` dengan objek yang betul.
- **Item kandungan**: Gantikan Chat `content[].type: "text"` dengan Responses `content[].type: "input_text"` untuk giliran sistem/pengguna.
- **Item kandungan imej**: Gantikan Chat `content[].type: "image_url"` dengan Responses `content[].type: "input_image"`. Luruskan medan `image_url` dari `{"image_url": {"url": "..."}}` ke `{"image_url": "..."}` (rentetan biasa — sama ada URL HTTPS atau URI data `data:image/...;base64,...`).

### Rujukan pemetaan parameter

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
| `tools` / function-calling | `tools` (tidak berubah) |
| `seed` | **Buang** (tidak disokong) |
| `store` | `store` (ditetapkan ke `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (rentetan rata) |

Untuk contoh kod lengkap sebelum/selepas, lihat [cheat-sheet.md](./references/cheat-sheet.md).

Untuk migrasi infrastruktur ujian (mock, snapshoot, pengesahan), lihat [test-migration.md](./references/test-migration.md).

Untuk penyelesaian masalah ralat dan gotcha, lihat [troubleshooting.md](./references/troubleshooting.md).

---

## Penyimpanan Data & Keadaan

- Tetapkan `store: false` pada semua permintaan Respons.
- Jangan bergantung pada ID mesej sebelumnya atau konteks yang disimpan pelayan; simpan keadaan yang diuruskan klien dan minimakan metadata.

---

## Kriteria Penerimaan

### Pintu aras kod (semua mesti lulus)

- [ ] Tiada padanan untuk `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` dalam fail yang dimigrasi.
- [ ] Tiada padanan untuk `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — semua pembina menggunakan `OpenAI`/`AsyncOpenAI` dengan titik akhir v1.
- [ ] Tiada padanan untuk `rg "models\.github\.ai|models\.inference\.ai\.azure"` — laluan kod Model GitHub dikeluarkan.
- [ ] Tiada padanan untuk `rg "OpenAIChatCompletionClient"` — kod MAF 1.0.0+ menggunakan `OpenAIChatClient` (yang menggunakan Responses API). Dalam versi pre-1.0.0, tingkatkan ke `agent-framework-openai>=1.0.0`.
- [ ] Semua panggilan `ChatOpenAI(...)` termasuk `use_responses_api=True`.
- [ ] Tiada padanan untuk `rg "choices\[0\]"` — semua akses respons menggunakan `resp.output_text` atau skema output Responses.
- [ ] Tiada `response_format` di peringkat atas; semua output berstruktur menggunakan `text={"format": {...}}`.
- [ ] `openai>=1.108.1` dan `azure-identity` dalam `requirements.txt` atau `pyproject.toml`; pergantungan dipasang semula.
- [ ] `store=False` ditetapkan pada setiap panggilan `responses.create`.
- [ ] Tiada `api_version` dalam pembinaan klien; `AZURE_OPENAI_API_VERSION` dikeluarkan daripada fail env dan infra.

### Pintu infrastruktur ujian (semua mesti lulus)

- [ ] Tiada padanan untuk `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Tiada padanan untuk `rg "_azure_ad_token_provider" tests/` — pengesahan dikemas kini untuk memeriksa `isinstance(client, AsyncOpenAI)` atau `base_url`.
- [ ] Tiada padanan untuk `rg "prompt_filter_results|content_filter_results" tests/` — mock penapis khusus Azure dikeluarkan.
- [ ] Mock fixture menggunakan `kwargs.get("input")` bukannya `kwargs.get("messages")`.
- [ ] Fail snapshot / golden dikemas kini ke bentuk penstriman Responses (tiada `choices[0]`, `function_call`, `logprobs`, dll).
- [ ] `pytest` lulus dengan sifar kegagalan selepas semua kemas kini ujian.

### Pintu tingkah laku (sahkan secara manual atau melalui harness ujian)

- [ ] **Penyelesaian asas**: `responses.create` tanpa penstriman mengembalikan `output_text` yang tidak kosong.
- [ ] **Kesetaraan penstriman**: jika kod asal menggunakan penstriman, kod migrasi menstrim dan menghasilkan acara `response.output_text.delta` dengan delta tidak kosong.
- [ ] **Output berstruktur**: jika menggunakan `text.format` dengan `json_schema`, `json.loads(resp.output_text)` berjaya dan sepadan dengan skema.
- [ ] **Gelung panggilan alat**: jika alat digunakan, model mengeluarkan panggilan alat, aplikasi melaksanakannya, dan permintaan susulan mengembalikan `output_text` akhir (tiada gelung tanpa had).
- [ ] **Kesetaraan Async**: jika `AsyncAzureOpenAI` digunakan, setara `AsyncOpenAI` berfungsi dengan `await`.
- [ ] **Kadar ralat**: tiada ralat 400/401/404 baru berbanding garis dasar sebelum migrasi.

### Hasil penghantaran

- Ringkasan termasuk fail yang diedit, kiraan tapak panggilan warisan sebelum/selepas, dan langkah seterusnya.
- Perubahan hanya suntingan pohon kerja (tiada komit).

---

## Keperluan Versi SDK

| Pakej | Versi Minimum |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Terkini (untuk pengesahan EntraID) |

---

## Rujukan

- [Lembaran Cheat — semua sepotong kod](./references/cheat-sheet.md)
- [Migrasi Ujian — mock, snapshoot, pengesahan](./references/test-migration.md)
- [Penyelesaian Masalah — ralat, jadual risiko, gotcha](./references/troubleshooting.md)
- [detect_legacy.py — pengimbas automatik](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Kit Permulaan Azure OpenAI](https://aka.ms/openai/start)
- [Dokumen API Respons Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Kitar Hayat Versi API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Rujukan API Respons OpenAI](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->