<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T10:00:17+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "my"
}
-->
# 🎯 GitHub Models (.NET) ဖြင့် အစီအစဉ်ရေးဆွဲခြင်းနှင့် ဒီဇိုင်းပုံစံများ

## 📋 သင်ယူရမည့် ရည်ရွယ်ချက်များ

ဒီ notebook သည် Microsoft Agent Framework ကို .NET နှင့် GitHub Models အသုံးပြု၍ ဉာဏ်ရည်ရှိသော Agent များကို တည်ဆောက်ရန်အတွက် စီးပွားရေးအဆင့်အစီအစဉ်ရေးဆွဲခြင်းနှင့် ဒီဇိုင်းပုံစံများကို ပြသသည်။ သင်သည် ရှုပ်ထွေးသော ပြဿနာများကို ခွဲခြမ်းစိတ်ဖြာနိုင်သော Agent များကို ဖန်တီးခြင်း၊ အဆင့်များစွာဖြင့် ဖြေရှင်းရန်အစီအစဉ်ရေးဆွဲခြင်းနှင့် .NET ၏ စီးပွားရေးအင်္ဂါရပ်များဖြင့် အလုပ်လုပ်ဆောင်နိုင်သော Workflow များကို ဖန်တီးခြင်းကို သင်ယူနိုင်ပါမည်။

## ⚙️ လိုအပ်ချက်များနှင့် Setup

**ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်:**
- .NET 9.0 SDK သို့မဟုတ် အထက်
- Visual Studio 2022 သို့မဟုတ် VS Code (C# extension ဖြင့်)
- GitHub Models API အထောက်အပံ့

**လိုအပ်သော Dependencies:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**ပတ်ဝန်းကျင်ဖိုင် (.env file) ကို ပြင်ဆင်ခြင်း:**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## ကုဒ်ကို အလုပ်လုပ်စေခြင်း

ဒီသင်ခန်းစာတွင် .NET Single File App အကောင်အထည်ဖော်မှု ပါဝင်သည်။ အလုပ်လုပ်စေရန်:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

သို့မဟုတ် dotnet run command ကို အသုံးပြုပါ:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## ကုဒ်အကောင်အထည်ဖော်မှု

`07-dotnet-agent-framework.cs` တွင် အပြည့်အစုံအကောင်အထည်ဖော်မှုကို တွေ့နိုင်ပြီး အောက်ပါအရာများကို ပြသသည်-

- DotNetEnv ဖြင့် ပတ်ဝန်းကျင်ဖိုင်ကို Load လုပ်ခြင်း
- GitHub Models အတွက် OpenAI client ကို Configure လုပ်ခြင်း
- JSON serialization ဖြင့် structured data models (Plan နှင့် TravelPlan) ကို သတ်မှတ်ခြင်း
- JSON schema အသုံးပြု structured output ဖြင့် AI agent တစ်ခုကို ဖန်တီးခြင်း
- Type-safe responses ဖြင့် planning requests ကို အကောင်အထည်ဖော်ခြင်း

## အဓိကအကြောင်းအရာများ

### Type-Safe Models ဖြင့် Structured Planning

Agent သည် planning outputs ၏ ဖွဲ့စည်းပုံကို သတ်မှတ်ရန် C# classes ကို အသုံးပြုသည်-

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### Structured Outputs အတွက် JSON Schema

Agent သည် TravelPlan schema ကို ကိုက်ညီသော response များကို ပြန်ပေးရန် Configure လုပ်ထားသည်-

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Planning Agent အညွှန်းများ

Agent သည် အထူး sub-agents များကို တာဝန်ပေးအပ်သော Coordinator အဖြစ် လုပ်ဆောင်သည်-

- FlightBooking: လေယာဉ်များကို Booking လုပ်ခြင်းနှင့် လေယာဉ်အချက်အလက်ပေးခြင်း
- HotelBooking: ဟိုတယ်များကို Booking လုပ်ခြင်းနှင့် ဟိုတယ်အချက်အလက်ပေးခြင်း
- CarRental: ကားများကို ငှားခြင်းနှင့် ကားငှားခြင်းအချက်အလက်ပေးခြင်း
- ActivitiesBooking: လှုပ်ရှားမှုများကို Booking လုပ်ခြင်းနှင့် လှုပ်ရှားမှုအချက်အလက်ပေးခြင်း
- DestinationInfo: သွားရောက်မည့်နေရာများအကြောင်းအချက်အလက်ပေးခြင်း
- DefaultAgent: အထွေထွေတောင်းဆိုမှုများကို ကိုင်တွယ်ခြင်း

## မျှော်လင့်ရသော Output

Travel planning request တစ်ခုဖြင့် Agent ကို အလုပ်လုပ်စေသောအခါ၊ အဆိုပါ request ကို ခွဲခြမ်းစိတ်ဖြာပြီး TravelPlan schema ကို ကိုက်ညီသော JSON အဖြစ် ဖွဲ့စည်းထားသော အစီအစဉ်တစ်ခုကို ဖန်တီးပြီး အထူး sub-agents များကို သင့်တော်သော Task Assignment များပေးအပ်ပါမည်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။