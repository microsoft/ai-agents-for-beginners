# AGENTS.md

## Project Overview

ဒီ repository မှာ "AI Agents for Beginners" ဆိုတာပါဝင်ပြီး AI Agents တည်ဆောက်ဖို့လိုအပ်တဲ့ အချက်အလက်အားလုံးကို သင်ကြားပေးသော အပြည့်အစုံ ပညာရေး သင်ခန်းစာတစ်ခုဖြစ်ပါတယ်။ သင်ခန်းစာတွင် AI agents များ၏ အခြေခံ၊ ဒီဇိုင်းပုံစံများ၊ ဖရိမ်ဝန်းများနှင့် ထုတ်လုပ်မှု deployment အထိ ၁၅ ကျော်သော အခန်းကဏ္ဍများပါဝင်သည်။

**အဓိက နည်းပညာများ:**
- Python 3.12+
- Jupyter Notebooks ကို လက်တွေ့ သင်ယူမှုအတွက် အသုံးပြုသည်
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**တည်ဆောက်ပုံ:**
- သင်ခန်းစာအရေအတွက်အလိုက် ဖိုင်ဖိုဒါများ (00-15+ directories)
- သင်ခန်းစာတိုင်းတွင်: README စာတမ်းများ၊ ကုဒ်နမူနာများ (Jupyter notebooks), ပုံများ ပါဝင်သည်
- အလိုအလျောက် ဘာသာပြန် စနစ်ဖြင့် မျိုးစုံဘာသာစကား ထောက်ခံမှု
- သင်ခန်းစာတစ်ခုစီအတွက် Microsoft Agent Framework ကို အသုံးပြုသော Python notebook တစ်ခု

## Setup Commands

### Prerequisites
- Python 3.12 သို့မဟုတ် အထက်
- Azure subscription (Azure AI Foundry အတွက်)
- Azure CLI ကို 설치ပြီး authenticated ဖြစ်ထားရန် (`az login`)

### Initial Setup

