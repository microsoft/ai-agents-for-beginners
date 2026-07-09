# AGENTS.md

## စီမံကိန်းအနှစ်ချုပ်

ဒီ repository မှာ "စတင်လေ့လာသူများအတွက် AI Agents" ဆိုတဲ့ အကြောင်းအရာပြည့်စုံသင်တန်းတစ်ခု ပါဝင်ပြီး AI Agents တည်ဆောက်ရာမှာ လိုအပ်တဲ့ ပညာသင်ကြားမှုအားလုံးပါဝင်ပါတယ်။ သင်တန်းမှာ သင်္ချာ, ဒီဇိုင်းပုံစံများ, Framework များနှင့် AI agents များကို တည်ဆောက်ထုတ်လုပ်ဖို့ လိုအပ်တဲ့ အခြေခံများကို ၁၈ ခန်းခွဲ ဖြန့်ဝေထားပါတယ်။

**အဓိကနည်းပညာများ:**
- Python 3.12+
- အပြန်အလှန်ဆက်သွယ်ပြီး သင်ယူနိုင်ဖို့အတွက် Jupyter Notebooks
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**ဖွဲ့စည်းပုံ:**
- ခန်း ၁၈ ခန်းအခြေခံ ဖိုင်ဆိုင်ရာအစီအစဉ် (00-15+ ဒိုင်ရက်တာရီးများ)
- တစ်ခန်းစီတွင် README စာရွက်စာတမ်းများ၊ ကုဒ်နမူနာများ (Jupyter notebooks) နှင့် ပုံများပါဝင်သည်
- အလိုအလျောက် ဘာသာပြန်စနစ်ဖြင့် ဘာသာစကားအမျိုးမျိုးကို ထောက်ပံ့သည်
- တစ်ခန်းစီအတွက် Microsoft Agent Framework ပါတဲ့ Python notebook တစ်ခု

## စတင်အသုံးပြုရန် မှတ်ချက်များ

### လိုအပ်ချက်များ
- Python 3.12 သို့မဟုတ် အထက်
- Azure subscription (Microsoft Foundry အတွက်)
- Azure CLI ထည့်သွင်းပြီး အတည်ပြုထားရန် (`az login`)

### မူလဆက်တင်များ

၁။ **Repository ကို Clone သို့ Fork ပြုလုပ်ပါ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ဒါမှမဟုတ်
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

၂။ **Python virtual environment ကို ဖန်တီးပြီး ဖွင့်ပါ:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows ပေါ်တွင်: venv\Scripts\activate
   ```

၃။ **လိုအပ်သော dependencies များ ထည့်သွင်းပါ:**
   ```bash
   pip install -r requirements.txt
   ```

၄။ **ပတ်ဝန်းကျင် 변수များကို သတ်မှတ်ပါ:**
   ```bash
   cp .env.example .env
   # သင့် API key များနှင့် endpoints များဖြင့် .env ကို တည်းဖြတ်ပါ
   ```

### လိုအပ်သော ပတ်ဝန်းကျင် 변수များ

**Microsoft Foundry** အတွက် (လိုအပ်သည်):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry ပရိုဂျက် အစွန်း
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment အမည် (ဥပမာ၊ gpt-4o)

**Azure AI Search** အတွက် (ခန်း ၀၅ - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search အစွန်း
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

အတည်ပြုချက်: notebooks များ ချဲ့ထွင်ခဏမှ မတိုင်ခင် `az login` ပြုလုပ်ပါ (AzureCliCredential ကို အသုံးပြုသည်)။

## ဖွံ့ဖြိုးရေး လုပ်ငန်းစဉ်

### Jupyter Notebooks များ စတင်ရမည့်နည်းလမ်း

တစ်ခန်းစီတွင် Framework များအလိုက် Jupyter notebooks များ များစွာ ပါဝင်သည်။

၁။ **Jupyter စတင်မှု:**
   ```bash
   jupyter notebook
   ```

၂။ **ခန်းခွဲဒိုင်ရက်တာရီသို့ သွားပါ** (ဥပမာ၊ `01-intro-to-ai-agents/code_samples/`)

၃။ **notebooks များ ဖွင့်ပြီး run ပါ:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) ဖြင့်အသုံးပြုခြင်း
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) ဖြင့်အသုံးပြုခြင်း

### Microsoft Agent Framework နှင့် လုပ်ဆောင်ခြင်း

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure subscription လိုအပ်သည်
- Agent Service V2 အတွက် `FoundryChatClient` ကို အသုံးပြုသည် (Foundry portal တွင် agents များမြင်ရသည်)
- ထုတ်လုပ်ရေးအဆင့်အတွက် တပ်ဆင်ထားသော observability ပါဝင်သည်
- ဖိုင်ပုံစံ: `*-python-agent-framework.ipynb`

## စမ်းသပ်နည်းလမ်း

ဒီ repository သည် ကျောင်းသားများ သင်ယူရန် အတွက် နမူနာကုဒ်များပါရှိသည်၊ ထုတ်လုပ်ရေးကုဒ် မဟုတ်ပါ။ သင့်တည်ဆောက်မှုနှင့် ပြင်ဆင်မှုများကို စစ်ဆေးရန်:

### လက်ခံစမ်းသပ်ခြင်း

၁။ **Python ပတ်ဝန်းကျင်ကို စမ်းသပ်ရန်:**
   ```bash
   python --version  # 3.12+ ဖြစ်သင့်သည်
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

