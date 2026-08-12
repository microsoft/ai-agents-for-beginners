# 🎯 الگوهای برنامه‌ریزی و طراحی با Azure OpenAI (Responses API) (.NET)

## 📋 اهداف یادگیری

این دفترچه‌کار الگوهای برنامه‌ریزی و طراحی در سطح سازمانی را برای ساخت عوامل هوشمند با استفاده از Microsoft Agent Framework در .NET با Azure OpenAI (Responses API) نشان می‌دهد. شما می‌آموزید که چگونه عواملی بسازید که می‌توانند مسائل پیچیده را تجزیه کنند، راه‌حل‌های چند مرحله‌ای برنامه‌ریزی کنند، و فرایندهای پیچیده را با ویژگی‌های سازمانی .NET اجرا کنند.

## ⚙️ پیش‌نیازها و راه‌اندازی

**محیط توسعه:**
- .NET 9.0 SDK یا بالاتر
- Visual Studio 2022 یا VS Code همراه با افزونه C#
- یک اشتراک Azure با منبع Azure OpenAI و استقرار مدل
- Azure CLI — ورود با فرمان `az login`

**وابستگی‌های مورد نیاز:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**پیکربندی محیط (.env file):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## اجرای کد

این درس شامل پیاده‌سازی برنامه تک‌فایلی .NET است. برای اجرای آن:

```bash
# فایل را اجرایی کنید (لینوکس/مک‌اواس)
chmod +x 07-dotnet-agent-framework.cs

# برنامه را اجرا کنید
./07-dotnet-agent-framework.cs
```

یا از فرمان dotnet run استفاده کنید:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## پیاده‌سازی کد

پیاده‌سازی کامل در `07-dotnet-agent-framework.cs` موجود است که نشان می‌دهد:

- بارگذاری پیکربندی محیط با DotNetEnv
- پیکربندی کلاینت Azure OpenAI و ایجاد عامل هوش مصنوعی با استفاده از `GetChatClient().AsAIAgent()`
- تعریف مدل‌های داده ساخت‌یافته (Plan و TravelPlan) با سریال‌سازی JSON
- ایجاد عامل هوش مصنوعی با خروجی ساخت‌یافته با استفاده از JSON schema
- اجرای درخواست‌های برنامه‌ریزی با پاسخ‌های نوع-ایمن

## مفاهیم کلیدی

### برنامه‌ریزی ساختاریافته با مدل‌های نوع-ایمن

عامل از کلاس‌های C# برای تعریف ساختار خروجی‌های برنامه‌ریزی استفاده می‌کند:

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

### JSON Schema برای خروجی‌های ساخت‌یافته

عامل به گونه‌ای پیکربندی شده است که پاسخ‌هایی مطابق با طرح TravelPlan بازگرداند:

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

### دستورالعمل‌های عامل برنامه‌ریزی

عامل به عنوان هماهنگ‌کننده عمل می‌کند و وظایف را به زیرعامل‌های تخصصی واگذار می‌کند:

- FlightBooking: برای رزرو پروازها و ارائه اطلاعات پرواز
- HotelBooking: برای رزرو هتل‌ها و ارائه اطلاعات هتل
- CarRental: برای رزرو خودرو و ارائه اطلاعات اجاره خودرو
- ActivitiesBooking: برای رزرو فعالیت‌ها و ارائه اطلاعات مربوط به فعالیت‌ها
- DestinationInfo: برای ارائه اطلاعات درباره مقاصد
- DefaultAgent: برای رسیدگی به درخواست‌های عمومی

## خروجی مورد انتظار

زمانی که عامل را با یک درخواست برنامه‌ریزی سفر اجرا کنید، درخواست را تحلیل کرده و یک برنامه ساختاریافته با تخصیص مناسب وظایف به عامل‌های تخصصی تولید می‌کند، قالب‌بندی شده به صورت JSON که با طرح TravelPlan مطابقت دارد.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->