1. **Repository ကို clone သို့မဟုတ် fork ဆွဲရန်:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # သို့မဟုတ်
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python virtual environment ကို ဖန်တီးပြီး အလုပ်လုပ်စေခြင်း:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows တွင်: venv\Scripts\activate
   ```

3. **လိုအပ်သော dependencies များ install ပြုလုပ်ခြင်း:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ပတ်ဝန်းကျင် environment variables များ ပြင်ဆင်ပါ:**
   ```bash
   cp .env.example .env
   # သင့် API key များနှင့် endpoint များဖြင့် .env ကိုတည်းဖြတ်ပါ။
   ```

### လိုအပ်သော Environment Variables

**Azure AI Foundry အတွက် (လိုအပ်သည်):**
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment အမည် (ဥပမာ gpt-4o)

**Azure AI Search အတွက် (Lesson 05 - RAG):**
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Notebooks မလုပ်ခင် `az login` လုပ်ပါ (AzureCliCredential ကို အသုံးပြုသည်)။

## Development Workflow

### Jupyter Notebooks များ လည်ပတ်ခြင်း

သင်ခန်းစာတစ်ခုစီတွင် အမျိုးမျိုးသော ဖရိမ်ဝန်းများအတွက် Jupyter notebooks များပါဝင်သည်။

1. **Jupyter ကို စတင်ပါ:**
   ```bash
   jupyter notebook
   ```

2. **သင်ခန်းစာ ဖိုဒါသို့ သွားပါ** (ဥပမာ `01-intro-to-ai-agents/code_samples/`)

3. **Notebooks များကို ဖွင့်၍ လည်ပတ်ပါ:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python ကိုအသုံးပြုသည်)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET ကိုအသုံးပြုသည်)

### Microsoft Agent Framework ဖြင့် လုပ်ဆောင်ခြင်း

**Microsoft Agent Framework + Azure AI Foundry:**
- Azure subscription လိုအပ်သည်
- Agent Service V2 အတွက် `AzureAIProjectAgentProvider` ကို အသုံးပြုသည် (agents များကို Foundry portal မှာ မြင်ရသည်)
- production အဆင့် အတွက် observability ပါရှိသည်
- ဖိုင် နမူနာ: `*-python-agent-framework.ipynb`

## Testing Instructions

ဒီ repository သည် ပညာရေး အတွက် နမူနာကုဒ်များသာပါဝင်မည်ဖြစ်၍ automated tests မပါဝင်ပါ။ သင့် environment နှင့် ပြင်ဆင်မှုများကို စစ်ဆေးရန်:

### ကိုယ်တိုင် စမ်းသပ်ခြင်း

1. **Python environment စမ်းသပ်ခြင်း:**
   ```bash
   python --version  # ၃.၁၂ ထက်အများစုဖြစ်သင့်သည်။
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Notebook ကြောင်း အလုပ်လုပ်မှု စစ်ဆေးခြင်း:**
   ```bash
   # နိုတ်ဘွတ်ကို စက്രပ်စ်အဖြစ်ပြောင်းပြီး လည်ပတ်ပါ (စမ်းသပ်မှုများအတွက် import များစစ်ဆေးသည်)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Environment variables မှန်ကန်မှု စစ်ဆေးခြင်း:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### တစ်ခုချင်း စာစုများ လည်ပတ်ခြင်း

Jupyter တွင် notebooks များဖွင့်ပြီး လိုက်လံ အဆင့်လိုက် ထည့်သွင်းဆောင်ရွက်ပါ။ Notebook တစ်ခုစီမှာ:
- Import ကြေညာချက်များ
- ပြင်ဆင်မှုတင်သွင်းခြင်း
- နမူနာ agent အကောင်အထည်ဖော်ချက်များ
- markdown cells တွင် မျှော်မှန်းထားသော output များ

## Code Style

### Python နှင့် ပတ်သက်သော အမှတ်အသားများ

- **Python ဗားရှင်း**: 3.12 နှင့် အထက်
- **Code style**: Python PEP 8 စံကျစနစ် လိုက်နာပါ
- **Notebooks**: သဘောတူ ပေါ်လိမျ့ markdown cells ဖြင့် ဖေါ်ပြပါ
- **Imports**: Standard library, third-party, local imports အလိုက် ပေါင်းစည်းပါ

### Jupyter Notebook စတိုင်

- ကိုးကားများ ပြတ်ရှင်းသော markdown cells မပြတ်စွာ ထည့်ပါ
- notebooks မှာ output နမူနာများ ထည့်သွင်းပါ
- သင်ခန်းစာအကြောင်းအရာနှင့် ကိုက်ညီသော variable နာမည်များ သုံးပါ
- Notebook အလုပ်လုပ် အစီအစဉ် တစ်လိုက်တည်း ထိန်းသိမ်းပါ (cell 1 → 2 → 3...)

### ဖိုင် စီမံခန့်ခွဲမှု

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

### Documentation ဆောက်လုပ်ခြင်း

ဒီ repository မှာ Markdown ကို အသုံးပြုသည်။
- သင်ခန်းစာတစ်ခုစီတွင် README.md ဖိုင်များ
- repository မူလတွေ့ README.md ဖိုင်
- GitHub Actions မှ auto-translation စနစ်

### CI/CD pipeline

`.github/workflows/` တွင်တည်ရှိသည်။

1. **co-op-translator.yml** - ဘာသာစကား ၅၀ ကျော်သို့ အလိုအလျောက် ဘာသာပြန်ခြင်း
2. **welcome-issue.yml** - အကြောင်းအရာ အသစ်တင်သူများကို ကြိုဆိုခြင်း
3. **welcome-pr.yml** - pull request တင်သူများကို ကြိုဆိုခြင်း

### Deployment

ပညာရေး repository ဖြစ်၍ deployment လုပ်ငန်းစဉ် မရှိပါ။ အသုံးပြုသူများသည်
1. Repository ကို fork သို့မဟုတ် clone ဆွဲသည်
2. မိမိ ဒေသတွင် သို့မဟုတ် GitHub Codespaces တွင် notebooks တွေ လည်ပတ်သည်
3. နမူနာများ ပြင်ဆင်၍ သင်ယူဆောင်ရွက်သည်

## Pull Request Guidelines

### တင်သွင်းမည့် အခါ

1. **ပြင်ဆင်ထားသည်များ စမ်းသပ်ပါ:**
   - ဆက်စပ် notebooks များကို အပြည့်အ၀ run လုပ်ပါ
   - အားလုံးသော cell များ error မရှိစွာ လည်ပတ်နေကြောင်းသေချာပါစေ
   - Output များ သင့်လျော်မှုရှိစွာ မျှော်မှန်းထားပါသည်

2. **စာရွက်စာတမ်း ပြင်ဆင်မှု:**
   - README.md ကို အကြောင်းအရာအသစ် ထပ်သွင်းပါက update လုပ်ပါ
   - အဆင်မပြေကောင်းသော code များအတွက် notebook တွင် မှတ်ချက်ထည့်ပါ
   - markdown cells များသည် ရည်ရွယ်ချက် ပြတ်သားစွာ ရှင်းပြထားရန်

3. **ဖိုင် ပြင်ဆင်မှုများ:**
   - `.env` ဖိုင်များ commit မလုပ်ပါ (ဒီတွင် `.env.example` သာ အသုံးပြုပါ)
   - `venv/` သို့မဟုတ် `__pycache__/` ဖိုဒါများ commit မလုပ်ပါ
   - သင်ခန်းစာနိဒါန်းများ သွားအုံးသော output များ notebook တွင် ထားပါ
   - ထူးခြားသည့် ဖိုင်များနှင့် backup notebooks (`*-backup.ipynb`) မလိုအပ်ပါက ဖယ်ရှားပါ

### PR ခေါင်းစဉ် ဖော်ပြပုံ

အသေးစိတ် ပြောကြားချက်များ သုံးပါ။
- `[Lesson-XX] <concept> အတွက် နမူနာ အသစ် ထည့်သွင်းခြင်း`
- `[Fix] lesson-XX README တွင် စာလုံးပေါင်းမှားစီ ပြင်ဆင်ခြင်း`
- `[Update] lesson-XX တွင် code နမူနာ တိုးတက်အောင် ပြင်ဆင်ခြင်း`
- `[Docs] သတ်မှတ်ချက်များ သို့မဟုတ် setup လမ်းညွှန်ချက်များ Update ပြုလုပ်ခြင်း`

### လိုအပ်သော စစ်ဆေးမှုများ

- Notebooks များ error မရှိစွာ လုပ်ဆောင်နိုင်ရမည်
- README များ ရှင်းလင်း တိကျမှုရှိရမည်
- Repository ၌ ရှိသော code ပုံစံများကို လိုက်နာမည်
- အခြား သင်ခန်းစာများနှင့် ကိုက်ညီမှု တည်ရှိရမည်

## Additional Notes

### အထူး သတိပြုချက်များ

1. **Python ဗားရှင်း မကိုက်ညီခြင်း:**
   - Python 3.12 နှင့်အထက်သုံးစွဲရန်
   - အဟောင်းဗားရှင်း များနှင့် အချို့ package မအသုံးပြုပေးနိုင်
   - Python ဗားရှင်း သတ်မှတ်ရန် `python3 -m venv` သုံးပါ

2. **Environment variables:**
   - `.env` ကို `.env.example` မှတ်သားပြီး ဖန်တီးပါ
   - `.env` ကို git မှ commit မလုပ်ပါ (အဘယ်ကြောင့်ဆိုသော် `.gitignore` တွင် ပါဝင်သည်)
   - GitHub token တွင် လိုအပ်သော ခွင့်ပြုချက်များရှိရမည်

3. **Package ကွဲပြားမှု:**
   - သန့်ရှင်းသော virtual environment အသုံးပြုပါ
   - `requirements.txt` မှာ မြးထုတ် install ပြုလုပ်ပါ
   - အချို့ notebooks မှာ အပိုပက်ကေ့များကို markdown တွင် ဖော်ပြထားနိုင်သည်

4. **Azure ဝန်ဆောင်မှုများ:**
   - Azure AI ဝန်ဆောင်မှုများတွင် active subscription လိုအပ်သည်
   - သတ်မှတ်ထားသော ဒေသအလိုက်သာ အချို့ လုပ်ဆောင်ချက်များ ရှိနိုင်သည်
   - GitHub Models မှာ အခမဲ့အဆင့် အကန့်အသတ်များ လုပ်ဆောင်မှု ရှိသည်

### သင်ယူမှု လမ်းကြောင်း

သင်ခန်းစာများကို အောက်ပါအတိုင်း လိုက်နာသင်ယူရန် အကြံပြုသည် -
1. **00-course-setup** - environment setup အတွက် စတင်ပါ
2. **01-intro-to-ai-agents** - AI agent များ၏ အခြေခံဖြစ်စဉ် အသိပညာ
3. **02-explore-agentic-frameworks** - ဖရိမ်ဝန်း မျိုးစုံ နှင့် ပတ်သက်သော သင်ယူမှု
4. **03-agentic-design-patterns** - အဓိက ဒီဇိုင်းနမူနာများ
5. နံပါတ်စဉ်အတိုင်း ဆက်လက်သင်ယူမှု

### Framework ရွေးချယ်မှု

ရည်ရွယ်ချက်အရ framework ပေါ်မူတည်၍ ရွေးချယ်ပါ -
- **သင်ခန်းစာအားလုံး**: Microsoft Agent Framework (MAF) ကို `AzureAIProjectAgentProvider` နှင့် အသုံးပြုသည်
- **Agents သည် server-side မှာ register ဖြစ်ပြီး Azure AI Foundry Agent Service V2 တွင် ဖေါ်ပြသည်**

### အကူအညီ ရယူခြင်း

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) သို့ ဝင်ရောက်ဆက်သွယ်ပါ
- သင်ခန်းစာ README ဖိုင်များကို အကြံပြုချက်အတွက် ကြည့်ရှုပါ
- [README.md](./README.md) တွင် သင်ခန်းစာ အနှစ်ချုပ် ရှိသည်
- အသေးစိတ် setup အတွက် [Course Setup](./00-course-setup/README.md) ကို ကြည့်ပါ

### ပါဝင်ဆောင်ရွက်ခြင်း

ပညာရေးဖက် အခမဲ့ project ဖြစ်ပြီး ပါဝင်ဆောင်ရွက်နိုင်သည်။
- ကုဒ် နမူနာများ တိုးတက်ကောင်းမွန်အောင်လုပ်သောသူများ
- စာလုံးပေါင်းမှားများ ပြင်ဆင်သူများ
- မှတ်ချက်များ ထည့်သွင်းသူများ
- သင်ခန်းစာအကြောင်းအရာ အသစ်များ အကြံပြုသူများ
- ဘာသာစကား အသစ်များသို့ ဘာသာပြန်သူများ

လက်ရှိ လိုအပ်ချက်များအတွက် [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) ကို ကြည့်ပါ။

## Project-Specific Context

### မျိုးစုံ ဘာသာပြန် ချိတ်ဆက်မှု

ဒီ repository က အလိုအလျောက် ဘာသာပြန်စနစ်ကို အသုံးပြုသည်။
- ဘာသာစကား ၅၀ ကျော် ထောက်ပံ့သည်
- `/translations/<lang-code>/` ဖိုဒါတွင် ဘာသာပြန်မှုများ သိမ်းဆည်းသည်
- GitHub Actions workflow က ဘာသာပြန်မှု update များကို ကိုင်တွယ်သည်
- ဒေတာဖိုင်များကို repository root တွင် အင်္ဂလိပ်ဘာသာဖြင့် ထားရှိသည်

### သင်ခန်းစာ ဖွဲ့စည်းပုံ

သင်ခန်းစာ တစ်ခုစီမှာ အောက်ပါအတိုင်း လုပ်ဆောင်သည် -
1. ဗီဒီယို thumbnail နှင့် link
2. စာသားအကြောင်းအရာ (README.md)
3. ဖရိမ်ဝန်း မျိုးစုံအတွက် ကုဒ် နမူနာများ
4. သင်ယူရမည့် ရည်ရွယ်ချက်များနှင့် prerequisite များ
5. သင်ယူမှု အပိုဆောင်း အရင်းအမြစ်များ လင့်ခ်ဖြင့် ဖော်ပြသည်

### ကုဒ် နမူနာ နာမည်ပုံစံ

ပုံစံ - `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - သင်ခန်းစာ ၁၊ MAF Python
- `14-sequential.ipynb` - သင်ခန်းစာ ၁၄၊ MAF ဆက်လက် တိုးတက်မှုအပိုင်း

