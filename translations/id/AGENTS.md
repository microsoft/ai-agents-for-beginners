# AGENTS.md

## Gambaran Proyek

Repositori ini berisi "AI Agents untuk Pemula" - kursus edukasi komprehensif yang mengajarkan semua yang dibutuhkan untuk membangun AI Agents. Kursus ini terdiri dari 15+ pelajaran yang mencakup dasar-dasar, pola desain, kerangka kerja, dan penerapan produksi agen AI.

**Teknologi Utama:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- Kerangka Kerja AI: Microsoft Agent Framework (MAF)
- Layanan AI Azure: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arsitektur:**
- Struktur berbasis pelajaran (direktori 00-15+)
- Setiap pelajaran berisi: dokumentasi README, contoh kode (Jupyter notebooks), dan gambar
- Dukungan multi-bahasa melalui sistem terjemahan otomatis
- Satu notebook Python per pelajaran menggunakan Microsoft Agent Framework

## Perintah Setup

### Prasyarat
- Python 3.12 atau lebih tinggi
- Langganan Azure (untuk Azure AI Foundry)
- Azure CLI terpasang dan terautentikasi (`az login`)

### Setup Awal

1. **Clone atau fork repositori:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ATAU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Buat dan aktifkan lingkungan virtual Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Pada Windows: venv\Scripts\activate
   ```

3. **Instal dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Atur variabel lingkungan:**
   ```bash
   cp .env.example .env
   # Edit .env dengan kunci API dan endpoint Anda
   ```

### Variabel Lingkungan yang Dibutuhkan

Untuk **Azure AI Foundry** (Wajib):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint proyek Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nama deployment model (misal: gpt-4o)

Untuk **Azure AI Search** (Pelajaran 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - kunci API Azure AI Search

Autentikasi: Jalankan `az login` sebelum menjalankan notebook (menggunakan `AzureCliCredential`).

## Alur Kerja Pengembangan

### Menjalankan Jupyter Notebooks

Setiap pelajaran berisi beberapa notebook Jupyter untuk berbagai kerangka kerja:

1. **Mulai Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigasi ke direktori pelajaran** (contoh: `01-intro-to-ai-agents/code_samples/`)

3. **Buka dan jalankan notebook:**
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)

### Bekerja dengan Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Memerlukan langganan Azure
- Menggunakan `AzureAIProjectAgentProvider` untuk Agent Service V2 (agen terlihat di portal Foundry)
- Siap produksi dengan observabilitas bawaan
- Pola file: `*-python-agent-framework.ipynb`

## Instruksi Pengujian

Ini adalah repositori edukasi dengan contoh kode, bukan kode produksi dengan tes otomatis. Untuk memverifikasi setup dan perubahan Anda:

### Pengujian Manual

1. **Uji lingkungan Python:**
   ```bash
   python --version  # Harus 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Uji eksekusi notebook:**
   ```bash
   # Mengonversi notebook ke skrip dan menjalankan (mengimpor tes)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifikasi variabel lingkungan:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Menjalankan Notebook Individu

Buka notebook di Jupyter dan jalankan sel secara berurutan. Setiap notebook mandiri dan mencakup:
- Pernyataan impor
- Memuat konfigurasi
- Implementasi agen contoh
- Output yang diharapkan dalam sel markdown

## Gaya Kode

### Konvensi Python

- **Versi Python**: 3.12+
- **Gaya Kode**: Ikuti konvensi PEP 8 standar Python
- **Notebook**: Gunakan sel markdown yang jelas untuk menjelaskan konsep
- **Impor**: Kelompokkan berdasarkan pustaka standar, pihak ketiga, dan lokal

### Konvensi Jupyter Notebook

- Sertakan sel markdown deskriptif sebelum sel kode
- Tambahkan contoh output di notebook sebagai referensi
- Gunakan nama variabel yang jelas sesuai konsep pelajaran
- Pertahankan urutan eksekusi notebook secara linear (sel 1 → 2 → 3...)

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

### Pipelines CI/CD

Terletak di `.github/workflows/`:

1. **co-op-translator.yml** - Penerjemahan otomatis ke 50+ bahasa
2. **welcome-issue.yml** - Menyambut pembuat isu baru
3. **welcome-pr.yml** - Menyambut kontributor permintaan tarik baru

### Deployment

Ini adalah repositori edukasi - tidak ada proses deployment. Pengguna:
1. Fork atau clone repositori
2. Jalankan notebook secara lokal atau di GitHub Codespaces
3. Belajar dengan memodifikasi dan bereksperimen dengan contoh

## Panduan Pull Request

### Sebelum Mengirimkan

1. **Uji perubahan Anda:**
   - Jalankan notebook yang terdampak secara keseluruhan
   - Pastikan semua sel berjalan tanpa error
   - Periksa output agar sesuai

2. **Perbarui dokumentasi:**
   - Perbarui README.md jika menambah konsep baru
   - Tambahkan komentar di notebook untuk kode rumit
   - Pastikan sel markdown menjelaskan tujuan

3. **Perubahan file:**
   - Hindari meng-commit file `.env` (gunakan `.env.example`)
   - Jangan commit direktori `venv/` atau `__pycache__/`
   - Pertahankan output notebook jika menunjukkan konsep
   - Hapus file sementara dan backup notebook (`*-backup.ipynb`)

### Format Judul PR

Gunakan judul deskriptif:
- `[Lesson-XX] Tambah contoh baru untuk <konsep>`
- `[Fix] Perbaiki salah ketik di lesson-XX README`
- `[Update] Tingkatkan contoh kode di lesson-XX`
- `[Docs] Perbarui instruksi setup`

### Pemeriksaan Wajib

- Notebook harus bisa dijalankan tanpa error
- Berkas README harus jelas dan akurat
- Ikuti pola kode yang sudah ada di repositori
- Pertahankan konsistensi dengan pelajaran lain

## Catatan Tambahan

### Kesalahan Umum

1. **Versi Python tidak cocok:**
   - Pastikan menggunakan Python 3.12+
   - Beberapa paket tidak kompatibel dengan versi lama
   - Gunakan `python3 -m venv` untuk menentukan versi Python secara eksplisit

2. **Variabel lingkungan:**
   - Selalu buat `.env` dari `.env.example`
   - Jangan commit file `.env` (terdaftar di `.gitignore`)
   - Token GitHub memerlukan izin yang sesuai

3. **Konflik Paket:**
   - Gunakan lingkungan virtual baru
   - Instal dari `requirements.txt` daripada paket tunggal
   - Beberapa notebook mungkin membutuhkan paket tambahan yang disebutkan di sel markdown mereka

4. **Layanan Azure:**
   - Layanan AI Azure memerlukan langganan aktif
   - Beberapa fitur kawasan-spesifik
   - Batasan tier gratis berlaku untuk Model GitHub

### Jalur Pembelajaran

Rekomendasi progresi pelajaran:
1. **00-course-setup** - Mulai di sini untuk setup lingkungan
2. **01-intro-to-ai-agents** - Pahami dasar agen AI
3. **02-explore-agentic-frameworks** - Pelajari berbagai kerangka kerja
4. **03-agentic-design-patterns** - Pola desain inti
5. Lanjutkan ke pelajaran bernomor secara berurutan

### Pilihan Kerangka Kerja

Pilih kerangka berdasarkan tujuan Anda:
- **Semua pelajaran**: Microsoft Agent Framework (MAF) dengan `AzureAIProjectAgentProvider`
- **Agen mendaftar di sisi server** di Azure AI Foundry Agent Service V2 dan terlihat di portal Foundry

### Mendapatkan Bantuan

- Bergabung dengan [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Tinjau berkas README pelajaran untuk panduan spesifik
- Periksa [README.md](./README.md) utama untuk gambaran kursus
- Rujuk ke [Course Setup](./00-course-setup/README.md) untuk instruksi setup terperinci

### Kontribusi

Ini adalah proyek edukasi terbuka. Kontribusi disambut:
- Perbaiki contoh kode
- Perbaiki salah ketik atau error
- Tambahkan komentar penjelas
- Sarankan topik pelajaran baru
- Terjemahkan ke bahasa lain

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk kebutuhan terkini.

## Konteks Spesifik Proyek

### Dukungan Multi-Bahasa

Repositori ini menggunakan sistem terjemahan otomatis:
- Mendukung 50+ bahasa
- Terjemahan di direktori `/translations/<kode-bahasa>/`
- Workflow GitHub Actions mengelola pembaruan terjemahan
- Berkas sumber dalam bahasa Inggris di root repositori

### Struktur Pelajaran

Setiap pelajaran mengikuti pola konsisten:
1. Thumbnail video dengan tautan
2. Konten pelajaran tertulis (README.md)
3. Contoh kode dalam beberapa kerangka kerja
4. Tujuan pembelajaran dan prasyarat
5. Sumber belajar tambahan yang ditautkan

### Penamaan Contoh Kode

Format: `<nomor-pelajaran>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Pelajaran 1, MAF Python
- `14-sequential.ipynb` - Pelajaran 14, pola lanjutan MAF

### Direktori Khusus

- `translated_images/` - Gambar lokal untuk terjemahan
- `images/` - Gambar asli untuk konten bahasa Inggris
- `.devcontainer/` - Konfigurasi container pengembangan VS Code
- `.github/` - Workflow dan template GitHub Actions

### Dependensi

Paket utama dari `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Dukungan protokol Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Layanan AI Azure
- `azure-identity` - Autentikasi Azure (AzureCliCredential)
- `azure-search-documents` - Integrasi Azure AI Search
- `mcp[cli]` - Dukungan Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk menjaga ketepatan, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->