# Pemecahan Masalah, Tabel Risiko & Hal-Hal yang Perlu Diperhatikan

## Pemecahan Masalah 400s

| Error | Perbaikan |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definisi alat menggunakan format bersarang Chat Completions yang lama | Datar dari `{"type": "function", "function": {"name": ...}}` ke `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters berada di tingkat atas |
| `unknown_parameter: input[N].tool_calls` | Hasil alat multi-putaran menggunakan format Chat Completions lama | Ganti `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` dengan item `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Alat `strict: true` tidak memiliki array `required` | Saat `strict: true`, semua properti harus terdaftar di `required` dan `additionalProperties: false` harus disetel |
| `invalid_function_parameters: 'additionalProperties' is required` | Alat `strict: true` tidak memiliki `additionalProperties: false` | Tambahkan `"additionalProperties": false` ke objek parameters |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID function_call few-shot memiliki awalan yang salah | ID panggilan fungsi harus diawali dengan `fc_` (misal, `fc_example1`), bukan `call_` |
| `missing_required_parameter: text.format.name` | Tambahkan kunci `"name"` ke dict format (misal, `"name": "Output"`) |
| `invalid_type: text.format` | Pastikan `text.format` adalah dict dengan kunci `type`, `name`, `strict`, `schema` — bukan string |
| `invalid input content type` | Gunakan tipe konten `input_text`/`output_text` bukan Chat `text` |
| `invalid input content type` (gambar) | Konten gambar masih menggunakan `"type": "image_url"` | Ubah ke `"type": "input_image"` |
| `Expected object, got string` pada `image_url` | `image_url` masih merupakan objek bersarang `{"url": "..."}` | Ubah ke string biasa: `"image_url": "https://..."` atau `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` untuk `max_output_tokens` | Minimum adalah **16** di Azure OpenAI. Gunakan 50+ untuk pengujian, 1000+ untuk produksi. |
| `429 Too Many Requests` selama streaming | Terbatas oleh rate limit. Bungkus streaming dengan `try/except`, hasilkan JSON error ke frontend, implementasikan backoff/retry. |
| `KeyError: 'innererror'` pada error filter konten | Struktur body error filter konten berubah di Responses API | Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]`; Responses API menggunakan `error.body["content_filters"][0]["content_filter_results"]` (plural, dalam array). Tuliskan ulang semua akses `innererror`. |

---

## Tabel Risiko Migrasi

| Gejala | Kesalahan Kemungkinan | Perbaikan |
|---------|---------------|-----|
| `output_text` kosong / respon terpotong | `max_output_tokens` terlalu rendah untuk model penalaran | Tetapkan `max_output_tokens=1000` atau lebih tinggi — token penalaran dihitung terhadap batas |
| `400 invalid_type: text.format` | Mengirim string `response_format` bukannya dict `text.format` | Gunakan `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` pada `/openai/v1/responses` | `base_url` salah — kurang akhiran `/openai/v1/` | Pastikan `base_url=f"{endpoint}/openai/v1/"` (dengan slash di akhir) |
| `401 Unauthorized` setelah beralih ke `OpenAI()` | `api_key` tidak disetel atau penyedia token tidak diberikan dengan benar | Untuk EntraID: `api_key=token_provider` (callable). Untuk API key: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model mengembalikan `deployment not found` | Parameter `model` tidak cocok dengan nama deployment Azure Anda | Gunakan `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — ini adalah nama deployment, bukan nama model |
| `json.loads(resp.output_text)` menghasilkan `JSONDecodeError` | Skema tidak ditegakkan atau model tidak mendukung JSON ketat | Pastikan `"strict": True` dalam skema, dan verifikasi model mendukung output terstruktur |
| Streaming tidak menghasilkan event `delta` | Memeriksa tipe event yang salah | Filter pada `event.type == "response.output_text.delta"`, bukan `chat.completion.chunk` dari Chat |
| Error `400` pada input gambar setelah migrasi | Tipe konten gambar tidak diperbarui | Ganti `"type": "image_url"` → `"type": "input_image"` dan datar `"image_url": {"url": "..."}` → `"image_url": "..."` (string biasa) |
| Panggilan alat berulang tanpa henti | Hasil alat hilang pada `input` lanjutan | Setelah mengeksekusi alat, tambahkan item `{"type": "function_call_output", "call_id": ..., "output": ...}` ke `input` di permintaan berikutnya |
| Error `temperature` dengan GPT-5 atau seri o | Nilai `temperature` eksplisit selain 1 | Hapus `temperature` atau setel ke `1` untuk model GPT-5 dan seri o (o1, o3-mini, o3, o4-mini) |
| Error `top_p` dengan seri o | `top_p` tidak didukung | Hapus `top_p` saat menargetkan model seri o |
| `max_completion_tokens` tidak dikenali | Menggunakan parameter spesifik Azure | Ganti `max_completion_tokens` dengan `max_output_tokens`. Setel ke 4096+ untuk seri o (token penalaran dihitung terhadap batas). |
| Output kosong/terpotong dari seri o | `max_output_tokens` terlalu rendah | Seri o menggunakan token penalaran secara internal. Atur `max_output_tokens=4096` atau lebih tinggi — bukan 500–1000. |
| `400 integer_below_min_value` untuk `max_output_tokens` | Nilai di bawah 16 | Azure OpenAI menerapkan `max_output_tokens >= 16`. Gunakan 50+ untuk tes asap, 1000+ untuk produksi. |
| `429 Too Many Requests` di tengah streaming | Terbatas oleh Azure OpenAI | Streaming terputus tanpa error handling. Selalu bungkus `async for event in await coroutine:` dalam `try/except` dan hasilkan `{"error": str(e)}` ke frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Tenant salah atau belum masuk | Berikan `tenant_id=os.getenv("AZURE_TENANT_ID")` secara eksplisit. Jalankan `azd auth login --tenant <tenant-id>` secara lokal. |
| `404 Not Found` menggunakan GitHub Models (`models.github.ai`) | GitHub Models tidak mendukung Responses API | Hapus jalur kode GitHub Models sepenuhnya. Gunakan Azure OpenAI, OpenAI, atau endpoint lokal kompatibel (misal, Ollama dengan dukungan Responses). |
| MAF `OpenAIChatCompletionClient` masih menggunakan Chat Completions | Menggunakan klien MAF lama di 1.0.0+ | Dalam MAF 1.0.0+, `OpenAIChatClient` menggunakan Responses API secara default. Ganti `OpenAIChatCompletionClient` dengan `OpenAIChatClient`. Untuk pre-1.0.0, upgrade ke `agent-framework-openai>=1.0.0`. |
| Agen LangChain mengembalikan kosong atau gagal dengan panggilan alat | `ChatOpenAI` tidak menggunakan Responses API | Tambahkan `use_responses_api=True` ke `ChatOpenAI(...)`. Juga ubah `.content` → `.text` pada pesan respons. |
| `KeyError: 'innererror'` dalam handler error filter konten | Struktur body error berubah di Responses API | Tulis ulang `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Pembungkus `innererror` hilang; rincian filter konten sekarang di array level atas `content_filters` dengan `content_filter_results` (jamak) di setiap entri. |
| Panggilan HTTP mentah ke `/openai/deployments/.../chat/completions` mengembalikan 404 | Endpoint REST Chat Completions lama | Tulis ulang URL ke `/openai/v1/responses`. Ubah body permintaan: `messages` → `input`, tambahkan `max_output_tokens` + `store: false`, hapus query param `api-version`. Ubah parsing respons: `choices[0].message.content` → `output[0].content[0].text` (perlu dicatat: `output_text` adalah properti kenyamanan SDK, tidak ada di JSON REST mentah). |

---

## Hal-Hal yang Perlu Diperhatikan

1. Jika sebelumnya Anda menggunakan Chat Completions untuk status percakapan, kelola status Anda sendiri secara eksplisit dengan Responses.
2. Lebih disukai `max_output_tokens` daripada `max_tokens` lama.
3. Saat migrasi ke `gpt-5`, pastikan `temperature` tidak ditentukan atau disetel ke `1`.
4. Ganti Chat `content[].type: "text"` dengan Responses `content[].type: "input_text"` untuk input pengguna/sistem.
5. Untuk `text.format`, berikan dict yang benar (misal, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), bukan string biasa.
6. Parameter `seed` tidak didukung di Responses; hapus dari permintaan.
7. **Penalaran**: Sertakan `reasoning` hanya jika kode asli sudah menggunakannya. Jangan tambahkan `reasoning` ke panggilan API yang tidak memilikinya — banyak model (misal, gpt-4o-mini) tidak mendukung parameter ini.
8. **Penyetelan `max_output_tokens`**: Untuk model penalaran (GPT-5-mini, GPT-5, seri o), gunakan `max_output_tokens=4096` atau lebih — bukan 50–1000. Model menggunakan token penalaran secara internal sebelum menghasilkan output terlihat; batas terlalu rendah menyebabkan respon terpotong atau kosong.
9. **`max_completion_tokens` pada seri o**: Jika kode asli menggunakan `max_completion_tokens` (spesifik Azure untuk seri o), gantikan dengan `max_output_tokens`. Responses API tidak menerima `max_completion_tokens`.
10. **`reasoning_effort` pada seri o**: Jika kode asli menggunakan `reasoning_effort` (rendah/sedang/tinggi), migrasikan ke `reasoning={"effort": "<nilai>"}` dalam panggilan Responses API.
11. **Penundaan streaming seri o**: Model seri o melakukan penalaran internal sebelum menghasilkan output. Saat streaming, harapkan penundaan lebih lama sebelum event pertama `response.output_text.delta`. Ini normal — model sedang menalar, bukan macet.
9. **`_azure_ad_token_provider` sudah hilang**: `AsyncOpenAI` / `OpenAI` tidak memiliki atribut `_azure_ad_token_provider`. Tes atau kode yang mengakses atribut ini akan gagal dengan `AttributeError`. Penyedia token diberikan sebagai `api_key` dan tidak dapat diinspeksi pada objek klien.
10. **File snapshot / golden**: Jika rangkaian tes menggunakan snapshot testing, **semua** file snapshot yang berisi bentuk streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, dll) harus diperbarui ke bentuk baru Responses. Ini mudah terlewat dan menyebabkan kegagalan asersi snapshot.
11. **Jalur monkeypatch mock**: Target monkeypatch berubah dari `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (atau `Responses.create` untuk sinkron). Menggunakan jalur lama tidak berfungsi diam-diam — mock tidak akan menangkap, dan tes akan mengakses API asli atau gagal.
12. **`input` bukan `messages`**: Fungsi mock harus membaca `kwargs.get("input")`, bukan `kwargs.get("messages")`. Responses API menggunakan `input` untuk riwayat percakapan.
13. **Penamaan variabel lingkungan**: Azure Identity SDK menggunakan `AZURE_CLIENT_ID` (bukan `AZURE_OPENAI_CLIENT_ID`) untuk `ManagedIdentityCredential(client_id=...)`. Ubah nama di tes, file `.env`, pengaturan aplikasi, dan Bicep/infra.
14. **Minimum `max_output_tokens` adalah 16**: Azure OpenAI menolak nilai di bawah 16 dengan `400 integer_below_min_value`. Gunakan `50` untuk tes asap, `1000`+ untuk produksi. `max_tokens` lama tidak memiliki minimum seperti itu.
15. **`tenant_id` untuk `AzureDeveloperCliCredential`**: Jika sumber daya Azure OpenAI berada di tenant berbeda, Anda **harus** memberikan `tenant_id` secara eksplisit — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Tanpa ini, kredensial menggunakan tenant salah secara diam-diam dan mengembalikan `401`.
16. **Batas rate muncul berbeda dalam streaming**: Dengan Chat Completions, 429 biasanya mencegah stream dimulai. Dengan streaming Responses API, 429 dapat terjadi **di tengah stream** — iterator async melempar pengecualian. Selalu bungkus loop streaming dalam `try/except` dan hasilkan baris JSON error agar frontend dapat menanganinya dengan baik.

