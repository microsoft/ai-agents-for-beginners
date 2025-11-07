<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:29:10+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "my"
}
-->
# 🛠️ GitHub Models (.NET) ကို အသုံးပြု၍ အဆင့်မြင့် Tool အသုံးပြုခြင်း

## 📋 သင်ယူရမည့် အချက်များ

ဒီ notebook က Microsoft Agent Framework ကို .NET နဲ့ GitHub Models တွေကို အသုံးပြုပြီး အဆင့်မြင့် tool တွေကို ပေါင်းစပ်အသုံးပြုနိုင်တဲ့ enterprise-grade pattern တွေကို ပြသထားပါတယ်။ C# ရဲ့ strong typing နဲ့ .NET ရဲ့ enterprise features တွေကို အသုံးပြုပြီး အထူးပြု tool တွေစွမ်းဆောင်နိုင်တဲ့ agent တွေကို တည်ဆောက်ပုံကို သင်ယူနိုင်ပါမယ်။

**သင်ကျွမ်းကျင်ရမည့် အဆင့်မြင့် Tool စွမ်းဆောင်ရည်များ:**
- 🔧 **Multi-Tool Architecture**: အထူးပြုစွမ်းဆောင်ရည်များစွာပါဝင်တဲ့ agent တွေတည်ဆောက်ခြင်း
- 🎯 **Type-Safe Tool Execution**: C# ရဲ့ compile-time validation ကို အသုံးပြုခြင်း
- 📊 **Enterprise Tool Patterns**: ထုတ်လုပ်မှုအဆင့် tool ဒီဇိုင်းနဲ့ error ကို ကိုင်တွယ်ခြင်း
- 🔗 **Tool Composition**: အဆင့်မြင့်လုပ်ငန်းစဉ်များအတွက် tool တွေကို ပေါင်းစပ်အသုံးပြုခြင်း

## 🎯 .NET Tool Architecture ရဲ့ အကျိုးကျေးဇူးများ

### Enterprise Tool Features
- **Compile-Time Validation**: Strong typing က tool parameter တွေကို မှန်ကန်စေခြင်း
- **Dependency Injection**: IoC container ကို tool management အတွက် ပေါင်းစပ်အသုံးပြုခြင်း
- **Async/Await Patterns**: Non-blocking tool execution နဲ့ resource ကို မှန်ကန်စွာ စီမံခြင်း
- **Structured Logging**: Tool execution ကို စောင့်ကြည့်နိုင်တဲ့ logging integration

### Production-Ready Patterns
- **Exception Handling**: Typed exceptions နဲ့ error ကို စုံလင်စွာ ကိုင်တွယ်ခြင်း
- **Resource Management**: Disposal pattern တွေကို မှန်ကန်စွာ အသုံးပြုခြင်း
- **Performance Monitoring**: Built-in metrics နဲ့ performance counters
- **Configuration Management**: Validation ပါဝင်တဲ့ type-safe configuration

## 🔧 Technical Architecture

### Core .NET Tool Components
- **Microsoft.Extensions.AI**: Tool abstraction layer တစ်ခု
- **Microsoft.Agents.AI**: Enterprise-grade tool orchestration
- **GitHub Models Integration**: Connection pooling ပါဝင်တဲ့ အမြန်ဆုံး API client

### Tool Execution Pipeline
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Tool Categories & Patterns

### 1. **Data Processing Tools**
- **Input Validation**: Data annotations နဲ့ strong typing
- **Transform Operations**: Type-safe data conversion နဲ့ formatting
- **Business Logic**: Domain-specific အတွက် calculation နဲ့ analysis tools
- **Output Formatting**: Structured response generation

### 2. **Integration Tools** 
- **API Connectors**: RESTful service integration ကို HttpClient နဲ့
- **Database Tools**: Entity Framework integration ကို data access အတွက်
- **File Operations**: Validation ပါဝင်တဲ့ secure file system operations
- **External Services**: Third-party service integration patterns

### 3. **Utility Tools**
- **Text Processing**: String manipulation နဲ့ formatting utilities
- **Date/Time Operations**: Culture-aware date/time calculations
- **Mathematical Tools**: Precision calculations နဲ့ statistical operations
- **Validation Tools**: Business rule validation နဲ့ data verification

## ⚙️ Prerequisites & Setup

**Development Environment:**
- .NET 9.0 SDK သို့မဟုတ် အထက်
- Visual Studio 2022 သို့မဟုတ် VS Code (C# extension ပါဝင်)
- GitHub Models API access

**Required NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Environment Configuration (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Enterprise-grade agent တွေကို .NET နဲ့ type-safe tool စွမ်းဆောင်ရည်များနဲ့ တည်ဆောက်ဖို့ အဆင်သင့်ဖြစ်ပါပြီ။ 🏢⚡

## 💻 Code Implementation

C# implementation အပြည့်အစုံကို `04-dotnet-agent-framework.cs` ဖိုင်မှာ တွေ့နိုင်ပါတယ်။ ဒီ .NET Single File App က အောက်ပါအချက်များကို ပြသထားပါတယ်-

- GitHub Models configuration အတွက် environment variables တွေ load လုပ်ခြင်း
- C# methods နဲ့ attributes အသုံးပြုပြီး custom tools တွေကို သတ်မှတ်ခြင်း
- Tool integration ပါဝင်တဲ့ AI agent တစ်ခုကို ဖန်တီးခြင်း
- Conversation threads ကို စီမံခြင်း
- Tool invocation နဲ့ agent requests တွေကို အကောင်အထည်ဖော်ခြင်း

ဥပမာကို run လုပ်ရန်:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

သို့မဟုတ် .NET CLI ကို အသုံးပြု၍:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသောအရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။