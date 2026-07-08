# AGENTS.md

## Gambaran Projek

Repositori ini mengandungi "Ejen AI untuk Pemula" - kursus pendidikan menyeluruh yang mengajar segala yang diperlukan untuk membina Ejen AI. Kursus ini terdiri daripada 18 pelajaran yang merangkumi asas, corak reka bentuk, rangka kerja, dan penempatan pengeluaran ejen AI.

**Teknologi Utama:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- Rangka Kerja AI: Microsoft Agent Framework (MAF)
- Perkhidmatan AI Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Seni Bina:**
- Struktur berasaskan pelajaran (direktori 00-15+)
- Setiap pelajaran mengandungi: dokumentasi README, contoh kod (notebook Jupyter), dan imej
- Sokongan pelbagai bahasa melalui sistem terjemahan automatik
- Satu notebook Python bagi setiap pelajaran menggunakan Microsoft Agent Framework

## Perintah Penetapan

### Prasyarat
- Python 3.12 atau lebih tinggi
- Langganan Azure (untuk Microsoft Foundry)
- Azure CLI dipasang dan diautentikasi (`az login`)

### Penetapan Awal

1. **Klona atau buat forkan repositori:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ATAU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Buat dan aktifkan persekitaran maya Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Pada Windows: venv\Scripts\activate
   ```

3. **Pasang kebergantungan:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Tetapkan pembolehubah persekitaran:**
   ```bash
   cp .env.example .env
   # Edit .env dengan kekunci API dan titik akhir anda
   ```

### Pembolehubah Persekitaran yang Diperlukan

Untuk **Microsoft Foundry** (Diperlukan):
- `AZURE_AI_PROJECT_ENDPOINT` - titik hujung projek Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nama penempatan model (contohnya, gpt-4o)

Untuk **Azure AI Search** (Pelajaran 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - titik hujung Azure AI Search
- `AZURE_SEARCH_API_KEY` - kunci API Azure AI Search

Pengesahan: Jalankan `az login` sebelum menjalankan notebook (menggunakan `AzureCliCredential`).

## Aliran Kerja Pembangunan

### Menjalankan Jupyter Notebooks

Setiap pelajaran mengandungi pelbagai notebook Jupyter untuk rangka kerja yang berbeza:

1. **Mula Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigasi ke direktori pelajaran** (contohnya, `01-intro-to-ai-agents/code_samples/`)

3. **Buka dan jalankan notebook:**
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)

### Bekerja dengan Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Memerlukan langganan Azure
- Menggunakan `FoundryChatClient` untuk Agent Service V2 (ejen kelihatan dalam portal Foundry)
- Sedia untuk pengeluaran dengan pemerhatian terbina dalam
- Corak fail: `*-python-agent-framework.ipynb`

## Arahan Pengujian

Ini adalah repositori pendidikan dengan contoh kod dan bukannya kod pengeluaran dengan ujian automatik. Untuk mengesahkan penetapan dan perubahan anda:

### Ujian Manual

1. **Uji persekitaran Python:**
   ```bash
   python --version  # Sepatutnya 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Uji pelaksanaan notebook:**
   ```bash
   # Tukar buku catatan ke skrip dan jalankan (menguji import)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Sahkan pembolehubah persekitaran:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Menjalankan Notebook Individu

Buka notebook dalam Jupyter dan jalankan sel secara berurutan. Setiap notebook berdikari dan termasuk:
- Pernyataan import
- Memuatkan konfigurasi
- Pelaksanaan contoh ejen
- Output dijangka dalam sel markdown

## Gaya Kod

### Konvensyen Python

- **Versi Python**: 3.12+
- **Gaya Kod**: Ikuti konvensyen PEP 8 Python yang standard
- **Notebook**: Gunakan sel markdown yang jelas untuk menerangkan konsep
- **Import**: Kumpulkan mengikut perpustakaan standard, pihak ketiga, import tempatan

### Konvensyen Jupyter Notebook

- Sertakan sel markdown yang deskriptif sebelum sel kod
- Tambah contoh output dalam notebook untuk rujukan
- Gunakan nama pembolehubah yang jelas yang sepadan dengan konsep pelajaran
- Kekalkan susunan pelaksanaan notebook secara linear (sel 1 → 2 → 3...)

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

## Pembinaan dan Penempatan

### Membina Dokumentasi

Repositori ini menggunakan Markdown untuk dokumentasi:
- Fail README.md dalam setiap folder pelajaran
- README.md utama di akar repositori
- Sistem terjemahan automatik melalui GitHub Actions

### Salur CI/CD

Terletak di `.github/workflows/`:

1. **co-op-translator.yml** - Terjemahan automatik ke lebih 50 bahasa
2. **welcome-issue.yml** - Menyambut pencipta isu baru
3. **welcome-pr.yml** - Menyambut penyumbang permintaan tarik baru

### Penempatan

Ini adalah repositori pendidikan - tiada proses penempatan. Pengguna:
1. Buat forkan atau klon repositori
2. Jalankan notebook secara tempatan atau dalam GitHub Codespaces
3. Belajar dengan mengubah suai dan bereksperimen dengan contoh

## Garis Panduan Pull Request

### Sebelum Mengemukakan

1. **Uji perubahan anda:**
   - Jalankan notebook terjejas sepenuhnya
   - Pastikan semua sel berjaya dilaksanakan tanpa ralat
   - Semak output adalah sesuai

2. **Kemaskini dokumentasi:**
   - Kemaskini README.md jika menambah konsep baru
   - Tambah komen dalam notebook untuk kod yang kompleks
   - Pastikan sel markdown menerangkan tujuan

3. **Perubahan fail:**
   - Elakkan meluluskan fail `.env` (guna `.env.example`)
   - Jangan meluluskan direktori `venv/` atau `__pycache__/`
   - Kekalkan output notebook apabila ia menunjukan konsep
   - Keluarkan fail sementara dan notebook sandaran (`*-backup.ipynb`)

### Format Tajuk PR

Gunakan tajuk deskriptif:
- `[Lesson-XX] Tambah contoh baru untuk <konsep>`
- `[Fix] Betulkan typo dalam README pelajaran-XX`
- `[Update] Perbaiki contoh kod dalam pelajaran-XX`
- `[Docs] Kemaskini arahan penetapan`

### Pemeriksaan Diperlukan

- Notebook harus dijalankan tanpa ralat
- Fail README harus jelas dan tepat
- Ikut corak kod sedia ada dalam repositori
- Kekalkan konsistensi dengan pelajaran lain

## Nota Tambahan

### Perkara Lazim yang Perlu Diambil Perhatian

1. **Ketidakpadanan versi Python:**
   - Pastikan menggunakan Python 3.12+
   - Sesetengah pakej mungkin tidak berfungsi dengan versi lama
   - Gunakan `python3 -m venv` untuk menentukan versi Python secara eksplisit

2. **Pembolehubah persekitaran:**
   - Sentiasa buat `.env` dari `.env.example`
   - Jangan luluskan fail `.env` (termasuk dalam `.gitignore`)
   - Log masuk dengan `az login` untuk pengesahan Entra ID tanpa kunci

3. **Konflik pakej:**
   - Gunakan persekitaran maya yang baru
   - Pasang dari `requirements.txt` dan bukan pakej individu
   - Sesetengah notebook mungkin memerlukan pakej tambahan yang disebut dalam sel markdown mereka

4. **Perkhidmatan Azure:**
   - Perkhidmatan AI Azure memerlukan langganan aktif
   - Sesetengah ciri khusus untuk kawasan tertentu
   - Pastikan penempatan model Azure OpenAI anda menyokong API Respons

### Laluan Pembelajaran

Cadangan urutan pelajaran:
1. **00-course-setup** - Mulakan di sini untuk penetapan persekitaran
2. **01-intro-to-ai-agents** - Fahami asas ejen AI
3. **02-explore-agentic-frameworks** - Pelajari tentang pelbagai rangka kerja
4. **03-agentic-design-patterns** - Corak reka bentuk utama
5. Teruskan melalui pelajaran bernombor secara berurutan

### Pemilihan Rangka Kerja

Pilih rangka kerja berdasarkan matlamat anda:
- **Semua pelajaran**: Microsoft Agent Framework (MAF) dengan `FoundryChatClient`
- **Ejen mendaftar di sisi pelayan** dalam Microsoft Foundry Agent Service V2 dan kelihatan dalam portal Foundry

### Mendapatkan Bantuan

- Sertai [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Semak fail README pelajaran untuk panduan khusus
- Rujuk [README.md](./README.md) utama untuk gambaran kursus
- Rujuk [Course Setup](./00-course-setup/README.md) untuk arahan penetapan terperinci

### Menyumbang

Ini adalah projek pendidikan terbuka. Sumbangan dialu-alukan:
- Perbaiki contoh kod
- Betulkan typo atau ralat
- Tambah komen penjelas
- Cadangkan topik pelajaran baru
- Terjemah ke bahasa tambahan

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk keperluan semasa.

## Konteks Khusus Projek

### Sokongan Pelbagai Bahasa

Repositori ini menggunakan sistem terjemahan automatik:
- Menyokong lebih 50 bahasa
- Terjemahan dalam direktori `/translations/<kod-bahasa>/`
- Aliran kerja GitHub Actions mengurus kemaskini terjemahan
- Fail sumber dalam bahasa Inggeris di akar repositori

### Struktur Pelajaran

Setiap pelajaran mengikuti corak yang konsisten:
1. Thumbnail video dengan pautan
2. Kandungan pelajaran bertulis (README.md)
3. Contoh kod dalam pelbagai rangka kerja
4. Objektif pembelajaran dan prasyarat
5. Sumber pembelajaran tambahan pautan

### Penamaan Contoh Kod

Format: `<nombor-pelajaran>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Pelajaran 1, MAF Python
- `14-sequential.ipynb` - Pelajaran 14, corak lanjutan MAF

### Direktori Khusus

- `translated_images/` - Imej diterjemah untuk terjemahan
- `images/` - Imej asal untuk kandungan Inggeris
- `.devcontainer/` - Konfigurasi bekas pembangunan VS Code
- `.github/` - Aliran kerja dan templat GitHub Actions

### Kebergantungan

Pakej utama dari `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Sokongan protokol Agent-ke-Agent
- `azure-ai-inference`, `azure-ai-projects` - Perkhidmatan AI Azure
- `azure-identity` - Pengesahan Azure (AzureCliCredential)
- `azure-search-documents` - Integrasi Azure AI Search
- `mcp[cli]` - Sokongan Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->