# AGENTS.md

## ਪ੍ਰੋਜੈਕਟ ਝਲਕ

ਇਹ ਰਿਪੋਜ਼ਟਰੀ "AI Agents for Beginners" ਨੂੰ ਸ਼ਾਮਲ ਕਰਦੀ ਹੈ - ਇੱਕ ਵਿਸਤ੍ਰਿਤ ਸ਼ਿਕਸ਼ਣ ਕੋਰਸ ਜੋ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਲੋੜੀਂਦੇ ਸਾਰੇ ਗੁਣ ਸਿਖਾਉਂਦਾ ਹੈ। ਕੋਰਸ ਵਿੱਚ 15+ ਪਾਠ ਸ਼ਾਮਲ ਹਨ ਜੋ ਮੂਲ ਭਾਗਾਂ, ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ, ਫਰੇਮਵਰਕ ਅਤੇ AI ਏਜੰਟਾਂ ਦੀ ਉਤਪਾਦਨ ਤੈਨਾਤੀ ਨੂੰ ਕਵਰ ਕਰਦੇ ਹਨ।

**ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ:**
- Python 3.12+
- ਇੰਟਰਐਕਟਿਵ ਸਿਖਲਾਈ ਲਈ Jupyter Notebooks
- AI ਫਰੇਮਵਰਕ: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI ਸੇਵਾਵਾਂ: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (ਮੁਫ਼ਤ ਟੀਅਰ ਉਪਲਬਧ)

**ਆਰਕੀਟੈਕਚਰ:**
- ਪਾਠ-ਅਧਾਰਿਤ ਬਣਤਰ (00-15+ ਡਾਇਰੈਕਟਰੀਜ਼)
- ਹਰ ਪਾਠ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ: README ਦਸਤਾਵੇਜ਼, ਕੋਡ ਨਮੂਨੇ (Jupyter notebooks), ਅਤੇ ਚਿੱਤਰ
- ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ ਰਾਹੀਂ ਬਹੁ-ਭਾਸ਼ਾ ਸਹਾਇਤਾ
- ਹਰ ਪਾਠ ਲਈ ਕਈ ਫਰੇਮਵਰਕ ਵਿਕਲਪ (Semantic Kernel, AutoGen, Azure AI Agent Service)

## ਸੈਟਅਪ ਕਮਾਂਡ

### ਪੂਰਵ ਸ਼ਰਤਾਂ
- Python 3.12 ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ
- GitHub ਖਾਤਾ (GitHub Models - ਮੁਫ਼ਤ ਟੀਅਰ ਲਈ)
- Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ (ਵਿਕਲਪਿਕ, Azure AI ਸੇਵਾਵਾਂ ਲਈ)

### ਸ਼ੁਰੂਆਤੀ ਸੈਟਅਪ

1. **ਰਿਪੋਜ਼ਟਰੀ ਕਲੋਨ ਜਾਂ ਫੋਰਕ ਕਰੋ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ ਐਕਟੀਵੇਟ ਕਰੋ:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Dependencies ਇੰਸਟਾਲ ਕਰੋ:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈਟ ਕਰੋ:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### ਲੋੜੀਂਦੇ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

**GitHub Models (ਮੁਫ਼ਤ)** ਲਈ:
- `GITHUB_TOKEN` - GitHub ਤੋਂ Personal access token

**Azure AI ਸੇਵਾਵਾਂ** (ਵਿਕਲਪਿਕ) ਲਈ:
- `PROJECT_ENDPOINT` - Azure AI Foundry ਪ੍ਰੋਜੈਕਟ ਐਂਡਪੌਇੰਟ
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API ਕੁੰਜੀ
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI ਐਂਡਪੌਇੰਟ URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - ਚੈਟ ਮਾਡਲ ਲਈ ਡਿਪਲੌਇਮੈਂਟ ਨਾਮ
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - ਐਮਬੈਡਿੰਗ ਲਈ ਡਿਪਲੌਇਮੈਂਟ ਨਾਮ
- `.env.example` ਵਿੱਚ ਦਿਖਾਈ ਗਈ ਵਾਧੂ Azure ਸੰਰਚਨਾ

