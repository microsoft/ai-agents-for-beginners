# AGENTS.md

## Project Overview

ಈ ರೆಪೊಸಿಟರಿ "ಶುರುವಾರುಗಳಿಗೆ AI ಏಜೆಂಟ್ಸ್" ಎಂಬ ಸಮಗ್ರ ಶೈಕ್ಷಣಿಕ ಕೋರ್ಸ್ ಅನ್ನು ಒಳಗೊಂಡಿದೆ - AI ಏಜೆಂಟ್ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಬೇಕಾದ ಎಲ್ಲಾ ವಿಷಯಗಳನ್ನು ಕಲಿಸುವ ಕೋರ್ಸ್. ಈ ಕೋರ್ಸ್ 15+ ಪಾಠಗಳನ್ನು ಒಳಗೊಂಡಿದ್ದು ಅಡಿಪಾಯಗಳು, ವಿನ್ಯಾಸ ಮಾದರಿಗಳು, ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ಮತ್ತು AI ಏಜೆಂಟ್ಸ್ ರಚನೆ ಮತ್ತು ಉತ್ಪಾದನಾ ನಿಯೋಜನೆಗಳನ್ನು ಒಳಗೊಂಡಿದೆ.

**ಮುಖ್ಯ ತಂತ್ರಜ್ಞಾನಗಳು:**
- Python 3.12+
- ಪರಸ್ಪರ ಕಲಿಕೆಗೆ ಜುಪಿಟರ್ ನೋಟ್ಬುಕ್‌ಗಳು
- AI ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು: Microsoft Agent Framework (MAF)
- Azure AI ಸೇವೆಗಳು: Microsoft Foundry, Azure AI Foundry Agent Service V2

**ವಾಸ್ತುಶಿಲ್ಪ:**
- ಪಾಠಾಧಾರಿತ ರಚನೆ (00-15+ ಡೈರೆಕ್ಟರಿಗಳು)
- ಪ್ರತಿ ಪಾಠದಲ್ಲಿ: README ದಾಖಲೆ, ಕೋಡ್ ಮಾದರಿಗಳು (ಜುಪಿಟರ್ ನೋಟ್ಬುಕ್‌ಗಳು), ಮತ್ತು ಚಿತ್ರಗಳು
- ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದ ವ್ಯವಸ್ಥೆಯ ಮೂಲಕ ಬಹುಭಾಷಾ ಬೆಂಬಲ
- ಪ್ರತಿಒಂದು ಪಾಠಕ್ಕೆ Microsoft Agent Framework ಬಳಸಿ ಒಮ್ಮೆ Python ನೋಟ್ಬುಕ್

## Setup Commands

### Prerequisites
- Python 3.12 ಅಥವಾ ಹೆಚ್ಚು
- Azure ಚಂದಾ (Azure AI Foundry ಗಾಗಿ)
- Azure CLI ಸ್ಥಾಪಿಸಿ ಮತ್ತು ಸಾಂದರ್ಭಿಕ (`az login`)

### Initial Setup

