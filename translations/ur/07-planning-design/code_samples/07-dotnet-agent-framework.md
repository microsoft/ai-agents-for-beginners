# 🎯 ایزور اوپن اے آئی (Responses API) کے ساتھ منصوبہ بندی اور ڈیزائن پیٹرنز (.NET)

## 📋 سیکھنے کے مقاصد

یہ نوٹ بک مائیکروسافٹ ایجنٹ فریم ورک کو .NET میں ایزور اوپن اے آئی (Responses API) کے ساتھ استعمال کرتے ہوئے ذہین ایجنٹس بنانے کے لئے انٹرپرائز درجے کی منصوبہ بندی اور ڈیزائن پیٹرنز دکھاتی ہے۔ آپ سیکھیں گے کہ ایسے ایجنٹس کیسے بنائیں جو پیچیدہ مسائل کو توڑ سکیں، کثیر مرحلہ حل کی منصوبہ بندی کر سکیں، اور .NET کی انٹرپرائز خصوصیات کے ساتھ پیچیدہ ورک فلو کو انجام دے سکیں۔

## ⚙️ ضروریات اور ترتیب

**ڈیولپمنٹ کا ماحول:**
- .NET 9.0 SDK یا اس سے اوپر
- Visual Studio 2022 یا VS Code C# ایکسٹینشن کے ساتھ
- ایک ایزور سبسکرپشن جس میں ایزور اوپن اے آئی ریسورس اور ماڈل ڈپلائمنٹ ہو
- ایزور CLI — `az login` کے ذریعے سائن ان کریں

**ضروری ڈیپنڈنسیز:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**ماحول کی ترتیب (.env فائل):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## کوڈ چلانا

یہ سبق ایک .NET سنگل فائل ایپ کی امپلیمینٹیشن شامل کرتا ہے۔ اسے چلانے کے لئے:

```bash
# فائل کو قابلِ اجرا بنائیں (لینکس/میک او ایس)
chmod +x 07-dotnet-agent-framework.cs

# ایپلیکیشن چلائیں
./07-dotnet-agent-framework.cs
```

یا dotnet run کمانڈ استعمال کریں:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## کوڈ کی امپلیمینٹیشن

مکمل امپلیمینٹیشن `07-dotnet-agent-framework.cs` میں دستیاب ہے، جو یہ دکھاتی ہے:

- DotNetEnv کے ساتھ ماحول کی ترتیب لوڈ کرنا
- Azure OpenAI کلائنٹ کی ترتیب اور `GetChatClient().AsAIAgent()` کے ذریعے AI ایجنٹ بنانا
- JSON سیریلائزیشن کے ساتھ ساختہ ڈیٹا ماڈلز (Plan اور TravelPlan) کی تعریف کرنا
- JSON اسکیمہ کے ذریعے ساختہ آؤٹ پٹ کے ساتھ AI ایجنٹ بنانا
- ٹائپ-سیف جوابات کے ساتھ منصوبہ بندی کی درخواستیں انجام دینا

## کلیدی تصورات

### ٹائپ-سیف ماڈلز کے ساتھ ساختہ منصوبہ بندی

ایجنٹ منصوبہ بندی کے آؤٹ پٹس کی ساخت کو C# کلاسز کے ذریعے بیان کرتا ہے:

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

### ساختہ آؤٹ پٹس کے لئے JSON اسکیمہ

ایجنٹ کو اس بات کی ترتیب دی گئی ہے کہ وہ TravelPlan اسکیمہ سے مطابقت رکھنے والے جوابات دے:

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

### منصوبہ بندی ایجنٹ کی ہدایات

ایجنٹ بطور کوآرڈینیٹر کام کرتا ہے، اور مخصوص سب-ایجنٹس کو کام تفویض کرتا ہے:

- FlightBooking: پروازیں بک کرنے اور پرواز کی معلومات فراہم کرنے کے لئے
- HotelBooking: ہوٹلز بک کرنے اور ہوٹل کی معلومات فراہم کرنے کے لئے
- CarRental: گاڑیاں کرایہ پر لینے اور کرایہ کار کی معلومات کے لئے
- ActivitiesBooking: سرگرمیاں بک کرنے اور سرگرمی کی معلومات دینے کے لئے
- DestinationInfo: مقامات کی معلومات فراہم کرنے کے لئے
- DefaultAgent: عمومی درخواستوں کو سنبھالنے کے لئے

## متوقع نتیجہ

جب آپ ایجنٹ کو ایک سفر کی منصوبہ بندی کی درخواست کے ساتھ چلائیں گے، تو یہ درخواست کا تجزیہ کرے گا اور مخصوص ایجنٹس کو مناسب کام تفویض کرتے ہوئے ایک ساختہ منصوبہ تخلیق کرے گا، جو JSON کی شکل میں TravelPlan اسکیمہ کے مطابق ہوگا۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->