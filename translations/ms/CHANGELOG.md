# Perubahan

Semua perubahan penting untuk kursus **Ejen AI untuk Pemula** didokumenkan dalam fail ini.

## [Dilepaskan] — 2026-07-14

Siaran ini memindahkan kursus dari dua model yang baru sahaja tidak digunakan, memindahkan buku nota Pelajaran yang tinggal ke API Bingkai Ejen Microsoft yang stabil, dan mengesahkan buku nota Python terhadap penyebaran Microsoft Foundry yang hidup.

### Ditukar

- **Berpindah dari model yang tidak digunakan (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Kedua-dua `gpt-4.1` dan `gpt-4.1-mini` kini tidak digunakan lagi (tarikh persaraan yang diterbitkan **14 Oktober 2026**). Menggantikan setiap rujukan kursus (dokumen, `.env.example`, buku nota Python/.NET dan contoh) dengan `gpt-5-mini` yang tidak digunakan lagi. Contoh penghalaan model Pelajaran 16 mengekalkan kontras kecil/besar menggunakan `gpt-5-nano` (kecil) dan `gpt-5-mini` (besar). Fail pihak ketiga yang dijual ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), teks Model GitHub sejarah, dan nota kemampuan kemahiran `azure-openai-to-responses` dengan sengaja dibiarkan tidak berubah.
- **Notebook penyerahan Pelajaran 14 dipindahkan ke API stabil.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) kini menggunakan `agent_framework.orchestrations.HandoffBuilder` dengan `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, penstriman berasaskan `event.type`, dan `FoundryChatClient` (menggantikan simbol `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` pra-1.0 yang dibuang).
- **Notebook manusia-dalam-gelung Pelajaran 14 dipindahkan ke API stabil.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) kini berhenti seketika melalui `ctx.request_info(...)` + `@response_handler` (menggantikan `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` yang dibuang), membina dengan `WorkflowBuilder(start_executor=..., output_executors=[...])`, mengawal output berstruktur melalui `default_options={"response_format": ...}`, dan menggunakan jawapan berskrip supaya buku nota berjalan tanpa pengawasan (tanpa `input()` yang menyekat).
- **Konfigurasi persekitaran** ([.env.example](../../.env.example)): menukar nama penyebaran model kepada `gpt-5-mini`; menambah `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (penghalaan Pelajaran 16) dan `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` yang sebelum ini hilang (penggunaan pelayar Pelajaran 15).
- **Kebergantungan** ([requirements.txt](../../requirements.txt)): memaku `agent-framework`, `agent-framework-foundry`, dan `agent-framework-openai` kepada `~=1.10.0` untuk set yang konsisten sendiri dan disahkan (1.11.0 mengandungi perubahan pecah eksperimental pada permukaan yang digunakan pelajaran ini).

### Nota dan had yang diketahui

