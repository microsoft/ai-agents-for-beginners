# AGENTS.md

## Project Overview

This repository contains "AI Agents for Beginners" - a comprehensive educational course teaching everything needed to build AI Agents. The course consists of 15+ lessons covering fundamentals, design patterns, frameworks, and production deployment of AI agents.

**Key Technologies:**
- Python 3.12+
- Jupyter Notebooks for interactive learning
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architecture:**
- Lesson-based structure (00-15+ directories)
- Each lesson contains: README documentation, code samples (Jupyter notebooks), and images
- Multi-language support via automated translation system
- One Python notebook per lesson using Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 or higher
- Azure subscription (for Azure AI Foundry)
- Azure CLI installed and authenticated (`az login`)

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

For **Azure AI Foundry** (Required):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (contohnya, gpt-4o)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Jalankan `az login` sebelum menjalankan notebook (menggunakan `AzureCliCredential`).

## Development Workflow

### Running Jupyter Notebooks

Each lesson contains multiple Jupyter notebooks for different frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate to a lesson directory** (e.g., `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Menggunakan Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Requires Azure subscription
- Uses `AzureAIProjectAgentProvider` for Agent Service V2 (agents visible in Foundry portal)
- Production-ready with built-in observability
- File pattern: `*-python-agent-framework.ipynb`

## Testing Instructions

This is an educational repository with example code rather than production code with automated tests. To verify your setup and changes:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # Seharusnya 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # Tukar notebook menjadi skrip dan jalankan (menguji import)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Running Individual Notebooks

Open notebooks in Jupyter and execute cells sequentially. Each notebook is self-contained and includes:
- Import statements
- Configuration loading
- Example agent implementations
- Expected outputs in markdown cells

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: Ikuti konvensi Python standard PEP 8
- **Notebooks**: Gunakan sel markdown yang jelas untuk menerangkan konsep
- **Imports**: Kumpulkan mengikut standard library, pihak ketiga, import tempatan

### Jupyter Notebook Conventions

- Sertakan sel markdown yang menerangkan sebelum sel kod
- Tambah contoh output dalam notebook untuk rujukan
- Gunakan nama pembolehubah yang jelas yang sepadan dengan konsep pelajaran
- Pastikan susunan pelaksanaan notebook linear (sel 1 → 2 → 3...)

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

This repository uses Markdown for documentation:
- README.md files in each lesson folder
- Main README.md at repository root
- Automated translation system via GitHub Actions

### CI/CD Pipeline

Located in `.github/workflows/`:

1. **co-op-translator.yml** - Automatic translation to 50+ languages
2. **welcome-issue.yml** - Welcomes new issue creators
3. **welcome-pr.yml** - Welcomes new pull request contributors

### Deployment

This is an educational repository - no deployment process. Users:
1. Fork or clone the repository
2. Run notebooks locally or in GitHub Codespaces
3. Learn by modifying and experimenting with examples

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Run affected notebooks completely
   - Verify all cells execute without errors
   - Check that outputs are appropriate

2. **Documentation updates:**
   - Update README.md if adding new concepts
   - Add comments in notebooks for complex code
   - Ensure markdown cells explain the purpose

3. **File changes:**
   - Avoid committing `.env` files (use `.env.example`)
   - Don't commit `venv/` or `__pycache__/` directories
   - Keep notebook outputs when they demonstrate concepts
   - Remove temporary files and backup notebooks (`*-backup.ipynb`)

### PR Title Format

Use descriptive titles:
- `[Lesson-XX] Tambah contoh baru untuk <concept>`
- `[Fix] Betulkan typo dalam lesson-XX README`
- `[Update] Tingkatkan contoh kod dalam lesson-XX`
- `[Docs] Kemas kini arahan persediaan`

### Required Checks

- Notebooks should execute without errors
- README files should be clear and accurate
- Follow existing code patterns in the repository
- Maintain consistency with other lessons

## Additional Notes

### Common Gotchas

1. **Python version mismatch:**
   - Pastikan Python 3.12+ digunakan
   - Sesetengah pakej mungkin tidak berfungsi dengan versi lama
   - Gunakan `python3 -m venv` untuk menentukan versi Python dengan jelas

2. **Environment variables:**
   - Sentiasa cipta `.env` dari `.env.example`
   - Jangan commit fail `.env` (ia disenaraikan dalam `.gitignore`)
   - Token GitHub memerlukan kebenaran yang sesuai

3. **Package conflicts:**
   - Gunakan persekitaran maya yang baru
   - Pasang dari `requirements.txt` dan bukannya pakej individu
   - Sesetengah notebook mungkin memerlukan pakej tambahan yang dinyatakan dalam sel markdown mereka

4. **Azure services:**
   - Perkhidmatan Azure AI memerlukan langganan aktif
   - Sesetengah ciri adalah spesifik kepada rantau
   - Had tier percuma terpakai kepada GitHub Models

### Learning Path

Recommended progression through lessons:
1. **00-course-setup** - Start here for environment setup
2. **01-intro-to-ai-agents** - Understand AI agent fundamentals
3. **02-explore-agentic-frameworks** - Learn about different frameworks
4. **03-agentic-design-patterns** - Core design patterns
5. Continue through numbered lessons sequentially

### Framework Selection

Choose framework based on your goals:
- **All lessons**: Microsoft Agent Framework (MAF) with `AzureAIProjectAgentProvider`
- **Agents register server-side** in Azure AI Foundry Agent Service V2 and are visible in the Foundry portal

### Getting Help

- Sertai [Komuniti Discord Microsoft Foundry](https://aka.ms/ai-agents/discord)
- Semak fail README pelajaran untuk panduan khusus
- Check the main [README.md](./README.md) for course overview
- Rujuk [Persediaan Kursus](./00-course-setup/README.md) untuk arahan persediaan terperinci

### Contributing

This is an open educational project. Contributions welcome:
- Improve code examples
- Fix typos or errors
- Add clarifying comments
- Suggest new lesson topics
- Translate to additional languages

See [Isu GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) for current needs.

## Project-Specific Context

### Multi-Language Support

This repository uses an automated translation system:
- 50+ languages supported
- Translations in `/translations/<lang-code>/` directories
- GitHub Actions workflow handles translation updates
- Source files are in English at repository root

### Lesson Structure

Each lesson follows a consistent pattern:
1. Video thumbnail with link
2. Written lesson content (README.md)
3. Code samples in multiple frameworks
4. Learning objectives and prerequisites
5. Extra learning resources linked

### Code Sample Naming

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lesson 1, MAF Python
- `14-sequential.ipynb` - Lesson 14, MAF advanced patterns

### Special Directories

- `translated_images/` - Localized images for translations
- `images/` - Original images for English content
- `.devcontainer/` - VS Code development container configuration
- `.github/` - GitHub Actions workflows and templates

### Dependencies

Key packages from `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol support
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure authentication (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integration
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI Co-op Translator (https://github.com/Azure/co-op-translator). Walaupun kami berusaha mencapai ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, disyorkan mendapatkan terjemahan profesional oleh penterjemah manusia. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->