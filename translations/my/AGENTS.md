# AGENTS.md

## Project Overview

ဤ repository တွင် "စတင်သူများအတွက် AI Agent များ" ပါဝင်သည် - AI Agent များ တည်ဆောက်ရန် လိုအပ်သည့် အရာအားလုံးကို သင်ကြားသည့် ဖြည့်စွက်ပညာသင်တန်း တစ်ခု ဖြစ်သည်။ အတန်းတွင် အခြေခံအရာများ၊ ဒီဇိုင်းပုံစံများ၊ ဖရိမ်းဝပ်များနှင့် AI agent များ၏ ထုတ်လုပ်မှုတပ်ဆင်ခြင်းများပါဝင်သည့် များစွာသော ၁၅ ကျော် သင်ခန်းစာများ ပါဝင်သည်။

**အဓိက နည်းပညာများ:**
- Python 3.12+
- အပြန်အလှန် သင်ယူနိုင်သော Jupyter Notebooks
- AI Framework များ: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architecture:**
- သင်ခန်းစာအလိုက် ဖွဲ့စည်းမှု (00-15+ ဖိုင်အိတ်များ)
- သင်ခန်းစာတိုင်းတွင်: README စာတမ်း၊ ကုဒ်နမူနာများ (Jupyter notebooks), နှင့်ပုံများ
- အလိုအလျောက်ဘာသာပြန်စနစ်မှ ဆော့မြောက်သော ဘာသာစကားအများအပြားကို ပံ့ပိုးမှုရှိခြင်း
- သင်ခန်းစာတိုင်းတွင် Microsoft Agent Framework ကို အသုံးပြုသော Python notebook တစ်ခု

## Setup Commands

### Prerequisites
- Python 3.12 သို့မဟုတ် အထက်
- Azure subscription (Azure AI Foundry အတွက်)
- Azure CLI တပ်ဆင်ပြီး လက်မှတ်ရယူထား (`az login`)

### Initial Setup

