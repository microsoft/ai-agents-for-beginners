<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-30T00:24:55+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "my"
}
-->
# MCP Server Integration Guide

## ကြိုတင်လိုအပ်ချက်များ
- Node.js (version 14 သို့မဟုတ် အထက်) တင်ထားပြီးဖြစ်ရမည်  
- npm package manager  
- လိုအပ်သော dependencies များပါဝင်သော Python environment  

## Setup လုပ်ဆောင်ရန်အဆင့်များ

1. **MCP Server Package ကို Install လုပ်ပါ**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```  

2. **MCP Server ကို Start လုပ်ပါ**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Server သည် စတင်ပြီး connection URL ကို ပြသသင့်သည်။  

3. **Connection ကို Verify လုပ်ပါ**  
   - Chainlit interface တွင် plug အိုင်ကွန် (🔌) ကို ရှာပါ  
   - Plug အိုင်ကွန်အနားတွင် (1) ဆိုသော နံပါတ်တစ်လုံး ပေါ်လာသင့်သည်၊ ဒါက connection အောင်မြင်ကြောင်း ပြသသည်  
   - Console တွင် "GitHub plugin setup completed successfully" ဟု ပြသသင့်ပြီး အခြား status လိုင်းများနှင့်အတူပါဝင်သည်  

## ပြဿနာရှင်းရန်

### ရှိနေတတ်သော ပြဿနာများ

1. **Port Conflict**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   ဖြေရှင်းနည်း: Port ကို အောက်ပါအတိုင်း ပြောင်းပါ-  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```  

2. **Authentication ပြဿနာများ**  
   - GitHub credentials များကို မှန်ကန်စွာ configure လုပ်ထားကြောင်း သေချာပါ  
   - .env ဖိုင်တွင် လိုအပ်သော tokens များပါဝင်ကြောင်း စစ်ဆေးပါ  
   - GitHub API access ကို Verify လုပ်ပါ  

3. **Connection မအောင်မြင်ခြင်း**  
   - Server သည် မျှော်မှန်းထားသော port တွင် run လုပ်နေကြောင်း အတည်ပြုပါ  
   - Firewall settings များကို စစ်ဆေးပါ  
   - Python environment တွင် လိုအပ်သော packages များပါဝင်ကြောင်း Verify လုပ်ပါ  

## Connection ကို Verify လုပ်ခြင်း

MCP server သည် အောင်မြင်စွာ ချိတ်ဆက်ထားကြောင်း သေချာရန်-  
1. Console တွင် "GitHub plugin setup completed successfully" ဟု ပြသရမည်  
2. Connection logs တွင် "✓ MCP Connection Status: Active" ဟု ပြသရမည်  
3. GitHub commands များကို chat interface တွင် အသုံးပြုနိုင်ရမည်  

## Environment Variables

သင့် .env ဖိုင်တွင် လိုအပ်သောအချက်များ-  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```  

## Connection ကို စမ်းသပ်ခြင်း

Chat တွင် အောက်ပါ စမ်းသပ်စာကို ပို့ပါ-  
```
Show me the repositories for username: [GitHub Username]
```  
အောင်မြင်သော ပြန်ကြားချက်တွင် repository အချက်အလက်များ ပြသမည်။  

---

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို ကျေးဇူးပြု၍ သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်ရန် လိုအပ်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ အတည်ပြုထားသော ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားမှုများ သို့မဟုတ် အဓိပ္ပာယ်မှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။