# Changelog

Semua perubahan penting pada kursus **AI Agents untuk Pemula** didokumentasikan dalam file ini.

## [Dirilis] — 2026-07-14

Rilis ini memindahkan kursus dari dua model yang baru saja tidak digunakan lagi, memigrasi notebook Lesson yang tersisa ke API Microsoft Agent Framework yang stabil, dan memvalidasi notebook Python terhadap deployment Microsoft Foundry yang hidup.

### Diubah

- **Berpindah dari model yang sudah tidak digunakan (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Baik `gpt-4.1` maupun `gpt-4.1-mini` sekarang sudah tidak digunakan lagi (tanggal pensiun yang diterbitkan **14 Oktober 2026**). Mengganti setiap referensi kursus (dokumen, `.env.example`, notebook dan sampel Python/.NET) dengan `gpt-5-mini` yang tidak digunakan lagi. Contoh routing model di Lesson 16 mempertahankan kontras kecil/besar menggunakan `gpt-5-nano` (kecil) dan `gpt-5-mini` (besar). File pihak ketiga yang disertakan ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), teks model GitHub historis, dan catatan kemampuan pada skill `azure-openai-to-responses` sengaja tidak diubah.
- **Notebook handoff Lesson 14 dimigrasi ke API stabil.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) sekarang menggunakan `agent_framework.orchestrations.HandoffBuilder` dengan `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streaming berbasis `event.type`, dan `FoundryChatClient` (mengganti simbol `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` pra-1.0 yang dihapus).
- **Notebook human-in-the-loop Lesson 14 dimigrasi ke API stabil.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) sekarang menghentikan sementara melalui `ctx.request_info(...)` + `@response_handler` (menggantikan `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` yang dihapus), membangun dengan `WorkflowBuilder(start_executor=..., output_executors=[...])`, mengarahkan keluaran terstruktur melalui `default_options={"response_format": ...}`, dan menggunakan jawaban secara skrip supaya notebook berjalan tanpa pengawasan (tidak ada blocking `input()`).
- **Konfigurasi lingkungan** ([.env.example](../../.env.example)): mengganti nama deployment model ke `gpt-5-mini`; menambahkan `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (routing Lesson 16) dan `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` yang sebelumnya hilang (penggunaan browser Lesson 15).
- **Ketergantungan** ([requirements.txt](../../requirements.txt)): mengunci `agent-framework`, `agent-framework-foundry`, dan `agent-framework-openai` ke versi `~=1.10.0` untuk set yang konsisten dan tervalidasi (1.11.0 mengandung perubahan eksperimental yang memecah permukaan yang digunakan pelajaran ini).

### Catatan dan keterbatasan yang diketahui

