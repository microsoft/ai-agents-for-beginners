# Log Perubahan

Semua perubahan ketara untuk kursus **Ejen AI untuk Pemula** didokumentasikan dalam fail ini.

## [Belum Dikeluarkan] — 2026-07-06

Keluaran ini menghijrahkan kursus ke dalam **API Tindak Balas Azure OpenAI**, menyeragamkan penamaan produk pada **Microsoft Foundry** dan **Microsoft Agent Framework (MAF)**, menghentikan Penggunaan Model GitHub, mengemas kini versi SDK, dan menambah kandungan baru mengenai model tempatan dan pengehosan rangka kerja lain pada Foundry.

### Ditambah

- **Kemahiran migrasi** — Memasang Kemahiran Ejen [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (dari [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) di bawah `.agents/skills/`, termasuk rujukan dan skrip pengimbasannya.
- **Foundry Tempatan (jalankan model pada peranti)** — Bahagian baru "Penyedia Alternatif: Foundry Tempatan" dalam [00-course-setup/README.md](./00-course-setup/README.md) yang menerangkan pemasangan (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, serta penyambungan `FoundryLocalManager` ke Microsoft Agent Framework melalui `OpenAIChatClient`.
- **Pengehosan agen LangChain / LangGraph pada Microsoft Foundry** — Bahagian baru dalam [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) serta contoh yang boleh dijalankan [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) menggunakan `langchain-azure-ai[hosting]` dan `ResponsesHostServer` (protokol `/responses`), berdasarkan [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Bahagian baru "Contoh Dunia Sebenar: Microsoft Project Opal" dalam [15-browser-use/README.md](./15-browser-use/README.md) yang memperlihatkan Opal sebagai ejen penggunaan komputer enterprise dan memadankannya dengan konsep kursus (manusia dalam kitaran, kepercayaan/keselamatan, perancangan, Kemahiran).
- **Contoh Python Pelajaran Kedua 02** — Ditambah [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (rujuk "Diubah" — berhijrah dari nota Semantic Kernel yang lama) dan dipautkan dalam README pelajaran.
- Ditambah bahagian **Model dan Penyedia** dalam [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Diubah

- **Chat Completions → Responses API (Python).** Contoh yang memanggil model secara langsung telah berhijrah dari Chat Completions ke Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), menggunakan klien `OpenAI` terhadap titik akhir Azure OpenAI `/openai/v1/` yang stabil (tiada `api_version`). Contoh terlibat termasuk:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — langkah lengkap penggunaan fungsi seruan (skema alat diratakan kepada format Responses, keputusan alat dikembalikan sebagai `function_call_output`, `max_output_tokens`, dll.).
- **Model GitHub → Azure OpenAI.** Model GitHub telah dihentikan (dijangka berhenti **Julai 2026**) dan tidak menyokong Responses API. Semua laluan kod Model GitHub telah ditukar kepada Azure OpenAI / Microsoft Foundry dalam contoh Python dan .NET:
  - Python: nota kerja Pelajaran 08 (`01`–`03`), Pelajaran 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` fail `*-dotnet-agent-framework.cs` + dokumen `.md` pendamping, dan nota kerja .NET Pelajaran 08/`.md` (`01`–`03`) kini menggunakan `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` dengan `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Fail `02-semantic-kernel.ipynb` yang lama ditulis semula untuk menggunakan Microsoft Agent Framework dengan Azure OpenAI (Responses API) dan dinamakan semula kepada `02-python-agent-framework-azure-openai.ipynb`.
- **Standar pada `FoundryChatClient` + `as_agent`.** Kod README dan nota yang merujuk `AzureAIProjectAgentProvider` diseragamkan menggunakan corak rasmi seperti yang digunakan dalam Pelajaran 01 dan contoh rangka kerja sendiri: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` dengan `provider.as_agent(...)`. Dikemaskini merentas README dan nota Pelajaran 02–14 (contohnya, memori Pelajaran 13, semua nota Pelajaran 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Penamaan produk.** Ditukar serata kandungan Bahasa Inggeris:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Tidak berubah: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", dan nama pembolehubah persekitaran.)
- **Kebergantungan** ([requirements.txt](../../requirements.txt)):
  - Tetapkan `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Tetapkan `openai>=1.108.1` (minimum untuk Responses API).
  - Buang `azure-ai-inference` (hanya digunakan oleh contoh Model GitHub yang berhijrah).
- **Konfigurasi persekitaran** ([.env.example](../../.env.example)): keluarkan pembolehubah Model GitHub (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); tambah `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, dan pilihan `AZURE_OPENAI_API_KEY`; kemas kini penamaan ke Microsoft Foundry.
- **Dokumen** — Kemas kini [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), dan [STUDY_GUIDE.md](./STUDY_GUIDE.md) untuk perkara di atas (tetapkan pembolehubah persekitaran, snippet pengesahan, panduan penyedia, penamaan).

### Dibuang

- Langkah onboarding Model GitHub dan pembolehubah persekitaran dari dokumen persediaan (digantikan oleh Azure OpenAI / Microsoft Foundry).

### Keselamatan / Privasi (pembersihan perkongsian awam)

- Bersihkan output pelaksanaan Jupyter notebook yang mendedahkan **ID langganan Azure** sebenar, nama kumpulan sumber / sumber, dan ID sambungan Bing, serta **laluan fail tempatan dan nama pengguna** pembangun, dalam:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Sahkan tiada kunci API, token, ID langganan, atau laluan peribadi kekal dalam kandungan Bahasa Inggeris yang dijejak (rujukan `GITHUB_TOKEN` yang tinggal adalah token GitHub Actions dalam workflow dan PAT pelayan GitHub MCP dalam persediaan Pelajaran 11 — kedua-duanya sah dan tidak berkaitan Model GitHub).

### Nota dan had diketahui

- **Tidak dilaksanakan/dikompilasi.** Ini adalah contoh pendidikan yang dikemas kini untuk kesahihan API/penamaan; mereka tidak dijalankan terhadap sumber Azure sebenar, dan contoh .NET tidak dikompilasi dalam persekitaran ini. Sahkan dengan penghantaran Microsoft Foundry / Azure OpenAI anda sendiri.
- **Penghantaran model mesti menyokong Responses API.** Gunakan penghantaran seperti `gpt-4o-mini`, `gpt-4.1`, atau model `gpt-5.x`. Model lama menyokong fungsi teras Responses tetapi tidak semua ciri.
- **Versi agent-framework.** Contoh menyasarkan MAF terkini (`>=1.10.0`). Panggilan penciptaan ejen rasmi adalah `client.as_agent(...)`; API disahkan dengan dokumen yang diterbitkan dan binaan terpasang rangka kerja. Jika anda menetapkan versi lain, sahkan ketersediaan kaedah (`as_agent` vs `create_agent`).
- **Nota kerja alur Pelajaran 08 04** sengaja mengekalkan `AzureAIAgentClient` (dari `agent-framework-azure-ai`) kerana ia menggunakan alat Microsoft Foundry Agent Service yang dihoskan (asas Bing, penterjemah kod); ia sudah berasaskan Responses.
- **Penghantaran lalai .NET.** Dua contoh alur kerja dotNET Pelajaran 08 yang sebelum ini kod keras `gpt-4o`; kini lalai kepada `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). Jika contoh bergantung pada input multimodal/visi, tetapkan `AZURE_OPENAI_DEPLOYMENT` kepada model yang sesuai.
- **Foundry Tempatan** menyediakan titik akhir **Chat Completions** yang serasi OpenAI dan dimaksudkan untuk pembangunan tempatan; gunakan Azure OpenAI / Microsoft Foundry untuk set ciri penuh API Responses.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->