<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T09:17:15+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "my"
}
-->
# အခန်း ၁၁: Model Context Protocol (MCP) ပေါင်းစည်းမှု

## Model Context Protocol (MCP) အကြောင်းမိတ်ဆက်

Model Context Protocol (MCP) သည် AI မော်ဒယ်များနှင့် client အက်ပ်လီကေးရှင်းများအကြား အပြန်အလှန်ဆက်သွယ်မှုများကို စံပြုလုပ်ရန် ရည်ရွယ်ထားသော နောက်ဆုံးပေါ်ဖရိမ်းဝက်ဖြစ်သည်။ MCP သည် AI မော်ဒယ်များနှင့် အက်ပ်လီကေးရှင်းများအကြား တစ်ဆက်တည်းတံတားအဖြစ် လုပ်ဆောင်ပေးပြီး မော်ဒယ်အခြေခံအကောင်အထည်မည်သည့်အမျိုးအစားမဆို တူညီသောအင်တာဖေ့စ်ကို ပေးစွမ်းနိုင်သည်။

MCP ၏ အဓိကအချက်များမှာ -

- **စံပြဆက်သွယ်မှု**: MCP သည် AI မော်ဒယ်များနှင့် အက်ပ်လီကေးရှင်းများအကြား ဆက်သွယ်ရန် တူညီသောဘာသာစကားကို ဖန်တီးပေးသည်  
- **အကြောင်းအရာစီမံခန့်ခွဲမှုတိုးတက်မှု**: AI မော်ဒယ်များသို့ အကြောင်းအရာဆိုင်ရာအချက်အလက်များကို ထိရောက်စွာ ပေးပို့နိုင်သည်  
- **ပလက်ဖောင်းအကြားလိုက်လျောညီထွေမှု**: C#, Java, JavaScript, Python, TypeScript အပါအဝင် အမျိုးမျိုးသောပရိုဂရမ်မင်းဘာသာစကားများတွင် အလုပ်လုပ်နိုင်သည်  
- **ရိုးရှင်းသောပေါင်းစည်းမှု**: အမျိုးမျိုးသော AI မော်ဒယ်များကို အက်ပ်လီကေးရှင်းများတွင် လွယ်ကူစွာ ပေါင်းစည်းနိုင်သည်  

MCP သည် AI အေးဂျင့်ဖွံ့ဖြိုးတိုးတက်မှုတွင် အထူးတန်ဖိုးရှိပြီး အေးဂျင့်များကို စနစ်အမျိုးမျိုးနှင့် ဒေတာရင်းမြစ်များနှင့် တစ်ဆက်တည်းဆက်သွယ်နိုင်စေသော စံပြပရိုတိုကောအဖြစ် လုပ်ဆောင်ပေးသည်။ ၎င်းက အေးဂျင့်များကို ပိုမိုလွယ်ကူပြီး အားကောင်းစေသည်။

## သင်ခန်းစာရည်မှန်းချက်များ
- MCP ဆိုတာဘာလဲ၊ AI အေးဂျင့်ဖွံ့ဖြိုးတိုးတက်မှုတွင် ၎င်း၏အခန်းကဏ္ဍကို နားလည်ရန်  
- GitHub ပေါင်းစည်းမှုအတွက် MCP server ကို စတင်တပ်ဆင်ပြီး ပြင်ဆင်ရန်  
- MCP tools အသုံးပြု၍ မျိုးစုံအေးဂျင့်စနစ်တစ်ခု တည်ဆောက်ရန်  
- Azure Cognitive Search ဖြင့် RAG (Retrieval Augmented Generation) ကို အကောင်အထည်ဖော်ရန်  

## လိုအပ်ချက်များ
- Python 3.8+  
- Node.js 14+  
- Azure subscription  
- GitHub အကောင့်  
- Semantic Kernel အခြေခံအကြောင်းအရာကို နားလည်မှု  

## Setup လုပ်ဆောင်ရန်ညွှန်ကြားချက်များ

