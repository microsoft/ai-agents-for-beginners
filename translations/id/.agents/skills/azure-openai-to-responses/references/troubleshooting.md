# Pemecahan Masalah, Tabel Risiko & Hal yang Harus Diwaspadai

## Pemecahan Masalah 400s

| Error | Perbaikan |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definisi alat menggunakan format nested lama Chat Completions | Ratakan dari `{"type": "function", "function": {"name": ...}}` ke `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters diletakkan di level atas |
| `unknown_parameter: input[N].tool_calls` | Hasil alat multi-turn menggunakan format lama Chat Completions | Ganti `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` dengan item `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Alat `strict: true` hilang array `required` | Saat `strict: true`, semua properti harus tercantum di `required` dan `additionalProperties: false` harus disetel |
| `invalid_function_parameters: 'additionalProperties' is required` | Alat `strict: true` hilang `additionalProperties: false` | Tambahkan `"additionalProperties": false` ke objek parameters |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID function_call few-shot prefix salah | ID pemanggilan fungsi harus dimulai dengan `fc_` (misal, `fc_example1`), bukan `call_` |
| `missing_required_parameter: text.format.name` | Tambahkan kunci `"name"` ke dict format (misal, `"name": "Output"`) |
| `invalid_type: text.format` | Pastikan `text.format` adalah dict dengan kunci `type`, `name`, `strict`, `schema` — bukan string |
| `invalid input content type` | Gunakan tipe konten `input_text`/`output_text` bukan `text` Chat |
| `invalid input content type` (gambar) | Konten gambar masih menggunakan `"type": "image_url"` | Ubah menjadi `"type": "input_image"` |
| `Expected object, got string` pada `image_url` | `image_url` masih berupa objek nested `{"url": "..."}` | Ratakan menjadi string biasa: `"image_url": "https://..."` atau `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` untuk `max_output_tokens` | Minimum adalah **16** pada Azure OpenAI. Gunakan 50+ untuk pengujian, 1000+ untuk produksi. |
| `429 Too Many Requests` saat streaming | Terbatas rate. Bungkus streaming dalam `try/except`, hasilkan JSON error ke frontend, terapkan backoff/retry. |
| `KeyError: 'innererror'` pada kesalahan filter konten | Struktur body error filter konten berubah di Responses API | Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]`; Responses API menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, dalam array). Tulis ulang semua akses `innererror`. |

---

## Tabel Risiko Migrasi

| Gejala | Kesalahan Kemungkinan | Perbaikan |
|---------|---------------|-----|
| `output_text` kosong / respon terpotong | `max_output_tokens` terlalu rendah untuk model reasoning | Set `max_output_tokens=1000` atau lebih — token reasoning dihitung terhadap batas |
| `400 invalid_type: text.format` | Mengoper string `response_format` bukan dict `text.format` | Gunakan `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` pada `/openai/v1/responses` | `base_url` salah — hilang akhiran `/openai/v1/` | Pastikan `base_url=f"{endpoint}/openai/v1/"` (dengan slash di akhir) |
| `401 Unauthorized` setelah beralih ke `OpenAI()` | `api_key` belum disetel atau penyedia token tidak diteruskan dengan benar | Untuk EntraID: `api_key=token_provider` (callable). Untuk kunci API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model mengembalikan `deployment not found` | parameter `model` tidak cocok dengan nama deployment Azure Anda | Gunakan `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — ini adalah nama deployment, bukan nama model |
| `json.loads(resp.output_text)` memicu `JSONDecodeError` | Skema tidak ditegakkan atau model tidak mendukung JSON ketat | Pastikan `"strict": True` dalam skema, dan verifikasi model mendukung output terstruktur |
| Streaming tidak menghasilkan event `delta` | Memeriksa tipe event yang salah | Filter pada `event.type == "response.output_text.delta"`, bukan `chat.completion.chunk` Chat |
| Error `400` pada input gambar setelah migrasi | Jenis konten gambar tidak diperbarui | Ubah `"type": "image_url"` → `"type": "input_image"` dan ratakan `"image_url": {"url": "..."}` → `"image_url": "..."` (string biasa) |
| Panggilan alat berulang tanpa henti | Hasil alat hilang dalam `input` tindak lanjut | Setelah menjalankan alat, tambahkan item `{"type": "function_call_output", "call_id": ..., "output": ...}` ke `input` pada permintaan berikutnya |
| Error `temperature` dengan GPT-5 atau seri o | Nilai `temperature` eksplisit selain 1 | Hapus `temperature` atau atur ke `1` untuk model GPT-5 dan seri o (o1, o3-mini, o3, o4-mini) |
| Error `top_p` dengan seri o | `top_p` tidak didukung | Hapus `top_p` saat menarget seri o |
| `max_completion_tokens` tidak dikenali | Menggunakan parameter khusus Azure | Ganti `max_completion_tokens` dengan `max_output_tokens`. Tetapkan ke 4096+ untuk seri o (token reasoning dihitung terhadap batas). |
| Output kosong/terpotong dari seri o | `max_output_tokens` terlalu rendah | Seri o menggunakan token reasoning secara internal. Set `max_output_tokens=4096` atau lebih — bukan 500–1000. |
| `400 integer_below_min_value` untuk `max_output_tokens` | Nilai di bawah 16 | Azure OpenAI mewajibkan `max_output_tokens >= 16`. Gunakan 50+ untuk tes singkat, 1000+ untuk produksi. |
| `429 Too Many Requests` di tengah streaming | Dibatasi rate oleh Azure OpenAI | Streaming berhenti diam tanpa penanganan error. Selalu bungkus `async for event in await coroutine:` dalam `try/except` dan hasilkan `{"error": str(e)}` ke frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Tenant salah atau belum login | Teruskan `tenant_id=os.getenv("AZURE_TENANT_ID")` secara eksplisit. Jalankan `azd auth login --tenant <tenant-id>` secara lokal. |
| `404 Not Found` menggunakan GitHub Models (`models.github.ai`) | GitHub Models tidak mendukung Responses API | Hapus seluruh jalur kode GitHub Models. Gunakan Azure OpenAI, OpenAI, atau endpoint lokal kompatibel (misal, Ollama dengan dukungan Responses). |
| MAF `OpenAIChatCompletionClient` masih memakai Chat Completions | Menggunakan klien MAF legacy pada 1.0.0+ | Di MAF 1.0.0+, `OpenAIChatClient` memakai Responses API secara default. Ganti `OpenAIChatCompletionClient` dengan `OpenAIChatClient`. Untuk pra-1.0.0, upgrade ke `agent-framework-openai>=1.0.0`. |
| Agen LangChain mengembalikan kosong atau gagal dengan panggilan alat | `ChatOpenAI` tidak menggunakan Responses API | Tambahkan `use_responses_api=True` ke `ChatOpenAI(...)`. Juga ubah `.content` → `.text` pada pesan respons. |
| `KeyError: 'innererror'` di penanganan error filter konten | Struktur body error berubah di Responses API | Tulis ulang `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Pembungkus `innererror` hilang; detail filter konten sekarang di array `content_filters` tingkat atas dengan `content_filter_results` (jamak) dalam setiap entri. |
| Panggilan HTTP mentah ke `/openai/deployments/.../chat/completions` mengembalikan 404 | Endpoint REST Chat Completions lama | Ubah URL menjadi `/openai/v1/responses`. Ganti body permintaan: `messages` → `input`, tambahkan `max_output_tokens` + `store: false`, hilangkan query param `api-version`. Ganti parsing respons: `choices[0].message.content` → `output[0].content[0].text` (perhatikan: `output_text` adalah properti kemudahan SDK, tidak ada dalam JSON REST mentah). |

---

## Hal yang Harus Diwaspadai

1. Jika sebelumnya menggunakan Chat Completions untuk status percakapan, kelola status Anda sendiri secara eksplisit dengan Responses.
2. Utamakan `max_output_tokens` dibanding `max_tokens` legacy.
3. Saat migrasi ke `gpt-5`, pastikan `temperature` tidak disetel atau disetel ke `1`.
4. Ganti tipe Chat `content[].type: "text"` dengan Responses `content[].type: "input_text"` untuk input pengguna/sistem.
5. Untuk `text.format`, sediakan dict yang tepat (misal, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), bukan string biasa.
6. Parameter `seed` tidak didukung di Responses; hapus dari permintaan.
7. **Reasoning**: Sertakan `reasoning` hanya jika kode asli sudah menggunakannya. Jangan tambahkan `reasoning` ke panggilan API yang tidak memilikinya — banyak model non-reasoning tidak mendukung parameter ini.
8. **Pengaturan ukuran `max_output_tokens`**: Untuk model reasoning (GPT-5-mini, GPT-5, seri o), gunakan `max_output_tokens=4096` atau lebih — bukan 50–1000. Model menggunakan token reasoning secara internal sebelum menghasilkan output yang terlihat; batas terlalu rendah menyebabkan respons terpotong atau kosong.
9. **`max_completion_tokens` seri o**: Jika kode asli menggunakan `max_completion_tokens` (khusus Azure untuk seri o), ganti dengan `max_output_tokens`. Responses API tidak menerima `max_completion_tokens`.
10. **`reasoning_effort` seri o**: Jika kode asli menggunakan `reasoning_effort` (low/medium/high), migrasikan ke `reasoning={"effort": "<nilai>"}` dalam panggilan Responses API.
11. **Penundaan streaming seri o**: Model seri o melakukan reasoning internal sebelum menghasilkan output. Saat streaming, harapkan penundaan lebih lama sebelum event `response.output_text.delta` pertama. Ini normal — model sedang melakukan reasoning, bukan macet.
9. **`_azure_ad_token_provider` sudah hilang**: `AsyncOpenAI` / `OpenAI` tidak memiliki atribut `_azure_ad_token_provider`. Tes atau kode yang mengakses atribut ini akan gagal dengan `AttributeError`. Penyedia token diteruskan sebagai `api_key` dan tidak dapat diperiksa pada objek klien.
10. **File snapshot / golden**: Jika suite tes menggunakan snapshot testing, **semua** file snapshot yang berisi bentuk streaming Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, dll.) harus diperbarui ke bentuk Responses yang baru. Hal ini mudah terlewat dan menyebabkan kegagalan asersi snapshot.
11. **Jalur monkeypatch mock**: Target monkeypatch berubah dari `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (atau `Responses.create` untuk sinkron). Menggunakan jalur lama tidak berfungsi diam-diam — mock tidak akan menyergap, dan tes mencapai API nyata atau gagal.
12. **`input` bukan `messages`**: Fungsi mock harus membaca `kwargs.get("input")` bukan `kwargs.get("messages")`. Responses API menggunakan `input` untuk riwayat percakapan.
13. **Penamaan variabel lingkungan**: SDK Azure Identity menggunakan `AZURE_CLIENT_ID` (bukan `AZURE_OPENAI_CLIENT_ID`) untuk `ManagedIdentityCredential(client_id=...)`. Ubah nama di tes, file `.env`, pengaturan aplikasi, dan Bicep/infrastruktur.
14. **Minimum `max_output_tokens` adalah 16**: Azure OpenAI menolak nilai di bawah 16 dengan `400 integer_below_min_value`. Gunakan `50` untuk tes singkat, `1000`+ untuk produksi. `max_tokens` lama tidak memiliki minimum ini.
15. **`tenant_id` untuk `AzureDeveloperCliCredential`**: Ketika sumber daya Azure OpenAI berada di tenant berbeda, Anda **harus** menyertakan `tenant_id` secara eksplisit — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Tanpa ini, kredensial menggunakan tenant salah secara diam-diam dan mengembalikan `401`.
16. **Batasan rate muncul berbeda dalam streaming**: Dengan Chat Completions, 429 biasanya mencegah streaming dimulai. Dengan streaming Responses API, 429 dapat terjadi **tengah streaming** — iterator async melempar pengecualian. Selalu bungkus loop streaming dalam `try/except` dan hasilkan baris JSON error agar frontend dapat menanganinya dengan baik.

