# AGENTS.md

## Project Overview

Dis repositori get "AI Agents for Beginners" - one beta complete educational course wey dey teach all tins wey you need sabi to build AI Agents. Di course get 18 lessons (wey dem number 00-18) wey dey cover fundamentals, design patterns, frameworks, production deployment, local/on-device agents, and security of AI agents.

**Key Technologies:**
- Python 3.12+
- Jupyter Notebooks for interactive learning
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architecture:**
- Lesson-based structure (00-18 directories)
- Every lesson get README documentation, code samples (Jupyter notebooks), and images
- Multi-language support through automated translation system
- One Python notebook per lesson wey use Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 or higher
- Azure subscription (for Microsoft Foundry)
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

For **Microsoft Foundry** (Required):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-5-mini)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Run `az login` before you run notebooks (e dey use `AzureCliCredential`).

## Development Workflow

### Running Jupyter Notebooks

Every lesson get many Jupyter notebooks for different frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate go lesson directory** (example, `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - Using Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Using Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Need Azure subscription
- Dey use `FoundryChatClient` for Agent Service V2 (agents wey dey show inside Foundry portal)
- Production-ready with built-in observability
- File pattern: `*-python-agent-framework.ipynb`

## Testing Instructions

Dis na educational repository wey get example code no be production code get automated tests. To confirm your setup and changes:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Running Individual Notebooks

Open notebooks for Jupyter and run cells one by one. Each notebook self-contained and e get:
- Import statements
- Configuration loading
- Example agent implementations
- Expected outputs inside markdown cells

### Smoke-Testing Deployed Agents

For lessons wey agent dem deploy as Microsoft Foundry hosted agent (01, 04, 05, 16), the repo get smoke-test catalogs under `tests/` wey the `.github/workflows/smoke-test.yml` workflow dey run through the [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) action. Dis na light post-deploy gate (agent fit dey reachable and follow basic prompt expectations?), e complement evaluation pipeline inside Lessons 10 and 16. See [tests/README.md](./tests/README.md) for catalog-to-lesson-to-agent mapping. Lesson 17 dey run locally with Foundry Local and no get hosted endpoint, so di e dey validate by running e notebook directly.

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: Follow standard Python PEP 8 conventions
- **Notebooks**: Use clear markdown cells to explain concepts
- **Imports**: Group by standard library, third-party, local imports

### Jupyter Notebook Conventions

- Put descriptive markdown cells before code cells
- Add output examples for notebooks as reference
- Use clear variable names wey match lesson concepts
- Make notebook execution order dey linear (cell 1 → 2 → 3...)

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
- Main README.md for repository root
- Automated translation system through GitHub Actions

### CI/CD Pipeline

E dey inside `.github/workflows/`:

1. **co-op-translator.yml** - Automatic translation reach 50+ languages
2. **welcome-issue.yml** - Welcomes new issue creators
3. **welcome-pr.yml** - Welcomes new pull request contributors

### Deployment

Dis na educational repository - no deployment process. Users:
1. Fork or clone the repository
2. Run notebooks locally or for GitHub Codespaces
3. Learn by modifying and experimenting with examples

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Run affected notebooks complete
   - Confirm all cells run without errors
   - Check say outputs dey correct

2. **Documentation updates:**
   - Update README.md if you add new concepts
   - Put comments inside notebooks for everywhere wey code dey complex
   - Make sure markdown cells explain wetin e suppose do

3. **File changes:**
   - No commit `.env` files (use `.env.example`)
   - No commit `venv/` or `__pycache__/` directories
   - Keep notebook outputs if dem show concepts
   - Remove temporary files and backup notebooks (`*-backup.ipynb`)

### PR Title Format

Use clear descriptive titles:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- Notebooks suppose run without errors
- README files suppose clear and accurate
- Follow the current code patterns inside repository
- Make e consistent with other lessons

## Additional Notes

### Common Gotchas

1. **Python version mismatch:**
   - Make sure say you dey use Python 3.12+
   - Some packages no fit work with older versions
   - Use `python3 -m venv` to talk Python version clear clear

2. **Environment variables:**
   - Always create `.env` from `.env.example`
   - No commit `.env` file (e dey inside `.gitignore`)
   - Sign in with `az login` for keyless Entra ID authentication

3. **Package conflicts:**
   - Use fresh virtual environment
   - Install from `requirements.txt` not individual packages
   - Some notebooks fit need additional packages wey their markdown cells talk about

4. **Azure services:**
   - Azure AI services need active subscription
   - Some features dey region specific
   - Make sure your Azure OpenAI model deployment support the Responses API

### Learning Path

How to take move well through lessons:
1. **00-course-setup** - Start here for environment setup
2. **01-intro-to-ai-agents** - Understand AI agent basics
3. **02-explore-agentic-frameworks** - Learn about different frameworks
4. **03-agentic-design-patterns** - Core design patterns
5. Continue through lessons wey dem number sequentially

### Framework Selection

Choose framework based on wetin you want achieve:
- **All lessons**: Microsoft Agent Framework (MAF) with `FoundryChatClient`
- **Agents register server-side** for Microsoft Foundry Agent Service V2 and e dey visible for Foundry portal

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
- Translate to more languages

See [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for wetin dem need now.

## Project-Specific Context

### Multi-Language Support

Dis repository dey use automated translation system:
- Support 50+ languages
- Translations dey inside `/translations/<lang-code>/` directories
- GitHub Actions workflow dey handle translation updates
- Source files dey English for repository root

### Lesson Structure

Every lesson dey follow one level pattern:
1. Video thumbnail with link
2. Written lesson content (README.md)
3. Code samples for different frameworks
4. Learning objectives and prerequisites
5. Extra learning resources linked

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