# AGENTS.md

## Project Overview

This repository contains "AI Agents for Beginners" - a comprehensive educational course that teaches everything you need to know to build AI Agents. The course includes over 15 lessons covering the basics, design patterns, frameworks, and deploying AI agents in production.

**Key Technologies:**
- Python 3.12+
- Jupyter Notebooks for interactive learning
- AI Frameworks: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI Services: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (free tier available)

**Architecture:**
- Lesson-based structure (directories numbered 00-15+)
- Each lesson includes: README documentation, code samples (Jupyter notebooks), and images
- Multi-language support through an automated translation system
- Multiple framework options for each lesson (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Setup Commands

### Prerequisites
- Python 3.12 or higher
- GitHub account (required for GitHub Models - free tier)
- Azure subscription (optional, for Azure AI services)

### Initial Setup

1. **Clone or fork the repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Create and activate a Python virtual environment:**
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
- Additional Azure configuration as shown in `.env.example`

## Development Workflow

### Running Jupyter Notebooks

Each lesson includes multiple Jupyter notebooks for different frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate to a lesson directory** (e.g., `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-semantic-kernel.ipynb` - Using the Semantic Kernel framework
   - `*-autogen.ipynb` - Using the AutoGen framework
   - `*-python-agent-framework.ipynb` - Using Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Using Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Using Azure AI Agent Service

### Working with Different Frameworks

**Semantic Kernel + GitHub Models:**
- Free tier available with GitHub account
- Ideal for learning and experimentation
- File pattern: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Free tier available with GitHub account
- Supports multi-agent orchestration
- File pattern: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Latest framework from Microsoft
- Available in Python and .NET
- File pattern: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Requires Azure subscription
- Production-ready features
- File pattern: `*-azureaiagent.ipynb`

## Testing Instructions

This is an educational repository with example code rather than production code with automated tests. To verify your setup and changes:

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

Open notebooks in Jupyter and execute cells sequentially. Each notebook is self-contained and includes:
- Import statements
- Configuration loading
- Example agent implementations
- Expected outputs in markdown cells

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: Follow standard Python PEP 8 conventions
- **Notebooks**: Use clear markdown cells to explain concepts
- **Imports**: Group by standard library, third-party, local imports

### Jupyter Notebook Conventions

- Include descriptive markdown cells before code cells
- Add output examples in notebooks for reference
- Use clear variable names that match lesson concepts
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

This repository uses Markdown for documentation:
- README.md files in each lesson folder
- Main README.md at the repository root
- Automated translation system via GitHub Actions

### CI/CD Pipeline

Located in `.github/workflows/`:

1. **co-op-translator.yml** - Automatically translates content into 50+ languages
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
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- Notebooks should execute without errors
- README files should be clear and accurate
- Follow existing code patterns in the repository
- Maintain consistency with other lessons

## Additional Notes

### Common Gotchas

1. **Python version mismatch:**
   - Ensure Python 3.12+ is used
   - Some packages may not work with older versions
   - Use `python3 -m venv` to specify Python version explicitly

2. **Environment variables:**
   - Always create `.env` from `.env.example`
   - Don't commit `.env` file (it's in `.gitignore`)
   - GitHub token needs appropriate permissions

3. **Package conflicts:**
   - Use a fresh virtual environment
   - Install from `requirements.txt` rather than individual packages
   - Some notebooks may require additional packages mentioned in their markdown cells

4. **Azure services:**
   - Azure AI services require an active subscription
   - Some features are region-specific
   - Free tier limitations apply to GitHub Models

### Learning Path

Recommended progression through lessons:
1. **00-course-setup** - Start here for environment setup
2. **01-intro-to-ai-agents** - Understand AI agent fundamentals
3. **02-explore-agentic-frameworks** - Learn about different frameworks
4. **03-agentic-design-patterns** - Core design patterns
5. Continue through numbered lessons sequentially

### Framework Selection

Choose a framework based on your goals:
- **Learning/Prototyping**: Semantic Kernel + GitHub Models (free)
- **Multi-agent systems**: AutoGen
- **Latest features**: Microsoft Agent Framework (MAF)
- **Production deployment**: Azure AI Agent Service

### Getting Help

- Join the [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Review lesson README files for specific guidance
- Check the main [README.md](./README.md) for course overview
- Refer to [Course Setup](./00-course-setup/README.md) for detailed setup instructions

### Contributing

This is an open educational project. Contributions are welcome:
- Improve code examples
- Fix typos or errors
- Add clarifying comments
- Suggest new lesson topics
- Translate to additional languages

See [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for current needs.

## Project-Specific Context

### Multi-Language Support

This repository uses an automated translation system:
- 50+ languages supported
- Translations in `/translations/<lang-code>/` directories
- GitHub Actions workflow handles translation updates
- Source files are in English at the repository root

### Lesson Structure

Each lesson follows a consistent pattern:
1. Video thumbnail with link
2. Written lesson content (README.md)
3. Code samples in multiple frameworks
4. Learning objectives and prerequisites
5. Extra learning resources linked

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

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.