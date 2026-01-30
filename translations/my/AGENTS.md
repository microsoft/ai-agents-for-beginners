# AGENTS.md

## ပရောဂျက်အကျဉ်းချုပ်

ဤ repository တွင် "AI Agents for Beginners" ပါဝင်ပြီး AI Agents တည်ဆောက်ရန် လိုအပ်သော အရာအားလုံးကို သင်ကြားပေးသည့် အကျုံးဝင်သော ပညာရေးသင်ခန်းစာများ ပါဝင်သည်။ သင်ခန်းစာများတွင် အခြေခံအကြောင်းအရာများ၊ ဒီဇိုင်းပုံစံများ၊ framework များနှင့် AI agents များကို ထုတ်လုပ်မှုအဆင့်သို့ ရောက်ရန် လိုအပ်သော နည်းလမ်းများကို 15+ သင်ခန်းစာများဖြင့် ဖုံးအုပ်ထားသည်။

**အဓိကနည်းပညာများ:**
- Python 3.12+
- Jupyter Notebooks ဖြင့် အပြန်အလှန်လေ့လာမှု
- AI Frameworks: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI Services: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (အခမဲ့အဆင့်ရရှိနိုင်)

**Architecture:**
- သင်ခန်းစာအခြေခံဖွဲ့စည်းမှု (00-15+ directories)
- သင်ခန်းစာတစ်ခုစီတွင် README documentation, code samples (Jupyter notebooks), နှင့် ပုံများ ပါဝင်သည်
- အလိုအလျောက်ဘာသာပြန်စနစ်ဖြင့် ဘာသာစကားများစွာကို ပံ့ပိုးမှု
- သင်ခန်းစာတစ်ခုစီတွင် framework အမျိုးမျိုးကို ရွေးချယ်နိုင်မှု (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Setup Commands

### လိုအပ်ချက်များ
- Python 3.12 သို့မဟုတ် အထက်
- GitHub အကောင့် (GitHub Models - အခမဲ့အဆင့်)
- Azure subscription (optional, Azure AI services အတွက်)

### စတင်တပ်ဆင်ခြင်း

1. **Repository ကို Clone သို့မဟုတ် Fork လုပ်ပါ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python virtual environment ကို ဖန်တီးပြီး အလုပ်လုပ်စေပါ:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **လိုအပ်သော dependencies များကို တပ်ဆင်ပါ:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment variables များကို စနစ်တကျပြင်ဆင်ပါ:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### လိုအပ်သော Environment Variables

**GitHub Models (အခမဲ့):**
- `GITHUB_TOKEN` - GitHub မှ Personal access token

**Azure AI Services** (optional):
- `PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API key
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Chat model အတွက် deployment name
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Embeddings အတွက် deployment name
- `.env.example` တွင် ဖော်ပြထားသော အခြား Azure configuration

## Development Workflow

### Jupyter Notebooks ကို အလုပ်လုပ်စေခြင်း

သင်ခန်းစာတစ်ခုစီတွင် framework များအမျိုးမျိုးအတွက် Jupyter notebooks များပါဝင်သည်:

1. **Jupyter ကို စတင်ပါ:**
   ```bash
   jupyter notebook
   ```

2. **သင်ခန်းစာ directory သို့ သွားပါ** (ဥပမာ `01-intro-to-ai-agents/code_samples/`)

3. **Notebooks များကို ဖွင့်ပြီး အလုပ်လုပ်စေပါ:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel framework ကို အသုံးပြုခြင်း
   - `*-autogen.ipynb` - AutoGen framework ကို အသုံးပြုခြင်း
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) ကို အသုံးပြုခြင်း
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) ကို အသုံးပြုခြင်း
   - `*-azureaiagent.ipynb` - Azure AI Agent Service ကို အသုံးပြုခြင်း

### Framework များနှင့် အလုပ်လုပ်ခြင်း

**Semantic Kernel + GitHub Models:**
- GitHub အကောင့်ဖြင့် အခမဲ့အဆင့်ရရှိနိုင်
- လေ့လာမှုနှင့် စမ်းသပ်မှုအတွက် သင့်လျော်သည်
- ဖိုင်ပုံစံ: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- GitHub အကောင့်ဖြင့် အခမဲ့အဆင့်ရရှိနိုင်
- Multi-agent orchestration စွမ်းရည်များ
- ဖိုင်ပုံစံ: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoft မှ နောက်ဆုံးထွက် framework
- Python နှင့် .NET တွင် ရရှိနိုင်
- ဖိုင်ပုံစံ: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azure subscription လိုအပ်သည်
- ထုတ်လုပ်မှုအဆင့်အတွက် သင့်လျော်သော features
- ဖိုင်ပုံစံ: `*-azureaiagent.ipynb`

## Testing Instructions

ဤ repository သည် ပညာရေးအတွက် ရည်ရွယ်ထားသော code များပါဝင်ပြီး automated tests မပါဝင်ပါ။ သင့် setup နှင့် ပြင်ဆင်မှုများကို အတည်ပြုရန်:

### Manual Testing

1. **Python environment ကို စမ်းသပ်ပါ:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Notebook များကို အလုပ်လုပ်စေခြင်းကို စမ်းသပ်ပါ:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Environment variables ကို အတည်ပြုပါ:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Individual Notebooks ကို အလုပ်လုပ်စေခြင်း

Notebooks များကို Jupyter တွင် ဖွင့်ပြီး cell များကို အစဉ်လိုက် အလုပ်လုပ်စေပါ။ Notebook တစ်ခုစီသည် အခြားနဲ့မပေါင်းစပ်သော အကြောင်းအရာများပါဝင်ပြီး:
- Import statements
- Configuration loading
- Agent implementation ဥပမာများ
- Markdown cells တွင် မျှော်မှန်းထားသော output များ

## Code Style

### Python Conventions

- **Python Version**: 3.12+
- **Code Style**: Python PEP 8 standard ကို လိုက်နာပါ
- **Notebooks**: အကြောင်းအရာများကို ရှင်းလင်းသော markdown cells ဖြင့် ရှင်းပြပါ
- **Imports**: Standard library, third-party, local imports အလိုက် အုပ်စုဖွဲ့ပါ

### Jupyter Notebook Conventions

- Code cells မတိုင်မီ ရှင်းလင်းသော markdown cells ထည့်ပါ
- Notebook များတွင် output ဥပမာများ ထည့်သွင်းပါ
- သင်ခန်းစာအကြောင်းအရာနှင့် ကိုက်ညီသော variable names အသုံးပြုပါ
- Notebook execution order ကို linear ထားပါ (cell 1 → 2 → 3...)

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

### Documentation တည်ဆောက်ခြင်း

ဤ repository သည် Markdown ကို documentation အတွက် အသုံးပြုသည်:
- သင်ခန်းစာ folder တစ်ခုစီတွင် README.md ဖိုင်များ
- Repository root တွင် Main README.md
- GitHub Actions ဖြင့် အလိုအလျောက်ဘာသာပြန်စနစ်

### CI/CD Pipeline

`.github/workflows/` တွင် တည်ရှိသည်:

1. **co-op-translator.yml** - 50+ ဘာသာစကားများသို့ အလိုအလျောက်ဘာသာပြန်ခြင်း
2. **welcome-issue.yml** - Issue အသစ်ဖန်တီးသူများကို ကြိုဆိုခြင်း
3. **welcome-pr.yml** - Pull request အသစ်တင်သူများကို ကြိုဆိုခြင်း

### Deployment

ဤ repository သည် ပညာရေးအတွက် ရည်ရွယ်ထားပြီး deployment လုပ်ငန်းစဉ်မပါဝင်ပါ။ အသုံးပြုသူများ:
1. Repository ကို Fork သို့မဟုတ် Clone လုပ်ပါ
2. Notebooks များကို ဒေသတွင်း သို့မဟုတ် GitHub Codespaces တွင် အလုပ်လုပ်စေပါ
3. ဥပမာများကို ပြင်ဆင်ခြင်းနှင့် စမ်းသပ်ခြင်းဖြင့် လေ့လာပါ

## Pull Request Guidelines

### Submit မလုပ်မီ

1. **သင့်ပြင်ဆင်မှုများကို စမ်းသပ်ပါ:**
   - သက်ဆိုင်သော notebooks များကို အပြည့်အဝ အလုပ်လုပ်စေပါ
   - Cell များအားလုံး error မရှိဘဲ အလုပ်လုပ်စေပါ
   - Output များကို သင့်လျော်မှုရှိကြောင်း စစ်ဆေးပါ

2. **Documentation ပြင်ဆင်မှုများ:**
   - Concepts အသစ်ထည့်သွင်းပါက README.md ကို update လုပ်ပါ
   - ရှုပ်ထွေးသော code များအတွက် notebooks တွင် comment ထည့်ပါ
   - Markdown cells တွင် ရည်ရွယ်ချက်ကို ရှင်းပြပါ

3. **File ပြောင်းလဲမှုများ:**
   - `.env` ဖိုင်များကို commit မလုပ်ပါ (`.env.example` ကို အသုံးပြုပါ)
   - `venv/` သို့မဟုတ် `__pycache__/` directories မပါဝင်စေရန် သေချာပါ
   - Concepts ကို ဖော်ပြသော notebook outputs များကို ထားပါ
   - Temporary files နှင့် backup notebooks (`*-backup.ipynb`) ကို ဖယ်ရှားပါ

### PR Title Format

ရှင်းလင်းသော ခေါင်းစဉ်များကို အသုံးပြုပါ:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- Notebooks များ error မရှိဘဲ အလုပ်လုပ်စေရန်
- README ဖိုင်များ ရှင်းလင်းပြီး မှန်ကန်မှုရှိရန်
- Repository တွင် ရှိသော code pattern များကို လိုက်နာရန်
- အခြားသင်ခန်းစာများနှင့် အညီရှိရန်

## အပိုဆောင်းမှတ်ချက်များ

### Common Gotchas

1. **Python version မကိုက်ညီမှု:**
   - Python 3.12+ ကို အသုံးပြုပါ
   - အချို့သော packages များသည် အဟောင်း version များနှင့် အလုပ်မလုပ်နိုင်ပါ
   - `python3 -m venv` ကို အသုံးပြု၍ Python version ကို သတ်မှတ်ပါ

2. **Environment variables:**
   - `.env.example` မှ `.env` ကို ဖန်တီးပါ
   - `.env` ဖိုင်ကို commit မလုပ်ပါ (`.gitignore` တွင် ပါဝင်သည်)
   - GitHub token သင့် permissions လိုအပ်သည်

3. **Package conflicts:**
   - အသစ်သော virtual environment ကို အသုံးပြုပါ
   - Individual packages မထည့်ဘဲ `requirements.txt` မှ တပ်ဆင်ပါ
   - အချို့သော notebooks တွင် markdown cells တွင် ဖော်ပြထားသော အပို packages လိုအပ်နိုင်သည်

4. **Azure services:**
   - Azure AI services သည် subscription လိုအပ်သည်
   - အချို့သော features သည် region-specific ဖြစ်သည်
   - GitHub Models အတွက် အခမဲ့အဆင့်ကန့်သတ်ချက်များ ရှိသည်

### Learning Path

သင်ခန်းစာများကို အစဉ်လိုက် လေ့လာရန် အကြံပြုသည်:
1. **00-course-setup** - Environment setup အတွက် ဤနေရာမှ စတင်ပါ
2. **01-intro-to-ai-agents** - AI agent အခြေခံအကြောင်းအရာများကို နားလည်ပါ
3. **02-explore-agentic-frameworks** - Framework များအကြောင်း လေ့လာပါ
4. **03-agentic-design-patterns** - အဓိက ဒီဇိုင်းပုံစံများ
5. အနံ့လိုက် သင်ခန်းစာများကို ဆက်လက် လေ့လာပါ

### Framework Selection

သင့်ရည်ရွယ်ချက်အပေါ်မူတည်၍ framework ကို ရွေးချယ်ပါ:
- **လေ့လာမှု/Prototype**: Semantic Kernel + GitHub Models (အခမဲ့)
- **Multi-agent systems**: AutoGen
- **နောက်ဆုံး features**: Microsoft Agent Framework (MAF)
- **ထုတ်လုပ်မှု deployment**: Azure AI Agent Service

### Getting Help

- [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord) ကို Join လုပ်ပါ
- သင်ခန်းစာ README ဖိုင်များကို သီးသန့်လမ်းညွှန်အတွက် ပြန်လည်ကြည့်ပါ
- ပရောဂျက်အကျဉ်းချုပ်အတွက် [README.md](./README.md) ကို ကြည့်ပါ
- အသေးစိတ် setup လမ်းညွှန်များအတွက် [Course Setup](./00-course-setup/README.md) ကို ရည်ညွှန်းပါ

### Contributing

ဤသည်မှာ ပွင့်လင်းသော ပညာရေးပရောဂျက်ဖြစ်သည်။ အထောက်အကူပြုမှုများကို ကြိုဆိုပါသည်:
- Code ဥပမာများကို တိုးတက်အောင် ပြင်ဆင်ပါ
- စာလုံးပေါင်းမှားများ သို့မဟုတ် အမှားများကို ပြင်ဆင်ပါ
- ရှင်းလင်းသော comment များ ထည့်သွင်းပါ
- သင်ခန်းစာအကြောင်းအရာအသစ်များကို အကြံပြုပါ
- အပိုဘာသာစကားများသို့ ဘာသာပြန်ပါ

[GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) တွင် လက်ရှိလိုအပ်ချက်များကို ကြည့်ပါ။

## Project-Specific Context

### Multi-Language Support

ဤ repository သည် အလိုအလျောက်ဘာသာပြန်စနစ်ကို အသုံးပြုသည်:
- 50+ ဘာသာစကားများကို ပံ့ပိုးသည်
- `/translations/<lang-code>/` directories တွင် ဘာသာပြန်ထားသော ဖိုင်များ
- GitHub Actions workflow သည် ဘာသာပြန် update များကို ကိုင်တွယ်သည်
- Source ဖိုင်များသည် repository root တွင် အင်္ဂလိပ်ဘာသာဖြင့် ရှိသည်

### Lesson Structure

သင်ခန်းစာတစ်ခုစီသည် အညီတူပုံစံကို လိုက်နာသည်:
1. Video thumbnail နှင့် link
2. ရေးသားထားသော သင်ခန်းစာအကြောင်းအရာ (README.md)
3. Framework များအမျိုးမျိုးဖြင့် code samples
4. Learning objectives နှင့် prerequisites
5. အပို learning resources များကို link ဖြင့် ထည့်သွင်းထားသည်

### Code Sample Naming

ပုံစံ: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Lesson 4, Semantic Kernel
- `07-autogen.ipynb` - Lesson 7, AutoGen
- `14-python-agent-framework.ipynb` - Lesson 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lesson 14, MAF .NET

### Special Directories

- `translated_images/` - ဘာသာပြန်ထားသော ပုံများ
- `images/` - အင်္ဂလိပ်အကြောင်းအရာအတွက် ပုံများ
- `.devcontainer/` - VS Code development container configuration
- `.github/` - GitHub Actions workflows နှင့် templates

### Dependencies

`requirements.txt` မှ အဓိက packages:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen framework
- `semantic-kernel` - Semantic Kernel framework
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-search-documents` - Azure AI Search integration
- `chromadb` - RAG ဥပမာများအတွက် vector database
- `chainlit` - Chat UI framework
- `browser_use` - Agents အတွက် browser automation
- `mcp[cli]` - Model Context Protocol support
- `mem0ai` - Agents အတွက် memory management

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။