## ਵਿਕਾਸ ਵਰਕਫਲੋ

### Jupyter Notebooks ਚਲਾਉਣਾ

ਹਰ ਪਾਠ ਵਿੱਚ ਵੱਖ-ਵੱਖ ਫਰੇਮਵਰਕ ਲਈ ਕਈ Jupyter notebooks ਸ਼ਾਮਲ ਹਨ:

1. **Jupyter ਸ਼ੁਰੂ ਕਰੋ:**
   ```bash
   jupyter notebook
   ```

2. **ਕਿਸੇ ਪਾਠ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ** (ਜਿਵੇਂ `01-intro-to-ai-agents/code_samples/`)

3. **Notebooks ਖੋਲ੍ਹੋ ਅਤੇ ਚਲਾਓ:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel ਫਰੇਮਵਰਕ ਵਰਤ ਕੇ
   - `*-autogen.ipynb` - AutoGen ਫਰੇਮਵਰਕ ਵਰਤ ਕੇ
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) ਵਰਤ ਕੇ
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) ਵਰਤ ਕੇ
   - `*-azureaiagent.ipynb` - Azure AI Agent Service ਵਰਤ ਕੇ

### ਵੱਖ-ਵੱਖ ਫਰੇਮਵਰਕ ਨਾਲ ਕੰਮ ਕਰਨਾ

**Semantic Kernel + GitHub Models:**
- GitHub ਖਾਤੇ ਨਾਲ ਮੁਫ਼ਤ ਟੀਅਰ ਉਪਲਬਧ
- ਸਿਖਲਾਈ ਅਤੇ ਪ੍ਰਯੋਗ ਲਈ ਵਧੀਆ
- ਫਾਈਲ ਪੈਟਰਨ: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- GitHub ਖਾਤੇ ਨਾਲ ਮੁਫ਼ਤ ਟੀਅਰ ਉਪਲਬਧ
- ਬਹੁ-ਏਜੰਟ ਆਰਕੇਸਟ੍ਰੇਸ਼ਨ ਸਮਰੱਥਾ
- ਫਾਈਲ ਪੈਟਰਨ: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoft ਦਾ ਨਵਾਂ ਫਰੇਮਵਰਕ
- Python ਅਤੇ .NET ਵਿੱਚ ਉਪਲਬਧ
- ਫਾਈਲ ਪੈਟਰਨ: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਦੀ ਲੋੜ ਹੈ
- ਉਤਪਾਦਨ-ਤਿਆਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ
- ਫਾਈਲ ਪੈਟਰਨ: `*-azureaiagent.ipynb`

## ਟੈਸਟਿੰਗ ਹਦਾਇਤਾਂ

ਇਹ ਇੱਕ ਸ਼ਿਕਸ਼ਣ ਰਿਪੋਜ਼ਟਰੀ ਹੈ ਜਿਸ ਵਿੱਚ ਉਦਾਹਰਣ ਕੋਡ ਹੈ, ਨਾ ਕਿ ਆਟੋਮੈਟਿਕ ਟੈਸਟਾਂ ਵਾਲਾ ਉਤਪਾਦਨ ਕੋਡ। ਆਪਣੀ ਸੈਟਅਪ ਅਤੇ ਬਦਲਾਅ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਲਈ:

### ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ

1. **Python ਵਾਤਾਵਰਣ ਟੈਸਟ ਕਰੋ:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Notebook ਚਲਾਉਣ ਦੀ ਜਾਂਚ ਕਰੋ:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### ਵਿਅਕਤੀਗਤ Notebooks ਚਲਾਉਣਾ

Notebooks ਨੂੰ Jupyter ਵਿੱਚ ਖੋਲ੍ਹੋ ਅਤੇ ਸੈਲਾਂ ਨੂੰ ਲਗਾਤਾਰ ਚਲਾਓ। ਹਰ Notebook ਸਵੈ-ਨਿਰਭਰ ਹੈ ਅਤੇ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ:
- Import statements
- ਸੰਰਚਨਾ ਲੋਡ ਕਰਨਾ
- ਉਦਾਹਰਣ ਏਜੰਟ ਅਮਲ
- Markdown ਸੈਲਾਂ ਵਿੱਚ ਉਮੀਦ ਕੀਤੇ ਨਤੀਜੇ

