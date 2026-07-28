# Penyelesaian Masalah, Jadual Risiko & Perkara Penting

## Penyelesaian Masalah 400s

| Ralat | Pembaikan |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definisi alat menggunakan format bersarang lama Chat Completions | Ratakan dari `{"type": "function", "function": {"name": ...}}` ke `{"type": "function", "name": ..., "parameters": ...}` — nama, deskripsi, parameter diletakkan di peringkat atas |
| `unknown_parameter: input[N].tool_calls` | Keputusan alat berbilang giliran menggunakan format lama Chat Completions | Gantikan `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` dengan item `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Alat `strict: true` tiada array `required` | Apabila `strict: true`, semua sifat mesti disenaraikan dalam `required` dan `additionalProperties: false` mesti ditetapkan |
| `invalid_function_parameters: 'additionalProperties' is required` | Alat `strict: true` tiada `additionalProperties: false` | Tambah `"additionalProperties": false` ke objek parameter |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID panggilan fungsi few-shot mempunyai awalan yang salah | ID panggilan fungsi mesti bermula dengan `fc_` (contoh, `fc_example1`), bukan `call_` |
| `missing_required_parameter: text.format.name` | Tambah kunci `"name"` ke dict format (contoh, `"name": "Output"`) |
| `invalid_type: text.format` | Pastikan `text.format` adalah dict dengan kunci `type`, `name`, `strict`, `schema` — bukan string |
| `invalid input content type` | Gunakan jenis kandungan `input_text`/`output_text` dan bukannya teks Chat `text` |
| `invalid input content type` (imej) | Jenis kandungan imej masih menggunakan `"type": "image_url"` | Tukar kepada `"type": "input_image"` |
| `Expected object, got string` pada `image_url` | `image_url` masih objek bersarang `{"url": "..."}` | Ratakan kepada string biasa: `"image_url": "https://..."` atau `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` untuk `max_output_tokens` | Minimum adalah **16** di Azure OpenAI. Gunakan 50+ untuk ujian, 1000+ untuk pengeluaran. |
| `429 Too Many Requests` semasa penstriman | Had kadar dicapai. Balut penstriman dalam `try/except`, hasilkan JSON ralat ke frontend, laksanakan backoff/cuba semula. |
| `KeyError: 'innererror'` pada ralat penapis kandungan | Struktur badan ralat penapis kandungan berubah dalam Responses API | Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]`; Responses API menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, di dalam array). Tulis semula semua akses `innererror`. |

---

## Jadual Risiko Migrasi

