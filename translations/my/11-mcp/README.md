<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T07:45:54+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "my"
}
-->
# အခန်း ၁၁: Model Context Protocol (MCP) ပေါင်းစည်းမှု

## Model Context Protocol (MCP) ကိုမိတ်ဆက်ခြင်း

Model Context Protocol (MCP) သည် AI မော်ဒယ်များနှင့် client အပလီကေးရှင်းများအကြား အပြန်အလှန်ဆက်သွယ်မှုများကို စံပြုလုပ်ရန် ရည်ရွယ်ထားသော နောက်ဆုံးပေါ်ဖရိမ်းဝေါ့ဖြစ်သည်။ MCP သည် AI မော်ဒယ်များနှင့် အပလီကေးရှင်းများအကြား တစ်ခုတည်းသော အင်တာဖေ့စ်ကို ပံ့ပိုးပေးပြီး မော်ဒယ်အကောင်အထည်ဖော်မှုမည်သည့်ပုံစံဖြစ်စေ တူညီစွာ ဆက်သွယ်နိုင်စေသည်။

MCP ၏ အဓိကအချက်များမှာ -

- **စံပြဆက်သွယ်မှု**: MCP သည် AI မော်ဒယ်များနှင့် အပလီကေးရှင်းများအကြား ဆက်သွယ်ရန် တူညီသော ဘာသာစကားတစ်ခုကို ဖန်တီးပေးသည်။
- **အကြောင်းအရာစီမံခန့်ခွဲမှုတိုးတက်မှု**: AI မော်ဒယ်များသို့ အကြောင်းအရာဆိုင်ရာ အချက်အလက်များကို ထိရောက်စွာ ပေးပို့နိုင်စေသည်။
- **ပလက်ဖောင်းများအကြားသင့်လျော်မှု**: C#, Java, JavaScript, Python, TypeScript အပါအဝင် အမျိုးမျိုးသော programming language များတွင် အသုံးပြုနိုင်သည်။
- **ပေါင်းစည်းမှုလွယ်ကူမှု**: အမျိုးမျိုးသော AI မော်ဒယ်များကို အပလီကေးရှင်းများတွင် လွယ်ကူစွာ ပေါင်းစည်းနိုင်စေသည်။

MCP သည် AI အေးဂျင့် ဖွံ့ဖြိုးတိုးတက်မှုတွင် အထူးတန်ဖိုးရှိပြီး အေးဂျင့်များကို စနစ်များနှင့် ဒေတာရင်းမြစ်များအမျိုးမျိုးနှင့် တစ်ခုတည်းသော ပရိုတိုကောမှတစ်ဆင့် ဆက်သွယ်နိုင်စေသည်။ ဒါကြောင့် အေးဂျင့်များ ပိုမိုတက်ကြွပြီး အားကောင်းလာစေသည်။

## သင်ခန်းစာရည်မှန်းချက်များ
- MCP သည်အဘယ်နည်း၊ AI အေးဂျင့် ဖွံ့ဖြိုးတိုးတက်မှုတွင် ၎င်း၏ အခန်းကဏ္ဍကို နားလည်ခြင်း
- GitHub ပေါင်းစည်းမှုအတွက် MCP server တစ်ခုကို တပ်ဆင်ခြင်းနှင့် ဖွဲ့စည်းခြင်း
- MCP tools များကို အသုံးပြု၍ multi-agent system တစ်ခု တည်ဆောက်ခြင်း
- Azure Cognitive Search ဖြင့် RAG (Retrieval Augmented Generation) ကို အကောင်အထည်ဖော်ခြင်း

## လိုအပ်ချက်များ
- Python 3.8+
- Node.js 14+
- Azure subscription
- GitHub account
- Semantic Kernel အခြေခံနားလည်မှု

## Setup လုပ်ဆောင်ရန်ညွှန်ကြားချက်များ

