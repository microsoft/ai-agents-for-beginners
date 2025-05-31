# သင်ခန်းစာ ၁၁ - Model Context Protocol (MCP) ပေါင်းစပ်ခြင်း

## Model Context Protocol (MCP) မိတ်ဆက်

Model Context Protocol (MCP) သည် AI မော်ဒယ်များနှင့် client အပ္ပလီကေးရှင်းများကြား အပြန်အလှန်ဆက်သွယ်မှုကို စံချိန်စံညွှန်းပြုလုပ်ရန် ဒီဇိုင်းပြုလုပ်ထားသော ခေတ်မီ framework တစ်ခုဖြစ်သည်။ MCP သည် AI မော်ဒယ်များနှင့် ၎င်းတို့ကို အသုံးပြုသော အပ္ပလီကေးရှင်းများကြား တံတားအဖြစ် လုပ်ဆောင်ပြီး၊ အခြေခံ မော်ဒယ် implementation နည်းလမ်းများမခွဲခြားဘဲ တညီညာသော interface ကို ပံ့ပိုးပေးပါသည်။

### MCP ၏ အဓိက အရေးပါသော အချက်များ:

- **စံနှုန်းသတ်မှတ်ထားသော ဆက်သွယ်ရေး**: MCP သည် အပ္ပလီကေးရှင်းများ AI မော်ဒယ်များနှင့် ဆက်သွယ်ရန်အတွက် တူညီသော ဘာသာစကားကို တည်ထောင်ပေးသည်

- **ပိုမိုကောင်းမွန်သော Context စီမံခန့်ခွဲမှု**: AI မော်ဒယ်များသို့ contextual အချက်အလက်များကို ထိရောက်စွာ လွှဲပြောင်းပေးနိုင်သည်

- **Cross-platform လိုက်ဖက်မှု**: C#၊ Java၊ JavaScript၊ Python၊ နှင့် TypeScript အပါအဝင် programming language များတွင် အလုပ်လုပ်နိုင်သည်

- **ပြတ်သားသော ပေါင်းစပ်မှု**: developer များအား ၎င်းတို့၏အပ্ললิকেশনများတွင် မတူညီသော AI မော်ဒယ်များကို လွယ်ကူစွာ ပေါင်းစပ်နိုင်စေပါသည်

MCP သည် AI agent development တွင် အထူးတန်ဖိုးရှိပါသည်၊ အကြောင်းမှာ agent များသည် တူညီသော protocol တစ်ခုမှတစ်ဆင့် မတူညီသော စနစ်များနှင့် ဒေတာအရင်းအမြစ်များနှင့် အပြန်အလှန်ဆက်သွယ်နိုင်ပြီး၊ agent များကို ပိုမိုပြောင်းလွယ်ပြင်လွယ်နှင့် အစွမ်းထက-သော ဖြစ်စေပါသည်။

## သင်ယူမည့် ရည်မှန်းချက်များ

- MCP ဆိုသည်မှာ အဘယ်နည်းနှင့် AI agent development တွင် ၎င်း၏ အခန်းကဏ္ဍကို နားလည်ခြင်း
- GitHub ပေါင်းစပ်မှုအတွက် MCP server ကို တပ်ဆင်ပြီး configure လုပ်ခြင်း
- MCP tools များကို အသုံးပြု၍ multi-agent system တည်ဆောက်ခြင်း
- Azure Cognitive Search နှင့်အတူ RAG (Retrieval Augmented Generation) implement လုပ်ခြင်း

## လိုအပ်သော ကြိုတင်အသိများ

- Python 3.8+
- Node.js 14+
- Azure subscription
- GitHub account
- Semantic Kernel ၏ အခြေခံ နားလည်မှု

## တပ်ဆင်မှု လမ်းညွှန်များ

# ၁. **ပတ်ဝန်းကျင် တပ်ဆင်မှု**
 ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

# ၂. **Azure ဝန်ဆောင်မှုများ ပြင်ဆင်ခြင်း**
  - Azure Cognitive Search resource တည်ဆောက်ခြင်း
  - Azure OpenAI service တပ်ဆင်ခြင်း
  - `.env` ဖိုင်တွင် environment variables များ configure လုပ်ခြင်း

