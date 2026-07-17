# AGENTS.md

## ပရောဂျက် အကျဉ်းချုပ်

ဤ repository သည် "အစရှိသူများအတွက် AI Agents" ဆိုသော - AI Agents တည်ဆောက်ရန် လိုအပ်သော အချက်အလက်များအားလုံးကို သင်ကြားပေးသည့် အပြည့်အစုံ ပညာရေးသင်တန်း ဖြစ်သည်။ သင်တန်းတွင် ၁၈ သင်ခန်းစာ (နံပါတ် ၀၀ မှ ၁၈ ထိ) ပါဝင်ပြီး အခြေခံအဆောက်အအုံများ၊ ဒီဇိုင်းပုံစံများ၊ ဖရိမ်ဝတ်များ၊ ထုတ်လုပ်မှုတင်ချခြင်း၊ ဒေသခံ/စက်ပစ္စည်းပေါ်တွင် run မည့် agents များ နှင့် AI agents များ၏ လုံခြုံရေးတို့ကို ဖောက်ပြန်သင်ကြားသည်။

**အဓိက နည်းပညာများ:**
- Python 3.12+
- အပြန်အလှန်လေ့လာမှုအတွက် Jupyter Notebooks
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**ဖွဲ့စည်းမှု:**
- သင်ခန်းစာအခြေခံ ဖိုင်ဖွဲ့စည်းမှု (၀၀-၁၅+ ဒိုင်ရက်ထရီများ)
- သင်ခန်းစာတိုင်းတွင်: README စာတမ်း, ကုဒ်နမူနာများ (Jupyter notebooks), ပုံများ ပါဝင်သည်
- အလိုအလျောက် ဘာသာပြန်စနစ်ဖြင့် ဘာသာစကားစုံထောက်ပံ့မှု
- သင်ခန်းစာတစ်ခုလျှင် Microsoft Agent Framework ကို အသုံးပြုသော Python notebook တစ်ခု

## အဆင်သင့် တည်ဆောက်ခြင်းအမိန့်များ

### လိုအပ်ချက်များ
- Python 3.12 သို့ မျှတ거나 उच्चतर ဗားရှင်း
- Azure subscription (Microsoft Foundry အတွက်)
- Azure CLI ကို install လုပ်ပြီး authenticated (`az login`)

### အစပိုင်း တည်ဆောက်ခြင်း

