# AGENTS.md

## Project Overview

Dis repo contain "AI Agents for Beginners" - na comprehensive educational course wey dey teach everything wey person need to build AI Agents. Di course get 18 lessons (dem number 00-18) wey cover fundamentals, design patterns, frameworks, production deployment, local/on-device agents, plus security for AI agents.

**Key Technologies:**
- Python 3.12+
- Jupyter Notebooks for interactive learning
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architecture:**
- Lesson-based structure (00-15+ directories)
- Each lesson get: README documentation, code samples (Jupyter notebooks), and images
- Multi-language support via automated translation system
- One Python notebook per lesson wey dey use Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 or higher
- Azure subscription (for Microsoft Foundry)
- Azure CLI installed and authenticated (`az login`)

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
   # Change .env wit your API keys and endpoints
   ```

### Required Environment Variables

For **Microsoft Foundry** (Required):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-5-mini)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Run `az login` before you run notebooks (e dey use `AzureCliCredential`).

## Development Workflow

### Running Jupyter Notebooks

Every lesson get multiple Jupyter notebooks for different frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate to di lesson directory** (e.g., `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - Using Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Using Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Need Azure subscription
- Dem dey use `FoundryChatClient` for Agent Service V2 (agents dey visible for Foundry portal)
- Production-ready with built-in observability
- File pattern: `*-python-agent-framework.ipynb`

## Testing Instructions

Dis na educational repository wey get example code instead of production code wey get automated tests. To check your setup and changes:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # E suppose be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # Change notebook go script and run am (test di imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Running Individual Notebooks

Open notebooks for Jupyter and run cells one by one. Every notebook get:
- Import statements
- Configuration loading
- Example agent implementations
- Expected outputs for markdown cells

### Smoke-Testing Deployed Agents

For lessons wey dem deploy agent as Microsoft Foundry hosted agent (01, 04, 05, 16), di repo get smoke-test catalogs under `tests/` wey `.github/workflows/smoke-test.yml` workflow dey run through [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) action. Dem be lightweight post-deploy gate (agent fit reach and e dey follow basic prompt expectations?), e dey complement evaluation pipeline for Lessons 10 and 16. Check [tests/README.md](./tests/README.md) for catalog-to-lesson-to-agent mapping. Lesson 17 dey run locally with Foundry Local and e no get hosted endpoint, so e dey validated by running e notebook direct.

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: Follow standard Python PEP 8 conventions
- **Notebooks**: Use clear markdown cells to explain concepts
- **Imports**: Group by standard library, third-party, local imports

### Jupyter Notebook Conventions

- Include descriptive markdown cells before code cells
- Add output examples for notebooks reference
- Use clear variable names wey match lesson concepts
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
- README.md files dey for each lesson folder
- Main README.md dey for repository root
- Automated translation system via GitHub Actions

### CI/CD Pipeline

E dey for `.github/workflows/`:

1. **co-op-translator.yml** - Automatic translation to 50+ languages
2. **welcome-issue.yml** - Welcomes new issue creators
3. **welcome-pr.yml** - Welcomes new pull request contributors

### Deployment

Dis na educational repository - no deployment process. Users go:
1. Fork or clone di repository
2. Run notebooks locally or for GitHub Codespaces
3. Learn by modifying and experimenting with examples

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Run all affected notebooks full
   - Verify all cells run without error
   - Check say outputs correct

2. **Documentation updates:**
   - Update README.md if you add new concepts
   - Add comments inside notebooks for complex code
   - Make sure markdown cells explain wetin dem dey do

3. **File changes:**
   - No commit `.env` files (use `.env.example`)
   - No commit `venv/` or `__pycache__/` directories
   - Keep notebook outputs when dem dey show concepts
   - Remove temporary files and backup notebooks (`*-backup.ipynb`)

### PR Title Format

Use descriptive titles:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo for lesson-XX README`
- `[Update] Improve code sample for lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- Notebooks suppose run without errors
- README files suppose clear and accurate
- Follow di code patterns wey dey this repository
- Keep consistency with other lessons

## Additional Notes

### Common Gotchas

1. **Python version mismatch:**
   - Make sure you dey use Python 3.12+
   - Some packages no go work wit old versions
   - Use `python3 -m venv` to specify Python version clearly

2. **Environment variables:**
   - Always create `.env` from `.env.example`
   - No commit `.env` file (e dey `.gitignore`)
   - Use `az login` to sign in for keyless Entra ID authentication

3. **Package conflicts:**
   - Use fresh virtual environment
   - Install from `requirements.txt` instead of individual packages
   - Some notebooks fit need extra packages wey dem talk for markdown cells

4. **Azure services:**
   - Azure AI services need active subscription
   - Some features dey region-specific
   - Make sure say your Azure OpenAI model deployment support Responses API

### Learning Path

How e go better if you dey follow lessons:
1. **00-course-setup** - Start here to setup environment
2. **01-intro-to-ai-agents** - Understand AI agent basics
3. **02-explore-agentic-frameworks** - Learn different frameworks
4. **03-agentic-design-patterns** - Core design patterns
5. Continue through di lessons in order

### Framework Selection

Choose framework based on wetin you want achieve:
- **All lessons**: Microsoft Agent Framework (MAF) wit `FoundryChatClient`
- **Agents register server-side** inside Microsoft Foundry Agent Service V2 and dem dey visible for Foundry portal

### Getting Help

- Join the [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Check lesson README files for specific guidance
- Check main [README.md](./README.md) for course overview
- Refer to [Course Setup](./00-course-setup/README.md) for detailed setup instructions

### Contributing

Dis na open educational project. Contributions dey welcome:
- Improve code examples
- Fix typos or errors
- Add clarifying comments
- Suggest new lesson topics
- Translate to other languages

See [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for wetin dem need now.

## Project-Specific Context

### Multi-Language Support

Dis repository dey use automated translation system:
- 50+ languages supported
- Translations dey for `/translations/<lang-code>/` directories
- GitHub Actions workflow dey handle translation updates
- Source files na English for repository root

### Lesson Structure

Every lesson follow consistent pattern:
1. Video thumbnail wit link
2. Written lesson content (README.md)
3. Code samples for multiple frameworks
4. Learning objectives and prerequisites
5. Extra learning resources wey get link

### Code Sample Naming

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lesson 1, MAF Python
- `14-sequential.ipynb` - Lesson 14, MAF advanced patterns
- `16-python-agent-framework.ipynb` - Lesson 16, production customer-support agent
- `17-local-agent-foundry-local.ipynb` - Lesson 17, local agent with Foundry Local + Qwen

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