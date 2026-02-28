# AGENTS.md

## ਪ੍ਰੋਜੈਕਟ ਓਵਰਵਿਊ

ਇਸ ਰਿਪੋਸਟਰੀ ਵਿੱਚ "ਬਿਗਿਨਰਜ਼ ਲਈ AI ਏਜੰਟਸ" ਸ਼ਾਮਿਲ ਹਨ - ਇੱਕ ਵਿਸ਼ਤ੍ਰਿਤ ਸਿੱਖਿਆਕਰਮ ਜੋ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਜਰੂਰੀ ਹਰ ਚੀਜ਼ ਸਿਖਾਉਂਦਾ ਹੈ। ਕੋਰਸ ਵਿੱਚ 15+ ਪਾਠ ਸ਼ਾਮਿਲ ਹਨ ਜੋ ਮੂਲਭੂਤ, ਡਿਜ਼ਾਇਨ ਪੈਟਰਨ, ਫ੍ਰੇਮਵਰਕਸ ਅਤੇ AI ਏਜੰਟਸ ਦੀ ਪ੍ਰੋਡਕਸ਼ਨ ਡਿਪਲੋਯਮੈਂਟ ਨੂੰ ਕਵਰ ਕਰਦੇ ਹਨ।

**ਮੁੱਖ ਤਕਨਾਲੋਜੀਜ਼:**
- Python 3.12+
- ਇੰਟਰਐਕਟਿਵ ਸਿੱਖਣ ਲਈ Jupyter ਨੋਟਬੁੱਕਸ
- AI ਫ੍ਰੇਮਵਰਕਸ: Microsoft Agent Framework (MAF)
- Azure AI ਸੇਵਾਵਾਂ: Microsoft Foundry, Azure AI Foundry Agent Service V2

**ਆਰਕੀਟੈਕਚਰ:**
- ਪਾਠ-ਆਧਾਰਿਤ ਸਟ੍ਰਕਚਰ (00-15+ ਡਾਇਰੈਕਟਰੀਆਂ)
- ਹਰ ਪਾਠ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹਨ: README ਦਸਤਾਵੇਜ਼ੀ, ਕੋਡ ਨਮੂਨੇ (Jupyter ਨੋਟਬੁੱਕਸ), ਅਤੇ ਚਿੱਤਰ
- ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ ਰਾਹੀਂ ਬਹੁ-ਭਾਸ਼ਾਈ ਸਹਾਇਤਾ
- ਹਰ ਪਾਠ ਲਈ ਇੱਕ Python ਨੋਟਬੁੱਕ ਜੋ Microsoft Agent Framework ਵਰਤਦਾ ਹੈ

## ਸੈਟਅਪ ਕਮਾਂਡਜ਼

### ਜ਼ਰੂਰੀ ਸ਼ਰਤਾਂ
- Python 3.12 ਜਾਂ ਉਪਰ
- Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ (Azure AI Foundry ਲਈ)
- Azure CLI ਇੰਸਟਾਲ ਅਤੇ ਪ੍ਰਮਾਣਿਤ (`az login`)

### ਸ਼ੁਰੂਆਤੀ ਸੈਟਅਪ

