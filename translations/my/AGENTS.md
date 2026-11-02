# AGENTS.md

## စီမံကိန်းအနှစ်ချုပ်

ဤ မှတ်တမ်းတွဲတွင် "အစပိုင်းအတွက် AI ကိုယ်စားလှယ်များ" ပါရှိသည် - AI ကိုယ်စားလှယ်များ ဖန်တီးရန် လိုအပ်သော အားလုံးကို သင်ကြားပေးသည့် လေ့လာရေးသင်တန်းတစ်ခု ဖြစ်သည်။ သင်တန်းတွင် အခြေခံအကြောင်းအရာများ၊ ဒီဇိုင်းပုံစံများ၊ ဖရိမ်းဝတ်များ၊ ထုတ်လုပ်မှု တင်သွင်းခြင်း၊ ဒေသတွင်း/စက်ပေါ်ကိုယ်စားလှယ်များနှင့် AI ကိုယ်စားလှယ်များ၏ လုံခြုံမှုများကို ကိုင်တွယ်သော သင်ခန်းစာ ၁၈ ခု (00-18 နံပါတ်လိုက်) ပါဝင်သည်။

**အဓိကနည်းပညာများ -**
- Python 3.12+
- အသုံးပြု၍လေ့လာရန် Jupyter Notebooks
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**ဖွဲ့စည်းပုံ -**
- သင်ခန်းစာအလိုက် ဖိုင်ဖိုဒါများ (00-18)
- တစ်ခုချင်းစီတွင် README စာတမ်း၊ ကုဒ်နမူနာများ (Jupyter notebooks), ဓာတ်ပုံများ ပါဝင်
- အလိုအလျောက် ဘာသာပြန်စနစ်ဖြင့် မျိုးစုံဘာသာဖြင့် ထောက်ပံ့မှု
- Microsoft Agent Framework ကို အသုံးပြုသည့် Python notebook တစ်ခုစီ

## ဆက်တင်ကမ်းလှမ်းချက်များ

### ကြိုတင်လိုအပ်ချက်များ
- Python 3.12 သို့မဟုတ် အထက်
- Azure subscription (Microsoft Foundry အတွက်)
- Azure CLI တပ်ဆင်ပြီး အတည်ပြုထား (`az login`)

### ပထမဆုံချက် ဆက်တင်ခြင်း

1. **မှတ်တမ်းတွဲကို ကလုန်းလို့ ဒါမှမဟုတ် ဂျုံရိုးလုပ်ပါ -**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python virtual environment တစ်ခု ဖန်တီးပြီး အလုပ်လုပ်အောင်လုပ်ပါ -**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **လိုအပ်သော ဆော့ဖ်ဝဲများ ထည့်သွင်းပါ -**
   ```bash
   pip install -r requirements.txt
   ```

4. **ပတ်ဝန်းကျင်အ_VARIABLE_ များ ရေးထည့်ပါ -**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### လိုအပ်သော ပတ်ဝန်းကျင်အ_VARIABLE_ များ

**Microsoft Foundry အတွက်** (လိုအပ်သည်) -
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry ပရောဂျက် အဆုံးအချက်
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - မော်ဒယ် တင်သွင်းအမည် (ဥပမာ gpt-5-mini)

**Azure AI Search အတွက်** (သင်ခန်းစာ 05 - RAG) -
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search အဆုံးအချက်
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

အတည်ပြုခြင်း - notebook မများကို ပြေးရန်မတိုင်မီ `az login` ကို ပြေးပါ (`AzureCliCredential` ကို အသုံးပြုသည်)။

## ဖွံ့ဖြိုးတိုးတက်မှု လုပ်ငန်းစဉ်

### Jupyter Notebooks များ ရှေ့ဆောင်ပြေးခြင်း

တစ်ခုချင်းသင်ခန်းစာတွင် ဖရိမ်းဝတ်မတူများ အတွက် Jupyter notebooks များ ပါရှိသည် -

1. **Jupyter ကို စတင်ပါ -**
   ```bash
   jupyter notebook
   ```

2. **သင်ခန်းစာ ဖိုဒါသို့ သွားပါ** (ဥပမာ `01-intro-to-ai-agents/code_samples/`)

