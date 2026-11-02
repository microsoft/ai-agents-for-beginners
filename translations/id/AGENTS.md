# AGENTS.md

## Gambaran Proyek

Repositori ini berisi "AI Agents untuk Pemula" - sebuah kursus edukasi komprehensif yang mengajarkan segala yang diperlukan untuk membangun AI Agents. Kursus ini terdiri dari 18 pelajaran (diberi nomor 00-18) yang mencakup dasar-dasar, pola desain, kerangka kerja, penerapan produksi, agen lokal/di perangkat, dan keamanan agen AI.

**Teknologi Kunci:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- Kerangka AI: Microsoft Agent Framework (MAF)
- Layanan AI Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arsitektur:**
- Struktur berbasis pelajaran (direktori 00-18)
- Setiap pelajaran berisi: dokumentasi README, contoh kode (notebook Jupyter), dan gambar
- Dukungan multibahasa melalui sistem terjemahan otomatis
- Satu notebook Python per pelajaran menggunakan Microsoft Agent Framework

## Perintah Setup

### Prasyarat
- Python 3.12 atau lebih tinggi
- Langganan Azure (untuk Microsoft Foundry)
- Azure CLI terinstal dan terautentikasi (`az login`)

### Setup Awal

1. **Clone atau fork repositori:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Buat dan aktifkan lingkungan virtual Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Pasang dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Siapkan variabel lingkungan:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Variabel Lingkungan yang Diperlukan

Untuk **Microsoft Foundry** (Diperlukan):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint proyek Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Nama deployment model (misalnya, gpt-5-mini)

Untuk **Azure AI Search** (Pelajaran 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - Kunci API Azure AI Search

Autentikasi: Jalankan `az login` sebelum menjalankan notebook (menggunakan `AzureCliCredential`).

## Alur Kerja Pengembangan

### Menjalankan Jupyter Notebooks

Setiap pelajaran berisi beberapa notebook Jupyter untuk kerangka kerja yang berbeda:

1. **Mulai Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Arahkan ke direktori pelajaran** (misalnya, `01-intro-to-ai-agents/code_samples/`)

3. **Buka dan jalankan notebooks:**
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)

### Bekerja dengan Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Memerlukan langganan Azure
- Menggunakan `FoundryChatClient` untuk Agent Service V2 (agen terlihat di portal Foundry)
- Siap produksi dengan observabilitas bawaan
- Pola berkas: `*-python-agent-framework.ipynb`

## Instruksi Pengujian

Ini adalah repositori edukasi dengan contoh kode daripada kode produksi dengan tes otomatis. Untuk memverifikasi setup dan perubahan Anda:

### Pengujian Manual

1. **Uji lingkungan Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Uji eksekusi notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifikasi variabel lingkungan:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Menjalankan Notebook Individu

Buka notebook di Jupyter dan eksekusi cell secara berurutan. Setiap notebook berdiri sendiri dan meliputi:
- Pernyataan import
- Pemanggilan konfigurasi
- Implementasi contoh agen
- Output yang diharapkan di cell markdown

### Smoke-Test Agen yang Telah Dideploy