17. **Penanganan kesalahan streaming wajib untuk aplikasi web**: Pola `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` sangat penting. Tanpanya, aliran SSE/JSONL akan berhenti secara diam-diam pada kesalahan sisi server apa pun dan frontend menjadi macet.
18. **Definisi alat harus menggunakan format datar**: API Responses mengharapkan `{"type": "function", "name": ..., "parameters": ...}` — bukan format bersarang Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Ini adalah kesalahan migrasi paling umum untuk kode pemanggilan fungsi.
19. **`pydantic_function_tool()` tidak kompatibel**: Bantuan `openai.pydantic_function_tool()` masih menghasilkan format lama yang bersarang. Jangan gunakan dengan `responses.create()`. Definisikan skema alat secara manual atau ratakan outputnya.
20. **Hasil alat menggunakan `function_call_output`, bukan `role: tool`**: Setelah menjalankan alat, tambahkan `{"type": "function_call_output", "call_id": ..., "output": ...}` — bukan `{"role": "tool", "tool_call_id": ..., "content": ...}`. Untuk permintaan alat asisten, gunakan `messages.extend(response.output)` — bukan dict `{"role": "assistant", "tool_calls": [...]}` secara manual.
21. **`strict: true` memerlukan `required` + `additionalProperties: false`**: Saat menggunakan `strict: true` pada alat, setiap properti harus dicantumkan dalam array `required` dan `additionalProperties` harus `false`. Kehilangan salah satunya menyebabkan kesalahan 400.
22. **ID panggilan fungsi memiliki awalan khusus**: Saat menyediakan item `function_call` few-shot dalam `input`, bidang `id` harus diawali dengan `fc_` dan bidang `call_id` harus diawali dengan `call_` (misalnya, `"id": "fc_example1", "call_id": "call_example1"`). Menggunakan awalan `call_` lama dari Chat Completions untuk `id` akan ditolak.
23. **GitHub Models tidak mendukung Responses API**: Jika aplikasi memiliki jalur kode GitHub Models (`base_url` menunjuk ke `models.github.ai` atau `models.inference.ai.azure.com`), hapus sepenuhnya. Tidak ada jalur migrasi — beralihlah ke Azure OpenAI, OpenAI, atau endpoint lokal yang kompatibel.
24. **Struktur isi kesalahan filter konten berubah**: Kesalahan Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]` (tunggal). Kesalahan Responses API menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, di dalam array). Kunci `innererror` tidak ada lagi. Kode yang mengakses `innererror` secara langsung akan memunculkan `KeyError` saat runtime — ini mudah terlewat saat migrasi karena hanya muncul saat filter konten benar-benar dipicu. Selalu cari `innererror` selama migrasi.
25. **Panggilan HTTP mentah memerlukan penulisan ulang URL + body**: Aplikasi yang memanggil Azure OpenAI REST langsung (melalui `requests`, `httpx`, `aiohttp`) menggunakan `/openai/deployments/{name}/chat/completions?api-version=...` harus beralih ke `/openai/v1/responses`. Body permintaan menggunakan `input` bukan `messages`, memerlukan `max_output_tokens` dan `store`, dan parameter kueri `api-version` dihapus. Teks body respons ada di `output[0].content[0].text` — **bukan** `output_text`, yang merupakan properti kemudahan SDK yang tidak ada dalam JSON REST mentah.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->