1. **ပတ်ဝန်းကျင်ပြင်ဆင်မှု**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure ဝန်ဆောင်မှုများကို ပြင်ဆင်ရန်**
   - Azure Cognitive Search resource တစ်ခု ဖန်တီးပါ  
   - Azure OpenAI ဝန်ဆောင်မှုကို ပြင်ဆင်ပါ  
   - `.env` ဖိုင်တွင် ပတ်ဝန်းကျင်အပြောင်းအလဲများကို သတ်မှတ်ပါ  

3. **MCP Server ပြင်ဆင်မှု**
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

### ၁. မျိုးစုံအေးဂျင့်စနစ်
- GitHub အေးဂျင့်: Repository ခွဲခြမ်းစိတ်ဖြာမှု  
- Hackathon အေးဂျင့်: Project အကြံပြုချက်များ  
- Events အေးဂျင့်: နည်းပညာပွဲအစီအစဉ်အကြံပြုချက်များ  

### ၂. Azure ပေါင်းစည်းမှု
- အဖြစ်အပျက်များကို index လုပ်ရန် Cognitive Search  
- အေးဂျင့်အတတ်ပညာအတွက် Azure OpenAI  
- RAG ပုံစံအကောင်အထည်ဖော်မှု  

### ၃. MCP Tools
- GitHub repository ခွဲခြမ်းစိတ်ဖြာမှု  
- ကုဒ်စစ်ဆေးမှု  
- Metadata ထုတ်ယူမှု  

## Code Walkthrough

ဤနမူနာတွင် ပြသထားသည်မှာ -  
1. MCP server ပေါင်းစည်းမှု  
2. မျိုးစုံအေးဂျင့်စနစ် စီမံခန့်ခွဲမှု  
3. Azure Cognitive Search ပေါင်းစည်းမှု  
4. RAG ပုံစံအကောင်အထည်ဖော်မှု  

အဓိကအင်္ဂါရပ်များ -  
- GitHub repository ကို အချိန်နှင့်တပြေးညီ ခွဲခြမ်းစိတ်ဖြာမှု  
- Intelligent project အကြံပြုချက်များ  
- Azure Search အသုံးပြု၍ အဖြစ်အပျက်ကို ကိုက်ညီမှုရှာဖွေမှု  
- Chainlit ဖြင့် စီးဆင်းမှုတုံ့ပြန်မှုများ  

## နမူနာကို အလုပ်လုပ်ရန်

အသေးစိတ် setup ညွှန်ကြားချက်များနှင့် အခြားအချက်အလက်များအတွက် [Github MCP Server Example README](./code_samples/github-mcp/README.md) ကို ကြည့်ပါ။

1. MCP server ကို စတင်ပါ -  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. အက်ပ်လီကေးရှင်းကို ဖွင့်ပါ -  
   ```bash
   chainlit run app.py -w
   ```

3. ပေါင်းစည်းမှုကို စမ်းသပ်ပါ -  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## ပြဿနာဖြေရှင်းမှု

အထွေထွေပြဿနာများနှင့် ဖြေရှင်းနည်းများ -  
1. MCP ဆက်သွယ်မှုပြဿနာများ  
   - Server အလုပ်လုပ်နေမနေ စစ်ဆေးပါ  
   - Port ရရှိနိုင်မှု စစ်ဆေးပါ  
   - GitHub tokens အတည်ပြုပါ  

2. Azure Search ပြဿနာများ  
   - Connection strings အတည်ပြုပါ  
   - Index ရှိမရှိ စစ်ဆေးပါ  
   - Document upload အတည်ပြုပါ  

## နောက်တစ်ဆင့်
- MCP tools အပိုများကို စူးစမ်းပါ  
- အေးဂျင့်စိတ်ကြိုက်ဖန်တီးပါ  
- RAG စွမ်းဆောင်ရည်တိုးတက်စေပါ  
- အဖြစ်အပျက်ရင်းမြစ်များ ပိုမိုထည့်သွင်းပါ  
- **အဆင့်မြင့်**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) တွင် အေးဂျင့်-အေးဂျင့် ဆက်သွယ်မှုနမူနာများကို ကြည့်ပါ  

## ရင်းမြစ်များ
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)  

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူပညာရှင်များမှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပါယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။