1. **ರೆಪೊಸಿಟರಿಯನ್ನು ಕ್ಲೋನ್ ಅಥವಾ ಫೋರ್ಕ್ ಮಾಡಿ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ಅಥವಾ
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ ಮತ್ತು ಸಕ್ರಿಯಗೊಳಿಸಿ:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # ವಿಂಡೋಸ್‌ನಲ್ಲಿ: venv\Scripts\activate
   ```

3. **ಆವಶ್ಯಕತೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ಪರಿಸರ ಚರಗಳನ್ನು ಸೆಟ್ ಮಾಡಿ:**
   ```bash
   cp .env.example .env
   # ನಿಮ್ಮ API ಕೀಲಿಗಳು ಮತ್ತು ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳೊಂದಿಗೆ .env ಅನ್ನು ಸಂಪಾದಿಸಿ
   ```

### Required Environment Variables

**Azure AI Foundry** (ಅವಶ್ಯಕ):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry ಯೋಜನೆ ಎಂಡ್‌ಪಾಯಿಂಟ್
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ಮಾದರಿ ನಿಯೋಜನೆಯ ಹೆಸರು (ಉದಾ: gpt-4o)

**Azure AI Search** (ಪಾಠ 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search ಎಂಡ್‌ಪಾಯಿಂಟ್
- `AZURE_SEARCH_API_KEY` - Azure AI Search API ಕೀ

ಪ್ರಮಾಣೀಕರಣ: ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ನಡೆಸುವುದಕ್ಕೂ ಮುಂಚೆ `az login` ಅನ್ನು ಚಲಾಯಿಸಿ (`AzureCliCredential` ಉಪಯೋಗಿಸುತ್ತದೆ).

## Development Workflow

### Jupyter ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ನಡೆಸುವುದು

ಪ್ರತಿ ಪಾಠದಲ್ಲಿ ವಿಭಿನ್ನ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳಿಗಾಗಿ ಹಲವಾರು ಜುಪಿಟರ್ ನೋಟ್ಬುಕ್‌ಗಳು ಇವೆ:

1. **ಜುಪಿಟರ್ ಪ್ರಾರಂಭಿಸಿ:**
   ```bash
   jupyter notebook
   ```

2. **ಒಂದು ಪಾಠ ಡೈರೆಕ್ಟರಿಗೆ ನಾವಿಗೇಟ್ ಮಾಡಿ** (ಉದಾ: `01-intro-to-ai-agents/code_samples/`)

3. **ನೋಟ್ಬುಕ್ ತೆರೆಯಿರಿ ಮತ್ತು ಚಲಾಯಿಸಿ:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) ಬಳಸಲಾಗುತ್ತದೆ
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) ಬಳಸಲಾಗುತ್ತದೆ

### Microsoft Agent Framework ಯೊಂದಿಗೆ ಕೆಲಸ

**Microsoft Agent Framework + Azure AI Foundry:**
- Azure ಚಂದಾ ಅಗತ್ಯವಿದೆ
- Agent Service V2 ಗಾಗಿ `AzureAIProjectAgentProvider` ಬಳಸುತ್ತದೆ (Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಏಜೆಂಟ್ಸ್ ದೃಶ್ಯಮಾನ)
- ಬಿಲ್ಟ್-ಇನ್ ಅವಲೋಕನದೊಂದಿಗೆ ಉತ್ಪಾದನಾ ಸಿದ್ಧ
- ಫೈಲ್ ಮಾದರಿ: `*-python-agent-framework.ipynb`

## Testing Instructions

ಇದು ಸ್ವಯಂಶಿಕ್ಷಣ ರೆಪೊಸಿಟರಿ; ಸ್ವಯಂಚಾಲಿತ ಪರೀಕ್ಷೆಗಳಿಗಿಂತ ಉದಾಹರಣೆ ಕೋಡ್ ಇದೆ. ನಿಮ್ಮ ವ್ಯವಸ್ಥೆ ಮತ್ತು ಬದಲಾವಣೆಗಳನ್ನು ಪರಿಶೀಲಿಸಲು:

### ಕೈಗಾರಿಕಾ ಪರೀಕ್ಷೆ

1. **Python ಪರಿಸರವನ್ನು ಪರೀಕ್ಷಿಸಿ:**
   ```bash
   python --version  # 3.12 ಕ್ಕಿಂತ ಹೆಚ್ಚು ಇರಬೇಕು
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **ನೋಟ್ಬುಕ್ ನಿರ್ವಹಣೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ:**
   ```bash
   # ನೋಟ್ಬುಕ್ ಅನ್ನು ಸ್ಕ್ರಿಪ್ಟ್‌ಗೆ ಪರಿವರ್ತಿಸಿ ಮತ್ತು ಚಾಲನೆ ಮಾಡಿ (ಟೆಸ್ಟ್‌ಗಳ ಆಮದುಗಳು)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ಪರಿಸರ ಚರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### ವೈಯಕ್ತಿಕ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಚಲಾಯಿಸುವುದು

ಜುಪಿಟರ್‌ನಲ್ಲಿ ನೋಟ್ಬುಕ್ ತೆರೆಯಿರಿ ಮತ್ತು ಕೋಷ್ಟಕಗಳನ್ನು ಕ್ರಮವಾಗಿ ಚಲಾಯಿಸಿ. ಪ್ರತಿ ನೋಟ್ಬುಕ್ ಸ್ವತಂತ್ರ ಮತ್ತು ಹೊಂದಿದೆ:
- ಆಮದು ಸೂಚನೆಗಳು
- ಸಂರಚನಾ ಲೋಡ್
- ಉದಾಹರಣೆ ಏಜೆಂಟ್ ಅನುಷ್ಠಾನಗಳು
- markdown ಕೋಷ್ಟಕದಲ್ಲಿ ನಿರೀಕ್ಷಿತ ಔಟ್‌ಪುಟ್‌ಗಳು

## Code Style

### Python Conventions

- **Python ಆವೃತ್ತಿ**: 3.12+
- **ಕೋಡ್ ಶೈಲಿ**: ಸ್ಥೂಲ Python PEP 8 ಮಾನದಂಡಗಳನ್ನು ಅನುಸರಿಸಿ
- **ನೋಟ್ಬುಕ್‌ಗಳು**: ಕಲಿಕೆಗಳ ವಿವರಣೆಗಾಗಿ ಸ್ಪಷ್ಟ markdown ಕೋಷ್ಟಕಗಳನ್ನು ಬಳಸಿ
- **ಆಮದುಗಳು**: ನಿಯಮಿತ ಲೈಬ್ರರಿ, ತೃತೀಯ-ಪಕ್ಷ, ಸ್ಥಳೀಯ ಆಮದುಗಳ ಪ್ರಕಾರ ಗುಂಪು ಮಾಡಿ

### Jupyter Notebook Conventions

- ಕೋಡ್ ಕೋಷ್ಟಕಗಳ ಮುಂಚೆ ವಿವರಾತ್ಮಕ markdown ಕೋಷ್ಟಕಗಳನ್ನು ಸೇರಿಸಿ
- ಉಲ್ಲೇಖಕ್ಕಾಗಿ ಔಟ್‌ಪುಟ್ ಉದಾಹರಣೆಗಳನ್ನು ನೋಟ್ಬುಕ್‌ನಲ್ಲಿ ಸೇರಿಸಿ
- ಪಾಠದ ಕಲ್ಪನೆಗಳಿಗೆ ಹೊಂದುವ ಸ್ಪಷ್ಟ ವ್ಯತ್ಯಯ ಹೆಸರುಗಳನ್ನು ಬಳಸಿ
- ನೋಟ್ಬುಕ್ ನಿರ್ವಹಣೆಯ ಕ್ರಮವನ್ನು ಲೀನಿಯರ್ (ಕೋಷ್ಟಕ 1 → 2 → 3...) ಆಗಿರಿಸಿ

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

### ದಸ್ತಾವೇಜು ಕಟ್ಟುವಿಕೆ

ಈ ರೆಪೊಸಿಟರಿ Markdown ಬಳಸಿ:
- ಪ್ರತಿ ಪಾಠದ ಫೋಲ್ಡರ್‌ನಲ್ಲಿ README.md ಫೈಲ್
- ಪ್ರಮುಖ README.md ರೆಪೊ ಫೈಲ್ ರೂಟ್‌ನಲ್ಲಿ
- GitHub Actions ಮೂಲಕ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದ ವ್ಯವಸ್ಥೆ

### CI/CD ಪೈಪ್ಲೈನ್

`.github/workflows/` ನಲ್ಲಿ:

1. **co-op-translator.yml** - 50+ ಭಾಷೆಗೆ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದ
2. **welcome-issue.yml** - ಹೊಸ ಮೊತ್ತದ ಸೃಷ್ಟಿಕರ್ತರಿಗೆ ಸ್ವಾಗತ
3. **welcome-pr.yml** - ಹೊಸ ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್ ಕಂತ್ರಿಬ್ಯೂಟರ್ಸ್‌ಗೆ ಸ್ವಾಗತ

### ನಿಯೋಜನೆ

ಇದು ಶೈಕ್ಷಣಿಕ ರೆಪೊಸಿಟರಿ - ನಿಯೋಜನೆ ಪ್ರಕ್ರಿಯೆ ಇಲ್ಲ. ಬಳಕೆದಾರರು:
1. ರೆಪೊ ಕ್ಲೋನ್ ಅಥವಾ ಫೋರ್ಕ್ ಮಾಡಿ
2. ನೋಟ್ಬುಕ್ ಅನ್ನು ಸ್ಥಳೀಯವಾಗಿ ಅಥವಾ GitHub Codespaces ನಲ್ಲಿ ಚಾಲನೆ ಮಾಡಿರಿ
3. ಉದಾಹರಣೆಗಳನ್ನು ಬದಲಾಯಿಸಿ ಮತ್ತು ಪ್ರಯೋಗಮಾಡಿ ಕಲಿಯಿರಿ

## Pull Request Guidelines

### ಸಲ್ಲಿಸುವ ಮೊದಲು

1. **ನಿಮ್ಮ ಬದಲಾವಣೆಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ:**
   - ಪರಿಣಾಮಿತ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಚಲಾಯಿಸಿ
   - ಎಲ್ಲಾ ಕೋಷ್ಟಕವು ದೋಷವಿಲ್ಲದೆ ನಡೆಯುತ್ತಿವೆ ಎಂದು ಪರಿಶೀಲಿಸಿ
   - ಔಟ್‌ಪುಟ್‌ಗಳು ಸೂಕ್ತವಾಗಿವೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ

2. **ದಾಖಲೆ ನವೀಕರಣಗಳು:**
   - ಹೊಸ ಕಲ್ಪನೆಗಳನ್ನು ಸೇರಿಸುವಾಗ README.md ನವೀಕರಿಸಿ
   - ಸಂಕೀರ್ಣ ಕೋಡ್ ಗೆ ಟಿಪ್ಪಣಿಗಳನ್ನು ಸೇರಿಸಿ ನೋಟ್ಬುಕ್‌ನಲ್ಲಿ
   - markdown ಕೋಷ್ಟಕಗಳು ಉದ್ದೇಶವನ್ನು ವಿವರಿಸುತ್ತವೆ ಎಂಬುದನ್ನು ಖಚಿತ ಪಡಿಸಿ

3. **ಫೈಲ್ ಬದಲಾವಣೆಗಳು:**
   - `.env` ಫೈಲ್‌ಗಳನ್ನು ಶೇಖರಿಸಬೇಡಿ (`.env.example` ಬಳಸಿ)
   - `venv/` ಅಥವಾ `__pycache__/` ಡೈರೆಕ್ಟರಿಗಳನ್ನು ಶೇಖರಿಸಬೇಡಿ
   - ಕಲ್ಪನೆಗಳನ್ನು ಪ್ರదర్శಿಸುವಾಗ ನೋಟ್ಬುಕ್ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಉಳಿಸಿ
   - ತಾತ್ಕಾಲಿಕ ಫೈಲ್‌ಗಳು ಮತ್ತು ಬ್ಯಾಕಪ್ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು (`*-backup.ipynb`) ತೆಗೆದುಹಾಕಿ

### PR ಶೀರ್ಷಿಕೆ ವಿನ್ಯಾಸ

ವಿವರಣಾತ್ಮಕ ಶೀರ್ಷಿಕೆಗಳನ್ನು ಬಳಸಿ:
- `[Lesson-XX] <kalpanege> kosha Hegollu`
- `[Fix] ಪಾಠ-XX README ನಲ್ಲಿ ಟೈಪೋ ಸರಿಪಡಿಸಿ`
- `[Update] ಪಾಠ-XX ನಲ್ಲಿ ಕೋಡ್ ಮಾದರಿಯನ್ನು ಸುಧಾರಿಸಿ`
- `[Docs] ಸೆಟಪ್ ಸೂಚನೆಗಳನ್ನು ನವೀಕರಿಸಿ`

### ಅವಶ್ಯಕ ಪರಿಶೀಲನೆಗಳು

- ನೋಟ್ಬುಕ್‌ಗಳು ದೋಷರಹಿತವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸಬೇಕು
- README ಫೈಲ್‌ಗಳು ಸ್ಪಷ್ಟವಾಗಿರಬೇಕು
- ರೆಪೊದಲ್ಲಿ ಇರುವ ಇತರ ಕೋಡ್ ಮಾದರಿಗಳನ್ನು ಅನುಸರಿಸಿ
- ಇತರ ಪಾಠಗಳೊಂದಿಗೆ ಸಮ್ಮತಿ ಕಾಪಾಡಿಕೊಳ್ಳಿ

## Additional Notes

### ಸಾಮಾನ್ಯ ಕಷ್ಟಗಳು

1. **Python ಆವೃತ್ತಿ ಭಿನ್ನತೆ:**
   - Python 3.12+ ಬಳಸುರಿ
   - ಕೆಲವು ಪ್ಯಾಕೇಜುಗಳು ಹಳೆಯ ಆವೃತ್ತಿಗಳಲ್ಲಿ ಕೆಲಸವಿಲ್ಲ
   - Python ಆವೃತ್ತಿ ಸ್ಪಷ್ಟಪಡಿಸಲು `python3 -m venv` ಬಳಸಿ

2. **ಪರಿಸರ ಚರಗಳು:**
   - `.env.example` ನಿಂದ `.env` ಸದಾ ರಚಿಸಿ
   - `.env` ಫೈಲ್ ಅನ್ನು ಶೇಖರಿಸಬೇಡಿ (`.gitignore` ನಲ್ಲಿ ಇದೆ)
   - GitHub ಟೋಕನ್ ಸೂಕ್ತ ಅನುಮತಿಗಳನ್ನು ಹೊಂದಿರಬೇಕು

3. **ಪ್ಯಾಕೇಜ್ ಸಂಘರ್ಷಗಳು:**
   - ಹೊಸ ವರ್ಚುವಲ್ ಪರಿಸರ ಬಳಸಿ
   - ಬಾಹ್ಯ ಪ್ಯಾಕೇಜುಗಳಿಗಿಂತ `requirements.txt` ನಿಂದ ಸ್ಥಾಪನೆ ಮಾಡಿ
   - ಕೆಲವು ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ markdown ಕೋಷ್ಟಕಗಳಲ್ಲಿ ಉಲ್ಲೇಖಿತ ಹೆಚ್ಚುವರಿ ಪ್ಯಾಕೇಜುಗಳು ಬೇಕಾಗಬಹುದು

4. **Azure ಸೇವೆಗಳು:**
   - Azure AI ಸೇವೆಗಳಿಗಾಗಿ ಸಕ್ರಿಯ ಚಂದಾ ಅಗತ್ಯ
   - ಕೆಲವು ವೈಶಿಷ್ಟ್ಯಗಳು ಪ್ರದೇಶ-ನಿರ್ಬಂಧಿತ
   - GitHub Models ಗೆ ಉಚಿತ ಟಿಯರ್ ಮಿತಿ

### ಕಲಿಕೆಯ ಮಾರ್ಗ

ಪಾಠಗಳ ಸರಣಿಯಲ್ಲಿ ಶಿಫಾರಸು:
1. **00-course-setup** - ಪರಿಸರ ವ್ಯವಸ್ಥೆಗಾಗಿ ಇಲ್ಲಿ ಪ್ರಾರಂಭಿಸಿ
2. **01-intro-to-ai-agents** - AI ಏಜೆಂಟ್ ಮೂಲಭೂತಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ
3. **02-explore-agentic-frameworks** - ವಿಭಿನ್ನ ಫ್ರೇಮ್‌ವರ್ಕ್ ಬಗ್ಗೆ ತಿಳಿದುಕೊಳ್ಳಿ
4. **03-agentic-design-patterns** - ಪ್ರಮುಖ ವಿನ್ಯಾಸ ಮಾದರಿಗಳು
5. ಕ್ರಮವಾಗಿ ಸಂಖ್ಯೆ ಬರುವ ಪಾಠಗಳನ್ನು ಮುಂದುವರಿಸಿ

### ಫ್ರೇಮ್‌ವರ್ಕ್ ಆಯ್ಕೆ

ನಿಮ್ಮ ಗುರಿಗಳಿಗೆ ಅನುಗುಣವಾಗಿ ಫ್ರೇಮ್‌ವರ್ಕ್ ಆಯ್ಕೆಮಾಡಿ:
- **ಎಲ್ಲಾ ಪಾಠಗಳು**: Microsoft Agent Framework (MAF) ಜೊತೆಗೆ `AzureAIProjectAgentProvider`
- **ಆಯೋಜಿತ ಏಜೆಂಟ್‌ಗಳು** Azure AI Foundry Agent Service V2 ನಲ್ಲಿ ಸರ್ವರ್-ಬೈಡ್‌ಗೆ ನೋಂದಾಯಿತವಾಗಿವೆ ಮತ್ತು Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಕಾಣಸಿಗುತ್ತವೆ

### ಸಹಾಯ ಪಡೆಯುವುದು

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) ಗೆ ಸೇರ್ಪಡೆ ಆಗಿ
- ವಿಶಿಷ್ಟ ಮಾರ್ಗದರ್ಶನಕ್ಕಾಗಿ ಪಾಠ README ಫೈಲ್ ಪರಿಶೀಲಿಸಿ
- ಕೋರ್ಸ್ ಅವಲೋಕನಕ್ಕೆ ಮುಖ್ಯ [README.md](./README.md) ನೋಡಿ
- ವಿವರವಾದ ಸೆಟಪ್ ಸೂಚನೆಗಳಿಗೆ [Course Setup](./00-course-setup/README.md) ನೋಡಿ

### ಕೊಡುಗೆ ನೀಡುವುದು

ಇದು ತೆರೆಯಾದ ಶೈಕ್ಷಣಿಕ ಯೋಜನೆ. ಕೊಡುಗೆ ಸ್ವಾಗತ:
- ಕೋಡ್ ಉದಾಹರಣೆಗಳನ್ನು ಸುಧಾರಿಸಿ
- ಟೈಪೋಗಳು ಅಥವಾ ದೋಷಗಳನ್ನು ಸರಿಪಡಿಸಿ
- ಸ್ಪಷ್ಟತೆಯ ಟಿಪ್ಪಣಿಗಳನ್ನು ಸೇರಿಸಿ
- ಹೊಸ ಪಾಠ ವಿಷಯಗಳನ್ನು ಸೂಚಿಸಿ
- ಹೆಚ್ಚಿನ ಭಾಷೆಗಳಿಗಾಗಿಯೂ ಅನುವಾದ ಮಾಡಿ

ಪ್ರಸ್ತುತ ಅವಶ್ಯಕತೆಗಳಿಗೆ [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) ನೋಡಿ.

## Project-Specific Context

### ಬಹುಭಾಷಾ ಬೆಂಬಲ

ಈ ರೆಪೊ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದ ವ್ಯವಸ್ಥೆ ಬಳಸುತ್ತದೆ:
- 50+ ಭಾಷೆಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ
- ಅನುವಾದಗಳು `/translations/<lang-code>/` ಡೈರೆಕ್ಟರಿಗಳಲ್ಲಿ ಇವೆ
- GitHub Actions ಕಾರ್ಯವಾಹಿಯು ಅನುವಾದ ನವೀಕರಣಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ
- ಮೂಲ ಫೈಲ್‌ಗಳು ಕೋಡ್ ರೂಟ್‌ನಲ್ಲಿ ಇಂಗ್ಲೀಷ್‌ನಲ್ಲಿವೆ

### ಪಾಠ ರಚನೆ

ಪ್ರತಿ ಪಾಠ ನಿಯಮಿತ ಮಾದರಿಯನ್ನು ಅನುಸರಿಸುತ್ತದೆ:
1. ವೀಡಿಯೋ ಥಂಬ್ನೇಲ್ ಲಿಂಕ್ ಜೊತೆಗೆ
2. ಬರಹದ ಪಾಠ ವಿಷಯ (README.md)
3. ಹಲವು ಫ್ರೇಮ್‌ವರ್ಕ್‌ನಲ್ಲಿ ಕೋಡ್ ಮಾದರಿಗಳು
4. ಕಲಿಕಾ ಉದ್ದೇಶಗಳು ಮತ್ತು ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು
5. ಹೆಚ್ಚುವರಿ ಕಲಿಕೆಯ ಸಂಪನ್ಮೂಲಗಳ ಲಿಂಕ್

### ಕೋಡ್ ಮಾದರಿ ಹೆಸರಿಸುವಿಕೆ

ರೂಪ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - ಪಾಠ 1, MAF Python
- `14-sequential.ipynb` - ಪಾಠ 14, MAF ಅಗ್ರಗಣ್ಯ ಮಾದರಿಗಳು

### ವಿಶೇಷ ಡೈರೆಕ್ಟರಿಗಳು

- `translated_images/` - ಅನುವಾದಕ್ಕಾಗಿ ಸ್ಥಳೀಯಕೃತ ಚಿತ್ರಗಳು
- `images/` - ಮೂಲ ಇಂಗ್ಲೀಷ್ ಚಿತ್ರಗಳು
- `.devcontainer/` - VS Code ಅಭಿವೃದ್ಧಿ ಕಂಟೈನರ್ ಸಂರಚನೆ
- `.github/` - GitHub Actions ಕಾರ್ಯವಾಹಿಗಳು ಮತ್ತು ಟೆಂಪ್ಲೇಟುಗಳು

### ಅವಲಂಬನೆಗಳು

`requirements.txt` ನ ಪ್ರಮುಖ ಪ್ಯಾಕೇಜುಗಳು:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - ಏಜೆಂಟ್-ಟು-ಏಜೆಂಟ್ ಪ್ರೋಟೋಕಾಲ್ ಬೆಂಬಲ
- `azure-ai-inference`, `azure-ai-projects` - Azure AI ಸೇವೆಗಳು
- `azure-identity` - Azure ಪ್ರಾಮಾಣೀಕರಣ (AzureCliCredential)
- `azure-search-documents` - Azure AI Search ಇಂಟಿಗ್ರೇಷನ್
- `mcp[cli]` - Model Context Protocol ಬೆಂಬಲ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ನೀವು ಸೂಚನೆ ನೀಡಿರುವ ಡಾಕ್ಯುಮೆಂಟ್‌ನ ಕನ್ನಡ ಅನುವಾದ:**

**ಇತರೆ ಮಾಹಿತಿ**:  
ಈ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಸರಿಯಾದ ಅನುವಾದಕ್ಕೆ ಪ್ರಯತ್ನಿಸುವುದಾದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುಗಳಿರಬಹುದು ಎಂಬುದನ್ನು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಸೂಕ್ತ ಮತ್ತು ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುನಿರ್ವಹಣೆ ಅಥವಾ ತಪ್ಪಾಗಿ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆಯ ಸಂಬಂಧದಲ್ಲಿ ನಾವು ಜವಾಬ್ದಾರಿಯಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->