3. **မှတ်တမ်းများ ဖွင့်ပြီး ကွက်များ အဆက်လိုက် အလုပ်လုပ်ပါ -**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework ဖြင့် (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework ဖြင့် (.NET)

### Microsoft Agent Framework နှင့်အတူ လုပ်ငန်းလုပ်ခြင်း

**Microsoft Agent Framework + Microsoft Foundry -**
- Azure subscription လိုအပ်သည်
- Agent Service V2 အတွက် `FoundryChatClient` ကို အသုံးပြုသည် (Foundry portal တွင် ကိုယ်စားလှယ်များ မြင်နိုင်)
- ထုတ်လုပ်မှုအဆင့်အတွက် observability built-in ပါရှိသည်
- ဖိုင်ပုံစံ - `*-python-agent-framework.ipynb`

## စမ်းသပ်ရန် လမ်းညွှန်ချက်များ

ဤသည် သင်ကြားရေးမှတ်တမ်းတွဲဖြစ်ပြီး ထုတ်လုပ်မှုကုဒ် မဟုတ်သဖြင့် အလိုအလျောက် စမ်းသပ်မှု မပါရှိပါ။ သင်၏ ဆက်တင်နှင့် အပြောင်းအလဲများကို စစ်ဆေးရန် -

### လက်တွေ့စမ်းသပ်ခြင်း

1. **Python ပတ်ဝန်းကျင် စမ်းသပ်သည် -**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Notebook နဲ့ cell များ စမ်းသပ်ကြည့်သည် -**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **ပတ်ဝန်းကျင်အ_VARIABLE_ များစစ်ကြည့်ပါ -**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### တစ်ခုချင်း Notebook များ လည်ပတ်ခြင်း

Jupyter တွင် notebook များဖွင့်ပြီး cells များ အဆက်လိုက် အလုပ်လုပ်ပါ။ တစ်ခုချင်း ဖိုင်တွင် ပါဝင်သည် -
- တင်သွင်းချက်များ
- ဆက်တင်ဖြတ်တောက်ခြင်း
- ဥပမာ ကိုယ်စားလှယ်များ အကောင်အထည်ဖော်ချက်များ
- Markdown cell များတွင် မျှော်မှန်းခြေ output များ

### ထုတ်လုပ်ပြီး ကိုယ်စားလှယ်များ အတွက် Smoke-Test လုပ်ခြင်း

Microsoft Foundry တွင် တင်သွင်းထားသော ကိုယ်စားလှယ်များ (01, 04, 05, 16) အတွက် ဤ repo မှ smoke-test စာရင်းများ `tests/` အောက်တွင် ပါရှိပြီး `.github/workflows/smoke-test.yml` workflow ဖြင့် [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) အရေးပါမှုကဲ့သို့ ပြေးဆဲဖြစ်သည်။ ၎င်းမှာ တင်သွင်းပြီးနောက် gate (ကိုယ်စားလှယ် ရောက်ရှိနိုင်ပြီး မူလ prompt တောင်းဆိုချက်များကို လိုက်နာနေစစ်ဆေးခြင်း) ျဖစ္ပြီး သင်ခန်းစာ 10 နှင့် 16 တွင် ရှိသော အကဲဖြတ်မှု အစီအစဉ်ကို ဖြည့်ဆည်းသည်။ Catalog မှ သင်ခန်းစာမှ ကိုယ်စားလှယ်ဆီသို့ mapping အတွက် [tests/README.md](./tests/README.md) ကို ကြည့်ပါ။ သင်ခန်းစာ 17 သည် Foundry Local နှင့် ဒေသတွင်း၌ လည်ပတ်သည့် agents ဖြစ်ပြီး hosted endpoint မရှိသဖြင့် notebook ကို တိုက်ရိုက် ပြေး၍ စစ်ဆေးသည်။

## ကုဒ်စတိုင်

### Python အညွှန်းများ

- **Python ဗားရှင်း**: 3.12+
- **ကုဒ်စတိုင်**: စံနမူနာ Python PEP 8 အညွှန်းများကို လိုက်နာပါ
- **Notebooks**: အကြောင်းအရာများ ရှင်းလင်းသော markdown cell များ အသုံးပြုပါ
- **တင်သွင်းချက်များ**: စံ library, တတိယအဖက်, ဒေသခံ တင်သွင်းချက် များအလိုက် အုပ်စုဖွဲ့ပါ

### Jupyter Notebook အညွှန်းများ

- ကုဒ် cell မတိုင်မီ ရှင်းလင်းဖေါ်ပြသော markdown cell များပါပါစေ
- ကိုးကားရန် output ဥပမာများ notebook များတွင် ထည့်သွင်းပါ
- သင်ခန်းစာ အကြောင်းအရာနှင့် ကိုက်ညီသော ပြောင်းလဲနိုင်သော variable အမည်များ အသုံးပြုပါ
- notebook ရှေ့ဆက်မှု အစီအစဉ်ကို လိုက်နာပါ (cell 1 → 2 → 3 ...)

### ဖိုင် အစီအစဉ်

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## ဆောက်လုပ်ခြင်း နှင့် တင်သွင်းခြင်း

### စာတမ်းများ ဆောက်လုပ်ခြင်း

ဤ မှတ်တမ်းတွဲသည် Markdown ကို စာတမ်းရေးရန် အသုံးပြုသည်။
- သင်ခန်းစာတိုင်းတွင် README.md ဖိုင်များ
- မှတ်တမ်းတွဲ၏ အမြစ်တွင် မူလ README.md
- GitHub Actions ဖြင့် အလိုအလျောက် ဘာသာပြန်စနစ်

### CI/CD လမ်းကြောင်း

`.github/workflows/` တွင်တည်ရှိသည်။

1. **co-op-translator.yml** - ဘာသာစကား ၅၀ ကျော်သို့ အလိုအလျောက် ဘာသာပြန်ခြင်း
2. **welcome-issue.yml** - အသစ်ဖြစ်သော issue ဖန်တီးသူများကို ကြိုဆိုခြင်း
3. **welcome-pr.yml** - အသစ်ဖြစ်သော pull request ကမ်းလှမ်းသူများကို ကြိုဆိုခြင်း

### တင်သွင်းခြင်း

ဤသည် သင်ကြားရေးမှတ်တမ်းတွဲဖြစ်ပြီး တင်သွင်းခြင်း လုပ်ငန်းစဉ် မရှိပါ။ အသုံးပြုသူများသည် -
1. မှတ်တမ်းတွဲကို ကလုန်းရန် သို့မဟုတ် fork လုပ်ရန်
2. notebook များကို ဒေသတွင်း သို့ GitHub Codespaces တွင် ပြေးရန်
3. ဥပမာများကို ပြင်ဆင် နှင့် စမ်းသပ်ခြင်းဖြင့် သင်ယူရန်

## Pull Request လမ်းညွှန်ချက်များ

### တင်သွင်းရန် မတိုင်မီ

1. **ပြင်ဆင်မှုများ စမ်းသပ်ပါ -**
   - ထိခိုက်သည့် notebook များ အပြည့်အ၀ ပြေးရန်
   - cell များ Error မရှိစွာ အလုပ်လုပ်မှု များ စစ်ဆေးရန်
   - output များ သင့်တော်မှန်ကန်မှု ကြည့်ရန်

2. **စာတမ်းများ အပ်ဒိတ်လုပ်ရန် -**
   - အသစ်သော အကြောင်းအရာ ထည့်သွင်းပါက README.md ကို အသစ်လုပ်ပါ
   - ကြမ်းသပ်လှုပ်ရှားမှုနည်းသော ကုဒ်လမ်းညွှန်ချက်များ notebook တွင် ထည့်သွင်းပါ
   - markdown cell များသည် ရည်ရွယ်ချက် ရှင်းလင်းရေး အတွက် အသုံးပြုရန်

3. **ဖိုင် ပြင်ဆင်မှုများ -**
   - `.env` ဖိုင်များ မတင်ရန် မလိုအပ်ပါ (`.env.example` သုံးပါ)
   - `venv/` သို့မဟုတ် `__pycache__/` ဖိုဒါ မတင်ပါနှင့်
   - သင်ခန်းစာ အကျဉ်းချုပ်အတွက် notebook output များ သိမ်းဆည်းရန်
   - ခဏခဏဖိုင်များ နှင့် အထောက်အထား notebook များ ( `*-backup.ipynb` ) ဖယ်ရှားရန်

### PR ခေါင်းစဉ် ပုံစံ

ရှင်းလင်း ဖေါ်ပြချက် ခေါင်းစဉ် အသုံးပြုပါ -
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### လိုအပ်သော စစ်ဆေးမှုများ

- Notebook များ Error မရှိစေ ပြေးရမည်
- README ဖိုင်များ ရှင်းလင်း သေချာရမည်
- မှတ်တမ်းတွဲအတွင်း ရှိတည့်‌ရန် ကုဒ်ပုံစံများနှင့် လိုက်နာရမည်
- အခြား သင်ခန်းစာများနှင့် တစ်ညီတစ်သူ ရှိရန် ပြုလုပ်ရမည်

## နောက်ထပ် မှတ်ချက်များ

### ရောင့်ရဲလို့ဖြစ်နိုင်သည့်အချက်များ

1. **Python ဗားရှင်း မကိုက်ညီမှု -**
   - Python 3.12+ သုံးထားစေရန်
   - အချို့ package များ ဟောင်းရှေး ဗားရှင်း မသုံးနိုင်ပါ
   - Python ဗားရှင်းကို အသေးစိတ် သတ်မှတ်ရန် `python3 -m venv` သုံးပါ

2. **ပတ်ဝန်းကျင် အ_VARIABLE_ များ -**
   - `.env` ကို `.env.example` မှ ပြုလုပ်စေပါ
   - `.env` ဖိုင် ကို မတင်သင့်ပါ (`.gitignore` တွင်ရှိသည်)
   - `az login` ဖြင့် ဝင်ရောက်ပြီး keyless Entra ID အတည်ပြုမှု လုပ်ပါ

3. **Package ဆန့်ကျင်မှုများ -**
   - အသစ် ဖ virtual environment အသုံးပြုပါ
   - package များကို တစ်ခုချင်းထဲမှ မဟုတ်ဘဲ `requirements.txt` မှ တပ်ဆင်ပါ
   - အချို့ notebook များတွင် markdown cell များတွင် ဖော်ပြထားသည့် အပို package များ လိုအပ်နိုင်သည်

4. **Azure ဝန်ဆောင်မှုများ -**
   - Azure AI ဝန်ဆောင်မှုများ အဖွင့် subscription လိုအပ်သည်
   - အချို့ စွမ်းဆောင်ချက်များ သီးခြား ဒေသအလိုက် အကန့်အသတ် ရှိသည်
   - Azure OpenAI မော်ဒယ် တင်သွင်းမှုသည် Responses API ကို ထောက်ပံ့ရမည်

### သင်ယူရာ လမ်းကြောင်း

သင်ခန်းစာများကို လိုက်လံ တိုးတက်ရန် အကြံပြုသည် -
1. **00-course-setup** - ပတ်ဝန်းကျင် ထားဆောက်ခြင်းကို ဒီနေရာမှ စတင်ပါ
2. **01-intro-to-ai-agents** - AI ကိုယ်စားလှယ် အခြေခံကို နားလည်ပါ
3. **02-explore-agentic-frameworks** - ဖရိမ်းဝတ် မျိုးစုံအကြောင်း ကိုယ်စားလှယ် ဖြည့်စွက်ပါ
4. **03-agentic-design-patterns** - အဓိက ဒီဇိုင်း ပုံစံများ
5. နံပါတ်လိုက် သင်ခန်းစာများ စဉ်ဆက်အသီးသီး အတွက် ဆက်လက်လုပ်ဆောင်ပါ

### ဖရိမ်းဝတ် ရွေးချယ်ခြင်း

မိမိရည်မှန်းချက်အရ ဖရိမ်းဝတ် ရွေးချယ်ပါ -
- **သင်ခန်းစာအားလုံး**: Microsoft Agent Framework (MAF) နှင့် `FoundryChatClient`
- **ကိုယ်စားလှယ်များ server-side တွင် Microsoft Foundry Agent Service V2 တွင် မှတ်ပုံတင်ပြီး Foundry portal တွင် မြင်နိုင်ပါသည်**

### ကူညီမှုရယူခြင်း

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) တွင် ပူးပေါင်းပါ
- သင်ခန်းစာ README ဖိုင်များမှ ထူးခြားသော လမ်းညွှန်ချက်များ ကြည့်ရှုပါ
- အဓိက [README.md](./README.md) မှ သင်တန်းအနှစ်ချုပ် ကြည့်ရှုပါ
- အသေးစိတ် ဆက်တင်များအတွက် [Course Setup](./00-course-setup/README.md) ကို တွေ့ပါ

