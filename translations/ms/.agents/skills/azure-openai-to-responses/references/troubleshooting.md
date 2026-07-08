# Penyelesaian Masalah, Jadual Risiko & Perkara Penting

## Penyelesaian Masalah 400s

| Ralat | Pembetulan |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definisi alat menggunakan format bersarang Chat Completions lama | Rata-ratakan daripada `{"type": "function", "function": {"name": ...}}` ke `{"type": "function", "name": ..., "parameters": ...}` — nama, penerangan, parameter diletakkan di peringkat atas |
| `unknown_parameter: input[N].tool_calls` | Keputusan alat pelbagai pusingan menggunakan format Chat Completions lama | Gantikan `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` dengan item `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Alat `strict: true` tiada array `required` | Apabila `strict: true`, semua sifat mesti disenaraikan dalam `required` dan `additionalProperties: false` mesti ditetapkan |
| `invalid_function_parameters: 'additionalProperties' is required` | Alat `strict: true` tiada `additionalProperties: false` | Tambah `"additionalProperties": false` ke objek parameter |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID function_call few-shot mempunyai awalan salah | ID panggilan fungsi mesti bermula dengan `fc_` (contoh, `fc_example1`), bukan `call_` |
| `missing_required_parameter: text.format.name` | Tambah kunci `"name"` ke dalam dict format (contoh, `"name": "Output"`) |
| `invalid_type: text.format` | Pastikan `text.format` adalah dict dengan kunci `type`, `name`, `strict`, `schema` — bukan string |
| `invalid input content type` | Gunakan jenis kandungan `input_text`/`output_text` bukan Chat `text` |
| `invalid input content type` (imej) | Kandungan imej masih menggunakan `"type": "image_url"` | Tukar kepada `"type": "input_image"` |
| `Expected object, got string` pada `image_url` | `image_url` masih objek bersarang `{"url": "..."}` | Rata-ratakan kepada string biasa: `"image_url": "https://..."` atau `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` untuk `max_output_tokens` | Minimum adalah **16** pada Azure OpenAI. Gunakan 50+ untuk ujian, 1000+ untuk pengeluaran. |
| `429 Too Many Requests` semasa penstriman | Had kadar dikenakan. Bungkus penstriman dalam `try/except`, hasilkan JSON ralat ke frontend, laksanakan penangguhan/cuba semula. |
| `KeyError: 'innererror'` pada ralat penapis kandungan | Struktur badan ralat penapis kandungan berubah dalam Responses API | Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]`; Responses API menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, di dalam array). Tulis semula semua akses `innererror`. |

---

## Jadual Risiko Migrasi