## ਕੋਡ ਸ਼ੈਲੀ

### Python ਸੰਕਲਪ

- **Python ਵਰਜਨ**: 3.12+
- **ਕੋਡ ਸ਼ੈਲੀ**: ਮਿਆਰੀ Python PEP 8 ਸੰਕਲਪਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ
- **Notebooks**: ਸੰਕਲਪਾਂ ਨੂੰ ਸਮਝਾਉਣ ਲਈ ਸਪਸ਼ਟ Markdown ਸੈਲਾਂ ਵਰਤੋ
- **Imports**: ਮਿਆਰੀ ਲਾਇਬ੍ਰੇਰੀ, ਤੀਜੀ-ਪਾਰਟੀ, ਸਥਾਨਕ ਇੰਪੋਰਟਾਂ ਦੁਆਰਾ ਸਮੂਹ ਬਣਾਓ

### Jupyter Notebook ਸੰਕਲਪ

- ਕੋਡ ਸੈਲਾਂ ਤੋਂ ਪਹਿਲਾਂ ਵਰਣਾਤਮਕ Markdown ਸੈਲਾਂ ਸ਼ਾਮਲ ਕਰੋ
- ਸੰਦਰਭ ਲਈ Notebook ਵਿੱਚ ਨਤੀਜਿਆਂ ਦੇ ਉਦਾਹਰਣ ਸ਼ਾਮਲ ਕਰੋ
- ਪਾਠ ਸੰਕਲਪਾਂ ਨਾਲ ਮੇਲ ਖਾਣ ਵਾਲੇ ਸਪਸ਼ਟ ਵੈਰੀਏਬਲ ਨਾਮ ਵਰਤੋ
- Notebook ਚਲਾਉਣ ਦੀ ਕ੍ਰਮਬੱਧਤਾ ਰੱਖੋ (ਸੈਲ 1 → 2 → 3...)

### ਫਾਈਲ ਸੰਗਠਨ

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

## ਬਣਾਉ ਅਤੇ ਤੈਨਾਤੀ

### ਦਸਤਾਵੇਜ਼ ਬਣਾਉਣਾ

ਇਹ ਰਿਪੋਜ਼ਟਰੀ ਦਸਤਾਵੇਜ਼ ਲਈ Markdown ਵਰਤਦੀ ਹੈ:
- ਹਰ ਪਾਠ ਫੋਲਡਰ ਵਿੱਚ README.md ਫਾਈਲਾਂ
- ਰਿਪੋਜ਼ਟਰੀ ਰੂਟ 'ਤੇ ਮੁੱਖ README.md
- GitHub Actions ਰਾਹੀਂ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ

### CI/CD ਪਾਈਪਲਾਈਨ

`.github/workflows/` ਵਿੱਚ ਸਥਿਤ:

1. **co-op-translator.yml** - 50+ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ
2. **welcome-issue.yml** - ਨਵੇਂ issue ਬਣਾਉਣ ਵਾਲਿਆਂ ਦਾ ਸਵਾਗਤ ਕਰਦਾ ਹੈ
3. **welcome-pr.yml** - ਨਵੇਂ pull request ਯੋਗਦਾਨਕਰਤਾਵਾਂ ਦਾ ਸਵਾਗਤ ਕਰਦਾ ਹੈ

### ਤੈਨਾਤੀ

ਇਹ ਇੱਕ ਸ਼ਿਕਸ਼ਣ ਰਿਪੋਜ਼ਟਰੀ ਹੈ - ਕੋਈ ਤੈਨਾਤੀ ਪ੍ਰਕਿਰਿਆ ਨਹੀਂ। ਉਪਭੋਗਤਾ:
1. ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਫੋਰਕ ਜਾਂ ਕਲੋਨ ਕਰੋ
2. Notebooks ਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਜਾਂ GitHub Codespaces ਵਿੱਚ ਚਲਾਓ
3. ਉਦਾਹਰਣਾਂ ਨੂੰ ਸੋਧ ਕੇ ਅਤੇ ਪ੍ਰਯੋਗ ਕਰਕੇ ਸਿੱਖੋ

