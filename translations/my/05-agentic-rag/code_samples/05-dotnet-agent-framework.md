<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:10:48+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "my"
}
-->
# 🔍 Azure AI Foundry (.NET) ဖြင့် Enterprise RAG

## 📋 သင်ယူရမည့်အရာများ

ဒီ notebook က Microsoft Agent Framework ကို .NET နှင့် Azure AI Foundry တွင် အသုံးပြု၍ Enterprise-grade Retrieval-Augmented Generation (RAG) စနစ်များကို တည်ဆောက်ပုံကို ပြသထားပါတယ်။ သင်သည် စက်မှုလုပ်ငန်းအဆင့်အတန်းရှိသော agent များကို ဖန်တီးနိုင်ပြီး၊ စာရွက်စာတမ်းများကို ရှာဖွေပြီး အကျိုးရှိသော၊ အကြောင်းအရာနှင့်သက်ဆိုင်သော အဖြေများကို လုံခြုံမှုနှင့် အတိုင်းအတာကျသောစနစ်ဖြင့် ပေးနိုင်မည်ဖြစ်သည်။

**သင်တည်ဆောက်မည့် Enterprise RAG စွမ်းရည်များ:**
- 📚 **စာရွက်စာတမ်းအာရုံခံမှု**: Azure AI ဝန်ဆောင်မှုများဖြင့် အဆင့်မြင့်စာရွက်စာတမ်းများကို အလုပ်လုပ်စေခြင်း
- 🔍 **Semantic ရှာဖွေမှု**: စက်မှုလုပ်ငန်းအဆင့်အတန်းရှိ vector ရှာဖွေမှု
- 🛡️ **လုံခြုံမှုပေါင်းစည်းမှု**: အခန်းကဏ္ဍအလိုက် ဝင်ခွင့်နှင့် ဒေတာကာကွယ်မှုပုံစံများ
- 🏢 **အတိုင်းအတာကျသော Architecture**: စက်မှုလုပ်ငန်းအဆင့် RAG စနစ်များကို စောင့်ကြည့်မှုနှင့်အတူ

## 🎯 Enterprise RAG Architecture

### စက်မှုလုပ်ငန်းအဆင့်အတန်းရှိ အစိတ်အပိုင်းများ
- **Azure AI Foundry**: လုံခြုံမှုနှင့်လိုက်နာမှုရှိသော စက်မှုလုပ်ငန်း AI ပလက်ဖောင်း
- **Persistent Agents**: စကားဝိုင်းသမိုင်းနှင့် အကြောင်းအရာစီမံခန့်ခွဲမှုရှိသော Stateful agents
- **Vector Store Management**: စက်မှုလုပ်ငန်းအဆင့်စာရွက်စာတမ်းများကို အညွှန်းနှင့် ရှာဖွေမှု
- **Identity Integration**: Azure AD အတည်ပြုမှုနှင့် အခန်းကဏ္ဍအလိုက် ဝင်ခွင့်ထိန်းချုပ်မှု

### .NET စက်မှုလုပ်ငန်းအကျိုးကျေးဇူးများ
- **Type Safety**: RAG လုပ်ဆောင်မှုများနှင့် ဒေတာဖွဲ့စည်းမှုများအတွက် Compile-time အတည်ပြုမှု
- **Async Performance**: စာရွက်စာတမ်းများကို Non-blocking အလုပ်လုပ်စေခြင်း
- **Memory Management**: စာရွက်စာတမ်းစုစည်းမှုများအတွက် အရင်းအမြစ်အသုံးပြုမှုကို ထိရောက်စွာစီမံခန့်ခွဲခြင်း
- **Integration Patterns**: Azure ဝန်ဆောင်မှုများနှင့် Dependency Injection ကို သဘာဝကျသောပေါင်းစည်းမှု

## 🏗️ နည်းပညာဆိုင်ရာ Architecture