Untuk pelajaran dimana agen dideploy sebagai agen host Microsoft Foundry (01, 04, 05, 16), repositori menyediakan katalog smoke-test di `tests/` yang dijalankan oleh workflow `.github/workflows/smoke-test.yml` melalui aksi [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Ini adalah pemeriksaan pintu ringan pasca-deploy (apakah agen dapat dijangkau dan mengikuti ekspektasi prompt dasar?), melengkapi pipeline evaluasi di Pelajaran 10 dan 16. Lihat [tests/README.md](./tests/README.md) untuk pemetaan katalog-ke-pelajaran-ke-agen. Pelajaran 17 berjalan secara lokal dengan Foundry Local dan tidak memiliki endpoint yang dihosting, jadi divalidasi dengan menjalankan notebooknya langsung.

## Gaya Kode

### Konvensi Python

- **Versi Python**: 3.12+
- **Gaya Kode**: Ikuti konvensi Python PEP 8 standar
- **Notebook**: Gunakan cell markdown yang jelas untuk menjelaskan konsep
- **Imports**: Kelompokkan berdasarkan pustaka standar, pihak ketiga, import lokal

### Konvensi Jupyter Notebook

- Sertakan cell markdown deskriptif sebelum cell kode
- Tambahkan contoh output di notebook sebagai referensi
- Gunakan nama variabel yang jelas sesuai dengan konsep pelajaran
- Jaga urutan eksekusi notebook linear (cell 1 → 2 → 3...)

### Organisasi Berkas

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Build dan Deployment

### Membangun Dokumentasi

Repositori ini menggunakan Markdown untuk dokumentasi:
- Berkas README.md di setiap folder pelajaran
- README.md utama di root repositori
- Sistem terjemahan otomatis melalui GitHub Actions

### Pipeline CI/CD

Terletak di `.github/workflows/`:

1. **co-op-translator.yml** - Terjemahan otomatis ke 50+ bahasa
2. **welcome-issue.yml** - Menyambut pembuat issue baru
3. **welcome-pr.yml** - Menyambut kontributor pull request baru

### Deployment

Ini adalah repositori edukasi - tidak ada proses deployment. Pengguna:
1. Fork atau clone repositori
2. Jalankan notebook secara lokal atau di GitHub Codespaces
3. Belajar dengan memodifikasi dan bereksperimen dengan contoh

## Panduan Pull Request

### Sebelum Mengirim

1. **Uji perubahan Anda:**
   - Jalankan notebook yang terkena dampak sepenuhnya
   - Pastikan semua cell berjalan tanpa error
   - Periksa output apakah sesuai

2. **Pembaruan dokumentasi:**
   - Update README.md jika menambah konsep baru
   - Tambah komentar di notebook untuk kode kompleks
   - Pastikan cell markdown menjelaskan tujuan

3. **Perubahan berkas:**
   - Hindari commit berkas `.env` (gunakan `.env.example`)
   - Jangan commit direktori `venv/` atau `__pycache__/`
   - Jaga output notebook jika menunjukkan konsep
   - Hapus berkas sementara dan backup notebook (`*-backup.ipynb`)

### Format Judul PR

Gunakan judul deskriptif:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Pemeriksaan Wajib

- Notebook harus dijalankan tanpa error
- Berkas README harus jelas dan akurat
- Ikuti pola kode yang ada di repositori
- Pertahankan konsistensi dengan pelajaran lain

## Catatan Tambahan

### Hal Umum yang Perlu Diperhatikan

1. **Perbedaan versi Python:**
   - Pastikan menggunakan Python 3.12+
   - Beberapa paket mungkin tidak bekerja dengan versi lama
   - Gunakan `python3 -m venv` untuk spesifikasikan versi Python secara eksplisit

2. **Variabel lingkungan:**
   - Selalu buat `.env` dari `.env.example`
   - Jangan commit berkas `.env` (termasuk di `.gitignore`)
   - Masuk dengan `az login` untuk autentikasi Entra ID tanpa kunci

3. **Konflik paket:**
   - Gunakan lingkungan virtual baru
   - Pasang dari `requirements.txt` bukan dari paket individual
   - Beberapa notebook mungkin memerlukan paket tambahan seperti yang disebutkan di cell markdown mereka

4. **Layanan Azure:**
   - Layanan AI Azure memerlukan langganan aktif
   - Beberapa fitur spesifik wilayah
   - Pastikan deployment model Azure OpenAI Anda mendukung Responses API

### Jalur Pembelajaran

Progresi yang direkomendasikan melalui pelajaran:
1. **00-course-setup** - Mulai di sini untuk setup lingkungan
2. **01-intro-to-ai-agents** - Pahami dasar agen AI
3. **02-explore-agentic-frameworks** - Pelajari berbagai kerangka kerja
4. **03-agentic-design-patterns** - Pola desain inti
5. Lanjutkan melalui pelajaran berurut sesuai nomor

### Pemilihan Kerangka Kerja

Pilih kerangka kerja sesuai tujuan Anda:
- **Semua pelajaran**: Microsoft Agent Framework (MAF) dengan `FoundryChatClient`
- **Agen mendaftar sisi server** di Microsoft Foundry Agent Service V2 dan terlihat di portal Foundry

### Mendapatkan Bantuan

- Bergabung dengan [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Review berkas README pelajaran untuk panduan spesifik
- Cek [README.md](./README.md) utama untuk gambaran kursus
- Rujuk [Course Setup](./00-course-setup/README.md) untuk instruksi setup terperinci

### Kontribusi

Ini adalah proyek edukasi terbuka. Kontribusi dipersilakan:
- Tingkatkan contoh kode
- Perbaiki typo atau error
- Tambah komentar penjelas
- Sarankan topik pelajaran baru
- Terjemahkan ke bahasa tambahan

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk kebutuhan terkini.

## Konteks Spesifik Proyek

### Dukungan Multibahasa

Repositori ini menggunakan sistem terjemahan otomatis:
- Mendukung 50+ bahasa
- Terjemahan dalam direktori `/translations/<lang-code>/`
- Workflow GitHub Actions menangani pembaruan terjemahan
- Berkas sumber berbahasa Inggris di root repositori

### Struktur Pelajaran

Setiap pelajaran mengikuti pola konsisten:
1. Thumbnail video dengan tautan
2. Konten pelajaran tertulis (README.md)
3. Contoh kode dalam berbagai kerangka kerja
4. Tujuan pembelajaran dan prasyarat
5. Sumber belajar tambahan yang ditautkan

### Penamaan Contoh Kode

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Pelajaran 1, MAF Python
- `14-sequential.ipynb` - Pelajaran 14, pola lanjutan MAF
- `16-python-agent-framework.ipynb` - Pelajaran 16, agen dukungan pelanggan produksi
- `17-local-agent-foundry-local.ipynb` - Pelajaran 17, agen lokal dengan Foundry Local + Qwen

### Direktori Khusus

- `translated_images/` - Gambar yang dilokalkan untuk terjemahan
- `images/` - Gambar asli untuk konten bahasa Inggris
- `.devcontainer/` - Konfigurasi container pengembangan VS Code
- `.github/` - Workflow dan template GitHub Actions

### Dependensi

Paket kunci dari `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Dukungan protokol Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Layanan AI Azure
- `azure-identity` - Autentikasi Azure (AzureCliCredential)
- `azure-search-documents` - Integrasi Azure AI Search
- `mcp[cli]` - Dukungan Protokol Konteks Model

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->