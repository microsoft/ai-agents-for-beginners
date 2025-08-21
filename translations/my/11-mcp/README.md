<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:48:58+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "my"
}
-->
# အခန်း ၁၁: Model Context Protocol (MCP) ပေါင်းစည်းမှု

## Model Context Protocol (MCP) ကိုမိတ်ဆက်ခြင်း

Model Context Protocol (MCP) သည် AI မော်ဒယ်များနှင့် client အက်ပ်လီကေးရှင်းများအကြား အပြန်အလှန်ဆက်သွယ်မှုများကို စံပြုလုပ်ရန် ရည်ရွယ်ထားသော နောက်ဆုံးပေါ်ဖရိမ်းဝေါ့ဖြစ်သည်။ MCP သည် AI မော်ဒယ်များနှင့် အက်ပ်လီကေးရှင်းများအကြား တစ်ခုတည်းသော အင်တာဖေ့စ်ကို ပံ့ပိုးပေးပြီး မော်ဒယ်အကောင်အထည်ဖော်မှု မည်သည့်ပုံစံဖြစ်စေ တူညီစွာ ဆက်သွယ်နိုင်စေသည်။

MCP ၏ အဓိကအချက်များ:

- **စံပြဆက်သွယ်မှု**: MCP သည် AI မော်ဒယ်များနှင့် အက်ပ်လီကေးရှင်းများအကြား ဆက်သွယ်ရန် တူညီသော ဘာသာစကားတစ်ခုကို ဖန်တီးပေးသည်  
- **အကြောင်းအရာစီမံခန့်ခွဲမှုတိုးတက်မှု**: AI မော်ဒယ်များသို့ အကြောင်းအရာဆိုင်ရာ အချက်အလက်များကို ထိရောက်စွာ ပေးပို့နိုင်စေသည်  
- **ပလက်ဖောင်းများအကြားသင့်လျော်မှု**: C#, Java, JavaScript, Python, TypeScript အပါအဝင် အမျိုးမျိုးသော programming language များတွင် အသုံးပြုနိုင်သည်  
- **လွယ်ကူသောပေါင်းစည်းမှု**: အက်ပ်လီကေးရှင်းများတွင် မတူညီသော AI မော်ဒယ်များကို လွယ်ကူစွာ ပေါင်းစည်းနိုင်စေသည်  

MCP သည် AI အေးဂျင့်များ ဖွံ့ဖြိုးတိုးတက်မှုတွင် အထူးတန်ဖိုးရှိပြီး အေးဂျင့်များကို တစ်ခုတည်းသော ပရိုတိုကောမှတစ်ဆင့် မတူညီသော စနစ်များနှင့် ဒေတာရင်းမြစ်များနှင့် ဆက်သွယ်နိုင်စေသည်။ ဒါကြောင့် အေးဂျင့်များ ပိုမိုတင်းကျပ်ပြီး အင်အားကြီးလာစေသည်။

## သင်ခန်းစာရည်မှန်းချက်များ
- MCP သည် အဘယ်နည်း၊ AI အေးဂျင့် ဖွံ့ဖြိုးတိုးတက်မှုတွင် ၎င်း၏ အခန်းကဏ္ဍကို နားလည်ရန်  
- GitHub ပေါင်းစည်းမှုအတွက် MCP server ကို စတင်ပြီး ဖွဲ့စည်းရန်  
- MCP tools အသုံးပြု၍ multi-agent system တစ်ခု တည်ဆောက်ရန်  
- Azure Cognitive Search ဖြင့် RAG (Retrieval Augmented Generation) ကို အကောင်အထည်ဖော်ရန်  

## လိုအပ်ချက်များ
- Python 3.8+  
- Node.js 14+  
- Azure subscription  
- GitHub account  
- Semantic Kernel အခြေခံအကြောင်းအရာကို နားလည်မှု  

## Setup လုပ်ဆောင်ရန်အညွှန်း