### Enterprise RAG Pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### .NET အဓိကအစိတ်အပိုင်းများ
- **Azure.AI.Agents.Persistent**: စက်မှုလုပ်ငန်း agent စီမံခန့်ခွဲမှုနှင့် အခြေအနေထိန်းသိမ်းမှု
- **Azure.Identity**: Azure ဝန်ဆောင်မှုများကို လုံခြုံစွာဝင်ရောက်နိုင်ရန် အတည်ပြုမှု
- **Microsoft.Agents.AI.AzureAI**: Azure အတွက် အထူးပြု agent framework အကောင်အထည်ဖော်မှု
- **System.Linq.Async**: အမြင့်ဆုံးစွမ်းဆောင်ရည်ရှိသော asynchronous LINQ လုပ်ဆောင်မှုများ

## 🔧 Enterprise Features & Benefits

### လုံခြုံမှုနှင့်လိုက်နာမှု
- **Azure AD Integration**: စက်မှုလုပ်ငန်း identity စီမံခန့်ခွဲမှုနှင့် အတည်ပြုမှု
- **Role-Based Access**: စာရွက်စာတမ်းဝင်ခွင့်နှင့် လုပ်ဆောင်မှုများအတွက် အခန်းကဏ္ဍအလိုက် ခွင့်ပြုချက်များ
- **Data Protection**: အရေးကြီးသောစာရွက်စာတမ်းများအတွက် Encryption at rest နှင့် in transit
- **Audit Logging**: လိုက်နာမှုလိုအပ်ချက်များအတွက် လုပ်ဆောင်မှုများကို စုံလင်စွာ မှတ်တမ်းတင်ခြင်း

### စွမ်းဆောင်ရည်နှင့်အတိုင်းအတာကျမှု
- **Connection Pooling**: Azure ဝန်ဆောင်မှုများကို ထိရောက်စွာ ချိတ်ဆက်မှုစီမံခန့်ခွဲခြင်း
- **Async Processing**: အမြင့် throughput အခြေအနေများအတွက် Non-blocking လုပ်ဆောင်မှုများ
- **Caching Strategies**: မကြာခဏအသုံးပြုသောစာရွက်စာတမ်းများအတွက် caching
- **Load Balancing**: အကြီးစား deployment များအတွက် ဖြန့်ဖြူးလုပ်ဆောင်မှု

### စီမံခန့်ခွဲမှုနှင့် စောင့်ကြည့်မှု
- **Health Checks**: RAG စနစ်အစိတ်အပိုင်းများအတွက် monitoring
- **Performance Metrics**: ရှာဖွေမှုအရည်အသွေးနှင့် အဖြေချိန်များအပေါ် analytics
- **Error Handling**: Exception စီမံခန့်ခွဲမှုနှင့် retry policies
- **Configuration Management**: ပတ်ဝန်းကျင်-specific ဆက်တင်များနှင့် အတည်ပြုမှု

## ⚙️ လိုအပ်ချက်များနှင့် Setup

**ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်:**
- .NET 9.0 SDK သို့မဟုတ် အထက်
- Visual Studio 2022 သို့မဟုတ် VS Code (C# extension ဖြင့်)
- Azure subscription (AI Foundry access ပါဝင်)

**လိုအပ်သော NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure Authentication Setup:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**ပတ်ဝန်းကျင် Configuration:**
* Azure AI Foundry configuration (Azure CLI မှတဆင့် အလိုအလျောက် စီမံခန့်ခွဲသည်)
* သင်သည် သင့် Azure subscription မှန်ကန်စွာ authenticated ဖြစ်ကြောင်း သေချာပါ

## 📊 Enterprise RAG Patterns

### စာရွက်စာတမ်းစီမံခန့်ခွဲမှု Patterns
- **Bulk Upload**: စာရွက်စာတမ်းစုစည်းမှုများကို ထိရောက်စွာ အလုပ်လုပ်စေခြင်း
- **Incremental Updates**: စာရွက်စာတမ်းများကို အချိန်နှင့်တပြေးညီ ထည့်သွင်းခြင်းနှင့် ပြင်ဆင်ခြင်း
- **Version Control**: စာရွက်စာတမ်းများကို versioning နှင့် ပြောင်းလဲမှု tracking
- **Metadata Management**: စာရွက်စာတမ်း attributes နှင့် taxonomy

### ရှာဖွေမှုနှင့် ရယူမှု Patterns
- **Hybrid Search**: Semantic နှင့် keyword ရှာဖွေမှုကို ပေါင်းစပ်၍ အကောင်းဆုံးရလဒ်ရရှိစေခြင်း
- **Faceted Search**: အမျိုးအစားများအလိုက် filtering နှင့် categorization
- **Relevance Tuning**: domain-specific လိုအပ်ချက်များအတွက် scoring algorithms
- **Result Ranking**: စီးပွားရေး logic integration ဖြင့် အဆင့်သတ်မှတ်ခြင်း

### လုံခြုံမှု Patterns
- **Document-Level Security**: စာရွက်စာတမ်းတစ်ခုချင်းစီအတွက် ဝင်ခွင့်ထိန်းချုပ်မှု
- **Data Classification**: sensitivity labeling နှင့် ကာကွယ်မှုကို အလိုအလျောက်လုပ်ဆောင်ခြင်း
- **Audit Trails**: RAG လုပ်ဆောင်မှုများအားလုံးကို စုံလင်စွာ မှတ်တမ်းတင်ခြင်း
- **Privacy Protection**: PII detection နှင့် redaction စွမ်းရည်များ

## 🔒 Enterprise လုံခြုံမှု Features

### Authentication & Authorization
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Data Protection
- **Encryption**: စာရွက်စာတမ်းများနှင့် ရှာဖွေမှု indices အတွက် အဆုံးမှအဆုံး encryption
- **Access Controls**: အသုံးပြုသူနှင့်အဖွဲ့ခွင့်ပြုချက်များအတွက် Azure AD integration
- **Data Residency**: လိုက်နာမှုအတွက် ဒေတာတည်နေရာထိန်းချုပ်မှု
- **Backup & Recovery**: အလိုအလျောက် backup နှင့် disaster recovery စွမ်းရည်များ

## 📈 စွမ်းဆောင်ရည်တိုးတက်မှု

### Async Processing Patterns
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Memory Management
- **Streaming Processing**: စာရွက်စာတမ်းများကို memory ပြဿနာမရှိအောင် စီမံခန့်ခွဲခြင်း
- **Resource Pooling**: အရင်းအမြစ်များကို ထိရောက်စွာ အသုံးပြုခြင်း
- **Garbage Collection**: memory allocation patterns ကို အကောင်းဆုံးလုပ်ဆောင်ခြင်း
- **Connection Management**: Azure ဝန်ဆောင်မှု connection lifecycle ကို သေချာစီမံခြင်း

### Caching Strategies
- **Query Caching**: မကြာခဏလုပ်ဆောင်သော ရှာဖွေမှုများကို cache
- **Document Caching**: frequently accessed စာရွက်စာတမ်းများအတွက် in-memory caching
- **Index Caching**: vector index caching ကို optimize
- **Result Caching**: intelligent caching of generated responses

## 📊 Enterprise Use Cases

### Knowledge Management
- **Corporate Wiki**: ကုမ္ပဏီ knowledge bases အတွင်း intelligent ရှာဖွေမှု
- **Policy & Procedures**: လိုက်နာမှုနှင့် procedure အကြံပေးမှုကို အလိုအလျောက်လုပ်ဆောင်ခြင်း
- **Training Materials**: သင်ကြားမှုနှင့် ဖွံ့ဖြိုးမှုအကူအညီ
- **Research Databases**: သုတေသနနှင့် စာတမ်းများကို analysis လုပ်ခြင်း

### Customer Support
- **Support Knowledge Base**: customer service အဖြေများကို အလိုအလျောက်ပေးခြင်း
- **Product Documentation**: intelligent product information ရှာဖွေမှု
- **Troubleshooting Guides**: အကြောင်းအရာနှင့်သက်ဆိုင်သော ပြဿနာဖြေရှင်းမှုအကူအညီ
- **FAQ Systems**: စာရွက်စာတမ်းစုစည်းမှုများမှ dynamic FAQ ဖန်တီးခြင်း

### Regulatory Compliance
- **Legal Document Analysis**: စာချုပ်နှင့် ဥပဒေစာရွက်စာတမ်း intelligence
- **Compliance Monitoring**: လိုက်နာမှုကို အလိုအလျောက်စစ်ဆေးခြင်း
- **Risk Assessment**: စာရွက်စာတမ်းအခြေခံ risk analysis နှင့် reporting
- **Audit Support**: audit များအတွက် intelligent စာရွက်စာတမ်းရှာဖွေမှု

## 🚀 Production Deployment

### Monitoring & Observability
- **Application Insights**: telemetry နှင့် စွမ်းဆောင်ရည် monitoring
- **Custom Metrics**: စီးပွားရေး-specific KPI tracking နှင့် alerting
- **Distributed Tracing**: ဝန်ဆောင်မှုများအတွင်း request tracking
- **Health Dashboards**: စနစ် health နှင့် စွမ်းဆောင်ရည် visualization

### Scalability & Reliability
- **Auto-Scaling**: load နှင့် စွမ်းဆောင်ရည် metrics အပေါ်အခြေခံပြီး အလိုအလျောက် scaling
- **High Availability**: multi-region deployment နှင့် failover စွမ်းရည်များ
- **Load Testing**: စက်မှုလုပ်ငန်း load အခြေအနေများအောက်တွင် စွမ်းဆောင်ရည်စစ်ဆေးခြင်း
- **Disaster Recovery**: backup နှင့် recovery လုပ်ဆောင်မှုများကို အလိုအလျောက်လုပ်ဆောင်ခြင်း

စက်မှုလုပ်ငန်းအဆင့်အတန်းရှိ RAG စနစ်များကို sensitive စာရွက်စာတမ်းများကို အတိုင်းအတာကျစွာ စီမံနိုင်ရန် အဆင့်မြင့် knowledge systems များကို architect လုပ်ကြစို့! 🏢📖✨

## Code Implementation

ဒီသင်ခန်းစာအတွက် အပြည့်အစုံအလုပ်လုပ်သော code sample ကို `05-dotnet-agent-framework.cs` တွင် ရရှိနိုင်ပါသည်။

ဥပမာကို run လုပ်ရန်:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

သို့မဟုတ် `dotnet run` ကို တိုက်ရိုက်အသုံးပြုပါ:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

ဒီ code က ပြသထားသည်မှာ:

1. **Package Installation**: Azure AI Agents အတွက်လိုအပ်သော NuGet packages ကို install လုပ်ခြင်း
2. **Environment Configuration**: Azure AI Foundry endpoint နှင့် model settings ကို load လုပ်ခြင်း
3. **Document Upload**: RAG လုပ်ဆောင်မှုအတွက် စာရွက်စာတမ်းတစ်ခုကို upload လုပ်ခြင်း
4. **Vector Store Creation**: semantic ရှာဖွေမှုအတွက် vector store တည်ဆောက်ခြင်း
5. **Agent Configuration**: စာရွက်စာတမ်းရှာဖွေမှုစွမ်းရည်ရှိသော AI agent ကို setup လုပ်ခြင်း
6. **Query Execution**: upload လုပ်ထားသော စာရွက်စာတမ်းအပေါ် query များကို run လုပ်ခြင်း

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။