1. **Repository ကို clone သို့ fork လုပ်ပါ:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ဒါမှမဟုတ်
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python virtual environment ဖန်တီး၍ ဖွင့်ပါ:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows တွင်: venv\Scripts\activate
   ```

3. **လိုအပ်သော package များ install လုပ်ပါ:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment variable များကို သတ်မှတ်ပါ:**
   ```bash
   cp .env.example .env
   # သင်၏ API keys နှင့် endpoints များဖြင့် .env ကိုတည်းဖြတ်ပါ
   ```

### လိုအပ်သော Environment Variable များ

**Microsoft Foundry** အတွက် (လိုအပ်သည်):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment အမည် (ဥပမာ gpt-4.1-mini)

**Azure AI Search** အတွက် (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Notebook များ run မပြုမီ `az login` ကို အသုံးပြုပါ (သုံးသည်မှာ `AzureCliCredential` ဖြစ်သည်)။

## ဖွံ့ဖြိုးတိုးတက်ရေး လုပ်ငန်းစဉ်

### Jupyter Notebooks ဖန်တီးခြင်းနှင့် လည်ပတ်ခြင်း

သင်ခန်းစာတိုင်းတွင် ဖရိမ်ဝတ်အမျိုးမျိုးအတွက် Jupyter notebook များ ပါဝင်သည်။

1. **Jupyter စတင်ပါ:**
   ```bash
   jupyter notebook
   ```

2. **သင်ခန်းစာ ဒိုင်ရက်ထရီ သို့ သွားပါ** (ဥပမာ: `01-intro-to-ai-agents/code_samples/`)

3. **Notebook များ ဖွင့်၍ လုပ်ဆောင်ပါ:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) အသုံးပြုခြင်း
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) အသုံးပြုခြင်း

### Microsoft Agent Framework ဖြင့် လုပ်ကိုင်ခြင်း

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure subscription လိုအပ်သည်
- Agent Service V2 အတွက် `FoundryChatClient` အသုံးပြုသည် (Foundry portal တွင် မြင်တွေ့နိုင်သည်)
- ထုတ်လုပ်မှုအတွက် ပြင်ဆင်ပြီး observability built-in ဖြစ်သည်
- ဖိုင်ပုံစံ: `*-python-agent-framework.ipynb`

## စစ်ဆေးမှုလမ်းညွှန်ချက်များ

ဤသည်သည် ပညာရေးအတွက် repository ဖြစ်ကာ automated tests အား မပါဝင်ပါ၊ သင့်တည်ဆောက်မှုနှင့် ပြင်ဆင်မှုများကို စစ်ဆေးရန်:

### ကိုယ်တိုင်စစ်ဆေးခြင်း

1. **Python ပတ်ဝန်းကျင်စစ်ဆေးရမည်:**
   ```bash
   python --version  # ၃.၁၂ နှင့်အထက်ဖြစ်ရမည်။
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Notebook များ ဆောင်ရွက်မှု စစ်ဆေးရမည်:**
   ```bash
   # နိုတ်ဘွတ်ကို script အဖြစ်ပြောင်းပြီး ပြေးဆော့ရန် (စမ်းသပ်မှု imports များ)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Environment variables များကို အတည်ပြုရမည်:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### သီးသန့် Notebook များ Run ပြုလုပ်ခြင်း

Jupyter တွင် Notebook များဖွင့်ပြီး အဆင့်လိုက် cell များကို ဆောင်ရွက်ပါ။ Notebook တစ်ခုချင်းစီသည် အလိုအလျောက် မိမိကိုယ်ပိုင်ဖြစ်ပြီး အောက်ပါအစိတ်အပိုင်းများ ပါဝင်သည်-
- Import ပြုလုပ်ထားသော အကြောင်းအရာများ
- သတ်မှတ်ချက်များ ရယူခြင်း
- Agent နမူနာများ
- Markdown cell များတွင် မျှော်မှန်း output များ

### Smoke ကာကွယ်စစ်ဆေးမှု Microsoft Foundry Hosted Agent များအတွက်

01, 04, 05, 16 သင်ခန်းစာများတွင် agent များကို Microsoft Foundry hosted agent အနေနှင့် တည်ဆောက်ထားပါက tests/ တွင် smoke-test catalogs သေချာရေးဖော်ပြထားပြီး .github/workflows/smoke-test.yml workflow မှ AI Smoke Test action ကို သုံးပြီး ပြုလုပ်သည်။ ၎င်းသည် တင်ချီးပြီးနောက် gate အနေနှင့် အိမ်ကွင်းမော်ဒယ်၏ ဖော်ပြချက် (prompt expectations) များနှင့် ဇဈပုံတည်ရှိမှု စစ်ဆေးသည်။ Lessons 10 နှင့် 16 ရှိ ဤဖော်ပြချက်ခုနှစ်န်းကို မြှင့်တင်သည်။ tests/README.md တွင် catalog-to-lesson-to-agent mapping ကြည့်ရှုနိုင်သည်။ Lesson 17 သည် Foundry Local နဲ့ ဒေသခံအနေဖြင့် run လျှက်ရှိပြီး hosted endpoint မရှိ၊ ထိုသို့ ဖြစ်သည့်အတွက် သင့် notebook ကို တိုက်ရိုက် run ပြုလုပ်၍ စစ်ဆေးသည်။

## ကုဒ်ပုံစံ

### Python အကြောင်းအရာများ

- **Python ဗားရှင်း**: 3.12+
- **ကုဒ်ပုံစံ**: စံပုံမှန် Python PEP 8 ကိုလိုက်နာပါ
- **Notebook များ**: အကြောင်းအရာရှင်းလင်းအောင် markdown cell များအသုံးပြုပါ
- **Import များ**: စံ library, third-party, ဒေသခံ import များအလိုက် အုပ်စုဖွဲ့ပါ

### Jupyter Notebook အလေ့အထ

- Code cell မတိုင်မီ ဖော်ပြချက်များပါသော markdown cells များ ထည့်သွင်းပါ
- Notebook များတွင် output ဥပမာများ ထည့်သွင်းပါ
- သင်ခန်းစာ အယူအဆနှင့် ကိုက်ညီသော variable အမည်များ အသုံးပြုပါ
- Notebook လုပ်ဆောင်မှု အစီအစဉ်ကို တန်းတူ ထိန်းသိမ်းပါ (cell ၁ → ၂ → ၃...)

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

## ဆောက်လုပ်ခြင်းနှင့် တင်ချခြင်း

### စာရွက်စာတမ်းဆောက်ခြင်း

ဤ repository သည် Markdown ကို စာရွက်စာတမ်းအတွက် အသုံးပြုသည်:
- သင်ခန်းစာတိုင်းအတွက် README.md ဖိုင်များ
- repository အခြေခံရှိ Main README.md
- GitHub Actions ဖြင့် အလိုအလျောက် ဘာသာပြန်စနစ်

### CI/CD pipeline

`.github/workflows/` တွင် တည်ရှိသည်:

1. **co-op-translator.yml** - ၅၀+ ဘာသာစကားသို့ အလိုအလျောက် ဘာသာပြန်ခြင်း
2. **welcome-issue.yml** - အသစ်တင်သည့် issue ဖန်တီးသူ မိတ်ဆက်
3. **welcome-pr.yml** - အသစ်တင်သည့် pull request ပူးတွဲဝင်သူ မိတ်ဆက်

### တင်ချခြင်း

ဤသည်မှာ ပညာရေးအတွက် repository ဖြစ်သည် - တင်ချခြင်း လုပ်ငန်းစဉ် မရှိပါ။ အသုံးပြုသူများ -
1. Repository ကို fork သို့ clone ပြုလုပ်ပါ
2. Notebook များကို ဒေသခံ သို့ GitHub Codespaces တွင် run ပြုလုပ်ပါ
3. နမူနာပြောင်းလဲခြင်းနှင့် စမ်းသပ်ခြင်းဖြင့် သင်ယူပါ

## Pull Request လမ်းညွှန်ချက်များ

### တင်သွင်းမရောက်မီ

1. **သင်ပြုလုပ်ထားသော အပြောင်းအလဲများစစ်ဆေးပါ:**
   - သက်ဆိုင်ရာ notebook များ အပြည့်အစုံ run ပြုလုပ်ပါ
   - cell များ မည်သည့် error မရှိစွာ run ဖြစ်မည်ကို အတည်ပြုပါ
   - output များမှန်ကန်မှုကို စစ်ဆေးပါ

2. **စာရွက်စာတမ်း ပြင်ဆင်မှုများ:**
   - အသစ်တိုးထည့်ထားသော အယူအဆများအတွက် README.md ကို ပြင်ဆင်ပါ
   - ရှုပ်ထွေးသော code များအတွက် notebook တွင် မှတ်ချက်ထည့်ပါ
   - markdown cell များက ရည်ရွယ်ချက်ကို ဖော်ပြပါ

3. **ဖိုင်ပြောင်းလဲမှုများ:**
   - `.env` ဖိုင်များ commit မလုပ်ပါ (`.env.example` ကိုအသုံးပြုပါ)
   - `venv/` သို့မဟုတ် `__pycache__/` ဒိုင်ရက်ထရီ မထည့်ပါနှင့်
   - တင်ပြချက်အနေဖြင့် notebook output များကို သိမ်းဆည်းပါ
   - ယာယီဖိုင်များနှင့် backup notebook များ (`*-backup.ipynb`) ဖယ်ရှားပါ

### PR ခေါင်းစဉ် ပုံစံ

ဖော်ပြချက်တိတိပြောပါ-
- `[Lesson-XX] <concept> အတွက် နမူနာအသစ် ထည့်သွင်းခြင်း`
- `[Fix] lesson-XX README မှ စာလုံးထဲ သိပ်အမှားများ ပြင်ခြင်း`
- `[Update] lesson-XX ကုဒ်နမူနာ တိုးတက်အောင် ပြင်ဆင်ခြင်း`
- `[Docs] တပ်ဆင်ရေးလမ်းညွှန် များ ပြင်ဆင်ခြင်း`

### လိုအပ်သော စစ်ဆေးမှုများ

- Notebook များ error မရှိစွာ run ဖြစ်ရမည်
- README ဖိုင်များ သန့်ရှင်းမြင်သာ ရှိရမည်
- Repository အတွင်းရှိ အခက်အခဲ မပါသော code နမူနာများနှင့် လိုက်နာရမည်
- အခြားသင်ခန်းစာများနှင့် သဟဇာတ ဖြစ်ရမည်

## အပို မှတ်ချက်များ

### နှုတ်ဆက်စရာ အသိပေးချက်များ

1. **Python ဗားရှင်း မကိုက်ညီခြင်း:**
   - Python 3.12+ ကို အသုံးပြုရေး သေချာပါ
   - အချို့ package များဟာ အနည်းငယ်အဟောင်းဗားရှင်းတွင် မအောင်မြင်နိုင်ပါ
   - `python3 -m venv` ဖြင့် Python ဗားရှင်းကို တိတိကျကျ သတ်မှတ်ပါ

2. **Environment variables:**
   - `.env` ကို `.env.example` မှ ဖန်တီးပါ
   - `.env` ဖိုင်ကို commit မလုပ်ပါ (gitignore ထဲတွင် ပါဝင်သည်)
   - keyless Entra ID authentication အတွက် `az login` ဖြင့် လက်မှတ်ထိုးပါ

3. **Package conflicts:**
   - အသစ်ဖန်တီးထားသော virtual environment ကို အသုံးပြုပါ
   - အမျိုးမျိုး package များထက် `requirements.txt` မှ install လုပ်ပါ
   - အချို့ notebook များတွင် markdown cell များ၌ ပြောထားသည့် အပို packages လိုတယ်

4. **Azure စေဝန်ဆောင်မှုများ:**
   - Azure AI service များသည် အသုံးပြုမှု subscription လိုအပ်သည်
   - အချို့ features များသည် ဒေသအလိုက် ကွာခြားသည်
   - သင့် Azure OpenAI model deployment သည် Responses API ကို ပံ့ပိုးထားရန် သေချာပါစေ

### သင်ယူရန် လမ်းကြောင်း

သင်ခန်းစာများ အလိုက်လိုက်တူ တိုးတက် ဖို့ အကြံပြုသည်:
1. **00-course-setup** - ပတ်ဝန်းကျင် တပ်ဆင်ရန် စတင်ပါ
2. **01-intro-to-ai-agents** - AI agent အခြေခံ သိရှိရန်
3. **02-explore-agentic-frameworks** - framework အမျိုးမျိုးကို သင်ယူရန်
4. **03-agentic-design-patterns** - အဓိက ဒီဇိုင်းပုံစံများ
5. နံပါတ်စဉ်အတိုင်း သင်ခန်းစာများ ဆက်လက် လေ့လာပါ

### framework ရွေးချယ်ခြင်း

ကိုယ်ကို လိုအပ်သည်အတိုင်း framework ရွေးပါ:
- **သင်ခန်းစာအားလုံး**: Microsoft Agent Framework (MAF) နှင့် `FoundryChatClient`
- **Agents များ server-side တွင် Microsoft Foundry Agent Service V2 မှာ register ဖြစ်ပြီး Foundry portal တွင် မြင်တွေ့ရသည်**

### အကူအညီ ရရန်

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) တွင် ပူးပေါင်းပါ
- သတ်မှတ်ထားသည့် သင်ခန်းစာ README ဖိုင်များကို စစ်ဆေးပါ
- ပရောဂျက်အကျဉ်းချုပ်အတွက် [README.md](./README.md) ကို ကြည့်ပါ
- အသေးစိတ် တပ်ဆင်ခြင်းအတွက် [Course Setup](./00-course-setup/README.md) ကို ခေါ်ယူပါ

### ပါဝင်ဆောင်ရွက်ခြင်း

ဤသည်မှာ ပညာရေးအတွက် ဖွင့်လှစ်သော ပရောဂျက်ဖြစ်သည်။ ပူးပေါင်း ဆောင်ရွက်မှုများအား လက်ခံပါသည်-
- ကုဒ်နမူနာများ မြှင့်တင်ထည့်သွင်းခြင်း
- စာအမှား သို့မဟုတ် အမှားများ ပြင်ဆင်ခြင်း
- သပ်သပ်ရှင်းရှင်း မှတ်ချက်များ ထည့်သွင်းခြင်း
- သင်ခန်းစာ အကြောင်းအရာ အသစ် အကြံပြုခြင်း
- အခြားဘာသာစကားများသို့ ဘာသာပြန်ခြင်း

လတ်တလော လိုအပ်ချက်များအတွက် [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) ကို ကြည့်ပါ။

## ပရောဂျက် အထူးပြုပြင်ချက်များ

### ဘာသာစကားစုံ ထောက်ပံ့မှု

ဤ repository သည် အလိုအလျောက် ဘာသာပြန်စနစ် အသုံးပြုသည်-
- ၅၀+ ဘာသာစကား ထောက်ပံ့သည်
- `/translations/<lang-code>/` ဒိုင်ရက်ထရီများတွင် ဘာသာပြန်ချက်များရှိသည်
- GitHub Actions workflow က ဘာသာပြန်အပ်ဒိတ်များ ကိုင်တွယ်သည်
- မူလအားဖြင့် repository အခြေခံရှိ အင်္ဂလိပ်ဖိုင်များ

### သင်ခန်းစာ ဖွဲ့စည်းမှု

သင်ခန်းစာတိုင်းသည် စံနမူနာ တစ်ခုလိုက်နာသည်-
1. ဗီဒီယိုတံဆိပ်ပုံနှင့် Link
2. ရေးသားထားသော သင်ခန်းစာ အကြောင်းအရာ (README.md)
3. ကုဒ်နမူနာ များ (ဖရိမ်ဝတ်စုံ)
4. သင်ယူရမည့် ရည်မှန်းချက်များနှင့် ကြိုတင်လိုအပ်ချက်များ
5. ထပ်ဆောင်း သင်ယူရေး အရင်းအမြစ်များ အတွက် လင့်ခ်ဖြင့် ပံ့ပိုးခြင်း

### ကုတ်နမူနာ ဖိုင်အမည် သတ်မှတ်ခြင်း

ပုံစံ: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - သင်ခန်းစာ ၁, MAF Python
- `14-sequential.ipynb` - သင်ခန်းစာ ၁၄, MAF ခေါင်းထွက်ပုံစံများ (အဆင့်မြင့်)
- `16-python-agent-framework.ipynb` - သင်ခန်းစာ ၁၆, ထုတ်လုပ်မှု ဖောက်သည်ထောက်ခံမှု agent
- `17-local-agent-foundry-local.ipynb` - သင်ခန်းစာ ၁၇, ဒေသခံ agent နှင့် Foundry Local + Qwen အသုံးပြုခြင်း

### အထူး ဒိုင်ရက်ထရီများ

- `translated_images/` - ဘာသာပြန်ပုံများ (ဒေသစံအတိုင်း)
- `images/` - အင်္ဂလိပ် အကြောင်းအရာ မူရင်း ပုံများ
- `.devcontainer/` - VS Code ဖွံ့ဖြိုးရေး ကွန်တိန်နာ သတ်မှတ်ချက်
- `.github/` - GitHub Actions workflow များနှင့် template များ

### မူလ အခြေခံ package များ

`requirements.txt` မှ အဓိက packages:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol support
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure authentication (AzureCliCredential)
- `azure-search-documents` - Azure AI Search အစိတ်အပိုင်း
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->