## Pull Request ਹਦਾਇਤਾਂ

### ਜਮ੍ਹਾਂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

1. **ਆਪਣੇ ਬਦਲਾਅ ਦੀ ਜਾਂਚ ਕਰੋ:**
   - ਪ੍ਰਭਾਵਿਤ Notebooks ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਚਲਾਓ
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਾਰੇ ਸੈਲ ਬਿਨਾਂ ਗਲਤੀਆਂ ਦੇ ਚਲਦੇ ਹਨ
   - ਨਤੀਜੇ ਸਹੀ ਹਨ ਇਹ ਜਾਂਚੋ

2. **ਦਸਤਾਵੇਜ਼ ਅਪਡੇਟ:**
   - ਨਵੇਂ ਸੰਕਲਪ ਸ਼ਾਮਲ ਕਰਨ 'ਤੇ README.md ਅਪਡੇਟ ਕਰੋ
   - ਜਟਿਲ ਕੋਡ ਲਈ Notebooks ਵਿੱਚ ਟਿੱਪਣੀਆਂ ਸ਼ਾਮਲ ਕਰੋ
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ Markdown ਸੈਲਾਂ ਉਦੇਸ਼ ਨੂੰ ਸਮਝਾਉਂਦੀਆਂ ਹਨ

3. **ਫਾਈਲ ਬਦਲਾਅ:**
   - `.env` ਫਾਈਲਾਂ ਨੂੰ ਕਮਿਟ ਕਰਨ ਤੋਂ ਬਚੋ (`.env.example` ਵਰਤੋ)
   - `venv/` ਜਾਂ `__pycache__/` ਡਾਇਰੈਕਟਰੀਜ਼ ਨੂੰ ਕਮਿਟ ਨਾ ਕਰੋ
   - ਜਦੋਂ ਉਹ ਸੰਕਲਪ ਦਿਖਾਉਂਦੇ ਹਨ ਤਾਂ Notebook ਨਤੀਜੇ ਰੱਖੋ
   - ਅਸਥਾਈ ਫਾਈਲਾਂ ਅਤੇ ਬੈਕਅਪ Notebooks (`*-backup.ipynb`) ਹਟਾਓ

### PR ਸਿਰਲੇਖ ਫਾਰਮੈਟ

ਵਰਣਾਤਮਕ ਸਿਰਲੇਖ ਵਰਤੋ:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### ਲੋੜੀਂਦੇ ਜਾਂਚ

- Notebooks ਗਲਤੀਆਂ ਤੋਂ ਬਿਨਾਂ ਚਲਣੇ ਚਾਹੀਦੇ ਹਨ
- README ਫਾਈਲਾਂ ਸਪਸ਼ਟ ਅਤੇ ਸਹੀ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ
- ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਮੌਜੂਦ ਕੋਡ ਪੈਟਰਨ ਦੀ ਪਾਲਣਾ ਕਰੋ
- ਹੋਰ ਪਾਠਾਂ ਨਾਲ ਸਥਿਰਤਾ ਬਣਾਈ ਰੱਖੋ

## ਵਾਧੂ ਟਿੱਪਣੀਆਂ

### ਆਮ ਗਲਤੀਆਂ

1. **Python ਵਰਜਨ ਅਸੰਗਤਤਾ:**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ Python 3.12+ ਵਰਤਿਆ ਜਾ ਰਿਹਾ ਹੈ
   - ਕੁਝ ਪੈਕੇਜ ਪੁਰਾਣੀਆਂ ਵਰਜਨਾਂ ਨਾਲ ਕੰਮ ਨਹੀਂ ਕਰਦੇ
   - `python3 -m venv` ਵਰਤ ਕੇ Python ਵਰਜਨ ਸਪਸ਼ਟ ਕਰੋ

