# AGENTS.md

## Gambaran Proyek

Repositori ini berisi "AI Agents untuk Pemula" - sebuah kursus pendidikan komprehensif yang mengajarkan segala sesuatu yang diperlukan untuk membangun AI Agents. Kursus ini terdiri dari lebih dari 15 pelajaran yang mencakup dasar-dasar, pola desain, kerangka kerja, dan penerapan produksi AI agents.

**Teknologi Utama:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- Kerangka AI: Microsoft Agent Framework (MAF)
- Layanan Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arsitektur:**
- Struktur berbasis pelajaran (direktori 00-15+)
- Setiap pelajaran berisi: dokumentasi README, contoh kode (Jupyter notebooks), dan gambar
- Dukungan multi-bahasa melalui sistem terjemahan otomatis
- Satu notebook Python per pelajaran menggunakan Microsoft Agent Framework

## Perintah Setup

### Prasyarat
- Python 3.12 atau lebih tinggi
- Langganan Azure (untuk Azure AI Foundry)
- Azure CLI terinstal dan terautentikasi (`az login`)

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

3. **Pasang ketergantungan:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Atur variabel lingkungan:**
   ```bash
   cp .env.example .env
   # Edit .env dengan kunci API dan endpoint Anda
   ```

### Variabel Lingkungan yang Diperlukan

Untuk **Azure AI Foundry** (Diperlukan):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint proyek Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nama penerapan model (misal: gpt-4o)

Untuk **Azure AI Search** (Pelajaran 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - kunci API Azure AI Search

Otentikasi: Jalankan `az login` sebelum menjalankan notebook (menggunakan `AzureCliCredential`).

## Alur Kerja Pengembangan

### Menjalankan Jupyter Notebooks

Setiap pelajaran berisi beberapa notebook Jupyter untuk berbagai kerangka kerja:

1. **Mulai Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigasi ke direktori pelajaran** (misal `01-intro-to-ai-agents/code_samples/`)

3. **Buka dan jalankan notebook:**
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)

### Bekerja dengan Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Membutuhkan langganan Azure
- Menggunakan `AzureAIProjectAgentProvider` untuk Agent Service V2 (agen terlihat di portal Foundry)
- Siap produksi dengan observabilitas bawaan
- Pola file: `*-python-agent-framework.ipynb`

## Instruksi Pengujian

Ini adalah repositori edukasi dengan kode contoh, bukan kode produksi dengan pengujian otomatis. Untuk memverifikasi setup dan perubahan Anda:

### Pengujian Manual

1. **Uji lingkungan Python:**
   ```bash
   python --version  # Harus 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Uji eksekusi notebook:**
   ```bash
   # Ubah notebook menjadi skrip dan jalankan (menguji impor)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifikasi variabel lingkungan:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Menjalankan Notebook Individu

Buka notebook di Jupyter dan jalankan sel secara berurutan. Setiap notebook bersifat mandiri dan mencakup:
- Pernyataan impor
- Pemuatan konfigurasi
- Implementasi contoh agen
- Output yang diharapkan dalam sel markdown

## Gaya Kode

### Konvensi Python

- **Versi Python**: 3.12+
- **Gaya Kode**: Ikuti konvensi standar Python PEP 8
- **Notebooks**: Gunakan sel markdown yang jelas untuk menjelaskan konsep
- **Impor**: Kelompokkan berdasarkan pustaka standar, pihak ketiga, lokal

### Konvensi Jupyter Notebook

- Sertakan sel markdown deskriptif sebelum sel kode
- Tambahkan contoh output di notebook sebagai referensi
- Gunakan nama variabel yang jelas dan sesuai konsep pelajaran
- Jaga urutan eksekusi notebook linier (sel 1 → 2 → 3...)

### Organisasi File

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Bangun dan Penyebaran

### Membangun Dokumentasi

Repositori ini menggunakan Markdown untuk dokumentasi:
- File README.md di setiap folder pelajaran
- README.md utama di root repositori
- Sistem terjemahan otomatis melalui GitHub Actions

### Pipeline CI/CD

Terletak di `.github/workflows/`:

1. **co-op-translator.yml** - Terjemahan otomatis ke 50+ bahasa
2. **welcome-issue.yml** - Menyambut pembuat isu baru
3. **welcome-pr.yml** - Menyambut kontributor pull request baru

### Penyebaran

Ini adalah repositori edukasi - tidak ada proses penyebaran. Pengguna:
1. Fork atau clone repositori
2. Jalankan notebook secara lokal atau di GitHub Codespaces
3. Belajar dengan memodifikasi dan bereksperimen dengan contoh

## Panduan Pull Request

### Sebelum Mengirim

1. **Uji perubahan Anda:**
   - Jalankan notebook yang terdampak secara lengkap
   - Pastikan semua sel berjalan tanpa error
   - Periksa apakah output sudah sesuai