1. **ပတ်ဝန်းကျင်ကို ပြင်ဆင်ရန်**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure ဝန်ဆောင်မှုများကို ဖွဲ့စည်းရန်**  
   - Azure Cognitive Search resource တစ်ခု ဖန်တီးပါ  
   - Azure OpenAI service ကို စတင်ပါ  
   - `.env` တွင် environment variables များကို ဖွဲ့စည်းပါ  

3. **MCP Server ကို ဖွဲ့စည်းရန်**  
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
- GitHub Agent: Repository ကို ခွဲခြမ်းစိတ်ဖြာမှု  
- Hackathon Agent: Project အကြံပြုချက်များ  
- Events Agent: နည်းပညာပွဲများအကြံပြုချက်  

### ၂. Azure ပေါင်းစည်းမှု
- Cognitive Search ကို event indexing အတွက် အသုံးပြုခြင်း  
- Azure OpenAI ကို အေးဂျင့်၏ ထောက်ခံမှုအတွက် အသုံးပြုခြင်း  
- RAG ပုံစံကို အကောင်အထည်ဖော်ခြင်း  

### ၃. MCP Tools
- GitHub repository ခွဲခြမ်းစိတ်ဖြာမှု  
- Code စစ်ဆေးမှု  
- Metadata ထုတ်ယူမှု  

## Code Walkthrough

ဤနမူနာတွင် ဖော်ပြထားသည်မှာ:
1. MCP server ပေါင်းစည်းမှု  
2. Multi-agent စီမံခန့်ခွဲမှု  
3. Azure Cognitive Search ပေါင်းစည်းမှု  
4. RAG ပုံစံ အကောင်အထည်ဖော်မှု  

အဓိကအင်္ဂါရပ်များ:
- GitHub repository ကို အချိန်နှင့်တပြေးညီ ခွဲခြမ်းစိတ်ဖြာမှု  
- Intelligent project အကြံပြုချက်များ  
- Azure Search ကို အသုံးပြု၍ event ကို ကိုက်ညီမှု  
- Chainlit ဖြင့် Streaming response များ  

## နမူနာကို အလုပ်လုပ်စေခြင်း

အသေးစိတ် setup အညွှန်းများနှင့် အခြားအချက်အလက်များအတွက် [Github MCP Server Example README](./code_samples/github-mcp/README.md) ကို ကြည့်ပါ။

1. MCP server ကို စတင်ပါ:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. အက်ပ်လီကေးရှင်းကို စတင်ပါ:  
   ```bash
   chainlit run app.py -w
   ```

3. ပေါင်းစည်းမှုကို စမ်းသပ်ပါ:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## ပြဿနာဖြေရှင်းခြင်း

အထွေထွေပြဿနာများနှင့် ဖြေရှင်းနည်းများ:
1. MCP ဆက်သွယ်မှုပြဿနာများ  
   - Server အလုပ်လုပ်နေမှုကို စစ်ဆေးပါ  
   - Port ရရှိနိုင်မှုကို စစ်ဆေးပါ  
   - GitHub tokens ကို အတည်ပြုပါ  

2. Azure Search ပြဿနာများ  
   - Connection strings ကို စစ်ဆေးပါ  
   - Index ရှိမှုကို အတည်ပြုပါ  
   - Document upload ကို စစ်ဆေးပါ  

## နောက်တစ်ဆင့်
- အခြား MCP tools များကို စူးစမ်းပါ  
- အေးဂျင့်များကို ကိုယ်ပိုင်ဖန်တီးပါ  
- RAG စွမ်းရည်များကို တိုးမြှင့်ပါ  
- Event ရင်းမြစ်များကို ပိုမိုထည့်သွင်းပါ  
- **အဆင့်မြင့်**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) တွင် အေးဂျင့်-အေးဂျင့် ဆက်သွယ်မှု နမူနာများကို ကြည့်ပါ  

## ရင်းမြစ်များ
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)  

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်ပါသည်။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူပညာရှင်များမှ ဘာသာပြန်ဆိုမှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ဆိုမှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပာယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။