2. **ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ:**
   - ਹਮੇਸ਼ਾ `.env.example` ਤੋਂ `.env` ਬਣਾਓ
   - `.env` ਫਾਈਲ ਨੂੰ ਕਮਿਟ ਨਾ ਕਰੋ (ਇਹ `.gitignore` ਵਿੱਚ ਹੈ)
   - GitHub token ਨੂੰ ਉਚਿਤ ਅਧਿਕਾਰਾਂ ਦੀ ਲੋੜ ਹੈ

3. **ਪੈਕੇਜ ਸੰਘਰਸ਼:**
   - ਨਵੇਂ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਦੀ ਵਰਤੋਂ ਕਰੋ
   - `requirements.txt` ਤੋਂ ਇੰਸਟਾਲ ਕਰੋ ਨਾ ਕਿ ਵਿਅਕਤੀਗਤ ਪੈਕੇਜ
   - ਕੁਝ Notebooks ਵਿੱਚ ਉਨ੍ਹਾਂ ਦੇ Markdown ਸੈਲਾਂ ਵਿੱਚ ਵਾਧੂ ਪੈਕੇਜ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ

4. **Azure ਸੇਵਾਵਾਂ:**
   - Azure AI ਸੇਵਾਵਾਂ ਲਈ ਸਰਗਰਮ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਦੀ ਲੋੜ ਹੈ
   - ਕੁਝ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਖੇਤਰ-ਵਿਸ਼ੇਸ਼ ਹਨ
   - GitHub Models ਲਈ ਮੁਫ਼ਤ ਟੀਅਰ ਸੀਮਾਵਾਂ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ

### ਸਿਖਲਾਈ ਪਾਠ

ਪਾਠਾਂ ਦੁਆਰਾ ਸਿਧੇ ਤੌਰ 'ਤੇ ਅਗੇ ਵਧਣ ਦੀ ਸਿਫਾਰਸ਼:
1. **00-course-setup** - ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਲਈ ਇੱਥੇ ਸ਼ੁਰੂ ਕਰੋ
2. **01-intro-to-ai-agents** - AI ਏਜੰਟ ਮੂਲ ਭਾਗਾਂ ਨੂੰ ਸਮਝੋ
3. **02-explore-agentic-frameworks** - ਵੱਖ-ਵੱਖ ਫਰੇਮਵਰਕ ਬਾਰੇ ਸਿੱਖੋ
4. **03-agentic-design-patterns** - ਮੁੱਖ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ
5. ਗਿਣਤੀਵਾਰ ਪਾਠਾਂ ਦੁਆਰਾ ਅਗੇ ਵਧੋ

### ਫਰੇਮਵਰਕ ਚੋਣ

ਆਪਣੇ ਲਕਸ਼ਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਫਰੇਮਵਰਕ ਚੁਣੋ:
- **ਸਿਖਲਾਈ/ਪ੍ਰੋਟੋਟਾਈਪਿੰਗ**: Semantic Kernel + GitHub Models (ਮੁਫ਼ਤ)
- **ਬਹੁ-ਏਜੰਟ ਪ੍ਰਣਾਲੀ**: AutoGen
- **ਤਾਜ਼ਾ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ**: Microsoft Agent Framework (MAF)
- **ਉਤਪਾਦਨ ਤੈਨਾਤੀ**: Azure AI Agent Service

### ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ

- [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord) ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ
- ਵਿਸ਼ੇਸ਼ ਮਦਦ ਲਈ ਪਾਠ README ਫਾਈਲਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ
- ਮੁੱਖ [README.md](./README.md) ਵਿੱਚ ਕੋਰਸ ਝਲਕ ਦੀ ਜਾਂਚ ਕਰੋ
- ਵਿਸ਼ਤ੍ਰਿਤ ਸੈਟਅਪ ਹਦਾਇਤਾਂ ਲਈ [Course Setup](./00-course-setup/README.md) ਨੂੰ ਦੇਖੋ

### ਯੋਗਦਾਨ