2. **Pembaruan dokumentasi:**
   - Perbarui README.md jika menambahkan konsep baru
   - Tambahkan komentar di notebook untuk kode yang kompleks
   - Pastikan sel markdown menjelaskan tujuannya

3. **Perubahan file:**
   - Hindari commit file `.env` (gunakan `.env.example`)
   - Jangan commit direktori `venv/` atau `__pycache__/`
   - Simpan output notebook jika menunjukkan konsep
   - Hapus file sementara dan notebook cadangan (`*-backup.ipynb`)

### Format Judul PR

Gunakan judul deskriptif:
- `[Lesson-XX] Tambah contoh baru untuk <konsep>`
- `[Fix] Koreksi typo di lesson-XX README`
- `[Update] Perbaiki contoh kode di lesson-XX`
- `[Docs] Perbarui instruksi setup`

### Pengecekan Wajib

- Notebook harus dapat dijalankan tanpa error
- File README harus jelas dan akurat
- Ikuti pola kode yang ada dalam repositori
- Jaga konsistensi dengan pelajaran lain

## Catatan Tambahan

### Kesalahan Umum

1. **Versi Python tidak cocok:**
   - Pastikan menggunakan Python 3.12+
   - Beberapa paket mungkin tidak berfungsi dengan versi lama
   - Gunakan `python3 -m venv` untuk menentukan versi Python secara eksplisit

2. **Variabel lingkungan:**
   - Selalu buat `.env` dari `.env.example`
   - Jangan commit file `.env` (sudah di `.gitignore`)
   - Token GitHub perlu izin yang tepat

3. **Konflik paket:**
   - Gunakan lingkungan virtual baru
   - Pasang dari `requirements.txt` bukan paket satu per satu
   - Beberapa notebook mungkin perlu paket tambahan yang disebutkan di sel markdown mereka

4. **Layanan Azure:**
   - Layanan Azure AI memerlukan langganan aktif
   - Beberapa fitur terbatas per wilayah
   - Batas gratis berlaku untuk GitHub Models

### Jalur Pembelajaran

Rekomendasi progresi pelajaran:
1. **00-course-setup** - Mulai di sini untuk setup lingkungan
2. **01-intro-to-ai-agents** - Pahami dasar agent AI
3. **02-explore-agentic-frameworks** - Pelajari berbagai kerangka kerja
4. **03-agentic-design-patterns** - Pola desain inti
5. Lanjutkan pelajaran berurutan berdasarkan nomor

### Pemilihan Kerangka Kerja

Pilih kerangka kerja berdasarkan tujuan Anda:
- **Semua pelajaran**: Microsoft Agent Framework (MAF) dengan `AzureAIProjectAgentProvider`
- **Agen mendaftar server-side** di Azure AI Foundry Agent Service V2 dan terlihat di portal Foundry

### Mendapatkan Bantuan

- Bergabung dengan [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Tinjau file README pelajaran untuk panduan khusus
- Cek [README.md utama](./README.md) untuk gambaran kursus
- Rujuk [Course Setup](./00-course-setup/README.md) untuk instruksi setup detail

### Kontribusi

Ini adalah proyek edukasi terbuka. Kontribusi dipersilakan:
- Tingkatkan contoh kode
- Perbaiki typo atau kesalahan
- Tambahkan komentar yang memperjelas
- Usulkan topik pelajaran baru
- Terjemahkan ke bahasa lain

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk kebutuhan saat ini.

## Konteks Khusus Proyek

### Dukungan Multi-Bahasa

Repositori ini menggunakan sistem terjemahan otomatis:
- Mendukung 50+ bahasa
- Terjemahan di direktori `/translations/<kode-bahasa>/`
- Workflow GitHub Actions menangani pembaruan terjemahan
- File sumber berbahasa Inggris di root repositori

### Struktur Pelajaran

Setiap pelajaran mengikuti pola konsisten:
1. Thumbnail video dengan tautan
2. Isi pelajaran tertulis (README.md)
3. Contoh kode di berbagai kerangka kerja
4. Tujuan pembelajaran dan prasyarat
5. Sumber belajar tambahan tertaut

### Penamaan Contoh Kode

Format: `<nomor-pelajaran>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Pelajaran 1, MAF Python
- `14-sequential.ipynb` - Pelajaran 14, pola lanjutan MAF

### Direktori Spesial

- `translated_images/` - Gambar yang sudah diterjemahkan
- `images/` - Gambar asli untuk konten bahasa Inggris
- `.devcontainer/` - Konfigurasi container pengembangan VS Code
- `.github/` - Workflow dan template GitHub Actions

### Ketergantungan

Paket utama dari `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Dukungan protokol Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Layanan Azure AI
- `azure-identity` - Otentikasi Azure (AzureCliCredential)
- `azure-search-documents` - Integrasi Azure AI Search
- `mcp[cli]` - Dukungan Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->