- **Telah divalidasi terhadap Microsoft Foundry yang hidup.** Notebook Python dieksekusi tanpa kepala menggunakan `nbconvert` terhadap proyek Microsoft Foundry dengan `gpt-5-mini` (dan `gpt-5-nano` untuk routing Lesson 16). Deploy model non-deprecated yang setara dalam proyek Anda sendiri; notebook membaca nama deployment dari `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Masih memerlukan sumber daya ekstra untuk beberapa pelajaran.** Lesson 05 memerlukan Azure AI Search; workflow pembumian Bing di Lesson 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) memerlukan koneksi Bing dan alat hosting Microsoft Foundry Agent Service; Lesson 13 (Cognee) dan Lesson 17 (Foundry Lokal) memerlukan runtime masing-masing.

## [Dirilis] — 2026-07-13

Rilis ini menambahkan dua pelajaran baru yang menyelesaikan lengkungan deployment — menskalakan agen ke Microsoft Foundry dan menurun ke satu workstation — plus pipeline uji asap, navigasi kursus yang disegarkan, keterampilan pembelajar baru, dan pembaruan merek.

### Ditambahkan

- **Lesson 16 — Men-deploy Agen yang Dapat Diskalakan dengan Microsoft Foundry.** Pelajaran baru [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) dan notebook dapat dijalankan [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) membangun agen dukungan pelanggan produksi (alat, RAG, memori, routing model, caching respons, persetujuan manusia, gerbang evaluasi, dan pelacakan OpenTelemetry), dengan diagram Mermaid pengembangan/deployment/runtime, pemeriksaan pengetahuan, tugas, dan tantangan.
- **Lesson 17 — Membuat Agen AI Lokal dengan Foundry Local dan Qwen.** Pelajaran baru [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) dan notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) membangun asisten teknik sepenuhnya di perangkat (pemanggilan fungsi Qwen via Foundry Local, alat file sandboxed, RAG lokal dengan Chroma, MCP lokal opsional), dengan diagram hanya lokal / RAG lokal / pemanggilan alat, pemeriksaan pengetahuan, tugas, dan tantangan.
- **Pipeline uji asap.** Workflow baru [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus katalog per pelajaran di bawah [tests/](./tests/README.md) untuk agen yang dapat dideploy di Lessons 01, 04, 05, dan 16, dengan README indeks yang memetakan setiap katalog ke pelajaran dan nama agen yang dihosting. Lesson 16 mendapat bagian "Memvalidasi Agen yang Dideploy dengan Smoke Tests"; Lessons 01/04/05 mendapat penunjuk uji asap opsional.
- **Keterampilan pembelajar.** Keterampilan Agen baru di bawah `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (mengemas panduan Lesson 16 dan 17), dan [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (cara memvalidasi sampel notebook terhadap setup Microsoft Foundry / Azure OpenAI yang hidup).
- **Runner validasi notebook.** Baru [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) yang menjalankan setiap notebook Python tanpa kepala menggunakan `nbconvert` dan mencetak matriks PASS/FAIL (plus `results.json`). Mendeteksi akar repo dan Python secara otomatis, mengecualikan notebook non-kursus (`.venv`, `site-packages`, `translations`, aset template skill) dan notebook `.NET` secara default, serta mendukung `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, dan `-Python`.
- **Navigasi kursus.** Menambahkan tautan pelajaran Sebelumnya/Berikutnya ke Lessons 11–15 (yang sebelumnya hilang) sehingga seluruh kursus mengalir 00 → 18 ke dua arah.
- **Thumbnail baru.** Thumbnail pelajaran untuk Lessons 16 dan 17, plus gambar sosial repositori yang diperbarui [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (sekarang mengiklankan dua pelajaran baru dan URL `aka.ms/ai-agents-beginners`).
- **Ketergantungan** ([requirements.txt](../../requirements.txt)): ditambahkan `foundry-local-sdk` dan `chromadb` untuk Lesson 17.

### Diubah

- **Tabel pelajaran utama di [README.md](./README.md)**: Lessons 16 dan 17 sekarang menautkan ke isi mereka (sebelumnya "Segera Hadir"); gambar repositori diubah ke `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: menambahkan Lessons 16 dan 17 ke panduan pelajaran per pelajaran dan jalur pembelajaran, serta bagian "Memvalidasi Agen yang Dideploy dengan Smoke Tests".
- **[AGENTS.md](./AGENTS.md)**: memperbarui jumlah/deskripsi pelajaran (00–18), menambahkan bagian validasi uji asap, dan contohnama sampel Lesson 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Pelajaran Sebelumnya" sekarang menunjuk ke Lesson 17 (sebelumnya Lesson 15), menutup rantai.
- **Standarisasi referensi model pada model yang tidak deprecated.** Mengganti semua referensi `gpt-4o` / `gpt-4o-mini` di seluruh kursus (dokumen, `.env.example`, notebook dan sampel Python/.NET) dengan `gpt-4.1-mini` — `gpt-4o` (semua versi) akan pensiun pada 2026. Contoh routing model di Lesson 16 mempertahankan kontras kecil/besar menggunakan `gpt-4.1-mini` (kecil) dan `gpt-4.1` (besar). Notebook Python sekarang memilih model dari variabel lingkungan (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) daripada mengkodekan nama model secara keras.

### Catatan dan keterbatasan yang diketahui

- **Tidak dijalankan terhadap Azure yang hidup.** Notebook pelajaran baru adalah sampel pendidikan; jalankan dan validasi terhadap setup Microsoft Foundry / Foundry Lokal Anda sendiri. Workflow uji asap mengharuskan Anda men-deploy agen pelajaran dan mengonfigurasi rahasia Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) dengan peran **Azure AI User** pada cakupan proyek Foundry.
- **Lesson 17 hanya lokal.** Ia tidak memiliki endpoint Foundry Responses, sehingga aksi uji asap tidak berlaku; validasi dengan menjalankan notebook pada workstation Anda.

