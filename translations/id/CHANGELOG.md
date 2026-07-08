# Daftar Perubahan

Semua perubahan penting pada kursus **AI Agents for Beginners** didokumentasikan dalam file ini.

## [Belum Dirilis] — 2026-07-06

Rilis ini memigrasikan kursus ke **Azure OpenAI Responses API**, menstandarisasi penamaan produk pada **Microsoft Foundry** dan **Microsoft Agent Framework (MAF)**, menghentikan GitHub Models, memperbarui versi SDK, dan menambahkan konten baru tentang model lokal serta hosting framework lain di Foundry.

### Ditambahkan

- **Keterampilan migrasi** — Menginstal Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (dari [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) di bawah `.agents/skills/`, termasuk referensi dan skrip pemindaiannya.
- **Foundry Lokal (jalankan model di perangkat)** — Bagian baru "Alternative Provider: Foundry Local" di [00-course-setup/README.md](./00-course-setup/README.md) yang membahas instalasi (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, dan menghubungkan `FoundryLocalManager` ke Microsoft Agent Framework melalui `OpenAIChatClient`.
- **Hosting agen LangChain / LangGraph di Microsoft Foundry** — Bagian baru di [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus contoh bisa dijalankan [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) menggunakan `langchain-azure-ai[hosting]` dan `ResponsesHostServer` (protokol `/responses`), berdasarkan [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Bagian baru "Contoh Dunia Nyata: Microsoft Project Opal" di [15-browser-use/README.md](./15-browser-use/README.md) yang menempatkan Opal sebagai agen penggunaan komputer perusahaan dan memetakan ke konsep kursus (human-in-the-loop, kepercayaan/keamanan, perencanaan, Keterampilan).
- **Sample Python Pelajaran Kedua 02** — Menambahkan [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (lihat "Diubah" — dimigrasi dari notebook Semantic Kernel sebelumnya) dan menautkannya di README pelajaran.
- Menambahkan bagian **Models and Providers** pada [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Diubah

- **Chat Completions → Responses API (Python).** Contoh yang memanggil model secara langsung dimigrasikan dari Chat Completions ke Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), menggunakan klien `OpenAI` ke endpoint Azure OpenAI `/openai/v1/` yang stabil (tanpa `api_version`). Contoh terpengaruh termasuk:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — walkthrough lengkap pemanggilan fungsi (skema alat diratakan ke format Responses, hasil alat dikembalikan sebagai `function_call_output`, `max_output_tokens`, dll.).
- **GitHub Models → Azure OpenAI.** GitHub Models dihentikan (akan pensiun **Juli 2026**) dan tidak mendukung Responses API. Semua jalur kode GitHub Models diubah ke Azure OpenAI / Microsoft Foundry di contoh Python dan .NET:
  - Python: Notebook workflow Pelajaran 08 (`01`–`03`), Pelajaran 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + dokumen `.md` pendamping, dan notebook/`.md` workflow dotNET Pelajaran 08 (`01`–`03`) sekarang menggunakan `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` dengan `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Notebook `02-semantic-kernel.ipynb` yang sebelumnya diubah menjadi menggunakan Microsoft Agent Framework dengan Azure OpenAI (Responses API) dan diubah nama menjadi `02-python-agent-framework-azure-openai.ipynb`.
- **Distandarisasi pada `FoundryChatClient` + `as_agent`.** Kode README dan notebook yang menyebutkan `AzureAIProjectAgentProvider` distandarisasi dengan pola kanonik yang digunakan oleh Pelajaran 01 dan contoh framework sendiri: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` dengan `provider.as_agent(...)`. Diperbarui di seluruh README dan notebook Pelajaran 02–14 (misalnya, memori Pelajaran 13, semua notebook Pelajaran 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Penamaan produk.** Diubah di seluruh konten bahasa Inggris:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Tidak diubah: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", dan nama variabel lingkungan.)
- **Dependencies** ([requirements.txt](../../requirements.txt)):
  - Mematok `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Mematok `openai>=1.108.1` (minimum untuk Responses API).
  - Menghapus `azure-ai-inference` (hanya dipakai oleh contoh GitHub Models yang dimigrasi).
- **Konfigurasi lingkungan** ([.env.example](../../.env.example)): menghapus variabel GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); menambahkan `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, dan `AZURE_OPENAI_API_KEY` opsional; memperbarui penamaan ke Microsoft Foundry.
- **Dokumentasi** — Memperbarui [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), dan [STUDY_GUIDE.md](./STUDY_GUIDE.md) untuk hal di atas (pengaturan variabel lingkungan, potongan pemeriksaan, panduan penyedia, penamaan).

### Dihapus

- Langkah onboarding GitHub Models dan variabel lingkungan dari dokumen setup (digantikan oleh Azure OpenAI / Microsoft Foundry).

### Keamanan / Privasi (pembersihan berbagi publik)

- Membersihkan output eksekusi notebook Jupyter yang membocorkan **ID langganan Azure** asli, nama grup sumber daya / sumber daya, dan ID koneksi Bing, serta jalur file lokal dan nama pengguna pengembang, di:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Memastikan tidak ada kunci API, token, ID langganan, atau jalur pribadi yang tersisa dalam konten bahasa Inggris yang dilacak (referensi `GITHUB_TOKEN` yang tersisa adalah token GitHub Actions di workflow dan PAT server GitHub MCP di pengaturan Pelajaran 11 — keduanya sah dan tidak terkait dengan GitHub Models).

### Catatan dan keterbatasan yang diketahui

- **Tidak dieksekusi/dikompilasi.** Ini adalah contoh edukasi yang diperbarui untuk keakuratan API/penamaan; mereka tidak dijalankan pada sumber daya Azure yang nyata, dan contoh .NET tidak dikompilasi di lingkungan ini. Validasi menggunakan Microsoft Foundry / Azure OpenAI yang Anda miliki.
- **Deployment model harus mendukung Responses API.** Gunakan deployment seperti `gpt-4o-mini`, `gpt-4.1`, atau model `gpt-5.x`. Model lama mendukung fungsi inti Responses tapi tidak semua fitur.
- **Versi agent-framework.** Contoh menargetkan MAF terbaru (`>=1.10.0`). Panggilan pembuatan agen kanonik adalah `client.as_agent(...)`; API divalidasi berdasarkan dokumentasi resmi framework dan build yang diinstal. Jika menggunakan versi lain, pastikan metode tersedia (`as_agent` vs `create_agent`).
- **Notebook workflow Pelajaran 08 nomor 04** dengan sengaja mempertahankan `AzureAIAgentClient` (dari `agent-framework-azure-ai`) karena menggunakan alat yang dihosting layanan Microsoft Foundry Agent (Bing grounding, interpreter kode); sudah berbasis Responses.
- **Deployment default .NET.** Dua contoh workflow dotNET Pelajaran 08 sebelumnya menggunakan `gpt-4o` yang di-hardcode; sekarang menggunakan default `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Jika contoh menggunakan input multimodal/vision, atur `AZURE_OPENAI_DEPLOYMENT` ke model yang sesuai.
- **Foundry Lokal** menyediakan endpoint OpenAI-kompatibel **Chat Completions** dan dimaksudkan untuk pengembangan lokal; gunakan Azure OpenAI / Microsoft Foundry untuk fitur lengkap Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->