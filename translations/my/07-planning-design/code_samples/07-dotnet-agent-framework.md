# 🎯 Azure OpenAI (Responses API) ဖြင့် စီမံခန့်ခွဲမှုနှင့် ဒီဇိုင်းပုံစံများ (.NET)

## 📋 သင်ယူရမည့်ရည်မှန်းချက်များ

ဒီ notebook သည် Microsoft Agent Framework ကိုအသုံးပြုပြီး .NET နှင့် Azure OpenAI (Responses API) အသုံးပြုပြီး အထူးပြုမြန်မာ့အင်တယ်လီဂျင့်ကို တည်ဆောက်ရာတွင် စက်မှုနယ်ပယ်အဆင့် စီမံခန့်ခွဲမှုနှင့် ဒီဇိုင်းပုံစံများကို ပြသပါသည်။ သင်သည် ရှုပ်ထွေးသောပြဿနာများကို ခွဲခြမ်းစိတ်ဖြာနိုင်သော အေးဂျင့်များ ဖန်တီးနိုင်ရန်၊ များစွာသောအဆင့်များဖြင့် အဖြေရှာနိုင်ရန် နှင့် .NET ၏ စက်မှုနယ်ပယ်အင်္ဂါရပ်များဖြင့် ချိတ်ဆက်စီမံချက်ခေါ်နှင့် မျက်နှာပြင်ကြီး workflows များ ဆောင်ရွက်နိုင်ရန် သင်ယူမည်ဖြစ်သည်။

## ⚙️ လိုအပ်ချက်များနှင့် ဆက်တင်များ

**ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်:**
- .NET 9.0 SDK သို့မဟုတ် ထက်မြင့်သောဗားရှင်း
- Visual Studio 2022 သို့မဟုတ် VS Code ကို C# နဲ့တစ်ပြိုင်နက်တည်း အသုံးပြုခြင်း
- Azure subscription တစ်ခုတွင် Azure OpenAI အရင်းအမြစ်နှင့် မော်ဒယ် deployment တည်ရှိပြီးသားဖြစ်ရန်
- Azure CLI — `az login` ဖြင့် ဝင်ရောက်ချိတ်ဆက်ရန်

**လိုအပ်သော Dependencies များ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**ပတ်ဝန်းကျင် ဖိုင် (.env ဖိုင်):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```

## ကုဒ် အလုပ်လုပ်မှု

ဒီသင်ခန်းစာမှာ .NET Single File App လုပ်ဆောင်ချက်ပါဝင်ပါတယ်။ အလုပ်လုပ်ရန်:

```bash
# ဖိုင်ကို အလုပ်လုပ်နိုင်အောင် ပြင်ဆင်ပါ (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# အပလီကေးရှင်းအား စတင်ပါ
./07-dotnet-agent-framework.cs
```

ဒါမှမဟုတ် dotnet run command ကို အသုံးပြုပါ:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## ကုဒ် ဆောင်ရွက်ချက်

အပြည့်အစုံဆောင်ရွက်ချက်ကို `07-dotnet-agent-framework.cs` မှာ တွေ့ရှုနိုင်ပြီး၊ အောက်ပါအချက်များကို ပြသပါသည်။

- DotNetEnv ဖြင့် ပတ်ဝန်းကျင်ဆက်တင်များ တင်ယူခြင်း
- Azure OpenAI client ကို ဆက်တင်ပြီး `GetChatClient().AsAIAgent()` အသုံးပြုပြီး AI agent တစ်ခု ဖန်တီးခြင်း
- JSON serialization နဲ့ ပန်းတိုင် (Plan) နှင့် ခရီးစဉ် (TravelPlan) အတွက် ဖွဲ့စည်းထားသော ဒေတာမော်ဒယ်များ သတ်မှတ်ခြင်း
- JSON schema ကို အသုံးပြုပြီး ဖွဲ့စည်းထားသော output ရှိ AI agent တစ်ခု ဖန်တီးခြင်း
- အမျိုးအစားလုံလောက်သော တုံ့ပြန်ချက်များဖြင့် စီမံချက်ပေးခြင်း ကိစ္စများ ဆောင်ရွက်ခြင်း

## အဓိကအယူအဆများ

### အမျိုးအစားလုံလောက်သော မော်ဒယ်များဖြင့် ဖွဲ့စည်းထားသော စီမံခန့်ခွဲမှု

အေးဂျင့်သည် စီမံချက် အဖြေများ၏ ဖွဲ့စည်းပုံကို C# class များဖြင့် သတ်မှတ်သည်။

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

အေးဂျင့်သည် TravelPlan schema နှင့် သဟဇာတဖြစ်သော တုံ့ပြန်ချက်များ ပြန်လည်ပေးသွားရန် ဆက်တင်ပြုလုပ်ထားသည်။

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

### စီမံခန့်ခွဲမှု အေးဂျင့် လမ်းညွှန်ချက်များ

အေးဂျင့်သည် ပူးတွဲ၏အဖြစ်ဆောင်ရွက်ပြီး ကျွမ်းကျင်သူ အေးဂျင့်သေးများကို တာဝန်အပ်ပေးသည်။

- FlightBooking: ဂြိုဟ်တုလေယာဉ်များ ကြိုက်နှစ်သက်မှုနှင့် လေယာဉ်သတင်းအချက်အလက်များ ပေးသွားခြင်း
- HotelBooking: ဟိုတယ်များ ကြိုတင်မှာယူခြင်းနှင့် ဟိုတယ် သတင်းအချက်အလက်များ ပေးသွားခြင်း
- CarRental: ကားငှားမှု ကိစ္စများ နှင့် ကားငှားသတင်းအချက်အလက် ပေးခြင်း
- ActivitiesBooking: လှုပ်ရှားမှုများ ကြိုတင်မှာယူခြင်းနှင့် လှုပ်ရှားမှုပတ်သက်သတင်းပေးခြင်း
- DestinationInfo: သွားရောက်မည့်နေရာများ အကြောင်းအရာ ပေးသွားခြင်း
- DefaultAgent: စုံစမ်းခြင်းအထူးပြု စီမံကိစ္စများကို ကိုင်တွယ်ခြင်း

## သင့်တယ်ဆိုသော ရလဒ်

ခရီးစဉ်စီမံခန့်ခွဲမှု တောင်းဆိုမှုဖြင့် အေးဂျင့်ကို ကြိုးစားပါက၊ ၎င်းသည် တောင်းဆိုမှုကို ခွဲခြမ်းစိတ်ဖြာပြီး အထူးပြု အေးဂျင့်များသို့ တာဝန် ပေးအပ်ခြင်းဖြင့် ဖွဲ့စည်းထားသော စီမံချက်တစ်ခု ထုတ်ပေးမည်ဖြစ်ပြီး၊ TravelPlan schema နှင့် ကိုက်ညီသည့် JSON ပုံစံဖြင့် ဖော်ပြမည်ဖြစ်သည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->