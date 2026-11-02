# 🎯 Azure OpenAI (Responses API) ( .NET) ဖြင့် စီမံကိန်းချမှတ်ခြင်းနှင့် ဒီဇိုင်းပုံစံများ

## 📋 သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီနုတ်ဘုတ်ရွက်သည် .NET တွင် Microsoft Agent Framework ကိုအသုံးပြုကာ Azure OpenAI (Responses API) ဖြင့် စျေးကွက်အဆင့်မီ စီမံကိန်းခြင်းနှင့် ဒီဇိုင်းပုံစံများကို ဆောက်လုပ်ရာတွင် ကိုယ်ပိုင်ဗဟုသုတ Agents များဖန်တီးနည်းကို ပြသသည်။ သင်သည် ပြဿနာရှုပ်ထွေးမှုများကိုခွဲခြမ်းစိတ်ဖြာနိုင်သော၊ နောက်တစ်ဆင့်တွင်ဖြေရှင်းချက်များ စီစဉ်နိုင်သော နှင့် .NET ၏စျေးကွက်အဆင့်အင်္ဂါရပ်များဖြင့် ရှုပ်ထွေးသောလုပ်ငန်းစဉ်များကို ဆောင်ရွက်နိုင်သော Agent များ ဖန်တီးနည်းကို သင်ယူမည်ဖြစ်သည်။

## ⚙️ မလိုအပ်သော အချက်အလက်များနှင့် ပြင်ဆင်မှု

**တိုးတက်မှု ပတ်ဝန်းကျင်:**
- .NET 9.0 SDK သို့မဟုတ် အထက်တန်း
- Visual Studio 2022 သို့မဟုတ် VS Code C# extension ဖြင့်
- Azure subscription တစ်ခု၊ Azure OpenAI resource နှင့် မော်ဒယ် တပ်ဆင်မှုတစ်ခု
- Azure CLI — `az login` ဖြင့် ဝင်ရောက်ချိတ်ဆက်ခြင်း

**လိုအပ်သော စဉ်ဆက်အလိုက်များ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**ပတ်ဝန်းကျင် တပ်ဆင်မှု (.env ဖိုင်):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## ကုဒ်ကို ပြေးဆွဲခြင်း

ဒီသင်ခန်းစာတွင် .NET Single File App အသုံးပြုထားသည်။ အသုံးပြုရန်:

```bash
# ဖိုင်ကို အလုပ်လုပ်နိုင်အောင် ပြုလုပ်ပါ (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# အပလီကေးရှင်းကို ပြေးပါ
./07-dotnet-agent-framework.cs
```

ဒါမှမဟုတ် dotnet run command ကို သုံးပါ:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## ကုဒ် အကောင်အထည်ဖော်ခြင်း

အကောင်အထည်ဖော်မှု အပြည့်အစုံကို `07-dotnet-agent-framework.cs` တွင် ရနိုင်ပြီး၊ မည်သို့မှ:

- DotNetEnv ဖြင့် ပတ်ဝန်းကျင် တပ်ဆင်မှုကို တင်သွင်းခြင်း
- Azure OpenAI client ကို တပ်ဆင်ပြီး `GetChatClient().AsAIAgent()` ဖြင့် AI agent ဖန်တီးခြင်း
- JSON serialization ဖြင့် ဖွဲ့စည်းထားသော ဒေတာ မော်ဒယ်များ (Plan နှင့် TravelPlan) ကို သတ်မှတ်ခြင်း
- JSON schema အသုံးပြု၍ ဖွဲ့စည်းထားသော ထုတ်လွှင့်ချက်ရှိ AI agent တစ်ခုဖန်တီးခြင်း
- အမျိုးအစား-လုံခြုံသော ပြန်ကြားချက်များဖြင့် စီမံကိန်း တောင်းဆိုမှုများ ဆောင်ရွက်ခြင်း

## အဓိက သဘောအယူများ

### အမျိုးအစား-လုံခြုံသော မော်ဒယ်များဖြင့် ဖွဲ့စည်းထားသော စီမံကိန်းချမှတ်ခြင်း

Agent တွင် C# class များကို အသုံးပြုကာ စီမံကိန်းထုတ်လွှင့်ချက်ဖွဲ့စည်းမှုကို သတ်မှတ်သည်။

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

### ဖွဲ့စည်းထားသော ထုတ်လွှင့်ချက်များအတွက် JSON Schema

Agent သည် TravelPlan schema နှင့် ကိုက်ညီသော ပြန်ကြားချက်များ ပေးပို့ရန် တပ်ဆင်ထားသည်။

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### စီမံကိန်း Agent ၏ ညွှန်ကြားချက်များ

Agent သည် အုပ်ချုပ်ကူညီသူအဖြစ် လုပ်ဆောင်ကာ အထူးပြု sub-agent များအား တာဝန်ပေးအပ်သည်-

- FlightBooking: လေကြောင်းလက်မှတ်စာရင်းသွင်းခြင်းနှင့် လေကြောင်းအချက်အလက်ပေးခြင်း
- HotelBooking: ဟိုတယ်လက်မှတ်စာရင်းသွင်းခြင်း နှင့် ဟိုတယ်အချက်အလက်ပေးခြင်း
- CarRental: ကားငှားရန် စာရင်းသွင်းခြင်းနှင့် ကားငှားမှုအချက်အလက်ပေးခြင်း
- ActivitiesBooking: လုပ်ဆောင်မှုများစာရင်းသွင်းခြင်းနှင့် လုပ်ဆောင်မှုအချက်အလက်ပေးခြင်း
- DestinationInfo: ခရီးသွားရာနေရာအကြောင်းအချက်အလက် ပေးခြင်း
- DefaultAgent: အထွေထွေတောင်းဆိုမှုများကို ကိုင်တွယ်သည်

## မျှော်မှန်းထားသော ရလဒ်

ခရီးသွားစီမံကိန်း တောင်းဆိုမှုနှင့် Agent ကို ပြေးဆွဲသောအခါ၊ တောင်းဆိုမှုကို ခွဲခြမ်းစိစစ်ပြီး အထူးပြု agent များကို တာဝန်နှင့် ထပ်ဆောင်းထားသော ဖွဲ့စည်းထားသော စီမံကိန်းတစ်ခုကို ထုတ်ပေးမည်ဖြစ်ပြီး၊ TravelPlan schema ဖြင့် ကိုက်ညီသော JSON ပုံစံဖြင့် ဖော်ပြပါမည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->