| Gejala | Kesilapan Mungkin | Pembaikan |
|---------|---------------|-----|
| `output_text` kosong / respons terpotong | `max_output_tokens` terlalu rendah untuk model penalaran | Tetapkan `max_output_tokens=1000` atau lebih tinggi — token penalaran diambil kira terhadap had |
| `400 invalid_type: text.format` | Menghantar rentetan `response_format` dan bukannya dict `text.format` | Gunakan `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` pada `/openai/v1/responses` | `base_url` salah — tiada suffix `/openai/v1/` | Pastikan `base_url=f"{endpoint}/openai/v1/"` (dengan slash di belakang) |
| `401 Unauthorized` selepas beralih ke `OpenAI()` | `api_key` tidak ditetapkan atau penyedia token tidak diserahkan dengan betul | Untuk EntraID: `api_key=token_provider` (callable). Untuk kunci API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model mengembalikan `deployment not found` | Param `model` tidak sepadan dengan nama deployment Azure anda | Gunakan `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — ini adalah nama deployment, bukan nama model |
| `json.loads(resp.output_text)` mengalami `JSONDecodeError` | Skema tidak dikuatkuasakan atau model tidak sokong JSON ketat | Pastikan `"strict": True` dalam skema, dan semak model menyokong output berstruktur |
| Penstriman tidak menghasilkan acara `delta` | Memeriksa jenis acara salah | tapis pada `event.type == "response.output_text.delta"`, bukan Chat `chat.completion.chunk` |
| Ralat `400` pada input imej selepas migrasi | Jenis kandungan imej tidak dikemas kini | Tukar `"type": "image_url"` → `"type": "input_image"` dan ratakan `"image_url": {"url": "..."}` → `"image_url": "..."` (string biasa) |
| Panggilan alat berulang tanpa henti | Tiada keputusan alat dalam `input` susulan | Selepas laksanakan alat, tambah item `{"type": "function_call_output", "call_id": ..., "output": ...}` ke `input` dalam permintaan seterusnya |
| Ralat `temperature` dengan GPT-5 atau siri o | Nilai `temperature` eksplisit selain 1 | Buang `temperature` atau tetapkan ke `1` untuk model GPT-5 dan siri o (o1, o3-mini, o3, o4-mini) |
| Ralat `top_p` dengan siri o | `top_p` tidak disokong | Buang `top_p` apabila mensasarkan model siri o |
| `max_completion_tokens` tidak dikenali | Menggunakan parameter khusus Azure | Gantikan `max_completion_tokens` dengan `max_output_tokens`. Tetapkan 4096+ untuk siri o (token penalaran diambil kira terhadap had). |
| Output kosong/terpotong dari siri o | `max_output_tokens` terlalu rendah | Siri o menggunakan token penalaran secara dalaman. Tetapkan `max_output_tokens=4096` atau lebih tinggi — bukan 500–1000. |
| `400 integer_below_min_value` untuk `max_output_tokens` | Nilai kurang daripada 16 | Azure OpenAI menguatkuasakan `max_output_tokens >= 16`. Gunakan 50+ untuk ujian asas, 1000+ untuk pengeluaran. |
| `429 Too Many Requests` pertengahan penstriman | Had kadar oleh Azure OpenAI | Aliran putus secara senyap tanpa pengendalian ralat. Sentiasa balut `async for event in await coroutine:` dalam `try/except` dan hasilkan `{"error": str(e)}` ke frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Tenant salah atau tidak log masuk | Serahkan `tenant_id=os.getenv("AZURE_TENANT_ID")` secara eksplisit. Jalankan `azd auth login --tenant <tenant-id>` secara tempatan. |
| `404 Not Found` menggunakan Model GitHub (`models.github.ai`) | Model GitHub tidak menyokong Responses API | Buang laluan kod Model GitHub sepenuhnya. Gunakan Azure OpenAI, OpenAI, atau endpoint tempatan yang serasi (contoh, Ollama dengan sokongan Responses). |
| MAF `OpenAIChatCompletionClient` masih menggunakan Chat Completions | Menggunakan klien MAF lama dalam 1.0.0+ | Dalam MAF 1.0.0+, `OpenAIChatClient` gunakan Responses API secara lalai. Gantikan `OpenAIChatCompletionClient` dengan `OpenAIChatClient`. Untuk versi sebelum 1.0.0, kemas kini ke `agent-framework-openai>=1.0.0`. |
| Agen LangChain mengembalikan kosong atau gagal dengan panggilan alat | `ChatOpenAI` tidak menggunakan Responses API | Tambah `use_responses_api=True` pada `ChatOpenAI(...)`. Juga tukar `.content` → `.text` pada mesej respons. |
| `KeyError: 'innererror'` dalam pengendali ralat penapis kandungan | Struktur badan ralat berubah dalam Responses API | Tulis semula `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Pembungkus `innererror` sudah tiada; butiran penapis kandungan kini dalam array `content_filters` peringkat atas dengan `content_filter_results` (jamak) di dalam setiap entri. |
| Panggilan HTTP mentah ke `/openai/deployments/.../chat/completions` memberi 404 | Titik akhir REST Chat Completions lama | Tulis semula URL ke `/openai/v1/responses`. Tukar badan permintaan: `messages` → `input`, tambah `max_output_tokens` + `store: false`, buang param kueri `api-version`. Tukar penguraian respons: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` adalah sifat kemudahan SDK, tidak dalam JSON REST mentah). |

---

## Perkara Penting

1. Jika anda sebelum ini menggunakan Chat Completions untuk keadaan perbualan, urus keadaan anda sendiri secara eksplisit dengan Responses.
2. Utamakan `max_output_tokens` berbanding `max_tokens` lama.
3. Semasa migrasi ke `gpt-5`, pastikan `temperature` tidak ditentukan atau ditetapkan ke `1`.
4. Gantikan Chat `content[].type: "text"` dengan Responses `content[].type: "input_text"` untuk input pengguna/sistem.
5. Untuk `text.format`, berikan dict yang betul (contoh, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), bukan rentetan biasa.
6. Parameter `seed` tidak disokong dalam Responses; buang dari permintaan.
7. **Penalaran**: Sertakan `reasoning` hanya jika kod asal sudah menggunakannya. Jangan tambah `reasoning` ke panggilan API yang sebelum ini tiada — banyak model bukan penalaran tidak menyokong parameter ini.
8. **Saiz `max_output_tokens`**: Untuk model penalaran (GPT-5-mini, GPT-5, siri o), gunakan `max_output_tokens=4096` atau lebih tinggi — bukan 50–1000. Model menggunakan token penalaran secara dalaman sebelum menjana output yang kelihatan; had terlalu rendah menyebabkan respons terpotong atau kosong.
9. **Siri o `max_completion_tokens`**: Jika kod asal menggunakan `max_completion_tokens` (khusus Azure untuk siri o), gantikan dengan `max_output_tokens`. Responses API tidak menerima `max_completion_tokens`.
10. **Siri o `reasoning_effort`**: Jika kod asal menggunakan `reasoning_effort` (rendah/sederhana/tinggi), migrasi kepada `reasoning={"effort": "<nilai>"}` dalam panggilan Responses API.
11. **Kelewatan penstriman siri o**: Model siri o melaksanakan penalaran dalaman sebelum menjana output. Semasa penstriman, jangka kelewatan lebih lama sebelum acara `response.output_text.delta` pertama. Ini normal — model sedang berfikir, bukan terhenti.
9. **`_azure_ad_token_provider` sudah tiada**: `AsyncOpenAI` / `OpenAI` tiada atribut `_azure_ad_token_provider`. Ujian atau kod yang mengakses atribut ini akan gagal dengan `AttributeError`. Penyedia token diserahkan sebagai `api_key` dan tidak boleh diperiksa pada objek klien.
10. **Fail snapshot / golden**: Jika suite ujian menggunakan ujian snapshot, **semua** fail snapshot yang mengandungi bentuk penstriman Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, dan lain-lain) mesti dikemas kini ke bentuk Responses yang baru. Ini mudah terlepas dan menyebabkan kegagalan perbandingan snapshot.
11. **Jalan monkeypatch mock**: Sasaran monkeypatch berubah daripada `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (atau `Responses.create` untuk sync). Menggunakan jalan lama tidak menghasilkan apa-apa secara senyap — mock tidak akan memintas, dan ujian terkena API sebenar atau gagal.
12. **`input` bukan `messages`**: Fungsi mock mesti membaca `kwargs.get("input")` bukan `kwargs.get("messages")`. Responses API menggunakan `input` untuk sejarah perbualan.
13. **Penamaan var env**: Azure Identity SDK menggunakan `AZURE_CLIENT_ID` (bukan `AZURE_OPENAI_CLIENT_ID`) untuk `ManagedIdentityCredential(client_id=...)`. Tukar nama dalam ujian, fail `.env`, tetapan aplikasi, dan Bicep/infrastruktur.
14. **Minimum `max_output_tokens` adalah 16**: Azure OpenAI menolak nilai kurang daripada 16 dengan `400 integer_below_min_value`. Gunakan 50 untuk ujian ringan, 1000+ untuk pengeluaran. `max_tokens` lama tiada minimum sebegini.
15. **`tenant_id` untuk `AzureDeveloperCliCredential`**: Apabila sumber Azure OpenAI berada dalam tenant berbeza, anda **mesti** serahkan `tenant_id` secara eksplisit — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Tanpanya, kredensial menggunakan tenant salah secara senyap dan mengembalikan `401`.
16. **Had kadar muncul berlainan dalam penstriman**: Dengan Chat Completions, 429 biasanya menghalang permulaan aliran. Dengan penstriman Responses API, 429 boleh berlaku **pertengahan aliran** — iterator async mengeluarkan pengecualian. Sentiasa balut gelung penstriman dalam `try/except` dan hasilkan baris JSON ralat supaya frontend boleh mengendalikannya dengan baik.