# ၃. **MCP Server တပ်ဆင်မှု**
 ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## ပရောဂျက် ဖွဲ့စည်းပုံ
```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## အဓိက အစိတ်အပိုင်းများ

### ၁. Multi-Agent စနစ်
- **GitHub Agent**: Repository များ ခွဲခြမ်းစိတ်ဖြာခြင်း
- **Hackathon Agent**: ပရောဂျက် အကြံပြုချက်များ
- **Events Agent**: နည်းပညာ ဖြစ်ရပ် အကြံပြုချက်များ

### ၂. Azure ပေါင်းစပ်မှု
- ဖြစ်ရပ်များ indexing အတွက် Cognitive Search
- Agent intelligence အတွက် Azure OpenAI
- RAG pattern implementation

### ၃. MCP ကိရိယာများ
- GitHub repository ခွဲခြမ်းစိတ်ဖြာမှု
- ကုဒ် စစ်ဆေးမှု
- Metadata ထုတ်နုတ်မှု

## ကုဒ် လမ်းလျှောက်မှု

နမူနာတွင် သရုပ်ပြထားသော အရာများ:
1. MCP server ပေါင်းစပ်မှု
2. Multi-agent စီစဉ်ခန့်ခွဲမှု
3. Azure Cognitive Search ပေါင်းစပ်မှု
4. RAG pattern အကောင်အထည်ဖော်မှု

### အဓိက လုပ်ဆောင်ချက်များ:
- Real-time GitHub repository ခွဲခြမ်းစိတ်ဖြာမှု
- ဉာဏ်ရှိသော ပရောဂျက် အကြံပြုချက်များ
- Azure Search အသုံးပြု၍ ဖြစ်ရပ် လိုက်ဖက်မှု
- Chainlit နှင့်အတူ Streaming responses

## နမူနာ လုပ်ဆောင်ခြင်း

အသေးစိတ် တပ်ဆင်မှု လမ်းညွှန်များနှင့် နောက်ထပ် အချက်အလက်များအတွက် [Github MCP Server Example README](./code_samples/github-mcp/README.md) ကို ကြည့်ရှုပါ။

### ၁. MCP server စတင်ခြင်း
   ```bash
   npx @modelcontextprotocol/server-github
   ```

### ၂. အပ္ပလီကေးရှင်း ဖွင့်လှစ်ခြင်း
```bash
   chainlit run app.py -w
   ```

### ၃. ပေါင်းစပ်မှု စမ်းသပ်ခြင်း
```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## ပြဿနာရှင်းဖွေမှု

အဖြစ်များသော ပြဿနာများနှင့် ဖြေရှင်းနည်းများ:

### ၁. MCP ချိတ်ဆက်မှု ပြဿနာများ
  - Server လုပ်ဆောင်နေသည်ကို စစ်ဆေးပါ
  - Port ရရှိနိုင်မှုကို စစ်ဆေးပါ
  - GitHub tokens များကို အတည်ပြုပါ

### ၂. Azure Search ပြဿနာများ
  - Connection strings များကို validate လုပ်ပါ
  - Index တည်ရှိမှုကို စစ်ဆေးပါ
  - Document upload ကို verify လုပ်ပါ

## နောက်ထပ် လုပ်ဆောင်ရမည့် အဆင့်များ

- နောက်ထပ် MCP tools များ လေ့လာခြင်း
- စိတ်ကြိုက် agents များ အကောင်အထည်ဖော်ခြင်း
- RAG စွမ်းရည်များ မြှင့်တင်ခြင်း
- ဖြစ်ရပ် အရင်းအမြစ်များ နောက်ထပ် ထည့်သွင်းခြင်း

## အရင်းအမြစ်များ

- [အစပြု MCP](https://aka.ms/mcp-for-beginners)  
- [MCP စွဲလမ်းများ](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search စွဲလမ်းများ](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel လမ်းညွှန်များ](https://learn.microsoft.com/semantic-kernel/)