| Simptom | Kesalahan Mungkin | Pembetulan |
|---------|---------------|-----|
| `output_text` kosong / respons dipotong | `max_output_tokens` terlalu rendah untuk model penalaran | Tetapkan `max_output_tokens=1000` atau lebih tinggi — token penalaran dikira dalam had |
| `400 invalid_type: text.format` | Berikan string `response_format` bukan dict `text.format` | Gunakan `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` pada `/openai/v1/responses` | `base_url` salah — tiada akhiran `/openai/v1/` | Pastikan `base_url=f"{endpoint}/openai/v1/"` (dengan slash di akhir) |
| `401 Unauthorized` selepas bertukar ke `OpenAI()` | `api_key` tidak diset atau pemberi token tidak diserahkan dengan betul | Untuk EntraID: `api_key=token_provider` (yang callable). Untuk kunci API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model mengembalikan `deployment not found` | Param `model` tidak sepadan dengan nama penyebaran Azure anda | Gunakan `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — ini adalah nama penyebaran, bukan nama model |
| `json.loads(resp.output_text)` menjana `JSONDecodeError` | Skema tidak dikuatkuasakan atau model tidak menyokong JSON ketat | Pastikan `"strict": True` dalam skema, dan sahkan model menyokong output berstruktur |
| Penstriman tiada acara `delta` | Memeriksa jenis acara salah | Tampal pada `event.type == "response.output_text.delta"`, bukan Chat `chat.completion.chunk` |
| Ralat `400` pada input imej selepas migrasi | Jenis kandungan imej tidak dikemas kini | Tukar `"type": "image_url"` → `"type": "input_image"` dan rata-ratakan `"image_url": {"url": "..."}` → `"image_url": "..."` (string biasa) |
| Panggilan alat berulang tanpa henti | Keputusan alat hilang dalam `input` susulan | Selepas melaksanakan alat, tambahkan item `{"type": "function_call_output", "call_id": ..., "output": ...}` ke dalam `input` dalam permintaan seterusnya |
| Ralat `temperature` dengan GPT-5 atau siri o | Nilai `temperature` jelas selain 1 | Alih keluar `temperature` atau setkan ke `1` untuk model GPT-5 dan siri o (o1, o3-mini, o3, o4-mini) |
| Ralat `top_p` dengan siri o | `top_p` tidak disokong | Alih keluar `top_p` apabila mensasarkan model siri o |
| `max_completion_tokens` tidak dikenali | Menggunakan parameter khusus Azure | Gantikan `max_completion_tokens` dengan `max_output_tokens`. Tetapkan ke 4096+ bagi siri o (token penalaran dikira dalam had). |
| Output kosong/dipotong dari siri o | `max_output_tokens` terlalu rendah | Siri o menggunakan token penalaran secara dalaman. Tetapkan `max_output_tokens=4096` atau lebih tinggi — bukan 500–1000. |
| `400 integer_below_min_value` untuk `max_output_tokens` | Nilai di bawah 16 | Azure OpenAI menetapkan `max_output_tokens >= 16`. Gunakan 50+ untuk ujian smoke, 1000+ untuk pengeluaran. |
| `429 Too Many Requests` tengah penstriman | Had kadar dikenakan oleh Azure OpenAI | Aliran terhenti tanpa amaran ralat. Sentiasa bungkus `async for event in await coroutine:` dalam `try/except` dan hasilkan `{"error": str(e)}` ke frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Penyewa salah atau tidak log masuk | Serahkan `tenant_id=os.getenv("AZURE_TENANT_ID")` secara eksplisit. Jalankan `azd auth login --tenant <tenant-id>` secara tempatan. |
| `404 Not Found` menggunakan Model GitHub (`models.github.ai`) | Model GitHub tidak menyokong Responses API | Alih keluar laluan kod Model GitHub sepenuhnya. Gunakan Azure OpenAI, OpenAI, atau titik akhir tempatan yang sesuai (contoh, Ollama dengan sokongan Responses). |
| MAF `OpenAIChatCompletionClient` masih menggunakan Chat Completions | Menggunakan klien MAF lama dalam 1.0.0+ | Dalam MAF 1.0.0+, `OpenAIChatClient` menggunakan Responses API secara lalai. Gantikan `OpenAIChatCompletionClient` dengan `OpenAIChatClient`. Untuk sebelum 1.0.0, naik taraf ke `agent-framework-openai>=1.0.0`. |
| Ejen LangChain mengembalikan kosong atau gagal dengan panggilan alat | `ChatOpenAI` tidak menggunakan Responses API | Tambah `use_responses_api=True` ke `ChatOpenAI(...)`. Juga tukar `.content` → `.text` pada mesej respons. |
| `KeyError: 'innererror'` dalam pengendali ralat penapis kandungan | Struktur badan ralat berubah dalam Responses API | Tulis semula `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Penutup `innererror` hilang; butiran penapis kandungan kini dalam array tahap atas `content_filters` dengan `content_filter_results` (jamak) di dalam setiap entri. |
| Panggilan HTTP mentah ke `/openai/deployments/.../chat/completions` mengembalikan 404 | Titik akhir REST Chat Completions lama | Tulis semula URL ke `/openai/v1/responses`. Tukar badan permintaan: `messages` → `input`, tambah `max_output_tokens` + `store: false`, alih keluar param query `api-version`. Tukar parsing respons: `choices[0].message.content` → `output[0].content[0].text` (nota: `output_text` adalah sifat kemudahan SDK, bukan dalam JSON REST mentah). |

---

## Perkara Penting

