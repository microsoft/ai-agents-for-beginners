# AGENTS.md

## Gambaran Proyek

Repositori ini berisi "AI Agents for Beginners" - sebuah kursus edukasi yang komprehensif untuk mempelajari segala hal yang diperlukan untuk membangun AI Agents. Kursus ini terdiri dari lebih dari 15 pelajaran yang mencakup dasar-dasar, pola desain, kerangka kerja, dan penerapan AI agents ke dalam produksi.

**Teknologi Utama:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- Kerangka AI: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Layanan Azure AI: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (tersedia versi gratis)

**Arsitektur:**
- Struktur berbasis pelajaran (direktori 00-15+)
- Setiap pelajaran berisi: dokumentasi README, contoh kode (Jupyter notebooks), dan gambar
- Dukungan multi-bahasa melalui sistem terjemahan otomatis
- Pilihan kerangka kerja yang beragam untuk setiap pelajaran (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Perintah Pengaturan

### Prasyarat
- Python 3.12 atau lebih tinggi
- Akun GitHub (untuk GitHub Models - versi gratis)
- Langganan Azure (opsional, untuk layanan Azure AI)

### Pengaturan Awal

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

3. **Instal dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Atur variabel lingkungan:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Variabel Lingkungan yang Diperlukan

Untuk **GitHub Models (Gratis)**:
- `GITHUB_TOKEN` - Token akses pribadi dari GitHub

Untuk **Layanan Azure AI** (opsional):
- `PROJECT_ENDPOINT` - Endpoint proyek Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Kunci API Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Nama deployment untuk model chat
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Nama deployment untuk embeddings
- Konfigurasi Azure tambahan seperti yang ditunjukkan dalam `.env.example`

## Alur Kerja Pengembangan

### Menjalankan Jupyter Notebooks

Setiap pelajaran berisi beberapa Jupyter notebooks untuk kerangka kerja yang berbeda:

1. **Mulai Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigasi ke direktori pelajaran** (misalnya, `01-intro-to-ai-agents/code_samples/`)

3. **Buka dan jalankan notebooks:**
   - `*-semantic-kernel.ipynb` - Menggunakan kerangka kerja Semantic Kernel
   - `*-autogen.ipynb` - Menggunakan kerangka kerja AutoGen
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Menggunakan Azure AI Agent Service

### Bekerja dengan Kerangka Kerja yang Berbeda

**Semantic Kernel + GitHub Models:**
- Tersedia versi gratis dengan akun GitHub
- Cocok untuk pembelajaran dan eksperimen
- Pola file: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Tersedia versi gratis dengan akun GitHub
- Kemampuan orkestrasi multi-agent
- Pola file: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Kerangka kerja terbaru dari Microsoft
- Tersedia dalam Python dan .NET
- Pola file: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Membutuhkan langganan Azure
- Fitur siap produksi
- Pola file: `*-azureaiagent.ipynb`

## Instruksi Pengujian

Repositori ini adalah repositori edukasi dengan contoh kode, bukan kode produksi dengan pengujian otomatis. Untuk memverifikasi pengaturan dan perubahan Anda:

### Pengujian Manual

1. **Uji lingkungan Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Uji eksekusi notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifikasi variabel lingkungan:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Menjalankan Notebook Secara Individual

Buka notebook di Jupyter dan eksekusi sel secara berurutan. Setiap notebook bersifat mandiri dan mencakup:
- Pernyataan impor
- Pemuatan konfigurasi
- Implementasi agen contoh
- Output yang diharapkan dalam sel markdown

## Gaya Kode

### Konvensi Python

- **Versi Python**: 3.12+
- **Gaya Kode**: Ikuti konvensi standar Python PEP 8
- **Notebooks**: Gunakan sel markdown yang jelas untuk menjelaskan konsep
- **Impor**: Kelompokkan berdasarkan pustaka standar, pihak ketiga, dan impor lokal

### Konvensi Jupyter Notebook

- Sertakan sel markdown deskriptif sebelum sel kode
- Tambahkan contoh output dalam notebook untuk referensi
- Gunakan nama variabel yang jelas sesuai dengan konsep pelajaran
- Pertahankan urutan eksekusi notebook secara linear (sel 1 → 2 → 3...)

### Organisasi File

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## Pembuatan dan Penerapan

### Pembuatan Dokumentasi

Repositori ini menggunakan Markdown untuk dokumentasi:
- File README.md di setiap folder pelajaran
- README.md utama di root repositori
- Sistem terjemahan otomatis melalui GitHub Actions

### Pipeline CI/CD

Terletak di `.github/workflows/`:

1. **co-op-translator.yml** - Terjemahan otomatis ke lebih dari 50 bahasa
2. **welcome-issue.yml** - Menyambut pembuat issue baru
3. **welcome-pr.yml** - Menyambut kontributor pull request baru

### Penerapan

Repositori ini bersifat edukasi - tidak ada proses penerapan. Pengguna:
1. Fork atau clone repositori
2. Jalankan notebook secara lokal atau di GitHub Codespaces
3. Belajar dengan memodifikasi dan bereksperimen dengan contoh

## Panduan Pull Request

### Sebelum Mengirimkan

1. **Uji perubahan Anda:**
   - Jalankan notebook yang terpengaruh sepenuhnya
   - Verifikasi semua sel berjalan tanpa error
   - Periksa bahwa output sesuai

2. **Pembaruan dokumentasi:**
   - Perbarui README.md jika menambahkan konsep baru
   - Tambahkan komentar dalam notebook untuk kode yang kompleks
   - Pastikan sel markdown menjelaskan tujuan

3. **Perubahan file:**
   - Hindari meng-commit file `.env` (gunakan `.env.example`)
   - Jangan commit direktori `venv/` atau `__pycache__/`
   - Pertahankan output notebook jika menunjukkan konsep
   - Hapus file sementara dan backup notebook (`*-backup.ipynb`)

### Format Judul PR

Gunakan judul yang deskriptif:
- `[Lesson-XX] Tambahkan contoh baru untuk <konsep>`
- `[Fix] Perbaiki typo di README pelajaran-XX`
- `[Update] Tingkatkan contoh kode di pelajaran-XX`
- `[Docs] Perbarui instruksi pengaturan`

### Pemeriksaan yang Diperlukan

- Notebook harus berjalan tanpa error
- File README harus jelas dan akurat
- Ikuti pola kode yang ada di repositori
- Pertahankan konsistensi dengan pelajaran lainnya

## Catatan Tambahan

### Hal-Hal yang Sering Terjadi

1. **Ketidaksesuaian versi Python:**
   - Pastikan menggunakan Python 3.12+
   - Beberapa paket mungkin tidak berfungsi dengan versi lama
   - Gunakan `python3 -m venv` untuk menentukan versi Python secara eksplisit

2. **Variabel lingkungan:**
   - Selalu buat `.env` dari `.env.example`
   - Jangan commit file `.env` (sudah ada di `.gitignore`)
   - Token GitHub membutuhkan izin yang sesuai

3. **Konflik paket:**
   - Gunakan lingkungan virtual yang baru
   - Instal dari `requirements.txt` daripada paket individual
   - Beberapa notebook mungkin membutuhkan paket tambahan yang disebutkan dalam sel markdown mereka

4. **Layanan Azure:**
   - Layanan Azure AI membutuhkan langganan aktif
   - Beberapa fitur bersifat spesifik wilayah
   - Batasan versi gratis berlaku untuk GitHub Models

### Jalur Pembelajaran

Urutan yang direkomendasikan untuk pelajaran:
1. **00-course-setup** - Mulai di sini untuk pengaturan lingkungan
2. **01-intro-to-ai-agents** - Memahami dasar-dasar AI agent
3. **02-explore-agentic-frameworks** - Pelajari berbagai kerangka kerja
4. **03-agentic-design-patterns** - Pola desain inti
5. Lanjutkan melalui pelajaran bernomor secara berurutan

### Pemilihan Kerangka Kerja

Pilih kerangka kerja berdasarkan tujuan Anda:
- **Pembelajaran/Prototipe**: Semantic Kernel + GitHub Models (gratis)
- **Sistem multi-agent**: AutoGen
- **Fitur terbaru**: Microsoft Agent Framework (MAF)
- **Penerapan produksi**: Azure AI Agent Service

### Mendapatkan Bantuan

- Bergabunglah dengan [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Tinjau file README pelajaran untuk panduan spesifik
- Periksa [README.md utama](./README.md) untuk gambaran kursus
- Lihat [Course Setup](./00-course-setup/README.md) untuk instruksi pengaturan yang lebih rinci

### Kontribusi

Ini adalah proyek edukasi terbuka. Kontribusi sangat diterima:
- Tingkatkan contoh kode
- Perbaiki typo atau kesalahan
- Tambahkan komentar yang memperjelas
- Usulkan topik pelajaran baru
- Terjemahkan ke bahasa tambahan

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk kebutuhan saat ini.

## Konteks Spesifik Proyek

### Dukungan Multi-Bahasa

Repositori ini menggunakan sistem terjemahan otomatis:
- Mendukung lebih dari 50 bahasa
- Terjemahan berada di direktori `/translations/<lang-code>/`
- Workflow GitHub Actions menangani pembaruan terjemahan
- File sumber berada dalam bahasa Inggris di root repositori

### Struktur Pelajaran

Setiap pelajaran mengikuti pola yang konsisten:
1. Thumbnail video dengan tautan
2. Konten pelajaran tertulis (README.md)
3. Contoh kode dalam berbagai kerangka kerja
4. Tujuan pembelajaran dan prasyarat
5. Sumber daya pembelajaran tambahan yang ditautkan

### Penamaan Contoh Kode

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Pelajaran 4, Semantic Kernel
- `07-autogen.ipynb` - Pelajaran 7, AutoGen
- `14-python-agent-framework.ipynb` - Pelajaran 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Pelajaran 14, MAF .NET

### Direktori Khusus

- `translated_images/` - Gambar yang dilokalkan untuk terjemahan
- `images/` - Gambar asli untuk konten bahasa Inggris
- `.devcontainer/` - Konfigurasi container pengembangan VS Code
- `.github/` - Workflow dan template GitHub Actions

### Dependensi

Paket utama dari `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Kerangka kerja AutoGen
- `semantic-kernel` - Kerangka kerja Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Layanan Azure AI
- `azure-search-documents` - Integrasi Pencarian Azure AI
- `chromadb` - Basis data vektor untuk contoh RAG
- `chainlit` - Kerangka kerja UI chat
- `browser_use` - Otomasi browser untuk agen
- `mcp[cli]` - Dukungan Model Context Protocol
- `mem0ai` - Manajemen memori untuk agen

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.