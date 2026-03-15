# AGENTS.md

## Project Overview

Dis repository get "AI Agents for Beginners" - one kain full educational course wey dey teach everything wey person need take build AI Agents. Di course get more dan 15 lessons wey cover fundamentals, design patterns, frameworks, and how to deploy AI agents for production.

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
- Python 3.12 or pass
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
   # Edit .env wit your API keys an endpoints
   ```

### Required Environment Variables

For **Azure AI Foundry** (You Must Get Am):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (example, gpt-4o)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Run `az login` before you start notebooks (e dey use `AzureCliCredential`).

## Development Workflow

### Running Jupyter Notebooks

Every lesson get plenty Jupyter notebooks for different frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Go enter one lesson directory** (for example `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - Using Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Using Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- You need Azure subscription
- E dey use `AzureAIProjectAgentProvider` for Agent Service V2 (agents wey you fit see inside Foundry portal)
- Ready for production and get built-in observability
- File pattern: `*-python-agent-framework.ipynb`

## Testing Instructions

Dis na educational repository wey get example code, no be production code with automated tests. To check say your setup correct and your changes dey right:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # E suppose be 3.12+
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

Open notebooks for Jupyter and run cells one by one. Every notebook get everything inside am and get:
- Import statements
- Configuration loading
- Example agent implementations
- Expected outputs for markdown cells

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: Follow standard Python PEP 8 rules
- **Notebooks**: Use clear markdown cells to explain ideas
- **Imports**: Arrange by standard library, third-party, local imports

### Jupyter Notebook Conventions

- Put clear markdown cells before code
- Add output examples for notebooks dem
- Use clear variable names wey match lesson topics
- Run notebook cells in order (cell 1 → 2 → 3...)

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

Dis repository dey use Markdown for document:
- README.md files inside every lesson folder
- Main README.md for repository root
- Automated translation system through GitHub Actions

### CI/CD Pipeline

E dey for `.github/workflows/` directory:

1. **co-op-translator.yml** - Automatic translation to more than 50 languages
2. **welcome-issue.yml** - Welcomes new issue creators
3. **welcome-pr.yml** - Welcomes new pull request contributors

### Deployment

Dis na educational repository - no deployment process. Users go:
1. Fork or clone the repository
2. Run notebooks locally or for GitHub Codespaces
3. Learn by modifying and testing examples

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Run all affected notebooks completely
   - Check say all cells run without error
   - Make sure outputs correct

2. **Documentation updates:**
   - Update README.md if you add new concepts
   - Add comments inside notebooks for complex code
   - Make markdown cells explain wetin dem suppose explain

3. **File changes:**
   - No commit `.env` files (use `.env.example`)
   - No commit `venv/` or `__pycache__/` directories
   - Keep notebook outputs if dem dey show concepts well
   - Remove temporary files and backup notebooks (`*-backup-ipynb`)

### PR Title Format

Use clear titles:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- Notebooks suppose run without error
- README files suppose be clear and correct
- Follow existing code pattern for repo
- Make e consistent with other lessons dem

## Additional Notes

### Common Gotchas

1. **Python version wahala:**
   - Make sure you dey use Python 3.12+
   - Some packages no go work with old versions
   - Use `python3 -m venv` to specify Python version correct like that

2. **Environment variables:**
   - Always create `.env` from `.env.example`
   - No commit `.env` file (e dey `.gitignore`)
   - GitHub token need correct permissions

3. **Package conflicts:**
   - Use fresh virtual environment
   - Install from `requirements.txt` not individual packages
   - Some notebooks fit need extra packages wey dem talk for markdown cells

4. **Azure services:**
   - Azure AI services need active subscription
   - Some features na region-specific
   - Free tier get limitation for GitHub Models

### Learning Path

Recommended order for lessons:
1. **00-course-setup** - Begin here to setup environment
2. **01-intro-to-ai-agents** - Understand AI agent fundamentals
3. **02-explore-agentic-frameworks** - Learn about different frameworks
4. **03-agentic-design-patterns** - Core design patterns
5. Continue with next lessons in correct number order

### Framework Selection

Choose framework based on your goals:
- **All lessons**: Microsoft Agent Framework (MAF) with `AzureAIProjectAgentProvider`
- **Agents register server-side** inside Azure AI Foundry Agent Service V2 and you fit see dem for Foundry portal

### Getting Help

- Join the [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Check lesson README files for specific help
- Read main [README.md](./README.md) for course overview
- Look [Course Setup](./00-course-setup/README.md) for full setup guide

### Contributing

Dis na open educational project. Contributions dey welcome:
- Improve code examples
- Fix typos or errors
- Add clarifying comments
- Suggest new lesson topics
- Translate to more languages

See [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for current wants.

## Project-Specific Context

### Multi-Language Support

Dis repository dey use automated translation system:
- More than 50 languages supported
- Translations dey for `/translations/<lang-code>/` folders
- GitHub Actions workflow na im dey handle translation updates
- The source files dey English for repository root

### Lesson Structure

Every lesson follow correct pattern:
1. Video thumbnail with link
2. Written lesson content (README.md)
3. Code samples for many frameworks
4. Learning objectives and prerequisites
5. Extra learning resources wey dem link give you

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

Important packages from `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol support
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure authentication (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integration
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document na translation wey AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do. Even though we try make am correct, abeg sabi say automated translation fit get mistake or no too correct. Di original document wey e dey for im original language na di correct source. If na important matter, e good make person wey sabi translate am do am. We no dey responsible if person no understand well or if dem wrong interpret dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->