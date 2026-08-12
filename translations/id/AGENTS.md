# AGENTS.md

## Ikhtisar Proyek

Repositori ini berisi "Agen AI untuk Pemula" - sebuah kursus edukasi komprehensif yang mengajarkan segala hal yang dibutuhkan untuk membangun Agen AI. Kursus ini terdiri dari 18 pelajaran (dinomori 00-18) yang mencakup dasar-dasar, pola desain, kerangka kerja, penerapan produksi, agen lokal/pada perangkat, dan keamanan agen AI.

**Teknologi Utama:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- Kerangka Kerja AI: Microsoft Agent Framework (MAF)
- Layanan AI Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arsitektur:**
- Struktur berbasis pelajaran (direktori 00-15+)
- Setiap pelajaran berisi: dokumentasi README, contoh kode (Jupyter notebooks), dan gambar
- Dukungan multi-bahasa melalui sistem penerjemahan otomatis
- Satu notebook Python per pelajaran menggunakan Microsoft Agent Framework

## Perintah Setup

### Prasyarat
- Python 3.12 atau lebih tinggi
- Langganan Azure (untuk Microsoft Foundry)
- Azure CLI terpasang dan sudah autentikasi (`az login`)

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

3. **Instal dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setel variabel lingkungan:**
   ```bash
   cp .env.example .env
   # Edit .env dengan kunci API dan endpoint Anda
   ```

### Variabel Lingkungan yang Diperlukan

Untuk **Microsoft Foundry** (Diperlukan):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint proyek Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nama penerapan model (contoh: gpt-5-mini)

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

2. **Arahkan ke direktori pelajaran** (contoh: `01-intro-to-ai-agents/code_samples/`)

3. **Buka dan jalankan notebook:**
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)

### Bekerja dengan Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Membutuhkan langganan Azure
- Menggunakan `FoundryChatClient` untuk Agent Service V2 (agen terlihat di portal Foundry)
- Siap produksi dengan observabilitas bawaan
- Pola file: `*-python-agent-framework.ipynb`

## Petunjuk Pengujian

Ini adalah repositori edukasi dengan contoh kode, bukan kode produksi dengan pengujian otomatis. Untuk memverifikasi setup dan perubahan Anda:

### Pengujian Manual

1. **Uji lingkungan Python:**
   ```bash
   python --version  # Harus 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Uji eksekusi notebook:**
   ```bash
   # Ubah notebook menjadi skrip dan jalankan (mengujikan impor)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifikasi variabel lingkungan:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Menjalankan Notebook Individu

Buka notebook di Jupyter dan eksekusi sel secara berurutan. Setiap notebook berdiri sendiri dan mencakup:
- Pernyataan impor
- Pemuatan konfigurasi
- Implementasi contoh agen
- Output yang diharapkan dalam sel markdown

### Smoke-Testing Agen yang Diterapkan

