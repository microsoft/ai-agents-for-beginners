# AGENTS.md

## Project Overview

Repositori ini mengandungi "AI Agents for Beginners" - sebuah kursus pendidikan komprehensif yang mengajar segala yang diperlukan untuk membina Ejen AI. Kursus ini mengandungi 15+ pelajaran yang merangkumi asas, corak reka bentuk, rangka kerja, dan penyebaran pengeluaran ejen AI.

**Key Technologies:**
- Python 3.12+
- Jupyter Notebooks untuk pembelajaran interaktif
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architecture:**
- Struktur berasaskan pelajaran (direktori 00-15+)
- Setiap pelajaran mengandungi: dokumentasi README, contoh kod (Jupyter notebooks), dan imej
- Sokongan berbilang bahasa melalui sistem terjemahan automatik
- Satu notebook Python setiap pelajaran menggunakan Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 atau lebih tinggi
- Azure subscription (untuk Azure AI Foundry)
- Azure CLI dipasang dan diautentikasi (`az login`)

### Initial Setup

1. **Clone or fork the repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ATAU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Create and activate Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Di Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Sunting .env dengan kunci API dan titik akhir anda
   ```

### Required Environment Variables

For **Azure AI Foundry** (Diperlukan):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint projek Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nama deployment model (contoh, gpt-4o)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Jalankan `az login` sebelum menjalankan notebook (menggunakan `AzureCliCredential`).

## Development Workflow

### Running Jupyter Notebooks

Setiap pelajaran mengandungi berbilang Jupyter notebooks untuk rangka kerja yang berbeza:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate to a lesson directory** (contoh, `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Memerlukan langganan Azure
- Menggunakan `AzureAIProjectAgentProvider` untuk Agent Service V2 (ejen terlihat dalam portal Foundry)
- Sedia untuk pengeluaran dengan kebolehlihatan terbina dalam
- Corak fail: `*-python-agent-framework.ipynb`

## Testing Instructions

Ini adalah repositori pendidikan dengan kod contoh dan bukannya kod pengeluaran dengan ujian automatik. Untuk mengesahkan persediaan dan perubahan anda:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # Sepatutnya 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # Tukar notebook kepada skrip dan jalankan (menguji import)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Running Individual Notebooks

Buka notebook dalam Jupyter dan jalankan sel secara berurutan. Setiap notebook berdiri sendiri dan mengandungi:
- Pernyataan import
- Pemuatan konfigurasi
- Implementasi contoh ejen
- Output yang dijangka dalam sel markdown

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: Ikuti konvensyen Python PEP 8 piawai
- **Notebooks**: Gunakan sel markdown yang jelas untuk menerangkan konsep
- **Imports**: Kumpulkan mengikut standard library, pihak ketiga, import tempatan

### Jupyter Notebook Conventions

- Sertakan sel markdown deskriptif sebelum sel kod
- Tambah contoh output dalam notebook untuk rujukan
- Gunakan nama pembolehubah yang jelas dan sepadan dengan konsep pelajaran
- Kekalkan susunan pelaksanaan notebook secara linear (sel 1 → 2 → 3...)

### File Organization

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Build and Deployment

### Building Documentation

Repositori ini menggunakan Markdown untuk dokumentasi:
- Fail README.md dalam setiap folder pelajaran
- Main README.md at repository root
- Sistem terjemahan automatik melalui GitHub Actions

### CI/CD Pipeline

Terletak di `.github/workflows/`:

1. **co-op-translator.yml** - Terjemahan automatik ke 50+ bahasa
2. **welcome-issue.yml** - Menyambut pencipta isu baru
3. **welcome-pr.yml** - Menyambut penyumbang pull request baru

### Deployment

Ini adalah repositori pendidikan - tiada proses penyebaran. Pengguna:
1. Fork atau clone repositori
2. Jalankan notebook secara tempatan atau dalam GitHub Codespaces
3. Belajar dengan memodifikasi dan mencuba contoh

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Jalankan notebook yang terjejas sepenuhnya
   - Sahkan semua sel berjalan tanpa ralat
   - Semak bahawa output adalah sesuai

2. **Documentation updates:**
   - Kemas kini README.md jika menambah konsep baru
   - Tambah komen dalam notebook untuk kod yang kompleks
   - Pastikan sel markdown menerangkan tujuan

3. **File changes:**
   - Elakkan membuat commit fail `.env` (gunakan `.env.example`)
   - Jangan commit `venv/` atau `__pycache__/` direktori
   - Simpan output notebook apabila ia menunjukkan konsep
   - Alih keluar fail sementara dan notebook sandaran (`*-backup.ipynb`)