1. **ਰਿਪੋਸਟਰੀ ਕਲੋਨ ਜਾਂ ਫੋਰਕ ਕਰੋ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ਜਾਂ
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ ਸਰਗਰਮ ਕਰੋ:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # ਵਿੰਡੋਜ਼ 'ਤੇ: venv\Scripts\activate
   ```

3. **ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰੋ:**
   ```bash
   cp .env.example .env
   # ਆਪਣੇ API ਕੁੰਜੀਆਂ ਅਤੇ ਐਂਡਪੌਇੰਟਾਂ ਨਾਲ .env ਨੂੰ ਸੰਪਾਦਿਤ ਕਰੋ
   ```

### ਜ਼ਰੂਰੀ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ

**Azure AI Foundry** ਲਈ (ਲਾਜ਼ਮੀ):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry ਪ੍ਰੋਜੈਕਟ ਐਂਡਪੋਇੰਟ
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - ਮਾਡਲ ਡਿਪਲੋਯਮੈਂਟ ਨਾਮ (ਜਿਵੇਂ ਕਿ gpt-4o)

**Azure AI Search** ਲਈ (ਪਾਠ 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search ਐਂਡਪੋਇੰਟ
- `AZURE_SEARCH_API_KEY` - Azure AI Search API ਕੁੰਜੀ

ਪ੍ਰਮਾਣੀਕਰਣ: ਨੋਟਬੁੱਕਸ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ `az login` ਚਲਾਓ (`AzureCliCredential` ਵਰਤਦਾ ਹੈ)।

## ਵਿਕਾਸ ਕਿਰਿਆਵਲੀ

### Jupyter ਨੋਟਬੁੱਕਸ ਚਲਾਉਣਾ

ਹਰ ਪਾਠ ਵਿੱਚ ਵੱਖ-ਵੱਖ ਫ੍ਰੇਮਵਰਕ ਲਈ ਬਹੁਤ ਸਾਰੇ Jupyter ਨੋਟਬੁੱਕ ਹਨ:

1. **Jupyter ਸ਼ੁਰੂ ਕਰੋ:**
   ```bash
   jupyter notebook
   ```

2. **ਪਾਠ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ** (ਉਦਾਹਰਨ ਲਈ, `01-intro-to-ai-agents/code_samples/`)

3. **ਨੋਟਬੁੱਕ ਖੋਲ੍ਹੋ ਅਤੇ ਚਲਾਓ:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) ਵਰਤ ਕੇ
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) ਵਰਤ ਕੇ

### Microsoft Agent Framework ਨਾਲ ਕੰਮ ਕਰਨਾ

**Microsoft Agent Framework + Azure AI Foundry:**
- Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ
- Agent Service V2 ਲਈ `AzureAIProjectAgentProvider` ਵਰਤਦਾ ਹੈ (foundry ਪੋਰਟਲ ਵਿੱਚ ਏਜੰਟਸ ਦਿੱਖਦੇ ਹਨ)
- ਬਿਲਟ-ਇਨ ਨਜ਼ਰੀਅਤ ਸਮੇਤ ਪ੍ਰੋਡਕਸ਼ਨ-ਤੈਯਾਰ
- ਫਾਇਲ ਨਮੂਨਾ: `*-python-agent-framework.ipynb`

## ਟੈਸਟਿੰਗ ਹਿਦਾਇਤਾਂ

ਇਹ ਇੱਕ ਸਿੱਖਿਆਕਰਮ ਰਿਪੋਸਟਰੀ ਹੈ ਜਿਸ ਵਿੱਚ ਮਿਸਾਲੀ ਕੋਡ ਹੈ ਪਰ ਪ੍ਰੋਡਕਸ਼ਨ ਕੋਡ ਜਾਂ ਆਟੋਮੈਟਿਕ ਟੈਸਟ ਨਹੀ ਹਨ। ਆਪਣੀ ਸੈਟਅਪ ਅਤੇ ਬਦਲਾਅ ਦੀ ਜਾਂਚ ਲਈ:

### ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ

1. **Python ਵਾਤਾਵਰਣ ਦੀ ਜਾਂਚ ਕਰੋ:**
   ```bash
   python --version  # 3.12+ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **ਨੋਟਬੁੱਕ ਲਾਗੂਗੀਰੀ ਟੈਸਟ ਕਰੋ:**
   ```bash
   # ਨੋਟਬੁੱਕ ਨੂੰ ਸਕ੍ਰਿਪਟ ਵਿੱਚ ਬਦਲੋ ਅਤੇ ਚਲਾਓ (ਟੈਸਟਾਂ ਦੇ ਇੰਪੋਰਟ)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### ਵੱਖਰੇ ਨੋਟਬੁੱਕ ਚਲਾਉਣਾ

Jupyter ਵਿੱਚ ਨੋਟਬੁੱਕ ਖੋਲ੍ਹੋ ਅਤੇ ਸੈੱਲਾਂ ਨੂੰ ਲੜੀਵਾਰ ਚਲਾਓ। ਹਰ ਨੋਟਬੁੱਕ ਖੁਦਮੁਖਤਿਆਰ ਹੈ ਅਤੇ ਸ਼ਾਮਿਲ ਹੈ:
- ਆਯਾਤ ਬਿਆਨ
- ਸੰਰਚਨਾ ਲੋਡ ਕਰਨਾ
- ਉਦਾਹਰਣ ਏਜੰਟ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ
- ਮਾਰਕਡਾਊਨ ਸੈੱਲਾਂ ਵਿੱਚ ਉਮੀਦਵਾਰ ਨਤੀਜੇ

## ਕੋਡ ਅੰਦਾਜ਼

### Python ਰਿਵਾਜ਼

- **Python ਵਰਜ਼ਨ**: 3.12+
- **ਕੋਡ ਅੰਦਾਜ਼**: ਸਧਾਰਣ Python PEP 8 ਨਿਯਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ
- **ਨੋਟਬੁੱਕਸ**: ਸਪਸ਼ਟ ਮਾਰਕਡਾਊਨ ਸੈੱਲ ਵਿਕਲਪਾਓਂ ਸਮਝਾਅ ਲਈ
- **ਆਯਾਤ**: ਮਿਆਰੀ ਲਾਇਬ੍ਰੇਰੀ, ਤੀਜੀ ਪੱਖ, ਲੋਕਲ ਆਯਾਤ ਵਿੱਚ ਸਮੂਹਬੱਧ ਕਰੋ

### Jupyter ਨੋਟਬੁੱਕ ਰਿਵਾਜ਼

- ਕੋਡ ਸੈੱਲਾਂ ਤੋਂ ਪਹਿਲਾਂ ਵਰਣਨਾਤਮਕ ਮਾਰਕਡਾਊਨ ਸੈੱਲ ਸ਼ਾਮਿਲ ਕਰੋ
- ਸੰਦਰਭ ਲਈ ਨਤੀਜਿਆਂ ਦੇ ਉਦਾਹਰਣ ਢਾਂਚੇ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰੋ
- ਪਾਠ ਦੇ ਅਰਥਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਵਰਿਅਬਲ ਨਾਮ ਵਰਤੋ
- ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਦੀ ਕ੍ਰਮਬੱਧਤਾ ਲੀਨੀਅਰ ਰੱਖੋ (ਸੈੱਲ 1 → 2 → 3...)

### ਫਾਇਲ ਸੰਗਠਨ

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## ਬਣਾਉਟ ਅਤੇ ਡਿਪਲੋਯਮੈਂਟ

### ਦਸਤਾਵੇਜ਼ੀ ਬਣਾਉਣਾ

ਇਹ ਰਿਪੋਸਟਰੀ ਦਸਤਾਵੇਜ਼ੀ ਲਈ Markdown ਉਪਯੋਗ ਕਰਦੀ ਹੈ:
- ਹਰ ਪਾਠ ਫੋਲਡਰ ਵਿੱਚ README.md ਫਾੲਲ
- ਰਿਪੋਸਟਰੀ ਰੂਟ 'ਤੇ ਮੁੱਖ README.md
- GitHub Actions ਰਾਹੀਂ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ

### CI/CD ਪਾਈਪਲਾਈਨ

ਜ਼ਪੰਜਾਬੀ `.github/workflows/` ਵਿੱਚ:

1. **co-op-translator.yml** - 50+ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ
2. **welcome-issue.yml** - ਨਵੇਂ ਮੁੱਦੇ ਬਣਾਉਣ ਵਾਲਿਆਂ ਦਾ ਸਵਾਗਤ
3. **welcome-pr.yml** - ਨਵੇਂ ਪੁੱਲ ਰਿਕਵੇਸਟ ਸਹਿਯੋਗੀਆਂ ਦਾ ਸਵਾਗਤ

### ਡਿਪਲੋਯਮੈਂਟ

ਇਹ ਸਿੱਖਿਆਕਰਮ ਰਿਪੋਸਟਰੀ ਹੈ - ਕੋਈ ਡਿਪਲੋਯਮੈਂਟ ਪ੍ਰਕਿਰਿਆ ਨਹੀਂ। ਯੂਜ਼ਰ:
1. ਰਿਪੋਸਟਰੀ ਨੂੰ ਫੋਰਕ ਜਾਂ ਕਲੋਨ ਕਰਦੇ ਹਨ
2. ਨੋਟਬੁੱਕਸ ਸਥਾਨਕ ਜਾਂ GitHub Codespaces ਵਿੱਚ ਚਲਾਉਂਦੇ ਹਨ
3. ਉਦਾਹਰਣਾਂ ਨੂੰ ਸੋਧ ਕੇ ਅਤੇ ਪ੍ਰਯੋਗ ਕਰਕੇ ਸਿੱਖਦੇ ਹਨ

## ਪੁੱਲ ਰਿਕਵੇਸਟ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼

### ਜਮ੍ਹਾ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

1. **ਤੁਹਾਡੇ ਬਦਲਾਅ ਦੀ ਜਾਂਚ:**
   - ਪ੍ਰਭਾਵਿਤ ਨੋਟਬੁੱਕਸ ਪੂਰੇ ਤੌਰ ਤੇ ਚਲਾਓ
   - ਯਕੀਨ ਕਰੋ ਸਾਰੇ ਸੈੱਲ ਬਗ਼ੈਰ ਗਲਤੀ ਦੇ ਚੱਲਦੇ ਹਨ
   - ਨਤੀਜੇ ਉਚਿਤ ਹਨ

2. **ਦਸਤਾਵੇਜ਼ੀ ਅੱਪਡੇਟ:**
   - ਨਵੀਆਂ ਸਿੱਖਿਆਵਾਂ ਜੋੜਣ 'ਤੇ README.md ਅੱਪਡੇਟ ਕਰੋ
   - ਗੁੰਝਲਦਾਰ ਕੋਡ ਲਈ ਨੋਟਬੁੱਕਸ ਵਿੱਚ ਟਿੱਪਣੀਆਂ ਸ਼ਾਮਿਲ ਕਰੋ
   - ਮਾਰਕਡਾਊਨ ਸੈੱਲਾਂ ਵਿੱਚ ਮਕਸਦ ਵਿਆਖਿਆ ਕਰੋ

3. **ਫਾਇਲ ਬਦਲਾਅ:**
   - `.env` ਫਾਇਲਾਂ ਕਮੇਟ ਨਾ ਕਰੋ (`.env.example` ਵਰਤੋ)
   - `venv/` ਜਾਂ `__pycache__/` ਫੋਲਡਰਾਂ ਨੂੰ ਕਮੇਟ ਨਾ ਕਰੋ
   - ਸੰਕਲਪ ਦਿੱਖਾਉਣ ਵਾਸਤੇ ਨੋਟਬੁੱਕ ਆਉਟਪੁੱਟ ਰੱਖੋ
   - ਅਸਥਾਈ ਫਾਇਲਾਂ ਅਤੇ ਬੈਕਅਪ ਨੋਟਬੁੱਕ ਹਟਾਓ (`*-backup.ipynb`)

### PR ਸਿਰਲੇਖ ਫਾਰਮੈਟ

ਵਰਣਨਪੂਰਕ ਸਿਰਲੇਖ ਵਰਤੋ:
- `[Lesson-XX] <concept> ਲਈ ਨਵਾਂ ਉਦਾਹਰਣ ਸ਼ਾਮਿਲ ਕਰੋ`
- `[Fix] ਪਾਠ-XX README ਵਿੱਚ ਟਾਈਪੋ ਸੁਧਾਰੋ`
- `[Update] ਪਾਠ-XX ਵਿੱਚ ਕੋਡ ਨਮੂਨਾ ਸੁਧਾਰੋ`
- `[Docs] ਸੈਟਅਪ ਹਿਦਾਇਤਾਂ ਅੱਪਡੇਟ ਕਰੋ`

### ਲਾਜ਼ਮੀ ਜਾਂਚਾਂ

- ਨੋਟਬੁੱਕ ਬਿਨਾਂ ਗਲਤੀਆਂ ਦੇ ਚੱਲੇ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ
- README ਫਾਇਲ ਸਪੱਸਟ ਅਤੇ ਸਹੀ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ
- ਰਿਪੋਸਟਰੀ ਦੇ ਮੌਜੂਦਾ ਕੋਡ ਪੈਟਰਨ ਦੀ ਪਾਲਣਾ ਕਰੋ
- ਹੋਰ ਪਾਠਾਂ ਨਾਲ ਸੰਗਤੀ ਰੱਖੋ

## ਵਧੀਕ ਨੋਟਸ

### ਆਮ ਗਲਤੀਆਂ

1. **Python ਵਰਜ਼ਨ ਦਾ ਮਿਲਾਪ ਨਾ ਹੋਣਾ:**
   - ਪੱਕਾ ਕਰੋ ਕਿ Python 3.12+ ਵਰਤਿਆ ਜਾ ਰਿਹਾ ਹੈ
   - ਕੁਝ ਪੈਕੇਜ ਪੁਰਾਣੇ ਵਰਜ਼ਨ 'ਤੇ ਕੰਮ ਨਹੀਂ ਕਰਦੇ
   - Python ਵਰਜ਼ਨ ਖਾਸ ਕਰਕੇ `python3 -m venv` ਨਾਲ ਬਣਾਓ

2. **ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ:**
   - ਹਮੇਸ਼ਾ `.env.example` ਤੋਂ `.env` ਬਣਾਓ
   - `.env` ਫਾਇਲ ਕਮੇਟ ਨਾ ਕਰੋ (ਇਹ `.gitignore` ਵਿੱਚ ਹੈ)
   - GitHub ਟੋਕਨ ਲਈ ਸਹੀ ਅਧਿਕਾਰਾਂ ਦੀ ਲੋੜ

3. **ਪੈਕੇਜ ਟਕਰਾਅ:**
   - ਨਵਾਂ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਵਰਤੋਂ
   - ਵਿਅਕਤੀਗਤ ਪੈਕੇਜਾਂ ਦੀ ਬਜਾਏ `requirements.txt` ਤੋਂ ਇੰਸਟਾਲ ਕਰੋ
   - ਕੁਝ ਨੋਟਬੁੱਕਸ ਵਿੱਚ ਹੋਰ ਪੈਕੇਜ ਜਿਨ੍ਹਾਂ ਦਾ ਉਲੇਖ ਮਾਰਕਡਾਊਨ ਸੈੱਲਾਂ ਵਿੱਚ ਹੈ

4. **Azure ਸੇਵਾਵਾਂ:**
   - Azure AI ਸੇਵਾਵਾਂ ਲਈ ਐਕਟਿਵ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਲਾਜ਼ਮੀ ਹੈ
   - ਕੁਝ ਫੀਚਰ ਖੇਤਰ-ਵਿਸ਼ੇਸ਼ ਹਨ
   - GitHub ਮਾਡਲਸ ਲਈ ਮੁਫ਼ਤ ਟੀਅਰ ਸੀਮਤੀਆਂ ਲਾਗੂ

### ਸਿੱਖਣ ਦਾ ਰਸਤਾ

ਪਾਠਾਂ ਵਿੱਚ ਸਿਧਾ ਅੱਗੇ ਵਧਣ ਦੀ ਸਿਫਾਰਸ਼:
1. **00-course-setup** - ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਲਈ ਸ਼ੁਰੂ ਕਰੋ
2. **01-intro-to-ai-agents** - AI ਏਜੰਟ ਮੂਲਭੂਤ ਸਮਝੋ
3. **02-explore-agentic-frameworks** - ਵੱਖ-ਵੱਖ ਫ੍ਰੇਮਵਰਕ ਬਾਰੇ ਜਾਨਕਾਰੀ
4. **03-agentic-design-patterns** - ਮੁੱਖ ਡਿਜ਼ਾਇਨ ਪੈਟਰਨ
5. ਲੜੀਵਾਰ ਨੰਬਰਾਂ ਵਾਲੇ ਪਾਠ ਜਾਰੀ ਰੱਖੋ

### ਫ੍ਰੇਮਵਰਕ ਚੋਣ

ਆਪਣੇ ਲਕੜੀ ਤੇ ਆਧਾਰਿਤ ਫ੍ਰੇਮਵਰਕ ਚੁਣੋ:
- **ਸਾਰੇ ਪਾਠਾਂ**: Microsoft Agent Framework (MAF) `AzureAIProjectAgentProvider` ਦੇ ਨਾਲ
- ਏਜੰਟ ਸਰਵਰ-ਸਾਈਡ ਰਜਿਸਟਰ ਕਰਦੇ ਹਨ Azure AI Foundry Agent Service V2 ਵਿੱਚ ਅਤੇ Foundry ਪੋਰਟਲ ਵਿਚ ਦਿੱਖਦੇ ਹਨ

### ਮਦਦ ਲੈਣ ਲਈ

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) 'ਚ ਸ਼ਾਮਿਲ ਹੋਵੋ
- ਖਾਸ ਹਦਾਇਤਾਂ ਲਈ ਪਾਠਾਂ ਦੇ README ਫਾਇਲ ਵੇਖੋ
- ਕੋਰਸ ਓਵਰਵਿਊ ਲਈ ਮੁੱਖ [README.md](./README.md) ਚੈੱਕ ਕਰੋ
- ਵਿਸਤ੍ਰਿਤ ਸੈਟਅਪ ਲਈ [Course Setup](./00-course-setup/README.md) ਵੇਖੋ

### ਯੋਗਦਾਨ ਪਾਉਣਾ

ਇਹ ਇੱਕ ਖੁੱਲਾ ਸਿੱਖਿਆਕਰਮ ਪ੍ਰੋਜੈਕਟ ਹੈ। ਯੋਗਦਾਨ ਤਰੂਤ:
- ਕੋਡ ਉਦਾਹਰਣ ਸੁਧਾਰੋ
- ਟਾਈਪੋ ਜਾਂ ਗਲਤੀਆਂ ਠੀਕ ਕਰੋ
- ਸਪਸ਼ਟੀਕਰਨ ਲਈ ਟਿੱਪਣੀਆਂ ਜੋੜੋ
- ਨਵੇਂ ਪਾਠ ਵਿਸ਼ਿਆਂ ਦੀ ਸਿਫਾਰਸ਼ ਕਰੋ
- ਹੋਰ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ

ਹੁਣ ਦੇ ਲੋੜੀਂਦੇ ਕੰਮ ਵੇਖਣ ਲਈ [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) ਤੇ ਜਾਓ।

## ਪ੍ਰੋਜੈਕਟ-ਵਿਸ਼ੇਸ਼ ਸੰਦਰਭ

### ਬਹੁ-ਭਾਸ਼ਾਈ ਸਹਾਇਤਾ

ਇਹ ਰਿਪੋਸਟਰੀ ਇੱਕ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ ਵਰਤਦੀ ਹੈ:
- 50+ ਭਾਸ਼ਾਵਾਂ ਦਾ ਸਮਰਥਨ
- ਅਨੁਵਾਦ `/translations/<lang-code>/` ਡਾਇਰੈਕਟਰੀਜ਼ ਵਿੱਚ
- ਅਨੁਵਾਦ ਅੱਪਡੇਟ ਲਈ GitHub Actions ਵਰਕਫਲੋ
- ਮੂਲ ਫਾਇਲਾਂ ਇੰਗਲਿਸ਼ ਵਿੱਚ ਰਿਪੋਸਟਰੀ ਰੂਟ ਤੇ

### ਪਾਠ ਸਟ੍ਰਕਚਰ

ਹਰ ਪਾਠ ਇੱਕ ਸਥਿਰ ਪੈਟਰਨ ਦੇ ਅਨੁਸਾਰ:
1. ਵੀਡੀਓ ਥੰਬਨੇਲ ਲਿੰਕ ਸਮੇਤ
2. ਲਿਖਤ ਪਾਠ ਸਮੱਗਰੀ (README.md)
3. ਕਈ ਫ੍ਰੇਮਵਰਕਸ ਵਿੱਚ ਕੋਡ ਨਮੂਨੇ
4. ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼ ਅਤੇ ਜ਼ਰੂਰੀ ਸ਼ਰਤਾਂ
5. ਵਾਧੂ ਸਿੱਖਣ ਵਾਲੇ ਸਾਧਨ ਲਿੰਕ ਕੀਤੇ ਹੋਏ

### ਕੋਡ ਸੈਂਪਲ ਨਾਮਕਰਨ

ਫਾਰਮੈਟ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - ਪਾਠ 1, MAF Python
- `14-sequential.ipynb` - ਪਾਠ 14, MAF ਅਗੇਫੇਜ਼ੀ ਪੈਟਰਨ

### ਖਾਸ ਡਾਇਰੈਕਟਰੀਜ਼

- `translated_images/` - ਅਨੁਵਾਦਾਂ ਲਈ ਸਥਾਨਕ ਚਿੱਤਰ
- `images/` - ਅਸਲੀ ਚਿੱਤਰ ਇੰਗਲਿਸ਼ ਸਮੱਗਰੀ ਲਈ
- `.devcontainer/` - VS Code ਡਿਵੈਲਪਮੈਂਟ ਕੰਟੇਨਰ ਸੰਰਚਨਾ
- `.github/` - GitHub Actions ਵਰਕਫਲੋ ਅਤੇ ਟੈਮਪਲੇਟ

### ਡਿਪੈਂਡੈਂਸੀਜ਼

`requirements.txt` ਤੋਂ ਮੁੱਖ ਪੈਕੇਜ:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - ਏਜੰਟ-ਟੂ-ਏਜੰਟ ਪ੍ਰੋਟੋਕੋਲ ਸਹਾਇਤਾ
- `azure-ai-inference`, `azure-ai-projects` - Azure AI ਸੇਵਾਵਾਂ
- `azure-identity` - Azure ਪ੍ਰਮਾਣੀਕਰਣ (AzureCliCredential)
- `azure-search-documents` - Azure AI Search ਇੰਟੀਗ੍ਰੇਸ਼ਨ
- `mcp[cli]` - ਮਾਡਲ ਸੰਦੇਭ ਪ੍ਰੋਟੋਕੋਲ ਸਹਾਇਤਾ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋक्ति**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਨੂੰ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਤੀਰਤਾ ਹੋ ਸਕਦੀ ਹੈ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸ੍ਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਵਿਸ਼ੇਸ਼ਗਿਆ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->