၂။ **Notebook များကို စမ်းသပ်ပါ:**
   ```bash
   # နော့စ်ဘုတ်ကို စကရစ်ပ်သို့ ပြောင်းပြီး ပြေးဆွဲပါ (စမ်းသပ်မှုများအတွက် တင်သွင်းမှုများ)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

၃။ **ပတ်ဝန်းကျင် 변수များကို အတည်ပြုပါ:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### တစ်ခုချင်း တစဲ notebook များ run ပြုလုပ်ခြင်း

Jupyter တွင် notebooks များ ဖွင့်ပြီး နောက်တစ်ခုနောက်ကို စီစဥ် run စေလော့ပါ။ တစ်ခုချင်းစီမှာ တစ်ဦးချင်း အပြည့်အစုံပါရှိပြီး:
- import အဖြစ် ကြေညာချက်များ
- configuration ကို လုပ်ဆောင်ခြင်း
- agent များ အကောင်အထည်ဖော်မှု နမူနာများ
- markdown cells မျှဝေထားသော အနာဂတ်ထုတ်လောများ

## ကုဒ်စတိုင်

### Python စံနှုန်းများ

- **Python ဗားရှင်း**: 3.12+
- **ကုဒ်စတိုင်**: Python PEP 8 စံနှုန်းများ လိုက်နာပါ
- **Notebooks**: ရိုးရှင်းပြီး ဖော်ပြချက် မာ့ခ်ဒေါင်းကွက် များ သုံးပါ
- **imports**: standard library, third-party, ရှေ့နေ imports အလိုက် အုပ်စုဖွဲ့ပါ

### Jupyter Notebook စံနှုန်းများ

- ကုဒ်မတိုင်မီ ဖော်ပြချက် မာ့ခ်ဒေါင်းကွက်များ ထည့်သွင်းပါ
- အပေါ်ထွက်ကုန်မာ့နမူနာများ ထည့်သွင်းပါ
- သင်ခန်းစာပေါ်မူတည်ပြီး variable အမည်များ အသုံးပြုပါ
- Notebook အုပ်ချုပ်မှု နောက်ဆက်တွဲ စဉ်ဆက် run အဆင့်တကျ ဖြစ်စေရန် ထိန်းသိမ်းပါ

### ဖိုင်စီမံခန့်ခွဲမှု

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## တည်ဆောက်ခြင်းနှင့် ထုတ်လုပ်ခြင်း

### စာရွက်စာတမ်း တည်ဆောက်ခြင်း

ဒီ repository သည် Markdown ကို စာတမ်းအတွက် အသုံးပြုသည်။
- တစ်ခန်းစီဖိုလ်ဒါတွင် README.md ဖိုင်များ
- Repository အဓိကအမွေ့ မှာသော README.md
- GitHub Actions ဖြင့် အလိုအလျောက် ဘာသာပြန်မှု

### CI/CD လုပ်ငန်းစဉ်

`.github/workflows/` တွင် တည်ရှိသည်။

၁။ **co-op-translator.yml** - ၅၀ ကျော်ဘာသာစကားသို့ အလိုအလျောက် ဘာသာပြန်ခြင်း
၂။ **welcome-issue.yml** - issue အသစ်ဖန်တီးသူများ ကို ကြိုဆိုခြင်း
၃။ **welcome-pr.yml** - pull request  အသစ်ပေးပို့သူများကို ကြိုဆိုခြင်း

### ထုတ်လုပ်ခြင်း

ဒီ repository သည် သင်ကြားရေးဆိုင်ရာဖြစ်ပြီး ထုတ်လုပ်မှုလုပ်ငန်းစဉ် မရှိပါ။ အသုံးပြုသူများအနေဖြင့်:
၁။ Repository ကို fork သို့ clone ချပါ
၂။ Notebooks များကို နေရာခံ သို့ GitHub Codespaces တွင် run ပါ
၃။ ဥပမာများ ပြင်ဆင်၍ လေ့လာပါ

## Pull Request လမ်းညွှန်ချက်များ

### တင်သွင်းရန် မတိုင်မီ

၁။ **ပြင်ဆင်မှုများ စမ်းသပ်ပါ:**
   - သက်ရောက်ထားသော notebooks များကို အပြည့် run လုပ်ပါ
   - စဲပြီး cell များ အမှား မရှိစေရေး စစ်ဆေးပါ
   - ထွက်လာသောအဖြေပေါ် ပိုင်းသက်သာမှုကို စစ်ဆေးပါ

၂။ **စာရွက်စာတမ်းများ ပြင်ဆင်မှု:**
   - သင်ဆိုလိုသည့် အကြောင်းအရာ အသစ် ထည့်မယ်ဆို အတွက် README.md ကို ενημερώστε
   - ပြတ်ပွားသောကုဒ်များအတွက် notebook များတွင် မှတ်ချက်ထည့်ပါ
   - နည်းနာများကို markdown cells တွင် ရေးပါ

၃။ **ဖိုင်ပြင်ဆင်မှုများ:**
   - `.env` ဖိုင်များကို မတင်သွင်းပါနဲ့ (.env.example အသုံးပြုပါ)
   - `venv/` သို့မဟုတ် `__pycache__/` ဒိုင်ရက်တာရီး မတင်ပါနဲ့
   - နမူနာဖော်ပြရာ notebook output များကို ထိန်းသိမ်းပါ
   - ယာယီဖိုင်များနှင့် backup notebooks (`*-backup.ipynb`) မပါဝင်‌စေရန် ဖယ်ရှားပါ

### PR ခေါင်းစဉ်ပုံစံ

ဖော်ပြချက်ပြည့်စုံသော ခေါင်းစဉ်များ အသုံးပြုပါ:
- `[Lesson-XX] <ခံယူချက်အတွက်> အတွက် နမူနာအသစ် ထည့်ပါ`
- `[Fix] lesson-XX README မှာ မှားတာ ပြင်ပါ`
- `[Update] lesson-XX ကုဒ်နမူနာ တိုးတက်အောင် ပြုပြင်သည်`
- `[Docs] စတင်ရန် လမ်းညွှန်ချက်များ ပြင်ဆင်သည်`

### လိုအပ်သော စစ်ဆေးမှုများ

- Notebooks များ error မရှိစေရန် ရှေ့ပြေး run ပြုလုပ်ပါ
- README ဖိုင်များ ရှင်းလင်းပြီးတိကျမှုရှိစေရန် စောင့်ကြည့်ပါ
- Repository မှာရှိပြီးသား ကုဒ်ပုံစံများနဲ့ လိုက်နာပါ
- အခြားချုပ်ခန်းများနှင့် နည်းလမ်းတူအောင် ထိန်းသိမ်းပါ

## ထပ်မံ အသိပေးချက်များ

### အလွန်ကြုံတွေ့ရတဲ့ အခက်အခဲများ

၁။ **Python ဗားရှင်း မတူညီခြင်း:**
   - Python 3.12+ ကို အသုံးပြုကြပါ
   - အချို့ package များ သက်ဆိုင်ရာ လက်ရှိဗားရှင်းတွင် မအောင်မြင်နိုင်ပါက
   - Python ဗားရှင်း သတ်မှတ်ရန် `python3 -m venv` ကို အသုံးပြုပါ

၂။ **ပတ်ဝန်းကျင် 변수များ:**
   - `.env.example` မှ `.env` ဖိုင် ကို အမြဲဖန်တီးပါ
   - `.env` ဖိုင်ကို commit မလုပ်ပါနဲ့ ( `.gitignore` ထဲမှာပါ)
   - Entra ID အတည်ပြုချက် key မလိုဘဲ အသုံးပြုရန် `az login` ဖြင့် ဝင်ပါ

၃။ **Package conflicts များ:**
   - အသစ်ဖန်တီးထားသော virtual environment ကို အသုံးပြုပါ
   - နီးကိုအများဆုံး package များအား `requirements.txt` မှ တပ်ဆင်ပါ
   - အချို့ notebooks များတွင် အပို package များလိုအပ်နိုင်သည်၊ markdown cells တွင် ဖော်ပြထားသော package များကို ထည့်သွင်းပါ

၄။ **Azure ဝန်ဆောင်မှုများ:**
   - Azure AI ဝန်ဆောင်မှုများ အသက်ဝင်ရနိုင်ရန် subscription လိုအပ်သည်
   - အချို့ feature များသည် တိုင်းဒေသ အလိုက်ကွဲပြားသည်
   - သင့် Azure OpenAI model deployment သည် Responses API ကို ထောက်ပံ့မှု ရှိရမည်

### သင်ယူမှု လမ်းကြောင်း

သင်္ကေတ သင်ခန်းစာများ လမ်းညွှန်ချက်အတိုင်း အဆင့်ဆင့် လေ့လာရန်:
၁။ **00-course-setup** - ပတ်ဝန်းကျင် အဆင်သင့် ပြုလုပ်မှု စတင်မှု
၂။ **01-intro-to-ai-agents** - AI agent များ၏ အခြေခံများနားလည်ရန်
၃။ **02-explore-agentic-frameworks** - အသုံးပြုနိုင်သော Framework များကို လေ့လာရန်
၄။ **03-agentic-design-patterns** - အခြေခံဒီဇိုင်းပုံစံများ
၅။ နံပါတ်ခွဲစဉ်ဆက်လက် လေ့လာရန်

### Framework ရွေးချယ်မှု

သင့်ရဲ့ရည်ရွယ်ချက်အလိုက် Framework ရွေးပါ:
- **ခန်းများအားလုံး**: Microsoft Agent Framework (MAF) ကို `FoundryChatClient` နှင့် အသုံးပြုပါ
- Microsoft Foundry Agent Service V2 တွင် အေးဂျင့်များ server-side မှတ်ပုံတင်ပြီး Foundry portal တွင် မြင်ရသည်

### ကူညီမှုရယူခြင်း

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) တွင် ပါဝင်ဆောင်ရွက်ပါ
- သင်ခန်းစာ README ဖိုင်များကို မြင်ပြီး မည်သည့်အကြံညဏ် မဆို လေ့လာပါ
- သင်တန်းအနှစ်ချုပ်အတွက် [README.md](./README.md) ကို ပြန်လည်ကြည့်ပါ
- အနက်ရှိုင်းဆုံး စတင်ပုံများအတွက် [Course Setup](./00-course-setup/README.md) ကို ကြည့်ရှုပါ

### ပါဝင်ဆောင်ရွက်ခြင်း

ဒီပရောဂျက်သည် ဖွင့်လှစ် သင်ကြားရေးပရောဂျက်ပါ။ ပါဝင်ထားခြင်းကို ကြိုဆိုပါသည်။
- ကုဒ်နမူနာများတိုးတက်အောင် ပြုလုပ်ပါ
- မှားယွင်းချက်များပြင်ဆင်ပါ
- ရှင်းလင်းတဲ့ မှတ်ချက်များ ထည့်သွင်းပါ
- သင်ခန်းစာအကြောင်းအရာ အသစ် စိတ်ကူးထည့်သွင်းပါ
- ဘာသာစကား များစွာ သို့ ဘာသာပြန်ခြင်းလုပ်ပါ

လတ်တလောလိုအပ်ချက်များအတွက် [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) ကို ကြည့်ရှုပါ။

## စီမံကိန်းအထူး ဆောင်ရန်အချက်များ

### ဘာသာစကား မျိုးစုံထောက်ပံ့မှု

ဒီ repository တွင် အလိုအလျောက် ဘာသာပြန်စနစ် အသုံးပြုသည်။
- ၅၀ ကျော် ဘာသာစကား ထောက်ပံ့ထားသည်
- ဘာသာပြန်မှုကို `/translations/<lang-code>/` ဒိုင်ရက်တာရီများတွင် သိမ်းဆည်းထားသည်
- GitHub Actions workflow သည် ဘာသာပြန်ချက်များ update လုပ်ခြင်းကို ကိုင်တွယ်သည်
- မူရင်းဖိုင်များ သည် repository အမြစ်တွင် အင်္ဂလိပ်စာဖြင့် ရှိသည်

### ခန်းသို့မဟုတ် သင်ခန်းစာ ဖွဲ့စည်းပုံ

တစ်ခန်းစီသည် ပုံမွန် pattern အတိုင်း လိုက်နာသည်။
၁။ ဗွီဒီယို thumbnail နှင့်လင့်ခ်
၂။ စာဖြင့်ရေးသားထားသော သင်ခန်းစာ အကြောင်းအရာ (README.md)
၃။ Framework များစွာမှ ကုဒ်နမူနာများ
၄။ သင်ယူရန် ရည်မှန်းချက်များ နှင့် လိုအပ်ချက်များ
၅။ အပို သင်ယူရအောင် အရင်းအမြစ်များ ချိတ်ဆက်ထားသည်

### ကုဒ်နမူနာ ဖိုင်အမည်ပုံစံ

ပုံစံ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lesson 1, MAF Python
- `14-sequential.ipynb` - Lesson 14, MAF advanced patterns

### အထူး ဒိုင်ရက်တာရီများ

- `translated_images/` - ဘာသာပြန်ပြုလုပ်ထားသော ပုံများ
- `images/` - အင်္ဂလိပ်လက်မှတ် ပုံများ
- `.devcontainer/` - VS Code ဖွံ့ဖြိုးရေး ကွန်တိနာ စတင်ရန် ဖိုင်များ
- `.github/` - GitHub Actions workflow နှင့် အစီအစဉ်များ

### လိုအပ်သော Dependency များ

`requirements.txt` မှ အဓိက အထောက်အကူပြု package များ:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol ပံ့ပိုးမှု
- `azure-ai-inference`, `azure-ai-projects` - Azure AI ဝန်ဆောင်မှုများ
- `azure-identity` - Azure အတည်ပြုချက် (AzureCliCredential)
- `azure-search-documents` - Azure AI Search တွဲဖက်မှု
- `mcp[cli]` - Model Context Protocol ပံ့ပိုးမှု

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->