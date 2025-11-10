<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:52:42+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "my"
}
-->
# 🎨 GitHub Models (.NET) နှင့်အတူ Agentic Design Patterns

## 📋 သင်ယူရန်ရည်ရွယ်ချက်များ

ဒီ notebook က Microsoft Agent Framework ကို .NET နဲ့ GitHub Models တွေကို ပေါင်းစပ်ပြီး အဆင့်မြင့် design patterns တွေကို အသုံးပြုကာ အတတ်သက်သက်ရှိတဲ့ agent တွေကို တည်ဆောက်ပုံကို ပြသထားပါတယ်။ သင်သည် agent တွေကို ထုတ်လုပ်နိုင်စေဖို့၊ ထိန်းသိမ်းနိုင်စေဖို့၊ နှင့် အရွယ်အစားကြီးမားစွာ တိုးချဲ့နိုင်စေဖို့ professional patterns နှင့် architectural approaches တွေကို သင်ယူနိုင်ပါမည်။

**Enterprise Design Patterns:**
- 🏭 **Factory Pattern**: Dependency injection ဖြင့် agent တစ်ခုကို စနစ်တကျဖန်တီးခြင်း
- 🔧 **Builder Pattern**: Fluent agent configuration နှင့် setup
- 🧵 **Thread-Safe Patterns**: Concurrent conversation ကို စနစ်တကျ စီမံခန့်ခွဲခြင်း
- 📋 **Repository Pattern**: Tool နှင့် capability များကို စနစ်တကျ စီမံခန့်ခွဲခြင်း

## 🎯 .NET-Specific Architectural Benefits

### Enterprise Features
- **Strong Typing**: Compile-time validation နှင့် IntelliSense အထောက်အကူ
- **Dependency Injection**: Built-in DI container integration
- **Configuration Management**: IConfiguration နှင့် Options patterns
- **Async/Await**: Asynchronous programming ကို အထူးထောက်ပံ့မှု

### Production-Ready Patterns
- **Logging Integration**: ILogger နှင့် structured logging အထောက်အကူ
- **Health Checks**: Built-in monitoring နှင့် diagnostics
- **Configuration Validation**: Data annotations ဖြင့် strong typing
- **Error Handling**: Structured exception management

## 🔧 Technical Architecture

### Core .NET Components
- **Microsoft.Extensions.AI**: AI service abstractions ကို တစ်ခုတည်းအဖြစ် ပေါင်းစည်းထားခြင်း
- **Microsoft.Agents.AI**: Enterprise agent orchestration framework
- **GitHub Models Integration**: High-performance API client patterns
- **Configuration System**: appsettings.json နှင့် environment integration

### Design Pattern Implementation
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Enterprise Patterns Demonstrated

### 1. **Creational Patterns**
- **Agent Factory**: Configuration တစ်ခုတည်းဖြင့် agent ကို စနစ်တကျ ဖန်တီးခြင်း
- **Builder Pattern**: Complex agent configuration အတွက် Fluent API
- **Singleton Pattern**: Shared resources နှင့် configuration management
- **Dependency Injection**: Loose coupling နှင့် testability

### 2. **Behavioral Patterns**
- **Strategy Pattern**: Tool execution strategies များကို အလွယ်တကူ ပြောင်းလဲနိုင်ခြင်း
- **Command Pattern**: Agent operations များကို undo/redo အထောက်အကူဖြင့် encapsulate
- **Observer Pattern**: Event-driven agent lifecycle management
- **Template Method**: Agent execution workflows ကို စနစ်တကျ ပြုလုပ်ခြင်း

### 3. **Structural Patterns**
- **Adapter Pattern**: GitHub Models API integration layer
- **Decorator Pattern**: Agent capability ကို တိုးချဲ့ခြင်း
- **Facade Pattern**: Agent interaction interface ကို ရိုးရှင်းစွာ ပြုလုပ်ခြင်း
- **Proxy Pattern**: Lazy loading နှင့် caching ဖြင့် performance တိုးမြှင့်ခြင်း

## ⚙️ Prerequisites & Setup

**Development Environment:**
- .NET 9.0 SDK သို့မဟုတ် အထက်
- Visual Studio 2022 သို့မဟုတ် VS Code (C# extension ဖြင့်)
- GitHub Models API access

**NuGet Dependencies:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuration (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 .NET Design Principles

### SOLID Principles
- **Single Responsibility**: Component တစ်ခုစီမှာ ရည်ရွယ်ချက်တစ်ခုသာရှိခြင်း
- **Open/Closed**: Modification မလိုအပ်ဘဲ တိုးချဲ့နိုင်ခြင်း
- **Liskov Substitution**: Interface-based tool implementations
- **Interface Segregation**: Focused, cohesive interfaces
- **Dependency Inversion**: Abstractions တွေကိုသာ အခြေခံပြီး concretions မဟုတ်

### Clean Architecture
- **Domain Layer**: Core agent နှင့် tool abstractions
- **Application Layer**: Agent orchestration နှင့် workflows
- **Infrastructure Layer**: GitHub Models integration နှင့် အပြင်ဆက်သွယ်မှုများ
- **Presentation Layer**: User interaction နှင့် response formatting

## 🔒 Enterprise Considerations

### Security
- **Credential Management**: IConfiguration ဖြင့် API key ကို လုံခြုံစွာ စီမံခြင်း
- **Input Validation**: Strong typing နှင့် data annotation validation
- **Output Sanitization**: Response ကို လုံခြုံစွာ စစ်ဆေးခြင်းနှင့် filtering
- **Audit Logging**: Operation tracking ကို စုံလင်စွာ ပြုလုပ်ခြင်း

### Performance
- **Async Patterns**: Non-blocking I/O operations
- **Connection Pooling**: HTTP client ကို ထိရောက်စွာ စီမံခြင်း
- **Caching**: Response caching ဖြင့် performance တိုးမြှင့်ခြင်း
- **Resource Management**: Disposal နှင့် cleanup patterns ကို သေချာစွာ ပြုလုပ်ခြင်း

### Scalability
- **Thread Safety**: Concurrent agent execution ကို ထောက်ပံ့ခြင်း
- **Resource Pooling**: Resource များကို ထိရောက်စွာ အသုံးပြုခြင်း
- **Load Management**: Rate limiting နှင့် backpressure handling
- **Monitoring**: Performance metrics နှင့် health checks

## 🚀 Production Deployment

- **Configuration Management**: Environment-specific settings
- **Logging Strategy**: Correlation IDs ဖြင့် structured logging
- **Error Handling**: Global exception handling နှင့် proper recovery
- **Monitoring**: Application insights နှင့် performance counters
- **Testing**: Unit tests, integration tests, နှင့် load testing patterns

Enterprise-grade intelligent agents တွေကို .NET နဲ့ တည်ဆောက်ဖို့ အဆင်သင့်ဖြစ်ပါပြီလား? Robust ဖြစ်တဲ့ architecture တစ်ခုကို တည်ဆောက်ကြစို့! 🏢✨

## Code Sample

အပြည့်အစုံသော အလုပ်လုပ်နိုင်တဲ့ နမူနာကို [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) တွင် ကြည့်ရှုပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။