## [Dirilis] — 2026-07-06

Rilis ini memigrasi kursus ke **Azure OpenAI Responses API**, menstandarisasi penamaan produk pada **Microsoft Foundry** dan **Microsoft Agent Framework (MAF)**, menghentikan GitHub Models, memperbarui versi SDK, dan menambahkan isi baru tentang model lokal dan hosting kerangka kerja lain pada Foundry.

### Ditambahkan

- **Keterampilan migrasi** — Memasang Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (dari [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) di bawah `.agents/skills/`, termasuk referensi dan skrip pemindaiannya.
- **Foundry Lokal (menjalankan model di perangkat)** — Bagian baru "Penyedia Alternatif: Foundry Local" di [00-course-setup/README.md](./00-course-setup/README.md) yang membahas instalasi (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, dan pengkabelan `FoundryLocalManager` ke Microsoft Agent Framework melalui `OpenAIChatClient`.
- **Hosting agen LangChain / LangGraph pada Microsoft Foundry** — Bagian baru di [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus sampel yang dapat dijalankan [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) menggunakan `langchain-azure-ai[hosting]` dan `ResponsesHostServer` (protokol `/responses`), berdasarkan [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Bagian baru "Contoh Dunia Nyata: Microsoft Project Opal" di [15-browser-use/README.md](./15-browser-use/README.md) membingkai Opal sebagai agen penggunaan komputer perusahaan dan memetakannya ke konsep kursus (human-in-the-loop, kepercayaan/keamanan, perencanaan, Keterampilan).
- **Contoh Python Lesson 02 kedua** — Menambahkan [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (lihat "Diubah" — dimigrasi dari notebook Semantic Kernel sebelumnya) dan menautkannya di README pelajaran.
- Menambahkan bagian Models and Providers pada [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Diubah

- **Chat Completions → Responses API (Python).** Sampel yang memanggil model secara langsung dimigrasi dari Chat Completions ke Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), menggunakan klien `OpenAI` terhadap endpoint Azure OpenAI `/openai/v1/` yang stabil (tanpa `api_version`). Sampel yang terpengaruh termasuk:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — walkthrough fungsi-panggilan penuh (skema alat diratakan ke format Responses, hasil alat dikembalikan sebagai `function_call_output`, `max_output_tokens`, dll.).

- **Model GitHub → Azure OpenAI.** Model GitHub sudah usang (akan dihentikan **Juli 2026**) dan tidak mendukung Responses API. Semua jalur kode Model GitHub diubah ke Azure OpenAI / Microsoft Foundry pada contoh Python dan .NET:
  - Python: Buku catatan alur kerja Lesson 08 (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + dokumen `.md` pendamping, dan buku catatan/.md alur kerja Lesson 08 dotNET (`01`–`03`) sekarang menggunakan `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` dengan `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** `02-semantic-kernel.ipynb` sebelumnya ditulis ulang untuk menggunakan Microsoft Agent Framework dengan Azure OpenAI (Responses API) dan diubah namanya menjadi `02-python-agent-framework-azure-openai.ipynb`.
- **Standarisasi pada `FoundryChatClient` + `as_agent`.** README dan kode buku catatan yang merujuk `AzureAIProjectAgentProvider` distandarisasi pada pola kanonik yang digunakan oleh Lesson 01 dan contoh kerangka kerja itu sendiri: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` dengan `provider.as_agent(...)`. Diperbarui di seluruh README dan buku catatan Lesson 02–14 (misalnya, memori Lesson 13, semua buku catatan Lesson 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Penamaan produk.** Diubah di seluruh konten bahasa Inggris:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Tidak berubah: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", dan nama variabel lingkungan.)
- **Dependensi** ([requirements.txt](../../requirements.txt)):
  - Dipatok `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Dipatok `openai>=1.108.1` (minimum untuk Responses API).
  - Dihapus `azure-ai-inference` (hanya digunakan oleh contoh Model GitHub yang sudah dipindahkan).
- **Konfigurasi lingkungan** ([.env.example](../../.env.example)): menghapus variabel Model GitHub (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); menambahkan `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, dan opsional `AZURE_OPENAI_API_KEY`; memperbarui penamaan ke Microsoft Foundry.
- **Dokumentasi** — Memperbarui [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), dan [STUDY_GUIDE.md](./STUDY_GUIDE.md) untuk hal di atas (penyiapan variabel lingkungan, potongan verifikasi, panduan penyedia, penamaan).

### Dihapus

- Langkah onboarding Model GitHub dan variabel lingkungan dari dokumen setup (digantikan oleh Azure OpenAI / Microsoft Foundry).

### Keamanan / Privasi (pembersihan berbagi publik)

- Menghapus hasil eksekusi buku catatan Jupyter yang membocorkan **ID langganan Azure sungguhan**, nama grup sumber daya / sumber daya, dan ID koneksi Bing, serta **jalur file lokal dan nama pengguna** pengembang, di:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Memastikan tidak ada kunci API, token, ID langganan, atau jalur pribadi yang tersisa di konten bahasa Inggris yang dilacak (referensi `GITHUB_TOKEN` yang tersisa adalah token GitHub Actions di alur kerja dan PAT server GitHub MCP di setup Lesson 11 – keduanya sah dan tidak terkait dengan Model GitHub).

### Catatan dan batasan yang diketahui

- **Tidak dieksekusi/disusun.** Ini adalah contoh edukasi yang diperbarui untuk ketepatan API/penamaan; mereka tidak dijalankan terhadap sumber daya Azure secara langsung, dan contoh .NET tidak disusun di lingkungan ini. Validasi terhadap penyebaran Microsoft Foundry / Azure OpenAI Anda sendiri.
- **Penerapan model harus mendukung Responses API.** Gunakan penerapan seperti `gpt-4.1-mini`, `gpt-4.1`, atau model `gpt-5.x`. Model lama mendukung fungsi inti Responses tetapi tidak semua fitur.
- **Versi agent-framework.** Contoh menargetkan MAF terbaru (`>=1.10.0`). Panggilan penciptaan agen kanonik adalah `client.as_agent(...)`; API diverifikasi terhadap dokumentasi resmi framework dan build terpasang. Jika Anda memasang versi berbeda, konfirmasi ketersediaan metode (`as_agent` vs `create_agent`).
- **Buku catatan alur kerja Lesson 08 nomor 04** sengaja mempertahankan `AzureAIAgentClient` (dari `agent-framework-azure-ai`) karena menggunakan alat layanan Microsoft Foundry Agent Service yang dihosting (dasar Bing, penerjemah kode); sudah berbasis Responses.
- **Penerapan default .NET.** Dua contoh alur kerja Lesson 08 dotNET sebelumnya mengkodekan model tertentu; sekarang default ke `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Jika contoh tergantung pada input multimodal/visi, setel `AZURE_OPENAI_DEPLOYMENT` ke model yang sesuai.
- **Foundry Local** menyediakan endpoint **Chat Completions** yang kompatibel OpenAI dan dimaksudkan untuk pengembangan lokal; gunakan Azure OpenAI / Microsoft Foundry untuk fitur lengkap Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->