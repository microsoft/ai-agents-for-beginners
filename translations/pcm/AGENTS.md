# AGENTS.md

## Project Overview

Dis repository get "AI Agents for Beginners" - na complete educational course wey dey teach everything wey person need sabi to build AI Agents. Di course get 18 lessons wey cover fundamentals, design patterns, frameworks, and how to deploy AI agents for production.

**Key Technologies:**
- Python 3.12+
- Jupyter Notebooks for interactive learning
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architecture:**
- Lesson-based structure (00-15+ directories)
- Every lesson get: README documentation, code samples (Jupyter notebooks), plus images
- Multi-language support with automated translation system
- One Python notebook per lesson wey dey use Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 or above
- Azure subscription (for Microsoft Foundry)
- Azure CLI install and authenticated (`az login`)

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
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Change .env wit your API keys an where you go take run am
   ```

### Required Environment Variables

For **Microsoft Foundry** (Required):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (ex: gpt-4o)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Run `az login` before you run notebooks (e dey use `AzureCliCredential`).

## Development Workflow

### Running Jupyter Notebooks

Every lesson get plenty Jupyter notebooks for different frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Go enter lesson directory** (ex: `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - Using Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Using Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- You need Azure subscription
- E dey use `FoundryChatClient` for Agent Service V2 (agents go dey visible for Foundry portal)
- E ready for production plus e get built-in observability
- File pattern: `*-python-agent-framework.ipynb`

## Testing Instructions

Dis na educational repository with example code, no be production code with automated tests. To check if your setup and changes correct:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # E suppose be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # Change notebook go script and run am (e dey test imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Running Individual Notebooks

Open notebooks for Jupyter and run the cells one by one. Every notebook get:
- Import statements
- Configuration loading
- Example agent implementations
- Expected outputs inside markdown cells

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: Follow normal Python PEP 8 conventions
- **Notebooks**: Use clear markdown cells to explain concepts
- **Imports**: Group by standard library, third-party, local imports

### Jupyter Notebook Conventions

- Put clear markdown cells before code cells
- Add output examples inside notebooks for reference
- Use clear variable names wey relate to lesson concepts
- Keep notebook execution order simple (cell 1 → 2 → 3...)

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
- README.md files for every lesson folder
- Main README.md for repository root
- Automated translation system using GitHub Actions

### CI/CD Pipeline

E dey by `.github/workflows/`:

1. **co-op-translator.yml** - Automatic translation to 50+ languages
2. **welcome-issue.yml** - Welcomes new issue creators
3. **welcome-pr.yml** - Welcomes new pull request contributors

### Deployment

Dis na educational repository - no deployment process. Users:
1. Fork or clone di repository
2. Run notebooks for local machine or for GitHub Codespaces
3. Learn by toying and experimenting with examples

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Run the affected notebooks fully
   - Check say all cells run without error
   - Make sure say outputs dey correct

2. **Documentation updates:**
   - Update README.md if na new concepts you add
   - Add comments for complex code inside notebooks
   - Make sure markdown cells explain wetin the code dey do

3. **File changes:**
   - No commit `.env` files (use `.env.example`)
   - No commit `venv/` or `__pycache__/` folders
   - Keep notebook outputs when dem dey explain concepts
   - Remove temporary files and backup notebooks (`*-backup.ipynb`)

### PR Title Format

Use descriptive titles like:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- Notebooks must run without error
- README files must dey clear and correct
- Follow existing code style inside repository
- Maintain consistency with other lessons

## Additional Notes

### Common Gotchas

1. **Python version mismatch:**
   - Make sure say you dey use Python 3.12+
   - Some packages no go work with old versions
   - Use `python3 -m venv` to specify Python version clearly

2. **Environment variables:**
   - Always create `.env` from `.env.example`
   - No commit `.env` file (na `.gitignore` dey ignore am)
   - Use `az login` to sign in for keyless Entra ID authentication

3. **Package conflicts:**
   - Use fresh virtual environment
   - Install from `requirements.txt` no be individually
   - Some notebooks fit need extra packages wey dem talk for the markdown cells

4. **Azure services:**
   - Azure AI services need active subscription
   - Some features dey region-specific
   - Make sure your Azure OpenAI model deployment dey support the Responses API

### Learning Path

Recommended way to waka through lessons:
1. **00-course-setup** - Start here to set up environment
2. **01-intro-to-ai-agents** - Understand AI agent basics
3. **02-explore-agentic-frameworks** - Learn about different frameworks
4. **03-agentic-design-patterns** - Core design patterns
5. Continue through all numbered lessons one by one

### Framework Selection

Choose framework based on wetin you wan achieve:
- **All lessons**: Microsoft Agent Framework (MAF) with `FoundryChatClient`
- **Agents register for server-side** inside Microsoft Foundry Agent Service V2 and dem go visible for Foundry portal

### Getting Help

- Join the [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Check lesson README files for special guidance
- Look di main [README.md](./README.md) for course overview
- Refer to [Course Setup](./00-course-setup/README.md) for detailed setup instructions

### Contributing

Dis na open educational project. Contributions welcome:
- Improve code examples
- Fix typos or errors
- Add clear comments
- Suggest new lesson topics
- Translate to more languages

See [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for wetin we need now.

## Project-Specific Context

### Multi-Language Support

Dis repository dey use automated translation system:
- 50+ languages dey supported
- Translations dey inside `/translations/<lang-code>/` directories
- GitHub Actions workflow dey handle translation updates
- Source files dey English for repository root

### Lesson Structure

Every lesson get one kain pattern:
1. Video thumbnail with link
2. Written lesson content (README.md)
3. Code samples for different frameworks
4. Learning objectives and prerequisites
5. Extra learning resources linked

### Code Sample Naming

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lesson 1, MAF Python
- `14-sequential.ipynb` - Lesson 14, advanced MAF patterns

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
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->