17. **Penanganan error streaming wajib untuk aplikasi web**: Pola `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` adalah penting. Tanpanya, aliran SSE/JSONL akan mati diam-diam saat terjadi kesalahan di sisi server dan frontend akan macet.
18. **Definisi alat harus menggunakan format datar**: API Responses mengharapkan `{"type": "function", "name": ..., "parameters": ...}` — bukan format bersarang Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Ini adalah kesalahan migrasi paling umum untuk kode pemanggilan fungsi.
19. **`pydantic_function_tool()` tidak kompatibel**: Pembantu `openai.pydantic_function_tool()` masih menghasilkan format lama yang bersarang. Jangan gunakan dengan `responses.create()`. Definisikan skema alat secara manual atau ratakan outputnya.
20. **Hasil alat menggunakan `function_call_output`, bukan `role: tool`**: Setelah menjalankan alat, tambahkan `{"type": "function_call_output", "call_id": ..., "output": ...}` — bukan `{"role": "tool", "tool_call_id": ..., "content": ...}`. Untuk permintaan alat asisten, gunakan `messages.extend(response.output)` — bukan dictionary manual `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` membutuhkan `required` + `additionalProperties: false`**: Saat menggunakan `strict: true` pada sebuah alat, setiap properti harus tercantum dalam array `required` dan `additionalProperties` harus `false`. Ketiadaan salah satunya menyebabkan error 400.
22. **ID pemanggilan fungsi memiliki prefix spesifik**: Saat memberikan item `function_call` few-shot dalam `input`, field `id` harus diawali dengan `fc_` dan field `call_id` harus diawali dengan `call_` (misal, `"id": "fc_example1", "call_id": "call_example1"`). Menggunakan prefix lama Chat Completions `call_` untuk `id` akan ditolak.
23. **GitHub Models tidak mendukung API Responses**: Jika aplikasi memiliki jalur kode GitHub Models (`base_url` menunjuk ke `models.github.ai` atau `models.inference.ai.azure.com`), hapus sepenuhnya. Tidak ada jalur migrasi — beralihlah ke Azure OpenAI, OpenAI, atau endpoint lokal yang kompatibel.
24. **Struktur body error filter konten berubah**: Error Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]` (tunggal). Error API Responses menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, dalam array). Kunci `innererror` tidak ada lagi. Kode yang langsung mengakses `innererror` akan melempar `KeyError` saat runtime — ini mudah terlewat saat migrasi karena hanya muncul saat filter konten benar-benar memicu. Selalu cari `innererror` saat migrasi.
25. **Panggilan HTTP mentah perlu penulisan ulang URL + body**: Aplikasi yang memanggil Azure OpenAI REST langsung (via `requests`, `httpx`, `aiohttp`) menggunakan `/openai/deployments/{name}/chat/completions?api-version=...` harus menggantinya ke `/openai/v1/responses`. Body permintaan menggunakan `input` bukan `messages`, membutuhkan `max_output_tokens` dan `store`, dan parameter query `api-version` dihapus. Teks body respon ada di `output[0].content[0].text` — **bukan** `output_text`, yang merupakan properti kenyamanan SDK yang tidak ada di JSON REST mentah.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->