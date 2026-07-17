# AGENTS.md

## Project Overview

Dis repository get "AI Agents for Beginners" - na complete educational course wey dey teach everything wey person need to sabi build AI Agents. Di course get 18 lessons (wey dem number 00-18) wey dey cover fundamentals, design patterns, frameworks, production deployment, local/on-device agents, plus security of AI agents.

**Key Technologies:**
- Python 3.12+
- Jupyter Notebooks for interactive learning
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architecture:**
- Lesson-based structure (00-15+ directories)
- Every lesson get: README documentation, code samples (Jupyter notebooks), plus images
- Multi-language support through automated translation system
- One Python notebook per lesson wey dey use Microsoft Agent Framework

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

For **Microsoft Foundry** (Wey una need):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-4.1-mini)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Run `az login` before running notebooks (e dey use `AzureCliCredential`).

## Development Workflow

### Running Jupyter Notebooks

Every lesson get plenty Jupyter notebooks for different frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Go enter lesson directory** (like `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - Using Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Using Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Requires Azure subscription
- Uses `FoundryChatClient` for Agent Service V2 (agents wey you fit see for Foundry portal)
- Production-ready with built-in observability
- File pattern: `*-python-agent-framework.ipynb`

## Testing Instructions

Dis na educational repository wey get example code, no be production code wey get automated tests. To check your setup and changes:

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # E suppose be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # Change notebook go skript and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Running Individual Notebooks

Open notebooks for Jupyter and run cells one by one. Every notebook dey self-contained and e get:
- Import statements
- Configuration loading
- Example agent implementations
- Expected outputs for markdown cells

### Smoke-Testing Deployed Agents

For lessons wey dem deploy agent as Microsoft Foundry hosted agent (01, 04, 05, 16), di repo get smoke-test catalogs inside `tests/` wey di `.github/workflows/smoke-test.yml` workflow dey run through the [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) action. Dem be lightweight post-deploy gate (to check if agent dey reachable and e dey follow basic prompt expectations), e also dey complement the evaluation pipeline for Lessons 10 and 16. Check [tests/README.md](./tests/README.md) for how catalog relate to lesson and agent. Lesson 17 dey run local with Foundry Local and no get hosted endpoint, so e dey validate by running e notebook directly.

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: Follow standard Python PEP 8 conventions
- **Notebooks**: Use clear markdown cells to explain concepts
- **Imports**: Group by standard library, third-party, local imports

### Jupyter Notebook Conventions

- Include descriptive markdown cells before code cells
- Add output examples in notebooks for reference
- Use clear variable names weh follow lesson concepts
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
- README.md files for every lesson folder
- Main README.md for repository root
- Automated translation system through GitHub Actions

### CI/CD Pipeline

E dey for `.github/workflows/`:

1. **co-op-translator.yml** - Automatic translation to 50+ languages
2. **welcome-issue.yml** - Welcomes new issue creators
3. **welcome-pr.yml** - Welcomes new pull request contributors

### Deployment

Dis na educational repository - no deployment process. Users:
1. Fork or clone di repository
2. Run notebooks local or inside GitHub Codespaces
3. Learn by modifying and testing examples

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - Run all affected notebooks complete
   - Make sure all cells run without any error
   - Check say outputs dey correct

2. **Documentation updates:**
   - Update README.md if you add new concepts
   - Put comments for complex code inside notebooks
   - Make sure markdown cells explain wetin e mean

3. **File changes:**
   - No make you commit `.env` files (use `.env.example`)
   - No commit `venv/` or `__pycache__/` directories
   - Keep notebook outputs if dem dey show concepts
   - Remove temporary files and backup notebooks (`*-backup.ipynb`)

### PR Title Format

Use descriptive titles:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- Notebooks suppose run without error
- README files suppose dey clear and correct
- Follow the code patterns wey dey already for the repository
- Make everything consistent with other lessons

## Additional Notes

### Common Gotchas

1. **Python version mismatch:**
   - Make sure you dey use Python 3.12+ 
   - Some packages no go work for old Python versions
   - Use `python3 -m venv` to specify Python version explicitly

2. **Environment variables:**
   - Always create `.env` from `.env.example`
   - No commit `.env` file (e dey for `.gitignore`)
   - Sign in with `az login` for keyless Entra ID authentication

3. **Package conflicts:**
   - Use fresh virtual environment
   - Install from `requirements.txt` instead of individual packages
   - Some notebooks fit need extra packages wey dem talk about for markdown cells dem

4. **Azure services:**
   - Azure AI services need active subscription
   - Some features dey only for certain regions
   - Make sure your Azure OpenAI model deployment fit support the Responses API

### Learning Path

Recommended progression through lessons:
1. **00-course-setup** - Start from here for environment setup
2. **01-intro-to-ai-agents** - Understand AI agent fundamentals
3. **02-explore-agentic-frameworks** - Learn about different frameworks
4. **03-agentic-design-patterns** - Core design patterns
5. Continue with next lessons for the sequence

### Framework Selection

Choose framework based on your goals:
- **All lessons**: Microsoft Agent Framework (MAF) with `FoundryChatClient`
- **Agents register for server-side** inside Microsoft Foundry Agent Service V2 and you go fit see am for Foundry portal

### Getting Help

- Join the [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Check lesson README files for specific guidance
- Check the main [README.md](./README.md) for course overview
- Refer to [Course Setup](./00-course-setup/README.md) for detailed setup instructions

### Contributing

Dis na open educational project. Contributions dey welcome:
- Improve code examples
- Fix typos or mistakes
- Add clarifying comments
- Suggest new lesson topics
- Translate to more languages

Check [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for wetin dem dey currently need.

## Project-Specific Context

### Multi-Language Support

Dis repository dey use automated translation system:
- 50+ languages supported
- Translations dey for `/translations/<lang-code>/` directories
- GitHub Actions workflow dey handle translation updates
- Source files na English for repository root

### Lesson Structure

Every lesson follow one consistent pattern:
1. Video thumbnail wey get link
2. Written lesson content (README.md)
3. Code samples for several frameworks
4. Learning objectives and prerequisites
5. Extra learning resources link

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