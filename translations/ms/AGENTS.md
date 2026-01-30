# AGENTS.md

## Gambaran Projek

Repositori ini mengandungi "AI Agents for Beginners" - kursus pendidikan yang komprehensif mengajar segala yang diperlukan untuk membina AI Agents. Kursus ini terdiri daripada lebih 15 pelajaran yang merangkumi asas, corak reka bentuk, rangka kerja, dan penerapan AI agents dalam pengeluaran.

**Teknologi Utama:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- Rangka Kerja AI: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Perkhidmatan Azure AI: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (tier percuma tersedia)

**Senibina:**
- Struktur berdasarkan pelajaran (direktori 00-15+)
- Setiap pelajaran mengandungi: dokumentasi README, contoh kod (Jupyter notebooks), dan imej
- Sokongan pelbagai bahasa melalui sistem terjemahan automatik
- Pilihan rangka kerja pelbagai untuk setiap pelajaran (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Perintah Persediaan

### Prasyarat
- Python 3.12 atau lebih tinggi
- Akaun GitHub (untuk GitHub Models - tier percuma)
- Langganan Azure (pilihan, untuk perkhidmatan Azure AI)

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

Untuk **GitHub Models (Percuma)**:
- `GITHUB_TOKEN` - Token akses peribadi dari GitHub

Untuk **Perkhidmatan Azure AI** (pilihan):
- `PROJECT_ENDPOINT` - Endpoint projek Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Kunci API Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Nama penerapan untuk model chat
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Nama penerapan untuk embeddings
- Konfigurasi Azure tambahan seperti yang ditunjukkan dalam `.env.example`

## Aliran Kerja Pembangunan

### Menjalankan Jupyter Notebooks

Setiap pelajaran mengandungi beberapa Jupyter notebooks untuk rangka kerja yang berbeza:

1. **Mulakan Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigasi ke direktori pelajaran** (contoh: `01-intro-to-ai-agents/code_samples/`)

3. **Buka dan jalankan notebooks:**
   - `*-semantic-kernel.ipynb` - Menggunakan rangka kerja Semantic Kernel
   - `*-autogen.ipynb` - Menggunakan rangka kerja AutoGen
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Menggunakan Azure AI Agent Service

### Bekerja dengan Rangka Kerja Berbeza

**Semantic Kernel + GitHub Models:**
- Tier percuma tersedia dengan akaun GitHub
- Bagus untuk pembelajaran dan eksperimen
- Corak fail: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Tier percuma tersedia dengan akaun GitHub
- Keupayaan orkestrasi multi-agent
- Corak fail: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Rangka kerja terkini dari Microsoft
- Tersedia dalam Python dan .NET
- Corak fail: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Memerlukan langganan Azure
- Ciri-ciri sedia untuk pengeluaran
- Corak fail: `*-azureaiagent.ipynb`

## Arahan Pengujian

Ini adalah repositori pendidikan dengan kod contoh dan bukan kod pengeluaran dengan ujian automatik. Untuk mengesahkan persediaan dan perubahan anda:

### Pengujian Manual

1. **Uji persekitaran Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Uji pelaksanaan notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Sahkan pembolehubah persekitaran:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Menjalankan Notebook Individu

Buka notebook dalam Jupyter dan jalankan sel secara berurutan. Setiap notebook adalah berdiri sendiri dan termasuk:
- Pernyataan import
- Pemuatan konfigurasi
- Pelaksanaan contoh agent
- Output yang dijangka dalam sel markdown

## Gaya Kod

### Konvensyen Python

- **Versi Python**: 3.12+
- **Gaya Kod**: Ikuti konvensyen Python PEP 8 standard
- **Notebooks**: Gunakan sel markdown yang jelas untuk menerangkan konsep
- **Imports**: Kumpulkan mengikut pustaka standard, pihak ketiga, dan import tempatan

### Konvensyen Jupyter Notebook

- Sertakan sel markdown deskriptif sebelum sel kod
- Tambahkan contoh output dalam notebook untuk rujukan
- Gunakan nama pembolehubah yang jelas yang sepadan dengan konsep pelajaran
- Kekalkan susunan pelaksanaan notebook secara linear (sel 1 → 2 → 3...)

### Organisasi Fail

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

## Pembinaan dan Penerapan

### Membina Dokumentasi

Repositori ini menggunakan Markdown untuk dokumentasi:
- Fail README.md dalam setiap folder pelajaran
- README.md utama di akar repositori
- Sistem terjemahan automatik melalui GitHub Actions

### Pipeline CI/CD

Terletak dalam `.github/workflows/`:

1. **co-op-translator.yml** - Terjemahan automatik ke lebih 50 bahasa
2. **welcome-issue.yml** - Menyambut pencipta isu baru
3. **welcome-pr.yml** - Menyambut penyumbang pull request baru

### Penerapan

Ini adalah repositori pendidikan - tiada proses penerapan. Pengguna:
1. Fork atau clone repositori
2. Jalankan notebook secara tempatan atau dalam GitHub Codespaces
3. Belajar dengan mengubah dan bereksperimen dengan contoh

## Garis Panduan Pull Request

### Sebelum Menghantar

1. **Uji perubahan anda:**
   - Jalankan notebook yang terjejas sepenuhnya
   - Sahkan semua sel dilaksanakan tanpa ralat
   - Periksa bahawa output adalah sesuai

2. **Kemas kini dokumentasi:**
   - Kemas kini README.md jika menambah konsep baru
   - Tambahkan komen dalam notebook untuk kod yang kompleks
   - Pastikan sel markdown menerangkan tujuan

3. **Perubahan fail:**
   - Elakkan komit fail `.env` (gunakan `.env.example`)
   - Jangan komit direktori `venv/` atau `__pycache__/`
   - Kekalkan output notebook apabila ia menunjukkan konsep
   - Buang fail sementara dan notebook sandaran (`*-backup.ipynb`)

### Format Tajuk PR

Gunakan tajuk yang deskriptif:
- `[Lesson-XX] Tambah contoh baru untuk <konsep>`
- `[Fix] Betulkan typo dalam README pelajaran-XX`
- `[Update] Perbaiki contoh kod dalam pelajaran-XX`
- `[Docs] Kemas kini arahan persediaan`

### Pemeriksaan Diperlukan

- Notebook harus dilaksanakan tanpa ralat
- Fail README harus jelas dan tepat
- Ikuti corak kod sedia ada dalam repositori
- Kekalkan konsistensi dengan pelajaran lain

## Nota Tambahan

### Masalah Umum

1. **Ketidakpadanan versi Python:**
   - Pastikan Python 3.12+ digunakan
   - Beberapa pakej mungkin tidak berfungsi dengan versi lama
   - Gunakan `python3 -m venv` untuk menentukan versi Python secara eksplisit

2. **Pembolehubah persekitaran:**
   - Sentiasa buat `.env` dari `.env.example`
   - Jangan komit fail `.env` (ia dalam `.gitignore`)
   - Token GitHub memerlukan kebenaran yang sesuai

3. **Konflik pakej:**
   - Gunakan persekitaran maya yang baru
   - Pasang dari `requirements.txt` dan bukan pakej individu
   - Beberapa notebook mungkin memerlukan pakej tambahan yang disebutkan dalam sel markdown mereka

4. **Perkhidmatan Azure:**
   - Perkhidmatan Azure AI memerlukan langganan aktif
   - Beberapa ciri adalah khusus untuk wilayah
   - Had tier percuma terpakai untuk GitHub Models

### Laluan Pembelajaran

Kemajuan yang disyorkan melalui pelajaran:
1. **00-course-setup** - Mulakan di sini untuk persediaan persekitaran
2. **01-intro-to-ai-agents** - Fahami asas AI agents
3. **02-explore-agentic-frameworks** - Pelajari tentang rangka kerja yang berbeza
4. **03-agentic-design-patterns** - Corak reka bentuk teras
5. Teruskan melalui pelajaran bernombor secara berurutan

### Pemilihan Rangka Kerja

Pilih rangka kerja berdasarkan matlamat anda:
- **Pembelajaran/Prototip**: Semantic Kernel + GitHub Models (percuma)
- **Sistem multi-agent**: AutoGen
- **Ciri terkini**: Microsoft Agent Framework (MAF)
- **Penerapan pengeluaran**: Azure AI Agent Service

### Mendapatkan Bantuan

- Sertai [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Semak fail README pelajaran untuk panduan khusus
- Periksa [README.md](./README.md) utama untuk gambaran kursus
- Rujuk [Course Setup](./00-course-setup/README.md) untuk arahan persediaan terperinci

### Menyumbang

Ini adalah projek pendidikan terbuka. Sumbangan dialu-alukan:
- Perbaiki contoh kod
- Betulkan typo atau kesilapan
- Tambahkan komen penjelasan
- Cadangkan topik pelajaran baru
- Terjemahkan ke bahasa tambahan

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk keperluan semasa.

## Konteks Khusus Projek

### Sokongan Pelbagai Bahasa

Repositori ini menggunakan sistem terjemahan automatik:
- Lebih 50 bahasa disokong
- Terjemahan dalam direktori `/translations/<lang-code>/`
- Aliran kerja GitHub Actions mengendalikan kemas kini terjemahan
- Fail sumber dalam bahasa Inggeris di akar repositori

### Struktur Pelajaran

Setiap pelajaran mengikuti pola yang konsisten:
1. Thumbnail video dengan pautan
2. Kandungan pelajaran bertulis (README.md)
3. Contoh kod dalam pelbagai rangka kerja
4. Objektif pembelajaran dan prasyarat
5. Sumber pembelajaran tambahan yang dipautkan

### Penamaan Contoh Kod

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Pelajaran 4, Semantic Kernel
- `07-autogen.ipynb` - Pelajaran 7, AutoGen
- `14-python-agent-framework.ipynb` - Pelajaran 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Pelajaran 14, MAF .NET

### Direktori Khas

- `translated_images/` - Imej yang diterjemahkan untuk terjemahan
- `images/` - Imej asal untuk kandungan bahasa Inggeris
- `.devcontainer/` - Konfigurasi kontena pembangunan VS Code
- `.github/` - Aliran kerja dan templat GitHub Actions

### Kebergantungan

Pakej utama dari `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Rangka kerja AutoGen
- `semantic-kernel` - Rangka kerja Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Perkhidmatan Azure AI
- `azure-search-documents` - Integrasi Azure AI Search
- `chromadb` - Pangkalan data vektor untuk contoh RAG
- `chainlit` - Rangka kerja UI chat
- `browser_use` - Automasi pelayar untuk agents
- `mcp[cli]` - Sokongan Model Context Protocol
- `mem0ai` - Pengurusan memori untuk agents

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.