ਇਹ ਇੱਕ ਖੁੱਲ੍ਹਾ ਸ਼ਿਕਸ਼ਣ ਪ੍ਰੋਜੈਕਟ ਹੈ। ਯੋਗਦਾਨ ਸਵਾਗਤ:
- ਕੋਡ ਉਦਾਹਰਣਾਂ ਨੂੰ ਸੁਧਾਰੋ
- ਟਾਈਪੋ ਜਾਂ ਗਲਤੀਆਂ ਨੂੰ ਠੀਕ ਕਰੋ
- ਸਪਸ਼ਟ ਟਿੱਪਣੀਆਂ ਸ਼ਾਮਲ ਕਰੋ
- ਨਵੇਂ ਪਾਠ ਵਿਸ਼ਿਆਂ ਦਾ ਸੁਝਾਅ ਦਿਓ
- ਵਾਧੂ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ

[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) ਵਿੱਚ ਮੌਜੂਦਾ ਜ਼ਰੂਰਤਾਂ ਦੇਖੋ।

## ਪ੍ਰੋਜੈਕਟ-ਵਿਸ਼ੇਸ਼ ਸੰਦਰਭ

### ਬਹੁ-ਭਾਸ਼ਾ ਸਹਾਇਤਾ

ਇਹ ਰਿਪੋਜ਼ਟਰੀ ਇੱਕ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ ਵਰਤਦੀ ਹੈ:
- 50+ ਭਾਸ਼ਾਵਾਂ ਸਹਾਇਤਿਤ
- `/translations/<lang-code>/` ਡਾਇਰੈਕਟਰੀਜ਼ ਵਿੱਚ ਅਨੁਵਾਦ
- GitHub Actions ਵਰਕਫਲੋ ਅਨੁਵਾਦ ਅਪਡੇਟਾਂ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ
- ਮੂਲ ਫਾਈਲਾਂ ਰਿਪੋਜ਼ਟਰੀ ਰੂਟ 'ਤੇ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਹਨ

### ਪਾਠ ਬਣਤਰ

ਹਰ ਪਾਠ ਇੱਕ ਸਥਿਰ ਪੈਟਰਨ ਦੀ ਪਾਲਣਾ ਕਰਦਾ ਹੈ:
1. ਵੀਡੀਓ ਥੰਬਨੇਲ ਨਾਲ ਲਿੰਕ
2. ਲਿਖਤ ਪਾਠ ਸਮੱਗਰੀ (README.md)
3. ਕਈ ਫਰੇਮਵਰਕ ਵਿੱਚ ਕੋਡ ਨਮੂਨੇ
4. ਸਿਖਲਾਈ ਦੇ ਉਦੇਸ਼ ਅਤੇ ਪੂਰਵ ਸ਼ਰਤਾਂ
5. ਵਾਧੂ ਸਿਖਲਾਈ ਸਰੋਤ ਲਿੰਕ ਕੀਤੇ

### ਕੋਡ ਨਮੂਨਾ ਨਾਮਕਰਨ

ਫਾਰਮੈਟ: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - ਪਾਠ 4, Semantic Kernel
- `07-autogen.ipynb` - ਪਾਠ 7, AutoGen
- `14-python-agent-framework.ipynb` - ਪਾਠ 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - ਪਾਠ 14, MAF .NET

### ਵਿਸ਼ੇਸ਼ ਡਾਇਰੈਕਟਰੀਜ਼

- `translated_images/` - ਅਨੁਵਾਦ ਲਈ ਸਥਾਨਕ ਚਿੱਤਰ
- `images/` - ਅੰਗਰੇਜ਼ੀ ਸਮੱਗਰੀ ਲਈ ਮੂਲ ਚਿੱਤਰ
- `.devcontainer/` - VS Code ਵਿਕਾਸ ਕੰਟੇਨਰ ਸੰਰਚਨਾ
- `.github/` - GitHub Actions ਵਰਕਫਲੋ ਅਤੇ ਟੈਂਪਲੇਟ

### Dependencies

`requirements.txt` ਤੋਂ ਮੁੱਖ ਪੈਕੇਜ:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen ਫਰੇਮਵਰਕ
- `semantic-kernel` - Semantic Kernel ਫਰੇਮਵਰਕ
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI ਸੇਵਾਵਾਂ
- `azure-search-doc

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਅਸਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।