1. Jika anda sebelum ini menggunakan Chat Completions untuk keadaan perbualan, uruskan keadaan sendiri dengan Responses secara eksplisit.
2. Utamakan `max_output_tokens` berbanding `max_tokens` lama.
3. Apabila bermigrasi ke `gpt-5`, pastikan `temperature` tidak ditentukan atau disetkan ke `1`.
4. Gantikan Chat `content[].type: "text"` dengan Responses `content[].type: "input_text"` untuk input pengguna/sistem.
5. Untuk `text.format`, sediakan dict yang betul (contoh, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), bukan string biasa.
6. Parameter `seed` tidak disokong dalam Responses; buangkannya dari permintaan.
7. **Penalaran**: Hanya sertakan `reasoning` jika kod asal sudah menggunakannya. Jangan tambahkan `reasoning` ke panggilan API yang tiada — banyak model (contoh, gpt-4o-mini) tidak menyokong parameter ini.
8. **Penentuan saiz `max_output_tokens`**: Untuk model penalaran (GPT-5-mini, GPT-5, siri o), gunakan `max_output_tokens=4096` atau lebih tinggi — bukan 50–1000. Model menggunakan token penalaran secara dalaman sebelum menjana output yang kelihatan; had terlalu rendah menyebabkan respons dipotong atau kosong.
9. **Siri o `max_completion_tokens`**: Jika kod asal menggunakan `max_completion_tokens` (khusus Azure untuk siri o), gantikan dengan `max_output_tokens`. Responses API tidak menerima `max_completion_tokens`.
10. **Siri o `reasoning_effort`**: Jika kod asal menggunakan `reasoning_effort` (rendah/sederhana/tinggi), migrasi kepada `reasoning={"effort": "<nilai>"}` dalam panggilan Responses API.
11. **Kelewatan penstriman siri o**: Model siri o menjalankan penalaran dalaman sebelum menjana output. Semasa penstriman, jangka kelewatan lebih lama sebelum acara pertama `response.output_text.delta`. Ini normal — model sedang berfikir, bukan tersekat.
9. **`_azure_ad_token_provider` tiada lagi**: `AsyncOpenAI` / `OpenAI` tiada atribut `_azure_ad_token_provider`. Ujian atau kod yang mengakses atribut ini akan gagal dengan `AttributeError`. Pemberi token diserahkan sebagai `api_key` dan tidak boleh diperiksa pada objek klien.
10. **Fail snapshot / golden**: Jika suite ujian menggunakan ujian snapshot, **semua** fail snapshot yang mengandungi bentuk penstriman Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, dan lain-lain) mesti dikemas kini ke bentuk Responses baru. Ini mudah terlepas dan menyebabkan kegagalan penegasan snapshot.
11. **Laluan monkeypatch mock**: Sasaran monkeypatch berubah daripada `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (atau `Responses.create` untuk sync). Menggunakan laluan lama tidak menghasilkan apa-apa — mock tidak akan mengganggu, dan ujian akan mengakses API sebenar atau gagal.
12. **`input` bukan `messages`**: Fungsi mock mesti baca `kwargs.get("input")` bukan `kwargs.get("messages")`. Responses API menggunakan `input` untuk sejarah perbualan.
13. **Penamaan pembolehubah persekitaran**: Azure Identity SDK menggunakan `AZURE_CLIENT_ID` (bukan `AZURE_OPENAI_CLIENT_ID`) untuk `ManagedIdentityCredential(client_id=...)`. Namakan semula dalam ujian, fail `.env`, tetapan aplikasi, dan Bicep/infrastruktur.
14. **Minimum `max_output_tokens` adalah 16**: Azure OpenAI menolak nilai di bawah 16 dengan `400 integer_below_min_value`. Gunakan `50` untuk ujian smoke, `1000`+ untuk pengeluaran. `max_tokens` lama tidak mempunyai minimum sedemikian.
15. **`tenant_id` untuk `AzureDeveloperCliCredential`**: Apabila sumber Azure OpenAI berada dalam penyewa berbeza, anda **mesti** serahkan `tenant_id` secara eksplisit — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Tanpanya, kelayakan menggunakan penyewa salah secara senyap dan mengembalikan `401`.
16. **Had kadar ditunjukkan berbeza dalam penstriman**: Dengan Chat Completions, 429 biasanya menghalang aliran bermula. Dengan penstriman Responses API, 429 boleh berlaku **tengah aliran** — pengulang async menjana pengecualian. Sentiasa bungkus gelung penstriman dalam `try/except` dan hasilkan baris JSON ralat supaya frontend dapat mengendalikan dengan kemas.

17. **Pengendalian ralat streaming adalah wajib untuk aplikasi web**: Corak `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` adalah kritikal. Tanpanya, aliran SSE/JSONL akan mati secara senyap apabila berlaku sebarang ralat di sisi pelayan dan antaramuka pengguna akan tergantung.
18. **Definisi alat mesti menggunakan format rata**: API Responses mengharapkan `{"type": "function", "name": ..., "parameters": ...}` — bukannya Chat Completions bersarang `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Ini adalah kesilapan migrasi yang paling biasa untuk kod panggilan fungsi.
19. **`pydantic_function_tool()` tidak serasi**: Pembantu `openai.pydantic_function_tool()` masih menghasilkan format lama yang bersarang. Jangan gunakan ia dengan `responses.create()`. Definisikan skema alat secara manual atau ratakan outputnya.
20. **Keputusan alat menggunakan `function_call_output`, bukan `role: tool`**: Selepas menjalankan alat, tambah `{"type": "function_call_output", "call_id": ..., "output": ...}` — bukan `{"role": "tool", "tool_call_id": ..., "content": ...}`. Untuk permintaan alat pembantu, gunakan `messages.extend(response.output)` — bukan kamus manual `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` memerlukan `required` + `additionalProperties: false`**: Apabila menggunakan `strict: true` pada alat, setiap sifat mesti disenaraikan dalam array `required` dan `additionalProperties` mesti `false`. Ketiadaan salah satu akan menyebabkan ralat 400.
22. **ID panggilan fungsi mempunyai awalan khusus**: Apabila menyediakan item `function_call` beberapa contoh dalam `input`, medan `id` mesti bermula dengan `fc_` dan medan `call_id` mesti bermula dengan `call_` (contoh, `"id": "fc_example1", "call_id": "call_example1"`). Menggunakan awalan lama Chat Completions `call_` untuk `id` akan ditolak.
23. **GitHub Models tidak menyokong Responses API**: Jika aplikasi mempunyai laluan kod GitHub Models (`base_url` menunjuk ke `models.github.ai` atau `models.inference.ai.azure.com`), hapuskan sepenuhnya. Tiada laluan migrasi — beralih ke Azure OpenAI, OpenAI, atau titik hujung tempatan yang serasi.
24. **Struktur badan ralat penapis kandungan telah berubah**: Ralat Chat Completions menggunakan `error.body["innererror"]["content_filter_result"]` (tunggal). Ralat Responses API menggunakan `error.body["content_filters"][0]["content_filter_results"]` (jamak, dalam tatasusunan). Kunci `innererror` tidak lagi wujud. Kod yang terus mengakses `innererror` akan menyebabkan `KeyError` semasa runtime — ini mudah terlepas semasa migrasi kerana hanya muncul apabila penapis kandungan benar-benar diaktifkan. Sentiasa grep untuk `innererror` semasa migrasi.
25. **Panggilan HTTP mentah perlu ubah suai URL + badan**: Aplikasi yang membuat panggilan REST Azure OpenAI secara langsung (melalui `requests`, `httpx`, `aiohttp`) menggunakan `/openai/deployments/{name}/chat/completions?api-version=...` mesti beralih ke `/openai/v1/responses`. Badan permintaan menggunakan `input` bukan `messages`, memerlukan `max_output_tokens` dan `store`, dan parameter kueri `api-version` dibuang. Teks badan respons terdapat pada `output[0].content[0].text` — **bukan** `output_text`, yang merupakan sifat kemudahan SDK yang tidak terdapat dalam JSON REST mentah.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->