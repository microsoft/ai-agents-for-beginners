<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:19:31+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "my"
}
-->
# 🤝 အလုပ်အကိုင် Multi-Agent Workflow Systems (.NET)

## 📋 သင်ယူရန် ရည်ရွယ်ချက်များ

ဒီ notebook က Microsoft Agent Framework ကို .NET နဲ့ GitHub Models တွေကို အသုံးပြုပြီး အလုပ်အကိုင်အဆင့်မြင့် multi-agent systems တည်ဆောက်ပုံကို ပြသပေးမှာဖြစ်ပါတယ်။ .NET ရဲ့ အလုပ်အကိုင်အဆင့်မြင့် features တွေကို အသုံးပြုပြီး ထုတ်လုပ်မှုအဆင့်ရောက်တဲ့ ဖြေရှင်းချက်တွေကို ဖန်တီးဖို့အတွက် အထူး agent တွေ အတူတကွ လုပ်ဆောင်တဲ့ structured workflows တွေကို စီမံခန့်ခွဲပုံကို သင်ယူနိုင်ပါမယ်။

**သင်တည်ဆောက်မယ့် အလုပ်အကိုင် Multi-Agent အစွမ်းသတ္တိများ:**
- 👥 **Agent ပေါင်းစည်းမှု**: Type-safe agent တွေကို compile-time validation နဲ့ ပေါင်းစည်းခြင်း
- 🔄 **Workflow စီမံခန့်ခွဲမှု**: .NET ရဲ့ async patterns တွေကို အသုံးပြုပြီး declarative workflow ကို သတ်မှတ်ခြင်း
- 🎭 **အခန်းကဏ္ဍအထူးပြုမှု**: Strongly-typed agent ရဲ့ ပုဂ္ဂိုလ်ရေးနှင့် အထူးပြုမှုဧရိယာများ
- 🏢 **အလုပ်အကိုင် ပေါင်းစည်းမှု**: ထုတ်လုပ်မှုအဆင့်ရောက်တဲ့ patterns တွေကို monitoring နဲ့ error handling နဲ့အတူ ဖော်ပြခြင်း

## ⚙️ လိုအပ်ချက်များနှင့် Setup

**ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်:**
- .NET 9.0 SDK သို့မဟုတ် အထက်
- Visual Studio 2022 သို့မဟုတ် VS Code (C# extension ပါဝင်)
- Azure subscription (persistent agents အတွက်)

**လိုအပ်တဲ့ NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Code Sample

ဒီ သင်ခန်းစာအတွက် အပြည့်အစုံအလုပ်လုပ်တဲ့ code ကို အတူပါဝင်တဲ့ C# ဖိုင်မှာ ရနိုင်ပါတယ်: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

ဒီ sample ကို run ဖို့:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

သို့မဟုတ် .NET CLI ကို အသုံးပြုခြင်း:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## ဒီ Sample က ပြသတဲ့အရာများ

ဒီ multi-agent workflow system က hotel travel recommendation service တစ်ခုကို ဖန်တီးပေးပြီး အထူးပြု agent နှစ်ယောက်ပါဝင်ပါတယ်:

1. **FrontDesk Agent**: Activity နဲ့ location recommendation ပေးတဲ့ travel agent
2. **Concierge Agent**: Recommendation တွေကို authentic, non-touristy အတွေ့အကြုံတွေဖြစ်ဖို့ ပြန်လည်သုံးသပ်ပေးခြင်း

Agent တွေ workflow မှာ အတူတကွ လုပ်ဆောင်ပုံ:
- FrontDesk agent က travel request ကို စတင်လက်ခံခြင်း
- Concierge agent က recommendation ကို ပြန်လည်သုံးသပ်ပြီး အဆင့်မြှင့်တင်ပေးခြင်း
- Workflow က real-time response တွေကို stream လုပ်ပေးခြင်း

## အဓိက Concepts

### Agent ပေါင်းစည်းမှု
ဒီ sample က Microsoft Agent Framework ကို အသုံးပြုပြီး type-safe agent ပေါင်းစည်းမှုကို compile-time validation နဲ့ ပြသပေးပါတယ်။

### Workflow စီမံခန့်ခွဲမှု
.NET ရဲ့ async patterns တွေကို အသုံးပြုပြီး agent အများအပြားကို pipeline မှာ ချိတ်ဆက်တဲ့ declarative workflow ကို အသုံးပြုထားပါတယ်။

### Streaming Responses
Async enumerables နဲ့ event-driven architecture ကို အသုံးပြုပြီး agent response တွေကို real-time stream လုပ်ပုံကို ဖော်ပြထားပါတယ်။

### အလုပ်အကိုင် ပေါင်းစည်းမှု
ထုတ်လုပ်မှုအဆင့်ရောက်တဲ့ patterns တွေကို ဖော်ပြထားပြီး:
- Environment variable configuration
- Secure credential management
- Error handling
- Asynchronous event processing

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။