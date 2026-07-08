# AGENTS.md

## Gambaran Proyek

Repositori ini berisi "AI Agents untuk Pemula" - sebuah kursus edukasi komprehensif yang mengajarkan segala hal yang diperlukan untuk membangun AI Agents. Kursus ini terdiri dari 18 pelajaran yang mencakup dasar-dasar, pola desain, kerangka kerja, dan penerapan produksi agen AI.

**Teknologi Utama:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- Kerangka AI: Microsoft Agent Framework (MAF)
- Layanan Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arsitektur:**
- Struktur berbasis pelajaran (direktori 00-15+)
- Setiap pelajaran berisi: dokumentasi README, contoh kode (notebook Jupyter), dan gambar
- Dukungan multi-bahasa melalui sistem terjemahan otomatis
- Satu notebook Python per pelajaran menggunakan Microsoft Agent Framework

## Perintah Setup

### Prasyarat
- Python 3.12 atau lebih baru
- Langganan Azure (untuk Microsoft Foundry)
- Azure CLI terpasang dan terotentikasi (`az login`)

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
   source venv/bin/activate  # Di Windows: venv\Scripts\activate
   ```

3. **Pasang dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Atur variabel lingkungan:**
   ```bash
   cp .env.example .env
   # Edit .env dengan kunci API dan endpoint Anda
   ```

### Variabel Lingkungan yang Diperlukan

Untuk **Microsoft Foundry** (Diperlukan):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint proyek Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Nama penyebaran model (misal, gpt-4o)

Untuk **Azure AI Search** (Pelajaran 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - Kunci API Azure AI Search

Autentikasi: Jalankan `az login` sebelum menjalankan notebook (menggunakan `AzureCliCredential`).

## Alur Kerja Pengembangan

### Menjalankan Jupyter Notebooks

Setiap pelajaran berisi beberapa notebook Jupyter untuk berbagai kerangka kerja:

1. **Mulai Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigasi ke direktori pelajaran** (misal, `01-intro-to-ai-agents/code_samples/`)

3. **Buka dan jalankan notebook:**
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)

### Bekerja dengan Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Memerlukan langganan Azure
- Menggunakan `FoundryChatClient` untuk Agent Service V2 (agen terlihat di portal Foundry)
- Siap produksi dengan observabilitas bawaan
- Pola file: `*-python-agent-framework.ipynb`

## Instruksi Pengujian

Ini adalah repositori edukasi dengan kode contoh bukan kode produksi dengan tes otomatis. Untuk memverifikasi setup dan perubahan Anda:

### Pengujian Manual

1. **Uji lingkungan Python:**
   ```bash
   python --version  # Harus 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Uji eksekusi notebook:**
   ```bash
   # Mengonversi notebook menjadi skrip dan menjalankan (menguji impor)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifikasi variabel lingkungan:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Menjalankan Notebook Individu

Buka notebook di Jupyter dan jalankan sel secara berurutan. Setiap notebook berdiri sendiri dan meliputi:
- Pernyataan import
- Pemanggilan konfigurasi
- Implementasi contoh agen
- Output yang diharapkan di sel markdown

## Gaya Kode

### Konvensi Python

- **Versi Python**: 3.12+
- **Gaya Kode**: Ikuti konvensi Python PEP 8 standar
- **Notebook**: Gunakan sel markdown yang jelas untuk menjelaskan konsep
- **Import**: Kelompokkan berdasarkan library standar, pihak ketiga, lokal

### Konvensi Jupyter Notebook

- Sertakan sel markdown deskriptif sebelum sel kode
- Tambahkan contoh output di notebook sebagai referensi
- Gunakan nama variabel yang jelas dan sesuai konsep pelajaran
- Pertahankan urutan eksekusi notebook linear (sel 1 → 2 → 3...)

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
- Sistem terjemahan otomatis via GitHub Actions

### Pipeline CI/CD

Berada di `.github/workflows/`:

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
   - Jalankan notebook yang terpengaruh sepenuhnya
   - Verifikasi semua sel berjalan tanpa error
   - Periksa output sudah sesuai

2. **Perbarui dokumentasi:**
   - Perbarui README.md jika menambah konsep baru
   - Tambah komentar di notebook untuk kode kompleks
   - Pastikan sel markdown menjelaskan tujuan

3. **Perubahan berkas:**
   - Hindari commit berkas `.env` (gunakan `.env.example`)
   - Jangan commit direktori `venv/` atau `__pycache__/`
   - Pertahankan output notebook ketika menjelaskan konsep
   - Hapus berkas sementara dan backup notebook (`*-backup.ipynb`)

### Format Judul PR

Gunakan judul deskriptif:
- `[Lesson-XX] Tambah contoh baru untuk <concept>`
- `[Fix] Koreksi typo di README lesson-XX`
- `[Update] Perbaiki contoh kode di lesson-XX`
- `[Docs] Perbarui instruksi setup`

### Pemeriksaan yang Diperlukan

- Notebook harus berjalan tanpa error
- File README harus jelas dan akurat
- Ikuti pola kode yang sudah ada di repositori
- Pertahankan konsistensi dengan pelajaran lain

## Catatan Tambahan

### Kesalahan Umum

1. **Versi Python tidak cocok:**
   - Pastikan menggunakan Python 3.12+
   - Beberapa paket mungkin tidak berfungsi dengan versi lama
   - Gunakan `python3 -m venv` untuk menentukan versi Python secara eksplisit

2. **Variabel lingkungan:**
   - Selalu buat `.env` dari `.env.example`
   - Jangan commit berkas `.env` (termasuk dalam `.gitignore`)
   - Masuk dengan `az login` untuk autentikasi Entra ID tanpa kunci

3. **Konflik paket:**
   - Gunakan lingkungan virtual baru
   - Pasang dari `requirements.txt` daripada paket individual
   - Beberapa notebook mungkin memerlukan paket tambahan yang disebutkan di sel markdown mereka

4. **Layanan Azure:**
   - Layanan Azure AI membutuhkan langganan aktif
   - Beberapa fitur spesifik wilayah
   - Pastikan penyebaran model Azure OpenAI mendukung Responses API

### Jalur Pembelajaran

Rekomendasi urutan pelajaran:
1. **00-course-setup** - Mulai di sini untuk setup lingkungan
2. **01-intro-to-ai-agents** - Pahami dasar agen AI
3. **02-explore-agentic-frameworks** - Pelajari kerangka kerja berbeda
4. **03-agentic-design-patterns** - Pola desain inti
5. Lanjutkan pelajaran bernomor secara berurutan

### Pemilihan Kerangka Kerja

Pilih kerangka kerja sesuai tujuan Anda:
- **Semua pelajaran**: Microsoft Agent Framework (MAF) dengan `FoundryChatClient`
- **Agen mendaftar di sisi server** di Microsoft Foundry Agent Service V2 dan terlihat di portal Foundry

### Mendapatkan Bantuan

- Bergabunglah dengan [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Tinjau file README pelajaran untuk panduan spesifik
- Cek [README.md](./README.md) utama untuk gambaran kursus
- Rujuk [Course Setup](./00-course-setup/README.md) untuk instruksi setup rinci

### Berkontribusi

Ini adalah proyek edukasi terbuka. Kontribusi disambut:
- Perbaiki contoh kode
- Perbaiki typo atau kesalahan
- Tambah komentar penjelas
- Usulkan topik pelajaran baru
- Terjemahkan ke bahasa tambahan

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk kebutuhan saat ini.

## Konteks Spesifik Proyek

### Dukungan Multi-Bahasa

Repositori ini menggunakan sistem terjemahan otomatis:
- Mendukung 50+ bahasa
- Terjemahan berada di direktori `/translations/<lang-code>/`
- Workflow GitHub Actions menangani pembaruan terjemahan
- Berkas sumber dalam bahasa Inggris di root repositori

### Struktur Pelajaran

Setiap pelajaran mengikuti pola konsisten:
1. Thumbnail video dengan tautan
2. Konten pelajaran tertulis (README.md)
3. Contoh kode dalam berbagai kerangka kerja
4. Tujuan pembelajaran dan prasyarat
5. Sumber pembelajaran tambahan yang ditautkan

### Penamaan Contoh Kode

Format: `<nomor-pelajaran>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Pelajaran 1, MAF Python
- `14-sequential.ipynb` - Pelajaran 14, pola lanjutan MAF

### Direktori Khusus

- `translated_images/` - Gambar lokal untuk terjemahan
- `images/` - Gambar asli untuk konten bahasa Inggris
- `.devcontainer/` - Konfigurasi kontainer pengembangan VS Code
- `.github/` - Workflow dan template GitHub Actions

### Dependensi

Paket utama dari `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Dukungan protokol Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Layanan Azure AI
- `azure-identity` - Autentikasi Azure (AzureCliCredential)
- `azure-search-documents` - Integrasi Azure AI Search
- `mcp[cli]` - Dukungan Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->