### အထူး ဖိုဒါများ

- `translated_images/` - ဘာသာပြန်ထားသော ပုံများ
- `images/` - အင်္ဂလိပ်ဘာသာ အတွက် မူလ ပုံများ
- `.devcontainer/` - VS Code development container ပတ်သက်သော ဖိုင်များ
- `.github/` - GitHub Actions workflows နှင့် template များ

### လိုအပ်သော Dependencies

`requirements.txt` ထဲမှ အဓိက ကိုးကားမှုများ -
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol အတွက်
- `azure-ai-inference`, `azure-ai-projects` - Azure AI ဝန်ဆောင်မှုများ
- `azure-identity` - Azure authentication (AzureCliCredential)
- `azure-search-documents` - Azure AI Search ထည့်သွင်းမှု
- `mcp[cli]` - Model Context Protocol ထောက်ခံမှု

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ဤစာတမ်းအတွက် အသိပေးချက်**:
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးပမ်းထားသော်လည်း၊ စက်လိုက်ဘာသာပြန်မှုတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုရန် ကြေငြာလိုပါသည်။ မူရင်းစာတမ်းကို မိသားစုဘာသာဖြင့်သာ တရားဝင် အချက်အလက်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် လူအရည်အချင်းပြည့်မီသော လူ့ဘာသာပြန်ဝန်ဆောင်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှု အသုံးပြုမှုမှ ဖြစ်ပေါ်လာနိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မွားယွင်းဖော်ပြမှုများအပေါ် ကျွန်ုပ်တို့အား တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->