Untuk pelajaran dimana agen diterapkan sebagai agen Microsoft Foundry yang dihosting (01, 04, 05, 16), repo menyediakan katalog smoke-test di bawah `tests/` yang dijalankan oleh workflow `.github/workflows/smoke-test.yml` melalui aksi [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Ini adalah gerbang pasca-tayang ringan (apakah agen bisa dijangkau dan mengikuti ekspektasi prompt dasar?), melengkapi pipeline evaluasi pada Pelajaran 10 dan 16. Lihat [tests/README.md](./tests/README.md) untuk pemetaan katalog-ke-pelajaran-ke-agen. Pelajaran 17 dijalankan secara lokal dengan Foundry Local dan tidak memiliki endpoint yang dihosting, sehingga divalidasi dengan menjalankan notebooknya langsung.

## Gaya Kode

### Konvensi Python

- **Versi Python**: 3.12+
- **Gaya Kode**: Ikuti konvensi standar Python PEP 8
- **Notebook**: Gunakan sel markdown yang jelas untuk menjelaskan konsep
- **Impor**: Kelompokkan berdasarkan pustaka standar, pihak ketiga, impor lokal

### Konvensi Jupyter Notebook

- Sertakan sel markdown deskriptif sebelum sel kode
- Tambahkan contoh output di notebook sebagai referensi
- Gunakan nama variabel yang jelas sesuai konsep pelajaran
- Jaga urutan eksekusi notebook linear (sel 1 → 2 → 3...)

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

## Build dan Deployment

### Membangun Dokumentasi

Repositori ini menggunakan Markdown untuk dokumentasi:
- Berkas README.md di setiap folder pelajaran
- README.md utama di root repositori
- Sistem penerjemahan otomatis melalui GitHub Actions

### Pipeline CI/CD

Berada di `.github/workflows/`:

1. **co-op-translator.yml** - Penerjemahan otomatis ke 50+ bahasa
2. **welcome-issue.yml** - Menyambut pembuat isu baru
3. **welcome-pr.yml** - Menyambut kontributor pull request baru

### Deployment

Ini adalah repositori edukasi - tidak ada proses deployment. Pengguna:
1. Fork atau clone repositori
2. Jalankan notebook secara lokal atau di GitHub Codespaces
3. Belajar dengan memodifikasi dan bereksperimen dengan contoh

## Pedoman Pull Request

### Sebelum Mengirim

1. **Uji perubahan Anda:**
   - Jalankan notebook yang terdampak secara lengkap
   - Verifikasi semua sel berjalan tanpa error
   - Periksa bahwa output sesuai

2. **Pembaruan dokumentasi:**
   - Perbarui README.md jika menambahkan konsep baru
   - Tambahkan komentar pada notebook untuk kode kompleks
   - Pastikan sel markdown menjelaskan tujuan

3. **Perubahan berkas:**
   - Hindari commit berkas `.env` (gunakan `.env.example`)
   - Jangan commit direktori `venv/` atau `__pycache__/`
   - Simpan output notebook jika mendemonstrasikan konsep
   - Hapus berkas sementara dan notebook cadangan (`*-backup.ipynb`)

### Format Judul PR

Gunakan judul yang deskriptif:
- `[Lesson-XX] Tambah contoh baru untuk <konsep>`
- `[Fix] Koreksi typo di README pelajaran-XX`
- `[Update] Perbaiki contoh kode di pelajaran-XX`
- `[Docs] Perbarui instruksi setup`

### Pemeriksaan Wajib

- Notebook harus berjalan tanpa error
- Berkas README harus jelas dan akurat
- Ikuti pola kode yang sudah ada di repositori
- Pertahankan konsistensi dengan pelajaran lain

## Catatan Tambahan

### Hal-hal Umum yang Harus Diwaspadai

1. **Ketidaksesuaian versi Python:**
   - Pastikan menggunakan Python 3.12+
   - Beberapa paket mungkin tidak bekerja dengan versi lama
   - Gunakan `python3 -m venv` untuk menentukan versi Python secara eksplisit

2. **Variabel lingkungan:**
   - Selalu buat `.env` dari `.env.example`
   - Jangan commit berkas `.env` (sudah ada di `.gitignore`)
   - Login dengan `az login` untuk autentikasi Entra ID tanpa kunci

3. **Konflik paket:**
   - Gunakan lingkungan virtual baru
   - Instal dari `requirements.txt` daripada paket terpisah
   - Beberapa notebook mungkin memerlukan paket tambahan yang disebutkan di sel markdownnya

4. **Layanan Azure:**
   - Layanan AI Azure memerlukan langganan aktif
   - Beberapa fitur spesifik wilayah
   - Pastikan penerapan model Azure OpenAI Anda mendukung Responses API

### Jalur Pembelajaran

Rekomendasi urutan pelajaran:
1. **00-course-setup** - Mulai dari sini untuk setup lingkungan
2. **01-intro-to-ai-agents** - Pahami dasar agen AI
3. **02-explore-agentic-frameworks** - Pelajari berbagai kerangka kerja
4. **03-agentic-design-patterns** - Pola desain inti
5. Lanjutkan pelajaran bernomor secara berurutan

### Pemilihan Kerangka Kerja

Pilih kerangka kerja berdasarkan tujuan Anda:
- **Semua pelajaran**: Microsoft Agent Framework (MAF) dengan `FoundryChatClient`
- **Agen terdaftar sisi server** di Microsoft Foundry Agent Service V2 dan terlihat di portal Foundry

### Mendapatkan Bantuan

- Bergabung dengan [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Tinjau berkas README pelajaran untuk panduan khusus
- Periksa [README.md](./README.md) utama untuk ikhtisar kursus
- Lihat [Course Setup](./00-course-setup/README.md) untuk instruksi setup rinci

### Kontribusi

Ini adalah proyek edukasi terbuka. Kontribusi diterima:
- Perbaiki contoh kode
- Perbaiki typo atau kesalahan
- Tambahkan komentar yang memperjelas
- Usulkan topik pelajaran baru
- Terjemahkan ke bahasa tambahan

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk kebutuhan saat ini.

## Konteks Khusus Proyek

### Dukungan Multi-Bahasa

Repositori ini menggunakan sistem penerjemahan otomatis:
- Mendukung 50+ bahasa
- Terjemahan berada di direktori `/translations/<kode-bahasa>/`
- GitHub Actions mengelola pembaruan terjemahan
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
- `16-python-agent-framework.ipynb` - Pelajaran 16, agen dukungan pelanggan produksi
- `17-local-agent-foundry-local.ipynb` - Pelajaran 17, agen lokal dengan Foundry Local + Qwen

### Direktori Khusus

- `translated_images/` - Gambar yang dilokalkan untuk terjemahan
- `images/` - Gambar asli untuk konten bahasa Inggris
- `.devcontainer/` - konfigurasi kontainer pengembangan VS Code
- `.github/` - workflow dan template GitHub Actions

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