### ကူညီပေးခြင်း

အားလုံးကို ဖွင့်လင်းလေ့လာရေး စီမံကိန်းသည်။ အကူအညီများ လက်ခံသည် -
- ကုဒ် ဥပမာများ တိုးတက်စေခြင်း
- အမှားသို့မဟုတ် တစ်ပုံတစ်ဖော် ဖြေရှင်းခြင်း
- ရှင်းလင်းသော မှတ်ချက်များ ထည့်သွင်းခြင်း
- သင်ခန်းစာခေါင်းစဉ်အသစ်များ ကမ်းလှမ်းခြင်း
- ဘာသာစကားများ အသစ်အတွက် ဘာသာပြန်ခြင်း

လက်ရှိ လိုအပ်ချက်များအတွက် [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) တွင် ကြည့်ရှုပါ။

## စီမံကိန်း အချက်အလက် အထူးအချက်အလက်များ

### မျိုးစုံ ဘာသာစကား ထောက်ပံ့မှု

ဤ မှတ်တမ်းတွဲသည် အလိုအလျောက် ဘာသာပြန် စနစ်ကို အသုံးပြုသည် -
- ၅၀ ခန့် ဘာသာစကားများ ထောက်ပံ့သည်
- `/translations/<lang-code>/` ဖိုဒါများတွင် ဘာသာပြန်ထားသည်
- GitHub Actions workflow က ဘာသာပြန် အပ်ဒိတ်မှုများ ကိုင်တွယ်သည်
- အင်္ဂလိပ်ဘာသာဖြင့် အမြစ်ဖိုင်များ ရှိသည်

