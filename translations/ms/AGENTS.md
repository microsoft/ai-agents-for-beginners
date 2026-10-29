# AGENTS.md

## Gambaran Projek

Repositori ini mengandungi "Ejen AI untuk Pemula" - kursus pendidikan komprehensif yang mengajar segala yang diperlukan untuk membina Ejen AI. Kursus ini terdiri daripada 18 pelajaran (dinomborkan 00-18) yang merangkumi asas, corak reka bentuk, kerangka kerja, pengeluaran pengeluaran, ejen tempatan/pada peranti, dan keselamatan ejen AI.

**Teknologi Utama:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- Kerangka AI: Microsoft Agent Framework (MAF)
- Perkhidmatan AI Azure: Microsoft Foundry, Perkhidmatan Ejen Microsoft Foundry V2

**Arkitektur:**
- Struktur berasaskan pelajaran (direktori 00-18)
- Setiap pelajaran mengandungi: dokumentasi README, contoh kod (notebook Jupyter), dan imej
- Sokongan pelbagai bahasa melalui sistem terjemahan automatik
- Satu notebook Python setiap pelajaran menggunakan Microsoft Agent Framework

## Perintah Persediaan

### Prasyarat
- Python 3.12 atau lebih tinggi
- Langganan Azure (untuk Microsoft Foundry)
- Azure CLI dipasang dan diautentikasi (`az login`)

### Persediaan Awal

1. **Clone atau fork repositori:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Buat dan aktifkan persekitaran maya Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Pasang kebergantungan:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Tetapkan pembolehubah persekitaran:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Pembolehubah Persekitaran Diperlukan

Untuk **Microsoft Foundry** (Diperlukan):
- `AZURE_AI_PROJECT_ENDPOINT` - titik akhir projek Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nama pengeluaran model (contoh, gpt-5-mini)

Untuk **Azure AI Search** (Pelajaran 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - titik akhir Azure AI Search
- `AZURE_SEARCH_API_KEY` - kunci API Azure AI Search

Pengesahan: Jalankan `az login` sebelum menjalankan notebook (menggunakan `AzureCliCredential`).

## Aliran Kerja Pembangunan

### Menjalankan Jupyter Notebooks

Setiap pelajaran mengandungi pelbagai notebook Jupyter untuk kerangka kerja berbeza:

1. **Mulakan Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigasi ke direktori pelajaran** (contohnya `01-intro-to-ai-agents/code_samples/`)

3. **Buka dan jalankan notebook:**
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)

### Bekerja dengan Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Memerlukan langganan Azure
- Menggunakan `FoundryChatClient` untuk Perkhidmatan Ejen V2 (ejen kelihatan di portal Foundry)
- Sedia produksi dengan kebolehamatan terbina dalam
- Corak fail: `*-python-agent-framework.ipynb`

## Arahan Ujian

Ini adalah repositori pendidikan dengan contoh kod dan bukan kod produksi dengan ujian automatik. Untuk mengesahkan persediaan dan perubahan anda:

### Ujian Manual

1. **Uji persekitaran Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Uji pelaksanaan notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Sahkan pembolehubah persekitaran:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Menjalankan Notebook Individu

Buka notebook dalam Jupyter dan jalankan sel secara berurutan. Setiap notebook berdiri sendiri dan termasuk:
- Penyataan import
- Memuat konfigurasi
- Contoh pelaksanaan ejen
- Output yang dijangkakan dalam sel markdown

### Ujian Asap Ejen yang Dikerahkan