17. **Pengendalian ralat aliran adalah wajib untuk aplikasi web**: Corak `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` adalah kritikal. Tanpanya, aliran SSE/JSONL akan berhenti tanpa keluaran pada sebarang ralat di sisi pelayan dan antaramuka hadapan akan tergantung.
18. **Definisi alat mesti menggunakan format rata**: API Respons menjangkakan `{"type": "function", "name": ..., "parameters": ...}` — bukan `{"type": "function", "function": {"name": ..., "parameters": ...}}` yang bersarang seperti dalam Chat Completions. Ini adalah kesilapan migrasi paling biasa untuk kod panggilan fungsi.
19. **`pydantic_function_tool()` tidak serasi**: Pembantu `openai.pydantic_function_tool()` masih menjana format bersarang yang lama. Jangan guna bersama `responses.create()`. Definisikan skema alat secara manual atau ratakan output.
20. **Keputusan alat menggunakan `function_call_output`, bukan `role: tool`**: Selepas melaksanakan alat, tambah `{"type": "function_call_output", "call_id": ..., "output": ...}` — bukan `{"role": "tool", "tool_call_id": ..., "content": ...}`. Untuk permintaan alat pembantu, gunakan `messages.extend(response.output)` — bukan `{"role": "assistant", "tool_calls": [...]}` secara manual.
21. **`strict: true` memerlukan `required` + `additionalProperties: false`**: Apabila menggunakan `strict: true` pada alat, setiap sifat mesti disenaraikan dalam array `required` dan `additionalProperties` mesti `false`. Kehilangan salah satu menyebabkan ralat 400.
22. **ID panggilan fungsi mempunyai awalan tertentu**: Apabila menyediakan item `function_call` few-shot dalam `input`, medan `id` mesti bermula dengan `fc_` dan medan `call_id` mesti bermula dengan `call_` (contoh, `"id": "fc_example1", "call_id": "call_example1"`). Penggunaan awalan lama `call_` dari Chat Completions untuk `id` akan ditolak.
23. **Model GitHub tidak menyokong API Respons**: Jika aplikasi mempunyai laluan kod Model GitHub (`base_url` menunjuk ke `models.github.ai` atau `models.inference.ai.azure.com`), keluarkan sepenuhnya. Tiada laluan migrasi — beralih ke Azure OpenAI, OpenAI, atau titik akhir tempatan yang serasi.
24. **Struktur badan ralat penapis kandungan berubah**: Ralat Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]` (tunggal). Ralat API Respons menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, dalam susunan). Kekunci `innererror` tidak lagi wujud. Kod yang terus mengakses `innererror` akan menyebabkan `KeyError` semasa runtime — ini mudah terlepas pandang dalam migrasi kerana hanya muncul apabila penapis kandungan benar-benar mencetuskan. Sentiasa grep untuk `innererror` semasa migrasi.
25. **Panggilan HTTP mentah memerlukan penulisan semula URL + badan**: Aplikasi yang memanggil REST Azure OpenAI secara langsung (melalui `requests`, `httpx`, `aiohttp`) dengan `/openai/deployments/{name}/chat/completions?api-version=...` mesti beralih ke `/openai/v1/responses`. Badan permintaan menggunakan `input` dan bukan `messages`, memerlukan `max_output_tokens` dan `store`, dan parameter kueri `api-version` dibuang. Teks badan respons berada di `output[0].content[0].text` — **bukan** `output_text`, yang merupakan sifat kemudahan SDK yang tiada dalam JSON REST mentah.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->