### PR Title Format

Use descriptive titles:
- `[Lesson-XX] Tambah contoh baru untuk <concept>`
- `[Fix] Betulkan typo dalam lesson-XX README`
- `[Update] Tingkatkan contoh kod dalam lesson-XX`
- `[Docs] Kemas kini arahan persediaan`

### Required Checks

- Notebook harus dijalankan tanpa ralat
- Fail README harus jelas dan tepat
- Ikuti corak kod sedia ada dalam repositori
- Kekalkan konsistensi dengan pelajaran lain

## Additional Notes

### Perkara Lazim

1. **Ketidakpadanan versi Python:**
   - Pastikan Python 3.12+ digunakan
   - Sesetengah pakej mungkin tidak berfungsi dengan versi yang lebih lama
   - Gunakan `python3 -m venv` untuk menentukan versi Python secara eksplisit

2. **Pembolehubah persekitaran:**
   - Sentiasa buat `.env` daripada `.env.example`
   - Jangan commit fail `.env` (ia ada dalam `.gitignore`)
   - Token GitHub memerlukan kebenaran yang sesuai

3. **Konflik pakej:**
   - Gunakan persekitaran maya yang baru
   - Pasang daripada `requirements.txt` daripada pakej individu
   - Sesetengah notebook mungkin memerlukan pakej tambahan yang disebut dalam sel markdown mereka

4. **Perkhidmatan Azure:**
   - Perkhidmatan Azure AI memerlukan langganan aktif
   - Sesetengah ciri adalah khusus untuk rantau tertentu
   - Had tier percuma terpakai untuk GitHub Models

### Learning Path

Perkembangan disyorkan melalui pelajaran:
1. **00-course-setup** - Mula di sini untuk persediaan persekitaran
2. **01-intro-to-ai-agents** - Fahami asas ejen AI
3. **02-explore-agentic-frameworks** - Pelajari tentang pelbagai rangka kerja
4. **03-agentic-design-patterns** - Corak reka bentuk teras
5. Teruskan melalui pelajaran bernombor secara berurutan

### Framework Selection

Pilih rangka kerja berdasarkan matlamat anda:
- **Semua pelajaran**: Microsoft Agent Framework (MAF) dengan `AzureAIProjectAgentProvider`
- **Ejen didaftarkan di sisi pelayan** dalam Azure AI Foundry Agent Service V2 dan terlihat dalam portal Foundry

### Getting Help

- Sertai [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Semak fail README pelajaran untuk panduan khusus
- Semak the main [README.md](./README.md) untuk ikhtisar kursus
- Rujuk [Persediaan Kursus](./00-course-setup/README.md) untuk arahan persediaan terperinci

### Contributing

Ini adalah projek pendidikan terbuka. Sumbangan dialu-alukan:
- Perbaiki contoh kod
- Betulkan kesilapan ejaan atau ralat
- Tambah komen yang menjelaskan
- Cadangkan topik pelajaran baru
- Terjemahkan ke bahasa tambahan

Lihat [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) untuk keperluan semasa.

## Project-Specific Context

### Multi-Language Support

Repositori ini menggunakan sistem terjemahan automatik:
- Sokongan 50+ bahasa
- Terjemahan dalam direktori `/translations/<lang-code>/`
- Aliran kerja GitHub Actions mengendalikan kemas kini terjemahan
- Fail sumber adalah dalam Bahasa Inggeris di akar repositori

### Lesson Structure

Setiap pelajaran mengikuti pola yang konsisten:
1. Imej kecil video dengan pautan
2. Kandungan pelajaran bertulis (README.md)
3. Contoh kod dalam pelbagai rangka kerja
4. Objektif pembelajaran dan prasyarat
5. Sumber pembelajaran tambahan yang dipautkan

### Code Sample Naming

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Pelajaran 1, MAF Python
- `14-sequential.ipynb` - Pelajaran 14, corak maju MAF

### Special Directories

- `translated_images/` - Imej yang dilokalkan untuk terjemahan
- `images/` - Imej asal untuk kandungan Bahasa Inggeris
- `.devcontainer/` - VS Code development container configuration
- `.github/` - GitHub Actions workflows and templates

### Dependencies

Key packages from `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Sokongan protokol Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Perkhidmatan Azure AI
- `azure-identity` - Autentikasi Azure (AzureCliCredential)
- `azure-search-documents` - Integrasi Azure AI Search
- `mcp[cli]` - Sokongan Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat yang penting, adalah disyorkan agar penterjemahan profesional oleh manusia digunakan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->