Untuk pelajaran di mana ejen dikerahkan sebagai ejen dihos Microsoft Foundry (01, 04, 05, 16), repo menyediakan katalog ujian asap di bawah `tests/` yang dijalankan oleh aliran kerja `.github/workflows/smoke-test.yml` melalui tindakan [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Ini adalah pintu ringan selepas pengeluaran (adakah ejen boleh dicapai dan memenuhi jangkaan arahan asas?), melengkapkan saluran penilaian dalam Pelajaran 10 dan 16. Lihat [tests/README.md](./tests/README.md) untuk pemetaan katalog-ke-pelajaran-ke-ejen. Pelajaran 17 dijalankan secara tempatan dengan Foundry Local dan tidak mempunyai titik hujung dihos, jadi ia disahkan dengan menjalankan notebooknya terus.

## Gaya Kod

### Konvensyen Python

- **Versi Python**: 3.12+
- **Gaya Kod**: Ikuti konvensyen PEP 8 Python standard
- **Notebook**: Gunakan sel markdown yang jelas untuk menerangkan konsep
- **Import**: Kumpulkan mengikut perpustakaan standard, pihak ketiga, import tempatan

### Konvensyen Jupyter Notebook

- Sertakan sel markdown penerangan sebelum sel kod
- Tambah contoh output dalam notebook untuk rujukan
- Gunakan nama pembolehubah yang jelas yang selaras dengan konsep pelajaran
- Kekalkan urutan pelaksanaan notebook secara linear (sel 1 → 2 → 3...)

### Pengurusan Fail

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Pembinaan dan Pengeluaran

### Membina Dokumentasi

Repositori ini menggunakan Markdown untuk dokumentasi:
- Fail README.md dalam setiap folder pelajaran
- README.md utama di akar repositori
- Sistem terjemahan automatik melalui GitHub Actions

### Saluran CI/CD

Terletak di `.github/workflows/`:

1. **co-op-translator.yml** - Terjemahan automatik ke 50+ bahasa
2. **welcome-issue.yml** - Menyambut pencipta isu baru
3. **welcome-pr.yml** - Menyambut penyumbang pull request baru

### Pengeluaran

Ini adalah repositori pendidikan - tiada proses pengeluaran. Pengguna:
1. Fork atau clone repositori
2. Jalankan notebook secara tempatan atau dalam GitHub Codespaces
3. Belajar dengan memodifikasi dan bereksperimen dengan contoh

## Garis Panduan Pull Request

### Sebelum Mengemukakan

1. **Uji perubahan anda:**
   - Jalankan notebook terjejas sepenuhnya
   - Sahkan semua sel berjalan tanpa ralat
   - Periksa output adalah sesuai

2. **Kemas kini dokumentasi:**
   - Kemas kini README.md jika menambah konsep baru
   - Tambah komen dalam notebook untuk kod kompleks
   - Pastikan sel markdown menerangkan tujuan

3. **Perubahan fail:**
   - Elakkan commit fail `.env` (gunakan `.env.example`)
   - Jangan commit direktori `venv/` atau `__pycache__/`
   - Kekalkan output notebook apabila ia menunjukkan konsep
   - Buang fail sementara dan notebook sandaran (`*-backup.ipynb`)

### Format Tajuk PR

Gunakan tajuk yang menerangkan:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Pemeriksaan Diperlukan

- Notebook harus dijalankan tanpa ralat
- Fail README harus jelas dan tepat
- Ikuti corak kod sedia ada dalam repositori
- Kekalkan konsistensi dengan pelajaran lain

## Nota Tambahan

### Perkara Lazim Bermasalah

1. **Ketidakpadanan versi Python:**
   - Pastikan menggunakan Python 3.12+
   - Sesetengah pakej mungkin tidak berfungsi dengan versi lama
   - Gunakan `python3 -m venv` untuk nyatakan versi Python dengan jelas

2. **Pembolehubah persekitaran:**
   - Sentiasa buat `.env` daripada `.env.example`
   - Jangan commit fail `.env` (ia dalam `.gitignore`)
   - Log masuk dengan `az login` untuk pengesahan Entra ID tanpa kunci

3. **Konflik pakej:**
   - Gunakan persekitaran maya baru
   - Pasang dari `requirements.txt` dan bukan pakej individu
   - Sesetengah notebook mungkin memerlukan pakej tambahan yang disebut dalam sel markdown mereka

4. **Perkhidmatan Azure:**
   - Perkhidmatan AI Azure memerlukan langganan aktif
   - Sesetengah ciri khusus untuk wilayah
   - Pastikan pengeluaran model Azure OpenAI anda menyokong API Respon

### Laluan Pembelajaran

Cadangan susunan pelajaran:
1. **00-course-setup** - Mula di sini untuk persediaan persekitaran
2. **01-intro-to-ai-agents** - Fahami asas ejen AI
3. **02-explore-agentic-frameworks** - Belajar mengenai kerangka kerja yang berbeza
4. **03-agentic-design-patterns** - Corak reka bentuk teras
5. Teruskan melalui pelajaran dinomborkan secara berurutan

### Pemilihan Kerangka Kerja

Pilih kerangka berdasarkan matlamat anda:
- **Semua pelajaran**: Microsoft Agent Framework (MAF) dengan `FoundryChatClient`
- **Ejen mendaftar di server sisi** dalam Perkhidmatan Ejen Microsoft Foundry V2 dan kelihatan di portal Foundry

### Mendapatkan Bantuan

- Sertai [Komuniti Discord Microsoft Foundry](https://aka.ms/ai-agents/discord)
- Semak fail README pelajaran untuk panduan khusus
- Periksa [README.md] utama (./README.md) untuk gambaran kursus
- Rujuk [Setup Kursus](./00-course-setup/README.md) untuk arahan persediaan terperinci

### Menyumbang

Ini adalah projek pendidikan terbuka. Penyumbang dialu-alukan:
- Memperbaiki contoh kod
- Betulkan ralat atau kesalahan taip
- Tambah komen penjelasan
- Cadangkan topik pelajaran baru
- Terjemahkan ke bahasa tambahan

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk keperluan semasa.

## Konteks Projek Spesifik

### Sokongan Pelbagai Bahasa

Repositori ini menggunakan sistem terjemahan automatik:
- Menyokong 50+ bahasa
- Terjemahan dalam direktori `/translations/<lang-code>/`
- Aliran kerja GitHub Actions mengendalikan kemaskini terjemahan
- Fail sumber dalam Bahasa Inggeris di akar repositori

### Struktur Pelajaran

Setiap pelajaran mengikuti corak konsisten:
1. Gambar kecil video dengan pautan
2. Kandungan pelajaran bertulis (README.md)
3. Contoh kod dalam pelbagai kerangka
4. Objektif pembelajaran dan prasyarat
5. Sumber pembelajaran tambahan dipautkan

### Penamaan Contoh Kod

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Pelajaran 1, MAF Python
- `14-sequential.ipynb` - Pelajaran 14, corak lanjutan MAF
- `16-python-agent-framework.ipynb` - Pelajaran 16, ejen sokongan pelanggan produksi
- `17-local-agent-foundry-local.ipynb` - Pelajaran 17, ejen tempatan dengan Foundry Local + Qwen

### Direktori Khas

- `translated_images/` - Imej disesuaikan untuk terjemahan
- `images/` - Imej asal untuk kandungan Bahasa Inggeris
- `.devcontainer/` - Konfigurasi bekas pembangunan VS Code
- `.github/` - Aliran kerja dan templat GitHub Actions

### Kebergantungan

Pakej utama dari `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Sokongan protokol Agent-ke-Agent
- `azure-ai-inference`, `azure-ai-projects` - Perkhidmatan AI Azure
- `azure-identity` - Pengesahan Azure (AzureCliCredential)
- `azure-search-documents` - Integrasi Azure AI Search
- `mcp[cli]` - Sokongan Protokol Konteks Model

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->