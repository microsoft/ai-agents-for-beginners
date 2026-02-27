# AGENTS.md

## Project Overview

Dis repository get "AI Agents for Beginners" - one kain complete educational course wey dey teach everything wey person need sabi to build AI Agents. Di course get 15+ lessons wey cover fundamentals, design patterns, frameworks, and how to deploy AI agents for production.

**Key Technologies:**
- Python 3.12+
- Jupyter Notebooks for interactive learning
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architecture:**
- Lesson-based structure (00-15+ directories)
- Each lesson get: README documentation, code samples (Jupyter notebooks), and images
- Multi-language support through automated translation system
- One Python notebook per lesson wey dey use Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 or higher
- Azure subscription (for Azure AI Foundry)
- Azure CLI installed and authenticated (`az login`)

### Initial Setup

1. **Clone or fork the repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Create and activate Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env wit your API keys and endpoints
   ```

### Required Environment Variables

For **Azure AI Foundry** (Required):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-4o)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Run `az login` before running notebooks (na `AzureCliCredential` e use).

## Development Workflow

### Running Jupyter Notebooks

Each lesson get plenty Jupyter notebooks for different frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate to a lesson directory** (like `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - Using Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Using Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Need Azure subscription
- E dey use `AzureAIProjectAgentProvider` for Agent Service V2 (agents dey show for Foundry portal)
- Production-ready with built-in observability
- File pattern: `*-python-agent-framework.ipynb`

## Testing Instructions

Dis one na educational repository with example code, no be production code with automated tests. To check your setup and changes:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # E suppose be 3.12 or pass
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # Change notebook go script and run am (to test imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Running Individual Notebooks

Open notebooks for Jupyter and run cells one by one. Each notebook dey complete on e own and get:
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

- Include descriptive markdown cells before code cells
- Add output examples in notebooks for reference
- Use clear variable names wey follow lesson concepts
- Keep notebook execution order linear (cell 1 → 2 → 3...)

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

Dis repository dey use Markdown for documentation:
- README.md files inside every lesson folder
- Main README.md dey for repository root
- Automated translation system by GitHub Actions

### CI/CD Pipeline

Dem dey for `.github/workflows/`:

1. **co-op-translator.yml** - Automatic translation to 50+ languages
2. **welcome-issue.yml** - Welcomes new issue creators
3. **welcome-pr.yml** - Welcomes new pull request contributors

### Deployment

Na educational repository dis - no get any deployment process. Users:
1. Fork or clone the repository
2. Run notebooks locally or inside GitHub Codespaces
3. Learn by modifying and experimenting with examples

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Run all affected notebooks complete
   - Make sure all cells run without wahala
   - Check say outputs dey correct

2. **Documentation updates:**
   - Update README.md if you add new concepts
   - Put comments for notebooks if code dey complex
   - Make sure markdown cells explain wetin dem mean

3. **File changes:**
   - No commit `.env` files (use `.env.example` instead)
   - No commit `venv/` or `__pycache__/` dirs
   - Keep notebook outputs if dem show concepts well
   - Remove temporary files and backup notebooks (`*-backup.ipynb`)

### PR Title Format

Use titles wey clear:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- Notebooks must run without errors
- README files must dey clear and correct
- Follow existing code patterns for di repository
- Maintain consistency with other lessons

## Additional Notes

### Common Gotchas

1. **Python version mismatch:**
   - Make sure you dey use Python 3.12+
   - Some packages no go work with older versions
   - Use `python3 -m venv` to specify Python version well well

2. **Environment variables:**
   - Always create `.env` from `.env.example`
   - No commit your `.env` file (e dey ignored)
   - GitHub token need correct permissions

3. **Package conflicts:**
   - Use fresh virtual environment
   - Install from `requirements.txt` instead of installing packages one by one
   - Some notebooks fit need extra packages wey dem mention for markdown cells

4. **Azure services:**
   - Azure AI services need active subscription
   - Some features dey only for certain regions
   - Free tier restrictions dey for GitHub Models

### Learning Path

Recommended steps through lessons:
1. **00-course-setup** - Start here for environment setup
2. **01-intro-to-ai-agents** - Understand AI agent fundamentals
3. **02-explore-agentic-frameworks** - Learn about different frameworks
4. **03-agentic-design-patterns** - Main design patterns
5. Continue with numbered lessons one after another

### Framework Selection

Choose framework based on your goals:
- **All lessons**: Microsoft Agent Framework (MAF) with `AzureAIProjectAgentProvider`
- **Agents register server-side** for Azure AI Foundry Agent Service V2 and dem dey visible for Foundry portal

### Getting Help

- Join the [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Read lesson README files for specific guidance
- Check main [README.md](./README.md) for course overview
- Refer to [Course Setup](./00-course-setup/README.md) for detailed setup steps

### Contributing

Na open educational project dis one. Contributions dey welcome:
- Improve code examples
- Fix typos or errors
- Add clarifying comments
- Suggest new lesson topics
- Translate to more languages

See [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for wetin dem need currently.

## Project-Specific Context

### Multi-Language Support

Dis repository dey use automated translation system:
- 50+ languages supported
- Translations dey `/translations/<lang-code>/` directories
- GitHub Actions workflow dey handle translation updates
- Source files dey English for repository root

### Lesson Structure

Each lesson get consistent pattern:
1. Video thumbnail with link
2. Written lesson content (README.md)
3. Code samples in different frameworks
4. Learning objectives and prerequisites
5. Extra learning resources with links

### Code Sample Naming

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lesson 1, MAF Python
- `14-sequential.ipynb` - Lesson 14, MAF advanced patterns

### Special Directories

- `translated_images/` - Localized images for translations
- `images/` - Original images for English content
- `.devcontainer/` - VS Code development container config
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
**Disclaimer**:  
Dis document dem don translate am wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we try make e correct well well, abeg no forget say automated translation fit get error or wahala for accuracy. Di original document wey na im own language be di correct and true one. If na important info, e beta make professional human translation do am. We no gree take responsibility for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->