- **Disahkan terhadap Microsoft Foundry yang hidup.** Buku nota Python dijalankan tanpa kepala dengan `nbconvert` terhadap projek Microsoft Foundry menggunakan `gpt-5-mini` (dan `gpt-5-nano` untuk penghalaan Pelajaran 16). Sebarkan model bukan usang setara dalam projek anda sendiri; buku nota membaca nama penyebaran dari `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Masih memerlukan sumber tambahan untuk beberapa pelajaran.** Pelajaran 05 memerlukan Azure AI Search; aliran kerja berasaskan Bing Pelajaran 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) memerlukan sambungan Bing dan alat hos Perkhidmatan Ejen Microsoft Foundry; Pelajaran 13 (Cognee) dan Pelajaran 17 (Foundry Local) memerlukan masa jalan sendiri.

## [Dilepaskan] — 2026-07-13

Siaran ini menambah dua pelajaran baru yang melengkapkan arka penyebaran — skala ejen ke Microsoft Foundry dan ke stesen kerja tunggal — serta talian uji asap, navigasi kursus yang diperkemas, kemahiran pelajar baru, dan penjenamaan terkini.

### Ditambah

- **Pelajaran 16 — Menyebarkan Ejen Skala dengan Microsoft Foundry.** Pelajaran baru [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) dan buku nota boleh dijalankan [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) membina ejen sokongan pelanggan produksi (alat, RAG, memori, penghalaan model, cache respons, kelulusan manusia, pintu penilaian, dan penjejakan OpenTelemetry), dengan rajah pembangunan/penyebaran/masa jalan Mermaid, semakan pengetahuan, tugasan, dan cabaran.
- **Pelajaran 17 — Mencipta Ejen AI Tempatan dengan Foundry Local dan Qwen.** Pelajaran baru [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) dan buku nota [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) membina pembantu kejuruteraan benar-benar di peranti (panggilan fungsi Qwen melalui Foundry Local, alat fail berpasir, RAG tempatan dengan Chroma, MCP tempatan pilihan), dengan rajah hanya tempatan / RAG tempatan / pemanggilan alat, semakan pengetahuan, tugasan, dan cabaran.
- **Talian uji asap.** Aliran kerja baru [Uji Asap AI](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) serta katalog per pelajaran di bawah [tests/](./tests/README.md) untuk ejen yang boleh disebarkan dalam Pelajaran 01, 04, 05, dan 16, dengan README indeks yang memetakan setiap katalog kepada pelajaran dan nama ejen yang dihos. Pelajaran 16 mendapat seksyen "Mengesahkan Ejen Disebarkan dengan Ujian Asap"; Pelajaran 01/04/05 mendapat petunjuk uji asap pilihan.
- **Kemahiran pelajar.** Kemahiran Ejen baru dalam `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (membungkus panduan Pelajaran 16 dan 17), dan [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (cara mengesahkan sampel buku nota terhadap Microsoft Foundry / Azure OpenAI yang hidup).
- **Pelari pengesahan buku nota.** [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) baru yang menjalankan setiap buku nota Python tanpa kepala dengan `nbconvert` dan mencetak matriks LULUS/GAGAL (serta `results.json`). Ia mengesan akar repo dan Python secara automatik, mengecualikan buku nota bukan kursus (`.venv`, `site-packages`, `translations`, aset templat kemahiran) dan buku nota `.NET` secara lalai, serta menyokong `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, dan `-Python`.
- **Navigasi kursus.** Menambah pautan Pelajaran Sebelumnya/Seterusnya ke Pelajaran 11–15 (yang sebelumnya tiada) supaya keseluruhan kursus berantai 00 → 18 dalam kedua-dua arah.
- **Thumbnail baru.** Thumbnail pelajaran bagi Pelajaran 16 dan 17, serta imej sosial repositori yang diperkemas [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (kini mengiklankan dua pelajaran baru dan URL `aka.ms/ai-agents-beginners`).
- **Kebergantungan** ([requirements.txt](../../requirements.txt)): menambah `foundry-local-sdk` dan `chromadb` untuk Pelajaran 17.

### Ditukar

- **Jadual pelajaran utama [README.md](./README.md)**: Pelajaran 16 dan 17 kini paut kepada kandungan mereka (sebelum ini "Akan Datang"); imej repositori dinaikkan ke `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: menambah Pelajaran 16 dan 17 kepada panduan satu-persatu pelajaran dan laluan pembelajaran, serta seksyen "Mengesahkan Ejen Disebarkan dengan Ujian Asap".
- **[AGENTS.md](./AGENTS.md)**: mengemas kini kiraan/penerangan pelajaran (00–18), menambah seksyen pengesahan ujian asap, dan menambah contoh penamaan sampel Pelajaran 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Pelajaran Sebelumnya" kini menunjuk ke Pelajaran 17 (dahulu Pelajaran 15), menutup rantaian.
- **Penyeragaman rujukan model pada model tidak usang.** Menggantikan semua rujukan `gpt-4o` / `gpt-4o-mini` dalam kursus (dokumen, `.env.example`, buku nota Python/.NET dan sampel) dengan `gpt-4.1-mini` — `gpt-4o` (semua versi) akan bersara pada 2026. Contoh penghalaan model Pelajaran 16 mengekalkan kontras kecil/besar menggunakan `gpt-4.1-mini` (kecil) dan `gpt-4.1` (besar). Buku nota Python kini memilih model daripada pembolehubah persekitaran (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) dan bukannya mengekod nama model secara keras.

### Nota dan had yang diketahui

- **Tidak dijalankan terhadap Azure yang hidup.** Buku nota pelajaran baru adalah sampel pendidikan; jalankan dan sahkan ia terhadap tetapan Microsoft Foundry / Foundry Local anda sendiri. Aliran kerja uji asap memerlukan anda menyebarkan ejen pelajaran dan mengkonfigurasi rahsia Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) dengan peranan **Azure AI User** pada skop projek Foundry.
- **Pelajaran 17 adalah hanya tempatan.** Ia tiada titik akhir Foundry Responses, jadi tindakan uji asap tidak terpakai; sahkan ia dengan menjalankan buku nota di stesen kerja anda.

