<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5f54aa3f419865e5d58bcfddb1d3198",
  "translation_date": "2025-11-11T11:52:22+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pcm"
}
-->
# AGENTS.md

## Project Overview

Dis repository get "AI Agents for Beginners" - na full educational course wey dey teach wetin you need to sabi to build AI Agents. Di course get 15+ lessons wey cover fundamentals, design patterns, frameworks, and how to deploy AI agents for production.

**Key Technologies:**
- Python 3.12+
- Jupyter Notebooks for interactive learning
- AI Frameworks: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI Services: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (free tier dey)

**Architecture:**
- Lesson-based structure (00-15+ directories)
- Each lesson get: README documentation, code samples (Jupyter notebooks), and images
- Multi-language support dey through automated translation system
- Multiple framework options dey for each lesson (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Setup Commands

### Prerequisites
- Python 3.12 or higher
- GitHub account (for GitHub Models - free tier)
- Azure subscription (optional, for Azure AI services)

### Initial Setup

1. **Clone or fork di repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Create and activate Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Required Environment Variables

For **GitHub Models (Free)**:
- `GITHUB_TOKEN` - Personal access token from GitHub

For **Azure AI Services** (optional):
- `PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API key
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Deployment name for chat model
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Deployment name for embeddings
- Additional Azure configuration dey for `.env.example`

## Development Workflow

### Running Jupyter Notebooks

Each lesson get plenty Jupyter notebooks for different frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate go one lesson directory** (e.g., `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-semantic-kernel.ipynb` - Use Semantic Kernel framework
   - `*-autogen.ipynb` - Use AutoGen framework
   - `*-python-agent-framework.ipynb` - Use Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Use Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Use Azure AI Agent Service

### Working with Different Frameworks

**Semantic Kernel + GitHub Models:**
- Free tier dey with GitHub account
- Good for learning and experimentation
- File pattern: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Free tier dey with GitHub account
- Multi-agent orchestration capabilities dey
- File pattern: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Latest framework from Microsoft
- Dey available for Python and .NET
- File pattern: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- E need Azure subscription
- Production-ready features dey
- File pattern: `*-azureaiagent.ipynb`

## Testing Instructions

Dis na educational repository with example code, e no be production code wey get automated tests. To check your setup and changes:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Test notebook execution:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Running Individual Notebooks

Open notebooks for Jupyter and run di cells one by one. Each notebook dey self-contained and e get:
- Import statements
- Configuration loading
- Example agent implementations
- Expected outputs for markdown cells

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: Follow standard Python PEP 8 conventions
- **Notebooks**: Use clear markdown cells to explain concepts
- **Imports**: Group by standard library, third-party, local imports

### Jupyter Notebook Conventions

- Put descriptive markdown cells before code cells
- Add output examples for notebooks for reference
- Use clear variable names wey match lesson concepts
- Keep notebook execution order linear (cell 1 → 2 → 3...)

### File Organization

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

## Build and Deployment

### Building Documentation

Dis repository dey use Markdown for documentation:
- README.md files dey for each lesson folder
- Main README.md dey for repository root
- Automated translation system dey through GitHub Actions

### CI/CD Pipeline

E dey for `.github/workflows/`:

1. **co-op-translator.yml** - Automatic translation to 50+ languages
2. **welcome-issue.yml** - E dey welcome new issue creators
3. **welcome-pr.yml** - E dey welcome new pull request contributors

### Deployment

Dis na educational repository - e no get deployment process. Users:
1. Fork or clone di repository
2. Run notebooks locally or for GitHub Codespaces
3. Learn by modifying and experimenting with examples

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Run di notebooks wey you change completely
   - Make sure say all cells dey run without errors
   - Check say di outputs dey correct

2. **Documentation updates:**
   - Update README.md if you dey add new concepts
   - Add comments for notebooks for complex code
   - Make sure markdown cells dey explain di purpose

3. **File changes:**
   - No commit `.env` files (use `.env.example`)
   - No commit `venv/` or `__pycache__/` directories
   - Keep notebook outputs if dem dey show concepts
   - Remove temporary files and backup notebooks (`*-backup.ipynb`)

### PR Title Format

Use descriptive titles:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo for lesson-XX README`
- `[Update] Improve code sample for lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- Notebooks suppose dey run without errors
- README files suppose dey clear and correct
- Follow di existing code patterns for di repository
- Maintain consistency with other lessons

## Additional Notes

### Common Gotchas

1. **Python version mismatch:**
   - Make sure say you dey use Python 3.12+
   - Some packages no go work with older versions
   - Use `python3 -m venv` to specify Python version well

2. **Environment variables:**
   - Always create `.env` from `.env.example`
   - No commit `.env` file (e dey for `.gitignore`)
   - GitHub token need correct permissions

3. **Package conflicts:**
   - Use fresh virtual environment
   - Install from `requirements.txt` instead of individual packages
   - Some notebooks fit need extra packages wey dem mention for markdown cells

4. **Azure services:**
   - Azure AI services need active subscription
   - Some features dey region-specific
   - Free tier limitations dey for GitHub Models

### Learning Path

Recommended progression through lessons:
1. **00-course-setup** - Start here to set up environment
2. **01-intro-to-ai-agents** - Understand AI agent fundamentals
3. **02-explore-agentic-frameworks** - Learn about different frameworks
4. **03-agentic-design-patterns** - Core design patterns
5. Continue through numbered lessons one by one

### Framework Selection

Choose framework based on wetin you wan achieve:
- **Learning/Prototyping**: Semantic Kernel + GitHub Models (free)
- **Multi-agent systems**: AutoGen
- **Latest features**: Microsoft Agent Framework (MAF)
- **Production deployment**: Azure AI Agent Service

### Getting Help

- Join di [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Check lesson README files for specific guidance
- Look di main [README.md](./README.md) for course overview
- Check [Course Setup](./00-course-setup/README.md) for detailed setup instructions

### Contributing

Dis na open educational project. Contributions dey welcome:
- Improve code examples
- Fix typos or errors
- Add clarifying comments
- Suggest new lesson topics
- Translate to more languages

Check [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for current needs.

## Project-Specific Context

### Multi-Language Support

Dis repository dey use automated translation system:
- 50+ languages dey supported
- Translations dey for `/translations/<lang-code>/` directories
- GitHub Actions workflow dey handle translation updates
- Source files dey for English for repository root

### Lesson Structure

Each lesson dey follow one consistent pattern:
1. Video thumbnail with link
2. Written lesson content (README.md)
3. Code samples for multiple frameworks
4. Learning objectives and prerequisites
5. Extra learning resources wey dem link

### Code Sample Naming

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Lesson 4, Semantic Kernel
- `07-autogen.ipynb` - Lesson 7, AutoGen
- `14-python-agent-framework.ipynb` - Lesson 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lesson 14, MAF .NET

### Special Directories

- `translated_images/` - Localized images for translations
- `images/` - Original images for English content
- `.devcontainer/` - VS Code development container configuration
- `.github/` - GitHub Actions workflows and templates

### Dependencies

Key packages from `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen framework
- `semantic-kernel` - Semantic Kernel framework
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-search-documents` - Azure AI Search integration
- `chromadb` - Vector database for RAG examples
- `chainlit` - Chat UI framework
- `browser_use` - Browser automation for agents
- `mcp[cli]` - Model Context Protocol support
- `mem0ai` - Memory management for agents

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even though we dey try make am correct, abeg make you sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument for im native language na di main source wey you go fit trust. For important mata, e good make you use professional human translator. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->