### သင်ခန်းစာ ဖွဲ့စည်းပုံ

သင်ခန်းစာတိုင်းသည် တူညီသော စသည်သောပုံစံကို လိုက်နာသည် -
1. ဗီဒီယို သရုပ်ပြ အညွှန်း နှင့် အလင့်
2. ရေးသားထားသော သင်ခန်းစာ အကြောင်းအရာ (README.md)
3. ဖရိမ်းဝတ် များတွင် ကုဒ်နမူနာများ
4. သင်ယူရန် ရည်မှန်းချက်များ နှင့် ကြိုတင်လိုအပ်ချက်များ
5. ပိုမိုသိရှိရန် အရင်းအမြစ်များကို လင့်ခ်ထားသည်

### ကုဒ်နမူနာ ဖိုင်အမည်တွဲ။

ပုံစံ - `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - သင်ခန်းစာ 1၊ MAF Python
- `14-sequential.ipynb` - သင်ခန်းစာ 14, MAF အဆင့်မြင့် ဒီဇိုင်းပုံစံများ
- `16-python-agent-framework.ipynb` - သင်ခန်းစာ 16, ထုတ်လုပ်မှုဖောက်သည်-ထောက်ခံရေး ကိုယ်စားလှယ်
- `17-local-agent-foundry-local.ipynb` - သင်ခန်းစာ 17, ဒေသတွင်း ကိုယ်စားလှယ် Foundry Local + Qwen ဖြင့်

### အထူး ဖိုဒါများ

- `translated_images/` - ဘာသာပြန်ထားသော ဒဿနိကာရိုက်ပုံများ
- `images/` - အင်္ဂလိပ်စာအတန်းမူရင်း ဓာတ်ပုံများ
- `.devcontainer/` - VS Code ဖွံ့ဖြိုးရေး ကွန်တိန်းနာ ကွန်ဖစ်
- `.github/` - GitHub Actions workflow နှင့် မှန်ကန်ထားမှုများ

### လိုအပ်သော package များ

`requirements.txt` မှ အဓိက package များ -
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - ကိုယ်စားလှယ်မှ ကိုယ်စားလှယ် protocol ထောက်ပံ့မှု
- `azure-ai-inference`, `azure-ai-projects` - Azure AI ဝန်ဆောင်မှုများ
- `azure-identity` - Azure အတည်ပြုခြင်း (AzureCliCredential)
- `azure-search-documents` - Azure AI Search ပေါင်းစပ်မှု
- `mcp[cli]` - မော်ဒယ် ပတ်ဝန်းကျင် protocol ထောက်ပံ့မှု

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->