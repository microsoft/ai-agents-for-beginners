# AGENTS.md

## Gambaran Projek

Repositori ini mengandungi "Ejen AI untuk Pemula" - kursus pendidikan menyeluruh yang mengajar segala yang diperlukan untuk membina Ejen AI. Kursus ini terdiri daripada 18 pelajaran (dinomborkan 00-18) yang merangkumi asas, corak reka bentuk, rangka kerja, pengeluaran pengeluaran, ejen tempatan/pada peranti, dan keselamatan ejen AI.

**Teknologi Utama:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- Rangka Kerja AI: Microsoft Agent Framework (MAF)
- Perkhidmatan AI Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Seni Bina:**
- Struktur berasaskan pelajaran (direktori 00-15+)
- Setiap pelajaran mengandungi: dokumentasi README, contoh kod (Jupyter notebooks), dan imej
- Sokongan pelbagai bahasa melalui sistem terjemahan automatik
- Satu notebook Python setiap pelajaran menggunakan Microsoft Agent Framework

## Arahan Penyediaan

### Prasyarat
- Python 3.12 atau lebih tinggi
- Langganan Azure (untuk Microsoft Foundry)
- Azure CLI dipasang dan diautentikasi (`az login`)

### Penyediaan Awal

1. **Clone atau fork repositori:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ATAU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Cipta dan aktifkan persekitaran maya Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Pada Windows: venv\Scripts\activate
   ```

3. **Pasang pergantungan:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Tetapkan pembolehubah persekitaran:**
   ```bash
   cp .env.example .env
   # Edit .env dengan kunci API dan titik hujung anda
   ```

### Pembolehubah Persekitaran Diperlukan

Untuk **Microsoft Foundry** (Diperlukan):
- `AZURE_AI_PROJECT_ENDPOINT` - titik hujung projek Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nama penyebaran model (contoh, gpt-5-mini)

Untuk **Azure AI Search** (Pelajaran 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - titik hujung Azure AI Search
- `AZURE_SEARCH_API_KEY` - kunci API Azure AI Search

Pengesahan: Jalankan `az login` sebelum menjalankan notebook (menggunakan `AzureCliCredential`).

## Aliran Kerja Pembangunan

### Menjalankan Jupyter Notebooks

Setiap pelajaran mengandungi pelbagai Jupyter notebook untuk rangka kerja berbeza:

1. **Mulakan Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigasi ke direktori pelajaran** (contoh, `01-intro-to-ai-agents/code_samples/`)

3. **Buka dan jalankan notebook:**
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)

### Bekerja dengan Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Memerlukan langganan Azure
- Menggunakan `FoundryChatClient` untuk Agent Service V2 (ejen kelihatan di portal Foundry)
- Sedia untuk pengeluaran dengan kebolehlihatan terbina dalam
- Corak fail: `*-python-agent-framework.ipynb`

## Arahan Ujian

Ini adalah repositori pendidikan dengan kod contoh dan bukan kod produksi dengan ujian automatik. Untuk mengesahkan penyediaan dan perubahan anda:

### Ujian Manual

1. **Uji persekitaran Python:**
   ```bash
   python --version  # Mesti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Uji pelaksanaan notebook:**
   ```bash
   # Tukar nota buku ke skrip dan jalankan (uji import)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Sahkan pembolehubah persekitaran:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Menjalankan Notebook Individu

Buka notebook dalam Jupyter dan jalankan sel secara berurutan. Setiap notebook berdiri sendiri dan termasuk:
- Pernyataan import
- Pemindahan konfigurasi
- Pelaksanaan contoh ejen
- Output yang dijangka dalam sel markdown

### Ujian Ringkas Ejen Terpasang

Untuk pelajaran di mana ejen dipasang sebagai ejen Microsoft Foundry hos (01, 04, 05, 16), repo ini menghantar katalog ujian ringkas di bawah `tests/` yang dijalankan oleh aliran kerja `.github/workflows/smoke-test.yml` melalui tindakan [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Ini adalah pintu ringan selepas pasca-pemasangan (adakah ejen boleh dicapai dan mengikuti jangkaan prompt asas?), melengkapi saluran penilaian dalam Pelajaran 10 dan 16. Lihat [tests/README.md](./tests/README.md) untuk pemetaan katalog-ke-pelajaran-ke-ejen. Pelajaran 17 dijalankan secara tempatan dengan Foundry Local dan tiada titik hujung hos, jadi ia disahkan dengan menjalankan notebuknya secara langsung.

## Gaya Kod

### Konvensyen Python

- **Versi Python**: 3.12+
- **Gaya Kod**: Ikut konvensyen standard Python PEP 8
- **Notebook**: Gunakan sel markdown yang jelas untuk menerangkan konsep
- **Imports**: Kumpul mengikut pustaka standard, pihak ketiga, import tempatan

### Konvensyen Jupyter Notebook

- Sertakan sel markdown deskriptif sebelum sel kod
- Tambah contoh output dalam notebook sebagai rujukan
- Gunakan nama pembolehubah yang jelas dan padan dengan konsep pelajaran
- Kekalkan susunan pelaksanaan notebook secara linear (sel 1 → 2 → 3...)

### Organisasi Fail

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

Terletak dalam `.github/workflows/`:

1. **co-op-translator.yml** - Terjemahan automatik ke 50+ bahasa
2. **welcome-issue.yml** - Mengalu-alukan pencipta isu baru
3. **welcome-pr.yml** - Mengalu-alukan penyumbang permintaan tarik baru

### Pengeluaran

Ini adalah repositori pendidikan - tiada proses pengeluaran. Pengguna:
1. Fork atau clone repositori
2. Jalankan notebook secara tempatan atau dalam GitHub Codespaces
3. Belajar dengan mengubah dan bereksperimen dengan contoh

## Garis Panduan Permintaan Tarik

### Sebelum Menghantar

1. **Uji perubahan anda:**
   - Jalankan notebook yang terlibat sepenuhnya
   - Sahkan semua sel berjalan tanpa ralat
   - Semak agar output adalah sesuai

2. **Kemaskini dokumentasi:**
   - Kemas kini README.md jika menambah konsep baru
   - Tambah komen dalam notebook untuk kod kompleks
   - Pastikan sel markdown menerangkan tujuan

3. **Perubahan fail:**
   - Elakkan komit fail `.env` (gunakan `.env.example`)
   - Jangan komit direktori `venv/` atau `__pycache__/`
   - Kekalkan output notebook jika ia menerangkan konsep
   - Buang fail sementara dan notebook sandaran (`*-backup.ipynb`)

### Format Tajuk PR

Gunakan tajuk deskriptif:
- `[Lesson-XX] Tambah contoh baru untuk <konsep>`
- `[Fix] Betulkan ejaan dalam README pelajaran-XX`
- `[Update] Tingkatkan contoh kod dalam pelajaran-XX`
- `[Docs] Kemas kini arahan penyediaan`

### Semakan Diperlukan

- Notebook perlu berjalan tanpa ralat
- Fail README mestilah jelas dan tepat
- Ikut corak kod sedia ada dalam repositori
- Kekalkan konsistensi dengan pelajaran lain

## Nota Tambahan

### Kesilapan Lazim

1. **Versi Python tidak sepadan:**
   - Pastikan menggunakan Python 3.12+
   - Sesetengah pakej mungkin tidak berfungsi dengan versi lama
   - Gunakan `python3 -m venv` untuk menyatakan versi Python dengan jelas

2. **Pembolehubah persekitaran:**
   - Sentiasa cipta `.env` dari `.env.example`
   - Jangan commit fail `.env` (ia dalam `.gitignore`)
   - Daftar masuk dengan `az login` untuk pengesahan Entra ID tanpa kunci

3. **Konflik pakej:**
   - Gunakan persekitaran maya baru
   - Pasang dari `requirements.txt` daripada pakej secara individu
   - Sesetengah notebook mungkin perlukan pakej tambahan yang disebut dalam sel markdown mereka

4. **Perkhidmatan Azure:**
   - Perkhidmatan AI Azure memerlukan langganan aktif
   - Sesetengah ciri adalah khusus kepada wilayah
   - Pastikan penyebaran model Azure OpenAI anda menyokong API Respons

### Laluan Pembelajaran

Cadangan kemajuan melalui pelajaran:
1. **00-course-setup** - Mula di sini untuk penyediaan persekitaran
2. **01-intro-to-ai-agents** - Fahami asas ejen AI
3. **02-explore-agentic-frameworks** - Pelajari tentang pelbagai rangka kerja
4. **03-agentic-design-patterns** - Corak reka bentuk teras
5. Teruskan melalui pelajaran bernombor secara berturutan

### Pemilihan Rangka Kerja

Pilih rangka kerja berdasarkan matlamat anda:
- **Semua pelajaran**: Microsoft Agent Framework (MAF) dengan `FoundryChatClient`
- **Ejen mendaftar di server** dalam Microsoft Foundry Agent Service V2 dan boleh dilihat di portal Foundry

### Mendapatkan Bantuan

- Sertai [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Semak fail README pelajaran untuk panduan khusus
- Rujuk [README.md](./README.md) utama untuk gambaran kursus
- Rujuk [Course Setup](./00-course-setup/README.md) untuk arahan penyediaan terperinci

### Menyumbang

Ini adalah projek pendidikan terbuka. Sumbangan dialu-alukan:
- Memperbaiki contoh kod
- Membetulkan ejaan atau ralat
- Menambah komen penjelasan
- Mencadangkan topik pelajaran baru
- Menterjemah ke bahasa tambahan

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk keperluan semasa.

## Konteks Khusus Projek

### Sokongan Pelbagai Bahasa

Repositori ini menggunakan sistem terjemahan automatik:
- Menyokong lebih 50 bahasa
- Terjemahan dalam direktori `/translations/<kod-bahasa>/`
- Aliran kerja GitHub Actions mengendalikan kemaskini terjemahan
- Fail sumber adalah dalam Bahasa Inggeris di akar repositori

### Struktur Pelajaran

Setiap pelajaran mengikuti corak konsisten:
1. Imej kecil video dengan pautan
2. Kandungan pelajaran bertulis (README.md)
3. Contoh kod dalam pelbagai rangka kerja
4. Objektif pembelajaran dan prasyarat
5. Sumber pembelajaran tambahan dipaut

### Penamaan Contoh Kod

Format: `<nombor-pelajaran>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Pelajaran 1, MAF Python
- `14-sequential.ipynb` - Pelajaran 14, corak maju MAF
- `16-python-agent-framework.ipynb` - Pelajaran 16, ejen sokongan pelanggan produksi
- `17-local-agent-foundry-local.ipynb` - Pelajaran 17, ejen tempatan dengan Foundry Local + Qwen

### Direktori Khas

- `translated_images/` - Imej dilokalkan untuk terjemahan
- `images/` - Imej asal untuk kandungan Bahasa Inggeris
- `.devcontainer/` - Konfigurasi bekas pembangunan VS Code
- `.github/` - Aliran kerja dan templat GitHub Actions

### Pergantungan

Pakej utama dari `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Sokongan protokol Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Perkhidmatan AI Azure
- `azure-identity` - Pengesahan Azure (AzureCliCredential)
- `azure-search-documents` - Integrasi Azure AI Search
- `mcp[cli]` - Sokongan Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->