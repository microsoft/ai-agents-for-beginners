# 🎯 Azure OpenAI (Responses API) ဖြင့် စီမံကိန်းရေးဆွဲခြင်းနှင့် ဒီဇိုင်းပုံစံများ (.NET)

## 📋 သင်ယူရယူရန် ရည်ရွယ်ချက်များ

ဤ notebook သည် .NET တွင် Microsoft Agent Framework ကို အသုံးပြု၍ Azure OpenAI (Responses API) ဖြင့် အမြင့်မားဆုံး အဆင့်ရှိ စမတ်တုံ့ပြန်သူများ ဖန်တီးရာအတွက် စီမံကိန်းရေးဆွဲခြင်းနှင့် ဒီဇိုင်းပုံစံများကို ဖော်ပြသည်။ သင်သည် ကိစ္စရှုပ်ထွေးမှုများကို ခွဲခြမ်းစိတ်ဖြာပြီး၊ အဆင့်များစွာဖြင့် ဖြေရှင်းချက်များ ကျင်းပနိုင်သော နည်းလမ်းများ ဦးဆောင်ပြီး၊ .NET ၏ စီးပွားရေးအင်အားများဖြင့် ရှုပ်ထွေးသော စနစ်တကျ လည်ပတ်မှုများအကောင်အထည် ဖော်နိုင်မည်ဖြစ်သည်။

## ⚙️ မလိုအပ်သည့် အရာများနှင့် တပ်ဆင်ခြင်း

**ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်:**
- .NET 9.0 SDK သို့မဟုတ် ညီမျှသော ဗားရှင်း
- Visual Studio 2022 သို့မဟုတ် C# extension ပါဝင်သော VS Code
- Azure subscription တစ်ခု၊ Azure OpenAI ရင်းမြစ်နှင့် မော်ဒယ် deployment
- Azure CLI — `az login` ဖြင့် အကောင့် ဝင်ပါ

**လိုအပ်သော ဆောင်ရွက်ရမည့် ပေါင်းစပ်ပစ္စည်းများ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**ပတ်ဝန်းကျင် ဆက်တင် (.env ဖိုင်):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## ကုဒ်ကို မှန်မှန်ကန်ကန် လည်ပတ်ခြင်း

ဤသင်ခန်းစာတွင် .NET Single File App အကောင်အထည်ဖော်မှု ပါဝင်သည်။ လည်ပတ်ရန်:

```bash
# ဖိုင်ကို လည်ပတ်နိုင်အောင် ပြုလုပ်ပါ (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# အပလီ케ေးရှင်းကို ဖြည့်ဆောင်ပါ
./07-dotnet-agent-framework.cs
```

သို့မဟုတ် dotnet run command ကို အသုံးပြုပါ:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## ကုဒ် အကောင်အထည်ဖော်မှု

အပြည့်အစုံအောက်ပါ `07-dotnet-agent-framework.cs` တွင် ရနိုင်ပြီး အောက်ပါအချက်များကို ဖော်ပြသည်-

- DotNetEnv ဖြင့် ပတ်ဝန်းကျင် ဆက်တင်များ ကို စတင်သွင်းယူခြင်း
- Responses API အတွက် Azure OpenAI client ကို စီမံခြင်း
- JSON serialization ဖြင့် ဖေါ်ပြထားသော ဒေတာပုံစံများ (Plan နှင့် TravelPlan) ကို သတ်မှတ်ခြင်း
- JSON schema ဖြင့် ဖွဲ့စည်းထားသော output ရှိ AI agent တစ်ယောက် ဖန်တီးခြင်း
- အမျိုးအစားလုံခြုံသော တုံ့ပြန်ချက်များဖြင့် စီမံကိန်း မေးမြန်းချက်များ ဆောင်ရွက်ခြင်း

## အဓိက အယူအဆများ

### အမျိုးအစားအာမခံထားသော ပုံစံများဖြင့် စနစ်တကျ စီမံခြင်း

agent သည် စီမံကိန်း output များ၏ ဖွဲ့စည်းမှုကို C# ဗဟုသုတများဖြင့် သတ်မှတ်သည်။

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

### ဖွဲ့စည်းထားသော output များအတွက် JSON Schema

agent သည် TravelPlan schema နှင့် ကိုက်ညီသော တုံ့ပြန်မှုများ ပေးပို့ရန် ဆောင်ရွက်ထားသည်။

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

### စီမံကိန်း agent အတွက် လမ်းညွှန်ချက်များ

agent သည် ရုံးတည်းဖြတ်သူတစ်ယောက်အဖြစ် အထူးပြု စွမ်းဆောင်သူများသို့ တာဝန်ပေးအပ်သည်။

- FlightBooking: လေယာဉ်လိုင်း သတင်းအချက်အလက်နှင့် လေယာဉ်မှတ်ပုံတင်ခြင်းအတွက်
- HotelBooking: ဟိုတယ် စီစဉ်ခြင်းနှင့် သတင်းအချက်အလက်ပေးခြင်းအတွက်
- CarRental: ကားငှားရမ်းခြင်းနှင့် သတင်းအချက်အလက်ပေးခြင်းအတွက်
- ActivitiesBooking: လှုပ်ရှားမှုများ စီစဉ်ပြီး သတင်းပေးခြင်းအတွက်
- DestinationInfo: ခရီးစင်တာများအကြောင်း သတင်းပေးခြင်းအတွက်
- DefaultAgent: ပုံမှန် တောင်းဆိုမှုများကို ကိုင်တွယ်ရန်

## မျှော်မှန်းထားသည့် အဖြေ

ခရီးစဉ် စီမံကိန်း တောင်းဆိုချက်ဖြင့် agent ကို လည်ပတ်စဉ်၊ တောင်းဆိုချက်ကို ခွဲခြမ်းစိတ်ဖြာပြီး အထူးပြုထားသော agent များသို့ တာဝန်များ ခွဲဝေပေးသည့် စနစ်တကျ စီမံကိန်းကို TravelPlan schema နှင့် ကိုက်ညီသော JSON ပုံစံဖြင့် ပြန်လည်ထုတ်ပေးမည်ဖြစ်သည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->