1. **ပတ်ဝန်းကျင် Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure ဝန်ဆောင်မှုများကို ဖွဲ့စည်းခြင်း**
   - Azure Cognitive Search resource တစ်ခု ဖန်တီးပါ
   - Azure OpenAI service ကို တပ်ဆင်ပါ
   - `.env` တွင် environment variables များကို ဖွဲ့စည်းပါ

3. **MCP Server Setup**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Project ဖွဲ့စည်းမှု

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## အဓိကအစိတ်အပိုင်းများ

### ၁. Multi-Agent System
- GitHub Agent: Repository ကို ခွဲခြမ်းစိတ်ဖြာခြင်း
- Hackathon Agent: Project အကြံပြုချက်များ
- Events Agent: နည်းပညာပွဲများအကြံပြုချက်

### ၂. Azure ပေါင်းစည်းမှု
- Cognitive Search ကို event indexing အတွက် အသုံးပြုခြင်း
- Azure OpenAI ကို အေးဂျင့်၏ ဉာဏ်ရည်အတွက် အသုံးပြုခြင်း
- RAG pattern ကို အကောင်အထည်ဖော်ခြင်း

### ၃. MCP Tools
- GitHub repository ခွဲခြမ်းစိတ်ဖြာခြင်း
- Code စစ်ဆေးခြင်း
- Metadata ထုတ်ယူခြင်း

## Code Walkthrough

ဤနမူနာတွင် ဖော်ပြထားသည်မှာ -
1. MCP server ပေါင်းစည်းမှု
2. Multi-agent orchestration
3. Azure Cognitive Search ပေါင်းစည်းမှု
4. RAG pattern အကောင်အထည်ဖော်မှု

အဓိကအင်္ဂါရပ်များ:
- GitHub repository ကို အချိန်နှင့်တပြေးညီ ခွဲခြမ်းစိတ်ဖြာခြင်း
- Project အကြံပြုချက်များကို ဉာဏ်ရည်ဖြင့် ပေးခြင်း
- Azure Search ကို အသုံးပြု၍ event များကို ကိုက်ညီစေခြင်း
- Chainlit ဖြင့် Streaming responses

## နမူနာကို အလုပ်လုပ်စေခြင်း

အသေးစိတ် setup ညွှန်ကြားချက်များနှင့် အခြားအချက်အလက်များအတွက် [Github MCP Server Example README](./code_samples/github-mcp/README.md) ကို ကြည့်ပါ။

1. MCP server ကို စတင်ပါ:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. အပလီကေးရှင်းကို စတင်ပါ:
   ```bash
   chainlit run app.py -w
   ```

3. ပေါင်းစည်းမှုကို စမ်းသပ်ပါ:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## ပြဿနာဖြေရှင်းခြင်း

အများဆုံးတွေ့ရသော ပြဿနာများနှင့် ဖြေရှင်းနည်းများ:
1. MCP ဆက်သွယ်မှုပြဿနာများ
   - Server အလုပ်လုပ်နေမလုပ်နေ စစ်ဆေးပါ
   - Port ရရှိနိုင်မှု စစ်ဆေးပါ
   - GitHub tokens ကို အတည်ပြုပါ

2. Azure Search ပြဿနာများ
   - Connection strings ကို အတည်ပြုပါ
   - Index ရှိမရှိ စစ်ဆေးပါ
   - Document upload ကို အတည်ပြုပါ

## နောက်တစ်ဆင့်
- MCP tools များကို ထပ်မံလေ့လာပါ
- Custom agents များကို အကောင်အထည်ဖော်ပါ
- RAG စွမ်းဆောင်ရည်များကို တိုးတက်စေပါ
- Event ရင်းမြစ်များကို ပိုမိုထည့်သွင်းပါ
- **အဆင့်မြင့်**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) တွင် agent-to-agent ဆက်သွယ်မှု နမူနာများကို ကြည့်ပါ

## ရင်းမြစ်များ
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။