## [Dilepaskan] — 2026-07-06

Siaran ini memindahkan kursus ke **API Respon Azure OpenAI**, menyeragamkan penamaan produk pada **Microsoft Foundry** dan **Microsoft Agent Framework (MAF)**, memberhentikan Model GitHub, mengemas kini versi SDK, dan menambah kandungan baru mengenai model tempatan dan kehosan bingkai lain di Foundry.

### Ditambah

- **Kemahiran migrasi** — Dipasang Kemahiran Ejen [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (dari [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) di bawah `.agents/skills/`, termasuk rujukan dan skrip pengimbasannya.
- **Foundry Local (menjalankan model di peranti)** — Seksyen baru "Pembekal Alternatif: Foundry Local" dalam [00-course-setup/README.md](./00-course-setup/README.md) merangkumi pemasangan (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, dan penyambungan `FoundryLocalManager` ke Microsoft Agent Framework melalui `OpenAIChatClient`.
- **Menghoskan ejen LangChain / LangGraph di Microsoft Foundry** — Seksyen baru dalam [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) serta sampel boleh dijalankan [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) menggunakan `langchain-azure-ai[hosting]` dan `ResponsesHostServer` (protokol `/responses`), berdasarkan [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Projek Microsoft Opal** — Seksyen baru "Contoh Dunia Sebenar: Projek Microsoft Opal" dalam [15-browser-use/README.md](./15-browser-use/README.md) menggambarkan Opal sebagai ejen penggunaan komputer perusahaan dan memetakannya kepada konsep kursus (manusia dalam gelung, kepercayaan/keselamatan, perancangan, Kemahiran).
- **Sampel Python Pelajaran 02 kedua** — Ditambah [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (lihat "Ditukar" — dipindahkan dari buku nota Semantic Kernel yang lama) dan pautkan dalam README pelajaran.
- **Seksyen Model dan Pembekal** ditambah kepada [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Ditukar

- **Completi Chat → Responses API (Python).** Sampel yang memanggil model secara langsung dipindahkan dari Completi Chat ke API Respon (`client.responses.create(input=..., store=False)`, `resp.output_text`), menggunakan klien `OpenAI` terhadap titik akhir Azure OpenAI `/openai/v1/` yang stabil (tanpa `api_version`). Sampel yang terjejas termasuk:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — walkthrough keseluruhan pemanggilan fungsi (skema alat diratakan ke format Responses, keputusan alat dikembalikan sebagai `function_call_output`, `max_output_tokens`, dan sebagainya).

- **Model GitHub → Azure OpenAI.** Model GitHub sudah tidak digunakan (berhenti **Julai 2026**) dan tidak menyokong API Respons. Semua laluan kod Model GitHub telah ditukar kepada Azure OpenAI / Microsoft Foundry merentas contoh Python dan .NET:
  - Python: buku nota aliran kerja Pelajaran 08 (`01`–`03`), Pelajaran 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + dokumen `.md` pendamping, dan buku nota/`.md` aliran kerja dotNET Pelajaran 08 (`01`–`03`) kini menggunakan `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` dengan `AzureCliCredential`.
- **Semantic Kernel → Rangka Kerja Ejen Microsoft.** `02-semantic-kernel.ipynb` yang dahulu ditulis semula untuk menggunakan Rangka Kerja Ejen Microsoft dengan Azure OpenAI (API Respons) dan dinamakan semula kepada `02-python-agent-framework-azure-openai.ipynb`.
- **Distandardkan kepada `FoundryChatClient` + `as_agent`.** Kod README dan buku nota yang merujuk `AzureAIProjectAgentProvider` didistandardkan kepada corak kanonik yang digunakan oleh Pelajaran 01 dan contoh rangka kerja sendiri: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` dengan `provider.as_agent(...)`. Dikemaskini merentas README dan buku nota Pelajaran 02–14 (contohnya, ingatan Pelajaran 13, semua buku nota Pelajaran 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Penamaan produk.** Ditukar nama sepanjang kandungan Bahasa Inggeris:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Perkhidmatan Ejen Microsoft Foundry**
  - (Tidak berubah: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", dan nama pembolehubah persekitaran.)
- **Kebergantungan** ([requirements.txt](../../requirements.txt)):
  - Dikunci `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Dikunci `openai>=1.108.1` (minimum untuk API Respons).
  - Dibuang `azure-ai-inference` (hanya digunakan oleh contoh Model GitHub yang dipindahkan).
- **Konfigurasi persekitaran** ([.env.example](../../.env.example)): membuang pembolehubah Model GitHub (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); menambah `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, dan pilihan `AZURE_OPENAI_API_KEY`; mengemas kini penamaan kepada Microsoft Foundry.
- **Dokumen** — Dikemaskini [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), dan [STUDY_GUIDE.md](./STUDY_GUIDE.md) untuk perkara di atas (penetapan pembolehubah persekitaran, serpihan pengesahan, panduan penyedia, penamaan).

### Dibuang

- Langkah pendaftaran Model GitHub dan pembolehubah persekitaran daripada dokumen persediaan (digantikan oleh Azure OpenAI / Microsoft Foundry).

### Keselamatan / Privasi (pembersihan perkongsian awam)

- Mengosongkan output pelaksanaan buku nota Jupyter yang mendedahkan **ID langganan Azure** sebenar, nama kumpulan sumber / sumber, dan ID sambungan Bing, serta laluan fail tempatan dan nama pengguna pembangun di:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Memastikan tiada kunci API, token, ID langganan atau laluan peribadi yang tinggal dalam kandungan Bahasa Inggeris yang dijejaki (rujukan `GITHUB_TOKEN` yang tinggal adalah token GitHub Actions dalam aliran kerja dan PAT pelayan GitHub MCP dalam persediaan Pelajaran 11 — kedua-duanya sah dan tidak berkaitan dengan Model GitHub).

### Nota dan had dikenali

- **Tidak dilaksanakan/disusun.** Ini adalah contoh pendidikan yang dikemaskini untuk ketepatan API/penamaan; ia tidak dijalankan ke atas sumber Azure secara langsung, dan contoh .NET tidak disusun dalam persekitaran ini. Sahkan dengan pelaksanaan Microsoft Foundry / Azure OpenAI anda sendiri.
- **Perkembangan model mesti menyokong API Respons.** Gunakan penyebaran seperti `gpt-4.1-mini`, `gpt-4.1`, atau model `gpt-5.x`. Model lama menyokong fungsi asas Respons tetapi tidak semua ciri.
- **Versi rangka kerja ejen.** Contoh menyasarkan MAF terkini (`>=1.10.0`). Panggilan penciptaan ejen kanonik ialah `client.as_agent(...)`; API disahkan mengikut dokumen yang diterbitkan rangka kerja dan binaan terpasang. Jika anda mengunci versi berbeza, sahkan ketersediaan kaedah (`as_agent` berbanding `create_agent`).
- **Buku nota aliran kerja Pelajaran 08 04** sengaja mengekalkan `AzureAIAgentClient` (daripada `agent-framework-azure-ai`) kerana ia menggunakan alat hos Perkhidmatan Ejen Microsoft Foundry (pembumian Bing, penafsir kod); ia telah berasaskan Respons.
- **Penyebaran lalai .NET.** Dua contoh aliran kerja dotNET Pelajaran 08 sebelum ini dikod keras model tertentu; kini lalai kepada `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Jika contoh menggunakan input multimodal/visi, tetapkan `AZURE_OPENAI_DEPLOYMENT` kepada model yang sesuai.
- **Foundry Tempatan** memperlihatkan titik akhir **Chat Completions** serasi OpenAI dan bertujuan untuk pembangunan tempatan; gunakan Azure OpenAI / Microsoft Foundry untuk set ciri API Respons penuh.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->