1. **Repository ကို clone သို့မဟုတ် fork လုပ်ပါ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # သို့မဟုတ်
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python virtual environment ဖန်တီးပြီး အလုပ်စတင်ပါ:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows များတွင်: venv\Scripts\activate
   ```

3. **လိုအပ်သော dependency များ သွင်းပါ:**
   ```bash
   pip install -r requirements.txt
   ```

4. **ပတ်ဝန်းကျင်ပြင်ဆင်ချက်များ သတ်မှတ်ပါ:**
   ```bash
   cp .env.example .env
   # သင့်ရဲ့ API keys နဲ့ endpoints ကို .env ဖိုင်ထဲမှာ ပြင်ဆင်ပါ။
   ```

### လိုအပ်သော ပတ်ဝန်းကျင် ပြင်ဆင်ချက်များ

**Azure AI Foundry** (လိုအပ်သည်):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - မော်ဒယ် တပ်ဆင်မှု အမည် (ဥပမာ gpt-4o)

**Azure AI Search** (သင်ခန်းစာ 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Notebooks ပြေးရန်မတိုင်မီ `az login` ကို တက်မြှောက်ပါ (အသုံးပြုသည် `AzureCliCredential`)။

## Development Workflow

### Jupyter Notebooks ကို အသုံးပြုခြင်း

သင်ခန်းစာမျိုးစုံတွင် Framework များအလိုက် Jupyter notebooks များ ပါရှိသည် -

1. **Jupyter ကို စတင်ပါ:**
   ```bash
   jupyter notebook
   ```

2. **သင်ခန်းစာ ဖိုလ်ဒါသို့ သွားပါ** (ဥပမာ `01-intro-to-ai-agents/code_samples/`)

3. **Notebooks များ ဖွင့်ပြီး ပြေးပါ:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework ကို အသုံးပြုခြင်း (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework ကို အသုံးပြုခြင်း (.NET)

### Microsoft Agent Framework နှင့် နှိုင်းယှဉ် အသုံးချခြင်း

**Microsoft Agent Framework + Azure AI Foundry:**
- Azure subscription လိုအပ်သည်
- `AzureAIProjectAgentProvider` ကို Agent Service V2 အတွက် အသုံးပြုသည် (Foundry portal တွင် agent များမြင်ရ)
- ထုတ်လုပ်မှုသုံးအဆင့် အသင့်ဖြစ်ပြီး built-in observability ပါရှိသည်
- ဖိုင်ပုံစံ: `*-python-agent-framework.ipynb`

## Testing Instructions

ဤ repository သည် ပညာရေးရာ ရည်ရွယ်ချက်ဖြစ်ပြီး အလိုအလျောက်စမ်းသပ်မှုများပါမရှိသော နမူနာကုဒ်များ ပါဝင်သည်။ သင်၏ စနစ်နှင့် ပြင်ဆင်မှုအသစ်များကို စစ်ဆေးရန် -

### လက်တွေ့ စမ်းသပ်ခြင်း

1. **Python ပတ်ဝန်းကျင် စမ်းသပ်ပါ:**
   ```bash
   python --version  # 3.12+ ဖြစ်ရမည်
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Notebook များ လက်တွေ့ ပြေးစစ်ပါ:**
   ```bash
   # အမှတ်အသားစာအုပ်ကို စာတမ်းကိုပြောင်းပြီး ဖြည်းဖြည်းစမ်းသပ်မှုများ imports စစ်ဆေးရန် ချပြပါ။
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ပတ်ဝန်းကျင်ပြင်ဆင်ချက်များ စစ်ဆေးပါ:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### သီးသန့် Notebooks များ ပြေးရန်

Jupyter တွင် notebooks တွေကို ဖွင့်ပြီး လေးနက်စွာ ชိန်းဆောင်၍ ခွဲစိတ်ဆဲလျင် လိုက်လံ ပြီးသား - 
- import statement များ
- သတ်မှတ်ချက်များ ဖတ်ခြင်း
- နမူနာ agent လုပ်ဆောင်မှုများ
- markdown cells တွင် မျှော်မှန်းထားသော ထွက်ရှိမှုများ

## Code Style

### Python အလေ့အထ

- **Python ဗားရှင်း**: 3.12+
- **ကုဒ် စတိုင်**: Python PEP 8 အညွှန်းအတိုင်း လိုက်နာပါ
- **Notebooks**: သဘောတရားရှင်းလင်းစွာ ရှင်းပြသည့် markdown cells များ ထည့်ပါ
- **Imports**: စံ library, အခြားပူးပေါင်း library နှင့် ဒေသခံ imports သို့ ခွဲပါ

### Jupyter Notebook အလေ့အထ

- ကုဒ် cell မတိုင်မှီ ရှင်းလင်းလန်းဆန်းသော markdown cell များ ထည့်သွင်းပါ
- နမူနာ output များကို notebooks တွင် ထည့်သွင်းပါ
- သင်ခန်းစာ အတွက် ကိုက်ညီသော သီးသန့် variable နာမည်များကို အသုံးပြုပါ
- Notebook execution ကို တန်းတူစဉ်လိုက် ပြန်လည် ထိန်းသိမ်းပါ (cell ၁ → ၂ → ၃...)

### ဖိုင် အုပ်ချုပ်မှု

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

### စာတမ်းများ တည်ဆောက်ခြင်း

ဤ repository သည် စာတမ်းများအတွက် Markdown ကို အသုံးပြုသည် -
- သင်ခန်းစာတိုင်းတွင် README.md ဖိုင်များ
- repository မှာ မူလ README.md
- GitHub Actions ဖြင့် automated ဘာသာပြန်စနစ်

### CI/CD Pipeline

`.github/workflows/` တွင်ရှိသည် -

1. **co-op-translator.yml** - ဘာသာစကား 50+ သို့ အလိုအလျောက် ဘာသာပြန်ခြင်း
2. **welcome-issue.yml** - ပြဿနာ အသစ်တင်သူများကို ကြိုဆိုခြင်း
3. **welcome-pr.yml** - Pull Request အသစ်တင်သူများကို ကြိုဆိုခြင်း

### Deployment

ဤသည် ပညာရေးရည်ရွယ်ချက် repository ဖြစ်ပြီး deployment လုပ်ငန်းစဉ် မရှိပါ။ အသုံးပြုသူများ -
1. Repository ကို fork သို့မဟုတ် clone ပြုလုပ်ပါ
2. Notebooks ကို ကိုယ်ပိုင်စက်သို့မဟုတ် GitHub Codespaces တွင် ပြေးပါ
3. နမူနာများကို ပြင်ဆင်ပြီး စမ်းသပ်ကာ သင်ယူပါ

## Pull Request Guidelines

### တင်သွင်းရှေ့မှာ

1. **သင်ပြင်ဆင်မှုများ စမ်းသပ်ပါ:**
   - သက်ဆိုင်ရာ notebooks များအားလုံး ပြေးပါ
   - အားလုံး cell များ အမှားမရှိဘဲ ပြေးစစ်ပါ
   - ထွက်ရှိမှုများ သက်ဆိုင်ရာ ဖြစ်မှုကို အတည်ပြုပါ

2. **စာတမ်းများ ပြင်ဆင်ပါ:**
   - နမူနာသစ် ထည့်မယ်ဆိုရင် README.md ကို update လုပ်ပါ
   - ခက်ခဲသောကုဒ်ကို notebook များတွင် မှတ်ချက် ထည့်ပါ
   - markdown cells မှကြေညာချက် ရှင်းပြပါ

3. **ဖိုင် ပြင်ဆင်မှုများ:**
   - `.env` ဖိုင်များ မတင်ရမှာ ဂရုပြုပါ (`.env.example` သာအသုံးပြု)
   - `venv/` သို့မဟုတ် `__pycache__/` ဖိုင်အိတ်များ မတင်ရ
   - နမူနာများ တစ်ခုကို ရည်ညွှန်းသော output များ notebook တွင် ထားပါ
   - အချိန်ပိုင်း ဖိုင်များ၊ backup notebooks များ (`*-backup.ipynb`) ဖယ်ရှားပါ

### PR ခေါင်းစဉ် ပုံစံ

မူးလင်းဖော်ပြချက်ရှိသော ခေါင်းစဉ်ကို အသုံးပြုပါ -
- `[Lesson-XX] <concept> အတွက် နမူနာ သစ် ထည့်ရန်`
- `[Fix] lesson-XX README တွင် အမှား ပြင်ဆင်ခြင်း`
- `[Update] lesson-XX တွင် ကုဒ်နမူနာ တိုးတက်စေရန်`
- `[Docs] Setup အချက်အလက်များ အသစ်ထည့်ခြင်း`

### လိုအပ်သော စစ်ဆေးမှုများ

- Notebooks များ အမှားမရှိစွာ ပြေးနိုင်ရမည်
- README ဖိုင်များ လိုက်လျောညီထွေရှိရမည်
- Repository ၏ နမူနာကုဒ် ပုံစံနှင့် ကိုက်ညီရမည်
- အခြားသင်ခန်းစာများနှင့် နှိုင်းယှဉ် သီးခြားမှုမရှိပါစေရန်

## Additional Notes

### ခေါင်းပိုး စိုးရိမ်ရမှုများ

1. **Python ဗားရှင်း မကိုက်ညီခြင်း:**
   - Python 3.12+ သုံးရမည်ကို အာမခံပါ
   - အချို့ package များသည် အဟောင်းဗားရှင်းများတွင် မအလုပ်လုပ်နိုင်ပါ
   - Python ဗားရှင်း ပိုမို သေချာစေရန် `python3 -m venv` အသုံးပြုပါ

2. **ပတ်ဝန်းကျင်ပြင်ဆင်ချက်များ:**
   - `.env.example` မှ `.env` ဖိုင်ပြုလုပ်ပါ
   - `.env` ဖိုင်ကို Git သို့ commit မလုပ်ပေးရ
   - GitHub token သည် လိုအပ်သည့်ခွင့်ပြုချက်များ ရှိရမည်

3. **Package တွေရှုပ်ထွေးမှု:**
   - အသစ် virtual environment တစ်ခု အသုံးပြုပါ
   - `requirements.txt` မှ သာ dependency များ install လုပ်ပါ
   - အချို့ notebooks များတွင် markdown cells တွင် လိုအပ်သော packages ကို ဖော်ပြထားသည်

4. **Azure Services:**
   - Azure AI service များတွင် active subscription လိုအပ်သည်
   - အချို့ features များသည် ဒေသအလိုက် ကန့်သတ်ချက်ရှိသည်
   - GitHub Models တွင် free tier ကန့်သတ်ချက်များ ရှိသည်

### သင်ယူလမ်းကြောင်း

သင်ခန်းစာများကို အောက်ပါအတိုင်း ရှေ့ဆက်သင်ယူရန် အကြံပြုသည် -
1. **00-course-setup** - ပတ်ဝန်းကျင် အဆင့်ဆင့် လုပ်ဆောင်ရန် ဒီနေရာမှ စတင်ပါ
2. **01-intro-to-ai-agents** - AI agent အခြေခံများကို နားလည်ရန်
3. **02-explore-agentic-frameworks** - အမျိုးမျိုး framework များ လေ့လာရန်
4. **03-agentic-design-patterns** - အဓိကဒီဇိုင်း pattern များ
5. နံပါတ်စဉ်လိုက် သင်ခန်းစာများကို ဆက်လက်လေ့လာရန်

### Framework ရွေးချယ်ခြင်း

ရည်ရွယ်ချက်အလိုက် framework ရွေးချယ်မည် -
- **သင်ခန်းစာအားလုံးတွင်** Microsoft Agent Framework (MAF) အသုံးပြုခြင်းနှင့် `AzureAIProjectAgentProvider`
- Azure AI Foundry Agent Service V2 တွင် agents များကို ဆာဗာဘက်တွင် မှတ်ပုံတင်ပြီး Foundry portal မှာ မြင်ရသည်

### အကူအညီ ရယူရန်

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) သို့ ဝင်ရောက်ပါ
- သင်ခန်းစာ README ဖိုင်များတွင် လမ်းညွှန်ချက် ရှိသည်
- ကိုယ်စားလှယ် README.md မှာ သင်တန်း အသေးစိတ် အထောက်အကူပြုချက် ရှိသည်
- [Course Setup](./00-course-setup/README.md) တွင် ရှင်းလင်းချက် များ

### ပါဝင်ဆောင်ရွက်မှု

ဤမှာ သင်္ချာပညာ တတ်မြောက်ရေး သင်တန်း စီမံချက် တစ်ခုဖြစ်ပြီး ပါဝင်ဆောင်ရွက်သူများ မဟုတ်မဖြစ်လိုအပ် -
- ကုဒ် နမူနာများ တိုးတက်အောင် ပြုလုပ်ရန်
- အမှားများ ပြင်ဆင်ရန်
- မှတ်ချက်များ ထည့်သွင်းရန်
- သင်ခန်းစာ စိတ်ဝင်စားဖွယ် ရေးရန်
- ဘာသာစကားအများအပြားသို့ ဘာသာပြန်ရန်

လက်ရှိ လိုအပ်ချက်များကို [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) တွင် ကြည့်ရှုနိုင်ပါသည်။

## Project-Specific Context

### ဘာသာစကား အများအပြား ပံ့ပိုးမှု

ဤ repository သည် အလိုအလျောက် ဘာသာပြန်စနစ် အသုံးပြုသည် -
- ဘာသာစကား ၅၀ ကျော်ကို ပံ့ပိုးသည်
- `/translations/<lang-code>/` ဖိုင်အိတ်များတွင် ဘာသာပြန်ထားသည်
- GitHub Actions workflow မှ ဘာသာပြန် အပ်ဒိတ်လုပ်သည်
- အင်္ဂလိပ်ကို မူလစာနယ်ဇင်း root တွင် သိမ်းဆည်းထားသည်

### သင်ခန်းစာ ဖွဲ့စည်းမှု

သင်ခန်းစာတိုင်းသည် အောက်ပါ စံပြ အတိုင်း လိုက်နာသည် -
1. ဗီဒီယို အထဲက ပုံလေးတစ်ပုံပါ ဆက်သွယ်သည့် လင့်ခ်ဖြင့်
2. စာရွက် သင်ခန်းစာအကြောင်း (README.md)
3. Framework မျိုးစုံအတွင်း ကုဒ်နမူနာများ
4. သင်ယူရမည့် ရည်ရွယ်ချက်များနှင့် လိုအပ်ချက်များ
5. ထပ်ဆင့် သင်ယူမှု အရင်းအမြစ်များ ထည့်သွင်းထားခြင်း

### ကုဒ်နမူနာ ဖိုင်နာမည် မိမိ

ပုံစံ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - သင်ခန်းစာ ၁၊ MAF Python
- `14-sequential.ipynb` - သင်ခန်းစာ ၁၄၊ MAF ဆက်တိုက်ဒီဇိုင်းများ

### အထူး ဖိုလ်ဒါများ

- `translated_images/` - ဘာသာပြန်ထားသော ပုံများ
- `images/` - အင်္ဂလိပ် မူရင်း ပုံများ
- `.devcontainer/` - VS Code ဖွံ့ဖြိုးရေး အဆင့် ဖိုင်အိတ်
- `.github/` - GitHub Actions workflow များ နှင့် template များ

### လိုအပ်သော dependency များ

`requirements.txt` မှ အဓိက package များ:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol လုပ်ငန်းကိစ္စ
- `azure-ai-inference`, `azure-ai-projects` - Azure AI service များ
- `azure-identity` - Azure authentication (AzureCliCredential)
- `azure-search-documents` - Azure AI Search အတွက် ပေါင်းစပ်မှု
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**သတိပေးချက်**  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်မှု စနစ်ဖြစ်သော [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့်ဘာသာပြန်ထားသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုကို ကြိုးစားပါသည် သို့သော် အလိုအလျောက်ဘာသာပြန်မှုတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်သည်ကို ကျေးဇူးပြု၍ သိရှိထားပါ။ မူရင်းစာရွက်ကို မူလဘာသာဖြင့် အခြေခံရင်း ထောက်မှတ်ရမည့် အချက်အလက်အဖြစ် သတ်မှတ်ပါ။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် လုပ်ငန်းကျွမ်းကျင် လူပုဂ္ဂိုလ်များမှ ဘာသာပြန်ပေးခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုအသုံးပြုမှုမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားခြင်း သို့မဟုတ် မှားယွင်းထင်မြင်မှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->